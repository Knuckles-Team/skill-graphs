[Skip to main content](https://gofastmcp.com/integrations/eunomia-authorization#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
Eunomia Authorization 🤝 FastMCP
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
  * AuthenticationUPDATED


##### Integrations
  * Auth
    * [Auth0](https://gofastmcp.com/integrations/auth0)
    * [AuthKit](https://gofastmcp.com/integrations/authkit)
    * [AWS Cognito](https://gofastmcp.com/integrations/aws-cognito)
    * [Azure (Entra ID)](https://gofastmcp.com/integrations/azure)
    * [Descope](https://gofastmcp.com/integrations/descope)
    * [Discord](https://gofastmcp.com/integrations/discord)
    * [Eunomia Auth](https://gofastmcp.com/integrations/eunomia-authorization)
    * [GitHub](https://gofastmcp.com/integrations/github)
    * [Google](https://gofastmcp.com/integrations/google)
    * [Oracle](https://gofastmcp.com/integrations/oci)
    * [Permit.io](https://gofastmcp.com/integrations/permit)
    * [PropelAuth](https://gofastmcp.com/integrations/propelauth)
    * [Scalekit](https://gofastmcp.com/integrations/scalekit)
    * [Supabase](https://gofastmcp.com/integrations/supabase)
    * [WorkOS](https://gofastmcp.com/integrations/workos)
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
  * [How it Works](https://gofastmcp.com/integrations/eunomia-authorization#how-it-works)
  * [Listing Operations](https://gofastmcp.com/integrations/eunomia-authorization#listing-operations)
  * [Execution Operations](https://gofastmcp.com/integrations/eunomia-authorization#execution-operations)
  * [Add Authorization to Your Server](https://gofastmcp.com/integrations/eunomia-authorization#add-authorization-to-your-server)
  * [Create a Server with Authorization](https://gofastmcp.com/integrations/eunomia-authorization#create-a-server-with-authorization)
  * [Configure Access Policies](https://gofastmcp.com/integrations/eunomia-authorization#configure-access-policies)
  * [Run the Server](https://gofastmcp.com/integrations/eunomia-authorization#run-the-server)


Auth
# Eunomia Authorization 🤝 FastMCP
Copy page
Add policy-based authorization to your FastMCP servers with Eunomia
Copy page
Add **policy-based authorization** to your FastMCP servers with one-line code addition with the  Control which tools, resources and prompts MCP clients can view and execute on your server. Define dynamic JSON-based policies and obtain a comprehensive audit log of all access attempts and violations.
##
[​](https://gofastmcp.com/integrations/eunomia-authorization#how-it-works)
How it Works
Exploiting FastMCP’s [Middleware](https://gofastmcp.com/servers/middleware), the Eunomia middleware intercepts all MCP requests to your server and automatically maps MCP methods to authorization checks.
###
[​](https://gofastmcp.com/integrations/eunomia-authorization#listing-operations)
Listing Operations
The middleware behaves as a filter for listing operations (`tools/list`, `resources/list`, `prompts/list`), hiding to the client components that are not authorized by the defined policies.
Eunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientEunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientMCP Listing Request (e.g., tools/list)MCP Listing RequestMCP Listing ResponseAuthorization ChecksAuthorization DecisionsFiltered MCP Listing Response
###
[​](https://gofastmcp.com/integrations/eunomia-authorization#execution-operations)
Execution Operations
The middleware behaves as a firewall for execution operations (`tools/call`, `resources/read`, `prompts/get`), blocking operations that are not authorized by the defined policies.
Eunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientEunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientMCP Execution Request (e.g., tools/call)Authorization CheckAuthorization DecisionMCP Unauthorized Error (if denied)MCP Execution Request (if allowed)MCP Execution Response (if allowed)MCP Execution Response (if allowed)
##
[​](https://gofastmcp.com/integrations/eunomia-authorization#add-authorization-to-your-server)
Add Authorization to Your Server
Eunomia is an AI-specific authorization server that handles policy decisions. The server runs embedded within your MCP server by default for a zero-effort configuration, but can alternatively be run remotely for centralized policy decisions.
###
[​](https://gofastmcp.com/integrations/eunomia-authorization#create-a-server-with-authorization)
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
[​](https://gofastmcp.com/integrations/eunomia-authorization#configure-access-policies)
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
[​](https://gofastmcp.com/integrations/eunomia-authorization#run-the-server)
Run the Server
Start your FastMCP server normally:
Copy
```
python server.py

```

The middleware will now intercept all MCP requests and check them against your policies. Requests include agent identification through headers like `X-Agent-ID`, `X-User-ID`, `User-Agent`, or `Authorization` and an automatic mapping of MCP methods to authorization resources and actions.
For detailed policy configuration, custom authentication, and remote deployments, visit the
[ Discord OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/discord)[ GitHub OAuth 🤝 FastMCP Next ](https://gofastmcp.com/integrations/github)
Ctrl+I
