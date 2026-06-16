# Optional gRPC metadata for observability or routing
temporal --profile prod config set --prop grpc_meta.environment --value "production"
temporal --profile prod config set --prop grpc_meta.service-version --value "v1.2.3"
```

  </TabItem>
</Tabs>

## Load configuration profile and environment variables

If you don't specify a profile, the SDKs load the `default` profile and the environment variables. If you haven't set
`TEMPORAL_CONFIG_FILE`, the SDKs will look for the configuration file in the default location. Refer to
[Configuration methods](#configuration-methods) for the default locations for your operating system.

No matter what profile you choose to load, environment variables are always loaded when you use the APIs in the
environment configuration package to load Temporal Client connection options. They always take precedence over TOML file
settings in the profiles.

<SdkTabs hideUnsupportedLanguages>
  <SdkTabs.Python>

To load the `default` profile along with any environment variables in Python, use the `ClientConfigProfile.load()`
method from the `temporalio.envconfig` package.

```python {7-8}

from temporalio.client import Client
from temporalio.envconfig import ClientConfigProfile

async def main():
    # Load the "default" profile from default locations and environment variables.
    default_profile = ClientConfigProfile.load()
    connect_config = default_profile.to_client_connect_config()

    # Connect to the client using the loaded configuration.
    client = await Client.connect(**connect_config)
    print(f"✅ Client connected to {client.service_client.config.target_host} in namespace '{client.namespace}'")

if __name__ == "__main__":
    asyncio.run(main())
```

  </SdkTabs.Python>
  <SdkTabs.Go>

To load the `default` profile along with any environment variables in Go, use the
`envconfig.MustLoadDefaultClientOptions()` function from the `temporalio.envconfig` package.

```go {13}
package main

	"fmt"
	"log"

	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/contrib/envconfig"
)

func main() {
	// Loads the "default" profile from the standard location and environment variables.
	c, err := client.Dial(envconfig.MustLoadDefaultClientOptions())
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}
	defer c.Close()

	fmt.Printf("✅ Connected to Temporal Service")
}
```

  </SdkTabs.Go>
  <SdkTabs.Ruby>

To load the `default` profile along with any environment variables in Ruby, use the
`EnvConfig::ClientConfig.load_client_connect_options()` method from the `temporalio.env_config` package.

```Ruby {16-18}
require 'temporalio/client'
require 'temporalio/env_config'

def main
  puts '--- Loading default profile from config.toml ---'

  # For this sample to be self-contained, we explicitly provide the path to
  # the config.toml file included in this directory.
  # By default though, the config.toml file will be loaded from
  # ~/.config/temporalio/temporal.toml (or the equivalent standard config directory on your OS).
  config_file = File.join(__dir__, 'config.toml')

  # load_client_connect_options is a helper that loads a profile and prepares
  # the configuration for Client.connect. By default, it loads the
  # "default" profile.
  args, kwargs = Temporalio::EnvConfig::ClientConfig.load_client_connect_options(
    config_source: Pathname.new(config_file)
  )

  puts "Loaded 'default' profile from #{config_file}."
  puts "  Address: #{args[0]}"
  puts "  Namespace: #{args[1]}"
  puts "  gRPC Metadata: #{kwargs[:rpc_metadata]}"

  puts "\nAttempting to connect to client..."
  begin
    client = Temporalio::Client.connect(*args, **kwargs)
    puts '✅ Client connected successfully!'
    sys_info = client.workflow_service.get_system_info(Temporalio::Api::WorkflowService::V1::GetSystemInfoRequest.new)
    puts "✅ Successfully verified connection to Temporal server!\n#{sys_info}"
  rescue StandardError => e
    puts "❌ Failed to connect: #{e}"
  end
end
```

  </SdkTabs.Ruby>

  <SdkTabs.DotNet>

To load the `default` profile along with any environment variables in .NET C#, use the
`ClientEnvConfig.LoadClientConnectOptions()` method from the `Temporalio.Client.EnvConfig` package.

```csharp {22,27-30}
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

  </SdkTabs.DotNet>

  <SdkTabs.TypeScript>
