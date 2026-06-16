# Build a data analysis agent from scratch
Source: https://docs.langchain.com/oss/python/langchain/deep-agent-from-scratch

Build a data analysis agent step by step using create_agent and deepagents middleware.

This guide builds a data analysis agent from first principles using `create_agent` and deepagents middleware. Rather than starting with `create_deep_agent`, we assemble the harness one piece at a time: so you can see exactly what each component adds and swap in only what your use case needs.

The agent we'll build:

1. Accepts a CSV file for analysis
2. Writes and executes Python code in an isolated sandbox
3. Delegates visualization work to a specialized subagent
4. Loads data analysis patterns from a skills file

## Setup

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
pip install deepagents langsmith
```

Enable LangSmith tracing to inspect every step:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=...
```

***

## Step 1: The minimal agent

A model, a loop. Nothing else yet.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent

agent = create_agent("anthropic:claude-sonnet-4-6", tools=[])
```

This runs, but the agent has no filesystem and no way to execute code. The next steps add those.

***

## Step 2: Add a sandbox backend

`LangSmithSandbox` gives the agent an isolated environment with a filesystem and an `execute` tool for running shell commands. The agent can install packages, write scripts, and run them: without touching the host.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langsmith.sandbox import SandboxClient
from deepagents.backends.langsmith import LangSmithSandbox
from deepagents.middleware import FilesystemMiddleware

client = SandboxClient()
sandbox = client.create_sandbox(template_name="deepagents-deploy")
backend = LangSmithSandbox(sandbox=sandbox)

agent = create_agent(
    "anthropic:claude-sonnet-4-6",
    tools=[],
    middleware=[FilesystemMiddleware(backend=backend)],
)
```

[`FilesystemMiddleware`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware) adds `read_file`, `write_file`, `edit_file`, `glob`, and `grep`. Because `LangSmithSandbox` implements the sandbox protocol, it also adds `execute`: the agent can now run shell commands.

Upload a CSV and invoke:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import csv, io

rows = [
    ["Date", "Product", "Units", "Revenue"],
    ["2025-08-01", "Widget A", 10, 250],
    ["2025-08-02", "Widget B", 5, 125],
    ["2025-08-03", "Widget A", 7, 175],
    ["2025-08-04", "Widget C", 3, 90],
]
buf = io.StringIO()
csv.writer(buf).writerows(rows)
backend.upload("sales.csv", buf.getvalue().encode())

result = agent.invoke({
    "messages": [{"role": "user", "content": "Analyze sales.csv. Summarize trends."}]
})
```

***

## Step 3: Add context management

For longer analysis sessions the context window fills. `SummarizationMiddleware` compresses history automatically so the agent keeps working without hitting token limits.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents.middleware import FilesystemMiddleware, SummarizationMiddleware

model = "anthropic:claude-sonnet-4-6"

agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=model, backend=backend),
    ],
)
```

***

## Step 4: Add skills

Skills give the agent on-demand domain knowledge via progressive disclosure: loaded only when the current task calls for it. Create a skill file in your skills directory:

```
skills/
  pandas-patterns/
    SKILL.md
```

```markdown theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
---
name: pandas-patterns
description: Common pandas and matplotlib patterns for data analysis and visualization
---

## Data loading
Use `pd.read_csv()` for CSV files. Always check `df.info()` and `df.describe()` first.

## Visualization
Use `matplotlib` for bar charts, `seaborn` for statistical plots.
Save figures with `plt.savefig("output.png", dpi=150, bbox_inches="tight")`.

## Reporting
Write a markdown summary to `report.md` alongside any generated charts.
```

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents.middleware import FilesystemMiddleware, SkillsMiddleware, SummarizationMiddleware

agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=model, backend=backend),
        SkillsMiddleware(backend=backend, sources=["./skills/"]),
    ],
)
```

***

## Step 5: Add a visualization subagent

Some tasks benefit from isolation. A visualization subagent runs in its own context window, keeping chart generation separate from the main analysis: and enabling parallel execution.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents.middleware import TodoListMiddleware
from deepagents import SubAgent
from deepagents.middleware import (
    FilesystemMiddleware,
    SkillsMiddleware,
    SubAgentMiddleware,
    SummarizationMiddleware,
)

visualizer: SubAgent = {
    "name": "visualizer",
    "description": "Generates charts and visualizations from data files in the sandbox.",
    "system_prompt": "You are a data visualization specialist. Write Python scripts using matplotlib and seaborn. Save all figures as PNG files.",
    "tools": [],
}

agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        FilesystemMiddleware(backend=backend),
        SummarizationMiddleware(model=model, backend=backend),
        SkillsMiddleware(backend=backend, sources=["./skills/"]),
        TodoListMiddleware(),
        SubAgentMiddleware(backend=backend, subagents=[visualizer]),
    ],
)
```

