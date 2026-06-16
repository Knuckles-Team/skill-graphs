# Custom headers for production
[profile.prod.grpc_meta]
environment     = "production"
service-version = "v1.2.3"
````

Load the configuration and connect with the `prod` profile as follows:

```rust
use temporalio_client::{
    Client, ClientOptions, Connection
};
use temporalio_common::{envconfig::LoadClientConfigProfileOptions, telemetry::TelemetryOptions};
use temporalio_sdk::{Worker, WorkerOptions};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let runtime = CoreRuntime::new_assume_tokio(
        RuntimeOptions::builder()
            .telemetry_options(TelemetryOptions::builder().build())
            .build()?,
    )?;
    let (conn_opts, client_opts) =
        ClientOptions::load_from_config(LoadClientConfigProfileOptions {
            config_file_profile: "prod".to_string().into(),
            ..Default::default()
        })?;
    let connection = Connection::connect(conn_opts).await?;
    let client = Client::new(connection, client_opts)?;

    ...

    Ok(())
}
```

</TabItem>

<TabItem value="env-vars" label="Environment Variables">

You can also configure the Temporal Client with environment variables using `envconfig`. This is useful for local development, CI, and production deployments.

```rust
use temporalio_client::{
    Client, ClientOptions, Connection
};
use temporalio_common::{envconfig::LoadClientConfigProfileOptions, telemetry::TelemetryOptions};
use temporalio_sdk::{Worker, WorkerOptions};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let runtime = CoreRuntime::new_assume_tokio(
        RuntimeOptions::builder()
            .telemetry_options(TelemetryOptions::builder().build())
            .build()?,
    )?;
    let (conn_opts, client_opts) =
        ClientOptions::load_from_config(LoadClientConfigProfileOptions::default())?;
    let connection = Connection::connect(conn_opts).await?;
    let client = Client::new(connection, client_opts)?;

    let worker_options = WorkerOptions::new("hello-world")
        .register_workflow::<HelloWorldWorkflow>()
        .register_activities(GreetingActivities)
        .build();

    let mut worker = Worker::new(&runtime, client, worker_options)?;
    println!("Worker started on task queue: hello-world");
    worker.run().await?;

    Ok(())
}
```

</TabItem>

<TabItem value="code" label="Code">

You can also specify connection options directly in code. This is convenient for local development and testing.

```rust
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let runtime = CoreRuntime::new_assume_tokio(
        RuntimeOptions::builder()
            .telemetry_options(TelemetryOptions::builder().build())
            .build()?,
    )?;
    let (conn_opts, client_opts) =
        ClientOptions::load_from_config(LoadClientConfigProfileOptions::default())?;
    let connection = Connection::connect(conn_opts).await?;
    let client = Client::new(connection, client_opts)?;

    let wf_handle = client.start_workflow(
        GreetingsWorkflow::run,
        (),
        WorkflowStartOptions::new(
            "my-task-queue",
            "greetings-workflow-10",
        ).build()
    ).await?;
}
```

</TabItem>

</Tabs>

## Connect to Temporal Cloud {/* #connect-to-temporal-cloud */}

You can connect to Temporal Cloud using either an API key or mTLS. Connection to Temporal Cloud or any secured Temporal Service requires additional connection options compared to connecting to an unsecured local development instance:

- Your authentication credentials:
    - For API key authentication, provide the API key.
    - If you are using mTLS, provide the mTLS CA certificate and mTLS private key.
- Your _Namespace_ and _Account ID_ combination in the format `<namespace_id>.<account_id>`
- The recommended gRPC endpoint for your Namespace, such as `<namespace>.<account>.tmprl.cloud:7233`

For more information about managing and generating client certificates for Temporal Cloud, see [How to manage certificates in Temporal Cloud](/cloud/certificates).

You can provide these connection options using environment variables, a configuration file, or directly in code.

<Tabs groupId="connect-api-key-options" defaultValue="config-file" >

<TabItem value="config-file" label="Configuration File">

You can define a Temporal Cloud profile in `temporal.toml`:

```toml
[profile.api]
address = "your-namespace.a1b2c.tmprl.cloud:7233"
namespace = "your-namespace"
api_key = "your-api-key-here"
```

If you want to use mTLS instead of an API key:

```toml
[profile.mtls]
address = "your-namespace.a1b2c.tmprl.cloud:7233"
namespace = "your-namespace"
tls_client_cert_data = "your-tls-client-cert-data"
tls_client_key_path = "your-tls-client-key-path"
```

Then load the profile and connect:

