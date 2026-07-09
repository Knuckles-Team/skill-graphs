  namespace: (rt) => [rt.serverInfo.user.identity],  // [!code highlight]
});

// Per-assistant: all users of the same assistant share storage
const backend = new StoreBackend({
  namespace: (rt) => [rt.serverInfo.assistantId],  // [!code highlight]
});

// Per-thread: storage scoped to a single conversation
const backend = new StoreBackend({
  namespace: (rt) => [rt.executionInfo.threadId],  // [!code highlight]
});
```

You can combine multiple components to create more specific scopes — for example, `(user_id, thread_id)` for per-user per-conversation isolation, or append a suffix like `"filesystem"` to disambiguate when the same scope uses multiple store namespaces.

Namespace components must contain only alphanumeric characters, hyphens, underscores, dots, `@`, `+`, colons, and tildes. Wildcards (`*`, `?`) are rejected to prevent glob injection.

<Warning>
  The `namespace` parameter will be **required** in v1.9.0. Always set it explicitly for new code.
</Warning>

<Note>
  When no namespace factory is provided, the legacy default uses the `assistant_id` from LangGraph config metadata. This means all users of the same [assistant](/langsmith/assistants) share the same storage. For multi-user [going to production](/oss/javascript/deepagents/going-to-production), always provide a namespace factory.
</Note>

### ContextHubBackend

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

**How it works:**

* [`CompositeBackend`](https://reference.langchain.com/javascript/deepagents/backends/CompositeBackend) routes file operations to different backends based on path prefix.
* Preserves the original path prefixes in listings and search results.

**Best for:**

* When you want to give your agent both thread-scoped and cross-thread storage, a `CompositeBackend` allows you provide both a `StateBackend` and `StoreBackend`
* When you have multiple sources of information that you want to provide to your agent as part of a single filesystem.
  * e.g. You have long-term memories stored under `/memories/` in one Store and you also have a custom backend that has documentation accessible at /docs/.

## Specify a backend

* Pass a backend instance to `createDeepAgent({ backend: ... })`. The filesystem middleware uses it for all tooling.
* The backend must implement `AnyBackendProtocol` (`BackendProtocolV1` or `BackendProtocolV2`) — for example, `new StateBackend()`, `new FilesystemBackend({ rootDir: "." })`, `new StoreBackend()`.
* If omitted, the default is `new StateBackend()`.

<Note>
  Before version 1.9.0, only `BackendProtocol` was supported which is now `BackendProtocolV1`. V1 backends are automatically adapted to V2 at runtime via `adaptBackendProtocol()`. No code changes are required to keep using existing V1 backends. To update to v2, see [update existing backends to v2](#update-existing-backends-to-v2).
</Note>

## Route to different backends

Route parts of the namespace to different backends. Commonly used to persist `/memories/*` across threads and keep everything else thread-scoped.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { createDeepAgent, CompositeBackend, FilesystemBackend, StateBackend } from "deepagents";

const agent = createDeepAgent({
  backend: new CompositeBackend(
    new StateBackend(),
    {
      "/memories/": new FilesystemBackend({ rootDir: "/deepagents/myagent", virtualMode: true }),
    },
  ),
});
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

* All query methods (`ls`, `read`, `readRaw`, `grep`, `glob`) must return structured Result objects (e.g., `LsResult`, `ReadResult`) with an optional `error` field.

* Support binary files in `read()` by returning `Uint8Array` content with the appropriate `mimeType`.

S3-style outline:

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  type BackendProtocolV2,
  type LsResult,
  type ReadResult,
  type ReadRawResult,
  type GrepResult,
  type GlobResult,
  type WriteResult,
  type EditResult,
} from "deepagents";

class S3Backend implements BackendProtocolV2 {
  constructor(private bucket: string, private prefix: string = "") {
    this.prefix = prefix.replace(/\/$/, "");
  }

  private key(path: string): string {
    return `${this.prefix}${path}`;
  }

  async ls(path: string): Promise<LsResult> {
    // List objects under key(path); return { files: [...] }
    ...
  }

  async read(filePath: string, offset?: number, limit?: number): Promise<ReadResult> {
    // Fetch object; return { content, mimeType }
    // For binary files, return Uint8Array content
    ...
  }

  async readRaw(filePath: string): Promise<ReadRawResult> {
    // Return { data: FileData }
    ...
  }

  async grep(pattern: string, path?: string | null, glob?: string | null): Promise<GrepResult> {
    // Search text files; skip binary; return { matches: [...] }
    ...
  }

  async glob(pattern: string, path = "/"): Promise<GlobResult> {
    // Apply glob relative to path; return { files: [...] }
    ...
  }

  async write(filePath: string, content: string): Promise<WriteResult> {
    // Enforce create-only semantics; return { path: filePath, filesUpdate: null }
    ...
  }

  async edit(filePath: string, oldString: string, newString: string, replaceAll?: boolean): Promise<EditResult> {
    // Read → replace → write → return { path, occurrences }
    ...
  }
}
```

Postgres-style outline:

* Table `files(path text primary key, content text, mime_type text, created_at timestamptz, modified_at timestamptz)`
* Map tool operations onto SQL:
  * `ls` uses `WHERE path LIKE $1 || '%'` → return `LsResult`
  * `glob` filter in SQL or fetch then apply glob locally → return `GlobResult`
  * `grep` can fetch candidate rows by extension or last modified time, then scan lines (skip rows where `mime_type` is binary) → return `GrepResult`

## Permissions

Use [permissions](/oss/javascript/deepagents/permissions) to declaratively control which files and directories the agent can read or write. Permissions apply to the built-in filesystem tools and are evaluated before the backend is called.

For the full set of options including rule ordering, subagent permissions, and composite backend interactions, see the [permissions guide](/oss/javascript/deepagents/permissions).

## Add policy hooks

For custom validation logic beyond path-based allow/deny rules (rate limiting, audit logging, content inspection), enforce enterprise rules by subclassing or wrapping a backend.

Block writes/edits under selected prefixes (subclass):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import { FilesystemBackend, type WriteResult, type EditResult } from "deepagents";

class GuardedBackend extends FilesystemBackend {
  private denyPrefixes: string[];

  constructor({ denyPrefixes, ...options }: { denyPrefixes: string[]; rootDir?: string }) {
    super(options);
    this.denyPrefixes = denyPrefixes.map(p => p.endsWith("/") ? p : p + "/");
  }

  async write(filePath: string, content: string): Promise<WriteResult> {
    if (this.denyPrefixes.some(p => filePath.startsWith(p))) {
      return { error: `Writes are not allowed under ${filePath}` };
    }
    return super.write(filePath, content);
  }

  async edit(filePath: string, oldString: string, newString: string, replaceAll = false): Promise<EditResult> {
    if (this.denyPrefixes.some(p => filePath.startsWith(p))) {
      return { error: `Edits are not allowed under ${filePath}` };
    }
    return super.edit(filePath, oldString, newString, replaceAll);
  }
}
```

Generic wrapper (works with any backend):

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import {
  type BackendProtocolV2,
  type LsResult,
  type ReadResult,
  type ReadRawResult,
  type GrepResult,
  type GlobResult,
  type WriteResult,
  type EditResult,
} from "deepagents";

class PolicyWrapper implements BackendProtocolV2 {
  private denyPrefixes: string[];

  constructor(private inner: BackendProtocolV2, denyPrefixes: string[] = []) {
    this.denyPrefixes = denyPrefixes.map(p => p.endsWith("/") ? p : p + "/");
  }

  private isDenied(path: string): boolean {
    return this.denyPrefixes.some(p => path.startsWith(p));
  }

  ls(path: string): Promise<LsResult> { return this.inner.ls(path); }
  read(filePath: string, offset?: number, limit?: number): Promise<ReadResult> { return this.inner.read(filePath, offset, limit); }
  readRaw(filePath: string): Promise<ReadRawResult> { return this.inner.readRaw(filePath); }
  grep(pattern: string, path?: string | null, glob?: string | null): Promise<GrepResult> { return this.inner.grep(pattern, path, glob); }
  glob(pattern: string, path?: string): Promise<GlobResult> { return this.inner.glob(pattern, path); }

  async write(filePath: string, content: string): Promise<WriteResult> {
    if (this.isDenied(filePath)) return { error: `Writes are not allowed under ${filePath}` };
    return this.inner.write(filePath, content);
  }

  async edit(filePath: string, oldString: string, newString: string, replaceAll = false): Promise<EditResult> {
    if (this.isDenied(filePath)) return { error: `Edits are not allowed under ${filePath}` };
    return this.inner.edit(filePath, oldString, newString, replaceAll);
  }
}
```

## Multimodal and binary files

<Note>
  Multi-modal file support (PDFs, audio, video) requires `deepagents>=1.9.0`.
</Note>

V2 backends support binary files natively. When `read()` encounters a binary file (determined by MIME type from the file extension), it returns a `ReadResult` with `Uint8Array` content and the corresponding `mimeType`. Text files return `string` content.

### Supported MIME types

| Category  | Extensions                                                               | MIME types                                                                                                                      |
| --------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Images    | `.png`, `.jpg`/`.jpeg`, `.gif`, `.webp`, `.svg`, `.heic`, `.heif`        | `image/png`, `image/jpeg`, `image/gif`, `image/webp`, `image/svg+xml`, `image/heic`, `image/heif`                               |
| Audio     | `.mp3`, `.wav`, `.aiff`, `.aac`, `.ogg`, `.flac`                         | `audio/mpeg`, `audio/wav`, `audio/aiff`, `audio/aac`, `audio/ogg`, `audio/flac`                                                 |
| Video     | `.mp4`, `.webm`, `.mpeg`/`.mpg`, `.mov`, `.avi`, `.flv`, `.wmv`, `.3gpp` | `video/mp4`, `video/webm`, `video/mpeg`, `video/quicktime`, `video/x-msvideo`, `video/x-flv`, `video/x-ms-wmv`, `video/3gpp`    |
| Documents | `.pdf`, `.ppt`, `.pptx`                                                  | `application/pdf`, `application/vnd.ms-powerpoint`, `application/vnd.openxmlformats-officedocument.presentationml.presentation` |
| Text      | `.txt`, `.html`, `.json`, `.js`, `.ts`, `.py`, etc.                      | `text/plain`, `text/html`, `application/json`, etc.                                                                             |

### Read binary files

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
const result = await backend.read("/workspace/screenshot.png");

if (result.error) {
  console.error(result.error);
} else if (result.content instanceof Uint8Array) {
  // Binary file — content is Uint8Array, mimeType is set
  console.log(`Binary file: ${result.mimeType}`); // "image/png"
} else {
  // Text file — content is string
  console.log(`Text file: ${result.mimeType}`); // "text/plain"
}
```

### FileData format

`FileData` is the type used to store file content in state and store backends.

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
type FileData =
  // Current format (v2)
  | {
      content: string | Uint8Array; // string for text, Uint8Array for binary
      mimeType: string;             // e.g. "text/plain", "image/png"
      created_at: string;           // ISO 8601 timestamp
      modified_at: string;          // ISO 8601 timestamp
    }
  // Legacy format (v1)
  | {
      content: string[];            // array of lines
      created_at: string;           // ISO 8601 timestamp
      modified_at: string;          // ISO 8601 timestamp
    };
```

Backends may encounter either format when reading from state or store. The framework handles both transparently. New writes default to the v2 format. During rolling deployments where older readers need the legacy format, pass `fileFormat: "v1"` to the backend constructor (e.g., `new StoreBackend({ fileFormat: "v1" })`).

## Migrate from backend factories

<Warning>
  The backend factory pattern is **deprecated** as of `deepagents` 1.9.0. Pass pre-constructed backend instances directly instead of factory functions.
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

| Deprecated                                                   | Replacement                                            |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| `BackendFactory` type                                        | Pass a backend instance directly                       |
| `BackendRuntime` interface                                   | Backends resolve context internally                    |
| `StateBackend(runtime, options?)` constructor overload       | `new StateBackend(options?)`                           |
| `StoreBackend(stateAndStore, options?)` constructor overload | `new StoreBackend(options?)`                           |
| `filesUpdate` field on `WriteResult` and `EditResult`        | State writes are now handled internally by the backend |

<Note>
  The factory pattern still works at runtime and emits a deprecation warning. Update your code to use direct instances before the next major version.
</Note>

### Migration example

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// Before (deprecated)
import { createDeepAgent, CompositeBackend, StateBackend, StoreBackend } from "deepagents";

const agent = createDeepAgent({
  backend: (config) => new CompositeBackend(
    new StateBackend(config),
    { "/memories/": new StoreBackend(config, {
      namespace: (rt) => [rt.serverInfo.user.identity],
    }) },
  ),
});

// After
const agent = createDeepAgent({
  backend: new CompositeBackend(
    new StateBackend(),
    { "/memories/": new StoreBackend({
      namespace: (rt) => [rt.serverInfo.user.identity],
    }) },
  ),
});
```

### Migrating from `BackendContext`

In `deepagents>=0.5.2` (Python) and `deepagents>=1.9.1` (TypeScript), namespace factories receive a LangGraph [`Runtime`](https://reference.langchain.com/javascript/langchain/index/Runtime) directly instead of a `BackendContext` wrapper. The old `BackendContext` form still works via backwards-compatible `.runtime` and `.state` accessors, but those accessors emit a deprecation warning and will be removed in `deepagents>=0.7`.

**What changed:**

* The factory argument is now a `Runtime`, not a `BackendContext`.
* Drop the `.runtime` accessor — for example, `ctx.runtime.context.user_id` becomes `rt.server_info.user.identity`.
* There is no direct replacement for `ctx.state`. Namespace info should be read-only and stable for the lifetime of a run, whereas state is mutable and changes step-to-step—deriving a namespace from it risks data ending up under inconsistent keys. If you have a use case that requires reading agent state, please [open an issue](https://github.com/langchain-ai/deepagents/issues).

```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
// Before (deprecated, removed in v0.7)
new StoreBackend({
  namespace: (ctx) => [ctx.runtime.context.userId],  // [!code --]
});

// After
new StoreBackend({
  namespace: (rt) => [rt.serverInfo.user.identity],  // [!code ++]
});
```

## Protocol reference

Backends must implement [`BackendProtocol`](https://reference.langchain.com/javascript/deepagents/backends/BackendProtocol).

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
