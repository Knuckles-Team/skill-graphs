        // Pretend that we are calling a remote service.
        sleep(Duration::from_millis(200)).await;

        let mut greetings = HashMap::new();

        greetings.insert(Language::Arabic, "مرحبا بالعالم".to_string());
        greetings.insert(Language::Chinese, "你好，世界".to_string());
        greetings.insert(Language::English, "Hello, world".to_string());
        greetings.insert(Language::French, "Bonjour, monde".to_string());
        greetings.insert(Language::Hindi, "नमस्ते दुनिया".to_string());
        greetings.insert(Language::Spanish, "Hola mundo".to_string());

        let result = greetings.get(&to_language).cloned();

        Ok(format!("Hello, {:?}!", result))
    }
}
```

After updating the code to use an `async fn`, your Update handler can schedule an Activity and await the result. Although an `async fn` Signal handler can also execute an Activity, using an Update handler allows the client to receive a result or error once the Activity completes.

This lets your client track the progress of asynchronous work performed by the Update's Activities, Child Workflows, etc. Here's how you could start that Activity from within your Workflow:

```rust
#[update]
async fn set_language_activity(
    ctx: &mut WorkflowContext<Self>,
    language: Language,
) -> Language {
    let needs_greeting = ctx.state(|s| !s.greetings.contains_key(&language));

    if needs_greeting {
        ctx.wait_condition(|s| !s.approved_for_release).await;

        ctx.state_mut(|s| {
            s.approved_for_release = true;
        });

        let result = async {
            let greeting = ctx.start_activity(
                MyActivities::call_greeting_service,
                Language::French,
                ActivityOptions::start_to_close_timeout(Duration::from_secs(10))
            ).await;

            ctx.state_mut(|s| {
                s.greetings.insert(language, greeting.unwrap());
            });
        }.await;

        ctx.state_mut(|s| {
            s.approved_for_release = false;
        });

        result;
    }

    let previous_language = ctx.state(|s| s.language);

    ctx.state_mut(|s| {
        s.language = language;
    });

    previous_language
}
```

### Add wait conditions to block

Sometimes, async Signal or Update handlers need to meet certain conditions before they should continue. You can use `ctx.wait_condition` to prevent the code from proceeding until a condition is true. You specify the condition by passing a function that returns a boolean and you can optionally set a timeout. This is an important feature that helps you control your handler logic.

Here are three important use cases for `ctx.wait_condition`:

- Wait for a Signal or Update to arrive.
- Wait in a handler until it's appropriate to continue.
- Wait in the main Workflow until all active handlers have finished.

It's common to use `ctx.condition` to wait for a particular Signal or Update to be sent by a client. In your Workflow, you will have something like:

```rust
#[run]
pub async fn run(ctx: &mut WorkflowContext<Self>) -> WorkflowResult<String> {
    let name = ctx.state(|s| s.greetings.clone());

    ctx.wait_condition(|s| !s.approved_for_release).await;

    // Other Workflow logic
    ...
}
```

### Ensure handlers finish before completion

Workflow wait conditions can ensure your handler completes before a Workflow finishes. When your Workflow uses async Signal or Update handlers, your main Workflow method can return or continue-as-new while a handler is still waiting on an async task, such as an Activity result.

The Workflow completing may interrupt the handler before it finishes crucial work and cause client errors when trying retrieve Update results. Use `ctx.wait_condition` to address this problem and allow your Workflow to end smoothly.

---

## Workflow Timeouts - Rust SDK

## Workflow timeouts {/* #workflow-timeouts */}

Each Workflow timeout controls the maximum duration of a different aspect of a Workflow Execution.

In most cases, **Workflow Timeouts are not recommended**. Temporal Workflows are designed to be long-running and resilient. Setting timeouts can unnecessarily limit their ability to tolerate delays or extended processing.

If you need to trigger logic after a specific duration, use a **Timer inside the Workflow** instead of a timeout.

You can configure Workflow timeouts when starting a Workflow Execution.

Available timeouts include:

- [Workflow Execution Timeout](/encyclopedia/detecting-workflow-failures#workflow-execution-timeout): Maximum total time a Workflow Execution can run.
- [Workflow Run Timeout](/encyclopedia/detecting-workflow-failures#workflow-run-timeout): Maximum time a single Workflow Run can last.
- [Workflow Task Timeout](/encyclopedia/detecting-workflow-failures#workflow-task-timeout): Maximum time a Worker can take to complete a Workflow Task.

In Rust, you set these via `WorkflowStartOptions` when starting or executing a Workflow.

Available fields:

- `execution_timeout`
- `run_timeout`
- `task_timeout`

```rust
let wf_handle = client.start_workflow(
    GreetingsWorkflow::run,
    (),
    WorkflowStartOptions::new(
        "my-task-queue",
        "greetings-workflow-10",
    )
    // Set timeouts
    .execution_timeout(Duration::from_secs(3600))
    .run_timeout(Duration::from_secs(600))
    .task_timeout(Duration::from_secs(10))
    .build()
).await?;
```

## Workflow retries {/* #workflow-retries */}

A Retry Policy can be used alongside timeouts to control how Workflow Executions are retried after failure.

Workflow Executions do **not retry by default**. Retry Policies should only be applied when restarting the entire Workflow is safe and intentional.

To enable retries, configure a [Retry Policy](/encyclopedia/retry-policies) when starting the Workflow.

```rust
let wf_handle = client.start_workflow(
    GreetingsWorkflow::run,
    (),
    WorkflowStartOptions::new(
        "my-task-queue",
        "greetings-workflow-10",
    )
    .retry_policy(RetryPolicy {
        initial_interval: Some(prost_dur!(from_secs(1))),
        backoff_coefficient: 2.0,
        maximum_interval: Some(prost_dur!(from_secs(100))),
        maximum_attempts: 5,
        non_retryable_error_types: vec!["NonRetryableError".to_string()],
    }).build()
).await?;
```

Retry Policies define retry behavior such as backoff intervals, maximum attempts, and retry conditions.

---

## Timers - Rust SDK

A Workflow can set a Durable Timer for a fixed time period. In some SDKs, the function is called `sleep()`, and in others, it's called `timer()`.

A Workflow can sleep for days, months, or even years. Timers are persisted, so even if your Worker or Temporal Service is down when the time period completes, as soon as your Worker and Temporal Service are back up, the `sleep()` call will resolve and your code will continue executing.

Sleeping is a resource-light operation: it doesn't tie up the process, and you can run millions of Timers off a single Worker.

To set a Timer in Rust, use the `timer()` function and pass the duration you want to wait before continuing.

```rust
ctx.timer(TimerOptions {
    duration: Duration::from_secs(60),
    summary: Some("important timer".into())
}).await;
```

---

## Safely deploying changes to Workflow code

Making changes safely to existing Workflow code requires care. Your Workflow code--as opposed to your Activity code--must be [deterministic](/workflow-definition#deterministic-constraints). This means your changes to that code have to be as well. Changes to your Workflow code that qualify as non-deterministic need to be protected by either using [Worker Versioning](/production-deployment/worker-deployments/worker-versioning) to pin your Workflows to specific code revisions, or by using the [patching APIs](/workflow-definition#workflow-versioning) within your Workflow code.

:::note
We strongly recommend using Worker Versioning as users see improved error rates when adopting it.
:::

In this article, we’ll provide some advice on how you can safely validate changes to your Workflow code, ensuring that you won’t experience unexpected non-determinism errors in production when rolling them out.

:::caution
Eager start does not respect Worker versioning. An eagerly started Workflow may run on any available local Worker even if that Worker is not the Current or Ramping version of its Worker deployment.
:::

## Use Replay Testing before and during your deployments

The best way to verify that your code won’t cause non-determinism errors once deployed is to make use of [replay testing](/workflow-execution#replay).

Replay testing takes one or more existing [Event Histories](/workflow-execution/event#event-history) that ran against a previous version of Workflow code and runs them against your _current_ Workflow code, verifying that it is compatible with the provided history.

In the case of Worker Versioning, you may have a [pinned Workflow](/worker-versioning#pinned) that you're switching over to the [current Worker deployment version](/worker-versioning#versioning-definitions) and you want to make sure that the changes don't introduce non-determinism errors. Or you may have an [Auto-Upgrade Workflow](/worker-versioning#auto-upgrade) that you want to run automated tests on to ensure the deployments don't trigger errors.

There are multiple points in your development lifecycle where running replay tests can make sense. They exist on a spectrum, with shortest time to feedback on one end, and most representative of a production deployment on the other.

- During development, replay testing lets you get feedback as early as possible on whether your changes are compatible. For example, you might include some integration tests that run your Workflows against the Temporal Test Server to produce histories which you then check in. You can use those checked-in histories for replay tests to verify you haven’t made breaking changes.
- During pre-deployment validation (such as during some automated deployment validation) you can get feedback in a more representative environment. For example, you might fetch histories from a live Temporal environment (whether production or some kind of pre-production) and use them in replay tests.
- At deployment time, your environment _is_ production, but you are using the new code to replay recent real-world Workflow histories.

When you're writing changes to Workflow code, you can fetch some representative histories from your pre-production or production Temporal environment and verify they work with your changes. You can do the same with the pre-merge CI pipeline. However, if you are using encrypted Payloads, which is a typical and recommended setup in production, you may not be able to decrypt the fetched histories.

Additionally if your Workflows contain any PII (which should be encrypted), make sure this information is scrubbed for the purposes of your tests, or err on the side of caution and don’t use this method.
With that constraint in mind, we’ll focus on how you can perform replay tests in a production deployment of a Worker with new Workflow code. The core of how replay testing is done is the same regardless of when you choose to do it, so you can apply some of the lessons here to earlier stages in your development process.

## Implement a deployment-time replay test

The key to a successful safe deployment is to break it into two phases: a verification phase, where you’ll run the replay test, followed by the actual deployment of your new Worker code.

You can accomplish this by wrapping your Worker application with some code that can choose whether it will run in verification mode, or in production. This is most easily done if you do not deploy your Workers side-by-side with other application code, which is a recommended best practice. If you do deploy your Workers as part of some other application, you will likely need to separate out a different entry point specifically for verification.

### Run a replay and real Worker with the same code

The following code demonstrates how the same entry point could be used to either verify the new code using replay testing, or to actually run the Worker.

```python

