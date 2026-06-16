# Don't avoid, but rather encourage things using TaskScheduler.Current in workflows
dotnet_diagnostic.VSTHRD105.severity = none
```

### Customize Workflow Type {/* #workflow-type */}

Workflows have a Type that are referred to as the Workflow name.

The following examples demonstrate how to set a custom name for your Workflow Type.

You can customize the Workflow name with a custom name in the attribute. For example, `[Workflow("my-workflow-name")]`. If the name parameter is not specified, the Workflow name defaults to the unqualified class name.

```csharp
using Temporalio.Workflows;

[Workflow("MyDifferentWorkflowName")]
public class MyWorkflow
{
    public async Task<string> RunAsync(string name)
    {
        var param = MyActivityParams("Hello", name);
        return await Workflow.ExecuteActivityAsync(
            (MyActivities a) => a.MyActivity(param),
            new() { StartToCloseTimeout = TimeSpan.FromMinutes(5) });
    }
}
```

---

## Cancellation - .NET SDK

This page shows how to interrupt a Workflow Execution.

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

## Cancellation {/* #cancellation */}

To give a Workflow and its Activities the ability to be cancelled, do the following:

- Handle a Cancellation request within a Workflow.
- Set Activity Heartbeat Timeouts.
- Listen for and handle a Cancellation request within an Activity.
- Send a Cancellation request from a Temporal Client.

### Handle Cancellation in Workflow {/* #handle-cancellation-in-workflow */}

Workflow Definitions can be written to respond to cancellation requests. It is common for an Activity to be run on
Cancellation to perform cleanup.

Cancellation Requests on Workflows cancel the `Workflow.CancellationToken`. This is the token that is implicitly used
for all calls within the workflow as well (e.g. Timers, Activities, etc) and therefore cancellation is propagated to
them to be handled and bubble out.

```csharp
[WorkflowRun]
public async Task RunAsync()
{
    try
    {
        // Whether this workflow waits on the activity to handle the cancellation or not is
        // dependent upon the CancellationType option. We leave the default here which sends the
        // cancellation but does not wait on it to be handled.
        await Workflow.ExecuteActivityAsync(
            (MyActivities a) => a.MyNormalActivity(),
            new() { ScheduleToCloseTimeout = TimeSpan.FromMinutes(5) });
    }
    catch (Exception e) when (TemporalException.IsCanceledException(e))
    {
        // The "when" clause above is because we only want to apply the logic to cancellation, but
        // this kind of cleanup could be done on any/all exceptions too.
        Workflow.Logger.LogError(e, "Cancellation occurred, performing cleanup");

        // Call cleanup activity. If this throws, it will swallow the original exception which we
        // are ok with here. This could be changed to just log a failure and let the original
        // cancellation continue.
        // The default token on Workflow.CancellationToken is now marked
        // cancelled, so we pass a different one. We use CancellationToken.None here because the
        // cleanup activity itself doesn't need to be cancellable; if it did (e.g. you want to
        // cancel cleanup from a timeout or another signal), create a new detached
        // CancellationTokenSource and pass its Token instead.
        await Workflow.ExecuteActivityAsync(
            (MyActivities a) => a.MyCancellationCleanupActivity(),
            new()
            {
                ScheduleToCloseTimeout = TimeSpan.FromMinutes(5),
                CancellationToken = CancellationToken.None,
            });

        // Rethrow the cancellation
        throw;
    }
}
```

### Handle Cancellation in an Activity {/* #handle-cancellation-in-an-activity */}

Ensure that the Activity is [Heartbeating](/develop/dotnet/activities/timeouts#activity-heartbeats) to receive the
Cancellation request and stop execution. Also make sure that the
[Heartbeat Timeout](/develop/dotnet/activities/timeouts#heartbeat-timeout) is set on the Activity Options when calling
from the Workflow. An Activity Cancellation Request cancels the `CancellationToken` on the `ActivityExecutionContext`.

```csharp
[Activity]
public async Task MyActivityAsync()
{
    // This is a naive loop simulating work, but similar heartbeat/cancellation logic applies to
    // other scenarios as well
    while (true)
    {
        // Send heartbeat
        ActivityExecutionContext.Current.Heartbeat();

        // Do some work, passing the cancellation token
        await Task.Delay(1000, ActivityExecutionContext.Current.CancellationToken);
    }
}
```

### Request Cancellation {/* #request-cancellation */}

Use `CancelAsync` on the `WorkflowHandle` to cancel a Workflow Execution.

```csharp
// Get a workflow handle by its workflow ID. This could be made specific to a run by passing run ID.
// This could also just be a handle that is returned from StartWorkflowAsync instead.
var handle = myClient.GetWorkflowHandle("my-workflow-id");

