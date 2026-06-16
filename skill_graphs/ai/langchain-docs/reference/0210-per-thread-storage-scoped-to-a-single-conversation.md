# Per-thread: storage scoped to a single conversation
backend = StoreBackend(
    namespace=lambda rt: (
        rt.execution_info.thread_id,  # [!code highlight]
    ),
)
```

You can combine multiple components to create more specific scopes — for example, `(user_id, thread_id)` for per-user per-conversation isolation, or append a suffix like `"filesystem"` to disambiguate when the same scope uses multiple store namespaces.

Namespace components must contain only alphanumeric characters, hyphens, underscores, dots, `@`, `+`, colons, and tildes. Wildcards (`*`, `?`) are rejected to prevent glob injection.

<Warning>
  The `namespace` parameter will be **required** in v0.5.0. Always set it explicitly for new code.
</Warning>

<Note>
  When no namespace factory is provided, the legacy default uses the `assistant_id` from LangGraph config metadata. This means all users of the same [assistant](/langsmith/assistants) share the same storage. For multi-user [going to production](/oss/python/deepagents/going-to-production), always provide a namespace factory.
</Note>

### ContextHubBackend

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import ContextHubBackend

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      backend=ContextHubBackend("my-agent"),
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import ContextHubBackend

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      backend=ContextHubBackend("my-agent"),
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import ContextHubBackend

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      backend=ContextHubBackend("my-agent"),
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import ContextHubBackend

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      backend=ContextHubBackend("my-agent"),
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import ContextHubBackend

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      backend=ContextHubBackend("my-agent"),
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import ContextHubBackend

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      backend=ContextHubBackend("my-agent"),
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import ContextHubBackend

  agent = create_deep_agent(
      model="ollama:devstral-2",
      backend=ContextHubBackend("my-agent"),
  )
  ```
</CodeGroup>

`ContextHubBackend` stores files in a LangSmith Hub repo. Construct it with a repo identifier in `owner/name` or `name` format.

<Note>
  Set `LANGSMITH_API_KEY` before using `ContextHubBackend`.
</Note>

**How it works:**

* Pulls the Hub repo tree lazily on first use, then serves reads from an in-memory cache.
* Persists writes and edits as Hub commits and updates the cache after successful commits.
* Uses optimistic parent-commit writes (`parent_commit`): each push targets the latest known commit hash.

**Behavior and limits:**

* If the repo does not exist, first pull is treated as empty; the first successful write can create the repo.
* If another writer advances the repo first, your stale parent-commit write can fail. Re-pull and retry on conflict.
* `upload_files()` accepts UTF-8 text. Non-UTF-8 files are rejected per path with `invalid_path`.

**Best for:**

* LangSmith-native durable filesystem persistence without separately wiring a LangGraph `BaseStore`.
* Workflows that benefit from Hub commit history on filesystem changes.

### CompositeBackend (router)

<CodeGroup>
  ```python Google theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="google_genai:gemini-3.5-flash",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
          },
      ),
      store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
  )
  ```

  ```python OpenAI theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="openai:gpt-5.5",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
          },
      ),
      store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
  )
  ```

  ```python Anthropic theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="anthropic:claude-sonnet-4-6",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
          },
      ),
      store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
  )
  ```

  ```python OpenRouter theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="openrouter:anthropic/claude-sonnet-4-6",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
          },
      ),
      store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
  )
  ```

  ```python Fireworks theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="fireworks:accounts/fireworks/models/qwen3p5-397b-a17b",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
          },
      ),
      store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
  )
  ```

  ```python Baseten theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="baseten:zai-org/GLM-5",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
          },
      ),
      store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
  )
  ```

  ```python Ollama theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from deepagents import create_deep_agent
  from deepagents.backends import CompositeBackend, StateBackend, StoreBackend
  from langgraph.store.memory import InMemoryStore

  agent = create_deep_agent(
      model="ollama:devstral-2",
      backend=CompositeBackend(
          default=StateBackend(),
          routes={
              "/memories/": StoreBackend(namespace=lambda _rt: ("memories",)),
          },
      ),
      store=InMemoryStore(),  # Store passed to create_deep_agent, not backend
  )
  ```
</CodeGroup>

**How it works:**

