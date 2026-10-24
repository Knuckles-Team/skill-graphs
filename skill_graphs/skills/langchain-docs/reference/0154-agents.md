# Agents
Source: https://docs.langchain.com/oss/javascript/langchain/agents

An agent is a model calling tools in a loop until a given task is complete.

<img alt="Core agent loop diagram" />

<Note>
  **Agent = Model + Harness**

  The job of a harness: get the model the right context at the right time for the given task.
</Note>

A harness is everything around that loop: the model, its prompt, its tools, and any middleware that shapes its behavior.

[`create_agent`](https://reference.langchain.com/javascript/langchain/index/createAgent) is a highly configurable harness. At its simplest:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent } from "langchain";

const agent = createAgent({ model: "openai:gpt-5.5", tools });
```

Configure the basics directly — `model=`, `tools=`, `system_prompt=`. For more advanced capabilities, extend the harness with [middleware](#configure-the-harness).

## Core components

### Model

Pass a model identifier string (`"provider:model"`) or an initialized model instance. See [Models](/oss/javascript/langchain/models) for parameters, provider setup, and dynamic model selection.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent } from "langchain";

const agent = createAgent({ model: "openai:gpt-5.5", tools });
```

### Tools

Pass any Python callable, LangChain tool, or tool dict. See [Tools](/oss/javascript/langchain/tools) for tool definition, context access, and dynamic tool selection.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent, tool } from "langchain";
import * as z from "zod";

const search = tool(({ query }) => `Results for: ${query}`, {
  name: "search",
  description: "Search for information",
  schema: z.object({ query: z.string() }),
});

const agent = createAgent({ model: "openai:gpt-5.5", tools: [search] });
```

### System prompt

Shape how the agent approaches tasks. Accepts a string or `SystemMessage`. For dynamic prompts at runtime, use [middleware](/oss/javascript/langchain/middleware).

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const agent = createAgent({
  model: "openai:gpt-5.5",
  tools,
  systemPrompt: "You are a helpful assistant. Be concise and accurate.",
});
```

### Structured output

Return a validated schema from the agent using `response_format=`. See [Structured output](/oss/javascript/langchain/structured-output) for strategies and examples.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import * as z from "zod";

const Answer = z.object({ summary: z.string(), confidence: z.number() });

const agent = createAgent({ model: "openai:gpt-5.5", tools, responseFormat: Answer });
const result = await agent.invoke({ messages: [{ role: "user", content: "Summarize AI trends" }] });
result.structuredResponse; // { summary: ..., confidence: ... }
```

### Name

Optional identifier used as the node name when embedding this agent as a subgraph in [multi-agent](/oss/javascript/langchain/multi-agent) systems.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const agent = createAgent({ model: "openai:gpt-5.5", tools, name: "research_assistant" });
```

<Tip>
  To extend the agent's state schema with custom fields, use [`state_schema`](/oss/javascript/langchain/long-term-memory) on `create_agent` or define it via middleware. See [Memory](/oss/javascript/langchain/long-term-memory) for details.
</Tip>

## Invocation

<Tip>
  Trace each step of this loop, debug tool calls, and evaluate agent outputs with [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langchain-agents). Follow the [tracing quickstart](/langsmith/trace-with-langchain) to get set up. We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.
</Tip>

