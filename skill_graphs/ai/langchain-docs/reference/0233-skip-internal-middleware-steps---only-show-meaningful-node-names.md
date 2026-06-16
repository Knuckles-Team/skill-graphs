# Skip internal middleware steps - only show meaningful node names
INTERESTING_NODES = {"model_request", "tools"}

last_source = ""
mid_line = False  # True when we've written tokens without a trailing newline

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Analyze the impact of remote work on team productivity"}]},
    stream_mode=["updates", "messages", "custom"],
    subgraphs=True,
    version="v2",
):
    is_subagent = any(s.startswith("tools:") for s in chunk["ns"])
    source = "subagent" if is_subagent else "main"

    if chunk["type"] == "updates":
        for node_name in chunk["data"]:
            if node_name not in INTERESTING_NODES:
                continue
            if mid_line:
                print()
                mid_line = False
            print(f"[{source}] step: {node_name}")

    elif chunk["type"] == "messages":
        token, metadata = chunk["data"]
        if token.content:
            # Print a header when the source changes
            if source != last_source:
                if mid_line:
                    print()
                    mid_line = False
                print(f"\n[{source}] ", end="")
                last_source = source
            print(token.content, end="", flush=True)
            mid_line = True

    elif chunk["type"] == "custom":
        if mid_line:
            print()
            mid_line = False
        print(f"[{source}] custom event:", chunk["data"])

print()
```

## Common patterns

### Track subagent lifecycle

Monitor when subagents start, run, and complete:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
active_subagents = {}

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Research the latest AI safety developments"}]},
    stream_mode="updates",
    subgraphs=True,
    version="v2",
):
    if chunk["type"] == "updates":
        for node_name, data in chunk["data"].items():
            # ─── Phase 1: Detect subagent starting ────────────────────────
            # When the main agent's model_request contains task tool calls,
            # a subagent has been spawned.
            if not chunk["ns"] and node_name == "model_request":
                for msg in data.get("messages", []):
                    for tc in getattr(msg, "tool_calls", []):
                        if tc["name"] == "task":
                            active_subagents[tc["id"]] = {
                                "type": tc["args"].get("subagent_type"),
                                "description": tc["args"].get("description", "")[:80],
                                "status": "pending",
                            }
                            print(
                                f'[lifecycle] PENDING  → subagent "{tc["args"].get("subagent_type")}" '
                                f'({tc["id"]})'
                            )

            # ─── Phase 2: Detect subagent running ─────────────────────────
            # When we receive events from a tools:UUID namespace, that
            # subagent is actively executing.
            if chunk["ns"] and chunk["ns"][0].startswith("tools:"):
                pregel_id = chunk["ns"][0].split(":")[1]
                # Check if any pending subagent needs to be marked running.
                # Note: the pregel task ID differs from the tool_call_id,
                # so we mark any pending subagent as running on first subagent event.
                for sub_id, sub in active_subagents.items():
                    if sub["status"] == "pending":
                        sub["status"] = "running"
                        print(
                            f'[lifecycle] RUNNING  → subagent "{sub["type"]}" '
                            f"(pregel: {pregel_id})"
                        )
                        break

            # ─── Phase 3: Detect subagent completing ──────────────────────
            # When the main agent's tools node returns a tool message,
            # the subagent has completed and returned its result.
            if not chunk["ns"] and node_name == "tools":
                for msg in data.get("messages", []):
                    if msg.type == "tool":
                        sub = active_subagents.get(msg.tool_call_id)
                        if sub:
                            sub["status"] = "complete"
                            print(
                                f'[lifecycle] COMPLETE → subagent "{sub["type"]}" '
                                f"({msg.tool_call_id})"
                            )
                            print(f"  Result preview: {str(msg.content)[:120]}...")

# Print final state
print("\n--- Final subagent states ---")
for sub_id, sub in active_subagents.items():
    print(f"  {sub['type']}: {sub['status']}")
```

## v2 streaming format

<Note>
  Requires LangGraph >= 1.1.
</Note>

All examples on this page use the v2 streaming format (`version="v2"`), which is the recommended approach. Every chunk is a `StreamPart` dict with `type`, `ns`, and `data` keys — the same shape regardless of stream mode, number of modes, or subgraph settings.

The v2 format eliminates nested tuple unpacking, making it straightforward to handle subgraph streaming in Deep Agents. Compare the two formats:

