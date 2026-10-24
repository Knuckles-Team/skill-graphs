[Skip to main content](https://gofastmcp.com/servers/transforms/transforms#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Transforms
Transforms Overview
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
  * [Mental Model](https://gofastmcp.com/servers/transforms/transforms#mental-model)
  * [Built-in Transforms](https://gofastmcp.com/servers/transforms/transforms#built-in-transforms)
  * [Server vs Provider Transforms](https://gofastmcp.com/servers/transforms/transforms#server-vs-provider-transforms)
  * [Provider-Level Transforms](https://gofastmcp.com/servers/transforms/transforms#provider-level-transforms)
  * [Server-Level Transforms](https://gofastmcp.com/servers/transforms/transforms#server-level-transforms)
  * [Transform Order](https://gofastmcp.com/servers/transforms/transforms#transform-order)
  * [Custom Transforms](https://gofastmcp.com/servers/transforms/transforms#custom-transforms)


Transforms
# Transforms Overview
Copy page
Modify components as they flow through your server
Copy page
`3.0.0` Transforms modify components as they flow from providers to clients. When a client asks “what tools do you have?”, the request passes through each transform in the chain. Each transform can modify the components before passing them along.
##
[​](https://gofastmcp.com/servers/transforms/transforms#mental-model)
Mental Model
Think of transforms as filters in a pipeline. Components flow from providers through transforms to reach clients:
Copy
```
Provider → [Transform A] → [Transform B] → Client

```

When listing components, transforms receive sequences and return transformed sequences—a pure function pattern. When getting a specific component by name, transforms use a middleware pattern with `call_next`, working in reverse: mapping the client’s requested name back to the original, then transforming the result.
##
[​](https://gofastmcp.com/servers/transforms/transforms#built-in-transforms)
Built-in Transforms
FastMCP provides several transforms for common use cases:
  * **[Namespace](https://gofastmcp.com/servers/transforms/namespace)** - Prefix component names to prevent conflicts when composing servers
  * **[Tool Transformation](https://gofastmcp.com/servers/transforms/tool-transformation)** - Rename tools, modify descriptions, reshape arguments
  * **[Enabled](https://gofastmcp.com/servers/visibility)** - Control which components are visible at runtime
  * **[Tool Search](https://gofastmcp.com/servers/transforms/tool-search)** - Replace large tool catalogs with on-demand search
  * **[Resources as Tools](https://gofastmcp.com/servers/transforms/resources-as-tools)** - Expose resources to tool-only clients
  * **[Prompts as Tools](https://gofastmcp.com/servers/transforms/prompts-as-tools)** - Expose prompts to tool-only clients
  * **[Code Mode (Experimental)](https://gofastmcp.com/servers/transforms/code-mode)** - Replace many tools with programmable `search` + `execute`


##
[​](https://gofastmcp.com/servers/transforms/transforms#server-vs-provider-transforms)
Server vs Provider Transforms
Transforms can be added at two levels, each serving different purposes.
###
[​](https://gofastmcp.com/servers/transforms/transforms#provider-level-transforms)
Provider-Level Transforms
Provider transforms apply to components from a specific provider. They run first, modifying components before they reach the server level.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.providers import FastMCPProvider
from fastmcp.server.transforms import Namespace, ToolTransform
from fastmcp.tools.tool_transform import ToolTransformConfig

sub_server = FastMCP("Sub")

@sub_server.tool
def process(data: str) -> str:
    return f"Processed: {data}"

# Create provider and add transforms
provider = FastMCPProvider(sub_server)
provider.add_transform(Namespace("api"))
provider.add_transform(ToolTransform({
    "api_process": ToolTransformConfig(description="Process data through the API"),
}))

main = FastMCP("Main", providers=[provider])
# Tool is now: api_process with updated description

```

When using `mount()`, the returned provider reference lets you add transforms directly.
Copy
```
main = FastMCP("Main")
mount = main.mount(sub_server, namespace="api")
mount.add_transform(ToolTransform({...}))

```

###
[​](https://gofastmcp.com/servers/transforms/transforms#server-level-transforms)
Server-Level Transforms
Server transforms apply to all components from all providers. They run after provider transforms, seeing the already-transformed names.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.transforms import Namespace

mcp = FastMCP("Server", transforms=[Namespace("v1")])

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

# All tools become v1_toolname

```

Server-level transforms are useful for API versioning or applying consistent naming across your entire server.
###
[​](https://gofastmcp.com/servers/transforms/transforms#transform-order)
Transform Order
Transforms stack in the order they’re added. The first transform added is innermost (closest to the provider), and subsequent transforms wrap it.
Copy
```
from fastmcp.server.providers import FastMCPProvider
from fastmcp.server.transforms import Namespace, ToolTransform
from fastmcp.tools.tool_transform import ToolTransformConfig

provider = FastMCPProvider(server)
provider.add_transform(Namespace("api"))           # Applied first
provider.add_transform(ToolTransform({             # Sees namespaced names
    "api_verbose_name": ToolTransformConfig(name="short"),
}))

# Flow: "verbose_name" -> "api_verbose_name" -> "short"

```

When a client requests “short”, the transforms reverse the mapping: ToolTransform maps “short” to “api_verbose_name”, then Namespace strips the prefix to find “verbose_name” in the provider.
##
[​](https://gofastmcp.com/servers/transforms/transforms#custom-transforms)
Custom Transforms
Create custom transforms by subclassing `Transform` and overriding the methods you need.
Copy
```
from collections.abc import Sequence
from fastmcp.server.transforms import Transform, GetToolNext
from fastmcp.tools.tool import Tool

class TagFilter(Transform):
    """Filter tools to only those with specific tags."""

    def __init__(self, required_tags: set[str]):
        self.required_tags = required_tags

    async def list_tools(self, tools: Sequence[Tool]) -> Sequence[Tool]:
        return [t for t in tools if t.tags & self.required_tags]

    async def get_tool(self, name: str, call_next: GetToolNext) -> Tool | None:
        tool = await call_next(name)
        if tool and tool.tags & self.required_tags:
            return tool
        return None

```

The `Transform` base class provides default implementations that pass through unchanged. Override only the methods relevant to your transform. Each component type has two methods with different patterns:
Method | Pattern | Purpose
---|---|---
`list_tools(tools)` | Pure function | Transform the sequence of tools
`get_tool(name, call_next)` | Middleware | Transform lookup by name
`list_resources(resources)` | Pure function | Transform the sequence of resources
`get_resource(uri, call_next)` | Middleware | Transform lookup by URI
`list_resource_templates(templates)` | Pure function | Transform the sequence of templates
`get_resource_template(uri, call_next)` | Middleware | Transform template lookup by URI
`list_prompts(prompts)` | Pure function | Transform the sequence of prompts
`get_prompt(name, call_next)` | Middleware | Transform lookup by name
List methods receive sequences directly and return transformed sequences. Get methods use `call_next` for routing flexibility—when a client requests “new_name”, your transform maps it back to “original_name” before calling `call_next()`.
Copy
```
class PrefixTransform(Transform):
    def __init__(self, prefix: str):
        self.prefix = prefix

    async def list_tools(self, tools: Sequence[Tool]) -> Sequence[Tool]:
        return [t.model_copy(update={"name": f"{self.prefix}_{t.name}"}) for t in tools]

    async def get_tool(self, name: str, call_next: GetToolNext) -> Tool | None:
        # Reverse the prefix to find the original
        if not name.startswith(f"{self.prefix}_"):
            return None
        original = name[len(self.prefix) + 1:]
        tool = await call_next(original)
        if tool:
            return tool.model_copy(update={"name": name})
        return None

```

[ Custom Providers Previous ](https://gofastmcp.com/servers/providers/custom)[ Namespace Transform Next ](https://gofastmcp.com/servers/transforms/namespace)
Ctrl+I
