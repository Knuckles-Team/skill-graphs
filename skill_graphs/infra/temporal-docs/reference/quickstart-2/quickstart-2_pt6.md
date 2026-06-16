
<SdkLogos />

- Go SDK [developer guide](/develop/go) and [API reference](http://t.mp/go-api)
- Java SDK [developer guide](/develop/java) and [API reference](http://t.mp/java-api)
- PHP SDK [developer guide](/develop/php) and [API reference](https://php.temporal.io/namespaces/temporal.html)
- Python SDK [developer guide](/develop/python) and [API reference](https://python.temporal.io)
- TypeScript SDK [developer guide](/develop/typescript) and [API reference](https://typescript.temporal.io)
- .NET SDK [developer guide](/develop/dotnet) and [API reference](https://dotnet.temporal.io/)
- Ruby SDK [developer guide](/develop/ruby) and [API reference](https://ruby.temporal.io/)
- Rust SDK [developer guide](/develop/rust) and [API reference](https://docs.rs/temporalio-sdk/latest/temporalio_sdk/)

---

## Asynchronous Activity completion - Java SDK

This page shows how to asynchronously complete an Activity

[Asynchronous Activity Completion](/activity-execution#asynchronous-activity-completion) enables the Activity Function to return without the Activity Execution completing.

There are three steps to follow:

1. The Activity provides the external system with identifying information needed to complete the Activity Execution.
   Identifying information can be a [Task Token](/activity-execution#task-token), or a combination of Namespace, Workflow Id, and Activity Id.
2. The Activity Function completes in a way that identifies it as waiting to be completed by an external system.
3. The Temporal Client is used to Heartbeat and complete the Activity.

To complete an Activity asynchronously, set the [`ActivityCompletionClient`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/ActivityCompletionClient.html) interface to the `complete()` method.

```java
    @Override
    public String composeGreeting(String greeting, String name) {

      // Get the activity execution context
      ActivityExecutionContext context = Activity.getExecutionContext();

      // Set a correlation token that can be used to complete the activity asynchronously
      byte[] taskToken = context.getTaskToken();

      /**
       * For the example we will use a {@link java.util.concurrent.ForkJoinPool} to execute our
       * activity. In real-life applications this could be any service. The composeGreetingAsync
       * method is the one that will actually complete workflow action execution.
       */
      ForkJoinPool.commonPool().execute(() -> composeGreetingAsync(taskToken, greeting, name));
      context.doNotCompleteOnReturn();

      // Since we have set doNotCompleteOnReturn(), the workflow action method return value is
      // ignored.
      return "ignored";
    }

    // Method that will complete action execution using the defined ActivityCompletionClient
    private void composeGreetingAsync(byte[] taskToken, String greeting, String name) {
      String result = greeting + " " + name + "!";

      // Complete our workflow activity using ActivityCompletionClient
      completionClient.complete(taskToken, result);
    }
  }
```

Alternatively, set the [`doNotCompleteOnReturn()`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityExecutionContext.html#doNotCompleteOnReturn()) method during an Activity Execution.

```java
    @Override
    public String composeGreeting(String greeting, String name) {

      // Get the activity execution context
      ActivityExecutionContext context = Activity.getExecutionContext();

      // Set a correlation token that can be used to complete the activity asynchronously
      byte[] taskToken = context.getTaskToken();

      /**
       * For the example we will use a {@link java.util.concurrent.ForkJoinPool} to execute our
       * activity. In real-life applications this could be any service. The composeGreetingAsync
       * method is the one that will actually complete workflow action execution.
       */
      ForkJoinPool.commonPool().execute(() -> composeGreetingAsync(taskToken, greeting, name));
      context.doNotCompleteOnReturn();

      // Since we have set doNotCompleteOnReturn(), the workflow action method return value is
      // ignored.
      return "ignored";
    }
```

When this method is called during an Activity Execution, the Activity Execution does not complete when its method returns.

---

## Activity basics - Java SDK

## Develop an Activity

One of the primary things that Workflows do is orchestrate the execution of Activities.
An Activity is a normal function or method execution that's intended to execute a single, well-defined action (either short or long-running), such as querying a database, calling a third-party API, or transcoding a media file.
An Activity can interact with world outside the Temporal Platform or use a Temporal Client to interact with a Temporal Service.
For the Workflow to be able to execute the Activity, we must define the [Activity Definition](/activity-definition).

An [Activity Definition](/activities) is a combination of the Temporal Java SDK [Activity](https://www.javadoc.io/static/io.temporal/temporal-sdk/0.19.0/io/temporal/activity/Activity.html) Class implementing a specially annotated interface.

An Activity interface is annotated with `@ActivityInterface` and an Activity implementation implements this Activity interface.
To handle Activity types that do not have an explicitly registered handler, you can directly implement a dynamic Activity.

```java
@ActivityInterface
public interface GreetingActivities {
    String composeGreeting(String greeting, String language);
}
```

Each method defined in the Activity interface defines a separate Activity method.
You can annotate each method in the Activity interface with the `@ActivityMethod` annotation, but this is completely optional.
The following example uses the `@ActivityMethod` annotation for the method defined in the previous example.

```java
@ActivityInterface
public interface GreetingActivities {
    @ActivityMethod
    String composeGreeting(String greeting, String language);
}
```

An Activity implementation is a Java class that implements an Activity annotated interface.

```java
// Implementation for the GreetingActivities interface example from in the previous section
 static class GreetingActivitiesImpl implements GreetingActivities {
    @Override
    public String composeGreeting(String greeting, String name) {
      return greeting + " " + name + "!";
    }
  }
```

## Define Activity parameters {/* #activity-parameters */}

There is no explicit limit to the total number of parameters that an [Activity Definition](/activity-definition) may support.
However, there is a limit to the total size of the data that ends up encoded into a gRPC message Payload.

A single argument is limited to a maximum size of 2 MB.
And the total size of a gRPC message, which includes all the arguments, is limited to a maximum of 4 MB.

Also, keep in mind that all Payload data is recorded in the [Workflow Execution Event History](/workflow-execution/event#event-history) and large Event Histories can affect Worker performance.
This is because the entire Event History could be transferred to a Worker Process with a [Workflow Task](/tasks#workflow-task).

{/* TODO link to gRPC limit section when available */}

Some SDKs require that you pass context objects, others do not.
When it comes to your application data—that is, data that is serialized and encoded into a Payload—we recommend that you use a single object as an argument that wraps the application data passed to Activities.
This is so that you can change what data is passed to the Activity without breaking a function or method signature.

An Activity interface can have any number of parameters.
All inputs should be serializable by the default Jackson JSON Payload Converter.

When implementing Activities, be mindful of the amount of data that you transfer using the Activity invocation parameters or return values as these are recorded in the Workflow Execution Events History.
Large Event Histories can adversely impact performance.

You can create a custom object, and pass it to the Activity interface, as shown in the following example.

```java
@ActivityInterface
public interface YourActivities {
    String getCustomObject(CustomObj customobj);
    void sendCustomObject(CustomObj customobj, String abc);
}
```

The `execute` method in the dynamic Activity interface implementation takes in `EncodedValues` that are inputs to the Activity Execution, as shown in the following example.

```java
// Dynamic Activity implementation
 public static class DynamicActivityImpl implements DynamicActivity {
   @Override
   public Object execute(EncodedValues args) {
     String activityType = Activity.getExecutionContext().getInfo().getActivityType();
     return activityType
         + ": "
         + args.get(0, String.class)
         + " "
         + args.get(1, String.class)
         + " from: "
         + args.get(2, String.class);
   }
 }
```

For more details, see [Dynamic Activity Reference](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/DynamicActivity.html).

## Define Activity return values {/* #activity-return-values */}

All data returned from an Activity must be serializable.

Activity return values are subject to payload size limits in Temporal. The default payload size limit is 2MB, and there is a hard limit of 4MB for any gRPC message size in the Event History transaction ([see Cloud limits here](https://docs.temporal.io/cloud/limits#per-message-grpc-limit)). Keep in mind that all return values are recorded in a [Workflow Execution Event History](/workflow-execution/event#event-history).

Activity return values must be serializable and deserializable by the provided [`DataConverter`](https://www.javadoc.io/static/io.temporal/temporal-sdk/1.17.0/io/temporal/common/converter/DataConverter.html).

The `execute` method for `DynamicActivity` can return type Object.
Ensure that your Workflow or Client can handle an Object type return or is able to convert the Object type response.

- [Data Converter](/dataconversion)
- Java DataConverter reference: [https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/common/converter/DataConverter.html](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/common/converter/DataConverter.html)

## Customize your Activity Type {/* #activity-type */}

Each Activity has a Type, which may also be referred to as the Activity 'name'.
This name appears in the Workflow Execution Event History in the Summary tab for each Activity Task.
The name lets you identify Activity Types called during the Execution.

Custom Activity Type names prevent name collisions across interfaces and Workflows.
They offer descriptive Activity method names without concerns about re-using those names elsewhere in your project.
They also support code management, especially in larger projects with many Activities.
For example, you might use a prefix to group related activities together.
Custom names also distinguish keys for gathering metrics without name conflicts.

The following examples show how to set custom names for your Activity Type.

### Default behavior

By default, an Activity Type is the method name with the first letter capitalized:

```java
@ActivityInterface
public interface GreetingActivities {
    String sendMessage(String input);

    @ActivityMethod
    String composeGreeting(String greeting, String language);
}
```

- Method Name: `sendMessage`
- Activity Type: `SendMessage`
- Method Name: `composeGreeting`
- Activity Type: `ComposeGreeting`

### Custom Prefix

Using the `namePrefix` parameter in the `@ActivityInterface` annotation adds a prefix to each Activity Type name mentioned in the interface, unless the prefix is specifically overridden:

```java
@ActivityInterface(namePrefix = "Messaging_")
public interface GreetingActivities {
    String sendMessage(String input);

    @ActivityMethod
    String composeGreeting(String greeting, String language);
}
```

- Method Name: `sendMessage`
- Activity Type: `Messaging_SendMessage`
- Method Name: `composeGreeting`
- Activity Type: `Messaging_ComposeGreeting`

The Activity Type is capitalized, even when using a prefix.

### Custom Name

To override the default name and any inherited prefixes, use the `name` parameter in the `@ActivityMethod` annotation:

```java
@ActivityInterface(namePrefix = "Messaging_")
public interface GreetingActivities {
    String sendMessage(String input);

    @ActivityMethod
    String composeGreeting(String greeting, String language);
    @ActivityMethod(name = "farewell")
    String composeFarewell(String farewell, String language);
}
```

Using the `name` parameter won't automatically capitalize the result:

- Method Name: `sendMessage`
- Activity Type: `Messaging_SendMessage`
- Method Name: `composeGreeting`
- Activity Type: `Messaging_ComposeGreeting`
- Method Name: `composeFarewell`
- Activity Type: `farewell`

Be cautious with names that contain special characters, as these can be used as metric tags.
Systems such as Prometheus may ignore metrics with tags using unsupported characters.

---

## Benign exceptions - Java SDK

When Activities throw errors that are expected or not severe, they can create noise in your logs, metrics, and OpenTelemetry traces, making it harder to identify real issues.
By marking these errors as benign, you can exclude them from your observability data while still handling them in your Workflow logic.

To mark an error as benign, set the category to `ApplicationErrorCategory.BENIGN` using the [`ApplicationFailure`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/failure/ApplicationFailure.html) builder.

Benign errors:
- Have Activity failure logs downgraded to DEBUG level
- Do not emit Activity failure metrics
- Do not set the OpenTelemetry failure status to ERROR

```java

@ActivityInterface
public interface MyActivities {
  @ActivityMethod
  String myActivity();
}

public class MyActivitiesImpl implements MyActivities {
  @Override
  public String myActivity() {
    try {
      return callExternalService();
    } catch (Exception e) {
      // Mark this error as benign since it's expected
      throw ApplicationFailure.newBuilder()
          .setMessage(e.getMessage())
          .setType(e.getClass().getName())
          .setCause(e)
          .setCategory(ApplicationErrorCategory.BENIGN)
          .build();
    }
  }
}
```

Use benign exceptions for Activity errors that occur regularly as part of normal operations, such as polling an external service that isn't ready yet, or handling expected transient failures that will be retried.

---

## Activity execution - Java SDK

## Start an Activity Execution {/* #activity-execution */}

Calls to spawn [Activity Executions](/activity-execution) are written within a [Workflow Definition](/workflow-definition).
The call to spawn an Activity Execution generates the [ScheduleActivityTask](/references/commands#scheduleactivitytask) Command.
This results in the set of three [Activity Task](/tasks#activity-task) related Events ([ActivityTaskScheduled](/references/events#activitytaskscheduled), [ActivityTaskStarted](/references/events#activitytaskstarted), and ActivityTask[Closed]) in your Workflow Execution Event History.

A single instance of the Activities implementation is shared across multiple simultaneous Activity invocations.
Activity implementation code should be _idempotent_.

The values passed to Activities through invocation parameters or returned through a result value are recorded in the Execution history.
The entire Execution history is transferred from the Temporal service to Workflow Workers when a Workflow state needs to recover.
A large Execution history can thus adversely impact the performance of your Workflow.

Therefore, be mindful of the amount of data you transfer through Activity invocation parameters or Return Values.
Otherwise, no additional limitations exist on Activity implementations.

Activities are remote procedure calls that must be invoked from within a Workflow using `ActivityStub`.
Activities are not executable on their own. You cannot start an Activity Execution by itself.

Note that before an Activity Execution is invoked:

- Activity options (either [`setStartToCloseTimeout`](/encyclopedia/detecting-activity-failures#start-to-close-timeout) or [`ScheduleToCloseTimeout`](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout) are required) must be set for the Activity.
  For details, see [How to set Activity timeouts](/develop/java/activities/timeouts).
- The Activity must be registered with a Worker.
  See [Worker Program](/develop/java/workers/run-worker-process#run-a-dev-worker)
- Activity code must be thread-safe.

Activities should only be instantiated using stubs from within a Workflow.
An `ActivityStub` returns a client-side stub that implements an Activity interface.
You can invoke Activities using `Workflow.newActivityStub`(type-safe) or `Workflow.newUntypedActivityStub` (untyped).

Calling a method on the Activity interface schedules the Activity invocation with the Temporal service, and generates an [`ActivityTaskScheduled` Event](/references/events#activitytaskscheduled).

Activities can be invoked synchronously or asynchronously.

### Invoking Activities Synchronously

In the following example, we use the type-safe `Workflow.newActivityStub` within the "FileProcessingWorkflow" Workflow implementation to create a client-side stub of the `FileProcessingActivities` class. We also define `ActivityOptions` and set `setStartToCloseTimeout` option to one hour.

```java
public class FileProcessingWorkflowImpl implements FileProcessingWorkflow {

    private final FileProcessingActivities activities;

    public FileProcessingWorkflowImpl() {
        this.activities = Workflow.newActivityStub(
                FileProcessingActivities.class,
                ActivityOptions.newBuilder()
                        .setStartToCloseTimeout(Duration.ofHours(1))
                        .build());
    }

    @Override
    public void processFile(Arguments args) {
        String localName = null;
        String processedName = null;
        try {
            localName = activities.download(args.getSourceBucketName(), args.getSourceFilename());
            processedName = activities.processFile(localName);
            activities.upload(args.getTargetBucketName(), args.getTargetFilename(), processedName);
        } finally {
            if (localName != null) {
                activities.deleteLocalFile(localName);
            }
            if (processedName != null) {
                activities.deleteLocalFile(processedName);
            }
        }
    }
    // ...
}
```

A Workflow can have multiple Activity stubs. Each Activity stub can have its own `ActivityOptions` defined.
The following example shows a Workflow implementation with two typed Activity stubs.

```java
public FileProcessingWorkflowImpl() {
    ActivityOptions options1 = ActivityOptions.newBuilder()
             .setTaskQueue("taskQueue1")
             .setStartToCloseTimeout(Duration.ofMinutes(10))
             .build();
    this.store1 = Workflow.newActivityStub(FileProcessingActivities.class, options1);

    ActivityOptions options2 = ActivityOptions.newBuilder()
             .setTaskQueue("taskQueue2")
             .setStartToCloseTimeout(Duration.ofMinutes(5))
             .build();
    this.store2 = Workflow.newActivityStub(FileProcessingActivities.class, options2);
}
```

To invoke Activities inside Workflows without referencing the interface it implements, use an untyped Activity stub `Workflow.newUntypedActivityStub`.
This is useful when the Activity type is not known at compile time, or to invoke Activities implemented in different programming languages.

```java
   // Workflow code
    ActivityOptions activityOptions =
        ActivityOptions.newBuilder()
        .setStartToCloseTimeout(Duration.ofSeconds(3))
        .setTaskQueue("simple-queue-node")
        .build();

    ActivityStub activity = Workflow.newUntypedActivityStub(activityOptions);
    activity.execute("ComposeGreeting", String.class, "Hello World", "Spanish");
```

### Invoking Activities Asynchronously

Sometimes Workflows need to perform certain operations in parallel.
The Temporal Java SDK provides the `Async` class which includes static methods used to invoke any Activity asynchronously.
The calls return a result of type `Promise` which is similar to the Java `Future` and `CompletionStage`.
When invoking Activities, use `Async.function` for Activities that return a result, and `Async.procedure` for Activities that return void.

In the following asynchronous Activity invocation, the method reference is passed to `Async.function` followed by Activity arguments.

```java
Promise<String> localNamePromise = Async.function(activities::download, sourceBucket, sourceFile);
```

The following example shows how to call two Activity methods, "download" and "upload", in parallel on multiple files.

```java
  public void processFile(Arguments args) {
    List<Promise<String>> localNamePromises = new ArrayList<>();
    List<String> processedNames = null;
    try {
      // Download all files in parallel.
      for (String sourceFilename : args.getSourceFilenames()) {
        Promise<String> localName =
            Async.function(activities::download, args.getSourceBucketName(), sourceFilename);
        localNamePromises.add(localName);
      }
      List<String> localNames = new ArrayList<>();
      for (Promise<String> localName : localNamePromises) {
        localNames.add(localName.get());
      }
      processedNames = activities.processFiles(localNames);

      // Upload all results in parallel.
      List<Promise<Void>> uploadedList = new ArrayList<>();
      for (String processedName : processedNames) {
        Promise<Void> uploaded =
            Async.procedure(
                activities::upload,
                args.getTargetBucketName(),
                args.getTargetFilename(),
                processedName);
        uploadedList.add(uploaded);
      }
      // Wait for all uploads to complete.
      Promise.allOf(uploadedList).get();
    } finally {
      for (Promise<String> localNamePromise : localNamePromises) {
        // Skip files that haven't completed downloading.
        if (localNamePromise.isCompleted()) {
          activities.deleteLocalFile(localNamePromise.get());
        }
      }
      if (processedNames != null) {
        for (String processedName : processedNames) {
          activities.deleteLocalFile(processedName);
        }
      }
    }
  }
```

### Activity Execution Context

`ActivityExecutionContext` is a context object passed to each Activity implementation by default.
You can access it in your Activity implementations via `Activity.getExecutionContext()`.

It provides getters to access information about the Workflow that invoked the Activity.
Note that the Activity context information is stored in a thread-local variable.
Therefore, calls to `getExecutionContext()` succeed only within the thread that invoked the Activity function.

Following is an example of using the `ActivityExecutionContext`:

```java
public class FileProcessingActivitiesImpl implements FileProcessingActivities {

  @Override
  public String download(String bucketName, String remoteName, String localName) {

    ActivityExecutionContext ctx = Activity.getExecutionContext();
    ActivityInfo info = ctx.getInfo();

    log.info("namespace=" +  info.getActivityNamespace());
    log.info("workflowId=" + info.getWorkflowId());
    log.info("runId=" + info.getRunId());
    log.info("activityId=" + info.getActivityId());
    log.info("activityTimeout=" + info.getStartToCloseTimeout();

    return downloadFileFromS3(bucketName, remoteName, localDirectory + localName);
  }
    ...
}
```

For details on getting the results of an Activity Execution, see [Activity Execution Result](#activity-execution-result).

## Set required Activity Timeouts {/* #required-timeout */}

Activity Execution semantics rely on several parameters.
The only required value that needs to be set is either a [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout) or a [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout).
These values are set in the Activity Options.

Set your Activity Timeout from the [`ActivityOptions.Builder`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/activity/ActivityOptions.Builder.html) class.

Available timeouts are:

- ScheduleToCloseTimeout()
- ScheduleToStartTimeout()
- StartToCloseTimeout()

You can set Activity Options using an `ActivityStub` within a Workflow implementation, or per-Activity using `WorkflowImplementationOptions` within a Worker.

The following uses `ActivityStub`.

```java
GreetingActivities activities = Workflow.newActivityStub(GreetingActivities.class,
                ActivityOptions.newBuilder()
                        .setScheduleToCloseTimeout(Duration.ofSeconds(5))
                        // .setStartToCloseTimeout(Duration.ofSeconds(2)
                        // .setScheduletoCloseTimeout(Duration.ofSeconds(20))
                        .build());
```

The following uses `WorkflowImplementationOptions`.

```java
WorkflowImplementationOptions options =
            WorkflowImplementationOptions.newBuilder()
                    .setActivityOptions(
