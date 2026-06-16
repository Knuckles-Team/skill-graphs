# Worker
Worker(..., plugins=[StrandsPlugin(models={
    "claude": lambda: AnthropicModel(client_args={"api_key": "..."}),
    "bedrock": lambda: BedrockModel(),
})])
```

Each `TemporalAgent` carries its own Activity options (timeouts, retry policy, task queue, streaming topic) and
dispatches to a shared model Activity, which resolves the model name against the registered factories at runtime. A
model name not present in the `models` mapping raises `ValueError` inside the Activity.

### Run non-deterministic tools as Activities

Strands tools that perform I/O, access external services, or produce non-deterministic results need to run as Temporal
Activities rather than inline in the Workflow. Wrap each tool in an `@activity.defn` function, register the Activities
on the Worker, and pass them to the agent using `activity_as_tool`.

Define an Activity for the tool:

<!--SNIPSTART python-strands-tools-activity-->
[strands_plugin/tools/workflow.py](https://github.com/temporalio/samples-python/blob/main/strands_plugin/tools/workflow.py)
```py
@activity.defn
async def fetch_weather(city: str) -> dict:
    """Stub weather lookup — replace with a real HTTP call in production."""
    return {
        "city": city,
        "temperature_f": 72,
        "conditions": "sunny",
    }

```
<!--SNIPEND-->

Pass the Activity to the agent in the Workflow using `activity_as_tool`:

<!--SNIPSTART python-strands-tools-workflow-->
[strands_plugin/tools/workflow.py](https://github.com/temporalio/samples-python/blob/main/strands_plugin/tools/workflow.py)
```py
@workflow.defn
class ToolsWorkflow:
    def __init__(self) -> None:
        self.agent = TemporalAgent(
            start_to_close_timeout=timedelta(seconds=60),
            tools=[
                letter_counter,
                activity_as_tool(
                    fetch_weather,
                    start_to_close_timeout=timedelta(seconds=30),
                ),
                activity_as_tool(
                    environment_activity,
                    start_to_close_timeout=timedelta(seconds=30),
                ),
            ],
        )

    @workflow.run
    async def run(self, prompt: str) -> str:
        result = await self.agent.invoke_async(prompt)
        return str(result)

```
<!--SNIPEND-->

Register the Activity functions on the Worker:

<!--SNIPSTART python-strands-tools-worker-->
[strands_plugin/tools/run_worker.py](https://github.com/temporalio/samples-python/blob/main/strands_plugin/tools/run_worker.py)
```py

from temporalio.client import Client
from temporalio.contrib.strands import StrandsPlugin
from temporalio.worker import Worker

from strands_plugin.tools.workflow import (
    ToolsWorkflow,
    environment_activity,
    fetch_weather,
)

async def main() -> None:
    plugin = StrandsPlugin()
    client = await Client.connect(
        os.environ.get("TEMPORAL_ADDRESS", "localhost:7233"),
        plugins=[plugin],
    )

    worker = Worker(
        client,
        task_queue="strands-tools",
        workflows=[ToolsWorkflow],
        activities=[fetch_weather, environment_activity],
    )
    print("Worker started. Ctrl+C to exit.")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
```
<!--SNIPEND-->

If you are using built-in `strands_tools`, wrap them in a thin async function decorated with `@activity.defn` so they
run as Temporal Activities.

### React to agent lifecycle events

Strands' [hook system](https://strandsagents.com/docs/user-guide/concepts/agents/hooks/) lets you subscribe callbacks to events in the agent lifecycle, such
as invocation start/end, model call before/after, tool call before/after, and message added. Use hooks to add logging,
metrics, or custom logic at each stage.

Pass `hooks=[MyHookProvider()]` to `TemporalAgent`. Hook callbacks fire in Workflow context, so deterministic callbacks
work without any extra setup.

For callbacks that need I/O (audit logging, metrics, alerting), use `activity_as_hook` to dispatch the work as a
Temporal Activity. The following example shows both patterns in one `HookProvider`. The `_record` callback runs in
Workflow context (deterministic), while `persist_tool_call` runs as an Activity (I/O-safe):

<!--SNIPSTART python-strands-hooks-activity-->
[strands_plugin/hooks/workflow.py](https://github.com/temporalio/samples-python/blob/main/strands_plugin/hooks/workflow.py)
```py
@activity.defn
async def persist_tool_call(tool_name: str) -> None:
    # In production, write to a database / S3 / your audit pipeline.
    activity.logger.info(f"audit: tool {tool_name} completed")

```
<!--SNIPEND-->

<!--SNIPSTART python-strands-hooks-provider-->
[strands_plugin/hooks/workflow.py](https://github.com/temporalio/samples-python/blob/main/strands_plugin/hooks/workflow.py)
```py
class AuditHook(HookProvider):
    def __init__(self) -> None:
        self.fired: list[str] = []

    def register_hooks(self, registry: HookRegistry, **kwargs: object) -> None:
        registry.add_callback(AfterToolCallEvent, self._record)
        registry.add_callback(
            AfterToolCallEvent,
            activity_as_hook(
                persist_tool_call,
                activity_input=lambda event: event.tool_use["name"],
                start_to_close_timeout=timedelta(seconds=15),
            ),
        )

    def _record(self, event: AfterToolCallEvent) -> None:
        self.fired.append(event.tool_use["name"])

```
<!--SNIPEND-->

:::caution

Hook callbacks run in Workflow context, so they must be
[deterministic](/develop/python/workflows/basics#workflow-logic-requirements). Do not use `time.time()`, `uuid.uuid4()`,
or I/O inside hook callbacks. Use `activity_as_hook` for anything that requires I/O.

:::

The `activity_input` parameter extracts serializable values from the event to pass as the Activity's input. Use a
dataclass or Pydantic model for multiple values. This is needed because hook events hold references to `Agent`,
`AgentTool` instances, and other objects that cannot cross the Activity boundary.

### Connect to MCP servers

If your agent needs access to tools provided by an [MCP](https://modelcontextprotocol.io/) server, configure the MCP
clients on the Worker and reference them by name in the Workflow.

`StrandsPlugin(mcp_clients=...)` takes a mapping of `name` to `MCPClient` factory, mirroring the `models` pattern. The
plugin registers a per-server Activity and connects at Worker startup to enumerate available tools. In the Workflow,
`TemporalMCPClient(server="name")` is a handle that references the server by name and carries per-call Activity options.

Define the Workflow with a `TemporalMCPClient`:

<!--SNIPSTART python-strands-mcp-workflow-->
[strands_plugin/mcp/workflow.py](https://github.com/temporalio/samples-python/blob/main/strands_plugin/mcp/workflow.py)
```py
from datetime import timedelta

from temporalio import workflow
from temporalio.contrib.strands import TemporalAgent, TemporalMCPClient

@workflow.defn
class MCPWorkflow:
    def __init__(self) -> None:
        echo = TemporalMCPClient(
            server="echo",
            start_to_close_timeout=timedelta(seconds=30),
        )
        self.agent = TemporalAgent(
            start_to_close_timeout=timedelta(seconds=60),
            tools=[echo],
        )

    @workflow.run
    async def run(self, prompt: str) -> str:
        result = await self.agent.invoke_async(prompt)
        return str(result)

```
<!--SNIPEND-->

Register the MCP client factory on the Worker:

<!--SNIPSTART python-strands-mcp-worker {"selectedLines": ["6-10", "17-25", "28-41"]}-->
[strands_plugin/mcp/run_worker.py](https://github.com/temporalio/samples-python/blob/main/strands_plugin/mcp/run_worker.py)
```py