// Send cancellation. This returns when cancellation is received by the server. Wait on the handle's
// result to wait for cancellation to be applied.
await handle.CancelAsync();
```

#### How to request Cancellation of an Activity

By default, Activities are automatically cancelled when the Workflow is cancelled since the workflow cancellation token
is used by activities by default. To issue a cancellation explicitly, a new cancellation token can be created.

```csharp
[WorkflowRun]
public async Task RunAsync()
{
    // Create a source linked to workflow cancellation. A new source could be created instead if we
    // didn't want it associated with workflow cancellation.
    using var cancelActivitySource = CancellationTokenSource.CreateLinkedTokenSource(
        Workflow.CancellationToken);

    // Start the activity. Whether this workflow waits on the activity to handle the cancellation
    // or not is dependent upon the CancellationType option. We leave the default here which sends
    // the cancellation but does not wait on it to be handled.
    var activityTask = Workflow.ExecuteActivityAsync(
        (MyActivities a) => a.MyNormalActivity(),
        new()
        {
            ScheduleToCloseTimeout = TimeSpan.FromMinutes(5),
            CancellationToken = cancelActivitySource.Token;
        });
    activityTask.Start();

    // Wait 5 minutes, then cancel it
    await Workflow.DelayAsync(TimeSpan.FromMinutes(5));
    cancelActivitySource.Cancel();

    // Wait on the activity which will throw cancellation which will fail the workflow
    await activityTask;
}
```

## Termination {/* #termination */}

To Terminate a Workflow Execution in .NET, use the
[TerminateAsync()](https://dotnet.temporal.io/api/Temporalio.Client.WorkflowHandle.html#Temporalio_Client_WorkflowHandle_TerminateAsync_System_String_Temporalio_Client_WorkflowTerminateOptions_)
method on the Workflow handle.

```csharp
// Get a workflow handle by its workflow ID. This could be made specific to a run by passing run ID.
// This could also just be a handle that is returned from StartWorkflowAsync instead.
var handle = myClient.GetWorkflowHandle("my-workflow-id");

// Terminate
await handle.TerminateAsync();
```

Workflow Executions can also be Terminated directly from the WebUI. In this case, a custom note can be logged from the
UI when that happens.

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

## Child Workflows - .NET SDK

This page shows how to do the following:

- [Start a Child Workflow Execution](#child-workflows)
- [Set a Parent Close Policy](#parent-close-policy)

## Start a Child Workflow Execution {/* #child-workflows */}

A [Child Workflow Execution](/child-workflows) is a Workflow Execution that is scheduled from within another Workflow using a Child Workflow API.

When using a Child Workflow API, Child Workflow related Events ([StartChildWorkflowExecutionInitiated](/references/events#startchildworkflowexecutioninitiated), [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted), [ChildWorkflowExecutionCompleted](/references/events#childworkflowexecutioncompleted), etc...) are logged in the Workflow Execution Event History.

The [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted) Event must be logged to the Event History before the Parent Workflow completes to ensure the Child Workflow has started.
In .NET, awaiting `StartChildWorkflowAsync()` or `ExecuteChildWorkflowAsync()` internally waits for this Event before returning, so the Child Workflow is guaranteed to have started once the call resolves.
If you start a Child Workflow from a non-main context (for example, a Signal or Update handler), make sure the Parent Workflow doesn't complete before that call resolves.

To spawn a Child Workflow Execution in .NET, use the `ExecuteChildWorkflowAsync()` method which starts the Child Workflow and waits for completion or
use the `StartChildWorkflowAsync()` method to start a Child Workflow and return its handle.
This is useful if you want to do something after it has only started, or to get the Workflow/Run ID, or to be able to signal it while running.

:::note

`ExecuteChildWorkflowAsync()` is a helper method for `StartChildWorkflowAsync()` plus `await handle.GetResultAsync()`.

:::

```csharp
await Workflow.ExecuteChildWorkflowAsync((MyChildWorkflow wf) => wf.RunAsync());
```

## Set a Parent Close Policy {/* #parent-close-policy */}

A [Parent Close Policy](/parent-close-policy) determines what happens to a Child Workflow Execution if its Parent changes to a Closed status (Completed, Failed, or Timed Out).

The default Parent Close Policy option is set to terminate the Child Workflow Execution.

Set the `ParentClosePolicy` property inside the [`ChildWorkflowOptions`](https://dotnet.temporal.io/api/Temporalio.Workflows.ChildWorkflowOptions.html) for `ExecuteChildWorkflowAsync` or `StartChildWorkflowAsync` to specify the behavior of the Child Workflow when the Parent Workflow closes.

```csharp
await Workflow.ExecuteChildWorkflowAsync(
  (MyChildWorkflow wf) => wf.RunAsync(),
  new() { ParentClosePolicy = ParentClosePolicy.Abandon });
