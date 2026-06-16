# Managed Deep Agents CLI reference
Source: https://docs.langchain.com/langsmith/managed-deep-agents-cli

Reference for Managed Deep Agents CLI commands, project files, and deploy behavior.

The `deepagents` CLI, installed from the `deepagents-cli` package, provides deployment tooling for [Managed Deep Agents](/langsmith/managed-deep-agents-overview). Use it to scaffold local agent projects, deploy them to LangSmith, manage Managed Deep Agent resources, and register MCP servers.

<Note>
  Managed Deep Agents is in **private preview**, available on [LangSmith Cloud](/langsmith/cloud) in the US region only. [Join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist) to request access.
</Note>

For the fastest end-to-end path, see the [quickstart](/langsmith/managed-deep-agents-quickstart). For workflow guides, see [Connect tools](/langsmith/managed-deep-agents-mcp), [Deploy an agent](/langsmith/managed-deep-agents-deploy), and [Run an agent](/langsmith/managed-deep-agents-invoke).

## Requirements

<Note>
  Managed Deep Agents requires `deepagents-cli>=0.2.2`.
</Note>

Install `deepagents-cli` with `uv` (preferred) or `pip`:

<CodeGroup>
  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv tool install "deepagents-cli>=0.2.2"
  ```

  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install -U "deepagents-cli>=0.2.2"
  ```
</CodeGroup>

To upgrade an existing `uv` install, run `uv tool upgrade deepagents-cli`.

The CLI reads `LANGSMITH_API_KEY`. To create a key, see [Create an API key](/langsmith/create-account-api-key). To override the default endpoint, set `LANGSMITH_ENDPOINT`.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY="<LANGSMITH_API_KEY>"
```

Project `.env` files can set API keys. Project `.env` files cannot set endpoint, proxy, or TLS environment variables for managed API requests. Set those overrides in your shell or in `~/.deepagents/.env`.

## Command overview

| Command                                   | Use                                                             |
| ----------------------------------------- | --------------------------------------------------------------- |
| `deepagents --help`                       | Show CLI help.                                                  |
| `deepagents --version`                    | Show the installed `deepagents-cli` version.                    |
| `deepagents init [name]`                  | Scaffold a new Managed Deep Agents project.                     |
| `deepagents deploy`                       | Create or update a Managed Deep Agent from local project files. |
| `deepagents agents list`                  | List Managed Deep Agents in the workspace.                      |
| `deepagents agents get <agent_id>`        | Inspect one Managed Deep Agent.                                 |
| `deepagents agents delete <agent_id>`     | Delete one Managed Deep Agent.                                  |
| `deepagents mcp-servers list`             | List registered workspace MCP servers.                          |
| `deepagents mcp-servers add`              | Register a workspace MCP server.                                |
| `deepagents mcp-servers get <server>`     | Inspect one MCP server with header values redacted.             |
| `deepagents mcp-servers tools <server>`   | List a server's tools and print a `tools.json` snippet.         |
| `deepagents mcp-servers update <server>`  | Update an MCP server URL, headers, or auth type.                |
| `deepagents mcp-servers delete <server>`  | Delete one MCP server.                                          |
| `deepagents mcp-servers connect <server>` | Complete OAuth for an OAuth MCP server.                         |

Bare `deepagents` invocations do not start an interactive REPL. Install and run [Deep Agents Code](/oss/python/deepagents/code/overview) for interactive coding sessions.

## Initialize projects

Use `deepagents init` to create a project directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents init my-agent
```

If you omit the project name, the CLI prompts for it:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents init
```

| Argument or flag | Use                                                             |
| ---------------- | --------------------------------------------------------------- |
| `name`           | Project directory name. If omitted, the CLI prompts for a name. |
| `--force`        | Overwrite files in an existing project directory.               |
| `-h`, `--help`   | Show command help.                                              |

The `init` command creates the following files in the project directory:

| File or directory       | Description                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `agent.json`            | Agent metadata, model, backend, permissions, and optional target `agent_id`. See the [agent.json](#agent-json) section. |
| `AGENTS.md`             | Main agent instructions. See the [AGENTS.md](#agents-md) section.                                                       |
| `tools.json`            | Empty tool configuration. Add MCP-backed tools after registering a server. See the [tools.json](#tools-json) section.   |
| `skills/example-skill/` | Example skill directory. Edit, replace, or delete it. See the [skills](#skills) section.                                |
| `subagents/researcher/` | Example subagent directory. Edit, replace, or delete it. See the [subagents](#subagents) section.                       |
| `.gitignore`            | Excludes local `.env` files.                                                                                            |

## Deploy projects

Run `deepagents deploy` from a project directory:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents deploy
```