* [`CompositeBackend`](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend) routes file operations to different backends based on path prefix.
* Preserves the original path prefixes in listings and search results.

**Best for:**

* When you want to give your agent both thread-scoped and cross-thread storage, a `CompositeBackend` allows you provide both a `StateBackend` and `StoreBackend`
* When you have multiple sources of information that you want to provide to your agent as part of a single filesystem.
  * e.g. You have long-term memories stored under `/memories/` in one Store and you also have a custom backend that has documentation accessible at /docs/.

## Specify a backend

* Pass a backend instance to `create_deep_agent(model=..., backend=...)`. The filesystem middleware uses it for all tooling.
* The backend must implement `BackendProtocol` (for example, `StateBackend()`, `FilesystemBackend(root_dir=".")`, `StoreBackend()`, `ContextHubBackend("my-agent")`).
* If omitted, the default is `StateBackend()`.

## Route to different backends

Route parts of the namespace to different backends. Commonly used to persist `/memories/*` across threads and keep everything else thread-scoped.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent
from deepagents.backends import CompositeBackend, StateBackend, FilesystemBackend

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": FilesystemBackend(root_dir="/deepagents/myagent", virtual_mode=True),
        },
    )
)
```

Behavior:

* `/workspace/plan.md` → `StateBackend` (thread-scoped)
* `/memories/agent.md` → `FilesystemBackend` under `/deepagents/myagent`
* `ls`, `glob`, `grep` aggregate results and show original path prefixes.

Notes:

* Longer prefixes win (for example, route `"/memories/projects/"` can override `"/memories/"`).
* For StoreBackend routing, ensure a store is provided via `create_deep_agent(model=..., store=...)` or provisioned by the platform.
* Deep Agents write internal data (offloaded tool results, conversation history) to the default backend. Use `StateBackend` as the default to keep these artifacts ephemeral and avoid writing them to disk or a persistent store. See the [FilesystemBackend tip](#filesystembackend-local-disk) for a complete example.

## Use a virtual filesystem

Build a custom backend to project a remote or database filesystem (e.g., S3 or Postgres) into the tools namespace.

Design guidelines:

* Paths are absolute (`/x/y.txt`). Decide how to map them to your storage keys/rows.

* Implement `ls` and `glob` efficiently (server-side filtering where available, otherwise local filter).

* For external persistence (S3, Postgres, etc.), return `files_update=None` (Python) or omit `filesUpdate` (JS) in write/edit results — only in-memory state backends need to return a files update dict.

* Use `ls` and `glob` as the method names.

* Return structured result types with an `error` field for missing files or invalid patterns (do not raise).

S3-style outline:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents.backends.protocol import (
    BackendProtocol, WriteResult, EditResult, LsResult, ReadResult, GrepResult, GlobResult,
)

class S3Backend(BackendProtocol):
    def __init__(self, bucket: str, prefix: str = ""):
        self.bucket = bucket
        self.prefix = prefix.rstrip("/")

    def _key(self, path: str) -> str:
        return f"{self.prefix}{path}"

    def ls(self, path: str) -> LsResult:
        # List objects under _key(path); build FileInfo entries (path, size, modified_at)
        ...

    def read(self, file_path: str, offset: int = 0, limit: int = 2000) -> ReadResult:
        # Fetch object; return ReadResult(file_data=...) or ReadResult(error=...)
        ...

    def grep(self, pattern: str, path: str | None = None, glob: str | None = None) -> GrepResult:
        # Optionally filter server‑side; else list and scan content
        ...

    def glob(self, pattern: str, path: str | None = None) -> GlobResult:
        # Apply glob relative to path across keys
        ...

    def write(self, file_path: str, content: str) -> WriteResult:
        # Enforce create‑only semantics; return WriteResult(path=file_path, files_update=None)
        ...

    def edit(self, file_path: str, old_string: str, new_string: str, replace_all: bool = False) -> EditResult:
        # Read → replace (respect uniqueness vs replace_all) → write → return occurrences
        ...
```

Postgres-style outline:

* Table `files(path text primary key, content text, created_at timestamptz, modified_at timestamptz)`
* Map tool operations onto SQL:
  * `ls` uses `WHERE path LIKE $1 || '%'`
  * `glob` filter in SQL or fetch then apply glob in Python
  * `grep` can fetch candidate rows by extension or last modified time, then scan lines

