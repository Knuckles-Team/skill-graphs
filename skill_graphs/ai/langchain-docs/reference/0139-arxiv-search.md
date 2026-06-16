# arxiv-search

Search arXiv for papers matching the user's query.

## Instructions

1. Run `scripts/search.ts` with the user's query as an argument.
2. Parse the results and present them with title, authors, abstract summary, and link.
3. If the user asks for more detail on a specific paper, fetch the full abstract.
```

The agent can *read* scripts from any backend, but to *execute* them, the agent needs access to a shell, which only [sandbox backends](/oss/javascript/deepagents/sandboxes) provide.

[Sandbox backends](/oss/javascript/deepagents/sandboxes) run in isolated containers. Skill files stored outside the sandbox are not available inside it, which means the agent cannot execute skill scripts or access skill resources unless they are transferred in first. Use [custom middleware](/oss/javascript/langchain/middleware/custom) to handle this transfer:

* **`before_agent`**: Read skill files from the backend and upload them into the sandbox so the agent can execute scripts from the start.
* **`after_agent`**: Download any updated or newly created skill files from the sandbox and write them back to the backend so changes persist across runs.

<CodeGroup>
  ```ts Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { readFile, readdir } from "node:fs/promises";
  import { join, posix, relative, resolve } from "node:path";
  import { fileURLToPath } from "node:url";

  import { createMiddleware } from "langchain";
  import {
    CompositeBackend,
    createDeepAgent,
    type FileData,
    StoreBackend,
  } from "deepagents";
  import { InMemoryStore } from "@langchain/langgraph";

  import { DaytonaSandbox } from "@langchain/daytona";

  /** Identical skill bundles for every user: one shared store namespace. */
  const SKILLS_SHARED_NAMESPACE = ["skills", "builtin"] as const;

  function createFileData(content: string): FileData {
    const now = new Date().toISOString();
    return {
      content: content.split("\n"),
      created_at: now,
      modified_at: now,
    };
  }

  function normalizeSkillsStoreKey(key: string): string {
    const k = String(key);
    if (k.includes("..") || /[*?]/.test(k)) {
      throw new Error(`Invalid key: ${key}`);
    }
    return k.startsWith("/") ? k : `/${k}`;
  }

  async function walkFiles(dir: string): Promise<string[]> {
    const entries = await readdir(dir, { withFileTypes: true });
    const files: string[] = [];
    for (const entry of entries) {
      const fullPath = join(dir, entry.name);
      if (entry.isDirectory()) {
        files.push(...(await walkFiles(fullPath)));
      } else if (entry.isFile()) {
        files.push(fullPath);
      }
    }
    return files.sort((a, b) => a.localeCompare(b));
  }

  /** Load canonical skill files from disk into the shared store namespace (run once at deploy).
   *  You can retrieve skills from any source (local filesystem, remote URL, etc.).
   */
  async function seedSkillStore(store: InMemoryStore) {
    const moduleDir = resolve(fileURLToPath(new URL(".", import.meta.url)));
    const skillsDir = resolve(moduleDir, "skills");
    const filePaths = await walkFiles(skillsDir);
    for (const filePath of filePaths) {
      const rel = relative(skillsDir, filePath);
      // StoreBackend keys are paths *relative to the routed backend root*.
      // CompositeBackend strips the route prefix (`/skills/`) before delegating,
      // so store keys should look like "/<skillname>/SKILL.md".
      const key = `/${posix.normalize(rel.split("\\").join("/"))}`;
      const content = await readFile(filePath, "utf8");
      await store.put([...SKILLS_SHARED_NAMESPACE], key, createFileData(content));
    }
  }

  /** Copy shared skill files from the store into the sandbox before each agent run. */
  function createSkillSandboxSyncMiddleware(backend: CompositeBackend) {
    return createMiddleware({
      name: "SkillSandboxSyncMiddleware",
      beforeAgent: async (state, runtime) => {
        const store = (runtime as any).store;
        if (!store) {
          throw new Error(
            "Store is required for syncing skills into the sandbox. " +
              "Pass `store` to createDeepAgent and ensure your runtime provides it.",
          );
        }

        const encoder = new TextEncoder();
        const files: Array<[string, Uint8Array]> = [];

        for (const item of await store.search([...SKILLS_SHARED_NAMESPACE])) {
          const normalized = normalizeSkillsStoreKey(String(item.key));
          const data = item.value as FileData;
          // CompositeBackend routes paths and batches uploads to the right backend.
          files.push([
            `/skills${normalized}`,
            encoder.encode(data.content.join("\n")),
          ]);
        }

        if (files.length > 0) await backend.uploadFiles(files);

        return state;
      },
    });
  }

  async function main() {
    const store = new InMemoryStore();
    await seedSkillStore(store);

    const sandbox = await DaytonaSandbox.create({
      language: "python",
      timeout: 300,
    });

    const backend = new CompositeBackend(sandbox, {
      "/skills/": new StoreBackend({
        store,
        namespace: () => [...SKILLS_SHARED_NAMESPACE],
      } as any),
    });

    try {
      const agent = await createDeepAgent({
        model: "google-genai:gemini-3.5-flash",
        backend,
        skills: ["/skills/"],
        store,
        middleware: [createSkillSandboxSyncMiddleware(backend)],
      });

    } finally {
      await sandbox.close();
    }
  }

  main().catch((err) => {
    console.error(err);
    process.exitCode = 1;
  });
  ```

  ```ts OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { readFile, readdir } from "node:fs/promises";
  import { join, posix, relative, resolve } from "node:path";
  import { fileURLToPath } from "node:url";

  import { createMiddleware } from "langchain";
  import {
    CompositeBackend,
    createDeepAgent,
    type FileData,
    StoreBackend,
  } from "deepagents";
  import { InMemoryStore } from "@langchain/langgraph";

  import { DaytonaSandbox } from "@langchain/daytona";

  /** Identical skill bundles for every user: one shared store namespace. */
  const SKILLS_SHARED_NAMESPACE = ["skills", "builtin"] as const;

  function createFileData(content: string): FileData {
    const now = new Date().toISOString();
    return {
      content: content.split("\n"),
      created_at: now,
      modified_at: now,
    };
  }

  function normalizeSkillsStoreKey(key: string): string {
    const k = String(key);
    if (k.includes("..") || /[*?]/.test(k)) {
      throw new Error(`Invalid key: ${key}`);
    }
    return k.startsWith("/") ? k : `/${k}`;
  }

  async function walkFiles(dir: string): Promise<string[]> {
    const entries = await readdir(dir, { withFileTypes: true });
    const files: string[] = [];
    for (const entry of entries) {
      const fullPath = join(dir, entry.name);
      if (entry.isDirectory()) {
        files.push(...(await walkFiles(fullPath)));
      } else if (entry.isFile()) {
        files.push(fullPath);
      }
    }
    return files.sort((a, b) => a.localeCompare(b));
  }

  /** Load canonical skill files from disk into the shared store namespace (run once at deploy).
   *  You can retrieve skills from any source (local filesystem, remote URL, etc.).
   */
  async function seedSkillStore(store: InMemoryStore) {
    const moduleDir = resolve(fileURLToPath(new URL(".", import.meta.url)));
    const skillsDir = resolve(moduleDir, "skills");
    const filePaths = await walkFiles(skillsDir);
    for (const filePath of filePaths) {
      const rel = relative(skillsDir, filePath);
      // StoreBackend keys are paths *relative to the routed backend root*.
      // CompositeBackend strips the route prefix (`/skills/`) before delegating,
      // so store keys should look like "/<skillname>/SKILL.md".
      const key = `/${posix.normalize(rel.split("\\").join("/"))}`;
      const content = await readFile(filePath, "utf8");
      await store.put([...SKILLS_SHARED_NAMESPACE], key, createFileData(content));
    }
  }

  /** Copy shared skill files from the store into the sandbox before each agent run. */
  function createSkillSandboxSyncMiddleware(backend: CompositeBackend) {
    return createMiddleware({
      name: "SkillSandboxSyncMiddleware",
      beforeAgent: async (state, runtime) => {
        const store = (runtime as any).store;
        if (!store) {
          throw new Error(
            "Store is required for syncing skills into the sandbox. " +
              "Pass `store` to createDeepAgent and ensure your runtime provides it.",
          );
        }

        const encoder = new TextEncoder();
        const files: Array<[string, Uint8Array]> = [];

        for (const item of await store.search([...SKILLS_SHARED_NAMESPACE])) {
          const normalized = normalizeSkillsStoreKey(String(item.key));
          const data = item.value as FileData;
          // CompositeBackend routes paths and batches uploads to the right backend.
          files.push([
            `/skills${normalized}`,
            encoder.encode(data.content.join("\n")),
          ]);
        }

        if (files.length > 0) await backend.uploadFiles(files);

        return state;
      },
    });
  }

  async function main() {
    const store = new InMemoryStore();
    await seedSkillStore(store);

    const sandbox = await DaytonaSandbox.create({
      language: "python",
      timeout: 300,
    });

    const backend = new CompositeBackend(sandbox, {
      "/skills/": new StoreBackend({
        store,
        namespace: () => [...SKILLS_SHARED_NAMESPACE],
      } as any),
    });

    try {
      const agent = await createDeepAgent({
        model: "openai:gpt-5.5",
        backend,
        skills: ["/skills/"],
        store,
        middleware: [createSkillSandboxSyncMiddleware(backend)],
      });

    } finally {
      await sandbox.close();
    }
  }

  main().catch((err) => {
    console.error(err);
    process.exitCode = 1;
  });
  ```

  ```ts Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { readFile, readdir } from "node:fs/promises";
  import { join, posix, relative, resolve } from "node:path";
  import { fileURLToPath } from "node:url";

  import { createMiddleware } from "langchain";
  import {
    CompositeBackend,
    createDeepAgent,
    type FileData,
    StoreBackend,
  } from "deepagents";
  import { InMemoryStore } from "@langchain/langgraph";

  import { DaytonaSandbox } from "@langchain/daytona";

  /** Identical skill bundles for every user: one shared store namespace. */
  const SKILLS_SHARED_NAMESPACE = ["skills", "builtin"] as const;

  function createFileData(content: string): FileData {
    const now = new Date().toISOString();
    return {
      content: content.split("\n"),
      created_at: now,
      modified_at: now,
    };
  }

  function normalizeSkillsStoreKey(key: string): string {
    const k = String(key);
    if (k.includes("..") || /[*?]/.test(k)) {
      throw new Error(`Invalid key: ${key}`);
    }
    return k.startsWith("/") ? k : `/${k}`;
  }

  async function walkFiles(dir: string): Promise<string[]> {
    const entries = await readdir(dir, { withFileTypes: true });
    const files: string[] = [];
    for (const entry of entries) {
      const fullPath = join(dir, entry.name);
      if (entry.isDirectory()) {
        files.push(...(await walkFiles(fullPath)));
      } else if (entry.isFile()) {
        files.push(fullPath);
      }
    }
    return files.sort((a, b) => a.localeCompare(b));
  }

  /** Load canonical skill files from disk into the shared store namespace (run once at deploy).
   *  You can retrieve skills from any source (local filesystem, remote URL, etc.).
   */
  async function seedSkillStore(store: InMemoryStore) {
    const moduleDir = resolve(fileURLToPath(new URL(".", import.meta.url)));
    const skillsDir = resolve(moduleDir, "skills");
    const filePaths = await walkFiles(skillsDir);
    for (const filePath of filePaths) {
      const rel = relative(skillsDir, filePath);
      // StoreBackend keys are paths *relative to the routed backend root*.
      // CompositeBackend strips the route prefix (`/skills/`) before delegating,
      // so store keys should look like "/<skillname>/SKILL.md".
      const key = `/${posix.normalize(rel.split("\\").join("/"))}`;
      const content = await readFile(filePath, "utf8");
      await store.put([...SKILLS_SHARED_NAMESPACE], key, createFileData(content));
    }
  }

  /** Copy shared skill files from the store into the sandbox before each agent run. */
  function createSkillSandboxSyncMiddleware(backend: CompositeBackend) {
    return createMiddleware({
      name: "SkillSandboxSyncMiddleware",
      beforeAgent: async (state, runtime) => {
        const store = (runtime as any).store;
        if (!store) {
          throw new Error(
            "Store is required for syncing skills into the sandbox. " +
              "Pass `store` to createDeepAgent and ensure your runtime provides it.",
          );
        }

        const encoder = new TextEncoder();
        const files: Array<[string, Uint8Array]> = [];

        for (const item of await store.search([...SKILLS_SHARED_NAMESPACE])) {
          const normalized = normalizeSkillsStoreKey(String(item.key));
          const data = item.value as FileData;
          // CompositeBackend routes paths and batches uploads to the right backend.
          files.push([
            `/skills${normalized}`,
            encoder.encode(data.content.join("\n")),
          ]);
        }

        if (files.length > 0) await backend.uploadFiles(files);

        return state;
      },
    });
  }

  async function main() {
    const store = new InMemoryStore();
    await seedSkillStore(store);

    const sandbox = await DaytonaSandbox.create({
      language: "python",
      timeout: 300,
    });

    const backend = new CompositeBackend(sandbox, {
      "/skills/": new StoreBackend({
        store,
        namespace: () => [...SKILLS_SHARED_NAMESPACE],
      } as any),
    });

    try {
      const agent = await createDeepAgent({
        model: "anthropic:claude-sonnet-4-6",
        backend,
        skills: ["/skills/"],
        store,
        middleware: [createSkillSandboxSyncMiddleware(backend)],
      });

    } finally {
      await sandbox.close();
    }
  }

  main().catch((err) => {
    console.error(err);
    process.exitCode = 1;
  });
  ```

  ```ts OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { readFile, readdir } from "node:fs/promises";
  import { join, posix, relative, resolve } from "node:path";
  import { fileURLToPath } from "node:url";

  import { createMiddleware } from "langchain";
  import {
    CompositeBackend,
    createDeepAgent,
    type FileData,
    StoreBackend,
  } from "deepagents";
  import { InMemoryStore } from "@langchain/langgraph";

  import { DaytonaSandbox } from "@langchain/daytona";

  /** Identical skill bundles for every user: one shared store namespace. */
  const SKILLS_SHARED_NAMESPACE = ["skills", "builtin"] as const;

  function createFileData(content: string): FileData {
    const now = new Date().toISOString();
    return {
      content: content.split("\n"),
      created_at: now,
      modified_at: now,
    };
  }

  function normalizeSkillsStoreKey(key: string): string {
    const k = String(key);
    if (k.includes("..") || /[*?]/.test(k)) {
      throw new Error(`Invalid key: ${key}`);
    }
    return k.startsWith("/") ? k : `/${k}`;
  }

  async function walkFiles(dir: string): Promise<string[]> {
    const entries = await readdir(dir, { withFileTypes: true });
    const files: string[] = [];
    for (const entry of entries) {
      const fullPath = join(dir, entry.name);
      if (entry.isDirectory()) {
        files.push(...(await walkFiles(fullPath)));
      } else if (entry.isFile()) {
        files.push(fullPath);
      }
    }
    return files.sort((a, b) => a.localeCompare(b));
  }

  /** Load canonical skill files from disk into the shared store namespace (run once at deploy).
   *  You can retrieve skills from any source (local filesystem, remote URL, etc.).
   */
  async function seedSkillStore(store: InMemoryStore) {
    const moduleDir = resolve(fileURLToPath(new URL(".", import.meta.url)));
    const skillsDir = resolve(moduleDir, "skills");
    const filePaths = await walkFiles(skillsDir);
    for (const filePath of filePaths) {
      const rel = relative(skillsDir, filePath);
      // StoreBackend keys are paths *relative to the routed backend root*.
      // CompositeBackend strips the route prefix (`/skills/`) before delegating,
      // so store keys should look like "/<skillname>/SKILL.md".
      const key = `/${posix.normalize(rel.split("\\").join("/"))}`;
      const content = await readFile(filePath, "utf8");
      await store.put([...SKILLS_SHARED_NAMESPACE], key, createFileData(content));
    }
  }

  /** Copy shared skill files from the store into the sandbox before each agent run. */
  function createSkillSandboxSyncMiddleware(backend: CompositeBackend) {
    return createMiddleware({
      name: "SkillSandboxSyncMiddleware",
      beforeAgent: async (state, runtime) => {
        const store = (runtime as any).store;
        if (!store) {
          throw new Error(
            "Store is required for syncing skills into the sandbox. " +
              "Pass `store` to createDeepAgent and ensure your runtime provides it.",
          );
        }

        const encoder = new TextEncoder();
        const files: Array<[string, Uint8Array]> = [];

        for (const item of await store.search([...SKILLS_SHARED_NAMESPACE])) {
          const normalized = normalizeSkillsStoreKey(String(item.key));
          const data = item.value as FileData;
          // CompositeBackend routes paths and batches uploads to the right backend.
          files.push([
            `/skills${normalized}`,
            encoder.encode(data.content.join("\n")),
          ]);
        }

        if (files.length > 0) await backend.uploadFiles(files);

        return state;
      },
    });
  }

  async function main() {
    const store = new InMemoryStore();
    await seedSkillStore(store);

    const sandbox = await DaytonaSandbox.create({
      language: "python",
      timeout: 300,
    });

    const backend = new CompositeBackend(sandbox, {
      "/skills/": new StoreBackend({
        store,
        namespace: () => [...SKILLS_SHARED_NAMESPACE],
      } as any),
    });

    try {
      const agent = await createDeepAgent({
        model: "openrouter:anthropic/claude-sonnet-4-6",
        backend,
        skills: ["/skills/"],
        store,
        middleware: [createSkillSandboxSyncMiddleware(backend)],
      });

    } finally {
      await sandbox.close();
    }
  }

  main().catch((err) => {
    console.error(err);
    process.exitCode = 1;
  });
  ```

  ```ts Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { readFile, readdir } from "node:fs/promises";
  import { join, posix, relative, resolve } from "node:path";
  import { fileURLToPath } from "node:url";

  import { createMiddleware } from "langchain";
  import {
    CompositeBackend,
    createDeepAgent,
    type FileData,
    StoreBackend,
  } from "deepagents";
  import { InMemoryStore } from "@langchain/langgraph";

  import { DaytonaSandbox } from "@langchain/daytona";

  /** Identical skill bundles for every user: one shared store namespace. */
  const SKILLS_SHARED_NAMESPACE = ["skills", "builtin"] as const;

  function createFileData(content: string): FileData {
    const now = new Date().toISOString();
    return {
      content: content.split("\n"),
      created_at: now,
      modified_at: now,
    };
  }

  function normalizeSkillsStoreKey(key: string): string {
    const k = String(key);
    if (k.includes("..") || /[*?]/.test(k)) {
      throw new Error(`Invalid key: ${key}`);
    }
    return k.startsWith("/") ? k : `/${k}`;
  }

  async function walkFiles(dir: string): Promise<string[]> {
    const entries = await readdir(dir, { withFileTypes: true });
    const files: string[] = [];
    for (const entry of entries) {
      const fullPath = join(dir, entry.name);
      if (entry.isDirectory()) {
        files.push(...(await walkFiles(fullPath)));
      } else if (entry.isFile()) {
        files.push(fullPath);
      }
    }
    return files.sort((a, b) => a.localeCompare(b));
  }

  /** Load canonical skill files from disk into the shared store namespace (run once at deploy).
   *  You can retrieve skills from any source (local filesystem, remote URL, etc.).
   */
  async function seedSkillStore(store: InMemoryStore) {
    const moduleDir = resolve(fileURLToPath(new URL(".", import.meta.url)));
    const skillsDir = resolve(moduleDir, "skills");
    const filePaths = await walkFiles(skillsDir);
    for (const filePath of filePaths) {
      const rel = relative(skillsDir, filePath);
      // StoreBackend keys are paths *relative to the routed backend root*.
      // CompositeBackend strips the route prefix (`/skills/`) before delegating,
      // so store keys should look like "/<skillname>/SKILL.md".
      const key = `/${posix.normalize(rel.split("\\").join("/"))}`;
      const content = await readFile(filePath, "utf8");
      await store.put([...SKILLS_SHARED_NAMESPACE], key, createFileData(content));
    }
  }

  /** Copy shared skill files from the store into the sandbox before each agent run. */
  function createSkillSandboxSyncMiddleware(backend: CompositeBackend) {
    return createMiddleware({
      name: "SkillSandboxSyncMiddleware",
      beforeAgent: async (state, runtime) => {
        const store = (runtime as any).store;
        if (!store) {
          throw new Error(
            "Store is required for syncing skills into the sandbox. " +
              "Pass `store` to createDeepAgent and ensure your runtime provides it.",
          );
        }

        const encoder = new TextEncoder();
        const files: Array<[string, Uint8Array]> = [];

        for (const item of await store.search([...SKILLS_SHARED_NAMESPACE])) {
          const normalized = normalizeSkillsStoreKey(String(item.key));
          const data = item.value as FileData;
          // CompositeBackend routes paths and batches uploads to the right backend.
          files.push([
            `/skills${normalized}`,
            encoder.encode(data.content.join("\n")),
          ]);
        }

        if (files.length > 0) await backend.uploadFiles(files);

        return state;
      },
    });
  }

  async function main() {
    const store = new InMemoryStore();
    await seedSkillStore(store);

    const sandbox = await DaytonaSandbox.create({
      language: "python",
      timeout: 300,
    });

    const backend = new CompositeBackend(sandbox, {
      "/skills/": new StoreBackend({
        store,
        namespace: () => [...SKILLS_SHARED_NAMESPACE],
      } as any),
    });

    try {
      const agent = await createDeepAgent({
        model: "fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
        backend,
        skills: ["/skills/"],
        store,
        middleware: [createSkillSandboxSyncMiddleware(backend)],
      });

    } finally {
      await sandbox.close();
    }
  }

  main().catch((err) => {
    console.error(err);
    process.exitCode = 1;
  });
  ```

  ```ts Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { readFile, readdir } from "node:fs/promises";
  import { join, posix, relative, resolve } from "node:path";
  import { fileURLToPath } from "node:url";

  import { createMiddleware } from "langchain";
  import {
    CompositeBackend,
    createDeepAgent,
    type FileData,
    StoreBackend,
  } from "deepagents";
  import { InMemoryStore } from "@langchain/langgraph";

  import { DaytonaSandbox } from "@langchain/daytona";

  /** Identical skill bundles for every user: one shared store namespace. */
  const SKILLS_SHARED_NAMESPACE = ["skills", "builtin"] as const;

  function createFileData(content: string): FileData {
    const now = new Date().toISOString();
    return {
      content: content.split("\n"),
      created_at: now,
      modified_at: now,
    };
  }

  function normalizeSkillsStoreKey(key: string): string {
    const k = String(key);
    if (k.includes("..") || /[*?]/.test(k)) {
      throw new Error(`Invalid key: ${key}`);
    }
    return k.startsWith("/") ? k : `/${k}`;
  }

  async function walkFiles(dir: string): Promise<string[]> {
    const entries = await readdir(dir, { withFileTypes: true });
    const files: string[] = [];
    for (const entry of entries) {
      const fullPath = join(dir, entry.name);
      if (entry.isDirectory()) {
        files.push(...(await walkFiles(fullPath)));
      } else if (entry.isFile()) {
        files.push(fullPath);
      }
    }
    return files.sort((a, b) => a.localeCompare(b));
  }

  /** Load canonical skill files from disk into the shared store namespace (run once at deploy).
   *  You can retrieve skills from any source (local filesystem, remote URL, etc.).
   */
  async function seedSkillStore(store: InMemoryStore) {
    const moduleDir = resolve(fileURLToPath(new URL(".", import.meta.url)));
    const skillsDir = resolve(moduleDir, "skills");
    const filePaths = await walkFiles(skillsDir);
    for (const filePath of filePaths) {
      const rel = relative(skillsDir, filePath);
      // StoreBackend keys are paths *relative to the routed backend root*.
      // CompositeBackend strips the route prefix (`/skills/`) before delegating,
      // so store keys should look like "/<skillname>/SKILL.md".
      const key = `/${posix.normalize(rel.split("\\").join("/"))}`;
      const content = await readFile(filePath, "utf8");
      await store.put([...SKILLS_SHARED_NAMESPACE], key, createFileData(content));
    }
  }

  /** Copy shared skill files from the store into the sandbox before each agent run. */
  function createSkillSandboxSyncMiddleware(backend: CompositeBackend) {
    return createMiddleware({
      name: "SkillSandboxSyncMiddleware",
      beforeAgent: async (state, runtime) => {
        const store = (runtime as any).store;
        if (!store) {
          throw new Error(
            "Store is required for syncing skills into the sandbox. " +
              "Pass `store` to createDeepAgent and ensure your runtime provides it.",
          );
        }

        const encoder = new TextEncoder();
        const files: Array<[string, Uint8Array]> = [];

        for (const item of await store.search([...SKILLS_SHARED_NAMESPACE])) {
          const normalized = normalizeSkillsStoreKey(String(item.key));
          const data = item.value as FileData;
          // CompositeBackend routes paths and batches uploads to the right backend.
          files.push([
            `/skills${normalized}`,
            encoder.encode(data.content.join("\n")),
          ]);
        }

        if (files.length > 0) await backend.uploadFiles(files);

        return state;
      },
    });
  }

  async function main() {
    const store = new InMemoryStore();
    await seedSkillStore(store);

    const sandbox = await DaytonaSandbox.create({
      language: "python",
      timeout: 300,
    });

    const backend = new CompositeBackend(sandbox, {
      "/skills/": new StoreBackend({
        store,
        namespace: () => [...SKILLS_SHARED_NAMESPACE],
      } as any),
    });

    try {
      const agent = await createDeepAgent({
        model: "baseten:zai-org/GLM-5",
        backend,
        skills: ["/skills/"],
        store,
        middleware: [createSkillSandboxSyncMiddleware(backend)],
      });

    } finally {
      await sandbox.close();
    }
  }

  main().catch((err) => {
    console.error(err);
    process.exitCode = 1;
  });
  ```

  ```ts Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { readFile, readdir } from "node:fs/promises";
  import { join, posix, relative, resolve } from "node:path";
  import { fileURLToPath } from "node:url";

  import { createMiddleware } from "langchain";
  import {
    CompositeBackend,
    createDeepAgent,
    type FileData,
    StoreBackend,
  } from "deepagents";
  import { InMemoryStore } from "@langchain/langgraph";

  import { DaytonaSandbox } from "@langchain/daytona";

  /** Identical skill bundles for every user: one shared store namespace. */
  const SKILLS_SHARED_NAMESPACE = ["skills", "builtin"] as const;

  function createFileData(content: string): FileData {
    const now = new Date().toISOString();
    return {
      content: content.split("\n"),
      created_at: now,
      modified_at: now,
    };
  }

  function normalizeSkillsStoreKey(key: string): string {
    const k = String(key);
    if (k.includes("..") || /[*?]/.test(k)) {
      throw new Error(`Invalid key: ${key}`);
    }
    return k.startsWith("/") ? k : `/${k}`;
  }

  async function walkFiles(dir: string): Promise<string[]> {
    const entries = await readdir(dir, { withFileTypes: true });
    const files: string[] = [];
    for (const entry of entries) {
      const fullPath = join(dir, entry.name);
      if (entry.isDirectory()) {
        files.push(...(await walkFiles(fullPath)));
      } else if (entry.isFile()) {
        files.push(fullPath);
      }
    }
    return files.sort((a, b) => a.localeCompare(b));
  }

  /** Load canonical skill files from disk into the shared store namespace (run once at deploy).
   *  You can retrieve skills from any source (local filesystem, remote URL, etc.).
   */
  async function seedSkillStore(store: InMemoryStore) {
    const moduleDir = resolve(fileURLToPath(new URL(".", import.meta.url)));
    const skillsDir = resolve(moduleDir, "skills");
    const filePaths = await walkFiles(skillsDir);
    for (const filePath of filePaths) {
      const rel = relative(skillsDir, filePath);
      // StoreBackend keys are paths *relative to the routed backend root*.
      // CompositeBackend strips the route prefix (`/skills/`) before delegating,
      // so store keys should look like "/<skillname>/SKILL.md".
      const key = `/${posix.normalize(rel.split("\\").join("/"))}`;
      const content = await readFile(filePath, "utf8");
      await store.put([...SKILLS_SHARED_NAMESPACE], key, createFileData(content));
    }
  }

  /** Copy shared skill files from the store into the sandbox before each agent run. */
  function createSkillSandboxSyncMiddleware(backend: CompositeBackend) {
    return createMiddleware({
      name: "SkillSandboxSyncMiddleware",
      beforeAgent: async (state, runtime) => {
        const store = (runtime as any).store;
        if (!store) {
          throw new Error(
            "Store is required for syncing skills into the sandbox. " +
              "Pass `store` to createDeepAgent and ensure your runtime provides it.",
          );
        }

        const encoder = new TextEncoder();
        const files: Array<[string, Uint8Array]> = [];

        for (const item of await store.search([...SKILLS_SHARED_NAMESPACE])) {
          const normalized = normalizeSkillsStoreKey(String(item.key));
          const data = item.value as FileData;
          // CompositeBackend routes paths and batches uploads to the right backend.
          files.push([
            `/skills${normalized}`,
            encoder.encode(data.content.join("\n")),
          ]);
        }

        if (files.length > 0) await backend.uploadFiles(files);

        return state;
      },
    });
  }

  async function main() {
    const store = new InMemoryStore();
    await seedSkillStore(store);

    const sandbox = await DaytonaSandbox.create({
      language: "python",
      timeout: 300,
    });

    const backend = new CompositeBackend(sandbox, {
      "/skills/": new StoreBackend({
        store,
        namespace: () => [...SKILLS_SHARED_NAMESPACE],
      } as any),
    });

    try {
      const agent = await createDeepAgent({
        model: "ollama:devstral-2",
        backend,
        skills: ["/skills/"],
        store,
        middleware: [createSkillSandboxSyncMiddleware(backend)],
      });

    } finally {
      await sandbox.close();
    }
  }

  main().catch((err) => {
    console.error(err);
    process.exitCode = 1;
  });
  ```
</CodeGroup>

For a complete example that seeds both skills and memories before execution and syncs both back afterward, see [syncing skills and memories with custom middleware](/oss/javascript/deepagents/going-to-production#example-syncing-skills-and-memories-with-custom-middleware).

## Troubleshooting

Use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-deepagents-skills) traces to debug skill discovery, `read_file` calls on `SKILL.md`, and supporting resource access. Follow the [tracing quickstart](/langsmith/observability-quickstart) to get set up. We recommend you also set up [LangSmith Engine](/langsmith/engine), which monitors your traces, detects issues, and proposes fixes.

### Skill not activated

**Problem**: The agent handles the task without reading the skill's `SKILL.md`.

**Solutions**:

1. **Make the description more specific.** The agent selects skills from the [`description`](#frontmatter-fields) field alone at [discovery](#how-skills-work). Include what the skill does, when to use it, and keywords the agent can match:

   ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   # Good
   description: >-
     Search the arXiv preprint repository for research papers. Use when the
     user asks about academic papers, recent research, or scientific literature.

   # Poor
   description: Helps with research.
   ```

