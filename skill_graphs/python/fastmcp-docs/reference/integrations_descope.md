[Skip to main content](https://gofastmcp.com/integrations/descope#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
Descope 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/integrations/descope#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/descope#prerequisites)
  * [Step 1: Configure Descope](https://gofastmcp.com/integrations/descope#step-1-configure-descope)
  * [Step 2: Environment Setup](https://gofastmcp.com/integrations/descope#step-2-environment-setup)
  * [Step 3: FastMCP Configuration](https://gofastmcp.com/integrations/descope#step-3-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/integrations/descope#testing)
  * [Production Configuration](https://gofastmcp.com/integrations/descope#production-configuration)


Auth
# Descope 🤝 FastMCP
Copy page
Secure your FastMCP server with Descope
Copy page
`2.12.4` This guide shows you how to secure your FastMCP server using [**Remote OAuth**](https://gofastmcp.com/servers/auth/remote-oauth) pattern, where Descope handles user login and your FastMCP server validates the tokens.
##
[​](https://gofastmcp.com/integrations/descope#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/descope#prerequisites)
Prerequisites
Before you begin, you will need:
  1. To
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:3000`)


###
[​](https://gofastmcp.com/integrations/descope#step-1-configure-descope)
Step 1: Configure Descope
1
[](https://gofastmcp.com/integrations/descope)
Create an MCP Server
  1. Go to the
  2. Give the MCP server a name and description.
  3. Ensure that **Dynamic Client Registration (DCR)** is enabled. Then click **Create**.
  4. Once you’ve created the MCP Server, note your Well-Known URL.


DCR is required for FastMCP clients to automatically register with your authentication server.
2
[](https://gofastmcp.com/integrations/descope)
Note Your Well-Known URL
Save your Well-Known URL from
Copy
```
Well-Known URL: https://.../v1/apps/agentic/P.../M.../.well-known/openid-configuration

```

###
[​](https://gofastmcp.com/integrations/descope#step-2-environment-setup)
Step 2: Environment Setup
Create a `.env` file with your Descope configuration:
Copy
```
DESCOPE_CONFIG_URL=https://.../v1/apps/agentic/P.../M.../.well-known/openid-configuration     # Your Descope Well-Known URL
SERVER_URL=http://localhost:3000     # Your server's base URL

```

###
[​](https://gofastmcp.com/integrations/descope#step-3-fastmcp-configuration)
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
[​](https://gofastmcp.com/integrations/descope#testing)
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
[​](https://gofastmcp.com/integrations/descope#production-configuration)
Production Configuration
For production deployments, load configuration from environment variables:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.descope import DescopeProvider

# Load configuration from environment variables
auth = DescopeProvider(
    config_url=os.environ.get("DESCOPE_CONFIG_URL"),
    base_url=os.environ.get("BASE_URL", "https://your-server.com")
)

mcp = FastMCP(name="My Descope Protected Server", auth=auth)

```

[ Azure (Microsoft Entra ID) OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/azure)[ Discord OAuth 🤝 FastMCP Next ](https://gofastmcp.com/integrations/discord)
Ctrl+I
