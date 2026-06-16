This is so that you can change what data is passed to the Activity without breaking a method signature.

Activity parameters are the method parameters of the method with the `[Activity]` attribute.
These can be any data type Temporal can convert, including records.
Technically this can be multiple parameters, but Temporal strongly encourages a single parameter containing all input fields.

---

## Benign exceptions - .NET SDK

**How to mark an Activity error as benign using the Temporal .NET SDK**

When Activities throw errors that are expected or not severe, they can create noise in your logs, metrics, and OpenTelemetry traces, making it harder to identify real issues.
By marking these errors as benign, you can exclude them from your observability data while still handling them in your Workflow logic.

To mark an error as benign, set the `category` parameter to `ApplicationErrorCategory.Benign` when throwing an [`ApplicationFailureException`](https://dotnet.temporal.io/api/Temporalio.Exceptions.ApplicationFailureException.html).

Benign errors:
- Have Activity failure logs downgraded to DEBUG level
- Do not emit Activity failure metrics
- Do not set the OpenTelemetry failure status to ERROR

```csharp
using Temporalio.Activities;
using Temporalio.Api.Enums.V1;
using Temporalio.Exceptions;

public class MyActivities
{
    [Activity]
    public async Task<string> MyActivityAsync()
    {
        try
        {
            return await CallExternalServiceAsync();
        }
        catch (Exception e)
        {
            // Mark this error as benign since it's expected
            throw new ApplicationFailureException(
                "Service is down",
                inner: e,
                category: ApplicationErrorCategory.Benign);
        }
    }
}
```

Use benign exceptions for Activity errors that occur regularly as part of normal operations, such as polling an external service that isn't ready yet, or handling expected transient failures that will be retried.

---

## Dynamic Activity - .NET SDK

## Set a Dynamic Activity {/* #set-a-dynamic-activity */}

**How to set a Dynamic Activity using the Temporal .NET SDK**

A Dynamic Activity in Temporal is an Activity that is invoked dynamically at runtime if no other Activity with the same name is registered.
An Activity can be made dynamic by setting `Dynamic` as `true` on the `[Activity]` attribute.
You must register the Activity with the Worker before it can be invoked.
Only one Dynamic Activity can be present on a Worker.

The Activity Definition must then accept a single argument of type `Temporalio.Converters.IRawValue[]`.
The [PayloadConverter](https://dotnet.temporal.io/api/Temporalio.Activities.ActivityExecutionContext.html#Temporalio_Activities_ActivityExecutionContext_PayloadConverter) property on the `ActivityExecutionContext` is used to convert an `IRawValue` object to the desired type using extension methods in the `Temporalio.Converters` namespace.

```csharp
public class MyActivities
{
    [Activity(Dynamic = true)]
    public string DynamicActivity(IRawValue[] args)
    {
        var input = ActivityExecutionContext.Current.PayloadConverter.ToValue<MyActivityParams>(args.Single());
        return $"{input.Greeting}, {input.Name}!";
    }
}
```

---

## Activity execution - .NET SDK

## Start Activity Execution {/* #activity-execution */}

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

To spawn an Activity Execution, use the `ExecuteActivityAsync` operation from within your Workflow Definition.

```csharp
using Temporalio.Workflows;

[Workflow]
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

Activity Execution semantics rely on several parameters.
The only required value that needs to be set is either a [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout) or a [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout).
These values are set in the Activity Options.

### Get Activity Execution results {/* #get-activity-results */}

The Activity result is returned in the Task from the `ExecuteActivityAsync` call.

---

## Activities - .NET SDK

![.NET SDK Banner](/img/assets/banner-dotnet-temporal.png)

## Activities

- [Activity basics](/develop/dotnet/activities/basics)
- [Activity execution](/develop/dotnet/activities/execution)
- [Standalone Activities](/develop/dotnet/activities/standalone-activities)
- [Timeouts](/develop/dotnet/activities/timeouts)
- [Asynchronous Activity completion](/develop/dotnet/activities/asynchronous-activity)
- [Dynamic Activity](/develop/dotnet/activities/dynamic-activity)
- [Benign exceptions](/develop/dotnet/activities/benign-exceptions)

---

## Standalone Activities - .NET SDK

<ReleaseNoteHeader
  featureName="standaloneActivity"
/>

Standalone Activities are Activities that run independently, without being orchestrated by a
Workflow. Instead of starting an Activity from within a Workflow Definition, you start a Standalone
Activity directly from a Temporal Client.

The way you write the Activity and register it with a Worker is identical to [Workflow
Activities](/develop/dotnet/activities/basics#develop-activity). The only difference is that you execute a
Standalone Activity directly from your Temporal Client.

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

This documentation uses source code from the [StandaloneActivity](https://github.com/temporalio/samples-dotnet/tree/main/src/StandaloneActivity) sample project.

:::

## Get Started with Standalone Activities {/* #get-started */}

Prerequisites:

- **[.NET](https://dotnet.microsoft.com/download)** 8.0+

- **Temporal .NET SDK** (v1.12.0 or higher). See the [.NET Quickstart](https://docs.temporal.io/develop/dotnet/set-up-your-local-dotnet) for install instructions.

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

```bash
temporal server start-dev
```

This command automatically starts the Temporal development server with the Web UI, and creates the `default` Namespace.
It uses an in-memory database, so do not use it for real use cases.

:::info Temporal Cloud

All code samples on this page use
[`ClientEnvConfig.LoadClientConnectOptions()`](https://dotnet.temporal.io/api/Temporalio.Common.EnvConfig.ClientEnvConfig.html)
to configure the Temporal Client connection. It responds to [environment
variables](/references/client-environment-configuration) and [TOML configuration
files](/references/client-environment-configuration), so the same code works against a local dev
server and Temporal Cloud without changes. See [Run Standalone Activities with Temporal
Cloud](#run-standalone-activities-temporal-cloud) below.

:::

The Temporal Server will now be available for client connections on `localhost:7233`, and the
Temporal Web UI will now be accessible at [http://localhost:8233](http://localhost:8233). Standalone
Activities are available from the nav bar item located towards the top left of the page:

Clone the [samples-dotnet](https://github.com/temporalio/samples-dotnet) repository to follow along:

```
git clone https://github.com/temporalio/samples-dotnet.git
cd samples-dotnet
```

The sample project is structured as follows:

```
src/StandaloneActivity/
├── MyActivities.cs
├── Program.cs
├── README.md
└── TemporalioSamples.StandaloneActivity.csproj
```

## Define your Activity {/* #define-activity */}

An Activity in the Temporal .NET SDK is a method decorated with the `[Activity]` attribute. The way
you write a Standalone Activity is identical to how you write an Activity orchestrated by a Workflow.
In fact, the same Activity can be executed both as a Standalone Activity and as a Workflow Activity.

[src/StandaloneActivity/MyActivities.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/StandaloneActivity/MyActivities.cs)

```csharp
namespace TemporalioSamples.StandaloneActivity;

using Temporalio.Activities;

public static class MyActivities
{
    [Activity]
    public static Task<string> ComposeGreetingAsync(ComposeGreetingInput input) =>
        Task.FromResult($"{input.Greeting}, {input.Name}!");
}

public record ComposeGreetingInput(string Greeting, string Name);
```

## Run a Worker with the Activity registered {/* #run-worker */}

Running a Worker for Standalone Activities is the same as running a Worker for Workflow Activities —
you create a Worker, register the Activity, and run the Worker. The Worker doesn't need to know
whether the Activity will be invoked from a Workflow or as a Standalone Activity. See [How to develop
a Worker](/develop/dotnet/workers/run-worker-process) for more details on Worker setup and
configuration options.

[src/StandaloneActivity/Program.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/StandaloneActivity/Program.cs)

```csharp
using Microsoft.Extensions.Logging;
using Temporalio.Client;
using Temporalio.Common.EnvConfig;
using Temporalio.Worker;
using TemporalioSamples.StandaloneActivity;

var connectOptions = ClientEnvConfig.LoadClientConnectOptions();
connectOptions.TargetHost ??= "localhost:7233";
connectOptions.LoggerFactory = LoggerFactory.Create(builder =>
    builder.
        AddSimpleConsole(options => options.TimestampFormat = "[HH:mm:ss] ").
        SetMinimumLevel(LogLevel.Information));
var client = await TemporalClient.ConnectAsync(connectOptions);

const string taskQueue = "standalone-activity-sample";

using var tokenSource = new CancellationTokenSource();
Console.CancelKeyPress += (_, eventArgs) =>
{
    tokenSource.Cancel();
    eventArgs.Cancel = true;
};

using var worker = new TemporalWorker(
    client,
    new TemporalWorkerOptions(taskQueue).
        AddActivity(MyActivities.ComposeGreetingAsync));

await worker.ExecuteAsync(tokenSource.Token);
```

Open a new terminal, navigate to the `samples-dotnet` directory, and run the Worker:

```
dotnet run --project src/StandaloneActivity worker
```

Leave this terminal running - the Worker needs to stay up to process activities.

## Execute a Standalone Activity {/* #execute-activity */}

Use
[`client.ExecuteActivityAsync()`](https://dotnet.temporal.io/api/Temporalio.Client.ITemporalClientExtensions.html)
to execute a Standalone Activity and wait for the result. Call this from your application code, not
from inside a Workflow Definition. This durably enqueues your Standalone Activity in the Temporal
Server, waits for it to be executed on your Worker, and then returns the result.

[src/StandaloneActivity/Program.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/StandaloneActivity/Program.cs)

```csharp
using Temporalio.Client;
using Temporalio.Common.EnvConfig;
using TemporalioSamples.StandaloneActivity;

var connectOptions = ClientEnvConfig.LoadClientConnectOptions();
connectOptions.TargetHost ??= "localhost:7233";
var client = await TemporalClient.ConnectAsync(connectOptions);

var result = await client.ExecuteActivityAsync(
    () => MyActivities.ComposeGreetingAsync(new ComposeGreetingInput("Hello", "World")),
    new("standalone-activity-id", "standalone-activity-sample")
    {
        ScheduleToCloseTimeout = TimeSpan.FromSeconds(10),
    });
Console.WriteLine($"Activity result: {result}");
```

You can pass the Activity as either a lambda expression or a string Activity type name:

```csharp
// Using a lambda expression (type-safe)
var result = await client.ExecuteActivityAsync(
    () => MyActivities.ComposeGreetingAsync(new ComposeGreetingInput("Hello", "World")),
    new("standalone-activity-id", "standalone-activity-sample")
    {
        ScheduleToCloseTimeout = TimeSpan.FromSeconds(10),
    });

// Using a string type name
var result = await client.ExecuteActivityAsync<string>(
    "ComposeGreeting",
    new object?[] { new ComposeGreetingInput("Hello", "World") },
    new("standalone-activity-id", "standalone-activity-sample")
    {
        ScheduleToCloseTimeout = TimeSpan.FromSeconds(10),
    });
```

`StartActivityOptions` requires `Id`, `TaskQueue`, and at least one of `ScheduleToCloseTimeout` or
`StartToCloseTimeout`. See
[`StartActivityOptions`](https://dotnet.temporal.io/api/Temporalio.Client.StartActivityOptions.html)
in the API reference for the full set of options.

To run it:

1. Make sure the Temporal Server is running (from the [Get Started](#get-started) step above).
2. Make sure the Worker is running (from the [Run a Worker](#run-worker) step above).
3. Open a new terminal, navigate to the `samples-dotnet` directory, and run:

```
dotnet run --project src/StandaloneActivity execute-activity
```

Or use the Temporal CLI:

```bash
temporal activity execute \
  --type ComposeGreeting \
  --activity-id standalone-activity-id \
  --task-queue standalone-activity-sample \
  --schedule-to-close-timeout 10s \
  --input '{"Greeting": "Hello", "Name": "World"}'
```

## Start a Standalone Activity without waiting for the result {/* #start-activity */}

Use
[`client.StartActivityAsync()`](https://dotnet.temporal.io/api/Temporalio.Client.ITemporalClient.html)
to start a Standalone Activity and get a handle without waiting for the result:

[src/StandaloneActivity/Program.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/StandaloneActivity/Program.cs)

```csharp
using Temporalio.Client;
using Temporalio.Common.EnvConfig;
using TemporalioSamples.StandaloneActivity;

var connectOptions = ClientEnvConfig.LoadClientConnectOptions();
connectOptions.TargetHost ??= "localhost:7233";
var client = await TemporalClient.ConnectAsync(connectOptions);

var handle = await client.StartActivityAsync(
    () => MyActivities.ComposeGreetingAsync(new ComposeGreetingInput("Hello", "World")),
    new("standalone-activity-id", "standalone-activity-sample")
    {
        ScheduleToCloseTimeout = TimeSpan.FromSeconds(10),
    });
Console.WriteLine($"Started activity: {handle.Id}");

// Wait for the result later
var result = await handle.GetResultAsync();
Console.WriteLine($"Activity result: {result}");
```

With the Temporal Server and Worker running, open a new terminal in the `samples-dotnet` directory and run:

```
dotnet run --project src/StandaloneActivity start-activity
```

Or use the Temporal CLI:

```bash
temporal activity start \
  --type ComposeGreeting \
  --activity-id standalone-activity-id \
  --task-queue standalone-activity-sample \
  --schedule-to-close-timeout 10s \
  --input '{"Greeting": "Hello", "Name": "World"}'
```

## Get a handle to an existing Standalone Activity {/* #get-activity-handle */}

Use `client.GetActivityHandle()` to create a handle to a previously started Standalone Activity:

```csharp
// Without a known result type
var handle = client.GetActivityHandle("my-activity-id", runId: "the-run-id");

// With a known result type
var typedHandle = client.GetActivityHandle<string>("my-activity-id", runId: "the-run-id");
```

You can use the handle to wait for the result, describe, cancel, or terminate the Activity.

## Wait for the result of a Standalone Activity {/* #get-activity-result */}

Under the hood, calling `client.ExecuteActivityAsync()` is the same as calling
`client.StartActivityAsync()` to durably enqueue the Standalone Activity, and then calling
`await handle.GetResultAsync()` to wait for the Activity to be executed and return the result:

```csharp
var result = await handle.GetResultAsync();
```

Or use the Temporal CLI to wait for a result by Activity ID:

```bash
temporal activity result --activity-id my-standalone-activity-id
```

## List Standalone Activities {/* #list-activities */}

Use
[`client.ListActivitiesAsync()`](https://dotnet.temporal.io/api/Temporalio.Client.ITemporalClient.html)
to list Standalone Activity Executions that match a [List Filter](/list-filter) query. The result is
an `IAsyncEnumerable` that yields `ActivityExecution` entries.

These APIs return only Standalone Activity Executions. Activities running inside Workflows are not included.

[src/StandaloneActivity/Program.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/StandaloneActivity/Program.cs)

```csharp
using Temporalio.Client;
using Temporalio.Common.EnvConfig;

var connectOptions = ClientEnvConfig.LoadClientConnectOptions();
connectOptions.TargetHost ??= "localhost:7233";
var client = await TemporalClient.ConnectAsync(connectOptions);

await foreach (var info in client.ListActivitiesAsync(
    "TaskQueue = 'standalone-activity-sample'"))
{
    Console.WriteLine(
        $"ActivityID: {info.ActivityId}, Type: {info.ActivityType}, Status: {info.Status}");
}
```

Run it:

```
dotnet run --project src/StandaloneActivity list-activities
```

Or use the Temporal CLI:

```bash
temporal activity list
```

The query parameter accepts the same [List Filter](/list-filter) syntax used for [Workflow
Visibility](/visibility). For example, `"ActivityType = 'ComposeGreeting' AND Status = 'Running'"`.

## Count Standalone Activities {/* #count-activities */}

Use
[`client.CountActivitiesAsync()`](https://dotnet.temporal.io/api/Temporalio.Client.ITemporalClient.html)
to count Standalone Activity Executions that match a [List Filter](/list-filter) query. This returns
the total count of executions (running, completed, failed, etc.) - not the number of queued tasks.
It works the same way as counting Workflow Executions.

[src/StandaloneActivity/Program.cs](https://github.com/temporalio/samples-dotnet/blob/main/src/StandaloneActivity/Program.cs)

```csharp
using Temporalio.Client;
using Temporalio.Common.EnvConfig;

var connectOptions = ClientEnvConfig.LoadClientConnectOptions();
connectOptions.TargetHost ??= "localhost:7233";
var client = await TemporalClient.ConnectAsync(connectOptions);

var resp = await client.CountActivitiesAsync(
    "TaskQueue = 'standalone-activity-sample'");
Console.WriteLine($"Total activities: {resp.Count}");
```

Run it:

```
dotnet run --project src/StandaloneActivity count-activities
```

Or use the Temporal CLI:

```bash
temporal activity count
```

## Run Standalone Activities with Temporal Cloud {/* #run-standalone-activities-temporal-cloud */}

The code samples on this page use `ClientEnvConfig.LoadClientConnectOptions()`, so the same code
works against Temporal Cloud - just configure the connection via environment variables or a TOML
profile. No code changes are needed.

For a step-by-step guide on connecting to Temporal Cloud, including Namespace creation, certificate
generation, and authentication setup in the Cloud UI, see
[Connect to Temporal Cloud](/develop/dotnet/client/temporal-client#connect-to-temporal-cloud).

### Connect with mTLS

Set these environment variables with values from your Temporal Cloud Namespace settings:

```
export TEMPORAL_ADDRESS=<your-namespace>.<your-account-id>.tmprl.cloud:7233
export TEMPORAL_NAMESPACE=<your-namespace>.<your-account-id>
export TEMPORAL_TLS_CLIENT_CERT_PATH='path/to/your/client.pem'
export TEMPORAL_TLS_CLIENT_KEY_PATH='path/to/your/client.key'
```

### Connect with an API key

Set these environment variables with values from your Temporal Cloud API key settings:

```
export TEMPORAL_ADDRESS=<region>.<cloud_provider>.api.temporal.io:7233
export TEMPORAL_NAMESPACE=<your-namespace>.<your-account-id>
export TEMPORAL_API_KEY=<your-api-key>
```

Then run the Worker and starter code as shown in the earlier sections.

---

## Activity Timeouts - .NET SDK

## Activity Timeouts {/* #activity-timeouts */}

Each Activity Timeout controls the maximum duration of a different aspect of an Activity Execution.

The following Timeouts are available in the Activity Options.

- **[Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout):** is the maximum amount of time allowed for the overall [Activity Execution](/activity-execution).
- **[Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout):** is the maximum time allowed for a single [Activity Task Execution](/tasks#activity-task-execution).
- **[Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout):** is the maximum amount of time that is allowed from when an [Activity Task](/tasks#activity-task) is scheduled to when a [Worker](/workers#worker) starts that Activity Task.

An Activity Execution must have either the Start-To-Close or the Schedule-To-Close Timeout set.

These values can be set in the `ActivityOptions` when calling `ExecuteActivityAsync`.

Available timeouts are:

- ScheduleToCloseTimeout
- ScheduleToStartTimeout
- StartToCloseTimeout

```csharp
return await Workflow.ExecuteActivityAsync(
    (MyActivities a) => a.MyActivity(param),
    new() { StartToCloseTimeout = TimeSpan.FromMinutes(5) });
```

### Set an Activity Retry Policy {/* #activity-retries */}

A Retry Policy works in cooperation with the timeouts to provide fine controls to optimize the execution experience.

Activity Executions are automatically associated with a default [Retry Policy](/encyclopedia/retry-policies) if a custom one is not provided.

To create an Activity Retry Policy in .NET, set the `RetryPolicy` on the `ActivityOptions` when calling `ExecuteActivityAsync`.

```csharp
return await Workflow.ExecuteActivityAsync(
    (MyActivities a) => a.MyActivity(param),
    new()
    {
        StartToCloseTimeout = TimeSpan.FromMinutes(5),
        RetryPolicy = new() { MaximumInterval = TimeSpan.FromSeconds(10) },
    });
```

### Override the Retry interval with `nextRetryDelay` {/* #next-retry-delay */}

When you throw an [Application Failure](/references/failures#application-failure) and assign the `nextRetryDelay` field, its value replaces and overrides the Retry interval defined in the active Retry Policy.

For example, you might scale the next Retry delay interval based on the current number of attempts.
Here's how you'd do that in an Activity.
In the following sample, the `attempt` count is retrieved from the Activity Execution context and used to set the number of seconds for the next Retry delay:

```csharp
var attempt = ActivityExecutionContext.Current.Info.Attempt;

throw new ApplicationFailureException(
    $"Something bad happened on attempt {attempt}",
    errorType: "my_failure_type",
    nextRetryDelay: TimeSpan.FromSeconds(3 * attempt));
```

## Heartbeat an Activity {/* #activity-heartbeats */}

An [Activity Heartbeat](/encyclopedia/detecting-activity-failures#activity-heartbeat) is a ping from the [Worker Process](/workers#worker-process) that is executing the Activity to the [Temporal Service](/temporal-service).
Each Heartbeat informs the Temporal Service that the [Activity Execution](/activity-execution) is making progress and the Worker has not crashed.
If the Temporal Service does not receive a Heartbeat within a [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) time period, the Activity will be considered failed and another [Activity Task Execution](/tasks#activity-task-execution) may be scheduled according to the Retry Policy.

Heartbeats may not always be sent to the Temporal Service—they may be [throttled](/encyclopedia/detecting-activity-failures#throttling) by the Worker.

Activity Cancellations are delivered to Activities from the Temporal Service when they Heartbeat. Activities that don't Heartbeat can't receive a Cancellation.
