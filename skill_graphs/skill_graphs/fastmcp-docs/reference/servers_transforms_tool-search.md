[Skip to main content](https://gofastmcp.com/servers/transforms/tool-search#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Transforms
Tool Search
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
  * [How It Works](https://gofastmcp.com/servers/transforms/tool-search#how-it-works)
  * [Search Strategies](https://gofastmcp.com/servers/transforms/tool-search#search-strategies)
  * [Regex Search](https://gofastmcp.com/servers/transforms/tool-search#regex-search)
  * [BM25 Search](https://gofastmcp.com/servers/transforms/tool-search#bm25-search)
  * [Which to Choose](https://gofastmcp.com/servers/transforms/tool-search#which-to-choose)
  * [Configuration](https://gofastmcp.com/servers/transforms/tool-search#configuration)
  * [Limiting Results](https://gofastmcp.com/servers/transforms/tool-search#limiting-results)
  * [Pinning Tools](https://gofastmcp.com/servers/transforms/tool-search#pinning-tools)
  * [Custom Tool Names](https://gofastmcp.com/servers/transforms/tool-search#custom-tool-names)
  * [The call_tool Proxy](https://gofastmcp.com/servers/transforms/tool-search#the-call_tool-proxy)
  * [Auth and Visibility](https://gofastmcp.com/servers/transforms/tool-search#auth-and-visibility)


Transforms
# Tool Search
Copy page
Replace large tool catalogs with on-demand search
Copy page
`3.1.0` When a server exposes hundreds or thousands of tools, sending the full catalog to an LLM wastes tokens and degrades tool selection accuracy. Search transforms solve this by replacing the tool listing with a search interface — the LLM discovers tools on demand instead of receiving everything upfront.
##
[​](https://gofastmcp.com/servers/transforms/tool-search#how-it-works)
How It Works
When you add a search transform, `list_tools()` returns just two synthetic tools instead of the full catalog:
  * **`search_tools`**finds tools matching a query and returns their full definitions
  * **`call_tool`**executes a discovered tool by name

The original tools are still callable. They’re hidden from the listing but remain fully functional — the search transform controls _discovery_ , not _access_. Both synthetic tools search across tool names, descriptions, parameter names, and parameter descriptions. A search for `"email"` would match a tool named `send_email`, a tool with “email” in its description, or a tool with an `email_address` parameter. Search results are returned in the same JSON format as `list_tools`, including the full input schema, so the LLM can construct valid calls immediately without a second round-trip.
##
[​](https://gofastmcp.com/servers/transforms/tool-search#search-strategies)
Search Strategies
FastMCP provides two search transforms. They share the same interface — two synthetic tools, same configuration options — but differ in how they match queries to tools.
###
[​](https://gofastmcp.com/servers/transforms/tool-search#regex-search)
Regex Search
`RegexSearchTransform` matches tools against a regex pattern using case-insensitive `re.search`. It has zero overhead and no index to build, making it a good default when the LLM knows roughly what it’s looking for.
Copy
```
from fastmcp import FastMCP
from fastmcp.server.transforms.search import RegexSearchTransform

mcp = FastMCP("My Server", transforms=[RegexSearchTransform()])

@mcp.tool
def search_database(query: str, limit: int = 10) -> list[dict]:
    """Search the database for records matching the query."""
    ...

@mcp.tool
def delete_record(record_id: str) -> bool:
    """Delete a record from the database by its ID."""
    ...

@mcp.tool
def send_email(to: str, subject: str, body: str) -> bool:
    """Send an email to the given recipient."""
    ...

```

The LLM’s `search_tools` call takes a `pattern` parameter — a regex string:
Copy
```
# Exact substring match
result = await client.call_tool("search_tools", {"pattern": "database"})
# Returns: search_database, delete_record

# Regex pattern
result = await client.call_tool("search_tools", {"pattern": "send.*email|notify"})
# Returns: send_email

```

Results are returned in catalog order. If the pattern is invalid regex, the search returns an empty list rather than raising an error.
###
[​](https://gofastmcp.com/servers/transforms/tool-search#bm25-search)
BM25 Search
`BM25SearchTransform` ranks tools by relevance using the
Copy
```
from fastmcp import FastMCP
from fastmcp.server.transforms.search import BM25SearchTransform

mcp = FastMCP("My Server", transforms=[BM25SearchTransform()])

# ... define tools ...

```

The LLM’s `search_tools` call takes a `query` parameter — natural language:
Copy
```
result = await client.call_tool("search_tools", {
    "query": "tools for deleting things from the database"
})
# Returns: delete_record ranked first, search_database second

```

BM25 builds an in-memory index from the searchable text of all tools. The index is created lazily on the first search and automatically rebuilt whenever the tool catalog changes — for example, when tools are added, removed, or have their descriptions updated. The staleness check is based on a hash of all searchable text, so description changes are detected even when tool names stay the same.
###
[​](https://gofastmcp.com/servers/transforms/tool-search#which-to-choose)
Which to Choose
Use **regex** when your LLM is good at constructing targeted patterns and you want deterministic, predictable results. Regex is also simpler to debug — you can see exactly what pattern was sent. Use **BM25** when your LLM tends to describe what it needs in natural language, or when your tool catalog has nuanced descriptions where relevance ranking adds value. BM25 handles partial matches and synonyms better because it scores on individual terms rather than requiring a single pattern to match.
##
[​](https://gofastmcp.com/servers/transforms/tool-search#configuration)
Configuration
Both search transforms accept the same configuration options.
###
[​](https://gofastmcp.com/servers/transforms/tool-search#limiting-results)
Limiting Results
By default, search returns at most 5 tools. Adjust `max_results` based on your catalog size and how much context you want the LLM to receive per search:
Copy
```
mcp.add_transform(RegexSearchTransform(max_results=10))
mcp.add_transform(BM25SearchTransform(max_results=3))

```

With regex, results stop as soon as the limit is reached (first N matches in catalog order). With BM25, all tools are scored and the top N by relevance are returned.
###
[​](https://gofastmcp.com/servers/transforms/tool-search#pinning-tools)
Pinning Tools
Some tools should always be visible regardless of search. Use `always_visible` to pin them in the listing alongside the synthetic tools:
Copy
```
mcp.add_transform(RegexSearchTransform(
    always_visible=["help", "status"],
))

# list_tools returns: help, status, search_tools, call_tool

```

Pinned tools appear directly in `list_tools` so the LLM can call them without searching. They’re excluded from search results to avoid duplication.
###
[​](https://gofastmcp.com/servers/transforms/tool-search#custom-tool-names)
Custom Tool Names
The default names `search_tools` and `call_tool` can be changed to avoid conflicts with real tools:
Copy
```
mcp.add_transform(RegexSearchTransform(
    search_tool_name="find_tools",
    call_tool_name="run_tool",
))

```

##
[​](https://gofastmcp.com/servers/transforms/tool-search#the-call_tool-proxy)
The `call_tool` Proxy
The `call_tool` proxy forwards calls to the real tool. When a client calls `call_tool(name="search_database", arguments={...})`, the proxy resolves `search_database` through the server’s normal tool pipeline — including transforms and middleware — and executes it. The proxy rejects attempts to call the synthetic tools themselves. `call_tool(name="call_tool")` raises an error rather than recursing.
Tools discovered through search can also be called directly via `client.call_tool("search_database", {...})` without going through the proxy. The proxy exists for LLMs that only know about the tools returned by `list_tools` and need a way to invoke discovered tools through a tool they can see.
##
[​](https://gofastmcp.com/servers/transforms/tool-search#auth-and-visibility)
Auth and Visibility
Search results respect the full authorization pipeline. Tools filtered by middleware, visibility transforms, or component-level auth checks won’t appear in search results. The search tool queries `list_tools()` through the complete pipeline at search time, so the same filtering that controls what a client sees in the listing also controls what they can discover through search.
Copy
```
from fastmcp.server.transforms import Visibility
from fastmcp.server.transforms.search import RegexSearchTransform

mcp = FastMCP("My Server")

# ... define tools ...

# Disable admin tools globally
mcp.add_transform(Visibility(False, tags={"admin"}))

# Add search — admin tools won't appear in results
mcp.add_transform(RegexSearchTransform())

```

Session-level visibility changes (via `ctx.disable_components()`) are also reflected immediately in search results.
[ Code Mode Previous ](https://gofastmcp.com/servers/transforms/code-mode)[ Resources as Tools Next ](https://gofastmcp.com/servers/transforms/resources-as-tools)
Ctrl+I
