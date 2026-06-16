# Custom headers for production
[profile.prod.grpc_meta]
environment     = "production"
service-version = "v1.2.3"
```

You can create a Temporal Client using a profile from the configuration file as follows. In this example, you load the
`default` profile for local development:

```csharp title="LoadFromFile.cs" {27-30}
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
        Console.WriteLine("--- Loading default profile from config.toml ---");

        try
        {
            // For this sample to be self-contained, we explicitly provide the path to
            // the config.toml file included in this directory.
            // By default though, the config.toml file will be loaded from
            // ~/.config/temporalio/temporal.toml (or the equivalent standard config directory on your OS).
            var configFile = Path.Combine(Directory.GetCurrentDirectory(), "config.toml");

            // LoadClientConnectOptions is a helper that loads a profile and prepares
            // the config for TemporalClient.ConnectAsync. By default, it loads the
            // "default" profile.
            var connectOptions = ClientEnvConfig.LoadClientConnectOptions(new ClientEnvConfig.ProfileLoadOptions
            {
                ConfigSource = DataSource.FromPath(configFile),
            });

            Console.WriteLine($"Loaded 'default' profile from {configFile}.");
            Console.WriteLine($"  Address: {connectOptions.TargetHost}");
            Console.WriteLine($"  Namespace: {connectOptions.Namespace}");
            if (connectOptions.RpcMetadata?.Count > 0)
            {
                Console.WriteLine($"  gRPC Metadata: {string.Join(", ", connectOptions.RpcMetadata.Select(kv => $"{kv.Key}={kv.Value}"))}");
            }

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

Use the `EnvConfig` package to set connection options for the Temporal Client using environment variables. For a list of
all available environment variables and their default values, refer to
[Environment Configuration](/references/client-environment-configuration).

For example, the following code snippet loads all environment variables and creates a Temporal Client with the options
specified in those variables. If you have defined a configuration file at either the default location
(`~/.config/temporalio/temporal.toml`) or a custom location specified by the `TEMPORAL_CONFIG_FILE` environment
variable, this will also load the default profile in the configuration file. However, any options set via environment
variables will take precedence.

Set the following environment variables before running your .NET application. Replace the placeholder values with your
actual configuration. Since this is for a local development Temporal Service, the values connect to `localhost:7233` and
the `default` Namespace. You may omit these variables entirely since they're the defaults.

```bash
export TEMPORAL_NAMESPACE="default"
export TEMPORAL_ADDRESS="localhost:7233"
```

After setting the environment variables, use the following code to create the Temporal Client:

```csharp
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

If you don't want to use environment variables or a configuration file, you can specify connection options directly in
code. This is convenient for local development and testing. You can also load a base configuration from environment
variables or a configuration file, and then override specific options in code.

```csharp
using System;
using System.Threading.Tasks;
using Temporalio.Client;

namespace TemporalioSamples.Manual
{
    public static class ManualConnect
    {
        public static async Task RunAsync()
        {
            Console.WriteLine("--- Connecting manually to Temporal ---");

            var client = await TemporalClient.ConnectAsync(new TemporalClientConnectOptions
            {
                TargetHost = "localhost:7233",
                Namespace  = "default",
            });

            Console.WriteLine("✅ Connected to local Temporal service!");
        }
    }
}

```

</TabItem>

</Tabs>

## Connect to Temporal Cloud {/* #connect-to-temporal-cloud */}

You can connect to Temporal Cloud using either an [API key](/cloud/api-keys) or through mTLS. Connection to Temporal
Cloud or any secured Temporal Service requires additional connection options compared to connecting to an unsecured
local development instance:

- Your credentials for authentication.
  - If you are using an API key, provide the API key value.
  - If you are using mTLS, provide the mTLS CA certificate and mTLS private key.
- Your _Namespace and Account ID_ combination, which follows the format `<namespace_id>.<account_id>`.
- The recommended _endpoint_ is the gRPC Namespace endpoint: `<namespace>.<account>.tmprl.cloud:7233`.
  This endpoint works for all Namespaces and automatically directs traffic to the active region for Namespaces with [High Availability](/cloud/high-availability).
  See [accessing Namespaces](/cloud/namespaces#access-namespaces) for more information on endpoint options.

You can find the Namespace and Account ID, as well as the endpoint, on the Namespaces tab:

![The Namespace and Account ID combination on the left, and the regional endpoint on the right](/img/cloud/apikeys/namespaces-and-regional-endpoints.png)

For more information about managing and generating client certificates for Temporal Cloud, see
[How to manage certificates in Temporal Cloud](/cloud/certificates).

You can provide these connection options using environment variables, a configuration file, or directly in code.

<Tabs groupId="connect-api-key-options-dotnet" defaultValue="config-file" >

<TabItem value="config-file" label="Configuration File">

You can use a TOML configuration file to set connection options for the Temporal Client. The configuration file lets you
configure multiple profiles, each with its own set of connection options. You can then specify which profile to use when
creating the Temporal Client. For a list of all available configuration options you can set in the TOML file, refer to
[Environment Configuration](/references/client-environment-configuration).

You can use the environment variable `TEMPORAL_CONFIG_FILE` to specify the location of the TOML file or provide the path
to the file directly in code. If you don't provide the path to the configuration file, the SDK looks for it at the
default path `~/.config/temporalio/temporal.toml`.

:::info

The connection options set in configuration files have lower precedence than environment variables. This means that if
you set the same option in both the configuration file and as an environment variable, the environment variable value
overrides the option set in the configuration file.

:::

For example, the following TOML configuration file defines a `cloud` profile with the necessary connection options to
connect to Temporal Cloud via an API key:

```toml
