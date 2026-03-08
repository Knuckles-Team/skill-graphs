[Skip to main content](https://gofastmcp.com/v2/getting-started/welcome#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v2.14.5
Search...
Navigation
Get Started
Welcome to FastMCP 2.0!
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
  * [Beyond Basic MCP](https://gofastmcp.com/v2/getting-started/welcome#beyond-basic-mcp)
  * [What is MCP?](https://gofastmcp.com/v2/getting-started/welcome#what-is-mcp)
  * [Why FastMCP?](https://gofastmcp.com/v2/getting-started/welcome#why-fastmcp)
  * [LLM-Friendly Docs](https://gofastmcp.com/v2/getting-started/welcome#llm-friendly-docs)
  * [MCP Server](https://gofastmcp.com/v2/getting-started/welcome#mcp-server)
  * [Text Formats](https://gofastmcp.com/v2/getting-started/welcome#text-formats)


Get Started
# Welcome to FastMCP 2.0!
Copy page
The fast, Pythonic way to build MCP servers and clients.
Copy page
!['F' logo on a watercolor background](https://mintcdn.com/fastmcp/xdeorzy2A8w9kCCa/assets/brand/f-watercolor-waves.png?fit=max&auto=format&n=xdeorzy2A8w9kCCa&q=85&s=77138c04347ed9726fc34a7ef5e4f21d) !['F' logo on a watercolor background](https://mintcdn.com/fastmcp/xdeorzy2A8w9kCCa/assets/brand/f-watercolor-waves-dark.png?fit=max&auto=format&n=xdeorzy2A8w9kCCa&q=85&s=7bc98874cb9bd5ef7eefea5555e8280d) **FastMCP is the standard framework for building MCP applications.** The
Copy
```
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()

```

##
[​](https://gofastmcp.com/v2/getting-started/welcome#beyond-basic-mcp)
Beyond Basic MCP
FastMCP pioneered Python MCP development, and FastMCP 1.0 was incorporated into the  **This is FastMCP 2.0,** the actively maintained version that extends far beyond basic protocol implementation. While the SDK provides core functionality, FastMCP 2.0 delivers everything needed for production: advanced MCP patterns (server composition, proxying, OpenAPI/FastAPI generation, tool transformation), enterprise auth (Google, GitHub, Azure, Auth0, WorkOS, and more), deployment tools, testing frameworks, and comprehensive client libraries. Ready to build? Start with our [installation guide](https://gofastmcp.com/v2/getting-started/installation) or jump straight to the [quickstart](https://gofastmcp.com/v2/getting-started/quickstart). FastMCP is made with 💙 by
**FastMCP 3.0** is in development and may include breaking changes. To avoid unexpected issues, pin your dependency to v2: `fastmcp<3`
##
[​](https://gofastmcp.com/v2/getting-started/welcome#what-is-mcp)
What is MCP?
The Model Context Protocol lets you build servers that expose data and functionality to LLM applications in a secure, standardized way. It is often described as “the USB-C port for AI”, providing a uniform way to connect LLMs to resources they can use. It may be easier to think of it as an API, but specifically designed for LLM interactions. MCP servers can:
  * Expose data through `Resources` (think of these sort of like GET endpoints; they are used to load information into the LLM’s context)
  * Provide functionality through `Tools` (sort of like POST endpoints; they are used to execute code or otherwise produce a side effect)
  * Define interaction patterns through `Prompts` (reusable templates for LLM interactions)
  * And more!

FastMCP provides a high-level, Pythonic interface for building, managing, and interacting with these servers.
##
[​](https://gofastmcp.com/v2/getting-started/welcome#why-fastmcp)
Why FastMCP?
FastMCP handles all the complex protocol details so you can focus on building. In most cases, decorating a Python function is all you need — FastMCP handles the rest. 🚀 **Fast** : High-level interface means less code and faster development 🍀 **Simple** : Build MCP servers with minimal boilerplate 🐍 **Pythonic** : Feels natural to Python developers 🔍 **Complete** : Everything for production — enterprise auth (Google, GitHub, Azure, Auth0, WorkOS), deployment tools, testing frameworks, client libraries, and more FastMCP provides the shortest path from idea to production. Deploy locally, to the cloud with
**This documentation reflects FastMCP’s`main` branch**, meaning it always reflects the latest development version. Features are generally marked with version badges (e.g. `New in version: 2.13.1`) to indicate when they were introduced. Note that this may include features that are not yet released.
##
[​](https://gofastmcp.com/v2/getting-started/welcome#llm-friendly-docs)
LLM-Friendly Docs
The FastMCP documentation is available in multiple LLM-friendly formats:
###
[​](https://gofastmcp.com/v2/getting-started/welcome#mcp-server)
MCP Server
The FastMCP docs are accessible via MCP! The server URL is `https://gofastmcp.com/mcp`. In fact, you can use FastMCP to search the FastMCP docs:
Copy
```
import asyncio
from fastmcp import Client

async def main():
    async with Client("https://gofastmcp.com/mcp") as client:
        result = await client.call_tool(
            name="SearchFastMcp",
            arguments={"query": "deploy a FastMCP server"}
        )
    print(result)

asyncio.run(main())

```

###
[​](https://gofastmcp.com/v2/getting-started/welcome#text-formats)
Text Formats
The docs are also available in
  * [llms.txt](https://gofastmcp.com/llms.txt) - A sitemap listing all documentation pages
  * [llms-full.txt](https://gofastmcp.com/llms-full.txt) - The entire documentation in one file (may exceed context windows)

Any page can be accessed as markdown by appending `.md` to the URL. For example, this page becomes `https://gofastmcp.com/getting-started/welcome.md`. You can also copy any page as markdown by pressing “Cmd+C” (or “Ctrl+C” on Windows) on your keyboard.
[ Installation Next ](https://gofastmcp.com/v2/getting-started/installation)
Ctrl+I