The main agent handles analysis and planning; it delegates chart generation to the `visualizer` subagent via the `task` tool.

***

## What you built

| Middleware                                                                                                                                                                                                                             | What it adds                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| [`FilesystemMiddleware`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware) + `LangSmithSandbox`                                                                                            | Isolated filesystem + `execute` tool |
| [`SummarizationMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware)                                                                                                  | Automatic context compression        |
| [`SkillsMiddleware`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware)                                                                                                                             | Domain knowledge loaded on demand    |
| [`TodoListMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware) + [`SubAgentMiddleware`](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware) | Parallel visualization subagent      |

This is the same foundation as `create_deep_agent`: assembled manually so you control exactly what's included. The possibilities don't end here: see [Prebuilt middleware](/oss/python/langchain/middleware/built-in) for the full list of composable capabilities, and the [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) reference for all configuration options.

For a pre-assembled version, see [`create_deep_agent`](https://reference.langchain.com/python/deepagents/graph/create_deep_agent) and [Customize Deep Agents](/oss/python/deepagents/customization). For the full data analysis example using `create_deep_agent`, see [Data analysis](/oss/python/deepagents/data-analysis).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/deep-agent-from-scratch.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Deployment
Source: https://docs.langchain.com/oss/python/langchain/deploy

When you're ready to deploy your LangChain agent to production, LangSmith provides a managed hosting platform designed for agent workloads. Traditional hosting platforms are built for stateless, short-lived web applications, while LangGraph is **purpose-built for stateful, long-running agents** that require persistent state and background execution. LangSmith handles the infrastructure, scaling, and operational concerns so you can deploy directly from your repository.

## Prerequisites

Before you begin, ensure you have the following:

* A [GitHub account](https://github.com/)
* A [LangSmith account](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-deploy) (free to sign up)

## Deploy your agent

### 1. Create a repository on GitHub

Your application's code must reside in a GitHub repository to be deployed on LangSmith. Both public and private repositories are supported. For this quickstart, first make sure your app is LangGraph-compatible by following the [local server setup guide](/oss/python/langchain/studio). Then, push your code to the repository.

### 2. Deploy to LangSmith

<Steps>
  <Step title="Navigate to LangSmith Deployment">
    Log in to [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=snippets-oss-deploy-py). In the left sidebar, select **Deployments**.
  </Step>

  <Step title="Create new deployment">
    Click the **+ New Deployment** button. A pane will open where you can fill in the required fields.
  </Step>

  <Step title="Link repository">
    If you are a first time user or adding a private repository that has not been previously connected, click the **Add new account** button and follow the instructions to connect your GitHub account.
  </Step>

  <Step title="Deploy repository">
    Select your application's repository. Click **Submit** to deploy. This may take about 15 minutes to complete. You can check the status in the **Deployment details** view.
  </Step>
</Steps>

### 3. Test your application in Studio

Once your application is deployed:

1. Select the deployment you just created to view more details.
2. Click the **Studio** button in the top right corner. Studio will open to display your graph.

### 4. Get the API URL for your deployment

1. In the **Deployment details** view in LangGraph, click the **API URL** to copy it to your clipboard.
2. Click the `URL` to copy it to the clipboard.

### 5. Test the API

You can now test the API:

<Tabs>
  <Tab title="Python">
    1. Install LangGraph Python:

    ```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    pip install langgraph-sdk
    ```

    2. Send a message to the agent:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph_sdk import get_sync_client # or get_client for async

    client = get_sync_client(url="your-deployment-url", api_key="your-langsmith-api-key")

    for chunk in client.runs.stream(
        None,    # Threadless run
        "agent", # Name of agent. Defined in langgraph.json.
        input={
            "messages": [{
                "role": "human",
                "content": "What is LangGraph?",
            }],
        },
        stream_mode="updates",
    ):
        print(f"Receiving new event of type: {chunk.event}...")
        print(chunk.data)
        print("\n\n")
    ```
  </Tab>

  <Tab title="Rest API">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl -s --request POST \
        --url <DEPLOYMENT_URL>/runs/stream \
        --header 'Content-Type: application/json' \
        --header "X-Api-Key: <LANGSMITH API KEY> \
        --data "{
            \"assistant_id\": \"agent\", `# Name of agent. Defined in langgraph.json.`
            \"input\": {
                \"messages\": [
                    {
                        \"role\": \"human\",
                        \"content\": \"What is LangGraph?\"
                    }
                ]
            },
            \"stream_mode\": \"updates\"
        }"
    ```
  </Tab>
</Tabs>

<Tip>
  LangSmith offers additional hosting options, including self-hosted and hybrid. For more information, please see the [Platform setup overview](/langsmith/platform-setup).
</Tip>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/deploy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Event streaming
Source: https://docs.langchain.com/oss/python/langchain/event-streaming

Stream real-time updates from LangChain agent runs

LangChain agents are built on LangGraph, so they support the same streaming stack with agent-focused projections for messages, tool calls, state, and custom updates.

For most application and frontend use cases, use **Event Streaming** through `stream_events(..., version="v3")`. Event Streaming returns a run object with typed projections, so each projection can be consumed independently instead of parsing stream-mode tuples.

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="gpt-5-nano",
    tools=[get_weather],
)

stream = agent.stream_events({
    "messages": [{"role": "user", "content": "What is the weather in SF?"}],
}, version="v3")

for message in stream.messages:
    for delta in message.text:
        print(delta, end="", flush=True)

final_state = stream.output
```

