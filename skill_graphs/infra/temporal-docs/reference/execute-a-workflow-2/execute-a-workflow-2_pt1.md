# Execute a workflow
result = await client.execute_workflow(
    GreetingWorkflow.run,
    name,
    id="my-workflow",
    task_queue=TASK_QUEUE_NAME,
)
```

**Excerpt of code used to configure the Worker, referencing the constant
defined with the Task Queue name in Python**

```python
worker = Worker(
    client,
    task_queue=TASK_QUEUE_NAME,
    workflows=[GreetingWorkflow],
    activities=[activities.say_hello],
)
```

</TabItem>
<TabItem value="go" label="Go">

**Excerpt of code used to define a constant with the Task Queue name in Go**

```go
package app

const TaskQueueName = "my-taskqueue-name"
```

**Excerpt of code used to start the Workflow, referencing the constant defined with the Task Queue name in Go**

```go
options := client.StartWorkflowOptions{
    ID:        "my-workflow",
    TaskQueue: app.TaskQueueName,
}

run, err := c.ExecuteWorkflow(ctx, options, ProcessOrderWorkflow, input)
```

**Excerpt of code used to configure the Worker, referencing the constant defined with the Task Queue name in Go**

```go
w := worker.New(c, app.TaskQueueName, worker.Options{})
```

</TabItem>
<TabItem value="java" label="Java">

**Excerpt of code used to define a constant with the Task Queue name in Java**

```java
package app;

public class Constants {

  public static final String taskQueueName = "my-task-queue-name";

}
```

**Excerpt of code used to start the Workflow, referencing the constant defined with the Task Queue name in Java**

```java
WorkflowOptions options = WorkflowOptions.newBuilder()
        .setWorkflowId("my-workflow")
        .setTaskQueue(Constants.taskQueueName)
        .build();

MyWorkflow workflow = client.newWorkflowStub(MyWorkflow.class, options);
```

**Excerpt of code used to configure the Worker, referencing the constant defined with the Task Queue name in Java**

```java
Worker worker = factory.newWorker(Constants.taskQueueName);
```

</TabItem>
<TabItem value="typescript" label="Typescript">

**Excerpt of code used to define a constant with the Task Queue name in TypeScript**

```typescript
const TASK_QUEUE_NAME = 'my-taskqueue-name';
```

**Excerpt of code used to start the Workflow, referencing the constant defined with the Task Queue name in TypeScript**

```typescript

// additional code would follow

await client.workflow.start(OrderProcessingWorkflow, {
  args: [order],
  taskQueue: TASK_QUEUE_NAME,
  workflowId: `workflow-order-${order.id},`,
});
```

**Excerpt of code used to configure the Worker, referencing the constant defined with the Task Queue name in TypeScript**

```typescript

// additional code would follow

const worker = await Worker.create({
  taskQueue: TASK_QUEUE_NAME,
  connection,
  workflowsPath: require.resolve('./workflows'),
  activities,
});
```

</TabItem>
<TabItem value="dotnet" label=".NET">

**Excerpt of code used to define a constant with the Task Queue name in C# and .NET**

```csharp
public static class WorkflowConstants
{
    public const string TaskQueueName = "translation-tasks";
}
```

**Excerpt of code used to start the Workflow, referencing the constant defined with the Task Queue name in C# and .NET**

```csharp
var options = new WorkflowOptions(
            id: "translation-workflow",
            taskQueue: WorkflowConstants.TaskQueueName);

// Run workflow
var result = await client.ExecuteWorkflowAsync(
    (TranslationWorkflow wf) => wf.RunAsync(input),
    options);
```

**Excerpt of code used to configure the Worker, referencing the constant defined with the Task Queue name in C# and .NET**

```csharp
using var worker = new TemporalWorker(
    client,
    new TemporalWorkerOptions(WorkflowConstants.TaskQueueName)
    .AddAllActivities(activities)
    .AddWorkflow<TranslationWorkflow>());
