# Create Connection
Source: https://docs.langchain.com/api-reference/agent-connections-v2/create-connection

https://api.host.langchain.com/openapi.json post /v2/auth/agents/{agent_id}/connections

# List Connections
Source: https://docs.langchain.com/api-reference/agent-connections-v2/list-connections

https://api.host.langchain.com/openapi.json get /v2/auth/agents/{agent_id}/connections

# Remove Connection
Source: https://docs.langchain.com/api-reference/agent-connections-v2/remove-connection

https://api.host.langchain.com/openapi.json delete /v2/auth/agents/{agent_id}/connections/{connection_id}

# Authenticate
Source: https://docs.langchain.com/api-reference/auth-service-v2/authenticate

https://api.host.langchain.com/openapi.json post /v2/auth/authenticate
Get OAuth token or start authentication flow if needed.

# Check Oauth Token Exists
Source: https://docs.langchain.com/api-reference/auth-service-v2/check-oauth-token-exists

https://api.host.langchain.com/openapi.json get /v2/auth/tokens/exists
Return whether the current user has any tokens for a given provider (across agents).

# Check Workspace Slack Tokens Exist
Source: https://docs.langchain.com/api-reference/auth-service-v2/check-workspace-slack-tokens-exist

https://api.host.langchain.com/openapi.json get /v2/auth/tokens/workspace/slack/exists
Check if the workspace has any Slack tokens.

# Create Mcp Oauth Provider
Source: https://docs.langchain.com/api-reference/auth-service-v2/create-mcp-oauth-provider

https://api.host.langchain.com/openapi.json post /v2/auth/providers/mcp-discover
Create an OAuth provider via MCP auto-discovery.

# Create Oauth Provider
Source: https://docs.langchain.com/api-reference/auth-service-v2/create-oauth-provider

https://api.host.langchain.com/openapi.json post /v2/auth/providers
Create a new OAuth provider manually.

# Delete Oauth Provider
Source: https://docs.langchain.com/api-reference/auth-service-v2/delete-oauth-provider

https://api.host.langchain.com/openapi.json delete /v2/auth/providers/{provider_id}
Delete an OAuth provider.

# Delete Oauth Tokens For User
Source: https://docs.langchain.com/api-reference/auth-service-v2/delete-oauth-tokens-for-user

https://api.host.langchain.com/openapi.json delete /v2/auth/tokens
Delete all tokens for the current user for the given provider (across agents).

# Delete Single Oauth Token
Source: https://docs.langchain.com/api-reference/auth-service-v2/delete-single-oauth-token

https://api.host.langchain.com/openapi.json delete /v2/auth/tokens/{token_id}
Delete a specific OAuth token, revoking it at the provider first.

Only the token owner can delete it.

# Get Oauth Provider
Source: https://docs.langchain.com/api-reference/auth-service-v2/get-oauth-provider

https://api.host.langchain.com/openapi.json get /v2/auth/providers/{provider_id}
Get a specific OAuth provider.

# List Oauth Providers
Source: https://docs.langchain.com/api-reference/auth-service-v2/list-oauth-providers

https://api.host.langchain.com/openapi.json get /v2/auth/providers
List OAuth providers.

# List Oauth Tokens For User
Source: https://docs.langchain.com/api-reference/auth-service-v2/list-oauth-tokens-for-user

https://api.host.langchain.com/openapi.json get /v2/auth/tokens
List the calling user's tokens for a provider.

# Oauth Callback
Source: https://docs.langchain.com/api-reference/auth-service-v2/oauth-callback

https://api.host.langchain.com/openapi.json post /v2/auth/callback/{provider_id}

# Oauth Callback Get
Source: https://docs.langchain.com/api-reference/auth-service-v2/oauth-callback-get

https://api.host.langchain.com/openapi.json get /v2/auth/callback/{provider_id}
Handle OAuth callback redirect from OAuth providers.

Processes the OAuth token exchange, then redirects to the frontend callback
page for a consistent UI experience.

# Oauth Setup Callback
Source: https://docs.langchain.com/api-reference/auth-service-v2/oauth-setup-callback

https://api.host.langchain.com/openapi.json get /v2/auth/setup/{provider_id}
Handle OAuth setup callback redirect from GitHub Apps.

This endpoint handles the "Setup URL" callback from GitHub Apps, which is
triggered when a user installs or updates their GitHub App installation.

For "update" actions (user modified repo access via GitHub), we just show
a success page since no token exchange is needed.

For new installations with code/state, we process similar to the regular
OAuth callback.

# Revoke All Slack Tokens For Workspace
Source: https://docs.langchain.com/api-reference/auth-service-v2/revoke-all-slack-tokens-for-workspace

https://api.host.langchain.com/openapi.json delete /v2/auth/tokens/workspace/slack
Revoke ALL Slack tokens for the workspace. Admin-only action that disconnects Slack entirely.