## What you can stream

| Projection            | Use                                                                        |
| --------------------- | -------------------------------------------------------------------------- |
| `for event in stream` | Raw protocol events with full envelope and access to every channel.        |
| `stream.messages`     | Model message streams, one per LLM call.                                   |
| `message.text`        | Text deltas and final text for a message.                                  |
| `message.reasoning`   | Reasoning deltas for models that expose reasoning content.                 |
| `message.tool_calls`  | Tool-call argument chunks and finalized tool calls.                        |
| `message.output`      | Final message object after the model call completes.                       |
| `stream.values`       | Agent state snapshots.                                                     |
| `stream.output`       | Final agent state.                                                         |
| `stream.subgraphs`    | Nested graph runs (sub-agents and plain subgraphs).                        |
| `stream.extensions`   | Custom transformer projections.                                            |
| `stream.tool_calls`   | Tool execution lifecycle, inputs, output deltas, final output, and errors. |

`stream.messages` yields `ChatModelStream` objects. Each message stream exposes `.text`, `.reasoning`, `.tool_calls`, and `.output`. Sync projections are iterable for live deltas and drainable for final values: use `str(message.text)` for final text and `message.tool_calls.get()` for finalized tool calls.

## Agent messages

Use `stream.messages` when you want model output from each LLM call.

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream = agent.stream_events(input, version="v3")

for message in stream.messages:
    print(f"[{message.node}] ", end="")
    for delta in message.text:
        print(delta, end="", flush=True)

    full_message = message.output
    usage = full_message.usage_metadata
    if usage:
        print(usage)
```

`message.output` gives you the finalized AI message, including provider-specific content blocks. In TypeScript, use `message.usage` when you only need token counts or other usage metadata; in Python, read usage from `message.output.usage_metadata`.

## Reasoning content

Reasoning content uses the same shape as text content, but it is available only when the selected model emits reasoning blocks.

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream = agent.stream_events(input, version="v3")

for message in stream.messages:
    for delta in message.reasoning:
        print(f"[thinking] {delta}", end="", flush=True)

    for delta in message.text:
        print(delta, end="", flush=True)
```

