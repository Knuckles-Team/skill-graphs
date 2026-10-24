[Skip to main content](https://gofastmcp.com/clients/roots#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Handlers
Client Roots
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
  * [Static Roots](https://gofastmcp.com/clients/roots#static-roots)
  * [Dynamic Roots](https://gofastmcp.com/clients/roots#dynamic-roots)


Handlers
# Client Roots
Copy page
Provide local context and resource boundaries to MCP servers.
Copy page
`2.0.0` Use this when you need to tell servers what local resources the client has access to. Roots inform servers about resources the client can provide. Servers can use this information to adjust behavior or provide more relevant responses.
##
[​](https://gofastmcp.com/clients/roots#static-roots)
Static Roots
Provide a list of roots when creating the client:
Copy
```
from fastmcp import Client

client = Client(
    "my_mcp_server.py",
    roots=["/path/to/root1", "/path/to/root2"]
)

```

##
[​](https://gofastmcp.com/clients/roots#dynamic-roots)
Dynamic Roots
Use a callback to compute roots dynamically when the server requests them:
Copy
```
from fastmcp import Client
from fastmcp.client.roots import RequestContext

async def roots_callback(context: RequestContext) -> list[str]:
    print(f"Server requested roots (Request ID: {context.request_id})")
    return ["/path/to/root1", "/path/to/root2"]

client = Client(
    "my_mcp_server.py",
    roots=roots_callback
)

```

[ Server Logging Previous ](https://gofastmcp.com/clients/logging)[ OAuth Authentication Next ](https://gofastmcp.com/clients/auth/oauth)
Ctrl+I