This is a destructive operation that:
- Revokes all Slack tokens on Slack's side for all users in the workspace
- Deletes all Slack tokens from the database

# Update Oauth Provider
Source: https://docs.langchain.com/api-reference/auth-service-v2/update-oauth-provider

https://api.host.langchain.com/openapi.json patch /v2/auth/providers/{provider_id}
Update an OAuth provider.

# Update Token Label
Source: https://docs.langchain.com/api-reference/auth-service-v2/update-token-label

https://api.host.langchain.com/openapi.json patch /v2/auth/tokens/{token_id}/metadata
Update a token's provider_account_label. Only the token owner can update.

# Wait For Auth Completion
Source: https://docs.langchain.com/api-reference/auth-service-v2/wait-for-auth-completion

https://api.host.langchain.com/openapi.json get /v2/auth/wait/{auth_id}
Wait for OAuth authentication completion.

# Create Deployment
Source: https://docs.langchain.com/api-reference/deployments-v2/create-deployment

https://api.host.langchain.com/openapi.json post /v2/deployments
Create a new deployment.

# Delete Deployment
Source: https://docs.langchain.com/api-reference/deployments-v2/delete-deployment

https://api.host.langchain.com/openapi.json delete /v2/deployments/{deployment_id}
Delete a deployment by ID.

# Delete Deployments
Source: https://docs.langchain.com/api-reference/deployments-v2/delete-deployments

https://api.host.langchain.com/openapi.json delete /v2/deployments
Delete multiple deployments with partial success support.

Returns:
    - 200: All deployments deleted successfully
    - 207: Some deployments deleted successfully, some failed

# Get Deployment
Source: https://docs.langchain.com/api-reference/deployments-v2/get-deployment

https://api.host.langchain.com/openapi.json get /v2/deployments/{deployment_id}
Get a deployment by ID.

# Get Revision
Source: https://docs.langchain.com/api-reference/deployments-v2/get-revision

https://api.host.langchain.com/openapi.json get /v2/deployments/{deployment_id}/revisions/{revision_id}
Get a revision by ID for a deployment.

# List Deployments
Source: https://docs.langchain.com/api-reference/deployments-v2/list-deployments

https://api.host.langchain.com/openapi.json get /v2/deployments
List all deployments.

# List Revisions
Source: https://docs.langchain.com/api-reference/deployments-v2/list-revisions

https://api.host.langchain.com/openapi.json get /v2/deployments/{deployment_id}/revisions
List all revisions for a deployment.

# Patch Deployment
Source: https://docs.langchain.com/api-reference/deployments-v2/patch-deployment

https://api.host.langchain.com/openapi.json patch /v2/deployments/{deployment_id}
Patch a deployment by ID.

# Redeploy Revision
Source: https://docs.langchain.com/api-reference/deployments-v2/redeploy-revision

https://api.host.langchain.com/openapi.json post /v2/deployments/{deployment_id}/revisions/{revision_id}/redeploy
Redeploy a specific revision ID.

# List Forge GitHub Integrations
Source: https://docs.langchain.com/api-reference/integrations-v1/list-forge-github-integrations

https://api.host.langchain.com/openapi.json get /v1/integrations/forge/github/install
List available Forge GitHub integrations.

# List Forge GitHub Repositories
Source: https://docs.langchain.com/api-reference/integrations-v1/list-forge-github-repositories

https://api.host.langchain.com/openapi.json get /v1/integrations/forge/github/{integration_id}/repos
List available GitHub repositories for a Forge integration.

# List GitHub Integrations
Source: https://docs.langchain.com/api-reference/integrations-v1/list-github-integrations

https://api.host.langchain.com/openapi.json get /v1/integrations/github/install
List available GitHub integrations for LangGraph Platfom Cloud SaaS.

# List GitHub Repositories
Source: https://docs.langchain.com/api-reference/integrations-v1/list-github-repositories

https://api.host.langchain.com/openapi.json get /v1/integrations/github/{integration_id}/repos
List available GitHub repositories for an integration that are available to deploy to LangSmith Deployment.

# Create Listener
Source: https://docs.langchain.com/api-reference/listeners-v2/create-listener

https://api.host.langchain.com/openapi.json post /v2/listeners
Create a listener.<br>
<br>
Creating a listener is only allowed for LangSmith organizations with self-hosted enterprise plans.

# Delete Listener
Source: https://docs.langchain.com/api-reference/listeners-v2/delete-listener

https://api.host.langchain.com/openapi.json delete /v2/listeners/{listener_id}
Delete a listener by ID.

# Get Listener
Source: https://docs.langchain.com/api-reference/listeners-v2/get-listener

https://api.host.langchain.com/openapi.json get /v2/listeners/{listener_id}
Get a listener by ID.

# List Listeners
Source: https://docs.langchain.com/api-reference/listeners-v2/list-listeners

https://api.host.langchain.com/openapi.json get /v2/listeners
List all listeners.