See the [reasoning guide](/oss/python/langchain/models#reasoning) and your provider's integration page for model configuration details.

## Tool calls

There are two useful tool-call projections:

* `message.tool_calls` streams tool-call argument chunks while the model is producing the tool call.
* `stream.tool_calls` streams the lifecycle of tool execution after the tool call starts.

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream = agent.stream_events(input, version="v3")

for message in stream.messages:
    for chunk in message.tool_calls:
        print(f"tool call chunk: {chunk}")

    finalized = message.tool_calls.get()
    if finalized:
        print(f"finalized tool calls: {finalized}")

for call in stream.tool_calls:
    print(f"{call.tool_name}({call.input})")
    for delta in call.output_deltas:
        print(delta, end="", flush=True)
    print(call.output, call.error)
```

## Streaming sub-agents

When a `create_agent` call invokes another named `create_agent` (via a wrapping tool, typically), the inner agent's events flow at a nested namespace. The `name=` you pass to `create_agent` identifies that inner agent in the stream, so you can filter and label per agent.

Named sub-agents surface on the dedicated `stream.subagents` projection. Each handle exposes the inner agent's own `.messages`, `.values`, `.tool_calls`, and `.output`, plus `.name` (the `name=` you passed) and `.cause` (the tool call that dispatched the sub-agent). Because only named `create_agent` runs appear here, you don't need to filter plain subgraphs out.

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

weather_agent = create_agent(
    model=init_chat_model("openai:gpt-5.5"),
    tools=[get_weather],
    name="weather_agent",
)

def call_weather(query: str) -> str:
    """Query the weather agent."""
    result = weather_agent.invoke({"messages": [{"role": "user", "content": query}]})
    return result["messages"][-1].text

supervisor = create_agent(
    model=init_chat_model("openai:gpt-5.5"),
    tools=[call_weather],
    name="supervisor",
)

stream = supervisor.stream_events(
    {"messages": [{"role": "user", "content": "What's the weather in Boston?"}]},
    version="v3",
)

for subagent in stream.subagents:
    print(f"{subagent.name}: ", end="")
    for message in subagent.messages:
        for token in message.text:
            print(token, end="", flush=True)
    print()
```

Plain `StateGraph` subgraphs invoked from a tool also surface on `stream.subgraphs` — set `name=` on `.compile(name=...)` to get a label in `subagent.graph_name`.

`stream.subagents` is the focused view of named `create_agent` sub-agents, while `stream.subgraphs` covers every nested graph. Use whichever matches your UI.

## State and final output

Use `stream.values` for state snapshots and `stream.output` for the final agent state.

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream = agent.stream_events(input, version="v3")

for snapshot in stream.values:
    print(snapshot)

final_state = stream.output
```

## Multiple projections

For concurrent consumption in async code, use `astream_events` with `asyncio.gather`:

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio

stream = await agent.astream_events(input, version="v3")

async def consume_messages():
    async for message in stream.messages:
        print(await message.text)

async def consume_tool_calls():
    async for call in stream.tool_calls:
        print(call.tool_name, call.input)

await asyncio.gather(consume_messages(), consume_tool_calls())
```

For synchronous code, use `stream.interleave(...)` instead:

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream = agent.stream_events(input, version="v3")

for name, item in stream.interleave("messages", "tool_calls", "values"):
    if name == "messages":
        print(item.text)
    elif name == "tool_calls":
        print(item.tool_name, item.input)
    elif name == "values":
        print(item)
```

To access channels that aren't exposed as typed projections, or to inspect the full event envelope, iterate raw protocol events:

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
for event in stream:
    print(event["method"], event["params"]["namespace"], event["params"]["data"])
```

## Custom updates

Use custom stream transformers when your application needs a projection that is not built in, such as retrieval progress, artifacts, or domain-specific events.

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
stream = agent.stream_events(
    input,
    version="v3",
    transformers=[ToolActivityTransformer],
)

for activity in stream.extensions["tool_activity"]:
    print(activity)
```

### Register transformers on middleware

<Note>Middleware-registered transformers require `langchain>=1.3.2`.</Note>

Middleware can declare stream transformer factories alongside its hooks and tools. The factory shape differs between languages:

Set the `transformers` attribute on an `AgentMiddleware` subclass to a sequence of factories. Each factory has the shape `Callable[[tuple[str, ...]], StreamTransformer]` and is invoked as `factory(scope)`, where `scope` is the mini-mux scope tuple (`()` for the root mux, non-empty for subgraphs). Returning a fresh transformer per call keeps each subgraph isolated.

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware

class ToolActivityMiddleware(AgentMiddleware):
    transformers = (ToolActivityTransformer,)

agent = create_agent(
    model="gpt-5-nano",
    tools=[get_weather],
    middleware=[ToolActivityMiddleware()],
)
```

At compile time, `create_agent` merges middleware-registered factories with anything passed to its own `transformers=` argument. The final order on the compiled graph is:

1. The built-in `ToolCallTransformer`.
2. Middleware-registered factories, in middleware order.
3. Caller-supplied `transformers=` from `create_agent`.

This keeps the built-in tool-call projection in front of consumer transformers and gives caller-supplied entries the final word.

The built-in `PIIMiddleware` uses this hook to redact PII from streamed wire output. With `apply_to_output=True`, its registered transformer scrubs detected PII from text deltas, tool-call args, tool outputs, and state snapshots before they leave the run, closing the window where `after_model` state-level redaction would otherwise let raw PII through to live readers of `stream_events(version="v3")`.

```py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain.agents.middleware import PIIMiddleware

agent = create_agent(
    model="gpt-5-nano",
    tools=[],
    middleware=[
        PIIMiddleware("email", strategy="redact", apply_to_output=True),
    ],
)
```

See [PII detection](/oss/python/langchain/middleware/built-in#pii-detection) for the full configuration surface.

See [Build your own projection](/oss/python/langgraph/event-streaming#build-your-own-projection) for the transformer contract.

## Related

* [Streaming](/oss/python/langchain/streaming) covers low-level Pregel stream modes.
* [Build your own projection](/oss/python/langgraph/event-streaming#build-your-own-projection) covers writing application-specific projections.
* [Frontend streaming patterns](/oss/python/langchain/frontend/overview) shows UI use cases built on streamed state.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/event-streaming.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Branching chat
Source: https://docs.langchain.com/oss/python/langchain/frontend/branching-chat

Edit messages and regenerate responses by forking from checkpoints

Conversations with AI agents are rarely linear. You may want to rephrase a
question, regenerate a response you didn't like, or explore a different
conversational path without losing the checkpoint history. Branching chat uses
LangGraph checkpoints as fork points: every edit or regeneration submits a new
run from the selected message's parent checkpoint.

<PatternEmbed />

<Note>
  This feature requires the [LangGraph Agent Server](../langgraph/local-server). Run your agent locally with `langgraph dev` or [deploy it to LangSmith](/langsmith/deployment) to use this pattern.
</Note>

## What is branching chat?

Branching chat treats a conversation as a checkpointed timeline rather than a
flat list. Each message has metadata that points to the checkpoint before that
message was created. Editing a message or regenerating a response submits a new
run from that checkpoint.

Key capabilities:

* **Edit any user message:** rewrite a previous prompt and re-run the agent from that point
* **Regenerate any AI response:** ask the agent to produce a different answer for the same input
* **Inspect history:** use the LangGraph client to load checkpoints when you need a branch timeline

## Set up stream metadata

Use the root stream for messages, then read per-message checkpoint metadata in
the component that renders each message. The metadata includes the parent
checkpoint ID to fork from.

<Info>
  The code examples use `useStream<typeof myAgent>` for type-safe stream state. See Type inference for [Python](/oss/python/langchain/frontend/overview#type-inference) or [JavaScript](/oss/javascript/langchain/frontend/overview#type-inference) backends.
</Info>

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";

  const AGENT_URL = "http://localhost:2024";

  export function Chat() {
    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "simple_agent",
    });

    return (
      <div>
        {stream.messages.map((msg) => (
          <MessageWithForkControls key={msg.id} stream={stream} message={msg} />
        ))}
      </div>
    );
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";

  const AGENT_URL = "http://localhost:2024";

  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "simple_agent",
  });
  </script>

  <template>
    <div>
      <MessageWithForkControls
        v-for="msg in stream.messages.value"
        :key="msg.id"
        :stream="stream"
        :message="msg"
      />
    </div>
  </template>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";

    const AGENT_URL = "http://localhost:2024";

    const stream = useStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "simple_agent",
    });
  </script>

  <div>
    {#each stream.messages as msg (msg.id)}
      <Message
        message={msg}
        {stream}
      />
    {/each}
  </div>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component } from "@angular/core";
  import { injectStream } from "@langchain/angular";

  const AGENT_URL = "http://localhost:2024";

  @Component({
    selector: "app-chat",
    template: `
      @for (msg of stream.messages(); track msg.id) {
        <app-message
          [message]="msg"
          [stream]="stream"
        />
      }
    `,
  })
  export class ChatComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: AGENT_URL,
      assistantId: "simple_agent",
    });
  }
  ```
</CodeGroup>

## Understand message metadata

The `useMessageMetadata(stream, messageId)` helper returns [MessageMetadata](https://reference.langchain.com/javascript/langchain-react/MessageMetadata)
for one message. Use it in the component that renders each message so the
metadata stays scoped to that message ID:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import type { BaseMessage } from "langchain";
import { useState } from "react";
import { useMessageMetadata, useStream } from "@langchain/react";

function Chat() {
  const stream = useStream<typeof myAgent>({
    apiUrl: AGENT_URL,
    assistantId: "simple_agent",
  });

  return stream.messages.map((message) => (
    <MessageWithForkControls
      key={message.id}
      stream={stream}
      message={message}
    />
  ));
}

function MessageWithForkControls({
  stream,
  message,
}: {
  stream: ReturnType<typeof useStream>;
  message: BaseMessage;
}) {
  const metadata = useMessageMetadata(stream, message.id);
  const checkpointId = metadata?.parentCheckpointId;
  const [editedText, setEditedText] = useState(message.text);

  return (
    <form
      onSubmit={(event) => {
        event.preventDefault();
        if (!checkpointId) return;

        stream.submit(
          { messages: [{ type: "human", content: editedText }] },
          { forkFrom: { checkpointId } }
        );
      }}
    >
      <textarea
        value={editedText}
        onChange={(event) => setEditedText(event.target.value)}
      />
      <button disabled={!checkpointId || editedText === message.text}>
        Submit edited branch
      </button>
    </form>
  );
}
```

