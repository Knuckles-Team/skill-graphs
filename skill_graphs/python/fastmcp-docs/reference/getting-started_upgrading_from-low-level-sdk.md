[Skip to main content](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Upgrading
Upgrading from the MCP Low-Level SDK
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
    * [From FastMCP 2](https://gofastmcp.com/getting-started/upgrading/from-fastmcp-2)
    * [From MCP SDK](https://gofastmcp.com/getting-started/upgrading/from-mcp-sdk)
    * [From MCP Low-Level SDK](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk)
  * Development
  * What's New


On this page
  * [Install](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#install)
  * [Server and Transport](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#server-and-transport)
  * [Tools](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#tools)
  * [Type Mapping](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#type-mapping)
  * [Return Values](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#return-values)
  * [Resources](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#resources)
  * [Prompts](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#prompts)
  * [Request Context](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#request-context)
  * [Complete Example](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#complete-example)
  * [What’s Next](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#what%E2%80%99s-next)


Upgrading
# Upgrading from the MCP Low-Level SDK
Copy page
Upgrade your MCP server from the low-level Python SDK’s Server class to FastMCP
Copy page
If you’ve been building MCP servers directly on the `mcp` package’s `Server` class — writing `list_tools()` and `call_tool()` handlers, hand-crafting JSON Schema dicts, and wiring up transport boilerplate — this guide is for you. FastMCP replaces all of that machinery with a declarative, Pythonic API where your functions _are_ the protocol surface. The core idea: instead of telling the SDK what your tools look like and then separately implementing them, you write ordinary Python functions and let FastMCP derive the protocol layer from your code. Type hints become JSON Schema. Docstrings become descriptions. Return values are serialized automatically. The plumbing you wrote to satisfy the protocol just disappears.
This guide covers upgrading from **v1** of the `mcp` package. We’ll provide a separate guide when v2 ships.
Already using FastMCP 1.0 via `from mcp.server.fastmcp import FastMCP`? Your upgrade is simpler — see the [FastMCP 1.0 upgrade guide](https://gofastmcp.com/getting-started/upgrading/from-mcp-sdk) instead.
Copy this prompt into any LLM along with your server code to get automated upgrade guidance.
Copy prompt
##
[​](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#install)
Install
Copy
```
pip install --upgrade fastmcp
# or
uv add fastmcp

```

FastMCP includes the `mcp` package as a transitive dependency, so you don’t lose access to anything.
##
[​](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#server-and-transport)
Server and Transport
The `Server` class requires you to choose a transport, connect streams, build initialization options, and run an event loop. FastMCP collapses all of that into a constructor and a `run()` call.
Before
After
Copy
```
import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server

server = Server("my-server")

# ... register handlers ...

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )

asyncio.run(main())

```

Need HTTP instead of stdio? With the `Server` class, you’d wire up Starlette routes and `SseServerTransport` or `StreamableHTTPSessionManager`. With FastMCP:
Copy
```
mcp.run(transport="http", host="0.0.0.0", port=8000)

```

##
[​](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#tools)
Tools
This is where the difference is most dramatic. The `Server` class requires two handlers — one to describe your tools (with hand-written JSON Schema) and another to dispatch calls by name. FastMCP eliminates both by deriving everything from your function signature.
Before
After
Copy
```
import mcp.types as types
from mcp.server import Server

server = Server("math")

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="add",
            description="Add two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"],
            },
        ),
        types.Tool(
            name="multiply",
            description="Multiply two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"},
                },
                "required": ["a", "b"],
            },
        ),
    ]

@server.call_tool()
async def call_tool(
    name: str, arguments: dict
) -> list[types.TextContent]:
    if name == "add":
        result = arguments["a"] + arguments["b"]
        return [types.TextContent(type="text", text=str(result))]
    elif name == "multiply":
        result = arguments["a"] * arguments["b"]
        return [types.TextContent(type="text", text=str(result))]
    raise ValueError(f"Unknown tool: {name}")

```

Each `@mcp.tool` function is self-contained: its name becomes the tool name, its docstring becomes the description, its type annotations become the JSON Schema, and its return value is serialized automatically. No routing. No schema dictionaries. No content-type wrappers.
###
[​](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#type-mapping)
Type Mapping
When converting your `inputSchema` to Python type hints:
JSON Schema | Python Type
---|---
`{"type": "string"}` | `str`
`{"type": "number"}` | `float`
`{"type": "integer"}` | `int`
`{"type": "boolean"}` | `bool`
`{"type": "array", "items": {"type": "string"}}` | `list[str]`
`{"type": "object"}` | `dict`
Optional property (not in `required`) | `param: str | None = None`
###
[​](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#return-values)
Return Values
With the `Server` class, tools return `list[types.TextContent | types.ImageContent | ...]`. In FastMCP, return plain Python values — strings, numbers, dicts, lists, dataclasses, Pydantic models — and serialization is handled for you. For images or other non-text content, FastMCP provides helpers:
Copy
```
from fastmcp import FastMCP
from fastmcp.utilities.types import Image

mcp = FastMCP("media")

@mcp.tool
def create_chart(data: list[float]) -> Image:
    """Generate a chart from data."""
    png_bytes = generate_chart(data)  # your logic
    return Image(data=png_bytes, format="png")

```

##
[​](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#resources)
Resources
The `Server` class uses three handlers for resources: `list_resources()` to enumerate them, `list_resource_templates()` for URI templates, and `read_resource()` to serve content — all with manual routing by URI. FastMCP replaces all three with per-resource decorators.
Before
After
Copy
```
import json
import mcp.types as types
from mcp.server import Server
from pydantic import AnyUrl

server = Server("data")

@server.list_resources()
async def list_resources() -> list[types.Resource]:
    return [
        types.Resource(
            uri=AnyUrl("config://app"),
            name="app_config",
            description="Application configuration",
            mimeType="application/json",
        ),
        types.Resource(
            uri=AnyUrl("config://features"),
            name="feature_flags",
            description="Active feature flags",
            mimeType="application/json",
        ),
    ]

@server.list_resource_templates()
async def list_resource_templates() -> list[types.ResourceTemplate]:
    return [
        types.ResourceTemplate(
            uriTemplate="users://{user_id}/profile",
            name="user_profile",
            description="User profile by ID",
        ),
        types.ResourceTemplate(
            uriTemplate="projects://{project_id}/status",
            name="project_status",
            description="Project status by ID",
        ),
    ]

@server.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    uri_str = str(uri)
    if uri_str == "config://app":
        return json.dumps({"debug": False, "version": "1.0"})
    if uri_str == "config://features":
        return json.dumps({"dark_mode": True, "beta": False})
    if uri_str.startswith("users://"):
        user_id = uri_str.split("/")[2]
        return json.dumps({"id": user_id, "name": f"User {user_id}"})
    if uri_str.startswith("projects://"):
        project_id = uri_str.split("/")[2]
        return json.dumps({"id": project_id, "status": "active"})
    raise ValueError(f"Unknown resource: {uri}")

```

Static resources and URI templates use the same `@mcp.resource` decorator — FastMCP detects `{placeholders}` in the URI and automatically registers a template. The function parameter `user_id` maps directly to the `{user_id}` placeholder.
##
[​](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#prompts)
Prompts
Same pattern: the `Server` class uses `list_prompts()` and `get_prompt()` with manual routing. FastMCP uses one decorator per prompt.
Before
After
Copy
```
import mcp.types as types
from mcp.server import Server

server = Server("prompts")

@server.list_prompts()
async def list_prompts() -> list[types.Prompt]:
    return [
        types.Prompt(
            name="review_code",
            description="Review code for issues",
            arguments=[
                types.PromptArgument(
                    name="code",
                    description="The code to review",
                    required=True,
                ),
                types.PromptArgument(
                    name="language",
                    description="Programming language",
                    required=False,
                ),
            ],
        )
    ]

@server.get_prompt()
async def get_prompt(
    name: str, arguments: dict[str, str] | None
) -> types.GetPromptResult:
    if name == "review_code":
        code = (arguments or {}).get("code", "")
        language = (arguments or {}).get("language", "")
        lang_note = f" (written in {language})" if language else ""
        return types.GetPromptResult(
            description="Code review prompt",
            messages=[
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(
                        type="text",
                        text=f"Please review this code{lang_note}:\n\n{code}",
                    ),
                )
            ],
        )
    raise ValueError(f"Unknown prompt: {name}")

```

Returning a `str` from a prompt function automatically wraps it as a user message. For multi-turn prompts, return a `list[Message]`:
Copy
```
from fastmcp import FastMCP
from fastmcp.prompts import Message

mcp = FastMCP("prompts")

@mcp.prompt
def debug_session(error: str) -> list[Message]:
    """Start a debugging conversation"""
    return [
        Message(f"I'm seeing this error:\n\n{error}"),
        Message("I'll help you debug that. Can you share the relevant code?", role="assistant"),
    ]

```

##
[​](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#request-context)
Request Context
The `Server` class exposes request context through `server.request_context`, which gives you the raw `ServerSession` for sending notifications. FastMCP replaces this with a typed `Context` object injected into any function that declares it.
Before
After
Copy
```
import mcp.types as types
from mcp.server import Server

server = Server("worker")

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "process_data":
        ctx = server.request_context
        await ctx.session.send_log_message(
            level="info", data="Starting processing..."
        )
        # ... do work ...
        await ctx.session.send_log_message(
            level="info", data="Done!"
        )
        return [types.TextContent(type="text", text="Processed")]

```

The `Context` object provides logging (`ctx.debug()`, `ctx.info()`, `ctx.warning()`, `ctx.error()`), progress reporting (`ctx.report_progress()`), resource subscriptions, session state, and more. See [Context](https://gofastmcp.com/servers/context) for the full API.
##
[​](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#complete-example)
Complete Example
A full server upgrade, showing how all the pieces fit together:
Before
After
Copy
```
import asyncio
import json
import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server
from pydantic import AnyUrl

server = Server("demo")

@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="greet",
            description="Greet someone by name",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                },
                "required": ["name"],
            },
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "greet":
        return [types.TextContent(type="text", text=f"Hello, {arguments['name']}!")]
    raise ValueError(f"Unknown tool: {name}")

@server.list_resources()
async def list_resources() -> list[types.Resource]:
    return [
        types.Resource(
            uri=AnyUrl("info://version"),
            name="version",
            description="Server version",
        )
    ]

@server.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    if str(uri) == "info://version":
        return json.dumps({"version": "1.0.0"})
    raise ValueError(f"Unknown resource: {uri}")

@server.list_prompts()
async def list_prompts() -> list[types.Prompt]:
    return [
        types.Prompt(
            name="summarize",
            description="Summarize text",
            arguments=[
                types.PromptArgument(name="text", required=True)
            ],
        )
    ]

@server.get_prompt()
async def get_prompt(
    name: str, arguments: dict[str, str] | None
) -> types.GetPromptResult:
    if name == "summarize":
        return types.GetPromptResult(
            description="Summarize text",
            messages=[
                types.PromptMessage(
                    role="user",
                    content=types.TextContent(
                        type="text",
                        text=f"Summarize:\n\n{(arguments or {}).get('text', '')}",
                    ),
                )
            ],
        )
    raise ValueError(f"Unknown prompt: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream, write_stream,
            server.create_initialization_options(),
        )

asyncio.run(main())

```

##
[​](https://gofastmcp.com/getting-started/upgrading/from-low-level-sdk#what%E2%80%99s-next)
What’s Next
Once you’ve upgraded, you have access to everything FastMCP provides beyond the basics:
  * **[Server composition](https://gofastmcp.com/servers/composition)** — Mount sub-servers to build modular applications
  * **[Middleware](https://gofastmcp.com/servers/middleware)** — Add logging, rate limiting, error handling, and caching
  * **[Proxy servers](https://gofastmcp.com/servers/providers/proxy)** — Create a proxy to any existing MCP server
  * **[OpenAPI integration](https://gofastmcp.com/integrations/openapi)** — Generate an MCP server from an OpenAPI spec
  * **[Authentication](https://gofastmcp.com/servers/auth/authentication)** — Built-in OAuth and token verification
  * **[Testing](https://gofastmcp.com/servers/testing)** — Test your server directly in Python without running a subprocess

Explore the full documentation at [gofastmcp.com](https://gofastmcp.com).
[ Upgrading from the MCP SDK Previous ](https://gofastmcp.com/getting-started/upgrading/from-mcp-sdk)[ Contributing Next ](https://gofastmcp.com/development/contributing)
Ctrl+I