The first deploy creates a Managed Deep Agent. Later deploys update the same agent. Deploy state is user-local and stored outside your project, so files committed to the repository do not change which agent you deploy to.

By default, deploy uploads the project, polls the agent health endpoint, and prints the agent name, ID, short revision, agent URL, and a post-deploy MCP health check. Use `--detach` to skip polling and exit immediately after create or update.

| Flag           | Use                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------- |
| `--dir DIR`    | Project directory. Defaults to the current working directory.                                              |
| `--dry-run`    | Print the agent payload and managed file tree without sending a request.                                   |
| `--detach`     | Exit after create or update without polling the agent health endpoint.                                     |
| `--reset`      | Discard local deploy state and create a fresh agent. Cannot be used when `agent.json` declares `agent_id`. |
| `--yes`        | Confirm target-agent updates without prompting.                                                            |
| `-h`, `--help` | Show command help.                                                                                         |

`deepagents deploy --dry-run` prints JSON with:

| Field             | Description                                                       |
| ----------------- | ----------------------------------------------------------------- |
| `agent_payload`   | The create or update payload for the Managed Deep Agent resource. |
| `directory_files` | The managed file tree that deploy syncs to Context Hub.           |

### Target existing agents

For shared repositories or intentional updates to an existing Managed Deep Agent, declare the target in `agent.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "my-agent",
  "agent_id": "agent-uuid",
  "model": "openai:gpt-5.5",
  "backend": {
    "type": "state"
  }
}
```

On first use, the CLI asks you to confirm before updating that remote agent. Use `--yes` to skip the prompt.

### Validate the project before deploy

Deploy fails before sending a request when the project is malformed. Common validation rules include:

* `agent.json` and `AGENTS.md` are required.
* `agent.json` must contain a non-empty `name`.
* `backend.sandbox_config` requires `backend.type` to be `sandbox`.
* `backend.sandbox_config.scope` must be `thread` or `agent`.
* `backend.sandbox_config.policy_ids` must be an array of strings.
* `backend.sandbox_config.idle_ttl_seconds` and `backend.sandbox_config.delete_after_stop_seconds` must be integers.
* Symlinks are not allowed in deploy project inputs.
* `tools.json` must contain a `tools` array.
* Each tool in `tools.json` must include `name` and `mcp_server_url`.
* Skill files require YAML frontmatter with `name` and `description`.
* Subagent directories require `agent.json` and `AGENTS.md`.
* Legacy `deepagents.toml` and `mcp.json` files produce migration hints instead of being deployed.

Before deploying, the CLI also validates referenced MCP server URLs. If a server URL is not registered, deploy fails with a command hint to add it. If an OAuth server is registered but the caller cannot invoke it, deploy fails with a hint to run `deepagents mcp-servers connect <id|name|url>`.

## Manage agents

List agents:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents agents list
```

The command prints tab-separated rows with agent ID, agent name, and update time:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
e2de7a35-9dda-462b-b982-9e57051993bc\tmy-agent\t2026-06-01T12:00:00Z
```

Inspect an agent:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents agents get <agent_id>
```

Include managed files in the response:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents agents get <agent_id> --include-files
```

| Flag              | Use                                    |
| ----------------- | -------------------------------------- |
| `--include-files` | Include managed files in the response. |
| `-h`, `--help`    | Show command help.                     |

Delete an agent:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents agents delete <agent_id>
```

The delete command asks for confirmation. Skip the prompt with `--yes`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents agents delete <agent_id> --yes
```

| Flag           | Use                           |
| -------------- | ----------------------------- |
| `--yes`        | Skip the confirmation prompt. |
| `-h`, `--help` | Show command help.            |

## Manage MCP servers

For a practical setup guide, see [Connect tools](/langsmith/managed-deep-agents-mcp).

