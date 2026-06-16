# Install Temporal SDK in each project
dotnet add Workflow/Workflow.csproj package Temporalio
dotnet add Worker/Worker.csproj package Temporalio
dotnet add Client/Client.csproj package Temporalio`
}
      </CodeSnippet>

Build the solution:

      <CodeSnippet language="bash">{`dotnet build`}</CodeSnippet>
    </>
  }>
    ## Install the Temporal .NET SDK

    Create a solution and the three projects used in this guide: `Workflow` (class library), `Worker` (console), and `Client` (console). Add them to the solution.

    Tip: You can also centralize the `Temporalio` package for all projects using `Directory.Packages.props` and `Directory.Build.props` at the solution root.
  </SetupStep>

  <SetupStep code={
    <>
      <Tabs>
        <TabItem value="macos" label="macOS" default>
          Install the Temporal CLI using Homebrew:
          <CodeSnippet language="bash">{`brew install temporal`}</CodeSnippet>
        </TabItem>
        <TabItem value="windows" label="Windows">
          Download the Temporal CLI archive for your architecture:

            Windows amd64
            Windows arm64

          Extract it and add <code>temporal.exe</code> to your PATH.
        </TabItem>
        <TabItem value="linux" label="Linux">
          Download the Temporal CLI for your architecture:

            Linux amd64
            Linux arm64

          Extract the archive and move the <code>temporal</code> binary into your PATH, for example:
          <CodeSnippet language="bash">{`sudo mv temporal /usr/local/bin`}</CodeSnippet>
        </TabItem>
      </Tabs>
    </>
  }>
    ## Install Temporal CLI and start the development server

    The fastest way to get a development version of the Temporal Service running on your local machine is to use [Temporal CLI](https://docs.temporal.io/cli).

    Choose your operating system to install Temporal CLI:
  </SetupStep>

  <SetupStep code={
    <>
      After installing, open a new Terminal window and start the development server:
      <CodeSnippet language="bash">{`temporal server start-dev`}</CodeSnippet>

        Change the Web UI port

          The Temporal Web UI may be on a different port in some examples or tutorials.
          To change the <code>--ui-port</code> option when starting the server:

        <CodeSnippet language="bash">{`temporal server start-dev --ui-port 8080`}</CodeSnippet>

          The Temporal Web UI will now be available at http://localhost:8080.

    </>
  }>
    ## Start the development server

    Once you've installed Temporal CLI and added it to your PATH, open a new Terminal window and run the following command.

    This command starts a local Temporal Service. It starts the Web UI, creates the default Namespace, and uses an in-memory database.

    The Temporal Service will be available on localhost:7233.
    The Temporal Web UI will be available at http://localhost:8233.

    Leave the local Temporal Service running as you work through tutorials and other projects. You can stop the Temporal Service at any time by pressing CTRL+C.

    Once you have everything installed, you're ready to build apps with Temporal on your local machine.
  </SetupStep>
</SetupSteps>

## Run Hello World: Test Your Installation

Now let's verify your setup is working by creating and running a complete Temporal application with both a Workflow and Activity.

This test will confirm that:

- Your .NET SDK installation is working
- Your local Temporal Service is running
- You can successfully create and execute Workflows and Activities
- The communication between components is functioning correctly

<details>
  <summary>Tip: Example Directory Structure</summary>

```text
TemporalioHelloWorld/
├── Client/
│   ├── Client.csproj
│   └── Program.cs              # Starts a workflow
├── Worker/
│   ├── Worker.csproj
│   └── Program.cs              # Runs a worker
├── Workflow/
│   ├── Workflow.csproj
│   ├── MyActivities.cs         # Activity definition
│   └── SayHelloWorkflow.cs     # Workflow definition
└── TemporalioHelloWorld.sln
```

</details>

### 1. Create the Activity and Workflow

#### Create an Activity file (MyActivities.cs) in the Workflow project:

```csharp
namespace MyNamespace;

using Temporalio.Activities;

public class MyActivities
{
    // Activities can be async and/or static too! We just demonstrate instance
    // methods since many will use them that way.
    [Activity]
    public string SayHello(string name) => $"Hello, {name}!";
}
```

An Activity is a normal function or method that executes a single, well-defined action (either short or long running), which often involve interacting with the outside world, such as sending emails, making network requests, writing to a database, or calling an API, which are prone to failure.
If an Activity fails, Temporal automatically retries it based on your configuration.

#### Create a Workflow file (SayHelloWorkflow.cs) in the Workflow project:

```csharp
namespace MyNamespace;

