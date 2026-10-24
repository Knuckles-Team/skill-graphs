# Get vendor account
Source: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/get-vendor-account

/langsmith/langsmith-platform-openapi.json get /v1/platform/mcp-vendors/{vendor_slug}/account
Resolves OAuth token and returns the vendor's account info.

# Get vendor settings
Source: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/get-vendor-settings

/langsmith/langsmith-platform-openapi.json get /v1/platform/mcp-vendors/{vendor_slug}/settings
Returns the current vendor-specific settings.

# List MCP servers for a vendor
Source: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/list-mcp-servers-for-a-vendor

/langsmith/langsmith-platform-openapi.json get /v1/platform/mcp-vendors/{vendor_slug}/mcp-servers
Returns the MCP gateways from the vendor for the workspace's configured org/project.

# List MCP vendors
Source: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/list-mcp-vendors

/langsmith/langsmith-platform-openapi.json get /v1/platform/mcp-vendors
Returns the catalog of available MCP vendors.

# List tools for a vendor
Source: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/list-tools-for-a-vendor

/langsmith/langsmith-platform-openapi.json get /v1/platform/mcp-vendors/{vendor_slug}/tools
Returns the tool catalog for this vendor.

# Replace vendor settings
Source: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/replace-vendor-settings

/langsmith/langsmith-platform-openapi.json put /v1/platform/mcp-vendors/{vendor_slug}/settings
Replaces vendor settings.

# Create Onboarding State
Source: https://docs.langchain.com/langsmith/smith-api/me/create-onboarding-state

/langsmith/langsmith-platform-openapi.json post /api/v1/me/onboarding_state
Initialize onboarding state for the current user.

# Get Ls User Id
Source: https://docs.langchain.com/langsmith/smith-api/me/get-ls-user-id

/langsmith/langsmith-platform-openapi.json get /api/v1/me/ls_user_id
Get the LangSmith user ID for the current user.

# Get Onboarding State
Source: https://docs.langchain.com/langsmith/smith-api/me/get-onboarding-state

/langsmith/langsmith-platform-openapi.json get /api/v1/me/onboarding_state
Get onboarding state for the current user.

# Get the authenticated user's provider user ID
Source: https://docs.langchain.com/langsmith/smith-api/me/get-the-authenticated-users-provider-user-id

/langsmith/langsmith-platform-openapi.json get /me/providers/{providerType}
Returns the provider user ID associated with the authenticated user for a given provider type, or null if not set. Scoped to the current tenant.

# Update Onboarding State Field
Source: https://docs.langchain.com/langsmith/smith-api/me/update-onboarding-state-field

/langsmith/langsmith-platform-openapi.json put /api/v1/me/onboarding_state/{field}
Update a specific onboarding completion field for the current user.

Valid fields:
- tracing_completed_at
- lgstudio_completed_at
- playground_completed_at
- evaluation_completed_at
- success_viewed_at

# Create New Model Price
Source: https://docs.langchain.com/langsmith/smith-api/model-price-map/create-new-model-price

/langsmith/langsmith-platform-openapi.json post /api/v1/model-price-map

# Delete Model Price
Source: https://docs.langchain.com/langsmith/smith-api/model-price-map/delete-model-price

/langsmith/langsmith-platform-openapi.json delete /api/v1/model-price-map/{id}

# Read Model Price Map
Source: https://docs.langchain.com/langsmith/smith-api/model-price-map/read-model-price-map

/langsmith/langsmith-platform-openapi.json get /api/v1/model-price-map

# Update Model Price
Source: https://docs.langchain.com/langsmith/smith-api/model-price-map/update-model-price

/langsmith/langsmith-platform-openapi.json put /api/v1/model-price-map/{id}

# Approve OAuth2 authorization request
Source: https://docs.langchain.com/langsmith/smith-api/oauth/approve-oauth2-authorization-request

/langsmith/langsmith-platform-openapi.json post /oauth/authorize/approve
Issues an authorization code after the authenticated user approves the request. Called by the frontend consent page. Requires authentication.

# Authorize a device code
Source: https://docs.langchain.com/langsmith/smith-api/oauth/authorize-a-device-code

/langsmith/langsmith-platform-openapi.json post /oauth/device/authorize
Marks a device code as authorized for the authenticated user. Called by the /activate page when the user enters their user code. Requires authentication.

# Exchange grant for OAuth2 tokens
Source: https://docs.langchain.com/langsmith/smith-api/oauth/exchange-grant-for-oauth2-tokens

/langsmith/langsmith-platform-openapi.json post /oauth/token
Token endpoint that dispatches by grant_type: authorization_code, urn:ietf:params:oauth:grant-type:device_code, or refresh_token.

# Get OAuth2 authorization server metadata
Source: https://docs.langchain.com/langsmith/smith-api/oauth/get-oauth2-authorization-server-metadata

/langsmith/langsmith-platform-openapi.json get /.well-known/oauth-authorization-server
Returns OAuth2 authorization server metadata per RFC 8414, including supported endpoints, grant types, and response types.

# Get public OAuth2 client metadata
Source: https://docs.langchain.com/langsmith/smith-api/oauth/get-public-oauth2-client-metadata

/langsmith/langsmith-platform-openapi.json get /oauth/client/{clientID}
Returns the display metadata (name, logo, homepage/terms/privacy links) for a registered OAuth2 client. Used by the consent screen to show a human-readable client identity instead of the raw client_id. Public endpoint; exposes only non-sensitive display fields.

