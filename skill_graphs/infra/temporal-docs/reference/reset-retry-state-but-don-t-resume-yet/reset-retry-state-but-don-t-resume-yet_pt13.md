
## Automatic retries {/* #automatic-retries */}

Once the caller Workflow schedules an Operation with the caller's Temporal Service, the caller's Nexus Machinery keeps trying to start the Operation.
If a [retryable Nexus error](/references/failures#nexus-errors) is returned the Nexus Machinery will retry until the Nexus Operation's [Schedule-to-Start timeout](#schedule-to-start-timeout) or [Schedule-to-close timeout](#schedule-to-close-timeout) is exceeded.

For example, if a Nexus handler returns a [retryable error](/references/failures#nexus-errors), or an [upstream timeout](https://github.com/nexus-rpc/api/blob/main/SPEC.md#predefined-handler-errors) is encountered by the caller, the Nexus request will be retried up to the [default Retry Policy's](https://github.com/temporalio/temporal/blob/de7c8879e103be666a7b067cc1b247f0ac63c25c/components/nexusoperations/config.go#L111) max attempts and expiration interval.

:::note
This differs from Activity and Workflow error handling.
See [errors in Activities](/references/failures#errors-in-activities) and [non-retryable errors](/references/failures#non-retryable).
:::

To control retry behavior, return a [non-retryable Nexus error](/references/failures#non-retryable-nexus-errors).
See [errors in Nexus handlers](/nexus/error-handling#errors-in-nexus-handlers).

## Timeouts {/* #timeouts */}

Nexus Operations support three types of timeouts that control how long the caller is willing to wait at different stages of the Operation lifecycle.
These timeouts are set by the caller when scheduling the Operation.

### Schedule-to-Close timeout {/* #schedule-to-close-timeout */}

The Schedule-to-Close timeout limits the total duration from when the Operation is scheduled to when it completes.
This is the overall timeout for the entire Operation.
The Nexus Machinery [automatically retries](#automatic-retries) failed requests internally until this timeout is exceeded, at which point the Operation fails with a [NexusOperationTimedOut](/references/events#nexusoperationtimedout) event.

This timeout covers the full [Nexus Operation lifecycle](https://docs.temporal.io/nexus/operations#operation-lifecycle). Asynchronous Operations are scheduled, started, and completed. Synchronous Operations don't have an intermediate started state because they complete as part of the start request.

In Temporal Cloud, the [maximum Schedule-to-Close timeout is 60 days](https://docs.temporal.io/cloud/limits#nexus-operation-duration-limits).

### Schedule-to-Start timeout {/* #schedule-to-start-timeout */}

The Schedule-to-Start timeout limits how long the caller is willing to wait for the Operation to be started (or completed, if synchronous) by the handler.
If the Operation is not started within this timeout, it fails with `TIMEOUT_TYPE_SCHEDULE_TO_START`.

If not set or set to zero, no Schedule-to-Start timeout is enforced.

:::note

The Schedule-to-Start timeout requires Temporal Server version 1.31.0 or later.

:::

### Start-to-Close timeout {/* #start-to-close-timeout */}

The Start-to-Close timeout limits how long the caller is willing to wait for an asynchronous Operation to complete after it has been started.
If the Operation does not complete within this timeout after starting, it fails with `TIMEOUT_TYPE_START_TO_CLOSE`.

This timeout only applies to asynchronous Operations.
Synchronous Operations ignore this timeout because they complete as part of the start request.

If not set or set to zero, no Start-to-Close timeout is enforced.

:::note

The Start-to-Close timeout requires Temporal Server version 1.31.0 or later.

:::

## Circuit breaking {/* #circuit-breaking */}

Nexus implements circuit breaking per caller-Namespace/Endpoint pair ("destination pair").
Each destination pair trips and resets independently.
By default, the circuit breaker activates after 5 consecutive [retryable errors](/references/failures#nexus-errors).

After tripping, the circuit breaker enters the _open_ state and stops sending requests.
After 60 seconds, it transitions to _half-open_, allowing a single probe request.
If the probe succeeds, the circuit breaker returns to _closed_ (normal operation).
If it fails, the circuit breaker returns to _open_ for another 60 seconds.

:::note
Note that worker availability affects the circuit breaker as well.
If no workers are polling the handler task queue — due to a deployment issue, crash, or scale-down — Nexus requests will time out.
Consecutive timeouts count as retryable errors and will trip the circuit breaker just as application-level errors do.
Ensure handler workers maintain sufficient availability to avoid unintended circuit breaker trips.

:::

<CaptionedImage
    src="/img/cloud/nexus/circuit-breaker.png"
    title="Flow chart showing the states of the Temporal Nexus Circuit Breaker"
/>

Circuit breaker state surfaces in [Pending Nexus Operations](/nexus/execution-debugging#pending-operations) and [Pending Callbacks](/nexus/execution-debugging#pending-callbacks).
Check it in the UI, CLI, or `DescribeWorkflowExecution` API.

When open, pending Operations show a `Blocked` state with a `BlockedReason`:

<CaptionedImage
    src="/img/cloud/nexus/circuit-breaking.png"
    title="Circuit Breaking"
/>

Different Operations within the same destination pair contribute to the trip count.
A given Operation may have fewer than 5 attempts when the circuit breaker opens.

From the CLI:

```sh
temporal workflow describe -w my-workflow-id
```

```sh
Pending Nexus Operations: 1

  Endpoint                 my-nexus-endpoint
  Service                  nexus-playground
  Operation                sync-op-ok
  State                    Blocked
  Attempt                  1
  LastAttemptFailure       {"message":"handler error (UPSTREAM_TIMEOUT): upstream timeout",...}
  BlockedReason            The circuit breaker is open.
```

Cancellation requests surface the same pattern with `CancelationState: Blocked` and `CancelationBlockedReason`.

```sh
Execution Info:
  WorkflowId            my-workflow-id
  ...

Pending Activities: 0
Pending Child Workflows: 0
Pending Nexus Operations: 1

  Endpoint                            my-nexus-endpoint
  Service                             nexus-playground
  Operation                           async-op-workflow-wait-for-cancel
  OperationToken                      eyJ2IjowLCJ0IjoxLCJucyI6Im5zIiwid2lkIjoidyJ
  State                               Started
  Attempt                             1
  ScheduleToCloseTimeout              1d 0h 0m 0s
  LastAttemptCompleteTime             51 seconds ago
  CancelationState                    Blocked
  CancelationAttempt                  5
  CancelationRequestedTime            37 seconds ago
  CancelationLastAttemptCompleteTime  27 seconds ago
  CancelationLastAttemptFailure       {"message":"handler error (UPSTREAM_TIMEOUT): upstream timeout","cause":{"message":"upstream timeout","applicationFailureInfo":{"type":"NexusFailure"}},"applicationFailureInfo":{"type":"NexusHandlerError"}}
  CancelationBlockedReason            The circuit breaker is open.
```

## Execution semantics {/* #execution-semantics */}

### At-least-once execution semantics and idempotency

The Nexus Machinery provides reliable execution with at-least-once execution semantics for a Nexus Operation, until the caller's [Schedule-to-Close timeout](#schedule-to-close-timeout) is exceeded, at which time the overall Nexus Operation times out.
The Machinery retries on handler timeouts or retryable errors, so a handler may be invoked multiple times for the same Operation.

Nexus Operation handlers should be idempotent, similar to Activities.
Not strictly required in all cases, but highly recommended.

### Exactly-once execution semantics

To upgrade to exactly-once, back your Operation with a Workflow that uses a WorkflowIDReusePolicy of RejectDuplicates.
This allows only one Workflow Execution per Workflow ID within a Namespace for the Retention Period.

## Cancelation

Cancelling a caller Workflow automatically propagates to all pending Nexus Operations and their underlying handler Workflows.
A canceled handler Workflow reports a [Canceled Failure](/references/failures#cancelled-failure) to the caller.

## Termination

Terminating a caller Workflow abandons all pending Nexus Operations. Unlike cancellation, no cancel request is sent to the
handler Namespace, so handler Workflows continue running indefinitely, consuming resources until they time out or are manually
stopped. Because the handler runs in a separate Namespace, it has no signal that the caller is gone, making orphaned Operations
difficult to detect and correlate. If the Nexus Operation was part of a multi-step process, termination also leaves no opportunity
to run compensation logic, potentially leaving the system in a partially completed state.
Prefer [cancellation](#cancelation) when possible.

## Versioning {/* #versioning */}

Task Routing is the simplest way to version Nexus service code.
For backward-incompatible changes, use a different Service name and Task Queue (for example, `prod.payments.v2`).
Callers migrate to the new version on their own deployment schedule.

## Attaching multiple Nexus callers to a handler Workflow {/* #attaching-multiple-nexus-callers */}

Operations started with [New-Workflow-Run-Operation](/nexus/operations#sdk-support) automatically attach a completion Callback to the handler Workflow.
Additional callers can attach to the same handler Workflow using a [Conflict-Policy of Use-Existing](/workflow-execution/workflowid-runid#workflow-id-conflict-policy).

Each handler Workflow has a [Callback limit](/workflow-execution/limits#workflow-execution-callback-limits) (configurable for self-hosted, see [Cloud limits](/cloud/limits#per-workflow-callback-limits) for Temporal Cloud).
Callers that exceed the limit receive an error.

When a handler Workflow uses [Continue-As-New](/workflow-execution/continue-as-new), existing completion Callbacks are copied to the new Execution.
The previous Execution's Callbacks remain in `Standby` state indefinitely.

---

## Nexus Patterns

There are two common patterns for building and deploying [Nexus Services](/nexus/services):
- **[Collocated pattern](#collocated-pattern)**: Runs on the same Workers as your existing Workflows and Activities. Use by default.
- **[Router pattern](#router-queue-pattern)**: Separates Nexus routing from Workflow execution. A dedicated Nexus Worker on a “router” Task Queue routes Operations to Workflows on other Task Queues.
Use when you need independent scaling, different IAM permissions per Worker fleet, or want to add Nexus to without modifying existing Workers.

## Collocated pattern (default) {/* #collocated-pattern */}

The **collocated pattern** runs Nexus Operation handlers in the same Worker and on the same Task Queue as the underlying Workflows.
This is the default and simplest deployment.

The Nexus Endpoint targets the same Task Queue used by the underlying Workflows.
A single Worker registers both Nexus Services and Workflow types, so everything runs together.

### Why start here

- **Simplest setup:** One Worker, one Task Queue, one deployment. No extra infrastructure.
- **Eager Workflow Start:** When the handler starts a Workflow in the same Worker, you can use [Eager Workflow Start](/develop/worker-performance#eager-workflow-start) to execute the first Workflow Task locally without an extra call to the Temporal Server - while still recording durable state. If the process crashes, the Workflow resumes on another Worker.
- **Clean facade:** Operations act as a stable contract. You can change the underlying implementation (Signal today, Workflow tomorrow) without impacting callers.

### When to use this pattern

- Getting started with Nexus.
- The same team owns both the Nexus Service and underlying Workflows.
- You don't need to scale Nexus routing separately from Workflow execution.
- You are setting up a simple test environment

Use this pattern by default unless you have a good reason to use the Router-queue pattern below

## Router-queue pattern

The **router-queue pattern** separates Nexus routing from Workflow execution. A dedicated Nexus Worker on a "router" Task Queue routes Operations to Workflows on other Task Queues in the same Namespace.

### When to use this pattern

- **Separate scaling:** Scale Nexus routing independently from Workflow execution.
- **Dedicated routing layer:** A single Nexus Worker routes requests to multiple Workflow types on different Task Queues.
- **Different IAM permissions:** Worker fleets behind different Task Queues may have different IAM permissions to different underlying resources.
- **Avoid modifying existing Workers:** Add a router Worker to a Namespace without changing any existing Workers or Workflows.

### How it works

1. Register a Nexus Worker that polls a dedicated "router" Task Queue.
2. Configure the Nexus Endpoint's target Task Queue to point to this router Task Queue.
3. In each Nexus Operation handler, specify a different target Task Queue in the Workflow start options.
4. Existing Workers continue to poll their own Task Queues and execute the Workflows started by the router.

### Production usage

Used in production by organizations running self-service platforms where a central gateway routes requests to domain-specific Namespaces and Task Queues.
The router Worker is lightweight - it only handles routing logic.

---

## Nexus Registry

The [Nexus Registry](/glossary#nexus-registry) manages [Nexus Endpoints](/nexus/endpoints).
Developers can advertise available Endpoints and Services, so others can find and use them in their caller Workflows.
Adding an Endpoint to the Registry deploys it for immediate runtime use.
Endpoint names must be unique within the Registry.
In Temporal Cloud, the Registry is global across your entire Account, spanning all Namespaces.
In self-hosted deployments, it is scoped to a Cluster.

## View and manage Nexus Endpoints

Manage Endpoints using the Temporal UI, CLI, Terraform provider, or [Cloud Ops API](/ops).

:::tip RESOURCES

- [Terraform support](/cloud/terraform-provider#manage-temporal-cloud-nexus-endpoints-with-terraform) for Temporal Cloud.
- [tcld nexus](/cloud/tcld/nexus) for Temporal Cloud.
- [temporal operator nexus](/cli/command-reference/operator#nexus) for self-hosted deployments.
  :::

### Search for a Nexus Endpoint

Search by Endpoint name or target Namespace.

<CaptionedImage
    src="/img/cloud/nexus/nexus-endpoints-ss.png"
    title="Nexus Endpoints"
/>

The details page shows the target Namespace, Task Queue, and description rendered as markdown.

<CaptionedImage
    src="/img/cloud/nexus/nexus-billing-ss.png"
    title="Nexus Billing"
/>

### Create a Nexus Endpoint

Creating an Endpoint includes setting an Access Policy - the allowlist of caller Namespaces permitted to use the Endpoint.
No callers are allowed by default, even if in the same Namespace as the Endpoint target.

<CaptionedImage
    src="/img/cloud/nexus/create-nexus-endpoint-ss.png"
    title="Create Nexus Endpoint"
/>

### Edit a Nexus Endpoint

Everything except the Endpoint name can be edited.
New Operations route to the updated target immediately.

:::caution Changing the target Namespace

- **In-flight async Operations** - Completion callbacks point to the original handler Namespace and are unaffected, but Cancel requests route to the new target.
- **Workflow ID uniqueness** - IDs are scoped per Namespace. Signal-With-Start creates a new Workflow in the new target even if the same ID is active in the old target, resulting in potential duplicates.
- **Recommendation:** Drain existing Nexus Operations and underlying handler Workflows before changing the target Namespace.

:::

<CaptionedImage
    src="/img/cloud/nexus/target-namespace-ss.png"
    title="Edit Nexus Endpoint"
/>

### Configure runtime access controls

The Access Policy controls which caller Namespaces can use an Endpoint at runtime.
No callers are allowed by default.

See [Runtime Access Controls](/nexus/security#runtime-access-controls) for details.

<CaptionedImage
    src="/img/cloud/nexus/create-nexus-endpoint-ss.png"
    title="Configure runtime access controls"
/>

## Roles and permissions

:::info

The Nexus Registry uses default roles in Temporal Cloud. For self-hosted deployments, you can implement [custom Authorizers](/self-hosted-guide/security#authorizer-plugin to restrict access).

:::

In Temporal Cloud, Nexus Registry respects RBAC permissions, and restricts functionality based on user role:

| Action                     | Required permissions                                      |
|---------------------------|-----------------------------------------------------------|
| View or search Endpoints  | Read-only role (or higher) at the Account level           |
| Manage Endpoints          | Developer role (or higher) and Namespace Admin on target Namespace |

See [Nexus security in Temporal Cloud](/cloud/nexus/security).

## Automate Nexus Endpoint provisioning and lifecycle management

There are two ways to automate endpoint provisioning and lifecycle management: Terraform and the Operator API.

:::tip RESOURCES

- [Terraform support](/cloud/terraform-provider#manage-temporal-cloud-nexus-endpoints-with-terraform) for Temporal Cloud.
- [Cloud Ops API](/ops) for Temporal Cloud.
- [Operator API](https://github.com/temporalio/api/blob/main/temporal/api/operatorservice/v1/service.proto) for self-hosted deployments.

:::

---

## Security in Temporal Nexus

Temporal Cloud provides built-in Endpoint access controls and secure connectivity across Namespaces.
Self-hosted deployments can implement [custom Authorizers](/self-hosted-guide/security#authorizer-plugin).

## Runtime access controls {/* #runtime-access-controls */}

In Temporal Cloud, each Endpoint has an access control policy: an allowlist of caller Namespaces.

<CaptionedImage
    src="/img/cloud/nexus/nexus-workers-short.png"
    title="Nexus Security"
/>

Workers authenticate with their Namespace using mTLS or API key.
When a caller Workflow executes a Nexus Operation, Temporal Cloud verifies the caller's Namespace is in the Endpoint's allowlist before routing the request to the handler.
Temporal Cloud acts as a trusted broker across Namespace boundaries.

See [Configure runtime access controls](/nexus/registry#configure-runtime-access-controls).

## Secure connectivity {/* #secure-connectivity */}

:::info

Temporal Cloud has built-in secure connectivity across all Namespaces in an Account.

Self-hosted deployments rely on the Temporal Cluster being secure.

:::

Temporal Cloud secures all Nexus communication:

- Workers authenticate to their Namespace using mTLS or API key.
- mTLS encrypts all cross-Namespace Nexus traffic (start, cancel, and completion callbacks) across cells and regions.
- Endpoints are only accessible from within a Temporal Cloud Account through the Temporal SDK - not externally accessible.

## Payload encryption and Data Converter {/* #payload-encryption-data-converter */}

Nexus uses the same Data Converter as Workflows and Activities - JSON, Proto, and binary payloads are all supported.
If you use a Codec for encryption, it also encrypts Nexus payloads.

Caller and handler Workers must have compatible Data Converters.
Payloads are encrypted by the sender (caller encrypts input, handler encrypts result).

Three common approaches for cross-Namespace payload encryption:

### Option 1: Same encryption key {/* #same-encryption-key */}

Both Namespaces share the same encryption key.
Simplest approach - no additional configuration needed.

### Option 2: Pass KMS key ID in payload metadata {/* #kms-key-id-metadata */}

Each Namespace uses its own encryption key, with the KMS key ID passed in Temporal payload metadata.
The receiver reads the key ID from metadata and decrypts using KMS IAM permissions.

Works bi-directionally: caller encrypts input with the caller's key, handler decrypts using the key ID from metadata, then encrypts the result with the handler's key.
The Codec Server needs KMS decrypt permissions for all relevant keys.

See the [encryption sample](https://github.com/temporalio/samples-go/blob/main/encryption/data_converter.go) and the [reference-app-orders-go data converter](https://github.com/temporalio/reference-app-orders-go/blob/main/app/temporalutil/data_converter.go).

### Option 3: Wrapper types for endpoint-specific encryption keys {/* #endpoint-specific-keys */}

Use wrapper types (for example, `EndpointValue`) so the Data Converter selects an Endpoint-specific encryption key.
This encrypts only Nexus traffic with a dedicated key, without sharing Namespace keys across teams.

See the [draft endpoint-based encryption sample](https://github.com/temporalio/samples-go/compare/main...bergundy:samples-go:nexus-encryption-by-endpoint).

### Choosing an approach

Options 1 and 2, where both sides share the same key or flow the KMS key ID in payload metadata, work with the standard Data Converter.
Option 3 is more advanced and is intended for teams that don't want to share their Namespace encryption keys with other teams.

## Nexus Registry security {/* #managing-nexus-endpoints */}

See [Nexus Registry Roles and Permissions](/nexus/registry#roles-and-permissions).

---

## Nexus services

[Nexus Services](/glossary#nexus-service) are named collections of [Nexus Operations](/nexus/operations) that provide a contract for sharing across team boundaries.
A [Nexus Endpoint](/nexus/endpoints) exposes Services for callers to use.

Services are registered in a Worker that polls the Endpoint's target Task Queue.
Multiple Services can run in the same Worker.
Services typically run alongside the Workflows they abstract, or in a dedicated router Worker using the [router-queue pattern](/nexus/patterns#router-queue-pattern).

Callers reference a Service by name when executing a Nexus Operation.

---

## Temporal Nexus

:::info NEW TO NEXUS?

This page explains what Nexus is and how it works. To evaluate whether Nexus fits your use case, see the [evaluation guide](/evaluate/nexus).

:::

As a platform grows, coordinating work across teams and applications becomes increasingly difficult.
Nexus lets teams selectively expose functionality that other teams can discover and reuse, without exposing their internal implementation details.
This approach makes it easier to build new applications by reusing what already exists, forming the foundation for a more modular and collaborative platform.

## What is Nexus?

Nexus connects Temporal Applications across (and within) isolated Namespaces.
Each team gets their own Namespace for security and fault isolation, while exposing a clean service contract for others to use through a [Nexus Endpoint](/nexus/endpoints).

Designed for Durable Execution, Nexus combines a familiar SDK programming model with reliable execution, built-in observability, and multi-region connectivity in Temporal Cloud.

Nexus is peer-to-peer, not hierarchical.
Caller and handler Workflows are siblings that communicate across Namespace boundaries.

<CaptionedImage
    src="/img/cloud/nexus/nexus-overview-short.png"
    title="Nexus connects caller and handler Namespaces through a Nexus Endpoint"
    width="100%"
    zoom="true"
/>

## How Nexus works

### Services and Operations

A [Nexus Service](/nexus/services) is a named collection of [Nexus Operations](/nexus/operations) that a team exposes.
Operations abstract the underlying implementation - callers don't need to know whether an Operation starts a Workflow, sends a Signal, runs a Query, or executes other reliable code.

The [Operation lifecycle](/nexus/operations#operation-lifecycle) supports two modes:

- **Asynchronous** - Starts a Workflow (same or different Task Queue, with optional [Eager Start](/develop/worker-performance#eager-workflow-start)). Can run up to [60 days](/cloud/limits#nexus-operation-duration-limits).
- **Synchronous** - Completes within the [10-second handler deadline](/cloud/limits#nexus-operation-request-timeout). Use for Signals, Queries, Updates, or other reliable low-latency calls using the [Temporal SDK Client](/nexus/operations#executing-arbitrary-code-from-a-sync-handler).

Services and Operations are built with the Temporal SDK and typically [collocated](/nexus/patterns#collocated-pattern) in the same Worker as the Temporal primitives they abstract, or in a dedicated router Worker using the [router-queue pattern](/nexus/patterns#router-queue-pattern).

:::tip SDK GUIDES

- [Go](/develop/go/nexus/feature-guide) |
  [Java](/develop/java/nexus) |
  [Python](/develop/python/nexus) |
  [TypeScript](/develop/typescript/nexus) |
  [.NET](/develop/dotnet/nexus)

:::

### Endpoints and Registry

A [Nexus Endpoint](/nexus/endpoints) is a reverse proxy that decouples callers from handlers.
Callers reference an Endpoint by name. The Endpoint routes requests to a target Namespace and Task Queue.
Callers never need to know the handler's Namespace, Task Queue, or internal implementation.

Endpoints are managed in the [Nexus Registry](/nexus/registry) using the UI, CLI, or Cloud Ops API.

### Queue-based Worker architecture

Nexus uses the same queue-based Worker architecture as the rest of Temporal.
Handler Workers poll the Endpoint's target Task Queue for [Nexus Tasks](/tasks#nexus-task).
If a Nexus Service is down, caller Workflows continue to schedule Operations - they process when the service is back up.
No bespoke service deployments needed. Load balancing is automatic.
