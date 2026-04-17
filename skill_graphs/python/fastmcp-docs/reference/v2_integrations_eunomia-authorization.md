[Skip to main content](https://gofastmcp.com/v2/integrations/eunomia-authorization#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authorization
Eunomia Authorization 🤝 FastMCP
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
  * Authentication


##### Integrations
  * Authentication
  * Authorization
    * [Eunomia Auth](https://gofastmcp.com/v2/integrations/eunomia-authorization)
    * [Permit.io](https://gofastmcp.com/v2/integrations/permit)
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
  * [How it Works](https://gofastmcp.com/v2/integrations/eunomia-authorization#how-it-works)
  * [Listing Operations](https://gofastmcp.com/v2/integrations/eunomia-authorization#listing-operations)
  * [Execution Operations](https://gofastmcp.com/v2/integrations/eunomia-authorization#execution-operations)
  * [Add Authorization to Your Server](https://gofastmcp.com/v2/integrations/eunomia-authorization#add-authorization-to-your-server)
  * [Create a Server with Authorization](https://gofastmcp.com/v2/integrations/eunomia-authorization#create-a-server-with-authorization)
  * [Configure Access Policies](https://gofastmcp.com/v2/integrations/eunomia-authorization#configure-access-policies)
  * [Run the Server](https://gofastmcp.com/v2/integrations/eunomia-authorization#run-the-server)


Authorization
# Eunomia Authorization 🤝 FastMCP
Copy page
Add policy-based authorization to your FastMCP servers with Eunomia
Copy page
Add **policy-based authorization** to your FastMCP servers with one-line code addition with the  Control which tools, resources and prompts MCP clients can view and execute on your server. Define dynamic JSON-based policies and obtain a comprehensive audit log of all access attempts and violations.
##
[​](https://gofastmcp.com/v2/integrations/eunomia-authorization#how-it-works)
How it Works
Exploiting FastMCP’s [Middleware](https://gofastmcp.com/servers/middleware), the Eunomia middleware intercepts all MCP requests to your server and automatically maps MCP methods to authorization checks.
###
[​](https://gofastmcp.com/v2/integrations/eunomia-authorization#listing-operations)
Listing Operations
The middleware behaves as a filter for listing operations (`tools/list`, `resources/list`, `prompts/list`), hiding to the client components that are not authorized by the defined policies.
Eunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientEunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientMCP Listing Request (e.g., tools/list)MCP Listing RequestMCP Listing ResponseAuthorization ChecksAuthorization DecisionsFiltered MCP Listing Response
###
[​](https://gofastmcp.com/v2/integrations/eunomia-authorization#execution-operations)
Execution Operations
The middleware behaves as a firewall for execution operations (`tools/call`, `resources/read`, `prompts/get`), blocking operations that are not authorized by the defined policies.
Eunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientEunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientMCP Execution Request (e.g., tools/call)Authorization CheckAuthorization DecisionMCP Unauthorized Error (if denied)MCP Execution Request (if allowed)MCP Execution Response (if allowed)MCP Execution Response (if allowed)
##
[​](https://gofastmcp.com/v2/integrations/eunomia-authorization#add-authorization-to-your-server)
Add Authorization to Your Server
Eunomia is an AI-specific authorization server that handles policy decisions. The server runs embedded within your MCP server by default for a zero-effort configuration, but can alternatively be run remotely for centralized policy decisions.
###
[​](https://gofastmcp.com/v2/integrations/eunomia-authorization#create-a-server-with-authorization)
Create a Server with Authorization
First, install the `eunomia-mcp` package:
Copy
```
pip install eunomia-mcp

```

Then create a FastMCP server and add the Eunomia middleware in one line:
server.py
Copy
```
from fastmcp import FastMCP
from eunomia_mcp import create_eunomia_middleware

# Create your FastMCP server
mcp = FastMCP("Secure MCP Server 🔒")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add middleware to your server
middleware = create_eunomia_middleware(policy_file="mcp_policies.json")
mcp.add_middleware(middleware)

if __name__ == "__main__":
    mcp.run()

```

###
[​](https://gofastmcp.com/v2/integrations/eunomia-authorization#configure-access-policies)
Configure Access Policies
Use the `eunomia-mcp` CLI in your terminal to manage your authorization policies:
Copy
```
# Create a default policy file
eunomia-mcp init

# Or create a policy file customized for your FastMCP server
eunomia-mcp init --custom-mcp "app.server:mcp"

```

This creates `mcp_policies.json` file that you can further edit to your access control needs.
Copy
```
# Once edited, validate your policy file
eunomia-mcp validate mcp_policies.json

```

###
[​](https://gofastmcp.com/v2/integrations/eunomia-authorization#run-the-server)
Run the Server
Start your FastMCP server normally:
Copy
```
python server.py

```

The middleware will now intercept all MCP requests and check them against your policies. Requests include agent identification through headers like `X-Agent-ID`, `X-User-ID`, `User-Agent`, or `Authorization` and an automatic mapping of MCP methods to authorization resources and actions.
For detailed policy configuration, custom authentication, and remote deployments, visit the
[ WorkOS 🤝 FastMCP Previous ](https://gofastmcp.com/v2/integrations/workos)[ Permit.io Authorization 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/permit)
Ctrl+I
