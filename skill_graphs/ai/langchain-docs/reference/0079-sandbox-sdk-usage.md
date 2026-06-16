# Sandbox SDK usage
Source: https://docs.langchain.com/langsmith/sandbox-sdk

Create and manage sandboxes programmatically with the Python or TypeScript SDK.

The [LangSmith SDK](/langsmith/reference) provides a programmatic interface to create and interact with sandboxes.

## Install

<CodeGroup>
  ```bash Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # uv
  uv add "langsmith[sandbox]"

  # pip
  pip install "langsmith[sandbox]"
  ```

  ```bash TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  npm install langsmith
  # or
  yarn add langsmith
  ```
</CodeGroup>

The `[sandbox]` extra for Python installs `websockets`, which enables real-time streaming and `timeout=0`. Without it, `run()` falls back to HTTP automatically. For TypeScript, install the optional `ws` package for WebSocket streaming:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
npm install ws
```

## Create and run a sandbox

Pass a snapshot ID or name when you want to boot from a reusable custom filesystem image; see [Snapshots](/langsmith/sandbox-snapshots) for that flow.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.sandbox import SandboxClient

  # Client uses LANGSMITH_ENDPOINT and LANGSMITH_API_KEY from environment
  client = SandboxClient()

  # Create a sandbox with the default runtime and run code
  with client.sandbox() as sb:
      result = sb.run("python -c 'print(2 + 2)'")
      print(result.stdout)  # "4\n"
      print(result.success)  # True
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { SandboxClient } from "langsmith/sandbox";

  // Client uses LANGSMITH_ENDPOINT and LANGSMITH_API_KEY from environment
  const client = new SandboxClient();

  // Create a sandbox with the default runtime and run code
  const sandbox = await client.createSandbox();
  const result = await sandbox.run("node -e 'console.log(2 + 2)'");
  console.log(result.stdout); // "4\n"

  // Don't forget to clean up
  await sandbox.delete();
  ```
</CodeGroup>

## Run commands

Every `run()` call returns an `ExecutionResult` with `stdout`, `stderr`, `exit_code`, and `success`.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  with client.sandbox() as sb:
      result = sb.run("echo 'Hello, World!'")

      print(result.stdout)     # "Hello, World!\n"
      print(result.stderr)     # ""
      print(result.exit_code)  # 0
      print(result.success)    # True

      # Commands that fail return non-zero exit codes
      result = sb.run("exit 1")
      print(result.success)    # False
      print(result.exit_code)  # 1
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const sandbox = await client.createSandbox();
  try {
    const result = await sandbox.run("echo 'Hello, World!'");

    console.log(result.stdout);     // "Hello, World!\n"
    console.log(result.stderr);     // ""
    console.log(result.exit_code);  // 0

    // Pass environment variables and working directory
    const envResult = await sandbox.run("echo $MY_VAR", {
      env: { MY_VAR: "test-value" },
      cwd: "/tmp",
    });
  } finally {
    await sandbox.delete();
  }
  ```
</CodeGroup>

## Stream output

For long-running commands, stream output in real time using callbacks or a `CommandHandle`.

### Stream with callbacks

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import sys

  with client.sandbox() as sb:
      result = sb.run(
          "make build",
          timeout=600,
          on_stdout=lambda s: print(s, end=""),
          on_stderr=lambda s: print(s, end="", file=sys.stderr),
      )
      print(f"\nBuild {'succeeded' if result.success else 'failed'}")
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const result = await sandbox.run("make build", {
    timeout: 600,
    onStdout: (data) => process.stdout.write(data),
    onStderr: (data) => process.stderr.write(data),
  });
  console.log(`Exit code: ${result.exit_code}`);
  ```
</CodeGroup>

### Stream with CommandHandle

Set `wait=False` to get a `CommandHandle` for full control over the output stream.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  with client.sandbox() as sb:
      handle = sb.run("make build", timeout=600, wait=False)

      print(f"Command ID: {handle.command_id}")

      for chunk in handle:
          prefix = "OUT" if chunk.stream == "stdout" else "ERR"
          print(f"[{prefix}] {chunk.data}", end="")

      result = handle.result
      print(f"\nExit code: {result.exit_code}")
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const handle = await sandbox.run("python train.py", {
    wait: false,
    timeout: 600,
  });

  console.log(`Command ID: ${handle.commandId}`);
  console.log(`PID: ${handle.pid}`);

  for await (const chunk of handle) {
    if (chunk.stream === "stdout") {
      process.stdout.write(chunk.data);
    } else {
      process.stderr.write(chunk.data);
    }
  }

  const result = await handle.result;
  console.log(`Exit code: ${result.exit_code}`);
  ```
</CodeGroup>

### Send stdin and kill commands

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  with client.sandbox() as sb:
      handle = sb.run(
          "python -c 'name = input(\"Name: \"); print(f\"Hello {name}\")'",
          timeout=30,
          wait=False,
      )

      for chunk in handle:
          if "Name:" in chunk.data:
              handle.send_input("World\n")
          print(chunk.data, end="")

      result = handle.result
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const handle = await sandbox.run("python -i", { wait: false });

  // Send input to stdin
  handle.sendInput("print(2 + 2)\n");
  handle.sendInput("exit()\n");

  for await (const chunk of handle) {
    process.stdout.write(chunk.data);
  }
  ```
