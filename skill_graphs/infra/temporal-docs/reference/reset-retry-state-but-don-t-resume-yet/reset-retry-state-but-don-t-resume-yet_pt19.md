
Temporal does not impose a limit on the number of custom Search Attributes you can create with Elasticsearch. However, [Elasticsearch sets a default mapping limit](https://www.elastic.co/guide/en/elasticsearch/reference/8.6/mapping-settings-limit.html) that may apply.
Custom Search Attributes are an advanced Visibility feature and are not supported on Cassandra.

Size limits for a custom Search Attribute:

{/*
_This refers to the SA key you create in the visibility store with `tctl search-attribute create`. this value is no longer applicable so commenting out for ref later_
Default total maximum number of Search Attribute **keys** per Temporal Service is 100. */}

- The default single Search Attribute **value** size limit is 2 KB.

{/* TODO - [How to configure Search Attribute value size limit](#) */}

- The maximum total Search Attribute size is 40 KB.

{/* TODO - [How to configure total Search Attribute size limit](#) */}

- The maximum total characters per Search Attribute value is 255.

{/* temp keeping for reference
This is configurable with [`SearchAttributesNumberOfKeysLimit`, `SearchAttributesTotalSizeLimit` and `SearchAttributesSizeOfValueLimit`](https://github.com/temporalio/temporal/blob/v1.7.0/service/history/configs/config.go#L440-L442), if you know what you are doing.
*/}

For Temporal Cloud specific configurations, see the [Defaults, limits, and configurable settings -Temporal Cloud](/cloud/limits#number-of-custom-search-attributes) guide.

### Usage {/* #usage */}

Search Attributes available in your Visibility store can be used with Workflow Executions for the Temporal Service.
To actually have results from the use of a [List Filter](/list-filter), Search Attributes must be added to a Workflow Execution as metadata.

- To create custom Search Attributes in your Visibility store, see [Create custom Search Attributes](/self-hosted-guide/visibility#create-custom-search-attributes).
- To remove a custom Search Attribute from the Visibility store, see [Remove custom Search Attributes](/self-hosted-guide/visibility#remove-custom-search-attributes).
  Removing custom Search Attributes is not supported on Temporal Cloud.
- To rename a custom Search Attribute on Temporal Cloud, see [`tcld namespace search-attributes rename`](/cloud/tcld/namespace/#rename).

With Workflows you can do the following:

- Set the value of Search Attributes in your Workflow
- Update the value set for a Search Attribute from within the Workflow code
- Remove the value set for a Search Attribute from within the Workflow code

:::info Manage Search Attributes by SDK

- [How to manage Search Attributes using the Go SDK](/develop/go/platform/observability#visibility)
- [How to manage Search Attributes using the Java SDK](/develop/java/platform/observability#visibility)
- [How to manage Search Attributes using the PHP SDK](/develop/php/platform/observability#visibility)
- [How to manage Search Attributes using the Python SDK](/develop/python/platform/observability#visibility)
- [How to manage Search Attributes using the TypeScript SDK](/develop/typescript/platform/observability#visibility)
- [How to manage Search Attributes using the .NET SDK](/develop/dotnet/platform/observability#search-attributes)

:::

- To get a list of Search Attributes using the Temporal CLI, issue `temporal operator search-attribute list`. See [Search Attributes](/search-attribute).

After you add and set your Search Attributes, use your default or custom Search Attributes in a List Filter.

{/* commenting out this part. added this detail in how to create a custom search attribute under clusters.
The [temporalio/auto-setup](https://hub.docker.com/r/temporalio/auto-setup) Docker image uses a pre-defined set of custom Search Attributes that are handy for testing.
Their names indicate their types:

- CustomBoolField
- CustomDatetimeField
- CustomDoubleField
- CustomIntField
- CustomKeywordField
- CustomTextField
  */}

---

## Temporal Visibility

This page provides an overview of Temporal Visibility.

The term [Visibility](/visibility), within the Temporal Platform, refers to the subsystems and APIs that enable an operator to view, filter, and search for Workflow Executions that currently exist within a Temporal Service.

The [Visibility store](/self-hosted-guide/visibility) in your Temporal Service stores persisted Workflow Execution Event History data and is set up as a part of your [Persistence store](/temporal-service/persistence) to enable listing and filtering details about Workflow Executions that exist on your Temporal Service.

- [How to set up a Visibility store](/self-hosted-guide/visibility)

With Temporal Server v1.21, you can set up [Dual Visibility](/dual-visibility) to migrate your Visibility store from one database to another.

## Visibility features {/* #advanced-visibility */}

Visibility enables the listing, filtering, and sorting of [Workflow Executions](/workflow-execution) through a custom SQL-like [List Filter](/list-filter).

Visibility supports [custom Search Attributes](/search-attribute#custom-search-attribute) for user-defined filtering beyond the default system attributes.

- On SQL databases (MySQL v8.0.17+, PostgreSQL v12+), Visibility is available with Temporal Server v1.20 and later.
- On Elasticsearch (v7+ with Temporal Server v1.7+, v8 with Temporal Server v1.18+) and OpenSearch (2+ with Temporal Server v1.30.1+).
- On Temporal Cloud, Visibility is enabled by default for [all users](/cloud/users#invite-users).

For self-hosted setup and version compatibility details, see [Visibility store setup](/self-hosted-guide/visibility).

### Count Workflow by ExecutionStatus

The Count API feature lets you count the number of Workflows that match a given query. For example, the command `temporal workflow count -q "WorkflowType='foo'"` returns the number of Workflows that match `WorkflowType='foo'`.

You can send queries to the Count API to group by a given search attribute. For example, `-q "WorkflowType='foo' GROUP BY ExecutionStatus` returns the number of Workflows that match `WorkflowType='foo'` grouped by `ExecutionStatus`.

The `GROUP BY` clause is only supported in the Count API and currently only grouping by `ExecutionStatus` is supported.

:::note

The Count API returns approximate counts.

:::

## Legacy: standard Visibility {/* #standard-visibility */}

Prior to Temporal Server v1.20, Temporal had two Visibility modes: "standard" and "advanced." Standard Visibility supported only predefined filters such as Workflow Type, Workflow Id, Run Id, and Execution Status, without custom Search Attributes. Advanced Visibility required Elasticsearch.

Starting with Temporal Server v1.20, advanced Visibility became available on SQL databases. Standard Visibility was deprecated in v1.21 and removed in v1.24. All current deployments use what was formerly called advanced Visibility, now simply called Visibility.

If you are running a Temporal Server version older than v1.24, see the [legacy standard Visibility section](/self-hosted-guide/visibility#legacy-standard-visibility) in the self-hosted guide.

---

## Worker versioning (legacy)

:::tip Support, stability, and dependency info

- This document refers to the 2023 draft of Worker Versioning, which was deprecated
- It was not made available in Temporal Cloud
- The 2024 draft was available in Cloud on an opt-in basis, and is documented in this [Pre-release README.md](https://github.com/temporalio/temporal/blob/main/docs/worker-versioning.md).

For newer revisions of this feature set, please see [Worker Versioning](/production-deployment/worker-deployments/worker-versioning) instead.

:::

Worker Versioning simplifies the process of deploying changes to [Workflow Definitions](/workflow-definition).
It does this by letting you define sets of versions that are compatible with each other, and then assigning a Build ID to the code that defines a Worker.
The Temporal Server uses the Build ID to determine which versions of a Workflow Definition a Worker can process.

We recommend that you read about Workflow Definitions before proceeding, because Workflow Versioning is largely concerned with helping to manage nondeterministic changes to those definitions.

Worker Versioning helps manage nondeterministic changes by providing a convenient way to ensure that [Workers](/workers) with different Workflow and Activity Definitions operating on the same Task Queue don't attempt to process [Workflow Tasks](/tasks#workflow-task) and [Activity Tasks](/tasks#activity-task-execution) that they can't successfully process, according to sets of versions associated with that Task Queue that you've defined.

Accomplish this goal by assigning a Build ID (a free-form string) to the code that defines a Worker, and specifying which Build IDs are compatible with each other by updating the version sets associated with the Task Queue, stored by the Temporal Server.

### When and why you should use Worker Versioning

:::caution

This section is for a deprecated Worker Versioning API. Please redirect your attention to [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

:::

The main reason to use this feature is to deploy incompatible changes to short-lived [Workflows](/workflows).
On Task Queues using this feature, the Workflow starter doesn't have to know about the introduction of new versions.

The new code in the newly deployed Workers executes new [Workflow Executions](/workflow-execution), while only Workers with an appropriate version process old Workflow Executions.

#### Decommission old Workers

You can decommission old Workers after you archive all open Workflows using their version.
If you have no need to query closed Workflows, you can decommission them when no open Workflows remain at that version.

For example, if you have a Workflow that completes within a day, a good strategy is to assign a new Build ID to every new Worker build and add it as the new overall default in the version sets.

Because your Workflow completes in a day, you know that you won't need to keep older Workers running for more than a day after you deploy the new version (assuming availability).
You can apply this technique to longer-lived Workflows too; however, you might need to run multiple Worker versions simultaneously while open Workflows complete.

Version sets have a maximum size limit, which defaults to 100 Build IDs across all sets.
Operations to add new Build IDs to the sets will fail if they exceed this limit.
There is also a limit on the number of Version Sets, which defaults to 10.
A version can only be garbage collected after a Workflow Execution is deleted.

#### Deploy code changes to Workers

The feature also lets you implement compatible changes to or prevent a buggy code path from executing on currently open Workflows.
You can achieve this by adding a new version to an existing set and defining it as _compatible_ with an existing version, which shouldn't execute any future Workflow Tasks.
Because the new version processes existing [Event Histories](/workflow-execution/event#event-history), it must adhere to the usual [deterministic constraints](/workflow-definition#deterministic-constraints), and you might need to use one of the [versioning APIs](/workflow-definition#workflow-versioning).

Moreover, this feature lets you make incompatible changes to Activity Definitions in conjunction with incompatible changes to Workflow Definitions that use those Activities.
This functionality works because any Activity that a Workflow schedules on the same Task Queue gets dispatched by default only to Workers compatible with the Workflow that scheduled it.
If you want to change an Activity Definition's type signature while creating a new incompatible Build ID for a Worker, you can do so without worrying about the Activity failing to execute on some other Worker with an incompatible definition.
The same principle applies to Child Workflows.
For both Activities and Child Workflows, you can override the default behavior and run the Activity or Child Workflow on latest default version.

:::tip

Public-facing Workflows on a versioned Task Queue shouldn't change their signatures because doing so contradicts the purpose of Workflow-launching Clients remaining unaware of changes in the Workflow Definition.
If you need to change a Workflow's signature, use a different Workflow Type or a completely new Task Queue.

:::

:::note

If you schedule an Activity or a Child Workflow on _a different_ Task Queue from the one the Workflow runs on, the system doesn't assign a specific version.
This means if the target queue is versioned, they run on the latest default, and if it's unversioned, they operate as they would have without this feature.

:::

**Continue-As-New and Worker Versioning**

By default, a versioned Task Queue's Continue-as-New function starts the continued Workflow on the same compatible set as the original Workflow.

If you continue-as-new onto a different Task Queue, the system doesn't assign any particular version.
You also have the option to specify that the continued Workflow should start using the Task Queue's latest default version.

### How to use Worker Versioning

:::caution

This section is for a deprecated Worker Versioning API. See [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

:::

To use Worker Versioning, follow these steps:

1. Define Worker build-identifier version sets for the Task Queue.
   You can use either the Temporal CLI or your choice of SDK.
2. Enable the feature on your Worker by specifying a Build ID.

#### Defining the version sets

Whether you use [Temporal CLI](/cli/) or an SDK, updating the version sets feels the same.
You specify the Task Queue that you're targeting, the Build ID that you're adding (or promoting), whether it becomes the new default version, and any existing versions it should be considered compatible with.

The rest of this section uses updates to one Task Queue's version sets as examples.

By default, both Task Queues and Workers are in an unversioned state.
[Unversioned Worker](#unversioned-workers) can poll unversioned Task Queues and receive tasks.
To use this feature, both the Task Queue and the Worker must be associated with Build IDs.

If you run a Worker using versioning against a Task Queue that has not been set up to use versioning (or is missing that Worker's Build ID), it won't get any tasks.
Likewise, an unversioned Worker polling a Task Queue with versioning won't work either.

:::note Versions don't need to follow semver or any other semantic versioning scheme!

The versions in the following examples look like semver versions for clarity, but they don't need to be.
Versions can be any arbitrary string.

:::

First, add a version `1.0` to the Task Queue as the new default.
Your version sets now look like this:

| set 1 (default) |
| --------------- |
| 1.0 (default)   |

All new Workflows started on the Task Queue have their first tasks assigned to version `1.0`.
Workers with their Build ID set to `1.0` receive these Tasks.

If Workflows that don't have an assigned version are still running on the Task Queue, Workers without a version take those tasks.
So ensure that such Workers are still operational if any Workflows were open when you added the first version.
If you deployed any Workers with a _different_ version, those Workers receive no Tasks.

Now, imagine you need to change the Workflow for some reason.

Add `2.0` to the sets as the new default:

| set 1         | set 2 (default) |
| ------------- | --------------- |
| 1.0 (default) | 2.0 (default)   |

All new Workflows started on the Task Queue have their first tasks assigned to version `2.0`.
Existing `1.0` Workflows keep generating tasks targeting `1.0`.
Each deployment of Workers receives their respective Tasks.
This same concept carries forward for each new incompatible version.

Maybe you have a bug in `2.0`, and you want to make sure all open `2.0` Workflows switch to some new code as fast as possible.
So, you add `2.1` to the sets, marking it as compatible with `2.0`.
Now your sets look like this:

| set 1         | set 2 (default) |
| ------------- | --------------- |
| 1.0 (default) | 2.0             |
|               | 2.1 (default)   |

All new Workflow Tasks that are generated for Workflows whose last Workflow Task completion was on version `2.0` are now assigned to version `2.1`.
Because you specified that `2.1` is compatible with `2.0`, Temporal Server assumes that Workers with this version can process the existing Event Histories successfully.

Continue with your normal development cycle, adding a `3.0` version.
Nothing new here:

| set 1         | set 2         | set 3 (default) |
| ------------- | ------------- | --------------- |
| 1.0 (default) | 2.0           | 3.0 (default)   |
|               | 2.1 (default) |                 |

Now imagine that version `3.0` doesn't have an explicit bug, but something about the business logic
is less than ideal.
You are okay with existing `3.0` Workflows running to completion, but you want new Workflows to use the old `2.x` branch.
This operation is supported by performing an update targeting `2.1` (or `2.0`) and setting its set as the current default, which results in these sets:

| set 1         | set 3         | set 2 (default) |
| ------------- | ------------- | --------------- |
| 1.0 (default) | 3.0 (default) | 2.0             |
|               |               | 2.1 (default)   |

Now new Workflows start on `2.1`.

#### Permitted and forbidden operations on version sets

A request to change the sets can do one of the following:

- Add a version to the sets as the new default version in a new overall-default compatible set.
- Add a version to an existing set that's compatible with an existing version.
  - Optionally making it the default for that set.
  - Optionally making that set the overall-default set.
- Promote a version within an existing set to become the default for that set.
- Promote a set to become the overall-default set.

You can't explicitly delete versions. This helps you avoid the situation in which Workflows accidentally become stuck with no means of making progress because the version they're associated with no longer exists.

However, sometimes you might want to do this intentionally.
If you _want_ to make sure that all Workflows currently being processed by, say, `2.0` stop (even if you don't yet have a new version ready), you can add a new version `2.1` to the sets marked as compatible with `2.0`.
New tasks will target `2.1`, but because you haven't deployed any `2.1` Workers, they won't make any progress.

#### Set constraints

The sets have a maximum size limit, which defaults to 100 build IDs across all sets.
This limit is configurable on Temporal Server via the `limit.versionBuildIdLimitPerQueue` dynamic config property.
Operations to add new Build IDs to the sets fail if the limit would be exceeded.

There is also a limit on the number of sets, which defaults to 10.
This limit is configurable via the `limit.versionCompatibleSetLimitPerQueue` dynamic config property.

In practice, these limits should rarely be a concern because a version is no longer needed after no open Workflows are using that version, and a background process will delete IDs and sets that are no longer needed.

There is also a limit on the size of each Build ID or version string, which defaults to 255 characters.
This limit is configurable on the server via the `limit.workerBuildIdSize` dynamic config property.

### Build ID reachability

:::caution

This section is for a deprecated Worker Versioning API. See [Worker Versioning](/production-deployment/worker-deployments/worker-versioning).

:::

Eventually, you'll want to know whether you can retire the old Worker versions.
Temporal provides functionality to help you determine whether a version is still in use by open or closed Workflows.
You can use the Temporal CLI to do this with the following command:

```command
temporal task-queue get-build-id-reachability
```

The command determines, for each Task Queue, whether the Build ID in question is unreachable, only reachable by closed Workflows, or reachable by open and new Workflows.
For example, this "2.0" Build ID is shown here by the Temporal CLI to be reachable by both new Workflows and some existing Workflows:

```command
temporal task-queue get-build-id-reachability --build-id "2.0"
```

```output
BuildId                         TaskQueue                                   Reachability
    2.0  build-id-versioning-dc0068f6-0426-428f-b0b2-703a7e409a97  [NewWorkflows
                                                                   ExistingWorkflows]
```

For more information, see the [CLI documentation](/cli/) or help output.

You can also use this API `GetWorkerTaskReachability` directly from within language SDKs.

### Unversioned Workers

Unversioned Workers refer to Workers that have not opted into the Worker Versioning feature in their configuration.
They receive tasks only from Task Queues that do not have any version sets defined on them, or that have open Workflows that began executing before versions were added to the queue.

To migrate from an unversioned Task Queue, add a new default Build ID to the Task Queue.
From there, deploy Workers with the same Build ID.
Unversioned Workers will continue processing open Workflows, while Workers with the new Build ID will process new Workflow Executions.

---

## Serverless Workers

<ReleaseNoteHeader
  featureName="serverlessWorkers"
>
  To request access during Pre-release, create a [support ticket](/cloud/support#support-ticket) or contact your account team. APIs are experimental and may be subject to backwards-incompatible changes. [Sign up for updates](https://temporal.io/pages/serverless-workers-updates) to be notified when Serverless Workers reach Public Preview.
</ReleaseNoteHeader>

This page covers the following:

- [What is a Serverless Worker?](#serverless-worker)
- [How Serverless invocation works](#how-invocation-works)
- [Autoscaling](#autoscaling)
- [Scaling with long-lived Workers](#scaling-with-long-lived-workers)
- [Worker lifecycle](#worker-lifecycle)
- [Failure handling](#failure-handling)
- [Constraints](#constraints)
- [Compute providers](#compute-providers)

## What is a Serverless Worker? {/* #serverless-worker */}

A Serverless Worker is a Temporal Worker that runs on serverless compute instead of a long-lived process. There is no
always-on infrastructure to provision or scale. Temporal invokes the Worker when Tasks arrive on a Task Queue, and the
Worker shuts down when the work is done.

A Serverless Worker uses the same Temporal SDKs as a traditional long-lived Worker. It registers Workflows and
Activities the same way. The difference is in the lifecycle: instead of the Worker starting and polling continuously,
Temporal invokes the Serverless Worker on demand, the Worker starts, processes available Tasks, and then shuts down.

Serverless Workers require [Worker Versioning](/worker-versioning). Each Serverless Worker must be associated with a
[Worker Deployment Version](/worker-versioning#deployment-versions) that has a compute provider configured.

To deploy a Serverless Worker, see
[Deploy a Serverless Worker](/production-deployment/worker-deployments/serverless-workers).

## How Serverless invocation works {/* #how-invocation-works */}

With long-lived Workers, you start the Worker process, which connects to Temporal and polls a Task Queue for work.
Temporal does not need to know anything about the Worker's infrastructure.

With Serverless Workers, Temporal starts the Worker.

### Worker Controller Instance {/* #worker-controller-instance */}

The Worker Controller Instance (WCI) is a system Workflow that scales Serverless Workers based on Task Queue conditions.
One WCI Workflow runs per Worker Deployment Version that has a compute provider configured. The WCI runs in the same
Namespace as your Worker Deployment.

The WCI responds to two triggers: [sync match failures](#sync-match-failure) and
[Task Queue backlog](#task-queue-backlog). When either trigger fires, the WCI produces a scaling action, such as
invoking the configured compute provider (for example, calling AWS Lambda's `InvokeFunction` API) to start new Workers.
For details on how scaling works, see [Autoscaling](#autoscaling).

You can list WCI Workflows in your Namespace:

```bash
temporal workflow list \
  --namespace <NAMESPACE> \
  --query 'TemporalNamespaceDivision = "TemporalWorkerControllerInstance"'
```

WCI Workflow IDs follow the pattern `temporal-sys-worker-controller-instance:<deployment-name>:<build-id>`. You can
inspect a WCI Workflow's history to see its recent Activity results:

```bash
temporal workflow show \
  --namespace <NAMESPACE> \
  --workflow-id 'temporal-sys-worker-controller-instance:<DEPLOYMENT_NAME>:<BUILD_ID>'
```

The following diagram illustrates the invocation flow of a Serverless Worker.

<CaptionedImage
  src="/diagrams/serverless-worker-flow.svg"
  srcDark="/diagrams/serverless-worker-flow-dark.svg"
  alt="Serverless invocation flow"
  title="Temporal's Worker Controller Instance invokes a Serverless Worker when Tasks arrive on a Task Queue with a compute provider configured."
/>

The invocation flow works as follows:

1. A Task is submitted (for example, `StartWorkflow` or `ScheduleActivity`).
2. The [Matching Service](/temporal-service/temporal-server#matching-service) attempts to route the Task directly to an
