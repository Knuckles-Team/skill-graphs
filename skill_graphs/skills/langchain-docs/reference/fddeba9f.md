      import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

      const AGENTS_MD_URL =
        "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

      async function fetchText(url: string): Promise<string> {
        const res = await fetch(url);
        if (!res.ok) {
          throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
        }
        return await res.text();
      }

      const agentsMd = await fetchText(AGENTS_MD_URL);

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const store = new InMemoryStore();
      const fileData = createFileData(agentsMd);
      await store.put(["filesystem"], "/AGENTS.md", fileData);

      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        backend: new StoreBackend({
          namespace: () => ["filesystem"],
        }),
        store: store,
        checkpointer: checkpointer,
        memory: ["/AGENTS.md"],
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
        },
        { configurable: { thread_id: "12345" } },
      );
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
      import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

      const AGENTS_MD_URL =
        "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

      async function fetchText(url: string): Promise<string> {
        const res = await fetch(url);
        if (!res.ok) {
          throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
        }
        return await res.text();
      }

      const agentsMd = await fetchText(AGENTS_MD_URL);

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const store = new InMemoryStore();
      const fileData = createFileData(agentsMd);
      await store.put(["filesystem"], "/AGENTS.md", fileData);

      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        backend: new StoreBackend({
          namespace: () => ["filesystem"],
        }),
        store: store,
        checkpointer: checkpointer,
        memory: ["/AGENTS.md"],
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
        },
        { configurable: { thread_id: "12345" } },
      );
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
      import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

      const AGENTS_MD_URL =
        "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

      async function fetchText(url: string): Promise<string> {
        const res = await fetch(url);
        if (!res.ok) {
          throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
        }
        return await res.text();
      }

      const agentsMd = await fetchText(AGENTS_MD_URL);

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const store = new InMemoryStore();
      const fileData = createFileData(agentsMd);
      await store.put(["filesystem"], "/AGENTS.md", fileData);

      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "baseten:zai-org/GLM-5",
        backend: new StoreBackend({
          namespace: () => ["filesystem"],
        }),
        store: store,
        checkpointer: checkpointer,
        memory: ["/AGENTS.md"],
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
        },
        { configurable: { thread_id: "12345" } },
      );
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
      import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

      const AGENTS_MD_URL =
        "https://raw.githubusercontent.com/langchain-ai/deepagents/refs/heads/main/examples/text-to-sql-agent/AGENTS.md";

      async function fetchText(url: string): Promise<string> {
        const res = await fetch(url);
        if (!res.ok) {
          throw new Error(`Failed to fetch ${url}: ${res.status} ${res.statusText}`);
        }
        return await res.text();
      }

      const agentsMd = await fetchText(AGENTS_MD_URL);

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const store = new InMemoryStore();
      const fileData = createFileData(agentsMd);
      await store.put(["filesystem"], "/AGENTS.md", fileData);

      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "ollama:devstral-2",
        backend: new StoreBackend({
          namespace: () => ["filesystem"],
        }),
        store: store,
        checkpointer: checkpointer,
        memory: ["/AGENTS.md"],
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
        },
        { configurable: { thread_id: "12345" } },
      );
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Filesystem">
    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

      // Checkpointer is REQUIRED for human-in-the-loop
      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "google-genai:gemini-3.5-flash",
        backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
        memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
        interruptOn: {
          read_file: true,
          write_file: true,
          delete_file: true,
        },
        checkpointer, // Required!
      });
      ```

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

      // Checkpointer is REQUIRED for human-in-the-loop
      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "openai:gpt-5.5",
        backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
        memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
        interruptOn: {
          read_file: true,
          write_file: true,
          delete_file: true,
        },
        checkpointer, // Required!
      });
      ```

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

      // Checkpointer is REQUIRED for human-in-the-loop
      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "anthropic:claude-sonnet-4-6",
        backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
        memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
        interruptOn: {
          read_file: true,
          write_file: true,
          delete_file: true,
        },
        checkpointer, // Required!
      });
      ```

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

      // Checkpointer is REQUIRED for human-in-the-loop
      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
        memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
        interruptOn: {
          read_file: true,
          write_file: true,
          delete_file: true,
        },
        checkpointer, // Required!
      });
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

      // Checkpointer is REQUIRED for human-in-the-loop
      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
        memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
        interruptOn: {
          read_file: true,
          write_file: true,
          delete_file: true,
        },
        checkpointer, // Required!
      });
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

      // Checkpointer is REQUIRED for human-in-the-loop
      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "baseten:zai-org/GLM-5",
        backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
        memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
        interruptOn: {
          read_file: true,
          write_file: true,
          delete_file: true,
        },
        checkpointer, // Required!
      });
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, FilesystemBackend } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

      // Checkpointer is REQUIRED for human-in-the-loop
      const checkpointer = new MemorySaver();

      const agent = await createDeepAgent({
        model: "ollama:devstral-2",
        backend: new FilesystemBackend({ rootDir: "/Users/user/{project}" }),
        memory: ["./AGENTS.md", "./.deepagents/AGENTS.md"],
        interruptOn: {
          read_file: true,
          write_file: true,
          delete_file: true,
        },
        checkpointer, // Required!
      });
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Structured output

Deep Agents support [structured output](/oss/javascript/langchain/structured-output).

You can set a desired structured output schema by passing it as the `responseFormat` argument to the call to `createDeepAgent()`.
When the model generates the structured data, it's captured, validated, and returned in the 'structuredResponse' key of the agent's state.

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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

const weatherReportSchema = z.object({
  location: z.string().describe("The location for this weather report"),
  temperature: z.number().describe("Current temperature in Celsius"),
  condition: z
    .string()
    .describe("Current weather condition (e.g., sunny, cloudy, rainy)"),
  humidity: z.number().describe("Humidity percentage"),
  windSpeed: z.number().describe("Wind speed in km/h"),
  forecast: z.string().describe("Brief forecast for the next 24 hours"),
});

const agent = await createDeepAgent({
  responseFormat: weatherReportSchema,
  tools: [internetSearch],
});

const result = await agent.invoke({
  messages: [
    {
      role: "user",
      content: "What's the weather like in San Francisco?",
    },
  ],
});

console.log(result.structuredResponse);
// {
//   location: 'San Francisco, California',
//   temperature: 18.3,
//   condition: 'Sunny',
//   humidity: 48,
//   windSpeed: 7.6,
//   forecast: 'Clear skies with temperatures remaining mild. High of 18°C (64°F) during the day, dropping to around 11°C (52°F) at night.'
// }
```

For more information and examples, see [response format](/oss/javascript/langchain/structured-output#response-format).

## Advanced

`createDeepAgent` pre-assembles a middleware stack on top of `createAgent`. To build a fully custom agent—choosing exactly which capabilities to include—see [Configure the harness](/oss/javascript/langchain/agents#configure-the-harness).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/customization.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
