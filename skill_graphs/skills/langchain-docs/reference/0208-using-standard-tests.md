# Using standard tests
Source: https://docs.langchain.com/oss/python/contributing/standard-tests-langchain

**Standard tests ensure your integration works as expected.**

When creating either a custom class for yourself or to publish in a LangChain integration, it is necessary to add tests to ensure it works as expected. LangChain provides a comprehensive [set of tests](https://pypi.org/project/langchain-tests/) for each integration type for you. This guide will show you how to add LangChain's standard test suite to each integration type.

## Setup

First, install the required dependencies:

<CardGroup>
  <Card title="langchain-core" icon="cube" href="https://github.com/langchain-ai/langchain/tree/master/libs/core#readme">
    Defines the interfaces we want to import to define our custom components
  </Card>

  <Card title="langchain-tests" icon="flask" href="https://github.com/langchain-ai/langchain/tree/master/libs/standard-tests#readme">
    Provides the standard tests and `pytest` plugins necessary to run them
  </Card>
</CardGroup>

<Warning>
  Because added tests in new versions of `langchain-tests` can break your CI/CD pipelines, we recommend pinning to the latest version of [`langchain-tests`](https://pypi.org/project/langchain-tests/#history) to avoid unexpected changes.
</Warning>

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U langchain-core
  pip install -U langchain-tests
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add langchain-core
  uv add langchain-tests
  ```
</CodeGroup>

There are 2 namespaces in the `langchain-tests` package:

<AccordionGroup>
  <Accordion title="Unit tests" icon="settings">
    **Location**: `langchain_tests.unit_tests`

    Designed to test the component in isolation and without access to external services

    [View API reference](https://reference.langchain.com/python/langchain_tests/unit_tests)
  </Accordion>

  <Accordion title="Integration tests" icon="network">
    **Location**: `langchain_tests.integration_tests`

    Designed to test the component with access to external services (in particular, the external service that the component is designed to interact with)

    [View API reference](https://reference.langchain.com/python/langchain_tests/integration_tests)
  </Accordion>
</AccordionGroup>

Both types of tests are implemented as [`pytest`](https://docs.pytest.org/en/stable/) class-based test suites.

## Implementing standard tests

Depending on your integration type, you will need to implement either or both unit and integration tests.

By subclassing the standard test suite for your integration type, you get the full collection of standard tests for that type. For a test run to be successful, the a given test should pass only if the model supports the capability being tested. Otherwise, the test should be skipped.

Because different integrations offer unique sets of features, most standard tests provided by LangChain are **opt-in by default** to prevent false positives. Consequently, you will need to override properties to indicate which features your integration supports - see the below example for an illustration.

```python tests/integration_tests/test_standard.py theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Indicate that a chat model supports image inputs

class TestChatParrotLinkStandard(ChatModelIntegrationTests):
    # ... other required properties

    @property
    def supports_image_inputs(self) -> bool:
        return True  # (The default is False)
```

<Note>
  You should organize tests in these subdirectories relative to the root of your package:

  * `tests/unit_tests` for unit tests
  * `tests/integration_tests` for integration tests
</Note>

To see the complete list of configurable capabilities and their defaults, visit the [API reference](https://reference.langchain.com/python/langchain_tests) for standard tests.

Here are some example implementations of standard tests from popular integrations:

<Tabs>
  <Tab title="Unit tests">
    <Columns>
      <Card title="ChatOpenAI" href="https://github.com/langchain-ai/langchain/blob/master/libs/partners/openai/tests/unit_tests/chat_models/test_base_standard.py">Unit tests</Card>
      <Card title="ChatAnthropic" href="https://github.com/langchain-ai/langchain/blob/master/libs/partners/anthropic/tests/unit_tests/test_standard.py">Unit tests</Card>
      <Card title="ChatGenAI" href="https://github.com/langchain-ai/langchain-google/blob/main/libs/genai/tests/unit_tests/test_standard.py">Unit tests</Card>
    </Columns>
  </Tab>

  <Tab title="Integration tests">
    <Columns>
      <Card title="ChatOpenAI" href="https://github.com/langchain-ai/langchain/blob/master/libs/partners/openai/tests/integration_tests/chat_models/test_base_standard.py">Integration tests</Card>
      <Card title="ChatAnthropic" href="https://github.com/langchain-ai/langchain/blob/master/libs/partners/anthropic/tests/integration_tests/test_standard.py">Integration tests</Card>
      <Card title="ChatGenAI" href="https://github.com/langchain-ai/langchain-google/blob/main/libs/genai/tests/integration_tests/test_standard.py">Integration tests</Card>
    </Columns>
  </Tab>

  <Tab title="Sandbox integration tests">
    Ensure your integration passes the standard test suite.
    See the [Daytona integration](https://github.com/langchain-ai/deepagents/blob/main/libs/partners/daytona/tests/integration_tests/test_integration.py) as an example.

    <Card title="Daytona" href="https://github.com/langchain-ai/deepagents/blob/main/libs/partners/daytona/tests/integration_tests/test_integration.py">Sandbox Integration tests</Card>
  </Tab>
</Tabs>

## Sandbox integrations

Deep Agents sandbox integrations use `SandboxIntegrationTests` from `langchain_tests.integration_tests`.
Subclass it and provide a `sandbox` fixture that yields a `SandboxBackendProtocol` instance.
Use the [Daytona integration tests](https://github.com/langchain-ai/deepagents/blob/main/libs/partners/daytona/tests/integration_tests/test_integration.py) as a reference implementation.
See [Contributing a sandbox integration](/oss/python/contributing/integrations-langchain) for publishing guidelines.

***

## Running tests

If bootstrapping an integration from a template, a `Makefile` is provided that includes targets for running unit and integration tests:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
make test
make integration_test
```

Otherwise, if you follow the recommended directory structure, you can run tests with:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Run all tests
uv run --group test pytest tests/unit_tests/
uv run --group test --group test_integration pytest -n auto tests/integration_tests/

# For certain unit tests, you may need to set certain flags and environment variables:
TIKTOKEN_CACHE_DIR=tiktoken_cache uv run --group test pytest --disable-socket --allow-unix-socket tests/unit_tests/

# Run a specific test file
uv run --group test pytest tests/integration_tests/test_chat_models.py

# Run a specific test function in a file
uv run --group test pytest tests/integration_tests/test_chat_models.py::test_chat_completions

# Run a specific test function within a class
uv run --group test pytest tests/integration_tests/test_chat_models.py::TestChatParrotLinkIntegration::test_chat_completions
```

## Troubleshooting

For a full list of the standard test suites that are available, as well as information on which tests are included and how to troubleshoot common issues, see the [Standard Tests API Reference](https://reference.langchain.com/python/langchain_tests).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/standard-tests-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# A2A server
Source: https://docs.langchain.com/oss/python/deepagents/a2a

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/a2a.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Agent Client Protocol (ACP)
Source: https://docs.langchain.com/oss/python/deepagents/acp

Expose Deep Agents over the Agent Client Protocol (ACP) to integrate with code editors and IDEs.

[Agent Client Protocol (ACP)](https://agentclientprotocol.com/get-started/introduction) standardizes communication between coding agents and code editors or IDEs.
With the ACP protocol, you can make use of your custom deep agents with any ACP-compatible client, allowing your code editor to provide project context and receive rich updates.

<Note>
  ACP is designed for agent-editor integrations. If you want your agent to call tools hosted by external servers, see [Model Context Protocol (MCP)](/oss/python/langchain/mcp/).
</Note>

## Quickstart

Install the ACP integration package:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install deepagents-acp
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add deepagents-acp
  ```
</CodeGroup>

Then expose a deep agent over ACP.

This starts an ACP server in stdio mode (it reads requests from stdin and writes responses to stdout). In practice, you usually run this as a command launched by an ACP client (for example, your editor), which then communicates with the server over stdio.

```python icon="server" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import asyncio

from acp import run_agent
from deepagents import create_deep_agent
from langgraph.checkpoint.memory import MemorySaver

from deepagents_acp.server import AgentServerACP

async def main() -> None:
    agent = create_deep_agent(
        model="google_genai:gemini-3.5-flash",
        # You can customize your deep agent here: set a custom prompt,
        # add your own tools, attach middleware, or compose subagents.
        system_prompt="You are a helpful coding assistant",
        checkpointer=MemorySaver(),
    )

    server = AgentServerACP(agent)
    await run_agent(server)

if __name__ == "__main__":
    asyncio.run(main())
```

<Card title="Example coding agent" icon="brand-github" href="https://github.com/langchain-ai/deepagents/blob/main/libs/acp/examples/demo_agent.py">
  The `deepagents-acp` package includes an example coding agent with filesystem and shell that you can run out of the box.
</Card>

## Clients

Deep agents work anywhere you can run an ACP agent server. Some notable ACP clients include:

* [Zed](https://zed.dev/docs/ai/external-agents)
* [JetBrains IDEs](https://www.jetbrains.com/help/ai-assistant/acp.html)
* Visual Studio Code (via [vscode-acp](https://github.com/formulahendry/vscode-acp))
* Neovim (via ACP-compatible plugins)

### Zed

The `deepagents` repo includes [a demo ACP entrypoint](https://github.com/langchain-ai/deepagents/blob/main/libs/acp/run_demo_agent.sh) you can register with [Zed](https://zed.dev/docs/ai/external-agents):

1. Clone the `deepagents` repo and install dependencies:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
git clone https://github.com/langchain-ai/deepagents.git
cd deepagents/libs/acp
uv sync --all-groups
chmod +x run_demo_agent.sh
```

2. Configure credentials for the demo agent:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
cp .env.example .env
```

Then set `ANTHROPIC_API_KEY` in `.env`.

3. Configure your ACP agent server command in Zed's `settings.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "agent_servers": {
    "DeepAgents": {
      "type": "custom",
      "command": "/your/absolute/path/to/deepagents/libs/acp/run_demo_agent.sh"
    }
  }
}
```

4. Open Zed's Agents panel and start a Deep Agents thread.

### Toad

If you want to run an ACP agent server as a local dev tool, you can use [Toad](https://github.com/batrachianai/toad) to manage the process.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
uv tool install -U batrachian-toad

toad acp "python path/to/your_server.py" .

# or
toad acp "uv run python path/to/your_server.py" .
```

<Info>
  See the upstream ACP docs for protocol details and editor support:

  * Introduction: [https://agentclientprotocol.com/get-started/introduction](https://agentclientprotocol.com/get-started/introduction)
  * Clients/editors: [https://agentclientprotocol.com/get-started/clients](https://agentclientprotocol.com/get-started/clients)
</Info>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/acp.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Async subagents
Source: https://docs.langchain.com/oss/python/deepagents/async-subagents

Launch background subagents that run concurrently while the supervisor continues interacting with the user

Async subagents let a supervisor agent launch background tasks that return immediately, so the supervisor can continue interacting with the user while subagents work concurrently. The supervisor can check progress, send follow-up instructions, or cancel tasks at any point.

This builds on [subagents](/oss/python/deepagents/subagents), which run synchronously and block the supervisor until completion. Use async subagents when tasks are long-running, parallelizable, or need mid-flight steering.

<Note>
  Async subagents are a preview feature available in `deepagents` 0.5.0. Preview features are under active development and APIs may change.
</Note>

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph TB
    User([User]) --> Supervisor[Supervisor Agent]

    Supervisor --> |launch| Researcher[Researcher]
    Supervisor --> |launch| Coder[Coder]

    Researcher --> |check| Supervisor
    Coder --> |check| Supervisor
```

<Note>
  Async subagents communicate with any server that implements the [Agent Protocol](https://github.com/langchain-ai/agent-protocol). You can use [LangSmith Deployments](/langsmith/deployment), or self-host any Agent Protocol-compatible server. Each subagent runs independently of the supervisor, which controls them through the SDK to launch, check, update, and cancel.
</Note>

## When to use async subagents

| Dimension            | Sync subagents                                                  | Async subagents                                                   |
| -------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Execution model**  | Supervisor blocks until subagent completes                      | Returns job ID immediately; supervisor continues                  |
| **Concurrency**      | Parallel but blocking                                           | Parallel and non-blocking                                         |
| **Mid-task updates** | Not possible                                                    | Send follow-up instructions via `update_async_task`               |
| **Cancellation**     | Not possible                                                    | Cancel running tasks via `cancel_async_task`                      |
| **Statefulness**     | Stateless -- no persistent state between invocations            | Stateful -- maintains state on its own thread across interactions |
| **Best for**         | Tasks where the agent should wait for results before continuing | Long-running, complex tasks managed interactively in a chat       |

## Configure async subagents

Define async subagents as a list of [`AsyncSubAgent`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent) specs, each pointing to an Agent Protocol server:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import AsyncSubAgent, create_deep_agent

async_subagents = [
    AsyncSubAgent(
        name="researcher",
        description="Research agent for information gathering and synthesis",
        graph_id="researcher",
        # No url → ASGI transport (co-deployed in the same deployment)
    ),
    AsyncSubAgent(
        name="coder",
        description="Coding agent for code generation and review",
        graph_id="coder",
        # url="https://coder-deployment.langsmith.dev"  # Optional: HTTP transport for remote
    ),
]

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    subagents=async_subagents,
)
```

| Field         | Type             | Description                                                                                                                                                     |
| ------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | `str`            | Required. Unique identifier. The supervisor uses this when launching tasks.                                                                                     |
| `description` | `str`            | Required. What this subagent does. The supervisor uses this to decide which agent to delegate to.                                                               |
| `graph_id`    | `str`            | Required. The graph ID (or assistant ID) on the Agent Protocol server. For LangGraph-based deployments, this must match a graph registered in `langgraph.json`. |
| `url`         | `str`            | Optional. When omitted, uses ASGI transport (in-process). When set, uses HTTP transport to a remote Agent Protocol server.                                      |
| `headers`     | `dict[str, str]` | Optional. Additional headers for requests to the remote server. Use for custom authentication with self-hosted Agent Protocol servers.                          |

For LangGraph-based deployments, register all graphs in the same `langgraph.json` for co-deployed setups:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "graphs": {
    "supervisor": "./src/supervisor.py:graph",
    "researcher": "./src/researcher.py:graph",
    "coder": "./src/coder.py:graph"
  }
}
```

## Use the async subagent tools

The [`AsyncSubAgentMiddleware`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware) which is included in the [default middleware stack](/oss/python/deepagents/customization#default-stack-main-agent) when async subagents are configured, gives the supervisor five tools:

| Tool                | Purpose                                   | Returns                       |
| ------------------- | ----------------------------------------- | ----------------------------- |
| `start_async_task`  | Start a new background task               | Task ID (immediately)         |
| `check_async_task`  | Get current status and result of a task   | Status + result (if complete) |
| `update_async_task` | Send new instructions to a running task   | Confirmation + updated status |
| `cancel_async_task` | Stop a running task                       | Confirmation                  |
| `list_async_tasks`  | List all tracked tasks with live statuses | Summary of all tasks          |

The supervisor's LLM calls these tools like any other tool. The middleware handles thread creation, run management, and state persistence automatically.

### Understand the lifecycle

A typical interaction follows this sequence:

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sequenceDiagram
    participant User
    participant Supervisor
    participant Platform as Agent Protocol Server

    User->>Supervisor: "Research topic X"
    Supervisor->>Platform: launch(researcher, "topic X")
    Platform-->>Supervisor: task_id: abc123

    Note over Platform: Researcher working...

    Supervisor-->>User: "Started task abc123"

    Note over User,Platform: User continues conversation

    User->>Supervisor: "How's the research going?"
    Supervisor->>Platform: check(abc123)
    Platform-->>Supervisor: status: success, result: "findings..."
    Supervisor-->>User: "Here are the results"
```

* **Launch** creates a new thread on the server, starts a run with the task description as input, and returns the thread ID as the task ID. The supervisor reports this ID to the user and does not poll for completion.
* **Check** fetches the current run status. If the run succeeded, it retrieves the thread state to extract the subagent's final output. If still running, it reports that to the user.
* **Update** creates a new run on the same thread with an interrupt multitask strategy. The previous run is interrupted, and the subagent restarts with the full conversation history plus the new instructions. The task ID stays the same.
* **Cancel** calls `runs.cancel()` on the server and marks the task as `"cancelled"`.
* **List** iterates over all tracked tasks. For non-terminal tasks, it fetches live status from the server in parallel. Terminal statuses (`success`, `error`, `cancelled`) are returned from cache.

## Understand state management

Task metadata is stored in a dedicated state channel (`async_tasks`) on the supervisor's graph, separate from the message history. This is critical because deep agents [compact their message history](/oss/python/deepagents/context-engineering#summarization) when the context window fills up. If task IDs were only in tool messages, they would be lost during compaction. The dedicated channel ensures the supervisor can always recall its tasks through `list_async_tasks`, even after multiple rounds of summarization.

Each tracked task records the task ID, agent name, thread ID, run ID, status, and timestamps (`created_at`, `last_checked_at`, `last_updated_at`).

## Choose a transport

### ASGI transport (co-deployed)

When a subagent spec omits the `url` field, the LangGraph SDK uses ASGI transport -- SDK calls are routed through in-process function calls rather than HTTP. For LangGraph-based deployments, this requires both graphs to be registered in the same `langgraph.json`.

ASGI transport eliminates network latency and requires no additional auth configuration. The subagent still runs as a separate thread with its own state. This is the recommended default.

### HTTP transport (remote)

Add a `url` field to switch to HTTP transport, where SDK calls go over the network to a remote Agent Protocol server:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
AsyncSubAgent(
    name="researcher",
    description="Research agent",
    graph_id="researcher",
    url="https://my-research-deployment.langsmith.dev",
)
```

For LangGraph deployments, authentication is handled by the LangGraph SDK using `LANGSMITH_API_KEY` (or `LANGGRAPH_API_KEY`) from environment variables. Self-hosted Agent Protocol servers may use a different authentication mechanism.

Use HTTP transport when subagents need independent scaling, different resource profiles, or are maintained by a different team.

## Choose a deployment topology

### Single deployment

A single deployment means all agents are co-deployed on the same server using ASGI transport. For LangGraph-based deployments, register all graphs in one `langgraph.json`. This is the recommended starting point -- one server to manage, zero network latency between agents.

### Split deployment

Supervisor on one server, subagents on another via HTTP transport. Use when subagents need different compute profiles or independent scaling.

### Hybrid

In a hybrid deployment, some subagents are co-deployed via ASGI, others remote via HTTP:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async_subagents = [
    AsyncSubAgent(
        name="researcher",
        description="Research agent",
        graph_id="researcher",
        # No url → ASGI (co-deployed)
    ),
    AsyncSubAgent(
        name="coder",
        description="Coding agent",
        graph_id="coder",
        url="https://coder-deployment.langsmith.dev",
        # url present → HTTP (remote)
    ),
]
```

## Best practices

### Size the worker pool for local development

When running locally with `langgraph dev`, increase the worker pool to accommodate concurrent subagent runs. Each active run occupies a worker slot. A supervisor with 3 concurrent subagent tasks requires 4 slots (1 supervisor + 3 subagents). Under-provisioning causes launches to queue.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langgraph dev --n-jobs-per-worker 10
```

### Write clear subagent descriptions

The supervisor uses descriptions to decide which subagent to launch. Be specific and action-oriented:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Good
AsyncSubAgent(
    name="researcher",
    description="Conducts in-depth research using web search. Use for questions requiring multiple searches and synthesis.",
    graph_id="researcher",
)

# Bad
AsyncSubAgent(
    name="helper",
    description="helps with stuff",
    graph_id="helper",
)
```

### Trace with thread IDs

When using LangGraph-based deployments, every async subagent run is a standard LangGraph run, fully visible in LangSmith. The supervisor's trace shows tool calls for `launch`, `check`, `update`, `cancel`, and `list`. Each subagent run appears as a separate trace, linked by thread ID. Use the thread ID (task ID) to correlate supervisor orchestration traces with subagent execution traces.

## Troubleshooting

### Supervisor polls immediately after launch

**Problem**: The supervisor calls `check` in a loop right after launching, turning async execution into blocking.

**Solution**: The middleware injects system prompt rules to prevent this. If polling persists, reinforce the behavior in your supervisor's system prompt:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    system_prompt="""...your instructions...

    After launching an async subagent, ALWAYS return control to the user.
    Never call check_async_task immediately after launch.""",
    subagents=async_subagents,
)
```

### Supervisor reports stale status

**Problem**: The supervisor references a task status from earlier in conversation history instead of making a fresh `check` call.

**Solution**: The middleware prompt instructs the model that "task statuses in conversation history are always stale." If this still occurs, add explicit instructions to always call `check` or `list` before reporting status.

### Task ID lookup failures

**Problem**: The supervisor truncates or reformats the task ID, causing `check` or `cancel` to fail.

**Solution**: The middleware prompt instructs the model to always use the full task ID. If truncation persists, this is typically a model-specific issue -- try a different model or add "always show the full task\_id, never truncate or abbreviate it" to your system prompt.

### Subagent launches queue instead of running

**Problem**: Launching a subagent hangs or takes a long time to start.

**Solution**: The worker pool is likely exhausted. Increase the pool size with `--n-jobs-per-worker`. See [Size the worker pool](#size-the-worker-pool-for-local-development).

## Reference implementation

The [async-deep-agents](https://github.com/langchain-ai/async-deep-agents) repository contains working examples in both Python and TypeScript that deploy to LangSmith Deployments. It demonstrates a supervisor with researcher and coder subagents running as background tasks.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/async-subagents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
