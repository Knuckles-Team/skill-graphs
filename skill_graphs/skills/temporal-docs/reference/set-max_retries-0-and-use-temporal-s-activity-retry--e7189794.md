# Set max_retries=0 and use Temporal's Activity retry policy instead.
@traceable(name="Call OpenAI", run_type="llm")
@activity.defn
async def call_openai(request: OpenAIRequest) -> str:
    client = wrap_openai(AsyncOpenAI(max_retries=0))
    response = await client.responses.create(
        model=request.model,
        input=request.input,
    )
    return response.output_text
```

LangSmith ships similar wrappers for
[Anthropic](https://docs.smith.langchain.com/observability/how-to/integrations#anthropic) and other providers; refer
to the LangSmith documentation for the full list.

## Add custom runs with @traceable

Decorate functions with `@traceable` to create named runs for your business logic. You control the run name, tags,
metadata, and `run_type` (`chain`, `llm`, `tool`, `retriever`).

Put `@traceable` on Activities and on private helper methods within your Workflow class that get called from Workflow
code. For example:

```python
from langsmith import traceable
from temporalio import workflow

@workflow.defn
class ChatbotWorkflow:
    # Private helper methods can be decorated directly.
    @traceable(name="Save Note", run_type="tool")
    def _save_note(self, name: str, content: str) -> str:
        ...
```

:::warning

Do not put `@traceable` directly on any `@workflow` method (for example, `@workflow.run`, `@workflow.signal`,
`@workflow.update`, `@workflow.query`). Doing so can produce duplicate or orphaned (unknown parent) runs in LangSmith.
If you want to trace the body of one of these methods, move the logic into an inner function and decorate that:

```python
@workflow.defn
class MyWorkflow:
    @workflow.run
    async def run(self, prompt: str) -> str:
        # Option 1: Use the @traceable decorator
        @traceable(name=f"Ask: {prompt[:60]}", run_type="chain")
        async def _run() -> str:
            ...
        return await _run()

    @workflow.update
    async def message_from_user(self, message: str) -> str:
        async def _handle_message(self, message: str) -> str:
            ...
        # Option 2: Use the traceable() function
        return await traceable(
            name=f"Update: {message[:60]}",
            run_type="chain",
        )(self._handle_message)(message)
```

:::

## Include Temporal operations as runs

By default, `LangSmithPlugin(add_temporal_runs=False)` only propagates LangSmith context so that `@traceable` and
`wrap_openai` calls nest correctly. The plugin does not create its own runs.

Set `add_temporal_runs=True` if you want runs for the Temporal operations themselves: Workflow executions, Activity
executions, Signals, Updates, Queries, and Child Workflows.

```python
plugin = LangSmithPlugin(
    project_name="my-project",
    add_temporal_runs=True,
)
```

With this on, your LangSmith traces include runs like `StartWorkflow:MyWorkflow`, `RunWorkflow:MyWorkflow`,
`StartActivity:call_openai`, and `RunActivity:call_openai`. `Start*` and `Run*` pairs appear as siblings: the `Start*`
run is emitted by the side scheduling the operation (for example, the Client), and the `Run*` run is emitted by the
side executing it (for example, the Worker).

## Trace hierarchy example

With the plugin configured on both Client and Worker, and `add_temporal_runs=True`, a trace for a simple LLM call looks
like this:

```
Run Agent                               (@traceable, client-side)
├── StartWorkflow:MyWorkflow             (automatic, LangSmithPlugin)
└── RunWorkflow:MyWorkflow               (automatic, LangSmithPlugin)
    └── Ask: What is Temporal?          (@traceable, Workflow)
        ├── StartActivity:call_openai    (automatic, LangSmithPlugin)
        └── RunActivity:call_openai      (automatic, LangSmithPlugin)
            └── Call OpenAI              (@traceable, Activity)
                └── ChatOpenAI           (automatic via wrap_openai)
```

Without `add_temporal_runs` (the default), only the `@traceable` and `wrap_openai` runs appear. Context still
propagates, so they nest correctly under the client-side run:

```
Run Agent                               (@traceable, client-side)
└── Ask: What is Temporal?              (@traceable, Workflow-side)
    └── Call OpenAI                     (@traceable, Activity-side)
        └── ChatOpenAI                  (automatic via wrap_openai)
