# Tools
Source: https://docs.langchain.com/oss/javascript/deepagents/tools

Connect Deep Agents to custom functions, APIs, databases, and any MCP server

Deep Agents can call any tool you define, any [LangChain tool](https://python.langchain.com/docs/concepts/tools/), and tools from any [MCP server](#mcp-tools).
Pass them to `create_deep_agent` via the `tools=` parameter alongside the [built-in harness tools](/oss/javascript/deepagents/harness#execution-environment) for planning, file management, and subagent spawning.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-4-6",
  tools: [search, fetchUrl, runQuery],
});
```

## Custom tools

Pass any callable — plain functions, LangChain `@tool`-decorated functions, or tool dicts — directly to `tools=`.
Deep Agents infers the tool schema from the function signature and docstring, so you don't need to define a separate schema in most cases.

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent } from "deepagents";
  import { z } from "zod";

  const internetSearch = tool(
    async ({
      query,
      maxResults = 5,
      topic = "general",
      includeRawContent = false,
    }: {
      query: string;
      maxResults?: number;
      topic?: "general" | "news" | "finance";
      includeRawContent?: boolean;
    }) => {
      const tavilySearch = new TavilySearch({
        maxResults,
        tavilyApiKey: process.env.TAVILY_API_KEY,
        includeRawContent,
        topic,
      });
      return await tavilySearch._call({ query });
    },
    {
      name: "internet_search",
      description: "Run a web search",
      schema: z.object({
        query: z.string().describe("The search query"),
        maxResults: z.number().optional().default(5),
        topic: z
          .enum(["general", "news", "finance"])
          .optional()
          .default("general"),
        includeRawContent: z.boolean().optional().default(false),
      }),
    },
  );

  const agent = createDeepAgent({
    model: "google-genai:gemini-3.5-flash",
    tools: [internetSearch],
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent } from "deepagents";
  import { z } from "zod";

  const internetSearch = tool(
    async ({
      query,
      maxResults = 5,
      topic = "general",
      includeRawContent = false,
    }: {
      query: string;
      maxResults?: number;
      topic?: "general" | "news" | "finance";
      includeRawContent?: boolean;
    }) => {
      const tavilySearch = new TavilySearch({
        maxResults,
        tavilyApiKey: process.env.TAVILY_API_KEY,
        includeRawContent,
        topic,
      });
      return await tavilySearch._call({ query });
    },
    {
      name: "internet_search",
      description: "Run a web search",
      schema: z.object({
        query: z.string().describe("The search query"),
        maxResults: z.number().optional().default(5),
        topic: z
          .enum(["general", "news", "finance"])
          .optional()
          .default("general"),
        includeRawContent: z.boolean().optional().default(false),
      }),
    },
  );

  const agent = createDeepAgent({
    model: "openai:gpt-5.5",
    tools: [internetSearch],
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent } from "deepagents";
  import { z } from "zod";

  const internetSearch = tool(
    async ({
      query,
      maxResults = 5,
      topic = "general",
      includeRawContent = false,
    }: {
      query: string;
      maxResults?: number;
      topic?: "general" | "news" | "finance";
      includeRawContent?: boolean;
    }) => {
      const tavilySearch = new TavilySearch({
        maxResults,
        tavilyApiKey: process.env.TAVILY_API_KEY,
        includeRawContent,
        topic,
      });
      return await tavilySearch._call({ query });
    },
    {
      name: "internet_search",
      description: "Run a web search",
      schema: z.object({
        query: z.string().describe("The search query"),
        maxResults: z.number().optional().default(5),
        topic: z
          .enum(["general", "news", "finance"])
          .optional()
          .default("general"),
        includeRawContent: z.boolean().optional().default(false),
      }),
    },
  );

  const agent = createDeepAgent({
    model: "anthropic:claude-sonnet-4-6",
    tools: [internetSearch],
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent } from "deepagents";
  import { z } from "zod";

  const internetSearch = tool(
    async ({
      query,
      maxResults = 5,
      topic = "general",
      includeRawContent = false,
    }: {
      query: string;
      maxResults?: number;
      topic?: "general" | "news" | "finance";
      includeRawContent?: boolean;
    }) => {
      const tavilySearch = new TavilySearch({
        maxResults,
        tavilyApiKey: process.env.TAVILY_API_KEY,
        includeRawContent,
        topic,
      });
      return await tavilySearch._call({ query });
    },
    {
      name: "internet_search",
      description: "Run a web search",
      schema: z.object({
        query: z.string().describe("The search query"),
        maxResults: z.number().optional().default(5),
        topic: z
          .enum(["general", "news", "finance"])
          .optional()
          .default("general"),
        includeRawContent: z.boolean().optional().default(false),
      }),
    },
  );

  const agent = createDeepAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    tools: [internetSearch],
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent } from "deepagents";
  import { z } from "zod";

  const internetSearch = tool(
    async ({
      query,
      maxResults = 5,
      topic = "general",
      includeRawContent = false,
    }: {
      query: string;
      maxResults?: number;
      topic?: "general" | "news" | "finance";
      includeRawContent?: boolean;
    }) => {
      const tavilySearch = new TavilySearch({
        maxResults,
        tavilyApiKey: process.env.TAVILY_API_KEY,
        includeRawContent,
        topic,
      });
      return await tavilySearch._call({ query });
    },
    {
      name: "internet_search",
      description: "Run a web search",
      schema: z.object({
        query: z.string().describe("The search query"),
        maxResults: z.number().optional().default(5),
        topic: z
          .enum(["general", "news", "finance"])
          .optional()
          .default("general"),
        includeRawContent: z.boolean().optional().default(false),
      }),
    },
  );

  const agent = createDeepAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    tools: [internetSearch],
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent } from "deepagents";
  import { z } from "zod";

  const internetSearch = tool(
    async ({
      query,
      maxResults = 5,
      topic = "general",
      includeRawContent = false,
    }: {
      query: string;
      maxResults?: number;
      topic?: "general" | "news" | "finance";
      includeRawContent?: boolean;
    }) => {
      const tavilySearch = new TavilySearch({
        maxResults,
        tavilyApiKey: process.env.TAVILY_API_KEY,
        includeRawContent,
        topic,
      });
      return await tavilySearch._call({ query });
    },
    {
      name: "internet_search",
      description: "Run a web search",
      schema: z.object({
        query: z.string().describe("The search query"),
        maxResults: z.number().optional().default(5),
        topic: z
          .enum(["general", "news", "finance"])
          .optional()
          .default("general"),
        includeRawContent: z.boolean().optional().default(false),
      }),
    },
  );

  const agent = createDeepAgent({
    model: "baseten:zai-org/GLM-5",
    tools: [internetSearch],
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent } from "deepagents";
  import { z } from "zod";

  const internetSearch = tool(
    async ({
      query,
      maxResults = 5,
      topic = "general",
      includeRawContent = false,
    }: {
      query: string;
      maxResults?: number;
      topic?: "general" | "news" | "finance";
      includeRawContent?: boolean;
    }) => {
      const tavilySearch = new TavilySearch({
        maxResults,
        tavilyApiKey: process.env.TAVILY_API_KEY,
        includeRawContent,
        topic,
      });
      return await tavilySearch._call({ query });
    },
    {
      name: "internet_search",
      description: "Run a web search",
      schema: z.object({
        query: z.string().describe("The search query"),
        maxResults: z.number().optional().default(5),
        topic: z
          .enum(["general", "news", "finance"])
          .optional()
          .default("general"),
        includeRawContent: z.boolean().optional().default(false),
      }),
    },
  );

  const agent = createDeepAgent({
    model: "ollama:devstral-2",
    tools: [internetSearch],
  });
  ```
