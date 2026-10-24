# Streaming
Source: https://docs.langchain.com/oss/javascript/langchain/streaming

Stream real-time updates from agent runs

<Tip>
  For new applications, we recommend [event streaming](/oss/javascript/langchain/event-streaming)—the typed-projection API introduced in LangChain v1.3. Event streaming gives you separate iterators per projection (messages, values, tool calls, subgraphs) so you can consume them independently instead of branching on `stream_mode` chunks.
</Tip>

LangChain implements a streaming system to surface real-time updates.

Streaming is crucial for enhancing the responsiveness of applications built on LLMs. By displaying output progressively, even before a complete response is ready, streaming significantly improves user experience (UX), particularly when dealing with the latency of LLMs.

## Overview

LangChain's streaming system lets you surface live feedback from agent runs to your application.

What's possible with LangChain streaming:

* <Icon icon="brain" /> [**Stream agent progress**](#agent-progress)—get state updates after each agent step.
* <Icon icon="binary" /> [**Stream LLM tokens**](#llm-tokens)—stream language model tokens as they're generated.
* <Icon icon="bulb" /> [**Stream thinking / reasoning tokens**](#streaming-thinking-/-reasoning-tokens)—surface model reasoning as it's generated.
* <Icon icon="table" /> [**Stream custom updates**](#custom-updates)—emit user-defined signals (e.g., `"Fetched 10/100 records"`).
* <Icon icon="stack-push" /> [**Stream multiple modes**](#stream-multiple-modes)—choose from `updates` (agent progress), `messages` (LLM tokens + metadata), or `custom` (arbitrary user data).

See the [common patterns](#common-patterns) section below for additional end-to-end examples.

## Supported stream modes

Pass one or more of the following stream modes as a list to the [`stream`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.CompiledStateGraph.html#stream) method:

| Mode       | Description                                                                                                                                                       |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `updates`  | Streams state updates after each agent step. If multiple updates are made in the same step (e.g., multiple nodes are run), those updates are streamed separately. |
| `messages` | Streams tuples of `(token, metadata)` from any graph nodes where an LLM is invoked.                                                                               |
| `custom`   | Streams custom data from inside your graph nodes using the stream writer.                                                                                         |

## Agent progress

To stream agent progress, use the [`stream`](https://reference.langchain.com/javascript/classes/_langchain_langgraph.index.CompiledStateGraph.html#stream) method with `streamMode: "updates"`. This emits an event after every agent step.

For example, if you have an agent that calls a tool once, you should see the following updates:

* **LLM node**: [`AIMessage`](https://reference.langchain.com/javascript/langchain-core/messages/AIMessage) with tool call requests
* **Tool node**: [`ToolMessage`](https://reference.langchain.com/javascript/langchain-core/messages/ToolMessage) with execution result
* **LLM node**: Final AI response

Pass a `thread_id` via `configurable` so the conversation is checkpointed and follow-up turns can resume the same history. `thread_id` is independent of `streamMode`; you can also pass `context` alongside it for per-run data your tools read from `runtime.context`.

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, tool } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";
  import z from "zod";

  const getWeather = tool(
    async ({ city }) => {
      return `The weather in ${city} is always sunny!`;
    },
    {
      name: "get_weather",
      description: "Get weather for a given city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  const agent = createAgent({
    model: "google-genai:gemini-3.5-flash",
    tools: [getWeather],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  for await (const chunk of await agent.stream(
    { messages: [{ role: "user", content: "what is the weather in sf" }] },
    { ...config, streamMode: "updates", version: "v2" },
  )) {
    const [step, content] = Object.entries(chunk)[0];
    console.log(`step: ${step}`);
    console.log(`content: ${JSON.stringify(content, null, 2)}`);
  }
  /**
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         // ...
   *         "tool_calls": [
   *           {
   *             "name": "get_weather",
   *             "args": {
   *               "city": "San Francisco"
   *             },
   *             "type": "tool_call",
   *             "id": "call_0qLS2Jp3MCmaKJ5MAYtr4jJd"
   *           }
   *         ],
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: tools
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The weather in San Francisco is always sunny!",
   *         "name": "get_weather",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The latest update says: The weather in San Francisco is always sunny!\n\nIf you'd like real-time details (current temperature, humidity, wind, and today's forecast), I can pull the latest data for you. Want me to fetch that?",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   */
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, tool } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";
  import z from "zod";

  const getWeather = tool(
    async ({ city }) => {
      return `The weather in ${city} is always sunny!`;
    },
    {
      name: "get_weather",
      description: "Get weather for a given city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [getWeather],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  for await (const chunk of await agent.stream(
    { messages: [{ role: "user", content: "what is the weather in sf" }] },
    { ...config, streamMode: "updates", version: "v2" },
  )) {
    const [step, content] = Object.entries(chunk)[0];
    console.log(`step: ${step}`);
    console.log(`content: ${JSON.stringify(content, null, 2)}`);
  }
  /**
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         // ...
   *         "tool_calls": [
   *           {
   *             "name": "get_weather",
   *             "args": {
   *               "city": "San Francisco"
   *             },
   *             "type": "tool_call",
   *             "id": "call_0qLS2Jp3MCmaKJ5MAYtr4jJd"
   *           }
   *         ],
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: tools
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The weather in San Francisco is always sunny!",
   *         "name": "get_weather",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The latest update says: The weather in San Francisco is always sunny!\n\nIf you'd like real-time details (current temperature, humidity, wind, and today's forecast), I can pull the latest data for you. Want me to fetch that?",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   */
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, tool } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";
  import z from "zod";

  const getWeather = tool(
    async ({ city }) => {
      return `The weather in ${city} is always sunny!`;
    },
    {
      name: "get_weather",
      description: "Get weather for a given city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  const agent = createAgent({
    model: "anthropic:claude-sonnet-4-6",
    tools: [getWeather],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  for await (const chunk of await agent.stream(
    { messages: [{ role: "user", content: "what is the weather in sf" }] },
    { ...config, streamMode: "updates", version: "v2" },
  )) {
    const [step, content] = Object.entries(chunk)[0];
    console.log(`step: ${step}`);
    console.log(`content: ${JSON.stringify(content, null, 2)}`);
  }
  /**
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         // ...
   *         "tool_calls": [
   *           {
   *             "name": "get_weather",
   *             "args": {
   *               "city": "San Francisco"
   *             },
   *             "type": "tool_call",
   *             "id": "call_0qLS2Jp3MCmaKJ5MAYtr4jJd"
   *           }
   *         ],
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: tools
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The weather in San Francisco is always sunny!",
   *         "name": "get_weather",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The latest update says: The weather in San Francisco is always sunny!\n\nIf you'd like real-time details (current temperature, humidity, wind, and today's forecast), I can pull the latest data for you. Want me to fetch that?",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   */
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, tool } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";
  import z from "zod";

  const getWeather = tool(
    async ({ city }) => {
      return `The weather in ${city} is always sunny!`;
    },
    {
      name: "get_weather",
      description: "Get weather for a given city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  const agent = createAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    tools: [getWeather],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  for await (const chunk of await agent.stream(
    { messages: [{ role: "user", content: "what is the weather in sf" }] },
    { ...config, streamMode: "updates", version: "v2" },
  )) {
    const [step, content] = Object.entries(chunk)[0];
    console.log(`step: ${step}`);
    console.log(`content: ${JSON.stringify(content, null, 2)}`);
  }
  /**
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         // ...
   *         "tool_calls": [
   *           {
   *             "name": "get_weather",
   *             "args": {
   *               "city": "San Francisco"
   *             },
   *             "type": "tool_call",
   *             "id": "call_0qLS2Jp3MCmaKJ5MAYtr4jJd"
   *           }
   *         ],
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: tools
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The weather in San Francisco is always sunny!",
   *         "name": "get_weather",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The latest update says: The weather in San Francisco is always sunny!\n\nIf you'd like real-time details (current temperature, humidity, wind, and today's forecast), I can pull the latest data for you. Want me to fetch that?",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   */
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, tool } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";
  import z from "zod";

  const getWeather = tool(
    async ({ city }) => {
      return `The weather in ${city} is always sunny!`;
    },
    {
      name: "get_weather",
      description: "Get weather for a given city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  const agent = createAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools: [getWeather],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  for await (const chunk of await agent.stream(
    { messages: [{ role: "user", content: "what is the weather in sf" }] },
    { ...config, streamMode: "updates", version: "v2" },
  )) {
    const [step, content] = Object.entries(chunk)[0];
    console.log(`step: ${step}`);
    console.log(`content: ${JSON.stringify(content, null, 2)}`);
  }
  /**
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         // ...
   *         "tool_calls": [
   *           {
   *             "name": "get_weather",
   *             "args": {
   *               "city": "San Francisco"
   *             },
   *             "type": "tool_call",
   *             "id": "call_0qLS2Jp3MCmaKJ5MAYtr4jJd"
   *           }
   *         ],
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: tools
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The weather in San Francisco is always sunny!",
   *         "name": "get_weather",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The latest update says: The weather in San Francisco is always sunny!\n\nIf you'd like real-time details (current temperature, humidity, wind, and today's forecast), I can pull the latest data for you. Want me to fetch that?",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   */
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, tool } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";
  import z from "zod";

  const getWeather = tool(
    async ({ city }) => {
      return `The weather in ${city} is always sunny!`;
    },
    {
      name: "get_weather",
      description: "Get weather for a given city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  const agent = createAgent({
    model: "baseten:zai-org/GLM-5",
    tools: [getWeather],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  for await (const chunk of await agent.stream(
    { messages: [{ role: "user", content: "what is the weather in sf" }] },
    { ...config, streamMode: "updates", version: "v2" },
  )) {
    const [step, content] = Object.entries(chunk)[0];
    console.log(`step: ${step}`);
    console.log(`content: ${JSON.stringify(content, null, 2)}`);
  }
  /**
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         // ...
   *         "tool_calls": [
   *           {
   *             "name": "get_weather",
   *             "args": {
   *               "city": "San Francisco"
   *             },
   *             "type": "tool_call",
   *             "id": "call_0qLS2Jp3MCmaKJ5MAYtr4jJd"
   *           }
   *         ],
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: tools
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The weather in San Francisco is always sunny!",
   *         "name": "get_weather",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The latest update says: The weather in San Francisco is always sunny!\n\nIf you'd like real-time details (current temperature, humidity, wind, and today's forecast), I can pull the latest data for you. Want me to fetch that?",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   */
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, tool } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";
  import z from "zod";

  const getWeather = tool(
    async ({ city }) => {
      return `The weather in ${city} is always sunny!`;
    },
    {
      name: "get_weather",
      description: "Get weather for a given city.",
      schema: z.object({
        city: z.string(),
      }),
    },
  );

  const agent = createAgent({
    model: "ollama:devstral-2",
    tools: [getWeather],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  for await (const chunk of await agent.stream(
    { messages: [{ role: "user", content: "what is the weather in sf" }] },
    { ...config, streamMode: "updates", version: "v2" },
  )) {
    const [step, content] = Object.entries(chunk)[0];
    console.log(`step: ${step}`);
    console.log(`content: ${JSON.stringify(content, null, 2)}`);
  }
  /**
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         // ...
   *         "tool_calls": [
   *           {
   *             "name": "get_weather",
   *             "args": {
   *               "city": "San Francisco"
   *             },
   *             "type": "tool_call",
   *             "id": "call_0qLS2Jp3MCmaKJ5MAYtr4jJd"
   *           }
   *         ],
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: tools
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The weather in San Francisco is always sunny!",
   *         "name": "get_weather",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   * step: model_request
   * content: {
   *   "messages": [
   *     {
   *       "kwargs": {
   *         "content": "The latest update says: The weather in San Francisco is always sunny!\n\nIf you'd like real-time details (current temperature, humidity, wind, and today's forecast), I can pull the latest data for you. Want me to fetch that?",
   *         // ...
   *       }
   *     }
   *   ]
   * }
   */
  ```
</CodeGroup>

<Note>
  Persisting conversation history with `thread_id` requires the agent to be configured with a [checkpointer](/oss/javascript/langchain/long-term-memory). On [LangSmith deployments](/langsmith/deployment) a checkpointer is provisioned automatically. Locally, pass one explicitly, for example `createAgent({ ..., checkpointer: new MemorySaver() })`. The remaining snippets on this page omit `thread_id` for brevity, but you should pass it in production.
</Note>

## LLM tokens

To stream tokens as they are produced by the LLM, use `streamMode: "messages"`:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import z from "zod";
import { createAgent, tool } from "langchain";

const getWeather = tool(
    async ({ city }) => {
        return `The weather in ${city} is always sunny!`;
    },
    {
        name: "get_weather",
        description: "Get weather for a given city.",
        schema: z.object({
        city: z.string(),
        }),
    }
);

const agent = createAgent({
    model: "gpt-5.4-mini",
    tools: [getWeather],
});

for await (const [token, metadata] of await agent.stream(
    { messages: [{ role: "user", content: "what is the weather in sf" }] },
    { streamMode: "messages" }
)) {
    console.log(`node: ${metadata.langgraph_node}`);
    console.log(`content: ${JSON.stringify(token.contentBlocks, null, 2)}`);
}
```

## Custom updates

To stream updates from tools as they are executed, you can use the `writer` parameter from the configuration.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import z from "zod";
import { tool, createAgent } from "langchain";
import { LangGraphRunnableConfig } from "@langchain/langgraph";

const getWeather = tool(
    async (input, config: LangGraphRunnableConfig) => {
        // Stream any arbitrary data
        config.writer?.(`Looking up data for city: ${input.city}`);
        // ... fetch city data
        config.writer?.(`Acquired data for city: ${input.city}`);
        return `It's always sunny in ${input.city}!`;
    },
    {
        name: "get_weather",
        description: "Get weather for a given city.",
        schema: z.object({
        city: z.string().describe("The city to get weather for."),
        }),
    }
);

const agent = createAgent({
    model: "gpt-5.4-mini",
    tools: [getWeather],
});

for await (const chunk of await agent.stream(
    { messages: [{ role: "user", content: "what is the weather in sf" }] },
    { streamMode: "custom" }
)) {
    console.log(chunk);
}
```

```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
Looking up data for city: San Francisco
Acquired data for city: San Francisco
```

<Note>
  If you add the `writer` parameter to your tool, you won't be able to invoke the tool outside of a LangGraph execution context without providing a writer function.
</Note>

## Stream multiple modes

You can specify multiple streaming modes by passing streamMode as an array: `streamMode: ["updates", "messages", "custom"]`.

The streamed outputs will be tuples of `[mode, chunk]` where `mode` is the name of the stream mode and `chunk` is the data streamed by that mode.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import z from "zod";
import { tool, createAgent } from "langchain";
import { LangGraphRunnableConfig } from "@langchain/langgraph";

const getWeather = tool(
    async (input, config: LangGraphRunnableConfig) => {
        // Stream any arbitrary data
        config.writer?.(`Looking up data for city: ${input.city}`);
        // ... fetch city data
        config.writer?.(`Acquired data for city: ${input.city}`);
        return `It's always sunny in ${input.city}!`;
    },
    {
        name: "get_weather",
        description: "Get weather for a given city.",
        schema: z.object({
        city: z.string().describe("The city to get weather for."),
        }),
    }
);

const agent = createAgent({
    model: "gpt-5.4-mini",
    tools: [getWeather],
});

for await (const [streamMode, chunk] of await agent.stream(
    { messages: [{ role: "user", content: "what is the weather in sf" }] },
    { streamMode: ["updates", "messages", "custom"] }
)) {
    console.log(`${streamMode}: ${JSON.stringify(chunk, null, 2)}`);
}
```

## Common patterns

Below are examples showing common use cases for streaming.

### Streaming thinking / reasoning tokens

Some models perform internal reasoning before producing a final answer. You can stream these thinking / reasoning tokens as they're generated by filtering [standard content blocks](/oss/javascript/langchain/messages#standard-content-blocks) for the `type` `"reasoning"`.

<Note>
  Reasoning output must be enabled on the model.

  See the [reasoning section](/oss/javascript/langchain/models#reasoning) and your [provider's integration page](/oss/javascript/integrations/providers/overview) for configuration details.

  To quickly check a model's reasoning support, see [models.dev](https://models.dev).
</Note>

To stream thinking tokens from an agent, use `streamMode: "messages"` and filter for reasoning content blocks. Use a model instance (e.g. `ChatAnthropic`) with extended thinking enabled when the model supports it:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import z from "zod";
import { createAgent, tool } from "langchain";
import { ChatAnthropic } from "@langchain/anthropic";

const getWeather = tool(
  async ({ city }) => {
    return `It's always sunny in ${city}!`;
  },
  {
    name: "get_weather",
    description: "Get weather for a given city.",
    schema: z.object({ city: z.string() }),
  },
);

const agent = createAgent({
  model: new ChatAnthropic({
    model: "claude-sonnet-4-6",
    thinking: { type: "enabled", budget_tokens: 5000 },
  }),
  tools: [getWeather],
});

for await (const [token, metadata] of await agent.stream(
  { messages: [{ role: "user", content: "What is the weather in SF?" }] },
  { streamMode: "messages" }, // [!code highlight]
)) {
  if (!token.contentBlocks) continue;
  const reasoning = token.contentBlocks.filter((b) => b.type === "reasoning");
  const text = token.contentBlocks.filter((b) => b.type === "text");
  if (reasoning.length) {
    process.stdout.write(`[thinking] ${reasoning[0].reasoning}`);
  }
  if (text.length) {
    process.stdout.write(text[0].text);
  }
}
```

```shell title="Output" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
[thinking] The user is asking about the weather in San Francisco. I have a tool
[thinking]  available to get this information. Let me call the get_weather tool
[thinking]  with "San Francisco" as the city parameter.
The weather in San Francisco is: It's always sunny in San Francisco!
```

This works the same way regardless of the model provider—LangChain normalizes provider-specific formats (Anthropic `thinking` blocks, OpenAI `reasoning` summaries, etc.) into a standard `"reasoning"` content block type via the [`content_blocks`](/oss/javascript/langchain/messages#standard-content-blocks) property.

To stream reasoning tokens directly from a chat model (without an agent), see [streaming with chat models](/oss/javascript/langchain/models#reasoning).

## Disable streaming

In some applications you might need to disable streaming of individual tokens for a given model. This is useful when:

* Working with [multi-agent](/oss/javascript/langchain/multi-agent) systems to control which agents stream their output
* Mixing models that support streaming with those that do not
* Deploying to [LangSmith](/langsmith/observability) and wanting to prevent certain model outputs from being streamed to the client

Set `streaming: false` when initializing the model.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  model: "gpt-5.5",
  streaming: false,  // [!code highlight]
});
```

<Tip>
  When deploying to LangSmith, set `streaming=False` on any models whose output you don't want streamed to the client. This is configured in your graph code before deployment.
</Tip>

<Note>
  Not all chat model integrations support the `streaming` parameter. If your model doesn't support it, use `disableStreaming: true` instead. This parameter is available on all chat models via the base class.
</Note>

See the [LangGraph streaming guide](/oss/javascript/langgraph/streaming#disable-streaming-for-specific-chat-models) for more details.

## Related

* [Frontend streaming](/oss/javascript/langchain/frontend/overview)—Build React UIs with [`useStream`](https://reference.langchain.com/javascript/langchain-react/index/useStream) for real-time agent interactions
* [Streaming with chat models](/oss/javascript/langchain/models#stream)—Stream tokens directly from a chat model without using an agent or graph
* [Reasoning with chat models](/oss/javascript/langchain/models#reasoning)—Configure and access reasoning output from chat models
* [Standard content blocks](/oss/javascript/langchain/messages#standard-content-blocks)—Understand the normalized content block format used for reasoning, text, and other content types
* [Streaming with human-in-the-loop](/oss/javascript/langchain/human-in-the-loop#streaming-with-human-in-the-loop)—Stream agent progress while handling interrupts for human review
* [LangGraph streaming](/oss/javascript/langgraph/streaming)—Advanced streaming options including `values`, `debug` modes, and subgraph streaming

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/streaming.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Structured output
Source: https://docs.langchain.com/oss/javascript/langchain/structured-output

Structured output allows agents to return data in a specific, predictable format. Instead of parsing natural language responses, you get typed structured data.

<Tip>
  This page covers structured output with agents using `createAgent`. To use structured output directly on a model (outside of agents), see [Models - Structured output](/oss/javascript/langchain/models#structured-output).
</Tip>

LangChain's prebuilt ReAct agent `createAgent` handles structured output automatically. The user sets their desired structured output schema, and when the model generates the structured data, it's captured, validated, and returned in the `structuredResponse` key of the agent's state.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
type ResponseFormat = (
    | ZodSchema<StructuredResponseT> // a Zod schema
    | StandardSchema<StructuredResponseT> // any Standard Schema library
    | Record<string, unknown> // a JSON Schema
)

const agent = createAgent({
    // ...
    responseFormat: ResponseFormat | ResponseFormat[]
})
```

## Response format

Controls how the agent returns structured data. You can provide a Zod schema, any [Standard Schema](https://standardschema.dev/)-compatible schema, or a JSON Schema object. By default, the agent uses a tool calling strategy, in which the output is created by an additional tool call. Certain models support native structured output, in which case the agent will use that strategy instead.

You can control the behavior by wrapping `ResponseFormat` in a `toolStrategy` or `providerStrategy` function call:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { toolStrategy, providerStrategy } from "langchain";

const agent = createAgent({
    // use a provider strategy if supported by the model
    responseFormat: providerStrategy(z.object({ ... }))
    // or enforce a tool strategy
    responseFormat: toolStrategy(z.object({ ... }))
})
```

The structured response is returned in the `structuredResponse` key of the agent's final state.

<Tip>
  Support for native structured output features is read dynamically from the model's [profile data](/oss/javascript/langchain/models#model-profiles) if using `langchain>=1.1`. If data are not available, use another condition or specify manually:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const customProfile: ModelProfile = {
      structuredOutput: true,
      // ...
  }
  const model = await initChatModel("...", { profile: customProfile });
  ```

  If tools are specified, the model must support simultaneous use of tools and structured output.
</Tip>

## Provider strategy

Some model providers support structured output natively through their APIs (e.g. OpenAI, xAI (Grok), Gemini, Anthropic (Claude)). This is the most reliable method when available.

To use this strategy, configure a `ProviderStrategy`:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function providerStrategy<StructuredResponseT>(
    schema: ZodSchema<StructuredResponseT> | SerializableSchema | JsonSchemaFormat
): ProviderStrategy<StructuredResponseT>
```

<ParamField>
  The schema defining the structured output format. Supports:

  * **Zod Schema**: A zod schema
  * **Standard Schema**: Any schema implementing the [Standard Schema](https://standardschema.dev/) spec
  * **JSON Schema**: A JSON schema object
</ParamField>

LangChain automatically uses `ProviderStrategy` when you pass a schema type directly to `createAgent.responseFormat` and the model supports native structured output:

<CodeGroup>
  ```ts Zod Schema theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { createAgent, providerStrategy } from "langchain";

  const ContactInfo = z.object({
      name: z.string().describe("The name of the person"),
      email: z.string().describe("The email address of the person"),
      phone: z.string().describe("The phone number of the person"),
  });

  const agent = createAgent({
      model: "gpt-5.5",
      tools: [],
      responseFormat: providerStrategy(ContactInfo)
  });

  const result = await agent.invoke({
      messages: [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
  });

  console.log(result.structuredResponse);
  // { name: "John Doe", email: "john@example.com", phone: "(555) 123-4567" }
  ```

  ```ts Standard Schema theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as v from "valibot";
  import { toStandardJsonSchema } from "@valibot/to-json-schema";
  import { createAgent, providerStrategy } from "langchain";

  const ContactInfo = toStandardJsonSchema(
      v.object({
          name: v.pipe(v.string(), v.description("The name of the person")),
          email: v.pipe(v.string(), v.description("The email address of the person")),
          phone: v.pipe(v.string(), v.description("The phone number of the person")),
      })
  );

  const agent = createAgent({
      model: "gpt-5.5",
      tools: [],
      responseFormat: providerStrategy(ContactInfo)
  });

  const result = await agent.invoke({
      messages: [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
  });

  console.log(result.structuredResponse);
  // { name: "John Doe", email: "john@example.com", phone: "(555) 123-4567" }
  ```

  ```ts JSON Schema theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, providerStrategy } from "langchain";

  const contactInfoSchema = {
      "type": "object",
      "description": "Contact information for a person.",
      "properties": {
          "name": {"type": "string", "description": "The name of the person"},
          "email": {"type": "string", "description": "The email address of the person"},
          "phone": {"type": "string", "description": "The phone number of the person"}
      },
      "required": ["name", "email", "phone"]
  }

  const agent = createAgent({
      model: "gpt-5.5",
      tools: [],
      responseFormat: providerStrategy(contactInfoSchema)
  });

  const result = await agent.invoke({
      messages: [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
  });

  console.log(result.structuredResponse);
  // { name: "John Doe", email: "john@example.com", phone: "(555) 123-4567" }
  ```
</CodeGroup>

Provider-native structured output provides high reliability and strict validation because the model provider enforces the schema. Use it when available.

<Note>
  If the provider natively supports structured output for your model choice, it is functionally equivalent to write `responseFormat: contactInfoSchema` instead of `responseFormat: providerStrategy(contactInfoSchema)`.

  In either case, if structured output is not supported, the agent will fall back to a tool calling strategy.
</Note>

## Tool calling strategy

For models that don't support native structured output, LangChain uses tool calling to achieve the same result. This works with all models that support tool calling (most modern models).

To use this strategy, configure a `ToolStrategy`:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
function toolStrategy<StructuredResponseT>(
    responseFormat:
        | JsonSchemaFormat
        | ZodSchema<StructuredResponseT>
        | SerializableSchema
        | (ZodSchema<StructuredResponseT> | SerializableSchema | JsonSchemaFormat)[]
    options?: ToolStrategyOptions
): ToolStrategy<StructuredResponseT>
```

<ParamField>
  The schema defining the structured output format. Supports:

  * **Zod Schema**: A zod schema
  * **Standard Schema**: Any schema implementing the [Standard Schema](https://standardschema.dev/) spec
  * **JSON Schema**: A JSON schema object
</ParamField>

<ParamField>
  Custom content for the tool message returned when structured output is generated.
  If not provided, defaults to a message showing the structured response data.
</ParamField>

<ParamField>
  Options parameter containing an optional `handleError` parameter for customizing the error handling strategy.

  * **`true`**: Catch all errors with default error template (default)
  * **`False`**: No retry, let exceptions propagate
  * **`(error: ToolStrategyError) => string | Promise<string>`**: retry with the provided message or throw the error
</ParamField>

<CodeGroup>
  ```ts Zod Schema theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { createAgent, toolStrategy } from "langchain";

  const ProductReview = z.object({
      rating: z.number().min(1).max(5).optional(),
      sentiment: z.enum(["positive", "negative"]),
      keyPoints: z.array(z.string()).describe("The key points of the review. Lowercase, 1-3 words each."),
  });

  const agent = createAgent({
      model: "gpt-5.5",
      tools: [],
      responseFormat: toolStrategy(ProductReview)
  })

  const result = await agent.invoke({
      "messages": [{"role": "user", "content": "Analyze this review: 'Great product: 5 out of 5 stars. Fast shipping, but expensive'"}]
  })

  console.log(result.structuredResponse);
  // { "rating": 5, "sentiment": "positive", "keyPoints": ["fast shipping", "expensive"] }
  ```

  ```ts Standard Schema theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as v from "valibot";
  import { toStandardJsonSchema } from "@valibot/to-json-schema";
  import { createAgent, toolStrategy } from "langchain";

  const ProductReview = toStandardJsonSchema(
      v.object({
          rating: v.optional(v.pipe(v.number(), v.minValue(1), v.maxValue(5))),
          sentiment: v.picklist(["positive", "negative"]),
          keyPoints: v.pipe(v.array(v.string()), v.description("The key points of the review. Lowercase, 1-3 words each.")),
      })
  );

  const agent = createAgent({
      model: "gpt-5.5",
      tools: [],
      responseFormat: toolStrategy(ProductReview)
  })

  const result = await agent.invoke({
      messages: [{"role": "user", "content": "Analyze this review: 'Great product: 5 out of 5 stars. Fast shipping, but expensive'"}]
  })

  console.log(result.structuredResponse);
  // { "rating": 5, "sentiment": "positive", "keyPoints": ["fast shipping", "expensive"] }
  ```

  ```ts JSON Schema theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, toolStrategy } from "langchain";

  const productReviewSchema = {
      "type": "object",
      "description": "Analysis of a product review.",
      "properties": {
          "rating": {
              "type": ["integer", "null"],
              "description": "The rating of the product (1-5)",
              "minimum": 1,
              "maximum": 5
          },
          "sentiment": {
              "type": "string",
              "enum": ["positive", "negative"],
              "description": "The sentiment of the review"
          },
          "key_points": {
              "type": "array",
              "items": {"type": "string"},
              "description": "The key points of the review"
          }
      },
      "required": ["sentiment", "key_points"]
  }

  const agent = createAgent({
      model: "gpt-5.5",
      tools: [],
      responseFormat: toolStrategy(productReviewSchema)
  });

  const result = await agent.invoke({
      messages: [{"role": "user", "content": "Analyze this review: 'Great product: 5 out of 5 stars. Fast shipping, but expensive'"}]
  })

  console.log(result.structuredResponse);
  // { "rating": 5, "sentiment": "positive", "keyPoints": ["fast shipping", "expensive"] }
  ```

  ```ts Union Types theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { createAgent, toolStrategy } from "langchain";

  const ProductReview = z.object({
      rating: z.number().min(1).max(5).optional(),
      sentiment: z.enum(["positive", "negative"]),
      keyPoints: z.array(z.string()).describe("The key points of the review. Lowercase, 1-3 words each."),
  });

  const CustomerComplaint = z.object({
      issueType: z.enum(["product", "service", "shipping", "billing"]),
      severity: z.enum(["low", "medium", "high"]),
      description: z.string().describe("Brief description of the complaint"),
  });

  const agent = createAgent({
      model: "gpt-5.5",
      tools: [],
      responseFormat: toolStrategy([ProductReview, CustomerComplaint])
  });

  const result = await agent.invoke({
      messages: [{"role": "user", "content": "Analyze this review: 'Great product: 5 out of 5 stars. Fast shipping, but expensive'"}]
  })

  console.log(result.structuredResponse);
  // { "rating": 5, "sentiment": "positive", "keyPoints": ["fast shipping", "expensive"] }
  ```
</CodeGroup>

### Custom tool message content

The `toolMessageContent` parameter allows you to customize the message that appears in the conversation history when structured output is generated:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as z from "zod";
import { createAgent, toolStrategy } from "langchain";

const MeetingAction = z.object({
    task: z.string().describe("The specific task to be completed"),
    assignee: z.string().describe("Person responsible for the task"),
    priority: z.enum(["low", "medium", "high"]).describe("Priority level"),
});

const agent = createAgent({
    model: "gpt-5.5",
    tools: [],
    responseFormat: toolStrategy(MeetingAction, {
        toolMessageContent: "Action item captured and added to meeting notes!"
    })
});

const result = await agent.invoke({
    messages: [{"role": "user", "content": "From our meeting: Sarah needs to update the project timeline as soon as possible"}]
});

console.log(result);
/**
 * {
 *   messages: [
 *     { role: "user", content: "From our meeting: Sarah needs to update the project timeline as soon as possible" },
 *     { role: "assistant", content: "Action item captured and added to meeting notes!", tool_calls: [ { name: "MeetingAction", args: { task: "update the project timeline", assignee: "Sarah", priority: "high" }, id: "call_456" } ] },
 *     { role: "tool", content: "Action item captured and added to meeting notes!", tool_call_id: "call_456", name: "MeetingAction" }
 *   ],
 *   structuredResponse: { task: "update the project timeline", assignee: "Sarah", priority: "high" }
 * }
 */
```

Without `toolMessageContent`, we'd see:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
