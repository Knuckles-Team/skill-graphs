
```typescript
try {
  await addAddress();
} catch (err) {
  if (err instanceof ActivityFailure && err.cause instanceof ApplicationFailure) {
    log.error(err.cause.message);
    throw err;
  }
}
```

This works differently in a Workflow than raising exceptions from Activities.
In an Activity, any Typescript exceptions or custom exceptions are converted to a Temporal `ApplicationFailure`.
In a Workflow, any exceptions that are raised other than an explicit Temporal `ApplicationFailure` will only fail that particular [Workflow Task](https://docs.temporal.io/tasks#workflow-task-execution) and be retried.
This includes any typical Typescript runtime errors like an `undefined` error that are raised automatically.
These errors are treated as bugs that can be corrected with a fixed deployment, rather than a reason for a Temporal Workflow Execution to return unexpectedly.

## Workflow Timeouts {/* #workflow-timeouts */}

**How to set Workflow Timeouts using the Temporal TypeScript SDK**

Each Workflow timeout controls the maximum duration of a different aspect of a Workflow Execution.

Before we continue, we want to note that we generally do not recommend setting Workflow Timeouts, because Workflows are designed to be long-running and resilient.
Instead, setting a Timeout can limit its ability to handle unexpected delays or long-running processes.
If you need to perform an action inside your Workflow after a specific period of time, we recommend using a Timer.

Workflow Timeouts are set when starting a Workflow using either the Client or Workflow API.

- **[Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout)** - restricts the maximum amount of time that a single Workflow Execution can be executed
- **[Workflow Run Timeout](/encyclopedia/detecting-workflow-failures#workflow-run-timeout):** restricts the maximum amount of time that a single Workflow Run can last
- **[Workflow Task Timeout](/encyclopedia/detecting-workflow-failures#workflow-task-timeout):** restricts the maximum amount of time that a Worker can execute a Workflow Task

The following properties can be set on the [`WorkflowOptions`](https://typescript.temporal.io/api/interfaces/client.WorkflowOptions/) when starting a Workflow using either the Client or Workflow API:

- [`workflowExecutionTimeout​`](https://typescript.temporal.io/api/interfaces/client.WorkflowOptions/#workflowexecutiontimeout)
- [`workflowRunTimeout`](https://typescript.temporal.io/api/interfaces/client.WorkflowOptions/#workflowruntimeout)
- [`workflowTaskTimeout`](https://typescript.temporal.io/api/interfaces/client.WorkflowOptions/#workflowtasktimeout)

```typescript
await client.workflow.start(example, {
  taskQueue,
  workflowId,
  // Set Workflow Timeout duration
  workflowExecutionTimeout: '1 day',
  // workflowRunTimeout: '1 minute',
  // workflowTaskTimeout: '30 seconds',
});
```

## Workflow retries {/* #workflow-retries */}

**How to set Workflow retries using the Temporal TypeScript SDK**

A Retry Policy can work in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Use a [Retry Policy](/encyclopedia/retry-policies) to retry a Workflow Execution in the event of a failure.

Workflow Executions do not retry by default, and Retry Policies should be used with Workflow Executions only in certain situations.

The Retry Policy can be set through the [`WorkflowOptions.retry`](https://typescript.temporal.io/api/interfaces/client.WorkflowOptions/#retry) property when starting a Workflow using either the Client or Workflow API.

```typescript
const handle = await client.workflow.start(example, {
  taskQueue,
  workflowId,
  retry: {
    maximumAttempts: 3,
    maximumInterval: '30 seconds',
  },
});
```

---

## Timers - TypeScript SDK

## What is a Timer? {/* #timers */}

A Workflow can set a durable Timer for a fixed time period.
In some SDKs, the function is called `sleep()`, and in others, it's called `timer()`.

A Workflow can sleep for months.
Timers are persisted, so even if your Worker or Temporal Service is down when the time period completes, as soon as your Worker and Temporal Service are back up, the `sleep()` call will resolve and your code will continue executing.

Sleeping is a resource-light operation: it does not tie up the process, and you can run millions of Timers off a single Worker.

## Asynchronous design patterns in TypeScript {/* #asynchronous-design-patterns */}

The real value of `sleep` and `condition` is in knowing how to use them to model asynchronous business logic.
Here are some examples we use the most; we welcome more if you can think of them!

<details>
<summary>
Racing Timers
</summary>

Use `Promise.race` with Timers to dynamically adjust delays.

```ts
export async function processOrderWorkflow({
  orderProcessingMS,
  sendDelayedEmailTimeoutMS,
}: ProcessOrderOptions): Promise<void> {
  let processing = true;
  const processOrderPromise = processOrder(orderProcessingMS).then(() => {
    processing = false;
  });

  await Promise.race([processOrderPromise, sleep(sendDelayedEmailTimeoutMS)]);

  if (processing) {
    await sendNotificationEmail();
    await processOrderPromise;
  }
}
```

</details>
<details>
<summary>
Racing Signals
</summary>

Use `Promise.race` with Signals and Triggers to have a promise resolve at the earlier of either system time or human intervention.

```ts

const userInteraction = new Trigger<boolean>();
const completeUserInteraction = defineSignal('completeUserInteraction');

export async function yourWorkflow(userId: string) {
  setHandler(completeUserInteraction, () => userInteraction.resolve(true)); // programmatic resolve
  const userInteracted = await Promise.race([
    userInteraction,
    sleep('30 days'),
  ]);
  if (!userInteracted) {
    await sendReminderEmail(userId);
  }
}
```

You can invert this to create a reminder pattern where the promise resolves _if_ no Signal is received.

:::caution Antipattern: Racing sleep.then

Be careful when racing a chained `sleep`.
This might cause bugs because the chained `.then` will still continue to execute.

```ts
await Promise.race([
  sleep('5s').then(() => (status = 'timed_out')),
  somethingElse.then(() => (status = 'processed')),
]);

if (status === 'processed') await complete(); // takes more than 5 seconds
// status = timed_out
```

:::

</details>

<details>
<summary>
Updatable Timer
</summary>

Here is how you can build an updatable Timer with `condition`:

```ts

// usage
export async function countdownWorkflow(): Promise<void> {
  const target = Date.now() + 24 * 60 * 60 * 1000; // 1 day!!!
  const timer = new UpdatableTimer(target);
  console.log('timer set for: ' + new Date(target).toString());
  wf.setHandler(setDeadlineSignal, (deadline) => {
    // send in new deadlines via Signal
    timer.deadline = deadline;
    console.log('timer now set for: ' + new Date(deadline).toString());
  });
  wf.setHandler(timeLeftQuery, () => timer.deadline - Date.now());
  await timer; // if you send in a signal with a new time, this timer will resolve earlier!
  console.log('countdown done!');
}
```

This is available in the third-party package [`temporal-time-utils`](https://www.npmjs.com/package/temporal-time-utils#user-content-updatabletimer), where you can also see the implementation:

```ts
// implementation
export class UpdatableTimer implements PromiseLike<void> {
  deadlineUpdated = false;
  #deadline: number;

  constructor(deadline: number) {
    this.#deadline = deadline;
  }

  private async run(): Promise<void> {
    /* eslint-disable no-constant-condition */
    while (true) {
      this.deadlineUpdated = false;
      if (
        !(await wf.condition(
          () => this.deadlineUpdated,
          this.#deadline - Date.now(),
        ))
      ) {
        break;
      }
    }
  }

  then<TResult1 = void, TResult2 = never>(
    onfulfilled?: (value: void) => TResult1 | PromiseLike<TResult1>,
    onrejected?: (reason: any) => TResult2 | PromiseLike<TResult2>,
  ): PromiseLike<TResult1 | TResult2> {
    return this.run().then(onfulfilled, onrejected);
  }

  set deadline(value: number) {
    this.#deadline = value;
    this.deadlineUpdated = true;
  }

  get deadline(): number {
    return this.#deadline;
  }
}
```

</details>

---

## Versioning - TypeScript SDK

Since Workflow Executions in Temporal can run for long periods — sometimes months or even years — it's common to need to make changes to a Workflow Definition, even while a particular Workflow Execution is in progress.

The Temporal Platform requires that Workflow code is [deterministic](/workflow-definition#deterministic-constraints).
If you make a change to your Workflow code that would cause non-deterministic behavior on Replay, you'll need to use one of our Versioning methods to gracefully update your running Workflows.

Common causes include adding, removing, or reordering `await` calls on Command-producing APIs such as Activities and timers. Each `await` is a yield point that affects the Command sequence seen during Replay.

With Versioning, you can modify your Workflow Definition so that new executions use the updated code, while existing ones continue running the original version.
There are two primary Versioning methods that you can use:

- [Worker Versioning](/production-deployment/worker-deployments/worker-versioning). The Worker Versioning feature allows you to tag your Workers and programmatically roll them out in versioned deployments, so that old Workers can run old code paths and new Workers can run new code paths.
- [Versioning with Patching](#patching). This method works by adding branches to your code tied to specific revisions. It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.

:::danger
Support for the experimental Worker Versioning method before 2025 will be removed from Temporal Server in March 2026. Refer to the [latest Worker Versioning docs](/worker-versioning) for guidance. You can still refer to the [Worker Versioning Legacy](/develop/typescript/worker-versioning-legacy) docs if needed.
:::

## Versioning with Patching {/* #patching */}

### Adding a patch

A Patch defines a logical branch in a Workflow for a specific change, similar to a feature flag.
It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.
When you want to make substantive code changes that may affect existing Workflow Executions, create a patch.

Suppose you have an initial Workflow that runs `activityA`:

```ts
// v1
export async function myWorkflow(): Promise<void> {
  await activityA();
  await sleep('1 days'); // arbitrary long sleep to simulate a long running workflow we need to patch
  await activityThatMustRunAfterA();
}
```

Now, you want to update your code to run `activityB` instead. This represents your desired end state.

```ts
// vFinal
export async function myWorkflow(): Promise<void> {
  await activityB();
  await sleep('1 days');
}
```

The problem is that you cannot deploy this `vFinal` revision directly until you're certain there are no more running Workflows created using the `v1` code, otherwise you are likely to cause a nondeterminism error.
Instead, you'll need to use the [`patched`](https://typescript.temporal.io/api/namespaces/workflow#patched) function to check which version of the code should be executed.

Patching is a three-step process:

1. Patch in any new, updated code using the `patched()` function. Run the new patched code alongside old code.
2. Remove old code and use `deprecatePatch()` to mark a particular patch as deprecated.
3. Once there are no longer any open Workflow Executions of the previous version of the code, remove `deprecatePatch()`.
   Let's walk through this process in sequence.

### Patching in new code

Using `patched` inserts a marker into the Event History.
During Replay, if a Worker encounters a history with that marker, it will fail the Workflow task when the Workflow code doesn't produce the same patch marker (in this case `your-change-id`).
This ensures you can safely deploy code from `v2` as a "feature flag" alongside the original version (`v1`).

```ts
// v2

export async function myWorkflow(): Promise<void> {
  if (patched('my-change-id')) {
    await activityB();
    await sleep('1 days');
  } else {
    await activityA();
    await sleep('1 days');
    await activityThatMustRunAfterA();
  }
}
```

### Deprecating patches {/* #deprecated-patches */}

After ensuring that all Workflows started with `v1` code have left retention, you can [deprecate the patch](https://typescript.temporal.io/api/namespaces/workflow#deprecatepatch).

Once your Workflows are no longer running the pre-patch code paths, you can deploy your code with `deprecatePatch()`.
These Workers will be running the most up-to-date version of the Workflow code, which no longer requires the patch.
Deprecated patches serve as a bridge between the final stage of the patching process and the final state that no longer has patches. They function similarly to regular patches by adding a marker to the Event History. However, this marker won't cause a replay failure when the Workflow code doesn't produce it.

```ts
// v3

export async function myWorkflow(): Promise<void> {
  deprecatePatch('my-change-id');
  await activityB();
  await sleep('1 days');
}
```

### Removing a patch {/* #deploy-new-code */}

Once your pre-patch Workflows have left retention, you can then safely deploy Workers that no longer use either the `patched()` or `deprecatePatch()` calls:

Patching allows you to make changes to currently running Workflows.
It is a powerful method for introducing compatible changes without introducing non-determinism errors.

### Workflow cutovers

To understand why Patching is useful, it's helpful to demonstrate cutting over an entire Workflow.

Since incompatible changes only affect open Workflow Executions of the same type, you can avoid determinism errors by creating a whole new Workflow when making changes.
To do this, you can copy the Workflow Definition function, giving it a different name, and register both names with your Workers.

For example, you would duplicate `PizzaWorkflow` as `PizzaWorkflowV2`:

```typescript
function pizzaWorkflow(order: PizzaOrder): Promise<OrderConfirmation> {
  // this function contains the original code
}

function pizzaWorkflowV2(order: PizzaOrder): Promise<OrderConfirmation> {
  // this function contains the updated code
}
```

You would then need to update the Worker configuration, and any other identifier strings, to register both Workflow Types:

```typescript
const worker = await Worker.create({
  workflowsPath: require.resolve('./workflows'),
  // other configurations
});
```

The downside of this method is that it requires you to duplicate code and to update any commands used to start the Workflow.
This can become impractical over time.
This method also does not provide a way to version any still-running Workflows -- it is essentially just a cutover, unlike Patching.

### Testing a Workflow for replay safety

To determine whether your Workflow your needs a patch, or that you've patched it successfully, you should incorporate [Replay Testing](/develop/typescript/best-practices/testing-suite#replay).

## Worker Versioning

Temporal's [Worker Versioning](/production-deployment/worker-deployments/worker-versioning) feature allows you to tag your Workers and programmatically roll them out in Deployment Versions, so that old Workers can run old code paths and new Workers can run new code paths. This way, you can pin your Workflows to specific revisions, avoiding the need for patching.

---

## Worker performance

This page documents metrics and configurations that drive the efficiency of your Worker fleet.
It provides coverage of performance metric families, Worker configuration options, Task Queue information, backlog counts, Task rates, and how to evaluate Worker availability.
This content covers practical methods for querying Task Queue information, and strategies for tuning Workers and Task Queue processing so you manage your resources effectively.

:::info

All metrics on this page are prepended with the `temporal_` prefix.
For example, `worker_task_slots_available` is actually `temporal_worker_task_slots_available` when used.
The omitted prefix makes the names more readable and descriptive.

:::

## Worker performance concepts {/* #worker-performance-concepts */}

A Worker's performance characteristics are affected by, but not limited to, the following elements.

### Task slots {/* #slots */}

A **Worker Task Slot**, represents the capacity of a Temporal Worker to execute a single concurrent Task.
Slots are crucial for managing the workload and performance of Workers in a Temporal application.
They're used for both Workflow and Activity Tasks.
When a Worker starts processing a Task, it occupies one slot.
The number of available slots directly affects how many tasks a Worker can handle simultaneously.

### Slot suppliers {/* #slot-suppliers */}

A **Slot Supplier** defines a strategy to provide slots for a Worker, increasing or decreasing the Worker's slot count.
The supplier determines when it's acceptable to begin a new Task.
Each supplier manages one slot type.
There are slot types for Activity, Workflow, Nexus, or Local Activity Tasks.
An available slot determines whether or not a Worker is willing to poll for, and execute, a new Task of that type.

Slot supplier strategies include manual assignment of fixed slot counts and resource-balanced "auto-tuner" assignment.
Resource-based suppliers adjust slot counts based on CPU and memory resources.
Available slot suppliers include:

- **Fixed Size Slot Suppliers**:
  Hands out slots up to a preset limit.
  This is useful if you have a concrete idea of how many resources your tasks are going to consume, and can easily determine an upper bound on how many should run at once.
  When you need the absolute best performance, review your hardware and environment characteristics.
  This information lets you calculate an appropriate fixed-size limit.
  Evaluate the maximum number of slots you can support without oversubscribing or hitting out-of-memory conditions ("OOMing").
  Using that value with a fixed-size supplier provides optimal results with the least overhead.

- **Resource-Based Slot Suppliers**:
  Hands out slots based on real-time CPU and memory usage.
  You set target utilization for both CPU and memory and the Slot Supplier tries to reach those values without exceeding them under load.
  A resource-based supplier will account for memory limits imposed in containerized environments.
  It dynamically adjusts the number of available slots for different task types with respect to current system resources.

:::info

When running in a containerized environment, all SDKs use cgroups for both CPU and memory. CPU is accounted for at the container level.

:::

- **Custom Slot Suppliers**:
  Hands out slots based on the custom logic that you define.
  Use this approach when you need complete control over when Workers accept and execute Tasks.
  For implementation details, see [Implement Custom Slot Suppliers](#custom-slot-implementation).

:::caution

- You cannot guarantee that the targets for resource-based suppliers won't ever be exceeded.
  Resources consumed during a task can't be known ahead of time.

- Read about [choosing an appropriate slot supplier type](#choosing-slot-supplier-types) before picking one.

- Worker tuners supersede the existing `maxConcurrentXXXTask` style Worker options.
  Using both styles will cause an error at Worker initialization time.

:::

### Worker tuning {/* #worker-tuning */}

Worker tuning is the process of defining customized slot suppliers for the different task slots of a Worker to fine-tune its performance.
You use special types called **Worker tuners** that assign slot suppliers to various Task Types, including Worker, Activity, Nexus, and Local Activity Tasks.

For more on how to configure and use Worker tuners, refer to [Worker runtime performance tuning](#worker-performance-tuning).

:::caution

Worker tuners supersede the existing `maxConcurrentXXXTask` style Worker options.
  Using both styles will cause an error at Worker initialization time.

:::

### Task Pollers

A Worker's **Task Pollers** play a crucial role in the Temporal architecture by efficiently ingesting work to Workers to support scalable, resilient Workflow Execution.
Pollers create long-polling connections to the Temporal Service and actively poll a Task Queue for Tasks to process. When a Task Poller receives a Task, it delivers the Task to the appropriate Executor Slot for processing.

Temporal SDKs implement support for *Poller Autoscaling*, which dynamically adjusts the number of pollers in use to maximize throughput for a given number of workers and the size of the task backlog.
Temporal recommends using Poller Autoscaling for the majority of use cases, as manually setting the number of pollers too high or too low for your workload will result in decreased performance.
To configure Poller Autoscaling, see [Configuring Poller Options](#configuring-poller-options) and samples for each Temporal SDK.

### Eager task execution

:::caution
Eager start does not respect Worker versioning. An eagerly started Workflow may run on any available local Worker even if that Worker is not the Current or Ramping version of its Worker deployment.
:::

As a latency optimization, Activity and Workflow Tasks may be started eagerly in a local Worker under the right circumstances.

#### Eager Activity Start

Eager Activity Start may happen automatically if the Worker processing a Workflow Task has also registered the Activity Definition being called.
If it does, it may try to reserve an Activity Slot for the execution of the Activity, and the server may respond to the Workflow Task completion with the Activity Task for the worker to execute immediately.

#### Eager Workflow Start

<ReleaseNoteHeader type="publicPreview" languages={["Go", "Java", "Python", ".NET"]}>
  Eager Workflow Start is enabled for all Temporal Cloud users and self-hosted Temporal Server 1.29.0+. No additional configuration or access request is needed. However, you must set `Request-Eager-Start` to true when starting each Workflow for Eager Workflow Start to be used.
</ReleaseNoteHeader>

Eager Workflow Start reduces the latency required to initiate a Workflow execution.
It is recommended for short-lived Workflows that use Local Activities to interact with external services, especially when these interactions are initiated in the first Workflow Task and the Workflow is deployed near the Temporal Server to minimize network delay.

This feature is particularly beneficial for Workflows with a “happy path” that must begin external interactions within tens of milliseconds, while still relying on Temporal’s server-driven retries and compensation mechanisms to ensure reliability in failure scenarios.

**Quick Start**

Eager Workflow Start requires the Starter and the Worker to share a Client located in the same process and setting the `request_eager_start` (or similar name) to true in the Start Workflow call.
When set, and the Worker has a Workflow Task slot available and the Workflow Definition registered, the Worker can execute the first task of the Workflow locally without first making a round-trip to the Temporal Server.
This is typically most useful in combination with a Local Activity executing in the first Workflow Task, since other Workflow API calls that require waiting on something will force a round-trip.

:::tip RESOURCES

- [Go SDK - Code sample](https://github.com/temporalio/samples-go/tree/main/eager-workflow-start)
- [Java SDK - Code sample](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/hello/HelloEagerWorkflowStart.java)
- Python SDK - use `request_eager_start` when calling `start_workflow` or `execute_workflow`
- .NET SDK - use `RequestEagerStart` in your `WorkflowOptions` when starting a workflow
- [Blog: Improving Latency with Eager Workflow Start](https://temporal.io/blog/improving-latency-with-eager-workflow-start)

:::

**How it works**

The traditional way to start a Workflow decouples the starter program from the worker by sharing a Task Queue name between them, similar to a publish/subscribe pattern.
This has many advantages: for example, we can reliably schedule a Workflow Execution without a running Worker, or separate the Worker and Workflow implementation from the Starter application and host them independently.

But decoupling also makes it harder to optimize for latency.
Instead, when the **Starter and Worker are collocated in the same process** and aware of each other, they can interact while bypassing the server, saving a few time-intensive operations.

<CaptionedImage
    src="/img/develop/worker-performance/eager-workflow-start-flow.png"
    title="Eager Workflow Start"
/>

The above figure shows Eager Workflow Start in action:

1. The process begins with the Starter setting `request_eager_start` (or similar name) to true in the Start Workflow Options.
1. The SDK will try to locate a local Worker that is willing to execute the first Workflow Task, and reserve an execution slot for it.
1. If successful, the SDK will provide a hint to the server that eager mode is preferred for the new Workflow.
1. The server not only registers the start of the Workflow in history, it also assigns the first Workflow Task to the Starter, all in the same DB update.