| Command                                                  | Use                                                       |
| -------------------------------------------------------- | --------------------------------------------------------- |
| `deepagents mcp-servers list`                            | List MCP server IDs, names, and URLs.                     |
| `deepagents mcp-servers add --url URL`                   | Register a static-header MCP server.                      |
| `deepagents mcp-servers add --url URL --auth-type oauth` | Register an OAuth MCP server.                             |
| `deepagents mcp-servers get <server>`                    | Print one MCP server as JSON with header values redacted. |
| `deepagents mcp-servers tools <server>`                  | List a server's tools and print a `tools.json` snippet.   |
| `deepagents mcp-servers update <server>`                 | Update server URL, headers, or auth type.                 |
| `deepagents mcp-servers delete <server>`                 | Delete one MCP server.                                    |
| `deepagents mcp-servers connect <server>`                | Start or reuse OAuth authorization for one MCP server.    |

Commands that take `<server>` accept an MCP server ID, exact name, or URL. Non-ID values are resolved against `deepagents mcp-servers list`; URL matching ignores case and trailing slashes. If a name or URL matches more than one server, re-run the command with the server ID.

### Add MCP servers

Register a static-header server:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents mcp-servers add \
  --url https://example.com/mcp \
  --name my-tools \
  --header Authorization="Bearer <token>"
```

| Flag                  | Use                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------- |
| `--url URL`           | MCP server URL. Required.                                                                |
| `--name NAME`         | Display name. Defaults to the URL hostname.                                              |
| `--header KEY=VALUE`  | Static credential header. Repeat for multiple headers.                                   |
| `--auth-type headers` | Static-header auth. This is the default.                                                 |
| `--auth-type oauth`   | OAuth auth. Cannot be combined with `--header`.                                          |
| `--connect`           | Start OAuth connection after creating an OAuth MCP server. Requires `--auth-type oauth`. |
| `--no-tools`          | Skip best-effort tool listing after registration.                                        |

Register an OAuth MCP server:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents mcp-servers add \
  --url https://example.com/mcp \
  --name github-tools \
  --auth-type oauth \
  --connect
```

OAuth `add` supports the same OAuth flags as [`connect`](/langsmith/managed-deep-agents-cli#connect-oauth-mcp-servers): `--scope`, `--force-new`, `--timeout`, and `--no-browser`.

### List MCP server tools

List a registered server's tools:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents mcp-servers tools <id|name|url>
```

The command prints each tool name and the first line of its description, then prints a paste-ready `tools.json` snippet. For OAuth servers, connect first so the MCP server record includes the caller's `oauth_provider_id`.

### Update MCP servers

Update a server URL or headers:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents mcp-servers update <id|name|url> \
  --url https://new.example.com/mcp \
  --header Authorization="Bearer <token>"
```

| Flag                  | Use                                                                               |
| --------------------- | --------------------------------------------------------------------------------- |
| `--url URL`           | Replace the server URL.                                                           |
| `--header KEY=VALUE`  | Replace stored headers with the provided header set. Repeat for multiple headers. |
| `--clear-headers`     | Clear stored headers. Cannot be combined with `--header`.                         |
| `--auth-type headers` | Set the auth type to static headers.                                              |

The command requires at least one change flag.

Delete an MCP server:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents mcp-servers delete <id|name|url>
```

The delete command asks for confirmation. Skip the prompt with `--yes`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents mcp-servers delete <id|name|url> --yes
```

### Connect OAuth MCP servers

Start or reuse OAuth authorization:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents mcp-servers connect <id|name|url>
```

| Flag                | Use                                                                               |
| ------------------- | --------------------------------------------------------------------------------- |
| `--scope SCOPE`     | OAuth scope to request. Repeat for multiple scopes.                               |
| `--force-new`       | Create a fresh OAuth session instead of reusing an existing token.                |
| `--timeout SECONDS` | Seconds to wait for OAuth completion. Use `0` to skip polling. Defaults to `300`. |
| `--no-browser`      | Print the verification URL without opening a browser.                             |

If authorization is pending, the CLI prints the verification URL. When `--timeout 0` is set, the CLI starts authorization and exits. Re-run `deepagents mcp-servers connect <id|name|url>` later to complete or reuse the connection.

## Project file reference

Managed Deep Agents projects use this layout:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-agent/
  agent.json
  AGENTS.md
  tools.json
  skills/<name>/SKILL.md
  skills/<name>/<file>
  subagents/<name>/agent.json
  subagents/<name>/AGENTS.md
  subagents/<name>/tools.json
  subagents/<name>/skills/<skill-name>/SKILL.md
```

### agent.json

`agent.json` configures the Managed Deep Agent resource:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "my-agent",
  "description": "A managed deep agent.",
  "model": "openai:gpt-5.5",
  "backend": {
    "type": "state"
  }
}
```

| Field         | Description                                                                    |
| ------------- | ------------------------------------------------------------------------------ |
| `name`        | Required non-empty agent name.                                                 |
| `description` | Optional agent description.                                                    |
| `agent_id`    | Optional existing Managed Deep Agent ID to update.                             |
| `model`       | Optional shorthand model identifier in `{provider}:{model_id}` form.           |
| `runtime`     | Optional API-shaped runtime object. Use either `model` or `runtime`, not both. |
| `backend`     | Optional backend configuration.                                                |
| `permissions` | Optional identity, visibility, and tenant access settings.                     |
| `extras`      | Optional extra metadata passed through to the API.                             |

### Configure the backend

Managed Deep Agents projects generated by `deepagents-cli>=0.2.2` use the `state` backend. Use a [LangSmith sandbox](/langsmith/sandboxes) backend when the agent needs an isolated environment for code execution, filesystem work, or long-running tasks.

| Backend type                                    | Use for                                           |
| ----------------------------------------------- | ------------------------------------------------- |
| `state`                                         | Use no sandbox-specific backend behavior.         |
| `sandbox` with `sandbox_config.scope: "thread"` | Scope LangSmith sandbox resources to each thread. |
| `sandbox` with `sandbox_config.scope: "agent"`  | Scope LangSmith sandbox resources to the agent.   |

Sandbox backends can include optional sandbox settings:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "backend": {
    "type": "sandbox",
    "sandbox_config": {
      "scope": "thread",
      "policy_ids": ["policy-id"],
      "idle_ttl_seconds": 900,
      "delete_after_stop_seconds": 300
    }
  }
}
```

