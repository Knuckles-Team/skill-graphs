[Skip to main content](https://gofastmcp.com/servers/providers/local#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Providers
Local Provider
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
    * [ Overview NEW ](https://gofastmcp.com/servers/providers/overview)
    * [ Local NEW ](https://gofastmcp.com/servers/providers/local)
    * [ Filesystem NEW ](https://gofastmcp.com/servers/providers/filesystem)
    * [MCP Proxy](https://gofastmcp.com/servers/providers/proxy)
    * [ Skills NEW ](https://gofastmcp.com/servers/providers/skills)
    * [ Custom NEW ](https://gofastmcp.com/servers/providers/custom)
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
  * [How It Works](https://gofastmcp.com/servers/providers/local#how-it-works)
  * [Component Registration](https://gofastmcp.com/servers/providers/local#component-registration)
  * [Using Decorators](https://gofastmcp.com/servers/providers/local#using-decorators)
  * [Using Direct Methods](https://gofastmcp.com/servers/providers/local#using-direct-methods)
  * [Removing Components](https://gofastmcp.com/servers/providers/local#removing-components)
  * [Duplicate Handling](https://gofastmcp.com/servers/providers/local#duplicate-handling)
  * [Component Visibility](https://gofastmcp.com/servers/providers/local#component-visibility)
  * [Standalone LocalProvider](https://gofastmcp.com/servers/providers/local#standalone-localprovider)


Providers
# Local Provider
Copy page
The default provider for decorator-registered components
Copy page
`3.0.0` `LocalProvider` stores components that you define directly on your server. When you use `@mcp.tool`, `@mcp.resource`, or `@mcp.prompt`, you’re adding components to your server’s `LocalProvider`.
##
[​](https://gofastmcp.com/servers/providers/local#how-it-works)
How It Works
Every FastMCP server has a `LocalProvider` as its first provider. Components registered via decorators or direct methods are stored here:
Copy
```
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

# These are stored in the server's `LocalProvider`
@mcp.tool
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

@mcp.resource("data://config")
def get_config() -> str:
    """Return configuration data."""
    return '{"version": "1.0"}'

@mcp.prompt
def analyze(topic: str) -> str:
    """Create an analysis prompt."""
    return f"Please analyze: {topic}"

```

The `LocalProvider` is always queried first when clients request components, ensuring that your directly-defined components take precedence over those from mounted or proxied servers.
##
[​](https://gofastmcp.com/servers/providers/local#component-registration)
Component Registration
###
[​](https://gofastmcp.com/servers/providers/local#using-decorators)
Using Decorators
The most common way to register components:
Copy
```
@mcp.tool
def my_tool(x: int) -> str:
    return str(x)

@mcp.resource("data://info")
def my_resource() -> str:
    return "info"

@mcp.prompt
def my_prompt(topic: str) -> str:
    return f"Discuss: {topic}"

```

###
[​](https://gofastmcp.com/servers/providers/local#using-direct-methods)
Using Direct Methods
You can also add pre-built component objects:
Copy
```
from fastmcp.tools import Tool

# Create a tool object
my_tool = Tool.from_function(some_function, name="custom_tool")

# Add it to the server
mcp.add_tool(my_tool)
mcp.add_resource(my_resource)
mcp.add_prompt(my_prompt)

```

###
[​](https://gofastmcp.com/servers/providers/local#removing-components)
Removing Components
Remove components by name or URI:
Copy
```
mcp.local_provider.remove_tool("my_tool")
mcp.local_provider.remove_resource("data://info")
mcp.local_provider.remove_prompt("my_prompt")

```

##
[​](https://gofastmcp.com/servers/providers/local#duplicate-handling)
Duplicate Handling
When you try to add a component that already exists, the behavior depends on the `on_duplicate` setting:
Mode | Behavior
---|---
`"error"` (default) | Raise `ValueError`
`"warn"` | Log warning and replace
`"replace"` | Silently replace
`"ignore"` | Keep existing component
Configure this when creating the server:
Copy
```
mcp = FastMCP("MyServer", on_duplicate="warn")

```

##
[​](https://gofastmcp.com/servers/providers/local#component-visibility)
Component Visibility
`3.0.0` Components can be dynamically enabled or disabled at runtime. Disabled components don’t appear in listings and can’t be called.
Copy
```
@mcp.tool(tags={"admin"})
def delete_all() -> str:
    """Delete everything."""
    return "Deleted"

@mcp.tool
def get_status() -> str:
    """Get system status."""
    return "OK"

# Disable admin tools
mcp.disable(tags={"admin"})

# Or only enable specific tools
mcp.enable(keys={"tool:get_status"}, only=True)

```

See [Visibility](https://gofastmcp.com/servers/visibility) for the full documentation on keys, tags, allowlist mode, and provider-level control.
##
[​](https://gofastmcp.com/servers/providers/local#standalone-localprovider)
Standalone LocalProvider
You can create a LocalProvider independently and attach it to multiple servers:
Copy
```
from fastmcp import FastMCP
from fastmcp.server.providers import LocalProvider

# Create a reusable provider
shared_tools = LocalProvider()

@shared_tools.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

@shared_tools.resource("data://version")
def get_version() -> str:
    return "1.0.0"

# Attach to multiple servers
server1 = FastMCP("Server1", providers=[shared_tools])
server2 = FastMCP("Server2", providers=[shared_tools])

```

This is useful for:
  * Sharing components across servers
  * Testing components in isolation
  * Building reusable component libraries

Standalone providers also support visibility control with `enable()` and `disable()`. See [Visibility](https://gofastmcp.com/servers/visibility) for details.
[ Providers Previous ](https://gofastmcp.com/servers/providers/overview)[ Filesystem Provider Next ](https://gofastmcp.com/servers/providers/filesystem)
Ctrl+I