# Patch Listener
Source: https://docs.langchain.com/api-reference/listeners-v2/patch-listener

https://api.host.langchain.com/openapi.json patch /v2/listeners/{listener_id}
Patch a listener by ID.

#
Source: https://docs.langchain.com/index

<div>
  <div>
    <h1>The platform for agent engineering</h1>

    One platform to improve every step of the agent development lifecycle, so you can ship reliable agents faster.
    <h2>Get started</h2>

    <CardGroup>
      <Card title="Build" icon="hammer" href="/oss/python/build-overview">
        Build agents with code using LangChain, LangGraph, and Deep Agents.
      </Card>

      <Card title="Test" icon="flask" href="/langsmith/test-overview">
        Evaluate agents with datasets, evaluations, and prompt engineering.
      </Card>

      <Card title="Deploy" icon="rocket" href="/langsmith/deployment">
        Deploy and serve agents at scale.
      </Card>

      <Card title="Monitor" icon="chart-line" href="/langsmith/observability">
        Trace, debug, and observe agents in production.
      </Card>

      <Card title="Govern" icon="shield-check" href="/langsmith/admin">
        Administer access, settings, and governance.
      </Card>

      <Card title="No-code agents" icon="wand" href="/langsmith/fleet">
        Build and run agents without code using LangSmith Fleet.
      </Card>
    </CardGroup>

    <Card title="Find and fix failures with Engine" icon="https://mintcdn.com/langchain-5e9cc07a/auWE6_dMRp183OCf/images/brand/engine-icon-no-bg-dark.svg?fit=max&auto=format&n=auWE6_dMRp183OCf&q=85&s=dd41aef3ce789c1a04ea3c37b5903eac" href="/langsmith/engine-overview">
      Find and fix recurring agent failures automatically with LangSmith Engine.
    </Card>

    <h2>Resources</h2>

    <CardGroup>
      <Card title="LangChain Academy" icon="school" href="https://academy.langchain.com/">
        Take free courses on building with LangChain and LangGraph.
      </Card>

      <Card title="Community forum" icon="messages" href="https://forum.langchain.com/">
        Ask questions, share solutions, and discuss best practices.
      </Card>

      <Card title="Support portal" icon="message-circle-question" href="https://support.langchain.com/">
        Submit tickets and track support requests.
      </Card>

      <Card title="Sign up for LangSmith" icon="tools" href="https://smith.langchain.com/">
        Start with LangSmith for free.
      </Card>

      <Card title="LangSmith status" icon="activity-heartbeat" href="https://status.smith.langchain.com/">
        Real-time status of LangSmith services and APIs.
      </Card>

      <Card title="Trust Center" icon="shield-lock" href="https://trust.langchain.com/">
        HIPAA, SOC 2 Type 2, and GDPR compliance details.
      </Card>
    </CardGroup>
  </div>
</div>

# Attribute-based access control
Source: https://docs.langchain.com/langsmith/abac

This reference explains LangSmith's Attribute-Based Access Control (ABAC) system, which enables fine-grained access control based on resource attributes, complementing [RBAC](/langsmith/rbac). For automated user provisioning into roles, see [SCIM](/langsmith/user-management#set-up-scim-for-your-organization).

