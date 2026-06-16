    }
    catch (OperationCanceledException)
    {
        logger.LogInformation("Handler worker cancelled");
    }
}
```

## Develop a caller Workflow that uses the Nexus Service {/* #develop-caller-workflow-nexus-service */}

Import the Service API package that has the necessary service and operation names and input/output types to execute a Nexus Operation from the caller Workflow:

[NexusSimple/Caller/EchoCallerWorkflow.workflow.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/NexusSimple/Caller/EchoCallerWorkflow.workflow.cs)
```csharp
using Temporalio.Workflows;

[Workflow]
public class EchoCallerWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync(string message)
    {
        var output = await Workflow.CreateNexusWorkflowClient<IHelloService>(IHelloService.EndpointName).
            ExecuteNexusOperationAsync(svc => svc.Echo(new(message)));
        return output.Message;
    }
}
```

[NexusSimple/Caller/HelloCallerWorkflow.workflow.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/NexusSimple/Caller/HelloCallerWorkflow.workflow.cs)
```csharp
using Temporalio.Workflows;

[Workflow]
public class HelloCallerWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync(string name, IHelloService.HelloLanguage language)
    {
        var output = await Workflow.CreateNexusWorkflowClient<IHelloService>(IHelloService.EndpointName).
            ExecuteNexusOperationAsync(svc => svc.SayHello(new(name, language)));
        return output.Message;
    }
}
```

### Set Nexus Operation timeouts

Nexus Operations support [three types of timeouts](/nexus/operations#timeouts) that control how long the caller is willing to wait at different stages of the Operation lifecycle.
Set these timeouts in `NexusWorkflowOperationOptions` when calling `ExecuteNexusOperationAsync`.

#### Schedule-to-Close timeout

The [Schedule-to-Close timeout](/nexus/operations#schedule-to-close-timeout) limits the total duration of the Operation from when it is scheduled to when it completes.
The Nexus Machinery automatically retries failed requests until this timeout is exceeded.

```csharp
var output = await Workflow.CreateNexusWorkflowClient<IHelloService>(IHelloService.EndpointName).
    ExecuteNexusOperationAsync(svc => svc.SayHello(new(name, language)), new NexusWorkflowOperationOptions
    {
        ScheduleToCloseTimeout = TimeSpan.FromMinutes(10),
    });
```

#### Schedule-to-Start timeout

The [Schedule-to-Start timeout](/nexus/operations#schedule-to-start-timeout) limits how long the caller will wait for the Operation to be started by the handler.
If not set, no Schedule-to-Start timeout is enforced.

```csharp
var output = await Workflow.CreateNexusWorkflowClient<IHelloService>(IHelloService.EndpointName).
    ExecuteNexusOperationAsync(svc => svc.SayHello(new(name, language)), new NexusWorkflowOperationOptions
    {
        ScheduleToStartTimeout = TimeSpan.FromMinutes(2),
    });
```

#### Start-to-Close timeout

The [Start-to-Close timeout](/nexus/operations#start-to-close-timeout) limits how long the caller will wait for an asynchronous Operation to complete after it has been started.
This timeout only applies to asynchronous Operations.
If not set, no Start-to-Close timeout is enforced.

```csharp
var output = await Workflow.CreateNexusWorkflowClient<IHelloService>(IHelloService.EndpointName).
    ExecuteNexusOperationAsync(svc => svc.SayHello(new(name, language)), new NexusWorkflowOperationOptions
    {
        StartToCloseTimeout = TimeSpan.FromMinutes(5),
    });
