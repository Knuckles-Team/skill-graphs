[Skip to main content](https://gofastmcp.com/v2/integrations/azure#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authentication
Azure (Microsoft Entra ID) OAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/v2/integrations/azure#configuration)
  * [Prerequisites](https://gofastmcp.com/v2/integrations/azure#prerequisites)
  * [Step 1: Create an Azure App Registration](https://gofastmcp.com/v2/integrations/azure#step-1-create-an-azure-app-registration)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/v2/integrations/azure#step-2-fastmcp-configuration)
  * [Scope Handling](https://gofastmcp.com/v2/integrations/azure#scope-handling)
  * [Testing](https://gofastmcp.com/v2/integrations/azure#testing)
  * [Running the Server](https://gofastmcp.com/v2/integrations/azure#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/v2/integrations/azure#testing-with-a-client)
  * [Production Configuration](https://gofastmcp.com/v2/integrations/azure#production-configuration)
  * [Environment Variables](https://gofastmcp.com/v2/integrations/azure#environment-variables)
  * [Provider Selection](https://gofastmcp.com/v2/integrations/azure#provider-selection)
  * [Azure-Specific Configuration](https://gofastmcp.com/v2/integrations/azure#azure-specific-configuration)


Authentication
# Azure (Microsoft Entra ID) OAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with Azure/Microsoft Entra OAuth
Copy page
`2.13.0` This guide shows you how to secure your FastMCP server using **Azure OAuth** (Microsoft Entra ID). Since Azure doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/v2/servers/auth/oauth-proxy) pattern to bridge Azure’s traditional OAuth with MCP’s authentication requirements. FastMCP validates Azure JWTs against your application’s client_id.
##
[​](https://gofastmcp.com/v2/integrations/azure#configuration)
Configuration
###
[​](https://gofastmcp.com/v2/integrations/azure#prerequisites)
Prerequisites
Before you begin, you will need:
  1. An
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)
  3. Your Azure tenant ID (found in Azure Portal under Microsoft Entra ID)


###
[​](https://gofastmcp.com/v2/integrations/azure#step-1-create-an-azure-app-registration)
Step 1: Create an Azure App Registration
Create an App registration in Azure Portal to get the credentials needed for authentication:
1
[](https://gofastmcp.com/v2/integrations/azure)
Navigate to App registrations
Go to the **Microsoft Entra ID → App registrations**.Click **“New registration”** to create a new application.
2
[](https://gofastmcp.com/v2/integrations/azure)
Configure Your Application
Fill in the application details:
  * **Name** : Choose a name users will recognize (e.g., “My FastMCP Server”)
  * **Supported account types** : Choose based on your needs:
    * **Single tenant** : Only users in your organization
    * **Multitenant** : Users in any Microsoft Entra directory
    * **Multitenant + personal accounts** : Any Microsoft account
  * **Redirect URI** : Select “Web” and enter your server URL + `/auth/callback` (e.g., `http://localhost:8000/auth/callback`)


The redirect URI must match exactly. The default path is `/auth/callback`, but you can customize it using the `redirect_path` parameter. For local development, Azure allows `http://localhost` URLs. For production, you must use HTTPS.
If you want to use a custom callback path (e.g., `/auth/azure/callback`), make sure to set the same path in both your Azure App registration and the `redirect_path` parameter when configuring the AzureProvider.
  * **Expose an API** : Configure your Application ID URI and define scopes
    * Go to **Expose an API** in the App registration sidebar.
    * Click **Set** next to “Application ID URI” and choose one of:
      * Keep the default `api://{client_id}`
      * Set a custom value, following the supported formats (see
    * Click **Add a scope** and create a scope your app will require, for example:
      * Scope name: `read` (or `write`, etc.)
      * Admin consent display name/description: as appropriate for your org
      * Who can consent: as needed (Admins only or Admins and users)
  * **Configure Access Token Version** : Ensure your app uses access token v2
    * Go to **Manifest** in the App registration sidebar.
    * Find the `requestedAccessTokenVersion` property and set it to `2`:
Copy
```
"api": {
    "requestedAccessTokenVersion": 2
}

```

    * Click **Save** at the top of the manifest editor.


Access token v2 is required for FastMCP’s Azure integration to work correctly. If this is not set, you may encounter authentication errors.
In FastMCP’s `AzureProvider`, set `identifier_uri` to your Application ID URI (optional; defaults to `api://{client_id}`) and set `required_scopes` to the unprefixed scope names (e.g., `read`, `write`). During authorization, FastMCP automatically prefixes scopes with your `identifier_uri`.
3
[](https://gofastmcp.com/v2/integrations/azure)
Create Client Secret
After registration, navigate to **Certificates & secrets** in your app’s settings.
  * Click **“New client secret”**
  * Add a description (e.g., “FastMCP Server”)
  * Choose an expiration period
  * Click **“Add”**


Copy the secret value immediately - it won’t be shown again! You’ll need to create a new secret if you lose it.
4
[](https://gofastmcp.com/v2/integrations/azure)
Note Your Credentials
From the **Overview** page of your app registration, note:
  * **Application (client) ID** : A UUID like `835f09b6-0f0f-40cc-85cb-f32c5829a149`
  * **Directory (tenant) ID** : A UUID like `08541b6e-646d-43de-a0eb-834e6713d6d5`
  * **Client Secret** : The value you copied in the previous step


Store these credentials securely. Never commit them to version control. Use environment variables or a secrets manager in production.
###
[​](https://gofastmcp.com/v2/integrations/azure#step-2-fastmcp-configuration)
Step 2: FastMCP Configuration
Create your FastMCP server using the `AzureProvider`, which handles Azure’s OAuth flow automatically:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.azure import AzureProvider

# The AzureProvider handles Azure's token format and validation
auth_provider = AzureProvider(
    client_id="835f09b6-0f0f-40cc-85cb-f32c5829a149",  # Your Azure App Client ID
    client_secret="your-client-secret",                 # Your Azure App Client Secret
    tenant_id="08541b6e-646d-43de-a0eb-834e6713d6d5", # Your Azure Tenant ID (REQUIRED)
    base_url="http://localhost:8000",                   # Must match your App registration
    required_scopes=["your-scope"],                 # At least one scope REQUIRED - name of scope from your App
    # identifier_uri defaults to api://{client_id}
    # identifier_uri="api://your-api-id",
    # Optional: request additional upstream scopes in the authorize request
    # additional_authorize_scopes=["User.Read", "offline_access", "openid", "email"],
    # redirect_path="/auth/callback"                  # Default value, customize if needed
    # base_authority="login.microsoftonline.us"      # For Azure Government (default: login.microsoftonline.com)
)

mcp = FastMCP(name="Azure Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_user_info() -> dict:
    """Returns information about the authenticated Azure user."""
    from fastmcp.server.dependencies import get_access_token

    token = get_access_token()
    # The AzureProvider stores user data in token claims
    return {
        "azure_id": token.claims.get("sub"),
        "email": token.claims.get("email"),
        "name": token.claims.get("name"),
        "job_title": token.claims.get("job_title"),
        "office_location": token.claims.get("office_location")
    }

```

**Important** : The `tenant_id` parameter is **REQUIRED**. Azure no longer supports using “common” for new applications due to security requirements. You must use one of:
  * **Your specific tenant ID** : Found in Azure Portal (e.g., `08541b6e-646d-43de-a0eb-834e6713d6d5`)
  * **“organizations”** : For work and school accounts only
  * **“consumers”** : For personal Microsoft accounts only

Using your specific tenant ID is recommended for better security and control.
**Important** : The `required_scopes` parameter is **REQUIRED** and must include at least one scope. Azure’s OAuth API requires the `scope` parameter in all authorization requests - you cannot authenticate without specifying at least one scope. Use the unprefixed scope names from your Azure App registration (e.g., `["read", "write"]`). These scopes must be created under **Expose an API** in your App registration.
###
[​](https://gofastmcp.com/v2/integrations/azure#scope-handling)
Scope Handling
FastMCP automatically prefixes `required_scopes` with your `identifier_uri` (e.g., `api://your-client-id`) since these are your custom API scopes. Scopes in `additional_authorize_scopes` are sent as-is since they target external resources like Microsoft Graph. **`required_scopes`**— Your custom API scopes, defined in Azure “Expose an API”:
You write | Sent to Azure | Validated on tokens
---|---|---
`mcp-read` | `api://xxx/mcp-read` | ✓
`my.scope` | `api://xxx/my.scope` | ✓
`openid` | `openid` | ✗ (OIDC scope)
`api://xxx/read` | `api://xxx/read` | ✓
**`additional_authorize_scopes`**— External scopes (e.g., Microsoft Graph) for server-side use:
You write | Sent to Azure | Validated on tokens
---|---|---
`User.Read` | `User.Read` | ✗
`Mail.Send` | `Mail.Send` | ✗
**Why aren’t`additional_authorize_scopes` validated?** Azure issues separate tokens per resource. The access token FastMCP receives is for _your API_ —Graph scopes aren’t in its `scp` claim. To call Graph APIs, your server uses the upstream Azure token in an on-behalf-of (OBO) flow.
OIDC scopes (`openid`, `profile`, `email`, `offline_access`) are never prefixed and excluded from validation because Azure doesn’t include them in access token `scp` claims.
##
[​](https://gofastmcp.com/v2/integrations/azure#testing)
Testing
###
[​](https://gofastmcp.com/v2/integrations/azure#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by Azure OAuth authentication.
###
[​](https://gofastmcp.com/v2/integrations/azure#testing-with-a-client)
Testing with a Client
Create a test client that authenticates with your Azure-protected server:
test_client.py
Copy
```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle Azure OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open Azure login in your browser
        print("✓ Authenticated with Azure!")

        # Test the protected tool
        result = await client.call_tool("get_user_info")
        print(f"Azure user: {result['email']}")
        print(f"Name: {result['name']}")

if __name__ == "__main__":
    asyncio.run(main())

```

When you run the client for the first time:
  1. Your browser will open to Microsoft’s authorization page
  2. Sign in with your Microsoft account (work, school, or personal based on your tenant configuration)
  3. Grant the requested permissions
  4. After authorization, you’ll be redirected back
  5. The client receives the token and can make authenticated requests


The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.
##
[​](https://gofastmcp.com/v2/integrations/azure#production-configuration)
Production Configuration
`2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key` and `client_storage`:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.azure import AzureProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth_provider = AzureProvider(
    client_id="835f09b6-0f0f-40cc-85cb-f32c5829a149",
    client_secret="your-client-secret",
    tenant_id="08541b6e-646d-43de-a0eb-834e6713d6d5",
    base_url="https://your-production-domain.com",
    required_scopes=["your-scope"],

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

mcp = FastMCP(name="Production Azure App", auth=auth_provider)

```

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/v2/servers/auth/oauth-proxy#configuration-parameters).
##
[​](https://gofastmcp.com/v2/integrations/azure#environment-variables)
Environment Variables
`2.12.1` For production deployments, use environment variables instead of hardcoding credentials.
###
[​](https://gofastmcp.com/v2/integrations/azure#provider-selection)
Provider Selection
Setting this environment variable allows the Azure provider to be used automatically without explicitly instantiating it in code.
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth)
FASTMCP_SERVER_AUTH
default:"Not set"
Set to `fastmcp.server.auth.providers.azure.AzureProvider` to use Azure authentication.
###
[​](https://gofastmcp.com/v2/integrations/azure#azure-specific-configuration)
Azure-Specific Configuration
These environment variables provide default values for the Azure provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth-azure-client-id)
FASTMCP_SERVER_AUTH_AZURE_CLIENT_ID
required
Your Azure App registration Client ID (e.g., `835f09b6-0f0f-40cc-85cb-f32c5829a149`)
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth-azure-client-secret)
FASTMCP_SERVER_AUTH_AZURE_CLIENT_SECRET
required
Your Azure App registration Client Secret
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth-azure-tenant-id)
FASTMCP_SERVER_AUTH_AZURE_TENANT_ID
required
Your Azure tenant ID (specific ID, “organizations”, or “consumers”)
This is **REQUIRED**. Find your tenant ID in Azure Portal under Microsoft Entra ID → Overview.
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth-azure-base-url)
FASTMCP_SERVER_AUTH_AZURE_BASE_URL
default:"http://localhost:8000"
Public URL where OAuth endpoints will be accessible (includes any mount path)
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth-azure-issuer-url)
FASTMCP_SERVER_AUTH_AZURE_ISSUER_URL
default:"Uses BASE_URL"
Issuer URL for OAuth metadata (defaults to `BASE_URL`). Set to root-level URL when mounting under a path prefix to avoid 404 logs. See [HTTP Deployment guide](https://gofastmcp.com/v2/deployment/http#mounting-authenticated-servers) for details.
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth-azure-redirect-path)
FASTMCP_SERVER_AUTH_AZURE_REDIRECT_PATH
default:"/auth/callback"
Redirect path configured in your Azure App registration
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth-azure-required-scopes)
FASTMCP_SERVER_AUTH_AZURE_REQUIRED_SCOPES
required
Comma-, space-, or JSON-separated list of required scopes for your API (at least one scope required). These are validated on tokens and used as defaults if the client does not request specific scopes. Use unprefixed scope names from your Azure App registration (e.g., `read,write`).You can include standard OIDC scopes (`openid`, `profile`, `email`, `offline_access`) in `required_scopes`. FastMCP automatically handles them correctly: they’re sent to Azure unprefixed and excluded from token validation (since Azure doesn’t include OIDC scopes in access token `scp` claims).
Azure’s OAuth API requires the `scope` parameter - you must provide at least one scope.
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth-azure-additional-authorize-scopes)
FASTMCP_SERVER_AUTH_AZURE_ADDITIONAL_AUTHORIZE_SCOPES
default:""
Comma-, space-, or JSON-separated list of additional scopes to include in the authorization request without prefixing. Use this to request upstream scopes such as Microsoft Graph permissions. These are not used for token validation.
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth-azure-identifier-uri)
FASTMCP_SERVER_AUTH_AZURE_IDENTIFIER_URI
default:"api://{client_id}"
Application ID URI used to prefix scopes during authorization.
[​](https://gofastmcp.com/v2/integrations/azure#param-fastmcp-server-auth-azure-base-authority)
FASTMCP_SERVER_AUTH_AZURE_BASE_AUTHORITY
default:"login.microsoftonline.com"
Azure authority base URL. Override this to use Azure Government:
  * `login.microsoftonline.com` - Azure Public Cloud (default)
  * `login.microsoftonline.us` - Azure Government

This setting affects all Azure OAuth endpoints (authorization, token, issuer, JWKS).
Example `.env` file:
Copy
```
# Use the Azure provider
FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.azure.AzureProvider

# Azure OAuth credentials
FASTMCP_SERVER_AUTH_AZURE_CLIENT_ID=835f09b6-0f0f-40cc-85cb-f32c5829a149
FASTMCP_SERVER_AUTH_AZURE_CLIENT_SECRET=your-client-secret-here
FASTMCP_SERVER_AUTH_AZURE_TENANT_ID=08541b6e-646d-43de-a0eb-834e6713d6d5
FASTMCP_SERVER_AUTH_AZURE_BASE_URL=https://your-server.com
FASTMCP_SERVER_AUTH_AZURE_REQUIRED_SCOPES=read,write
# Optional custom API configuration
# FASTMCP_SERVER_AUTH_AZURE_IDENTIFIER_URI=api://your-api-id
# Request additional upstream scopes (optional)
# FASTMCP_SERVER_AUTH_AZURE_ADDITIONAL_AUTHORIZE_SCOPES=User.Read,Mail.Read

```

With environment variables set, your server code simplifies to:
server.py
Copy
```
from fastmcp import FastMCP

# Authentication is automatically configured from environment
mcp = FastMCP(name="Azure Secured App")

@mcp.tool
async def protected_tool(query: str) -> str:
    """A tool that requires Azure authentication to access."""
    # Your tool implementation here
    return f"Processing authenticated request: {query}"

```

[ AWS Cognito OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/v2/integrations/aws-cognito)[ Descope 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/descope)
Ctrl+I
