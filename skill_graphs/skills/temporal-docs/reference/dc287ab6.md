# Reset retry state but don't resume yet
temporal activity reset \
  --workflow-id my-workflow \
  --activity-id my-activity \
  --keep-paused
```

See the [CLI reference for `temporal activity reset`](/cli/command-reference/activity#reset) for all options, including
`--reset-heartbeats` and bulk mode via `--query`.

### Detect Reset in Activity code

Activities with Heartbeat can detect that an interruption was caused by Reset rather than a timeout or Workflow
Cancellation. A Reset Activity is retried from attempt 1. A Cancelled Activity isn't. Your Activity code may need to
handle these cases differently, for example saving partial progress on Reset while discarding it on Cancellation.

| SDK        | How to detect Reset                                                                |
| ---------- | ---------------------------------------------------------------------------------- |
| Go         | `activity.GetCancellationDetails(ctx).Cause()` returns `activity.ErrActivityReset` |
| Java       | Catch `ActivityResetException`                                                     |
| TypeScript | Catch `ApplicationFailure` with `error.type === "ActivityReset"`                   |
| Python     | Check `cancellation_details().reset` on `asyncio.CancelledError`                   |
| .NET       | Check `CancellationDetails.IsReset` on `OperationCanceledException`                |

### Important considerations

- **A Reset Activity can still time out.** Reset doesn't restart the
  [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout). The deadline is
  calculated from when the Activity was originally scheduled. Use [`update-options`](#update-options) to extend the
  timeout before or after Reset.
- **Heartbeat details are preserved by default.** If your Activity uses Heartbeat details for progress tracking and you
  want a clean restart, pass `--reset-heartbeats`.
- **Reset won't interrupt an Activity that doesn't Heartbeat.** The current execution runs to completion, which could
  take up to the full [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout). If the
  Activity had already retried (attempt > 1), the Temporal Service rejects the current execution's result because Reset
  changed the expected attempt number. The Activity waits for its Start-To-Close Timeout to expire before a new
  execution is scheduled.
- **`--restore-original-options` restores the Activity's original configuration.** It reverts timeouts, Retry Policy,
  and Task Queue to the values from when the Activity was first scheduled.
- **Bulk Reset can overwhelm downstream services.** When using `--query` to Reset Activities across many Workflows, use
  `--jitter` to stagger the restart times.

## Update Options {/* #update-options */}

Update Options changes an Activity's runtime configuration without restarting it.

### When to Update Options

- The [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout) is about to
  expire on a Paused Activity, and you need to extend it before Unpausing.
- An Activity's [Retry Policy](/encyclopedia/retry-policies) needs tuning based on observed failure patterns (for
  example, increasing the backoff interval or maximum attempts).
- You want to move an Activity to a different [Task Queue](/task-queue) to route it to a specific set of
  [Workers](/workers).
- You need to restore an Activity's original configuration after a temporary override.

### What happens when you Update an Activity's Options

You can change [timeouts](/encyclopedia/detecting-activity-failures) (Schedule-To-Close, Start-To-Close,
Schedule-To-Start, Heartbeat), Retry Policy (initial interval, maximum interval, backoff coefficient, maximum attempts),
and Task Queue. Only the fields you specify are changed. All other options remain unchanged.

- **If the Activity is waiting for retry (scheduled),** the new options take effect immediately. Any pending retry timer
  is regenerated with the updated configuration.
- **If the Activity is currently running,** the new options are stored but take effect on the next execution. The
  in-flight execution isn't interrupted.
- **If the Activity is Paused,** the new options are stored immediately. They take effect when the Activity is Unpaused
  and the next execution starts.
- **Workflow code has no visibility into Activity Operations.** Update Options doesn't produce an Event History event,
  so the Workflow can't detect or react to it. See [Observability](#observability).

Update Options is idempotent. Updating an Activity with the same values it already has produces no change. Updating
options on an Activity that has already completed returns an error.

### CLI usage

```bash
temporal activity update-options \
  --workflow-id my-workflow \
  --activity-id my-activity \
  --schedule-to-close-timeout 24h