`backend.sandbox_config` is valid only when `backend.type` is `sandbox`. For standalone sandbox features such as snapshots, service URLs, permissions, CLI commands, and SDK usage, see the [LangSmith sandboxes overview](/langsmith/sandboxes).

| Field                       | Description                                                                                            |
| --------------------------- | ------------------------------------------------------------------------------------------------------ |
| `scope`                     | Sandbox scope. Use `thread` for one sandbox per thread or `agent` for one sandbox shared by the agent. |
| `policy_ids`                | Array of sandbox policy IDs.                                                                           |
| `idle_ttl_seconds`          | Integer idle timeout.                                                                                  |
| `delete_after_stop_seconds` | Integer deletion delay after stop.                                                                     |

### Configure permissions

The optional `permissions` field in `agent.json` sets identity, visibility, and tenant access. Supported values are:

| Field                 | Values                 |
| --------------------- | ---------------------- |
| `identity`            | `personal`, `shared`   |
| `visibility`          | `tenant`, `user`       |
| `tenant_access_level` | `read`, `run`, `write` |

### AGENTS.md

`AGENTS.md` contains the main agent instructions. The CLI sends this content as the agent system prompt and stores it in the managed file tree.

### tools.json

`tools.json` configures MCP-backed tools. `deepagents init` creates this file with an empty `tools` array. Add tool entries after registering an MCP server:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "tools": [
    {
      "name": "example_tool",
      "mcp_server_url": "https://example.com/mcp",
      "mcp_server_name": "my-tools",
      "display_name": "example_tool"
    }
  ],
  "interrupt_config": {
    "https://example.com/mcp::example_tool": true
  }
}
```

Each tool requires `name` and `mcp_server_url`. `mcp_server_name` and `display_name` are optional. `interrupt_config` is optional and must be an object when present. Key each interrupt entry by `"{mcp_server_url}::{tool_name}"`. Additional `::{mcp_server_name}` components are accepted for compatibility.

### skills

Each skill lives under `skills/<name>/SKILL.md` and requires YAML frontmatter:

```mdx theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
---
name: summarize
description: Summarize text into a one-paragraph summary.
---

# Summarize

