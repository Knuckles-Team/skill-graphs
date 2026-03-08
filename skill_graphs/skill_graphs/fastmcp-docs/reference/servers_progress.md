[Skip to main content](https://gofastmcp.com/servers/progress#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Features
Progress Reporting
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
  * [Basic Usage](https://gofastmcp.com/servers/progress#basic-usage)
  * [Progress Patterns](https://gofastmcp.com/servers/progress#progress-patterns)
  * [Client Requirements](https://gofastmcp.com/servers/progress#client-requirements)


Features
# Progress Reporting
Copy page
Update clients on the progress of long-running operations through the MCP context.
Copy page
Progress reporting allows MCP tools to notify clients about the progress of long-running operations. Clients can display progress indicators and provide better user experience during time-consuming tasks.
##
[​](https://gofastmcp.com/servers/progress#basic-usage)
Basic Usage
Use `ctx.report_progress()` to send progress updates to the client. The method accepts a `progress` value representing how much work is complete, and an optional `total` representing the full scope of work.
Copy
```
from fastmcp import FastMCP, Context
import asyncio

mcp = FastMCP("ProgressDemo")

@mcp.tool
async def process_items(items: list[str], ctx: Context) -> dict:
    """Process a list of items with progress updates."""
    total = len(items)
    results = []

    for i, item in enumerate(items):
        await ctx.report_progress(progress=i, total=total)
        await asyncio.sleep(0.1)
        results.append(item.upper())

    await ctx.report_progress(progress=total, total=total)
    return {"processed": len(results), "results": results}

```

##
[​](https://gofastmcp.com/servers/progress#progress-patterns)
Progress Patterns
Pattern | Description | Example
---|---|---
Percentage | Progress as 0-100 percentage | `progress=75, total=100`
Absolute | Completed items of a known count | `progress=3, total=10`
Indeterminate | Progress without known endpoint |  `progress=files_found` (no total)
For multi-stage operations, map each stage to a portion of the total progress range. A four-stage operation might allocate 0-25% to validation, 25-60% to export, 60-80% to transform, and 80-100% to import.
##
[​](https://gofastmcp.com/servers/progress#client-requirements)
Client Requirements
Progress reporting requires clients to support progress handling. Clients must send a `progressToken` in the initial request to receive progress updates. If no progress token is provided, progress calls have no effect (they don’t error). See [Client Progress](https://gofastmcp.com/clients/progress) for details on implementing client-side progress handling.
[ Pagination Previous ](https://gofastmcp.com/servers/pagination)[ Sampling Next ](https://gofastmcp.com/servers/sampling)
Ctrl+I
