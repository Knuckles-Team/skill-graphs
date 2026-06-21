# Default values for a Namespace if none are provided at creation
namespaceDefaults:
  # Archival defaults
  archival:
    # Event History defaults
    history:
      state: 'enabled'
      # New Namespaces will default to the local provider
      URI: 'file:///tmp/temporal_archival/development'
```

You can disable Archival by setting `archival.history.state` and `namespaceDefaults.archival.history.state` to
`"disabled"`.

Example:

```yaml
archival:
  history:
    state: 'disabled'

namespaceDefaults:
  archival:
    history:
      state: 'disabled'
```

The following table shows the available configuration options and their accepted values:

| Config                                         | Acceptable values                                                                  | Description                                                                                                                  |
| ---------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `archival.history.state`                       | `enabled`, `disabled`                                                              | Must be `enabled` to use the Archival feature with any Namespace in the Temporal Service.                                    |
| `archival.history.enableRead`                  | `true`, `false`                                                                    | Must be `true` to read from the archived Event History.                                                                      |
| `archival.history.provider`                    | Sub provider configs are `filestore`, `gstorage`, `s3`, or `your_custom_provider`. | Default config specifies `filestore`.                                                                                        |
| `archival.history.provider.filestore.fileMode` | File permission string                                                             | File permissions of the archived files. We recommend using the default value of `"0666"` to avoid read/write issues.         |
| `archival.history.provider.filestore.dirMode`  | File permission string                                                             | Directory permissions of the archive directory. We recommend using the default value of `"0766"` to avoid read/write issues. |
| `namespaceDefaults.archival.history.state`     | `enabled`, `disabled`                                                              | Default state of the Archival feature whenever a new Namespace is created without specifying the Archival state.             |
| `namespaceDefaults.archival.history.URI`       | Valid URI                                                                          | Must be a URI of the file store location and match a schema that correlates to a provider.                                   |

Additional resources: [Temporal Service configuration reference](/references/configuration).

#### Create an Archiving Namespace {/* #create-an-archiving-namespace */}

Although Archival is configured at the Temporal Service level, it operates independently within each Namespace. If you
don't specify an Archival URI during Namespace creation, the Namespace uses `namespaceDefaults.archival.history.URI`
from `config/development.yaml`. The Archival URI cannot be changed after the Namespace is created. Each Namespace
supports only a single Archival URI, but each Namespace can use a different URI. A Namespace can safely switch Archival
between `enabled` and `disabled` states as long as Archival is enabled at the Temporal Service level.

Archival is supported in [Global Namespaces](/global-namespace) (Namespaces that span multiple clusters). When Archival
is running in a Global Namespace, it first runs on the active cluster; later it runs on the standby cluster. Before
archiving, a history check is done to see what has been previously archived.

#### Test your Archival setup {/* #test-your-archival-setup */}

To test Archival locally, start by running a Temporal server:

```bash
./temporal-server start
```

Then register a new Namespace with Archival enabled.

{/* ./tctl --ns samples-namespace namespace register --gd false --history_archival_state enabled --retention 3 */}

```bash
./temporal operator namespace create --namespace="my-namespace" --global false --history-archival-state="enabled" --retention="4d"
```

:::note

If the retention period isn't set, it defaults to 72h. The minimum retention period is one day. For retention maximums,
check [Temporal Service Retention Period limits](/temporal-service/temporal-server#retention-period) for your server
version.

Setting the retention period to 0 results in the error _A valid retention period is not set on request_.

:::

Next, run a sample Workflow such as the
[helloworld temporal sample](https://github.com/temporalio/samples-go/tree/main/helloworld).

When the Workflow Execution closes, Temporal schedules archival processing.

#### Retrieve archived history {/* #retrieve-archived-history */}

You can retrieve archived Event Histories by copying the `workflowId` and `runId` of the completed Workflow from the log
output and running the following command:

{/* ./tctl --ns samples-namespace wf show --wid <workflowId> --rid <runId> */}

```bash
./temporal workflow show --workflow-id="my-workflow-id" --run-id="my-run-id" --namespace="my-namespace"
```

### Create a custom Archiver {/* #custom-archiver */}

To archive data with a given provider, using the [Archival](/temporal-service/archival) feature, Temporal must have a
corresponding Archiver component installed. The platform does not limit you to the existing providers. To use a provider
that is not currently supported, you can create your own Archiver.

#### Create a new package

The first step is to create a new package for your implementation in
[/common/archiver](https://github.com/temporalio/temporal/tree/main/common/archiver). Create a directory in the archiver
folder and arrange the structure to look like the following:

```
temporal/common/archiver
  - filestore/                      -- Filestore implementation
  - provider/
      - provider.go                 -- Provider of archiver instances
  - yourImplementation/
      - historyArchiver.go          -- HistoryArchiver implementation
      - historyArchiver_test.go     -- Unit tests for HistoryArchiver
      - visibilityArchiver.go       -- VisibilityArchiver implementations
      - visibilityArchiver_test.go  -- Unit tests for VisibilityArchiver
