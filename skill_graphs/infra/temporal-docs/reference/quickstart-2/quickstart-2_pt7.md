                            ImmutableMap.of(
                                    "GetCustomerGreeting",
                                    // Set Activity Execution timeout
                                    ActivityOptions.newBuilder()
                                        .setScheduleToCloseTimeout(Duration.ofSeconds(5))
                                        // .setStartToCloseTimeout(Duration.ofSeconds(2))
                                        // .setScheduleToStartTimeout(Duration.ofSeconds(5))
                                        .build()))
                    .build();
```

:::note

If you define options per-Activity Type options with `WorkflowImplementationOptions.setActivityOptions()`, setting them again specifically with `ActivityStub` in a Workflow will override this setting.

:::

## Java ActivityOptions reference {/* #activity-options-reference */}

Use [`ActivityOptions`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityOptions.Builder.html) to configure how to invoke an Activity Execution.

You can set Activity Options using an `ActivityStub` within a Workflow implementation, or per-Activity using `WorkflowImplementationOptions` within a Worker.
Note that if you define options per-Activity Type options with `WorkflowImplementationOptions.setActivityOptions()`, setting them again specifically with `ActivityStub` in a Workflow will override this setting.

The following table lists all `ActivityOptions` that can be configured for an Activity invocation.

| Option                                                 | Required                                           | Type                     |
| ------------------------------------------------------ | -------------------------------------------------- | ------------------------ |
| [`setScheduleToCloseTimeout`](#scheduletoclosetimeout) | Yes (if `StartToCloseTimeout` is not specified)    | Duration                 |
| [`setScheduleToStartTimeout`](#scheduletostarttimeout) | No                                                 | Duration                 |
| [`setStartToCloseTimeout`](#starttoclosetimeout)       | Yes (if `ScheduleToCloseTimeout` is not specified) | Duration                 |
| [`setHeartbeatTimeout`](#heartbeattimeout)             | No                                                 | Duration                 |
| [`setTaskQueue`](#taskqueue)                           | No                                                 | String                   |
| [`setRetryOptions`](#retryoptions)                     | No                                                 | RetryOptions             |
| [`setCancellationType`](#setcancellationtype)          | No                                                 | ActivityCancellationType |

### ScheduleToCloseTimeout

To set a [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout), use [`ActivityOptions.newBuilder.setScheduleToCloseTimeout​`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityOptions.Builder.html).

This or `StartToCloseTimeout` must be set.

- Type: `Duration`
- Default: Unlimited.
  Note that if `WorkflowRunTimeout` and/or `WorkflowExecutionTimeout` are defined in the Workflow, all Activity retries will stop when either or both of these timeouts are reached.

You can set Activity Options using an `ActivityStub` within a Workflow implementation, or per-Activity using `WorkflowImplementationOptions` within a Worker.
Note that if you define options per-Activity Type options with `WorkflowImplementationOptions.setActivityOptions()`, setting them again specifically with `ActivityStub` in a Workflow will override this setting.

- With `ActivityStub`

  ```java
  GreetingActivities activities = Workflow.newActivityStub(GreetingActivities.class,
                  ActivityOptions.newBuilder()
                          .setScheduleToCloseTimeout(Duration.ofSeconds(5))
                          .build());
  ```

- With `WorkflowImplementationOptions`

  ```java
  WorkflowImplementationOptions options =
              WorkflowImplementationOptions.newBuilder()
                      .setActivityOptions(
                              ImmutableMap.of(
                                      "GetCustomerGreeting",
                                      ActivityOptions.newBuilder()
                                          .setScheduleToCloseTimeout(Duration.ofSeconds(5))
                                          .build()))
                      .build();
  ```

### ScheduleToStartTimeout

To set a [Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout), use [`ActivityOptions.newBuilder.setScheduleToStartTimeout​`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityOptions.Builder.html).

- Type: `Duration`
- Default: Unlimited. This timeout is non-retryable.

You can set Activity Options using an `ActivityStub` within a Workflow implementation, or per-Activity using `WorkflowImplementationOptions` within a Worker.
Note that if you define options per-Activity Type options with `WorkflowImplementationOptions.setActivityOptions()`, setting them again specifically with `ActivityStub` in a Workflow will override this setting.

- With `ActivityStub`

  ```java
  GreetingActivities activities = Workflow.newActivityStub(GreetingActivities.class,
                  ActivityOptions.newBuilder()
                          .setScheduleToStartTimeout(Duration.ofSeconds(5))
                          // note that either StartToCloseTimeout or ScheduleToCloseTimeout are
                          // required when setting Activity options.
                          .setScheduletoCloseTimeout(Duration.ofSeconds(20))
                          .build());
  ```

- With `WorkflowImplementationOptions`

  ```java
  WorkflowImplementationOptions options =
             WorkflowImplementationOptions.newBuilder()
                      .setActivityOptions(
                              ImmutableMap.of(
                                "GetCustomerGreeting",
                                ActivityOptions.newBuilder()
                                    .setScheduleToStartTimeout(Duration.ofSeconds(5))
                                    .build()))
                      .build();
  ```

### StartToCloseTimeout

To set a [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout), use [`ActivityOptions.newBuilder.setStartToCloseTimeout​`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityOptions.Builder.html).

This or `ScheduleToClose` must be set.

- Type: `Duration`
- Default: Defaults to [`ScheduleToCloseTimeout`](#scheduletoclosetimeout) value

You can set Activity Options using an `ActivityStub` within a Workflow implementation, or per-Activity using `WorkflowImplementationOptions` within a Worker.
Note that if you define options per-Activity Type options with `WorkflowImplementationOptions.setActivityOptions()`, setting them again specifically with `ActivityStub` in a Workflow will override this setting.

- With `ActivityStub`

  ```java
  GreetingActivities activities = Workflow.newActivityStub(GreetingActivities.class,
              ActivityOptions.newBuilder()
                      .setStartToCloseTimeout(Duration.ofSeconds(2))
                      .build());
  ```

- With `WorkflowImplementationOptions`

  ```java
  WorkflowImplementationOptions options =
              WorkflowImplementationOptions.newBuilder()
                      .setActivityOptions(
                              ImmutableMap.of(
                                "EmailCustomerGreeting",
                                      ActivityOptions.newBuilder()
                                            // Set Activity Execution timeout (single run)
                                            .setStartToCloseTimeout(Duration.ofSeconds(2))
                                            .build()))
                      .build();
  ```

### HeartbeatTimeout

To set a [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout), use [`ActivityOptions.newBuilder.setHeartbeatTimeout`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityOptions.Builder.html).

- Type: `Duration`
- Default: None

You can set Activity Options using an `ActivityStub` within a Workflow implementation, or per-Activity using `WorkflowImplementationOptions` within a Worker.
Note that if you define options per-Activity Type options with `WorkflowImplementationOptions.setActivityOptions()`, setting them again specifically with `ActivityStub` in a Workflow will override this setting.

- With `ActivityStub`

  ```java
  private final GreetingActivities activities =
      Workflow.newActivityStub(
          GreetingActivities.class,
          ActivityOptions.newBuilder()
              // note that either StartToCloseTimeout or ScheduleToCloseTimeout are
              // required when setting Activity options.
              .setStartToCloseTimeout(Duration.ofSeconds(5))
              .setHeartbeatTimeout(Duration.ofSeconds(2))
              .build());
  ```

- With `WorkflowImplementationOptions`

  ```java
  WorkflowImplementationOptions options =
              WorkflowImplementationOptions.newBuilder()
                      .setActivityOptions(
                              ImmutableMap.of(
                                "EmailCustomerGreeting",
                                      ActivityOptions.newBuilder()
                                          // note that either StartToCloseTimeout or ScheduleToCloseTimeout are
                                          // required when setting Activity options.
                                            .setStartToCloseTimeout(Duration.ofSeconds(5))
                                            .setHeartbeatTimeout(Duration.ofSeconds(2))
                                            .build()))
                      .build();
  ```

### TaskQueue

- Type: `String`
- Default: Defaults to the Task Queue that the Workflow was started with.

- With `ActivityStub`

  ```java
  GreetingActivities activities = Workflow.newActivityStub(GreetingActivities.class,
                  ActivityOptions.newBuilder()
                          // note that either StartToCloseTimeout or ScheduleToCloseTimeout are required when
                          // setting Activity options.
                          .setStartToCloseTimeout(Duration.ofSeconds(5))
                          .setTaskQueue("yourTaskQueue")
                          .build());
  ```

- With `WorkflowImplementationOptions`

  ```java
  WorkflowImplementationOptions options =
              WorkflowImplementationOptions.newBuilder()
                      .setActivityOptions(
                              ImmutableMap.of(
                                "EmailCustomerGreeting",
                                      ActivityOptions.newBuilder()
                                            // note that either StartToCloseTimeout or ScheduleToCloseTimeout are
                                            // required when setting Activity options.
                                            .setStartToCloseTimeout(Duration.ofSeconds(5))
                                            .setTaskQueue("yourTaskQueue")
                                            .build()))
                      .build();
  ```

See [Task Queue](/task-queue)

### RetryOptions

To set a Retry Policy, known as the [Retry Options](/encyclopedia/retry-policies) in Java, use [`ActivityOptions.newBuilder.setRetryOptions()`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityOptions.Builder.html).

- Type: `RetryOptions`
- Default: Server-defined Activity Retry policy.

- With `ActivityStub`

  ```java
  private final ActivityOptions options =
      ActivityOptions.newBuilder()
          // note that either StartToCloseTimeout or ScheduleToCloseTimeout are
          // required when setting Activity options.
          .setStartToCloseTimeout(Duration.ofSeconds(5))
          .setRetryOptions(
              RetryOptions.newBuilder()
                  .setInitialInterval(Duration.ofSeconds(1))
                  .setMaximumInterval(Duration.ofSeconds(10))
                  .build())
          .build();
  ```

- With `WorkflowImplementationOptions`

  ```java
  WorkflowImplementationOptions options =
          WorkflowImplementationOptions.newBuilder()
                 .setActivityOptions(
                      ImmutableMap.of(
                          "EmailCustomerGreeting",
                          ActivityOptions.newBuilder()
                                // note that either StartToCloseTimeout or ScheduleToCloseTimeout are
                                // required when setting Activity options.
                                .setStartToCloseTimeout(Duration.ofSeconds(5))
                                .setRetryOptions(
                                      RetryOptions.newBuilder()
                                          .setDoNotRetry(NullPointerException.class.getName())
                                          .build())
                                .build()))
                .build();
  ```

### setCancellationType

- Type: `ActivityCancellationType`
- Default: `ActivityCancellationType.TRY_CANCEL`

- With `ActivityStub`

  ```java
  private final GreetingActivities activities =
    Workflow.newActivityStub(
        GreetingActivities.class,
        ActivityOptions.newBuilder()
            .setCancellationType(ActivityCancellationType.WAIT_CANCELLATION_COMPLETED)
            .build());
  ```

- With `WorkflowImplementationOptions`

  ```java
  WorkflowImplementationOptions options =
          WorkflowImplementationOptions.newBuilder()
                 .setActivityOptions(
                      ImmutableMap.of(
                          "EmailCustomerGreeting",
                          ActivityOptions.newBuilder()
                                .setCancellationType(ActivityCancellationType.WAIT_CANCELLATION_COMPLETED)
                                .build()))
                .build();
  ```

## Get the result of an Activity Execution {/* #activity-execution-result */}

The call to spawn an [Activity Execution](/activity-execution) generates the [ScheduleActivityTask](/references/commands#scheduleactivitytask) Command and provides the Workflow with an Awaitable.
Workflow Executions can either block progress until the result is available through the Awaitable or continue progressing, making use of the result when it becomes available.

To get the results of an asynchronously invoked Activity method, use the `Promise` `get` method to block until the Activity method result is available.

Sometimes an Activity Execution lifecycle goes beyond a synchronous method invocation.
For example, a request can be put in a queue and later a reply comes and is picked up by a different Worker process.
The whole request-reply interaction can be modeled as a single Activity.

To indicate that an Activity should not be completed upon its method return, call `ActivityExecutionContext.doNotCompleteOnReturn()` from the original Activity thread.

Then later, when replies come, complete the Activity using the `ActivityCompletionClient`.
To correlate Activity invocation with completion, use either a `TaskToken` or Workflow and Activity Ids.

Following is an example of using `ActivityExecutionContext.doNotCompleteOnReturn()`:

```java
public class FileProcessingActivitiesImpl implements FileProcessingActivities {

