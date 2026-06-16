    List<String> getHistory();

    @QueryMethod
    String getStatus();

    @SignalMethod
    void abandon();
}
```

Then some other Workflow interface can extend just `Retryable`, for example:

```java
@WorkflowInterface
public interface MediaProcessingWorkflow extends Retryable {

    @WorkflowMethod
    String processBlob(Arguments args);
}
```

Now if we have two running Workflows, one that implements the `FileProcessingWorkflow` interface and another that implements the `MediaProcessingWorkflow` interface, we can Signal to both using their common interface and knowing their WorkflowIds, for example:

```java
Retryable r1 = client.newWorkflowStub(Retryable.class, firstWorkflowId);
Retryable r2 = client.newWorkflowStub(Retryable.class, secondWorkflowId);
r1.retryNow();
r2.retryNow();
```

The same technique can be used to query Workflows using a base Workflow interface.

Note that this approach does not apply to `@WorkflowMethod` annotations, meaning that when using a base interface, it should not include any `@WorkflowMethod` methods.
To illustrate this, let's say that we define the following **invalid** code:

```java
// INVALID CODE!
public interface BaseWorkflow {
    @WorkflowMethod
    void retryNow();
}

@WorkflowInterface
public interface Workflow1 extends BaseWorkflow {}

@WorkflowInterface
public interface Workflow2 extends BaseWorkflow {}
```

Any attempt to register both implementations with the Worker will fail.
Let's say that we have:

```java
worker.registerWorkflowImplementationTypes(
    Workflow1Impl.class, Workflow2Impl.class);
```

This registration will fail with:

```text
java.lang.IllegalStateException: BaseWorkflow workflow type is already registered with the worker
```

## Define Workflow parameters {/* #workflow-parameters */}

Temporal Workflows may have any number of custom parameters.
However, we strongly recommend that objects are used as parameters, so that the object's individual fields may be altered without breaking the signature of the Workflow.
All Workflow Definition parameters must be serializable.

A method annotated with `@WorkflowMethod` can have any number of parameters.

We recommend passing a single parameter that contains all the input fields to allow for adding fields in a backward-compatible manner.

Note that all inputs should be serializable by the default Jackson JSON Payload Converter.

You can create a custom object and pass it to the Workflow method, as shown in the following example.

```java
//...
@WorkflowInterface
public interface YourWorkflow {
    @WorkflowMethod
    String yourWFMethod(CustomObj customobj);
// ...
}
```

## Define Workflow return parameters {/* #workflow-return-values */}

Workflow return values must also be serializable.
Returning results, returning errors, or throwing exceptions is fairly idiomatic in each language that is supported.
However, Temporal APIs that must be used to get the result of a Workflow Execution will only ever receive one of either the result or the error.

Workflow method arguments and return values must be serializable and deserializable using the provided [`DataConverter`](https://www.javadoc.io/static/io.temporal/temporal-sdk/1.17.0/io/temporal/common/converter/DataConverter.html).

The `execute` method for `DynamicWorkflow` can return type Object.
Ensure that your Client can handle an Object type return or is able to convert the Object type response.

Related references:

- [Data Converter](/dataconversion)
- [Java DataConverter reference](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/common/converter/DataConverter.html)

## Customize your Workflow Type {/* #workflow-type */}

Workflows have a Type that is referred to as the Workflow name.

The following examples demonstrate how to set a custom name for your Workflow Type.

The Workflow Type defaults to the short name of the Workflow interface.
In the following example, the Workflow Type defaults to `NotifyUserAccounts`.

```java
  @WorkflowInterface

  public interface NotifyUserAccounts {
    @WorkflowMethod
    void notify(String[] accountIds);
}
```

To overwrite this default naming and assign a custom Workflow Type, use the `@WorkflowMethod` annotation with the `name` parameter.
In the following example, the Workflow Type is set to `your-workflow`.

```java
@WorkflowInterface

  public interface NotifyUserAccounts {
  @WorkflowMethod(name = "your-workflow")
  void notify(String[] accountIds);
  }
