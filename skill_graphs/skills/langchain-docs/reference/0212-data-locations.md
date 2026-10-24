# Data locations
Source: https://docs.langchain.com/oss/python/deepagents/code/data-locations

Where Deep Agents Code stores configuration, sessions, and customization files

Deep Agents Code stores data in two directory hierarchies:

* **`~/.deepagents/`** — Deep Agents-specific data (agent memory, skills, sessions)
* **`~/.agents/`** — Tool-agnostic data (skills shared across AI CLI tools)

## Directory structure

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
~/.deepagents/
├── .state/                  # Per-machine Deep Agents Code state (managed automatically)
│   ├── sessions.db          #   SQLite database for conversation checkpoints
│   ├── history.jsonl        #   Command input history
│   ├── chatgpt-auth.json    #   ChatGPT OAuth token for the openai_codex provider
│   ├── ...                  #   Other markers & credentials
└── {agent}/                 # Per-agent directory (default: "agent")
    ├── AGENTS.md            # User customizations to agent instructions
    ├── skills/              # User-level skills
    │   └── {skill-name}/
    │       └── SKILL.md
    └── agents/              # Custom subagent definitions
        └── {subagent-name}/
            └── AGENTS.md

~/.agents/                   # Tool-agnostic alias (shared across AI CLIs)
└── skills/                  # Skills available to any compatible tool
    └── {skill-name}/
        └── SKILL.md

{project}/                   # Project-level (in git repo root)
├── AGENTS.md                # Project instructions (root-level)
└── .deepagents/
│   ├── AGENTS.md            # Project instructions (preferred location)
│   ├── skills/              # Project-specific skills
│   │   └── {skill-name}/
│   │       └── SKILL.md
│   └── agents/              # Project-specific subagents
│       └── {subagent-name}/
│           └── AGENTS.md
└── .agents/                 # Tool-agnostic project skills
    └── skills/
        └── {skill-name}/
            └── SKILL.md
