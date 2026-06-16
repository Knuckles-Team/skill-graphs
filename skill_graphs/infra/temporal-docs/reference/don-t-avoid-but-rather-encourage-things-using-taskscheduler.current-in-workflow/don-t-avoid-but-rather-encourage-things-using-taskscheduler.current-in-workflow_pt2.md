
- Use [`Workflow.CurrentUpdateInfo`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html#Temporalio_Workflows_Workflow_CurrentUpdateInfo) to obtain information about the current Update.
  This includes the Update ID, which can be useful for deduplication when using Continue-As-New: see [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing).
- Update (and Signal) handlers can be asynchronous and blocking.
  This allows you to use Activities, Child Workflows, durable [`Workflow.DelayAsync`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html?#Temporalio_Workflows_Workflow_DelayAsync_System_Int32_System_Nullable_System_Threading_CancellationToken__) Timers, [`Workflow.WaitConditionAsync`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html?#Temporalio_Workflows_Workflow_WaitConditionAsync_System_Func_System_Boolean__System_Int32_System_Nullable_System_Threading_CancellationToken__) conditions, and more.
  See [Async handlers](#async-handlers) and [Workflow message passing](/encyclopedia/workflow-message-passing) for guidelines on safely using async Update and Signal handlers.

## Send messages {/* #send-messages */}

To send Queries, Signals, or Updates you call methods on a [`WorkflowHandle`](https://dotnet.temporal.io/api/Temporalio.Client.WorkflowHandle.html) object.
To obtain the WorkflowStub, you can:

- Use [`TemporalClient.StartWorkflowAsync`](https://dotnet.temporal.io/api/Temporalio.Client.TemporalClient.html#Temporalio_Client_TemporalClient_StartWorkflowAsync_System_String_System_Collections_Generic_IReadOnlyCollection_System_Object__Temporalio_Client_WorkflowOptions_) to start a Workflow and return its handle.
- Use the [`TemporalClient.GetWorkflowHandle`](https://dotnet.temporal.io/api/Temporalio.Client.TemporalClient.html#Temporalio_Client_TemporalClient_GetWorkflowHandle_System_String_System_String_System_String_) method to retrieve a Workflow handle by its Workflow Id.

For example:

```csharp
var client = await TemporalClient.ConnectAsync(new("localhost:7233"));
var workflowHandle = await client.StartWorkflowAsync(
    (GreetingWorkflow wf) => wf.RunAsync(),
    new(id: "message-passing-workflow-id", taskQueue: "message-passing-sample"));
```

To check the argument types required when sending messages -- and the return type for Queries and Updates -- refer to the corresponding handler method in the Workflow Definition.

:::warning Using Continue-as-New and Updates

- Temporal _does not_ support Continue-as-New functionality within Update handlers.
- Complete all handlers _before_ using Continue-as-New.
- Use Continue-as-New from your main Workflow Definition method, just as you would complete or fail a Workflow Execution.

:::

### Send a Query {/* #send-query */}

Call a Query method with [`WorkflowHandle.QueryAsync`](https://dotnet.temporal.io/api/Temporalio.Client.WorkflowHandle.html#Temporalio_Client_WorkflowHandle_QueryAsync__1_System_String_System_Collections_Generic_IReadOnlyCollection_System_Object__Temporalio_Client_WorkflowQueryOptions_):

```csharp
var supportedLanguages = await workflowHandle.QueryAsync(wf => wf.GetLanguages(new(false)));
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

Use [`WorkflowHandle.SignalAsync`](https://dotnet.temporal.io/api/Temporalio.Client.WorkflowHandle.html#Temporalio_Client_WorkflowHandle_SignalAsync_System_String_System_Collections_Generic_IReadOnlyCollection_System_Object__Temporalio_Client_WorkflowSignalOptions_) from Client code to send a Signal:

```csharp
await workflowHandle.SignalAsync(wf => wf.ApproveAsync(new("MyUser")));
```

- The call returns when the server accepts the Signal; it does _not_ wait for the Signal to be delivered to the Workflow Execution.

- The [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the Workflow's Event History.

#### Send a Signal from a Workflow {/* #send-signal-from-workflow */}

A Workflow can send a Signal to another Workflow, known as an _External Signal_.
In this case you need to obtain a Workflow handle for the external Workflow.
Use `Workflow.GetExternalWorkflowHandle`, passing a running Workflow Id, to retrieve a typed Workflow handle:

```csharp
// ...

[Workflow]
public class WorkflowB
{
    [WorkflowRun]
    public async Task RunAsync()
    {
        var handle = Workflow.GetExternalWorkflowHandle<WorkflowA>("workflow-a");
        await handle.SignalAsync(wf => wf.YourSignalAsync("signal argument"));
    }

    // ...
```

When an External Signal is sent:

- A [SignalExternalWorkflowExecutionInitiated](/references/events#signalexternalworkflowexecutioninitiated) Event appears in the sender's Event History.
- A [WorkflowExecutionSignaled](/references/events#workflowexecutionsignaled) Event appears in the recipient's Event History.

#### Signal-With-Start {/* #signal-with-start */}

Signal-With-Start allows a Client to send a Signal to a Workflow Execution, starting the Execution if it is not already running.
If there's a Workflow running with the given Workflow Id, it will be signaled.
If there isn't, a new Workflow will be started and immediately signaled.
To use Signal-With-Start, call `SignalWithStart` with a lambda expression invoking it:

```csharp
var client = await TemporalClient.ConnectAsync(new("localhost:7233"));
var options = new WorkflowOptions(id: "your-signal-with-start-workflow", taskQueue: "signal-tq");
options.SignalWithStart((GreetingWorkflow wf) => wf.SubmitGreetingAsync("User Signal with Start"));
await client.StartWorkflowAsync((GreetingWorkflow wf) => wf.RunAsync(), options);
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

- Call the Update method with `ExecuteUpdateAsync` from the Client and wait for the Update to complete.
  This code fetches an Update result:

  ```csharp
  var previousLanguage = await workflowHandle.ExecuteUpdateAsync(
    wf => wf.SetCurrentLanguageAsync(GreetingWorkflow.Language.Chinese));
  ```

2. Use `StartUpdateAsync` to receive a handle as soon as the Update is accepted.
     It returns an `UpdateHandle`

  - Use this `UpdateHandle` later to fetch your results.
  - Asynchronous Update handlers normally perform long-running async Activities.
  - `StartUpdateAsync` only waits until the Worker has accepted or rejected the Update, not until all asynchronous operations are complete.

  For example:

  ```csharp
  // Wait until the update is accepted
  var updateHandle = await workflowHandle.StartUpdateAsync(
      wf => wf.SetGreetingAsync(new HelloWorldInput("World")),
      new(waitForStage: WorkflowUpdateStage.Accepted));
  // Wait until the update is completed
  var updateResult = await updateHandle.GetResultAsync();
  ```

  For more details, see the "Async handlers" section.

#### Update-with-Start {/* #update-with-start */}

:::tip

For open source server users, Temporal Server version [Temporal Server version 1.28](https://github.com/temporalio/temporal/releases/tag/v1.28.0) is recommended.

:::

[Update-with-Start](/sending-messages#update-with-start) lets you [send an Update](/develop/dotnet/workflows/message-passing#send-update-from-client) that checks whether an already-running Workflow with that ID exists:

- If the Workflow exists, the Update is processed.
- If the Workflow does not exist, a new Workflow Execution is started with the given ID, and the Update is processed before the main Workflow method starts to execute.

Use `ExecuteUpdateWithStartAsync` to start the Update and wait for the result in one go.

Alternatively, use `StartUpdateWithStartAsync` to start the Update and receive a `WorkflowUpdateHandle`, and then use `await updateHandle.GetResultAsync()` to retrieve the result from the Update.

These calls return once the requested Update wait stage has been reached, or when the request times out.

- You will need to provide a `WithStartWorkflowOperation` to define the Workflow that will be started if necessary, and its arguments.
- You must specify an [IdConflictPolicy](/workflow-execution/workflowid-runid#workflow-id-conflict-policy) when creating the `WithStartWorkflowOperation`.
  Note that a `WithStartWorkflowOperation` can only be used once.

Here's an example taken from the [UpdateWithStartLazyInit](https://github.com/temporalio/samples-dotnet/blob/main/src/UpdateWithStartLazyInit/Program.cs) sample:

```csharp
async Task<AddCartItemResult> AddCartItemAsync(string sessionId, ShoppingCartItem item)
{
    // Issue an update-with-start that will create the workflow if it does not
    // exist before attempting the update

    // Create the start operation
    var startOperation = WithStartWorkflowOperation.Create(
        (ShoppingCartWorkflow wf) => wf.RunAsync(),
        new(id: $"cart-{sessionId}", taskQueue: TaskQueue)
        {
            IdConflictPolicy = Temporalio.Api.Enums.V1.WorkflowIdConflictPolicy.UseExisting,
        });

    // Issue the update-with-start, swallowing item-unavailable failure
    decimal? subtotal;
    try
    {
        subtotal = await client.ExecuteUpdateWithStartWorkflowAsync(
            (ShoppingCartWorkflow wf) => wf.AddItemAsync(item),
            new(startOperation));
    }
    catch (WorkflowUpdateFailedException e) when (
        e.InnerException is ApplicationFailureException appErr && appErr.ErrorType == "ItemUnavailable")
    {
        // Set subtotal to null if item was not found
        subtotal = null;
    }

    return new(await startOperation.GetHandleAsync(), subtotal);
}
```

:::info NON-TYPE SAFE API CALLS

In real-world development, sometimes you may be unable to import Workflow Definition method signatures.
When you don't have access to the Workflow Definition or it isn't written in .NET, you can still use non-type safe APIs and dynamic method invocation.
Pass method names instead of method objects to:

- [`TemporalClient.StartWorkflowAsync`](https://dotnet.temporal.io/api/Temporalio.Client.TemporalClient.html#Temporalio_Client_TemporalClient_StartWorkflowAsync_System_String_System_Collections_Generic_IReadOnlyCollection_System_Object__Temporalio_Client_WorkflowOptions_)
- [`WorkflowHandle.QueryAsync`](https://dotnet.temporal.io/api/Temporalio.Client.WorkflowHandle.html#Temporalio_Client_WorkflowHandle_QueryAsync__1_System_String_System_Collections_Generic_IReadOnlyCollection_System_Object__Temporalio_Client_WorkflowQueryOptions_)
- [`WorkflowHandle.SignalAsync`](https://dotnet.temporal.io/api/Temporalio.Client.WorkflowHandle.html#Temporalio_Client_WorkflowHandle_SignalAsync_System_String_System_Collections_Generic_IReadOnlyCollection_System_Object__Temporalio_Client_WorkflowSignalOptions_)
- [`WorkflowHandle.ExecuteUpdateAsync`](https://dotnet.temporal.io/api/Temporalio.Client.WorkflowHandle.html#Temporalio_Client_WorkflowHandle_ExecuteUpdateAsync_System_String_System_Collections_Generic_IReadOnlyCollection_System_Object__Temporalio_Client_WorkflowUpdateOptions_)
- [`WorkflowHandle.StartUpdateAsync`](https://dotnet.temporal.io/api/Temporalio.Client.WorkflowHandle.html#Temporalio_Client_WorkflowHandle_StartUpdateAsync_System_String_System_Collections_Generic_IReadOnlyCollection_System_Object__Temporalio_Client_WorkflowUpdateStartOptions_)

Use non-type safe overloads of these APIs:

- [`TemporalClient.GetWorkflowHandle`](https://dotnet.temporal.io/api/Temporalio.Client.TemporalClient.html#Temporalio_Client_TemporalClient_GetWorkflowHandle_System_String_System_String_System_String_)
- [`Workflow.GetExternalWorkflowHandle`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html#Temporalio_Workflows_Workflow_GetExternalWorkflowHandle_System_String_System_String_)

:::

## Message handler patterns {/* #message-handler-patterns */}

This section covers common write operations, such as Signal and Update handlers.
It doesn't apply to pure read operations, like Queries or Update Validators.

:::tip

For additional information, see [Inject work into the main Workflow](/handling-messages#injecting-work-into-main-workflow) and [Ensuring your messages are processed exactly once](/handling-messages#exactly-once-message-processing).

:::

### Add async handlers to use `await` {/* #async-handlers */}

Signal and Update handlers can be asynchronous as well as blocking.
Using asynchronous calls allows you to `await` Activities, Child Workflows, [`Workflow.DelayAsync`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html?#Temporalio_Workflows_Workflow_DelayAsync_System_Int32_System_Nullable_System_Threading_CancellationToken__) Timers, [`Workflow.WaitConditionAsync`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html?#Temporalio_Workflows_Workflow_WaitConditionAsync_System_Func_System_Boolean__System_Int32_System_Nullable_System_Threading_CancellationToken__) wait conditions, etc.
This expands the possibilities for what can be done by a handler but it also means that handler executions and your main Workflow method are all running concurrently, with switching occurring between them at await calls.

It's essential to understand the things that could go wrong in order to use asynchronous handlers safely.
See [Workflow message passing](/encyclopedia/workflow-message-passing) for guidance on safe usage of async Signal and Update handlers, and the [Controlling handler concurrency](#control-handler-concurrency) and [Waiting for message handlers to finish](#wait-for-message-handlers) sections below.

The following code executes an Activity that simulates a network call to a remote service:

```csharp
public class MyActivities
{
    private static readonly Dictionary<Language, string> Greetings = new()
    {
        [Language.Arabic] = "مرحبا بالعالم",
        [Language.Chinese] = "你好，世界",
        [Language.English] = "Hello, world",
        [Language.French] = "Bonjour, monde",
        [Language.Hindi] = "नमस्ते दुनिया",
        [Language.Spanish] = "Hola mundo",
    };

    [Activity]
    public async Task<string?> CallGreetingServiceAsync(Language language)
    {
        // Pretend that we are calling a remove service
        await Task.Delay(200);
        return Greetings.TryGetValue(language, out var value) ? value : null;
    }
}
```

The following code modifies a `WorkflowUpdate` for asynchronous use of the preceding Activity:

```csharp
[Workflow]
public class GreetingWorkflow
{
    private readonly Mutex mutex = new();

    // ...

    [WorkflowUpdate]
    public async Task<Language> SetLanguageAsync(Language language)
    {
        // 👉 Use a mutex here to ensure that multiple calls to SetLanguageAsync are processed in order.
        await mutex.WaitOneAsync();
        try
        {
            if (!greetings.ContainsKey(language))
            {
                var greeting = Workflow.ExecuteActivityAsync(
                    (MyActivities acts) => acts.CallGreetingServiceAsync(language),
                    new() { StartToCloseTimeout = TimeSpan.FromSeconds(10) });
                if (greeting == null)
                {
                    // 👉 An update validator cannot be async, so cannot be used to check that the remote
                    // CallGreetingServiceAsync supports the requested language. Throwing ApplicationFailureException
                    // will fail the Update, but the WorkflowExecutionUpdateAccepted event will still be
                    // added to history.
                    throw new ApplicationFailureException(
                        $"Greeting service does not support {language}");
                }
                greetings[language] = greeting;
            }
            var previousLanguage = CurrentLanguage;
            CurrentLanguage = language;
            return previousLanguage;
        }
        finally
        {
            mutex.ReleaseMutex();
        }
    }
}
```

After updating the code for asynchronous calls, your Update handler can schedule an Activity and await the result.
Although an async Signal handler can initiate similar network tasks, using an Update handler allows the Client to receive a result or error once the Activity completes.
This lets your Client track the progress of asynchronous work performed by the Update's Activities, Child Workflows, etc.

### Add wait conditions to block {/* #block-with-wait */}

Sometimes, async Signal or Update handlers need to meet certain conditions before they should continue.
Using a wait condition with [`Workflow.WaitConditionAsync`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html?#Temporalio_Workflows_Workflow_WaitConditionAsync_System_Func_System_Boolean__System_Int32_System_Nullable_System_Threading_CancellationToken__) sets a function that prevents the code from proceeding until the condition returns `true`.
This is an important feature that helps you control your handler logic.

Here are two important use cases for `Workflow.WaitConditionAsync`:

- Waiting in a handler until it is appropriate to continue.
- Waiting in the main Workflow until all active handlers have finished.

The condition state you're waiting for can be updated by and reflect any part of the Workflow code.
This includes the main Workflow method, other handlers, or child coroutines spawned by the main Workflow method, and so forth.

#### Use wait conditions in handlers {/* #wait-in-handlers */}

Sometimes, async Signal or Update handlers need to meet certain conditions before they should continue.
Using a wait condition with [`Workflow.WaitConditionAsync`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html?#Temporalio_Workflows_Workflow_WaitConditionAsync_System_Func_System_Boolean__System_Int32_System_Nullable_System_Threading_CancellationToken__) sets a function that prevents the code from proceeding until the condition returns `true`.
This is an important feature that helps you control your handler logic.

Consider a `ReadyForUpdateToExecute` method that runs before your Update handler executes.
The [`Workflow.WaitConditionAsync`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.html?#Temporalio_Workflows_Workflow_WaitConditionAsync_System_Func_System_Boolean__System_Int32_System_Nullable_System_Threading_CancellationToken__) call waits until your condition is met:

```csharp
[WorkflowUpdate]
public async Task<string> MyUpdateAsync(UpdateInput updateInput)
{
    await Workflow.WaitConditionAsync(() => ReadyForUpdateToExecute(updateInput));
    // ...
}
```

Remember: Handlers can execute before the main Workflow method starts.

#### Ensure your handlers finish before the Workflow completes {/* #wait-for-message-handlers */}

Workflow wait conditions can ensure your handler completes before a Workflow finishes.
When your Workflow uses async Signal or Update handlers, your main Workflow method can return or continue-as-new while a handler is still waiting on an async task, such as an Activity result.
The Workflow completing may interrupt the handler before it finishes crucial work and cause Client errors when trying retrieve Update results.
Use `Workflow.AllHandlersFinished` to address this problem and allow your Workflow to end smoothly:

```csharp
[Workflow]
public class MyWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync()
    {
        // ...
        await Workflow.WaitConditionAsync(() => Workflow.AllHandlersFinished);
        return "workflow-result";
    }

    // ...
```

By default, your Worker will log a warning when you allow a Workflow Execution to finish with unfinished handler executions.
You can silence these warnings on a per-handler basis by passing the `UnfinishedPolicy` argument to the [`WorkflowSignalAttribute`](https://dotnet.temporal.io/api/Temporalio.Workflows.WorkflowSignalAttribute.html) / [`WorkflowUpdateAttribute`](https://dotnet.temporal.io/api/Temporalio.Workflows.WorkflowUpdateAttribute.html) decorator:

```csharp
[WorkflowUpdate(UnfinishedPolicy = HandlerUnfinishedPolicy.Abandon)]
public async Task MyUpdateAsync()
{
    // ...
```

See [Finishing handlers before the Workflow completes](/handling-messages#finishing-message-handlers) for more information.

### Use `[WorkflowInit]` to operate on Workflow input before any handler executes

The `[WorkflowInit]` attribute gives message handlers access to [Workflow input](/handling-messages#workflow-initializers).
When you use the `[WorkflowInit]` attribute on your constructor, you give the constructor the same Workflow parameters as your `[WorkflowRun]` method.
The SDK will then ensure that your constructor receives the Workflow input arguments that the [Client sent](/develop/dotnet/client/temporal-client#start-workflow).
The Workflow input arguments are also passed to your `[WorkflowRun]` method -- that always happens, whether or not you use the `[WorkflowInit]` attribute.

Here's an example.
The constructor and `RunAsync` must have the same parameters with the same types:

```csharp
[Workflow]
public class WorkflowInitWorkflow
{
    public record Input(string Name);

    private readonly string nameWithTitle;
    private bool titleHasBeenChecked;

    [WorkflowInit]
    public WorkflowInitWorkflow(Input input) =>
        nameWithTitle = $"Sir {input.Name}";

    [WorkflowRun]
    public async Task<string> RunAsync(Input ignored)
    {
        await Workflow.WaitConditionAsync(() => titleHasBeenChecked);
        return $"Hello, {nameWithTitle}";
    }

    [WorkflowUpdate]
    public async Task<bool> CheckTitleValidityAsync()
    {
        // The handler is now guaranteed to see the workflow input after it has
        // been processed by the constructor.
        var valid = await Workflow.ExecuteActivityAsync(
            (MyActivities acts) -> acts.CheckTitleValidityAsync(nameWithTitle),
            new() { StartToCloseTimeout = TimeSpan.FromSeconds(10) });
        titleHasBeenChecked = true;
        return valid;
    }
}
```

### Use locks to prevent concurrent handler execution {/* #control-handler-concurrency */}

Concurrent processes can interact in unpredictable ways.
Incorrectly written [concurrent message-passing](/handling-messages#message-handler-concurrency) code may not work correctly when multiple handler instances run simultaneously.
Here's an example of a pathological case:

```csharp
[Workflow]
public class MyWorkflow
{
    // ...

    [WorkflowSignal]
    public async Task BadHandlerAsync()
    {
        var data = await Workflow.ExecuteActivityAsync(
            (MyActivities acts) => acts.FetchDataAsync(),
            new() { StartToCloseTimeout = TimeSpan.FromSeconds(10) });
        this.x = data.X;
        // 🐛🐛 Bug!! If multiple instances of this handler are executing concurrently, then
        // there may be times when the Workflow has this.x from one Activity execution and this.y from another.
        await Workflow.DelayAsync(1000);
        this.y = data.Y;
    }
}
```

Coordinating access with [`Workflows.Mutex`](https://dotnet.temporal.io/api/Temporalio.Workflows.Mutex.html), a mutual exclusion lock, corrects this code.
Locking makes sure that only one handler instance can execute a specific section of code at any given time:

```csharp
[Workflow]
public class MyWorkflow
{
    private readonly Mutex mutex = new();

    // ...

    [WorkflowSignal]
    public async Task SafeHandlerAsync()
    {
        await mutex.WaitOneAsync();
        try
        {
            var data = await Workflow.ExecuteActivityAsync(
                (MyActivities acts) => acts.FetchDataAsync(),
                new() { StartToCloseTimeout = TimeSpan.FromSeconds(10) });
            this.x = data.X;
            // ✅ OK: the scheduler may switch now to a different handler execution, or to the main workflow
            // method, but no other execution of this handler can run until this execution finishes.
            await Workflow.DelayAsync(1000);
            this.y = data.Y;
        }
        finally
        {
            mutex.ReleaseMutex();
        }
    }
}
```

For additional concurrency options, you can use [`Workflows.Semaphore`](https://dotnet.temporal.io/api/Temporalio.Workflows.Semaphore.html).
Semaphores manage access to shared resources and coordinate the order in which threads or processes execute.
