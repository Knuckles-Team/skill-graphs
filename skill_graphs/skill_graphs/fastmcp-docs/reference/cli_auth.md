[Skip to main content](https://gofastmcp.com/cli/auth#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
CLI
Auth Utilities
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
  * [Creating a CIMD](https://gofastmcp.com/cli/auth#creating-a-cimd)
  * [Options](https://gofastmcp.com/cli/auth#options)
  * [Example](https://gofastmcp.com/cli/auth#example)
  * [Validating a CIMD](https://gofastmcp.com/cli/auth#validating-a-cimd)


CLI
# Auth Utilities
Copy page
Create and validate CIMD documents for OAuth
Copy page
`3.0.0` The `fastmcp auth` commands help with CIMD (Client ID Metadata Document) management — part of MCP’s OAuth authentication flow. A CIMD is a JSON document you host at an HTTPS URL to identify your client application to MCP servers.
##
[​](https://gofastmcp.com/cli/auth#creating-a-cimd)
Creating a CIMD
`fastmcp auth cimd create` generates a CIMD document:
Copy
```
fastmcp auth cimd create \
  --name "My App" \
  --redirect-uri "http://localhost:*/callback"

```

Copy
```
{
  "client_id": "https://your-domain.com/oauth/client.json",
  "client_name": "My App",
  "redirect_uris": ["http://localhost:*/callback"],
  "token_endpoint_auth_method": "none"
}

```

The generated document includes a placeholder `client_id` — update it to match the URL where you’ll host the document before deploying.
###
[​](https://gofastmcp.com/cli/auth#options)
Options
Option | Flag | Description
---|---|---
Name | `--name` |  **Required.** Human-readable client name
Redirect URI | `--redirect-uri` |  **Required.** Allowed redirect URIs (repeatable)
Client URI | `--client-uri` | Client’s home page URL
Logo URI | `--logo-uri` | Client’s logo URL
Scope | `--scope` | Space-separated list of scopes
Output |  `--output`, `-o` | Save to file (default: stdout)
Pretty | `--pretty` | Pretty-print JSON (default: true)
###
[​](https://gofastmcp.com/cli/auth#example)
Example
Copy
```
fastmcp auth cimd create \
  --name "My Production App" \
  --redirect-uri "http://localhost:*/callback" \
  --redirect-uri "https://myapp.example.com/callback" \
  --client-uri "https://myapp.example.com" \
  --scope "read write" \
  --output client.json

```

##
[​](https://gofastmcp.com/cli/auth#validating-a-cimd)
Validating a CIMD
`fastmcp auth cimd validate` fetches a hosted CIMD and verifies it conforms to the spec:
Copy
```
fastmcp auth cimd validate https://myapp.example.com/oauth/client.json

```

The validator checks that the URL is valid (HTTPS, non-root path), the document is valid JSON, the `client_id` matches the URL, and no shared-secret auth methods are used. On success:
Copy
```
→ Fetching https://myapp.example.com/oauth/client.json...
✓ Valid CIMD document

Document details:
  client_id: https://myapp.example.com/oauth/client.json
  client_name: My App
  token_endpoint_auth_method: none
  redirect_uris:
    • http://localhost:*/callback

```

Option | Flag | Description
---|---|---
Timeout |  `--timeout`, `-t` | HTTP request timeout in seconds (default: 10)
[ Generate CLI Previous ](https://gofastmcp.com/cli/generate-cli)[ Upgrading from FastMCP 2 Next ](https://gofastmcp.com/getting-started/upgrading/from-fastmcp-2)
Ctrl+I
