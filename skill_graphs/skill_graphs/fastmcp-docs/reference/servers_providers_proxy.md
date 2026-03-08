[Skip to main content](https://gofastmcp.com/servers/providers/proxy#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Providers
MCP Proxy Provider
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
  * [Why Use Proxy Provider](https://gofastmcp.com/servers/providers/proxy#why-use-proxy-provider)
  * [Quick Start](https://gofastmcp.com/servers/providers/proxy#quick-start)
  * [Transport Bridging](https://gofastmcp.com/servers/providers/proxy#transport-bridging)
  * [Session Isolation](https://gofastmcp.com/servers/providers/proxy#session-isolation)
  * [Shared Sessions](https://gofastmcp.com/servers/providers/proxy#shared-sessions)
  * [MCP Feature Forwarding](https://gofastmcp.com/servers/providers/proxy#mcp-feature-forwarding)
  * [Disabling Features](https://gofastmcp.com/servers/providers/proxy#disabling-features)
  * [Configuration-Based Proxies](https://gofastmcp.com/servers/providers/proxy#configuration-based-proxies)
  * [Multi-Server Proxies](https://gofastmcp.com/servers/providers/proxy#multi-server-proxies)
  * [Component Prefixing](https://gofastmcp.com/servers/providers/proxy#component-prefixing)
  * [Mirrored Components](https://gofastmcp.com/servers/providers/proxy#mirrored-components)
  * [Performance Considerations](https://gofastmcp.com/servers/providers/proxy#performance-considerations)
  * [Advanced Usage](https://gofastmcp.com/servers/providers/proxy#advanced-usage)
  * [FastMCPProxy Class](https://gofastmcp.com/servers/providers/proxy#fastmcpproxy-class)
  * [Adding Proxied Components to Existing Server](https://gofastmcp.com/servers/providers/proxy#adding-proxied-components-to-existing-server)


Providers
# MCP Proxy Provider
Copy page
Source components from other MCP servers
Copy page
`2.0.0` The Proxy Provider sources components from another MCP server through a client connection. This lets you expose any MCP server’s tools, resources, and prompts through your own server, whether the source is local or accessed over the network.
##
[​](https://gofastmcp.com/servers/providers/proxy#why-use-proxy-provider)
Why Use Proxy Provider
The Proxy Provider enables:
  * **Bridge transports** : Make an HTTP server available via stdio, or vice versa
  * **Aggregate servers** : Combine multiple source servers into one unified server
  * **Add security** : Act as a controlled gateway with authentication and authorization
  * **Simplify access** : Provide a stable endpoint even if backend servers change


Source ServerFastMCP ProxyYour ClientSource ServerFastMCP ProxyYour ClientMCP Request (stdio)MCP Request (HTTP/stdio/SSE)MCP ResponseMCP Response
##
[​](https://gofastmcp.com/servers/providers/proxy#quick-start)
Quick Start
`2.10.3` Create a proxy using `create_proxy()`:
Copy
```
from fastmcp.server import create_proxy

# create_proxy() accepts URLs, file paths, and transports directly
proxy = create_proxy("http://example.com/mcp", name="MyProxy")

if __name__ == "__main__":
    proxy.run()

```

This gives you:
  * Safe concurrent request handling
  * Automatic forwarding of MCP features (sampling, elicitation, etc.)
  * Session isolation to prevent context mixing


To mount a proxy inside another FastMCP server, see [Mounting External Servers](https://gofastmcp.com/servers/composition#mounting-external-servers).
##
[​](https://gofastmcp.com/servers/providers/proxy#transport-bridging)
Transport Bridging
A common use case is bridging transports between servers:
Copy
```
from fastmcp.server import create_proxy

# Bridge HTTP server to local stdio
http_proxy = create_proxy("http://example.com/mcp/sse", name="HTTP-to-stdio")

# Run locally via stdio for Claude Desktop
if __name__ == "__main__":
    http_proxy.run()  # Defaults to stdio

```

Or expose a local server via HTTP:
Copy
```
from fastmcp.server import create_proxy

# Bridge local server to HTTP
local_proxy = create_proxy("local_server.py", name="stdio-to-HTTP")

if __name__ == "__main__":
    local_proxy.run(transport="http", host="0.0.0.0", port=8080)

```

##
[​](https://gofastmcp.com/servers/providers/proxy#session-isolation)
Session Isolation
`2.10.3` `create_proxy()` provides session isolation - each request gets its own isolated backend session:
Copy
```
from fastmcp.server import create_proxy

# Each request creates a fresh backend session (recommended)
proxy = create_proxy("backend_server.py")

# Multiple clients can use this proxy simultaneously:
# - Client A calls a tool → gets isolated session
# - Client B calls a tool → gets different session
# - No context mixing

```

###
[​](https://gofastmcp.com/servers/providers/proxy#shared-sessions)
Shared Sessions
If you pass an already-connected client, the proxy reuses that session:
Copy
```
from fastmcp import Client
from fastmcp.server import create_proxy

async with Client("backend_server.py") as connected_client:
    # This proxy reuses the connected session
    proxy = create_proxy(connected_client)

    # ⚠️ Warning: All requests share the same session

```

Shared sessions may cause context mixing in concurrent scenarios. Use only in single-threaded situations or with explicit synchronization.
##
[​](https://gofastmcp.com/servers/providers/proxy#mcp-feature-forwarding)
MCP Feature Forwarding
`2.10.3` Proxies automatically forward MCP protocol features:
Feature | Description
---|---
Roots | Filesystem root access requests
Sampling | LLM completion requests
Elicitation | User input requests
Logging | Log messages from backend
Progress | Progress notifications
Copy
```
from fastmcp.server import create_proxy

# All features forwarded automatically
proxy = create_proxy("advanced_backend.py")

# When the backend:
# - Requests LLM sampling → forwarded to your client
# - Logs messages → appear in your client
# - Reports progress → shown in your client

```

###
[​](https://gofastmcp.com/servers/providers/proxy#disabling-features)
Disabling Features
Selectively disable forwarding:
Copy
```
from fastmcp.server.providers.proxy import ProxyClient

backend = ProxyClient(
    "backend_server.py",
    sampling_handler=None,  # Disable LLM sampling
    log_handler=None        # Disable log forwarding
)

```

##
[​](https://gofastmcp.com/servers/providers/proxy#configuration-based-proxies)
Configuration-Based Proxies
`2.4.0` Create proxies from configuration dictionaries:
Copy
```
from fastmcp.server import create_proxy

config = {
    "mcpServers": {
        "default": {
            "url": "https://example.com/mcp",
            "transport": "http"
        }
    }
}

proxy = create_proxy(config, name="Config-Based Proxy")

```

###
[​](https://gofastmcp.com/servers/providers/proxy#multi-server-proxies)
Multi-Server Proxies
Combine multiple servers with automatic namespacing:
Copy
```
from fastmcp.server import create_proxy

config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather-api.example.com/mcp",
            "transport": "http"
        },
        "calendar": {
            "url": "https://calendar-api.example.com/mcp",
            "transport": "http"
        }
    }
}

# Creates unified proxy with prefixed components:
# - weather_get_forecast
# - calendar_add_event
composite = create_proxy(config, name="Composite")

```

##
[​](https://gofastmcp.com/servers/providers/proxy#component-prefixing)
Component Prefixing
Proxied components follow standard prefixing rules:
Component Type | Pattern
---|---
Tools | `{prefix}_{tool_name}`
Prompts | `{prefix}_{prompt_name}`
Resources | `protocol://{prefix}/path`
Templates | `protocol://{prefix}/...`
##
[​](https://gofastmcp.com/servers/providers/proxy#mirrored-components)
Mirrored Components
`2.10.5` Components from a proxy server are “mirrored” - they reflect the remote server’s state and cannot be modified directly. To modify a proxied component (like disabling it), create a local copy:
Copy
```
from fastmcp import FastMCP
from fastmcp.server import create_proxy

proxy = create_proxy("backend_server.py")

# Get mirrored tool
mirrored_tool = await proxy.get_tool("useful_tool")

# Create modifiable local copy
local_tool = mirrored_tool.copy()

# Add to your own server
my_server = FastMCP("MyServer")
my_server.add_tool(local_tool)

# Now you can control enabled state
my_server.disable(keys={local_tool.key})

```

##
[​](https://gofastmcp.com/servers/providers/proxy#performance-considerations)
Performance Considerations
Proxying introduces network latency:
Operation | Local | Proxied (HTTP)
---|---|---
`list_tools()` | 1-2ms | 300-400ms
`call_tool()` | 1-2ms | 200-500ms
When mounting proxy servers, this latency affects all operations on the parent server. For low-latency requirements, consider caching strategies or limiting mounting depth.
##
[​](https://gofastmcp.com/servers/providers/proxy#advanced-usage)
Advanced Usage
###
[​](https://gofastmcp.com/servers/providers/proxy#fastmcpproxy-class)
FastMCPProxy Class
For explicit session control, use `FastMCPProxy` directly:
Copy
```
from fastmcp.server.providers.proxy import FastMCPProxy, ProxyClient

# Custom session factory
def create_client():
    return ProxyClient("backend_server.py")

proxy = FastMCPProxy(client_factory=create_client)

```

This gives you full control over session creation and reuse strategies.
###
[​](https://gofastmcp.com/servers/providers/proxy#adding-proxied-components-to-existing-server)
Adding Proxied Components to Existing Server
Mount a proxy to add components from another server:
Copy
```
from fastmcp import FastMCP
from fastmcp.server import create_proxy

server = FastMCP("My Server")

# Add local tools
@server.tool
def local_tool() -> str:
    return "Local result"

# Mount proxied tools from another server
external = create_proxy("http://external-server/mcp")
server.mount(external)

# Now server has both local and proxied tools

```

[ Filesystem Provider Previous ](https://gofastmcp.com/servers/providers/filesystem)[ Skills Provider Next ](https://gofastmcp.com/servers/providers/skills)
Ctrl+I