# Initiate OAuth2 authorization
Source: https://docs.langchain.com/langsmith/smith-api/oauth/initiate-oauth2-authorization

/langsmith/langsmith-platform-openapi.json get /oauth/authorize
Validates authorization request parameters and redirects to the frontend consent page per RFC 6749.

# Register an OAuth2 dynamic client
Source: https://docs.langchain.com/langsmith/smith-api/oauth/register-an-oauth2-dynamic-client

/langsmith/langsmith-platform-openapi.json post /oauth/register
Public RFC 7591 Dynamic Client Registration endpoint. Only mints public clients with allowed loopback, HTTPS, or native client redirect URIs. Body limit 8 KB.

# Request OAuth2 device authorization
Source: https://docs.langchain.com/langsmith/smith-api/oauth/request-oauth2-device-authorization

/langsmith/langsmith-platform-openapi.json post /oauth/device/code
Issues a device code and user code for the device authorization flow per RFC 8628.

# Revoke an OAuth2 token
Source: https://docs.langchain.com/langsmith/smith-api/oauth/revoke-an-oauth2-token

/langsmith/langsmith-platform-openapi.json post /oauth/revoke
Revokes an access token or refresh token per RFC 7009. Always returns 200 regardless of whether the token was found.

# Create Job
Source: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/create-job

/langsmith/langsmith-platform-openapi.json post /api/v1/repos/{owner}/{repo}/optimization-jobs
Create a new prompt optimization job.

# Create Log
Source: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/create-log

/langsmith/langsmith-platform-openapi.json post /api/v1/repos/{owner}/{repo}/optimization-jobs/{job_id}/logs
Create a new log entry for a prompt optimization job.

# Delete Job
Source: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/delete-job

/langsmith/langsmith-platform-openapi.json delete /api/v1/repos/{owner}/{repo}/optimization-jobs/{job_id}
Delete a prompt optimization job.

# Delete Log
Source: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/delete-log

/langsmith/langsmith-platform-openapi.json delete /api/v1/repos/{owner}/{repo}/optimization-jobs/{job_id}/logs/{log_id}
Delete a prompt optimization job log.

# Get Job
Source: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/get-job

/langsmith/langsmith-platform-openapi.json get /api/v1/repos/{owner}/{repo}/optimization-jobs/{job_id}
Get a specific optimization job.

# Get Log
Source: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/get-log

/langsmith/langsmith-platform-openapi.json get /api/v1/repos/{owner}/{repo}/optimization-jobs/{job_id}/logs/{log_id}
Get a specific prompt optimization job log.

# List Job Logs
Source: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/list-job-logs

/langsmith/langsmith-platform-openapi.json get /api/v1/repos/{owner}/{repo}/optimization-jobs/{job_id}/logs
List all logs for a specific prompt optimization job.

# List Jobs
Source: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/list-jobs

/langsmith/langsmith-platform-openapi.json get /api/v1/repos/{owner}/{repo}/optimization-jobs
List all prompt optimization jobs.

# Update Job
Source: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/update-job

/langsmith/langsmith-platform-openapi.json patch /api/v1/repos/{owner}/{repo}/optimization-jobs/{job_id}
Replace an existing prompt optimization job with a new, modified job.

# Get current organization info
Source: https://docs.langchain.com/langsmith/smith-api/organizations/get-current-organization-info

/langsmith/langsmith-platform-openapi.json get /v1/platform/orgs/current/info
Returns organization info for the authenticated user's current organization.

# Add Basic Auth Members To Current Org
Source: https://docs.langchain.com/langsmith/smith-api/orgs/add-basic-auth-members-to-current-org

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/members/basic/batch
Batch add up to 500 users to the org and specified workspaces in basic auth mode.

# Add Member To Current Org
Source: https://docs.langchain.com/langsmith/smith-api/orgs/add-member-to-current-org

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/members

# Add Members To Current Org Batch
Source: https://docs.langchain.com/langsmith/smith-api/orgs/add-members-to-current-org-batch

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/members/batch
Batch invite up to 500 users to the current org.

# Change Payment Plan
Source: https://docs.langchain.com/langsmith/smith-api/orgs/change-payment-plan

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/plan

# Claim Pending Organization Invite
Source: https://docs.langchain.com/langsmith/smith-api/orgs/claim-pending-organization-invite

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/pending/{organization_id}/claim

# Create Customers And Get Stripe Setup Intent
Source: https://docs.langchain.com/langsmith/smith-api/orgs/create-customers-and-get-stripe-setup-intent

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/setup

# Create Org Personal Access Token
Source: https://docs.langchain.com/langsmith/smith-api/orgs/create-org-personal-access-token

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/personal-access-tokens

# Create Org Service Key
Source: https://docs.langchain.com/langsmith/smith-api/orgs/create-org-service-key

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/service-keys
Create org-scoped service key. If workspaces is None, key is org-wide.

# Create Organization
Source: https://docs.langchain.com/langsmith/smith-api/orgs/create-organization

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs

# Create Organization Roles
Source: https://docs.langchain.com/langsmith/smith-api/orgs/create-organization-roles

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/roles

# Create Sso Settings
Source: https://docs.langchain.com/langsmith/smith-api/orgs/create-sso-settings

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/sso-settings
Create SSO provider settings for the current organization.

# Create Stripe Account Links Endpoint
Source: https://docs.langchain.com/langsmith/smith-api/orgs/create-stripe-account-links-endpoint

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/stripe_account_links
Kick off a Stripe account link flow.

