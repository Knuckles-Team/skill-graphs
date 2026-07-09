   available Worker (a sync match).
3. If a Worker is available, the Task is routed to that Worker.
4. If no Worker is available (sync match fails), the Matching Service pushes a signal to the WCI, and the WCI invokes
   the configured compute provider.
5. The Serverless Worker starts, creates a Temporal Client, and begins polling the Task Queue.
6. The Worker processes available Tasks until it exits (see [Worker lifecycle](#worker-lifecycle)).

Each invocation is independent. The Worker creates a fresh client connection on every invocation. There is no connection
reuse or shared state across invocations.

## Autoscaling {/* #autoscaling */}

The [WCI](#worker-controller-instance) automatically scales Serverless Workers based on Task Queue signals. When Tasks
arrive and no Worker is available, the WCI invokes new Workers. When the Tasks are done, Workers exit and scale to zero.

The WCI uses two signals to decide when to invoke new Workers:

### Sync match failure {/* #sync-match-failure */}

When a Task is submitted, the [Matching Service](/temporal-service/temporal-server#matching-service) attempts to route
it directly to an available Worker. If no Worker is available, the sync match fails, and the Matching Service pushes a
signal to the WCI. The WCI then invokes a new Worker. This is the primary scaling path. Because the Matching Service
pushes match failures to the WCI as they happen rather than the WCI polling on a timer, latency stays low and scaling is
responsive.

### Task Queue backlog {/* #task-queue-backlog */}

The WCI monitors Task Queue metadata to determine whether pending Tasks exist without enough Workers to process them. If
there are Tasks on the queue and not enough Workers, the WCI invokes additional Workers.

## Scaling with long-lived Workers {/* #scaling-with-long-lived-workers */}

Serverless Workers can share a Task Queue with long-lived Workers. Because Serverless Workers are only invoked on
[sync match failure](#sync-match-failure), Serverless Workers only pick up Tasks that no long-lived Worker was available
to handle. In practice, the Serverless Workers act as spillover capacity for the long-lived fleet.

:::caution

If you configure Serverless and long-lived Workers on the same Task Queue, do not enable dynamic scaling on the
long-lived Workers. The two groups cannot coordinate their scaling behavior. If both scale dynamically, the long-lived
Workers may scale up to handle the same Tasks that Temporal is simultaneously invoking Serverless Workers for, leading
to unnecessary invocations and unpredictable scaling.

:::

## Worker lifecycle {/* #worker-lifecycle */}

A single Serverless Worker invocation has three phases: init, work, and shutdown.

<CaptionedImage
  src="/diagrams/serverless-worker-lifecycle.svg"
  srcDark="/diagrams/serverless-worker-lifecycle-dark.svg"
  alt="Serverless Worker lifecycle"
  title="Diagram is not to scale. The shutdown deadline buffer controls when the Worker stops polling, and the Worker stop timeout controls how long the Worker waits for in-flight Tasks to finish before shutdown hooks run. Shutdown hooks typically take less than a few seconds."
/>

During the **init** phase, the Worker initializes and establishes a client connection to Temporal.

During the **work** phase, the Worker polls the Task Queue and processes Tasks.

During the **shutdown** phase, the Worker stops polling, waits for in-flight Tasks to finish, and runs any shutdown
hooks (for example, OpenTelemetry telemetry flushes). Shutdown begins before the invocation deadline so the Worker can
exit cleanly before the compute provider forcibly terminates the execution environment.

### Tuning for long-running Activities

If your Worker handles long-running Activities, set these three values together:

- **Worker stop timeout > longest Activity runtime.** Gives in-flight Activities enough time to finish after polling
  stops.
- **Shutdown deadline buffer > Worker stop timeout + shutdown hook time.** Ensures the drain and any shutdown hooks
  complete before the compute provider terminates the environment.
- **Invocation deadline > longest Activity runtime + shutdown deadline buffer.** Set on the compute provider to give
  each invocation enough total runtime.

  :::tip

  If your longest-running Activity runs longer than half the maximum invocation deadline, this constraint may be
  difficult or impossible to meet. In this case, use
  [Activity Heartbeats](/encyclopedia/detecting-activity-failures#activity-heartbeat) to record the state of the
  Activity execution so that the next retry can pick up where it left off.

  :::

For example, if your longest Activity runtime is 5 minutes, and your shutdown hooks take 3 seconds to run, set the
Worker stop timeout to more than 5 minutes, and the shutdown deadline buffer to more than 303 seconds (5 minutes + 3
seconds). Set your invocation deadline to at least 10 minutes and 3 seconds (5 minutes + 303 seconds).

The Worker stop timeout controls how long the Worker waits for in-flight Tasks to finish after it stops polling. The
shutdown deadline buffer controls how much time before the invocation deadline the Worker stops polling for Tasks.

Raising only the shutdown deadline buffer makes the Worker stop polling earlier, but does not give in-flight Tasks any
more time to complete.

Raising only the Worker stop timeout does not make the Worker stop polling earlier, which means the compute provider
might terminate the Worker before the full stop timeout completes. In-flight Activities then do not get the full stop
timeout to finish, and the shutdown hooks may not run.

## Failure handling {/* #failure-handling */}

Serverless Workers rely on Temporal's standard retry and timeout semantics to recover from failures. The following
sections describe common failure scenarios and how they are handled.

### Worker crash {/* #worker-crash */}

If a Worker invocation crashes (out of memory, unhandled exception, etc.), the behavior follows standard Temporal retry
semantics:

- The Activity Timeout fires after the configured duration.
- Temporal retries the Activity on a different Worker invocation.
- No manual intervention is required.

### Provider concurrency limit {/* #provider-concurrency-limit */}

If the compute provider's concurrency limit is reached (for example, AWS Lambda account concurrency):

- Further invocations from the WCI fail.
- Tasks remain in the Task Queue backlog. No data loss occurs.
- Processing slows until concurrency frees up.

### Resource exhaustion across Activity slots {/* #resource-exhaustion */}

By default, a single Worker invocation may run multiple Activity slots. A crash or resource exhaustion in one Activity
(for example, out-of-memory from a memory-intensive operation) can affect other Activities running in the same
invocation.

To isolate Activities from each other:

- Split Workflow and Activity Workers into separate compute functions.
- Set Activity slots to 1 per invocation.

With single-slot configuration, each Activity gets a dedicated execution environment.

## Constraints {/* #constraints */}

| Constraint        | Detail                                                                                                                                                             |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Activity duration | Must complete within the compute provider's invocation limit (minus shutdown deadline buffer). For AWS Lambda, the maximum is 15 minutes.                          |
| Workflow duration | No limit. Workflows of any duration work, regardless of the invocation timeout. A Workflow runs across as many invocations as needed.                              |
| Worker code       | Same Temporal SDK Worker code, using the serverless Worker package for your SDK.                                                                                   |
| Versioning        | [Worker Versioning](/worker-versioning) is required. Each Workflow must have an `AutoUpgrade` or `Pinned` behavior, set per-Workflow or as a Worker-level default. |

## Compute providers {/* #compute-providers */}

A compute provider is the configuration that tells Temporal how to invoke a Serverless Worker. The compute provider is
set on a [Worker Deployment Version](/worker-versioning#deployment-versions) and specifies the provider type, the
invocation target, and the credentials Temporal needs to trigger the invocation.

For example, an AWS Lambda compute provider includes the Lambda function ARN and the IAM role that Temporal assumes to
invoke the function.

Compute providers are only needed for Serverless Workers. Traditional long-lived Workers do not require a compute
provider because the Worker process manages its own lifecycle.

### Supported providers

| Provider   | Description                                                                   |
| ---------- | ----------------------------------------------------------------------------- |
| AWS Lambda | Temporal assumes an IAM role in your AWS account to invoke a Lambda function. |

---

## Sticky Execution

This page discusses [Sticky Execution](#sticky-execution).

## What is a Sticky Execution? {/* #sticky-execution */}

Workers cache the state of the Workflow they execute.
To make this caching more effective, Temporal employs a performance optimization known as "Sticky Execution", which directs Workflow Tasks to the same Worker that previously processed tasks for a specific Workflow Execution.

### How Sticky Execution Works

Once Workflow Execution begins, the Temporal Service schedules a Workflow Task and puts it into a Task Queue with the name you specify.
Any Worker that polls that Task Queue is eligible to accept the Task and begin executing the Workflow.

The Worker that picks up this Workflow Task will continue polling the original Task Queue, but will also begin polling an additional Task Queue, which the Temporal Service shares exclusively with that specific Worker.
This queue, which has an automatically-generated name, is known as a **Sticky Queue**.

The Worker caches the Workflow state in memory, which improves performance by reducing the need to reconstruct the Workflow from its Event History for every Task.
As the Workflow Execution progresses, the Temporal Service schedules additional Workflow Tasks into this Worker-specific Sticky Queue.

If the Worker fails to start a Workflow Task in the Sticky Queue shortly after it's scheduled (within five seconds by default), the Temporal Service disables stickiness for that Workflow Execution.
When stickiness is disabled, the Temporal Service reschedules the Workflow Task in the original queue, allowing any Worker to pick it up and continue the Workflow Execution.

If a Workflow Task fails, the Worker removes that Workflow Execution from its cache (as it's now in an unknown state), which invalidates the Sticky Execution.
The Workflow Task is then put back into the original Task Queue.

### Why Sticky Execution?

The main benefit of Sticky Execution is improved performance.
By caching the Workflow state in memory and directing tasks to the same Worker, it reduces the need to reconstruct the Workflow from its Event History for every Task, which is particularly useful for latency-sensitive Workflows.

Sticky Execution is the default behavior of the Temporal Platform and only applies to Workflow Tasks.
Since Event History is associated with a Workflow, the concept of Sticky Execution is not relevant to Activity Tasks.

- [How to set `StickyScheduleToStartTimeout` on a Worker in Go](https://pkg.go.dev/go.temporal.io/sdk/internal#WorkerOptions)

Sticky Executions are the default behavior of the Temporal Platform.

---

## Task Queues and naming best practices
