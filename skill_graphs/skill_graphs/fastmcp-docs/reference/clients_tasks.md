[Skip to main content](https://gofastmcp.com/clients/tasks#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Handlers
Background Tasks
Search the docs...
Ctrl K
Documentation
##### Get Started
  * [Welcome!](https://gofastmcp.com/getting-started/welcome)
  * [Installation](https://gofastmcp.com/getting-started/installation)
  * [Quickstart](https://gofastmcp.com/getting-started/quickstart)


##### Servers
  * [Overview](https://gofastmcp.com/servers/server)
  * Core Components
  * FeaturesUPDATED
  * ProvidersNEW
  * TransformsNEW
  * AuthenticationUPDATED
  * [ Authorization NEW ](https://gofastmcp.com/servers/authorization)
  * Deployment


##### Apps
  * [ Overview NEW ](https://gofastmcp.com/apps/overview)
  * [ Prefab Apps SOON ](https://gofastmcp.com/apps/prefab)
  * [ Patterns SOON ](https://gofastmcp.com/apps/patterns)
  * [ Custom HTML NEW ](https://gofastmcp.com/apps/low-level)


##### Clients
  * [Overview](https://gofastmcp.com/clients/client)
  * [Transports](https://gofastmcp.com/clients/transports)
  * Core Operations
  * HandlersUPDATED
    * [Notifications](https://gofastmcp.com/clients/notifications)
    * [Sampling](https://gofastmcp.com/clients/sampling)
    * [Elicitation](https://gofastmcp.com/clients/elicitation)
    * [ Tasks NEW ](https://gofastmcp.com/clients/tasks)
    * [Progress](https://gofastmcp.com/clients/progress)
    * [Logging](https://gofastmcp.com/clients/logging)
    * [Roots](https://gofastmcp.com/clients/roots)
  * AuthenticationUPDATED


##### Integrations
  * Auth
  * Web Frameworks
  * AI Assistants
  * AI SDKs
  * [MCP.json](https://gofastmcp.com/integrations/mcp-json-configuration)


##### CLI
  * [Overview](https://gofastmcp.com/cli/overview)
  * [Running](https://gofastmcp.com/cli/running)
  * [Install MCPs](https://gofastmcp.com/cli/install-mcp)
  * [Inspecting](https://gofastmcp.com/cli/inspecting)
  * [Client](https://gofastmcp.com/cli/client)
  * [Generate CLI](https://gofastmcp.com/cli/generate-cli)
  * [Auth](https://gofastmcp.com/cli/auth)


##### More
  * Upgrading
  * Development
  * What's New


On this page
  * [Requesting Background Execution](https://gofastmcp.com/clients/tasks#requesting-background-execution)
  * [Task API](https://gofastmcp.com/clients/tasks#task-api)
  * [Getting Results](https://gofastmcp.com/clients/tasks#getting-results)
  * [Checking Status](https://gofastmcp.com/clients/tasks#checking-status)
  * [Waiting with Control](https://gofastmcp.com/clients/tasks#waiting-with-control)
  * [Cancellation](https://gofastmcp.com/clients/tasks#cancellation)
  * [Status Updates](https://gofastmcp.com/clients/tasks#status-updates)
  * [Handler Template](https://gofastmcp.com/clients/tasks#handler-template)
  * [Graceful Degradation](https://gofastmcp.com/clients/tasks#graceful-degradation)
  * [Example](https://gofastmcp.com/clients/tasks#example)


Handlers
# Background Tasks
Copy page
Execute operations asynchronously and track their progress.
Copy page
`2.14.0` Use this when you need to run long operations asynchronously while doing other work. The MCP task protocol lets you request operations to run in the background. The call returns a Task object immediately, letting you track progress, cancel operations, or await results.
##
[​](https://gofastmcp.com/clients/tasks#requesting-background-execution)
Requesting Background Execution
Pass `task=True` to run an operation as a background task:
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
[​](https://gofastmcp.com/clients/tasks#task-api)
Task API
All task types share a common interface.
###
[​](https://gofastmcp.com/clients/tasks#getting-results)
Getting Results
Call `await task.result()` or simply `await task` to block until the task completes:
Copy
```
task = await client.call_tool("analyze", {"text": "hello"}, task=True)

# Wait for result (blocking)
result = await task.result()
# or: result = await task

```

###
[​](https://gofastmcp.com/clients/tasks#checking-status)
Checking Status
Check the current status without blocking:
Copy
```
status = await task.status()
print(f"{status.status}: {status.statusMessage}")
# status.status is "working", "completed", "failed", or "cancelled"

```

###
[​](https://gofastmcp.com/clients/tasks#waiting-with-control)
Waiting with Control
Use `task.wait()` for more control over waiting:
Copy
```
# Wait up to 30 seconds for completion
status = await task.wait(timeout=30.0)

# Wait for a specific state
status = await task.wait(state="completed", timeout=30.0)

```

###
[​](https://gofastmcp.com/clients/tasks#cancellation)
Cancellation
Cancel a running task:
Copy
```
await task.cancel()

```

##
[​](https://gofastmcp.com/clients/tasks#status-updates)
Status Updates
Register callbacks to receive real-time status updates as the server reports progress:
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

###
[​](https://gofastmcp.com/clients/tasks#handler-template)
Handler Template
Copy
```
from fastmcp import Client

def status_handler(status):
    """
    Handle task status updates.

    Args:
        status: Task status object with:
            - taskId: Unique task identifier
            - status: "working", "completed", "failed", or "cancelled"
            - statusMessage: Optional progress message from server
    """
    if status.status == "working":
        print(f"Progress: {status.statusMessage}")
    elif status.status == "completed":
        print("Task completed")
    elif status.status == "failed":
        print(f"Task failed: {status.statusMessage}")

task.on_status_change(status_handler)

```

##
[​](https://gofastmcp.com/clients/tasks#graceful-degradation)
Graceful Degradation
You can always pass `task=True` regardless of whether the server supports background tasks. Per the MCP specification, servers without task support execute the operation immediately and return the result inline.
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

This lets you write task-aware client code without worrying about server capabilities.
##
[​](https://gofastmcp.com/clients/tasks#example)
Example
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

See [Server Background Tasks](https://gofastmcp.com/servers/tasks) for how to enable background task support on the server side.
[ User Elicitation Previous ](https://gofastmcp.com/clients/elicitation)[ Progress Monitoring Next ](https://gofastmcp.com/clients/progress)
Ctrl+I
