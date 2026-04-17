[Skip to main content](https://gofastmcp.com/v2/integrations/supabase#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authentication
Supabase 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/v2/integrations/supabase#configuration)
  * [Prerequisites](https://gofastmcp.com/v2/integrations/supabase#prerequisites)
  * [Step 1: Get Supabase Project URL](https://gofastmcp.com/v2/integrations/supabase#step-1-get-supabase-project-url)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/v2/integrations/supabase#step-2-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/v2/integrations/supabase#testing)
  * [Running the Server](https://gofastmcp.com/v2/integrations/supabase#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/v2/integrations/supabase#testing-with-a-client)
  * [Environment Variables](https://gofastmcp.com/v2/integrations/supabase#environment-variables)
  * [Provider Selection](https://gofastmcp.com/v2/integrations/supabase#provider-selection)
  * [Supabase-Specific Configuration](https://gofastmcp.com/v2/integrations/supabase#supabase-specific-configuration)


Authentication
# Supabase 🤝 FastMCP
Copy page
Secure your FastMCP server with Supabase Auth
Copy page
`2.13.0` This guide shows you how to secure your FastMCP server using **Supabase Auth**. This integration uses the [**Remote OAuth**](https://gofastmcp.com/v2/servers/auth/remote-oauth) pattern, where Supabase handles user authentication and your FastMCP server validates the tokens.
##
[​](https://gofastmcp.com/v2/integrations/supabase#configuration)
Configuration
###
[​](https://gofastmcp.com/v2/integrations/supabase#prerequisites)
Prerequisites
Before you begin, you will need:
  1. A **Supabase Auth** instance
  2. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/v2/integrations/supabase#step-1-get-supabase-project-url)
Step 1: Get Supabase Project URL
In your Supabase Dashboard:
  1. Go to **Project Settings**
  2. Copy your **Project URL** (e.g., `https://abc123.supabase.co`)


###
[​](https://gofastmcp.com/v2/integrations/supabase#step-2-fastmcp-configuration)
Step 2: FastMCP Configuration
Create your FastMCP server using the `SupabaseProvider`:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.supabase import SupabaseProvider

# Configure Supabase Auth
auth = SupabaseProvider(
    project_url="https://abc123.supabase.co",
    base_url="http://localhost:8000",
    auth_route="/my/auth/route" # if self-hosting and using custom routes
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
[​](https://gofastmcp.com/v2/integrations/supabase#testing)
Testing
###
[​](https://gofastmcp.com/v2/integrations/supabase#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by Supabase authentication.
###
[​](https://gofastmcp.com/v2/integrations/supabase#testing-with-a-client)
Testing with a Client
Create a test client that authenticates with your Supabase-protected server:
client.py
Copy
```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle Supabase OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open Supabase login in your browser
        print("✓ Authenticated with Supabase!")

        # Test the protected tool
        result = await client.call_tool("protected_tool", {"message": "Hello!"})
        print(result)

if __name__ == "__main__":
    asyncio.run(main())

```

When you run the client for the first time:
  1. Your browser will open to Supabase’s authorization page
  2. After you authorize, you’ll be redirected back
  3. The client receives the token and can make authenticated requests


##
[​](https://gofastmcp.com/v2/integrations/supabase#environment-variables)
Environment Variables
For production deployments, use environment variables instead of hardcoding credentials.
###
[​](https://gofastmcp.com/v2/integrations/supabase#provider-selection)
Provider Selection
Setting this environment variable allows the Supabase provider to be used automatically without explicitly instantiating it in code.
[​](https://gofastmcp.com/v2/integrations/supabase#param-fastmcp-server-auth)
FASTMCP_SERVER_AUTH
default:"Not set"
Set to `fastmcp.server.auth.providers.supabase.SupabaseProvider` to use Supabase authentication.
###
[​](https://gofastmcp.com/v2/integrations/supabase#supabase-specific-configuration)
Supabase-Specific Configuration
These environment variables provide default values for the Supabase provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.
[​](https://gofastmcp.com/v2/integrations/supabase#param-fastmcp-server-auth-supabase-project-url)
FASTMCP_SERVER_AUTH_SUPABASE_PROJECT_URL
required
Your Supabase project URL (e.g., `https://abc123.supabase.co`)
[​](https://gofastmcp.com/v2/integrations/supabase#param-fastmcp-server-auth-supabase-base-url)
FASTMCP_SERVER_AUTH_SUPABASE_BASE_URL
required
Public URL of your FastMCP server (e.g., `https://your-server.com` or `http://localhost:8000` for development)
[​](https://gofastmcp.com/v2/integrations/supabase#param-fastmcp-server-auth-supabase-auth-route)
FASTMCP_SERVER_AUTH_SUPABASE_AUTH_ROUTE
default:"/auth/v1"
Your Supabase auth route (e.g., `/auth/v1`)
[​](https://gofastmcp.com/v2/integrations/supabase#param-fastmcp-server-auth-supabase-required-scopes)
FASTMCP_SERVER_AUTH_SUPABASE_REQUIRED_SCOPES
default:"[]"
Comma-, space-, or JSON-separated list of required OAuth scopes (e.g., `openid email` or `["openid", "email"]`)
Example `.env` file:
Copy
```
# Use the Supabase provider
FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.supabase.SupabaseProvider

# Supabase configuration
FASTMCP_SERVER_AUTH_SUPABASE_PROJECT_URL=https://abc123.supabase.co
FASTMCP_SERVER_AUTH_SUPABASE_BASE_URL=https://your-server.com
FASTMCP_SERVER_AUTH_SUPABASE_REQUIRED_SCOPES=openid,email

```

With environment variables set, your server code simplifies to:
server.py
Copy
```
from fastmcp import FastMCP

# Authentication is automatically configured from environment
mcp = FastMCP(name="Supabase Protected Server")

```

[ Scalekit 🤝 FastMCP Previous ](https://gofastmcp.com/v2/integrations/scalekit)[ WorkOS 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/workos)
Ctrl+I