```

## What goes where

| Data                     | Location                                   | Read/Write | Notes                                                                                                                                                                              |
| ------------------------ | ------------------------------------------ | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sessions**             | `~/.deepagents/.state/sessions.db`         | R/W        | SQLite checkpoint database                                                                                                                                                         |
| **Input history**        | `~/.deepagents/.state/history.jsonl`       | R/W        | JSON-lines, up/down arrow recall                                                                                                                                                   |
| **ChatGPT OAuth token**  | `~/.deepagents/.state/chatgpt-auth.json`   | R/W        | Backs the [`openai_codex`](/oss/python/deepagents/code/providers) provider; created when you sign in with ChatGPT and refreshed automatically. Readable only by your user account. |
| **Base instructions**    | Package `default_agent_prompt.md`          | R          | Immutable, updated with Deep Agents Code upgrades                                                                                                                                  |
| **User customizations**  | `~/.deepagents/{agent}/AGENTS.md`          | R/W        | Appended to base instructions                                                                                                                                                      |
| **Project instructions** | `.deepagents/AGENTS.md` or `AGENTS.md`     | R          | Both loaded if present                                                                                                                                                             |
| **User skills**          | `~/.deepagents/{agent}/skills/`            | R/W        | Agent-specific skills                                                                                                                                                              |
| **Shared skills**        | `~/.agents/skills/`                        | R          | Tool-agnostic, cross-CLI                                                                                                                                                           |
| **Project skills**       | `.deepagents/skills/` or `.agents/skills/` | R          | Project-scoped                                                                                                                                                                     |
| **Custom subagents**     | `~/.deepagents/{agent}/agents/`            | R/W        | User-defined subagents                                                                                                                                                             |
| **Project subagents**    | `.deepagents/agents/`                      | R          | Project-defined subagents                                                                                                                                                          |

## Precedence rules

When the same item exists in multiple locations, **higher precedence wins completely** (no merging).

### Skills

Precedence order (lowest to highest):

1. `~/.deepagents/{agent}/skills/` — User Deep Agents Code
2. `~/.agents/skills/` — User tool-agnostic
3. `.deepagents/skills/` — Project Deep Agents Code
4. `.agents/skills/` — Project tool-agnostic *(highest)*

When a skill is loaded, Deep Agents Code verifies that the resolved file path stays within one of these directories. Symlinks that resolve outside all skill roots are rejected. To allow symlink targets in additional directories, see [`[skills].extra_allowed_dirs`](/oss/python/deepagents/code/configuration#skill-directory-allowlist).

### Subagents

Precedence order (lowest to highest):

1. `~/.deepagents/{agent}/agents/` — User-level
2. `.deepagents/agents/` — Project-level *(highest)*

Each subagent is an `AGENTS.md` file with YAML frontmatter (`name`, `description`, optional `model`) and a markdown body for the system prompt. See [Use subagents in Deep Agents Code](/oss/python/deepagents/code/subagents) for the full format reference.

### Instructions

All instruction sources are **combined** (not overridden):

1. Package base prompt *(always loaded)*
2. `~/.deepagents/{agent}/AGENTS.md` *(appended)*
3. `.deepagents/AGENTS.md` *(appended)*
4. `AGENTS.md` at project root *(appended)*

## `.deepagents` vs `.agents`

| Directory      | Purpose                   | When to use                                                   |
| -------------- | ------------------------- | ------------------------------------------------------------- |
| `.deepagents/` | Deep Agents Code-specific | Skills and config that use Deep Agents Code-specific features |
| `.agents/`     | Tool-agnostic             | Skills you want to share across different AI CLI tools        |

<Tip>
  Use `.agents/skills/` for skills that work with any AI coding assistant.
  Use `.deepagents/skills/` for skills that rely on Deep Agents-specific tools or conventions.
</Tip>

## Cleaning up

| Need                        | Action                                             |
| --------------------------- | -------------------------------------------------- |
| Reset all data              | `rm -rf ~/.deepagents`                             |
| Clear sessions only         | `rm ~/.deepagents/.state/sessions.db*`             |
| Clear input history         | `rm ~/.deepagents/.state/history.jsonl`            |
| Clear stored API keys       | `rm ~/.deepagents/.state/auth.json`                |
| Clear MCP OAuth tokens      | `rm -rf ~/.deepagents/.state/mcp-tokens`           |
| Clear MCP project trust     | `rm ~/.deepagents/.state/mcp_trust.json`           |
| Re-run first-run onboarding | `rm ~/.deepagents/.state/onboarding_complete`      |
| Reset agent instructions    | `dcode agents reset --agent {name}`                |
| Remove a skill              | `rm -rf ~/.deepagents/{agent}/skills/{skill-name}` |

<Warning>
  Deleting `~/.deepagents/.state/sessions.db` will remove all conversation history and checkpoints.

  This cannot be undone unless you have a backup of the `sessions.db` file.
</Warning>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/data-locations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# MCP tools
Source: https://docs.langchain.com/oss/python/deepagents/code/mcp-tools

Load additional tools from MCP (Model Context Protocol) servers

[MCP (Model Context Protocol)](https://modelcontextprotocol.io/) lets you extend Deep Agents Code with tools from external servers—file systems, APIs, databases, and more—without modifying the agent itself. Deep Agents Code connects to MCP servers at startup, discovers their tools, and makes them available to the agent alongside the built-in tools.

Add MCP servers by adding a `.mcp.json` config file to your project for project-level scope, or at user-level to apply to all projects.

## Quickstart

This quickstart adds the [LangChain documentation MCP server](https://docs.langchain.com/mcp) to every Deep Agents Code session on your machine. Swap in any other MCP server's URL or stdio command in the same shape.

<Steps>
  <Step title="Create the config file" icon="file">
    If not already present, create the `.mcp.json` file at user-level to make the server available to every project on the machine or at project-level.

    <Tabs>
      <Tab title="User">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        mkdir -p ~/.deepagents
        touch ~/.deepagents/.mcp.json
        ```

        Servers in this file (`~/.deepagents/.mcp.json`) are available in every project on this machine.
      </Tab>

      <Tab title="Project">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        touch .mcp.json
        ```

        Servers in this file (`<project>/.mcp.json`) are available to this project.
      </Tab>

      <Tab title="Project (hidden)">
        ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
        mkdir -p .deepagents
        touch .deepagents/.mcp.json
        ```

        Servers in this file (`<project>/.deepagents/.mcp.json`) are available to this project but kept out of the repo root.
      </Tab>
    </Tabs>

    See [Discovery locations](#discovery-locations) for full precedence rules.
  </Step>

  <Step title="Add the MCP server" icon="plug">
    ```json title="~/.deepagents/.mcp.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    {
        "mcpServers": {
            "docs-langchain": {
                "type": "http",
                "url": "https://docs.langchain.com/mcp"
            }
        }
    }
    ```

    To add more servers, add more entries to `mcpServers`. See [Configuration format](#configuration-format) for OAuth, stdio, SSE, and HTTP server fields, environment variables, and headers.
  </Step>

  <Step title="Launch Deep Agents Code" icon="terminal">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    dcode
    ```

    On startup, Deep Agents Code auto-discovers the config, connects to each server, discovers its tools, and prints a confirmation:

    ```
    ✓ Loaded 3 MCP tools
    ```

    Run `/mcp` in an interactive session to see per-server status, transport, and the loaded tool list. The agent can now use those tools for the duration of the session—stdio servers are kept alive between tool calls.
  </Step>
</Steps>

## Auto-discovery

Deep Agents Code automatically searches for `.mcp.json` files in standard locations. No flags are needed—just place a config file and it gets picked up.

### Discovery locations

Configs are checked in this order (lowest to highest precedence):

| Priority    | Location                          | Scope                                       |
| ----------- | --------------------------------- | ------------------------------------------- |
| 1 (lowest)  | `~/.deepagents/.mcp.json`         | User-level—applies to all projects          |
| 2           | `<project>/.deepagents/.mcp.json` | Project-level—`.deepagents` subdirectory    |
| 3 (highest) | `<project>/.mcp.json`             | Project-level—root (Claude Code compatible) |

The project root is the nearest parent directory containing a `.git` folder, falling back to the current working directory.

When multiple config files exist, their `mcpServers` entries are merged. If the same server name appears in more than one file, the higher-precedence config wins. This lets a project-level config override a user-level entry (for example, pinning a different version of the same server) without disturbing your other projects.

### Flags

| Flag                | Behavior                                                                                           |
| ------------------- | -------------------------------------------------------------------------------------------------- |
| `--mcp-config PATH` | Add an explicit config as the highest-precedence source (merged on top of auto-discovered configs) |
| `--no-mcp`          | Disable MCP entirely—no servers are loaded                                                         |

<Note>
  `--mcp-config` and `--no-mcp` are mutually exclusive.
</Note>

### Claude Code compatibility

If you already have a `.mcp.json` at your project root for Claude Code, Deep Agents Code picks it up automatically—no extra setup needed.

## Configuration format

Each key under `mcpServers` is a server name. The server's fields determine how Deep Agents Code connects to it.

### stdio servers (default)

stdio servers are spawned as child processes. Deep Agents Code communicates with them over stdin/stdout.

```json title="mcp-config.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
      "env": {}
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "your-token" }
    }
  }
}
```

### SSE and HTTP servers

For remote MCP servers, set `type` to `"sse"` or `"http"` and provide a `url`:

```json title="mcp-config.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "mcpServers": {
    "remote-api": {
      "type": "sse",
      "url": "https://api.example.com/mcp",
      "headers": { "Authorization": "Bearer your-token" }
    }
  }
}
```

### Field reference

<AccordionGroup>
  <Accordion title="stdio (default)">
    **Required:** `command`. **Optional:** `args`, `env`, plus the shared [tool-filter fields](#tool-filtering).

    <ResponseField name="command" type="string">
      The executable to run.
    </ResponseField>

    <ResponseField name="args" type="string[]">
      Arguments passed to the command.
    </ResponseField>

    <ResponseField name="env" type="object">
      Environment variables set for the subprocess. Use this to pass API keys and other credentials without exposing them in shell history.
    </ResponseField>
  </Accordion>

  <Accordion title="sse">
    **Required:** `type: "sse"`, `url`. **Optional:** `headers`, `auth`, plus the shared [tool-filter fields](#tool-filtering).

    <ResponseField name="type" type="&#x22;sse&#x22;">
      Transport type. Use `"sse"` for Server-Sent Events.
    </ResponseField>

    <ResponseField name="url" type="string">
      The server endpoint URL.
    </ResponseField>

    <ResponseField name="headers" type="object">
      HTTP headers sent with every request. Commonly used for authentication. Values support `${VAR}` references to parent-shell environment variables (resolved when the server activates).
    </ResponseField>

    <ResponseField name="auth" type="&#x22;oauth&#x22;">
      Set to `"oauth"` to drive an OAuth login flow with `dcode mcp login` instead of supplying an `Authorization` header. Cannot be combined with an `Authorization` header. See [OAuth login](#oauth-login).
    </ResponseField>
  </Accordion>

  <Accordion title="http">
    **Required:** `type: "http"`, `url`. **Optional:** `headers`, `auth`, plus the shared [tool-filter fields](#tool-filtering).

    <ResponseField name="type" type="&#x22;http&#x22;">
      Transport type. Use `"http"` for streamable HTTP. `streamable_http` and `streamable-http` are accepted as aliases.
    </ResponseField>

    <ResponseField name="url" type="string">
      The server endpoint URL.
    </ResponseField>

    <ResponseField name="headers" type="object">
      HTTP headers sent with every request. Commonly used for authentication. Values support `${VAR}` references to parent-shell environment variables (resolved when the server activates).
    </ResponseField>

    <ResponseField name="auth" type="&#x22;oauth&#x22;">
      Set to `"oauth"` to drive an OAuth login flow with `dcode mcp login` instead of supplying an `Authorization` header. Cannot be combined with an `Authorization` header. See [OAuth login](#oauth-login).
    </ResponseField>
  </Accordion>
</AccordionGroup>

<Note>
  The `type` field can also be written as `transport` for compatibility with other MCP clients.
</Note>

<Note>
  Server names must match `[A-Za-z0-9_-]+`. Names are used as on-disk basenames for OAuth token files, so path separators and other shell metacharacters are rejected at config load.
</Note>

### Header environment variables

Header values support `${VAR}` substitution from the parent shell, resolved at server activation rather than at config load. One unset variable only fails the server that needs it; the rest still come up.

```json title=".mcp.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "mcpServers": {
        "internal-api": {
            "type": "http",
            "url": "https://api.example.com/mcp",
            "headers": { "Authorization": "Bearer ${INTERNAL_API_TOKEN}" }
        }
    }
}
```

## Multiple servers

You can configure as many servers as you need. Tools from all servers are merged and available to the agent:

```json title="mcp-config.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_TOKEN": "ghp_..." }
    },
    "database": {
      "type": "sse",
      "url": "https://db-mcp.internal:8080/mcp",
      "headers": { "Authorization": "Bearer ..." }
    }
  }
}
```

## Tool filtering

Each server may narrow the tools it exposes to the agent with one of two optional fields:

* `allowedTools`: keep only the listed tools; drop everything else.
* `disabledTools`: drop the listed tools; keep everything else.

Filtering applies to stdio, HTTP, and SSE servers alike. Both of the following are rejected at config load:

* Setting `allowedTools` and `disabledTools` on the same server.
* Setting either field to an empty list (would silently strip every tool, or be a no-op). Omit the field instead.

```json title=".mcp.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
      "allowedTools": ["read_file", "list_directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "disabledTools": ["delete_repository", "delete_*_branch"]
    }
  }
}
```

### Match rules

Each entry is a literal tool name or an [`fnmatch`](https://docs.python.org/3/library/fnmatch.html)-style glob (any entry containing `*`, `?`, or `[` is treated as a pattern). Entries are matched against both the bare MCP tool name and the server-prefixed form (`{server}_{tool}`), so either form works:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "allowedTools": ["read_file", "fs_list_*"]
}
```

<Note>
  Entries that match no loaded tool are logged as a warning, not an error — the underlying MCP server can evolve its tool list across versions without breaking your config.
</Note>

<ResponseField name="allowedTools" type="string[]">
  Tool names or `fnmatch` glob patterns to keep. All other tools from this server are dropped. Mutually exclusive with `disabledTools`.
</ResponseField>

<ResponseField name="disabledTools" type="string[]">
  Tool names or `fnmatch` glob patterns to drop. All other tools from this server are kept. Mutually exclusive with `allowedTools`.
</ResponseField>

## OAuth login

For remote MCP servers that require OAuth (Slack, GitHub, Notion, Linear, and other hosted MCP endpoints), set `"auth": "oauth"` on the server entry and run the login subcommand once. Tokens are persisted to disk and refreshed automatically.

### Configure the server

```json title=".mcp.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "mcpServers": {
        "linear": {
            "type": "http",
            "url": "https://mcp.linear.app/mcp",
            "auth": "oauth"
        }
    }
}
```

`auth: "oauth"` is mutually exclusive with an `Authorization` header on the same entry, and cannot be set on a stdio server.

To connect Deep Agents Code to LangSmith, use the [LangSmith Remote MCP](/langsmith/langsmith-remote-mcp):

```json title=".mcp.json" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
    "mcpServers": {
        "langsmith": {
            "url": "https://api.smith.langchain.com/mcp",
            "transport": "http",
            "auth": "oauth"
        }
    }
}
```

### Run the login flow

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
dcode mcp login linear
```

What happens depends on the server's host:

* **Spec-compliant servers** (the default): Deep Agents Code performs Dynamic Client Registration, opens an Authorization Code + PKCE flow in your browser, and asks you to paste the redirected URL back into the terminal.
* **Slack** (`slack.com`, `*.slack.com`): same paste-back flow, but with Slack's public client preseeded. You're prompted for an optional team ID (e.g., `T01234567`) so the app installs into the right workspace.
* **GitHub** (`api.githubcopilot.com`): RFC 8628 Device Authorization Grant. Deep Agents Code prints a verification URL and a user code; you enter the code in your browser and Deep Agents Code polls for completion.

By default, `dcode mcp login` reads the same auto-discovered configs Deep Agents Code uses at runtime (subject to project-level trust gating). Pass `--config <path>` to use a specific file:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
dcode mcp login linear --config ./mcp-config.json
```

<Warning>
  Project-level configs that haven't been trusted (see [Project-level trust](#project-level-trust)) are skipped during `mcp login` to prevent attacker-controlled `headers` entries from exfiltrating local secrets through `${VAR}` interpolation. Run `dcode` in the project once to approve the config, or pass `--config <path>` explicitly.
</Warning>

### Token storage

Tokens are written to:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
~/.deepagents/.state/mcp-tokens/<server>-<sha256-16(url)>.json
```

The `<sha256-16(url)>` segment is the first 16 hex characters of the SHA-256 of the server URL. The directory is locked to mode `0700` and each token file is mode `0600`. Files include the OAuth access token, refresh token, and the dynamically registered client info, all in a schema-versioned payload that's written atomically (write-to-temp + `rename`).

<Note>
  Hashing the URL into the filename means the same server name pointing at different URLs (for example, dev vs. prod) gets independent token files and can't trample each other.
</Note>

### Re-authentication

When refresh fails at runtime (the refresh token expired or was revoked), Deep Agents Code marks the server as `unauthenticated` instead of crashing the agent. The welcome banner shows the count of unauthenticated servers, and `/mcp` reports the reason per server. Re-run `dcode mcp login <server>` to refresh credentials — your conversation continues without restarting.

## Server status

Each configured server lands in one of three states after startup:

| Status            | Meaning                                                                        |
| ----------------- | ------------------------------------------------------------------------------ |
| `ok`              | Connected; tools are loaded and available to the agent                         |
| `unauthenticated` | OAuth login required or refresh failed — run `dcode mcp login <server>`        |
| `error`           | Pre-flight, discovery, or transport setup failed; an error message is attached |

A single failing server no longer aborts startup. The agent runs with whichever servers came up cleanly, and the welcome banner surfaces counts of unauthenticated and errored servers next to the tool count. Open `/mcp` in an interactive session to see per-server status, transport, tool list, and the failure reason for non-`ok` entries. The viewer live-updates as servers connect and supports `tab`/`shift+tab` navigation.

## Project-level trust

Project-level configs can contain stdio servers that execute local commands and remote servers whose `headers` may interpolate `${VAR}` from your environment. To prevent untrusted repositories from running arbitrary code or exfiltrating local secrets on CLI startup, Deep Agents Code enforces a **default-deny** policy for project-level entries.

### How it works

* **Interactive mode:** Deep Agents Code prompts for approval before activating project servers, showing each stdio command and remote URL. Approval is persisted using a SHA-256 content fingerprint—if the config changes, you are prompted again.
* **Non-interactive mode (`-n`):** Project servers are silently skipped unless `--trust-project-mcp` is passed.
* **Trust covers stdio and remote entries alike** — remote servers can SSRF into localhost or cloud-metadata endpoints during the pre-flight probe and exfiltrate `${VAR}` values via headers, so they're gated the same way as stdio.
* **User-level configs** (`~/.deepagents/.mcp.json`) are always trusted—the same trust model as `config.toml` and `hooks.json`.
* **`dcode mcp login`** also honors project trust: an untrusted project-level config is skipped during login discovery so an attacker-controlled remote entry cannot pull secrets into the OAuth handshake.

### Flags

| Flag                  | Behavior                                                                        |
| --------------------- | ------------------------------------------------------------------------------- |
| `--trust-project-mcp` | Trust all project-level stdio servers without prompting (for CI and automation) |

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Skip the approval prompt
dcode --trust-project-mcp

# Non-interactive: explicitly trust project servers
dcode -n "run tests" --trust-project-mcp
```

### Trust store

Trust decisions are stored in `~/.deepagents/.state/mcp_trust.json`:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "version": 1,
  "projects": {
    "/Users/you/myproject": "sha256:abc123..."
  }
}
```

Each key under `projects` is an absolute project root path. The value is a SHA-256 digest of the concatenated project-level config contents. To revoke trust, delete the entry or modify the project's `.mcp.json` (which invalidates the fingerprint automatically).

<Warning>
  A trusted stdio MCP server has the same permissions as your user account. Only approve servers from repositories you trust. Review the commands shown in the approval prompt before accepting.
</Warning>

## System prompt awareness

Connected MCP servers and their tools are automatically listed in the agent's system prompt, grouped by server name and transport type. This helps the model reason about tool provenance and failure domains without requiring manual context.

## Troubleshooting

<AccordionGroup>
  <Accordion title="Server fails to start (stdio)">
    Verify the command works outside Deep Agents Code:

    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    npx -y @modelcontextprotocol/server-filesystem /tmp
    ```

    Common causes: the package isn't installed, `npx` isn't on `PATH`, or required environment variables are missing.
  </Accordion>

  <Accordion title="Connection refused (SSE/HTTP)">
    Check that the remote server is running and the URL is correct. If the server requires authentication, make sure `headers` includes the correct credentials.
  </Accordion>

  <Accordion title="Tools not appearing">
    Deep Agents Code prints the number of tools loaded at startup (e.g., `✓ Loaded 3 MCP tools`). If you see `0`, the server started successfully but didn't advertise any tools—check the server's own logs or documentation.
  </Accordion>

  <Accordion title="Server shows `unauthenticated` in /mcp">
    Either you haven't run `dcode mcp login <server>` yet, or the persisted refresh token expired or was revoked server-side. Run the login command again — your session keeps running and the server will re-attach once tokens are refreshed.
  </Accordion>

  <Accordion title="`Invalid MCP config at ...`">
    A pre-flight validation rejected `--mcp-config` (or an auto-discovered `.mcp.json`). Common causes: an unsupported server name (must match `[A-Za-z0-9_-]+`), `auth: oauth` on a stdio server, both `command` and `url` set on the same entry, or a header value that isn't a string. Fix the highlighted reason and relaunch — Deep Agents Code no longer dumps a multi-page subprocess trace for config errors.
  </Accordion>

  <Accordion title="`${VAR}` header references fail">
    Header interpolation runs at activation time, so an unset variable only fails the server that needs it. Export the variable in the parent shell or add it to `~/.deepagents/.env`. To debug, set `DEEPAGENTS_CODE_DEBUG=1` and inspect the per-session log path printed to stderr on shutdown.
  </Accordion>
