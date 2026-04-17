[Skip to main content](https://gofastmcp.com/v2/integrations/workos#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authentication
WorkOS 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/v2/integrations/workos#configuration)
  * [Prerequisites](https://gofastmcp.com/v2/integrations/workos#prerequisites)
  * [Step 1: Create a WorkOS OAuth App](https://gofastmcp.com/v2/integrations/workos#step-1-create-a-workos-oauth-app)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/v2/integrations/workos#step-2-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/v2/integrations/workos#testing)
  * [Running the Server](https://gofastmcp.com/v2/integrations/workos#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/v2/integrations/workos#testing-with-a-client)
  * [Production Configuration](https://gofastmcp.com/v2/integrations/workos#production-configuration)
  * [Environment Variables](https://gofastmcp.com/v2/integrations/workos#environment-variables)
  * [Provider Selection](https://gofastmcp.com/v2/integrations/workos#provider-selection)
  * [WorkOS-Specific Configuration](https://gofastmcp.com/v2/integrations/workos#workos-specific-configuration)
  * [Configuration Options](https://gofastmcp.com/v2/integrations/workos#configuration-options)


Authentication
# WorkOS 🤝 FastMCP
Copy page
Authenticate FastMCP servers with WorkOS Connect
Copy page
`2.12.0` Secure your FastMCP server with WorkOS Connect authentication. This integration uses the OAuth Proxy pattern to handle authentication through WorkOS Connect while maintaining compatibility with MCP clients.
This guide covers WorkOS Connect applications. For Dynamic Client Registration (DCR) with AuthKit, see the [AuthKit integration](https://gofastmcp.com/v2/integrations/authkit) instead.
##
[​](https://gofastmcp.com/v2/integrations/workos#configuration)
Configuration
###
[​](https://gofastmcp.com/v2/integrations/workos#prerequisites)
Prerequisites
Before you begin, you will need:
  1. A
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/v2/integrations/workos#step-1-create-a-workos-oauth-app)
Step 1: Create a WorkOS OAuth App
Create an OAuth App in your WorkOS dashboard to get the credentials needed for authentication:
1
[](https://gofastmcp.com/v2/integrations/workos)
Create OAuth Application
In your WorkOS dashboard:
  1. Navigate to **Applications**
  2. Click **Create Application**
  3. Select **OAuth Application**
  4. Name your application


2
[](https://gofastmcp.com/v2/integrations/workos)
Get Credentials
In your OAuth application settings:
  1. Copy your **Client ID** (starts with `client_`)
  2. Click **Generate Client Secret** and save it securely
  3. Copy your **AuthKit Domain** (e.g., `https://your-app.authkit.app`)


3
[](https://gofastmcp.com/v2/integrations/workos)
Configure Redirect URI
In the **Redirect URIs** section:
  * Add: `http://localhost:8000/auth/callback` (for development)
  * For production, add your server’s public URL + `/auth/callback`


The callback URL must match exactly. The default path is `/auth/callback`, but you can customize it using the `redirect_path` parameter.
###
[​](https://gofastmcp.com/v2/integrations/workos#step-2-fastmcp-configuration)
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
[​](https://gofastmcp.com/v2/integrations/workos#testing)
Testing
###
[​](https://gofastmcp.com/v2/integrations/workos#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by WorkOS OAuth authentication.
###
[​](https://gofastmcp.com/v2/integrations/workos#testing-with-a-client)
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
[​](https://gofastmcp.com/v2/integrations/workos#production-configuration)
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

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/v2/servers/auth/oauth-proxy#configuration-parameters).
##
[​](https://gofastmcp.com/v2/integrations/workos#environment-variables)
Environment Variables
`2.12.1` For production deployments, use environment variables instead of hardcoding credentials.
###
[​](https://gofastmcp.com/v2/integrations/workos#provider-selection)
Provider Selection
Setting this environment variable allows the WorkOS provider to be used automatically without explicitly instantiating it in code.
[​](https://gofastmcp.com/v2/integrations/workos#param-fastmcp-server-auth)
FASTMCP_SERVER_AUTH
default:"Not set"
Set to `fastmcp.server.auth.providers.workos.WorkOSProvider` to use WorkOS authentication.
###
[​](https://gofastmcp.com/v2/integrations/workos#workos-specific-configuration)
WorkOS-Specific Configuration
These environment variables provide default values for the WorkOS provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.
[​](https://gofastmcp.com/v2/integrations/workos#param-fastmcp-server-auth-workos-client-id)
FASTMCP_SERVER_AUTH_WORKOS_CLIENT_ID
required
Your WorkOS OAuth App Client ID (e.g., `client_01K33Y6GGS7T3AWMPJWKW42Y3Q`)
[​](https://gofastmcp.com/v2/integrations/workos#param-fastmcp-server-auth-workos-client-secret)
FASTMCP_SERVER_AUTH_WORKOS_CLIENT_SECRET
required
Your WorkOS OAuth App Client Secret
[​](https://gofastmcp.com/v2/integrations/workos#param-fastmcp-server-auth-workos-authkit-domain)
FASTMCP_SERVER_AUTH_WORKOS_AUTHKIT_DOMAIN
required
Your WorkOS AuthKit domain (e.g., `https://your-app.authkit.app`)
[​](https://gofastmcp.com/v2/integrations/workos#param-fastmcp-server-auth-workos-base-url)
FASTMCP_SERVER_AUTH_WORKOS_BASE_URL
default:"http://localhost:8000"
Public URL where OAuth endpoints will be accessible (includes any mount path)
[​](https://gofastmcp.com/v2/integrations/workos#param-fastmcp-server-auth-workos-issuer-url)
FASTMCP_SERVER_AUTH_WORKOS_ISSUER_URL
default:"Uses BASE_URL"
Issuer URL for OAuth metadata (defaults to `BASE_URL`). Set to root-level URL when mounting under a path prefix to avoid 404 logs. See [HTTP Deployment guide](https://gofastmcp.com/v2/deployment/http#mounting-authenticated-servers) for details.
[​](https://gofastmcp.com/v2/integrations/workos#param-fastmcp-server-auth-workos-redirect-path)
FASTMCP_SERVER_AUTH_WORKOS_REDIRECT_PATH
default:"/auth/callback"
Redirect path configured in your WorkOS OAuth App
[​](https://gofastmcp.com/v2/integrations/workos#param-fastmcp-server-auth-workos-required-scopes)
FASTMCP_SERVER_AUTH_WORKOS_REQUIRED_SCOPES
default:"[]"
Comma-, space-, or JSON-separated list of required OAuth scopes (e.g., `openid profile email` or `["openid","profile","email"]`)
[​](https://gofastmcp.com/v2/integrations/workos#param-fastmcp-server-auth-workos-timeout-seconds)
FASTMCP_SERVER_AUTH_WORKOS_TIMEOUT_SECONDS
default:"10"
HTTP request timeout for WorkOS API calls
Example `.env` file:
Copy
```
# WorkOS OAuth credentials (always used as defaults)
FASTMCP_SERVER_AUTH_WORKOS_CLIENT_ID=client_01K33Y6GGS7T3AWMPJWKW42Y3Q
FASTMCP_SERVER_AUTH_WORKOS_CLIENT_SECRET=your_client_secret
FASTMCP_SERVER_AUTH_WORKOS_AUTHKIT_DOMAIN=https://your-app.authkit.app
FASTMCP_SERVER_AUTH_WORKOS_BASE_URL=https://your-server.com
FASTMCP_SERVER_AUTH_WORKOS_REQUIRED_SCOPES=["openid","profile","email"]

# Optional: Automatically provision WorkOS auth for all servers
FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.workos.WorkOSProvider

```

With environment variables set, you can either: **Option 1: Manual instantiation (env vars provide defaults)**
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import WorkOSProvider

# Env vars provide default values for WorkOSProvider()
auth = WorkOSProvider()  # Uses env var defaults
mcp = FastMCP(name="WorkOS Protected Server", auth=auth)

```

**Option 2: Automatic provisioning (requires FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.workos.WorkOSProvider)**
server.py
Copy
```
from fastmcp import FastMCP

# Auth is automatically provisioned from FASTMCP_SERVER_AUTH
mcp = FastMCP(name="WorkOS Protected Server")

```

##
[​](https://gofastmcp.com/v2/integrations/workos#configuration-options)
Configuration Options
[​](https://gofastmcp.com/v2/integrations/workos#param-client-id)
client_id
required
WorkOS OAuth application client ID
[​](https://gofastmcp.com/v2/integrations/workos#param-client-secret)
client_secret
required
WorkOS OAuth application client secret
[​](https://gofastmcp.com/v2/integrations/workos#param-authkit-domain)
authkit_domain
required
Your WorkOS AuthKit domain URL (e.g., `https://your-app.authkit.app`)
[​](https://gofastmcp.com/v2/integrations/workos#param-base-url)
base_url
required
Your FastMCP server’s public URL
[​](https://gofastmcp.com/v2/integrations/workos#param-required-scopes)
required_scopes
default:"[]"
OAuth scopes to request
[​](https://gofastmcp.com/v2/integrations/workos#param-redirect-path)
redirect_path
default:"/auth/callback"
OAuth callback path
[​](https://gofastmcp.com/v2/integrations/workos#param-timeout-seconds)
timeout_seconds
default:"10"
API request timeout
[ Supabase 🤝 FastMCP Previous ](https://gofastmcp.com/v2/integrations/supabase)[ Eunomia Authorization 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/eunomia-authorization)
Ctrl+I
