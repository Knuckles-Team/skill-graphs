| `--end-time` | No | **timestamp** Schedule end time. |
| `--execution-timeout` | No | **duration** Fail a WorkflowExecution if it lasts longer than `DURATION`. This time-out includes retries and ContinueAsNew tasks. |
| `--fairness-key` | No | **string** Fairness key (max 64 bytes) for proportional task dispatch. Tasks with same key share capacity based on their weight. |
| `--fairness-weight` | No | **float** Weight [0.001-1000] for this fairness key. Keys are dispatched proportionally to their weights. |
| `--headers` | No | **string[]** Temporal workflow headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times to set multiple Temporal headers. Note: These are workflow headers, not gRPC headers. |
| `--input`, `-i` | No | **string[]** Input value. Use JSON content or set --input-meta to override. Can't be combined with --input-file. Can be passed multiple times to pass multiple arguments. |
| `--input-base64` | No | **bool** Assume inputs are base64-encoded and attempt to decode them. |
| `--input-file` | No | **string[]** A path or paths for input file(s). Use JSON content or set --input-meta to override. Can't be combined with --input. Can be passed multiple times to pass multiple arguments. |
| `--input-meta` | No | **string[]** Input payload metadata as a `KEY=VALUE` pair. When the KEY is "encoding", this overrides the default ("json/plain"). Can be passed multiple times. Repeated metadata keys are applied to the corresponding inputs in the provided order. |
| `--interval` | No | **string[]** Interval duration. For example, 90m, or 60m/15m to include phase offset. |
| `--jitter` | No | **duration** Max difference in time from the specification. Vary the start time randomly within this amount. |
| `--memo` | No | **string[]** Memo using 'KEY="VALUE"' pairs. Use JSON values. |
| `--notes` | No | **string** Initial notes field value. |
| `--overlap-policy` | No | **string-enum** Policy for handling overlapping Workflow Executions. Accepted values: Skip, BufferOne, BufferAll, CancelOther, TerminateOther, AllowAll. |
| `--pause-on-failure` | No | **bool** Pause schedule after Workflow failures. |
| `--paused` | No | **bool** Pause the Schedule immediately on creation. |
| `--priority-key` | No | **int** Priority key (1-5, lower numbers = higher priority). Tasks in a queue should be processed in close-to-priority-order. Default is 3 when not specified. |
| `--remaining-actions` | No | **int** Total allowed actions. Default is zero (unlimited). |
| `--run-timeout` | No | **duration** Fail a Workflow Run if it lasts longer than `DURATION`. |
| `--schedule-id`, `-s` | Yes | **string** Schedule ID. |
| `--search-attribute` | No | **string[]** Search Attribute in `KEY=VALUE` format. Keys must be identifiers, and values must be JSON values. For example: `'YourKey={"your": "value"}'`. Can be passed multiple times. |
| `--start-time` | No | **timestamp** Schedule start time. |
| `--static-details` | No | **string** Static Workflow details for human consumption in UIs. Uses Temporal Markdown formatting, may be multiple lines. _(Experimental)_ |
| `--static-summary` | No | **string** Static Workflow summary for human consumption in UIs. Uses Temporal Markdown formatting, should be a single line. _(Experimental)_ |
| `--task-queue`, `-t` | Yes | **string** Workflow Task queue. |
| `--task-timeout` | No | **duration** Fail a Workflow Task if it lasts longer than `DURATION`. This is the Start-to-close timeout for a Workflow Task. |
| `--time-zone` | No | **string** Interpret calendar specs with the `TZ` time zone. For a list of time zones, see: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. |
| `--type` | Yes | **string** Workflow Type name. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. If not supplied, the Service generates a unique ID. |

## Global Flags

The following options can be used with any command.

