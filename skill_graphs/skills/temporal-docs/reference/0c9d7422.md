
Service Accounts use API Keys as the authentication mechanism to connect to Temporal Cloud.
You should use Service Accounts to represent a non-human identity when authenticating to Temporal Cloud for operations automation or the Temporal SDKs and the Temporal CLI for Workflow Execution and management.

For guidance on how to structure Service Accounts across services, Namespaces, and teams, see
[Managing Temporal Cloud access control](/best-practices/cloud-access-control). A common default is one Service Account
per service or worker deployment, with Namespace-scoped Service Accounts preferred when a service only needs access to a
single Namespace.

:::tip

Namespace Admins can now manage and create [Namespace-scoped Service Accounts](/cloud/service-accounts#scoped), regardless of their Account Role.

:::

## Manage Service Accounts

Account Owner and Global Admin [roles](/cloud/manage-access/roles-and-permissions#account-level-roles) can manage Service Accounts by creating, viewing, updating, deleting Service Accounts using the following tools:

- Temporal Cloud UI
- Temporal Cloud CLI (tcld)
  - Use `tcld service-account --help` for a list of all service-account commands

Account Owner and Global Admin [roles](/cloud/manage-access/roles-and-permissions#account-level-roles) also have the ability to manage API Keys for Service Accounts.

### Prerequisites

- A Cloud user account with Account Owner or Global Admin [role](/cloud/manage-access/roles-and-permissions#account-level-roles) permissions
- Access to the Temporal Cloud UI or Temporal Cloud CLI (tcld)
- Enable access to API Keys for your Account
- To manage Service Accounts using the Temporal Cloud CLI (tcld), upgrade to the latest version of tcld (v0.18.0 or higher) using `brew upgrade tcld`.
  - If using a version of tcld less than v0.31.0, enable Service Account commands with `tcld feature toggle-service-account`.

### Create a Service Account

Create a Service Account using the Temporal Cloud UI or tcld.
While User identities are invited to Temporal Cloud, Service Accounts are created in Temporal Cloud.

<Tabs groupId="service-account">
  <TabItem value="cloud-ui" label="Using the Cloud UI">

1. Go to [Settings → Identities](https://cloud.temporal.io/settings/identities)
2. Click the `Create Service Account` button located near the top of the `Identities` page
3. Provide the following information:
   - **Name** (required)
   - **Description** (optional)
   - **Account Level Role** (required)
   - **Namespace Permissions** (optional)
     - Use this section of the Create Service Account page to grant the Service Account access to individual Namespaces
4. Click `Create Service Account` at the bottom of the page
   - A status message is displayed at the bottom right corner of the screen and on the next screen
   - You will be prompted to create an API Key for the Service Account (optional)
5. (Optional) Create API Key
   - It is recommended to create an API Key for the Service Account right after you create the Service Account, though you can create/manage API Keys for Service Accounts at any time
   - See the API Key [documentation](/cloud/api-keys) for more information on creating and managing API Keys

  </TabItem>
  <TabItem value="tcld" label="Using tcld">

To create a Service Account using tcld, use the `tcld service-account create` command:

```
tcld service-account create -n "sa_test" -d "this is a test SA" --ar "Read"
```

This example creates a Service Account with the name `"sa_test"`, description `"this is a test SA"`, and a `Read` Account Role.

Creating a Service Account requires the following attributes: `name` and `account-role` (as above).
You can also provide the Namespace Permissions for the Service Account using the `—-np` flag.
Creating a Service Account returns the `ServiceAccountId` which is used to retrieve, update, or delete a Service Account.

  </TabItem>
</Tabs>

### View Service Accounts

View a single or all Service Account(s) using the Temporal Cloud UI or tcld.

<Tabs groupId="service-account">
  <TabItem value="cloud-ui" label="Using the Cloud UI">

Service Accounts are listed on the `Identities` section of the `Settings` page, along with Users.
To locate a Service Account:

1. Go to [Settings → Identities](https://cloud.temporal.io/settings/identities)
2. Select the `Service Accounts` filter

  </TabItem>
  <TabItem value="tcld" label="Using tcld">

To view all Service Accounts in your account using tcld, use the `tcld service-account list` command:

```
tcld service-account list
```

  </TabItem>
</Tabs>

### Delete a Service Account

Delete a Service Account using the Temporal Cloud UI or tcld. When you delete a Service Account, all associated API keys are automatically deleted as well.
Therefore, you don't need to manually remove API keys after deleting a Service Account.

<Tabs groupId="service-account">
  <TabItem value="cloud-ui" label="Using the Cloud UI">

1. Go to [Settings → Identities](https://cloud.temporal.io/settings/identities)
2. Find the relevant Service Account
3. Select the vertical ellipsis menu in the Service Account row
4. Select `Delete`
5. Confirm the delete action when prompted

  </TabItem>
  <TabItem value="tcld" label="Using tcld">

To delete a Service Account using tcld, use the `tcld service-account delete` command:

```
tcld service-account delete --service-account-id "e9d87418221548"
```

Use the tcld Service Account list command to validate the Service Account has been removed from the account.
The Service Account is deleted when it is no longer visible in the output of the list command.

  </TabItem>
</Tabs>

### Update a Service Account {/* #update */}

Update a Service Account using the Temporal Cloud UI or tcld.

:::note Account roles and Namespace Permissions

Service Accounts with the Account Owner or Global Admin account-level role automatically have Namespace Admin access to
all Namespaces. Do not add explicit Namespace Permissions while using either role. To move a Service Account from Global
Admin to a lower-privilege account role, update the Account Level Role and desired Namespace Permissions together.

:::

<Tabs groupId="service-account">
  <TabItem value="cloud-ui" label="Using the Cloud UI">

1. Go to [Settings → Identities](https://cloud.temporal.io/settings/identities)
2. Find the relevant Service Account
3. Select the vertical ellipsis menu in the Service Account row
4. Select `Edit`
5. Make changes to the Service Account
   - You can change the Service Account's name, description, Account Level Role, and Namespace Permissions
6. Click the `Save` button located in the bottom left of the screen
   - A status message is displayed at the bottom right corner of the screen

  </TabItem>
  <TabItem value="tcld" label="Using tcld">

Three different commands exist to help users update a Service Account using tcld:

- `tcld service-account update`: to update a Service Account's name or description field
- `tcld service-account set-account-role`: to update a Service Account's Account Role
- `tcld service-account set-namespace-permissions`: to update a Service Account's Namespace Permissions

Example:

```
tcld service-account update --id "2f68507677904e09b9bcdbf93380bb95" -d "new description"
```

  </TabItem>
</Tabs>

## Namespace-scoped Service Accounts {/* #scoped */}

There is a special type of Service Account, called a Namespace-scoped Service Account, which shares the
same functionality as the Service Accounts above, but is limited (or scoped) to a single namespace.

In particular, a Namespace-scoped Service Account must _always_ have:

- A `Read` Account Role
- A single Namespace Permission

Note that a Namespace-scoped Service Account cannot be reassigned to a different Namespace after creation, but its Namespace permission can be modified (e.g. from `Read` to `Write`).

Namespace-scoped Service Accounts are useful in situations when you need to restrict a client's access to a single Namespace.

You can retrieve, update, and delete a Namespace-scoped Service Account using the same process and commands as above, but creation is slightly different.

### Permissions
Unlike regular Service Accounts, which require a Global Admin or Account Owner role, Namespace-scoped Service Accounts can be created and managed by Namespace Admins.
For example, an Account Developer with Namespace Admin for `test_ns` can create a Service Account scoped to `test_ns`.

Global Admins and Account Owners can also create Namespace-scoped Service Accounts, as they implicitly have Namespace Admin rights for all Namespaces.

### Create a Namespace-scoped Service Account

As with regular Service Accounts, Namespace-scoped Service Accounts can be created using Temporal Cloud UI or tcld.

#### Using the Cloud UI {/* #scoped-ui */}

Currently, creating a Namespace-scoped Service Account from the Temporal Cloud UI happens on an individual [Namespace](/cloud/namespaces#manage-namespaces) page.
If the current Namespace has API key authentication enabled, then there will be a `Generate API Key` button as a banner on the top of the Namespace page or in the `Authentication` section.

By clicking on the `Generate API Key` button, a Namespace-scoped Service Account will be automatically created for the given Namespace (if one does not already exist) and an associated API key will be displayed. This key will have the maximum expiration time, which is 2 years.

The resulting Namespace-scoped Service Account will be named `<namespace>-service-account` and will have an `Admin` Namespace permission by default.

#### Using tcld

To create a Namespace-scoped Service Account with tcld, use the `tcld service-account create-scoped` command:

```
tcld service-account create-scoped -n "test-scoped-sa" --np "test-ns=Admin"
```

This example creates a Namespace-scoped Service Account for the Namespace `test-ns`, named `test-scoped-sa`, with `Admin` Namespace Permission.
Note that the Account Role is omitted, since Namespace-scoped Service Accounts always have a `Read` Account Role.

### Lifecycle

When a Namespace is deleted, all associated Namespace-scoped Service Accounts and their associated API keys are automatically deleted as well.
Therefore, you do not need to manually remove Namespace-scoped Service Accounts and their API keys after deleting a Namespace.

---

## Manage user groups

## What are user groups?

User groups can be used to help manage sets of users that should have the same
access. Instead of separately assigning the same role to individual users, a user group can be
created, assigned the desired roles, and then users added to the user group. This
eases the toil of managing individual user permissions and can simplify access management. When
a new role is needed, it can be added to the group once and all users' access will reflect the
new role.

User groups can be assigned both [account-level roles](/cloud/manage-access/roles-and-permissions#account-level-roles) and [namespace-level permissions](/cloud/manage-access/roles-and-permissions#namespace-level-permissions).

One user can be assigned to many groups. In the event that a user's group memberships have multiple roles for the same resource, the user will have an effective role of the most permissive of the permissions. For example if `Group A` grants a read-only role to a namespace, but `Group B` grants a write role to a namespace then a user that belongs to both `Group A` and `Group B` would have the write role to the namespace.

[Service accounts](/cloud/service-accounts) cannot be assigned to user groups.

Only users with the Account Owner or Global Admin account-level [role](/cloud/manage-access/roles-and-permissions#account-level-roles) can manage user groups.

## How SCIM groups work with user groups {/* #scim-groups */}

[SCIM groups](/cloud/scim) work similarly to user groups with respect to role assignment. Unlike a user group, the lifecycle of a SCIM group is fully managed by the SCIM integration which means:

1. SCIM groups cannot be created except through the SCIM integration
1. SCIM groups cannot be deleted except through the SCIM integration
1. SCIM group membership is managed through the SCIM integration

User groups and SCIM groups can be used simultaneously in a single Temporal Cloud account. One user may belong to multiple SCIM groups and to multiple user groups.

Using user group and SCIM groups together can be useful when the groups defined in the identity provider (IDP) don't map cleanly to the access you need to grant in Temporal Cloud. Instead of having to update the IDP (which is often sensitive and time-consuming), you can use Temporal Cloud user groups to manage access.

:::info

All user group administration requires an Account Owner or Global Admin account-level [role](/cloud/manage-access/roles-and-permissions#account-level-roles).

:::

## How to create a user group in your Temporal Cloud account {/* #create-group */}

User group names must be 3-64 characters long and can only contain lowercase letters, numbers, hyphens, and underscores.

<Tabs>

<TabItem value="create-group-webui" label="Web UI">

1. Navigate to the [identities page](https://cloud.temporal.io/settings/identities)
1. Click the Create Group button
1. Name the group
1. Assign an account-level role to the group (you can assign namespace-level permissions after the group is created)
1. Click Save

</TabItem>

<TabItem value="create-group-tcld" label="tcld">
See the [`tcld` user-group create](/cloud/tcld/user-group/#create) command reference for details.
</TabItem>

<TabItem value="create-group-tf" label="Terraform">
See the [Terraform provider documentation](https://registry.terraform.io/providers/temporalio/temporalcloud/latest/docs/resources/group) for details.
</TabItem>

</Tabs>

## How to assign roles to a user group {/* #assign-group-roles */}

<Tabs>
<TabItem value="assign-roles-webui" label="Web UI">

To edit the account role of a group:
  1. Navigate to the [identities page](https://cloud.temporal.io/settings/identities)
  1. Find the group to edit (You can filter the list of identities to only show groups to find the relevant group by clicking the Groups tab on the table)
  1. Click Edit Group
  1. Click the Account Role dropdown
  1. Select a new account role
  1. Click Save

To add namespace permissions to a group:
  1. Navigate to the [identities page](https://cloud.temporal.io/settings/identities)
  1. Find the group to edit (You can filter the list of identities to only show groups to find the relevant group by clicking the Groups tab on the table)
  1. Click Edit Group
  1. Click Add Namespaces
  1. Under Grant Access to a Namespace, search for the namespace you’d like to add permissions for
  1. Select the namespace
  1. Click the pencil to edit the permissions for the selected namespace
  1. Click Save

To edit or remove namespace permissions from a group:
  1. Click Edit Group
  1. Click the pencil on a permission to edit it, or the trash can to delete it
  1. Click Save

</TabItem>

<TabItem value="assign-roles-tcld" label="tcld">
See the [`tcld` user-group set-access](/cloud/tcld/user-group/#set-access) command reference for details.
</TabItem>

<TabItem value="assign-roles-tf" label="Terraform">
See the [Terraform provider documentation](https://registry.terraform.io/providers/temporalio/temporalcloud/latest/docs/resources/group) for details.
</TabItem>

</Tabs>

## How to manage users in a group {/* #assign-group-members */}

<Tabs>
<TabItem value="assign-group-members-webui" label="Web UI">

To add users to the group:
  1. Navigate to the [identities page](https://cloud.temporal.io/settings/identities)
  1. Find the group to edit (You can filter the list of identities to only show groups to find the relevant group by clicking the Groups tab on the table)
  1. Click Edit Group
  1. Under Members, search for the user you’d like to add
  1. Select the user
  1. Click Save
To remove a user from the group:
  1. Click Edit Group
  1. Under Members, click the X next to the user you’d like to remove
  1. Click Save

</TabItem>

<TabItem value="assign-group-members-tcld" label="tcld">
See the [`tcld` user-group add-users](/cloud/tcld/user-group/#add-users) and the [`tcld` user-group remove-users](/cloud/tcld/user-group/#remove-users) command reference for details.
</TabItem>

<TabItem value="assign-group-members-tf" label="Terraform">
See the [Terraform provider documentation](https://registry.terraform.io/providers/temporalio/temporalcloud/latest/docs/resources/group) for details.
</TabItem>

</Tabs>

## Delete a user group

<Tabs>
<TabItem value="delete-group-webui" label="Web UI">

  1. Navigate to the [identities page](https://cloud.temporal.io/settings/identities)
  1. Find the group to edit (You can filter the list of identities to only show groups to find the relevant group by clicking the Groups tab on the table)
  1. Click the dropdown next to the edit button
  1. Click Delete
  1. Confirm by clicking Delete

</TabItem>

<TabItem value="delete-group-tcld" label="tcld">
See the [`tcld` user-group delete](/cloud/tcld/user-group/#delete) command reference for details.
</TabItem>

<TabItem value="delete-group-tf" label="Terraform">
See the [Terraform provider documentation](https://registry.terraform.io/providers/temporalio/temporalcloud/latest/docs/resources/group) for details.
</TabItem>

</Tabs>

---

## User management

<Tabs>

<TabItem value="invite-webui" label="Web UI">

To invite users using the Temporal Cloud UI:

1. In Temporal Web UI, select **Settings** in the left portion of the window.
1. On the **Settings** page, select **Create Users** in the upper-right portion of the window.
1. On the **Create Users** page in the **Email Addresses** box, type or paste one or more email addresses.
1. In **Account-Level Role**, select a [Role](/cloud/manage-access/roles-and-permissions#account-level-roles). The Role
   applies to all users whose email addresses appear in **Email Addresses**.
1. If the account has any Namespaces, they are listed under **Grant access to Namespaces**. To add a permission, select
   the checkbox next to a Namespace, and then select a
   [permission](/cloud/manage-access/roles-and-permissions#namespace-level-permissions). Repeat as needed.
1. When all permissions are assigned, select **Send Invite**.

</TabItem>

<TabItem value="invite-tcld" label="tcld">

Use the [`tcld user invite`](/cloud/tcld/user/#invite) command. Specify the user's email, an account-level role, and
optionally one or more Namespace permissions.

Available account roles: `admin` | `developer` | `read`.

Available Namespace permissions: `Admin` | `Write` | `Read`.

```command
tcld user invite \
  --user-email <user@example.com> \
  --account-role <role> \
  --namespace-permission <namespace>=<permission>
```

You can invite multiple users and assign multiple Namespace permissions in a single command:

```command
tcld user invite \
  --user-email user1@example.com \
  --user-email user2@example.com \
  --account-role developer \
  --namespace-permission ns1=Admin \
  --namespace-permission ns2=Write
```

</TabItem>

</Tabs>

### Frequently Asked Questions

#### Can multiple Temporal Cloud accounts share the same email domain?

Yes. Multiple Temporal Cloud accounts can coexist with users from the same email domain.
Each account has its own independent SAML configuration, tied to its unique Account Id.
We recommend configuring [SAML](/cloud/saml) for each account independently.
For the smoother login experience, you can configure SAML for each account separately and use IdP-initiated login: you click the relevant app tile in your identity provider's portal to access the Temporal Cloud account associated with your email address directly.

#### Can the same email be used across different Temporal Cloud accounts?

No. Each email address can only be associated with a single Temporal Cloud account.
If you need access to multiple accounts, you’ll need a separate invite for each one using a different email address.

#### Can I use Google or Microsoft SSO after signing up with email and password?

If you originally signed up for Temporal Cloud using an email and password, you won’t be able to log in using Google or Microsoft single sign-on.

If you prefer SSO, ask your Account Owner to delete your current user and send you a new invitation.
During re-invitation, be sure to sign up using your preferred authentication method.

Use the [CreateUser](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/users) endpoint to invite a user.

```
POST /cloud/users
```

The request body includes a `spec` with the following fields:

- `spec.email` — The email address of the user to invite.
- `spec.access.account_access.role` — The account-level role to assign.
- `spec.access.namespace_accesses` — A map of Namespace names to permissions.

Available roles: `ROLE_ADMIN` | `ROLE_DEVELOPER` | `ROLE_READ` | `ROLE_OWNER` | `ROLE_FINANCE_ADMIN`.

Available Namespace permissions: `PERMISSION_ADMIN` | `PERMISSION_WRITE` | `PERMISSION_READ`.

The new users receive an email with a link to accept the invitation and complete their setup. The new user must use this
link to sign up to be added to your account unless the account has a SAML configuration. If your account has a SAML
configuration, the new user can sign in using their existing SAML credentials and be included in the account
automatically.

:::caution

The new user must use the same authentication method they originally signed up with to sign in to Temporal Cloud. If
they used single sign-on (SSO), they must use the same SSO provider to sign in to Temporal Cloud. If they used email and
password authentication, they must use the same email and password to sign in to Temporal Cloud, and cannot use SSO,
even if the underlying email address is the same.

:::

---

## Manage users

Users are one of the primary access principals in Temporal Cloud. Each user is assigned one
[account-level role](/cloud/manage-access/roles-and-permissions#account-level-roles), and each role has a set of
permissions. In addition to account-level roles, users can also be assigned
[Namespace-level permissions](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) for specific
Namespaces. Each user can only perform an action if they have a role that grants them the necessary permissions.

When you register for Temporal Cloud without joining an existing account, you are assigned the Account Owner role for a
new account. You can then invite other users to join the account and assign them roles.

## Invite users to your Temporal Cloud account {/* #invite-users */}

<InvitationContent />

Global Admin roles cannot assign the Account Owner role or the Finance Admin role to new users they invite to the
account.

## Update a user's account-level role {/* #update-roles */}

With Global Admin or Account Owner privileges, you can update any user's account-level
[role](/cloud/manage-access/roles-and-permissions#account-level-roles). The Account Owner role can only be granted by
existing Account Owners.

For security reasons, you cannot remove the Account Owner role from a user. Removing the Account Owner role must be made
through Temporal Support. To remove the Account Owner role, you must submit a
[support ticket](https://temporalsupport.zendesk.com/).

<Tabs>

<TabItem value="update-role-webui" label="Web UI">

1. In Temporal Web UI, select **Settings** in the left portion of the window.
1. On the **Settings** page, select the user.
1. On the user profile page, select **Edit User**.
1. On the **Edit User** page in **Account Level Role**, select the role.
1. Select **Save**.

</TabItem>

<TabItem value="update-role-tcld" label="tcld">

Use the [`tcld user set-account-role`](/cloud/tcld/user/#set-account-role) command. Specify the user by email or ID and
the new role.

Available account roles: `admin` | `developer` | `read`. The Account Owner and Finance Admin roles cannot be assigned
through tcld; use the Web UI or Cloud Ops API to assign these roles.

```command
tcld user set-account-role --user-email <user@example.com> --account-role <role>
```

You can also identify the user by ID:

```command
tcld user set-account-role --user-id <user-id> --account-role <role>
```

</TabItem>

<TabItem value="update-role-api" label="Cloud Ops API">

Use the [UpdateUser](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/users) endpoint to update a user's account-level
role.

```
POST /cloud/users/{userId}
```

The request body includes a `spec` with the user's `access.account_access.role` field set to the desired role.

Available roles: `ROLE_OWNER` | `ROLE_ADMIN` | `ROLE_DEVELOPER` | `ROLE_FINANCE_ADMIN` | `ROLE_READ`.

</TabItem>

</Tabs>

## Update a user's Namespace-level permissions {/* #update-permissions */}

With Account Owner, Global Admin, or Namespace Admin privileges, you can update
[Namespace-level permissions](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) for users within
Namespaces you administer. Account Owners and Global Admins have Namespace Admin permissions on all Namespaces
automatically.

<Tabs>

<TabItem value="update-perms-webui" label="Web UI">

**Update a user's permissions across multiple Namespaces:**

1. In Temporal Web UI, select **Namespaces** in the left portion of the window.
1. On the **Namespaces** page, select the Namespace.
1. If necessary, scroll down to the list of permissions.
1. On the user profile page in **Namespace permissions**, select the Namespace.
1. On the Namespace page in **Account Level Role**, select the role.
