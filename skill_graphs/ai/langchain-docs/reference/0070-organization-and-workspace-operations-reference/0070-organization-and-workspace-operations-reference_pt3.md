| Update workspace extended retention duration (Enterprise) |        ✓        |         ✗        |         ✗        | `workspaces:manage`         |
| View usage limits                                         |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| View shared entities                                      |        ✓        |         ✓        |         ✓        | `workspaces:read`           |
| Bulk unshare entities                                     |        ✓        |         ✗        |         ✗        | `workspaces:manage`         |

### Tags

| Operation                       | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ------------------------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List tag keys                   |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Get tag key                     |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Create tag key                  |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| Update tag key                  |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| Delete tag key                  |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| List tag values                 |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Get tag value                   |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Create tag value                |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| Update tag value                |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| Delete tag value                |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| List tags                       |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| List tags for resource          |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| List tags for resources (batch) |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| List taggings                   |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Create tagging                  |        ✓        |         ✗        |         ✗        | `workspaces:manage` |
| Delete tagging                  |        ✓        |         ✗        |         ✗        | `workspaces:manage` |

### Bulk exports

| Operation                      | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission   |
| ------------------------------ | :-------------: | :--------------: | :--------------: | --------------------- |
| List bulk exports              |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Get bulk export                |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Get bulk export runs           |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Get bulk export run            |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Create bulk export             |        ✓        |         ✗        |         ✗        | `bulk-exports:manage` |
| Cancel bulk export             |        ✓        |         ✗        |         ✗        | `bulk-exports:manage` |
| Get bulk export destinations   |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Get bulk export destination    |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |
| Create bulk export destination |        ✓        |         ✗        |         ✗        | `bulk-exports:manage` |
| Update bulk export destination |        ✓        |         ✗        |         ✗        | `bulk-exports:manage` |
| Get filtered export runs       |        ✓        |         ✓        |         ✓        | `bulk-exports:read`   |

<Tip>
  `bulk-exports:read` and `bulk-exports:manage` are dedicated permissions that allow you to grant export access via a [custom role](/langsmith/rbac#custom-roles) without granting the broader `workspaces:manage` scope. This is useful for security-team service keys that need to export traces but should not be able to manage workspaces, members, or secrets.
</Tip>

### MCP servers

Model Context Protocol servers for extended functionality.

| Operation         | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission |
| ----------------- | :-------------: | :--------------: | :--------------: | ------------------- |
| List MCP servers  |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Get MCP server    |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Create MCP server |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Update MCP server |        ✓        |         ✓        |         ✓        | `workspaces:read`   |
| Delete MCP server |        ✓        |         ✓        |         ✓        | `workspaces:read`   |

### Fleet

[Fleet](/langsmith/fleet/index) workspace administration operations.

| Operation                               | Workspace Admin | Workspace Editor | Workspace Viewer | Required Permission        |
| --------------------------------------- | :-------------: | :--------------: | :--------------: | -------------------------- |
| View Fleet admin section (usage, spend) |        ✓        |         ✗        |         ✗        | `fleet:read-admin-config`  |
| Manage Fleet spend limits               |        ✓        |         ✗        |         ✗        | `fleet:write-admin-config` |

## User-level operations

These operations are available to all authenticated users and don't require specific workspace or organization permissions:

* View own user profile
* Update own user profile
* List organizations for user
* Create new organization
* List pending workspace invites
* Delete pending workspace invite
* Claim pending workspace invite
* List pending organization invites
* Delete pending organization invite
* Claim pending organization invite

## Permission inheritance

### Organization to workspace

* [Organization Admin](/langsmith/rbac#organization-admin) automatically has full permissions in all workspaces.
* [Organization Operator](/langsmith/rbac#organization-operator) only gets workspace access when explicitly added to workspaces with workspace-level roles (or to workspaces they create).
* [Organization User](/langsmith/rbac#organization-user) and [Organization Viewer](/langsmith/rbac#organization-viewer) only get workspace access when explicitly added to workspaces with workspace-level roles.

For detailed role definitions, refer to [Organization roles](/langsmith/rbac#organization-roles) and [Workspace roles](/langsmith/rbac#workspace-roles).

### Workspace role independence

* Users can have different workspace roles in different workspaces.
* A user might be a [Workspace Admin](/langsmith/rbac#workspace-admin) in one workspace and a [Workspace Viewer](/langsmith/rbac#workspace-viewer) in another.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/organization-workspace-operations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
