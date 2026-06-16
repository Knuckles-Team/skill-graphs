# Customize Deep Agents
Source: https://docs.langchain.com/oss/javascript/deepagents/customization

Learn how to customize Deep Agents with system prompts, tools, subagents, and more

Build the harness around your goal. `create_deep_agent` gives you a production-ready foundation: connect it to your data, shape its behavior, and add the capabilities your use case needs.

`createDeepAgent` ships with a pre-assembled harness: filesystem, summarization, subagents, and prompt caching by default. The parameters below let you define the agent's persona, connect it to your data and tools, and extend the [default middleware stack](#default-stack-main-agent) with additional middleware.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent } from "deepagents";

const agent = await createDeepAgent({
  model: "anthropic:claude-sonnet-4-6",
  systemPrompt: "You are a helpful assistant.",
  tools: [search, fetchUrl],
  memory: ["./AGENTS.md"],
  skills: ["./skills/"],
});
```

| Parameter        | What it does                                                                |
| ---------------- | --------------------------------------------------------------------------- |
| `model`          | Which model to use                                                          |
| `systemPrompt`   | Custom instructions for the agent                                           |
| `tools`          | Domain tools the agent can call                                             |
| `memory`         | AGENTS.md files loaded at startup                                           |
| `skills`         | Skills directory for on-demand knowledge                                    |
| `backend`        | Filesystem backend (StateBackend by default)                                |
| `permissions`    | Path-level access control for the filesystem                                |
| `subagents`      | Custom subagents for delegated tasks                                        |
| `middleware`     | Extra middleware appended to the [default stack](#default-stack-main-agent) |
| `interruptOn`    | Pause before tool calls for human approval                                  |
| `responseFormat` | Structured output schema                                                    |

For the full parameter list, see the [`createDeepAgent`](https://reference.langchain.com/javascript/deepagents/types/CreateDeepAgentParams) API reference. To compose a fully custom harness from scratch, see [Configure the harness](/oss/javascript/langchain/agents#configure-the-harness).

<Tip>
  As you add tools, subagents, and backends, use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-customization) to trace how each piece behaves together. Follow the [observability quickstart](/langsmith/observability-quickstart) to get set up, and see [Going to production](/oss/javascript/deepagents/going-to-production) for deployment on LangSmith.

  We recommend you also set up [LangSmith Engine](/langsmith/engine), which monitors your traces, detects issues, and proposes fixes.
</Tip>

## Model

Pass a `model` string in `provider:model` format, or an initialized model instance. See [supported models](/oss/javascript/deepagents/models#supported-models) for all providers and [suggested models](/oss/javascript/deepagents/models#suggested-models) for tested recommendations.

<Tip>
  Use the `provider:model` format (for example `openai:gpt-5.5`) to quickly switch between models.
</Tip>

<Tabs>
  <Tab title="OpenAI">
    👉 Read the [OpenAI chat model integration docs](/oss/javascript/integrations/chat/openai/)

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/openai deepagents
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm install @langchain/openai deepagents
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/openai deepagents
      ```

      ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      bun add @langchain/openai deepagents
      ```
    </CodeGroup>

    <CodeGroup>
      ```typescript default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";

      process.env.OPENAI_API_KEY = "your-api-key";

      const agent = createDeepAgent({ model: "gpt-5.5" });
      // this calls initChatModel for the specified model with default parameters
      // to use specific model parameters, use initChatModel directly
      ```

      ```typescript initChatModel theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { initChatModel } from "langchain";
      import { createDeepAgent } from "deepagents";

      process.env.OPENAI_API_KEY = "your-api-key";

      const model = await initChatModel("gpt-5.5");
      const agent = createDeepAgent({
        model,
        temperature: 0,
      });
      ```

      ```typescript Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { ChatOpenAI } from "@langchain/openai";
      import { createDeepAgent } from "deepagents";

      const agent = createDeepAgent({
        model: new ChatOpenAI({
          model: "gpt-5.5",
          apiKey: "your-api-key",
          temperature: 0,
        }),
      });
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Anthropic">
    👉 Read the [Anthropic chat model integration docs](/oss/javascript/integrations/chat/anthropic/)

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/anthropic deepagents
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm install @langchain/anthropic deepagents
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/anthropic deepagents
      ```

      ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      bun add @langchain/anthropic deepagents
      ```
    </CodeGroup>

    <CodeGroup>
      ```typescript default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";

      process.env.ANTHROPIC_API_KEY = "your-api-key";

      const agent = createDeepAgent({ model: "anthropic:claude-sonnet-4-6" });
      // this calls initChatModel for the specified model with default parameters
      // to use specific model parameters, use initChatModel directly
      ```

      ```typescript initChatModel theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { initChatModel } from "langchain";
      import { createDeepAgent } from "deepagents";

      process.env.ANTHROPIC_API_KEY = "your-api-key";

      const model = await initChatModel("claude-sonnet-4-6");
      const agent = createDeepAgent({
        model,
        temperature: 0,
      });
      ```

      ```typescript Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { ChatAnthropic } from "@langchain/anthropic";
      import { createDeepAgent } from "deepagents";

      const agent = createDeepAgent({
        model: new ChatAnthropic({
          model: "claude-sonnet-4-6",
          apiKey: "your-api-key",
          temperature: 0,
        }),
      });
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Azure">
    👉 Read the [Azure chat model integration docs](/oss/javascript/integrations/chat/azure/)

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/azure deepagents
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm install @langchain/azure deepagents
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/azure deepagents
      ```

      ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      bun add @langchain/azure deepagents
      ```
    </CodeGroup>

    <CodeGroup>
      ```typescript default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";

      process.env.AZURE_OPENAI_API_KEY = "your-api-key";
      process.env.AZURE_OPENAI_ENDPOINT = "your-endpoint";
      process.env.OPENAI_API_VERSION = "your-api-version";

      const agent = createDeepAgent({ model: "azure_openai:gpt-5.5" });
      // this calls initChatModel for the specified model with default parameters
      // to use specific model parameters, use initChatModel directly
      ```

      ```typescript initChatModel theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { initChatModel } from "langchain";
      import { createDeepAgent } from "deepagents";

      process.env.AZURE_OPENAI_API_KEY = "your-api-key";
      process.env.AZURE_OPENAI_ENDPOINT = "your-endpoint";
      process.env.OPENAI_API_VERSION = "your-api-version";

      const model = await initChatModel("azure_openai:gpt-5.5");
      const agent = createDeepAgent({
        model,
        temperature: 0,
      });
      ```

      ```typescript Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { AzureChatOpenAI } from "@langchain/openai";
      import { createDeepAgent } from "deepagents";

      const agent = createDeepAgent({
        model: new AzureChatOpenAI({
          model: "gpt-5.5",
          azureOpenAIApiKey: "your-api-key",
          azureOpenAIApiEndpoint: "your-endpoint",
          azureOpenAIApiVersion: "your-api-version",
          temperature: 0,
        }),
      });
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Google Gemini">
    👉 Read the [Google GenAI chat model integration docs](/oss/javascript/integrations/chat/google_generative_ai/)

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/google-genai deepagents
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm install @langchain/google-genai deepagents
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/google-genai deepagents
      ```

      ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      bun add @langchain/google-genai deepagents
      ```
    </CodeGroup>

    <CodeGroup>
      ```typescript default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";

      process.env.GOOGLE_API_KEY = "your-api-key";

      const agent = createDeepAgent({ model: "google-genai:gemini-3.1-pro-preview" });
      // this calls initChatModel for the specified model with default parameters
      // to use specific model parameters, use initChatModel directly
      ```

      ```typescript initChatModel theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { initChatModel } from "langchain";
      import { createDeepAgent } from "deepagents";

      process.env.GOOGLE_API_KEY = "your-api-key";

      const model = await initChatModel("google-genai:gemini-3.1-pro-preview");
      const agent = createDeepAgent({
        model,
        temperature: 0,
      });
      ```

      ```typescript Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { ChatGoogleGenerativeAI } from "@langchain/google-genai";
      import { createDeepAgent } from "deepagents";

      const agent = createDeepAgent({
        model: new ChatGoogleGenerativeAI({
          model: "gemini-3.1-pro-preview",
          apiKey: "your-api-key",
          temperature: 0,
        }),
      });
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Bedrock Converse">
    👉 Read the [AWS Bedrock chat model integration docs](/oss/javascript/integrations/chat/bedrock_converse/)

    <CodeGroup>
      ```bash npm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      npm install @langchain/aws deepagents
      ```

      ```bash pnpm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      pnpm install @langchain/aws deepagents
      ```

      ```bash yarn theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      yarn add @langchain/aws deepagents
      ```

      ```bash bun theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      bun add @langchain/aws deepagents
      ```
    </CodeGroup>

    <CodeGroup>
      ```typescript default parameters theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent } from "deepagents";

      // Follow the steps here to configure your credentials:
      // https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

      const agent = createDeepAgent({ model: "bedrock:anthropic.claude-sonnet-4-6" });
      // this calls initChatModel for the specified model with default parameters
      // to use specific model parameters, use initChatModel directly
      ```

      ```typescript initChatModel theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { initChatModel } from "langchain";
      import { createDeepAgent } from "deepagents";

      // Follow the steps here to configure your credentials:
      // https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

      const model = await initChatModel("bedrock:anthropic.claude-sonnet-4-6");
      const agent = createDeepAgent({
        model,
        temperature: 0,
      });
      ```

      ```typescript Model Class theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { ChatBedrockConverse } from "@langchain/aws";
      import { createDeepAgent } from "deepagents";

      // Follow the steps here to configure your credentials:
      // https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html

      const agent = createDeepAgent({
        model: new ChatBedrockConverse({
          model: "anthropic.claude-sonnet-4-6",
          region: "us-east-2",
          temperature: 0,
        }),
      });
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Other">
    Pass any [supported model string](/oss/javascript/deepagents/models#supported-models), or an initialized model instance:

    ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { initChatModel } from "langchain";
    import { createDeepAgent } from "deepagents";

    const model = await initChatModel("provider:model-name");
    const agent = createDeepAgent({ model });
    ```
  </Tab>
</Tabs>

<Tip>
  Chat models automatically retry transient API failures (with exponential backoff). For defaults, limits, and code samples for tuning `max_retries` / `timeout` live on the LangChain [Models](/oss/javascript/langchain/models#connection-resilience) page.
</Tip>

## Tools

In addition to [built-in tools](/oss/javascript/deepagents/overview#core-capabilities) for planning, file management, and subagent spawning, you can provide custom tools:

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

### MCP tools

<Tip>
  Deep Agents fully support [Model Context Protocol (MCP)](/oss/javascript/langchain/mcp) tools. You can load tools from any MCP server—databases, APIs, file systems, and more—and pass them directly to `create_deep_agent`.
</Tip>

Install `@langchain/mcp-adapters` to connect to MCP servers:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm install @langchain/mcp-adapters
```

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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

For detailed configuration options including stdio servers, OAuth authentication, tool filtering, and stateful sessions, see the full [MCP guide](/oss/javascript/langchain/mcp).

## System prompt

Deep Agents come with a built-in system prompt. A deep agent's value comes from the orchestration layer the SDK provides on top of the model—planning, virtual-filesystem tools, and subagents—and the model needs to know those exist and when to reach for them. The built-in prompt teaches the agent how to use that scaffolding so you don't have to re-derive it for every project; tweak it through a [profile](/oss/javascript/deepagents/profiles#harness-profiles) or your own `system_prompt=` rather than copying it verbatim.

When middleware add special tools, like the filesystem tools, it appends them to the system prompt.

Each deep agent should also include a custom system prompt specific to its specific use case:

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const researchInstructions =
    `You are an expert researcher. ` +
    `Your job is to conduct thorough research, and then ` +
    `write a polished report.`;

  const agent = createDeepAgent({
    model: "google-genai:gemini-3.5-flash",
    systemPrompt: researchInstructions,
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const researchInstructions =
    `You are an expert researcher. ` +
    `Your job is to conduct thorough research, and then ` +
    `write a polished report.`;

  const agent = createDeepAgent({
    model: "openai:gpt-5.5",
    systemPrompt: researchInstructions,
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const researchInstructions =
    `You are an expert researcher. ` +
    `Your job is to conduct thorough research, and then ` +
    `write a polished report.`;

  const agent = createDeepAgent({
    model: "anthropic:claude-sonnet-4-6",
    systemPrompt: researchInstructions,
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const researchInstructions =
    `You are an expert researcher. ` +
    `Your job is to conduct thorough research, and then ` +
    `write a polished report.`;

  const agent = createDeepAgent({
    model: "openrouter:anthropic/claude-sonnet-4-6",
    systemPrompt: researchInstructions,
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const researchInstructions =
    `You are an expert researcher. ` +
    `Your job is to conduct thorough research, and then ` +
    `write a polished report.`;

  const agent = createDeepAgent({
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
    systemPrompt: researchInstructions,
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const researchInstructions =
    `You are an expert researcher. ` +
    `Your job is to conduct thorough research, and then ` +
    `write a polished report.`;

  const agent = createDeepAgent({
    model: "baseten:zai-org/GLM-5",
    systemPrompt: researchInstructions,
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent } from "deepagents";

  const researchInstructions =
    `You are an expert researcher. ` +
    `Your job is to conduct thorough research, and then ` +
    `write a polished report.`;

  const agent = createDeepAgent({
    model: "ollama:devstral-2",
    systemPrompt: researchInstructions,
  });
  ```
</CodeGroup>

### Prompt assembly

Deep Agents builds the system prompt from up to four named parts so that caller-supplied instructions, the SDK's built-in agent guidance, and any model-specific [profile](/oss/javascript/deepagents/profiles) overrides can coexist with predictable precedence. Without this layering, a profile suffix tuned for Claude (for example) could overwrite or be overwritten by your `system_prompt=` argument depending on call order; the named slots make the ordering explicit and stable.

In practice, most callers only encounter two slots: `USER` (your `system_prompt=`) and `BASE` (the SDK default). Selecting a model with a built-in profile—Anthropic or OpenAI today—adds a `SUFFIX`. The full four-part assembly is mainly relevant when you author a custom `HarnessProfile` or debug why a profile's text appears where it does.

The four named parts (each may be absent):

| Name     | Source                                                                                        | Notes                                                     |
| -------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `USER`   | `system_prompt=` argument to `create_deep_agent`                                              | `str` or `SystemMessage`; omitted when unset.             |
| `BASE`   | The SDK default (`BASE_AGENT_PROMPT`)                                                         | Always present unless replaced by a profile's `CUSTOM`.   |
| `CUSTOM` | [`HarnessProfile.base_system_prompt`](/oss/javascript/deepagents/profiles#harness-profiles)   | Replaces `BASE` outright when a matching profile sets it. |
| `SUFFIX` | [`HarnessProfile.system_prompt_suffix`](/oss/javascript/deepagents/profiles#harness-profiles) | Appended last when a matching profile sets it.            |

The order is always **`USER` -> (`BASE` or `CUSTOM`) -> `SUFFIX`**, joined by blank lines (`\n\n`). Two invariants follow:

1. **`USER` is always at the front.** The caller's text precedes any SDK or profile content, so persona/instructions take precedence regardless of which model is selected.
2. **`SUFFIX` is always at the end.** Profile suffixes sit closest to the conversation history, where model-tuning guidance lands most reliably.

Assembled shapes (✓ = field is set, - = field is unset):

| `system_prompt=` | profile `base_system_prompt` (`CUSTOM`) | profile `system_prompt_suffix` (`SUFFIX`) | Final assembled system prompt |
| ---------------- | :-------------------------------------: | :---------------------------------------: | ----------------------------- |
| `None`           |                    -                    |                     -                     | `BASE`                        |
| `None`           |                    -                    |                     ✓                     | `BASE` + `SUFFIX`             |
| `None`           |                    ✓                    |                     -                     | `CUSTOM`                      |
| `None`           |                    ✓                    |                     ✓                     | `CUSTOM` + `SUFFIX`           |
| `str`            |                    -                    |                     -                     | `USER` + `BASE`               |
| `str`            |                    -                    |                     ✓                     | `USER` + `BASE` + `SUFFIX`    |
| `str`            |                    ✓                    |                     -                     | `USER` + `CUSTOM`             |
| `str`            |                    ✓                    |                     ✓                     | `USER` + `CUSTOM` + `SUFFIX`  |

Worked example—built-in profiles (Anthropic, OpenAI) ship only a `system_prompt_suffix`, so a typical call lands in the `str` + `-` + `✓` row:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
agent = create_deep_agent(
    model="anthropic:claude-sonnet-4-6",
    system_prompt="You are a customer-support agent for ACME Corp.",
)

# Final = USER + BASE + SUFFIX

#       = "You are a customer-support agent for ACME Corp."

#         + "\n\n"

#         + BASE_AGENT_PROMPT

#         + "\n\n"
