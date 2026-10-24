Heartbeat throttling may lead to Cancellation getting delivered later than expected.

Heartbeats can contain a `Details` field describing the Activity's current progress.
If an Activity gets retried, the Activity can access the `Details` from the last Heartbeat that was sent to the Temporal Service.

To Heartbeat an Activity Execution in .NET, use the [`Heartbeat()`](https://dotnet.temporal.io/api/Temporalio.Activities.ActivityExecutionContext.html#Temporalio_Activities_ActivityExecutionContext_Heartbeat_System_Object___) method on the `ActivityExecutionContext`.

```csharp
[Activity]
public async Task MyActivityAsync()
{
    while (true)
    {
        // Send heartbeat
        ActivityExecutionContext.Current.Heartbeat();

        // Do some work, passing the cancellation token
        await Task.Delay(1000, ActivityExecutionContext.Current.CancellationToken);
    }
}
```

In addition to obtaining cancellation information, Heartbeats also support detail data that persists on the server for retrieval during Activity retry.
If an Activity calls `Heartbeat(123, 456)` and then fails and is retried, `HeartbeatDetails` on the `ActivityInfo` returns an collection containing `123` and `456` on the next Run.

### Set a Heartbeat Timeout {/* #heartbeat-timeout */}

A [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) works in conjunction with [Activity Heartbeats](/encyclopedia/detecting-activity-failures#activity-heartbeat).

`HeartbeatTimeout` is a property on `ActivityOptions` for `ExecuteActivityAsync` used to set the maximum time between Activity Heartbeats.

```csharp
await Workflow.ExecuteActivityAsync(
    (MyActivities a) => a.MyActivity(param),
    new()
    {
        StartToCloseTimeout = TimeSpan.FromMinutes(5),
        HeartbeatTimeout = TimeSpan.FromSeconds(30),
    });
```

---

## Converters and encryption - .NET SDK

Temporal's security model is designed around client-side encryption of Payloads.
A client may encrypt Payloads before sending them to the server, and decrypt them after receiving them from the server.
This provides a high degree of confidentiality because the Temporal Server itself has absolutely no knowledge of the actual data.
It also gives implementers more power and more freedom regarding which client is able to read which data -- they can control access with keys, algorithms, or other security measures.

A Temporal developer adds client-side encryption of Payloads by providing a Custom Payload Codec to its Client.
Depending on business needs, a complete implementation of Payload Encryption may involve selecting appropriate encryption algorithms, managing encryption keys, restricting a subset of their users from viewing payload output, or a combination of these.

The server itself never adds encryption over Payloads.
Therefore, unless client-side encryption is implemented, Payload data will be persisted in non-encrypted form to the data store, and any Client that can make requests to a Temporal namespace (including the Temporal UI and CLI) will be able to read Payloads contained in Workflows.
When working with sensitive data, you should always implement Payload encryption.

## Custom Payload Codec {/* #custom-payload-codec */}

Custom Data Converters can change the default Temporal Data Conversion behavior by adding hooks, sending payloads to external storage, or performing different encoding steps.
If you only need to change the encoding performed on your payloads -- by adding compression or encryption -- you can override the default Data Converter to use a new `PayloadCodec`.

The `IPayloadCodec` needs to implement `EncodeAsync()` and `DecodeAsync()` methods.
These should convert the given payloads as needed into new payloads, using the `"encoding"` metadata field.
Do not mutate the existing payloads.
Here is an example of an encryption codec that just uses base64 in each direction:

```csharp
public class EncryptionCodec : IPayloadCodec
{
    public Task<IReadOnlyCollection<Payload>> EncodeAsync(IReadOnlyCollection<Payload> payloads) =>
        Task.FromResult<IReadOnlyCollection<Payload>>(payloads.Select(p =>
        {
            return new Payload()
            {
                // Set our specific encoding. We may also want to add a key ID in here for use by
                // the decode side
                Metadata = { ["encoding"] = "binary/my-payload-encoding" },
                Data = ByteString.CopyFrom(Encrypt(p.ToByteArray())),
            };
        }).ToList());

    public Task<IReadOnlyCollection<Payload>> DecodeAsync(IReadOnlyCollection<Payload> payloads) =>
        Task.FromResult<IReadOnlyCollection<Payload>>(payloads.Select(p =>
        {
            // Ignore if it doesn't have our expected encoding
            if (p.Metadata.GetValueOrDefault("encoding") != "binary/my-payload-encoding")
            {
                return p;
            }
            // Decrypt
            return Payload.Parser.ParseFrom(Decrypt(p.Data.ToByteArray()));
        }).ToList());

    private byte[] Encrypt(byte[] data) => Encoding.ASCII.GetBytes(Convert.ToBase64String(data));

    private byte[] Decrypt(byte[] data) => Convert.FromBase64String(Encoding.ASCII.GetString(data));
}
```

**Set Data Converter to use custom Payload Codec**

When creating a client, the default `DataConverter` can be updated with the payload codec like so:

```csharp
var myClient = await TemporalClient.ConnectAsync(new("localhost:7233")
{
    DataConverter = DataConverter.Default with { PayloadCodec = new EncryptionCodec() },
});
```

- Data **encoding** is performed by the client using the converters and codecs provided by Temporal or your custom implementation when passing input to the Temporal Cluster. For example, plain text input is usually serialized into a JSON object, and can then be compressed or encrypted.
- Data **decoding** may be performed by your application logic during your Workflows or Activities as necessary, but decoded Workflow results are never persisted back to the Temporal Cluster. Instead, they are stored encoded on the Cluster, and you need to provide an additional parameter when using the [temporal workflow show](/cli/command-reference/workflow#show) command or when browsing the Web UI to view output.

For reference, see the [Encryption](https://github.com/temporalio/samples-dotnet/tree/main/src/Encryption) sample.

### Using a Codec Server

A Codec Server is an HTTP server that uses your custom Codec logic to decode your data remotely.
The Codec Server is independent of the Temporal Cluster and decodes your encrypted payloads through predefined endpoints.
You create, operate, and manage access to your Codec Server in your own environment.
The Temporal CLI and the Web UI in turn provide built-in hooks to call the Codec Server to decode encrypted payloads on demand.
Refer to the [Codec Server](/production-deployment/data-encryption) documentation for information on how to design and deploy a Codec Server.

## Payload conversion

Temporal SDKs provide a default [Payload Converter](/payload-converter) that can be customized to convert a custom data type to [Payload](/dataconversion#payload) and back.

### Conversion sequence {/* #conversion-sequence */}

The order in which your encoding Payload Converters are applied depend on the order given to the Data Converter.
You can set multiple encoding Payload Converters to run your conversions.
When the Data Converter receives a value for conversion, it passes through each Payload Converter in sequence until the converter that handles the data type does the conversion.

Payload Converters can be customized independently of a Payload Codec.
Temporal's Converter architecture looks like this:

<CaptionedImage
    src="/img/info/converter-architecture.png"
    title="Temporal converter architecture"
/>

### Custom Payload Converter {/* #custom-payload-converter */}

Data converters are used to convert raw Temporal payloads to/from actual .NET types.
A custom data converter can be set via the `DataConverter` option when creating a client. Data converters are a combination of payload converters, payload codecs, and failure converters.
Payload converters convert .NET values to/from serialized bytes. Payload codecs convert bytes to bytes (e.g. for compression or encryption). Failure converters convert exceptions to/from serialized failures.

Data converters are in the `Temporalio.Converters` namespace.
The default data converter uses a default payload converter, which supports the following types:

- `null`
- `byte[]`
- `Google.Protobuf.IMessage` instances
- Anything that `System.Text.Json` supports
- `IRawValue` as unconverted raw payloads

Custom converters can be created for all uses. For example, to create client with a data converter that converts all C#
property names to camel case, you would:

```csharp
using System.Text.Json;
using Temporalio.Client;
using Temporalio.Converters;

public class CamelCasePayloadConverter : DefaultPayloadConverter
{
    public CamelCasePayloadConverter()
      : base(new JsonSerializerOptions { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    {
    }
}

var client = await TemporalClient.ConnectAsync(new()
{
    TargetHost = "localhost:7233",
    Namespace = "my-namespace",
    DataConverter = DataConverter.Default with { PayloadConverter = new CamelCasePayloadConverter() },
});
```

<!--  ### Custom Type Data Conversion TODO(cretz): Develop https://github.com/temporalio/samples-dotnet/issues/38 first -->

---

## Debugging - .NET SDK

## Debugging {/* #debug */}

This page shows how to do the following:

- [Debug in a development environment](#debug-in-a-development-environment)
- [Debug in a production environment](#debug-in-a-development-production)

### Debug in a development environment {/* #debug-in-a-development-environment */}

In developing Workflows, you can use the normal development tools of logging and a debugger to see what’s happening in your Workflow.
In addition to the normal development tools of logging and a debugger, you can also see what’s happening in your Workflow by using the [Web UI](/web-ui) or [Temporal CLI](/cli).
The Web UI provides insight into your Workflows, making it easier to identify issues and monitor the state of your Workflows in real time.

### Debug in a production environment {/* #debug-in-a-development-production */}

**How to debug in a production environment using the Temporal .NET SDK**

You can debug production Workflows using:

- [Web UI](/web-ui)
- [Temporal CLI](/cli)
- [Replay](/develop/dotnet/best-practices/testing-suite#replay)
- [Tracing](/develop/dotnet/platform/observability#tracing)
- [Logging](/develop/dotnet/platform/observability#logging)

You can debug and tune Worker performance with metrics and the [Worker performance guide](/develop/worker-performance).
For more information, see [Observability ▶️ Metrics](/develop/dotnet/platform/observability#metrics) for setting up SDK metrics.

Debug Server performance with [Cloud metrics](/cloud/metrics/) or [self-hosted Server metrics](/self-hosted-guide/production-checklist#scaling-and-metrics).

---

## Error handling - .NET SDK

## Raise and Handle Exceptions {/* #exception-handling */}

In each Temporal SDK, error handling is implemented idiomatically, following the conventions of the language.
Temporal uses several different error classes internally — for example, [`CancelledFailureException`](https://dotnet.temporal.io/api/Temporalio.Exceptions.CanceledFailureException.html) in the .NET SDK, to handle a Workflow cancellation.
You should not raise or otherwise implement these manually, as they are tied to Temporal platform logic.

The one Temporal error class that you will typically raise deliberately is [`ApplicationFailureException`](https://dotnet.temporal.io/api/Temporalio.Exceptions.ApplicationFailureException.html).
In fact, *any* other exceptions that are raised from your C# code in a Temporal Activity will be converted to an `ApplicationFailureException` internally.
This way, an error's type, severity, and any additional details can be sent to the Temporal Service, indexed by the Web UI, and even serialized across language boundaries.

In other words, these two code samples do the same thing:

```csharp
[Serializable]
public class InvalidDepartmentException : Exception
{
    public InvalidDepartmentException() : base() { }
    public InvalidDepartmentException(string message) : base(message) { }
    public InvalidDepartmentException(string message, Exception inner) : base(message, inner) { }
}

[Activity]
public Task<OrderConfirmation> SendBillAsync(Bill bill)
{
    throw new InvalidDepartmentException("Invalid department");
}
```

```csharp
[Activity]
public Task<OrderConfirmation> SendBillAsync(Bill bill)
{
    throw new ApplicationFailureException("Invalid department", errorType: "InvalidDepartmentException");
}
```

Depending on your implementation, you may decide to use either method.
One reason to use the Temporal `ApplicationFailureException` class is because it allows you to set an additional `non_retryable` parameter.
This way, you can decide whether an error should not be retried automatically by Temporal.
This can be useful for deliberately failing a Workflow due to bad input data, rather than waiting for a timeout to elapse:

```csharp
[Activity]
public Task<OrderConfirmation> SendBillAsync(Bill bill)
{
    throw new ApplicationFailureException("Invalid department", nonRetryable: true);
}
```

You can alternately specify a list of errors that are non-retryable in your Activity [Retry Policy](/develop/dotnet/activities/timeouts#activity-retries).

## Failing Workflows {/* #workflow-failure */}

One of the core design principles of Temporal is that an Activity Failure will never directly cause a Workflow Failure — a Workflow should never return as Failed unless deliberately.
The default retry policy associated with Temporal Activities is to retry them until reaching a certain timeout threshold.
Activities will not actually *return* a failure to your Workflow until this condition or another non-retryable condition is met.
At this point, you can decide how to handle an error returned by your Activity the way you would in any other program.
For example, you could implement a [Saga Pattern](https://github.com/temporalio/samples-dotnet/tree/main/src/Saga) that uses `try`/`catch` blocks to "unwind" some of the steps your Workflow has performed up to the point of Activity Failure.

**You will only fail a Workflow by manually raising an `ApplicationFailureException` from the Workflow code.**
You could do this in response to an Activity Failure, if the failure of that Activity means that your Workflow should not continue:

```csharp
try
{
    await Workflow.ExecuteActivityAsync(
        (Activities act) => act.ValidateCreditCardAsync(order.Customer.CreditCardNumber),
        options);
}
catch (ActivityFailureException err)
{
    logger.LogError("Unable to process credit card: {Message}", err.Message);
    throw new ApplicationFailureException(message: "Invalid credit card number error");
}
```

This works differently in a Workflow than raising exceptions from Activities.
In an Activity, any C# exceptions or custom exceptions are converted to a Temporal `ApplicationError`.
In a Workflow, any exceptions that are raised other than an explicit Temporal `ApplicationError` will only fail that particular [Workflow Task](https://docs.temporal.io/tasks#workflow-task-execution) and be retried.
This includes any typical C# `RuntimeError`s that are raised automatically.
These errors are treated as bugs that can be corrected with a fixed deployment, rather than a reason for a Temporal Workflow Execution to return unexpectedly.

---

## Best Practices - .NET SDK

![.NET SDK Banner](/img/assets/banner-dotnet-temporal.png)

## Best practices

- [Error handling](/develop/dotnet/best-practices/error-handling)
- [Testing](/develop/dotnet/best-practices/testing-suite)
- [Debugging](/develop/dotnet/best-practices/debugging)
- [Converters and encryption](/develop/dotnet/best-practices/converters-and-encryption)

---

## Testing - .NET SDK

The .NET test-suite feature guide describes the frameworks that facilitate Workflow and integration testing.

In the context of Temporal, you can create these types of automated tests:

- **End-to-end:** Running a Temporal Server and Worker with all its Workflows and Activities; starting and interacting with Workflows from a Client.
- **Integration:** Anything between end-to-end and unit testing.
  - Running Activities with mocked Context and other SDK imports (and usually network requests).
  - Running Workers with mock Activities, and using a Client to start Workflows.
  - Running Workflows with mocked SDK imports.
- **Unit:** Running a piece of Workflow or Activity code and mocking any code it calls.

We generally recommend writing the majority of your tests as integration tests.

Because the test server supports skipping time, use the test server for both end-to-end and integration tests with Workers.

## Test frameworks {/* #test-frameworks */}

**Compatible testing frameworks**

The .NET SDK is compatible with any testing framework and does not have a specific recommendation.
Most .NET SDK samples use [xUnit](https://xunit.net/).

## Testing Workflows {/* #testing-workflows */}

**How to test Workflow Definitions using the Temporal .NET SDK**

Workflow testing can be done in an integration-test fashion against a real server, however it is hard to simulate timeouts and other long time-based code.
Using the time-skipping Workflow test environment can help there.

### Testing Workflows with standard server

A non-time-skipping `Temporalio.Testing.WorkflowEnvironment` can be started via `StartLocalAsync` which supports all standard Temporal features.
It is actually the real Temporal dev server packaged in the Temporal CLI, lazily downloaded on first use, and run as a sub-process in the background.
Assuming tests properly use separate Task Queues, the same server can and should be reused across tests.

Here's a simple example of a Workflow:

```csharp
[Workflow]
public class SayHelloWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync(string name)
    {
        return $"Hello, {name}!";
    }
}
```

Here's how a test of that Workflow may appear in xUnit:

```csharp
using Temporalio.Testing;
using Temporalio.Worker;

[Fact]
public async Task SayHelloWorkflow_SimpleRun_Succeeds()
{
    // Start local dev server
    await using var env = await WorkflowEnvironment.StartLocalAsync();

    // Create a worker
    using var worker = new TemporalWorker(
      env.Client,
      new TemporalWorkerOptions($"task-queue-{Guid.NewGuid()}").
          AddWorkflow<SayHelloWorkflow>());

    // Run the worker only for the life of the code within
    await worker.ExecuteAsync(async () =>
    {
        // Execute the workflow and confirm the result
        var result = await env.Client.ExecuteWorkflowAsync(
            (SayHelloWorkflow wf) => wf.RunAsync("Temporal"),
            new(id: $"wf-{Guid.NewGuid()}", taskQueue: worker.Options.TaskQueue!));
        Assert.Equal("Hello, Temporal!", result);
    });
}
```

While this is just a demonstration, a local server is often used as a fixture across many tests.

### Testing Workflows with time skipping

Sometimes there is a need to test Workflows that run a long time or to test that timeouts occur.
A time-skipping `Temporalio.Testing.WorkflowEnvironment` can be started via `StartTimeSkippingAsync` which is a reimplementation of the Temporal server with special time skipping capabilities.
Like `StartLocalAsync`, this also lazily downloads the process to run when first called.
Note, unlike `StartLocalAsync`, this class is not thread safe nor safe for use with independent tests.
It can be technically be reused, but only for one test at a time because time skipping is locked/unlocked at the environment level.
Developers are encouraged to run it per test needed.

#### Automatic time skipping

Here's a simple example of a Workflow that waits a day:

```csharp
[Workflow]
public class WaitADayWorkflow
{
    [WorkflowRun]
    public async Task<string> RunAsync()
    {
        await Workflow.DelayAsync(TimeSpan.FromDays(1));
        return "all done";
    }
}
```

A regular integration test of this Workflow on a normal server would be way too slow.
However, the time-skipping server automatically skips to the next event when we wait on the result.
Here's a test for that Workflow in xUnit:

```csharp
using Temporalio.Testing;
using Temporalio.Worker;

[Fact]
public async Task WaitADayWorkflow_SimpleRun_Succeeds()
{
    // Start time-skipping test server
    await using var env = await WorkflowEnvironment.StartTimeSkippingAsync();

    // Create a worker
    using var worker = new TemporalWorker(
      env.Client,
      new TemporalWorkerOptions($"task-queue-{Guid.NewGuid()}").
          AddWorkflow<WaitADayWorkflow>());

    // Run the worker only for the life of the code within
    await worker.ExecuteAsync(async () =>
    {
        // Execute the workflow and confirm the result
        var result = await env.Client.ExecuteWorkflowAsync(
            (WaitADayWorkflow wf) => wf.RunAsync(),
            new(id: $"wf-{Guid.NewGuid()}", taskQueue: worker.Options.TaskQueue!));
        Assert.Equal("all done", result);
    });
}
```

This test will run almost instantly.
This is because by calling `ExecuteWorkflowAsync` on our client, we are actually calling `StartWorkflowAsync` + `GetResultAsync`, and `GetResultAsync` automatically skips time as much as it can (basically until the end of the workflow or until an activity is run).

To disable automatic time-skipping while waiting for a workflow result, run code as a lambda passed to `env.WithAutoTimeSkippingDisabled` or `env.WithAutoTimeSkippingDisabledAsync`.

#### Manual time skipping

Until a Workflow is waited on, all time skipping in the time-skipping environment is done manually via `WorkflowEnvironment.DelayAsync`.

Here's a Workflow that waits for a Signal or times out:

```csharp
[Workflow]
public class SignalWorkflow
{
    private bool signalReceived = false;

    [WorkflowRun]
    public async Task<string> RunAsync()
    {
        // Wait for signal or timeout in 45 seconds
        if (Workflow.WaitConditionAsync(() => signalReceived, TimeSpan.FromSeconds(45)))
        {
            return "got signal";
        }
        return "got timeout";
    }

    [WorkflowSignal]
    public async Task SomeSignalAsync() => signalReceived = true;
}
```

To test a normal Signal in xUnit, you might:

```csharp
using Temporalio.Testing;
using Temporalio.Worker;

[Fact]
public async Task SignalWorkflow_SendSignal_HasExpectedResult()
{
    await using var env = await WorkflowEnvironment.StartTimeSkippingAsync();
    using var worker = new TemporalWorker(
        env.Client,
        new TemporalWorkerOptions($"task-queue-{Guid.NewGuid()}").
            AddWorkflow<SignalWorkflow>());
    await worker.ExecuteAsync(async () =>
    {
        var handle = await env.Client.StartWorkflowAsync(
            (SignalWorkflow wf) => wf.RunAsync(),
            new(id: $"wf-{Guid.NewGuid()}", taskQueue: worker.Options.TaskQueue!));
        await handle.SignalAsync(wf => wf.SomeSignalAsync());
        Assert.Equal("got signal", await handle.GetResultAsync());
    });
}
```

But how would you test the timeout part? Like so:

```csharp
using Temporalio.Testing;
using Temporalio.Worker;

[Fact]
public async Task SignalWorkflow_SignalTimeout_HasExpectedResult()
{
    await using var env = await WorkflowEnvironment.StartTimeSkippingAsync();
    using var worker = new TemporalWorker(
        env.Client,
        new TemporalWorkerOptions($"task-queue-{Guid.NewGuid()}").
            AddWorkflow<SignalWorkflow>());
    await worker.ExecuteAsync(async () =>
    {
        var handle = await env.Client.StartWorkflowAsync(
            (SignalWorkflow wf) => wf.RunAsync(),
            new(id: $"wf-{Guid.NewGuid()}", taskQueue: worker.Options.TaskQueue!));
        await env.DelayAsync(TimeSpan.FromSeconds(50));
        Assert.Equal("got timeout", await handle.GetResultAsync());
    });
}
```

### Mocking Activities

When testing Workflows, often you don't want to actually run the Activities.
Activities are just methods with the `[Activity]` attribute.
Simply write different/empty/fake/asserting ones and pass those to the Worker to have different activities called during the test.

## Testing Activities {/* #test-activities */}

**How to test Activity Definitions using the Temporal .NET SDK**

Unit testing an Activity or any code that could run in an Activity is done via the `Temporalio.Testing.ActivityEnvironment` class.
Simply instantiate the class, and any code inside `RunAsync` will be invoked inside the activity context.
The following important members are available on the environment to affect the activity context:

- `Info` - Activity info, defaulted to a basic set of values.
- `Logger` - Activity logger, defaulted to a null logger.
- `Cancel(CancelReason)` - Helper to set the reason and cancel the source.
- `CancelReason` - Cancel reason.
- `CancellationTokenSource` - Token source for issuing cancellation.
- `Heartbeater` - Callback invoked each heartbeat.
- `WorkerShutdownTokenSource` - Token source for issuing Worker shutdown.
- `PayloadConverter` - Defaulted to default payload converter.

## Replay test {/* #replay */}

**How to do a Replay test using the Temporal .NET SDK**

Given a Workflow's history, it can be replayed locally to check for things like non-determinism errors.