# Create Stripe Checkout Sessions Endpoint
Source: https://docs.langchain.com/langsmith/smith-api/orgs/create-stripe-checkout-sessions-endpoint

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/stripe_checkout_session
Kick off a Stripe checkout session flow.

# Delete Current Org Pending Member
Source: https://docs.langchain.com/langsmith/smith-api/orgs/delete-current-org-pending-member

/langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/current/members/{identity_id}/pending
When an admin deletes a pending member invite.

# Delete Org Personal Access Token
Source: https://docs.langchain.com/langsmith/smith-api/orgs/delete-org-personal-access-token

/langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/current/personal-access-tokens/{pat_id}

# Delete Org Service Key
Source: https://docs.langchain.com/langsmith/smith-api/orgs/delete-org-service-key

/langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/current/service-keys/{api_key_id}

# Delete Organization Roles
Source: https://docs.langchain.com/langsmith/smith-api/orgs/delete-organization-roles

/langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/current/roles/{role_id}

# Delete Pending Organization Invite
Source: https://docs.langchain.com/langsmith/smith-api/orgs/delete-pending-organization-invite

/langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/pending/{organization_id}

# Delete Sso Settings
Source: https://docs.langchain.com/langsmith/smith-api/orgs/delete-sso-settings

/langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/current/sso-settings/{id}
Delete SSO provider settings for the current organization.

# Export Granular Usage Csv
Source: https://docs.langchain.com/langsmith/smith-api/orgs/export-granular-usage-csv

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/billing/granular-usage/export
Export granular usage data as CSV.

Same `kind` semantics as `/granular-usage`. The CSV's value columns
vary by kind:
- `traces`: single `Traces` column.
- `langsmith_deployments`: `Nodes Executed`, `Agent Runs`,
  `Agent Uptime (seconds)` columns.
Dimension columns are identical across kinds.

# Get Company Info
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-company-info

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/business-info

# Get Current Active Org Members
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-current-active-org-members

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/members/active

# Get Current Org Members
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-current-org-members

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/members

# Get Current Organization Info
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-current-organization-info

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/info

# Get Current Pending Org Members
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-current-pending-org-members

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/members/pending

# Get Current Sso Settings
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-current-sso-settings

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/sso-settings
Get SSO provider settings for the current organization.

# Get Current User Login Methods
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-current-user-login-methods

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/user/login-methods
Get login methods for the current user.

# Get Dashboard
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-dashboard

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/dashboard

# Get Granular Usage
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-granular-usage

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/billing/granular-usage
Get granular usage data with flexible grouping.

`kind` selects the billable usage domain:
- `traces` (default): trace counts.
- `langsmith_deployments`: LangSmith Deployment metrics (nodes
  executed, agent runs, agent uptime). The three Deployment fields
  are populated and `traces` is `0`.

`trace_tier` (only meaningful for `kind=traces`) optionally restricts
results to a single retention tier (longlived = extended retention,
shortlived = standard retention). When `group_by=trace_tier`, results
are split into one record per retention tier per time bucket.

`workspace_ids` filters results to the specified workspaces. Only
workspaces the user has read access to are included.

# Get Org Usage
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-org-usage

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/billing/usage

# Get Organization Billing Info
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-organization-billing-info

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/billing

# Get Organization Info
Source: https://docs.langchain.com/langsmith/smith-api/orgs/get-organization-info

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current

# List org members with workspace roles
Source: https://docs.langchain.com/langsmith/smith-api/orgs/list-org-members-with-workspace-roles

/langsmith/langsmith-platform-openapi.json get /v1/platform/orgs/current/members
Returns a paginated list of org members (active and pending) enriched with workspace memberships.

# List Org Personal Access Tokens
Source: https://docs.langchain.com/langsmith/smith-api/orgs/list-org-personal-access-tokens

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/personal-access-tokens

# List Org Service Keys
Source: https://docs.langchain.com/langsmith/smith-api/orgs/list-org-service-keys

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/service-keys

# List Organization Roles
Source: https://docs.langchain.com/langsmith/smith-api/orgs/list-organization-roles

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/current/roles

# List Organizations
Source: https://docs.langchain.com/langsmith/smith-api/orgs/list-organizations

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs
Get all orgs visible to this auth

# List Pending Organization Invites
Source: https://docs.langchain.com/langsmith/smith-api/orgs/list-pending-organization-invites

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/pending
Get all pending orgs visible to this auth

# List Permissions
Source: https://docs.langchain.com/langsmith/smith-api/orgs/list-permissions

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/permissions

# List Ttl Settings
Source: https://docs.langchain.com/langsmith/smith-api/orgs/list-ttl-settings

/langsmith/langsmith-platform-openapi.json get /api/v1/orgs/ttl-settings
List out the configured TTL settings for a given org (org-level and tenant-level).

# On Payment Method Created
Source: https://docs.langchain.com/langsmith/smith-api/orgs/on-payment-method-created

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/payment-method

# Remove Member From Current Org
Source: https://docs.langchain.com/langsmith/smith-api/orgs/remove-member-from-current-org

/langsmith/langsmith-platform-openapi.json delete /api/v1/orgs/current/members/{identity_id}
Remove a user from the current organization.

# Set Company Info
Source: https://docs.langchain.com/langsmith/smith-api/orgs/set-company-info

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/business-info

