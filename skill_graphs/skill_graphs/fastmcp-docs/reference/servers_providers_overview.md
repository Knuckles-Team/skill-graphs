[Skip to main content](https://gofastmcp.com/servers/providers/overview#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Providers
Providers
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
    * [ Overview NEW ](https://gofastmcp.com/servers/providers/overview)
    * [ Local NEW ](https://gofastmcp.com/servers/providers/local)
    * [ Filesystem NEW ](https://gofastmcp.com/servers/providers/filesystem)
    * [MCP Proxy](https://gofastmcp.com/servers/providers/proxy)
    * [ Skills NEW ](https://gofastmcp.com/servers/providers/skills)
    * [ Custom NEW ](https://gofastmcp.com/servers/providers/custom)
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
  * [What Is a Provider?](https://gofastmcp.com/servers/providers/overview#what-is-a-provider)
  * [Why Providers?](https://gofastmcp.com/servers/providers/overview#why-providers)
  * [Built-in Providers](https://gofastmcp.com/servers/providers/overview#built-in-providers)
  * [Transforms](https://gofastmcp.com/servers/providers/overview#transforms)
  * [Provider Order](https://gofastmcp.com/servers/providers/overview#provider-order)
  * [When to Care About Providers](https://gofastmcp.com/servers/providers/overview#when-to-care-about-providers)
  * [Next Steps](https://gofastmcp.com/servers/providers/overview#next-steps)


Providers
# Providers
Copy page
How FastMCP sources tools, resources, and prompts
Copy page
`3.0.0` Every FastMCP server has one or more component providers. A provider is a source of tools, resources, and prompts - it’s what makes components available to clients.
##
[​](https://gofastmcp.com/servers/providers/overview#what-is-a-provider)
What Is a Provider?
When a client connects to your server and asks “what tools do you have?”, FastMCP asks each provider that question and combines the results. When a client calls a specific tool, FastMCP finds which provider has it and delegates the call. You’re already using providers. When you write `@mcp.tool`, you’re adding a tool to your server’s `LocalProvider` - the default provider that stores components you define directly in code. You just don’t have to think about it for simple servers. Providers become important when your components come from multiple sources: another FastMCP server to include, a remote MCP server to proxy, or a database where tools are defined dynamically. Each source gets its own provider, and FastMCP queries them all seamlessly.
##
[​](https://gofastmcp.com/servers/providers/overview#why-providers)
Why Providers?
The provider abstraction solves a common problem: as servers grow, you need to organize components across multiple sources without tangling everything together. **Composition** : Break a large server into focused modules. A “weather” server and a “calendar” server can each be developed independently, then mounted into a main server. Each mounted server becomes a `FastMCPProvider`. **Proxying** : Expose a remote MCP server through your local server. Maybe you’re bridging transports (remote HTTP to local stdio) or aggregating multiple backends. Remote connections become `ProxyProvider` instances. **Dynamic sources** : Load tools from a database, generate them from an OpenAPI spec, or create them based on user permissions. Custom providers let components come from anywhere.
##
[​](https://gofastmcp.com/servers/providers/overview#built-in-providers)
Built-in Providers
FastMCP includes providers for common patterns:
Provider | What it does | How you use it
---|---|---
`LocalProvider` | Stores components you define in code |  `@mcp.tool`, `mcp.add_tool()`
`FastMCPProvider` | Wraps another FastMCP server | `mcp.mount(server)`
`ProxyProvider` | Connects to remote MCP servers | `create_proxy(client)`
Most users only interact with `LocalProvider` (through decorators) and occasionally mount or proxy other servers. The provider abstraction stays invisible until you need it.
##
[​](https://gofastmcp.com/servers/providers/overview#transforms)
Transforms
[Transforms](https://gofastmcp.com/servers/transforms/transforms) modify components as they flow from providers to clients. Each transform sits in a chain, intercepting queries and modifying results before passing them along.
Transform | Purpose
---|---
`Namespace` | Prefixes names to avoid conflicts
`ToolTransform` | Modifies tool schemas (rename, description, arguments)
The most common use is namespacing mounted servers to prevent name collisions. When you call `mount(server, namespace="api")`, FastMCP creates a `Namespace` transform automatically. Transforms can be added to individual providers (affecting just that source) or to the server itself (affecting all components). See [Transforms](https://gofastmcp.com/servers/transforms/transforms) for the full picture.
##
[​](https://gofastmcp.com/servers/providers/overview#provider-order)
Provider Order
When a client requests a tool, FastMCP queries providers in registration order. The first provider that has the tool handles the request. `LocalProvider` is always first, so your decorator-defined tools take precedence. Additional providers are queried in the order you added them. This means if two providers have a tool with the same name, the first one wins.
##
[​](https://gofastmcp.com/servers/providers/overview#when-to-care-about-providers)
When to Care About Providers
**You can ignore providers entirely** if you’re building a simple server with decorators. Just use `@mcp.tool`, `@mcp.resource`, and `@mcp.prompt` - FastMCP handles the rest. **Learn about providers when** you want to:
  * [Mount another server](https://gofastmcp.com/servers/composition) into yours
  * [Proxy a remote server](https://gofastmcp.com/servers/providers/proxy) through yours
  * [Control visibility state](https://gofastmcp.com/servers/visibility) of components
  * [Build dynamic sources](https://gofastmcp.com/servers/providers/custom) like database-backed tools


##
[​](https://gofastmcp.com/servers/providers/overview#next-steps)
Next Steps
  * [Local](https://gofastmcp.com/servers/providers/local) - How decorators work
  * [Mounting](https://gofastmcp.com/servers/composition) - Compose servers together
  * [Proxying](https://gofastmcp.com/servers/providers/proxy) - Connect to remote servers
  * [Transforms](https://gofastmcp.com/servers/transforms/transforms) - Namespace, rename, and modify components
  * [Visibility](https://gofastmcp.com/servers/visibility) - Control which components clients can access
  * [Custom](https://gofastmcp.com/servers/providers/custom) - Build your own providers


[ Versioning Previous ](https://gofastmcp.com/servers/versioning)[ Local Provider Next ](https://gofastmcp.com/servers/providers/local)
Ctrl+I