```

## Example sample

The [LangSmith tracing sample](https://github.com/temporalio/samples-python/tree/main/langsmith_tracing) puts
these patterns together in two working examples:

- **`basic/`**: a one-shot Workflow that sends a prompt to OpenAI and returns the response.
- **`chatbot/`**: a long-running conversational Workflow with tool calls (save and read notes), Update handlers, and
  dynamic trace names per message.

Each example shows the `LangSmithPlugin` configuration, `@traceable` runs on the Client, Workflow, and Activity, and
expected trace output for both `add_temporal_runs=False` and `add_temporal_runs=True`.

---

## Strands Agents integration

Temporal's integration with [Strands Agents](https://strandsagents.com/) is an [SDK Plugin](/develop/plugins-guide) that
gives your Strands agents [Durable Execution](/temporal#durable-execution) via the Temporal platform. The plugin routes
model invocations, tool calls, MCP tool calls, and hooks through Temporal Activities, so every step your agent takes is
recorded in Workflow history and can survive crashes, restarts, and infrastructure failures.

<ReleaseNoteHeader type="publicPreview" />

Code snippets in this guide are taken from the
[Strands Agents plugin samples](https://github.com/temporalio/samples-python/tree/main/strands_plugin). Refer to the
samples for the complete code.

## Get started

Install the plugin, then run a minimal Strands agent inside a Temporal Workflow.

### Prerequisites

- This guide assumes you are already familiar with Strands Agents. If you are not, refer to the
  [Strands Agents documentation](https://strandsagents.com/) for more details.
- If you are new to Temporal, read [Understanding Temporal](/evaluate/understanding-temporal) or take the
  [Temporal 101](https://learn.temporal.io/courses/temporal_101/) course.
- Set up your local development environment by following the
  [Set up your local development environment](/develop/python/set-up-your-local-python) guide. Leave the Temporal
  development server running if you want to test your code locally.

### Install the plugin

Install the Temporal Python SDK with Strands Agents support (requires `temporalio` 1.28.0 or later):

```bash
uv add "temporalio[strands-agents]"
```

or with pip:

```bash
pip install "temporalio[strands-agents]"
```

### Run a Strands agent with Durable Execution

The following example runs a Strands agent inside a Temporal Workflow. Model calls execute as Temporal Activities, which
means they get automatic retries, timeouts, and durable execution. If the Worker process crashes mid-conversation,
Temporal replays the Workflow and resumes from the last completed Activity.

**1. Define the Workflow**

Create a Workflow that holds a `TemporalAgent` and invokes it with a prompt. The `start_to_close_timeout` sets the
maximum time each model call Activity can run:

<!--SNIPSTART python-strands-hello-world-workflow-->
[strands_plugin/hello_world/workflow.py](https://github.com/temporalio/samples-python/blob/main/strands_plugin/hello_world/workflow.py)
```py
from datetime import timedelta

from temporalio import workflow
from temporalio.contrib.strands import TemporalAgent

@workflow.defn
class HelloWorldWorkflow:
    def __init__(self) -> None:
        self.agent = TemporalAgent(start_to_close_timeout=timedelta(seconds=60))

    @workflow.run
    async def run(self, prompt: str) -> str:
        result = await self.agent.invoke_async(prompt)
        return str(result)

```
<!--SNIPEND-->

:::caution

Inside a Workflow, always call `agent.invoke_async(message)`, not `agent(message)`. The synchronous form spawns a worker
thread, which the Workflow sandbox blocks.

:::

**2. Start a Worker**

Create a Worker that registers the Workflow and the `StrandsPlugin`. The plugin automatically registers the Activities
that handle model calls:

<!--SNIPSTART python-strands-hello-world-worker-->
[strands_plugin/hello_world/run_worker.py](https://github.com/temporalio/samples-python/blob/main/strands_plugin/hello_world/run_worker.py)
```py

from temporalio.client import Client
from temporalio.contrib.strands import StrandsPlugin
from temporalio.worker import Worker

from strands_plugin.hello_world.workflow import HelloWorldWorkflow

async def main() -> None:
    plugin = StrandsPlugin()
    client = await Client.connect(
        os.environ.get("TEMPORAL_ADDRESS", "localhost:7233"),
        plugins=[plugin],
    )

    worker = Worker(
        client,
        task_queue="strands-hello-world",
        workflows=[HelloWorldWorkflow],
    )
    print("Worker started. Ctrl+C to exit.")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
```
<!--SNIPEND-->

**3. Run the Workflow**

Start the Workflow from a separate client script. This example sends the prompt "Write a haiku about durable execution"
and prints the agent's response:

<!--SNIPSTART python-strands-hello-world-run-workflow-->
[strands_plugin/hello_world/run_workflow.py](https://github.com/temporalio/samples-python/blob/main/strands_plugin/hello_world/run_workflow.py)
```py

from temporalio.client import Client

from strands_plugin.hello_world.workflow import HelloWorldWorkflow

async def main() -> None:
    client = await Client.connect(os.environ.get("TEMPORAL_ADDRESS", "localhost:7233"))

    result = await client.execute_workflow(
        HelloWorldWorkflow.run,
        "Write a haiku about durable execution.",
        id="strands-hello-world",
        task_queue="strands-hello-world",
    )

    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```
<!--SNIPEND-->

## Build the agent

Customize which model provider your agent uses, add tools that run as Activities, subscribe to lifecycle events with
hooks, and connect to MCP servers.

### Choose and configure models

By default, `StrandsPlugin` uses Strands' own default model (`BedrockModel`). To use a different model, pass a `models`
mapping to `StrandsPlugin` on the Worker. When you provide a custom `models` mapping, each `TemporalAgent` must specify
which model to use by name.

Each entry in the mapping pairs a name with a factory function that creates a model provider (such as `AnthropicModel`
or `BedrockModel`). The provider is created on first use and reused for the Worker's lifetime:

```python
from strands.models.anthropic import AnthropicModel
from strands.models.bedrock import BedrockModel
