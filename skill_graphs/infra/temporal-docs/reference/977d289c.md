
To pause a Scheduled Workflow Execution in Java, use the `pause()` method on the `ScheduleHandle`.
You can pass a `note` to the `pause()` method to provide a reason for pausing the schedule.

```java
ScheduleHandle handle = client.getHandle("schedule-id")
handle.pause("Pausing the schedule for now");
```

### How to trigger a Schedule in Java {/* #trigger-schedule */}

The trigger action triggers an immediate action with a given Schedule. By default, this action is subject to the Overlap Policy of the Schedule. This command is helpful when you want to execute a Workflow outside of its scheduled time.

To trigger a Scheduled Workflow Execution in Java, use the `trigger()` method on the `ScheduleHandle`.

```java
ScheduleHandle handle = client.getHandle("schedule-id")
handle.trigger();
```

### How to update a Schedule in Java {/* #update-schedule */}

The update action enables you to update an existing Schedule. This command is useful when you need to modify the Schedule's configuration, such as changing the start time, end time, or interval.

Create a function that takes `ScheduleUpdateInput` and returns `ScheduleUpdate`.
To update a Schedule, use a callback to build the update from the description.
The following example updates the Schedule to set a limited number of actions.

```java
ScheduleHandle handle = client.getHandle("schedule-id")
handle.update(
    (ScheduleUpdateInput input) -> {
      Schedule.Builder builder = Schedule.newBuilder(input.getDescription().getSchedule());
      // Make the schedule paused to demonstrate how to unpause a schedule
      builder.setState(
          ScheduleState.newBuilder()
              .setLimitedAction(true)
              .setRemainingActions(10)
              .build());
      return new ScheduleUpdate(builder.build());
    });
```

## How to set a Cron Schedule in Java {/* #cron-schedule */}

:::caution Cron support is not recommended

We recommend using [Schedules](https://docs.temporal.io/schedule) instead of Cron Jobs.
Schedules were built to provide a better developer experience, including more configuration options and the ability to update or pause running Schedules.

:::

A [Temporal Cron Job](/cron-job) is the series of Workflow Executions that occur when a Cron Schedule is provided in the call to spawn a Workflow Execution.

A Cron Schedule is provided as an option when the call to spawn a Workflow Execution is made.

Set the Cron Schedule with the [`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html) instance in the Client code using [`WorkflowOptions.Builder.setCronSchedule`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

Setting `setCronSchedule` changes the Workflow Execution into a Temporal Cron Job.
The default timezone for a Cron is UTC.

- Type: `String`
- Default: None

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    YourWorker.yourclient.newWorkflowStub(
        YourWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("YourWF")
                .setTaskQueue(YourWorker.TASK_QUEUE)
                // Set Cron Schedule
                .setCronSchedule("* * * * *")
                .build());
```

Temporal Workflow Schedule Cron strings follow this format:

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
│ │ │ │ │
* * * * *
```

For more details, see the [Cron Sample](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/hello/HelloCron.java)

## Start Delay {/* #start-delay */}

**How to delay the start of a Workflow Execution using Start Delay with the Temporal Java SDK.**

Use the `StartDelay` to schedule a Workflow Execution at a specific one-time future point rather than on a recurring schedule.

Create an instance of [`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html) in the Client code and set `StartDelay` using `setStartDelay`.

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("YourWorkflow")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                // Start the workflow in 12 hours
                .setStartDelay(Duration.ofHours(12))
                .build());
