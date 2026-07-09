
#### Exceptions in Updates

Doing any of the following will fail the Update and cause the client to receive the error:

- Reject the Update by throwing any exception from your [Validator](https://docs.temporal.io/handling-messages#update-validators).
- Allow a failing Activity or Child Workflow to exhaust its retries, so that it throws an [Activity Failure](https://docs.temporal.io/references/failures#activity-failure) or [Child Workflow Failure](https://docs.temporal.io/references/failures#child-workflow-failure). Note that for Activities, this will only happen if you change the default Activity [Retry Policy](https://docs.temporal.io/encyclopedia/retry-policies), since by default they retry forever.
- Throw an [Application Failure](/references/failures#application-failure) from your Update handler.

Unlike with Signals, the Workflow will keep going in these cases.

If you throw any other exception, by default, it will cause a [Workflow Task Failure](/references/failures#workflow-task-failures). This means the Workflow will get stuck and will retry the handler periodically until the exception is fixed, for example by a code change or infrastructure coming back online. Note that this will cause a delay for clients waiting for an Update result.

#### Errors and panics in message handlers in the Go SDK

In Go, returning an error behaves like an [Application Failure](/references/failures#application-failure) in the other SDKs. Panics behave like non-Application Failure exceptions in other languages, in that they cause a [Workflow Task Failure](/references/failures#workflow-task-failures).

### Writing Signal Handlers {/* #writing-signal-handlers */}

Use these links to see a simple Signal handler.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/message-passing#signals" text="Handle Signals in Go" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing#signals" text="Handle Signals in Java" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#signals" text="Handle Signals in Python" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#signals" text="Handle Signals in TypeScript" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing#signals" text="Handle Signals in .NET" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing#handle-signal" text="Handle Signals in PHP" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#signals" text="Handle Signals in Ruby" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#signals" text="Handle Signals in Rust" archetype="feature-guide" />
</RelatedReadContainer>

### Writing Update Handlers {/* #writing-update-handlers */}

Use these links to see a simple update handler.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/message-passing#updates" text="Handle Updates in Go" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing#updates" text="Handle Updates in Java" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#updates" text="Handle Updates in Python" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#updates" text="Handle Updates in TypeScript" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing#updates" text="Handle Updates in .NET" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing#handle-updates" text="Handle Updates in PHP" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#updates" text="Handle Updates in Ruby" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#updates" text="Handle Updates in Rust" archetype="feature-guide" />
</RelatedReadContainer>

### Writing Query Handlers {/* #writing-query-handlers */}

Author queries using these per-language guides.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/message-passing#queries" text="Handle Queries in Go" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing#queries" text="Handle Queries in Java" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#queries" text="Handle Queries in Python" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#queries" text="Handle Queries in TypeScript" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing#queries" text="Handle Queries in .NET" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing#handle-query" text="Handle Queries in PHP" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#queries" text="Handle Queries in Ruby" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#queries" text="Handle Queries in Rust" archetype="feature-guide" />
</RelatedReadContainer>

---

## Sending Signals, Queries, & Updates

This section will help you write clients that send messages to Workflows which includes:

- [Sending Signals](#sending-signals)
- [Sending Updates](#sending-updates)
- [Sending Queries](#sending-queries)

### Sending Signals {/* #sending-signals */}

You can send Signals from any Temporal Client, the Temporal CLI, or you can Signal one Workflow to another.

You can also Signal-With-Start to lazily initialize a Workflow while sending a Signal.

#### Send a Signal from a Temporal Client or the CLI

<RelatedReadContainer>
    <RelatedReadItem path="/cli/command-reference/workflow#signal" text="Send a Signal using the Temporal CLI" archetype="feature-guide" />
    <RelatedReadItem path="/develop/go/workflows/message-passing#send-signal-from-client" text="Send Signals with the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing#send-signal-from-client" text="Send Signals with the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing#send-signal-from-client" text="Send Signals with the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#send-signal-from-client" text="Send Signals with the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#send-signal-from-client" text="Send Signals with the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing#send-signal-from-client" text="Send Signals with the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#signals" text="Send Signals with the Ruby SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#signals" text="Send Signals with the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

#### Send a Signal from one Workflow to another

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/message-passing#send-signal-from-workflow" text="Send Signals from Workflows with the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing#send-signal-from-workflow" text="Send Signals from Workflows with the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing#send-signal-from-workflow" text="Send Signals from Workflows with the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#send-signal-from-workflow" text="Send Signals from Workflows with the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#send-signal-from-workflow" text="Send Signals from Workflows with the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing#send-signal-from-workflow" text="Send Signals from Workflows with the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#send-signal-from-workflow" text="Send Signals from Workflows with the Ruby SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#from-a-workflow" text="Send Signals from Workflows with the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

#### Signal-With-Start {/* #signal-with-start */}

Signal-With-Start is a great tool for lazily initializing Workflows. When you send this operation, if there is a running Workflow Execution with the given Workflow Id, it will be Signaled. Otherwise, a new Workflow Execution starts and is immediately sent the Signal.

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/message-passing#signal-with-start" text="Signal-With-Start using the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing#signal-with-start" text="Signal-With-Start using the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing#signal-with-start" text="Signal-With-Start using the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#signal-with-start" text="Signal-With-Start using the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#signal-with-start" text="Signal-With-Start using the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing#signal-with-start" text="Signal-With-Start using the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#signal-with-start" text="Signal-With-Start using the Ruby SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#signal-with-start" text="Signal-With-Start using the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

### Sending Updates {/* #sending-updates */}

:::note

To use the Workflow Update feature in versions prior to v1.25.0, it must be manually enabled.

Set the [frontend.enableUpdateWorkflowExecution](https://github.com/temporalio/temporal/blob/main/common/dynamicconfig/constants.go) and [frontend.enableUpdateWorkflowExecutionAsyncAccepted](https://github.com/temporalio/temporal/blob/main/common/dynamicconfig/constants.go) dynamic config values to `true`.

For example, with the Temporal CLI, run these commands:

```command
temporal server start-dev --dynamic-config-value frontend.enableUpdateWorkflowExecution=true
temporal server start-dev --dynamic-config-value frontend.enableUpdateWorkflowExecutionAsyncAccepted=true
```

:::

Updates can be sent from a Temporal Client or the Temporal CLI to a Workflow Execution. This call is synchronous and will call into the corresponding Update handler. If you’d rather make an asynchronous request, you should use Signals.

In most languages (except Go), you may call `executeUpdate` to complete an Update and get its result.

Alternatively, to start an Update, you may call `startUpdate` and pass in the Workflow Update Stage as an argument. You have two choices on what to await:

- Accepted - wait until the Worker is contacted, which ensures that the Update is persisted. See [Update Validators](/handling-messages#update-validators) for more information.
- Completed - wait until the handler finishes and returns a result. (This is equivalent to `executeUpdate`.)

The start call will give you a handle you can use to track the Update, determine whether it was Accepted, and ultimately get its result or an error.

If you want to send an Update to another Workflow such as a Child Workflow from within a Workflow, you should do so within an Activity and use the Temporal Client as normal.

There are limits on the total number of Updates that may occur during a Workflow Execution run, and also on the number of concurrent in-progress Updates that a Workflow Execution may have.
Use [Update Validators](/handling-messages#update-validators) and [Update IDs](/handling-messages#exactly-once-message-processing) to stay within the system limits in both [Cloud](/cloud/limits#per-workflow-execution-update-limits) and [Self-Hosted](/self-hosted-guide/defaults).

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/message-passing#send-update-from-client" text="Send Updates in Go" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing#send-update-from-client" text="Send Updates in Java" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing#send-update-from-client" text="Send Updates in PHP" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#send-update-from-client" text="Send Updates in Python" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#send-update-from-client" text="Send Updates in TypeScript" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing#send-update-from-client" text="Send Updates in .NET" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#send-update-from-client" text="Send Updates in Ruby" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#send-update-from-client" text="Send Updates in Rust" archetype="feature-guide" />
</RelatedReadContainer>

#### Update-With-Start {/* #update-with-start */}

:::tip

For open source server users, Temporal Server version [Temporal Server version 1.28](https://github.com/temporalio/temporal/releases/tag/v1.28.0) is recommended.

:::

Update-with-Start sends an Update request, starting a Workflow if necessary.
A [`WorkflowIDConflictPolicy`](https://docs.temporal.io/workflow-execution/workflowid-runid#workflow-id-conflict-policy) must be specified.
Workflow ID and Update ID can be used as idempotency keys as follows:

- If the Workflow exists and you provided an Update ID, and the Update exists in the latest Workflow Run, then Update-With-Start attaches to the existing Update (regardless of `WorkflowIDConflictPolicy`)
  - If the Workflow is closed, it attaches only if the Update has completed.
- Otherwise it uses [`WorkflowIDConflictPolicy`](https://docs.temporal.io/workflow-execution/workflowid-runid#workflow-id-conflict-policy) and [`WorkflowIDReusePolicy`](https://docs.temporal.io/workflow-execution/workflowid-runid#workflow-id-reuse-policy) as usual to determine whether to start a Workflow, and then starts a new Update immediately.

Update-With-Start is great for latency-sensitive use cases:

- **Lazy Initialization** -
  Instead of making separate Start Workflow and Update Workflow calls, Update-With-Start allows you to send them together in a single roundtrip.
  For example, a shopping cart can be modeled using Update-With-Start.
  Updates let you add and remove items from the cart.
  Update-With-Start lets the customer start shopping, whether the cart already exists or they've just started shopping.
  It ensures the cart, modeled by a Workflow Execution, exists before applying any Update that changes the state of items within the cart.
  Set your `WorkflowIDConflictPolicy` to `USE_EXISTING` for this pattern.
- **Early Return** -
  Using Update-With-Start you can begin a new Workflow Execution and synchronously receive a response, while the Workflow Execution continues to run to completion.
  For example, you might model a payment process using Update-With-Start.
  This allows you to send the payment validation results back to the client synchronously, while the transaction Workflow continues in the background.
  Set your `WorkflowIDConflictPolicy` to `FAIL` and use a unique Update ID for this pattern if you want to assert it does not reuse an existing Workflow.

:::caution

Unlike Signal-with-Start - Update-With-Start is _not_ atomic.
If the Update can't be delivered, for example, because there's no running Worker available, a new Workflow Execution will still start.
The SDKs will retry the Update-With-Start request, but there is no guarantee that the Update will succeed.

:::

<RelatedReadContainer>
    <RelatedReadItem path="/develop/go/workflows/message-passing#update-with-start" text="Update-With-Start with the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing#update-with-start" text="Update-With-Start with the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing#update-with-start" text="Update-With-Start with the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#update-with-start" text="Update-With-Start with the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#update-with-start" text="Update-With-Start with the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing#update-with-start" text="Update-With-Start with the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#update-with-start" text="Update-With-Start with the Ruby SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#update-with-start" text="Update-With-Start with the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

### Sending Queries {/* #sending-queries */}

Queries can be sent from a Temporal Client or the Temporal CLI to a Workflow Execution--even if this Workflow has Completed. This call is synchronous and will call into the corresponding Query handler.
You can also send a built-in "Stack Trace Query" for debugging.

<RelatedReadContainer>
    <RelatedReadItem path="/cli/command-reference/workflow#query" text="Send a Query using the Temporal CLI" archetype="feature-guide" />
    <RelatedReadItem path="/develop/go/workflows/message-passing#send-query" text="Send a Query with the Go SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/java/workflows/message-passing#send-query" text="Send a Query with the Java SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/php/workflows/message-passing#send-query" text="Send a Query with the PHP SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/python/workflows/message-passing#send-query" text="Send a Query with the Python SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/typescript/workflows/message-passing#send-query" text="Send a Query with the TypeScript SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/dotnet/workflows/message-passing#send-query" text="Send a Query with the .NET SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/ruby/workflows/message-passing#send-query" text="Send a Query with the Ruby SDK" archetype="feature-guide" />
    <RelatedReadItem path="/develop/rust/workflows/message-passing#send-query" text="Send a Query with the Rust SDK" archetype="feature-guide" />
</RelatedReadContainer>

#### Stack Trace Query {/* #stack-trace-query */}

In many SDKs, the Temporal Client exposes a predefined `__stack_trace` Query that returns the call stack of all the threads owned by that Workflow Execution.
This is a great way to troubleshoot a Workflow Execution in production.
For example, if a Workflow Execution has been stuck at a state for longer than an expected period of time, you can send a `__stack_trace` Query to return the current call stack.
The `__stack_trace` Query name does not require special handling in your Workflow code.

:::note

Stack Trace Queries are available only for running Workflow Executions.

:::

---

## Temporal Workflow message passing - Signals, Queries, & Updates

Workflows can be thought of as stateful web services that can receive messages. The Workflow can have powerful message
handlers akin to endpoints that react to the incoming messages in combination with the current state of the Workflow.
Temporal supports three types of messages: Signals, Queries, and Updates:

- Queries are read requests. They can read the current state of the Workflow but cannot block in doing so.
- Signals are asynchronous write requests. They cause changes in the running Workflow, but you cannot await any response
  or error.
- Updates are synchronous, tracked write requests. The sender of the Update can wait for a response on completion or an
  error on failure.

## How to choose between Signals, Updates, and Queries as a Workflow author? {/* #choosing-messages */}

This section will help you write Workflows that receive messages.

### For write requests

Unlike Signals, Updates must be synchronous and must wait for the Worker running the Workflow to acknowledge the
request.

The following table compares when to use **Signals** versus **Updates**.

| **Requirement type**           | **Use Signals when...**                                                                     | **Use Updates when...**                                                                                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Asynchronous communication** | Clients want to quickly move on after sending an asynchronous message.                      | Clients want to track the completion of the message.                                                                                                                                       |
| **Result handling**            | Clients are okay with “fire and forget” — no result or exception needed.                    | Clients need a result or exception without performing a query.                                                                                                                             |
| **Worker availability**        | Clients don't depend on the Worker being available.                                         | You want to validate the Update before accepting it into the Workflow and its history.                                                                                                     |
| **Concurrency and throughput** | You don’t want to limit the number of messages processed concurrently by a single Workflow. | You don’t need more concurrent Updates per Workflow than the allowed limits for [Cloud](/cloud/limits#per-workflow-execution-update-limits) or [Self-Hosted](/self-hosted-guide/defaults). |
| **Latency sensitivity**        | Since clients don’t expect a result, latency is often not relevant when using Signals.      | Clients want a low-latency end-to-end operation and are willing to wait for completion or validation.                                                                                      |

### For read requests

You normally want to do a Query, because:

- Queries are efficient–they never add entries to the [Workflow Event History](/workflow-execution/event#event-history),
  whereas an Update would (if accepted).
- Queries can operate on completed Workflows.

However, because Queries cannot block, sometimes Updates are best. When your goal is to do a read once the Workflow
achieves a certain desired state, you have two options:

- You could poll periodically with Queries until the Workflow is ready.
- You could write your read operation as an Update, which will give you better efficiency and latency, though it will
  write an entry to the [Workflow Event History](/workflow-execution/event#event-history).

### For read/write requests

Use an Update for synchronous read/write requests. If your request must be asynchronous, consider sending a Signal
followed by polling with a Query.

---

## Cloud automation - Temporal feature

Temporal Cloud Automation changes how you manage and scale your cloud infrastructure.
Its features enable you to automate critical tasks like user and namespace management, mTLS certificate rotation, and access control, ensuring security and operational efficiency.
Cloud Automation offers secure authentication across all interfaces, reducing errors and enhancing security.

**Key Features:**

- [Secure API Keys](https://docs.temporal.io/cloud/api-keys): Manage resources securely with Temporal Cloud API Keys.
- [Temporal Cloud CLI (tcld)](https://docs.temporal.io/cloud/tcld): Automate operations directly from the command line.
- [Terraform Provider for Cloud](https://docs.temporal.io/cloud/terraform-provider#prerequisites): Scale effortlessly with infrastructure-as-code.

<RelatedReadContainer>
