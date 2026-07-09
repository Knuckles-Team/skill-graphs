      import {
        createDeepAgent,
        CompositeBackend,
        StateBackend,
        StoreBackend,
      } from "deepagents";
      import { InMemoryStore } from "@langchain/langgraph";

      const store = new InMemoryStore();

      const agent = createDeepAgent({
        model: "ollama:devstral-2",
        backend: new CompositeBackend(new StateBackend(), {
          "/memories/": new StoreBackend({
            namespace: () => ["memories"],
          }),
        }),
        store,
      });
      ```
    </CodeGroup>
  </Tab>
</Tabs>

For more information, see [Backends](/oss/javascript/deepagents/backends).

### Sandboxes

Sandboxes are specialized [backends](/oss/javascript/deepagents/backends) that run agent code in an isolated environment with their own filesystem and an `execute` tool for shell commands.
Use a sandbox backend when you want your deep agent to write files, install dependencies, and run commands without changing anything on your local machine.

You configure sandboxes by passing a sandbox backend to `backend` when creating your deep agent:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent } from "deepagents";
import { ChatAnthropic } from "@langchain/anthropic";
import { DenoSandbox } from "@langchain/deno";

// Create and initialize the sandbox
const sandbox = await DenoSandbox.create({
  memoryMb: 1024,
  lifetime: "10m",
});

try {
  const agent = createDeepAgent({
    model: new ChatAnthropic({ model: "claude-opus-4-8" }),
    systemPrompt: "You are a JavaScript coding assistant with sandbox access.",
    backend: sandbox,
  });

  const result = await agent.invoke({
    messages: [
      {
        role: "user",
        content:
          "Create a simple HTTP server using Deno.serve and test it with curl",
      },
    ],
  });
} finally {
  await sandbox.close();
}
```

For more information, see [Sandboxes](/oss/javascript/deepagents/sandboxes).

## Human-in-the-loop

Some tool operations may be sensitive and require human approval before execution.
You can configure the approval for each tool:

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { tool } from "langchain";
import { createDeepAgent } from "deepagents";
import { MemorySaver } from "@langchain/langgraph";
import { z } from "zod";

const removeFile = tool(
  async ({ path }: { path: string }) => {
    return `Deleted ${path}`;
  },
  {
    name: "remove_file",
    description: "Delete a file from the filesystem.",
    schema: z.object({
      path: z.string(),
    }),
  },
);

const fetchFile = tool(
  async ({ path }: { path: string }) => {
    return `Contents of ${path}`;
  },
  {
    name: "fetch_file",
    description: "Read a file from the filesystem.",
    schema: z.object({
      path: z.string(),
    }),
  },
);

const notifyEmail = tool(
  async ({
    to,
    subject,
    body,
  }: {
    to: string;
    subject: string;
    body: string;
  }) => {
    return `Sent email to ${to}`;
  },
  {
    name: "notify_email",
    description: "Send an email.",
    schema: z.object({
      to: z.string(),
      subject: z.string(),
      body: z.string(),
    }),
  },
);

// Checkpointer is REQUIRED for human-in-the-loop
const checkpointer = new MemorySaver();

