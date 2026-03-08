[Skip to main content](https://gofastmcp.com/integrations/azure#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
Azure (Microsoft Entra ID) OAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/integrations/azure#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/azure#prerequisites)
  * [Step 1: Create an Azure App Registration](https://gofastmcp.com/integrations/azure#step-1-create-an-azure-app-registration)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/integrations/azure#step-2-fastmcp-configuration)
  * [Scope Handling](https://gofastmcp.com/integrations/azure#scope-handling)
  * [Testing](https://gofastmcp.com/integrations/azure#testing)
  * [Running the Server](https://gofastmcp.com/integrations/azure#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/integrations/azure#testing-with-a-client)
  * [Production Configuration](https://gofastmcp.com/integrations/azure#production-configuration)
  * [Token Verification Only (Managed Identity)](https://gofastmcp.com/integrations/azure#token-verification-only-managed-identity)
  * [On-Behalf-Of (OBO)](https://gofastmcp.com/integrations/azure#on-behalf-of-obo)
  * [Azure Portal Setup](https://gofastmcp.com/integrations/azure#azure-portal-setup)
  * [Configure AzureProvider for OBO](https://gofastmcp.com/integrations/azure#configure-azureprovider-for-obo)
  * [EntraOBOToken Dependency](https://gofastmcp.com/integrations/azure#entraobotoken-dependency)


Auth
# Azure (Microsoft Entra ID) OAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with Azure/Microsoft Entra OAuth
Copy page
`2.13.0` This guide shows you how to secure your FastMCP server using **Azure OAuth** (Microsoft Entra ID). Since Azure doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/servers/auth/oauth-proxy) pattern to bridge Azure’s traditional OAuth with MCP’s authentication requirements. FastMCP validates Azure JWTs against your application’s client_id.
##
[​](https://gofastmcp.com/integrations/azure#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/azure#prerequisites)
Prerequisites
Before you begin, you will need:
  1. An
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)
  3. Your Azure tenant ID (found in Azure Portal under Microsoft Entra ID)


###
[​](https://gofastmcp.com/integrations/azure#step-1-create-an-azure-app-registration)
Step 1: Create an Azure App Registration
Create an App registration in Azure Portal to get the credentials needed for authentication:
1
[](https://gofastmcp.com/integrations/azure)
Navigate to App registrations
Go to the **Microsoft Entra ID → App registrations**.Click **“New registration”** to create a new application.
2
[](https://gofastmcp.com/integrations/azure)
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
[](https://gofastmcp.com/integrations/azure)
Create Client Secret
After registration, navigate to **Certificates & secrets** in your app’s settings.
  * Click **“New client secret”**
  * Add a description (e.g., “FastMCP Server”)
  * Choose an expiration period
  * Click **“Add”**


Copy the secret value immediately - it won’t be shown again! You’ll need to create a new secret if you lose it.
4
[](https://gofastmcp.com/integrations/azure)
Note Your Credentials
From the **Overview** page of your app registration, note:
  * **Application (client) ID** : A UUID like `835f09b6-0f0f-40cc-85cb-f32c5829a149`
  * **Directory (tenant) ID** : A UUID like `08541b6e-646d-43de-a0eb-834e6713d6d5`
  * **Client Secret** : The value you copied in the previous step


Store these credentials securely. Never commit them to version control. Use environment variables or a secrets manager in production.
###
[​](https://gofastmcp.com/integrations/azure#step-2-fastmcp-configuration)
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
    # additional_authorize_scopes=["User.Read", "openid", "email"],
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
[​](https://gofastmcp.com/integrations/azure#scope-handling)
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
`offline_access` is automatically included to obtain refresh tokens. FastMCP manages token refreshing automatically.
**Why aren’t`additional_authorize_scopes` validated?** Azure issues separate tokens per resource. The access token FastMCP receives is for _your API_ —Graph scopes aren’t in its `scp` claim. To call Graph APIs, your server uses the upstream Azure token in an on-behalf-of (OBO) flow.
OIDC scopes (`openid`, `profile`, `email`, `offline_access`) are never prefixed and excluded from validation because Azure doesn’t include them in access token `scp` claims.
##
[​](https://gofastmcp.com/integrations/azure#testing)
Testing
###
[​](https://gofastmcp.com/integrations/azure#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by Azure OAuth authentication.
###
[​](https://gofastmcp.com/integrations/azure#testing-with-a-client)
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
[​](https://gofastmcp.com/integrations/azure#production-configuration)
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

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/servers/auth/oauth-proxy#configuration-parameters).
##
[​](https://gofastmcp.com/integrations/azure#token-verification-only-managed-identity)
Token Verification Only (Managed Identity)
`2.15.0` For deployments where your server only needs to **validate incoming tokens** — such as Azure Container Apps with Managed Identity — use `AzureJWTVerifier` with `RemoteAuthProvider` instead of the full `AzureProvider`. This pattern is ideal when:
  * Your infrastructure handles authentication (e.g., Managed Identity)
  * You don’t need the OAuth proxy flow (no `client_secret` required)
  * You just need to verify that incoming Azure AD tokens are valid


server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth import RemoteAuthProvider
from fastmcp.server.auth.providers.azure import AzureJWTVerifier
from pydantic import AnyHttpUrl

tenant_id = "your-tenant-id"
client_id = "your-client-id"

# AzureJWTVerifier auto-configures JWKS, issuer, and audience
verifier = AzureJWTVerifier(
    client_id=client_id,
    tenant_id=tenant_id,
    required_scopes=["access_as_user"],  # Scope names from Azure Portal
)

auth = RemoteAuthProvider(
    token_verifier=verifier,
    authorization_servers=[
        AnyHttpUrl(f"https://login.microsoftonline.com/{tenant_id}/v2.0")
    ],
    base_url="https://your-container-app.azurecontainerapps.io",
)

mcp = FastMCP(name="Azure MI App", auth=auth)

```

`AzureJWTVerifier` handles Azure’s scope format automatically. You write scope names exactly as they appear in Azure Portal under **Expose an API** (e.g., `access_as_user`). The verifier validates tokens using the short-form scopes that Azure puts in the `scp` claim, while advertising the full URI scopes (e.g., `api://your-client-id/access_as_user`) in OAuth metadata so MCP clients know what to request.
For Azure Government, pass `base_authority="login.microsoftonline.us"` to `AzureJWTVerifier`.
##
[​](https://gofastmcp.com/integrations/azure#on-behalf-of-obo)
On-Behalf-Of (OBO)
`3.0.0` The On-Behalf-Of (OBO) flow allows your FastMCP server to call downstream Microsoft APIs—like Microsoft Graph—using the authenticated user’s identity. When a user authenticates to your MCP server, you receive a token for your API. OBO exchanges that token for a new token that can call other services, maintaining the user’s identity and permissions throughout the chain. This pattern is useful when your tools need to access user-specific data from Microsoft services: reading emails, accessing calendar events, querying SharePoint, or any other Graph API operation that requires user context.
OBO features require the `azure` extra:
Copy
```
pip install 'fastmcp[azure]'

```

###
[​](https://gofastmcp.com/integrations/azure#azure-portal-setup)
Azure Portal Setup
OBO requires additional configuration in your Azure App registration beyond basic authentication.
1
[](https://gofastmcp.com/integrations/azure)
Add API Permissions
In your App registration, navigate to **API permissions** and add the Microsoft Graph permissions your tools will need.
  * Click **Add a permission** → **Microsoft Graph** → **Delegated permissions**
  * Select the permissions required for your use case (e.g., `Mail.Read`, `Calendars.Read`, `User.Read`)
  * Repeat for any other APIs you need to call


Only add delegated permissions for OBO. Application permissions bypass user context entirely and are inappropriate for the OBO flow.
2
[](https://gofastmcp.com/integrations/azure)
Grant Admin Consent
OBO requires admin consent for the permissions you’ve added. In the **API permissions** page, click **Grant admin consent for [Your Organization]**.Without admin consent, OBO token exchanges will fail with an `AADSTS65001` error indicating the user or administrator hasn’t consented to use the application.
For development, you can grant consent for just your own account. For production, an Azure AD administrator must grant tenant-wide consent.
###
[​](https://gofastmcp.com/integrations/azure#configure-azureprovider-for-obo)
Configure AzureProvider for OBO
The `additional_authorize_scopes` parameter tells Azure which downstream API permissions to include during the initial authorization. These scopes establish what your server can request through OBO later.
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.azure import AzureProvider

auth_provider = AzureProvider(
    client_id="your-client-id",
    client_secret="your-client-secret",
    tenant_id="your-tenant-id",
    base_url="http://localhost:8000",
    required_scopes=["mcp-access"],  # Your API scope
    # Include Graph scopes for OBO
    additional_authorize_scopes=[
        "https://graph.microsoft.com/Mail.Read",
        "https://graph.microsoft.com/User.Read",
        "offline_access",  # Enables refresh tokens
    ],
)

mcp = FastMCP(name="Graph-Enabled Server", auth=auth_provider)

```

Scopes listed in `additional_authorize_scopes` are requested during the initial OAuth flow but aren’t validated on incoming tokens. They establish permission for your server to later exchange the user’s token for downstream API access.
Use fully-qualified scope URIs for downstream APIs (e.g., `https://graph.microsoft.com/Mail.Read`). Short forms like `Mail.Read` work for authorization requests, but fully-qualified URIs are clearer and avoid ambiguity.
###
[​](https://gofastmcp.com/integrations/azure#entraobotoken-dependency)
EntraOBOToken Dependency
The `EntraOBOToken` dependency handles the complete OBO flow automatically. Declare it as a parameter default with the scopes you need, and FastMCP exchanges the user’s token for a downstream API token before your function runs.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.azure import AzureProvider, EntraOBOToken
import httpx

auth_provider = AzureProvider(
    client_id="your-client-id",
    client_secret="your-client-secret",
    tenant_id="your-tenant-id",
    base_url="http://localhost:8000",
    required_scopes=["mcp-access"],
    additional_authorize_scopes=[
        "https://graph.microsoft.com/Mail.Read",
        "https://graph.microsoft.com/User.Read",
    ],
)

mcp = FastMCP(name="Email Reader", auth=auth_provider)

@mcp.tool
async def get_recent_emails(
    count: int = 10,
    graph_token: str = EntraOBOToken(["https://graph.microsoft.com/Mail.Read"]),
) -> list[dict]:
    """Get the user's recent emails from Microsoft Graph."""
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://graph.microsoft.com/v1.0/me/messages?$top={count}",
            headers={"Authorization": f"Bearer {graph_token}"},
        )
        response.raise_for_status()
        data = response.json()

    return [
        {"subject": msg["subject"], "from": msg["from"]["emailAddress"]["address"]}
        for msg in data.get("value", [])
    ]

```

The `graph_token` parameter receives a ready-to-use access token for Microsoft Graph. FastMCP handles the OBO exchange transparently—your function just uses the token to call the API.
**Scope alignment is critical.** The scopes passed to `EntraOBOToken` must be a subset of the scopes in `additional_authorize_scopes`. If you request a scope during OBO that wasn’t included in the initial authorization, the exchange will fail.
For advanced OBO scenarios, use `CurrentAccessToken()` to get the user’s token, then construct an `azure.identity.aio.OnBehalfOfCredential` directly with your Azure credentials.
For a complete working example of Azure OBO with FastMCP, see
[ AWS Cognito OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/aws-cognito)[ Descope 🤝 FastMCP Next ](https://gofastmcp.com/integrations/descope)
Ctrl+I
