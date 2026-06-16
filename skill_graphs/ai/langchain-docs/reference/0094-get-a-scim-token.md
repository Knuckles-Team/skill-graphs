# Get a SCIM token
Source: https://docs.langchain.com/langsmith/smith-api/scim-tokens/get-a-scim-token

/langsmith/langsmith-platform-openapi.json get /v1/platform/orgs/current/scim/tokens/{scim_token_id}
Retrieve a specific SCIM token by ID for the current organization. The full token value is not returned.

# List SCIM tokens
Source: https://docs.langchain.com/langsmith/smith-api/scim-tokens/list-scim-tokens

/langsmith/langsmith-platform-openapi.json get /v1/platform/orgs/current/scim/tokens
List all SCIM bearer tokens for the current organization. The full token values are not returned.

# Update a SCIM token
Source: https://docs.langchain.com/langsmith/smith-api/scim-tokens/update-a-scim-token

/langsmith/langsmith-platform-openapi.json patch /v1/platform/orgs/current/scim/tokens/{scim_token_id}
Update the description of an existing SCIM token for the current organization.

# Create Service Account
Source: https://docs.langchain.com/langsmith/smith-api/service-accounts/create-service-account

/langsmith/langsmith-platform-openapi.json post /api/v1/service-accounts
Create a service account

# Delete Service Account
Source: https://docs.langchain.com/langsmith/smith-api/service-accounts/delete-service-account

/langsmith/langsmith-platform-openapi.json delete /api/v1/service-accounts/{service_account_id}
Delete a service account

# Get Service Accounts
Source: https://docs.langchain.com/langsmith/smith-api/service-accounts/get-service-accounts

/langsmith/langsmith-platform-openapi.json get /api/v1/service-accounts
Get the current organization's service accounts.

# List agent versions for a project
Source: https://docs.langchain.com/langsmith/smith-api/sessions/list-agent-versions-for-a-project

/langsmith/langsmith-platform-openapi.json get /v1/platform/sessions/{sessionID}/agent-versions
Returns all agent versions (commit SHAs) seen in the given tracing project, ordered by first_seen_at descending.

# Get Settings
Source: https://docs.langchain.com/langsmith/smith-api/settings/get-settings

/langsmith/langsmith-platform-openapi.json get /api/v1/settings
Get settings.

# Set Tenant Handle
Source: https://docs.langchain.com/langsmith/smith-api/settings/set-tenant-handle

/langsmith/langsmith-platform-openapi.json post /api/v1/settings/handle
Set tenant handle.

# Get tag transition history
Source: https://docs.langchain.com/langsmith/smith-api/tag-transitions/get-tag-transition-history

/langsmith/langsmith-platform-openapi.json get /repos/{owner}/{repo}/tags/{tag_name}/history
Returns the paginated audit log of transitions for a specific
tag in a repository. Each entry records a commit change
(from_commit → to_commit) along with who performed it.

# Create Tag
Source: https://docs.langchain.com/langsmith/smith-api/tags/create-tag

/langsmith/langsmith-platform-openapi.json post /api/v1/repos/{owner}/{repo}/tags
Create a tag. Requires repo ownership, prompts:tag permission, or ABAC grant.

# Delete Tag
Source: https://docs.langchain.com/langsmith/smith-api/tags/delete-tag

/langsmith/langsmith-platform-openapi.json delete /api/v1/repos/{owner}/{repo}/tags/{tag_name}
Delete a tag. Requires repo ownership, prompts:tag permission, or ABAC grant.

# Get Tag
Source: https://docs.langchain.com/langsmith/smith-api/tags/get-tag

/langsmith/langsmith-platform-openapi.json get /api/v1/repos/{owner}/{repo}/tags/{tag_name}

# Get Tags
Source: https://docs.langchain.com/langsmith/smith-api/tags/get-tags

/langsmith/langsmith-platform-openapi.json get /api/v1/repos/{owner}/{repo}/tags

# Update Tag
Source: https://docs.langchain.com/langsmith/smith-api/tags/update-tag