const agent = createDeepAgent({
  model: "google_genai:gemini-3.5-flash",
  tools: [removeFile, fetchFile, notifyEmail],
  interruptOn: {
    remove_file: true, // Default: approve, edit, reject, respond
    fetch_file: false, // No interrupts needed
    notify_email: { allowedDecisions: ["approve", "reject"] }, // No editing
  },
  checkpointer, // Required!
});
```

You can configure interrupt for agents and subagents on tool call as well as from within tool calls.
For more information, see [Human-in-the-loop](/oss/javascript/deepagents/human-in-the-loop).

## Skills

You can use [skills](/oss/javascript/deepagents/overview) to provide your deep agent with new capabilities and expertise.
While [tools](/oss/javascript/deepagents/customization#tools) tend to cover lower level functionality like native file system actions or planning, skills can contain detailed instructions on how to complete tasks, reference info, and other assets, such as templates.
These files are only loaded by the agent when the agent has determined that the skill is useful for the current prompt.
This progressive disclosure reduces the amount of tokens and context the agent has to consider upon startup.

For example skills, see [Deep Agents example skills](https://github.com/langchain-ai/deepagentsjs/tree/main/examples/skills).

To add skills to your deep agent, pass them as an argument to `create_deep_agent`:

<Tabs>
  <Tab title="StateBackend">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { createDeepAgent, StateBackend, type FileData } from "deepagents";
    import { MemorySaver } from "@langchain/langgraph";

    const checkpointer = new MemorySaver();
    const backend = new StateBackend();

    function createFileData(content: string): FileData {
      const now = new Date().toISOString();
      return {
        content: content.split("\n"),
        created_at: now,
        modified_at: now,
      };
    }

    const skillsFiles: Record<string, FileData> = {};
    const skillUrl =
      "https://raw.githubusercontent.com/langchain-ai/deepagentsjs/refs/heads/main/examples/skills/langgraph-docs/SKILL.md";
    const response = await fetch(skillUrl);
    const skillContent = await response.text();

    skillsFiles["/skills/langgraph-docs/SKILL.md"] = createFileData(skillContent);

    const agent = await createDeepAgent({
      model: "google-genai:gemini-3.1-pro-preview",
      backend,
      checkpointer, // Required !
      // IMPORTANT: deepagents skill source paths are virtual (POSIX) paths relative to the backend root.
      skills: ["/skills/"],
    });

    const config = { configurable: { thread_id: `thread-${Date.now()}` } };
    const result = await agent.invoke(
      {
        messages: [{ role: "user", content: "what is langraph?" }],
        files: skillsFiles,
      },
      config,
    );
    ```
  </Tab>

  <Tab title="StoreBackend">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
    import { InMemoryStore, MemorySaver } from "@langchain/langgraph";

    const checkpointer = new MemorySaver();
    const store = new InMemoryStore();
    const backend = new StoreBackend({
      namespace: () => ["filesystem"],
    });

    function createFileData(content: string): FileData {
      const now = new Date().toISOString();
      return {
        content: content.split("\n"),
        created_at: now,
        modified_at: now,
      };
    }

    const skillUrl =
      "https://raw.githubusercontent.com/langchain-ai/deepagentsjs/refs/heads/main/examples/skills/langgraph-docs/SKILL.md";

    const response = await fetch(skillUrl);
    const skillContent = await response.text();
    const fileData = createFileData(skillContent);

    await store.put(["filesystem"], "/skills/langgraph-docs/SKILL.md", fileData);

    const agent = await createDeepAgent({
      model: "google-genai:gemini-3.1-pro-preview",
      backend,
      store,
      checkpointer,
      // IMPORTANT: deepagents skill source paths are virtual (POSIX) paths relative to the backend root.
      skills: ["/skills/"],
    });

    const config = {
      recursionLimit: 50,
      configurable: { thread_id: `thread-${Date.now()}` },
    };
    const result = await agent.invoke(
      { messages: [{ role: "user", content: "what is langraph?" }] },
      config,
    );
    ```
  </Tab>

  <Tab title="FilesystemBackend">
    ```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { createDeepAgent, FilesystemBackend } from "deepagents";
    import { MemorySaver } from "@langchain/langgraph";

    const checkpointer = new MemorySaver();
    const backend = new FilesystemBackend({ rootDir: process.cwd() });

    const agent = await createDeepAgent({
      model: "google-genai:gemini-3.1-pro-preview",
      backend,
      skills: ["./examples/skills/"],
      interruptOn: {
        read_file: true,
        write_file: true,
        delete_file: true,
      },
      checkpointer, // Required!
    });

    const config = { configurable: { thread_id: `thread-${Date.now()}` } };
    const result = await agent.invoke(
      { messages: [{ role: "user", content: "what is langraph?" }] },
      config,
    );
    ```
  </Tab>
</Tabs>

## Memory

Use [`AGENTS.md` files](https://agents.md/) to provide extra context to your deep agent.

You can pass one or more file paths to the `memory` parameter when creating your deep agent:

<Tabs>
  <Tab title="StateBackend">
    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, type FileData } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

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
      const checkpointer = new MemorySaver();

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const agent = await createDeepAgent({
        model: "google-genai:gemini-3.5-flash",
        memory: ["/AGENTS.md"],
        checkpointer: checkpointer,
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
          // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
          files: { "/AGENTS.md": createFileData(agentsMd) },
        },
        { configurable: { thread_id: "12345" } },
      );
      ```

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, type FileData } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

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
      const checkpointer = new MemorySaver();

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const agent = await createDeepAgent({
        model: "openai:gpt-5.5",
        memory: ["/AGENTS.md"],
        checkpointer: checkpointer,
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
          // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
          files: { "/AGENTS.md": createFileData(agentsMd) },
        },
        { configurable: { thread_id: "12345" } },
      );
      ```

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, type FileData } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

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
      const checkpointer = new MemorySaver();

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const agent = await createDeepAgent({
        model: "anthropic:claude-sonnet-4-6",
        memory: ["/AGENTS.md"],
        checkpointer: checkpointer,
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
          // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
          files: { "/AGENTS.md": createFileData(agentsMd) },
        },
        { configurable: { thread_id: "12345" } },
      );
      ```

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, type FileData } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

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
      const checkpointer = new MemorySaver();

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const agent = await createDeepAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        memory: ["/AGENTS.md"],
        checkpointer: checkpointer,
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
          // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
          files: { "/AGENTS.md": createFileData(agentsMd) },
        },
        { configurable: { thread_id: "12345" } },
      );
      ```

      ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, type FileData } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

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
      const checkpointer = new MemorySaver();

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const agent = await createDeepAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        memory: ["/AGENTS.md"],
        checkpointer: checkpointer,
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
          // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
          files: { "/AGENTS.md": createFileData(agentsMd) },
        },
        { configurable: { thread_id: "12345" } },
      );
      ```

      ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, type FileData } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

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
      const checkpointer = new MemorySaver();

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const agent = await createDeepAgent({
        model: "baseten:zai-org/GLM-5",
        memory: ["/AGENTS.md"],
        checkpointer: checkpointer,
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
          // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
          files: { "/AGENTS.md": createFileData(agentsMd) },
        },
        { configurable: { thread_id: "12345" } },
      );
      ```

      ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, type FileData } from "deepagents";
      import { MemorySaver } from "@langchain/langgraph";

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
      const checkpointer = new MemorySaver();

      function createFileData(content: string): FileData {
        const now = new Date().toISOString();
        return {
          content,
          mimeType: "text/plain",
          created_at: now,
          modified_at: now,
        };
      }

      const agent = await createDeepAgent({
        model: "ollama:devstral-2",
        memory: ["/AGENTS.md"],
        checkpointer: checkpointer,
      });

      const result = await agent.invoke(
        {
          messages: [
            {
              role: "user",
              content: "Please tell me what's in your memory files.",
            },
          ],
          // Seed the default StateBackend's in-state filesystem (virtual paths must start with "/").
          files: { "/AGENTS.md": createFileData(agentsMd) },
        },
        { configurable: { thread_id: "12345" } },
      );
      ```
    </CodeGroup>
  </Tab>

  <Tab title="StoreBackend">
    <CodeGroup>
      ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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
        model: "google-genai:gemini-3.5-flash",
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

      ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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
        model: "openai:gpt-5.5",
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

      ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
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
        model: "anthropic:claude-sonnet-4-6",
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

      ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
      import { createDeepAgent, StoreBackend, type FileData } from "deepagents";