Given a text, produce a one-paragraph summary.
```

The CLI recursively includes all other files in the skill directory, excluding hidden paths.

### subagents

Each subagent lives under `subagents/<name>/` and requires:

| File         | Description                                            |
| ------------ | ------------------------------------------------------ |
| `agent.json` | Subagent metadata. Supports `description` and `model`. |
| `AGENTS.md`  | Subagent instructions.                                 |
| `tools.json` | Optional MCP-backed tools for the subagent.            |
| `skills/`    | Optional subagent-local skills.                        |

Example subagent `agent.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "description": "Researches a topic.",
  "model": "openai:gpt-5.5"
}
```

The legacy `model_id` key is still accepted in local subagent files, but new projects should use `model`. The REST API `SubagentSpec` uses `model_id`.

Subagent names come from directory names. Names are checked case insensitively for duplicates.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-cli.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Deploy a Managed Deep Agent
Source: https://docs.langchain.com/langsmith/managed-deep-agents-deploy

Create or update a Managed Deep Agent with the CLI, SDK, or REST API.

Deploying a Managed Deep Agent creates or updates the hosted agent resource and syncs the managed file tree that contains instructions, skills, subagents, and tool configuration. A deploy does not create a [LangSmith Deployment](/langsmith/deployment-quickstart). For more information on what a deploy does create, refer to [Created resources](/langsmith/managed-deep-agents-overview#created-resources).

Choose the interface that fits your task:

* [CLI](/langsmith/managed-deep-agents-cli) for most setups.
* [SDKs](/langsmith/managed-deep-agents-sdk) for Python or TypeScript automation.
* [REST API](/langsmith/managed-deep-agents-api-overview) when you need direct control over request payloads.

<Note>
  Managed Deep Agents is in **private preview**, available on [LangSmith Cloud](/langsmith/cloud) in the US region only. [Join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist) to request access.
</Note>

This page covers the full deploy workflow: project files, MCP tools, subagents, backends, shared-agent updates, and the REST API. For a faster, guided setup, see the [quickstart](/langsmith/managed-deep-agents-quickstart).

## Prerequisites

Before you deploy, make sure you have:

* Managed Deep Agents [private preview access](https://www.langchain.com/langsmith-managed-deep-agents-waitlist).
* A [LangSmith API key](/langsmith/create-account-api-key) for a workspace with preview access, exported as `LANGSMITH_API_KEY`.
* The `deepagents-cli` installed. For install and version requirements, see the [quickstart](/langsmith/managed-deep-agents-quickstart#prerequisites).

## Deploy from project files with the CLI

The CLI creates a local project, validates files, checks referenced MCP servers, and deploys the project to Managed Deep Agents. For all commands and project file rules, see the [CLI reference](/langsmith/managed-deep-agents-cli).

### Create a project

Create a Managed Deep Agents project:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents init my-agent
cd my-agent
```

The command generates:

| File or directory       | Purpose                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------- |
| `agent.json`            | Configures the managed agent name, model, backend, and optional target `agent_id`. |
| `AGENTS.md`             | Defines the agent instructions.                                                    |
| `tools.json`            | Starts empty. Add MCP-backed tools after registering an MCP server.                |
| `skills/example-skill/` | Contains an example skill you can edit or remove.                                  |
| `subagents/researcher/` | Contains an example subagent you can edit or remove.                               |
| `.gitignore`            | Excludes local environment files.                                                  |

You can also add:

| File or directory   | Purpose                                                      |
| ------------------- | ------------------------------------------------------------ |
| `skills/<name>/`    | Contains additional skills the agent can use.                |
| `subagents/<name>/` | Contains additional subagent definitions for delegated work. |

The generated `agent.json` uses the readable local CLI format:

```json agent.json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "my-agent",
  "description": "A managed deep agent.",
  "model": "openai:gpt-5.5",
  "backend": {
    "type": "state"
  }
}
```