# Set Default Sso Provision
Source: https://docs.langchain.com/langsmith/smith-api/orgs/set-default-sso-provision

/langsmith/langsmith-platform-openapi.json post /api/v1/orgs/current/set-default-sso-provision
Set the current organization as the default for SSO provisioning in self-hosted environments.

# Update Allowed Login Methods
Source: https://docs.langchain.com/langsmith/smith-api/orgs/update-allowed-login-methods

/langsmith/langsmith-platform-openapi.json patch /api/v1/orgs/current/login-methods
Update allowed login methods for the current organization.

# Update Current Org Member
Source: https://docs.langchain.com/langsmith/smith-api/orgs/update-current-org-member

/langsmith/langsmith-platform-openapi.json patch /api/v1/orgs/current/members/{identity_id}
This is used for updating a user's role (all auth modes) or full_name/password (basic auth)

# Update Current Organization Info
Source: https://docs.langchain.com/langsmith/smith-api/orgs/update-current-organization-info

/langsmith/langsmith-platform-openapi.json patch /api/v1/orgs/current/info

# Update Current User
Source: https://docs.langchain.com/langsmith/smith-api/orgs/update-current-user

/langsmith/langsmith-platform-openapi.json patch /api/v1/orgs/members/basic
Update a user's full_name/password (basic auth only)

# Update Org Service Key
Source: https://docs.langchain.com/langsmith/smith-api/orgs/update-org-service-key

/langsmith/langsmith-platform-openapi.json patch /api/v1/orgs/current/service-keys/{api_key_id}
Update an API key's role(s) in place without rotating the key.

Restricted to org admins (ORGANIZATION_MANAGE). Applies to both
org-scoped and workspace-scoped keys listed in /orgs/current/service-keys.

# Update Organization Roles
Source: https://docs.langchain.com/langsmith/smith-api/orgs/update-organization-roles

/langsmith/langsmith-platform-openapi.json patch /api/v1/orgs/current/roles/{role_id}

# Update Sso Settings
Source: https://docs.langchain.com/langsmith/smith-api/orgs/update-sso-settings

/langsmith/langsmith-platform-openapi.json patch /api/v1/orgs/current/sso-settings/{id}
Update SSO provider settings defaults for the current organization.

# Upsert Ttl Settings
Source: https://docs.langchain.com/langsmith/smith-api/orgs/upsert-ttl-settings

/langsmith/langsmith-platform-openapi.json put /api/v1/orgs/ttl-settings

# Add Repo Owner
Source: https://docs.langchain.com/langsmith/smith-api/ownerships/add-repo-owner

/langsmith/langsmith-platform-openapi.json post /api/v1/repos/{owner}/{repo}/owners
Add an owner to a repo.

Requires being an existing owner of the repo.

# List Repo Owners
Source: https://docs.langchain.com/langsmith/smith-api/ownerships/list-repo-owners

/langsmith/langsmith-platform-openapi.json get /api/v1/repos/{owner}/{repo}/owners
List all owners of a repo.

Requires read permission on the repo.

# Remove Repo Owner
Source: https://docs.langchain.com/langsmith/smith-api/ownerships/remove-repo-owner

/langsmith/langsmith-platform-openapi.json delete /api/v1/repos/{owner}/{repo}/owners
Remove an owner from a repo.

Requires being an existing owner of the repo.

# Create Playground Settings
Source: https://docs.langchain.com/langsmith/smith-api/playground-settings/create-playground-settings

/langsmith/langsmith-platform-openapi.json post /api/v1/playground-settings
Create playground settings.

# Delete Playground Settings
Source: https://docs.langchain.com/langsmith/smith-api/playground-settings/delete-playground-settings

/langsmith/langsmith-platform-openapi.json delete /api/v1/playground-settings/{playground_settings_id}
Delete playground settings.

# Get Playground Settings
Source: https://docs.langchain.com/langsmith/smith-api/playground-settings/get-playground-settings

/langsmith/langsmith-platform-openapi.json get /api/v1/playground-settings/{playground_settings_id}
Get a single playground settings by ID.

# List Playground Settings
Source: https://docs.langchain.com/langsmith/smith-api/playground-settings/list-playground-settings

/langsmith/langsmith-platform-openapi.json get /api/v1/playground-settings
Get all playground settings for this tenant id.

# Update Playground Settings
Source: https://docs.langchain.com/langsmith/smith-api/playground-settings/update-playground-settings

/langsmith/langsmith-platform-openapi.json patch /api/v1/playground-settings/{playground_settings_id}
Update playground settings.

# Create Prompt Webhook
Source: https://docs.langchain.com/langsmith/smith-api/prompt-webhooks/create-prompt-webhook

/langsmith/langsmith-platform-openapi.json post /api/v1/prompt-webhooks
Create a new prompt webhook.

# Delete Prompt Webhook
Source: https://docs.langchain.com/langsmith/smith-api/prompt-webhooks/delete-prompt-webhook

/langsmith/langsmith-platform-openapi.json delete /api/v1/prompt-webhooks/{webhook_id}
Delete a specific prompt webhook.

# Get Prompt Webhook
Source: https://docs.langchain.com/langsmith/smith-api/prompt-webhooks/get-prompt-webhook

/langsmith/langsmith-platform-openapi.json get /api/v1/prompt-webhooks/{webhook_id}
Get a specific prompt webhook.

# List Prompt Webhooks
Source: https://docs.langchain.com/langsmith/smith-api/prompt-webhooks/list-prompt-webhooks

