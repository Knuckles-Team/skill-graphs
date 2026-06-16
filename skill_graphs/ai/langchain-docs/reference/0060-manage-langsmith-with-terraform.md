# Manage LangSmith with Terraform
Source: https://docs.langchain.com/langsmith/manage-with-terraform

Use the official LangSmith Terraform provider to manage workspaces, roles, members, evaluators, run rules, and alert rules as code.

The official [LangSmith Terraform provider](https://registry.terraform.io/providers/langchain-ai/langsmith/latest) lets you manage LangSmith organization and workspace resources as code—workspaces, custom roles, organization and workspace members, evaluators, run rules, and alert rules. It's the infrastructure-as-code counterpart to [managing your organization using the API](/langsmith/manage-organization-by-api).

<Check>
  Before diving in, it might be helpful to read:

  * [Conceptual guide on organizations and workspaces](/langsmith/administration-overview)
  * [Organization setup how-to](/langsmith/set-up-hierarchy#set-up-an-organization)
</Check>

## Install and configure

Add the provider to your Terraform configuration and pin a version:

```hcl theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
terraform {
  required_providers {
    langsmith = {
      source  = "langchain-ai/langsmith"
      version = "~> 0.0.2"
    }
  }
}

provider "langsmith" {
  # Cloud (US). Use https://eu.api.smith.langchain.com for the EU region,
  # or your self-hosted URL. Can also be set via LANGSMITH_ENDPOINT.
  api_url = "https://api.smith.langchain.com"

  # Optional: scope workspace-level resources to a specific workspace.
  workspace_id = "00000000-0000-0000-0000-000000000000"
}
```

Then run `terraform init` to download the provider.

## Authentication

The provider resolves credentials the same way as the LangSmith SDK and CLI. Prefer environment variables or a profile over hardcoding `api_key`:

* **Environment**—`LANGSMITH_API_KEY`, `LANGSMITH_ENDPOINT` (API URL), `LANGSMITH_WORKSPACE_ID`.
* **Profile**—set `profile` (or `LANGSMITH_PROFILE`) to use a LangSmith CLI profile.
* **Provider arguments**—`api_key`, `api_url`, `workspace_id`, `profile`.

Create an API key or [service key](/langsmith/administration-overview#service-keys) in your LangSmith settings. See [Authentication methods](/langsmith/authentication-methods) for the available key types.

<Warning>
  Organization-scoped operations—creating workspaces and inviting organization members—require an **organization-scoped service key with Organization Admin permissions**. Set `workspace_id` (or `LANGSMITH_WORKSPACE_ID`) to target workspace-scoped resources such as workspace memberships, evaluators, and run rules.
</Warning>

## Examples

### Create a workspace

```hcl theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
resource "langsmith_workspace" "demo" {
  display_name  = "Demo Workspace"
  tenant_handle = "demo-workspace"
}
```

### Manage roles and members

Look up built-in roles with data sources, then assign them. This invites a user to the organization and grants them admin on the workspace:

```hcl theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
data "langsmith_org_role" "user" {
  name = "ORGANIZATION_USER"
}

data "langsmith_workspace_role" "admin" {
  name = "WORKSPACE_ADMIN"
}

resource "langsmith_org_membership" "alice" {
  email   = "alice@example.com"
  role_id = data.langsmith_org_role.user.id
}

resource "langsmith_workspace_membership" "alice_demo" {
  workspace_id = langsmith_workspace.demo.id
  email        = langsmith_org_membership.alice.email
  role_id      = data.langsmith_workspace_role.admin.id
}
```

You can also define a custom workspace role, for example by cloning an existing role's permissions:

```hcl theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
resource "langsmith_workspace_role" "issues_agent" {
  display_name = "Issues Agent"
  description  = data.langsmith_workspace_role.admin.description
  permissions  = data.langsmith_workspace_role.admin.permissions
}
```

### Automate evaluators, run rules, and alerts

The provider manages more than accounts. You can codify [online code evaluators](/langsmith/online-evaluations-code), the [run rules](/langsmith/rules) that apply them, and [alerts](/langsmith/alerts) alongside your workspaces:

```hcl theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
resource "langsmith_evaluator" "tool_calls" {
  workspace_id = langsmith_workspace.demo.id
  name         = "tool call counts"
  type         = "code"

  code_evaluator = {
    language = "javascript"
    code     = file("${path.module}/evaluator.js")
  }
}

# A run rule applies the evaluator to matching runs in a tracing project.

# Run rules can also add runs to a dataset or annotation queue, or call webhooks.
resource "langsmith_run_rule" "score_root_runs" {
  workspace_id  = langsmith_workspace.demo.id
  display_name  = "score root runs"
  session_id    = "00000000-0000-0000-0000-000000000000" # tracing project ID
  sampling_rate = 1
  filter        = "eq(is_root, true)"

  evaluator_id = langsmith_evaluator.tool_calls.id
}

resource "langsmith_alert_rule" "error_rate" {
  session_id     = "00000000-0000-0000-0000-000000000000" # tracing project ID
  name           = "run error count high"
  type           = "threshold"
  attribute      = "error_count"
  aggregation    = "sum"
  window_minutes = 15
  operator       = "gte"
  threshold      = 10
  filter         = "eq(is_root, true)"

  actions = [{
    target  = "webhook"
    url_env = "LANGSMITH_ALERTS_WEBHOOK_URL"
    config_json = jsonencode({
      body = jsonencode({ text = "Error rate elevated" })
    })
  }]
}
```

## Resource reference

The full list of resources and data sources—with every argument and attribute—is published and kept in sync on the Terraform Registry:

<Card title="LangSmith provider on the Terraform Registry" icon="brand-terraform" href="https://registry.terraform.io/providers/langchain-ai/langsmith/latest/docs">
  Browse the complete reference for all resources and data sources.
</Card>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/manage-with-terraform.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Managed Deep Agents
Source: https://docs.langchain.com/langsmith/managed-deep-agents

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Managed Deep Agents API reference
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-api.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Managed Deep Agents API reference
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api-overview

Common REST commands and generated endpoint references for Managed Deep Agents.

The Managed Deep Agents API is a private preview API for creating, updating, connecting, and invoking [Managed Deep Agents](/langsmith/managed-deep-agents-overview). Use the [Managed Deep Agents SDKs](/langsmith/managed-deep-agents-sdk) for Python, TypeScript, and React applications. Use the REST API when you need direct control over request payloads. For the recommended end-to-end workflow, see the [quickstart](/langsmith/managed-deep-agents-quickstart).

<Note>
  Managed Deep Agents is in **private preview**, available on [LangSmith Cloud](/langsmith/cloud) in the US region only. [Join the waitlist](https://www.langchain.com/langsmith-managed-deep-agents-waitlist) to request access.
</Note>

## Set request defaults

The private preview API uses `/v1/deepagents`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
export LANGSMITH_API_KEY="<LANGSMITH_API_KEY>"
export LANGSMITH_API_URL="https://api.smith.langchain.com"
export DEEPAGENTS_BASE_URL="$LANGSMITH_API_URL/v1/deepagents"
```

Requests require the `X-Api-Key` header:

```txt theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
X-Api-Key: <LANGSMITH_API_KEY>
```

For example, list agents with the base URL and header set above:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl "$DEEPAGENTS_BASE_URL/agents" \
  -H "X-Api-Key: $LANGSMITH_API_KEY"
```

A missing `X-Api-Key` header returns `401` with `{"error": "Unauthorized"}`. A key that is invalid or lacks workspace access returns `403` with `{"error": "Forbidden"}`. These auth responses use a flat `{"error": "..."}` body, unlike the structured error body returned by other `4xx` responses.

## Understand resource groups

| Resource group | Purpose                                                                                      |
| -------------- | -------------------------------------------------------------------------------------------- |
| Agents         | Create and manage Managed Deep Agent resources, including runtime and backend configuration. |
| Threads        | Create and manage durable thread state for Managed Deep Agents.                              |
| Runs           | Start and stream Managed Deep Agent runs on threads.                                         |
| MCP servers    | Register MCP servers and store credentials referenced by agent tools.                        |
| MCP tools      | List tools exposed by a registered MCP server so clients can build `tools.json` entries.     |
| Auth sessions  | Start and poll user OAuth sessions for OAuth MCP servers.                                    |

Managed Deep Agents are not LangSmith Deployments. Creating a Managed Deep Agent creates a Managed Deep Agent resource, a separate LangSmith tracing project, and a Context Hub agent repo for the managed file tree.

## Configure sandboxes

Create-agent and update-agent payloads can include a `backend` object. Use `state` when the agent does not need sandbox-specific backend behavior:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "backend": {
    "type": "state"
  }
}
```

Use `sandbox` when the agent needs a [LangSmith sandbox](/langsmith/sandboxes) for code execution, filesystem work, or long-running tasks. Sandbox backend settings live under `backend.sandbox_config` and are valid only when `backend.type` is `sandbox`:

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

The `sandbox` object accepts:

| Field                       | Description                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------- |
| `scope`                     | Sandbox scope. Use `thread` for one sandbox per thread, or `agent` for one sandbox shared by the agent. |
| `policy_ids`                | Sandbox policy IDs to apply.                                                                            |
| `idle_ttl_seconds`          | Idle timeout before the sandbox stops, in seconds.                                                      |
| `delete_after_stop_seconds` | Delay before the sandbox is deleted after it stops, in seconds.                                         |

For backend guidance, see [Deploy an agent](/langsmith/managed-deep-agents-deploy#choose-a-backend). For standalone sandbox concepts, see the [LangSmith sandboxes overview](/langsmith/sandboxes).

## Use common REST commands

### Agents

See [Deploy an agent](/langsmith/managed-deep-agents-deploy#create-or-update-an-agent-with-the-sdk-or-api) for the create and update workflow. For deletion behavior, see [Limits and notes](/langsmith/managed-deep-agents-overview#delete-agents).

| Task               | Endpoint reference                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------- |
| Create an agent    | [`POST /v1/deepagents/agents`](/langsmith/managed-deep-agents-api/agents/create-agent)                        |
| List agents        | [`GET /v1/deepagents/agents`](/langsmith/managed-deep-agents-api/agents/list-agents)                          |
| Get an agent       | [`GET /v1/deepagents/agents/{agent_id}`](/langsmith/managed-deep-agents-api/agents/get-agent)                 |
| Update an agent    | [`PATCH /v1/deepagents/agents/{agent_id}`](/langsmith/managed-deep-agents-api/agents/update-agent)            |
| Delete an agent    | [`DELETE /v1/deepagents/agents/{agent_id}`](/langsmith/managed-deep-agents-api/agents/delete-agent)           |
| Clone an agent     | [`POST /v1/deepagents/agents/{agent_id}/clone`](/langsmith/managed-deep-agents-api/agents/clone-agent)        |
| Check agent health | [`GET /v1/deepagents/agents/{agent_id}/health`](/langsmith/managed-deep-agents-api/agents/check-agent-health) |

### Threads

See [Run an agent](/langsmith/managed-deep-agents-invoke#create-a-thread) for creating threads and managing the durable state they hold across runs.

| Task                | Endpoint reference                                                                                          |
| ------------------- | ----------------------------------------------------------------------------------------------------------- |
| List threads        | [`GET /v1/deepagents/threads`](/langsmith/managed-deep-agents-api/threads/list-threads)                     |
| Create a thread     | [`POST /v1/deepagents/threads`](/langsmith/managed-deep-agents-api/threads/create-thread)                   |
| Search threads      | [`POST /v1/deepagents/threads/search`](/langsmith/managed-deep-agents-api/threads/search-threads)           |
| Count threads       | [`GET /v1/deepagents/threads/count`](/langsmith/managed-deep-agents-api/threads/count-threads)              |
| Get a thread        | [`GET /v1/deepagents/threads/{thread_id}`](/langsmith/managed-deep-agents-api/threads/get-thread)           |
| Update a thread     | [`PATCH /v1/deepagents/threads/{thread_id}`](/langsmith/managed-deep-agents-api/threads/update-thread)      |
| Delete a thread     | [`DELETE /v1/deepagents/threads/{thread_id}`](/langsmith/managed-deep-agents-api/threads/delete-thread)     |
| Bulk update threads | [`POST /v1/deepagents/threads/bulk-modify`](/langsmith/managed-deep-agents-api/threads/bulk-update-threads) |

### Runs

See [Run an agent](/langsmith/managed-deep-agents-invoke#stream-a-run-from-a-thread) for starting runs on a thread and streaming their output.

| Task                    | Endpoint reference                                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Create a thread and run | [`POST /v1/deepagents/threads/runs`](/langsmith/managed-deep-agents-api/runs/create-thread-and-run)                      |
| Start a thread run      | [`POST /v1/deepagents/threads/{thread_id}/runs`](/langsmith/managed-deep-agents-api/runs/create-thread-run)              |
| Stream a thread run     | [`POST /v1/deepagents/threads/{thread_id}/runs/stream`](/langsmith/managed-deep-agents-api/runs/stream-thread-run)       |
| Resolve an interrupt    | [`POST /v1/deepagents/threads/{thread_id}/resolve-interrupt`](/langsmith/managed-deep-agents-api/runs/resolve-interrupt) |

### MCP servers

See [Connect tools](/langsmith/managed-deep-agents-mcp#connect-tools-with-the-sdk-or-api) for registering MCP servers and storing the credentials your agent tools use.

| Task                       | Endpoint reference                                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Create an MCP server       | [`POST /v1/deepagents/mcp-servers`](/langsmith/managed-deep-agents-api/mcp-servers/create-mcp-server)                                      |
| List MCP servers           | [`GET /v1/deepagents/mcp-servers`](/langsmith/managed-deep-agents-api/mcp-servers/list-mcp-servers)                                        |
| Get an MCP server          | [`GET /v1/deepagents/mcp-servers/{mcp_server_id}`](/langsmith/managed-deep-agents-api/mcp-servers/get-mcp-server)                          |
| Update an MCP server       | [`PATCH /v1/deepagents/mcp-servers/{mcp_server_id}`](/langsmith/managed-deep-agents-api/mcp-servers/update-mcp-server)                     |
| Delete an MCP server       | [`DELETE /v1/deepagents/mcp-servers/{mcp_server_id}`](/langsmith/managed-deep-agents-api/mcp-servers/delete-mcp-server)                    |
| Register an OAuth provider | [`POST /v1/deepagents/mcp-servers/{mcp_server_id}/oauth-provider`](/langsmith/managed-deep-agents-api/mcp-servers/register-oauth-provider) |

### MCP tools

See [Connect tools](/langsmith/managed-deep-agents-mcp#connect-tools-with-the-sdk-or-api) for listing the tools a registered server exposes and building `tools.json` entries.

| Task           | Endpoint reference                                                                            |
| -------------- | --------------------------------------------------------------------------------------------- |
| List MCP tools | [`GET /v1/deepagents/mcp/tools`](/langsmith/managed-deep-agents-api/mcp-tools/list-mcp-tools) |

### Auth sessions

See [Connect tools](/langsmith/managed-deep-agents-mcp#connect-tools-with-the-sdk-or-api) for running the OAuth flow that authorizes MCP servers.

| Task                  | Endpoint reference                                                                                                   |
| --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Start an auth session | [`POST /v1/deepagents/auth-sessions`](/langsmith/managed-deep-agents-api/auth-sessions/start-auth-session)           |
| Get an auth session   | [`GET /v1/deepagents/auth-sessions/{session_id}`](/langsmith/managed-deep-agents-api/auth-sessions/get-auth-session) |

## Paginate the agents list

[`GET /v1/deepagents/agents`](/langsmith/managed-deep-agents-api/agents/list-agents) is cursor-paginated. Pass `page_size` (defaults to `20`, maximum `100`) and the opaque `cursor` returned by a previous request. The response wraps results in an `items` array alongside a `next_cursor` field that is `null` on the last page:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "items": [],
  "next_cursor": null
}
```

The endpoint also accepts `name` to filter by name substring, `sort_by` (`created_at`, `updated_at`, or `name`, defaults to `updated_at`), and `sort_order` (`asc` or `desc`, defaults to `desc`).

## Understand API stability

Routes are versioned at `/v1/`, but the surface is in private preview and may change in backwards-incompatible ways before general availability. See [API stability](/langsmith/managed-deep-agents-overview#api-stability) for breaking-change communication.

The API does not mirror every LangSmith Deployment endpoint in private preview. Endpoint groups such as integrations, triggers, skills, sandboxes, auth providers, and auth tokens are not mirrored yet.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-api-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Check agent health
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/check-agent-health

/langsmith/managed-deep-agents-openapi.json get /agents/{agent_id}/health
Return a per-MCP-server health summary for the agent.

# Clone an agent
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/clone-agent

/langsmith/managed-deep-agents-openapi.json post /agents/{agent_id}/clone
Create a new agent that mirrors the source agent behavior but is owned by the caller. The clone copies runtime, backend, file tree, tools, subagents, and skills; caller metadata and sharing state start fresh.

# Create an agent
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/create-agent

/langsmith/managed-deep-agents-openapi.json post /agents
Create an agent with metadata, runtime configuration, and an optional file tree. Creation is atomic: either the agent is fully created or no state is persisted.

# Delete an agent
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/delete-agent

/langsmith/managed-deep-agents-openapi.json delete /agents/{agent_id}
Delete the agent. The call is idempotent: deleting a non-existent agent returns `204`. Deletion does not cascade to the agent's threads — existing threads remain queryable but cannot start new runs (attempts return `502`). Delete threads explicitly when you want to clean them up.

# Get an agent
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/get-agent

/langsmith/managed-deep-agents-openapi.json get /agents/{agent_id}
Return the specified agent, including metadata, permissions, runtime, extras, and the parsed file tree at the latest commit. Pass `include_files=true` to include the raw file map.

# List agents
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/list-agents

/langsmith/managed-deep-agents-openapi.json get /agents
Return Managed Deep Agents owned by the authenticated user. System-created default agents are excluded.

# Update an agent
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/agents/update-agent

/langsmith/managed-deep-agents-openapi.json patch /agents/{agent_id}
Update the specified agent. Top-level scalar fields merge field-by-field. Nested objects such as `runtime`, `permissions`, `tools`, `subagents`, `skills`, and `extras` are replaced in full when provided. Providing file-tree fields such as `instructions`, `tools`, `subagents`, `skills`, or `files` creates a new file tree commit.

# Get an authorization session
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/auth-sessions/get-auth-session

/langsmith/managed-deep-agents-openapi.json get /auth-sessions/{session_id}
Return the current status of an in-flight authorization session. Use `wait_seconds` to long-poll until the session completes or the wait window expires.

# Start an authorization session
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/auth-sessions/start-auth-session

/langsmith/managed-deep-agents-openapi.json post /auth-sessions
Start an OAuth authorization session for the caller. If the user is already authorized, the response can be completed immediately. Otherwise, the response includes a verification URL that the user must visit to complete authorization.

# Register an MCP server
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/create-mcp-server

/langsmith/managed-deep-agents-openapi.json post /mcp-servers
Register an MCP server in the caller's workspace. Static-header servers can include credential headers. OAuth servers should set `auth_type=oauth` and `oauth_mode=per_user_dynamic_client`, then register an OAuth provider and start an auth session before use.

# Delete an MCP server
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/delete-mcp-server

/langsmith/managed-deep-agents-openapi.json delete /mcp-servers/{mcp_server_id}
Delete an MCP server. The call is idempotent: deleting a non-existent server returns `204`. After deletion, agents whose tools reference this server's URL will no longer have the stored headers attached at invocation time.

# Get an MCP server
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/get-mcp-server

/langsmith/managed-deep-agents-openapi.json get /mcp-servers/{mcp_server_id}
Fetch a single MCP server by ID.

# List MCP servers
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/list-mcp-servers

/langsmith/managed-deep-agents-openapi.json get /mcp-servers
List MCP servers registered in the caller's workspace.

# Register per-user MCP OAuth provider
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/register-oauth-provider

/langsmith/managed-deep-agents-openapi.json post /mcp-servers/{mcp_server_id}/oauth-provider
Discovers and registers an OAuth provider for the authenticated user against a Deep Agents MCP server configured with per-user dynamic client mode. Idempotent when a mapping already exists.

# Update an MCP server
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-servers/update-mcp-server

/langsmith/managed-deep-agents-openapi.json patch /mcp-servers/{mcp_server_id}
Update an MCP server's URL, credential headers, or auth configuration. Passing `headers` replaces the entire stored header array — partial diffs are not supported. Use this endpoint to rotate credentials.

# List MCP tools
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/mcp-tools/list-mcp-tools

/langsmith/managed-deep-agents-openapi.json get /mcp/tools
Return tools exposed by a registered MCP server. The API serves cached results when fresh; otherwise, it fetches tools from the remote MCP server and caches the response.

# Create a thread and start a run
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/runs/create-thread-and-run

/langsmith/managed-deep-agents-openapi.json post /threads/runs
Create a thread bound to `agent_id` and start a run on it in one call. Run kwargs are passed through; thread-creation flags go in the optional `thread` envelope.

# Create a thread run
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/runs/create-thread-run

/langsmith/managed-deep-agents-openapi.json post /threads/{thread_id}/runs
Start a run on the thread. This endpoint is proxied to the upstream agent runtime and accepts its run payload. Include the assistant or agent identifier and run inputs in the request body.

# Resolve an interrupt
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/runs/resolve-interrupt

/langsmith/managed-deep-agents-openapi.json post /threads/{thread_id}/resolve-interrupt
Complete a human-interrupt pause on the thread without sending new input, allowing execution to continue or finish. On success the response has no body.

# Stream a thread run
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/runs/stream-thread-run

/langsmith/managed-deep-agents-openapi.json post /threads/{thread_id}/runs/stream
Start a run on a thread and stream output as server-sent events. The request must use `agent_id`; `assistant_id` is reserved for server-side forwarding and is rejected.

# Bulk update threads
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/bulk-update-threads

/langsmith/managed-deep-agents-openapi.json post /threads/bulk-modify
Apply one thread update payload to multiple threads. Returns one result per thread in request order.

# Count threads
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/count-threads

/langsmith/managed-deep-agents-openapi.json get /threads/count
Return the caller inbox `attention_count`: unread idle threads plus interrupted and errored threads. Scoped to deep-agent threads; test-run threads are excluded.

# Create a thread
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/create-thread

/langsmith/managed-deep-agents-openapi.json post /threads
Create a thread bound to a Managed Deep Agent. Use the returned thread ID to start runs.

# Delete thread
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/delete-thread

/langsmith/managed-deep-agents-openapi.json delete /threads/{thread_id}
Delete a thread and all of its runs. Idempotent: deleting a missing thread returns 204.

# Get thread
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/get-thread

/langsmith/managed-deep-agents-openapi.json get /threads/{thread_id}
Return thread metadata and status for the given thread ID.

# List threads
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/list-threads

/langsmith/managed-deep-agents-openapi.json get /threads
Return one page of recent threads for a Managed Deep Agent. Results are ordered by latest conversation activity.

# Search threads
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/search-threads

/langsmith/managed-deep-agents-openapi.json post /threads/search
Search threads. Request and response bodies are proxied unchanged to the upstream agent runtime.

# Update thread
Source: https://docs.langchain.com/langsmith/managed-deep-agents-api/threads/update-thread

/langsmith/managed-deep-agents-openapi.json patch /threads/{thread_id}
Update thread fields such as title and metadata. Omitted fields are unchanged.
