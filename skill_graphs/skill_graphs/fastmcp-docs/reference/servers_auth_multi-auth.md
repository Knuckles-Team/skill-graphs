[Skip to main content](https://gofastmcp.com/servers/auth/multi-auth#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Authentication
Multiple Auth Sources
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
    * [Overview](https://gofastmcp.com/servers/auth/authentication)
    * [Token Verification](https://gofastmcp.com/servers/auth/token-verification)
    * [Remote OAuth](https://gofastmcp.com/servers/auth/remote-oauth)
    * [ OAuth Proxy NEW ](https://gofastmcp.com/servers/auth/oauth-proxy)
    * [OIDC Proxy](https://gofastmcp.com/servers/auth/oidc-proxy)
    * [Full OAuth Server](https://gofastmcp.com/servers/auth/full-oauth-server)
    * [Multiple Auth Sources](https://gofastmcp.com/servers/auth/multi-auth)
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
  * [Understanding MultiAuth](https://gofastmcp.com/servers/auth/multi-auth#understanding-multiauth)
  * [Verification Order](https://gofastmcp.com/servers/auth/multi-auth#verification-order)
  * [Verifiers Only](https://gofastmcp.com/servers/auth/multi-auth#verifiers-only)
  * [API Reference](https://gofastmcp.com/servers/auth/multi-auth#api-reference)
  * [MultiAuth](https://gofastmcp.com/servers/auth/multi-auth#multiauth)


Authentication
# Multiple Auth Sources
Copy page
Accept tokens from multiple authentication sources with a single server.
Copy page
`3.1.0` Production servers often need to accept tokens from multiple authentication sources. An interactive application might authenticate through an OAuth proxy, while a backend service sends machine-to-machine JWT tokens directly. `MultiAuth` composes these sources into a single `auth` provider so every valid token is accepted regardless of where it was issued.
##
[​](https://gofastmcp.com/servers/auth/multi-auth#understanding-multiauth)
Understanding MultiAuth
`MultiAuth` wraps an optional auth server (like `OAuthProxy`) together with one or more token verifiers (like `JWTVerifier`). When a request arrives with a bearer token, `MultiAuth` tries each source in order and accepts the first successful verification. The auth server, if provided, is tried first. It owns all OAuth routes and metadata — the verifiers contribute only token verification logic. This keeps the MCP discovery surface clean: one set of routes, one set of metadata, multiple verification paths.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth import MultiAuth, OAuthProxy
from fastmcp.server.auth.providers.jwt import JWTVerifier

auth = MultiAuth(
    server=OAuthProxy(
        issuer_url="https://login.example.com/...",
        client_id="my-app",
        client_secret="secret",
        base_url="https://my-server.com",
    ),
    verifiers=[
        JWTVerifier(
            jwks_uri="https://internal-issuer.example.com/.well-known/jwks.json",
            issuer="https://internal-issuer.example.com",
            audience="my-mcp-server",
        ),
    ],
)

mcp = FastMCP("My Server", auth=auth)

```

Interactive MCP clients authenticate through the OAuth proxy as usual. Backend services skip OAuth entirely and send a JWT signed by the internal issuer. Both paths are validated, and the first match wins.
##
[​](https://gofastmcp.com/servers/auth/multi-auth#verification-order)
Verification Order
`MultiAuth` checks sources in a deterministic order:
  1. **Server** (if provided) — the full auth provider’s `verify_token` runs first
  2. **Verifiers** — each `TokenVerifier` is tried in list order

The first source that returns a valid `AccessToken` wins. If every source returns `None`, the request receives a 401 response. This ordering means the server acts as the “primary” authentication path, with verifiers as fallbacks for tokens the server doesn’t recognize.
##
[​](https://gofastmcp.com/servers/auth/multi-auth#verifiers-only)
Verifiers Only
You don’t always need a full OAuth server. If your server only needs to accept tokens from multiple issuers, pass verifiers without a server:
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth import MultiAuth
from fastmcp.server.auth.providers.jwt import JWTVerifier, StaticTokenVerifier

auth = MultiAuth(
    verifiers=[
        JWTVerifier(
            jwks_uri="https://issuer-a.example.com/.well-known/jwks.json",
            issuer="https://issuer-a.example.com",
            audience="my-server",
        ),
        JWTVerifier(
            jwks_uri="https://issuer-b.example.com/.well-known/jwks.json",
            issuer="https://issuer-b.example.com",
            audience="my-server",
        ),
    ],
)

mcp = FastMCP("Multi-Issuer Server", auth=auth)

```

Without a server, no OAuth routes or metadata are served. This is appropriate for internal systems where clients already know how to obtain tokens.
##
[​](https://gofastmcp.com/servers/auth/multi-auth#api-reference)
API Reference
###
[​](https://gofastmcp.com/servers/auth/multi-auth#multiauth)
MultiAuth
Parameter | Type | Description
---|---|---
`server` | `AuthProvider | None` | Optional auth provider that owns routes and OAuth metadata. Also tried first for token verification.
`verifiers` | `list[TokenVerifier] | TokenVerifier` | One or more token verifiers tried after the server.
`base_url` | `str | None` | Override the base URL. Defaults to the server’s `base_url`.
`required_scopes` | `list[str] | None` | Override required scopes. Defaults to the server’s scopes.
[ Full OAuth Server Previous ](https://gofastmcp.com/servers/auth/full-oauth-server)[ Authorization Next ](https://gofastmcp.com/servers/authorization)
Ctrl+I
