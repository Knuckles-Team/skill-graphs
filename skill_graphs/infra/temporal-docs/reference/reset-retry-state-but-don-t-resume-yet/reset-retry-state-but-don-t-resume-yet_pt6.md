    'At this point, the Worker has reached the point where the crash occurred, and replaying the code has completely restored the state of the Workflow Execution prior to the crash.',
    'For example, the `distance` variable was set using the value that was stored in the Event History from the previous Execution.',
    'Since Replay uses the same input data as before, this also means that the conditional statement evaluates to `false`, like it did before.',
    'The `totalPrice` variable also has the same value as it did before the crash.',
    'The Worker has now reached a statement beyond where the crash occurred, which is evident because the Event History does not contain any Events related to this `SendBill` Activity. Further execution of this Workflow continues on as if the crash never happened.',
    'Because the Worker encounters a request to execute an Activity, the Worker completes the current Workflow Task.',
    'The Worker issues a Command to the Service, requesting execution of the Activity.',
    'The Worker adds the Activity Task to the Task queue, adding `ActivityTaskScheduled` to the Event History. The Worker polls for the Task.',
    'The Worker dequeues the Task, adding `ActivityTaskStarted` to the Event History.',
    'When the Activity returns a result, the Worker notifies the Service.',
    'The Worker records an `ActivityTaskCompleted` Event, which includes the result from the `SendBill` Activity.',
    "But since the Service hasn't yet received a Command that says the Workflow Execution has completed or failed, the Service schedules another Workflow Task to continue progress of the execution.",
    'The Worker polls for and accepts the Task.',
    'When the Workflow completes, the Worker notifies the Service that the current Workflow Task is complete. The Service records a `WorkflowTaskCompleted` Event to reflect this.',
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
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.014.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.002.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.015.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.016.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.018.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.019.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.020.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.021.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.022.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.023.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.024.jpeg',
    'https://learn.temporal.io/courses/temporal-102/dotnet/event-history-walkthrough/nondeterministic-workflow/nondeterministic-workflow.025.jpeg',
  ]}
  captions={[
    'NA',
    'Imagine the following Workflow Definition is being executed.',
    'As the Workflow executes step by step, the first line that results in a Command is the call to the `ImportSalesData` Activity. The Worker issues the `ScheduleActivityTask` Command to the Service. In this case, the execution of the Activity is successful, so the Service logs three Events to the Event History: `ActivityTaskScheduled`, `ActivityTaskStarted`, `ActivityTaskCompleted`.',
    'Now, the Worker reaches a conditional statement which evaluates the value of a random-generated number. The random number generator happens to return the value of 84 during this execution. Since the expression evaluates to `true`, execution continues with the next line.',
    'The next line is a request to start a Timer, so the Worker issues a Command to the Service - `StartTimer` - requesting that it starts a Timer.',
    'The Service starts the Timer, records an Event - `TimerStarted` - and then records another Event when the Timer fires - `TimerFired`.',
    'Now imagine that the Worker happens to crash once it reaches to next line, so another Worker takes over, using Replay to restore the current state before continuing execution of the lines that follow.',
    'The Worker then requests the Event History to replay it. Once the Worker has the Event History, the Worker determines the expected sequence of Commands needed to restore the current state. The Worker is expecting to encounter the `ScheduleActivityTask` and `StartTimer` Commands.',
    "As the Worker executes the code during Replay, it reaches the first call to execute an Activity and creates a `ScheduleActivityTask` Command. This Command matches the one expected based on the Event History. It's not only the right type of Command, with the same details, but it also occurs at the right position in the sequence of expected Commands. Therefore, Replay proceeds.",
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
[versioning](https://docs.temporal.io/develop/dotnet/workflows/versioning) to learn more.

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

## Event History

With Temporal, your Workflows can seamlessly recover from crashes. This is made possible by the [Event History](https://docs.temporal.io/workflow-execution/event), a complete and durable log of everything that has happened in the lifecycle of a Workflow Execution, as well as the ability of the Temporal Service to durably persist the Events during Replay.

Temporal uses the Event History to record every step taken along the way. Each time your Workflow Definition makes an API call to execute an Activity or start a Timer for instance, it doesn’t perform the action directly. Instead, it sends a Command to the Temporal Service.

A Command is a requested action issued by a Worker to the Temporal Service after a Workflow Task Execution completes. The Temporal Service will act on these Commands such as scheduling an Activity or scheduling a timer. These Commands are then mapped to Events which are persisted in case of failure. For example, if the Worker crashes, the Worker uses the Event History to replay the code and recreate the state of the Workflow Execution to what it was immediately before the crash. It then resumes progress from the point of failure as if the failure never occurred.

For a deep dive on how the Event History works, refer to the walkthroughs in the dropdown.

- [Go](/encyclopedia/event-history/event-history-go)
- [Java](/encyclopedia/event-history/event-history-java)
- [Python](/encyclopedia/event-history/event-history-python)
- [Typescript](/encyclopedia/event-history/event-history-typescript)
- [.NET](/encyclopedia/event-history/event-history-dotnet)

---

## Event History walkthrough with the Go SDK

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
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.001.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.002.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.003.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.004.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.005.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.007.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.008.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.009.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.010.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.011.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/code-commands/code-commands.012.jpeg',
  ]}
  captions={[
    'NA',
    'Here is code for a basic Temporal Workflow Definition, which does the items described on the right side of the screen.',
    'Some steps are internal to the Workflow and do not involve interaction with the Service.',
    'On the other hand, some steps do involve interaction with the Temporal Service. For example, when the code requests execution of an Activity, it generates a Command to schedule the Activity Task. Another example is when the code returns a value from the Workflow, the Worker notifies the Temporal Service that the Workflow Execution is complete.',
    "The code walkthrough will now begin. In this Workflow Definition, setting the Start-to-Close Timeout and setting a variable are internal steps. That is, these steps don't require any interaction with the Temporal Service.",
    "The Worker then reaches a statement that does require interaction with the Temporal Service. In this case, it's a request to execute an Activity. This causes the Worker to issue a Command to the Temporal Service and provides the details needed. For example, the `ScheduleActivityTask` Command contains details such as the Task Queue name, the Activity Type, and the input parameter values. Even though an Activity can take hours or days to complete, the Worker does not use resources.",
    'After the `GetDistance` Activity has successfully completed, the Worker continues executing the Workflow code. The next line, highlighted here, evaluates a variable. Depending on the outcome, it may return an error, which would send a Command to the Server to request it to fail the Workflow Execution. However, this example assumes that this is a delivery for a nearby customer. The execution will continue.',
    'The Worker now reaches the call to start a Timer, which is another statement that involves interaction with the Temporal Service. This causes the Worker to issue another Command, one which requests the Temporal Service to start a Timer. The duration is one of the details specified in this Command. Further execution of this Workflow will now pause for 30 minutes until the Timer fires.',
    "The Timer then fires. The next few lines, highlighted here, create and populate a data structure that represents the input for the next Activity. While it is related to the Activity, it doesn't involve any interaction with the Service.",
    'The next statement involves interaction with the Temporal Service. It requests execution of an Activity, so the Worker issues another Command to the Temporal Service: `ScheduleActivityTask`.',
    'Finally, returning from the Workflow function also results in a Command. It issues a `CompleteWorkflowExecution` Command to the Temporal Service, which includes the value that was returned from the function.',
  ]}
/>

## How Workflow Commands Map to Events {/* #How-Workflow-Commands-Map-To-Events */}

The Commands that are sent to the Temporal Service are then turned into Events, which build up the Event History. The
Event History is a detailed log of Events that occur during the lifecycle of a Workflow Execution, such as the execution
of Workflow Tasks or Activity Tasks. Event Histories are persisted to the database used by the Temporal Service, so
they're durable, and will even survive a crash of the Temporal Service itself.

These Events are what are used to recreate a Workflow Execution's state in the case of failure.

<PhotoCarousel
  images={[
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.001.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.002.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.003.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.004.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.005.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.006.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.007.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.008.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.009.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.010.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.011.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.012.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.013.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/commands-events/commands-events.014.jpeg',
  ]}
  captions={[
    'NA',
    'In this walkthrough, there will be a running list of the Commands issued with the corresponding Event to the right.',
    "The call to the Activity is the first line of code in the Workflow that causes a Command to be issued. In response to this Command, the Temporal Service creates an Activity Task, adds it to the Task Queue, and appends the `ActivityTaskScheduled` Event to the Event History. This Event is colored blue to indicate that it's the direct result of a Command.",
    'The Service will then dispatch this Activity to an available Worker.',
    'The Service will respond to the poll request with a Task, and the Worker will begin executing the code needed to complete the Task.',
    "The `ActivityTaskStarted` Event is not written to the Event History until a Task closes, because the number of retry attempts is an attribute of the `ActivityTaskStarted` Event. Once the Activity completes, the Temporal Service records another Event in response to the Worker accepting the Task: `ActivityTaskStarted`. This Event is colored pink to indicate that it's an indirect result of the Command. By the way, the `Start-to-Close` Timeout indicates the amount of time that the Activity has to complete.",
    "The Worker executes the code within the Activity Definition, and when that method returns a result, the Worker sends a message to the Temporal Service, notifying it that the Task is complete. To reiterate, this is just a notification, not a Command, because it's not requesting that the Temporal Service do something that will allow the Workflow Execution to progress. In response to this notification, the Temporal Service records another Event: `ActivityTaskCompleted`.",
    'The next statement that results in a Command is the call to start a Timer. It issues a `StartTimer` Command.',
    'The Temporal Service responds after starting a Timer for 30 minutes in the Service, logging a `TimerStarted` Event to the history. It is a direct result of the `StartTimer` Command.',
    'After 30 minutes has elapsed, the Timer is fired on the Temporal Service, which it then records the Event `TimerFired` to the history. The Workflow Execution continues with the next statement, but this is an internal step, meaning that it does not interact with the Temporal Service.',
    'The Worker then reaches the call to the `SendBill` Activity and issues another `ScheduleActivityTask` Command. The Temporal Service adds an Activity Task to the Task Queue and records an `ActivityTaskScheduled` Event to the Event History.',
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
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.001.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.002.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.003.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.004.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.005.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.006.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.007.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.008.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.009.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.011.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.012.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.013.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.015.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.016.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.017.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.018.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.019.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.021.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.022.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.024.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.025.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.026.jpeg',
    'https://learn.temporal.io/courses/temporal-102/go/event-history-walkthrough/history-walkthrough/history-walkthrough.027.jpeg',