To load the `default` profile along with any environment variables in TypeScript, use the `loadClientConnectConfig` helper from `@temporalio/envconfig` package.

{/* SNIPSTART typescript-env-config-load-default-profile {"highlightedLines": "17-19,28-29"} */}
[env-config/src/load-from-file.ts](https://github.com/temporalio/samples-typescript/blob/main/env-config/src/load-from-file.ts)
```ts {17-19,28-29}

async function main() {
  console.log('--- Loading default profile from config.toml ---');

  // For this sample to be self-contained, we explicitly provide the path to
  // the config.toml file included in this directory.
  // By default though, the config.toml file will be loaded from
  // ~/.config/temporalio/temporal.toml (or the equivalent standard config directory on your OS).
  const configFile = resolve(__dirname, '../config.toml');

  // loadClientConnectConfig is a helper that loads a profile and prepares
  // the configuration for Connection.connect and Client. By default, it loads the
  // "default" profile.
  const config = loadClientConnectConfig({
    configSource: { path: configFile },
  });

  console.log(`Loaded 'default' profile from ${configFile}.`);
  console.log(`  Address: ${config.connectionOptions.address}`);
  console.log(`  Namespace: ${config.namespace}`);
  console.log(`  gRPC Metadata: ${JSON.stringify(config.connectionOptions.metadata)}`);

  console.log('\nAttempting to connect to client...');
  try {
    const connection = await Connection.connect(config.connectionOptions);
    const client = new Client({ connection, namespace: config.namespace });
    console.log('✅ Client connected successfully!');
    await connection.close();
  } catch (err) {
    console.log(`❌ Failed to connect: ${err}`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
```
{/* SNIPEND */}

  </SdkTabs.TypeScript>

  <SdkTabs.Java>

To load the `default` profile along with any environment variables in Java, use the `ClientConfigProfile.load` method
from the `envconfig` package. This method will load the `default` profile from the default location and any environment
variables. Environment variables take precedence over the configuration file settings.

Then use `profile.toWorkflowServiceStubsOptions` and `profile.toWorkflowClientOptions` to convert the profile to
`WorkflowServiceStubsOptions` and `WorkflowClientOptions` respectively. Then use `WorkflowClient.newInstance` to create
a Temporal Client.

```java

public class LoadFromFile {

  private static final Logger logger = LoggerFactory.getLogger(LoadFromFile.class);

  public static void main(String[] args) {
    try {

      ClientConfigProfile profile = ClientConfigProfile.load(LoadClientConfigProfileOptions.newBuilder().build());

      WorkflowServiceStubsOptions serviceStubsOptions = profile.toWorkflowServiceStubsOptions();
      WorkflowClientOptions clientOptions = profile.toWorkflowClientOptions();

      try {
        // Create the workflow client using the loaded configuration
        WorkflowClient client =
            WorkflowClient.newInstance(
                WorkflowServiceStubs.newServiceStubs(serviceStubsOptions), clientOptions);

        // Test the connection by getting system info
        var systemInfo =
            client
                .getWorkflowServiceStubs()
                .blockingStub()
                .getSystemInfo(
                    io.temporal.api.workflowservice.v1.GetSystemInfoRequest.getDefaultInstance());

        logger.info("✅ Client connected successfully!");
        logger.info("   Server version: {}", systemInfo.getServerVersion());

      } catch (Exception e) {
        logger.error("❌ Failed to connect: {}", e.getMessage());
      }

    } catch (Exception e) {
      logger.error("Failed to load configuration: {}", e.getMessage(), e);
      System.exit(1);
    }
  }
}
```

  </SdkTabs.Java>
</SdkTabs>

## Load configuration from a custom path

To load configuration from a non-standard file location without relying on the `TEMPORAL_CONFIG_FILE` environment
variable, you can use a function from the `temporalio.envconfig` package. The specific method you need to call depends
on the SDK you are using.

This is useful if you store application-specific configurations separately. Loading connection options using this method
will still respect environment variables, which take precedence over the file settings.

<SdkTabs hideUnsupportedLanguages>

<SdkTabs.Python>

To load a specific profile from a custom path in Python, use the `ClientConfig.load_client_connect_config()` method with
the `config_file` parameter. In this example, we construct the path to a `config.toml` file located in the same
directory as the script.

After loading the connection options, you can override specific settings programmatically before passing them to
`Client.connect()`.

```py {12-13,21-23}

from pathlib import Path
from temporalio.client import Client
from temporalio.envconfig import ClientConfig

async def main():
    """
    Demonstrates loading a named profile and overriding values programmatically.
    """
    print("--- Loading 'staging' profile with programmatic overrides ---")

    config_file = Path(__file__).parent / "config.toml"
    profile_name = "staging"

    print(
        "The 'staging' profile in config.toml has an incorrect address (localhost:9999)."
    )
    print("We'll programmatically override it to the correct address.")

    # Load the 'staging' profile.
    connect_config = ClientConfig.load_client_connect_config(
        profile=profile_name,
        config_file=str(config_file),
    )

    # Override the target host to the correct address.
    # This is the recommended way to override configuration values.
    connect_config["target_host"] = "localhost:7233"

    print(f"\nLoaded '{profile_name}' profile from {config_file} with overrides.")
    print(
        f"  Address: {connect_config.get('target_host')} (overridden from localhost:9999)"
    )
    print(f"  Namespace: {connect_config.get('namespace')}")

    print("\nAttempting to connect to client...")
    try:
        await Client.connect(**connect_config)  # type: ignore
        print("✅ Client connected successfully!")
    except Exception as e:
        print(f"❌ Failed to connect: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

</SdkTabs.Python>

<SdkTabs.Go>

To load a specific profile from a custom filepath in Go, use the `envconfig.LoadClientOptions()` function with the
`ConfigFilePath` field set in the `LoadClientOptionsRequest` struct. Use the `ConfigFileProfile` field to specify the
profile name.

After loading the connection options, you can override specific settings programmatically before passing them to
`client.Dial()`. Refer to the [GO SDK API documentation](https://pkg.go.dev/go.temporal.io/sdk/contrib/envconfig) for
all available options.

```go {14-16}
package main

	"fmt"
	"log"

	"go.temporal.io/sdk/client"
	"go.temporal.io/sdk/contrib/envconfig"
)

