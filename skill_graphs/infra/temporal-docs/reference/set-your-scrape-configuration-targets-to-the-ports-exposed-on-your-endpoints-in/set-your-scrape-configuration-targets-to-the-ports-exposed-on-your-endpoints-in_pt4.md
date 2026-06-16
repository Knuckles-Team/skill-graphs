  providers.

Even though the RPO target is under 1 minute, data is virtually never "lost" thanks to Temporal's built-in Recovery and
Conflict Resolution process, which reconciles state between the active and replica when a failover occurs.

## How RTO and RPO are measured {/* #how-rto-and-rpo-are-measured */}

Temporal Cloud achieves its RTO and RPO targets through [High Availability](/cloud/high-availability) replication. The
following sections explain how each metric is measured and what factors can affect them.

### RPO {/* #how-rpo-is-measured */}

Unlike a traditional database where data within the recovery point window may be permanently lost, Temporal Cloud
durably persists all acknowledged data. After an outage resolves, Temporal's Recovery and Conflict Resolution process
automatically syncs data back into the Namespace. The RPO therefore reflects the maximum data that may be _temporarily
unavailable_ in the replica at the moment of failover, not data that is permanently lost.

Temporal keeps replicas up to date using
[asynchronous replication](https://youtu.be/mULBvv83dYM?si=RDeWb3gVsEtgGM4z&t=334), with monitoring, alerting, and
internal SLOs on replication lag for every Namespace.

User actions on a Namespace can affect the recovery point. For example, suddenly spiking into much higher throughput
than a Namespace has seen before could create a period of replication lag where the replica falls behind the active.

Temporal provides a
[replication lag](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_replication_lag_p99) metric for each
Namespace. This metric approximates the recovery point the Namespace would achieve in a worst-case failure at that
moment. Temporal recommends monitoring the replication lag and alerting if it rises above 1 minute.

### RTO {/* #how-rto-is-measured */}

The Recovery Time for a given incident is measured from the moment the incident begins to cause abnormal Namespace
operation — for example, when unavailability or error rates rise above an acceptable level — to the moment the Namespace
is restored to full functionality.

For most incidents, the vast majority of the Recovery Time is spent detecting the incident, determining the affected
boundary (a single cell, a region, or an entire cloud), and deciding to fail Namespaces over to their replicas. The
actual time to complete the failover is usually a very small piece of the Recovery Time.

This Recovery Time covers only the Temporal Namespace. Your application's overall Recovery Time also depends on having
enough healthy Workers that can reach the Namespace and process Workflows. Maintaining sufficient Worker capacity that
can reach the replica region (or replica cloud) during a failover is your responsibility. You are also responsible for
failing over any other regional dependencies your application relies on, such as replicated application databases.

## Tips for a lower Recovery Time

To achieve the lowest possible recovery times, Temporal recommends that you:

- Keep automatic failovers enabled on your Namespace (the default)
- Invest in a process to detect outages and trigger a manual failover.

You can trigger manual failovers on your Namespaces even if automatic failovers are enabled. There are several
benefits to combining a manual failover process with automatic failovers:

- You can detect outages that Temporal doesn't. In the cloud, regional outages don't affect all services equally. It's
  possible that Temporal--and the services it depends on--are unaffected by the outage, even while your Workers or other
  cloud infrastructure are disrupted. If you
  [monitor services in your critical path](https://sre.google/sre-book/monitoring-distributed-systems/) and alert on
  unusual error rates, you may catch outages before Temporal Cloud does.

- You can sequence your failovers in a particular order. Your cloud infrastructure probably contains more pieces than
  just your Temporal Namespace: Temporal Workers, compute pools, data stores, and other cloud services. If you manually
  fail over, you can choose the order in which these pieces switch to the replica region. You can then test that
  ordering with failover drills and ensure it executes smoothly without data consistency issues or bottlenecks.

- You can proactively fail over more aggressively than Temporal. While the 20-minute RTO should be sufficient for most
  use cases, some may strive to hit an even lower RTO. For workloads like high frequency trading, auctions, or popular
  sporting events, an outage at the wrong time could cause tremendous lost revenue per minute. You can adopt a posture
  that fails over more eagerly than Temporal does. For example, you could trigger a manual failover at the first sign of
  a possible disruption, before knowing whether there's a true regional outage.

- Even if you have robust tooling to detect an outage and trigger a failover, leaving automatic failovers
  enabled provides a "safety net" in case your automation misses an outage. It also gives Temporal leeway to
  preemptively fail over your Namespace if we detect that it may be disrupted soon, e.g., by a rolling failure that has
  impacted other Namespaces but not yours, yet.

## Comparing RTO and SLA

Temporal has both a Recovery Time Objective (RTO) and a Service Level Agreement (SLA). They serve complementary purposes
and apply in different situations.

| Aspect                            | RTO                                                                                                                                                                                                                                                          | SLA                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| What is it?                       | An objective, or high-priority goal, for the total time that an outage disrupts a Namespace.                                                                                                                                                                 | A contractual agreement that sets an upper bound on the service error rate, with financial repercussions.                                                                                                                                                                                                                                                                                                                                                                      |
| How is it measured?               | The achieved recovery time is measured in terms of minutes per outage.                                                                                                                                                                                       | The achieved service error rate is measured in terms of error rate per month.                                                                                                                                                                                                                                                                                                                                                                                                  |
| How is the calculation performed? | The achieved recovery time in a given outage is the total time between when a disruption to a Namespace began and when the Namespace was restored to full functionality, either after a failover to a healthy region or after the outage has been mitigated. | Temporal measures the percentage of requests to Temporal Cloud that fail, and applies a [formula](/cloud/sla) to get the final percentage for the month.                                                                                                                                                                                                                                                                                                                       |
| Do partial degradations count?    | Most outages contain periods of **partial degradation** where some percentage of Namespace operations fail while the rest complete as normal. When they disrupt a Namespace, periods of partial degradation count in the calculation of the recovery time.   | Partial degradations only partially count for the service error rate calculation. A 5-minute window with a 10% error rate would count less than a 5-minute window with a 100% error rate.                                                                                                                                                                                                                                                                                      |
| What is excluded?                 | For partial degradations, what counts as a disruption to a Namespace is subject to Temporal's expert judgment, but a good rule of thumb is a service error rate >=10%.                                                                                       | We exclude outages that are out of Temporal's control to mitigate, e.g., a failure of the underlying cloud provider infrastructure that affects a Namespace without High Availability and automatic failovers enabled. If a Namespace has the relevant High Availability feature and has automatic failovers enabled, then Temporal can act to mitigate the outage and it does usually count against the SLA. Full exclusions on the [SLA page](/cloud/sla). |

The following examples illustrate the RTO and SLA calculations for different types of outages in a regional outage. These
hypothetical Namespaces are based on actual Temporal Cloud performance in a
[real-world outage](https://temporal.io/blog/how-devs-kept-running-during-the-aws-us-east-1-oct-20-2025).

Suppose that region `middle-earth-1` experienced a cascading failure starting at 10:00:00 UTC, causing various instances
and machines to fail over time. Temporal's automatic failover triggered for all Namespaces and completed at 10:15:00
UTC.

- Namespace 0 was in the region but its cell was not affected by the outage. The only downtime it had was for a few
  seconds during the failover operation. It experienced a near-zero Recovery Time, and its service error rate was
  negligible. Graceful failover was successful, and this Namespace achieved a recovery point of 0.

- Namespace 1_A was in the region and its cell experienced a partial degradation that caused 10% of requests to fail in
  the first 5 minutes, 25% in the second five minutes, and 50% in the third five minutes. Since it was significantly
  impacted from 10:00:00 to 10:15:00, its Recovery Time was 15 minutes. If it had no other service errors that month,
  then its service error rate for the month would be: ( (1 - 10%) + (1 - 25%) + (1 - 50%) + 8925 \* 100% ) / 8928 =
  99.990%. (Note: there are 8928 5-minute periods in a 31-day month.) Graceful failover was successful, and this
  Namespace achieved a recovery point of 0.

- Namespace 1*B was in the same cell as Namespace 2_A, so it also experienced a partial degradation that caused 10% of
  requests to fail. However, its owner detected the outage via their own tooling and decided to manually fail over at
  10:05:00. This Namespace achieved a recovery time of 5 minutes and a service error rate of ( 1 * (1 - 10%) + 8927 \_
  100% ) / 8928 = 99.998%. Graceful failover was successful, and this Namespace achieved a recovery point of 0.

- Namespace 2*A was in the region and its cell was fully network partitioned at the start of the outage, causing 100% of
  requests to fail. Since it was significantly impacted from 10:00:00 to 10:15:00, its Recovery Time was 15 minutes. If
  it had no other service errors that month, then its service error rate for the month would be: ( 3 * (1 - 100%) + 8928
  \_ 100% ) / 8640 5-minute periods per month = 99.97%. Because the Namespace was network partitioned, graceful failover
  did not succeed, and forced failover was used. The recovery point achieved was equal to the replication lag at the
  time of the network partition, which was a few seconds.

- Namespace 2*B was in the region and was fully network partitioned, causing 100% of requests to fail. However, its
  owner detected the outage via their own tooling and decided to manually fail over at 10:05:00. This Namespace achieved
  a recovery time of 5 minutes and a service error rate of ( 1 5-minute periods * (1 - 100%) + 8639 5-minute periods \_
  100% ) / 8640 5-minute periods per month = 99.99%. Because the Namespace was network partitioned, graceful failover
  did not succeed, and forced failover was used. The recovery point achieved was equal to the replication lag at the
  time of the network partition, which was a few seconds.

All of the above Namespaces were in the affected region and beat the 1-minute RPO. But they achieved varying recovery
times and service error rates.

- Notice how Namespace 1_A and Namespace 2_A were both automatically failed over with **the same recovery time but
  different service error rates**. Notice how Namespace 2_B and Namespace 1_A happen to have the **same service error
  rate but different recovery times**. This illustrates how RTO and SLA can differ, even in the same outage. Both are
  valuable tools for Temporal Cloud users to measure the availability of their Namespaces.

- Notice how the Namespaces that were manually failed over (Namespace 1_B and Namespace 2_B) achieved lower recovery
  times than the Namespaces that were automatically failed over (Namespace 1_A and Namespace 2_A). This illustrates how
  **proactive, aggressive manual failover can achieve a better recovery time than automatic failover**.

---

## SAML authentication

Integrating with your organization's identity provider (IdP) with Temporal Cloud through Security Assertion Markup
Language (SAML) 2.0 allows you to authenticate users of your Temporal Cloud account using your organization's IdP. This
allows you to enforce your corporate identity policies, such as multi-factor authentication (MFA), password complexity,
and reduces the risk of credential theft.

SAML is included in the Business, Enterprise, and Mission Critical plans. For more details, refer to
[Temporal Cloud pricing](/cloud/pricing#base_plans).

## Integrate SAML with your Temporal Cloud account

1. Locate your [Temporal Cloud Account Id](/cloud/namespaces#temporal-cloud-account-id). Your Account Id can be viewed
   and copied from the Temporal Cloud user profile dropdown menu in the top right corner. Alternatively, find your
   [Namespace Id](/cloud/namespaces#temporal-cloud-namespace-id). The Account Id is the five or six characters following
   the period (.), such as `f45a2`. You will need the Account Id to construct your callback URL and your entity
   identifier.
1. Configure SAML with your IdP by following one of these sets of instructions:
   - [Microsoft Entra ID](#configure-saml-with-azure-ad)
   - [Okta](#configure-saml-with-okta)
1. [Share your connection information with us and test your connection.](#finish-saml-configuration)

## How to configure SAML with Microsoft Entra ID {/* #configure-saml-with-azure-ad */}

If you want to use the general Microsoft login mechanism, you don't need to set up SAML with Entra ID. Just select
**Continue with Microsoft** on the Temporal Cloud sign-in page.

To use Entra ID as your SAML IdP, create a Microsoft Entra ID Enterprise application.

1. Sign in to the [Microsoft Entra ID](https://portal.azure.com/).
1. On the home page, under **Manage Microsoft Entra ID**, select **View**.
1. On the **Overview** page near the top, select **Add > Enterprise application**.
1. On the **Browse Microsoft Entra ID Gallery** page near the top, select **Create your own application**.
1. In the **Create your own application** pane, provide a name for your application (such as `temporal-cloud`) and
   select **Integrate any other application you don't find in the gallery**.
1. Select **Save**.
1. In the **Getting Started** section, select **2. Set up single sign on**.
1. On the **Single sign-on** page, select **SAML**.
1. In the **Basic SAML Configuration** section of the **SAML-based Sign-on** page, select **Edit**.
1. In **Identifier (Entity ID)**, enter the following entity identifier, including your Account Id where indicated:

   ```bash
   urn:auth0:prod-tmprl:ACCOUNT_ID-saml
   ```

   A correctly formed entity identifier looks like this:

   ```bash
   urn:auth0:prod-tmprl:f45a2-saml
   ```

1. In **Reply URL (Assertion Consumer Service URL)**, enter the following callback URL, including your Account Id where
   indicated:

   ```bash
   https://login.tmprl.cloud/login/callback?connection=ACCOUNT_ID-saml
   ```

   A correctly formed callback URL looks like this:

   ```bash
   https://login.tmprl.cloud/login/callback?connection=f45a2-saml
   ```

1. In **Sign on URL**, enter the following login url, including your Account Id where indicated:

   ```bash
   https://cloud.temporal.io/login/saml?connection=ACCOUNT_ID-saml
   ```

   A correctly formed login URL looks like this:

   ```bash
   https://cloud.temporal.io/login/saml?connection=f45a2-saml
   ```

1. You can leave the other fields blank. Near the top of the pane, select **Save**.
1. In the **Attributes & Claims** section, select **Edit**. Configure the following settings. Under **Required claim**:
   - Set **Unique User Identifier (NameID)** to `user.userprincipalname`
   - Set the **NameID format** to `emailAddress`

   These are the default settings for Microsoft Entra ID. Then under **Additional claims**, ensure **Email** and
   **Name** are present.

1. Collect information that you need to send to us:
   - In the **SAML Certificates** section of the **SAML-based Sign-on** page, select the download link for **Certificate
     (Base64)**.
   - In the **Set up _APPLICATION_NAME_** section of the **SAML-based Sign-on** page, copy the value of **Login URL**.

To finish setting up Microsoft Entra ID as your SAML IdP, see [Finish SAML configuration](#finish-saml-configuration).

## How to configure SAML with Okta {/* #configure-saml-with-okta */}

To use Okta as your SAML IdP, configure a new Okta application integration.

1. Sign in to the [Okta Admin Console](https://www.okta.com/login/).
1. In the left navigation pane, select **Applications > Applications**.
1. On the **Applications** page, select **Create App Integration**.
1. In the **Create a new app integration** dialog, select **SAML 2.0** and then select **Next**.
1. On the **Create SAML Integration** page in the **General Settings** section, provide a name for your application
   (such as `temporal-cloud`) and then select **Next**.
1. In the **Configure SAML** section in **Single sign on URL**, enter the following callback URL, including your Account
   Id where indicated:

   ```bash
   https://login.tmprl.cloud/login/callback?connection=ACCOUNT_ID-saml
   ```

   A correctly formed callback URL looks like this:

   ```bash
   https://login.tmprl.cloud/login/callback?connection=f45a2-saml
   ```

1. In **Audience URI (SP Entity ID)**, enter the following entity identifier, including your Account Id where indicated:

   ```bash
   urn:auth0:prod-tmprl:ACCOUNT_ID-saml
   ```

   A correctly formed entity identifier looks like this:

   ```bash
   urn:auth0:prod-tmprl:f45a2-saml
   ```

1. We require the user's full email address when connecting to Temporal.
   - In **Name ID format**, select `EmailAddress`.
   - In **Attribute Statements**, set **email** and **name**.
1. Select **Next**.
1. In the **Feedback** section, select **Finish**.
1. On the **Applications** page, select the name of the application integration you just created.
1. On the application integration page, select the **Sign On** tab.
1. Under **SAML Setup**, select **View SAML setup instructions**.
1. Collect information that you need to send to us:
   - Copy the IdP settings.
   - Download the active certificate.

To finish setting up Okta as your SAML IdP, see the next section,
[Finish SAML configuration](#finish-saml-configuration).

## How to finish your SAML configuration {/* #finish-saml-configuration */}

After you configure SAML with your IdP, we can finish the configuration on our side.
[Create a support ticket](/cloud/support#support-ticket) that includes the following information:

- The sign-in URL from your application
- The X.509 SAML sign-in certificate in PEM format
- One or more IdP domains to map to the SAML connection

Generally, the provided IdP domain is the same as the domain for your email address. You can provide multiple IdP
domains.

When you receive confirmation from us that we have finished configuration, log in to Temporal Cloud. This time, though,
enter your email address and click **Continue**. You will be directed to the authentication page of your IdP.

---

## SCIM user management

[SCIM](https://scim.cloud/) lets you integrate your identity provider (IdP) with Temporal Cloud to automate user provisioning and access. Once SCIM is configured, changes in your IdP are automatically reflected in Temporal Cloud, including:

- User creation / onboarding
- User deletion / offboarding
- User membership in groups

You can map SCIM groups to Temporal Cloud [roles and permissions](/cloud/manage-access/roles-and-permissions), so users automatically get the Temporal Cloud access they need based on the groups they belong to.

:::info

SCIM is a paid feature. See the [pricing page](/cloud/pricing) for details.

:::

## Supported IdP Vendors

Supported upstream IdP vendors include:
* [Okta](#configure-scim-with-okta)
* Microsoft Entra ID (Azure AD)
* Google Workspace
* OneLogin
* CyberArk
* JumpCloud
* PingFederate
* Any SCIM 2.0-compliant provider

## Preparing for SCIM

Before starting your work with SCIM, you'll need to complete this checklist:

1. Configure [SAML](/cloud/saml) SSO.
1. Identify your organization's **IdP administrator**, who is responsible for configuring and managing your SCIM integration.
   Specify their contact details when you reach out to support in the next stage of this process.

After completing these steps, you're ready to submit your [support ticket](/cloud/support#support-ticket) to enable SCIM.

:::tip Adding and removing users

When SCIM is enabled for user management, you can still add and remove users outside of SCIM using the Temporal Cloud interface, until you disable user lifecycle management.
You can always change a user's or group's Account Role from the Temporal Cloud interface.

:::

## Onboarding with SCIM and Okta {/* #configure-scim-with-okta */}

1. Temporal Support enables the SCIM integration on your account.
   Enabling integration automatically emails a configuration link to your Okta administrator.
   This authorizes them to set up the integration.
1. Your Okta administrator opens the supplied link.
   The link leads to step-by-step instructions for configuring the integration.
1. Once configured in Okta, Temporal Cloud will begin to receive SCIM messages and automatically onboard and offboard the users and groups configured in Okta.

Some points to note:

- User and group change events are applied within 10 minutes of them being made in Okta.
- User lifecycle management with SCIM also allows user roles to be derived from group membership.
- Once a group has been synced in Temporal Cloud, you can use `tcld` to assign roles to the group.
  For instructions, see the [User Group Management](https://github.com/temporalio/tcld?tab=readme-ov-file#user-group-management) page.

---

## Monitor Temporal Cloud

Temporal Cloud metrics help monitor production deployments.
This documentation covers best practices for monitoring Temporal Cloud.

## Monitor availability issues

When you see a sudden drop in Worker resource utilization, verify whether Temporal Cloud's API is showing increased latency and error rates.

### Reference Metrics

- [temporal\_cloud\_v1\_service\_latency\_p99](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_service_latency_p99)

This metric measures latency for `SignalWithStartWorkflowExecution`, `SignalWorkflowExecution`, `StartWorkflowExecution` operations.
These operations are mission critical and never [throttled](/cloud/service-availability#throughput).
This metric is a good indicator of your lowest possible latency for the 99th percentile of requests.