</CodeGroup>

For full details on defining and using LangChain tools (tool dicts, `StructuredTool`, return types, error handling, and more), see [Tools](/oss/javascript/langchain/tools).

## MCP tools

<Note>
  Deep Agents fully support [Model Context Protocol (MCP)](/oss/javascript/langchain/mcp) — the open standard for connecting agents to external services. Load tools from any MCP server and pass them directly to `create_deep_agent`.
</Note>

MCP is an open protocol that lets agents connect to a growing ecosystem of servers — databases, APIs, file systems, browsers, and more — through a standard interface. Instead of writing custom integration code for each service, you point Deep Agents at an MCP server and it gets all the tools that server exposes.

Install `@langchain/mcp-adapters` to connect to MCP servers:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm install @langchain/mcp-adapters
```

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { MultiServerMCPClient } from "@langchain/mcp-adapters";
import { createDeepAgent } from "deepagents";

const client = new MultiServerMCPClient({
  my_server: {
    transport: "http",
    url: "http://localhost:8000/mcp",
  },
});

const tools = await client.getTools();

const agent = await createDeepAgent({
  model: "openai:gpt-5.5",
  tools,
});

const result = await agent.invoke({
  messages: [{ role: "user", content: "Use the MCP server to help me." }],
});
```

For detailed configuration options — including stdio servers, OAuth authentication, tool filtering, and stateful sessions — see the full [MCP guide](/oss/javascript/langchain/mcp).

