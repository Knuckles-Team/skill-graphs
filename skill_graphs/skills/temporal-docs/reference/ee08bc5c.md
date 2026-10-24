1. The first task is included in the server response, no matching step required.
1. The SDK extracts the task from the response, and dispatches it to the local worker.

To recover from errors, Eager Workflow Start falls back to the non-eager path. For example, when the first Task is returned eagerly, but the local Worker fails or times out while processing the task, the server retries this task non-eagerly after WorkflowTaskTimeout.

## Visualize Workers in the UI {/* #visualize-workers */}

The Temporal SDK includes a heartbeat for Worker processes that is sent to the Server, carrying information such as available task slots, CPU usage, and Worker configuration.
The Server exposes this data through APIs that surface Worker details in the Temporal UI. See a list of all running Workers by selecting Workers in the left navigation menu.
View the list of Workers assigned to the Workflow Task Queue and inspect Worker details to troubleshoot Workflows with delayed processing by selecting the Workers tab in the Workflow details page.

This feature requires Temporal Server 1.30 or higher with API version 1.62 or higher, and is also available in Temporal Cloud.
Worker Heartbeating is required; see [Manage Worker Heartbeating](/cloud/worker-health#manage-worker-heartbeating) for the minimum SDK versions.

## Performance metrics for tuning {/* #metrics */}

The Temporal SDKs emit metrics from Temporal Client usage and Worker Processes.
Performance tuning uses three important SDK metric groups:

### Slot availability metrics

Temporal's [`worker_task_slots_available`](/references/sdk-metrics#worker_task_slots_available) and `worker_task_slots_used` gauges can report the number of available executor “slots” that are currently available and unoccupied for a Worker type.
Tag these with `worker_type=WorkflowWorker` for Workflow Task Workers or `worker_type=ActivityWorker` for Activity Workers.

:::tip

Unlike `worker_task_slots_used`, `worker_task_slots_available` can only be used with fixed size slot suppliers and can't be used with resource-based slot suppliers.

:::

### Latency metrics

Temporal provides two latency timers: [`workflow_task_schedule_to_start_latency`](/references/sdk-metrics#workflow_task_schedule_to_start_latency) for Workflow Tasks and [`activity_schedule_to_start_latency`](/references/sdk-metrics#activity_schedule_to_start_latency) for Activities.
A Schedule-To-Start latency is the time from when an Task is scheduled (that is, placed in a Queue) to when a Worker starts (that is, picks up from the Task Queue) that Task.
These metrics help ensure that Tasks are being processed from the queue in a timely manner.
For more information about `schedule_to_start` timeout and latency, see [Schedule-To-Start Timeout](/encyclopedia/detecting-activity-failures#schedule-to-start-timeout).

### Cache metrics

The [`sticky_cache_size`](/references/sdk-metrics#sticky_cache_size) and [`workflow_active_thread_count`](/references/sdk-metrics#workflow_active_thread_count) metrics report the size of the Workflow cache and the number of cached Workflow threads.

## Worker performance options {/* #configuration */}

Each Worker can be configured by providing custom Worker options (`WorkerOptions`) at instantiation.
Options are specific to individual Workers and do not affect other members of your fleet.

### Executor slot options

The `maxConcurrentWorkflowTaskExecutionSize` and `maxConcurrentActivityExecutionSize` options define the number of total available Workflow Task and Activity Task slots for a Worker.

:::caution

- Worker tuners supersede the existing `maxConcurrentXXXTask` style Worker options.
  Using both styles will cause an error at Worker initialization time.

:::

### Configuring Poller Options

#### Recommended Approach

The Temporal SDKs support Poller Autoscaling, which automatically selects an appropriate number of pollers based on need. Using this feature results in more efficient poller usage, better throughput, and schedule-to-start latency improvements. You can enable this feature by setting the `*_task_poller_behavior` options to `PollerBehaviorAutoscaling`. Names may vary slightly depending on the SDK. For specific examples of enabling Poller Autoscaling, see the SDK Examples section below. Poller Autoscaling will be the default configuration in future versions of Temporal SDKs.

:::tip

`PollerBehaviorAutoscaling` is only enabled in Temporal Server v1.28.0 and later.

:::

#### Manual Configuration

There are options available to manually configure minimum, maximum, and initial poller counts, but it is not recommended to set these values manually for production use cases. To set these values manually, the following options are available:

- `maxConcurrentWorkflowTaskPollers` (in the JavaSDK: `workflowPollThreadCount`)
- `maxConcurrentActivityTaskPollers` (in the JavaSDK: `activityPollThreadCount`)

These options define the maximum count of pollers performing poll requests on Workflow and Activity Task Queues, respectively.

#### SDK Examples

<SdkTabs>
<SdkTabs.Go>
[Go SDK docs](https://pkg.go.dev/go.temporal.io/sdk/worker#PollerBehaviorAutoscalingOptions)
```go
w := worker.New(c, "my-task-queue", worker.Options{
  WorkflowTaskPollerBehavior: worker.NewPollerBehaviorAutoscaling(worker.PollerBehaviorAutoscalingOptions{}),
  ActivityTaskPollerBehavior: worker.NewPollerBehaviorAutoscaling(worker.PollerBehaviorAutoscalingOptions{}),
  NexusTaskPollerBehavior: worker.NewPollerBehaviorAutoscaling(worker.PollerBehaviorAutoscalingOptions{}),
})
```
</SdkTabs.Go>
<SdkTabs.Java>
[Java SDK docs](https://javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/worker/tuning/PollerBehaviorAutoscaling.html)
```java
public class WorkerExample {
    public static void main(String[] args) {
        WorkflowServiceStubs service = WorkflowServiceStubs.newLocalServiceStubs();
        WorkflowClient client = WorkflowClient.newInstance(service);
        WorkerFactory factory = WorkerFactory.newInstance(client);
        WorkerOptions workerOptions = WorkerOptions.newBuilder()
            .setWorkflowTaskPollersBehavior(new PollerBehaviorAutoscaling())
            .setActivityTaskPollersBehavior(new PollerBehaviorAutoscaling())
            .setNexusTaskPollersBehavior(new PollerBehaviorAutoscaling())
            .build();

        Worker worker = factory.newWorker("my-task-queue", workerOptions);
    }
}
```
</SdkTabs.Java>
<SdkTabs.Python>
[Python SDK docs](https://python.temporal.io/temporalio.worker.PollerBehaviorAutoscaling.html)
```python
worker = Worker(
    client,
    task_queue="my-task-queue",
    workflows=[MyWorkflow],
    activities=[my_activity],

    workflow_task_poller_behavior=PollerBehaviorAutoscaling(),
    activity_task_poller_behavior=PollerBehaviorAutoscaling(),
    nexus_task_poller_behavior=PollerBehaviorAutoscaling(),
)
```
</SdkTabs.Python>
<SdkTabs.TypeScript>
[TypeScript SDK docs](https://typescript.temporal.io/api/interfaces/proto.temporal.api.sdk.v1.WorkerConfig.IAutoscalingPollerBehavior)
```ts
const worker = await Worker.create({
  connection,
  taskQueue: 'my-task-queue',
  workflowsPath: require.resolve('./workflows'),
  activities,

  workflowTaskPollerBehavior: PollerBehavior.autoscaling(),
  activityTaskPollerBehavior: PollerBehavior.autoscaling(),
  nexusTaskPollerBehavior: PollerBehavior.autoscaling(),
});
```
</SdkTabs.TypeScript>
<SdkTabs.DotNet>
[DotNet SDK docs](https://dotnet.temporal.io/api/Temporalio.Worker.Tuning.PollerBehavior.Autoscaling.html)
```csharp
using var worker = new TemporalWorker(
    client,
    new TemporalWorkerOptions("my-task-queue")
    {
        WorkflowTaskPollerBehavior = new PollerBehavior.Autoscaling(),
        ActivityTaskPollerBehavior = new PollerBehavior.Autoscaling(),
        NexusTaskPollerBehavior = new PollerBehavior.Autoscaling(),
    }
    .AddWorkflow<MyWorkflow>()
    .AddActivity(MyActivities.MyActivity)
);
```
</SdkTabs.DotNet>
<SdkTabs.Ruby>
[Ruby SDK docs](https://ruby.temporal.io/Temporalio/Worker/PollerBehavior/Autoscaling.html)
```ruby
worker = Temporalio::Worker.new(
  client,
  'my-task-queue',
  workflows: [MyWorkflow],
  activities: [MyActivity],

  workflow_task_poller_behavior: Temporalio::Worker::PollerBehavior::Autoscaling.new,
  activity_task_poller_behavior: Temporalio::Worker::PollerBehavior::Autoscaling.new,
  nexus_task_poller_behavior: Temporalio::Worker::PollerBehavior::Autoscaling.new,
)

```

</SdkTabs.Ruby>
</SdkTabs>

### Cache options (Java SDK) {/* #cache-options */}

A Workflow Cache is created and shared between all Workers on a single host.
It's designed to limit the resources used by the cache for each host/process.
These options are defined on `WorkerFactoryOptions`:

- `WorkerFactoryOptions#workflowCacheSize` defines the maximum number of cached Workflow Executions.
  Each cached Workflow contains at least one Workflow thread and its resources (memory, etc.).
- `maxWorkflowThreadCount` defines the maximum number of Workflow threads that may exist concurrently at any time.

These cache options limit the resource consumption of the in-memory Workflow cache.
Workflow cache options are shared between all Workers because the Workflow cache is tightly integrated with the resource consumption of the entire host.
This includes memory and the total thread count, which should be limited per host/JVM.

For Go, use [`SetStickyWorkflowCacheSize`](https://pkg.go.dev/go.temporal.io/sdk/worker#SetStickyWorkflowCacheSize). For Python, use the `max_cached_workflows` Worker option.

### "Large value" drawbacks

There are drawbacks when you use "large values everywhere."
As with any multithreading system, specifying excessively large values without monitoring with the SDK and system metrics leads to constant resource contention/stealing
This decreases the total throughput and increases latency jitter of the system.

### Invariants (JavaSDK only) {/* #invariants */}

These properties should always be true for a Worker's configuration.

Perform this sanity check after the adjustments to Worker settings.

1. `workflowCacheSize` should be ≤ `maxWorkflowThreadCount`. Each Workflow has at least one Workflow thread.
2. `maxConcurrentWorkflowTaskExecutionSize` should be ≤ `maxWorkflowThreadCount`. Having more Worker slots than the Workflow cache size will lead to resource contention/stealing between executors and unpredictable delays. It's recommended that `maxWorkflowThreadCount` be at least 2x of `maxConcurrentWorkflowTaskExecutionSize`.
3. `maxConcurrentWorkflowTaskPollers` should be significantly ≤ `maxConcurrentWorkflowTaskExecutionSize`. And `maxConcurrentActivityTaskPollers` should be significantly ≤ `maxConcurrentActivityExecutionSize`. The number of pollers should always be lower than the number of executors.

## Worker runtime performance tuning {/* #worker-performance-tuning */}

Worker tuning manages the assignment of slot suppliers.
A **Worker Tuner** instance exists per-Worker, providing slot suppliers for different slot types (Activity, Workflow, Nexus, or Local Activity Tasks).
A tuner assigns different suppliers to each slot type.
For example, it might provide a fixed assignment slot supplier for Workflows and use a resource-based supplier for Activities.

### Choosing slot supplier types {/* #choosing-slot-supplier-types */}

Temporal offers three types of slot suppliers: fixed assignment, resource-based, and custom.
**For most workloads, Temporal recommends fixed-size slot suppliers.**
A fixed-size tuner with appropriately chosen values delivers better performance and more predictable behavior than a resource-based tuner.

Each SDK provides [default slot counts](/develop/worker-tuning-reference#compute-defaults-by-sdk), but Temporal recommends [actively tuning these values](/best-practices/worker#actively-tune-worker-options-instead-of-relying-on-defaults) for your workload.

#### When to use resource-based slot suppliers

Resource-based slot suppliers are suited to specific use cases.

- **Fluctuating workloads with low per-Task consumption**:
  The resource-based supplier works well when each Task consumes few resources but may run for a (relatively) long time.
  For example: HTTP calls or other blocking I/Os that spend most of their time waiting on external events.
- **Protection from out-of-memory & over-subscription in the face of unpredictable per-task consumption:**
  Do your Tasks often consume an unpredictable number of resources?
  Do you want to avoid crashes without setting an overly-conservative fixed limit?
  In these cases, the resource-based supplier is a good match.
  Keep in mind that auto-tuning can never do a _perfect_ job and may sometimes exceed your requested system limits for CPU and memory.

Scenarios with tasks that have variable, or very high, per-task resource needs should rely on fixed-size suppliers and manual tuning rather than resource-based suppliers.

#### When to use custom slot suppliers

For the highest level of control over slot allocation, consider custom slot suppliers.
Custom suppliers let you tailor the logic of how slots are allocated based on your system requirements, providing flexibility to optimize for specific use cases that fixed assignment and resource-based suppliers do not fully address.

### Implement Custom Slot Suppliers {/* #custom-slot-implementation */}

Implement your own Slot Supplier to control how Workers are allocated Tasks and manage the processing of Workflows, Activities, and Nexus Operations.
Custom Slot Suppliers let you fine-tune task processing based on your application's needs.

Each SDK's reference documentation explains the specifics of the interface, but the core concepts are consistent across SDKs:

| Language                                               | Slot Supplier Reference                                                                                                  |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
|      | [`SlotSupplier`](https://pkg.go.dev/go.temporal.io/sdk/worker#SlotSupplier)                                              |
|        | [`SlotSupplier`](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/worker/tuning/SlotSupplier.html) |
|      | [`CustomSlotSupplier`](https://python.temporal.io/temporalio.worker.CustomSlotSupplier.html)                             |
|  | [`CustomSlotSupplier`](https://typescript.temporal.io/api/interfaces/worker.CustomSlotSupplier)                          |
|      | [`CustomSlotSupplier`](https://dotnet.temporal.io/api/Temporalio.Worker.Tuning.CustomSlotSupplier.html)                  |

Slot Suppliers issue `SlotPermit`s.
These represent the right to use a slot of a specific type, namely Workflow, Activity, Local Activity, or Nexus.
You control whether a Worker can perform certain tasks by issuing or withholding permits.

Custom Slot Suppliers must implement these functions:

- `reserveSlot` - Called before polling for new tasks. Your implementation can block and must return a Slot Permit once it decides to accept new work.
- `tryReserveSlot` - Called for slot reservations in cases like eager activity processing. This must not block.
- `markSlotUsed` - Called when a slot is about to be used for a task (not while it’s held during polling). It provides information about the task.
- `releaseSlot` - Called when a slot is no longer needed, whether or not it was used.

Custom policies require more effort, but provide finer control over Task processing.
By implementing your own Slot Supplier, you can tailor how Workflows, Activities, and Nexus Operations are handled, optimizing performance for your specific needs.

### Slot supplier throttles

Auto-tuned suppliers may diverge from requested thresholds.
The resources a given Task will use can't be known ahead of time.
There is a fundamental tradeoff between how quickly a slot supplier is willing to accept Tasks and how well it can respect the defined thresholds.

Slot throttling is a mechanism to control the rate at which new slots for concurrent tasks are made available for processing.
This concept is part of the resource-based auto-tuning feature for Workers.
By waiting a brief period between making slots available, the Worker can assess how resource usage has changed since the last task began processing.

This throttle is called `rampThrottle` in the SDK options for resource-based slot suppliers.
It defines the minimum time the Worker will wait between handing out new slots after passing the minimum slots number.

**A higher `rampThrottle` trades off performance for safety.**

For example:

If a just-started worker were to have no throttle, and there was a backlog of Tasks, it might immediately accept 100 Tasks at once.
If each Task allocated 1GB of RAM, the Worker would likely run out of memory and crash.
The throttle enforces a wait before handing out new slots (after a minimum number of slots have been occupied) so you can measure newly consumed resources.

## Performance tuning examples {/* #examples */}

The following examples show how to create and provision composite Worker tuners and set other
performance related options.
Each tuner provides slot suppliers for various Task types.
These examples focus on Activities and Local Activities, since Workflow Tasks normally do not need resource-based tuning.

### Go SDK

**Resource-based tuner:**

<!--SNIPSTART go-resource-based-tuner-->
[features/snippets/worker_tuner/worker_tuner.go](https://github.com/temporalio/features/blob/main/features/snippets/worker_tuner/worker_tuner.go)
```go
func resourceBasedTuner() (worker.Options, error) {
	tuner, err := worker.NewResourceBasedTuner(worker.ResourceBasedTunerOptions{
		TargetMem:    0.8,
		TargetCpu:    0.9,
		InfoSupplier: sysinfo.SysInfoProvider(),
	})
	if err != nil {
		return worker.Options{}, err
	}
	return worker.Options{
		Tuner: tuner,
	}, nil
}

```
<!--SNIPEND-->

**Composite tuner:**

A composite tuner lets you mix different slot supplier strategies for each Task type.
For example, you can use fixed-size slot suppliers for Workflow and Nexus Tasks while using resource-based slot suppliers for Activity and Local Activity Tasks.

<!--SNIPSTART go-composite-tuner-->
[features/snippets/worker_tuner/worker_tuner.go](https://github.com/temporalio/features/blob/main/features/snippets/worker_tuner/worker_tuner.go)
```go
func compositeTuner() (worker.Options, error) {
	options := worker.DefaultResourceControllerOptions()
	options.MemTargetPercent = 0.8
	options.CpuTargetPercent = 0.9
	options.InfoSupplier = sysinfo.SysInfoProvider()
	controller := worker.NewResourceController(options)
	wfSS, err := worker.NewFixedSizeSlotSupplier(10)
	if err != nil {
		return worker.Options{}, err
	}

	actSS, err := worker.NewResourceBasedSlotSupplier(controller, worker.DefaultActivityResourceBasedSlotSupplierOptions())
	if err != nil {
		return worker.Options{}, err
	}
	laSS, err := worker.NewResourceBasedSlotSupplier(controller, worker.DefaultActivityResourceBasedSlotSupplierOptions())
	if err != nil {
		return worker.Options{}, err
	}
	nexusSS, err := worker.NewFixedSizeSlotSupplier(10)
	if err != nil {
		return worker.Options{}, err
	}

	compositeTuner, err := worker.NewCompositeTuner(worker.CompositeTunerOptions{
		WorkflowSlotSupplier:      wfSS,
		ActivitySlotSupplier:      actSS,
		LocalActivitySlotSupplier: laSS,
		NexusSlotSupplier:         nexusSS,
	})
	if err != nil {
		return worker.Options{}, err
	}
	return worker.Options{
		Tuner: compositeTuner,
	}, nil
}

```
<!--SNIPEND-->

### Java SDK

```java
// Just resource based
WorkerOptions.newBuilder()
    .setWorkerTuner(
        ResourceBasedTuner.newBuilder()
            .setControllerOptions(
                ResourceBasedControllerOptions.newBuilder(0.8, 0.9).build())
            .build())
    .build())
// Combining different types
SlotSupplier<WorkflowSlotInfo> workflowTaskSlotSupplier = new FixedSizeSlotSupplier<>(10);
SlotSupplier<ActivitySlotInfo> activityTaskSlotSupplier =
    ResourceBasedSlotSupplier.createForActivity(
        resourceController, ResourceBasedTuner.DEFAULT_ACTIVITY_SLOT_OPTIONS);
SlotSupplier<LocalActivitySlotInfo> localActivitySlotSupplier =
    ResourceBasedSlotSupplier.createForLocalActivity(
        resourceController, ResourceBasedTuner.DEFAULT_ACTIVITY_SLOT_OPTIONS);
SlotSupplier<NexusSlotInfo> nexusSlotSupplier = new FixedSizeSlotSupplier<>(10);

WorkerOptions.newBuilder()
    .setWorkerTuner(
        new CompositeTuner(
            workflowTaskSlotSupplier,
            activityTaskSlotSupplier,
            localActivitySlotSupplier,
            nexusSlotSupplier))
    .build();
```

### TypeScript SDK

```tsx
// Just resource based
const resourceBasedTunerOptions: ResourceBasedTunerOptions = {
  targetMemoryUsage: 0.8,
  targetCpuUsage: 0.9,
};
const workerOptions = {
  tuner: {
    tunerOptions: resourceBasedTunerOptions,
  },
};
// Combining different types
const resourceBasedTunerOptions: ResourceBasedTunerOptions = {
  targetMemoryUsage: 0.8,
  targetCpuUsage: 0.9,
};
const workerOptions = {
  tuner: {
    activityTaskSlotSupplier: {
      type: 'resource-based',
      tunerOptions: resourceBasedTunerOptions,
    },
    workflowTaskSlotSupplier: {
      type: 'fixed-size',
      numSlots: 10,
    },
    localActivityTaskSlotSupplier: {
      type: 'resource-based',
      tunerOptions: resourceBasedTunerOptions,
    },
  },
};
```

### Python SDK

```python
