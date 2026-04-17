[Skip to main content](https://gofastmcp.com/cli/generate-cli#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
CLI
Generate CLI
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
  * [Generating a Script](https://gofastmcp.com/cli/generate-cli#generating-a-script)
  * [What You Get](https://gofastmcp.com/cli/generate-cli#what-you-get)
  * [Parameter Handling](https://gofastmcp.com/cli/generate-cli#parameter-handling)
  * [Agent Skill](https://gofastmcp.com/cli/generate-cli#agent-skill)
  * [How It Works](https://gofastmcp.com/cli/generate-cli#how-it-works)


CLI
# Generate CLI
Copy page
Scaffold a standalone typed CLI from any MCP server
Copy page
`3.0.0` `fastmcp list` and `fastmcp call` are general-purpose — you always specify the server, the tool name, and the arguments from scratch. `fastmcp generate-cli` goes further: it connects to a server, reads its tool schemas, and writes a standalone Python script where every tool is a proper subcommand with typed flags, help text, and tab completion. The result is a CLI that feels hand-written for that specific server. MCP tool schemas already contain everything a CLI framework needs — parameter names, types, descriptions, required/optional status, and defaults. `generate-cli` maps that into `--help` text, and required parameters become mandatory flags.
##
[​](https://gofastmcp.com/cli/generate-cli#generating-a-script)
Generating a Script
Point the command at any [server target](https://gofastmcp.com/cli/overview#server-targets) and it writes a CLI script:
Copy
```
fastmcp generate-cli weather
fastmcp generate-cli http://localhost:8000/mcp
fastmcp generate-cli server.py my_weather_cli.py

```

The second positional argument sets the output path (defaults to `cli.py`). If the file already exists, pass `-f` to overwrite:
Copy
```
fastmcp generate-cli weather -f

```

##
[​](https://gofastmcp.com/cli/generate-cli#what-you-get)
What You Get
The generated script is a regular Python file — executable, editable, and yours:
Copy
```
$ python cli.py call-tool --help
Usage: weather-cli call-tool COMMAND

Call a tool on the server

Commands:
  get_forecast  Get the weather forecast for a city.
  search_city   Search for a city by name.

```

Each tool has typed parameters with help text pulled directly from the server’s schema:
Copy
```
$ python cli.py call-tool get_forecast --help
Usage: weather-cli call-tool get_forecast [OPTIONS]

Get the weather forecast for a city.

Options:
  --city    [str]  City name (required)
  --days    [int]  Number of forecast days (default: 3)

```

Beyond tool commands, the script includes generic MCP operations — `list-tools`, `list-resources`, `read-resource`, `list-prompts`, and `get-prompt` — that always reflect the server’s current state, even if tools have changed since generation.
##
[​](https://gofastmcp.com/cli/generate-cli#parameter-handling)
Parameter Handling
Parameters are mapped based on their JSON Schema type: **Simple types** (`string`, `integer`, `number`, `boolean`) become typed flags:
Copy
```
python cli.py call-tool get_forecast --city London --days 3

```

**Arrays of simple types** become repeatable flags:
Copy
```
python cli.py call-tool tag_items --tags python --tags fastapi --tags mcp

```

**Complex types** (objects, nested arrays, unions) accept JSON strings. The `--help` output shows the full schema so you know what structure to pass:
Copy
```
python cli.py call-tool create_user \
  --name John \
  --metadata '{"role": "admin", "dept": "engineering"}'

```

##
[​](https://gofastmcp.com/cli/generate-cli#agent-skill)
Agent Skill
Alongside the CLI script, `generate-cli` writes a `SKILL.md` file — a `--help` or experimenting with flag names. To skip skill generation:
Copy
```
fastmcp generate-cli weather --no-skill

```

##
[​](https://gofastmcp.com/cli/generate-cli#how-it-works)
How It Works
The generated script is a _client_ , not a server — it connects to the server on every invocation rather than bundling it. A `CLIENT_SPEC` variable at the top holds the resolved transport (a URL string or `StdioTransport` with baked-in command and arguments). The most common edit is changing `CLIENT_SPEC` — for example, pointing a script generated from a dev server at production. Beyond that, the helper functions (`_call_tool`, `_print_tool_result`) are thin wrappers around `fastmcp.Client` that are easy to adapt. The script requires `fastmcp` as a dependency. If it lives outside a project that already has FastMCP installed:
Copy
```
uv run --with fastmcp python cli.py call-tool get_forecast --city London

```

[ Client Commands Previous ](https://gofastmcp.com/cli/client)[ Auth Utilities Next ](https://gofastmcp.com/cli/auth)
Ctrl+I
