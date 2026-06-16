
:::

### Do blocking operations in handlers {/* #blocking-handlers */}

Signal and Update handlers can block.
This allows you to use [`Workflow.await`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#await(java.time.Duration,java.util.function.Supplier)), Activities, Child Workflows, [`Workflow.sleep`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#sleep(java.time.Duration)) Timers, etc.
This expands the possibilities for what can be done by a handler but it also means that handler executions and your main Workflow method are all running concurrently, with switching occurring between them at await calls.

It's essential to understand the things that could go wrong in order to use blocking handlers safely.
See [Workflow message passing](/encyclopedia/workflow-message-passing) for guidance on safe usage of blocking Signal and Update handlers, and the [Controlling handler concurrency](#control-handler-concurrency) and [Waiting for message handlers to finish](#wait-for-message-handlers) sections below.

The following code modifies the Update handler from earlier on in this page.
The Update handler now makes a blocking call to execute an Activity:

```java
public static class GreetingWorkflowImpl implements GreetingWorkflow {
    ...
    @Override
    public Language setLanguage(Language language) {
        if (!greetings.containsKey(language)) {
            String greeting = activity.greetingService(language);
            if (greeting == null) {
                // 👉 An update validator cannot be blocking, so cannot be used to check that the remote
                // greetingService supports the requested language. Throwing an ApplicationFailure
                // will fail the Update, but the WorkflowExecutionUpdateAccepted event will still be
                // added to history.
                throw ApplicationFailure.newFailure("Greeting service does not support: " + language, "GreetingFailure")
            }
            greetings.put(language, greeting);
        }
        Language previousLanguage = this.language;
        this.language = language;
        return previousLanguage;
    }
}
```

Although a Signal handler can also make blocking calls like this, using an Update handler allows the Client to receive a result or error once the Activity completes.
This lets your Client track the progress of asynchronous work performed by the Update's Activities, Child Workflows, etc.

### Add blocking wait conditions {/* #block-with-wait */}

Sometimes, blocking Signal or Update handlers need to meet certain conditions before they should continue.
You can use [`Workflow.await`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#await(java.time.Duration,java.util.function.Supplier)) to prevent the code from proceeding until a condition is true.
You specify the condition by passing a function that returns `true` or `false`.
This is an important feature that helps you control your handler logic.

Here are two important use cases for `Workflow.await`:

- Waiting in a handler until it is appropriate to continue.
- Waiting in the main Workflow until all active handlers have finished.

#### Wait for conditions in handlers {/* #wait-in-handlers */}

It's common to use `Workflow.await` in a handler.
For example, suppose your Workflow class has a `updateReadyToExecute` method that indicates whether your Update handler should be allowed to start executing.
You can use `workflow.wait_condition` in the handler to make the handler pause until the condition is met:

```java
@Override
public String setLanguage(UpdateInput input) {
    Workflow.await(() -> this.updateReadyToExecute(input));
    ...
}
```

Remember: handlers can execute before the main Workflow method starts.

You can also use `Workflow.await` anywhere else in the handler to wait for a specific condition to become true.
This allows you to write handlers that pause at multiple points, each time waiting for a required condition to become true.

#### Ensure your handlers finish before the Workflow completes {/* #wait-for-message-handlers */}

`Workflow.await` can ensure your handler completes before a Workflow finishes.
When your Workflow uses blocking Signal or Update handlers, your main Workflow method can return or Continue-as-New while a handler is still waiting on an async task, such as an Activity.
The Workflow completing may interrupt the handler before it finishes crucial work and cause Client errors when trying to retrieve Update results.
Use `Workflow.await` to wait for [`Workflow.isEveryHandlerFinished`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#isEveryHandlerFinished()) to return `true` to address this problem and allow your Workflow to end smoothly:

```java
public class MyWorkflowImpl implements MyWorkflow {
    ...
    @Override
    public String run() {
        ...
        Workflow.await(() -> Workflow.isEveryHandlerFinished());
        return "workflow-result";
    }
}
```

By default, your Worker will log a warning when you allow a Workflow Execution to finish with unfinished handler executions.
You can silence these warnings on a per-handler basis by passing the `unfinishedPolicy` argument to the [`@SignalMethod`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/SignalMethod.html) / [`@UpdateMethod`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/UpdateMethod.html) annotation:

```java
@WorkflowInterface
public interface MyWorkflow {
    ...
    @UpdateMethod(unfinishedPolicy = HandlerUnfinishedPolicy.ABANDON)
    void myUpdate();
}
```

See [Finishing handlers before the Workflow completes](/handling-messages#finishing-message-handlers) for more information.

### Use `@WorkflowInit` to operate on Workflow input before any handler executes

Normally, your Workflows constructor won't have any parameters.
However, if you use the `@WorkflowInit` annotation on your constructor, you can give it the same [Workflow parameters](/develop/java/workflows/basics#workflow-parameters) as your `@WorkflowMethod`.
The SDK will then ensure that your constructor receives the Workflow input arguments that the [Client sent](/develop/java/client/temporal-client#start-workflow-execution).
The Workflow input arguments are also passed to your `@WorkflowMethod` method -- that always happens, whether or not you use the `@WorkflowInit` annotation.
This is useful if you have message handlers that need access to Workflow input: see [Initializing the Workflow first](/handling-messages#workflow-initializers).

:::caution

Do not make blocking calls from within your `@WorkflowInit` method. This could result in your Workflow being incompletely initialized at the start, meaning, for example, that Signal, Query, and Update handler registration would be delayed.

:::

Here's an example.
Notice that the constructor and `getGreeting` must have the same parameters:

```java
public class GreetingExample {
    @WorkflowInterface
    public interface GreetingWorkflow {
        @WorkflowMethod
        String getGreeting(String input);

        @UpdateMethod
        boolean checkTitleValidity();
    }

    public static class GreetingWorkflowImpl implements GreetingWorkflow {
        private final String nameWithTitle;
        private boolean titleHasBeenChecked;
        ...
        // Note the annotation is on a public constructor
        @WorkflowInit
        public GreetingWorkflowImpl(String input) {
          this.nameWithTitle = "Sir " + input;
          this.titleHasBeenChecked = false;
        }

        @Override
        public String getGreeting(String input) {
          Workflow.await(() -> titleHasBeenChecked)
          return "Hello " + nameWithTitle;
        }

        @Override
        public boolean checkTitleValidity() {
          // 👉 The handler is now guaranteed to see the workflow input
          // after it has been processed by the constructor.
          boolean isValid = activity.checkTitleValidity(nameWithTitle);
          titleHasBeenChecked = true;
          return isValid;
        }
    }
}
```

### Use locks to prevent concurrent handler execution {/* #control-handler-concurrency */}

Concurrent processes can interact in unpredictable ways.
Incorrectly written [concurrent message-passing](/handling-messages#message-handler-concurrency) code may not work correctly when multiple handler instances run simultaneously.
Here's an example of a pathological case:

```java
public class DataWorkflowImpl implements DataWorkflow {
    ...
    @Override
    public void badSignalHandler() {
        Data data = activity.fetchData();
        this.x = data.x;
        // 🐛🐛 Bug!! If multiple instances of this method are executing concurrently, then
        // there may be times when the Workflow has self.x from one Activity execution and self.y from another.
        Workflow.sleep(Duration.ofSeconds(1));
        this.y = data.y;
    }
}
```

Coordinating access with `WorkflowLock` corrects this code.
Locking makes sure that only one handler instance can execute a specific section of code at any given time:

```java
public class DataWorkflowImpl implements DataWorkflow {
    WorkflowLock lock = Workflow.newWorkflowLock();
    ...
    @Override
    public void safeSignalHandler() {
        try {
            lock.lock();
            Data data = activity.fetchData();
            this.x = data.x;
            // ✅ OK: the scheduler may switch now to a different handler execution,
            // or to the main workflow method, but no other execution of this handler
            // can run until this execution finishes.
            Workflow.sleep(Duration.ofSeconds(1));
            this.y = data.y;
        } finally {
            lock.unlock()
        }
    }
}
```

## Message handler troubleshooting {/* #message-handler-troubleshooting */}

When sending a Signal, Update, or Query to a Workflow, your Client might encounter the following errors:

- **The Client can't contact the server**:
  You'll receive a [`WorkflowServiceException`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowServiceException.html) on which the `cause` is a [`StatusRuntimeException`](https://grpc.github.io/grpc-java/javadoc/io/grpc/StatusRuntimeException.html) and `status` of `UNAVAILABLE` (after some retries).

- **The Workflow does not exist**:
  You'll receive a [`WorkflowNotFoundException`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowNotFoundException.html).

See [Exceptions in message handlers](/handling-messages#exceptions) for a non–Java-specific discussion of this topic.

### Problems when sending a Signal {/* #signal-problems */}

When using Signal, the above `WorkflowException`s are the only types of exception that will result from the request.

In contrast, for Queries and Updates, the client waits for a response from the Worker.
If an issue occurs during the handler execution by the Worker, the Client may receive an exception.

### Problems when sending an Update {/* #update-problems */}

When working with Updates, you may encounter these errors:

- **No Workflow Workers are polling the Task Queue**:
  Your request will be retried by the SDK Client indefinitely.
  You can impose a timeout with `CompletableFuture.get()` method with a timeout parameter.
  This throws a `java.util.concurrent.TimeoutException` exception when it expires.

- **Update failed**: You'll receive a `WorkflowUpdateException` exception.
  There are two ways this can happen:

  - The Update was rejected by an Update validator defined in the Workflow alongside the Update handler.

  - The Update failed after having been accepted.

  Update failures are like [Workflow failures](/references/failures).
  Issues that cause a Workflow failure in the main method also cause Update failures in the Update handler.
  These might include:

      - A failed Child Workflow
      - A failed Activity (if the Activity retries have been set to a finite number)
      - The Workflow author throwing `ApplicationFailure`
      - Any error listed in [getFailWorkflowExceptionTypes](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/worker/WorkflowImplementationOptions.html#getFailWorkflowExceptionTypes()) (empty by default)

- **The handler caused the Workflow Task to fail**:
  A [Workflow Task Failure](/references/failures) causes the server to retry Workflow Tasks indefinitely. What happens to your Update request depends on its stage:
  - If the request hasn't been accepted by the server, you receive a `FAILED_PRECONDITION` [`WorkflowServiceException`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowServiceException.html) exception.
  - If the request has been accepted, it is durable.
    Once the Workflow is healthy again after a code deploy, use a [`WorkflowUpdateHandle`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowUpdateHandle.html) to fetch the Update result.

- **The Workflow finished while the Update handler execution was in progress**:
  You'll receive a [`WorkflowServiceException`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowServiceException.html) "workflow execution already completed"`.

  This will happen if the Workflow finished while the Update handler execution was in progress, for example because

  - The Workflow was canceled or failed.

  - The Workflow completed normally or continued-as-new and the Workflow author did not [wait for handlers to be finished](/handling-messages#finishing-message-handlers).

### Problems when sending a Query {/* #query-problems */}

When working with Queries, you may encounter these errors:

- **There is no Workflow Worker polling the Task Queue**:
  You'll receive a [`WorkflowServiceException`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowServiceException.html) on which the `cause` is a [`StatusRuntimeException`](https://grpc.github.io/grpc-java/javadoc/io/grpc/StatusRuntimeException.html) with a `status` of `FAILED_PRECONDITION`.

- **Query failed**:
  You'll receive a [`WorkflowQueryException`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowQueryException.html) exception if something goes wrong during a Query.
  Any exception in a Query handler will trigger this error.
  This differs from Signal and Update requests, where exceptions can lead to Workflow Task Failure instead.

- **The handler caused the Workflow Task to fail.**
  This would happen, for example, if the Query handler blocks the thread for too long without yielding.

## Dynamic components {/* #dynamic-handler */}

A dynamic Workflow, Activity, Signal, Update, or Query is a kind of unnamed item.
Normally, these items are registered by name with the Worker and invoked at runtime.
When an unregistered or unrecognized Workflow, Activity, or message request arrives with a recognized method signature, the Worker can use a pre-registered dynamic stand-in.

For example, you might send a request to start a Workflow named "MyUnknownWorkflow".
After receiving a Workflow Task, the Worker may find that there's no registered Workflow Definitions of that type.
It then checks to see if there's a registered dynamic Workflow.
If the dynamic Workflow signature matches the incoming Workflow signature, the Worker invokes that just as it would invoke a non-dynamic statically named version.

By registering dynamic versions of your Temporal components, the Worker can fall back to these alternate implementations for name mismatches.

:::caution

Use dynamic elements judiciously and as a fallback mechanism, not a primary design.
They can introduce long-term maintainability and debugging issues.
Reserve dynamic invocation use for cases where a name is not or can't be known at compile time.

:::

### Set a Dynamic Workflow {/* #set-a-dynamic-workflow */}

Use [`DynamicWorkflow`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/DynamicWorkflow.html) to implement Workflow Types dynamically.
Register a Workflow implementation type that extends `DynamicWorkflow` to implement any Workflow Type that is not explicitly registered with the Worker.

The dynamic Workflow interface is implemented with the `execute` method. This method takes in `EncodedValues` that are inputs to the Workflow Execution.
These inputs can be specified by the Client when invoking the Workflow Execution.

```java
public class MyDynamicWorkflow implements DynamicWorkflow {
   @Override
    public Object execute(EncodedValues args) {
    }
}
```

### How to set a Dynamic Activity {/* #set-a-dynamic-activity */}

To handle Activity types that do not have an explicitly registered handler, you can directly implement a dynamic Activity.

Use `DynamicActivity` to implement any number of Activity types dynamically.
When an Activity implementation that extends `DynamicActivity` is registered, it is called for any Activity type invocation that doesn't have an explicitly registered handler.

The dynamic Activity interface is implemented with the `execute` method, as shown in the following example.

```java
// Dynamic Activity implementation
 public static class DynamicGreetingActivityImpl implements DynamicActivity {
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

Use `Activity.getExecutionContext()` to get information about the Activity type that should be implemented dynamically.

### How to set a Dynamic Signal {/* #set-a-dynamic-signal */}

You can also implement Signal handlers dynamically. This is useful for library-level code and implementation of DSLs.

Use `Workflow.registerListener(Object)` to register an implementation of the `DynamicSignalListener` in the Workflow implementation code.

```java
Workflow.registerListener(
  (DynamicSignalHandler)
      (signalName, encodedArgs) -> name = encodedArgs.get(0, String.class));
```

When registered, any Signals sent to the Workflow without a defined handler will be delivered to the `DynamicSignalHandler`.
Note that you can only register one `Workflow.registerListener(Object)` per Workflow Execution.
`DynamicSignalHandler` can be implemented in both regular and dynamic Workflow implementations.

### How to set a Dynamic Query {/* #set-a-dynamic-query */}

You can also implement Query handlers dynamically. This is useful for library-level code and implementation of DSLs.

Use `Workflow.registerListener(Object)` to register an implementation of the `DynamicQueryListener` in the Workflow implementation code.

```java
Workflow.registerListener(
  (DynamicQueryHandler)
      (queryName, encodedArgs) -> name = encodedArgs.get(0, String.class));
```

When registered, any Queries sent to the Workflow without a defined handler will be delivered to the `DynamicQueryHandler`.
Note that you can only register one `Workflow.registerListener(Object)` per Workflow Execution.
`DynamicQueryHandler` can be implemented in both regular and dynamic Workflow implementations.

### How to set a Dynamic Update {/* #set-a-dynamic-update */}

You can also implement Update handlers dynamically.
This is useful for library-level code and implementation of DSLs.

```java
Workflow.registerListener(
  (DynamicUpdateHandler)
      (updateName, encodedArgs) -> encodedArgs.get(0, String.class));
```

When registered, any Updates sent to the Workflow without a defined handler will be delivered to the `DynamicUpdateHandler`.
You can only register one `Workflow.registerListener(Object)` per Workflow Execution.
`DynamicUpdateHandler` can be implemented in both regular and dynamic Workflow implementations.

---

## Schedules - Java SDK

This page shows how to do the following:

- [How to Schedule a Workflow](#schedule-a-workflow)
  - [How to create a Schedule in Java](#create-schedule)
  - [How to backfill a Schedule in Java](#backfill-schedule)
  - [How to delete a Schedule in Java](#delete-schedule)
  - [How to describe a Schedule in Java](#describe-schedule)
  - [How to list a Schedule in Java](#list-schedule)
  - [How to pause a Schedule in Java](#pause-schedule)
  - [How to trigger a Schedule in Java](#trigger-schedule)
  - [How to update a Schedule in Java](#update-schedule)
- [How to set a Cron Schedule in Java](#cron-schedule)
- [Start Delay](#start-delay)

## How to Schedule a Workflow {/* #schedule-a-workflow */}

Scheduling Workflows is a crucial aspect of any automation process, especially when dealing with time-sensitive tasks. By scheduling a Workflow, you can automate repetitive tasks, reduce the need for manual intervention, and ensure timely execution of your business processes.

Use any of the following actions to help Schedule a Workflow Execution and take control over your automation process.

### How to create a Schedule in Java {/* #create-schedule */}

The create action enables you to create a new Schedule. When you create a new Schedule, a unique Schedule ID is generated, which you can use to reference the Schedule in other Schedule commands.

To create a Scheduled Workflow Execution in Java, use the `createSchedule()` method on the `ScheduleClient`. When you create the `ScheduleClient`, you can also use any custom Namespace instead of the default by setting the [`ScheduleClientOptions`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/schedules/ScheduleClientOptions.Builder.html). Schedules must be initialized with a Schedule ID.

```java
Schedule schedule =
    Schedule.newBuilder()
        .setAction(
            ScheduleActionStartWorkflow.newBuilder()
                .setWorkflowType(HelloSchedules.GreetingWorkflow.class)
                .setArguments("World")
                .setOptions(
                    WorkflowOptions.newBuilder()
                        .setWorkflowId("WorkflowId")
                        .setTaskQueue("TaskQueue")
                        .build())
                .build())
        .setSpec(ScheduleSpec.newBuilder()
                .setIntervals(
                    Collections.singletonList(new ScheduleIntervalSpec(Duration.ofSeconds(5)))
                ).build()
            )
        .build();

// Create a schedule on the server
ScheduleClient scheduleClient = ScheduleClient
    .newInstance(service, ScheduleClientOptions.newBuilder()
        .setNamespace("custom_namespace")
        .build()
    );

ScheduleHandle handle =
    scheduleClient.createSchedule("ScheduleId", schedule, ScheduleOptions.newBuilder().build());
```

:::tip Schedule Auto-Deletion

Once a Schedule has completed creating all its Workflow Executions, the Temporal Service deletes it since it won’t fire again.
The Temporal Service doesn't guarantee when this removal will happen.

:::

### How to backfill a Schedule in Java {/* #backfill-schedule */}

The backfill action executes Actions ahead of their specified time range. This command is useful when you need to execute a missed or delayed Action, or when you want to test the Workflow before its scheduled time.

To Backfill a Scheduled Workflow Execution in Java, use the `backfill()` method on the `ScheduleHandle`.

```java
ScheduleHandle handle = client.getHandle("schedule-id")

Instant now = Instant.now();
handle.backfill(
    Arrays.asList(
        new ScheduleBackfill(now.minusMillis(5500), now.minusMillis(2500)),
        new ScheduleBackfill(now.minusMillis(2500), now)));
```

### How to delete a Schedule in Java {/* #delete-schedule */}

The delete action enables you to delete a Schedule. When you delete a Schedule, it does not affect any Workflows that were started by the Schedule.

To delete a Scheduled Workflow Execution in Java, use the `delete()` method on the `Schedule Handle`.

```java
ScheduleHandle handle = client.getHandle("schedule-id")
handle.delete();
```

### How to describe a Schedule in Java {/* #describe-schedule */}

The describe action shows the current Schedule configuration, including information about past, current, and future Workflow Runs. This command is helpful when you want to get a detailed view of the Schedule and its associated Workflow Runs.

To describe a Scheduled Workflow Execution in Java, use the `describe()` method on the `ScheduleHandle`.

```java
ScheduleHandle handle = client.getHandle("schedule-id")
ScheduleDescription description = handle.describe();
```

### How to list a Schedule in Java {/* #list-schedule */}

The list action lists all the available Schedules. This command is useful when you want to view a list of all the Schedules and their respective Schedule IDs.

To list all schedules, use the `listSchedules()` asynchronous method on the `ScheduleClient`.
If a schedule is added or deleted, it may not be available in the list immediately.

```java
Stream<ScheduleListDescription> scheduleStream = client.listSchedules();
```

### How to pause a Schedule in Java {/* #pause-schedule */}

The pause action enables you to pause and unpause a Schedule. When you pause a Schedule, all the future Workflow Runs associated with the Schedule are temporarily stopped. This command is useful when you want to temporarily halt a Workflow due to maintenance or any other reason.