<Note>
  Model identifiers use the `{provider}:{model_id}` form. For the providers and models you can use, see [Supported models](/langsmith/managed-deep-agents-overview#supported-models).
</Note>

Edit `AGENTS.md` to define the agent's behavior. The full project layout that deploy syncs to the managed file tree is:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-agent/
  agent.json                       # Agent metadata, model, and backend
  AGENTS.md                        # Main agent instructions (system prompt)
  tools.json                       # Optional: MCP-backed tools
  skills/<name>/SKILL.md           # Optional: reusable procedures
  subagents/<name>/agent.json      # Optional: delegated worker metadata
  subagents/<name>/AGENTS.md       # Optional: delegated worker instructions
  subagents/<name>/tools.json      # Optional: subagent-scoped MCP tools
```

`deepagents init` generates an empty `tools.json`, one example [skill](/oss/python/deepagents/skills), and one example [subagent](/oss/python/deepagents/subagents) so the initial deploy succeeds before you register an MCP server. Edit or remove the examples to fit your agent. Deploy reads every file in the project and syncs the tree to the [Context Hub](/langsmith/use-the-context-hub) agent repo. For the complete field reference, see the [CLI reference](/langsmith/managed-deep-agents-cli#project-file-reference).

### Add MCP tools

To let the agent call MCP tools, [register the MCP server](/langsmith/managed-deep-agents-mcp) once for the workspace, then add tool entries to the project `tools.json`. Tool entries reference a registered server by URL.

After you register a server, list its tools and print a paste-ready `tools.json` snippet:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
deepagents mcp-servers tools <id|name|url>
```

The `deepagents mcp-servers add` command also tries to list tools after registration. Pass `--no-tools` when you want to skip that discovery step.

```json tools.json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "tools": [
    {
      "name": "example_tool",
      "mcp_server_url": "https://example.com/mcp",
      "mcp_server_name": "my-tools",
      "display_name": "example_tool"
    }
  ],
  "interrupt_config": {
    "https://example.com/mcp::example_tool": true
  }
}
```

Each tool requires `name` and `mcp_server_url`. The `mcp_server_name` and `display_name` fields are optional. Use the optional `interrupt_config` object to require human approval before a tool runs. Key each entry by `"{mcp_server_url}::{tool_name}"` and set it to `true`.

Deploy validates referenced MCP server URLs before sending a request. If a server URL is not registered, deploy fails with a hint to add it. For server setup and OAuth, see [Connect tools](/langsmith/managed-deep-agents-mcp).

### Add subagents

Subagents are delegated workers the main agent can call for focused tasks. Add a `subagents/` directory to the project root, then create one directory per subagent. Each subagent directory requires an `agent.json` and an `AGENTS.md`, and can include its own `tools.json` and `skills/`. The subagent name comes from its directory name.

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
my-agent/
  agent.json
  AGENTS.md
  subagents/
    researcher/
      agent.json
      AGENTS.md
      tools.json                   # Optional: subagent-scoped MCP tools
      skills/                      # Optional: subagent-local skills
```

The subagent `agent.json` supports an optional `description` and `model`:

```json subagents/researcher/agent.json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "description": "Researches a topic and returns concise findings with citations.",
  "model": "openai:gpt-5.5"
}
```

Use `model` for new projects. For compatibility, the legacy `model_id` key still works in local subagent files, and the REST API subagent schema still uses `model_id`.

Write the subagent instructions in `subagents/researcher/AGENTS.md`:

```md subagents/researcher/AGENTS.md theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Researcher

Search for sources, take notes, and return concise findings with citations.
```

To give a subagent its own MCP tools, add `subagents/researcher/tools.json` with the same shape as the project-level `tools.json`. Subagent names are checked case insensitively for duplicates.

### Review the complete project

Tools and subagents live outside `agent.json`: tools in `tools.json`, subagents in the `subagents/` directory. A project that uses all three looks like this:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
research-assistant/
  agent.json
  AGENTS.md
  tools.json
  subagents/
    researcher/
      agent.json
      AGENTS.md
      tools.json
```

`agent.json` stays focused on agent metadata, model, and backend:

```json agent.json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "research-assistant",
  "description": "Research assistant that searches the web and delegates deep research.",
  "model": "openai:gpt-5.5",
  "backend": {
    "type": "state"
  }
}
```

`AGENTS.md` defines the main agent instructions:

```md AGENTS.md theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Research assistant

You are a research assistant. Use the available tools to search for sources, and
delegate deep research to the `researcher` subagent. Return concise answers with
citations.
```

`tools.json` references the workspace MCP server the main agent calls:

```json tools.json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "tools": [
    {
      "name": "web_search",
      "mcp_server_url": "https://example.com/mcp",
      "mcp_server_name": "my-tools"
    }
  ]
}
```

`subagents/researcher/agent.json` sets the subagent metadata and model:

```json subagents/researcher/agent.json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "description": "Researches a topic and returns concise findings with citations.",
  "model": "openai:gpt-5.5"
}
```

`subagents/researcher/AGENTS.md` defines the subagent instructions:

```md subagents/researcher/AGENTS.md theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
