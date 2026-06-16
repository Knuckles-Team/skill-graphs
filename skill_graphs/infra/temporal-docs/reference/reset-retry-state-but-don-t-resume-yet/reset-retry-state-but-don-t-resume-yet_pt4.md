
To decode output when using the Web UI and the Temporal CLI, use a [Codec Server](/codec-server).

Note that a remote data encoder is a separate system with access to your encryption keys and exposes APIs to encode and decode any data.
Evaluate and ensure that your remote data encoder endpoints are secured and only authorized users have access to them.

Samples:

- [Go](https://github.com/temporalio/samples-go/tree/main/codec-server)
- [Java](https://github.com/temporalio/sdk-java/tree/master/temporal-remote-data-encoder)
- [Python](https://github.com/temporalio/samples-python/tree/main/encryption)
- [TypeScript](https://github.com/temporalio/samples-typescript/tree/main/encryption)

---

## Detecting Activity failures

A Workflow can detect different kinds of Activity Execution failures through the following timeouts:

- [Schedule-To-Start Timeout](#schedule-to-start-timeout)
- [Start-To-Close Timeout](#start-to-close-timeout)
- [Schedule-To-Close Timeout](#schedule-to-close-timeout)
- [Activity Heartbeats](#activity-heartbeat)

## Schedule-To-Start Timeout {/* #schedule-to-start-timeout */}

**What is a Schedule-To-Start Timeout in Temporal?**

A Schedule-To-Start Timeout is the maximum amount of time that is allowed from when an [Activity Task](/tasks#activity-task) is scheduled (that is, placed in a Task Queue) to when a [Worker](/workers#worker) starts (that is, picks up from the Task Queue) that Activity Task.
In other words, it's a limit for how long an Activity Task can be enqueued.

<RelatedReadContainer>
  <RelatedReadItem path="/develop/go/activities/timeouts" text="Set a Schedule-To-Start Timeout using the Go SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/java/activities/timeouts" text="Set a Schedule-To-Start Timeout using the Java SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/php/activities/timeouts#activity-timeouts" text="Set a Schedule-To-Start Timeout using the PHP SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/python/activities/timeouts" text="Set a Schedule-To-Start Timeout using the Python SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/typescript/activities/timeouts" text="Set a Schedule-To-Start Timeout using the TypeScript SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/dotnet/activities/timeouts" text="Set a Schedule-To-Start Timeout using the .NET SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/rust/activities/timeouts" text="Set a Schedule-To-Start Timeout using the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

The moment that the Task is picked by the Worker, from the Task Queue, is considered to be the start of the Activity Task Execution for the purposes of the Schedule-To-Start Timeout and associated metrics.
This definition of "Start" avoids issues that a clock difference between the Temporal Service and a Worker might create.

<CaptionedImage
    src="/diagrams/schedule-to-start-timeout.svg"
    title="Schedule-To-Start Timeout period" />

"Schedule" in Schedule-To-Start and Schedule-To-Close have different frequency guarantees.

The Schedule-To-Start Timeout is enforced for each Activity Task, whereas the Schedule-To-Close Timeout is enforced once per Activity Execution.
Thus, "Schedule" in Schedule-To-Start refers to the scheduling moment of _every_ Activity Task in the sequence of Activity Tasks that make up the Activity Execution, while
"Schedule" in Schedule-To-Close refers to the _first_ Activity Task in that sequence.

A [Retry Policy](/encyclopedia/retry-policies) attached to an Activity Execution retries an Activity Task.

<CaptionedImage
    src="/diagrams/schedule-to-start-timeout-with-retry.svg"
    title="Start-To-Close Timeout period with retries" />

This timeout has two primary use cases:

1. Detect whether an individual Worker has crashed.
2. Detect whether the fleet of Workers polling the Task Queue is not able to keep up with the rate of Activity Tasks.

**The default Schedule-To-Start Timeout is ∞ (infinity).**

If this timeout is used, we recommend setting this timeout to the maximum time a Workflow Execution is willing to wait for an Activity Execution in the presence of all possible Worker outages, and have a concrete plan in place to reroute Activity Tasks to a different Task Queue.
This timeout **does not** trigger any retries regardless of the Retry Policy, as a retry would place the Activity Task back into the same Task Queue.
We do not recommend using this timeout unless you know what you are doing.

In most cases, we recommend monitoring the `temporal_activity_schedule_to_start_latency` metric to know when Workers slow down picking up Activity Tasks, instead of setting this timeout.

## Start-To-Close Timeout {/* #start-to-close-timeout */}

**What is a Start-To-Close Timeout in Temporal?**

A Start-To-Close Timeout is the maximum time allowed for a single [Activity Task Execution](/tasks#activity-task-execution).

<RelatedReadContainer>
  <RelatedReadItem path="/develop/go/activities/timeouts" text="Set a Start-To-Close Timeout using the Go SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/java/activities/timeouts" text="Set a Start-To-Close Timeout using the Java SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/php/activities/timeouts#activity-timeouts" text="Set a Start-To-Close Timeout using the PHP SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/python/activities/timeouts" text="Set a Start-To-Close Timeout using the Python SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/typescript/activities/timeouts" text="Set a Start-To-Close Timeout using the TypeScript SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/dotnet/activities/timeouts" text="Set a Start-To-Close Timeout using the .NET SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/rust/activities/timeouts" text="Set a Start-To-Close Timeout using the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

**The default Start-To-Close Timeout is the same as the default [Schedule-To-Close Timeout](#schedule-to-close-timeout).**

An Activity Execution must have either this timeout (Start-To-Close) or the [Schedule-To-Close Timeout](#schedule-to-close-timeout) set.
We recommend always setting this timeout; however, make sure that Start-To-Close Timeout is always set to be longer than the maximum possible time for the Activity Execution to complete.
For long running Activity Executions, we recommend also using [Activity Heartbeats](#activity-heartbeat) and [Heartbeat Timeouts](#heartbeat-timeout).

:::tip

We strongly recommend setting a Start-To-Close Timeout.

The Temporal Server doesn't detect failures when a Worker loses communication with the Server or crashes.
Therefore, the Temporal Server relies on the Start-To-Close Timeout to force Activity retries.

:::

The main use case for the Start-To-Close timeout is to detect when a Worker crashes after it has started executing an Activity Task.

<CaptionedImage
    src="/diagrams/start-to-close-timeout.svg"
    title="Start-To-Close Timeout period" />

A [Retry Policy](/encyclopedia/retry-policies) attached to an Activity Execution retries an Activity Task Execution.
Thus, the Start-To-Close Timeout is applied to each Activity Task Execution within an Activity Execution.

If the first Activity Task Execution returns an error the first time, then the full Activity Execution might look like this:

<CaptionedImage
    src="/diagrams/start-to-close-timeout-with-retry.svg"
    title="Start-To-Close Timeout period with retries" />

If this timeout is reached, the following actions occur:

- An [ActivityTaskTimedOut](/references/events#activitytasktimedout) Event is written to the Workflow Execution's mutable state.
- If a Retry Policy dictates a retry, the Temporal Service schedules another Activity Task.
  - The attempt count increments by 1 in the Workflow Execution's mutable state.
  - The Start-To-Close Timeout timer is reset.

## Schedule-To-Close Timeout {/* #schedule-to-close-timeout */}

**What is a Schedule-To-Close Timeout in Temporal?**

A Schedule-To-Close Timeout is the maximum amount of time allowed for the overall [Activity Execution](/activity-execution), from when the first [Activity Task](/tasks#activity-task) is scheduled to when the last Activity Task, in the chain of Activity Tasks that make up the Activity Execution, reaches a Closed status.

<RelatedReadContainer>
  <RelatedReadItem path="/develop/go/activities/timeouts" text="Set a Schedule-To-Close Timeout using the Go SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/java/activities/timeouts" text="Set a Schedule-To-Close Timeout using the Java SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/php/activities/timeouts#activity-timeouts" text="Set a Schedule-To-Close Timeout using the PHP SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/python/activities/timeouts" text="Set a Schedule-To-Close Timeout using the Python SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/typescript/activities/timeouts" text="Set a Schedule-To-Close Timeout using the TypeScript SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/dotnet/activities/timeouts" text="Set a Schedule-To-Close Timeout using the .NET SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/rust/activities/timeouts" text="Set a Schedule-To-Close Timeout using the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

<CaptionedImage
    src="/diagrams/schedule-to-close-timeout.svg"
    title="Schedule-To-Close Timeout period" />

Example Schedule-To-Close Timeout period for an Activity Execution that has a chain Activity Task Executions:

<CaptionedImage
    src="/diagrams/schedule-to-close-timeout-with-retry.svg"
    title="Schedule-To-Close Timeout period with a retry" />

**The default Schedule-To-Close Timeout is ∞ (infinity).**

An Activity Execution must have either this timeout (Schedule-To-Close) or [Start-To-Close](#start-to-close-timeout) set.
This timeout can be used to control the overall duration of an Activity Execution in the face of failures (repeated Activity Task Executions), without altering the Maximum Attempts field of the Retry Policy.

:::tip

We strongly recommend setting a Start-To-Close Timeout.

The Temporal Server doesn't detect failures when a Worker loses communication with the Server or crashes.
Therefore, the Temporal Server relies on the Start-To-Close Timeout to force Activity retries.

:::

## Activity Heartbeat {/* #activity-heartbeat */}

**What is an Activity Heartbeat in Temporal?**

An Activity Heartbeat is a ping from the Worker that is executing the Activity to the Temporal Service.
Each ping informs the Temporal Service that the Activity Execution is making progress and the Worker has not crashed.

<RelatedReadContainer>
  <RelatedReadItem path="/develop/go/activities/timeouts#activity-heartbeats" text="Heartbeat an Activity using the Go SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/java/activities/timeouts#activity-heartbeats" text="Heartbeat an Activity using the Java SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/php/activities/timeouts#activity-heartbeats" text="Heartbeat an Activity using the PHP SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/python/activities/timeouts#activity-heartbeats" text="Heartbeat an Activity using the Python SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/typescript/activities/timeouts#activity-heartbeat-timeout" text="Heartbeat an Activity using the TypeScript SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/dotnet/activities/timeouts#activity-heartbeats" text="Heartbeat an Activity using the .NET SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/rust/activities/timeouts#activity-heartbeats" text="Heartbeat an Activity using the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

Activity Heartbeats work in conjunction with a [Heartbeat Timeout](#heartbeat-timeout).

Activity Heartbeats are implemented within the Activity Definition.
Custom progress information can be included in the Heartbeat which can then be used by the Activity Execution should a retry occur.

An Activity Heartbeat can be recorded as often as needed (e.g. once a minute or every loop iteration).
It is often a good practice to Heartbeat on anything but the shortest Activity Execution.
Temporal SDKs control the rate at which Heartbeats are sent to the Temporal Service.

Heartbeating is not required from [Local Activities](/local-activity), and does nothing.

For _long-running_ Activities, we recommend using a relatively short Heartbeat Timeout and a frequent Heartbeat.
That way if a Worker fails it can be handled in a timely manner.

A Heartbeat can include an application layer payload that can be used to _save_ Activity Execution progress.
If an [Activity Task Execution](/tasks#activity-task-execution) times out due to a missed Heartbeat, the next Activity Task can access and continue with that payload.

Activity Cancellations are delivered to Activities from the Temporal Service when they Heartbeat. Activities that don't Heartbeat can't receive a Cancellation.
Heartbeat throttling may lead to Cancellation getting delivered later than expected.

### Throttling

Heartbeats may not always be sent to the Temporal Service—they may be throttled by the Worker.
The throttle interval is the smaller of the following:

- If `heartbeatTimeout` is provided, `heartbeatTimeout * 0.8`; otherwise, `defaultHeartbeatThrottleInterval`
- `maxHeartbeatThrottleInterval`

`defaultHeartbeatThrottleInterval` is 30 seconds by default, and `maxHeartbeatThrottleInterval` is 60 seconds by default.
Each can be set in Worker options.

Throttling is implemented as follows:

- After sending a Heartbeat, the Worker sets a timer for the throttle interval.
- The Worker stops sending Heartbeats, but continues receiving Heartbeats from the Activity and remembers the most recent one.
- When the timer fires, the Worker:
  - Sends the most recent Heartbeat.
  - Sets the timer again.

Throttling allows the Worker to reduce network traffic and load on the Temporal Service by suppressing Heartbeats that aren’t necessary to prevent a Heartbeat Timeout.
Throttling does not apply to the final Heartbeat message in the case of Activity Failure.
If an Activity fails just after recording progress information in a Heartbeat message, that progress information will be available during the next retry attempt, provided that the Worker itself did not crash before delivering it to the Temporal Service.

### Which Activities should Heartbeat?

Heartbeating is best thought about not in terms of time, but in terms of "How do you know you are making progress?"
For short-term operations, progress updates are not a requirement.
However, checking the progress and status of Activity Executions that run over long periods is almost always useful.

Consider the following when setting Activity Heartbeats:

- Your underlying task must be able to report definite progress.
  Note that your Workflow cannot read this progress information while the Activity is still executing (or it would have to store it in Event History).
  You can report progress to external sources if you need it exposed to the user.

- Your Activity Execution is long-running, and you need to verify whether the Worker that is processing your Activity is still alive and has not run out of memory or silently crashed.

For example, the following scenarios are suitable for Heartbeating:

- Reading a large file from Amazon S3.
- Running a ML training job on some local GPUs.

And the following scenarios are not suitable for Heartbeating:

- Making a quick API call.
- Reading a small file from disk.

### Heartbeat Timeout {/* #heartbeat-timeout */}

**What is a Heartbeat Timeout in Temporal?**

A Heartbeat Timeout is the maximum time between [Activity Heartbeats](#activity-heartbeat).

<RelatedReadContainer>
  <RelatedReadItem path="/develop/go/activities/timeouts#activity-heartbeats" text="Set a Heartbeat Timeout using the Go SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/java/activities/timeouts#heartbeat-timeout" text="Set a Heartbeat Timeout using the Java SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/php/activities/timeouts#heartbeat-timeout" text="Set a Heartbeat Timeout using the PHP SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/python/activities/timeouts#heartbeat-timeout" text="Set a Heartbeat Timeout using the Python SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/typescript/activities/timeouts#activity-heartbeat-timeout" text="Set a Heartbeat Timeout using the TypeScript SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/dotnet/activities/timeouts#heartbeat-timeout" text="Set a Heartbeat Timeout using the .NET SDK" archetype="feature-guide" />
  <RelatedReadItem path="/develop/rust/activities/timeouts#heartbeat-timeout" text="Set a Heartbeat Timeout using the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

<CaptionedImage
    src="/diagrams/heartbeat-timeout.svg"
    title="Heartbeat Timeout periods" />

If this timeout is reached, the Activity Task fails and a retry occurs if a [Retry Policy](/encyclopedia/retry-policies) dictates it.

---

## Detecting Workflow failures

Each Workflow Timeout controls the maximum duration of a different aspect of a Workflow Execution. Workflow Timeouts are set when starting the Workflow Execution.

Before we continue, we want to note that we generally do not recommend setting Workflow Timeouts, because Workflows are designed to be long-running and resilient.
Instead, setting a Timeout can limit its ability to handle unexpected delays or long-running processes.
If you need to perform an action inside your Workflow after a specific period of time, we recommend using a Timer.

- [Workflow Execution Timeout](#workflow-execution-timeout)
- [Workflow Run Timeout](#workflow-run-timeout)
- [Workflow Task Timeout](#workflow-task-timeout)

## Workflow Execution Timeout {/* #workflow-execution-timeout */}

**What is a Workflow Execution Timeout in Temporal?**

A Workflow Execution Timeout is the maximum time that a Workflow Execution can be executing (have an Open status) including retries and any usage of Continue As New.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/timeouts" text="Set a Workflow Execution Timeout using the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/timeouts" text="Set a Workflow Execution Timeout using the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/timeouts#workflow-timeouts" text="Set a Workflow Execution Timeout using the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/timeouts" text="Set a Workflow Execution Timeout using the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/timeouts" text="Set a Workflow Execution Timeout using the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/timeouts" text="Set a Workflow Execution Timeout using the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/timeouts" text="Set a Workflow Execution Timeout using the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

<CaptionedImage
    src="/diagrams/workflow-execution-timeout.svg"
    title="Workflow Execution Timeout period" />

**The default value is ∞ (infinite).**
If this timeout is reached, the Workflow Execution changes to a Timed Out status.
This timeout is different from the [Workflow Run Timeout](#workflow-run-timeout).
This timeout is most commonly used for stopping the execution of a [Temporal Cron Job](/cron-job) after a certain amount of time has passed.

## Workflow Run Timeout {/* #workflow-run-timeout */}

**What is a Workflow Run Timeout in Temporal?**

A Workflow Run is the instance of a specific Workflow Execution.

Due to the potential for Workflow Retries or Continue-as-New, a Workflow Execution may have multiple Workflow runs. For example, if a Workflow that specifies a Retry Policy initially fails and then succeeds during the next retry attempt, there is a single Workflow Execution that spans two Workflow Runs. Both runs will share the same Workflow ID but have a unique Run ID to distinguish them.

A Workflow Run Timeout restricts the maximum duration of a single Workflow Run. If the Workflow Run Timeout is reached, the Workflow Execution will be Timed Out. Because this Timeout only applies to an individual Workflow Run, this does not include retries or Continue-As-New.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/timeouts" text="Set a Workflow Run Timeout using the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/timeouts" text="Set a Workflow Run Timeout using the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/timeouts#workflow-timeouts" text="Set a Workflow Run Timeout using the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/timeouts" text="Set a Workflow Run Timeout using the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/timeouts" text="Set a Workflow Run Timeout using the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/timeouts" text="Set a Workflow Timeout using the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/timeouts" text="Set a Workflow Timeout using the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

<CaptionedImage
    src="/diagrams/workflow-run-timeout.svg"
    title="Workflow Run Timeout period" />

**The default is set to the same value as the [Workflow Execution Timeout](#workflow-execution-timeout).**
This timeout is most commonly used to limit the execution time of a single [Temporal Cron Job Execution](/cron-job).

If the Workflow Run Timeout is reached, the Workflow Execution will be Timed Out.

## Workflow Task Timeout {/* #workflow-task-timeout */}

**What is a Workflow Task Timeout in Temporal?**

A Workflow Task Timeout is the maximum amount of time allowed for a [Worker](/workers#worker) to execute a [Workflow Task](/tasks#workflow-task) after the Worker has pulled that Workflow Task from the [Task Queue](/task-queue).

This Timeout is primarily available to recognize whether a Worker has gone down so that the Workflow Execution can be recovered on a different Worker.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/timeouts" text="Set a Workflow Task Timeout using the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/timeouts" text="Set a Workflow Task Timeout using the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/timeouts#workflow-timeouts" text="Set a Workflow Task Timeout using the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/timeouts" text="Set a Workflow Task Timeout using the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/timeouts" text="Set a Workflow Task Timeout using the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/timeouts" text="Set a Workflow Task Timeout using the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/timeouts" text="Set a Workflow Task Timeout using the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

<CaptionedImage
    src="/diagrams/workflow-task-timeout.svg"
    title="Workflow Task Timeout period" />

**The default value is 10 seconds.**
This timeout is primarily available to recognize whether a Worker has gone down so that the Workflow Execution can be recovered on a different Worker.
The main reason for increasing the default value is to accommodate a Workflow Execution that has an extensive Workflow Execution History, requiring more than 10 seconds for the Worker to load.
It's worth mentioning that although you can extend the timeout up to the maximum value of 120 seconds, it's not recommended to move beyond the default value.

## Detecting Workflow Task Failures

Use the `TemporalReportedProblems` Search Attribute to detect Workflows with failed Workflow Tasks.
A failed Workflow Task does not cause the Workflow to fail. Some Tasks within a Workflow may be intended to fail.
For example, a Workflow Task may check a remote data source for new messages. If there aren't any, the Task will fail as intended.
If your Task has code to handle the failure, the Workflow will proceed.
However, if your Workflow has a Task that fails and the failure is not handled, the Workflow will continue to run, but will not complete.
Detecting Workflows in this state is a common troubleshooting issue.

To identify Workflows with Task failures, you can use the Temporal Web UI. See [Task Failures View](/web-ui/#task-failures-view) for more details.

You can also detect Workflows with Task failures by searching for the `TemporalReportedProblems` search attribute with your observability tools.
