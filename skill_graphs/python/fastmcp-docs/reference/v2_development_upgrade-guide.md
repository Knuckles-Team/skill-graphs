[Skip to main content](https://gofastmcp.com/v2/development/upgrade-guide#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Development
Upgrade Guide
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
  * [v2.14.0](https://gofastmcp.com/v2/development/upgrade-guide#v2-14-0)
  * [OpenAPI Parser Promotion](https://gofastmcp.com/v2/development/upgrade-guide#openapi-parser-promotion)
  * [Deprecated Features Removed](https://gofastmcp.com/v2/development/upgrade-guide#deprecated-features-removed)
  * [v2.13.0](https://gofastmcp.com/v2/development/upgrade-guide#v2-13-0)
  * [OAuth Token Key Management](https://gofastmcp.com/v2/development/upgrade-guide#oauth-token-key-management)


Development
# Upgrade Guide
Copy page
Migration instructions for upgrading between FastMCP versions
Copy page
This guide provides migration instructions for breaking changes and major updates when upgrading between FastMCP versions.
##
[​](https://gofastmcp.com/v2/development/upgrade-guide#v2-14-0)
v2.14.0
###
[​](https://gofastmcp.com/v2/development/upgrade-guide#openapi-parser-promotion)
OpenAPI Parser Promotion
The experimental OpenAPI parser is now the standard implementation. The legacy parser has been removed. **If you were using the legacy parser:** No code changes required. The new parser is a drop-in replacement with improved architecture. **If you were using the experimental parser:** Update your imports from the experimental module to the standard location:
Before
After
Copy
```
from fastmcp.experimental.server.openapi import FastMCPOpenAPI, RouteMap, MCPType

```

The experimental imports will continue working temporarily but will show deprecation warnings. The `FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER` environment variable is no longer needed and can be removed.
###
[​](https://gofastmcp.com/v2/development/upgrade-guide#deprecated-features-removed)
Deprecated Features Removed
The following deprecated features have been removed in v2.14.0: **BearerAuthProvider** (deprecated in v2.11):
Before
After
Copy
```
from fastmcp.server.auth.providers.bearer import BearerAuthProvider

```

**Context.get_http_request()** (deprecated in v2.2.11):
Before
After
Copy
```
request = context.get_http_request()

```

**Top-level Image import** (deprecated in v2.8.1):
Before
After
Copy
```
from fastmcp import Image

```

**FastMCP dependencies parameter** (deprecated in v2.11.4):
Before
After
Copy
```
mcp = FastMCP("server", dependencies=["requests", "pandas"])

```

**Legacy resource prefix format** : The `resource_prefix_format` parameter and “protocol” format have been removed. Only the “path” format is supported (this was already the default). **FastMCPProxy client parameter** :
Before
After
Copy
```
proxy = FastMCPProxy(client=my_client)

```

**output_schema=False** :
Before
After
Copy
```
@mcp.tool(output_schema=False)
def my_tool() -> str:
    return "result"

```

##
[​](https://gofastmcp.com/v2/development/upgrade-guide#v2-13-0)
v2.13.0
###
[​](https://gofastmcp.com/v2/development/upgrade-guide#oauth-token-key-management)
OAuth Token Key Management
The OAuth proxy now issues its own JWT tokens to clients instead of forwarding upstream provider tokens. This improves security by maintaining proper token audience boundaries. **What changed:** The OAuth proxy now implements a token factory pattern - it receives tokens from your OAuth provider (GitHub, Google, etc.), encrypts and stores them, then issues its own FastMCP JWT tokens to clients. This requires cryptographic keys for JWT signing and token encryption. **Default behavior (development):** By default, FastMCP automatically manages keys based on your platform:
  * **Mac/Windows** : Keys are auto-managed via system keyring, surviving server restarts with zero configuration. Suitable **only** for development and local testing.
  * **Linux** : Keys are ephemeral (random salt at startup, regenerated on each restart).

This works fine for development and testing where re-authentication after restart is acceptable. **For production:** Production deployments must provide explicit keys and use persistent storage. Add these three things:
Copy
```
auth = GitHubProvider(
    client_id=os.environ["GITHUB_CLIENT_ID"],
    client_secret=os.environ["GITHUB_CLIENT_SECRET"],
    base_url="https://your-server.com",

    # Explicit keys (required for production)
    jwt_signing_key=os.environ["JWT_SIGNING_KEY"],

    # Persistent network storage (required for production)
    client_storage=RedisStore(host="redis.example.com", port=6379)
)

```

**More information:**
  * [OAuth Token Security](https://gofastmcp.com/v2/deployment/http#oauth-token-security) - Complete production setup guide
  * [Key and Storage Management](https://gofastmcp.com/v2/servers/auth/oauth-proxy#key-and-storage-management) - Detailed explanation of defaults and production requirements
  * [OAuth Proxy Parameters](https://gofastmcp.com/v2/servers/auth/oauth-proxy#configuration-parameters) - Parameter documentation


[ Releases Previous ](https://gofastmcp.com/v2/development/releases)[ Changelog Next ](https://gofastmcp.com/v2/changelog)
Ctrl+I
