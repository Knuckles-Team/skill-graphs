# Terminal 3: Run a research query
uv run python -m start_workflow "What are the latest advances in quantum computing?"
```

---

## Integrations

The following integrations are available for the Temporal Python SDK.
These integrations are built on the Temporal Python SDK's [Plugin system](/develop/plugins-guide), which you can also
use to build your own integrations.

<IntegrationsGrid defaultSdks={["Python"]} />

---

## LangGraph integration

Temporal's integration with [LangGraph](https://www.langchain.com/langgraph) gives your LangGraph AI agent workflows
durable execution, automatic retries, and timeouts via the Temporal platform.

The plugin supports both the LangGraph **Graph API** (`StateGraph` with nodes and edges) and the **Functional API**
(`@entrypoint` / `@task` decorators). Each graph node and task must specify whether it runs as a Temporal Activity or
directly inside the Workflow — Activity nodes get configurable timeouts and retry policies, while Workflow nodes run
inline and must be deterministic.

<ReleaseNoteHeader type="prerelease" />

Code snippets in this guide are taken from the
[LangGraph plugin samples](https://github.com/temporalio/samples-python/tree/main/langgraph_plugin). Refer to the
samples for the complete code.

## Prerequisites

- This guide assumes you are already familiar with LangGraph. If you aren't, refer to the
  [LangGraph documentation](https://langchain-ai.github.io/langgraph/) for more details.
- If you are new to Temporal, we recommend reading [Understanding Temporal](/evaluate/understanding-temporal) or taking
  the [Temporal 101](https://learn.temporal.io/courses/temporal_101/) course.
- Ensure you have set up your local development environment by following the
  [Set up your local development environment](/develop/python/set-up-your-local-python) guide. When you're done, leave the
  Temporal development server running if you want to test your code locally.

## Install the plugin

Install the Temporal Python SDK with LangGraph support (requires `temporalio` 1.27.0 or later):

```bash
uv add "temporalio[langgraph]"
```

or with pip:

```bash
pip install "temporalio[langgraph]"
```

:::note

Python 3.11 or newer is required for the Functional API (`@entrypoint` / `@task`), for `interrupt()`, and for streaming
from a node running in the Workflow. On older Python versions the plugin loads but emits a warning, and those features
will not work because LangGraph relies on `contextvars` propagation through `asyncio.create_task()`, which is only
available from Python 3.11 onward.

:::

## Graph API

The Graph API uses `StateGraph` to define nodes and edges declaratively.

### Define a graph and Workflow

Build a `StateGraph`, then retrieve it inside your Workflow with the `graph()` helper:

```python
from datetime import timedelta

from langgraph.graph import START, StateGraph
from temporalio import workflow
from temporalio.contrib.langgraph import graph

async def process_query(query: str) -> str:
    """Process a query and return a response."""
    return f"Processed: {query}"

def build_graph() -> StateGraph:
    """Construct a single-node graph."""
    g = StateGraph(str)
    g.add_node(
        "process_query",
        process_query,
        metadata={
            "execute_in": "activity",
            "start_to_close_timeout": timedelta(seconds=10),
        },
    )
    g.add_edge(START, "process_query")
    return g

@workflow.defn
class HelloWorldWorkflow:
    @workflow.run
    async def run(self, query: str) -> str:
        return await graph("hello-world").compile().ainvoke(query)
```

### Configure the Worker

Create a `LangGraphPlugin` with your graphs and pass it to the Worker:

```python

from temporalio.client import Client
from temporalio.contrib.langgraph import LangGraphPlugin
from temporalio.worker import Worker

