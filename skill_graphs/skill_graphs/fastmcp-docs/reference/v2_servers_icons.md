[Skip to main content](https://gofastmcp.com/v2/servers/icons#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Advanced Features
Icons
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
  * [Icon Format](https://gofastmcp.com/v2/servers/icons#icon-format)
  * [Server Icons](https://gofastmcp.com/v2/servers/icons#server-icons)
  * [Component Icons](https://gofastmcp.com/v2/servers/icons#component-icons)
  * [Tool Icons](https://gofastmcp.com/v2/servers/icons#tool-icons)
  * [Resource Icons](https://gofastmcp.com/v2/servers/icons#resource-icons)
  * [Resource Template Icons](https://gofastmcp.com/v2/servers/icons#resource-template-icons)
  * [Prompt Icons](https://gofastmcp.com/v2/servers/icons#prompt-icons)
  * [Using Data URIs](https://gofastmcp.com/v2/servers/icons#using-data-uris)


Advanced Features
# Icons
Copy page
Add visual icons to your servers, tools, resources, and prompts
Copy page
`2.13.0` Icons provide visual representations for your MCP servers and components, helping client applications present better user interfaces. When displayed in MCP clients, icons help users quickly identify and navigate your server’s capabilities.
##
[​](https://gofastmcp.com/v2/servers/icons#icon-format)
Icon Format
Icons use the standard MCP Icon type from the MCP protocol specification. Each icon specifies:
  * **src** : URL or data URI pointing to the icon image
  * **mimeType** (optional): MIME type of the image (e.g., “image/png”, “image/svg+xml”)
  * **sizes** (optional): Array of size descriptors (e.g., [“48x48”], [“any”])


Copy
```
from mcp.types import Icon

icon = Icon(
    src="https://example.com/icon.png",
    mimeType="image/png",
    sizes=["48x48"]
)

```

##
[​](https://gofastmcp.com/v2/servers/icons#server-icons)
Server Icons
Add icons and a website URL to your server for display in client applications:
Copy
```
from fastmcp import FastMCP
from mcp.types import Icon

mcp = FastMCP(
    name="WeatherService",
    website_url="https://weather.example.com",
    icons=[
        Icon(
            src="https://weather.example.com/icon-48.png",
            mimeType="image/png",
            sizes=["48x48"]
        ),
        Icon(
            src="https://weather.example.com/icon-96.png",
            mimeType="image/png",
            sizes=["96x96"]
        ),
    ]
)

```

Server icons appear in MCP client interfaces to help users identify your server among others they may have installed.
##
[​](https://gofastmcp.com/v2/servers/icons#component-icons)
Component Icons
Icons can be added to individual tools, resources, resource templates, and prompts:
###
[​](https://gofastmcp.com/v2/servers/icons#tool-icons)
Tool Icons
Copy
```
from mcp.types import Icon

@mcp.tool(
    icons=[Icon(src="https://example.com/calculator-icon.png")]
)
def calculate_sum(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

```

###
[​](https://gofastmcp.com/v2/servers/icons#resource-icons)
Resource Icons
Copy
```
@mcp.resource(
    "config://settings",
    icons=[Icon(src="https://example.com/config-icon.png")]
)
def get_settings() -> dict:
    """Retrieve application settings."""
    return {"theme": "dark", "language": "en"}

```

###
[​](https://gofastmcp.com/v2/servers/icons#resource-template-icons)
Resource Template Icons
Copy
```
@mcp.resource(
    "user://{user_id}/profile",
    icons=[Icon(src="https://example.com/user-icon.png")]
)
def get_user_profile(user_id: str) -> dict:
    """Get a user's profile."""
    return {"id": user_id, "name": f"User {user_id}"}

```

###
[​](https://gofastmcp.com/v2/servers/icons#prompt-icons)
Prompt Icons
Copy
```
@mcp.prompt(
    icons=[Icon(src="https://example.com/prompt-icon.png")]
)
def analyze_code(code: str):
    """Create a prompt for code analysis."""
    return f"Please analyze this code:\n\n{code}"

```

##
[​](https://gofastmcp.com/v2/servers/icons#using-data-uris)
Using Data URIs
For small icons or when you want to embed the icon directly, use data URIs:
Copy
```
from mcp.types import Icon
from fastmcp.utilities.types import Image

# SVG icon as data URI
svg_icon = Icon(
    src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCI+PHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6Ii8+PC9zdmc+",
    mimeType="image/svg+xml"
)

@mcp.tool(icons=[svg_icon])
def my_tool() -> str:
    """A tool with an embedded SVG icon."""
    return "result"

# Generating a data URI from a local image file.
img = Image(path="./assets/brand/favicon.png")
icon = Icon(src=img.to_data_uri())

@mcp.tool(icons=[icon])
def file_icon_tool() -> str:
    """A tool with an icon generated from a local file."""
    return "result"

```

[ User Elicitation Previous ](https://gofastmcp.com/v2/servers/elicitation)[ Client Logging Next ](https://gofastmcp.com/v2/servers/logging)
Ctrl+I