/langsmith/langsmith-platform-openapi.json patch /api/v1/repos/{owner}/{repo}/tags/{tag_name}
Update a tag. Requires repo ownership, prompts:tag permission, or ABAC grant.

# Create Tenant
Source: https://docs.langchain.com/langsmith/smith-api/tenant/create-tenant

/langsmith/langsmith-platform-openapi.json post /api/v1/tenants
Create a new organization and corresponding workspace.

# List Tenants
Source: https://docs.langchain.com/langsmith/smith-api/tenant/list-tenants

/langsmith/langsmith-platform-openapi.json get /api/v1/tenants
Get all tenants visible to this auth

# Create a tool
Source: https://docs.langchain.com/langsmith/smith-api/tools/create-a-tool

/langsmith/langsmith-platform-openapi.json post /v1/platform/tools
Creates a new tool in the workspace.

# Delete a tool by handle
Source: https://docs.langchain.com/langsmith/smith-api/tools/delete-a-tool-by-handle

/langsmith/langsmith-platform-openapi.json delete /v1/platform/tools/{handle}
Deletes a tool identified by its handle.

# Delete a tool by ID
Source: https://docs.langchain.com/langsmith/smith-api/tools/delete-a-tool-by-id

/langsmith/langsmith-platform-openapi.json delete /v1/platform/tools/id/{id}
Deletes a tool identified by its UUID.

# Get a tool by handle
Source: https://docs.langchain.com/langsmith/smith-api/tools/get-a-tool-by-handle

/langsmith/langsmith-platform-openapi.json get /v1/platform/tools/{handle}
Returns a tool identified by its handle.

# Get a tool by ID
Source: https://docs.langchain.com/langsmith/smith-api/tools/get-a-tool-by-id

/langsmith/langsmith-platform-openapi.json get /v1/platform/tools/id/{id}
Returns a tool identified by its UUID.

# List tools
Source: https://docs.langchain.com/langsmith/smith-api/tools/list-tools

/langsmith/langsmith-platform-openapi.json get /v1/platform/tools
Returns a paginated list of tools in the workspace.

# Update a tool by handle
Source: https://docs.langchain.com/langsmith/smith-api/tools/update-a-tool-by-handle

/langsmith/langsmith-platform-openapi.json patch /v1/platform/tools/{handle}
Updates an existing tool identified by its handle.

# Update a tool by ID
Source: https://docs.langchain.com/langsmith/smith-api/tools/update-a-tool-by-id

/langsmith/langsmith-platform-openapi.json patch /v1/platform/tools/id/{id}
Updates an existing tool identified by its UUID.

# [Beta] Auto-Generate Insights Job Config
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-auto-generate-insights-job-config

/langsmith/langsmith-platform-openapi.json post /api/v1/sessions/{session_id}/insights/configs/generate
Auto-generate an insights job config.

# [Beta] Create Insights Job
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-create-insights-job

/langsmith/langsmith-platform-openapi.json post /api/v1/sessions/{session_id}/insights
Create an insights job.

# [Beta] Create Insights Job Config
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-create-insights-job-config

/langsmith/langsmith-platform-openapi.json post /api/v1/sessions/{session_id}/insights/configs
Save an insights job config.

# [Beta] Delete Insights Job
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-delete-insights-job

/langsmith/langsmith-platform-openapi.json delete /api/v1/sessions/{session_id}/insights/{job_id}
Delete a session cluster job.

# [Beta] Delete Insights Job Config
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-delete-insights-job-config

/langsmith/langsmith-platform-openapi.json delete /api/v1/sessions/{session_id}/insights/configs/{config_id}
Delete an insights job config.

# [Beta] Get Insights Job
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-get-insights-job

/langsmith/langsmith-platform-openapi.json get /api/v1/sessions/{session_id}/insights/{job_id}
Get a specific cluster job for a session.

# [Beta] Get Insights Job Configs
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-get-insights-job-configs

/langsmith/langsmith-platform-openapi.json get /api/v1/sessions/{session_id}/insights/configs
Get all insights job configs for a session.

# [Beta] Get Insights Jobs
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-get-insights-jobs

