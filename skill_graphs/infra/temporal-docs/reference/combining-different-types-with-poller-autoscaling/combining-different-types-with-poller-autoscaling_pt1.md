# Combining different types, with poller autoscaling
resource_based_options = ResourceBasedTunerConfig(0.8, 0.9)
tuner = WorkerTuner.create_composite(
    workflow_supplier=FixedSizeSlotSupplier(10),
    activity_supplier=ResourceBasedSlotSupplier(
        ResourceBasedSlotConfig(),
        resource_based_options,
    ),
    local_activity_supplier=ResourceBasedSlotSupplier(
        ResourceBasedSlotConfig(),
        resource_based_options,
    ),
)
worker = Worker(
    client,
    task_queue="foo",
    tuner=tuner,
    workflow_task_poller_behavior=PollerBehaviorAutoscaling(),
    activity_task_poller_behavior=PollerBehaviorAutoscaling()
)
```

### .NET C# SDK

```csharp
// Just resource based
var worker = new TemporalWorker(
    Client,
    new TemporalWorkerOptions("my-task-queue")
    {
        Tuner = WorkerTuner.CreateResourceBased(0.8, 0.9),
    });
// Combining different types
var resourceTunerOptions = new ResourceBasedTunerOptions(0.8, 0.9);
var worker = new TemporalWorker(
    Client,
    new TemporalWorkerOptions("my-task-queue")
    {
        Tuner = new WorkerTuner(
             new FixedSizeSlotSupplier(10),
             new ResourceBasedSlotSupplier(
                 new ResourceBasedSlotSupplierOptions(),
                 resourceTunerOptions),
             new ResourceBasedSlotSupplier(
                 new ResourceBasedSlotSupplierOptions(),
                 resourceTunerOptions)),
    });
