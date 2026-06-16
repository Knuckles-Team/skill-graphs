# Sleep for 72 hours
Temporalio::Workflow.sleep(72 * 60 * 60, summary: 'my timer')
```

There is also a `Temporalio::Workflow.timeout` method that accepts a block and works like standard Ruby
`Timeout.timeout` if needing the ability to timeout a set of code.

---

## Versioning - Ruby SDK

Since Workflow Executions in Temporal can run for long periods — sometimes months or even years — it's common to need to make changes to a Workflow Definition, even while a particular Workflow Execution is in progress.

The Temporal Platform requires that Workflow code is [deterministic](/workflow-definition#deterministic-constraints). If you make a change to your Workflow code that would cause non-deterministic behavior on Replay, you'll need to use one of our Versioning methods to gracefully update your running Workflows. This only applies to Workflow orchestration logic. Non-deterministic work such as API calls, and database queries should be placed in Activities, which Temporal retries reliably.

With Versioning, you can modify your Workflow Definition so that new executions use the updated code, while existing ones continue running the original version.
There are two primary Versioning methods that you can use:

- [Worker Versioning](/production-deployment/worker-deployments/worker-versioning). The Worker Versioning feature allows you to tag your Workers and programmatically roll them out in versioned deployments, so that old Workers can run old code paths and new Workers can run new code paths.
- [Versioning with Patching](#ruby-sdk-patching-api). This method works by adding branches to your code tied to specific revisions. It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.

## Worker Versioning

Temporal's [Worker Versioning](/production-deployment/worker-deployments/worker-versioning) feature allows you to tag your Workers and programmatically roll them out in Deployment Versions, so that old Workers can run old code paths and new Workers can run new code paths. This way, you can pin your Workflows to specific revisions, avoiding the need for patching.

## Versioning with Patching {/* #ruby-sdk-patching-api */}

### Adding a patch

A Patch defines a logical branch in a Workflow for a specific change, similar to a feature flag.
It applies a code change to new Workflow Executions while avoiding disruptive changes to in-progress Workflow Executions.
When you want to make substantive code changes that may affect existing Workflow Executions, create a patch.

Suppose you have an initial Workflow that runs `PrePatchActivity`:

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  def execute
    result = Temporalio::Workflow.execute_activity(
      PrePatchActivity,
      start_to_close_timeout: 100
    )

    # ...
  end
end
```

Now, you want to update your code to run `PostPatchActivity` instead. This represents your desired end state.

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  def execute
    result = Temporalio::Workflow.execute_activity(
      PostPatchActivity,
      start_to_close_timeout: 100
    )

    # ...
  end
end
```

The problem is that you cannot deploy this new revision directly until you're certain there are no more running Workflows created using the `PrePatchActivity` code, otherwise you are likely to cause a nondeterminism error.
Instead, you'll need to use the [`patched`](https://ruby.temporal.io/Temporalio/Workflow.html#patched-class_method) function to check which version of the code should be executed.

Patching is a three-step process:

1. Patch in any new, updated code using the `patched()` function. Run the new patched code alongside old code.
2. Remove old code and use `deprecate_patch()` to mark a particular patch as deprecated.
3. Once there are no longer any open Workflow Executions of the previous version of the code, remove `deprecate_patch()`.
   Let's walk through this process in sequence.

### Patching in new code

Using `patched` inserts a marker into the Event History.
During Replay, if a Worker encounters a history with that marker, it will fail the Workflow task when the Workflow code doesn't produce the same patch marker (in this case `my-patch`).
This ensures you can safely deploy new code paths alongside the original branch.

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  def execute
    if Temporalio::Workflow.patched('my-patch')
      result = Temporalio::Workflow.execute_activity(
        PostPatchActivity,
        start_to_close_timeout: 100
      )
    else
      result = Temporalio::Workflow.execute_activity(
        PrePatchActivity,
        start_to_close_timeout: 100
      )
    end

    # ...
  end
end
```