using Temporalio.Workflows;

[Workflow]
public class SayHelloWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync(string name)
    {
        // This workflow just runs a simple activity to completion.
        // StartActivityAsync could be used to just start and there are many
        // other things that you can do inside a workflow.
        return await Workflow.ExecuteActivityAsync(
            // This is a lambda expression where the instance is typed. If this
            // were static, you wouldn't need a parameter.
            (MyActivities act) => act.SayHello(name),
            new() { StartToCloseTimeout = TimeSpan.FromMinutes(5) }
        );
    }
}
```

Workflows orchestrate Activities and contain the application logic.
Temporal Workflows are resilient.
They can run and keep running for years, even if the underlying infrastructure fails.
If the application itself crashes, Temporal will automatically recreate its pre-failure state so it can continue right where it left off.

### 2. Create the Worker

With your Activity and Workflow defined, you need a Worker to execute them.

#### Create a Worker file (Program.cs) in the Worker project:

```csharp
using MyNamespace;
using Temporalio.Client;
using Temporalio.Worker;

// Create a client to localhost on "default" namespace
var client = await TemporalClient.ConnectAsync(new("localhost:7233"));

// Cancellation token to shutdown worker on ctrl+c
using var tokenSource = new CancellationTokenSource();
Console.CancelKeyPress += (_, eventArgs) =>
{
    tokenSource.Cancel();
    eventArgs.Cancel = true;
};

// Create an activity instance since we have instance activities. If we had
// all static activities, we could just reference those directly.
var activities = new MyActivities();

// Create worker with the activity and workflow registered
using var worker = new TemporalWorker(
    client,
    new TemporalWorkerOptions("my-task-queue")
        .AddActivity(activities.SayHello)
        .AddWorkflow<SayHelloWorkflow>()
);

// Run worker until cancelled
Console.WriteLine("Running worker");
try
{
    await worker.ExecuteAsync(tokenSource.Token);
}
catch (OperationCanceledException)
{
    Console.WriteLine("Worker cancelled");
}
```

Run the Worker:

```bash
dotnet run --project Worker/Worker.csproj
```
Keep this terminal running - you should see `Running worker` displayed.

A Worker polls a Task Queue, that you configure it to poll, looking for work to do.
Once the Worker dequeues the Workflow or Activity task from the Task Queue, it then executes that task.

Workers are a crucial part of your Temporal application as they're what actually execute the tasks defined in your Workflows and Activities.
For more information on Workers, see [Understanding Temporal](/evaluate/understanding-temporal#workers) and a [deep dive into Workers](/workers).

### 3. Execute the Workflow

Now that your Worker is running, it's time to start a Workflow Execution.
This final step will validate that everything is working correctly.

#### Create a Client file (Program.cs) in the Client project:

```csharp
using MyNamespace;
using Temporalio.Client;

// Create a client to localhost on "default" namespace
var client = await TemporalClient.ConnectAsync(new("localhost:7233"));

// Run workflow
var result = await client.ExecuteWorkflowAsync(
    (SayHelloWorkflow wf) => wf.RunAsync("Temporal"),
    new(id: $"my-workflow-id-{Guid.NewGuid()}", taskQueue: "my-task-queue")
);

