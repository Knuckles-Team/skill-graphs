
**Per-IdP setup:**

<Tabs>
  <Tab title="Okta">
    In the LangSmith SAML application:

    1. **Directory** → **Profile Editor** → select the LangSmith application's user profile.
    2. Add a custom attribute named `groups` with **Type** `string array`.
    3. **Sign On** → edit the SAML settings and add an attribute statement:
       * **Name**: `groups`
       * **Name format**: `Unspecified` (or `Basic`)
       * **Filter**: `Matches regex` with `.*` to send all groups, or use a more restrictive regex (e.g., `^LS:.*`) to limit to LangSmith-prefixed groups.
  </Tab>

  <Tab title="Entra ID (Azure)">
    In the LangSmith Enterprise Application:

    1. **Single sign-on** → **Attributes & Claims** → **Add a group claim**.
    2. Choose which groups to emit (typically **Groups assigned to the application**).
    3. Set **Source attribute** to `Cloud-only group display names` so the group name (which must match the [naming convention](#group-naming-convention)) is sent rather than the object ID.
    4. Set the claim **Name** to `groups` (or your configured **Groups claim field** value), with no namespace.
  </Tab>

  <Tab title="Google Workspace">
    Google's SAML SSO does not natively emit Google Group memberships as a SAML attribute. To use SSO Groups Sync with Google Workspace, you must either:

    * Manage group membership through a directory sync tool that exposes groups as a SAML attribute, or
    * Use [SCIM](#set-up-scim-for-your-organization) instead, which supports group push from Google Workspace.
  </Tab>
</Tabs>

#### Group naming examples

Group names follow the [SCIM naming convention](#group-naming-convention). The `<workspace_role>` segment accepts both built-in roles and [custom workspace roles](/langsmith/rbac#custom-roles) by name.

| Intent                                               | Example group name                           |
| ---------------------------------------------------- | -------------------------------------------- |
| Org admin (grants workspace admin in all workspaces) | `LS:Organization Admins`                     |
| Workspace admin in `Production`                      | `LS:Organization User:Production:Admin`      |
| Workspace editor in `Engineering`                    | `LS:Organization User:Engineering:Editor`    |
| Workspace viewer in `Marketing`                      | `LS:Organization User:Marketing:Viewer`      |
| Custom role `Annotators` in `Production`             | `LS:Organization User:Production:Annotators` |

#### Behavior

* **Naming convention**: Group names follow the same format as SCIM (e.g., `LS:Organization Admins` for org admins, `LS:Organization User:Production:Editor` for workspace-scoped). See [Group naming convention](#group-naming-convention) for the full format. The separator is configured per-org via [`scim_group_name_separator`](#configure-custom-separator) and is shared with SCIM.
* **Malformed group names**: Group names that don't match the convention are skipped silently (logged) and don't block login for valid groups.
* **Login gate**: When **Require matching group to sign in** is enabled and the SSO token contains zero matching groups, login is blocked.
* **Precedence**: SSO Groups Sync does not modify SCIM-sourced, manually assigned, or JIT-provisioned memberships. It is fully authoritative for its own assignments and replaces them on each login based on the token's group membership.
* **Org admin propagation**: If a user receives an org admin role from their groups, they are granted workspace admin in all workspaces (same as SCIM behavior).

#### Things to note

* **Deprovisioning lag**: Unlike SCIM (proactive push), SSO Groups Sync only updates on login. A user removed from a group in the IdP retains their existing workspace access until their next LangSmith login. The **Require matching group to sign in** gate mitigates this by blocking the user entirely on next login.
* **No retroactive sync**: Changing role mappings or enabling the feature does not update existing users until they log in again.
* **Naming convention required**: Customers must name their IdP groups following the SCIM convention. If your IdP groups follow a different naming policy, SCIM with `description`-based mapping (see [Group attributes](#group-attributes)) may be a better fit.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/user-management.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
