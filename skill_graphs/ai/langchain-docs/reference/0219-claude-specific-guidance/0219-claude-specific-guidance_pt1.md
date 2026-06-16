#         + <Claude-specific guidance>
```

<Note>
  Passing a `SystemMessage` (rather than a string) triggers a different concatenation path: the right-hand assembly (`BASE`-or-`CUSTOM` plus any `SUFFIX`) is appended as an additional text content block onto the message's existing `content_blocks`. The same logical ordering applies (caller blocks first), and any `cache_control` markers on the caller's blocks are preserved—useful for placing explicit Anthropic prompt-cache breakpoints.
</Note>

<AccordionGroup>
  <Accordion title="Subagent prompts">
    The [prompt assembly](#prompt-assembly) overlay rules also apply to declarative [subagents](/oss/python/deepagents/subagents): each subagent re-runs profile resolution against **its own model**, then applies the resolved profile's `base_system_prompt` / `system_prompt_suffix` to its authored `system_prompt`. The subagent's `system_prompt` plays the `BASE` role; `CUSTOM` and `SUFFIX` come from the profile that matches the subagent's model (which may differ from the main agent's profile).

    | `spec["system_prompt"]` | profile `base_system_prompt` (`CUSTOM`) | profile `system_prompt_suffix` (`SUFFIX`) | Final subagent system prompt |
    | ----------------------- | :-------------------------------------: | :---------------------------------------: | ---------------------------- |
    | authored                |                    -                    |                     -                     | authored                     |
    | authored                |                    -                    |                     ✓                     | authored + `SUFFIX`          |
    | authored                |                    ✓                    |                     -                     | `CUSTOM`                     |
    | authored                |                    ✓                    |                     ✓                     | `CUSTOM` + `SUFFIX`          |

    There is no `USER` segment for subagents. The spec's authored `system_prompt` is the closest analog and stays in the `BASE` slot. A profile that ships only a `system_prompt_suffix` (the common case for built-in Anthropic / OpenAI profiles) just appends to whatever the subagent author wrote. A profile that sets `base_system_prompt` will *replace* the authored prompt outright.
  </Accordion>

  <Accordion title="General-purpose subagent prompt">
    The auto-added [general-purpose subagent](/oss/python/deepagents/subagents#the-general-purpose-subagent) follows the [prompt assembly](#prompt-assembly) overlay rules with one extra layer: the GP base prompt is resolved as **`general_purpose_subagent.system_prompt` (if set) -> `HarnessProfile.base_system_prompt` (if set) -> SDK general-purpose default**. The profile suffix layers on top either way.

    The two override fields can both carry a base-prompt replacement, but they are not interchangeable. `general_purpose_subagent.system_prompt` is general-purpose-specific configuration; `base_system_prompt` is a global override that primarily targets the main agent. When both are set, the **general-purpose-specific intent wins for the general-purpose subagent** so a user tuning both fields never sees their GP override silently dropped:

    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    register_harness_profile(
        "anthropic",
        HarnessProfile(
            base_system_prompt="You are ACME's support orchestrator.",  # main agent
            general_purpose_subagent=GeneralPurposeSubagentProfile(
                system_prompt="You are a research subagent. Cite sources.",  # GP subagent
            ),
            system_prompt_suffix="Always think step by step.",
        ),
    )
    ```

    | Stack       | Final system prompt                                     |
    | ----------- | ------------------------------------------------------- |
    | Main agent  | `"You are ACME's support orchestrator." + SUFFIX`       |
    | GP subagent | `"You are a research subagent. Cite sources." + SUFFIX` |

    If `general_purpose_subagent.system_prompt` is unset, the GP subagent falls back to `base_system_prompt` (when set) and finally to the SDK general-purpose default.
  </Accordion>
</AccordionGroup>

## Middleware

Deep Agents support any [middleware](/oss/python/langchain/middleware/overview), including the built-in middleware listed below, prebuilt middleware from LangChain, provider-specific middleware, and custom middleware you write yourself.

