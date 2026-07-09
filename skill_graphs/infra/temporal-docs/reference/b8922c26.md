    'The Service will then dispatch this Activity to an available Worker.',
    'The Service will respond to the poll request with a Task, and the Worker will begin executing the code needed to complete the Task.',
    "The `ActivityTaskStarted` Event is not written to the Event History until a Task closes, because the number of retry attempts is an attribute of the `ActivityTaskStarted` Event. Once the Activity completes, the Temporal Service records another Event in response to the Worker accepting the Task: `ActivityTaskStarted`. This Event is colored pink to indicate that it's an indirect result of the Command. By the way, the `Start-to-Close` Timeout indicates the amount of time that the Activity has to complete.",
    "The Worker executes the code within the Activity Definition, and when that function returns a result, the Worker sends a message to the Temporal Service, notifying it that the Task is complete. To reiterate, this is just a notification, not a Command, because it's not requesting that the Temporal Service do something that will allow the Workflow Execution to progress. In response to this notification, the Temporal Service records another Event: `ActivityTaskCompleted`.",
    'The next statement that results in a Command is the call to start a Timer. It issues a `StartTimer` Command.',
    'The Temporal Service responds after starting a Timer for 30 minutes in the Service, logging a `TimerStarted` Event to the history. It is a direct result of the `StartTimer` Command.',
    'After 30 minutes has elapsed, the Timer is fired on the Temporal Service, which it then records the Event `TimerFired` to the history. The Workflow Execution continues with the next statement, but this is an internal step, meaning that it does not interact with the Temporal Service.',
    'The Worker then reaches the call to the `sendBill` Activity and issues another `ScheduleActivityTask` Command. The Temporal Service adds an Activity Task to the Task Queue and records an `ActivityTaskScheduled` Event to the Event History.',
    'The Service will then dispatch this Activity to the Worker.',
    'The Worker then removes the Task from the Task Queue, and begins working on it. The Temporal Service records an `ActivityTaskStarted` Event to the Event History, signifying that the Task has been dequeued.',
    'When the Activity returns, the Task is complete and the Worker notifies the Temporal Service. In response, the Temporal Service records the `ActivityTaskCompleted` Event to the Event History. Execution will then continue until the Workflow has completed. There will be a complete walkthrough in the next section.',
  ]}
/>

## How History Replay Provides Durable Execution {/* #How-History-Replay-Provides-Durable-Execution */}

Now that you have seen how code maps to Commands, and how Commands map to Events, this next walkthrough will take a look
at how Temporal uses Replay with the Events to provide Durable Execution and restore a Workflow Execution in the case of
a failure.

This code walkthrough will begin by walking through a Workflow Execution, describing how the code maps to Commands and
Events. There will then be a Worker crash halfway through, explaining how Temporal uses Replay to recover the state of
the Workflow Execution, ultimately resulting in a completed execution that's identical to one that had not crashed.

