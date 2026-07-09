
The `tctl admin shard close_shard` command closes a shard with an Id that corresponds to the value given in the command.

`tctl admin shard close_shard [command options] [arguments...]`

The modifier below will change the behavior and output of the command.

#### --shard_id value

ShardId managed by the Temporal Cluster.

### describe_task

The `tctl admin shard describe_task` command describes a specified Task's Task Id, Task type, shard Id, and task visibility timestamp.

The modifiers below control the output and behavior of the command. Enter all modifiers after the command as such:

`tctl admin shard describe_task <modifiers>`

#### --db_engine

The type of database (DB) engine for the shard to use.

Default: "cassandra"

Values: "cassandra", "mysql", "postgres"

{/* todo: examples */}

#### --db_address

Persistence address for the database.

Default: 127.0.0.1

#### --db_port

Persistence port for the database.

Default: 9042

#### --username

Username entered into the database.

#### --password

Password entered into the database.

#### --keyspace

Keyspace for the database.

default: "temporal"

#### --tls

Enables TLS over the database connection.

#### --tls_cert_path

DB tls client cert path.

Note: tls must be enabled

#### --tls_server_name

DB tls server name

Note: tls must be enabled

#### --tls_disable_host_verification

DB tls verify hostname and server cert

Note: tls must be enabled

#### --shard_id

Identifies the specified shard.

Default: 0

#### --task_id

Describes the task.

Default: 0

#### --task_type

The kind of Task that is targeted within a shard.

Default: transfer

Values: transfer, timer, replication

#### --task_timestamp

Task visibility timestamp in nanoseconds

Default: 0

#### --target_cluster

Temporal cluster for the shard to use.

Default: "active"

### describe

The `tctl admin shard describe` command shows the Id for the specified shard.

The modifier below controls the behavior of the command.

#### --shard_id value

The Id of the shard to describe

Default: 0

### list_tasks

The `tctl admin shard list_tasks` command will list the Tasks available for a given shard Id and Task type.

The modifiers below affect the output and behavior of the command.

#### --more

Lists more pages of list tasks.
The default setting is to list one page of 10 list tasks.

#### --pagesize value

The size of the result page.
Default: 10

#### --target_cluster value

Temporal cluster to use.
Default: "active"

#### --shard_id value

The ID of the shard

Default: 0

#### --task_type value

The type of Task.

Default: transfer
Values: transfer, timer, replication, visibility

#### --min_visibility_ts value

The minimum value that can be set as a Task Visibility timestamp.

Supported formats include:

- '2006-01-02T15:04:05+07:00'
- Raw UnixNano
- Time range (N-duration), where 0 < N < 1000000 and duration (full-notation/short-notation) can be:
  - second/s
  - minute/m
  - week/w
  - month/m
  - year/y

#### --max_visibility_ts value

The maximum value that can be set as a Task Visibility timestamp.

Supported formats:

- '2006-01-02T15:04:05+07:00'
- Raw UnixNano
- Time range (N-duration), where 0 < N < 1000000 and duration (full-notation/short-notation) can be:
  - second/s
  - minute/m
  - week/w
  - month/m
  - year/y

### remove_task

The `tctl admin shard remove_task` command removes a Task from the shard.

`tctl admin shard remove_task [command options] [arguments...]`

The Task removed must have values that matches what is given in the command line.

The modifiers below change the behavior of the command.

#### --shard_id value

The shardId for the Task to be removed.

Default: 0

#### --task_id value

The taskId for the Task to be removed.

Default: 0

#### --task_type value

The type of Task to remove.

Default: transfer

Values: transfer, timer, replication

#### --task_timestamp value

The task visibility timestamp, given in nanoseconds.

Default: 0

## workflow

The `tctl admin workflow` commands enable administrator-level operations on Workflow Executions.

`tctl admin workflow command [modifiers] [arguments...]`

