[Skip to main content](https://gofastmcp.com/v2/integrations/oci#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authentication
OCI IAM OAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/v2/integrations/oci#configuration)
  * [Prerequisites](https://gofastmcp.com/v2/integrations/oci#prerequisites)
  * [Step 1: Make sure client access is enabled for JWK’s URL](https://gofastmcp.com/v2/integrations/oci#step-1-make-sure-client-access-is-enabled-for-jwk%E2%80%99s-url)
  * [Step 2: Create OAuth client for MCP server authentication](https://gofastmcp.com/v2/integrations/oci#step-2-create-oauth-client-for-mcp-server-authentication)
  * [Step 3: Token Exchange Setup (Only if MCP server needs to talk to OCI Control Plane)](https://gofastmcp.com/v2/integrations/oci#step-3-token-exchange-setup-only-if-mcp-server-needs-to-talk-to-oci-control-plane)
  * [Running MCP server](https://gofastmcp.com/v2/integrations/oci#running-mcp-server)
  * [Production Configuration](https://gofastmcp.com/v2/integrations/oci#production-configuration)
  * [Environment Variables](https://gofastmcp.com/v2/integrations/oci#environment-variables)
  * [Provider Selection](https://gofastmcp.com/v2/integrations/oci#provider-selection)
  * [OCI-Specific Configuration](https://gofastmcp.com/v2/integrations/oci#oci-specific-configuration)


Authentication
# OCI IAM OAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with OCI IAM OAuth
Copy page
`2.13.0` This guide shows you how to secure your FastMCP server using **OCI IAM OAuth**. Since OCI IAM doesn’t support Dynamic Client Registration, this integration uses the [**OIDC Proxy**](https://gofastmcp.com/v2/servers/auth/oidc-proxy) pattern to bridge OCI’s traditional OAuth with MCP’s authentication requirements.
##
[​](https://gofastmcp.com/v2/integrations/oci#configuration)
Configuration
###
[​](https://gofastmcp.com/v2/integrations/oci#prerequisites)
Prerequisites
  1. An OCI cloud Account with access to create an Integrated Application in an Identity Domain.
  2. Your FastMCP server’s URL (For dev environments, it is


###
[​](https://gofastmcp.com/v2/integrations/oci#step-1-make-sure-client-access-is-enabled-for-jwk%E2%80%99s-url)
Step 1: Make sure client access is enabled for JWK’s URL
1
[](https://gofastmcp.com/v2/integrations/oci)
Navigate to OCI IAM Domain Settings
Login to OCI console (
![OCI console showing the Edit Domain Settings button in the IAM Domain settings page](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocieditdomainsettingsbutton.png?fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=189e2e2c679c33b33a79164756cb6440)
2
[](https://gofastmcp.com/v2/integrations/oci)
Update Domain Setting
Enable “Configure client access” checkbox as shown in the screenshot.
![OCI IAM Domain Settings](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocieditdomainsettings.png?fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=3f4422ba7b3c45fec724b4bb5de6ff31)
###
[​](https://gofastmcp.com/v2/integrations/oci#step-2-create-oauth-client-for-mcp-server-authentication)
Step 2: Create OAuth client for MCP server authentication
Follow the Steps as mentioned below to create an OAuth client.
1
[](https://gofastmcp.com/v2/integrations/oci)
Navigate to OCI IAM Integrated Applications
Login to OCI console (
2
[](https://gofastmcp.com/v2/integrations/oci)
Add an Integrated Application
Select Add application. In the Add application window, select Confidential Application. Select Launch workflow. In the Add application details page, Enter name and description as shown below.
![Adding a Confidential Integrated Application in OCI IAM Domain](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ociaddapplication.png?fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=5855c5dc6cd69f8a0c53f3f103e7b4fc)
3
[](https://gofastmcp.com/v2/integrations/oci)
Update OAuth Configuration for an Integrated Application
Once the Integrated Application is created, Click on “OAuth configuration” tab. Click on “Edit OAuth configuration” button. Configure the application as OAuth client by selecting “Configure this application as a client now” radio button. Select “Authorization code” grant type. If you are planning to use the same OAuth client application for token exchange, select “Client credentials” grant type as well. In the sample, we will use the same client. For Authorization grant type, select redirect URL. In most cases, this will be the MCP server URL followed by “/oauth/callback”.
![OAuth Configuration for an Integrated Application in OCI IAM Domain](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocioauthconfiguration.png?fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=885b0adc7c2a25ee71cf7e455b6afd62)
4
[](https://gofastmcp.com/v2/integrations/oci)
Activate the Integrated Application
Click on “Submit” button to update OAuth configuration for the client application. **Note: You don’t need to do any special configuration to support PKCE for the OAuth client.** Make sure to Activate the client application. Note down client ID and client secret for the application. Update .env file and replace FASTMCP_SERVER_AUTH_OCI_CLIENT_ID and FASTMCP_SERVER_AUTH_OCI_CLIENT_SECRET values. FASTMCP_SERVER_AUTH_OCI_IAM_GUID in the env file is the Identity domain URL that you chose for the MCP server.
This is all you need to implement MCP server authentication against OCI IAM. However, you may want to use an authenticated user token to invoke OCI control plane APIs and propagate identity to the OCI control plane instead of using a service user account. In that case, you need to implement token exchange.
###
[​](https://gofastmcp.com/v2/integrations/oci#step-3-token-exchange-setup-only-if-mcp-server-needs-to-talk-to-oci-control-plane)
Step 3: Token Exchange Setup (Only if MCP server needs to talk to OCI Control Plane)
Token exchange helps you exchange a logged-in user’s OCI IAM token for an OCI control plane session token, also known as UPST (User Principal Session Token). To learn more about token exchange, refer to my  For token exchange, we need to configure Identity propagation trust. The blog above discusses setting up the trust using REST APIs. However, you can also use OCI CLI. Before using the CLI command below, ensure that you have created a token exchange OAuth client. In most cases, you can use the same OAuth client that you created above. You will use the client ID of the token exchange OAuth client in the CLI command below and replace it with . You will also need to update the client secret for the token exchange OAuth client in the .env file. It is the FASTMCP_SERVER_AUTH_OCI_CLIENT_SECRET parameter. Update FASTMCP_SERVER_AUTH_OCI_IAM_GUID and FASTMCP_SERVER_AUTH_OCI_CLIENT_ID as well for the token exchange OAuth client in the .env file.
Copy
```
oci identity-domains identity-propagation-trust create \
--schemas '["urn:ietf:params:scim:schemas:oracle:idcs:IdentityPropagationTrust"]' \
--public-key-endpoint "https://{FASTMCP_SERVER_AUTH_OCI_IAM_GUID}.identity.oraclecloud.com/admin/v1/SigningCert/jwk" \
--name "For Token Exchange" --type "JWT" \
--issuer "https://identity.oraclecloud.com/" --active true \
--endpoint "https://{FASTMCP_SERVER_AUTH_OCI_IAM_GUID}.identity.oracleclcoud.com" \
--subject-claim-name "sub" --allow-impersonation false \
--subject-mapping-attribute "username" \
--subject-type "User" --client-claim-name "iss" \
--client-claim-values '["https://identity.oraclecloud.com/"]' \
--oauth-clients '["{FASTMCP_SERVER_AUTH_OCI_CLIENT_ID}"]'

```

To exchange access token for OCI token and create a signer object, you need to add below code in MCP server. You can then use the signer object to create any OCI control plane client.
Copy
```

from fastmcp.server.dependencies import get_access_token
from fastmcp.utilities.logging import get_logger
from oci.auth.signers import TokenExchangeSigner
import os

logger = get_logger(__name__)

# Load configuration from environment
FASTMCP_SERVER_AUTH_OCI_IAM_GUID = os.environ["FASTMCP_SERVER_AUTH_OCI_IAM_GUID"]
FASTMCP_SERVER_AUTH_OCI_CLIENT_ID = os.environ["FASTMCP_SERVER_AUTH_OCI_CLIENT_ID"]
FASTMCP_SERVER_AUTH_OCI_CLIENT_SECRET = os.environ["FASTMCP_SERVER_AUTH_OCI_CLIENT_SECRET"]

_global_token_cache = {} #In memory cache for OCI session token signer

def get_oci_signer() -> TokenExchangeSigner:

    authntoken = get_access_token()
    tokenID = authntoken.claims.get("jti")
    token = authntoken.token

    #Check if the signer exists for the token ID in memory cache
    cached_signer = _global_token_cache.get(tokenID)
    logger.debug(f"Global cached signer: {cached_signer}")
    if cached_signer:
        logger.debug(f"Using globally cached signer for token ID: {tokenID}")
        return cached_signer

    #If the signer is not yet created for the token then create new OCI signer object
    logger.debug(f"Creating new signer for token ID: {tokenID}")
    signer = TokenExchangeSigner(
        jwt_or_func=token,
        oci_domain_id=FASTMCP_SERVER_AUTH_OCI_IAM_GUID.split(".")[0],
        client_id=FASTMCP_SERVER_AUTH_OCI_CLIENT_ID,
        client_secret=FASTMCP_SERVER_AUTH_OCI_CLIENT_SECRET,
    )
    logger.debug(f"Signer {signer} created for token ID: {tokenID}")

    #Cache the signer object in memory cache
    _global_token_cache[tokenID] = signer
    logger.debug(f"Signer cached for token ID: {tokenID}")

    return signer

```

##
[​](https://gofastmcp.com/v2/integrations/oci#running-mcp-server)
Running MCP server
Once the setup is complete, to run the MCP server, run the below command.
Copy
```
fastmcp run server.py:mcp --transport http --port 8000

```

To run MCP client, run the below command.
Copy
```
python3 client.py

```

MCP Client sample is as below.
client.py
Copy
```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle OCI OAuth flows
    async with Client("http://localhost:8000/mcp/", auth="oauth") as client:
        # First-time connection will open OCI login in your browser
        print("✓ Authenticated with OCI IAM")

        tools = await client.list_tools()
        print(f"🔧 Available tools ({len(tools)}):")
        for tool in tools:
            print(f"   - {tool.name}: {tool.description}")

if __name__ == "__main__":
    asyncio.run(main())

```

When you run the client for the first time:
  1. Your browser will open to OCI IAM’s login page
  2. Sign in with your OCI account and grant the requested consent
  3. After authorization, you’ll be redirected back to the redirect path
  4. The client receives the token and can make authenticated requests


##
[​](https://gofastmcp.com/v2/integrations/oci#production-configuration)
Production Configuration
`2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key`, and `client_storage`:
server.py
Copy
```

import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.oci import OCIProvider

from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Load configuration from environment
FASTMCP_SERVER_AUTH_OCI_CONFIG_URL = os.environ["FASTMCP_SERVER_AUTH_OCI_CONFIG_URL"]
FASTMCP_SERVER_AUTH_OCI_CLIENT_ID = os.environ["FASTMCP_SERVER_AUTH_OCI_CLIENT_ID"]
FASTMCP_SERVER_AUTH_OCI_CLIENT_SECRET = os.environ["FASTMCP_SERVER_AUTH_OCI_CLIENT_SECRET"]

# Production setup with encrypted persistent token storage
auth_provider = OCIProvider(
    config_url=FASTMCP_SERVER_AUTH_OCI_CONFIG_URL,
    client_id=FASTMCP_SERVER_AUTH_OCI_CLIENT_ID,
    client_secret=FASTMCP_SERVER_AUTH_OCI_CLIENT_SECRET,
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

mcp = FastMCP(name="Production OCI App", auth=auth_provider)

```

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at Rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/v2/servers/auth/oauth-proxy#configuration-parameters).
The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.
##
[​](https://gofastmcp.com/v2/integrations/oci#environment-variables)
Environment Variables
For production deployments, use environment variables instead of hardcoding credentials.
###
[​](https://gofastmcp.com/v2/integrations/oci#provider-selection)
Provider Selection
Setting this environment variable allows the OCI provider to be used automatically without explicitly instantiating it in code.
[​](https://gofastmcp.com/v2/integrations/oci#param-fastmcp-server-auth)
FASTMCP_SERVER_AUTH
default:"Not set"
Set to `fastmcp.server.auth.providers.oci.OCIProvider` to use OCI IAM authentication.
###
[​](https://gofastmcp.com/v2/integrations/oci#oci-specific-configuration)
OCI-Specific Configuration
These environment variables provide default values for the OCI IAM provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.
[​](https://gofastmcp.com/v2/integrations/oci#param-fastmcp-server-auth-oci-iam-guid)
FASTMCP_SERVER_AUTH_OCI_IAM_GUID
required
Your OCI Application Configuration URL (e.g., `idcs-asdascxasd11......identity.oraclecloud.com`)
[​](https://gofastmcp.com/v2/integrations/oci#param-fastmcp-server-auth-oci-config-url)
FASTMCP_SERVER_AUTH_OCI_CONFIG_URL
required
Your OCI Application Configuration URL (e.g., `https://{FASTMCP_SERVER_AUTH_OCI_IAM_GUID}.identity.oraclecloud.com/.well-known/openid-configuration`)
[​](https://gofastmcp.com/v2/integrations/oci#param-fastmcp-server-auth-oci-client-id)
FASTMCP_SERVER_AUTH_OCI_CLIENT_ID
required
Your OCI Application Client ID (e.g., `tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB`)
[​](https://gofastmcp.com/v2/integrations/oci#param-fastmcp-server-auth-oci-client-secret)
FASTMCP_SERVER_AUTH_OCI_CLIENT_SECRET
required
Your OCI Application Client Secret (e.g., `idcsssvPYqbjemq...`)
[​](https://gofastmcp.com/v2/integrations/oci#param-fastmcp-server-auth-oci-base-url)
FASTMCP_SERVER_AUTH_OCI_BASE_URL
required
Public URL where OAuth endpoints will be accessible (includes any mount path)
[​](https://gofastmcp.com/v2/integrations/oci#param-fastmcp-server-auth-oci-redirect-path)
FASTMCP_SERVER_AUTH_OCI_REDIRECT_PATH
default:"/auth/callback"
Redirect path configured in your OCI IAM Integrated Application
Example `.env` file:
Copy
```
# Use the OCI IAM provider
FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.oci.OCIProvider

# OCI IAM configuration and credentials
FASTMCP_SERVER_AUTH_OCI_IAM_GUID=idcs-asaacasd1111.....
FASTMCP_SERVER_AUTH_OCI_CONFIG_URL=https://{FASTMCP_SERVER_AUTH_OCI_IAM_GUID}.identity.oraclecloud.com/.well-known/openid-configuration
FASTMCP_SERVER_AUTH_OCI_CLIENT_ID=<your-client-id>
FASTMCP_SERVER_AUTH_OCI_CLIENT_SECRET=<your-client-secret>
FASTMCP_SERVER_AUTH_OCI_BASE_URL=https://your-server.com

```

With environment variables set, your server code simplifies to:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_access_token

# Authentication is automatically configured from environment
mcp = FastMCP(name="OCI Secured App")

@mcp.tool
def whoami() -> str:
    """The whoami function is to test MCP server without requiring token exchange.
    This tool can be used to test successful authentication against OCI IAM.
    It will return logged in user's subject (username from IAM domain)."""
    token = get_access_token()
    user = token.claims.get("sub")
    return f"You are User: {user}"

```

[ Google OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/v2/integrations/google)[ Scalekit 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/scalekit)
Ctrl+I
![OCI console showing the Edit Domain Settings button in the IAM Domain settings page](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocieditdomainsettingsbutton.png?w=840&fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=ac35f055a4def431abc642bda1a3f08d)
![OCI IAM Domain Settings](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocieditdomainsettings.png?w=840&fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=2aea4bdc7947eef4105fe42a82a349ad)
![Adding a Confidential Integrated Application in OCI IAM Domain](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ociaddapplication.png?w=840&fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=d8fcb00216ca7d4dc5c2294185e79957)
![OAuth Configuration for an Integrated Application in OCI IAM Domain](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocioauthconfiguration.png?w=840&fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=0eeb569886c184fd1e192fee120b06e1)
