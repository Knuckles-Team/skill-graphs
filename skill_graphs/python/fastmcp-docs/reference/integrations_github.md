[Skip to main content](https://gofastmcp.com/integrations/github#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
GitHub OAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/integrations/github#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/github#prerequisites)
  * [Step 1: Create a GitHub OAuth App](https://gofastmcp.com/integrations/github#step-1-create-a-github-oauth-app)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/integrations/github#step-2-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/integrations/github#testing)
  * [Running the Server](https://gofastmcp.com/integrations/github#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/integrations/github#testing-with-a-client)
  * [Production Configuration](https://gofastmcp.com/integrations/github#production-configuration)


Auth
# GitHub OAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with GitHub OAuth
Copy page
`2.12.0` This guide shows you how to secure your FastMCP server using **GitHub OAuth**. Since GitHub doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/servers/auth/oauth-proxy) pattern to bridge GitHub’s traditional OAuth with MCP’s authentication requirements.
##
[​](https://gofastmcp.com/integrations/github#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/github#prerequisites)
Prerequisites
Before you begin, you will need:
  1. A
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/integrations/github#step-1-create-a-github-oauth-app)
Step 1: Create a GitHub OAuth App
Create an OAuth App in your GitHub settings to get the credentials needed for authentication:
1
[](https://gofastmcp.com/integrations/github)
Navigate to OAuth Apps
Go to **Settings → Developer settings → OAuth Apps** in your GitHub account, or visit Click **“New OAuth App”** to create a new application.
2
[](https://gofastmcp.com/integrations/github)
Configure Your OAuth App
Fill in the application details:
  * **Application name** : Choose a name users will recognize (e.g., “My FastMCP Server”)
  * **Homepage URL** : Your application’s homepage or documentation URL
  * **Authorization callback URL** : Your server URL + `/auth/callback` (e.g., `http://localhost:8000/auth/callback`)


The callback URL must match exactly. The default path is `/auth/callback`, but you can customize it using the `redirect_path` parameter. For local development, GitHub allows `http://localhost` URLs. For production, you must use HTTPS.
If you want to use a custom callback path (e.g., `/auth/github/callback`), make sure to set the same path in both your GitHub OAuth App settings and the `redirect_path` parameter when configuring the GitHubProvider.
3
[](https://gofastmcp.com/integrations/github)
Save Your Credentials
After creating the app, you’ll see:
  * **Client ID** : A public identifier like `Ov23liAbcDefGhiJkLmN`
  * **Client Secret** : Click “Generate a new client secret” and save the value securely


Store these credentials securely. Never commit them to version control. Use environment variables or a secrets manager in production.
###
[​](https://gofastmcp.com/integrations/github#step-2-fastmcp-configuration)
Step 2: FastMCP Configuration
Create your FastMCP server using the `GitHubProvider`, which handles GitHub’s OAuth quirks automatically:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.github import GitHubProvider

# The GitHubProvider handles GitHub's token format and validation
auth_provider = GitHubProvider(
    client_id="Ov23liAbcDefGhiJkLmN",  # Your GitHub OAuth App Client ID
    client_secret="github_pat_...",     # Your GitHub OAuth App Client Secret
    base_url="http://localhost:8000",   # Must match your OAuth App configuration
    # redirect_path="/auth/callback"   # Default value, customize if needed
)

mcp = FastMCP(name="GitHub Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_user_info() -> dict:
    """Returns information about the authenticated GitHub user."""
    from fastmcp.server.dependencies import get_access_token

    token = get_access_token()
    # The GitHubProvider stores user data in token claims
    return {
        "github_user": token.claims.get("login"),
        "name": token.claims.get("name"),
        "email": token.claims.get("email")
    }

```

##
[​](https://gofastmcp.com/integrations/github#testing)
Testing
###
[​](https://gofastmcp.com/integrations/github#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by GitHub OAuth authentication.
###
[​](https://gofastmcp.com/integrations/github#testing-with-a-client)
Testing with a Client
Create a test client that authenticates with your GitHub-protected server:
test_client.py
Copy
```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle GitHub OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open GitHub login in your browser
        print("✓ Authenticated with GitHub!")

        # Test the protected tool
        result = await client.call_tool("get_user_info")
        print(f"GitHub user: {result['github_user']}")

if __name__ == "__main__":
    asyncio.run(main())

```

When you run the client for the first time:
  1. Your browser will open to GitHub’s authorization page
  2. After you authorize the app, you’ll be redirected back
  3. The client receives the token and can make authenticated requests


The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.
##
[​](https://gofastmcp.com/integrations/github#production-configuration)
Production Configuration
`2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key` and `client_storage`:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.github import GitHubProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth_provider = GitHubProvider(
    client_id="Ov23liAbcDefGhiJkLmN",
    client_secret="github_pat_...",
    base_url="https://your-production-domain.com",

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

mcp = FastMCP(name="Production GitHub App", auth=auth_provider)

```

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/servers/auth/oauth-proxy#configuration-parameters).
[ Eunomia Authorization 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/eunomia-authorization)[ Google OAuth 🤝 FastMCP Next ](https://gofastmcp.com/integrations/google)
Ctrl+I
