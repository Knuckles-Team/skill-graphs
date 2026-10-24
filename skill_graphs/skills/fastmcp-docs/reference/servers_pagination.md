[Skip to main content](https://gofastmcp.com/servers/pagination#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Features
Pagination
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
  * [Server Configuration](https://gofastmcp.com/servers/pagination#server-configuration)
  * [Cursor Format](https://gofastmcp.com/servers/pagination#cursor-format)
  * [Client Behavior](https://gofastmcp.com/servers/pagination#client-behavior)
  * [Manual Pagination](https://gofastmcp.com/servers/pagination#manual-pagination)
  * [When to Use Pagination](https://gofastmcp.com/servers/pagination#when-to-use-pagination)


Features
# Pagination
Copy page
Control how servers return large lists of components to clients.
Copy page
`3.0.0` When a server exposes many tools, resources, or prompts, returning them all in a single response can be impractical. MCP supports pagination for list operations, allowing servers to return results in manageable chunks that clients can fetch incrementally.
##
[​](https://gofastmcp.com/servers/pagination#server-configuration)
Server Configuration
By default, FastMCP servers return all components in a single response for backward compatibility. To enable pagination, set the `list_page_size` parameter when creating your server. This value determines the maximum number of items returned per page across all list operations.
Copy
```
from fastmcp import FastMCP

# Enable pagination with 50 items per page
server = FastMCP("ComponentRegistry", list_page_size=50)

# Register tools (in practice, these might come from a database or config)
@server.tool
def search(query: str) -> str:
    return f"Results for: {query}"

@server.tool
def analyze(data: str) -> dict:
    return {"status": "analyzed", "data": data}

# ... many more tools, resources, prompts

```

When `list_page_size` is configured, the `tools/list`, `resources/list`, `resources/templates/list`, and `prompts/list` endpoints all paginate their responses. Each response includes a `nextCursor` field when more results exist, which clients use to fetch subsequent pages.
###
[​](https://gofastmcp.com/servers/pagination#cursor-format)
Cursor Format
Cursors are opaque base64-encoded strings per the MCP specification. Clients should treat them as black boxes, passing them unchanged between requests. The cursor encodes the offset into the result set, but this is an implementation detail that may change.
##
[​](https://gofastmcp.com/servers/pagination#client-behavior)
Client Behavior
The FastMCP Client handles pagination transparently. Convenience methods like `list_tools()`, `list_resources()`, `list_resource_templates()`, and `list_prompts()` automatically fetch all pages and return the complete list. Existing code continues to work without modification.
Copy
```
from fastmcp import Client

async with Client(server) as client:
    # Returns all 200 tools, fetching pages automatically
    tools = await client.list_tools()
    print(f"Total tools: {len(tools)}")  # 200

```

###
[​](https://gofastmcp.com/servers/pagination#manual-pagination)
Manual Pagination
For scenarios where you want to process results incrementally (memory-constrained environments, progress reporting, or early termination), use the `_mcp` variants with explicit cursor handling.
Copy
```
from fastmcp import Client

async with Client(server) as client:
    # Fetch first page
    result = await client.list_tools_mcp()
    print(f"Page 1: {len(result.tools)} tools")

    # Continue fetching while more pages exist
    while result.nextCursor:
        result = await client.list_tools_mcp(cursor=result.nextCursor)
        print(f"Next page: {len(result.tools)} tools")

```

The `_mcp` methods return the raw MCP protocol objects, which include both the items and the `nextCursor` for the next page. When `nextCursor` is `None`, you’ve reached the end of the result set. All four list operations support manual pagination:
Operation | Convenience Method | Manual Method
---|---|---
Tools | `list_tools()` | `list_tools_mcp(cursor=...)`
Resources | `list_resources()` | `list_resources_mcp(cursor=...)`
Resource Templates | `list_resource_templates()` | `list_resource_templates_mcp(cursor=...)`
Prompts | `list_prompts()` | `list_prompts_mcp(cursor=...)`
##
[​](https://gofastmcp.com/servers/pagination#when-to-use-pagination)
When to Use Pagination
Pagination becomes valuable when your server exposes a large number of components. Consider enabling it when:
  * Your server dynamically generates many components (e.g., from a database or file system)
  * Memory usage is a concern for clients
  * You want to reduce initial response latency

For servers with a fixed, modest number of components (fewer than 100), pagination adds complexity without meaningful benefit. The default behavior of returning everything in one response is simpler and efficient for typical use cases.
[ Middleware Previous ](https://gofastmcp.com/servers/middleware)[ Progress Reporting Next ](https://gofastmcp.com/servers/progress)
Ctrl+I