| Flag | Required | Description | Default |
|------|----------|-------------|--------|
| `--address` | No | **string** Temporal Service gRPC endpoint. | `localhost:7233` |
| `--api-key` | No | **string** API key for request. |  |
| `--client-authority` | No | **string** Temporal gRPC client :authority pseudoheader. |  |
| `--client-connect-timeout` | No | **duration** The client connection timeout. 0s means no timeout. |  |
| `--codec-auth` | No | **string** Authorization header for Codec Server requests. |  |
| `--codec-endpoint` | No | **string** Remote Codec Server endpoint. |  |
| `--codec-header` | No | **string[]** HTTP headers for requests to codec server. Format as a `KEY=VALUE` pair. May be passed multiple times to set multiple headers. |  |
| `--color` | No | **string-enum** Output coloring. Accepted values: always, never, auto. | `auto` |
| `--command-timeout` | No | **duration** The command execution timeout. 0s means no timeout. |  |
| `--config-file` | No | **string** File path to read TOML config from, defaults to `$CONFIG_PATH/temporalio/temporal.toml` where `$CONFIG_PATH` is defined as `$HOME/.config` on Unix, `$HOME/Library/Application Support` on macOS, and `%AppData%` on Windows. |  |
| `--disable-config-env` | No | **bool** If set, disables loading environment config from environment variables. |  |
| `--disable-config-file` | No | **bool** If set, disables loading environment config from config file. |  |
| `--env` | No | **string** Active environment name (`ENV`). | `default` |
| `--env-file` | No | **string** Path to environment settings file. Defaults to `$HOME/.config/temporalio/temporal.yaml`. |  |
| `--grpc-meta` | No | **string[]** HTTP headers for requests. Format as a `KEY=VALUE` pair. May be passed multiple times to set multiple headers. Can also be made available via environment variable as `TEMPORAL_GRPC_META_[name]`. |  |
| `--identity` | No | **string** The identity of the user or client submitting this request. Defaults to "temporal-cli:$USER@$HOST". |  |
| `--log-format` | No | **string-enum** Log format. Accepted values: text, json. | `text` |
| `--log-level` | No | **string-enum** Log level. Default is "never" for most commands and "warn" for "server start-dev". Accepted values: debug, info, warn, error, never. | `never` |
| `--namespace`, `-n` | No | **string** Temporal Service Namespace. | `default` |
| `--no-json-shorthand-payloads` | No | **bool** Raw payload output, even if the JSON option was used. |  |
| `--output`, `-o` | No | **string-enum** Non-logging data output format. Accepted values: text, json, jsonl, none. | `text` |
| `--profile` | No | **string** Profile to use for config file. |  |
| `--time-format` | No | **string-enum** Time format. Accepted values: relative, iso, raw. | `relative` |
| `--tls` | No | **bool** Enable base TLS encryption. Does not have additional options like mTLS or client certs. This is defaulted to true if api-key or any other TLS options are present. Use --tls=false to explicitly disable. |  |
| `--tls-ca-data` | No | **string** Data for server CA certificate. Can't be used with --tls-ca-path. |  |
| `--tls-ca-path` | No | **string** Path to server CA certificate. Can't be used with --tls-ca-data. |  |
| `--tls-cert-data` | No | **string** Data for x509 certificate. Can't be used with --tls-cert-path. |  |
| `--tls-cert-path` | No | **string** Path to x509 certificate. Can't be used with --tls-cert-data. |  |
| `--tls-disable-host-verification` | No | **bool** Disable TLS host-name verification. |  |
| `--tls-key-data` | No | **string** Private certificate key data. Can't be used with --tls-key-path. |  |
| `--tls-key-path` | No | **string** Path to x509 private key. Can't be used with --tls-key-data. |  |
| `--tls-server-name` | No | **string** Override target TLS server name. |  |

---

## Temporal CLI server command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli/blob/main/internal/commandsgen/commands.yml via internal/cmd/gen-docs */}

This page provides a reference for the `temporal` CLI `server` command. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## start-dev

Run a development Temporal Server on your local system.

```
+------------------------------------------------------------------------+
| WARNING: The development server is not intended for production use.    |
| It skips certain HTTP security checks to make local use simpler.       |
|                                                                        |
| For production use, see:                                               |
| https://docs.temporal.io/production-deployment                         |
+------------------------------------------------------------------------+
```

View the Web UI for the default configuration at: http://localhost:8233

```
temporal server start-dev
```

Add persistence for Workflow Executions across runs:

```
temporal server start-dev \
    --db-filename path-to-your-local-persistent-store
```

Set the port from the front-end gRPC Service (7233 default):

```
temporal server start-dev \
    --port 7000
```

Use a custom port for the Web UI. The default is the gRPC port (7233 default)
plus 1000 (8233):