<PhotoCarousel
  images={[
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.001.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.002.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.003.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.004.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.005.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.006.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.007.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.008.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.009.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.011.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.012.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.013.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.015.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.016.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.018.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.019.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.020.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.021.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.022.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.026.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.027.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.028.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.029.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.031.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.032.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.035.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.036.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.039.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.040.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.042.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.043.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.044.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.045.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.047.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.048.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.049.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.050.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.051.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.053.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.054.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.057.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.058.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.059.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.061.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.062.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.063.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.064.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.067.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.068.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.069.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.070.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.071.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.073.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.074.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.075.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.076.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.077.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.079.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.080.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.081.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/history-replay/history-replay.082.jpeg',
  ]}
  captions={[
    'NA',
    'This walkthrough begins with a request to execute this Workflow Definition, passing in some input data. In this case, the input data contains information about the customer and the pizzas ordered.',
    "This request to execute the Workflow Definition results in the Temporal Service recording a `WorkflowExecutionStarted` Event into the Event History. It's not indicated in the image, but the `WorkflowExecutionStarted` Event contains the input data provided to this Workflow Execution.",
    'The Worker then adds a Workflow Task to the Task Queue, and records a `WorkflowTaskScheduled` Event.',
    'The Service will then dispatch this Activity to the Worker.',
    'The Worker accepts the Task.',
    'The Temporal Service records a `WorkflowTaskStarted` Event.',
    'The Worker then invokes the Workflow code and runs the code within it, one statement at a time.',
    'The first few lines of code do not result in any interaction with the Temporal Service.',
    'However, the Worker encounters a request to execute an Activity, so the Worker will complete the current Workflow Task. The Service adds `WorkflowTaskCompleted` to the Event History.',
    'The Worker then makes a single gRPC call - `RespondWorkflowTaskCompleted` - to the Temporal Service, which signals completion of the Workflow Task, and includes any commands such as `ScheduleActivityTask`, containing all details about the Activity Execution within this call. So to clarify, `WorkflowTaskCompleted` and `ActivityTaskScheduled` are technically one call.',
    'In response, the Temporal Service queues an Activity Task and records an `ActivityTaskScheduled` Event to the Event History. This is shown in blue to indicate that it is the direct result of the Command.',
    'The Service will then dispatch this Activity to an available Worker.',
    "The Worker accepts the Task and starts working on the code within this `getDistance` Activity. The Temporal Service records an `ActivityTaskStarted` Event to the Event History to signify that the Worker has started the Activity Task. This Event is in a pink box to indicate that it's the indirect result of the Command. The `ActivityTaskStarted` Event is not written to the Event History until a Task closes, because the number of retry attempts is an attribute of the `ActivityTaskStarted` Event.",
    'When the Activity function returns - with a result of 15 - the Worker notifies the Service that the Activity Execution is complete.',
    'The Temporal Service records an `ActivityTaskCompleted` Event, which contains the result of the Activity.',
    'In order to deliver the Activity Task result, 15, back to the Workflow, the Temporal Service creates another Workflow Task which includes the result of this Activity. `WorkflowTaskScheduled` is appended to the Event History.',
    'The Service will then dispatch this Activity to an available Worker.',
    'The Worker dequeues the Task and resumes execution of the Workflow. The `WorkflowTaskStarted` Event gets appended to the Event History. The Worker then executes the next few lines of code - evaluating the distance, calculating the price of the pizza, and so on.',
    'The Worker reaches the request to start the Timer. Therefore, it notifies the Service to complete the current Workflow Task.',
    'The Worker will complete the current Workflow Task, adding `WorkflowTaskCompleted` to the Event History. This Event includes the `StartTimer` Command.',
    'The Worker issues a `StartTimer` Command to the Service, requesting it to set the Timer for 30 minutes. The Service records a `TimerStarted` Event in response.',
    'The Workflow does not progress until the Timer fires.',
    'After 30 minutes has elapsed, the Timer fires, and the Service records a `TimerFired` Event.',
    'The Service now adds a new Workflow Task to the Queue in order to deliver the `TimerFired` Event to the Workflow, so `WorkflowTaskScheduled` is added to the Event History to drive the Workflow progress forward.',
    'The Worker polls for the Task, dequeues it, and continues execution of the Workflow code.',
    'However, the Worker happens to crash right here. How does Temporal recover the state of the Workflow? But first, how do you know when a Worker has crashed?',
    'Once a Worker has accepted a Task, it is expected to complete that task within a predefined duration, known as a Timeout. This timeout is available to recognize whether a Worker has gone down. This results in a Workflow Task Timeout, which has a default value of 10 seconds.',
    'Therefore, if the Worker failed to complete this Workflow Task within that time, the Service will schedule a new Workflow Task.',
    "The Worker polling might be done by another Worker that's running in the Worker fleet or by a new Worker process created by restarting the one that crashed.",
    'In either case, the Worker will need the current Event History for this execution, so it requests it from the Service.',
    'The Service provides the Event History. Notice the black horizontal line in the column on the right to indicate the final Event in the History at the time of the Worker Crash.',
    'The Worker then begins a re-execution of the code, using the same input, which was stored in the `WorkflowExecutionStarted` Event. Remember, because the Workflow code is deterministic, the state of all variables encountered so far is identical to what it was before the crash.',
    'When the Replay reaches the call to schedule to `getDistance` Activity, it creates a `ScheduleActivityTask` Command but does not issue it to the Temporal Service. Instead, the Worker inspects the Event History and finds three Events related to this Activity.',
    'The `ActivityTaskScheduled` Event, with the details including this specific Activity Type, indicates that the Task was previously scheduled by the Temporal Service.',
    'The `ActivityTaskStarted` Event indicates that a Worker dequeued the Task.',
    'The `ActivityTaskCompleted` Event indicates that the Worker successfully completed the Task for the `getDistance` Activity, having returned a value of 15. The Worker now knows that the Activity has completed and does not need to issue the Command.',
    "The Worker uses the value stored in the `ActivityTaskCompleted` Event, 15, and assigns it to the `distance` variable. To emphasize, the Worker is not re-executing the Activity, it's using the result stored in the Event History, so there is no way that the Activity behaves differently during History Replay than the original execution.",
    'Replay continues replaying the code.',
    'NA',
    'The Worker then reaches the request to start a Timer. It creates a Command, `StartTimer`. Again, the Worker does not issue the Command to the Service.',
    'Instead, the Worker checks the Event History to see whether the Timer was started and fired during the previous execution. The Event History indicates that the Timer was started, because there is a `TimerStarted` Event.',
    'The Event History also indicates that the Timer was fired, because there is a `TimerFired` Event.',
    'At this point, the Worker has reached the point where the crash occurred, and replaying the code has completely restored the state of the Workflow Execution prior to the crash.',
    'For example, the `distance` variable was set using the value that was stored in the Event History from the previous Execution.',
    'Since Replay uses the same input data as before, this also means that the conditional statement evaluates to `false`, like it did before.',
    'The `totalPrice` variable also has the same value as it did before the crash.',
    'The Worker has now reached a statement beyond where the crash occurred, which is evident because the Event History does not contain any Events related to this `sendBill` Activity. Further execution of this Workflow continues on as if the crash never happened.',
    'Because the Worker encounters a request to execute an Activity, the Worker completes the current Workflow Task.',
    'The Worker issues a Command to the Service, requesting execution of the Activity.',
    'The Worker adds the Activity Task to the Task queue, adding `ActivityTaskScheduled` to the Event History. The Worker polls for the Task.',
    'The Worker dequeues the Task, adding `ActivityTaskStarted` to the Event History.',
    'When the Activity returns a result, the Worker notifies the Service.',
    'The Worker records an `ActivityTaskCompleted` Event, which includes the result from the `sendBill` Activity.',
    "But since the Service hasn't yet received a Command that says the Workflow Execution has completed or failed, the Service schedules another Workflow Task to continue progress of the execution.",
    'The Service will then dispatch this Activity to an available Worker.',
    'The Worker accepts the Task.',
    'When the Workflow completes, the Worker notifies the Service that the current Workflow Task is complete.',
    'The Service records a `WorkflowTaskCompleted` Event to reflect this.',
    'Since the Worker has now successfully completed the execution of the Workflow, it issues a `CompleteWorkflowExecution` Command to the Service, which contains the result returned by the Workflow Execution.',
    'The Service then records `WorkflowExecutionCompleted` as the final Event in the Event History. The Workflow Execution is now complete.',
  ]}
