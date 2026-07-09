- Establish cross-region connectivity (Transit Gateway, VPC Peering) so Workers in one region can reach the VPC Endpoint in the other.

## Single-cloud HA on GCP Private Service Connect

For GCP-only HA, the same model applies, but use a Cloud DNS private zone for `region.tmprl.cloud` and point each `gcp-<region>.region.tmprl.cloud` record at the local PSC endpoint IP address.

| Record name                              | Record type | Value (your PSC endpoint IP)        |
| ---------------------------------------- | ----------- | ----------------------------------- |
| `gcp-us-central1.region.tmprl.cloud`     | A           | `10.x.x.x` (PSC endpoint IP)        |
| `gcp-us-east1.region.tmprl.cloud`        | A           | `10.x.x.x` (PSC endpoint IP)        |

A Connectivity Rule is required for each PSC connection — see [GCP PSC setup](/cloud/connectivity/gcp-connectivity) and [Connectivity Rules](/cloud/connectivity#connectivity-rules).

## Multi-cloud HA (AWS PrivateLink + GCP Private Service Connect)

If your replicas span clouds — for example, AWS `us-east-1` (active) and GCP `us-east4` (passive) — your Workers need a way to reach the active replica regardless of which cloud it's in. The Temporal-managed CNAME rewrites still work the same way; the harder problems are on the client side.

Plan for these three things:

1. **DNS overrides for both clouds.** Your private DNS for `region.tmprl.cloud` needs entries for both the AWS region (CNAME → AWS VPCE) and the GCP region (A → PSC IP). This typically means a Route 53 private hosted zone in your AWS Worker VPCs *and* a Cloud DNS private zone in your GCP Worker network — both for the same `region.tmprl.cloud` parent — each with the records relevant to the cloud the Workers run in.
2. **Worker reachability across clouds.** Your AWS-resident Workers must be able to reach the GCP PSC endpoint when GCP is active, and vice versa. Options include:
   - Run Workers in both clouds (preferred — simplest, lowest latency, matches the failover model).
   - Establish cross-cloud connectivity (e.g., AWS Transit Gateway + GCP Cloud Interconnect, or a third-party transit) so Workers in one cloud can resolve and reach the other cloud's private endpoint.
3. **Connectivity Rules in both regions.** GCP PSC requires a Connectivity Rule. AWS PrivateLink does not, but if you want to enforce private-only access, add one for the AWS side as well so the Namespace is private-only in both regions.

:::caution Alpine/musl + GCP PSC: missing AAAA records can break Workers

GCP Private Service Connect endpoints return only A (IPv4) records — there is no AAAA (IPv6) record. Most Linux distributions handle a missing AAAA gracefully, but **Alpine Linux's musl resolver returns a SERVFAIL** when AAAA is missing, which can cause Temporal SDK clients to fail name resolution after a failover from AWS to GCP.

If you run Workers on Alpine and use multi-cloud HA, either:

- Switch the Worker base image to a glibc-based distribution (Debian, Ubuntu, distroless), or
- Configure your application/runtime to disable AAAA lookups (e.g., set `GODEBUG=netdns=go+v4` for Go, or prefer IPv4 in the Java/Node/Python runtimes you use).

:::

To set up the DNS override, configure specific regions to target the internal VPC Endpoint IP addresses.
For example, you might set `aws-us-west-1.region.tmprl.cloud` to target `192.168.1.2`.
In AWS, this can be done using a Route 53 private hosted zone for `region.tmprl.cloud`.
Link that private zone to the VPCs you use for Workers.

A reasonable validation plan:

Consider how you'll configure Workers for this setup.
You can either have Workers run in both regions continuously or establish connectivity between regions using Transit Gateway or VPC Peering.
Either approach ensures Workers can access the newly activated region once failover occurs.

### Available regions, PrivateLink endpoints, and DNS record overrides

:::caution

The `sa-east-1` region is not yet available for use with Multi-region Namespaces. Currently, it is the only region on the continent.

:::

The following tables list the available Temporal regions and the DNS record overrides used for HA + private connectivity:

### AWS regions and PrivateLink endpoints

<JsonTable filename="/json/privatelink_aws.json" />

### GCP regions and Private Service Connect endpoints

<JsonTable filename="/json/privatelink_gcp.json" />

When using a Namespace with High Availability features, the Namespace's DNS record `<ns>.<account>.tmprl.cloud` points to a regional DNS record in the format `<provider>-<region>.region.tmprl.cloud`, where `<provider>-<region>` is the currently active region for your Namespace.

During failover, Temporal Cloud changes the target of the Namespace DNS record from one region to another. Namespace DNS records are configured with a 15-second TTL. Any DNS cache should re-resolve the record within this time. As a rule of thumb, receiving an updated DNS record takes about twice (2x) the TTL — clients should converge to the newly targeted region within, at most, a 30-second delay, assuming their resolver and language runtime honor the TTL.

---

## High Availability

Temporal keeps your Workflows running even when a Worker crashes. But what happens when a whole data center crashes? Or a region?

In the cloud, outages are commonplace. An outage can bring down a whole data center, cluster, region, or cloud provider. To be durable in the cloud, Workflows and applications must handle these outages smoothly, just like Temporal handles a Worker crash.

Temporal Cloud's High Availability features add extra reliability to Temporal Cloud Namespaces by handling cloud outages. Using asynchronous <ToolTipTerm term="replication"/> between multiple regions or cloud providers, combined with automatic outage detection and failover, High Availability keeps your Workflows running even during a cloud region outage.
This extra availability comes with an enhanced [SLA](/cloud/sla) of 99.99%, _including_ cloud provider outages.

:::tip White paper

For an in-depth guide covering everything from why you need High Availability to setting it up in production and advanced options, read the [High Availability White Paper](https://temporal.io/pages/high-availability-white-paper).

:::

## Built-in reliability

Even without High Availability features, Temporal Cloud provides robust reliability and a 99.9% contractual Service Level Agreement ([SLA](/cloud/sla)) guarantee against service errors.

Each standard Temporal Namespace uses replication across three [Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) (AZs) to ensure high availability.
An Availability Zone is akin to an isolated data center managed by a cloud hyperscaler, with independent power, networking, and cooling infrastructure.

Replication across AZs makes sure that any changes to Workflow state or History are saved in all three AZs _before_ the Temporal Service acknowledges a change back to the Client.
As a result, your standard Temporal Namespace stays operational even if one of its three AZs becomes unavailable.
This provides the basis of the 99.9% service level agreement for Temporal Cloud Namespaces.

However some critical use cases--such as customer-facing applications--require even better availability. That is where Temporal Cloud's High Availability features come in.

## High Availability features {/* #high-availability-features */}

High Availability features extend Temporal Cloud's replication across regions and cloud providers, so your Namespace keeps running even when a whole region or cloud provider goes down:

| **Deployment**                          | **Description**                                            |
| --------------------------------------- | ---------------------------------------------------------- |
| **Multi&#8209;region&nbsp;Replication** | Namespace is replicated across two cloud regions           |
| **Multi&#8209;cloud&nbsp;Replication**  | Namespace is replicated across different cloud providers   |

### Key features

- **Real-time replication** — Temporal replicates your Namespace across distant regions or cloud providers with no performance impact to your Workers or Workflows.
- **Automatic failover with 20-minute RTO** — Temporal manages failover with a 20-minute [RTO](/cloud/rpo-rto). You can also [trigger failover](/cloud/high-availability/failovers) manually at any time, for example for testing.
- **Transparent DNS routing** — On failover, DNS reroutes your [Namespace Endpoint](/cloud/namespaces#access-namespaces) to the active region. [Requests that reach the replica are forwarded to the active region automatically](#request-forwarding).
- **Sub-1-minute RPO** — In a failover during an outage, the [Recovery Point Objective](/cloud/rpo-rto) is under one minute.
- **Real-time lag monitoring** — Monitor your Namespace's replication lag in real time to understand your current RPO.
- **Conflict resolution** — If the two regions are not fully in sync at the time of failover, Temporal's conflict resolution process reconciles discrepancies and ensures data integrity.

:::info Region availability

You can usually choose your replica region, but the replica must be on the same continent as the primary region.
This means that a few Temporal Cloud regions do not yet support Multi-region Replication or Multi-cloud Replication.
See [Regions](/cloud/regions) for a full list of supported replica regions.

You can't enable both Multi-region Replication and Multi-cloud Replication on the same Namespace at the same time.

:::

### Multi-cloud Replication

Multi-cloud Replication spreads a Namespace across entirely different cloud providers, keeping your Namespace running even during a cloud-wide outage.
If a provider outage, service disruption, or network issue occurs, traffic automatically shifts to the replica.

Replicated data is encrypted and transmitted across the public internet between cloud providers.
This internet connectivity also allows Workers in one cloud to reach the replica in a different cloud during failover.
If you use [private connectivity](/cloud/high-availability/ha-connectivity), additional architecture work may be required to ensure your Workers can reach the replica region.

:::info

When you adopt Temporal's High Availability features, don't forget to consider the reliability of your own workers, infrastructure, and dependencies.
Issues like network outages, hardware failures, or misconfigurations in your own systems can affect your application performance.

For the highest level of reliability, distribute your dependencies across regions, and use our Multi-region or Multi-cloud replication features.
Using physically separated regions improves the fault tolerance of your application.

:::

## Request forwarding {/* #request-forwarding */}

A Namespace with High Availability features replicates across two regions, with one replica active and one passive at any moment. The active replica accepts reads and writes; the passive replica receives replicated state asynchronously and stands ready for failover.

When a request reaches the passive replica — for example, through the passive region's Regional Endpoint — Temporal Cloud forwards the request transparently to the active replica and the response back to the Worker. This allows Workers and Clients to connect to the passive region during healthy times, and when an outage hits, start processing Workflows immediately after a failover.

Forwarding adds a cross-region hop, so requests that travel through the passive replica complete with higher average latency than requests that reach the active replica directly.

To route Workers to the passive region's replica, see [How requests reach the replica](/cloud/high-availability/ha-connectivity#how-requests-reach-the-replica).

To disable passive region replica forwarding, see [Change the forwarding behavior](/cloud/high-availability/enable#change-forwarding-behavior).

## Service levels and recovery objectives

Namespaces using High Availability have a 99.99% [uptime SLA](/cloud/sla) with sub-1-minute [RPO](/cloud/rpo-rto) and 20-minute [RTO](/cloud/rpo-rto). For detailed information:

- [Service Level Agreement (SLA)](/cloud/sla)
- [Recovery Point Objective (RPO) and Recovery Time Objective (RTO)](/cloud/rpo-rto)

## Failover

High Availability Namespaces can automatically or manually [fail over](/cloud/high-availability/failovers) to the replica if the primary is unavailable or unhealthy.

## Target workloads

High Availability Namespaces are a great solution for Workloads where an outage would cause:

- Revenue loss
- Poor customer experience
- Problems stemming from policy/legal requirements that demand high availability

These are often major concerns for financial services, e-commerce, gaming, global SaaS platforms, bookings & reservations, delivery & shipping, and order management.

## Same-region Replication

In selected regions, you can add a replica to a Namespace in the same region.
Temporal operates a "cell architecture" and will replicate the Namespace across multiple cells in that region.
This feature is currently in [Public Preview](/evaluate/development-production-features/release-stages) in selected regions.

Failovers between cells are always managed automatically by Temporal. Unlike Multi-region and Multi-cloud Replication, you cannot disable automatic failovers and you cannot trigger a manual failover for a Same-region Replication Namespace. See [Failovers](/cloud/high-availability/failovers) for details.

## Related considerations

### External Storage

If your Workflows use [External Storage](/external-storage) to offload large payloads, durability of the external store
is a separate concern from Namespace replication.

- For S3, see [Durable External Storage](/external-storage#durable-external-storage) to see how CRR + MRAP can be used.
- For external storage providers other than what is listed above, we do not yet provide guidance. Consult the providers documentation for more information.

---

## Monitoring High Availability

Temporal Cloud offers several ways for you to track the health and performance of your
[High Availability](/cloud/high-availability) namespaces.

## Replication status

You can monitor your replica status with the Temporal Cloud UI. If the replica is unhealthy, Temporal Cloud disables the
"Trigger a failover" option to prevent failing over to an unhealthy replica. An unhealthy replica might be due to:

- **Data synchronization issues:** The replica fails to remain in sync with the primary due to network or performance
  problems.
- **Replication lag:** The replica falls behind the primary, causing it to be out of sync.
- **Network issues:** Loss of communication between the replica and the primary causes problems.
- **Failed health checks:** If the replica fails health checks, it's marked as unhealthy.

These issues prevent the replica from being used during a failover, ensuring system stability and consistency.

## Monitoring replication

Temporal Cloud's High Availability features use asynchronous replication between the primary and the replica. Workflow
updates in the primary, along with associated History Events, are transmitted to the replica. Replication lag refers to
the transmission delay of Workflow updates and history events from the primary to the replica.

:::tip

Temporal Cloud strives to maintain a <ToolTipTerm term="P95" /> replication lag of less than 1 minute. In this context,
P95 means 95% of updates are processed faster than this limit.

:::

A forced failover, when there is significant replication lag, increases the likelihood of rolling back Workflow
progress. Always check the replication lag metrics before initiating a failover.

Temporal Cloud emits replication lag [metrics](/cloud/metrics/openmetrics/metrics-reference#replication-metrics)
as pre-computed percentiles (p50, p95, p99) that are labeled with `temporal_namespace`.

When a Namespace is using a replica, you may notice that the Action count in `temporal_cloud_v1_total_action_count` is
2x what it was before adding a replica. This happens because Actions are replicated; they occur on both the primary and
the replica.

## Failover audit log

When Temporal triggers failovers, the [audit log](/cloud/audit-logs) will update with details.

Look for `"operation": "FailoverNamespace"` in the logs.

---

## Temporal Cloud guide

Welcome to the Temporal Cloud guide.

In this guide you will find information about Temporal Cloud, onboarding, features, and how to use them.

To create a Temporal Cloud account, sign up [here](https://temporal.io/get-cloud).

**[Get started with Temporal Cloud.](/cloud/get-started)**

## Become familiar with Temporal Cloud

- [Overview of Temporal Cloud](/cloud/overview)
  - [Security model](/cloud/security)
  - [Service availability](/cloud/service-availability) (availability, region support, throughput, latency, and limits)
  - [Account, Namespace, and application level configurations](/cloud/limits)
  - [Service Level Agreement (SLA)](/cloud/sla)
  - [Pricing](/cloud/pricing)
  - [Support](/cloud/support)

## Feature guides

- [Get started with Temporal Cloud](/cloud/get-started)
  - [Manage certificates](/cloud/certificates)
  - [Manage API keys](/cloud/api-keys)
  - [Manage Namespaces](/cloud/namespaces)
  - [Manage users](/cloud/users)
  - [Manage user groups](/cloud/user-groups)
  - [Manage billing](/cloud/billing)
  - [Manage Service Accounts](/cloud/service-accounts)
- [API key feature guide](/cloud/api-keys)
- [Metrics feature guide](/cloud/metrics)
- [Temporal Nexus](/cloud/nexus)
- [SAML authentication feature guide](/cloud/saml)
- [Cloud Ops API](/ops)
- [Audit logging feature guide](/cloud/audit-logs)
- [`tcld` (Temporal Cloud command-line interface) reference](/cloud/tcld)

---

## Account access

Access to Temporal Cloud is governed by role-based access control (RBAC). Within an account, each access principal, such
as user, user group or service account, has one account-level role and optionally, one or more Namespace-level
permissions. Each principal can only perform actions that are allowed by their assigned roles and permissions.

Temporal Cloud supports Security Assertion Markup Language (SAML) and System for Cross-domain Identity Management (SCIM)
for integration with your organization's identity provider (IdP). SAML enables single sign-on (SSO) by allowing your
identity provider to authenticate users into Temporal Cloud. SCIM automatically creates, updates, and removes users and
groups in Temporal Cloud based on changes in your identity provider.

## Temporal Cloud accounts

Accounts are the top-level container for access control. Each account has at least one user assigned the Account Owner
role, which has full administrative permissions across the account, including users, billing and usage. An account is
**not** an access principal itself.

When you sign up for Temporal Cloud without joining an existing account, you are automatically assigned the Account
Owner role for a new account. You can then invite other users to join the account and assign them roles. If your
organization has an IdP, we recommend using [a SAML integration](/cloud/saml) for enterprise identity management.

:::info

Multiple accounts can coexist on the same email domain. Each account can have its own independent SAML configuration,
tied to its unique Account ID.

However, each email address can only be associated with a single Temporal Cloud account. If you need access to multiple
accounts, you’ll need a separate invite for each one using a different email address.

:::

## Access principals

Temporal Cloud offers the following principals for access control:

- [**Users**](/cloud/users) - Manage individual user accounts and permissions
- [**User Groups**](/cloud/user-groups) - Organize users into groups for simplified access management
- [**Service Accounts**](/cloud/service-accounts) - Configure service accounts for automated access

These principals can assume [account-level roles](/cloud/manage-access/roles-and-permissions#account-level-roles) and be
granted [Namespace-level permissions](/cloud/manage-access/roles-and-permissions#namespace-level-permissions) to perform
actions within the account and a Namespace, respectively.

## Roles and permissions

Temporal Cloud's RBAC model works in a hierarchical manner. Account-level roles grant permissions to perform actions
within the account, and Namespace-level permissions grant permissions to perform actions within a Namespace. Refer to
the [Roles and permissions](/cloud/manage-access/roles-and-permissions) page for more details.

## Integration with identity providers

Temporal Cloud supports SAML and SCIM for integration with your organization's identity provider (IDP).

- [**SAML**](/cloud/saml) - Configure SAML-based SSO integration
- [**SCIM**](/cloud/scim) - Use your IDP to manage Temporal Cloud users and access via SCIM integration

## Troubleshoot account access issues

### Recover your account after losing access to your authenticator app {/* #mfa-recovery */}

Accounts registered with email and password require multi-factor authentication (MFA) with an authenticator app. If you
lose access to your authenticator app, you can still log in by clicking **Try another method** on the MFA screen. From
there, you can either:

- Enter your recovery code (provided when you first set up MFA)
- Receive a verification code through email

Once you're logged in, you can reset your authenticator app by navigating to **My Profile** > **Password and
Authentication** and then clicking **Authenticator App** > **Remove method**.

### Reset your password {/* #reset-password */}

If you're currently logged in and would like to change your password, click your profile icon at the top right of the
Temporal Cloud UI, navigate to **My Profile** > **Password and Authentication**, and then click **Reset Password**.

If you're not currently logged in, navigate to the login page of the Temporal Cloud UI, enter your email address, click
**Continue**, and then select **Forgot password**. In both cases, you will receive an email with instructions on how to
reset your password.

### Sign in after email domain changes {/* #email-domain-change */}

If your organization changed its email domain (for example, from `@oldcompany.com` to `@newcompany.com`), you may be
unable to sign in to Temporal Cloud with your existing account.

**Why this happens:** When you sign in using "Continue with Google" or "Continue with Microsoft", Temporal Cloud
identifies your account by your email address. If your email address changes, Temporal Cloud sees this as a different
identity and cannot match it to your existing account.

**How to resolve this:** [Create a support ticket](/cloud/support#support-ticket) with the following information:

- Your previous email address (the one originally used to access Temporal Cloud)
- Your new email address
- Your Temporal Cloud Account Id (if known)

Temporal Support can update your account to use your new email address.

:::tip Use SAML for enterprise identity management

If your organization frequently changes email domains or wants centralized control over user authentication, consider
using [SAML authentication](/cloud/saml). With SAML, your identity provider (IdP) manages user identities, and email
domain changes can be handled within your IdP without affecting Temporal Cloud access.

:::

---

## Permissions reference

Temporal Cloud access controls are organized across two scopes:

- Account-level role permissions
- Namespace-level permissions

Within each scope, permissions apply to publicly documented [Temporal Cloud Ops API](https://docs.temporal.io/ops)
endpoints and to additional non-Cloud Ops capabilities, such as Temporal Cloud UI and internal automation behaviors.

## Account-level access {/* #account-level-access */}

Account-level access is granted to users and service accounts by assigning them an account-level role. Temporal Cloud
supports the following account-level roles:

- Account Owner
- Global Admin
- Developer
- Finance Admin
- Read-Only

### Cloud Ops API permissions

This table provides API-level details for permissions granted through account-level roles. These permissions are
configured per user.

| Permission                  | Read-only | Developer | Finance Admin | Global Admin | Account Owner |
| --------------------------- | :-------: | :-------: | :-----------: | :----------: | :-----------: |
| [AddUserGroupMember](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/groups/POST/cloud/user-groups/%7BgroupId%7D/members)          |           |           |               |      ✔       |       ✔       |
| [CreateAccountAuditLogSink](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/account/POST/cloud/audit-log-sinks)   |           |           |               |      ✔       |       ✔       |
| [CreateApiKey](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/api-keys/POST/cloud/api-keys)                |    ✔\*    |    ✔\*    |      ✔\*      |     ✔\*      |      ✔\*      |
| [CreateConnectivityRule](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/connectivity-rules/POST/cloud/connectivity-rules)      |           |           |               |      ✔       |       ✔       |
| [CreateNamespace](https://saas-api.tmprl.cloud/docs/httpapi.html#tag/namespaces/POST/cloud/namespaces)             |           |     ✔     |               |      ✔       |       ✔       |
