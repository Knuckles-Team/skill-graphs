    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.028.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.029.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.031.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.032.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.033.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.034.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.035.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.036.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.037.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.040.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.043.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.044.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.046.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.047.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.048.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.049.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.054.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.057.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.058.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.059.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.060.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.061.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.063.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.064.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.066.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.067.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.069.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.070.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.073.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.075.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.076.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.077.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.079.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.081.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.082.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.083.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.084.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.085.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.087.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.088.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.089.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.090.jpeg',
  ]}
  captions={[
    'NA',
    'This walkthrough begins with a request to execute this Workflow Definition, passing in some input data. In this case, the input data contains information about the customer and the pizzas ordered.',
    "This request to execute the Workflow Definition results in the Temporal Service recording a `WorkflowExecutionStarted` Event into the Event History. This is always the first Event for any Workflow Execution. It's not indicated in the image, but the `WorkflowExecutionStarted` Event contains the input data provided to this Workflow Execution.",
    'The Worker then adds a Workflow Task to the Task Queue, and records a `WorkflowTaskScheduled` Event.',
    'The Service will then dispatch this Activity to the Worker.',
    'The Worker accepts the Task.',
    'The Temporal Service records a `WorkflowTaskStarted` Event.',
    'The Worker then invokes the Workflow code and runs the code within it, one statement at a time.',
    'The first few lines of code do not result in any interaction with the Temporal Service.',
    'The first few lines of code do not result in any interaction with the Temporal Service.',
    'The first few lines of code do not result in any interaction with the Temporal Service.',
    'The first few lines of code do not result in any interaction with the Temporal Service.',
    'The first few lines of code do not result in any interaction with the Temporal Service.',
    'However, the Worker encounters a request to execute an Activity, so the Worker will complete the current Workflow Task.',
    'The Service adds `WorkflowTaskCompleted` to the Event History.',
    'The Worker then makes a single gRPC call - `RespondWorkflowTaskCompleted` - to the Temporal Service, which signals completion of the Workflow Task, and includes any commands such as `ScheduleActivityTask`, containing all details about the Activity Execution within this call. So to clarify, `WorkflowTaskCompleted` and `ActivityTaskScheduled` are technically one call.',
    'In response, the Temporal Service queues an Activity Task and records an `ActivityTaskScheduled` Event to the Event History. This is shown in blue to indicate that it is the direct result of the Command.',
    'The Service will then dispatch this Activity to an available Worker.',
    "The Worker accepts the Task and starts working on the code within this `GetDistance` Activity. The Temporal Service records an `ActivityTaskStarted` Event to the Event History to signify that the Worker has started the Activity Task. This Event is in a pink box to indicate that it's the indirect result of the Command. The `ActivityTaskStarted` Event is not written to the Event History until a Task closes, because the number of retry attempts is an attribute of the `ActivityTaskStarted` Event.",
    'When the Activity function returns - with a result of 15 - the Worker notifies the Service that the Activity Execution is complete.',
    'The Temporal Service records an `ActivityTaskCompleted` Event, which contains the result of the Activity.',
    'In order to deliver the Activity Task result, 15, back to the Workflow, the Temporal Service creates another Workflow Task which includes the result of this Activity. `WorkflowTaskScheduled` is appended to the Event History.',
    'The Service will then dispatch this Activity to an available Worker.',
    'The Worker dequeues the Task and resumes execution of the Workflow. The `WorkflowTaskStarted` Event gets appended to the Event History.',
    'The Worker then executes the next few lines of code, evaluating the distance.',
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
    'For example, the `totalPrice` variable was the same as it was prior to the crash.',
    'When the Replay reaches the call to schedule to `GetDistance` Activity, it creates a `ScheduleActivityTask` Command but does not issue it to the Temporal Service. Instead, the Worker inspects the Event History and finds three Events related to this Activity.',
    'The `ActivityTaskScheduled` Event, with the details including this specific Activity Type, indicates that the Task was previously scheduled by the Temporal Service.',
    'The `ActivityTaskStarted` Event indicates that a Worker dequeued the Task.',
    'The `ActivityTaskCompleted` Event indicates that the Worker successfully completed the Task for the `GetDistance` Activity, having returned a value of 15. The Worker now knows that the Activity has completed and does not need to issue the Command.',
    "The Worker uses the value stored in the `ActivityTaskCompleted` Event, 15, and assigns it to the `distance` variable. To emphasize, the Worker is not re-executing the Activity, it's using the result stored in the Event History, so there is no way that the Activity behaves differently during History Replay than the original execution.",
    'Replay continues replaying the code.',
    'The Worker then reaches the request to start a Timer. It creates a Command, `StartTimer`. Again, the Worker does not issue the Command to the Service.',
    'Instead, the Worker checks the Event History to see whether the Timer was started and fired during the previous execution. The Event History indicates that the Timer was started, because there is a `TimerStarted` Event.',
    'The Event History also indicates that the Timer was fired, because there is a `TimerFired` Event.',
    'At this point, the Worker has reached the point where the crash occurred, and replaying the code has completely restored the state of the Workflow Execution prior to the crash.',
    'For example, the `totalPrice` variable was the same as it was prior to the crash.',
    'Since Replay uses the same input data as before, this also means that the conditional statement evaluates to `false`, like it did before.',
    'The Worker has now reached a statement beyond where the crash occurred, which is evident because the Event History does not contain any Events related to this `SendBill` Activity. Further execution of this Workflow continues on as if the crash never happened. Because the Worker encounters a request to execute an Activity, the Worker completes the current Workflow Task.',
    'The Worker issues a Command to the Service, requesting execution of the Activity.',
    'The Worker adds the Activity Task to the Task queue, adding `ActivityTaskScheduled` to the Event History. The Worker polls for the Task.',
    'The Worker dequeues the Task, adding `ActivityTaskStarted` to the Event History.',
    'When the Activity returns a result, the Worker notifies the Service.',
    'The Worker records an `ActivityTaskCompleted` Event, which includes the result from the `SendBill` Activity.',
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
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.001.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.002.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.004.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.005.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.006.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.007.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.008.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.009.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.011.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.012.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.013.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.014.jpeg',
  ]}
  captions={[
    'NA',
    'Imagine the following Workflow Definition is being executed. As the Workflow executes step by step, the first line that results in a Command is the call to the `ImportSalesData` Activity. The Worker issues the `ScheduleActivityTask` Command to the Service. In this case, the execution of the Activity is successful, so the Service logs three Events to the Event History: `ActivityTaskScheduled`, `ActivityTaskStarted`, `ActivityTaskCompleted`.',
    'Now, the Worker reaches a conditional statement which evaluates the value of a random-generated number. The random number generator happens to return the value of 84 during this execution. Since the expression evaluates to `true`, execution continues with the next line.',
    'The next line is a request to start a Timer, so the Worker issues a Command to the Service - `StartTimer` - requesting that it starts a Timer. The Service starts the Timer, records an Event - `TimerStarted` - and then records another Event when the Timer fires - `TimerFired`.',
    'Now imagine that the Worker happens to crash once it reaches to next line, so another Worker takes over, using Replay to restore the current state before continuing execution of the lines that follow.',
    'The Worker then requests the Event History to replay it. Once the Worker has the Event History, the Worker determines the expected sequence of Commands needed to restore the current state. The Worker is expecting to encounter the `ScheduleActivityTask` and `StartTimer` Commands.',
    'As the Worker executes the code during Replay, it reaches the first call to execute an Activity and creates a `ScheduleActivityTask` Command.',
    "This Command matches the one expected based on the Event History. It's not only the right type of Command, but it also occurs at the right position in the sequence of expected Commands. Therefore, Replay proceeds.",
    'The Worker now reaches the conditional statement with the random number generator. This time, the random number generator happens to return 14, so the conditional expression evaluates to `false`, and execution skips over the next line.',
    'The Worker now reaches the next Command which is to request execution of the `RunDailyReport` Activity, so the Worker creates another `ScheduleActivityTask` Command.',
    'However, this is a different Command than it expected to find at this position in the Event History. Since the Workflow produced a different sequence of Commands during Replay than it was expecting due to the Event History that was produced prior to the crash, the Worker is unable to restore the previous state.',
    'The Workflow Execution was unable to be replayed due to a non-deterministic error.',
  ]}
