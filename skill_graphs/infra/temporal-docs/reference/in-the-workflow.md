# In the Workflow:
g = graph("my-graph").compile()
await g.ainvoke({...}, context=Context(user_id="alice"))
```

Your `context` object must be serializable by the configured Temporal payload converter, since it crosses the Activity
boundary.

## Continue-as-new

Long-running graphs can hit Temporal's per-Event history size limit. Use Temporal's
[continue-as-new](/develop/python/workflows/continue-as-new) to start a fresh execution while preserving the results of nodes
and tasks that have already completed.

The `cache()` helper returns the current task-result cache as a serializable dict. Pass it to `graph(name, cache=...)`
or `entrypoint(name, cache=...)` in the new run to skip re-executing nodes that already produced a result.

```python
from temporalio import workflow
from temporalio.contrib.langgraph import cache, graph

@workflow.defn
class LongRunningWorkflow:
    @workflow.run
    async def run(self, state: State, prior_cache: dict | None = None) -> State:
        g = graph("my-graph", cache=prior_cache).compile()
        # ... run some steps, then continue-as-new before history grows too large ...
        workflow.continue_as_new(args=[state, cache()])
```

## Tracing

For tracing your LangGraph Workflows and Activities, we recommend the
[Temporal LangSmith plugin](https://github.com/temporalio/sdk-python/tree/main/temporalio/contrib/langsmith). It
composes with `LangGraphPlugin` — pass both plugins to your Worker.

## Stores are not supported

LangGraph's `Store` (for example, `InMemoryStore` passed via `graph.compile(store=...)` or `@entrypoint(store=...)`)
isn't accessible inside Activity-wrapped nodes: the Store holds live state that can't cross the Activity boundary, and
Activities may run on a different worker than the Workflow. If you pass a store, the plugin logs a warning on first use
and `runtime.store` is `None` inside nodes.

Use Workflow state for per-run memory, or an external database (Postgres, Redis, etc.) configured on each worker if you
need shared memory across runs.

## Activity vs. Workflow execution

Every graph node and `@task` must specify `execute_in` — set it to `"activity"` to run as a Temporal Activity, or
`"workflow"` to run directly inside the Workflow. The plugin raises an error if you forget to set it.

`execute_in` must be set per node or task; it cannot be set in `default_activity_options`.

Understanding when to use each mode is important for correctness and durability.

### When to use an Activity

Use `execute_in: "activity"` when a node does any of the following:

- **Makes network calls** — LLM calls, HTTP requests, database queries, or any I/O. Activities can do I/O; Workflows
  cannot.
- **Has non-deterministic behavior** — anything that can return different results on re-execution (random numbers,
  current time, external data). Workflows must be deterministic.
- **Is long-running or may fail** — Activities get configurable timeouts, automatic retries, and heartbeating. If an LLM
  call times out or a service is unavailable, Temporal retries the Activity without re-running the entire Workflow.
- **Calls `interrupt()`** — LangGraph's `interrupt()` is supported in Activity nodes. The plugin serializes the
  interrupt and propagates it back to the Workflow for human-in-the-loop patterns.

### When to run in the Workflow

Use `execute_in: "workflow"` when a node:

- **Orchestrates other graphs** — a node that calls `graph("child").compile().ainvoke(state)` to dispatch to a subgraph.
  The subgraph's own nodes still run as Activities, but the orchestration logic runs in the Workflow.
- **Performs pure state transformations** — deterministic data reshaping, merging, or filtering with no I/O.
- **Is a lightweight routing step** — when a node's only job is to decide what happens next and you want to avoid the
  overhead of an Activity round-trip.

:::warning

Workflow code must be [deterministic](/develop/python/workflows/basics#workflow-logic-requirements). A node running in
the Workflow **must not** make network calls, use `random`, read the system clock, or do file I/O. Violating this causes
non-determinism errors on replay.

:::

### Where LangGraph primitives run

Not all LangGraph primitives are node functions. Some run in the Workflow context regardless of the `execute_in` setting:

| Primitive | Runs in | Notes |
| --- | --- | --- |
| Node functions | Activity or Workflow | Controlled by `execute_in` in node `metadata` (required) |
| `@task` functions | Activity or Workflow | Controlled by `execute_in` in `activity_options` (required) |
| Conditional edge functions (`add_conditional_edges`) | Workflow | Always runs in the Workflow. Must be **deterministic** and **async** (sync functions trigger `run_in_executor`, which is not allowed in the Temporal sandbox). |
| `interrupt()` | Activity | Call `interrupt()` inside Activity nodes. The plugin serializes the interrupt and propagates it to the Workflow. |
| `Command(resume=...)` | Workflow | Used from Workflow code to resume after an interrupt. |
| `InMemorySaver` checkpointer | Workflow | Runs in-process. Temporal handles durability — external checkpointers are not needed. |

:::tip

Conditional edge functions like `should_continue` must be `async def`, not plain `def`. Synchronous functions cause
LangGraph to use `run_in_executor`, which is not supported inside Temporal's Workflow sandbox.

```python
