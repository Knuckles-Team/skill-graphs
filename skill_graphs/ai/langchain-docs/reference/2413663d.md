# User management
Source: https://docs.langchain.com/langsmith/user-management

This page covers user management features in LangSmith, including access control, authentication, and automated user provisioning:

* [Set up access control](#set-up-access-control): Configure role-based access control (RBAC) to manage user permissions within workspaces, including creating custom roles and assigning them to users.
* [SAML SSO (Enterprise plan)](#set-up-saml-sso-for-your-organization): Set up Single Sign-On authentication for Enterprise customers using SAML 2.0, including configuration for popular identity providers.
* [SCIM User Provisioning (Enterprise plan)](#set-up-scim-for-your-organization): Automate user provisioning and deprovisioning between your identity provider and LangSmith using SCIM.

## Set up access control

<Note>
  RBAC (Role-Based Access Control) is a feature that is only available to Enterprise customers. If you are interested in this feature, [contact our sales team](https://www.langchain.com/contact-sales). Other plans default to using the [`Admin` role](/langsmith/administration-overview) for all users.
</Note>

<Check>
  You may find it helpful to read the [Administration overview](/langsmith/administration-overview) page before setting up access control.
</Check>

LangSmith relies on RBAC to manage user permissions within a [workspace](/langsmith/administration-overview#workspaces). This allows you to control who can access your LangSmith workspace and what they can do within it. Users with the `workspaces:manage` permission can manage workspace settings, and users with the `workspaces:manage-members` permission can add, remove, and update workspace members. The built-in Workspace Admin role includes both permissions.

For a complete reference of workspace roles and their permissions, refer to the [Role-based access control](/langsmith/rbac#workspace-roles) guide. For specific operations each role can perform, refer to the [Organization and workspace operations reference](/langsmith/organization-workspace-operations).

### Create a role

By default, LangSmith comes with a set of system roles:

* `Admin`: has full access to all resources within the workspace.
* `Viewer`: has read-only access to all resources within the workspace.
* `Editor`: has full permissions except for workspace management (adding/removing users, changing roles, configuring service keys).

If these do not fit your access model, `Organization Admins` can create custom roles to suit your needs.

To create a role, navigate to the **Roles** tab in the **Members and roles** section of the [Organization settings page](https://smith.langchain.com/settings). Note that new roles that you create will be usable across all workspaces within your organization.

Click on the **Create Role** button to create a new role. A **Create role** form will open.

<img alt="Create Role" />

Assign permissions for the different LangSmith resources that you want to control access to.

### Assign a role to a user

Once you have your roles set up, you can assign them to users. To assign a role to a user, navigate to the `Workspace members` tab in the `Workspaces` section of the [Organization settings page](https://smith.langchain.com/settings)

Each user will have a **Role** dropdown that you can use to assign a role to them.

<img alt="Assign Role" />

You can also invite new users with a given role.

<img alt="Invite User" />

## Set up SAML SSO for your organization

Single Sign-On (SSO) functionality is **available for Enterprise Cloud** customers to access LangSmith through a single authentication source. This allows administrators to centrally manage team access and keeps information more secure.

LangSmith's SSO configuration is built using the SAML (Security Assertion Markup Language) 2.0 standard. SAML 2.0 enables connecting an Identity Provider (IdP) to your organization for an easier, more secure login experience.

SSO services permit a user to use one set of credentials (for example, a name or email address and password) to access multiple applications. The service authenticates the end user only once for all the applications the user has been given rights to and eliminates further prompts when the user switches applications during the same session. The benefits of SSO include:

* Streamlines user management across systems for organization owners.
* Enables organizations to enforce their own security policies (e.g., MFA).
* Removes the need for end users to remember and manage multiple passwords. Simplifies the end-user experience, by allowing sign in at one single access point across multiple applications.

### Just-in-time (JIT) provisioning

LangSmith supports Just-in-time provisioning when using SAML SSO. This allows someone signing in via SAML SSO to join the organization and selected workspaces automatically as a member. For detailed information on managing JIT provisioning and user invites, refer to [Manage user access in SSO organizations](/langsmith/jit-invite-sso).

<Note>
  JIT provisioning only runs for new users, that is, users who do not already have access to the organization with the same email address via a [different login method](/langsmith/authentication-methods#cloud).
</Note>

### Login methods and access

Once you have completed your configuration of SAML SSO for your organization, users will be able to log in via SAML SSO in addition to [other login methods](/langsmith/authentication-methods#cloud), such as username/password or Google Authentication:

* When logged in via SAML SSO, users can only access the corresponding organization with SAML SSO configured.
* Users with SAML SSO as their only login method do not have [personal organizations](/langsmith/administration-overview#organizations).
* When logged in via any other method, users can access the organization with SAML SSO configured along with any other organizations they are a part of.

### Enforce SAML SSO only

<Note>
  User invites are not supported in organizations enforcing SAML SSO only. Initial workspace membership and role is determined by [JIT provisioning](/langsmith/jit-invite-sso#jit-provisioning), and changes afterwards can be managed in the UI.
  For additional flexibility in automated user management, LangSmith supports SCIM.
</Note>

To ensure users can only access the organization when logged in using SAML SSO and no other method, check the **Login via SSO only** checkbox and click **Save**. Once this happens, users accessing the organization that are logged-in via a non-SSO login method are required to log back in using SAML SSO. This setting can be switched back to allow all login methods by unselecting the checkbox and clicking **Save**.

<Note>
  You must be logged in via SAML SSO in order to update this setting to `Only SAML SSO`. This is to ensure the SAML settings are valid and avoid locking users out of your organization.
</Note>

For troubleshooting, refer to the [SAML SSO FAQs](/langsmith/faq#saml-sso-faqs). If you have issues setting up SAML SSO, contact the LangChain support team via [support.langchain.com](https://support.langchain.com).

### Prerequisites

<Note>
  SAML SSO is available for organizations on the [Enterprise plan](https://www.langchain.com/pricing-langsmith). Please [contact sales](https://www.langchain.com/contact-sales) to learn more.
</Note>

* Your organization must be on an Enterprise plan.
* Your Identity Provider (IdP) must support the SAML 2.0 standard.
* Only [`Organization Admins`](/langsmith/organization-workspace-operations#sso-and-authentication) can configure SAML SSO.

For instructions on using SCIM along with SAML for user provisioning and deprovisioning, refer to the [SCIM setup](#set-up-scim-for-your-organization).

### Initial configuration

<Note>
  For IdP-specific configuration steps, refer to one of the following:

  * [Entra ID](#entra-id-azure)
  * [Google](#google)
  * [Okta](#okta)
</Note>

1. In your IdP: Configure a SAML application with the following details, then copy the metadata URL or XML for step 3.

   <Note>
     The following URLs depend on whether your organization is on the GCP US, GCP EU, GCP APAC, or AWS US cloud region. Ensure you select the correct link.
   </Note>

   1. Single sign-on URL (or ACS URL):

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

   2. Audience URI (or SP Entity ID):

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

   3. Name ID format: email address.

   4. Application username: email address.

   5. Required claims: `sub` and `email`.

2. In LangSmith: Go to **Settings** -> **Members and roles** -> **SSO Configuration**. Fill in the required information and submit to activate SSO login:

   1. Fill in either the `SAML metadata URL` or `SAML metadata XML`.
   2. Select the `Default workspace role` and `Default workspaces`. New users logging in via SSO will be added to the specified workspaces with the selected role.

      * `Default workspace role` and `Default workspaces` are editable. The updated settings will apply to new users only, not existing users.
      * (Coming soon) `SAML metadata URL` and `SAML metadata XML` are editable. This is usually only necessary when cryptographic keys are rotated/expired or the metadata URL has changed but the same IdP is still used.

### Supabase Attribute Mapping

<Note>
  Supabase Attribute Mapping is a [cloud-only](/langsmith/cloud) feature. [Self-hosted](/langsmith/self-hosted) deployments configure SAML/OIDC attributes directly with the IdP—see [Set up SSO with OAuth2.0 and OIDC](/langsmith/self-host-sso).
</Note>

LangSmith cloud uses [Supabase](/langsmith/cloud) as the SAML SSO backend. Supabase passes a small set of standard SAML attributes (such as `email` and `sub`) onto the user's JWT automatically. Any additional, non-standard SAML attribute your IdP emits (for example, `groups` for [SSO Groups Sync](#sso-groups-sync-alternative)) must be explicitly forwarded through Supabase before LangSmith can read it.

**Attribute flow (1:1):**

1. **IdP**: emits a SAML attribute with the configured name (e.g., `groups`).
2. **Supabase**: forwards the attribute onto the user's JWT only if the attribute name appears in the **Supabase Attribute Mapping** table on the SSO provider. Standard attributes are forwarded automatically; non-standard attributes are dropped unless explicitly listed.
3. **LangSmith**: reads the JWT claim by name (e.g., the value of [SSO Groups Sync](#sso-groups-sync-alternative)'s **Groups claim field**).

The attribute name is preserved end-to-end: the IdP attribute name, the Supabase Attribute Mapping entry, and the downstream LangSmith setting all use the same string.

#### Configuration

In **Settings** → **Members and roles** → **SSO Configuration**, scroll to the **Supabase Attribute Mapping** section and add one row per non-standard attribute you want to forward:

| Column             | Description                                                                                                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Attribute name** | The SAML attribute name as emitted by your IdP. Must match the JWT claim name LangSmith expects downstream (for SSO Groups Sync, this matches the **Groups claim field** value).          |
| **Array**          | Check this if the attribute is multi-valued (a list of strings). Leave unchecked for scalar (single-value) attributes. Example: check this for `groups`; leave unchecked for `full_name`. |

Click **Add row** for each additional attribute, then **Save**. An empty mapping table means no non-standard attributes flow through to the JWT.

### Entra ID (Azure)

For additional information, see Microsoft's [documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-setup-sso).

<div />

**Step 1: Create a new Entra ID application integration**

1. Log in to the [Azure portal](https://portal.azure.com/#home) with a privileged role (e.g., `Global Administrator`). On the left navigation pane, select the `Entra ID` service.

2. Navigate to **Enterprise Applications** and then select **All Applications**.

3. Click **Create your own application**.

4. In the **Create your own application** window:

   1. Enter a name for your application (e.g., `LangSmith`).
   2. Select **Integrate any other application you don't find in the gallery (Non-gallery)**.

5. Click **Create**.

**Step 2: Configure the Entra ID application and obtain the SAML Metadata**

1. Open the enterprise application that you created.

2. In the left-side navigation, select **Manage** > **Single sign-on**.

3. On the Single sign-on page, click **SAML**.

4. Update the **Basic SAML Configuration**:

   1. `Identifier (Entity ID)`:

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

   2. `Reply URL (Assertion Consumer Service URL)`:

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

   3. Leave `Relay State`, `Logout Url`, and `Sign on URL` empty.

   4. Click **Save**.

5. Ensure required claims are present with **Namespace**: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims`:

   1. `sub`: `user.objectid`.
   2. `emailaddress`: `user.userprincipalname` or `user.mail` (if using the latter, ensure all users have the `Email` field filled in under `Contact Information`).
   3. (Optional) For SCIM, see the [setup documentation](/langsmith/user-management) for specific instructions about `Unique User Identifier (Name ID)`.

6. On the SAML-based Sign-on page, under **SAML Certificates**, copy the **App Federation Metadata URL**.

**Step 3: Set up LangSmith SSO Configuration**

Follow the instructions under [initial configuration](#initial-configuration) in the `Fill in required information` step, using the metadata URL from the previous step.

**Step 4: Verify the SSO setup**

1. Assign the application to users/groups in Entra ID:

   1. Select **Manage** > **Users and groups**.

   2. Click **Add user/group**.

   3. In the **Add Assignment** window:

      1. Under **Users**, click **None Selected**.
      2. Search for the user you want to assign to the enterprise application, and then click **Select**.
      3. Verify that the user is selected, and click **Assign**.

2. Have the user sign in via the unique login URL from the **SSO Configuration** page, or go to **Manage** > **Single sign-on** and select **Test single sign-on with (application name)**.

### Google

For additional information, see Google's [documentation](https://support.google.com/a/answer/6087519).

**Step 1: Create and configure the Google Workspace SAML application**

1. Make sure you're signed into an administrator account with the appropriate permissions.

2. In the Admin console, go to **Menu** -> **Apps** -> **Web and mobile apps**.

3. Click **Add App** and then **Add custom SAML app**.

4. Enter the app name and, optionally, upload an icon. Click **Continue**.

5. On the Google Identity Provider details page, download the **IDP metadata** and save it for Step 2. Click **Continue**.

6. In the `Service Provider Details` window, enter:

   1. `ACS URL`:

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

   2. `Entity ID`:

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

   3. Leave `Start URL` and the `Signed response` box empty.

   4. Set `Name ID` format to `EMAIL` and leave `Name ID` as the default (`Basic Information > Primary email`).

   5. Click `Continue`.

7. Use `Add mapping` to ensure required claims are present:
   1. `Basic Information > Primary email` -> `email`

**Step 2: Set up LangSmith SSO Configuration**

Follow the instructions under [initial configuration](#initial-configuration) in the `Fill in required information` step, using the `IDP metadata` from the previous step as the metadata XML.

**Step 3: Turn on the SAML app in Google**

1. Select the SAML app under `Menu -> Apps -> Web and mobile apps`

2. Click `User access`.

3. Turn on the service:

   1. To turn the service on for everyone in your organization, click `On for everyone`, and then click `Save`.

   2. To turn the service on for an organizational unit:

      1. At the left, select the organizational unit then `On`.
      2. If the Service status is set to `Inherited` and you want to keep the updated setting, even if the parent setting changes, click `Override`.
      3. If the Service status is set to `Overridden`, either click `Inherit` to revert to the same setting as its parent, or click `Save` to keep the new setting, even if the parent setting changes.

   3. To turn on a service for a set of users across or within organizational units, select an access group. For details, go to [Use groups to customize service access](https://support.google.com/a/answer/9050643).

4. Ensure that the email addresses your users use to sign in to LangSmith match the email addresses they use to sign in to your Google domain.

**Step 4: Verify the SSO setup**

Have a user with access sign in via the unique login URL from the **SSO Configuration** page, or go to the SAML application page in Google and click **TEST SAML LOGIN**.

### Okta

#### Supported features

* IdP-initiated SSO (Single Sign-On)
* SP-initiated SSO
* Just-In-Time provisioning
* Enforce SSO only

#### Configuration steps

For additional information, see Okta's [documentation](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_saml.htm).

**Step 1: Create and configure the Okta SAML application**

<div>
  <b>Via Okta Integration Network (recommended)</b>
</div>

1. Sign in to [Okta](https://login.okta.com/).

2. In the upper-right corner, select Admin. The button is not visible from the Admin area.

3. Select `Browse App Integration Catalog`.

4. Find and select the LangSmith application.

5. On the application overview page, select Add Integration.

6. Leave `ApiUrlBase` empty.

7. Fill in `AuthHost`:

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

8. (Optional, if planning to use [SCIM](#set-up-scim-for-your-organization) as well) Fill in `LangSmithUrl`:

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

9. Under Application Visibility, keep the box unchecked.

10. Select Next.

11. Select `SAML 2.0`.

12. Fill in `Sign-On Options`:
    * `Application username format`: `Email`
    * `Update application username on`: `Create and update`
    * `Allow users to securely see their password`: leave **unchecked**.

13. Copy the **Metadata URL** from the **Sign On Options** page to use in the next step.

**Via Custom App Integration**

<Warning>
  SCIM is not compatible with this method of configuration. Refer to [**Via Okta Integration Network**](#via-okta-integration-network).
</Warning>

1. Log in to Okta as an administrator, and go to the **Okta Admin console**.

2. Under **Applications** > **Applications** click **Create App Integration**.

3. Select **SAML 2.0**.

4. Enter an `App name` (e.g., `LangSmith`) and optionally an **App logo**, then click **Next**.

5. Enter the following information in the **Configure SAML** page:

   1. `Single sign-on URL` (`ACS URL`). Keep `Use this for Recipient URL and Destination URL` checked:

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

   2. `Audience URI (SP Entity ID)`:

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

   3. `Name ID format`: **Persistent**.

   4. `Application username`: `email`.

   5. Leave the rest of the fields empty or set to their default.

   6. Click **Next**.

6. Click **Finish**.

7. Copy the **Metadata URL** from the **Sign On** page to use in the next step.

**Step 2: Set up LangSmith SSO Configuration**

Follow the instructions under [initial configuration](#initial-configuration) in the **Fill in required information** step, using the metadata URL from the previous step.

**Step 3: Assign users to LangSmith in Okta**

1. Under **Applications** > **Applications**, select the SAML application created in Step 1.
2. Under the **Assignments** tab, click **Assign** then either **Assign to People** or **Assign to Groups**.
3. Make the desired selection(s), then **Assign** and **Done**.

**Step 4: Verify the SSO setup**

Have a user with access sign in via the unique login URL from the `SSO Configuration` page, or have a user select the application from their Okta dashboard.

#### SP-initiated SSO

Once service-provider–initiated SSO is configured, users can sign in using a unique login URL. You can find this in the LangSmith UI under **Organization members and roles** then **SSO configuration**.

## Set up SCIM for your organization

<Note>
  Looking for a lighter-weight alternative to SCIM that doesn't require IdP admin involvement to push groups? See [SSO Groups Sync](#sso-groups-sync-alternative) below—it reads group memberships directly from the SSO token at login time and reuses the same naming convention.
</Note>

System for Cross-domain Identity Management (SCIM) is an open standard that allows for the automation of user provisioning. Using SCIM, you can automatically provision and de-provision users in your LangSmith [organization and workspaces](/langsmith/administration-overview), keeping user access synchronized with your organization's identity provider.

<Note>
  SCIM is available for organizations on the [Enterprise plan](https://www.langchain.com/pricing). [Contact sales](https://www.langchain.com/contact-sales) to learn more.

  SCIM is available on Helm chart versions 0.10.41 (application version 0.10.108) and later.

  SCIM support is API-only (see instructions below).
</Note>

SCIM eliminates the need for manual user management and ensures that user access is always up-to-date with your organization's identity system. This allows for:

* **Automated user management**: Users are automatically added, updated, and removed from LangSmith based on their status in your IdP.
* **Reduced administrative overhead**: No need to manage user access manually across multiple systems.
* **Improved security**: Users who leave your organization are automatically deprovisioned from LangSmith.