/>

Note that non-deterministic failures do not fail the Workflow Execution by default. A non-deterministic failure is
considered a [Workflow Task Failure](https://docs.temporal.io/references/failures#workflow-task-failures) which is
considered a transient failure, meaning it retries over and over. Users can also fix the source of non-determinism,
perhaps by removing the Activity, and then restart the Workers. This means that this type of failure can recover by
itself. You can also use a strategy called versioning to address this non-determinism error. See
[versioning](/develop/go/workflows/versioning) to learn more.

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

## Event History walkthrough with the Java SDK

In order to understand how Workflow Replay works, this page will go through the following walkthroughs:

1. [How Workflow Code Maps to Commands](#How-Workflow-Code-Maps-To-Commands)
2. [How Workflow Commands Map to Events](#How-Workflow-Commands-Map-To-Events)
3. [How History Replay Provides Durable Execution](#How-History-Replay-Provides-Durable-Execution)
4. [Example of a Non-Deterministic Workflow](#Example-of-Non-Deterministic-Workflow)

## How Workflow Code Maps to Commands {/* #How-Workflow-Code-Maps-To-Commands */}

This walkthrough will cover how the Workflow code maps to Commands that get sent to the Temporal Service, letting the
Temporal Service know what to do.

<PhotoCarousel
  images={[
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.001.jpeg',
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.003.jpeg',
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.004.jpeg',
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.005.jpeg',
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.006.jpeg',
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.008.jpeg',
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.009.jpeg',
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.010.jpeg',
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.011.jpeg',
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.012.jpeg',
    'https://learn.temporal.io/courses/temporal-102/java/event-history-walkthrough/code-commands/code-commands.013.jpeg',
  ]}
  captions={[
    'NA',
    'Here is code for a basic Temporal Workflow Definition, which does the items described on the right side of the screen.',
    'Some steps are internal to the Workflow and do not involve interaction with the Service.',
    'On the other hand, some steps do involve interaction with the Temporal Service. For example, when the code requests execution of an Activity, it generates a Command to schedule the Activity Task. Another example is when the code returns a value from the Workflow, the Worker notifies the Temporal Service that the Workflow Execution is complete.',
    "The code walkthrough will now begin. In this Workflow Definition, setting the Start-to-Close Timeout and setting a variable are internal steps. That is, these steps don't require any interaction with the Temporal Service.",