```

---

## Side Effects - Java SDK

## Side Effects {/* #side-effects */}

Side Effects are used to execute non-deterministic code, such as generating a UUID or a random number, without compromising determinism in the Workflow.
This is done by storing the non-deterministic results of the Side Effect into the Workflow [Event History](/workflow-execution/event#event-history).

A Side Effect does not re-execute during a Replay. Instead, it returns the recorded result from the Workflow Execution Event History.

Side Effects should not fail. An exception that is thrown from the Side Effect causes failure and retry of the current Workflow Task.

An Activity or a Local Activity may also be used instead of a Side effect, as its result is also persisted in Workflow Execution History.

:::note

You shouldn't modify the Workflow state inside a Side Effect function, because it is not reexecuted during Replay. Side Effect function should be used to return a value.

:::

To use a Side Effect in Java, set the [`sideEffect()`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#sideEffect(java.lang.Class,io.temporal.workflow.Functions.Func)) function in your Workflow Execution and return the non-deterministic code.

```java
int random = Workflow.sideEffect(Integer.class, () -> random.nextInt(100));
if random < 50 {
       ....
} else {
       ....
}
```

Here's another example that uses `sideEffect()`.

```java
// implementation of the @WorkflowMethod
public void execute() {
    int randomInt = Workflow.sideEffect( int.class, () -> {
        Random random = new SecureRandom();
        return random.nextInt();
    });

    String userHome = Workflow.sideEffect(String.class, () -> System.getenv("USER_HOME"));

    if(randomInt % 2 == 0) {
        // ...
    } else {
        // ...
    }
}
```

Java also provides a deterministic method to generate random numbers or random UUIDs.

To generate random numbers in a deterministic method, use [`newRandom()`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#newRandom).

```java
// implementation of the @WorkflowMethod
public void execute() {
    int randomInt = Workflow.newRandom().nextInt();
    // ...
}
```

To generate a random UUID in a deterministic method, use [`randomUUID()`](https://www.javadoc.io/static/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#newRandom()).

```java
// implementation of the @WorkflowMethod
public void execute() {
    String randomUUID = Workflow.randomUUID().toString();
    // ...
}
```

---

## Workflow Timeouts - Java SDK

## Workflow timeouts {/* #workflow-timeouts */}

Each Workflow timeout controls the maximum duration of a different aspect of a Workflow Execution.

Workflow timeouts are set when [starting the Workflow Execution](#workflow-timeouts).

Before we continue, we want to note that we generally do not recommend setting Workflow Timeouts, because Workflows are designed to be long-running and resilient.
Instead, setting a Timeout can limit its ability to handle unexpected delays or long-running processes.
If you need to perform an action inside your Workflow after a specific period of time, we recommend using a Timer.

- **[Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout)** - restricts the maximum amount of time that a single Workflow Execution can be executed.
- **[Workflow Run Timeout](/encyclopedia/detecting-workflow-failures#workflow-run-timeout):** restricts the maximum amount of time that a single Workflow Run can last.
- **[Workflow Task Timeout](/encyclopedia/detecting-workflow-failures#workflow-task-timeout):** restricts the maximum amount of time that a Worker can execute a Workflow Task.

Create an instance of [`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html) in the Client code and set your timeout.

Available timeouts are:

