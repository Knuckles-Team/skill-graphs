[Skip to main content](https://gofastmcp.com/clients/auth/cimd#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Authentication
CIMD Authentication
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
  * [Client Usage](https://gofastmcp.com/clients/auth/cimd#client-usage)
  * [Creating a CIMD Document](https://gofastmcp.com/clients/auth/cimd#creating-a-cimd-document)
  * [CLI Options](https://gofastmcp.com/clients/auth/cimd#cli-options)
  * [Redirect URIs](https://gofastmcp.com/clients/auth/cimd#redirect-uris)
  * [Hosting Requirements](https://gofastmcp.com/clients/auth/cimd#hosting-requirements)
  * [Validating Your Document](https://gofastmcp.com/clients/auth/cimd#validating-your-document)
  * [How It Works](https://gofastmcp.com/clients/auth/cimd#how-it-works)
  * [Server Configuration](https://gofastmcp.com/clients/auth/cimd#server-configuration)


Authentication
# CIMD Authentication
Copy page
Use Client ID Metadata Documents for verifiable, domain-based client identity.
Copy page
`3.0.0`
CIMD authentication is only relevant for HTTP-based transports and requires a server that advertises CIMD support.
With standard OAuth, your client registers dynamically with every server it connects to, receiving a fresh `client_id` each time. This works, but the server has no way to verify _who_ your client actually is — any client can claim any name during registration. CIMD (Client ID Metadata Documents) flips this around. You host a small JSON document at an HTTPS URL you control, and that URL becomes your `client_id`. When your client connects to a server, the server fetches your metadata document and can verify your identity through your domain ownership. Users see a verified domain badge in the consent screen instead of an unverified client name.
##
[​](https://gofastmcp.com/clients/auth/cimd#client-usage)
Client Usage
Pass your CIMD document URL to the `client_metadata_url` parameter of `OAuth`:
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

When the server supports CIMD, the client uses your metadata URL as its `client_id` instead of performing Dynamic Client Registration. The server fetches your document, validates it, and proceeds with the standard OAuth authorization flow.
You don’t need to pass `mcp_url` when using `OAuth` with `Client(auth=...)` — the transport provides the server URL automatically.
##
[​](https://gofastmcp.com/clients/auth/cimd#creating-a-cimd-document)
Creating a CIMD Document
A CIMD document is a JSON file that describes your client. The most important field is `client_id`, which must exactly match the URL where you host the document. Use the FastMCP CLI to generate one:
Copy
```
fastmcp auth cimd create \
    --name "My Application" \
    --redirect-uri "http://localhost:*/callback" \
    --client-id "https://myapp.example.com/oauth/client.json"

```

This produces:
Copy
```
{
  "client_id": "https://myapp.example.com/oauth/client.json",
  "client_name": "My Application",
  "redirect_uris": ["http://localhost:*/callback"],
  "token_endpoint_auth_method": "none",
  "grant_types": ["authorization_code"],
  "response_types": ["code"]
}

```

If you omit `--client-id`, the CLI generates a placeholder value and reminds you to update it before hosting.
###
[​](https://gofastmcp.com/clients/auth/cimd#cli-options)
CLI Options
The `create` command accepts these flags:
Flag | Description
---|---
`--name` | Human-readable client name (required)
`--redirect-uri`, `-r` | Allowed redirect URIs — can be specified multiple times (required)
`--client-id` | The URL where you’ll host this document (sets `client_id` directly)
`--output`, `-o` | Write to a file instead of stdout
`--scope` | Space-separated list of scopes the client may request
`--client-uri` | URL of the client’s home page
`--logo-uri` | URL of the client’s logo image
`--no-pretty` | Output compact JSON
###
[​](https://gofastmcp.com/clients/auth/cimd#redirect-uris)
Redirect URIs
The `redirect_uris` field supports wildcard port matching for localhost. The pattern `http://localhost:*/callback` matches any port, which is useful for development clients that bind to random available ports (which is what FastMCP’s `OAuth` helper does by default).
##
[​](https://gofastmcp.com/clients/auth/cimd#hosting-requirements)
Hosting Requirements
CIMD documents must be hosted at a publicly accessible HTTPS URL with a non-root path:
  * **HTTPS required** — HTTP URLs are rejected for security
  * **Non-root path** — The URL must have a path component (e.g., `/oauth/client.json`, not just `/`)
  * **Public accessibility** — The server must be able to fetch the document over the internet
  * **Matching`client_id`** — The `client_id` field in the document must exactly match the hosting URL

Common hosting options include static file hosting services like GitHub Pages, Cloudflare Pages, Vercel, or S3 — anywhere you can serve a JSON file over HTTPS.
##
[​](https://gofastmcp.com/clients/auth/cimd#validating-your-document)
Validating Your Document
Before deploying, verify your hosted document passes validation:
Copy
```
fastmcp auth cimd validate https://myapp.example.com/oauth/client.json

```

The validator fetches the document and checks that:
  * The URL is valid (HTTPS, non-root path)
  * The document is well-formed JSON conforming to the CIMD schema
  * The `client_id` in the document matches the URL it was fetched from


##
[​](https://gofastmcp.com/clients/auth/cimd#how-it-works)
How It Works
When your client connects to a CIMD-enabled server, the flow works like this:
1
[](https://gofastmcp.com/clients/auth/cimd)
Client Presents Metadata URL
Your client sends its `client_metadata_url` as the `client_id` in the OAuth authorization request.
2
[](https://gofastmcp.com/clients/auth/cimd)
Server Recognizes CIMD URL
The server sees that the `client_id` is an HTTPS URL with a path — the signature of a CIMD client — and skips Dynamic Client Registration.
3
[](https://gofastmcp.com/clients/auth/cimd)
Server Fetches and Validates
The server fetches your JSON document from the URL, validates that `client_id` matches the URL, and extracts your client metadata (name, redirect URIs, scopes).
4
[](https://gofastmcp.com/clients/auth/cimd)
Authorization Proceeds
The standard OAuth flow continues: browser opens for user consent, authorization code exchange, token issuance. The consent screen shows your verified domain.
The server caches your CIMD document according to HTTP cache headers, so subsequent requests don’t require re-fetching.
##
[​](https://gofastmcp.com/clients/auth/cimd#server-configuration)
Server Configuration
CIMD is a server-side feature that your MCP server must support. FastMCP’s OAuth proxy providers (GitHub, Google, Auth0, etc.) support CIMD by default. See the [OAuth Proxy CIMD documentation](https://gofastmcp.com/servers/auth/oauth-proxy#cimd-support) for server-side configuration, including private key JWT authentication and security details.
[ OAuth Authentication Previous ](https://gofastmcp.com/clients/auth/oauth)[ Bearer Token Authentication Next ](https://gofastmcp.com/clients/auth/bearer)
Ctrl+I
