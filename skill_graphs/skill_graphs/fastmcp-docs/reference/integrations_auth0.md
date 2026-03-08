[Skip to main content](https://gofastmcp.com/integrations/auth0#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
Auth0 OAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/integrations/auth0#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/auth0#prerequisites)
  * [Step 1: Create an Auth0 Application](https://gofastmcp.com/integrations/auth0#step-1-create-an-auth0-application)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/integrations/auth0#step-2-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/integrations/auth0#testing)
  * [Running the Server](https://gofastmcp.com/integrations/auth0#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/integrations/auth0#testing-with-a-client)
  * [Production Configuration](https://gofastmcp.com/integrations/auth0#production-configuration)


Auth
# Auth0 OAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with Auth0 OAuth
Copy page
`2.12.4` This guide shows you how to secure your FastMCP server using **Auth0 OAuth**. While Auth0 does have support for Dynamic Client Registration, it is not enabled by default so this integration uses the [**OIDC Proxy**](https://gofastmcp.com/servers/auth/oidc-proxy) pattern to bridge Auth0’s dynamic OIDC configuration with MCP’s authentication requirements.
##
[​](https://gofastmcp.com/integrations/auth0#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/auth0#prerequisites)
Prerequisites
Before you begin, you will need:
  1. An
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/integrations/auth0#step-1-create-an-auth0-application)
Step 1: Create an Auth0 Application
Create an Application in your Auth0 settings to get the credentials needed for authentication:
1
[](https://gofastmcp.com/integrations/auth0)
Navigate to Applications
Go to **Applications → Applications** in your Auth0 account.Click **”+ Create Application”** to create a new application.
2
[](https://gofastmcp.com/integrations/auth0)
Create Your Application
  * **Name** : Choose a name users will recognize (e.g., “My FastMCP Server”)
  * **Choose an application type** : Choose “Single Page Web Applications”
  * Click **Create** to create the application


3
[](https://gofastmcp.com/integrations/auth0)
Configure Your Application
Select the “Settings” tab for your application, then find the “Application URIs” section.
  * **Allowed Callback URLs** : Your server URL + `/auth/callback` (e.g., `http://localhost:8000/auth/callback`)
  * Click **Save** to save your changes


The callback URL must match exactly. The default path is `/auth/callback`, but you can customize it using the `redirect_path` parameter.
If you want to use a custom callback path (e.g., `/auth/auth0/callback`), make sure to set the same path in both your Auth0 Application settings and the `redirect_path` parameter when configuring the Auth0Provider.
4
[](https://gofastmcp.com/integrations/auth0)
Save Your Credentials
After creating the app, in the “Basic Information” section you’ll see:
  * **Client ID** : A public identifier like `tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB`
  * **Client Secret** : A private hidden value that should always be stored securely


Store these credentials securely. Never commit them to version control. Use environment variables or a secrets manager in production.
5
[](https://gofastmcp.com/integrations/auth0)
Select Your Audience
Go to **Applications → APIs** in your Auth0 account.
  * Find the API that you want to use for your application
  * **API Audience** : A URL that uniquely identifies the API


Store this along with of the credentials above. Never commit this to version control. Use environment variables or a secrets manager in production.
###
[​](https://gofastmcp.com/integrations/auth0#step-2-fastmcp-configuration)
Step 2: FastMCP Configuration
Create your FastMCP server using the `Auth0Provider`.
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.auth0 import Auth0Provider

# The Auth0Provider utilizes Auth0 OIDC configuration
auth_provider = Auth0Provider(
    config_url="https://.../.well-known/openid-configuration",  # Your Auth0 configuration URL
    client_id="tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB",               # Your Auth0 application Client ID
    client_secret="vPYqbjemq...",                               # Your Auth0 application Client Secret
    audience="https://...",                                     # Your Auth0 API audience
    base_url="http://localhost:8000",                           # Must match your application configuration
    # redirect_path="/auth/callback"                            # Default value, customize if needed
)

mcp = FastMCP(name="Auth0 Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_token_info() -> dict:
    """Returns information about the Auth0 token."""
    from fastmcp.server.dependencies import get_access_token

    token = get_access_token()

    return {
        "issuer": token.claims.get("iss"),
        "audience": token.claims.get("aud"),
        "scope": token.claims.get("scope")
    }

```

##
[​](https://gofastmcp.com/integrations/auth0#testing)
Testing
###
[​](https://gofastmcp.com/integrations/auth0#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by Auth0 authentication.
###
[​](https://gofastmcp.com/integrations/auth0#testing-with-a-client)
Testing with a Client
Create a test client that authenticates with your Auth0-protected server:
test_client.py
Copy
```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle Auth0 OAuth flows
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open Auth0 login in your browser
        print("✓ Authenticated with Auth0!")

        # Test the protected tool
        result = await client.call_tool("get_token_info")
        print(f"Auth0 audience: {result['audience']}")

if __name__ == "__main__":
    asyncio.run(main())

```

When you run the client for the first time:
  1. Your browser will open to Auth0’s authorization page
  2. After you authorize the app, you’ll be redirected back
  3. The client receives the token and can make authenticated requests


##
[​](https://gofastmcp.com/integrations/auth0#production-configuration)
Production Configuration
`2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key`, and `client_storage`:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.auth0 import Auth0Provider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth_provider = Auth0Provider(
    config_url="https://.../.well-known/openid-configuration",
    client_id="tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB",
    client_secret="vPYqbjemq...",
    audience="https://...",
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

mcp = FastMCP(name="Production Auth0 App", auth=auth_provider)

```

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/servers/auth/oauth-proxy#configuration-parameters).
The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.
[ Bearer Token Authentication Previous ](https://gofastmcp.com/clients/auth/bearer)[ AuthKit 🤝 FastMCP Next ](https://gofastmcp.com/integrations/authkit)
Ctrl+I
