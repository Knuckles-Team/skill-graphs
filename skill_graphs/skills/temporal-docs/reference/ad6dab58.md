
### nexus_task_endtoend_latency

Total latency of Nexus Tasks from the time the corresponding request hit the Frontend to after the SDK gets
acknowledgment from the server for task completion.

- Type: Histogram
- Available in: Go, Java
- Tags: `namespace`, `task_queue`, `nexus_service`, `nexus_operation`

### num_pollers

Current number of Worker Entities that are polling.

- Type: Gauge
- Available in: Core, Go, Java
- Tags: `namespace`, `poller_type`, `task_queue`

### poller_start

A Worker Entity poller was started.

- Type: Counter
- Available in: Go, Java
- Tags: `namespace`, `task_queue`

### request

Temporal Client made an RPC request.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `operation`

### request_failure

Temporal Client made an RPC request that failed.
This number is included into the total `request` counter for RPC requests.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `operation`

### request_latency

Latency of a Temporal Client gRPC request.

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `namespace`, `operation`

### resource_slots_cpu_usage

CPU usage as a value between 0 and 100. As perceived by the resource-based slots tuner, if
enabled.

- Type: Gauge
- Available in: Core, Java

### resource_slots_mem_usage

Memory usage as a value between 0 and 100. As perceived by the resource-based slots tuner, if
enabled.

- Type: Gauge
- Available in: Core, Java

### sticky_cache_hit

A Workflow Task found a cached Workflow Execution to run against.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`

### sticky_cache_miss

A Workflow Task did not find a cached Workflow execution to run against.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`

### sticky_cache_size

Current cache size, expressed in number of Workflow Executions.

- Type: Gauge
- Available in: Core, Go, Java
- Tags: `namespace` (TypeScript, Java), `task_queue` (TypeScript)

### sticky_cache_total_forced_eviction

A Workflow Execution has been forced from the cache intentionally.

- Type: Counter
- Available in: Go, Java
- Tags: `namespace`, `task_queue`

### unregistered_activity_invocation

A request to spawn an Activity Execution is not registered with the Worker.

- Type: Counter
- Available in: Go,
- Tags: `activity_type`, `namespace`, `task_queue`, `workflow_type`

### worker_start

A Worker Entity has been registered, created, or started.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `worker_type`

### worker_task_slots_available

The total number of Workflow, Activity, Local Activity, or Nexus Task execution slots that are currently available.
Use the `worker_type` key to differentiate execution slots.
The Worker type specifies an ability to perform certain tasks.
For example, Workflow Workers execute Workflow Tasks, Activity Workers execute Activity Tasks, and so forth.

- Type: Gauge
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `worker_type`

### worker_task_slots_used

The total number of Workflow, Activity, Local Activity, or Nexus Tasks execution slots in current use.
Use the `worker_type` key to differentiate execution slots.
The Worker type specifies an ability to perform certain tasks.
For example, Workflow Workers execute Workflow Tasks, Activity Workers execute Activity Tasks, and so forth.

- Type: Gauge
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `worker_type`

### workflow_active_thread_count

Total amount of Workflow threads in the Worker Process.

- Type: Gauge
- Available in: Java

### workflow_cancelled

Workflow Execution ended because of a cancellation request.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `workflow_type`

### workflow_completed

A Workflow Execution completed successfully.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `workflow_type`

### workflow_continue_as_new

A Workflow ended with Continue-As-New.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `workflow_type`

### workflow_endtoend_latency

Total Workflow Execution time from schedule to completion for a single Workflow Run. (A retried Workflow Execution is a separate Run.)

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `workflow_type`

### workflow_failed

A Workflow Execution failed.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `workflow_type`

### workflow_task_execution_failed

A Workflow Task Execution failed.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `workflow_type`, `failure_reason`

Valid values for the `failure_reason` tag:

- `NonDeterminismError`: The Workflow Task failed due to a non-determinism error.
- `WorkflowError`: The Workflow Task failed for any other reason.

### workflow_task_execution_latency

Workflow Task Execution time.

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `workflow_type`

### workflow_task_queue_poll_empty

A Workflow Worker polled a Task Queue and timed out without picking up a Workflow Task.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`

### workflow_task_queue_poll_succeed

A Workflow Worker polled a Task Queue and successfully picked up a Workflow Task.

- Type: Counter
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`

### workflow_task_replay_latency