/langsmith/langsmith-platform-openapi.json get /api/v1/prompt-webhooks
List all prompt webhooks for the current tenant.

# Test Prompt Webhook
Source: https://docs.langchain.com/langsmith/smith-api/prompt-webhooks/test-prompt-webhook

/langsmith/langsmith-platform-openapi.json post /api/v1/prompt-webhooks/test
Test a specific prompt webhook.

# Update Prompt Webhook
Source: https://docs.langchain.com/langsmith/smith-api/prompt-webhooks/update-prompt-webhook

/langsmith/langsmith-platform-openapi.json patch /api/v1/prompt-webhooks/{webhook_id}
Update a specific prompt webhook.

# Invoke Prompt
Source: https://docs.langchain.com/langsmith/smith-api/prompts/invoke-prompt

/langsmith/langsmith-platform-openapi.json post /api/v1/prompts/invoke_prompt

# Prompt Canvas
Source: https://docs.langchain.com/langsmith/smith-api/prompts/prompt-canvas

/langsmith/langsmith-platform-openapi.json post /api/v1/prompts/canvas

# Count Shared Examples
Source: https://docs.langchain.com/langsmith/smith-api/public/count-shared-examples

/langsmith/langsmith-platform-openapi.json get /api/v1/public/{share_token}/examples/count
Count all examples by query params

# Generate Query For Shared Dataset Runs
Source: https://docs.langchain.com/langsmith/smith-api/public/generate-query-for-shared-dataset-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/public/{share_token}/datasets/runs/generate-query
Get runs in projects run over a dataset that has been shared.

# Get Message Json Schema
Source: https://docs.langchain.com/langsmith/smith-api/public/get-message-json-schema

/langsmith/langsmith-platform-openapi.json get /api/v1/public/schemas/{version}/message.json

# Get Shared Run
Source: https://docs.langchain.com/langsmith/smith-api/public/get-shared-run

/langsmith/langsmith-platform-openapi.json get /api/v1/public/{share_token}/run
Get the shared run.

# Get Shared Run By Id
Source: https://docs.langchain.com/langsmith/smith-api/public/get-shared-run-by-id

/langsmith/langsmith-platform-openapi.json get /api/v1/public/{share_token}/run/{id}
Get the shared run.

# Get Tool Def Json Schema
Source: https://docs.langchain.com/langsmith/smith-api/public/get-tool-def-json-schema

/langsmith/langsmith-platform-openapi.json get /api/v1/public/schemas/{version}/tooldef.json

# Query Shared Dataset Runs
Source: https://docs.langchain.com/langsmith/smith-api/public/query-shared-dataset-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/public/{share_token}/datasets/runs/query
Get runs in projects run over a dataset that has been shared.

# Query Shared Runs
Source: https://docs.langchain.com/langsmith/smith-api/public/query-shared-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/public/{share_token}/runs/query
Get run by ids or the shared run if not specifed.

# Read Shared Comparative Experiments
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-comparative-experiments

/langsmith/langsmith-platform-openapi.json get /api/v1/public/{share_token}/datasets/comparative
Get all comparative experiments for a given dataset.

# Read Shared Dataset
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-dataset

/langsmith/langsmith-platform-openapi.json get /api/v1/public/{share_token}/datasets
Get dataset by ids or the shared dataset if not specifed.

# Read Shared Dataset Examples With Runs
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-dataset-examples-with-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/public/{share_token}/examples/runs
Get examples with associated runs from sessions in a dataset that has been shared.

# Read Shared Dataset Feedback
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-dataset-feedback

/langsmith/langsmith-platform-openapi.json get /api/v1/public/{share_token}/datasets/feedback
Get feedback for runs in projects run over a dataset that has been shared.

# Read Shared Dataset Run
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-dataset-run

/langsmith/langsmith-platform-openapi.json get /api/v1/public/{share_token}/datasets/runs/{run_id}
Get runs in projects run over a dataset that has been shared.

# Read Shared Dataset Tracer Sessions
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-dataset-tracer-sessions

/langsmith/langsmith-platform-openapi.json get /api/v1/public/{share_token}/datasets/sessions
Get projects run on a dataset that has been shared.

# Read Shared Dataset Tracer Sessions Bulk
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-dataset-tracer-sessions-bulk

/langsmith/langsmith-platform-openapi.json get /api/v1/public/datasets/sessions-bulk
Get sessions from multiple datasets using share tokens.

# Read Shared Delta
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-delta

/langsmith/langsmith-platform-openapi.json post /api/v1/public/{share_token}/datasets/runs/delta
Fetch the number of regressions/improvements for each example in a dataset, between sessions[0] and sessions[1].

# Read Shared Delta Stream
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-delta-stream

/langsmith/langsmith-platform-openapi.json post /api/v1/public/{share_token}/datasets/runs/delta/stream
Stream feedback deltas for multiple feedback keys.

Returns results in chunks as they become available. Each chunk contains
results for one or more feedback keys. Errors for individual chunks are
included in the response rather than failing the entire operation.

Response format (SSE):
    event: data
    data: {"feedback_deltas": {"key1": {session_id: {...}}, ...}, "errors": null}

    event: data
    data: {"feedback_deltas": {"key2": {...}}, "errors": null}

    event: end

# Read Shared Examples
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-examples

/langsmith/langsmith-platform-openapi.json get /api/v1/public/{share_token}/examples
Get example by ids or the shared example if not specifed.