from datetime import datetime, timedelta

from temporalio.client import Client
from temporalio.worker import Worker, Replayer

async def main():
    parser = argparse.ArgumentParser(prog='MyTemporalWorker')
    parser.add_argument('mode', choices=['verify', 'run'])
    args = parser.parse_args()

    temporal_url = "localhost:7233"
    task_queue = "your-task-queue"
    my_workflows = [YourWorkflow]
    my_activities = [your_activity]

    client = await Client.connect(temporal_url)
```

Everything up to this point is standard. You import the Workflow and Activity code, instantiate a parser with two modes, and create your Task Queue, Workflow, and Activity.

You can pass in the `args.mode` from any appropriate spot in your code. If the mode is set to `verify`, you conduct the replay testing by specifying the time period to test, and passing in the Workflows corresponding to that time period. Note that the Workflows are consumed as histories, using [the `map_histories()` function](https://python.temporal.io/temporalio.client.WorkflowExecutionAsyncIterator.html#map_histories).

```python
if args.mode == 'verify':
    start_time = (datetime.now() - timedelta(hours=10)).isoformat(timespec='seconds')
    workflows = client.list_workflows(
     f"TaskQueue={task_queue} and StartTime > '{start_time}'",
    limit = 100)
    histories = workflows.map_histories()
    replayer = Replayer(
        workflows=my_workflows,
    )
    await replayer.replay_workflows(histories)
    return
