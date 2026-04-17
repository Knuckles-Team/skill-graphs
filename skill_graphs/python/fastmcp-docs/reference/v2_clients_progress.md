[Skip to main content](https://gofastmcp.com/v2/clients/progress#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Advanced Features
Progress Monitoring
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
  * [Progress Handler](https://gofastmcp.com/v2/clients/progress#progress-handler)
  * [Handler Parameters](https://gofastmcp.com/v2/clients/progress#handler-parameters)
  * [Per-Call Progress Handler](https://gofastmcp.com/v2/clients/progress#per-call-progress-handler)


Advanced Features
# Progress Monitoring
Copy page
Handle progress notifications from long-running server operations.
Copy page
`2.3.5` MCP servers can report progress during long-running operations. The client can receive these updates through a progress handler.
##
[​](https://gofastmcp.com/v2/clients/progress#progress-handler)
Progress Handler
Set a progress handler when creating the client:
Copy
```
from fastmcp import Client

async def my_progress_handler(
    progress: float,
    total: float | None,
    message: str | None
) -> None:
    if total is not None:
        percentage = (progress / total) * 100
        print(f"Progress: {percentage:.1f}% - {message or ''}")
    else:
        print(f"Progress: {progress} - {message or ''}")

client = Client(
    "my_mcp_server.py",
    progress_handler=my_progress_handler
)

```

###
[​](https://gofastmcp.com/v2/clients/progress#handler-parameters)
Handler Parameters
The progress handler receives three parameters:
## Progress Handler Parameters
[​](https://gofastmcp.com/v2/clients/progress#param-progress)
progress
float
Current progress value
[​](https://gofastmcp.com/v2/clients/progress#param-total)
total
float | None
Expected total value (may be None)
[​](https://gofastmcp.com/v2/clients/progress#param-message)
message
str | None
Optional status message (may be None)
##
[​](https://gofastmcp.com/v2/clients/progress#per-call-progress-handler)
Per-Call Progress Handler
Override the progress handler for specific tool calls:
Copy
```
async with client:
    # Override with specific progress handler for this call
    result = await client.call_tool(
        "long_running_task",
        {"param": "value"},
        progress_handler=my_progress_handler
    )

```

[ Server Logging Previous ](https://gofastmcp.com/v2/clients/logging)[ LLM Sampling Next ](https://gofastmcp.com/v2/clients/sampling)
Ctrl+I