</CodeGroup>

Kill a running command:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  with client.sandbox() as sb:
      handle = sb.run("python server.py", timeout=0, wait=False)

      for chunk in handle:
          print(chunk.data, end="")
          if "Ready" in chunk.data:
              break

      handle.kill()
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const handle = await sandbox.run("sleep 300", { wait: false });
  handle.kill();

  const result = await handle.result;
  console.log(result.exit_code); // non-zero
  ```
</CodeGroup>

### Reconnect to a running command

If a client disconnects, reconnect using the command ID:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  with client.sandbox() as sb:
      handle = sb.run("make build", timeout=600, wait=False)
      command_id = handle.command_id

      # Later, possibly in a different process
      handle = sb.reconnect(command_id)
      for chunk in handle:
          print(chunk.data, end="")
      result = handle.result
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const handle = await sandbox.run("long-task", { wait: false });
  const commandId = handle.commandId;

  // Later, or from a different client
  const newHandle = await sandbox.reconnect(commandId);
  for await (const chunk of newHandle) {
    process.stdout.write(chunk.data);
  }
  ```
</CodeGroup>

## File operations

Read and write files in the sandbox:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  with client.sandbox() as sb:
      # Write a file
      sb.write("/app/script.py", "print('Hello from file!')")

      # Run the script
      result = sb.run("python /app/script.py")
      print(result.stdout)  # "Hello from file!\n"

      # Read a file (returns bytes)
      content = sb.read("/app/script.py")
      print(content.decode())  # "print('Hello from file!')"

      # Write binary files
      sb.write("/app/data.bin", b"\x00\x01\x02\x03")
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const sandbox = await client.createSandbox();
  try {
    // Write a file (string content)
    await sandbox.write("/app/script.py", "print('Hello from file!')");

    // Run the script
    const result = await sandbox.run("python /app/script.py");
    console.log(result.stdout);  // "Hello from file!\n"

    // Read a file (returns Uint8Array)
    const content = await sandbox.read("/app/script.py");
    console.log(new TextDecoder().decode(content));

    // Write binary files
    await sandbox.write("/app/data.bin", new Uint8Array([0x00, 0x01, 0x02, 0x03]));
  } finally {
    await sandbox.delete();
  }
  ```
</CodeGroup>

## Sandbox lifetime and retention

Sandboxes are governed by a two-stage retention model anchored to **idle
activity** and the **`stopped`** state.

| Field                       | What it controls                                                                                                                                                                                                                    | When it fires                                                           |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `idle_ttl_seconds`          | The launcher stops the sandbox after this many seconds of inactivity. Any command execution or file I/O resets the timer. `0` disables the idle stop.                                                                               | Default `600` (10 minutes) when omitted.                                |
| `delete_after_stop_seconds` | Once the sandbox enters the `stopped` state, this timer starts. After it elapses, the sandbox row + filesystem clone are permanently deleted by a server-side sweep. `0` disables stop-anchored deletion (manual cleanup required). | Server applies its configured default (typically 14 days) when omitted. |

Both values must be multiples of 60 (minute resolution). The full lifecycle is:

```
running ──(idle for idle_ttl_seconds)──▶ stopped ──(delete_after_stop_seconds)──▶ deleted
```

You can also call `stop_sandbox` / `stopSandbox` explicitly — that also
populates `stopped_at` and starts the deletion timer.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # Default retention (server defaults: 10-min idle stop, 14-day delete)
  with client.sandbox() as sb:
      sb.run("echo hello")

  # Aggressive: stop after 5 min idle, delete 1 hour after stop
  sb = client.create_sandbox(
      idle_ttl_seconds=300,
      delete_after_stop_seconds=3600,
  )

  # Long-running: never auto-stop, delete 7 days after manual stop
  sb = client.create_sandbox(
      idle_ttl_seconds=0,
      delete_after_stop_seconds=604800,
  )

  # Update retention on an existing sandbox
  sb = client.update_sandbox(
      sb.name,
      idle_ttl_seconds=1800,
      delete_after_stop_seconds=2592000,  # 30 days
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  // Default retention (server defaults applied)
  const sandbox = await client.createSandbox();

  // Aggressive: stop after 5 min idle, delete 1 hour after stop
  const sb = await client.createSandbox({
    idleTtlSeconds: 300,
    deleteAfterStopSeconds: 3600,
  });

  // Long-running: never auto-stop, delete 7 days after manual stop
  const longRunning = await client.createSandbox({
    idleTtlSeconds: 0,
    deleteAfterStopSeconds: 604800,
  });

  // Update retention on an existing sandbox
  await client.updateSandbox(sb.name, {
    idleTtlSeconds: 1800,
    deleteAfterStopSeconds: 2592000, // 30 days
  });
  ```
