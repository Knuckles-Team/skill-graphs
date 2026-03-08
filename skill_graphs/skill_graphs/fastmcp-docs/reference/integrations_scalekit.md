[Skip to main content](https://gofastmcp.com/integrations/scalekit#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
Scalekit 🤝 FastMCP
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
  * [Prerequisites](https://gofastmcp.com/integrations/scalekit#prerequisites)
  * [Step 1: Configure MCP server in Scalekit environment](https://gofastmcp.com/integrations/scalekit#step-1-configure-mcp-server-in-scalekit-environment)
  * [Step 2: Add auth to FastMCP server](https://gofastmcp.com/integrations/scalekit#step-2-add-auth-to-fastmcp-server)
  * [Testing](https://gofastmcp.com/integrations/scalekit#testing)
  * [Start the MCP server](https://gofastmcp.com/integrations/scalekit#start-the-mcp-server)
  * [Production Configuration](https://gofastmcp.com/integrations/scalekit#production-configuration)
  * [Capabilities](https://gofastmcp.com/integrations/scalekit#capabilities)
  * [Debugging](https://gofastmcp.com/integrations/scalekit#debugging)
  * [Token inspection](https://gofastmcp.com/integrations/scalekit#token-inspection)


Auth
# Scalekit 🤝 FastMCP
Copy page
Secure your FastMCP server with Scalekit
Copy page
`2.13.0` Install auth stack to your FastMCP server with [Remote OAuth](https://gofastmcp.com/servers/auth/remote-oauth) pattern: Scalekit handles user authentication, and the MCP server validates issued tokens.
###
[​](https://gofastmcp.com/integrations/scalekit#prerequisites)
Prerequisites
Before you begin
  1. Get a **Environment URL** from _Dashboard > Settings_ .
  2. Have your FastMCP server’s base URL ready (can be localhost for development, e.g., `http://localhost:8000/`)


###
[​](https://gofastmcp.com/integrations/scalekit#step-1-configure-mcp-server-in-scalekit-environment)
Step 1: Configure MCP server in Scalekit environment
1
[](https://gofastmcp.com/integrations/scalekit)
Register MCP server and set environment
In your Scalekit dashboard:
  1. Open the **MCP Servers** section, then select **Create new server**
  2. Enter server details: a name, a resource identifier, and the desired MCP client authentication settings
  3. Save, then copy the **Resource ID** (for example, res_92015146095)

In your FastMCP project’s `.env`:
Copy
```
SCALEKIT_ENVIRONMENT_URL=<YOUR_APP_ENVIRONMENT_URL>
SCALEKIT_RESOURCE_ID=<YOUR_APP_RESOURCE_ID> # res_926EXAMPLE5878
BASE_URL=http://localhost:8000/
# Optional: additional scopes tokens must have
# SCALEKIT_REQUIRED_SCOPES=read,write

```

###
[​](https://gofastmcp.com/integrations/scalekit#step-2-add-auth-to-fastmcp-server)
Step 2: Add auth to FastMCP server
Create your FastMCP server file and use the ScalekitProvider to handle all the OAuth integration automatically:
> **Warning:** The legacy `mcp_url` and `client_id` parameters are deprecated and will be removed in a future release. Use `base_url` instead of `mcp_url` and remove `client_id` from your configuration.
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.scalekit import ScalekitProvider

# Discovers Scalekit endpoints and set up JWT token validation
auth_provider = ScalekitProvider(
    environment_url=SCALEKIT_ENVIRONMENT_URL,    # Scalekit environment URL
    resource_id=SCALEKIT_RESOURCE_ID,            # Resource server ID
    base_url=SERVER_URL,                         # Public MCP endpoint
    required_scopes=["read"],                    # Optional scope enforcement
)

# Create FastMCP server with auth
mcp = FastMCP(name="My Scalekit Protected Server", auth=auth_provider)

@mcp.tool
def auth_status() -> dict:
    """Show Scalekit authentication status."""
    # Extract user claims from the JWT
    return {
        "message": "This tool requires authentication via Scalekit",
        "authenticated": True,
        "provider": "Scalekit"
    }


```

Set `required_scopes` when you need tokens to carry specific permissions. Leave it unset to allow any token issued for the resource.
##
[​](https://gofastmcp.com/integrations/scalekit#testing)
Testing
###
[​](https://gofastmcp.com/integrations/scalekit#start-the-mcp-server)
Start the MCP server
Copy
```
uv run python server.py

```

Use any MCP client (for example, mcp-inspector, Claude, VS Code, or Windsurf) to connect to the running serve. Verify that authentication succeeds and requests are authorized as expected.
##
[​](https://gofastmcp.com/integrations/scalekit#production-configuration)
Production Configuration
For production deployments, load configuration from environment variables:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.scalekit import ScalekitProvider

# Load configuration from environment variables
auth = ScalekitProvider(
    environment_url=os.environ.get("SCALEKIT_ENVIRONMENT_URL"),
    resource_id=os.environ.get("SCALEKIT_RESOURCE_ID"),
    base_url=os.environ.get("BASE_URL", "https://your-server.com")
)

mcp = FastMCP(name="My Scalekit Protected Server", auth=auth)

@mcp.tool
def protected_action() -> str:
    """A tool that requires authentication."""
    return "Access granted via Scalekit!"

```

##
[​](https://gofastmcp.com/integrations/scalekit#capabilities)
Capabilities
Scalekit supports OAuth 2.1 with Dynamic Client Registration for MCP clients and enterprise SSO, and provides built‑in JWT validation and security controls. **OAuth 2.1/DCR** : clients self‑register, use PKCE, and work with the Remote OAuth pattern without pre‑provisioned credentials. **Validation and SSO** : tokens are verified (keys, RS256, issuer, audience, expiry), and SAML, OIDC, OAuth 2.0, ADFS, Azure AD, and Google Workspace are supported; use HTTPS in production and review auth logs as needed.
##
[​](https://gofastmcp.com/integrations/scalekit#debugging)
Debugging
Enable detailed logging to troubleshoot authentication issues:
Copy
```
import logging
logging.basicConfig(level=logging.DEBUG)

```

###
[​](https://gofastmcp.com/integrations/scalekit#token-inspection)
Token inspection
You can inspect JWT tokens in your tools to understand the user context:
Copy
```
from fastmcp.server.context import request_ctx
import jwt

@mcp.tool
def inspect_token() -> dict:
    """Inspect the current JWT token claims."""
    context = request_ctx.get()

    # Extract token from Authorization header
    if hasattr(context, 'request') and hasattr(context.request, 'headers'):
        auth_header = context.request.headers.get('authorization', '')
        if auth_header.startswith('Bearer '):
            token = auth_header[7:]
            # Decode without verification (already verified by provider)
            claims = jwt.decode(token, options={"verify_signature": False})
            return claims

    return {"error": "No token found"}

```

[ PropelAuth 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/propelauth)[ Supabase 🤝 FastMCP Next ](https://gofastmcp.com/integrations/supabase)
Ctrl+I