```

When you set the Workflow Type this way, the value of the `name` parameter does not have to start with an uppercase letter.

## Workflow logic requirements {/* #workflow-logic-requirements */}

Workflow logic is constrained by [deterministic execution requirements](/workflow-definition#deterministic-constraints). Each Temporal SDK provides a set of APIs that can be used inside your Workflow to interact with external (to the Workflow) application code.

When defining Workflows using the Temporal Java SDK, the Workflow code must be written to execute effectively once and to completion.

The following constraints apply when writing Workflow Definitions:

- Do not use mutable global variables in your Workflow implementations. This will ensure that multiple Workflow instances are fully isolated.
- Workflow code must be deterministic. If you need to call non-deterministic functions (such as non-seeded random or `UUID.randomUUID()`) directly from the Workflow code, the Temporal SDK provides specific API for calling non-deterministic code in your Workflows.
  - For operations like calling external APIs, invoking LLMs, querying databases, or performing I/O, use Activities. Activities run outside Workflow replay and are retried reliably.
- Use Temporal-provided functions instead of that rely on system time. For example, use only `Workflow.currentTimeMillis()` to get the current time inside a Workflow.
- Use `Async.function` or `Async.procedure`, provided by the Temporal SDK, to execute code asynchronously instead of native Java `Thread` or any other multi-threaded classes like `ThreadPoolExecutor`.
- Use only the concurrency features provided by the Workflow class. Multi-threaded code inside a Workflow is executed one thread at a time and under a global lock, so there is no need for explicit synchronization.
  - Call `Workflow.sleep` instead of `Thread.sleep`.
  - Use `Promise` and `CompletablePromise` instead of `Future` and `CompletableFuture`.
  - Use `WorkflowQueue` instead of `BlockingQueue`.
- Use `Workflow.getVersion` when making any changes to the Workflow code to avoid deployment of updated Workflow code interfering with already-running Workflows.
- Do not access configuration APIs directly from a Workflow because changes in the configuration might affect a Workflow Execution path. Instead, pass it as an argument to a Workflow function or use an Activity to load it.
- Use `DynamicWorkflow` when you need a default Workflow that can handle all Workflow Types that are not registered with a Worker. A single implementation can implement a Workflow Type which by definition is dynamically loaded from some external source. All standard `WorkflowOptions` and determinism rules apply to Dynamic Workflow implementations.

Java Workflow reference: [https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/package-summary.html](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/package-summary.html)

---

## Interrupt a Workflow Execution - Java SDK

You can interrupt a Workflow Execution in one of the following ways:

- [Cancel](#cancellation): Canceling a Workflow provides a graceful way to stop Workflow Execution.
- [Terminate](#termination): Terminating a Workflow forcefully stops Workflow Execution.

Terminating a Workflow forcefully stops Workflow Execution. This action resembles killing a process.

- The system records a `WorkflowExecutionTerminated` event in the Event History.
- The termination forcefully and immediately stops the Workflow Execution.
- The Workflow code gets no chance to handle termination.
- A Workflow Task doesn't get scheduled.

In most cases, canceling is preferable because it allows the Workflow to finish gracefully. Terminate only if the
Workflow is stuck and cannot be canceled normally.

## Cancel a Workflow Execution {/* #cancellation */}

Canceling a Workflow provides a graceful way to stop Workflow Execution. This action resembles sending a `SIGTERM` to a
process.

- The system records a `WorkflowExecutionCancelRequested` event in the Event History.
- A Workflow Task gets scheduled to process the cancelation.
- The Workflow code can handle the cancelation and execute any cleanup logic.
- The system doesn't forcefully stop the Workflow.

To cancel a Workflow Execution in Java, use the
[cancel()](<https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html#cancel()>)
function on the WorkflowStub.

```java
WorkflowStub workflowStub = WorkflowStub.fromTyped(workflow);
workflowStub.cancel();
```

## Cancellation scopes in Java {/* #cancellation-scopes */}

In the Java SDK, Workflows are represented internally by a tree of cancellation scopes, each with cancellation behaviors
you can specify. By default, everything runs in the "root" scope.

Scopes are created using the
[Workflow.newCancellationScope](<https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#newCancellationScope(io.temporal.workflow.Functions.Proc1)>)
constructor

Cancellations are applied to cancellation scopes, which can encompass an entire Workflow or just part of one. Scopes can
be nested, and cancellation propagates from outer scopes to inner ones. A Workflow's method runs in the outermost scope.
Cancellations are handled by catching `CanceledFailure`s thrown by cancelable operations.

You can also use the following APIs:

- `CancellationScope.current()`: Get the current scope.
- `scope.cancel()`: Cancel all operations inside a `scope`.
- `scope.getCancellationRequest()`: A promise that resolves when a scope cancellation is requested, such as when
  Workflow code calls `cancel()` or the entire Workflow is cancelled by an external client.

When a `CancellationScope` is cancelled, it propagates cancellation in any child scopes and of any cancelable operations
created within it, such as the following:

- Activities
- Timers (created with the
  [sleep](<https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#sleep(java.time.Duration)>)
  function)
- Child Workflows
- Nexus Operations

### Cancel an Activity from a Workflow {/* #cancel-activity */}

Canceling an Activity from within a Workflow requires that the Activity Execution sends Heartbeats and sets a Heartbeat
Timeout. If the Heartbeat is not invoked, the Activity cannot receive a cancellation request. When any non-immediate
Activity is executed, the Activity Execution should send Heartbeats and set a
[Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) to ensure that the server knows it is
still working.

When an Activity is canceled, an error is raised in the Activity at the next available opportunity. If cleanup logic
needs to be performed, it can be done in a `finally` clause or inside a caught cancel error. However, for the Activity
to appear canceled the exception needs to be re-raised.

:::note

Unlike regular Activities, [Local Activities](/local-activity) currently do not support cancellation.

:::

To cancel an Activity from a Workflow Execution, call the
[cancel()](<https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/CancellationScope.html#cancel()>)
method on the CancellationScope that the activity was started in.

```java
public class GreetingWorkflowImpl implements GreetingWorkflow {
    @Override
    public String getGreeting(String name) {
      List<Promise<String>> results = new ArrayList<>(greetings.length);

      /*
       * Create our CancellationScope. Within this scope we call the workflow activity
       * composeGreeting method asynchronously for each of our defined greetings in different
       * languages.
       */
      CancellationScope scope =
          Workflow.newCancellationScope(
              () -> {
                for (String greeting : greetings) {
                  results.add(Async.function(activities::composeGreeting, greeting, name));
                }
              });

      /*
       * Execute all activities within the CancellationScope. Note that this execution is
       * non-blocking as the code inside our cancellation scope is also non-blocking.
       */
      scope.run();

      // We use "anyOf" here to wait for one of the activity invocations to return
      String result = Promise.anyOf(results).get();

      // Trigger cancellation of all uncompleted activity invocations within the cancellation scope
      scope.cancel();

      /*
       *  Wait for all activities to perform cleanup if needed.
       *  For the sake of the example we ignore cancellations and
       *  get all the results so that we can print them in the end.
       *
       *  Note that we cannot use "allOf" here as that fails on any Promise failures
       */
      for (Promise<String> activityResult : results) {
        try {
          activityResult.get();
        } catch (ActivityFailure e) {
          if (!(e.getCause() instanceof CanceledFailure)) {
            throw e;
          }
        }
      }
      return result;
    }
}
```

## Terminate a Workflow Execution {/* #termination */}

Terminating a Workflow forcefully stops Workflow Execution. This action resembles killing a process.

- The system records a `WorkflowExecutionTerminated` event in the Event History.
- The termination forcefully and immediately stops the Workflow Execution.
- The Workflow code gets no chance to handle termination.
- A Workflow Task doesn't get scheduled.

To terminate a Workflow Execution in Java, use the
[terminate()](<https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html#terminate(java.lang.String,java.lang.Object...)>)
function on the WorkflowStub.

```java
WorkflowStub untyped = WorkflowStub.fromTyped(myWorkflowStub);
untyped.terminate("Sample reason");
```

## Reset a Workflow Execution {/* #reset */}

Resetting a Workflow Execution terminates the current Workflow Execution and starts a new Workflow Execution from a
point you specify in its Event History. Use reset when a Workflow is blocked due to a non-deterministic error or other
issues that prevent it from completing.

When you reset a Workflow, the Event History up to the reset point is copied to the new Workflow Execution, and the
Workflow resumes from that point with the current code. Reset only works if you've fixed the underlying issue, such as
removing non-deterministic code. Any progress made after the reset point will be discarded. Provide a reason when
resetting, as it will be recorded in the Event History.

<Tabs>

<TabItem value="web-ui" label="Web UI">

1. Navigate to the Workflow Execution details page,
2. Click the **Reset** button in the top right dropdown menu,
3. Select the Event ID to reset to,
4. Provide a reason for the reset,
5. Confirm the reset.

The Web UI shows available reset points and creates a link to the new Workflow Execution after the reset completes.

</TabItem>

<TabItem value="cli" label="Temporal CLI">

Use the `temporal workflow reset` command to reset a Workflow Execution:

```bash
temporal workflow reset \
    --workflow-id <workflow-id> \
    --event-id <event-id> \
    --reason "Reason for reset"