```

### Register the caller Workflow in a Worker

After developing the caller Workflow, the next step is to register it with a Worker.

[NexusSimple/Program.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/NexusSimple/Program.cs)
```csharp
async Task RunCallerWorkerAsync()
{
    // Run worker until cancelled
    logger.LogInformation("Running caller worker");
    using var worker = new TemporalWorker(
        await ConnectClientAsync("nexus-simple-caller-namespace"),
        new TemporalWorkerOptions(taskQueue: "nexus-simple-caller-sample").
            AddWorkflow<EchoCallerWorkflow>().
            AddWorkflow<HelloCallerWorkflow>());
    try
    {
        await worker.ExecuteAsync(tokenSource.Token);
    }
    catch (OperationCanceledException)
    {
        logger.LogInformation("Caller worker cancelled");
    }
}
```

### Develop a starter to start the caller Workflow

To initiate the caller Workflow, a starter program is used.

[NexusSimple/Program.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/NexusSimple/Program.cs)
```csharp
async Task ExecuteCallerWorkflowAsync()
{
    logger.LogInformation("Executing caller echo workflow");
    var client = await ConnectClientAsync("nexus-simple-caller-namespace");
    var result1 = await client.ExecuteWorkflowAsync(
        (EchoCallerWorkflow wf) => wf.RunAsync("Nexus Echo 👋"),
        new(id: "nexus-simple-echo-id", taskQueue: "nexus-simple-caller-sample"));
    logger.LogInformation("Workflow result: {Result}", result1);

    logger.LogInformation("Executing caller hello workflow");
    var result2 = await client.ExecuteWorkflowAsync(
        (HelloCallerWorkflow wf) => wf.RunAsync("Temporal", IHelloService.HelloLanguage.Es),
        new(id: "nexus-simple-hello-id", taskQueue: "nexus-simple-caller-sample"));
    logger.LogInformation("Workflow result: {Result}", result2);
}
```

## Make Nexus calls across Namespaces with a development Server {/* #nexus-calls-across-namespaces-dev-server */}

Follow the steps below to run the Nexus handler Worker, the Nexus caller Worker, and the starter app.

### Run Workers connected to a local development server

Run the Nexus handler Worker:

```bash
dotnet run handler-worker
```

In another terminal window, run the Nexus caller Worker:

```bash
dotnet run caller-worker
```

### Start a caller Workflow

With the Workers running, the final step in the local development process is to start a caller Workflow.

Run the starter:

```bash
dotnet run caller-workflow
```

This will show the two workflows started and their results.

### Canceling a Nexus Operation {/* #canceling-a-nexus-operation */}

To cancel a Nexus Operation from within a Workflow, cancel the cancellation token passed to the operation call. Only asynchronous operations can be canceled in Nexus, since cancellation is sent using an operation token.
The Workflow or other resources backing the operation may choose to ignore the cancellation request.
If ignored, the operation may enter a terminal state.

When a Nexus operation is started, the caller can specify different cancellation types that control how the caller reacts to cancellation:

- `Abandon` - Do not request cancellation of the operation.
- `TryCancel` - Initiate a cancellation request and immediately report cancellation to the caller. Note that this type doesn't guarantee that cancellation is delivered to the operation handler if the caller exits before the delivery is done.
- `WaitCancellationRequested` - Request cancellation of the operation and wait for confirmation that the request was received. Doesn't wait for actual cancellation.
- `WaitCancellationCompleted` - Wait for operation completion. Operation may or may not complete as cancelled.

The default is `WaitCancellationCompleted`. Users can set a different option for `CancellationType` in `NexusWorkflowOperationOptions` when starting an operation.

Once the caller Workflow completes, the caller's Nexus Machinery will not make any further attempts to cancel operations that are still running.
It's okay to leave operations running in some use cases.
To ensure cancellations are delivered, wait for all pending operations to finish before exiting the Workflow.

See the [Nexus cancellation sample](https://github.com/temporalio/samples-dotnet/tree/main/src/NexusCancellation) for reference.

## Make Nexus calls across Namespaces in Temporal Cloud {/* #nexus-calls-across-namespaces-temporal-cloud */}

This section assumes you are already familiar with how to connect a Worker to Temporal Cloud.
The `tcld` CLI is used to create Namespaces and the Nexus Endpoint, and mTLS client certificates will be used to securely connect the caller and handler Workers to their respective Temporal Cloud Namespaces.

### Install the latest `tcld` CLI and generate certificates

To install the latest version of the `tcld` CLI, run the following command (on MacOS):

```
brew install temporalio/brew/tcld
```

If you don't already have certificates, you can generate them for mTLS Worker authentication using the command below:

```
tcld gen ca --org $YOUR_ORG_NAME --validity-period 1y --ca-cert ca.pem --ca-key ca.key
```

These certificates will be valid for one year.

### Create caller and handler Namespaces

Before deploying to Temporal Cloud, ensure that the appropriate Namespaces are created for both the caller and handler.
If you already have these Namespaces, you don't need to do this.

```
tcld login

