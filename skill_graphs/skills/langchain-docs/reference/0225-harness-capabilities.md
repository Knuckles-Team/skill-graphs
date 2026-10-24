# Harness capabilities
Source: https://docs.langchain.com/oss/python/deepagents/harness

A Deep Agents harness provides four categories of built-in capabilities that make building long-running, reliable agents easier:

<CardGroup>
  <Card title="Execution environment" icon="bolt" href="#execution-environment">
    Tools, virtual filesystem, optional sandbox, and REPL (interpreter)
  </Card>

  <Card title="Context management" icon="database" href="#context-management">
    Skills, memory, summarization, context offloading, and prompt caching
  </Card>

  <Card title="Delegation" icon="sitemap" href="#delegation">
    Subagent spawning and task planning
  </Card>

  <Card title="Steering" icon="user" href="#steering">
    Human-in-the-loop approval and interrupts
  </Card>
</CardGroup>

Alongside these four components, [harness profiles](#harness-profiles) let you package per-model configuration into reusable bundles.

<img alt="The Deep Agents open harness: planning, virtual filesystem, permissions, subagents, context management, code execution, human-in-the-loop, skills, and memory" />

## Execution environment

The execution environment is where an agent acts. It has four layers:

* **[Tools](#tools)**: custom functions, APIs, and databases the agent can call
* **[Virtual filesystem](#virtual-filesystem-access)**: file tools backed by pluggable backends
* **[Filesystem permissions](#filesystem-permissions)**: declarative access control over which paths agents can read or write
* **[Code execution](#code-execution)**: sandboxed shell execution and an in-process JavaScript interpreter

### Tools

Pass any Python callable, LangChain tool, or tool dict to `create_deep_agent` via the `tools=` parameter. These are the domain-specific actions your agent can take—web search, database queries, API calls, or any function you define.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    tools=[search, fetch_page, run_query],
)
```

For more information on defining custom tools, using MCP servers, and the full list of built-in harness tools, see [Tools](/oss/python/deepagents/tools).

### Virtual filesystem access

The harness provides a configurable virtual filesystem which can be backed by different pluggable backends.
The backends support the following file system operations:

| Tool         | Description                                                                                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ls`         | List files in a directory with metadata (size, modified time)                                                                                                                                                            |
| `read_file`  | Read file contents with line numbers, supports offset/limit for large files. Also supports returning multimodal content blocks for non-text files (images, video, audio, and documents). See supported extensions below. |
| `write_file` | Create new files                                                                                                                                                                                                         |
| `edit_file`  | Perform exact string replacements in files (with global replace mode)                                                                                                                                                    |
| `glob`       | Find files matching patterns (e.g., `**/*.py`)                                                                                                                                                                           |
| `grep`       | Search file contents with multiple output modes (files only, content with context, or counts)                                                                                                                            |
| `execute`    | Run shell commands in the environment (available with [sandbox backends](/oss/python/deepagents/sandboxes) only)                                                                                                         |

<Accordion title="Supported multimodal file extensions">
  | Type                                               | Extensions                                                                |
  | -------------------------------------------------- | ------------------------------------------------------------------------- |
  | [Image](/oss/python/langchain/messages#multimodal) | `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.heic`, `.heif`                |
  | [Video](/oss/python/langchain/messages#multimodal) | `.mp4`, `.mpeg`, `.mov`, `.avi`, `.flv`, `.mpg`, `.webm`, `.wmv`, `.3gpp` |
  | [Audio](/oss/python/langchain/messages#multimodal) | `.wav`, `.mp3`, `.aiff`, `.aac`, `.ogg`, `.flac`                          |
  | [File](/oss/python/langchain/messages#multimodal)  | `.pdf`, `.ppt`, `.pptx`                                                   |
</Accordion>

<Accordion title="Running without the default filesystem tools" icon="ban">
  To hide the filesystem tools listed above from the model, register a [harness profile](#harness-profiles) with `excluded_tools`:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import HarnessProfile, register_harness_profile

  register_harness_profile(
      "anthropic:claude-sonnet-4-6",
      HarnessProfile(
          excluded_tools=frozenset(
              {"ls", "read_file", "write_file", "edit_file", "glob", "grep"}
          ),
      ),
  )
  ```

  Removing [`FilesystemMiddleware`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware) itself via `excluded_middleware` is intentionally rejected—it is required scaffolding in the [default middleware stack](/oss/python/deepagents/customization#default-stack-main-agent). Use `excluded_tools` to hide only the model-visible tool surface and leave the middleware in place. To remove the `task` tool, see [Running without subagents](/oss/python/deepagents/subagents#running-without-subagents).
</Accordion>

The virtual filesystem is used by several other harness capabilities such as skills, memory, code execution, and context management.
You can also use the file system when building custom tools and middleware for Deep Agents.

For more information, see [backends](/oss/python/deepagents/backends).

### Filesystem permissions

The harness supports declarative permission rules that control which files and directories the agent can read or write. Permissions apply to the built-in filesystem tools listed above and are evaluated in declaration order with first-match-wins semantics.

**How it works:**

* Pass a list of rules to `permissions=` when creating the agent
* Each rule specifies `operations` (`"read"`, `"write"`), `paths` (glob patterns), and `mode` (`"allow"` or `"deny"`)
* The first matching rule wins. If no rule matches, the operation is allowed.

**Why it's useful:**

* Restrict agents to specific directories (e.g., `/workspace/`)
* Protect sensitive files (e.g., `.env`, credentials)
* Give subagents narrower access than the parent agent

Permissions do not apply to [sandbox backends](/oss/python/deepagents/sandboxes), which support arbitrary command execution via the `execute` tool. For custom validation logic, use [backend policy hooks](/oss/python/deepagents/backends#add-policy-hooks).

For the full rule structure, examples, and subagent inheritance, see [Permissions](/oss/python/deepagents/permissions).

### Code execution

Deep Agents supports code execution in two ways:

* [Sandbox backends](/oss/python/deepagents/sandboxes) expose an `execute` tool for shell commands in an isolated environment.
* [Interpreters](/oss/python/deepagents/interpreters) add an `eval` tool that runs JavaScript in a scoped QuickJS runtime.

Use sandbox backends when the agent needs to install dependencies, run tests, call CLIs, or work with an operating-system filesystem. Sandbox backends implement the `SandboxBackendProtocolV2`; when detected, the harness adds the `execute` tool to the agent's available tools.

Use interpreters when the agent needs a lightweight programmable layer for loops, batching, deterministic data transformations, or programmatic tool calling. Interpreters do not provide shell access, package installs, or filesystem and network access.

For sandbox setup, providers, and file transfer APIs, see [Sandboxes](/oss/python/deepagents/sandboxes). For the QuickJS runtime and programmatic tool calling, see [Interpreters](/oss/python/deepagents/interpreters).

## Context management

The context management component controls what the agent knows, how long it can operate within token limits, and what it retains across sessions. It has four layers:

* **[Skills](#skills)**—on-demand domain knowledge loaded progressively from skill files
* **[Memory](#memory)**—persistent instructions and preferences loaded at startup from `AGENTS.md` files
* **[Summarization and context offloading](#summarization-and-context-offloading)**—automatic compression of conversation history and large tool results
* **[Prompt caching](#prompt-caching)**—static prompt sections are cache-eligible to speed up inference and reduce cost on supported models

### Skills

The harness supports skills that provide specialized workflows and domain knowledge to your deep agent.

**How it works:**

* Skills follow the [Agent Skills standard](https://agentskills.io/)
* Each skill is a directory containing a `SKILL.md` file with instructions and metadata
* Skills can include additional scripts, reference docs, templates, and other resources
* Skills use progressive disclosure—they are only loaded when the agent determines they're useful for the current task
* Agent reads frontmatter from each `SKILL.md` file at startup, then reviews full skill content when needed

**Why it's useful:**

* Reduces token usage by only loading relevant skills when needed
* Bundles capabilities together into larger actions with additional context
* Provides specialized expertise without cluttering the system prompt
* Enables modular, reusable agent capabilities

For more information, see [Skills](/oss/python/deepagents/skills).

### Memory

The harness supports persistent memory files that provide extra context to your deep agent across conversations.
These files often contain general coding style, preferences, conventions, and guidelines that help the agent understand how to work with your codebase and follow your preferences.

**How it works:**

* Uses [`AGENTS.md` files](https://agents.md/) to provide persistent context
* Memory files are always loaded (unlike skills, which use progressive disclosure)
* Pass one or more file paths to the `memory` parameter when creating your agent
* Files are stored in the agent's backend (StateBackend, StoreBackend, or FilesystemBackend)
* The agent can update memory based on your interactions, feedback, and identified patterns

**Why it's useful:**

* Provides persistent context that does not need to be re-specified each conversation
* Useful for storing user preferences, project guidelines, or domain knowledge
* Always available to the agent, ensuring consistent behavior

For configuration details and examples, see [Memory](/oss/python/deepagents/customization#memory).

### Summarization and context offloading

The harness manages context so deep agents can handle long-running tasks within token limits while retaining the information they need.

**How it works:**

* **Input context**—System prompt, memory, skills, and tool prompts shape what the agent knows at startup
* **Compression**—Built-in offloading and summarization keep context within window limits as tasks progress
* **Isolation**—Subagents quarantine heavy work and return only results (see [Delegation](#delegation))
* **Long-term memory**—Persistent storage across threads via the virtual filesystem

**Why it's useful:**

* Enables multi-step tasks that exceed a single context window
* Keeps the most relevant information in scope without manual trimming
* Reduces token usage through automatic summarization and offloading

For configuration details, see [Context engineering](/oss/python/deepagents/context-engineering).

### Prompt caching

For Anthropic models, `create_deep_agent` automatically applies prompt caching to static sections of the system prompt—the base agent instructions, memory, and skill content that repeat on every turn. This avoids reprocessing the same tokens across calls, reducing both latency and cost on long-running agents.

Prompt caching is enabled by default when using an Anthropic model. No configuration is required.

For other providers, see [Middleware integrations](/oss/python/integrations/middleware#official-integrations) for available provider-specific caching middleware.

## Delegation

The delegation component enables agents to break large problems into smaller, parallelizable units of work. It has two layers:

* **[Task planning](#task-planning)**: a built-in `write_todos` tool for structured task tracking
* **[Subagents](#subagents)**: ephemeral child agents that handle isolated subtasks

### Task planning

The harness provides a `write_todos` tool that agents can use to maintain a structured task list.

**Features:**

* Track multiple tasks with statuses (`'pending'`, `'in_progress'`, `'completed'`)
* Persisted in agent state
* Helps agent organize complex multi-step work
* Useful for long-running tasks and planning

### Subagents

The harness allows the main agent to create ephemeral "subagents" for isolated multi-step tasks.

**Why it's useful:**

* **Context isolation**—Subagent's work does not clutter main agent's context
* **Parallel execution**—Multiple subagents can run concurrently
* **Specialization**—Subagents can have different tools and configurations
* **Token efficiency**—Large subtask context is compressed into a single result

**How it works:**

* Main agent has a `task` tool
* When invoked, it creates a fresh agent instance with its own context
* Subagent executes autonomously until completion
* Returns a single final report to the main agent
* Can use [default `general-purpose` subagent](/oss/python/deepagents/subagents#default-subagent) (enabled by default) or add [custom subagents](/oss/python/deepagents/subagents#custom-subagents)
* Subagents are stateless (cannot send multiple messages back)

<Accordion title="Running without subagents (no `task` tool)" icon="ban">
  To run an agent without the `task` tool, see [Running without subagents](/oss/python/deepagents/subagents#running-without-subagents). Do not try removing [`SubAgentMiddleware`](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware) via `excluded_middleware`—that is intentionally rejected. Instead, disable the auto-added subagent via the [harness profile](#harness-profiles) and pass no synchronous subagents via `subagents=`. Async subagents are unaffected. See the [default middleware stack](/oss/python/deepagents/customization#default-stack-main-agent) for the full ordering.
</Accordion>

For more information, see [Subagents](/oss/python/deepagents/subagents).

## Steering

The steering component gives humans control over agent behavior at runtime.

### Human-in-the-loop

The harness can pause agent execution at specified tool calls to allow human approval or modification. This feature is opt-in via the `interrupt_on` parameter.

**Configuration:**

* Pass `interrupt_on` to `create_deep_agent` with a mapping of tool names to interrupt configurations
* Example: `interrupt_on={"edit_file": True}` pauses before every edit
* You can provide approval messages or modify tool inputs when prompted

**Why it's useful:**

* Safety gates for destructive operations
* User verification before expensive API calls
* Interactive debugging and guidance

For more information, see [Human-in-the-loop](/oss/python/deepagents/human-in-the-loop).

## Harness profiles

The harness can apply a declarative configuration bundle (a `HarnessProfile`) whenever a given provider or model is selected. Profiles tune runtime behavior after the model is built, without requiring per-agent setup code.

**How it works:**

* Register a profile under a provider name (`"openai"`) or a `provider:model` key (`"openai:gpt-5.5"`)
* `create_deep_agent` looks up and applies the profile when resolving the model
* Provider-level and model-level profiles merge at resolution time

**Why it's useful:**

* Package per-provider or per-model defaults (system-prompt tweaks, tool overrides, middleware) in one place
* Keep the `create_deep_agent` call site unchanged when switching models
* Ship reusable profiles as plugins via entry points

For the full field list, merge semantics, and plugin packaging, see [Profiles](/oss/python/deepagents/profiles).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/harness.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Human-in-the-loop
Source: https://docs.langchain.com/oss/python/deepagents/human-in-the-loop

Learn how to configure human approval for sensitive tool operations

Some tool operations may be sensitive and require human approval before execution. Deep Agents support human-in-the-loop workflows through LangGraph's interrupt capabilities. You can configure which tools require approval using the `interrupt_on` parameter. When `interrupt_on` is set, `HumanInTheLoopMiddleware` is added to the [default middleware stack](/oss/python/deepagents/customization#default-stack-main-agent). If a run is cancelled or interrupted before a tool returns a result, [`PatchToolCallsMiddleware`](https://reference.langchain.com/python/deepagents/middleware/patch_tool_calls/PatchToolCallsMiddleware) in the same stack repairs the message history automatically.

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph LR
    Agent[Agent] --> Check{Interrupt?}
    Check --> |no| Execute[Execute]
    Check --> |yes| Human{Human}

    Human --> |approve| Execute
    Human --> |edit| Execute
    Human --> |reject| ToolMessage[ToolMessage]
    Human --> |respond| ToolMessage

    Execute --> Agent
    ToolMessage --> Agent

    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef decision fill:#FDF3FF,stroke:#7E65AE,stroke-width:2px,color:#504B5F
    classDef alert fill:#F8E8E6,stroke:#B27D75,stroke-width:2px,color:#634643

    class Agent trigger
    class Check,Human decision
    class Execute process
    class ToolMessage process
```

## Basic configuration

The `interrupt_on` parameter accepts a dictionary mapping tool names to interrupt configurations. Each tool can be configured with:

* **`True`**: Enable interrupts with default behavior (approve, edit, reject, respond allowed)
* **`False`**: Disable interrupts for this tool
* **`InterruptOnConfig`**: Custom configuration. Set `allowed_decisions` to control review options.
  In Python, add an optional `when` predicate to interrupt only specific calls (see [Conditional interrupts](#conditional-interrupts)).

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.tools import tool
  from deepagents import create_deep_agent
  from langgraph.checkpoint.memory import MemorySaver

  @tool
  def remove_file(path: str) -> str:
      """Delete a file from the filesystem."""
      return f"Deleted {path}"

  @tool
  def fetch_file(path: str) -> str:
      """Read a file from the filesystem."""
      return f"Contents of {path}"

  @tool
  def notify_email(to: str, subject: str, body: str) -> str:
      """Send an email."""
      return f"Sent email to {to}"

  # Checkpointer is REQUIRED for human-in-the-loop
  checkpointer = MemorySaver()

  agent = create_deep_agent(
      model="ollama:devstral-2",
      tools=[remove_file, fetch_file, notify_email],
      interrupt_on={
          "remove_file": True,  # Default: approve, edit, reject, respond
          "fetch_file": False,  # No interrupts needed
          "notify_email": {"allowed_decisions": ["approve", "reject"]},  # No editing
      },
      checkpointer=checkpointer,  # Required!
  )
  ```
</CodeGroup>

## Decision types

The `allowed_decisions` list controls what actions a human can take when reviewing a tool call:

* **`"approve"`**: Execute the tool with the original arguments as proposed by the agent
* **`"edit"`**: Modify the tool arguments before execution
* **`"reject"`**: Skip executing this tool call entirely and return rejection feedback to the agent
* **`"respond"`**: Return the human's message directly as the tool result, skipping execution, for "ask user" style tools

Use `reject` when the human denies a proposed action. Use `respond` only when the human is acting as the tool, such as answering an `ask_user` prompt. Do not use `respond` to deny side-effecting tools, because its message may be treated by the model as a successful tool result.

You can customize which decisions are available for each tool:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
interrupt_on = {
    # Sensitive operations: allow all options
    "delete_file": {"allowed_decisions": ["approve", "edit", "reject"]},

    # Moderate risk: approval or rejection only
    "write_file": {"allowed_decisions": ["approve", "reject"]},

    # Must approve (no rejection allowed)
    "critical_operation": {"allowed_decisions": ["approve"]},
}
```

## Conditional interrupts

By default, every tool call listed in `interrupt_on` pauses for review. To pause only some calls, add a `when` predicate to a tool's `InterruptOnConfig`. The predicate receives a [ToolCallRequest](https://reference.langchain.com/python/langgraph.prebuilt/tool_node/ToolCallRequest) and returns `True` to interrupt or `False` to auto-approve, so you can gate on the tool's arguments.

<Note>
  Conditional interrupts require `langchain>=1.3.3`.
</Note>

<HitlConditionalInterruptsPy />

When the `when` predicate returns `False`, the call runs without interrupting. When it returns `True`, or when you omit `when`, the call pauses as usual. Calls that evaluate to `False` are never added to the interrupt batch, so a reviewer only sees the actions that need a decision.

See the [LangChain human-in-the-loop documentation](/oss/python/langchain/human-in-the-loop#conditional-interrupts) for additional configuration options and examples.

## Handle interrupts

When an interrupt is triggered, the agent pauses execution and returns control. Check for interrupts in the result and handle them accordingly. If the user rejects an action, include a clear `message` that tells the agent the tool was not executed and what to do next.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_core.utils.uuid import uuid7
from langgraph.types import Command

# Create config with thread_id for state persistence
config = {"configurable": {"thread_id": str(uuid7())}}

# Invoke the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Delete the file temp.txt"}]},
    config=config,
    version="v2",  # [!code highlight]
)

# Check if execution was interrupted
if result.interrupts:  # [!code highlight]
    # Extract interrupt information
    interrupt_value = result.interrupts[0].value  # [!code highlight]
    action_requests = interrupt_value["action_requests"]
    review_configs = interrupt_value["review_configs"]

    # Create a lookup map from tool name to review config
    config_map = {cfg["action_name"]: cfg for cfg in review_configs}

    # Display the pending actions to the user
    for action in action_requests:
        review_config = config_map[action["name"]]
        print(f"Tool: {action['name']}")
        print(f"Arguments: {action['args']}")
        print(f"Allowed decisions: {review_config['allowed_decisions']}")

    # Get user decisions (one per action_request, in order)
    decisions = [
        {
            "type": "reject",
            "message": "User rejected deleting temp.txt. Do not retry deletion.",
        }
    ]

    # Resume execution with decisions
    result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config,  # Must use the same config!
        version="v2",
    )

# Process final result
print(result.value["messages"][-1].content)  # [!code highlight]
```

## Multiple tool calls

When the agent calls multiple tools that require approval, all interrupts are batched together in a single interrupt. You must provide decisions for each one in order.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
config = {"configurable": {"thread_id": str(uuid7())}}

result = agent.invoke(
    {"messages": [{
        "role": "user",
        "content": "Delete temp.txt and send an email to admin@example.com"
    }]},
    config=config,
    version="v2",  # [!code highlight]
)

if result.interrupts:  # [!code highlight]
    interrupt_value = result.interrupts[0].value  # [!code highlight]
    action_requests = interrupt_value["action_requests"]

    # Two tools need approval
    assert len(action_requests) == 2

    # Provide decisions in the same order as action_requests
    decisions = [
        {"type": "approve"},  # First tool: delete_file
        {
            "type": "reject",
            "message": "User rejected this action. Do not retry this tool call.",
        }  # Second tool: send_email
    ]

    result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config,
        version="v2",
    )
```

## Rejection messages

When a reviewer returns a `reject` decision, Deep Agents skip the tool call and send rejection feedback back to the agent. If you omit `message`, the default feedback tells the model that the tool was not executed and not to retry the same tool call unless the user asks.

For sensitive or side-effecting tools, pass a domain-specific `message` with the decision. Be explicit about whether the agent should abandon the action, ask a follow-up question, or try a safer alternative.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
decisions = [
    {
        "type": "reject",
        "message": "User rejected deleting this file. Do not retry deletion. Ask which file to archive instead.",
    }
]
```

## Edit tool arguments

When `"edit"` is in the allowed decisions, you can modify the tool arguments before execution:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
if result.interrupts:  # [!code highlight]
    interrupt_value = result.interrupts[0].value  # [!code highlight]
    action_request = interrupt_value["action_requests"][0]

    # Original args from the agent
    print(action_request["args"])  # {"to": "everyone@company.com", ...}

    # User decides to edit the recipient
    decisions = [{
        "type": "edit",
        "edited_action": {
            "name": action_request["name"],  # Must include the tool name
            "args": {"to": "team@company.com", "subject": "...", "body": "..."}
        }
    }]

    result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config,
        version="v2",
    )
```

## Subagent interrupts

When using subagents, you can use interrupts [on tool calls](#interrupts-on-tool-calls) and [within tool calls](#interrupts-within-tool-calls).

### Interrupts on tool calls

Each subagent can have its own `interrupt_on` configuration that overrides the main agent's settings:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    tools=[delete_file, read_file],
    interrupt_on={
        "delete_file": True,
        "read_file": False,
    },
    subagents=[{
        "name": "file-manager",
        "description": "Manages file operations",
        "system_prompt": "You are a file management assistant.",
        "tools": [delete_file, read_file],
        "interrupt_on": {
            # Override: require approval for reads in this subagent
            "delete_file": True,
            "read_file": True,  # Different from main agent!
        }
    }],
    checkpointer=checkpointer
)
```

When a subagent triggers an interrupt, the handling is the same—check for `interrupts` on the result and resume with `Command`.

### Interrupts within tool calls

Subagent tools can call `interrupt()` directly to pause execution and await approval:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic
from langchain.messages import HumanMessage
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command, interrupt

from deepagents.graph import create_deep_agent
from deepagents.middleware.subagents import CompiledSubAgent

@tool(description="Request human approval before proceeding with an action.")
def request_approval(action_description: str) -> str:
    """Request human approval using the interrupt() primitive."""
    # interrupt() pauses execution and returns the value passed to Command(resume=...)
    approval = interrupt({
        "type": "approval_request",
        "action": action_description,
        "message": f"Please approve or reject: {action_description}",
    })

    if approval.get("approved"):
        return f"Action '{action_description}' was APPROVED. Proceeding..."
    else:
        return f"Action '{action_description}' was REJECTED. Reason: {approval.get('reason', 'No reason provided')}"

def main():
    checkpointer = InMemorySaver()
    model = ChatAnthropic(
        model_name="claude-sonnet-4-6",
        max_tokens=4096,
    )

    compiled_subagent = create_agent(
        model=model,
        tools=[request_approval],
        name="approval-agent",
    )

    parent_agent = create_deep_agent(
        model="google_genai:gemini-3.5-flash",
        checkpointer=checkpointer,
        subagents=[
            CompiledSubAgent(
                name="approval-agent",
                description="An agent that can request approvals",
                runnable=compiled_subagent,
            )
        ],
    )

    thread_id = "test_interrupt_directly"
    config = {"configurable": {"thread_id": thread_id}}

    print("Invoking agent - sub-agent will use request_approval tool...")

    result = parent_agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Use the task tool to launch the approval-agent sub-agent. "
                    "Tell it to use the request_approval tool to request approval for 'deploying to production'."
                )
            ]
        },
        config=config,
        version="v2",  # [!code highlight]
    )

    # Check for interrupt
    if result.interrupts:  # [!code highlight]
        interrupt_value = result.interrupts[0].value  # [!code highlight]
        print(f"\nInterrupt received!")
        print(f"  Type: {interrupt_value.get('type')}")
        print(f"  Action: {interrupt_value.get('action')}")
        print(f"  Message: {interrupt_value.get('message')}")

        print("\nResuming with Command(resume={'approved': True})...")
        result2 = parent_agent.invoke(
            Command(resume={"approved": True}),
            config=config,
            version="v2",  # [!code highlight]
        )

        if not result2.interrupts:  # [!code highlight]
            print("\nExecution completed!")
            # Find the tool response
            tool_msgs = [m for m in result2.value.get("messages", []) if m.type == "tool"]  # [!code highlight]
            if tool_msgs:
                print(f"  Tool result: {tool_msgs[-1].content}")
        else:
            print("\nAnother interrupt occurred")
    else:
        print("\n  No interrupt - the model may not have called request_approval")

if __name__ == "__main__":
    main()
```

When run, this produces the following output:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
Invoking agent - sub-agent will use request_approval tool...

Interrupt received!
  Type: approval_request
  Action: deploying to production
  Message: Please approve or reject: deploying to production

Resuming with Command(resume={'approved': True})...

Execution completed!
  Tool result: Great! The approval request has been processed. The action **"deploying to production"** was **APPROVED**. You can now proceed with the production deployment.
```

## Filesystem permission interrupts

<Note>
  Filesystem permission interrupts require `deepagents>=0.6.8`.
</Note>

Beyond `interrupt_on`, you can pause the built-in filesystem tools by marking a [permission rule](/oss/python/deepagents/permissions) with `mode="interrupt"`. When the agent calls `write_file` or `edit_file` on a path that matches an interrupt-mode rule, `create_deep_agent` raises the same human-in-the-loop interrupt as a configured tool, using the filesystem tool's name as the action name.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import FilesystemPermission, create_deep_agent
from langgraph.checkpoint.memory import MemorySaver

agent = create_deep_agent(
    model=model,
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/secrets/**"],
            mode="interrupt",
        ),
    ],
    checkpointer=MemorySaver(),  # Required to pause and resume
)
```

Handle and resume the interrupt the same way as a tool-call interrupt: run until it pauses, inspect the request, then resume with a decision.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.types import Command

config = {"configurable": {"thread_id": "fs-thread-1"}}

result = agent.invoke(
    {"messages": [{"role": "user", "content": "Save the API key to /secrets/key.txt"}]},
    config=config,
    version="v2",
)

if result.interrupts:
    action = result.interrupts[0].value["action_requests"][0]
    print(f"Approve {action['name']} on {action['args']}?")

    # Resume with the human decision (approve, edit, or reject).
    result = agent.invoke(
        Command(resume={"decisions": [{"type": "approve"}]}),
        config=config,  # Same thread ID
        version="v2",
    )
```

Filesystem-permission interrupts merge with any `interrupt_on` you pass, so a single review step can cover both custom tools and protected filesystem paths.

## Best practices

### Always use a checkpointer

Human-in-the-loop requires a checkpointer to persist agent state between the interrupt and resume:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    tools=[...],
    interrupt_on={...},
    checkpointer=checkpointer  # Required for HITL
)
```

### Use the same thread ID

When resuming, you must use the same config with the same `thread_id`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# First call
config = {"configurable": {"thread_id": "my-thread"}}
result = agent.invoke(input, config=config, version="v2")

# Resume (use same config)
result = agent.invoke(Command(resume={...}), config=config, version="v2")
```

### Match decision order to actions

The decisions list must match the order of `action_requests`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
if result.interrupts:  # [!code highlight]
    interrupt_value = result.interrupts[0].value  # [!code highlight]
    action_requests = interrupt_value["action_requests"]

    # Create one decision per action, in order
    decisions = []
    for action in action_requests:
        decision = get_user_decision(action)  # Your logic
        decisions.append(decision)

    result = agent.invoke(
        Command(resume={"decisions": decisions}),
        config=config,
        version="v2",
    )
```

### Tailor configurations by risk

Configure different tools based on their risk level:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
interrupt_on = {
    # High risk: full control (approve, edit, reject)
    "delete_file": {"allowed_decisions": ["approve", "edit", "reject"]},
    "send_email": {"allowed_decisions": ["approve", "edit", "reject"]},

    # Medium risk: no editing allowed
    "write_file": {"allowed_decisions": ["approve", "reject"]},

    # Low risk: no interrupts
    "read_file": False,
    "list_files": False,
}
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/human-in-the-loop.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