Pass middleware to the `middleware` argument of `create_deep_agent`. Custom middleware is appended after [`PatchToolCallsMiddleware`](https://reference.langchain.com/python/deepagents/middleware/patch_tool_calls/PatchToolCallsMiddleware) in the [default stack](#default-stack-main-agent).

By default, Deep Agents have access to the following middleware:

### Default stack (main agent)

From first to last:

1. [`TodoListMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/todo/TodoListMiddleware): Tracks and manages todo lists for organizing agent tasks and work.

2. [`SkillsMiddleware`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware): Only when you pass `skills`. Injected **immediately after** the todo middleware and **before** filesystem middleware so skill metadata is available before file tools run.

3. [`FilesystemMiddleware`](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware): Handles file system operations such as reading, writing, and navigating directories. When you pass `permissions`, filesystem permissions enforcement is included here so it can evaluate every tool the agent might call.

4. [`SubAgentMiddleware`](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware): Spawns and coordinates subagents for delegating tasks to specialized agents.

5. [`SummarizationMiddleware`](https://reference.langchain.com/python/langchain/agents/middleware/summarization/SummarizationMiddleware): Condenses message history to stay within context limits when conversations grow long (via [create\_summarization\_middleware](https://reference.langchain.com/python/deepagents/middleware/summarization/create_summarization_middleware)).

6. [`PatchToolCallsMiddleware`](https://reference.langchain.com/python/deepagents/middleware/patch_tool_calls/PatchToolCallsMiddleware): Repairs dangling tool calls in message history when a run resumes after an interruption or receives malformed tool-call arguments. Runs **before** Anthropic prompt caching and the tail stack below.

7. [`AsyncSubAgentMiddleware`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware): Only when you configure async subagents.

8. **Your middleware argument**: Optional middleware you pass as the `middleware` argument is appended here (after Patch, before the tail stack).

9. **Harness profile extras**: Provider-specific middleware from the resolved model profile, if any.

10. **Excluded-tool filtering**: When the harness profile lists excluded tools, middleware removes those tools from the agent.

11. [`AnthropicPromptCachingMiddleware`](https://reference.langchain.com/python/langchain-anthropic/middleware/prompt_caching/AnthropicPromptCachingMiddleware): Always registered; it no-ops on non-Anthropic models (`unsupported_model_behavior="ignore"`). Runs **after** Patch and after your middleware so the cached prefix matches what is actually sent to the model.

12. [`MemoryMiddleware`](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware): Only when you pass `memory`.

    <Note>
      `MemoryMiddleware` is placed **after** profile extras and Anthropic prompt caching so updates to injected memory are less likely to invalidate the Anthropic cache prefix. The same ordering concern is called out in the `create_deep_agent` implementation comments.
    </Note>

13. `HumanInTheLoopMiddleware`: Only when you pass `interrupt_on`. Pauses for human approval or input at configured tool calls.

### Default stack (synchronous subagents)

The built-in **general-purpose** subagent and each declarative synchronous `SubAgent` graph use a stack that `create_deep_agent` builds in code. It matches the main agent in broad shape (todo list, filesystem, summarization, Patch, profile extras, Anthropic caching, optional permissions) but differs in two ways:

* **Skills run after** [`PatchToolCallsMiddleware`](https://reference.langchain.com/python/deepagents/middleware/patch_tool_calls/PatchToolCallsMiddleware) on these inner agents (on the main agent, skills run **before** filesystem middleware when `skills` is set).
* There is **no** [`SubAgentMiddleware`](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgentMiddleware) inside a subagent graph (only the parent agent exposes the `task` tool).

When a declarative subagent sets `interrupt_on`, that value is forwarded to `create_agent` for the subagent, which wires up human-in-the-loop handling for the configured tool calls.

### Prebuilt middleware

LangChain exposes additional prebuilt middleware that let you add-on various features, such as retries, fallbacks, or PII detection. See [Prebuilt middleware](/oss/python/langchain/middleware/built-in) for more.

The `deepagents` library also exposes [`create_summarization_tool_middleware`](https://reference.langchain.com/python/deepagents/middleware/summarization/create_summarization_tool_middleware), enabling agents to trigger summarization at opportune times—such as between tasks—instead of at fixed token intervals. For more detail, see [Summarization](/oss/python/deepagents/context-engineering#summarization).

### Provider-specific middleware

For provider-specific middleware that is optimized for specific LLM providers, see [Official integrations](/oss/python/integrations/middleware#official-integrations) and [Community integrations](/oss/python/integrations/middleware#community-integrations).

### Custom middleware

You can provide additional middleware to extend functionality, add tools, or implement custom hooks:

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents.middleware import wrap_tool_call
  from langchain.tools import tool
  from deepagents import create_deep_agent

  @tool
  def get_weather(city: str) -> str:
      """Get the weather in a city."""
      return f"The weather in {city} is sunny."

  call_count = [0]  # Use list to allow modification in nested function

  @wrap_tool_call
  def log_tool_calls(request, handler):
      """Intercept and log every tool call - demonstrates cross-cutting concern."""
      call_count[0] += 1
      tool_name = request.name if hasattr(request, "name") else str(request)

      print(f"[Middleware] Tool call #{call_count[0]}: {tool_name}")
      print(f"[Middleware] Arguments: {request.args if hasattr(request, 'args') else 'N/A'}")

      # Execute the tool call
      result = handler(request)

      # Log the result
      print(f"[Middleware] Tool call #{call_count[0]} completed")

      return result

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      tools=[get_weather],
      middleware=[log_tool_calls],
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents.middleware import wrap_tool_call
  from langchain.tools import tool
  from deepagents import create_deep_agent

  @tool
  def get_weather(city: str) -> str:
      """Get the weather in a city."""
      return f"The weather in {city} is sunny."

  call_count = [0]  # Use list to allow modification in nested function

  @wrap_tool_call
  def log_tool_calls(request, handler):
      """Intercept and log every tool call - demonstrates cross-cutting concern."""
      call_count[0] += 1
      tool_name = request.name if hasattr(request, "name") else str(request)

      print(f"[Middleware] Tool call #{call_count[0]}: {tool_name}")
      print(f"[Middleware] Arguments: {request.args if hasattr(request, 'args') else 'N/A'}")

      # Execute the tool call
      result = handler(request)

      # Log the result
      print(f"[Middleware] Tool call #{call_count[0]} completed")

      return result

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      tools=[get_weather],
      middleware=[log_tool_calls],
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents.middleware import wrap_tool_call
  from langchain.tools import tool
  from deepagents import create_deep_agent

  @tool
  def get_weather(city: str) -> str:
      """Get the weather in a city."""
      return f"The weather in {city} is sunny."

  call_count = [0]  # Use list to allow modification in nested function

  @wrap_tool_call
  def log_tool_calls(request, handler):
      """Intercept and log every tool call - demonstrates cross-cutting concern."""
      call_count[0] += 1
      tool_name = request.name if hasattr(request, "name") else str(request)

      print(f"[Middleware] Tool call #{call_count[0]}: {tool_name}")
      print(f"[Middleware] Arguments: {request.args if hasattr(request, 'args') else 'N/A'}")

      # Execute the tool call
      result = handler(request)

      # Log the result
      print(f"[Middleware] Tool call #{call_count[0]} completed")

      return result

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      tools=[get_weather],
      middleware=[log_tool_calls],
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents.middleware import wrap_tool_call
  from langchain.tools import tool
  from deepagents import create_deep_agent

  @tool
  def get_weather(city: str) -> str:
      """Get the weather in a city."""
      return f"The weather in {city} is sunny."

  call_count = [0]  # Use list to allow modification in nested function

  @wrap_tool_call
  def log_tool_calls(request, handler):
      """Intercept and log every tool call - demonstrates cross-cutting concern."""
      call_count[0] += 1
      tool_name = request.name if hasattr(request, "name") else str(request)

      print(f"[Middleware] Tool call #{call_count[0]}: {tool_name}")
      print(f"[Middleware] Arguments: {request.args if hasattr(request, 'args') else 'N/A'}")

      # Execute the tool call
      result = handler(request)

      # Log the result
      print(f"[Middleware] Tool call #{call_count[0]} completed")

      return result

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      tools=[get_weather],
      middleware=[log_tool_calls],
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents.middleware import wrap_tool_call
  from langchain.tools import tool
  from deepagents import create_deep_agent

  @tool
  def get_weather(city: str) -> str:
      """Get the weather in a city."""
      return f"The weather in {city} is sunny."

  call_count = [0]  # Use list to allow modification in nested function

  @wrap_tool_call
  def log_tool_calls(request, handler):
      """Intercept and log every tool call - demonstrates cross-cutting concern."""
      call_count[0] += 1
      tool_name = request.name if hasattr(request, "name") else str(request)

      print(f"[Middleware] Tool call #{call_count[0]}: {tool_name}")
      print(f"[Middleware] Arguments: {request.args if hasattr(request, 'args') else 'N/A'}")

      # Execute the tool call
      result = handler(request)

      # Log the result
      print(f"[Middleware] Tool call #{call_count[0]} completed")

      return result

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      tools=[get_weather],
      middleware=[log_tool_calls],
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents.middleware import wrap_tool_call
  from langchain.tools import tool
  from deepagents import create_deep_agent

  @tool
  def get_weather(city: str) -> str:
      """Get the weather in a city."""
      return f"The weather in {city} is sunny."

  call_count = [0]  # Use list to allow modification in nested function

  @wrap_tool_call
  def log_tool_calls(request, handler):
      """Intercept and log every tool call - demonstrates cross-cutting concern."""
      call_count[0] += 1
      tool_name = request.name if hasattr(request, "name") else str(request)

      print(f"[Middleware] Tool call #{call_count[0]}: {tool_name}")
      print(f"[Middleware] Arguments: {request.args if hasattr(request, 'args') else 'N/A'}")

      # Execute the tool call
      result = handler(request)

      # Log the result
      print(f"[Middleware] Tool call #{call_count[0]} completed")

      return result

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      tools=[get_weather],
      middleware=[log_tool_calls],
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents.middleware import wrap_tool_call
  from langchain.tools import tool
  from deepagents import create_deep_agent

  @tool
  def get_weather(city: str) -> str:
      """Get the weather in a city."""
      return f"The weather in {city} is sunny."

  call_count = [0]  # Use list to allow modification in nested function

  @wrap_tool_call
  def log_tool_calls(request, handler):
      """Intercept and log every tool call - demonstrates cross-cutting concern."""
      call_count[0] += 1
      tool_name = request.name if hasattr(request, "name") else str(request)

      print(f"[Middleware] Tool call #{call_count[0]}: {tool_name}")
      print(f"[Middleware] Arguments: {request.args if hasattr(request, 'args') else 'N/A'}")

      # Execute the tool call
      result = handler(request)

      # Log the result
      print(f"[Middleware] Tool call #{call_count[0]} completed")

      return result

  agent = create_deep_agent(
      model="ollama:devstral-2",
      tools=[get_weather],
      middleware=[log_tool_calls],
  )
  ```
</CodeGroup>

<Warning>
  **Do not mutate attributes after initialization**

  If you need to track values across hook invocations (for example, counters or accumulated data), use graph state.
  Graph state is scoped to a thread by design, so updates are safe under concurrency.

  **Do this:**

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.agents.middleware import AgentMiddleware

  class CustomMiddleware(AgentMiddleware):
      def __init__(self):
          pass

      def before_agent(self, state, runtime):
          return {"x": state.get("x", 0) + 1}  # Update graph state instead
  ```

  Do **not** do this:

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  class CustomMiddlewareBad(AgentMiddleware):
      def __init__(self):
          self.x = 1

      def before_agent(self, state, runtime):
          self.x += 1  # Mutation causes race conditions
  ```

  Mutation in place, such as modifying `self.x` in `before_agent` or changing other shared values in hooks, can lead to subtle bugs and race conditions because many operations run concurrently (subagents, parallel tools, and parallel invocations on different threads).

  For full details on extending state with custom properties, see [Custom middleware - Custom state schema](/oss/python/langchain/middleware/custom#custom-state-schema).

  If you must use mutation in custom middleware, consider what happens when subagents, parallel tools, or concurrent agent invocations run at the same time.
</Warning>

### Interpreters

Use [interpreters](/oss/python/deepagents/interpreters) to add an `eval` tool that runs JavaScript in a scoped QuickJS runtime. Interpreters are useful when the agent needs to compose tools programmatically, batch work, handle errors in code, or transform structured data without a full shell environment.

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from langchain_quickjs import CodeInterpreterMiddleware

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      middleware=[CodeInterpreterMiddleware()],
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from langchain_quickjs import CodeInterpreterMiddleware

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      middleware=[CodeInterpreterMiddleware()],
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from langchain_quickjs import CodeInterpreterMiddleware

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      middleware=[CodeInterpreterMiddleware()],
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from langchain_quickjs import CodeInterpreterMiddleware

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      middleware=[CodeInterpreterMiddleware()],
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from langchain_quickjs import CodeInterpreterMiddleware

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      middleware=[CodeInterpreterMiddleware()],
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from langchain_quickjs import CodeInterpreterMiddleware

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      middleware=[CodeInterpreterMiddleware()],
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from langchain_quickjs import CodeInterpreterMiddleware

  agent = create_deep_agent(
      model="ollama:devstral-2",
      middleware=[CodeInterpreterMiddleware()],
  )
  ```
</CodeGroup>

For setup, programmatic tool calling, subagent orchestration, and limits, see [Interpreters](/oss/python/deepagents/interpreters).

## Subagents

To isolate detailed work and avoid context bloat, use subagents:

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

For more information, see [Subagents](/oss/python/deepagents/subagents).

## Backends

Tools for a deep agent can make use of virtual file systems to store, access, and edit files. By default, deep agents use a [`StateBackend`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend).

If you are using [skills](#skills) or [memory](#memory), you must add the expected skill or memory files to the backend before creating the agent.

<Tabs>
  <Tab title="StateBackend">
    A thread-scoped filesystem backend stored in `langgraph` state.

    Files persist across turns within a thread (via your checkpointer) and are not shared across threads.

    <CodeGroup>
      ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend

      # By default we provide a StateBackend
      agent = create_deep_agent(model="google_genai:gemini-3.5-flash")

      # Under the hood, it looks like
      agent2 = create_deep_agent(
          model="openai:gpt-5.5",
          backend=StateBackend(),
      )
      ```

      ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend

      # By default we provide a StateBackend
      agent = create_deep_agent(model="openai:gpt-5.5")

      # Under the hood, it looks like
      agent2 = create_deep_agent(
          model="openai:gpt-5.5",
          backend=StateBackend(),
      )
      ```

      ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      from deepagents import create_deep_agent
      from deepagents.backends import StateBackend
