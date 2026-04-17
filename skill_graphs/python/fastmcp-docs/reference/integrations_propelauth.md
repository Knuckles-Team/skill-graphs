[Skip to main content](https://gofastmcp.com/integrations/propelauth#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
PropelAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/integrations/propelauth#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/propelauth#prerequisites)
  * [Step 1: Configure PropelAuth](https://gofastmcp.com/integrations/propelauth#step-1-configure-propelauth)
  * [Step 2: Environment Setup](https://gofastmcp.com/integrations/propelauth#step-2-environment-setup)
  * [Step 3: FastMCP Configuration](https://gofastmcp.com/integrations/propelauth#step-3-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/integrations/propelauth#testing)
  * [Accessing User Information](https://gofastmcp.com/integrations/propelauth#accessing-user-information)
  * [Advanced Configuration](https://gofastmcp.com/integrations/propelauth#advanced-configuration)


Auth
# PropelAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with PropelAuth
Copy page
`3.1.0` This guide shows you how to secure your FastMCP server using [**Remote OAuth**](https://gofastmcp.com/servers/auth/remote-oauth) pattern, where PropelAuth handles user login, consent management, and your FastMCP server validates the tokens.
##
[​](https://gofastmcp.com/integrations/propelauth#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/propelauth#prerequisites)
Prerequisites
Before you begin, you will need:
  1. A
  2. Your FastMCP server’s base URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/integrations/propelauth#step-1-configure-propelauth)
Step 1: Configure PropelAuth
1
[](https://gofastmcp.com/integrations/propelauth)
Enable MCP Authentication
Navigate to the **MCP** section in your PropelAuth dashboard, click **Enable MCP** , and choose which environments to enable it for (Test, Staging, Prod).
2
[](https://gofastmcp.com/integrations/propelauth)
Configure Allowed MCP Clients
Under **MCP > Allowed MCP Clients**, add redirect URIs for each MCP client you want to allow. PropelAuth provides templates for popular clients like Claude, Cursor, and ChatGPT.
3
[](https://gofastmcp.com/integrations/propelauth)
Configure Scopes
Under **MCP > Scopes**, define the permissions available to MCP clients (e.g., `read:user_data`).
4
[](https://gofastmcp.com/integrations/propelauth)
Choose How Users Create OAuth Clients
Under **MCP > Settings > How Do Users Create OAuth Clients?**, you can optionally enable:
  * **Dynamic Client Registration** — clients self-register automatically via the DCR protocol
  * **Manually via Hosted Pages** — PropelAuth creates a UI for your users to register OAuth clients

You can enable neither, one, or both. If you enable neither, you’ll manage OAuth client creation yourself.
5
[](https://gofastmcp.com/integrations/propelauth)
Generate Introspection Credentials
Go to **MCP > Request Validation** and click **Create Credentials**. Note the **Client ID** and **Client Secret** - you’ll need these to validate tokens.
6
[](https://gofastmcp.com/integrations/propelauth)
Note Your Auth URL
Find your Auth URL in the **Backend Integration** section of the dashboard (e.g., `https://auth.yourdomain.com`).
For more details, see the
###
[​](https://gofastmcp.com/integrations/propelauth#step-2-environment-setup)
Step 2: Environment Setup
Create a `.env` file with your PropelAuth configuration:
Copy
```
PROPELAUTH_AUTH_URL=https://auth.yourdomain.com          # From Backend Integration page
PROPELAUTH_INTROSPECTION_CLIENT_ID=your-client-id        # From MCP > Request Validation
PROPELAUTH_INTROSPECTION_CLIENT_SECRET=your-client-secret # From MCP > Request Validation
SERVER_URL=http://localhost:8000                          # Your server's base URL

```

###
[​](https://gofastmcp.com/integrations/propelauth#step-3-fastmcp-configuration)
Step 3: FastMCP Configuration
Create your FastMCP server file and use the PropelAuthProvider to handle all the OAuth integration automatically:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.propelauth import PropelAuthProvider

auth_provider = PropelAuthProvider(
    auth_url=os.environ["PROPELAUTH_AUTH_URL"],
    introspection_client_id=os.environ["PROPELAUTH_INTROSPECTION_CLIENT_ID"],
    introspection_client_secret=os.environ["PROPELAUTH_INTROSPECTION_CLIENT_SECRET"],
    base_url=os.environ["SERVER_URL"],
    required_scopes=["read:user_data"],                          # Optional scope enforcement
)

mcp = FastMCP(name="My PropelAuth Protected Server", auth=auth_provider)

```

##
[​](https://gofastmcp.com/integrations/propelauth#testing)
Testing
With your `.env` loaded, start the server:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Then use a FastMCP client to verify authentication works:
Copy
```
from fastmcp import Client
import asyncio

async def main():
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        assert await client.ping()

if __name__ == "__main__":
    asyncio.run(main())

```

##
[​](https://gofastmcp.com/integrations/propelauth#accessing-user-information)
Accessing User Information
You can use `get_access_token()` inside your tools to identify the authenticated user:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.propelauth import PropelAuthProvider
from fastmcp.server.dependencies import get_access_token

auth = PropelAuthProvider(
    auth_url=os.environ["PROPELAUTH_AUTH_URL"],
    introspection_client_id=os.environ["PROPELAUTH_INTROSPECTION_CLIENT_ID"],
    introspection_client_secret=os.environ["PROPELAUTH_INTROSPECTION_CLIENT_SECRET"],
    base_url=os.environ["SERVER_URL"],
    required_scopes=["read:user_data"],
)

mcp = FastMCP(name="My PropelAuth Protected Server", auth=auth)

@mcp.tool
def whoami() -> dict:
    """Return the authenticated user's ID."""
    token = get_access_token()
    if token is None:
        return {"error": "Not authenticated"}
    user_id = token.claims.get("sub")
    return {"user_id": user_id}

```

##
[​](https://gofastmcp.com/integrations/propelauth#advanced-configuration)
Advanced Configuration
The `PropelAuthProvider` supports optional overrides for token introspection behavior, including caching and request timeouts:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.propelauth import PropelAuthProvider

auth = PropelAuthProvider(
    auth_url=os.environ["PROPELAUTH_AUTH_URL"],
    introspection_client_id=os.environ["PROPELAUTH_INTROSPECTION_CLIENT_ID"],
    introspection_client_secret=os.environ["PROPELAUTH_INTROSPECTION_CLIENT_SECRET"],
    base_url=os.environ.get("BASE_URL", "https://your-server.com"),
    required_scopes=["read:user_data"],
    resource="https://your-server.com/mcp",              # Restrict to tokens intended for this server (RFC 8707)
    token_introspection_overrides={
        "cache_ttl_seconds": 300,       # Cache introspection results for 5 minutes
        "max_cache_size": 1000,         # Maximum cached tokens
        "timeout_seconds": 15,          # HTTP request timeout
    },
)

mcp = FastMCP(name="My PropelAuth Protected Server", auth=auth)

```

[ Permit.io Authorization 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/permit)[ Scalekit 🤝 FastMCP Next ](https://gofastmcp.com/integrations/scalekit)
Ctrl+I
