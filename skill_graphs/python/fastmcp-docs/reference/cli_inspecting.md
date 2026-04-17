[Skip to main content](https://gofastmcp.com/cli/inspecting#content-area)
Deploy FastMCP servers for free on
[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)
v3
Search...
Navigation
CLI
Inspecting Servers
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
  * [JSON Output](https://gofastmcp.com/cli/inspecting#json-output)
  * [Options](https://gofastmcp.com/cli/inspecting#options)
  * [Entrypoints](https://gofastmcp.com/cli/inspecting#entrypoints)


CLI
# Inspecting Servers
Copy page
View a server’s components and metadata
Copy page
`2.9.0` `fastmcp inspect` loads a server and reports what it contains — its tools, resources, prompts, version, and metadata. The default output is a human-readable summary:
Copy
```
fastmcp inspect server.py

```

Copy
```
Server: MyServer
Instructions: A helpful MCP server
Version: 1.0.0

Components:
  Tools: 5
  Prompts: 2
  Resources: 3
  Templates: 1

Environment:
  FastMCP: 2.0.0
  MCP: 1.0.0

Use --format [fastmcp|mcp] for complete JSON output

```

##
[​](https://gofastmcp.com/cli/inspecting#json-output)
JSON Output
For programmatic use, two JSON formats are available: **FastMCP format** (`--format fastmcp`) includes everything FastMCP knows about the server — tool tags, enabled status, output schemas, annotations, and custom metadata. Field names use `snake_case`. This is the format for debugging and introspecting FastMCP servers. **MCP protocol format** (`--format mcp`) shows exactly what MCP clients see through the protocol — only standard MCP fields, `camelCase` names, no FastMCP-specific extensions. This is the format for verifying client compatibility and debugging what clients actually receive.
Copy
```
# Full FastMCP metadata to stdout
fastmcp inspect server.py --format fastmcp

# MCP protocol view saved to file
fastmcp inspect server.py --format mcp -o manifest.json

```

##
[​](https://gofastmcp.com/cli/inspecting#options)
Options
Option | Flag | Description
---|---|---
Format |  `--format`, `-f` |  `fastmcp` or `mcp` (required when using `-o`)
Output File |  `--output`, `-o` | Save to file instead of stdout
##
[​](https://gofastmcp.com/cli/inspecting#entrypoints)
Entrypoints
The `inspect` command supports the same local entrypoints as [`fastmcp run`](https://gofastmcp.com/cli/running): inferred instances, explicit entrypoints, factory functions, and `fastmcp.json` configs.
Copy
```
fastmcp inspect server.py                  # inferred instance
fastmcp inspect server.py:my_server        # explicit entrypoint
fastmcp inspect server.py:create_server    # factory function
fastmcp inspect fastmcp.json               # config file

```

`inspect` only works with local files and `fastmcp.json` — it doesn’t connect to remote URLs or standard MCP config files.
[ Install MCP Servers Previous ](https://gofastmcp.com/cli/install-mcp)[ Client Commands Next ](https://gofastmcp.com/cli/client)
Ctrl+I