/langsmith/langsmith-platform-openapi.json get /api/v1/sessions/{session_id}/insights
Get all clusters for a session.

# [Beta] Get Run Cluster From Insights Job
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-get-run-cluster-from-insights-job

/langsmith/langsmith-platform-openapi.json get /api/v1/sessions/{session_id}/insights/{job_id}/clusters/{cluster_id}
Get a specific cluster for a session.

# [Beta] Get Runs From Insights Job
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-get-runs-from-insights-job

/langsmith/langsmith-platform-openapi.json get /api/v1/sessions/{session_id}/insights/{job_id}/runs
Get all runs for a cluster job, optionally filtered by cluster.

# [Beta] Update Insights Job
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-update-insights-job

/langsmith/langsmith-platform-openapi.json patch /api/v1/sessions/{session_id}/insights/{job_id}
Update a session cluster job.

# [Beta] Update Insights Job Config
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/[beta]-update-insights-job-config

/langsmith/langsmith-platform-openapi.json patch /api/v1/sessions/{session_id}/insights/configs/{config_id}
Update an insights job config.

# Create Filter View
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/create-filter-view

/langsmith/langsmith-platform-openapi.json post /api/v1/sessions/{session_id}/views
Create a new filter view.

# Create Tracer Session
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/create-tracer-session

/langsmith/langsmith-platform-openapi.json post /api/v1/sessions
Create a new session.

# Delete Filter View
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/delete-filter-view

/langsmith/langsmith-platform-openapi.json delete /api/v1/sessions/{session_id}/views/{view_id}
Delete a specific filter view.

# Delete Tracer Session
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/delete-tracer-session

/langsmith/langsmith-platform-openapi.json delete /api/v1/sessions/{session_id}
Delete a specific session.

# Delete Tracer Sessions
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/delete-tracer-sessions

/langsmith/langsmith-platform-openapi.json delete /api/v1/sessions
Delete sessions.

# Get Tracing Project Prebuilt Dashboard
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/get-tracing-project-prebuilt-dashboard

/langsmith/langsmith-platform-openapi.json post /api/v1/sessions/{session_id}/dashboard
Get a prebuilt dashboard for a tracing project.

# Read Filter View
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/read-filter-view

/langsmith/langsmith-platform-openapi.json get /api/v1/sessions/{session_id}/views/{view_id}
Get a specific filter view.

# Read Filter Views
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/read-filter-views

/langsmith/langsmith-platform-openapi.json get /api/v1/sessions/{session_id}/views
Get all filter views for a session.

# Read Tracer Session
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/read-tracer-session

/langsmith/langsmith-platform-openapi.json get /api/v1/sessions/{session_id}
Get a specific session.

# Read Tracer Sessions
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/read-tracer-sessions

/langsmith/langsmith-platform-openapi.json get /api/v1/sessions
Get all sessions.

# Read Tracer Sessions Runs Metadata
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/read-tracer-sessions-runs-metadata

/langsmith/langsmith-platform-openapi.json get /api/v1/sessions/{session_id}/metadata
Given a session, a number K, and (optionally) a list of metadata keys, return the top K values for each key.

# Rename Filter View
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/rename-filter-view

/langsmith/langsmith-platform-openapi.json patch /api/v1/sessions/{session_id}/views/{view_id}/rename
Rename a filter view (display_name and description only).

# Update Filter View
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/update-filter-view

/langsmith/langsmith-platform-openapi.json patch /api/v1/sessions/{session_id}/views/{view_id}
Update a filter view.

# Update Tracer Session
Source: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/update-tracer-session

/langsmith/langsmith-platform-openapi.json patch /api/v1/sessions/{session_id}
Update a session.

# Get workspace TTL settings
Source: https://docs.langchain.com/langsmith/smith-api/ttl-settings/get-workspace-ttl-settings

/langsmith/langsmith-platform-openapi.json get /workspaces/current/ttl-settings
Get the longlived trace TTL settings for a workspace

# List Ttl Settings
Source: https://docs.langchain.com/langsmith/smith-api/ttl-settings/list-ttl-settings

