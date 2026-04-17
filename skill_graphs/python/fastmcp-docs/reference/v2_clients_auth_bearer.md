[Skip to main content](https://gofastmcp.com/v2/clients/auth/bearer#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authentication
Bearer Token Authentication
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
    * [ OAuth NEW ](https://gofastmcp.com/v2/clients/auth/oauth)
    * [Bearer Auth](https://gofastmcp.com/v2/clients/auth/bearer)


##### Integrations
  * Authentication
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
  * [Client Usage](https://gofastmcp.com/v2/clients/auth/bearer#client-usage)
  * [BearerAuth Helper](https://gofastmcp.com/v2/clients/auth/bearer#bearerauth-helper)
  * [Custom Headers](https://gofastmcp.com/v2/clients/auth/bearer#custom-headers)


Authentication
# Bearer Token Authentication
Copy page
Authenticate your FastMCP client with a Bearer token.
Copy page
`2.6.0`
Bearer Token authentication is only relevant for HTTP-based transports.
You can configure your FastMCP client to use **bearer authentication** by supplying a valid access token. This is most appropriate for service accounts, long-lived API keys, CI/CD, applications where authentication is managed separately, or other non-interactive authentication methods. A Bearer token is a JSON Web Token (JWT) that is used to authenticate a request. It is most commonly used in the `Authorization` header of an HTTP request, using the `Bearer` scheme:
Copy
```
Authorization: Bearer <token>

```

##
[​](https://gofastmcp.com/v2/clients/auth/bearer#client-usage)
Client Usage
The most straightforward way to use a pre-existing Bearer token is to provide it as a string to the `auth` parameter of the `fastmcp.Client` or transport instance. FastMCP will automatically format it correctly for the `Authorization` header and bearer scheme.
If you’re using a string token, do not include the `Bearer` prefix. FastMCP will add it for you.
Copy
```
from fastmcp import Client

async with Client(
    "https://your-server.fastmcp.app/mcp",
    auth="<your-token>",
) as client:
    await client.ping()

```

You can also supply a Bearer token to a transport instance, such as `StreamableHttpTransport` or `SSETransport`:
Copy
```
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

transport = StreamableHttpTransport(
    "http://your-server.fastmcp.app/mcp",
    auth="<your-token>",
)

async with Client(transport) as client:
    await client.ping()

```

##
[​](https://gofastmcp.com/v2/clients/auth/bearer#bearerauth-helper)
`BearerAuth` Helper
If you prefer to be more explicit and not rely on FastMCP to transform your string token, you can use the `BearerAuth` class yourself, which implements the `httpx.Auth` interface.
Copy
```
from fastmcp import Client
from fastmcp.client.auth import BearerAuth

async with Client(
    "https://your-server.fastmcp.app/mcp",
    auth=BearerAuth(token="<your-token>"),
) as client:
    await client.ping()

```

##
[​](https://gofastmcp.com/v2/clients/auth/bearer#custom-headers)
Custom Headers
If the MCP server expects a custom header or token scheme, you can manually set the client’s `headers` instead of using the `auth` parameter by setting them on your transport:
Copy
```
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async with Client(
    transport=StreamableHttpTransport(
        "https://your-server.fastmcp.app/mcp",
        headers={"X-API-Key": "<your-token>"},
    ),
) as client:
    await client.ping()

```

[ OAuth Authentication Previous ](https://gofastmcp.com/v2/clients/auth/oauth)[ Auth0 OAuth 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/auth0)
Ctrl+I