Console.WriteLine("Workflow result: {0}", result);
```

While the Worker is still running, run the Workflow:

```bash
dotnet run --project Client/Client.csproj
```

### Verify Success

If everything is working correctly, you should see:

- Worker processing the workflow and activity
- Output: `Workflow result: Hello Temporal`
- Workflow Execution details in the [Temporal Web UI](http://localhost:8233)

<CallToAction href="https://learn.temporal.io/getting_started/dotnet/first_program_in_dotnet/">
  Run your first Temporal Application
  Create a basic Workflow and run it with the Temporal .NET SDK
</CallToAction>

<CallToAction href="https://learn.temporal.io/courses/">
  Take a Temporal 101 course
  Learn Temporal concepts and build your first application with a guided course
</CallToAction>

---

## Workers - .NET SDK

![.NET SDK Banner](/img/assets/banner-dotnet-temporal.png)

## Workers

- [Worker processes](/develop/dotnet/workers/run-worker-process)
- [Interceptors](/develop/dotnet/workers/interceptors)

---

## Interceptors - .NET SDK

Interceptors are SDK hooks that let you intercept inbound and outbound Temporal calls. You use them to apply shared
behavior across many calls, such as tracing and authorization, before calls reach the application code and after they return.
This is similar to middleware in other frameworks, like [ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware).

There are two main types of interceptors: inbound and outbound.

* Outbound interceptors wrap network calls, running before they reach the network and after they return.
* Inbound interceptors run after the network hop, wrapping application code and running before it starts and after it returns.

Concretely, there are five categories of inbound and outbound calls that you can modify in this way:

| | [Outbound Client](https://dotnet.temporal.io/api/Temporalio.Client.Interceptors.ClientOutboundInterceptor.html) | [Inbound Workflow](https://dotnet.temporal.io/api/Temporalio.Worker.Interceptors.WorkflowInboundInterceptor.html) | [Outbound Workflow](https://dotnet.temporal.io/api/Temporalio.Worker.Interceptors.WorkflowOutboundInterceptor.html) | [Inbound Activity](https://dotnet.temporal.io/api/Temporalio.Worker.Interceptors.ActivityInboundInterceptor.html) | [Outbound Activity](https://dotnet.temporal.io/api/Temporalio.Worker.Interceptors.ActivityOutboundInterceptor.html) |
| --- | --- | --- | --- | --- | --- |
| **Description** | Wraps calls from your application to the Temporal Client to start a Workflow or send [Messages](/encyclopedia/workflow-message-passing/) to it | Wraps calls arriving into a [Workflow Execution](/workflow-execution), such as executing the Workflow, handling [Messages](/encyclopedia/workflow-message-passing/) | Wraps calls a [Workflow](/workflow-definition) makes to the SDK, such as scheduling [Activities](/activities), starting [Child Workflows](/child-workflows), and invoking [Nexus Operations](/nexus) | Wraps calls arriving into an [Activity Execution](/activity-execution) | Wraps calls an [Activity](/activities) makes to the SDK, such as sending [Heartbeats](/encyclopedia/detecting-activity-failures#activity-heartbeat) and reading Activity info |
| **Runs on** | Client | Worker (Workflow sandbox) | Worker (Workflow sandbox) | Worker (Activity context) | Worker (Activity context) |
| **Example methods** | `StartWorkflowAsync()`, `WorkflowHandle.SignalAsync()`, `ListWorkflowsAsync()` | `ExecuteWorkflowAsync()`, `WorkflowHandle.QueryAsync()`, `WorkflowHandle.SignalAsync ()`, `WorkflowHandle.ExecuteUpdateAsync()` | `StartActivityAsync()`, `StartChildWorkflowAsync()`, `ChildWorkflowHandle.SignalAsync()`, `StartNexusOperationAsync()` | `ExecuteActivityAsync()` | `Info()`, `Heartbeat()` |

:::warning Workflow interceptors and replay

Workflow inbound and outbound interceptor methods also execute during [replay](/develop/dotnet/best-practices/testing-suite#replay). Use replay-safe APIs for logging, randomness, and time in these interceptors.
See [Develop Workflow logic](/develop/dotnet/workflows/basics#workflow-logic-requirements) for details.

If you want to write generic code shared by all inbound Workflow call handlers but want to skip read-only operations, check [`Workflow.Unsafe.IsReplaying`](https://dotnet.temporal.io/api/Temporalio.Workflows.Workflow.Unsafe.html#Temporalio_Workflows_Workflow_Unsafe_IsReplaying).

Activity and Client interceptors are not affected by replay.

:::

## Register an Interceptor {/* #register */}

Registering an interceptor means supplying an interceptor instance to the SDK so Temporal can invoke it when matching
Client or Worker calls occur. Once registered, the interceptor runs as part of the call path and can observe or modify
request and response data.

### Register on the Client

Pass interceptors in the `Interceptors` property of [`TemporalClientConnectOptions`](https://dotnet.temporal.io/api/Temporalio.Client.TemporalClientConnectOptions.html). Client interceptors modify outbound calls such
as starting and signaling Workflows. One example is [setting up tracing](/develop/dotnet/platform/observability) to see your call graph of a Workflow.

```csharp
using Temporalio.Extensions.OpenTelemetry;