/langsmith/langsmith-platform-openapi.json get /api/v1/ttl-settings
List out the configured TTL settings for a given tenant.

# Update workspace TTL settings
Source: https://docs.langchain.com/langsmith/smith-api/ttl-settings/update-workspace-ttl-settings

/langsmith/langsmith-platform-openapi.json put /workspaces/current/ttl-settings
Update the longlived trace TTL for a workspace.

# Upsert Ttl Settings
Source: https://docs.langchain.com/langsmith/smith-api/ttl-settings/upsert-ttl-settings

/langsmith/langsmith-platform-openapi.json put /api/v1/ttl-settings

# Delete Usage Limit
Source: https://docs.langchain.com/langsmith/smith-api/usage-limits/delete-usage-limit

/langsmith/langsmith-platform-openapi.json delete /api/v1/usage-limits/{usage_limit_id}
Delete a specific usage limit.

# List Org Usage Limits
Source: https://docs.langchain.com/langsmith/smith-api/usage-limits/list-org-usage-limits

/langsmith/langsmith-platform-openapi.json get /api/v1/usage-limits/org
List out the configured usage limits for a given organization.

# List Usage Limits
Source: https://docs.langchain.com/langsmith/smith-api/usage-limits/list-usage-limits

/langsmith/langsmith-platform-openapi.json get /api/v1/usage-limits
List out the configured usage limits for a given tenant.

# Upsert Usage Limit
Source: https://docs.langchain.com/langsmith/smith-api/usage-limits/upsert-usage-limit

/langsmith/langsmith-platform-openapi.json put /api/v1/usage-limits
Create a new usage limit.

# Add Member To Current Workspace
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/add-member-to-current-workspace

/langsmith/langsmith-platform-openapi.json post /api/v1/workspaces/current/members
Add an existing organization member to the current workspace.

# Add Members To Current Workspace Batch
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/add-members-to-current-workspace-batch

/langsmith/langsmith-platform-openapi.json post /api/v1/workspaces/current/members/batch
Batch invite up to 500 users to the current workspace and organization.

# Bulk Unshare Entities
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/bulk-unshare-entities

/langsmith/langsmith-platform-openapi.json delete /api/v1/workspaces/current/shared
Bulk unshare entities by share tokens for the workspace.

# Claim Pending Workspace Invite
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/claim-pending-workspace-invite

/langsmith/langsmith-platform-openapi.json post /api/v1/workspaces/pending/{workspace_id}/claim

# Create Tag Key
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/create-tag-key

/langsmith/langsmith-platform-openapi.json post /api/v1/workspaces/current/tag-keys

# Create Tag Value
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/create-tag-value

/langsmith/langsmith-platform-openapi.json post /api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values

# Create Tagging
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/create-tagging

/langsmith/langsmith-platform-openapi.json post /api/v1/workspaces/current/taggings

# Create Workspace
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/create-workspace

/langsmith/langsmith-platform-openapi.json post /api/v1/workspaces
Create a new workspace.

# Delete Current Workspace Member
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/delete-current-workspace-member

/langsmith/langsmith-platform-openapi.json delete /api/v1/workspaces/current/members/{identity_id}

# Delete Current Workspace Pending Member
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/delete-current-workspace-pending-member

/langsmith/langsmith-platform-openapi.json delete /api/v1/workspaces/current/members/{identity_id}/pending

# Delete Pending Workspace Invite
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/delete-pending-workspace-invite

/langsmith/langsmith-platform-openapi.json delete /api/v1/workspaces/pending/{id}

# Delete Tag Key
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/delete-tag-key

/langsmith/langsmith-platform-openapi.json delete /api/v1/workspaces/current/tag-keys/{tag_key_id}

# Delete Tag Value
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/delete-tag-value

/langsmith/langsmith-platform-openapi.json delete /api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values/{tag_value_id}

# Delete Tagging
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/delete-tagging

/langsmith/langsmith-platform-openapi.json delete /api/v1/workspaces/current/taggings/{tagging_id}

# Delete Workspace
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/delete-workspace

/langsmith/langsmith-platform-openapi.json delete /api/v1/workspaces/{workspace_id}