## Built-in harness tools

In addition to the tools you provide, every Deep Agent comes with a built-in set of tools from the harness:

| Tool          | Description                                                 |
| ------------- | ----------------------------------------------------------- |
| `ls`          | List files in a directory                                   |
| `read_file`   | Read file contents (with pagination and multimodal support) |
| `write_file`  | Create new files                                            |
| `edit_file`   | Perform exact string replacements in files                  |
| `glob`        | Find files matching a glob pattern                          |
| `grep`        | Search file contents                                        |
| `execute`     | Run shell commands (sandbox backends only)                  |
| `task`        | Spawn a subagent to handle a delegated task                 |
| `write_todos` | Manage a structured todo list                               |

For a full breakdown of what each built-in tool does, see [Harness capabilities](/oss/javascript/deepagents/harness#execution-environment).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# ChatAnthropic integration
Source: https://docs.langchain.com/oss/javascript/integrations/chat/anthropic

Integrate with the ChatAnthropic chat model using LangChain JavaScript.

[Anthropic](https://www.anthropic.com/) is an AI safety and research company. They are the creator of Claude.

This will help you getting started with `ChatAnthropic` [chat models](/oss/javascript/langchain/models). For detailed documentation of all `ChatAnthropic` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-anthropic/ChatAnthropic).

## Overview

### Integration details

| Class                                                                                           | Package                                                                      | Serializable | [PY support](https://python.langchain.com/docs/integrations/chat/anthropic/) |                                               Downloads                                              |                                              Version                                              |
| :---------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- | :----------: | :--------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------: |
| [`ChatAnthropic`](https://reference.langchain.com/javascript/langchain-anthropic/ChatAnthropic) | [`@langchain/anthropic`](https://www.npmjs.com/package/@langchain/anthropic) |       ✅      |                                       ✅                                      | ![NPM - Downloads](https://img.shields.io/npm/dm/@langchain/anthropic?style=flat-square\&label=%20&) | ![NPM - Version](https://img.shields.io/npm/v/@langchain/anthropic?style=flat-square\&label=%20&) |

### Model features

See the links in the table headers below for guides on how to use specific features.

| [Tool calling](/oss/javascript/langchain/tools) | [Structured output](/oss/javascript/langchain/structured-output) | [Image input](/oss/javascript/langchain/messages#multimodal) | Audio input | Video input | [Token-level streaming](/oss/javascript/langchain/streaming/) | [Token usage](/oss/javascript/langchain/models#token-usage) | [Logprobs](/oss/javascript/langchain/models#log-probabilities) |
| :---------------------------------------------: | :--------------------------------------------------------------: | :----------------------------------------------------------: | :---------: | :---------: | :-----------------------------------------------------------: | :---------------------------------------------------------: | :------------------------------------------------------------: |
|                        ✅                        |                                 ✅                                |                               ✅                              |      ❌      |      ❌      |                               ✅                               |                              ✅                              |                                ❌                               |

## Setup

You'll need to sign up and obtain an [Anthropic API key](https://www.anthropic.com/), and install the `@langchain/anthropic` integration package.

### Credentials

Head to [Anthropic's website](https://www.anthropic.com/) to sign up to Anthropic and generate an API key. Once you've done this set the `ANTHROPIC_API_KEY` environment variable:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export ANTHROPIC_API_KEY="your-api-key"
```

If you want to get automated tracing of your model calls you can also set your [LangSmith](/langsmith/observability) API key by uncommenting below:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# export LANGSMITH_TRACING="true"