  public String download(String bucketName, String remoteName, String localName) {

    ActivityExecutionContext ctx = Activity.getExecutionContext();

    // Used to correlate reply
    byte[] taskToken = ctx.getInfo().getTaskToken();

    asyncDownloadFileFromS3(taskToken, bucketName, remoteName, localDirectory + localName);
    ctx.doNotCompleteOnReturn();

    // Return value is ignored when doNotCompleteOnReturn was called.
    return "ignored";
  }
  ...
}
```

When the download is complete, the download service potentially can complete the Activity, or fail it from a different process, for example:

```java
  public <R> void completeActivity(byte[] taskToken, R result) {
    completionClient.complete(taskToken, result);
  }

  public void failActivity(byte[] taskToken, Exception failure) {
    completionClient.completeExceptionally(taskToken, failure);
  }
```

---

## Activities - Java SDK

![Java SDK Banner](/img/assets/banner-java-temporal.png)

## Activities

- [Activity basics](/develop/java/activities/basics)
- [Activity execution](/develop/java/activities/execution)
- [Standalone Activities](/develop/java/activities/standalone-activities)
- [Timeouts](/develop/java/activities/timeouts)
- [Asynchronous Activity Completion](/develop/java/activities/asynchronous-activity)
- [Benign exceptions](/develop/java/activities/benign-exceptions)

---

## Standalone Activities - Java SDK

<ReleaseNoteHeader
  type="prerelease"
/>

[Standalone Activities](/standalone-activity) are Activities that run independently, without being orchestrated by a
Workflow. Instead of starting an Activity from within a Workflow Definition, you start a Standalone
Activity directly from a Temporal Client using `ActivityClient`.

The way you write the Activity and register it with a Worker is identical to [Workflow
Activities](/develop/java/activities/basics). The only difference is that you execute a Standalone
Activity directly from your Temporal Client.

This page covers the following:

- [Get Started with Standalone Activities](#get-started)
- [Define your Activity](#define-activity)
- [Run a Worker with the Activity registered](#run-worker)
- [Execute a Standalone Activity](#execute-activity)
- [Start a Standalone Activity without waiting for the result](#start-activity)
- [Get a handle to an existing Standalone Activity](#get-activity-handle)
- [Wait for the result of a Standalone Activity](#get-activity-result)
- [List Standalone Activities](#list-activities)
- [Count Standalone Activities](#count-activities)
- [Run Standalone Activities with Temporal Cloud](#run-standalone-activities-temporal-cloud)

:::note

This documentation uses source code from the
[standaloneactivities](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/standaloneactivities)
sample.

:::

## Get Started with Standalone Activities {/* #get-started */}

Prerequisites:

- **Java** 8+

- **Temporal Java SDK** (v1.35.0 or higher). See the [Java Quickstart](/develop/java/set-up-your-local-java) for
  install instructions.

- **Temporal CLI** v1.7.0 or higher

  Install with Homebrew:

  ```bash
  brew install temporal
  ```

  Or see the [Temporal CLI install guide](/cli/setup-cli) for other platforms.

  Verify the installation:

  ```bash
  temporal --version
  ```

Start the Temporal development server:

```
temporal server start-dev
```

This command automatically starts the Temporal development server with the Web UI, and creates the `default` Namespace.
It uses an in-memory database, so do not use it for real use cases.

:::info Temporal Cloud

All code samples on this page use
[`ClientConfigProfile.load()`](https://www.javadoc.io/doc/io.temporal/temporal-envconfig/latest/io/temporal/envconfig/ClientConfigProfile.html)
to configure the Temporal Client connection. It responds to [environment
variables](/references/client-environment-configuration) and [TOML configuration
files](/references/client-environment-configuration), so the same code works against a local dev
server and Temporal Cloud without changes. See [Run Standalone Activities with Temporal
Cloud](#run-standalone-activities-temporal-cloud) below.

:::

The Temporal Server will now be available for client connections on `localhost:7233`, and the
Temporal Web UI will now be accessible at [http://localhost:8233](http://localhost:8233). Standalone
Activities are available from the nav bar item located towards the top left of the page:

Clone the [samples-java](https://github.com/temporalio/samples-java) repository to follow along:

```bash
git clone https://github.com/temporalio/samples-java.git
cd samples-java
```

The sample consists of separate programs in the `standaloneactivities` package:

```
core/src/main/java/io/temporal/samples/standaloneactivities/
├── GreetingActivities.java       # Activity interface
├── GreetingActivitiesImpl.java   # Activity implementation
├── StandaloneActivityWorker.java # Worker that processes activity tasks
├── ExecuteActivity.java          # Starts an activity and waits for the result
├── StartActivity.java            # Starts an activity without blocking
├── ListActivities.java           # Lists activity executions
└── CountActivities.java          # Counts activity executions
```

## Define your Activity {/* #define-activity */}

An Activity in the Temporal Java SDK is an interface annotated with `@ActivityInterface`, with
methods annotated with `@ActivityMethod`. The way you define a Standalone Activity is identical to
how you define an Activity orchestrated by a Workflow. In fact, the same Activity can be executed
both as a Standalone Activity and as a Workflow Activity.

[GreetingActivities.java](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/standaloneactivities/GreetingActivities.java)

```java
@ActivityInterface
public interface GreetingActivities {