- [setWorkflowExecutionTimeout()](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html#setWorkflowExecutionTimeout(java.time.Duration))
- [setWorkflowRunTimeout()](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html#setWorkflowRunTimeout(java.time.Duration))
- [setWorkflowTaskTimeout()](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html#setWorkflowTaskTimeout(java.time.Duration))

```java
//create Workflow stub for YourWorkflowInterface
YourWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("YourWorkflow")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                // Set Workflow Timeout duration
                .setWorkflowExecutionTimeout(Duration.ofSeconds(10))
                // .setWorkflowRunTimeout(Duration.ofSeconds(10))
                // .setWorkflowTaskTimeout(Duration.ofSeconds(10))
                .build());
```

## Workflow Retry Policy {/* #workflow-retries */}

**How to set a Workflow Retry Policy in Java.**

A Retry Policy can work in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Use a [Retry Policy](/encyclopedia/retry-policies) to retry a Workflow Execution in the event of a failure.

Workflow Executions do not retry by default, and Retry Policies should be used with Workflow Executions only in certain situations.

To set a Workflow Retry Options in the [`WorkflowStub`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html) instance use [`WorkflowOptions.Builder.setWorkflowRetryOptions`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.Builder.html).

- Type: `RetryOptions`
- Default: `Null` which means no retries will be attempted.

```java
//create Workflow stub for GreetWorkflowInterface
GreetWorkflowInterface workflow1 =
    WorkerGreet.greetclient.newWorkflowStub(
        GreetWorkflowInterface.class,
        WorkflowOptions.newBuilder()
                .setWorkflowId("GreetWF")
                .setTaskQueue(WorkerGreet.TASK_QUEUE)
                // Set Workflow Retry Options
                .setRetryOptions(RetryOptions.newBuilder()
                .build());
```

---

## Timers - Java SDK

## What is a Timer? {/* #timers */}

A Workflow can set a durable Timer for a fixed time period.
In some SDKs, the function is called `sleep()`, and in others, it's called `timer()`.

A Workflow can sleep for months.

Timers are persisted, so even if your Worker or Temporal Service is down when the time period completes, as soon as your Worker and Temporal Service are back up, the `Workflow.sleep()` call resolves and your code continues executing.

Sleeping is a resource-light operation: it does not tie up the process, and you can run millions of Timers off a single Worker.

To set a Timer in Java, use [`sleep()`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#sleep) and pass the number of seconds you want to wait before continuing.

```java
sleep(5);
```

---

## Versioning - Java SDK

Since Workflow Executions in Temporal can run for long periods — sometimes months or even years — it's common to need to make changes to a Workflow Definition, even while a particular Workflow Execution is in progress.

The Temporal Platform requires that Workflow code is [deterministic](/workflow-definition#deterministic-constraints). If you make a change to your Workflow code that would cause non-deterministic behavior on Replay, you'll need to use one of our Versioning methods to gracefully update your running Workflows. This only applies to Workflow orchestration logic. Non-deterministic work such as API calls, and database queries should be placed in Activities, which Temporal retries reliably.

With Versioning, you can modify your Workflow Definition so that new executions use the updated code, while existing ones continue running the original version.
There are two primary Versioning methods that you can use:

- [Worker Versioning](/production-deployment/worker-deployments/worker-versioning). The Worker Versioning feature allows you to tag your Workers and programmatically roll them out in versioned deployments, so that old Workers can run old code paths and new Workers can run new code paths.
- [Versioning with Patching](#patching). This method works by adding branches to your code tied to specific revisions. It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.

:::danger
Support for the experimental Worker Versioning method before 2025 will be removed from Temporal Server in March 2026. Refer to the [latest Worker Versioning docs](/worker-versioning) for guidance. You can still refer to the [Worker Versioning Legacy](/develop/java/worker-versioning-legacy) docs if needed.
:::

## Worker Versioning

Temporal's [Worker Versioning](/production-deployment/worker-deployments/worker-versioning) feature allows you to tag your Workers and programmatically roll them out in Deployment Versions, so that old Workers can run old code paths and new Workers can run new code paths. This way, you can pin your Workflows to specific revisions, avoiding the need for patching.

## Versioning with Patching {/* #patching */}

### Patching with GetVersion

A Patch defines a logical branch in a Workflow for a specific change, similar to a feature flag.
It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.
When you want to make substantive code changes that may affect existing Workflow Executions, create a patch.

Consider the following Workflow Definition:

```java
public void processFile(Arguments args) {
    String localName = null;
    String processedName = null;
    try {
        localName = activities.download(args.getSourceBucketName(), args.getSourceFilename());
        processedName = activities.processFile(localName);
        activities.upload(args.getTargetBucketName(), args.getTargetFilename(), processedName);
    } finally {
        if (localName != null) { // File was downloaded.
            activities.deleteLocalFile(localName);
        }
        if (processedName != null) { // File was processed.
            activities.deleteLocalFile(processedName);
        }
    }
}
```

Imagine you want to revise this Workflow by adding another Activity to calculate a file checksum.
If an existing Workflow Execution was started by the original version of the Workflow code, where there was no `calculateChecksum()` Activity, and then resumed running on a new Worker where this Activity had been added, the server side Event History would be out of sync.
This would cause the Workflow to fail with a nondeterminism error.

To resolve this, you can use `workflow.GetVersion()` to patch to your Workflow:

```java
public void processFile(Arguments args) {
    String localName = null;
    String processedName = null;
    try {
        localName = activities.download(args.getSourceBucketName(), args.getSourceFilename());
        processedName = activities.processFile(localName);
        int version = Workflow.getVersion("checksumAdded", Workflow.DEFAULT_VERSION, 1);
        if (version == Workflow.DEFAULT_VERSION) {
            activities.upload(args.getTargetBucketName(), args.getTargetFilename(), processedName);
        } else {
            long checksum = activities.calculateChecksum(processedName);
            activities.uploadWithChecksum(
                args.getTargetBucketName(), args.getTargetFilename(), processedName, checksum);
        }
    } finally {
        if (localName != null) { // File was downloaded.
            activities.deleteLocalFile(localName);
        }
        if (processedName != null) { // File was processed.
            activities.deleteLocalFile(processedName);
        }
    }
}
```

When `workflow.GetVersion()` is run for the new Workflow Execution, it records a marker in the Event History so that all future calls to `GetVersion` for this change id — `checksumAdded` in the example — on this Workflow Execution will always return the given version number, which is `1` in the example.

After all the Workflow Executions prior to version 1 have left retention, you can remove the code for that version.

```java
public void processFile(Arguments args) {
    String localName = null;
    String processedName = null;
    try {
        localName = activities.download(args.getSourceBucketName(), args.getSourceFilename());
        processedName = activities.processFile(localName);
        // getVersion call is left here to ensure that any attempt to replay history
        // for a different version fails. It can be removed later when there is no possibility
        // of this happening.
        Workflow.getVersion("checksumAdded", 1, 1);
        long checksum = activities.calculateChecksum(processedName);
        activities.uploadWithChecksum(
            args.getTargetBucketName(), args.getTargetFilename(), processedName, checksum);
    } finally {
        if (localName != null) { // File was downloaded.
            activities.deleteLocalFile(localName);
        }
        if (processedName != null) { // File was processed.
            activities.deleteLocalFile(processedName);
        }
    }
}
```

### Adding support for versioned Workflow visibility in the Event History

When you invoke `getVersion`, the SDK can record an `UpsertWorkflowSearchAttribute` Event in the history.
This adds a [Search Attribute](/search-attribute#default-search-attribute) named `TemporalChangeVersion` that allows you to filter Workflows based on their version.

#### Enable automatic upsert (Java SDK v1.30.0+)

Starting with Java SDK v1.30.0, you can enable automatic `TemporalChangeVersion` upserts by setting `enableUpsertVersionSearchAttributes` in `WorkflowImplementationOptions`:

```java
WorkflowImplementationOptions options = WorkflowImplementationOptions.newBuilder()
    .setEnableUpsertVersionSearchAttributes(true)
    .build();

worker.registerWorkflowImplementationTypes(options, YourWorkflowImpl.class);
```

When enabled, each call to `Workflow.getVersion` automatically upserts the `TemporalChangeVersion` Search Attribute with a keyword list of `"<Change ID>-<Version>"` entries.

:::note

This option is backwards compatible and safe to enable on running Workflows.
However, once enabled, you cannot roll back to a version of the SDK that does not support this option.

:::

#### Upsert manually

If you are using a version of the Java SDK earlier than v1.30.0, or prefer to control the upsert yourself, you can set the attribute manually.

```java

public static final SearchAttributeKey<List<String>> TEMPORAL_CHANGE_VERSION =
    SearchAttributeKey.forKeywordList("TemporalChangeVersion");
```

Set this attribute when you call `getVersion`:

```java
int version = Workflow.getVersion("MovedThankYouAfterLoop", Workflow.DEFAULT_VERSION, 1);

if (version != Workflow.DEFAULT_VERSION) {
  Workflow.upsertTypedSearchAttributes(TEMPORAL_CHANGE_VERSION
      .valueSet(Arrays.asList("MovedThankYouAfterLoop-" + version)));
}
```

For multiple `getVersion` calls, collect all version changes and set the attribute once:

```java
List<String> list = new ArrayList<String>();
int versionOne = Workflow.getVersion("versionOne", Workflow.DEFAULT_VERSION, 1);
int versionTwo = Workflow.getVersion("versionTwo", Workflow.DEFAULT_VERSION, 1);
if (versionOne != Workflow.DEFAULT_VERSION) {
   list.add("versionOne-" + versionOne);
}
if (versionTwo != Workflow.DEFAULT_VERSION) {
   list.add("versionTwo-" + versionTwo);
}
Workflow.upsertTypedSearchAttributes(TEMPORAL_CHANGE_VERSION.valueSet(list));
```

Patching allows you to make changes to currently running Workflows.
It is a powerful method for introducing compatible changes without introducing non-determinism errors.

### Workflow cutovers

To understand why Patching is useful, it's helpful to demonstrate cutting over an entire Workflow.

Since incompatible changes only affect open Workflow Executions of the same type, you can avoid determinism errors by creating a whole new Workflow when making changes.
To do this, you can copy the Workflow Definition function, giving it a different name, and register both names with your Workers.

For example, you would duplicate `PizzaWorkflow` as `PizzaWorkflowV2`:

```java

@WorkflowInterface
public interface PizzaWorkflow {

  @WorkflowMethod
  public OrderConfirmation pizzaWorkflow(PizzaOrder order);
}

public class PizzaWorkflowImpl{

  @Override
  public OrderConfirmation pizzaWorkflow(PizzaOrder order){
      // implementation code omitted for this example
  }
}

@WorkflowInterface
public interface PizzaWorkflowV2 {

  @WorkflowMethod
  public OrderConfirmation pizzaWorkflow(PizzaOrder order);
}

public class PizzaWorkflowImplV2 implements PizzaWorkflowV2{

  @Override
  public OrderConfirmation pizzaWorkflow(PizzaOrder order){
      // implementation code omitted for this example
  }
}
```

It is necessary to create a separate interface because a Workflow Interface can only have one Workflow Method.

You would then need to update the Worker configuration, and any other identifier strings, to register both Workflow Types:

```java
worker.registerWorkflowImplementationTypes(PizzaWorkflowImpl.class);
worker.registerWorkflowImplementationTypes(PizzaWorkflowImplV2.class);
```

The downside of this method is that it requires you to duplicate code and to update any commands used to start the Workflow.
This can become impractical over time.
This method also does not provide a way to version any still-running Workflows -- it is essentially just a cutover, unlike Patching.

### Testing a Workflow for replay safety

To determine whether your Workflow your needs a patch, or that you've patched it successfully, you should incorporate [Replay Testing](/develop/java/best-practices/testing-suite#replay).

---

## Asynchronous Activity Completion - PHP SDK

## How to asynchronously complete an Activity {/* #asynchronous-activity-completion */}

[Asynchronous Activity Completion](/activity-execution#asynchronous-activity-completion) enables the Activity Function
to return without the Activity Execution completing.

There are three steps to follow:

1. The Activity provides the external system with identifying information needed to complete the Activity Execution.
   Identifying information can be a [Task Token](/activity-execution#task-token), or a combination of Namespace,
   Workflow Id, and Activity Id.
2. The Activity Function completes in a way that identifies it as waiting to be completed by an external system.
3. The Temporal Client is used to Heartbeat and complete the Activity.

Sometimes Workflows need to perform certain operations in parallel.

Invoking activity stub without the use of `yield` will return the Activity result promise which can be resolved at later
moment. Calling `yield` on promise blocks until a result is available.

> Activity promise also exposes `then` method to construct promise chains. Read more about Promises
> [here](https://github.com/reactphp/promise).

Alternatively you can explicitly wrap your code (including `yield` constructs) using `Workflow::async` which will
execute nested code in parallel with main Workflow code. Call `yield` on Promise returned by `Workflow::async` to merge
execution result back to primary Workflow method.

```php
public function greet(string $name): \Generator
{
    // Workflow::async runs it's activities and child workflows in a separate coroutine. Use keyword yield to merge
    // it back to parent process.

    $first = Workflow::async(
        function () use ($name) {
            $hello = yield $this->greetingActivity->composeGreeting('Hello', $name);
            $bye = yield $this->greetingActivity->composeGreeting('Bye', $name);

            return $hello . '; ' . $bye;
        }
    );

    $second = Workflow::async(
        function () use ($name) {
            $hello = yield $this->greetingActivity->composeGreeting('Hola', $name);
            $bye = yield $this->greetingActivity->composeGreeting('Chao', $name);

            return $hello . '; ' . $bye;
        }
    );

    // blocks until $first and $second complete
    return (yield $first) . "\n" . (yield $second);
}
```

**Async completion**

There are certain scenarios when moving on from an Activity upon completion of its function is not possible or
desirable. For example, you might have an application that requires user input to complete the Activity. You could
