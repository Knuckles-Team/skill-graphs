[Skip to main content](https://gofastmcp.com/servers/transforms/namespace#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Transforms
Namespace Transform
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
    * [ Overview NEW ](https://gofastmcp.com/servers/transforms/transforms)
    * [ Namespace NEW ](https://gofastmcp.com/servers/transforms/namespace)
    * [ Tool Transformation NEW ](https://gofastmcp.com/servers/transforms/tool-transformation)
    * [ Visibility NEW ](https://gofastmcp.com/servers/visibility)
    * [ Code Mode NEW ](https://gofastmcp.com/servers/transforms/code-mode)
    * [ Tool Search NEW ](https://gofastmcp.com/servers/transforms/tool-search)
    * [ Resources as Tools NEW ](https://gofastmcp.com/servers/transforms/resources-as-tools)
    * [ Prompts as Tools NEW ](https://gofastmcp.com/servers/transforms/prompts-as-tools)
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


Transforms
# Namespace Transform
Copy page
Prefix component names to prevent conflicts
Copy page
`3.0.0` The `Namespace` transform prefixes all component names, preventing conflicts when composing multiple servers. Tools and prompts receive an underscore-separated prefix. Resources and templates receive a path-segment prefix in their URIs.
Component | Original | With `Namespace("api")`
---|---|---
Tool | `my_tool` | `api_my_tool`
Prompt | `my_prompt` | `api_my_prompt`
Resource | `data://info` | `data://api/info`
Template | `data://{id}` | `data://api/{id}`
The most common use is through the `mount()` method’s `namespace` parameter.
Copy
```
from fastmcp import FastMCP

weather = FastMCP("Weather")
calendar = FastMCP("Calendar")

@weather.tool
def get_data() -> str:
    return "Weather data"

@calendar.tool
def get_data() -> str:
    return "Calendar data"

# Without namespacing, these would conflict
main = FastMCP("Main")
main.mount(weather, namespace="weather")
main.mount(calendar, namespace="calendar")

# Clients see: weather_get_data, calendar_get_data

```

You can also apply namespacing directly using the `Namespace` transform.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.transforms import Namespace

mcp = FastMCP("Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Namespace all components
mcp.add_transform(Namespace("api"))

# Tool is now: api_greet

```

[ Transforms Overview Previous ](https://gofastmcp.com/servers/transforms/transforms)[ Tool Transformation Next ](https://gofastmcp.com/servers/transforms/tool-transformation)
Ctrl+I
