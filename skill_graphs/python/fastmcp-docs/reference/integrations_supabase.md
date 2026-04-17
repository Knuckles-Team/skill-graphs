[Skip to main content](https://gofastmcp.com/integrations/supabase#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
Supabase 🤝 FastMCP
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
  * [Consent UI Requirement](https://gofastmcp.com/integrations/supabase#consent-ui-requirement)
  * [Configuration](https://gofastmcp.com/integrations/supabase#configuration)
  * [Prerequisites](https://gofastmcp.com/integrations/supabase#prerequisites)
  * [Step 1: Enable Supabase OAuth Server](https://gofastmcp.com/integrations/supabase#step-1-enable-supabase-oauth-server)
  * [Step 2: Get Supabase Project URL](https://gofastmcp.com/integrations/supabase#step-2-get-supabase-project-url)
  * [Step 3: FastMCP Configuration](https://gofastmcp.com/integrations/supabase#step-3-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/integrations/supabase#testing)
  * [Running the Server](https://gofastmcp.com/integrations/supabase#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/integrations/supabase#testing-with-a-client)
  * [Production Configuration](https://gofastmcp.com/integrations/supabase#production-configuration)


Auth
# Supabase 🤝 FastMCP
Copy page
Secure your FastMCP server with Supabase Auth
Copy page
`2.13.0` This guide shows you how to secure your FastMCP server using **Supabase Auth**. This integration uses the [**Remote OAuth**](https://gofastmcp.com/servers/auth/remote-oauth) pattern, where Supabase handles user authentication and your FastMCP server validates the tokens.
Supabase Auth does not currently support
##
[​](https://gofastmcp.com/integrations/supabase#consent-ui-requirement)
Consent UI Requirement
Supabase’s OAuth Server delegates the user consent screen to your application. When an MCP client initiates authorization, Supabase authenticates the user and then redirects to your application at a configured callback URL (e.g., `https://your-app.com/oauth/callback?authorization_id=...`). Your application must host a page that calls Supabase’s `approveAuthorization()` or `denyAuthorization()` APIs to complete the flow. `SupabaseProvider` handles the resource server side (token verification and metadata), but you are responsible for building and hosting the consent UI separately. See
##
[​](https://gofastmcp.com/integrations/supabase#configuration)
Configuration
###
[​](https://gofastmcp.com/integrations/supabase#prerequisites)
Prerequisites
Before you begin, you will need:
  1. A **Supabase Auth** instance
  2. **OAuth Server enabled** in your Supabase Dashboard (Authentication → OAuth Server)
  3. **Dynamic Client Registration enabled** in the same settings
  4. A **consent UI** hosted at your configured authorization path (see above)
  5. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/integrations/supabase#step-1-enable-supabase-oauth-server)
Step 1: Enable Supabase OAuth Server
In your Supabase Dashboard:
  1. Go to **Authentication → OAuth Server**
  2. Enable the **OAuth Server**
  3. Set your **Site URL** to where your consent UI is hosted
  4. Set the **Authorization Path** (e.g., `/oauth/callback`)
  5. Enable **Allow Dynamic OAuth Apps** for MCP client registration


###
[​](https://gofastmcp.com/integrations/supabase#step-2-get-supabase-project-url)
Step 2: Get Supabase Project URL
In your Supabase Dashboard:
  1. Go to **Project Settings**
  2. Copy your **Project URL** (e.g., `https://abc123.supabase.co`)


###
[​](https://gofastmcp.com/integrations/supabase#step-3-fastmcp-configuration)
Step 3: FastMCP Configuration
Create your FastMCP server using the `SupabaseProvider`:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.supabase import SupabaseProvider

auth = SupabaseProvider(
    project_url="https://abc123.supabase.co",
    base_url="http://localhost:8000",
)

mcp = FastMCP("Supabase Protected Server", auth=auth)

@mcp.tool
def protected_tool(message: str) -> str:
    """This tool requires authentication."""
    return f"Authenticated user says: {message}"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)

```

##
[​](https://gofastmcp.com/integrations/supabase#testing)
Testing
###
[​](https://gofastmcp.com/integrations/supabase#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

###
[​](https://gofastmcp.com/integrations/supabase#testing-with-a-client)
Testing with a Client
Create a test client that authenticates with your Supabase-protected server:
client.py
Copy
```
from fastmcp import Client
import asyncio

async def main():
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        print("Authenticated with Supabase!")

        result = await client.call_tool("protected_tool", {"message": "Hello!"})
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

```

When you run the client for the first time:
  1. Your browser will open to Supabase’s authorization endpoint
  2. After authenticating, Supabase redirects to your consent UI
  3. After you approve, the client receives the token and can make authenticated requests


##
[​](https://gofastmcp.com/integrations/supabase#production-configuration)
Production Configuration
For production deployments, load configuration from environment variables:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.supabase import SupabaseProvider

auth = SupabaseProvider(
    project_url=os.environ["SUPABASE_PROJECT_URL"],
    base_url=os.environ.get("BASE_URL", "https://your-server.com"),
)

mcp = FastMCP(name="Supabase Secured App", auth=auth)

```

[ Scalekit 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/scalekit)[ WorkOS 🤝 FastMCP Next ](https://gofastmcp.com/integrations/workos)
Ctrl+I