```

#### Archiver interfaces

Next, define objects that implement the
[HistoryArchiver](https://github.com/temporalio/temporal/blob/main/common/archiver/interface.go#L80) and the
[VisibilityArchiver](https://github.com/temporalio/temporal/blob/main/common/archiver/interface.go#L121) interfaces.

The objects should live in `historyArchiver.go` and `visibilityArchiver.go`, respectively.

#### Update provider

Update the `GetHistoryArchiver` and `GetVisibilityArchiver` methods of the `archiverProvider` object in the
[/common/archiver/provider/provider.go](https://github.com/temporalio/temporal/blob/main/common/archiver/provider/provider.go)
file so that it knows how to create an instance of your archiver.

#### Add configs

Add configs for your archiver to the `config/development.yaml` file and then modify the
[HistoryArchiverProvider](https://github.com/temporalio/temporal/blob/main/common/config/config.go#L376) and
[VisibilityArchiverProvider](https://github.com/temporalio/temporal/blob/main/common/config/config.go#L393) structs in
`/common/common/config.go` accordingly.

#### Custom archiver FAQ

**If my custom Archive method can automatically be retried by the caller, how can I record and access progress between
retries?**

Handle this situation by using `ArchiverOptions`. Here is an example:

```go
func(a * Archiver) Archive(ctx context.Context, URI string, request * ArchiveRequest, opts...ArchiveOption) error {
    featureCatalog: = GetFeatureCatalog(opts...) // this function is defined in options.go
    var progress progress
    // Check if the feature for recording progress is enabled.
    if featureCatalog.ProgressManager != nil {
        if err: = featureCatalog.ProgressManager.LoadProgress(ctx, & prevProgress);
        err != nil {
            // log some error message and return error if needed.
        }
    }

    // Your archiver implementation...

    // Record current progress
    if featureCatalog.ProgressManager != nil {
        if err: = featureCatalog.ProgressManager.RecordProgress(ctx, progress);
        err != nil {
            // log some error message and return error if needed.
        }
    }
}
```

**If my `Archive` method encounters an error that is non-retryable, how do I indicate to the caller that it should not
retry?**

```go
func(a * Archiver) Archive(ctx context.Context, URI string, request * ArchiveRequest, opts...ArchiveOption) error {
    featureCatalog: = GetFeatureCatalog(opts...) // this function is defined in options.go

    err: = youArchiverImpl()

    if nonRetryableErr(err) {
        if featureCatalog.NonRetryableError != nil {
            return featureCatalog.NonRetryableError() // when the caller gets this error type back it will not retry anymore.
        }
    }
}
```

**How does my history archiver implementation read history?**

The archiver package provides a utility called
[HistoryIterator](https://github.com/temporalio/temporal/blob/main/common/archiver/historyIterator.go) which is a
wrapper of
[ExecutionManager](https://github.com/temporalio/temporal/blob/main/common/persistence/data_interfaces.go#L1014).
`HistoryIterator` is more simple than the `HistoryManager`, which is available in the BootstrapContainer, so archiver
implementations can choose to use it when reading Workflow histories. See the
[historyIterator.go](https://github.com/temporalio/temporal/blob/main/common/archiver/history_iterator.go) file for more
details. Use the
[filestore historyArchiver implementation](https://github.com/temporalio/temporal/tree/main/common/archiver/filestore)
as an example.

**Should my archiver define its own error types?**

Each archiver is free to define and return its own errors. However, many common errors that exist between archivers are
already defined in
[common/archiver/constants.go](https://github.com/temporalio/temporal/blob/main/common/archiver/constants.go).

**Is there a generic query syntax for the visibility archiver?**

Currently, no. But this is something we plan to do in the future. As for now, try to make your syntax similar to the one
used by our advanced list Workflow API.

- [s3store](https://github.com/temporalio/temporal/tree/main/common/archiver/s3store#visibility-query-syntax)
- [gcloud](https://github.com/temporalio/temporal/tree/main/common/archiver/gcloud#visibility-query-syntax)

---

## Temporal Platform's production readiness checklist

This page describes common challenges customers face who self-host Temporal and it shares recommendations to mitigate those issues.

Temporal at its core is about durability and reliability.
To ensure this durability and reliability, a Temporal Service must be deployed according to best practices.

This guide provides a path to demonstrate that Temporal consumers can be confident in a Temporal Service and provides a list of key tests you as a user should perform against the service.

## Self-Hosting Challenge Areas

Significant engineering and ongoing effort is required to resolve several potential challenges:

- Scalability with spiky or growing workloads
- Global hosting
- Uptime, availability and reliability
- Management and control plane
- Latency, which must be kept low and consistent
- [Security](/self-hosted-guide/security)
- Maintenance and upgrades
- Expert support to users of the service
- Cost management

Each of these components is an essential part of building a mission critical Temporal Service.
Without demonstrated architectural durability, the value of Temporal's [Durable Execution](https://temporal.io/how-it-works) model is compromised.

## Scalability with Variable or Growing Workloads {/* #scaling-and-metrics */}

Workloads can be highly variable, and you may experience sustained workload spikes.
Temporal recommends scaling your clusters to well above the average throughput.
See [Scaling Temporal: The Basics](https://temporal.io/blog/scaling-temporal-the-basics) for an introduction to the topic.

Temporal server throughput is often limited by the number of [Shards](/temporal-service/temporal-server#history-shard) configured for the Temporal Service.
A Shard is a unit within a Temporal Service by which concurrent Workflow Execution throughput can be scaled.
Shard capacity, and often overall cluster throughput, is set at build time for a cluster and that cluster setting cannot be adjusted later.
Adding more Shards if needed requires a cluster rebuild, and a migration to the new cluster.

The requirements of your Temporal Service will vary widely based on your intended production workload.
You will want to run your own proof of concept tests and watch for key metrics to understand the system health and scaling needs.

**Load testing.** You can use [the Omes benchmarking tool](https://github.com/temporalio/omes/), see how we ourselves [stress test Temporal](https://temporal.io/blog/temporal-deep-dive-stress-testing/), or write your own.

All metrics emitted by the server are [listed in Temporal's source](https://github.com/temporalio/temporal/blob/main/common/metrics/defs.go).
There are also equivalent metrics that you can configure from the client side.
At a high level, you will want to track these 3 categories of metrics:

- **Service metrics**: For each request made by the service handler we emit `service_requests`, `service_errors`, and `service_latency` metrics with `type`, `operation`, and `namespace` tags.
  This gives you basic visibility into service usage and allows you to look at request rates across services, namespaces and even operations.
- **Persistence metrics**: The Server emits `persistence_requests`, `persistence_errors` and `persistence_latency` metrics for each persistence operation.
  These metrics include the `operation` tag such that you can get the request rates, error rates or latencies per operation.
  These are super useful in identifying issues caused by the database.
- **Workflow Execution stats**: The Server also emits counters for when Workflow Executions are complete.
  These are useful in getting overall stats about Workflow Execution completions.
  Use `workflow_success`, `workflow_failed`, `workflow_timeout`, `workflow_terminate` and `workflow_cancel` counters for each type of Workflow Execution completion.
  These include the `namespace` tag.

## Availability

A high level of availability and reliability (99.99%) is a requirement for mission critical deployments.
Temporal recommends testing for this availability level while load testing.
We also recommend validating this level of reliability while doing server upgrades, to ensure no loss of service availability.

Temporal Clusters can be deployed in as many regions as needed to meet various requirements:

- Data Residency
- Latency
- Security / Isolation
  This can multiply the effort to implement and maintain clusters.

[Temporal Cloud is available in various cloud provider regions](/cloud/service-availability).

## Management and Control Plane

Temporal success leads to larger Temporal deployments.
Needs can increase, and can go from having one or two production use cases in a single region to many use cases in many regions.
Running multiple Temporal Services is complex work, as each needs its own setup, tuning, and configuration.

Needing to monitor and manage all your Temporal Services in a unified way leads to operational management pain.
Consider adding a layer on top of Temporal to manage multiple Temporal Services: a control plane.
A control plane manages and directs data flow, deciding where data packets should be sent.
A Temporal Service data plane can streamline operations and improve efficiency.
Since Temporal does not ship its own open source data plane, rolling your own can be complex and take effort to add.

Temporal Cloud provides exactly that support.
With Temporal Cloud, all Namespaces in all regions can be managed from a single view.
[Temporal Cloud](https://temporal.io/cloud) also has RBAC functionality that can delegate responsibilities for individual Namespaces.

Self-hosted Temporal does not support RBAC or audit logging out of the box.
Temporal Cloud provides RBAC and SSO support, audit logging, data encryption, third party penetration test validation, and SOC 2-Type II and HIPAA compliance.

## Maintenance and Upgrades

Temporal recommends keeping up-to-date and not falling behind on your server versions.

Temporal Server is proactively updated, and releases as often as every two weeks.
Temporal recommends [upgrading sequentially](/self-hosted-guide/upgrade-server), not skipping any minor versions, although you can skip patch versions.
No support is guaranteed for Temporal Server, but very old servers will be hard for even the community to support, so we encourage you to keep up to date.
You must create and maintain the infrastructure to host and run your self-hosted Temporal installation, such as Kubernetes, as well as data stores for persistence.

Server upgrades can negatively affect self-hosted Temporal Service availability.
Temporal recommends load and availability testing during the upgrade process to understand the performance implications.

Temporal Cloud updates are managed by the Temporal Cloud team; Cloud upgrades are seamless.

## Expert Support

Temporal recommends that customer platform teams who are building out a Temporal service gain deep experience across the lifecycle and breadth of a Temporal application.

Specific activities include:

- [Worker tuning](/develop/worker-performance)
- [Worker best practices](/workers)
- Code reviews
- Design guidance
- Training
- Code reviews
- Security reviews
- [Metrics](/references/sdk-metrics) and monitoring
- Technical onboarding

[Temporal support](/cloud/support) provides guidance on all of the above.

## Cost Management

Running a mission critical, global Temporal Service can be expensive.
Temporal Server is a complex system to run and scale.
Temporal recommends performance testing and planning scaling as your performance requirements evolve.
Following our guidance can oversize your self-hosted Temporal Server installs, but this is necessary to handle unpredictable spiky workloads.
Performance testing can help you right-size your environments.
Running mission critical Temporal as a Service requires multiple Temporal Clusters for high availability and global coverage.

It is a good practice to have trained, experienced administrators familiar with Temporal Service architecture to maintain your Temporal servers and provide a mission critical service.
Staffing, training and skill development can be significant costs to maintaining a Temporal Service.

[Temporal Cloud](https://temporal.io/cloud) can be significantly less expensive to set up and scale.

---

## Self-hosted Temporal Service defaults

:::info Looking for Temporal Cloud defaults?

See the [Temporal Cloud defaults and limits page](/cloud/limits)

:::

This page details many of the defaults coded into the Temporal Platform that can produce errors and warnings.
Errors are hard limits that fail when reached.
Warnings are soft limits that produce a warning log on the server side.

:::info

These limits might apply specifically to each Workflow Execution and do not pertain to the entire Temporal Platform or individual Namespaces.

:::

- **Identifiers:** By default, the maximum length for identifiers (such as Workflow Id, Workflow Type, and Task Queue name) is 1000 characters.
  - This is configurable with the `limit.maxIDLength` dynamic config variable, set to 255 in [this SQL example](https://github.com/temporalio/samples-server/blob/main/compose/dynamicconfig/development-sql.yaml).
  - The character format is UTF-8.
- **gRPC:** gRPC has a limit of 4 MB for [each message received](https://github.com/grpc/grpc/blob/v1.36.2/include/grpc/impl/codegen/grpc_types.h#L466).
- **Event batch size:** The `DefaultTransactionSizeLimit` limit is [4 MB](https://github.com/temporalio/temporal/pull/1363).
  This is the largest transaction size allowed for the persistence of Event Histories.
- **Blob size limit** for Payloads (including Workflow context and each Workflow and Activity argument and return value; _[source](https://github.com/temporalio/temporal/blob/v1.7.0/service/frontend/service.go#L133-L134)_):
  - Temporal warns at 256 KB: `Blob size exceeds limit.`
  - Temporal errors at 2 MB: `ErrBlobSizeExceedsLimit: Blob data size exceeds limit.`
  - Refer to [Troubleshoot blob size limit error](/troubleshooting/blob-size-limit-error).
- **Workflow Execution Update limits**:
  - A single Workflow Execution can have a maximum of 10 in-flight Updates and 2000 total Updates in History.
- **History total size limit** (leading to a terminated Workflow Execution):
  - Temporal warns at 10 MB: [history size exceeds warn limit](https://github.com/temporalio/temporal/blob/v1.7.0/service/history/workflowExecutionContext.go#L1238).
  - Temporal errors at 50 MB: [history size exceeds error limit](https://github.com/temporalio/temporal/blob/v1.7.0/service/history/workflowExecutionContext.go#L1204).
  - This is configurable with [HistorySizeLimitError and HistorySizeLimitWarn](https://github.com/temporalio/temporal/blob/v1.7.0/service/history/configs/config.go#L380-L381).
- **History total count limit** (leading to a terminated Workflow Execution):
  - Temporal warns after 10,240 Events: [history size exceeds warn limit](https://github.com/temporalio/temporal/blob/v1.7.0/service/history/workflowExecutionContext.go#L1238).
  - Temporal errors after 51,200 Events: [history size exceeds error limit](https://github.com/temporalio/temporal/blob/v1.7.0/service/history/workflowExecutionContext.go#L1204).
  - This is configurable with [HistoryCountLimitError and HistoryCountLimitWarn](https://github.com/temporalio/temporal/blob/v1.7.0/service/history/configs/config.go#L382-L383).
- **Concurrent limit**
  - The following Commands are limited:
    - `ScheduleActivityTask`
    - `SignalExternalWorkflowExecution`
    - `RequestCancelExternalWorkflowExecution`
    - `StartChildWorkflowExecution`
  - These will fail if the concurrent pending count exceeds 2,000.
    For optimal performance, limit concurrent operations to 500 or fewer.
    This reduces Workflow's Event History size and decreases the loading time in the Web UI.
  - As of v1.21, the open source Temporal Service has a default limit of 2,000 pending Activities, Child Workflows, Signals, or Workflow cancellation requests, but you can override the limits in the dynamic configuration using these variables:
    - `limit.numPendingActivities.error`
    - `limit.numPendingSignals.error`
    - `limit.numPendingCancelRequests.error`
    - `limit.numPendingChildExecutions.error`
  - By default, [Batch jobs](/cli/command-reference/batch) are limited to one job at a time.
- [Custom Search Attributes limits](/search-attribute#custom-search-attribute-limits)

For details on dynamic configuration keys, see [Dynamic configuration reference](/references/dynamic-configuration).

---

## Deploying a Temporal Service

There are many ways to self-host a [Temporal Service](/temporal-service). The right way for you depends entirely on your
use case and where you plan to run it.

This page provides instructions for deploying a Temporal Service for sustained workloads that exceed what the
[development server](/cli#start-a-development-server) is designed to handle. For local development or testing, you can use the
Temporal CLI to [start a local development Temporal Service](/cli#start-a-development-server).

:::warning Temporal Hosts Should Not Be Exposed to the Open Internet

In self-hosted deployments, the Temporal Service is a critical control and persistence component and should be secured
similarly to a database. Temporal services should run on hosts that are not accessible from the public internet, with
network configurations that restrict access to trusted internal networks only.

:::

For step-by-step guides on deploying and configuring Temporal, refer to our
[Infrastructure tutorials](https://learn.temporal.io/tutorials/infrastructure/).

## Use Docker Compose

You can run a Temporal Service in [Docker](https://docs.docker.com/engine/install) containers using
[Docker Compose](https://docs.docker.com/compose/install).

### Prerequisites

- You have Docker Compose installed.
- Docker is running and the daemon is available.
- Git is installed and available.

### Procedure

1. Clone the [temporalio/samples-server](https://github.com/temporalio/samples-server) repository.

2. Change into the `compose` directory.

   ```
   cd samples-server/compose
   ```

3. Run the `docker compose up` command. This uses the default configuration from the `docker-compose.yaml` file, which
   includes a PostgreSQL database, an Elasticsearch instance, and exposes the Temporal gRPC Frontend on port 7233.

   ```
   docker compose up
   ```

   The Temporal Web UI will be available at `http://localhost:8080`.

4. (Optional) Review