`parentCheckpointId` is the checkpoint just before the message. Use it as the
fork point for edits and regenerations.

## Edit a message

To edit a user message and fork the conversation:

1. Get `parentCheckpointId` from the message's metadata
2. Submit the edited message with `forkFrom: { checkpointId }`
3. The agent re-runs from that point

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function handleEdit(
  stream: ReturnType<typeof useStream>,
  originalMsg: HumanMessage,
  metadata: MessageMetadata | undefined,
  newText: string
) {
  if (!metadata?.parentCheckpointId) return;

  stream.submit(
    {
      messages: [{ type: "human", content: newText }],
    },
    { forkFrom: { checkpointId: metadata.parentCheckpointId } }
  );
}
```

After the edit:

* The agent re-runs from the fork point with the updated message
* The original path remains available in the thread history

## Regenerate a response

To regenerate an AI response without changing the input:

1. Get the `parent_checkpoint` from the AI message's metadata
2. Submit with empty input and `forkFrom: { checkpointId }`
3. The agent produces a fresh response from that point

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function handleRegenerate(
  stream: ReturnType<typeof useStream>,
  metadata: MessageMetadata | undefined
) {
  if (!metadata?.parentCheckpointId) return;

  stream.submit(undefined, {
    forkFrom: { checkpointId: metadata.parentCheckpointId },
  });
}
```