var interceptor = new TracingInterceptor();

var client = await TemporalClient.ConnectAsync(new()
{
    TargetHost = "localhost:7233",
    Interceptors = [interceptor],
});
```

The `Interceptors` list can contain multiple interceptors.
The default behavior for interceptors is to form a chain. A method implemented on an interceptor instance in the list can perform side effects, and modify the data, before passing it on to the corresponding method on the next interceptor in the list.

### Register via a Plugin

If you're building a reusable library or want to bundle interceptors with other primitives, you can register them through a [Plugin](/develop/plugins-guide#interceptors).

### Register on the Worker only

If your interceptor doesn't affect the Client, you can pass interceptors in the `Interceptors` argument of `TemporalWorkerOptions`.
Worker interceptors modify inbound and outbound Workflow and Activity calls.

```csharp
using var worker = new TemporalWorker(
    client,
    new TemporalWorkerOptions("my-task-queue")
    {
        Interceptors = [interceptor]
    }
    .AddActivity(activities.SayHello)
    .AddWorkflow<SayHelloWorkflow>()
);
```

## How to implement Interceptors

Interceptors run as a chain.  Each interceptor wraps the entire inner call: your code runs before the call, invokes `next` to execute the rest of the chain, and then runs after the call completes. This means you can inspect or modify both the `input` and the result, handle errors, and perform side effects at either stage.

### Implementing Client call Interceptors

To modify outbound Client calls, define a class implementing [`IClientInterceptor`](https://dotnet.temporal.io/api/Temporalio.Client.Interceptors.IClientInterceptor.html). Implement `InterceptClient()` to return a [`ClientOutboundInterceptor`](https://dotnet.temporal.io/api/Temporalio.Client.Interceptors.ClientOutboundInterceptor.html), overriding the outbound Client calls you want to modify. `IClientInterceptor.InterceptClient` receives the next `ClientOutboundInterceptor` in the chain and returns the created interceptor.

This example implements an Interceptor on outbound Client calls that sets a certain key in the outbound `headers` field.
A User ID is context-propagated by being sent in a header field with outbound requests:

```csharp
using Google.Protobuf;
using Temporalio.Api.Common.V1;
using Temporalio.Client;
using Temporalio.Client.Interceptors;

public static class UserContext
{
    private static readonly AsyncLocal<string?> CurrentUser = new();

    public static string? UserId
    {
        get => CurrentUser.Value;
        set => CurrentUser.Value = value;
    }
}

public class ContextPropagationInterceptor : IClientInterceptor
{
    public ClientOutboundInterceptor InterceptClient(
        ClientOutboundInterceptor nextInterceptor) =>
        new ContextPropagationClientOutboundInterceptor(nextInterceptor);
}

public class ContextPropagationClientOutboundInterceptor(
    ClientOutboundInterceptor next)
    : ClientOutboundInterceptor(next)
{
    public override Task<WorkflowHandle<TWorkflow, TResult>>
        StartWorkflowAsync<TWorkflow, TResult>(StartWorkflowInput input)
    {
        var headers = input.Headers ?? new Dictionary<string, Payload>();
        headers["user-id"] = new Payload
        {
            Metadata = { ["encoding"] = ByteString.CopyFromUtf8("plain/text") },
            Data = ByteString.CopyFromUtf8(UserContext.UserId),
        };

        return base.StartWorkflowAsync<TWorkflow, TResult>(input with { Headers = headers });
    }
}
```

You can then [register](#register) this interceptor in your client/starter code.

Your interceptor classes don't need to implement every method. The default implementation is always to pass the data on to the next method in the interceptor chain.
During execution, when the SDK encounters an Inbound Activity call, it will look to the first Interceptor instance, get hold of the appropriate intercepted method, and call it.
The intercepted method will perform its function then call the same method on the next Interceptor in the chain.
At the end of the chain the SDK will call the "real" SDK method.

### Implementing Worker call Interceptors

To modify inbound Workflow and Activity calls, define a class implementing [`IWorkerInterceptor`](https://dotnet.temporal.io/api/Temporalio.Worker.Interceptors.IWorkerInterceptor.html). It provides `InterceptActivity()`, `InterceptWorkflow()`, and `InterceptNexusOperation()` methods for Activity, Workflow, and Nexus interception.

This example demonstrates using an interceptor to measure [Schedule-To-Start](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout) and Schedule-To-Close latency.
Notice how the interceptor wraps the call. It records Schedule-To-Start before `ExecuteActivityAsync`, then records Schedule-To-Close after it completes:

```csharp
using Temporalio.Activities;
using Temporalio.Worker;
using Temporalio.Worker.Interceptors;