<CodeGroup>
  ```python v2 (recommended) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Unified format — no nested tuple unpacking
  for chunk in agent.stream(
      {"messages": [{"role": "user", "content": "Research quantum computing"}]},
      stream_mode=["updates", "messages", "custom"],
      subgraphs=True,
      version="v2",
  ):
      print(chunk["type"])  # "updates", "messages", or "custom"
      print(chunk["ns"])    # () for main agent, ("tools:<id>",) for subagent
      print(chunk["data"])  # payload
  ```

  ```python v1 (legacy) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Must handle (namespace, (mode, data)) nested tuples
  for namespace, chunk in agent.stream(
      {"messages": [{"role": "user", "content": "Research quantum computing"}]},
      stream_mode=["updates", "messages", "custom"],
      subgraphs=True,
  ):
      mode, data = chunk[0], chunk[1]
      print(mode)       # "updates", "messages", or "custom"
      print(namespace)  # () for main agent, ("tools:<id>",) for subagent
      print(data)       # payload
  ```
</CodeGroup>

See the [LangGraph streaming docs](/oss/python/langgraph/streaming#stream-output-format-v2) for more details on the v2 format, including type narrowing and Pydantic/dataclass coercion.

## Related

* [Subagents](/oss/python/deepagents/subagents)—Configure and use subagents with Deep Agents
* [Frontend streaming](/oss/python/deepagents/frontend/overview)—Build React UIs with [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) for Deep Agents
* [LangChain Event Streaming](/oss/python/langchain/event-streaming)—General streaming concepts with LangChain agents

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/streaming.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Subagents
Source: https://docs.langchain.com/oss/python/deepagents/subagents

Learn how to use subagents to delegate work and keep context clean

A deep agent can create subagents to delegate work. You can specify custom subagents in the `subagents` parameter. Subagents are useful for [context quarantine](https://www.dbreunig.com/2025/06/26/how-to-fix-your-context.html#context-quarantine) (keeping the main agent's context clean) and for providing specialized instructions.

This page covers **synchronous** subagents, where the supervisor blocks until the subagent finishes. For long-running tasks, parallel workstreams, or cases where you need mid-flight steering and cancellation, see [Async subagents](/oss/python/deepagents/async-subagents).

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph TB
    Main[Main Agent] --> |task tool| Sub[Subagent]

    Sub --> Research[Research]
    Sub --> Code[Code]
    Sub --> General[General]

    Research --> |isolated work| Result[Final Result]
    Code --> |isolated work| Result
    General --> |isolated work| Result

    Result --> Main
```

## Why use subagents?

Subagents solve the **context bloat problem**. When agents use tools with large outputs (web search, file reads, database queries), the context window fills up quickly with intermediate results. Subagents isolate this detailed work—the main agent receives only the final result, not the dozens of tool calls that produced it.

**When to use subagents:**

* ✅ Multi-step tasks that would clutter the main agent's context
* ✅ Specialized domains that need custom instructions or tools
* ✅ Tasks requiring different model capabilities
* ✅ When you want to keep the main agent focused on high-level coordination

**When NOT to use subagents:**

* ❌ Simple, single-step tasks
* ❌ When you need to maintain intermediate context
* ❌ When the overhead outweighs benefits

## Configuration

`subagents` should be a list of dictionaries or [`CompiledSubAgent`](https://reference.langchain.com/python/deepagents/middleware/subagents/CompiledSubAgent) objects. There are two types:

### Default subagent

Deep Agents automatically adds a synchronous `general-purpose` subagent unless you already provide a synchronous subagent with that name.

The `general-purpose` subagent has filesystem tools by default and can be customized with additional tools/middleware.

* To replace it, pass your own subagent named `general-purpose`.
* To rename or re-prompt the auto-added version, set `general_purpose_subagent=GeneralPurposeSubagentProfile(...)` on the active [harness profile](/oss/python/deepagents/profiles#harness-profiles).
* To disable it, see [Running without subagents](#running-without-subagents) below.

### Running without subagents

To run an agent without the `task` tool, do two things:

1. Set `general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False)` on the active [harness profile](/oss/python/deepagents/profiles#harness-profiles).
2. Pass no synchronous subagents via `subagents=` on `create_deep_agent`.

Deep Agents only attaches [`SubAgentMiddleware`](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware) (and the `task` tool) when at least one synchronous subagent exists. With neither the default nor a caller-provided one, the agent runs without delegation.

Async subagents are unaffected—they flow through their own middleware and tools, described in [Async subagents](/oss/python/deepagents/async-subagents).

<Tip>
  Don't reach for `excluded_middleware` here—`SubAgentMiddleware` is required scaffolding and listing it raises `ValueError`. The `general_purpose_subagent.enabled = False` knob is the supported path.
</Tip>

## Custom subagents

You can define specialized subagents with specific tool by using the `subagents` parameter. For example to serve as a code reviewer, web researcher, or test runner.

For most use cases, define subagents as dictionaries with [SubAgent dictionaries](#subagent-dictionary-based). For complex workflows, use a [`CompiledSubAgent`](#compiledsubagent):

### SubAgent (Dictionary-based)

Define subagents as dictionaries matching the [`SubAgent`](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent) spec with the following fields:

| Field             | Type                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`            | `str`                                  | Required. Unique identifier for the subagent. The main agent uses this name when calling the `task()` tool. The subagent name becomes metadata for `AIMessage`s and for streaming, which helps to differentiate between agents.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `description`     | `str`                                  | Required. Description of what this subagent does. Be specific and action-oriented. The main agent uses this to decide when to delegate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `system_prompt`   | `str`                                  | Required. Instructions for the subagent. Custom subagents must define their own. Include tool usage guidance and output format requirements.<br />Does not inherit from main agent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `tools`           | `list[Callable]`                       | Optional. Tools the subagent can use. Keep this minimal and include only what's needed.<br />Inherits from main agent by default. When specified, overrides the inherited tools entirely.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `model`           | `str` \| `BaseChatModel`               | Optional. Overrides the main agent's model. Omit to use the main agent's model.<br />Inherits from main agent by default. You can pass either a model identifier string like `'openai:gpt-5.5'` (using the `'provider:model'` format) or a LangChain chat model object (`init_chat_model("gpt-5.5")` or `ChatOpenAI(model="gpt-5.5")`).                                                                                                                                                                                                                                                                                                                              |
| `middleware`      | `list[Middleware]`                     | Optional. Additional middleware for custom behavior, logging, or rate limiting.<br />Does not inherit from the main agent. Appended to the [default subagent stack](/oss/python/deepagents/customization#default-stack-synchronous-subagents).                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `interrupt_on`    | `dict[str, bool \| InterruptOnConfig]` | Optional. Configure [human-in-the-loop](/oss/python/deepagents/human-in-the-loop) for specific tools. Options:`True`, `False`, or an `InterruptOnConfig` with `allowed_decisions`. Requires checkpointer.<br />Inherits from main agent by default. Subagent value overrides the default.                                                                                                                                                                                                                                                                                                                                                                            |
| `skills`          | `list[str]`                            | Optional. [Skills](/oss/python/deepagents/skills) source paths. When specified, the subagent will load skills from these directories (e.g., `["/skills/research/", "/skills/web-search/"]`). This allows subagents to have different skill sets than the main agent.<br />Does not inherit from main agent. Only the general-purpose subagent inherits the main agent's skills. When a subagent has skills, it runs its own independent [`SkillsMiddleware`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware) instance. Skill state is fully isolated—a subagent's loaded skills are not visible to the parent, and vice versa. |
| `response_format` | `ResponseFormat`                       | Optional. [Structured output](/oss/python/langchain/structured-output) schema for the subagent. When set, the parent receives the subagent's result as JSON instead of free-form text. Accepts Pydantic models, `ToolStrategy(...)`, `ProviderStrategy(...)`, or a raw schema type. See [Structured output](#structured-output).                                                                                                                                                                                                                                                                                                                                     |
| `permissions`     | `list[FilesystemPermission]`           | Optional. [Filesystem permission rules](/oss/python/deepagents/permissions) for the subagent. When set, **replaces** the parent agent's permissions entirely.<br />Inherits from main agent by default.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### CompiledSubAgent

For complex workflows, use a prebuilt LangGraph graph as a [`CompiledSubAgent`](https://reference.langchain.com/python/deepagents/middleware/subagents/CompiledSubAgent):

| Field         | Type       | Description                                                                                                                                                       |
| ------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | `str`      | Required. Unique identifier for the subagent. The subagent name becomes metadata for `AIMessage`s and for streaming, which helps to differentiate between agents. |
| `description` | `str`      | Required. What this subagent does.                                                                                                                                |
| `runnable`    | `Runnable` | Required. A compiled LangGraph graph (must call `.compile()` first).                                                                                              |

## Using SubAgent

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
from typing import Literal

from deepagents import create_deep_agent
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )

research_subagent = {
    "name": "research-agent",
    "description": "Used to research more in depth questions",
    "system_prompt": "You are a great researcher",
    "tools": [internet_search],
    "model": "openai:gpt-5.5",  # Optional override, defaults to main agent model
}
subagents = [research_subagent]

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    subagents=subagents,
)
```

## Using CompiledSubAgent

For more complex use cases, you can provide your custom subagents with [`CompiledSubAgent`](https://reference.langchain.com/python/deepagents/middleware/subagents/CompiledSubAgent).
You can create a custom subagent using LangChain's [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) or by making a custom LangGraph graph using the [graph API](/oss/python/langgraph/graph-api).

If you're creating a custom LangGraph graph, make sure that the graph has a [state key called `"messages"`](/oss/python/langgraph/quickstart#2-define-state):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent, CompiledSubAgent
from langchain.agents import create_agent

# Create a custom agent graph
custom_graph = create_agent(
    model=your_model,
    tools=specialized_tools,
    prompt="You are a specialized agent for data analysis..."
)

# Use it as a custom subagent
custom_subagent = CompiledSubAgent(
    name="data-analyzer",
    description="Specialized agent for complex data analysis tasks",
    runnable=custom_graph
)

subagents = [custom_subagent]

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    tools=[internet_search],
    system_prompt=research_instructions,
    subagents=subagents
)
```

## Streaming

Deep Agents support streaming updates from both the coordinator and every delegated subagent.

Use [`stream_events`](/oss/python/deepagents/event-streaming) to get typed projections—separate iterators for subagents, messages, tool calls, and values—so you can consume each independently.

### Stream subagent progress

The simplest pattern is to iterate `stream.subagents` to track each delegated task as it starts, runs, and completes. Each subagent handle exposes `.name`, `.messages`, `.tool_calls`, and `.output`.

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import (
      create_deep_agent
  )

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      system_prompt=(
          "You are a project coordinator with no research knowledge. "
          "For every user request, you must call the task() tool with "
          "subagent_type set to research-agent. Never answer research "
          "questions yourself."
      ),
      subagents=[
          {
              "name": "research-agent",
              "description": (
                  "Delegate research to this subagent. Give one topic at a time."
              ),
              "system_prompt": (
                  "You are a great researcher. Return a brief summary."
              ),
          },
      ],
      name="main-agent",
  )

  if __name__ == "__main__":
      stream = agent.stream_events(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Research one recent advance in quantum computing.",
                  }
              ]
          },
          version="v3",
      )

      coordinator_messages: list[str] = []
      subagent_handles = []

      for name, item in stream.interleave("messages", "subagents"):
          if name == "messages":
              print("[coordinator]", item.text)
              coordinator_messages.append(item.text)
          else:
              print(f"[{item.name}] started")
              subagent_handles.append(item)
              for message in item.messages:
                  print(f"[{item.name}]", message.text)
              print(f"[{item.name}] status: {item.status}")
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import (
      create_deep_agent
  )

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      system_prompt=(
          "You are a project coordinator with no research knowledge. "
          "For every user request, you must call the task() tool with "
          "subagent_type set to research-agent. Never answer research "
          "questions yourself."
      ),
      subagents=[
          {
              "name": "research-agent",
              "description": (
                  "Delegate research to this subagent. Give one topic at a time."
              ),
              "system_prompt": (
                  "You are a great researcher. Return a brief summary."
              ),
          },
      ],
      name="main-agent",
  )

  if __name__ == "__main__":
      stream = agent.stream_events(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Research one recent advance in quantum computing.",
                  }
              ]
          },
          version="v3",
      )

      coordinator_messages: list[str] = []
      subagent_handles = []

      for name, item in stream.interleave("messages", "subagents"):
          if name == "messages":
              print("[coordinator]", item.text)
              coordinator_messages.append(item.text)
          else:
              print(f"[{item.name}] started")
              subagent_handles.append(item)
              for message in item.messages:
                  print(f"[{item.name}]", message.text)
              print(f"[{item.name}] status: {item.status}")
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import (
      create_deep_agent
  )

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      system_prompt=(
          "You are a project coordinator with no research knowledge. "
          "For every user request, you must call the task() tool with "
          "subagent_type set to research-agent. Never answer research "
          "questions yourself."
      ),
      subagents=[
          {
              "name": "research-agent",
              "description": (
                  "Delegate research to this subagent. Give one topic at a time."
              ),
              "system_prompt": (
                  "You are a great researcher. Return a brief summary."
              ),
          },
      ],
      name="main-agent",
  )

  if __name__ == "__main__":
      stream = agent.stream_events(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Research one recent advance in quantum computing.",
                  }
              ]
          },
          version="v3",
      )

      coordinator_messages: list[str] = []
      subagent_handles = []

      for name, item in stream.interleave("messages", "subagents"):
          if name == "messages":
              print("[coordinator]", item.text)
              coordinator_messages.append(item.text)
          else:
              print(f"[{item.name}] started")
              subagent_handles.append(item)
              for message in item.messages:
                  print(f"[{item.name}]", message.text)
              print(f"[{item.name}] status: {item.status}")
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import (
      create_deep_agent
  )

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      system_prompt=(
          "You are a project coordinator with no research knowledge. "
          "For every user request, you must call the task() tool with "
          "subagent_type set to research-agent. Never answer research "
          "questions yourself."
      ),
      subagents=[
          {
              "name": "research-agent",
              "description": (
                  "Delegate research to this subagent. Give one topic at a time."
              ),
              "system_prompt": (
                  "You are a great researcher. Return a brief summary."
              ),
          },
      ],
      name="main-agent",
  )

  if __name__ == "__main__":
      stream = agent.stream_events(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Research one recent advance in quantum computing.",
                  }
              ]
          },
          version="v3",
      )

      coordinator_messages: list[str] = []
      subagent_handles = []

      for name, item in stream.interleave("messages", "subagents"):
          if name == "messages":
              print("[coordinator]", item.text)
              coordinator_messages.append(item.text)
          else:
              print(f"[{item.name}] started")
              subagent_handles.append(item)
              for message in item.messages:
                  print(f"[{item.name}]", message.text)
              print(f"[{item.name}] status: {item.status}")
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import (
      create_deep_agent
  )

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      system_prompt=(
          "You are a project coordinator with no research knowledge. "
          "For every user request, you must call the task() tool with "
          "subagent_type set to research-agent. Never answer research "
          "questions yourself."
      ),
      subagents=[
          {
              "name": "research-agent",
              "description": (
                  "Delegate research to this subagent. Give one topic at a time."
              ),
              "system_prompt": (
                  "You are a great researcher. Return a brief summary."
              ),
          },
      ],
      name="main-agent",
  )

  if __name__ == "__main__":
      stream = agent.stream_events(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Research one recent advance in quantum computing.",
                  }
              ]
          },
          version="v3",
      )

      coordinator_messages: list[str] = []
      subagent_handles = []

      for name, item in stream.interleave("messages", "subagents"):
          if name == "messages":
              print("[coordinator]", item.text)
              coordinator_messages.append(item.text)
          else:
              print(f"[{item.name}] started")
              subagent_handles.append(item)
              for message in item.messages:
                  print(f"[{item.name}]", message.text)
              print(f"[{item.name}] status: {item.status}")
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import (
      create_deep_agent
  )

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      system_prompt=(
          "You are a project coordinator with no research knowledge. "
          "For every user request, you must call the task() tool with "
          "subagent_type set to research-agent. Never answer research "
          "questions yourself."
      ),
      subagents=[
          {
              "name": "research-agent",
              "description": (
                  "Delegate research to this subagent. Give one topic at a time."
              ),
              "system_prompt": (
                  "You are a great researcher. Return a brief summary."
              ),
          },
      ],
      name="main-agent",
  )

  if __name__ == "__main__":
      stream = agent.stream_events(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Research one recent advance in quantum computing.",
                  }
              ]
          },
          version="v3",
      )

      coordinator_messages: list[str] = []
      subagent_handles = []

      for name, item in stream.interleave("messages", "subagents"):
          if name == "messages":
              print("[coordinator]", item.text)
              coordinator_messages.append(item.text)
          else:
              print(f"[{item.name}] started")
              subagent_handles.append(item)
              for message in item.messages:
                  print(f"[{item.name}]", message.text)
              print(f"[{item.name}] status: {item.status}")
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import (
      create_deep_agent
  )

  agent = create_deep_agent(
      model="ollama:devstral-2",
      system_prompt=(
          "You are a project coordinator with no research knowledge. "
          "For every user request, you must call the task() tool with "
          "subagent_type set to research-agent. Never answer research "
          "questions yourself."
      ),
      subagents=[
          {
              "name": "research-agent",
              "description": (
                  "Delegate research to this subagent. Give one topic at a time."
              ),
              "system_prompt": (
                  "You are a great researcher. Return a brief summary."
              ),
          },
      ],
      name="main-agent",
  )

  if __name__ == "__main__":
      stream = agent.stream_events(
          {
              "messages": [
                  {
                      "role": "user",
                      "content": "Research one recent advance in quantum computing.",
                  }
              ]
          },
          version="v3",
      )

      coordinator_messages: list[str] = []
      subagent_handles = []

      for name, item in stream.interleave("messages", "subagents"):
          if name == "messages":
              print("[coordinator]", item.text)
              coordinator_messages.append(item.text)
          else:
              print(f"[{item.name}] started")
              subagent_handles.append(item)
              for message in item.messages:
                  print(f"[{item.name}]", message.text)
              print(f"[{item.name}] status: {item.status}")
  ```
</CodeGroup>

### LangSmith tracing

As your deep agent runs, all runs executed by a subagent or the coordinator will have the agent name in their metadata under the `lc_agent_name` key—for example, `{'lc_agent_name': 'research-agent'}`. This lets you identify and filter runs by subagent in LangSmith.

<img alt="LangSmith Example trace showing the metadata" />

<Tip>
  Open the run in [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-subagents) to compare the coordinator trace with each subagent run. Follow the [observability quickstart](/langsmith/observability-quickstart) to get set up. We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
</Tip>

## Filter by subagent in LangSmith

Because each subagent's `name` is written to the `lc_agent_name` metadata key on every run it produces, you can use LangSmith's metadata filtering to isolate all runs from a specific subagent — useful for debugging, monitoring, or comparing subagent behavior over time.

### Filter in the LangSmith UI

1. Open your tracing project in [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-subagents).
2. Switch the view to **Runs** on the Tracing project page to see individual spans.
3. Click **Add filter** and select **Metadata**.
4. Set the **Key** to `lc_agent_name` and the **Value** to the subagent name (for example, `research-agent`).

This shows only the runs produced by that subagent. You can save the filter as a named view for reuse. For a full reference on filtering options, see [Filter traces](/langsmith/filter-traces-in-application).

### Filter programmatically with the SDK

Use the `has` comparator in the LangSmith filter query language to match runs by metadata key-value pair:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith import Client

client = Client()

runs = client.list_runs(
    project_name="<your-project>",
    filter='has(metadata, \'{"lc_agent_name": "research-agent"}\')',
)

for run in runs:
    print(run.name, run.start_time, run.status)
```

