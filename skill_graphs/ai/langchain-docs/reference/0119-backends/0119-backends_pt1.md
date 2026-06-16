# Backends
Source: https://docs.langchain.com/oss/javascript/deepagents/backends

Choose and configure filesystem backends for Deep Agents. You can specify routes to different backends, implement virtual filesystems, and enforce policies.

Deep Agents expose a filesystem surface to the agent via tools like `ls`, `read_file`, `write_file`, `edit_file`, `glob`, and `grep`. These tools operate through a pluggable backend. The `read_file` tool natively supports image files (`.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`) across all backends, returning them as multimodal content blocks.

The `read_file` tool natively supports binary files (images, PDFs, audio, video) across all backends, returning a `ReadResult` with typed `content` and `mimeType`.

Sandboxes and the [`LocalShellBackend`](https://reference.langchain.com/javascript/deepagents/backends/LocalShellBackend) also provide an `execute` tool.
This page explains how to:

* [choose a backend](#specify-a-backend),

* [route different paths to different backends](#route-to-different-backends),

* [implement your own virtual filesystem](#use-a-virtual-filesystem) (e.g., S3 or Postgres),

* [set permissions](#permissions) on filesystem access,

* [add policy hooks](#add-policy-hooks),
  [work with binary and multimodal files](#multimodal-and-binary-files),

* [comply with the backend protocol](#protocol-reference),

* and [update existing backends to v2](#update-existing-backends-to-v2).

<Tip>
  When you deploy on [LangSmith Deployment](/langsmith/deployment), a store is provisioned automatically. Use [LangSmith](/langsmith/observability) tracing to debug file paths, permission denials, and cross-thread storage. Follow the [observability quickstart](/langsmith/observability-quickstart) to get set up.

  We recommend you also set up [LangSmith Engine](/langsmith/engine), which monitors your traces, detects issues, and proposes fixes.
</Tip>

## Quickstart

Here are a few prebuilt filesystem backends that you can quickly use with your deep agent:

| Built-in backend                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Default](#statebackend)                                         | `agent = create_deep_agent(model="google_genai:gemini-3.5-flash")` <br /> Thread-scoped. The default filesystem backend for an agent is stored in `langgraph` state. Files persist across turns within a thread (via your checkpointer) and are not shared across threads.                                                                                                                                                                                                                                          |
| [Local filesystem persistence](#filesystembackend-local-disk)    | `agent = create_deep_agent(model="google_genai:gemini-3.5-flash", backend=FilesystemBackend(root_dir="/Users/nh/Desktop/"))` <br />This gives the deep agent access to your local machine's filesystem. You can specify the root directory that the agent has access to. Note that any provided `root_dir` must be an absolute path. Typically, wrap in a [CompositeBackend](#compositebackend-router) to keep internal agent data (offloaded tool results, conversation history) separate from your project files. |
| [Durable store (LangGraph store)](#storebackend-langgraph-store) | `agent = create_deep_agent(model="google_genai:gemini-3.5-flash", backend=StoreBackend())` <br />This gives the agent access to long-term storage that is *persisted across threads*. This is great for storing longer term memories or instructions that are applicable to the agent over multiple executions.                                                                                                                                                                                                     |
| [Context Hub](#contexthubbackend)                                | `agent = create_deep_agent(model="google_genai:gemini-3.5-flash", backend=ContextHubBackend("my-agent"))` <br />Stores files durably in a LangSmith Hub repo, without provisioning a separate LangGraph store.                                                                                                                                                                                                                                                                                                      |
| [Sandbox](/oss/javascript/deepagents/sandboxes)                  | `agent = create_deep_agent(model="google_genai:gemini-3.5-flash", backend=sandbox)` <br />Execute code in isolated environments. Sandboxes provide filesystem tools plus the `execute` tool for running shell commands. Choose from Modal, Daytona, Runloop, AgentCore, LangSmith, Deno, E2B, or local VFS.                                                                                                                                                                                                         |
| [Local shell](#localshellbackend-local-shell)                    | `agent = create_deep_agent(model="google_genai:gemini-3.5-flash", backend=LocalShellBackend(root_dir=".", env={"PATH": "/usr/bin:/bin"}))` <br />Filesystem and shell execution directly on the host. No isolation—use only in controlled development environments. See [security considerations](#localshellbackend-local-shell) below.                                                                                                                                                                            |
| [Composite](#compositebackend-router)                            | Thread-scoped by default, `/memories/` persisted across threads. The Composite backend is maximally flexible. You can specify different routes in the filesystem to point towards different backends. See Composite routing below for a ready-to-paste example.                                                                                                                                                                                                                                                     |

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
graph TB
    Tools[Filesystem Tools] --> Backend[Backend]

    Backend --> State[State]
    Backend --> Disk[Filesystem]
    Backend --> Store[Store]
    Backend --> ContextHub[Context Hub]
    Backend --> Sandbox[Sandbox]
    Backend --> LocalShell[Local Shell]
    Backend --> Composite[Composite]
    Backend --> Custom[Custom]

    Composite --> Router{Routes}
    Router --> State
    Router --> Disk
    Router --> Store
    Router --> ContextHub

    Sandbox --> Execute["#43; execute tool"]
    LocalShell --> Execute["#43; execute tool"]

    classDef trigger fill:#F6FFDB,stroke:#6E8900,stroke-width:2px,color:#2E3900
    classDef process fill:#E5F4FF,stroke:#006DDD,stroke-width:2px,color:#030710
    classDef decision fill:#FDF3FF,stroke:#7E65AE,stroke-width:2px,color:#504B5F
    classDef output fill:#EBD0F0,stroke:#885270,stroke-width:2px,color:#441E33

    class Tools trigger
    class Backend,State,Disk,Store,ContextHub,Sandbox,LocalShell,Composite,Custom process
    class Router decision
    class Execute output
```

## Built-in backends

### StateBackend

```ts theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent, StateBackend } from "deepagents";

// By default we provide a StateBackend
const agent = createDeepAgent();

// Under the hood, it looks like
const agent2 = createDeepAgent({
  backend: new StateBackend(),
});
```

**How it works:**

* Stores files in LangGraph agent state for the current thread via [`StateBackend`](https://reference.langchain.com/javascript/deepagents/backends/StateBackend).
* Persists across multiple agent turns on the same thread via checkpoints. Files are not shared across threads.

<Warning>
  Designed to be used from within a graph. Calling backend methods (e.g., `state_backend.upload_files(...)`) outside of a graph run won't take effect until the graph executes.
</Warning>

**Best for:**

* A scratch pad for the agent to write intermediate results.
* Automatic eviction of large tool outputs which the agent can then read back in piece by piece.

Note that this backend is shared between the supervisor agent and subagents, and any files a subagent writes will remain in the LangGraph agent state
even after that subagent's execution is complete. Those files will continue to be available to the supervisor agent and other subagents.

### FilesystemBackend (local disk)

[`FilesystemBackend`](https://reference.langchain.com/javascript/deepagents/backends/FilesystemBackend) reads and writes real files under a configurable root directory.

<Warning>
  This backend grants agents direct filesystem read/write access.
  Use with caution and only in appropriate environments.

  **Appropriate use cases:**

  * Local development CLIs (coding assistants, development tools)
  * CI/CD pipelines (see security considerations below)

  **Inappropriate use cases:**

  * Web servers or HTTP APIs - use `StateBackend`, `StoreBackend`, or a [sandbox backend](/oss/javascript/deepagents/sandboxes) instead

  **Security risks:**

  * Agents can read any accessible file, including secrets (API keys, credentials, `.env` files)
  * Combined with network tools, secrets may be exfiltrated via SSRF attacks
  * File modifications are permanent and irreversible

  **Recommended safeguards:**

  1. Enable [Human-in-the-Loop (HITL) middleware](/oss/javascript/deepagents/human-in-the-loop) to review sensitive operations.
  2. Exclude secrets from accessible filesystem paths (especially in CI/CD).
  3. Use a [sandbox backend](/oss/javascript/deepagents/sandboxes) for production environments requiring filesystem interaction.
  4. **Always** use `virtual_mode=True` with `root_dir` to enable path-based access restrictions (blocks `..`, `~`, and absolute paths outside root).

     Note that the default (`virtual_mode=False`) provides no security even with `root_dir` set.
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

**How it works:**

* Reads/writes real files under a configurable `root_dir`.
* You can optionally set `virtual_mode=True` to sandbox and normalize paths under `root_dir`.
* Uses secure path resolution, prevents unsafe symlink traversal when possible, can use ripgrep for fast `grep`.

**Best for:**

* Local projects on your machine
* CI sandboxes
* Mounted persistent volumes

<Tip>
  **Wrap `FilesystemBackend` in a `CompositeBackend`** for most use cases. Deep Agents automatically write internal data to the backend, including offloaded large tool results (under `/large_tool_results/`) and conversation history (under `/conversation_history/`). When you use `FilesystemBackend` alone, these internal files are written to real disk under `root_dir`, mixing agent artifacts with your project files.

  Use a `CompositeBackend` to route your project directory to `FilesystemBackend` while keeping internal paths in ephemeral `StateBackend` storage:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { createDeepAgent, CompositeBackend, FilesystemBackend, StateBackend } from "deepagents";

  const agent = createDeepAgent({
    backend: new CompositeBackend(
      new StateBackend(),
      {
        "/workspace/": new FilesystemBackend({ rootDir: "/path/to/project", virtualMode: true }),
      },
    ),
  });
  ```

  This way, agent reads and writes under `/workspace/` go to real disk, while offloaded tool results and other internal data stay in ephemeral state. See [Route to different backends](#route-to-different-backends) for more routing patterns.
</Tip>

### LocalShellBackend (local shell)

<Warning>
  This backend grants agents direct filesystem read/write access **and** unrestricted shell execution on your host.
  Use with extreme caution and only in appropriate environments.

  **Appropriate use cases:**

  * Local development CLIs (coding assistants, development tools)
  * Personal development environments where you trust the agent's code
  * CI/CD pipelines with proper secret management

  **Inappropriate use cases:**

  * Production environments (such as web servers, APIs, multi-tenant systems)
  * Processing untrusted user input or executing untrusted code

  **Security risks:**

  * Agents can execute **arbitrary shell commands** with your user's permissions
  * Agents can read any accessible file, including secrets (API keys, credentials, `.env` files)
  * Secrets may be exposed
  * File modifications and command execution are **permanent and irreversible**
  * Commands run directly on your host system
  * Commands can consume unlimited CPU, memory, disk

  **Recommended safeguards:**

  1. Enable [Human-in-the-Loop (HITL) middleware](/oss/javascript/deepagents/human-in-the-loop) to review and approve operations before execution. This is **strongly recommended**.
  2. Run in dedicated development environments only. Never use on shared or production systems.
  3. Use a [sandbox backend](/oss/javascript/deepagents/sandboxes) for production environments requiring shell execution.

  **Note:** `virtual_mode=True` provides no security with shell access enabled, since commands can access any path on the system.
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

**How it works:**

* Extends `FilesystemBackend` with the `execute` tool for running shell commands on the host.
* Commands run directly on your machine using `subprocess.run(shell=True)` with no sandboxing.
* Supports `timeout` (default 120s), `max_output_bytes` (default 100,000), `env`, and `inherit_env` for environment variables.
* Shell commands use `root_dir` as the working directory but can access any path on the system.

**Best for:**

* Local coding assistants and development tools
* Quick iteration during development when you trust the agent

### StoreBackend (LangGraph store)

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

**How it works:**

* [`StoreBackend`](https://reference.langchain.com/javascript/deepagents/backends/StoreBackend) stores files in a LangGraph [`BaseStore`](https://reference.langchain.com/javascript/langchain-core/stores/BaseStore) provided by the runtime, enabling cross‑thread durable storage.

**Best for:**

* When you already run with a configured LangGraph store (for example, Redis, Postgres, or cloud implementations behind [`BaseStore`](https://reference.langchain.com/javascript/langchain-core/stores/BaseStore)).
* When you're deploying your agent through [LangSmith Deployment](/langsmith/deployment) (a store is automatically provisioned for your agent).

#### Namespace factories

A namespace factory controls where `StoreBackend` reads and writes data. It receives a LangGraph [`Runtime`](https://reference.langchain.com/javascript/langchain/index/Runtime) and returns a tuple of strings used as the store namespace. Use namespace factories to isolate data between users, tenants, or assistants.

Pass the namespace factory to the `namespace` parameter when constructing a `StoreBackend`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
NamespaceFactory = Callable[[Runtime], tuple[str, ...]]
```

The `Runtime` provides:

* `rt.context` — User-supplied context passed via LangGraph's [context schema](https://langchain-ai.github.io/langgraph/concepts/runtime/) (for example, `user_id`)

* `rt.serverInfo` — Server-specific metadata when running on LangGraph Server (assistant ID, graph ID, authenticated user)

* `rt.executionInfo` — Execution identity information (thread ID, run ID, checkpoint ID)

<Note>
  The `Runtime` argument is available in `deepagents>=1.9.1`. Earlier 1.9.x releases passed a `BackendContext` instead — see [migrating from `BackendContext`](#migrating-from-backendcontext) below. `rt.serverInfo` and `rt.executionInfo` require `deepagents>=1.9.0`.
</Note>

**Common namespace patterns:**

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { StoreBackend } from "deepagents";

// Per-user: each user gets their own isolated storage
const backend = new StoreBackend({
