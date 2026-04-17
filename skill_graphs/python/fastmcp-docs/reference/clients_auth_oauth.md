[Skip to main content](https://gofastmcp.com/clients/auth/oauth#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Authentication
OAuth Authentication
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
    * [OAuth](https://gofastmcp.com/clients/auth/oauth)
    * [ CIMD NEW ](https://gofastmcp.com/clients/auth/cimd)
    * [Bearer Auth](https://gofastmcp.com/clients/auth/bearer)


##### Integrations
  * Auth
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
  * [Client Usage](https://gofastmcp.com/clients/auth/oauth#client-usage)
  * [Default Configuration](https://gofastmcp.com/clients/auth/oauth#default-configuration)
  * [OAuth Helper](https://gofastmcp.com/clients/auth/oauth#oauth-helper)
  * [OAuth Parameters](https://gofastmcp.com/clients/auth/oauth#oauth-parameters)
  * [OAuth Flow](https://gofastmcp.com/clients/auth/oauth#oauth-flow)
  * [Token Storage](https://gofastmcp.com/clients/auth/oauth#token-storage)
  * [CIMD Authentication](https://gofastmcp.com/clients/auth/oauth#cimd-authentication)
  * [Pre-Registered Clients](https://gofastmcp.com/clients/auth/oauth#pre-registered-clients)


Authentication
# OAuth Authentication
Copy page
Authenticate your FastMCP client via OAuth 2.1.
Copy page
`2.6.0`
OAuth authentication is only relevant for HTTP-based transports and requires user interaction via a web browser.
When your FastMCP client needs to access an MCP server protected by OAuth 2.1, and the process requires user interaction (like logging in and granting consent), you should use the Authorization Code Flow. FastMCP provides the `fastmcp.client.auth.OAuth` helper to simplify this entire process. This flow is common for user-facing applications where the application acts on behalf of the user.
##
[​](https://gofastmcp.com/clients/auth/oauth#client-usage)
Client Usage
###
[​](https://gofastmcp.com/clients/auth/oauth#default-configuration)
Default Configuration
The simplest way to use OAuth is to pass the string `"oauth"` to the `auth` parameter of the `Client` or transport instance. FastMCP will automatically configure the client to use OAuth with default settings:
Copy
```
from fastmcp import Client

# Uses default OAuth settings
async with Client("https://your-server.fastmcp.app/mcp", auth="oauth") as client:
    await client.ping()

```

###
[​](https://gofastmcp.com/clients/auth/oauth#oauth-helper)
`OAuth` Helper
To fully configure the OAuth flow, use the `OAuth` helper and pass it to the `auth` parameter of the `Client` or transport instance. `OAuth` manages the complexities of the OAuth 2.1 Authorization Code Grant with PKCE (Proof Key for Code Exchange) for enhanced security, and implements the full `httpx.Auth` interface.
Copy
```
from fastmcp import Client
from fastmcp.client.auth import OAuth

oauth = OAuth(scopes=["user"])

async with Client("https://your-server.fastmcp.app/mcp", auth=oauth) as client:
    await client.ping()

```

You don’t need to pass `mcp_url` when using `OAuth` with `Client(auth=...)` — the transport provides the server URL automatically.
####
[​](https://gofastmcp.com/clients/auth/oauth#oauth-parameters)
`OAuth` Parameters
  * **`scopes`**(`str | list[str]` , optional): OAuth scopes to request. Can be space-separated string or list of strings
  * **`client_name`**(`str` , optional): Client name for dynamic registration. Defaults to `"FastMCP Client"`
  * **`client_id`**(`str` , optional): Pre-registered OAuth client ID. When provided, skips Dynamic Client Registration entirely. See [Pre-Registered Clients](https://gofastmcp.com/clients/auth/oauth#pre-registered-clients)
  * **`client_secret`**(`str` , optional): OAuth client secret for pre-registered clients. Optional — public clients that rely on PKCE can omit this
  * **`client_metadata_url`**(`str` , optional): URL-based client identity (CIMD). See [CIMD Authentication](https://gofastmcp.com/clients/auth/cimd) for details
  * **`token_storage`**(`AsyncKeyValue` , optional): Storage backend for persisting OAuth tokens. Defaults to in-memory storage (tokens lost on restart). See [Token Storage](https://gofastmcp.com/clients/auth/oauth#token-storage) for encrypted storage options
  * **`additional_client_metadata`**(`dict[str, Any]` , optional): Extra metadata for client registration
  * **`callback_port`**(`int` , optional): Fixed port for OAuth callback server. If not specified, uses a random available port
  * **`httpx_client_factory`**(`McpHttpClientFactory` , optional): Factory for creating httpx clients


##
[​](https://gofastmcp.com/clients/auth/oauth#oauth-flow)
OAuth Flow
The OAuth flow is triggered when you use a FastMCP `Client` configured to use OAuth.
1
[](https://gofastmcp.com/clients/auth/oauth)
Token Check
The client first checks the configured `token_storage` backend for existing, valid tokens for the target server. If one is found, it will be used to authenticate the client.
2
[](https://gofastmcp.com/clients/auth/oauth)
OAuth Server Discovery
If no valid tokens exist, the client attempts to discover the OAuth server’s endpoints using a well-known URI (e.g., `/.well-known/oauth-authorization-server`) based on the `mcp_url`.
3
[](https://gofastmcp.com/clients/auth/oauth)
Client Registration
If a `client_id` is provided, the client uses those pre-registered credentials directly and skips this step entirely. Otherwise, if a `client_metadata_url` is configured and the server supports CIMD, the client uses its metadata URL as its identity. As a fallback, the client performs Dynamic Client Registration (RFC 7591) if the server supports it.
4
[](https://gofastmcp.com/clients/auth/oauth)
Local Callback Server
A temporary local HTTP server is started on an available port (or the port specified via `callback_port`). This server’s address (e.g., `http://127.0.0.1:<port>/callback`) acts as the `redirect_uri` for the OAuth flow.
5
[](https://gofastmcp.com/clients/auth/oauth)
Browser Interaction
The user’s default web browser is automatically opened, directing them to the OAuth server’s authorization endpoint. The user logs in and grants (or denies) the requested `scopes`.
6
[](https://gofastmcp.com/clients/auth/oauth)
Authorization Code & Token Exchange
Upon approval, the OAuth server redirects the user’s browser to the local callback server with an `authorization_code`. The client captures this code and exchanges it with the OAuth server’s token endpoint for an `access_token` (and often a `refresh_token`) using PKCE for security.
7
[](https://gofastmcp.com/clients/auth/oauth)
Token Caching
The obtained tokens are saved to the configured `token_storage` backend for future use, eliminating the need for repeated browser interactions.
8
[](https://gofastmcp.com/clients/auth/oauth)
Authenticated Requests
The access token is automatically included in the `Authorization` header for requests to the MCP server.
9
[](https://gofastmcp.com/clients/auth/oauth)
Refresh Token
If the access token expires, the client will automatically use the refresh token to get a new access token.
##
[​](https://gofastmcp.com/clients/auth/oauth#token-storage)
Token Storage
`2.13.0` By default, tokens are stored in memory and lost when your application restarts. For persistent storage, pass an `AsyncKeyValue`-compatible storage backend to the `token_storage` parameter.
**Security Consideration** : Use encrypted storage for production. MCP clients can accumulate OAuth credentials for many servers over time, and a compromised token store could expose access to multiple services.
Copy
```
from fastmcp import Client
from fastmcp.client.auth import OAuth
from key_value.aio.stores.disk import DiskStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet
import os

# Create encrypted disk storage
encrypted_storage = FernetEncryptionWrapper(
    key_value=DiskStore(directory="~/.fastmcp/oauth-tokens"),
    fernet=Fernet(os.environ["OAUTH_STORAGE_ENCRYPTION_KEY"])
)

oauth = OAuth(token_storage=encrypted_storage)

async with Client("https://your-server.fastmcp.app/mcp", auth=oauth) as client:
    await client.ping()

```

You can use any `AsyncKeyValue`-compatible backend from the `FernetEncryptionWrapper` for encryption.
When selecting a storage backend, review the
##
[​](https://gofastmcp.com/clients/auth/oauth#cimd-authentication)
CIMD Authentication
`3.0.0` Client ID Metadata Documents (CIMD) provide an alternative to Dynamic Client Registration. Instead of registering with each server, your client hosts a static JSON document at an HTTPS URL. That URL becomes your client’s identity, and servers can verify who you are through your domain ownership.
Copy
```
from fastmcp import Client
from fastmcp.client.auth import OAuth

async with Client(
    "https://mcp-server.example.com/mcp",
    auth=OAuth(
        client_metadata_url="https://myapp.example.com/oauth/client.json",
    ),
) as client:
    await client.ping()

```

See the [CIMD Authentication](https://gofastmcp.com/clients/auth/cimd) page for complete documentation on creating, hosting, and validating CIMD documents.
##
[​](https://gofastmcp.com/clients/auth/oauth#pre-registered-clients)
Pre-Registered Clients
`3.0.0` Some OAuth servers don’t support Dynamic Client Registration — the MCP spec explicitly makes DCR optional. If your client has been pre-registered with the server (you already have a `client_id` and optionally a `client_secret`), you can provide them directly to skip DCR entirely.
Copy
```
from fastmcp import Client
from fastmcp.client.auth import OAuth

async with Client(
    "https://mcp-server.example.com/mcp",
    auth=OAuth(
        client_id="my-registered-client-id",
        client_secret="my-client-secret",
    ),
) as client:
    await client.ping()

```

Public clients that rely on PKCE for security can omit `client_secret`:
Copy
```
oauth = OAuth(client_id="my-public-client-id")

```

When using pre-registered credentials, the client will not attempt Dynamic Client Registration. If the server rejects the credentials, the error is surfaced immediately rather than falling back to DCR.
[ Client Roots Previous ](https://gofastmcp.com/clients/roots)[ CIMD Authentication Next ](https://gofastmcp.com/clients/auth/cimd)
Ctrl+I
