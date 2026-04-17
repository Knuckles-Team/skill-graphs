[Skip to main content](https://gofastmcp.com/v2/servers/auth/oidc-proxy#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authentication
OIDC Proxy
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
    * [Overview](https://gofastmcp.com/v2/servers/auth/authentication)
    * [Token Verification](https://gofastmcp.com/v2/servers/auth/token-verification)
    * [ Remote OAuth NEW ](https://gofastmcp.com/v2/servers/auth/remote-oauth)
    * [ OAuth Proxy NEW ](https://gofastmcp.com/v2/servers/auth/oauth-proxy)
    * [ OIDC Proxy NEW ](https://gofastmcp.com/v2/servers/auth/oidc-proxy)
    * [Full OAuth Server](https://gofastmcp.com/v2/servers/auth/full-oauth-server)
  * Deployment


##### Clients
  * Essentials
  * Core Operations
  * Advanced Features
  * Authentication


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
  * [Implementation](https://gofastmcp.com/v2/servers/auth/oidc-proxy#implementation)
  * [Provider Setup Requirements](https://gofastmcp.com/v2/servers/auth/oidc-proxy#provider-setup-requirements)
  * [Basic Setup](https://gofastmcp.com/v2/servers/auth/oidc-proxy#basic-setup)
  * [Configuration Parameters](https://gofastmcp.com/v2/servers/auth/oidc-proxy#configuration-parameters)
  * [Using Built-in Providers](https://gofastmcp.com/v2/servers/auth/oidc-proxy#using-built-in-providers)
  * [Scope Configuration](https://gofastmcp.com/v2/servers/auth/oidc-proxy#scope-configuration)
  * [Environment Configuration](https://gofastmcp.com/v2/servers/auth/oidc-proxy#environment-configuration)


Authentication
# OIDC Proxy
Copy page
Bridge OIDC providers to work seamlessly with MCP’s authentication flow.
Copy page
`2.12.4` The OIDC proxy enables FastMCP servers to authenticate with OIDC providers that **don’t support Dynamic Client Registration (DCR)** out of the box. This includes OAuth providers like: Auth0, Google, Azure, AWS, etc. For providers that do support DCR (like WorkOS AuthKit), use [`RemoteAuthProvider`](https://gofastmcp.com/v2/servers/auth/remote-oauth) instead. The OIDC proxy is built upon [`OAuthProxy`](https://gofastmcp.com/v2/servers/auth/oauth-proxy) so it has all the same functionality under the covers.
##
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#implementation)
Implementation
###
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#provider-setup-requirements)
Provider Setup Requirements
Before using the OIDC proxy, you need to register your application with your OAuth provider:
  1. **Register your application** in the provider’s developer console (Auth0 Applications, Google Cloud Console, Azure Portal, etc.)
  2. **Configure the redirect URI** as your FastMCP server URL plus your chosen callback path:
     * Default: `https://your-server.com/auth/callback`
     * Custom: `https://your-server.com/your/custom/path` (if you set `redirect_path`)
     * Development: `http://localhost:8000/auth/callback`
  3. **Obtain your credentials** : Client ID and Client Secret


The redirect URI you configure with your provider must exactly match your FastMCP server’s URL plus the callback path. If you customize `redirect_path` in the OIDC proxy, update your provider’s redirect URI accordingly.
###
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#basic-setup)
Basic Setup
Here’s how to implement the OIDC proxy with any provider:
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.oidc_proxy import OIDCProxy

# Create the OIDC proxy
auth = OIDCProxy(
    # Provider's configuration URL
    config_url="https://provider.com/.well-known/openid-configuration",

    # Your registered app credentials
    client_id="your-client-id",
    client_secret="your-client-secret",

    # Your FastMCP server's public URL
    base_url="https://your-server.com",

    # Optional: customize the callback path (default is "/auth/callback")
    # redirect_path="/custom/callback",
)

mcp = FastMCP(name="My Server", auth=auth)

```

###
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#configuration-parameters)
Configuration Parameters
## OIDCProxy Parameters
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-config-url)
config_url
str
required
URL of your OAuth provider’s OIDC configuration
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-client-id)
client_id
str
required
Client ID from your registered OAuth application
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-client-secret)
client_secret
str
required
Client secret from your registered OAuth application
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-base-url)
base_url
AnyHttpUrl | str
required
Public URL of your FastMCP server (e.g., `https://your-server.com`)
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-strict)
strict
bool | None
Strict flag for configuration validation. When True, requires all OIDC mandatory fields.
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-audience)
audience
str | None
Audience parameter for OIDC providers that require it (e.g., Auth0). This is typically your API identifier.
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-timeout-seconds)
timeout_seconds
int | None
default:"10"
HTTP request timeout in seconds for fetching OIDC configuration
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-token-verifier)
token_verifier
TokenVerifier | None
`2.13.1`Custom token verifier for validating tokens. When provided, FastMCP uses your custom verifier instead of creating a default `JWTVerifier`.Cannot be used with `algorithm` or `required_scopes` parameters - configure these on your verifier instead. The verifier’s `required_scopes` are automatically loaded and advertised.
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-algorithm)
algorithm
str | None
JWT algorithm to use for token verification (e.g., “RS256”). If not specified, uses the provider’s default. Only used when `token_verifier` is not provided.
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-required-scopes)
required_scopes
list[str] | None
List of OAuth scopes for token validation. These are automatically included in authorization requests. Only used when `token_verifier` is not provided.
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-redirect-path)
redirect_path
str
default:"/auth/callback"
Path for OAuth callbacks. Must match the redirect URI configured in your OAuth application
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-allowed-client-redirect-uris)
allowed_client_redirect_uris
list[str] | None
List of allowed redirect URI patterns for MCP clients. Patterns support wildcards (e.g., `"http://localhost:*"`, `"https://*.example.com/*"`).
  * `None` (default): All redirect URIs allowed (for MCP/DCR compatibility)
  * Empty list `[]`: No redirect URIs allowed
  * Custom list: Only matching patterns allowed

These patterns apply to MCP client loopback redirects, NOT the upstream OAuth app redirect URI.
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-token-endpoint-auth-method)
token_endpoint_auth_method
str | None
Token endpoint authentication method for the upstream OAuth server. Controls how the proxy authenticates when exchanging authorization codes and refresh tokens with the upstream provider.
  * `"client_secret_basic"`: Send credentials in Authorization header (most common)
  * `"client_secret_post"`: Send credentials in request body (required by some providers)
  * `"none"`: No authentication (for public clients)
  * `None` (default): Uses authlib’s default (typically `"client_secret_basic"`)

Set this if your provider requires a specific authentication method and the default doesn’t work.
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-jwt-signing-key)
jwt_signing_key
str | bytes | None
`2.13.0`Secret used to sign FastMCP JWT tokens issued to clients. Accepts any string or bytes - will be derived into a proper 32-byte cryptographic key using HKDF.**Default behavior (`None`):**
  * **Mac/Windows** : Auto-managed via system keyring. Keys are generated once and persisted, surviving server restarts with zero configuration. Keys are automatically derived from server attributes, so this approach, while convenient, is **only** suitable for development and local testing. For production, you must provide an explicit secret.
  * **Linux** : Ephemeral (random salt at startup). Tokens become invalid on server restart, triggering client re-authentication.

**For production:** Provide an explicit secret (e.g., from environment variable) to use a fixed key instead of the auto-generated one.
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-client-storage)
client_storage
AsyncKeyValue | None
`2.13.0`Storage backend for persisting OAuth client registrations and upstream tokens.**Default behavior:**
  * **Mac/Windows** : Encrypted DiskStore in your platform’s data directory (derived from `platformdirs`)
  * **Linux** : MemoryStore (ephemeral - clients lost on restart)

By default on Mac/Windows, clients are automatically persisted to encrypted disk storage, allowing them to survive server restarts as long as the filesystem remains accessible. This means MCP clients only need to register once and can reconnect seamlessly. On Linux where keyring isn’t available, ephemeral storage is used to match the ephemeral key strategy.For production deployments with multiple servers or cloud deployments, use a network-accessible storage backend rather than local disk storage. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest.** See [Storage Backends](https://gofastmcp.com/v2/servers/storage-backends) for available options.Testing with in-memory storage (unencrypted):
Copy
```
from key_value.aio.stores.memory import MemoryStore

# Use in-memory storage for testing (clients lost on restart)
auth = OIDCProxy(..., client_storage=MemoryStore())

```

Production with encrypted Redis storage:
Copy
```
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet
import os

auth = OIDCProxy(
    ...,
    jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
    client_storage=FernetEncryptionWrapper(
        key_value=RedisStore(host="redis.example.com", port=6379),
        fernet=Fernet(os.environ["STORAGE_ENCRYPTION_KEY"])
    )
)

```

[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-require-authorization-consent)
require_authorization_consent
bool
default:"True"
Whether to require user consent before authorizing MCP clients. When enabled (default), users see a consent screen that displays which client is requesting access. See [OAuthProxy documentation](https://gofastmcp.com/v2/servers/auth/oauth-proxy#confused-deputy-attacks) for details on confused deputy attack protection.
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#param-consent-csp-policy)
consent_csp_policy
str | None
default:"None"
Content Security Policy for the consent page.
  * `None` (default): Uses the built-in CSP policy with appropriate directives for form submission
  * Empty string `""`: Disables CSP entirely (no meta tag rendered)
  * Custom string: Uses the provided value as the CSP policy

This is useful for organizations that have their own CSP policies and need to override or disable FastMCP’s built-in CSP directives.
###
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#using-built-in-providers)
Using Built-in Providers
FastMCP includes pre-configured OIDC providers for common services:
Copy
```
from fastmcp.server.auth.providers.auth0 import Auth0Provider

auth = Auth0Provider(
    config_url="https://.../.well-known/openid-configuration",
    client_id="your-auth0-client-id",
    client_secret="your-auth0-client-secret",
    audience="https://...",
    base_url="https://localhost:8000"
)

mcp = FastMCP(name="My Server", auth=auth)

```

Available providers include `Auth0Provider` at present.
###
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#scope-configuration)
Scope Configuration
OAuth scopes are configured with `required_scopes` to automatically request the permissions your application needs. Dynamic clients created by the proxy will automatically include these scopes in their authorization requests.
##
[​](https://gofastmcp.com/v2/servers/auth/oidc-proxy#environment-configuration)
Environment Configuration
`2.13.0` For production deployments, configure the OIDC proxy through environment variables instead of hardcoding credentials:
Copy
```
# Specify the provider implementation
export FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.auth0.Auth0Provider

# Provider-specific credentials
export FASTMCP_SERVER_AUTH_AUTH0_CONFIG_URL=https://.../.well-known/openid-configuration
export FASTMCP_SERVER_AUTH_AUTH0_CLIENT_ID=tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB
export FASTMCP_SERVER_AUTH_AUTH0_CLIENT_SECRET=vPYqbjemq...
export FASTMCP_SERVER_AUTH_AUTH0_AUDIENCE=https://...
export FASTMCP_SERVER_AUTH_AUTH0_BASE_URL=https://localhost:8000

```

With environment configuration, your server code simplifies to:
Copy
```
from fastmcp import FastMCP

# Authentication automatically configured from environment
mcp = FastMCP(name="My Server")

@mcp.tool
def protected_tool(data: str) -> str:
    """This tool is now protected by OAuth."""
    return f"Processed: {data}"

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)

```

[ OAuth Proxy Previous ](https://gofastmcp.com/v2/servers/auth/oauth-proxy)[ Full OAuth Server Next ](https://gofastmcp.com/v2/servers/auth/full-oauth-server)
Ctrl+I
