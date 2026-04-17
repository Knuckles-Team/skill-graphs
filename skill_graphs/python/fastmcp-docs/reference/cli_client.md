[Skip to main content](https://gofastmcp.com/cli/client#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
CLI
Client Commands
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
  * [Listing Tools](https://gofastmcp.com/cli/client#listing-tools)
  * [Resources and Prompts](https://gofastmcp.com/cli/client#resources-and-prompts)
  * [Machine-Readable Output](https://gofastmcp.com/cli/client#machine-readable-output)
  * [Options](https://gofastmcp.com/cli/client#options)
  * [Calling Tools](https://gofastmcp.com/cli/client#calling-tools)
  * [Complex Arguments](https://gofastmcp.com/cli/client#complex-arguments)
  * [Error Handling](https://gofastmcp.com/cli/client#error-handling)
  * [Structured Output](https://gofastmcp.com/cli/client#structured-output)
  * [Interactive Elicitation](https://gofastmcp.com/cli/client#interactive-elicitation)
  * [Options](https://gofastmcp.com/cli/client#options-2)
  * [Discovering Configured Servers](https://gofastmcp.com/cli/client#discovering-configured-servers)
  * [LLM Agent Integration](https://gofastmcp.com/cli/client#llm-agent-integration)


CLI
# Client Commands
Copy page
List tools, call them, and discover configured servers
Copy page
`3.0.0` The CLI can act as an MCP client — connecting to any server (local or remote) to list what it exposes and call its tools directly. This is useful for development, debugging, scripting, and giving shell-capable LLM agents access to MCP servers.
##
[​](https://gofastmcp.com/cli/client#listing-tools)
Listing Tools
`fastmcp list` connects to a server and prints its tools as function signatures, showing parameter names, types, and descriptions at a glance:
Copy
```
fastmcp list http://localhost:8000/mcp
fastmcp list server.py
fastmcp list weather  # name-based resolution

```

When you need the full JSON Schema for a tool’s inputs or outputs — for understanding nested objects, enum constraints, or complex types — opt in with `--input-schema` or `--output-schema`:
Copy
```
fastmcp list server.py --input-schema

```

###
[​](https://gofastmcp.com/cli/client#resources-and-prompts)
Resources and Prompts
By default, only tools are shown. Add `--resources` or `--prompts` to include those:
Copy
```
fastmcp list server.py --resources --prompts

```

###
[​](https://gofastmcp.com/cli/client#machine-readable-output)
Machine-Readable Output
The `--json` flag switches to structured JSON with full schemas included. This is the format to use when feeding tool definitions to an LLM or building automation:
Copy
```
fastmcp list server.py --json

```

###
[​](https://gofastmcp.com/cli/client#options)
Options
Option | Flag | Description
---|---|---
Command | `--command` | Connect via stdio (e.g., `'npx -y @mcp/server'`)
Transport |  `--transport`, `-t` | Force `http` or `sse` for URL targets
Resources | `--resources` | Include resources in output
Prompts | `--prompts` | Include prompts in output
Input Schema | `--input-schema` | Show full input schemas
Output Schema | `--output-schema` | Show full output schemas
JSON | `--json` | Structured JSON output
Timeout | `--timeout` | Connection timeout in seconds
Auth | `--auth` |  `oauth` (default for HTTP), a bearer token, or `none`
##
[​](https://gofastmcp.com/cli/client#calling-tools)
Calling Tools
`fastmcp call` invokes a single tool on a server. Pass arguments as `key=value` pairs — the CLI fetches the tool’s schema and coerces your string values to the right types automatically:
Copy
```
fastmcp call server.py greet name=World
fastmcp call http://localhost:8000/mcp search query=hello limit=5

```

Type coercion is schema-driven: `"5"` becomes the integer `5` when the schema expects an integer. Booleans accept `true`/`false`, `yes`/`no`, and `1`/`0`. Arrays and objects are parsed as JSON.
###
[​](https://gofastmcp.com/cli/client#complex-arguments)
Complex Arguments
For tools with nested or structured parameters, `key=value` syntax gets awkward. Pass a single JSON object instead:
Copy
```
fastmcp call server.py create_item '{"name": "Widget", "tags": ["sale"], "metadata": {"color": "blue"}}'

```

Or use `--input-json` to provide a base dictionary, then override individual keys with `key=value` pairs:
Copy
```
fastmcp call server.py search --input-json '{"query": "hello", "limit": 5}' limit=10

```

###
[​](https://gofastmcp.com/cli/client#error-handling)
Error Handling
If you misspell a tool name, the CLI suggests corrections via fuzzy matching. Missing required arguments produce a clear message with the tool’s signature as a reminder. Tool execution errors are printed with a non-zero exit code, making the CLI straightforward to use in scripts.
###
[​](https://gofastmcp.com/cli/client#structured-output)
Structured Output
`--json` emits the raw result including content blocks, error status, and structured content:
Copy
```
fastmcp call server.py get_weather city=London --json

```

###
[​](https://gofastmcp.com/cli/client#interactive-elicitation)
Interactive Elicitation
Some tools request additional input during execution through MCP’s elicitation mechanism. When this happens, the CLI prompts you in the terminal — showing each field’s name, type, and whether it’s required. You can type `decline` to skip a question or `cancel` to abort the call entirely.
###
[​](https://gofastmcp.com/cli/client#options-2)
Options
Option | Flag | Description
---|---|---
Command | `--command` | Connect via stdio
Transport |  `--transport`, `-t` | Force `http` or `sse`
Input JSON | `--input-json` | Base arguments as JSON (merged with `key=value`)
JSON | `--json` | Raw JSON output
Timeout | `--timeout` | Connection timeout in seconds
Auth | `--auth` |  `oauth`, a bearer token, or `none`
##
[​](https://gofastmcp.com/cli/client#discovering-configured-servers)
Discovering Configured Servers
`fastmcp discover` scans your machine for MCP servers configured in editors and tools. It checks:
  * **Claude Desktop** — `claude_desktop_config.json`
  * **Claude Code** — `~/.claude.json`
  * **Cursor** — `.cursor/mcp.json` (walks up from current directory)
  * **Gemini CLI** — `~/.gemini/settings.json`
  * **Goose** — `~/.config/goose/config.yaml`
  * **Project** — `./mcp.json` in the current directory


Copy
```
fastmcp discover

```

The output groups servers by source, showing each server’s name and transport. Filter by source or get machine-readable output:
Copy
```
fastmcp discover --source claude-code
fastmcp discover --source cursor --source gemini --json

```

Any server that appears here can be used by name with `list`, `call`, and other commands — so you can go from “I have a server in Claude Code” to querying it without copying URLs or paths.
##
[​](https://gofastmcp.com/cli/client#llm-agent-integration)
LLM Agent Integration
For LLM agents that can execute shell commands but don’t have native MCP support, the CLI provides a clean bridge. The agent calls `fastmcp list --json` to discover available tools with full schemas, then `fastmcp call --json` to invoke them with structured results. Because the CLI handles connection management, transport selection, and type coercion internally, the agent doesn’t need to understand MCP protocol details — it just reads JSON and constructs shell commands.
[ Inspecting Servers Previous ](https://gofastmcp.com/cli/inspecting)[ Generate CLI Next ](https://gofastmcp.com/cli/generate-cli)
Ctrl+I
