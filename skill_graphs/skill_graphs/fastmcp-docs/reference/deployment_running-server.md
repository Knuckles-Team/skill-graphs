[Skip to main content](https://gofastmcp.com/deployment/running-server#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
Deployment
Running Your Server
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
    * [Running Your Server](https://gofastmcp.com/deployment/running-server)
    * [HTTP Deployment](https://gofastmcp.com/deployment/http)
    * [Prefect Horizon](https://gofastmcp.com/deployment/prefect-horizon)
    * [Project Configuration](https://gofastmcp.com/deployment/server-configuration)


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
  * [The run() Method](https://gofastmcp.com/deployment/running-server#the-run-method)
  * [Transport Protocols](https://gofastmcp.com/deployment/running-server#transport-protocols)
  * [STDIO Transport (Default)](https://gofastmcp.com/deployment/running-server#stdio-transport-default)
  * [HTTP Transport (Streamable)](https://gofastmcp.com/deployment/running-server#http-transport-streamable)
  * [SSE Transport (Legacy)](https://gofastmcp.com/deployment/running-server#sse-transport-legacy)
  * [Choosing the Right Transport](https://gofastmcp.com/deployment/running-server#choosing-the-right-transport)
  * [The FastMCP CLI](https://gofastmcp.com/deployment/running-server#the-fastmcp-cli)
  * [Dependency Management](https://gofastmcp.com/deployment/running-server#dependency-management)
  * [Passing Arguments to Servers](https://gofastmcp.com/deployment/running-server#passing-arguments-to-servers)
  * [Auto-Reload for Development](https://gofastmcp.com/deployment/running-server#auto-reload-for-development)
  * [Async Usage](https://gofastmcp.com/deployment/running-server#async-usage)
  * [Custom Routes](https://gofastmcp.com/deployment/running-server#custom-routes)
  * [Alternative Initialization Patterns](https://gofastmcp.com/deployment/running-server#alternative-initialization-patterns)
  * [CLI-Only Servers](https://gofastmcp.com/deployment/running-server#cli-only-servers)
  * [ASGI Applications](https://gofastmcp.com/deployment/running-server#asgi-applications)


Deployment
# Running Your Server
Copy page
Learn how to run your FastMCP server locally for development and testing
Copy page
FastMCP servers can be run in different ways depending on your needs. This guide focuses on running servers locally for development and testing. For production deployment to a URL, see the [HTTP Deployment](https://gofastmcp.com/deployment/http) guide.
##
[​](https://gofastmcp.com/deployment/running-server#the-run-method)
The `run()` Method
Every FastMCP server needs to be started to accept connections. The simplest way to run a server is by calling the `run()` method on your FastMCP instance. This method starts the server and blocks until it’s stopped, handling all the connection management for you.
For maximum compatibility, it’s best practice to place the `run()` call within an `if __name__ == "__main__":` block. This ensures the server starts only when the script is executed directly, not when imported as a module.
my_server.py
Copy
```
from fastmcp import FastMCP

mcp = FastMCP(name="MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()

```

You can now run this MCP server by executing `python my_server.py`.
##
[​](https://gofastmcp.com/deployment/running-server#transport-protocols)
Transport Protocols
MCP servers communicate with clients through different transport protocols. Think of transports as the “language” your server speaks to communicate with clients. FastMCP supports three main transport protocols, each designed for specific use cases and deployment scenarios. The choice of transport determines how clients connect to your server, what network capabilities are available, and how many clients can connect simultaneously. Understanding these transports helps you choose the right approach for your application.
###
[​](https://gofastmcp.com/deployment/running-server#stdio-transport-default)
STDIO Transport (Default)
STDIO (Standard Input/Output) is the default transport for FastMCP servers. When you call `run()` without arguments, your server uses STDIO transport. This transport communicates through standard input and output streams, making it perfect for command-line tools and desktop applications like Claude Desktop. With STDIO transport, the client spawns a new server process for each session and manages its lifecycle. The server reads MCP messages from stdin and writes responses to stdout. This is why STDIO servers don’t stay running - they’re started on-demand by the client.
Copy
```
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()  # Uses STDIO transport by default

```

STDIO is ideal for:
  * Local development and testing
  * Claude Desktop integration
  * Command-line tools
  * Single-user applications


###
[​](https://gofastmcp.com/deployment/running-server#http-transport-streamable)
HTTP Transport (Streamable)
HTTP transport turns your MCP server into a web service accessible via a URL. This transport uses the Streamable HTTP protocol, which allows clients to connect over the network. Unlike STDIO where each client gets its own process, an HTTP server can handle multiple clients simultaneously. The Streamable HTTP protocol provides full bidirectional communication between client and server, supporting all MCP operations including streaming responses. This makes it the recommended choice for network-based deployments. To use HTTP transport, specify it in the `run()` method along with networking options:
Copy
```
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Start an HTTP server on port 8000
    mcp.run(transport="http", host="127.0.0.1", port=8000)

```

Your server is now accessible at `http://localhost:8000/mcp`. This URL is the MCP endpoint that clients will connect to. HTTP transport enables:
  * Network accessibility
  * Multiple concurrent clients
  * Integration with web infrastructure
  * Remote deployment capabilities

For production HTTP deployment with authentication and advanced configuration, see the [HTTP Deployment](https://gofastmcp.com/deployment/http) guide.
###
[​](https://gofastmcp.com/deployment/running-server#sse-transport-legacy)
SSE Transport (Legacy)
Server-Sent Events (SSE) transport was the original HTTP-based transport for MCP. While still supported for backward compatibility, it has limitations compared to the newer Streamable HTTP transport. SSE only supports server-to-client streaming, making it less efficient for bidirectional communication.
Copy
```
if __name__ == "__main__":
    # SSE transport - use HTTP instead for new projects
    mcp.run(transport="sse", host="127.0.0.1", port=8000)

```

We recommend using HTTP transport instead of SSE for all new projects. SSE remains available only for compatibility with older clients that haven’t upgraded to Streamable HTTP.
###
[​](https://gofastmcp.com/deployment/running-server#choosing-the-right-transport)
Choosing the Right Transport
Each transport serves different needs. STDIO is perfect when you need simple, local execution - it’s what Claude Desktop and most command-line tools expect. HTTP transport is essential when you need network access, want to serve multiple clients, or plan to deploy your server remotely. SSE exists only for backward compatibility and shouldn’t be used in new projects. Consider your deployment scenario: Are you building a tool for local use? STDIO is your best choice. Need a centralized service that multiple clients can access? HTTP transport is the way to go.
##
[​](https://gofastmcp.com/deployment/running-server#the-fastmcp-cli)
The FastMCP CLI
FastMCP provides a powerful command-line interface for running servers without modifying the source code. The CLI can automatically find and run your server with different transports, manage dependencies, and handle development workflows:
Copy
```
fastmcp run server.py

```

The CLI automatically finds a FastMCP instance in your file (named `mcp`, `server`, or `app`) and runs it with the specified options. This is particularly useful for testing different transports or configurations without changing your code.
###
[​](https://gofastmcp.com/deployment/running-server#dependency-management)
Dependency Management
The CLI integrates with `uv` to manage Python environments and dependencies:
Copy
```
# Run with a specific Python version
fastmcp run server.py --python 3.11

# Run with additional packages
fastmcp run server.py --with pandas --with numpy

# Run with dependencies from a requirements file
fastmcp run server.py --with-requirements requirements.txt

# Combine multiple options
fastmcp run server.py --python 3.10 --with httpx --transport http

# Run within a specific project directory
fastmcp run server.py --project /path/to/project

```

When using `--python`, `--with`, `--project`, or `--with-requirements`, the server runs via `uv run` subprocess instead of using your local environment.
###
[​](https://gofastmcp.com/deployment/running-server#passing-arguments-to-servers)
Passing Arguments to Servers
When servers accept command line arguments (using argparse, click, or other libraries), you can pass them after `--`:
Copy
```
fastmcp run config_server.py -- --config config.json
fastmcp run database_server.py -- --database-path /tmp/db.sqlite --debug

```

This is useful for servers that need configuration files, database paths, API keys, or other runtime options. For more CLI features including development mode with the MCP Inspector, see the [CLI documentation](https://gofastmcp.com/cli/running).
###
[​](https://gofastmcp.com/deployment/running-server#auto-reload-for-development)
Auto-Reload for Development
`3.0.0` During development, you can use the `--reload` flag to automatically restart your server when source files change:
Copy
```
fastmcp run server.py --reload

```

The server watches for changes to Python files in the current directory and restarts automatically when you save changes. This provides a fast feedback loop during development without manually stopping and starting the server.
Copy
```
# Watch specific directories for changes
fastmcp run server.py --reload --reload-dir ./src --reload-dir ./lib

# Combine with other options
fastmcp run server.py --reload --transport http --port 8080

```

Auto-reload uses stateless mode to enable seamless restarts. For stdio transport, this is fully featured. For HTTP transport, some bidirectional features like elicitation are not available during reload mode.
SSE transport does not support auto-reload due to session limitations. Use HTTP transport instead if you need both network access and auto-reload.
###
[​](https://gofastmcp.com/deployment/running-server#async-usage)
Async Usage
FastMCP servers are built on async Python, but the framework provides both synchronous and asynchronous APIs to fit your application’s needs. The `run()` method we’ve been using is actually a synchronous wrapper around the async server implementation. For applications that are already running in an async context, FastMCP provides the `run_async()` method:
Copy
```
from fastmcp import FastMCP
import asyncio

mcp = FastMCP(name="MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

async def main():
    # Use run_async() in async contexts
    await mcp.run_async(transport="http", port=8000)

if __name__ == "__main__":
    asyncio.run(main())

```

The `run()` method cannot be called from inside an async function because it creates its own async event loop internally. If you attempt to call `run()` from inside an async function, you’ll get an error about the event loop already running.Always use `run_async()` inside async functions and `run()` in synchronous contexts.
Both `run()` and `run_async()` accept the same transport arguments, so all the examples above apply to both methods.
##
[​](https://gofastmcp.com/deployment/running-server#custom-routes)
Custom Routes
When using HTTP transport, you might want to add custom web endpoints alongside your MCP server. This is useful for health checks, status pages, or simple APIs. FastMCP lets you add custom routes using the `@custom_route` decorator:
Copy
```
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("MyServer")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

@mcp.tool
def process(data: str) -> str:
    return f"Processed: {data}"

if __name__ == "__main__":
    mcp.run(transport="http")  # Health check at http://localhost:8000/health

```

Custom routes are served by the same web server as your MCP endpoint. They’re available at the root of your domain while the MCP endpoint is at `/mcp/`. For more complex web applications, consider [mounting your MCP server into a FastAPI or Starlette app](https://gofastmcp.com/deployment/http#integration-with-web-frameworks).
##
[​](https://gofastmcp.com/deployment/running-server#alternative-initialization-patterns)
Alternative Initialization Patterns
The `if __name__ == "__main__"` pattern works well for standalone scripts, but some deployment scenarios require different approaches. FastMCP handles these cases automatically.
###
[​](https://gofastmcp.com/deployment/running-server#cli-only-servers)
CLI-Only Servers
When using the FastMCP CLI, you don’t need the `if __name__` block at all. The CLI will find your FastMCP instance and run it:
Copy
```
# server.py
from fastmcp import FastMCP

mcp = FastMCP("MyServer")  # CLI looks for 'mcp', 'server', or 'app'

@mcp.tool
def process(data: str) -> str:
    return f"Processed: {data}"

# No if __name__ block needed - CLI will find and run 'mcp'

```

###
[​](https://gofastmcp.com/deployment/running-server#asgi-applications)
ASGI Applications
For ASGI deployment (running with Uvicorn or similar), you’ll want to create an ASGI application object. This approach is common in production deployments where you need more control over the server configuration:
Copy
```
# app.py
from fastmcp import FastMCP

def create_app():
    mcp = FastMCP("MyServer")

    @mcp.tool
    def process(data: str) -> str:
        return f"Processed: {data}"

    return mcp.http_app()

app = create_app()  # Uvicorn will use this

```

See the [HTTP Deployment](https://gofastmcp.com/deployment/http) guide for more ASGI deployment patterns.
[ Authorization Previous ](https://gofastmcp.com/servers/authorization)[ HTTP Deployment Next ](https://gofastmcp.com/deployment/http)
Ctrl+I