</CodeGroup>

## Command lifecycle and TTL

The sandbox daemon manages command session lifecycles with two timeout mechanisms:

* **Session TTL (finished commands)**: After a command finishes, its session remains in memory for a TTL period. During this window you can reconnect to retrieve output. After the TTL expires, the session is cleaned up.
* **Idle timeout (running commands)**: Running commands with no connected clients are killed after an idle timeout (default: 5 minutes). The idle timer resets each time a client connects. Set to `-1` for no idle timeout.

### Combine lifecycle options

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  with client.sandbox() as sb:
      # Long-running task: 30-min idle timeout, 1-hour session TTL
      handle = sb.run(
          "python train.py",
          timeout=0,              # No command timeout
          idle_timeout=1800,      # Kill after 30min with no clients
          ttl_seconds=3600,       # Keep session for 1 hour after exit
          wait=False,
      )

      # Fire-and-forget: no idle timeout, infinite TTL
      handle = sb.run(
          "python background_job.py",
          timeout=0,
          idle_timeout=-1,        # Never kill due to idle
          ttl_seconds=-1,         # Keep session forever
          wait=False,
      )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const sandbox = await client.createSandbox();
  try {
    // Long-running task: 30-min idle timeout, 1-hour session TTL
    const handle = await sandbox.run("python train.py", {
      timeout: 0,              // No command timeout
      idleTimeout: 1800,       // Kill after 30min with no clients
      ttlSeconds: 3600,        // Keep session for 1 hour after exit
      wait: false,
    });

    // Fire-and-forget: no idle timeout, infinite TTL
    const bg = await sandbox.run("python background_job.py", {
      timeout: 0,
      idleTimeout: -1,         // Never kill due to idle
      ttlSeconds: -1,          // Keep session forever
      wait: false,
    });
  } finally {
    await sandbox.delete();
  }
  ```
</CodeGroup>

Set `kill_on_disconnect=True` (Python) or `killOnDisconnect: true` (TypeScript) to kill the command immediately when the last client disconnects, instead of waiting for the idle timeout.

## Service URLs (Python)

Access an HTTP service running inside a sandbox via an authenticated URL. You can open it in a browser, call it from code, or share it with a teammate.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
with client.sandbox() as sb:
    sb.run("python -m http.server 8000", timeout=0, wait=False)

    svc = sb.service(port=8000)

    # Open in a browser
    print(svc.browser_url)

    # Or make requests with built-in helpers (auth is injected automatically)
    resp = svc.get("/api/data")
    resp = svc.post("/api/data", json={"key": "value"})
```

For more details, including use cases, REST API access, and a full FastAPI example, see [Service URLs](/langsmith/sandbox-service-urls).

## TCP tunnels (Python)

Access any TCP service running inside a sandbox as if it were local. The tunnel opens a local TCP port and forwards connections through a WebSocket to the target port inside the sandbox.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import psycopg2

# Snapshot built from the official postgres:16 image
sb = client.create_sandbox(snapshot_id=postgres_snapshot_id)
pg_handle = sb.run(
    "POSTGRES_HOST_AUTH_METHOD=trust docker-entrypoint.sh postgres",
    timeout=0,
    wait=False,
)
import time; time.sleep(6)  # Wait for Postgres to start

