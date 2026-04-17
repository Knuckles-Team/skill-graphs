[Skip to main content](https://gofastmcp.com/servers/visibility#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Transforms
Component Visibility
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
  * [Component Visibility](https://gofastmcp.com/servers/visibility#component-visibility)
  * [Disabling Components](https://gofastmcp.com/servers/visibility#disabling-components)
  * [Enabling Components](https://gofastmcp.com/servers/visibility#enabling-components)
  * [Keys and Tags](https://gofastmcp.com/servers/visibility#keys-and-tags)
  * [Component Keys](https://gofastmcp.com/servers/visibility#component-keys)
  * [Tags](https://gofastmcp.com/servers/visibility#tags)
  * [Combining Keys and Tags](https://gofastmcp.com/servers/visibility#combining-keys-and-tags)
  * [Allowlist Mode](https://gofastmcp.com/servers/visibility#allowlist-mode)
  * [Allowlist Behavior](https://gofastmcp.com/servers/visibility#allowlist-behavior)
  * [Ordering and Overrides](https://gofastmcp.com/servers/visibility#ordering-and-overrides)
  * [Server vs Provider](https://gofastmcp.com/servers/visibility#server-vs-provider)
  * [Server-Level](https://gofastmcp.com/servers/visibility#server-level)
  * [Provider-Level](https://gofastmcp.com/servers/visibility#provider-level)
  * [Layered Transforms](https://gofastmcp.com/servers/visibility#layered-transforms)
  * [Per-Session Visibility](https://gofastmcp.com/servers/visibility#per-session-visibility)
  * [How Session Rules Work](https://gofastmcp.com/servers/visibility#how-session-rules-work)
  * [Filter Criteria](https://gofastmcp.com/servers/visibility#filter-criteria)
  * [Automatic Notifications](https://gofastmcp.com/servers/visibility#automatic-notifications)
  * [Namespace Activation Pattern](https://gofastmcp.com/servers/visibility#namespace-activation-pattern)
  * [Method Reference](https://gofastmcp.com/servers/visibility#method-reference)
  * [Client Notifications](https://gofastmcp.com/servers/visibility#client-notifications)
  * [Filtering Logic](https://gofastmcp.com/servers/visibility#filtering-logic)
  * [The Visibility Transform](https://gofastmcp.com/servers/visibility#the-visibility-transform)


Transforms
# Component Visibility
Copy page
Control which components are available to clients
Copy page
`3.0.0` Components can be dynamically enabled or disabled at runtime. A disabled tool disappears from listings and cannot be called. This enables runtime access control, feature flags, and context-aware component exposure.
##
[​](https://gofastmcp.com/servers/visibility#component-visibility)
Component Visibility
Every FastMCP server provides `enable()` and `disable()` methods for controlling component availability.
###
[​](https://gofastmcp.com/servers/visibility#disabling-components)
Disabling Components
The `disable()` method marks components as disabled. Disabled components are filtered out from all client queries.
Copy
```
from fastmcp import FastMCP

mcp = FastMCP("Server")

@mcp.tool(tags={"admin"})
def delete_everything() -> str:
    """Delete all data."""
    return "Deleted"

@mcp.tool(tags={"admin"})
def reset_system() -> str:
    """Reset the system."""
    return "Reset"

@mcp.tool
def get_status() -> str:
    """Get system status."""
    return "OK"

# Disable admin tools
mcp.disable(tags={"admin"})

# Clients only see: get_status

```

###
[​](https://gofastmcp.com/servers/visibility#enabling-components)
Enabling Components
The `enable()` method re-enables previously disabled components.
Copy
```
# Re-enable admin tools
mcp.enable(tags={"admin"})

# Clients now see all three tools

```

##
[​](https://gofastmcp.com/servers/visibility#keys-and-tags)
Keys and Tags
Visibility filtering works with two identifiers: keys (for specific components) and tags (for groups).
###
[​](https://gofastmcp.com/servers/visibility#component-keys)
Component Keys
Every component has a unique key in the format `{type}:{identifier}`.
Component | Key Format | Example
---|---|---
Tool | `tool:{name}` | `tool:delete_everything`
Resource | `resource:{uri}` | `resource:data://config`
Template | `template:{uri}` | `template:file://{path}`
Prompt | `prompt:{name}` | `prompt:analyze`
Use keys to target specific components.
Copy
```
# Disable a specific tool
mcp.disable(keys={"tool:delete_everything"})

# Disable multiple specific components
mcp.disable(keys={"tool:reset_system", "resource:data://secrets"})

```

###
[​](https://gofastmcp.com/servers/visibility#tags)
Tags
Tags group components for bulk operations. Define tags when creating components, then filter by them.
Copy
```
from fastmcp import FastMCP

mcp = FastMCP("Server")

@mcp.tool(tags={"public", "read"})
def get_data() -> str:
    return "data"

@mcp.tool(tags={"admin", "write"})
def set_data(value: str) -> str:
    return f"Set: {value}"

@mcp.tool(tags={"admin", "dangerous"})
def delete_data() -> str:
    return "Deleted"

# Disable all admin tools
mcp.disable(tags={"admin"})

# Disable all dangerous tools (some overlap with admin)
mcp.disable(tags={"dangerous"})

```

A component is disabled if it has **any** of the disabled tags. The component doesn’t need all the tags; one match is enough.
###
[​](https://gofastmcp.com/servers/visibility#combining-keys-and-tags)
Combining Keys and Tags
You can specify both keys and tags in a single call. The filters combine additively.
Copy
```
# Disable specific tools AND all dangerous-tagged components
mcp.disable(keys={"tool:debug_info"}, tags={"dangerous"})

```

##
[​](https://gofastmcp.com/servers/visibility#allowlist-mode)
Allowlist Mode
By default, visibility filtering uses blocklist mode: everything is enabled unless explicitly disabled. The `only=True` parameter switches to allowlist mode, where **only** specified components are enabled.
Copy
```
from fastmcp import FastMCP

mcp = FastMCP("Server")

@mcp.tool(tags={"safe"})
def read_only_operation() -> str:
    return "Read"

@mcp.tool(tags={"safe"})
def list_items() -> list[str]:
    return ["a", "b", "c"]

@mcp.tool(tags={"dangerous"})
def delete_all() -> str:
    return "Deleted"

@mcp.tool
def untagged_tool() -> str:
    return "Untagged"

# Only enable safe tools - everything else is disabled
mcp.enable(tags={"safe"}, only=True)

# Clients see: read_only_operation, list_items
# Disabled: delete_all, untagged_tool

```

Allowlist mode is useful for restrictive environments where you want to explicitly opt-in components rather than opt-out.
###
[​](https://gofastmcp.com/servers/visibility#allowlist-behavior)
Allowlist Behavior
When you call `enable(only=True)`:
  1. Default visibility state switches to “disabled”
  2. Previous allowlists are cleared
  3. Only specified keys/tags become enabled


Copy
```
# Start fresh - only enable these specific tools
mcp.enable(keys={"tool:safe_read", "tool:safe_write"}, only=True)

# Later, switch to a different allowlist
mcp.enable(tags={"production"}, only=True)

```

###
[​](https://gofastmcp.com/servers/visibility#ordering-and-overrides)
Ordering and Overrides
Later `enable()` and `disable()` calls override earlier ones. This lets you create broad rules with specific exceptions.
Copy
```
mcp.enable(tags={"api"}, only=True)  # Allow all api-tagged
mcp.disable(keys={"tool:api_admin"})  # Later disable overrides for this tool

# api_admin is disabled because the later disable() overrides the allowlist

```

You can always re-enable something that was disabled by adding another `enable()` call after it.
##
[​](https://gofastmcp.com/servers/visibility#server-vs-provider)
Server vs Provider
Visibility state operates at two levels: the server and individual providers.
###
[​](https://gofastmcp.com/servers/visibility#server-level)
Server-Level
Server-level visibility state applies to all components from all providers. When you call `mcp.enable()` or `mcp.disable()`, you’re filtering the final view that clients see.
Copy
```
from fastmcp import FastMCP

main = FastMCP("Main")
main.mount(sub_server, namespace="api")

@main.tool(tags={"internal"})
def local_debug() -> str:
    return "Debug"

# Disable internal tools from ALL sources
main.disable(tags={"internal"})

```

###
[​](https://gofastmcp.com/servers/visibility#provider-level)
Provider-Level
Each provider can add its own visibility transforms. These run before server-level transforms, so the server can override provider-level disables.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.providers import LocalProvider

# Create provider with visibility control
admin_tools = LocalProvider()

@admin_tools.tool(tags={"admin"})
def admin_action() -> str:
    return "Admin"

@admin_tools.tool
def regular_action() -> str:
    return "Regular"

# Disable at provider level
admin_tools.disable(tags={"admin"})

# Server can override if needed
mcp = FastMCP("Server", providers=[admin_tools])
mcp.enable(names={"admin_action"})  # Re-enables despite provider disable

```

Provider-level transforms are useful for setting default visibility that servers can selectively override.
###
[​](https://gofastmcp.com/servers/visibility#layered-transforms)
Layered Transforms
Provider transforms run first, then server transforms. Later transforms override earlier ones, so the server has final say.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.providers import LocalProvider

provider = LocalProvider()

@provider.tool(tags={"feature", "beta"})
def new_feature() -> str:
    return "New"

# Provider enables feature-tagged
provider.enable(tags={"feature"}, only=True)

# Server disables beta-tagged (runs after provider)
mcp = FastMCP("Server", providers=[provider])
mcp.disable(tags={"beta"})

# new_feature is disabled (server's later disable overrides provider's enable)

```

##
[​](https://gofastmcp.com/servers/visibility#per-session-visibility)
Per-Session Visibility
Server-level visibility changes affect all connected clients simultaneously. When you need different clients to see different components, use per-session visibility instead. Session visibility lets individual sessions customize their view of available components. When a tool calls `ctx.enable_components()` or `ctx.disable_components()`, those rules apply only to the current session. Other sessions continue to see the global defaults. This enables patterns like progressive disclosure, role-based access, and on-demand feature activation.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.context import Context

mcp = FastMCP("Session-Aware Server")

@mcp.tool(tags={"premium"})
def premium_analysis(data: str) -> str:
    """Advanced analysis available to premium users."""
    return f"Premium analysis of: {data}"

@mcp.tool
async def unlock_premium(ctx: Context) -> str:
    """Unlock premium features for this session."""
    await ctx.enable_components(tags={"premium"})
    return "Premium features unlocked"

@mcp.tool
async def reset_features(ctx: Context) -> str:
    """Reset to default feature set."""
    await ctx.reset_visibility()
    return "Features reset to defaults"

# Premium tools are disabled globally by default
mcp.disable(tags={"premium"})

```

All sessions start with `premium_analysis` hidden. When a session calls `unlock_premium`, that session gains access to premium tools while other sessions remain unaffected. Calling `reset_features` returns the session to the global defaults.
###
[​](https://gofastmcp.com/servers/visibility#how-session-rules-work)
How Session Rules Work
Session rules override global transforms. When listing components, FastMCP first applies global enable/disable rules, then applies session-specific rules on top. Rules within a session accumulate, and later rules override earlier ones for the same component.
Copy
```
@mcp.tool
async def customize_session(ctx: Context) -> str:
    # Enable finance tools for this session
    await ctx.enable_components(tags={"finance"})

    # Also enable admin tools
    await ctx.enable_components(tags={"admin"})

    # Later: disable a specific admin tool
    await ctx.disable_components(names={"dangerous_admin_tool"})

    return "Session customized"

```

Each call adds a rule to the session. The `dangerous_admin_tool` ends up disabled because its disable rule was added after the admin enable rule.
###
[​](https://gofastmcp.com/servers/visibility#filter-criteria)
Filter Criteria
The session visibility methods accept the same filter criteria as `server.enable()` and `server.disable()`:
Parameter | Description
---|---
`names` | Component names or URIs to match
`keys` | Component keys (e.g., `{"tool:my_tool"}`)
`tags` | Tags to match (component must have at least one)
`version` | Version specification to match
`components` | Component types (`{"tool"}`, `{"resource"}`, `{"prompt"}`, `{"template"}`)
`match_all` | If `True`, matches all components regardless of other criteria
Copy
```
from fastmcp.utilities.versions import VersionSpec

@mcp.tool
async def enable_recent_tools(ctx: Context) -> str:
    """Enable only tools from version 2.0.0 or later."""
    await ctx.enable_components(
        version=VersionSpec(gte="2.0.0"),
        components={"tool"}
    )
    return "Recent tools enabled"

```

###
[​](https://gofastmcp.com/servers/visibility#automatic-notifications)
Automatic Notifications
When session visibility changes, FastMCP automatically sends notifications to that session. Clients receive `ToolListChangedNotification`, `ResourceListChangedNotification`, and `PromptListChangedNotification` so they can refresh their component lists. These notifications go only to the affected session. When you specify the `components` parameter, FastMCP optimizes by sending only the relevant notifications:
Copy
```
# Only sends ToolListChangedNotification
await ctx.enable_components(tags={"finance"}, components={"tool"})

# Sends all three notifications (no components filter)
await ctx.enable_components(tags={"finance"})

```

###
[​](https://gofastmcp.com/servers/visibility#namespace-activation-pattern)
Namespace Activation Pattern
A common pattern organizes tools into namespaces using tag prefixes, disables them globally, then provides activation tools that unlock namespaces on demand:
Copy
```
from fastmcp import FastMCP
from fastmcp.server.context import Context

server = FastMCP("Multi-Domain Assistant")

# Finance namespace
@server.tool(tags={"namespace:finance"})
def analyze_portfolio(symbols: list[str]) -> str:
    return f"Analysis for: {', '.join(symbols)}"

@server.tool(tags={"namespace:finance"})
def get_market_data(symbol: str) -> dict:
    return {"symbol": symbol, "price": 150.25}

# Admin namespace
@server.tool(tags={"namespace:admin"})
def list_users() -> list[str]:
    return ["alice", "bob", "charlie"]

# Activation tools - always visible
@server.tool
async def activate_finance(ctx: Context) -> str:
    await ctx.enable_components(tags={"namespace:finance"})
    return "Finance tools activated"

@server.tool
async def activate_admin(ctx: Context) -> str:
    await ctx.enable_components(tags={"namespace:admin"})
    return "Admin tools activated"

@server.tool
async def deactivate_all(ctx: Context) -> str:
    await ctx.reset_visibility()
    return "All namespaces deactivated"

# Disable namespace tools globally
server.disable(tags={"namespace:finance", "namespace:admin"})

```

Sessions start seeing only the activation tools. Calling `activate_finance` reveals finance tools for that session only. Multiple namespaces can be activated independently, and `deactivate_all` returns to the initial state.
###
[​](https://gofastmcp.com/servers/visibility#method-reference)
Method Reference
  * **`await ctx.enable_components(...) -> None`**: Enable matching components for this session
  * **`await ctx.disable_components(...) -> None`**: Disable matching components for this session
  * **`await ctx.reset_visibility() -> None`**: Clear all session rules, returning to global defaults


##
[​](https://gofastmcp.com/servers/visibility#client-notifications)
Client Notifications
When visibility state changes, FastMCP automatically notifies connected clients. Clients supporting the MCP notification protocol receive `list_changed` events and can refresh their component lists. This happens automatically. You don’t need to trigger notifications manually.
Copy
```
# This automatically notifies clients
mcp.disable(tags={"maintenance"})

# Clients receive: tools/list_changed, resources/list_changed, etc.

```

##
[​](https://gofastmcp.com/servers/visibility#filtering-logic)
Filtering Logic
Understanding the filtering logic helps when debugging visibility state issues. The `is_enabled()` function checks a component’s internal metadata:
  1. If the component has `meta.fastmcp._internal.visibility = False`, it’s disabled
  2. If the component has `meta.fastmcp._internal.visibility = True`, it’s enabled
  3. If no visibility state is set, the component is enabled by default

When multiple `enable()` and `disable()` calls are made, transforms are applied in order. **Later transforms override earlier ones** , so the last matching transform wins.
##
[​](https://gofastmcp.com/servers/visibility#the-visibility-transform)
The Visibility Transform
Under the hood, `enable()` and `disable()` add `Visibility` transforms to the server or provider. The `Visibility` transform marks components with visibility metadata, and the server applies the final filter after all provider and server transforms complete.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.transforms import Visibility

mcp = FastMCP("Server")

# Using the convenience method (recommended)
mcp.disable(names={"secret_tool"})

# Equivalent to:
mcp.add_transform(Visibility(False, names={"secret_tool"}))

```

Server-level transforms override provider-level transforms. If a component is disabled at the provider level but enabled at the server level, the server-level `enable()` can re-enable it.
[ Tool Transformation Previous ](https://gofastmcp.com/servers/transforms/tool-transformation)[ Code Mode Next ](https://gofastmcp.com/servers/transforms/code-mode)
Ctrl+I