```

## Workflow Cache Tuning

When the number of cached Workflow Executions reported by `sticky_cache_size` hits `workflowCacheSize` _or_ the number of threads reported by the `workflow_active_thread_count` metrics gauge hits `maxWorkflowThreadCount`, Workflow Executions will start to be evicted from the cache.
An evicted Workflow Execution will need to be replayed when it gets any action that may advance it.

If the Workflow Cache limits described above are hit, and Worker hosts have enough free RAM and are not close to reasonable thread limits, then you may choose to increase `workflowCacheSize` and `maxWorkflowThreadCount` limits to decrease the overall latency and cost of the Replays in the system.
If the opposite occurs, consider decreasing the limits.

:::note

In CoreSDK based SDKs, like TypeScript, this metric works differently and should be monitored and adjusted on a per Worker and Task Queue basis.

The `maxWorkflowThreadCount` and `workflow_active_thread_count` parameters are for the Java SDK only.

:::

## Available Task Queue information {/* #task-queue-metrics */}

:::info

The information listed in this section is readable using the `DescribeTaskQueueEnhanced` method in the [Go SDK](https://github.com/temporalio/sdk-go/blob/74320648ab0e4178b1fedde01672f9b5b9f6c898/client/client.go), with the [Temporal CLI](https://github.com/temporalio/cli/releases/tag/v1.1.0) `task-queue describe` command, and using `DescribeTaskQueue` through RPC.

:::

The Temporal Service reports information separately for each Task Queue type (not aggregated).
Use the following Task Queue properties to retrieve and evaluate information about Task Queue health and performance.
Available data include:

- [`ApproximateBacklogCount`](#ApproximateBacklogCountAndAge) and [`ApproximateBacklogAge`](#ApproximateBacklogCountAndAge)
- [`TasksAddRate`](#TasksAddRate-and-TasksDispatchRate) and [`TasksDispatchRate`](#TasksAddRate-and-TasksDispatchRate)
- [`BacklogIncreaseRate`](#BacklogIncreaseRate) (derived from [`TasksAddRate`](#TasksAddRate-and-TasksDispatchRate) and [`TasksDispatchRate`](#TasksAddRate-and-TasksDispatchRate))

### `ApproximateBacklogCount` and `ApproximateBacklogAge` {/* #ApproximateBacklogCountAndAge */}

`ApproximateBacklogCount` represents the approximate count of Tasks currently backlogged in this Task Queue.
The number may include expired Tasks as well as active Tasks, but it will eventually converge to the correct count over time.

`ApproximateBacklogAge` returns the approximate age of the oldest Task in the backlog.
The age is based on the creation time of the Task at the head of the queue.

You can rely on both these counts when making scaling decisions.

#### Known accuracy limitations {/* #backlog-accuracy-limitations */}

These values are approximate.
The most common sources:

- **Overcount from invalid or expired Tasks**: Tasks belonging to cancelled, terminated, completed, or timed out Workflows and Activities stay in the count until they reach the head of the queue and are processed and discarded.
  An invalid or expired Task at the head is removed quickly, so it rarely holds up the count for long.
  A valid Task at the head can stay there longer when there aren't enough Workers to dispatch it. While it sits there, invalid or expired Tasks queued behind it cannot be removed.
  Invalid and expired Tasks are eventually accounted for, but the count may not return to a fully accurate value because of other sources of discrepancy like infrequent metadata updates and database row expirations.
- **Reset to zero on idle Task Queue unload**: If a Task Queue sees no activity for approximately 5 minutes - no Worker polls, no new Tasks added, and no other Task Queue calls (`DescribeTaskQueue`, `UpdateTaskQueueConfig`, etc.) - the Temporal Service unloads it from memory.
  When this happens, `ApproximateBacklogCount` reports zero until the Task Queue is reloaded by the next Worker poll, new Task, or Task Queue API call.
  An idle Task Queue with a backlog but no active Workers can therefore temporarily report zero even though there are Tasks waiting to be processed.
- **Sticky queue exclusion**: [Sticky queues](/sticky-execution) are not included in these values.
  Because Sticky queue Tasks only remain valid for a few seconds, this inaccuracy diminishes as the backlog grows.

### `TasksAddRate` and `TasksDispatchRate` {/* #TasksAddRate-and-TasksDispatchRate */}

Reports the approximate Tasks-per-second added to or dispatched from a Task Queue.
This rate is averaged over the most recent 30-second time interval.
The calculations include Tasks that were added to or dispatched from the backlog as well as Tasks that were immediately dispatched and bypassed the backlog (sync-matched).

The actual Task delivery count may be significantly higher than the number reported by these two values:

- Eager dispatch refers to a Temporal feature where Activities can be requested by an SDK using one Workflow Task completion response.
  Tasks using Eager dispatch do not pass through Task Queues.
- Tasks passed to Sticky Task Queues not included in the returned values for `TasksAddRate` and `TasksDispatchRate`.

### `BacklogIncreaseRate` {/* #BacklogIncreaseRate */}

Approximates the _net_ Tasks per second added to the backlog, averaged over the most recent 30 seconds.
This is calculated as:

```
TasksAddRate - TasksDispatchRate
```

- Positive values of `X` indicate the backlog is growing by about `X` Tasks per second.
- Negative values of `X` indicate the backlog is shrinking by about `X` Tasks per second.

While individual `add` and `dispatch` rates may be inaccurate due to Eager and Sticky Task Queues, the `BacklogIncreaseRate` reliably reflects the rate at which the backlog is shrinking or growing for backlogs older than a few seconds.

## Evaluate Task Queue performance {/* #evaluate-worker-loads */}

A [Task Queue](https://docs.temporal.io/task-queue) is a lightweight, dynamically allocated queue.
[Worker Entities](/workers#worker-entity) poll the queue for [Tasks](https://docs.temporal.io/tasks#task) and retrieve Tasks to work on.
Tasks are contexts that a Worker progresses using a specific Workflow Execution, Activity Execution, or a Nexus Task Execution.
Each Task Queue type offers its Tasks to compatible Workers for Task completion.
The Temporal Service dynamically creates different [Task Queue types](/task-queue) including Activity Task Queues, Workflow Task Queues, and Nexus Task Queues.

With an accurate estimate of backlog Tasks, you can determine the optimal number of Workers to deploy.
Balance your Worker count with the number of Tasks to achieve the best performance.
This approach minimizes Task backlog saturation and reduces idle Workers.

Task Queue data provide numerical insights into your Task Queue activity and backlog characteristics.
Use these numbers to tune your production deployments.
Evaluate your Worker loads and assess whether you need to scale up or reduce your Worker deployment.

:::note RATE LIMITS

[Visibility API rate limits](/cloud/limits#visibility-api-rate-limit) apply to Task Queue performance data requests.

:::

### Query Task Queue info with Temporal CLI {/* #cli-task-queue-info */}

The Temporal CLI helps you monitor and evaluate Worker performance.
Issue the following command to display a list of active Workers that have recently polled a Task Queue:

```
temporal task-queue describe \
    --task-queue YourTaskQueueName \
    [additional options]