public class SimpleWorkerInterceptor : IWorkerInterceptor
{
    public ActivityInboundInterceptor InterceptActivity(
        ActivityInboundInterceptor nextInterceptor) =>
        new ActivityMetricsInterceptor(nextInterceptor);

    public WorkflowInboundInterceptor InterceptWorkflow(
        WorkflowInboundInterceptor nextInterceptor) =>
        nextInterceptor;

    public NexusOperationInboundInterceptor InterceptNexusOperation(
        NexusOperationInboundInterceptor nextInterceptor) =>
        nextInterceptor;
}

public class ActivityMetricsInterceptor(ActivityInboundInterceptor next)
    : ActivityInboundInterceptor(next)
{
    public override async Task<object?> ExecuteActivityAsync(
        ExecuteActivityInput input)
    {
        var info = ActivityExecutionContext.Current.Info;
        var started = DateTimeOffset.UtcNow;

        // Before the activity executes
        var scheduleToStart =
            started - info.CurrentAttemptScheduledTime;

        Console.WriteLine(
            $"Schedule-To-Start latency: {scheduleToStart}");

        // Execute the activity
        var result = await base.ExecuteActivityAsync(input);

        // After the activity completes
        var scheduleToClose =
            DateTimeOffset.UtcNow - info.CurrentAttemptScheduledTime;

        Console.WriteLine(
            $"Schedule-To-Close latency: {scheduleToClose}");

        return result;
    }
}
```

Register it on the Worker:

```csharp
using var worker = new TemporalWorker(
    client,
    new TemporalWorkerOptions("my-task-queue")
    {
        Interceptors = new IWorkerInterceptor[]
        {
            new SimpleWorkerInterceptor(),
        },
    }
    .AddActivity(activities.SayHello)
    .AddWorkflow<SayHelloWorkflow>());

await worker.ExecuteAsync();
```

---

## Worker processes - .NET SDK

## Run Worker Process

**How to create and run a Worker Process using the Temporal .NET SDK**

The [Worker Process](/workers#worker-process) is where Workflow Functions and Activity Functions are executed.

- Each [Worker Entity](/workers#worker-entity) in the Worker Process must register the exact Workflow Types and Activity Types it may execute.
- Each Worker Entity must also associate itself with exactly one [Task Queue](/task-queue).
- Each Worker Entity polling the same Task Queue must be registered with the same Workflow Types and Activity Types.

A [Worker Entity](/workers#worker-entity) is the component within a Worker Process that listens to a specific Task Queue.

Although multiple Worker Entities can be in a single Worker Process, a single Worker Entity Worker Process may be perfectly sufficient.
For more information, see the [Worker tuning guide](/develop/worker-performance).

A Worker Entity contains a Workflow Worker and/or an Activity Worker, which makes progress on Workflow Executions and Activity Executions, respectively.

To develop a Worker, create a new `Temporalio.Worker.TemporalWorker` providing the Client and worker options which include Task Queue, Workflows, and Activities and more.
The following code example creates a Worker that polls for tasks from the Task Queue and executes the Workflow.
When a Worker is created, it accepts a list of Workflows, a list of Activities, or both.

```csharp
// Create a client to localhost on default namespace
var client = await TemporalClient.ConnectAsync(new("localhost:7233")
{
    LoggerFactory = LoggerFactory.Create(builder =>
        builder.
            AddSimpleConsole(options => options.TimestampFormat = "[HH:mm:ss] ").
            SetMinimumLevel(LogLevel.Information)),
});

// Cancellation token cancelled on ctrl+c
using var tokenSource = new CancellationTokenSource();
Console.CancelKeyPress += (_, eventArgs) =>
{
    tokenSource.Cancel();
    eventArgs.Cancel = true;
};

// Create an activity instance with some state
var activities = new MyActivities();

// Run worker until cancelled
Console.WriteLine("Running worker");
using var worker = new TemporalWorker(
    client,
    new TemporalWorkerOptions(taskQueue: "my-task-queue").
        AddAllActivities(activities).
        AddWorkflow<MyWorkflow>());
