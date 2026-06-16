# Wait for the result later
puts "Activity result: #{handle.result}"
```

With the Temporal Server and Worker running, open a new terminal in the `samples-ruby` directory and
run:

```bash
bundle exec ruby standalone_activity/start_activity.rb
```

Or use the Temporal CLI:

```bash
temporal activity start \
  --type ComposeGreeting \
  --activity-id standalone-activity-id \
  --task-queue standalone-activity-sample \
  --start-to-close-timeout 10s \
  --input '"Hello"' \
  --input '"World"'
```

## Get a handle to an existing Standalone Activity {/* #get-activity-handle */}

Use [`Temporalio::Client#activity_handle`](https://ruby.temporal.io/Temporalio/Client.html#activity_handle-instance_method) to create an [`ActivityHandle`](https://ruby.temporal.io/Temporalio/Client/ActivityHandle.html) for a previously started Standalone Activity:

```ruby
handle = client.activity_handle('standalone-activity-id')
```

Pass no run ID (the default) to target the latest run of the given Activity ID, or pass
`activity_run_id:` to target a specific run. You can then use the handle to wait for the result,
describe, cancel, or terminate the Activity:

```ruby
handle.result      # block until the activity completes; returns the result
handle.describe    # fetch metadata (status, timestamps, attempt, last failure, etc.)
handle.cancel      # request cancellation
handle.terminate   # force-close the activity
```

## Wait for the result of a Standalone Activity {/* #get-activity-result */}

Under the hood, calling `client.execute_activity` is the same as calling `client.start_activity` to
durably enqueue the Standalone Activity, and then calling `handle.result` to block until the
Activity completes and return the result:

```ruby
result = handle.result
```

Or use the Temporal CLI to wait for a result by Activity ID:

```bash
temporal activity result --activity-id standalone-activity-id
```

## List Standalone Activities {/* #list-activities */}