Each regeneration creates a new path for the AI message at that position.

<Tip>
  Regeneration is useful for non-deterministic agents. Since LLM outputs vary
  with temperature, regenerating the same prompt often produces meaningfully
  different responses.
</Tip>

## How branching works under the hood

LangGraph persists every state transition as a **checkpoint**. When you submit
with `forkFrom`, the backend starts a new execution path from that point instead
of appending to the current conversation. The result is a tree structure:

```
User: "What is React?"
  └─ AI: "React is a JavaScript library..." (branch A)
  └─ AI: "React is a UI framework..." (branch B, regenerated)

User: "Tell me about hooks" (branch A)
  └─ AI: "Hooks are functions..."

User: "Tell me about JSX" (edited from branch A)
  └─ AI: "JSX is a syntax extension..."
```

Each path is persisted in the checkpoint store. Use
`stream.client.threads.getHistory(threadId)` when you want to build a separate
timeline view across checkpoints.

## Best practices

* **Read metadata near the message**: call `useMessageMetadata` in the component
  that renders the message controls.
* **Show fork controls on hover**: edit and regenerate buttons should appear on
  hover to keep the UI clean.
* **Refresh history on demand**: call `client.threads.getHistory()` only when
  rendering a timeline or after a fork settles.
* **Disable controls while streaming**: don't allow edits or regeneration
  while the agent is actively streaming a response. Check `stream.isLoading`
  before enabling these actions.
* **Preserve edit text on cancel**: if the user starts editing, then cancels,
  reset the textarea to the original message content.
* **Test with deep checkpoint trees**: users who edit and regenerate frequently
  can create many paths. Ensure timeline rendering remains performant.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/branching-chat.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Generative UI
Source: https://docs.langchain.com/oss/python/langchain/frontend/generative-ui

Render AI-generated user interfaces using json-render

Generative UI lets the AI generate complete user interfaces from natural language
prompts. Instead of rendering text responses in chat bubbles, the AI output **is**
the UI: forms, cards, dashboards, and more. The developer defines which components
are available (the "catalog"), and the AI composes them into a valid UI tree.