### Deprecating patches {/* #deprecated-patches */}

After ensuring that all Workflows started with `v1` code have left retention, you can [deprecate the patch](https://ruby.temporal.io/Temporalio/Workflow.html#deprecate_patch-class_method).

Once your Workflows are no longer running the pre-patch code paths, you can deploy your code with `deprecate_patch()`.
These Workers will be running the most up-to-date version of the Workflow code, which no longer requires the patch.
The `deprecate_patch()` function works similarly to the `patched()` function by recording a marker in the Event history.
This marker does not fail replay when Workflow code does not emit it.
Deprecated patches serve as a bridge between the pre-patch code paths and the post-patch code paths, and are useful for avoiding errors resulting from patched code paths in your Event history.

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  def execute
    Temporalio::Workflow.deprecate_patch('my-patch')
    result = Temporalio::Workflow.execute_activity(
      PostPatchActivity,
      start_to_close_timeout: 100
    )

    # ...
  end
end
```

### Removing a patch {/* #deploy-new-code */}

Once the pre-patch Workflows have left retention, you can then safely deploy Workers that no longer use either the `patched()` or `deprecate_patch()` calls:

Patching allows you to make changes to currently running Workflows.
It is a powerful method for introducing compatible changes without introducing non-determinism errors.

### Workflow cutovers

To understand why Patching is useful, it's helpful to demonstrate cutting over an entire Workflow.

Since incompatible changes only affect open Workflow Executions of the same type, you can avoid determinism errors by creating a whole new Workflow when making changes.
To do this, you can copy the Workflow Definition function, giving it a different name, and register both names with your Workers.

For example, you would duplicate `MyWorkflow` as `MyWorkflowV2`:

```ruby
class MyWorkflow < Temporalio::Workflow::Definition
  def execute
    # ...
  end
end

class MyWorkflowV2 < Temporalio::Workflow::Definition
  def execute
    # ...
  end
end
```

You would then need to update the Worker configuration, and any other identifier strings, to register both Workflow Types:

```ruby
client = Temporalio::Client.connect('localhost:7233', 'default')

worker = Temporalio::Worker.new(
  client:,
  task_queue: 'my-task-queue',
  workflows: [MyWorkflow, MyWorkflowV2]
)
```

The downside of this method is that it requires you to duplicate code and to update any commands used to start the Workflow.
This can become impractical over time.
This method also does not provide a way to version any still-running Workflows -- it is essentially just a cutover, unlike Patching.

### Testing a Workflow for replay safety

To determine whether your Workflow your needs a patch, or that you've patched it successfully, you should incorporate [Replay Testing](/develop/ruby/best-practices/testing-suite#replay-test).

---

## Run a development server

## How to install the Temporal CLI and run a development server {/* #run-a-development-server */}

This page describes how to install the [Temporal CLI](/cli) and run a development Temporal Service. The local
development Temporal Service comes packaged with the [Temporal Web UI](/web-ui).

For information on deploying and running a self-hosted production Temporal Service, see the
[Self-hosted guide](/self-hosted-guide), or sign up for [Temporal Cloud](/cloud) and let us run your production Temporal
Service for you.

Temporal CLI is a tool for interacting with a Temporal Service from the command line and it includes a distribution of
the Temporal Server and Web UI. This local development Temporal Service runs as a single process with zero runtime
dependencies and it supports persistence to disk and in-memory mode through SQLite.

**Install the Temporal CLI**

The Temporal CLI is available on macOS, Windows, and Linux.

### macOS

**How to install the Temporal CLI on macOS**

Choose one of the following install methods to install the Temporal CLI on macOS:

**Install the Temporal CLI with Homebrew**

```bash
brew install temporal
```

**Install the Temporal CLI from CDN**

1. Select the platform and architecture needed.

- Download for Darwin amd64: https://temporal.download/cli/archive/latest?platform=darwin&arch=amd64
- Download for Darwin arm64: https://temporal.download/cli/archive/latest?platform=darwin&arch=arm64

2. Extract the downloaded archive.

3. Add the `temporal` binary to your PATH.

### Linux

**How to install the Temporal CLI on Linux**

Choose one of the following install methods to install the Temporal CLI on Linux:

**Install the Temporal CLI with Homebrew**

```bash
brew install temporal
```

**Install the Temporal CLI from CDN**

1. Select the platform and architecture needed.

- Download for Linux amd64: https://temporal.download/cli/archive/latest?platform=linux&arch=amd64
- Download for Linux arm64: https://temporal.download/cli/archive/latest?platform=linux&arch=arm64

2. Extract the downloaded archive.

3. Add the `temporal` binary to your PATH.

### Windows

**How to install the Temporal CLI on Windows**

Follow these instructions to install the Temporal CLI on Windows:

**Install the Temporal CLI from CDN**

1. Select the platform and architecture needed and download the binary.

- Download for Windows amd64: https://temporal.download/cli/archive/latest?platform=windows&arch=amd64
- Download for Windows arm64: https://temporal.download/cli/archive/latest?platform=windows&arch=arm64

2. Extract the downloaded archive.

3. Add the `temporal.exe` binary to your PATH.

### Start the Temporal Development Server

Start the Temporal Development Server by using the `server start-dev` command.

```bash
temporal server start-dev
```

This command automatically starts the Web UI, creates the default [Namespace](/namespaces), and uses an in-memory
database.

The Temporal Server should be available on `localhost:7233` and the Temporal Web UI should be accessible at
[`http://localhost:8233`](http://localhost:8233/).

The server's startup configuration can be customized using command line options. For a full list of options, run:

```bash
temporal server start-dev --help
```

---

## Activity basics - Rust SDK

## Develop a basic Activity {/* #develop-activities */}

One of the primary things that Workflows do is orchestrate the execution of Activities. An Activity is a normal function or method execution that's intended to execute a single, well-defined action (either short or long-running), such as querying a database, calling a third-party API, or transcoding a media file.

An Activity can interact with the world outside the Temporal Platform or use a Temporal Client to interact with a Temporal Service. For the Workflow to be able to execute the Activity, you need to define the [Activity Definition](/activity-definition).

The `#[activities]` macro marks an `impl` block as containing Activity definitions. Each method decorated with `#[activity]` becomes an Activity that can be invoked from a Workflow.

Here's an example of an Activity:

```rust
use temporalio_sdk::activities::{ActivityContext, ActivityError};
use temporalio_macros::activities;

pub struct GreetingActivities;

#[activities]
impl GreetingActivities {
    #[activity]
    pub async fn greet(_ctx: ActivityContext, name: String) -> Result<String, ActivityError> {
        Ok(format!("Hello, {}!", name))
    }

    #[activity]
    pub async fn send_notification(_ctx: ActivityContext, message: String) -> Result<(), ActivityError> {
        println!("Sending notification: {}", message);
        Ok(())
    }
}
```

### Define Activity parameters {/* #activity-parameters */}

There is a limit of 6 parameters that an [Activity Definition](/activity-definition) may support. There is also a limit to the total size of the data that ends up encoded into a gRPC message Payload.

A single argument is limited to a maximum size of 2 MB. And the total size of a gRPC message, which includes all the arguments, is limited to a maximum of 4 MB.

Also, keep in mind that all Payload data is recorded in the [Workflow Execution Event History](/workflow-execution/event#event-history) and large Event Histories can affect Worker performance.

We recommend that you use a single struct as an argument that wraps all the application data passed to Activities. This way you can change what data is passed to the Activity without breaking the function signature.

Each Activity method must:

- Be `async` (return a future)
- Take `ActivityContext` as the first parameter
- Return `Result<T, ActivityError>` where `T` is the return type
- Be `pub` (public)

The `ActivityContext` parameter provides access to Activity execution information and capabilities like heartbeating. If you don't need it, you can use `_ctx` as a parameter name.

Activities can also take `Arc<Self>` and be registered using an instance. Here's an example using `Arc`:

```rust
struct SleeperActivities {
    acts_started: Arc<Semaphore>,
    acts_done: Arc<Semaphore>,
}

#[activities]
impl SleeperActivities {
    #[activity]
    async fn sleeper(
        self: Arc<Self>,
        ctx: ActivityContext,
        _: String,
    ) -> Result<(), ActivityError> {
        self.acts_started.add_permits(1);
        // just wait to be cancelled
        ctx.cancelled().await;
        self.acts_done.add_permits(1);
        Err(ActivityError::cancelled())
    }
}
```

Activity parameters should be serializable and deserializable using serde. Use `#[derive(Serialize, Deserialize)]` on your data types:

```rust
use serde::{Serialize, Deserialize};
use temporalio_macros::activities;
use temporalio_sdk::activities::{ActivityContext, ActivityError};

#[derive(Serialize, Deserialize)]
pub struct GreetingInput {
    pub greeting: String,
    pub name: String,
}

pub struct GreetingActivities;

#[activities]
impl GreetingActivities {
    #[activity]
    pub async fn compose_greeting(
        _ctx: ActivityContext,
        input: GreetingInput,
    ) -> Result<String, ActivityError> {
        Ok(format!("{} {}!", input.greeting, input.name))
    }
}
```

### Define Activity return values {/* #activity-return-values */}

All data returned from an Activity must be serializable.

Activity return values are subject to payload size limits in Temporal. The default payload size limit is 2MB, and there is a hard limit of 4MB for any gRPC message size in the Event History transaction. Keep in mind that all return values are recorded in a [Workflow Execution Event History](/workflow-execution/event#event-history).

The return type of an Activity is `Result<T, ActivityError>`. The `T` type must implement `Serialize`. Use `ApplicationFailure::new` for errors that should be retried, and `ApplicationFailure::non_retryable` for permanent failures:

```rust
#[derive(serde::Serialize, serde::Deserialize, Debug, Clone, PartialEq, Eq, Hash)]
pub struct ProcessedData {
    pub processed: String,
}

#[activities]
impl MyActivities {
    #[activity]
    pub async fn process_data(
        _ctx: ActivityContext,
        input: String,
    ) -> Result<ProcessedData, ActivityError> {
        // If an error should be retried
        if !validate_input(&input) {
            return Err(ApplicationFailure::builder(anyhow::anyhow!("Invalid input format"))
                .next_retry_delay(Duration::from_secs(5))
                .build()
                .into());
        }

        // If an error should not be retried
        if input.len() > 1000000 {
            return Err(ApplicationFailure::non_retryable(
                anyhow::anyhow!("Input too large")
            ).into());
        }

        let result = ProcessedData {
            processed: input.to_uppercase(),
        };

        Ok(result)
    }
}
```

### Customize your Activity Type {/* #activity-type */}

Activities have a Type that refers to the Activity name. The Activity name is used to identify Activity Types in the Workflow Execution Event History, Visibility Queries, and Metrics.

By default, the Activity name is the method name. You can customize it by providing a `name` parameter to the `#[activity]` macro:

```rust
#[activities]
impl GreetingActivities {
    #[activity(name = "compose_greeting")]
    pub async fn greet(_ctx: ActivityContext, name: String) -> Result<String, ActivityError> {
        Ok(format!("Hello, {}!", name))
    }

    #[activity(name = "send_email")]
    pub async fn send_notification(_ctx: ActivityContext, message: String) -> Result<(), ActivityError> {
        println!("Sending notification: {}", message);
        Ok(())
    }
}
```

---

## Activity execution - Rust SDK

## Start an Activity Execution {/* #activity-execution */}

Calls to spawn [Activity Executions](/activity-execution) are written within a
[Workflow Definition](/workflow-definition). The call to spawn an Activity Execution generates the
[ScheduleActivityTask](/references/commands#scheduleactivitytask) Command. This results in a set of three [Activity Task](/tasks#activity-task) related Events in your Workflow Execution Event History:
[ActivityTaskScheduled](/references/events#activitytaskscheduled), [ActivityTaskStarted](/references/events#activitytaskstarted), and ActivityTaskClosed.

A single instance of the Activity implementation may be used across multiple concurrent Activity invocations. Activity implementation code should be *idempotent*.

Values passed to Activities as input parameters or returned as results are recorded in the Workflow Execution history. This history is replayed to Workflow Workers during recovery. Large payloads can negatively impact Workflow performance.

Be mindful of the size of data passed to and from Activities. Otherwise, there are no strict limitations on Activity implementations.

To spawn an Activity Execution, use the Workflow context’s Activity execution APIs within your Workflow code.

In Rust, Activities are typically executed using `ctx.start_activity(...)`, which returns a `Future` that can be awaited.

```rust
#[workflow_methods]
impl GreetingWorkflow {
    #[run]
    pub async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
        let name = ctx.state(|s| s.name.clone());
        // Execute an activity
        let greeting = ctx.start_activity(
            MyActivities::greet,
            name,
            ActivityOptions::start_to_close_timeout(Duration::from_secs(30)),
        ).await?;

        println!("{}", greeting);

        Ok(greeting)
    }
}
```

### Set the required Activity Timeouts {/* #required-timeout */}

Activity Execution semantics rely on several timeout parameters. You need to set at least one of these:

* [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout)
* [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout)

These are configured as part of the Activity options when scheduling the Activity. Available timeouts include:

- `start_to_close_timeout`
- `schedule_to_close_timeout`
- `with_start_to_close_timeout`
- `with_schedule_to_close_timeout`

```rust
#[workflow_methods]
impl GreetingWorkflow {
    #[init]
    fn new(_ctx: &WorkflowContextView, name: String) -> Self {
        Self { name }
    }

    #[run]
    pub async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
        let name = ctx.state(|s| s.name.clone());
        // Execute an activity
        let greeting = ctx.start_activity(
            MyActivities::greet,
            name,
            ActivityOptions::schedule_to_close_timeout(Duration::from_secs(30))
        ).await?;

        println!("{}", greeting);
        Ok(greeting)
    }
}
```

### Get the results of an Activity Execution {/* #get-activity-results */}

Spawning an [Activity Execution](/activity-execution) generates a [ScheduleActivityTask](/references/commands#scheduleactivitytask) Command and returns a `Future` to the Workflow.

Workflows can either:

* `await` the result immediately (blocking progress), or
* store the `Future` and await it later to allow concurrent execution.

In Rust, calling `.await` on the Activity invocation returns the result. If you need more control (e.g., parallel execution), you can create multiple Activity futures and await them selectively.

You must provide either `schedule_to_close_timeout` or `start_to_close_timeout`.

```rust
#[workflow_methods]
impl GreetingWorkflow {
    #[run]
    pub async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
        let name = ctx.state(|s| s.name.clone());
        // Execute an activity
        let greeting = ctx.start_activity(
            MyActivities::greet,
            name,
            ActivityOptions::start_to_close_timeout(Duration::from_secs(30))
        ).await?;

        println!("{}", greeting);
        Ok(greeting)
    }
}
```

For concurrent execution:

```rust
use temporalio_sdk::workflows::join;

#[run]
pub async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
    let name = ctx.state(|s| s.name.clone());
    // Execute an activity
    let greeting = ctx.start_activity(
        MyActivities::greet,
        name,
        ActivityOptions::start_to_close_timeout(Duration::from_secs(30))
    );

    let language = ctx.start_activity(
        MyActivities::call_greeting_service,
        ActivityLanguages::English,
        ActivityOptions::start_to_close_timeout(Duration::from_secs(30))
    );

    // Run in parallel
    let (greeting_res, language_res) = join!(greeting, language);
}
```

Use direct `.await` in most cases. More advanced patterns, like parallel execution or cancellation, can be built using Rust’s async primitives.

---

## Activities - Rust SDK

![Rust SDK Banner](/img/assets/banner-rust-temporal.png)

## Activities

- [Activity basics](/develop/rust/activities/basics)
- [Activity execution](/develop/rust/activities/execution)
- [Timeouts](/develop/rust/activities/timeouts)

---

## Activity Timeouts - Rust SDK

## Set Activity timeouts {/* #activity-timeouts */}

Each Activity timeout controls the maximum duration of a different aspect of an Activity Execution.

The following timeouts are available in Activity options:

- [Schedule-To-Close Timeout](/encyclopedia/detecting-activity-failures#schedule-to-close-timeout): the maximum amount of time allowed for the overall [Activity Execution](/activity-execution).
- [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout): the maximum time allowed for a single [Activity Task Execution](/tasks#activity-task-execution).
- [Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout): the maximum amount of time allowed from when an [Activity Task](/tasks#activity-task) is scheduled to when a [Worker](/workers#worker) starts that Activity Task.

An Activity Execution must have either the Start-To-Close Timeout or the Schedule-To-Close Timeout set. Temporal strongly recommends setting a Start-To-Close Timeout because the service relies on it to detect lost Activity Tasks and trigger retries when appropriate.

In Rust, these values are configured as part of the Activity options when scheduling an Activity from a Workflow. The Rust SDK is currently pre-release and its API is still evolving, so exact method names may change over time.

Available timeout fields include:

- `schedule_to_close_timeout`
- `schedule_to_start_timeout`
- `start_to_close_timeout`

```rust
let greeting = ctx.start_activity(
    MyActivities::greet,
    name,
    ActivityOptions::start_to_close_timeout(Duration::from_secs(30))
);
````

### Set an Activity Retry Policy {/* #activity-retries */}

A Retry Policy works together with timeouts to provide fine-grained control over Activity failure handling. Activities automatically use a default [Retry Policy](/encyclopedia/retry-policies) unless you provide a custom one.

In Rust, configure the Retry Policy as part of the Activity options when scheduling the Activity from Workflow code. Because the Rust SDK API is still evolving, treat the following as representative of the current style rather than a guaranteed stable surface.

```rust
let language = ctx.start_activity(
    MyActivities::call_greeting_service,
    ActivityLanguages::English,
    ActivityOptions::with_start_to_close_timeout(Duration::from_secs(30))
        .retry_policy(
            RetryPolicy {
                initial_interval: Some(prost_dur!(from_secs(10))),
                backoff_coefficient: 2.0,
                maximum_interval: Some(prost_dur!(from_secs(100))),
                maximum_attempts: 5,
                non_retryable_error_types: vec!["NonRetryableError".to_string()]
            }
        ).build()
    );
```

### Override the retry interval with `explicit_delay` {/* #next-retry-delay */}

To override the next retry interval set by the current policy, return a failure from an Activity with a custom next retry delay. That value replaces the interval the Retry Policy would otherwise use for the next retry attempt. This is useful when retry timing depends on runtime state such as the current attempt number.

For example, you can increase the delay linearly with each attempt instead of using the exponential backoff defined by a backoff coefficient:

```rust
use temporalio_macros::{activities};
use temporalio_sdk::activities::{ActivityContext, ActivityError};
use std::sync::{Arc, atomic::{AtomicUsize, Ordering}};

struct TestGreetActivities {
    counter: AtomicUsize,
}

#[activities]
impl TestGreetActivities {
    #[activity]
    pub async fn greet(_ctx: ActivityContext, name: String) -> Result<String, ActivityError> {
        if name == "ziggy" {
            return Err(ApplicationFailure::builder(anyhow::anyhow!("Ziggy is not a valid name"))
                // next retry will be after 5 seconds
                .next_retry_delay(std::time::Duration::from_secs(5))
                .build()
                .into());
        }
        Ok(format!("Hello, {}!", name))
    }
}
```

## Heartbeat an Activity {/* #activity-heartbeats */}

An [Activity Heartbeat](/encyclopedia/detecting-activity-failures#activity-heartbeat) is a signal from the [Worker Process](/workers#worker-process) executing the Activity to the [Temporal Service](/temporal-service). Each heartbeat tells the service that the [Activity Execution](/activity-execution) is still making progress and that the Worker has not crashed. If the service does not receive a heartbeat within the configured [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout), the Activity can time out and be retried according to its Retry Policy.

Heartbeats may be throttled by the Worker, so not every heartbeat call is necessarily sent immediately to the Temporal Service. Activity cancellation is also delivered through heartbeat processing, which means Activities that don't heartbeat cannot receive cancellation promptly. ([Temporal Docs][3])

Heartbeats can include `details` that describe current progress. If the Activity fails and is retried, the retried attempt can retrieve the details from the most recently recorded heartbeat. The Rust SDK exposes activity context support for heartbeat details.

To heartbeat an Activity in Rust, call the heartbeat API from inside the Activity with `record_heartbeat`:

```rust
pub async fn greet(ctx: ActivityContext, name: String) -> Result<String, ActivityError> {
    ctx.record_heartbeat(vec!["greet activity started".into()]);

    if name == "ziggy" {
        return Err(anyhow::anyhow!("Ziggy is not a valid name").into());
    }

    Ok(format!("Hello, {}!", name))
}
```

### Set a Heartbeat Timeout {/* #heartbeat-timeout */}

A [Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) works together with Activity heartbeats and sets the maximum time allowed between heartbeats. Configure it as part of the Activity options when scheduling the Activity.

```rust
let language = ctx.start_activity(
    MyActivities::call_greeting_service,
    ActivityLanguages::English,
    ActivityOptions::with_start_to_close_timeout(Duration::from_secs(30))
        .heartbeat_timeout(Duration::from_secs(5))
        .build()
    );
```

---

## Client - Rust SDK

![Rust SDK Banner](/img/assets/banner-rust-temporal.png)

## Temporal Client

- [Temporal Client](/develop/rust/client/temporal-client)

---

## Temporal Client - Rust SDK

A [Temporal Client](/encyclopedia/temporal-sdks#temporal-client) lets your application communicate with the Temporal Service. Use it to start Workflow Executions, send Signals, run Queries, fetch Workflow results, and more.

This page shows how to do the following using the Rust SDK and Temporal Client:

- [Connect to a local development Temporal Service](#connect-to-development-service)
- [Connect to Temporal Cloud](#connect-to-temporal-cloud)
- [Start a Workflow Execution](#start-workflow-execution)
- [Get Workflow results](#get-workflow-results)

A Temporal Client can't be created and used inside Workflow code. However, using a Temporal Client inside an Activity is acceptable when you need to communicate with the Temporal Service.

## Connect to development Temporal Service {/* #connect-to-development-service */}

In Rust, create a client by establishing a `Connection` and then constructing a `Client`.
You can provide connection options directly in code or load them from environment variables.

When you are running Temporal locally, the minimal setup is typically a local server address and the `default` Namespace.

<Tabs groupId="connect-options" defaultValue="config-file" >

<TabItem value="config-file" label="Configuration File">

You can use a TOML configuration file to set connection options for the Temporal Client.
The configuration file supports multiple profiles, each with its own connection options.

If you don't specify a configuration file path, the SDK looks in the default OS-specific location.
Environment variables take precedence over values from the configuration file.

For example, the following TOML file defines two profiles:

```toml title="temporal.toml"