tcld namespace create \
  --namespace <your-caller-namespace> \
  --region us-west-2 \
  --ca-certificate-file 'path/to/your/ca.pem' \
  --retention-days 1

tcld namespace create \
  --namespace <your-target-namespace> \
  --region us-west-2 \
  --ca-certificate-file 'path/to/your/ca.pem' \
  --retention-days 1
```

Alternatively, you can create Namespaces through the UI: [https://cloud.temporal.io/Namespaces](https://cloud.temporal.io/Namespaces).

### Create a Nexus Endpoint to route requests from caller to handler

To create a Nexus Endpoint you must have a Developer account role or higher, and have NamespaceAdmin permission on the `--target-namespace`.

```
tcld nexus endpoint create \
  --name nexus-simple-endpoint \
  --target-task-queue nexus-simple-handler-sample \
  --target-namespace <your-handler-namespace.account> \
  --allow-namespace <your-caller-namespace.account> \
  --description-file endpoint_description.md
```

The `--allow-namespace` is used to build an Endpoint allowlist of caller Namespaces that can use the Nexus Endpoint, as described in Runtime Access Control.

Alternatively, you can create a Nexus Endpoint through the UI: [https://cloud.temporal.io/nexus](https://cloud.temporal.io/nexus).

## Observability

### Web UI

A synchronous Nexus Operation will surface in the caller Workflow as follows, with just `NexusOperationScheduled` and `NexusOperationCompleted` events in the caller's Event history:

<CaptionedImage
    src="/img/cloud/nexus/go-sdk-observability-sync.png"
    title="Observability Sync"
/>

An asynchronous Nexus Operation will surface in the caller Workflow as follows, with `NexusOperationScheduled`, `NexusOperationStarted`, and `NexusOperationCompleted`, in the caller's Event history:

<CaptionedImage
    src="/img/cloud/nexus/go-sdk-observability-async.png"
    title="Observability Async"
/>

### Temporal CLI

Use the `workflow describe` command to show pending Nexus Operations in the caller Workflow and any attached callbacks on the handler Workflow:

```
temporal workflow describe -w <ID>
```

Nexus events are included in the caller's Event history:

```
temporal workflow show -w <ID>
```

For **asynchronous Nexus Operations** the following are reported in the caller's history:

- `NexusOperationScheduled`
- `NexusOperationStarted`
- `NexusOperationCompleted`

For **synchronous Nexus Operations** the following are reported in the caller's history:

- `NexusOperationScheduled`
- `NexusOperationCompleted`

:::note

`NexusOperationStarted` isn't reported in the caller's history for synchronous operations.

:::

## Learn more

- Read the high-level description of the [Temporal Nexus feature](/evaluate/nexus) and watch the [Nexus keynote and demo](https://youtu.be/qqc2vsv1mrU?feature=shared&t=2082).
- Learn how Nexus works in the [Nexus deep dive talk](https://www.youtube.com/watch?v=izR9dQ_eIe4) and [Encyclopedia](/nexus).
- Deploy Nexus Endpoints in production with [Temporal Cloud](/cloud/nexus).

---

## Nexus - .NET SDK

<ReleaseNoteHeader
  featureName="nexus"
/>

![.NET SDK Banner](/img/assets/banner-dotnet-temporal.png)

## Temporal Nexus

- [Quickstart](/develop/dotnet/nexus/quickstart)
- [Feature guide](/develop/dotnet/nexus/feature-guide)

---

## Nexus .NET Quickstart

<ReleaseNoteHeader
  featureName="nexus"
/>

[Temporal Nexus](/evaluate/nexus) connects Temporal Applications within and across Namespaces using a Nexus Endpoint, a Nexus Service contract, and Nexus Operations. Build a Nexus Service that wraps an existing Temporal Workflow, then invoke it from a caller Workflow.

:::info NEW TO NEXUS?

This page will help you get a working sample running in .NET.

To evaluate whether Nexus fits your use case, see the [evaluation guide](/evaluate/nexus) and to learn more about Nexus features, click [here](/nexus).

:::

**Prerequisites:** Complete the [.NET SDK Quickstart](/develop/dotnet/set-up-your-local-dotnet) first.
You should have `SayHelloWorkflow`, `MyActivities`, and a `Worker` project from that guide.

## What you'll build

You have `SayHelloWorkflow` running in the `default` Namespace.

By the end of this guide:

1. A Nexus Service will expose `SayHelloWorkflow` as an Operation.
2. A second Namespace will contain a Workflow that calls that Operation.
3. The caller Workflow will get back `"Hello, Temporal!"` — the same result, but across Namespaces.

<SetupSteps>

<SetupStep code={
<>

<CodeSnippet language="csharp">
{`namespace MyNamespace;