func main() {
  // Load a specific profile from the TOML config file.
  // This requires a [profile.prod] section in your config.
  opts, err := envconfig.LoadClientOptions(envconfig.LoadClientOptionsRequest{
    ConfigFileProfile: "prod",
    ConfigFilePath:    "/Users/yourname/.config/my-app/temporal.toml",
  })
  if err != nil {
    log.Fatalf("Failed to load 'prod' profile: %v", err)
  }

  // Programmatically override the Namespace value.
  opts.Namespace = "new-namespace"

  c, err := client.Dial(opts)
  if err != nil {
    log.Fatalf("Failed to connect using 'prod' profile: %v", err)
  }
  defer c.Close()

  fmt.Printf("✅ Connected to Temporal namespace %q on %s using 'prod' profile\n", c.Options().Namespace, c.Options().HostPort)
}
```

</SdkTabs.Go>

<SdkTabs.Ruby>

To load a specific profile from a custom path in Ruby, use the `EnvConfig::ClientConfig.load_client_connect_options()`
method with the `config_source` parameter. In this example, we construct the path to a `config.toml` file located in the
same directory as the script. Use the `profile` parameter to specify the profile name.

After loading the connection options, you can override specific settings programmatically before passing them to
`Client.connect()`. Refer to the [Ruby SDK API documentation](https://ruby.temporal.io/Temporalio/EnvConfig.html) for
all available options.

```Ruby {7-8,14-16}
require 'temporalio/client'
require 'temporalio/env_config'

