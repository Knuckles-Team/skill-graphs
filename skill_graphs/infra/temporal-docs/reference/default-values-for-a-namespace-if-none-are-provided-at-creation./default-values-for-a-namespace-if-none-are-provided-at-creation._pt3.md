| workflow_execution_expiration_time | The absolute time at which the Workflow Execution will [time out](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout).                       |
| cron_schedule                      | Displays the Workflow's [Cron Schedule](/cron-job), if applicable.                                                                                             |
| first_workflow_task_backoff        | Contains the amount of time between when this iteration of the Workflow was scheduled, and when it should run next. Applies to Cron Scheduling.                |
| memo                               | Non-indexed information to show in the Workflow.                                                                                                               |
| search_attributes                  | Provides data for setting up a Workflow's [Search Attributes](/search-attribute).                                                                              |
| prev_auto_reset_points             |                                                                                                                                                                |
| header                             | Information passed by the sender of the [Signal](/sending-messages#sending-signals) that is copied into the [Workflow Task](/tasks#workflow-task).             |
| completion_callbacks               | Completion callbacks attached when this workflow was started.                                                                                                  |

### WorkflowExecutionCompleted

This indicates that the [Workflow Execution](/workflow-execution) has successfully completed. The [Event](/workflow-execution/event#event) contains Workflow Execution results.

| Field                            | Description                                                                                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| result                           | Serialized result of completed [Workflow](/workflows).                                                                                       |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with.                                              |
| new_execution_run_id             | The [Run Id](/workflow-execution/workflowid-runid#run-id) of the new Workflow Execution started as a result of a [Cron Schedule](/cron-job). |

### WorkflowExecutionFailed

This [Event](/workflow-execution/event#event) indicates that the [Workflow Execution](/workflow-execution) has unsuccessfully completed and contains the Workflow Execution error.

| Field                            | Description                                                                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| failure                          | Serialized result of a [Workflow](/workflows) failure.                                                                                             |
| retry_state                      | The reason provided for whether the [Task](/tasks#task) should or shouldn't be retried.                                                            |
| workflow_task_completed_event_id | The [Run Id](/workflow-execution/workflowid-runid#run-id) of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with. |
| new_execution_run_id             | The [Run Id](/workflow-execution/workflowid-runid#run-id) of the new Workflow started by Cron or [Retry](/encyclopedia/retry-policies).            |

### WorkflowExecutionTimedOut

This [Event](/workflow-execution/event#event) type indicates that the [Workflow Execution](/workflow-execution) has timed out by the [Temporal Server](/temporal-service/temporal-server) due to the [Workflow](/workflows) having not been completed within [timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout) settings.

| Field                | Description                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| retry_state          | The reason provided for whether the [Task](/tasks#task) should or shouldn't be retried.                                                 |
| new_execution_run_id | The [Run Id](/workflow-execution/workflowid-runid#run-id) of the new Workflow started by Cron or [Retry](/encyclopedia/retry-policies). |

### WorkflowExecutionCancelRequested

This [Event](/workflow-execution/event#event) type indicates that a request has been made to cancel the [Workflow Execution](/workflow-execution).

| Field                       | Description                                                                                                                                     |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| cause                       | The user-provided reason for the cancelation request.                                                                                           |
| external_initiated_event_id | The [Run Id](/workflow-execution/workflowid-runid#run-id) of the Event in the [Workflow](/workflows) that requested cancelation, if applicable. |
| external_workflow_execution | Identifies the external Workflow and the run of the its execution.                                                                              |
| identity                    | Id of the [Worker](/workers#worker) that requested cancelation.                                                                                 |

### WorkflowExecutionCanceled

This [Event](/workflow-execution/event#event) type indicates that the client has confirmed the cancelation request and the [Workflow Execution](/workflow-execution) has been canceled.

| Field                            | Description                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with. |
| details                          | Additional information reported by the [Workflow](/workflows) upon cancelation.                 |

### WorkflowExecutionSignaled

This [Event](/workflow-execution/event#event) type indicates the [Workflow](/workflows) has received a [Signal](/sending-messages#sending-signals) Event.
The Event type contains the Signal name and a Signal payload.

| Field       | Description                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------- |
| signal_name | The name/type of Signal to be fired.                                                                          |
| input       | Information that is deserialized by the SDK to provide arguments to the Workflow function.                    |
| identity    | Identifies the [Worker](/workers#worker) that signaled to the Workflow.                                       |
| header      | Information passed by the sender of the Signal that is copied into the [Workflow Task](/tasks#workflow-task). |

### WorkflowExecutionTerminated

This [Event](/workflow-execution/event#event) type indicates that the [Workflow Execution](/workflow-execution) has been forcefully terminated and that likely the terminate Workflow API was called.

| Field    | Description                                                          |
| -------- | -------------------------------------------------------------------- |
| reason   | Information provided by the user or client for Workflow termination. |
| details  | Additional information reported by the Workflow upon termination.    |
| identity | Identifies the Worker that requested termination.                    |

### WorkflowExecutionContinuedAsNew

This [Event](/workflow-execution/event#event) type indicates that the Workflow has successfully completed, and a new Workflow has been started within the same transaction.
This Event type contains last [Workflow Execution](/workflow-execution) results as well as new Workflow Execution inputs.

| Field                            | Description                                                                                                          |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| new_execution_run_id             | The [Run Id](/workflow-execution/workflowid-runid#run-id) of the new Workflow started by this Continue-As-New Event. |
| workflow_type                    | The name/type of Workflow that was started by this Event.                                                            |
| task_queue                       | The [Task Queue](/task-queue) that this [Workflow Task](/tasks#workflow-task) was enqueued in.                       |
| input                            | Information that is deserialized by the SDK to provide arguments to the Workflow.                                    |
| workflow_run_timeout             | Timeout of a single Workflow run.                                                                                    |
| workflow_task_timeout            | Timeout of a single Workflow Task.                                                                                   |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event command was reported with.              |
| backoff_start_interval           | The amount of time to delay the beginning of the [ContinuedAsNew](#workflowexecutioncontinuedasnew) Workflow.        |
| initiator                        | Allows the Workflow to continue as a new execution.                                                                  |
| last_completion_result           | Information passed by the previously completed Task to the ongoing execution.                                        |
| header                           | Information passed by the sender of the Signal that is copied into the Workflow Task.                                |
| memo                             | Non-indexed information to show in the Workflow.                                                                     |
| search_attributes                | Provides data for setting up a Workflow's [Search Attributes](/search-attribute).                                    |

### WorkflowExecutionOptionsUpdated

This [Event](/workflow-execution/event#event) type indicates that the Workflow options have been updated.
The Event type contains updated options such as a versioning override or attached completion callbacks.

| Field                         | Description                                                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| versioning_override           | Versioning override upserted in this event. Ignored if nil or if unset_versioning_override is true.                    |
| unset_versioning_override     | Versioning override removed in this event.                                                                             |
| attached_request_id           | Request ID attached to the running workflow execution so subsequent requests with the same request ID will be deduped. |
| attached_completion_callbacks | Completion callbacks attached to the running workflow execution.                                                       |

### WorkflowTaskScheduled

This [Event](/workflow-execution/event#event) type indicates that the [Workflow Task](/tasks#workflow-task) has been scheduled.
The SDK client should now be able to process any new history events.

| Field                  | Description                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| task_queue             | The [Task Queue](/task-queue) that this Workflow Task was enqueued in.                     |
| start_to_close_timeout | The time that the [Worker](/workers#worker) takes to process this Task once it's received. |
| attempt                | The number of attempts that have been made to complete this Task.                          |

### WorkflowTaskStarted

This [Event](/workflow-execution/event#event) type indicates that the [Workflow Task](/tasks#workflow-task) has started.
The SDK client has picked up the Workflow Task and is processing new history events.

| Field              | Description                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| scheduled_event_id | The Id of the [WorkflowTaskScheduled](#workflowtaskscheduled) Event that this Workflow Task corresponds to. |
| identity           | Identifies the [Worker](/workers#worker) that started this Task.                                            |
| request_id         | Identifies the Workflow Task request.                                                                       |

### WorkflowTaskCompleted

This [Event](/workflow-execution/event#event) type indicates that the [Workflow Task](/tasks#workflow-task) completed.

| Field              | Description                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| scheduled_event_id | The Id of the [WorkflowTaskScheduled](#workflowtaskscheduled) Event that this Workflow Task corresponds to. |
| started_event_id   | The Id of the [WorkflowTaskStarted](#workflowtaskstarted) Event that this Task corresponds to.              |
| identity           | Identity of the [Worker](/workers#worker) that completed this Task.                                         |
| binary_checksum    | Binary Id of the Worker that completed this Task.                                                           |

The SDK client picked up the Workflow Task, processed new history events, and may or may not ask the [Temporal Server](/temporal-service/temporal-server) to do additional work.
It is possible for the following events to still occur:

- [ActivityTaskScheduled](#activitytaskscheduled)
- [TimerStarted](#timerstarted)
- [UpsertWorkflowSearchAttributes](#upsertworkflowsearchattributes)
- [MarkerRecorded](#markerrecorded)
- [StartChildWorkflowExecutionInitiated](#startchildworkflowexecutioninitiated)
- [RequestCancelExternalWorkflowExecutionInitiated](#requestcancelexternalworkflowexecutioninitiated)
- [SignalExternalWorkflowExecutionInitiated](#signalexternalworkflowexecutioninitiated)
- [WorkflowExecutionCompleted](#workflowexecutioncompleted)
- [WorkflowExecutionFailed](#workflowexecutionfailed)
- [WorkflowExecutionCanceled](#workflowexecutioncanceled)
- [WorkflowExecutionContinuedAsNew](#workflowexecutioncontinuedasnew)

### WorkflowTaskTimedOut

This [Event](/workflow-execution/event#event) type indicates that the [Workflow Task](/tasks#workflow-task) encountered a [timeout](/encyclopedia/detecting-workflow-failures#workflow-task-timeout).
Either an SDK client with a local cache was not available at the time, or it took too long for the SDK client to process the Task.

| Field              | Description                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| scheduled_event_id | The Id of the [WorkflowTaskScheduled](#workflowtaskscheduled) Event that this Workflow Task corresponds to. |
| started_event_id   | The Id of the [WorkflowTaskStarted](#workflowtaskstarted) Event that this Task corresponds to.              |
| timeout_type       | The type of timeout that has occurred.                                                                      |

### WorkflowTaskFailed

This [Event](/workflow-execution/event#event) type indicates that the [Workflow Task](/tasks#workflow-task) encountered a failure.
Usually this means that the Workflow was non-deterministic.
However, the Workflow reset functionality also uses this Event.

| Field              | Description                                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| scheduled_event_id | The Id of the [WorkflowTaskScheduled](#workflowtaskscheduled) Event that this Workflow Task corresponds to.                                  |
| started_event_id   | The Id of the [WorkflowTaskStarted](#workflowtaskstarted) Event that this Workflow Task corresponds to.                                      |
| failure            | Details for the Workflow Task's failure.                                                                                                     |
| identity           | The identity of the [Worker](/workers#worker) that failed this Task. The Worker must be explicitly defined to return a value for this field. |
| base_run_id        | The original [Run Id](/workflow-execution/workflowid-runid#run-id) of the Workflow.                                                          |
| new_run_id         | The Run Id of the reset Workflow.                                                                                                            |
| fork_event_version | Identifies the Event version that was forked off to the reset Workflow.                                                                      |
| binary_checksum    | The Binary Id of the Worker that failed this Task. The Worker must be explicitly defined to return a value for this field.                   |

### ActivityTaskScheduled

This [Event](/workflow-execution/event#event) type indicates that an [Activity Task](/tasks#activity-task) was scheduled.
The SDK client should pick up this Activity Task and execute.
This Event type contains Activity inputs, as well as Activity Timeout configurations.

| Field                            | Description                                                                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| activity_id                      | The identifier assigned to this Activity by a [Worker](/workers#worker) or user.                                                                   |
| activity_type                    | The [type of Activity](/activity-definition#activity-type) that was scheduled.                                                                     |
| namespace                        | Namespace of the Workflow that the [Activity](/activities) resides in.                                                                             |
| task_queue                       | The [Task Queue](/task-queue) that this Activity Task was enqueued in.                                                                             |
| header                           | Information passed by the sender of the [Signal](/sending-messages#sending-signals) that is copied into the [Workflow Task](/tasks#workflow-task). |
| input                            | Information that is deserialized by the SDK to provide arguments to the [Workflow](/workflows) function.                                           |
| schedule_to_close_timeout        | The amount of time that a caller will wait for Activity completion. Limits the amount of time that retries will be attempted for this Activity.    |
| schedule_to_start_timeout        | Limits the time that an Activity Task can stay in a Task Queue. This timeout cannot be retried.                                                    |
| start_to_close_timeout           | Maximum amount of execution time that an Activity is allowed after being picked up by a Worker. This timeout is retryable.                         |
| heartbeat_timeout                | Maximum amount of time allowed between successful Worker heartbeats.                                                                               |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with.                                                    |
| retry_policy                     | The amount of retries as determined by the service's dynamic configuration. Retries will happen until `schedule_to_close_timeout` is reached.      |

### ActivityTaskStarted

This [Event](/workflow-execution/event#event) type indicates that an [Activity Task Execution](/tasks#activity-task-execution) was started. The SDK Worker picked up the Activity Task and started processing the [Activity](/activities) invocation. `ActivityTaskStarted` is generated by the server when the Task is dispatched to the Worker, not when the Worker starts executing the Task.

Note, however, that this Event is not written to History until the terminal Event (like [ActivityTaskCompleted](#activitytaskcompleted) or [ActivityTaskFailed](#activitytaskfailed)) occurs.

| Field              | Description                                                                                                          |
| ------------------ | -------------------------------------------------------------------------------------------------------------------- |
| scheduled_event_id | The Id of the [ActivityTaskScheduled](#activitytaskscheduled) Event that this Task corresponds to.                   |
| identity           | Identifies the [Worker](/workers#worker) that started the Task.                                                      |
| request_id         | Identifies the Activity Task request.                                                                                |
| attempt            | The number of attempts that have been made to complete this Task.                                                    |
| last_failure       | Details from the most recent failure Event. Only assigned values if the Task has previously failed and been retried. |

### ActivityTaskCompleted

This [Event](/workflow-execution/event#event) type indicates that the [Activity Task](/tasks#activity-task) has completed.
The SDK client has picked up and successfully completed the Activity Task.
This Event type contains [Activity Execution](/activity-execution) results.

| Field              | Description                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------- |
| result             | Serialized result of a completed [Activity](/activities).                                                      |
| scheduled_event_id | The Id of the [ActivityTaskScheduled](#activitytaskscheduled) Event that this completion Event corresponds to. |
| started_event_id   | The Id of the [ActivityTaskStarted](#activitytaskstarted) Event that this Task corresponds to.                 |
| identity           | Identity of the [Worker](/workers#worker) that completed this Task.                                            |

### ActivityTaskFailed

This [Event](/workflow-execution/event#event) type indicates that the [Activity Task](/tasks#activity-task) has failed.
The SDK client picked up the Activity Task but unsuccessfully completed it.
This Event type contains [Activity Execution](/activity-execution) errors.

| Field              | Description                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| failure            | Serialized result of a [Workflow](/workflows) failure.                                                      |
| scheduled_event_id | The Id of the [ActivityTaskScheduled](#activitytaskscheduled) Event that this failure Event corresponds to. |