```

If any of the Workflows fail to replay, an error will be thrown. If no errors occur, you can return successfully to indicate success here, or communicate with an endpoint you've defined to indicate success or failure of the verification. You could switch to the `run` mode, and have this Worker transition to a real Worker that will start pulling from the Task Queue and processing Workflows:

```python
    else:
        worker = Worker(
            client,
            task_queue=task_queue,
            workflows=my_workflows,
            activities=my_activities,
        )
        await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
```

### Use the multi-modal Worker

The most straightforward way to use this bimodal Worker is to deploy one instance of it at the beginning of your deployment process in verify mode, see that it passes, and then proceed to deploy the rest of your new workers in run mode.

---

## Standalone Activities Demo

<ReleaseNoteHeader
  featureName="standaloneActivity"
  languages={["Go", "Python", "Java", ".NET", "TypeScript", "Ruby"]}
>
  Available in [Temporal Cloud](/standalone-activity#temporal-cloud-support) and in the [Temporal CLI](/standalone-activity#temporal-cli-support) v1.7.0 or higher with Temporal Server v1.31.0 or higher. Java SDK support is in [Pre-release](/evaluate/development-production-features/release-stages#pre-release).
</ReleaseNoteHeader>

Standalone Activities let you run a single Activity straight from your application without
writing a Workflow. Your code uses the Temporal Client to send the request to the Server, the Server durably enqueues the request
for a Worker to pick up, and the result comes back through a handle that your code can wait on or
check later.

Try the demo below to walk through the full flow, tweak the retry and timeout settings, and watch
the SDK code and CLI command update as you go.

<StandaloneActivityDemo />

---

## How it works

When you call `client.execute_activity()` (or the equivalent in your applicable SDK) from your
application, the following happens:

1. **Connect**: Your application opens a connection to the Temporal Server using a Temporal Client
   configured with your namespace and credentials.
2. **Schedule**: The Server durably persists the Activity Task on the specified Task Queue so that
   the request survives Worker restarts and network interruptions.
3. **Poll**: A Worker that is polling that Task Queue picks up the Activity Task and prepares to
   execute it.
4. **Execute**: The Worker runs your Activity function with the provided arguments and reports the
   outcome back to the Server.
5. **Return**: The Server stores the result and returns it to the original caller, either directly
   or via a handle, depending on which SDK method you use.

### Standalone vs Workflow Activities

| | Workflow Activity | Standalone Activity |
|---|---|---|
| Orchestrated by | A Workflow Definition | Your application code (via the Temporal Client) |
| Started with | `workflow.execute_activity()` (or the equivalent in your applicable SDK) from inside a Workflow Definition | `client.execute_activity()` (or the equivalent in your applicable SDK) from your application code |
| Retry policy | Set when calling the Activity from inside a Workflow | Set when calling the Activity from your application |
| Visibility | Shown in the Workflow's Event History | Shown in the Standalone Activity list and count views |
| Use case | Multi-step orchestration with multiple Activities | Single, independent jobs like sending an email or processing a webhook |

The Activity function and Worker registration are **identical** for both approaches, and only the
execution path that triggers the Activity differs between them. If the Activity fails, the Server
automatically retries it according to the Retry Policy you configure.

---

## Next steps

For complete API reference and advanced usage, see the SDK-specific guides:

  {[
    { name: 'goLangBlock',     href: '/develop/go/activities/standalone-activities',         label: 'Standalone Activities - Go' },
    { name: 'javaBlock',       href: '/develop/java/activities/standalone-activities',       label: 'Standalone Activities - Java' },
    { name: 'pythonBlock',     href: '/develop/python/activities/standalone-activities',     label: 'Standalone Activities - Python' },
    { name: 'typeScriptBlock', href: '/develop/typescript/activities/standalone-activities', label: 'Standalone Activities - TypeScript' },
    { name: 'dotnetBlock',     href: '/develop/dotnet/activities/standalone-activities',     label: 'Standalone Activities - .NET' },
  ].map(({ name, href, label }) => (

          <SdkSvg name={name} />

      {label}

  ))}

---

## Task Queue Priority and Fairness

[Task Queue Priority](#task-queue-priority) and [Task Queue Fairness](#task-queue-fairness) are two ways to manage the
distribution of work within a Task Queue. Priority allows [Tasks](/tasks) to be executed in Priority order.
Fairness prevents one set of Tasks from blocking others within the same priority level.

You can use Priority and Fairness individually or combine them to express Fairness within a Priority level.

## Task Queue Priority

**Task Queue Priority** lets you control the execution order of Workflows, Activities, and Child Workflows based on assigned priority values within a Task Queue. Each priority level acts as a sub-queue that separates Tasks so that high priority Tasks can cut in front of low priority Tasks.

<EnlargeImage
  src="/img/develop/task-queue-priority-fairness/priority-details.png"
  alt="Flowchart of how Priority dispatches Tasks from highest to lowest priority queue"
/>

### When to use Priority

If you need a way to specify the order your Tasks execute in, you can use Priority to manage that. Priority lets you differentiate between your Tasks, like batch and real-time Tasks, so that you can use a single pool of Workers for efficient resource allocation, while ensuring real-time Tasks are processed ahead of batch Tasks.

You can also use this as a way to run urgent Tasks immediately and override others. For example, if you are running an e-commerce platform, you may want to process payment related Tasks before less time-sensitive Tasks like internal inventory management.

### How to use Priority

Priority is enabled by default in both Temporal Cloud and self-hosted Temporal. To disable Priority in self-hosted Temporal, set the [dynamic config](/temporal-service/configuration#dynamic-configuration) `matching.useNewMatcher` to `false` on a Task Queue, Namespace, or globally.

To use Priority, you need to set a _priority key_ at the Workflow, Activity, or Child Workflow level to a value within the integer range `[1,5]`.
A lower value implies higher priority, so `1` is the highest priority level. If you don't specify a Priority, a Task defaults to a
Priority of `3`. Activities and Child Workflows will inherit their Workflow's priority unless they explicitly specify
their own priority.

When Priority is enabled, all Tasks within a Task Queue will be processed in Priority order. For example, all priority level `1` Tasks will start executing before the first priority level `2` Task, and so on. Lower priority Tasks will be blocked until all higher priority Tasks have started. Tasks are scheduled by default to run in first-in-first-out (FIFO) order within each priority level. If you need greater control of task ordering within a priority level, such as preventing large tenants from overwhelming small tenants, check out [the Fairness section](#task-queue-fairness).

You can set a Workflow's priority key via the CLI like so:

```
temporal workflow start \
  --type ChargeCustomer \
  --task-queue my-task-queue \
  --workflow-id my-workflow-id \
  --input '{"customerId":"12345"}' \
  --priority-key 1