# Read Shared Feedbacks
Source: https://docs.langchain.com/langsmith/smith-api/public/read-shared-feedbacks

/langsmith/langsmith-platform-openapi.json get /api/v1/public/{share_token}/feedbacks

# Stats Shared Dataset Runs
Source: https://docs.langchain.com/langsmith/smith-api/public/stats-shared-dataset-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/public/{share_token}/datasets/runs/stats
Get run stats in projects run over a dataset that has been shared.

# Create Repo
Source: https://docs.langchain.com/langsmith/smith-api/repos/create-repo

/langsmith/langsmith-platform-openapi.json post /api/v1/repos
Create a repo.

# Delete Repo
Source: https://docs.langchain.com/langsmith/smith-api/repos/delete-repo

/langsmith/langsmith-platform-openapi.json delete /api/v1/repos/{owner}/{repo}
Delete a repo.

# Delete Repos
Source: https://docs.langchain.com/langsmith/smith-api/repos/delete-repos

/langsmith/langsmith-platform-openapi.json delete /api/v1/repos
Delete multiple repos with partial success support.

Returns:
    - 200: All repos deleted successfully
    - 207: Some repos deleted successfully, some failed

# Fork Repo
Source: https://docs.langchain.com/langsmith/smith-api/repos/fork-repo

/langsmith/langsmith-platform-openapi.json post /api/v1/repos/{owner}/{repo}/fork
Fork a repo.

# Get Repo
Source: https://docs.langchain.com/langsmith/smith-api/repos/get-repo

/langsmith/langsmith-platform-openapi.json get /api/v1/repos/{owner}/{repo}
Get a repo.

# List Repo Tags
Source: https://docs.langchain.com/langsmith/smith-api/repos/list-repo-tags

/langsmith/langsmith-platform-openapi.json get /api/v1/repos/tags
Get all repo tags.

# List Repos
Source: https://docs.langchain.com/langsmith/smith-api/repos/list-repos

/langsmith/langsmith-platform-openapi.json get /api/v1/repos
Get all repos.

# Optimize Prompt Job
Source: https://docs.langchain.com/langsmith/smith-api/repos/optimize-prompt-job

/langsmith/langsmith-platform-openapi.json post /api/v1/repos/optimize-job
Optimize prompt

# Update Repo
Source: https://docs.langchain.com/langsmith/smith-api/repos/update-repo

/langsmith/langsmith-platform-openapi.json patch /api/v1/repos/{owner}/{repo}
Update a repo.

# Create Rule
Source: https://docs.langchain.com/langsmith/smith-api/run/create-rule

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/rules
Create a new run rule.

# Create Run Proxy
Source: https://docs.langchain.com/langsmith/smith-api/run/create-run-proxy

/langsmith/langsmith-platform-openapi.json post /api/v1/runs
Create a new run.

# Create Runs Batch Proxy
Source: https://docs.langchain.com/langsmith/smith-api/run/create-runs-batch-proxy

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/batch
Proxy POST /runs/batch to Go backend for tests.

# Create Runs Multipart Proxy
Source: https://docs.langchain.com/langsmith/smith-api/run/create-runs-multipart-proxy

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/multipart
Proxy POST /runs/multipart to Go backend for tests.

# Delete Rule
Source: https://docs.langchain.com/langsmith/smith-api/run/delete-rule

/langsmith/langsmith-platform-openapi.json delete /api/v1/runs/rules/{rule_id}
Delete a run rule.

# Delete Runs
Source: https://docs.langchain.com/langsmith/smith-api/run/delete-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/delete
Delete specific runs by trace IDs or metadata key-value pairs.

# Delete Runs Abac
Source: https://docs.langchain.com/langsmith/smith-api/run/delete-runs-abac

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/delete/traces
Delete specific runs by trace IDs.

# Generate Query For Runs
Source: https://docs.langchain.com/langsmith/smith-api/run/generate-query-for-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/generate-query
Get runs filter expression query for a given natural language query.

# Get Last Applied Rule
Source: https://docs.langchain.com/langsmith/smith-api/run/get-last-applied-rule

/langsmith/langsmith-platform-openapi.json get /api/v1/runs/rules/{rule_id}/last_applied
Get the last applied rule.

# Group Runs
Source: https://docs.langchain.com/langsmith/smith-api/run/group-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/group
Get runs grouped by an expression

# List Rule Logs
Source: https://docs.langchain.com/langsmith/smith-api/run/list-rule-logs

/langsmith/langsmith-platform-openapi.json get /api/v1/runs/rules/{rule_id}/logs
List logs for a particular rule

# List Rule Logs V2
Source: https://docs.langchain.com/langsmith/smith-api/run/list-rule-logs-v2

/langsmith/langsmith-platform-openapi.json get /api/v1/runs/rules/{rule_id}/logs/v2
List logs for a particular rule with cursor-based pagination.

This endpoint handles S3-stored outcomes correctly by using run_outcomes_count
to predict batch sizes and avoid over-fetching.

# List Rules
Source: https://docs.langchain.com/langsmith/smith-api/run/list-rules

/langsmith/langsmith-platform-openapi.json get /api/v1/runs/rules
List all run rules.

# Query Runs
Source: https://docs.langchain.com/langsmith/smith-api/run/query-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/query

# Read Run
Source: https://docs.langchain.com/langsmith/smith-api/run/read-run

/langsmith/langsmith-platform-openapi.json get /api/v1/runs/{run_id}
Get a specific run.

