| started_event_id   | The Id of the [ActivityTaskStarted](#activitytaskstarted) Event that this failure corresponds to.           |
| retry_state        | The reason provided for whether the Task should or shouldn't be retried.                                    |

### ActivityTaskTimedOut

This [Event](/workflow-execution/event#event) type indicates that the Activity has timed out according to the [Temporal Server](/temporal-service/temporal-server), due to one of these [Activity](/activities) timeouts: [Schedule-to-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout) and [Schedule-to-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout).

| Field              | Description                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| failure            | Serialized result of a [Workflow](/workflows) failure.                                                      |
| scheduled_event_id | The Id of the [ActivityTaskScheduled](#activitytaskscheduled) Event that this timeout Event corresponds to. |
| started_event_id   | The Id of the [ActivityTaskStarted](#activitytaskstarted) Event that this timeout corresponds to.           |
| retry_state        | The reason provided for whether the Task should or shouldn't be retried.                                    |
| timeout_type       | The type of timeout that led to this Event, e.g., Start-to-Close, Schedule-to-Close, Schedule-to-Start.     |

You can run a Workflow containing an Activity Execution that takes longer than the Start-to-Close Timeout you set and use a RetryPolicy that sets MaxAttempts to 1 so it does not retry indefinitely.
When the Activity times out, you will observe that the `ActivityTaskTimedOut` Event contains other attributes missing from the documentation, including the type of timeout that led to the Event.

### ActivityTaskCancelRequested

This [Event](/workflow-execution/event#event) type indicates that a request to [cancel](/activity-execution#cancellation) the [Activity](/activities) has occurred.

| Field                            | Description                                                                                                |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| scheduled_event_id               | The Id of the [ActivityTaskScheduled](#activitytaskscheduled) Event that this cancel Event corresponds to. |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with.            |

### ActivityTaskCanceled

This [Event](/workflow-execution/event#event) type indicates that the [Activity](/activities) has been [canceled](/activity-execution#cancellation).

| Field                            | Description                                                                                                                |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| details                          | Additional information reported by the Activity upon confirming cancelation.                                               |
| latest_cancel_requested_event_id | Id of the most recent [ActivityTaskCancelRequested](#activitytaskcancelrequested) Event which refers to the same Activity. |
| scheduled_event_id               | The Id of the [ActivityTaskScheduled](#activitytaskscheduled) Event that this cancelation corresponds to.                  |
| started_event_id                 | The Id of the [ActivityTaskStarted](#activitytaskstarted) Event that this cancelation corresponds to.                      |
| identity                         | Identifies the [Worker](/workers#worker) that requested cancelation.                                                       |

### TimerStarted

This [Event](/workflow-execution/event#event) type indicates a timer has started.

| Field                            | Description                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| timer_id                         | The Id assigned for the timer by a [Worker](/workers#worker) or user.                           |
| start_to_fire_timeout            | Amount of time to elapse before the timer fires.                                                |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with. |

### TimerFired

This [Event](/workflow-execution/event#event) type indicates a timer has fired.

| Field            | Description                                                           |
| ---------------- | --------------------------------------------------------------------- |
| timer_id         | The Id assigned for the timer by a [Worker](/workers#worker) or user. |
| started_event_id | The Id of the [TimerStarted](#timerstarted) Event itself.             |

### TimerCanceled

This [Event](/workflow-execution/event#event) type indicates a Timer has been canceled.

| Field                            | Description                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| timer_id                         | The Id assigned for the timer by a [Worker](/workers#worker) or user.                           |
| started_event_id                 | The Id of the [TimerStarted](#timerstarted) Event itself.                                       |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with. |

### RequestCancelExternalWorkflowExecutionInitiated

This [Event](/workflow-execution/event#event) type indicates that a [Workflow](/workflows) has requested that the [Temporal Server](/temporal-service/temporal-server) try to cancel another Workflow.

| Field                            | Description                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with. |
| namespace                        | [Namespace](/namespaces) of the Workflow that`s going to be signaled for execution.             |
| workflow_execution               | Identifies the Workflow and the run of the [Workflow Execution](/workflow-execution).           |
| child_workflow_only              | Set to true if this Workflow is a child of the Workflow which issued the cancelation request.   |
| reason                           | Information provided by the user or client for Workflow cancelation.                            |

### RequestCancelExternalWorkflowExecutionFailed

This [Event](/workflow-execution/event#event) type indicates that [Temporal Server](/temporal-service/temporal-server) could not cancel the targeted [Workflow](/workflows).
This is usually because the target Workflow could not be found.

| Field                            | Description                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with. |
| namespace                        | [Namespace](/namespaces) of the Workflow that failed to cancel.                                 |
| workflow_execution               | Identifies the Workflow and the run of the [Workflow Execution](/workflow-execution).           |
| initiated_event_id               | Id of the [RequestCancelExternalWorkflowExecutionInitiated] Event this failure corresponds to.  |

### ExternalWorkflowExecutionCancelRequested

This [Event](/workflow-execution/event#event) type indicates that the [Temporal Server](/temporal-service/temporal-server) has successfully requested the cancelation of the target [Workflow](/workflows).

| Field              | Description                                                                                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| initiated_event_id | Id of the [RequestCancelExternalWorkflowExecutionInitiated](#requestcancelexternalworkflowexecutioninitiated) Event that this cancelation request corresponds to. |
| namespace          | [Namespace](/namespaces) of the Workflow that was requested to cancel.                                                                                            |
| workflow_execution | Identifies the Workflow and the run of the [Workflow Execution](/workflow-execution).                                                                             |

### ExternalWorkflowExecutionSignaled

This [Event](/workflow-execution/event#event) type indicates that the [Temporal Server](/temporal-service/temporal-server) has successfully [Signaled](/sending-messages#sending-signals) the targeted [Workflow](/workflows).

| Field              | Description                                                                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| initiated_event_id | Id of the [SignalExternalWorkflowExecutionInitiated](#signalexternalworkflowexecutioninitiated) Event this Event corresponds to. |
| namespace          | [Namespace](/namespaces) of the Workflow that was signaled to.                                                                   |
| workflow_execution | Identifies the Workflow and the run of the [Workflow Execution](/workflow-execution).                                            |

### MarkerRecorded

This [Event](/workflow-execution/event#event) type is transparent to the [Temporal Server](/temporal-service/temporal-server).
The Server will only store it and will not try to understand it.
The SDK client may use it for local activities or side effects.

| Field                            | Description                                                                                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| marker_name                      | Identifies various markers.                                                                                         |
| details                          | Serialized information recorded in the marker.                                                                      |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with.                     |
| header                           | Information passed by the sender of the [Signal](/sending-messages#sending-signals) that is copied into the marker. |
| failure                          | Serialized result of a [Workflow](/workflows) failure.                                                              |

### StartChildWorkflowExecutionInitiated

This [Event](/workflow-execution/event#event) type indicates that the [Temporal Server](/temporal-service/temporal-server) will try to start a Child Workflow.

| Field         | Description                                     |
| ------------- | ----------------------------------------------- |
| namespace     | [Namespace](/namespaces) of the Child Workflow. |
| workflow_id   | Identifies the Child Workflow.                  |
| workflow_type | The name/type of Workflow that was initiated.   |

### StartChildWorkflowExecutionFailed

This [Event](/workflow-execution/event#event) type indicates a [Child Workflow Execution](/child-workflows) cannot be started / triggered.
It is usually due to a Child Workflow Id collision.

| Field                            | Description                                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| namespace                        | [Namespace](/namespaces) of the Child Workflow.                                                                          |
| workflow_id                      | Identifies the Child Workflow.                                                                                           |
| workflow_type                    | The name/type of Workflow that has failed.                                                                               |
| initiated_event_id               | Id of the [StartChildWorkflowExecutionInitiated](#startchildworkflowexecutioninitiated) Event this Event corresponds to. |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with.                          |

### ChildWorkflowExecutionStarted

This [Event](/workflow-execution/event#event) type indicates a [Child Workflow Execution](/child-workflows) has successfully started / triggered.
This would also cause the [WorkflowExecutionStarted](#workflowexecutionstarted) to be recorded for the Workflow that has started.

| Field              | Description                                                                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| namespace          | [Namespace](/namespaces) of the Child Workflow.                                                                                  |
| initiated_event_id | Id of the [StartChildWorkflowExecutionInitiated](#startchildworkflowexecutioninitiated) Event this Event corresponds to.         |
| workflow_execution | Identifies the Workflow and the run of the Workflow Execution.                                                                   |
| workflow_type      | The name/type of Workflow that has started execution.                                                                            |
| header             | Information passed by the sender of the [Signal](/sending-messages#sending-signals) that is copied into the Child Workflow Task. |

### ChildWorkflowExecutionCompleted

This [Event](/workflow-execution/event#event) type indicates that the [Child Workflow Execution](/child-workflows) has successfully completed.
This would also cause the [WorkflowExecutionCompleted](#workflowexecutioncompleted) to be recorded for the [Workflow](/workflows) that has completed.

| Field              | Description                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| result             | Serialized result of the completed Child Workflow.                                                                       |
| namespace          | [Namespace](/namespaces) of the completed Child Workflow.                                                                |
| workflow_execution | Identifies the Workflow and the run of the [Workflow Execution](/workflow-execution).                                    |
| workflow_type      | The name/type of Workflow that was completed.                                                                            |
| initiated_event_id | Id of the [StartChildWorkflowExecutionInitiated](#startchildworkflowexecutioninitiated) Event this Event corresponds to. |
| started_event_id   | Id of the [ChildWorkflowExecutionStarted](#childworkflowexecutionstarted) Event this Event corresponds to.               |

### ChildWorkflowExecutionFailed

This [Event](/workflow-execution/event#event) type indicates that the [Child Workflow Execution](/child-workflows) has unsuccessfully completed.
This would also cause the [WorkflowExecutionFailed](#workflowexecutionfailed) to be recorded for the Workflow that has failed.

| Field              | Description                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| failure            | Serialized result of a [Workflow](/workflows) failure.                                                                   |
| namespace          | [Namespace](/namespaces) of the Child Workflow that failed.                                                              |
| workflow_execution | Identifies the Workflow and the run of the [Workflow Execution](/workflow-execution).                                    |
| workflow_type      | The name/type of Workflow that has failed.                                                                               |
| initiated_event_id | Id of the [StartChildWorkflowExecutionInitiated](#startchildworkflowexecutioninitiated) Event this Event corresponds to. |
| started_event_id   | Id of the [ChildWorkflowExecutionStarted](#childworkflowexecutionstarted) Event this failure corresponds to.             |
| retry_state        | The reason provided for whether the Task should or shouldn't be retried.                                                 |

### ChildWorkflowExecutionCanceled

This [Event](/workflow-execution/event#event) type indicates that the Child Workflow Execution has been canceled.
This would also cause the [WorkflowExecutionCanceled](#workflowexecutioncanceled) to be recorded for the Workflow that was canceled.

| Field              | Description                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| details            | Additional information reported by the Child Workflow upon cancelation.                                                  |
| namespace          | [Namespace](/namespaces) of the Child Workflow that was canceled.                                                        |
| workflow_execution | Identifies the Workflow and the run of the [Workflow Execution](/workflow-execution).                                    |
| workflow_type      | The name/type of Workflow that was canceled.                                                                             |
| initiated_event_id | Id of the [StartChildWorkflowExecutionInitiated](#startchildworkflowexecutioninitiated) Event this Event corresponds to. |
| started_event_id   | Id of the [ChildWorkflowExecutionStarted](#childworkflowexecutionstarted) Event this cancelation corresponds to.         |

### ChildWorkflowExecutionTimedOut

This Event type indicates that the [Child Workflow Execution](/child-workflows) has timed out by the [Temporal Server](/temporal-service/temporal-server).
This would also cause the [WorkflowExecutionTimeOut](#workflowexecutiontimedout) to be recorded for the Workflow that timed out.

| Field              | Description                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| namespace          | [Namespace](/namespaces) of the Child Workflow.                                                                          |
| workflow_execution | Identifies the Workflow and the run of the Workflow Execution.                                                           |
| workflow_type      | The name/type of Workflow that has timed out.                                                                            |
| initiated_event_id | Id of the [StartChildWorkflowExecutionInitiated](#startchildworkflowexecutioninitiated) Event this Event corresponds to. |
| started_event_id   | Id of the [ChildWorkflowExecutionStarted](#childworkflowexecutionstarted) Event that this timeout corresponds to.        |
| retry_state        | The reason provided for whether the Task should or shouldn't be retried.                                                 |

### ChildWorkflowExecutionTerminated

This [Event](/workflow-execution/event#event) type indicates that the Child Workflow Execution has been terminated.
This would also cause the [WorkflowExecutionTerminated](#workflowexecutionterminated) to be recorded for the Workflow that was terminated.

| Field              | Description                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| namespace          | [Namespace](/namespaces) of the Child Workflow.                                                                          |
| workflow_execution | Identifies the Workflow and the run of the Workflow Execution.                                                           |
| workflow_type      | The name/type of Workflow that was terminated.                                                                           |
| initiated_event_id | Id of the [StartChildWorkflowExecutionInitiated](#startchildworkflowexecutioninitiated) Event this Event corresponds to. |
| started_event_id   | Id of the [ChildWorkflowExecutionStarted](#childworkflowexecutionstarted) Event that this termination corresponds to.    |
| retry_state        | The reason provided for whether the Task should or shouldn't be retried.                                                 |

### SignalExternalWorkflowExecutionInitiated

This [Event](/workflow-execution/event#event) type indicates that the [Temporal Server](/temporal-service/temporal-server) will try to [Signal](/sending-messages#sending-signals) the targeted [Workflow](/workflows).
This Event type contains the Signal name, as well as a Signal payload.

| Field                            | Description                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------------------- |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with. |
| namespace                        | [Namespace](/namespaces) of the Workflow that's to be signaled.                                 |
| workflow_execution               | Identifies the Workflow and the run of the [Workflow Execution](/workflow-execution).           |
| signal_name                      | The name/type of Signal to be fired.                                                            |
| input                            | Information that is deserialized by the SDK to provide arguments to the Workflow Function.      |
| child_workflow_only              | Set to true if this Workflow is a child of the Workflow which issued the cancelation request.   |
| header                           | Information to be passed from the Signal to the targeted Workflow.                              |

### SignalExternalWorkflowExecutionFailed

This [Event](/workflow-execution/event#event) type indicates that the [Temporal Server](/temporal-service/temporal-server) cannot Signal the targeted [Workflow](/workflows), usually because the Workflow could not be found.

| Field                            | Description                                                                                                                                                                                  |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| workflow_task_completed_event_id | The Id of the [WorkflowTaskCompleted](#workflowtaskcompleted) that the Event was reported with.                                                                                              |
| namespace                        | [Namespace](/namespaces) of the Workflow that failed to execute.                                                                                                                             |
| workflow_execution               | Identifies the Workflow and the run of the [Workflow Execution](/workflow-execution).                                                                                                        |