```

---

## Continue-As-New - .NET SDK

This page answers the following questions for .NET developers:

- [What is Continue-As-New?](#what)
- [How to Continue-As-New?](#how)
- [When is it right to Continue-as-New?](#when)
- [How to test Continue-as-New?](#how-to-test)

## What is Continue-As-New? {/* #what */}

[Continue-As-New](/workflow-execution/continue-as-new) lets a Workflow Execution close successfully and creates a new Workflow Execution.
You can think of it as a checkpoint when your Workflow gets too long or approaches certain scaling limits.

The new Workflow Execution is in the same [chain](/workflow-execution#workflow-execution-chain); it keeps the same Workflow Id but gets a new Run Id and a fresh Event History.
It also receives your Workflow's usual parameters.

## How to Continue-As-New using the .NET SDK {/* #how */}

First, design your Workflow parameters so that you can pass in the "current state" when you Continue-As-New into the next Workflow run.
This state is typically set to `None` for the original caller of the Workflow.

    View the source code
  {' '}
  in the context of the rest of the application code.

```csharp
public record Input
    {
        public State State { get; init; } = new();

        public bool TestContinueAsNew { get; init; }
    }

[WorkflowInit]
public ClusterManagerWorkflow(Input input)

````
The test hook in the above snippet is covered [below](#how-to-test).

Inside your Workflow, throw a [`CreateContinueAsNewException`](https://dotnet.temporal.io/api/Temporalio.Workflows.ContinueAsNewException.html) exception.
This stops the Workflow right away and starts a new one.

    View the source code
  {' '}
  in the context of the rest of the application code.

```csharp
throw Workflow.CreateContinueAsNewException((ClusterManagerWorkflow wf) => wf.RunAsync(new()
{
    State = CurrentState,
    TestContinueAsNew = input.TestContinueAsNew,
}));
````

### Considerations for Workflows with Message Handlers {/* #with-message-handlers */}

If you use Updates or Signals, don't call Continue-as-New from the handlers.
Instead, wait for your handlers to finish in your main Workflow before you throw `CreateContinueAsNewException`.
See the [`AllHandlersFinished`](message-passing#wait-for-message-handlers) example for guidance.

## When is it right to Continue-as-New using the .NET SDK? {/* #when */}

Use Continue-as-New when your Workflow might hit [Event History Limits](/workflow-execution/event#event-history).

Temporal tracks your Workflow's progress against these limits to let you know when you should Continue-as-New.
Call `Workflow.ContinueAsNewSuggested` to check if it's time.

## How to test Continue-as-New using the .NET SDK {/* #how-to-test */}

Testing Workflows that naturally Continue-as-New may be time-consuming and resource-intensive.
Instead, add a test hook to check your Workflow's Continue-as-New behavior faster in automated tests.

For example, when `TestContinueAsNew == true`, this sample creates a test-only variable called `maxHistoryLength` and sets it to a small value.
A helper variable in the Workflow checks it each time it considers using Continue-as-New:

    View the source code
  {' '}
  in the context of the rest of the application code.

```csharp
private bool ShouldContinueAsNew =>
    // Don't continue as new while update running
    Workflow.AllHandlersFinished &&
    // Continue if suggested or, for ease of testing, max history reached
    (Workflow.ContinueAsNewSuggested || Workflow.CurrentHistoryLength > maxHistoryLength);
```

---

## Dynamic Workflow - .NET SDK

## Set a Dynamic Workflow {/* #set-a-dynamic-workflow */}

**How to set a Dynamic Workflow using the Temporal .NET SDK**

A Dynamic Workflow in Temporal is a Workflow that is invoked dynamically at runtime if no other Workflow with the same name is registered.
A Workflow can be made dynamic by setting `Dynamic` as `true` on the `[Workflow]` attribute.
You must register the Workflow with the Worker before it can be invoked.
Only one Dynamic Workflow can be present on a Worker.

The Workflow Definition must then accept a single argument of type `Temporalio.Converters.IRawValue[]`.
The [Workflow.PayloadConverter](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html#Temporalio_Workflows_Workflow_PayloadConverter) property is used to convert an `IRawValue` object to the desired type using extension methods in the `Temporalio.Converters` namespace.

```csharp
[Workflow(Dynamic = true)]
public class DynamicWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync(IRawValue[] args)
    {
        var name = Workflow.PayloadConverter.ToValue<string>(args.Single());
        var param = MyActivityParams("Hello", name);
        return await Workflow.ExecuteActivityAsync(
            (MyActivities a) => a.MyActivity(param),
            new() { StartToCloseTimeout = TimeSpan.FromMinutes(5) });
    }
}
```

---

## Workflows - .NET SDK

![.NET SDK Banner](/img/assets/banner-dotnet-temporal.png)

## Workflows

- [Workflow basics](/develop/dotnet/workflows/basics)
- [Child Workflows](/develop/dotnet/workflows/child-workflows)
- [Continue-As-New](/develop/dotnet/workflows/continue-as-new)
- [Cancellation](/develop/dotnet/workflows/cancellation)
- [Timeouts](/develop/dotnet/workflows/timeouts)
- [Message passing](/develop/dotnet/workflows/message-passing)
- [Schedules](/develop/dotnet/workflows/schedules)
- [Timers](/develop/dotnet/workflows/timers)
- [Dynamic Workflow](/develop/dotnet/workflows/dynamic-workflow)
- [Versioning](/develop/dotnet/workflows/versioning)

---

## Message passing - .NET SDK

A Workflow can act like a stateful web service that receives messages: Queries, Signals, and Updates.
The Workflow implementation defines these endpoints via handler methods that can react to incoming messages and return values.
Temporal Clients use messages to read Workflow state and control execution.
See [Workflow message passing](/encyclopedia/workflow-message-passing) for a general overview of this topic.
This page introduces these features for the Temporal .NET SDK.

## Write message handlers {/* #writing-message-handlers */}

:::info
The code that follows is part of a [working solution](https://github.com/temporalio/samples-dotnet/tree/main/src/MessagePassing).
:::

Follow these guidelines when writing your message handlers:

- Message handlers are defined as methods on the Workflow class, using one of the three attributes: [`WorkflowQueryAttribute`](https://dotnet.temporal.io/api/Temporalio.Workflows.WorkflowQueryAttribute.html), [`WorkflowSignalAttribute`](https://dotnet.temporal.io/api/Temporalio.Workflows.WorkflowSignalAttribute.html), and [`WorkflowUpdateAttribute`](https://dotnet.temporal.io/api/Temporalio.Workflows.WorkflowUpdateAttribute.html).
- The parameters and return values of handlers and the main Workflow function must be [serializable](/dataconversion).
- Prefer data classes to multiple input parameters. Data class parameters allow you to add fields without changing the calling signature. Keep in mind that serialization and deserialization can fail with the default data converter if the new field does not have a default value.

### Query handlers {/* #queries */}

A [Query](/sending-messages#sending-queries) is a synchronous operation that retrieves state from a Workflow Execution.
Define as a method:

```csharp
[Workflow]
public class GreetingWorkflow
{
    public enum Language
    {
        Chinese,
        English,
        French,
        Spanish,
        Portuguese,
    }

    public record GetLanguagesInput(bool IncludeUnsupported);

    // ...

    [WorkflowQuery]
    public IList<Language> GetLanguages(GetLanguagesInput input) =>
        Enum.GetValues<Language>().
            Where(language => input.IncludeUnsupported || Greetings.ContainsKey(language)).
            ToList();

    // ...
```

Or as a property getter:

```csharp
[Workflow]
public class GreetingWorkflow
{
    public enum Language
    {
        Chinese,
        English,
        French,
        Spanish,
        Portuguese,
    }

    // ...

    [WorkflowQuery]
    public Language CurrentLanguage { get; private set; } = Language.English;

    // ...
```

- The Query attribute can accept arguments.
  See the API reference docs: [`WorkflowQueryAttribute`](https://dotnet.temporal.io/api/Temporalio.Workflows.WorkflowQueryAttribute.html).
- A Query handler must not modify Workflow state.
- You can't perform async blocking operations such as executing an Activity in a Query handler.

### Signal handlers {/* #signals */}

A [Signal](/sending-messages#sending-signals) is an asynchronous message sent to a running Workflow Execution to change its state and control its flow:

```csharp
[Workflow]
public class GreetingWorkflow
{
    public record ApproveInput(string Name);

    // ...

    [WorkflowSignal]
    public async Task ApproveAsync(ApproveInput input)
    {
        approvedForRelease = true;
        approverName = input.Name;
    }

    // ...
```

- The Signal attribute can accept arguments.
  Refer to the API docs: [`WorkflowSignalAttribute`](https://dotnet.temporal.io/api/Temporalio.Workflows.WorkflowSignalAttribute.html).

- The handler should not return a value.
  The response is sent immediately from the server, without waiting for the Workflow to process the Signal.

- Signal (and Update) handlers can be asynchronous and blocking.
  This allows you to use Activities, Child Workflows, durable [`Workflow.DelayAsync`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html?#Temporalio_Workflows_Workflow_DelayAsync_System_Int32_System_Nullable_System_Threading_CancellationToken__) Timers, [`Workflow.WaitConditionAsync`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html?#Temporalio_Workflows_Workflow_WaitConditionAsync_System_Func_System_Boolean__System_Int32_System_Nullable_System_Threading_CancellationToken__) conditions, and more.
  See [Async handlers](#async-handlers) and [Workflow message passing](/encyclopedia/workflow-message-passing) for guidelines on safely using async Signal and Update handlers.

### Update handlers and validators {/* #updates */}

An [Update](/sending-messages#sending-updates) is a trackable synchronous request sent to a running Workflow Execution.
It can change the Workflow state, control its flow, and return a result.
The sender must wait until the Worker accepts or rejects the Update.
The sender may wait further to receive a returned value or an exception if something goes wrong:

```csharp
[Workflow]
public class GreetingWorkflow
{
    public enum Language
    {
        Chinese,
        English,
        French,
        Spanish,
        Portuguese,
    }

    // ...

    [WorkflowUpdateValidator(nameof(SetCurrentLanguageAsync))]
    public void ValidateLanguage(Language language)
    {
        if (!Greetings.ContainsKey(language))
        {
            throw new ApplicationFailureException($"{language} is not supported");
        }
    }

    [WorkflowUpdate]
    public async Task<Language> SetCurrentLanguageAsync(Language language)
    {
        var previousLanguage = CurrentLanguage;
        CurrentLanguage = language;
        return previousLanguage;
    }

    // ...
```

- The Update attribute can take arguments (like, `Name`, `Dynamic` and `UnfinishedPolicy`) as described in the API reference docs for [`WorkflowUpdateAttribute`](https://dotnet.temporal.io/api/Temporalio.Workflows.WorkflowUpdateAttribute.html).

- About validators:
  - Use validators to reject an Update before it is written to History.
    Validators are always optional.
    If you don't need to reject Updates, you can skip them.
  - Define an Update validator with the [`WorkflowUpdateValidatorAttribute`](https://dotnet.temporal.io/api/Temporalio.Workflows.WorkflowUpdateValidatorAttribute.html) attribute.
    Use the Name argument when declaring the validator to connect it to its Update.
    The validator must be a `void` type and accept the same argument types as the handler.

- Accepting and rejecting Updates with validators:
  - To reject an Update, raise an exception of any type in the validator.
  - Without a validator, Updates are always accepted.
- Validators and Event History:
  - The `WorkflowExecutionUpdateAccepted` event is written into the History whether the acceptance was automatic or programmatic.
  - When a Validator raises an error, the Update is rejected, the Update is not run, and `WorkflowExecutionUpdateAccepted` _won't_ be added to the Event History.
    The caller receives an "Update failed" error.