# Read Run Share State
Source: https://docs.langchain.com/langsmith/smith-api/run/read-run-share-state

/langsmith/langsmith-platform-openapi.json get /api/v1/runs/{run_id}/share
Get the state of sharing of a run.

# Share Run
Source: https://docs.langchain.com/langsmith/smith-api/run/share-run

/langsmith/langsmith-platform-openapi.json put /api/v1/runs/{run_id}/share
Share a run.

# Stats Group Runs
Source: https://docs.langchain.com/langsmith/smith-api/run/stats-group-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/group/stats
Get stats for the grouped runs.

# Stats Runs
Source: https://docs.langchain.com/langsmith/smith-api/run/stats-runs

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/stats
Get all runs by query in body payload.

# Thread Preview
Source: https://docs.langchain.com/langsmith/smith-api/run/thread-preview

/langsmith/langsmith-platform-openapi.json get /api/v1/runs/threads/{thread_id}
Get preview of a thread.

# Trigger Rule
Source: https://docs.langchain.com/langsmith/smith-api/run/trigger-rule

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/rules/{rule_id}/trigger
Trigger a run rule manually.

# Trigger Rules
Source: https://docs.langchain.com/langsmith/smith-api/run/trigger-rules

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/rules/trigger
Trigger an array of run rules manually.

# Unshare Run
Source: https://docs.langchain.com/langsmith/smith-api/run/unshare-run

/langsmith/langsmith-platform-openapi.json delete /api/v1/runs/{run_id}/share
Unshare a run.

# Update Rule
Source: https://docs.langchain.com/langsmith/smith-api/run/update-rule

/langsmith/langsmith-platform-openapi.json patch /api/v1/runs/rules/{rule_id}
Update a run rule.

# Update Run
Source: https://docs.langchain.com/langsmith/smith-api/run/update-run

/langsmith/langsmith-platform-openapi.json patch /api/v1/runs/{run_id}
Update a run.

# Validate Rule
Source: https://docs.langchain.com/langsmith/smith-api/run/validate-rule

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/rules/validate
Validate a rule by executing it with test data without creating a saved rule.

This endpoint allows testing LLM-as-judge evaluators before saving them. It accepts
a rule configuration (same as rule creation) and test data, executes the evaluator,
and returns the evaluation results in the same format as batch_invoke_evaluator.

Only LLM-as-judge rules (evaluators) are supported. Code evaluators are not allowed.

The evaluator execution traces are written to the database (in the "evaluators"
project), which allows users to see the evaluator execution history.

# Validate Runs Query
Source: https://docs.langchain.com/langsmith/smith-api/run/validate-runs-query

/langsmith/langsmith-platform-openapi.json post /api/v1/runs/query/validate
Validate runs query syntax, returns errors for broken queries.

# Create a Run
Source: https://docs.langchain.com/langsmith/smith-api/runs/create-a-run

/langsmith/langsmith-platform-openapi.json post /runs
Queues a single run for ingestion. The request body must be a JSON-encoded run object that follows the Run schema.

# Ingest Runs (Batch JSON)
Source: https://docs.langchain.com/langsmith/smith-api/runs/ingest-runs-batch-json

/langsmith/langsmith-platform-openapi.json post /runs/batch
Ingests a batch of runs in a single JSON payload. The payload must have `post` and/or `patch` arrays containing run objects.
Prefer this endpoint over single‑run ingestion when submitting hundreds of runs, but `/runs/multipart` offers better handling for very large fields and attachments.

# Ingest Runs (Multipart)
Source: https://docs.langchain.com/langsmith/smith-api/runs/ingest-runs-multipart

/langsmith/langsmith-platform-openapi.json post /runs/multipart
Ingests multiple runs, feedback objects, and binary attachments in a single `multipart/form-data` request.
**Part‑name pattern**: `<event>.<run_id>[.<field>]` where `event` ∈ {`post`, `patch`, `feedback`, `attachment`}.
* `post|patch.<run_id>` – JSON run payload.
* `post|patch.<run_id>.<field>` – out‑of‑band run data (`inputs`, `outputs`, `events`, `error`, `extra`, `serialized`).
* `feedback.<run_id>` – JSON feedback payload (must include `trace_id`).
* `attachment.<run_id>.<filename>` – arbitrary binary attachment stored in S3.
**Headers**: every part must set `Content-Type` **and** either a `Content-Length` header or `length` parameter. Per‑part `Content-Encoding` is **not** allowed; the top‑level request may be `Content-Encoding: gzip` or `Content-Encoding: zstd`.
**Best performance** for high‑volume ingestion.

# Update a Run
Source: https://docs.langchain.com/langsmith/smith-api/runs/update-a-run

/langsmith/langsmith-platform-openapi.json patch /runs/{run_id}
Updates a run identified by its ID. The body should contain only the fields to be changed; unknown fields are ignored.

# Batch delete sandboxes
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/batch-delete-sandboxes

/langsmith/langsmith-platform-openapi.json post /v2/sandboxes/boxes/batch-delete
Delete multiple sandboxes by name or UUID in a single request.

# Capture a snapshot from a sandbox
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/capture-a-snapshot-from-a-sandbox

/langsmith/langsmith-platform-openapi.json post /v2/sandboxes/boxes/{name}/snapshot
Create a snapshot by capturing the current state of a sandbox or promoting an existing checkpoint.

# Create a sandbox
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/create-a-sandbox

