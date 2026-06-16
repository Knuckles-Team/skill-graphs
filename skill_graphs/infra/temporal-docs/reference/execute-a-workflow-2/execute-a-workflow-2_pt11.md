| ----------------------- | ----------- | ------------------ |
| Export Workflow History | N/A         | N/A                |

## Fairness {/* #fairness */}

For each hour a Namespace has the [Fairness](/develop/task-queue-priority-fairness#task-queue-fairness) feature enabled,
an additional `0.1` Action is charged per Action in the Namespace.

- Excluded from APS calculations.

| Usage Name      | Metric Name | History Event Type |
| --------------- | ----------- | ------------------ |
| Enable Fairness | N/A         | N/A                |

## Capacity {/* #capacity */}

- For Namespace Capacity Temporal Resource Units (TRUs), Actions are generated up to the included hourly allocation for
  TRUs in any hour where TRUs are set and actual usage falls beneath the included hourly Action allocation.
- Excluded from APS calculations.

| Usage Name                  | Metric Name | History Event Type |
| --------------------------- | ----------- | ------------------ |
| Enable Provisioned Capacity | N/A         | N/A                |

Actions usage can be tracked in multiple areas depending on the needed granularity. Refer to the
[Billing and Usage](/cloud/billing-and-usage) documentation for more information.

---

## System limits - Temporal Cloud

Temporal Cloud enforces a variety of limits to keep the service reliable, including rate limits (how often something may occur in a unit of time), resource limits (how many of a given resource may exist at any one time), and configuration limits (minimum or maximum values for a setting)

Every limit applies at a specific scope (level of the application):

- At the Temporal Cloud [Account level](#account-level)
- At the [Namespace level](#namespace-level)
- At the [Nexus endpoint level](#nexus-endpoint-level)
- Within the [programming model](#programming-model-level) itself

## Account level

The following limits apply at the Temporal Cloud Account level (per account).

### Users

- Scope: Account
- Default limit: 300 users
- How to increase: [Contact support](/cloud/support#support-ticket)

### Namespaces

- Scope: Account
- Default limit: 10 namespaces
- How to increase:
  - Automatically increased as you start creating namespaces
  - [Contact support](/cloud/support#support-ticket) for large-scale needs

## Namespace level

The following limits apply at the Namespace level.

### Actions per second

- Scope: Namespace
- Default limit: 500 actions per second (APS)
- How to increase:
  - Automatically increases (and decreases) based on the last 7 days of APS usage. Will never go below the default limit.
  - See [Capacity Modes](/cloud/capacity-modes).
  - [Contact support](/cloud/support#support-ticket).
- What happens when you exceed the limit: See [Throttling behavior](#throttling-behavior) below.

See the [Actions page](/cloud/actions) for the list of actions.

### Requests per second

- Scope: Namespace
- Default limit: 2000 requests per second (RPS)
- How to increase:
  - Automatically increases (and decreases) based on the last 7 days of RPS usage. Will never go below the default limit.
  - See [Capacity Modes](/cloud/capacity-modes).
  - [Contact support](/cloud/support#support-ticket).

See the [glossary](/glossary#requests-per-second-rps) for more about RPS.

### Operations per second

- Scope: Namespace
- Default limit: 4000 operations per second (OPS)
- How to increase:
  - Automatically increases (and decreases) based on the last 7 days of OPS usage. Will never go below the default limit.
  - See [Capacity Modes](/cloud/capacity-modes).
  - [Contact support](/cloud/support#support-ticket).

See the [operations list](/references/operation-list) for the list of operations.

### Throttling behavior

When you exceed your APS, RPS, or OPS limits, Temporal Cloud throttles requests. Here's what happens:

1. **Priority-based throttling**: Low-priority operations are throttled first. Higher-priority operations like `StartWorkflowExecution`, `SignalWorkflowExecution`, and `UpdateWorkflowExecution` continue to go through when possible. Temporal Cloud uses similar [throttling priorities as the open source server](https://github.com/temporalio/temporal/blob/main/service/frontend/configs/quotas.go#L66).
2. **Throttling latency**: Rate limiting is not instantaneous, so usage may briefly exceed your limit before throttling takes effect.
3. **ResourceExhausted errors**: When throttled, the server returns a `ResourceExhausted` gRPC error. SDK clients automatically retry these based on the default gRPC retry policy.
4. **Potential failure**: If throttling persists beyond the SDK's retry limit, client calls fail. This means work _can_ be lost if you don't handle these failures.

**Best practices for handling throttling:**
- Log any failed `StartWorkflowExecution`, `SignalWorkflowExecution`, or `UpdateWorkflowExecution` calls on the client side, including the payload, so you can retry or backfill later.
- Set up [Cloud metrics](/cloud/metrics/openmetrics/metrics-reference#limit-metrics) to alert when throttling occurs and when you approach your limits.
- Consider [Provisioned Capacity](/cloud/capacity-modes#provisioned-capacity) if you have predictable spikes or need guaranteed throughput.

### Schedules rate limit

- Scope: Namespace
- Default limit: 10 schedule requests per second (RPS)
- How to increase: [Contact support](/cloud/support#support-ticket)

To avoid throttling, don't schedule all your Workflow Executions to start at the same time (daily, weekly, monthly, etc.).
Every Temporal SDK supports jittering, which adds small random delays to Schedule specifications, helping to reduce load at any specific moment.
Set the `jitter` value to the largest delay you will permit before your Workflow Execution must begin.
This approach uniformly distributes the scheduled Workflow Execution launches through that period and reduces your Schedule Workflow Execution RPS load.

### Visibility API Rate Limit

- Scope: Namespace
- Default limit: 30 Visibility API calls per second
- Not configurable

All read calls are subject to the Visibility API rate limit.

### Nexus Rate Limit {/* #nexus-rate-limits */}

Nexus requests (such as starting a Nexus Operation or sending a Nexus completion callback) are counted as part of the overall Namespace RPS limit.
If too many Nexus requests are sent at once, they may be throttled, along with other requests to the Namespace.
Throttling limits the rate at which Nexus requests are processed, ensuring the RPS limit isn't exceeded.

You can request this limit be manually raised by [opening a support ticket](https://docs.temporal.io/cloud/support#support-ticket).

:::note

For the target Namespace of a Nexus Endpoint, even though there are no Action results for handling a Nexus Operation itself, the Nexus requests on a target Namespace do count towards the overall RPS limit for the Namespace as a whole.

:::

### Certificates

Temporal Cloud limits each Namespace to a total of 32 KB or 16 certificates, whichever is reached first.

### Concurrent Task pollers

Temporal Cloud limits each Namespace to 20,000 Activity pollers and 20,000 Workflow Task pollers concurrently.

Each SDK offers a way to configure Workers for per-Worker maximum Activity and Workflow Task pollers.
Those values do not affect the global Namespace limit.

### Default Retention Period

The [Retention Period](/temporal-service/temporal-server#retention-period) is set per Namespace.

Temporal Cloud sets the default Retention Period to 30 days.
This is configurable in the Temporal Web UI.

[Navigate to your list of Namespaces](https://cloud.temporal.io/namespaces), choose the Namespace you want to update, and select edit:

<CaptionedImage
    src="/img/cloud/cloud-guide/edit-namespace-option.png"
    title="Choose your Namespace and select Edit"
/>

<CaptionedImage
    src="/img/cloud/cloud-guide/edit-retention-period.png"
    title="Update the Retention Period"
/>

You can set the Retention Period between 1 and 90 days.

### Batch jobs

A Namespace can have just one [Batch job](/cli/command-reference/batch) running at a time.

Each batch job operates on a maximum of 50 Workflow Executions per second.

### Number of Custom Search Attributes

There is a limit to the number of custom Search Attributes per attribute type per Namespace:

| Search Attribute type | Limit |
| --------------------- | ----- |
| Bool                  | 20    |
| Datetime              | 20    |
| Double                | 20    |
| Int                   | 20    |
| Keyword               | 40    |
| KeywordList           | 5     |
| Text                  | 5     |

### Custom Search Attribute names

When creating custom Search Attributes in Temporal Cloud, the attribute names must adhere to the following constraints:

- Maximum characters: 64
- Allowed characters: `[a-zA-Z0-9.,:-_\/@ ]`.

For more information on custom Search Attributes see [Custom Search Attributes limits](/search-attribute#custom-search-attribute).

## Nexus Endpoint level

### Nexus Endpoints limits

By default, each account is provisioned with 100 Nexus Endpoints.
You can request further increases beyond the initial 100 Endpoint limit by [opening a support ticket](/cloud/support#support-ticket).

## Programming model level

The following limits apply at the programming model level.
See also: [Self-hosted Temporal Service defaults](/self-hosted-guide/defaults).

### Identifier length limit

Identifiers, such as Workflow Id, Workflow Type, and Task Queue names, are limited to a maximum length of 1,000 bytes.
Note that Unicode characters may use multiple bytes.

### Per message gRPC limit

Each gRPC message received has a limit of 4 MB.
This limit applies to all gRPC endpoints across the Temporal Platform.

### Event History transaction size limit

An Event History transaction encompasses a set of operations such as initiating a new Workflow, scheduling an Activity, processing a Signal, or starting a Child Workflow.
These operations create Events that are then logged in the Event History.
The transaction size limit restricts the total size of Events that can be accommodated within a single transaction.

The size limit for any given [Event History](/workflow-execution/event#event-history) transaction is 4 MB.
This limit is non-configurable for Temporal Cloud.

### Transaction Payload size limit

Blob size limit for Payloads, including Workflow context and each Workflow and Activity argument and return value:
  - The max payload for a single request is 2 MB.
  - The max size limit for any given [Event History](/workflow-execution/event#event-history) transaction is 4 MB.

This limit is non-configurable for Temporal Cloud.

The [BlobSizeLimitError guide](/troubleshooting/blob-size-limit-error) provides solutions for handling large payloads.

### Per Workflow Execution concurrency limits

If a Workflow Execution has 2,000 incomplete Activities, Signals, Child Workflows, or external Workflow Cancellation requests, additional [Commands](/workflow-execution#command) of that type will fail to be applied to that Workflow Execution:

- `ScheduleActivityTask`
- `SignalExternalWorkflowExecution`
- `StartChildWorkflowExecution`
- `RequestCancelExternalWorkflowExecution`

For optimal performance, limit concurrent operations to 500 or fewer.
This reduces Workflow's Event History size and decreases the loading time in the Web UI.

### Per Workflow Execution Signal limit

A single Workflow Execution may receive up to 10,000 Signals.
After that limit is reached, no more Signals will be processed for that Workflow Execution.

### Per Workflow Execution Update limits

A single Workflow Execution can have a maximum of 10 in-flight Updates and 2000 total Updates in History.

### Workflow Execution Event History limits

As a precautionary measure, a Workflow Execution's Event History is limited to 51,200 Events or 50 MB.
It warns you after 10,240 Events or 10 MB.
This limit applies to all Temporal Workflow Executions, whether on Temporal Cloud or other deployments.

This limit is non-configurable for Temporal Cloud.

Read more about [Temporal Workflow Execution limits](/workflow-execution/limits) on the [Temporal Workflow](/workflows) documentation page.

### Per Workflow Callback limits {/* #per-workflow-callback-limits */}

A single Workflow Execution can have a maximum of 2000 total Callbacks.

These limits may be exceeded when [multiple Nexus callers attach to the same handler Workflow](/nexus/operations#attaching-multiple-nexus-callers).

See the Nexus Encyclopedia entry for [additional details](/workflow-execution/limits#workflow-execution-callback-limits).

### Per Workflow Nexus Operation limits {/* #per-workflow-nexus-operation-limits */}

A single Workflow Execution can have a maximum of 30 in-flight Nexus Operations.

See the Nexus Encyclopedia entry for [additional details](/workflow-execution/limits#workflow-execution-nexus-operation-limits).

### Nexus Operation request timeout {/* #nexus-operation-request-timeout */}

Less than 10 seconds is the maximum duration for a Nexus handler to process a single Nexus start or cancel request.

The timeout is measured from the calling History Service and the request must go through matching, so the available time for a handler to respond is often much less than 10 seconds.
Handlers should observe the context deadline and ensure they don't exceed it.
This includes fully processing a synchronous Nexus operation and starting an asynchronous Nexus operation, for example one that starts a Workflow.

If a Nexus handler doesn’t process a start or cancel request within 10 seconds, it will receive a context deadline exceeded error, and the caller will retry, with an exponential backoff, for the ScheduleToClose duration for the overall Nexus Operation.
This has a default and maximum as defined below in [Nexus Operation duration limits](/cloud/limits#nexus-operation-duration-limits).

### Nexus Operation duration limits {/* #nexus-operation-duration-limits */}

Each Nexus Operation has a maximum ScheduleToClose duration of 60 days.
This is most applicable to asynchronous Nexus Operations completed with an asynchronous callback using a separate Nexus request from the handler back to the caller Namespace.

For enhanced security, you may sign completion callbacks with a single-use token in the future, and the 60 day maximum allows you to rotate the asymmetric encryption keys used for completion callback request signing.

While the caller of a Nexus Operation can configure the ScheduleToClose duration to be shorter than 60 days, the maximum duration can not extend beyond 60 days and capped by the server to 60 days.

### Timer duration limit

Timers have a maximum duration of 100 years in Temporal Cloud.

## Worker Versioning level

### Max Worker deployments limits {/* #max-worker-deployments-limits */}

The maximum number of Worker deployments that the server allows to be registered in a single Namespace. Defaults to 100.

### Max versions in deployment limits {/* #max-versions-in-deployment-limits */}

The maximum number of versions that the server allows to be registered in a single Worker deployments at a given time. Note that unused versions will be deleted by the system automatically when this limit is reached. Defaults to 100.

### Max Task Queues In Deployment Version limits {/* #max-task-queues-in-deployment-version-limits */}

The maximum number of Task Queues that the server allows to be registered in a single Worker Deployment Version. Defaults to 100.

---

## Overview - Temporal Cloud

Temporal Cloud is a fully managed durable execution platform.
It handles the complexity of running Temporal at scale—persistence, replication, upgrades, and availability—so you can focus on building applications.

Your code runs in your environment.
Temporal Cloud never sees your application logic or sensitive data.
The platform stores encrypted Workflow state and orchestrates execution, while your Workers execute business logic wherever you deploy them.

## How Temporal Cloud works

Temporal Cloud operates as the Control Plane for your distributed applications:

1. **Your environment**: You run Workers that execute your Workflow and Activity code. These can be deployed anywhere—Kubernetes, VMs, serverless, on-premises.
2. **Temporal Cloud**: Manages Workflow state, Event History, task queuing, and scheduling. All data is encrypted in transit and at rest.
3. **Temporal SDKs**: Your applications use the SDK to communicate with Temporal Cloud over secure gRPC connections.

This separation means Temporal Cloud scales independently of your application.
You control compute resources for your Workers; Temporal handles the orchestration layer.

## Architecture

### Cell-based infrastructure

Temporal Cloud uses a cell-based architecture to achieve isolation and scalability.
Each cell is a self-contained deployment unit with its own:

- Dedicated cloud account and VPC
- Kubernetes cluster running Temporal services
- Primary database with synchronous replication across three availability zones
- Elasticsearch for Workflow visibility and search
- Load balancers and ingress management
- Observability and certificate infrastructure

Cells act as failure domains.
If infrastructure within a cell experiences issues, only Namespaces in that cell are affected.
This design limits blast radius and enables independent scaling.

### Data plane and control plane

**Data plane**: Where your Workflows execute. Each cell processes Workflow operations, persists state, and manages task queues. The data plane is optimized for low latency and high throughput.

**Control plane**: Manages provisioning, configuration, and lifecycle operations. When you create a Namespace, the Control Plane:
1. Selects an appropriate cell in your chosen region
2. Provisions database resources and roles
3. Generates and deploys mTLS certificates
4. Configures ingress routes and validates connectivity

The control plane uses Temporal itself (durable execution) to orchestrate these operations reliably.

### Multi-cloud availability

Temporal Cloud runs on both AWS and GCP:

- <CloudRegionCount provider="aws" /> AWS regions spanning North America, Europe, Asia Pacific, and South America
- <CloudRegionCount provider="gcp" /> GCP regions in North America, Europe, and Asia Pacific

You can create Namespaces in any supported region.
For disaster recovery, you can replicate across regions within a cloud provider or across cloud providers entirely.

See [Service regions](/cloud/regions) for the complete list of available regions.

## Built-in reliability

Every Temporal Cloud Namespace includes baseline high availability:

- **Three-zone replication**: Workflow state synchronously replicates across three availability zones before acknowledging writes
- **Automatic failover**: If one zone becomes unavailable, operations continue on the remaining zones
- **99.9% SLA**: Contractual uptime guarantee for standard Namespaces

### High Availability features

For workloads requiring stronger guarantees, Temporal Cloud offers three replication options:

| Deployment | Description | Use case |
|------------|-------------|----------|
| **Same-region** | Replicate across isolated cells within one region | Single-region applications needing cell-level isolation |
| **Multi-region** | Replicate across regions within one cloud provider | Geographic redundancy and compliance requirements |
| **Multi-cloud** | Replicate across cloud providers (AWS ↔ GCP) | Maximum resilience against provider-level outages |

High Availability Namespaces include:
- **99.99% SLA**: Four-nines contractual uptime guarantee
- **Sub-1-minute RPO**: Recovery Point Objective for data loss
- **20-minute RTO**: Recovery Time Objective for failover completion
- **Automatic or manual failover**: Choose your preferred failover strategy

See [High Availability](/cloud/high-availability) for configuration details.

## Security model

Temporal Cloud implements defense-in-depth security:

### Your code stays with you

Temporal Cloud never executes your application code.
Workers run in your environment, connecting to Temporal Cloud over encrypted channels.
You control access to your compute resources and secrets.

### Client-side encryption

The [Data Converter](/dataconversion) lets you encrypt payloads before they leave your Workers.
Temporal Cloud stores ciphertext—if the service were compromised, your data remains encrypted.
Deploy a [Codec Server](/production-deployment/data-encryption) to decrypt data in the Web UI without sharing keys.

### Network isolation

- **mTLS authentication**: Per-Namespace certificate-based authentication for gRPC endpoints
- **API key authentication**: Alternative to certificates for simpler key management
- **Private connectivity**: AWS PrivateLink and GCP Private Service Connect for traffic that never traverses the public internet

### Compliance

Temporal Technologies maintains SOC 2 Type 2 certification and complies with GDPR and HIPAA regulations.
Audit logs capture all API operations and can be exported to your security monitoring systems.

See [Security model](/cloud/security) for complete details.

## Consumption-based pricing

Temporal Cloud charges based on what you use:

### Actions

The primary billing unit.
Actions are billable operations like starting Workflows, sending Signals, recording Heartbeats, and completing Activities.
Pricing starts at $50 per million Actions with volume discounts as you scale.

### Storage

- **Active Storage**: Event History for running Workflows
- **Retained Storage**: Event History for completed Workflows (configurable retention period up to 90 days)

### Plans

Four tiers—Essentials, Business, Enterprise, and Mission Critical—with increasing support levels, included Actions/Storage, and features like SAML and SCIM.
The Essentials plan starts at $100/month.

Self-serve signup and plan management available at [cloud.temporal.io](https://cloud.temporal.io).

See [Pricing](/cloud/pricing) for detailed rates and examples.

## Portability

Temporal Cloud runs the same Temporal Server as the open-source distribution.
This means:

### Zero code changes

Applications built for self-hosted Temporal work on Temporal Cloud without modification.
Update your connection configuration to point at your Cloud Namespace—that's it.

### Zero-downtime migration

[Automated migration](/cloud/migrate/automated) uses Workflow replication to move running Workflows from self-hosted to Cloud (or between Cloud regions) without interruption.
No Workflow restarts, no data loss, no downtime.

[Manual migration](/cloud/migrate/manual) works by updating Clients and Workers to use new Namespace endpoints while existing Workflows complete naturally.

### Bidirectional

Move workloads from self-hosted to Cloud, Cloud to self-hosted, or between Cloud regions and providers.
The same migration tooling works in any direction.

## Self-serve operations

Temporal Cloud is designed for self-service:

- **Web UI**: Create Namespaces, manage users, configure settings at [cloud.temporal.io](https://cloud.temporal.io)
- **CLI (`tcld`)**: Automate operations from the command line
- **Terraform provider**: Infrastructure-as-code for Namespaces, users, and configuration
- **Cloud Ops API**: Programmatic access for custom tooling and automation

No support tickets required for standard operations.

## Getting started

1. [Sign up for Temporal Cloud](https://temporal.io/get-cloud)
2. [Create your first Namespace](/cloud/namespaces)
3. [Connect your Workers](/cloud/get-started#set-up-your-clients-and-workers)
4. [Run your first Workflow](/cloud/get-started#run-your-first-workflow)

For existing Temporal users, see [Migration](/cloud/migrate) to move self-hosted workloads to Cloud.

---

## Temporal Cloud pricing

Temporal Cloud is a consumption-based service.
You pay only for what you use.
Our pricing reflects your use of [_Actions_](#action), [_Storage_](#storage), and [_Support_](/cloud/support#support).
It is flexible, transparent, and predictable, so you know your costs.

This page describes the elements of Temporal Cloud pricing.
It gives you the information you need to understand and estimate costs for your implementation.
For more exact estimates, please reach out to [our team](https://pages.temporal.io/ask-an-expert).

Billing and cost information is available directly in the Temporal Cloud UI.
For more information, visit the [Billing](/cloud/billing) page.

## Temporal Cloud pricing model {/* #pricing-model */}

This section explains the basis of the Temporal Cloud pricing model and how it works.
Your total invoice each calendar month is the combination of Temporal Cloud consumption ([Actions](#action) and [Storage](#storage)), and a [Temporal Cloud Plan](#base_plans) that includes [Support](/cloud/support#support).

### Temporal Cloud Plans {/* #base_plans */}

**How plans work**

Each Temporal Cloud account includes a plan with Support, Actions, Active Storage, Retained Storage and platform features.
Base allocations help you get started with the Temporal platform, so you can better estimate costs.

- Temporal Cloud Plans are charged monthly.
- Action and Storage allocations are reset each calendar month.

Temporal offers four plans: Essentials, Business, Enterprise, Mission Critical.
Prices are outlined in the following table:

|                   | Essentials                                                                     | Business                                                                                                                          | Enterprise                                                                                                                                                 | Mission Critical                                                                                                                                           |