async def main() -> None:
    client = await Client.connect("localhost:7233")
    plugin = LangGraphPlugin(graphs={"hello-world": build_graph()})

    worker = Worker(
        client,
        task_queue="langgraph-hello-world",
        workflows=[HelloWorldWorkflow],
        plugins=[plugin],
    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
```

### Set Activity options

Pass Activity options as node `metadata` when calling `add_node`. Every node must include `"execute_in"` set to either
`"activity"` or `"workflow"`; the plugin raises an error if it's missing.

```python
from datetime import timedelta
from temporalio.common import RetryPolicy

g = StateGraph(str)
g.add_node(
    "my_node",
    my_node,
    metadata={
        "execute_in": "activity",
        "start_to_close_timeout": timedelta(seconds=30),
        "retry_policy": RetryPolicy(maximum_attempts=3),
    },
)
```

:::warning

Don't pass a LangGraph `retry_policy=` to `add_node` (or `@task(retry_policy=...)`) — the plugin raises an error if you
do. Use Temporal's `RetryPolicy` via the node's `metadata` (Graph API) or `activity_options` (Functional API) instead.

:::

### Shared defaults

To apply the same Activity options across every node and task, pass `default_activity_options` to `LangGraphPlugin`.
Per-node `metadata` (Graph API) and per-task `activity_options` (Functional API) override these defaults key by key:

```python
plugin = LangGraphPlugin(
    graphs={"my-graph": g},
    default_activity_options={
        "start_to_close_timeout": timedelta(seconds=30),
        "retry_policy": RetryPolicy(maximum_attempts=3),
    },
)
```

To mitigate potential determinism bugs, `execute_in` cannot be set in `default_activity_options` — you must set it on each node or task individually.  See [Activity vs. Workflow execution](#activity-vs-workflow-execution).

## Functional API

The Functional API uses `@entrypoint` and `@task` decorators, letting you orchestrate tasks with native Python
control flow (`while`, `if/else`, `for`) rather than declaring nodes and edges.

### Define tasks and a Workflow

```python
from datetime import timedelta

from langgraph.func import entrypoint as lg_entrypoint
from langgraph.func import task
from temporalio import workflow
from temporalio.contrib.langgraph import entrypoint

@task
def agent_think(query: str, history: list[str]) -> dict:
    """Decide the next action based on query and tool history."""
    tool_results = [h for h in history if h.startswith("[Tool]")]
    if len(tool_results) < 2:
        return {"action": "tool", "tool_name": "search", "tool_input": query}
    return {"action": "final", "answer": f"Found: {'; '.join(tool_results)}"}

@task
def execute_tool(tool_name: str, tool_input: str) -> str:
    """Execute a tool by name."""
    return f"[Tool] Result for {tool_name}({tool_input})"

@lg_entrypoint()
async def react_agent(query: str) -> dict:
    """ReAct agent loop: think -> act -> observe -> repeat."""
    history: list[str] = []
    while True:
        decision = await agent_think(query, history)
        if decision["action"] == "final":
            return {"answer": decision["answer"], "steps": len(history)}
        result = await execute_tool(decision["tool_name"], decision["tool_input"])
        history.append(result)

all_tasks = [agent_think, execute_tool]

activity_options = {
    t.func.__name__: {
        "execute_in": "activity",
        "start_to_close_timeout": timedelta(seconds=30),
    }
    for t in all_tasks
}

@workflow.defn
class ReactAgentWorkflow:
    @workflow.run
    async def run(self, query: str) -> dict:
        return await entrypoint("react-agent").ainvoke(query)
```

### Configure the Worker with the Functional API

```python
from temporalio.contrib.langgraph import LangGraphPlugin

plugin = LangGraphPlugin(
    entrypoints={"react-agent": react_agent},
    tasks=all_tasks,
    activity_options=activity_options,
)

worker = Worker(
    client,
    task_queue="langgraph-react-agent",
    workflows=[ReactAgentWorkflow],
    plugins=[plugin],
)
```

## Checkpointer

If your LangGraph code requires a checkpointer (for example, if you're using interrupts), use `InMemorySaver`. Temporal
handles durability, so third-party checkpointers (like PostgreSQL or Redis) are not needed.

```python

g = graph("my-graph").compile(
    checkpointer=langgraph.checkpoint.memory.InMemorySaver(),
)
```

## Runtime context

LangGraph's run-scoped context (`context_schema`) is reconstructed on the Activity side, so nodes and tasks can read
from `runtime.context`:

```python
from langgraph.runtime import Runtime
from typing_extensions import TypedDict

from temporalio.contrib.langgraph import graph

class Context(TypedDict):
    user_id: str

async def my_node(state: State, runtime: Runtime[Context]) -> dict:
    return {"user": runtime.context["user_id"]}