To fetch runs from *any* named subagent (excluding the main agent), filter for runs that have the `lc_agent_name` key at all:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
runs = client.list_runs(
    project_name="<your-project>",
    filter="has(metadata, 'lc_agent_name')",
)
```

For the full filter query language reference, see [Trace query syntax](/langsmith/trace-query-syntax).

## Structured output

Subagents support [structured output](/oss/python/langchain/structured-output), so the parent agent receives predictable, parseable JSON instead of free-form text.

<Note>
  Structured output for subagents requires `deepagents>=0.5.3`.
</Note>

Pass `response_format` on the subagent config. When the subagent finishes, its structured response is JSON-serialized and returned as the `ToolMessage` content to the parent agent. The schema accepts anything supported by [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent): Pydantic models, `ToolStrategy(...)`, `ProviderStrategy(...)`, or a raw schema type.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from pydantic import BaseModel, Field

from deepagents import create_deep_agent

class ResearchFindings(BaseModel):
    """Structured findings from a research task."""
    summary: str = Field(description="Summary of findings")
    confidence: float = Field(description="Confidence score from 0 to 1")
    sources: list[str] = Field(description="List of source URLs")

research_subagent = {
    "name": "researcher",
    "description": "Researches topics and returns structured findings",
    "system_prompt": "Research the given topic thoroughly. Return your findings.",
    "tools": [web_search],
    "response_format": ResearchFindings,
}

agent = create_deep_agent(
    model="claude-sonnet-4-6",
    subagents=[research_subagent],
)

result = await agent.ainvoke(
    {"messages": [{"role": "user", "content": "Research recent advances in quantum computing"}]}
)

# The parent's ToolMessage contains JSON-serialized structured data:

# '{"summary": "...", "confidence": 0.87, "sources": ["https://..."]}'
```