```
temporal server start-dev \
    --ui-port 3000
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--db-filename`, `-f` | No | **string** Path to file for persistent Temporal state store. By default, Workflow Executions are lost when the server process dies. |
| `--dynamic-config-value` | No | **string[]** Dynamic configuration value using `KEY=VALUE` pairs. Keys must be identifiers, and values must be JSON values. For example: `YourKey="YourString"` Can be passed multiple times. |
| `--headless` | No | **bool** Disable the Web UI. |
| `--http-port` | No | **int** Port for the HTTP API service. Defaults to a random free port. |
| `--ip` | No | **string** IP address bound to the front-end Service. |
| `--log-config` | No | **bool** Print the server config to stderr. |
| `--metrics-port` | No | **int** Port for the '/metrics' HTTP endpoint. Defaults to a random free port. |
| `--namespace`, `-n` | No | **string[]** Namespaces to be created at launch. The "default" Namespace is always created automatically. |
| `--port`, `-p` | No | **int** Port for the front-end gRPC Service. |
| `--search-attribute` | No | **string[]** Search attributes to register using `KEY=VALUE` pairs. Keys must be identifiers, and values must be the search attribute type, which is one of the following: Text, Keyword, Int, Double, Bool, Datetime, KeywordList. |
| `--sqlite-pragma` | No | **string[]** SQLite pragma statements in "PRAGMA=VALUE" format. |
| `--ui-asset-path` | No | **string** UI custom assets path. |
| `--ui-codec-endpoint` | No | **string** UI remote codec HTTP endpoint. |
| `--ui-ip` | No | **string** IP address bound to the Web UI. Defaults to same as '--ip' value. |
| `--ui-port` | No | **int** Port for the Web UI. Defaults to '--port' value + 1000. |
| `--ui-public-path` | No | **string** The public base path for the Web UI. Defaults to `/`. |

## Global Flags

The following options can be used with any command.

| Flag | Required | Description | Default |
|------|----------|-------------|--------|
| `--address` | No | **string** Temporal Service gRPC endpoint. | `localhost:7233` |
| `--api-key` | No | **string** API key for request. |  |
| `--client-authority` | No | **string** Temporal gRPC client :authority pseudoheader. |  |
| `--client-connect-timeout` | No | **duration** The client connection timeout. 0s means no timeout. |  |
| `--codec-auth` | No | **string** Authorization header for Codec Server requests. |  |
| `--codec-endpoint` | No | **string** Remote Codec Server endpoint. |  |
| `--codec-header` | No | **string[]** HTTP headers for requests to codec server. Format as a `KEY=VALUE` pair. May be passed multiple times to set multiple headers. |  |
| `--color` | No | **string-enum** Output coloring. Accepted values: always, never, auto. | `auto` |
| `--command-timeout` | No | **duration** The command execution timeout. 0s means no timeout. |  |
| `--config-file` | No | **string** File path to read TOML config from, defaults to `$CONFIG_PATH/temporalio/temporal.toml` where `$CONFIG_PATH` is defined as `$HOME/.config` on Unix, `$HOME/Library/Application Support` on macOS, and `%AppData%` on Windows. |  |
| `--disable-config-env` | No | **bool** If set, disables loading environment config from environment variables. |  |
| `--disable-config-file` | No | **bool** If set, disables loading environment config from config file. |  |
| `--env` | No | **string** Active environment name (`ENV`). | `default` |
| `--env-file` | No | **string** Path to environment settings file. Defaults to `$HOME/.config/temporalio/temporal.yaml`. |  |
| `--grpc-meta` | No | **string[]** HTTP headers for requests. Format as a `KEY=VALUE` pair. May be passed multiple times to set multiple headers. Can also be made available via environment variable as `TEMPORAL_GRPC_META_[name]`. |  |
| `--identity` | No | **string** The identity of the user or client submitting this request. Defaults to "temporal-cli:$USER@$HOST". |  |
| `--log-format` | No | **string-enum** Log format. Accepted values: text, json. | `text` |
| `--log-level` | No | **string-enum** Log level. Default is "never" for most commands and "warn" for "server start-dev". Accepted values: debug, info, warn, error, never. | `never` |
| `--namespace`, `-n` | No | **string** Temporal Service Namespace. | `default` |
| `--no-json-shorthand-payloads` | No | **bool** Raw payload output, even if the JSON option was used. |  |
| `--output`, `-o` | No | **string-enum** Non-logging data output format. Accepted values: text, json, jsonl, none. | `text` |
| `--profile` | No | **string** Profile to use for config file. |  |
| `--time-format` | No | **string-enum** Time format. Accepted values: relative, iso, raw. | `relative` |
| `--tls` | No | **bool** Enable base TLS encryption. Does not have additional options like mTLS or client certs. This is defaulted to true if api-key or any other TLS options are present. Use --tls=false to explicitly disable. |  |
| `--tls-ca-data` | No | **string** Data for server CA certificate. Can't be used with --tls-ca-path. |  |
| `--tls-ca-path` | No | **string** Path to server CA certificate. Can't be used with --tls-ca-data. |  |
| `--tls-cert-data` | No | **string** Data for x509 certificate. Can't be used with --tls-cert-path. |  |
| `--tls-cert-path` | No | **string** Path to x509 certificate. Can't be used with --tls-cert-data. |  |
| `--tls-disable-host-verification` | No | **bool** Disable TLS host-name verification. |  |
| `--tls-key-data` | No | **string** Private certificate key data. Can't be used with --tls-key-path. |  |
| `--tls-key-path` | No | **string** Path to x509 private key. Can't be used with --tls-key-data. |  |
| `--tls-server-name` | No | **string** Override target TLS server name. |  |