try:
    with sb.tunnel(remote_port=5432, local_port=25432) as t:
        conn = psycopg2.connect(
            host="127.0.0.1",
            port=t.local_port,
            user="postgres",
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version()")
        print(cursor.fetchone())
        conn.close()
finally:
    pg_handle.kill()
    client.delete_sandbox(sb.name)
```

Tunnels work with any TCP service (Redis, HTTP servers, etc.) and you can open multiple tunnels simultaneously:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
with sb.tunnel(remote_port=5432, local_port=25432) as t1, \
     sb.tunnel(remote_port=6379, local_port=26379) as t2:
    # Use both Postgres and Redis simultaneously
    pass
```

## Async support (Python)

The Python SDK provides a full async client:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith.sandbox import AsyncSandboxClient

async def main():
    async with AsyncSandboxClient() as client:
        async with await client.sandbox() as sb:
            result = await sb.run("python -c 'print(1 + 1)'")
            print(result.stdout)  # "2\n"

            await sb.write("/app/test.txt", "async content")
            content = await sb.read("/app/test.txt")
            print(content.decode())

            # Async streaming
            handle = await sb.run("make build", timeout=600, wait=False)
            async for chunk in handle:
                print(chunk.data, end="")
            result = await handle.result

            # Async service URLs
            svc = await sb.service(port=8000)
            resp = await svc.get("/api/data")
            url = await svc.get_service_url()
            token = await svc.get_token()
```

## Trace sandbox activity

Pass LangSmith tracing environment variables through the `env` parameter on `run()` to send traces from code running inside a sandbox. Call `flush()` before the process exits to ensure all traces are delivered.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.sandbox import SandboxClient

  client = SandboxClient()

  tracing_env = {
      "LANGSMITH_API_KEY": "lsv2_pt_...",
      "LANGSMITH_ENDPOINT": "https://api.smith.langchain.com",
      "LANGSMITH_TRACING": "true",
      "LANGSMITH_PROJECT": "my-sandbox-traces",
  }

  with client.sandbox() as sandbox:
      sandbox.run("pip install langsmith", timeout=120, env=tracing_env)
      result = sandbox.run("python3 my_agent.py", env=tracing_env)
      print(result.stdout)
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { SandboxClient } from "langsmith/sandbox";

  const client = new SandboxClient();

  const tracingEnv = {
    LANGSMITH_API_KEY: "lsv2_pt_...",
    LANGSMITH_ENDPOINT: "https://api.smith.langchain.com",
    LANGSMITH_TRACING: "true",
    LANGSMITH_PROJECT: "my-sandbox-traces",
  };

  const sandbox = await client.createSandbox();
  try {
    await sandbox.run("pip install langsmith", { timeout: 120, env: tracingEnv });
    const result = await sandbox.run("python3 my_agent.py", { env: tracingEnv });
    console.log(result.stdout);
  } finally {
    await sandbox.delete();
  }
  ```
</CodeGroup>

Inside the sandbox, any LangSmith-instrumented code (`@traceable`, LangChain, LangGraph) automatically picks up the tracing configuration from the injected environment variables.

<Warning>
  Always call `flush()` before the sandbox process exits — `langsmith.Client().flush()` in Python or `await new Client().flush()` in TypeScript. Without it, traces may be lost because the container is destroyed when the command finishes.
</Warning>

## Error handling

Both SDKs provide typed exceptions for specific error handling:

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.sandbox import (
      SandboxClientError,       # Base exception
      ResourceCreationError,    # Provisioning failed
      ResourceNotFoundError,    # Resource doesn't exist
      ResourceTimeoutError,     # Operation timed out
      SandboxNotReadyError,     # Sandbox not ready yet
      SandboxConnectionError,   # Network/WebSocket error
      CommandTimeoutError,      # Command exceeded timeout
      QuotaExceededError,       # Quota limit reached
  )

  try:
      with client.sandbox() as sb:
          result = sb.run("sleep 999", timeout=10)
  except CommandTimeoutError as e:
      print(f"Command timed out: {e}")
  except ResourceNotFoundError as e:
      print(f"{e.resource_type} not found: {e}")
  except SandboxClientError as e:
      print(f"Error: {e}")
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import {
    LangSmithSandboxError,
    LangSmithResourceNotFoundError,
    LangSmithResourceTimeoutError,
    LangSmithSandboxConnectionError,
    LangSmithCommandTimeoutError,
    LangSmithQuotaExceededError,
  } from "langsmith/sandbox";

  try {
    const sandbox = await client.createSandbox("not-a-real-snapshot");
    await sandbox.delete();
  } catch (e) {
    if (e instanceof LangSmithResourceNotFoundError) {
      console.log(`${e.resourceType} not found: ${e.message}`);
    } else if (e instanceof LangSmithResourceTimeoutError) {
      console.log(`Timeout waiting for ${e.resourceType}: ${e.message}`);
    } else if (e instanceof LangSmithSandboxError) {
      console.log(`Error: ${e.message}`);
    }
  }
  ```
</CodeGroup>

<Note>
  For more details, see the sandbox SDK reference on GitHub for [Python](https://github.com/langchain-ai/langsmith-sdk/tree/main/python/langsmith/sandbox) or [TypeScript](https://github.com/langchain-ai/langsmith-sdk/tree/main/js/src/sandbox).
</Note>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandbox-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Sandbox service URLs
Source: https://docs.langchain.com/langsmith/sandbox-service-urls

Access HTTP services running inside sandboxes via authenticated URLs, from a browser or programmatically.

Service URLs let you access an HTTP service running inside a sandbox (a REST API, a Streamlit app, a Jupyter notebook, API documentation) without tunnels, port forwarding, or CLI tools. Each sandbox + port combination gets its own URL that you can open in a browser, call from code, or share with a teammate.

<img alt="Service URLs view" />

## Quick start

Start an HTTP server inside a sandbox, then get a URL to access it:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith.sandbox import SandboxClient

client = SandboxClient()

with client.sandbox() as sb:
    handle = sb.run("python -m http.server 8000", timeout=0, wait=False)

    svc = sb.service(port=8000)

    # Open in a browser
    print(svc.browser_url)

    # Or make requests programmatically
    resp = svc.get("/")
    print(resp.status_code)

    handle.kill()
```

## Use cases

| Scenario                                     | How                                                               |
| -------------------------------------------- | ----------------------------------------------------------------- |
| Preview a web app (Streamlit, Jupyter, etc.) | `sb.service(port=<PORT>)` then open `browser_url`                 |
| Call an API from code or CI                  | `svc.get(...)` / `svc.post(...)` or `curl` with the service token |
| Share a live demo with a teammate            | Click **Share Link** in the UI and send the URL                   |

## Open a service from the UI

1. Open the sandbox detail page.
2. Find the **Open service** widget.
3. Type a port number (e.g. `3000`).
4. Click **Open** to launch in a new tab, or **Share Link** to copy a URL you can send to a teammate.

Anyone with the link can access the service, even without a LangSmith account. After the token expires, generate a new link from the UI.

## Open a service from the SDK

### Get a service URL

Call `service()` on a sandbox instance or on the client directly:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
svc = sb.service(port=3000)

# Or from the client, by sandbox name
svc = client.service("my-sandbox", port=3000)

# Customize token lifetime (default: 10 minutes, max: 24 hours)
svc = sb.service(port=3000, expires_in_seconds=3600)
```

<Note>
  The service must be running and listening on the specified port before you request a service URL. The URL only routes traffic and does not start a service for you.
</Note>

### Make requests

The returned `ServiceURL` object has built-in HTTP helpers that handle authentication automatically. Tokens refresh transparently before they expire, so no manual management is needed.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
svc = sb.service(port=8000)

resp = svc.get("/api/items")
resp = svc.post("/api/items", json={"name": "widget"})
resp = svc.put("/api/items/1", json={"name": "updated"})
resp = svc.patch("/api/items/1", json={"status": "active"})
resp = svc.delete("/api/items/1")
```

### Use your own HTTP client

If you prefer a different HTTP client, use the raw URL and token:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import httpx

svc = sb.service(port=8000)

resp = httpx.get(
    svc.service_url + "api/items",
    headers={"X-Langsmith-Sandbox-Service-Token": svc.token},
)
```

### Open in a browser

Use `browser_url` to open the service in a browser. It sets an authentication cookie automatically, so all subsequent page loads, images, and API calls are authenticated without tokens in the URL.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
svc = sb.service(port=8000)
print(svc.browser_url)
```

You can share this URL with teammates. No LangSmith login is required to access it.

### Generate a URL via the REST API

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X POST \
  "$LANGSMITH_ENDPOINT/api/v2/sandboxes/boxes/{sandbox_name}/service-url" \
  -H "x-api-key: $LANGSMITH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"port": 3000, "expires_in_seconds": 3600}'
```

Response:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "browser_url": "https://{sandbox-id}--3000.smithbox.dev/_svc/auth?token=ey...",
  "service_url": "https://{sandbox-id}--3000.smithbox.dev/",
  "token": "ey...",
  "expires_at": "2026-04-08T15:30:00Z"
}
```

## Example: serve a FastAPI app

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langsmith.sandbox import SandboxClient

client = SandboxClient()

with client.sandbox() as sb:
    sb.write("/app/main.py", """
from fastapi import FastAPI

app = FastAPI()
items = []

@app.get("/items")
def list_items():
    return items

@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return item
""")

    sb.run("pip install fastapi uvicorn", timeout=120)
    handle = sb.run(
        "uvicorn main:app --host 0.0.0.0 --port 8000",
        timeout=0,
        wait=False,
        env={"PYTHONPATH": "/app"},
    )

    import time
    time.sleep(3)

    svc = sb.service(port=8000)

    svc.post("/items", json={"name": "widget", "price": 9.99})
    svc.post("/items", json={"name": "gadget", "price": 24.99})

    resp = svc.get("/items")
    print(resp.json())
    # [{"name": "widget", "price": 9.99}, {"name": "gadget", "price": 24.99}]

    # Open the auto-generated API docs in a browser
    print(svc.browser_url)

    handle.kill()
```

## Service URLs vs TCP tunnels

|                         | Service URLs                     | TCP tunnels                           |
| ----------------------- | -------------------------------- | ------------------------------------- |
| **Protocol**            | HTTP                             | Any TCP (databases, Redis, SSH, HTTP) |
| **Setup**               | Zero — just a URL                | Requires SDK or CLI                   |
| **Access from**         | Browser, scripts, CI, anywhere   | Local machine only                    |
| **Sharing**             | Copy the URL and send it         | Not shareable                         |
| **Multi-page web apps** | Full support (subdomain routing) | Full support (local port)             |
| **Non-HTTP services**   | Not supported                    | Full support                          |

Use **service URLs** for HTTP services you want to access from a browser or share with others. Use **[TCP tunnels](/langsmith/sandbox-sdk#tcp-tunnels-python)** for non-HTTP protocols (like `psql` or `redis-cli`) or when you need local-only access.

## Troubleshoot

| Error                          | Cause                             | Fix                                                                                        |
| ------------------------------ | --------------------------------- | ------------------------------------------------------------------------------------------ |
| **"Service link has expired"** | Token lifetime exceeded           | Open the service again from LangSmith or call `sb.service()` for a fresh URL               |
| **"Service is not reachable"** | Nothing is listening on that port | Verify the server is running inside the sandbox                                            |
| **"Authentication required"**  | No token in header or cookie      | Use `browser_url` for browser access or set the `X-Langsmith-Sandbox-Service-Token` header |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandbox-service-urls.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Sandbox snapshots
Source: https://docs.langchain.com/langsmith/sandbox-snapshots

Build and capture reusable filesystem images for sandboxes.

A **snapshot** is a reusable filesystem bundle backed by a Docker image. Build or capture a snapshot when you want to boot sandboxes from a custom filesystem image.

You can also capture a snapshot from a running sandbox—install packages, write data files, or configure state, then snapshot the result and reuse it as a new starting point.

<img alt="Sandboxes snapshots page" />

## Build a snapshot from a Docker image

Build a snapshot by pointing at any Docker image. The call blocks until the snapshot is ready (default timeout is 60 seconds; bump it for large images).

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.sandbox import SandboxClient

  client = SandboxClient()

  snapshot = client.create_snapshot(
      "python",
      docker_image="python:3.12-slim",
      fs_capacity_bytes=1 * 1024**3,  # 1 GiB
  )

  print(snapshot.id)
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { SandboxClient } from "langsmith/sandbox";

  const client = new SandboxClient();

  const snapshot = await client.createSnapshot(
    "python",
    "python:3.12-slim",
    1_073_741_824, // 1 GiB
  );

  console.log(snapshot.id);
  ```
</CodeGroup>

### Private registries

Pass registry credentials (or a pre-registered `registry_id` / `registryId`) to pull from a private registry.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import os

  snapshot = client.create_snapshot(
      "internal-python",
      docker_image="registry.example.com/internal/python:3.12",
      fs_capacity_bytes=2 * 1024**3,
      registry_url="https://registry.example.com",
      registry_username="me",
      registry_password=os.environ["REGISTRY_PASSWORD"],
      timeout=600,
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const snapshot = await client.createSnapshot(
    "internal-python",
    "registry.example.com/internal/python:3.12",
    2_147_483_648,
    {
      registryUrl: "https://registry.example.com",
      registryUsername: "me",
      registryPassword: process.env.REGISTRY_PASSWORD,
      timeout: 600,
    },
  );
  ```
</CodeGroup>

## Build a snapshot from a Dockerfile

When you have a local `Dockerfile` but don't want to publish the image to a registry first, build a snapshot directly from the `Dockerfile` and its build context. LangSmith spins up a temporary builder sandbox, uploads the context, runs the build inside it with [BuildKit](https://docs.docker.com/build/buildkit/), and captures the resulting image as a snapshot. The builder sandbox is torn down automatically once the build finishes.

The call blocks until the snapshot is ready (default timeout is 60 seconds; raise it for large or slow builds). `fs_capacity_bytes` must be large enough to hold the build context, the intermediate layers, and the final image.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith.sandbox import SandboxClient

  client = SandboxClient()

  snapshot = client.create_snapshot_from_dockerfile(
      "my-app",
      dockerfile="Dockerfile",
      fs_capacity_bytes=2 * 1024**3,  # 2 GiB
      context=".",  # build context directory (default: current directory)
  )

  print(snapshot.id)
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { SandboxClient } from "langsmith/sandbox";

  const client = new SandboxClient();

  const snapshot = await client.createSnapshotFromDockerfile(
    "my-app",
    "Dockerfile",
    2_147_483_648, // 2 GiB
    { context: "." },
  );

  console.log(snapshot.id);
  ```
</CodeGroup>

<Note>
  `dockerfile` is resolved relative to `context` unless you pass an absolute path, and it must live inside the context directory. The `.git` directory is excluded from the uploaded context automatically.
</Note>

### Build args and target stage

Pass `build_args` / `buildArgs` to set Docker `ARG` values, and `target` to stop at a specific stage of a multi-stage build.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  snapshot = client.create_snapshot_from_dockerfile(
      "my-app",
      dockerfile="Dockerfile",
      fs_capacity_bytes=2 * 1024**3,
      build_args={"PYTHON_VERSION": "3.12", "ENV": "prod"},
      target="runtime",
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const snapshot = await client.createSnapshotFromDockerfile(
    "my-app",
    "Dockerfile",
    2_147_483_648,
    {
      buildArgs: { PYTHON_VERSION: "3.12", ENV: "prod" },
      target: "runtime",
    },
  );
  ```
</CodeGroup>

### Stream build logs

Pass a callback to `on_build_log` / `onBuildLog` to receive the build's stdout and stderr as it runs, which is useful for surfacing progress or debugging a failing build.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  snapshot = client.create_snapshot_from_dockerfile(
      "my-app",
      dockerfile="Dockerfile",
      fs_capacity_bytes=2 * 1024**3,
      on_build_log=lambda line: print(line, end=""),
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const snapshot = await client.createSnapshotFromDockerfile(
    "my-app",
    "Dockerfile",
    2_147_483_648,
    { onBuildLog: (line) => process.stdout.write(line) },
  );
  ```
</CodeGroup>

### Speed up cold builds

`vcpus` / `vCpus` and `mem_bytes` / `memBytes` size the temporary builder sandbox. The build runs BuildKit plus the native snapshotter's layer copies inside it, which contend for a single core by default, so giving the builder an extra vCPU can cut a cold build's wall time substantially.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  snapshot = client.create_snapshot_from_dockerfile(
      "my-app",
      dockerfile="Dockerfile",
      fs_capacity_bytes=2 * 1024**3,
      vcpus=2,
      mem_bytes=4 * 1024**3,  # 4 GiB
      timeout=600,
  )
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const snapshot = await client.createSnapshotFromDockerfile(
    "my-app",
    "Dockerfile",
    2_147_483_648,
    {
      vCpus: 2,
      memBytes: 4_294_967_296, // 4 GiB
      timeout: 600,
    },
  );
  ```
</CodeGroup>

<Tip>
  Both the sync `SandboxClient` and the `AsyncSandboxClient` expose this method with the same arguments—`await client.create_snapshot_from_dockerfile(...)` on the async client.
</Tip>

## Capture a snapshot from a running sandbox

Start a sandbox from an existing snapshot, install packages or prepare data, then capture the result as a new snapshot. The returned snapshot has its `source_sandbox_id` set to the sandbox it was captured from, and can be used as the `snapshot_id` for any later `create_sandbox` call.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  sb = client.create_sandbox(snapshot_id=base_snapshot_id, name="setup-box")
  sb.run("pip install numpy pandas scikit-learn", timeout=180)
  sb.write("/opt/config.yaml", "model: gpt-5\n")

  # Capture the current filesystem as a new snapshot
  snapshot = sb.capture_snapshot("ml-ready")
  print(snapshot.id, snapshot.source_sandbox_id)

  sb.delete()

  # Boot fresh sandboxes pre-loaded with those dependencies
  with client.sandbox(snapshot_id=snapshot.id) as sb:
      sb.run("python -c 'import numpy; print(numpy.__version__)'")
      assert sb.read("/opt/config.yaml") == b"model: gpt-5\n"
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const running = await client.createSandbox(baseSnapshotId, { name: "setup-box" });
  await running.run("pip install numpy pandas scikit-learn", { timeout: 180 });
  await running.write("/opt/config.yaml", "model: gpt-5\n");

  const snapshot = await running.captureSnapshot("ml-ready");
  console.log(snapshot.id, snapshot.source_sandbox_id);

  await running.delete();

  const sandbox = await client.createSandbox(snapshot.id);
  try {
    await sandbox.run("python -c 'import numpy; print(numpy.__version__)'");
    const cfg = await sandbox.read("/opt/config.yaml");
    console.log(new TextDecoder().decode(cfg));
  } finally {
    await sandbox.delete();
  }
  ```
</CodeGroup>

<Note>
  Capture preserves the **persistent filesystem only**. Installed packages (under `/usr/local`, `/root`, `/opt`, the home directory, etc.) and files you wrote to those locations are kept. Running processes, open sockets, in-memory state, and anything under `/tmp` (which is a tmpfs) are **not** carried over — boot the new sandbox and start the processes you need again.
</Note>

<Tip>
  You can boot a sandbox from a snapshot by **name** instead of ID — handy when you know the human-readable label you captured with:

  <CodeGroup>
    ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    sb = client.create_sandbox(snapshot_name="ml-ready")
    ```

    ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const sb = await client.createSandbox({ snapshotName: "ml-ready" });
    ```
  </CodeGroup>

  Pass at most one of `snapshot_id` / `snapshot_name` (or `snapshotId` / `snapshotName` in TypeScript). Omit both to use the default runtime.
</Tip>

### Tune capture timing

`capture_snapshot` blocks until the new snapshot is ready. Raise the `timeout` kwarg (default 60s) if your filesystem is large or your storage backend is slow.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  snapshot = sb.capture_snapshot("ml-ready-v2", timeout=600)
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const snapshot = await sb.captureSnapshot("ml-ready-v2", { timeout: 600 });
  ```
</CodeGroup>

## List, fetch, and delete snapshots

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # List all snapshots in the workspace
  snapshots = client.list_snapshots()
  for s in snapshots:
      print(s.id, s.name, s.status)

  # Fetch a single snapshot by ID
  snapshot = client.get_snapshot("550e8400-e29b-41d4-a716-446655440000")

  # Delete a snapshot (fails if any sandbox still references it)
  client.delete_snapshot(snapshot.id)
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const snapshots = await client.listSnapshots();
  for (const s of snapshots) {
    console.log(s.id, s.name, s.status);
  }

  const snapshot = await client.getSnapshot("550e8400-e29b-41d4-a716-446655440000");

  await client.deleteSnapshot(snapshot.id);
  ```
</CodeGroup>

<Note>
  `list_snapshots` / `listSnapshots` paginates server-side (default page size 50, max 500) and accepts optional filters: `name_contains` / `nameContains` (case-insensitive substring on name), `limit` (1–500), and `offset` (≥ 0). Page through results by advancing `offset`.

  <CodeGroup>
    ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    page = client.list_snapshots(name_contains="ml", limit=100)
    ```

    ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    const page = await client.listSnapshots({ nameContains: "ml", limit: 100 });
    ```
  </CodeGroup>
</Note>

## Stop and start sandboxes

Sandboxes can be stopped and restarted without losing filesystem state. Files you wrote during the previous run are still there when the sandbox comes back up.

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  sb = client.create_sandbox(snapshot_id=snapshot.id, name="my-vm")
  sb.run("echo 'hello' > /tmp/state.txt")

  # Stop the sandbox — preserves files on disk
  sb.stop()

  # Later: start it again (blocks until ready, default timeout=120s)
  sb.start()

  result = sb.run("cat /tmp/state.txt")
  assert result.stdout.strip() == "hello"
  ```

  ```ts TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  const sb = await client.createSandbox(snapshot.id, { name: "my-vm" });
  await sb.run("echo 'hello' > /tmp/state.txt");

  await sb.stop();

  await sb.start();

  const result = await sb.run("cat /tmp/state.txt");
  console.log(result.stdout.trim()); // "hello"
  ```
</CodeGroup>

You can also stop and start by name via the client directly (`client.stop_sandbox(name)` / `client.start_sandbox(name)` in Python, `client.stopSandbox(name)` / `client.startSandbox(name)` in TypeScript).

## Next steps

* [Create sandboxes from snapshots with the SDK](/langsmith/sandbox-sdk)
* [Expose HTTP services with Service URLs](/langsmith/sandbox-service-urls)
* [Inject credentials via the Auth proxy](/langsmith/sandbox-auth-proxy)

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/sandbox-snapshots.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