  @ActivityMethod
  String composeGreeting(String greeting, String name);
}
```

[GreetingActivitiesImpl.java](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/standaloneactivities/GreetingActivitiesImpl.java)

```java
public class GreetingActivitiesImpl implements GreetingActivities {

  private static final Logger log = LoggerFactory.getLogger(GreetingActivitiesImpl.class);

  @Override
  public String composeGreeting(String greeting, String name) {
    log.info("Composing greeting...");
    return greeting + ", " + name + "!";
  }
}
```

## Run a Worker with the Activity registered {/* #run-worker */}

Running a Worker for Standalone Activities is the same as running a Worker for Workflow Activities —
you create a `WorkerFactory`, register the Activity implementation, and call `factory.start()`. The
Worker doesn't need to know whether the Activity will be invoked from a Workflow or as a Standalone
Activity. See [How to run a Worker](/develop/java/workers/run-worker-process) for more details on
Worker setup and configuration options.

[StandaloneActivityWorker.java](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/standaloneactivities/StandaloneActivityWorker.java)

```java
ClientConfigProfile profile = ClientConfigProfile.load();
WorkflowServiceStubs service =
    WorkflowServiceStubs.newServiceStubs(profile.toWorkflowServiceStubsOptions());

WorkflowClient client = WorkflowClient.newInstance(service, profile.toWorkflowClientOptions());
WorkerFactory factory = WorkerFactory.newInstance(client);
Worker worker = factory.newWorker(TASK_QUEUE);
worker.registerActivitiesImplementations(new GreetingActivitiesImpl());
factory.start();
System.out.println("Worker running on task queue: " + TASK_QUEUE);
```

Open a new terminal, navigate to the `samples-java` directory, and run the Worker:

```bash
./gradlew -q execute -PmainClass=io.temporal.samples.standaloneactivities.StandaloneActivityWorker
```

Leave this terminal running — the Worker needs to stay up to process activities.

## Execute a Standalone Activity {/* #execute-activity */}

Use
[`ActivityClient.execute()`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/ActivityClient.html)
to execute a Standalone Activity and block until it completes. Call this from your application code,
not from inside a Workflow Definition. This durably enqueues your Standalone Activity in the Temporal
Server, waits for it to be executed on your Worker, and then returns the typed result.

[ExecuteActivity.java](https://github.com/temporalio/samples-java/blob/main/core/src/main/java/io/temporal/samples/standaloneactivities/ExecuteActivity.java)

```java
ActivityClient client =
    ActivityClient.newInstance(
        service,
        ActivityClientOptions.newBuilder().setNamespace(profile.getNamespace()).build());

StartActivityOptions options =
    StartActivityOptions.newBuilder()
        .setId(ACTIVITY_ID)
        .setTaskQueue(TASK_QUEUE)
        .setStartToCloseTimeout(Duration.ofSeconds(10))
        .build();

String result =
    client.execute(
        GreetingActivities.class,
        GreetingActivities::composeGreeting,
        options,
        "Hello",
        "World");
System.out.println("Activity result: " + result);
```

The typed `execute()` API takes the Activity interface class and an unbound method reference. The SDK
uses the method reference to infer the Activity type name and result type at runtime. You can also
call Activities by string type name:

```java
// Using a string type name
String result = client.execute("ComposeGreeting", String.class, options, "Hello", "World");
```

`StartActivityOptions` requires `id`, `taskQueue`, and at least one of `startToCloseTimeout` or
`scheduleToCloseTimeout`.

To run it:

1. Make sure the Temporal Server is running (from the [Get Started](#get-started) step above).
