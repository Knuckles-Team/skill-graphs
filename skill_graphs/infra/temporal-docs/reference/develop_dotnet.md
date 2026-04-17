[Skip to main content](https://docs.temporal.io/develop/dotnet/testing-suite#__docusaurus_skipToContent_fallback)
[![Temporal logo](https://docs.temporal.io/img/assets/temporal-logo-dark.svg)](https://temporal.io)[Home](https://docs.temporal.io/)[Courses](https://learn.temporal.io/getting_started/)[SDKs](https://docs.temporal.io/develop)[AI Cookbook](https://docs.temporal.io/ai-cookbook)[Code Exchange](https://temporal.io/code-exchange)[Temporal Cloud](https://docs.temporal.io/cloud)
Ask AI
Search
  * [Home](https://docs.temporal.io/)
  * [Quickstarts](https://docs.temporal.io/quickstarts)
  * [Evaluate](https://docs.temporal.io/evaluate/)
  * [Develop](https://docs.temporal.io/develop/)
    * [Go SDK](https://docs.temporal.io/develop/go/)
    * [Java SDK](https://docs.temporal.io/develop/java/)
    * [PHP SDK](https://docs.temporal.io/develop/php/)
    * [Python SDK](https://docs.temporal.io/develop/python/)
    * [TypeScript SDK](https://docs.temporal.io/develop/typescript/)
    * [.NET SDK](https://docs.temporal.io/develop/dotnet/)
      * [Quickstart](https://docs.temporal.io/develop/dotnet/set-up-your-local-dotnet)
      * [Core application](https://docs.temporal.io/develop/dotnet/core-application)
      * [Temporal Client](https://docs.temporal.io/develop/dotnet/temporal-client)
      * [Testing](https://docs.temporal.io/develop/dotnet/testing-suite)
      * [Failure detection](https://docs.temporal.io/develop/dotnet/failure-detection)
      * [Messages](https://docs.temporal.io/develop/dotnet/message-passing)
      * [Interrupt a Workflow](https://docs.temporal.io/develop/dotnet/cancellation)
      * [Asynchronous Activity completion](https://docs.temporal.io/develop/dotnet/asynchronous-activity)
      * [Versioning](https://docs.temporal.io/develop/dotnet/versioning)
      * [Observability](https://docs.temporal.io/develop/dotnet/observability)
      * [Benign exceptions](https://docs.temporal.io/develop/dotnet/benign-exceptions)
      * [Enriching the UI](https://docs.temporal.io/develop/dotnet/enriching-ui)
      * [Debugging](https://docs.temporal.io/develop/dotnet/debugging)
      * [Schedules](https://docs.temporal.io/develop/dotnet/schedules)
      * [Converters and encryption](https://docs.temporal.io/develop/dotnet/converters-and-encryption)
      * [Durable Timers](https://docs.temporal.io/develop/dotnet/durable-timers)
      * [Temporal Nexus](https://docs.temporal.io/develop/dotnet/nexus)
      * [Child Workflows](https://docs.temporal.io/develop/dotnet/child-workflows)
      * [Continue-As-New](https://docs.temporal.io/develop/dotnet/continue-as-new)
    * [Ruby SDK](https://docs.temporal.io/develop/ruby/)
    * [Environment configuration](https://docs.temporal.io/develop/environment-configuration)
    * [Activity retry simulator](https://docs.temporal.io/develop/activity-retry-simulator)
    * [Worker performance](https://docs.temporal.io/develop/worker-performance)
    * [Worker tuning reference](https://docs.temporal.io/develop/worker-tuning-reference)
    * [Safe deployments](https://docs.temporal.io/develop/safe-deployments)
    * [Plugins guide](https://docs.temporal.io/develop/plugins-guide)
  * [Temporal Cloud](https://docs.temporal.io/cloud)
  * [Deploy to production](https://docs.temporal.io/production-deployment)
  * [CLI (temporal)](https://docs.temporal.io/cli)
  * [References](https://docs.temporal.io/references/)
  * [Troubleshooting](https://docs.temporal.io/troubleshooting/)
  * [Best practices](https://docs.temporal.io/best-practices/)
  * [Encyclopedia](https://docs.temporal.io/encyclopedia/)
  * [Glossary](https://docs.temporal.io/glossary)
  * [Use with AI](https://docs.temporal.io/with-ai)


  * [](https://docs.temporal.io/)
  * [Develop](https://docs.temporal.io/develop/)
  * [.NET SDK](https://docs.temporal.io/develop/dotnet/)
  * Testing


On this page
# Testing - .NET SDK
The .NET test-suite feature guide describes the frameworks that facilitate Workflow and integration testing.
In the context of Temporal, you can create these types of automated tests:
  * **End-to-end:** Running a Temporal Server and Worker with all its Workflows and Activities; starting and interacting with Workflows from a Client.
  * **Integration:** Anything between end-to-end and unit testing. 
    * Running Activities with mocked Context and other SDK imports (and usually network requests).
    * Running Workers with mock Activities, and using a Client to start Workflows.
    * Running Workflows with mocked SDK imports.
  * **Unit:** Running a piece of Workflow or Activity code and mocking any code it calls.


We generally recommend writing the majority of your tests as integration tests.
Because the test server supports skipping time, use the test server for both end-to-end and integration tests with Workers.
## Test frameworks[​](https://docs.temporal.io/develop/dotnet/testing-suite#test-frameworks "Direct link to Test frameworks")
**Compatible testing frameworks**
The .NET SDK is compatible with any testing framework and does not have a specific recommendation. Most .NET SDK samples use 
## Testing Workflows[​](https://docs.temporal.io/develop/dotnet/testing-suite#testing-workflows "Direct link to Testing Workflows")
**How to test Workflow Definitions using the Temporal .NET SDK**
Workflow testing can be done in an integration-test fashion against a real server, however it is hard to simulate timeouts and other long time-based code. Using the time-skipping Workflow test environment can help there.
### Testing Workflows with standard server[​](https://docs.temporal.io/develop/dotnet/testing-suite#testing-workflows-with-standard-server "Direct link to Testing Workflows with standard server")
A non-time-skipping `Temporalio.Testing.WorkflowEnvironment` can be started via `StartLocalAsync` which supports all standard Temporal features. It is actually the real Temporal dev server packaged in the Temporal CLI, lazily downloaded on first use, and run as a sub-process in the background. Assuming tests properly use separate Task Queues, the same server can and should be reused across tests.
Here's a simple example of a Workflow:
```
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
```
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
### Testing Workflows with time skipping[​](https://docs.temporal.io/develop/dotnet/testing-suite#testing-workflows-with-time-skipping "Direct link to Testing Workflows with time skipping")
Sometimes there is a need to test Workflows that run a long time or to test that timeouts occur. A time-skipping `Temporalio.Testing.WorkflowEnvironment` can be started via `StartTimeSkippingAsync` which is a reimplementation of the Temporal server with special time skipping capabilities. Like `StartLocalAsync`, this also lazily downloads the process to run when first called. Note, unlike `StartLocalAsync`, this class is not thread safe nor safe for use with independent tests. It can be technically be reused, but only for one test at a time because time skipping is locked/unlocked at the environment level. Developers are encouraged to run it per test needed.
#### Automatic time skipping[​](https://docs.temporal.io/develop/dotnet/testing-suite#automatic-time-skipping "Direct link to Automatic time skipping")
Here's a simple example of a Workflow that waits a day:
```
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

A regular integration test of this Workflow on a normal server would be way too slow. However, the time-skipping server automatically skips to the next event when we wait on the result. Here's a test for that Workflow in xUnit:
```
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

This test will run almost instantly. This is because by calling `ExecuteWorkflowAsync` on our client, we are actually calling `StartWorkflowAsync` + `GetResultAsync`, and `GetResultAsync` automatically skips time as much as it can (basically until the end of the workflow or until an activity is run).
To disable automatic time-skipping while waiting for a workflow result, run code as a lambda passed to `env.WithAutoTimeSkippingDisabled` or `env.WithAutoTimeSkippingDisabledAsync`.
#### Manual time skipping[​](https://docs.temporal.io/develop/dotnet/testing-suite#manual-time-skipping "Direct link to Manual time skipping")
Until a Workflow is waited on, all time skipping in the time-skipping environment is done manually via `WorkflowEnvironment.DelayAsync`.
Here's a Workflow that waits for a Signal or times out:
```
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
```
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
```
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

### Mocking Activities[​](https://docs.temporal.io/develop/dotnet/testing-suite#mocking-activities "Direct link to Mocking Activities")
When testing Workflows, often you don't want to actually run the Activities. Activities are just methods with the `[Activity]` attribute. Simply write different/empty/fake/asserting ones and pass those to the Worker to have different activities called during the test.
## Testing Activities[​](https://docs.temporal.io/develop/dotnet/testing-suite#test-activities "Direct link to Testing Activities")
**How to test Activity Definitions using the Temporal .NET SDK**
Unit testing an Activity or any code that could run in an Activity is done via the `Temporalio.Testing.ActivityEnvironment` class. Simply instantiate the class, and any code inside `RunAsync` will be invoked inside the activity context. The following important members are available on the environment to affect the activity context:
  * `Info` - Activity info, defaulted to a basic set of values.
  * `Logger` - Activity logger, defaulted to a null logger.
  * `Cancel(CancelReason)` - Helper to set the reason and cancel the source.
  * `CancelReason` - Cancel reason.
  * `CancellationTokenSource` - Token source for issuing cancellation.
  * `Heartbeater` - Callback invoked each heartbeat.
  * `WorkerShutdownTokenSource` - Token source for issuing Worker shutdown.
  * `PayloadConverter` - Defaulted to default payload converter.


## Replay test[​](https://docs.temporal.io/develop/dotnet/testing-suite#replay "Direct link to Replay test")
**How to do a Replay test using the Temporal .NET SDK**
Given a Workflow's history, it can be replayed locally to check for things like non-determinism errors. For example, assuming the `history` parameter below is given a JSON string of history exported from the CLI or web UI, the following method will replay it:
```
using Temporalio;  
using Temporalio.Worker;  
  
public static async Task ReplayFromJsonAsync(string historyJson)  
{  
    var replayer = new WorkflowReplayer(  
        new WorkflowReplayerOptions().AddWorkflow<MyWorkflow>());  
    await replayer.ReplayWorkflowAsync(WorkflowHistory.FromJson("my-workflow-id", historyJson));  
}  

```

If there is a non-determinism, this will throw an exception.
Workflow history can be loaded from more than just JSON. It can be fetched individually from a Workflow handle, or even in a list. For example, the following code will check that all Workflow histories for a certain Workflow type (i.e. workflow class) are safe with the current Workflow code.
```
using Temporalio;  
using Temporalio.Client;  
using Temporalio.Worker;  
  
public static async Task CheckPastHistoriesAsync(ITemporalClient client)  
{  
    var replayer = new WorkflowReplayer(  
        new WorkflowReplayerOptions().AddWorkflow<MyWorkflow>());  
    var listIter = client.ListWorkflowHistoriesAsync("WorkflowType = 'SayHello'");  
    await foreach (var result in replayer.ReplayWorkflowsAsync(listIter))  
    {  
        if (result.ReplayFailure != null)  
        {  
            ExceptionDispatchInfo.Throw(result.ReplayFailure);  
        }  
    }  
}  

```

**Tags:**
  * [.Net SDK](https://docs.temporal.io/tags/net-sdk)
  * [Temporal SDKs](https://docs.temporal.io/tags/temporal-sd-ks)
  * [Testing](https://docs.temporal.io/tags/testing)


Help us make Temporal better. Contribute to our 
[Previous Temporal Client](https://docs.temporal.io/develop/dotnet/temporal-client)[Next Failure detection](https://docs.temporal.io/develop/dotnet/failure-detection)
  * [Test frameworks](https://docs.temporal.io/develop/dotnet/testing-suite#test-frameworks)
  * [Testing Workflows](https://docs.temporal.io/develop/dotnet/testing-suite#testing-workflows)
    * [Testing Workflows with standard server](https://docs.temporal.io/develop/dotnet/testing-suite#testing-workflows-with-standard-server)
    * [Testing Workflows with time skipping](https://docs.temporal.io/develop/dotnet/testing-suite#testing-workflows-with-time-skipping)
      * [Automatic time skipping](https://docs.temporal.io/develop/dotnet/testing-suite#automatic-time-skipping)
      * [Manual time skipping](https://docs.temporal.io/develop/dotnet/testing-suite#manual-time-skipping)
    * [Mocking Activities](https://docs.temporal.io/develop/dotnet/testing-suite#mocking-activities)
  * [Testing Activities](https://docs.temporal.io/develop/dotnet/testing-suite#test-activities)
  * [Replay test](https://docs.temporal.io/develop/dotnet/testing-suite#replay)


  * [Temporal Cloud](https://temporal.io/cloud)
  * [Meetups](https://temporal.io/community#events)
  * [Workshops](https://temporal.io/community#workshops)
  * [Support forum](https://community.temporal.io/)
  * [Ask an expert](https://pages.temporal.io/ask-an-expert)


  * [Learn Temporal](https://learn.temporal.io)
  * [Blog](https://temporal.io/blog)
  * [Use cases](https://temporal.io/use-cases)
  * [Newsletter signup](https://pages.temporal.io/newsletter-subscribe)


  * [Security](https://docs.temporal.io/security)
  * [Privacy policy](https://temporal.io/global-privacy-policy)
  * [Terms of service](https://docs.temporal.io/pdf/temporal-tos-2021-07-24.pdf)
  * [We're hiring](https://temporal.io/careers)


[![Temporal logo](https://docs.temporal.io/img/favicon.png)](https://temporal.io)
Copyright © 2026 Temporal Technologies Inc.
Feedback![](https://static.scarf.sh/a.png?x-pxid=6fb132d3-92f6-455f-bf17-eb3d6937bdea)
Recaptcha requires verification. 
- 
protected by **reCAPTCHA**
-