```

This command retrieves poller information, backlog statistics, and task reachability for Task types (available in Temporal Server v1.25.0, Temporal CLI 1.1 and later).

:::warning

Task reachability status is experimental.
Determining Task reachability incurs a non-trivial computing cost.
This feature may significantly change or be removed in a future release.

:::

### Query Task Queue info with the Go SDK {/* #go-sdk-task-queue-info */}

Retrieve Task Queue data using the Go SDK by calling `DescribeTaskQueueEnhanced`.
Specify the Task Queue name and set `ReportStats` to `true`, as in the following example:

```go
for _, taskQueueName := range taskQueueNames {
        resp, err := s.client.DescribeTaskQueueEnhanced(ctx, client.DescribeTaskQueueEnhancedOptions{
            TaskQueue:   taskQueueName,
            ReportStats: true,
        })
        if err != nil {
            log.Printf("Error describing task queue %s: %v", taskQueueName, err)
        }

        // Get the backlog count from the enhanced response
        backlogCount += getBacklogCount(resp)
    }
```

### Evaluate Worker availability and capacity issues {/* #worker-capacity-issues */}

Each Temporal [Server](https://docs.temporal.io/temporal-service/temporal-server) records the last time of each poll request.
This time is displayed in the `temporal task-queue describe` output.

- A `LastAccessTime` value exceeding one minute may indicate that the Worker fleet is at capacity or that Workers have shut down or been removed.

- Values under 5 minutes typically suggest the Worker fleet is at capacity.
  "At capacity" means that all Workflow and Activity slots are full.

- Values over 5 minutes since the last poll request usually suggest that Workers have shut down or been removed.
  Workers are removed if 5 minutes have passed since the last poll request.

### Manage your Worker fleet {/* #manage-your-worker-fleet */}

You can adjust the number of Workers to enhance Workflow Execution performance and manage your fleet size.
For instance, a large backlog of Tasks with too few Workers will slow down Workflow Execution completions and decrease processing efficiency.
Adding more Workers boosts speeds up completion rates and improves throughput.
An empty backlog indicates low Worker utilization, allowing you to reduce your fleet and associated costs.

The values provided by `temporal task-queue describe` can help you manage your Worker fleet deployment:

- `ApproximateBacklogAge` shows how long Tasks have been waiting to be dispatched.
  If this time grows too long, more Workers can boost Workflow efficiency.

- Calculate the demand per Worker by dividing the number of backlogged Tasks (`ApproximateBacklogCount`) by the number of Workers.
  Determine if your task processing rate is within an acceptable range for your needs using the per-Worker demand (how many Tasks each Worker has yet to process), the backlog consumption rate (`TasksDispatchRate`, the rate at which Workers are processing Tasks), and the dispatch latency (`ApproximateBacklogAge`, the time the oldest Task has been waiting to be assigned to a Worker).

- The backlog increase rate (`BacklogIncreaseRate`) shows the changing demand on your Workers over time.
  As this rate increases, you may need to add more Workers until demand and capacity are balanced.
  As it decreases, you may be able to reduce your Worker fleet.

## Task Queue processing tuning {/* #task-queues-processing-tuning */}

The following steps limit delays in Task Queue processing due to insufficient or unbalanced Workers.
Review these steps if you notice high `schedule_to_start` metrics.

The steps are arranged in the recommended order of execution.

### Hosts and Resources provisioning

If currently provisioned Worker hosts are fully utilized (near full CPU usage, high load average, etc), additional Workers hosts have to be provisioned to increase the capacity of the Workers pool.

**It's possible to have too many Workers**

Monitor the poll success (`poll_success`/`poll_success_sync`) and poll timeout `poll_timeouts` Server metric counters.

Poll Success Rate = (`poll_success` + `poll_success_sync`) / (`poll_success` + `poll_success_sync` + `poll_timeouts`)

Poll Success Rate should be >90% in most cases of systems with a steady load. For high volume and low latency, try to target >95%.

If you see

1. low Poll Success Rate, and
2. low `schedule_to_start_latency`, and
3. low Worker hosts resource utilization at the same time,

then you might have too many workers, consider sizing down.

### Worker Executor Slots sizing

The main area to focus on when tuning is the number of Worker Executor Slots.
Increase the maximum number of working slots by adjusting `maxConcurrentWorkflowTaskExecutionSize` or `maxConcurrentActivityExecutionSize` if both of the following conditions are met:

1. The Worker hosts are underutilized (no bottlenecks on CPU, load average, etc.).
2. The `worker_task_slots_available` metric from the corresponding Worker type frequently shows a depleted number of available Worker slots.

Alternatively, consider using a resource-based slot supplier as described [here](#slot-suppliers).

### Poller count

Sometimes, it can be appropriate to increase the number of task pollers.
This is usually more common in situations where your Workers have somewhat high latency when communicating with the server.
You can simply use automated poller tuning to handle this automatically.

Consider manual adjustment if:

1. The Worker hosts are underutilized, for example, there are no bottlenecks on CPU, load average, etc.
2. `worker_task_slots_available` metric from the corresponding Worker type shows that a significant percentage of Worker slots are available on a regular basis.
3. The `schedule_to_start` metric is abnormally long.

Then consider increasing the number of pollers by adjusting `maxConcurrentWorkflowTaskPollers` or `maxConcurrentActivityTaskPollers`, depending on which type of `schedule_to_start` metric is elevated.

### Rate Limiting

If, after adjusting the poller and executors count as specified earlier, you still observe an elevated `schedule_to_start`, underutilized Worker hosts, or high `worker_task_slots_available`, you might want to check the following:

- If server-side rate limiting per Task Queue is set by `WorkerOptions#maxTaskQueueActivitiesPerSecond`, remove the limit or adjust the value up. (See [Go](https://pkg.go.dev/go.temporal.io/sdk/internal#WorkerOptions) and [Java](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/worker/WorkerOptions.Builder.html).)
- If Worker-side rate limiting per Worker is set by `WorkerOptions#maxWorkerActivitiesPerSecond`, remove the limit. (See [Go](https://pkg.go.dev/go.temporal.io/sdk/internal#WorkerOptions), [TypeScript](https://typescript.temporal.io/api/interfaces/worker.WorkerOptions#maxconcurrentactivitytaskexecutions), and [Java](https://www.javadoc.io/doc/io.temporal/temporal-sdk/latest/io/temporal/worker/WorkerOptions.Builder.html).)

## Related reading

- [Worker tuning quick reference](/develop/worker-tuning-reference) - SDK defaults and metrics by resource type
- [Workers in production operation guide](https://temporal.io/blog/workers-in-production)
- [Full set of SDK Metrics reference](/references/sdk-metrics)

---

## Worker tuning quick reference

This page provides a quick reference for Worker configuration options and their default values across Temporal SDKs.
Use this guide alongside the comprehensive [Worker performance](/develop/worker-performance) documentation for detailed tuning guidance.

Worker performance is constrained by three primary resources:

| Resource | Description |
|----------|-------------|
| **Compute** | CPU-bound operations, concurrent Task execution |
| **Memory** | Workflow cache, thread pools |
| **IO** | Network calls to Temporal Service, polling |

## How a Worker works

Workers poll a [Task Queue](/task-queue) in Temporal Cloud or a self-hosted Temporal Service, execute Tasks, and respond with the result.

```
┌─────────────────┐     Poll for Tasks       ┌──────────────────┐
│   - Worker      │ ◄─────────────────────── │ Temporal Service │
│   - Workflows   │                          │                  │
│   - Activities  │ ───────────────────────► │                  │
└─────────────────┘   Respond with results   └──────────────────┘
```

Multiple Workers can poll the same Task Queue, providing horizontal scalability.

### How Worker failure recovery works

When a Worker crashes or experiences a host outage:

1. The Workflow Task times out
2. Another available Worker picks up the Task
3. The new Worker replays the Event History to reconstruct state
4. Execution continues from where it left off

For more details on Worker architecture, see [What is a Temporal Worker?](/workers)

## Compute settings

Compute settings control how many Tasks a Worker can execute concurrently.

### Compute configuration options

| Setting | Description |
|---------|-------------|
| `MaxConcurrentWorkflowTaskExecutionSize` | Maximum concurrent Workflow Tasks |
| `MaxConcurrentActivityTaskExecutionSize` | Maximum concurrent Activity Tasks |
| `MaxConcurrentLocalActivityTaskExecutionSize` | Maximum concurrent Local Activities |
| `MaxWorkflowThreadCount` / `workflowThreadPoolSize` | Thread pool for Workflow execution |

### Compute defaults by SDK

| SDK | MaxConcurrentWorkflowTaskExecutionSize | MaxConcurrentActivityTaskExecutionSize | MaxConcurrentLocalActivityTaskExecutionSize | MaxWorkflowThreadCount |
|-----|----------------------------------------|----------------------------------------|---------------------------------------------|------------------------|
| **Go** | 1,000 | 1,000 | 1,000 | - |
| **Java** | 200 | 200 | 200 | 600 |
| **TypeScript** | 40 | 100 | 100 | 1 (reuseV8Context) |
| **Python** | 100 | 100 | 100 | - |
| **.NET** | 100 | 100 | 100 | - |

### Resource-based slot suppliers

Instead of fixed slot counts, you can use resource-based slot suppliers that automatically adjust available Task slots based on CPU and memory utilization.
For implementation details, see [Slot suppliers](/develop/worker-performance#slot-suppliers).

## Memory settings

Memory settings control the Workflow cache size and thread pool allocation.

### Memory configuration options

| Setting | Description |
|---------|-------------|
| `MaxCachedWorkflows` / `StickyWorkflowCacheSize` | Number of Workflows to keep in cache |
| `MaxWorkflowThreadCount` | Thread pool size |
| `reuseV8Context` (TypeScript) | Reuse V8 context for Workflows |

### Memory defaults by SDK

| SDK | MaxCachedWorkflows / StickyWorkflowCacheSize |
|-----|----------------------------------------------|
| **Go** | 10,000 |
| **Java** | 600 |
| **TypeScript** | Dynamic (e.g., 2000 for 4 GiB RAM) |
| **Python** | 1,000 |
| **.NET** | 10,000 |

For cache tuning guidance, see [Workflow cache tuning](/develop/worker-performance#workflow-cache-tuning).

## IO settings

IO settings control the number of pollers and rate limits for Task Queue interactions.

### IO configuration options

| Setting | Description |
|---------|-------------|
| `MaxConcurrentWorkflowTaskPollers` | Number of concurrent Workflow pollers |
| `MaxConcurrentActivityTaskPollers` | Number of concurrent Activity pollers |
| `Namespace APS` | Actions per second limit for Namespace |
| `TaskQueueActivitiesPerSecond` | Activity rate limit per Task Queue |

### IO defaults by SDK

| SDK | MaxConcurrentWorkflowTaskPollers | MaxConcurrentActivityTaskPollers | Namespace APS | TaskQueueActivitiesPerSecond |
|-----|----------------------------------|----------------------------------|---------------|------------------------------|
| **Go** | 2 | 2 | 400 | Unlimited |
| **Java** | 5 | 5 | - | - |
| **TypeScript** | 10 | 10 | - | - |
| **Python** | 5 | 5 | - | - |
| **.NET** | 5 | 5 | - | - |

### Poller autoscaling

Use poller autoscaling to automatically adjust the number of concurrent polls based on workload.
For configuration details, see [Configuring poller options](/develop/worker-performance#configuring-poller-options).

## Metrics reference by resource type

Use these metrics to identify bottlenecks and guide tuning decisions.
For the complete metrics reference, see [SDK metrics](/references/sdk-metrics).

### Compute-related metrics

| Worker configuration option | SDK metric |
|-----------------------------|------------|
| `MaxConcurrentWorkflowTaskExecutionSize` | [`worker_task_slots_available {worker_type = WorkflowWorker}`](/references/sdk-metrics#worker_task_slots_available) |
| `MaxConcurrentActivityTaskExecutionSize` | [`worker_task_slots_available {worker_type = ActivityWorker}`](/references/sdk-metrics#worker_task_slots_available) |
| `MaxWorkflowThreadCount` | [`workflow_active_thread_count`](/references/sdk-metrics#workflow_active_thread_count) (Java only) |
| CPU-intensive logic | [`workflow_task_execution_latency`](/references/sdk-metrics#workflow_task_execution_latency) |

Also monitor your machine's CPU consumption (for example, `container_cpu_usage_seconds_total` in Kubernetes).

### Memory-related metrics

| Worker configuration option | SDK metric |
|-----------------------------|------------|
| `StickyWorkflowCacheSize` | [`sticky_cache_total_forced_eviction`](/references/sdk-metrics#sticky_cache_total_forced_eviction), [`sticky_cache_size`](/references/sdk-metrics#sticky_cache_size), [`sticky_cache_hit`](/references/sdk-metrics#sticky_cache_hit), [`sticky_cache_miss`](/references/sdk-metrics#sticky_cache_miss) |

Also monitor your machine's memory consumption (for example, `container_memory_usage_bytes` in Kubernetes).

### IO-related metrics

| Worker configuration option | SDK metric |
|-----------------------------|------------|
| `MaxConcurrentWorkflowTaskPollers` | [`num_pollers {poller_type = workflow_task}`](/references/sdk-metrics#num_pollers) |
| `MaxConcurrentActivityTaskPollers` | [`num_pollers {poller_type = activity_task}`](/references/sdk-metrics#num_pollers) |
| Network latency | [`request_latency {namespace, operation}`](/references/sdk-metrics#request_latency) |

### Task Queue metrics

| Metric | Description |
|--------|-------------|
| [`poll_success_sync_count`](/cloud/metrics/reference#temporal_cloud_v0_poll_success_sync_count) | Sync match rate (Tasks immediately assigned to Workers) |
| [`approximate_backlog_count`](/cloud/metrics/openmetrics/metrics-reference#temporal_cloud_v1_approximate_backlog_count) | Approximate number of Tasks in a Task Queue |

Task Queue statistics are also available via the `DescribeTaskQueue` API:
- `ApproximateBacklogCount`
- `ApproximateBacklogAge`
- `TasksAddRate`
- `TasksDispatchRate`
- `BacklogIncreaseRate`

For more on Task Queue metrics, see [Available Task Queue information](/develop/worker-performance#task-queue-metrics).

### Failure metrics

| Metric | Description |
|--------|-------------|
| [`long_request_failure`](/references/sdk-metrics#long_request_failure) | Failures for long-running operations (polling, history retrieval) |
| [`request_failure`](/references/sdk-metrics#request_failure) | Failures for standard operations (Task completion responses) |

Common failure codes:
- `RESOURCE_EXHAUSTED` - Rate limits exceeded
- `DEADLINE_EXCEEDED` - Operation timeout
- `NOT_FOUND` - Resource not found

## Worker tuning tips

1. **Scale test before production**: Validate your configuration under realistic load.
2. **Infrastructure matters**: Workers don't operate in a vacuum. Consider network latency, database performance, and external service dependencies.
3. **Tune and observe**: Make incremental changes and monitor metrics before making additional adjustments.
4. **Identify the bottleneck**: Use the [theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints). Improving non-bottleneck resources won't improve overall throughput.

For detailed tuning guidance, see:
- [Worker performance](/develop/worker-performance)
- [Worker deployment and performance best practices](/best-practices/worker)
- [Performance bottlenecks troubleshooting](/troubleshooting/performance-bottlenecks)

## Related resources

- [What is a Temporal Worker?](/workers) - Conceptual overview
- [Worker performance](/develop/worker-performance) - Comprehensive tuning guide
- [Worker deployment and performance](/best-practices/worker) - Best practices