# Get Current Active Workspace Members
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-active-workspace-members

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/members/active

# Get Current Pending Workspace Members
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-pending-workspace-members

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/members/pending

# Get Current Workspace Encrypted Secrets
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-workspace-encrypted-secrets

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/secrets/encrypted
Get encrypted workspace secrets for use with Fleet and external services.

# Get Current Workspace Members
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-workspace-members

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/members

# Get Current Workspace Stats
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-workspace-stats

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/stats

# Get Current Workspace Usage Limits Info
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-workspace-usage-limits-info

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/usage_limits

# Get Shared Tokens
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/get-shared-tokens

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/shared
List all shared entities and their tokens by the workspace.

# Get Tag Key
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/get-tag-key

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/tag-keys/{tag_key_id}

# Get Tag Value
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/get-tag-value

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values/{tag_value_id}

# List Current Workspace Secrets
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/list-current-workspace-secrets

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/secrets

# List Pending Workspace Invites
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/list-pending-workspace-invites

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/pending
Get all workspaces visible to this auth

# List Tag Keys
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/list-tag-keys

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/tag-keys

# List Tag Values
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/list-tag-values

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values

# List Taggings
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/list-taggings

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/taggings

# List Tags
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/list-tags

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/tags

# List Tags For Resource
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/list-tags-for-resource

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces/current/tags/resource

# List Tags For Resources
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/list-tags-for-resources

/langsmith/langsmith-platform-openapi.json post /api/v1/workspaces/current/tags/resources

# List Workspaces
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/list-workspaces

/langsmith/langsmith-platform-openapi.json get /api/v1/workspaces
Get all workspaces visible to this auth in the current org. Does not create a new workspace/org.

# Patch Current Workspace Member
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/patch-current-workspace-member

/langsmith/langsmith-platform-openapi.json patch /api/v1/workspaces/current/members/{identity_id}

# Patch Workspace
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/patch-workspace

/langsmith/langsmith-platform-openapi.json patch /api/v1/workspaces/{workspace_id}
Update a workspace.

# Update Tag Key
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/update-tag-key

/langsmith/langsmith-platform-openapi.json patch /api/v1/workspaces/current/tag-keys/{tag_key_id}

# Update Tag Value
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/update-tag-value

/langsmith/langsmith-platform-openapi.json patch /api/v1/workspaces/current/tag-keys/{tag_key_id}/tag-values/{tag_value_id}

# Upsert Current Workspace Secrets
Source: https://docs.langchain.com/langsmith/smith-api/workspaces/upsert-current-workspace-secrets

/langsmith/langsmith-platform-openapi.json post /api/v1/workspaces/current/secrets

# LangSmith Deployment SDK
Source: https://docs.langchain.com/langsmith/smith-deployments-sdk

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/smith-deployments-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Go SDK
Source: https://docs.langchain.com/langsmith/smith-go-sdk

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/smith-go-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Java SDK
Source: https://docs.langchain.com/langsmith/smith-java-sdk

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/smith-java-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith JS/TS SDK
Source: https://docs.langchain.com/langsmith/smith-js-ts-sdk

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/smith-js-ts-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith Python SDK
Source: https://docs.langchain.com/langsmith/smith-python-sdk

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/smith-python-sdk.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Stateless runs
Source: https://docs.langchain.com/langsmith/stateless-runs

Most of the time, you provide a `thread_id` to your client when you run your graph in order to keep track of prior runs through the persistent state implemented in LangSmith Deployment. However, if you don't need to persist the runs you don't need to use the built-in persistent state and can create stateless runs.

## Setup