## Permissions

Use [permissions](/oss/python/deepagents/permissions) to declaratively control which files and directories the agent can read or write. Permissions apply to the built-in filesystem tools and are evaluated before the backend is called.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents import create_deep_agent, FilesystemPermission

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    backend=CompositeBackend(
        default=StateBackend(),
        routes={
            "/memories/": StoreBackend(
                namespace=lambda rt: (rt.server_info.user.identity,),
            ),
            "/policies/": StoreBackend(
                namespace=lambda rt: (rt.context.org_id,),
            ),
        },
    ),
    permissions=[
        FilesystemPermission(
            operations=["write"],
            paths=["/policies/**"],
            mode="deny",
        ),
    ],
)
```

For the full set of options including rule ordering, subagent permissions, and composite backend interactions, see the [permissions guide](/oss/python/deepagents/permissions).

## Add policy hooks

For custom validation logic beyond path-based allow/deny rules (rate limiting, audit logging, content inspection), enforce enterprise rules by subclassing or wrapping a backend.

Block writes/edits under selected prefixes (subclass):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents.backends.filesystem import FilesystemBackend
from deepagents.backends.protocol import WriteResult, EditResult

class GuardedBackend(FilesystemBackend):
    def __init__(self, *, deny_prefixes: list[str], **kwargs):
        super().__init__(**kwargs)
        self.deny_prefixes = [p if p.endswith("/") else p + "/" for p in deny_prefixes]

    def write(self, file_path: str, content: str) -> WriteResult:
        if any(file_path.startswith(p) for p in self.deny_prefixes):
            return WriteResult(error=f"Writes are not allowed under {file_path}")
        return super().write(file_path, content)

    def edit(self, file_path: str, old_string: str, new_string: str, replace_all: bool = False) -> EditResult:
        if any(file_path.startswith(p) for p in self.deny_prefixes):
            return EditResult(error=f"Edits are not allowed under {file_path}")
        return super().edit(file_path, old_string, new_string, replace_all)
```

Generic wrapper (works with any backend):

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from deepagents.backends.protocol import (
    BackendProtocol, WriteResult, EditResult, LsResult, ReadResult, GrepResult, GlobResult,
)

class PolicyWrapper(BackendProtocol):
    def __init__(self, inner: BackendProtocol, deny_prefixes: list[str] | None = None):
        self.inner = inner
        self.deny_prefixes = [p if p.endswith("/") else p + "/" for p in (deny_prefixes or [])]

    def _deny(self, path: str) -> bool:
        return any(path.startswith(p) for p in self.deny_prefixes)

    def ls(self, path: str) -> LsResult:
        return self.inner.ls(path)

    def read(self, file_path: str, offset: int = 0, limit: int = 2000) -> ReadResult:
        return self.inner.read(file_path, offset=offset, limit=limit)
    def grep(self, pattern: str, path: str | None = None, glob: str | None = None) -> GrepResult:
        return self.inner.grep(pattern, path, glob)
    def glob(self, pattern: str, path: str | None = None) -> GlobResult:
        return self.inner.glob(pattern, path)
    def write(self, file_path: str, content: str) -> WriteResult:
        if self._deny(file_path):
            return WriteResult(error=f"Writes are not allowed under {file_path}")
        return self.inner.write(file_path, content)
    def edit(self, file_path: str, old_string: str, new_string: str, replace_all: bool = False) -> EditResult:
        if self._deny(file_path):
            return EditResult(error=f"Edits are not allowed under {file_path}")
        return self.inner.edit(file_path, old_string, new_string, replace_all)
