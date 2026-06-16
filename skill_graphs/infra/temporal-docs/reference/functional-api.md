# Functional API
plugin = LangGraphPlugin(
    tasks=[my_task],
    activity_options={"my_task": {"execute_in": "workflow"}},
)
```

### Example: subgraph orchestration

A common pattern is a parent node that runs in the Workflow and dispatches to a child graph whose nodes run as
Activities:

```python
async def parent_node(state: State) -> dict[str, str]:
    return await graph("child").compile().ainvoke(state)

parent = StateGraph(State)
parent.add_node("parent_node", parent_node, metadata={"execute_in": "workflow"})
parent.add_edge(START, "parent_node")

plugin = LangGraphPlugin(graphs={"parent": parent, "child": child})
```

## Human-in-the-loop

LangGraph's `interrupt()` works with Temporal signals and queries to support human-in-the-loop patterns:

1. A graph node calls `interrupt(draft)`, pausing execution.
2. The Workflow exposes the pending draft via a Temporal query.
3. An external process (UI, CLI) queries the draft and sends approval via a Temporal signal.
4. The graph resumes — `interrupt()` returns the signal value and the node completes.

See the [human-in-the-loop samples](https://github.com/temporalio/samples-python/tree/main/langgraph_plugin/graph_api/human_in_the_loop) for
complete working examples using both Graph and Functional APIs.

## Samples

The [LangGraph plugin samples](https://github.com/temporalio/samples-python/tree/main/langgraph_plugin)
demonstrate all supported patterns across both APIs.

---

## LangSmith integration

<ReleaseNoteHeader type="prerelease">
  All APIs are experimental and may be subject to backwards-incompatible changes.
</ReleaseNoteHeader>

Temporal's LangSmith integration lets you trace AI agent Workflows in [LangSmith](https://smith.langchain.com/)
alongside every LLM call, tool execution, and Temporal operation.

Temporal gives your agent code [durable execution](https://docs.temporal.io/temporal#durable-execution).
LangSmith adds the observability side, so you can inspect LLM inputs and outputs, follow a
request from the Client through to the model, and compare runs over time.

The `LangSmithPlugin` is what connects the two. It propagates trace context across Temporal boundaries so that runs
started on the Client nest correctly under Workflow and Activity runs on the Worker. It can also create LangSmith
runs for Temporal operations themselves: Workflow executions, Activity executions, Signals, Updates, and Queries.

All code snippets in this guide are taken from the
[LangSmith tracing sample](https://github.com/temporalio/samples-python/tree/main/langsmith_tracing). Refer to the
sample for complete code.

## Prerequisites

- This guide assumes you are already familiar with LangSmith. If you aren't, refer to the
  [LangSmith documentation](https://docs.smith.langchain.com/) for more details.
- If you are new to Temporal, we recommend reading [Understanding Temporal](/evaluate/understanding-temporal) or taking
  the [Temporal 101](https://learn.temporal.io/courses/temporal_101/) course.
- Ensure you have set up your local development environment by following the
  [Set up your local development environment](/develop/python/set-up-your-local-python) guide. When you're done, leave
  the Temporal Development Server running if you want to test your code locally.

## Configure Workers to use LangSmith

Workers execute the code that defines your Workflows and Activities. To trace Workflow and Activity execution in
LangSmith, add the `LangSmithPlugin` to your Worker.

Follow the steps below to configure your Worker.

1. Install the Temporal Python SDK with the LangSmith extra.

   ```bash
   uv add "temporalio[langsmith]>=1.26.0"
   ```

2. Add the `LangSmithPlugin` to your Worker. Set `project_name` to the LangSmith project where you want traces to
   appear.

   ```python
   from temporalio.contrib.langsmith import LangSmithPlugin
   from temporalio.worker import Worker

   worker = Worker(
       client,
       task_queue="my-task-queue",
       workflows=[MyWorkflow],
       activities=[my_activity],
       plugins=[LangSmithPlugin(project_name="my-project")],
   )
   ```

3. Run the Worker. Ensure the Worker process has access to your LangSmith API key via the `LANGSMITH_API_KEY`
   environment variable, and enable tracing with `LANGCHAIN_TRACING_V2`.

   ```bash
   export LANGSMITH_API_KEY="your-api-key"
   export LANGCHAIN_TRACING_V2=true
   python worker.py
   ```

## Configure Clients to use LangSmith

Add the plugin to any Temporal Client you use on the Client side (typically a starter or API that calls into
your Workflows) so that client-side operations like starting a Workflow or sending an Update get linked to the
Workflows they trigger.

```python
from temporalio.client import Client
from temporalio.contrib.langsmith import LangSmithPlugin

client = await Client.connect(
    "localhost:7233",
    plugins=[LangSmithPlugin(project_name="my-project")],
)
```

:::tip

Use the same `project_name` on both the Worker and the Client so their traces land in the same LangSmith project.

:::

:::note

`@traceable` functions on the Client side run outside the plugin's interceptor scope, so they don't pick up
`project_name` from the plugin. If you have a client-side `@traceable` that wraps a call into your Workflow, pass
`project_name` to it explicitly so it lands in the same LangSmith project as the rest of the trace.

:::

## Trace Activities

Any non-deterministic work in a Temporal Workflow (LLM calls, tool executions, database queries, external API calls,
and so on) must run inside an Activity. That makes Activities an important place to add LangSmith runs. When you
decorate an Activity function with `@traceable`, the run shows up in LangSmith nested under the Workflow that
scheduled it.

```python
from dataclasses import dataclass
from langsmith import traceable
from temporalio import activity

@traceable(name="Fetch Weather", run_type="tool")
@activity.defn
async def fetch_weather(city: str) -> str:
    # Call an external weather API here.
    ...
```

You can combine `@traceable` with provider-specific LangSmith wrappers to capture more detail. For OpenAI, for
example, `wrap_openai` patches the client so that every API call creates its own child run with the model name,
prompt, completion, token counts, and latency. You can access this by wrapping the client:

```python
from langsmith import traceable
from langsmith.wrappers import wrap_openai
from openai import AsyncOpenAI
from temporalio import activity

@dataclass
class OpenAIRequest:
    model: str
    input: str