</AccordionGroup>

## Further reading

* [LangSmith Remote MCP](/langsmith/langsmith-remote-mcp): connect Deep Agents Code to LangSmith tools over OAuth
* [LangChain MCP guide](/oss/python/langchain/mcp): protocol details, building custom servers, and using `langchain-mcp-adapters` programmatically
* [MCP specification](https://modelcontextprotocol.io/): the official protocol spec and server registry

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/mcp-tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Memory and Skills
Source: https://docs.langchain.com/oss/python/deepagents/code/memory-and-skills

Persistent memory, AGENTS.md files, and reusable skills for Deep Agents Code, including creation, discovery, and invocation.

There are two primary ways to customize an agent in Deep Agents Code:

* **[Memory](#memory)**: `AGENTS.md` files and auto-saved memories that persist across sessions. Use memory for general coding style, preferences, and learned conventions.

* **[Skills](#skills)**: Reusable, on-demand capabilities that the agent discovers and reads only when relevant. Use skills for task-specific context such as workflows, best practices, and reference docs.

In practice, skills and memory sit on a spectrum. For more on when to use each, see [Skills, memory, and tools](/oss/python/deepagents/skills#skills-memory-and-tools).

Use `/remember` to explicitly prompt the agent to update its memory and skills from the current conversation.

<Tip>
  Building a custom agent with the SDK? See [Memory](/oss/python/deepagents/memory) for programmatic memory backends.
</Tip>

## Memory

### Automatic memory

As you use the agent, it automatically stores information in `~/.deepagents/<agent_name>/memories/` as markdown files using a memory-first protocol:

1. **Research**: Searches memory for relevant context before starting tasks
2. **Response**: Checks memory when uncertain during execution
3. **Learning**: Automatically saves new information for future sessions

The agent organizes its memories by topic with descriptive filenames:

```
~/.deepagents/backend-dev/memories/
├── api-conventions.md
├── database-schema.md
└── deployment-process.md
```

When you teach the agent conventions:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
dcode --agent backend-dev
> Our API uses snake_case and includes created_at/updated_at timestamps
```

It remembers for future sessions:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
> Create a /users endpoint

# Applies conventions without prompting
```

### AGENTS.md files

[`AGENTS.md` files](https://agents.md/) provide persistent context that is always loaded at session start:

* **Global**: `~/.deepagents/<agent_name>/AGENTS.md`—loaded every session.
* **Project**: `.deepagents/AGENTS.md` in any git project root—loaded when Deep Agents Code is run from within that project.

Both files are appended to the system prompt at startup.

### How memory works

The agent may also read its memory files when answering project-specific questions or when you reference past work or patterns.

The agent updates `AGENTS.md` as you provide information on how it should behave, feedback on its work, or instructions to remember something.
It also updates its memory if it identifies patterns or preferences from your interactions.

To add more structured project knowledge in additional memory files, add them in `.deepagents/` and reference them in the `AGENTS.md` file.
You must reference additional files in the `AGENTS.md` file for the agent to be aware of them.
The additional files are not read on startup but the agent can reference and update them when needed.

### When to use global vs. project AGENTS.md

Use a global `AGENTS.md` (`~/.deepagents/agent/AGENTS.md`) for:

* Your personality, style, and universal coding preferences
* General tone and communication style
* Universal coding preferences (formatting, type hints, etc.)
* Tool usage patterns that apply everywhere
* Workflows and methodologies that don't change per-project

Use a project `AGENTS.md` (`.deepagents/AGENTS.md` in project root) for:

* Project-specific context and conventions
* Project architecture and design patterns
* Coding conventions specific to this codebase
* Testing strategies and deployment processes
* Team guidelines and project structure

## Skills

Skills package domain expertise, such as workflows, best practices, scripts, and reference docs, into reusable directories that the agent discovers and reads only when relevant.
Deep agent skills follow the [Agent Skills specification](https://agentskills.io/). For more on how skills work and how to write effective ones, see [Skills](/oss/python/deepagents/skills).

At startup, Deep Agents Code reads the name and description from each `SKILL.md` file's frontmatter. When a task matches a skill's description, the agent reads the skill file and follows its instructions. Discovery runs again on `/reload`.

### Add a skill

<Steps>
  <Step title="Create a skill">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    # User skill (stored in ~/.deepagents/<agent_name>/skills/)
    dcode skills create test-skill

    # Project skill (stored in .deepagents/skills/)
    dcode skills create test-skill --project
    ```

    This generates:

    ```plaintext theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    skills/
    └── test-skill
        └── SKILL.md
    ```
  </Step>

  <Step title="Edit SKILL.md">
    Open the generated `SKILL.md` and edit the file to include your instructions.
  </Step>

  <Step title="Add optional resources">
    Optionally add additional scripts or other resources to the `test-skill` folder. For more information, see [Usage](/oss/python/deepagents/skills#add-supporting-resources).
  </Step>
</Steps>

You can also copy existing skills directly to the agent's folder:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
mkdir -p ~/.deepagents/<agent_name>/skills
cp -r examples/skills/web-research ~/.deepagents/<agent_name>/skills/
```

### Install community skills

You can use tools like Vercel's [Skills CLI](https://github.com/vercel-labs/skills) to install community [Agent Skills](https://agentskills.io/) in your environment and make them available to your deep agents:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Install a skill globally
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a deepagents -g -y

# List installed skills
npx skills ls -a deepagents -g
```

Global installs (`-g`) symlink skills into `~/.deepagents/agent/skills/`—the default agent's user-level skills directory. Project-level installs (omit `-g`) place skills in `.deepagents/skills/` relative to the current directory, making them available to any agent running in that project regardless of agent name.

<Note>
  Global installs target the default `agent` directory only. If you use a custom-named agent, either use project-level installs or manually symlink the skill into `~/.deepagents/{your-agent}/skills/`.
</Note>

### Skill discovery

Skills are loaded from the following directories at startup:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
~/.deepagents/<agent_name>/skills/
~/.agents/skills/
.deepagents/skills/
.agents/skills/
~/.claude/skills/          (experimental)
.claude/skills/            (experimental)
```

When duplicate skill names exist, later-precedence directories override earlier ones (see [App data](/oss/python/deepagents/code/data-locations#skills)).

For project-specific skills (under `.deepagents/skills/` or `.agents/skills/`), the project root is identified by a containing `.git` folder.

### Invoke a skill mid-session

Inside an interactive session, run a skill directly with the `/skill:<name>` slash command:

```text theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
/skill:code-review
/skill:code-review review the auth module
```

The skill's `SKILL.md` instructions are injected into the prompt along with any arguments you pass.

### Launch with a skill

The `--skill` flag invokes a skill immediately on launch, in either interactive (TUI) or non-interactive (headless) mode:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# Open the TUI and immediately run a skill
dcode --skill code-review

# Pass a request to the skill with -m
dcode --skill code-review -m 'review the auth module'

# Pipe content into a skill
cat diff.txt | dcode --skill code-review

# Pipe content and add a request
cat diff.txt | dcode --skill code-review -m 'focus on security'

# Run a skill headlessly
dcode --skill code-review -n 'review this patch'

# Quiet mode (only agent output on stdout)
dcode --skill code-review -n 'review this patch' -q
```

<Note>
  `--skill` with `--quiet` or `--no-stream` requires `-n` (non-interactive mode).
</Note>

### List skills

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}

# List all user skills
dcode skills list

# List project skills
dcode skills list --project

# Get detailed info about a specific skill
dcode skills info test-skill
dcode skills info test-skill --project
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/memory-and-skills.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
