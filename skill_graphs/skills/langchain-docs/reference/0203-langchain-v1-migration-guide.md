# LangChain v1 migration guide
Source: https://docs.langchain.com/oss/javascript/migrate/langchain-v1

This migration guide outlines the major changes in LangChain v1. To learn more about the new features of v1, see the [introductory post](/oss/javascript/releases/langchain-v1).

To upgrade,

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langchain@latest @langchain/core@latest
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm install langchain@latest @langchain/core@latest
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add langchain@latest @langchain/core@latest
  ```

  ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  bun add langchain@latest @langchain/core@latest
  ```
</CodeGroup>

## `createAgent`

In v1, the react agent prebuilt is now in the langchain package. The table below outlines what functionality has changed:

| Section                                            | What changed                                                                             |
| -------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [Import path](#import-path)                        | Package moved from `@langchain/langgraph/prebuilts` to `langchain`                       |
| [Prompts](#prompts)                                | Parameter renamed to `systemPrompt`, dynamic prompts use middleware                      |
| [Pre-model hook](#pre-model-hook)                  | Replaced by middleware with `beforeModel` method                                         |
| [Post-model hook](#post-model-hook)                | Replaced by middleware with `afterModel` method                                          |
| [Custom state](#custom-state)                      | Defined in middleware, zod objects only                                                  |
| [Model](#model)                                    | Dynamic selection via middleware, pre-bound models not supported                         |
| [Tools](#tools)                                    | Tool error handling moved to middleware with `wrapToolCall`                              |
| [Structured output](#structured-output)            | prompted output removed, use `toolStrategy`/`providerStrategy`                           |
| [Streaming node name](#streaming-node-name-rename) | Node name changed from `"agent"` to `"model"`                                            |
| [Runtime context](#runtime-context)                | `context` property instead of `config.configurable`                                      |
| [Namespace](#simplified-package)                   | Streamlined to focus on agent building blocks, legacy code moved to `@langchain/classic` |

### Import path

The import path for the react agent prebuilt has changed from `@langchain/langgraph/prebuilts` to `langchain`. The name of the function has changed from `createReactAgent` to `createAgent`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createReactAgent } from "@langchain/langgraph/prebuilts"; // [!code --]
import { createAgent } from "langchain"; // [!code ++]
```

### Prompts

#### Static prompt rename

The `prompt` parameter has been renamed to `systemPrompt`:

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent } from "langchain";

  agent = createAgent({
    model,
    tools,
    systemPrompt: "You are a helpful assistant.", // [!code highlight]
  });
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createReactAgent } from "@langchain/langgraph/prebuilts";

  const agent = createReactAgent({
    model,
    tools,
    prompt: "You are a helpful assistant.", // [!code highlight]
  });
  ```
</CodeGroup>

#### `SystemMessage`

If using `SystemMessage` objects in the system prompt, the string content is now used directly:

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { SystemMessage, createAgent } from "langchain";

  const agent = createAgent({
    model,
    tools,
    systemPrompt: "You are a helpful assistant.", // [!code highlight]
  });
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createReactAgent } from "@langchain/langgraph/prebuilts";

  const agent = createReactAgent({
    model,
    tools,
    prompt: new SystemMessage(content: "You are a helpful assistant."), // [!code highlight]
  });
  ```
</CodeGroup>

#### Dynamic prompts

Dynamic prompts are a core context engineering pattern—they adapt what you tell the model based on the current conversation state. To do this, use `dynamicSystemPromptMiddleware`:

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, dynamicSystemPromptMiddleware } from "langchain";
  import * as z from "zod";

  const contextSchema = z.object({
    userRole: z.enum(["expert", "beginner"]).default("beginner"),
  });

  const userRolePrompt = dynamicSystemPromptMiddleware<z.infer<typeof contextSchema>>( // [!code highlight]
      (_state, runtime) => {
          const userRole = runtime.context.userRole;
          const basePrompt = "You are a helpful assistant.";

          if (userRole === "expert") {
              return `${basePrompt} Provide detailed technical responses.`;
          } else if (userRole === "beginner") {
              return `${basePrompt} Explain concepts simply and avoid jargon.`;
          }
          return basePrompt; // [!code highlight]
      }
  );

  const agent = createAgent({
    model,
    tools,
    middleware: [userRolePrompt],
    contextSchema,
  });

  await agent.invoke(
    {
      messages: [new HumanMessage("Explain async programming")],
    },
    {
      context: {
        userRole: "expert",
      },
    }
  );
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createReactAgent } from "@langchain/langgraph/prebuilts";

  const contextSchema = z.object({
    userRole: z.enum(["expert", "beginner"]),
  });

  const agent = createReactAgent({
    model,
    tools,
    prompt: (state) => {
      const userRole = state.context.userRole;
      const basePrompt = "You are a helpful assistant.";

      if (userRole === "expert") {
        return `${basePrompt} Provide detailed technical responses.`;
      } else if (userRole === "beginner") {
        return `${basePrompt} Explain concepts simply and avoid jargon.`;
      }
      return basePrompt;
    },
    contextSchema,
  });

  // Use with context via config.configurable
  await agent.invoke(
    {
      messages: [new HumanMessage("Explain async programming")],
    },
    {
      config: {
        configurable: { userRole: "expert" },
      },
    }
  );
  ```
</CodeGroup>

### Pre-model hook

Pre-model hooks are now implemented as middleware with the `beforeModel` method. This pattern is more extensible--you can define multiple middlewares to run before the model is called and reuse them across agents.

Common use cases include:

* Summarizing conversation history
* Trimming messages
* Input guardrails, like PII redaction

v1 includes built-in summarization middleware:

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, summarizationMiddleware } from "langchain";

  const agent = createAgent({
    model: "claude-sonnet-4-6",
    tools,
    middleware: [
      summarizationMiddleware({
        model: "claude-sonnet-4-6",
        trigger: { tokens: 1000 },
      }),
    ],
  });
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createReactAgent } from "@langchain/langgraph/prebuilts";

  function customSummarization(state) {
    // Custom logic for message summarization
  }

  const agent = createReactAgent({
    model: "claude-sonnet-4-6",
    tools,
    preModelHook: customSummarization,
  });
  ```
</CodeGroup>

### Post-model hook

Post-model hooks are now implemented as middleware with the `afterModel` method. This lets you compose multiple handlers after the model responds.

Common use cases include:

* Human-in-the-loop approval
* Output guardrails

v1 includes a built-in human-in-the-loop middleware:

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, humanInTheLoopMiddleware } from "langchain";

  const agent = createAgent({
    model: "claude-sonnet-4-6",
    tools: [readEmail, sendEmail],
    middleware: [
      humanInTheLoopMiddleware({
        interruptOn: {
          sendEmail: { allowedDecisions: ["approve", "edit", "reject"] },
        },
      }),
    ],
  });
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createReactAgent } from "@langchain/langgraph/prebuilts";

  function customHumanInTheLoopHook(state) {
    // Custom approval logic
  }

  const agent = createReactAgent({
    model: "claude-sonnet-4-6",
    tools: [readEmail, sendEmail],
    postModelHook: customHumanInTheLoopHook,
  });
  ```
</CodeGroup>

### Custom state

Custom state is now defined in middleware using the `stateSchema` property. Use Zod to declare additional state fields that are carried through the agent run.

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { createAgent, createMiddleware, tool } from "langchain";

  const UserState = z.object({
    userName: z.string(),
  });

  const userState = createMiddleware({
    name: "UserState",
    stateSchema: UserState,
    beforeModel: (state) => {
      // Access custom state properties
      const name = state.userName;
      // Optionally modify messages/system prompt based on state
      return;
    },
  });

  const greet = tool(
    async () => {
      return "Hello!";
    },
    {
      name: "greet",
      description: "Greet the user",
      schema: z.object({}),
    }
  );

  const agent = createAgent({
    model: "claude-sonnet-4-6",
    tools: [greet],
    middleware: [userState],
  });

  await agent.invoke({
    messages: [{ role: "user", content: "Hi" }],
    userName: "Ada",
  });
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { getCurrentTaskInput } from "@langchain/langgraph";
  import { createReactAgent } from "@langchain/langgraph/prebuilts";
  import * as z from "zod";

  const UserState = z.object({
    userName: z.string(),
  });

  const greet = tool(
    async () => {
      const state = await getCurrentTaskInput();
      const userName = state.userName;
      return `Hello ${userName}!`;
    },
  );

  // Custom state was provided via agent-level state schema or accessed ad hoc in hooks
  const agent = createReactAgent({
    model: "claude-sonnet-4-6",
    tools: [greet],
    stateSchema: UserState,
  });
  ```
</CodeGroup>

### Model

Dynamic model selection now happens via middleware. Use `wrapModelCall` to swap models (and tools) based on state or runtime context. In `createReactAgent`, this was done via a function passed to the `model` parameter.

This functionality has been ported to the middleware interface in v1.

#### Dynamic model selection

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, createMiddleware } from "langchain";

  const dynamicModel = createMiddleware({
    name: "DynamicModel",
    wrapModelCall: (request, handler) => {
      const messageCount = request.state.messages.length;
      const model = messageCount > 10 ? "openai:gpt-5.5" : "openai:gpt-5-nano";
      return handler({ ...request, model });
    },
  });

  const agent = createAgent({
    model: "gpt-5-nano",
    tools,
    middleware: [dynamicModel],
  });
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createReactAgent } from "@langchain/langgraph/prebuilts";

  function selectModel(state) {
    return state.messages.length > 10 ? "openai:gpt-5.5" : "openai:gpt-5-nano";
  }

  const agent = createReactAgent({
    model: selectModel,
    tools,
  });
  ```
</CodeGroup>

#### Pre-bound models

To better support structured output, `createAgent` should receive a plain model (string or instance) and a separate `tools` list. Avoid passing models pre-bound with tools when using structured output.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// No longer supported
// const modelWithTools = new ChatOpenAI({ model: "gpt-5.4-mini" }).bindTools([someTool]);
// const agent = createAgent({ model: modelWithTools, tools: [] });

// Use instead
const agent = createAgent({ model: "gpt-5.4-mini", tools: [someTool] });
```

### Tools

The `tools` argument to `createAgent` accepts:

* Functions created with `tool`
* LangChain tool instances
* Objects that represent built-in provider tools

#### Handling tool errors

You can now configure the handling of tool errors with middleware implementing the `wrapToolCall` method.

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, createMiddleware, ToolMessage } from "langchain";

  const handleToolErrors = createMiddleware({
    name: "HandleToolErrors",
    wrapToolCall: async (request, handler) => {
      try {
        return await handler(request);
      } catch (error) {
        // Only handle errors that occur during tool execution due to invalid inputs
        // that pass schema validation but fail at runtime (e.g., invalid SQL syntax).
        // Do NOT handle:
        // - Network failures (use tool retry middleware instead)
        // - Incorrect tool implementation errors (should bubble up)
        // - Schema mismatch errors (already auto-handled by the framework)
        //
        // Return a custom error message to the model
        return new ToolMessage({
          content: `Tool error: Please check your input and try again. (${error})`,
          tool_call_id: request.toolCall.id!,
        });
      }
    },
  });

  const agent = createAgent({
    model: "claude-sonnet-4-6",
    tools: [checkWeather, searchWeb],
    middleware: [handleToolErrors],
  });
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createReactAgent, ToolNode } from "@langchain/langgraph/prebuilts";

  const agent = createReactAgent({
    model: "claude-sonnet-4-6",
    tools: new ToolNode(
      [checkWeather, searchWeb],
      { handleToolErrors: true } // [!code highlight]
    ),
  });
  ```
</CodeGroup>

### Structured output

#### Node changes

Structured output used to be generated in a separate node from the main agent. This is no longer the case. Structured output is generated in the main loop (no extra LLM call), reducing cost and latency.

#### Tool and provider strategies

In v1, there are two strategies:

* `toolStrategy` uses artificial tool calling to generate structured output
* `providerStrategy` uses provider-native structured output generation

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, toolStrategy } from "langchain";
  import * as z from "zod";

  const OutputSchema = z.object({
    summary: z.string(),
    sentiment: z.string(),
  });

  const agent = createAgent({
    model: "gpt-5.4-mini",
    tools,
    // explicitly using tool strategy
    responseFormat: toolStrategy(OutputSchema), // [!code highlight]
  });
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createReactAgent } from "@langchain/langgraph/prebuilts";
  import * as z from "zod";

  const OutputSchema = z.object({
    summary: z.string(),
    sentiment: z.string(),
  });

  const agent = createReactAgent({
    model: "gpt-5.4-mini",
    tools,
    // Structured output was driven primarily via tool-calling with fewer options
    responseFormat: OutputSchema,
  });
  ```
</CodeGroup>

#### Prompted output removed

Prompted output via custom instructions in `responseFormat` is removed in favor of the above strategies.

### Streaming node name rename

When streaming events from agents, the node name was changed from `"agent"` to `"model"` to better reflect the node's purpose.

### Runtime context

When invoking an agent, pass static, read-only configuration via the `context` config argument. This replaces patterns that used `config.configurable`.

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, HumanMessage } from "langchain";
  import * as z from "zod";

  const agent = createAgent({
    model: "gpt-5.5",
    tools,
    contextSchema: z.object({ userId: z.string(), sessionId: z.string() }),
  });

  const result = await agent.invoke(
    { messages: [new HumanMessage("Hello")] },
    { context: { userId: "123", sessionId: "abc" } }, // [!code highlight]
  );
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createReactAgent, HumanMessage } from "@langchain/langgraph/prebuilts";

  const agent = createReactAgent({ model, tools });

  // Pass context via config.configurable
  const result = await agent.invoke(
    { messages: [new HumanMessage("Hello")] },
    {
      config: { // [!code highlight]
        configurable: { userId: "123", sessionId: "abc" }, // [!code highlight]
      }, // [!code highlight]
    }
  );
  ```
</CodeGroup>

<Note>
  The old `config.configurable` pattern still works for backward compatibility, but using the new `context` parameter is recommended for new applications or applications migrating to v1.
</Note>

***

## Standard content

In v1, messages gain provider-agnostic standard content blocks. Access them via `message.contentBlocks` for a consistent, typed view across providers. The existing `message.content` field remains unchanged for strings or provider-native structures.

### What changed

* New `contentBlocks` property on messages for normalized content.
* New TypeScript types under `ContentBlock` for strong typing.
* Optional serialization of standard blocks into `content` via `LC_OUTPUT_VERSION=v1` or `outputVersion: "v1"`.

### Read standardized content

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { initChatModel } from "langchain";

  const model = await initChatModel("gpt-5-nano");
  const response = await model.invoke("Explain AI");

  for (const block of response.contentBlocks) {
    if (block.type === "reasoning") {
      console.log(block.reasoning);
    } else if (block.type === "text") {
      console.log(block.text);
    }
  }
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Provider-native formats vary; you needed per-provider handling.
  const response = await model.invoke("Explain AI");
  for (const item of response.content as any[]) {
    if (item.type === "reasoning") {
      // OpenAI-style reasoning
    } else if (item.type === "thinking") {
      // Anthropic-style thinking
    } else if (item.type === "text") {
      // Text
    }
  }
  ```
</CodeGroup>

### Create multimodal messages

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { HumanMessage } from "langchain";

  const message = new HumanMessage({
    contentBlocks: [
      { type: "text", text: "Describe this image." },
      { type: "image", url: "https://example.com/image.jpg" },
    ],
  });
  const res = await model.invoke([message]);
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { HumanMessage } from "langchain";

  const message = new HumanMessage({
    // Provider-native structure
    content: [
      { type: "text", text: "Describe this image." },
      { type: "image_url", image_url: { url: "https://example.com/image.jpg" } },
    ],
  });
  const res = await model.invoke([message]);
  ```
</CodeGroup>

### Example block types

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ContentBlock } from "langchain";

const textBlock: ContentBlock.Text = {
  type: "text",
  text: "Hello world",
};

const imageBlock: ContentBlock.Multimodal.Image = {
  type: "image",
  url: "https://example.com/image.png",
  mimeType: "image/png",
};
```

See the content blocks [reference](/oss/javascript/langchain/messages#content-block-reference) for more details.

### Serialize standard content

Standard content blocks are **not serialized** into the `content` attribute by default. If you need to access standard content blocks in the `content` attribute (e.g., when sending messages to a client), you can opt-in to serializing them into `content`.

<CodeGroup>
  ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  export LC_OUTPUT_VERSION=v1
  ```

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { initChatModel } from "langchain";

  const model = await initChatModel("gpt-5-nano", {
    outputVersion: "v1",
  });
  ```
</CodeGroup>

<Note>
  Learn more: [Messages](/oss/javascript/langchain/messages#message-content) and [Standard content blocks](/oss/javascript/langchain/messages#standard-content-blocks). See [Multimodal](/oss/javascript/langchain/messages#multimodal) for input examples.
</Note>

***

## Simplified package

The `langchain` package namespace is streamlined to focus on agent building blocks. Legacy functionality has moved to `@langchain/classic`. The new package exposes only the most useful and relevant functionality.

### Exports

The v1 package includes:

| Module      | What's available                              | Notes                              |
| ----------- | --------------------------------------------- | ---------------------------------- |
| Agents      | `createAgent`, `AgentState`                   | Core agent creation functionality  |
| Messages    | Message types, content blocks, `trimMessages` | Re-exported from `@langchain/core` |
| Tools       | `tool`, tool classes                          | Re-exported from `@langchain/core` |
| Chat models | `initChatModel`, `BaseChatModel`              | Unified model initialization       |

### `@langchain/classic`

If you use legacy chains, the indexing API, or functionality previously re-exported from `@langchain/community`, install `@langchain/classic` and update imports:

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/classic
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm install @langchain/classic
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/classic
  ```

  ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  bun add @langchain/classic
  ```
</CodeGroup>

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// v1 (new)
import { ... } from "@langchain/classic";
import { ... } from "@langchain/classic/chains";

// v0 (old)
import { ... } from "langchain";
import { ... } from "langchain/chains";
```

***

## Breaking changes

### Dropped Node 18 support

All LangChain packages now require **Node.js 20 or higher**. Node.js 18 reached [end of life](https://nodejs.org/en/about/releases/) in March 2025.

### New build outputs

Builds for all langchain packages now use a bundler based approach instead of using raw typescript outputs. If you were importing files from the `dist/` directory (which is not recommended), you will need to update your imports to use the new module system.

### Legacy code moved to `@langchain/classic`

Legacy functionality outside the focus of standard interfaces and agents has been moved to the [`@langchain/classic`](https://www.npmjs.com/package/@langchain/classic) package. See the [Simplified package](#simplified-package) section for details on what's available in the core `langchain` package and what moved to `@langchain/classic`.

### Removal of deprecated APIs

Methods, functions, and other objects that were already deprecated and slated for removal in 1.0 have been deleted.

<Accordion title="View removed deprecated APIs">
  The following deprecated APIs have been removed in v1:

  #### Core functionality

  * `TraceGroup` - Use LangSmith tracing instead
  * `BaseDocumentLoader.loadAndSplit` - Use `.load()` followed by a text splitter
  * `RemoteRunnable` - No longer supported

  #### Prompts

  * `BasePromptTemplate.serialize` and `.deserialize` - Use JSON serialization directly
  * `ChatPromptTemplate.fromPromptMessages` - Use `ChatPromptTemplate.fromMessages`

  #### Retrievers

  * `BaseRetrieverInterface.getRelevantDocuments` - Use `.invoke()` instead

  #### Runnables

  * `Runnable.bind` - Use `.bindTools()` or other specific binding methods
  * `Runnable.map` - Use `.batch()` instead
  * `RunnableBatchOptions.maxConcurrency` - Use `maxConcurrency` in the config object

  #### Chat models

  * `BaseChatModel.predictMessages` - Use `.invoke()` instead
  * `BaseChatModel.predict` - Use `.invoke()` instead
  * `BaseChatModel.serialize` - Use JSON serialization directly
  * `BaseChatModel.callPrompt` - Use `.invoke()` instead
  * `BaseChatModel.call` - Use `.invoke()` instead

  #### LLMs

  * `BaseLLMParams.concurrency` - Use `maxConcurrency` in the config object
  * `BaseLLM.call` - Use `.invoke()` instead
  * `BaseLLM.predict` - Use `.invoke()` instead
  * `BaseLLM.predictMessages` - Use `.invoke()` instead
  * `BaseLLM.serialize` - Use JSON serialization directly

  #### Streaming

  * `createChatMessageChunkEncoderStream` - Use `.stream()` method directly

  #### Tracing

  * `BaseTracer.runMap` - Use LangSmith tracing APIs
  * `getTracingCallbackHandler` - Use LangSmith tracing
  * `getTracingV2CallbackHandler` - Use LangSmith tracing
  * `LangChainTracerV1` - Use LangSmith tracing

  #### Memory and storage

  * `BaseListChatMessageHistory.addAIChatMessage` - Use `.addMessage()` with `AIMessage`
  * `BaseStoreInterface` - Use specific store implementations

  #### Utilities

  * `getRuntimeEnvironmentSync` - Use async `getRuntimeEnvironment()`
</Accordion>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/migrate/langchain-v1.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangGraph v1 migration guide
Source: https://docs.langchain.com/oss/javascript/migrate/langgraph-v1

This guide outlines changes in LangGraph v1 and how to migrate from previous versions. For a high-level overview of what's new, see the [release notes](/oss/javascript/releases/langgraph-v1).

To upgrade,

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/langgraph@latest @langchain/core@latest
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/langgraph@latest @langchain/core@latest
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/langgraph@latest @langchain/core@latest
  ```

  ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  bun add @langchain/langgraph@latest @langchain/core@latest
  ```
</CodeGroup>

## Summary of changes

| Area                             | What changed                                               |
| -------------------------------- | ---------------------------------------------------------- |
| React prebuilt                   | `createReactAgent` deprecated; use LangChain `createAgent` |
| Interrupts                       | Typed interrupts supported via `interrupts` config         |
| `toLangGraphEventStream` removed | Use `graph.stream` with the desired `encoding` format      |
| `useStream`                      | Supports custom transports                                 |

***

## Deprecation: `createReactAgent` → `createAgent`

LangGraph v1 deprecates the `createReactAgent` prebuilt. Use LangChain's `createAgent`, which runs on LangGraph and adds a flexible middleware system.

See the LangChain v1 docs for details:

* [Release notes](/oss/javascript/releases/langchain-v1#createagent)
* [Migration guide](/oss/javascript/migrate/langchain-v1#createagent)

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent } from "langchain";

  const agent = createAgent({
    model,
    tools,
    systemPrompt: "You are a helpful assistant.", // [!code highlight]
  });
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createReactAgent } from "@langchain/langgraph/prebuilts";

  const agent = createReactAgent({
    model,
    tools,
    prompt: "You are a helpful assistant.", // [!code highlight]
  });
  ```
</CodeGroup>

***

## Typed interrupts

You can now define interrupt types at graph construction to strictly type the values passed to and received from interrupts.

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { StateGraph, interrupt } from "@langchain/langgraph";
  import * as z from "zod";

  const State = z.object({ foo: z.string() });

  const graphConfig = {
    interrupts: {
      approve: interrupt<{ reason: string }, { messages: string[] }>(),
    },
  }

  const graph = new StateGraph(State, graphConfig)
    .addNode("node", async (state, runtime) => {
      const value = runtime.interrupt.approve({ reason: "review" }); // [!code highlight]
      return { foo: value };
    })
    .compile();
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { StateGraph } from "@langchain/langgraph";

  const graph = new StateGraph(State)
    .addNode("node", async (state, runtime) => {
      const value = runtime.interrupt.approve({ reason: "review" }); // [!code highlight]
      return state;
    })
    .compile();
  ```
</CodeGroup>

See [Interrupts](/oss/javascript/langgraph/interrupts) to learn more.

***

## Event stream encoding

The low-level `toLangGraphEventStream` helper is removed. Streaming responses are handled by the SDK; when using low-level clients, select the wire format via an `encoding` option passed to `graph.stream`.

<CodeGroup>
  ```typescript v1 (new) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const stream = await graph.stream(input, {
    encoding: "text/event-stream",
    streamMode: ["values", "messages"],
  });

  return new Response(stream, {
    headers: { "Content-Type": "text/event-stream" }, // [!code highlight]
  });
  ```

  ```typescript v0 (old) theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  return toLangGraphEventStreamResponse({
    stream: graph.streamEvents(input, {
      version: "v2",
      streamMode: ["values", "messages"],
    }),
  });
  ```
</CodeGroup>

***

## Breaking changes

### Dropped Node 18 support

All LangGraph packages now require **Node.js 20 or higher**. Node.js 18 reached [end of life](https://nodejs.org/en/about/releases/) in March 2025.

### New build outputs

Builds for all langgraph packages now use a bundler based approach instead of using raw typescript outputs. If you were importing files from the `dist/` directory (which is not recommended), you will need to update your imports to use the new module system.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/migrate/langgraph-v1.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deep Agents
Source: https://docs.langchain.com/oss/javascript/reference/deepagents-javascript

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/deepagents-javascript.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Integrations
Source: https://docs.langchain.com/oss/javascript/reference/integrations-javascript

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/integrations-javascript.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangChain SDK
Source: https://docs.langchain.com/oss/javascript/reference/langchain-javascript

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/langchain-javascript.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangGraph SDK
Source: https://docs.langchain.com/oss/javascript/reference/langgraph-javascript

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/langgraph-javascript.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Reference
Source: https://docs.langchain.com/oss/javascript/reference/overview

Comprehensive API reference documentation for the LangChain and LangGraph Python and TypeScript libraries.

## Reference sites

<CardGroup>
  <Card title="LangChain" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=663b30f85baf99ad708b97e05da2a5a4" href="https://reference.langchain.com/javascript/langchain">
    Complete API reference for LangChain JavaScript/TypeScript, including chat models, tools, agents, and more.
  </Card>

  <Card title="LangGraph" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81" href="https://reference.langchain.com/javascript/langchain-langgraph">
    Complete API reference for LangGraph JavaScript/TypeScript, including graph APIs, state management, checkpointing, and more.
  </Card>

  <Card title="Deep Agents" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/deep-agents-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=1cc68f66a9e7550331cc0875f1ba53af" href="https://reference.langchain.com/javascript/deepagents">
    Build agents that can plan, use subagents, and leverage file systems for complex tasks
  </Card>

  <Card title="MCP Adapter" icon="plug" href="https://reference.langchain.com/javascript/langchain-mcp-adapters">
    Use Model Context Protocol (MCP) tools within LangChain and LangGraph applications.
  </Card>

  <Card title="Deep Agents" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/deep-agents-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=1cc68f66a9e7550331cc0875f1ba53af" href="https://reference.langchain.com/javascript/deepagents">
    Build agents that can plan, use subagents, and leverage file systems for complex tasks.
  </Card>
</CardGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/reference/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Release policy
Source: https://docs.langchain.com/oss/javascript/release-policy

This page explains the LangChain and LangGraph release policies. Click on the tabs below to view the release policies for each:

<Tabs>
  <Tab title="LangChain">
    The LangChain ecosystem is composed of different component packages (e.g., `@langchain/core`, `langchain`, partner packages, etc.)

    ## Release cadence

    With the release of LangChain 1.0, **minor** releases (e.g., from `1.0.x` to `1.1.0`) of `langchain` and `@langchain/core` follow semantic versioning and may be released frequently. Minor releases contain new features and improvements but do not include breaking changes.

    Patch versions are released frequently, up to a few times per week, as they contain bug fixes and minor improvements.

    ## API stability

    The development of LLM applications is a rapidly evolving field, and we are constantly learning from our users and the community. As such, we expect that the APIs in `langchain` and `@langchain/core` will continue to evolve to better serve the needs of our users.

    With LangChain 1.0's adoption of semantic versioning:

    * Breaking changes to the public API will only occur in major version releases (e.g., `2.0.0`)
    * Minor version bumps (e.g., `1.0.0` to `1.1.0`) add new features without breaking changes
    * Patch version bumps (e.g., `1.0.0` to `1.0.1`) contain bug fixes and minor improvements

    We will generally try to avoid making unnecessary changes, and will provide a deprecation policy for features that are being removed.

    ### Stability of other packages

    The stability of other packages in the LangChain ecosystem may vary:

    * **Partner packages maintained by LangChain** (such as `langchain-openai` and `langchain-anthropic`) follow semantic versioning and are expected to be stable post 1.0. Other partner packages may follow different stability and versioning policies, and users should refer to the documentation of those packages for more information.

    ## Deprecation policy

    We will generally avoid deprecating features until a better alternative is available.

    With LangChain 1.0's semantic versioning approach, deprecated features will continue to work throughout the entire 1.x release series. Breaking changes, including the removal of deprecated features, will only occur in major version releases (e.g., 2.0).

    When a feature is deprecated in `langchain` or `@langchain/core`, we will:

    * Clearly mark it as deprecated in the code and documentation
    * Provide migration guidance to the recommended alternative
    * Provide security updates for the deprecated feature through all 1.x minor releases

    In some situations, we may allow deprecated features to remain in the code base even longer if they are not causing maintenance issues, to further reduce the burden on users.

    ## Long-term support (LTS)

    LangChain follows a long-term support (LTS) policy to provide stability for production applications:

    ### Release status definitions

    Packages are marked with one of the following statuses:

    * **ACTIVE**: Current active development, includes bug fixes, security patches, and new features
    * **MAINTENANCE**: Receives all security patches and critical bug fixes, but no new features

    ### Current LTS releases

    **LangChain 1.0** is designated as an LTS release:

    * **Status**: ACTIVE until the release of 2.0
    * **Support period**: After 2.0 is released, 1.0 will enter MAINTENANCE mode for at least 1 year
    * **Semver compliance**: Users can upgrade between minor versions (e.g., 1.0 to 1.1) without breaking changes

    ### Legacy version support

    **LangChain 0.3**:

    * **Status**: MAINTENANCE mode
    * **Support period**: Until December 2026
    * **Support includes**: Security patches and critical bug fixes
  </Tab>

  <Tab title="LangGraph">
    LangGraph follows a structured release policy to ensure stability and predictability for users building production applications.

    ## Release cadence

    We expect to space out **major** releases by at least 6-12 months to provide stability for production applications.

    **Minor** releases are typically released every 1-2 months with new features and improvements.

    **Patch** releases are released as needed, often weekly, to address bugs and security issues.

    ## API stability

    ### Stable APIs

    All APIs without special prefixes are considered stable and ready for production use. We maintain backward compatibility for stable features within a major version.

    ### Beta features

    Features marked as `beta` in the documentation are:

    * Feature-complete and tested
    * Safe for production use with the understanding they may change
    * Subject to minor API adjustments based on user feedback

    ### Experimental features

    Features marked as `experimental` or `alpha`:

    * Are under active development
    * May change significantly or be removed
    * Should be used with caution in production

    ### Internal APIs

    APIs prefixed with underscore (`_`) or explicitly marked as internal:

    * Are not part of the public API
    * May change without notice
    * Should not be used directly

    ## Deprecation policy

    When deprecating features:

    1. **Deprecation Notice**: Features are marked as deprecated with clear migration guidance
    2. **Grace Period**: Deprecated features remain functional for at least one minor version
    3. **Removal**: Features are removed only in major version releases
    4. **Migration Support**: We provide migration guides and, when possible, automated tools

    ## Platform compatibility

    ### JavaScript/TypeScript support

    * We support Node.js LTS versions
    * TypeScript definitions are provided for all public APIs
    * Browser compatibility is documented for client-side components

    ## Breaking changes

    Breaking changes are only introduced in major versions and include:

    * Removal of deprecated APIs
    * Changes to required parameters
    * Changes to default behavior that affect existing applications
    * Minimum Python/Node.js version updates

    ## Migration support

    For major version upgrades, we provide:

    * Comprehensive migration guides
    * Automated migration scripts when feasible
    * Extended support period for the previous major version
    * Clear documentation of all breaking changes

    ## Long-term support (LTS)

    LangGraph follows a long-term support (LTS) policy to provide stability for production applications:

    ### Release status definitions

    Packages are marked with one of the following statuses:

    * **ACTIVE**: Current active development, includes bug fixes, security patches, and new features
    * **MAINTENANCE**: Receives all security patches and critical bug fixes, but no new features

    ### Current LTS releases

    **LangGraph 1.0** is designated as an LTS release:

    * **Status**: ACTIVE until the release of 2.0
    * **Support period**: After 2.0 is released, 1.0 will enter MAINTENANCE mode for at least 1 year
    * **Semver compliance**: Users can upgrade between minor versions (e.g., 1.0 to 1.1) without breaking changes

    ### Legacy version support

    **LangGraph 0.4**:

    * **Status**: MAINTENANCE mode
    * **Support period**: Until December 2026
    * **Support includes**: All security patches and critical bug fixes

    ## See also

    * [Versioning](/oss/javascript/versioning) - Version numbering and support details
    * [Releases](/oss/javascript/releases) - Version-specific release notes and migration guides
  </Tab>

  <Tab title="Deep Agents" />
</Tabs>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/release-policy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