- [show](#show)

- [describe](#describe)

- [refresh_tasks](#refresh_tasks)

- [delete](#delete)

### delete

The `tctl admin workflow delete` command deletes the current [Workflow Execution](/workflow-execution) and the mutableState record.

#### --db_engine value

The type of database (DB) engine to use.

Default: "cassandra"
Values: "cassandra", "mysql", "postgres"

#### --db_address value

Persistence address for the database.

Default: 127.0.0.1

#### --db_port value

Persistence port for the database.

Default: 9042

#### --username value

Username entered into the database.

#### --password value

Password entered into the database.

#### --keyspace value

Keyspace for the database.

default: "temporal"

#### --url value

URL of the Elasticsearch cluster.

Default: "http://127.0.0.1:9200"

#### --es-username value

Username for the Elasticsearch cluster.

#### --es-password value

Password for the Elasticsearch cluster.

#### --version value

The version of the Elasticsearch cluster for the Workflow.

Default: v7

Values: v6, v7

#### --index value

Elasticsearch index name.

#### --workflow_id value

Alias: `-w`

The Id of the current Workflow.

#### --run_id value

Alias: `-r`

The Id of the current run.

#### --skip_errors

Skip any errors that occur in the Workflow Execution.

#### --tls

Enables TLS over the database connection.

:::note

TLS must be enabled to use the following modifiers.

:::

#### --tls_cert_path value

DB tls client cert path.

Note: tls must be enabled

#### --tls_key_path value

DB tls client key path

Note: tls must be enabled

#### --tls_ca_path value

DB tls client ca path

Note: tls must be enabled

#### --tls_server_name value

DB tls server name

Note: tls must be enabled

#### --tls_disable_host_verification

DB tls verify hostname and server cert

Note: tls must be enabled

## describe

The `tctl admin workflow describe` command describes internal information of the current [Workflow Execution](/workflow-execution).

#### --workflow_id value

Alias: `-w`

The Id of the current Workflow.

#### --run_id value

Alias: `-r`

The Id of the current run.

## refresh_tasks

The `tctl admin workflow refresh_tasks` command updates all [Tasks](/tasks#task) in a [Workflow](/workflows), provided that the command can fetch new information for Tasks.

#### --workflow_id value

Alias: `-w`

The Id of the current Workflow.

#### --run_id value

Alias: `-r`

The Id of the current run.

## show

The `tctl admin workflow show` command displays Event history from the database.

#### --workflow_id value

Alias: `-w`

The current Workflow.

#### --run_id value

Alias: `-r`

The current RunId.

#### --min_event_id value

The minimum Event Id to include in the history.

Default: 0

#### --max_event_id value

The maximum Event Id to include in the history.

Default: 0

#### --min_event_version value

The start Event version to be included in the history.

Default: 0

#### --max_event_version value

The end Event version to be included in the history.

Default: 0

#### --output_filename value

The file where the output is sent to.

---

## tctl v1.17 batch command reference

:::info tctl is deprecated

The tctl command line utility has been deprecated and is no longer actively supported.
We recommend transitioning to [Temporal CLI](/cli) for continued use and access to new features.

Thank you for being a valued part of the Temporal community.

:::

**How to run a tctl batch command.**

A `tctl batch` command enables you to affect multiple existing [Workflow Executions](/workflow-execution) with a single command.
A batch job runs in the background and affects Workflow Executions one at a time.

Use [tctl batch start](#start) to start a batch job.

:::note

`tctl-v1` can run `batch` and `batch-v2` commands.

:::

When starting a batch job, you must provide a [List Filter](/list-filter) and the type of batch job that should occur.
Batch jobs run in the background and affect Workflow Executions one at a time.

The List Filter identifies the set of Workflow Executions to be affected by the batch job.
The `tctl batch start` command shows you how many Workflow Executions will be affected by the batch job and asks you to confirm before proceeding.

The batch type determines what other parameters you must provide and what is being affected.
There are three types of batch jobs:

- Signal: Send a Signal to the set of Workflow Executions that the List Filter specifies.
- Cancel: Cancel the set of Workflow Executions that the List Filter specifies.
- Terminate: Terminate the set of Workflow Executions that the List Filter specifies.

A successfully started batch job returns a Job ID.
You can use this Job ID in the `tctl batch describe` command, which describes the progress of a specific batch job.

You can also use the Job ID to terminate the batch job itself.
Terminating a batch job does not roll back the operations already performed by the batch job.

### tctl batch commands

- [tctl batch describe](#describe)
- [tctl batch list](#list)
- [tctl batch start](#start)
- [tctl batch terminate](#terminate)

## start

The `tctl batch start` command starts a batch job.

`tctl batch start --query <value> <modifiers>`

The following modifiers control the behavior of the command.

### `--query`

_Required modifier_

Specify the [Workflow Executions](/workflow-execution) that this batch job should operate.

The SQL-like query of [Search Attributes](/search-attribute) is the same as used by the `tctl workflow list --query` command.

Alias: `-q`

**Example**

```bash
tctl batch start --query <value>
```

### `--reason`

Specify a reason for running this batch job.

**Example**

```bash
tctl batch start --query <value> --reason <string>
```

### `--batch_type`

Specify the operation that this batch job performs. The supported operations are `signal`, `cancel`, and `terminate`.

**Example**

```bash
tctl batch start --query <value> --batch_type <operation>
```

### `--signal_name`

Specify the name of a [Signal](/sending-messages#sending-signals). This modifier is required when `--batch_type` is `signal`.

**Example**

```bash
tctl batch start --query <value> --batch_type signal --signal_name <name>
```

### `--input`

Pass input for the [Signal](/sending-messages#sending-signals). Input must be in JSON format.

Alias: `-i`

**Example**

```bash
tctl batch start --query <value> --input <json>
```

### `--rps`

Specify RPS of processing. The default value is 50.

**Example**

```bash
tctl batch start --query <value> --rps <value>
```

### `--yes`

Disable the confirmation prompt.

Alias: `y`

**Example**

```bash
tctl batch start --query <value> --yes
```

## list

The `tctl batch list` command lists all batch jobs.

`tctl batch list <modifiers>`

:::note

`tctl-v1` can run `batch` and `batch-v2` commands.

:::

The following modifier controls the behavior of the command.

### --pagesize

Specify the maximum number of batch jobs to list on a page. The default value is 30.

**Example**

```bash
tctl batch list --pagesize <value>
```

## describe

The `tctl batch describe` command describes the progress of a batch job.

`tctl batch describe --job_id <id>`

:::note

`tctl` can run `batch` and `batch-v2` commands.

:::

The following modifier controls the behavior of the command.

### --job_id

_Required modifier_

Specify the job ID of a batch job.

**Example**

```bash
tctl batch describe --job_id <id>
```

## terminate

The `tctl batch terminate` command terminates a batch job.

`tctl batch terminate --job_id <id> <modifiers>`

:::note

`tctl-v1` can run `batch` and `batch-v2` commands.

:::

The following modifiers control the behavior of the command.

### `--job_id`

_Required modifier_

Specify the job ID of a batch job.

**Example**

```bash
tctl batch terminate --job_id <id>
```

### `--reason`

Specify a reason for terminating this batch job.

**Example**

```bash
tctl batch terminate --job_id <id> --reason <string>
```

---

## tctl v1.17 cluster command reference

:::info tctl is deprecated

The tctl command line utility has been deprecated and is no longer actively supported.
We recommend transitioning to [Temporal CLI](/cli) for continued use and access to new features.

Thank you for being a valued part of the Temporal community.

:::

The `tctl cluster` command enables [Temporal Cluster](/temporal-service) operations.

- [tctl cluster health](#health)
- [tctl cluster get-search-attributes](#get-search-attributes)

## get-search-attributes

The `tctl cluster get-search-attributes` command lists all [Search Attributes](/search-attribute) that can be used in the `--query` modifier of the [`tctl workflow list`](/tctl-v1/workflow#list) command and the `--search_attr_key` and `--search_attr_value` modifiers of the [`tctl workflow run`](/tctl-v1/workflow#run) and [`tctl workflow start`](/tctl-v1/workflow#start) commands.

**Example:**

```bash
tctl cluster get-search-attributes
```

The command has no modifiers.

Example output:

```text
+-----------------------+----------+
|         NAME          |   TYPE   |
+-----------------------+----------+
| BinaryChecksums       | Keyword  |
| CloseTime             | Int      |
| CustomBoolField       | Bool     |
| CustomDatetimeField   | Datetime |
| CustomDoubleField     | Double   |
| CustomIntField        | Int      |
| CustomKeywordField    | Keyword  |
| CustomNamespace       | Keyword  |
| CustomStringField     | String   |
| ExecutionStatus       | Int      |
| ExecutionTime         | Int      |
| Operator              | Keyword  |
| RunId                 | Keyword  |
| StartTime             | Int      |
| TaskQueue             | Keyword  |
| TemporalChangeVersion | Keyword  |
| WorkflowId            | Keyword  |
| WorkflowType          | Keyword  |
+-----------------------+----------+
```

The admin version of this command displays default and custom Search Attributes separately, and also shows the underlying Elasticsearch index schema and system Workflow status.

## health

The `tctl cluster health` command checks the health of the [Frontend Service](/temporal-service/temporal-server#frontend-service).

`tctl cluster health`

The command has no modifiers.

---

## tctl v1.17 data-converter command reference

:::info tctl is deprecated

The tctl command line utility has been deprecated and is no longer actively supported.
We recommend transitioning to [Temporal CLI](/cli) for continued use and access to new features.

Thank you for being a valued part of the Temporal community.

:::

The `tctl dataconverter` command enables custom [Data Converter](/dataconversion) operations.

- [tctl dataconverter web](#web)

## web

The `tctl dataconverter web` command specifies the WebSocket URL of a custom [Data Converter](/dataconversion) to use with Temporal Web.

`tctl dataconverter web --web_ui_url <url>`

The following modifiers control the behavior of the command.

### --port

Specify a port for the WebSocket URL of a custom [Data Converter](/dataconversion).
The default value is 0.

**Example**

```bash
tctl dataconverter web --web_ui_url <url> --port <value>
```

### --web_ui_url

_Required modifier_

Specify the WebSocket URL of a custom [Data Converter](/dataconversion).

**Example**

```bash
tctl dataconverter web --web_ui_url <url>
```

---

## tctl v1.17 command reference

:::info tctl is deprecated

The tctl command line utility has been deprecated and is no longer actively supported.
We recommend transitioning to [Temporal CLI](/cli) for continued use and access to new features.

Thank you for being a valued part of the Temporal community.

:::

:::note

This documentation reflects tctl version 1.17.

:::

The Temporal CLI (tctl) is a command-line tool that you can use to interact with a Temporal Cluster.
It can perform [Namespace](/namespaces) operations (such as register, update, and describe) and [Workflow](/workflows) operations (such as start
Workflow, show Event History, and Signal Workflow).

- [How to install tctl](#install)
- [Environment variables for tctl](#environment-variables)

## tctl commands

- [tctl activity](/tctl-v1/activity/)
- [tctl admin](/tctl-v1/admin/)
- [tctl batch](/tctl-v1/batch/)
- [tctl cluster](/tctl-v1/cluster/)
- [tctl dataconverter](/tctl-v1/dataconverter/)
- [tctl namespace](/tctl-v1/namespace/)
- [tctl taskqueue](/tctl-v1/taskqueue/)
- [tctl workflow](/tctl-v1/workflow/)

## How to install tctl {/* #install */}

> The Temporal tctl documentation covers version 1.17 of the Temporal CLI.

You can install [tctl](/tctl-v1) in the following ways.

- Install locally by using [Homebrew](https://brew.sh/): `brew install tctl`
- Run locally together with Temporal Server in [Docker Compose](https://github.com/temporalio/docker-compose): `docker exec temporal-admin-tools tctl YOUR COMMANDS HERE`
  - To invoke [tctl](/tctl-v1) as though it is installed locally (such as `tctl namespace describe`), set an alias: `alias tctl="docker exec temporal-admin-tools tctl"`
- Run the [temporal-admin-tools](https://hub.docker.com/r/temporalio/admin-tools) Docker image:
  - On Linux: `docker run --rm -it --entrypoint tctl --network host --env TEMPORAL_CLI_ADDRESS=localhost:7233 temporalio/admin-tools:1.14.0`
  - On macOS or Windows: `docker run --rm -it --entrypoint tctl --env TEMPORAL_CLI_ADDRESS=host.docker.internal:7233 temporalio/admin-tools:1.14.0`
  - If your Temporal Server is running on a remote host, change the value of `TEMPORAL_CLI_ADDRESS`.
  - To simplify command lines, create a `tctl` alias.
- Install the latest version of the tctl in your `GOPATH`: `go install github.com/temporalio/tctl/cmd/tctl@latest`

**Note:** To use [tctl](/tctl-v1), you must have a Temporal Server running.

To see help for [tctl](/tctl-v1) commands, enter the following commands.

| Command             | Description                                            |
| ------------------- | ------------------------------------------------------ |
| `tctl -h`           | Display help for top-level commands and global options |
| `tctl namespace -h` | Display help for [Namespace](/namespaces) operations   |
| `tctl workflow -h`  | Display help for [Workflow](/workflows) operations     |
| `tctl taskqueue -h` | Display help for [Task Queue](/task-queue) operations  |

## Global modifiers

You can supply the values for many of these modifiers by setting [environment variables](#environment-variables) instead of including the modifiers in a tctl command.

### --address

Specify a host and port for the Frontend Service.
The default is `127.0.0.1:7233`.

### --auto_confirm

Automatically confirm all prompts.

### --context_timeout

Specify a timeout for the context of an RPC call in seconds.
The default value is 5.

### --data_converter_plugin

Specify the name of the executable for a custom Data Converter plugin.

### --headers_provider_plugin

Specify the name of the executable for a headers provider plugin.

### --help

Display help for tctl in the CLI.

Alias: `-h`

### --namespace

Specify a Namespace.
By using this modifier, you don't need to specify a `--namespace` modifier for a sub-command.
The default Namespace is `default`.

Alias: `--n`

### --tls_ca_path

Specify the path to a server Certificate Authority (CA) certificate file.

### --tls_cert_path

Specify the path to a public X.509 certificate file for mutual TLS authentication.
If you use this modifier, you must also use the `--tls_key_path` modifier.

### --tls_disable_host_verification

Disable verification of the server certificate (and thus host verification).

### --tls_key_path

Specify the path to a private key file for mutual TLS authentication.
If you use this modifier, you must also use the `--tls_cert_path` modifier.

### --tls_server_name

Specify an override for the name of the target server that is used for TLS host verification.
The name must be one of the DNS names listed in the server TLS certificate.
Specifying this modifier also enables host verification.

### --version

Display the version of tctl in the CLI.

### --codec_endpoint

The URL and port number for a Codec Server.

## Environment variables

Setting environment variables for repeated parameters can shorten tctl commands.

### TEMPORAL_CLI_ADDRESS

Specify a host and port for the Frontend Service.
The default is `127.0.0.1:7233`.

### TEMPORAL_CLI_AUTHORIZATION_TOKEN

Specify a token to be used by the HTTP Basic Authorization plugin.

{/* TODO: Add link to "Securing tctl" page or its equivalent when it exists. */}

### TEMPORAL_CLI_AUTH

Specify the authorization header to be set for a gRPC request.

### TEMPORAL_CLI_NAMESPACE

Specify a Namespace.
By setting this variable, you don't need to specify a `--namespace` modifier in a tctl command.
The default Namespace is `default`.

### TEMPORAL_CLI_PLUGIN_DATA_CONVERTER

Specify the name of the executable for a custom Data Converter plugin.

### TEMPORAL_CLI_PLUGIN_HEADERS_PROVIDER

Specify the name of the executable for a headers provider plugin.

### TEMPORAL_CLI_TLS_CA

Specify the path to a server Certificate Authority (CA) certificate file.

### TEMPORAL_CLI_TLS_CERT

Specify the path to a public X.509 certificate file for mutual TLS authentication.

### TEMPORAL_CLI_TLS_DISABLE_HOST_VERIFICATION

Set to disable verification of the server certificate (and thus host verification).

### TEMPORAL_CLI_TLS_KEY

Specify the path to a private key file for mutual TLS authentication.
If you set this variable, you must also set the `TEMPORAL_CLI_TLS_CERT` variable.

### TEMPORAL_CLI_TLS_SERVER_NAME

Specify an override for the name of the target server that is used for TLS host verification.
The name must be one of the DNS names listed in the server TLS certificate.
Setting this variable also enables host verification.

### TEMPORAL_CONTEXT_TIMEOUT

Specify a timeout for the context of an RPC call in seconds.
The default value is 5.

---

## tctl v1.17 namespace command reference

:::info tctl is deprecated

The tctl command line utility has been deprecated and is no longer actively supported.
We recommend transitioning to [Temporal CLI](/cli) for continued use and access to new features.

Thank you for being a valued part of the Temporal community.

:::

The `tctl namespace` commands enable [Namespace](/namespaces) operations.

Alias: `n`

- [tctl namespace describe](#describe)
- [tctl namespace list](#list)
- [tctl namespace register](#register)
- [tctl namespace update](#update)

## describe

The `tctl namespace describe` command describes a [Namespace](/namespaces).

`tctl namespace describe`

The following modifier controls the behavior of the command.

### --namespace_id

Specify the ID of a Namespace to describe.

This modifier is required unless the global `--namespace` modifier is specified (`tctl --namespace <name> describe`).

**Example**

```bash
tctl namespace describe --namespace_id <id>
```

Example results for a [Global Namespace](/global-namespace)

```bash
$ tctl --ns canary-namespace n desc
Name: canary-namespace
Description: testing namespace
OwnerEmail: dev@yourtech.io
NamespaceData:
Status: REGISTERED
RetentionInDays: 7
EmitMetrics: true
ActiveClusterName: dc1
Clusters: dc1, dc2
```

## list

The `tctl namespace list` command lists all [Namespaces](/namespaces).

`tctl namespace list`

The command has no modifiers.

## register

The `tctl namespace register` command registers a [Namespace](/namespaces).

`tctl namespace register`

By default, Temporal uses a "default" Namespace.
Create and register a new Namespace with the following command:

```bash
tctl --namespace your-namespace namespace register
