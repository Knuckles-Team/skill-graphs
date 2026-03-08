[Skip to main content](https://gofastmcp.com/integrations/discord#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
Discord OAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/integrations/discord#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/discord#prerequisites)
  * [Step 1: Create a Discord Application](https://gofastmcp.com/integrations/discord#step-1-create-a-discord-application)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/integrations/discord#step-2-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/integrations/discord#testing)
  * [Running the Server](https://gofastmcp.com/integrations/discord#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/integrations/discord#testing-with-a-client)
  * [Discord Scopes](https://gofastmcp.com/integrations/discord#discord-scopes)
  * [Production Configuration](https://gofastmcp.com/integrations/discord#production-configuration)


Auth
# Discord OAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with Discord OAuth
Copy page
`2.13.2` This guide shows you how to secure your FastMCP server using **Discord OAuth**. Since Discord doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/servers/auth/oauth-proxy) pattern to bridge Discord’s traditional OAuth with MCP’s authentication requirements.
##
[​](https://gofastmcp.com/integrations/discord#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/discord#prerequisites)
Prerequisites
Before you begin, you will need:
  1. A
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/integrations/discord#step-1-create-a-discord-application)
Step 1: Create a Discord Application
Create an application in the Discord Developer Portal to get the credentials needed for authentication:
1
[](https://gofastmcp.com/integrations/discord)
Navigate to Discord Developer Portal
Go to the Click **“New Application”** and give it a name users will recognize (e.g., “My FastMCP Server”).
2
[](https://gofastmcp.com/integrations/discord)
Configure OAuth2 Settings
In the left sidebar, click **“OAuth2”**.In the **Redirects** section, click **“Add Redirect”** and enter your callback URL:
  * For development: `http://localhost:8000/auth/callback`
  * For production: `https://your-domain.com/auth/callback`


The redirect URL must match exactly. The default path is `/auth/callback`, but you can customize it using the `redirect_path` parameter. Discord allows `http://localhost` URLs for development. For production, use HTTPS.
3
[](https://gofastmcp.com/integrations/discord)
Save Your Credentials
On the same OAuth2 page, you’ll find:
  * **Client ID** : A numeric string like `12345`
  * **Client Secret** : Click “Reset Secret” to generate one


Store these credentials securely. Never commit them to version control. Use environment variables or a secrets manager in production.
###
[​](https://gofastmcp.com/integrations/discord#step-2-fastmcp-configuration)
Step 2: FastMCP Configuration
Create your FastMCP server using the `DiscordProvider`, which handles Discord’s OAuth flow automatically:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.discord import DiscordProvider

auth_provider = DiscordProvider(
    client_id="12345",      # Your Discord Application Client ID
    client_secret="your-client-secret",    # Your Discord OAuth Client Secret
    base_url="http://localhost:8000",      # Must match your OAuth configuration
)

mcp = FastMCP(name="Discord Secured App", auth=auth_provider)

@mcp.tool
async def get_user_info() -> dict:
    """Returns information about the authenticated Discord user."""
    from fastmcp.server.dependencies import get_access_token

    token = get_access_token()
    return {
        "discord_id": token.claims.get("sub"),
        "username": token.claims.get("username"),
        "avatar": token.claims.get("avatar"),
    }

```

##
[​](https://gofastmcp.com/integrations/discord#testing)
Testing
###
[​](https://gofastmcp.com/integrations/discord#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by Discord OAuth authentication.
###
[​](https://gofastmcp.com/integrations/discord#testing-with-a-client)
Testing with a Client
Create a test client that authenticates with your Discord-protected server:
test_client.py
Copy
```
from fastmcp import Client
import asyncio

async def main():
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        print("✓ Authenticated with Discord!")

        result = await client.call_tool("get_user_info")
        print(f"Discord user: {result['username']}")

if __name__ == "__main__":
    asyncio.run(main())

```

When you run the client for the first time:
  1. Your browser will open to Discord’s authorization page
  2. Sign in with your Discord account and authorize the app
  3. After authorization, you’ll be redirected back
  4. The client receives the token and can make authenticated requests


The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.
##
[​](https://gofastmcp.com/integrations/discord#discord-scopes)
Discord Scopes
Discord OAuth supports several scopes for accessing different types of user data:
Scope | Description
---|---
`identify` | Access username, avatar, and discriminator (default)
`email` | Access the user’s email address
`guilds` | Access the user’s list of servers
`guilds.join` | Ability to add the user to a server
To request additional scopes:
Copy
```
auth_provider = DiscordProvider(
    client_id="...",
    client_secret="...",
    base_url="http://localhost:8000",
    required_scopes=["identify", "email"],
)

```

##
[​](https://gofastmcp.com/integrations/discord#production-configuration)
Production Configuration
For production deployments with persistent token management across server restarts, configure `jwt_signing_key` and `client_storage`:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.discord import DiscordProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

auth_provider = DiscordProvider(
    client_id="12345",
    client_secret=os.environ["DISCORD_CLIENT_SECRET"],
    base_url="https://your-production-domain.com",

    jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
    client_storage=FernetEncryptionWrapper(
        key_value=RedisStore(
            host=os.environ["REDIS_HOST"],
            port=int(os.environ["REDIS_PORT"])
        ),
        fernet=Fernet(os.environ["STORAGE_ENCRYPTION_KEY"])
    )
)

mcp = FastMCP(name="Production Discord App", auth=auth_provider)

```

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/servers/auth/oauth-proxy#configuration-parameters).
[ Descope 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/descope)[ Eunomia Authorization 🤝 FastMCP Next ](https://gofastmcp.com/integrations/eunomia-authorization)
Ctrl+I
