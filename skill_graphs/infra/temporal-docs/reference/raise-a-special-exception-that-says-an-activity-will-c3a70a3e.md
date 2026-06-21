# Raise a special exception that says an activity will be completed somewhere else
raise Temporalio::Activity::CompleteAsyncError
```

To update an Activity outside the Activity, use the [async_activity_handle](https://ruby.temporal.io/Temporalio/Client.html#async_activity_handle-instance_method) method on the client to get the handle of the Activity.

```ruby
handle = my_client.async_activity_handle(captured_token)
```

Then, on that handle, you can use `heartbeat`, `complete`, `fail`, or `report_cancellation` methods to update the Activity.

```ruby
handle.complete('completion value')
```

---

## Activity basics - Ruby SDK

## Develop an Activity {/* #develop-activity */}

One of the primary things that Workflows do is orchestrate the execution of Activities.
An Activity is a normal method execution that's intended to execute a single, well-defined action (either short or long-running), such as querying a database, calling a third-party API, or transcoding a media file.
An Activity can interact with world outside the Temporal Platform or use a Temporal Client to interact with a Temporal Service.
For the Workflow to be able to execute the Activity, we must define the [Activity Definition](/activity-definition).

You can develop an Activity Definition by creating a class that extends `Temporalio::Activity::Definition`.
To register a class as an Activity with a custom name, use the `activity_name` class method in the class definition.
Otherwise, the activity name is the unqualified class name.

```ruby
class MyActivity < Temporalio::Activity::Definition
  def execute(input)
    "#{input['greeting']}, #{input['name']}!"
  end
end
```

Activity implementation code should be _idempotent_. Learn more about [idempotency](/activity-definition#idempotency).

There is no explicit limit to the total number of parameters that an [Activity Definition](/activity-definition) may support.
However, there is a limit to the total size of the data that ends up encoded into a gRPC message Payload.

A single argument is limited to a maximum size of 2 MB.
And the total size of a gRPC message, which includes all the arguments, is limited to a maximum of 4 MB.

Some SDKs require that you pass context objects, others do not.
When it comes to your application data—that is, data that is serialized and encoded into a Payload—we recommend that you use a single hash or object as an argument that wraps the application data passed to Activities.
This is so that you can change what data is passed to the Activity without breaking a method signature.

The `execute` method in your Activity can technically accept multiple parameters of any data type that Temporal can convert.
However, Temporal strongly encourages using a single parameter object to simplify versioning and maintainability.

### Activity Concurrency and Executors {/* #activity-concurrency-and-executors */}

:::note

This section covers advanced concurrency and execution options that most users will not need when getting started.

:::

By default, activities run in the "thread pool executor" (i.e. `Temporalio::Worker::ActivityExecutor::ThreadPool`).
This default is shared across all workers and is a naive thread pool that continually makes threads as needed when none are
idle/available to handle incoming work.
If a thread sits idle long enough, it will be killed.

The maximum number of concurrent activities a worker will run at a time is configured via its `tuner` option.
The default is `Temporalio::Worker::Tuner.create_fixed` which defaults to 100 activities at a time for that worker.
When this value is reached, the worker will stop asking for work from the server until there are slots available again.

In addition to the thread pool executor, there is also a fiber executor in the default executor set.
To use fibers, call `activity_executor :fiber` class method at the top of the activity class (the default of this value is `:default` which is the thread pool executor).
Activities can only choose the fiber executor if the worker has been created and run in a fiber, but thread pool executor is always available.
Currently due to [an issue](https://github.com/temporalio/sdk-ruby/issues/162), workers can only run in a fiber on Ruby versions 3.3 and newer.

---

## Benign exceptions - Ruby SDK

**How to mark an Activity error as benign using the Temporal Ruby SDK**

When Activities throw errors that are expected or not severe, they can create noise in your logs, metrics, and OpenTelemetry traces, making it harder to identify real issues.
By marking these errors as benign, you can exclude them from your observability data while still handling them in your Workflow logic.

To mark an error as benign, set the `category` parameter to `Temporalio::Error::ApplicationError::Category::BENIGN` when raising an `ApplicationError`.

Benign errors:
- Have Activity failure logs downgraded to DEBUG level
- Do not emit Activity failure metrics
- Do not set the OpenTelemetry failure status to ERROR

```ruby
require 'temporalio/activity'