using NexusRpc;

[NexusService]
public interface ISayHelloNexusService
{
    public static readonly string EndpointName = "my-nexus-endpoint-name";

    [NexusOperation]
    string SayHello(MyInput input);

    public record MyInput(string Name);
}`}
</CodeSnippet>

</>
}>

## 1. Define the Nexus Service

Create a file called `ISayHelloNexusService.cs` in the `Workflow` project.

The `[NexusService]` attribute on an interface defines the Nexus Service contract. `[NexusOperation]` marks each method that callers can invoke. The `EndpointName` static field is shared between the handler and caller to keep the endpoint name in one place.

`SayHelloWorkflow` returns `string`, so the operation output type is `string`. The input is a `record` carrying the workflow argument.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="csharp">
{`namespace MyNamespace;

using NexusRpc.Handlers;
using Temporalio.Nexus;

[NexusServiceHandler(typeof(ISayHelloNexusService))]
public class SayHelloNexusServiceHandler
{
    [NexusOperationHandler]
    public IOperationHandler<ISayHelloNexusService.MyInput, string> SayHello() =>
        WorkflowRunOperationHandler.FromHandleFactory(
            (WorkflowRunOperationContext context, ISayHelloNexusService.MyInput input) =>
                context.StartWorkflowAsync(
                    (SayHelloWorkflow wf) => wf.RunAsync(input.Name),
                    new() { Id = context.HandlerContext.RequestId }));
}`}
</CodeSnippet>

</>
}>

## 2. Define the Nexus Operation handler

Create a file called `SayHelloNexusServiceHandler.cs` in the `Workflow` project.

`[NexusServiceHandler]` links this class to the `ISayHelloNexusService` contract. Each `[NexusOperationHandler]` method returns an `IOperationHandler` that describes how the operation runs.

`WorkflowRunOperationHandler.FromHandleFactory` creates an asynchronous operation backed by a Workflow run. The `input.Name` bridges the Nexus `MyInput` record to `SayHelloWorkflow`'s `string` parameter.

Using `context.HandlerContext.RequestId` as the Workflow ID ensures that retried Nexus operation requests are deduplicated.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="csharp">
{`// Worker/Program.cs
var activities = new MyActivities();
using var worker = new TemporalWorker(
    client,
    new TemporalWorkerOptions("my-task-queue")
        .AddActivity(activities.SayHello)
        .AddWorkflow<SayHelloWorkflow>()
        .AddNexusService(new SayHelloNexusServiceHandler()));`}
</CodeSnippet>

</>
}>

## 3. Register the Nexus Service handler in a Worker

Update `Worker/Program.cs` to register the Nexus Service handler alongside the existing Workflow and Activity registrations.

A Worker will only handle incoming Nexus requests if the Nexus Service handlers are registered. Like `.AddActivity()`, `.AddNexusService()` takes an instance — both register concrete objects that the Worker dispatches work to.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="csharp">
{`namespace MyNamespace;

using Temporalio.Workflows;

[Workflow]
public class CallerWorkflow
{
    public static readonly string CallerTaskQueue = "my-caller-task-queue";

