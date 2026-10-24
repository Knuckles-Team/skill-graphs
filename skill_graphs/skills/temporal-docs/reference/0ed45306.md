Instead, wait for your handlers to finish in your main Workflow before you run `continueAsNew`.

## When is it right to Continue-as-New using the Java SDK? {/* #when */}

Use Continue-as-New when your Workflow might hit [Event History Limits](/workflow-execution/event#event-history).

Temporal tracks your Workflow's progress against these limits to let you know when you should Continue-as-New.
Call `Workflow.getInfo().isContinueAsNewSuggested()` to check if it's time.

## How to test Continue-as-New using the Java SDK {/* #how-to-test */}

Testing Workflows that naturally Continue-as-New may be time-consuming and resource-intensive.
Instead, add a test hook to check your Workflow's Continue-as-New behavior faster in automated tests.

For example, when `testContinueAsNew == true`, this sample creates a test-only variable called `maxHistoryLength` and sets it to a small value.
A helper method in the Workflow checks it each time it considers using Continue-as-New:

    View the source code
  {' '}
  in the context of the rest of the application code.

```java
private boolean shouldContinueAsNew() {
  if (Workflow.getInfo().isContinueAsNewSuggested()) {
    return true;
  }
  // This is just for ease-of-testing.  In production, we trust temporal to tell us when to
  // continue as new.
  if (maxHistoryLength > 0 && Workflow.getInfo().getHistoryLength() > maxHistoryLength) {
    return true;
  }
  return false;
}
```

---

## Workflows - Java SDK

![Java SDK Banner](/img/assets/banner-java-temporal.png)

## Workflows

- [Workflow basics](/develop/java/workflows/basics)
- [Child Workflows](/develop/java/workflows/child-workflows)
- [Continue-As-New](/develop/java/workflows/continue-as-new)
- [Message passing](/develop/java/workflows/message-passing)
- [Cancellation](/develop/java/workflows/cancellation)
- [Timeouts](/develop/java/workflows/timeouts)
- [Schedules](/develop/java/workflows/schedules)
- [Timers](/develop/java/workflows/timers)
- [Side effects](/develop/java/workflows/side-effects)
- [Versioning](/develop/java/workflows/versioning)

---

## Workflow message passing - Java SDK

A Workflow can act like a stateful web service that receives messages: Queries, Signals, and Updates.
The Workflow implementation defines these endpoints via handler methods that can react to incoming messages and return values.
Temporal Clients use messages to read Workflow state and control execution.
See [Workflow message passing](/encyclopedia/workflow-message-passing) for a general overview of this topic.
This page introduces these features for the Temporal Java SDK.

## Write message handlers {/* #writing-message-handlers */}

Follow these guidelines when writing your message handlers:

- Message handlers are defined as methods on the Workflow class, using one of the three annotations: [`@QueryMethod`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/QueryMethod.html), [`@SignalMethod`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/SignalMethod.html), and [`@UpdateMethod`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/UpdateMethod.html).
- The parameters and return values of handlers and the main Workflow function must be [serializable](/dataconversion).
- Prefer a single class with multiple fields over using multiple input parameters.
  A class allows you to add fields without changing the calling signature.

### Query handlers {/* #queries */}

A [Query](/sending-messages#sending-queries) is a synchronous operation that retrieves state from a Workflow Execution:

```java
public class MessagePassingIntro {

    public enum Language {
        CHINESE,
        ENGLISH,
        FRENCH,
        SPANISH,
        PORTUGUESE,
    }

    public static class GetLanguagesInput {
        public boolean includeUnsupported;

        public GetLanguagesInput() {
            this.includeUnsupported = false;
        }

        public GetLanguagesInput(boolean includeUnsupported) {
            this.includeUnsupported = includeUnsupported;
        }
    }

    @WorkflowInterface
    public interface GreetingWorkflow {
        ...
        // 👉 Use the @QueryMethod annotation to define a Query handler in the
        // Workflow interface.
        @QueryMethod
        List<Language> getLanguages(GetLanguagesInput input);
    }

    public static class GreetingWorkflowImpl implements GreetingWorkflow {
        ...
        @Override
        public List<Language> getLanguages(GetLanguagesInput input) {
            // 👉 The Query handler returns a value: it must not mutate the Workflow state
            // or perform blocking operations.
            if (input.includeUnsupported) {
                return Arrays.asList(Language.values());
            } else {
                return new ArrayList(greetings.keySet());
            }
        }
    }

}
```

- A Query handler must not modify Workflow state.
- You can't perform blocking operations such as executing an Activity in a Query handler.
- The Query annotation accepts an argument (`name`) as described in the API reference docs for [`@QueryMethod`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/QueryMethod.html).

### Signal handlers {/* #signals */}

A [Signal](/sending-messages#sending-signals) is an asynchronous message sent to a running Workflow Execution to change its state and control its flow:

```java
public class MessagePassingIntro {

    public static class ApproveInput {
        private String name;

        public ApproveInput() {}

        public ApproveInput(String name) {
            this.name = name;
        }
    }

    @WorkflowInterface
    public interface GreetingWorkflow {
        ...
        // 👉 Use the @SignalMethod annotation to define a Signal handler in the
        // Workflow interface.
        @SignalMethod
        void approve(ApproveInput input);
    }

    public static class GreetingWorkflowImpl implements GreetingWorkflow {
        ...
        private Boolean approvedForRelease;
        private String approverName;

        @Override
        public void approve(ApproveInput input) {
            // 👉 The Signal handler mutates the Workflow state but cannot return a value.
            this.approvedForRelease = true;
            this.approverName = input.name;
        }
    }
}
```

- The handler should not return a value.
  The response is sent immediately from the server, without waiting for the Workflow to process the Signal.

- The Signal annotation accepts arguments (`name`, and `unfinished_policy`) as described in the API reference docs for [`@SignalMethod`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/SignalMethod.html).

- Signal (and Update) handlers can be blocking.
  This allows you to use Activities, Child Workflows, durable [`Workflow.sleep`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#sleep(java.time.Duration)) Timers, [`Workflow.await`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#await(java.time.Duration,java.util.function.Supplier)), and more.
  See [Blocking handlers](#blocking-handlers) and [Workflow message passing](/encyclopedia/workflow-message-passing) for guidelines on safely using blocking Signal and Update handlers.

### Update handlers and validators {/* #updates */}

An [Update](/sending-messages#sending-updates) is a trackable synchronous request sent to a running Workflow Execution.
It can change the Workflow state, control its flow, and return a result.
The sender must wait until the Worker accepts or rejects the Update.
The sender may wait further to receive a returned value or an exception if something goes wrong:

```java
public class MessagePassingIntro {
    @WorkflowInterface
    public interface GreetingWorkflow {
        ...
        // 👉 Use the @UpdateMethod annotation to define an Update handler in the
        // Workflow interface.
        @UpdateMethod
        Language setLanguage(Language language);

        // 👉 Update validators are optional
        @UpdateValidatorMethod(updateName = "setLanguage")
        void setLanguageValidator(Language language);
    }

    public static class GreetingWorkflowImpl implements GreetingWorkflow {
        ...
        @Override
        public Language setLanguage(Language language) {
            // 👉 The Update handler can mutate the Workflow state and return a value.
            Language previousLanguage = this.language;
            this.language = language;
            return previousLanguage;
        }

        @Override
        public void setLanguageValidator(Language language) {
            // 👉 The Update validator performs validation but cannot mutate the Workflow state.
            if (!greetings.containsKey(language)) {
                throw new IllegalArgumentException("Unsupported language: " + language);
            }
        }
    }
}
```

- The Update annotation accepts arguments (`name`, and `unfinished_policy`) as described in the API reference docs for [`@UpdateMethod`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/UpdateMethod.html).

- About validators:
  - Use validators to reject an Update before it is written to History.
    Validators are always optional.
    If you don't need to reject Updates, you can skip them.
  - Define an Update validator with the `@UpdateValidatorMethod` annotation.
    Use the `updateName` argument when declaring the validator to connect it to its Update.
    The validator must return `void` and accept the same argument types as the handler.

- Accepting and rejecting Updates with validators:
  - To reject an Update, throw an exception of any type in the validator.
  - Without a validator, Updates are always accepted.
- Validators and Event History:
  - The `WorkflowExecutionUpdateAccepted` event is written into the History whether the acceptance was automatic or programmatic.
  - When a Validator throws an error, the Update is rejected, the Update is not run, and `WorkflowExecutionUpdateAccepted` _won't_ be added to the Event History.
    The caller receives an "Update failed" error.

- Use [`getCurrentUpdateInfo`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/internal/sync/WorkflowInternal.html#getCurrentUpdateInfo()) to obtain information about the current Update. This includes the Update ID, which can be useful for deduplication when using Continue-As-New: see [Ensuring your messages are processed exactly once](https://docs.temporal.io/handling-messages#exactly-once-message-processing).

- Signal (and Update) handlers can be blocking, letting them use Activities, Child Workflows, durable [`Workflow.sleep`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#sleep(java.time.Duration)) Timers, [`Workflow.await`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#await(java.time.Duration,java.util.function.Supplier)) conditions, and more.
  See [Blocking handlers](#blocking-handlers) and [Workflow message passing](/encyclopedia/workflow-message-passing) for safe usage guidelines.

## Send messages {/* #send-messages */}

To send Queries, Signals, or Updates you call methods on a `WorkflowInterface`, often called the "WorkflowStub."

Use [newWorkflowStub](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowClient.html#newWorkflowStub(java.lang.Class,io.temporal.client.WorkflowOptions)) to obtain the WorkflowStub.

For example:

```java
WorkflowServiceStubs service = WorkflowServiceStubs.newLocalServiceStubs();

WorkflowClient client = WorkflowClient.newInstance(service);

WorkflowOptions workflowOptions =
    WorkflowOptions.newBuilder().setTaskQueue(TASK_QUEUE).setWorkflowId(WORKFLOW_ID).build();

// Create the workflow client stub. It is used to start the workflow execution.
GreetingWorkflow workflow = client.newWorkflowStub(GreetingWorkflow.class, workflowOptions);

// Start workflow asynchronously and call its getGreeting workflow method
WorkflowClient.start(workflow::getGreetings);
```

To check the argument types required when sending messages -- and the return type for Queries and Updates -- refer to the corresponding handler method in the Workflow Definition.

:::warning Using Continue-as-New and Updates

- Temporal _does not_ support Continue-as-New functionality within Update handlers.
- Complete all handlers _before_ using Continue-as-New.
- Use Continue-as-New from your main Workflow Definition method, just as you would complete or fail a Workflow Execution.

:::

### Send a Query {/* #send-query */}

Call a Query method defined within a Workflow from a `WorkflowStub` created in Client code to send a Query to a Workflow Execution:

```java
List<Language> languages = workflow.getLanguages(new GetLanguagesInput(false));
System.out.println("Supported languages: " + languages);
```

- Sending a Query doesn’t add events to a Workflow's Event History.

- You can send Queries to closed Workflow Executions within a Namespace's Workflow retention period.
  This includes Workflows that have completed, failed, or timed out.
  Querying terminated Workflows is not safe and, therefore, not supported.

- A Worker must be online and polling the Task Queue to process a Query.

### Send a Signal {/* #send-signal */}

You can send a Signal to a Workflow Execution from a Temporal Client or from another Workflow Execution.
However, you can only send Signals to Workflow Executions that haven’t closed.

#### Send a Signal from a Client {/* #send-signal-from-client */}

To send a Signal from Client code, call a Signal method on the WorkflowStub:

```java
workflow.approve(new ApproveInput("Me"));
```

- The call returns when the server accepts the Signal; it does _not_ wait for the Signal to be delivered to the Workflow Execution.

- The [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the Workflow's Event History.

#### Send a Signal from a Workflow {/* #send-signal-from-workflow */}

A Workflow can send a Signal to another Workflow, known as an _External Signal_.
Use [`Workflow.newExternalWorkflowStub`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#newExternalWorkflowStub(java.lang.Class,io.temporal.api.common.v1.WorkflowExecution)) in your _current_ Workflow to create an `ExternalWorkflowStub` for the other Workflow.
Call Signal methods on the external stub to Signal the other Workflow:

```java
OtherWorkflow other = Workflow.newExternalWorkflowStub(OtherWorkflow.class, otherWorkflowID);
other.mySignalMethod();
```

When an External Signal is sent:

- A [SignalExternalWorkflowExecutionInitiated](/references/events#signalexternalworkflowexecutioninitiated) Event appears in the sender's Event History.
- A [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the recipient's Event History.

#### Signal-With-Start {/* #signal-with-start */}

Signal-With-Start allows a Client to send a Signal to a Workflow Execution, starting the Execution if it is not already running.
If there's a Workflow running with the given Workflow Id, it will be signaled.
If there isn't, a new Workflow will be started and immediately signaled.
To use Signal-With-Start, call `signalWithStart` and pass the name of your Signal with its arguments:

```java
public static void signalWithStart() {
    // WorkflowStub is a client-side stub to a single Workflow instance
    WorkflowStub untypedWorkflowStub = client.newUntypedWorkflowStub("GreetingWorkflow",
    WorkflowOptions.newBuilder()
            .setWorkflowId(workflowId)
            .setTaskQueue(taskQueue)
            .build());

    untypedWorkflowStub.signalWithStart("setCustomer", new Object[] {customer2}, new Object[] {customer1});

    String greeting = untypedWorkflowStub.getResult(String.class);
}
```

Here's the `WorkflowInterface` for the previous example.
When using Signal-With-Start, the Signal handler (`setCustomer`) will be executed before the Workflow method (`greet`).

```java
@WorkflowInterface
public interface GreetingWorkflow {
    @WorkflowMethod
    String greet(Customer customer);

    @SignalMethod
    void setCustomer(Customer customer);

    @QueryMethod
    Customer getCustomer();
}
```

### Send an Update {/* #send-update-from-client */}

An Update is a synchronous, blocking call that can change Workflow state, control its flow, and return a result.

A Client sending an Update must wait until the Server delivers the Update to a Worker.
Workers must be available and responsive.
If you need a response as soon as the Server receives the request, use a Signal instead.
You can't send Updates directly from one Workflow to another. If you need to send Updates across Workflows, like to Child Workflows, use an Activity.

- `WorkflowExecutionUpdateAccepted` is added to the Event History when the Worker confirms that the Update passed validation.
- `WorkflowExecutionUpdateCompleted` is added to the Event History when the Worker confirms that the Update has finished.

To send an Update to a Workflow Execution, you can:

- Call the Update method on a WorkflowStub in Client code and wait for the Update to complete.
  This code fetches an Update result:

  ```java
  Language previousLanguage = workflow.setLanguage(Language.CHINESE);
  ```

- Send [`startUpdate`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html#startUpdate(io.temporal.client.UpdateOptions,java.lang.Object...)) to receive an [`WorkflowUpdateHandle`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowUpdateHandle.html) as soon as the Update is accepted or rejected.

  - Use this `WorkflowUpdateHandle` later to fetch your results.
  - Blocking Update handlers normally perform long-running asynchronous operations.
  - `startUpdate` only waits until the Worker has accepted or rejected the Update, not until all asynchronous operations are complete.

  For example:

  ```java
  WorkflowUpdateHandle<Language> handle =
      WorkflowStub.fromTyped(workflow)
          .startUpdate(
              "setLanguage", WorkflowUpdateStage.ACCEPTED, Language.class, Language.ENGLISH);
  previousLanguage = handle.getResultAsync().get();
  ```

  For more details, see the "Blocking handlers" section.

To obtain an Update handle, you can:

- Use [`startUpdate`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html#startUpdate(io.temporal.client.UpdateOptions,java.lang.Object...)) to start an Update and return the handle, as shown in the preceding example.
- Use [`getUpdateHandle`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html#getUpdateHandle(java.lang.String,java.lang.Class)) to fetch a handle for an in-progress Update using the Update ID and Workflow ID.

You can use the `WorkflowUpdateHandle` to obtain information about the update:

- `getExecution()`: Returns the Workflow Execution that this Update was sent to.
- `getId()`: Returns the Update's unique ID, which can be useful for deduplication when using Continue-As-New: see [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing).
- `getResultAsync()`: Returns a `CompletableFuture` which can be used to wait for the Update to complete.

#### Update-With-Start {/* #update-with-start */}

:::tip

For open source server users, Temporal Server version [Temporal Server version 1.28](https://github.com/temporalio/temporal/releases/tag/v1.28.0) is recommended.

:::

[Update-with-Start](/sending-messages#update-with-start) lets you
[send an Update](/develop/java/workflows/message-passing#send-update-from-client) that checks whether an already-running Workflow with that ID exists:

- If the Workflow exists, the Update is processed.
- If the Workflow does not exist, a new Workflow Execution is started with the given ID, and the Update is processed before the main Workflow method starts to execute.

Use the [`startUpdateWithStart`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowClient.html#startUpdateWithStart(io.temporal.workflow.Functions.Func,io.temporal.client.UpdateOptions,io.temporal.client.WithStartWorkflowOperation)) WorkflowClient API.
It returns once the requested Update wait stage has been reached; or when the request times out.
Use the [`WorkflowUpdateHandle`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowUpdateHandle.html) to retrieve a result from the Update.

You will need to provide:

- WorkflowStub created from [`WorkflowOptions`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowOptions.html).
  The `WorkflowOptions` require [Workflow Id Conflict Policy](/workflow-execution/workflowid-runid#workflow-id-conflict-policy) to be specified.
  Choose "Use Existing" and use an idempotent Update handler to ensure your code can be executed again in case of a Client failure.
  Not all `WorkflowOptions` are allowed.
  For example, specifying a Cron Schedule will result in an error.

- [`UpdateOptions`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/UpdateOptions.html).
  Same as for [Update Workflow](/develop/java/workflows/message-passing#send-update-from-client), the update wait stage must be specified.
  For Update-with-Start, the Workflow Id is optional.
  When specified, the Id must match the one used in `WorkflowOptions`.
  Since a running Workflow Execution may not already exist, you can't set a Run Id.

- [`WithStartWorkflowOperation`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WithStartWorkflowOperation.html).
  Specify the workflow method.
  Note that a `WithStartWorkflowOperation` can only be used once.
  Re-using a previously used operation returns an error from `startUpdateWithStart`.

For example:

```java
WorkflowUpdateHandle<Language> handle =
    WorkflowClient.startUpdateWithStart(
        workflow::setLanguage,
        Language.ENGLISH,
        UpdateOptions.<Language>newBuilder().setWaitForStage(WorkflowUpdateStage.ACCEPTED).build(),
        new WithStartWorkflowOperation<>(workflow::getGreetings));

Language previousLanguage = handle.getResultAsync().get();
```

To obtain the update result directly, use the [`executeUpdateWithStart`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowClient.html#executeUpdateWithStart(io.temporal.workflow.Functions.Func,io.temporal.client.UpdateOptions,io.temporal.client.WithStartWorkflowOperation)) WorkflowClient API.
It returns once the update result is available; or when the API call times out.
The update wait stage on the `UpdateOptions` is optional.
When specified, it must be `WorkflowUpdateStage.COMPLETED`.

For example:

```java
Language previousLanguage =
    WorkflowClient.executeUpdateWithStart(
        workflow::setLanguage,
        Language.ENGLISH,
        UpdateOptions.<Language>newBuilder().build(),
        new WithStartWorkflowOperation<>(workflow::getGreetings));
```

For more examples, see the [Java sample for early-return pattern](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/earlyreturn).

:::info NON-TYPE SAFE API CALLS

In real-world development, sometimes you may be unable to import Workflow Definition method signatures.
When you don't have access to the Workflow Definition or it isn't written in Java, you can use these non-type safe APIs to obtain an untyped WorkflowStub:

- [`WorkflowClient.newUntypedWorkflowStub`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowClient.html#newUntypedWorkflowStub(java.lang.String,io.temporal.client.WorkflowOptions))
- [`Workflow.newUntypedExternalWorkflowStub`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/workflow/Workflow.html#newUntypedExternalWorkflowStub(java.lang.String)).

Pass method names instead of method objects to:

- [`WorkflowStub.query`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html#query(java.lang.String,java.lang.Class,java.lang.Object...))
- [`WorkflowStub.signal`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html#signal(java.lang.String,java.lang.Object...))
- [`WorkflowStub.update`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html#update(java.lang.String,java.lang.Class,java.lang.Object...))
- [`WorkflowStub.startUpdateWithStart`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html#startUpdateWithStart(io.temporal.client.UpdateOptions,java.lang.Object%5B%5D,java.lang.Object%5B%5D))
- [`WorkflowStub.executeUpdateWithStart`](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/client/WorkflowStub.html#executeUpdateWithStart(io.temporal.client.UpdateOptions,java.lang.Object%5B%5D,java.lang.Object%5B%5D))

:::

## Message handler patterns {/* #message-handler-patterns */}

This section covers common write operations, such as Signal and Update handlers.
It doesn't apply to pure read operations, like Queries or Update Validators.

:::tip

For additional information, see [Inject work into the main Workflow](/handling-messages#injecting-work-into-main-workflow), and [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing).