```

For example:

```bash
temporal workflow reset \
    --workflow-id my-background-check \
    --event-id 4 \
    --reason "Fixed non-deterministic code"
```

By default, the command resets the latest Workflow Execution in the `default` Namespace. Use `--run-id` to reset a
specific run. Use `--namespace` to specify a different Namespace:

```bash
temporal workflow reset \
    --workflow-id my-background-check \
    --event-id 4 \
    --reason "Fixed non-deterministic code" \
    --namespace my-namespace \
    --tls-cert-path /path/to/cert.pem \
    --tls-key-path /path/to/key.pem
```

Monitor the new Workflow Execution after resetting to ensure it completes successfully.

</TabItem>

</Tabs>

---

## Child Workflows - Java SDK

This page shows how to do the following:

- [Start a Child Workflow Execution](#start-child-workflow)
- [Set a Parent Close Policy](#parent-close-policy)

## Start a Child Workflow Execution {/* #start-child-workflow */}

A [Child Workflow Execution](/child-workflows) is a Workflow Execution that is scheduled from within another Workflow using a Child Workflow API.

When using a Child Workflow API, Child Workflow related Events ([StartChildWorkflowExecutionInitiated](/references/events#startchildworkflowexecutioninitiated), [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted), [ChildWorkflowExecutionCompleted](/references/events#childworkflowexecutioncompleted), etc...) are logged in the Workflow Execution Event History.

The [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted) Event must be logged to the Event History before the Parent Workflow completes to ensure the Child Workflow has started.
In Java, you must explicitly call `Workflow.getWorkflowExecution(child)` to get a `Promise`, then call `.get()` on that Promise to wait for this Event.
See the [Parent Close Policy](#parent-close-policy) section below for a complete example.

### Async Child Workflows

The first call to the Child Workflow stub must always be its Workflow method (method annotated with `@WorkflowMethod`).
Similar to Activities, invoking Child Workflow methods can be made synchronous or asynchronous by using `Async#function` or `Async#procedure`.
The synchronous call blocks until a Child Workflow method completes.
The asynchronous call returns a `Promise` which can be used to wait for the completion of the Child Workflow method, as in the following example:

