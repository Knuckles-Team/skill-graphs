[Skip to main content](https://gofastmcp.com/integrations/google#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
Google OAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/integrations/google#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/google#prerequisites)
  * [Step 1: Create a Google OAuth 2.0 Client ID](https://gofastmcp.com/integrations/google#step-1-create-a-google-oauth-2-0-client-id)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/integrations/google#step-2-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/integrations/google#testing)
  * [Running the Server](https://gofastmcp.com/integrations/google#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/integrations/google#testing-with-a-client)
  * [Production Configuration](https://gofastmcp.com/integrations/google#production-configuration)


Auth
# Google OAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with Google OAuth
Copy page
`2.12.0` This guide shows you how to secure your FastMCP server using **Google OAuth**. Since Google doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/servers/auth/oauth-proxy) pattern to bridge Google’s traditional OAuth with MCP’s authentication requirements.
##
[​](https://gofastmcp.com/integrations/google#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/google#prerequisites)
Prerequisites
Before you begin, you will need:
  1. A
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/integrations/google#step-1-create-a-google-oauth-2-0-client-id)
Step 1: Create a Google OAuth 2.0 Client ID
Create an OAuth 2.0 Client ID in your Google Cloud Console to get the credentials needed for authentication:
1
[](https://gofastmcp.com/integrations/google)
Navigate to OAuth Consent Screen
Go to the First, configure the OAuth consent screen by navigating to **APIs & Services → OAuth consent screen**. Choose “External” for testing or “Internal” for G Suite organizations.
2
[](https://gofastmcp.com/integrations/google)
Create OAuth 2.0 Client ID
Navigate to **APIs & Services → Credentials** and click **”+ CREATE CREDENTIALS”** → **“OAuth client ID”**.Configure your OAuth client:
  * **Application type** : Web application
  * **Name** : Choose a descriptive name (e.g., “FastMCP Server”)
  * **Authorized JavaScript origins** : Add your server’s base URL (e.g., `http://localhost:8000`)
  * **Authorized redirect URIs** : Add your server URL + `/auth/callback` (e.g., `http://localhost:8000/auth/callback`)


The redirect URI must match exactly. The default path is `/auth/callback`, but you can customize it using the `redirect_path` parameter. For local development, Google allows `http://localhost` URLs with various ports. For production, you must use HTTPS.
If you want to use a custom callback path (e.g., `/auth/google/callback`), make sure to set the same path in both your Google OAuth Client settings and the `redirect_path` parameter when configuring the GoogleProvider.
3
[](https://gofastmcp.com/integrations/google)
Save Your Credentials
After creating the client, you’ll receive:
  * **Client ID** : A string ending in `.apps.googleusercontent.com`
  * **Client Secret** : A string starting with `GOCSPX-`

Download the JSON credentials or copy these values securely.
Store these credentials securely. Never commit them to version control. Use environment variables or a secrets manager in production.
###
[​](https://gofastmcp.com/integrations/google#step-2-fastmcp-configuration)
Step 2: FastMCP Configuration
Create your FastMCP server using the `GoogleProvider`, which handles Google’s OAuth flow automatically:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.google import GoogleProvider

# The GoogleProvider handles Google's token format and validation
auth_provider = GoogleProvider(
    client_id="123456789.apps.googleusercontent.com",  # Your Google OAuth Client ID
    client_secret="GOCSPX-abc123...",                  # Your Google OAuth Client Secret
    base_url="http://localhost:8000",                  # Must match your OAuth configuration
    required_scopes=[                                  # Request user information
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
    ],
    # redirect_path="/auth/callback"                  # Default value, customize if needed
)

mcp = FastMCP(name="Google Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_user_info() -> dict:
    """Returns information about the authenticated Google user."""
    from fastmcp.server.dependencies import get_access_token

    token = get_access_token()
    # The GoogleProvider stores user data in token claims
    return {
        "google_id": token.claims.get("sub"),
        "email": token.claims.get("email"),
        "name": token.claims.get("name"),
        "picture": token.claims.get("picture"),
        "locale": token.claims.get("locale")
    }

```

##
[​](https://gofastmcp.com/integrations/google#testing)
Testing
###
[​](https://gofastmcp.com/integrations/google#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by Google OAuth authentication.
###
[​](https://gofastmcp.com/integrations/google#testing-with-a-client)
Testing with a Client
Create a test client that authenticates with your Google-protected server:
test_client.py
Copy
```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle Google OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open Google login in your browser
        print("✓ Authenticated with Google!")

        # Test the protected tool
        result = await client.call_tool("get_user_info")
        print(f"Google user: {result['email']}")
        print(f"Name: {result['name']}")

if __name__ == "__main__":
    asyncio.run(main())

```

When you run the client for the first time:
  1. Your browser will open to Google’s authorization page
  2. Sign in with your Google account and grant the requested permissions
  3. After authorization, you’ll be redirected back
  4. The client receives the token and can make authenticated requests


The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.
##
[​](https://gofastmcp.com/integrations/google#production-configuration)
Production Configuration
`2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key` and `client_storage`:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.google import GoogleProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth_provider = GoogleProvider(
    client_id="123456789.apps.googleusercontent.com",
    client_secret="GOCSPX-abc123...",
    base_url="https://your-production-domain.com",
    required_scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],

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

mcp = FastMCP(name="Production Google App", auth=auth_provider)

```

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/servers/auth/oauth-proxy#configuration-parameters).
[ GitHub OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/github)[ OCI IAM OAuth 🤝 FastMCP Next ](https://gofastmcp.com/integrations/oci)
Ctrl+I
