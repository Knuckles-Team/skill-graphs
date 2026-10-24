  :::

Backends implement `BackendProtocolV2`. All query methods return structured Result objects with `{ error?: string, ...data }`.

### Required methods

* **`ls(path: string) → LsResult`**
  * List files and directories in the specified directory (non-recursive). Directories have a trailing `/` in their path and `is_dir=true`. Include `is_dir`, `size`, `modified_at` when available.

* **`read(filePath: string, offset?: number, limit?: number) → ReadResult`**
  * Read file content. For text files, content is paginated by line offset/limit (default offset 0, limit 500). For binary files, the full raw `Uint8Array` content is returned with the `mimeType` field set. On missing file, return `{ error: "File '/x' not found" }`.

* **`readRaw(filePath: string) → ReadRawResult`**
  * Read file content as raw `FileData`. Returns the full file data including timestamps.

* **`grep(pattern: string, path?: string | null, glob?: string | null) → GrepResult`**
  * Search file contents for a literal text pattern. Binary files (determined by MIME type) are skipped. On failure, return `{ error: "..." }`.

* **`glob(pattern: string, path?: string) → GlobResult`**
  * Return files matching a glob pattern as `FileInfo` entries.

* **`write(filePath: string, content: string) → WriteResult`**
  * Create-only semantics. On conflict, return `{ error: "..." }`. On success, set `path` and for state backends set `filesUpdate={...}`; external backends should use `filesUpdate=null`.

* **`edit(filePath: string, oldString: string, newString: string, replaceAll?: boolean) → EditResult`**
  * Enforce uniqueness of `oldString` unless `replaceAll=true`. If not found, return error. Include `occurrences` on success.

### Optional methods

* **`uploadFiles(files: Array<[string, Uint8Array]>) → FileUploadResponse[]`** — Upload multiple files (for sandbox backends).
* **`downloadFiles(paths: string[]) → FileDownloadResponse[]`** — Download multiple files (for sandbox backends).

### Result types

| Type            | Success fields                                        | Error field |
| --------------- | ----------------------------------------------------- | ----------- |
| `ReadResult`    | `content?: string \| Uint8Array`, `mimeType?: string` | `error`     |
| `ReadRawResult` | `data?: FileData`                                     | `error`     |
| `LsResult`      | `files?: FileInfo[]`                                  | `error`     |
| `GlobResult`    | `files?: FileInfo[]`                                  | `error`     |
| `GrepResult`    | `matches?: GrepMatch[]`                               | `error`     |
| `WriteResult`   | `path?: string`                                       | `error`     |
| `EditResult`    | `path?: string`, `occurrences?: number`               | `error`     |

### Supporting types

* **`FileInfo`** — `path` (required), optionally `is_dir`, `size`, `modified_at`.
* **`GrepMatch`** — `path`, `line` (1-indexed), `text`.
* **`FileData`** — File content with timestamps. See [FileData format](#filedata-format).

### Sandbox extension

`SandboxBackendProtocolV2` extends `BackendProtocolV2` with:

* **`execute(command: string) → ExecuteResponse`** — Run a shell command in the sandbox.
* **`readonly id: string`** — Unique identifier for the sandbox instance.

## Update existing backends to V2

<Accordion title="Migration guide">
  ### Method renames

  | V1 method                       | V2 method                       | Return type change                     |
  | ------------------------------- | ------------------------------- | -------------------------------------- |
  | `lsInfo(path)`                  | `ls(path)`                      | `FileInfo[]` → `LsResult`              |
  | `read(filePath, offset, limit)` | `read(filePath, offset, limit)` | `string` → `ReadResult`                |
  | `readRaw(filePath)`             | `readRaw(filePath)`             | `FileData` → `ReadRawResult`           |
  | `grepRaw(pattern, path, glob)`  | `grep(pattern, path, glob)`     | `GrepMatch[] \| string` → `GrepResult` |
  | `globInfo(pattern, path)`       | `glob(pattern, path)`           | `FileInfo[]` → `GlobResult`            |
  | `write(...)`                    | `write(...)`                    | Unchanged (`WriteResult`)              |
  | `edit(...)`                     | `edit(...)`                     | Unchanged (`EditResult`)               |

  ### Type renames

  | V1 type                  | V2 type                    |
  | ------------------------ | -------------------------- |
  | `BackendProtocol`        | `BackendProtocolV2`        |
  | `SandboxBackendProtocol` | `SandboxBackendProtocolV2` |

  ### Adaptation utilities

  If you have existing V1 backends that you need to use with V2-only code, use the adaptation functions:

  ```typescript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { adaptBackendProtocol, adaptSandboxProtocol } from "deepagents";

  // Adapt a V1 backend to V2
  const v2Backend = adaptBackendProtocol(v1Backend);

  // Adapt a V1 sandbox to V2
  const v2Sandbox = adaptSandboxProtocol(v1Sandbox);
  ```

  <Note>
    The framework auto-adapts V1 backends passed to `createDeepAgent()`. Manual adaptation is only needed when calling protocol methods directly.
  </Note>
</Accordion>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/backends.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
