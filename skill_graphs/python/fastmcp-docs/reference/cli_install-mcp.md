[Skip to main content](https://gofastmcp.com/cli/install-mcp#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
CLI
Install MCP Servers
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
  * [Supported Clients](https://gofastmcp.com/cli/install-mcp#supported-clients)
  * [Declaring Dependencies](https://gofastmcp.com/cli/install-mcp#declaring-dependencies)
  * [Options](https://gofastmcp.com/cli/install-mcp#options)
  * [Examples](https://gofastmcp.com/cli/install-mcp#examples)
  * [Generating MCP JSON](https://gofastmcp.com/cli/install-mcp#generating-mcp-json)
  * [Generating Stdio Commands](https://gofastmcp.com/cli/install-mcp#generating-stdio-commands)


CLI
# Install MCP Servers
Copy page
Install MCP servers into Claude, Cursor, Gemini, and other clients
Copy page
`2.10.3` `fastmcp install` registers a server with an MCP client application so the client can launch it automatically. Each MCP client runs servers in its own isolated environment, which means dependencies need to be explicitly declared — you can’t rely on whatever happens to be installed locally.
Copy
```
fastmcp install claude-desktop server.py
fastmcp install claude-code server.py --with pandas --with matplotlib
fastmcp install cursor server.py -e .

```

`uv` must be installed and available in your system PATH. Both Claude Desktop and Cursor run servers in isolated environments managed by `uv`. On macOS, install it globally with Homebrew for Claude Desktop compatibility: `brew install uv`.
##
[​](https://gofastmcp.com/cli/install-mcp#supported-clients)
Supported Clients
Client | Install method
---|---
`claude-code` | Claude Code’s built-in MCP management
`claude-desktop` | Direct config file modification
`cursor` | Deeplink that opens Cursor for confirmation
`gemini-cli` | Gemini CLI’s built-in MCP management
`goose` | Deeplink that opens Goose for confirmation (uses `uvx`)
`mcp-json` | Generates standard MCP JSON config for manual use
`stdio` | Outputs the shell command to run via stdio
##
[​](https://gofastmcp.com/cli/install-mcp#declaring-dependencies)
Declaring Dependencies
Because MCP clients run servers in isolation, you need to tell the install command what your server needs. There are two approaches: **Command-line flags** let you specify dependencies directly:
Copy
```
fastmcp install claude-desktop server.py --with pandas --with "sqlalchemy>=2.0"
fastmcp install cursor server.py -e . --with-requirements requirements.txt

```

**`fastmcp.json`**configuration files declare dependencies alongside the server definition. When you install from a config file, dependencies are picked up automatically:
Copy
```
fastmcp install claude-desktop fastmcp.json
fastmcp install claude-desktop  # auto-detects fastmcp.json in current directory

```

See [Server Configuration](https://gofastmcp.com/deployment/server-configuration) for the full config format.
##
[​](https://gofastmcp.com/cli/install-mcp#options)
Options
Option | Flag | Description
---|---|---
Server Name |  `--server-name`, `-n` | Custom name for the server
Editable Package |  `--with-editable`, `-e` | Install a directory in editable mode
Extra Packages | `--with` | Additional packages (repeatable)
Environment Variables | `--env` |  `KEY=VALUE` pairs (repeatable)
Environment File |  `--env-file`, `-f` | Load env vars from a `.env` file
Python | `--python` | Python version (e.g., `3.11`)
Project | `--project` | Run within a uv project directory
Requirements | `--with-requirements` | Install from a requirements file
##
[​](https://gofastmcp.com/cli/install-mcp#examples)
Examples
Copy
```
# Basic install with auto-detected server instance
fastmcp install claude-desktop server.py

# Install from fastmcp.json with auto-detection
fastmcp install claude-desktop

# Explicit entrypoint with dependencies
fastmcp install claude-desktop server.py:my_server \
  --server-name "My Analysis Server" \
  --with pandas

# With environment variables
fastmcp install claude-code server.py \
  --env API_KEY=secret \
  --env DEBUG=true

# With env file
fastmcp install cursor server.py --env-file .env

# Specific Python version and requirements file
fastmcp install claude-desktop server.py \
  --python 3.11 \
  --with-requirements requirements.txt

```

##
[​](https://gofastmcp.com/cli/install-mcp#generating-mcp-json)
Generating MCP JSON
The `mcp-json` target generates standard MCP configuration JSON instead of installing into a specific client. This is useful for clients that FastMCP doesn’t directly support, for CI/CD environments, or for sharing server configs:
Copy
```
fastmcp install mcp-json server.py

```

The output follows the standard format used by Claude Desktop, Cursor, and other MCP clients:
Copy
```
{
  "server-name": {
    "command": "uv",
    "args": ["run", "--with", "fastmcp", "fastmcp", "run", "/path/to/server.py"],
    "env": {
      "API_KEY": "value"
    }
  }
}

```

Use `--copy` to send it to your clipboard instead of stdout.
##
[​](https://gofastmcp.com/cli/install-mcp#generating-stdio-commands)
Generating Stdio Commands
The `stdio` target outputs the shell command an MCP host would use to start your server over stdio:
Copy
```
fastmcp install stdio server.py
# Output: uv run --with fastmcp fastmcp run /absolute/path/to/server.py

```

When installing from a `fastmcp.json`, dependencies from the config are included automatically:
Copy
```
fastmcp install stdio fastmcp.json
# Output: uv run --with fastmcp --with pillow --with 'qrcode[pil]>=8.0' fastmcp run /path/to/server.py

```

Use `--copy` to copy to clipboard.
`fastmcp install` is designed for local server files with stdio transport. For remote servers running over HTTP, use your client’s native configuration — FastMCP’s value here is simplifying the complex local setup with `uv`, dependencies, and environment variables.
[ Running Servers Previous ](https://gofastmcp.com/cli/running)[ Inspecting Servers Next ](https://gofastmcp.com/cli/inspecting)
Ctrl+I
