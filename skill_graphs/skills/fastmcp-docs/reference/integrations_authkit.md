[Skip to main content](https://gofastmcp.com/integrations/authkit#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
AuthKit 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/integrations/authkit#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/authkit#prerequisites)
  * [Step 1: AuthKit Configuration](https://gofastmcp.com/integrations/authkit#step-1-authkit-configuration)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/integrations/authkit#step-2-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/integrations/authkit#testing)
  * [Production Configuration](https://gofastmcp.com/integrations/authkit#production-configuration)


Auth
# AuthKit 🤝 FastMCP
Copy page
Secure your FastMCP server with AuthKit by WorkOS
Copy page
`2.11.0` This guide shows you how to secure your FastMCP server using WorkOS’s **AuthKit** , a complete authentication and user management solution. This integration uses the [**Remote OAuth**](https://gofastmcp.com/servers/auth/remote-oauth) pattern, where AuthKit handles user login and your FastMCP server validates the tokens.
AuthKit does not currently support [WorkOSProvider](https://gofastmcp.com/integrations/workos) (OAuth proxy pattern) instead.
##
[​](https://gofastmcp.com/integrations/authkit#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/authkit#prerequisites)
Prerequisites
Before you begin, you will need:
  1. A **Project**.
  2. An
  3. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`).


###
[​](https://gofastmcp.com/integrations/authkit#step-1-authkit-configuration)
Step 1: AuthKit Configuration
In your WorkOS Dashboard, enable AuthKit and configure the following settings:
1
[](https://gofastmcp.com/integrations/authkit)
Enable Dynamic Client Registration
Go to **Applications → Configuration** and enable **Dynamic Client Registration**. This allows MCP clients register with your application automatically.![Enable Dynamic Client Registration](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/authkit/enable_dcr.png?fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=5849352618ef89da08cf452c5dcf38a8)
2
[](https://gofastmcp.com/integrations/authkit)
Note Your AuthKit Domain
Find your **AuthKit Domain** on the configuration page. It will look like `https://your-project-12345.authkit.app`. You’ll need this for your FastMCP server configuration.
###
[​](https://gofastmcp.com/integrations/authkit#step-2-fastmcp-configuration)
Step 2: FastMCP Configuration
Create your FastMCP server file and use the `AuthKitProvider` to handle all the OAuth integration automatically:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import AuthKitProvider

# The AuthKitProvider automatically discovers WorkOS endpoints
# and configures JWT token validation
auth_provider = AuthKitProvider(
    authkit_domain="https://your-project-12345.authkit.app",
    base_url="http://localhost:8000"  # Use your actual server URL
)

mcp = FastMCP(name="AuthKit Secured App", auth=auth_provider)

```

##
[​](https://gofastmcp.com/integrations/authkit#testing)
Testing
To test your server, you can use the `fastmcp` CLI to run it locally. Assuming you’ve saved the above code to `server.py` (after replacing the `authkit_domain` and `base_url` with your actual values!), you can run the following command:
Copy
```
fastmcp run server.py --transport http --port 8000

```

AuthKit defaults DCR clients to `client_secret_basic` for token exchange, which conflicts with how some MCP clients send credentials. To avoid token exchange errors, register as a public client by setting `token_endpoint_auth_method` to `"none"`:
client.py
Copy
```
from fastmcp import Client
from fastmcp.client.auth import OAuth
import asyncio

auth = OAuth(additional_client_metadata={"token_endpoint_auth_method": "none"})

async def main():
    async with Client("http://localhost:8000/mcp", auth=auth) as client:
        assert await client.ping()

if __name__ == "__main__":
    asyncio.run(main())

```

##
[​](https://gofastmcp.com/integrations/authkit#production-configuration)
Production Configuration
For production deployments, load sensitive configuration from environment variables:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.workos import AuthKitProvider

# Load configuration from environment variables
auth = AuthKitProvider(
    authkit_domain=os.environ.get("AUTHKIT_DOMAIN"),
    base_url=os.environ.get("BASE_URL", "https://your-server.com")
)

mcp = FastMCP(name="AuthKit Secured App", auth=auth)

```

[ Auth0 OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/auth0)[ AWS Cognito OAuth 🤝 FastMCP Next ](https://gofastmcp.com/integrations/aws-cognito)
Ctrl+I
![Enable Dynamic Client Registration](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/authkit/enable_dcr.png?w=840&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=26ba396eef845948a2bbe7405716a419)