/langsmith/langsmith-platform-openapi.json post /v2/sandboxes/boxes
Create a new sandbox from a snapshot. Provide at most one of `snapshot_id` or `snapshot_name`; if neither is provided, the server uses the default static blueprint.

# Create a snapshot
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/create-a-snapshot

/langsmith/langsmith-platform-openapi.json post /v2/sandboxes/snapshots
Create a snapshot from a Docker image (async build).

# Delete a sandbox
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/delete-a-sandbox

/langsmith/langsmith-platform-openapi.json delete /v2/sandboxes/boxes/{name}
Delete a sandbox by name or UUID. Tears down the sandbox runtime and removes the DB record.

# Delete a snapshot
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/delete-a-snapshot

/langsmith/langsmith-platform-openapi.json delete /v2/sandboxes/snapshots/{snapshot_id}
Delete a snapshot by ID. The underlying storage is reclaimed asynchronously.

# Download a sandbox file
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/download-a-sandbox-file

/langsmith/langsmith-platform-openapi.json get /v2/sandboxes/{sandbox_id}/download
Download file contents from a sandbox filesystem path.

# Execute a sandbox command
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/execute-a-sandbox-command

/langsmith/langsmith-platform-openapi.json post /v2/sandboxes/{sandbox_id}/execute
Execute a command inside a sandbox and return stdout, stderr, and exit code.

# Execute a sandbox command over WebSocket
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/execute-a-sandbox-command-over-websocket

/langsmith/langsmith-platform-openapi.json get /v2/sandboxes/{sandbox_id}/execute/ws
Open a WebSocket connection for streaming command execution inside a sandbox.

# Generate a service access token
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/generate-a-service-access-token

/langsmith/langsmith-platform-openapi.json post /v2/sandboxes/boxes/{name}/service-url
Create a short-lived JWT for accessing an HTTP service running on a specific port inside a sandbox. Returns a browser_url (sets auth cookie via redirect), a service_url (for use with the X-Langsmith-Sandbox-Service-Token header), the raw token, and its expiry.

# Get a sandbox
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/get-a-sandbox

/langsmith/langsmith-platform-openapi.json get /v2/sandboxes/boxes/{name}
Retrieve a sandbox by name. Stale provisioning sandboxes are auto-failed.

# Get a snapshot
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/get-a-snapshot

/langsmith/langsmith-platform-openapi.json get /v2/sandboxes/snapshots/{snapshot_id}
Get a sandbox snapshot by ID.

# Get sandbox access decision
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/get-sandbox-access-decision

/langsmith/langsmith-platform-openapi.json get /auth/sandbox-access
Combines authn + per-sandbox authz for runtime access. Returns the caller's PublicAuthInfo on allow (HTTP 200) or a 403 with the deny reason on deny.

# Get sandbox resource usage
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/get-sandbox-resource-usage

/langsmith/langsmith-platform-openapi.json get /v2/sandboxes/usage
Get current sandbox resource usage and quota limits for the workspace

# Get sandbox status
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/get-sandbox-status

/langsmith/langsmith-platform-openapi.json get /v2/sandboxes/boxes/{name}/status
Retrieve the lightweight status of a sandbox for polling.

# List sandboxes
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/list-sandboxes

/langsmith/langsmith-platform-openapi.json get /v2/sandboxes/boxes
List sandboxes for the authenticated tenant, with optional filtering, sorting, and pagination.

# List snapshots
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/list-snapshots

/langsmith/langsmith-platform-openapi.json get /v2/sandboxes/snapshots
List sandbox snapshots for the authenticated tenant, with optional filtering, sorting, and pagination.

# Open a sandbox TCP tunnel
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/open-a-sandbox-tcp-tunnel

/langsmith/langsmith-platform-openapi.json get /v2/sandboxes/{sandbox_id}/tunnel
Open a WebSocket tunnel to a specific port inside a sandbox.

# Start a sandbox
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/start-a-sandbox

/langsmith/langsmith-platform-openapi.json post /v2/sandboxes/boxes/{name}/start
Start a stopped or failed sandbox. This endpoint is not idempotent.

# Stop a sandbox
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/stop-a-sandbox

/langsmith/langsmith-platform-openapi.json post /v2/sandboxes/boxes/{name}/stop
Stop a ready sandbox. This endpoint is not idempotent; the filesystem is preserved for later restart.

# Update a sandbox
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/update-a-sandbox

/langsmith/langsmith-platform-openapi.json patch /v2/sandboxes/boxes/{name}
Update a sandbox's display name. The name must be unique within the tenant.

# Upload a sandbox file
Source: https://docs.langchain.com/langsmith/smith-api/sandboxes/upload-a-sandbox-file

/langsmith/langsmith-platform-openapi.json post /v2/sandboxes/{sandbox_id}/upload
Upload a file to a sandbox filesystem path.

# Create a SCIM token
Source: https://docs.langchain.com/langsmith/smith-api/scim-tokens/create-a-scim-token

/langsmith/langsmith-platform-openapi.json post /v1/platform/orgs/current/scim/tokens
Create a new SCIM bearer token for the current organization. The full token value is only returned once upon creation.

# Delete a SCIM token
Source: https://docs.langchain.com/langsmith/smith-api/scim-tokens/delete-a-scim-token

/langsmith/langsmith-platform-openapi.json delete /v1/platform/orgs/current/scim/tokens/{scim_token_id}
Delete a SCIM bearer token from the current organization.
