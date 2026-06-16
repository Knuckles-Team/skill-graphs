# Set up SSO with OAuth2.0 and OIDC
Source: https://docs.langchain.com/langsmith/self-host-sso

LangSmith Self-Hosted provides SSO via OAuth2.0 and OIDC. This will delegate authentication to your Identity Provider (IdP) to manage access to LangSmith.

Our implementation supports almost anything that is OIDC compliant, with a few exceptions. Once configured, you will see a login screen like this:

<img alt="LangSmith UI with OAuth SSO" />

## Overview

<Note>
  You may upgrade a [basic auth](/langsmith/self-host-basic-auth) installation to this mode, but not a [none auth](/langsmith/authentication-methods#none) installation. In order to upgrade, simply remove the basic auth configuration and add the required configuration parameters as shown below. Users may then login via OAuth *only*. **In order to maintain access post-upgrade, you must have access to login via OAuth using an email address that previously logged in via basic auth.**
</Note>

<Warning>
  LangSmith does not support moving from SSO to basic auth mode in self-hosted at the moment. We also do not support moving from OAuth Mode with client secret to OAuth mode without a client secret and vice versa. Finally, we do not support having both basic auth and OAuth at the same time. Ensure you disable the basic auth configuration when enabling OAuth.
</Warning>

## With client secret (Recommended)

By default, LangSmith Self-Hosted supports the `Authorization Code` flow with `Client Secret`. In this version of the flow, your client secret is stored security in LangSmith (not on the frontend) and used for authentication and establishing auth sessions.

### Prerequisites

* You must be self-hosted and on an Enterprise plan.
* Your IdP must support the `Authorization Code` flow with `Client Secret`.
* Your IdP must support using an external discovery/issuer URL. We will use this to fetch the necessary routes and keys for your IdP.
* You must provide the `OIDC`, `email`, and `profile` scopes to LangSmith. We use these to fetch the necessary user information and email for your users.

<Note>
  LangSmith SSO is only supported over `https`.
</Note>

### Configuration

* You will need to set the callback URL in your IdP to `https://<host>/api/v1/oauth/custom-oidc/callback`, where `host` is the domain or IP you have provisioned for your LangSmith instance. This is where your IdP will redirect the user after they have authenticated.
* To terminate the IdP session on logout (so users must re-authenticate), register your LangSmith URL (e.g., `https://<host>`) as a **post-logout redirect URI** (sometimes called "Sign-out redirect URI") in your IdP, then set `OAUTH_IDP_LOGOUT_ENABLED=true` in your environment (via `commonEnv` in Helm or your `.env` file in Docker Compose).
* You will need to provide the `oauthClientId`, `oauthClientSecret`, `hostname`, and `oauthIssuerUrl` in your `values.yaml` file. This is where you will configure your LangSmith instance.
* If you have **not** already configured Oauth with client secret or if you only have personal orgs, you must provide an email address to assign as the initial org admin for the newly provisioned SSO org. If you are upgrading from basic auth, your existing org will be reused instead.

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    authType: mixed
    hostname: https://langsmith.example.com
    initialOrgAdminEmail: test@email.com # Set this if required
    oauth:
      enabled: true
      oauthClientId: <YOUR CLIENT ID>
      oauthClientSecret: <YOUR CLIENT SECRET>
      oauthIssuerUrl: <YOUR DISCOVERY URL>
      oauthScopes: "email,profile,openid"
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  AUTH_TYPE=mixed
  INITIAL_ORG_ADMIN_EMAIL=test@email.com
  LANGSMITH_URL=https://langsmith.example.com
  OAUTH_CLIENT_ID=your-client-id
  OAUTH_CLIENT_SECRET=your-client-secret
  OAUTH_ISSUER_URL=https://your-issuer-url
  OAUTH_SCOPES=email,profile,openid
  ```
</CodeGroup>

### Session length controls

<Note>
  All of the environment variables in this section are for the `platform-backend` service and can be added using `platformBackend.deployment.extraEnv` in Helm.
</Note>

* By default, session length is controlled by the expiration of the identity token returned by the identity provider
* Most setups should use refresh tokens to enable session length extension beyond the identity token expiration up to `OAUTH_SESSION_MAX_SEC`, which may require including the `offline_access` scope by adding to `oauthScopes` (Helm) or `OAUTH_SCOPES` (Docker)
* `OAUTH_SESSION_MAX_SEC` (default 1 day) can be overridden to a maximum of one week (`604800`)
* For identity provider setups that don't support refresh tokens, setting `OAUTH_OVERRIDE_TOKEN_EXPIRY="true"` will take `OAUTH_SESSION_MAX_SEC` as the session length, ignoring the identity token expiration

### Override sub claim

In some scenarios, it may be necessary to override which claim is used as the `sub` claim from your identity provider.
For example, in SCIM, the resolved `sub` claim and SCIM `externalId` must match in order for login to succeed.
If there are restrictions on the source attribute of the `sub` claim and/or the SCIM `externalId`, set the `ISSUER_SUB_CLAIM_OVERRIDES` environment variable to select which OIDC JWT claim is used as the `sub`.

If an issuer URL **starts with** one of the URLs in this configuration, the `sub` claim is taken from the field name specified.
For example, with the following configuration, a token with the issuer `https://idp.yourdomain.com/application/uuid` would use the `customClaim` value as the `sub`:

```
ISSUER_SUB_CLAIM_OVERRIDES='{"https://idp.yourdomain.com": "customClaim"}'
```

If unset, the default value for this configuration uses the `oid` claim when Azure Entra ID is used as the identity provider:

```
ISSUER_SUB_CLAIM_OVERRIDES='{"https://login.microsoftonline.com/": "oid", "https://sts.windows.net/": "oid", "https://login.microsoftonline.us/": "oid", "https://login.partner.microsoftonline.cn/": "oid"}'
```

### SSO Groups Sync

<Note>
  SSO Groups Sync on self-hosted requires LangSmith chart version **0.15.0-rc.3** (application version **0.15.2rc1**) or later.
</Note>

[SSO Groups Sync](/langsmith/user-management#sso-groups-sync-alternative) lets LangSmith assign org and workspace roles from a group membership claim on the OIDC token, as a simpler alternative to [SCIM](/langsmith/user-management#set-up-scim-for-your-organization). On self-hosted, you must configure the IdP to include groups in the OIDC ID token before LangSmith can read them.

**IdP-side configuration (varies by provider):**

1. Configure your IdP application to emit a group membership claim in the OIDC ID token. The source attribute and the resulting claim name vary by IdP. Common examples include `groups`, `roles`, or a custom claim name. LangSmith does not dictate the source attribute.
2. Depending on your IdP, you may need to add an additional scope (commonly `groups`) to `oauthScopes` to receive the claim. Check your IdP's documentation for the required scope and any additional configuration needed to include group memberships in the token.
3. Group names must follow the [SCIM naming convention](/langsmith/user-management#group-naming-convention) (e.g., `LS:Organization Admin`, `LS:Organization User:prod:Editor`). The separator is shared with SCIM via [`scim_group_name_separator`](/langsmith/user-management#configure-custom-separator).

**Helm configuration:**

If your IdP requires an additional OIDC scope to include groups in the token (commonly `groups`), add it to `oauthScopes`:

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    authType: mixed
    hostname: https://langsmith.example.com
    oauth:
      enabled: true
      oauthClientId: <YOUR CLIENT ID>
      oauthClientSecret: <YOUR CLIENT SECRET>
      oauthIssuerUrl: <YOUR DISCOVERY URL>
      oauthScopes: "email,profile,openid,groups"
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  AUTH_TYPE=mixed
  LANGSMITH_URL=https://langsmith.example.com
  OAUTH_CLIENT_ID=your-client-id
  OAUTH_CLIENT_SECRET=your-client-secret
  OAUTH_ISSUER_URL=https://your-issuer-url
  OAUTH_SCOPES=email,profile,openid,groups
  ```
</CodeGroup>

The exact scope name (`groups`, `roles`, etc.) depends on your IdP. Check your IdP's OIDC documentation.

**LangSmith-side configuration:**

Per-provider SSO Groups Sync settings are stored on the SSO provider record and toggled via the [LangSmith UI](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-self-host-sso) or [API](/langsmith/reference) (not via Helm values). Once your IdP emits the groups claim, configure SSO Groups Sync from the UI in **Settings** → **Members and roles** → **SSO Configuration** → **SSO Groups Sync**. Or, via the API as described in the [main SSO Groups Sync documentation](/langsmith/user-management#sso-groups-sync-alternative). The claim name configured in the **Groups claim field** must match the claim emitted by your IdP.

### Google workspace IdP setup

You can use Google Workspace as a single sign-on (SSO) provider using [OAuth2.0 and OIDC](https://developers.google.com/identity/openid-connect/openid-connect) without PKCE.

<Note>
  You must have administrator-level access to your organization's Google Cloud Platform (GCP) account to create a new project, or permissions to create and configure OAuth 2.0 credentials for an existing project. We recommend that you create a new project for managing access, since each GCP project has a single OAuth consent screen.
</Note>

1. Create a new GCP project, see the Google documentation topic [creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects)

2. After you have created the project, open the [Credentials](https://console.developers.google.com/apis/credentials) page in the Google API Console (making sure the project in the top left corner is correct)

3. Create new credentials: `Create Credentials → OAuth client ID`

4. Choose `Web application` as the `Application type` and enter a name for the application e.g. `LangSmith`

5. In `Authorized Javascript origins` put the domain of your LangSmith instance e.g. `https://langsmith.yourdomain.com`

6. In `Authorized redirect URIs` put the domain of your LangSmith instance followed by `/api/v1/oauth/custom-oidc/callback` e.g. `https://langsmith.yourdomain.com/api/v1/oauth/custom-oidc/callback`

7. Click `Create`, then download the JSON or copy and save the `Client ID` (ends with `.apps.googleusercontent.com`) and `Client secret` somewhere secure. **You will be able to access these later if needed**.

8. Select `OAuth consent screen` from the navigation menu on the left

   1. Choose the Application type as `Internal`. **If you select `Public`, anyone with a Google account can sign in.**
   2. Enter a descriptive `Application name`. This name is shown to users on the consent screen when they sign in. For example, use `LangSmith` or `<organization_name> SSO for LangSmith`.
   3. Verify that the Scopes for Google APIs only lists email, profile, and openid scopes. Only these scopes are required for single sign-on. If you grant additional scopes it increases the risk of exposing sensitive data.

9. (Optional) control who within your organization has access to LangSmith: [https://admin.google.com/ac/owl/list?tab=configuredApps](https://admin.google.com/ac/owl/list?tab=configuredApps). See [Google's documentation](https://support.google.com/a/answer/7281227?hl=en\&fl=1\&sjid=9554153972856467090-NA) for additional details.

10. Configure LangSmith to use this OAuth application. For examples, here are the `config`values that would be used for Kubernetes configuration:

    1. `oauthClientId`: `Client ID` (ends with `.apps.googleusercontent.com`)
    2. `oauthClientSecret`: `Client secret`
    3. `hostname`: the domain of your LangSmith instance e.g. `https://langsmith.yourdomain.com` (no trailing slash)
    4. `oauthIssuerUrl`: `https://accounts.google.com`
    5. `oauth.enabled`: `true`
    6. `authType`: `mixed`

### Okta IdP setup

#### Supported features

* IdP-initiated SSO
* SP-initiated SSO
* Just-In-Time provisioning (see [Manage user access in SSO organizations](/langsmith/jit-invite-sso))

#### Configuration steps

For additional information, see Okta's [documentation](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm).
If you have any questions or issues, please contact support via [support.langchain.com](https://support.langchain.com).

<div>
  <b>Via Okta Integration Network (recommended)</b>
</div>

<Info>For details on SCIM setup, refer to [Set up SCIM for your organization](/langsmith/user-management#set-up-scim-for-your-organization).</Info>

<Note>
  This method of configuration is required in order to use SCIM with Okta.
</Note>

1. Sign in to [Okta](https://login.okta.com/).
2. In the upper-right corner, select Admin. The button is not visible from the Admin area.
3. Select `Browse App Integration Catalog`.
4. Find and select the LangSmith application.
5. On the application overview page, select Add Integration.
6. Fill in `ApiUrlBase`:
   * Your LangSmith API URL **without the protocol** (`https://`) formatted as `<langsmith_domain>/api/v1`, e.g., `langsmith.yourdomain.com/api/v1`.
   * If your installation is configured with a subdomain / path prefix, include that in the URL, e.g., `langsmith.yourdomain.com/prefix/api/v1`.
7. Leave `AuthHost` empty.
8. (Optional, if planning to use [SCIM](/langsmith/user-management#set-up-scim-for-your-organization) as well) Fill in `LangSmithUrl`: The `<langsmith_url>` portion from above, e.g., `langsmith.yourdomain.com`.
9. Under Application Visibility, keep the box unchecked.
10. Select Next.
11. Select `OpenID Connect`.
12. Fill in `Sign-On Options`:
    * `Application username format`: `Email`.
    * `Update application username on`: `Create and update`.
    * `Allow users to securely see their password`: leave **unchecked**.
13. Click **Save**.
14. Configure LangSmith to use this OAuth application (see [general configuration section](#configuration) for details about `initialOrgAdminEmail`):

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    authType: mixed
    hostname: https://langsmith.example.com # the domain of your instance (note no trailing slash)
    initialOrgAdminEmail: test@email.com # Set this if required
    oauth:
      enabled: true
      oauthClientId: "Client ID" # (starts with `0o`)
      oauthClientSecret: "Client secret"
      oauthIssuerUrl: "https://company-7422949.okta.com" # the URL of your Okta instance
      oauthScopes: "email,profile,openid"
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  AUTH_TYPE=mixed
  INITIAL_ORG_ADMIN_EMAIL=test@email.com # Set this if required
  LANGSMITH_URL=https://langsmith.example.com # the domain of your instance (note no trailing slash)
  OAUTH_CLIENT_ID="Client ID" # (starts with `0o`)
  OAUTH_CLIENT_SECRET="Client secret"
  OAUTH_ISSUER_URL="https://company-7422949.okta.com" # the URL of your Okta instance
  OAUTH_SCOPES=email,profile,openid
  ```
</CodeGroup>

<Info>For details on SCIM setup, refer to [Set up SCIM for your organization](/langsmith/user-management#set-up-scim-for-your-organization).</Info>

<div>
  <b>Via Custom App Integration</b>
</div>

<Warning>
  SCIM is not compatible with this method of configuration. Refer to [**Via Okta Integration Network**](#via-okta-integration-network).
</Warning>

1. Log in to Okta as an administrator, and go to the **Okta Admin console**.
2. Under **Applications** > **Applications** click **Create App Integration**.
3. Select **OIDC - OpenID Connect** as the Sign-in method and **Web Application** as the Application type, then click **Next**.
4. Enter an `App integration name` (e.g., `LangSmith`).
5. Recommended: Check **Core grants > Refresh Token** (see [session length controls](#session-length-controls)).
6. In **Sign-in redirect URIs** put the domain of your LangSmith instance followed by `/api/v1/oauth/custom-oidc/callback`, e.g., `https://langsmith.yourdomain.com/api/v1/oauth/custom-oidc/callback`. If your installation is configured with a subdomain / path prefix, include that in the URL, e.g., `https://langsmith.yourdomain.com/prefix/api/v1/oauth/custom-oidc/callback`.
7. Under **Sign-out redirect URIs**, set the value to your LangSmith URL, e.g., `https://langsmith.yourdomain.com`. This ensures the IdP session is terminated when users log out of LangSmith.
8. Under **Trusted Origins > Base URIs** add your langsmith URL with the protocol, e.g., `https://langsmith.yourdomain.com`.
9. Select your desired option under **Assignments > Controlled access**:
   * Allow everyone in your organization to access.
   * Limit access to selected groups.
   * Skip group assignment for now.
10. Click **Save**.
11. Under **Sign On > OpenID Connect ID Token** set **Issuer** to **Okta URL**.
12. (Optional) Under **General > Login** set **Login initiated by** to `Either Okta or App` to enable IdP-initiated login.
13. (Recommended) Under **General > Login > Email verification experience** fill in the **Callback URI** with the LangSmith URL, e.g., `https://langsmith.yourdomain.com`.
14. Configure LangSmith to use this OAuth application (see [general configuration section](#configuration) for details about `initialOrgAdminEmail`):

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    authType: mixed
    hostname: https://langsmith.example.com # the domain of your instance (note no trailing slash)
    initialOrgAdminEmail: test@email.com # Set this if required
    oauth:
      enabled: true
      oauthClientId: "Client ID" # (starts with `0o`)
      oauthClientSecret: "Client secret"
      oauthIssuerUrl: "https://company-7422949.okta.com" # the URL of your Okta instance
      oauthScopes: "email,profile,openid"
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  AUTH_TYPE=mixed
  INITIAL_ORG_ADMIN_EMAIL=test@email.com # Set this if required
  LANGSMITH_URL=https://langsmith.example.com # the domain of your instance (note no trailing slash)
  OAUTH_CLIENT_ID="Client ID" # (starts with `0o`)
  OAUTH_CLIENT_SECRET="Client secret"
  OAUTH_ISSUER_URL="https://company-7422949.okta.com" # the URL of your Okta instance
  OAUTH_SCOPES=email,profile,openid
  ```
</CodeGroup>

#### SP-initiated SSO

Users can sign in using the **Login via SSO** button on the LangSmith homepage.

## Without client secret (PKCE) (Deprecated)

We recommend running with a `Client Secret` if possible (previously we didn't support this). However, if your IdP does not support this, you can use the `Authorization Code with PKCE` flow.

This flow does *not* require a `Client Secret`. For the alternative workflow, refer to [With client secret](#with-client-secret-recommended).

### Requirements

There are a couple of requirements for using OAuth SSO with LangSmith:

* Your IdP must support the `Authorization Code with PKCE` [flow](https://www.oauth.com/oauth2-servers/pkce) (Google does not support this flow for example, but see [above](#with-client-secret-recommended) for an alternative configuration that Google supports). This is often displayed in your OAuth Provider as configuring a "Single Page Application (SPA)"
* Your IdP must support using an external discovery/issuer URL. We will use this to fetch the necessary routes and keys for your IdP.
* You must provide the `OIDC`, `email`, and `profile` scopes to LangSmith. We use these to fetch the necessary user information and email for your users.
* You will need to set the callback URL in your IdP to `http://<host>/oauth-callback`, where host is the domain or IP you have provisioned for your LangSmith instance. This is where your IdP will redirect the user after they have authenticated.
* You will need to provide the `oauthClientId` and `oauthIssuerUrl` in your `values.yaml` file. This is where you will configure your LangSmith instance.

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    oauth:
      enabled: true
      oauthClientId: <YOUR CLIENT ID>
      oauthIssuerUrl: <YOUR DISCOVERY URL>
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  AUTH_TYPE=oauth
  OAUTH_CLIENT_ID=your-client-id
  OAUTH_ISSUER_URL=https://your-issuer-url
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-sso.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Enable TTL and data retention
Source: https://docs.langchain.com/langsmith/self-host-ttl

LangSmith Self-Hosted allows enablement of automatic TTL and Data Retention of traces. This can be useful if you're complying with data privacy regulations, or if you want to have more efficient space usage and auto cleanup of your traces. Traces will also have their data retention period automatically extended based on certain actions or run rule applications.

<Note>
  **Self-hosted [Enterprise](/langsmith/pricing-plans) customers:** You can now configure extended data retention at the workspace level through the UI, which provides more granular control without requiring environment variable changes. For more information, refer to [Customize extended retention policy](/langsmith/data-purging-compliance#customize-extended-retention-policy). The system-wide TTL configuration documented on this page is still supported.
</Note>

## Requirements

You can configure retention through helm or environment variable settings. There are a few options that are configurable:

* *Enabled:* Whether data retention is enabled or disabled. If enabled, via the UI you can your default organization and project TTL tiers to apply to traces (see [data retention guide](/langsmith/usage-and-billing#data-retention) for details).
* *Retention Periods:* You can configure system-wide retention periods for shortlived and longlived traces. Once configured, you can manage the retention level at each project as well as set an organization-wide default for new projects.

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    ttl:
      enabled: true
      ttl_period_seconds:
        # -- 400 day longlived and 14 day shortlived
        longlived: "34560000"
        shortlived: "1209600"
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env fileFF_TRACE_TIERS_ENABLED=trueTRACE_TIER_TTL_DURATION_SEC_MAP='{"longlived": 34560000, "shortlived": 1209600}'
  ```
</CodeGroup>

## ClickHouse TTL cleanup job

As of version **0.11**, a cron job runs on weekends to assist in deleting expired data that may not have been cleaned up by ClickHouse's built-in TTL mechanism.

<Warning>
  This job uses potentially long running **mutations** (`ALTER TABLE DELETE`), which are expensive operations that can impact ClickHouse's performance. We recommend running these operations only during off-peak hours (nights and weekends). During testing with **1 concurrent active** mutation (default), we did not observe significant CPU, memory, or latency increases.
</Warning>

### Default schedule

By default, the cleanup job runs:

* **Saturday**: 8pm and 10pm UTC
* **Sunday**: 12am, 2am, and 4am UTC

### Disabling the job

To disable the cleanup job entirely:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
queue:
  deployment:
    extraEnv:
      - name: "ENABLE_CLICKHOUSE_TTL_CLEANUP_CRON"
        value: "false"
```

### Configuring the schedule

You can customize when the cleanup job runs by modifying the cron expressions:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
queue:
  deployment:
    extraEnv:
      # UTC: Sunday 12am/2am/4am
      - name: "CLICKHOUSE_TTL_CLEANUP_CRON_WEEKEND_MORNING"
        value: "0 0,2,4 * * 0"
      # UTC: Saturday 8pm/10pm
      - name: "CLICKHOUSE_TTL_CLEANUP_CRON_WEEKEND_EVENING"
        value: "0 20,22 * * 6"
```

<Tip>
  To run the job on a single cron schedule, set both `CLICKHOUSE_TTL_CLEANUP_CRON_WEEKEND_EVENING` and `CLICKHOUSE_TTL_CLEANUP_CRON_WEEKEND_MORNING` to the same value. Job locking prevents overlapping executions.
</Tip>

### Configuring minimum expired rows per part

The job goes table by table, scanning parts and deleting data from parts containing a minimum number of expired rows. This threshold balances efficiency and thoroughness:

* **Too low**: Job scans entire parts to clear minimal data (inefficient)
* **Too high**: Job misses parts with significant expired data

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
queue:
  deployment:
    extraEnv:
      - name: "CLICKHOUSE_TTL_CRON_MIN_EXPIRED_ROWS_PER_PART"
        value: "100000" # 100k expired rows
```

#### Checking expired rows

Use this query to analyze expired rows in your tables, and tweak your minimum value accordingly:

```sql theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
-- Query for Runs table. For other tables, replace 'ttl_seconds' with 'trace_ttl_seconds'
SELECT
    _part,
    count() AS expired_rows
FROM runs
WHERE trace_first_received_at IS NOT NULL
AND ttl_seconds IS NOT NULL
AND toDateTime(assumeNotNull(trace_first_received_at) + toIntervalSecond(assumeNotNull(ttl_seconds))) < now()
GROUP BY _part
ORDER BY expired_rows DESC
```

### Configuring maximum active mutations

Delete operations can be time-consuming (\~50 minutes for a 100GB part). You can increase concurrent mutations to speed up the process:

```yaml theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
queue:
  deployment:
    extraEnv:
      - name: "CLICKHOUSE_TTL_CRON_MAX_ACTIVE_MUTATIONS"
        value: "1"
```

<Warning>
  Increasing concurrent DELETE operations can severely impact system performance. Monitor your system carefully and only increase this value if you can tolerate potentially slower insert and read latencies.
</Warning>

### Emergency: Stopping running mutations

If you experience latency spikes and need to terminate a running mutation:

1. **Find active mutations**:

   ```sql theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   SELECT * FROM system.mutations WHERE is_done = 0;
   ```

   Look for the `mutation_id` where the `command` column contains a `DELETE` statement.

2. **Kill the mutation**:
   ```sql theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   KILL MUTATION WHERE mutation_id = '<mutation_id>';
   ```

### Backups and data retention

If disk space does not decrease after running this job, or if it continues to increase, backups may be causing the issue by creating file system hard links. These links prevent ClickHouse from cleaning up the data.

To verify, check the following directories inside your ClickHouse pod:

* `/var/lib/clickhouse/backup`
* `/var/lib/clickhouse/shadow`

If backups are present, copy them to an external filesystem or blob storage (e.g., S3), then clear the directories. Within a few minutes, you will notice disk space releasing.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-ttl.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Customize the error support message
Source: https://docs.langchain.com/langsmith/self-host-ui-customization

Customize support contact information in the LangSmith frontend for self-hosted deployments.

## Custom error support message

By default, error messages in LangSmith direct users to the [Support Portal](https://support.langchain.com). You can replace this with your own support contact information.

When set, all error and support messages throughout the UI will display your custom text instead of the default LangChain support email.

<Note>
  The custom message is rendered as **plain text** only. HTML tags will not be interpreted and will display as literal text.
</Note>

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    customErrorSupportMessage: "For help, contact your internal IT team at helpdesk@example.com"
  ```

  ```yaml Docker Compose theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  services:
    langchain-frontend:
      environment:
        - CUSTOM_ERROR_SUPPORT_MESSAGE=For help, contact your internal IT team at helpdesk@example.com
  ```
</CodeGroup>

To revert to the default behavior, remove the setting or set it to an empty string.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-ui-customization.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Upgrade an installation
Source: https://docs.langchain.com/langsmith/self-host-upgrades

<Warning>
  Downgrades are not officially supported. LangSmith upgrades may include database migrations and other changes that are not backward-compatible. If you need to roll back to a previous version, contact technical support via the [Support Portal](https://support.langchain.com) for guidance.
</Warning>

If you don't have the repo added, run the following command to add it:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm repo add langchain https://langchain-ai.github.io/helm/
```

Update your local helm repo

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm repo update
```

Update your helm chart config file with any updates that are needed in the new version. These will be detailed in the release notes for the new version.

Run the following command to upgrade the chart (replace `version` with the version you want to upgrade to):

<Note>
  If you are using a namespace other than the default namespace, you will need to specify the namespace in the `helm` and `kubectl` commands by using the `-n <namespace` flag.
</Note>

Find the latest version of the chart. You can find this in the [LangSmith Helm Chart GitHub repository](https://github.com/langchain-ai/helm/releases) or by running the following command:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm search repo langchain/langsmith --versions
```

You should see output similar to this:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
langchain/langsmith     0.10.14         0.10.32         Helm chart to deploy the langsmith application ...
langchain/langsmith     0.10.13         0.10.32         Helm chart to deploy the langsmith application ...
langchain/langsmith     0.10.12         0.10.32         Helm chart to deploy the langsmith application ...
langchain/langsmith     0.10.11         0.10.29         Helm chart to deploy the langsmith application ...
langchain/langsmith     0.10.10         0.10.29         Helm chart to deploy the langsmith application ...
langchain/langsmith     0.10.9          0.10.29         Helm chart to deploy the langsmith application ...
```

Choose the version you want to upgrade to (generally the latest version is recommended) and note the version number:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm upgrade <release-name> langchain/langsmith --version <version> --values <path-to-values-file> --wait --debug
```

Verify that the upgrade was successful:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
helm status <release-name>
```

All pods should be in the `Running` state. Verify that ClickHouse is running and that both `migrations` jobs have completed.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
kubectl get pods
NAME                                     READY   STATUS      RESTARTS   AGE
langsmith-backend-95b6d54f5-gz48b        1/1     Running     0          15h
langsmith-pg-migrations-d2z6k            0/1     Completed   0          5h48m
langsmith-ch-migrations-gasvk            0/1     Completed   0          5h48m
langsmith-clickhouse-0                   1/1     Running     0          26h
langsmith-frontend-84687d9d45-6cg4r      1/1     Running     0          15h
langsmith-hub-backend-66ffb75fb4-qg6kl   1/1     Running     0          15h
langsmith-playground-85b444d8f7-pl589    1/1     Running     0          15h
langsmith-queue-d58cb64f7-87d68          1/1     Running     0          15h
```

## Validate your deployment

1. Run `kubectl get services`

   Output will be similar to:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   NAME                         TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                      AGE
   kubernetes                   ClusterIP      172.20.0.1       <none>          443/TCP                      27d
   langsmith-backend            ClusterIP      172.20.22.34     <none>          1984/TCP                     21d
   langsmith-clickhouse         ClusterIP      172.20.117.62    <none>          8123/TCP,9000/TCP            21d
   langsmith-frontend           LoadBalancer   172.20.218.30    <external ip>   80:30093/TCP,443:31130/TCP   21d
   langsmith-platform-backend   ClusterIP      172.20.232.183   <none>          1986/TCP                     21d
   langsmith-playground         ClusterIP      172.20.167.132   <none>          3001/TCP                     21d
   langsmith-postgres           ClusterIP      172.20.59.63     <none>          5432/TCP                     21d
   langsmith-redis              ClusterIP      172.20.229.98    <none>          6379/TCP                     20d
   ```

2. Curl the external ip of the `langsmith-frontend` service:

   ```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
   curl <external ip>/api/info
   {"version":"0.5.7","license_expiration_time":"2033-05-20T20:08:06","batch_ingest_config":{"scale_up_qsize_trigger":1000,"scale_up_nthreads_limit":16,"scale_down_nempty_trigger":4,"size_limit":100,"size_limit_bytes":20971520}}
   ```

   Check that the version matches the version you upgraded to.

3. Visit the external IP for the `langsmith-frontend` service on your browser. The LangSmith UI should be visible and operational.

   <img alt="LangSmith UI" />

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-upgrades.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Interact with your self-hosted instance of LangSmith
Source: https://docs.langchain.com/langsmith/self-host-usage

This guide will walk you through the process of using your self-hosted instance of LangSmith.

<Info>
  This guide assumes you have already deployed a self-hosted LangSmith instance. If you have not, please refer to the [kubernetes deployment guide](/langsmith/kubernetes).
</Info>

### Configuring the application you want to use with LangSmith

LangSmith has a single API for interacting with both the hub and the LangSmith backend.

1. Once you have deployed your instance, you can access the LangSmith UI at `http(s)://<host>`.
2. The LangSmith API will be available at `http(s)://<host>/api/v1`
3. The LangSmith Control Plane will be available at `http(s)://<host>/api-host`

To use the API of your instance, you will need to set the following environment variables in your application:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
LANGSMITH_ENDPOINT=http://<host>/api/v1
LANGSMITH_API_KEY=foo # Set to a legitimate API key if using OAuth
```

You can also configure these variables directly in the LangSmith SDK client:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import langsmith
langsmith_client = langsmith.Client(
    api_key='<api_key>',
    api_url='http(s)://<host>/api/v1',
)
```

After setting the above, you should be able to run your code and see the results in your self-hosted instance. We recommend running through the [*quickstart guide*](https://docs.smith.langchain.com/#quick-start) to get a feel for how to use LangSmith.

### Self-Signed certificates

If you are using self-signed certificates for your self-hosted LangSmith instance, this can be problematic as Python comes with its own set of trusted certificates, which may not include your self-signed certificate. To resolve this, you may need to use something like `truststore` to load system certificates into your Python environment.

You can do this like so:

1. pip install truststore (or similar depending on the package manager you are using)

Then use the following code to load the system certificates:

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
import truststore
truststore.inject_into_ssl()

# The rest of your code
import langsmith
langsmith_client = langsmith.Client(
    api_key='<api_key>',
    api_url='http(s)://<host>/api/v1',
)
```

***

## API reference

To access the API reference, navigate to `http://<host>/api/docs` in your browser.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-usage.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Customize user management
Source: https://docs.langchain.com/langsmith/self-host-user-management

<Note>
  This guide assumes you have read the [admin guide](/langsmith/administration-overview) and [organization setup guide](/langsmith/set-up-hierarchy#set-up-an-organization).
</Note>

LangSmith offers additional customization features for user management using feature flags.

## Features

### Workspace level invites to an organization

The default behavior in LangSmith requires a user to be an Organization Admin in order to invite new users to an organization. For self-hosted customers that would like to delegate this responsibility to workspace Admins, a feature flag may be set that enables workspace Admins to invite new users to the organization as well as their specific workspace **at the workspace level**.

Once this feature is enabled via the configuration option below, workspace Admins may add new users in the `Workspace members` tab under `Settings` > `Workspaces`. Both of the following cases are supported when inviting at the workspace level, while the organization level invite functions the same as before.

1. Invite users who are NOT already active in the organization: this will add the users as pending to the organization and specific workspace
2. Invite users who ARE already active in the organization: adds the users directly to the workspace as an active member (no pending state).

Admins may invite users for both cases at the same time.

#### Configuration

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    workspaceScopeOrgInvitesEnabled: true
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  WORKSPACE_SCOPE_ORG_INVITES_ENABLED="true"
  ```
</CodeGroup>

### SSO new member login flow

As of helm **v0.11.10**, self-hosted deployments using OAuth SSO will no longer need to manually add members in LangSmith settings for them to join. Deployments will have a <b>default</b> organization, to which new users will automatically be added upon their first login to LangSmith.

For your **default** organization, you can set which workspace(s) and workspace role is assigned to new members. For **non-default** organizations, the invitation flow remains the same.
Once a user joins an organization, any changes to their workspaces or roles beyond the default organization settings must be managed either through LangSmith settings (as before) or via SCIM.

<Note>
  By default, all new users are added to the organization’s initially provisioned workspace (**Workspace 1** by default) with the **Workspace Editor** role.
</Note>

<img alt="Update SSO Member Settings" />

<Note>
  To change your default organization, use **Set Default Organization** in the organization selector dropdown. (Org Admin permissions required in both the source and target organization.)
</Note>

### SSO Groups Sync

<Note>
  SSO Groups Sync on self-hosted requires LangSmith chart version **0.15.0-rc.3** (application version **0.15.2rc1**) or later.
</Note>

[SSO Groups Sync](/langsmith/user-management#sso-groups-sync-alternative) reads group memberships from the OIDC ID token and assigns org and workspace roles using the [SCIM naming convention](/langsmith/user-management#group-naming-convention). It is a simpler alternative to [SCIM](/langsmith/user-management#set-up-scim-for-your-organization) for self-hosted organizations whose IdP can include groups in the OIDC token but cannot easily run SCIM provisioning.

For IdP-side configuration (claim, scope) refer to the [SSO Groups Sync section in the OIDC SSO setup guide](/langsmith/self-host-sso#sso-groups-sync). For settings reference and behavior, see the [main SSO Groups Sync documentation](/langsmith/user-management#sso-groups-sync-alternative).

### Disabling organization creating

By default, any user can create an organization in LangSmith. For self-hosted customers, an admin may want to restrict this ability after setting up initial organizations. This feature flag allows an admin to disable the ability for users to create new organizations.

#### Configuration

<Note>
  The `userOrgCreationDisabled` feature flag is set to `true` by default for organizations using [basic auth](/langsmith/self-host-basic-auth) or [SSO](/langsmith/self-host-sso).
</Note>

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    userOrgCreationDisabled: true
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  FF_ORG_CREATION_DISABLED="true"
  ```
</CodeGroup>

### Disabling personal organizations

By default, any user who logs in to LangSmith will have a personal organization created for them. For self-hosted customers, an admin may want to restrict this ability. This feature flag allows an admin to disable the ability for users to create personal organizations.

#### Configuration

<Note>
  The `personalOrgsDisabled` feature flag is set to `true` by default for organizations using [basic auth](/langsmith/self-host-basic-auth) or [SSO](/langsmith/self-host-sso).
</Note>

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  config:
    personalOrgsDisabled: true
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  FF_PERSONAL_ORGS_DISABLED="true"
  ```
</CodeGroup>

### Disabling personal access token creation

<Note>
  This feature requires Helm chart version 0.13.12 (application version 0.13.12) or later.
</Note>

By default, users can create Personal Access Tokens (PATs) in any organization. For self-hosted customers, an admin may want to globally disable PAT creation across all organizations. This environment variable allows an admin to prevent users from creating new PATs in any organization on the instance.

To disable PAT creation for a single organization instead, see the [per-organization API option](/langsmith/manage-organization-by-api#security-settings).

#### Configuration

<CodeGroup>
  ```yaml Helm theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  commonEnv:
    - name: PAT_CREATION_DISABLED
      value: "true"
  ```

  ```bash Docker theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  # In your .env file
  PAT_CREATION_DISABLED="true"
  ```
</CodeGroup>

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-user-management.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