```

## Migrate from backend factories

<Warning>
  The backend factory pattern is **deprecated** as of `deepagents` 0.5.0. Pass pre-constructed backend instances directly instead of factory functions.
</Warning>

Previously, backends like `StateBackend` and `StoreBackend` required a factory function that received a runtime object, because they needed runtime context (state, store) to operate. Backends now resolve this context internally via LangGraph's `get_config()`, `get_store()`, and `get_runtime()` helpers, so you can pass instances directly.

### What changed

| Before (deprecated)                                                  | After                                                   |
| -------------------------------------------------------------------- | ------------------------------------------------------- |
| `backend=lambda rt: StateBackend(rt)`                                | `backend=StateBackend()`                                |
| `backend=lambda rt: StoreBackend(rt)`                                | `backend=StoreBackend()`                                |
| `backend=lambda rt: CompositeBackend(default=StateBackend(rt), ...)` | `backend=CompositeBackend(default=StateBackend(), ...)` |
| `backend: (config) => new StateBackend(config)`                      | `backend: new StateBackend()`                           |
| `backend: (config) => new StoreBackend(config)`                      | `backend: new StoreBackend()`                           |

### Deprecated APIs

| Deprecated                                                | Replacement                                                  |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| Passing a callable to `backend=` in `create_deep_agent`   | Pass a backend instance directly                             |
| `runtime` constructor argument on `StateBackend(runtime)` | `StateBackend()` (no arguments needed)                       |
| `runtime` constructor argument on `StoreBackend(runtime)` | `StoreBackend()` or `StoreBackend(namespace=..., store=...)` |
| `files_update` field on `WriteResult` and `EditResult`    | State writes are now handled internally by the backend       |
| `Command` wrapping in middleware write/edit tools         | Tools return plain strings; no `Command(update=...)` needed  |

<Note>
  The factory pattern still works at runtime and emits a deprecation warning. Update your code to use direct instances before the next major version.
</Note>

### Migration example

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Before (deprecated)
from deepagents import create_deep_agent
from deepagents.backends import CompositeBackend, StateBackend, StoreBackend

agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    backend=lambda rt: CompositeBackend(
        default=StateBackend(rt),
        routes={"/memories/": StoreBackend(rt, namespace=lambda rt: (rt.server_info.user.identity,))},
    ),
)

# After
agent = create_deep_agent(
    model="google_genai:gemini-3.5-flash",
    backend=CompositeBackend(
        default=StateBackend(),
        routes={"/memories/": StoreBackend(namespace=lambda rt: (rt.server_info.user.identity,))},
    ),
)
```

### Migrating from `BackendContext`

