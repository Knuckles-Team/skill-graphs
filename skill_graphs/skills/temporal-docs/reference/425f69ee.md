To check both types of cases, TypeScript has the [isCancellation](https://typescript.temporal.io/api/namespaces/workflow#iscancellation) helper.

When a Workflow, Activity or Nexus Operation is successfully Cancelled, a Cancelled Failure is the `cause` field of the Activity Failure, Nexus Operation Failure or "Workflow failed" error.

- TypeScript: [CancelledFailure](https://typescript.temporal.io/api/classes/common.CancelledFailure)
- Java: [CanceledFailure](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/CanceledFailure.html)
- Go: [CanceledError](https://pkg.go.dev/go.temporal.io/sdk/temporal#CanceledError)
- Python: [CancelledError](https://python.temporal.io/temporalio.exceptions.CancelledError.html)
- PHP: [CanceledFailure](https://php.temporal.io/classes/Temporal-Exception-Failure-CanceledFailure.html)
- Proto: [CanceledFailureInfo](https://api-docs.temporal.io/#temporal.api.failure.v1.CanceledFailureInfo) and [Failure](https://api-docs.temporal.io/#temporal.api.failure.v1.Failure)

## Activity Failure

An Activity Failure is delivered to the Workflow Execution when an Activity fails.
It contains information about the failure and the Activity Execution; for example, the Activity Type and Activity Id.
The reason for the failure is in the `cause` field.
For example, if an Activity Execution times out, the `cause` is a [Timeout Failure](#timeout-failure).

- TypeScript: [ActivityFailure](https://typescript.temporal.io/api/classes/common.ActivityFailure)
- Java: [ActivityFailure](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/ActivityFailure.html)
- Go: [ActivityError](https://pkg.go.dev/go.temporal.io/sdk/temporal#ActivityError)
- Python: [ActivityError](https://python.temporal.io/temporalio.exceptions.ActivityError.html)
- PHP: [ActivityFailure](https://php.temporal.io/classes/Temporal-Exception-Failure-ActivityFailure.html)
- Proto: [ActivityFailureInfo](https://api-docs.temporal.io/#temporal.api.failure.v1.ActivityFailureInfo) and [Failure](https://api-docs.temporal.io/#temporal.api.failure.v1.Failure)

## Nexus Operation Failure

A Nexus Operation Failure is delivered to the Workflow Execution when a Nexus Operation fails.
It contains information about the failure and the Nexus Operation Execution; for example, the Nexus Operation name and Nexus Operation token.
The reason for the failure is in the message and cause (typically an Application Error or a Canceled Error).

- Go: NexusOperationError
- Proto: NexusOperationFailureInfo

A Nexus Operation Failure includes the following fields:

- Endpoint is set to the name of the endpoint.
- Service is set to the name of the service.
- Operation is set to the name of the operation.
- Operation_token is set if this is an async operation, which can be used to perform additional actions like cancelling the operation.
- Scheduled_event_id is set to the caller’s event id that scheduled the operation.
- Message is set to a generic unsuccessful error message.
- Cause is set to the underlying Application Failure with the following fields:
  - Non-retryable is set to true.
  - Type is set to the error's type name.
  - Message is set to the error message.
- Nexus_error_code is set to the underlying Nexus error code.

## Child Workflow Failure

A Child Workflow Failure is delivered to the Workflow Execution when a Child Workflow Execution fails.
It contains information about the failure and the Child Workflow Execution; for example, the Workflow Type and Workflow Id.
The reason for the failure is in the `cause` field.

- TypeScript: [ChildWorkflowFailure](https://typescript.temporal.io/api/classes/common.ChildWorkflowFailure)
- Java: [ChildWorkflowFailure](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/ChildWorkflowFailure.html)
- Go: [ChildWorkflowExecutionError](https://pkg.go.dev/go.temporal.io/sdk/temporal#ChildWorkflowExecutionError)
- Python: [ChildWorkflowError](https://python.temporal.io/temporalio.exceptions.ChildWorkflowError.html)
- PHP: [ChildWorkflowFailure](https://php.temporal.io/classes/Temporal-Exception-Failure-ChildWorkflowFailure.html)
- Proto: [ChildWorkflowExecutionFailureInfo](https://api-docs.temporal.io/#temporal.api.failure.v1.ChildWorkflowExecutionFailureInfo) and [Failure](https://api-docs.temporal.io/#temporal.api.failure.v1.Failure)

## Timeout Failure

A Timeout Failure represents the timeout of an Activity or Workflow.

When an Activity times out, the last Heartbeat details it emitted is attached.

- TypeScript: [TimeoutFailure](https://typescript.temporal.io/api/classes/common.TimeoutFailure)
- Java: [TimeoutFailure](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/TimeoutFailure.html)
- Go: [TimeoutError](https://pkg.go.dev/go.temporal.io/sdk/temporal#TimeoutError)
- Python: [TimeoutError](https://python.temporal.io/temporalio.exceptions.TimeoutError.html)
- PHP: [TimeoutFailure](https://php.temporal.io/classes/Temporal-Exception-Failure-TimeoutFailure.html)
- Proto: [TimeoutFailureInfo](https://api-docs.temporal.io/#temporal.api.failure.v1.TimeoutFailureInfo) and [Failure](https://api-docs.temporal.io/#temporal.api.failure.v1.Failure)

## Terminated Failure

A Terminated Failure is used as the `cause` of an error when a Workflow is terminated, and you receive the error in one of the following locations:

- Inside a Workflow that's waiting for the result of a Child Workflow.
- When waiting for the result of a Workflow on the Client.

In the SDKs:

- TypeScript: [TerminatedFailure](https://typescript.temporal.io/api/classes/common.TerminatedFailure)
- Java: [TerminatedFailure](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/TerminatedFailure.html)
- Go: [TerminatedError](https://pkg.go.dev/go.temporal.io/sdk/temporal#TerminatedError)
- Python: [TerminatedError](https://python.temporal.io/temporalio.exceptions.TerminatedError.html)
- PHP: [TerminatedFailure](https://php.temporal.io/classes/Temporal-Exception-Failure-TerminatedFailure.html)
- Proto: [TerminatedFailureInfo](https://api-docs.temporal.io/#temporal.api.failure.v1.TerminatedFailureInfo) and [Failure](https://api-docs.temporal.io/#temporal.api.failure.v1.Failure)

## Server Failure

A Server Failure is used for errors that originate in the Temporal Service.

- TypeScript: [ServerFailure](https://typescript.temporal.io/api/classes/common.ServerFailure)
- Java: [ServerFailure](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/ServerFailure.html)
- Go: [ServerError](https://pkg.go.dev/go.temporal.io/sdk/temporal#ServerError)
- Python: [ServerError](https://python.temporal.io/temporalio.exceptions.ServerError.html)
- PHP: [ServerFailure](https://php.temporal.io/classes/Temporal-Exception-Failure-ServerFailure.html)
- Proto: [ServerFailureInfo](https://api-docs.temporal.io/#temporal.api.failure.v1.ServerFailureInfo) and [Failure](https://api-docs.temporal.io/#temporal.api.failure.v1.Failure)

---

## Temporal Platform references

- [API reference](/references/api-reference)
- [SDK metrics reference](/references/sdk-metrics)
- [Commands reference](/references/commands)
- [Events reference](/references/events)
- [Web UI environment variables reference](/references/web-ui-environment-variables)
- [Temporal Service configuration reference](/references/configuration)
- [Temporal Web UI configuration reference](/references/web-ui-configuration)
- [Temporal Cloud Operation reference](/references/operation-list)
- [Glossary](/glossary)

---

## Operations

Temporal Cloud [rate limits operations per second (OPS)](/cloud/limits#operations-per-second) per namespace. An operation is anything 1. a user does directly, or 2. Temporal does on behalf of the user in the background that results in load on Temporal Server. The exception is visibility queries: they do hit the Server (the query is passed from the server to the visibility store), but primarily the load is on the visibility system. Visibility rate limits are separate from OPS rate limits.

Below is the list of operations, including:
- operation name
- description
- priority (foreground is higher priority, background is lower priority)
- effect of that operation being throttled

<OperationsTable />

---

## Temporal SDK metrics reference

:::info SDK metrics

The information on this page is relevant to [Temporal SDKs](/encyclopedia/temporal-sdks).

See [Cloud metrics](/cloud/metrics/) for metrics emitted by [Temporal Cloud](/cloud/overview).

See [Cluster metrics](/references/cluster-metrics) for metrics emitted by the [OSS Cluster](/temporal-service).

Some SDKs may emit metrics beyond what is listed in this SDK Metrics reference.
Only metrics included in this Metrics reference have guaranteed, defined behavior.
Other metrics are considered deprecated, inconsistent or experimental.

:::

The Temporal SDKs emit a set of metrics from Temporal Client usage and Worker Processes.

- [How to emit metrics using the Go SDK](/develop/go/platform/observability#metrics)
- [How to emit metrics using the Java SDK](/develop/java/platform/observability#metrics)
- [How to emit metrics using the Python SDK](/develop/python/platform/observability#metrics)
- [How to emit metrics using the TypeScript SDK](/develop/typescript/platform/observability#metrics)
- [How to emit metrics using the .NET SDK](/develop/dotnet/platform/observability#metrics)
- [How to emit metrics using the Ruby SDK](/develop/ruby/platform/observability#metrics)
- [How to tune Worker performance based on metrics](/develop/worker-performance)

All metrics are prefixed with `temporal_` before being exported to their configured destination.
(The prefix has been removed in parts of this reference.)
Currently, some metrics are specific to certain SDKs.

TypeScript, Python, .NET, and Ruby SDK metrics are defined in the Core SDK.

PHP and Go metrics are defined in the Go SDK.

Java metrics are defined in the Java SDK.
Metrics are defined in the following locations.

- [Core SDK Worker metrics](https://github.com/temporalio/sdk-rust/blob/main/crates/sdk-core/src/telemetry/metrics.rs)
- [Core SDK Client metrics](https://github.com/temporalio/sdk-rust/blob/main/crates/client/src/metrics.rs)
- [Java SDK Worker metrics](https://github.com/temporalio/sdk-java/blob/master/temporal-sdk/src/main/java/io/temporal/worker/MetricsType.java)
- [Java SDK Client metrics](https://github.com/temporalio/sdk-java/blob/master/temporal-serviceclient/src/main/java/io/temporal/serviceclient/MetricsType.java)
- [Go SDK Worker and Client metrics](https://github.com/temporalio/sdk-go/blob/c32b04729cc7691f80c16f80eed7f323ee5ce24f/internal/common/metrics/constants.go)

:::note Metric units across SDKs

The unit of measurement for metrics can vary based on which SDK they are being reported from:

**Core-based SDKs:** Metrics of the type Histogram are measured in _milliseconds_ by default.
This can be customized to use seconds for SDKs using [Core SDK](/glossary#core-sdk).
The Core SDK is a shared common core library used by several Temporal SDKs, including TypeScript, Python, and .NET.

**Java and Go SDKs:** Metrics of the type Histogram are measured in _seconds_.

:::

Each metric may have some combination of the following keys attached to them:

- `task-queue`: Task Queue that the Worker Entity is polling
- `namespace`: Namespace the Worker is bound to
- `poller_type`: One of the following:
  - `workflow_task`
  - `activity_task`
  - `nexus_task` (Go and Java only)
  - `sticky_workflow_task`
- `worker_type`: One of the following:
  - `ActivityWorker`
  - `WorkflowWorker`
  - `LocalActivityWorker` (Go and Java only)
  - `NexusWorker` (Go and Java only)
- `activity_type`: The name of the Activity Function the metric is associated with
- `workflow_type`: The name of the Workflow Function the metric is associated with
- `operation`: RPC method name; available for metrics related to Temporal Client gRPC requests

Some keys may not be available in every SDK, and Histogram metrics may have different buckets in each SDK.

| Metric name                                                                                      | Emitted by     | Metric type | Availability   |
| ------------------------------------------------------------------------------------------------ | -------------- | ----------- | -------------- |
| [temporal_activity_execution_cancelled](#activity_execution_cancelled)                           | Worker         | Counter     | Java           |
| [temporal_activity_execution_failed](#activity_execution_failed)                                 | Worker         | Counter     | Core, Go, Java |
| [temporal_activity_execution_latency](#activity_execution_latency)                               | Worker         | Histogram   | Core, Go, Java |
| [temporal_activity_poll_no_task](#activity_poll_no_task)                                         | Worker         | Counter     | Core, Go, Java |
| [temporal_activity_schedule_to_start_latency](#activity_schedule_to_start_latency)               | Worker         | Histogram   | Core, Go, Java |
| [temporal_activity_succeed_endtoend_latency](#activity_succeed_endtoend_latency)                 | Worker         | Histogram   | Core, Go, Java |
| [temporal_activity_task_error](#activity_task_error)                                             | Worker         | Counter     | Go             |
| [temporal_corrupted_signals](#corrupted_signals)                                                 | Worker         | Counter     | Go, Java       |
| [temporal_local_activity_execution_cancelled](#local_activity_execution_cancelled)               | Worker         | Counter     | Core, Go, Java |
| [temporal_local_activity_execution_failed](#local_activity_execution_failed)                     | Worker         | Counter     | Core, Go, Java |
| [temporal_local_activity_execution_latency](#local_activity_execution_latency)                   | Worker         | Histogram   | Core, Go, Java |
| [temporal_local_activity_succeeded_endtoend_latency](#local_activity_succeeded_endtoend_latency) | Worker         | Histogram   | Core, Go, Java |
| [temporal_local_activity_total](#local_activity_total)                                           | Worker         | Counter     | Core, Go, Java |
| [temporal_long_request](#long_request)                                                           | Service Client | Counter     | Core, Go, Java |
| [temporal_long_request_failure](#long_request_failure)                                           | Service Client | Counter     | Core, Go, Java |
| [temporal_long_request_latency](#long_request_latency)                                           | Service Client | Histogram   | Core, Go, Java |
| [temporal_nexus_poll_no_task](#nexus_poll_no_task)                                               | Worker         | Counter     | Core, Go, Java |
| [temporal_nexus_task_schedule_to_start_latency](#nexus_task_schedule_to_start_latency)           | Worker         | Histogram   | Core, Go, Java |
| [temporal_nexus_task_execution_failed](#nexus_task_execution_failed)                             | Worker         | Counter     | Core, Go, Java |
| [temporal_nexus_task_execution_latency](#nexus_task_execution_latency)                           | Worker         | Histogram   | Core, Go, Java |
| [temporal_nexus_task_endtoend_latency](#nexus_task_endtoend_latency)                             | Worker         | Histogram   | Core, Go, Java |
| [temporal_num_pollers](#num_pollers)                                                             | Worker         | Gauge       | Core, Go       |
| [temporal_poller_start](#poller_start)                                                           | Worker         | Counter     | Go, Java       |
| [temporal_request](#request)                                                                     | Service Client | Counter     | Core, Go, Java |
| [temporal_request_failure](#request_failure)                                                     | Service Client | Counter     | Core, Go, Java |
| [temporal_request_latency](#request_latency)                                                     | Service Client | Histogram   | Core, Go, Java |
| [temporal_resource_slots_mem_usage](#resource_slots_cpu_usage)                                   | Worker         | Gauge       | Core, Java     |
| [temporal_resource_slots_cpu_usage](#resource_slots_mem_usage)                                   | Worker         | Gauge       | Core, Java     |
| [temporal_sticky_cache_hit](#sticky_cache_hit)                                                   | Worker         | Counter     | Core, Go, Java |
| [temporal_sticky_cache_miss](#sticky_cache_miss)                                                 | Worker         | Counter     | Core, Go, Java |
| [temporal_sticky_cache_size](#sticky_cache_size)                                                 | Worker         | Gauge       | Core, Go, Java |
| [temporal_sticky_cache_total_forced_eviction](#sticky_cache_total_forced_eviction)               | Worker         | Counter     | Go, Java       |
| [temporal_unregistered_activity_invocation](#unregistered_activity_invocation)                   | Worker         | Counter     | Go             |
| [temporal_worker_start](#worker_start)                                                           | Worker         | Counter     | Core, Go, Java |
| [temporal_worker_task_slots_available](#worker_task_slots_available)                             | Worker         | Gauge       | Core, Go, Java |
| [temporal_worker_task_slots_used](#worker_task_slots_used)                                       | Worker         | Gauge       | Core, Go, Java |
| [temporal_workflow_active_thread_count](#workflow_active_thread_count)                           | Worker         | Gauge       | Java           |
| [temporal_workflow_cancelled](#workflow_cancelled)                                               | Worker         | Counter     | Core, Go, Java |
| [temporal_workflow_completed](#workflow_completed)                                               | Worker         | Counter     | Core, Go, Java |
| [temporal_workflow_continue_as_new](#workflow_continue_as_new)                                   | Worker         | Counter     | Core, Go, Java |
| [temporal_workflow_endtoend_latency](#workflow_endtoend_latency)                                 | Worker         | Histogram   | Core, Go, Java |
| [temporal_workflow_failed](#workflow_failed)                                                     | Worker         | Counter     | Core, Go, Java |
| [temporal_workflow_task_execution_failed](#workflow_task_execution_failed)                       | Worker         | Counter     | Core, Go, Java |
| [temporal_workflow_task_execution_latency](#workflow_task_execution_latency)                     | Worker         | Histogram   | Core, Go, Java |
| [temporal_workflow_task_queue_poll_empty](#workflow_task_queue_poll_empty)                       | Worker         | Counter     | Core, Go, Java |
| [temporal_workflow_task_queue_poll_succeed](#workflow_task_queue_poll_succeed)                   | Worker         | Counter     | Core, Go, Java |
| [temporal_workflow_task_replay_latency](#workflow_task_replay_latency)                           | Worker         | Histogram   | Core, Go, Java |
| [temporal_workflow_task_schedule_to_start_latency](#workflow_task_schedule_to_start_latency)     | Worker         | Histogram   | Core, Go, Java |

### activity_execution_cancelled

An Activity Execution was canceled.

- Type: Counter
- Available in: Java
- Tags: `activity_type`, `namespace`, `task_queue`

### activity_execution_failed

An Activity Execution failed.
This does not include local Activity Failures in the Go and Java SDKs (see [local_activity_execution_failed](#local_activity_execution_failed)).

- Type: Counter
- Available in: Core, Go, Java
- Tags: `activity_type`, `namespace`, `task_queue`

### activity_execution_latency

Time to complete an Activity Execution, from the time the Activity Task is generated to the time the language SDK responded with a completion (failure or success).

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `activity_type`, `namespace`, `task_queue`

### activity_poll_no_task

An Activity Worker poll for an Activity Task timed out, and no Activity Task is available to pick from the Task Queue.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`

### activity_schedule_to_start_latency

The Schedule-To-Start time of an Activity Task in seconds.
A [Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout) can be set when an Activity Execution is spawned.
This metric is useful for ensuring Activity Tasks are being processed from the queue in a timely manner. Some SDKs may include
the `activity_type` label, but the metric should not vary by type, as it does not influence the rate at which tasks are pulled
from the queue.

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`

### activity_succeed_endtoend_latency

Total latency of successfully finished Activity Executions from the time they are scheduled to the time they are completed.
This metric is not recorded for async Activity completion.

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `activity_type`, `namespace`, `task_queue`

### activity_task_error

An internal error or panic occurred during Activity Task handling or execution.

- Type: Counter
- Available in: Go,
- Tags: `activity_type`, `namespace`, `task_queue`, `workflow_type`

### corrupted_signals

Number of Signals whose payload could not be deserialized.

- Type: Counter
- Available in: Go, Java
- Tags: `namespace`, `task_queue`, `workflow_type`

### local_activity_execution_cancelled

A Local Activity Execution was canceled.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `activity_type`, `namespace`, `task_queue`

### local_activity_execution_failed

A Local Activity Execution failed.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `activity_type`, `namespace`, `task_queue`

### local_activity_execution_latency

Time to complete a Local Activity Execution, from the time the first Activity Task is generated to the time the SDK responds that the execution is complete.

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `activity_type`, `namespace`, `task_queue`

### local_activity_succeeded_endtoend_latency

Total latency of successfully finished Local Activity Executions (from schedule to completion).

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `activity_type`, `namespace`, `task_queue`

### local_activity_total

Total number of [Local Activity Executions](/local-activity).

- Type: Counter
- Available in: Core, Go, Java
- Tags: `activity_type`, `namespace`, `task_queue`

### long_request

Temporal Client made an RPC long poll request.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `operation`

### long_request_failure

Temporal Client made an RPC long poll request that failed.
This number is included into the total `long_request` counter for long poll RPC requests.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `operation`

### long_request_latency

Latency of a Temporal Client gRPC long poll request.

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `namespace`, `operation`

### nexus_poll_no_task

A Nexus Worker poll for a Nexus Task timed out, and no Nexus Task is available to pick from the Task Queue.

- Type: Counter
- Available in: Go, Java
- Tags: `namespace`, `task_queue`

### nexus_task_schedule_to_start_latency

The Schedule-To-Start time of a Nexus Task in seconds. The schedule time is taken from when the corresponding request
hit the Frontend service to when the SDK started processing the task.

This time is limited by the `Request-Timeout` header given to the Frontend when handling this request.

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`

### nexus_task_execution_failed

Handling of a Nexus Task resulted in an error. This includes any error returned from a user handler and unexpected
internal errors in the SDK.

- Type: Counter
- Available in: Go, Java
- Tags: `namespace`, `task_queue`, `nexus_service`, `nexus_operation`, `failure_reason`

Valid values for the `failure_reason` tag:

- `internal_sdk_error`: There was an unexpected internal error within the SDK while handling the Nexus task. Indicates a
  bug in the SDK.
- `handler_error_{TYPE}`: The user handler code returned a predefined error, as specified in the [Nexus spec](https://github.com/nexus-rpc/api/blob/main/SPEC.md#predefined-handler-errors).
  If the handler returns an unexpected error, the TYPE is set to `INTERNAL`.
- `timeout`: The user handler code did not return within the request timeout.
- `operation_failed`: The user handler code has indicated that the operation has failed. In Go, this maps to an
  `UnsuccessfulOperationError` with a `failed` state.
- `operation_canceled`: The user handler code has indicated that the operation has completed as canceled. In Go, this maps
  to an `UnsuccessfulOperationError` with a `canceled` state.

### nexus_task_execution_latency

Time to complete a Nexus Task, from the time the Nexus Task processing starts in the SDK to the time the user handler
completes.

- Type: Histogram
- Available in: Go, Java
- Tags: `namespace`, `task_queue`, `nexus_service`, `nexus_operation`
