- [SDK metrics reference](/references/sdk-metrics) - Complete metrics documentation
- [Worker Versioning](/production-deployment/worker-deployments/worker-versioning) - Safe deployments
- [Workers in production](https://temporal.io/blog/workers-in-production) - Blog post
- [Introduction to Worker Tuning](https://temporal.io/blog/an-introduction-to-worker-tuning) - Blog post

---

## What is a Temporal Activity?

This guide provides a comprehensive overview of Temporal Activities including
[Activity Definition](/activity-definition), [Activity Type](/activity-definition#activity-type),
[Activity Execution](/activity-execution), [Local Activity](/local-activity), and [Standalone Activity](/standalone-activity).

An Activity is a normal function or method that executes a single, well-defined action (either short or long running),
such as calling another service, transcoding a media file, or sending an email message. Activity code can be
non-deterministic. We recommend that it be [idempotent](/activity-definition#idempotency).

Activities are the most common Temporal primitive and encompass small units of work such as:

- Single write operations, like updating user information or submitting a credit card payment
- Batches of similar writes, like creating multiple orders or sending multiple messages
- One or more read operations followed by a write operation, like checking a product status and user address before updating an order status
- A read that should be memoized, like an LLM call, a large download, or a slow-polling read

Larger pieces of functionality should be broken up into multiple activities. This makes it easier to do failure recovery, have short timeouts, and be idempotent.

Workflow code orchestrates the execution of Activities, persisting the results. If an Activity Execution fails,
any future attempt will start from the initial state, unless your code uses ([Heartbeat details payloads](/encyclopedia/detecting-activity-failures#activity-heartbeat))
for checkpointing (storing state on the server, and using it when resuming subsequent attempts).

Activity Functions are executed by Worker Processes. When the Activity Function returns, the Worker sends the results
back to the Temporal Service as part of the [ActivityTaskCompleted](/references/events#activitytaskcompleted) Event. The
Event is added to the Workflow Execution's Event History. For other Activity-related Events, see
[Activity Events](/workflow-execution/event#activity-events).

If you only want to execute one Activity Function, then you don't need to use a Workflow: you can
use your SDK Client to invoke it directly as a [Standalone Activity](/standalone-activity).

---

## Activity Definition

This page discusses the following:

- [Activity Definition](#activity-definition)
- [Idempotency](#idempotency)
- [Constraints](#activity-constraints)
- [Parameters](#activity-parameters)
- [Activity Type](#activity-type)

In day-to-day conversation, the term _Activity_ denotes an [Activity Definition](/activity-definition), [Activity Type](/activity-definition#activity-type), or [Activity Execution](/activity-execution).
Temporal documentation aims to be explicit and differentiate between them.

## What is an Activity Definition? {/* #activity-definition */}

An Activity Definition is the code that defines the constraints of an [Activity Task Execution](/tasks#activity-task-execution).
Activities encapsulate business logic that is prone to failure, allowing for automatic retries when issues occur.

Below are examples of basic Activity Definitions across supported SDKs.

<Tabs groupId="basic-activity-definition" queryString>
<TabItem value="go" label="Go">

**[Activity Definition in Go](/develop/go/activities/basics)**

```go

    "context"

    "go.temporal.io/sdk/activity"
)

func YourSimpleActivity(ctx context.Context) error {
    return nil
}
```

</TabItem>
<TabItem value="java" label="Java">

**[Activity Definition in Java (Interface)](/develop/java/activities/basics)**

```java
@ActivityInterface
public interface GreetingActivities {
    @ActivityMethod
    String composeGreeting(String greeting, String language);
}
```

**[Activity Definition in Java (Implementation)](/develop/java/activities/basics)**

```java
static class GreetingActivitiesImpl implements GreetingActivities {
    @Override
    public String composeGreeting(String greeting, String name) {
        return greeting + " " + name + "!";
    }
}
```

</TabItem>
<TabItem value="php" label="PHP">

**[Activity Definition in PHP (Interface)](/develop/php/activities/basics)**

```php
#[ActivityInterface]
interface GreetingActivities
{
    public function composeGreeting(string $greeting, string $name): string;
}
```

**[Activity Definition in PHP (Implementation)](/develop/php/activities/basics)**

```php
class GreetingActivitiesImpl implements GreetingActivities
{
    public function composeGreeting(string $greeting, string $name): string
    {
        return $greeting . ' ' . $name;
    }
}
```

</TabItem>
<TabItem value="python" label="Python">

**[Activity Definition in Python](/develop/python/activities/basics)**

```python
from temporalio import activity

@activity.defn(name="your_activity")
async def your_activity(input: YourParams) -> str:
    return f"{input.greeting}, {input.name}!"
```

</TabItem>
<TabItem value="typescript" label="TypeScript">

**[Activity Definition in TypeScript](/develop/typescript/activities/basics)**

```ts
export async function greet(name: string): Promise<string> {
  return `Hello, ${name}!`;
}
```

</TabItem>
<TabItem value="dotnet" label=".NET">

**[Activity Definition in C# and .NET](/develop/dotnet/activities/basics)**

```csharp
using Temporalio.Activities;

public class MyActivities
{
    [Activity]
    public string MyActivity(MyActivityParams input) =>
        $"{input.Greeting}, {input.Name}!";
}
```

</TabItem>
<TabItem value="rust" label="Rust">

**[Activity Definition in Rust](/develop/rust/activities/basics)**

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
}
```

</TabItem>
</Tabs>

For full SDK-specific guides, see:

- [How to develop an Activity Definition using the Go SDK](/develop/go/activities/basics)
- [How to develop an Activity Definition using the Java SDK](/develop/java/activities/basics)
- [How to develop an Activity Definition using the PHP SDK](/develop/php/activities/basics)
- [How to develop an Activity Definition using the Python SDK](/develop/python/activities/basics)
- [How to develop an Activity Definition using the TypeScript SDK](/develop/typescript/activities/basics)
- [How to develop an Activity Definition using the .NET SDK](/develop/dotnet/activities/basics)
- [How to develop an Activity Definition using the Rust SDK](/develop/rust/activities/basics)

The term 'Activity Definition' is used to refer to the full set of primitives in any given language SDK that provides an access point to an Activity Function Definition——the method or function that is invoked for an [Activity Task Execution](/tasks#activity-task-execution).
Therefore, the terms Activity Function and Activity Method refer to the source of an instance of an execution.

Activity Definitions are named and referenced in code by their [Activity Type](/activity-definition#activity-type).

<CaptionedImage
    src="/diagrams/activity-definition.svg"
    title="Activity Definition"
    />

### Idempotency {/* #idempotency */}

Temporal recommends that Activities be idempotent.

Idempotence means that performing an operation multiple times has the same result as performing it once.
In the context of Temporal, Activities should be designed to be safely executed multiple times without causing unexpected or undesired side effects.

Consider the power button on your laptop. When you press it, the machine is changed from one state to the other, from on to off, and vice versa. This is not an idempotent operation. Each invocation leads to a different state. However, imagine that you modified your laptop to have separate on and off buttons. Pressing the On button multiple times would have no effect beyond the initial invocation as the laptop is already on. This action is considered idempotent.

<CaptionedImage
  src="/diagrams/idempotence-image.png"
/>

Idempotency is an important design consideration in software applications as well. You have probably encountered idempotent operations in your work already.

A few examples where idempotent operations are vital would be:

- **Infrastructure-as-Code (IaC) tool** - Conserving resources is important when you're provisioning infrastructure in the cloud. An IaC system that was not designed with idempotence in mind could lead to high costs if the function to provision a new server was accidentally invoked multiple times. An IaC tool that is designed with idempotence in mind ensures that multiple invocations of the tool doesn't lead to unintended instances being created.
- **Payment processing system** - A payment processing system must charge the customer only once for a given purchase. If the system was not designed to be idempotent, duplicate requests would result in extra charges and unhappy customers. A payment processing system that is designed to be idempotent ensures customers are not charged multiple times for the same transaction, preventing financial discrepancies.

:::info

By design, completed Activities will not re-execute as part of a [Workflow Replay](/workflow-execution#replay). However, Activities won’t record to the [Event History](/encyclopedia/retry-policies#event-history) until they return or produce an error. If an Activity fails to report to the server at all, it will be retried. Designing for idempotence, especially if you have a [Global Namespace](/global-namespace), will improve reusability and reliability.

:::

An Activity is idempotent if multiple [Activity Task Executions](/tasks#activity-task-execution) do not change the state of the system beyond the first Activity Task Execution.

The lack of idempotency might affect the correctness of your application but does not affect the Temporal Platform.
In other words, lack of idempotency doesn't lead to a platform error.

In some cases, whether something is idempotent doesn't affect the correctness of an application.
For example, if you have a monotonically incrementing counter, you might not care that retries increment the counter because you don't care about the actual value, only that the current value is greater than a previous value.

You should always make your business logic Activities idempotent in Temporal. Because Activities may be retried, these functions may be executed more than once. A non-idempotent Activity could adversely affect the state of the system.

Activities are an atomic unit of execution within Temporal. They are invoked and either complete successfully or not. Take this into consideration when you design your Activities.

For example, consider an Activity that has the following three steps:

1. Perform a database lookup
2. Make a call to a microservice with parameters retrieved from the database
3. Write the result of the microservice call to the filesystem

Imagine that the first two steps succeed, but the third step fails due to a permissions issue. During retry, the entire Activity—and therefore each of the three steps—is executed again. To maintain idempotency, design your Activities to be more granular. In this case, you could have three Activities, one for each step. This way, only the step that failed will be executed again. However, you must balance this against the potential for a larger Event History, since there would now be three Activity Executions instead of one.

Idempotence for Activities is also important due to a particular edge case inherent in distributed computing. Consider a scenario in which a Worker polls the Temporal Service, accepts the Activity Task, and begins executing the Activity. The Activity function completes successfully, but the Worker crashes just before it notifies the Temporal Service. In this case, the Event History won’t reflect the successful completion of the Task, so the Activity will be retried. If the Activity is not idempotent, this could have negative consequences, such as duplicate charges in a payment processing scenario.

You can achieve idempotency in your application through the use of unique identifiers, known as idempotency keys, which are used to detect duplicate requests. These are enforced by the service you are calling from your Activity, not by the Activity itself.

For example, the APIs provided by most payment processors allow the client to include an idempotency key with the request. When the payment service receives a request, it checks a database to determine whether there has already been a request with this key. If so, the duplicate request is ignored and does not result in another charge. If not, then it writes a new record to the database with this key, allowing it to identify duplicate requests in the future.

In Temporal, the request to the payment service would be made from within an Activity. You can use a combination of the Workflow Run ID and the Activity ID as an idempotency key since this is guaranteed to be consistent across retry attempts but unique among Workflow Executions.

For more information about idempotency in Temporal, see the following post:

[Idempotency and Durable Execution](https://temporal.io/blog/idempotency-and-durable-execution)

### Activity retry policy

The Activity retry mechanism gives applications the benefits of durable execution.
For example, Temporal will keep track of the [exponential backoff delay](/encyclopedia/retry-policies#backoff-coefficient) even if the Worker crashes. Since Temporal can’t tell when a Worker crashes, Workflows rely on the [start_to_close timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout) to know how long to wait before assuming that an Activity is inactive.

For an Activity with a [Retry Policy](/encyclopedia/retry-policies) that allows retries, Temporal guarantees that the Activity will be observed as completed exactly once. However, the Activity may be executed multiple times and may even partially complete more than once during this process. This could lead to a scenario where certain parts of the Activity are executed multiple times before a successful execution is completed.

:::caution
Be cautious when doing retries within your Activity because it lengthens the needed Activity timeout.  Such internal retries also prevent users from counting failure metrics and make it harder for users to debug in Temporal UI when something is wrong.
:::

### Constraints {/* #activity-constraints */}

Activity Definitions are executed as normal functions.

In the event of failure, the function begins at its initial state when retried (except when Activity Heartbeats are established).

Therefore, an Activity Definition has no restrictions on the code it contains.

### Parameters {/* #activity-parameters */}

An Activity Definition can support as many parameters as needed.

All values passed through these parameters are recorded in the [Event History](/workflow-execution/event#event-history) of the Workflow Execution.
Return values are also captured in the Event History for the calling Workflow Execution.

Activity Definitions must contain the following parameters:

- Context: an optional parameter that provides Activity context within multiple APIs.
- Heartbeat: a notification from the Worker to the Temporal Service that the Activity Execution is progressing. Cancelations are allowed only if the Activity Definition permits Heartbeating.
- Timeouts: intervals that control the execution and retrying of Activity Task Executions.

Other parameters, such as [Retry Policies](/encyclopedia/retry-policies) and return values, can be seen in the implementation guides, listed in the next section.

## What is an Activity Type? {/* #activity-type */}

An Activity Type is the mapping of a name to an Activity Definition.

Activity Types are scoped through Task Queues.

## Best practices for defining Activities

Here are some best practices you can use when you are creating Activities for your Workflow:

- Activity arguments and return values should be serializable.
- Activities that perform writes should be idempotent.
- Activities have [timeouts](/develop/python/activities/timeouts#activity-heartbeats) and [retry policies](/encyclopedia/retry-policies). For Activities, your operation should either complete within a few minutes or it should support the ability to heartbeat or poll for a result. This way it will be clear to the Workflow when the Activity is still making progress.
- You need to specify at least one timeout, typically the [start_to_close timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout). Keep in mind that the shorter the timeout, the faster Temporal will retry upon failure. See the [Activity retry policy section](#activity-retry-policy) to learn more.

---

## Activity Execution

This page discusses the following:

- [Activity Execution](#activity-execution)
- [Cancellation](#cancellation)
- [Activity Id](#activity-id)
- [Asynchronous Activity Completion](#asynchronous-activity-completion)
- [Task Token](#task-token)

## What is an Activity Execution? {/* #activity-execution */}

An Activity Execution is the full chain of [Activity Task Executions](/tasks#activity-task-execution).

:::info

- [How to start an Activity Execution using the Go SDK](/develop/go/activities/execution)
- [How to start an Activity Execution using the Java SDK](/develop/java/activities/execution)
- [How to start an Activity Execution using the PHP SDK](/develop/php/activities/execution)
- [How to start an Activity Execution using the Python SDK](/develop/python/activities/execution)
- [How to start an Activity Execution using the TypeScript SDK](/develop/typescript/activities/execution)
- [How to start an Activity Execution using the .NET SDK](/develop/dotnet/activities/execution)

:::

<CaptionedImage src="/diagrams/activity-execution.svg" title="Activity Execution" />

You can customize [Activity Execution timeouts](/encyclopedia/detecting-activity-failures#start-to-close-timeout) and
[retry policies](/encyclopedia/retry-policies).

If an Activity Execution fails (because it exhausted all retries, threw a
[non-retryable error](/encyclopedia/retry-policies#non-retryable-errors), or was canceled), the error is returned to your
[Workflow](/workflows) code when it attempts to fetch the Activity result. For [Standalone Activities](/standalone-activity) the error is
returned to the Client when you attempt to fetch the Activity result.

:::note

Temporal guarantees that an Activity Task either runs or timeouts. There are multiple failure scenarios when an Activity
Task is lost. It can be lost during delivery to a Worker or after the Activity Function is called and the Worker
crashed.

Temporal doesn't detect task loss directly. It relies on
[Start-To-Close timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout). If the Activity Task times
out, the Activity Execution will be retried according to the Activity Execution Retry Policy.

In scenarios where the Activity Execution Retry Policy is set to `1` and a Timeout occurs, the Activity Execution will
not be tried.

:::

## Cancellation {/* #cancellation */}

Activity Cancellation:

- lets the Activity know it doesn't need to keep doing work, and
- gives the Activity time to clean up any resources it has created.

Activities must heartbeat to receive cancellations from a Temporal Service.

An Activity may receive Cancellation if:

- The Activity was requested to be Cancelled. This can often cascade from Workflow Cancellation, but not always—SDKs
  have ways to stop Cancellation from cascading. {/* TODO link to workflow cancellation */}
- The Activity was considered failed by the Server because any of the Activity timeouts have triggered (for example, the
  Server didn't receive a heartbeat within the Activity's Heartbeat timeout). The
  [Cancelled Failure](/references/failures#cancelled-failure) that the Activity receives will have
  `message: 'TIMED_OUT'`.
- The Workflow Run reached a [Closed state](/workflow-execution#workflow-execution-status), in which case the Cancelled
  Failure will have `message: 'NOT_FOUND'`.
- In some SDKs:
  - The Worker is shutting down.
  - An Activity sends a Heartbeat but the Heartbeat details can't be converted by the Worker's configured
    [Data Converter](/dataconversion). This fails the Activity Task Execution with an Application Failure.
  - The Activity timed out on the Worker side and is not Heartbeating or the Temporal Service hasn't relayed a
    Cancellation.

There are different ways to receive Cancellation depending on the SDK. {/* TODO link to dev guide */} An Activity may
accept or ignore Cancellation:

- To allow Cancellation to happen, let the Cancellation Failure propagate.
- To ignore Cancellation, catch it and continue executing.

Some SDKs have ways to shield tasks from being stopped while still letting the Cancellation propagate.

The Workflow can also decide if it wants to wait for the Activity Cancellation to be accepted or to proceed without
waiting.

Cancellation can only be requested a single time. If you try to cancel your Activity Execution more than once, it will
not receive more than one Cancellation request.

## What is an Activity Id? {/* #activity-id */}

The identifier for an [Activity Execution](#activity-execution). The identifier can be generated by the system, or it
can be provided by the Workflow code that spawns the Activity Execution. The identifier is unique among the open
Activity Executions of a [Workflow Run](/workflow-execution/workflowid-runid#run-id). (A single Workflow Run may reuse
an Activity Id if an earlier Activity Execution with the same Id has closed.)

An Activity Id can be used to [complete the Activity asynchronously](#asynchronous-activity-completion).

[Standalone Activities](/standalone-activity) have a separate ID space from Workflows and other Temporal primitives.
This means use of conflict policy (`USE_EXISTING`, …) and reuse policy (`REJECT_DUPLICATES`, …) will only observe the Standalone Activity ID space.

## What is Asynchronous Activity Completion? {/* #asynchronous-activity-completion */}

Asynchronous Activity Completion is a feature that enables an Activity Function to return without causing the Activity
Execution to complete. The Temporal Client can then be used from anywhere to both Heartbeat Activity Execution progress
and eventually complete the Activity Execution and provide a result.

How to complete an Activity Asynchronously in:

- [Go](/develop/go/activities/asynchronous-activity)
- [Java](/develop/java/activities/asynchronous-activity)
- [PHP](/develop/php/activities/asynchronous-activity)
- [Python](/develop/python/activities/asynchronous-activity)
- [TypeScript](/develop/typescript/activities/asynchronous-activity)
- [.NET](/develop/dotnet/activities/asynchronous-activity)

### When to use Async Completion

When an external system has the final result of a computation that is started by an Activity, there are three main ways
of getting the result to the Workflow:

1. The external system uses Async Completion to complete the Activity with the result.
2. The Activity completes normally, without the result. Later, the external system sends a Signal to the Workflow with
   the result.
3. A subsequent Activity
   [polls the external system](https://community.temporal.io/t/what-is-the-best-practice-for-a-polling-activity/328/2)
   for the result.

If you don't have control over the external system — that is, you can't add Async Completion or a Signal to its code —
then:

- you can poll (#3), or
- if the external system can reliably call a webhook (and retry calling in the case of failure), you can write a webhook
  handler that sends a Signal to the Workflow (#2).

The decision between using #1 vs #2 involves a few factors. Use Async Completion if:

- the external system is unreliable and might fail to Signal, or
- you want the external process to Heartbeat or receive Cancellation.

Otherwise, if the external system can reliably be trusted to do the task and Signal back with the result, and it doesn't
need to Heartbeat or receive Cancellation, then you may want to use Signals.

The benefit to using Signals has to do with the timing of failure retries. For example, consider an external process
that is waiting for a human to review something and respond, and they could take up to a week to do so. If you use Async
Completion (#1), you would:

- set a [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout) of one week on the
  Activity,
- in the Activity, notify the external process you need the human review, and
- have the external process Asynchronously Complete the Activity when the human responds.

If the Activity fails on the second step to notify the external system and doesn't throw an error (for example, if the
Worker dies), then the Activity won't be retried for a week, when the Start-To-Close Timeout is hit.

If you use Signals, you would:

- set a [Start-To-Close Timeout](/encyclopedia/detecting-activity-failures#start-to-close-timeout) of one minute on the