```java
GreetingChild child = Workflow.newChildWorkflowStub(GreetingChild.class);
Promise<String> greeting = Async.function(child::composeGreeting, "Hello", name);
// ...
greeting.get()
```

To execute an untyped Child Workflow asynchronously, call `executeAsync` on the `ChildWorkflowStub`, as shown in the following example.

```java
//...
ChildWorkflowStub childUntyped =
    Workflow.newUntypedChildWorkflowStub(
        "GreetingChild", // your workflow type
        ChildWorkflowOptions.newBuilder().setWorkflowId("childWorkflow").build());

Promise<String> greeting =
    childUntyped.executeAsync(String.class, String.class, "Hello", name);
String result = greeting.get();
//...
```

The following examples show how to spawn a Child Workflow:

- Spawn a Child Workflow from a Workflow

  ```java
  // Child Workflow interface
  @WorkflowInterface
  public interface GreetingChild {
  @WorkflowMethod
  String composeGreeting(String greeting, String name);
  }
  // Child Workflow implementation not shown

  // Parent Workflow implementation
  public class GreetingWorkflowImpl implements GreetingWorkflow {

  @Override
  public String getGreeting(String name) {
      GreetingChild child = Workflow.newChildWorkflowStub(GreetingChild.class);

      // This is a blocking call that returns only after child has completed.
      return child.composeGreeting("Hello", name );
  }
  }
  ```

- Spawn two Child Workflows (with the same type) in parallel:

  ```java
  // Parent Workflow implementation
  public class GreetingWorkflowImpl implements GreetingWorkflow {

      @Override
      public String getGreeting(String name) {

          // Workflows are stateful, so a new stub must be created for each new child.
          GreetingChild child1 = Workflow.newChildWorkflowStub(GreetingChild.class);
          Promise<String> greeting1 = Async.function(child1::composeGreeting, "Hello", name);

          // Both children will run concurrently.
          GreetingChild child2 = Workflow.newChildWorkflowStub(GreetingChild.class);
          Promise<String> greeting2 = Async.function(child2::composeGreeting, "Bye", name);

          // Do something else here.
          ...
          return "First: " + greeting1.get() + ", second: " + greeting2.get();
      }
  }
  ```

