
When you reset a Workflow, the Event History up to the reset point is copied to the new Workflow Execution, and the
Workflow resumes from that point with the current code. Reset only works if you've fixed the underlying issue, such as
removing non-deterministic code. Any progress made after the reset point will be discarded. Provide a reason when
resetting, as it will be recorded in the Event History.

<Tabs>

<TabItem value="web-ui" label="Web UI">

1. Navigate to the Workflow Execution details page,
2. Click the **Reset** button in the top right dropdown menu,
3. Select the Event ID to reset to,
4. Provide a reason for the reset,
5. Confirm the reset.

The Web UI shows available reset points and creates a link to the new Workflow Execution after the reset completes.

</TabItem>

<TabItem value="cli" label="Temporal CLI">

Use the `temporal workflow reset` command to reset a Workflow Execution:

```bash
temporal workflow reset \
    --workflow-id <workflow-id> \
    --event-id <event-id> \
    --reason "Reason for reset"
```

For example:

```bash
temporal workflow reset \
    --workflow-id my-background-check \
    --event-id 4 \
    --reason "Fixed non-deterministic code"
```

By default, the command resets the latest Workflow Execution in the `default` Namespace. Use `--run-id` to reset a
specific run. Use `--namespace` to specify a different Namespace:

```bash
temporal workflow reset \
    --workflow-id my-background-check \
    --event-id 4 \
    --reason "Fixed non-deterministic code" \
    --namespace my-namespace \
    --tls-cert-path /path/to/cert.pem \
    --tls-key-path /path/to/key.pem
```

Monitor the new Workflow Execution after resetting to ensure it completes successfully.

</TabItem>

</Tabs>

---

## Child Workflows - Rust SDK

This page shows how to do the following:

