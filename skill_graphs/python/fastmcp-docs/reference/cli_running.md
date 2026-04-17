[Skip to main content](https://gofastmcp.com/cli/running#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
CLI
Running Servers
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
  * [Starting a Server](https://gofastmcp.com/cli/running#starting-a-server)
  * [Entrypoints](https://gofastmcp.com/cli/running#entrypoints)
  * [Options](https://gofastmcp.com/cli/running#options)
  * [Dependency Management](https://gofastmcp.com/cli/running#dependency-management)
  * [Development with the Inspector](https://gofastmcp.com/cli/running#development-with-the-inspector)
  * [Pre-Building Environments](https://gofastmcp.com/cli/running#pre-building-environments)


CLI
# Running Servers
Copy page
Start, develop, and configure servers from the command line
Copy page
##
[​](https://gofastmcp.com/cli/running#starting-a-server)
Starting a Server
`fastmcp run` starts a server. Point it at a Python file, a factory function, a remote URL, or a config file:
Copy
```
fastmcp run server.py
fastmcp run server.py:create_server
fastmcp run https://example.com/mcp
fastmcp run fastmcp.json

```

By default, the server runs over **stdio** — the transport that MCP clients like Claude Desktop expect. To serve over HTTP instead, specify the transport:
Copy
```
fastmcp run server.py --transport http
fastmcp run server.py --transport http --host 0.0.0.0 --port 9000

```

###
[​](https://gofastmcp.com/cli/running#entrypoints)
Entrypoints
FastMCP supports several ways to locate and start your server: **Inferred instance** — FastMCP imports the file and looks for a variable named `mcp`, `server`, or `app`:
Copy
```
fastmcp run server.py

```

**Explicit instance** — point at a specific variable:
Copy
```
fastmcp run server.py:my_server

```

**Factory function** — FastMCP calls the function and uses the returned server. Useful when your server needs async setup or configuration that runs before startup:
Copy
```
fastmcp run server.py:create_server

```

**Remote URL** — starts a local proxy that bridges to a remote server. Handy for local development against a deployed server, or for bridging a remote HTTP server to stdio:
Copy
```
fastmcp run https://example.com/mcp

```

**FastMCP config** — uses a `fastmcp.json` file that declaratively specifies the server, its dependencies, and deployment settings. When you run `fastmcp run` with no arguments, it auto-detects `fastmcp.json` in the current directory:
Copy
```
fastmcp run
fastmcp run my-config.fastmcp.json

```

See [Server Configuration](https://gofastmcp.com/deployment/server-configuration) for the full `fastmcp.json` format. **MCP config** — runs servers defined in a standard MCP configuration file (any `.json` with an `mcpServers` key):
Copy
```
fastmcp run mcp.json

```

`fastmcp run` completely ignores the `if __name__ == "__main__"` block. Any setup code in that block won’t execute. If you need initialization logic to run, use a [factory function](https://gofastmcp.com/cli/overview#factory-functions).
###
[​](https://gofastmcp.com/cli/running#options)
Options
Option | Flag | Description
---|---|---
Transport |  `--transport`, `-t` |  `stdio` (default), `http`, or `sse`
Host | `--host` | Bind address for HTTP (default: `127.0.0.1`)
Port |  `--port`, `-p` | Bind port for HTTP (default: `8000`)
Path | `--path` | URL path for HTTP (default: `/mcp/`)
Log Level |  `--log-level`, `-l` |  `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
No Banner | `--no-banner` | Suppress the startup banner
Auto-Reload |  `--reload` / `--no-reload` | Watch for file changes and restart automatically
Reload Dirs | `--reload-dir` | Directories to watch (repeatable)
Skip Env | `--skip-env` | Don’t set up a uv environment (use when already in one)
Python | `--python` | Python version to use (e.g., `3.11`)
Extra Packages | `--with` | Additional packages to install (repeatable)
Project | `--project` | Run within a specific uv project directory
Requirements | `--with-requirements` | Install from a requirements file
###
[​](https://gofastmcp.com/cli/running#dependency-management)
Dependency Management
By default, `fastmcp run` uses your current Python environment directly. When you pass `--python`, `--with`, `--project`, or `--with-requirements`, it switches to running via `uv run` in a subprocess, which handles dependency isolation automatically. The `--skip-env` flag is useful when you’re already inside an activated venv, a Docker container with pre-installed dependencies, or a uv-managed project — it prevents uv from trying to set up another environment layer.
##
[​](https://gofastmcp.com/cli/running#development-with-the-inspector)
Development with the Inspector
`fastmcp dev inspector` launches your server inside the
Copy
```
fastmcp dev inspector server.py
fastmcp dev inspector server.py -e . --with pandas

```

The Inspector always runs your server via `uv run` in a subprocess — it never uses your local environment directly. Specify dependencies with `--with`, `--with-editable`, `--with-requirements`, or through a `fastmcp.json` file.
The Inspector connects over **stdio only**. When it launches, you may need to select “STDIO” from the transport dropdown and click connect. To test a server over HTTP, start it separately with `fastmcp run server.py --transport http` and point the Inspector at the URL.
Option | Flag | Description
---|---|---
Editable Package |  `--with-editable`, `-e` | Install a directory in editable mode
Extra Packages | `--with` | Additional packages (repeatable)
Inspector Version | `--inspector-version` | MCP Inspector version to use
UI Port | `--ui-port` | Port for the Inspector UI
Server Port | `--server-port` | Port for the Inspector proxy
Auto-Reload |  `--reload` / `--no-reload` | File watching (default: on)
Reload Dirs | `--reload-dir` | Directories to watch (repeatable)
Python | `--python` | Python version
Project | `--project` | Run within a uv project directory
Requirements | `--with-requirements` | Install from a requirements file
##
[​](https://gofastmcp.com/cli/running#pre-building-environments)
Pre-Building Environments
`fastmcp project prepare` creates a persistent uv project from a `fastmcp.json` file, pre-installing all dependencies. This separates environment setup from server execution — install once, run many times.
Copy
```
# Step 1: Build the environment (slow, does dependency resolution)
fastmcp project prepare fastmcp.json --output-dir ./env

# Step 2: Run using the prepared environment (fast, no install step)
fastmcp run fastmcp.json --project ./env

```

The prepared directory contains a `pyproject.toml`, a `.venv` with all packages installed, and a `uv.lock` for reproducibility. This is particularly useful in deployment scenarios where you want deterministic, pre-built environments.
[ CLI Previous ](https://gofastmcp.com/cli/overview)[ Install MCP Servers Next ](https://gofastmcp.com/cli/install-mcp)
Ctrl+I