Use [`Temporalio::Client#list_activities`](https://ruby.temporal.io/Temporalio/Client.html#list_activities-instance_method) to list
Standalone Activity Executions that match a [List Filter](/list-filter) query. The result is an
`Enumerator` of [`ActivityExecution`](https://ruby.temporal.io/Temporalio/Client/ActivityExecution.html) values that fetches pages from the server on demand as the
enumerator is consumed.

These APIs return only Standalone Activity Executions. Activities running inside Workflows are not
included.

[list_activities.rb](https://github.com/temporalio/samples-ruby/blob/main/standalone_activity/list_activities.rb)

```ruby
client.list_activities("TaskQueue = 'standalone-activity-sample'").each do |execution|
  puts "#{execution.activity_id} #{execution.activity_type} #{execution.status}"
end
```

Run it:

```bash
bundle exec ruby standalone_activity/list_activities.rb
```

Or use the Temporal CLI:

```bash
temporal activity list
```

The query parameter accepts the same [List Filter](/list-filter) syntax used for [Workflow
Visibility](/visibility). For example, `ActivityType = 'ComposeGreeting' AND Status = 'Running'`.

## Count Standalone Activities {/* #count-activities */}

Use [`Temporalio::Client#count_activities`](https://ruby.temporal.io/Temporalio/Client.html#count_activities-instance_method) to count
Standalone Activity Executions that match a [List Filter](/list-filter) query. This returns the
total count of executions (running, completed, failed, etc.) — not the number of queued tasks. It
works the same way as counting Workflow Executions.

[count_activities.rb](https://github.com/temporalio/samples-ruby/blob/main/standalone_activity/count_activities.rb)

```ruby
result = client.count_activities("TaskQueue = 'standalone-activity-sample'")
puts "Total: #{result.count}"
result.groups.each do |group|
  puts "  #{group.group_values.join(',')} => #{group.count}"
end
```

Run it:

```bash
bundle exec ruby standalone_activity/count_activities.rb
```

Or use the Temporal CLI:

```bash
temporal activity count
```

## Run Standalone Activities with Temporal Cloud {/* #run-standalone-activities-temporal-cloud */}

The code samples on this page use [`Temporalio::EnvConfig::ClientConfig.load_client_connect_options`](https://ruby.temporal.io/Temporalio/EnvConfig/ClientConfig.html#load_client_connect_options-class_method),
so the same code works against Temporal Cloud — just configure the connection via environment
variables or a TOML profile. No code changes are needed.

For a step-by-step guide on connecting to Temporal Cloud, including Namespace creation, certificate
generation, and authentication setup in the Cloud UI, see
[Connect to Temporal Cloud](/develop/ruby/client/temporal-client#connect-to-temporal-cloud).

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

## Activity Timeouts - Ruby SDK

## Activity timeouts {/* #activity-timeouts */}

Each Activity Timeout controls a different aspect of how long an Activity Execution can take:

- **[Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout)**
- **[Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout)**
- **[Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout)**

At least one of `start_to_close_timeout` or `schedule_to_close_timeout` is required.

```ruby
Temporalio::Workflow.execute_activity(
  MyActivity,
  { greeting: 'Hello', name: },
  start_to_close_timeout: 5 * 60
)
```

### Activity Retry Policy {/* #activity-retries */}

By default, Activities use a system Retry Policy.
You can override it by specifying a custom Retry Policy.

To create an Activity Retry Policy in Ruby, set the `retry_policy` parameter when executing an activity.

```ruby
Temporalio::Workflow.execute_activity(
  MyActivity,
  { greeting: 'Hello', name: },
  start_to_close_timeout: 5 * 60,
  retry_policy: Temporalio::RetryPolicy.new(max_interval: 10)
)
```

### Override the retry interval with `next_retry_delay` {/* #next-retry-delay */}

If you raise an application-level error, you can override the Retry Policy's delay by specifying a new delay.

```ruby
raise Temporalio::Error::ApplicationError.new(
  'Some error',
  type: 'SomeErrorType',
  next_retry_delay: 3 * Temporalio::Activity::Context.current.info.attempt
)
```

## Heartbeat an Activity {/* #activity-heartbeats */}

A Heartbeat is a periodic signal from the Worker to the Temporal Service indicating the Activity is still alive and making progress.

- Heartbeats are used to detect Worker failure.
- Cancellations are delivered via Heartbeats.
- Heartbeats may contain custom progress details.

```ruby
class MyActivity < Temporalio::Activity::Definition
  def execute
    # This is a naive loop simulating work, but similar heartbeat logic
    # applies to other scenarios as well
    loop do
      # Send heartbeat
      Temporalio::Activity::Context.current.heartbeat
      # Sleep before heartbeating again
      sleep(3)
    end
  end
end
```

### Heartbeat Timeout {/* #heartbeat-timeout */}

The Heartbeat Timeout sets the maximum duration between Heartbeats before the Temporal Service considers the Activity failed.

```ruby
Temporalio::Workflow.execute_activity(
  MyActivity,
  { greeting: 'Hello', name: },
  start_to_close_timeout: 5 * 60,
  heartbeat_timeout: 5
)
```

---

## Converters and encryption - Ruby SDK

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

The Payload Codec needs to extend `Temporalio::Converters::PayloadCodec` and implement `encode` and `decode` methods.
These should convert the given payloads as needed into new payloads, using the `"encoding"` metadata field.
Do not mutate the existing payloads.
Here is an example of an encryption codec that just uses base64 in each direction:

```ruby
class Base64Codec < Temporalio::Converters::PayloadCodec
  def encode(payloads)
    payloads.map do |p|
      Temporalio::Api::Common::V1::Payload.new(
        # Set our specific encoding. We may also want to add a key ID in here for use by
        # the decode side
        metadata: { 'encoding' => 'binary/my-payload-encoding' },
        data: Base64.strict_encode64(p.to_proto)
      )
    end
  end

  def decode(payloads)
    payloads.map do |p|
      # Ignore if it doesn't have our expected encoding
      next p unless p.metadata['encoding'] == 'binary/my-payload-encoding'

      Temporalio::Api::Common::V1::Payload.decode(
        Base64.strict_decode64(p.data)
      )
    end
  end
end
```

**Set Data Converter to use custom Payload Codec**

When creating a client, the default `DataConverter` can be updated with the payload codec like so:

```ruby
my_client = Temporalio::Client.connect(
  'localhost:7233',
  'my-namespace',
  data_converter: Temporalio::Converters::DataConverter.new(payload_codec: Base64Codec.new)
)
```

- Data **encoding** is performed by the client using the converters and codecs provided by Temporal or your custom implementation when passing input to the Temporal Cluster. For example, plain text input is usually serialized into a JSON object, and can then be compressed or encrypted.
- Data **decoding** may be performed by your application logic during your Workflows or Activities as necessary, but decoded Workflow results are never persisted back to the Temporal Cluster.
  Instead, they are stored encoded on the Cluster, and you need to provide an additional parameter when using the [temporal workflow show](/cli/command-reference/workflow#show) command or when browsing the Web UI to view output.

<!-- TODO: For reference, see the [Encryption](https://github.com/temporalio/samples-ruby/tree/main/encryption) sample. -->

### Using a Codec Server

A Codec Server is an HTTP server that uses your custom Codec logic to decode your data remotely.
The Codec Server is independent of the Temporal Cluster and decodes your encrypted payloads through predefined endpoints.
You create, operate, and manage access to your Codec Server in your own environment.
The Temporal CLI and the Web UI in turn provide built-in hooks to call the Codec Server to decode encrypted payloads on demand.
Refer to the [Codec Server](/production-deployment/data-encryption) documentation for information on how to design and deploy a Codec Server.

## Payload conversion {/* #custom-payload-converter */}

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

### Supported Data Types {/* #supported-data-types */}

Data converters are used to convert raw Temporal payloads to/from actual Ruby types.
A custom data converter can be set via the `data_converter` keyword argument when creating a client. Data converters are a combination of payload converters, payload codecs, and failure converters.
Payload converters convert Ruby values to/from serialized bytes. Payload codecs convert bytes to bytes (e.g. for compression or encryption). Failure converters convert exceptions to/from serialized failures.

Data converters are in the `Temporalio::Converters` module.
The default data converter uses a default payload converter, which supports the following types:

- `nil`
- "bytes" (i.e. `String` with `Encoding::ASCII_8BIT` encoding)
- `Google::Protobuf::MessageExts` instances
- [JSON module](https://docs.ruby-lang.org/en/master/JSON.html) for everything else

This means that normal Ruby objects will use `JSON.generate` when serializing and `JSON.parse` when deserializing (with `create_additions: true` set by default).
So a Ruby object will often appear as a hash when deserialized.
Also, hashes that are passed in with symbol keys end up with string keys when deserialized.
While "JSON Additions" are supported, it is not cross-SDK-language compatible since this is a Ruby-specific construct.

The default payload converter is a collection of "encoding payload converters".
On serialize, each encoding converter will be tried in order until one accepts (default falls through to the JSON one).
The encoding converter sets an `encoding` metadata value which is used to know which converter to use on deserialize.
Custom encoding converters can be created, or even the entire payload converter can be replaced with a different implementation.

**NOTE:** For ActiveRecord, or other general/ORM models that are used for a different purpose, it is not recommended to try to reuse them as Temporal models.
Eventually model purposes diverge and models for a Temporal workflows/activities should be specific to their use for clarity and compatibility reasons.
Also many Ruby ORMs do many lazy things and therefore provide unclear serialization semantics.
Instead, consider having models specific for workflows/activities and translate to/from existing models as needed.
See the next section on how to do this with ActiveModel objects.

#### ActiveModel {/* #active-model */}

By default, ActiveModel objects do not natively support the `JSON` module.
A mixin can be created to add this support for ActiveModel, for example:

```ruby
module ActiveModelJSONSupport
  extend ActiveSupport::Concern
  include ActiveModel::Serializers::JSON

  included do
    def as_json(*)
      super.merge(::JSON.create_id => self.class.name)
    end

    def to_json(*args)
      as_json.to_json(*args)
    end

    def self.json_create(object)
      object = object.dup
      object.delete(::JSON.create_id)
      new(**object.symbolize_keys)
    end
  end
end
```

Now if `include ActiveModelJSONSupport` is present on any ActiveModel class, on serialization `to_json` will be used which will use `as_json` which calls the super `as_json` but also includes the fully qualified class name as the JSON
`create_id` key.
On deserialization, Ruby JSON then uses this key to know what class to call `json_create` on.

---

## Debugging - Ruby SDK

## Debugging {/* #debug */}

This page shows how to do the following:

- [Debug in a development environment](#debug-in-a-development-environment)
- [Debug in a production environment](#debug-in-a-production-environment)

## Debug in a development environment {/* #debug-in-a-development-environment */}

In developing Workflows, you can use the normal development tools of logging and a debugger to see what’s happening in your Workflow.

In addition to the normal development tools of logging and a debugger, you can also see what’s happening in your Workflow by using the [Web UI](/web-ui) or [Temporal CLI](/cli).
The Web UI provides insight into your Workflows, making it easier to identify issues and monitor the state of your Workflows in real time.

## Debug in a production environment {/* #debug-in-a-production-environment */}

For production Workflows, debugging options include:

- [Web UI](/web-ui)
- [Temporal CLI](/cli)
- [Replay](/develop/ruby/best-practices/testing-suite#replay-test)
- [Tracing](/develop/ruby/platform/observability#tracing)
- [Logging](/develop/ruby/platform/observability#logging)

You can analyze Worker performance using:

- [Metrics](/develop/ruby/platform/observability#metrics)
- [Worker performance guide](/develop/worker-performance)

To monitor Server performance:

- Use [Cloud metrics](/cloud/metrics/) if you're on Temporal Cloud
- Or [self-hosted Server metrics](/self-hosted-guide/production-checklist#scaling-and-metrics) if running your own deployment

---

## Error handling - Ruby SDK

## Raise and Handle Exceptions {/* #exception-handling */}

In each Temporal SDK, error handling is implemented idiomatically, following the conventions of the language.
Temporal uses several different error classes internally — for example, [`CancelledError`](https://ruby.temporal.io/Temporalio/Error/CanceledError.html) in the Ruby SDK, to handle a Workflow cancellation.
You should not raise or otherwise implement these manually, as they are tied to Temporal platform logic.

The one Temporal error class that you will typically raise deliberately is [`ApplicationError`](https://ruby.temporal.io/Temporalio/Error/ApplicationError.html).
In fact, *any* other exceptions that are raised from your Ruby code in a Temporal Activity will be converted to an `ApplicationError` internally.
This way, an error's type, severity, and any additional details can be sent to the Temporal Service, indexed by the Web UI, and even serialized across language boundaries.

In other words, these two code samples do the same thing:

```ruby
class MyError < StandardError
end

class SomethingThatFails < Temporalio::Activity::Definition
  def execute(details)
    Temporalio::Activity::Context.current.logger.info(
      "We have a problem."
    )
    raise MyError.new('Simulated failure')
  end
end
```

```ruby
class SomethingThatFails < Temporalio::Activity::Definition
  def execute(details)
    Temporalio::Activity::Context.current.logger.info(
      "We have a problem."
    )
    raise Temporalio::Error::ApplicationError.new('Simulated failure', type: 'MyError')
  end
end
```

Depending on your implementation, you may decide to use either method.
One reason to use the Temporal `ApplicationError` class is because it allows you to set an additional `non_retryable` parameter.
This way, you can decide whether an error should not be retried automatically by Temporal.
This can be useful for deliberately failing a Workflow due to bad input data, rather than waiting for a timeout to elapse:

```ruby
class SomethingThatFails < Temporalio::Activity::Definition
  def execute(details)
    Temporalio::Activity::Context.current.logger.info(
      "We have a problem."
    )
    raise Temporalio::Error::ApplicationError.new('Simulated failure', non_retryable: true)
  end
end
```

You can alternately specify a list of errors that are non-retryable in your Activity [Retry Policy](/develop/ruby/activities/timeouts#activity-retries).

## Failing Workflows {/* #workflow-failure */}

One of the core design principles of Temporal is that an Activity Failure will never directly cause a Workflow Failure — a Workflow should never return as Failed unless deliberately.
The default retry policy associated with Temporal Activities is to retry them until reaching a certain timeout threshold.
Activities will not actually *return* a failure to your Workflow until this condition or another non-retryable condition is met.
At this point, you can decide how to handle an error returned by your Activity the way you would in any other program.
For example, you could implement a [Saga Pattern](https://github.com/temporalio/samples-ruby/tree/main/saga) that uses `rescue` blocks to "unwind" some of the steps your Workflow has performed up to the point of Activity Failure.

**You will only fail a Workflow by manually raising an `ApplicationError` from the Workflow code.**
You could do this in response to an Activity Failure, if the failure of that Activity means that your Workflow should not continue:

```ruby
class SagaWorkflow < Temporalio::Workflow::Definition
  def execute(details)
    Temporalio::Workflow.execute_activity(Activities::SomethingThatFails, details,start_to_close_timeout: 30)
  rescue StandardError
    raise Temporalio::Error::ApplicationError.new('Fail the Workflow')
```

This works differently in a Workflow than raising exceptions from Activities.
In an Activity, any Ruby exceptions or custom exceptions are converted to a Temporal `ApplicationError`.
In a Workflow, any exceptions that are raised other than an explicit Temporal `ApplicationError` will only fail that particular [Workflow Task](https://docs.temporal.io/tasks#workflow-task-execution) and be retried.
This includes any typical Ruby `RuntimeError`s that are raised automatically.
These errors are treated as bugs that can be corrected with a fixed deployment, rather than a reason for a Temporal Workflow Execution to return unexpectedly.

---

## Best Practices - Ruby SDK

![Ruby SDK Banner](/img/assets/banner-ruby-temporal.png)

## Best practices

- [Error handling](/develop/ruby/best-practices/error-handling)
- [Testing](/develop/ruby/best-practices/testing-suite)
- [Debugging](/develop/ruby/best-practices/debugging)
- [Converters and encryption](/develop/ruby/best-practices/converters-and-encryption)

---

## Testing - Ruby SDK

This page shows how to do the following:

- [Understand types of tests](#types-of-tests)
- [Use compatible test frameworks](#test-frameworks)
- [Test Workflows](#testing-workflows)
- [Test Activities](#test-activities)
- [Replay tests](#replay-test)

The Ruby test-suite feature guide describes the frameworks that facilitate Workflow and integration testing.

## Types of Tests {/* #types-of-tests */}

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

The Ruby SDK is compatible with any testing framework and does not have a specific recommendation.
Most Ruby SDK samples use [minitest](https://github.com/minitest/minitest).

## Testing Workflows {/* #testing-workflows */}

Workflow testing can be done in an integration-test fashion against a real server, however it is hard to simulate timeouts and other long time-based code.
Using the time-skipping Workflow test environment can help there.

### Testing Workflows with standard server

A non-time-skipping `Temporalio::Testing::WorkflowEnvironment` can be started via `start_local` which supports all standard Temporal features.
It is actually the real Temporal dev server packaged in the Temporal CLI, lazily downloaded on first use, and run as a sub-process in the background.
Assuming tests properly use separate Task Queues, the same server can and should be reused across tests.

Here's a simple example of a Workflow:

```ruby
class SimpleWorkflow < Temporalio::Workflow::Definition
  def execute(name)
    "Hello, #{name}!"
  end
end
```

Here's how a test of that Workflow may appear in minitest:

```ruby
def test_simple_workflow
  # Start local server that is stopped when block is done
  Temporalio::Testing::WorkflowEnvironment.start_local do |env|
    # Start worker that is stopped when block is done
    worker = Temporalio::Worker.new(
      env.client,
      task_queue: "tq-#{SecureRandom.uuid}",
      workflows: [SimpleWorkflow]
    )
    worker.run do
      # Execute workflow and check result
      result = env.client.execute_workflow(
        SimpleWorkflow, 'some-name',
        id: "wf-#{SecureRandom.uuid}", task_queue: worker.task_queue
      )
      assert_equal 'Hello, some-name!', result
    end
  end
end
```

While this is just a demonstration, a local server is often used as a fixture across many tests.
In minitest for instance, users often start the environment lazily (with no block), and shut it down inside a block passed to `Minitest.after_run`.

### Testing Workflows with time skipping

Sometimes there is a need to test Workflows that run a long time or to test that timeouts occur.
A time-skipping `Temporalio::Testing::WorkflowEnvironment` can be started via `start_time_skipping` which is a reimplementation of the Temporal server with special time skipping capabilities.
Like `start_local`, this also lazily downloads the process to run when first called.
Note, unlike `start_local`, this class is not thread safe nor safe for use with independent tests.
It can be technically be reused, but only for one test at a time because time skipping is locked/unlocked at the environment level.
Developers are encouraged to run it per test needed.

#### Automatic time skipping

Here's a simple example of a Workflow that waits a day:

```ruby
class WaitADayWorkflow < Temporalio::Workflow::Definition
  def execute
    Temporalio::Workflow.sleep(1 * 24 * 60 * 60)
    'all done'
  end
end
```

A regular integration test of this Workflow on a normal server would be way too slow.
However, the time-skipping server automatically skips to the next event when we wait on the result.
Here's a test for that Workflow in minitest:

```ruby
def test_wait_a_day_workflow
  # Start time-skipping test server that is stopped when block is done
  Temporalio::Testing::WorkflowEnvironment.start_time_skipping do |env|
    # Start worker that is stopped when block is done
    worker = Temporalio::Worker.new(
      env.client,
      task_queue: "tq-#{SecureRandom.uuid}",
      workflows: [WaitADayWorkflow]
    )
    worker.run do
      # Execute workflow and check result
      result = env.client.execute_workflow(
        WaitADayWorkflow,
        id: "wf-#{SecureRandom.uuid}", task_queue: worker.task_queue
      )
      assert_equal 'all done', result
    end
  end
end
```

This test will run almost instantly.
This is because by calling `execute_workflow` on our client, we are actually calling `start_workflow` + `result`, and `result` automatically skips time as much as it can (basically until the end of the workflow or until an activity is run).

To disable automatic time-skipping while waiting for a workflow result, run code in a block passed to `env.auto_time_skipping_disabled`.

#### Manual time skipping

Until a Workflow is waited on, all time skipping in the time-skipping environment is done manually via `WorkflowEnvironment#sleep`.

Here's a Workflow that waits for a Signal or times out:

```ruby
class SignalWorkflow < Temporalio::Workflow::Definition
  def execute
    # Wait for signal or timeout in 45 seconds
    Temporalio::Workflow.timeout(45 * 60) do
      Temporalio::Workflow.wait_condition { @signal_received }
    end
    'got signal'
  rescue Timeout::Error
    'got timeout'
  end

  workflow_signal
  def some_signal
    @signal_received = true
  end
end
```

To test a normal Signal in minitest, you might:

```ruby
def test_signal_workflow
  Temporalio::Testing::WorkflowEnvironment.start_time_skipping do |env|
    worker = Temporalio::Worker.new(
      env.client,
      task_queue: "tq-#{SecureRandom.uuid}",
      workflows: [SignalWorkflow]
    )
    worker.run do
      handle = env.client.start_workflow(
        SignalWorkflow,
        id: "wf-#{SecureRandom.uuid}", task_queue: worker.task_queue
      )
      handle.signal(SignalWorkflow.some_signal)
      assert_equal 'got signal', handle.result
    end
  end
end
```

But how would you test the timeout part? Like so:

```ruby
def test_signal_workflow_timeout
  Temporalio::Testing::WorkflowEnvironment.start_time_skipping do |env|
    worker = Temporalio::Worker.new(
      env.client,
      task_queue: "tq-#{SecureRandom.uuid}",
      workflows: [SignalWorkflow]
    )
    worker.run do
      handle = env.client.start_workflow(
        SignalWorkflow,
        id: "wf-#{SecureRandom.uuid}", task_queue: worker.task_queue
      )
      # Advance 50 seconds
      env.sleep(50)
      assert_equal 'got timeout', handle.result
    end
  end
end
```

### Mocking Activities

When testing Workflows, often you don't want to actually run the Activities.
Activities are just classes that extend `Temporalio::Activity::Definition`.
Simply write different/empty/fake/asserting ones and pass those to the Worker to have different activities called during the test.

## Testing Activities {/* #test-activities */}

Unit testing an Activity or any code that could run in an Activity is done via the `Temporalio::Testing::ActivityEnvironment` class.
Simply instantiate the class, and any code inside the block to `run` will be invoked inside the activity context.
Several things about the activity environment can be customized via parameters when constructing the environment including setting the info, providing a proc to call back on each heartbeat, setting the cancellation to be used, etc.

## Replay test {/* #replay-test */}

Given a Workflow's history, it can be replayed locally to check for things like non-determinism errors.
For example, assuming the `history_json` parameter below is given a JSON string of history exported from the CLI or web UI for workflow `MyWorkflow`, the following method will replay it:

```ruby
def replay_from_json(history_json)
  # Create a replayer
  replayer = Temporalio::Worker::WorkflowReplayer.new(workflows: [MyWorkflow])
  # Replay the history
  history = Temporalio::WorkflowHistory.from_history_json(history_json)
  replayer.replay_workflow(history)
end
```

If there is a non-determinism, this will raise an exception.

Event history can be loaded from more than just JSON.
It can be fetched individually from a Workflow handle, or even in a list.
For example, the following code will check that all Workflow histories for a certain Workflow type (i.e. workflow class) are safe with the current Workflow code.

```ruby
