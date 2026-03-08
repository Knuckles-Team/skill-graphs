[Skip to main content](https://gofastmcp.com/integrations/oci#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
OCI IAM OAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/integrations/oci#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/oci#prerequisites)
  * [Step 1: Make sure client access is enabled for JWK’s URL](https://gofastmcp.com/integrations/oci#step-1-make-sure-client-access-is-enabled-for-jwk%E2%80%99s-url)
  * [Step 2: Create OAuth client for MCP server authentication](https://gofastmcp.com/integrations/oci#step-2-create-oauth-client-for-mcp-server-authentication)
  * [Step 3: Token Exchange Setup (Only if MCP server needs to talk to OCI Control Plane)](https://gofastmcp.com/integrations/oci#step-3-token-exchange-setup-only-if-mcp-server-needs-to-talk-to-oci-control-plane)
  * [Running MCP server](https://gofastmcp.com/integrations/oci#running-mcp-server)
  * [Production Configuration](https://gofastmcp.com/integrations/oci#production-configuration)


Auth
# OCI IAM OAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with OCI IAM OAuth
Copy page
`2.13.0` This guide shows you how to secure your FastMCP server using **OCI IAM OAuth**. Since OCI IAM doesn’t support Dynamic Client Registration, this integration uses the [**OIDC Proxy**](https://gofastmcp.com/servers/auth/oidc-proxy) pattern to bridge OCI’s traditional OAuth with MCP’s authentication requirements.
##
[​](https://gofastmcp.com/integrations/oci#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/oci#prerequisites)
Prerequisites
  1. An OCI cloud Account with access to create an Integrated Application in an Identity Domain.
  2. Your FastMCP server’s URL (For dev environments, it is


###
[​](https://gofastmcp.com/integrations/oci#step-1-make-sure-client-access-is-enabled-for-jwk%E2%80%99s-url)
Step 1: Make sure client access is enabled for JWK’s URL
1
[](https://gofastmcp.com/integrations/oci)
Navigate to OCI IAM Domain Settings
Login to OCI console (
![OCI console showing the Edit Domain Settings button in the IAM Domain settings page](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocieditdomainsettingsbutton.png?fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=189e2e2c679c33b33a79164756cb6440)
2
[](https://gofastmcp.com/integrations/oci)
Update Domain Setting
Enable “Configure client access” checkbox as shown in the screenshot.
![OCI IAM Domain Settings](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocieditdomainsettings.png?fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=3f4422ba7b3c45fec724b4bb5de6ff31)
###
[​](https://gofastmcp.com/integrations/oci#step-2-create-oauth-client-for-mcp-server-authentication)
Step 2: Create OAuth client for MCP server authentication
Follow the Steps as mentioned below to create an OAuth client.
1
[](https://gofastmcp.com/integrations/oci)
Navigate to OCI IAM Integrated Applications
Login to OCI console (
2
[](https://gofastmcp.com/integrations/oci)
Add an Integrated Application
Select Add application. In the Add application window, select Confidential Application. Select Launch workflow. In the Add application details page, Enter name and description as shown below.
![Adding a Confidential Integrated Application in OCI IAM Domain](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ociaddapplication.png?fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=5855c5dc6cd69f8a0c53f3f103e7b4fc)
3
[](https://gofastmcp.com/integrations/oci)
Update OAuth Configuration for an Integrated Application
Once the Integrated Application is created, Click on “OAuth configuration” tab. Click on “Edit OAuth configuration” button. Configure the application as OAuth client by selecting “Configure this application as a client now” radio button. Select “Authorization code” grant type. If you are planning to use the same OAuth client application for token exchange, select “Client credentials” grant type as well. In the sample, we will use the same client. For Authorization grant type, select redirect URL. In most cases, this will be the MCP server URL followed by “/oauth/callback”.
![OAuth Configuration for an Integrated Application in OCI IAM Domain](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocioauthconfiguration.png?fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=885b0adc7c2a25ee71cf7e455b6afd62)
4
[](https://gofastmcp.com/integrations/oci)
Activate the Integrated Application
Click on “Submit” button to update OAuth configuration for the client application. **Note: You don’t need to do any special configuration to support PKCE for the OAuth client.** Make sure to Activate the client application. Note down client ID and client secret for the application. You’ll use these values when configuring the OCIProvider in your code.
This is all you need to implement MCP server authentication against OCI IAM. However, you may want to use an authenticated user token to invoke OCI control plane APIs and propagate identity to the OCI control plane instead of using a service user account. In that case, you need to implement token exchange.
###
[​](https://gofastmcp.com/integrations/oci#step-3-token-exchange-setup-only-if-mcp-server-needs-to-talk-to-oci-control-plane)
Step 3: Token Exchange Setup (Only if MCP server needs to talk to OCI Control Plane)
Token exchange helps you exchange a logged-in user’s OCI IAM token for an OCI control plane session token, also known as UPST (User Principal Session Token). To learn more about token exchange, refer to my  For token exchange, we need to configure Identity propagation trust. The blog above discusses setting up the trust using REST APIs. However, you can also use OCI CLI. Before using the CLI command below, ensure that you have created a token exchange OAuth client. In most cases, you can use the same OAuth client that you created above. Replace `<IAM_GUID>` and `<CLIENT_ID>` in the CLI command below with your actual values.
Copy
```
oci identity-domains identity-propagation-trust create \
--schemas '["urn:ietf:params:scim:schemas:oracle:idcs:IdentityPropagationTrust"]' \
--public-key-endpoint "https://<IAM_GUID>.identity.oraclecloud.com/admin/v1/SigningCert/jwk" \
--name "For Token Exchange" --type "JWT" \
--issuer "https://identity.oraclecloud.com/" --active true \
--endpoint "https://<IAM_GUID>.identity.oraclecloud.com" \
--subject-claim-name "sub" --allow-impersonation false \
--subject-mapping-attribute "username" \
--subject-type "User" --client-claim-name "iss" \
--client-claim-values '["https://identity.oraclecloud.com/"]' \
--oauth-clients '["<CLIENT_ID>"]'

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
OCI_IAM_GUID = os.environ.get("OCI_IAM_GUID")
OCI_CLIENT_ID = os.environ.get("OCI_CLIENT_ID")
OCI_CLIENT_SECRET = os.environ.get("OCI_CLIENT_SECRET")

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
        oci_domain_id=OCI_IAM_GUID.split(".")[0] if OCI_IAM_GUID else "",
        client_id=OCI_CLIENT_ID,
        client_secret=OCI_CLIENT_SECRET,
    )
    logger.debug(f"Signer {signer} created for token ID: {tokenID}")

    #Cache the signer object in memory cache
    _global_token_cache[tokenID] = signer
    logger.debug(f"Signer cached for token ID: {tokenID}")

    return signer

```

##
[​](https://gofastmcp.com/integrations/oci#running-mcp-server)
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
[​](https://gofastmcp.com/integrations/oci#production-configuration)
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
# Production setup with encrypted persistent token storage
auth_provider = OCIProvider(
    config_url=os.environ.get("OCI_CONFIG_URL"),
    client_id=os.environ.get("OCI_CLIENT_ID"),
    client_secret=os.environ.get("OCI_CLIENT_SECRET"),
    base_url=os.environ.get("BASE_URL", "https://your-production-domain.com"),

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

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at Rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/servers/auth/oauth-proxy#configuration-parameters).
The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.
[ Google OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/google)[ Permit.io Authorization 🤝 FastMCP Next ](https://gofastmcp.com/integrations/permit)
Ctrl+I
![OCI console showing the Edit Domain Settings button in the IAM Domain settings page](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocieditdomainsettingsbutton.png?w=840&fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=ac35f055a4def431abc642bda1a3f08d)
![OCI IAM Domain Settings](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocieditdomainsettings.png?w=840&fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=2aea4bdc7947eef4105fe42a82a349ad)
![Adding a Confidential Integrated Application in OCI IAM Domain](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ociaddapplication.png?w=840&fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=d8fcb00216ca7d4dc5c2294185e79957)
![OAuth Configuration for an Integrated Application in OCI IAM Domain](https://mintcdn.com/fastmcp/dDafRTA33FK_2khu/integrations/images/oci/ocioauthconfiguration.png?w=840&fit=max&auto=format&n=dDafRTA33FK_2khu&q=85&s=0eeb569886c184fd1e192fee120b06e1)
