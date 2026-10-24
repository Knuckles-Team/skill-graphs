[Skip to main content](https://gofastmcp.com/servers/composition#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Features
Composing Servers
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
  * [Mounting External Servers](https://gofastmcp.com/servers/composition#mounting-external-servers)
  * [Mounting npm/uvx Packages](https://gofastmcp.com/servers/composition#mounting-npm%2Fuvx-packages)
  * [Namespacing](https://gofastmcp.com/servers/composition#namespacing)
  * [How Namespacing Works](https://gofastmcp.com/servers/composition#how-namespacing-works)
  * [Dynamic Composition](https://gofastmcp.com/servers/composition#dynamic-composition)
  * [Tag Filtering](https://gofastmcp.com/servers/composition#tag-filtering)
  * [Performance Considerations](https://gofastmcp.com/servers/composition#performance-considerations)
  * [Custom Routes](https://gofastmcp.com/servers/composition#custom-routes)
  * [Conflict Resolution](https://gofastmcp.com/servers/composition#conflict-resolution)


Features
# Composing Servers
Copy page
Combine multiple servers into one
Copy page
`2.2.0` As your application grows, you’ll want to split it into focused servers — one for weather, one for calendar, one for admin — and combine them into a single server that clients connect to. That’s what `mount()` does. When you mount a server, all its tools, resources, and prompts become available through the parent. The connection is live: add a tool to the child after mounting, and it’s immediately visible through the parent.
Copy
```
from fastmcp import FastMCP

weather = FastMCP("Weather")

@weather.tool
def get_forecast(city: str) -> str:
    """Get weather forecast for a city."""
    return f"Sunny in {city}"

@weather.resource("data://cities")
def list_cities() -> list[str]:
    """List supported cities."""
    return ["London", "Paris", "Tokyo"]

main = FastMCP("MainApp")
main.mount(weather)

# main now serves get_forecast and data://cities

```

##
[​](https://gofastmcp.com/servers/composition#mounting-external-servers)
Mounting External Servers
Mount remote HTTP servers or subprocess-based MCP servers using `create_proxy()`:
Copy
```
from fastmcp import FastMCP
from fastmcp.server import create_proxy

mcp = FastMCP("Orchestrator")

# Mount a remote HTTP server (URLs work directly)
mcp.mount(create_proxy("http://api.example.com/mcp"), namespace="api")

# Mount local Python scripts (file paths work directly)
mcp.mount(create_proxy("./my_server.py"), namespace="local")

```

###
[​](https://gofastmcp.com/servers/composition#mounting-npm/uvx-packages)
Mounting npm/uvx Packages
For npm packages or Python tools, use the config dict format:
Copy
```
from fastmcp import FastMCP
from fastmcp.server import create_proxy

mcp = FastMCP("Orchestrator")

# Mount npm package via config
github_config = {
    "mcpServers": {
        "default": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-github"]
        }
    }
}
mcp.mount(create_proxy(github_config), namespace="github")

# Mount Python tool via config
sqlite_config = {
    "mcpServers": {
        "default": {
            "command": "uvx",
            "args": ["mcp-server-sqlite", "--db", "data.db"]
        }
    }
}
mcp.mount(create_proxy(sqlite_config), namespace="db")

```

Or use explicit transport classes:
Copy
```
from fastmcp import FastMCP
from fastmcp.server import create_proxy
from fastmcp.client.transports import NpxStdioTransport, UvxStdioTransport

mcp = FastMCP("Orchestrator")

mcp.mount(
    create_proxy(NpxStdioTransport(package="@modelcontextprotocol/server-github")),
    namespace="github"
)
mcp.mount(
    create_proxy(UvxStdioTransport(tool_name="mcp-server-sqlite", tool_args=["--db", "data.db"])),
    namespace="db"
)

```

For advanced configuration, see [Proxying](https://gofastmcp.com/servers/providers/proxy).
##
[​](https://gofastmcp.com/servers/composition#namespacing)
Namespacing
`3.0.0` When mounting multiple servers, use namespaces to avoid naming conflicts:
Copy
```
weather = FastMCP("Weather")
calendar = FastMCP("Calendar")

@weather.tool
def get_data() -> str:
    return "Weather data"

@calendar.tool
def get_data() -> str:
    return "Calendar data"

main = FastMCP("Main")
main.mount(weather, namespace="weather")
main.mount(calendar, namespace="calendar")

# Tools are now:
# - weather_get_data
# - calendar_get_data

```

###
[​](https://gofastmcp.com/servers/composition#how-namespacing-works)
How Namespacing Works
Component Type | Without Namespace | With `namespace="api"`
---|---|---
Tool | `my_tool` | `api_my_tool`
Prompt | `my_prompt` | `api_my_prompt`
Resource | `data://info` | `data://api/info`
Template | `data://{id}` | `data://api/{id}`
Namespacing uses [transforms](https://gofastmcp.com/servers/transforms/transforms) under the hood.
##
[​](https://gofastmcp.com/servers/composition#dynamic-composition)
Dynamic Composition
Because `mount()` creates a live link, you can add components to a child server after mounting and they’ll be immediately available through the parent:
Copy
```
main = FastMCP("Main")
main.mount(dynamic_server, namespace="dynamic")

# Add a tool AFTER mounting - it's accessible through main
@dynamic_server.tool
def added_later() -> str:
    return "Added after mounting!"

```

##
[​](https://gofastmcp.com/servers/composition#tag-filtering)
Tag Filtering
`3.0.0` Parent server tag filters apply recursively to mounted servers:
Copy
```
api_server = FastMCP("API")

@api_server.tool(tags={"production"})
def prod_endpoint() -> str:
    return "Production data"

@api_server.tool(tags={"development"})
def dev_endpoint() -> str:
    return "Debug data"

# Mount with production filter
prod_app = FastMCP("Production")
prod_app.mount(api_server, namespace="api")
prod_app.enable(tags={"production"}, only=True)

# Only prod_endpoint (namespaced as api_prod_endpoint) is visible

```

##
[​](https://gofastmcp.com/servers/composition#performance-considerations)
Performance Considerations
Operations like `list_tools()` on the parent are affected by the performance of all mounted servers. This is particularly noticeable with:
  * HTTP-based mounted servers (300-400ms vs 1-2ms for local tools)
  * Mounted servers with slow initialization
  * Deep mounting hierarchies

If low latency is critical, consider implementing caching strategies or limiting mounting depth.
##
[​](https://gofastmcp.com/servers/composition#custom-routes)
Custom Routes
`2.4.0` Custom HTTP routes defined with `@server.custom_route()` are also forwarded when mounting:
Copy
```
subserver = FastMCP("Sub")

@subserver.custom_route("/health", methods=["GET"])
async def health_check():
    return {"status": "ok"}

main = FastMCP("Main")
main.mount(subserver, namespace="sub")

# /health is now accessible through main's HTTP app

```

##
[​](https://gofastmcp.com/servers/composition#conflict-resolution)
Conflict Resolution
`3.0.0` When mounting multiple servers with the same namespace (or no namespace), the **most recently mounted** server takes precedence for conflicting component names:
Copy
```
server_a = FastMCP("A")
server_b = FastMCP("B")

@server_a.tool
def shared_tool() -> str:
    return "From A"

@server_b.tool
def shared_tool() -> str:
    return "From B"

main = FastMCP("Main")
main.mount(server_a)
main.mount(server_b)

# shared_tool returns "From B" (most recently mounted)

```

[ Background Tasks Previous ](https://gofastmcp.com/servers/tasks)[ Dependency Injection Next ](https://gofastmcp.com/servers/dependency-injection)
Ctrl+I
