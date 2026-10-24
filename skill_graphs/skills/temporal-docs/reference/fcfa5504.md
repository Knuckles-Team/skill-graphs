The default is one year, meaning Actions will be taken unless over one year late.
If your Actions are more time-sensitive, you can set the Catchup Window to a smaller value (minimum ten seconds), accepting that an outage longer than the window could lead to missed Actions.
(But you can always [Backfill](#backfill).)

#### Pause-on-failure

If this policy is set, a Workflow Execution started by a Schedule that ends with a failure or timeout (but not Cancellation or Termination) causes the Schedule to automatically pause.

Note that with the `AllowAll` Overlap Policy, this pause might not apply to the next Workflow Execution, because the next Workflow Execution might have started before the failed one finished.
It applies only to Workflow Executions that were scheduled to start after the failed one finished.

### Last completion result

A Workflow started by a Schedule can obtain the completion result from the most recent successful run.
(How you do this depends on the SDK you're using.)

For overlap policies that don't allow overlap, “the most recent successful run” is straightforward to define.
For the `AllowAll` policy, it refers to the run that completed most recently, at the time that the run in question is started.
Consider the following overlapping runs:

```
time -------------------------------------------->
 A     |----------------------|
 B               |-------|
 C                          |---------------|
 D                                |--------------T
```

If D asks for the last completion result at time T, it gets the result of A.
Not B, even though B started more recently, because A completed later.
And not C, even though C completed after A, because the result for D is captured when D is started, not when it's queried.

Failures and timeouts do not affect the last completion result.

:::note

When a Schedule triggers a Workflow that completes successfully and yields a result, the result from the initial Schedule execution can be accessed by the subsequent scheduled execution through `LastCompletionResult`.

Be aware that if, during the subsequent run, the Workflow employs the [Continue-As-New](/workflow-execution/continue-as-new) feature, `LastCompletionResult` won't be accessible for this new Workflow iteration.

It is important to note that the [status](/workflow-execution#workflow-execution-status) of the subsequent run is marked as `Continued-As-New` and not as `Completed`.

:::

:::caution

A scheduled Workflow Execution may complete with a result up to the maximum blob size (2 MiB by default).
However, due to internal limitations, results that are within 1 KiB of this limit cannot be passed to the next execution.
So, for example, a Workflow Execution that returns a result of size 2,096,640 bytes (which is above 2MiB - 1KiB limit)
will be allowed to complete successfully, but that value will not be available as a last completion result.
This limitation may be lifted in the future.

:::

### Last failure

A Workflow started by a Schedule can obtain the details of the failure of the most recent run that ended at the time when the Workflow in question was started. Unlike last completion result, a _successful_ run _does_ reset the last failure.

### Limitations

Internally, a Schedule is implemented as a Workflow.
If you're using Elasticsearch, these Workflow Executions are hidden from normal views.

---

## Temporal Workflow Definition

This page covers the following:

- [What is a Workflow Definition?](/workflow-definition)
- [Determinism and constraints](#deterministic-constraints)
- [Handling code changes and non-deterministic behavior](#non-deterministic-change)
- [Intrinsic non-determinism logic](#intrinsic-nondeterministic-logic)
- [Versioning Workflow code and Patching](#workflow-versioning)
- [Handling unreliable Worker Processes](#unreliable-worker-processes)
- [What is a Workflow Type?](#workflow-type)

A Temporal Workflow defines the overall flow of the application.
Conceptually, a Workflow is a sequence of steps written in a general-purpose programming language.
With Temporal, those steps are defined by writing code, known as a Workflow Definition, and are carried out by running that code, which results in a Workflow Execution.

In day-to-day conversations, the term _Workflow_ might refer to [Workflow Type](#workflow-type), a [Workflow Definition](/workflow-definition), or a [Workflow Execution](/workflow-execution).
Temporal documentation aims to be explicit and differentiate between them.

## What is a Workflow Definition? {/* #workflow-definition */}

A Workflow Definition is the code that defines the Workflow.
It is written with a programming language and corresponding Temporal SDK.
Depending on the programming language, it's typically implemented as a function or an object method and encompasses the end-to-end series of steps of a Temporal application.

Below are different ways to develop a basic Workflow Definition.

<Tabs groupId="basic-workflow-definition" queryString>
<TabItem value="go" label="Go">

**[Workflow Definition in Go](/develop/go/workflows/basics)**

```go
func YourBasicWorkflow(ctx workflow.Context) error {
    // ...
    return nil
}
```

</TabItem>
<TabItem value="java" label="Java">

**[Workflow Definition in Java (Interface)](/develop/java/workflows/basics)**

```java
// Workflow interface
@WorkflowInterface
public interface YourBasicWorkflow {

    @WorkflowMethod
    String workflowMethod(Arguments args);
}
```

**[Workflow Definition in Java (Implementation)](/develop/java/workflows/basics)**

```java
// Workflow implementation
public class YourBasicWorkflowImpl implements YourBasicWorkflow {
    // ...
}
```

</TabItem>
<TabItem value="php" label="PHP">

**[Workflow Definition in PHP (Interface)](/develop/php/workflows/basics)**

```php
#[WorkflowInterface]
interface YourBasicWorkflow {
    #[WorkflowMethod]
    public function workflowMethod(Arguments args);
}
```

**[Workflow Definition in PHP (Implementation)](/develop/php/workflows/basics)**

```php
class YourBasicWorkflowImpl implements YourBasicWorkflow {
    // ...
}
```

</TabItem>
<TabItem value="python" label="Python">

**[Workflow Definition in Python](/develop/python/workflows/basics)**

```Python
@workflow.defn
class YourWorkflow:
    @workflow.run
    async def YourBasicWorkflow(self, input: str) -> str:
        # ...
```

</TabItem>
<TabItem value="typescript" label="Typescript">

**[Workflow Definition in Typescript](/develop/typescript/workflows/basics)**

```Typescript
type BasicWorkflowArgs = {
  param: string;
};

export async function WorkflowExample(
  args: BasicWorkflowArgs,
): Promise<{ result: string }> {
  // ...
}
```

</TabItem>
<TabItem value="dotnet" label=".NET">

**[Workflow Definition in C# and .NET](/develop/dotnet/workflows/basics)**

```csharp
[Workflow]
public class YourBasicWorkflow {

    [WorkflowRun]
    public async Task<string> workflowExample(string param) {
        // ...
    }
}
```

</TabItem>
<TabItem value="rust" label="Rust">

**[Workflow Definition in Rust](/develop/rust/workflows/basics)**

```rust
use temporalio_macros::{workflow, workflow_methods};
use temporalio_sdk::{WorkflowContext, WorkflowContextView, WorkflowResult};

#[workflow]
pub struct YourBasicWorkflow {
    param: String,
}

#[workflow_methods]
impl YourBasicWorkflow {
    #[init]
    fn new(_ctx: &WorkflowContextView, param: String) -> Self {
        Self { param }
    }

    #[run]
    async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
        // ...
        Ok(String::new())
    }
}
```

</TabItem>

</Tabs>

A Workflow Definition may be also referred to as a Workflow Function.
In Temporal's documentation, a Workflow Definition refers to the source for the instance of a Workflow Execution, while a Workflow Function refers to the source for the instance of a Workflow Function Execution.

A Workflow Execution effectively executes once to completion, while a Workflow Function Execution occurs many times during the life of a Workflow Execution.

We strongly recommend that you write a Workflow Definition in a language that has a corresponding Temporal SDK.

### Deterministic constraints {/* #deterministic-constraints */}

A critical aspect of developing Workflow Definitions is ensuring that they are deterministic.
Generally speaking, this means you must take care to ensure that any time your Workflow code is executed it makes the same Workflow API calls in the same sequence, given the same input.
Some changes to those API calls are safe to make.

:::tip Note on determinism

Workflow code must be deterministic to support replay. To handle non-deterministic operations like API calls, LLM/AI invocations, database queries, and other external interactions, put them in Activities. Activities execute outside the replay path and are automatically retried so they don't cause non-determinism errors.

:::

For example, you can change:

- The input parameters, return values, and execution timeouts of Child Workflows and Activities
  - However, it is not safe to change the types or IDs of Child Workflows or Activities
- The input parameters used to Signal an external Workflow
- The duration of Timers (although changing them to 0 is not safe in all SDKs)
- Add or remove calls to Workflow APIs that don't produce [Commands](/workflow-execution#command) (For example - `workflow.GetInfo` in the Go SDK or its equivalent in other SDKs)

The following Workflow API calls all can produce Commands, and thus must not be reordered, added, or removed without proper [Versioning techniques](#workflow-versioning):

- Starting or cancelling a Timer
- Scheduling or cancelling Activity Executions (including local Activities)
- Starting or cancelling Child Workflow executions
- Signalling or cancelling signals to external Workflow Executions
- Scheduling or cancelling Nexus operations
- Ending the Workflow Execution in any way (completing, failing, cancelling, or continuing-as-new)
- `Patched` or `GetVersion` calls for Versioning (although they may be added or removed according to the [patching](#workflow-patching) rules)
- Upserting Workflow Search Attributes
- Upserting Workflow Memos
- Running a `SideEffect` or `MutableSideEffect`

For a complete reference, see the [Command reference](/references/commands).

More formally, the use of certain Workflow APIs in the function is what generates Commands.
Commands tell the Temporal Service which Events to create and add to the Workflow Execution's [Event History](/workflow-execution/event#event-history).
When the Workflow's code [replays](/workflow-execution#replay), the Commands that are emitted are compared with the existing Event History.
If a corresponding Event already exists within the Event History that matches that command, then the Execution progresses.
See [Event History](/encyclopedia/event-history/) for a detailed walkthrough of the process.

For example, using an SDK's "Execute Activity" API generates the [ScheduleActivityTask](/references/commands#scheduleactivitytask) Command.
When this API is called upon re-execution, that Command is compared with the Event that is in the same location within the sequence.
The Event in the sequence must be an [ActivityTaskScheduled](/references/events#activitytaskscheduled) Event, where the Activity name is the same as what is in the Command.

If a generated Command doesn't match what it needs to in the existing Event History, then the Workflow Execution returns a _non-deterministic_ error.

The following are the two reasons why a Command might be generated out of sequence or the wrong Command might be generated altogether:

1. Code changes are made to a Workflow Definition that is in use by a running Workflow Execution.
2. There is intrinsic non-deterministic logic (such as inline random branching).

### Code changes can cause non-deterministic behavior {/* #non-deterministic-change */}

The Workflow Definition can change in very limited ways once there is a Workflow Execution depending on it.
To alleviate non-deterministic issues that arise from code changes, we recommend using [Workflow Versioning](#workflow-versioning).

For example, let's say we have a Workflow Definition that defines the following sequence:

1. Start and wait on a Timer/sleep.
2. Spawn and wait on an Activity Execution.
3. Complete.

We start a Worker and spawn a Workflow Execution that uses that Workflow Definition.
The Worker would emit the [StartTimer](/references/commands#starttimer) Command and the Workflow Execution would become suspended.

Before the Timer is up, we change the Workflow Definition to the following sequence:

1. Spawn and wait on an Activity Execution.
2. Start and wait on a Timer/sleep.
3. Complete.

When the Timer fires, the next Workflow Task will cause the Workflow Function to re-execute.
The first Command the Worker sees would be ScheduleActivityTask Command, which wouldn't match up to the expected [TimerStarted](/references/events#timerstarted) Event.

The Workflow Execution would fail and return a nondeterminism error.

The following are examples of minor changes that would not result in non-determinism errors when re-executing a History which already contain the Events:

- Changing the duration of a Timer, with the following exceptions:
  - In Java, Python, and Go, changing a Timer's duration from or to 0 is a non-deterministic behavior.
  - In .NET, changing a Timer's duration from or to -1 (which means "infinite") is a non-deterministic behavior.
- Changing the arguments to:
  - The Activity Options in a call to spawn an Activity Execution (local or nonlocal).
  - The Child Workflow Options in a call to spawn a Child Workflow Execution.
  - Call to Signal an External Workflow Execution.
- Adding a Signal Handler for a Signal Type that has not been sent to this Workflow Execution.

### Intrinsic non-deterministic logic {/* #intrinsic-nondeterministic-logic */}

Intrinsic non-determinism is when a Workflow Function Execution might emit a different sequence of Commands on re-execution, regardless of whether all the input parameters are the same.

For example, a Workflow Definition can not have inline logic that branches (emits a different Command sequence) based off a local time setting or a random number.
In the representative pseudocode below, the `local_clock()` function returns the local time, rather than Temporal-defined time:

```text
fn your_workflow() {
  if local_clock().is_before("12pm") {
    await workflow.sleep(duration_until("12pm"))
  } else {
    await your_afternoon_activity()
  }
}
```

Each Temporal SDK offers APIs that enable Workflow Definitions to have logic that gets and uses time, random numbers, and data from unreliable resources.
When those APIs are used, the results are stored as part of the Event History, which means that a re-executed Workflow Function will issue the same sequence of Commands, even if there is branching involved.

In other words, all operations that do not purely mutate the Workflow Execution's state should occur through a Temporal SDK API.

For SDK-specific replay-safe APIs and examples (logging, random numbers, time, replay detection), see:

- [Go: Develop Workflow logic](/develop/go/workflows/basics#workflow-logic-requirements)
- [Java: Workflow logic requirements](/develop/java/workflows/basics#workflow-logic-requirements)
- [Python: Develop Workflow logic](/develop/python/workflows/basics#workflow-logic-requirements)
- [TypeScript: Develop Workflow logic](/develop/typescript/workflows/basics#workflow-logic-requirements)
- [.NET: Workflow logic requirements](/develop/dotnet/workflows/basics#workflow-logic-requirements)
- [Ruby: Workflow Logic Requirements](/develop/ruby/workflows/basics#workflow-logic-requirements)
- [Rust: Workflow Logic Requirements](/develop/rust/workflows/basics#workflow-logic-requirements)

### Versioning Workflows {/* #workflow-versioning */}

The Temporal Platform requires that Workflow code (Workflow Definitions) be deterministic in nature.
This requirement means that developers should consider how they plan to handle changes to Workflow code over time.

A versioning strategy is even more important if your Workflow Executions live long enough to run on multiple versions of your Worker. Temporal Platform provides Workflow Versioning APIs.

Temporal offers two Versioning strategies:

- [Worker Versioning](#worker-versioning): keep Workers tied to specific code revisions, so that old Workers can run old code paths and new Workers can run new code paths.

:::note
Support for the experimental method of Worker Versioning prior to 2025 will be removed from Temporal Server in March 2026. Refer to the [latest Worker Versioning docs](/worker-versioning) for guidance.
:::

- [Versioning with patching](#workflow-patching): make sure your code changes are compatible across versions of your Workflow.

You can use either strategy, or a combination.

#### Worker Versioning {/* #worker-versioning */}

This is the **recommended** way to handle versioning and users see improved error rates when adopting it. To learn more about Worker Versioning, see our [Worker Versioning in production](production-deployment/worker-deployments/worker-versioning) page.

#### Versioning with Patching {/* #workflow-patching */}

When keeping Workflows compatible, you should patch and ideally how to test your running Workflows will be safe to run on a new code version.

To patch:

- [How to patch Workflow code in Go](/develop/go/workflows/versioning#patching)
- [How to patch Workflow code in Java](/develop/java/workflows/versioning#patching)
- [How to patch Workflow code in Python](/develop/python/workflows/versioning#patching)
- [How to patch Workflow code in PHP](/develop/php/workflows/versioning#php-sdk-patching-api)
- [How to patch Workflow code in TypeScript](/develop/typescript/workflows/versioning#patching)
- [How to patch Workflow code in .NET](/develop/dotnet/workflows/versioning#patching)

To test, see [Safe Deployments](/develop/safe-deployments.mdx).

### Handling unreliable Worker Processes {/* #unreliable-worker-processes */}

You do not handle Worker Process failure or restarts in a Workflow Definition.

Workflow Function Executions are completely oblivious to the Worker Process in terms of failures or downtime.
The Temporal Platform ensures that the state of a Workflow Execution is recovered and progress resumes if there is an outage of either Worker Processes or the Temporal Service itself.
The only reason a Workflow Execution might fail is due to the code throwing an error or exception, not because of underlying infrastructure outages.

### What is a Workflow Type? {/* #workflow-type */}

A Workflow Type is a name that maps to a Workflow Definition.

- A single Workflow Type can be instantiated as multiple Workflow Executions.
- A Workflow Type is scoped by a Task Queue.
  It is acceptable to have the same Workflow Type name map to different Workflow Definitions if they are using completely different Workers.

<CaptionedImage
    src="/diagrams/workflow-type-cardinality.svg"
    title="Workflow Type cardinality with Workflow Definitions and Workflow Executions" />

---

## Continue-As-New

This page discusses [Continue-As-New](#continue-as-new) and how to decide [when to use it](#when).

## What is Continue-As-New? {/* #continue-as-new */}

Continue-As-New allows you to checkpoint your Workflow's state and start a fresh Workflow.

There are two main reasons you might want to start a new Workflow:

- A Workflow Execution with a long, or large [Event History](/workflow-execution/event#event-history), such as one calling many Activities, may bog down and have performance issues.
  It could even generate more Events than allowed by the [Event History limits](/workflow-execution/event#event-history-limits).
- A Workflow Execution can hit [Workflow Versioning](/workflow-definition#workflow-versioning) problems if it started running on an older version of your code and then begins executing on a newer version.

Your goal is to create a new Workflow with a fresh history that picks up where your last one left off.
First, pass your latest relevant state into Continue-As-New.
This hands it to a new Execution in the [Execution Chain](/workflow-execution#workflow-execution-chain).
This state is passed in as arguments to your Workflow.
The parameters are typically optional and left unset by the original caller of the Workflow.

The new Workflow Execution has the same Workflow Id, but a different Run Id, and starts its own Event History.

You can repeat Continue-As-New as often as needed, which means that your Workflow can run forever.
Workflows that do this are often called Entity Workflows because they represent durable objects, not just processes.

- [How to Continue-As-New using the Go SDK](/develop/go/workflows/continue-as-new#how)
- [How to Continue-As-New using the Java SDK](/develop/java/workflows/continue-as-new)
- [How to Continue-As-New using the PHP SDK](/develop/php/workflows/continue-as-new)
- [How to Continue-As-New using the Python SDK](/develop/python/workflows/continue-as-new#how)
- [How to Continue-As-New using the TypeScript SDK](/develop/typescript/workflows/continue-as-new)
- [How to Continue-As-New using the .NET SDK](/develop/dotnet/workflows/continue-as-new)
- [How to Continue-As-New using the Ruby SDK](/develop/ruby/workflows/continue-as-new)
- [How to Continue-As-New using the Rust SDK](/develop/rust/workflows/continue-as-new)

## When in your Workflow is it right to Continue-As-New? {/* #when */}

Temporal will tell your Workflow when it's approaching performance or scalability problems.
Find out if it's time by checking Continue-As-New Suggested in your Workflow at spots in your implementation where you are ready to checkpoint your state.

To prevent long-running Workflows from running on stale versions of code, you may also want to Continue-as-New periodically, depending on how often you deploy. This makes sure you're running only a couple of versions, which avoids some backwards compatibility problems.

- [Determine when to Continue-As-New using the Go SDK](/develop/go/workflows/continue-as-new#when)
- [Determine when to Continue-As-New using the Java SDK](/develop/java/workflows/continue-as-new)
- [Determine when to Continue-As-New using the PHP SDK](/develop/php/workflows/continue-as-new)
- [Determine when to Continue-As-New using the Python SDK](/develop/python/workflows/continue-as-new)
- [Determine when to Continue-As-New using the TypeScript SDK](/develop/typescript/workflows/continue-as-new)
- [Determine when to Continue-As-New using the .NET SDK](/develop/dotnet/workflows/continue-as-new)
- [Determine when to Continue-As-New using the Ruby SDK](/develop/ruby/workflows/continue-as-new)
- [Determine when to Continue-As-New using the Rust SDK](/develop/rust/workflows/continue-as-new)

---

## Events and Event History

This page discusses the following:

- [Events](#event)
- [Activity Events](#activity-events)
- [Event History](#event-history)
- [Event Loop](#event-loop)
- [Time Constraints](#time-constraints)
- [Reset](#reset)
- [Side Effect](#side-effect)
- [Principal Attribution](#principal-attribution)

The Temporal Service tracks the progress of each Workflow Execution by appending information about Events, such as when the Workflow Execution began or ended, to the Event History associated with that execution.
This information not only enables developers to know what took place, but is also essential for providing Durable Execution, since it enables the Workflow Execution to recover from a crash and continue making progress.
In order to maintain high performance, the Temporal Service places limits on both the number and size of items in the Event History for each Workflow Execution.

## What is an Event? {/* #event */}

Events are created by the Temporal Service in response to external occurrences and Commands generated by a Workflow Execution.
Each Event corresponds to an `enum` that is defined in the [Server API](https://github.com/temporalio/api/blob/main/temporal/api/enums/v1/event_type.proto).

All Events are recorded in the [Event History](#event-history).

A list of all possible Events that could appear in a Workflow Execution Event History is provided in the [Event reference](/references/events).

### Activity Events {/* #activity-events */}

Seven Activity-related Events are added to Event History at various points in an Activity Execution:

- After a [Workflow Task Execution](/tasks#activity-task-execution) reaches a line of code that starts/executes an Activity, the Worker sends the Activity Type and arguments to the Temporal Service, and the Temporal Service adds an [ActivityTaskScheduled](/references/events#activitytaskscheduled) Event to Event History.
- When `ActivityTaskScheduled` is added to History, the Temporal Service adds a corresponding Activity Task to the Task Queue.
- A Worker polling that Task Queue picks up the Activity Task and runs the Activity function or method.
- If the Activity function returns, the Worker reports completion to the Temporal Service, and the Temporal Service adds [ActivityTaskStarted](/references/events#activitytaskstarted) and [ActivityTaskCompleted](/references/events#activitytaskcompleted) to Event History.
- If the Activity function throws a [non-retryable Failure](/references/failures#non-retryable), the Temporal Service adds [ActivityTaskStarted](/references/events#activitytaskstarted) and [ActivityTaskFailed](/references/events#activitytaskfailed) to Event History.