```

You can set priority keys for a Workflow within the SDK like so:

<SdkTabs>
<SdkTabs.Go>
```go
workflowOptions := client.StartWorkflowOptions{
  ID:        "my-workflow-id",
  TaskQueue: "my-task-queue",
  Priority:  temporal.Priority{PriorityKey: 5},
}
we, err := c.ExecuteWorkflow(context.Background(), workflowOptions, MyWorkflow)
```
</SdkTabs.Go>
<SdkTabs.Java>
```java
WorkflowOptions options = WorkflowOptions.newBuilder()
  .setTaskQueue("my-task-queue")
  .setPriority(Priority.newBuilder().setPriorityKey(5).build())
  .build();

WorkflowClient client = WorkflowClient.newInstance(service); MyWorkflow workflow =
client.newWorkflowStub(MyWorkflow.class, options); workflow.run();

````
</SdkTabs.Java>
<SdkTabs.Python>
```python
await client.start_workflow(
  MyWorkflow.run,
  args="hello",
  id="my-workflow-id",
  task_queue="my-task-queue",
  priority=Priority(priority_key=1),
)
````

</SdkTabs.Python>
<SdkTabs.DotNet>
```csharp
var handle = await Client.StartWorkflowAsync(
  (MyWorkflow wf) => wf.RunAsync("hello"),
  new StartWorkflowOptions(
    id: "my-workflow-id",
    taskQueue: "my-task-queue"
  )
  {
    Priority = new Priority(1),
  }
);
```
</SdkTabs.DotNet>
</SdkTabs>

You can set priority keys for an Activity within the SDK like so:

<SdkTabs>
<SdkTabs.Go>
```go
ao := workflow.ActivityOptions{
  StartToCloseTimeout: time.Minute,
  Priority:            temporal.Priority{PriorityKey: 3},
}
ctx := workflow.WithActivityOptions(ctx, ao)
err := workflow.ExecuteActivity(ctx, MyActivity).Get(ctx, nil)
```
</SdkTabs.Go>
<SdkTabs.Java>
```java
ActivityOptions options = ActivityOptions.newBuilder()
  .setStartToCloseTimeout(Duration.ofMinutes(1))
  .setPriority(Priority.newBuilder().setPriorityKey(3).build())
  .build();

