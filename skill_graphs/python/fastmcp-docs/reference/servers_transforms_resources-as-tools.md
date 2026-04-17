[Skip to main content](https://gofastmcp.com/servers/transforms/resources-as-tools#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Transforms
Resources as Tools
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
    * [ Overview NEW ](https://gofastmcp.com/servers/transforms/transforms)
    * [ Namespace NEW ](https://gofastmcp.com/servers/transforms/namespace)
    * [ Tool Transformation NEW ](https://gofastmcp.com/servers/transforms/tool-transformation)
    * [ Visibility NEW ](https://gofastmcp.com/servers/visibility)
    * [ Code Mode NEW ](https://gofastmcp.com/servers/transforms/code-mode)
    * [ Tool Search NEW ](https://gofastmcp.com/servers/transforms/tool-search)
    * [ Resources as Tools NEW ](https://gofastmcp.com/servers/transforms/resources-as-tools)
    * [ Prompts as Tools NEW ](https://gofastmcp.com/servers/transforms/prompts-as-tools)
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
  * [Basic Usage](https://gofastmcp.com/servers/transforms/resources-as-tools#basic-usage)
  * [Static Resources vs Templates](https://gofastmcp.com/servers/transforms/resources-as-tools#static-resources-vs-templates)
  * [Reading Resources](https://gofastmcp.com/servers/transforms/resources-as-tools#reading-resources)
  * [Binary Content](https://gofastmcp.com/servers/transforms/resources-as-tools#binary-content)


Transforms
# Resources as Tools
Copy page
Expose resources to tool-only clients
Copy page
`3.0.0` Some MCP clients only support tools. They cannot list or read resources directly because they lack resource protocol support. The `ResourcesAsTools` transform bridges this gap by generating tools that provide access to your server’s resources. When you add `ResourcesAsTools` to a server, it creates two tools that clients can call instead of using the resource protocol:
  * **`list_resources`**returns JSON describing all available resources and templates
  * **`read_resource`**reads a specific resource by URI

This means any client that can call tools can now access resources, even if the client has no native resource support.
##
[​](https://gofastmcp.com/servers/transforms/resources-as-tools#basic-usage)
Basic Usage
Pass your server to `ResourcesAsTools` when adding the transform. The transform queries that server for resources whenever the generated tools are called.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.transforms import ResourcesAsTools

mcp = FastMCP("My Server")

@mcp.resource("config://app")
def app_config() -> str:
    """Application configuration."""
    return '{"app_name": "My App", "version": "1.0.0"}'

@mcp.resource("user://{user_id}/profile")
def user_profile(user_id: str) -> str:
    """Get a user's profile by ID."""
    return f'{{"user_id": "{user_id}", "name": "User {user_id}"}}'

# Add the transform - creates list_resources and read_resource tools
mcp.add_transform(ResourcesAsTools(mcp))

```

Clients now see three tools: whatever tools you defined directly, plus `list_resources` and `read_resource`.
##
[​](https://gofastmcp.com/servers/transforms/resources-as-tools#static-resources-vs-templates)
Static Resources vs Templates
Resources come in two forms, and the `list_resources` tool distinguishes between them in its JSON output. Static resources have fixed URIs. They represent concrete data that exists at a known location. In the listing output, static resources include a `uri` field containing the exact URI to request. Resource templates have parameterized URIs with placeholders like `{user_id}`. They represent patterns for accessing dynamic data. In the listing output, templates include a `uri_template` field showing the pattern with its placeholders. When a client calls `list_resources`, it receives JSON like this:
Copy
```
[
  {
    "uri": "config://app",
    "name": "app_config",
    "description": "Application configuration.",
    "mime_type": "text/plain"
  },
  {
    "uri_template": "user://{user_id}/profile",
    "name": "user_profile",
    "description": "Get a user's profile by ID."
  }
]

```

The client can distinguish resource types by checking which field is present: `uri` for static resources, `uri_template` for templates.
##
[​](https://gofastmcp.com/servers/transforms/resources-as-tools#reading-resources)
Reading Resources
The `read_resource` tool accepts a single `uri` argument. For static resources, pass the exact URI. For templates, fill in the placeholders with actual values.
Copy
```
# Reading a static resource
result = await client.call_tool("read_resource", {"uri": "config://app"})
print(result.data)  # '{"app_name": "My App", "version": "1.0.0"}'

# Reading a templated resource - fill in {user_id} with an actual ID
result = await client.call_tool("read_resource", {"uri": "user://42/profile"})
print(result.data)  # '{"user_id": "42", "name": "User 42"}'

```

The transform handles template matching automatically. When you request `user://42/profile`, it matches against the `user://{user_id}/profile` template, extracts `user_id=42`, and calls your resource function with that parameter.
##
[​](https://gofastmcp.com/servers/transforms/resources-as-tools#binary-content)
Binary Content
Resources that return binary data (like images or files) are automatically base64-encoded when read through the `read_resource` tool. This ensures binary content can be transmitted as a string in the tool response.
Copy
```
@mcp.resource("data://binary", mime_type="application/octet-stream")
def binary_data() -> bytes:
    return b"\x00\x01\x02\x03"

# Client receives base64-encoded string
result = await client.call_tool("read_resource", {"uri": "data://binary"})
decoded = base64.b64decode(result.data)  # b'\x00\x01\x02\x03'

```

[ Tool Search Previous ](https://gofastmcp.com/servers/transforms/tool-search)[ Prompts as Tools Next ](https://gofastmcp.com/servers/transforms/prompts-as-tools)
Ctrl+I