2. **Reduce overlap between skills.** If multiple skills have similar descriptions, the agent may skip the right one or pick the wrong one. Differentiate descriptions or [consolidate related skills](#write-effective-skills).

3. **Confirm the skill is in the `skills` array.** Skills load only from paths you pass at agent creation or from subagent-specific `skills` parameters.

### Skills missing at startup

**Problem**: The agent does not list a skill in its system prompt, or `read_file` on `SKILL.md` fails.

**Solutions**:

1. **Check the skill path.** Paths must use forward slashes and be relative to the backend root. With `FilesystemBackend`, the path is relative to `root_dir`. With `StateBackend`, pass skill files in `invoke(files={...})` using `create_file_data()`.

2. **Validate `SKILL.md` [frontmatter](#frontmatter-fields).** The [`name`](#frontmatter-fields) must match the parent directory name and follow the [Agent Skills specification](https://agentskills.io/specification). Use the [`skills-ref` validation tool](https://github.com/agentskills/agentskills/tree/main/skills-ref) to check formatting.

3. **Check file size.** Deep Agents skips `SKILL.md` files over 10 MB during discovery.

4. **Check layered sources.** When the same skill name appears in multiple sources, the [last source wins](#usage). An older or empty skill from a later path can override the one you expect.

### Supporting files not found

**Problem**: The agent reads `SKILL.md` but cannot access scripts, references, or assets.

**Solutions**:

1. **Reference files from `SKILL.md`.** The agent does not auto-discover supporting files. State what each file contains and when to use it. Use [relative paths](#reference-files-from-skill-md) from the skill root.

2. **Keep paths within the skill directory.** File paths resolve against the backend. Confirm supporting files exist at the paths your instructions reference.

3. **Sync skills into sandboxes.** If you use [sandbox backends](/oss/javascript/deepagents/sandboxes), skill files outside the container are not available until you copy them in. See [Sandbox scripts](#sandbox-scripts) and [syncing skills and memories with custom middleware](/oss/javascript/deepagents/going-to-production#example-syncing-skills-and-memories-with-custom-middleware).

### Scripts fail to run

**Problem**: The agent reads a script but cannot run it.

**Solution**: The agent can read scripts from any backend, but running them requires a [sandbox backend](/oss/javascript/deepagents/sandboxes). See [Execute code with skills](#execute-code-with-skills).

### Subagent cannot access a skill

**Problem**: A custom subagent does not see skills that the main agent uses.

**Solution**: Custom subagents do not inherit the main agent's skills. Add a `skills` parameter to each [subagent definition](#skills-for-subagents) with that subagent's skill source paths. The general-purpose subagent inherits skills from `create_deep_agent` automatically.

## Reference

### Skills, memory, and tools

Skills, [memory](/oss/javascript/deepagents/memory) (`AGENTS.md` files), and tools all provide context or capabilities to the agent. The following table summarizes when to reach for each:

|              | Skills                                                           | Memory                                                        | Tools                                                                             |
| ------------ | ---------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Purpose**  | On-demand capabilities discovered through progressive disclosure | Persistent context loaded at startup                          | Programmatic actions the agent can call                                           |
| **Loading**  | Read only when the agent determines relevance                    | Loaded at agent start                                         | Available every turn                                                              |
| **Format**   | `SKILL.md` in named directories                                  | `AGENTS.md` files                                             | Functions bound to the agent                                                      |
| **Layering** | User, then project (last wins)                                   | User, then project (combined)                                 | Defined at agent creation                                                         |
| **Use when** | Instructions are task-specific and potentially large             | Context is always relevant (project conventions, preferences) | The agent needs a programmatic action, or does not have access to the file system |

These are guidelines, not hard boundaries. In practice, skills and memory sit on a spectrum. An agent can update its own skills as it works, capturing new procedures and refining instructions over time. In this way, skills can function as a form of progressive-disclosure memory: context the agent builds up and retrieves on demand rather than loading on every prompt.

### Frontmatter fields

The [Agent Skills specification](https://agentskills.io/specification) defines the following frontmatter fields:

| Field           | Required | Description                                                                                 |
| --------------- | -------- | ------------------------------------------------------------------------------------------- |
| `name`          | Yes      | Lowercase alphanumeric with hyphens, 1-64 characters. Must match the parent directory name. |
| `description`   | Yes      | What the skill does and when to use it. Max 1,024 characters.                               |
| `license`       | No       | License name or reference to a bundled license file.                                        |
| `compatibility` | No       | Environment requirements (system packages, network access). Max 500 characters.             |
| `metadata`      | No       | Arbitrary key-value pairs for additional properties.                                        |
| `allowed-tools` | No       | Space-separated list of pre-approved tools the skill can use. Experimental.                 |

```md expandable theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
---
name: langgraph-docs
description: Use this skill for requests related to LangGraph in order to fetch relevant documentation to provide accurate, up-to-date guidance.
license: MIT
compatibility: Requires internet access for fetching documentation URLs
metadata:
  author: langchain
  version: "1.0"
allowed-tools: fetch_url
---

# langgraph-docs

Instructions for the agent go here. See [Usage](#usage) for a complete example of skill instructions.
```

<Warning>
  Refer to the full [Agent Skills specification](https://agentskills.io/specification) for detailed constraints and validation rules. In Deep Agents, `SKILL.md` files must be under 10 MB. Files exceeding this limit are skipped during skill loading.
</Warning>

For more example skills, see [Deep Agents example skills](https://github.com/langchain-ai/deepagentsjs/tree/main/examples/skills).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/skills.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