```

</TabItem>

</Tabs>

However, it’s not always possible to do define the Task Queue name in a constant, such as when the Client used
to start the Workflow is running on another system or is implemented in a
different programming language.

---

## Task Queues

This page discusses [Task Queues](#task-queue) including [where to set Task Queues](#set-task-queue) and [Task Ordering](#task-ordering).

## What is a Task Queue? {/* #task-queue */}

A Task Queue is a lightweight, dynamically allocated queue that one or more [Worker Entities](/workers#worker-entity) poll for [Tasks](/tasks).
There are three types of Task Queues: Activity Task Queues, Workflow Task Queues, and Nexus Task Queues.

<CaptionedImage
    src="/diagrams/task-queue.svg"
    title="Task Queue component"
    />

A Nexus Endpoint creates an entry point that separates callers from the underlying Nexus Task Queue.
The Nexus callers only interact with the Nexus Endpoint.
This endpoint routes Nexus Requests to a target Task Queue that's polled by a Nexus Worker.

<CaptionedImage
    src="/img/encyclopedia/workers/nexus-task-queue.png"
    title="Nexus Endpoint component"
    />

Task Queues are lightweight components that don’t require explicit registration.
They’re created on demand when a Workflow Execution, Activity, or Nexus Operation is invoked, and/or when a Worker Process subscribes to start polling.
When a named Task Queue is created, individual Task Queues for Workflows, Activities, and Nexus are created using the same name.
A Temporal Application can use, and the Temporal Service can maintain, an unlimited number of Task Queues.

Workers poll for Tasks in Task Queues via synchronous RPC.
This implementation offers several benefits:

- A Worker Process polls for a message only when it has spare capacity, avoiding overloading itself.
- In effect, Task Queues enable load balancing across many Worker Processes.
- Task Queues enable [Task Routing](/task-routing), which is the routing of specific Tasks to specific Worker Processes or even a specific process.
- Activity Task Queues support server-side throttling, which enables you to limit the Task dispatching rate to the pool of Worker Processes while still supporting Task dispatching at higher rates when spikes happen.
- Workflow and Activity Tasks persist in a Task Queue.
  When a Worker Process goes down, the messages remain until the Worker recovers and can process the Tasks.
- Nexus and Query Tasks are not persisted.
  Instead, they are sync matched when, and only when, polled by a Worker.
  Sync matching immediately matches and delivers a Task to an available Worker without persisting a Task to the Service database.
  The caller is responsible to retry failed operations.
  Caller Workflows that invoke Nexus Operations will automatically retry Nexus Tasks until exceeding the Schedule-to-Close timeout.
- Worker Processes do not need to advertise themselves through DNS or any other network discovery mechanism.
- Worker Processes connect directly to the Temporal Service for secure communication without needing to open exposed ports.

Any Worker can pick up any Task on a given Task Queue.
You must ensure that if a Worker accepts a Task that it can process that task using one of its registered Workflows, Activities, or Nexus Operation handlers.
This means that all Workers listening to a Task Queue must register all Workflows, Activities, and Nexus Operations that live on that Queue.

There are two exceptions to this "Task Queue Workers with identical registrations" rule.
First, Worker Versioning may be used.
During Worker upgrade binary rollouts, it's okay to have temporarily misaligned registrations.
Second, dynamic Workflows or Activity components may be used.
If a Task arrives with a recognized method signature, the Worker can use a pre-registered dynamic stand-in.

When Workers don't have a registered Workflow, Activity, Nexus Operation, or dynamic Workflow or Activity component for a given Task, the Task will fail with a "Not Found" error.

- "Not Found" Workflow Tasks and Activity Tasks are treated as _retryable_ errors.
- "Not Found" Nexus Operation handlers are _non-retryable_ and must be manually retried from the caller Workflow.

#### Where to set Task Queues {/* #set-task-queue */}

There are five places where the name of the Task Queue can be set by the developer.

1. A Task Queue must be set when spawning a Workflow Execution:

   - [How to start a Workflow Execution using the Temporal CLI](/cli/command-reference/workflow#start)
   - [How to start a Workflow Execution using the Go SDK](/develop/go/client/temporal-client#start-workflow-execution)
   - [How to start a Workflow Execution using the Java SDK](/develop/java/client/temporal-client#start-workflow-execution)
   - [How to start a Workflow Execution using the PHP SDK](/develop/php/client/temporal-client#start-workflow-execution)
   - [How to start a Workflow Execution using the Python SDK](/develop/python/client/temporal-client#start-workflow-execution)
   - [How to start a Workflow Execution using the TypeScript SDK](/develop/typescript/client/temporal-client#start-workflow-execution)
   - [How to start a Workflow Execution using the .NET SDK](/develop/dotnet/client/temporal-client#start-workflow)

2. A Task Queue name must be set when creating a Worker Entity and when running a Worker Process:

   - [How to run a development Worker using the Go SDK](/develop/go/workers/run-worker-process)
   - [How to run a development Worker using the Java SDK](/develop/java/workers/run-worker-process)
   - [How to run a development Worker using the PHP SDK](/develop/php/workers/run-worker-process#run-a-dev-worker)
   - [How to run a development Worker using the Python SDK](/develop/python/workers/run-worker-process#run-a-dev-worker)
   - [How to run a development Worker using the TypeScript SDK](/develop/typescript/workers/run-worker-process#run-a-dev-worker)
   - [How to run a development Worker using the .NET SDK](/develop/dotnet/workers/run-worker-process)
   - [How to connect a Go SDK Worker to Temporal Cloud](/develop/go/workers/run-worker-process#connect-to-temporal-cloud)
   - [How to run a Temporal Cloud Worker using the TypeScript SDK](/develop/typescript/workers/run-worker-process#run-a-temporal-cloud-worker)

   Note that all Worker Entities listening to the same Task Queue name must be registered to handle the exact same Workflows Types, Activity Types, and Nexus Operations.

   If a Worker Entity polls a Task for a Workflow Type or Activity Type it does not know about, it will fail that Task.
   However, the failure of the Task will not cause the associated Workflow Execution to fail.

3. A Task Queue name can be provided when spawning an Activity Execution:

   This is optional.
   An Activity Execution inherits the Task Queue name from its Workflow Execution if one is not provided.

   - [How to start an Activity Execution using the Go SDK](/develop/go/activities/execution)
   - [How to start an Activity Execution using the Java SDK](/develop/java/activities/execution)
   - [How to start an Activity Execution using the PHP SDK](/develop/php/activities/execution)
   - [How to start an Activity Execution using the Python SDK](/develop/python/activities/execution)
   - [How to start an Activity Execution using the TypeScript SDK](/develop/typescript/activities/execution)
   - [How to start an Activity Execution using the .NET SDK](/develop/dotnet/activities/execution)

4. A Task Queue name can be provided when spawning a Child Workflow Execution:

   This is optional.
   A Child Workflow Execution inherits the Task Queue name from its Parent Workflow Execution if one is not provided.

   - [How to start a Child Workflow Execution using the Go SDK](/develop/go/workflows/child-workflows)
   - [How to start a Child Workflow Execution using the Java SDK](/develop/java/workflows/child-workflows)
   - [How to start a Child Workflow Execution using the PHP SDK](/develop/php/workflows/continue-as-new)
   - [How to start a Child Workflow Execution using the Python SDK](/develop/python/workflows/child-workflows)
   - [How to start a Child Workflow Execution using the TypeScript SDK](/develop/typescript/workflows/child-workflows)
   - [How to start a Child Workflow Execution using the .NET SDK](/develop/dotnet/workflows/child-workflows)

5. A Task Queue name can be provided when creating a Nexus Endpoint.
   Nexus Endpoints route requests to the target Task Queue.
   Nexus Workers poll the target Task Queue to handle the Nexus Tasks, such as starting or cancelling a Nexus Operation.

   - [How to run a Nexus Worker using the Go SDK](/develop/go/nexus/feature-guide#register-a-nexus-service-in-a-worker)
   - [How to run a Nexus Worker using the Java SDK](/develop/java/nexus/feature-guide#register-a-nexus-service-in-a-worker)

#### Task ordering

Task Queues can be scaled by adding partitions.
By [default](/references/dynamic-configuration#service-level-rps-limits) each Task Queue has 4 partitions.

Task Queues with a single partition are almost always first-in, first-out, with rare edge case exceptions.
However, using a single partition limits you to low- and medium-throughput use cases.

In Task Queues with multiple partitions, each task is assigned to a random partition.
Generally partitions will act as FIFO queues, so once a task queue builds up a backlog, the sync match (tasks that can be dispatched immediately) rate will drop to nearly zero because the task queue will instead dispatch tasks from the backlog (i.e. async matches) first.

:::note

This section is on the ordering of individual Tasks, and does not apply to the ordering of Workflow Executions, Activity Executions, or [Events](/workflow-execution/event#event) in a single Workflow Execution.
The order of Events in a Workflow Execution is guaranteed to remain constant once they have been written to that Workflow Execution's [History](/workflow-execution/event#event-history).

:::

---

## Task Routing and Worker sessions

This page discusses the following:

- [Task Routing](#task-routing)
- [Worker Sessions](#worker-session)

## What is Task Routing? {/* #task-routing */}

Task Routing is simply when a Task Queue is paired with one or more Workers, primarily for Activity Task Executions.

This could also mean employing multiple Task Queues, each one paired with a Worker Process.

Task Routing has many applicable use cases.

Some SDKs provide a [Session API](#worker-session) that provides a straightforward way to ensure that Activity Tasks are executed with the same Worker without requiring you to manually specify Task Queue names.
It also includes features like concurrent session limitations and worker failure detection.

### Flow control

A Worker that consumes from a Task Queue asks for an Activity Task only when it has available capacity, so it is never overloaded by request spikes.
If Activity Tasks get created faster than Workers can process them, they are backlogged in the Task Queue.

### Throttling

The rate at which each Activity Worker polls for and processes Activity Tasks is configurable per Worker.
Workers do not exceed this rate even if it has spare capacity.
There is also support for global Task Queue rate limiting.
This limit works across all Workers for the given Task Queue.
It is frequently used to limit load on a downstream service that an Activity calls into.

### Specific environments

In some cases, you might need to execute Activities in a dedicated environment.
To send Activity Tasks to this environment, use a dedicated Task Queue.

#### Route Activity Tasks to a specific host

In some use cases, such as file processing or machine learning model training, an Activity Task must be routed to a specific Worker Process or Worker Entity.

For example, suppose that you have a Workflow with the following three separate Activities:

- Download a file.
- Process the file in some way.
- Upload a file to another location.

The first Activity, to download the file, could occur on any Worker on any host.
However, the second and third Activities must be executed by a Worker on the same host where the first Activity downloaded the file.

In a real-life scenario, you might have many Worker Processes scaled over many hosts.
You would need to develop your Temporal Application to route Tasks to specific Worker Processes when needed.

Code samples:

- [Go file processing example](https://github.com/temporalio/samples-go/tree/main/fileprocessing)
- [Java file processing example](https://github.com/temporalio/samples-java/tree/main/core/src/main/java/io/temporal/samples/fileprocessing)
- [PHP file processing example](https://github.com/temporalio/samples-php/tree/master/app/src/FileProcessing)

#### Route Activity Tasks to a specific process

Some Activities load large datasets and cache them in the process.
The Activities that rely on those datasets should be routed to the same process.

In this case, a unique Task Queue would exist for each Worker Process involved.

#### Workers with different capabilities

Some Workers might exist on GPU boxes versus non-GPU boxes.
In this case, each type of box would have its own Task Queue and a Workflow can pick one to send Activity Tasks.

### Multiple priorities

If your use case involves more than one priority, you can create one Task Queue per priority, with a Worker pool per priority.

Alternatively, you can use [Task Queue Priority](/develop/task-queue-priority-fairness), which lets you assign priority levels to Tasks within a single Task Queue.
This approach avoids the overhead of managing multiple Task Queues and separate Worker pools while still ensuring higher-priority Tasks are processed first.

### Versioning

Task Routing is the simplest way to version your code.

If you have a new backward-incompatible Activity Definition, start by using a different Task Queue.

Alternatively, you can use [Worker Versioning](/worker-versioning), which lets you tag Workers with a version and route Workflow and Activity Tasks to specific versions without requiring separate Task Queues.
Worker Versioning supports both Pinned Workflows (which complete on a single Worker Deployment Version) and Auto-Upgrade Workflows (which automatically move to the latest version).

## What is a Worker Session? {/* #worker-session */}

A Worker Session is a feature provided by some SDKs that provides a straightforward API for [Task Routing](#task-routing) to ensure that Activity Tasks are executed with the same Worker without requiring you to manually specify Task Queue names.
It also includes features like concurrent session limitations and Worker failure detection.

- [How to use Worker Sessions](/develop/go/workers/sessions)

---

## Tasks

This page discusses the following:

- [Task](#task)
- [Workflow Task](#workflow-task)
  - [When are Workflow Tasks scheduled?](#when-workflow-tasks-scheduled)
  - [How does a Worker process a Workflow Task?](#how-worker-processes-workflow-task)
  - [How does the SDK know which code to run?](#how-worker-processes-workflow-task)
  - [Workflow Tasks and Determinism](#workflow-task-failures-vs-execution-failures)
  - [Performance characteristics](#workflow-task-execution)
- [Workflow Task Execution](#workflow-task-execution)
- [Workflow Task Failures vs Workflow Execution Failures](#workflow-task-failures-vs-execution-failures)
- [Activity Task](#activity-task)
- [Activity Task Execution](#activity-task-execution)
- [Nexus Task](#nexus-task)
- [Nexus Task Execution](#nexus-task-execution)

## What is a Task? {/* #task */}

A Task is a unit of work for [Workers](/workers). The Temporal Service places Tasks on [Task Queues](/task-queue), and
Workers poll for and process them to advance [Workflows](/workflows), run [Activity](/activities) attempts, or handle
[Nexus](/nexus) requests.

There are three types of Tasks:

- [Workflow Task](#workflow-task)
- [Activity Task](#activity-task)
- [Nexus Task](#nexus-task)

## What is a Workflow Task? {/* #workflow-task */}

A Workflow Task advances a [Workflow Execution](/workflow-execution) by one step.

### When are Workflow Tasks scheduled? {/* #when-workflow-tasks-scheduled */}

The Temporal Service creates and schedules a new Workflow Task whenever one of the following occurs:

- The Workflow Execution is started
- A Signal is sent to the Workflow
- An Update is sent to the Workflow
- An Activity completes (successfully or with a failure)
- A Timer fires
- A Child Workflow completes
- A Workflow Task fails and needs to be retried

Any event that might affect the Workflow's state triggers a new Workflow Task. The Workflow Task bundles together all
new events that have occurred since the last Workflow Task completed.

### How does a Worker process a Workflow Task? {/* #how-worker-processes-workflow-task */}

When a Worker picks up a Workflow Task, it replays the entire Workflow Execution from the beginning using the Event
History.

- The Worker receives the Workflow Task, which contains the complete Event History for the Workflow Execution
- The Workflow Worker replays the Workflow code from the start, using the Event History to recreate the Workflow's state
- During replay, previously executed operations (like Activity calls or Timers) return their results immediately from
  the Event History instead of executing again
- The replay continues until the Worker reaches a point where it needs to make new progress (a new Activity to schedule,
  a new Timer to set, etc.)
- The Workflow code executes any new decisions and generates Commands
- The Worker sends these Commands back to the Temporal Service, completing the Workflow Task
- The Temporal Service persists the Commands as new Events in the Event History

This replay mechanism makes Temporal Workflows durable and fault-tolerant. If a Worker crashes mid-execution, another
Worker can pick up the Workflow Task and replay the entire history to reconstruct the exact state before continuing

### What is a Workflow Task Execution? {/* #workflow-task-execution */}

A Workflow Task Execution occurs when a [Worker](/workers#worker-entity) picks up a [Workflow Task](#workflow-task) and
uses it to make progress on the execution of a [Workflow Definition](/workflow-definition) (also known as a Workflow
function).

Workflow Task Execution is typically very fast (milliseconds). The Worker replays code and makes decisions based on the
Event History. No actual I/O operations occur during replay (Activity results come from history). The time spent in a
Workflow Task is unrelated to how long Activities or Timers take.

## Workflow Task Failures vs Workflow Execution Failures {/* #workflow-task-failures-vs-execution-failures */}

Understanding the difference between Workflow Task failures and Workflow Execution failures is essential to working with
Temporal at a deeper level.

**Workflow Task failure** means a Worker can't successfully process a Workflow Task due to infrastructure, Workflow
code, or execution environment issues (not business logic). Common causes include non-determinism, unhandled exceptions,
task timeouts, invalid Commands, or bad binary checksums. The Service automatically retries the task with exponential
backoff, and the Workflow Execution stays Open until a task completes, an operator terminates it, or the Workflow
Execution Timeout is reached. Fixes typically involve correcting code, scaling Workers, or resolving infrastructure
problems.

**Workflow Execution failure** means the Workflow's business logic determines it can't complete. It occurs when Workflow
code throws or returns an error, an Activity failure propagates uncaught, or an external system terminates/cancels the
Workflow. The Workflow closes with a Failed status and does not automatically retry; if a Retry Policy is configured,
the Service starts a new Run with the same Workflow ID and continues retrying until success or exhaustion. Each retry is
a separate Run with its own Event History.

The table summarizes the differences:

| Aspect              | Workflow Task Failure                                  | Workflow Execution Failure                                  |
| ------------------- | ------------------------------------------------------ | ----------------------------------------------------------- |
| **What failed**     | Infrastructure or Workflow code has a bug              | Business logic determined the Workflow cannot succeed       |
| **Workflow state**  | Workflow Execution remains Open                        | Workflow Execution closes (Failed, Terminated, etc.)        |
| **Automatic retry** | Always retried automatically by the Service            | Only retried if a Workflow Retry Policy is configured       |
| **Event History**   | Same Event History continues to grow                   | Each retry run has a separate Event History                 |
| **How to resolve**  | Fix code/infrastructure and redeploy                   | May require business logic changes or external intervention |
| **Visibility**      | Shows as Workflow Task failures in history and metrics | Shows as a Failed Workflow Execution in the UI              |

**Workflow Task failure example:** A new deployment introduces non-determinism, existing Workflows fail Workflow Tasks,
and the executions stay Open and retry. After deploying a fix, the Workflows automatically continue.

**Workflow Execution failure example:** A payment Activity fails due to a declined card, the failure propagates
uncaught, and the Workflow closes as Failed. The customer updates payment details and restarts the order.

## What is an Activity Task? {/* #activity-task */}

An Activity Task runs one attempt of an [Activity](/activities).

### What is an Activity Task Execution? {/* #activity-task-execution */}

An Activity Task Execution occurs when a [Worker](/workers#worker-entity) uses the context provided from the
