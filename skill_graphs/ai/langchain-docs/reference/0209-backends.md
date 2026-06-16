# Backends
Source: https://docs.langchain.com/oss/python/deepagents/backends

Choose and configure filesystem backends for Deep Agents. You can specify routes to different backends, implement virtual filesystems, and enforce policies.

Deep Agents expose a filesystem surface to the agent via tools like `ls`, `read_file`, `write_file`, `edit_file`, `glob`, and `grep`. These tools operate through a pluggable backend. The `read_file` tool natively supports image files (`.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`) across all backends, returning them as multimodal content blocks.

Sandboxes and the [`LocalShellBackend`](https://reference.langchain.com/python/deepagents/backends/local_shell/LocalShellBackend) also provide an `execute` tool.
This page explains how to:

* [choose a backend](#specify-a-backend),

* [route different paths to different backends](#route-to-different-backends),

* [implement your own virtual filesystem](#use-a-virtual-filesystem) (e.g., S3 or Postgres),

* [set permissions](#permissions) on filesystem access,

* [comply with the backend protocol](#protocol-reference),

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
| [Sandbox](/oss/python/deepagents/sandboxes)                      | `agent = create_deep_agent(model="google_genai:gemini-3.5-flash", backend=sandbox)` <br />Execute code in isolated environments. Sandboxes provide filesystem tools plus the `execute` tool for running shell commands. Choose from Modal, Daytona, Runloop, AgentCore, LangSmith, Deno, E2B, or local VFS.                                                                                                                                                                                                         |
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

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StateBackend

  # By default we provide a StateBackend
  agent = create_deep_agent(model="google_genai:gemini-3.5-flash")

  # Under the hood, it looks like
  agent2 = create_deep_agent(
      model="openai:gpt-5.5",
      backend=StateBackend(),
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StateBackend

  # By default we provide a StateBackend
  agent = create_deep_agent(model="openai:gpt-5.5")

  # Under the hood, it looks like
  agent2 = create_deep_agent(
      model="openai:gpt-5.5",
      backend=StateBackend(),
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StateBackend

  # By default we provide a StateBackend
  agent = create_deep_agent(model="anthropic:claude-sonnet-4-6")

  # Under the hood, it looks like
  agent2 = create_deep_agent(
      model="openai:gpt-5.5",
      backend=StateBackend(),
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StateBackend

  # By default we provide a StateBackend
  agent = create_deep_agent(model="openrouter:anthropic/claude-sonnet-4-6")

  # Under the hood, it looks like
  agent2 = create_deep_agent(
      model="openai:gpt-5.5",
      backend=StateBackend(),
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StateBackend

  # By default we provide a StateBackend
  agent = create_deep_agent(model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b")

  # Under the hood, it looks like
  agent2 = create_deep_agent(
      model="openai:gpt-5.5",
      backend=StateBackend(),
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StateBackend

  # By default we provide a StateBackend
  agent = create_deep_agent(model="baseten:zai-org/GLM-5")

  # Under the hood, it looks like
  agent2 = create_deep_agent(
      model="openai:gpt-5.5",
      backend=StateBackend(),
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StateBackend

  # By default we provide a StateBackend
  agent = create_deep_agent(model="ollama:devstral-2")

  # Under the hood, it looks like
  agent2 = create_deep_agent(
      model="openai:gpt-5.5",
      backend=StateBackend(),
  )
  ```
</CodeGroup>

**How it works:**

* Stores files in LangGraph agent state for the current thread via [`StateBackend`](https://reference.langchain.com/python/deepagents/backends/state/StateBackend).
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

[`FilesystemBackend`](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend) reads and writes real files under a configurable root directory.

<Warning>
  This backend grants agents direct filesystem read/write access.
  Use with caution and only in appropriate environments.

  **Appropriate use cases:**

  * Local development CLIs (coding assistants, development tools)
  * CI/CD pipelines (see security considerations below)

  **Inappropriate use cases:**

  * Web servers or HTTP APIs - use `StateBackend`, `StoreBackend`, or a [sandbox backend](/oss/python/deepagents/sandboxes) instead

  **Security risks:**

  * Agents can read any accessible file, including secrets (API keys, credentials, `.env` files)
  * Combined with network tools, secrets may be exfiltrated via SSRF attacks
  * File modifications are permanent and irreversible

  **Recommended safeguards:**

  1. Enable [Human-in-the-Loop (HITL) middleware](/oss/python/deepagents/human-in-the-loop) to review sensitive operations.
  2. Exclude secrets from accessible filesystem paths (especially in CI/CD).
  3. Use a [sandbox backend](/oss/python/deepagents/sandboxes) for production environments requiring filesystem interaction.
  4. **Always** use `virtual_mode=True` with `root_dir` to enable path-based access restrictions (blocks `..`, `~`, and absolute paths outside root).

     Note that the default (`virtual_mode=False`) provides no security even with `root_dir` set.
</Warning>

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import FilesystemBackend

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      backend=FilesystemBackend(root_dir=".", virtual_mode=True),
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import FilesystemBackend

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      backend=FilesystemBackend(root_dir=".", virtual_mode=True),
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import FilesystemBackend

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      backend=FilesystemBackend(root_dir=".", virtual_mode=True),
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import FilesystemBackend

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      backend=FilesystemBackend(root_dir=".", virtual_mode=True),
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import FilesystemBackend

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      backend=FilesystemBackend(root_dir=".", virtual_mode=True),
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import FilesystemBackend

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      backend=FilesystemBackend(root_dir=".", virtual_mode=True),
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import FilesystemBackend

  agent = create_deep_agent(
      model="ollama:devstral-2",
      backend=FilesystemBackend(root_dir=".", virtual_mode=True),
  )
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

  ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, FilesystemBackend

  agent = create_deep_agent(
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/workspace/": FilesystemBackend(root_dir="/path/to/project", virtual_mode=True),
          },
      )
  )
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

  1. Enable [Human-in-the-Loop (HITL) middleware](/oss/python/deepagents/human-in-the-loop) to review and approve operations before execution. This is **strongly recommended**.
  2. Run in dedicated development environments only. Never use on shared or production systems.
  3. Use a [sandbox backend](/oss/python/deepagents/sandboxes) for production environments requiring shell execution.

  **Note:** `virtual_mode=True` provides no security with shell access enabled, since commands can access any path on the system.
</Warning>

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import LocalShellBackend

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import LocalShellBackend

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import LocalShellBackend

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import LocalShellBackend

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import LocalShellBackend

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import LocalShellBackend

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import LocalShellBackend

  agent = create_deep_agent(
      model="ollama:devstral-2",
      backend=LocalShellBackend(root_dir=".", virtual_mode=True, env={"PATH": "/usr/bin:/bin"}),
  )
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
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      backend=StoreBackend(
          namespace=lambda rt: (rt.server_info.user.identity,),
      ),
      store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      backend=StoreBackend(
          namespace=lambda rt: (rt.server_info.user.identity,),
      ),
      store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      backend=StoreBackend(
          namespace=lambda rt: (rt.server_info.user.identity,),
      ),
      store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      backend=StoreBackend(
          namespace=lambda rt: (rt.server_info.user.identity,),
      ),
      store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      backend=StoreBackend(
          namespace=lambda rt: (rt.server_info.user.identity,),
      ),
      store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      backend=StoreBackend(
          namespace=lambda rt: (rt.server_info.user.identity,),
      ),
      store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="ollama:devstral-2",
      backend=StoreBackend(
          namespace=lambda rt: (rt.server_info.user.identity,),
      ),
      store=InMemoryStore(),  # Good for local dev; omit for LangSmith Deployment
  )
  ```
</CodeGroup>

<Note>
  When deploying to [LangSmith Deployment](/langsmith/deployment), omit the `store` parameter. The platform automatically provisions a store for your agent.
</Note>

<Tip>
  The `namespace` parameter controls data isolation. For multi-user deployments, always set a [namespace factory](/oss/python/deepagents/backends#namespace-factories) to isolate data per user or tenant.
</Tip>

**How it works:**

* [`StoreBackend`](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend) stores files in a LangGraph [`BaseStore`](https://reference.langchain.com/python/langchain-core/stores/BaseStore) provided by the runtime, enabling cross‑thread durable storage.

**Best for:**

* When you already run with a configured LangGraph store (for example, Redis, Postgres, or cloud implementations behind [`BaseStore`](https://reference.langchain.com/python/langchain-core/stores/BaseStore)).
* When you're deploying your agent through [LangSmith Deployment](/langsmith/deployment) (a store is automatically provisioned for your agent).

#### Namespace factories

A namespace factory controls where `StoreBackend` reads and writes data. It receives a LangGraph [`Runtime`](https://reference.langchain.com/python/langgraph/runtime/Runtime) and returns a tuple of strings used as the store namespace. Use namespace factories to isolate data between users, tenants, or assistants.

Pass the namespace factory to the `namespace` parameter when constructing a `StoreBackend`:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
NamespaceFactory = Callable[[Runtime], tuple[str, ...]]
```

The `Runtime` provides:

* `rt.context` — User-supplied context passed via LangGraph's [context schema](https://langchain-ai.github.io/langgraph/concepts/runtime/) (for example, `user_id`)
* `rt.server_info` — Server-specific metadata when running on LangGraph Server (assistant ID, graph ID, authenticated user)
* `rt.execution_info` — Execution identity information (thread ID, run ID, checkpoint ID)

<Note>
  The `Runtime` argument is available in `deepagents>=0.5.2`. Earlier 0.5.x releases passed a `BackendContext` instead — see [migrating from `BackendContext`](#migrating-from-backendcontext) below. `rt.server_info` and `rt.execution_info` require `deepagents>=0.5.0`.
</Note>

**Common namespace patterns:**

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents.backends import StoreBackend

# Per-user: each user gets their own isolated storage
backend = StoreBackend(
    namespace=lambda rt: (rt.server_info.user.identity,),  # [!code highlight]
)

# Per-assistant: all users of the same assistant share storage
backend = StoreBackend(
    namespace=lambda rt: (
        rt.server_info.assistant_id,  # [!code highlight]
    ),
)
