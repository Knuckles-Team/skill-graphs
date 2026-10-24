| initiated_event_id               | Id of the [RequestCancelExternalWorkflowExecutionInitiated](#requestcancelexternalworkflowexecutioninitiated) Event this failure [signal](/sending-messages#sending-signals) corresponds to. |

### UpsertWorkflowSearchAttributes

This [Event](/workflow-execution/event#event) type indicates that the Workflow [Search Attributes](/search-attribute) should be updated and synchronized with the visibility store.

| Field                            | Description                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------------ |
| workflow_task_completed_event_id | The [WorkflowTaskCompleted](#workflowtaskcompleted) Event reported the Event with this Id. |
| search_attributes                | Provides data for setting up a Workflow's [Search Attributes](/search-attribute).          |

### WorkflowExecutionUpdateAcceptedEvent

This [Event](/workflow-execution/event#event) type indicates that a [Workflow Execution](/workflow-execution) has accepted an [Update](/sending-messages#sending-updates) for execution.
The original request input payload is both indicated and stored by this Event, as it generates no Event when initially requesting an Update.

| Field                                | Description                                                                                                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| protocol_instance_id                 | The instance of the Update protocol with this Id is executing this Update.                                                                                             |
| accepted_request_message_id          | The Id of the request message sent by [Temporal Server](/temporal-service/temporal-server) to the [Worker](/workers#worker).                                           |
| accepted_request_sequencing_event_id | Execute this Update after the Event with this Id.                                                                                                                      |
| accepted_request                     | The request input and metadata initially provided by the invoker of the Update and subsequently relayed by Temporal Server to the Worker for acceptance and execution. |

### WorkflowExecutionUpdateCompletedEvent

This [Event](/workflow-execution/event#event) type indicates that a [Workflow Execution](/workflow-execution) has executed an [Update](/sending-messages#sending-updates) to completion.

| Field             | Description                                                                                                                                  |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| meta              | The metadata associated with this Update, sourced from the initial request.                                                                  |
| accepted_event_id | The Id of the [WorkflowExecutionUpdateAcceptedEvent](#workflowexecutionupdateacceptedevent) The Platform accepted this Update for execution. |
| outcome           | The outcome of execution of this Update whether the execution resulted in a success or a failure.                                            |

### NexusOperationScheduled

This Event type indicates that a Nexus Operation scheduled by a caller Workflow.
The caller's [Nexus Machinery](/glossary#nexus-machinery) will attempt to start the Nexus Operation.
This Event type contains Nexus Operation input and the Operation request ID.

| Field                            | Description                                                                                                                                                                                                                                                                                               |
| :------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| endpoint                         | Endpoint name, must exist in the endpoint registry.                                                                                                                                                                                                                                                       |
| service                          | Service name.                                                                                                                                                                                                                                                                                             |
| operation                        | Operation name.                                                                                                                                                                                                                                                                                           |
| input                            | Input for the operation. The server converts this into Nexus request content and the appropriate content headers internally when sending the StartOperation request. On the handler side, if it is also backed by Temporal, the content is transformed back to the original Payload stored in this event. |
| schedule_to_close_timeout        | Schedule-to-close timeout for this operation. Indicates how long the caller is willing to wait for operation completion. Calls are retried internally by the server.                                                                                                                                      |
| nexus_header                     | Header to attach to the Nexus request. Note these headers are not the same as Temporal headers on internal activities and child Workflows, these are transmitted to Nexus operations that may be external and are not traditional payloads.                                                               |
| workflow_task_completed_event_id | The ID of the [WorkflowTaskCompleted](#workflowtaskcompleted) event that the corresponding ScheduleNexusOperation command was reported with.                                                                                                                                                              |
| request_id                       | A unique ID generated by the History Service upon creation of this event. The ID will be transmitted with all Nexus StartOperation requests and is used as an idempotency key.                                                                                                                            |
| endpoint_id                      | Endpoint ID as resolved in the endpoint registry at the time this event was generated. This is stored on the event and used internally by the server in case the endpoint is renamed from the time the event was originally scheduled.                                                                    |

### NexusOperationStarted

This Event type indicates that a Nexus Operation Execution was started.
This Event is added to the caller's Event History for Asynchronous Nexus Operations, for example those that are backed by a Workflow.
The Event is not added to the caller's Event History for Synchronous Nexus Operations, since they transition directly to [NexusOperationCompleted](#nexusoperationcompleted) or another final state such as [NexusOperationFailed](#nexusoperationfailed) when the response is provided synchronously by the Nexus handler.

| Field              | Description                                                                                                                                       |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| scheduled_event_id | The ID of the [NexusOperationScheduled](#nexusoperationscheduled) event this task corresponds to.                                                 |
| operation_token    | The operation token returned by the Nexus handler in the response to the StartOperation request. This token is used when canceling the operation. |
| request_id         | The request ID allocated at schedule time.                                                                                                        |

### NexusOperationCompleted

This Event type indicates that a Nexus Operation has completed successfully.
The caller's Event History records the result of a successful Nexus Operation with this event for synchronous and asynchronous Nexus Operations.
This Event type contains Nexus Operation results.

| Field              | Description                                                                                                                                                          |
| :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scheduled_event_id | The ID of the [NexusOperationScheduled](#nexusoperationscheduled) event. Uniquely identifies this operation.                                                         |
| result             | Serialized result of the Nexus operation. The response of the Nexus handler. Delivered either via a completion callback or as a response to a synchronous operation. |
| request_id         | The request ID allocated at schedule time.                                                                                                                           |

### NexusOperationFailed

This Event type indicates that a Nexus Operation has failed.
The caller's Event History records a failed Nexus Operation with this event both for synchronous and asynchronous Nexus Operations.
For example, when a Nexus Handler responds synchronously with a non-retryable error or when a Workflow that backs an Operation fails, resulting in a [WorkflowExecutionFailed](#workflowexecutionfailed) Event.
When an SDK client picks up a Nexus Operation, the Nexus handler asynchronously starts an underlying Workflow, which subsequently results in [WorkflowExecutionFailed](#workflowexecutionfailed).
This Event type contains a Nexus Operation failure.

| Field              | Description                                                                                                   |
| :----------------- | :------------------------------------------------------------------------------------------------------------ |
| scheduled_event_id | The ID of the [NexusOperationScheduled](#nexusoperationscheduled)` event. Uniquely identifies this operation. |
| failure            | Failure details. A NexusOperationFailureInfo wrapping an ApplicationFailureInfo.                              |
| request_id         | The request ID allocated at schedule time.                                                                    |

### NexusOperationTimedOut

This Event type indicates that a Nexus Operation has timed out according to the Temporal Server, due to one of these Nexus Operation timeouts: Schedule-to-Close Timeout.
| Field | Description |
| :---- | :---- |
| scheduled_event_id | The ID of the [NexusOperationScheduled](#nexusoperationscheduled)` event. Uniquely identifies this operation. |
| failure | Failure details. A NexusOperationFailureInfo wrapping a CanceledFailureInfo. |
| request_id | The request ID allocated at schedule time. |

### NexusOperationCancelRequested

This Event type indicates that the Workflow that scheduled a Nexus Operation requested to cancel it.
| Field | Description |
| :---- | :---- |
| scheduled_event_id | The id of the [NexusOperationScheduled](#nexusoperationscheduled)` event this cancel request corresponds to. |
| workflow_task_completed_event_id | The [WorkflowTaskCompleted](#workflowtaskcompleted) event that the corresponding RequestCancelNexusOperation command was reported with. |

### NexusOperationCanceled

This Event type indicates that a Nexus Operation has resolved as canceled.
| Field | Description |
| :---- | :---- |
| scheduled_event_id | The ID of the [NexusOperationScheduled](#nexusoperationscheduled)` event. Uniquely identifies this operation. |
| failure | Cancellation details. |
| request_id | The request ID allocated at schedule time. |

---

## Temporal Failures reference

A Failure is Temporal's representation of various types of errors that occur in the system.

There are different types of Failures, and each has a different type in the SDKs and different information in the protobuf messages (which are used to communicate with the Temporal Service and appear in [Event History](/workflow-execution/event#event-history)).

## Temporal Failure

Most SDKs have a base class that the other Failures extend:

- TypeScript: [TemporalFailure](https://typescript.temporal.io/api/classes/common.TemporalFailure)
- Java: [TemporalFailure](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/TemporalFailure.html)
- Python: [FailureError](https://python.temporal.io/temporalio.exceptions.FailureError.html)
- PHP: [TemporalFailure](https://php.temporal.io/classes/Temporal-Exception-Failure-TemporalFailure.html)

The base [Failure proto message](https://api-docs.temporal.io/#temporal.api.failure.v1.Failure) has these fields:

- `string message`
- `string stack_trace`
- `string source`: The SDK this Failure originated in (for example, `"TypeScriptSDK"`). In some SDKs, this field is used to rehydrate the call stack into an exception object.
- `Failure cause`: The `Failure` message of the cause of this Failure (if applicable).
- `Payload encoded_attributes`: Contains the encoded `message` and `stack_trace` fields when using a [Failure Converter](/failure-converter).

## Application Failure

Workflow, and Activity, and Nexus Operation code use Application Failures to communicate application-specific failures that happen.
This is the only type of Temporal Failure created and thrown by user code.

- TypeScript: [ApplicationFailure](https://typescript.temporal.io/api/classes/common.ApplicationFailure)
- Java: [ApplicationFailure](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/ApplicationFailure.html)
- Go: [ApplicationError](https://pkg.go.dev/go.temporal.io/sdk/temporal#ApplicationError)
- Python: [ApplicationError](https://python.temporal.io/temporalio.exceptions.ApplicationError.html)
- PHP: [ApplicationFailure](https://php.temporal.io/classes/Temporal-Exception-Failure-ApplicationFailure.html)
- Proto: [ApplicationFailureInfo](https://api-docs.temporal.io/#temporal.api.failure.v1.ApplicationFailureInfo) and [Failure](https://api-docs.temporal.io/#temporal.api.failure.v1.Failure)

### Errors in Workflows

An error in a Workflow can cause either a **Workflow Task Failure** (the Task will be retried) or a **Workflow Execution Failure** (the Workflow is marked as failed).

Only Workflow exceptions that are Temporal Failures cause the Workflow Execution to fail; all other exceptions cause the Workflow Task to fail and be retried (in Go, any error returned from the Workflow fails the Workflow Execution, and a panic fails the Workflow Task).
Most types of Temporal Failures are raised by the Temporal Service, like a [Cancelled Failure](#cancelled-failure) when the Workflow is Cancelled or an [Activity Failure](#activity-failure) when an Activity fails.
In contrast, you can explicitly fail the Workflow Execution by throwing an Application Failure (returning any error in Go) in Workflow Definition code.

#### Workflow Task Failures

A **Workflow Task Failure** is an unexpected situation failing to process a Workflow Task.
This could be triggered by a non-Temporal exception being raised (panicking in Go) in your Workflow code.
Any exception that does not extend Temporal's `FailureError` exception is considered a Workflow Task Failure.
These types of failures will cause the Workflow Task to be retried until the
Workflow Execution Timeout, which is unlimited by default.

#### Workflow Execution Failures

An `ApplicationError`, an extension of `FailureError`, can be raised in a Workflow to fail the Workflow Execution.
Workflow Execution Failures put the Workflow Execution into the "Failed" state and no more attempts will be made in progressing this execution.
If you are creating custom exceptions you would need to extend the [`ApplicationError`](https://docs.temporal.io/references/failures#application-failure) class—a child class of [`FailureError`](https://docs.temporal.io/references/failures#temporal-failure).

### Errors in Activities

In Activities, you can either throw an Application Failure or another Error to fail the Activity Task.
In the latter case, the error is converted to an Application Failure.
During conversion, the following Application Failure fields are set:

- `type` is set to the error's type name.
- `message` is set to the error message.
- `non_retryable` is set to false.
- `details` are left unset.
- `cause` is a Failure converted from the error's `cause` property.
- `next_retry_delay` is left unset.
- call stack is copied.

When an [Activity Execution](/activity-execution) fails, the Application Failure from the last Activity Task is the `cause` field of the [ActivityFailure](#activity-failure).
This ActivityFailure is thrown by the Workflow's call to the Activity, and it can be handled in the Workflow Definition.

### Errors in Nexus Operations

Nexus Operations can end up in completed, failed, canceled, and timed out states.

Under the hood, the Nexus Operation machinery breaks up the lifecycle of an Operation into one or more StartOperation requests and completion callbacks, and automatically retries these requests as long they fail with retryable errors.

The Workflow-specified schedule-to-close timeout is enforced by the caller's machinery and is the only way for an Operation to transition to the timed out state.

Operations can end up in the other three states either when the operation handler returns a synchronous response or error, or when an asynchronous Operation (for example, one backed by a workflow) eventually reaches a terminal state.

A Nexus Operation handler can return either retryable or non-retryable errors to indicate to the caller's Nexus machinery whether to retry a given request.
Requests that time out before a response is sent to the caller are automatically retried.

By default, errors are considered retryable, unless specified below:

- Non retryable Application Failures
- Unsuccessful Operation errors that can resolve an operation as either failed or canceled
- [Handler errors](https://github.com/nexus-rpc/api/blob/main/SPEC.md#predefined-handler-errors) with the following types: `BAD_REQUEST`, `UNAUTHENTICATED`, `UNAUTHORIZED`, `NOT_FOUND`, and `RESOURCE_EXHAUSTED`

#### Nexus Operation Task Failures

A Nexus Operation Task Failure is an unexpected situation failing to process a Nexus Operation Task in a handler.
This could be triggered by throwing an unknown error in your Nexus handler code.
These types of failures will cause the Nexus Operation Task to be retried.

#### Nexus Operation Execution Failures

A non-retryable Application Failure can be thrown by a Nexus Operation handler to fail the overall Nexus Operation Execution.
Nexus Operation Execution Failures put the Nexus Operation Execution into the "Failed" state and no more attempts will be made to complete the Nexus Operation.

#### Propagation of Workflow errors

Application Errors thrown from a Workflow created by a Nexus NewWorkflowRunOperation handler will be automatically propagated to the caller as a non-retryable error and result in a Nexus Operation Execution Failure.

#### Using Failures in a Nexus handler

In a Nexus Operation handler, you can throw an Application Failure, a Nexus Error or another Error to fail the individual Nexus Operation Task or fail the overall Nexus Operation Execution.

Unknown errors are converted to a retryable Application Failure. During conversion, the following fields are set on the Application Failure:

- `non_retryable` is set to false.
- `type` is set to the error's type name.
- `message` is set to the error message.

#### Retryable failures

Retryable Nexus Operation Task failures, such as an unknown error, are automatically retried with a built-in Retry Policy.
When a Nexus Task fails, the caller Workflow records an event attempt failure on the pending Nexus Operation and sets the following fields:

- `state` is set to the new state, for example BackingOff.
- `attempt` is set to an incremented count.
- `next_attempt_schedule_time` is set when the Nexus Task will be retried.
- `last_attempt_failure` is set with the following fields:
  - `message` is set to the error message.
  - `failure_info` is set to the Application Failure.

For example, an unknown error thrown in a Nexus handler will surface as:

```
temporal workflow describe -w my-workflow-id
...
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
  LastAttemptFailure       {"message":"unexpected response status: "500 Internal Server Error": internal error","applicationFailureInfo":{}}
```

### Non-retryable

When an Activity or Workflow throws an Application Failure, the Failure's `type` field is matched against a Retry Policy's list of [non-retryable errors](/encyclopedia/retry-policies#non-retryable-errors) to determine whether to retry the Activity or Workflow.
Activities and Workflow can also avoid retrying by setting an Application Failure's `non_retryable` flag to `true`.

When a Nexus Operation handler throws an Application Failure, it is retried by default using a built-in Retry Policy that cannot be customized.
Nexus Operation handlers can avoid retrying by setting an Application Failure's `non_retryable` flag to true.
When a non-retryable error is returned from a Nexus handler, the overall Nexus Operation Execution is failed and the error is returned to the caller’s Workflow Execution as a Nexus Operation Failure.

### Setting the Next Retry Delay {/* #activity-next-retry-delay */}

By setting the Next Retry Delay for a given Application Failure, you can tell the server to wait that amount of time before trying the Activity or Workflow again.
This will override whatever the Retry Policy would have computed for your specific exception.

Java: [NextRetryDelay](/develop/java/activities/timeouts#activity-next-retry-delay)
TypeScript: [nextRetryDelay](/develop/typescript/activities/timeouts#activity-next-retry-delay)
PHP: [NextRetryDelay](/develop/php/activities/timeouts#activity-next-retry-delay)

### Nexus errors {/* #nexus-errors */}

#### Default mapping

By default, Application Failures thrown from a Nexus Operation handler will be mapped to the following underlying Nexus Failures, based on what `non_retryable` is set to:

| `non_retryable` | Nexus error                | HTTP status code          |
| :-------------- | :------------------------- | :------------------------ |
| false (default) | HandlerErrorTypeInternal   | 500 Internal Server Error |
| true            | UnsuccessfulOperationError | 424 Failed Dependency     |

#### Use Nexus Errors directly

For improved semantics and mapping to HTTP status codes for external Nexus callers (when supported), we recommend that Nexus Operation handlers throw a Nexus Error directly, which includes the list below with associated retry semantics.

For example the Nexus Go SDK provides

- `nexus.HandlerError(nexus.HandlerErrorType, msg)`
- `nexus.UnsuccessfulOperationError{state, failure}`

#### Retryable Nexus errors

| Nexus error type                  | `non_retryable` |
| :-------------------------------- | :-------------- |
| HandlerErrorTypeResourceExhausted | false           |
| HandlerErrorTypeInternal          | false           |
| HandlerErrorTypeNotImplemented    | false           |
| HandlerErrorTypeUnavailable       | false           |

#### Non-retryable Nexus errors

| Nexus error type                | `non_retryable` |
| :------------------------------ | :-------------- |
| HandlerErrorTypeBadRequest      | true            |
| HandlerErrorTypeUnauthenticated | true            |
| HandlerErrorTypeUnauthorized    | true            |
| HandlerErrorTypeNotFound        | true            |
| UnsuccessfulOperationError      | true            |

## Cancelled Failure

When [Cancellation](/activity-execution#cancellation) of a Workflow, Activity or Nexus Operation is requested, SDKs represent the cancellation to the user in language-specific ways.
For example, in TypeScript, in some cases a Cancelled Failure is thrown directly by a Workflow API function, and in other cases the Cancelled Failure is wrapped in a different Failure.