Without `response_format`, the parent receives the subagent's last message text as-is. With it, the parent always gets valid JSON matching the schema, which is useful when the parent needs to process the result programmatically or pass it to downstream tools.

For full details on schema types and strategies (tool calling vs. provider-native), see [Structured output](/oss/python/langchain/structured-output).

## The general-purpose subagent

In addition to any user-defined subagents, every deep agent has access to a `general-purpose` subagent at all times. This subagent:

* Uses its own [default system prompt with profile overlays applied](/oss/python/deepagents/customization#prompt-assembly)
* Has access to all the same tools
* Uses the same model (unless overridden)
* Inherits skills from the main agent (when skills are configured)

### Override the general-purpose subagent

Include a subagent with `name="general-purpose"` in your `subagents` list to replace the default. Use this to configure a different model, tools, or system prompt for the general-purpose subagent:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

# Main agent uses Gemini; general-purpose subagent uses GPT
agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    tools=[internet_search],
    subagents=[
        {
            "name": "general-purpose",
            "description": "General-purpose agent for research and multi-step tasks",
            "system_prompt": "You are a general-purpose assistant.",
            "tools": [internet_search],
            "model": "openai:gpt-5.5",  # Different model for delegated tasks
        },
    ],
)
```

When you provide a subagent with the general-purpose name, the default general-purpose subagent is not added. Your spec fully replaces it.

To remove the built-in general-purpose subagent entirely instead of replacing it, set the active harness profile's general-purpose subagent `enabled` flag to `False`.

### When to use it

The general-purpose subagent is ideal for context isolation without specialized behavior. The main agent can delegate a complex multi-step task to this subagent and get a concise result back without bloat from intermediate tool calls.

<Card title="Example">
  Instead of the main agent making 10 web searches and filling its context with results, it delegates to the general-purpose subagent: `task(name="general-purpose", task="Research quantum computing trends")`. The subagent performs all the searches internally and returns only a summary.
</Card>

### Skills inheritance

When configuring [skills](/oss/python/deepagents/skills) with `create_deep_agent`:

* **General-purpose subagent**: Automatically inherits skills from the main agent
* **Custom subagents**: Do NOT inherit skills by default—use the `skills` parameter to give them their own skills

<Note>
  Only subagents configured with skills get a `SkillsMiddleware` instance—custom subagents without a `skills` parameter do not. When present, skill state is fully isolated in both directions: the parent's skills are not visible to the child, and the child's skills are not propagated back to the parent.
</Note>

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent

# Research subagent with its own skills
research_subagent = {
    "name": "researcher",
    "description": "Research assistant with specialized skills",
    "system_prompt": "You are a researcher.",
    "tools": [web_search],
    "skills": ["/skills/research/", "/skills/web-search/"],  # Subagent-specific skills
}

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    skills=["/skills/main/"],  # Main agent and GP subagent get these
    subagents=[research_subagent],  # Gets only /skills/research/ and /skills/web-search/
)
```

## Best practices

### Write clear descriptions

The main agent uses descriptions to decide which subagent to call. Be specific:

✅ **Good:** `"Analyzes financial data and generates investment insights with confidence scores"`

❌ **Bad:** `"Does finance stuff"`

### Keep system prompts detailed

Include specific guidance on how to use tools and format outputs:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
research_subagent = {
    "name": "research-agent",
    "description": "Conducts in-depth research using web search and synthesizes findings",
    "system_prompt": """You are a thorough researcher. Your job is to:

    1. Break down the research question into searchable queries
    2. Use internet_search to find relevant information
    3. Synthesize findings into a comprehensive but concise summary
    4. Cite sources when making claims

    Output format:
    - Summary (2-3 paragraphs)
    - Key findings (bullet points)
    - Sources (with URLs)

    Keep your response under 500 words to maintain clean context.""",
    "tools": [internet_search],
}
```

### Minimize tool sets

Only give subagents the tools they need. This improves focus and security:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# ✅ Good: Focused tool set
email_agent = {
    "name": "email-sender",
    "tools": [send_email, validate_email],  # Only email-related
}
