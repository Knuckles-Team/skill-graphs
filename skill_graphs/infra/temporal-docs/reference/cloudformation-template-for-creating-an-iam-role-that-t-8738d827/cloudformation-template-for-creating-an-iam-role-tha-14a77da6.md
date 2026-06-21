Measures the in-memory latency across multiple attempts.

### `task_latency_queue`

Measures the duration, end-to-end, from when the Task should be executed (from the time it was fired) to when the Task is done.

### `task_latency_load`

(Available only in v1.18.0+) Measures the duration from Task generation to Task loading (Task schedule to start latency for persistence queue).

### `task_latency_schedule`

(Available only in v1.18.0+) Measures the duration from Task submission (to the Task scheduler) to processing (Task schedule to start latency for in-memory queue).

### `queue_latency_schedule`

(Available only in v1.18.0+) Measures the time to schedule 100 Tasks in one Task channel in the host-level Task scheduler.
If fewer than 100 Tasks are in the Task channel for 30 seconds, the latency is scaled to 100 Tasks upon emission.
Note: This is still an experimental metric and is subject to change.

### `service_latency_userlatency`

Shows the latency introduced because of Workflow logic.
For example, if you have one Workflow scheduling many Activities or Child Workflows at the same time, it can cause a per-Workflow lock contention.
The wait period for the per-Workflow lock is counted as `userlatency`.

The `operation` tag contains details about Task type and Active versus Standby statuses, and can be used to get request rates, error rates, or latencies per operation, which can help identify issues caused by database problems.

## Persistence metrics

Temporal Server emits metrics for every persistence database read and write.
Some of the most important ones are the following:

### `persistence_requests`

Emitted on every persistence request.
Examples:

- Prometheus query for getting the total number of persistence requests by operation for the History Service:
  `sum by (operation) (rate(persistence_requests{service_name="history"}[1m]))`
- Prometheus query for getting the total number of persistence requests by operation for the Matching Service:
  `sum by (operation) (rate(persistence_requests{service_name="matching"}[1m]))`

### `persistence_errors`

Shows all persistence errors.
This metric is a good indicator for connection issues between the Temporal Service and the persistence store.
Example:

- Prometheus query for getting all persistence errors by service (history)
  `sum (rate(persistence_errors{service_name="history"}[1m]))`

### `persistence_error_with_type`

Shows all errors related to the persistence store with type, and contain an `error_type` tag.

- Prometheus query for getting persistence errors with type by (history) and by error type:
  `sum(rate(persistence_error_with_type{service_name="history"}[1m])) by (error_type)`

### `persistence_latency`

Shows the latency on persistence operations.
Example:

- Prometheus query for getting latency by percentile:
  `histogram_quantile(0.95, sum(rate(persistence_latency_bucket{service_name="history"}[1m])) by (operation, le))`

## Schedule metrics

Temporal emits metrics that track the performance and outcomes of these Scheduled Executions.

Below are additional metrics that can help you monitor and optimize your Scheduled Workflow Executions.

### `schedule_buffer_overruns`

Indicates instances where the buffer for holding Scheduled Workflows exceeds its maximum capacity.
This scenario typically occurs when schedules with a `buffer_all` overlap policy have their average run length exceeding the average schedule interval.

Example: To monitor buffer overruns.

`sum(rate(schedule_buffer_overruns{namespace="$namespace"}[5m]))`

### `schedule_missed_catchup_window`

Tracks occurrences when the system fails to execute a Scheduled Action within the defined catchup window.
Missed catchup windows can result from extended outages beyond the configured catchup period.

Example: To identify missed catchup opportunities.

`sum(rate(schedule_missed_catchup_window{namespace="$namespace"}[5m]))`

### `schedule_rate_limited`

Reflects instances where the creation of Workflows by a Schedule is throttled due to rate limiting policies within a Namespace.
This metric is crucial for identifying scheduling patterns that frequently hit rate limits, potentially causing missed catchup windows.

