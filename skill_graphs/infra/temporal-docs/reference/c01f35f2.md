
:::

To use a Side Effect in PHP, use the `Workflow::sideEffect()` function in your Workflow Definition to run non-deterministic code and return a value.

```php
#[Workflow\WorkflowMethod]
public function run()
{
    $random = yield Workflow::sideEffect(fn() => random_int(0, 100));
    if ($random < 50) {
        // ...
    } else {
        // ...
    }
}
```

---

## Workflow Timeouts - PHP SDK

## Workflow timeouts {/* #workflow-timeouts */}

Each Workflow timeout controls the maximum duration of a different aspect of a Workflow Execution.

Before we continue, we want to note that we generally do not recommend setting Workflow Timeouts, because Workflows are designed to be long-running and resilient.
Instead, setting a Timeout can limit its ability to handle unexpected delays or long-running processes.
If you need to perform an action inside your Workflow after a specific period of time, we recommend using a Timer.

Workflow timeouts are set when [starting the Workflow Execution](#workflow-timeouts).

- **[Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout)** - restricts the maximum amount of time that a single Workflow Execution can be executed.
- **[Workflow Run Timeout](/encyclopedia/detecting-workflow-failures#workflow-run-timeout):** restricts the maximum amount of time that a single Workflow Run can last.
- **[Workflow Task Timeout](/encyclopedia/detecting-workflow-failures#workflow-task-timeout):** restricts the maximum amount of time that a Worker can execute a Workflow Task.

Create an instance of `WorkflowOptions` in the Client code and set your timeout.

Available timeouts are:

- `withWorkflowExecutionTimeout()`
- `withWorkflowRunTimeout()`
- `withWorkflowTaskTimeout()`

```php
$workflow = $this->workflowClient->newWorkflowStub(
    DynamicSleepWorkflowInterface::class,
    WorkflowOptions::new()
        ->withWorkflowId(DynamicSleepWorkflow::WORKFLOW_ID)
        ->withWorkflowIdReusePolicy(WorkflowIdReusePolicy::WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE)
        // Set Workflow Timeout duration
        ->withWorkflowExecutionTimeout(CarbonInterval::minutes(2))
        // ->withWorkflowRunTimeout(CarbonInterval::minute(2))
        // ->withWorkflowTaskTimeout(CarbonInterval::minute(2))
);
```

### Workflow retries {/* #workflow-retries */}

A Retry Policy can work in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Use a [Retry Policy](/encyclopedia/retry-policies) to retry a Workflow Execution in the event of a failure.

Workflow Executions do not retry by default, and Retry Policies should be used with Workflow Executions only in certain situations.

A Retry Policy can be configured with an instance of the `RetryOptions` object.
To enable retries for a Workflow, you need to provide a Retry Policy object via `ChildWorkflowOptions` for Child Workflows or via `WorkflowOptions` for top-level Workflows.

```php
$workflow = $this->workflowClient->newWorkflowStub(
      CronWorkflowInterface::class,
      WorkflowOptions::new()->withRetryOptions(
        RetryOptions::new()->withInitialInterval(120)
      )
);
```

---

## Timers - PHP SDK

## What is a Timer? {/* #timers */}

A Workflow can set a durable timer for a fixed time period.
In some SDKs, the function is called `sleep()`, and in others, it's called `timer()`.

A Workflow can sleep for months.
Timers are persisted, so even if your Worker or Temporal Service is down when the time period completes, as soon as your Worker and Temporal Service are back up, the `sleep()` call will resolve and your code will continue executing.

Sleeping is a resource-light operation: it does not tie up the process, and you can run millions of Timers off a single Worker.

To set a Timer in PHP, use `Workflow::timer()` and pass the number of seconds you want to wait before continuing.

The following example yields a sleep method for 5 minutes.

```php
yield Workflow::timer(300); // sleep for 5 minutes
```

You cannot set a Timer invocation inside the `await` or `awaitWithTimeout` methods.

---

## Versioning - PHP SDK feature guide

Since Workflow Executions in Temporal can run for long periods — sometimes months or even years — it's common to need to make changes to a Workflow Definition, even while a particular Workflow Execution is in progress.

The Temporal Platform requires that Workflow code is [deterministic](/workflow-definition#deterministic-constraints). If you make a change to your Workflow code that would cause non-deterministic behavior on Replay, you'll need to use one of our Versioning methods to gracefully update your running Workflows. This only applies to Workflow orchestration logic. Non-deterministic work such as API calls, and database queries should be placed in Activities, which Temporal retries reliably.

With Versioning, you can modify your Workflow Definition so that new executions use the updated code, while existing ones continue running the original version.
There are two primary Versioning methods that you can use:

- [Worker Versioning](/production-deployment/worker-deployments/worker-versioning). The Worker Versioning feature allows you to tag your Workers and programmatically roll them out in versioned deployments, so that old Workers can run old code paths and new Workers can run new code paths.
- [Versioning with Patching](#php-sdk-patching-api). This method works by adding branches to your code tied to specific revisions. It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.

## Worker Versioning

Temporal's [Worker Versioning](/production-deployment/worker-deployments/worker-versioning) feature allows you to tag your Workers and programmatically roll them out in Deployment Versions, so that old Workers can run old code paths and new Workers can run new code paths. This way, you can pin your Workflows to specific revisions, avoiding the need for patching.

## Versioning with Patching {/* #php-sdk-patching-api */}

### Patching with GetVersion

A Patch defines a logical branch in a Workflow for a specific change, similar to a feature flag.
It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.
When you want to make substantive code changes that may affect existing Workflow Executions, create a patch.

Suppose you have an initial Workflow that runs `prePatchActivity`:

```php
#[WorkflowInterface]
class MyWorkflow
{
    private $activity;

    public function __construct()
    {
        $this->activity = Workflow::newActivityStub(
            YourActivityInterface::class,
            ActivityOptions::new()->withScheduleToStartTimeout(60)
        );
    }

    #[WorkflowMethod]
    public function runAsync()
    {
        $result = yield $this->activity->prePatchActivity();
    }
}
```

Suppose you replaced `prePatchActivity` with `postPatchActivity` and deployed the updated code.

If an existing Workflow Execution was started by the original version of the Workflow code, where `prePatchActivity` was run, and then resumed running on a new Worker where it was replaced with `postPatchActivity`, the server side Event History would be out of sync.
This would cause the Workflow to fail with a nondeterminism error.

To resolve this, you can use [Workflow::getVersion](https://php.temporal.io/classes/Temporal-Workflow.html#method_getVersion) to patch to your Workflow:

```php
#[WorkflowInterface]
class MyWorkflow
{
    // ...

    #[WorkflowMethod]
    public function runAsync()
    {
        $version = yield Workflow::getVersion('Step 1', Workflow::DEFAULT_VERSION, 1);

        $result = $version === Workflow::DEFAULT_VERSION
            ? yield $this->activity->prePatchActivity()
            : yield $this->activity->postPatchActivity();
    }
}
```

When `getVersion()` is run for the new Workflow Execution, it records a marker in the Event History so that all future calls to `getVersion()` for this change Id — `Step 1` in the example — on this Workflow Execution will always return the given version number, which is `1` in the example.

If you make an additional change, such as adding `anotherPatchActivity()`, you need to
add some additional code:

```php
#[WorkflowInterface]
class MyWorkflow
{
    // ...

    #[WorkflowMethod]
    public function runAsync()
    {
        $version = yield Workflow::getVersion('Step 1', Workflow::DEFAULT_VERSION, maxSupported: 2);

        $result = match($version) {
            Workflow::DEFAULT_VERSION => yield $this->activity->prePatchActivity()
            1 => yield $this->activity->postPatchActivity();
            2 => yield $this->activity->anotherPatchActivity();
        };
    }
}
```

Note that we changed `maxSupported` from 1 to 2.
A Workflow that has already passed this `getVersion()` call before it was introduced returns `DEFAULT_VERSION`.
A Workflow that was run with `maxSupported` set to 1 returns 1.
New Workflows return 2.

After all the Workflow Executions prior to version 1 have left retention, you can remove the code for that version:

```php
    #[WorkflowMethod]
    public function runAsync()
    {
        $version = yield Workflow::getVersion('Step 1', minSupported: 1, maxSupported: 2);

        $result = match($version) {
            1 => yield $this->activity->postPatchActivity();
            2 => yield $this->activity->anotherPatchActivity();
        };
    }
```

You'll note that `minSupported` has changed from `DEFAULT_VERSION` to `1`.
If an older version of the Workflow Execution history is replayed on this code, it fails because the minimum expected version is 1.
After all the Workflow Executions for version 1 have left retention, you can remove version 1 so that your code looks like the following:

```php
    #[WorkflowMethod]
    public function runAsync()
    {
        $version = yield Workflow::getVersion('Step 1', minSupported: 2, maxSupported: 2);

        $result = yield $this->activity->anotherPatchActivity();
    }
```

Patching allows you to make changes to currently running Workflows.
It is a powerful method for introducing compatible changes without introducing non-determinism errors.

### Workflow cutovers

To understand why Patching is useful, it's helpful to demonstrate cutting over an entire Workflow.

Since incompatible changes only affect open Workflow Executions of the same type, you can avoid determinism errors by creating a whole new Workflow when making changes.
To do this, you can copy the Workflow Definition function, giving it a different name, and register both names with your Workers.

For example, you would duplicate `MyWorkflow` as `MyWorkflowV2`:

```php
#[WorkflowInterface]
class MyWorkflow
{}

#[WorkflowInterface]
class MyWorkflowV2
{}
```

You would then need to update the Worker configuration, and any other identifier strings, to register both Workflow Types.
The downside of this method is that it requires you to duplicate code and to update any commands used to start the Workflow.
This can become impractical over time.
This method also does not provide a way to version any still-running Workflows -- it is essentially just a cutover, unlike Patching.

## Runtime checking {/* #runtime-checking */}

The Temporal PHP SDK performs a runtime check to help prevent obvious incompatible changes.
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
Instead, you should incorporate [Replay Testing](/develop/php/best-practices/testing-suite#replay) when making revisions.

---

## Plugins guide
