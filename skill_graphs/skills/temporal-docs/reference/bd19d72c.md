For example, assuming the `history` parameter below is given a JSON string of history exported from the CLI or web UI, the following method will replay it:

```csharp
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

Event history can be loaded from more than just JSON.
It can be fetched individually from a Workflow handle, or even in a list.
For example, the following code will check that all Workflow histories for a certain Workflow type (i.e. workflow class) are safe with the current Workflow code.

```csharp
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

---

## Client - .NET SDK

![.NET SDK Banner](/img/assets/banner-dotnet-temporal.png)

## Temporal Client

- [Temporal Client](/develop/dotnet/client/temporal-client)

---

## Temporal Client - .NET SDK

A [Temporal Client](/encyclopedia/temporal-sdks#temporal-client) enables you to communicate with the Temporal Service.
Communication with a Temporal Service lets you perform actions such as starting Workflow Executions, sending Signals and
Queries to Workflow Executions, getting Workflow results, and more.

This page shows you how to do the following using the .NET SDK with the Temporal Client:

- [Connect to a local development Temporal Service](#connect-to-development-service)
- [Connect to Temporal Cloud](#connect-to-temporal-cloud)
- [Start a Workflow Execution](#start-workflow)
- [Get Workflow results](#get-workflow-results)

A Temporal Client cannot be initialized and used inside a Workflow. However, it is acceptable and common to use a
Temporal Client inside an Activity to communicate with a Temporal Service.

## Connect to development Temporal Service {/* #connect-to-development-service */}

Use
[`TemporalClient.ConnectAsync`](https://dotnet.temporal.io/api/Temporalio.Client.TemporalClient.html#Temporalio_Client_TemporalClient_ConnectAsync_Temporalio_Client_TemporalClientConnectOptions_)
to create a client. Connection options include the Temporal Server address, Namespace, and (optionally) TLS
configuration. You can provide these options directly in code, or load them from **environment variables** and/or a
**TOML configuration file** using the `Temporalio.Client.EnvConfig` helpers. We recommend environment variables or a
configuration file for secure, repeatable configuration.

When you’re running a Temporal Service locally (such as with the
[Temporal CLI dev server](https://docs.temporal.io/cli/command-reference/server#start-dev)), the required options are minimal. If you
don't specify a host/port, most connections default to `127.0.0.1:7233` and the `default` Namespace.

<Tabs groupId="connect-options-dotnet" defaultValue="config-file" >

<TabItem value="config-file" label="Configuration File">

You can use a TOML configuration file to set connection options for the Temporal Client. The configuration file lets you
configure multiple profiles, each with its own set of connection options. You can then specify which profile to use when
creating the Temporal Client. You can use the environment variable `TEMPORAL_CONFIG_FILE` to specify the location of the
TOML file or provide the path to the file directly in code. If you don't provide the configuration file path, the SDK
looks for it at the path `~/.config/temporalio/temporal.toml` or the equivalent on your OS. Refer to
[Environment Configuration](/references/client-environment-configuration) for more details about configuration
files and profiles.

:::info

The connection options set in configuration files have lower precedence than environment variables. This means that if
you set the same option in both the configuration file and as an environment variable, the environment variable value
overrides the option set in the configuration file.

:::

For example, the following TOML configuration file defines two profiles: `default` and `prod`. Each profile has its own
set of connection options.

```toml title="config.toml"