<Note>
  ABAC (Attribute-Based Access Control) is an Enterprise feature for managing fine-grained access control. If you are interested in this feature, [contact our sales team](https://www.langchain.com/contact-sales). Other plans default to using the Admin role for all users.
</Note>

ABAC complements [Role-Based Access Control (RBAC)](/langsmith/rbac) by adding tag-based conditions to access decisions. While RBAC grants blanket permissions based on a user's role (e.g., "can read all projects"), ABAC lets you restrict or grant access based on resource tags (e.g., "can only read projects tagged with Environment=Development").

<Note>
  Roles and resource tags can be managed via the UI or API. ABAC policies are configurable via the [API](https://api.smith.langchain.com/docs#/access_policies). Once configured, policies are automatically enforced in both the API and the UI.
</Note>

## Before you begin

* [Set up resource tags](/langsmith/set-up-resource-tags) in your workspace.
* ABAC currently only supports `resource_tag_key` as an `attribute_name` in policies, for evaluating against resource tags. No other attributes are supported yet.

## Enable ABAC for self-hosted deployments

1. ABAC requires a [self-hosted](/langsmith/self-hosted) LangSmith deployment running Helm chart 0.11.28 or later (application version 0.12.1). Once you've upgraded, use one of the following options to enable ABAC:

   * **Enable for a specific organization:** Run the following against your LangSmith PostgreSQL database, replacing `<organization_id>` with the ID copied from the organization settings page in the UI:

     ```sql theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     UPDATE organizations SET config = config || '{"can_use_abac": true}' WHERE id = '<organization_id>' AND NOT is_personal;
     ```

   * **Enable for all organizations:** Add the following environment variable to `commonEnv` in your `values.yaml`:

     ```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
     DEFAULT_ORG_FEATURE_CAN_USE_ABAC: "true"
     ```

     <Note>
       This environment variable has no effect on personal organizations, because [RBAC](/langsmith/rbac) is not enabled for personal organizations.
     </Note>

2. Set up authentication. To manage access policies via the API, you need a Personal Access Token (PAT) from an [Organization Admin](/langsmith/rbac#organization-admin) user, or an organization-scoped service key with Organization Admin permissions. Set the following environment variables before running any scripts:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   export LANGSMITH_API_KEY="your_admin_api_key"
   # Required for self-hosted or regional SaaS deployments:
   # export LANGCHAIN_ENDPOINT="https://eu.api.smith.langchain.com"
   # export LANGCHAIN_ENDPOINT="https://aws.api.smith.langchain.com"
   # export LANGCHAIN_ENDPOINT="https://apac.api.smith.langchain.com"
   # export LANGCHAIN_ENDPOINT="https://langsmith.yourdomain.com/api"
   ```

## Access policy structure

An access policy defines conditions under which access is granted or denied. Here's the structure:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "Policy Name",
  "description": "Optional description",
  "effect": "allow | deny",
  "condition_groups": [
    {
      "permission": "projects:read",
      "resource_type": "project",
      "conditions": [
        {
          "attribute_name": "resource_tag_key",
          "attribute_key": "Environment",
          "operator": "equals",
          "attribute_value": "Production"
        }
      ]
    }
  ],
  "role_ids": ["<role-uuid>"]
}
```

### Effect

The `effect` determines what happens when conditions match:

* **`allow`** - Grant access when conditions match
* **`deny`** - Block access when conditions match

<Note>
  Deny policies always take precedence. If both an allow and deny policy match, access is denied.
</Note>

### Condition groups

The `condition_groups` array contains one or more condition groups. Multiple condition groups are evaluated with **OR logic** - if any group matches, the policy applies.

Each condition group specifies:

* **`permission`** - The permission this group applies to
* **`resource_type`** - The resource type to match
* **`conditions`** - Array of conditions (evaluated with **AND logic** within the group)

#### Resource types and permissions

| Resource type       | Supported permissions                                                                                                                                                             |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `project`           | `projects:read`, `projects:update`, `projects:delete`, `runs:read`, `runs:share`, `runs:delete`, `projects:increase-trace-tier`, `projects:decrease-trace-tier`                   |
| `prompt`            | `prompts:read`, `prompts:update`, `prompts:delete`, `prompts:share`, `prompts:tag`                                                                                                |
| `dataset`           | `datasets:read`, `datasets:update`, `datasets:delete`, `datasets:share`                                                                                                           |
| `deployment`        | `deployments:read`, `deployments:update`, `deployments:delete`                                                                                                                    |
| `mcp_server`        | `mcp-servers:read`, `mcp-servers:invoke`, `mcp-servers:update`, `mcp-servers:delete`. See [Fleet tool access control](/langsmith/fleet/access-and-oversight#tool-access-control). |
| `fleet_integration` | `mcp-servers:read`, `mcp-servers:invoke`. See [Fleet tool access control](/langsmith/fleet/access-and-oversight#tool-access-control).                                             |

<Note>
  Runs don't have their own tags. Run permissions (`runs:read`, `runs:create`, `runs:share`, `runs:delete`) are evaluated against the parent project's tags.
</Note>

#### Conditions

Each condition in the `conditions` array specifies:

* **`attribute_name`** - Currently only `resource_tag_key` is supported
* **`attribute_key`** - The tag key to match (e.g., `Environment`, `Team`)
* **`operator`** - The comparison operator
* **`attribute_value`** - The value to compare against

##### Operators

| Operator                 | Description                                      |
| ------------------------ | ------------------------------------------------ |
| `equals`                 | Exact match (case sensitive)                     |
| `not_equals`             | Values differ (case sensitive)                   |
| `equals_ignore_case`     | Exact match (case insensitive)                   |
| `not_equals_ignore_case` | Values differ (case insensitive)                 |
| `matches`                | Glob pattern matching with `*` and `?` wildcards |
| `not_matches`            | Match when value doesn't match glob pattern      |

##### `_if_exists` variants

Each operator has an `_if_exists` variant that matches by default when the tag key is absent, or evaluates the condition normally when the tag exists:

| Operator                           | Description                                                       |
| ---------------------------------- | ----------------------------------------------------------------- |
| `equals_if_exists`                 | Exact match (case sensitive), or if tag key absent                |
| `not_equals_if_exists`             | Values differ (case sensitive), or if tag key absent              |
| `equals_ignore_case_if_exists`     | Exact match (case insensitive), or if tag key absent              |
| `not_equals_ignore_case_if_exists` | Values differ (case insensitive), or if tag key absent            |
| `matches_if_exists`                | Glob pattern match, or if tag key absent                          |
| `not_matches_if_exists`            | Match when value doesn't match glob pattern, or if tag key absent |

<Tip>
  In an **allow** policy, `_if_exists` variants grant access to resources that either match the condition or don't have the specified tag key. In a **deny** policy, they block resources that either match the condition or don't have the tag key.
</Tip>

### Roles

The `role_ids` array specifies which workspace roles the policy applies to. When a user with that role accesses a resource, the policy conditions are evaluated.

Policies can be attached to roles when creating the policy, or attached later via the API.

## Managing access policies

Access policies are managed via the LangSmith API by [Organization Admins](/langsmith/rbac#organization-admin). Before creating policies, [set up resource tags](/langsmith/set-up-resource-tags) in your workspace.

## How ABAC works with RBAC

[RBAC](/langsmith/rbac) permissions and ABAC policies are both considered when determining access to resources:

* ABAC **deny** policies override RBAC permissions
* ABAC **allow** policies can grant access even without RBAC permissions
* If no ABAC policies match, the system falls back to RBAC

### Policy evaluation outcomes

**Feature combinations:**

| RBAC enabled | ABAC enabled | Behavior                                            |
| ------------ | ------------ | --------------------------------------------------- |
| ✗            | ✗            | All workspace members have Admin-level access       |
| ✓            | ✗            | Standard RBAC - access based on role permissions    |
| ✓            | ✓            | RBAC + ABAC - fine-grained tag-based access control |

**When both RBAC and ABAC are enabled:**

| RBAC permits | Allow policy matches | Deny policy matches | Result                           |
| ------------ | -------------------- | ------------------- | -------------------------------- |
| ✓            | ✓                    | ✗                   | **Allowed**                      |
| ✓            | ✗                    | ✗                   | **Allowed** (RBAC fallback)      |
| ✓            | ✓                    | ✓                   | **Denied** (deny wins)           |
| ✓            | ✗                    | ✓                   | **Denied** (deny wins)           |
| ✗            | ✓                    | ✗                   | **Allowed** (ABAC grants access) |
| ✗            | ✗                    | ✗                   | **Denied**                       |
| ✗            | ✓                    | ✓                   | **Denied** (deny wins)           |

## Example scenarios

### 1. Annotator team assignment

Allow annotators to only access datasets tagged for their team:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "Annotator Team A Access",
  "effect": "allow",
  "condition_groups": [{
    "permission": "datasets:read",
    "resource_type": "dataset",
    "conditions": [{
      "attribute_name": "resource_tag_key",
      "attribute_key": "Annotation-Team",
      "operator": "equals",
      "attribute_value": "Team-A"
    }]
  }]
}
```

### 2. Block sensitive data

Deny access to datasets containing PII. Since deny policies override allow policies, this blocks access even for users with RBAC permissions:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "Block PII Datasets",
  "effect": "deny",
  "condition_groups": [{
    "permission": "datasets:read",
    "resource_type": "dataset",
    "conditions": [{
      "attribute_name": "resource_tag_key",
      "attribute_key": "Contains-PII",
      "operator": "equals",
      "attribute_value": "true"
    }]
  }]
}
```

### 3. Application-based access with wildcards

Allow engineers to access projects for any application in the "chatbot" family using glob patterns:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "Chatbot Apps Access",
  "effect": "allow",
  "condition_groups": [{
    "permission": "projects:read",
    "resource_type": "project",
    "conditions": [{
      "attribute_name": "resource_tag_key",
      "attribute_key": "Application",
      "operator": "matches",
      "attribute_value": "chatbot-*"
    }]
  }]
}
```

### 4. Client and purpose isolation (AND logic)

Grant access only if both conditions are met - dataset is for training AND belongs to a specific client:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "Client Training Data Access",
  "effect": "allow",
  "condition_groups": [{
    "permission": "datasets:read",
    "resource_type": "dataset",
    "conditions": [
      {
        "attribute_name": "resource_tag_key",
        "attribute_key": "Purpose",
        "operator": "equals",
        "attribute_value": "Training"
      },
      {
        "attribute_name": "resource_tag_key",
        "attribute_key": "Client",
        "operator": "equals",
        "attribute_value": "Acme-Corp"
      }
    ]
  }]
}
```

### 5. Client data plus resources without a `Client` tag using `_if_exists`

Consultants don't have RBAC `datasets:read` permission, but this policy grants them access to datasets tagged `Client=Acme-Corp`, as well as datasets that don't have a `Client` tag at all. Datasets tagged with a different client (e.g., `Client=Other-Corp`) remain blocked:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "name": "Acme Consultant Access",
  "effect": "allow",
  "condition_groups": [{
    "permission": "datasets:read",
    "resource_type": "dataset",
    "conditions": [{
      "attribute_name": "resource_tag_key",
      "attribute_key": "Client",
      "operator": "equals_if_exists",
      "attribute_value": "Acme-Corp"
    }]
  }]
}
```

## Troubleshooting

**Access unexpectedly denied?**

* Check if a deny policy is matching (deny always takes precedence)
* Check if the user has RBAC permissions or a matching allow policy
* Verify the resource has the expected tag and value
* Deny policies with `_if_exists` operators block resources missing that tag key
* For case-sensitive operators (`equals`, `not_equals`), check for case mismatches
* With multiple conditions in a group, all must match (AND logic)

**Access unexpectedly granted?**

* Review RBAC permissions (users may have access via their role)
* Check if an allow policy is too broad (e.g., using wildcards)
* `_if_exists` operators match resources missing that tag key

**Policy not taking effect?**

* Confirm the policy is attached to the correct role
* Verify the user has that role in the workspace
* Check that `resource_type` and `permission` match the resource being accessed

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/abac.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Access the current run (span) within a traced function
Source: https://docs.langchain.com/langsmith/access-current-span

In some cases you will want to access the current run (span) within a traced function. This can be useful for extracting UUIDs, tags, or other information from the current run.

You can access the current run by calling the `get_current_run_tree`/`getCurrentRunTree` function in the Python or TypeScript SDK, respectively.

For a full list of available properties on the `RunTree` object, see [this reference](/langsmith/run-data-format).

<CodeGroup>
  ```python Python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  from langsmith import traceable
  from langsmith.run_helpers import get_current_run_tree
  from openai import Client

      openai = Client()

      @traceable
      def format_prompt(subject):
          run = get_current_run_tree()
          print(f"format_prompt Run Id: {run.id}")
          print(f"format_prompt Trace Id: {run.trace_id}")
          print(f"format_prompt Parent Run Id: {run.parent_run.id}")
          return [
              {
                  "role": "system",
                  "content": "You are a helpful assistant.",
              },
              {
                  "role": "user",
                  "content": f"What's a good name for a store that sells {subject}?"
              }
          ]

      @traceable(run_type="llm")
      def invoke_llm(messages):
          run = get_current_run_tree()
          print(f"invoke_llm Run Id: {run.id}")
          print(f"invoke_llm Trace Id: {run.trace_id}")
          print(f"invoke_llm Parent Run Id: {run.parent_run.id}")
          return openai.chat.completions.create(
              messages=messages, model="gpt-5.4-mini", temperature=0
          )

      @traceable
      def parse_output(response):
          run = get_current_run_tree()
          print(f"parse_output Run Id: {run.id}")
          print(f"parse_output Trace Id: {run.trace_id}")
          print(f"parse_output Parent Run Id: {run.parent_run.id}")
          return response.choices[0].message.content

      @traceable
      def run_pipeline():
          run = get_current_run_tree()
          print(f"run_pipeline Run Id: {run.id}")
          print(f"run_pipeline Trace Id: {run.trace_id}")
          messages = format_prompt("colorful socks")
          response = invoke_llm(messages)
          return parse_output(response)

  run_pipeline()
  ```

  ```typescript TypeScript theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  import { traceable, getCurrentRunTree } from "langsmith/traceable";
  import OpenAI from "openai";

      const openai = new OpenAI();

      const formatPrompt = traceable((subject: string) => {
          const run = getCurrentRunTree();
          console.log("formatPrompt Run ID", run.id)
          console.log("formatPrompt Trace ID", run.trace_id)
          console.log("formatPrompt Parent Run ID", run.parent_run.id)
          return [
              {
                  role: "system" as const,
                  content: "You are a helpful assistant.",
              },
              {
                  role: "user" as const,
                  content: `What's a good name for a store that sells ${subject}?`,
              },
          ];
      }, { name: "formatPrompt" });

      const invokeLLM = traceable(
          async (messages: { role: string; content: string }[]) => {
              const run = getCurrentRunTree();
              console.log("invokeLLM Run ID", run.id)
              console.log("invokeLLM Trace ID", run.trace_id)
              console.log("invokeLLM Parent Run ID", run.parent_run.id)
              return openai.chat.completions.create({
                  model: "gpt-5.4-mini",
                  messages: messages,
                  temperature: 0,
              });
          },
          { run_type: "llm", name: "invokeLLM" }
      );

      const parseOutput = traceable(
          (response: any) => {
              const run = getCurrentRunTree();
              console.log("parseOutput Run ID", run.id)
              console.log("parseOutput Trace ID", run.trace_id)
              console.log("parseOutput Parent Run ID", run.parent_run.id)
              return response.choices[0].message.content;
          },
          { name: "parseOutput" }
      );

      const runPipeline = traceable(
          async () => {
              const run = getCurrentRunTree();
              console.log("runPipline Run ID", run.id)
              console.log("runPipline Trace ID", run.trace_id)
              console.log("runPipline Parent Run ID", run.parent_run?.id)
              const messages = await formatPrompt("colorful socks");
              const response = await invokeLLM(messages);
              return parseOutput(response);
          },
          { name: "runPipeline" }
      );

  await runPipeline();
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/access-current-span.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Connect an authentication provider
Source: https://docs.langchain.com/langsmith/add-auth-server

In [the last tutorial](/langsmith/resource-auth), you added resource authorization to give users private conversations. However, you are still using hard-coded tokens for authentication, which is not secure. Now you'll replace those tokens with real user accounts using [OAuth2](/langsmith/deployment-quickstart).

You'll keep the same [`Auth`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth) object and [resource-level access control](/langsmith/auth#single-owner-resources), but upgrade authentication to use Supabase as your identity provider. While Supabase is used in this tutorial, the concepts apply to any OAuth2 provider. You'll learn how to:

1. Replace test tokens with real JWT tokens
2. Integrate with OAuth2 providers for secure user authentication
3. Handle user sessions and metadata while maintaining our existing authorization logic

## Background

OAuth2 involves three main roles:

1. **Authorization server**: The identity provider (e.g., Supabase, Auth0, Google) that handles user authentication and issues tokens
2. **Application backend**: Your LangGraph application. This validates tokens and serves protected resources (conversation data)
3. **Client application**: The web or mobile app where users interact with your service

A standard OAuth2 flow works something like this:

```mermaid theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
sequenceDiagram
    participant User
    participant Client
    participant AuthServer
    participant Agent Server

    User->>Client: Initiate login
    User->>AuthServer: Enter credentials
    AuthServer->>Client: Send tokens
    Client->>Agent Server: Request with token
    Agent Server->>AuthServer: Validate token
    AuthServer->>Agent Server: Token valid
    Agent Server->>Client: Serve request (e.g., run agent or graph)
```

## Prerequisites

Before you start this tutorial, ensure you have:

* The [bot from the second tutorial](/langsmith/resource-auth) running without errors.
* A [Supabase project](https://supabase.com/dashboard) to use its authentication server.

## 1. Install dependencies

Install the required dependencies. Start in your `custom-auth` directory and ensure you have the `langgraph-cli` installed:

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  cd custom-auth
  pip install -U "langgraph-cli[inmem]"
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  cd custom-auth
  uv add "langgraph-cli[inmem]"
  ```
</CodeGroup>

<a />

## 2. Set up the authentication provider

Next, fetch the URL of your auth server and the private key for authentication.
Since you're using Supabase for this, you can do this in the Supabase dashboard:

1. In the left sidebar, click on t️⚙ Project Settings" and then click "API"
2. Copy your project URL and add it to your `.env` file

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
echo "SUPABASE_URL=your-project-url" >> .env
```

3. Copy your service role secret key and add it to your `.env` file:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
echo "SUPABASE_SERVICE_KEY=your-service-role-key" >> .env
```

4. Copy your "anon public" key and note it down. This will be used later when you set up our client code.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
SUPABASE_URL=your-project-url
SUPABASE_SERVICE_KEY=your-service-role-key
```

## 3. Implement token validation

In the previous tutorials, you used the [`Auth`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth) object to [validate hard-coded tokens](/langsmith/set-up-custom-auth) and [add resource ownership](/langsmith/resource-auth).

Now you'll upgrade your authentication to validate real JWT tokens from Supabase. The main changes will all be in the [`@auth.authenticate`](https://reference.langchain.com/python/langgraph-sdk/auth/Auth/authenticate) decorated function:

* Instead of checking against a hard-coded list of tokens, you'll make an HTTP request to Supabase to validate the token.
* You'll extract real user information (ID, email) from the validated token.
* The existing resource authorization logic remains unchanged.

Update `src/security/auth.py` to implement this:

```python {highlight={8-9,20-30}} title="src/security/auth.py" theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
import httpx
from langgraph_sdk import Auth

auth = Auth()

# This is loaded from the `.env` file you created above
SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_SERVICE_KEY = os.environ["SUPABASE_SERVICE_KEY"]

@auth.authenticate
async def get_current_user(authorization: str | None):
    """Validate JWT tokens and extract user information."""
    assert authorization
    scheme, token = authorization.split()
    assert scheme.lower() == "bearer"

    try:
        # Verify token with auth provider
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{SUPABASE_URL}/auth/v1/user",
                headers={
                    "Authorization": authorization,
                    "apiKey": SUPABASE_SERVICE_KEY,
                },
            )
            assert response.status_code == 200
            user = response.json()
            return {
                "identity": user["id"],  # Unique user identifier
                "email": user["email"],
                "is_authenticated": True,
            }
    except Exception as e:
        raise Auth.exceptions.HTTPException(status_code=401, detail=str(e))

# ... the rest is the same as before

# Keep our resource authorization from the previous tutorial
@auth.on
async def add_owner(ctx, value):
    """Make resources private to their creator using resource metadata."""
    filters = {"owner": ctx.user.identity}
    metadata = value.setdefault("metadata", {})
    metadata.update(filters)
    return filters
```

The most important change is that we're now validating tokens with a real authentication server. Our authentication handler has the private key for our Supabase project, which we can use to validate the user's token and extract their information.

## 4. Test authentication flow

Let's test out the new authentication flow. You can run the following code in a file or notebook. You will need to provide:

* A valid email address
* A Supabase project URL (from [above](#setup-auth-provider))
* A Supabase anon **public key** (also from [above](#setup-auth-provider))

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import os
import httpx
from getpass import getpass
from langgraph_sdk import get_client

# Get email from command line
email = getpass("Enter your email: ")
base_email = email.split("@")
password = "secure-password"  # CHANGEME
email1 = f"{base_email[0]}+1@{base_email[1]}"
email2 = f"{base_email[0]}+2@{base_email[1]}"

SUPABASE_URL = os.environ.get("SUPABASE_URL")
if not SUPABASE_URL:
    SUPABASE_URL = getpass("Enter your Supabase project URL: ")

# This is your PUBLIC anon key (which is safe to use client-side)

# Do NOT mistake this for the secret service role key
SUPABASE_ANON_KEY = os.environ.get("SUPABASE_ANON_KEY")
if not SUPABASE_ANON_KEY:
    SUPABASE_ANON_KEY = getpass("Enter your public Supabase anon  key: ")

async def sign_up(email: str, password: str):
    """Create a new user account."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{SUPABASE_URL}/auth/v1/signup",
            json={"email": email, "password": password},
            headers={"apiKey": SUPABASE_ANON_KEY},
        )
        assert response.status_code == 200
        return response.json()

# Create two test users
print(f"Creating test users: {email1} and {email2}")
await sign_up(email1, password)
await sign_up(email2, password)
```

⚠️ Before continuing: Check your email and click both confirmation links. Supabase will reject `/login` requests until after you have confirmed your users' email.

Now test that users can only see their own data. Make sure the server is running (run `langgraph dev`) before proceeding. The following snippet requires the "anon public" key that you copied from the Supabase dashboard while [setting up the auth provider](#setup-auth-provider) previously.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
async def login(email: str, password: str):
    """Get an access token for an existing user."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
            json={
                "email": email,
                "password": password
            },
            headers={
                "apikey": SUPABASE_ANON_KEY,
                "Content-Type": "application/json"
            },
        )
        assert response.status_code == 200
        return response.json()["access_token"]

# Log in as user 1
user1_token = await login(email1, password)
user1_client = get_client(
    url="http://localhost:2024", headers={"Authorization": f"Bearer {user1_token}"}
)

# Create a thread as user 1
thread = await user1_client.threads.create()
print(f"✅ User 1 created thread: {thread['thread_id']}")

# Try to access without a token
unauthenticated_client = get_client(url="http://localhost:2024")
try:
    await unauthenticated_client.threads.create()
    print("❌ Unauthenticated access should fail!")
except Exception as e:
    print("✅ Unauthenticated access blocked:", e)

# Try to access user 1's thread as user 2
user2_token = await login(email2, password)
user2_client = get_client(
    url="http://localhost:2024", headers={"Authorization": f"Bearer {user2_token}"}
)

try:
    await user2_client.threads.get(thread["thread_id"])
    print("❌ User 2 shouldn't see User 1's thread!")
except Exception as e:
    print("✅ User 2 blocked from User 1's thread:", e)
```

The output should look like this:

```shell theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
✅ User 1 created thread: d6af3754-95df-4176-aa10-dbd8dca40f1a
✅ Unauthenticated access blocked: Client error '403 Forbidden' for url 'http://localhost:2024/threads'
✅ User 2 blocked from User 1's thread: Client error '404 Not Found' for url 'http://localhost:2024/threads/d6af3754-95df-4176-aa10-dbd8dca40f1a'
```

Your authentication and authorization are working together:

1. Users must log in to access the bot
2. Each user can only see their own threads

All users are managed by the Supabase auth provider, so you don't need to implement any additional user management logic.

## Next steps

You've successfully built a production-ready authentication system for your LangGraph application! Let's review what you've accomplished:

1. Set up an authentication provider (Supabase in this case)
2. Added real user accounts with email/password authentication
3. Integrated JWT token validation into your Agent Server
4. Implemented proper authorization to ensure users can only access their own data
5. Created a foundation that's ready to handle your next authentication challenge

Now that you have production authentication, consider:

1. Building a web UI with your preferred framework (see the [Custom Auth](https://github.com/langchain-ai/custom-auth) template for an example)
2. Learn more about the other aspects of authentication and authorization in the [conceptual guide on authentication](/langsmith/auth).
3. Customize your handlers and setup further after reading the [reference docs](https://reference.langchain.com/python/langgraph-sdk/auth/Auth).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/add-auth-server.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
