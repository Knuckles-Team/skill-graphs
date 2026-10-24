# Run the agent and wait for the final response
curl -s -X POST "http://127.0.0.1:2024/threads/$THREAD/runs/wait" \
  -H "Content-Type: application/json" \
  -d '{
    "assistant_id": "adk_echo",
    "input": {"messages": [{"type": "human", "content": "Hello"}]}
  }'
```

## Deploy to LangSmith

Once the agent runs locally, deploy it to LangSmith with `langgraph deploy`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph deploy --name my-adk-agent
```

For environment configuration, deployment types, and revision management, refer to [Deploy to cloud](/langsmith/deploy-to-cloud). For self-hosted setups, refer to [Self-hosted deployments](/langsmith/self-hosted).

## Enable tracing

`wrap()` calls `langsmith.integrations.google_adk.configure_google_adk()` automatically whenever LangSmith tracing is enabled, so all you need to do is set the environment variables on the deployment:

```bash .env theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=my-adk-agent     # optional
GOOGLE_API_KEY=your-google-api-key
```

[Traces](/langsmith/observability) show agent invocations, tool calls, and LLM interactions in the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-deploy-google-adk). For more on the underlying tracing integration, see [Trace Google ADK applications](/langsmith/trace-with-google-adk).

## API reference

### `wrap(runner)`

Wraps a configured `google.adk.runners.Runner` and returns a LangGraph `Pregel` graph that can be exported from your module and served by Agent Server.

| Argument | Type                        | Description                                                                             |
| -------- | --------------------------- | --------------------------------------------------------------------------------------- |
| `runner` | `google.adk.runners.Runner` | A configured ADK Runner. Its `session_service` **must** be a `LangsmithSessionService`. |

**Returns:** A `Pregel` graph whose name is `runner.app_name`.

**Raises:** `TypeError` if `runner.session_service` is not a `LangsmithSessionService`.

If `runner.agent` defines an `output_key`, that key's value is also exposed on the graph's output, in addition to `messages`. This is what makes ADK structured-output agents (`output_schema=...`, `output_key=...`) work with Studio and the `/runs/wait` response.

### `LangsmithSessionService`

A `google.adk.sessions.BaseSessionService` implementation backed by Agent Server's checkpoint store. The wrapper manages session lifecycle automatically. It creates a session on the first turn of a thread, loads it from the checkpoint on subsequent turns, and writes the updated session back when the run completes.

Use a fresh instance per `Runner`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
session_service = LangsmithSessionService()
```

You should not need to call its methods directly; `wrap()` drives them through ADK's normal session lifecycle.

### `ADKInput`

The default input schema for a wrapped agent.

| Field         | Type                     | Description                                                                                                           |
| ------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `messages`    | `list[AnyMessage]`       | (Required) Conversation messages; the wrapper sends `messages[-1].content` to the ADK runner as the new user message. |
| `state_delta` | `dict[str, Any] \| None` | (Optional) Passed through to `runner.run_async(state_delta=...)` to mutate ADK session state for this turn.           |

### `ADKOutput`

The default output schema for a wrapped agent.

| Field      | Type               | Description                                                                                   |
| ---------- | ------------------ | --------------------------------------------------------------------------------------------- |
| `messages` | `list[AnyMessage]` | The agent's response messages, appended to the thread via LangGraph's `add_messages` reducer. |

Exposing `messages` as a typed field (rather than a plain `dict`) is what lets Studio detect the graph as chat-compatible and enable the chat-mode toggle.

## How it works

When a run arrives:

1. The wrapped graph reads `thread_id` from the run config and uses it as the ADK `session_id`. If [authentication](/langsmith/auth) is enabled, the authenticated user's id becomes the ADK `user_id`; otherwise the user id is `"anonymous"`.
2. The wrapper loads the previous session (if any) from the LangGraph checkpoint into `LangsmithSessionService`, then asks the runner to handle the latest message.
3. The runner emits ADK events. The wrapper forwards partial-token events through LangGraph's async callback manager so they stream out via `stream_mode="messages"`, and collects final text for the response message.
4. When the run finishes, the wrapper serializes the ADK session and saves it to the checkpoint via `entrypoint.final(save=...)`. The next run on the same thread resumes from that state.

This means ADK's own session/state semantics are preserved end-to-end while the deployment gets the standard Agent Server features: durable runs, streaming, multi-thread persistence, and tracing.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-google-adk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deploy other frameworks
Source: https://docs.langchain.com/langsmith/deploy-other-frameworks

Deploy agents built with Strands, CrewAI, or other frameworks to LangSmith using the LangGraph Functional API.

This guide shows you how to use [Functional API](/oss/python/langgraph/functional-api) to deploy a [Strands Agent](https://strandsagents.com/latest/documentation/docs/) on [LangSmith Deployment](/langsmith/deployment) and set up tracing for [LangSmith Observability](/langsmith/observability). You can follow the same approach with other frameworks like CrewAI and AutoGen.

To deploy Google ADK agents, refer to [Deploy Google ADK agents](/langsmith/deploy-google-adk).

Using Functional API and deploying to LangSmith Deployment provides several benefits:

* Production deployment: Deploy your integrated solution to [LangSmith Deployment](/langsmith/deployment) for scalable production use.
* Enhanced features: With Functional API, you can integrate your existing agents with [persistence](/oss/python/langgraph/persistence), [streaming](/langsmith/streaming), [short and long-term memory](/oss/python/concepts/memory) and more, with minimal changes to your existing code.
* Multi-agent systems: Build [multi-agent systems](/oss/python/langchain/multi-agent) where individual agents are built with different frameworks.

## Prerequisites

* Python 3.9+
* Dependencies: `pip install strands-agents strands-agents-tools langgraph`
* AWS Credentials in your environment

## 1. Define strands agent

Create a Strands Agent with prebuilt tools.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from strands import Agent
from strands_tools import file_read, file_write, python_repl, shell, journal

agent = Agent(
        tools=[file_read, file_write, python_repl, shell, journal],
        system_prompt="You are an Expert Software Developer Assistant specializing in web frameworks. Your task is to analyze project structures and identify mappings.",
        model="us.anthropic.claude-sonnet-4-20250514-v1:0",
    )
```