Example: To assess the impact of rate limiting on Scheduled Executions.

`sum(rate(schedule_rate_limited{namespace="$namespace"}[5m]))`

### `schedule_action_success`

Measures the successful execution of Workflows as per their schedules or through manual triggers.
This metric confirms that Workflows are running as expected without delays or errors.

Example: To track the success rate of Scheduled Workflow Executions.

`sum(rate(schedule_action_success{namespace="$namespace"}[5m]))`

## Workflow metrics

These metrics pertain to Workflow statistics.

### `workflow_cancel`

Number of Workflows canceled before completing execution.

### `workflow_continued_as_new`

Number of Workflow Executions that were Continued-As-New from a past execution.

### `workflow_failed`

Number of Workflows that failed before completion.

### `workflow_success`

Number of Workflows that successfully completed.

### `workflow_timeout`

Number of Workflows that timed out before completing execution.

## Nexus metrics

These metrics pertain to Nexus Operations.

### Nexus Machinery in the History Service

See [architecture document](https://github.com/temporalio/temporal/blob/5d55d6c707bd68d8f3274c57ae702331adf05e6e/docs/architecture/nexus.md#scheduler)
for more info.

#### In-Memory Buffer

`dynamic_worker_pool_scheduler_enqueued_tasks`: A counter that is incremented when a task is enqueued to the buffer.

`dynamic_worker_pool_scheduler_dequeued_tasks`: A counter that is incremented when a task is dequeued from the buffer.

`dynamic_worker_pool_scheduler_rejected_tasks`: A counter that is incremented when the buffer is full and adding the
task is rejected.

`dynamic_worker_pool_scheduler_buffer_size`: A gauge that periodically samples the size of the buffer.

### Concurrency Limiter

`dynamic_worker_pool_scheduler_active_workers`: A gauge that periodically samples the number of running goroutines.

#### Rate Limiter

`rate_limited_task_runnable_wait_time`: A histogram representing the time a task spends waiting for the rate limiter.

#### Circuit Breaker

`circuit_breaker_executable_blocked`: A counter that is incremented every time a task execution is blocked by the
circuit breaker.

#### Task Executors

`nexus_outbound_requests`: A counter representing the number of Nexus outbound requests made by the history service.

`nexus_outbound_latency`: A histogram representing the latency of outbound Nexus requests made by the history service.

`callback_outbound_requests`: A counter representing the number of callback outbound requests made by the history
service.

`callback_outbound_latency`: A histogram representing the latency histogram of outbound callback requests made by the
history service.

### Nexus Machinery on the Frontend Service

#### `nexus_requests`

The number of Nexus requests received by the service.

Type: Counter

#### `nexus_latency`

Latency of Nexus requests.

Type: Histogram

#### `nexus_request_preprocess_errors`

The number of Nexus requests for which pre-processing failed.

Type: Counter

#### `nexus_completion_requests`

The number of Nexus completion (callback) requests received by the service.

Type: Counter

#### `nexus_completion_latency`

Latency histogram of Nexus completion (callback) requests.

Type: Histogram

#### `nexus_completion_request_preprocess_errors`

The number of Nexus completion requests for which pre-processing failed.

Type: Counter

---

## Temporal Commands reference

A [Command](/workflow-execution#command) is a requested action issued by a [Worker](/workers#worker) to the [Temporal Service](/temporal-service) after a [Workflow Task Execution](/tasks#workflow-task-execution) completes.

The following is a complete list of possible Commands.

### CompleteWorkflowExecution

This Command is triggered when the Workflow Function Execution returns.
It indicates to the Temporal Service that the [Workflow Execution](/workflow-execution) is complete.
The corresponding [Event](/workflow-execution/event#event) for this Command is one of the few Events that will be the last in a Workflow Execution [Event History](/workflow-execution/event#event-history).

- Awaitable: No, a Workflow Execution can not await on the action resulting from this Command.
- Corresponding Event: [WorkflowExecutionCompleted](/references/events#workflowexecutioncompleted)

### ContinueAsNewWorkflowExecution

This Command is triggered when there is a call to [Continue-As-New](/workflow-execution/continue-as-new) from within the [Workflow](/workflows).
The corresponding Event for this Command is one of the few Events that will be the last in a Workflow Execution Event History.

- Awaitable: No, a Workflow Execution can not await on the action resulting from this Command.
- Corresponding Event: [WorkflowExecutionContinuedAsNew](/references/events#workflowexecutioncontinuedasnew)

### FailWorkflowExecution

This Command is triggered when the Workflow Execution returns an error or an exception is thrown.

- Awaitable: No, a Workflow Execution can not await on the action resulting from this Command.
- Corresponding Event: [WorkflowExecutionFailed](/references/events#workflowexecutionfailed)

### CancelWorkflowExecution

This Command is triggered when the Workflow has successfully cleaned up after receiving a Cancellation Request (which will be present as [WorkflowExecutionCancelRequestedEvent](/references/events#workflowexecutioncancelrequested) in the Event History).
The Corresponding Event for this Command is one of the few Events that will be the last in a Workflow Execution Event History.

- Awaitable: No, a Workflow Execution can not await on the action resulting from this Command.
- Corresponding Event: [WorkflowExecutionCanceled](/references/events#workflowexecutioncanceled)

### StartChildWorkflowExecution

This Command is triggered by a call to spawn a [Child Workflow Execution](/child-workflows).

- Awaitable: Yes, a Workflow Execution can await on the action resulting from this Command.
- Corresponding Event: [ChildWorkflowExecutionStarted](/references/events#childworkflowexecutionstarted)

By default, you cannot have more than 2,000 pending Child Workflows.

### SignalExternalWorkflowExecution

This Command is triggered by a call to [Signal](/sending-messages#sending-signals) another Workflow Execution.

- Awaitable: Yes, a Workflow Execution can await on the action resulting from this Command.
- Corresponding Event: [SignalExternalWorkflowExecutionInitiated](/references/events#signalexternalworkflowexecutioninitiated)

By default, you cannot have more than 2,000 pending Signals to other Workflows.

### RequestCancelExternalWorkflowExecution

This Command is triggered by a call to request cancellation of another Workflow Execution.

- Awaitable: Yes, a Workflow Execution can await on the action resulting from this Command.
- Corresponding Event: [RequestCancelExternalWorkflowExecutionInitiated](/references/events#requestcancelexternalworkflowexecutioninitiated)

By default, you cannot have more than 2,000 pending Signals to other Workflows.

### ScheduleActivityTask

This Command is triggered by a call to execute an [Activity](/activities).

- Awaitable: Yes, a Workflow Execution can await on the action resulting from this Command.
- Corresponding Event: [ActivityTaskScheduled](/references/events#activitytaskscheduled)

By default, you cannot schedule more than 2,000 Activities concurrently.

### RequestCancelActivityTask

This Command is triggered by a call to request the cancellation of an [Activity Task](/tasks#activity-task).

- Awaitable: No, a Workflow Execution can not await on the action resulting from this Command.
- Corresponding Event: [ActivityTaskCancelRequested](/references/events#activitytaskcancelrequested)

### StartTimer

This Command is triggered by a call to start a Timer.

- Awaitable: Yes, a Workflow Execution can await on the action resulting from this Command.
- Corresponding Event: [TimerStarted](/references/events#timerstarted)

### CancelTimer

This Command is triggered by a call to cancel a Timer.

- Awaitable: No, a Workflow Execution can not await on the action resulting from this Command.
- Corresponding Event: [TimerCanceled](/references/events#timercanceled)

### RecordMarker

This Command is triggered by the SDK.

- Awaitable: No, a Workflow Execution can not await on the action resulting from this Command.
- Corresponding Event: [MarkerRecorded](/references/events#markerrecorded)

### UpsertWorkflowSearchAttributes

This Command is triggered by a call to "upsert" Workflow [Search Attributes](/search-attribute).

- Awaitable: No, a Workflow Execution can not await on the action resulting from this Command.
- Corresponding Event: [UpsertWorkflowSearchAttributes](/references/events#upsertworkflowsearchattributes)

### ProtocolMessageCommand

This Command helps guarantee ordering constraints for features such as Updates.

This Command points at the message from which the Event is created.
Therefore, just from the Command, you can't predict the resulting Event type.

### ScheduleNexusOperation

This Command is triggered by a call to execute a Nexus Operation in the caller Workflow.

- Awaitable: Yes, a Workflow Execution can await on the action resulting from this Command.
- Corresponding Event: [NexusOperationScheduled](/references/events#nexusoperationscheduled)

By default, you can't schedule more than 30 Nexus Operations concurrently, see [Limits](/workflow-execution/limits#workflow-execution-nexus-operation-limits) for details.

### CancelNexusOperation

This Command is triggered by a call to request the cancellation of a Nexus Operation.

- Awaitable: No, a Workflow Execution can not await on the action resulting from this Command.
- Corresponding Event: [NexusOperationCancelRequested](/references/events#nexusoperationcancelrequested)

---

## Temporal Cluster configuration reference

Much of the behavior of a Temporal Cluster is configured using the `development.yaml` file and may contain the following top-level sections:

- [`global`](#global)
- [`persistence`](#persistence)
- [`log`](#log)
- [`clusterMetadata`](#clustermetadata)
- [`services`](#services)
- [`publicClient`](#publicclient)
- [`archival`](#archival)
- [`namespaceDefaults`](#namespacedefaults)
- [`dcRedirectionPolicy`](#dcredirectionpolicy)
- [`dynamicConfigClient`](#dynamicconfigclient)

Changing any properties in the `development.yaml` file requires a process restart for changes to take effect.
Configuration parsing code is available [here](https://github.com/temporalio/temporal/blob/main/common/config/config.go).

## global

The `global` section contains process-wide configuration. See below for a minimal configuration (optional parameters are commented out.)

```yaml
global:
  membership:
    broadcastAddress: '127.0.0.1'
  metrics:
    prometheus:
      framework: 'tally'
      listenAddress: '127.0.0.1:8000'
```

### membership

The `membership` section controls the following membership layer parameters.

#### maxJoinDuration

The amount of time the service will attempt to join the gossip layer before failing.

Default is 10s.

#### broadcastAddress

Used by gossip protocol to communicate with other hosts in the same Cluster for membership info.
Use IP address that is reachable by other hosts in the same Cluster.
If there is only one host in the Cluster, you can use 127.0.0.1.
Check `net.ParseIP` for supported syntax, only IPv4 is supported.

### metrics

Configures the Cluster's metric subsystem.
Specific providers are configured using provider names as the keys.

- [`statsd`](#statsd)
- `prometheus`
- `m3`

#### prefix

The prefix to be applied to all outgoing metrics.

#### tags

The set of key-value pairs to be reported as part of every metric.

#### excludeTags

A map from tag name string to tag values string list.
This is useful to exclude some tags that might have unbounded cardinality.
The value string list can be used to whitelist values of that excluded tag to continue to be included.
For example, if you want to exclude `task_queue` because it has unbounded cardinality, but you still want to see a whitelisted value for `task_queue`.

#### statsd

:::caution

`statsd` is not supported natively by Temporal.

:::

The `statsd` sections supports the following settings:

- `hostPort`: The host:port of the statsd server.
- `prefix`: Specific prefix in reporting to `statsd`.
- `flushInterval`: Maximum interval for sending packets. (_Default_ 300ms).
- `flushBytes`: Specifies the maximum UDP packet size you wish to send. (_Default_ 1432 bytes).

#### prometheus

The `prometheus` sections supports the following settings:

- `framework`: The framework to use, currently supports `opentelemetry` and `tally`, default is `tally`. We plan to switch default to `opentelemetry` once its API become stable.
- `listenAddress`: Address for Prometheus to scrape metrics from.
  The Temporal Server uses the Prometheus client API, and the `listenAddress` configuration is used to listen for metrics.
- `handlerPath`: Metrics handler path for scraper; default is `/metrics`.

#### m3

The `m3` sections supports the following settings:

- `hostPort`: The host:port of the M3 server.
- `service`: The service tag that this client emits.
- `queue`: M3 reporter queue size, default is 4k.
- `packetSize`: M3 reporter max packet size, default is 32k.

### pprof

- `port`: If specified, this will initialize pprof upon process start on the listed port.

### tls

The `tls` section controls the SSL/TLS settings for network communication and contains two subsections, `internode` and `frontend`.
The `internode` section governs internal service communication among roles where the `frontend` governs SDK client communication to the Frontend Service role.

Each of these subsections contain a `server` section and a `client` section.
The `server` contains the following parameters:

- `certFile`: The path to the file containing the PEM-encoded public key of the certificate to use.
- `keyFile`: The path to the file containing the PEM-encoded private key of the certificate to use.
- `requireClientAuth`: _boolean_ - Requires clients to authenticate with a certificate when connecting, otherwise known as mutual TLS.
- `clientCaFiles`: A list of paths to files containing the PEM-encoded public key of the Certificate Authorities you wish to trust for client authentication. This value is ignored if `requireClientAuth` is not enabled.

:::tip

See the [server samples repo](https://github.com/temporalio/samples-server/tree/main/tls) for sample TLS configurations.

:::

Below is an example enabling Server TLS (https) between SDKs and the Frontend APIs:

```yaml
global:
  tls:
    frontend:
      server:
        certFile: /path/to/cert/file
        keyFile: /path/to/key/file
      client:
        serverName: dnsSanInFrontendCertificate
```

Note, the `client` section generally needs to be provided to specify an expected DNS SubjectName contained in the presented server certificate via the `serverName` field; this is needed as Temporal uses IP to IP communication.
You can avoid specifying this if your server certificates contain the appropriate IP Subject Alternative Names.

Additionally, the `rootCaFiles` field needs to be provided when the client's host does not trust the Root CA used by the server.
The example below extends the above example to manually specify the Root CA used by the Frontend Services:

```yaml
global:
  tls:
    frontend:
      server:
        certFile: /path/to/cert/file
        keyFile: /path/to/key/file
      client:
        serverName: dnsSanInFrontendCertificate
        rootCaFiles:
          - /path/to/frontend/server/CA/files
```

Below is an additional example of a fully secured cluster using mutual TLS for both frontend and internode communication with manually specified CAs:

```yaml
global:
  tls:
    internode:
      server:
        certFile: /path/to/internode/cert/file
        keyFile: /path/to/internode/key/file
        requireClientAuth: true
        clientCaFiles:
          - /path/to/internode/serverCa
      client:
        serverName: dnsSanInInternodeCertificate
        rootCaFiles:
          - /path/to/internode/serverCa
    frontend:
      server:
        certFile: /path/to/frontend/cert/file
        keyFile: /path/to/frontend/key/file
        requireClientAuth: true
        clientCaFiles:
          - /path/to/internode/serverCa
          - /path/to/sdkClientPool1/ca
          - /path/to/sdkClientPool2/ca
      client:
        serverName: dnsSanInFrontendCertificate
        rootCaFiles:
          - /path/to/frontend/serverCa
```

**Note:** In the case that client authentication is enabled, the `internode.server` certificate is used as the client certificate among services. This adds the following requirements:

- The `internode.server` certificate must be specified on all roles, even for a frontend-only configuration.
- Internode server certificates must be minted with either **no** Extended Key Usages or **both** ServerAuth and ClientAuth EKUs.
- If your Certificate Authorities are untrusted, such as in the previous example, the internode server Ca will need to be specified in the following places:

  - `internode.server.clientCaFiles`
  - `internode.client.rootCaFiles`
  - `frontend.server.clientCaFiles`

## persistence

The `persistence` section holds configuration for the data store/persistence layer.
The following example shows a minimal specification for a password-secured Cluster using Cassandra.

```yaml
persistence:
  defaultStore: default
  visibilityStore: cass-visibility # The primary Visibility store.
  secondaryVisibilityStore: es-visibility # A secondary Visibility store added to enable Dual Visibility.
  numHistoryShards: 512
  datastores:
    default:
      cassandra:
        hosts: '127.0.0.1'
        keyspace: 'temporal'
        user: 'username'
        password: 'password'
    cass-visibility:
      cassandra:
        hosts: '127.0.0.1'
        keyspace: 'temporal_visibility'
    es-visibility:
      elasticsearch:
        version: 'v7'
        logLevel: 'error'
        url:
          scheme: 'http'
          host: '127.0.0.1:9200'
        indices:
          visibility: temporal_visibility_v1_dev
        closeIdleConnectionsInterval: 15s
```

The following top level configuration items are required:

### numHistoryShards

_Required_ - The number of history shards to create when initializing the Cluster.

**Warning:** This value is immutable and will be ignored after the first run.
Please ensure you set this value appropriately high enough to scale with the worst case peak load for this Cluster.

### defaultStore

_Required_ - The name of the data store definition that should be used by the Temporal server.

### visibilityStore

_Required_ - The name of the primary data store definition that should be used to set up [Visibility](/temporal-service/visibility) on the Temporal Cluster.

### secondaryVisibilityStore

_Optional_ - The name of the secondary data store definition that should be used to set up [Dual Visibility](/dual-visibility) on the Temporal Cluster.

### datastores

_Required_ - contains named data store definitions to be referenced.

Each definition is defined with a heading declaring a name (ie: `default:` and `visibility:` above), which contains a data store definition.

Data store definitions must be either `cassandra` or `sql`.

#### cassandra

A `cassandra` data store definition can contain the following values:

- `hosts`: _Required_ - "," separated Cassandra endpoints, e.g. "192.168.1.2,192.168.1.3,192.168.1.4".
- `port`: Default: 9042 - Cassandra port used for connection by `gocql` client.
- `user`: Cassandra username used for authentication by `gocql` client.
- `password`: Cassandra password used for authentication by `gocql` client.
- `keyspace`: _Required_ - the Cassandra keyspace.
- `datacenter`: The data center filter arg for Cassandra.
- `maxConns`: The max number of connections to this data store for a single TLS configuration.
- `tls`: See TLS below.

#### sql

A `sql` data store definition can contain the following values:

- `user`: Username used for authentication.
- `password`: Password used for authentication.
- `pluginName`: _Required_ - SQL database type.
  - _Valid values_: `mysql` or `postgres`.
- `databaseName` - _required_ - the name of SQL database to connect to.
- `connectAddr` - _required_ - the remote address of the database, e.g. "192.168.1.2".
- `connectProtocol` - _required_ - the protocol that goes with the `connectAddr`
  - _Valid values_: `tcp` or `unix`
- `connectAttributes` - a map of key-value attributes to be sent as part of connect `data_source_name` url.
- `maxConns` - the max number of connections to this data store.
- `maxIdleConns` - the max number of idle connections to this data store
- `maxConnLifetime` - is the maximum time a connection can be alive.
- `tls` - See below.

#### tls

The `tls` and `mtls` sections can contain the following values:

- `enabled` - _boolean_.
- `serverName` - name of the server hosting the data store.
- `certFile` - path to the cert file.
- `keyFile` - path to the key file.
- `caFile` - path to the ca file.
- `enableHostVerification` - _boolean_ - `true` to verify the hostname and server cert (like a wildcard for Cassandra cluster). This option is basically the inverse of `InSecureSkipVerify`. See `InSecureSkipVerify` in http://golang.org/pkg/crypto/tls/ for more info.
