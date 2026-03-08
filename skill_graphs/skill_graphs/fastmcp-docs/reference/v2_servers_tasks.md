[Skip to main content](https://gofastmcp.com/v2/servers/tasks#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Advanced Features
Background Tasks
Search the docs...
Ctrl K
Documentation
##### Get Started
  * [Welcome!](https://gofastmcp.com/v2/getting-started/welcome)
  * [Installation](https://gofastmcp.com/v2/getting-started/installation)
  * [Quickstart](https://gofastmcp.com/v2/getting-started/quickstart)
  * [ Updates NEW ](https://gofastmcp.com/v2/updates)


##### Servers
  * [Overview](https://gofastmcp.com/v2/servers/server)
  * Core Components
  * Advanced Features
    * [Composition](https://gofastmcp.com/v2/servers/composition)
    * [Context](https://gofastmcp.com/v2/servers/context)
    * [ Elicitation NEW ](https://gofastmcp.com/v2/servers/elicitation)
    * [ Icons NEW ](https://gofastmcp.com/v2/servers/icons)
    * [Logging](https://gofastmcp.com/v2/servers/logging)
    * [ Middleware NEW ](https://gofastmcp.com/v2/servers/middleware)
    * [Progress](https://gofastmcp.com/v2/servers/progress)
    * [Proxy Servers](https://gofastmcp.com/v2/servers/proxy)
    * [ Sampling NEW ](https://gofastmcp.com/v2/servers/sampling)
    * [ Storage Backends NEW ](https://gofastmcp.com/v2/servers/storage-backends)
    * [ Background Tasks NEW ](https://gofastmcp.com/v2/servers/tasks)
  * Authentication
  * Deployment


##### Clients
  * Essentials
  * Core Operations
  * Advanced Features
  * Authentication


##### Integrations
  * Authentication
  * Authorization
  * AI Assistants
  * AI SDKs
  * API Integration


##### Patterns
  * [Tool Transformation](https://gofastmcp.com/v2/patterns/tool-transformation)
  * [Decorating Methods](https://gofastmcp.com/v2/patterns/decorating-methods)
  * [CLI](https://gofastmcp.com/v2/patterns/cli)
  * [Contrib Modules](https://gofastmcp.com/v2/patterns/contrib)
  * [Testing](https://gofastmcp.com/v2/patterns/testing)


##### Development
  * [Contributing](https://gofastmcp.com/v2/development/contributing)
  * [Tests](https://gofastmcp.com/v2/development/tests)
  * [Releases](https://gofastmcp.com/v2/development/releases)
  * [ Upgrade Guide NEW ](https://gofastmcp.com/v2/development/upgrade-guide)
  * [Changelog](https://gofastmcp.com/v2/changelog)


These are the docs for FastMCP 2.0. [FastMCP 3.0](https://gofastmcp.com/getting-started/welcome) is now available.
On this page
  * [What Are MCP Background Tasks?](https://gofastmcp.com/v2/servers/tasks#what-are-mcp-background-tasks)
  * [MCP Background Tasks vs Python Concurrency](https://gofastmcp.com/v2/servers/tasks#mcp-background-tasks-vs-python-concurrency)
  * [Enabling Background Tasks](https://gofastmcp.com/v2/servers/tasks#enabling-background-tasks)
  * [Execution Modes](https://gofastmcp.com/v2/servers/tasks#execution-modes)
  * [Server-Wide Default](https://gofastmcp.com/v2/servers/tasks#server-wide-default)
  * [Graceful Degradation](https://gofastmcp.com/v2/servers/tasks#graceful-degradation)
  * [Configuration](https://gofastmcp.com/v2/servers/tasks#configuration)
  * [Backends](https://gofastmcp.com/v2/servers/tasks#backends)
  * [In-Memory Backend (Default)](https://gofastmcp.com/v2/servers/tasks#in-memory-backend-default)
  * [Redis Backend](https://gofastmcp.com/v2/servers/tasks#redis-backend)
  * [Workers](https://gofastmcp.com/v2/servers/tasks#workers)
  * [Progress Reporting](https://gofastmcp.com/v2/servers/tasks#progress-reporting)
  * [Docket Dependencies](https://gofastmcp.com/v2/servers/tasks#docket-dependencies)


Advanced Features
# Background Tasks
Copy page
Run long-running operations asynchronously with progress tracking
Copy page
`2.14.0` FastMCP implements the MCP background task protocol (
**What is Docket?** FastMCP’s task system is powered by
##
[​](https://gofastmcp.com/v2/servers/tasks#what-are-mcp-background-tasks)
What Are MCP Background Tasks?
In MCP, all component interactions are blocking by default. When a client calls a tool, reads a resource, or fetches a prompt, it sends a request and waits for the response. For operations that take seconds or minutes, this creates a poor user experience. The MCP background task protocol solves this by letting clients:
  1. **Start** an operation and receive a task ID immediately
  2. **Track** progress as the operation runs
  3. **Retrieve** the result when ready

FastMCP handles all of this for you. Add `task=True` to your decorator, and your function gains full background execution with progress reporting, distributed processing, and horizontal scaling.
###
[​](https://gofastmcp.com/v2/servers/tasks#mcp-background-tasks-vs-python-concurrency)
MCP Background Tasks vs Python Concurrency
You can always use Python’s concurrency primitives (asyncio, threads, multiprocessing) or external task queues in your FastMCP servers. FastMCP is just Python—run code however you like. MCP background tasks are different: they’re **protocol-native**. This means MCP clients that support the task protocol can start operations, receive progress updates, and retrieve results through the standard MCP interface. The coordination happens at the protocol level, not inside your application code.
##
[​](https://gofastmcp.com/v2/servers/tasks#enabling-background-tasks)
Enabling Background Tasks
Add `task=True` to any tool, resource, resource template, or prompt decorator. This marks the component as capable of background execution.
Copy
```
import asyncio
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool(task=True)
async def slow_computation(duration: int) -> str:
    """A long-running operation."""
    for i in range(duration):
        await asyncio.sleep(1)
    return f"Completed in {duration} seconds"

```

When a client requests background execution, the call returns immediately with a task ID. The work executes in a background worker, and the client can poll for status or wait for the result.
Background tasks require async functions. Attempting to use `task=True` with a sync function raises a `ValueError` at registration time.
##
[​](https://gofastmcp.com/v2/servers/tasks#execution-modes)
Execution Modes
For fine-grained control over task execution behavior, use `TaskConfig` instead of the boolean shorthand. The MCP task protocol defines three execution modes:
Mode | Client calls without task | Client calls with task
---|---|---
`"forbidden"` | Executes synchronously | Error: task not supported
`"optional"` | Executes synchronously | Executes as background task
`"required"` | Error: task required | Executes as background task
Copy
```
from fastmcp import FastMCP
from fastmcp.server.tasks import TaskConfig

mcp = FastMCP("MyServer")

# Supports both sync and background execution (default when task=True)
@mcp.tool(task=TaskConfig(mode="optional"))
async def flexible_task() -> str:
    return "Works either way"

# Requires background execution - errors if client doesn't request task
@mcp.tool(task=TaskConfig(mode="required"))
async def must_be_background() -> str:
    return "Only runs as a background task"

# No task support (default when task=False or omitted)
@mcp.tool(task=TaskConfig(mode="forbidden"))
async def sync_only() -> str:
    return "Never runs as background task"

```

The boolean shortcuts map to these modes:
  * `task=True` → `TaskConfig(mode="optional")`
  * `task=False` → `TaskConfig(mode="forbidden")`


###
[​](https://gofastmcp.com/v2/servers/tasks#server-wide-default)
Server-Wide Default
To enable background task support for all components by default, pass `tasks=True` to the constructor. Individual decorators can still override this with `task=False`.
Copy
```
mcp = FastMCP("MyServer", tasks=True)

```

If your server defines any synchronous tools, resources, or prompts, you will need to explicitly set `task=False` on their decorators to avoid an error.
###
[​](https://gofastmcp.com/v2/servers/tasks#graceful-degradation)
Graceful Degradation
When a client requests background execution but the component has `mode="forbidden"`, FastMCP executes synchronously and returns the result inline. This follows the SEP-1686 specification for graceful degradation—clients can always request background execution without worrying about server capabilities. Conversely, when a component has `mode="required"` but the client doesn’t request background execution, FastMCP returns an error indicating that task execution is required.
###
[​](https://gofastmcp.com/v2/servers/tasks#configuration)
Configuration
Environment Variable | Default | Description
---|---|---
`FASTMCP_DOCKET_URL` | `memory://` | Backend URL (`memory://` or `redis://host:port/db`)
##
[​](https://gofastmcp.com/v2/servers/tasks#backends)
Backends
FastMCP supports two backends for task execution, each with different tradeoffs.
###
[​](https://gofastmcp.com/v2/servers/tasks#in-memory-backend-default)
In-Memory Backend (Default)
The in-memory backend (`memory://`) requires zero configuration and works out of the box. **Advantages:**
  * No external dependencies
  * Simple single-process deployment

**Disadvantages:**
  * **Ephemeral** : If the server restarts, all pending tasks are lost
  * **Higher latency** : ~250ms task pickup time vs single-digit milliseconds with Redis
  * **No horizontal scaling** : Single process only—you cannot add additional workers


###
[​](https://gofastmcp.com/v2/servers/tasks#redis-backend)
Redis Backend
For production deployments, use Redis (or Valkey) as your backend by setting `FASTMCP_DOCKET_URL=redis://localhost:6379`. **Advantages:**
  * **Persistent** : Tasks survive server restarts
  * **Fast** : Single-digit millisecond task pickup latency
  * **Scalable** : Add workers to distribute load across processes or machines


##
[​](https://gofastmcp.com/v2/servers/tasks#workers)
Workers
Every FastMCP server with task-enabled components automatically starts an **embedded worker**. You do not need to start a separate worker process for tasks to execute. To scale horizontally, add more workers using the CLI:
Copy
```
fastmcp tasks worker server.py

```

Each additional worker pulls tasks from the same queue, distributing load across processes. Configure worker concurrency via environment:
Copy
```
export FASTMCP_DOCKET_CONCURRENCY=20
fastmcp tasks worker server.py

```

Additional workers only work with Redis/Valkey backends. The in-memory backend is single-process only.
##
[​](https://gofastmcp.com/v2/servers/tasks#progress-reporting)
Progress Reporting
The `Progress` dependency lets you report progress back to clients. Inject it as a parameter with a default value, and FastMCP will provide the active progress reporter.
Copy
```
from fastmcp import FastMCP
from fastmcp.dependencies import Progress

mcp = FastMCP("MyServer")

@mcp.tool(task=True)
async def process_files(files: list[str], progress: Progress = Progress()) -> str:
    await progress.set_total(len(files))

    for file in files:
        await progress.set_message(f"Processing {file}")
        # ... do work ...
        await progress.increment()

    return f"Processed {len(files)} files"

```

The progress API:
  * `await progress.set_total(n)` — Set the total number of steps
  * `await progress.increment(amount=1)` — Increment progress
  * `await progress.set_message(text)` — Update the status message

Progress works in both immediate and background execution modes—you can use the same code regardless of how the client invokes your function.
##
[​](https://gofastmcp.com/v2/servers/tasks#docket-dependencies)
Docket Dependencies
FastMCP exposes Docket’s full dependency injection system within your task-enabled functions. Beyond `Progress`, you can access the Docket instance, worker information, and use advanced features like retries and timeouts.
Copy
```
from docket import Docket, Worker
from fastmcp import FastMCP
from fastmcp.dependencies import Progress, CurrentDocket, CurrentWorker

mcp = FastMCP("MyServer")

@mcp.tool(task=True)
async def my_task(
    progress: Progress = Progress(),
    docket: Docket = CurrentDocket(),
    worker: Worker = CurrentWorker(),
) -> str:
    # Schedule additional background work
    await docket.add(another_task, arg1, arg2)

    # Access worker metadata
    worker_name = worker.name

    return "Done"

```

With `CurrentDocket()`, you can schedule additional background tasks, chain work together, and coordinate complex workflows. See the
[ Storage Backends Previous ](https://gofastmcp.com/v2/servers/storage-backends)[ Authentication Next ](https://gofastmcp.com/v2/servers/auth/authentication)
Ctrl+I
