[Skip to main content](https://gofastmcp.com/servers/transforms/code-mode#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Transforms
Code Mode
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
  * [Getting Started](https://gofastmcp.com/servers/transforms/code-mode#getting-started)
  * [Discovery](https://gofastmcp.com/servers/transforms/code-mode#discovery)
  * [Discovery Tools](https://gofastmcp.com/servers/transforms/code-mode#discovery-tools)
  * [Detail Levels](https://gofastmcp.com/servers/transforms/code-mode#detail-levels)
  * [Search](https://gofastmcp.com/servers/transforms/code-mode#search)
  * [GetSchemas](https://gofastmcp.com/servers/transforms/code-mode#getschemas)
  * [GetTags](https://gofastmcp.com/servers/transforms/code-mode#gettags)
  * [ListTools](https://gofastmcp.com/servers/transforms/code-mode#listtools)
  * [Discovery Patterns](https://gofastmcp.com/servers/transforms/code-mode#discovery-patterns)
  * [Three-Stage](https://gofastmcp.com/servers/transforms/code-mode#three-stage)
  * [Two-Stage](https://gofastmcp.com/servers/transforms/code-mode#two-stage)
  * [Single-Stage](https://gofastmcp.com/servers/transforms/code-mode#single-stage)
  * [Custom Discovery Tools](https://gofastmcp.com/servers/transforms/code-mode#custom-discovery-tools)
  * [Sandbox Configuration](https://gofastmcp.com/servers/transforms/code-mode#sandbox-configuration)
  * [Resource Limits](https://gofastmcp.com/servers/transforms/code-mode#resource-limits)
  * [Custom Sandbox Providers](https://gofastmcp.com/servers/transforms/code-mode#custom-sandbox-providers)


Transforms
# Code Mode
Copy page
Let LLMs write Python to orchestrate tools in a sandbox
Copy page
`3.1.0`
CodeMode is experimental. The core interface is stable, but the specific discovery tools and their parameters may evolve as we learn more about what works best in practice.
Standard MCP tool usage has two scaling problems. First, every tool in the catalog is loaded into the LLM’s context upfront — with hundreds of tools, that’s tens of thousands of tokens spent before the LLM even reads the user’s request. Second, every tool call is a round-trip: the LLM calls a tool, the result passes back through the context window, the LLM reasons about it, calls another tool, and so on. Intermediate results that only exist to feed the next step still burn tokens flowing through the model. CodeMode solves both problems. Instead of seeing your entire tool catalog, the LLM gets meta-tools for discovering what’s available and for writing and executing code that calls the tools it needs. It discovers on demand, writes a script that chains tool calls in a sandbox, and gets back only the final answer. The approach was introduced by Cloudflare in
##
[​](https://gofastmcp.com/servers/transforms/code-mode#getting-started)
Getting Started
CodeMode requires the `code-mode` extra for sandbox support. Install it with `pip install "fastmcp[code-mode]"`.
You take a normal server with normally registered tools and add a `CodeMode` transform. The transform wraps your existing tools in the code mode machinery — your tool functions don’t change at all:
Copy
```
from fastmcp import FastMCP
from fastmcp.experimental.transforms.code_mode import CodeMode

mcp = FastMCP("Server", transforms=[CodeMode()])

@mcp.tool
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

@mcp.tool
def multiply(x: int, y: int) -> int:
    """Multiply two numbers."""
    return x * y

```

Clients connecting to this server no longer see `add` and `multiply` directly. Instead, they see the meta-tools that CodeMode provides — tools for discovering what’s available and executing code against it. The original tools are still there, but they’re accessed through the CodeMode layer.
##
[​](https://gofastmcp.com/servers/transforms/code-mode#discovery)
Discovery
Before the LLM can write code that calls your tools, it needs to know what tools exist and how to call them. This is the **discovery** process — the LLM uses meta-tools to learn about your tool catalog, then writes code against what it finds. The fundamental tradeoff is **tokens vs. round-trips**. Each discovery step is an LLM round-trip: the model calls a tool, waits for the response, reasons about it, then decides what to do next. More steps mean less wasted context (each step is targeted) but more latency and API calls. Fewer steps mean the LLM gets information upfront but pays for detail it might not need. By default, CodeMode gives the LLM three tools — `search`, `get_schema`, and `execute` — creating a three-stage discovery flow:
1
[](https://gofastmcp.com/servers/transforms/code-mode)
Search for tools
First, the LLM uses the `search` meta-tool to find tools by keyword.For example, it might do `search(query="math numbers")` and receive the following response:
Copy
```
- add: Add two numbers.
- multiply: Multiply two numbers.

```

This lets the LLM know which tools are available and what they do, significantly reducing the surface area it needs to consider.
2
[](https://gofastmcp.com/servers/transforms/code-mode)
Get parameter details for the tools
Next, the LLM calls `get_schema` to get parameter details for the tools it found in the previous step.For example, it might do `get_schema(tools=["add", "multiply"])` and receive the following response:
Copy
```
### add

Add two numbers.

**Parameters**
- `x` (integer, required)
- `y` (integer, required)

### multiply

Multiply two numbers.

**Parameters**
- `x` (integer, required)
- `y` (integer, required)

```

Now the LLM knows the parameters for the tools it found, and can write code that chains the tool calls. If it needed more detail, it could have called `get_schema` with `detail="full"` to get the complete JSON schema.
3
[](https://gofastmcp.com/servers/transforms/code-mode)
Write and execute code that chains the tool calls
Finally, the LLM writes and executes code that chains the tool calls in a Python sandbox. Inside the sandbox, `call_tool(name, params)` is the only function available. The LLM uses this to compose tools into a workflow and return a final result.For example, it might write the following code and call the `execute` tool with it:
Copy
```
a = await call_tool("add", {"x": 3, "y": 4})
b = await call_tool("multiply", {"x": a, "y": 2})
return b

```

The result is returned to the LLM.
This three-stage flow works well for most servers — each step pulls in only the information needed for the next one, keeping context usage minimal. But CodeMode’s discovery surface is fully configurable. The sections below explain each built-in discovery tool and how to combine them into different patterns.
##
[​](https://gofastmcp.com/servers/transforms/code-mode#discovery-tools)
Discovery Tools
CodeMode ships with four built-in discovery tools: `Search`, `GetSchemas`, `GetTags`, and `ListTools`. By default, only `Search` and `GetSchemas` are enabled. Each tool supports a `default_detail` parameter that sets the default verbosity level, and the LLM can override the detail level on any individual call.
###
[​](https://gofastmcp.com/servers/transforms/code-mode#detail-levels)
Detail Levels
`Search` and `GetSchemas` share the same three detail levels, so the same `detail` value produces the same output format regardless of which tool the LLM calls:
Level | Output | Token cost
---|---|---
`"brief"` | Tool names and one-line descriptions | Cheapest — good for scanning
`"detailed"` | Compact markdown with parameter names, types, and required markers | Medium — often enough to write code
`"full"` | Complete JSON schema | Most expensive — everything
`Search` defaults to `"brief"` and `GetSchemas` defaults to `"detailed"`.
###
[​](https://gofastmcp.com/servers/transforms/code-mode#search)
Search
`Search` finds tools by natural-language query using BM25 ranking. At its default `"brief"` detail, results include just tool names and descriptions — enough to decide which tools are worth inspecting further. The LLM can request `"detailed"` to get parameter schemas inline, or `"full"` for the complete JSON. Search results include an annotation like `"2 of 10 tools:"` when the result set is smaller than the full catalog, so the LLM knows there are more tools to discover with different queries. You can cap result count with `default_limit`. The LLM can also override the limit per call. This is useful for large catalogs where you want to keep search results focused:
Copy
```
Search(default_limit=5)  # return at most 5 results per search

```

If your tools use [tags](https://gofastmcp.com/servers/tools#tags), Search also accepts a `tags` parameter so the LLM can narrow results to specific categories before searching.
###
[​](https://gofastmcp.com/servers/transforms/code-mode#getschemas)
GetSchemas
`GetSchemas` returns parameter details for specific tools by name. At its default `"detailed"` level, it renders compact markdown with parameter names, types, and required markers. At `"full"`, it returns the complete JSON schema — useful when tools have deeply nested parameters that the compact format doesn’t capture.
###
[​](https://gofastmcp.com/servers/transforms/code-mode#gettags)
GetTags
`GetTags` lets the LLM browse tools by category using [tag](https://gofastmcp.com/servers/tools#tags) metadata. At brief detail, the LLM sees tag names with counts. At full detail, it sees tools listed under each tag:
Copy
```
- math (3 tools)
- text (2 tools)
- untagged (1 tool)

```

`GetTags` isn’t included in the defaults — add it when browsing by category would help the LLM orient itself in a large catalog. The LLM can browse tags first, then pass specific tags into Search to narrow results.
###
[​](https://gofastmcp.com/servers/transforms/code-mode#listtools)
ListTools
`ListTools` dumps the entire catalog at whatever detail level the LLM requests. It supports the same three detail levels as `Search` and `GetSchemas`, defaulting to `"brief"`. `ListTools` isn’t included in the defaults — for large catalogs, search-based discovery is more token-efficient. But for smaller catalogs (under ~20 tools), letting the LLM see everything upfront can be faster than multiple search round-trips:
Copy
```
from fastmcp.experimental.transforms.code_mode import CodeMode, ListTools, GetSchemas

code_mode = CodeMode(
    discovery_tools=[ListTools(), GetSchemas()],
)

```

##
[​](https://gofastmcp.com/servers/transforms/code-mode#discovery-patterns)
Discovery Patterns
The right discovery configuration depends on your server — how many tools you have and how complex their parameters are. It may be tempting to minimize round-trips by collapsing everything into fewer steps, but for the complex servers that benefit most from CodeMode, our experience is that staged discovery leads to better results. Flooding the LLM with detailed schemas for tools it doesn’t end up using can hurt more than the extra round-trip costs. Each pattern below is a complete, copyable configuration.
###
[​](https://gofastmcp.com/servers/transforms/code-mode#three-stage)
Three-Stage
The default. The LLM searches for candidates, inspects schemas for the ones it wants, then writes code. Best for **large or complex tool sets** where you want to minimize context usage — the LLM only pays for schemas it actually needs.
Copy
```
from fastmcp import FastMCP
from fastmcp.experimental.transforms.code_mode import CodeMode

mcp = FastMCP("Server", transforms=[CodeMode()])

```

If your tools use [tags](https://gofastmcp.com/servers/tools#tags), add `GetTags` so the LLM can browse by category before searching — giving it four stages of progressive disclosure:
Copy
```
from fastmcp import FastMCP
from fastmcp.experimental.transforms.code_mode import CodeMode
from fastmcp.experimental.transforms.code_mode import GetTags, Search, GetSchemas

code_mode = CodeMode(
    discovery_tools=[GetTags(), Search(), GetSchemas()],
)

mcp = FastMCP("Server", transforms=[code_mode])

```

###
[​](https://gofastmcp.com/servers/transforms/code-mode#two-stage)
Two-Stage
Search returns parameter schemas inline, so the LLM can go straight from search to execute. Best for **smaller catalogs** where the extra tokens per search result are a reasonable price for one fewer round-trip.
Copy
```
from fastmcp import FastMCP
from fastmcp.experimental.transforms.code_mode import CodeMode
from fastmcp.experimental.transforms.code_mode import Search, GetSchemas

code_mode = CodeMode(
    discovery_tools=[Search(default_detail="detailed"), GetSchemas()],
)

mcp = FastMCP("Server", transforms=[code_mode])

```

`GetSchemas` is still available as a fallback — the LLM can call it with `detail="full"` if it encounters a tool with complex nested parameters where the compact markdown isn’t enough.
###
[​](https://gofastmcp.com/servers/transforms/code-mode#single-stage)
Single-Stage
Skip discovery entirely and bake tool instructions into the execute tool’s description. Best for **very simple servers** where the LLM already knows what tools are available — maybe there are only a few, or they’re described in the system prompt.
Copy
```
from fastmcp import FastMCP
from fastmcp.experimental.transforms.code_mode import CodeMode

code_mode = CodeMode(
    discovery_tools=[],
    execute_description=(
        "Available tools:\n"
        "- add(x: int, y: int) -> int: Add two numbers\n"
        "- multiply(x: int, y: int) -> int: Multiply two numbers\n\n"
        "Write Python using `await call_tool(name, params)` and `return` the result."
    ),
)

mcp = FastMCP("Server", transforms=[code_mode])

```

##
[​](https://gofastmcp.com/servers/transforms/code-mode#custom-discovery-tools)
Custom Discovery Tools
Discovery tools are composable — you can mix the built-ins with your own. Each discovery tool is a callable that receives catalog access and returns a `Tool`. The catalog accessor is a function (not the catalog itself) because the catalog is request-scoped — different users may see different tools based on auth. Here’s a minimal example:
Copy
```
from fastmcp.experimental.transforms.code_mode import CodeMode
from fastmcp.experimental.transforms.code_mode import GetToolCatalog, GetSchemas
from fastmcp.server.context import Context
from fastmcp.tools.tool import Tool

def list_all_tools(get_catalog: GetToolCatalog) -> Tool:
    async def list_tools(ctx: Context) -> str:
        """List all available tool names."""
        tools = await get_catalog(ctx)
        return ", ".join(t.name for t in tools)

    return Tool.from_function(fn=list_tools, name="list_tools")

code_mode = CodeMode(discovery_tools=[list_all_tools, GetSchemas()])

```

The LLM sees the docstring of each discovery tool’s inner function as its description — that’s how it learns what each tool does and when to use it. Write docstrings that explain what the tool returns and when the LLM should call it. Discovery tools and the execute tool can also have custom names:
Copy
```
from fastmcp.experimental.transforms.code_mode import Search, GetSchemas

code_mode = CodeMode(
    discovery_tools=[
        Search(name="find_tools"),
        GetSchemas(name="describe"),
    ],
    execute_tool_name="run_workflow",
)

mcp = FastMCP("Server", transforms=[code_mode])

```

##
[​](https://gofastmcp.com/servers/transforms/code-mode#sandbox-configuration)
Sandbox Configuration
###
[​](https://gofastmcp.com/servers/transforms/code-mode#resource-limits)
Resource Limits
The default `MontySandboxProvider` can enforce execution limits — timeouts, memory caps, recursion depth, and more. Without limits, LLM-generated scripts can run indefinitely.
Copy
```
from fastmcp.experimental.transforms.code_mode import CodeMode
from fastmcp.experimental.transforms.code_mode import MontySandboxProvider

sandbox = MontySandboxProvider(
    limits={"max_duration_secs": 10, "max_memory": 50_000_000},
)

mcp = FastMCP("Server", transforms=[CodeMode(sandbox_provider=sandbox)])

```

All keys are optional — omit any to leave that dimension uncapped:
Key | Type | Description
---|---|---
`max_duration_secs` | `float` | Maximum wall-clock execution time
`max_memory` | `int` | Memory ceiling in bytes
`max_allocations` | `int` | Cap on total object allocations
`max_recursion_depth` | `int` | Maximum recursion depth
`gc_interval` | `int` | Garbage collection frequency
###
[​](https://gofastmcp.com/servers/transforms/code-mode#custom-sandbox-providers)
Custom Sandbox Providers
You can replace the default sandbox with any object implementing the `SandboxProvider` protocol:
Copy
```
from collections.abc import Callable
from typing import Any

from fastmcp.experimental.transforms.code_mode import CodeMode
from fastmcp.experimental.transforms.code_mode import SandboxProvider

class RemoteSandboxProvider:
    async def run(
        self,
        code: str,
        *,
        inputs: dict[str, Any] | None = None,
        external_functions: dict[str, Callable[..., Any]] | None = None,
    ) -> Any:
        # Send code to your remote sandbox runtime
        ...

mcp = FastMCP(
    "Server",
    transforms=[CodeMode(sandbox_provider=RemoteSandboxProvider())],
)

```

The `external_functions` dict contains async callables injected into the sandbox scope — `execute` uses this to provide `call_tool`.
[ Component Visibility Previous ](https://gofastmcp.com/servers/visibility)[ Tool Search Next ](https://gofastmcp.com/servers/transforms/tool-search)
Ctrl+I