You can invoke an agent by passing an update to its [`State`](/oss/javascript/langgraph/graph-api#state). All agents include a [sequence of messages](/oss/javascript/langgraph/use-graph-api#messagesvalue) in their state; to invoke the agent, pass a new message along with a `thread_id` so the agent can persist and resume conversation history:

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const agent = createAgent({
    model: "google-genai:gemini-3.5-flash",
    tools: [],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  let result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    config,
  );

  // A follow-up turn on the same conversation: reuse the same thread_id to keep history
  result = await agent.invoke(
    { messages: [{ role: "user", content: "What about tomorrow?" }] },
    config,
  );
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  let result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    config,
  );

  // A follow-up turn on the same conversation: reuse the same thread_id to keep history
  result = await agent.invoke(
    { messages: [{ role: "user", content: "What about tomorrow?" }] },
    config,
  );
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const agent = createAgent({
    model: "anthropic:claude-sonnet-4-6",
    tools: [],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  let result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    config,
  );

  // A follow-up turn on the same conversation: reuse the same thread_id to keep history
  result = await agent.invoke(
    { messages: [{ role: "user", content: "What about tomorrow?" }] },
    config,
  );
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const agent = createAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    tools: [],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  let result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    config,
  );

  // A follow-up turn on the same conversation: reuse the same thread_id to keep history
  result = await agent.invoke(
    { messages: [{ role: "user", content: "What about tomorrow?" }] },
    config,
  );
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const agent = createAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools: [],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  let result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    config,
  );

  // A follow-up turn on the same conversation: reuse the same thread_id to keep history
  result = await agent.invoke(
    { messages: [{ role: "user", content: "What about tomorrow?" }] },
    config,
  );
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const agent = createAgent({
    model: "baseten:zai-org/GLM-5",
    tools: [],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  let result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    config,
  );

  // A follow-up turn on the same conversation: reuse the same thread_id to keep history
  result = await agent.invoke(
    { messages: [{ role: "user", content: "What about tomorrow?" }] },
    config,
  );
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const agent = createAgent({
    model: "ollama:devstral-2",
    tools: [],
    checkpointer: new MemorySaver(),
  });

  const config = { configurable: { thread_id: crypto.randomUUID() } };

  let result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    config,
  );

  // A follow-up turn on the same conversation: reuse the same thread_id to keep history
  result = await agent.invoke(
    { messages: [{ role: "user", content: "What about tomorrow?" }] },
    config,
  );
  ```
</CodeGroup>

<Note>
  Persisting conversation history with `thread_id` requires the agent to be configured with a [checkpointer](/oss/javascript/langchain/long-term-memory). When deployed on [LangSmith](/langsmith/deployment), a checkpointer is provisioned automatically. Locally, pass one explicitly, for example `create_agent(..., checkpointer=InMemorySaver())`.
</Note>

If you also need to pass per-run configuration (such as a user ID, API keys, or feature flags) to tools and middleware, pass it as `context` alongside the config. Define the shape of that data with `contextSchema` and access it through `runtime.context`:

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const contextSchema = z.object({
    user_id: z.string(),
  });

  const agent = createAgent({
    model: "google-genai:gemini-3.5-flash",
    tools: [],
    contextSchema,
    checkpointer: new MemorySaver(),
  });

  const result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    {
      configurable: { thread_id: crypto.randomUUID() },
      context: { user_id: "user-123" },
    },
  );
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const contextSchema = z.object({
    user_id: z.string(),
  });

  const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [],
    contextSchema,
    checkpointer: new MemorySaver(),
  });

  const result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    {
      configurable: { thread_id: crypto.randomUUID() },
      context: { user_id: "user-123" },
    },
  );
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const contextSchema = z.object({
    user_id: z.string(),
  });

  const agent = createAgent({
    model: "anthropic:claude-sonnet-4-6",
    tools: [],
    contextSchema,
    checkpointer: new MemorySaver(),
  });

  const result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    {
      configurable: { thread_id: crypto.randomUUID() },
      context: { user_id: "user-123" },
    },
  );
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const contextSchema = z.object({
    user_id: z.string(),
  });

  const agent = createAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    tools: [],
    contextSchema,
    checkpointer: new MemorySaver(),
  });

  const result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    {
      configurable: { thread_id: crypto.randomUUID() },
      context: { user_id: "user-123" },
    },
  );
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const contextSchema = z.object({
    user_id: z.string(),
  });

  const agent = createAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools: [],
    contextSchema,
    checkpointer: new MemorySaver(),
  });

  const result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    {
      configurable: { thread_id: crypto.randomUUID() },
      context: { user_id: "user-123" },
    },
  );
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const contextSchema = z.object({
    user_id: z.string(),
  });

  const agent = createAgent({
    model: "baseten:zai-org/GLM-5",
    tools: [],
    contextSchema,
    checkpointer: new MemorySaver(),
  });

  const result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    {
      configurable: { thread_id: crypto.randomUUID() },
      context: { user_id: "user-123" },
    },
  );
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import * as z from "zod";
  import { AIMessage } from "@langchain/core/messages";
  import { createAgent } from "langchain";
  import { MemorySaver } from "@langchain/langgraph";

  const contextSchema = z.object({
    user_id: z.string(),
  });

  const agent = createAgent({
    model: "ollama:devstral-2",
    tools: [],
    contextSchema,
    checkpointer: new MemorySaver(),
  });

  const result = await agent.invoke(
    {
      messages: [
        { role: "user", content: "What's the weather in San Francisco?" },
      ],
    },
    {
      configurable: { thread_id: crypto.randomUUID() },
      context: { user_id: "user-123" },
    },
  );
  ```
