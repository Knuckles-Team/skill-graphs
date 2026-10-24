[Skip to main content](https://gofastmcp.com/integrations/goose#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
AI Assistants
Goose 🤝 FastMCP
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
  * [Requirements](https://gofastmcp.com/integrations/goose#requirements)
  * [Create a Server](https://gofastmcp.com/integrations/goose#create-a-server)
  * [Install the Server](https://gofastmcp.com/integrations/goose#install-the-server)
  * [FastMCP CLI](https://gofastmcp.com/integrations/goose#fastmcp-cli)
  * [Dependencies](https://gofastmcp.com/integrations/goose#dependencies)
  * [Python Version](https://gofastmcp.com/integrations/goose#python-version)
  * [Environment Variables](https://gofastmcp.com/integrations/goose#environment-variables)
  * [Manual Configuration](https://gofastmcp.com/integrations/goose#manual-configuration)
  * [Dependencies](https://gofastmcp.com/integrations/goose#dependencies-2)
  * [Environment Variables](https://gofastmcp.com/integrations/goose#environment-variables-2)
  * [Using the Server](https://gofastmcp.com/integrations/goose#using-the-server)


AI Assistants
# Goose 🤝 FastMCP
Copy page
Install and use FastMCP servers in Goose
Copy page
**This integration focuses on running local FastMCP server files with STDIO transport.** For remote servers running with HTTP or SSE transport, use your client's native configuration - FastMCP's integrations focus on simplifying the complex local setup with dependencies and `uv` commands.
##
[​](https://gofastmcp.com/integrations/goose#requirements)
Requirements
This integration uses Goose’s deeplink protocol to register your server as a STDIO extension running via `uvx`. You must have Goose installed on your system for the deeplink to open automatically. For remote deployments, configure your FastMCP server with HTTP transport and add it to Goose directly using `goose configure` or the config file.
##
[​](https://gofastmcp.com/integrations/goose#create-a-server)
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
[​](https://gofastmcp.com/integrations/goose#install-the-server)
Install the Server
###
[​](https://gofastmcp.com/integrations/goose#fastmcp-cli)
FastMCP CLI
`3.0.0` The easiest way to install a FastMCP server in Goose is using the `fastmcp install goose` command. This generates a `goose://` deeplink and opens it, prompting Goose to install the server.
Copy
```
fastmcp install goose server.py

```

The install command supports the same `file.py:object` notation as the `run` command. If no object is specified, it will automatically look for a FastMCP server object named `mcp`, `server`, or `app` in your file:
Copy
```
# These are equivalent if your server object is named 'mcp'
fastmcp install goose server.py
fastmcp install goose server.py:mcp

# Use explicit object name if your server has a different name
fastmcp install goose server.py:my_custom_server

```

Under the hood, the generated command uses `uvx` to run your server in an isolated environment. Goose requires `uvx` rather than `uv run`, so the install produces a command like:
Copy
```
uvx --with pandas fastmcp run /path/to/server.py

```

####
[​](https://gofastmcp.com/integrations/goose#dependencies)
Dependencies
Use the `--with` flag to specify additional packages your server needs:
Copy
```
fastmcp install goose server.py --with pandas --with requests

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
[​](https://gofastmcp.com/integrations/goose#python-version)
Python Version
Use `--python` to specify which Python version your server should use:
Copy
```
fastmcp install goose server.py --python 3.11

```

The Goose install uses `uvx`, which does not support `--project`, `--with-requirements`, or `--with-editable`. If you need these options, use `fastmcp install mcp-json` to generate a full configuration and add it to Goose manually.
####
[​](https://gofastmcp.com/integrations/goose#environment-variables)
Environment Variables
Goose’s deeplink protocol does not support environment variables. If your server needs them (like API keys), you have two options:
  1. **Configure after install** : Run `goose configure` and add environment variables to the extension.
  2. **Manual config** : Use `fastmcp install mcp-json` to generate the full configuration, then add it to `~/.config/goose/config.yaml` with the `envs` field.


###
[​](https://gofastmcp.com/integrations/goose#manual-configuration)
Manual Configuration
For more control, you can manually edit Goose’s configuration file at `~/.config/goose/config.yaml`:
Copy
```
extensions:
  dice-roller:
    name: Dice Roller
    cmd: uvx
    args: [fastmcp, run, /path/to/server.py]
    enabled: true
    type: stdio
    timeout: 300

```

####
[​](https://gofastmcp.com/integrations/goose#dependencies-2)
Dependencies
When manually configuring, add packages using `--with` flags in the args:
Copy
```
extensions:
  dice-roller:
    name: Dice Roller
    cmd: uvx
    args: [--with, pandas, --with, requests, fastmcp, run, /path/to/server.py]
    enabled: true
    type: stdio
    timeout: 300

```

####
[​](https://gofastmcp.com/integrations/goose#environment-variables-2)
Environment Variables
Environment variables can be specified in the `envs` field:
Copy
```
extensions:
  weather-server:
    name: Weather Server
    cmd: uvx
    args: [fastmcp, run, /path/to/weather_server.py]
    enabled: true
    envs:
      API_KEY: your-api-key
      DEBUG: "true"
    type: stdio
    timeout: 300

```

You can also use `goose configure` to add extensions interactively, which prompts for environment variables.
**`uvx`(from`uv`) must be installed and available in your system PATH**. Goose uses `uvx` to run Python-based extensions in isolated environments.
##
[​](https://gofastmcp.com/integrations/goose#using-the-server)
Using the Server
Once your server is installed, you can start using your FastMCP server with Goose. Try asking Goose something like:
> “Roll some dice for me”
Goose will automatically detect your `roll_dice` tool and use it to fulfill your request, returning something like:
> 🎲 Here are your dice rolls: 4, 6, 4 You rolled 3 dice with a total of 14!
Goose can now access all the tools, resources, and prompts you’ve defined in your FastMCP server.
[ Gemini CLI 🤝 FastMCP Previous ](https://gofastmcp.com/integrations/gemini-cli)[ Anthropic API 🤝 FastMCP Next ](https://gofastmcp.com/integrations/anthropic)
Ctrl+I
