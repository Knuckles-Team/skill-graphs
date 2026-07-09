    "As the Worker executes the code during Replay, it reaches the first call to execute an Activity and creates a `ScheduleActivityTask` Command. This Command matches the one expected based on the Event History. It's not only the right type of Command, with the same details, but it also occurs at the right position in the sequence of expected Commands. Therefore, Replay proceeds.",
    'The Worker now reaches the conditional statement with the random number generator. This time, the random number generator happens to return 14, so the conditional expression evaluates to `false`, and execution skips over the next line.',
    'The Worker now reaches the next Command which is to request execution of the `runDailyReport` Activity, so the Worker creates another `ScheduleActivityTask` Command.',
    'However, this is a different Command than it expected to find at this position in the Event History. Since the Workflow produced a different sequence of Commands during Replay than it was expecting due to the Event History that was produced prior to the crash, the Worker is unable to restore the previous state.',
    'The Workflow Execution was unable to be replayed due to a non-deterministic error.',
  ]}
/>

Note that non-deterministic failures do not fail the Workflow Execution by default. A non-deterministic failure is
considered a [Workflow Task Failure](https://docs.temporal.io/references/failures#workflow-task-failures) which is
considered a transient failure, meaning it retries over and over. Users can also fix the source of non-determinism,
perhaps by removing the Activity, and then restart the Workers. This means that this type of failure can recover by
itself. You can also use a strategy called versioning to address this non-determinism error. See
[versioning](https://docs.temporal.io/develop/typescript/workflows/versioning) to learn more.

For more information on how Temporal handles Durable Execution or to see these slides in a video format with more
explanation, check out our free, self-paced courses: [Temporal 102](https://learn.temporal.io/courses/temporal_102/) and
[Versioning Workflows](https://learn.temporal.io/courses/versioning/).

## Temporal Applications Support Non-Deterministic Operations

We want to emphasize that although your Workflows themselves need to be deterministic, your application itself does not!

Remember that pretty much anything that interacts with the external world is inherently non-deterministic:

- Calling LLM APIs
- Querying databases
- Reading or writing files
- Making HTTP requests to external services

**Good news**: Your Temporal application can absolutely handle all of these operations. While your Workflow must be
deterministic, your application absolutely can handle any type of non-deterministic operation, including those listed
above. This gives you the best of both worlds—the crash-proof reliability of a Workflow and the resiliency of Activities
which have built-in support for retries.

---

## Extensibility

Temporal offers many mechanisms to augment the functionality of Workflows and Activities.
These allow you to customize how data is serialized, propagate metadata across execution boundaries, and inject cross-cutting behavior like tracing and logging.

- [Data Conversion](/dataconversion) - Customize how arguments and return values are serialized, compressed, or encrypted
- [Context Propagation](/encyclopedia/context-propagation) - Pass custom metadata (tracing IDs, tenant IDs, auth tokens) across Workflow, Activity, and Child Workflow boundaries
- [Interceptors](/encyclopedia/interceptors) - Add cross-cutting behavior (observability, authorization, header manipulation) before and after SDK operations
- [Plugins](/encyclopedia/plugins) - Bundle interceptors, context propagators, data converters, and built-in definitions into reusable packages

---

## Failures and error handling

Temporal provides Durable Execution, which guarantees that your application runs to completion despite infrastructure issues, network problems, and Worker crashes.
However, not all failures are handled automatically by the platform.
Understanding the difference between platform-level and application-level failures is key to building reliable Temporal applications.

This section covers:

- **[Application failures](/encyclopedia/application-failures)**: What application failures are, how Temporal represents them, and how they propagate through your code.
- **[Detecting Activity failures](/encyclopedia/detecting-activity-failures)**: How to use timeouts and Heartbeats to detect when Activities fail or become unresponsive.
- **[Detecting Workflow failures](/encyclopedia/detecting-workflow-failures)**: How Workflow-level timeouts work and when they apply.
- **[Retry Policies](/encyclopedia/retry-policies)**: How to configure automatic retry behavior for Activities and Workflows.

For prescriptive guidance on building an error handling strategy, see [Error handling](/best-practices/error-handling).

---

## Temporal Encyclopedia

[Temporal](/evaluate/why-temporal) provides developers a suite of effective tools for building reliable applications at scale.

The following Encyclopedia pages describe the concepts, components, and features of Temporal in detail:

- [Temporal](/temporal)
- [Temporal SDKs](/encyclopedia/temporal-sdks)
- [Temporal Client](/temporal-client)
- [Workflows](/workflows)
- [Activities](/activities)
- [Failures and error handling](/encyclopedia/failures-and-error-handling)
- [Workers](/workers)
- [Event History](/encyclopedia/event-history/)
- [Workflow Message Passing](/encyclopedia/workflow-message-passing/)
- [Child Workflows](/child-workflows)
- [Visibility](/visibility)
- [Temporal Service](/temporal-service)
- [Namespaces](/namespaces)
- [Temporal Nexus](/nexus)
- [Extensibility](/encyclopedia/extensibility)

For a complete list of Temporal terms, see the [Glossary](/glossary).

For information on how to implement the developer-facing features see the [Develop](/develop) section.

For information on how to use Temporal Cloud see the [Temporal Cloud production deployment](/cloud) section.

For information on how to self-host a Temporal Service see the [Self-hosted production deployment](/self-hosted-guide) section.

---

## Interceptors

Interceptors let you add cross-cutting behavior before and after SDK operations such as starting a Workflow, executing an Activity, or handling a Signal. They work like middleware: each interceptor wraps the next, forming a chain that executes around the underlying operation.

Common use cases:

- Observability (logging, metrics, tracing)
- Authorization and authentication checks
- Header manipulation (propagating metadata)
- Input/output validation

## Implementing Interceptors

Here are SDK-specific guides:

- [Python](/develop/python/workers/interceptors)
- [TypeScript](/develop/typescript/workers/interceptors)
- [.NET](/develop/dotnet/workers/interceptors)

---

## Global Namespace

This page provides an overview of Global Namespace.

## What is a Global Namespace? {/* #global-namespace */}

A Global Namespace is a [Namespace](/namespaces) that exists across Clusters when [Multi-Cluster Replication](/temporal-service/multi-cluster-replication) is set up.

- [How to register a Global Namespace](/cli/command-reference/operator#create)
- [How to change the active Cluster for a Global Namespace](/cli/command-reference/operator#update)

The Global Namespace feature enables Workflow Executions to progress through another Cluster in the event of a failover.

A Global Namespace may be replicated to any number of Clusters, but is active in only one Cluster at any given time.

For a failover to be successful, Worker Processes must be polling for Tasks for the Global Namespace on all Clusters.

A Global Namespace has a failover version.
Because a failover can be triggered from any Cluster, the failover version prevents certain conflicts from occurring if a failover is mistakenly triggered simultaneously on two Clusters.

Only the active Cluster dispatches [Tasks](/tasks#task); however, certain conflicts are possible.
Unlike regular Namespaces, which provide at-most-once semantics for an Activity Execution, Global Namespaces can support only at-least-once semantics (see [Conflict resolution](/temporal-service/multi-cluster-replication#conflict-resolution)).
Worker Processes on the standby Clusters are idle until a failover occurs and their Cluster becomes active.

Temporal Application API calls made to a non-active Cluster are rejected with a **NamespaceNotActiveError** which contains the name of the current active Cluster.
It is the responsibility of the Temporal Application to call the Cluster that is currently active.

---

## Temporal Namespace

:::info Open source and Temporal Cloud
This page covers core namespace concepts that apply to both open source Temporal and Temporal Cloud.

Temporal Cloud namespaces include additional capabilities, such as [API key](/cloud/api-keys) and [mTLS authentication](/cloud/certificates), [built-in role-based access controls](/cloud/manage-access/roles-and-permissions#namespace-level-permissions), [high availability replication](/cloud/high-availability), and [namespace tags](/cloud/namespaces#tag-a-namespace).

Moving from self-hosting to Cloud, or the reverse, requires zero code changes and incurs zero downtime.
:::

A Namespace is a unit of isolation within the [Temporal Platform](/temporal#temporal-platform).

[Task Queues](/task-queue) and [Workflow Executions](/workflow-execution) belong to a Namespace.
When a Workflow Execution is spawned, it does so within a specific Namespace.

## Usage

- **Workflow ID uniqueness**: Temporal guarantees a unique Workflow Id within a Namespace.
  Workflow Executions may have the same Workflow Id if they are in different Namespaces.
- **Resource isolation**: Heavy traffic from one Namespace will not impact other Namespaces running on the same Temporal Service.
- **Configuration boundaries**: Options like the [Retention Period](/temporal-service/temporal-server#retention-period) and [Archival](/temporal-service/archival) destination are configured per Namespace.
- **Default Namespace**: If no Namespace is specified, the Temporal Service uses the Namespace "default" for all Temporal SDKs and the Temporal CLI.
  You must create a Namespace before using it in your Client.
- **Multi-tenancy**: A single Namespace is still multi-tenant.
  Multiple applications or teams can share a Namespace, but must coordinate on Workflow ID and Task Queue naming to avoid conflicts.

## Namespace operations

For how to create and manage Namespaces:

- **Open source Temporal**: [Managing Namespaces](/self-hosted-guide/namespaces)
- **Temporal Cloud**: [Temporal Cloud Namespaces](/cloud/namespaces)

---

## Nexus Endpoints

A [Nexus Endpoint](/glossary#nexus-endpoint) is a fully managed reverse proxy for [Nexus Services](/nexus/services).
It routes requests from a caller Workflow to a target Namespace and Task Queue.
Callers only need to know the Endpoint name - the target Namespace, Task Queue, and internal implementation are encapsulated.

Workers handle Nexus requests by registering one or more Services and polling the Endpoint's target Task Queue.
Multiple Endpoints can target different Task Queues in the same Namespace.

The Endpoint description field supports markdown for documenting available Operations, contact information, or schema links.

## Reverse proxy for Nexus Services, not a general purpose proxy
A Nexus Endpoint acts as a reverse proxy for a single Nexus Service, routing requests to one target Namespace and Task Queue.

Unlike general-purpose proxies, it does not route to multiple backends. Instead, it provides a secure, managed connection to a specific upstream target, which can be in any region or cloud.
The [EndpointSpec](https://github.com/temporalio/api/blob/2a5b3951e71565e28628edea1b3d88d69ed26607/temporal/api/nexus/v1/message.proto#L170) support the following [target type](https://github.com/temporalio/api/blob/2a5b3951e71565e28628edea1b3d88d69ed26607/temporal/api/nexus/v1/message.proto#L185):

- **Worker**: Route to a target Namespace and Task Queue.

## Deploying a Nexus Endpoint

Adding an Endpoint to the [Nexus Registry](/nexus/registry) deploys it immediately. The Endpoint is available at runtime as soon as it's registered.

---

## Error Handling - Temporal Nexus

Nexus Operations can return errors for a caller Workflow to handle.
Errors from an asynchronous Operation's underlying Workflow propagate back to the caller.

## Errors in Nexus handlers

Nexus handlers may return [different error types](/references/failures#nexus-errors).
By default, handler errors are retryable unless they are:

- [Application Failures](/references/failures#nexus-errors) explicitly marked as non-retryable.
- [Nexus Operation errors](/references/failures#nexus-errors) that resolve an Operation as failed or canceled.
- [Non-retryable Nexus errors](/references/failures#non-retryable-nexus-errors).

When the caller's Nexus Machinery receives an error:

- **Non-retryable** - A [NexusOperationFailed](/references/events#nexusoperationfailed) event is added to the caller's Event History.
- **Retryable** - The Nexus Machinery [automatically retries](/nexus/operations#automatic-retries). These errors surface in [Pending Operations](/nexus/execution-debugging/#pending-operations).

:::tip

Return a [specific Nexus error type](/references/failures#nexus-errors) to avoid infinite retries.
See [errors in Nexus Operations](/references/failures#errors-in-nexus-operations) for additional details.

:::

## Nexus error handling in caller Workflows

When a Nexus Operation fails, the caller receives a Nexus Operation Failure containing the operation name, token, and failure reason.
The cause field indicates the type of error (for example, Application Error or Canceled Error).

:::tip RESOURCES

- [Errors in Nexus Operations](/references/failures#errors-in-nexus-operations)
- [Nexus Errors](/references/failures#nexus-errors)
- [Nexus Operation Failures](/references/failures#nexus-operation-failure)

:::

---

## Execution Debugging - Temporal Nexus

Nexus supports end-to-end execution debugging across caller Workflows, Nexus Operations, and handler Workflows - even across [multi-level calls](/nexus#multi-level-calls) spanning multiple Namespaces.

## Bi-directional linking

Bidirectional links connect Nexus Operation events in the caller's Event History to corresponding events in the handler's Event History.
They are automatically wired by SDK builder functions like New-Workflow-Run-Operation, enabling click-through navigation across Namespaces, regions, and clouds in the Temporal UI.

<CaptionedImage
    src="/img/cloud/nexus/nexus-bi-directional-linking.png"
    title="Bi-directional linking"
    zoom="true"
/>

- **Forward**: From a caller's Nexus Operation event to the handler's Workflow.
- **Backward**: From the handler's Workflow back to the caller's Nexus Operation event.

## Pending Operations

Pending Nexus Operations are displayed in the UI on the Workflow details page and can be listed from the CLI using the `temporal workflow describe` command.

From the UI:

<CaptionedImage
    src="/img/cloud/nexus/pending-nexus-operations.png"
    title="Pending Operations"
    zoom="true"
/>

From the CLI:

```
temporal workflow describe

Pending Nexus Operations: 1

  Endpoint                 myendpoint
  Service                  my-hello-service
  Operation                echo
  OperationToken
  State                    BackingOff
  Attempt                  6
  ScheduleToCloseTimeout   0s
  NextAttemptScheduleTime  20 seconds from now
  LastAttemptCompleteTime  11 seconds ago
  LastAttemptFailure       {"message":"handler error (INTERNAL): internal error","applicationFailureInfo":{}}
```

[Retryable errors](/nexus/error-handling#errors-in-nexus-handlers) surface in the Pending Operation.
Non-retryable errors resolve the Operation with a [Failed](/references/events#nexusoperationfailed), [TimedOut](/references/events#nexusoperationtimedout), or [Canceled](/references/events#nexusoperationcanceled) event.

## Pending Callbacks

Nexus completion callbacks are sent from the handler's Namespace to the caller's Namespace for asynchronous Operations.
These can be viewed in the UI or from the CLI using the `temporal workflow describe` command.

From the UI:

<CaptionedImage
    src="/img/cloud/nexus/nexus-callback.png"
    title="Pending Callbacks"
    zoom="true"
/>

From the CLI:

```
temporal workflow describe

Callbacks: 1

  URL               https://nexus.phil-caller-Namespace.a2dd6.cluster.tmprl.cloud:7243/Namespaces/phil-caller-Namespace.a2dd6/nexus/callback
  Trigger           WorkflowClosed
  State             Succeeded
  Attempt           1
  RegistrationTime  32 minutes ago
```

## Tracing

Temporal integrates with [OpenTelemetry](https://opentelemetry.io/) and [OpenTracing](https://opentracing.io/) to visualize call graphs across Activities, Nexus Operations, and Child Workflows.
Enable tracing by installing an interceptor on the Client or Worker:

- [Go SDK](https://github.com/temporalio/samples-go/tree/main/opentelemetry)
- [Java SDK](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/tracing)
- [Python SDK](https://github.com/temporalio/samples-python/tree/main/open_telemetry)
- [TypeScript](https://github.com/temporalio/samples-typescript/tree/main/interceptors-opentelemetry)
- [.NET SDK](https://github.com/temporalio/samples-dotnet/tree/main/src/OpenTelemetry)

---

## Nexus Metrics

Nexus provides SDK metrics, Cloud metrics, and OSS Cluster metrics in addition to integrated [execution debugging](/nexus/execution-debugging).

## SDK Metrics

[SDK metrics](/references/sdk-metrics) are emitted from a Nexus Worker, including:

- [nexus_poll_no_task](/references/sdk-metrics#nexus_poll_no_task)
- [nexus_task_schedule_to_start_latency](/references/sdk-metrics#nexus_task_schedule_to_start_latency)
- [nexus_task_execution_failed	Worker](/references/sdk-metrics#nexus_task_execution_failed)
- [nexus_task_execution_latency](/references/sdk-metrics#nexus_task_execution_latency)
- [nexus_task_endtoend_latency](/references/sdk-metrics#nexus_task_endtoend_latency)

## Cloud Metrics

[Cloud metrics](/cloud/metrics/reference) are emitted by Temporal Cloud, including:

- Caller Namespace
  - RespondWorkflowTaskCompleted \- schedule a Nexus Operation.
- Handler Namespace
  - PollNexusTaskQueue \- get a [Nexus Task](/tasks#nexus-task) to process, for example to start a Nexus Operation.
  - RespondNexusTaskCompleted \- report the Nexus Task was successful.
  - RespondNexusTaskFailed \- report the Nexus Task failed.

## OSS Cluster Metrics

[Cluster metrics](/references/cluster-metrics#nexus-metrics) are emitted from an OSS Cluster, including:

- History Service metrics
- Concurrency Limiter metrics
- Frontend Service metrics

---

## Nexus Operations

[Nexus Operations](/glossary#nexus-operation) can be synchronous or asynchronous. Unlike a traditional RPC, an asynchronous Nexus Operation has an operation token that can be used to re-attach to a long-running Operation backed by a Workflow.
An Operation's lifecycle spans scheduling, reliable delivery with retries, handler execution, and result or callback completion.

## SDK support {/* #sdk-support */}

:::tip SDK GUIDES

- [Go](/develop/go/nexus/feature-guide) |
  [Java](/develop/java/nexus) |
  [Python](/develop/python/nexus) |
  [TypeScript](/develop/typescript/nexus) |
  [.NET](/develop/dotnet/nexus)

:::

**Caller side:** A caller Workflow executes a Nexus Operation through a [Nexus Endpoint](/nexus/endpoints) using the Temporal SDK.

**Handler side:** [Nexus Services](/nexus/services) and their Operations are registered with a Worker that polls the Endpoint's target Task Queue. Operations are defined using SDK builder functions:

- **New-Workflow-Run-Operation** - Start a Workflow as an asynchronous Operation.
- **New-Sync-Operation** - Run a synchronous Operation: invoke a Query, Signal, or Update, or execute other reliable code using the Temporal SDK Client.

## Nexus Operation lifecycle {/* #operation-lifecycle */}

When a caller Workflow executes a Nexus Operation, the command is atomically handed off to the [Nexus Machinery](/glossary#nexus-machinery).
The Machinery ensures [at-least-once](#at-least-once-execution-semantics-and-idempotency) execution with [automatic retries](#automatic-retries) and reliable result delivery.

<CaptionedImage
    src="/img/cloud/nexus/nexus-overview.png"
    title="Nexus Overview"
/>

### Synchronous Operation lifecycle

Synchronous Operations must complete within the [10-second handler deadline](/cloud/limits#nexus-operation-request-timeout), as measured from the caller's Nexus Machinery.

<CaptionedImage
    src="/img/cloud/nexus/nexus-sync-operation.png"
    title="Nexus Sync Operation Lifecycle"
/>

Lifecycle for a synchronous Operation (for example, to Signal, Query, or Update a Workflow, or to run other reliable code):

1. Caller Workflow executes a Nexus Operation.
1. Caller Worker issues a [ScheduleNexusOperation](/references/commands#schedulenexusoperation) command.
1. Caller Namespace records a [NexusOperationScheduled](/references/events#nexusoperationscheduled) event.
1. Caller Nexus Machinery sends the start request.
1. Handler Nexus Machinery sync-matches the request to a handler Worker.
1. Handler Worker receives a [Nexus Task](/tasks#nexus-task) by polling the Endpoint's target Task Queue.
1. Handler processes the task using **New-Sync-Operation**.
1. Handler responds with the Operation result.
1. Caller Namespace records a [Completed](/references/events#nexusoperationcompleted) or [Failed](/references/events#nexusoperationfailed) event.
1. Caller Worker polls for a Workflow Task.
1. Caller Workflow receives the result.

<CaptionedImage
    src="/img/cloud/nexus/nexus-workers-short-sync-op-sequence.png"
    title="Nexus"
/>

:::tip

Stay within the [request deadline](/cloud/limits#nexus-operation-request-timeout) to avoid timeouts.
Timed-out handlers are retried until the Operation's Schedule-to-Close timeout is exceeded.

:::

### Asynchronous Operation lifecycle {/* #asynchronous-operation-lifecycle */}

Asynchronous Operations can run up to [60 days](/cloud/limits#nexus-operation-duration-limits) (the maximum Schedule-to-Close timeout in Temporal Cloud).
Differences from the synchronous lifecycle are in **bold**.

<CaptionedImage
    src="/img/cloud/nexus/nexus-async-operation.png"
    title="Nexus Async Operation Lifecycle"
/>

1. Caller Workflow executes a Nexus Operation.
1. Caller Worker issues a [ScheduleNexusOperation](/references/commands#schedulenexusoperation) command.
1. Caller Namespace records a [NexusOperationScheduled](/references/events#nexusoperationscheduled) event.
1. Caller Nexus Machinery sends the start request.
1. Handler Nexus Machinery sync-matches the request to a handler Worker.
1. Handler Worker receives a [Nexus Task](/tasks#nexus-task) by polling the Endpoint's target Task Queue.
1. Handler processes the task using **New-Workflow-Run-Operation**.
1. Handler responds with the **start Operation response**.
1. Caller Namespace records a **[NexusOperationStarted](/references/events#nexusoperationstarted)** event.
1. **Handler Workflow completes and a [Nexus Completion Callback](/glossary#nexus-async-completion-callback) is delivered to the caller's Nexus Machinery.**
1. Caller Namespace records a [Completed](/references/events#nexusoperationcompleted) or [Failed](/references/events#nexusoperationfailed) event.
1. Caller Worker polls for a Workflow Task.
1. Caller Workflow receives the result.

<CaptionedImage
    src="/img/cloud/nexus/nexus-workers-short-async-op-sequence.png"
    title="Nexus"
/>

### Executing code from a synchronous handler {/* #executing-arbitrary-code-from-a-sync-handler */}

Synchronous handlers can execute code directly but must complete within the [handler deadline](/cloud/limits#nexus-operation-request-timeout).
Use the Temporal SDK Client to invoke Signals, Queries, Updates, or other reliable code.

:::caution

Use [async Operations](#asynchronous-operation-lifecycle) for long-running work.
Repeated sync handler failures can trip the [circuit breaker](#circuit-breaking), blocking all Operations from that caller to the Endpoint.

:::

<CaptionedImage
    src="/img/cloud/nexus/nexus-sync-operation-arbitrary-code.png"
    title="Nexus Operations with Arbitrary Code"
/>

### System interactions

Nexus uses the same queue-based Worker architecture as the rest of Temporal.
Workers interact with their Namespace gRPC endpoint. Nexus Machinery on both sides handles cross-Namespace communication.

<CaptionedImage
    src="/img/cloud/nexus/nexus-workers.png"
    title="Nexus Queue-based Worker Architecture"
/>

At a high level, when a caller Workflow executes a Nexus Operation:

1. The caller Worker schedules the Operation with a [ScheduleNexusOperation command](/references/commands#schedulenexusoperation), atomically handing off execution to the caller's Nexus Machinery.
2. The handler Worker receives a [Nexus Task](/tasks#nexus-task) by polling the Endpoint's target Task Queue.
3. The handler processes the task and returns the result (synchronous) or an Operation token (asynchronous).
4. The caller's Nexus Machinery records a NexusOperation event ([Started](/references/events#nexusoperationstarted), [Completed](/references/events#nexusoperationcompleted), [Failed](/references/events#nexusoperationfailed), [Canceled](/references/events#nexusoperationcanceled), or [TimedOut](/references/events#nexusoperationtimedout)) in the caller's Event History.