</CodeGroup>

`thread_id` scopes the *conversation* (message history, checkpoints), while `context` carries *per-run* data your tools and middleware read at invocation time. Both are commonly passed together. See [tool context](/oss/javascript/langchain/tools#context) and [Runtime](/oss/javascript/langchain/runtime) for more.

### Streaming

We've seen how the agent can be called with `invoke` to get a final response. If the agent executes multiple steps, this may take a while. To show intermediate progress, we can stream back messages as they occur.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const stream = await agent.stream(
  {
    messages: [{
      role: "user",
      content: "Search for AI news and summarize the findings"
    }],
  },
  { streamMode: "values" }
);

for await (const chunk of stream) {
  // Each chunk contains the full state at that point
  const latestMessage = chunk.messages.at(-1);
  if (latestMessage?.content) {
    console.log(`Agent: ${latestMessage.content}`);
  } else if (latestMessage?.tool_calls) {
    const toolCallNames = latestMessage.tool_calls.map((tc) => tc.name);
    console.log(`Calling tools: ${toolCallNames.join(", ")}`);
  }
}
```

<Tip>
  For more details on streaming, see [Streaming](/oss/javascript/langchain/streaming).
</Tip>

## Configure the harness

`create_agent` is highly extensible. Middleware is the primitive for customization: each piece handles one concern, hooks into the agent loop at the right moment, and composes freely with any other. Take exactly what your use case needs — skip the rest.

Common patterns are pre-built as first-class middleware. Anything custom is [one middleware away](/oss/javascript/langchain/middleware/custom).

<img alt="Middleware lifecycle diagram" />

As agents take on complex work, they need support across a few key areas. The middleware ecosystem covers each:

<CardGroup>
  <Card title="Execution environment" icon="bolt" href="#execution-environment">
    Tools, filesystem, sandboxes, and code execution
  </Card>

  <Card title="Context management" icon="database" href="#context-management">
    Summarization, memory, skills, and prompt caching
  </Card>

  <Card title="Planning and delegation" icon="sitemap" href="#planning-and-delegation">
    Todo lists and subagents for parallel, isolated work
  </Card>

  <Card title="Fault tolerance" icon="shield" href="#fault-tolerance">
    Retries, fallbacks, and call limits
  </Card>

  <Card title="Guardrails" icon="lock" href="#guardrails">
    PII detection and content controls
  </Card>

  <Card title="Steering" icon="user" href="#steering">
    Human-in-the-loop approval before high-impact actions
  </Card>
</CardGroup>

### Execution environment

Agents are useful when they can take action — not just generate text. The execution environment gives the agent a workspace: tools it can call, a filesystem for reading and writing files across turns, and code execution for running scripts or shell commands.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createAgent } from "langchain";
import { FilesystemMiddleware, StateBackend } from "deepagents";

const agent = createAgent({
  model: "anthropic:claude-sonnet-4-6",
  tools: [search],
  middleware: [new FilesystemMiddleware({ backend: new StateBackend() })],
});
```

