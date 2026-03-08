[Skip to main content](https://gofastmcp.com/integrations/workos#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
WorkOS 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/integrations/workos#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/workos#prerequisites)
  * [Step 1: Create a WorkOS OAuth App](https://gofastmcp.com/integrations/workos#step-1-create-a-workos-oauth-app)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/integrations/workos#step-2-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/integrations/workos#testing)
  * [Running the Server](https://gofastmcp.com/integrations/workos#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/integrations/workos#testing-with-a-client)
  * [Production Configuration](https://gofastmcp.com/integrations/workos#production-configuration)
  * [Configuration Options](https://gofastmcp.com/integrations/workos#configuration-options)


Auth
# WorkOS 🤝 FastMCP
Copy page
Authenticate FastMCP servers with WorkOS Connect
Copy page
`2.12.0` Secure your FastMCP server with WorkOS Connect authentication. This integration uses the OAuth Proxy pattern to handle authentication through WorkOS Connect while maintaining compatibility with MCP clients.
This guide covers WorkOS Connect applications. For Dynamic Client Registration (DCR) with AuthKit, see the [AuthKit integration](https://gofastmcp.com/integrations/authkit) instead.
##
[​](https://gofastmcp.com/integrations/workos#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/workos#prerequisites)
Prerequisites
Before you begin, you will need:
  1. A
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/integrations/workos#step-1-create-a-workos-oauth-app)
Step 1: Create a WorkOS OAuth App
Create an OAuth App in your WorkOS dashboard to get the credentials needed for authentication:
1
[](https://gofastmcp.com/integrations/workos)
Create OAuth Application
In your WorkOS dashboard:
  1. Navigate to **Applications**
  2. Click **Create Application**
  3. Select **OAuth Application**
  4. Name your application


2
[](https://gofastmcp.com/integrations/workos)
Get Credentials
In your OAuth application settings:
  1. Copy your **Client ID** (starts with `client_`)
  2. Click **Generate Client Secret** and save it securely
  3. Copy your **AuthKit Domain** (e.g., `https://your-app.authkit.app`)


3
[](https://gofastmcp.com/integrations/workos)
Configure Redirect URI
In the **Redirect URIs** section:
  * Add: `http://localhost:8000/auth/callback` (for development)
  * For production, add your server’s public URL + `/auth/callback`


The callback URL must match exactly. The default path is `/auth/callback`, but you can customize it using the `redirect_path` parameter.
###
[​](https://gofastmcp.com/integrations/workos#step-2-fastmcp-configuration)
Step 2: FastMCP Configuration
Create your FastMCP server using the `WorkOSProvider`:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import WorkOSProvider

# Configure WorkOS OAuth
auth = WorkOSProvider(
    client_id="client_YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    authkit_domain="https://your-app.authkit.app",
    base_url="http://localhost:8000",
    required_scopes=["openid", "profile", "email"]
)

mcp = FastMCP("WorkOS Protected Server", auth=auth)

@mcp.tool
def protected_tool(message: str) -> str:
    """This tool requires authentication."""
    return f"Authenticated user says: {message}"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)

```

##
[​](https://gofastmcp.com/integrations/workos#testing)
Testing
###
[​](https://gofastmcp.com/integrations/workos#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by WorkOS OAuth authentication.
###
[​](https://gofastmcp.com/integrations/workos#testing-with-a-client)
Testing with a Client
Create a test client that authenticates with your WorkOS-protected server:
client.py
Copy
```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle WorkOS OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open WorkOS login in your browser
        print("✓ Authenticated with WorkOS!")

        # Test the protected tool
        result = await client.call_tool("protected_tool", {"message": "Hello!"})
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

```

When you run the client for the first time:
  1. Your browser will open to WorkOS’s authorization page
  2. After you authorize the app, you’ll be redirected back
  3. The client receives the token and can make authenticated requests


The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.
##
[​](https://gofastmcp.com/integrations/workos#production-configuration)
Production Configuration
`2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key`, and `client_storage`:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import WorkOSProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth = WorkOSProvider(
    client_id="client_YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    authkit_domain="https://your-app.authkit.app",
    base_url="https://your-production-domain.com",
    required_scopes=["openid", "profile", "email"],

    # Production token management
    jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
    client_storage=FernetEncryptionWrapper(
        key_value=RedisStore(
            host=os.environ["REDIS_HOST"],
            port=int(os.environ["REDIS_PORT"])
        ),
        fernet=Fernet(os.environ["STORAGE_ENCRYPTION_KEY"])
    )
)

mcp = FastMCP(name="Production WorkOS App", auth=auth)

```

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/servers/auth/oauth-proxy#configuration-parameters).
##
[​](https://gofastmcp.com/integrations/workos#configuration-options)
Configuration Options
[​](https://gofastmcp.com/integrations/workos#param-client-id)
client_id
required
WorkOS OAuth application client ID
[​](https://gofastmcp.com/integrations/workos#param-client-secret)
client_secret
required
WorkOS OAuth application client secret
[​](https://gofastmcp.com/integrations/workos#param-authkit-domain)
authkit_domain
required
Your WorkOS AuthKit domain URL (e.g., `https://your-app.authkit.app`)
[​](https://gofastmcp.com/integrations/workos#param-base-url)
base_url
required
Your FastMCP server’s public URL
[​](https://gofastmcp.com/integrations/workos#param-required-scopes)
required_scopes
default:"[]"
OAuth scopes to request
[​](https://gofastmcp.com/integrations/workos#param-redirect-path)
redirect_path
default:"/auth/callback"
OAuth callback path
[​](https://gofastmcp.com/integrations/workos#param-timeout-seconds)
timeout_seconds
default:"10"
API request timeout
[ Supabase 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/supabase)[ FastAPI 🤝 FastMCP Next ](https://gofastmcp.com/integrations/fastapi)
Ctrl+I
