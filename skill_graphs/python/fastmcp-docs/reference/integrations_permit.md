[Skip to main content](https://gofastmcp.com/integrations/permit#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Auth
Permit.io Authorization 🤝 FastMCP
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
    * [Auth0](https://gofastmcp.com/integrations/auth0)
    * [AuthKit](https://gofastmcp.com/integrations/authkit)
    * [AWS Cognito](https://gofastmcp.com/integrations/aws-cognito)
    * [Azure (Entra ID)](https://gofastmcp.com/integrations/azure)
    * [Descope](https://gofastmcp.com/integrations/descope)
    * [Discord](https://gofastmcp.com/integrations/discord)
    * [Eunomia Auth](https://gofastmcp.com/integrations/eunomia-authorization)
    * [GitHub](https://gofastmcp.com/integrations/github)
    * [Google](https://gofastmcp.com/integrations/google)
    * [Oracle](https://gofastmcp.com/integrations/oci)
    * [Permit.io](https://gofastmcp.com/integrations/permit)
    * [PropelAuth](https://gofastmcp.com/integrations/propelauth)
    * [Scalekit](https://gofastmcp.com/integrations/scalekit)
    * [Supabase](https://gofastmcp.com/integrations/supabase)
    * [WorkOS](https://gofastmcp.com/integrations/workos)
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
  * [How it Works](https://gofastmcp.com/integrations/permit#how-it-works)
  * [Policy Mapping](https://gofastmcp.com/integrations/permit#policy-mapping)
  * [Listing Operations](https://gofastmcp.com/integrations/permit#listing-operations)
  * [Execution Operations](https://gofastmcp.com/integrations/permit#execution-operations)
  * [Add Authorization to Your Server](https://gofastmcp.com/integrations/permit#add-authorization-to-your-server)
  * [Prerequisites](https://gofastmcp.com/integrations/permit#prerequisites)
  * [Run the Permit.io PDP](https://gofastmcp.com/integrations/permit#run-the-permit-io-pdp)
  * [Create a Server with Authorization](https://gofastmcp.com/integrations/permit#create-a-server-with-authorization)
  * [Configure Access Policies](https://gofastmcp.com/integrations/permit#configure-access-policies)
  * [Example Policy Configuration](https://gofastmcp.com/integrations/permit#example-policy-configuration)
  * [Identity Management](https://gofastmcp.com/integrations/permit#identity-management)
  * [JWT Authentication Example](https://gofastmcp.com/integrations/permit#jwt-authentication-example)
  * [ABAC Policies with Tool Arguments](https://gofastmcp.com/integrations/permit#abac-policies-with-tool-arguments)
  * [Example: Conditional Access](https://gofastmcp.com/integrations/permit#example-conditional-access)
  * [Run the Server](https://gofastmcp.com/integrations/permit#run-the-server)
  * [Advanced Configuration](https://gofastmcp.com/integrations/permit#advanced-configuration)
  * [Environment Variables](https://gofastmcp.com/integrations/permit#environment-variables)
  * [Custom Middleware Configuration](https://gofastmcp.com/integrations/permit#custom-middleware-configuration)
  * [Example: Complete JWT Authentication Server](https://gofastmcp.com/integrations/permit#example-complete-jwt-authentication-server)


Auth
# Permit.io Authorization 🤝 FastMCP
Copy page
Add fine-grained authorization to your FastMCP servers with Permit.io
Copy page
Add **policy-based authorization** to your FastMCP servers with one-line code addition with the  Control which tools, resources and prompts MCP clients can view and execute on your server. Define dynamic policies using Permit.io’s powerful RBAC, ABAC, and REBAC capabilities, and obtain comprehensive audit logs of all access attempts and violations.
##
[​](https://gofastmcp.com/integrations/permit#how-it-works)
How it Works
Leveraging FastMCP’s [Middleware](https://gofastmcp.com/servers/middleware), the Permit.io middleware intercepts all MCP requests to your server and automatically maps MCP methods to authorization checks against your Permit.io policies; covering both server methods and tool execution.
###
[​](https://gofastmcp.com/integrations/permit#policy-mapping)
Policy Mapping
The middleware automatically maps MCP methods to Permit.io resources and actions:
  * **MCP server methods** (e.g., `tools/list`, `resources/read`):
    * **Resource** : `{server_name}_{component}` (e.g., `myserver_tools`)
    * **Action** : The method verb (e.g., `list`, `read`)
  * **Tool execution** (method `tools/call`):
    * **Resource** : `{server_name}` (e.g., `myserver`)
    * **Action** : The tool name (e.g., `greet`)

![Permit.io Policy Mapping Example](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/permit/policy_mapping.png?fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=29e09fd3ceacd3aa8b1881eedb0a9d90) _Example: In Permit.io, the ‘Admin’ role is granted permissions on resources and actions as mapped by the middleware. For example, ‘greet’, ‘greet-jwt’, and ‘login’ are actions on the ‘mcp_server’ resource, and ‘list’ is an action on the ‘mcp_server_tools’ resource._
> **Note:** Don’t forget to assign the relevant role (e.g., Admin, User) to the user authenticating to your MCP server (such as the user in the JWT) in the Permit.io Directory. Without the correct role assignment, users will not have access to the resources and actions you’ve configured in your policies. ![Permit.io Directory Role Assignment Example](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/permit/role_assignement.png?fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=62f385a65b62cad9769e2b81e14902c2) _Example: In Permit.io Directory, both ‘client’ and ‘admin’ users are assigned the ‘Admin’ role, granting them the permissions defined in your policy mapping._
For detailed policy mapping examples and configuration, see
###
[​](https://gofastmcp.com/integrations/permit#listing-operations)
Listing Operations
The middleware behaves as a filter for listing operations (`tools/list`, `resources/list`, `prompts/list`), hiding to the client components that are not authorized by the defined policies.
Permit.io PDPFastMCP ServerPermit.io MiddlewareMCP ClientPermit.io PDPFastMCP ServerPermit.io MiddlewareMCP ClientMCP Listing Request (e.g., tools/list)MCP Listing RequestMCP Listing ResponseAuthorization ChecksAuthorization DecisionsFiltered MCP Listing Response
###
[​](https://gofastmcp.com/integrations/permit#execution-operations)
Execution Operations
The middleware behaves as an enforcement point for execution operations (`tools/call`, `resources/read`, `prompts/get`), blocking operations that are not authorized by the defined policies.
Permit.io PDPFastMCP ServerPermit.io MiddlewareMCP ClientPermit.io PDPFastMCP ServerPermit.io MiddlewareMCP ClientMCP Execution Request (e.g., tools/call)Authorization CheckAuthorization DecisionMCP Unauthorized Error (if denied)MCP Execution Request (if allowed)MCP Execution Response (if allowed)MCP Execution Response (if allowed)
##
[​](https://gofastmcp.com/integrations/permit#add-authorization-to-your-server)
Add Authorization to Your Server
Permit.io is a cloud-native authorization service. You need a Permit.io account and a running Policy Decision Point (PDP) for the middleware to function. You can run the PDP locally with Docker or use Permit.io’s cloud PDP.
###
[​](https://gofastmcp.com/integrations/permit#prerequisites)
Prerequisites
  1. **Permit.io Account** : Sign up at
  2. **PDP Setup** : Run the Permit.io PDP locally or use the cloud PDP (RBAC only)
  3. **API Key** : Get your Permit.io API key from the dashboard


###
[​](https://gofastmcp.com/integrations/permit#run-the-permit-io-pdp)
Run the Permit.io PDP
Run the PDP locally with Docker:
Copy
```
docker run -p 7766:7766 permitio/pdp:latest

```

Or use the cloud PDP URL: `https://cloudpdp.api.permit.io`
###
[​](https://gofastmcp.com/integrations/permit#create-a-server-with-authorization)
Create a Server with Authorization
First, install the `permit-fastmcp` package:
Copy
```
# Using UV (recommended)
uv add permit-fastmcp

# Using pip
pip install permit-fastmcp

```

Then create a FastMCP server and add the Permit.io middleware:
server.py
Copy
```
from fastmcp import FastMCP
from permit_fastmcp.middleware.middleware import PermitMcpMiddleware

mcp = FastMCP("Secure FastMCP Server 🔒")

@mcp.tool
def greet(name: str) -> str:
    """Greet a user by name"""
    return f"Hello, {name}!"

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add Permit.io authorization middleware
mcp.add_middleware(PermitMcpMiddleware(
    permit_pdp_url="http://localhost:7766",
    permit_api_key="your-permit-api-key"
))

if __name__ == "__main__":
    mcp.run(transport="http")

```

###
[​](https://gofastmcp.com/integrations/permit#configure-access-policies)
Configure Access Policies
Create your authorization policies in the Permit.io dashboard:
  1. **Create Resources** : Define resources like `mcp_server` and `mcp_server_tools`
  2. **Define Actions** : Add actions like `greet`, `add`, `list`, `read`
  3. **Create Roles** : Define roles like `Admin`, `User`, `Guest`
  4. **Assign Permissions** : Grant roles access to specific resources and actions
  5. **Assign Users** : Assign roles to users in the Permit.io Directory

For step-by-step setup instructions and troubleshooting, see
####
[​](https://gofastmcp.com/integrations/permit#example-policy-configuration)
Example Policy Configuration
Policies are defined in the Permit.io dashboard, but you can also use the
Copy
```
# Resources
resource "permitio_resource" "mcp_server" {
  name = "mcp_server"
  key  = "mcp_server"

  actions = {
    "greet" = { name = "greet" }
    "add"   = { name = "add" }
  }
}

resource "permitio_resource" "mcp_server_tools" {
  name = "mcp_server_tools"
  key  = "mcp_server_tools"

  actions = {
    "list" = { name = "list" }
  }
}

# Roles
resource "permitio_role" "Admin" {
  key         = "Admin"
  name        = "Admin"
  permissions = [
    "mcp_server:greet",
    "mcp_server:add",
    "mcp_server_tools:list"
  ]
}

```

You can also use the  For complete policy examples including ABAC and RBAC configurations, see
###
[​](https://gofastmcp.com/integrations/permit#identity-management)
Identity Management
The middleware supports multiple identity extraction modes:
  * **Fixed Identity** : Use a fixed identity for all requests
  * **Header-based** : Extract identity from HTTP headers
  * **JWT-based** : Extract and verify JWT tokens
  * **Source-based** : Use the MCP context source field

For detailed identity mode configuration and environment variables, see
####
[​](https://gofastmcp.com/integrations/permit#jwt-authentication-example)
JWT Authentication Example
Copy
```
import os

# Configure JWT identity extraction
os.environ["PERMIT_MCP_IDENTITY_MODE"] = "jwt"
os.environ["PERMIT_MCP_IDENTITY_JWT_SECRET"] = "your-jwt-secret"

mcp.add_middleware(PermitMcpMiddleware(
    permit_pdp_url="http://localhost:7766",
    permit_api_key="your-permit-api-key"
))

```

###
[​](https://gofastmcp.com/integrations/permit#abac-policies-with-tool-arguments)
ABAC Policies with Tool Arguments
The middleware supports Attribute-Based Access Control (ABAC) policies that can evaluate tool arguments as attributes. Tool arguments are automatically flattened as individual attributes (e.g., `arg_name`, `arg_number`) for granular policy conditions. ![ABAC Condition Example](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/permit/abac_condition_example.png?fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=e93d0547b6d75a207d453bb205412f01) _Example: Create dynamic resources with conditions like`resource.arg_number greater-than 10` to allow the `conditional-greet` tool only when the number argument exceeds 10._
####
[​](https://gofastmcp.com/integrations/permit#example-conditional-access)
Example: Conditional Access
Create a dynamic resource with conditions like `resource.arg_number greater-than 10` to allow the `conditional-greet` tool only when the number argument exceeds 10.
Copy
```
@mcp.tool
def conditional_greet(name: str, number: int) -> str:
    """Greet a user only if number > 10"""
    return f"Hello, {name}! Your number is {number}"

```

![ABAC Policy Example](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/permit/abac_policy_example.png?fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=ee7f1f8bfba6ad2954d3c17143755a04) _Example: The Admin role is granted access to the “conditional-greet” action on the “Big-greets” dynamic resource, while other tools like “greet”, “greet-jwt”, and “login” are granted on the base “mcp_server” resource._ For comprehensive ABAC configuration and advanced policy examples, see
###
[​](https://gofastmcp.com/integrations/permit#run-the-server)
Run the Server
Start your FastMCP server normally:
Copy
```
python server.py

```

The middleware will now intercept all MCP requests and check them against your Permit.io policies. Requests include user identification through the configured identity mode and automatic mapping of MCP methods to authorization resources and actions.
##
[​](https://gofastmcp.com/integrations/permit#advanced-configuration)
Advanced Configuration
###
[​](https://gofastmcp.com/integrations/permit#environment-variables)
Environment Variables
Configure the middleware using environment variables:
Copy
```
# Permit.io configuration
export PERMIT_MCP_PERMIT_PDP_URL="http://localhost:7766"
export PERMIT_MCP_PERMIT_API_KEY="your-api-key"

# Identity configuration
export PERMIT_MCP_IDENTITY_MODE="jwt"
export PERMIT_MCP_IDENTITY_JWT_SECRET="your-jwt-secret"

# Method configuration
export PERMIT_MCP_KNOWN_METHODS='["tools/list","tools/call"]'
export PERMIT_MCP_BYPASSED_METHODS='["initialize","ping"]'

# Logging configuration
export PERMIT_MCP_ENABLE_AUDIT_LOGGING="true"

```

For a complete list of all configuration options and environment variables, see
###
[​](https://gofastmcp.com/integrations/permit#custom-middleware-configuration)
Custom Middleware Configuration
Copy
```
from permit_fastmcp.middleware.middleware import PermitMcpMiddleware

middleware = PermitMcpMiddleware(
    permit_pdp_url="http://localhost:7766",
    permit_api_key="your-api-key",
    enable_audit_logging=True,
    bypass_methods=["initialize", "ping", "health/*"]
)

mcp.add_middleware(middleware)

```

For advanced configuration options and custom middleware extensions, see
##
[​](https://gofastmcp.com/integrations/permit#example-complete-jwt-authentication-server)
Example: Complete JWT Authentication Server
See the
Copy
```
from fastmcp import FastMCP, Context
from permit_fastmcp.middleware.middleware import PermitMcpMiddleware
import jwt
import datetime

# Configure JWT identity extraction
os.environ["PERMIT_MCP_IDENTITY_MODE"] = "jwt"
os.environ["PERMIT_MCP_IDENTITY_JWT_SECRET"] = "mysecretkey"

mcp = FastMCP("My MCP Server")

@mcp.tool
def login(username: str, password: str) -> str:
    """Login to get a JWT token"""
    if username == "admin" and password == "password":
        token = jwt.encode(
            {"sub": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            "mysecretkey",
            algorithm="HS256"
        )
        return f"Bearer {token}"
    raise Exception("Invalid credentials")

@mcp.tool
def greet_jwt(ctx: Context) -> str:
    """Greet a user by extracting their name from JWT"""
    # JWT extraction handled by middleware
    return "Hello, authenticated user!"

mcp.add_middleware(PermitMcpMiddleware(
    permit_pdp_url="http://localhost:7766",
    permit_api_key="your-permit-api-key"
))

if __name__ == "__main__":
    mcp.run(transport="http")

```

For detailed policy configuration, custom authentication, and advanced deployment patterns, visit the
[ OCI IAM OAuth 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/oci)[ PropelAuth 🤝 FastMCP Next ](https://gofastmcp.com/integrations/propelauth)
Ctrl+I
![Permit.io Policy Mapping Example](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/permit/policy_mapping.png?w=840&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=163d699bc4374faed40ee47ab6f5e8dd)
![Permit.io Directory Role Assignment Example](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/permit/role_assignement.png?w=840&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=0dcf730386f3b2d607a7fd47417499b3)
![ABAC Condition Example](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/permit/abac_condition_example.png?w=840&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=8c8be9114c76efb4f3fcf56d3f93e7e1)
![ABAC Policy Example](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/permit/abac_policy_example.png?w=840&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=59b0396315b015d2adb53e9c0f7e928d)
