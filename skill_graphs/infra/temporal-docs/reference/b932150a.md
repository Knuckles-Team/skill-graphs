Temporal's Go SDK `Selector`s are similar and act as a replacement.
They can block on sending and receiving from Channels but as a bonus can listen on Future deferred work.
Usage of Selectors to defer and process work (in place of Go's `select`) are necessary in order to ensure deterministic Workflow code execution (though using `select` in Activity code is fine).

## Full API example {/* #api-example */}

The API is sufficiently different from `select` that it bears documenting:

```go
func SampleWorkflow(ctx workflow.Context) error {
	// standard Workflow setup code omitted...

	// API Example: declare a new selector
	selector := workflow.NewSelector(ctx)

	// API Example: defer code execution until the Future that represents Activity result is ready
	work := workflow.ExecuteActivity(ctx, ExampleActivity)
	selector.AddFuture(work, func(f workflow.Future) {
		// deferred code omitted...
	})

	// more parallel timers and activities initiated...

	// API Example: receive information from a Channel
	var signalVal string
	channel := workflow.GetSignalChannel(ctx, channelName)
	selector.AddReceive(channel, func(c workflow.ReceiveChannel, more bool) {
		// matching on the channel doesn't consume the message.
	 	// So it has to be explicitly consumed here
		c.Receive(ctx, &signalVal)
		// do something with received information
	})

	// API Example: block until the next Future is ready to run
	// important! none of the deferred code runs until you call selector.Select
	selector.Select(ctx)

	// Todo: document selector.HasPending
}
```

## Use Selectors with Futures

You usually add `Futures` after `Activities`:

```go
// API Example: defer code execution until after an activity is done
work := workflow.ExecuteActivity(ctx, ExampleActivity)
selector.AddFuture(work, func(f workflow.Future) {
	// deferred code omitted...
})
```

Calling `ExecuteActivity` by itself doesn't result in actual Activity execution. It results in a command that gets batched with others when there's a yield point in the Workflow definition. Your `Futures` won't run until you call `selector.Select(ctx)`. So no calls to `ExecuteActivity` should result in commands being sent to the server until `selector.Select` is called.

A call to `selector.Select(ctx)` doesn't actually execute a `Future`, but it _requests_ execution for a `Future`. So this is a point where the SDK will communicate the command to execute the Activity to the server.

```go
  // API Example: blocking conditionally
  if somecondition != nil {
    selector.Select(ctx)
  }

  // API Example: popping off all remaining Futures
  for i := 0; i < len(someArray); i++ {
    selector.Select(ctx) // this will wait for one branch
    // you can interrupt execution here
  }
```

A Future matches only once per Selector instance even if Select is called multiple times.
If multiple items are available, the order of matching is not defined.

## Use Selectors with Timers

An important use case of futures is setting up a race between a timer and a pending activity, effectively adding a "soft" timeout that doesn't result in any errors or retries of that activity.

For example, [the Timer sample](https://github.com/temporalio/samples-go/blob/master/timer) shows how you can write a long running order processing operation where:

- if processing takes too long, we send out a notification email to user about the delay, but we won't cancel the operation
- if the operation finishes before the timer fires, then we want to cancel the timer.

```go
var processingDone bool
f := workflow.ExecuteActivity(ctx, OrderProcessingActivity)
selector.AddFuture(f, func(f workflow.Future) {
	processingDone = true
	// cancel timerFuture
	cancelHandler()
})

// use timer future to send notification email if processing takes too long
timerFuture := workflow.NewTimer(childCtx, processingTimeThreshold)
selector.AddFuture(timerFuture, func(f workflow.Future) {
	if !processingDone {
		// processing is not done yet when timer fires, send notification email
		_ = workflow.ExecuteActivity(ctx, SendEmailActivity).Get(ctx, nil)
	}
})

// wait the timer or the order processing to finish
selector.Select(ctx)
```

We create timers with the `workflow.NewTimer` API.

## Use Selectors with Channels

`selector.AddReceive(channel, func(c workflow.ReceiveChannel, more bool) {})` is the primary mechanism which receives messages from `Channels`.

```go
// API Example: receive information from a Channel
var signalVal string
channel := workflow.GetSignalChannel(ctx, channelName)
selector.AddReceive(channel, func(c workflow.ReceiveChannel, more bool) {
	c.Receive(ctx, &signalVal)
	// do something with received information
})
```

Merely matching on the channel doesn't consume the message; it has to be explicitly consumed with a `c.Receive(ctx, &signalVal)` call.

## Query Selector state

You can use the `selector.HasPending` API to ensure that signals are not lost when a Workflow is closed (e.g. by `ContinueAsNew`).

## Learn more

Usage of Selectors is best learned by example:

- Setting up a race condition between an Activity and a Timer, and conditionally execute ([Timer example](https://github.com/temporalio/samples-go/blob/14980b3792cc3a8447318fefe9a73fe0a580d4b9/timer/workflow.go))
- Receiving information in a Channel ([Mutex example](https://github.com/temporalio/samples-go/blob/14980b3792cc3a8447318fefe9a73fe0a580d4b9/mutex/mutex_workflow.go))
- Looping through a list of work and scheduling them all in parallel ([DSL example](https://github.com/temporalio/samples-go/blob/14980b3792cc3a8447318fefe9a73fe0a580d4b9/dsl/workflow.go))
- Executing activities in parallel, pick the first result, cancel remainder ([Pick First example](https://github.com/temporalio/samples-go/blob/14980b3792cc3a8447318fefe9a73fe0a580d4b9/pickfirst/pickfirst_workflow.go))

---

## Side Effects - Go SDK

Side Effects are used to execute non-deterministic code, such as generating a UUID or a random number, without compromising determinism in the Workflow.
This is done by storing the non-deterministic results of the Side Effect into the Workflow [Event History](/workflow-execution/event#event-history).

A Side Effect does not re-execute during a Replay. Instead, it returns the recorded result from the Workflow Execution Event History.

Side Effects should not fail. An exception that is thrown from the Side Effect causes failure and retry of the current Workflow Task.

An Activity or a Local Activity may also be used instead of a Side effect, as its result is also persisted in Workflow Execution History.

:::note

You shouldn't modify the Workflow state inside a Side Effect function, because it is not reexecuted during Replay. Side Effect function should be used to return a value.

:::

Use the [`SideEffect`](https://pkg.go.dev/go.temporal.io/sdk/workflow#SideEffect) function from the `go.temporal.io/sdk/workflow` package to execute a [Side Effect](/workflow-execution/event#side-effect) directly in your Workflow.

Pass it an instance of `context.Context` and the function to execute.

The `SideEffect` API returns a Future, an instance of [`converter.EncodedValue`](https://pkg.go.dev/go.temporal.io/sdk/workflow#SideEffect).

Use the `Get` method on the Future to retrieve the result of the Side Effect.

**Correct implementation**

The following example demonstrates the correct way to use `SideEffect`:

```go
encodedRandom := workflow.SideEffect(ctx, func(ctx workflow.Context) interface{} {
 return rand.Intn(100)
})

var random int
encodedRandom.Get(&random)
// ...
}
```

**Incorrect implementation**

The following example demonstrates how NOT to use `SideEffect`:

```go
// Warning: This is an incorrect example.
// This code is non-deterministic.
var random int
workflow.SideEffect(func(ctx workflow.Context) interface{} {
      random = rand.Intn(100)
      return nil
})
// random will always be 0 in replay, so this code is non-deterministic.
```

On replay the provided function is not executed, the random number will always be 0, and the Workflow Execution could take a different path, breaking determinism.

## Mutable Side Effects {/* #mutable-side-effects */}

Mutable Side Effects execute the provided function once, and then it looks up the History of the value with the given Workflow ID.

- If there is no existing value, then it records the function result as a value with the given Workflow Id on the History.
- If there is an existing value, then it compares whether the existing value from the History has changed from the new function results, by calling the equals function.
  - If the values are equal, then it returns the value without recording a new Marker Event
  - If the values aren't equal, then it records the new value with the same ID on the History.

:::note

During a Workflow Execution, every new Side Effect call results in a new Marker recorded on the Event History; whereas Mutable Side Effects only records a new Marker on the Event History if the value for the Side Effect ID changes or is set the first time.

During a Replay, Mutable Side Effects will not execute the function again. Instead, it returns the exact same value that was returned during the Workflow Execution.

:::

To use [`MutableSideEffect()`](https://pkg.go.dev/go.temporal.io/sdk/workflow#MutableSideEffect) in Go, provide a unique name within the scope of the workflow.

```go
if err := workflow.MutableSideEffect(ctx, "configureNumber", get, eq).Get(&number); err != nil {
    panic("can't decode number:" + err.Error())
  }
```

---

## Workflow Timeouts - Go SDK

## Workflow timeouts {/* #workflow-timeouts */}

Each Workflow timeout controls the maximum duration of a different aspect of a Workflow Execution.

Workflow timeouts are set when [starting the Workflow Execution](#workflow-timeouts).

Before we continue, we want to note that we generally do not recommend setting Workflow Timeouts, because Workflows are designed to be long-running and resilient.
Instead, setting a Timeout can limit its ability to handle unexpected delays or long-running processes.
If you need to perform an action inside your Workflow after a specific period of time, we recommend using a Timer.

- **[Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout)** - restricts the maximum amount of time that a single Workflow Execution can be executed.
- **[Workflow Run Timeout](/encyclopedia/detecting-workflow-failures#workflow-run-timeout):** restricts the maximum amount of time that a single Workflow Run can last.
- **[Workflow Task Timeout](/encyclopedia/detecting-workflow-failures#workflow-task-timeout):** restricts the maximum amount of time that a Worker can execute a Workflow Task.

Create an instance of [`StartWorkflowOptions`](https://pkg.go.dev/go.temporal.io/sdk/client#StartWorkflowOptions) from the `go.temporal.io/sdk/client` package, set a timeout, and pass the instance to the `ExecuteWorkflow` call.

Available timeouts are:

- `WorkflowExecutionTimeout`
- `WorkflowRunTimeout`
- `WorkflowTaskTimeout`

```go
workflowOptions := client.StartWorkflowOptions{
  // ...
  // Set Workflow Timeout duration
  WorkflowExecutionTimeout: 24 * 365 * 10 * time.Hour,
  // WorkflowRunTimeout: 24 * 365 * 10 * time.Hour,
  // WorkflowTaskTimeout: 10 * time.Second,
  // ...
}
workflowRun, err := c.ExecuteWorkflow(context.Background(), workflowOptions, YourWorkflowDefinition)
if err != nil {
  // ...
}
```

## Workflow Retry Policy {/* #workflow-retries */}

A Retry Policy can work in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Use a [Retry Policy](/encyclopedia/retry-policies) to retry a Workflow Execution in the event of a failure.

Workflow Executions do not retry by default, and Retry Policies should be used with Workflow Executions only in certain situations.

Create an instance of a [`RetryPolicy`](https://pkg.go.dev/go.temporal.io/sdk/temporal#RetryPolicy) from the `go.temporal.io/sdk/temporal` package and provide it as the value to the `RetryPolicy` field of the instance of `StartWorkflowOptions`.

- Type: [`RetryPolicy`](https://pkg.go.dev/go.temporal.io/sdk/temporal#RetryPolicy)
- Default: None

```go
retrypolicy := &temporal.RetryPolicy{
  InitialInterval:    time.Second,
  BackoffCoefficient: 2.0,
  MaximumInterval:    time.Second * 100,
}
workflowOptions := client.StartWorkflowOptions{
  RetryPolicy: retrypolicy,
  // ...
}
workflowRun, err := temporalClient.ExecuteWorkflow(context.Background(), workflowOptions, YourWorkflowDefinition)
if err != nil {
  // ...
}
```

---

## Timers - Go SDK

A Workflow can set a Durable Timer for a fixed time period.
In some SDKs, the function is called `sleep()`, and in others, it's called `timer()`.

A Workflow can sleep for days, months, or even years.
Timers are persisted, so even if your Worker or Temporal Service is down when the time period completes, as soon as your Worker and Temporal Service are back up, the `sleep()` call will resolve and your code will continue executing.

Sleeping is a resource-light operation: it does not tie up the process, and you can run millions of Timers off a single Worker.

To set a Timer in Go, use the [`NewTimer()`](https://pkg.go.dev/go.temporal.io/sdk/workflow#NewTimer) function and pass the duration you want to wait before continuing.

```go
timer := workflow.NewTimer(timerCtx, duration)
```

To set a sleep duration in Go, use the [`sleep()`](https://pkg.go.dev/go.temporal.io/sdk/workflow#Sleep) function and pass the duration you want to wait before continuing.
A zero or negative sleep duration causes the function to return immediately.

```go
sleep = workflow.Sleep(ctx, 10*time.Second)
```

For more information, see the [Timer](https://github.com/temporalio/samples-go/tree/main/timer) example in the [Go Samples repository](https://github.com/temporalio/samples-go).

---

## Versioning - Go SDK

Since Workflow Executions in Temporal can run for long periods — sometimes months or even years — it's common to need to make changes to a Workflow Definition, even while a particular Workflow Execution is in progress.

The Temporal Platform requires that Workflow code is [deterministic](/workflow-definition#deterministic-constraints). If you make a change to your Workflow code that would cause non-deterministic behavior on Replay, you'll need to use one of our Versioning methods to gracefully update your running Workflows. This only applies to Workflow orchestration logic. Non-deterministic work such as API calls, and database queries should be placed in Activities, which Temporal retries reliably.

With Versioning, you can modify your Workflow Definition so that new executions use the updated code, while existing ones continue running the original version.
There are two primary Versioning methods that you can use:

- [Worker Versioning](/production-deployment/worker-deployments/worker-versioning). The Worker Versioning feature allows you to tag your Workers and programmatically roll them out in versioned deployments, so that old Workers can run old code paths and new Workers can run new code paths.
- [Versioning with Patching](#patching). This method works by adding branches to your code tied to specific revisions. It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.

:::danger
Support for the experimental Worker Versioning method before 2025 will be removed from Temporal Server in March 2026. Refer to the [latest Worker Versioning docs](/worker-versioning) for guidance. You can still refer to the [Worker Versioning Legacy](/develop/go/worker-versioning-legacy) docs if needed.
:::

## Worker Versioning

Temporal's [Worker Versioning](/production-deployment/worker-deployments/worker-versioning) feature allows you to tag your Workers and programmatically roll them out in Deployment Versions, so that old Workers can run old code paths and new Workers can run new code paths. This way, you can pin your Workflows to specific revisions, avoiding the need for patching.

## Versioning with Patching {/* #patching */}

### Patching with GetVersion

A Patch defines a logical branch in a Workflow for a specific change, similar to a feature flag.
It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.
When you want to make substantive code changes that may affect existing Workflow Executions, create a patch.

Consider the following Workflow Definition:

```go
func YourWorkflow(ctx workflow.Context, data string) (string, error) {
        ao := workflow.ActivityOptions{
                ScheduleToStartTimeout: time.Minute,
                StartToCloseTimeout:    time.Minute,
        }
        ctx = workflow.WithActivityOptions(ctx, ao)
        var result1 string
        err := workflow.ExecuteActivity(ctx, ActivityA, data).Get(ctx, &result1)
        if err != nil {
                return "", err
        }
        var result2 string
        err = workflow.ExecuteActivity(ctx, ActivityB, result1).Get(ctx, &result2)
        return result2, err
}
```

Suppose you replaced `ActivityA` with `ActivityC` and deployed the updated code.

If an existing Workflow Execution was started by the original version of the Workflow code, where `ActivityA` was run, and then resumed running on a new Worker where it was replaced with `ActivityC`, the server side Event History would be out of sync.
This would cause the Workflow to fail with a nondeterminism error.

To resolve this, you can use `workflow.GetVersion()` to patch to your Workflow:

```go
var err error
v := workflow.GetVersion(ctx, "Step1", workflow.DefaultVersion, 1)
if v == workflow.DefaultVersion {
        err = workflow.ExecuteActivity(ctx, ActivityA, data).Get(ctx, &result1)
} else {
        err = workflow.ExecuteActivity(ctx, ActivityC, data).Get(ctx, &result1)
}
if err != nil {
        return "", err
}

var result2 string
err = workflow.ExecuteActivity(ctx, ActivityB, result1).Get(ctx, &result2)
return result2, err
```

When `workflow.GetVersion()` is run for the new Workflow Execution, it records a marker in the Event History so that all future calls to `GetVersion` for this change Id — `Step 1` in the example — on this Workflow Execution will always return the given version number, which is `1` in the example.

If you make an additional change, such as replacing ActivityC with ActivityD, you need to
add some additional code:

```go
v := workflow.GetVersion(ctx, "Step1", workflow.DefaultVersion, 2)
if v == workflow.DefaultVersion {
        err = workflow.ExecuteActivity(ctx, ActivityA, data).Get(ctx, &result1)
} else if v == 1 {
        err = workflow.ExecuteActivity(ctx, ActivityC, data).Get(ctx, &result1)
} else {
        err = workflow.ExecuteActivity(ctx, ActivityD, data).Get(ctx, &result1)
}
```

Note that we changed `maxSupported` from 1 to 2.
A Workflow that has already passed this `GetVersion()` call before it was introduced returns `DefaultVersion`.
A Workflow that was run with `maxSupported` set to 1 returns 1.
New Workflows return 2.

After all the Workflow Executions prior to version 1 have left retention, you can remove the code for that version:

```go
v := workflow.GetVersion(ctx, "Step1", 1, 2)
if v == 1 {
        err = workflow.ExecuteActivity(ctx, ActivityC, data).Get(ctx, &result1)
} else {
        err = workflow.ExecuteActivity(ctx, ActivityD, data).Get(ctx, &result1)
}
```

You'll note that `minSupported` has changed from `DefaultVersion` to `1`.
If an older version of the Workflow Execution history is replayed on this code, it fails because the minimum expected version is 1.
After all the Workflow Executions for version 1 have left retention, you can remove version 1 so that your code looks like the following:

```go
_ := workflow.GetVersion(ctx, "Step1", 2, 2)
err = workflow.ExecuteActivity(ctx, ActivityD, data).Get(ctx, &result1)
```

Note that we have preserved the call to `GetVersion()`. There are two reasons to preserve this call:

1. This ensures that if there is a Workflow Execution still running for an older version, it will
   fail here and not proceed.
2. If you need to make additional changes for `Step1`, such as changing ActivityD to ActivityE, you
   only need to update `maxVersion` from 2 to 3 and branch from there.

You need to preserve only the first call to `GetVersion()` for each `changeID`.
All subsequent calls to `GetVersion()` with the same change Id are safe to remove.
If necessary, you can remove the first `GetVersion()` call, but you need to ensure the following:

- All executions with an older version have left retention.
- You can no longer use `Step1` for the changeId. If you need to make changes to that same part in
  the future, such as change from ActivityD to ActivityE, you would need to use a different changeId
  like `Step1-fix2`, and start minVersion from DefaultVersion again. The code would look like the
  following:

```go
v := workflow.GetVersion(ctx, "Step1-fix2", workflow.DefaultVersion, 1)
if v == workflow.DefaultVersion {
        err = workflow.ExecuteActivity(ctx, ActivityD, data).Get(ctx, &result1)
} else {
        err = workflow.ExecuteActivity(ctx, ActivityE, data).Get(ctx, &result1)
}
```

You can add multiple calls to `GetVersion` in a single Workflow.
This can become challenging to manage if you have many long-running Workflows, as you will wind up with many code branches over time.
To clean these up, you can gradually deprecate older Workflow versions.

### Deprecating old Workflow versions

You can safely remove support for older Workflow versions once you are certain that there are no longer any open Workflow Executions based on that version. You can use the following [List Filter](/list-filter) syntax for this (the 1 near the end of the last line represents the version number):

```
WorkflowType = "PizzaWorkflow"
    AND ExecutionStatus = "Running"
    AND TemporalChangeVersion="ChangedNotificationActivityType-1"
```

Since Workflow Executions that were started before `GetVersion` was added to the code won't have the associated Marker in their Event History, you'll need to use a different query to determine if any of those are still running:

```
WorkflowType = "PizzaWorkflow"
    AND ExecutionStatus = "Running"
    AND TemporalChangeVersion IS NULL
```

If you have found that there are no longer any open executions for the first two versions of the Workflow, for example, then you could remove support for them by changing the code as shown below:

```go
version := GetVersion(ctx, "ChangedNotificationActivityType", 2, 3)
if version  == 2 {
    err = workflow.ExecuteActivity(ctx, SendTextMessage).Get(ctx, nil)
} else {
    err = workflow.ExecuteActivity(ctx, SendTweet).Get(ctx, nil)
}
```

Patching allows you to make changes to currently running Workflows.
It is a powerful method for introducing compatible changes without introducing non-determinism errors.

### Workflow cutovers

To understand why Patching is useful, it's helpful to demonstrate cutting over an entire Workflow.

Since incompatible changes only affect open Workflow Executions of the same type, you can avoid determinism errors by creating a whole new Workflow when making changes.
To do this, you can copy the Workflow Definition function, giving it a different name, and register both names with your Workers.

For example, you would duplicate `PizzaWorkflow` as `PizzaWorkflowV2`:

```go
func PizzaWorkflow(ctx workflow.Context, order PizzaOrder) (OrderConfirmation, error) {
    // this function contains the original code
}

func PizzaWorkflowV2(ctx workflow.Context, order PizzaOrder) (OrderConfirmation, error) {
    // this function contains the updated code
}
```

You can use any name you like for the new function, so long as the first character remains uppercase (this is a requirement for any Workflow Definition, since it must use an exported function).
Using some type of version identifier, such as V2 in this example, will make it easier to identify the change.

You would then need to update the Worker configuration, and any other identifier strings, to register both Workflow Types:

```go
w.RegisterWorkflow(pizza.PizzaWorkflow)
w.RegisterWorkflow(pizza.PizzaWorkflowV2)
```

The downside of this method is that it requires you to duplicate code and to update any commands used to start the Workflow.
This can become impractical over time.
This method also does not provide a way to version any still-running Workflows -- it is essentially just a cutover, unlike Patching.

## Runtime checking {/* #runtime-checking */}

The Temporal Go SDK performs a runtime check to help prevent obvious incompatible changes.
Adding, removing, or reordering any of these methods without Versioning triggers the runtime check and results in a nondeterminism error:

- `workflow.ExecuteActivity()`
- `workflow.ExecuteChildWorkflow()`
- `workflow.NewTimer()`
- `workflow.RequestCancelWorkflow()`
- `workflow.SideEffect()`
- `workflow.SignalExternalWorkflow()`
- `workflow.Sleep()`

The runtime check does not perform a thorough check.
For example, it does not check on the Activity's input arguments or the Timer duration.
Each Temporal SDK implements these sanity checks differently, and they are not a complete check for non-deterministic changes.
Instead, you should incorporate [Replay Testing](/develop/go/best-practices/testing-suite#replay) when making revisions.

---

## Develop durable applications with Temporal SDKs

The Temporal SDK developer guides provide a comprehensive overview of the structures, primitives, and features used in [Temporal Application](/temporal#temporal-application) development.
