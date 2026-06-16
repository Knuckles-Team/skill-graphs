  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent, type SubAgent } from "deepagents";
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

  const researchSubagent: SubAgent = {
    name: "research-agent",
    description: "Used to research more in depth questions",
    systemPrompt: "You are a great researcher",
    tools: [internetSearch],
    model: "openai:gpt-5.5", // Optional override, defaults to main agent model
  };
  const subagents = [researchSubagent];

  const agent = createDeepAgent({
    model: "google_genai:gemini-3.5-flash",
    subagents,
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent, type SubAgent } from "deepagents";
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

  const researchSubagent: SubAgent = {
    name: "research-agent",
    description: "Used to research more in depth questions",
    systemPrompt: "You are a great researcher",
    tools: [internetSearch],
    model: "anthropic:claude-sonnet-4-6", // Optional override, defaults to main agent model
  };
  const subagents = [researchSubagent];

  const agent = createDeepAgent({
    model: "google_genai:gemini-3.5-flash",
    subagents,
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent, type SubAgent } from "deepagents";
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

  const researchSubagent: SubAgent = {
    name: "research-agent",
    description: "Used to research more in depth questions",
    systemPrompt: "You are a great researcher",
    tools: [internetSearch],
    model: "openrouter:anthropic/claude-sonnet-4-6", // Optional override, defaults to main agent model
  };
  const subagents = [researchSubagent];

  const agent = createDeepAgent({
    model: "google_genai:gemini-3.5-flash",
    subagents,
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent, type SubAgent } from "deepagents";
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

  const researchSubagent: SubAgent = {
    name: "research-agent",
    description: "Used to research more in depth questions",
    systemPrompt: "You are a great researcher",
    tools: [internetSearch],
    model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b", // Optional override, defaults to main agent model
  };
  const subagents = [researchSubagent];

  const agent = createDeepAgent({
    model: "google_genai:gemini-3.5-flash",
    subagents,
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent, type SubAgent } from "deepagents";
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

  const researchSubagent: SubAgent = {
    name: "research-agent",
    description: "Used to research more in depth questions",
    systemPrompt: "You are a great researcher",
    tools: [internetSearch],
    model: "baseten:zai-org/GLM-5", // Optional override, defaults to main agent model
  };
  const subagents = [researchSubagent];

  const agent = createDeepAgent({
    model: "google_genai:gemini-3.5-flash",
    subagents,
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { tool } from "langchain";
  import { TavilySearch } from "@langchain/tavily";
  import { createDeepAgent, type SubAgent } from "deepagents";
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

  const researchSubagent: SubAgent = {
    name: "research-agent",
    description: "Used to research more in depth questions",
    systemPrompt: "You are a great researcher",
    tools: [internetSearch],
    model: "ollama:devstral-2", // Optional override, defaults to main agent model
  };
  const subagents = [researchSubagent];

  const agent = createDeepAgent({
    model: "google_genai:gemini-3.5-flash",
    subagents,
  });
  ```
</CodeGroup>

For more information, see [Subagents](/oss/javascript/deepagents/subagents).

## Backends

Tools for a deep agent can make use of virtual file systems to store, access, and edit files. By default, deep agents use a [`StateBackend`](https://reference.langchain.com/javascript/deepagents/backends/StateBackend).

If you are using [skills](#skills) or [memory](#memory), you must add the expected skill or memory files to the backend before creating the agent.

<Tabs>
  <Tab title="StateBackend">
    A thread-scoped filesystem backend stored in `langgraph` state.

    Files persist across turns within a thread (via your checkpointer) and are not shared across threads.

    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { createDeepAgent, StateBackend } from "deepagents";

    // By default we provide a StateBackend
    const agent = createDeepAgent();

    // Under the hood, it looks like
    const agent2 = createDeepAgent({
      backend: new StateBackend(),
    });
    ```
  </Tab>

  <Tab title="FilesystemBackend">
    The local machine's filesystem.

    <Warning>
      This backend grants agents direct filesystem read/write access.
      Use with caution and only in appropriate environments.
      For more information, see [`FilesystemBackend`](/oss/javascript/deepagents/backends#filesystembackend-local-disk).
    </Warning>

    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";

      const agent = createDeepAgent({
        model: "google-genai:gemini-3.5-flash",
        backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
      });
      ```

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";

      const agent = createDeepAgent({
        model: "openai:gpt-5.5",
        backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
      });
      ```

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";

      const agent = createDeepAgent({
        model: "anthropic:claude-sonnet-4-6",
        backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
      });
      ```

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";

      const agent = createDeepAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
      });
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";

      const agent = createDeepAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
      });
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";

      const agent = createDeepAgent({
        model: "baseten:zai-org/GLM-5",
        backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
      });
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";

      const agent = createDeepAgent({
        model: "ollama:devstral-2",
        backend: new FilesystemBackend({ rootDir: ".", virtualMode: true }),
      });
      ```
    </CodeGroup>

    <Tip>
      Wrap `FilesystemBackend` in a `CompositeBackend` to prevent internal agent data (offloaded tool results, conversation history) from being written to disk alongside your project files. See the [recommended pattern](/oss/javascript/deepagents/backends#filesystembackend-local-disk).
    </Tip>
  </Tab>

  <Tab title="LocalShellBackend">
    A filesystem with shell execution directly on the host. Provides filesystem tools plus the `execute` tool for running commands.

    <Warning>
      This backend grants agents direct filesystem read/write access **and** unrestricted shell execution on your host.
      Use with extreme caution and only in appropriate environments.
      For more information, see [`LocalShellBackend`](/oss/javascript/deepagents/backends#localshellbackend-local-shell).
    </Warning>

    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, LocalShellBackend } from "deepagents";

      const backend = new LocalShellBackend({ workingDirectory: "." });

      const agent = createDeepAgent({
        model: "google-genai:gemini-3.5-flash",
        backend,
      });
      ```

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, LocalShellBackend } from "deepagents";

      const backend = new LocalShellBackend({ workingDirectory: "." });

      const agent = createDeepAgent({
        model: "openai:gpt-5.5",
        backend,
      });
      ```

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, LocalShellBackend } from "deepagents";

      const backend = new LocalShellBackend({ workingDirectory: "." });

      const agent = createDeepAgent({
        model: "anthropic:claude-sonnet-4-6",
        backend,
      });
      ```

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, LocalShellBackend } from "deepagents";

      const backend = new LocalShellBackend({ workingDirectory: "." });

      const agent = createDeepAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        backend,
      });
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, LocalShellBackend } from "deepagents";

      const backend = new LocalShellBackend({ workingDirectory: "." });

      const agent = createDeepAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        backend,
      });
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, LocalShellBackend } from "deepagents";

      const backend = new LocalShellBackend({ workingDirectory: "." });

      const agent = createDeepAgent({
        model: "baseten:zai-org/GLM-5",
        backend,
      });
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, LocalShellBackend } from "deepagents";

      const backend = new LocalShellBackend({ workingDirectory: "." });

      const agent = createDeepAgent({
        model: "ollama:devstral-2",
        backend,
      });
      ```
    </CodeGroup>
  </Tab>

  <Tab title="StoreBackend">
    A filesystem that provides long-term storage that is *persisted across threads*.

    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

      const agent = createDeepAgent({
        model: "google-genai:gemini-3.5-flash",
        backend: new StoreBackend({
          namespace: (rt) => [rt.serverInfo.user.identity],
        }),
        store,
      });
      ```

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

      const agent = createDeepAgent({
        model: "openai:gpt-5.5",
        backend: new StoreBackend({
          namespace: (rt) => [rt.serverInfo.user.identity],
        }),
        store,
      });
      ```

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

      const agent = createDeepAgent({
        model: "anthropic:claude-sonnet-4-6",
        backend: new StoreBackend({
          namespace: (rt) => [rt.serverInfo.user.identity],
        }),
        store,
      });
      ```

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

      const agent = createDeepAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        backend: new StoreBackend({
          namespace: (rt) => [rt.serverInfo.user.identity],
        }),
        store,
      });
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

      const agent = createDeepAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        backend: new StoreBackend({
          namespace: (rt) => [rt.serverInfo.user.identity],
        }),
        store,
      });
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

      const agent = createDeepAgent({
        model: "baseten:zai-org/GLM-5",
        backend: new StoreBackend({
          namespace: (rt) => [rt.serverInfo.user.identity],
        }),
        store,
      });
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore(); // Good for local dev; omit for LangSmith Deployment

      const agent = createDeepAgent({
        model: "ollama:devstral-2",
        backend: new StoreBackend({
          namespace: (rt) => [rt.serverInfo.user.identity],
        }),
        store,
      });
      ```
    </CodeGroup>

    <Note>
      When deploying to [LangSmith Deployment](/langsmith/deployment), omit the `store` parameter. The platform automatically provisions a store for your agent.
    </Note>

    <Tip>
      The `namespace` parameter controls data isolation. For multi-user deployments, always set a [namespace factory](/oss/javascript/deepagents/backends#namespace-factories) to isolate data per user or tenant.
    </Tip>
  </Tab>

  <Tab title="ContextHubBackend">
    Durable filesystem storage in a LangSmith Hub repo.

    For more details, see [`ContextHubBackend`](/oss/javascript/deepagents/backends#contexthubbackend).
  </Tab>

  <Tab title="CompositeBackend">
    A flexible backend where you can specify different routes in the filesystem to point towards different backends.

    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import {
        createDeepAgent,
        CompositeBackend,
        StateBackend,
        StoreBackend,
      } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore();

      const agent = createDeepAgent({
        model: "google-genai:gemini-3.5-flash",
        backend: new CompositeBackend(new StateBackend(), {
          "/memories/": new StoreBackend({
            namespace: () => ["memories"],
          }),
        }),
        store,
      });
      ```

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import {
        createDeepAgent,
        CompositeBackend,
        StateBackend,
        StoreBackend,
      } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore();

      const agent = createDeepAgent({
        model: "openai:gpt-5.5",
        backend: new CompositeBackend(new StateBackend(), {
          "/memories/": new StoreBackend({
            namespace: () => ["memories"],
          }),
        }),
        store,
      });
      ```

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import {
        createDeepAgent,
        CompositeBackend,
        StateBackend,
        StoreBackend,
      } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore();

      const agent = createDeepAgent({
        model: "anthropic:claude-sonnet-4-6",
        backend: new CompositeBackend(new StateBackend(), {
          "/memories/": new StoreBackend({
            namespace: () => ["memories"],
          }),
        }),
        store,
      });
      ```

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import {
        createDeepAgent,
        CompositeBackend,
        StateBackend,
        StoreBackend,
      } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore();

      const agent = createDeepAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        backend: new CompositeBackend(new StateBackend(), {
          "/memories/": new StoreBackend({
            namespace: () => ["memories"],
          }),
        }),
        store,
      });
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import {
        createDeepAgent,
        CompositeBackend,
        StateBackend,
        StoreBackend,
      } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore();

      const agent = createDeepAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        backend: new CompositeBackend(new StateBackend(), {
          "/memories/": new StoreBackend({
            namespace: () => ["memories"],
          }),
        }),
        store,
      });
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import {
        createDeepAgent,
        CompositeBackend,
        StateBackend,
        StoreBackend,
      } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore();

      const agent = createDeepAgent({
        model: "baseten:zai-org/GLM-5",
        backend: new CompositeBackend(new StateBackend(), {
          "/memories/": new StoreBackend({
            namespace: () => ["memories"],
          }),
        }),
        store,
      });
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
