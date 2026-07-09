[Activity Task](#activity-task) and executes the [Activity Definition](/activity-definition) (also known as the Activity
Function).

The [ActivityTaskScheduled Event](/references/events#activitytaskscheduled) corresponds to when the Temporal Service
puts the Activity Task into the Task Queue.

The [ActivityTaskStarted Event](/references/events#activitytaskstarted) corresponds to when the Worker picks up the
Activity Task from the Task Queue.

Either [ActivityTaskCompleted](/references/events#activitytaskcompleted) or one of the other Closed Activity Task Events
corresponds to when the Worker has yielded back to the Temporal Service.

The API to schedule an Activity Execution provides an "effectively once" experience, even though there may be several
Activity Task Executions that take place to successfully complete an Activity.

Across retries, an Activity Task can carry forward
[Heartbeat](/encyclopedia/detecting-activity-failures#activity-heartbeat) payload from the previous attempt, allowing
long-running Activities to resume from their last checkpoint.

Once an Activity Task finishes execution, the Worker responds to the Temporal Service with a specific Event:

- ActivityTaskCanceled
- ActivityTaskCompleted
- ActivityTaskFailed
- ActivityTaskTerminated
- ActivityTaskTimedOut

## What is a Nexus Task? {/* #nexus-task */}

A Nexus Task delivers one Nexus request to start or cancel a [Nexus Operation](/nexus).

### What is a Nexus Task Execution? {/* #nexus-task-execution */}

A Nexus Task Execution occurs when a Worker uses the context provided from the Nexus Task and executes an action
associated with a Nexus Operation which commonly includes starting a Nexus Operation using its Nexus Operation handler
plus many additional actions that may be performed on a Nexus Operation.

The NexusOperationScheduled Event corresponds to when the Temporal Service records the Workflow's intent to schedule an
operation.

The NexusOperationStarted Event corresponds to when the Worker picks up the Nexus Task from the Task Queue, starts an
asynchronous Nexus Operation, and returns an Operation token to the caller indicating the asynchronous Nexus Operation
has started.

Either NexusOperationCompleted or one of the other Closed Nexus Operation Events corresponds to when the Nexus Operation
has reached a final state due to successfully completing the operation or unsuccessfully completing the operation in the
case of a failure, timeout, or cancellation.

A Nexus Operation Execution appears to the caller Workflow as a single RPC, while under the hood the Temporal Service
may issue several Nexus Tasks to attempt to start the Operation. Hence, a Nexus Operation Handler implementation should
be idempotent. The WorkflowRunOperation provided by the SDK leverages Workflow ID based deduplication to ensure
idempotency and provide an "effectively once" experience.

A Nexus Task Execution completes when a Worker responds to the Temporal Service with either a RespondNexusTaskCompleted
or RespondNexusTaskFailed call, or when the Task times out.

The Temporal Service interprets the outcome and determines whether to retry the Task or record the progress in a History
Event:

- NexusTaskCompleted
- NexusTaskFailed

---

## Worker Shutdown Behavior

When a Worker shuts down, it stops polling for new tasks and begins the shutdown sequence.
In the case of in-flight Workflow Tasks, shutdown may cause them to fail if they aren’t completed in time, after exhausting Retry Policy attempts.

There are two types of shutdown behavior that can occur, depending on whether an idea of “graceful shutdown” is configured.

## Graceful Shutdown

Graceful shutdown configures how much time a Worker has to complete its current task before shutting down.
An Activity is able to determine that the Worker it’s running on is being shut down, through the Activity context.

> Core SDKs - `graceful_shutdown_period`

> Go - `WorkerStopTimeout`

> Java - `shutdown()` followed by `awaitTermination(timeout, unit)`

### Workflow tasks

Any in-flight Workflow Tasks are (attempted to be) completed.
The only reason they may not immediately, is if Workflow code is (incorrectly) blocking, or because of Local Activities (see below).

### Activities

Activities are allowed to complete during the graceful shutdown period.

### Local Activities

Because Local Activities run within a Workflow Task, current and future Local Activities within the same Workflow Task will be allowed to run and complete, assuming there is no additional command to yield to.

If the Local Activity is unable to complete by the graceful shutdown period, the Local Activity attempt is sent a cancel signal.
In this case, no new Local Activities will be retried or started, and the Worker is shut down.
The Worker still waits for the current Workflow Task to complete, meaning you can eventually hit your Workflow Task or execution timeout, unless another Worker is spun up.

## Non-Graceful Period Shutdown

This behavior is for either no graceful period being specified, or if the shutdown has taken longer than the configured graceful period.
In all cases, the Activity context is canceled and the Worker will finish shutdown when the current Workflow Task completes (with either success or failure).

:::note
Go and Core SDKs behave differently when we pass task timeout and the Activity or Local Activity is still running:

**Go** - The shutdown completes, but the Activity will continue to run and use a slot.

**Core** - The Worker shutdown will not complete while the Activity completes.
:::

### Local Activities

The Local Activity is sent a cancel signal, then the Workflow Task heartbeats stop, and no new Local Activities will be retried or started.
The Worker still waits for the current Workflow Task to complete, meaning you can eventually hit your Workflow Task or execution timeout, unless another Worker is spun up.

## General Developer Guidance

- Ensure Activities and Local Activities **honor context cancellation** or other shutdown signals.
- Expect that **long or hung Local Activities may block shutdown** unless you fail early.
  It is recommended that Local Activities should already generally be used for short Activities.

---

## Worker Versioning

This page defines some of the underlying concepts used in [Worker Versioning](/production-deployment/worker-deployments/worker-versioning):

- [Worker Deployments](#deployments)
- [Worker Deployment Versions](#deployment-versions)
- [Versioning Behaviors](#versioning-behaviors)
- [Versioning Definitions](#versioning-definitions)
- [Versioning Statuses](#versioning-statuses)
- [Continue-as-new, Child Workflow, and Retry Semantics](#inheritance-semantics)

## Worker Deployments {/* #deployments */}

A Worker Deployment is a logical service that groups similar Workers together for unified management.
Each Deployment has a name (such as your service name) and supports versioning through a series of Worker Deployment Versions.

## Worker Deployment Versions {/* #deployment-versions */}

A Worker Deployment Version represents an iteration of a Worker Deployment.
Each Deployment Version is identified by a deployment name and a Build ID.
The deployment name groups related Workers across versions, and the Build ID identifies a specific release of your Worker code.
Each Deployment Version consists of Workers that share the same code build and environment.
When a Worker starts polling for Workflow and Activity Tasks, it reports its Deployment Version to the Temporal Server.

## Versioning Behaviors {/* #versioning-behaviors */}

You can declare each Workflow type to have a **Versioning Behavior**, either Pinned or Auto-Upgrade, in your Workflow configuration using an SDK or the CLI.

To learn more about implementing Worker Versioning, see our [Worker Versioning in production](production-deployment/worker-deployments/worker-versioning) page.

### Pinned Workflows {/* #pinned */}

A **Pinned** Workflow is guaranteed to complete on a single Worker Deployment Version. You can mark a Workflow Type as pinned when you register it by adding an additional Pinned parameter. If you need to move a pinned Workflow to a new version, use [`temporal workflow update-options`](/cli/command-reference/workflow#update-options).

### Auto-Upgrade Workflows {/* #auto-upgrade */}

An **Auto-Upgrade** Workflow will move to the latest Worker Deployment Version automatically whenever you change the current version. Auto-upgrade Workflows are not restricted to a single Deployment Version and need to be kept replay-safe manually, i.e. with [patching](/workflow-definition#workflow-versioning).

### Activity behavior across versions

There are a few scenarios to consider for your Activities when you're handling your Worker Deployment versions.

- Activities generally start on the Worker Deployment Version of their Workflow which means:
  - For Pinned Workflows, an Activity starts on the pinned version.
  - For Auto-Upgrade Workflows, an Activity starts on the Target Worker Deployment Version of the Workflow. In this case, Workflow Execution moves to its Target Version immediately before starting the Activity if the Target Version is different from the last used Version. The Target Worker Deployment Version of a Workflow is the Current or Ramping Version of the Workflow's Task Queue, depending on the Ramp Percentage and Workflow ID.

There is an exception where you will have **Independent Activities**. Independent Activities are specific to Worker Versioning. They start on the Current or Ramping Version of their own Task Queue independently from their Workflow.

- For a Pinned Workflow, Independent Activities are Activities that start on a Task Queue that's not a member of the calling Workflow's Pinned Worker Deployment Version.
- For an Auto-Upgrade Workflow, Independent Activities are Activities that start on a Task Queue that's not a member of the calling Workflow's Target Worker Deployment Version.

Since Independent Activities aren't part of a Workflow's version, they can run in a few different ways:

- The Activity Task Queue is running in a separate Worker Deployment that only has the Independent Activity.
- The Independent Activity is in an unversioned Task Queue.
- The Independent Activity is in a separate Worker Deployment that has its own Workflows, but other Workflows reuse the Activity from other Worker Deployments.

## Versioning Definitions

- **Current Worker Deployment Version**: The version where Workflows are routed to unless they were previously pinned on a different version. Other versions can continue polling to allow pinned Workflows to finish executing or in case you need to roll back. If no current version is specified, the default is unversioned.
- **Ramping Worker Deployment Version**: The version where a configurable percentage of Workflows are routed to unless they were previously pinned on a different version. The ramp percentage can be in the range [0, 100]. Workflows that don't go to the Ramping Version will go to the Current Version. If no Ramping Version is specified, 100% of new Workflows and Auto-Upgrade Workflows will go to the Current Version.
- **Target Worker Deployment Version**: The version your Workflow will upgrade to next. This could be the Deployment's Current Version or the Ramping Version. For example, if an Auto-Upgrade Workflow was running on Version A, the Current Version is B, and there is a 5% ramp to C, there is a 95% chance that its Target Version is B and 5% that it's C. Workflow ID determines whether the workflow falls into the 95% group or the 5% group.

## Versioning Statuses {/* #versioning-statuses */}

A Worker Deployment Version moves through the following states:

1. **Inactive**: The version exists because a Worker with that version has polled the server. If this version never becomes Active, it will never be Draining or Drained.
2. **Active**: The version is either Current or Ramping, so it is accepting new Workflows and existing auto-upgrade Workflows.
3. **Draining**: The version has open pinned Workflows running on it, but stopped being Current or Ramping, usually because a newer version has been deployed. It is possible to be Draining and have no open pinned Workflows for a short time, since the drainage status is updated only periodically.
4. **Drained**: The version was draining and now all the pinned Workflows that were running on it are closed. Closed Workflows may still re-run some code paths if they are [Queried](https://docs.temporal.io/sending-messages#sending-queries) within their [Retention Period](https://docs.temporal.io/temporal-service/temporal-server#retention-period) and Workers with that version are still polling.

## Continue-as-new, Child Workflow, and Retry Semantics {/* #inheritance-semantics */}

When Workflows start new runs (e.g. by continuing-as-new or retrying) the new run may inherit their versioning behavior. This section explains how inheritance works across different Workflow execution patterns.

### Ways Workflows Start New Runs

A Workflow can start a new run through:

- Starting a [Child Workflow](https://docs.temporal.io/child-workflows)
- Invoking [Continue-As-New](https://docs.temporal.io/workflow-execution/continue-as-new)
- Retrying per its [Retry Policy](https://docs.temporal.io/encyclopedia/retry-policies)
- Starting another iteration of a [Cron Job](https://docs.temporal.io/cron-job) (superseded by [Schedules](https://docs.temporal.io/schedule))

### Inheritance Rules Overview

Auto-upgrade Workflows never inherit versions.
By default, Pinned workflows will pass their version to any Pinned children.

This section provides more detail on specific inheritance scenarios.

### Inheritance by Scenario

#### Child Workflows

**When Parent is Pinned:**

- Child inherits the parent's version if the child's Task Queue belongs to that version
- Child's first Workflow task executes in the same version as its parent
- If child is also Pinned: child remains Pinned to the inherited version for its lifetime
- If child is Auto-Upgrade: child's behavior changes to Auto-Upgrade after the first task completes
- If child's Task Queue is not in the same Worker Deployment as parent: no inheritance occurs, child starts on Current Version of its task queue

**When Parent is Auto-upgrade:**

- Child inherits no initial Versioning Behavior
- Child starts on the Current Version of its Worker Deployment like all new Workflow executions

#### Continue-As-New

**When Original Workflow is Pinned:**

- The Pinned version is inherited across the Continue-As-New chain
- If the new run's Task Queue is not in the same Worker Deployment as the original Workflow: no inheritance occurs, new run starts on Current Version of its task queue

**When Original Workflow is Auto-upgrade:**

- No version inheritance occurs

#### Retries

**Inheritance Conditions (all must be met):**

- The retried run is effectively pinned at the time of retry
- The retried run inherited a pinned version when it started (i.e., it is a child of a pinned parent, or a Continue-As-New of a pinned run)
- The retried run is running on a Task Queue in the inherited version

**When Conditions Not Met:**

- No version inheritance occurs

#### Cron Jobs

- **Never inherit** versioning behavior or version

### Versioning Override Inheritance

- Children, crons, retries, and continue-as-new inherit the source run's override **if**:
  - The override is pinned, **AND**
  - The new Workflow's Task Queue belongs to the override version
- Override inheritance is evaluated separately and takes precedence over inherited base version

---

## What is a Temporal Worker?

This page discusses the following:

- [Worker](#worker)
- [Worker Program](#worker-program)
- [Worker Entity](#worker-entity)
- [Worker Identity](#worker-identity)
- [Worker Process](#worker-process)

## What is a Worker? {/* #worker */}

In day-to-day conversations, the term Worker is used to denote either a [Worker Program](#worker-program), a [Worker Process](#worker-process), or a [Worker Entity](/workers#worker-entity).
Temporal documentation aims to be explicit and differentiate between them.

## What is a Worker Program? {/* #worker-program */}

A Worker Program is the static code that defines the constraints of the Worker Process, developed using the APIs of a Temporal SDK.

:::info

- [How to run a development Worker using the Go SDK](/develop/go/workers/run-worker-process#develop-worker)
- [How to run a development Worker using the Java SDK](/develop/java/workers/run-worker-process)
- [How to run a development Worker using the PHP SDK](/develop/php/workers/run-worker-process#run-a-dev-worker)
- [How to run a development Worker using the Python SDK](/develop/python/workers/run-worker-process#run-a-dev-worker)
- [How to run a development Worker using the TypeScript SDK](/develop/typescript/workers/run-worker-process#run-a-dev-worker)
- [How to run a development Worker using the .NET SDK](/develop/dotnet/workers/run-worker-process)

- [How to connect a Go SDK Worker to Temporal Cloud](/develop/go/workers/run-worker-process#connect-to-temporal-cloud)
- [How to run a Temporal Cloud Worker using the TypeScript SDK](/develop/typescript/workers/run-worker-process#run-a-temporal-cloud-worker)

:::

## What is a Worker Entity? {/* #worker-entity */}

A Worker Entity is the individual Worker within a Worker Process that listens to a specific Task Queue.

A Worker Entity listens and polls on a single Task Queue.
A Worker Entity contains a Workflow Worker and/or an Activity Worker, which makes progress on Workflow Executions and Activity Executions, respectively.

**Can a Worker handle more Workflow Executions than its cache size or number of supported threads?**

Yes it can.
However, the trade off is added latency.

Workers are stateless, so any Workflow Execution in a blocked state can be safely removed from a Worker.
Later on, it can be resurrected on the same or different Worker when the need arises (in the form of an external event).
Therefore, a single Worker can handle millions of open Workflow Executions, assuming it can handle the update rate and that a slightly higher latency is not a concern.

**Operation guides:**

- [How to tune Workers](/develop/worker-performance)
- [Worker tuning quick reference](/develop/worker-tuning-reference) - SDK defaults and metrics

## What is a Worker Identity? {/* #worker-identity */}

Workers have an associated identifier that helps identify the specific Worker instance.
By default, Temporal SDKs set a Worker Identity to `${process.pid}@${os.hostname()}`, which combines the Worker's process ID (`process.pid`) and the hostname of the machine running the Worker (`os.hostname()`).

The Worker Identity is visible in various contexts, such as Event History and the list of pollers on a Task Queue.

You can use the Worker Identity to aid in debugging operational issues.
By providing a user assigned identifier, you can trace issues back to specific Worker instances.

**What are some limitations of the default identity?**

While the default identity format may seem sensible, it often proves to be of limited usefulness in cloud environments.
Some common issues include:

- **Docker containers**: When running Workers inside Docker containers, the process ID is always `1`, as each container typically runs a single process. This makes the process identifier meaningless for identification purposes.
- **Random hostnames**: In some cloud environments, such as Amazon ECS (Elastic Container Service), the hostname is a randomly generated string that does not provide any meaningful information about the Worker's execution context.
- **Ephemeral IP addresses**: In certain cases, the hostname might be set to an ephemeral IP address, which can change over time and does not uniquely identify a Worker instance.

**What are some recommended approaches?**

It is recommended that you ensure that the Worker Identity can be linked back to the corresponding machine, process, execution context, or log stream.
In some execution environments, this might require that you explicitly specify the Worker Identity.

Here are some approaches:

- **Use environment-specific identifiers**: Choose an identifier that is specific to your execution environment. For example, when running Workers on Amazon ECS, you can set the Worker Identity to the ECS Task ID, which uniquely identifies the task running the Worker.
- **Include relevant context**: Incorporate information that helps establish the context of the Worker, such as the deployment environment (`staging` or `production`), region, or any other relevant details.
- **Ensure uniqueness**: Make sure that the Worker Identity is unique within your system to avoid ambiguity when debugging issues.
- **Keep it concise**: While including relevant information is important, try to keep the Worker Identity concise and easily readable to facilitate quick identification and troubleshooting.

## What is a Worker Process? {/* #worker-process */}

<CaptionedImage
    src="/diagrams/worker-and-server-component.svg"
    title="Component diagram of a Worker Process and the Temporal Server"
    />

A Worker Process is responsible for polling a [Task Queue](/task-queue), dequeueing a [Task](/tasks#task), executing your code in response to a Task, and responding to the [Temporal Service](/temporal-service) with the results.

More formally, a Worker Process is any process that implements the Task Queue Protocol and the Task Execution Protocol.

- A Worker Process is a Workflow Worker Process if the process implements the Workflow Task Queue Protocol and executes the Workflow Task Execution Protocol to make progress on a Workflow Execution.
  A Workflow Worker Process can listen on an arbitrary number of Workflow Task Queues and can execute an arbitrary number of Workflow Tasks.
- A Worker Process is an Activity Worker Process if the process implements the Activity Task Queue Protocol and executes the Activity Task Processing Protocol to make progress on an Activity Execution.
  An Activity Worker Process can listen on an arbitrary number of Activity Task Queues and can execute an arbitrary number of Activity Tasks.

**Worker Processes are external to a Temporal Service.**
Temporal Application developers are responsible for developing [Worker Programs](#worker-program) and operating Worker Processes.
Said another way, the [Temporal Service](/temporal-service) (including the Temporal Cloud) doesn't execute any of your code (Workflow and Activity Definitions) on Temporal Service machines. The Temporal Service is solely responsible for orchestrating [State Transitions](/workflow-execution#state-transition) and providing Tasks to the next available [Worker Entity](/workers#worker-entity).

While data transferred in Event Histories is [secured by mTLS](/self-hosted-guide/security#encryption-in-transit-with-mtls), by default, it is still readable at rest in the Temporal Service.

To solve this, Temporal SDKs offer a [Data Converter API](/dataconversion) that you can use to customize the serialization of data going out of and coming back in to a Worker Entity, with the net effect of guaranteeing that the Temporal Service cannot read sensitive business data.

In many of our tutorials, we show you how to run both a Temporal Service and one Worker on the same machine for local development.
However, a production-grade Temporal Application typically has a _fleet_ of Worker Processes, all running on hosts external to the Temporal Service.
A Temporal Application can have as many Worker Processes as needed.

A Worker Process can be both a Workflow Worker Process and an Activity Worker Process.
Many SDKs support the ability to have multiple Worker Entities in a single Worker Process.
(Worker Entity creation and management differ between SDKs.)
A single Worker Entity can listen to only a single Task Queue.
But if a Worker Process has multiple Worker Entities, the Worker Process could be listening to multiple Task Queues.

<CaptionedImage
    src="/diagrams/worker-and-server-entity-relationship.svg"
    title="Entity relationship diagram (meta model) of Worker Processes, Task Queues, and Tasks"
/>

Worker Processes executing Activity Tasks must have access to any resources needed to execute the actions that are defined in Activity Definitions, such as the following:

- Network access for external API calls.
- Credentials for infrastructure provisioning.
- Specialized GPUs for machine learning utilities.

The Temporal Service itself has [internal workers](https://temporal.io/blog/workflow-engine-principles/#system-workflows-1910) for system Workflow Executions.
However, these internal workers are not visible to the developer.

---

## Temporal Cron Job

This page discusses [Cron Job](#temporal-cron-job) including [Cron Schedules](#cron-schedules), [Time Zones](#cron-job-time-zones), and [how to stop a Cron Schedule](#stop-cron-schedules).

## What is a Temporal Cron Job? {/* #temporal-cron-job */}

:::note

We recommend using [Schedules](/schedule) instead of Cron Jobs.
Schedules were built to provide a better developer experience, including more configuration options and the ability to update or pause running Schedules.

:::

A Temporal Cron Job is the series of Workflow Executions that occur when a Cron Schedule is provided in the call to spawn a Workflow Execution.

- [How to set a Cron Schedule using the Go SDK](/develop/go/workflows/schedules#temporal-cron-jobs)
- [How to set a Cron Schedule using the Java SDK](/develop/java/workflows/schedules#cron-schedule)