/>

## Example of a Non-Deterministic Workflow {/* #Example-of-Non-Deterministic-Workflow */}

Now that Replay has been covered, this section will explain why Workflows need to be
[deterministic](https://docs.temporal.io/workflow-definition#deterministic-constraints) in order for Replay to work.

A Workflow is deterministic if every execution of its Workflow Definition produces the same Commands in the same
sequence given the same input.

As mentioned in the [`How History Replay Provides Durable Execution`](#How-History-Replay-Provides-Durable-Execution)
walkthrough, in the case of a failure, a Worker requests the Event History to replay it. During Replay, the Worker runs
the Workflow code again to produce a set of Commands which is compared against the sequence of Commands in the Event
History. When there’s a mismatch between the expected sequence of Commands the Worker expects based on the Event History
and the actual sequence produced during Replay (due to non-determinism), Replay will be unable to continue.

To better understand why Workflows need to be deterministic, it's helpful to look at a Workflow Definition that violates
it. In this case, this code will walk through a Workflow Definition that breaks the determinism constraint with a random
number generator.

<PhotoCarousel
  images={[
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.001.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.002.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.004.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.006.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.008.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.009.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.010.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.011.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.013.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.015.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.016.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.017.jpeg',
    'https://learn.temporal.io/courses/temporal-102/typescript/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.018.jpeg',
  ]}
  captions={[
    'NA',
    'Imagine the following Workflow Definition is being executed.',
    'As the Workflow executes step by step, the first line that results in a Command is the call to the `importSalesData` Activity. The Worker issues the `ScheduleActivityTask` Command to the Service. In this case, the execution of the Activity is successful, so the Service logs three Events to the Event History: `ActivityTaskScheduled`, `ActivityTaskStarted`, `ActivityTaskCompleted`.',
    'Now, the Worker reaches a conditional statement which evaluates the value of a random-generated number. The random number generator happens to return the value of 84 during this execution. Since the expression evaluates to `true`, execution continues with the next line.',
    'The next line is a request to start a Timer, so the Worker issues a Command to the Service - `StartTimer` - requesting that it starts a Timer.',
    'The Service starts the Timer, records an Event - `TimerStarted` - and then records another Event when the Timer fires - `TimerFired`.',
    'Now imagine that the Worker happens to crash once it reaches to next line, so another Worker takes over, using Replay to restore the current state before continuing execution of the lines that follow.',
    'The Worker then requests the Event History to replay it. Once the Worker has the Event History, the Worker determines the expected sequence of Commands needed to restore the current state. The Worker is expecting to encounter the `ScheduleActivityTask` and `StartTimer` Commands.',