```rust
use temporalio_client::{
    Client, ClientOptions, Connection,
    envconfig::LoadClientConfigProfileOptions,
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let (conn_opts, client_opts) =
        ClientOptions::load_from_config(LoadClientConfigProfileOptions {
            config_file_profile: "api".to_string().into(),
            ..Default::default()
        })?;

    let runtime = CoreRuntime::new_assume_tokio(RuntimeOptions::builder().build()?)?;

    // Client setup
    let connection = Connection::connect(conn_opts).await?;
    let client = Client::new(connection, client_opts)?;

    println!("Connected to Temporal Cloud!");
    Ok(())
}
```

</TabItem>

<TabItem value="env-vars" label="Environment Variables">

The following environment variables are commonly used to connect to Temporal Cloud:

* `TEMPORAL_NAMESPACE`
* `TEMPORAL_ADDRESS`
* `TEMPORAL_API_KEY`
* `TEMPORAL_TLS_CLIENT_CERT_DATA` or `TEMPORAL_TLS_CLIENT_CERT_PATH`
* `TEMPORAL_TLS_CLIENT_KEY_DATA` or `TEMPORAL_TLS_CLIENT_KEY_PATH`

After setting the environment variables, load the configuration and connect:

```rust
use temporalio_client::{
    Client, ClientOptions, Connection
};
use temporalio_common::{envconfig::LoadClientConfigProfileOptions, telemetry::TelemetryOptions};
use temporalio_sdk::{Worker, WorkerOptions};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let runtime = CoreRuntime::new_assume_tokio(
        RuntimeOptions::builder()
            .telemetry_options(TelemetryOptions::builder().build())
            .build()?,
    )?;
    let (conn_opts, client_opts) =
        ClientOptions::load_from_config(LoadClientConfigProfileOptions::default())?;
    let connection = Connection::connect(conn_opts).await?;
    let client = Client::new(connection, client_opts)?;

    let worker_options = WorkerOptions::new("hello-world")
        .register_workflow::<HelloWorldWorkflow>()
        .register_activities(GreetingActivities)
        .build();

    let mut worker = Worker::new(&runtime, client, worker_options)?;
    println!("Worker started on task queue: hello-world");
    worker.run().await?;

    Ok(())
}
```

</TabItem>

<TabItem value="code" label="Code">

You can also specify connection options directly in code for Temporal Cloud.

```rust
use std::str::FromStr;
use temporalio_client::{Client, ClientOptions, Connection, ConnectionOptions, TlsOptions};
use temporalio_sdk_core::Url;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Connect to local Temporal server
    let connection_options =
        ConnectionOptions::new(Url::from_str("http://localhost:7233")?)
        .api_key("your_api_key")
        // If your Temporal server is configured to use TLS, you can set the TLS options here. For example, you can specify the path to the CA certificate, client certificate, and client key.
        // .tls_options(TlsOptions {
        //     ..Default::default()
        // })
        .build();

    let runtime = CoreRuntime::new_assume_tokio(RuntimeOptions::builder().build()?)?;

    // Client setup
    let connection = Connection::connect(connection_options).await?;
    let client = Client::new(connection, ClientOptions::new("default").build())?;

    println!("Connected to Temporal Cloud!");
    Ok(())
}
```

</TabItem>

</Tabs>

## Start a Workflow Execution {/* #start-workflow-execution */}

To start a Workflow Execution, supply:

- the Workflow Type
- the Workflow input
- a [Task Queue](/task-queue) that a Worker is polling
- a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id)

