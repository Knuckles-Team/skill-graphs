# Organization and workspace operations reference
Source: https://docs.langchain.com/langsmith/organization-workspace-operations

This page provides a comprehensive reference table of [workspace](/langsmith/administration-overview#workspaces) and [organization](/langsmith/administration-overview#organizations) operations and which roles can perform them.

The list includes API operations in LangSmith along with:

* Which system roles can perform each operation.
* The specific permission string required.
* Notes about partial access or special cases.

<Info>
  For an overview of LangSmith's RBAC system, role definitions, and permission concepts, refer to [Role-based access control](/langsmith/rbac).
</Info>

## Contents

| Organization-level operations                                                                                                                                                                                                                                                                               | Workspace-level operations                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Core management:**<br />• [Organization settings](#organization-settings): Org info and configuration<br />• [Workspaces](#workspaces): Workspace management<br />• [Organization members](#organization-members): Member management<br />• [Roles and permissions](#roles-and-permissions): Custom roles | **Core resources:**<br />• [Projects](#projects): Organize traces and runs<br />• [Runs](#runs): Individual execution traces<br />• [Datasets](#datasets): Test datasets for evaluation<br />• [Examples](#examples): Individual dataset examples<br />• [Experiments](#experiments): Comparative experiments |
| **Security and authentication:**<br />• [SSO and authentication](#sso-and-authentication): Single sign-on setup<br />• [SCIM](#scim): Identity provisioning<br />• [Access policies](#access-policies): Attribute-based access control                                                                      | **Monitoring and analysis:**<br />• [Rules](#rules): Automated run rules<br />• [Alerts](#alerts): Alert rules for monitoring<br />• [Feedback](#feedback): Scores and labels on outputs<br />• [Annotation Queues](#annotation-queues): Human review queues<br />• [Charts](#charts): Custom visualizations  |
| **Billing and accounts:**<br />• [Billing and payments](#billing-and-payments): Subscription management<br />• [API keys](#api-keys): Org-level keys                                                                                                                                                        | **Development and configuration:**<br />• [Prompts](#prompts): Prompt templates (LangChain Hub)<br />• [Deployments](#deployments): Deployment configurations<br />• [MCP Servers](#mcp-servers): Model Context Protocol servers<br />• [Fleet](#fleet): Fleet admin operations                               |
| **Analytics:**<br />• [Charts and dashboards](#organization-charts-and-dashboards): Org-level visualizations<br />• [Usage and analytics](#usage-and-analytics): Usage tracking and TTL settings                                                                                                            | **Workspace management:**<br />• [Workspace settings](#workspace-settings-and-management): Members, settings<br />• [Tags](#tags): Metadata tagging system<br />• [Bulk Exports](#bulk-exports): Data export operations                                                                                       |

**Additional information:**

* [User-level operations](#user-level-operations): Operations for all authenticated users
* [Permission inheritance](#permission-inheritance): How roles inherit across org/workspaces

## Legend

* ✓ **Allowed**: User with this role can perform this action
* ✗ **Not Allowed**: User with this role cannot perform this action
* ⚠ **Partial**: User has limited access (see notes)

## Organization-level operations

<Info>
  Organization-level operations are controlled by organization roles, which are separate from the RBAC feature. Learn more in the [Role-based access control](/langsmith/rbac#organization-roles) guide.
</Info>

### Organization settings

| Operation                   | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| --------------------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| View organization info      |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| View organization dashboard |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Update organization info    |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| View billing info           |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| View company info           |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Set company info            |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### Workspaces

Organization-level workspace management operations.

| Operation           | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ------------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| List all workspaces |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create workspace    |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### Organization members

| Operation                       | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   | Notes                                                  |
| ------------------------------- | :-------: | :----------: | :------: | :--------: | --------------------- | ------------------------------------------------------ |
| View organization members       |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |                                                        |
| View active org members         |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |                                                        |
| View pending org members        |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |                                                        |
| Invite member to organization   |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator can only invite Org Users and Org Viewers |
| Invite members (batch)          |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator can only invite Org Users and Org Viewers |
| Add basic auth members          |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator can only add Org Users and Org Viewers    |
| Remove organization member      |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator cannot remove Org Admins                  |
| Update organization member role |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator can only modify Org Users and Org Viewers |
| Delete pending org member       |     ✓     |       ⚠      |     ✗    |      ✗     | `organization:manage` | Org Operator cannot delete pending Org Admin invites   |

### Roles and permissions

| Operation                  | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| -------------------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| List organization roles    |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| List available permissions |     ✓     |       ✓      |     ✓    |      ✓     | N/A (user-level)      |
| Create custom role         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Update custom role         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete custom role         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### SSO and authentication

| Operation                    | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ---------------------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| View SSO settings            |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create SSO settings          |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Update SSO settings          |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete SSO settings          |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| View login methods           |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Update allowed login methods |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Set default SSO provision    |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### SCIM

System for Cross-domain Identity Management for user provisioning.

| Operation         | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ----------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| List SCIM tokens  |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Get SCIM token    |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create SCIM token |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Update SCIM token |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete SCIM token |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### Access policies

Attribute-based access control (ABAC) policies for fine-grained permissions.

| Operation                    | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ---------------------------- | :-------: | :----------: | :------: | :--------: | --------------------- |
| List access policies         |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Get access policy            |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create access policy         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete access policy         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Attach access policy to role |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### Billing and payments

| Operation                      | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ------------------------------ | :-------: | :----------: | :------: | :--------: | --------------------- |
| Create Stripe setup intent     |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Handle payment method creation |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Change payment plan            |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Create Stripe checkout session |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Confirm checkout completion    |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Create Stripe account links    |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |

### API keys

| Operation                                          | Org Admin | Org Operator | Org User | Org Viewer | Required Permission                                |
| -------------------------------------------------- | :-------: | :----------: | :------: | :--------: | -------------------------------------------------- |
| List org-scoped service keys                       |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`                                |
| Create org-scoped service key (workspace-scoped)\* |     ✓     |       ✓      |     ⚠    |      ✗     | `organization:pats:create`                         |
| Create org-scoped service key (org-wide)\*         |     ✓     |       ✗      |     ✗    |      ✗     | `organization:pats:create` + `organization:manage` |
| Update service key role                            |     ✓     |       ✗      |     ✗    |      ✗     | `organization:manage`                              |
| List personal access tokens (PATs)                 |     ✓     |       ✓      |     ✓    |      ✗     | `organization:read`                                |
| Create personal access token (PAT)                 |     ✓     |       ✓      |     ✓    |      ✗     | `organization:pats:create`                         |
| Delete personal access token (PAT)                 |     ✓     |       ✓      |     ✓    |      ✗     | `organization:read`                                |

<Note>
  \* Organization Operators and Organization Users can create workspace-scoped service keys only for workspaces where they are a Workspace Admin. Org-wide service keys require the Organization Admin role.
</Note>

### Organization charts and dashboards

| Operation                | Org Admin | Org Operator | Org User | Org Viewer | Required Permission   |
| ------------------------ | :-------: | :----------: | :------: | :--------: | --------------------- |
| List org charts          |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Get org chart by ID      |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create org chart         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Update org chart         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete org chart         |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Render org chart         |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Get org chart section    |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |
| Create org chart section |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Update org chart section |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Delete org chart section |     ✓     |       ✓      |     ✗    |      ✗     | `organization:manage` |
| Render org chart section |     ✓     |       ✓      |     ✓    |      ✓     | `organization:read`   |

### Usage and analytics

| Operation                                                            | Org Admin | Org Operator | Org User |      Org Viewer     | Required Permission   |
| -------------------------------------------------------------------- | :-------: | :----------: | :------: | :-----------------: | --------------------- |
| View organization usage                                              |     ✓     |       ✓      |     ✓    |          ✓          | `organization:read`   |
| [View granular billable usage](/langsmith/granular-usage)            |     ✓     |       ✓      |     ✓    | `organization:read` |                       |
| [Export granular usage as CSV](/langsmith/granular-usage#csv-export) |     ✓     |       ✓      |     ✓    | `organization:read` |                       |
| View workspace trace retention settings                              |     ✓     |       ✓      |     ✓    |          ✓          | `organization:read`   |
| Set workspace default trace tier (base/extended)                     |     ✓     |       ✓      |     ✗    |          ✗          | `organization:manage` |
| Set workspace extended retention duration (Enterprise)               |     ✓     |       ✓      |     ✗    |          ✗          | `organization:manage` |

## Workspace-level operations

These operations are controlled by [workspace-level roles and permissions](/langsmith/rbac#workspace-roles).

<Tip>
  To understand what each role means and their overall capabilities, refer to the [Role-based access control](/langsmith/rbac) guide.
</Tip>

### Projects

Projects organize traces and runs from your LLM applications.

| Operation                                          | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission              |
| -------------------------------------------------- | :-------------: | :--------------: | :--------------: | -------------------------------- |
| Create a new project                               |        ✓        |         ✗        |         ✗        | `projects:create`                |
| View project list                                  |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| View project details                               |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| View prebuilt dashboard                            |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| View project metadata (top K values)               |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| Update project metadata (name, description, tags)  |        ✓        |         ✓        |         ✗        | `projects:update`                |
| Increase project trace retention (base → extended) |        ✓        |         ✓        |         ✗        | `projects:increase-trace-tier`\* |
| Decrease project trace retention (extended → base) |        ✓        |         ✓        |         ✗        | `projects:decrease-trace-tier`\* |
| Create filter view                                 |        ✓        |         ✗        |         ✗        | `projects:create`                |
| View filter views                                  |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| View specific filter view                          |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| Update filter view                                 |        ✓        |         ✓        |         ✗        | `projects:update`                |
| Delete filter view                                 |        ✓        |         ✗        |         ✗        | `projects:delete`                |
| Delete a project                                   |        ✓        |         ✗        |         ✗        | `projects:delete`                |
| Delete multiple projects                           |        ✓        |         ✗        |         ✗        | `projects:delete`                |
| Get insights jobs (Beta)                           |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| Get specific insights job (Beta)                   |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| Create insights job (Beta)                         |        ✓        |         ✓        |         ✓        | `projects:read` + `rules:create` |
| Update insights job (Beta)                         |        ✓        |         ✓        |         ✗        | `projects:update`                |
| Delete insights job (Beta)                         |        ✓        |         ✗        |         ✗        | `projects:delete`                |
| Get insights job configs (Beta)                    |        ✓        |         ✓        |         ✓        | `rules:read`                     |
| Create insights job config (Beta)                  |        ✓        |         ✓        |         ✗        | `rules:create`                   |
| Auto-generate insights job config (Beta)           |        ✓        |         ✓        |         ✗        | `rules:create`                   |
| Update insights job config (Beta)                  |        ✓        |         ✓        |         ✗        | `rules:update`                   |
| Delete insights job config (Beta)                  |        ✓        |         ✓        |         ✗        | `rules:delete`                   |
| Get run cluster from insights job (Beta)           |        ✓        |         ✓        |         ✓        | `projects:read`                  |
| Get runs from insights job (Beta)                  |        ✓        |         ✓        |         ✓        | `projects:read`                  |

<Note>
  \* `projects:increase-trace-tier` and `projects:decrease-trace-tier` are independent and can be granted separately in custom roles. For example, you can allow a role to decrease retention without allowing it to increase retention. If a user lacks both permissions, the retention settings UI is hidden entirely. If they have only one, the UI is partially enabled (the disallowed direction is disabled).
</Note>

### Runs

Individual execution traces and spans from your LLM applications.

| Operation                                                              | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ---------------------------------------------------------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| Send traces from SDK (includes single run, batch, multipart, and OTEL) |        ✓        |         ✓        |         ✗        | `runs:create`       |
| View a specific run                                                    |        ✓        |         ✓        |         ✓        | `runs:read`         |
| View thread preview                                                    |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Query/list runs                                                        |        ✓        |         ✓        |         ✓        | `runs:read`         |
| View run statistics                                                    |        ✓        |         ✓        |         ✓        | `runs:read`         |
| View grouped run statistics                                            |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Group runs by expression                                               |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Generate filter query from natural language                            |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Prefetch runs                                                          |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Update a run (PATCH)                                                   |        ✓        |         ✓        |         ✗        | `runs:create`       |
| View run sharing state                                                 |        ✓        |         ✓        |         ✓        | `runs:read`         |
| Share a run publicly                                                   |        ✓        |         ✓        |         ✗        | `runs:share`        |
| Unshare a run                                                          |        ✓        |         ✓        |         ✗        | `runs:share`        |
| Delete runs by trace ID or metadata                                    |        ✓        |         ✗        |         ✗        | `runs:delete`       |

### Rules

Automated run rules that trigger actions based on run conditions.

| Operation               | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ----------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List all run rules      |        ✓        |         ✓        |         ✓        | `rules:read`        |
