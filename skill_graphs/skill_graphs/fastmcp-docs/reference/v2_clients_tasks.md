[Skip to main content](https://gofastmcp.com/v2/clients/tasks#content-area)
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
  * Authentication
  * Deployment


##### Clients
  * Essentials
  * Core Operations
  * Advanced Features
    * [Elicitation](https://gofastmcp.com/v2/clients/elicitation)
    * [Logging](https://gofastmcp.com/v2/clients/logging)
    * [Progress](https://gofastmcp.com/v2/clients/progress)
    * [Sampling](https://gofastmcp.com/v2/clients/sampling)
    * [ Background Tasks NEW ](https://gofastmcp.com/v2/clients/tasks)
    * [Messages](https://gofastmcp.com/v2/clients/messages)
    * [Roots](https://gofastmcp.com/v2/clients/roots)
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
  * [Requesting Background Execution](https://gofastmcp.com/v2/clients/tasks#requesting-background-execution)
  * [Working with Task Objects](https://gofastmcp.com/v2/clients/tasks#working-with-task-objects)
  * [Real-Time Status Updates](https://gofastmcp.com/v2/clients/tasks#real-time-status-updates)
  * [Graceful Degradation](https://gofastmcp.com/v2/clients/tasks#graceful-degradation)
  * [Complete Example](https://gofastmcp.com/v2/clients/tasks#complete-example)


Advanced Features
# Background Tasks
Copy page
Execute operations asynchronously and track their progress
Copy page
`2.14.0` The  See [Server Background Tasks](https://gofastmcp.com/v2/servers/tasks) for how to enable this on the server side.
##
[​](https://gofastmcp.com/v2/clients/tasks#requesting-background-execution)
Requesting Background Execution
Pass `task=True` to run an operation as a background task. The call returns immediately with a Task object while the work executes on the server.
Copy
```
from fastmcp import Client

async with Client(server) as client:
    # Start a background task
    task = await client.call_tool("slow_computation", {"duration": 10}, task=True)

    print(f"Task started: {task.task_id}")

    # Do other work while it runs...

    # Get the result when ready
    result = await task.result()

```

This works with tools, resources, and prompts:
Copy
```
tool_task = await client.call_tool("my_tool", args, task=True)
resource_task = await client.read_resource("file://large.txt", task=True)
prompt_task = await client.get_prompt("my_prompt", args, task=True)

```

##
[​](https://gofastmcp.com/v2/clients/tasks#working-with-task-objects)
Working with Task Objects
All task types share a common interface for retrieving results, checking status, and receiving updates. To get the result, call `await task.result()` or simply `await task`. This blocks until the task completes and returns the result. You can also check status without blocking using `await task.status()`, which returns the current state (`"working"`, `"completed"`, `"failed"`, or `"cancelled"`) along with any progress message from the server.
Copy
```
task = await client.call_tool("analyze", {"text": "hello"}, task=True)

# Check current status (non-blocking)
status = await task.status()
print(f"{status.status}: {status.statusMessage}")

# Wait for result (blocking)
result = await task.result()

```

For more control over waiting, use `task.wait()` with an optional timeout or target state:
Copy
```
# Wait up to 30 seconds for completion
status = await task.wait(timeout=30.0)

# Wait for a specific state
status = await task.wait(state="completed", timeout=30.0)

```

To cancel a running task, call `await task.cancel()`.
###
[​](https://gofastmcp.com/v2/clients/tasks#real-time-status-updates)
Real-Time Status Updates
Register callbacks to receive status updates as the server reports progress. Both sync and async callbacks are supported.
Copy
```
def on_status_change(status):
    print(f"Task {status.taskId}: {status.status} - {status.statusMessage}")

task.on_status_change(on_status_change)

# Async callbacks work too
async def on_status_async(status):
    await log_status(status)

task.on_status_change(on_status_async)

```

##
[​](https://gofastmcp.com/v2/clients/tasks#graceful-degradation)
Graceful Degradation
You can always pass `task=True` regardless of whether the server supports background tasks. Per the MCP specification, servers without task support execute the operation immediately and return the result inline. The Task API provides a consistent interface either way.
Copy
```
task = await client.call_tool("my_tool", args, task=True)

if task.returned_immediately:
    print("Server executed immediately (no background support)")
else:
    print("Running in background")

# Either way, this works
result = await task.result()

```

This means you can write task-aware client code without worrying about server capabilities.
##
[​](https://gofastmcp.com/v2/clients/tasks#complete-example)
Complete Example
Copy
```
import asyncio
from fastmcp import Client

async def main():
    async with Client(server) as client:
        # Start background task
        task = await client.call_tool(
            "slow_computation",
            {"duration": 10},
            task=True,
        )

        # Subscribe to updates
        def on_update(status):
            print(f"Progress: {status.statusMessage}")

        task.on_status_change(on_update)

        # Do other work while task runs
        print("Doing other work...")
        await asyncio.sleep(2)

        # Wait for completion and get result
        result = await task.result()
        print(f"Result: {result.content}")

asyncio.run(main())

```

[ LLM Sampling Previous ](https://gofastmcp.com/v2/clients/sampling)[ Message Handling Next ](https://gofastmcp.com/v2/clients/messages)
Ctrl+I
