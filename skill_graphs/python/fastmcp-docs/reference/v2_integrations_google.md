[Skip to main content](https://gofastmcp.com/v2/integrations/google#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authentication
Google OAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/v2/integrations/google#configuration)
  * [Prerequisites](https://gofastmcp.com/v2/integrations/google#prerequisites)
  * [Step 1: Create a Google OAuth 2.0 Client ID](https://gofastmcp.com/v2/integrations/google#step-1-create-a-google-oauth-2-0-client-id)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/v2/integrations/google#step-2-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/v2/integrations/google#testing)
  * [Running the Server](https://gofastmcp.com/v2/integrations/google#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/v2/integrations/google#testing-with-a-client)
  * [Production Configuration](https://gofastmcp.com/v2/integrations/google#production-configuration)
  * [Environment Variables](https://gofastmcp.com/v2/integrations/google#environment-variables)
  * [Provider Selection](https://gofastmcp.com/v2/integrations/google#provider-selection)
  * [Google-Specific Configuration](https://gofastmcp.com/v2/integrations/google#google-specific-configuration)


Authentication
# Google OAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with Google OAuth
Copy page
`2.12.0` This guide shows you how to secure your FastMCP server using **Google OAuth**. Since Google doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/v2/servers/auth/oauth-proxy) pattern to bridge Google’s traditional OAuth with MCP’s authentication requirements.
##
[​](https://gofastmcp.com/v2/integrations/google#configuration)
Configuration
###
[​](https://gofastmcp.com/v2/integrations/google#prerequisites)
Prerequisites
Before you begin, you will need:
  1. A
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/v2/integrations/google#step-1-create-a-google-oauth-2-0-client-id)
Step 1: Create a Google OAuth 2.0 Client ID
Create an OAuth 2.0 Client ID in your Google Cloud Console to get the credentials needed for authentication:
1
[](https://gofastmcp.com/v2/integrations/google)
Navigate to OAuth Consent Screen
Go to the First, configure the OAuth consent screen by navigating to **APIs & Services → OAuth consent screen**. Choose “External” for testing or “Internal” for G Suite organizations.
2
[](https://gofastmcp.com/v2/integrations/google)
Create OAuth 2.0 Client ID
Navigate to **APIs & Services → Credentials** and click **”+ CREATE CREDENTIALS”** → **“OAuth client ID”**.Configure your OAuth client:
  * **Application type** : Web application
  * **Name** : Choose a descriptive name (e.g., “FastMCP Server”)
  * **Authorized JavaScript origins** : Add your server’s base URL (e.g., `http://localhost:8000`)
  * **Authorized redirect URIs** : Add your server URL + `/auth/callback` (e.g., `http://localhost:8000/auth/callback`)


The redirect URI must match exactly. The default path is `/auth/callback`, but you can customize it using the `redirect_path` parameter. For local development, Google allows `http://localhost` URLs with various ports. For production, you must use HTTPS.
If you want to use a custom callback path (e.g., `/auth/google/callback`), make sure to set the same path in both your Google OAuth Client settings and the `redirect_path` parameter when configuring the GoogleProvider.
3
[](https://gofastmcp.com/v2/integrations/google)
Save Your Credentials
After creating the client, you’ll receive:
  * **Client ID** : A string ending in `.apps.googleusercontent.com`
  * **Client Secret** : A string starting with `GOCSPX-`

Download the JSON credentials or copy these values securely.
Store these credentials securely. Never commit them to version control. Use environment variables or a secrets manager in production.
###
[​](https://gofastmcp.com/v2/integrations/google#step-2-fastmcp-configuration)
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
[​](https://gofastmcp.com/v2/integrations/google#testing)
Testing
###
[​](https://gofastmcp.com/v2/integrations/google#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by Google OAuth authentication.
###
[​](https://gofastmcp.com/v2/integrations/google#testing-with-a-client)
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
[​](https://gofastmcp.com/v2/integrations/google#production-configuration)
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

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/v2/servers/auth/oauth-proxy#configuration-parameters).
##
[​](https://gofastmcp.com/v2/integrations/google#environment-variables)
Environment Variables
`2.12.1` For production deployments, use environment variables instead of hardcoding credentials.
###
[​](https://gofastmcp.com/v2/integrations/google#provider-selection)
Provider Selection
Setting this environment variable allows the Google provider to be used automatically without explicitly instantiating it in code.
[​](https://gofastmcp.com/v2/integrations/google#param-fastmcp-server-auth)
FASTMCP_SERVER_AUTH
default:"Not set"
Set to `fastmcp.server.auth.providers.google.GoogleProvider` to use Google authentication.
###
[​](https://gofastmcp.com/v2/integrations/google#google-specific-configuration)
Google-Specific Configuration
These environment variables provide default values for the Google provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.
[​](https://gofastmcp.com/v2/integrations/google#param-fastmcp-server-auth-google-client-id)
FASTMCP_SERVER_AUTH_GOOGLE_CLIENT_ID
required
Your Google OAuth 2.0 Client ID (e.g., `123456789.apps.googleusercontent.com`)
[​](https://gofastmcp.com/v2/integrations/google#param-fastmcp-server-auth-google-client-secret)
FASTMCP_SERVER_AUTH_GOOGLE_CLIENT_SECRET
required
Your Google OAuth 2.0 Client Secret (e.g., `GOCSPX-abc123...`)
[​](https://gofastmcp.com/v2/integrations/google#param-fastmcp-server-auth-google-base-url)
FASTMCP_SERVER_AUTH_GOOGLE_BASE_URL
default:"http://localhost:8000"
Public URL where OAuth endpoints will be accessible (includes any mount path)
[​](https://gofastmcp.com/v2/integrations/google#param-fastmcp-server-auth-google-issuer-url)
FASTMCP_SERVER_AUTH_GOOGLE_ISSUER_URL
default:"Uses BASE_URL"
Issuer URL for OAuth metadata (defaults to `BASE_URL`). Set to root-level URL when mounting under a path prefix to avoid 404 logs. See [HTTP Deployment guide](https://gofastmcp.com/v2/deployment/http#mounting-authenticated-servers) for details.
[​](https://gofastmcp.com/v2/integrations/google#param-fastmcp-server-auth-google-redirect-path)
FASTMCP_SERVER_AUTH_GOOGLE_REDIRECT_PATH
default:"/auth/callback"
Redirect path configured in your Google OAuth Client
[​](https://gofastmcp.com/v2/integrations/google#param-fastmcp-server-auth-google-required-scopes)
FASTMCP_SERVER_AUTH_GOOGLE_REQUIRED_SCOPES
default:"[]"
Comma-, space-, or JSON-separated list of required Google scopes (e.g., `"openid,https://www.googleapis.com/auth/userinfo.email"` or `["openid", "https://www.googleapis.com/auth/userinfo.email"]`)
[​](https://gofastmcp.com/v2/integrations/google#param-fastmcp-server-auth-google-timeout-seconds)
FASTMCP_SERVER_AUTH_GOOGLE_TIMEOUT_SECONDS
default:"10"
HTTP request timeout for Google API calls
Example `.env` file:
Copy
```
# Use the Google provider
FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.google.GoogleProvider

# Google OAuth credentials
FASTMCP_SERVER_AUTH_GOOGLE_CLIENT_ID=123456789.apps.googleusercontent.com
FASTMCP_SERVER_AUTH_GOOGLE_CLIENT_SECRET=GOCSPX-abc123...
FASTMCP_SERVER_AUTH_GOOGLE_BASE_URL=https://your-server.com
FASTMCP_SERVER_AUTH_GOOGLE_REQUIRED_SCOPES=openid,https://www.googleapis.com/auth/userinfo.email

```

With environment variables set, your server code simplifies to:
server.py
Copy
```
from fastmcp import FastMCP

# Authentication is automatically configured from environment
mcp = FastMCP(name="Google Secured App")

@mcp.tool
async def protected_tool(query: str) -> str:
    """A tool that requires Google authentication to access."""
    # Your tool implementation here
    return f"Processing authenticated request: {query}"

```

[ GitHub OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/v2/integrations/github)[ OCI IAM OAuth 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/oci)
Ctrl+I
