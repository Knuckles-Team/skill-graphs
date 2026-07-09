# Cloud profile for Temporal Cloud
[profile.cloud]
address = "your-namespace.a1b2c.tmprl.cloud:7233"
namespace = "your-namespace"
tls_client_cert_data = "your-tls-client-cert-data"
tls_client_key_path = "your-tls-client-key-path"
```

With the connections options defined in the configuration file, use the `ClientEnvConfig.LoadClientConnectOptions`
method to create a Temporal Client using the `staging` profile as follows. After loading the profile, you can also
programmatically override specific connection options before creating the client.

```csharp title="LoadProfile.cs" {25. 41}
using Temporalio.Client;
using Temporalio.Client.EnvConfig;

namespace TemporalioSamples.EnvConfig;

/// <summary>
/// Sample demonstrating loading a named environment configuration profile and
/// programmatically overriding its values.
/// </summary>
public static class LoadProfile
{
    public static async Task RunAsync()
    {
        Console.WriteLine("--- Loading 'staging' profile with programmatic overrides ---");

        try
        {
            var configFile = Path.Combine(Directory.GetCurrentDirectory(), "config.toml");
            var profileName = "staging";

            Console.WriteLine("The 'staging' profile in config.toml has an incorrect address (localhost:9999).");
            Console.WriteLine("We'll programmatically override it to the correct address.");

            // Load the 'staging' profile
            var connectOptions = ClientEnvConfig.LoadClientConnectOptions(new ClientEnvConfig.ProfileLoadOptions
            {
                Profile = profileName,
                ConfigSource = DataSource.FromPath(configFile),
            });

            // Override the target host to the correct address.
            // This is the recommended way to override configuration values.
            connectOptions.TargetHost = "localhost:7233";

            Console.WriteLine($"\nLoaded '{profileName}' profile from {configFile} with overrides.");
            Console.WriteLine($"  Address: {connectOptions.TargetHost} (overridden from localhost:9999)");
            Console.WriteLine($"  Namespace: {connectOptions.Namespace}");

            Console.WriteLine("\nAttempting to connect to client...");

            var client = await TemporalClient.ConnectAsync(connectOptions);
            Console.WriteLine("✅ Client connected successfully!");

            // Test the connection by checking the service
            var sysInfo = await client.Connection.WorkflowService.GetSystemInfoAsync(new());
            Console.WriteLine("✅ Successfully verified connection to Temporal server!\n{0}", sysInfo);
        }
        catch (Exception ex) when (ex is not OperationCanceledException)
        {
            Console.WriteLine($"❌ Failed to connect: {ex.Message}");
        }
    }
}
```

</TabItem>

<TabItem value="env-vars" label="Environment Variables">

The following environment variables are required to connect to Temporal Cloud:

- `TEMPORAL_NAMESPACE`: Your Namespace and Account ID combination in the format `<namespace_id>.<account_id>`.
- `TEMPORAL_ADDRESS`: The gRPC endpoint for your Temporal Cloud Namespace.
- `TEMPORAL_API_KEY`: Your API key value. Required if you are using API key authentication.
- `TEMPORAL_TLS_CLIENT_CERT_DATA` or `TEMPORAL_TLS_CLIENT_CERT_PATH`: Your mTLS client certificate data or file path.
  Required if you are using mTLS authentication.
- `TEMPORAL_TLS_CLIENT_KEY_DATA` or `TEMPORAL_TLS_CLIENT_KEY_PATH`: Your mTLS client private key data or file path.
  Required if you are using mTLS authentication.

Ensure these environment variables exist in your environment before running your .NET application.

Import the `Temporalio.Client.EnvConfig` namespace to set connection options for the Temporal Client using environment variables.
The `ClientEnvConfig.LoadClientConnectOptions` method will automatically load all environment variables. For a list of all available
environment variables and their default values, refer to
[Environment Configuration](/references/client-environment-configuration).

For example, the following code snippet loads all environment variables and creates a Temporal Client with the options
specified in those variables. If you have defined a configuration file at either the default location
(`~/.config/temporalio/temporal.toml`) or a custom location specified by the `TEMPORAL_CONFIG_FILE` environment
variable, this will also load the default profile in the configuration file. However, any options set via environment
variables will take precedence.

```csharp {16,20}
using Temporalio.Client;
using Temporalio.Client.EnvConfig;