try
{
    await worker.ExecuteAsync(tokenSource.Token);
}
catch (OperationCanceledException)
{
    Console.WriteLine("Worker cancelled");
}
```

All Workers listening to the same Task Queue name must be registered to handle the exact same Workflows Types and Activity Types.

If a Worker polls a Task for a Workflow Type or Activity Type it does not know about, it fails that Task.
However, the failure of the Task does not cause the associated Workflow Execution to fail.

### Worker Processes with host builder and dependency injection

The [Temporalio.Extensions.Hosting](https://github.com/temporalio/sdk-dotnet/tree/main/src/Temporalio.Extensions.Hosting) extension exists for .NET developers to support HostBuilder and Dependency Injection approaches.

To create the same worker as before using this approach:

```csharp
var host = Host.CreateDefaultBuilder(args)
    .ConfigureLogging(ctx => ctx.AddSimpleConsole().SetMinimumLevel(LogLevel.Information))
    .ConfigureServices(ctx =>
        ctx.
            // Add the database client at the scoped level
            AddScoped<IMyDatabaseClient, MyDatabaseClient>().
            // Add the worker
            AddHostedTemporalWorker(
                clientTargetHost: "localhost:7233",
                clientNamespace: "default",
                taskQueue: "my-task-queue").
            // Add the activities class at the scoped level
            AddScopedActivities<MyActivities>().
            AddWorkflow<MyWorkflow>())
    .Build();
await host.RunAsync();
```

---

## Workflow basics - .NET SDK

## Develop a Workflow {/* #develop-workflow */}

Workflows are the fundamental unit of a Temporal Application, and it all starts with the development of a [Workflow Definition](/workflow-definition).

In the Temporal .NET SDK programming model, Workflows are defined as classes.

Specify the `[Workflow]` attribute from the `Temporalio.Workflows` namespace on the Workflow class to identify a Workflow.

Use the `[WorkflowRun]` attribute to mark the entry point method to be invoked. This must be set on one asynchronous method defined on the same class as `[Workflow]`.

```csharp
using Temporalio.Workflows;