Starting a Workflow Execution creates the first [WorkflowExecutionStarted](/references/events#workflowexecutionstarted) Event in the Event History, followed by the first [WorkflowTaskScheduled](/references/events#workflowtaskscheduled) Event.

In Rust, use `start_workflow()` to start a Workflow and return a handle.

```rust
let handle = client.start_workflow(
    GreetingsWorkflow::run,
    (),
    WorkflowStartOptions::new(
        "my-task-queue",
        "greetings-workflow-10",
    ).build()
).await?;
```

### Set a Workflow's Task Queue {/* #set-task-queue */}

In most cases, the Task Queue is a required Workflow option.

For a Workflow to make progress, at least one Worker must be polling the same Task Queue.

In Rust, set the Task Queue in `WorkflowStartOptions`:

```rust
let handle = client
    .start_workflow(
        GreetingsWorkflow::run,
        (),
        WorkflowStartOptions::new(
            "your-task-queue",
            "your-workflow-id"
        ).build(),
    ).await?;
```

### Set a Workflow Id {/* #workflow-id */}

You must set a [Workflow Id](/workflow-execution/workflowid-runid#workflow-id).

A Workflow Id should usually map to a business process or business entity identifier, such as an order ID or customer ID.

In Rust, set the Workflow Id in `WorkflowStartOptions`:

```rust
let handle = client
    .start_workflow(
        GreetingsWorkflow::run,
        (),
        WorkflowStartOptions::new(
            "your-task-queue",
            "your-workflow-id"
        ).build(),
    ).await?;
```

## Get the results of a Workflow Execution {/* #get-workflow-results */}

If starting a Workflow succeeds, you get a Workflow handle.
You can use that handle to wait for the result, describe the Workflow, or interact with it through Signals, Queries, and Updates.

To get the result of a newly started Workflow:

```rust
let handle = client
    .start_workflow(
        GreetingsWorkflow::run,
        (),
        WorkflowStartOptions::new(
            "your-task-queue",
            "your-workflow-id"
        ).build(),
    ).await?;

let result = handle.get_result(WorkflowGetResultOptions::default()).await;

println!("Result: {:?}", result);
```

---

## Rust SDK developer guide

![Rust SDK Banner](/img/assets/banner-rust-temporal.png)

## Install and get started

You can find detailed installation instructions for the Rust SDK in the [Quickstart](/develop/rust/quickstart).

Once your local Temporal Service is set up, continue building with the following resources:

- [Develop a Workflow](/develop/rust/workflows/basics)
- [Develop an Activity](/develop/rust/activities/basics)
- [Start an Activity execution](/develop/rust/activities/execution)
- [Run Worker processes](/develop/rust/workers/worker-process)

## [Workflows](/develop/rust/workflows)

- [Workflow basics](/develop/rust/workflows/basics)
- [Child Workflows](/develop/rust/workflows/child-workflows)
- [Continue-As-New](/develop/rust/workflows/continue-as-new)
- [Message passing](/develop/rust/workflows/message-passing)
- [Cancellation](/develop/rust/workflows/cancellation)
- [Timers](/develop/rust/workflows/timers)
- [Timeouts](/develop/rust/workflows/timeouts)

## [Activities](/develop/rust/activities)

- [Activity basics](/develop/rust/activities/basics)
- [Activity execution](/develop/rust/activities/execution)
- [Timeouts](/develop/rust/activities/timeouts)

## [Workers](/develop/rust/workers)

- [Worker processes](/develop/rust/workers/worker-process)

## [Temporal Client](/develop/rust/client)

- [Temporal Client](/develop/rust/client/temporal-client)

## [Temporal Nexus](/develop/rust/nexus)

- [Feature guide](/develop/rust/nexus/feature-guide)

## Temporal Rust Technical Resources

- [Rust SDK Quickstart - Setup Guide](/develop/rust/quickstart)
- [Rust API Documentation](https://docs.rs/temporalio-sdk/latest/temporalio_sdk/)
- [Rust SDK GitHub](https://github.com/temporalio/sdk-core/tree/master/crates/sdk)

### Get Connected with the Temporal Rust Community

- [Temporal Rust Community Slack](https://temporalio.slack.com/archives/C08G723SFNZ/p1773935454727179)

---

## Nexus feature guide - Rust SDK

[Nexus](/nexus) is a tool for coordinating asynchronous operations between Temporal and external systems. Service handlers allow Workflows to receive inbound requests through Nexus.

## Call a Nexus Operation from a Workflow {/* #call-nexus-operation */}

You can start a Nexus operation from a Workflow using `ctx.start_nexus_operation()`:

```rust
use std::time::Duration;

use temporalio_common::protos::{coresdk::nexus, temporal::api::{common::v1::Payload,}};
use temporalio_macros::{workflow, workflow_methods};
use temporalio_sdk::{NexusOperationOptions, WorkflowContext, WorkflowContextView, WorkflowResult};

#[workflow]
pub struct GreetingWorkflow {
    pub name: String,
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

        let nexus_started = ctx.start_nexus_operation(NexusOperationOptions {
            endpoint: "my-endpoint".to_string(),
            service: "my-service".to_string(),
            operation: "my-operation".to_string(),
            input: Some(Payload {
                data: name.as_bytes().to_vec(),
                ..Default::default()
            }),
            start_to_close_timeout: Some(Duration::from_secs(10)),
            ..Default::default()
        }).await;

        let nexus_result = nexus_started.unwrap();

        println!("Nexus result: {:?}", nexus_result);

        Ok(format!("nexus result: {:?}", nexus_result))
    }
}
```

### Nexus Operation Arguments

- `endpoint` - The Nexus endpoint name
- `service` - The service name
- `operation` - The operation name
- `input` - The input payload (optional)
- `start_to_close_timeout` - How long the operation can run

---

## Nexus - Rust SDK

![Rust SDK Banner](/img/assets/banner-rust-temporal.png)

## Temporal Nexus

- [Feature guide](/develop/rust/nexus/feature-guide)

---

## Quickstart - Rust SDK