---

## Temporal CLI task-queue command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli/blob/main/internal/commandsgen/commands.yml via internal/cmd/gen-docs */}

This page provides a reference for the `temporal` CLI `task-queue` command. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## config

Manage Task Queue configuration:

```
temporal task-queue config [command] [options]
```

Available commands:
- `get`: Retrieve the current configuration for a task queue
- `set`: Update the configuration for a task queue

### get

Retrieve the current configuration for a Task Queue:

```
temporal task-queue config get \
    --task-queue YourTaskQueue \
    --task-queue-type activity
```

This command returns the current configuration including:
- Queue rate limit: The overall rate limit of the task queue.
  This setting overrides the worker rate limit if set.
  Unless modified, this is the system-defined rate limit.
- Fairness key rate limit defaults: Default rate limits for fairness keys.
  If set, each individual fairness key will be limited to this rate,
  scaled by the weight of the fairness key.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--task-queue`, `-t` | Yes | **string** Task Queue name. |
| `--task-queue-type` | Yes | **string-enum** Task Queue type. Accepted values: workflow, activity, nexus. Accepted values: workflow, activity, nexus. |

### set

Update configuration settings for a Task Queue.

```
temporal task-queue config set \
    --task-queue YourTaskQueue \
    --task-queue-type activity \
    --namespace YourNamespace \
    --queue-rps-limit <requests_per_second:float> \
    --queue-rps-limit-reason <reason_string> \
    --fairness-key-rps-limit-default <requests_per_second:float> \
    --fairness-key-rps-limit-reason <reason_string> \
    --fairness-key-weight HighPriority=2.0 \
    --fairness-key-weight LowPriority=0.5
```

This command supports updating:
- Queue rate limits: Controls the overall rate limit of the task queue.
  This setting overrides the worker rate limit if set.
  Unless modified, this is the system-defined rate limit.
- Fairness key rate limit defaults: Sets default rate limits for fairness keys.
  If set, each individual fairness key will be limited to this rate,
  scaled by the weight of the fairness key.
- Fairness key weight overrides: Set custom weights for specific fairness keys.
  Weights control the relative share of capacity each key receives.

To unset a rate limit, pass in 'default', for example: --queue-rps-limit default
To unset a specific fairness weight, use --fairness-key-weight \<key\>=default
To unset all fairness weights, use --fairness-key-weight-clear-all

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--fairness-key-rps-limit-default` | No | **float\|default** Fairness key rate limit default in requests per second. Accepts a float; or 'default' to unset. |
| `--fairness-key-rps-limit-reason` | No | **string** Reason for fairness key rate limit update. |
| `--fairness-key-weight` | No | **string[]** Set or unset fairness key weight overrides in format key=weight or key=default. Use key=weight to set a positive weight value; use key=default to unset. Can be specified multiple times. Example: --fairness-key-weight HighPriority=2.0 --fairness-key-weight LowPriority=default. |
| `--fairness-key-weight-clear-all` | No | **bool** Unset all fairness key weight overrides. Cannot be used with --fairness-key-weight. |
| `--queue-rps-limit` | No | **float\|default** Queue rate limit in requests per second. Accepts a float; or 'default' to unset. |
| `--queue-rps-limit-reason` | No | **string** Reason for queue rate limit update. |
| `--task-queue`, `-t` | Yes | **string** Task Queue name. |
| `--task-queue-type` | Yes | **string-enum** Task Queue type. Accepted values: workflow, activity, nexus. Accepted values: workflow, activity, nexus. |

## describe

Display a list of active Workers that have recently polled a Task Queue. The
Temporal Server records each poll request time. A `LastAccessTime` over one
minute may indicate the Worker is at capacity or has shut down. Temporal
Workers are removed if 5 minutes have passed since the last poll request.

```
temporal task-queue describe \
  --task-queue YourTaskQueue
```

This command provides poller information for a given Task Queue.
Workflow and Activity polling use separate Task Queues:

```
temporal task-queue describe \
    --task-queue YourTaskQueue \
    --task-queue-type "activity"
```

This command provides the following task queue statistics:
- `ApproximateBacklogCount`: The approximate number of tasks backlogged in this
  task queue. May count expired tasks but eventually converges to the right
  value.
- `ApproximateBacklogAge`: Approximate age of the oldest task in the backlog,
  based on its creation time, measured in seconds.
- `TasksAddRate`: Approximate rate at which tasks are being added to the task
  queue, measured in tasks per second, averaged over the last 30 seconds.
  Includes tasks dispatched immediately without going to the backlog
  (sync-matched tasks), as well as tasks added to the backlog. (See note below.)
- `TasksDispatchRate`: Approximate rate at which tasks are being dispatched from
  the task queue, measured in tasks per second, averaged over the last 30
  seconds.  Includes tasks dispatched immediately without going to the backlog
  (sync-matched tasks), as well as tasks added to the backlog. (See note below.)
- `BacklogIncreaseRate`: Approximate rate at which the backlog size is
  increasing (if positive) or decreasing (if negative), measured in tasks per
  second, averaged over the last 30 seconds.  This is roughly equivalent to:
  `TasksAddRate` - `TasksDispatchRate`.

NOTE: The `TasksAddRate` and `TasksDispatchRate` metrics may differ from the
actual rate of add/dispatch, because tasks may be dispatched eagerly to an
available worker, or may apply only to specific workers (they are "sticky").
Such tasks are not counted by these metrics. Despite the inaccuracy of
these two metrics, the derived metric of `BacklogIncreaseRate` is accurate
for backlogs older than a few seconds.

Safely retire Workers assigned a Build ID by checking reachability across
all task types. Use the flag `--report-reachability`:

```
temporal task-queue describe \
    --task-queue YourTaskQueue \
    --select-build-id "YourBuildId" \
    --report-reachability
```

Task reachability information is returned for the requested versions and all
task types, which can be used to safely retire Workers with old code versions,
provided that they were assigned a Build ID.

Note that task reachability status is deprecated in favor of Drainage Status
(ie. of a Drained or Draining Worker Deployment Version) and will be removed
in a future release. Also, determining task reachability incurs a non-trivial
computing cost.

Task reachability states are reported per build ID. The state may be one of the
following:

- `Reachable`: using the current versioning rules, the Build ID may be used
  by new Workflow Executions or Activities OR there are currently open
  Workflow or backlogged Activity tasks assigned to the queue.
- `ClosedWorkflowsOnly`: the Build ID does not have open Workflow Executions
  and can't be reached by new Workflow Executions. It MAY have closed
  Workflow Executions within the Namespace retention period.
- `Unreachable`: this Build ID is not used for new Workflow Executions and
  isn't used by any existing Workflow Execution within the retention period.

Task reachability is eventually consistent. You may experience a delay until
reachability converges to the most accurate value. This is designed to act
in the most conservative way until convergence. For example, `Reachable` is
more conservative than `ClosedWorkflowsOnly`.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--disable-stats` | No | **bool** Disable task queue statistics. |
| `--legacy-mode` | No | **bool** Enable a legacy mode for servers that do not support rules-based worker versioning. This mode only provides pollers info. |
| `--partitions-legacy` | No | **int** Query partitions 1 through `N`. Experimental/Temporary feature. Legacy mode only. |
| `--report-config` | No | **bool** Include task queue configuration in the response. When enabled, the command will return the current rate limit configuration for the task queue. |
| `--report-reachability` | No | **bool** Display task reachability information. |
| `--select-all-active` | No | **bool** Include all active versions. A version is active if it had new tasks or polls recently. |
| `--select-build-id` | No | **string[]** Filter the Task Queue based on Build ID. |
| `--select-unversioned` | No | **bool** Include the unversioned queue. |
| `--task-queue`, `-t` | Yes | **string** Task Queue name. |
| `--task-queue-type` | No | **string-enum[]** Task Queue type. If not specified, all types are reported. Accepted values: workflow, activity, nexus. |
| `--task-queue-type-legacy` | No | **string-enum** Task Queue type (legacy mode only). Accepted values: workflow, activity. |

## get-build-id-reachability

```
+-----------------------------------------------------------------------------+
| CAUTION: This command is deprecated and will be removed in a later release. |
+-----------------------------------------------------------------------------+
```

Show if a given Build ID can be used for new, existing, or closed Workflows
in Namespaces that support Worker versioning:
