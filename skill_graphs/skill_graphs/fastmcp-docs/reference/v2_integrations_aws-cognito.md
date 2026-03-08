[Skip to main content](https://gofastmcp.com/v2/integrations/aws-cognito#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Authentication
AWS Cognito OAuth 🤝 FastMCP
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
  * [Configuration](https://gofastmcp.com/v2/integrations/aws-cognito#configuration)
  * [Prerequisites](https://gofastmcp.com/v2/integrations/aws-cognito#prerequisites)
  * [Step 1: Create an AWS Cognito User Pool and App Client](https://gofastmcp.com/v2/integrations/aws-cognito#step-1-create-an-aws-cognito-user-pool-and-app-client)
  * [Step 2: FastMCP Configuration](https://gofastmcp.com/v2/integrations/aws-cognito#step-2-fastmcp-configuration)
  * [Testing](https://gofastmcp.com/v2/integrations/aws-cognito#testing)
  * [Running the Server](https://gofastmcp.com/v2/integrations/aws-cognito#running-the-server)
  * [Testing with a Client](https://gofastmcp.com/v2/integrations/aws-cognito#testing-with-a-client)
  * [Production Configuration](https://gofastmcp.com/v2/integrations/aws-cognito#production-configuration)
  * [Environment Variables](https://gofastmcp.com/v2/integrations/aws-cognito#environment-variables)
  * [Provider Selection](https://gofastmcp.com/v2/integrations/aws-cognito#provider-selection)
  * [AWS Cognito-Specific Configuration](https://gofastmcp.com/v2/integrations/aws-cognito#aws-cognito-specific-configuration)
  * [Features](https://gofastmcp.com/v2/integrations/aws-cognito#features)
  * [JWT Token Validation](https://gofastmcp.com/v2/integrations/aws-cognito#jwt-token-validation)
  * [User Claims and Groups](https://gofastmcp.com/v2/integrations/aws-cognito#user-claims-and-groups)
  * [Enterprise Integration](https://gofastmcp.com/v2/integrations/aws-cognito#enterprise-integration)


Authentication
# AWS Cognito OAuth 🤝 FastMCP
Copy page
Secure your FastMCP server with AWS Cognito user pools
Copy page
`2.12.4` This guide shows you how to secure your FastMCP server using **AWS Cognito user pools**. Since AWS Cognito doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/v2/servers/auth/oauth-proxy) pattern to bridge AWS Cognito’s traditional OAuth with MCP’s authentication requirements. It also includes robust JWT token validation, ensuring enterprise-grade authentication.
##
[​](https://gofastmcp.com/v2/integrations/aws-cognito#configuration)
Configuration
###
[​](https://gofastmcp.com/v2/integrations/aws-cognito#prerequisites)
Prerequisites
Before you begin, you will need:
  1. An
  2. Basic familiarity with AWS Cognito concepts (user pools, app clients)
  3. Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)


###
[​](https://gofastmcp.com/v2/integrations/aws-cognito#step-1-create-an-aws-cognito-user-pool-and-app-client)
Step 1: Create an AWS Cognito User Pool and App Client
Set up AWS Cognito user pool with an app client to get the credentials needed for authentication:
1
[](https://gofastmcp.com/v2/integrations/aws-cognito)
Navigate to AWS Cognito
Go to the Select **“User pools”** from the side navigation (click on the hamburger icon at the top left in case you don’t see any), and click **“Create user pool”** to create a new user pool.
2
[](https://gofastmcp.com/v2/integrations/aws-cognito)
Define Your Application
AWS Cognito now provides a streamlined setup experience:
  1. **Application type** : Select **“Traditional web application”** (this is the correct choice for FastMCP server-side authentication)
  2. **Name your application** : Enter a descriptive name (e.g., `FastMCP Server`)

The traditional web application type automatically configures:
  * Server-side authentication with client secrets
  * Authorization code grant flow
  * Appropriate security settings for confidential clients


Choose “Traditional web application” rather than SPA, Mobile app, or Machine-to-machine options. This ensures proper OAuth 2.0 configuration for FastMCP.
3
[](https://gofastmcp.com/v2/integrations/aws-cognito)
Configure Options
AWS will guide you through configuration options:
  * **Sign-in identifiers** : Choose how users will sign in (email, username, or phone)
  * **Required attributes** : Select any additional user information you need
  * **Return URL** : Add your callback URL (e.g., `http://localhost:8000/auth/callback` for development)


The simplified interface handles most OAuth security settings automatically based on your application type selection.
4
[](https://gofastmcp.com/v2/integrations/aws-cognito)
Review and Create
Review your configuration and click **“Create user pool”**.After creation, you’ll see your user pool details. Save these important values:
  * **User pool ID** (format: `eu-central-1_XXXXXXXXX`)
  * **Client ID** (found under → “Applications” → “App clients” in the side navigation → <Your application name, e.g., `FastMCP Server`> → “App client information”)
  * **Client Secret** (found under → “Applications” → “App clients” in the side navigation → <Your application name, e.g., `FastMCP Server`> → “App client information”)


The user pool ID and app client credentials are all you need for FastMCP configuration.
5
[](https://gofastmcp.com/v2/integrations/aws-cognito)
Configure OAuth Settings
Under “Login pages” in your app client’s settings, you can double check and adjust the OAuth configuration:
  * **Allowed callback URLs** : Add your server URL + `/auth/callback` (e.g., `http://localhost:8000/auth/callback`)
  * **Allowed sign-out URLs** : Optional, for logout functionality
  * **OAuth 2.0 grant types** : Ensure “Authorization code grant” is selected
  * **OpenID Connect scopes** : Select scopes your application needs (e.g., `openid`, `email`, `profile`)


For local development, you can use `http://localhost` URLs. For production, you must use HTTPS.
6
[](https://gofastmcp.com/v2/integrations/aws-cognito)
Configure Resource Server
AWS Cognito requires a resource server entry to support OAuth with protected resources. Without this, token exchange will fail with an `invalid_grant` error.Navigate to **“Branding” → “Domain”** in the side navigation, then:
  1. Click **“Create resource server”**
  2. **Resource server name** : Enter a descriptive name (e.g., `My MCP Server`)
  3. **Resource server identifier** : Enter your MCP endpoint URL exactly as it will be accessed (e.g., `http://localhost:8000/mcp` for development, or `https://your-server.com/mcp` for production)
  4. Click **“Create resource server”**


The resource server identifier must exactly match your `base_url + mcp_path`. For the default configuration with `base_url="http://localhost:8000"` and `path="/mcp"`, use `http://localhost:8000/mcp`.
7
[](https://gofastmcp.com/v2/integrations/aws-cognito)
Save Your Credentials
After setup, you’ll have:
  * **User Pool ID** : Format like `eu-central-1_XXXXXXXXX`
  * **Client ID** : Your application’s client identifier
  * **Client Secret** : Generated client secret (keep secure)
  * **AWS Region** : Where Your AWS Cognito user pool is located


Store these credentials securely. Never commit them to version control. Use environment variables or AWS Secrets Manager in production.
###
[​](https://gofastmcp.com/v2/integrations/aws-cognito#step-2-fastmcp-configuration)
Step 2: FastMCP Configuration
Create your FastMCP server using the `AWSCognitoProvider`, which handles AWS Cognito’s JWT tokens and user claims automatically:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.auth.providers.aws import AWSCognitoProvider
from fastmcp.server.dependencies import get_access_token

# The AWSCognitoProvider handles JWT validation and user claims
auth_provider = AWSCognitoProvider(
    user_pool_id="eu-central-1_XXXXXXXXX",   # Your AWS Cognito user pool ID
    aws_region="eu-central-1",               # AWS region (defaults to eu-central-1)
    client_id="your-app-client-id",          # Your app client ID
    client_secret="your-app-client-secret",  # Your app client Secret
    base_url="http://localhost:8000",        # Must match your callback URL
    # redirect_path="/auth/callback"         # Default value, customize if needed
)

mcp = FastMCP(name="AWS Cognito Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_access_token_claims() -> dict:
    """Get the authenticated user's access token claims."""
    token = get_access_token()
    return {
        "sub": token.claims.get("sub"),
        "username": token.claims.get("username"),
        "cognito:groups": token.claims.get("cognito:groups", []),
    }

```

##
[​](https://gofastmcp.com/v2/integrations/aws-cognito#testing)
Testing
###
[​](https://gofastmcp.com/v2/integrations/aws-cognito#running-the-server)
Running the Server
Start your FastMCP server with HTTP transport to enable OAuth flows:
Copy
```
fastmcp run server.py --transport http --port 8000

```

Your server is now running and protected by AWS Cognito OAuth authentication.
###
[​](https://gofastmcp.com/v2/integrations/aws-cognito#testing-with-a-client)
Testing with a Client
Create a test client that authenticates with Your AWS Cognito-protected server:
test_client.py
Copy
```
from fastmcp import Client
import asyncio

async def main():
    # The client will automatically handle AWS Cognito OAuth
    async with Client("http://localhost:8000/mcp", auth="oauth") as client:
        # First-time connection will open AWS Cognito login in your browser
        print("✓ Authenticated with AWS Cognito!")

        # Test the protected tool
        print("Calling protected tool: get_access_token_claims")
        result = await client.call_tool("get_access_token_claims")
        user_data = result.data
        print("Available access token claims:")
        print(f"- sub: {user_data.get('sub', 'N/A')}")
        print(f"- username: {user_data.get('username', 'N/A')}")
        print(f"- cognito:groups: {user_data.get('cognito:groups', [])}")

if __name__ == "__main__":
    asyncio.run(main())

```

When you run the client for the first time:
  1. Your browser will open to AWS Cognito’s hosted UI login page
  2. After you sign in (or sign up), you’ll be redirected back to your MCP server
  3. The client receives the JWT token and can make authenticated requests


The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.
##
[​](https://gofastmcp.com/v2/integrations/aws-cognito#production-configuration)
Production Configuration
`2.13.0` For production deployments with persistent token management across server restarts, configure `jwt_signing_key`, and `client_storage`:
server.py
Copy
```
import os
from fastmcp import FastMCP
from fastmcp.server.auth.providers.aws import AWSCognitoProvider
from key_value.aio.stores.redis import RedisStore
from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
from cryptography.fernet import Fernet

# Production setup with encrypted persistent token storage
auth_provider = AWSCognitoProvider(
    user_pool_id="eu-central-1_XXXXXXXXX",
    aws_region="eu-central-1",
    client_id="your-app-client-id",
    client_secret="your-app-client-secret",
    base_url="https://your-production-domain.com",

    # Production token management
    jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
    client_storage=FernetEncryptionWrapper(
        key_value=RedisStore(
            host=os.environ["REDIS_HOST"],
            port=int(os.environ["REDIS_PORT"])
        ),
        fernet=Fernet(os.environ["STORAGE_ENCRYPTION_KEY"])
    )
)

mcp = FastMCP(name="Production AWS Cognito App", auth=auth_provider)

```

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in`FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/v2/servers/auth/oauth-proxy#configuration-parameters).
##
[​](https://gofastmcp.com/v2/integrations/aws-cognito#environment-variables)
Environment Variables
For production deployments, use environment variables instead of hardcoding credentials.
###
[​](https://gofastmcp.com/v2/integrations/aws-cognito#provider-selection)
Provider Selection
Setting this environment variable allows the AWS Cognito provider to be used automatically without explicitly instantiating it in code.
[​](https://gofastmcp.com/v2/integrations/aws-cognito#param-fastmcp-server-auth)
FASTMCP_SERVER_AUTH
default:"Not set"
Set to `fastmcp.server.auth.providers.aws.AWSCognitoProvider` to use AWS Cognito authentication.
###
[​](https://gofastmcp.com/v2/integrations/aws-cognito#aws-cognito-specific-configuration)
AWS Cognito-Specific Configuration
These environment variables provide default values for the AWS Cognito provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.
[​](https://gofastmcp.com/v2/integrations/aws-cognito#param-fastmcp-server-auth-aws-cognito-user-pool-id)
FASTMCP_SERVER_AUTH_AWS_COGNITO_USER_POOL_ID
required
Your AWS Cognito user pool ID (e.g., `eu-central-1_XXXXXXXXX`)
[​](https://gofastmcp.com/v2/integrations/aws-cognito#param-fastmcp-server-auth-aws-cognito-aws-region)
FASTMCP_SERVER_AUTH_AWS_COGNITO_AWS_REGION
default:"eu-central-1"
AWS region where your AWS Cognito user pool is located
[​](https://gofastmcp.com/v2/integrations/aws-cognito#param-fastmcp-server-auth-aws-cognito-client-id)
FASTMCP_SERVER_AUTH_AWS_COGNITO_CLIENT_ID
required
Your AWS Cognito app client ID
[​](https://gofastmcp.com/v2/integrations/aws-cognito#param-fastmcp-server-auth-aws-cognito-client-secret)
FASTMCP_SERVER_AUTH_AWS_COGNITO_CLIENT_SECRET
required
Your AWS Cognito app client secret
[​](https://gofastmcp.com/v2/integrations/aws-cognito#param-fastmcp-server-auth-aws-cognito-base-url)
FASTMCP_SERVER_AUTH_AWS_COGNITO_BASE_URL
default:"http://localhost:8000"
Public URL where OAuth endpoints will be accessible (includes any mount path)
[​](https://gofastmcp.com/v2/integrations/aws-cognito#param-fastmcp-server-auth-aws-cognito-issuer-url)
FASTMCP_SERVER_AUTH_AWS_COGNITO_ISSUER_URL
default:"Uses BASE_URL"
Issuer URL for OAuth metadata (defaults to `BASE_URL`). Set to root-level URL when mounting under a path prefix to avoid 404 logs. See [HTTP Deployment guide](https://gofastmcp.com/v2/deployment/http#mounting-authenticated-servers) for details.
[​](https://gofastmcp.com/v2/integrations/aws-cognito#param-fastmcp-server-auth-aws-cognito-redirect-path)
FASTMCP_SERVER_AUTH_AWS_COGNITO_REDIRECT_PATH
default:"/auth/callback"
One of the redirect paths configured in your AWS Cognito app client
[​](https://gofastmcp.com/v2/integrations/aws-cognito#param-fastmcp-server-auth-aws-cognito-required-scopes)
FASTMCP_SERVER_AUTH_AWS_COGNITO_REQUIRED_SCOPES
default:"[\"openid\"]"
Comma-, space-, or JSON-separated list of required OAuth scopes (e.g., `openid email` or `["openid","email","profile"]`)
Example `.env` file:
Copy
```
# Use the AWS Cognito provider
FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.aws.AWSCognitoProvider

# AWS Cognito credentials
FASTMCP_SERVER_AUTH_AWS_COGNITO_USER_POOL_ID=eu-central-1_XXXXXXXXX
FASTMCP_SERVER_AUTH_AWS_COGNITO_AWS_REGION=eu-central-1
FASTMCP_SERVER_AUTH_AWS_COGNITO_CLIENT_ID=your-app-client-id
FASTMCP_SERVER_AUTH_AWS_COGNITO_CLIENT_SECRET=your-app-client-secret
FASTMCP_SERVER_AUTH_AWS_COGNITO_BASE_URL=https://your-server.com
FASTMCP_SERVER_AUTH_AWS_COGNITO_REQUIRED_SCOPES=openid,email,profile

```

With environment variables set, your server code simplifies to:
server.py
Copy
```
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_access_token

# Authentication is automatically configured from environment
mcp = FastMCP(name="AWS Cognito Secured App")

@mcp.tool
async def get_access_token_claims() -> dict:
    """Get the authenticated user's access token claims."""
    token = get_access_token()
    return {
        "sub": token.claims.get("sub"),
        "username": token.claims.get("username"),
        "cognito:groups": token.claims.get("cognito:groups", []),
    }

```

##
[​](https://gofastmcp.com/v2/integrations/aws-cognito#features)
Features
###
[​](https://gofastmcp.com/v2/integrations/aws-cognito#jwt-token-validation)
JWT Token Validation
The AWS Cognito provider includes robust JWT token validation:
  * **Signature Verification** : Validates tokens against AWS Cognito’s public keys (JWKS)
  * **Expiration Checking** : Automatically rejects expired tokens
  * **Issuer Validation** : Ensures tokens come from your specific AWS Cognito user pool
  * **Scope Enforcement** : Verifies required OAuth scopes are present


###
[​](https://gofastmcp.com/v2/integrations/aws-cognito#user-claims-and-groups)
User Claims and Groups
Access rich user information from AWS Cognito JWT tokens:
Copy
```
from fastmcp.server.dependencies import get_access_token

@mcp.tool
async def admin_only_tool() -> str:
    """A tool only available to admin users."""
    token = get_access_token()
    user_groups = token.claims.get("cognito:groups", [])

    if "admin" not in user_groups:
        raise ValueError("This tool requires admin access")

    return "Admin access granted!"

```

###
[​](https://gofastmcp.com/v2/integrations/aws-cognito#enterprise-integration)
Enterprise Integration
Perfect for enterprise environments with:
  * **Single Sign-On (SSO)** : Integrate with corporate identity providers
  * **Multi-Factor Authentication (MFA)** : Leverage AWS Cognito’s built-in MFA
  * **User Groups** : Role-based access control through AWS Cognito groups
  * **Custom Attributes** : Access custom user attributes defined in your AWS Cognito user pool
  * **Compliance** : Meet enterprise security and compliance requirements


[ AuthKit 🤝 FastMCP Previous ](https://gofastmcp.com/v2/integrations/authkit)[ Azure (Microsoft Entra ID) OAuth 🤝 FastMCP Next ](https://gofastmcp.com/v2/integrations/azure)
Ctrl+I