[Workflow]
public class MyWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync(string name)
    {
        var param = MyActivityParams("Hello", name);
        return await Workflow.ExecuteActivityAsync(
            (MyActivities a) => a.MyActivity(param),
            new() { StartToCloseTimeout = TimeSpan.FromMinutes(5) });
    }
}
```

Temporal Workflows may have any number of custom parameters.
However, we strongly recommend that objects are used as parameters, so that the object's individual fields may be altered without breaking the signature of the Workflow.
All Workflow Definition parameters must be serializable.

## Workflow logic requirements {/* #workflow-logic-requirements */}

Workflow logic is constrained by [deterministic execution requirements](/workflow-definition#deterministic-constraints). Each Temporal SDK provides a set of APIs that can be used inside your Workflow to interact with application code outside the Workflow.

This means there are several things Workflows shouldn't do such as:

- Perform IO (network, disk, stdio, etc)
- Access/alter external mutable state
- Do any threading
- Do anything using the system clock (e.g. `DateTime.Now`)
  - This includes .NET timers (e.g. `Task.Delay` or `Thread.Sleep`)
- Make any random calls
- Make any not-guaranteed-deterministic calls (e.g. iterating over a dictionary)

### .NET Task Determinism

Some calls in .NET do unsuspecting non-deterministic things and are easy to accidentally use.
This is especially true with `Task`s.
Temporal requires that the deterministic `TaskScheduler.Current` is used, but many .NET async calls will use `TaskScheduler.Default` implicitly (and some analyzers even encourage this).
Here are some known gotchas to avoid with .NET tasks inside of Workflows:

-  Use `Workflow.RunTaskAsync` instead of `Task.Run`. `Task.Run` uses the default scheduler and puts work on the thread pool.
    - You can also use `Task.Factory.StartNew` with current scheduler or instantiate the `Task` and run `Task.Start` on it.
- If you need to use `Task.ConfigureAwait`, use `Task.ConfigureAwait(true)`. `Task.ConfigureAwait(false)` won't use the current context.
  - There is no significant performance benefit to `Task.ConfigureAwait` in workflows because of how the scheduler works.
- Avoid anything that defaults to the default task scheduler.
- Use `Workflow.DelayAsync`, `Workflow.WaitConditionAsync`, or non-timeout-based cancellation token sources instead of `Task.Delay`, `Task.Wait`, timeout-based `CancellationTokenSource`, or anything that uses .NET built-in timers.
- Use `Workflow.WhenAnyAsync` instead of `Task.WhenAny`.
  - Technically this only applies to an enumerable set of tasks with results or more than 2 tasks with results. Other
    uses are safe. See [this issue](https://github.com/dotnet/runtime/issues/87481).
- Use `Workflow.WhenAllAsync` instead of `Task.WhenAll`.
  - Technically `Task.WhenAll` is currently deterministic in .NET and safe, but it is better to use the wrapper to be
    sure.
- Use `CancellationTokenSource.Cancel` instead of `CancellationTokenSource.CancelAsync`.
- Use `Temporalio.Workflows.Semaphore` or `Temporalio.Workflows.Mutex` instead of `System.Threading.Semaphore`, `System.Threading.SemaphoreSlim`, or `System.Threading.Mutex`.
  - _Technically_ `SemaphoreSlim` does work if only the async form of `WaitAsync` is used without no timeouts and
    `Release` is used. But anything else can deadlock the workflow and its use is cumbersome since it must be disposed.
- Be wary of additional libraries' implicit use of the default scheduler.
  - For example, while there are articles for `Dataflow` about [using a specific scheduler](https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/how-to-specify-a-task-scheduler-in-a-dataflow-block), there are hidden implicit uses of `TaskScheduler.Default`. For example, see [this bug](https://github.com/dotnet/runtime/issues/83159).

In order to help catch wrong scheduler use, by default the Temporal .NET SDK adds an event source listener for info-level task events.
While this technically receives events from all uses of tasks in the process, we make sure to ignore anything that is not running in a Workflow in a high performant way (basically one thread local check).

For code that does run in a Workflow and accidentally starts a task in another scheduler, an `InvalidWorkflowOperationException` will be thrown which "pauses" the Workflow (fails the Workflow Task which continually retries until the code is fixed).
This is unfortunately a runtime-only check, but can help catch mistakes early. If this needs to be turned off for any reason, set `DisableWorkflowTracingEventListener` to `true` in Worker options.

In the near future for modern .NET versions we hope to use the
[new `TimeProvider` API](https://github.com/dotnet/runtime/issues/36617) which will allow us to control current time and
timers.

### Workflow .editorconfig

Since Workflow code follows some different logic rules than regular C# code, there are some common analyzer rules that developers may want to disable.
To ensure these are only disabled for Workflows, current recommendation is to use the `.workflow.cs` extension for files containing Workflows.

Here are the rules to disable:

- [CA1024](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca1024) - This encourages properties instead of methods that look like getters. However for reflection reasons we cannot use property getters for queries, so it is very normal to have

  ```csharp
  [WorkflowQuery]
  public string GetSomeThing() => someThing;
  ```

- [CA1822](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca1822) - This encourages static methods when methods don't access instance state. Workflows however use instance methods for run, Signals, Queries, or Updates even if they could be static.
- [CA2007](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2007) - This encourages users to use `ConfigureAwait` instead of directly waiting on a task. But in Workflows, there is no benefit to this and it just adds noise (and if used, needs to be `ConfigureAwait(true)` not `ConfigureAwait(false)`).
- [CA2008](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca2008) - This encourages users to always apply an explicit task scheduler because the default of `TaskScheduler.Current` is bad. But for Workflows, the default of `TaskScheduler.Current` is good/required.
- [CA5394](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/quality-rules/ca5394) - This discourages use of non-crypto random. But deterministic Workflows, via `Workflow.Random` intentionally provide a deterministic non-crypto random instance.
- `CS1998` - This discourages use of `async` on async methods that don't `await`. But Workflows handlers like Signals are often easier to write in one-line form this way, e.g. `public async Task SignalSomethingAsync(string value) => this.value = value;`.
- [VSTHRD105](https://github.com/microsoft/vs-threading/blob/main/doc/analyzers/VSTHRD105.md) - This is similar to `CA2008` above in that use of implicit current scheduler is discouraged. That does not apply to Workflows where it is encouraged/required.

Here is the `.editorconfig` snippet for the above which may frequently change as more analyzers need to be adjusted:

```ini
##### Configuration specific for Temporal workflows #####
[*.workflow.cs]
