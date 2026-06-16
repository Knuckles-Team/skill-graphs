# Models
Source: https://docs.langchain.com/oss/python/deepagents/models

Configure model providers and parameters for Deep Agents

Deep Agents work with any [LangChain chat model](/oss/python/langchain/models) that supports [tool calling](/oss/python/langchain/models#tool-calling).

## Supported models

Specify models in `provider:model` format (for example, `google_genai:gemini-3.5-flash`, `openai:gpt-5.4`, or `anthropic:claude-sonnet-4-6`). The provider prefix selects the LangChain integration, and everything after the colon is passed through to that provider as the model identifier. For valid provider strings, see the `model_provider` parameter of [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model). For provider-specific configuration, see [chat model integrations](/oss/python/integrations/chat).

The model identifier must match the format expected by the provider. Some providers use simple names like `gpt-5.4`; others use namespaced IDs or deployment paths like `zai-org/GLM-5.1`, so the full Deep Agents string would be `baseten:zai-org/GLM-5.1`. Check the provider's model catalog or integration docs for the current identifiers.

### Suggested models

These models perform well on the [Deep Agents eval suite](https://github.com/langchain-ai/deepagents/tree/main/libs/evals#readme), which tests basic agent operations. Passing these evals is necessary but not sufficient for strong performance on longer, more complex tasks.

| Provider                                                  | Models                                                                                                                                   |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| [Google](/oss/python/integrations/providers/google)       | `gemini-3.1-pro-preview`, `gemini-3-flash-preview`                                                                                       |
| [OpenAI](/oss/python/integrations/providers/openai)       | `gpt-5.4`, `gpt-4o`, `gpt-5.4`, `o4-mini`, `gpt-5.2-codex`, `gpt-4o-mini`, `o3`                                                          |
| [Anthropic](/oss/python/integrations/providers/anthropic) | `claude-opus-4-6`, `claude-opus-4-5`, `claude-sonnet-4-6`, `claude-sonnet-4`, `claude-sonnet-4-5`, `claude-haiku-4-5`, `claude-opus-4-1` |
| Open-weight                                               | `GLM-5`, `Kimi-K2.5`, `MiniMax-M2.5`, `qwen3.5-397B-A17B`, `devstral-2-123B`                                                             |

Open-weight models are available through providers like [Baseten](/oss/python/integrations/providers/baseten), [Fireworks](/oss/python/integrations/chat/fireworks), [OpenRouter](/oss/python/integrations/providers/openrouter), and [Ollama](/oss/python/integrations/providers/ollama).

### Model evaluations

The [Deep Agents eval suite](https://github.com/langchain-ai/deepagents/tree/main/libs/evals#readme) tests popular models:

<div>
  | Model                                            |                                                                        Overall |                                                                        File Ops |                                                                       Retrieval |                                                                       Tool Use |                                                                         Memory |                                                                   Conversation |                                                                   Summarization |
  | :----------------------------------------------- | -----------------------------------------------------------------------------: | ------------------------------------------------------------------------------: | ------------------------------------------------------------------------------: | -----------------------------------------------------------------------------: | -----------------------------------------------------------------------------: | -----------------------------------------------------------------------------: | ------------------------------------------------------------------------------: |
  | google\_genai:gemini-3.5-flash                   |     [82%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** | **[90%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |     [54%](https://github.com/langchain-ai/deepagents/actions/runs/25290479270) |     [38%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |
  | openai:gpt-5.4                                   |     [18%](https://github.com/langchain-ai/deepagents/actions/runs/24906955930) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** |     [18%](https://github.com/langchain-ai/deepagents/actions/runs/24906955930) |     [51%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583) |     [38%](https://github.com/langchain-ai/deepagents/actions/runs/24425363630) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** |
  | openai:gpt-5.5                                   |     [80%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |     [84%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |     [64%](https://github.com/langchain-ai/deepagents/actions/runs/25345307822) | **[52%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |
  | anthropic:claude-opus-4-6                        |     [26%](https://github.com/langchain-ai/deepagents/actions/runs/24906955930) |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** |     [26%](https://github.com/langchain-ai/deepagents/actions/runs/24906955930) | **[69%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** |     [22%](https://github.com/langchain-ai/deepagents/actions/runs/24363491527) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/24172638583)** |
  | anthropic:claude-opus-4-7                        |     [80%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |     [82%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |                                                                              — |     [48%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |
  | baseten:moonshotai/Kimi-K2.6                     |     [79%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906) |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906)** |     [84%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906) |                                                                              — |     [43%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906) |      [60%](https://github.com/langchain-ai/deepagents/actions/runs/25475600906) |
  | baseten:zai-org/GLM-5                            |     [77%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424)** |     [89%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424) |     [44%](https://github.com/langchain-ai/deepagents/actions/runs/23872647281) |     [24%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424) |      [60%](https://github.com/langchain-ai/deepagents/actions/runs/25403850424) |
  | fireworks:accounts/fireworks/models/glm-5p1      |     [81%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650)** |     [87%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650) |                                                                              — |     [33%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650) |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25461031650) |
  | fireworks:accounts/fireworks/models/minimax-m2p7 |     [79%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412)** | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412)** |     [85%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412) |                                                                              — |     [43%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412) |      [60%](https://github.com/langchain-ai/deepagents/actions/runs/25403894412) |
  | ollama:minimax-m2.7:cloud                        |     [73%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |      [90%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |     [82%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |     [38%](https://github.com/langchain-ai/deepagents/actions/runs/23872647281) |     [29%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |      [60%](https://github.com/langchain-ai/deepagents/actions/runs/24106499785) |
  | openrouter:deepseek/deepseek-v4-flash            |     [81%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395)** |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395) | **[90%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395)** |                                                                              — |     [33%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395) |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25677815395) |
  | openrouter:minimax/minimax-m2.7                  |     [80%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535)** |     [89%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |                                                                              — |     [43%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |      [60%](https://github.com/langchain-ai/deepagents/actions/runs/25455998535) |
  | openrouter:z-ai/glm-5.1                          | **[89%](https://github.com/langchain-ai/deepagents/actions/runs/25387853856)** |      [92%](https://github.com/langchain-ai/deepagents/actions/runs/25234719085) | **[100%](https://github.com/langchain-ai/deepagents/actions/runs/25234686782)** |     [89%](https://github.com/langchain-ai/deepagents/actions/runs/25387853856) |                                                                              — |     [33%](https://github.com/langchain-ai/deepagents/actions/runs/25225620506) |      [80%](https://github.com/langchain-ai/deepagents/actions/runs/25235579950) |
</div>

For more information, see the [Eval runs](https://github.com/langchain-ai/deepagents/actions/workflows/evals.yml).

## Configure model parameters

Pass a model string to [`create_deep_agent`](https://reference.langchain.com/python/deepagents/graph/create_deep_agent) in `provider:model` format, or pass a configured model instance for full control. Under the hood, model strings are resolved via [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model).

To configure model-specific parameters, use [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model) or instantiate a provider model class directly:

<CodeGroup>
  ```python init_chat_model theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain.chat_models import init_chat_model
  from deepagents import create_deep_agent

  model = init_chat_model(
      model="google_genai:gemini-3.5-flash",
      thinking_level="medium",  # [!code highlight]
  )
  agent = create_deep_agent(model=model)
  ```

  ```python Provider package theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langchain_google_genai import ChatGoogleGenerativeAI
  from deepagents import create_deep_agent

  model = ChatGoogleGenerativeAI(
      model="gemini-3.1-pro-preview",
      thinking_level="medium",  # [!code highlight]
  )
  agent = create_deep_agent(model=model)
  ```
</CodeGroup>

<Note>
  Available parameters vary by provider. See the [chat model integrations](/oss/python/integrations/chat) page for provider-specific configuration options.
</Note>

### Provider profiles

A [`ProviderProfile`](/oss/python/deepagents/profiles#provider-profiles) packages initialization parameters that apply when you provide a `provider:model` string when creating the deep agent. It does not apply when you pass a preconfigured model with [`init_chat_model`](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model).

You can register at two levels, and both can coexist:

* **Provider level** — a bare provider key like `"openai"` applies to every model from the `openai` provider.
* **Model level** — a `provider:model` key like `"openai:gpt-5.4"` applies only to that specific model, and merges on top of any matching provider-level profile.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import ProviderProfile, register_provider_profile

# Provider-wide default: every openai model gets temperature=0.
register_provider_profile(
    "openai",
    ProviderProfile(init_kwargs={"temperature": 0}),
)

# Model-level override: gpt-5.4 additionally gets a specific reasoning effort.

# Inherits temperature=0 from the provider-level profile above.
register_provider_profile(
    "openai:gpt-5.4",
    ProviderProfile(init_kwargs={"reasoning_effort": "medium"}),
)
```

See [Profiles](/oss/python/deepagents/profiles) for the full field list, merge semantics, and plugin packaging.

<Tip>
  For shaping how the *agent* behaves once the model is built, use a [harness profile](/oss/python/deepagents/profiles#harness-profiles).
</Tip>

## Select a model at runtime

If your application lets users choose a model (for example using a dropdown in the UI), use [middleware](/oss/python/langchain/middleware) to swap the model at runtime without rebuilding the agent.

Pass the user's model selection through [runtime context](/oss/python/langchain/models#dynamic-model-selection), then use a `wrap_model_call` middleware to override the model on each invocation using the [`@wrap_model_call`](https://reference.langchain.com/python/langchain/agents/middleware/types/wrap_model_call) decorator:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from dataclasses import dataclass
from langchain.chat_models import init_chat_model
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from deepagents import create_deep_agent
from typing import Callable

@dataclass
class Context:
    model: str

@wrap_model_call
def configurable_model(
    request: ModelRequest,
    handler: Callable[[ModelRequest], ModelResponse],
) -> ModelResponse:
    model_name = request.runtime.context.model
    model = init_chat_model(model_name)
    return handler(request.override(model=model))

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    middleware=[configurable_model],
    context_schema=Context,
)

# Invoke with the user's model selection
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Hello!"}]},
    context=Context(model="openai:gpt-5.4"),
)
```

<Tip>
  For more dynamic model patterns (for example routing based on conversation complexity or cost optimization), see [Dynamic model](/oss/python/langchain/models#dynamic-model-selection) in the LangChain agents guide.
</Tip>

## Learn more

* [Models in LangChain](/oss/python/langchain/models): chat model features including tool calling, structured output, and multimodality

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/models.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deep Agents overview
Source: https://docs.langchain.com/oss/python/deepagents/overview

Build agents that can plan, use subagents, and leverage file systems for complex tasks

The easiest way to start building agents and applications powered by LLMs—with built-in capabilities for task planning, file systems for context management, subagent-spawning, and long-term memory.
You can use deep agents for any task, including complex, multi-step tasks.

Deep Agents is an ["agent harness"](/oss/python/concepts/products#agent-harnesses-like-the-deep-agents-sdk). It is the same core tool calling loop as other agent frameworks, but with built-in capabilities that make agents reliable for real tasks:

<CardGroup>
  <Card title="Take actions in an environment" icon="bolt">
    Take actions via tools, read and write files, execute code
  </Card>

  <Card title="Connect to your data" icon="database">
    Load memories, skills, and domain knowledge at the right moment
  </Card>

  <Card title="Manage growing context" icon="scissors">
    Summarize history and offload large results across long runs
  </Card>

  <Card title="Parallelize tasks" icon="sitemap">
    Delegate to general or specialized subagents running in isolated context windows
  </Card>

  <Card title="Stay in the loop" icon="user">
    Pause for human approval at critical decision points
  </Card>

  <Card title="Improve over time" icon="rocket">
    Update memory, skills, and prompts based on real usage
  </Card>
</CardGroup>

See [Harness capabilities](/oss/python/deepagents/harness) for a full breakdown of each component.

[`deepagents`](https://pypi.org/project/deepagents/) is a standalone library built on top of [LangChain](/oss/python/langchain/)'s core building blocks for agents. It uses the [LangGraph](/oss/python/langgraph/) runtime for durable execution, streaming, human-in-the-loop, and other features.

[LangChain](/oss/python/langchain/) is the framework that provides the core building blocks for your agents.
To learn more about the differences between LangChain, LangGraph, and Deep Agents, see [Frameworks, runtimes, and harnesses](/oss/python/concepts/products). For a side-by-side comparison with Anthropic's harness, see [Deep Agents vs. Claude Agent SDK](/oss/python/deepagents/comparison).

## <Icon icon="wand" /> Create a deep agent

<Tabs>
  <Tab title="Google">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # pip install -qU deepagents langchain-google-genai
    from deepagents import create_deep_agent

    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

    agent = create_deep_agent(
        model="google_genai:gemini-3.5-flash",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )
    ```
  </Tab>

  <Tab title="OpenAI">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # pip install -qU deepagents langchain-openai
    from deepagents import create_deep_agent

    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

    agent = create_deep_agent(
        model="openai:gpt-5.5",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )
    ```
  </Tab>

  <Tab title="Anthropic">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # pip install -qU deepagents langchain-anthropic
    from deepagents import create_deep_agent

    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

    agent = create_deep_agent(
        model="anthropic:claude-sonnet-4-6",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )
    ```
  </Tab>

  <Tab title="OpenRouter">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # pip install -qU deepagents langchain-openrouter
    from deepagents import create_deep_agent

    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

    agent = create_deep_agent(
        model="openrouter:anthropic/claude-sonnet-4-6",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )
    ```
  </Tab>

  <Tab title="Fireworks">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # pip install -qU deepagents langchain-fireworks
    from deepagents import create_deep_agent

    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

    agent = create_deep_agent(
        model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )
    ```
  </Tab>

  <Tab title="Baseten">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # pip install -qU deepagents langchain-baseten
    from deepagents import create_deep_agent

    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

    agent = create_deep_agent(
        model="baseten:zai-org/GLM-5",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )
    ```
  </Tab>

  <Tab title="Ollama">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # pip install -qU deepagents langchain-ollama
    from deepagents import create_deep_agent

    def get_weather(city: str) -> str:
        """Get weather for a given city."""
        return f"It's always sunny in {city}!"

    agent = create_deep_agent(
        model="ollama:devstral-2",
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )
    ```
  </Tab>
</Tabs>

See the [Quickstart](/oss/python/deepagents/quickstart/) and [Customization guide](/oss/python/deepagents/customization/) to get started building your own agents and applications with Deep Agents.

<Tip>
  Trace requests, debug agent behavior, and evaluate outputs with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-overview). Follow the [observability quickstart](/langsmith/observability-quickstart) to get set up. When ready for production, see [Going to production](/oss/python/deepagents/going-to-production) for LangSmith deployment options.
</Tip>

## Core capabilities

Use the **Deep Agents SDK** to build agents that handle complex, multi-step tasks across **any [model provider](/oss/python/deepagents/models)**. The SDK ships with the following built-in capabilities:

<Card title="Planning and task decomposition" icon="timeline">
  A built-in [`write_todos`](/oss/python/langchain/middleware/built-in#to-do-list) tool lets agents break down complex tasks into discrete steps, track progress, and adapt plans as new information emerges.
</Card>

<Card title="Context management" icon="scissors">
  Built-in [context compression](/oss/python/deepagents/context-engineering#context-compression) offloads large tool inputs and results to the [virtual filesystem](/oss/python/deepagents/harness#virtual-filesystem-access) and [summarizes](/oss/python/deepagents/context-engineering#summarization) older messages to keep agents effective across extended sessions.
</Card>

<Card title="Tools and MCP" icon="tool">
  Pass custom functions, LangChain tools, or tools from any [MCP server](/oss/python/deepagents/tools#mcp-tools) to `create_deep_agent`. Deep Agents fully support the [Model Context Protocol (MCP)](/oss/python/langchain/mcp), letting you connect to databases, APIs, file systems, and more through a standard interface.
</Card>

<Card title="Pluggable filesystem backends" icon="plug">
  Swap the virtual filesystem via [pluggable backends](/oss/python/deepagents/backends): in-memory state, local disk, LangGraph store, composite routing, or a custom backend with [permission rules](/oss/python/deepagents/permissions) for read and write access.
</Card>

<Card title="Shell execution" icon="terminal">
  Shell-capable backends add an `execute` tool for tests, builds, git operations, and system tasks. Use [`LocalShellBackend`](/oss/python/deepagents/backends#localshellbackend-local-shell) on the host for local development, or a [sandbox backend](/oss/python/deepagents/sandboxes) when you need isolation from your host system.
</Card>

<Card title="Interpreters" icon="code">
  Add an [interpreter](/oss/python/deepagents/interpreters) to run JavaScript in an in-memory runtime. Interpreters let agents compose tools programmatically, orchestrate subagents, and transform structured data without a full shell environment.
</Card>

<Card title="Subagent spawning" icon="users-group">
  A built-in `task` tool spawns general-purpose or specialized [subagents](/oss/python/deepagents/subagents) for context isolation on subtasks. For long-running or parallel work, [async subagents](/oss/python/deepagents/async-subagents) run in the background with progress checks, follow-ups, and cancellation.
</Card>

<Card title="Streaming" icon="broadcast">
  [Event streaming](/oss/python/deepagents/event-streaming) exposes agent runs as typed projections for messages, tool calls, values, and output. Deep Agents add `stream.subagents` so each delegated task gets its own handle with independent message, tool-call, and nested subagent streams.
</Card>

<Card title="Long-term memory" icon="database">
  Persist memory across threads and conversations using LangGraph's [Memory Store](/oss/python/langgraph/stores).
</Card>

<Card title="Filesystem permissions" icon="lock">
  Declare [permission rules](/oss/python/deepagents/permissions) that control which files and directories agents can read or write. Subagents can inherit or override the parent's rules.
</Card>

<Card title="Human-in-the-loop" icon="user-check">
  Configure [human approval](/oss/python/deepagents/human-in-the-loop) for sensitive tool operations using LangGraph's interrupt capabilities.
</Card>

<Card title="Skills" icon="puzzle">
  Extend agents with reusable [skills](/oss/python/deepagents/skills) that provide specialized workflows, domain knowledge, and custom instructions.
</Card>

<Card title="Smart defaults" icon="wand">
  Ships with opinionated system prompts that teach the model to plan before acting, verify work, and manage context. Customize or replace the defaults as needed.
</Card>

For building custom agents without these builtin capabilities, consider using LangChain's [`create_agent`](/oss/python/langchain/agents) or building a custom [LangGraph](/oss/python/langgraph/overview) workflow.

## Get started

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/oss/python/deepagents/quickstart">
    Build your first deep agent
  </Card>

  <Card title="Customization" icon="adjustments" href="/oss/python/deepagents/customization">
    Learn about customization options
  </Card>

  <Card title="Tools and MCP" icon="tool" href="/oss/python/deepagents/tools">
    Connect custom functions, APIs, and MCP servers
  </Card>

  <Card title="Models" icon="cpu" href="/oss/python/deepagents/models">
    Configure models and providers
  </Card>

  <Card title="Backends" icon="plug" href="/oss/python/deepagents/backends">
    Choose and configure pluggable filesystem backends
  </Card>

  <Card title="Sandboxes" icon="cube" href="/oss/python/deepagents/sandboxes">
    Execute code in isolated environments
  </Card>

  <Card title="Interpreters" icon="code" href="/oss/python/deepagents/interpreters">
    Compose tools and transform data in QuickJS
  </Card>

  <Card title="Permissions" icon="lock" href="/oss/python/deepagents/permissions">
    Control filesystem access with permission rules
  </Card>

  <Card title="Human-in-the-loop" icon="user-check" href="/oss/python/deepagents/human-in-the-loop">
    Configure approval for sensitive operations
  </Card>

  <Card title="Code" icon="terminal" href="/oss/python/deepagents/code/overview">
    Use Deep Agents Code
  </Card>

  <Card title="ACP" icon="plug-connected" href="/oss/python/deepagents/acp">
    Use deep agents in code editors via ACP
  </Card>

  <Card title="Reference" icon="external-link" href="https://reference.langchain.com/python/deepagents/">
    See the `deepagents` API reference
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Permissions
Source: https://docs.langchain.com/oss/python/deepagents/permissions

Control filesystem access with declarative permission rules for Deep Agents

Control which files and directories an agent can read or write to using declarative permission rules. Pass a list of rules to `permissions=` and the agent's built-in filesystem tools respect them.

<Note>
  Permissions require `deepagents>=0.5.2`.
</Note>

Permissions only apply to the built-in filesystem tools (`ls`, `read_file`, `glob`, `grep`, `write_file`, `edit_file`). Custom tools and MCP tools that access the filesystem are not covered. Permissions also do not apply to [sandbox backends](/oss/python/deepagents/sandboxes), which support arbitrary command execution via the `execute` tool.

<Tip>
  Use `permissions` when you need **path-based allow/deny rules** on the built-in filesystem tools. Use [backend policy hooks](/oss/python/deepagents/backends#add-policy-hooks) when you need custom validation logic (rate limiting, audit logging, content inspection) or need to control custom tools.
</Tip>

## Basic usage

Pass a list of [`FilesystemPermission`](https://reference.langchain.com/python/deepagents/middleware/permissions/FilesystemPermission) rules to [`create_deep_agent`](https://reference.langchain.com/python/deepagents/graph/create_deep_agent). Rules are evaluated in declaration order. The first matching rule wins. If no rule matches, the operation is allowed.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import FilesystemPermission, create_deep_agent

# Read-only agent: deny all writes
agent = create_deep_agent(
    model=model,
    backend=backend,
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/**"],
            mode="deny",
        ),
    ],
)
```

## Rule structure

Each `FilesystemPermission` has three fields:

| Field        | Type                               | Description                                                                                                                                                   |
| ------------ | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `operations` | `list["read" \| "write"]`          | Operations this rule applies to. `"read"` covers `ls`, `read_file`, `glob`, `grep`. `"write"` covers `write_file`, `edit_file`.                               |
| `paths`      | `list[str]`                        | Glob patterns for matching file paths (e.g., `["/workspace/**"]`). Supports `**` for recursive matching and `{a,b}` for alternation.                          |
| `mode`       | `"allow" \| "deny" \| "interrupt"` | Whether to allow, deny, or pause for human approval on matching operations. Defaults to `"allow"`. See [Pause for human approval](#pause-for-human-approval). |

Rules use first-match-wins evaluation: the first rule whose `operations` and `paths` match the current call determines the outcome. If no rule matches, the call is **allowed** (permissive default).

## Pause for human approval

<Note>
  The `"interrupt"` mode requires `deepagents>=0.6.8`.
</Note>

Set `mode="interrupt"` to pause for human approval instead of allowing or denying a matching operation outright. When the agent calls a built-in write tool (`write_file`, `edit_file`) on a path that matches an interrupt-mode rule, `create_deep_agent` raises a human-in-the-loop interrupt rather than running the tool, and a reviewer can approve, edit, or reject the call.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import FilesystemPermission, create_deep_agent
from langgraph.checkpoint.memory import InMemorySaver

agent = create_deep_agent(
    model=model,
    permissions=[
        # Pause for approval before writing anything under /secrets.
        FilesystemPermission(
            operations=["write"],
            paths=["/secrets/**"],
            mode="interrupt",
        ),
    ],
    # Interrupt mode requires a checkpointer to pause and resume.
    checkpointer=InMemorySaver(),
)
```

Interrupt-mode rules are wired into the agent's human-in-the-loop middleware automatically and merge with any `interrupt_on` you pass, so you handle and resume them the same way as tool-call interrupts. See [Human-in-the-loop](/oss/python/deepagents/human-in-the-loop) for the resume flow.

<Tip>
  Anchor interrupt patterns with a literal leading segment (for example, `/secrets/**` or `/projects/*/secrets/**`). Bulk tools (`ls`, `glob`, `grep`) fire the interrupt when their search subtree could overlap the rule's anchored prefix, so a fully unanchored pattern like `/**/secrets` conservatively over-fires.
</Tip>

## Examples

### Isolate to a workspace directory

Allow reads and writes only under `/workspace/` and deny everything else:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
agent = create_deep_agent(
    model=model,
    backend=backend,
    permissions=[
        FilesystemPermission(
            operations=["read", "write"],
            paths=["/workspace/**"],
            mode="allow",
        ),
        FilesystemPermission(
            operations=["read", "write"],
            paths=["/**"],
            mode="deny",
        ),
    ],
)
```

### Protect specific files

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
agent = create_deep_agent(
    model=model,
    backend=backend,
    permissions=[
        FilesystemPermission(
            operations=["read", "write"],
            paths=["/workspace/.env", "/workspace/examples/**"],
            mode="deny",
        ),
        FilesystemPermission(
            operations=["read", "write"],
            paths=["/workspace/**"],
            mode="allow",
        ),
        FilesystemPermission(
            operations=["read", "write"],
            paths=["/**"],
            mode="deny",
        ),
    ],
)
```

### Read-only memory

Allow the agent to read memory files but prevent it from modifying them. This is useful for organization-wide policies or shared knowledge bases that should only be updated by application code. See [read-only vs writable memory](/oss/python/deepagents/memory#read-only-vs-writable-memory) for more context.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

agent = create_deep_agent(
    model=model,
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": StoreBackend(
                namespace=lambda rt: (rt.server_info.user.identity,),
            ),
            "/policies/": StoreBackend(
                namespace=lambda rt: (rt.context.org_id,),
            ),
        },
    ),
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/memories/**", "/policies/**"],
            mode="deny",
        ),
    ],
)
```

### Deny all access

Block all reads and writes. This is a restrictive baseline you can layer more specific allow rules on top of:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
agent = create_deep_agent(
    model=model,
    backend=backend,
    permissions=[
        FilesystemPermission(
            operations=["read", "write"],
            paths=["/**"],
            mode="deny",
        ),
    ],
)
```

### Rule ordering

Because of first-match-wins, rule order matters. Place more specific rules before broader ones:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Correct: deny .env, allow workspace, deny everything else
correct_permissions = [
    FilesystemPermission(
        operations=["read", "write"],
        paths=["/workspace/.env"],
        mode="deny",
    ),
    FilesystemPermission(
        operations=["read", "write"],
        paths=["/workspace/**"],
        mode="allow",
    ),
    FilesystemPermission(
        operations=["read", "write"],
        paths=["/**"],
        mode="deny",
    ),
]

# Bug: /workspace/** matches .env first, so the deny never triggers
incorrect_permissions = [
    FilesystemPermission(
        operations=["read", "write"],
        paths=["/workspace/**"],
        mode="allow",
    ),
    FilesystemPermission(
        operations=["read", "write"],
        paths=["/workspace/.env"],
        mode="deny",  # never reached
    ),
    FilesystemPermission(
        operations=["read", "write"],
        paths=["/**"],
        mode="deny",
    ),
]
```

## Subagent permissions

[Subagents](/oss/python/deepagents/subagents) inherit the parent agent's permissions by default. To give a subagent different permissions, set the `permissions` field in its spec. This **replaces** the parent's rules entirely.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
agent = create_deep_agent(
    model=model,
    backend=backend,
    permissions=[
        FilesystemPermission(
            operations=["read", "write"],
            paths=["/workspace/**"],
            mode="allow",
        ),
        FilesystemPermission(
            operations=["read", "write"],
            paths=["/**"],
            mode="deny",
        ),
    ],
    subagents=[
        {
            "name": "auditor",
            "description": "Read-only code reviewer",
            "system_prompt": "Review the code for issues.",
            "permissions": [
                FilesystemPermission(
                    operations=["write"],
                    paths=["/**"],
                    mode="deny",
                ),
                FilesystemPermission(
                    operations=["read"],
                    paths=["/workspace/**"],
                    mode="allow",
                ),
                FilesystemPermission(
                    operations=["read"],
                    paths=["/**"],
                    mode="deny",
                ),
            ],
        }
    ],
)
```

## Composite backends

When using a [`CompositeBackend`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend) with a sandbox default, every permission path must be scoped under a known route prefix. Sandboxes support arbitrary command execution, so path-based restrictions alone cannot prevent filesystem access through shell commands. Scoping permissions to route-specific [backends](/oss/python/deepagents/backends) avoids this conflict.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents.backends import CompositeBackend

composite = CompositeBackend(
    default=sandbox,
    routes={"/memories/": memories_backend},
)

# Works: permissions are scoped to the /memories/ route
agent = create_deep_agent(
    model=model,
    backend=composite,
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/memories/**"],
            mode="deny",
        ),
    ],
)
```

Permissions that include paths outside any route raise `NotImplementedError`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Raises NotImplementedError: /workspace/** hits the sandbox default
try:
    create_deep_agent(
        model=model,
        backend=composite,
        permissions=[
            FilesystemPermission(
                operations=["write"],
                paths=["/workspace/**"],
                mode="deny",
            ),
        ],
    )
except NotImplementedError:
    pass

# Also raises: /** covers both routes and the default
try:
    create_deep_agent(
        model=model,
        backend=composite,
        permissions=[
            FilesystemPermission(
                operations=["read"],
                paths=["/**"],
                mode="deny",
            ),
        ],
    )
except NotImplementedError:
    pass
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/permissions.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