class MyActivity < Temporalio::Activity::Definition
  def execute
    begin
      call_external_service
    rescue StandardError => e
      # Mark this error as benign since it's expected
      raise Temporalio::Error::ApplicationError.new(
        e.message,
        category: Temporalio::Error::ApplicationError::Category::BENIGN
      )
    end
  end
end
```

Use benign exceptions for Activity errors that occur regularly as part of normal operations, such as polling an external service that isn't ready yet, or handling expected transient failures that will be retried.

---

## Dynamic Activities - Ruby SDK

## Set a Dynamic Activity {/* #set-a-dynamic-activity */}

A Dynamic Activity in Temporal is an Activity that is invoked dynamically at runtime if no other Activity with the same name is registered.
An Activity can be made dynamic by invoking `activity_dynamic` class method at the top of the definition.
You must register the Activity with the Worker before it can be invoked.
Only one Dynamic Activity can be present on a Worker.

Often, dynamic is used in conjunction with `activity_raw_args` which does not convert arguments but instead passes them
through as a splatted array of `Temporalio::Converters::RawValue` instances.

```ruby
class MyDynamicActivity < Temporalio::Activity::Definition
  # Make this the dynamic activity and accept raw args
  activity_dynamic
  activity_raw_args

  def execute(*raw_args)
    raise Temporalio::Error::ApplicationError, 'One arg expected' unless raw_args.size == 1

    # Use payload converter to convert it
    input = Temporalio::Activity::Context.current.payload_converter.from_payload(raw_args.first.payload)
    "#{input['greeting']}, #{input['name']}!"
  end
end
```

---

## Activity execution - Ruby SDK

## Start Activity Execution {/* #activity-execution */}

Calls to spawn [Activity Executions](/activity-execution) are written within a [Workflow Definition](/workflow-definition).
The call to spawn an Activity Execution generates the [ScheduleActivityTask](/references/commands#scheduleactivitytask) Command.
This results in the set of three [Activity Task](/tasks#activity-task) related Events ([ActivityTaskScheduled](/references/events#activitytaskscheduled), [ActivityTaskStarted](/references/events#activitytaskstarted), and `ActivityTask[Closed]`)in your Workflow Execution Event History.

The values passed to Activities through invocation parameters or returned through a result value are recorded in the Execution history.
The entire Execution history is transferred from the Temporal service to Workflow Workers when a Workflow state needs to recover.
A large Execution history can thus adversely impact the performance of your Workflow.

Therefore, be mindful of the amount of data you transfer through Activity invocation parameters or Return Values.
Otherwise, no additional limitations exist on Activity implementations.

To spawn an Activity Execution, use the `execute_activity` operation from within your Workflow Definition.

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  # Customize the name
  workflow_name :MyDifferentWorkflowName

  def execute(name)
    Temporalio::Workflow.execute_activity(
      MyActivity,
      { greeting: 'Hello', name: },
      start_to_close_timeout: 100
    )
  end
end
```

Activity Execution semantics rely on several parameters.
The only required value that needs to be set is either a [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout) or a [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout).
These values are set as keyword parameters.

The Activity result is the returned from the `execute_activity` call.

---

## Activities - Ruby SDK

![Ruby SDK Banner](/img/assets/banner-ruby-temporal.png)

## Activities