- Send a Signal to a Child Workflow from the parent:

  ```java
  // Child Workflow interface
  @WorkflowInterface
  public interface GreetingChild {
      @WorkflowMethod
      String composeGreeting(String greeting, String name);

      @SignalMethod
      void updateName(String name);
  }

  // Parent Workflow implementation
  public class GreetingWorkflowImpl implements GreetingWorkflow {

      @Override
      public String getGreeting(String name) {
          GreetingChild child = Workflow.newChildWorkflowStub(GreetingChild.class);
          Promise<String> greeting = Async.function(child::composeGreeting, "Hello", name);
          child.updateName("Temporal");
          return greeting.get();
      }
  }
  ```

- Sending a Query to Child Workflows from within the parent Workflow code is not supported. However, you can send a Query to Child Workflows from Activities using `WorkflowClient`.

Related reads:

- [How to develop a Workflow Definition](/develop/java/workflows/basics)

- Java Workflow reference: [https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/package-summary.html](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/package-summary.html)

## Parent Close Policy {/* #parent-close-policy */}

A [Parent Close Policy](/parent-close-policy) determines what happens to a Child Workflow Execution if its Parent changes to a Closed status (Completed, Failed, or Timed Out).

The default Parent Close Policy option is set to terminate the Child Workflow Execution.

Set [Parent Close Policy](/parent-close-policy) on an instance of `ChildWorkflowOptions` using [`ChildWorkflowOptions.newBuilder().setParentClosePolicy`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/ChildWorkflowOptions.Builder.html).

- Type: `ChildWorkflowOptions.Builder`
- Default: `PARENT_CLOSE_POLICY_TERMINATE`

```java
 public void parentWorkflow() {
     ChildWorkflowOptions options =
        ChildWorkflowOptions.newBuilder()
            .setParentClosePolicy(ParentClosePolicy.PARENT_CLOSE_POLICY_ABANDON)
            .build();
     MyChildWorkflow child = Workflow.newChildWorkflowStub(MyChildWorkflow.class, options);
     Async.procedure(child::<workflowMethod>, <args>...);
     Promise<WorkflowExecution> childExecution = Workflow.getWorkflowExecution(child);
     // Wait for child to start
     childExecution.get()
}
```

In this example, we are:

1. Setting `ChildWorkflowOptions.ParentClosePolicy` to `ABANDON` when creating a Child Workflow stub.
2. Starting Child Workflow Execution asynchronously using `Async.function` or `Async.procedure`.
3. Calling `Workflow.getWorkflowExecution(…)` on the child stub.
4. Waiting for the `Promise` returned by `getWorkflowExecution` to complete.
   This indicates whether the Child Workflow started successfully (or failed).
5. Completing parent Workflow Execution asynchronously.

Steps 3 and 4 are needed to ensure that a Child Workflow Execution starts before the parent closes.
If the parent initiates a Child Workflow Execution and then completes immediately after, the Child Workflow will never execute.

---

## Continue-As-New - Java SDK

This page answers the following questions for Java developers:

- [What is Continue-As-New?](#what)
- [How to Continue-As-New?](#how)
- [When is it right to Continue-as-New?](#when)
- [How to test Continue-as-New?](#how-to-test)

## What is Continue-As-New? {/* #what */}

[Continue-As-New](/workflow-execution/continue-as-new) lets a Workflow Execution close successfully and creates a new Workflow Execution.
You can think of it as a checkpoint when your Workflow gets too long or approaches certain scaling limits.

The new Workflow Execution is in the same [chain](/workflow-execution#workflow-execution-chain); it keeps the same Workflow Id but gets a new Run Id and a fresh Event History.
It also receives your Workflow's usual parameters.

## How to Continue-As-New using the Java SDK {/* #how */}

First, design your Workflow parameters so that you can pass in the "current state" when you Continue-As-New into the next Workflow run.
This state is typically set to `None` for the original caller of the Workflow.

    View the source code
  {' '}
  in the context of the rest of the application code.

```java
class ClusterManagerInput {
  private final Optional<ClusterManagerState> state;
  private final boolean testContinueAsNew;
}

@WorkflowMethod
ClusterManagerResult run(ClusterManagerInput input);

````
The test hook in the above snippet is covered [below](#how-to-test).

Inside your Workflow, call the [`continueAsNew()`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#continueAsNew(io.temporal.workflow.ContinueAsNewOptions,java.lang.Object...)) function with the same type.
This stops the Workflow right away and starts a new one.

    View the source code
  {' '}
  in the context of the rest of the application code.

```java
Workflow.continueAsNew(
  new ClusterManagerInput(Optional.of(state), input.isTestContinueAsNew()));
````

### Considerations for Workflows with Message Handlers {/* #with-message-handlers */}

If you use Updates or Signals, don't call Continue-as-New from the handlers.
