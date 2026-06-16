Most operations require multiple State Transitions.

For example, a simple Workflow with two sequential [Activity Tasks](/tasks#activity-task) (and no retries) produces 11 State Transitions: two for Workflow start, four for each Activity, and one for Workflow completion.

:::tip NEXT STEPS
For more information on Workflow Execution, please refer to the following subpages:

- [Event](/workflow-execution/event)
- [Workflow Id and Run Id](/workflow-execution/workflowid-runid)
- [Limits](/workflow-execution/limits)
- [Continue-as-New](/workflow-execution/continue-as-new)
- [Timers and Start Delay](/workflow-execution/timers-delays)
  :::

---

## Workflow Id and Run Id

This page discusses the following:

- [Run Id](#run-id)
- [Operations leading to non-determinism](#run-id-non-determinism)
- [Workflow Id](#workflow-id)
- [Workflow Id Reuse Policy](#workflow-id-reuse-policy)
- [Workflow Id Conflict Policy](#workflow-id-conflict-policy)

Each Workflow Execution is associated with a user-defined [Workflow ID](#workflow-id), a value which typically carries some business meaning (such as an order number or customer number).
Temporal guarantees that there can be at most one Workflow Execution with a given ID running at any point in time, a constraint that helps to protect against unexpected duplication.
In some cases, such as when running the same Workflow at recurring intervals using the Schedules features, there can be multiple "runs" of a single Workflow Execution over a period of time.
In this case, all runs will have the same Workflow ID.
However, each run will have a unique system-generated [Run ID](#run-id).

## What is a Run Id? {/* #run-id */}

A Run Id is a globally unique, platform-level identifier for a [Workflow Execution](/workflow-execution).

The current Run Id is mutable and can change during a [Workflow Retry](/encyclopedia/retry-policies). You shouldn't rely on storing the current Run Id, or using it for any logical choices, because a Workflow Retry changes the Run Id and can lead to non-determinism issues.

Temporal guarantees that only one Workflow Execution with a given [Workflow Id](#workflow-id) can be in an Open state at any given time.
But when a Workflow Execution reaches a Closed state, it is possible to have another Workflow Execution in an Open state with the same Workflow Id.
For example, a Temporal Cron Job is a chain of Workflow Executions that all have the same Workflow Id.
Each Workflow Execution within the chain is considered a _Run_.

A Run Id uniquely identifies a Workflow Execution even if it shares a Workflow Id with other Workflow Executions.

### Which operations lead to non-determinism issues? {/* #run-id-non-determinism */}

An operation like `ContinueAsNew`, `Retry`, `Cron`, and `Reset` creates a [Workflow Execution Chain](/workflow-execution#workflow-execution-chain) as identified by the [`first_execution_run_id`](https://github.com/temporalio/api/blob/main/temporal/api/history/v1/message.proto).

Each operation creates a new Workflow Execution inside a chain run and saves its information as `first_execution_run_id`.
Thus, the Run Id is updated during each operation on a Workflow Execution.

- The `first_execution_run_id` is the Run Id of the first Workflow Execution in a Chain run.
- The `original_execution_run_id` is the Run Id when the `WorkflowExecutionStarted` Event occurs.

A Workflow `Reset` changes the first execution Run Id, but preserves the original execution Run Id.
For example, when a new Workflow Execution in the chain starts, it stores its Run Id in `original_execution_run_id`.
A reset doesn't change that field, but the current Run Id is updated.

:::caution

Because of this behavior, you shouldn't rely on the current Run Id in your code to make logical choices.

:::

**Learn more**

For more information, see the following link.

- [`message.proto`](https://github.com/temporalio/api/blob/main/temporal/api/history/v1/message.proto#L75-L82)

## What is a Workflow Id? {/* #workflow-id */}

A Workflow Id is a customizable, application-level identifier for a [Workflow Execution](/workflow-execution) that is unique to an Open Workflow Execution within a [Namespace](/namespaces).

- [How to set a Workflow Id](/develop/go/client/temporal-client#workflow-id)

A Workflow Id is meant to be a business-process identifier, such as customer identifier or order identifier.

:::caution Do not use sensitive data or PII in Workflow Ids

Do not include sensitive data, secrets, or personally identifiable information (PII) as a Workflow Id.
Workflow Ids are stored in plain text, are **not** processed by a custom [Payload Codec](/payload-codec#payload-codec), and are visible in the Temporal Web UI, CLI output, Event History, and system logs.
The same applies to other user-defined identifiers such as Workflow Type names, Task Queue names, Activity names, and Signal/Query/Update names.

Using sensitive data in these identifiers risks exposure to anyone with Namespace access and may violate data protection regulations such as GDPR, HIPAA, or SOC 2.

:::

The Temporal Platform guarantees uniqueness of the Workflow Id within a [Namespace](/namespaces) based on the Workflow Id Reuse Policy.

A [Workflow Id Reuse Policy](#workflow-id-reuse-policy) can be used to manage whether a Workflow Id from a Closed Workflow can be re-used.

A [Workflow Id Conflict Policy](#workflow-id-conflict-policy) can be used to decide how to resolve a Workflow Id conflict with a Running Workflow.

A Workflow Execution can be uniquely identified across all Namespaces by its [Namespace](/namespaces), Workflow Id, and [Run Id](#run-id).

### What is a Workflow Id Reuse Policy? {/* #workflow-id-reuse-policy */}

A Workflow Id Reuse Policy determines whether a Workflow Execution is allowed to spawn with a particular Workflow Id, if that Workflow Id has been used with a previous, and now Closed, Workflow Execution.

It is not possible for a new Workflow Execution to spawn with the same Workflow Id as another Open Workflow Execution, regardless of the Workflow Id Reuse Policy.

See [Workflow Id Conflict Policy](#workflow-id-conflict-policy) for resolving a Workflow Id conflict.

The Workflow Id Reuse Policy can have one of the following values:

- **Allow Duplicate:** The Workflow Execution is allowed to exist regardless of the Closed status of a previous Workflow Execution with the same Workflow Id.
  **This is the default policy, if one is not specified.**
  Use this when it is OK to have a Workflow Execution with the same Workflow Id as a previous, but now Closed, Workflow Execution.
- **Allow Duplicate Failed Only:** The Workflow Execution is allowed to exist only if a previous Workflow Execution with the same Workflow Id does not have a Completed status.
  Use this policy when there is a need to re-execute a Failed, Timed Out, Terminated, or Cancelled Workflow Execution and guarantee that the Completed Workflow Execution will not be re-executed.
- **Reject Duplicate:** The Workflow Execution cannot exist if a previous Workflow Execution has the same Workflow Id, regardless of the Closed status.
  Use this when there can only be one Workflow Execution per Workflow Id within a Namespace for the given retention period.

The first three values (Allow Duplicate, Allow Duplicate Failed Only, and Reject Duplicate) of the Workflow Id Reuse Policy apply to Closed Workflow Executions that are retained within the Namespace.
For example, given a default Retention Period, the Temporal Service can only check the Workflow Id of the spawning Workflow Execution based on the Workflow Id Reuse Policy against the Closed Workflow Executions for the last _30 days_.

If you need to start a Workflow for a particular implementation only if it hasn't started yet, ensure that your Retention Period is long enough to check against.
If this becomes unwieldy, consider using [Workflow message passing](/encyclopedia/workflow-message-passing) instead of trying to start Workflows atomically.

The fourth value of the Workflow Id Reuse Policy, Terminate if Running, only applies to a Workflow Execution that is currently open within the Namespace.
For Terminate if Running, the Retention Period is not a consideration for this policy.

If there is an attempt to spawn a Workflow Execution with a Workflow Id Reuse Policy that won't allow it, the Server will prevent the Workflow Execution from spawning.

### What is a Workflow Id Conflict Policy? {/* #workflow-id-conflict-policy */}

A Workflow Id Conflict Policy determines how to resolve a conflict when spawning a new Workflow Execution with a particular Workflow Id used by an existing Open Workflow Execution.
See [Workflow Id Reuse Policy](#workflow-id-reuse-policy) for managing the reuse of a Workflow Id of a Closed Workflow.

By default, this results in a `Workflow execution already started` error.

:::note

The default [StartWorkflowOptions](https://pkg.go.dev/go.temporal.io/sdk/internal#StartWorkflowOptions) behavior in the Go SDK is to not return an error when a new Workflow Execution is attempted with the same Workflow Id as an Open Workflow Execution.
Instead, it returns a WorkflowRun instance representing the current or last run of the Open Workflow Execution.

To return the `Workflow execution already started` error, set `WorkflowExecutionErrorWhenAlreadyStarted` to `true`.

:::

The Workflow Id Conflict Policy can have one of the following values:

- **Fail:** Prevents the Workflow Execution from spawning and returns a `Workflow execution already started` error.
  **This is the default policy, if one isn't specified.**
- **Use Existing:** Prevents the Workflow Execution from spawning and returns a successful response with the Open Workflow Execution's Run Id.
- **Terminate Existing:** Terminates the Open Workflow Execution then spawns the new Workflow Execution with the same Workflow Id.

---

## Temporal Workflow

This guide provides a comprehensive overview of Temporal Workflows and covers the following:

- [Workflow Definition](/workflow-definition)
- [Workflow Execution](/workflow-execution)
- [Schedules](/schedule)
- [Dynamic Handler](/dynamic-handler)
- [Cron Job](/cron-job)

## Intro to Workflows

Conceptually, a workflow defines a sequence of steps. With Temporal, those steps are defined by writing code, known as a Workflow Definition, and are carried out by running that code, which results in a Workflow Execution.

In day-to-day conversations, the term Workflow might refer to Workflow Type, a Workflow Definition, or a Workflow Execution.

1. A **Workflow Definition** is the code that defines your Workflow.
2. The **Workflow Type** is the name that maps to a Workflow Definition. It's an identifier that makes it possible to distinguish one type of Workflow (such as order processing) from another (such as customer onboarding).
3. A **Workflow Execution** is a running Workflow, which is created by combining a Workflow Definition with a request to execute it. You can execute a Workflow Definition any number of times, potentially providing different input each time (i.e., a Workflow Definition for order processing might process order #123 in one execution and order #567 in another execution). It is the actual instance of the Workflow Definition running in the Temporal Platform.

You'll develop those Workflows by writing code in a general-purpose programming language such as Go, Java, TypeScript, or Python. The code you write is the same code that will be executed at runtime, so you can use your favorite tools and libraries to develop Temporal Workflows.

Temporal Workflows are resilient. They can run—and keep running—for years, even if the underlying infrastructure fails. If the application itself crashes, Temporal will automatically recreate its pre-failure state so it can continue right where it left off.

Each Workflow Execution emits a series of **Commands** and processes a sequence of **Events**, which are recorded in an **Event History**.

### How Workflow replay works

When a Workflow [yields](https://en.wikipedia.org/wiki/Yield_(multithreading)) or encounters an error, the goal of Temporal is to bring the Workflow back to the exact same state it was in before the pause occurred. To make that possible, Temporal keeps the Event History. This is a complete, ordered log of everything that has already happened in a Workflow.

The Event History could look like this for example:

- Started Timer for 5 minutes
- Scheduled Activity X
- Activity X completed with result Y
- Received Signal Z

This history is the source of truth for everything that happens in the Workflow.

#### Resuming a Workflow

When it's time to continue the Workflow, Temporal doesn't restore memory from a snapshot. It starts the Workflow code from the beginning, replays the Event History step by step, and uses that history to guide the code back to the exact state as before. So the Workflow code is re-run, but uses the recorded events instead of redoing work. Although Temporal doesn't always have to start from the beginning if the state is cached.

Because the Workflow is re-executed to rebuild its state:

- It has to make the same decisions when given the same history, which makes a Workflow deterministic.
- It shouldn't depend on any values _not_ recorded in the history which would be different between runs.

For example:

- A direct call to `Date.now()` could return a different value on replay.
- A random number could change.
- A network call, which wasn't performed inside an Activity, could return something new.

If those values changed, the Workflow could take a different path and fail to match the recorded history. To solve this, Temporal provides replay-safe versions of common operations:

- Time is read from the Workflow context so it matches the recorded history.
- Timers are recorded as events and don’t “wait” again during replay.
- Randomness and similar values can be captured once and reused.

These APIs make sure the Workflow receives the same values during replay as it did originally. Activities handle everything that interacts with the outside world, like:

- API calls
- Database queries
- LLM invocations
- File I/O

When a Workflow calls an Activity, the Activity runs once, its result is recorded in the Event History. During replay, that result is reused, not recomputed. So Activities aren't executed again during replay.

---

## Handling Signals, Queries, & Updates

When Signals, Updates, and Queries arrive at your Workflow, the handlers for these messages will operate on the current state of your Workflow and can use the fields you have set.
In this section, we’ll give you an overview of how messages work with Temporal and cover how to write correct and robust handlers by covering topics like atomicity, guaranteeing completion before the Workflow exits, exceptions, and idempotency.

## Handling Messages {/* #handling-messages */}

### Message handler concurrency {/* #message-handler-concurrency */}

If your Workflow receives messages, you may need to consider how those messages interact with one another or with the main Workflow method.
Behind the scenes, Temporal is running a loop that looks like this:

<CaptionedImage
    src="/img/info/messages-workflow-loop.png"
    title="Diagram that shows the execution ordering of Workflows" />

Every time the Workflow wakes up--generally, it wakes up when it needs to--it will process messages in the order they were received, followed by making progress in the Workflow’s main method.

This execution is on a single thread–while this means you don’t have to worry about parallelism, you do need to worry about concurrency if you have written Signal and Update handlers that can block. These can run interleaved with the main Workflow and with one another, resulting in potential race conditions. These methods should be made reentrant.

#### Initializing the Workflow first {/* #workflow-initializers */}

Initialize your Workflow's state before handling messages.
This prevents your handler from reading uninitialized instance variables.

To see why, refer to the [diagram](#message-handler-concurrency).
It shows that your Workflow processes messages before the first run of your Workflow's main method.

The message handler runs first in several scenarios, such as:

- When using [Signal-with-Start](/sending-messages#signal-with-start).
- When your Worker experiences delays, such as when the Task Queue it polls gets backlogged.
- When messages arrive immediately after a Workflow continues as new but before it resumes.

For all languages except Go and TypeScript, use your constructor to set up state.
Annotate your constructor as a Workflow Initializer and take the same arguments as your Workflow's main method.

Note that you can't make blocking calls from your constructor.
If you need to block, make your Signal or Update handler [wait](#waiting) for an initialization flag.

In Go and TypeScript, register any message handlers only after completing initialization.

### Message handler patterns {/* #message-handler-patterns */}

Here are several common patterns for write operations, Signal and Update handlers. They don't apply to pure read operations, i.e. Queries or [Update Validators](/handling-messages#update-validators):

- Returning immediately from a handler
- Waiting for the Workflow to be ready to process them
- Kicking off activities and other asynchronous tasks
- Injecting work into the main Workflow
- Finishing handlers before the Workflow completes
- Ensuring your messages are processed exactly once

#### Synchronous handlers

Synchronous handlers don’t kick off any long-running operations or otherwise block. They're guaranteed to run atomically.

#### Waiting {/* #waiting */}

A Signal or Update handler can block waiting for the Workflow to reach a certain state using a Wait Condition. See the links below to find out how to use this with your SDK.

#### Running asynchronous tasks

Sometimes, you need your message handler to wait for long-running operations such as executing an Activity. When this happens, the handler will yield control back to [the loop](#message-handler-concurrency). This means that your handlers can have race conditions if you’re not careful.
You can guard your handlers with concurrency primitives like mutexes or semaphores, but you should use versions of these primitives provided for Workflows in most languages. See the links below for examples of how to use them in your SDK.

#### Inject work into the main Workflow {/* #injecting-work-into-main-workflow */}

Sometimes you want to process work provided by messages in the main Workflow. Perhaps you’d like to accumulate several messages before acting on any of them. For example, message handlers might put work into a queue, which can then be picked up and processed in an event loop that you yourself write.
This option is considered advanced but offers powerful flexibility. And if you serialize the handling of your messages inside your main Workflow, you can avoid using concurrency primitives like mutexes and semaphores. See the links above for how to do this in your SDK.

#### Finishing handlers before the Workflow completes {/* #finishing-message-handlers */}

You should generally finish running all handlers before the Workflow run completes or continues as new. For some Workflows, this means you should explicitly check to make sure that all the handlers have completed before finishing. You can await a condition called All Handlers Finished at the end of your Workflow.

If you don’t need to ensure that your handlers complete, you may specify your handler’s Handler Unfinished Policy as Abandon to turn off the warnings. However, note that clients waiting for Updates will get Not Found errors if they're waiting for Updates that never complete before the Workflow run completes.

See the links below for how to ensure handlers are finished in your SDK.

#### Message IDs and handling Continue-As-New {/* #exactly-once-message-processing */}

Usually, you'll want your message handlers to run exactly once--to be idempotent--in cases where the same Signal or Update is delivered twice. For Updates, Temporal handles this for you on the server, by deduplicating according to the Update ID. The Update ID is set automatically to a UUID, but you can set it yourself.

For Signals, you should use a custom idempotency key that you send as part of your own signal inputs, implementing the deduplication in your Workflow code.

However, if you are using Updates with [Continue-As-New](/workflow-execution/continue-as-new) you should implement the deduplication in your Workflow code, since Update ID deduplication by the server is per Workflow run.

:::info

In addition to these application-level identifiers, both Signals and Updates automatically use request IDs to deduplicate retried client calls. You do not need to do anything to enable this.

:::

See the links below for examples of handling idempotency and Continue-As-New in your SDK.

#### Authoring message handler patterns

See examples of the above patterns.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing" text="Author message handler patterns in .NET" archetype="feature-guide" />
    <RelatedReadItem path="/develop/go/workflows/message-passing#message-handler-patterns" text="Author message handler patterns in Go" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing" text="Author message handler patterns in Java" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing" text="Author message handler patterns in PHP" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#message-handler-patterns" text="Author message handler patterns in Python" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#message-handler-patterns" text="Author message handler patterns in TypeScript" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#message-handler-patterns" text="Author message handler patterns in Ruby" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#message-handler-patterns" text="Author message handler patterns in Rust" archetype="feature-guide" />
</RelatedReadContainer>

### Update Validators {/* #update-validators */}

When you define an Update handler, you may optionally define an Update Validator: a read operation that's responsible for accepting or rejecting the Update. You can use Validators to verify arguments or make sure the Workflow is ready to accept your Updates.

- If it accepts, the Update will become part of your Workflow’s history and the client will be notified that the operation has been Accepted. The Update handler will then run until it returns a value.
- If it rejects, the client will be informed that it was Rejected, and the Workflow will have no indication that it was ever requested, similar to a Query handler.

:::note

Like Queries, Validators are not allowed to block.

:::

Once the Update handler is finished and has returned a value, the operation is considered Completed.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/message-passing#updates" text="Validate updates in Go" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing#updates" text="Validate updates in Java" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing#updates" text="Validate updates in .NET" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#updates" text="Validate updates in Python" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#updates" text="Validate updates in TypeScript" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing#handle-updates" text="Validate updates in PHP" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#updates" text="Validate updates in Ruby" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#updates" text="Validate updates in Rust" archetype="feature-guide" />
</RelatedReadContainer>

### Exceptions in message handlers {/* #exceptions */}

When throwing an exception in a message handler, you should decide whether to make it an [Application Failure](/references/failures#application-failure). The implications are different between Signals and Updates.

:::caution
The following content applies in every SDK except the Go SDK. See below.
:::

#### Exceptions in Signals

In Signal handlers, throw [Application Failures](/references/failures#application-failure) only for unrecoverable errors, because the entire Workflow will fail.
Similarly, allowing a failing Activity or Child Workflow to exhaust its retries, so that it throws an [Activity Failure](https://docs.temporal.io/references/failures#activity-failure) or [Child Workflow Failure](https://docs.temporal.io/references/failures#child-workflow-failure) will cause the entire Workflow to fail.
Note that for Activities, this will only happen if you change the default Activity [Retry Policy](https://docs.temporal.io/encyclopedia/retry-policies), since by default they retry forever.
If you throw any other exception, by default, it will cause a [Workflow Task Failure](/references/failures#workflow-task-failures). This means the Workflow will get stuck and will retry the handler periodically until the exception is fixed, for example by a code change.
