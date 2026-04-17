[Skip to main content](https://gofastmcp.com/v2/integrations/descope#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authentication
Descope 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/v2/integrations/descope#configuration)
  * [Prerequisites](https://gofastmcp.com/v2/integrations/descope#prerequisites)
  * [Step 1: Configure Descope](https://gofastmcp.com/v2/integrations/descope#step-1-configure-descope)
  * [Step 2: Environment Setup](https://gofastmcp.com/v2/integrations/descope#step-2-environment-setup)
  * [Step 3: FastMCP Configuration](https://gofastmcp.com/v2/integrations/descope#step-3-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/v2/integrations/descope#testing)
  * [Environment Variables](https://gofastmcp.com/v2/integrations/descope#environment-variables)
  * [Provider Selection](https://gofastmcp.com/v2/integrations/descope#provider-selection)
  * [Descope-Specific Configuration](https://gofastmcp.com/v2/integrations/descope#descope-specific-configuration)


Authentication
# Descope 🤝 FastMCP
Copy page
Secure your FastMCP server with Descope
Copy page
`2.12.4` This guide shows you how to secure your FastMCP server using [**Remote OAuth**](https://gofastmcp.com/v2/servers/auth/remote-oauth) pattern, where Descope handles user login and your FastMCP server validates the tokens.
##
[​](https://gofastmcp.com/v2/integrations/descope#configuration)
Configuration
###
[​](https://gofastmcp.com/v2/integrations/descope#prerequisites)
Prerequisites
Before you begin, you will need:
  1. To
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:3000`)


###
[​](https://gofastmcp.com/v2/integrations/descope#step-1-configure-descope)
Step 1: Configure Descope
1
[](https://gofastmcp.com/v2/integrations/descope)
Create an MCP Server
  1. Go to the
  2. Give the MCP server a name and description.
  3. Ensure that **Dynamic Client Registration (DCR)** is enabled. Then click **Create**.
  4. Once you’ve created the MCP Server, note your Well-Known URL.


DCR is required for FastMCP clients to automatically register with your authentication server.
2
[](https://gofastmcp.com/v2/integrations/descope)
Note Your Well-Known URL
Save your Well-Known URL from
Copy
```
Well-Known URL: https://.../v1/apps/agentic/P.../M.../.well-known/openid-configuration

```

###
[​](https://gofastmcp.com/v2/integrations/descope#step-2-environment-setup)
Step 2: Environment Setup
Create a `.env` file with your Descope configuration:
Copy
```
DESCOPE_CONFIG_URL=https://.../v1/apps/agentic/P.../M.../.well-known/openid-configuration     # Your Descope Well-Known URL
SERVER_URL=http://localhost:3000     # Your server's base URL

```

###
[​](https://gofastmcp.com/v2/integrations/descope#step-3-fastmcp-configuration)
Step 3: FastMCP Configuration
Create your FastMCP server file and use the DescopeProvider to handle all the OAuth integration automatically:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.descope import DescopeProvider

# The DescopeProvider automatically discovers Descope endpoints
# and configures JWT token validation
auth_provider = DescopeProvider(
    config_url=https://.../.well-known/openid-configuration,        # Your MCP Server .well-known URL
    base_url=SERVER_URL,                  # Your server's public URL
)

# Create FastMCP server with auth
mcp = FastMCP(name="My Descope Protected Server", auth=auth_provider)


```

##
[​](https://gofastmcp.com/v2/integrations/descope#testing)
Testing
To test your server, you can use the `fastmcp` CLI to run it locally. Assuming you’ve saved the above code to `server.py` (after replacing the environment variables with your actual values!), you can run the following command:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Now, you can use a FastMCP client to test that you can reach your server after authenticating:
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
[​](https://gofastmcp.com/v2/integrations/descope#environment-variables)
Environment Variables
For production deployments, use environment variables instead of hardcoding credentials.
###
[​](https://gofastmcp.com/v2/integrations/descope#provider-selection)
Provider Selection
Setting this environment variable allows the Descope provider to be used automatically without explicitly instantiating it in code.
[​](https://gofastmcp.com/v2/integrations/descope#param-fastmcp-server-auth)
FASTMCP_SERVER_AUTH
default:"Not set"
Set to `fastmcp.server.auth.providers.descope.DescopeProvider` to use Descope authentication.
###
[​](https://gofastmcp.com/v2/integrations/descope#descope-specific-configuration)
Descope-Specific Configuration
These environment variables provide default values for the Descope provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.
[​](https://gofastmcp.com/v2/integrations/descope#param-fastmcp-server-auth-descopeprovider-config-url)
FASTMCP_SERVER_AUTH_DESCOPEPROVIDER_CONFIG_URL
required
Your Well-Known URL from the
[​](https://gofastmcp.com/v2/integrations/descope#param-fastmcp-server-auth-descopeprovider-base-url)
FASTMCP_SERVER_AUTH_DESCOPEPROVIDER_BASE_URL
required
Public URL of your FastMCP server (e.g., `https://your-server.com` or `http://localhost:8000` for development)
Example `.env` file:
Copy
```
# Use the Descope provider
FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.descope.DescopeProvider

# Descope configuration
FASTMCP_SERVER_AUTH_DESCOPEPROVIDER_CONFIG_URL=https://.../v1/apps/agentic/P.../M.../.well-known/openid-configuration
FASTMCP_SERVER_AUTH_DESCOPEPROVIDER_BASE_URL=https://your-server.com

```

With environment variables set, your server code simplifies to:
server.py
Copy
```
from fastmcp import FastMCP

# Authentication is automatically configured from environment
mcp = FastMCP(name="My Descope Protected Server")

```

[ Azure (Microsoft Entra ID) OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/v2/integrations/azure)[ Discord OAuth 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/discord)
Ctrl+I
