[Skip to main content](https://gofastmcp.com/servers/logging#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Features
Client Logging
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
    * [ Background Tasks NEW ](https://gofastmcp.com/servers/tasks)
    * [Composition](https://gofastmcp.com/servers/composition)
    * [ Dependencies NEW ](https://gofastmcp.com/servers/dependency-injection)
    * [Elicitation](https://gofastmcp.com/servers/elicitation)
    * [Icons](https://gofastmcp.com/servers/icons)
    * [ Lifespan NEW ](https://gofastmcp.com/servers/lifespan)
    * [Logging](https://gofastmcp.com/servers/logging)
    * [Middleware](https://gofastmcp.com/servers/middleware)
    * [ Pagination NEW ](https://gofastmcp.com/servers/pagination)
    * [Progress](https://gofastmcp.com/servers/progress)
    * [Sampling](https://gofastmcp.com/servers/sampling)
    * [ Storage Backends NEW ](https://gofastmcp.com/servers/storage-backends)
    * [ Telemetry NEW ](https://gofastmcp.com/servers/telemetry)
    * [Testing](https://gofastmcp.com/servers/testing)
    * [ Versioning NEW ](https://gofastmcp.com/servers/versioning)
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
  * [Basic Usage](https://gofastmcp.com/servers/logging#basic-usage)
  * [Log Levels](https://gofastmcp.com/servers/logging#log-levels)
  * [Structured Logging](https://gofastmcp.com/servers/logging#structured-logging)
  * [Server-Side Logs](https://gofastmcp.com/servers/logging#server-side-logs)
  * [Client Handling](https://gofastmcp.com/servers/logging#client-handling)


Features
# Client Logging
Copy page
Send log messages back to MCP clients through the context.
Copy page
This documentation covers **MCP client logging** —sending messages from your server to MCP clients. For standard server-side logging (e.g., writing to files, console), use `fastmcp.utilities.logging.get_logger()` or Python’s built-in `logging` module.
Server logging allows MCP tools to send debug, info, warning, and error messages back to the client. Unlike standard Python logging, MCP server logging sends messages directly to the client, making them visible in the client’s interface or logs.
##
[​](https://gofastmcp.com/servers/logging#basic-usage)
Basic Usage
Use the context logging methods within any tool function:
Copy
```
from fastmcp import FastMCP, Context

mcp = FastMCP("LoggingDemo")

@mcp.tool
async def analyze_data(data: list[float], ctx: Context) -> dict:
    """Analyze numerical data with comprehensive logging."""
    await ctx.debug("Starting analysis of numerical data")
    await ctx.info(f"Analyzing {len(data)} data points")

    try:
        if not data:
            await ctx.warning("Empty data list provided")
            return {"error": "Empty data list"}

        result = sum(data) / len(data)
        await ctx.info(f"Analysis complete, average: {result}")
        return {"average": result, "count": len(data)}

    except Exception as e:
        await ctx.error(f"Analysis failed: {str(e)}")
        raise

```

##
[​](https://gofastmcp.com/servers/logging#log-levels)
Log Levels
Level | Use Case
---|---
`ctx.debug()` | Detailed execution information for diagnosing problems
`ctx.info()` | General information about normal program execution
`ctx.warning()` | Potentially harmful situations that don’t prevent execution
`ctx.error()` | Error events that might still allow the application to continue
##
[​](https://gofastmcp.com/servers/logging#structured-logging)
Structured Logging
All logging methods accept an `extra` parameter for sending structured data to the client. This is useful for creating rich, queryable logs.
Copy
```
@mcp.tool
async def process_transaction(transaction_id: str, amount: float, ctx: Context):
    await ctx.info(
        f"Processing transaction {transaction_id}",
        extra={
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": "USD"
        }
    )

```

##
[​](https://gofastmcp.com/servers/logging#server-side-logs)
Server-Side Logs
Messages sent to clients via `ctx.log()` and its convenience methods are also logged to the server’s log at `DEBUG` level. Enable debug logging on the `fastmcp.server.context.to_client` logger to see these messages:
Copy
```
import logging
from fastmcp.utilities.logging import get_logger

to_client_logger = get_logger(name="fastmcp.server.context.to_client")
to_client_logger.setLevel(level=logging.DEBUG)

```

##
[​](https://gofastmcp.com/servers/logging#client-handling)
Client Handling
Log messages are sent to the client through the MCP protocol. How clients handle these messages depends on their implementation—development clients may display logs in real-time, production clients may store them for analysis, and integration clients may forward them to external logging systems. See [Client Logging](https://gofastmcp.com/clients/logging) for details on how clients handle server log messages.
[ Lifespans Previous ](https://gofastmcp.com/servers/lifespan)[ Middleware Next ](https://gofastmcp.com/servers/middleware)
Ctrl+I
