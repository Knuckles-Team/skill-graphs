* **Consistent access control**: User attributes and group memberships are synchronized between systems.
* **Scaling team access control**: Efficiently manage large teams with many workspaces and custom roles.
* **Role assignment**: Select specific [Organization Roles](/langsmith/rbac#organization-roles) and [Workspace Roles](/langsmith/rbac#workspace-roles) for groups of users.

### Requirements

#### Prerequisites

* Your organization must be on an Enterprise plan.
* Your Identity Provider (IdP) must support SCIM 2.0.
* Only [Organization Admins](/langsmith/administration-overview#organization-roles) can configure SCIM.
* For cloud customers: [SAML SSO](#set-up-saml-sso-for-your-organization) must be configurable for your organization.
* For self-hosted customers: [OAuth with Client Secret](/langsmith/self-host-sso#with-client-secret-recommended) authentication mode must be enabled.
* For self-hosted customers, network traffic must be allowed from the identity provider to LangSmith:
  * Microsoft Entra ID supports allowlisting IP ranges or an agent-based solution to provide connectivity.
    ([details](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups#ip-ranges)).
  * Okta supports allow-listing IPs or domains ([details](https://help.okta.com/en-us/content/topics/security/ip-address-allow-listing.htm))
    or an agent-based solution ([details](https://help.okta.com/en-us/content/topics/provisioning/opp/opp-main.htm)) to provide connectivity.

<Note>
  SCIM connections typically require HTTP/1.1 or later. If your client uses HTTP/1.0, you may encounter a `426 Upgrade Required` error.
</Note>

#### Role precedence

When a user belongs to multiple groups for the same workspace, the following precedence applies:

1. **Organization Admin groups** take highest precedence. Users in these groups will be `Admin` in all workspaces.
2. **Most recently created workspace-specific group** takes precedence over other workspace groups.

<Note>
  When a group is deleted or a user is removed from a group, their access is updated according to their remaining group membership, following the precedence rules.

  SCIM group membership overrides manually assigned roles or roles assigned via Just-in-time (JIT) provisioning. We recommend disabling JIT provisioning to avoid conflicts. For more details, refer to [Manage user access in SSO organizations](/langsmith/jit-invite-sso#scim-integration).
</Note>

#### Email verification

In cloud only, creating a new user with SCIM triggers an email to the user.
They must verify their email address by clicking the link in this email.
The link expires in 24 hours, and can be resent if needed by removing and re-adding the user via SCIM.

### Attributes and mapping

#### Group naming convention

<Warning>
  Renaming groups is **not** supported via SCIM. Group names are persistent because they must match role names and/or workspace names in LangSmith.
</Warning>

Group membership maps to LangSmith workspace membership and workspace roles with a specific naming convention. By default, the separator between components is a colon (`:`), but you can [configure a custom separator](#configure-custom-separator) for your organization.

<Note>
  You can omit spaces in the **organization role name** portion of a group name. This helps with identity providers that disallow spaces in group names. For example, LangSmith accepts `OrganizationAdmins` and `OrganizationUser` as equivalents of `Organization Admins` and `Organization User`. This flexibility applies only to the organization role name token. Workspace names and workspace role names treat spaces as literal characters, so space-omitted variants do not match their spaced counterparts.
</Note>

**Organization Admin Groups**

Format: `<optional_prefix>Organization Admin` or `<optional_prefix>Organization Admins`

Examples:

* `LS:Organization Admins`
* `LS:OrganizationAdmins` (spaces omitted—useful for IdPs that disallow spaces in group names)
* `Groups-Organization Admins`
* `Organization Admin`

**Workspace-Specific Groups**

Format: `<optional_prefix><org_role_name><separator><workspace_name><separator><workspace_role_name>`

The separator defaults to `:` (colon). Supported separators are: `:` (colon), `-` (hyphen), `_` (underscore), ` ` (space), `&` (ampersand).

Examples with default colon separator:

* `LS:Organization User:Production:Annotators`
* `LS:OrganizationUser:Production:Annotators` (spaces omitted in role name token)
* `Groups-Organization User:Engineering:Developers`
* `Organization User:Marketing:Viewers`

Examples with hyphen separator:

* `LS-Organization User-Production-Annotators`
* `LS-OrganizationUser-Production-Annotators` (spaces omitted in role name token)
* `Organization User-Engineering-Developers`

<Note>
  If your workspace names contain the separator character (e.g., workspace `my-team` with separator `-`), LangSmith will automatically try all possible splits to find a valid workspace and role combination.
</Note>

#### Configure custom separator

To change the SCIM group name separator for your organization, use the `PATCH /api/v1/orgs/current/info` [endpoint](/langsmith/smith-api/orgs/update-current-organization-info). For regional SaaS deployments, send the request to the same path on the regional host (`eu.api.smith.langchain.com`, `apac.api.smith.langchain.com`, or `aws.api.smith.langchain.com`):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X PATCH $LANGCHAIN_ENDPOINT/api/v1/orgs/current/info \
  -H "X-Api-Key: $LANGCHAIN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"scim_group_name_separator": "-"}'
```

The separator must be a single character and one of: `:` (colon), `-` (hyphen), `_` (underscore), ` ` (space), or `&` (ampersand). The default is `:` (colon).

<Note>
  Changing the separator does not rename existing SCIM groups. If you change the separator, you must also update your group names in your identity provider to use the new separator.
</Note>

### Mapping

While specific instructions depending on the identity provider may vary, these mappings show what is supported by the LangSmith SCIM integration:

#### User attributes

| **LangSmith App Attribute**    | **Identity Provider Attribute**                       | **Matching Precedence** |
| ------------------------------ | ----------------------------------------------------- | ----------------------- |
| `userName`<sup>1</sup>         | email address                                         |                         |
| `active`                       | `!deactivated`                                        |                         |
| `emails[type eq "work"].value` | email address<sup>2</sup>                             |                         |
| `name.formatted`               | `displayName` OR `givenName + familyName`<sup>3</sup> |                         |
| `givenName`                    | `givenName`                                           |                         |
| `familyName`                   | `familyName`                                          |                         |
| `externalId`                   | `sub`<sup>4</sup>                                     | 1                       |

1. `userName` is not required by LangSmith
2. Email address is required
3. Use the computed expression if your `displayName` does not match the format of `Firstname Lastname`
4. To avoid inconsistency, this should match the SAML `NameID` assertion for cloud customers, or the `sub` OAuth2.0 claim for self-hosted.

#### Group attributes

| **LangSmith App Attribute** | **Identity Provider Attribute** | **Matching Precedence** |
| --------------------------- | ------------------------------- | ----------------------- |
| `displayName`               | `displayName`<sup>1</sup>       | 1                       |
| `externalId`                | `objectId`                      |                         |
| `members`                   | `members`                       |                         |

1. Groups must follow the naming convention described in the [Group Naming Convention](#group-naming-convention) section.
   If your company has a group naming policy, you should instead map from the `description` identity provider attribute and
   set the description based on the [Group Naming Convention](#group-naming-convention) section.

### Step 1 - configure SAML SSO (Cloud only)

There are two scenarios for [SAML SSO](#set-up-saml-sso-for-your-organization) configuration:

1. If SAML SSO is already configured for your organization, you should skip the steps to initially add the application ([Add application from Okta Integration Network](#add-application-okta-oin) or [Create a new Entra ID application integration](#create-application-entra-id)), as you already have an application configured and just need to enable provisioning.
2. If you are configuring SAML SSO for the first time alongside SCIM, first follow the instructions to [set up SAML SSO](#set-up-saml-sso-for-your-organization), *then* follow the instructions here to enable SCIM.

#### NameID format

LangSmith uses the SAML NameID to identify users. The NameID is a required field in the SAML response and is case-insensitive.

The NameID must:

1. Be unique to each user.
2. Be a persistent value that never changes, such as a randomly generated unique user ID.
3. Match exactly on each sign-in attempt. It should not rely on user input.

The NameID should not be an email address or username because email addresses and usernames are more likely to change over time and can be case-sensitive.

The NameID format must be `Persistent`, unless you are using a field, like email, that requires a different format.

### Step 2 - disable JIT provisioning

Before enabling SCIM, disable [Just-in-time (JIT) provisioning](/langsmith/jit-invite-sso#jit-provisioning) to prevent conflicts between automatic and manual user provisioning.

#### Disabling JIT for cloud

Use the `PATCH /orgs/current/info` [endpoint](/langsmith/smith-api/orgs/update-current-organization-info). For regional SaaS deployments, send the request to the same path on the regional host (`eu.api.smith.langchain.com`, `apac.api.smith.langchain.com`, or `aws.api.smith.langchain.com`):

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X PATCH $LANGCHAIN_ENDPOINT/orgs/current/info \
  -H "X-Api-Key: $LANGCHAIN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"jit_provisioning_enabled": false}'
```

#### Disabling JIT for Self-Hosted

As of LangSmith chart version **0.11.14**, you can disable JIT provisioning for your self-hosted organization using SSO. To disable, set the following values:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
commonEnv:
  - name: SELF_HOSTED_JIT_PROVISIONING_ENABLED
    value: "false"
```

### Step 3 - generate SCIM bearer token

<Note>
  In self-hosted environments, the full URL below may look like `https://langsmith.yourdomain.com/api/v1/platform/orgs/current/scim/tokens` (without a subdomain, note the `/api/v1` path prefix) or `https://langsmith.yourdomain.com/subdomain/api/v1/platform/orgs/current/scim/tokens` (with a subdomain) - see the [ingress docs](/langsmith/self-host-ingress) for more details.
</Note>

Generate a SCIM Bearer Token for your organization. This token will be used by your IdP to authenticate SCIM API requests. Ensure env vars are set appropriately, for example:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X POST $LANGCHAIN_ENDPOINT/v1/platform/orgs/current/scim/tokens \
  -H "X-Api-Key: $LANGCHAIN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"description": "Your description here"}'
```

Note that the SCIM Bearer Token value is not available outside of the response to this request. These additional endpoints are present:

* `GET /v1/platform/orgs/current/scim/tokens`
* `GET /v1/platform/orgs/current/scim/tokens/{scim_token_id}`
* `PATCH /v1/platform/orgs/current/scim/tokens/{scim_token_id}` (only the `description` field is supported)
* `DELETE /v1/platform/orgs/current/scim/tokens/{scim_token_id}`

### Step 4 - configure your identity provider

<Note>
  If you use Azure Entra ID (formerly Azure AD) or Okta, there are specific instructions for identity provider setup (refer to [Azure Entra ID](#azure-entra-id-configuration-steps), [Okta](#okta)). The requirements and steps above are applicable for all identity providers.
</Note>

#### Azure entra ID configuration steps

For additional information, see Microsoft's [documentation](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/user-provisioning).

<Note>
  In self-hosted installations, the `oid` JWT claim is used as the `sub`.
  See [this Microsoft Learn link](https://learn.microsoft.com/en-us/answers/questions/5546297/how-to-link-oidc-users-with-scim)
  and [the related configuration instructions](/langsmith/self-host-sso#override-sub-claim) for additional details.
</Note>

**Step 1: Configure SCIM in your Enterprise Application**

1. Log in to the [Azure portal](https://portal.azure.com/#home) with a privileged role (e.g., `Global Administrator`).
2. Navigate to your existing LangSmith Enterprise Application.
3. In the left-side navigation, select **Manage** > **Provisioning**.
4. Click **Get started**.

**Step 2: Configure Admin credentials**

1. Under **Admin Credentials**:

   * **Tenant URL**:

     <table>
       <thead>
         <tr>
           <th>Region</th>
         </tr>
       </thead>

       <tbody>
         <tr>
           <td>GCP US</td>
         </tr>

         <tr>
           <td>GCP EU</td>
         </tr>

         <tr>
           <td>GCP APAC</td>
         </tr>

         <tr>
           <td>AWS US</td>
         </tr>
       </tbody>
     </table>

     * Self-hosted: `<langsmith_url>/scim/v2`

   * **Secret Token**: Enter the SCIM Bearer Token generated in Step 3.

2. Click **Test Connection** to verify the configuration.

3. Click **Save**.

**Step 3: Configure Attribute Mappings**

Configure the following attribute mappings under `Mappings`:

**User Attributes**

Set **Target Object Actions** to `Create` and `Update` (start with `Delete` disabled for safety):

|   **LangSmith App Attribute**  |            **Microsoft Entra ID Attribute**           | **Matching Precedence** |
| :----------------------------: | :---------------------------------------------------: | :---------------------: |
|           `userName`           |                  `userPrincipalName`                  |                         |
|            `active`            |                 `Not([IsSoftDeleted])`                |                         |
| `emails[type eq "work"].value` |                        `mail`1                        |                         |
|        `name.formatted`        | `displayName` OR `Join(" ", [givenName], [surname])`2 |                         |
|          `externalId`          |                      `objectId`3                      |            1            |

1. User's email address must be present in Entra ID.
2. Use the `Join` expression if your `displayName` does not match the format of `Firstname Lastname`.
3. To avoid inconsistency, this should match the SAML NameID assertion and the `sub` OAuth2.0 claim. For SAML SSO in cloud, the `Unique User Identifier (Name ID)` required claim should be `user.objectID` and the `Name identifier format` should be `persistent`.

**Group Attributes**

Set **Target Object Actions** to `Create` and `Update` only (start with `Delete` disabled for safety):

| **LangSmith App Attribute** | **Microsoft Entra ID Attribute** | **Matching Precedence** |
| :-------------------------: | :------------------------------: | :---------------------: |
|        `displayName`        |          `displayName`1          |            1            |
|         `externalId`        |            `objectId`            |                         |
|          `members`          |             `members`            |                         |

1. Groups must follow the naming convention described in the [Group Naming Convention](#group-naming-convention) section.
   If your company has a group naming policy, you should instead map from the `description` Microsoft Entra ID Attribute and
   set the description based on the [Group Naming Convention](#group-naming-convention) section.

**Step 4: Assign Users and Groups**

1. Under **Applications** > **Applications**, select your LangSmith Enterprise Application.
2. Under the **Assignments** tab, click **Assign** then either **Assign to People** or **Assign to Groups**.
3. Make the desired selection(s), then **Assign** and **Done**.

**Step 5: Enable Provisioning**

1. Set **Provisioning Status** to `On` under **Provisioning**.
2. Monitor the initial sync to ensure users and groups are provisioned correctly.
3. Once verified, enable `Delete` actions for both User and Group mappings.

For troubleshooting, refer to the [SAML SSO FAQs](/langsmith/faq#saml-sso-faqs). If you have issues setting up SCIM, contact the LangChain support team via [support.langchain.com](https://support.langchain.com).

#### Okta configuration steps

<Note>
  You must use the [Okta Lifecycle Management](https://www.okta.com/products/lifecycle-management/) product. This product tier is required to use SCIM on Okta.
</Note>

<div>
  <b>Supported features</b>
</div>

* Create users
* Update user attributes
* Deactivate users
* Group push (**without group renaming**)
* Import users
* Import groups

<div>
  <b>Step 1: Add application from Okta Integration Network</b>
</div>

<Note>
  If you have already configured SSO login via SAML (cloud) or OAuth2.0 with OIDC (self-hosted), skip this step.
</Note>

See [SAML SSO setup](#okta) for cloud or [OAuth2.0 setup](/langsmith/self-host-sso#okta-idp-setup) for self-hosted.

**Step 2: Configure API Integration**

1. In the General tab, ensure the `LangSmithUrl` is filled in according to the instructions from [Step 1](#add-application-okta-oin)
2. In the Provisioning tab, select `Integration`.
3. Select `Edit` then `Enable API integration`.
4. For API Token, paste the SCIM token you [generated above](#step-3-generate-scim-bearer-token).
5. Keep `Import Groups` checked.
6. To verify the configuration, select Test API Credentials.
7. Select Save.
8. After saving the API integration details, new settings tabs appear on the left. Select `To App`.
9. Select Edit.
10. Select the Enable checkbox for Create Users, Update Users, and Deactivate Users.
11. Select Save.
12. Assign users and/or groups in the Assignments tab. Assigned users are created and managed in your LangSmith group.

**Step 3: Configure User Provisioning Settings**

1. Configure provisioning: under `Provisioning > To App > Provisioning to App`, click `Edit`, then check `Create Users`, `Update User Attributes`, and `Deactivate Users`.
2. Under `<application_name> Attribute Mappings`, set the user attribute mappings as shown below, and delete the rest:

<img alt="SCIM Okta User Attributes Mapping" />

**Step 4: Push Groups**

<Note>
  Okta does not support group attributes besides the group name itself, so group name *must* follow the naming convention described in the [Group Naming Convention](#group-naming-convention) section.
</Note>

Follow Okta's [Enable Group Push](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-enable-group-push.htm) instructions to configure groups to push by name or by rule.

#### Other identity providers

Other identity providers have not been tested but may function depending on their SCIM implementation.

### SSO Groups Sync (alternative)

<Note>
  SSO Groups Sync is available for organizations on the [Enterprise plan](/langsmith/pricing-plans) with SAML SSO (cloud) or OIDC (self-hosted) configured. [Contact sales](https://www.langchain.com/contact-sales) to learn more.
</Note>

SSO Groups Sync is a simpler alternative to [SCIM](#set-up-scim-for-your-organization) for organizations that can't or prefer not to configure SCIM group push. Instead of pushing groups from your IdP to LangSmith on a separate sync interval, LangSmith reads group memberships directly from a configurable claim in the SSO token at login time and applies org-level and workspace-level role assignments using the same [naming convention](#group-naming-convention) as SCIM.

This is a well-established pattern used by GitLab (SAML Group Links), Grafana (Team Sync), HashiCorp Vault (`groups_claim`), and Atlassian (JIT group assignment).

#### When to use SSO Groups Sync vs. SCIM

SSO Groups Sync and SCIM can technically coexist (each only manages identities tagged with its own provisioning method), but we recommend choosing **one mechanism per organization**, not both, to avoid confusing precedence behavior.

|                           | SSO Groups Sync                                                             | SCIM                                                       |
| ------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **Sync trigger**          | At each SSO login                                                           | Proactive push from IdP (\~1 hour cadence)                 |
| **IdP admin involvement** | Minimal, just include groups in the SSO token                               | Required, configure SCIM provisioning app                  |
| **Deprovisioning**        | Lags until next login                                                       | Near real-time via IdP push                                |
| **Naming convention**     | Reuses [SCIM convention](#group-naming-convention)                          | [SCIM convention](#group-naming-convention)                |
| **Custom separator**      | Reuses org-level [`scim_group_name_separator`](#configure-custom-separator) | [`scim_group_name_separator`](#configure-custom-separator) |

Choose **SSO Groups Sync** when IdP admin involvement is minimal and reactive (login-time) sync is acceptable. Choose **SCIM** when proactive provisioning/deprovisioning and near real-time group membership updates are required.

#### Configuration

1. In your IdP: add the user's group memberships to the SSO token claim (default claim name: `groups`). Group names must follow the [SCIM naming convention](#group-naming-convention).
2. In LangSmith: go to **Settings** → **Members and roles** → **SSO Configuration** → **SSO Groups Sync** and configure the following:

   | Setting                                   | Description                                                                       |
   | ----------------------------------------- | --------------------------------------------------------------------------------- |
   | **Enable SSO Groups Sync**                | Automatically assign workspace roles based on group memberships in the SSO token. |
   | **Groups claim field** (default `groups`) | The claim name in the SSO token that contains group memberships.                  |
   | **Sync workspace/role assignments**       | Update workspace memberships and roles from group names on each SSO login.        |
   | **Require matching group to sign in**     | Block login if the SSO token contains no groups matching the naming convention.   |

You can also configure these settings via the API by sending a `PATCH` to the SSO settings endpoint:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -X PATCH $LANGCHAIN_ENDPOINT/api/v1/orgs/current/sso-settings/$SSO_PROVIDER_ID \
  -H "X-Api-Key: $LANGCHAIN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "sso_groups_enabled": true,
    "sso_groups_claim_field": "groups",
    "sso_groups_role_sync_enabled": true,
    "sso_groups_required": false
  }'
```

<Warning>
  Disabling SSO Groups Sync does not remove existing access. Users provisioned by SSO groups will retain their current access until their next login.
</Warning>

#### Configure your IdP to emit a groups SAML attribute (cloud)

<Note>
  This section applies to **enterprise cloud** only. Self-hosted customers configure groups directly in their OIDC IdP, see [SSO Groups Sync on self-hosted](/langsmith/self-host-sso#sso-groups-sync).
</Note>

To make a user's group memberships visible to LangSmith at login, you need to do two things:

1. Configure your IdP's SAML application to emit a multi-valued group attribute.
2. Add a matching entry to [Supabase Attribute Mapping](#supabase-attribute-mapping) so the attribute flows through to the JWT (with **Array** checked).

**Requirements:**

* The IdP attribute name (e.g., `groups`) must match both the **Supabase Attribute Mapping** entry and the **Groups claim field** value (default `groups`).
* The attribute must be **multi-valued** (a list of strings), not a single delimited string. If your IdP only supports single-valued attributes, you'll need to emit one attribute statement per group.
* Each value must be a group name following the [SCIM naming convention](#group-naming-convention).
* Only groups whose names match the convention are processed. LangSmith ignores groups that don't match its naming convention, such as org-wide directory groups or app assignment groups. You don't need to filter these out on the IdP side—emit all groups and LangSmith will skip the irrelevant ones.