## 2. Use Functional API to deploy on LangSmith Deployment

[Functional API](/oss/python/langgraph/functional-api) allows you to integrate and deploy with frameworks other than LangChain. Functional API also provides the additional benefit to leverage other key features—persistence, memory, human-in-the-loop, and streaming—coupled with your existing agent, with minimal changes to your existing code.

It uses two key building blocks:

* **[`@entrypoint`](https://reference.langchain.com/python/langgraph/func/entrypoint)**: Marks a function as the starting point of a workflow, encapsulating logic and managing execution flow, including handling long-running tasks and interrupts.
* **[`@task`](https://reference.langchain.com/python/langgraph/func/task)**: Represents a discrete unit of work, such as an API call or data processing step, that can be executed asynchronously within an entrypoint. Tasks return a future-like object that can be awaited or resolved synchronously.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from strands.types.content import Message

from langgraph.func import entrypoint, task
import operator

@task
def invoke_strands(messages: list[Message]):
    # run the agent with existing messages; can invoke with the final message with messages[-1]
    result = agent(messages)
    # return the resulting message
    return [result.message]

@entrypoint()
def workflow(messages: list[Message], previous: list[Message]):
    messages = operator.add(previous or [], messages)
    response = invoke_strands(messages).result()
    return entrypoint.final(value=response, save=operator.add(messages, response))
```

## 3. Set up tracing with OpenTelemetry

In your environment variables, set up the following:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Turn off LangSmith default tracing, as we want to only trace with OpenTelemetry
LANGSMITH_TRACING=false

OTEL_EXPORTER_OTLP_ENDPOINT = "https://api.smith.langchain.com/otel/"

OTEL_EXPORTER_OTLP_HEADERS = "x-api-key=your-langsmith-api-key,Langsmith-Project=your-tracing-project-name"
```

<Note>
  If you're [self-hosting LangSmith](/langsmith/self-hosted), replace the  `OTEL_EXPORTER_OTLP_ENDPOINT` endpoint with your LangSmith API endpoint and append `/api/v1/otel`. For example: `OTEL_EXPORTER_OTLP_ENDPOINT = "https://ai-company.com/api/v1/otel"`
</Note>

<Note>
  Strand's OTel tracing contains synchronous code. In this case, you may need to set `BG_JOB_ISOLATED_LOOPS=true` to execute background runs in an isolated event loop separate from the serving API event loop. This only prevents health-check failures; the synchronous tracing code still degrades throughput and tail latency under load. See [`BG_JOB_ISOLATED_LOOPS`](/langsmith/env-var#bg_job_isolated_loops) for recommended async alternatives.
</Note>

In your main agent, set up the following:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from strands.telemetry import StrandsTelemetry

strands_telemetry = StrandsTelemetry()
strands_telemetry.setup_otlp_exporter()
strands_telemetry.setup_meter()
```

## 4. Prepare for deployment

From here, to deploy to LangSmith, create a file structure like the following:

```
my-strands-agent/
├── agent.py          # Your main agent code
├── requirements.txt  # Python dependencies
└── langgraph.json   # LangGraph configuration
```

To deploy your agent, follow the [Deploy to cloud](/langsmith/deploy-to-cloud) guide.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-other-frameworks.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