Time to catch up on replaying a Workflow Task.

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`, `workflow_type`

### workflow_task_schedule_to_start_latency

The Schedule-To-Start time of a Workflow Task.

- Type: Histogram
- Available in: Core, Go, Java
- Tags: `namespace`, `task_queue`

---

## Temporal Server options reference

You can run the [Temporal Server](/temporal-service/temporal-server) as a Go application by including the server package `go.temporal.io/server/temporal` and using it to create and start a Temporal Server.

The Temporal Server services can be run in various ways.
We recommend this approach for a limited number of situations.

```go
s, err := temporal.NewServer()
if err != nil {
	log.Fatal(err)
}
err = s.Start()
if err != nil{
	log.Fatal(err)
}
```

`NewServer()` accepts functions as parameters.
Each function returns a `ServerOption` that is applied to the instance.
Source code for parameter reference is here: https://github.com/temporalio/temporal/blob/main/temporal/server_option.go

### WithConfig

To launch a Temporal server, a configuration file is required. The server automatically searches for this configuration
in the default location ./config/development.yaml when starting. If you need to use a custom configuration, you can
specify it through the server's configuration option. For comprehensive details about configuration parameters and
structure, refer to the [official configuration documentation](https://pkg.go.dev/go.temporal.io/server/common/config).

```go
s, err := temporal.NewServer(
	temporal.WithConfig(cfg),
)
```

### WithConfigLoader

Load a custom configuration from a file.

```go
s, err := temporal.NewServer(
	temporal.WithConfigLoader(configDir, env, zone),
)
```

### ForServices

Sets the list of all valid temporal services.
The default can be used from the `go.temporal.io/server/temporal` package.

```go
s, err := temporal.NewServer(
	temporal.ForServices(temporal.Services),
)
```

### InterruptOn

This option provides a channel that interrupts the server on the signal from that channel.

- If `temporal.InterruptOn()` is not passed, `server.Start()` is never blocked and you need to call `server.Stop()` somewhere.
- If `temporal.InterruptOn(nil)` is passed, `server.Start()` blocks forever until the process is killed.
- If `temporal.InterruptOn(temporal.InterruptCh())` is passed, `server.Start()` blocks until you use Ctrl+C, which then gracefully shuts the server down.
- If `temporal.Interrupt(someCustomChan)` is passed, `server.Start()` blocks until a signal is sent to `someCustomChan`.

```go
s, err := temporal.NewServer(
	temporal.InterruptOn(temporal.InterruptCh()),
)
```

### WithAuthorizer

Sets a low level [authorization mechanism](/self-hosted-guide/security#authorizer-plugin) that determines whether to allow or deny inbound API calls.

```go
s, err := temporal.NewServer(
	temporal.WithAuthorizer(myAuthorizer),
)
```

### WithTLSConfigFactory

Overrides the default TLS configuration provider.
`TLSConfigProvider` is defined in the `go.temporal.io/server/common/rpc/encryption` package.

```go
s, err := temporal.NewServer(
	temporal.WithTLSConfigFactory(yourTLSConfigProvider),
)
```

### WithClaimMapper

Configures a [mechanism to map roles](/self-hosted-guide/security#claim-mapper) to `Claims` for authorization.

```go
s, err := temporal.NewServer(
  temporal.WithClaimMapper(func(cfg *config.Config) authorization.ClaimMapper {
  		logger := getYourLogger() // Replace with how you retrieve or initialize your logger
		return authorization.NewDefaultJWTClaimMapper(
			authorization.NewDefaultTokenKeyProvider(cfg, logger),
			cfg
		)
	}),
)
```

### WithCustomMetricsReporter

Sets a custom tally metric reporter.

```go
s, err := temporal.NewServer(
	temporal.WithCustomMetricsReporter(myReporter),
)
```

You can see the [Uber tally docs on custom reporter](https://github.com/uber-go/tally#report-your-metrics) and see a community implementation of [a reporter for Datadog's `dogstatsd` format](https://github.com/temporalio/temporal/pull/998#issuecomment-857884983).

---

## tctl v1.17 activity command reference

:::info tctl is deprecated

The tctl command line utility has been deprecated and is no longer actively supported.
We recommend transitioning to [Temporal CLI](/cli) for continued use and access to new features.

Thank you for being a valued part of the Temporal community.

:::

The `tctl activity` commands enable [Activity Execution](/activity-execution) operations.

- [tctl activity complete](#complete)
- [tctl activity fail](#fail)

## complete

The `tctl activity complete` command completes an [Activity Execution](/activity-execution).

`tctl activity complete <modifiers>`

The following modifiers control the behavior of the command.

### --workflow_id

Specify the [Workflow Id](/workflow-execution/workflowid-runid#workflow-id) of an [Activity Execution](/activity-execution) to complete.

Alias: `-w`

**Example**

```bash
tctl activity complete --workflow_id <id>
```

### --run_id

Specify the [Run Id](/workflow-execution/workflowid-runid#run-id) of an [Activity Execution](/activity-execution) to complete.

Alias: `-r`

**Example**

```bash
tctl activity complete --run_id <id>
```

### --activity_id

Specify the [Activity Id](/activity-execution#activity-id) of an [Activity Execution](/activity-execution) to complete.

**Example**

```bash
tctl activity complete --activity_id <id>
```

### --result

Specify the result of an [Activity Execution](/activity-execution) when using tctl to complete the Activity Execution.

**Example**

```bash
tctl activity complete --result <value>
```

### --identity

Specify the identity of the operator when using tctl to complete an [Activity Execution](/activity-execution).

**Example**

```bash
tctl activity complete --identity <value>
```

## fail

The `tctl activity fail` command fails an [Activity Execution](/activity-execution).

`tctl activity fail [<modifiers>]`

The following modifiers control the behavior of the command.

### --workflow_id

Specify the [Workflow Id](/workflow-execution/workflowid-runid#workflow-id) of an [Activity Execution](/activity-execution) to fail.

Alias: `-w`

**Example**

```bash
tctl activity fail --workflow_id <id>
```

### --run_id

Specify the [Run Id](/workflow-execution/workflowid-runid#run-id) of an [Activity Execution](/activity-execution) to fail.

Alias: `-r`

**Example**

```bash
tctl activity fail --run_id <id>
```

### --activity_id

Specify the [Activity Id](/activity-execution#activity-id) of an [Activity Execution](/activity-execution) to fail.

**Example**

```bash
tctl activity fail --activity_id <id>
```

### --reason

Specify the reason for failing an [Activity Execution](/activity-execution).

**Example**

```bash
tctl activity fail --reason <value>
```

### --detail

Specify details of the reason for failing an [Activity Execution](/activity-execution).

**Example**

```bash
tctl activity fail --detail <value>
```

### --identity

Specify the identity of the operator when using tctl to fail an [Activity Execution](/activity-execution).

**Example**

```bash
tctl activity complete --identity <value>
```

---

## tctl v1.17 admin command reference

:::info tctl is deprecated

The tctl command line utility has been deprecated and is no longer actively supported.
We recommend transitioning to [Temporal CLI](/cli) for continued use and access to new features.

Thank you for being a valued part of the Temporal community.

:::

A `tctl admin` command allows the user to run admin operations.

Modifiers:

#### --help

`tctl admin [--help | -h]`

## cluster

The `tctl admin cluster` command runs the administrator-level operations on a given Cluster.

`tctl admin cluster command [command modifiers] [arguments...]`

- [add_search_attributes](#add_search_attributes)
- [remove_search_attributes](#remove_search_attributes)
- [get_search_attributes](#get_search_attributes)
- [describe](#describe)
- [list](#list)
- [upsert_remote_cluster](#upsert_remote_cluster)
- [remove_remote_cluster](#upsert_remote_cluster)

### add_search_attributes

The `tctl admin cluster add-search-attributes` command allows Search Attributes to be added to a Cluster.
Custom Search Attributes can be used to make a Cluster more identifiable.

:::note
Due to Elasticsearch limitations, you can only add new custom Search Attributes. Existing Search Attributes cannot be renamed or removed from the Elasticsearch index.
:::

Use this command to add custom Search Attributes to your Temporal Cluster:

```bash
tctl admin cluster add-search-attributes --name <SearchAttributeName> --type <SearchAttributeValueType>
```

:::note
If you are adding custom Search Attributes to a Cluster running from the `docker-compose-es.yml` file in the [temporalio/docker-compose](https://github.com/temporalio/docker-compose) repo, make sure to increase the Docker memory to more than 6 GB.
:::

#### --skip_schema_update

Allows the user to skip the Elasticsearch index schema update.

:::note
This will only register in metadata.
:::

#### --name

The name of the Search Attribute to add. Names can have multiple values.

Search Attribute names are case sensitive.

#### --type

The type of Search Attribute to add.
Multiple values can be added at once.

Values: Text, Keyword, Int, Double, Bool, Datetime

### describe

The `tctl admin cluster describe` command provides information for the current Cluster.

The following modifier changes the behavior of the command:

#### --cluster_value

The name of the remote Cluster within the current Cluster.

This modifier is optional, and can default to the return of current Cluster information.

### get_search_attributes

The `tctl admin cluster get_search_attributes` command retrieves existing Search Attributes for a given Cluster.

The following modifier will change the behavior of the command:

#### --print_json

Prints the existing search attributes in JSON format.

### list

The `tctl admin cluster list` command lists Cluster information on the given Cluster.

Default: 100

The modifier below changes the behavior of the command:

#### --pagesize

The size of the page that the list is printed on.

### remove_remote_cluster

The `tctl admin cluster remove_remote_cluster` command removes remote Cluster information on the given Cluster.

The modifier below changes the behavior of the operation:

#### --cluster

The name of the remote Cluster to remove.

### remove_search_attributes

> The Temporal tctl documentation covers version 1.17 of the Temporal CLI.

The `tctl admin cluster remove-search-attributes` command removes custom Search Attribute metadata from a Cluster.
This operation has no effect on Elasticsearch index schema.

Use the following command to remove a [Search Attribute](/search-attribute) from a Cluster's metadata:

```bash
tctl admin cluster remove-search-attributes --name <SearchAttributeKey>
```

Only custom Search Attributes can be removed from a Cluster's metadata.
Default Search Attributes cannot be removed.

Removing a Search Attribute removes it from the Cluster's metadata but does not remove it from the Elasticsearch index.
This means that the Search Attribute can be added back later as the same type.
After a Search Attribute has been added to the Elasticsearch index, it cannot be changed.

The following modifier changes the behavior of the operation:

#### --name

Name of the Search Attribute to remove.

### upsert_remote_cluster

The `tctl admin cluster upsert_remote_cluster` command adds or updates remote Cluster information in the current Cluster.

#### --frontend_address

The remote Cluster frontend address.

#### --enable_connection

Enables remote Cluster connection.

## db

The `tctl admin db` command runs administrator-level operations on a given database.

### Usage

`tctl admin db command [command modifiers] [arguments...]`

### Commands

- [tctl admin db scan](#scan)
- [tctl admin db clean](#clean)

### clean

The `tctl admin db clean` command cleans corrupted [Workflow Executions](/workflow-execution) from the targeted database.

The modifiers below change the behavior of the command.

#### --db_engine

Type of DB engine to use

Default: `cassandra`
Value: `cassandra` | `mysql` | `postgres`

#### --db_address

Persistence address for the database.

Default: 127.0.0.1

#### --db_port

Persistence port for the DB.

Default: 9042

#### --username

Database username.

#### --password

Database password.

#### --keyspace

Database keyspace

Default: "temporal"

#### --input_directory

The directory which contains the corrupted [Workflow Execution](/workflow-execution) files from running [`scan`](#scan).

#### --lower_shard_bound

The minimum amount (inclusive) of corrupt shards to handle.

Default: 0

#### --upper_shard_bound

The maximum amount (exclusive) of corrupt shards to handle.

Default: 16384

#### --starting_rps

starting rps of database queries.

Default: 100

#### --rps

Target rps of database queries.

Default: 7000

#### --concurrency

Number of threads to handle a scan.

Default: 1000

#### --report_rate

The number of shards handled between each emittance of progress.

Default: 10

:::note

Enable `--tls` before using any of the following modifiers.

:::

#### --tls_cert_path

Where the tls client cert is located.

#### --tls_key_path

Where the tls key is located.

#### --tls_ca_path

Where the tls ca is located.

#### --tls_server_name

The name of the Db tls server.

#### --tls_disable_host_verification

Disables verification of the DB tls hostname and server cert.

### scan

The `tctl admin db scan` command scans concrete Workflow Executions in a given database, and detects corrupted ones.

#### --db_engine

Type of DB engine to use

Default: `cassandra`
Value: `cassandra` | `mysql` | `postgres`

#### --db_address

Persistence address for the DB.

Default: 127.0.0.1

#### --db_port

Persistence port for the DB.

Default: 9042

#### --username

DB username.

#### --password

DB password.

#### --keyspace

DB keyspace

Default: "temporal"

#### --lower_shard_bound value

The minimum amount (inclusive) of corrupt shards to handle.

Default: 0

#### --upper_shard_bound

The maximum amount (exclusive) of corrupt shards to handle.

Default: 16384

#### --starting_rps

starting rps of database queries.

Default: 100

#### --rps value

Target rps of database queries.

Default: 7000

#### --pagesize

The size of the page used to query database executions.

Default: 500

#### --concurrency

Number of threads to handle a scan.

Default: 1000

#### --report_rate

The number of shards handled between each emittance of progress.

Default: 10

#### --tls

Enable TLS over the DB connection.

:::note

Enable `--tls` before using any of the following modifiers.

:::

#### --tls_cert_path

Where the tls client cert is located.

#### --tls_key_path

Where the tls key is located.

#### --tls_ca_path

Where the tls ca is located.

#### --tls_server_name

The name of the Db tls server.

#### --tls_disable_host_verification

Disables verification of the DB tls hostname and server cert.

## decode

The `tctl admin decode` command allows the user to decode payloads sent and received from executed Activities.

`tctl admin decode command [command modifiers] [arguments...]`

- [proto](#proto)
- [base64](#base64)

### base64

The `tctl admin decode base64` command decodes base64 Payloads.

#### --base64_data

Decoded data in base64 format.

#### --base64_file

Creates a file with data in base64 format.

### proto

The `tctl admin decode proto` command decodes the Payload to proto format.

#### --type

The full name of the proto type to decode the Payload to.

#### --hex_data

Decodes the data to hex format.

#### --hex_file

Creates a file with the decoded hex data.

#### --binary_file

Creates a file with the decoded binary data.

## dlq

The `tctl admin dlq` commands run admin operations on a given dead-letter queue (DLQ).

`tctl admin dlq command [command modifiers] [arguments...]`

- [tctl admin dlq read](#read)
- [tctl admin dlq purge](#purge)
- [tctl admin dlq merge](#merge)

### merge

The `tctl admin dlq merge` command allows dead-letter queue (DLQ) messages to be merged.

The messages must have TaskIds with an equal or lesser value than the given TaskId.

#### --dlq_type

The type of DLQ to manage.

Options: namespace, history

#### --cluster

Source cluster for the DLQ.

#### --shard_id

ShardId provided for the command.

#### --last_message_id

Identifies the last read message.

Default: 0

### purge

The `tctl admin dlq purge` command deletes DLQ messages that have a Task Id equal to or less than the provided Task Id.

#### --dlq_type

The type of DLQ to manage.

Options: namespace, history

#### --cluster

Source cluster for the DLQ.

#### --shard_id

ShardId provided for the command.

#### --last_message_id

Identifies the last read message.

Default: 0

### read

The `tctl admin dlq read` command reads out messages from the dead-letter queue (DLQ).

---

#### --dlq_type

The type of DLQ to manage.

Options: namespace, history

#### --cluster

Source cluster for the DLQ.

#### --shard_id

ShardId provided for the command.

#### --max_message_count

The maximum number of messages to fetch.

Default: 0

#### --last_message_id

Identifies the last read message.

Default: 0

#### --output_filename

Provides a file to write output to.

Output is written to stdout on default.

## history_host

The `tctl admin history_host` command runs an admin-level operation on the history host.

## Usage

`tctl admin history_host command [command options] [arguments...]`

## Commands

- [tctl admin history_host describe](#describe)
- [tctl admin history_host get_shardid](#get_shardid)

### describe

The `tctl admin history_host describe` command describes the internal information of history host.

The following modifiers change the behavior of the command.

#### --workflow_id

Alias: `-w`

The WorkflowId of the Workflow whose history host is to be described.

#### --history_address

The history address of the history host.

#### --shard_id

The Id of the shard that belongs to the history host.

#### --print_full

Print a full and detailed summary of the history host.

### get_shardid

The `tctl admin history_host get_shardid` command gets the `shardId` for a given `namespaceId` and `workflowId`.

The following modifiers change the behavior of this command.

#### --namespace_id

The `namespaceId` of the history host where we're getting the `shardId`.

#### --workflow_id

Alias: `-w`

The WorkflowId of the history host where we're getting the shardId.

#### --number_of_shards

The total amount of shards for the Temporal Cluster.

Default: 0

## membership

The `tctl admin membership` command allows admin operations to be run on membership items.

### Usage

`tctl admin membership command [command modifiers] [arguments...]`

### Commands

- [list_gossip](#list_gossip)
- [list_db](#list_db)

### list_db

The `tctl admin membership list_db` command lists the Cluster items in a targeted membership.

The following modifiers change the behavior of the command.

#### --heartbeated_within

Filters the list by last Heartbeat time.

{/* todo: add supported format list */}

#### --role

Filters the results by membership role.

Default: all
Values: all, frontend, history, matching, worker

### list_gossip

The `tctl admin membership list_gossip` command lists the ringpop membership items present on the targeted membership.

The following modifier changes the behavior of the command:

#### --role value

Filters the results by membership role

Default: all
Values: all, frontend, history, matching, worker

## shard

The `tctl admin shard` commands enable admin-level operations on a specified shard.

#### tctl admin shard commands

- [describe](#describe)
- [describe_task](#describe_task)
- [list_tasks](#list_tasks)
- [close_shard](#close_shard)
- [remove_task](#remove_task)

### close_shard