- [Activity basics](/develop/ruby/activities/basics)
- [Activity execution](/develop/ruby/activities/execution)
- [Standalone Activities](/develop/ruby/activities/standalone-activities)
- [Timeouts](/develop/ruby/activities/timeouts)
- [Asynchronous Activity completion](/develop/ruby/activities/asynchronous-activity)
- [Dynamic Activity](/develop/ruby/activities/dynamic-activity)
- [Benign exceptions](/develop/ruby/activities/benign-exceptions)

---

## Standalone Activities - Ruby SDK

<ReleaseNoteHeader featureName="standaloneActivity" />

Standalone Activities are Activities that run independently, without being orchestrated by a
Workflow. Instead of starting an Activity from within a Workflow Definition, you start a Standalone
Activity directly from a [`Temporalio::Client`](https://ruby.temporal.io/Temporalio/Client.html).

The way you write the Activity and register it with a Worker is identical to [Workflow
Activities](/develop/ruby/activities/basics). The only difference is that you execute a Standalone
Activity directly from your Temporal Client.

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

This documentation uses source code from the
[standalone_activity](https://github.com/temporalio/samples-ruby/blob/main/standalone_activity)
sample.

:::

## Get Started with Standalone Activities {/* #get-started */}

Prerequisites:

- **Ruby** 3.3+

- **Temporal Ruby SDK** (v1.5.0 or higher). See the [Ruby Quickstart](/develop/ruby/set-up-local-ruby) for
  install instructions.

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

```
temporal server start-dev
```

This command automatically starts the Temporal development server with the Web UI, and creates the `default` Namespace.
It uses an in-memory database, so do not use it for real use cases.

:::info Temporal Cloud

All code samples on this page use
[`Temporalio::EnvConfig::ClientConfig.load_client_connect_options`](https://ruby.temporal.io/Temporalio/EnvConfig/ClientConfig.html#load_client_connect_options-class_method)
to configure the Temporal Client connection. It responds to [environment
variables](/references/client-environment-configuration) and [TOML configuration
files](/references/client-environment-configuration), so the same code works against a local dev
server and Temporal Cloud without changes. See [Run Standalone Activities with Temporal
Cloud](#run-standalone-activities-temporal-cloud) below.

:::

The Temporal Server will now be available for client connections on `localhost:7233`, and the
Temporal Web UI will now be accessible at [http://localhost:8233](http://localhost:8233). Standalone
Activities are available from the nav bar item located towards the top left of the page:

Clone the [samples-ruby](https://github.com/temporalio/samples-ruby) repository to follow along:

```bash
git clone https://github.com/temporalio/samples-ruby.git
cd samples-ruby
bundle install
```

The sample consists of separate programs in the `standalone_activity` directory:

```
standalone_activity/
├── my_activities.rb      # Activity definition
├── worker.rb             # Worker that processes activity tasks
├── execute_activity.rb   # Starts an activity and waits for the result
├── start_activity.rb     # Starts an activity without blocking
├── list_activities.rb    # Lists activity executions
└── count_activities.rb   # Counts activity executions
```

## Define your Activity {/* #define-activity */}

An Activity in the Temporal Ruby SDK is a subclass of [`Temporalio::Activity::Definition`](https://ruby.temporal.io/Temporalio/Activity/Definition.html) that
implements an `execute` method. The way you define a Standalone Activity is identical to how you
define an Activity orchestrated by a Workflow. In fact, the same Activity can be executed both as a
Standalone Activity and as a Workflow Activity.

[my_activities.rb](https://github.com/temporalio/samples-ruby/blob/main/standalone_activity/my_activities.rb)

```ruby
require 'temporalio/activity'

module StandaloneActivity
  module MyActivities
    class ComposeGreeting < Temporalio::Activity::Definition
      def execute(greeting, name)
        "#{greeting}, #{name}!"
      end
    end
  end
end
```

## Run a Worker with the Activity registered {/* #run-worker */}

Running a Worker for Standalone Activities is the same as running a Worker for Workflow Activities —
you create a [`Temporalio::Worker`](https://ruby.temporal.io/Temporalio/Worker.html), register the Activity class, and call `worker.run`. The Worker
doesn't need to know whether the Activity will be invoked from a Workflow or as a Standalone
Activity. See [How to run a Worker](/develop/ruby/workers/run-worker-process) for more details on
Worker setup and configuration options.

[worker.rb](https://github.com/temporalio/samples-ruby/blob/main/standalone_activity/worker.rb)

```ruby
args, kwargs = Temporalio::EnvConfig::ClientConfig.load_client_connect_options
args[0] ||= 'localhost:7233'
args[1] ||= 'default'

client = Temporalio::Client.connect(*args, **kwargs)

worker = Temporalio::Worker.new(
  client:,
  task_queue: 'standalone-activity-sample',
  activities: [StandaloneActivity::MyActivities::ComposeGreeting]
)

puts 'Starting worker (ctrl+c to exit)'
worker.run(shutdown_signals: ['SIGINT'])
```

Open a new terminal, navigate to the `samples-ruby` directory, and run the Worker:

```bash
bundle exec ruby standalone_activity/worker.rb
```

Leave this terminal running — the Worker needs to stay up to process activities.

## Execute a Standalone Activity {/* #execute-activity */}

Use [`Temporalio::Client#execute_activity`](https://ruby.temporal.io/Temporalio/Client.html#execute_activity-instance_method) to execute a
Standalone Activity and block until it completes. Call this from your application code, not from
inside a Workflow Definition. This durably enqueues your Standalone Activity in the Temporal Server,
waits for it to be executed on your Worker, and then returns the result.

[execute_activity.rb](https://github.com/temporalio/samples-ruby/blob/main/standalone_activity/execute_activity.rb)

```ruby
result = client.execute_activity(
  StandaloneActivity::MyActivities::ComposeGreeting,
  'Hello', 'World',
  id: 'standalone-activity-id',
  task_queue: 'standalone-activity-sample',
  start_to_close_timeout: 10
)
puts "Activity result: #{result}"
```

The first argument is the Activity to run. It can be the [`Activity::Definition`](https://ruby.temporal.io/Temporalio/Activity/Definition.html) subclass, an
instance of one, or a string/symbol name. Positional arguments after it are passed to the Activity's
`execute` method. The call requires `id`, `task_queue`, and at least one of `start_to_close_timeout`
or `schedule_to_close_timeout`.

To run it:

1. Make sure the Temporal Server is running (from the [Get Started](#get-started) step above).
2. Make sure the Worker is running (from the [Run a Worker](#run-worker) step above).
3. Open a new terminal, navigate to the `samples-ruby` directory, and run:

```bash
bundle exec ruby standalone_activity/execute_activity.rb
```

Or use the Temporal CLI:

```bash
temporal activity execute \
  --type ComposeGreeting \
  --activity-id standalone-activity-id \
  --task-queue standalone-activity-sample \
  --start-to-close-timeout 10s \
  --input '"Hello"' \
  --input '"World"'
```

## Start a Standalone Activity without waiting for the result {/* #start-activity */}

Starting a Standalone Activity means sending a request to the Temporal Server to durably enqueue
your Activity job, without waiting for it to be executed by your Worker.

Use [`Temporalio::Client#start_activity`](https://ruby.temporal.io/Temporalio/Client.html#start_activity-instance_method) to start a
Standalone Activity and get a handle without waiting for the result:

[start_activity.rb](https://github.com/temporalio/samples-ruby/blob/main/standalone_activity/start_activity.rb)

```ruby
handle = client.start_activity(
  StandaloneActivity::MyActivities::ComposeGreeting,
  'Hello', 'World',
  id: 'standalone-activity-id',
  task_queue: 'standalone-activity-sample',
  start_to_close_timeout: 10
)
puts "Started Activity with id=#{handle.id} run_id=#{handle.run_id}"