    [WorkflowRun]
    public async Task<string> RunAsync(string name)
    {
        return await Workflow
            .CreateNexusWorkflowClient<ISayHelloNexusService>(
                ISayHelloNexusService.EndpointName)
            .ExecuteNexusOperationAsync(svc => svc.SayHello(new(name)));
    }
}`}
</CodeSnippet>

</>
}>

## 4. Develop the caller Workflow

Create a file called `CallerWorkflow.cs` in the `Workflow` project.

The caller Workflow uses `Workflow.CreateNexusWorkflowClient<T>()` to get a typed client bound to the Nexus Endpoint. `ExecuteNexusOperationAsync` starts the operation and waits for the result.

The caller only depends on the Service contract (`ISayHelloNexusService`), not the handler implementation. This decoupling is what allows the caller and handler to live in separate Namespaces or even separate codebases.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="bash">
{`temporal operator namespace create --namespace my-caller-namespace`}
</CodeSnippet>

<CodeSnippet language="bash">
{`temporal operator nexus endpoint create \\
  --name my-nexus-endpoint-name \\
  --target-namespace default \\
  --target-task-queue my-task-queue`}
</CodeSnippet>

</>
}>

## 5. Create the caller Namespace and Nexus Endpoint

Before running the application, create a caller Namespace and a Nexus Endpoint to route requests from the caller to the handler. The handler uses the `default` Namespace that was created when you started the dev server.

Namespaces provide isolation between the caller and handler sides. The Nexus Endpoint acts as a routing layer that connects the caller Namespace to the handler's target Namespace and Task Queue. The endpoint name must match the `EndpointName` constant defined in Step 1.

Make sure your local Temporal dev server is running (`temporal server start-dev`).

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="bash">
{`dotnet new console -o CallerStarter
dotnet sln TemporalioHelloWorld.sln \\
  add CallerStarter/CallerStarter.csproj
dotnet add CallerStarter/CallerStarter.csproj \\
  reference Workflow/Workflow.csproj
dotnet add CallerStarter/CallerStarter.csproj package Temporalio`}
</CodeSnippet>

</>
}>

## 6. Add the caller project

Create a `CallerStarter` console project that starts a caller Worker and executes the Workflow.

The commands on the right create a new console project, add it to the solution, reference the Workflow project, and add the Temporalio package.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="csharp" title="CallerStarter/Program.cs">
{`using MyNamespace;
using Temporalio.Client;
using Temporalio.Worker;

var client = await TemporalClient.ConnectAsync(
    new("localhost:7233") { Namespace = "my-caller-namespace" });

using var tokenSource = new CancellationTokenSource();
Console.CancelKeyPress += (_, eventArgs) =>
{
    tokenSource.Cancel();
    eventArgs.Cancel = true;
};

using var worker = new TemporalWorker(
    client,
    new TemporalWorkerOptions(CallerWorkflow.CallerTaskQueue)
        .AddWorkflow<CallerWorkflow>());

Console.WriteLine("Running caller worker");
var workerTask = worker.ExecuteAsync(tokenSource.Token);

var result = await client.ExecuteWorkflowAsync(
    (CallerWorkflow wf) => wf.RunAsync("Temporal"),
    new(id: $"caller-workflow-{Guid.NewGuid()}",
        taskQueue: CallerWorkflow.CallerTaskQueue));
Console.WriteLine("Workflow result: {0}", result);