```

See the [CLI reference for `temporal activity update-options`](/cli/command-reference/activity#update-options) for all
options, including Retry Policy, Task Queue, and bulk mode via `--query`.

### Important considerations

- **Changes to a running Activity take effect on the next execution, not the current one.** If you need the change to
  apply immediately, the Activity must finish or fail its current execution first.
- **`--restore-original-options` is batch-only.** This flag only works with `--query`. It's silently ignored in
  single-workflow mode. It can't be combined with other option changes in the same command.

### Limitations

- **Update Options is CLI and gRPC only.** It's not available in the UI.

## Observability {/* #observability */}

Activity Operations have a limited audit trail because they are not recorded in a Workflow's Event History. However, you
can use the CLI and the UI to check Activity state and find Paused Activities for running Workflows.

### Check Activity state

`temporal workflow describe` shows the current state of each pending Activity, including whether it's Paused, its
current attempt count, and last failure. The UI shows who performed an operation, when, and why (if a `--reason` was
provided).

### Find Paused Activities

The `TemporalPauseInfo` [Search Attribute](/search-attribute) is filterable within a Workflow.

There's no Namespace-wide query to find all Paused Activities across Workflows. You must know the Workflow Id.

### Audit trail {/* #audit-trail */}

Activity Operations don't produce Event History events. There is no record of a Pause, Reset, or option change in the
Workflow's [Event History](/workflow-execution/event#event-history). Nothing that reads the Event History - Workflow
code, Replays, or external tooling - will see that an Operation occurred.

Evidence of an Operation is gone when the Activity completes or the Workflow closes. There's no persistent record that
an Activity was Paused, Reset, or had its options changed.

The only way to confirm the current state of an Activity is `temporal workflow describe` or the UI.

---

## Local Activity

This page discusses [Local Activity](#local-activity).

## What is a Local Activity? {/* #local-activity */}

A Local Activity is an [Activity Execution](/activity-execution) that executes in the same process as the [Workflow Execution](/workflow-execution) that spawns it.

Some Activity Executions are very short-living and do not need the queuing semantic, flow control, rate limiting, and routing capabilities.
For this case, Temporal supports the Local Activity feature.

The main benefit of Local Activities is that they use less Temporal Service resources (for example, fewer History events) and have much lower latency overhead (because no need to roundtrip to the Temporal Service) compared to normal Activity Executions.
However, Local Activities are subject to shorter durations and a lack of rate limiting.

Consider using Local Activities for functions that are the following:

- can be implemented in the same binary as the Workflow that calls them.
- do not require global rate limiting.
- do not require routing to a specific Worker or Worker pool.
- no longer than a few seconds, inclusive of retries.

If it takes longer than 80% of the Workflow Task Timeout (which is 10 seconds by default), the Worker will ask the Temporal Service to create a new Workflow Task to extend the "lease" for processing the Local Activity.
The Worker will continue doing so until the Local Activity has completed.
This is called Workflow Task Heartbeating.
The drawbacks of long-running Local Activities are:

- Each new Workflow Task results in 3 more Events in History.
- The Workflow won't get notified of new events like Signals and completions until the next Workflow Task Heartbeat.
- New Commands created by the Workflow concurrently with the Local Activity will not be sent to the Temporal Service until either the Local Activity completes or the next Workflow Task Heartbeat.

Using a Local Activity without understanding its limitations can cause various production issues.
**We recommend using regular Activities unless your use case requires very high throughput and large Activity fan outs of very short-lived Activities.**
More guidance in choosing between [Local Activity vs Activity](https://community.temporal.io/t/local-activity-vs-activity/290/3) is available in our forums.

---

## Standalone Activity

<ReleaseNoteHeader
  featureName="standaloneActivity"
  languages={["Go", "Python", "Java", ".NET", "TypeScript", "Ruby"]}
>
  Available in [Temporal Cloud](#temporal-cloud-support) and in the [Temporal CLI](#temporal-cli-support) v1.7.0 or higher with Temporal Server v1.31.0 or higher. Java SDK support is in [Pre-release](/evaluate/development-production-features/release-stages#pre-release).
</ReleaseNoteHeader>

See [limitations](#public-preview-limitations) below.

## What is a Standalone Activity? {/* #standalone-activity */}

If you need to orchestrate multiple Activities, use a [Workflow](/workflows). But if you just need to
execute a single Activity, use a Standalone Activity.

Standalone Activities are Temporal’s [job queue](/evaluate/development-production-features/job-queue) -
the simplest way to run durable, retryable tasks on Temporal.

    <ThemedImage
      alt="Standalone Activity vs. Workflow - Standalone Activities execute a single function reliably as a top-level primitive, while Workflows orchestrate multiple Activity steps"
      sources={{
        light: '/diagrams/standalone-activities-vs-workflowlight.svg',
        dark: '/diagrams/standalone-activities-vs-workflowdark.svg',
      }}
      style={{maxWidth: '100%', cursor: 'pointer'}}
    />

A Standalone Activity is a top-level [Activity Execution](/activity-execution) started directly by a
[Client](/encyclopedia/temporal-sdks#temporal-client), without using a Workflow. This results in
fewer [Billable Actions](/cloud/actions-usage#actions-in-workflows) in Temporal Cloud than using a Workflow
to run a single Activity. If your Activity Execution is short-lived, you will also notice lower
latency, since there are fewer Worker round-trips.

You write your Activity Functions the same way for both. In fact, the same Activity Function can be
executed as a Standalone Activity and as a Workflow Activity with no code changes.

:::tip GET STARTED

Pick your SDK and follow the quickstart:

- [Go SDK - Standalone Activities quickstart and code sample](/develop/go/activities/standalone-activities)
- [Python SDK - Standalone Activities quickstart and code sample](/develop/python/activities/standalone-activities)
- [.NET SDK - Standalone Activities quickstart and code sample](/develop/dotnet/activities/standalone-activities)
- [Java SDK - Standalone Activities quickstart and code sample](/develop/java/activities/standalone-activities)
- [Ruby SDK - Standalone Activities quickstart and code sample](/develop/ruby/activities/standalone-activities)
- [TypeScript SDK - Standalone Activities quickstart and code sample](/develop/typescript/activities/standalone-activities)

:::

## Use cases

Standalone Activities can be used for [durable job processing use
cases](/evaluate/development-production-features/job-queue) such as sending an email, processing a
webhook, syncing data, or executing a single function reliably with built-in retries and timeouts.

## Key features
- Execute any Temporal Activity as a top-level primitive without the overhead of a Workflow
- Native async job processing model: schedule -> dispatch -> process -> result
- No head-of-line blocking - a slow job doesn’t block the dispatch of other Tasks
- Arbitrary length jobs with heartbeats for liveness and checkpointing progress
- At-least-once execution by default with native retry policy and timeouts
- At-most-once execution if retry max attempts is 1
- Addressable - get an Activity ID / Run ID and get the result, cancel, and terminate
- Deduplication - with conflict policy: (USE_EXISTING, ...), reuse policy: (REJECT_DUPLICATES, ...)
- Separate ID space from Workflows - Standalone Activities are a different kind of top-level execution
- Priority and fairness - multi-tenant fairness, weighted priority tiers, and safeguards against starvation of lower-weighted tasks
- Visibility - list Activity Executions and view status, retry count, and last error
- Manual completion by ID (or token): ignore activity return and wait for external completion
- Activity metrics - including counts for success, failure, timeout, and cancel
- Dual use - execute Activities within a Workflow or standalone with no Worker code changes

## Observability {/* #observability */}

All existing [Activity metrics](/cloud/metrics/openmetrics/metrics-reference#activity-metrics) apply
to Standalone Activities. This includes counts for scheduled, started, completed, failed, timed out,
and canceled activities.

You can use [List Filters](/list-filter) to query Standalone Activity Executions by type, status,
task queue, and other attributes using the SDK or the `temporal activity list` CLI command.

`CountActivities` returns the total number of Standalone Activity Executions matching a filter,
analogous to counting Workflow Executions. This is the total count of executions (running, completed,
failed, etc.) - not the number of queued tasks.

## Public Preview limitations

The Public Preview of Standalone Activities has some known limitations:

- Pause, reset, and update options are not supported in Public Preview but scheduled for GA.
- `TerminateExisting` conflict policy / `TerminateIfRunning` reuse policy is not supported yet.

## Temporal CLI support

Standalone Activities require [Temporal CLI](https://github.com/temporalio/cli/releases/tag/v1.7.0) v1.7.0 or higher and [Temporal Server](https://github.com/temporalio/temporal/releases/tag/v1.31.0) v1.31.0 or higher.

Install with Homebrew:

```bash
brew install temporal
```

Or see the [Temporal CLI install guide](/cli/setup-cli) for other platforms.

Verify the installation:

```bash
temporal --version
```

Which should output v1.7.0 or higher, for example:
```
temporal version 1.7.0 (Server 1.31.0, UI 2.49.1)
```

The `temporal activity` subcommand supports Standalone Activities with commands including: `start`,
`execute`, `result`, `list`, `count`, `describe`, `cancel`, and `terminate`.

The Temporal Dev Server has Standalone Activities enabled by default for local testing.

## Temporal Cloud support

Standalone Activities in Temporal Cloud is available as a Public Preview feature.

---

## Application failures

Temporal handles many types of failures automatically through Durable Execution.
Worker crashes, network interruptions, and infrastructure outages are all recovered from without any intervention.
But some failures require your application to detect and respond to them.
Understanding which failures Temporal handles and which ones your application must handle is fundamental to building reliable Temporal applications.

## Platform failures vs application failures {/* #platform-vs-application */}

Failures fall into two categories based on where they are detected and mitigated: platform failures and application failures.

### Platform failures

Platform failures occur due to issues with the infrastructure: server outages, network interruptions, Worker crashes, or other environmental factors outside of your application's control.
Temporal's Durable Execution handles these failures transparently.
When a Worker crashes mid-execution, another Worker picks up the work and continues from where it left off.
Your application code does not need to account for these failures.

Platform failures are resolved through **forward recovery**: the system retries the failed operation, and if the retry succeeds, the application continues from the point of failure without undoing any previous work.

### Application failures

Application failures are generated by your code.
They indicate an issue with your application logic, such as invalid input data, a business rule violation, or a failed call to an external service.

Application failures do not resolve on their own through retries alone.
Recovering from an application failure may require fixing a bug, passing different input data, or performing some external mitigation.

Application failures often involve **backward recovery**: the system undoes some of the work that has already been performed to return to a previous state.
For example, if a payment step fails after inventory has already been reserved, the application may need to release that inventory.

For guidance on categorizing failures and deciding how to handle them, see [Error handling](/best-practices/error-handling).

## How Temporal represents failures {/* #failure-representation */}

When a failure surfaces to your application code, the SDK represents it as a typed error object.
Each SDK uses the conventions of its language: what is called a Failure in one SDK might be called an Error or Exception in another.

Most SDKs have a base class that other failure types extend.
This provides a common interface and shared behavior across different failure types.
For example:

- TypeScript: [TemporalFailure](https://typescript.temporal.io/api/classes/common.TemporalFailure)
- Java: [TemporalFailure](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/TemporalFailure.html)
- Python: [FailureError](https://python.temporal.io/temporalio.exceptions.FailureError.html)
- PHP: [TemporalFailure](https://php.temporal.io/classes/Temporal-Exception-Failure-TemporalFailure.html)
- Go: Uses specific error types rather than a base class

For the complete list of failure types and their SDK-specific classes, see [Failures reference](/references/failures).

Errors that extend this base class are referred to as **Temporal failures**.
These are the SDK's typed error classes for failures that surface to application code, whether generated by the system (such as ActivityFailure or TimeoutFailure) or by your code (ApplicationFailure).
Platform failures like Worker crashes and network interruptions do not produce Temporal failure objects. The platform handles those transparently through retries.

The SDK uses whether an error is a Temporal failure to determine how to handle it.
In Workflow code, throwing a Temporal failure fails the Workflow Execution, while throwing any other error fails the Workflow Task and is retried automatically.

The Temporal failure types are:

| Failure type | Description |
| :--- | :--- |
| **Application Failure** | Raised by your code to indicate application-specific errors. This is the only failure type you create directly. |
| **Activity Failure** | Wraps an error from an Activity Execution. The `cause` field contains the underlying error. |
| **Child Workflow Failure** | Wraps an error from a Child Workflow Execution. |
| **Timeout Failure** | Occurs when an Activity or Workflow exceeds its configured timeout. |
| **Cancelled Failure** | Results from cancellation of a Workflow, Activity, or Timer. |
| **Terminated Failure** | Occurs when a Workflow Execution is forcefully terminated. |
| **Server Failure** | Originates from the Temporal Service itself. |

Do not extend the base failure class or any of its children in your code.
The provided classes are designed to work with Temporal's serialization mechanism, which converts failures to Protocol Buffer messages for communication across process and language boundaries.
Custom subclasses can break this serialization and lead to unexpected behavior.

### Application Failure

Application Failure is the failure type you use to communicate application-specific errors.
It is the only failure type designed to be created and thrown directly by your code.

When you throw an Application Failure, you can set these fields:

- **message**: A human-readable description of the error.
- **type**: A string that categorizes the failure (for example, `"InvalidInput"` or `"InsufficientFunds"`).
- **non_retryable**: A flag that prevents the operation from being retried, regardless of the Retry Policy.
- **details**: Additional data about the failure.

Any non-Temporal error thrown from an Activity is automatically converted to an Application Failure.
During this conversion, the error's type name, message, and call stack are preserved, and `non_retryable` is set to `false`.

### Failure Converters

When Temporal returns a failure, the default Failure Converter copies error messages and stack traces as plain text.
This text is accessible in the Web UI and through the CLI.

If your errors might contain sensitive information, you can encrypt the message and stack trace by configuring a custom Failure Converter with a codec.
See [Failure Converter](/failure-converter) for details.

## Workflow Task failures vs Workflow Execution failures {/* #task-vs-execution */}

When an error occurs in Workflow code, it produces one of two outcomes depending on the error type: a Workflow Task failure or a Workflow Execution failure.
Understanding the difference is important because they have very different implications.

|  | Workflow Task failure | Workflow Execution failure |
| :--- | :--- | :--- |
| **Caused by** | Non-Temporal errors (null reference, division by zero, type errors, non-determinism errors) | Temporal failures thrown by your code, such as Application Failure |
| **Retried?** | Yes, automatically | No |
| **Workflow state** | Preserved. You can fix the bug and redeploy without losing progress. | "Failed" state permanently. No more attempts are made. |
| **Typical cause** | A bug in the Workflow code | A permanent business logic failure where retrying with the same input will not help |

When a Workflow Task failure is retried:

1. The Worker removes the Workflow Execution from its cache.
2. The Temporal Service schedules a new Workflow Task on the original Task Queue.
3. A Worker picks up the Task and replays the Workflow Execution from Event History to restore the correct state before continuing.

## How errors propagate {/* #error-propagation */}

When an Activity fails, Temporal wraps the error in an Activity Failure before delivering it to the Workflow.
The Activity Failure provides context about the failure, including the Activity Type, the number of retry attempts, and the original cause.

The original error is in the `cause` field.
For example, if an Activity throws an Application Failure with `type: "InvalidInput"`, the Workflow receives an Activity Failure whose `cause` is that Application Failure.
If an Activity times out instead, the `cause` is a Timeout Failure.

This wrapping pattern applies to other execution types as well.
A failed Child Workflow delivers a Child Workflow Failure to the parent Workflow, with the original error in the `cause` field.

If a Temporal failure propagates unhandled through Workflow code, it fails the Workflow Execution.
The exception is Cancelled Failure, which puts the Workflow in "Cancelled" state instead of "Failed".

### The outermost error type determines retryability {/* #outermost-error-type */}

When an Activity returns an error, the SDK inspects the **outermost** error to decide how to represent the failure to the Temporal Service.
The SDK performs a type check on the outermost error and converts it to a Protocol Buffer [Failure](https://api-docs.temporal.io/#temporal.api.failure.v1.Failure) message.
If the outermost error is an Application Failure, the SDK preserves its `non_retryable` flag and `type` field in the resulting `ApplicationFailureInfo` proto.
If the outermost error is any other type, the SDK falls back to creating a default, **retryable** `ApplicationFailureInfo`.

The Temporal Service only inspects the **top-level** `failure_info` on the Failure proto when making retry decisions.
The original error is preserved in the `cause` chain, but the Service does not look at `cause` to determine retryability.

This means that wrapping an Application Failure in a generic language error silently loses the `non_retryable` flag.
If an Activity throws a non-retryable Application Failure, but your code catches it and re-throws it wrapped in a standard error, the Activity will be retried despite the original intent.

:::caution Wrapping errors can lose retryability flags
If you need to add context to an error, wrap it in another Application Failure that preserves the `non_retryable` flag.
Do not wrap Application Failures in generic language errors (such as `Error` in TypeScript, `Exception` in Python, or `fmt.Errorf` in Go), as this causes the SDK to treat the error as a new, retryable failure.
