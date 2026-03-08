[Skip to main content](https://gofastmcp.com/servers/transforms/tool-transformation#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Transforms
Tool Transformation
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
  * [ToolTransform](https://gofastmcp.com/servers/transforms/tool-transformation#tooltransform)
  * [Tool.from_tool()](https://gofastmcp.com/servers/transforms/tool-transformation#tool-from_tool)
  * [Modification Options](https://gofastmcp.com/servers/transforms/tool-transformation#modification-options)
  * [Hiding Arguments](https://gofastmcp.com/servers/transforms/tool-transformation#hiding-arguments)
  * [Renaming Arguments](https://gofastmcp.com/servers/transforms/tool-transformation#renaming-arguments)
  * [Custom Transform Functions](https://gofastmcp.com/servers/transforms/tool-transformation#custom-transform-functions)
  * [Context-Aware Tool Factories](https://gofastmcp.com/servers/transforms/tool-transformation#context-aware-tool-factories)


Transforms
# Tool Transformation
Copy page
Modify tool schemas - rename, reshape arguments, and customize behavior
Copy page
`3.0.0` Tool transformation lets you modify tool schemas - renaming tools, changing descriptions, adjusting tags, and reshaping argument schemas. FastMCP provides two mechanisms that share the same configuration options but differ in timing. **Deferred transformation** with `ToolTransform` applies modifications when tools flow through a transform chain. Use this for tools from mounted servers, proxies, or other providers where you don’t control the source directly. **Immediate transformation** with `Tool.from_tool()` creates a modified tool object right away. Use this when you have direct access to a tool and want to transform it before registration.
##
[​](https://gofastmcp.com/servers/transforms/tool-transformation#tooltransform)
ToolTransform
The `ToolTransform` class is a transform that modifies tools as they flow through a provider. Provide a dictionary mapping original tool names to their transformation configuration.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.transforms import ToolTransform
from fastmcp.tools.tool_transform import ToolTransformConfig

mcp = FastMCP("Server")

@mcp.tool
def verbose_internal_data_fetcher(query: str) -> str:
    """Fetches data from the internal database."""
    return f"Results for: {query}"

# Rename the tool to something simpler
mcp.add_transform(ToolTransform({
    "verbose_internal_data_fetcher": ToolTransformConfig(
        name="search",
        description="Search the database.",
    )
}))

# Clients see "search" with the cleaner description

```

`ToolTransform` is useful when you want to modify tools from mounted or proxied servers without changing the original source.
##
[​](https://gofastmcp.com/servers/transforms/tool-transformation#tool-from_tool)
Tool.from_tool()
Use `Tool.from_tool()` when you have the tool object and want to create a transformed version for registration.
Copy
```
from fastmcp import FastMCP
from fastmcp.tools import Tool, tool
from fastmcp.tools.tool_transform import ArgTransform

# Create a tool without registering it
@tool
def search(q: str, limit: int = 10) -> list[str]:
    """Search for items."""
    return [f"Result {i} for {q}" for i in range(limit)]

# Transform it before registration
better_search = Tool.from_tool(
    search,
    name="find_items",
    description="Find items matching your search query.",
    transform_args={
        "q": ArgTransform(
            name="query",
            description="The search terms to look for.",
        ),
    },
)

mcp = FastMCP("Server")
mcp.add_tool(better_search)

```

The standalone `@tool` decorator (from `fastmcp.tools`) creates a Tool object without registering it to any server. This separates creation from registration, letting you transform tools before deciding where they go.
##
[​](https://gofastmcp.com/servers/transforms/tool-transformation#modification-options)
Modification Options
Both mechanisms support the same modifications. **Tool-level options:**
Option | Description
---|---
`name` | New name for the tool
`description` | New description
`title` | Human-readable title
`tags` | Set of tags for categorization
`annotations` | MCP ToolAnnotations
`meta` | Custom metadata dictionary
`enabled` | Whether the tool is visible to clients (default `True`)
**Argument-level options** (via `ArgTransform` or `ArgTransformConfig`):
Option | Description
---|---
`name` | Rename the argument
`description` | New description for the argument
`default` | New default value
`default_factory` | Callable that generates a default (requires `hide=True`)
`hide` | Remove from client-visible schema
`required` | Make an optional argument required
`type` | Change the argument’s type
`examples` | Example values for the argument
##
[​](https://gofastmcp.com/servers/transforms/tool-transformation#hiding-arguments)
Hiding Arguments
Hide arguments to simplify the interface or inject values the client shouldn’t control.
Copy
```
from fastmcp.tools.tool_transform import ArgTransform

# Hide with a constant value
transform_args = {
    "api_key": ArgTransform(hide=True, default="secret-key"),
}

# Hide with a dynamic value
import uuid
transform_args = {
    "request_id": ArgTransform(hide=True, default_factory=lambda: str(uuid.uuid4())),
}

```

Hidden arguments disappear from the tool’s schema. The client never sees them, but the underlying function receives the configured value.
`default_factory` requires `hide=True`. Visible arguments need static defaults that can be represented in JSON Schema.
##
[​](https://gofastmcp.com/servers/transforms/tool-transformation#renaming-arguments)
Renaming Arguments
Rename arguments to make them more intuitive for LLMs or match your API conventions.
Copy
```
from fastmcp.tools import Tool, tool
from fastmcp.tools.tool_transform import ArgTransform

@tool
def search(q: str, n: int = 10) -> list[str]:
    """Search for items."""
    return []

better_search = Tool.from_tool(
    search,
    transform_args={
        "q": ArgTransform(name="query", description="Search terms"),
        "n": ArgTransform(name="max_results", description="Maximum results to return"),
    },
)

```

##
[​](https://gofastmcp.com/servers/transforms/tool-transformation#custom-transform-functions)
Custom Transform Functions
For advanced scenarios, provide a `transform_fn` that intercepts tool execution. The function can validate inputs, modify outputs, or add custom logic while still calling the original tool via `forward()`.
Copy
```
from fastmcp import FastMCP
from fastmcp.tools import Tool, tool
from fastmcp.tools.tool_transform import forward, ArgTransform

@tool
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    return a / b

async def safe_divide(numerator: float, denominator: float) -> float:
    if denominator == 0:
        raise ValueError("Cannot divide by zero")
    return await forward(numerator=numerator, denominator=denominator)

safe_division = Tool.from_tool(
    divide,
    name="safe_divide",
    transform_fn=safe_divide,
    transform_args={
        "a": ArgTransform(name="numerator"),
        "b": ArgTransform(name="denominator"),
    },
)

mcp = FastMCP("Server")
mcp.add_tool(safe_division)

```

The `forward()` function handles argument mapping automatically. Call it with the transformed argument names, and it maps them back to the original function’s parameters. For direct access to the original function without mapping, use `forward_raw()` with the original parameter names.
##
[​](https://gofastmcp.com/servers/transforms/tool-transformation#context-aware-tool-factories)
Context-Aware Tool Factories
You can write functions that act as “factories,” generating specialized versions of a tool for different contexts. For example, create a `get_my_data` tool for the current user by hiding the `user_id` parameter and providing it automatically.
Copy
```
from fastmcp import FastMCP
from fastmcp.tools import Tool, tool
from fastmcp.tools.tool_transform import ArgTransform

# A generic tool that requires a user_id
@tool
def get_user_data(user_id: str, query: str) -> str:
    """Fetch data for a specific user."""
    return f"Data for user {user_id}: {query}"


def create_user_tool(user_id: str) -> Tool:
    """Factory that creates a user-specific version of get_user_data."""
    return Tool.from_tool(
        get_user_data,
        name="get_my_data",
        description="Fetch your data. No need to specify a user ID.",
        transform_args={
            "user_id": ArgTransform(hide=True, default=user_id),
        },
    )


# Create a server with a tool customized for the current user
mcp = FastMCP("User Server")
current_user_id = "user-123"  # e.g., from auth context
mcp.add_tool(create_user_tool(current_user_id))

# Clients see "get_my_data(query: str)" — user_id is injected automatically

```

This pattern is useful for multi-tenant servers where each connection gets tools pre-configured with their identity, or for wrapping generic tools with environment-specific defaults.
[ Namespace Transform Previous ](https://gofastmcp.com/servers/transforms/namespace)[ Component Visibility Next ](https://gofastmcp.com/servers/visibility)
Ctrl+I
