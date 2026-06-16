# Cloud profile for Temporal Cloud
[profile.staging]
address = "your-namespace.a1b2c.tmprl.cloud:7233"
namespace = "your-namespace"
tls_client_cert_data = "your-tls-client-cert-data"
tls_client_key_path = "your-tls-client-key-path"
```

With the connections options defined in the configuration file, use the
[`Client.connect` method](https://ruby.temporal.io/Temporalio/Client.html#connect-class_method) to create a Temporal
Client using the `staging` profile as follows. After loading the profile, you can also programmatically override
specific connection options before creating the client.

```ruby {8,14-16}
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

Ensure these environment variables exist in your environment before running your application.

Require the `temporalio/env_config` module to set connection options for the Temporal Client using environment variables.
The `Temporalio::EnvConfig::ClientConfig.load_client_connect_options` method will automatically load all environment variables. For a list of all available
environment variables and their default values, refer to
[Environment Configuration](/references/client-environment-configuration).

For example, the following code snippet loads all environment variables and creates a Temporal Client with the options
specified in those variables. If you have defined a configuration file at either the default location
(`~/.config/temporalio/temporal.toml`) or a custom location specified by the `TEMPORAL_CONFIG_FILE` environment
variable, this will also load the default profile in the configuration file. However, any options set via environment
variables will take precedence.

After setting the environment variables, use the following code to create the Temporal Client:

```ruby {9, 17}
require 'temporalio/client'
require 'temporalio/env_config'

def main
  # load_client_connect_options is a helper that loads a profile and prepares
  # the configuration for Client.connect. By default, it loads the
  # "default" profile. It also reads from environment variables. The environment
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

You can also specify connection options directly in code to connect to Temporal Cloud. To create an initial connection,
provide the endpoint, Namespace and Account ID combination, and API key values to the `Client.connect` method.

```ruby
client = Temporalio::Client.connect(
  '<endpoint>', # Endpoint
  '<namespace_id>.<account_id>', # Namespace
  api_key: '<api_key>',
  tls: true
)
```

To connect using mTLS instead of an API key, provide the mTLS certificate and private key as follows:

```ruby
client = Temporalio::Client.connect(
  '<endpoint>', # Endpoint
  '<namespace_id>.<account_id>', # Namespace
  tls: Temporalio::Client::Connection::TLSOptions.new(
    client_cert: File.read('my-client-cert.pem'),
    client_private_key: File.read('my-client-key.pem')
  )
)
```

For more information about configuring TLS to secure inter- and intra-network communication for a Temporal Service, see
[Temporal Customization Samples](https://github.com/temporalio/samples-server).

</TabItem>

</Tabs>

## Start a Workflow {/* #start-workflow */}

To start a Workflow Execution, supply:

- A Task Queue
- A Workflow Type
- Input arguments
- Workflow options such as Workflow Id

To start a Workflow Execution in Ruby, use either the `start_workflow` or `execute_workflow` methods in the Client. You
must set a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id) and [Task Queue](/task-queue) in the
parameters given to the method.

```ruby
result = my_client.execute_workflow(
  MyWorkflow, 'some-input',
  id: 'my-workflow-id', task_queue: 'my-task-queue'
)
puts "Result: #{result}"
```

## Get Workflow results {/* #get-workflow-results */}

Once a Workflow Execution is started, the Workflow Id and Run Id can be used to uniquely identify it.

You can block until the result is available, or retrieve it later using the handle.

You can also use Queries to access Workflow state and results while the Workflow is running.

Use `start_workflow` or `workflow_handle` on the Client to return a Workflow handle. Then use the `result` method to
await on the result of the Workflow.

```ruby
handle = my_client.workflow_handle('my-workflow-id')
result = handle.result
puts "Result: #{result}"
```

---

## Ruby SDK developer guide

<!-- Ruby SDK feature guidance landing page-->

![Ruby SDK Banner](/img/assets/banner-ruby-temporal.png)

## Install and get started

You can find detailed installation instructions for the Ruby SDK in the [Quickstart](/develop/ruby/set-up-local-ruby).

There's also a short walkthrough of how to use the Temporal primitives (Activities, Workflows, and Workers) to build and run a Temporal application to get you up and running.

Once your local Temporal Service is set up, continue building with the following resources:

- [Workflow basics](/develop/ruby/workflows/basics)
- [Activity basics](/develop/ruby/activities/basics)
- [Start an Activity execution](/develop/ruby/activities/execution)
- [Run Worker processes](/develop/ruby/workers/run-worker-process)

From there, you can dive deeper into any of the Temporal primitives to start building Workflows that fit your use cases.

## [Workflows](/develop/ruby/workflows)

- [Workflow basics](/develop/ruby/workflows/basics)
- [Child Workflows](/develop/ruby/workflows/child-workflows)
- [Continue-As-New](/develop/ruby/workflows/continue-as-new)
- [Cancellation](/develop/ruby/workflows/cancellation)
- [Timeouts](/develop/ruby/workflows/timeouts)
- [Message Passing](/develop/ruby/workflows/message-passing)
- [Schedules](/develop/ruby/workflows/schedules)
- [Timers](/develop/ruby/workflows/timers)
- [Futures](/develop/ruby/workflows/futures)
- [Dynamic Workflow](/develop/ruby/workflows/dynamic-workflow)
- [Versioning](/develop/ruby/workflows/versioning)

## [Activities](/develop/ruby/activities)

- [Activity basics](/develop/ruby/activities/basics)
- [Activity execution](/develop/ruby/activities/execution)
- [Standalone Activities](/develop/ruby/activities/standalone-activities)
- [Timeouts](/develop/ruby/activities/timeouts)
- [Asynchronous Activity completion](/develop/ruby/activities/asynchronous-activity)
- [Dynamic Activity](/develop/ruby/activities/dynamic-activity)
- [Benign exceptions](/develop/ruby/activities/benign-exceptions)

## [Workers](/develop/ruby/workers)

- [Worker processes](/develop/ruby/workers/run-worker-process)
- [Observability](/develop/ruby/platform/observability)

## [Temporal Client](/develop/ruby/client)

- [Temporal Client](/develop/ruby/client/temporal-client)

## [Platform](/develop/ruby/platform)

- [Observability](/develop/ruby/platform/observability)
- [Enriching the UI](/develop/ruby/platform/enriching-ui)

## [Integrations](/develop/ruby/integrations)

- [Rails integration](/develop/ruby/integrations/rails-integration)

## [Best practices](/develop/ruby/best-practices)

- [Error handling](/develop/ruby/best-practices/error-handling)
- [Testing](/develop/ruby/best-practices/testing-suite)
- [Debugging](/develop/ruby/best-practices/debugging)
- [Converters and encryption](/develop/ruby/best-practices/converters-and-encryption)

## Temporal Ruby Technical Resources

- [Ruby SDK Quickstart - Setup Guide](https://docs.temporal.io/develop/ruby/set-up-local-ruby)
- [Ruby SDK Code Samples](https://github.com/temporalio/samples-ruby)
- [Ruby API Documentation](https://ruby.temporal.io/)
- [Ruby SDK GitHub](https://github.com/temporalio/sdk-ruby)
- [Temporal 101 in Ruby Free Course](https://learn.temporal.io/courses/temporal_101/ruby/)

## Get Connected with the Temporal Ruby Community

- [Temporal Ruby Community Slack](https://temporalio.slack.com/archives/C052K5QFBNW)
- [Ruby SDK Forum](https://community.temporal.io/tag/ruby-sdk)

---

## Integrations - Ruby SDK

The following integrations are available for the Temporal Ruby SDK.

<IntegrationsGrid defaultSdks={["Ruby"]} />

---

## Rails integration - Ruby SDK

Temporal Ruby SDK is a generic Ruby library that can work in any Ruby environment.
However, there are some common conventions for Rails users to be aware of.

See the [rails_app sample](https://github.com/temporalio/samples-ruby/tree/main/rails_app) for an example of using Temporal from Rails.

## ActiveRecord

For ActiveRecord, or other general/ORM models that are used for a different purpose, it is not recommended to try to reuse them as Temporal models.
Eventually model purposes diverge and models for a Temporal workflows/activities should be specific to their use for clarity and compatibility reasons.
Also many Ruby ORMs do many lazy things and therefore provide unclear serialization semantics.
Instead, consider having models specific for Workflows/Activities and translate to/from existing models as needed.
See the [ActiveModel section](/develop/ruby/best-practices/converters-and-encryption#active-model) on how to do this with ActiveModel objects.

## Lazy/Eager Loading

By default, Rails eagerly loads all application code on application start in production, but lazily loads it in non-production environments.
Temporal Workflows by default disallow use of IO during the Workflow run.
With lazy loading enabled in dev/test environments, when an Activity class is referenced in a Workflow before it has been explicitly required, it can give an error like:

```
Cannot access File path from inside a workflow. If this is known to be safe, the code can be run in a Temporalio::Workflow::Unsafe.illegal_call_tracing_disabled block.
```

This comes from bootsnap via zeitwerk because it is lazily loading a class/module at Workflow runtime.
It is not good to lazily load code during a Workflow run because it can be side effecting.
Workflows and the classes they reference should be eagerly loaded.

To resolve this, either always eagerly load (e.g. `config.eager_load = true`) or explicitly require what is used by a workflow at the top of the file.

Note, this only affects non-production environments.

---

## Enriching the user interface - Ruby SDK

Temporal supports adding context to Workflows and Events with metadata.
This helps users identify and understand Workflows and their operations.

## Adding Summary and Details to Workflows

### Starting a Workflow

When starting a Workflow, you can provide a static summary and details to help identify the Workflow in the UI:

```ruby
require 'temporalio/client'