See [`FilesystemMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createFilesystemMiddleware), [Sandboxes](/oss/javascript/deepagents/sandboxes), [Interpreters](/oss/javascript/deepagents/interpreters).

### Context management

Every model call has a fixed context window. As an agent runs — accumulating history, tool results, and intermediate steps — that window fills. Summarization compresses history before overflow hits; memory loads persistent instructions at startup so knowledge carries across sessions; skills surface domain knowledge on demand rather than loading everything upfront.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { FilesystemMiddleware, MemoryMiddleware, SkillsMiddleware, SummarizationMiddleware, StateBackend } from "deepagents";

const backend = new StateBackend();
const model = "anthropic:claude-sonnet-4-6";

const agent = createAgent({
  model,
  tools: [search],
  middleware: [
    new FilesystemMiddleware({ backend }),
    new SummarizationMiddleware({ model, backend }),
    new MemoryMiddleware({ backend, sources: ["./AGENTS.md"] }),
    new SkillsMiddleware({ backend, sources: ["./skills/"] }),
  ],
});
```

See [`SummarizationMiddleware`](https://reference.langchain.com/javascript/langchain/index/summarizationMiddleware), [`MemoryMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createMemoryMiddleware), [`SkillsMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSkillsMiddleware), [Context engineering](/oss/javascript/deepagents/context-engineering).

### Planning and delegation

Complex tasks often exceed what one context window can handle. Delegation lets the main agent break work into pieces, hand them to subagents that each run in their own isolated context, and stay focused on coordination rather than execution. Work can run in parallel; the main agent's context stays clean.

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, todoListMiddleware, tool } from "langchain";
  import {
    createFilesystemMiddleware,
    createSubAgentMiddleware,
    StateBackend,
  } from "deepagents";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const backend = new StateBackend();

  const agent = createAgent({
    model: "google-genai:gemini-3.5-flash",
    tools: [search],
    middleware: [
      createFilesystemMiddleware({ backend }),
      todoListMiddleware(),
      createSubAgentMiddleware({
        defaultModel: "anthropic:claude-sonnet-4-6",
        defaultTools: [],
        subagents: [
          {
            name: "researcher",
            description: "Searches and returns a structured summary.",
            systemPrompt:
              "Use the search tool to research the question and summarize key points.",
            tools: [search],
            model: "anthropic:claude-sonnet-4-6",
            middleware: [],
          },
        ],
      }),
    ],
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, todoListMiddleware, tool } from "langchain";
  import {
    createFilesystemMiddleware,
    createSubAgentMiddleware,
    StateBackend,
  } from "deepagents";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const backend = new StateBackend();

  const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [search],
    middleware: [
      createFilesystemMiddleware({ backend }),
      todoListMiddleware(),
      createSubAgentMiddleware({
        defaultModel: "anthropic:claude-sonnet-4-6",
        defaultTools: [],
        subagents: [
          {
            name: "researcher",
            description: "Searches and returns a structured summary.",
            systemPrompt:
              "Use the search tool to research the question and summarize key points.",
            tools: [search],
            model: "anthropic:claude-sonnet-4-6",
            middleware: [],
          },
        ],
      }),
    ],
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, todoListMiddleware, tool } from "langchain";
  import {
    createFilesystemMiddleware,
    createSubAgentMiddleware,
    StateBackend,
  } from "deepagents";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const backend = new StateBackend();

  const agent = createAgent({
    model: "anthropic:claude-sonnet-4-6",
    tools: [search],
    middleware: [
      createFilesystemMiddleware({ backend }),
      todoListMiddleware(),
      createSubAgentMiddleware({
        defaultModel: "anthropic:claude-sonnet-4-6",
        defaultTools: [],
        subagents: [
          {
            name: "researcher",
            description: "Searches and returns a structured summary.",
            systemPrompt:
              "Use the search tool to research the question and summarize key points.",
            tools: [search],
            model: "anthropic:claude-sonnet-4-6",
            middleware: [],
          },
        ],
      }),
    ],
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, todoListMiddleware, tool } from "langchain";
  import {
    createFilesystemMiddleware,
    createSubAgentMiddleware,
    StateBackend,
  } from "deepagents";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const backend = new StateBackend();

  const agent = createAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    tools: [search],
    middleware: [
      createFilesystemMiddleware({ backend }),
      todoListMiddleware(),
      createSubAgentMiddleware({
        defaultModel: "anthropic:claude-sonnet-4-6",
        defaultTools: [],
        subagents: [
          {
            name: "researcher",
            description: "Searches and returns a structured summary.",
            systemPrompt:
              "Use the search tool to research the question and summarize key points.",
            tools: [search],
            model: "anthropic:claude-sonnet-4-6",
            middleware: [],
          },
        ],
      }),
    ],
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, todoListMiddleware, tool } from "langchain";
  import {
    createFilesystemMiddleware,
    createSubAgentMiddleware,
    StateBackend,
  } from "deepagents";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const backend = new StateBackend();

  const agent = createAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools: [search],
    middleware: [
      createFilesystemMiddleware({ backend }),
      todoListMiddleware(),
      createSubAgentMiddleware({
        defaultModel: "anthropic:claude-sonnet-4-6",
        defaultTools: [],
        subagents: [
          {
            name: "researcher",
            description: "Searches and returns a structured summary.",
            systemPrompt:
              "Use the search tool to research the question and summarize key points.",
            tools: [search],
            model: "anthropic:claude-sonnet-4-6",
            middleware: [],
          },
        ],
      }),
    ],
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, todoListMiddleware, tool } from "langchain";
  import {
    createFilesystemMiddleware,
    createSubAgentMiddleware,
    StateBackend,
  } from "deepagents";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const backend = new StateBackend();

  const agent = createAgent({
    model: "baseten:zai-org/GLM-5",
    tools: [search],
    middleware: [
      createFilesystemMiddleware({ backend }),
      todoListMiddleware(),
      createSubAgentMiddleware({
        defaultModel: "anthropic:claude-sonnet-4-6",
        defaultTools: [],
        subagents: [
          {
            name: "researcher",
            description: "Searches and returns a structured summary.",
            systemPrompt:
              "Use the search tool to research the question and summarize key points.",
            tools: [search],
            model: "anthropic:claude-sonnet-4-6",
            middleware: [],
          },
        ],
      }),
    ],
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, todoListMiddleware, tool } from "langchain";
  import {
    createFilesystemMiddleware,
    createSubAgentMiddleware,
    StateBackend,
  } from "deepagents";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const backend = new StateBackend();

  const agent = createAgent({
    model: "ollama:devstral-2",
    tools: [search],
    middleware: [
      createFilesystemMiddleware({ backend }),
      todoListMiddleware(),
      createSubAgentMiddleware({
        defaultModel: "anthropic:claude-sonnet-4-6",
        defaultTools: [],
        subagents: [
          {
            name: "researcher",
            description: "Searches and returns a structured summary.",
            systemPrompt:
              "Use the search tool to research the question and summarize key points.",
            tools: [search],
            model: "anthropic:claude-sonnet-4-6",
            middleware: [],
          },
        ],
      }),
    ],
  });
  ```
</CodeGroup>

See [`SubAgentMiddleware`](https://reference.langchain.com/javascript/deepagents/middleware/createSubAgentMiddleware), [Subagents](/oss/javascript/deepagents/subagents).

### Fault tolerance

Agents in production encounter failures that rarely appear in development: rate limits, model timeouts, transient API errors. Fault tolerance middleware handles these at the infrastructure level so your tools and business logic don't need try/catch around every call.

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    createAgent,
    modelRetryMiddleware,
    tool,
    toolRetryMiddleware,
  } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "google-genai:gemini-3.5-flash",
    tools: [search],
    middleware: [
      modelRetryMiddleware({ maxRetries: 3 }),
      toolRetryMiddleware({ maxRetries: 2 }),
    ],
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    createAgent,
    modelRetryMiddleware,
    tool,
    toolRetryMiddleware,
  } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [search],
    middleware: [
      modelRetryMiddleware({ maxRetries: 3 }),
      toolRetryMiddleware({ maxRetries: 2 }),
    ],
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    createAgent,
    modelRetryMiddleware,
    tool,
    toolRetryMiddleware,
  } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "anthropic:claude-sonnet-4-6",
    tools: [search],
    middleware: [
      modelRetryMiddleware({ maxRetries: 3 }),
      toolRetryMiddleware({ maxRetries: 2 }),
    ],
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    createAgent,
    modelRetryMiddleware,
    tool,
    toolRetryMiddleware,
  } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    tools: [search],
    middleware: [
      modelRetryMiddleware({ maxRetries: 3 }),
      toolRetryMiddleware({ maxRetries: 2 }),
    ],
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    createAgent,
    modelRetryMiddleware,
    tool,
    toolRetryMiddleware,
  } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools: [search],
    middleware: [
      modelRetryMiddleware({ maxRetries: 3 }),
      toolRetryMiddleware({ maxRetries: 2 }),
    ],
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    createAgent,
    modelRetryMiddleware,
    tool,
    toolRetryMiddleware,
  } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "baseten:zai-org/GLM-5",
    tools: [search],
    middleware: [
      modelRetryMiddleware({ maxRetries: 3 }),
      toolRetryMiddleware({ maxRetries: 2 }),
    ],
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    createAgent,
    modelRetryMiddleware,
    tool,
    toolRetryMiddleware,
  } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "ollama:devstral-2",
    tools: [search],
    middleware: [
      modelRetryMiddleware({ maxRetries: 3 }),
      toolRetryMiddleware({ maxRetries: 2 }),
    ],
  });
  ```
</CodeGroup>

See [`modelRetryMiddleware`](https://reference.langchain.com/javascript/langchain/index/modelRetryMiddleware), [`toolRetryMiddleware`](https://reference.langchain.com/javascript/langchain/index/toolRetryMiddleware), [Prebuilt middleware](/oss/javascript/langchain/middleware/built-in).

### Guardrails

Some policies can't live in a prompt — they need to be enforced deterministically regardless of what the model does. Guardrails intercept data as it flows through the agent loop, applying compliance rules or content policies before tool results reach the model's context.

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, piiMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "google-genai:gemini-3.5-flash",
    tools: [search],
    middleware: [piiMiddleware("email")],
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, piiMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [search],
    middleware: [piiMiddleware("email")],
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, piiMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "anthropic:claude-sonnet-4-6",
    tools: [search],
    middleware: [piiMiddleware("email")],
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, piiMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    tools: [search],
    middleware: [piiMiddleware("email")],
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, piiMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools: [search],
    middleware: [piiMiddleware("email")],
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, piiMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "baseten:zai-org/GLM-5",
    tools: [search],
    middleware: [piiMiddleware("email")],
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, piiMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "ollama:devstral-2",
    tools: [search],
    middleware: [piiMiddleware("email")],
  });
  ```
</CodeGroup>

See [`piiMiddleware`](https://reference.langchain.com/javascript/langchain/index/piiMiddleware), [Prebuilt middleware](/oss/javascript/langchain/middleware/built-in).

### Steering

Full autonomy isn't always appropriate. Steering lets you place humans at specific decision points — before destructive writes, expensive API calls, or anything requiring judgment — without restructuring your agent. The agent pauses and waits; a human approves, edits, or rejects; execution continues.

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "google-genai:gemini-3.5-flash",
    tools: [search],
    middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "openai:gpt-5.5",
    tools: [search],
    middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "anthropic:claude-sonnet-4-6",
    tools: [search],
    middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    tools: [search],
    middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools: [search],
    middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "baseten:zai-org/GLM-5",
    tools: [search],
    middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createAgent, humanInTheLoopMiddleware, tool } from "langchain";
  import * as z from "zod";

  const search = tool(({ query }) => `Search results for: ${query}`, {
    name: "search",
    description: "Search for a query and return a short summary.",
    schema: z.object({ query: z.string() }),
  });

  const agent = createAgent({
    model: "ollama:devstral-2",
    tools: [search],
    middleware: [humanInTheLoopMiddleware({ interruptOn: { writeFile: true } })],
  });
  ```
</CodeGroup>

See [`humanInTheLoopMiddleware`](https://reference.langchain.com/javascript/langchain/middleware/humanInTheLoopMiddleware), [Human-in-the-loop](/oss/javascript/deepagents/human-in-the-loop).

<Tip>
  `create_deep_agent` pre-assembles this stack for long-running coding and research tasks (filesystem, summarization, subagents, and prompt caching included by default). See [Deep Agents](/oss/javascript/deepagents/harness) for the full pre-built harness.
</Tip>

**Middleware resources:**

* [Middleware overview](/oss/javascript/langchain/middleware/overview): how the middleware stack works and when hooks fire
* [Prebuilt middleware](/oss/javascript/langchain/middleware/built-in): full reference with configuration examples
* [Custom middleware](/oss/javascript/langchain/middleware/custom): write your own hooks for business logic, PII scrubbing, and more

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/agents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Changelog
Source: https://docs.langchain.com/oss/javascript/langchain/changelog-js

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/changelog-js.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
