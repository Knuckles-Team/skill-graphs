[Skip to main content](https://gofastmcp.com/cli/overview#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
CLI
CLI
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
  * Development
  * What's New


On this page
  * [Commands at a Glance](https://gofastmcp.com/cli/overview#commands-at-a-glance)
  * [Server Targets](https://gofastmcp.com/cli/overview#server-targets)
  * [Name-Based Resolution](https://gofastmcp.com/cli/overview#name-based-resolution)
  * [Authentication](https://gofastmcp.com/cli/overview#authentication)
  * [Transport Override](https://gofastmcp.com/cli/overview#transport-override)


CLI
# CLI
Copy page
The fastmcp command-line interface
Copy page
The `fastmcp` CLI is installed automatically with FastMCP. It’s the primary way to run, test, install, and interact with MCP servers from your terminal.
Copy
```
fastmcp --help

```

##
[​](https://gofastmcp.com/cli/overview#commands-at-a-glance)
Commands at a Glance
Command | What it does
---|---
[`run`](https://gofastmcp.com/cli/running) | Run a server (local file, factory function, remote URL, or config file)
[`dev inspector`](https://gofastmcp.com/cli/running#development-with-the-inspector) | Launch a server inside the MCP Inspector for interactive testing
[`install`](https://gofastmcp.com/cli/install-mcp) | Install a server into Claude Code, Claude Desktop, Cursor, Gemini CLI, or Goose
[`inspect`](https://gofastmcp.com/cli/inspecting) | Print a server’s tools, resources, and prompts as a summary or JSON report
[`list`](https://gofastmcp.com/cli/client) | List a server’s tools (and optionally resources and prompts)
[`call`](https://gofastmcp.com/cli/client#calling-tools) | Call a single tool with arguments
[`discover`](https://gofastmcp.com/cli/client#discovering-configured-servers) | Find MCP servers configured in your editors and tools
[`generate-cli`](https://gofastmcp.com/cli/generate-cli) | Scaffold a standalone typed CLI from a server’s tool schemas
[`project prepare`](https://gofastmcp.com/cli/running#pre-building-environments) | Pre-install dependencies into a reusable uv project
[`auth cimd`](https://gofastmcp.com/cli/auth) | Create and validate CIMD documents for OAuth
`version` | Print version info (`--copy` to copy to clipboard)
##
[​](https://gofastmcp.com/cli/overview#server-targets)
Server Targets
Most commands need to know _which server_ to talk to. You pass a “server spec” as the first argument, and FastMCP resolves the right transport automatically. **URLs** connect to a running HTTP server:
Copy
```
fastmcp list http://localhost:8000/mcp
fastmcp call http://localhost:8000/mcp get_forecast city=London

```

**Python files** are loaded directly — no `mcp.run()` boilerplate needed. FastMCP finds a server instance named `mcp`, `server`, or `app` in the file, or you can specify one explicitly:
Copy
```
fastmcp list server.py
fastmcp run server.py:my_custom_server

```

**Config files** work too — both FastMCP’s own `fastmcp.json` format and standard MCP config files with an `mcpServers` key:
Copy
```
fastmcp run fastmcp.json
fastmcp list mcp-config.json

```

**Stdio commands** connect to any MCP server that speaks over standard I/O. Use `--command` instead of a positional argument:
Copy
```
fastmcp list --command 'npx -y @modelcontextprotocol/server-github'

```

###
[​](https://gofastmcp.com/cli/overview#name-based-resolution)
Name-Based Resolution
If your servers are already configured in an editor or tool, you can refer to them by name. FastMCP scans configs from Claude Desktop, Claude Code, Cursor, Gemini CLI, and Goose:
Copy
```
fastmcp list weather
fastmcp call weather get_forecast city=London

```

When the same name appears in multiple configs, use the `source:name` form to be specific:
Copy
```
fastmcp list claude-code:my-server
fastmcp call cursor:weather get_forecast city=London

```

Run [`fastmcp discover`](https://gofastmcp.com/cli/client#discovering-configured-servers) to see what’s available on your machine.
##
[​](https://gofastmcp.com/cli/overview#authentication)
Authentication
When targeting an HTTP URL, the CLI enables OAuth authentication by default. If the server requires it, you’ll be guided through the flow (typically opening a browser). If it doesn’t, the setup is a silent no-op. To skip authentication entirely — useful for local development servers — pass `--auth none`:
Copy
```
fastmcp call http://localhost:8000/mcp my_tool --auth none

```

You can also pass a bearer token directly:
Copy
```
fastmcp list http://localhost:8000/mcp --auth "Bearer sk-..."

```

##
[​](https://gofastmcp.com/cli/overview#transport-override)
Transport Override
FastMCP defaults to Streamable HTTP for URL targets. If the server only supports Server-Sent Events (SSE), force the older transport:
Copy
```
fastmcp list http://localhost:8000 --transport sse

```

[ MCP JSON Configuration 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/mcp-json-configuration)[ Running Servers Next ](https://gofastmcp.com/cli/running)
Ctrl+I
