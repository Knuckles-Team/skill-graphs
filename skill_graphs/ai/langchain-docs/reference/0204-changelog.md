# Changelog
Source: https://docs.langchain.com/oss/javascript/releases/changelog

Log of updates and improvements to our JavaScript/TypeScript packages

<Callout icon="rss">
  **Subscribe**: Our changelog includes an [RSS feed](https://docs.langchain.com/oss/javascript/releases/changelog/rss.xml) that can integrate with [Slack](https://slack.com/help/articles/218688467-Add-RSS-feeds-to-Slack), [email](https://zapier.com/apps/email/integrations/rss/1441/send-new-rss-feed-entries-via-email), Discord bots like [Readybot](https://readybot.io/) or [RSS Feeds to Discord Bot](https://rss.app/en/bots/rssfeeds-discord-bot), and other subscription tools.
</Callout>

<Update label="Mar 24, 2026">
  ## `deepagents` v1.9.0-alpha.0

  Alpha release of `deepagents` v1.9.0.

  * **[Async subagents](/oss/javascript/deepagents/async-subagents)**: Deep Agents can launch non-blocking background tasks, so users can continue interacting with the agent while subagents work concurrently. Requires [LangSmith Deployment](/langsmith/deployment) for sub-agents.

  * **[Backend](/oss/javascript/deepagents/backends) protocol v2**: We've introduced a new v2 backend protocol (`BackendProtocolV2`) with backward-compatible changes to the Deep Agents backend interface. Key changes:
    * **Structured result types**: All methods now return structured `Result` objects (e.g., `ReadResult`, `LsResult`, `GrepResult`, `GlobResult`) with consistent error handling via an `error` field, instead of returning raw values or throwing exceptions.
    * **Multi-modal file support**: `read()` returns a `ReadResult` with a `.content` field instead of a plain string. For binary files (images, PDFs, audio, video), the full raw `Uint8Array` content is returned via `readRaw()`, enabling agents to work with multi-modal files natively.
    * **Simplified method names**: `lsInfo` -> `ls`, `grepRaw` -> `grep`, `globInfo` -> `glob`.
    * **Backward compatible**: Existing v1 backends can be adapted to the v2 interface using `adaptBackendProtocol`. The v1 interfaces (`BackendProtocolV1`, `SandboxBackendProtocolV1`) are deprecated but retained for compatibility.
</Update>

<Update label="Jan 14, 2026">
  ## v1.1.0

  ### `@langchain/langgraph`

  Introducing **StateSchema** - a cleaner, library-agnostic way to define graph state that works with any [Standard Schema](https://github.com/standard-schema/standard-schema)-compliant validation library.

  ### Standard JSON Schema support

  LangGraph now supports [Standard JSON Schema](https://standardschema.dev/json-schema), an open specification implemented by Zod 4, Valibot, ArkType, and other schema libraries. This means you can use your preferred validation library without lock-in:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { z } from "zod"; // or valibot, arktype, etc.
  import { StateSchema, ReducedValue, MessagesValue } from "@langchain/langgraph";

  const AgentState = new StateSchema({
    messages: MessagesValue,
    currentStep: z.string(),
    count: z.number().default(0),
    history: new ReducedValue(
      z.array(z.string()).default(() => []),
      {
        inputSchema: z.string(),
        reducer: (current, next) => [...current, next],
      }
    ),
  });

  // Type-safe state and update types
  type State = typeof AgentState.State;
  type Update = typeof AgentState.Update;

  const graph = new StateGraph(AgentState)
    .addNode("agent", (state) => ({ count: state.count + 1 }))
    .addEdge(START, "agent")
    .addEdge("agent", END)
    .compile();
  ```

  ### New state value primitives

  * **ReducedValue**: Define fields with custom reducers for accumulating values. Supports separate input and output schemas for type-safe reducer inputs.
  * **UntrackedValue**: Define transient state that exists during execution but is never checkpointed - useful for database connections, caches, or runtime-only configuration.
  * **MessagesValue**: A prebuilt `ReducedValue` for chat messages with the standard messages reducer.

  ### Type helper exports

  New exported type utilities for typing functions outside the graph builder:

  * `GraphNode<Schema, Nodes?, Config?>` - Type node functions with full inference
  * `ConditionalEdgeRouter<Schema, Nodes?>` - Type conditional edge routers

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Type standalone node functions
  const myNode: GraphNode<typeof AgentState> = (state, config) => {
    return { count: state.count + 1 };
  };

  // Use schema type helpers directly
  const processState = (state: typeof AgentState.State) => {
    console.log(state.count);
  };
  ```

  The existing `Annotation` and zod-based API continues to work unchanged - `StateSchema` is an additional option for those who prefer schema-first definitions.

  <Card title="Learn more about StateSchema" icon="book" href="/oss/javascript/langgraph/graph-api#schema">
    See the full documentation for defining graph state with StateSchema, ReducedValue, and UntrackedValue.
  </Card>

  <Card title="Learn about type utilities" icon="code" href="/oss/javascript/langgraph/graph-api#type-utilities">
    Use GraphNode and ConditionalEdgeRouter to type functions outside the graph builder.
  </Card>
</Update>

<Update label="Dec 12, 2025">
  ## v1.2.0

  ### `langchain`

  * [Structured output](/oss/javascript/langchain/structured-output): Added ability to manually set `strict` mode when using `providerStrategy` for structured output.

  ### `@langchain/openai`

  * **New provider built-in tools:** Support for file search, web search, code interpreter, image generation, computer use, shell, and MCP connector tools executed server-side by the provider. See [Server-side tool use](/oss/javascript/langchain/tools#server-side-tool-use) and the [OpenAI](/oss/javascript/integrations/chat/openai) chat integration.
  * **Content moderation:** New `moderateContent` option on `ChatOpenAI` for detecting and handling unsafe content.
  * Prefer responses API for GPT-5.2 Pro model.

  ## v1.3.0

  ### `@langchain/anthropic`

  * **New provider built-in tools:** Support for text editor, web fetch, computer use, tool search, and MCP toolset tools executed server-side by the provider. See [Server-side tool use](/oss/javascript/langchain/tools#server-side-tool-use) and the [Anthropic](/oss/javascript/integrations/chat/anthropic) chat integration.
  * Exposed `ChatAnthropicInput` type for improved type safety.

  ## v1.1.0

  ### `@langchain/ollama`

  * **Native structured outputs:** Added support for native structured output via `withStructuredOutput`.
  * Support for custom `baseUrl` configuration.

  ## v1.0.0

  ### `@langchain/community`

  * Jira document loader updated to use v3 API.
  * LanceDB: Added `similaritySearch()` and `similaritySearchWithScore()` support.
  * Elasticsearch hybrid search support.
  * New `GoogleCalendarDeleteTool`.
  * Various bug fixes for LlamaCppEmbeddings, PrismaVectorStore, IBM WatsonX, and security improvements.

  ### Other packages

  * **@langchain/xai:** Native Live Search support.
  * **@langchain/tavily:** Added Tavily's research endpoint.
  * **@langchain/mongodb:** New MongoDB LLM cache.
  * **@langchain/mcp-adapters:** Added `onConnectionError` option.
  * **@langchain/google-common:** `jsonSchema` method support in `withStructuredOutput`.
  * **@langchain/core:** Security fixes, better subgraph nesting in Mermaid graphs, UUID7 for run IDs.
</Update>

<Update label="Nov 25, 2025">
  ## v1.1.0

  * [Model profiles](/oss/javascript/langchain/models#model-profiles): Chat models now expose supported features and capabilities through a `.profile` getter. These data are derived from [models.dev](https://models.dev), an open source project providing model capability data.
  * [Model retry middleware](/oss/javascript/langchain/middleware/built-in#model-retry): New middleware for automatically retrying failed model calls with configurable exponential backoff, improving agent reliability.
  * [Content moderation middleware](/oss/javascript/langchain/middleware/built-in#provider-specific-middleware): OpenAI content moderation middleware for detecting and handling unsafe content in agent interactions. Supports checking user input, model output, and tool results.
  * [Summarization middleware](/oss/javascript/langchain/middleware/built-in#summarization): Updated to support flexible trigger points using model profiles for context-aware summarization.
  * [Structured output](/oss/javascript/langchain/structured-output): `ProviderStrategy` support (native structured output) can now be inferred from model profiles.
  * [`SystemMessage` for `createAgent`](/oss/javascript/langchain/middleware/custom#dynamic-prompt): Support for passing `SystemMessage` instances directly to `createAgent`'s `systemPrompt` parameter and a new `concat` method for extending system messages. Enables advanced features like cache control and structured content blocks.
  * [Dynamic system prompt middleware](/oss/javascript/langchain/short-term-memory): Return values from `dynamicSystemPromptMiddleware` are now purely additive. When returning a [`SystemMessage`](https://reference.langchain.com/javascript/langchain-core/messages/SystemMessage) or `string`, they are merged with existing system messages rather than replacing them, making it easier to compose multiple middleware that modify the prompt.
  * **Compatibility improvements:** Fixed error handling for Zod v4 validation errors in structured output and tool schemas, ensuring detailed error messages are properly displayed.
</Update>

<Update label="Oct 20, 2025">
  ## v1.0.0

  ### `langchain`

  * [Release notes](/oss/javascript/releases/langchain-v1)
  * [Migration guide](/oss/javascript/migrate/langchain-v1)

  ### `langgraph`

  * [Release notes](/oss/javascript/releases/langgraph-v1)
  * [Migration guide](/oss/javascript/migrate/langgraph-v1)

  <Callout icon="speakerphone">
    If you encounter any issues or have feedback, please [open an issue](https://github.com/langchain-ai/docs/issues/new?template=01-langchain.yml) so we can improve. To view v0.x documentation, [go to the archived content](https://github.com/langchain-ai/langchainjs/tree/v0.3/docs/core_docs/docs).
  </Callout>
</Update>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/releases/changelog.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# What's new in LangChain v1
Source: https://docs.langchain.com/oss/javascript/releases/langchain-v1

**LangChain v1 is a focused, production-ready foundation for building agents.** We've streamlined the framework around three core improvements:

<CardGroup>
  <Card title="createAgent" icon="robot" href="#createagent">
    A new standard way to build agents in LangChain, replacing `createReactAgent` from LangGraph with a cleaner, more powerful API.
  </Card>

  <Card title="Standard content blocks" icon="cube" href="#standard-content-blocks">
    A new `contentBlocks` property that provides unified access to modern LLM features across all providers.
  </Card>

  <Card title="Simplified package" icon="sitemap" href="#simplified-package">
    The `langchain` package has been streamlined to focus on essential building blocks for agents, with legacy functionality moved to `@langchain/classic`.
  </Card>
</CardGroup>

To upgrade,

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langchain @langchain/core
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm install langchain @langchain/core
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add langchain @langchain/core
  ```

  ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  bun add langchain @langchain/core
  ```
</CodeGroup>

For a complete list of changes, see the [migration guide](/oss/javascript/migrate/langchain-v1).

## `createAgent`

`createAgent` is the standard way to build agents in LangChain 1.0. It provides a simpler interface than the prebuilt `createReactAgent` exported from LangGraph while offering greater customization potential by using middleware.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent } from "langchain";

const agent = createAgent({
  model: "claude-sonnet-4-6",
  tools: [getWeather],
  systemPrompt: "You are a helpful assistant.",
});

const result = await agent.invoke({
  messages: [
    { role: "user", content: "What is the weather in Tokyo?" },
  ],
});

console.log(result.content);
```

Under the hood, `createAgent` is built on the basic agent loop -- calling a model, letting it choose tools to execute, and then finishing when it calls no more tools:

<div>
  <img alt="Core agent loop diagram" />
</div>

For more information, see [Agents](/oss/javascript/langchain/agents).

### Middleware

Middleware is the defining feature of `createAgent`. It makes `createAgent` highly customizable, raising the ceiling for what you can build.

Great agents require [context engineering](/oss/javascript/langchain/context-engineering): getting the right information to the model at the right time. Middleware helps you control dynamic prompts, conversation summarization, selective tool access, state management, and guardrails through a composable abstraction.

#### Prebuilt middleware

LangChain provides a few [prebuilt middlewares](/oss/javascript/langchain/middleware#built-in-middleware) for common patterns, including:

* `summarizationMiddleware`: Condense conversation history when it gets too long
* `humanInTheLoopMiddleware`: Require approval for sensitive tool calls
* `piiRedactionMiddleware`: Redact sensitive information before sending to the model

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  createAgent,
  summarizationMiddleware,
  humanInTheLoopMiddleware,
  piiRedactionMiddleware,
} from "langchain";

const agent = createAgent({
  model: "claude-sonnet-4-6",
  tools: [readEmail, sendEmail],
  middleware: [
    piiRedactionMiddleware({ patterns: ["email", "phone", "ssn"] }),
    summarizationMiddleware({
      model: "claude-sonnet-4-6",
      trigger: { tokens: 500 },
    }),
    humanInTheLoopMiddleware({
      interruptOn: {
        sendEmail: {
          allowedDecisions: ["approve", "edit", "reject"],
        },
      },
    }),
  ],
});
```

#### Custom middleware

You can also build custom middleware to fit your specific needs.

Build custom middleware by implementing any of these hooks using the `createMiddleware` function:

| Hook            | When it runs             | Use cases                               |
| --------------- | ------------------------ | --------------------------------------- |
| `beforeAgent`   | Before calling the agent | Load memory, validate input             |
| `beforeModel`   | Before each LLM call     | Update prompts, trim messages           |
| `wrapModelCall` | Around each LLM call     | Intercept and modify requests/responses |
| `wrapToolCall`  | Around each tool call    | Intercept and modify tool execution     |
| `afterModel`    | After each LLM response  | Validate output, apply guardrails       |
| `afterAgent`    | After agent completes    | Save results, cleanup                   |

<div>
  <img alt="Middleware flow diagram" />
</div>

Example custom middleware:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createMiddleware } from "langchain";

const contextSchema = z.object({
  userExpertise: z.enum(["beginner", "expert"]).default("beginner"),
})

const expertiseBasedToolMiddleware = createMiddleware({
  wrapModelCall: async (request, handler) => {
    const userLevel = request.runtime.context.userExpertise;
    if (userLevel === "expert") {
      const tools = [advancedSearch, dataAnalysis];
      return handler(
        request.replace("openai:gpt-5.5", tools)
      );
    }
    const tools = [simpleSearch, basicCalculator];
    return handler(
      request.replace("openai:gpt-5-nano", tools)
    );
  },
});

const agent = createAgent({
  model: "claude-sonnet-4-6",
  tools: [simpleSearch, advancedSearch, basicCalculator, dataAnalysis],
  middleware: [expertiseBasedToolMiddleware],
  contextSchema,
});
```

For more information, see [the complete middleware guide](/oss/javascript/langchain/middleware).

### Built on LangGraph

Because `createAgent` is built on LangGraph, you automatically get built in support for long running and reliable agents via:

<CardGroup>
  <Card title="Persistence" icon="database">
    Conversations automatically persist across sessions with built-in checkpointing
  </Card>

  <Card title="Streaming" icon="droplet">
    Stream tokens, tool calls, and reasoning traces in real-time
  </Card>

  <Card title="Human-in-the-loop" icon="hand-stop">
    Pause agent execution for human approval before sensitive actions
  </Card>

  <Card title="Time travel" icon="history">
    Rewind conversations to any point and explore alternate paths and prompts
  </Card>
</CardGroup>

You don't need to learn LangGraph to use these features—they work out of the box.

### Structured output

`createAgent` has improved structured output generation:

* **Main loop integration**: Structured output is now generated in the main loop instead of requiring an additional LLM call
* **Structured output strategy**: Models can choose between calling tools or using provider-side structured output generation
* **Cost reduction**: Eliminates extra expense from additional LLM calls

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent } from "langchain";
import * as z from "zod";

const weatherSchema = z.object({
  temperature: z.number(),
  condition: z.string(),
});

const agent = createAgent({
  model: "gpt-5.4-mini",
  tools: [getWeather],
  responseFormat: weatherSchema,
});

const result = await agent.invoke({
  messages: [
    { role: "user", content: "What is the weather in Tokyo?" },
  ],
});

console.log(result.structuredResponse);
```

**Error handling**: Control error handling via the `handleErrors` parameter to `ToolStrategy`:

* **Parsing errors**: Model generates data that doesn't match desired structure
* **Multiple tool calls**: Model generates 2+ tool calls for structured output schemas

***

## Standard content blocks

<Note>
  1.0 releases are available for most packages. Only the following currently support new content blocks:

  * `langchain`
  * `@langchain/core`
  * `@langchain/anthropic`
  * `@langchain/openai`

  Broader support for content blocks is planned.
</Note>

### Benefits

* **Provider agnostic**: Access reasoning traces, citations, built-in tools (web search, code interpreters, etc.), and other features using the same API regardless of provider
* **Type safe**: Full type hints for all content block types
* **Backward compatible**: Standard content can be [loaded lazily](/oss/javascript/langchain/messages#standard-content-blocks), so there are no associated breaking changes

For more information, see our guide on [content blocks](/oss/javascript/langchain/messages#message-content)

***

## Simplified package

LangChain v1 streamlines the `langchain` package namespace to focus on essential building blocks for agents. The package exposes only the most useful and relevant functionality:

Most of these are re-exported from `@langchain/core` for convenience, which gives you a focused API surface for building agents.

### `@langchain/classic`

Legacy functionality has moved to [`@langchain/classic`](https://www.npmjs.com/package/@langchain/classic) to keep the core package lean and focused.

#### What's in `@langchain/classic`

* Legacy chains and chain implementations
* Retrievers
* The indexing API
* [`@langchain/community`](https://www.npmjs.com/package/@langchain/community) exports
* Other deprecated functionality

If you use any of this functionality, install [`@langchain/classic`](https://www.npmjs.com/package/@langchain/classic):

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

Then update your imports:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ... } from "langchain"; // [!code --]
import { ... } from "@langchain/classic"; // [!code ++]

import { ... } from "langchain/chains"; // [!code --]
import { ... } from "@langchain/classic/chains"; // [!code ++]
```

## Reporting issues

Please report any issues discovered with 1.0 on [GitHub](https://github.com/langchain-ai/langchainjs/issues) using the [`'v1'` label](https://github.com/langchain-ai/langchainjs/issues?q=state%3Aopen%20label%3Av1).

## Additional resources

<CardGroup>
  <Card title="LangChain 1.0" icon="rocket" href="https://blog.langchain.com/langchain-langchain-1-0-alpha-releases/">
    Read the announcement
  </Card>

  <Card title="Middleware guide" icon="puzzle" href="https://blog.langchain.com/agent-middleware/">
    Deep dive into middleware
  </Card>

  <Card title="Agents Documentation" icon="book" href="/oss/javascript/langchain/agents">
    Full agent documentation
  </Card>

  <Card title="Message Content" icon="message" href="/oss/javascript/langchain/messages#message-content">
    New content blocks API
  </Card>

  <Card title="Migration guide" icon="arrows-exchange" href="/oss/javascript/migrate/langchain-v1">
    How to migrate to LangChain v1
  </Card>

  <Card title="GitHub" icon="brand-github" href="https://github.com/langchain-ai/langchainjs">
    Report issues or contribute
  </Card>
</CardGroup>

## See also

* [Versioning](/oss/javascript/versioning) – Understanding version numbers
* [Release policy](/oss/javascript/release-policy) – Detailed release policies

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/releases/langchain-v1.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# What's new in LangGraph v1
Source: https://docs.langchain.com/oss/javascript/releases/langgraph-v1

**LangGraph v1 is a stability-focused release for the agent runtime.** It keeps the core graph APIs and execution model unchanged, while refining type safety, docs, and developer ergonomics.

It's designed to work hand-in-hand with [LangChain v1](/oss/javascript/releases/langchain-v1) (whose `createAgent` is built on LangGraph) so you can start high-level and drop down to granular control when needed.

<CardGroup>
  <Card title="Stable core APIs" icon="sitemap">
    Graph primitives (state, nodes, edges) and the execution/runtime model are unchanged, making upgrades straightforward.
  </Card>

  <Card title="Reliability, by default" icon="database">
    Durable execution with checkpointing, persistence, streaming, and human-in-the-loop continues to be first-class.
  </Card>

  <Card title="Seamless with LangChain v1" icon="link">
    LangChain's `createAgent` runs on LangGraph. Use LangChain for a fast start; drop to LangGraph for custom orchestration.
  </Card>
</CardGroup>

To upgrade,

<CodeGroup>
  ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install @langchain/langgraph @langchain/core
  ```

  ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pnpm add @langchain/langgraph @langchain/core
  ```

  ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  yarn add @langchain/langgraph @langchain/core
  ```

  ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  bun add @langchain/langgraph @langchain/core
  ```
</CodeGroup>

For a complete list of changes, see the [migration guide](/oss/javascript/migrate/langgraph-v1).

## Deprecation of `createReactAgent`

The LangGraph `createReactAgent` prebuilt has been deprecated in favor of LangChain's `createAgent`. It provides a simpler interface, and offers greater customization potential through the introduction of middleware.

* For information on the new `createAgent` API, see the [LangChain v1 release notes](/oss/javascript/releases/langchain-v1#createagent).
* For information on migrating from `createReactAgent` to `createAgent`, see the [LangChain v1 migration guide](/oss/javascript/migrate/langchain-v1#createagent).

## Typed interrupts

[`StateGraph`](https://reference.langchain.com/javascript/langchain-langgraph/index/StateGraph) now accepts a map of interrupt types in the constructor to more closely constrain the types of interrupts that can be used within a graph.

```typescript expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StateGraph, MemorySaver, interrupt } from "@langchain/langgraph";
import * as z from "zod";

const stateSchema = z.object({
  foo: z.string(),
})

const graphConfig = {
  interrupts: {
    // Define a simple interrupt that accepts a reason and returns messages
    simple: interrupt<{ reason: string }, { messages: string[] }>, // [!code highlight]
    // Define a complex interrupt with the same signature
    complex: interrupt<{ reason: string }, { messages: string[] }>, // [!code highlight]
  }
}

const checkpointer = new MemorySaver();

const graph = new StateGraph(stateSchema, graphConfig)
  .addNode("node", async (state, runtime) => {
    // Trigger the simple interrupt with a reason
    const response = runtime.interrupt.simple({ reason: "test" });
    // Return the interrupt response as the new state
    return { foo: response };
  })
  // Compile the graph with the checkpointer
  .compile({ checkpointer });

// Invoke the graph with initial state
const result = await graph.invoke({ foo: "test" });

// Access the interrupt data
if (graph.isInterrupted(result)) {
  console.log(result.__interrupt__.messages);
}
```

For more information on interrupts, see the [Interrupts](/oss/javascript/langgraph/interrupts) documentation.

## Frontend SDK enhancements

LangGraph v1 comes with a few enhancements when interacting with a LangGraph application from the frontend.

### Event stream encoding

The low-level `toLangGraphEventStream` helper has been removed. Streaming responses are now handled natively by the SDK, and you can select the wire format via passing in the `encoding` format to `graph.stream`. This makes switching between SSE and normal JSON responses straightforward without changing UI logic.

See the [migration guide](/oss/javascript/migrate/langgraph-v1#event-stream-encoding) for more information.

### Custom transports in `useStream`

The React `useStream` hook now supports pluggable transports so you can have more control over the network layer without changing UI code.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = useStream({
  transport: new FetchStreamTransport({
    apiUrl: "http://localhost:2024",
  }),
});
```

Learn how to integrate and customize the hook: [Integrate LangGraph into your React application](/oss/javascript/langgraph/ui).

## Reporting issues

Please report any issues discovered with 1.0 on [GitHub](https://github.com/langchain-ai/langgraphjs/issues) using the [`'v1'` label](https://github.com/langchain-ai/langgraphjs/issues?q=state%3Aopen%20label%3Av1).

## Additional resources

<CardGroup>
  <Card title="LangGraph 1.0" icon="rocket" href="https://blog.langchain.com/langchain-langchain-1-0-alpha-releases/">
    Read the announcement
  </Card>

  <Card title="Overview" icon="book" href="/oss/javascript/langgraph/overview">
    What LangGraph is and when to use it
  </Card>

  <Card title="Graph API" icon="sitemap" href="/oss/javascript/langgraph/graph-api">
    Build graphs with state, nodes, and edges
  </Card>

  <Card title="LangChain Agents" icon="robot" href="/oss/javascript/langchain/agents">
    High-level agents built on LangGraph
  </Card>

  <Card title="Migration guide" icon="arrows-exchange" href="/oss/javascript/migrate/langgraph-v1">
    How to migrate to LangGraph v1
  </Card>

  <Card title="GitHub" icon="brand-github" href="https://github.com/langchain-ai/langgraphjs">
    Report issues or contribute
  </Card>
</CardGroup>

## See also

* [Versioning](/oss/javascript/versioning) – Understanding version numbers
* [Release policy](/oss/javascript/release-policy) – Detailed release policies

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/releases/langgraph-v1.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Security policy
Source: https://docs.langchain.com/oss/javascript/security-policy

LangChain has a large ecosystem of integrations with various external resources like local and remote file systems, APIs and databases. These integrations allow developers to create versatile applications that combine the power of LLMs with the ability to access, interact with and manipulate external resources.

## Best practices

When building such applications developers should remember to follow good security practices:

* [**Limit permissions**](https://en.wikipedia.org/wiki/Principle_of_least_privilege): Scope permissions specifically to the application's need. Granting broad or excessive permissions can introduce significant security vulnerabilities. To avoid such vulnerabilities, consider using read-only credentials, disallowing access to sensitive resources, using sandboxing techniques (such as running inside a container), specifying proxy configurations to control external requests, etc. as appropriate for your application.
* **Anticipate potential misuse**: Just as humans can err, so can Large Language Models (LLMs). Always assume that any system access or credentials may be used in any way allowed by the permissions they are assigned. For example, if a pair of database credentials allows deleting data, it's safest to assume that any LLM able to use those credentials may in fact delete data.
* [**Defense in depth**](https://en.wikipedia.org/wiki/Defense_in_depth_\(computing\)): No security technique is perfect. Fine-tuning and good chain design can reduce, but not eliminate, the odds that a Large Language Model (LLM) may make a mistake. It's best to combine multiple layered security approaches rather than relying on any single layer of defense to ensure security. For example: use both read-only permissions and sandboxing to ensure that LLMs are only able to access data that is explicitly meant for them to use.

Risks of not doing so include, but are not limited to:

* Data corruption or loss.
* Unauthorized access to confidential information.
* Compromised performance or availability of critical resources.

Example scenarios with mitigation strategies:

* A user may ask an agent with access to the file system to delete files that should not be deleted or read the content of files that contain sensitive information. To mitigate, limit the agent to only use a specific directory and only allow it to read or write files that are safe to read or write. Consider further sandboxing the agent by running it in a container.
* A user may ask an agent with write access to an external API to write malicious data to the API, or delete data from that API. To mitigate, give the agent read-only API keys, or limit it to only use endpoints that are already resistant to such misuse.
* A user may ask an agent with access to a database to drop a table or mutate the schema. To mitigate, scope the credentials to only the tables that the agent needs to access and consider issuing READ-ONLY credentials.

If you're building applications that access external resources like file systems, APIs
or databases, consider speaking with your company's security team to determine how to best
design and secure your applications.

## Reporting OSS vulnerabilities

Please report security vulnerabilities associated with the LangChain open source projects using the following process:

1. **Submit a security advisory** on the Security tab in the GitHubrepository where the vulnerability exists.
2. **Send an email** to `security@langchain.dev` notifying us that you've filed a security issue and which repository it was filed in.

Before reporting a vulnerability, please review the [Best Practices](#best-practices) above to understand what we consider to be a security vulnerability vs. developer responsibility.

### Bug bounty eligibility

We welcome security vulnerability reports for all LangChain libraries. However, we may offer ad hoc bug bounties only for vulnerabilities in the following packages:

* Core libraries owned and maintained by the LangChain team: `langchain-core`, `langchain` (v1), `langgraph`, and related checkpointer packages (or their JavaScript equivalents)
* Popular integrations maintained by the LangChain team (e.g., `langchain-openai`, `langchain-anthropic`, etc., or their JavaScript equivalents)

The vulnerability must be in the library code itself, not in example code or example applications.

We welcome reports for all other LangChain packages and will address valid security concerns, but bug bounties will not be awarded for packages outside this scope. This includes the archived `langchain-community`, which due to its community-driven nature is not eligible for bug bounties, though we will accept and address reports.

### Out-of-scope targets

The following are out-of-scope for security vulnerability reports:

* **langchain-experimental**: This archived repository is for experimental code and is not in scope for security reports (see [package warning](https://pypi.org/project/langchain-experimental/)).
* **Examples and example applications**: Example code and demo applications are not in scope for security reports.
* **Code documented with security notices**: This will be decided on a case-by-case basis, but likely will not be in scope as the code is already documented with guidelines for developers that should be followed for making their application secure.
* **LangSmith related repositories or APIs**: See [Reporting LangSmith Vulnerabilities](#reporting-langsmith-vulnerabilities) below.

## Reporting LangSmith vulnerabilities

Please report security vulnerabilities associated with LangSmith by email to `security@langchain.dev`.

* LangSmith site: [https://smith.langchain.com?utm\_source=docs\&utm\_medium=cta\&utm\_campaign=langsmith-signup\&utm\_content=oss-security-policy](https://smith.langchain.com)
* SDK client: [https://github.com/langchain-ai/langsmith-sdk](https://github.com/langchain-ai/langsmith-sdk)

### Other security concerns

For any other security concerns, please contact us at `security@langchain.dev`.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/security-policy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Studio
Source: https://docs.langchain.com/oss/javascript/studio

Develop, run, and debug LangGraph agents in an interactive environment with LangSmith Studio.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/studio.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Versioning
Source: https://docs.langchain.com/oss/javascript/versioning

Our OSS version numbers follow the format: `MAJOR.MINOR.PATCH`, as defined by [Semantic Versioning](https://semver.org/).

* **Major**: Breaking API updates that require code changes.
* **Minor**: New features and improvements that maintain backward compatibility.
* **Patch**: Bug fixes and minor improvements.

For example:

* `1.0.0`: First stable release with production-ready APIs
* `1.1.0`: New features added in a backward-compatible manner
* `1.0.1`: Backward-compatible bug fixes

## API stability

We communicate the stability of our APIs as follows:

### Stable APIs

All APIs without special prefixes are considered stable and ready for production use. We maintain backward compatibility for stable features and only introduce breaking changes in major releases.

### Beta APIs

APIs marked as `beta` are feature-complete but may undergo minor changes based on user feedback. They are safe for production use but may require small adjustments in future releases.

### Alpha APIs

APIs marked as `alpha` are experimental and subject to significant changes. Use these with caution in production environments.

### Deprecated APIs

APIs marked as `deprecated` will be removed in future major releases. When possible, we specify the intended version of removal. To handle deprecations:

1. Switch to the recommended alternative API
2. Follow the migration guide (released alongside major releases)
3. Use automated migration tools when available

### Internal APIs

Certain APIs are explicitly marked as "internal" in a couple of ways:

* Some documentation refers to internals and mentions them as such. If the documentation says that something is internal, it may change.
* Functions, methods, and other objects prefixed by a leading underscore (**`_`**). This is the standard Python convention of indicating that something is private; if any method starts with a single **`_`**, it's an internal API.
  * **Exception:** Certain methods are prefixed with `_` , but do not contain an implementation. These methods are *meant* to be overridden by sub-classes that provide the implementation. Such methods are generally part of the **Public API** of LangChain.

## Release cycles

<AccordionGroup>
  <Accordion title="Major releases">
    Major releases (e.g., `1.0.0` → `2.0.0`) may include:

    * Breaking API changes
    * Removal of deprecated features
    * Significant architectural improvements

    We provide:

    * Detailed migration guides
    * Automated migration tools when possible
    * Extended support period for the previous major version
  </Accordion>

  <Accordion title="Minor releases">
    Minor releases (e.g., `1.0.0` → `1.1.0`) include:

    * New features and capabilities
    * Performance improvements
    * New optional parameters
    * Backward-compatible enhancements
  </Accordion>

  <Accordion title="Patch releases">
    Patch releases (e.g., `1.0.0` → `1.0.1`) include:

    * Bug fixes
    * Security updates
    * Documentation improvements
    * Performance optimizations without API changes
  </Accordion>
</AccordionGroup>

## Version support policy

* **Latest major version**: Full support with active development (ACTIVE status)
* **Previous major version**: Security updates and critical bug fixes for 12 months after the next major release (MAINTENANCE status)
* **Older versions**: Community support only

### Long-term support (LTS) releases

Both LangChain and LangGraph 1.0 are designated as LTS releases:

* Version 1.0 will remain in ACTIVE status until version 2.0 is released
* After version 2.0 is released, version 1.0 will enter MAINTENANCE mode for at least 1 year
* LTS releases follow semantic versioning (semver), allowing safe upgrades between minor versions
* Legacy versions (LangChain 0.3 and LangGraph 0.4) are in MAINTENANCE mode until December 2026

### Pre-1.0 packages

For detailed information about release status and support timelines, see the [Release policy](/oss/javascript/release-policy).

## Check your version

To check your installed version:

<CodeGroup>
  ```javascript LangChain theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { version } from "langchain/package.json";
  console.log(version);
  ```

  ```javascript LangGraph theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { version } from "@langchain/langgraph/package.json";
  console.log(version);
  ```
</CodeGroup>

## Upgrade

<CodeGroup>
  ```bash LangChain theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Upgrade to the latest version
  npm update langchain @langchain/core

  # Install a specific version
  npm install langchain@1.0.0 @langchain/core@1.0.0
  ```

  ```bash LangGraph theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Upgrade to the latest version
  npm update @langchain/langgraph

  # Install a specific version
  npm install @langchain/langgraph@1.0.0
  ```
</CodeGroup>

## Pre-release versions

We occasionally release alpha and beta versions for early testing:

* **Alpha** (e.g., `1.0.0a1`): Early preview, significant changes expected
* **Beta** (e.g., `1.0.0b1`): Feature-complete, minor changes possible
* **Release Candidate** (e.g., `1.0.0rc1`): Final testing before stable release

## See also

* [Release policy](/oss/javascript/release-policy) - Detailed release and deprecation policies

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/versioning.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Build
Source: https://docs.langchain.com/oss/python/build-overview

Build agents with LangChain, LangGraph, and Deep Agents using Python.

<div>
  <div>
    <h1>Build</h1>

    The LangChain open source stack provides the building blocks you need to design, test, and ship agents in Python.

    <h2>Choose your starting point</h2>

    Deep Agents, LangChain, and LangGraph share the same stack, so choose based on how much control you need:

    <CardGroup>
      <Card title="Deep Agents" href="/oss/python/deepagents/overview" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/deep-agents-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=1cc68f66a9e7550331cc0875f1ba53af">
        Build agents for complex, long-running tasks. A complete agent harness with planning, subagents, a virtual filesystem, and long-term memory built in. The fastest way to start.
      </Card>

      <Card title="LangChain" href="/oss/python/langchain/overview" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langchain-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=663b30f85baf99ad708b97e05da2a5a4">
        A minimal, configurable agent framework. Compose exactly what you need from models, tools, prompts, and middleware.
      </Card>

      <Card title="LangGraph" href="/oss/python/langgraph/overview" icon="https://mintcdn.com/langchain-5e9cc07a/nQm-sjd_MByLhgeW/images/brand/langgraph-icon.png?fit=max&auto=format&n=nQm-sjd_MByLhgeW&q=85&s=b997e1a7487d507a36556eedbfd99f81">
        Low-level orchestration for stateful, long-running agents: durable execution, streaming, memory, and human-in-the-loop.
      </Card>
    </CardGroup>

    <h2>Explore</h2>

    <CardGroup>
      <Card title="Integrations" href="/oss/python/integrations/providers/overview" icon="plug">
        Connect to model providers, vector stores, retrievers, and other components.
      </Card>

      <Card title="Learn" href="/oss/python/learn" icon="book">
        Follow tutorials and conceptual guides for common agent patterns and use cases.
      </Card>

      <Card title="Reference" href="/oss/python/reference/overview" icon="code">
        API references, error codes, release notes, and migration guides.
      </Card>

      <Card title="Contribute" href="/oss/python/contributing/overview" icon="heart-plus">
        Contribute documentation, code, and integrations to the LangChain ecosystem.
      </Card>
    </CardGroup>
  </div>
</div>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/build-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Errors
Source: https://docs.langchain.com/oss/python/common-errors

This page contains guides around resolving common errors you may find while building with LangChain and LangGraph.

Errors referenced below will have an `lc_error_code` property corresponding to one of the below codes when they are thrown in code.

| Error code                                                                                          |
| --------------------------------------------------------------------------------------------------- |
| [GRAPH\_RECURSION\_LIMIT](/oss/python/langgraph/errors/GRAPH_RECURSION_LIMIT)                       |
| [INVALID\_CHAT\_HISTORY](/oss/python/langgraph/errors/INVALID_CHAT_HISTORY)                         |
| [INVALID\_CONCURRENT\_GRAPH\_UPDATE](/oss/python/langgraph/errors/INVALID_CONCURRENT_GRAPH_UPDATE)  |
| [INVALID\_GRAPH\_NODE\_RETURN\_VALUE](/oss/python/langgraph/errors/INVALID_GRAPH_NODE_RETURN_VALUE) |
| [INVALID\_PROMPT\_INPUT](/oss/python/langchain/errors/INVALID_PROMPT_INPUT)                         |
| [INVALID\_TOOL\_RESULTS](/oss/python/langchain/errors/INVALID_TOOL_RESULTS)                         |
| [MESSAGE\_COERCION\_FAILURE](/oss/python/langchain/errors/MESSAGE_COERCION_FAILURE)                 |
| [MISSING\_CHECKPOINTER](/oss/python/langgraph/errors/MISSING_CHECKPOINTER)                          |
| [MODEL\_AUTHENTICATION](/oss/python/langchain/errors/MODEL_AUTHENTICATION)                          |
| [MODEL\_NOT\_FOUND](/oss/python/langchain/errors/MODEL_NOT_FOUND)                                   |
| [MODEL\_RATE\_LIMIT](/oss/python/langchain/errors/MODEL_RATE_LIMIT)                                 |
| [MULTIPLE\_SUBGRAPHS](/oss/python/langgraph/errors/MULTIPLE_SUBGRAPHS)                              |
| [OUTPUT\_PARSING\_FAILURE](/oss/python/langchain/errors/OUTPUT_PARSING_FAILURE)                     |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/common-errors.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