namespace TemporalioSamples.EnvConfig;

/// <summary>
/// Sample demonstrating loading the default environment configuration profile
/// from a TOML file.
/// </summary>
public static class LoadFromFile
{
    public static async Task RunAsync()
    {
        try
        {
            var connectOptions = ClientEnvConfig.LoadClientConnectOptions();

            Console.WriteLine("\nAttempting to connect to client...");

            var client = await TemporalClient.ConnectAsync(connectOptions);
            Console.WriteLine("✅ Client connected successfully!");
        }
        catch (Exception ex) when (ex is not OperationCanceledException)
        {
            Console.WriteLine($"❌ Failed to connect: {ex.Message}");
        }
    }
}
```

</TabItem>

<TabItem value="code" label="Code">

You can also provide connections options in your .NET code directly. To create an initial connection, provide the
Namespace and API key values to the ` TemporalClient.ConnectAsync` method.

```csharp
var myClient = TemporalClient.ConnectAsync(new(<endpoint>)
{
    Namespace = "<namespace_id>.<account_id>",
    ApiKey = "<APIKey>",
    Tls = new(),
});
```

To update an API key, update the value of `ApiKey` on the existing client connection:

```csharp
myClient.Connection.ApiKey = myKeyUpdated;
```

</TabItem>

</Tabs>

## Start a Workflow {/* #start-workflow */}

**How to start a Workflow using the Temporal .NET SDK**

[Workflow Execution](/workflow-execution) semantics rely on several parameters—that is, to start a Workflow Execution
you must supply a Task Queue that will be used for the Tasks (one that a Worker is polling), the Workflow Type,
language-specific contextual data, and Workflow Function parameters.

A request to spawn a Workflow Execution causes the Temporal Service to create the first Event
([WorkflowExecutionStarted](/references/events#workflowexecutionstarted)) in the Workflow Execution Event History. The
Temporal Service then creates the first Workflow Task, resulting in the first
[WorkflowTaskScheduled](/references/events#workflowtaskscheduled) Event.

To start a Workflow Execution in .NET, use either the `StartWorkflowAsync()` or `ExecuteWorkflowAsync()` methods in the
Client. You must set a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id) and [Task Queue](/task-queue) in
the `WorkflowOptions` given to the method.

```csharp
var result = await client.ExecuteWorkflowAsync(
    (MyWorkflow wf) => wf.RunAsync(),
    new(id: "my-workflow-id", taskQueue: "my-task-queue");
Console.WriteLine("Result: {0}", result);
```

## Get Workflow results {/* #get-workflow-results */}

**How to get the results of a Workflow Execution using the Temporal .NET SDK**

If the call to start a Workflow Execution is successful, you will gain access to the Workflow Execution's Run Id.

The Workflow Id, Run Id, and Namespace may be used to uniquely identify a Workflow Execution in the system and get its
result.

It's possible to both block progress on the result (synchronous execution) or get the result at some other point in time
(asynchronous execution).

In the Temporal Platform, it's also acceptable to use Queries as the preferred method for accessing the state and
results of Workflow Executions.

Use `StartWorkflowAsync()` or `GetWorkflowHandle()` to return a Workflow handle. Then use the `GetResultAsync()` method
to await on the result of the Workflow.

To get a handle for an existing Workflow by its Id, you can use `GetWorkflowHandle()`.

Then use
[`DescribeAsync()`](https://dotnet.temporal.io/api/Temporalio.Client.WorkflowHandle.html#Temporalio_Client_WorkflowHandle_DescribeAsync_Temporalio_Client_WorkflowDescribeOptions_)
to get the current status of the Workflow. If the Workflow does not exist, this call fails.

```csharp
var handle = client.GetWorkflowHandle("my-workflow-id");
var result = await handle.GetResultAsync<string>();
Console.WriteLine("Result: {0}", result);
```

---

## .Net SDK developer guide

![.NET](/img/assets/banner-dotnet-temporal.png)

## Install and get started

You can find detailed installation instructions for the .NET SDK in the [Quickstart](/develop/dotnet/set-up-your-local-dotnet).

There's also a short walkthrough of how to use the Temporal primitives (Activities, Workflows, and Workers) to build and run a Temporal application to get you up and running.

Once your local Temporal Service is set up, continue building with the following resources:

- [Workflow basics](/develop/dotnet/workflows/basics)
- [Activity basics](/develop/dotnet/activities/basics)
- [Start an Activity execution](/develop/dotnet/activities/execution)
- [Run Worker processes](/develop/dotnet/workers/run-worker-process)

From there, you can dive deeper into any of the Temporal primitives to start building Workflows that fit your use cases.

## [Workflows](/develop/dotnet/workflows)

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

## [Activities](/develop/dotnet/activities)

- [Activity basics](/develop/dotnet/activities/basics)
- [Activity execution](/develop/dotnet/activities/execution)
- [Standalone Activities](/develop/dotnet/activities/standalone-activities)
- [Timeouts](/develop/dotnet/activities/timeouts)
- [Asynchronous Activity completion](/develop/dotnet/activities/asynchronous-activity)
- [Dynamic Activity](/develop/dotnet/activities/dynamic-activity)
- [Benign exceptions](/develop/dotnet/activities/benign-exceptions)

## [Workers](/develop/dotnet/workers)

- [Worker processes](/develop/dotnet/workers/run-worker-process)
- [Interceptors](/develop/dotnet/workers/interceptors)

## [Temporal Client](/develop/dotnet/client)

- [Temporal Client](/develop/dotnet/client/temporal-client)

## [Temporal Nexus](/develop/dotnet/nexus)

- [Quickstart](/develop/dotnet/nexus/quickstart)
- [Feature guide](/develop/dotnet/nexus/feature-guide)

## [Platform](/develop/dotnet/platform)

- [Observability](/develop/dotnet/platform/observability)
- [Enriching the UI](/develop/dotnet/platform/enriching-ui)

## [Best practices](/develop/dotnet/best-practices)

- [Error handling](/develop/dotnet/best-practices/error-handling)
- [Testing](/develop/dotnet/best-practices/testing-suite)
- [Debugging](/develop/dotnet/best-practices/debugging)
- [Converters and encryption](/develop/dotnet/best-practices/converters-and-encryption)

## Temporal .NET Technical Resources

- [.NET Quickstart](/develop/dotnet/set-up-your-local-dotnet)
- [.NET API Documentation](https://dotnet.temporal.io/api/)
- [.NET SDK Code Samples](https://github.com/temporalio/samples-dotnet)
- [.NET SDK GitHub](https://github.com/temporalio/sdk-dotnet)
- [Temporal 101 in .NET Free Course](https://learn.temporal.io/courses/temporal_101/dotnet/)

Get Connected with the Temporal .NET Community

- [Temporal .NET Community Slack](https://temporalio.slack.com/archives/C012SHMPDDZ)
- [.NET SDK Forum](https://community.temporal.io/tag/dotnet-sdk)

---

## Temporal Nexus - .NET SDK feature guide

<ReleaseNoteHeader
  featureName="nexus"
/>

Use [Temporal Nexus](/evaluate/nexus) to connect Temporal Applications within and across Namespaces using a Nexus Endpoint, a Nexus Service contract, and Nexus Operations.

This page shows how to do the following:

- [Run a development Temporal Service with Nexus enabled](#run-the-temporal-nexus-development-server)
- [Create caller and handler Namespaces](#create-caller-handler-namespaces)
- [Create a Nexus Endpoint to route requests from caller to handler](#create-nexus-endpoint)
- [Define the Nexus Service contract](#define-nexus-service-contract)
- [Develop a Nexus Service and Operation handlers](#develop-nexus-service-operation-handlers)
- [Develop a caller Workflow that uses a Nexus Service](#develop-caller-workflow-nexus-service)
- [Make Nexus calls across Namespaces with a development Server](#nexus-calls-across-namespaces-dev-server)
- [Make Nexus calls across Namespaces in Temporal Cloud](#nexus-calls-across-namespaces-temporal-cloud)

:::note

This documentation uses source code derived from the [.NET Nexus sample](https://github.com/temporalio/samples-dotnet/tree/main/src/NexusSimple).

:::

## Run the Temporal Development Server with Nexus enabled {/* #run-the-temporal-nexus-development-server */}

Prerequisites:

- [Install the latest Temporal CLI](https://learn.temporal.io/getting_started/dotnet/dev_environment/#set-up-a-local-temporal-service-for-development-with-temporal-cli) (v1.3.0 or higher recommended)
- [Install the latest Temporal .NET SDK](https://learn.temporal.io/getting_started/dotnet/dev_environment/#install-the-temporal-net-sdk) (v1.9.0 or higher)

The first step in working with Temporal Nexus involves starting a Temporal server with Nexus enabled.

```
temporal server start-dev
```

This command automatically starts the Temporal development server with the Web UI, and creates the `default` Namespace. It uses an in-memory database, so do not use it for real use cases.

The Temporal Web UI should now be accessible at [http://localhost:8233](http://localhost:8233), and the Temporal Server should now be available for client connections on `localhost:7233`.

## Create caller and handler Namespaces {/* #create-caller-handler-namespaces */}

Before setting up Nexus endpoints, create separate Namespaces for the caller and handler.

```
temporal operator namespace create --namespace nexus-simple-handler-namespace
temporal operator namespace create --namespace nexus-simple-caller-namespace
```

`nexus-simple-handler-namespace` will contain the Nexus Operation handler, and we will use a Workflow in `nexus-simple-caller-namespace` to call that Operation handler.
We use different namespaces to demonstrate cross-Namespace Nexus calls.

## Create a Nexus Endpoint to route requests from caller to handler {/* #create-nexus-endpoint */}

After establishing caller and handler Namespaces, the next step is to create a Nexus Endpoint to route requests.

```
temporal operator nexus endpoint create \
  --name nexus-simple-endpoint \
  --target-namespace nexus-simple-handler-namespace \
  --target-task-queue nexus-simple-handler-sample
```

You can also use the Web UI to create the Namespaces and Nexus endpoint.

## Define the Nexus Service contract {/* #define-nexus-service-contract */}

Defining a clear contract for the Nexus Service is crucial for smooth communication.

In this example, there is a service package that describes the Service and Operation names along with input/output types for caller Workflows to use the Nexus Endpoint.

Each [Temporal SDK includes and uses a default Data Converter](https://docs.temporal.io/dataconversion).
The default data converter encodes payloads in the following order: Null, Byte array, Protobuf JSON, and JSON.
In a polyglot environment, that is where more than one language and SDK is being used to develop a Temporal solution, Protobuf and JSON are common choices.
This example uses .NET classes serialized into JSON.

[NexusSimple/IHelloService.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/NexusSimple/IHelloService.cs)
```csharp
using NexusRpc;

[NexusService]
public interface IHelloService
{
    static readonly string EndpointName = "nexus-simple-endpoint";

    [NexusOperation]
    EchoOutput Echo(EchoInput input);

    [NexusOperation]
    HelloOutput SayHello(HelloInput input);

    public record EchoInput(string Message);

    public record EchoOutput(string Message);

    public record HelloInput(string Name, HelloLanguage Language);

    public record HelloOutput(string Message);

    public enum HelloLanguage
    {
        En,
        Fr,
        De,
        Es,
        Tr,
    }
}
```

## Develop a Nexus Service and Operation handlers {/* #develop-nexus-service-operation-handlers */}

Nexus Operation handlers are typically defined in the same Worker as the underlying Temporal primitives they abstract.
Operation handlers can decide if a given Nexus Operation will be synchronous or asynchronous.
They can invoke underlying Temporal primitives such as a Query, Signal, or Update using the Temporal SDK Client, or run other reliable code.
Handlers should be reliable since the [circuit breaker](/nexus/operations#circuit-breaking) trips after 5 consecutive retryable errors, blocking all Operations from the caller to that Endpoint.

The `Temporalio.Nexus` namespace has utilities to help create Nexus Operations:

- `NexusOperationExecutionContext.Current.TemporalClient` \- Get the Temporal Client that the Worker was initialized with for synchronous handlers backed by
  Temporal primitives such as Signals and Queries
- `WorkflowRunOperationHandler.FromHandleFactory` \- Run a Workflow as an asynchronous Nexus Operation

This example starts with a sync Operation handler example using the `OperationHandler.Sync` method, and then shows how to create an async Operation handler that uses `WorkflowRunOperationHandler.FromHandleFactory` to start a handler Workflow from a Nexus Operation.

### Develop a Synchronous Nexus Operation handler

The `OperationHandler.Sync` method is for exposing simple RPC handlers.
Use `NexusOperationExecutionContext.Current.TemporalClient` to get the Temporal Client for signaling, querying, and listing Workflows.
Implementations can also make other calls, but handlers should be reliable to avoid tripping the [circuit breaker](/nexus/operations#circuit-breaking).

[NexusSimple/Handler/HelloService.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/NexusSimple/Handler/HelloService.cs)
```csharp
using NexusRpc.Handlers;

[NexusServiceHandler(typeof(IHelloService))]
public class HelloService
{
    [NexusOperationHandler]
    public IOperationHandler<IHelloService.EchoInput, IHelloService.EchoOutput> Echo() =>
        // This Nexus service operation is a simple sync handler
        OperationHandler.Sync<IHelloService.EchoInput, IHelloService.EchoOutput>(
            (ctx, input) => new(input.Message));

    // ...
}
```

### Use the Temporal Client for Signals, Queries, and Updates

A common pattern is to use the Temporal Client from within a sync handler to Signal, Query, or Update a Workflow.
You can also use Signal-With-Start or Update-With-Start to ensure the Workflow is started and send it a Signal or Update.
All calls must complete within the [Nexus request timeout](/cloud/limits#nexus-operation-request-timeout). Updates should be short-lived to stay within this deadline.

The [nexus_messaging](https://github.com/temporalio/samples-dotnet/tree/main/src/NexusMessaging) sample shows how to create a Nexus Service that uses synchronous operations to send Updates and Queries:

Use `NexusOperationExecutionContext`, like below, to get the Client that the Worker was initialized with. In this example, the Workflow Id is derived from the client Id using the `WorkflowIdForUser` method. This converts a given client Id (in this case, the client is passing in a user Id) to generate a Workflow Id from it.
This way the client only needs the identifier it cares about.

[NexusMessaging/CallerPattern/Handler/NexusGreetingService.cs](https://github.com/temporalio/samples-dotnet/tree/main/src/NexusMessaging/CallerPattern/Handler/NexusGreetingService.cs)

```csharp
private static string WorkflowIdForUser(string userId) => $"GreetingWorkflow_for_{userId}";

[NexusOperationHandler]
public IOperationHandler<INexusGreetingService.GetLanguagesInput, INexusGreetingService.GetLanguagesOutput> GetLanguages() =>
    OperationHandler.Sync<INexusGreetingService.GetLanguagesInput, INexusGreetingService.GetLanguagesOutput>(
        async (ctx, input) =>
        {
            // Access the Temporal client from the Nexus operation context
            var client = NexusOperationExecutionContext.Current.TemporalClient;
            var handle = client.GetWorkflowHandle<GreetingWorkflow>(WorkflowIdForUser(input.UserId));
            return await handle.QueryAsync(wf => wf.QueryLanguages(input.IncludeUnsupported));
        });
    ...
```

There are two examples of messaging through Nexus in the sample code: the [caller pattern](https://github.com/temporalio/samples-dotnet/tree/main/src/NexusMessaging/CallerPattern) and the [on-demand pattern](https://github.com/temporalio/samples-dotnet/tree/main/src/NexusMessaging/OnDemandPattern).
The caller pattern shows how to send messages to an existing Workflow, while the on-demand pattern shows how to start a Workflow through Nexus and then send Signals to it.

### Develop an Asynchronous Nexus Operation handler to start a Workflow

Use the `WorkflowRunOperationHandler.FromHandleFactory` method, which is the easiest way to expose a Workflow as an operation.

[NexusSimple/Handler/HelloService.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/NexusSimple/Handler/HelloService.cs)
```csharp

using NexusRpc.Handlers;
using Temporalio.Nexus;

[NexusServiceHandler(typeof(IHelloService))]
public class HelloService
{
    // ...

    [NexusOperationHandler]
    public IOperationHandler<IHelloService.HelloInput, IHelloService.HelloOutput> SayHello() =>
        // This Nexus service operation is backed by a workflow run
        WorkflowRunOperationHandler.FromHandleFactory(
            (WorkflowRunOperationContext context, IHelloService.HelloInput input) =>
                context.StartWorkflowAsync(
                    (HelloHandlerWorkflow wf) => wf.RunAsync(input),
                    // Workflow IDs should typically be business meaningful IDs and are used to
                    // dedupe workflow starts. For this example, we're using the request ID
                    // allocated by Temporal when the caller workflow schedules the operation,
                    // this ID is guaranteed to be stable across retries of this operation.
                    new() { Id = context.HandlerContext.RequestId }));
}
```

Workflow IDs should typically be business-meaningful IDs and are used to dedupe Workflow starts. In general, the ID should be passed in the Operation input as part of the Nexus Service contract.

:::tip RESOURCES

[Attach multiple Nexus callers to a handler Workflow](/nexus/operations#attaching-multiple-nexus-callers) with a Conflict-Policy of Use-Existing.

:::

#### Map a Nexus Operation input to multiple Workflow arguments

A Nexus Operation can only take one input parameter. If you want a Nexus Operation to start a Workflow that takes multiple arguments, simply pass in different arguments using `RunAsync`.

[NexusMultiArg/Handler/HelloService.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/NexusMultiArg/Handler/HelloService.cs)
```csharp
[NexusServiceHandler(typeof(IHelloService))]
public class HelloService
{
    [NexusOperationHandler]
    public IOperationHandler<IHelloService.HelloInput, IHelloService.HelloOutput> SayHello() =>
        // This Nexus service operation is backed by a workflow run. For this sample, we are
        // altering the parameters to the workflow (in this case expanding to two parameters).
        WorkflowRunOperationHandler.FromHandleFactory(
            (WorkflowRunOperationContext context, IHelloService.HelloInput input) =>
                context.StartWorkflowAsync(
                    (HelloHandlerWorkflow wf) => wf.RunAsync(input.Language, input.Name),
                    // Workflow IDs should typically be business meaningful IDs and are used to
                    // dedupe workflow starts. For this example, we're using the request ID
                    // allocated by Temporal when the caller workflow schedules the operation,
                    // this ID is guaranteed to be stable across retries of this operation.
                    new() { Id = context.HandlerContext.RequestId }));
}
```

### Register a Nexus Service in a Worker

After developing an asynchronous Nexus Operation handler to start a Workflow, the next step is to register a Nexus Service in a Worker.

[NexusSimple/Program.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/NexusSimple/Program.cs)
```csharp
async Task RunHandlerWorkerAsync()
{
    // Run worker until cancelled
    logger.LogInformation("Running handler worker");
    using var worker = new TemporalWorker(
        await ConnectClientAsync("nexus-simple-handler-namespace"),
        new TemporalWorkerOptions(taskQueue: "nexus-simple-handler-sample").
            AddNexusService(new HelloService()).
            AddWorkflow<HelloHandlerWorkflow>());
    try
    {
        await worker.ExecuteAsync(tokenSource.Token);
