[Skip to main content](https://gofastmcp.com/servers/auth/full-oauth-server#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Authentication
Full OAuth Server
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
  * [OAuthProvider](https://gofastmcp.com/servers/auth/full-oauth-server#oauthprovider)
  * [Required Implementation](https://gofastmcp.com/servers/auth/full-oauth-server#required-implementation)
  * [Client Management](https://gofastmcp.com/servers/auth/full-oauth-server#client-management)
  * [Authorization Flow](https://gofastmcp.com/servers/auth/full-oauth-server#authorization-flow)
  * [Token Management](https://gofastmcp.com/servers/auth/full-oauth-server#token-management)


Authentication
# Full OAuth Server
Copy page
Build a self-contained authentication system where your FastMCP server manages users, issues tokens, and validates them.
Copy page
`2.11.0`
**This is an extremely advanced pattern that most users should avoid.** Building a secure OAuth 2.1 server requires deep expertise in authentication protocols, cryptography, and security best practices. The complexity extends far beyond initial implementation to include ongoing security monitoring, threat response, and compliance maintenance.**Use[Remote OAuth](https://gofastmcp.com/servers/auth/remote-oauth) instead** unless you have compelling requirements that external identity providers cannot meet, such as air-gapped environments or specialized compliance needs.
The Full OAuth Server pattern exists to support the MCP protocol specification’s requirements. Your FastMCP server becomes both an Authorization Server and Resource Server, handling the complete authentication lifecycle from user login to token validation. This documentation exists for completeness - the vast majority of applications should use external identity providers instead.
##
[​](https://gofastmcp.com/servers/auth/full-oauth-server#oauthprovider)
OAuthProvider
FastMCP provides the `OAuthProvider` abstract class that implements the OAuth 2.1 specification. To use this pattern, you must subclass `OAuthProvider` and implement all required abstract methods.
`OAuthProvider` handles OAuth endpoints, protocol flows, and security requirements, but delegates all storage, user management, and business logic to your implementation of the abstract methods.
##
[​](https://gofastmcp.com/servers/auth/full-oauth-server#required-implementation)
Required Implementation
You must implement these abstract methods to create a functioning OAuth server:
###
[​](https://gofastmcp.com/servers/auth/full-oauth-server#client-management)
Client Management
## Client Management Methods
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-get-client)
get_client
async method
Retrieve client information by ID from your database.
Show Parameters
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-id)
client_id
str
Client identifier to look up
Show Returns
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-o-auth-client-information-full-none)
OAuthClientInformationFull | None
return type
Client information object or `None` if client not found
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-register-client)
register_client
async method
Store new client registration information in your database.
Show Parameters
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-info)
client_info
OAuthClientInformationFull
Complete client registration information to store
Show Returns
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-none)
None
return type
No return value
###
[​](https://gofastmcp.com/servers/auth/full-oauth-server#authorization-flow)
Authorization Flow
## Authorization Flow Methods
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-authorize)
authorize
async method
Handle authorization request and return redirect URL. Must implement user authentication and consent collection.
Show Parameters
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client)
client
OAuthClientInformationFull
OAuth client making the authorization request
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-params)
params
AuthorizationParams
Authorization request parameters from the client
Show Returns
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-str)
str
return type
Redirect URL to send the client to
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-load-authorization-code)
load_authorization_code
async method
Load authorization code from storage by code string. Return `None` if code is invalid or expired.
Show Parameters
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-1)
client
OAuthClientInformationFull
OAuth client attempting to use the authorization code
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-authorization-code)
authorization_code
str
Authorization code string to look up
Show Returns
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-authorization-code-none)
AuthorizationCode | None
return type
Authorization code object or `None` if not found
###
[​](https://gofastmcp.com/servers/auth/full-oauth-server#token-management)
Token Management
## Token Management Methods
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-exchange-authorization-code)
exchange_authorization_code
async method
Exchange authorization code for access and refresh tokens. Must validate code and create new tokens.
Show Parameters
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-2)
client
OAuthClientInformationFull
OAuth client exchanging the authorization code
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-authorization-code-1)
authorization_code
AuthorizationCode
Valid authorization code object to exchange
Show Returns
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-o-auth-token)
OAuthToken
return type
New OAuth token containing access and refresh tokens
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-load-refresh-token)
load_refresh_token
async method
Load refresh token from storage by token string. Return `None` if token is invalid or expired.
Show Parameters
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-3)
client
OAuthClientInformationFull
OAuth client attempting to use the refresh token
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-refresh-token)
refresh_token
str
Refresh token string to look up
Show Returns
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-refresh-token-none)
RefreshToken | None
return type
Refresh token object or `None` if not found
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-exchange-refresh-token)
exchange_refresh_token
async method
Exchange refresh token for new access/refresh token pair. Must validate scopes and token.
Show Parameters
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-4)
client
OAuthClientInformationFull
OAuth client using the refresh token
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-refresh-token-1)
refresh_token
RefreshToken
Valid refresh token object to exchange
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-scopes)
scopes
list[str]
Requested scopes for the new access token
Show Returns
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-o-auth-token-1)
OAuthToken
return type
New OAuth token with updated access and refresh tokens
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-load-access-token)
load_access_token
async method
Load an access token by its token string.
Show Parameters
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-token)
token
str
The access token to verify
Show Returns
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-access-token-none)
AccessToken | None
return type
The access token object, or `None` if the token is invalid
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-revoke-token)
revoke_token
async method
Revoke access or refresh token, marking it as invalid in storage.
Show Parameters
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-token-1)
token
AccessToken | RefreshToken
Token object to revoke and mark invalid
Show Returns
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-none-1)
None
return type
No return value
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-verify-token)
verify_token
async method
Verify bearer token for incoming requests. Return `AccessToken` if valid, `None` if invalid.
Show Parameters
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-token-2)
token
str
Bearer token string from incoming request
Show Returns
[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-access-token-none-1)
AccessToken | None
return type
Access token object if valid, `None` if invalid or expired
Each method must handle storage, validation, security, and error cases according to the OAuth 2.1 specification. The implementation complexity is substantial and requires expertise in OAuth security considerations.
**Security Notice:** OAuth server implementation involves numerous security considerations including PKCE, state parameters, redirect URI validation, token binding, replay attack prevention, and secure storage requirements. Mistakes can lead to serious security vulnerabilities.
[ OIDC Proxy Previous ](https://gofastmcp.com/servers/auth/oidc-proxy)[ Multiple Auth Sources Next ](https://gofastmcp.com/servers/auth/multi-auth)
Ctrl+I