tokenSource.Cancel();
try { await workerTask; } catch (OperationCanceledException) { }`}
</CodeSnippet>

</>
}>

## 7. Create the caller starter

Create the `CallerStarter/Program.cs` file with the code on the right.

This brings everything together: the caller Worker hosts `CallerWorkflow`, which uses the Nexus client to invoke `SayHello` on the handler side. The full request flows from the caller Workflow, through the Nexus Endpoint, to the handler Worker running `SayHelloWorkflow`, and back to the caller.

</SetupStep>

<SetupStep code={
<>

<CodeSnippet language="bash" title="Start the handler Worker">
{`dotnet run --project Worker/Worker.csproj`}
</CodeSnippet>

<CodeSnippet language="bash" title="Run the caller">
{`dotnet run --project CallerStarter/CallerStarter.csproj`}
</CodeSnippet>

</>
}>

## 8. Run and verify

Run the application using the commands on the right.

You should see:

```
Workflow result: Hello, Temporal!
```

Open the [Temporal Web UI](http://localhost:8233) and find the `CallerWorkflow` execution in the `my-caller-namespace` Namespace. You should see `NexusOperationScheduled`, `NexusOperationStarted`, and `NexusOperationCompleted` events in the Event history.

</SetupStep>

</SetupSteps>

## Next Steps

Now that you have a working Nexus Service, here are some resources to deepen your understanding:

- **[.NET Nexus Feature Guide](/develop/dotnet/nexus)**: Covers synchronous and asynchronous Operations, error handling, cancellation, and cross-Namespace calls.
- **[Nexus Operations](/nexus/operations)**: The full Operation lifecycle, including retries, timeouts, and execution semantics.
- **[Nexus Services](/nexus/services)**: Designing Service contracts and registering multiple Services per Worker.
- **[Nexus Patterns](/nexus/patterns)**: Comparing the collocated and router-queue deployment patterns.
- **[Error Handling in Nexus](/nexus/error-handling)**: Handling retryable and non-retryable errors across caller and handler boundaries.
- **[Execution Debugging](/nexus/execution-debugging)**: Bi-directional linking and OpenTelemetry tracing for debugging Nexus calls.
- **[Nexus Endpoints](/nexus/endpoints)**: Managing Endpoints and understanding how they route requests.
- **[Temporal Nexus on Temporal Cloud](/cloud/nexus)**: Deploying Nexus in a production Temporal Cloud environment with built-in access controls and multi-region connectivity.

---

## Enriching the user interface - .NET SDK

Temporal supports adding context to Workflows and events with metadata.
This helps users identify and understand Workflows and their operations.

## Adding Summary and Details to Workflows

### Starting a Workflow

When starting a Workflow, you can provide a static summary and details to help identify the Workflow in the UI:

```csharp
using Temporalio.Client;

// Create client
var client = await TemporalClient.ConnectAsync(new("localhost:7233"));

// Start a Workflow with static summary and details
var handle = await client.StartWorkflowAsync(
    (YourWorkflow wf) => wf.RunAsync("Workflow input"),
    new WorkflowOptions
    {
        Id = "your-Workflow-id",
        TaskQueue = "your-task-queue",
        StaticSummary = "Order processing for customer #12345",
        StaticDetails = "Processing premium order with expedited shipping"
    });
```

`StaticSummary` is a single-line description that appears in the Workflow list view, limited to 200 bytes.
`StaticDetails` can be multi-line and provides more comprehensive information that appears in the Workflow details view, with a larger limit of 20K bytes.

The input format is standard Markdown excluding images, HTML, and scripts.

You can also use the `ExecuteWorkflowAsync` method with the same parameters:

```csharp
var result = await client.ExecuteWorkflowAsync(
    (YourWorkflow wf) => wf.RunAsync("Workflow input"),
    new WorkflowOptions
    {
        Id = "your-Workflow-id",
        TaskQueue = "your-task-queue",
        StaticSummary = "Order processing for customer #12345",
        StaticDetails = "Processing premium order with expedited shipping"
    });
```

### Inside the Workflow

Within a Workflow, you can get and set the _current Workflow details_.
Unlike static summary/details set at Workflow start, this value can be updated throughout the life of the Workflow.
Current Workflow details also takes Markdown format (excluding images, HTML, and scripts) and can span multiple lines.

```csharp
using Temporalio.Workflows;

[Workflow]
public class YourWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync(string input)
    {
        // Get the current details
        var currentDetails = Workflow.CurrentDetails;
        Workflow.Logger.LogInformation($"Current details: {currentDetails}");

        // Set/update the current details
        Workflow.CurrentDetails = "Updated Workflow details with new status";

        return "Workflow completed";
    }
}
```

### Adding Summary to Activities and Timers

You can attach a metadata parameter `Summary` to Activities when starting them from within a Workflow:

```csharp
using Temporalio.Activities;
using Temporalio.Workflows;

[Workflow]
public class YourWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync(string input)
    {
        // Execute an activity with a summary
        var result = await Workflow.ExecuteActivityAsync(
            (YourActivities act) => act.YourActivityAsync(input),
            new ActivityOptions
            {
