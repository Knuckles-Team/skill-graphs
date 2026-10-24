- If the Activity function throws an error or retryable Failure, the Temporal Service schedules an Activity Task retry to be added to the Task Queue (unless you’ve reached the Maximum Attempts value of the [Retry Policy](/encyclopedia/retry-policies), in which case the Temporal Service adds [ActivityTaskStarted](/references/events#activitytaskstarted) and [ActivityTaskFailed](/references/events#activitytaskfailed) to Event History).
- If the Activity’s [Start-to-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout) passes before the Activity function returns or throws, the Temporal Service schedules a retry.
- If the Activity’s [Schedule-to-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout) passes before Activity Execution is complete, or if [Schedule-to-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout) passes before a Worker gets the Activity Task, the Temporal Service writes [ActivityTaskTimedOut](/references/events#activitytasktimedout) to Event History.
- If the Activity is [canceled](/activity-execution#cancellation), the Temporal Service writes [ActivityTaskCancelRequested](/references/events#activitytaskcancelrequested) to Event History, and if the Activity accepts cancellation, the Temporal Service writes [ActivityTaskCanceled](/references/events#activitytaskcanceled).

:::note

While the Activity is running and retrying, [ActivityTaskScheduled](/references/events#activitytaskscheduled) is the only Activity-related Event in History: [ActivityTaskStarted](/references/events#activitytaskstarted) is written along with a terminal Event like [ActivityTaskCompleted](/references/events#activitytaskcompleted) or [ActivityTaskFailed](/references/events#activitytaskfailed).

:::

### What is an Event History? {/* #event-history */}

An append-only log of [Events](#event) for your application.

- Event History is durably persisted by the Temporal service, enabling seamless recovery of your application state from crashes or failures.
- It also serves as an audit log for debugging.

### Event History limits {/* #event-history-limits */}

The Temporal Service stores the complete Event History for the entire lifecycle of a Workflow Execution.

The Temporal Service logs a [warning after 10,240 Events](/workflow-execution/limits) and periodically logs additional warnings as new Events are added.

The Workflow Execution is terminated when the Event History:

- exceeds 51,200 Events.
- contains more than 2000 Updates.
- contains more than 10000 Signals.

To avoid hitting these limits, you can use the [Continue-As-New](/workflow-execution/continue-as-new) feature to close the current Workflow Execution and create a new one.

### Event loop {/* #event-loop */}

A Workflow Execution is made up of a sequence of [Events](#event) called an [Event History](#event-history).
Events are created by the Temporal Service in response to either Commands or actions requested by a Temporal Client (such as a request to spawn a Workflow Execution).

<CaptionedImage
    src="/diagrams/workflow-execution-swim-lane-01.svg"
    title="Workflow Execution" />

## Time constraints {/* #time-constraints */}

**Is there a limit to how long Workflows can run?**

No, there is no time constraint on how long a Workflow Execution can run.

However, if your Workflow will perform many actions, or will receive many messages, it can run into [Event History limits](#event-history-limits).

It can also hit [Workflow Versioning](/workflow-definition#workflow-versioning) and other backwards incompatibility problems.

For these reasons, it can be a good idea to [Continue-As-New](/workflow-execution/continue-as-new) periodically.

## What is a Reset? {/* #reset */}

A Reset terminates a [Workflow Execution](/workflow-execution) and creates a new Workflow Execution with the same [Workflow Type](/workflow-definition#workflow-type) and [Workflow ID](/workflow-execution/workflowid-runid).
The [Event History](/workflow-execution/event#event-history) is copied from the original execution up to and including the reset point.
The new execution continues from the reset point. Valid reset points are: `WorkflowTaskStarted`, `WorkflowTaskCompleted`, `WorkflowTaskTimedOut`, and `WorkflowTaskFailed`.
Signals in the original history can be optionally copied to the new history, whether they appear after the reset point or not.

## What is a Side Effect? {/* #side-effect */}

:::note

Side Effects are included in the Go, Java, and PHP SDKs.
They are not included in other SDKs.
[Local Activities](/local-activity) fit the same use case and are slightly less resource intensive.

:::

A Side Effect is a way to execute a short, non-deterministic code snippet, such as generating a UUID, that executes the provided function once and records its result into the Workflow Execution Event History.

A Side Effect does not re-execute upon replay, but instead returns the recorded result.

Do not ever have a Side Effect that could fail, because failure could result in the Side Effect function executing more than once.
If there is any chance that the code provided to the Side Effect could fail, use an Activity.

## What is Principal Attribution? {/* #principal-attribution */}

<ReleaseNoteHeader type="prerelease">
  Email addresses can be displayed, which may be considered Personally Identifiable information (PII data), and should be handled according to your organization’s privacy, access control, logging, and retention policies.
</ReleaseNoteHeader>

Principal Attribution for Workflow Executions is a server-derived set of non-spoofable `Principal` fields for Event history events.

The `Principal` fields represent the authenticated principal responsible for a [dataplane](/cloud/overview#data-plane-and-control-plane) execution action.
This allows for identification of the entity that took a given action.

This is especially valuable for:

- compliance and audit use cases
- incident investigation and root cause analysis
- access governance and internal accountability

### Temporal Cloud

When enabled, Temporal Cloud populates the `Principal` value (with `Principal Type` and `Principal Name` fields).

Possible values are as follows:

| Type | Name |
| ---- | ---- |
| `users` | user email address |
| `service-accounts` | service account name |
| `mtls` | Common Name (CN) or Subject Domain Name (DN) if CN is not present |
| `temporal` | Temporal internal services |

Anyone who has permission to read Event history in the Namespace (ReadOnly access and above) can see the Principal (and the metadata such as email address).

To enable Principal Attribution for a Namespace, contact [Temporal Cloud support](https://docs.temporal.io/cloud/support#support-ticket).

### Self-hosted Temporal

In self-hosted Temporal, you can control Principal Attribution with a dynamic config flag scoped to the Namespace.
When enabled, the Principal returned by the `Authorizer` is stamped on Event history events.
To enable, set `frontend.enablePrincipalPropagation` to `true` for the appropriate Namespace.

When using the default `Authorizer` with the default JWT `ClaimMapper`, the following values are populated:

| Type | Name |
| ---- | ---- |
| `jwt ` | value of the JWT `sub` claim |
| `temporal` | `internal` (for internal frontend requests) |

A custom `Authorizer` must set the Principal field on `authorization.Result` for the request to be attributed.
Custom `ClaimMapper` implementations control the `AuthType` and `Subject` values that the default `Authorizer` then copies into the `Principal`.

---

## Workflow Execution limits

This page discusses [Workflow Execution limits](#workflow-execution-limits), [Workflow Execution Callback limits](#workflow-execution-callback-limits), and [Nexus Operation limits](#workflow-execution-nexus-operation-limits).

## Limits {/* #workflow-execution-limits */}

There is no limit to the number of concurrent Workflow Executions, albeit you must abide by the Workflow Execution's Event History limit.

:::caution

As a precautionary measure, the Workflow Execution's Event History is limited to [51,200 Events](https://github.com/temporalio/temporal/blob/e3496b1c51bfaaae8142b78e4032cc791de8a76f/service/history/configs/config.go#L382) or [50 MB](https://github.com/temporalio/temporal/blob/e3496b1c51bfaaae8142b78e4032cc791de8a76f/service/history/configs/config.go#L380) and will warn you after 10,240 Events or 10 MB.

:::

There is also a limit to the number of certain types of incomplete operations.

Each in-progress Activity generates a metadata entry in the Workflow Execution's mutable state.
Too many entries in a single Workflow Execution's mutable state causes unstable persistence.
To protect the system, Temporal enforces a maximum number of incomplete Activities, Child Workflows, Signals, or Cancellation requests per Workflow Execution (by default, 2,000 for each type of operation).
Once the limit is reached for a type of operation, if the Workflow Execution attempts to start another operation of that type (by producing a `ScheduleActivityTask`, `StartChildWorkflowExecution`, `SignalExternalWorkflowExecution`, or `RequestCancelExternalWorkflowExecution` Command), it will be unable to (the Workflow Task Execution will fail and get retried).

These limits are set with the following [dynamic configuration keys](https://github.com/temporalio/temporal/blob/main/service/history/configs/config.go):

- `NumPendingActivitiesLimit`
- `NumPendingChildExecutionsLimit`
- `NumPendingSignalsLimit`
- `NumPendingCancelRequestsLimit`

## Workflow Execution Callback limits {/* #workflow-execution-callback-limits */}

There is a limit to the total number of Workflow Callbacks that may be attached to a single Workflow Execution.
Attaching [multiple Nexus callers to a handler Workflow](/nexus/operations#attaching-multiple-nexus-callers) may exceed these limits.

These limits can be set with the following dynamic configuration keys:
- [MaxCallbacksPerWorkflow](https://github.com/temporalio/temporal/blob/3b626075691c483871630d4a4df266e783f86328/common/dynamicconfig/constants.go#L998)
- [MaxCHASMCallbacksPerWorkflow](https://github.com/temporalio/temporal/blob/3b626075691c483871630d4a4df266e783f86328/common/dynamicconfig/constants.go#L1005)

## Workflow Execution Nexus Operation Limits {/* #workflow-execution-nexus-operation-limits */}

There is a limit to the maximum number of Nexus Operations in a Workflow before Continue-As-New is required.
Each in-progress Nexus Operation generates a metadata entry in the Workflow Execution's mutable state.
Too many entries in a single Workflow Execution's mutable state causes unstable persistence.
To protect the system, Temporal enforces a maximum number of incomplete Nexus Operation requests per Workflow Execution (by default, 30 Nexus Operations).
Once the limit is reached for a type of operation, if the Workflow Execution attempts to start another Nexus operation (by producing a ScheduleNexusOperation), it will be unable to do so (the Workflow Task Execution will fail and get retried).

These limits are set with the following [dynamic configuration keys](https://github.com/temporalio/temporal/blob/de7c8879e103be666a7b067cc1b247f0ac63c25c/components/nexusoperations/config.go#L38):

- MaxConcurrentOperations

---

## Timers and Start Delays

This page discusses [Timer](#timer) and [Start Delay](#delay-workflow-execution).

## What is a Timer? {/* #timer */}

Temporal SDKs offer Timer APIs so that Workflow Executions are deterministic in their handling of time values.

Timers in Temporal are persisted, meaning that even if your Worker or Temporal Service is down when the time period completes, as soon as your Worker and Temporal Service become available, the call that is awaiting the Timer in your Workflow code will resolve, causing execution to proceed.
Timers are reliable and efficient.
Workers consume no additional resources while waiting for a Timer to fire, so a single Worker can await millions of Timers concurrently.

- [How to set Timers in Go](/develop/go/workflows/timers)
- [How to set Timers in Java](/develop/java/workflows/timers)
- [How to set Timers in PHP](/develop/php/workflows/timers)
- [How to set Timers in Python](/develop/python/workflows/timers)
- [How to set Timers in TypeScript](/develop/typescript/workflows/timers)
- [How to set Timers in .NET](/develop/dotnet/workflows/timers)

The duration of a Timer is fixed, and your Workflow might specify a value as short as one second or as long as several years. Although it's possible to specify an extremely precise duration, such as 36 milliseconds or 15.072 minutes, your Workflows should not rely on sub-second accuracy for Timers.

We recommend that you consider the duration as a minimum time, one which will be rounded up slightly due to the latency involved with scheduling and firing the Timer.
For example, setting a Timer for 11.97 seconds is guaranteed to delay execution for at least that long, but will likely be closer to 12 seconds in practice.

## What is a Start Delay? {/* #delay-workflow-execution */}

:::tip COMPATIBILITY

Start Delay Workflow Execution is incompatible with both [Schedules](/schedule) and [Cron Jobs](/cron-job).

:::

Start Delay determines the amount of time to wait before initiating a Workflow Execution.
This is useful if you have a Workflow you want to schedule out in the future, but only want it to execute once: in comparison to reoccurring Workflows using Schedules.

If the Workflow receives a Signal-With-Start or Update-With-Start during the delay, it dispatches a Workflow Task and the remaining delay is bypassed. If the Workflow receives a [Signal](/sending-messages#sending-signals) during the delay that is not a Signal-With-Start, the Signal does not interrupt the delay, and the Workflow continues to be delayed until the delay expires or a Signal-With-Start is received.

A delayed-start Workflow can be triggered with an [Update](/sending-messages#sending-updates). This is because a Workflow Task needs to be scheduled to deliver an Update to Worker. Once a Workflow Task is scheduled, the Workflow is unblocked. Delay start works by not scheduling the first Workflow Task on Workflow creation.

You can delay the dispatch of the initial Workflow Execution by setting this option in the Workflow Options field of your chosen SDK. This delay only applies to the initial Workflow Execution and does not affect subsequent executions, such as when the Workflow Continues-as-New.

---

## Temporal Workflow Execution overview

This page provides an overview of Workflow Execution:

- [What is a Workflow Execution?](#workflow-execution)
- [Replay](#replay)
- [Commands and awaitables](#commands-awaitables)
- [What is a Command?](#command)
- [Checking Workflow Execution Status](#workflow-execution-status)
- [Workflow Execution Chain](#workflow-execution-chain)
- [Memo](#memo)
- [State Transition](#state-transition)

## What is a Workflow Execution? {/* #workflow-execution */}

While the Workflow Definition is the code that defines the Workflow, the Workflow Execution is created by executing that code.
A Temporal Workflow Execution is a durable, reliable, and scalable function execution.
It is the main unit of execution of a [Temporal Application](/temporal#temporal-application).

- [How to start a Workflow Execution using temporal](/cli/command-reference/workflow#start)
- [How to start a Workflow Execution using the Go SDK](/develop/go/client/temporal-client#start-workflow-execution)
- [How to start a Workflow Execution using the Java SDK](/develop/java/client/temporal-client#start-workflow-execution)
- [How to start a Workflow Execution using the PHP SDK](/develop/php/client/temporal-client#start-workflow-execution)
- [How to start a Workflow Execution using the Python SDK](/develop/python/client/temporal-client#start-workflow-execution)
- [How to start a Workflow Execution using the TypeScript SDK](/develop/typescript/client/temporal-client#start-workflow-execution)
- [How to start a Workflow Execution using the .NET SDK](/develop/dotnet/client/temporal-client#start-workflow)

Each Temporal Workflow Execution has exclusive access to its local state.
It executes concurrently to all other Workflow Executions, and communicates with other Workflow Executions through [Signals](/sending-messages#sending-signals) and the environment through [Activities](/activities).
While a single Workflow Execution has limits on size and throughput, a Temporal Application can consist of millions to billions of Workflow Executions.

**Durability**

Durability is the absence of an imposed time limit.

A Workflow Execution is durable because it executes a Temporal Workflow Definition (also called a Temporal Workflow Function), your application code, effectively once and to completion—whether your code executes for seconds or years.

**Reliability**

Reliability is responsiveness in the presence of failure.

A Workflow Execution is reliable, because it is fully recoverable after a failure.
The Temporal Platform ensures the state of the Workflow Execution persists in the face of failures and outages and resumes execution from the latest state.

**Scalability**

Scalability is responsiveness in the presence of load.

A single Workflow Execution is limited in size and throughput but is scalable because it can [Continue-As-New](/workflow-execution/continue-as-new) in response to load.
A Temporal Application is scalable because the Temporal Platform is capable of supporting millions to billions of Workflow Executions executing concurrently, which is realized by the design and nature of the [Temporal Service](/temporal-service) and [Worker Processes](/workers#worker-process).

### Replays {/* #replay */}

A Replay is the method by which a Workflow Execution resumes making progress. During a Replay the Commands that are generated are checked against an existing Event History. Replays are necessary and often happen to give the effect that Workflow Executions are resumable, reliable, and durable.

For more information, see [Deterministic constraints](/workflow-definition#deterministic-constraints).

If a failure occurs, the Workflow Execution picks up where the last recorded event occurred in the Event History.

- [How to use Replay APIs using the Go SDK](/develop/go/best-practices/testing-suite#replay)
- [How to use Replay APIs using the Java SDK](/develop/java/best-practices/testing-suite#replay)
- [How to use Replay APIs using the Python SDK](/develop/python/best-practices/testing-suite#replay)
- [How to use Replay APIs using the TypeScript SDK](/develop/typescript/best-practices/testing-suite#replay)
- [How to use Replay APIs using the .NET SDK](/develop/dotnet/best-practices/testing-suite#replay)

### Commands and awaitables {/* #commands-awaitables */}

A Workflow Execution does two things:

1. Issue [Commands](#command).
2. Wait on an Awaitables (often called Futures).

<CaptionedImage
    src="/diagrams/workflow-execution-progession-simple.svg"
    title="Command generation and waiting" />

Commands are issued and Awaitables are provided by the use of Workflow APIs in the [Workflow Definition](/workflow-definition).

Commands are generated whenever the Workflow Function is executed.
The Worker Process supervises the Command generation and makes sure that it maps to the current Event History.
(For more information, see [Deterministic constraints](/workflow-definition#deterministic-constraints).)
The Worker Process batches the Commands and then suspends progress to send the Commands to the Temporal Service whenever the Workflow Function reaches a place where it can no longer progress without a result from an Awaitable.

A Workflow Execution may only ever block progress on an Awaitable that is provided through a Temporal SDK API.
Awaitables are provided when using APIs for the following:

- Awaiting: Progress can block using explicit "Await" APIs.
- Requesting cancellation of another Workflow Execution: Progress can block on confirmation that the other Workflow Execution is cancelled.
- Sending a [Signal](/sending-messages#sending-signals): Progress can block on confirmation that the Signal sent.
- Spawning a [Child Workflow Execution](/child-workflows): Progress can block on confirmation that the Child Workflow Execution started, and on the result of the Child Workflow Execution.
- Spawning an [Activity Execution](/activity-execution): Progress can block on the result of the Activity Execution.
- Starting a Timer: Progress can block until the Timer fires.

### What is a Command? {/* #command */}

A Command is a requested action issued by a [Worker](/workers#worker) to the [Temporal Service](/temporal-service) after a [Workflow Task Execution](/tasks#workflow-task-execution) completes.

The action that the Temporal Service takes is recorded in the [Workflow Execution's](#workflow-execution) [Event History](/workflow-execution/event#event-history) as an [Event](/workflow-execution/event).
The Workflow Execution can await on some of the Events that come as a result from some of the Commands.

Commands are generated by the use of Workflow APIs in your code. During a Workflow Task Execution there may be several Commands that are generated.
The Commands are batched and sent to the Temporal Service as part of the Workflow Task Execution completion request, after the Workflow Task has progressed as far as it can with the Workflow function.
There will always be [WorkflowTaskStarted](/references/events#workflowtaskstarted) and [WorkflowTaskCompleted](/references/events#workflowtaskcompleted) Events in the Event History when there is a Workflow Task Execution completion request.

<CaptionedImage
    src="/diagrams/commands.svg"
    title="Commands are generated by the use of Workflow APIs in your code" />

Commands are described in the [Command reference](/references/commands) and are defined in the [Temporal gRPC API](https://github.com/temporalio/api/blob/main/temporal/api/command/v1/message.proto).

### Status {/* #workflow-execution-status */}

A Workflow Execution can be either _Open_ or _Closed_.

<CaptionedImage
    src="/diagrams/workflow-execution-statuses.svg"
    title="Workflow Execution statuses" />

#### Open

An _Open_ status means that the Workflow Execution is able to make progress.

- Running: The only Open status for a Workflow Execution.
  When the Workflow Execution is Running, it is either actively progressing or is waiting on something.

#### Closed

A _Closed_ status means that the Workflow Execution cannot make further progress because of one of the following reasons:

- Cancelled: The Workflow Execution successfully handled a cancellation request.
- Completed: The Workflow Execution has completed successfully.
- Continued-As-New: The Workflow Execution [Continued-As-New](/workflow-execution/continue-as-new).
- Failed: The Workflow Execution returned an error and failed.
- Terminated: The Workflow Execution was terminated.
- Timed Out: The Workflow Execution reached a timeout limit.

### Workflow Execution Chain {/* #workflow-execution-chain */}

A Workflow Execution Chain is a sequence of Workflow Executions that share the same Workflow Id.
Each link in the Chain is often called a Workflow Run.
Each Workflow Run in the sequence is connected by one of the following:

- [Continue-As-New](/workflow-execution/continue-as-new)
- [Retries](/encyclopedia/retry-policies)
- [Temporal Cron Job](/cron-job)

A Workflow Execution is uniquely identified by its [Namespace](/namespaces), [Workflow Id](/workflow-execution/workflowid-runid#workflow-id), and [Run Id](/workflow-execution/workflowid-runid#run-id).

The [Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout) applies to a Workflow Execution Chain.
The [Workflow Run Timeout](/encyclopedia/detecting-workflow-failures#workflow-run-timeout) applies to a single Workflow Execution (Workflow Run).

## What is a Memo? {/* #memo */}

A Memo is a non-indexed set of Workflow Execution metadata that developers supply at start time or in Workflow code and that is returned when you describe or list Workflow Executions.

The primary purpose of using a Memo is to enhance the organization and management of Workflow Executions.
Add your own metadata, such as notes or descriptions, to a Workflow Execution, which lets you annotate and categorize Workflow Executions based on developer-defined criteria.
This feature is particularly useful when dealing with numerous Workflow Executions because it facilitates the addition of context, reminders, or any other relevant information that aids in understanding or tracking the Workflow Execution.

:::note Use Memos judiciously

Memos shouldn't store data that's critical to the execution of a Workflow, for some of the following reasons:

- Unlike Workflow inputs, Memos lack type safety
- Memos are subject to eventual consistency and may not be immediately available
- Excessive reliance on Memos hides mutable state from the Workflow Execution History

:::

## What is a State Transition? {/* #state-transition */}

A State Transition is a unit of progress made by a [Workflow Execution](#workflow-execution).
Each State Transition is recorded in a persistence store.

Some operations, such as [Activity Heartbeats](/encyclopedia/detecting-activity-failures#activity-heartbeat), require only one or two State Transitions each. With an Activity Heartbeat, there are two: the Activity Heartbeat and a Timer.