MyActivity activity = Workflow.newActivityStub(MyActivity.class, options); activity.perform();

````
</SdkTabs.Java>
<SdkTabs.Python>
```python
await workflow.execute_activity(
  say_hello,
  "hi",
  priority=Priority(priority_key=3),
  start_to_close_timeout=timedelta(seconds=5),
)
````

</SdkTabs.Python>
<SdkTabs.TypeScript>
</SdkTabs.TypeScript>
<SdkTabs.DotNet>
```csharp
await Workflow.ExecuteActivityAsync(
  () => SayHello("hi"),
    new()
    {
      StartToCloseTimeout = TimeSpan.FromSeconds(5),
      Priority = new(3),
    }
  );
```
</SdkTabs.DotNet>
</SdkTabs>

You can set priority keys for a Child Workflow within the SDK like so:

<SdkTabs>
<SdkTabs.Go>
```go
cwo := workflow.ChildWorkflowOptions{
  WorkflowID: "child-workflow-id",
  TaskQueue:  "child-task-queue",
  Priority:   temporal.Priority{PriorityKey: 1},
}
ctx := workflow.WithChildOptions(ctx, cwo)
err := workflow.ExecuteChildWorkflow(ctx, MyChildWorkflow).Get(ctx, nil)
```
</SdkTabs.Go>
<SdkTabs.Java>
```java
ChildWorkflowOptions childOptions = ChildWorkflowOptions.newBuilder()
  .setTaskQueue("child-task-queue")
  .setWorkflowId("child-workflow-id")
  .setPriority(Priority.newBuilder().setPriorityKey(1).build())
  .build();

MyChildWorkflow child = Workflow.newChildWorkflowStub(MyChildWorkflow.class, childOptions); child.run();

````
</SdkTabs.Java>
<SdkTabs.Python>
```python
await workflow.execute_child_workflow(
  MyChildWorkflow.run,
  args="hello child",
  priority=Priority(priority_key=1),
)
````

</SdkTabs.Python>
<SdkTabs.DotNet>
```csharp
await Workflow.ExecuteChildWorkflowAsync(
  (MyChildWorkflow wf) => wf.RunAsync("hello child"),
  new() { Priority = new(1) }
);
```
</SdkTabs.DotNet>
</SdkTabs>

## Task Queue Fairness

Task Queue Fairness lets you distribute Tasks based on _fairness keys_ and _fairness weights_ within a Task Queue.

Each fairness key creates its own "virtual queue", allowing you to organize Tasks into logical groups like tenants, applications, or workload types. These virtual queues operate using a round-robin dispatch mechanism, meaning the system cycles through each fairness key in turn when selecting the next Task to dispatch. This prevents any single fairness key from hogging Worker capacity, even if one key has a much larger backlog than the others.
