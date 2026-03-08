[Skip to main content](https://gofastmcp.com/v2/integrations/scalekit#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authentication
Scalekit 🤝 FastMCP
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
    * [ Auth0 NEW ](https://gofastmcp.com/v2/integrations/auth0)
    * [ AuthKit NEW ](https://gofastmcp.com/v2/integrations/authkit)
    * [ AWS Cognito NEW ](https://gofastmcp.com/v2/integrations/aws-cognito)
    * [ Azure (Entra ID) NEW ](https://gofastmcp.com/v2/integrations/azure)
    * [ Descope NEW ](https://gofastmcp.com/v2/integrations/descope)
    * [ Discord NEW ](https://gofastmcp.com/v2/integrations/discord)
    * [ GitHub NEW ](https://gofastmcp.com/v2/integrations/github)
    * [ Google NEW ](https://gofastmcp.com/v2/integrations/google)
    * [ Oracle NEW ](https://gofastmcp.com/v2/integrations/oci)
    * [ Scalekit NEW ](https://gofastmcp.com/v2/integrations/scalekit)
    * [ Supabase NEW ](https://gofastmcp.com/v2/integrations/supabase)
    * [ WorkOS NEW ](https://gofastmcp.com/v2/integrations/workos)
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
  * [Prerequisites](https://gofastmcp.com/v2/integrations/scalekit#prerequisites)
  * [Step 1: Configure MCP server in Scalekit environment](https://gofastmcp.com/v2/integrations/scalekit#step-1-configure-mcp-server-in-scalekit-environment)
  * [Step 2: Add auth to FastMCP server](https://gofastmcp.com/v2/integrations/scalekit#step-2-add-auth-to-fastmcp-server)
  * [Testing](https://gofastmcp.com/v2/integrations/scalekit#testing)
  * [Start the MCP server](https://gofastmcp.com/v2/integrations/scalekit#start-the-mcp-server)
  * [Provider selection](https://gofastmcp.com/v2/integrations/scalekit#provider-selection)
  * [Scalekit-specific configuration](https://gofastmcp.com/v2/integrations/scalekit#scalekit-specific-configuration)
  * [Capabilities](https://gofastmcp.com/v2/integrations/scalekit#capabilities)
  * [Debugging](https://gofastmcp.com/v2/integrations/scalekit#debugging)
  * [Token inspection](https://gofastmcp.com/v2/integrations/scalekit#token-inspection)


Authentication
# Scalekit 🤝 FastMCP
Copy page
Secure your FastMCP server with Scalekit
Copy page
`2.13.0` Install auth stack to your FastMCP server with [Remote OAuth](https://gofastmcp.com/v2/servers/auth/remote-oauth) pattern: Scalekit handles user authentication, and the MCP server validates issued tokens.
###
[​](https://gofastmcp.com/v2/integrations/scalekit#prerequisites)
Prerequisites
Before you begin
  1. Get a **Environment URL** from _Dashboard > Settings_ .
  2. Have your FastMCP server’s base URL ready (can be localhost for development, e.g., `http://localhost:8000/`)


###
[​](https://gofastmcp.com/v2/integrations/scalekit#step-1-configure-mcp-server-in-scalekit-environment)
Step 1: Configure MCP server in Scalekit environment
1
[](https://gofastmcp.com/v2/integrations/scalekit)
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
[​](https://gofastmcp.com/v2/integrations/scalekit#step-2-add-auth-to-fastmcp-server)
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
[​](https://gofastmcp.com/v2/integrations/scalekit#testing)
Testing
###
[​](https://gofastmcp.com/v2/integrations/scalekit#start-the-mcp-server)
Start the MCP server
Copy
```
uv run python server.py

```

Use any MCP client (for example, mcp-inspector, Claude, VS Code, or Windsurf) to connect to the running serve. Verify that authentication succeeds and requests are authorized as expected.
###
[​](https://gofastmcp.com/v2/integrations/scalekit#provider-selection)
Provider selection
Setting this environment variable allows the Scalekit provider to be used automatically without explicitly instantiating it in code.
[​](https://gofastmcp.com/v2/integrations/scalekit#param-fastmcp-server-auth)
FASTMCP_SERVER_AUTH
default:"Not set"
Set to `fastmcp.server.auth.providers.scalekit.ScalekitProvider` to use Scalekit authentication.
###
[​](https://gofastmcp.com/v2/integrations/scalekit#scalekit-specific-configuration)
Scalekit-specific configuration
These environment variables provide default values for the Scalekit provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.
[​](https://gofastmcp.com/v2/integrations/scalekit#param-fastmcp-server-auth-scalekitprovider-environment-url)
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_ENVIRONMENT_URL
required
Your Scalekit environment URL from the Admin Portal (e.g., `https://your-env.scalekit.com`)
[​](https://gofastmcp.com/v2/integrations/scalekit#param-fastmcp-server-auth-scalekitprovider-resource-id)
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_RESOURCE_ID
required
Your Scalekit resource server ID from the MCP Servers section
[​](https://gofastmcp.com/v2/integrations/scalekit#param-fastmcp-server-auth-scalekitprovider-base-url)
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_BASE_URL
required
Public URL of your FastMCP server (e.g., `https://your-server.com` or `http://localhost:8000/` for development)
Legacy `FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_MCP_URL` is still recognized for backward compatibility but will be removed soon-rename it to `...BASE_URL`.
[​](https://gofastmcp.com/v2/integrations/scalekit#param-fastmcp-server-auth-scalekitprovider-required-scopes)
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_REQUIRED_SCOPES
default:"[]"
Comma-, space-, or JSON-separated list of scopes that tokens must include to access your server
Example `.env`:
Copy
```
# Use the Scalekit provider
FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.scalekit.ScalekitProvider

# Scalekit configuration
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_ENVIRONMENT_URL=https://your-env.scalekit.com
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_RESOURCE_ID=res_456
FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_BASE_URL=https://your-server.com/
# FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_REQUIRED_SCOPES=read,write
# FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_MCP_URL=https://your-server.com/  # Deprecated

```

With environment variables set, your server code simplifies to:
server.py
Copy
```
from fastmcp import FastMCP

# Authentication is automatically configured from environment
mcp = FastMCP(name="My Scalekit Protected Server")

@mcp.tool
def protected_action() -> str:
    """A tool that requires authentication."""
    return "Access granted via Scalekit!"

```

##
[​](https://gofastmcp.com/v2/integrations/scalekit#capabilities)
Capabilities
Scalekit supports OAuth 2.1 with Dynamic Client Registration for MCP clients and enterprise SSO, and provides built‑in JWT validation and security controls. **OAuth 2.1/DCR** : clients self‑register, use PKCE, and work with the Remote OAuth pattern without pre‑provisioned credentials. **Validation and SSO** : tokens are verified (keys, RS256, issuer, audience, expiry), and SAML, OIDC, OAuth 2.0, ADFS, Azure AD, and Google Workspace are supported; use HTTPS in production and review auth logs as needed.
##
[​](https://gofastmcp.com/v2/integrations/scalekit#debugging)
Debugging
Enable detailed logging to troubleshoot authentication issues:
Copy
```
import logging
logging.basicConfig(level=logging.DEBUG)

```

###
[​](https://gofastmcp.com/v2/integrations/scalekit#token-inspection)
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

[ OCI IAM OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/v2/integrations/oci)[ Supabase 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/supabase)
Ctrl+I