def main
  puts "--- Loading 'staging' profile with programmatic overrides ---"

  config_file = File.join(__dir__, 'config.toml')
  profile_name = 'staging'

  puts "The 'staging' profile in config.toml has an incorrect address (localhost:9999)."
  puts "We'll programmatically override it to the correct address."

  # Load the 'staging' profile.
  args, kwargs = Temporalio::EnvConfig::ClientConfig.load_client_connect_options(
    profile: profile_name,
    config_source: Pathname.new(config_file)
  )

  # Override the target host to the correct address.
  # This is the recommended way to override configuration values.
  args[0] = 'localhost:7233'

  puts "\nLoaded '#{profile_name}' profile from #{config_file} with overrides."
  puts "  Address: #{args[0]} (overridden from localhost:9999)"
  puts "  Namespace: #{args[1]}"

  puts "\nAttempting to connect to client..."
  begin
    client = Temporalio::Client.connect(*args, **kwargs)
    puts '✅ Client connected successfully!'
    sys_info = client.workflow_service.get_system_info(Temporalio::Api::WorkflowService::V1::GetSystemInfoRequest.new)
    puts "✅ Successfully verified connection to Temporal server!\n#{sys_info}"
  rescue StandardError => e
    puts "❌ Failed to connect: #{e}"
  end
end

main if $PROGRAM_NAME == __FILE__
```

</SdkTabs.Ruby>

<SdkTabs.DotNet>

To load a specific profile from a custom path in .NET C#, use the `ClientEnvConfig.LoadClientConnectOptions()` method
with the `ProfileLoadOptions` parameter. Use the `Profile` property to specify the profile name and the `ConfigSource`
property to specify the file path.

After loading the connection options, you can override specific settings programmatically before passing them to
`TemporalClient.ConnectAsync()`. Refer to the
[C# SDK API documentation](https://dotnet.temporal.io/api/Temporalio.Common.EnvConfig.html) for all available options.

```csharp {18-19,25-28}
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

</SdkTabs.DotNet>

<SdkTabs.TypeScript>

To load a specific profile from a custom path in TypeScript, use the `loadClientConnectConfig` helper from
`@temporalio/envconfig` package with the `profile` and `configFile` options.

