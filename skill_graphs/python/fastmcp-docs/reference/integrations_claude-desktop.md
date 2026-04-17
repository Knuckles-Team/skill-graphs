[Skip to main content](https://gofastmcp.com/integrations/claude-desktop#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
AI Assistants
Claude Desktop 🤝 FastMCP
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
    * [ChatGPT](https://gofastmcp.com/integrations/chatgpt)
    * [Claude Code](https://gofastmcp.com/integrations/claude-code)
    * [Claude Desktop](https://gofastmcp.com/integrations/claude-desktop)
    * [Cursor](https://gofastmcp.com/integrations/cursor)
    * [Gemini CLI](https://gofastmcp.com/integrations/gemini-cli)
    * [Goose](https://gofastmcp.com/integrations/goose)
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
  * [Requirements](https://gofastmcp.com/integrations/claude-desktop#requirements)
  * [Create a Server](https://gofastmcp.com/integrations/claude-desktop#create-a-server)
  * [Install the Server](https://gofastmcp.com/integrations/claude-desktop#install-the-server)
  * [FastMCP CLI](https://gofastmcp.com/integrations/claude-desktop#fastmcp-cli)
  * [Dependencies](https://gofastmcp.com/integrations/claude-desktop#dependencies)
  * [Python Version and Project Directory](https://gofastmcp.com/integrations/claude-desktop#python-version-and-project-directory)
  * [Environment Variables](https://gofastmcp.com/integrations/claude-desktop#environment-variables)
  * [Manual Configuration](https://gofastmcp.com/integrations/claude-desktop#manual-configuration)
  * [Dependencies](https://gofastmcp.com/integrations/claude-desktop#dependencies-2)
  * [Environment Variables](https://gofastmcp.com/integrations/claude-desktop#environment-variables-2)
  * [Remote Servers](https://gofastmcp.com/integrations/claude-desktop#remote-servers)
  * [Authentication](https://gofastmcp.com/integrations/claude-desktop#authentication)


AI Assistants
# Claude Desktop 🤝 FastMCP
Copy page
Connect FastMCP servers to Claude Desktop
Copy page
**This integration focuses on running local FastMCP server files with STDIO transport.** For remote servers running with HTTP or SSE transport, use your client's native configuration - FastMCP's integrations focus on simplifying the complex local setup with dependencies and `uv` commands.
Remote MCP server support is currently in beta and available for users on Claude Pro, Max, Team, and Enterprise plans (as of June 2025). Most users will still need to use local STDIO connections.
This guide focuses specifically on using FastMCP servers with Claude Desktop. For general Claude Desktop MCP setup and official examples, see the
##
[​](https://gofastmcp.com/integrations/claude-desktop#requirements)
Requirements
Claude Desktop traditionally requires MCP servers to run locally using STDIO transport, where your server communicates with Claude through standard input/output rather than HTTP. However, users on certain plans now have access to remote server support as well.
If you don’t have access to remote server support or need to connect to remote servers, you can create a **proxy server** that runs locally via STDIO and forwards requests to remote HTTP servers. See the [Proxy Servers](https://gofastmcp.com/integrations/claude-desktop#proxy-servers) section below.
##
[​](https://gofastmcp.com/integrations/claude-desktop#create-a-server)
Create a Server
The examples in this guide will use the following simple dice-rolling server, saved as `server.py`.
server.py
Copy
```
import random
from fastmcp import FastMCP

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    mcp.run()

```

##
[​](https://gofastmcp.com/integrations/claude-desktop#install-the-server)
Install the Server
###
[​](https://gofastmcp.com/integrations/claude-desktop#fastmcp-cli)
FastMCP CLI
`2.10.3` The easiest way to install a FastMCP server in Claude Desktop is using the `fastmcp install claude-desktop` command. This automatically handles the configuration and dependency management.
Prior to version 2.10.3, Claude Desktop could be managed by running `fastmcp install <path>` without specifying the client.
Copy
```
fastmcp install claude-desktop server.py

```

The install command supports the same `file.py:object` notation as the `run` command. If no object is specified, it will automatically look for a FastMCP server object named `mcp`, `server`, or `app` in your file:
Copy
```
# These are equivalent if your server object is named 'mcp'
fastmcp install claude-desktop server.py
fastmcp install claude-desktop server.py:mcp

# Use explicit object name if your server has a different name
fastmcp install claude-desktop server.py:my_custom_server

```

After installation, restart Claude Desktop completely. You should see a hammer icon (🔨) in the bottom left of the input box, indicating that MCP tools are available.
####
[​](https://gofastmcp.com/integrations/claude-desktop#dependencies)
Dependencies
FastMCP provides several ways to manage your server’s dependencies when installing in Claude Desktop: **Individual packages** : Use the `--with` flag to specify packages your server needs. You can use this flag multiple times:
Copy
```
fastmcp install claude-desktop server.py --with pandas --with requests

```

**Requirements file** : If you have a `requirements.txt` file listing all your dependencies, use `--with-requirements` to install them all at once:
Copy
```
fastmcp install claude-desktop server.py --with-requirements requirements.txt

```

**Editable packages** : For local packages in development, use `--with-editable` to install them in editable mode:
Copy
```
fastmcp install claude-desktop server.py --with-editable ./my-local-package

```

Alternatively, you can use a `fastmcp.json` configuration file (recommended):
fastmcp.json
Copy
```
{
  "$schema": "https://gofastmcp.com/public/schemas/fastmcp.json/v1.json",
  "source": {
    "path": "server.py",
    "entrypoint": "mcp"
  },
  "environment": {
    "dependencies": ["pandas", "requests"]
  }
}

```

####
[​](https://gofastmcp.com/integrations/claude-desktop#python-version-and-project-directory)
Python Version and Project Directory
FastMCP allows you to control the Python environment for your server: **Python version** : Use `--python` to specify which Python version your server should run with. This is particularly useful when your server requires a specific Python version:
Copy
```
fastmcp install claude-desktop server.py --python 3.11

```

**Project directory** : Use `--project` to run your server within a specific project directory. This ensures that `uv` will discover all `pyproject.toml`, `uv.toml`, and `.python-version` files from that project:
Copy
```
fastmcp install claude-desktop server.py --project /path/to/my-project

```

When you specify a project directory, all relative paths in your server will be resolved from that directory, and the project’s virtual environment will be used.
####
[​](https://gofastmcp.com/integrations/claude-desktop#environment-variables)
Environment Variables
Claude Desktop runs servers in a completely isolated environment with no access to your shell environment or locally installed applications. You must explicitly pass any environment variables your server needs.
If your server needs environment variables (like API keys), you must include them:
Copy
```
fastmcp install claude-desktop server.py --server-name "Weather Server" \
  --env API_KEY=your-api-key \
  --env DEBUG=true

```

Or load them from a `.env` file:
Copy
```
fastmcp install claude-desktop server.py --server-name "Weather Server" --env-file .env

```

  * **`uv`must be installed and available in your system PATH**. Claude Desktop runs in its own isolated environment and needs `uv` to manage dependencies.
  * **On macOS, it is recommended to install`uv` globally with Homebrew** so that Claude Desktop will detect it: `brew install uv`. Installing `uv` with other methods may not make it accessible to Claude Desktop.


###
[​](https://gofastmcp.com/integrations/claude-desktop#manual-configuration)
Manual Configuration
For more control over the configuration, you can manually edit Claude Desktop’s configuration file. You can open the configuration file from Claude’s developer settings, or find it in the following locations:
  * **macOS** : `~/Library/Application Support/Claude/claude_desktop_config.json`
  * **Windows** : `%APPDATA%\Claude\claude_desktop_config.json`

The configuration file is a JSON object with a `mcpServers` key, which contains the configuration for each MCP server.
Copy
```
{
  "mcpServers": {
    "dice-roller": {
      "command": "python",
      "args": ["path/to/your/server.py"]
    }
  }
}

```

After updating the configuration file, restart Claude Desktop completely. Look for the hammer icon (🔨) to confirm your server is loaded.
####
[​](https://gofastmcp.com/integrations/claude-desktop#dependencies-2)
Dependencies
If your server has dependencies, you can use `uv` or another package manager to set up the environment. When manually configuring dependencies, the recommended approach is to use `uv` with FastMCP. The configuration uses `uv run` to create an isolated environment with your specified packages:
Copy
```
{
  "mcpServers": {
    "dice-roller": {
      "command": "uv",
      "args": [
        "run",
        "--with", "fastmcp",
        "--with", "pandas",
        "--with", "requests",
        "fastmcp",
        "run",
        "path/to/your/server.py"
      ]
    }
  }
}

```

You can also manually specify Python versions and project directories in your configuration. Add `--python` to use a specific Python version, or `--project` to run within a project directory:
Copy
```
{
  "mcpServers": {
    "dice-roller": {
      "command": "uv",
      "args": [
        "run",
        "--python", "3.11",
        "--project", "/path/to/project",
        "--with", "fastmcp",
        "fastmcp",
        "run",
        "path/to/your/server.py"
      ]
    }
  }
}

```

The order of arguments matters: Python version and project settings come before package specifications, which come before the actual command to run.
  * **`uv`must be installed and available in your system PATH**. Claude Desktop runs in its own isolated environment and needs `uv` to manage dependencies.
  * **On macOS, it is recommended to install`uv` globally with Homebrew** so that Claude Desktop will detect it: `brew install uv`. Installing `uv` with other methods may not make it accessible to Claude Desktop.


####
[​](https://gofastmcp.com/integrations/claude-desktop#environment-variables-2)
Environment Variables
You can also specify environment variables in the configuration:
Copy
```
{
  "mcpServers": {
    "weather-server": {
      "command": "python",
      "args": ["path/to/weather_server.py"],
      "env": {
        "API_KEY": "your-api-key",
        "DEBUG": "true"
      }
    }
  }
}

```

Claude Desktop runs servers in a completely isolated environment with no access to your shell environment or locally installed applications. You must explicitly pass any environment variables your server needs.
##
[​](https://gofastmcp.com/integrations/claude-desktop#remote-servers)
Remote Servers
Users on Claude Pro, Max, Team, and Enterprise plans have first-class remote server support via integrations. For other users, or as an alternative approach, FastMCP can create a proxy server that forwards requests to a remote HTTP server. You can install the proxy server in Claude Desktop. Create a proxy server that connects to a remote HTTP server:
proxy_server.py
Copy
```
from fastmcp.server import create_proxy

# Create a proxy to a remote server
proxy = create_proxy(
    "https://example.com/mcp/sse",
    name="Remote Server Proxy"
)

if __name__ == "__main__":
    proxy.run()  # Runs via STDIO for Claude Desktop

```

###
[​](https://gofastmcp.com/integrations/claude-desktop#authentication)
Authentication
For authenticated remote servers, create an authenticated client following the guidance in the [client auth documentation](https://gofastmcp.com/clients/auth/bearer) and pass it to the proxy:
auth_proxy_server.py
Copy
```
from fastmcp import Client
from fastmcp.client.auth import BearerAuth
from fastmcp.server import create_proxy

# Create authenticated client
client = Client(
    "https://api.example.com/mcp/sse",
    auth=BearerAuth(token="your-access-token")
)

# Create proxy using the authenticated client
proxy = create_proxy(client, name="Authenticated Proxy")

if __name__ == "__main__":
    proxy.run()

```

[ Claude Code 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/claude-code)[ Cursor 🤝 FastMCP Next ](https://gofastmcp.com/integrations/cursor)
Ctrl+I