First, let's setup our client:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    from langgraph_sdk import get_client

    client = get_client(url=<DEPLOYMENT_URL>)
    # Using the graph deployed with the name "agent"
    assistant_id = "agent"
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    import { Client } from "@langchain/langgraph-sdk";

    const client = new Client({ apiUrl: <DEPLOYMENT_URL> });
    // Using the graph deployed with the name "agent"
    const assistantId = "agent";
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url <DEPLOYMENT_URL>/assistants/search \
        --header 'Content-Type: application/json' \
        --data '{
            "limit": 10,
            "offset": 0
        }' | jq -c 'map(select(.config == null or .config == {})) | .[0].graph_id' && \
    curl --request POST \
        --url <DEPLOYMENT_URL>/threads \
        --header 'Content-Type: application/json' \
        --data '{}'
    ```
  </Tab>
</Tabs>

## Stateless streaming

We can stream the results of a stateless run in an almost identical fashion to how we stream from a run with the state attribute, but instead of passing a value to the `thread_id` parameter, we pass `None`:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    input = {
        "messages": [
            {"role": "user", "content": "Hello! My name is Bagatur and I am 26 years old."}
        ]
    }

    async for chunk in client.runs.stream(
        # Don't pass in a thread_id and the stream will be stateless
        None,
        assistant_id,
        input=input,
        stream_mode="updates",
    ):
        if chunk.data and "run_id" not in chunk.data:
            print(chunk.data)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    let input = {
      messages: [
        { role: "user", content: "Hello! My name is Bagatur and I am 26 years old." }
      ]
    };

    const streamResponse = client.runs.stream(
      // Don't pass in a thread_id and the stream will be stateless
      null,
      assistantId,
      {
        input,
        streamMode: "updates"
      }
    );
    for await (const chunk of streamResponse) {
      if (chunk.data && !("run_id" in chunk.data)) {
        console.log(chunk.data);
      }
    }
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url <DEPLOYMENT_URL>/runs/stream \
        --header 'Content-Type: application/json' \
        --data "{
            \"assistant_id\": \"agent\",
            \"input\": {\"messages\": [{\"role\": \"human\", \"content\": \"Hello! My name is Bagatur and I am 26 years old.\"}]},
            \"stream_mode\": [
                \"updates\"
            ]
        }" | jq -c 'select(.data and (.data | has("run_id") | not)) | .data'
    ```
  </Tab>
</Tabs>

Output:

```
{'agent': {'messages': [{'content': "Hello Bagatur! It's nice to meet you. Thank you for introducing yourself and sharing your age. Is there anything specific you'd like to know or discuss? I'm here to help with any questions or topics you're interested in.", 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'ai', 'name': None, 'id': 'run-489ec573-1645-4ce2-a3b8-91b391d50a71', 'example': False, 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': None}]}}
```

## Waiting for stateless results

In addition to streaming, you can also wait for a stateless result by using the `.wait` function like follows:

<Tabs>
  <Tab title="Python">
    ```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    stateless_run_result = await client.runs.wait(
        None,
        assistant_id,
        input=input,
    )
    print(stateless_run_result)
    ```
  </Tab>

  <Tab title="Javascript">
    ```js theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    let statelessRunResult = await client.runs.wait(
      null,
      assistantId,
      { input: input }
    );
    console.log(statelessRunResult);
    ```
  </Tab>

  <Tab title="CURL">
    ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
    curl --request POST \
        --url <DEPLOYMENT_URL>/runs/wait \
        --header 'Content-Type: application/json' \
        --data '{
            "assistant_id": <ASSISTANT_IDD>,
        }'
    ```
  </Tab>
</Tabs>

Output:

```
{
    'messages': [
        {
            'content': 'Hello! My name is Bagatur and I am 26 years old.',
            'additional_kwargs': {},
            'response_metadata': {},
            'type': 'human',
            'name': None,
            'id': '5e088543-62c2-43de-9d95-6086ad7f8b48',
            'example': False
        },
        {
            'content': 'Hello Bagatur! It's nice to meet you. Thank you for introducing yourself and sharing your age. Is there anything specific you'd like to know or discuss? I'm here to help with any questions or topics you'd like to explore.',
            'additional_kwargs': {},
            'response_metadata': {},
            'type': 'ai',
            'name': None,
            'id': 'run-d6361e8d-4d4c-45bd-ba47-39520257f773',
            'example': False,
            'tool_calls': [],
            'invalid_tool_calls': [],
            'usage_metadata': None
        }
    ]
}
```

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/stateless-runs.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith status
Source: https://docs.langchain.com/langsmith/status

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/status.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
