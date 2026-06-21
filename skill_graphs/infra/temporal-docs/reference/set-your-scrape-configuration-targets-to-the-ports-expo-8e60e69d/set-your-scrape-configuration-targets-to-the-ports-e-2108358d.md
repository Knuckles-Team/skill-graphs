is [supported](/cloud/limits#default-retention-period) in Temporal Cloud. In these cases it is recommended to utilize
[archival](/temporal-service/archival) to store closed Workflows that cannot be migrated. In general, archival is
recommended over large retention periods since the extra data can stress the persistence layer of the system.

### I am using payload encryption in my self-hosted Temporal cluster. Is this supported in cloud?
Yes. If payloads are already [encrypted](/payload-codec#encryption) in your self-hosted server via data converter, then
they will remain encrypted during and after migration.

### I would like to enable payload encryption as part of the migration. Is this supported?
The automated migration tooling cannot add payload encryption. To encrypt payloads sent to Temporal Cloud, you must encrypt
payloads in your cluster before starting the automated migration process.

---

## Estimate Actions for migration

Before you migrate from a self-hosted Temporal Service to Temporal Cloud, you can measure your current Action usage to help predict your Cloud usage and costs.

Use server metrics to estimate Actions per second (APS) and peak load.
Use representative Workflow Execution Histories to understand how many Actions a typical Workflow Execution creates.
Estimate storage separately from Actions.

For details about which operations count as Actions in Temporal Cloud, see [Temporal Cloud Actions](/cloud/actions).

## Choose an estimation method

Use one or more of the following methods depending on what you need to estimate.

| Method | Use it to estimate | Notes |
| --- | --- | --- |
| Self-hosted server metrics | APS, peak APS, and Action counts over a fixed time range | Best for sizing Namespace limits and understanding usage patterns. |
| Workflow Execution History samples | Actions per representative Workflow Execution | Best for understanding workload shape by Workflow Type. Some [Actions do not appear](/cloud/actions) in Event History. |
| Storage estimates | Event History storage | Storage is [priced separately](/cloud/pricing#pricing-model) from Actions. |

## Estimate APS from self-hosted server metrics

Temporal Server versions later than 1.17 provide an `action` metric.
Use this metric to estimate Actions per second from a self-hosted Temporal Service.

Temporal Server versions 1.22.3 and later provide an `action` metric that more closely reflects current Temporal Cloud Action pricing, including Local Activity metering.
For Temporal Server versions from 1.17 through 1.22.2, use the `action` metric to understand server load, but do not treat it as a precise billable Action estimate.

To calculate total APS, use the following PromQL query:

```promql
sum(rate(action{service_name="frontend"}[1m]))
```

To calculate APS by Namespace, use the following PromQL query:

```promql
sum(rate(action{service_name="frontend"}[1m])) by (exported_namespace)
```

Depending on your metrics exporter setup, the Namespace label might be `namespace` instead of `exported_namespace`.

For a Grafana dashboard example, see the [`server-general.json`](https://github.com/temporalio/dashboards/blob/master/server/server-general.json) dashboard in the Temporal dashboards repository.

For Datadog, use a query like the following to calculate Actions per second:

```text
sum:io.temporal.server.action.count{$server-name}.as_rate()
```

## Estimate Action counts over a fixed time range

To estimate total Actions during a fixed time range, use `increase()` over the range you want to measure.

For example, to estimate total Actions over 30 days, use the following PromQL query:

```promql
sum(increase(action{service_name="frontend"}[30d]))
```

To estimate Actions for one Namespace, add the Namespace label:

```promql
sum(increase(action{service_name="frontend", exported_namespace="default"}[30d]))
```

When you run fixed-range queries in Grafana, set the end of the dashboard time window to the end of the date range that you want to measure.
For example, to measure Actions for the 30-day period ending March 31, set the dashboard end time to March 31.

## Estimate Actions from Workflow Execution Histories

You can estimate Actions per Workflow Execution by counting billable events in representative Workflow Execution Histories.
This method is useful when you need to understand how much Action usage a Workflow Type creates.

1. Choose representative Workflow Executions for each Workflow Type.
2. Download the Event History for each Workflow Execution from the Web UI or API.
3. Count the events that map to Temporal Cloud Actions.
   For the list of Action types and corresponding History Event types, see [Temporal Cloud Actions](/cloud/actions).
4. Multiply the Action count by the expected number of Workflow Executions in the period you want to estimate.

This method produces an estimate.
Some Actions do not appear directly in Event History, including Queries and some Activity Heartbeat Actions.
If you use Global Namespaces, account for the additional Action and storage cost.
Estimate storage separately from Workflow Action counts.

## Estimate storage separately

Temporal Cloud storage is priced separately from Actions.
To estimate storage, collect the following information:

- Event History size for representative Workflow Executions.
- Retention Period for closed Workflow Executions.
- Duration for open Workflow Executions.
- Expected number of Workflow Executions.

For current storage pricing, see [Temporal Cloud pricing](/cloud/pricing).

---

## Migrate

Learn how to migrate your Temporal workflows with zero downtime:

- [Automated Migration](/cloud/migrate/automated) - This process enables seamless transitions from self-hosted Temporal instances to Temporal Cloud.
- [Manual Migration](/cloud/migrate/manual) - This process enables transitions from self-hosted Temporal instances to Temporal Cloud by updating clients
  and workflows to utilize new resources within Temporal Cloud.
- [Migrate between regions](/cloud/migrate/migrate-within-cloud) - This process allows you to migrate a Temporal Cloud Namespace between regions or providers.
- [Estimate Actions](/cloud/migrate/estimate-actions) - This process helps you estimate Actions and Actions per second from a self-hosted Temporal Service before migrating to Temporal Cloud.

---

## Manual migration

Migrating to Temporal Cloud from a self-hosted Temporal Service will have different requirements depending on your usage.
This guide provides some guidance based on our experience helping customers of all sizes successfully migrate.

### What to expect from a migration

Depending on your Workflows' requirements, the migration process may be as simple as changing a few parameters, or may require more extensive code changes.
There are two aspects to consider when migrating: your Temporal Client connection code and your Workflow Executions.
Here's a high-level overview of what you can expect:

- **Introduce another Temporal Client to your Starter and Worker Processes:** Configure and deploy a new Temporal Client so that Temporal Cloud becomes responsible for new Workflow Executions.
- **Migrate Workflow Executions:** There are different approaches for new, running, and completed Workflow Executions.
  - **New Workflow Executions:** When you no longer need to send Signals or Queries to your self-hosted Temporal Service, you can deprecate your old Client code. Until then, your self-hosted Temporal Service can receive relevant traffic, while new Workflow Executions are sent to Temporal Cloud.
  - **Running Workflow Executions:** Short-running Workflows can often be drained and then started again on Temporal Cloud. Long-running Workflows that cannot be drained might require you to implement more code changes to pass the state of the currently running Workflow to Temporal Cloud.
  - **Completed Workflow Executions:** Completed Workflow Execution History cannot be automatically migrated to Temporal Cloud. Refer to [Multi-Cluster Replication](#multi-cluster-replication) for more information.

### Updating Client connection code in your Workers

Whether you're self-hosting Temporal or using Temporal Cloud, you manage runtime of your code.
To migrate your Workflows to Temporal Cloud, you need to change some parameters in the Client connection code, such as updating the namespace and gRPC endpoint.

The changes needed to direct your Workflow to your Temporal Cloud
Namespace are only a few lines of code, including:

- Add your [SSL certificate and private key](/cloud/certificates) or [API key](/cloud/api-keys) associated with your Namespace.
- [Copy the Cloud-hosted endpoint](/cloud/namespaces#temporal-cloud-grpc-endpoint) from the Namespace detail Web page.
  The endpoint uses this format: `<namespace_id>.<account_id>.tmprl.cloud:port`.
- [Connect to Temporal Cloud](/cloud/get-started) with your Client.
- [Configure tcld, the Cloud CLI](/cloud/tcld), with the same address, Namespace, and
  certificate used to create a Client through code.

### Migrating your Workflow Executions

A Temporal Service stores the complete Event History for the entire lifecycle of a
Workflow Execution.
To migrate from a self-hosted Temporal Service to Temporal Cloud, take into account the current state, Event History, and any future expectations of your Workflow Executions.

**New Workflows are automatically executed on Temporal Cloud.**
Once you've made the code changes in Step 1, and your new code is deployed, new Workflow Executions will be sent to Temporal Cloud.
Existing Workflows must receive Signals to migrate and re-execute on Cloud.
If you maintain your self-hosted instance, you will still be able to use it to access any execution history from before your migration.
You can also export JSON from your previous execution history, that you can then import into your own analytics system.

**Running Workflows can either be drained or migrated.**
If your Workflow can be completed before any compelling event which drives a move to Temporal Cloud, those Workflows can be automatically restarted on Temporal Cloud.
If your Workflows need to run continuously, you must migrate Workflows while they are running.
To accomplish this migration, cancel your current Workflow and pass the current state to a new Workflow in Temporal Cloud.
Refer to [this repository](https://github.com/temporalio/temporal-migration) for an example of migrating running Workflows in Java.

When performing a live migration, make sure your Worker capacity can support the migration load.
Both a [Signal](/sending-messages#sending-signals) and a [Query](/sending-messages#sending-queries) will be executed during the course of the migration.
Also, the Query API loads the entire history of Workflows into Workers to compute the result (if they are not already cached).
That means that your self-hosted Temporal Service Worker capacity will need to support having those executions in memory to serve those requests.
The volume of these requests might be high to execute against all the matches to a `ListFilter`.

### Considerations when resuming Workflows on a new Temporal Service or Namespace

- **Skipping Steps:** If your Workflow steps cannot guarantee idempotency, determine whether you need to skip those steps when resuming the execution in the target Namespace.
- **Elapsed Time:** If your Workflow is “resuming sleep” when in the target Namespace, determine how you will calculate the delta for the sleep invocation in the new execution.
- **Child Relationships:** If your Workflow has Child Workflow relationships (other than Detached Parent Close Policy children), determine how you can pass the state of those children into the parent to execute the child in a resumed state.
- **Heartbeat state:** If you have long running activities relying on heartbeat state, determine how you can resume these activities in the target Namespace.
- Child Workflows with the same type as their Parent types are returned in List Filters used to gather relevant executions. Unless these are Detached `ParentClosePolicy` children, this is not what you want since the Parent/Child relationship will not be carried over to the target Namespace.
- Long running activities that use heartbeat details will not receive the latest details in the target Namespace.
- Duration between Awaitables inside a Workflow definition needs to be considered for elapsed time accuracy when resuming in the target Namespace.
- When Signaling directly from one Workflow to another, make sure to handle `NotFound` executions in the target Namespace. The Workflows may resume out of order.

### Other considerations when migrating

- Have you added an mTLS certificate to your Temporal Namespace? Review our [documentation for adding a certificate to your Temporal Cloud account](/cloud/certificates) for more information.
- There are differences in how metrics are generated in self-hosted Temporal and Temporal Cloud. Review the [documentation on Temporal Cloud metrics](/cloud/metrics/) for more information.
- Consider the implications for [security and access to your Temporal Service](/cloud/security).
- Review your current load with [Action estimates](/cloud/migrate/estimate-actions) and speak to your Account Executive and Solutions Architect so we can set appropriate [Namespace limits](/cloud/limits).

### Multi-Cluster Replication

[Multi-Cluster Replication](/self-hosted-guide/multi-cluster-replication) is an experimental feature which asynchronously replicates Workflow Executions from active Clusters to other passive Clusters for backup and state reconstruction.
Migrating Execution History from a self-hosted Temporal Service to Temporal Cloud is not currently supported.
However, a migration tool based on Multi-Cluster Replication, which will enable this, is currently in development for Temporal Cloud.
If you have used this feature locally or you are interested in using it to migrate to Temporal Cloud, [create a support ticket](https://docs.temporal.io/cloud/support) or watch this space for more information about public availability.

---

## Migrate between regions

Temporal Cloud's [High Availability features](/cloud/high-availability) allow you to migrate a Temporal Cloud Namespace from one region or cloud provider to another with zero downtime.

## Preparing to migrate

Namespaces using Export will need to stop Export and migrate the region configuration to the new region for Export jobs to continue after migration.
See [failover scenarios](/cloud/export#failover-scenarios) for details.

[Using High Availability features affects pricing](/cloud/pricing#high-availability-features).

:::info Using AWS PrivateLink or GCP Private Service Connect?

If the Namespace uses Private Connectivity, the steps below need additional DNS and VPC Endpoint work. Follow [How to migrate to another Temporal Cloud Region when using Private Connectivity](/cloud/high-availability/ha-connectivity#how-to-migrate-regions-with-private-connectivity) instead of (or alongside) the public steps below.

:::

## Steps to migrate

1. Add a Namespace replica in the region you want to migrate to. See [regions](/cloud/regions) for a list of available regions and supported multi-region and multi-cloud configurations.

<CaptionedImage
    src="/img/cloud/high-availability/migrate/1-add-replica.png"
    title="Add a namespace replica"
    zoom="true"
/>

<CaptionedImage
    src="/img/cloud/high-availability/migrate/2-choose-region.png"
    title="Choose the region for the replica"
    zoom="true"
/>

2. Wait for the replica to become active. The Cloud UI will display a time estimate, and namespace admins will receive an email when the replica is active.
3. If your workers are using API key authentication: ensure your workers (and all other client code) are updated to [use the regional endpoint of the new replica](/cloud/namespaces#access-namespaces).
4. Trigger a failover to the new region.

<CaptionedImage
    src="/img/cloud/high-availability/migrate/3-failover.png"
    title="Initiate failover to the new region"
    zoom="true"
/>

5. Remove the Namespace replica in the region you are migrating from.

:::note
If using [API keys](/cloud/api-keys) for worker authentication, you must open a [support ticket](/cloud/support#support-ticket) to remove the replica.

:::

<CaptionedImage
    src="/img/cloud/high-availability/migrate/4-remove-replica.png"
    title="Remove the replica for the original region"
    zoom="true"
/>

:::note
All replica changes are subject to a [cooldown period](/cloud/high-availability/enable#changing) before further replica changes can be made.

:::

---

## Nexus

Temporal Cloud builds on the [core Nexus experience](/nexus) with:

- **Global [Nexus Registry](/nexus/registry)** - Scoped to your entire Account across all Namespaces. Workers in any Namespace can host Nexus Services for others to use.
- **Built-in [access controls](/nexus/registry#configure-runtime-access-controls)** - Restrict which caller Namespaces can use a Nexus Endpoint at runtime.
- **[Audit logging](/cloud/audit-logs)** - Stream Nexus Registry actions (create, update, delete Endpoints) to your audit log integration.
- **Multi-region connectivity** - Nexus requests route across Namespaces within and across AWS and GCP using a global mTLS-secured Envoy mesh. Compatible with Namespaces that have [High Availability](/cloud/high-availability) as Endpoint targets.
- **[Terraform support](/cloud/terraform-provider#manage-temporal-cloud-nexus-endpoints-with-terraform)** - Manage Nexus Endpoints with the Temporal Cloud Terraform provider.

<CaptionedImage
    src="/img/cloud/nexus/nexus-overview-short.png"
    title="Nexus Overview"
/>

## Learn more

- [Evaluate Nexus](/evaluate/nexus) | [Keynote and demo](https://youtu.be/qqc2vsv1mrU?feature=shared&t=2082)
- [How Nexus works](/nexus) | [Deep dive talk](https://www.youtube.com/watch?v=izR9dQ_eIe4&t=934s)

---

## Latency and Availability - Temporal Nexus

Nexus latency and availability in Temporal Cloud:

- **SLOs and SLAs** - Nexus operations (for example, `RespondWorkflowTaskCompleted`, `PollNexusTaskQueue`, `RespondNexusTaskCompleted`, and `RespondNexusTaskFailed`) have the same [latency SLOs](/cloud/service-availability#latency) and [availability SLAs](/cloud/sla) as other Worker requests in both caller and handler Namespaces.
- **[Nexus metrics](/nexus/metrics)** - SDK and Cloud latency metrics for monitoring Nexus performance.
- **Cross-Namespace connectivity** - Traffic routes through a global mTLS-secured Envoy mesh. Same-region Namespaces have low latency; cross-region latency varies by provider. See [secure connectivity](/nexus/security#secure-connectivity).

---

## Limits - Temporal Nexus

Nexus limits are documented in [Temporal Cloud limits](/cloud/limits):

- [Nexus rate limits](/cloud/limits#nexus-rate-limits) - Nexus requests count toward the Namespace RPS limit.
- [Nexus Endpoint limits](/cloud/limits#nexus-endpoints-limits) - 100 Endpoints per Account (default).
- [Per-Workflow Nexus Operation limits](/cloud/limits#per-workflow-nexus-operation-limits) - 30 in-flight Operations per Workflow.
- [Nexus Operation request timeout](/cloud/limits#nexus-operation-request-timeout) - Less than 10 seconds for a handler to process a start or cancel request.
- [Nexus Operation duration limits](/cloud/limits#nexus-operation-duration-limits) - 60-day maximum ScheduleToClose duration.
- [Per-Workflow callback limits](/cloud/limits#per-workflow-callback-limits) - 2000 callbacks per Workflow. Governs how many Nexus callers can attach to a handler Workflow.

---

## Observability - Temporal Nexus

Nexus observability in Temporal Cloud:

- **[Nexus metrics](/nexus/metrics)** - [SDK metrics](/nexus/metrics#sdk-metrics) emitted by Workers and [Cloud metrics](/nexus/metrics#cloud-metrics) emitted by Temporal Cloud.
- **[Execution debugging](/nexus/execution-debugging)** - Bi-directional linking, pending Operations, pending callbacks, and tracing across Namespaces.
- **[Audit logging](/cloud/audit-logs)** - `CreateNexusEndpoint`, `UpdateNexusEndpoint`, and `DeleteNexusEndpoint` actions streamed to your audit log integration.

---

## Pricing for Temporal Nexus

Nexus pricing:

- **One Action to start or cancel a Nexus Operation** in the caller Namespace.
  Underlying primitives (Workflows, Activities, Signals) and their retries created by the handler result in normal Actions.
- **No Action for handling or retrying the Nexus Operation itself**.
  However, billable actions initiated by the handler (such as Activities) are charged if they fail and retry.

See [Pricing](/cloud/pricing) for details.

---

## Notifications

## Get notified about Temporal Cloud status {/* #cloud-status */}

In the event of an incident, Temporal updates the [Temporal Cloud status page](https://status.temporal.io/) with important updates.
Users can subscribe to updates in their preferred mode (e.g. email, Slack, SMS, etc.) by visiting this page.

## Get notified about administrative events {/* #admin-notifications */}

Temporal Cloud sends emails to notify users of important administrative events.

| Reason for email | Who receives email |
|------------------ | -------------------|
| Certificate Expiring in 15 days | Global Administrator, Namespace Administrator, Account Owner |
| Certificate Expiring in 10 days | Global Administrator, Namespace Administrator, Account Owner |
| Certificate Expiring in 5 days  | Global Administrator, Namespace Administrator, Account Owner |
| API Key Expiring in 30 days     | Global Administrator, Account Owner, individual user (if API Key has an owner) |
| API Key Expiring in 20 days     | Global Administrator, Account Owner, individual user (if API Key has an owner) |
| API Key Expiring in 10 days     | Global Administrator, Account Owner, individual user (if API Key has an owner) |
| Sign up credit expiring in 30 days | Account Owner, Finance Administrator |
| Sign up credit expiring in 14 days | Account Owner, Finance Administrator |
| Sign up credit expiring in  7 days | Account Owner, Finance Administrator |
| Sign up credit expiring in  1 days | Account Owner, Finance Administrator |
| Sign up credit is 50% consumed     | Account Owner, Finance Administrator |
| Sign up credit is 90% consumed     | Account Owner, Finance Administrator |
| Account plan type changed          | Global Administrator, Account Owner, Finance Administrator |
| Namespace Failover Completed/Failed | Global Administrator, Namespace Administrator, Account Owner |

To ensure that you receive email notifications, configure your junk-email filters to permit email from
`noreply@temporal.io`.

To provide feedback on notifications or request changes, [create a support ticket](/cloud/support#support-ticket).

---

## Cloud Ops API

<ReleaseNoteHeader
  type="publicPreview"
/>

The Temporal Cloud Operations API, or the Cloud Ops API, is an open source, public [HTTP API](https://saas-api.tmprl.cloud/docs/httpapi.html#description/introduction) and [gRPC API](https://github.com/temporalio/cloud-api/tree/main) for programmatically managing Temporal Cloud Control Plane resources, including [Namespaces](/cloud/namespaces), [Users](/cloud/users), [Service Accounts](/cloud/service-accounts), [API keys](/cloud/api-keys), and others. The Temporal Cloud [Terraform Provider](/cloud/terraform-provider), [tcld CLI](/cloud/tcld), and Web UI all use the Cloud Ops API.

## Develop applications with the Cloud Ops API

You can use the HTTP API or the gRPC API depending on how you need to integrate with your platform. The URL to access both the HTTP and gRPC Cloud Ops API is `saas-api.tmprl.cloud`.

### Prerequisites

These prerequisites are required for using either HTTP or gRPC.

- [Temporal Cloud user account](/cloud/get-started)
- [API Key](/cloud/tcld/apikey#create) for authentication

### Use cases

Some common reasons you might use the API are to:

- Provision Namespaces per environment or tenant via pipelines.
- Bootstrap new projects by creating users, assigning roles, and creating Namespaces via custom scripts.
- Rotate service account keys on a schedule with a job.
- Audit and report access across orgs with scheduled HTTP requests.

### Using HTTP

[The HTTP API](https://saas-api.tmprl.cloud/docs/httpapi.html#description/introduction) supports the same operations as the [gRPC API](#using-grpc), but it's usable via standard HTTP methods and authentication. This may be a more convenient option if you are writing automation scripts for CI/CD or you can't use gRPC due to network policies, proxies, tooling gaps, or language/runtime constraints. Since it's standard HTTP, it's language agnostic giving you the ability to run cloud operations consistently.

:::note
This *does not* allow interaction with individual Workflows or Activities via HTTP.
:::

### Using gRPC

*For Go developers:*
- Use the [Go SDK](https://github.com/temporalio/cloud-sdk-go) for the simplest setup experience

*For other programming languages:*
- Basic familiarity with gRPC and Protocol Buffers (protobuf)
- [Protocol Buffers](https://github.com/protocolbuffers/protobuf/releases)
- [gRPC](https://grpc.io/docs/languages/) in your preferred programming language

You can use the provided proto files to generate client libraries in your desired programming language, and then use that client to access the gRPC API. You can also find the [full gRPC docs on Buf](https://buf.build/temporalio/cloud-api/docs/main:temporal.api.cloud.cloudservice.v1#temporal.api.cloud.cloudservice.v1.CloudService).