This pattern uses [json-render](https://json-render.dev), the Generative UI framework,
to define component catalogs, generate specs with AI, and render them safely across
React, Vue, Svelte, and Angular.

<PatternEmbed />

## How it works

1. **Define a catalog**: declare what components the AI can use, with typed props
2. **Prompt the AI**: describe the UI you want in natural language
3. **AI generates a spec**: a JSON document describing the component tree
4. **Render safely**: json-render's `Renderer` renders the spec using your components

The catalog acts as a guardrail: the AI can only use components you've defined,
with props that match your schema. The output is always predictable and safe.

## Define a component catalog

The catalog describes every component the AI is allowed to use. Each component has a
Zod schema for its props and a description that the AI reads to understand when to
use it:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { defineCatalog } from "@json-render/core";
import { schema } from "@json-render/react/schema";
import { z } from "zod";

const catalog = defineCatalog(schema, {
  components: {
    Card: {
      description: "A card container with optional title and padding",
      props: z.object({
        title: z.string().optional(),
        padding: z.enum(["sm", "md", "lg"]).optional(),
      }),
    },
    Stack: {
      description: "Layout children vertically or horizontally with consistent spacing",
      props: z.object({
        direction: z.enum(["vertical", "horizontal"]).optional(),
        gap: z.enum(["sm", "md", "lg"]).optional(),
      }),
    },
    TextInput: {
      description: "A text input field with optional label and placeholder",
      props: z.object({
        label: z.string().optional(),
        placeholder: z.string().optional(),
        type: z.enum(["text", "email", "password", "number", "textarea"]).optional(),
      }),
    },
    Button: {
      description: "A clickable button with label and style variants",
      props: z.object({
        label: z.string(),
        variant: z.enum(["primary", "secondary", "ghost", "link"]).optional(),
        fullWidth: z.boolean().optional(),
      }),
    },
  },
  actions: {},
});
```

<Tip>
  Keep catalogs focused. Include only components the AI needs for the use case.
  A smaller catalog produces better results than a kitchen-sink approach.
</Tip>

## Build a component registry

The registry maps each catalog component to its actual rendering implementation.
Use `defineRegistry` to get type-safe bindings between the catalog props and
your component functions:

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { defineRegistry, Renderer, JSONUIProvider } from "@json-render/react";

  const { registry } = defineRegistry(catalog, {
    components: {
      Card: ({ props, children }) => (
        <div className="card">
          {props.title && <h2>{props.title}</h2>}
          {children}
        </div>
      ),
      Stack: ({ props, children }) => (
        <div className={`stack stack-${props.direction ?? "vertical"} gap-${props.gap ?? "md"}`}>
          {children}
        </div>
      ),
      TextInput: ({ props }) => (
        <div>
          {props.label && <label>{props.label}</label>}
          <input type={props.type ?? "text"} placeholder={props.placeholder} />
        </div>
      ),
      Button: ({ props }) => (
        <button className={props.variant ?? "primary"}>
          {props.label}
        </button>
      ),
    },
  });
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { h } from "vue";
  import { defineRegistry, Renderer, JSONUIProvider } from "@json-render/vue";

  const { registry } = defineRegistry(catalog, {
    components: {
      Card: ({ props, children }) =>
        h("div", { class: "card" }, [
          props.title ? h("h2", null, props.title) : null,
          children,
        ]),
      Stack: ({ props, children }) =>
        h("div", { class: `stack stack-${props.direction ?? "vertical"} gap-${props.gap ?? "md"}` }, children),
      TextInput: ({ props }) =>
        h("div", null, [
          props.label ? h("label", null, props.label) : null,
          h("input", { type: props.type ?? "text", placeholder: props.placeholder }),
        ]),
      Button: ({ props }) =>
        h("button", { class: props.variant ?? "primary" }, props.label),
    },
  });
  </script>
  ```
</CodeGroup>

## Connect to the agent

The agent uses structured output to return a json-render spec. Set up `useStream`
with your agent's assistant ID, then extract the spec from the AI message's
`tool_calls`:

<CodeGroup>
  ```tsx React theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { useStream } from "@langchain/react";
  import { AIMessage } from "langchain";

  function GenerativeUI() {
    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "generative_ui",
    });

    const aiMessage = stream.messages.find(AIMessage.isInstance);
    const rawSpec = aiMessage?.tool_calls?.[0]?.args;

    // ... filter and render (see streaming section below)
  }
  ```

  ```vue Vue theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script setup lang="ts">
  import { useStream } from "@langchain/vue";
  import { AIMessage } from "langchain";
  import { computed } from "vue";

  const stream = useStream<typeof myAgent>({
    apiUrl: "http://localhost:2024",
    assistantId: "generative_ui",
  });

  const aiMessage = computed(() => stream.messages.value.find(AIMessage.isInstance));
  const rawSpec = computed(() => aiMessage.value?.tool_calls?.[0]?.args);
  </script>
  ```

  ```svelte Svelte theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  <script lang="ts">
    import { useStream } from "@langchain/svelte";
    import { AIMessage } from "langchain";

    const stream = useStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "generative_ui",
    });

    const aiMessage = $derived(stream.messages.find((m) => AIMessage.isInstance(m)));
    const rawSpec = $derived(aiMessage?.tool_calls?.[0]?.args);
  </script>
  ```

  ```ts Angular theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { Component } from "@angular/core";
  import { injectStream } from "@langchain/angular";
  import { AIMessage } from "langchain";

  @Component({
    selector: "app-generative-ui",
    template: `...`,
  })
  export class GenerativeUIComponent {
    stream = injectStream<typeof myAgent>({
      apiUrl: "http://localhost:2024",
      assistantId: "generative_ui",
    });

    get rawSpec() {
      const ai = this.stream.messages().find(AIMessage.isInstance);
      return ai?.tool_calls?.[0]?.args;
    }
  }
  ```
</CodeGroup>

## Stream and render progressively

During streaming, the spec is built up incrementally. Elements arrive one at a
time and may initially lack `type` or `props`. Filter to only complete elements
and pass `loading={true}` to the `Renderer`, which tells it to silently skip
children that haven't arrived yet. The UI builds up component by component:

```tsx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
/*
 * Filter the streamed spec to only include elements with valid type/props,
 * enabling progressive rendering as the AI response builds up. Passing
 * loading={true} to the Renderer tells it to skip missing children silently.
 */
const spec = (() => {
  if (!rawSpec?.root || !rawSpec?.elements) return null;
  const rootEl = rawSpec.elements[rawSpec.root];
  if (!rootEl?.type || rootEl?.props == null) return null;

  const safeElements = {};
  for (const [key, el] of Object.entries(rawSpec.elements)) {
    if (el?.type && el?.props != null) {
      safeElements[key] = el;
    }
  }
  return { root: rawSpec.root, elements: safeElements };
})();

return (
  <>
    {spec && (
      <JSONUIProvider registry={registry}>
        <Renderer spec={spec} registry={registry} loading={stream.isLoading} />
      </JSONUIProvider>
    )}
  </>
);
```

<Note>
  The `JSONUIProvider` is required to set up json-render's internal context
  providers (state, visibility, validation, actions). The `Renderer` component
  must be rendered inside it.
</Note>

## The spec format

The AI agent generates a flat JSON spec with a `root` key pointing to the
root element and an `elements` map containing all components:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "root": "login-card",
  "elements": {
    "login-card": {
      "type": "Card",
      "props": { "title": "Login" },
      "children": ["login-stack"]
    },
    "login-stack": {
      "type": "Stack",
      "props": { "direction": "vertical", "gap": "md" },
      "children": ["email-input", "password-input", "submit-btn"]
    },
    "email-input": {
      "type": "TextInput",
      "props": { "label": "Email", "placeholder": "Enter your email", "type": "email" },
      "children": []
    },
    "password-input": {
      "type": "TextInput",
      "props": { "label": "Password", "placeholder": "Enter your password", "type": "password" },
      "children": []
    },
    "submit-btn": {
      "type": "Button",
      "props": { "label": "Sign In", "variant": "primary", "fullWidth": true },
      "children": []
    }
  }
}
```

Each element references its children by ID, and leaf elements like `TextInput`
and `Button` have empty `children` arrays.

## Best practices

* **Use descriptive component descriptions**: the AI uses these to understand when
  to use each component. Clear descriptions lead to better UI generation.
* **Validate before rendering**: always check that elements have valid `type` and
  non-null `props` before passing to the Renderer, since streaming delivers partial data.
* **Design for streaming**: pass `loading={true}` during streaming so the Renderer
  gracefully handles children that haven't arrived yet. Users see the UI build up
  in real time rather than waiting for the full response.
* **Style with design tokens**: use CSS custom properties so rendered components
  adapt to light and dark themes automatically.
* **Wrap with JSONUIProvider**: the `Renderer` must be inside a `JSONUIProvider`
  to access json-render's internal context for state, visibility, and actions.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/frontend/generative-ui.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