- [Start a Child Workflow execution](#start-child-workflow)
- [Set a Parent Close Policy](#parent-close-policy)

## Start a Child Workflow execution {/* #start-child-workflow */}

A [Child Workflow Execution](/child-workflows) is a Workflow Execution that is scheduled from within another Workflow using a Child Workflow API.

When using a Child Workflow API, Child Workflow related Events ([StartChildWorkflowExecutionInitiated](/references/events#startchildworkflowexecutioninitiated), [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted), [ChildWorkflowExecutionCompleted](/references/events#childworkflowexecutioncompleted), etc...) are logged in the Workflow Execution Event History.

The [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted) Event must be logged to the Event History before the Parent Workflow completes to ensure the Child Workflow has started.
In Rust, awaiting `ctx.child_workflow()` internally waits for this Event before returning, so the Child Workflow is guaranteed to have started once the call resolves.

To start a Child Workflow in Rust, use `ctx.child_workflow()`:

```rust
use temporalio_common::protos::temporal::api::common::v1::Payload;
use temporalio_macros::{workflow, workflow_methods};
use temporalio_sdk::{ChildWorkflowOptions, WorkflowContext, WorkflowContextView, WorkflowResult};

// child workflow
#[workflow]
pub struct ComposeGreetingWorkflow {
    pub name: String,
}

#[workflow_methods]
impl ComposeGreetingWorkflow {
    #[init]
    fn new(_ctx: &WorkflowContextView, name: String) -> Self {
        Self { name }
    }

    #[run]
    pub async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
        let name = ctx.state(|s| s.name.clone());
        Ok(format!("Hello from child: {}", name))
    }
}

// parent workflow
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

        let input = vec![
            Payload {
                data: name.as_bytes().to_vec(),
                ..Default::default()
            }
        ];
        let started = ctx.child_workflow(
            ComposeGreetingWorkflow::run,
            name.clone(),
            ChildWorkflowOptions {
                workflow_id: format!("greeting-child-en"),
                ..Default::default()
            },
        ).await?;

        let result = started.result().await;

        Ok(format!("ComposeGreetingWorkflow result: {:?}", result))
    }
}
```

### Specify Child Workflow options

Use [`ChildWorkflowOptions`](https://docs.rs/temporalio-sdk/0.2.0/temporalio_sdk/struct.ChildWorkflowOptions.html) to customize Child Workflow behavior.

### Execute multiple Child Workflows in parallel

You can start multiple Child Workflows and wait for all of them:

```rust
pub async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<Vec<Option<String>>> {
    let name = ctx.state(|s| s.name.clone());

    let en_greeting_child = ctx.child_workflow(
        ComposeEnGreetingWorkflow::run,
        name.clone(),
        ChildWorkflowOptions {
            workflow_id: format!("greeting-child-en"),
            ..Default::default()
        },
    ).await?;

    let es_greeting_child = ctx.child_workflow(
        ComposeEsGreetingWorkflow::run,
        name.clone(),
        ChildWorkflowOptions {
            workflow_id: format!("greeting-child-es"),
            ..Default::default()
        },
    ).await?;

    let en_result = en_greeting_child.result().await;
    let es_result = es_greeting_child.result().await;

    let combined = vec![en_result, es_result];

    print!("Combined greetings: {:?}", combined);

    ...
}
```

Both child Workflows run in parallel and the parent waits for both to complete.

## Parent Close Policy {/* #parent-close-policy */}

A [Parent Close Policy](/parent-close-policy) determines what happens to a Child Workflow Execution if its Parent changes to a Closed status (Completed, Failed, or Timed Out).

The default Parent Close Policy is set to terminate the Child Workflow Execution.

Set Parent Close Policy using the [`parent_close_policy`](https://docs.rs/temporalio-common/0.2.0/temporalio_common/protos/temporal/api/enums/v1/enum.ParentClosePolicy.html) field in `ChildWorkflowOptions`:

```rust
use temporalio_common::protos::temporal::api::{enums::v1::ParentClosePolicy};

let es_greeting_child = ctx.child_workflow(
    ComposeEsGreetingWorkflow::run,
    name.clone(),
    ChildWorkflowOptions {
        workflow_id: format!("greeting-child-es"),
        parent_close_policy: ParentClosePolicy::Abandon,
        ..Default::default()
    },
).await?;
```

### Parent Close Policy Options

- `Terminate` (default) - The Child Workflow will be terminated immediately when the parent closes
- `Abandon` - The Child Workflow will continue running even if the parent closes
- `RequestCancel` - The Child Workflow will receive a cancellation request when the parent closes

---

## Continue-As-New - Rust SDK

This page answers the following questions for Rust developers:

- [What is Continue-As-New?](#what)
- [How to Continue-As-New?](#how)
- [When is it right to Continue-as-New?](#when)

## What is Continue-As-New? {/* #what */}

[Continue-As-New](/workflow-execution/continue-as-new) lets a Workflow execution close successfully and creates a new Workflow execution. You can think of it as a checkpoint when your Workflow gets too long or approaches certain scaling limits.

The new Workflow execution is in the same [chain](/workflow-execution#workflow-execution-chain); it keeps the same Workflow Id but gets a new Run Id and a fresh Event History.
It also receives your Workflow's usual parameters.

## How to Continue-As-New using the Rust SDK {/* #how */}

First, design your Workflow parameters so that you can pass in the "current state" when you Continue-As-New into the next Workflow run.
This state is typically passed as a parameter or stored in the Workflow struct.

Inside your Workflow, return a `WorkflowTermination::ContinueAsNew` error to continue as new:

```rust
use temporalio_common::protos::coresdk::workflow_commands::ContinueAsNewWorkflowExecution;
use temporalio_macros::{workflow, workflow_methods};
use temporalio_sdk::{ActivityOptions, WorkflowContext, WorkflowContextView, WorkflowResult, WorkflowTermination};
use std::time::Duration;

use crate::activities::MyActivities;

#[workflow(name = "greeting-workflow-1")]
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
        // Execute an activity
        let greeting = ctx.start_activity(
            MyActivities::greet,
            name,
            ActivityOptions::start_to_close_timeout(Duration::from_secs(30))
        ).await?;

        println!("{}", greeting);

        if greeting.contains("Ziggy") {
            Ok(greeting)
        } else {
            let new_input = "New Name".to_string();

            ctx.continue_as_new(&new_input, Default::default());
        }
    }
}
```

The `WorkflowTermination::continue_as_new()` method accepts the input to pass to the next Workflow run.

## When is it right to Continue-as-New using the Rust SDK? {/* #when */}

Use Continue-as-New when your Workflow might encounter degraded performance or [Event History Limits](/workflow-execution/event#event-history).

Temporal tracks your Workflow's progress against these limits to let you know when you should Continue-as-New. Call `workflow.info().is_continue_as_new_suggested()` to check if it's time.

## How to test Continue-as-New using the Rust SDK

Testing Workflows that naturally Continue-as-New may be time-consuming and resource-intensive. Instead, add a test hook to check your Workflow's Continue-as-New behavior faster in automated tests.

For example, if you have an internal value like `test_continue_as_new == True`, this sample creates a test-only variable called `self.max_history_length` and sets it to a small value. A helper method in the Workflow impl checks it each time it considers using Continue-as-New:

```rust
use temporalio_common::protos::coresdk::workflow_commands::ContinueAsNewWorkflowExecution;
use temporalio_macros::{workflow, workflow_methods};
use temporalio_sdk::{ActivityOptions, WorkflowContext, WorkflowContextView, WorkflowResult, WorkflowTermination};
use std::time::Duration;
use serde::{Serialize, Deserialize};

use crate::activities::MyActivities;

#[derive(Serialize, Deserialize)]
pub struct GreetingInput {
    pub name: String,
    pub max_history_length: u32,
}

...

#[workflow_methods]
impl GreetingWorkflow {
    #[init]
    fn new(_ctx: &WorkflowContextView, input: GreetingInput) -> Self {
        Self {
            name: input.name,
            max_history_length: input.max_history_length,
        }
    }

    #[run]
    pub async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
        // your Workflow code here
    }

    fn should_continue_as_new(&self, ctx: &WorkflowContext<Self>) -> bool {
        if ctx.continue_as_new_suggested() {
            return true;
        }

        // For testing
        if self.max_history_length > 0 && ctx.history_length() > self.max_history_length {
            return true;
        }

        false
    }
}
```

## Best practices {/* #best-practices */}

1. Pass all necessary state: When continuing as new, include all state the next run needs.
2. Use meaningful iteration markers: Include iteration numbers or timestamps to track progress.
3. Test your state passing: Ensure parameters serialize and deserialize correctly.
4. Don't continue-as-new too frequently: It's better to have some Event History than to continue-as-new on every execution.
5. Consider batch sizes: Find the right balance between batch size and number of continues as new.

---

## Workflows - Rust SDK

![Rust SDK Banner](/img/assets/banner-rust-temporal.png)

## Workflows

- [Workflow basics](/develop/rust/workflows/basics)
- [Child Workflows](/develop/rust/workflows/child-workflows)
- [Continue-As-New](/develop/rust/workflows/continue-as-new)
- [Message passing](/develop/rust/workflows/message-passing)
- [Cancellation](/develop/rust/workflows/cancellation)
- [Timers](/develop/rust/workflows/timers)
- [Timeouts](/develop/rust/workflows/timeouts)

---

## Workflow message passing - Rust SDK

A Workflow can act like a stateful web service that receives messages: Queries, Signals, and Updates.
The Workflow implementation defines these endpoints via handler methods that can react to incoming messages and return values.

Temporal Clients use messages to read Workflow state and control its execution.
See [Workflow message passing](/encyclopedia/workflow-message-passing) for a general overview of this topic. This page introduces these features for the Temporal Rust SDK.

## Write message handlers {/* #writing-message-handlers */}

Follow these guidelines when writing your message handlers:

- Message handlers are defined as methods on your Workflow struct and registered with the Workflow runtime.
- The parameters and return values of handlers and the main Workflow function must be [serializable](/dataconversion).
- Prefer structs to multiple input parameters to allow for forward-compatible changes.

### Query handlers {/* #queries */}

A [Query](/sending-messages#sending-queries) is a synchronous operation that retrieves state from a Workflow Execution:

```rust
// workflows.rs
use std::collections::HashMap;

use temporalio_macros::{workflow, workflow_methods};
use temporalio_sdk::{WorkflowContext, WorkflowContextView, WorkflowResult};

#[derive(serde::Serialize, serde::Deserialize, Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum Language {
    Chinese,
    English,
    French,
}

#[derive(serde::Serialize, serde::Deserialize)]
pub struct GetLanguagesInput {
    pub include_unsupported: bool,
}

#[workflow(name = "greetings-workflow-10")]
pub struct GreetingsWorkflow {
    pub greetings: HashMap<Language, String>,
    pub input: GetLanguagesInput,
}

#[workflow_methods]
impl GreetingsWorkflow {
    #[init]
    fn new(_ctx: &WorkflowContextView) -> Self {
        let mut greetings = HashMap::new();
        greetings.insert(Language::Chinese, "你好，世界".to_string());
        greetings.insert(Language::English, "Hello, world".to_string());

        Self { greetings, input: GetLanguagesInput { include_unsupported: false } }
    }

    #[run]
    pub async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
        let name = ctx.state(|s| s.greetings.clone());
        Ok(format!("Hola: {:?}", name))
    }

    #[query]
    pub fn get_languages(&self, _ctx: &WorkflowContextView) -> Vec<Language> {
        if self.input.include_unsupported {
            vec![Language::Chinese, Language::English, Language::French]
        } else {
            self.greetings.keys().copied().collect()
        }
    }
}
```

```rust
// main.rs
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Connect to local Temporal server
    ...

    // Client setup
    let connection = Connection::connect(connection_options).await?;
    let client = Client::new(connection, ClientOptions::new("default").build())?;

    let wf_handle = client.start_workflow(GreetingsWorkflow::run, (), WorkflowStartOptions::new("my-task-queue", "greetings-workflow-10").build()).await?;

    // Set up Worker
    ...

    let supported_languages = wf_handle.query(GreetingsWorkflow::get_languages, GetLanguagesInput { include_unsupported: true }, WorkflowQueryOptions::default()).await?;

    // other Workflow stuff
    ...

    Ok(())
}
```

- Query handlers can't mutate Workflow state.
- Query handlers can't perform async operations, like executing Activities.

### Signal handlers {/* #signals */}

A [Signal](/sending-messages#sending-signals) is an asynchronous message sent to a running Workflow Execution to change its state and control its flow:

```rust
#[derive(serde::Serialize, serde::Deserialize)]
pub struct ApproveInput {
    pub name: String,
}

// Other structs
...

#[workflow_methods]
impl GreetingsWorkflow {
    #[init]
    fn new(_ctx: &WorkflowContextView) -> Self {
        let mut greetings = HashMap::new();
        greetings.insert(Language::Chinese, "你好，世界".to_string());
        greetings.insert(Language::English, "Hello, world".to_string());

        Self {greetings,input:GetLanguagesInput{include_unsupported:false}, approved_for_release: false, approver_name: None }
    }

    // Other Workflow logic
    ...

    #[signal]
    pub fn approve(&mut self, _ctx: &mut SyncWorkflowContext<Self>, input: ApproveInput) {
        self.approved_for_release = true;
        self.approver_name = Some(input.name);
    }
}
```

```rust
// main.rs
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Connect to local Temporal server
    ...

    // Client setup
    let connection = Connection::connect(connection_options).await?;
    let client = Client::new(connection, ClientOptions::new("default").build())?;

    let wf_handle = client.start_workflow(GreetingsWorkflow::run, (), WorkflowStartOptions::new("my-task-queue", "greetings-workflow-10").build()).await?;

    // Set up Worker
    ...

    let supported_languages = wf_handle.query(GreetingsWorkflow::get_languages, GetLanguagesInput { include_unsupported: true }, WorkflowQueryOptions::default()).await?;

    wf_handle.signal(GreetingsWorkflow::approve, ApproveInput { name: "Ziggy".to_string() }, WorkflowSignalOptions::default()).await?;

    // other Workflow stuff
    ...

    Ok(())
}
```

* Signal handlers do not return values.
* They can trigger async work (Activities, timers) depending on SDK capabilities.

### Update handlers and validators {/* #updates */}

An [Update](/sending-messages#sending-updates) is a trackable synchronous request sent to a running Workflow Execution. It can change the Workflow state, control its flow, and return a result. The sender must wait until the Worker accepts or rejects the Update. The sender may wait further to receive a returned value or an exception if something goes wrong:

```rust
// workflows.rs
...

#[derive(serde::Serialize, serde::Deserialize)]
pub struct SetLanguageInput {
    pub language: Language,
}

...

#[workflow_methods]
impl GreetingsWorkflow {
    // Other Workflow logic
    ...

    #[update]
    pub fn set_language(
        &mut self,
        _ctx: &mut SyncWorkflowContext<Self>,
        input: SetLanguageInput,
    ) -> Language {
        let previous_language = self.language;
        self.language = input.language;

        previous_language
    }

    #[update_validator(set_language)]
    fn validate_set_language(
        &self,
        _ctx: &WorkflowContextView,
        input: &SetLanguageInput,
    ) -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
        if !self.greetings.contains_key(&input.language) {
            Err("Not a valid language".into())
        } else {
            Ok(())
        }
    }
}
```

- About validators:
    - Use validators to reject an Update before it is written to History. Validators are always optional. If you don't need to reject Updates, you can skip them.
    - If you choose to create validators for your Updates, they will reject Updates before they're applied.
- Accepting and rejecting Updates with validators:
    - To reject an Update, raise an exception of any type in the validator.
    - Without a validator, Updates are always accepted.
- Validators and Event History:
    - The `WorkflowExecutionUpdateAccepted` event is written into the History whether the acceptance was automatic or programmatic.
    - When a Validator raises an error, the Update is rejected and `WorkflowExecutionUpdateAccepted` won't be added to the Event History. The caller receives an "Update failed" error.
- Update and Signal handlers can be async, letting you use Activities, Child Workflows, and more. See [Async handlers](#async-handlers) for safe usage guidelines.

## Send messages {/* #send-messages */}

To send Queries, Signals, or Updates, use a Workflow handle from the client:

```rust
let client = Client::new(connection, ClientOptions::new("default").build())?;

let wf_handle = client.start_workflow(
    GreetingsWorkflow::run,
    (),
    WorkflowStartOptions::new("my-task-queue", "greetings-workflow-10").build()
).await?;
```

### Send a Query {/* #send-query */}

```rust
let supported_languages = wf_handle.query(
    GreetingsWorkflow::get_languages,
    GetLanguagesInput { include_unsupported: true },
    WorkflowQueryOptions::default()
).await?;
```

- Sending a Query doesn’t add events to a Workflow's Event History.
- You can send Queries to closed Workflow Executions within a Namespace's Workflow retention period. This includes Workflows that have completed, failed, or timed out. Querying terminated Workflows is not safe and, therefore, not supported.
- A Worker must be online and polling the Task Queue to process a Query.

### Send a Signal {/* #send-signal */}

You can send a Signal to a Workflow Execution from a Temporal Client or from another Workflow Execution. However, you can only send Signals to Workflow Executions that haven’t closed.

#### From a Client

```rust
wf_handle.signal(
    GreetingsWorkflow::approve,
    ApproveInput { name: "Ziggy".to_string() },
    WorkflowSignalOptions::default()
).await?;
```

- The call returns when the server accepts the Signal; it does not wait for the Signal to be delivered to the Workflow Execution.

#### From a Workflow

```rust
let signal_res = ctx
    .external_workflow("workflow-id-1", Some("run-id-1".into()))
    .signal(GreetingsWorkflow::approve, ApproveInput { name: "Ziggy".to_string() })
    .await;
```

### Signal-With-Start {/* #signal-with-start */}

```rust
let signal_input = Payloads {
    payloads: vec![Payload::from("Ziggy".to_string())],
};

let wf_handle = client.start_workflow(
    GreetingsWorkflow::run,
    (),
    WorkflowStartOptions::new("my-task-queue", "greetings-workflow-10")
        .start_signal(
            WorkflowStartSignal::new("approve")
            .input(signal_input).build(),
        ).build(),
).await?;
```

### Send an Update {/* #send-update-from-client */}

An Update is a synchronous, blocking call that can change Workflow state, control its flow, and return a result.

A client sending an Update must wait until the Server delivers the Update to a Worker. Workers must be available and responsive. If you need a response as soon as the Server receives the request, use a Signal instead. You can't send Updates directly from one Workflow to another. If you need to send Updates across Workflows, like to Child Workflows, use an Activity.

- `WorkflowExecutionUpdateAccepted` is added to the Event History when the Worker confirms that the Update passed validation.
- `WorkflowExecutionUpdateCompleted` is added to the Event History when the Worker confirms that the Update has finished.

To send an Update to a Workflow Execution, you can call `execute_update` and wait for the Update to complete.

This code fetches an Update result:

```rust
let previous_language = wf_handle.execute_update(
    GreetingsWorkflow::set_language,
    SetLanguageInput { language: Language::French },
    WorkflowExecuteUpdateOptions::default()
).await?;
```

#### Update-With-Start

You can also send `start_update` to receive an `UpdateHandle` as soon as the Update is accepted.

- Use this `UpdateHandle` later to fetch your results.
- Async Update handlers normally perform long-running asynchronous operations, such as executing an Activity.
- `start_update` only waits until the Worker has accepted or rejected the Update, not until all asynchronous operations are complete.

For example:

```rust
let update_handle = main_wf_handle.start_update(
    GreetingsWorkflow::set_language,
    SetLanguageInput { language: Language::French },
    WorkflowStartUpdateOptions::default()
).await?;
```

- Updates are synchronous and return results.
- Worker must accept the Update before it proceeds.

## Message handler patterns {/* #message-handler-patterns */}

### Async handlers {/* #async-handlers */}

Signal and Update handlers can be `async fn` as well as `fn`. Using `async fn` allows you to use await with Activities, Child Workflows, Timers, etc. This expands the possibilities for what can be done by a handler, but it also means that handler executions and your main Workflow method are all running concurrently, with switching occurring between them at await calls.

It's essential to understand the things that could go wrong in order to use `async fn` handlers safely. See [Workflow message passing](/encyclopedia/workflow-message-passing) for guidance on safe usage of async Signal and Update handlers, the Safe message handlers sample and the sections below.

The following code executes an Activity that makes a network call to a remote service:

```rust
#[derive(serde::Serialize, serde::Deserialize, Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum ActivityLanguage {
    Arabic,
    Chinese,
    English,
    French,
    Hindi,
    Spanish,
}

pub struct MyActivities;

#[activities]
impl MyActivities {
    #[activity]
    pub async fn call_greeting_service(_ctx: ActivityContext, to_language: Language) -> Result<String, ActivityError> {