In `deepagents>=0.5.2` (Python) and `deepagents>=1.9.1` (TypeScript), namespace factories receive a LangGraph [`Runtime`](https://reference.langchain.com/python/langgraph/runtime/Runtime) directly instead of a `BackendContext` wrapper. The old `BackendContext` form still works via backwards-compatible `.runtime` and `.state` accessors, but those accessors emit a deprecation warning and will be removed in `deepagents>=0.7`.

**What changed:**

* The factory argument is now a `Runtime`, not a `BackendContext`.
* Drop the `.runtime` accessor — for example, `ctx.runtime.context.user_id` becomes `rt.server_info.user.identity`.
* There is no direct replacement for `ctx.state`. Namespace info should be read-only and stable for the lifetime of a run, whereas state is mutable and changes step-to-step—deriving a namespace from it risks data ending up under inconsistent keys. If you have a use case that requires reading agent state, please [open an issue](https://github.com/langchain-ai/deepagents/issues).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Before (deprecated, removed in v0.7)
StoreBackend(
    namespace=lambda ctx: (ctx.runtime.context.user_id,),  # [!code --]
)

# After
StoreBackend(
    namespace=lambda rt: (rt.server_info.user.identity,),  # [!code ++]
)
```

## Protocol reference

Backends must implement [`BackendProtocol`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol).

Required methods:

* `ls(path: str) -> LsResult`
  * Return entries with at least `path`. Include `is_dir`, `size`, `modified_at` when available. Sort by `path` for deterministic output.
* `read(file_path: str, offset: int = 0, limit: int = 2000) -> ReadResult`
  * Return file data on success. On missing file, return `ReadResult(error="Error: File '/x' not found")`.
* `grep(pattern: str, path: Optional[str] = None, glob: Optional[str] = None) -> GrepResult`
  * Return structured matches. On error, return `GrepResult(error="...")` (do not raise).
* `glob(pattern: str, path: Optional[str] = None) -> GlobResult`
  * Return matched files as `FileInfo` entries (empty list if none).
* `write(file_path: str, content: str) -> WriteResult`
  * Create-only. On conflict, return `WriteResult(error=...)`. On success, set `path` and for state backends set `files_update={...}`; external backends should use `files_update=None`.
* `edit(file_path: str, old_string: str, new_string: str, replace_all: bool = False) -> EditResult`
  * Enforce uniqueness of `old_string` unless `replace_all=True`. If not found, return error. Include `occurrences` on success.

Supporting types:

* `LsResult(error, entries)` — `entries` is a `list[FileInfo]` on success, `None` on failure.
* `ReadResult(error, file_data)` — `file_data` is a `FileData` dict on success, `None` on failure.
* `GrepResult(error, matches)` — `matches` is a `list[GrepMatch]` on success, `None` on failure.
* `GlobResult(error, matches)` — `matches` is a `list[FileInfo]` on success, `None` on failure.
* `WriteResult(error, path, files_update)`
* `EditResult(error, path, files_update, occurrences)`
* `FileInfo` with fields: `path` (required), optionally `is_dir`, `size`, `modified_at`.
* `GrepMatch` with fields: `path`, `line`, `text`.
* `FileData` with fields: `content` (str), `encoding` (`"utf-8"` or `"base64"`), `created_at`, `modified_at`.
  :::

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/backends.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Changelog
Source: https://docs.langchain.com/oss/python/deepagents/changelog-py

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/changelog-py.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Configuration
Source: https://docs.langchain.com/oss/python/deepagents/code/configuration

Configure Deep Agents Code with config.toml, hooks, and MCP servers

Deep Agents Code stores its configuration in the `~/.deepagents/` directory. The main config files are:

| File          | Format | Purpose                                                                                           |
| ------------- | ------ | ------------------------------------------------------------------------------------------------- |
| `config.toml` | TOML   | Model defaults, provider settings, constructor params, profile overrides, themes, update settings |
| `.env`        | Dotenv | Global API keys, secrets, and other environment variables                                         |
| `hooks.json`  | JSON   | External tool subscriptions to Deep Agents Code lifecycle events                                  |
| `.mcp.json`   | JSON   | Global MCP server definitions                                                                     |

<Note>
  Files under `~/.deepagents/.state/` hold per-machine Deep Agents Code state and are managed automatically.
</Note>

***

## Inspect configuration

The `dcode config` command group reports what configuration is in effect and where each value comes from, without starting a session. This is useful for confirming that an environment variable or `config.toml` setting is being picked up, and for sharing a redacted snapshot in a bug report.

| Command                          | Description                                                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `dcode config show`              | Resolve every option against the live environment and `config.toml`, printing the effective value and which source provided it                   |
| `dcode config list` (alias `ls`) | List every available option with its type, default, and where it can be set, without resolving values                                            |
| `dcode config get <key>`         | Show the effective value and source for a single option, e.g. `dcode config get interpreter.memory_limit_mb`                                     |
| `dcode config path`              | Show the on-disk config file locations (`config.toml`, project and global `.env`, `hooks.json`, and managed state files) and whether each exists |

Each option resolves from the first source that is set, in this order: a `DEEPAGENTS_CODE_`-prefixed env var, the canonical env var, `config.toml`, then the built-in default.

All four commands accept `--json` for machine-readable output.

<Warning>
  Provider credentials and other secrets are reported as configured / not configured only—their values are never printed by `config show` or `config get`, so the output is safe to paste into a bug report.
</Warning>

***

## Provider credentials

Deep Agents Code needs an API key for each model provider you use. The recommended way to add one is the [`/auth`](#use-%2Fauth-recommended) credential manager. For non-interactive runs, manage the same stored keys from the shell with [`dcode auth`](#manage-credentials-from-the-shell-dcode-auth) or set [environment variables](#environment-variables-ci-and-headless) instead.

If the same key is set in more than one place, see [Key resolution order](#key-resolution-order) for which one wins.

### Use `/auth` (recommended)

Open the credential manager from any session:

```txt theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
/auth
```

The manager lists the LLM providers available in your installation and marks the ones that already have a key set. Select a provider to add or replace its key, or remove one you have already stored. Keys you save here persist across sessions.

<Accordion title="Provider row labels" icon="list-check">
  Each row shows the provider name followed by where its key comes from:

  | Label            | Meaning                                                                                                                             |
  | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
  | `[stored]`       | A key saved in this manager via `/auth`                                                                                             |
  | `[env: VARNAME]` | The key comes from environment variable `VARNAME` (the resolved name, such as `DEEPAGENTS_CODE_OPENAI_API_KEY` or `OPENAI_API_KEY`) |
  | `[missing]`      | No key is stored and the env var is unset; select the row to paste one                                                              |
</Accordion>

The `/auth` prompt also has an optional **base URL** field. Leave it blank to use the provider's default endpoint, or set a custom one to use with this key. The base URL is saved alongside the key. See [Endpoints, keys, and gateways](#endpoints-keys-and-gateways) for how endpoints resolve, including with gateways.

<Warning>
  A stored base URL is not a secret and may be logged; the key paired with it is never logged.
</Warning>

<Note>
  Keys are scoped to your user account on this machine — Deep Agents Code never transmits them anywhere except to the configured provider's API.
</Note>

#### Sign in with ChatGPT

Selecting the `openai_codex` provider in `/auth` starts a browser sign-in instead of prompting for an API key, letting you use OpenAI models with a ChatGPT subscription. To re-authenticate or sign out, select `openai_codex` again. See [Sign in with ChatGPT (Codex models)](/oss/python/deepagents/code/providers) for the full flow.

`/auth` only manages **LLM provider** credentials. Tool credentials such as `TAVILY_API_KEY` (web search) and `LANGSMITH_API_KEY` (tracing) are read from the environment instead — [set them in `~/.deepagents/.env` or your shell](#environment-variables).

### Manage credentials from the shell (`dcode auth`)

The `dcode auth` command group is the scriptable equivalent of the `/auth` manager: it manages the same stored credentials without launching the TUI, which makes it usable for dotfile bootstrap, CI/CD, and setting a key on a remote box over SSH. The subcommands mirror the modal's verbs:

| Command                                                 | Description                                                   |
| ------------------------------------------------------- | ------------------------------------------------------------- |
| `dcode auth list` (alias `ls`)                          | List every known provider and where its key resolves from     |
| `dcode auth status <provider>`                          | Print the resolution source for one provider                  |
| `dcode auth set <provider>`                             | Store an API key, read from stdin by default                  |
| `dcode auth remove <provider>` (aliases `rm`, `delete`) | Delete a stored credential                                    |
| `dcode auth path`                                       | Print the resolved path to the credential store (`auth.json`) |

`set` reads the key from **stdin** by default, so it never lands in shell history or `argv`. Pipe the key in, or use `--from-env VAR` to copy it from a process environment variable:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Pipe the key in (stdin)
echo "$ANTHROPIC_API_KEY" | dcode auth set anthropic

# Copy it from an existing environment variable
dcode auth set openai --from-env OPENAI_API_KEY
```

<Note>
  `set` refuses to run in an interactive terminal so an accidental invocation cannot hang waiting on input — pipe the key via stdin or use `--from-env VAR`. Stored keys go through the same store as `/auth`, so warnings (for example, about file permissions on `auth.json`) are printed to stderr.
</Note>

Remove a stored key or print the store location:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
dcode auth remove anthropic
dcode auth path
```

<Note>
  `dcode auth set` manages API keys only. The `openai_codex` provider uses a ChatGPT browser sign-in rather than an API key, so run [`/auth` and select `openai_codex`](#sign-in-with-chatgpt) to sign in instead. `dcode auth remove openai_codex` does sign you out.
</Note>

### Environment variables (CI and headless)

For non-interactive runs, CI/CD pipelines, or anywhere a TUI isn't available, export the provider's env var in your shell:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."

# Prefix with DEEPAGENTS_CODE_ to scope a key to Deep Agents Code only,

# leaving a shared key used by other CI steps untouched
export DEEPAGENTS_CODE_OPENAI_API_KEY="sk-..."
```

To keep keys in a file instead, define them in a [`.env` file](#environment-variables).

### Key resolution order

When a provider's key is set in more than one place, Deep Agents Code uses the first of these that is set:

1. **`DEEPAGENTS_CODE_`-prefixed env var** — for example `DEEPAGENTS_CODE_OPENAI_API_KEY` as an inline shell export. The [`DEEPAGENTS_CODE_` prefix](#deepagents_code_-prefix) is the explicit "use this key in Deep Agents Code" override.
2. **App-stored key** — entered in the `/auth` credential manager.
3. **Plain provider env var** — for example `OPENAI_API_KEY`, from your shell or `.env` files.

An app-stored key wins over a plain env-var key for the same provider, but a `DEEPAGENTS_CODE_`-prefixed key wins over an app-stored key. The prefix is the way to override an already-stored key for a single run, without clearing it:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# With a key already stored via /auth, a plain env var does not override it.

# dcode still uses the app-stored key for this run:
OPENAI_API_KEY=sk-xxxx dcode -n "..."

# The DEEPAGENTS_CODE_ prefix does override it, for this run only:
DEEPAGENTS_CODE_OPENAI_API_KEY=sk-xxxx dcode -n "..."
```

This layering exists for the common case where your machine already exports a plain provider variable for some other purpose — a shared `OPENAI_API_KEY` used by other tools, scripts, or CI — that you do not want Deep Agents Code to reuse. An app-stored key or a `DEEPAGENTS_CODE_`-prefixed variable gives Deep Agents Code its own value while leaving the unprefixed one untouched for everything else, so the two never mix.

Each provider's API key and its endpoint (`base_url`) resolve as a pair from the same source. See [Endpoints, keys, and gateways](#endpoints-keys-and-gateways).

### Enable web search with Tavily

The built-in `web_search` tool uses [Tavily](https://tavily.com). Deep Agents Code shows a "Web search disabled — `TAVILY_API_KEY` is not set" notification on startup until you provide a key. Unlike model provider keys, Tavily is **not** managed by `/auth`; it is read directly from the environment.

<Steps>
  <Step title="Get a key">
    Sign up at [tavily.com](https://tavily.com) and copy the key (it starts with `tvly-`). The free tier is sufficient for most Deep Agents Code usage.
  </Step>

  <Step title="Add it to your environment">
    Add the key to `~/.deepagents/.env` so every session picks it up:

    ```bash title="~/.deepagents/.env" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    TAVILY_API_KEY=tvly-...
    ```

    Shell exports take precedence over `.env` values (see [Loading order and precedence](#loading-order-and-precedence)). To scope a key to Deep Agents Code only without affecting other tools that read `TAVILY_API_KEY`, use the [`DEEPAGENTS_CODE_` prefix](#deepagents_code_-prefix): `DEEPAGENTS_CODE_TAVILY_API_KEY=tvly-...`.
  </Step>

  <Step title="Reload or restart">
    In an existing session, run `/reload` to re-read `.env` files. On the next launch, the "Web search disabled" notification goes away and the agent can call `web_search`.
  </Step>
</Steps>

***

## Environment variables

In addition to shell exports, Deep Agents Code reads environment variables from dotenv files, so you can keep API keys out of your shell profile and avoid duplicating `.env` files across projects.

```bash title="~/.deepagents/.env" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
```

### Loading order and precedence

At startup, Deep Agents Code reads the nearest project `.env`, found by searching the directory you launch from and walking up through its parents (the first `.env` found wins), then `~/.deepagents/.env` as a global fallback for all projects. A project `.env` wins over the global one, and neither overrides a value already set in your shell. Running `/reload` re-reads both `.env` files so you can change keys without restarting, with shell values still taking precedence. This applies to every variable Deep Agents Code reads (for example, `TAVILY_API_KEY` or the `DEEPAGENTS_CODE_*` settings). Provider API keys have additional resolution rules; see [Provider credentials](#provider-credentials).

### `DEEPAGENTS_CODE_` prefix

All Deep Agents Code-specific environment variables use a `DEEPAGENTS_CODE_` prefix (e.g., `DEEPAGENTS_CODE_AUTO_UPDATE`, `DEEPAGENTS_CODE_DEBUG`). See the [environment variable reference](#environment-variable-reference) for the full list.

The prefix also works as an override mechanism for any environment variable Deep Agents Code reads, including third-party credentials. Deep Agents Code checks `DEEPAGENTS_CODE_{NAME}` first, then falls back to `{NAME}`:

```bash title="~/.deepagents/.env" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Give Deep Agents Code its own value, without affecting other tools
DEEPAGENTS_CODE_OPENAI_API_KEY=sk-cli-only
