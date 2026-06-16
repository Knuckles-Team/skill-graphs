# Quickstart

Configure your local development environment to get started developing with Temporal using the Rust SDK.

<SetupSteps>
<SetupStep code={
  <>
    <CodeSnippet language="bash">
    rustc --version
    </CodeSnippet>
  </>
}>

## Install Rust

Make sure you have Rust installed on your system. You can download and install Rust from [rustup.rs](https://rustup.rs/).

After installation, verify it's working by checking the version. You'll also need Cargo, which is Rust's package manager and comes bundled with Rust.

</SetupStep>

<SetupStep code={
<>
<CodeSnippet language="bash">mkdir temporal-rust-project</CodeSnippet>
<CodeSnippet language="bash">cd temporal-rust-project</CodeSnippet>
<CodeSnippet language="bash">cargo init --name temporal-hello-world</CodeSnippet>
</>
}>

## Create a Project

Now that you have Rust and Cargo installed, create a new Rust project to manage your dependencies.

</SetupStep>

<SetupStep code={
<>
<CodeSnippet language="toml">
{`[package]
name = "temporal-hello-world"
version = "0.1.0"
edition = "2024"

[dependencies]
futures = "0.3.32"
futures-util = "0.3.32"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
temporalio-client = "0.4.0"
temporalio-common = "0.4.0"
temporalio-macros = "0.4.0"
temporalio-sdk = "0.4.0"
temporalio-sdk-core = "0.4.0"
tokio = { version = "1", features = ["full"] }
anyhow = "1"
`}
</CodeSnippet>

If you run into issues installing the dependencies, try:
<CodeSnippet language="bash">
brew install protobuf
</CodeSnippet>
</>
}>

## Add Temporal Rust SDK Dependencies

Now update your project's `Cargo.toml` file to match the example and run `cargo build`.

The core dependencies you'll need are:

- `temporalio-sdk` - The Rust SDK for Temporal
- `tokio` - Async runtime required by the SDK
- `serde` - For serialization/deserialization

Next, you'll configure a local Temporal Service for development.

</SetupStep>

<SetupStep code={
<>

<Tabs>
<TabItem value="macos" label="macOS" default>
<CodeSnippet language="bash">
brew install temporal
</CodeSnippet>
</TabItem>

<TabItem value="windows" label="Windows">
Download the Temporal CLI archive for your architecture:

Windows amd64
Windows arm64

Extract it and add <code>temporal.exe</code> to your PATH.
</TabItem>

<TabItem value="linux" label="Linux">
Download the Temporal CLI for your architecture:

Linux amd64
Linux arm64

Extract the archive and move the <code>temporal</code> binary into your PATH:
<CodeSnippet language="bash">
sudo mv temporal /usr/local/bin
</CodeSnippet>
</TabItem>
</Tabs>

</>
}>

## Install Temporal CLI and start the development server

The fastest way to get a development version of the Temporal Service running on your local machine is to use
[Temporal CLI](https://docs.temporal.io/cli).

Choose your operating system to install Temporal CLI:

</SetupStep>

<SetupStep code={
<>
After installing, open a new Terminal. Keep this running in the background:
<CodeSnippet language="bash">temporal server start-dev</CodeSnippet>

Change the Web UI port
The Temporal Web UI may be on a different port in some examples or tutorials. To change the port for the Web UI, use the <code>--ui-port</code> option when starting the server:
<CodeSnippet language="bash">
temporal server start-dev --ui-port 8080
</CodeSnippet>
The Temporal Web UI will now be available at http://localhost:8080.

</>
}>

## Start the development server

Once you've installed Temporal CLI and added it to your PATH, open a new Terminal window and run the following command.

This command starts a local Temporal Service. It starts the Web UI, creates the default Namespace, and uses an in-memory database.

The Temporal Service will be available on localhost:7233. The Temporal Web UI will be available at http://localhost:8233.

Leave the local Temporal Service running as you work through tutorials and other projects. You can stop the Temporal Service at any time by pressing CTRL+C.

</SetupStep>
</SetupSteps>

## Run Hello World: Test Your Installation

Now let's verify your setup is working by creating and running a complete Temporal application with both a Workflow and Activity.

This test will confirm that:

- The Temporal Rust SDK is properly installed
- Your local Temporal Service is running
- You can successfully create and execute Workflows and Activities
- The communication between components is functioning correctly

### 1. Define Your Activity

Create a `/src/activities.rs` file with the Activity definition:

```rust
use temporalio_macros::activities;
use temporalio_sdk::activities::{ActivityContext, ActivityError};

pub struct MyActivities;

#[activities]
impl MyActivities {
    #[activity]
    pub async fn greet(_ctx: ActivityContext, name: String) -> Result<String, ActivityError> {
        Ok(format!("Hello, {}!", name))
    }
}
```

### 2. Define Your Workflow

Create a `/src/workflows.rs` file with the Workflow definition:

```rust
use temporalio_macros::{workflow, workflow_methods};
use temporalio_sdk::{ActivityOptions, WorkflowContext, WorkflowContextView, WorkflowResult};
use std::time::Duration;

use crate::activities::MyActivities;

#[workflow]
pub struct GreetingWorkflow {
    name: String,
}

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
            ActivityOptions::start_to_close_timeout(Duration::from_secs(30)),
        ).await?;

        println!("{}", greeting);
        Ok(greeting)
    }
}
```

### 3. Create and Run a Worker

Update your `/src/main.rs` file with the following:

```rust
use temporalio_client::{Client, ClientOptions, Connection};
use temporalio_common::envconfig::LoadClientConfigProfileOptions;
use temporalio_sdk::{Worker, WorkerOptions};
use temporalio_sdk_core::{CoreRuntime, RuntimeOptions};

mod workflows;
mod activities;

use crate::workflows::GreetingWorkflow;
use crate::activities::MyActivities;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let runtime = CoreRuntime::new_assume_tokio(RuntimeOptions::builder().build()?)?;

    // Set up client connection options, loading from config if available
    let (connection_options, client_options) = ClientOptions::load_from_config(
        LoadClientConfigProfileOptions::default(),
    )?;

    let connection = Connection::connect(connection_options).await?;
    let client = Client::new(connection, client_options)?;

    let worker_options = WorkerOptions::new("my-task-queue")
        .register_activities(MyActivities)
        .register_workflow::<GreetingWorkflow>()
        .build();

    Worker::new(&runtime, client, worker_options)?.run().await?;

    Ok(())
}
```

Open a new terminal and run the Worker with:

```bash
cargo run
```

### 4. Start a Workflow

You can now start a Workflow execution using the client. In a new terminal, run the Workflow with:

```bash
temporal workflow start \
  --type GreetingWorkflow \
  --task-queue my-task-queue \
  --input '"Ziggy"'
```

## Next Steps

Now that you have the basics working, explore the following resources to build more sophisticated applications:

- [Develop a Workflow](/develop/rust/workflows/basics) - Learn how to write complex workflow logic
- [Develop an Activity](/develop/rust/activities/basics) - Understand activity patterns and best practices
- [Worker Processes](/develop/rust/workers/worker-process) - Configure and scale workers
- [Using the Temporal Client](/develop/rust/client/temporal-client) - Start workflows and interact with the Temporal Service

<CallToAction href="https://learn.temporal.io/courses/">
  Take a Temporal 101 course
  Learn Temporal concepts and build your first application with a guided course
</CallToAction>

---

## Workers - Rust SDK

![Rust SDK Banner](/img/assets/banner-rust-temporal.png)

## Workers

- [Worker processes](/develop/rust/workers/worker-process)

---

## Worker processes - Rust SDK

## Run a Worker Process {/* #run-a-dev-worker */}

The [Worker Process](/workers#worker-process) is where Workflow and Activity code executes. A Worker polls a specific [Task Queue](/task-queue), processes Tasks from that queue, and reports results back to the Temporal Service.

- Each [Worker Entity](/workers#worker-entity) in a Worker Process must register the exact Workflow Types and Activity Types it may execute.
- Each Worker Entity must associate with exactly one [Task Queue](/task-queue).
- Each Worker Entity polling the same Task Queue must be registered with the same Workflow Types and Activity Types.

A [Worker Entity](/workers#worker-entity) is the component within a Worker Process that listens on a specific Task Queue.

A Worker Entity may host a Workflow Worker, an Activity Worker, or both. In many applications, a single Worker Process is enough, though you can scale out by running multiple Workers polling the same Task Queue.

In Rust, create a `Worker`, configure it with your Task Queue, register your Workflows and Activities, and then run it.

```rust
use temporalio_client::{Client, ClientOptions, Connection, ConnectionOptions};
use temporalio_sdk::{Worker, WorkerOptions};
use temporalio_sdk_core::{CoreRuntime, RuntimeOptions, Url};

use crate::workflow_messaging::GreetingsWorkflow;
use crate::activities::MyActivities;

#[tokio::main]
pub async fn run() -> Result<(), Box<dyn std::error::Error>> {
    // Connect to local Temporal server
    let connection_options =
        ConnectionOptions::new(Url::from_str("http://localhost:7233")?).build();

    let runtime = CoreRuntime::new_assume_tokio(RuntimeOptions::builder().build()?)?;

    // Client setup
    let connection = Connection::connect(connection_options).await?;
    let client = Client::new(connection, ClientOptions::new("default").build())?;

    let worker_options = WorkerOptions::new("my-task-queue")
        .register_activities(MyActivities)
        .register_workflow::<GreetingsWorkflow>()
        .build();

    Worker::new(&runtime, client, worker_options)?.run().await?;

    Ok(())
}
```

### Register types {/* #register-types */}

All Workers polling the same Task Queue name must be registered to handle the exact same Workflow Types and Activity Types. If a Worker receives a Task for a type it does not know how to execute, that Task fails, but the Workflow Execution itself does not necessarily fail.

When you create a Worker in Rust, register the Workflow and Activity types it's allowed to execute in the `WorkerOptions`:

```rust
let worker_options = WorkerOptions::new("my-task-queue")
    .register_activities(MyActivities)
    .register_workflow::<GreetingsWorkflow>()
    .build();
```

---

## Workflow basics - Rust SDK

## How to develop a Workflow {/* #develop-workflows */}

Workflows are the fundamental unit of a Temporal Application and it all starts with the development of a [Workflow Definition](/workflow-definition).

In the Temporal Rust SDK programming model, a Workflow Definition is made of a Workflow struct and associated methods decorated with macros.

A Workflow is defined by:

1. A struct that holds the Workflow state
3. A `#[run]` method that contains the main Workflow logic
2. An optional `#[init]` method that initializes the Workflow
4. Optional `#[signal]`, `#[query]`, and `#[update]` methods for external interaction

```rust
use temporalio_macros::{workflow, workflow_methods};
use temporalio_sdk::{WorkflowResult, WorkflowContextView};

#[workflow]
pub struct GreetingWorkflow {
    name: String,
}

#[workflow_methods]
impl GreetingWorkflow {
    #[init]
    fn new(_ctx: &WorkflowContextView, name: String) -> Self {
        Self { name }
    }

    #[run]
    async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
        let name = ctx.state(|s| s.name.clone());
        Ok(format!("Hello, {}!", name))
    }
}
```

The `#[workflow]` macro marks the struct as a Workflow. The `#[workflow_methods]` macro is applied to the `impl` block containing the Workflow methods.

### Workflow struct {/* #workflow-struct */}

The Workflow struct holds the state of your Workflow Execution. This state is persisted and recovered during replays. All fields in a Workflow struct should be serializable.

### Workflow initialization {/* #init-method */}

The `#[init]` method is optional and is called when the Workflow first starts. It receives the initial Workflow input parameters and initializes the Workflow struct:

```rust
#[init]
fn new(_ctx: &WorkflowContextView, name: String, age: u32) -> Self {
    Self {
        name,
        age,
        started_at: Instant::now(),
    }
}
```

The `#[init]` method receives a `WorkflowContextView`, which provides read-only access to Workflow execution information.

### Run method {/* #run-method */}

The `#[run]` method is required and contains the main Workflow logic. It:

- Must be `async`
- Receives a mutable `WorkflowContext<Self>`
- Returns `WorkflowResult<T>` where T is the Workflow return type
- Executes exactly once per Workflow execution

```rust
#[run]
async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
    // Execute activities, timers, child workflows, etc.
    let result = ctx.start_activity(
        MyActivities::greet,
        name,
        ActivityOptions::start_to_close_timeout(Duration::from_secs(30))
    ).await?;

    Ok(result)
}
```

## Define Workflow parameters {/* #workflow-parameters */}

Temporal Workflows may have any number of custom parameters. However, we strongly recommend that structs are used as parameters, so that the object's individual fields may be altered without breaking the signature of the Workflow. All Workflow Definition parameters must be serializable.

A method annotated with `#[init]` can have any number of parameters. We recommend passing a single struct that contains all the input fields:

```rust
use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize)]
pub struct ProcessingInput {
    pub data: Vec<String>,
    pub timeout_seconds: u32,
}

#[workflow]
pub struct ProcessingWorkflow {
    data: Vec<String>,
    timeout_seconds: u32,
}

#[workflow_methods]
impl ProcessingWorkflow {
    #[init]
    fn new(_ctx: &WorkflowContextView, input: ProcessingInput) -> Self {
        Self {
            data: input.data,
            timeout_seconds: input.timeout_seconds,
        }
    }

    #[run]
    async fn run(_ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
        // Use the initialized state
        Ok("Processing complete".to_string())
    }
}
```

All Workflow input should be serializable by `serde`.

## Define Workflow return parameters {/* #workflow-return-values */}

Workflow return values must also be serializable. Returning results, returning errors, or throwing exceptions is fairly idiomatic in each language that is supported. However, Temporal APIs that must be used to get the result of a Workflow Execution will only ever receive one of either the result or the error.

The return type of a Workflow is `WorkflowResult<T>` where `T` implements `Serialize`. Success is represented by `Ok(value)` and failure by `Err(...)`:

```rust
#[run]
async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<ProcessingResult> {
    // Can return a complex result type
    let result = ProcessingResult {
        status: "completed".to_string(),
        records_processed: 100,
    };

    Ok(result)
}
```

## Customize your Workflow Type {/* #workflow-type */}

Workflows have a Type that is referred to as the Workflow name. By default, the Workflow type is the name of the Workflow struct. You can customize it by providing a `name` parameter to the `#[workflow]` macro:

```rust
#[workflow(name = "my-custom-workflow")]
pub struct GreetingWorkflow {
    name: String,
}
```

The Workflow Type defaults to the struct name if not specified. For example, this Workflow would have the type `GreetingWorkflow`:

```rust
#[workflow]
pub struct GreetingWorkflow {
    // ...
}
```

## Workflow logic requirements {/* #workflow-logic-requirements */}

Workflow logic is constrained by [deterministic execution requirements](/workflow-definition#deterministic-constraints). For non-deterministic operations like API calls, and database queries, use [Activities](/develop/rust/activities/basics).

Workflow code must be deterministic because the Temporal Server may replay your Workflow to reconstruct its state. This means:

### Don't use nondeterministic functions

- No direct system time access - use `ctx.workflow_time()` instead of `SystemTime::now()`
- No random number generation - use `ctx.random_seed()` instead
- No external I/O (network, filesystem, etc.) - perform these in Activities instead
- No UUID generation via random means - the SDK doesn't have a direct UUID function, but you can use Activities for non-deterministic operations
- Do not use `tokio` or `futures` concurrency primitives directly in Workflow code. Many of them, like `tokio::select!`, `tokio::spawn`, `futures::select!`, introduce non-deterministic behavior that will break Workflow replay.

Instead, use the deterministic wrappers provided in `temporalio_sdk::workflows`:
    - `select!` — deterministic select (polls in declaration order)
    - `join!` — deterministic join for a fixed number of futures
    - `join_all` — deterministic join for a dynamic collection of futures

### Use Workflow-safe primitives

The Rust SDK provides:

- `ctx.timer()` - Wait for a duration
- `ctx.wait_condition(closure)` - Wait until a condition is true
- `workflows::select!` - Deterministic select statement
- `ctx.start_activity()` - Execute Activities
- `ctx.start_local_activity()` - Execute local Activities
- `ctx.child_workflow()` - Execute child Workflows
- `ctx.cancelled()` - Check if Workflow is cancelled

```rust
use std::time::Duration;

#[run]
async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
    // Good - deterministic timer
    ctx.timer(TimerOptions {
        duration: Duration::from_secs(60),
        summary: Some("important timer".into())
    }).await;

    // Good - deterministic wait for condition
    ctx.wait_condition(|s| s.data.len() >= 3).await;

    // Bad - nondeterministic sleep
    // tokio::time::sleep(Duration::from_secs(10)).await;

    // Bad - nondeterministic time
    // SystemTime::now()

    Ok("Done".to_string())
}
```

## Access Workflow State {/* #workflow-state */}

Use `ctx.state()` for read-only access and `ctx.state_mut()` for mutable access to your Workflow state:

```rust
#[run]
async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
    // Read-only access
    let name = ctx.state(|s| s.name.clone());

    // Mutable access (for signal handlers or update handlers)
    // Available in sync methods

    Ok(name)
}
```

In synchronous [`Signal`](/develop/rust/workflows/message-passing#signals) and [`Update`](/develop/rust/workflows/message-passing#updates) handlers, you can mutate state directly via `&mut self`.

## Workflow return types {/* #return-types */}

The `#[run]` method must return `WorkflowResult<T>`. This is a type alias for `Result<T, WorkflowTermination>`.

For errors, use `WorkflowTermination::Failed` which can be constructed from other error types via `into()`:

```rust
#[run]
async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
    if some_validation_fails {
        return Err(anyhow::anyhow!("validation_failed: Input is invalid").into());
    }

    Ok("Success".to_string())
}
```

Workflow errors will cause the Workflow Execution to fail and the error details will be available to clients.

---

## Cancellation - Rust SDK

You can interrupt a Workflow Execution in one of the following ways:

- [Cancel](#cancellation): Canceling a Workflow provides a graceful way to stop Workflow Execution.
- [Terminate](#termination): Terminating a Workflow forcefully stops Workflow Execution.

Terminating a Workflow forcefully stops Workflow Execution. This action resembles killing a process.

- The system records a `WorkflowExecutionTerminated` event in the Event History.
- The termination forcefully and immediately stops the Workflow Execution.
- The Workflow code gets no chance to handle termination.
- A Workflow Task doesn't get scheduled.

In most cases, canceling is preferable because it allows the Workflow to finish gracefully. Terminate only if the
Workflow is stuck and cannot be canceled normally.

## Cancel a Workflow Execution {/* #cancellation */}

Canceling a Workflow provides a graceful way to stop Workflow Execution. This action resembles sending a `SIGTERM` to a
process.

- The system records a `WorkflowExecutionCancelRequested` event in the Event History.
- A Workflow Task gets scheduled to process the cancelation.
- The Workflow code can handle the cancelation and execute any cleanup logic.
- The system doesn't forcefully stop the Workflow.

To cancel a Workflow Execution in Rust, use the `cancel` method on the Workflow handler:

```rust
let handle = client.start_workflow(
    GreetingsWorkflow::run,
    (),
    WorkflowStartOptions::new("my-task-queue", "greetings-workflow-10").build()
).await?;

handle.cancel(WorkflowCancelOptions::builder().reason("No longer needed").build()).await?;
````

### Cancel an Activity from a Workflow {/* #cancel-activity */}

Canceling an Activity from within a Workflow requires that the Activity Execution sends Heartbeats and sets a Heartbeat
Timeout. If the Heartbeat is not invoked, the Activity cannot receive a cancellation request. When any non-immediate
Activity is executed, the Activity Execution should send Heartbeats and set a
[Heartbeat Timeout](/encyclopedia/detecting-activity-failures#heartbeat-timeout) to ensure that the server knows it is
still working.

When an Activity is canceled, an error is returned in the Activity at the next available opportunity. If cleanup logic
needs to be performed, it can be done when handling the cancellation error. However, for the Activity to appear canceled
the error must be propagated.

Example of a cancellable Activity in Rust:

```rust
#![allow(unreachable_pub)]
use temporalio_macros::{activities};
use temporalio_sdk::{
    activities::{ActivityContext, ActivityError},
};

pub struct CancellationActivities;

#[activities]
impl CancellationActivities {
    #[activity]
    pub async fn long_running_cancellable_activity(
        ctx: ActivityContext,
        _input: (),
    ) -> Result<String, ActivityError> {
        loop {
            if ctx.is_cancelled() {
                return Err(ActivityError::cancelled());
            }
            ctx.record_heartbeat(vec![]);
            tokio::time::sleep(std::time::Duration::from_millis(200)).await;
        }
    }

    #[activity]
    pub async fn cleanup(_ctx: ActivityContext, _input: ()) -> Result<String, ActivityError> {
        Ok("cleanup done".to_string())
    }
}
```

Canceling the Activity from a Workflow:

```rust
fn activity_opts() -> ActivityOptions {
    ActivityOptions::with_start_to_close_timeout(Duration::from_secs(300))
        .heartbeat_timeout(Duration::from_secs(5))
        .build()
}

#[workflow_methods]
impl CancellationWorkflow {
    #[run]
    pub async fn run(ctx: &mut WorkflowContext<Self>, _input: ()) -> WorkflowResult<String> {
        let mut activity_fut = ctx.start_activity(
            CancellationActivities::long_running_cancellable_activity,
            (),
            activity_opts(),
        );

        temporalio_sdk::workflows::select! {
            result = &mut activity_fut => {
                let value = result.map_err(|e| anyhow::anyhow!("{e}"))?;
                Ok(value)
            }
            reason = ctx.cancelled() => {
                activity_fut.cancel();

                let cleanup_result = ctx
                    .start_activity(
                        CancellationActivities::cleanup,
                        (),
                        ActivityOptions::start_to_close_timeout(Duration::from_secs(10)),
                    )
                    .await
                    .map_err(|e| anyhow::anyhow!("{e}"))?;

                Ok(format!("Cancelled (reason={reason}), {cleanup_result}"))
            }
        }
    }
}
```

## Terminate a Workflow Execution {/* #termination */}

Terminating a Workflow forcefully stops Workflow Execution. This action resembles killing a process.

- The system records a `WorkflowExecutionTerminated` event in the Event History.
- The termination forcefully and immediately stops the Workflow Execution.
- The Workflow code gets no chance to handle termination.
- A Workflow Task doesn't get scheduled.

To terminate a Workflow Execution in Rust, use the `terminate` method on the client.

```rust
let handle = client.start_workflow(
    GreetingsWorkflow::run,
    (),
    WorkflowStartOptions::new("my-task-queue", "greetings-workflow-10").build()
).await?;

handle.terminate(WorkflowTerminateOptions::builder()
    .reason("Emergency shutdown")
    .build()
).await?;

```

## Reset a Workflow Execution {/* #reset */}

Resetting a Workflow Execution terminates the current Workflow Execution and starts a new Workflow Execution from a
point you specify in its Event History. Use reset when a Workflow is blocked due to a non-deterministic error or other
issues that prevent it from completing.
