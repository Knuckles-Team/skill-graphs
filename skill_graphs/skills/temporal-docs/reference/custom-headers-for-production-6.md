# Custom headers for production
[profile.prod.grpc_meta]
environment     = "production"
service-version = "v1.2.3"
```

You can create a Temporal Client using a profile from the configuration file using the
`ClientConfig.load_client_connect_options` function as follows. In this example, you load the `default` profile for
local development:

```ruby
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

main if $PROGRAM_NAME == __FILE__
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

Set the following environment variables before running your application. Replace the placeholder values with your actual
configuration. Since this is for a local development Temporal Service, the values connect to `localhost:7233` and the
`default` Namespace. You may omit these variables entirely since they're the defaults.

```bash
export TEMPORAL_NAMESPACE="default"
export TEMPORAL_ADDRESS="localhost:7233"
```

After setting the environment variables, you can create a Temporal Client as follows:

```ruby {9}
require 'temporalio/client'
require 'temporalio/env_config'

def main
  # load_client_connect_options is a helper that loads a profile and prepares
  # the configuration for Client.connect. By default, it loads the
  # "default" profile and also reads from environment variables. The environment
  # variables take precedence over the config file.
  args, kwargs = Temporalio::EnvConfig::ClientConfig.load_client_connect_options()

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

main if $PROGRAM_NAME == __FILE__
```

</TabItem>

<TabItem value="code" label="Code">

If you don't want to use environment variables or a configuration file, you can specify connection options directly in
code. This is convenient for local development and testing. You can also load a base configuration from environment
variables or a configuration file, and then override specific options in code.

Use the `connect` class method on the `Temporalio::Client` class to create and connect to a Temporal Client to the
Temporal Service.

```ruby
client = Temporalio::Client.connect('localhost:7233', 'default')
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

<Tabs groupId="connect-api-key-options" defaultValue="config-file" >

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

For example, the following TOML configuration file defines a `staging` profile with the necessary connection options to
connect to Temporal Cloud via an API key:

```toml
