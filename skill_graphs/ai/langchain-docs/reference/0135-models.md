# Models
Source: https://docs.langchain.com/oss/javascript/deepagents/models

Configure model providers and parameters for Deep Agents

Deep Agents work with any [LangChain chat model](/oss/javascript/langchain/models) that supports [tool calling](/oss/javascript/langchain/models#tool-calling).

## Supported models

Specify models in `provider:model` format (for example, `google_genai:gemini-3.5-flash`, `openai:gpt-5.4`, or `anthropic:claude-sonnet-4-6`). The provider prefix selects the LangChain integration, and everything after the colon is passed through to that provider as the model identifier. For valid provider strings, see the `model_provider` parameter of [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel). For provider-specific configuration, see [chat model integrations](/oss/javascript/integrations/chat).

The model identifier must match the format expected by the provider. Some providers use simple names like `gpt-5.4`; others use namespaced IDs or deployment paths like `zai-org/GLM-5.1`, so the full Deep Agents string would be `baseten:zai-org/GLM-5.1`. Check the provider's model catalog or integration docs for the current identifiers.

### Suggested models

These models perform well on the [Deep Agents eval suite](https://github.com/langchain-ai/deepagents/tree/main/libs/evals#readme), which tests basic agent operations. Passing these evals is necessary but not sufficient for strong performance on longer, more complex tasks.

| Provider                                                      | Models                                                                                                                                   |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| [Google](/oss/javascript/integrations/providers/google)       | `gemini-3.1-pro-preview`, `gemini-3-flash-preview`                                                                                       |
| [OpenAI](/oss/javascript/integrations/providers/openai)       | `gpt-5.4`, `gpt-4o`, `gpt-5.4`, `o4-mini`, `gpt-5.2-codex`, `gpt-4o-mini`, `o3`                                                          |
| [Anthropic](/oss/javascript/integrations/providers/anthropic) | `claude-opus-4-6`, `claude-opus-4-5`, `claude-sonnet-4-6`, `claude-sonnet-4`, `claude-sonnet-4-5`, `claude-haiku-4-5`, `claude-opus-4-1` |
| Open-weight                                                   | `GLM-5`, `Kimi-K2.5`, `MiniMax-M2.5`, `qwen3.5-397B-A17B`, `devstral-2-123B`                                                             |

Open-weight models are available through providers like [OpenRouter](/oss/javascript/integrations/chat/openrouter) and [Ollama](/oss/javascript/integrations/chat/ollama).

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

Pass a model string to [`createDeepAgent`](https://reference.langchain.com/javascript/deepagents/agent/createDeepAgent) in `provider:model` format, or pass a configured model instance for full control. Under the hood, model strings are resolved via [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel).

To configure model-specific parameters, use [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel) or instantiate a provider model class directly:

<CodeGroup>
  ```typescript initChatModel theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { initChatModel } from "langchain/chat_models/universal";
  import { createDeepAgent } from "deepagents";

  const model = await initChatModel("google_genai:gemini-3.5-flash", {
      reasoningEffort: "medium",  // [!code highlight]
  });
  const agent = createDeepAgent({ model });
  ```

  ```typescript Provider package theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { ChatGoogle } from "@langchain/google";
  import { createDeepAgent } from "deepagents";

  const model = new ChatGoogle({
      model: "gemini-3.1-pro-preview",
      reasoningEffort: "medium",  // [!code highlight]
  });
  const agent = createDeepAgent({ model });
  ```
</CodeGroup>

<Note>
  Available parameters vary by provider. See the [chat model integrations](/oss/javascript/integrations/chat) page for provider-specific configuration options.
</Note>

### Provider profiles

A [`ProviderProfile`](/oss/javascript/deepagents/profiles#provider-profiles) packages initialization parameters that apply when you provide a `provider:model` string when creating the deep agent. It does not apply when you pass a preconfigured model with [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel).

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

See [Profiles](/oss/javascript/deepagents/profiles) for the full field list, merge semantics, and plugin packaging.

<Tip>
  For shaping how the *agent* behaves once the model is built, use a [harness profile](/oss/javascript/deepagents/profiles#harness-profiles).
</Tip>

## Select a model at runtime

If your application lets users choose a model (for example using a dropdown in the UI), use [middleware](/oss/javascript/langchain/middleware) to swap the model at runtime without rebuilding the agent.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { initChatModel, createMiddleware } from "langchain";
import { createDeepAgent } from "deepagents";
import * as z from "zod";

const contextSchema = z.object({
  model: z.string(),
});

const configurableModel = createMiddleware({
  name: "ConfigurableModel",
  wrapModelCall: async (request, handler) => {
    const modelName = request.runtime.context.model;
    const model = await initChatModel(modelName);
    return handler({ ...request, model });
  },
});

const agent = await createDeepAgent({
  model: "google_genai:gemini-3.5-flash",
  middleware: [configurableModel],
  contextSchema,
});

// Invoke with the user's model selection
const result = await agent.invoke(
  { messages: [{ role: "user", content: "Hello!" }] },
  { context: { model: "openai:gpt-5.4" } },
);
```

<Tip>
  For more dynamic model patterns (for example routing based on conversation complexity or cost optimization), see [Dynamic model](/oss/javascript/langchain/models#dynamic-model-selection) in the LangChain agents guide.
</Tip>

## Learn more

* [Models in LangChain](/oss/javascript/langchain/models): chat model features including tool calling, structured output, and multimodality

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
Source: https://docs.langchain.com/oss/javascript/deepagents/overview

Build agents that can plan, use subagents, and leverage file systems for complex tasks

The easiest way to start building agents and applications powered by LLMs—with built-in capabilities for task planning, file systems for context management, subagent-spawning, and long-term memory.
You can use deep agents for any task, including complex, multi-step tasks.

Deep Agents is an ["agent harness"](/oss/javascript/concepts/products#agent-harnesses-like-the-deep-agents-sdk). It is the same core tool calling loop as other agent frameworks, but with built-in capabilities that make agents reliable for real tasks:

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

See [Harness capabilities](/oss/javascript/deepagents/harness) for a full breakdown of each component.

[`deepagents`](https://www.npmjs.com/package/deepagents) is a standalone library built on top of [LangChain](/oss/javascript/langchain/)'s core building blocks for agents and using [LangGraph](/oss/javascript/langgraph/)'s tooling for running agents in production.

[LangChain](/oss/javascript/langchain/) is the framework that provides the core building blocks for your agents.
To learn more about the differences between LangChain, LangGraph, and Deep Agents, see [Frameworks, runtimes, and harnesses](/oss/javascript/concepts/products). For a side-by-side comparison with Anthropic's harness, see [Deep Agents vs. Claude Agent SDK](/oss/javascript/deepagents/comparison).

## <Icon icon="wand" /> Create a deep agent

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as z from "zod";
// npm install deepagents langchain @langchain/core
import { createDeepAgent } from "deepagents";
import { tool } from "langchain";

const getWeather = tool(
  ({ city }) => `It's always sunny in ${city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string(),
    }),
  },
);

const agent = createDeepAgent({
  tools: [getWeather],
  systemPrompt: "You are a helpful assistant",
});

console.log(
  await agent.invoke({
    messages: [{ role: "user", content: "What's the weather in Tokyo?" }],
  })
);
```

See the [Quickstart](/oss/javascript/deepagents/quickstart/) and [Customization guide](/oss/javascript/deepagents/customization/) to get started building your own agents and applications with Deep Agents.

<Tip>
  Trace requests, debug agent behavior, and evaluate outputs with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-overview). Follow the [observability quickstart](/langsmith/observability-quickstart) to get set up. When ready for production, see [Going to production](/oss/javascript/deepagents/going-to-production) for LangSmith deployment options.
</Tip>

## Core capabilities

Use the **Deep Agents SDK** to build agents that handle complex, multi-step tasks across **any [model provider](/oss/javascript/deepagents/models)**. The SDK ships with the following built-in capabilities:

<Card title="Planning and task decomposition" icon="timeline">
  A built-in [`write_todos`](/oss/javascript/langchain/middleware/built-in#to-do-list) tool lets agents break down complex tasks into discrete steps, track progress, and adapt plans as new information emerges.
</Card>

<Card title="Context management" icon="scissors">
  Built-in [context compression](/oss/javascript/deepagents/context-engineering#context-compression) offloads large tool inputs and results to the [virtual filesystem](/oss/javascript/deepagents/harness#virtual-filesystem-access) and [summarizes](/oss/javascript/deepagents/context-engineering#summarization) older messages to keep agents effective across extended sessions.
</Card>

<Card title="Tools and MCP" icon="tool">
  Pass custom functions, LangChain tools, or tools from any [MCP server](/oss/javascript/deepagents/tools#mcp-tools) to `create_deep_agent`. Deep Agents fully support the [Model Context Protocol (MCP)](/oss/javascript/langchain/mcp), letting you connect to databases, APIs, file systems, and more through a standard interface.
</Card>

<Card title="Pluggable filesystem backends" icon="plug">
  Swap the virtual filesystem via [pluggable backends](/oss/javascript/deepagents/backends): in-memory state, local disk, LangGraph store, composite routing, or a custom backend with [permission rules](/oss/javascript/deepagents/permissions) for read and write access.
</Card>

<Card title="Shell execution" icon="terminal">
  Shell-capable backends add an `execute` tool for tests, builds, git operations, and system tasks. Use [`LocalShellBackend`](/oss/javascript/deepagents/backends#localshellbackend-local-shell) on the host for local development, or a [sandbox backend](/oss/javascript/deepagents/sandboxes) when you need isolation from your host system.
</Card>

<Card title="Interpreters" icon="code">
  Add an [interpreter](/oss/javascript/deepagents/interpreters) to run JavaScript in an in-memory runtime. Interpreters let agents compose tools programmatically, orchestrate subagents, and transform structured data without a full shell environment.
</Card>

<Card title="Subagent spawning" icon="users-group">
  A built-in `task` tool spawns general-purpose or specialized [subagents](/oss/javascript/deepagents/subagents) for context isolation on subtasks. For long-running or parallel work, [async subagents](/oss/javascript/deepagents/async-subagents) run in the background with progress checks, follow-ups, and cancellation.
</Card>

<Card title="Streaming" icon="broadcast">
  [Event streaming](/oss/javascript/deepagents/event-streaming) exposes agent runs as typed projections for messages, tool calls, values, and output. Deep Agents add `stream.subagents` so each delegated task gets its own handle with independent message, tool-call, and nested subagent streams.
</Card>

<Card title="Long-term memory" icon="database">
  Persist memory across threads and conversations using LangGraph's [Memory Store](/oss/javascript/langgraph/stores).
</Card>

<Card title="Filesystem permissions" icon="lock">
  Declare [permission rules](/oss/javascript/deepagents/permissions) that control which files and directories agents can read or write. Subagents can inherit or override the parent's rules.
</Card>

<Card title="Human-in-the-loop" icon="user-check">
  Configure [human approval](/oss/javascript/deepagents/human-in-the-loop) for sensitive tool operations using LangGraph's interrupt capabilities.
</Card>

<Card title="Skills" icon="puzzle">
  Extend agents with reusable [skills](/oss/javascript/deepagents/skills) that provide specialized workflows, domain knowledge, and custom instructions.
</Card>

<Card title="Smart defaults" icon="wand">
  Ships with opinionated system prompts that teach the model to plan before acting, verify work, and manage context. Customize or replace the defaults as needed.
</Card>

For building custom agents without these builtin capabilities, consider using LangChain's [`createAgent`](/oss/javascript/langchain/agents) or building a custom [LangGraph](/oss/javascript/langgraph/overview) workflow.

## Get started

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/oss/javascript/deepagents/quickstart">
    Build your first deep agent
  </Card>

  <Card title="Customization" icon="adjustments" href="/oss/javascript/deepagents/customization">
    Learn about customization options
  </Card>

  <Card title="Tools and MCP" icon="tool" href="/oss/javascript/deepagents/tools">
    Connect custom functions, APIs, and MCP servers
  </Card>

  <Card title="Models" icon="cpu" href="/oss/javascript/deepagents/models">
    Configure models and providers
  </Card>

  <Card title="Backends" icon="plug" href="/oss/javascript/deepagents/backends">
    Choose and configure pluggable filesystem backends
  </Card>

  <Card title="Interpreters" icon="code" href="/oss/javascript/deepagents/interpreters">
    Compose tools and transform data in QuickJS
  </Card>

  <Card title="Permissions" icon="lock" href="/oss/javascript/deepagents/permissions">
    Control filesystem access with permission rules
  </Card>

  <Card title="Human-in-the-loop" icon="user-check" href="/oss/javascript/deepagents/human-in-the-loop">
    Configure approval for sensitive operations
  </Card>

  <Card title="Code" icon="terminal" href="/oss/javascript/deepagents/code/overview">
    Use Deep Agents Code
  </Card>

  <Card title="Reference" icon="external-link" href="https://reference.langchain.com/javascript/modules/deepagents.html">
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
Source: https://docs.langchain.com/oss/javascript/deepagents/permissions

Control filesystem access with declarative permission rules for Deep Agents

Control which files and directories an agent can read or write to using declarative permission rules. Pass a list of rules to `permissions=` and the agent's built-in filesystem tools respect them.

<Note>
  Permissions require `deepagents>=1.9.1`.
</Note>

Permissions only apply to the built-in filesystem tools (`ls`, `read_file`, `glob`, `grep`, `write_file`, `edit_file`). Custom tools and MCP tools that access the filesystem are not covered. Permissions also do not apply to [sandbox backends](/oss/javascript/deepagents/sandboxes), which support arbitrary command execution via the `execute` tool.

<Tip>
  Use `permissions` when you need **path-based allow/deny rules** on the built-in filesystem tools. Use [backend policy hooks](/oss/javascript/deepagents/backends#add-policy-hooks) when you need custom validation logic (rate limiting, audit logging, content inspection) or need to control custom tools.
</Tip>

## Basic usage

Pass a list of `FilesystemPermission` rules to `createDeepAgent`. Rules are evaluated in declaration order. The first matching rule wins. If no rule matches, the operation is allowed.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const agent = createDeepAgent({
  model,
  backend,
  permissions: [
    {
      operations: ["write"],
      paths: ["/**"],
      mode: "deny",
    },
  ],
});
if (!agent) throw new Error("basic: agent not created");
```

## Rule structure

Each `FilesystemPermission` has three fields:

| Field        | Type                    | Description                                                                                                                          |
| ------------ | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `operations` | `("read" \| "write")[]` | Operations this rule applies to. `"read"` covers `ls`, `read_file`, `glob`, `grep`. `"write"` covers `write_file`, `edit_file`.      |
| `paths`      | `string[]`              | Glob patterns for matching file paths (e.g., `["/workspace/**"]`). Supports `**` for recursive matching and `{a,b}` for alternation. |
| `mode`       | `"allow" \| "deny"`     | Whether to allow or deny matching operations. Defaults to `"allow"`.                                                                 |

Rules use first-match-wins evaluation: the first rule whose `operations` and `paths` match the current call determines the outcome. If no rule matches, the call is **allowed** (permissive default).

Paths must be absolute (start with `/`) and cannot contain `..` or `~`. Invalid paths throw at agent construction time.

## Examples

### Isolate to a workspace directory

Allow reads and writes only under `/workspace/` and deny everything else:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const agent = createDeepAgent({
  model,
  backend,
  permissions: [
    {
      operations: ["read", "write"],
      paths: ["/workspace/**"],
      mode: "allow",
    },
    {
      operations: ["read", "write"],
      paths: ["/**"],
      mode: "deny",
    },
  ],
});
if (!agent) throw new Error("isolate-workspace: agent not created");
```

### Protect specific files

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const agent = createDeepAgent({
  model,
  backend,
  permissions: [
    {
      operations: ["read", "write"],
      paths: ["/workspace/.env", "/workspace/examples/**"],
      mode: "deny",
    },
    {
      operations: ["read", "write"],
      paths: ["/workspace/**"],
      mode: "allow",
    },
    {
      operations: ["read", "write"],
      paths: ["/**"],
      mode: "deny",
    },
  ],
});
if (!agent) throw new Error("protect-files: agent not created");
```

### Read-only memory

Allow the agent to read memory files but prevent it from modifying them. This is useful for organization-wide policies or shared knowledge bases that should only be updated by application code. See [read-only vs writable memory](/oss/javascript/deepagents/memory#read-only-vs-writable-memory) for more context.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const store = new InMemoryStore();
const agent = createDeepAgent({
  model,
  backend: new CompositeBackend(new StateBackend(), {
    "/memories/": new StoreBackend({
      namespace: (rt) => [rt.serverInfo.user.identity],
    }),
    "/policies/": new StoreBackend({
      namespace: (rt) => [rt.context.orgId],
    }),
  }),
  permissions: [
    {
      operations: ["write"],
      paths: ["/memories/**", "/policies/**"],
      mode: "deny",
    },
  ],
  store,
});
if (!agent) throw new Error("read-only-memory: agent not created");
```

### Deny all access

Block all reads and writes. This is a restrictive baseline you can layer more specific allow rules on top of:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const agent = createDeepAgent({
  model,
  backend,
  permissions: [
    {
      operations: ["read", "write"],
      paths: ["/**"],
      mode: "deny",
    },
  ],
});
if (!agent) throw new Error("deny-all: agent not created");
```

### Rule ordering

Because of first-match-wins, rule order matters. Place more specific rules before broader ones:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const correctPermissions: FilesystemPermission[] = [
  { operations: ["read", "write"], paths: ["/workspace/.env"], mode: "deny" },
  {
    operations: ["read", "write"],
    paths: ["/workspace/**"],
    mode: "allow",
  },
  { operations: ["read", "write"], paths: ["/**"], mode: "deny" },
];

const incorrectPermissions: FilesystemPermission[] = [
  {
    operations: ["read", "write"],
    paths: ["/workspace/**"],
    mode: "allow",
  },
  {
    operations: ["read", "write"],
    paths: ["/workspace/.env"],
    mode: "deny",
  },
  { operations: ["read", "write"], paths: ["/**"], mode: "deny" },
];
```

## Subagent permissions

[Subagents](/oss/javascript/deepagents/subagents) inherit the parent agent's permissions by default. To give a subagent different permissions, set the `permissions` field in its spec. This **replaces** the parent's rules entirely.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const agent = createDeepAgent({
  model,
  backend,
  permissions: [
    {
      operations: ["read", "write"],
      paths: ["/workspace/**"],
      mode: "allow",
    },
    { operations: ["read", "write"], paths: ["/**"], mode: "deny" },
  ],
  subagents: [
    {
      name: "auditor",
      description: "Read-only code reviewer",
      systemPrompt: "Review the code for issues.",
      permissions: [
        { operations: ["write"], paths: ["/**"], mode: "deny" },
        { operations: ["read"], paths: ["/workspace/**"], mode: "allow" },
        { operations: ["read"], paths: ["/**"], mode: "deny" },
      ],
    },
  ],
});
if (!agent) throw new Error("subagent: agent not created");
```

To explicitly grant a subagent unrestricted access, set `permissions: []`. An empty array overrides the parent rules with no restrictions. Omitting `permissions` inherits from the parent.

## Composite backends

When using a `CompositeBackend` with a sandbox default, every permission path must be scoped under a known route prefix. Sandboxes support arbitrary command execution, so path-based restrictions alone cannot prevent filesystem access through shell commands. Scoping permissions to route-specific [backends](/oss/javascript/deepagents/backends) avoids this conflict.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const sandbox = new StateBackend();
const memoriesBackend = new StateBackend();
const composite = new CompositeBackend(sandbox, {
  "/memories/": memoriesBackend,
});
const agent = createDeepAgent({
  model,
  backend: composite,
  permissions: [
    { operations: ["write"], paths: ["/memories/**"], mode: "deny" },
  ],
});
if (!agent) throw new Error("composite-backend: agent not created");
```

Permissions that include paths outside any route throw at construction time:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const sandbox = new StateBackend();
const memoriesBackend = new StateBackend();
const composite = new CompositeBackend(sandbox, {
  "/memories/": memoriesBackend,
});

createDeepAgent({
  model,
  backend: composite,
  permissions: [
    { operations: ["write"], paths: ["/workspace/**"], mode: "deny" },
  ],
});

createDeepAgent({
  model,
  backend: composite,
  permissions: [{ operations: ["read"], paths: ["/**"], mode: "deny" }],
});
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

# Profiles
Source: https://docs.langchain.com/oss/javascript/deepagents/profiles

Package per-provider and per-model defaults that Deep Agents applies when a model is selected

**Harness profiles** let you package configuration that Deep Agents applies whenever a given provider or specific model is selected: system-prompt tweaks, tool description overrides, excluded tools or middleware, extra middleware, and general-purpose subagent edits. They are the main way to tune how the harness behaves for a particular model without changing your `create_deep_agent` call site. Use `HarnessProfile` when building profiles in Python; use `HarnessProfileConfig` when [loading or saving YAML/JSON files](#load-profiles-from-config-files). Deep Agents ships built-in harness profiles for OpenAI and Anthropic (Claude) models.

**Provider profiles** are a narrower companion API for *model-construction* kwargs, which don't affect the harness. Most callers don't need them; reach for one when you want `init_chat_model` defaults, credential checks, or runtime-derived kwargs as defaults with your provider choice (for example, when packaging a provider integration).

## Harness profiles

A `HarnessProfile` describes prompt-assembly, tool-visibility, middleware, and default-subagent adjustments that `create_deep_agent` applies after the chat model has been constructed:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import (
    GeneralPurposeSubagentProfile,
    HarnessProfile,
    register_harness_profile,
)

register_harness_profile(
    "openai:gpt-5.5",
    HarnessProfile(
        system_prompt_suffix="Respond in under 100 words.",
        excluded_tools={"execute"},
        excluded_middleware={"SummarizationMiddleware"},
        general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False),
    ),
)
```

<ResponseField name="base_system_prompt" type="string">
  Replace the base Deep Agents system prompt (`CUSTOM` in [Prompt assembly](/oss/javascript/deepagents/customization#prompt-assembly)).
</ResponseField>

<ResponseField name="system_prompt_suffix" type="string">
  Append text to the assembled base prompt (`SUFFIX` in [Prompt assembly](/oss/javascript/deepagents/customization#prompt-assembly)); applied to the main agent, declarative subagents, and the auto-added general-purpose subagent.
</ResponseField>

<ResponseField name="tool_description_overrides" type="Mapping[str, str]">
  Override individual tool descriptions, keyed by tool name.
</ResponseField>

<ResponseField name="excluded_tools" type="frozenset[str]">
  Remove specific harness-level tools from the tool set. Matched by tool name (string), applied as a post-injection filter so it can drop both user-supplied tools and tools added by harness middleware. See [Running without the default filesystem tools](/oss/javascript/deepagents/harness#virtual-filesystem-access) for a worked example.
</ResponseField>

<ResponseField name="excluded_middleware" type="frozenset[type[AgentMiddleware] | str]">
  Strip specific middleware classes from the [default stack](/oss/javascript/deepagents/customization#default-stack-main-agent). Accepts middleware classes or string names.
</ResponseField>

<ResponseField name="extra_middleware" type="Sequence[AgentMiddleware] | Callable[[], Sequence[AgentMiddleware]]">
  Append middleware to every stack this profile applies to. See the [default middleware stack](/oss/javascript/deepagents/customization#middleware) for the built-in ordering.
</ResponseField>

<ResponseField name="general_purpose_subagent" type="GeneralPurposeSubagentProfile">
  Disable, rename, or re-prompt the general-purpose subagent. When this field's `system_prompt` is set alongside `base_system_prompt`, the general-purpose-specific subagent prompt wins—see [General-purpose subagent prompt](/oss/javascript/deepagents/customization#general-purpose-subagent-prompt).
</ResponseField>

<Note>
  Caller-supplied `system_prompt=` always sits at the front of the assembled prompt, and `system_prompt_suffix` always sits at the end—regardless of which model is selected. The same overlay rules apply to subagents: each subagent re-runs profile resolution against its own model. See [Prompt assembly](/oss/javascript/deepagents/customization#prompt-assembly) for the full per-case breakdown (main agent, subagents, and the general-purpose subagent).
</Note>

<Warning>
  To run an agent without the `task` tool, see [Running without subagents](/oss/javascript/deepagents/subagents#running-without-subagents) — set `general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False)` and pass no synchronous subagents via `subagents=`. `SubAgentMiddleware` (and the `task` tool) is only attached when at least one synchronous subagent exists, so this configuration leaves it out cleanly. Async subagents are unaffected.

  Listing `FilesystemMiddleware`, `SubAgentMiddleware`, or the internal permission middleware in `excluded_middleware` raises a `ValueError` — they're required scaffolding in the [default middleware stack](/oss/javascript/deepagents/customization#default-stack-main-agent). To hide their tools from the model without removing the middleware, use `excluded_tools` instead — see [Running without the default filesystem tools](/oss/javascript/deepagents/harness#virtual-filesystem-access).
</Warning>

Entries in `excluded_middleware` accept two forms:

* A middleware *class* (matched by exact type), or a plain string that matches `AgentMiddleware.name`. Use plain strings for built-ins and public aliases such as `"SummarizationMiddleware"`.
* An `module:Class` import ref (for example, `"my_pkg.middleware:TelemetryMiddleware"`) to target an exact middleware class from a config file. Import refs resolve lazily, so use them only for trusted local configuration — loading one imports Python code.

<Accordion title="Lookup order for preconfigured model instances">
  When you pass a preconfigured chat model instance instead of a `provider:model` string, the harness synthesizes the canonical `provider:identifier` key from the instance and looks it up in this order:

  1. Exact `provider:identifier` match
  2. Identifier-only (only when the identifier already contains `:`)
  3. Provider-only fallback
</Accordion>

## Registration keys

Both profile types use the same key format:

* **Provider-level** — a bare provider name like `"openai"` applies to every model from that provider.
* **Model-level** — a fully qualified `provider:model` key like `"openai:gpt-5.5"` applies only to that specific model.

When both a provider-level and a model-level profile exist, they are merged at resolution time. Unset model-level fields inherit from the provider-level profile; explicit model-level values override them.

Re-registering under an existing key merges the new profile on top of the prior one—it does not replace it. See [Merge semantics](#merge-semantics) for the per-field rules.

<Note>
  There is no wildcard key that matches every provider. To apply the same overrides everywhere—say, dropping `TodoListMiddleware` regardless of which model is selected—register the profile under each provider key you use. Profiles are intended for adjustments that depend on the model being selected. Global adjustments that should apply regardless of model should be made on the `create_deep_agent` call site.
</Note>

## Merge semantics

| Field                                        | Merge behavior                                                                                 |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `base_system_prompt`, `system_prompt_suffix` | New value wins when set; otherwise inherits                                                    |
| `tool_description_overrides`                 | Mappings merge per key; new value wins on a shared key                                         |
| `excluded_tools`, `excluded_middleware`      | Set union                                                                                      |
| `extra_middleware`                           | Merged by concrete class: new instance replaces existing at its position, novel classes append |
| `general_purpose_subagent`                   | Merged field-wise (unset fields inherit)                                                       |
| `init_kwargs` (provider)                     | Dicts merge key-wise; new value wins on a shared key                                           |
| `pre_init` (provider)                        | Callables chain: existing runs first, then the new one                                         |
| `init_kwargs_factory` (provider)             | Factories chain with their outputs merged every `resolve_model` call                           |

## Provider profiles

A `ProviderProfile` declares how Deep Agents should construct a chat model for a given provider or specific model spec. It applies only when you provide a `provider:model` string when creating the deep agent, not when you pass a preconfigured model with [`init_chat_model`](https://reference.langchain.com/javascript/langchain/chat_models/universal/initChatModel):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import ProviderProfile, register_provider_profile

register_provider_profile(
    "openai",
    ProviderProfile(init_kwargs={"temperature": 0}),
)
```

<ResponseField name="init_kwargs" type="Mapping[str, Any]">
  Static initialization arguments forwarded to `init_chat_model`.
</ResponseField>

<ResponseField name="pre_init" type="Callable[[str], None]">
  Side effects to run before construction (for example, credential validation).
</ResponseField>

<ResponseField name="init_kwargs_factory" type="Callable[[], dict[str, Any]]">
  Kwargs derived from runtime state (for example, headers pulled from environment variables).
</ResponseField>

## Load profiles from config files

For YAML/JSON-backed workflows, use `HarnessProfileConfig`. It mirrors the declarative subset of `HarnessProfile` (prompt text, tool-description overrides, excluded tools and middleware, general-purpose subagent edits) and owns `to_dict` / `from_dict`. Runtime-only state — middleware instances, factories, and class-form `excluded_middleware` entries — stays on `HarnessProfile`.

`register_harness_profile` accepts either type, so config-backed callers don't need a manual conversion step:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