{/* SNIPSTART typescript-env-config-load-default-profile {"highlightedLines": "17-19,28-29"} */}
[env-config/src/load-from-file.ts](https://github.com/temporalio/samples-typescript/blob/main/env-config/src/load-from-file.ts)
```ts {17-19,28-29}

async function main() {
  console.log('--- Loading default profile from config.toml ---');

  // For this sample to be self-contained, we explicitly provide the path to
  // the config.toml file included in this directory.
  // By default though, the config.toml file will be loaded from
  // ~/.config/temporalio/temporal.toml (or the equivalent standard config directory on your OS).
  const configFile = resolve(__dirname, '../config.toml');

  // loadClientConnectConfig is a helper that loads a profile and prepares
  // the configuration for Connection.connect and Client. By default, it loads the
  // "default" profile.
  const config = loadClientConnectConfig({
    configSource: { path: configFile },
  });

  console.log(`Loaded 'default' profile from ${configFile}.`);
  console.log(`  Address: ${config.connectionOptions.address}`);
  console.log(`  Namespace: ${config.namespace}`);
  console.log(`  gRPC Metadata: ${JSON.stringify(config.connectionOptions.metadata)}`);

  console.log('\nAttempting to connect to client...');
  try {
    const connection = await Connection.connect(config.connectionOptions);
    const client = new Client({ connection, namespace: config.namespace });
    console.log('✅ Client connected successfully!');
    await connection.close();
  } catch (err) {
    console.log(`❌ Failed to connect: ${err}`);
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
```
{/* SNIPEND */}

</SdkTabs.TypeScript>

<SdkTabs.Java>

To load a profile configuration file from a custom path in Java, use the `ClientConfigProfile.load` method from the
`envconfig` package with the `ConfigFilePath` parameter. This method will load the profile from the custom path and any
environment variables. Environment variables take precedence over the configuration file settings.

```java {21-25}

public class LoadFromFile {

  private static final Logger logger = LoggerFactory.getLogger(LoadFromFile.class);

  public static void main(String[] args) {
    try {

      String configFilePath =
          Paths.get(LoadFromFile.class.getResource("/config.toml").toURI()).toString();

      ClientConfigProfile profile =
          ClientConfigProfile.load(
              LoadClientConfigProfileOptions.newBuilder()
                  .setConfigFilePath(configFilePath)
                  .build());

      WorkflowServiceStubsOptions serviceStubsOptions = profile.toWorkflowServiceStubsOptions();
      WorkflowClientOptions clientOptions = profile.toWorkflowClientOptions();

      try {
        // Create the workflow client using the loaded configuration
        WorkflowClient client =
            WorkflowClient.newInstance(
                WorkflowServiceStubs.newServiceStubs(serviceStubsOptions), clientOptions);

        // Test the connection by getting system info
        var systemInfo =
            client
                .getWorkflowServiceStubs()
                .blockingStub()
                .getSystemInfo(
                    io.temporal.api.workflowservice.v1.GetSystemInfoRequest.getDefaultInstance());

        logger.info("✅ Client connected successfully!");
        logger.info("   Server version: {}", systemInfo.getServerVersion());

      } catch (Exception e) {
        logger.error("❌ Failed to connect: {}", e.getMessage());
      }

    } catch (Exception e) {
      logger.error("Failed to load configuration: {}", e.getMessage(), e);
      System.exit(1);
    }
  }
}
```

</SdkTabs.Java>

</SdkTabs>

---

## Asynchronous Activity completion - Go SDK

[Asynchronous Activity Completion](/activity-execution#asynchronous-activity-completion) enables the Activity Function to return without the Activity Execution completing.

There are three steps to follow:

1. The Activity provides the external system with identifying information needed to complete the Activity Execution.
   Identifying information can be a [Task Token](/activity-execution#task-token), or a combination of Namespace, Workflow Id, and Activity Id.
2. The Activity Function completes in a way that identifies it as waiting to be completed by an external system.
3. The Temporal Client is used to Heartbeat and complete the Activity.

**Step 1: Provide the external system with a Task Token to complete the Activity Execution.**
   To do this, use the `GetInfo()` API from the `go.temporal.io/sdk/activity` package.

```go
// Retrieve the Activity information needed to asynchronously complete the Activity.
activityInfo := activity.GetInfo(ctx)
taskToken := activityInfo.TaskToken
// Send the taskToken to the external service that will complete the Activity.
```

**Step 2: Return an `activity.ErrResultPending` error to indicate that the Activity is completing asynchronously.**

```go
return "", activity.ErrResultPending
```

**Step 3: Use the Temporal Client to complete the Activity using the Task Token.**

```go
// Instantiate a Temporal service client.
// The same client can be used to complete or fail any number of Activities.
// The client is a heavyweight object that should be created once per process.
temporalClient, err := client.Dial(client.Options{})

// Complete the Activity.
temporalClient.CompleteActivity(context.Background(), taskToken, result, nil)
```

The following are the parameters of the `CompleteActivity` function:

- `taskToken`: The value of the binary `TaskToken` field of the `ActivityInfo` struct retrieved inside
  the Activity.
- `result`: The return value to record for the Activity. The type of this value must match the type
  of the return value declared by the Activity function.
- `err`: The error code to return if the Activity terminates with an error.

If `err` is not null, the value of the `result` field is ignored.

To fail the Activity, you would do the following:

```go
// Fail the Activity.
client.CompleteActivity(context.Background(), taskToken, nil, err)
```

---

## Activity basics - Go SDK
