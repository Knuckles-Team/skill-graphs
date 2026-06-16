```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--active-cluster` | No | **string** Active Cluster (Service) name. |
| `--cluster` | No | **string[]** Cluster (Service) names. |
| `--data` | No | **string[]** Namespace data as `KEY=VALUE` pairs. Keys must be identifiers, and values must be JSON values. For example: `YourKey={"your": "value"}` Can be passed multiple times. |
| `--description` | No | **string** Namespace description. |
| `--email` | No | **string** Owner email. |
| `--history-archival-state` | No | **string-enum** History archival state. Accepted values: disabled, enabled. |
| `--history-uri` | No | **string** Archive history to this `URI`. Once enabled, can't be changed. |
| `--promote-global` | No | **bool** Enable multi-region data replication. |
| `--replication-state` | No | **string-enum** Replication state. Accepted values: normal, handover. |
| `--retention` | No | **duration** Length of time a closed Workflow is preserved before deletion. |
| `--visibility-archival-state` | No | **string-enum** Visibility archival state. Accepted values: disabled, enabled. |
| `--visibility-uri` | No | **string** Archive visibility data to this `URI`. Once enabled, can't be changed. |

## nexus

These commands manage Nexus resources.

Nexus commands follow this syntax:

```
temporal operator nexus [command] [subcommand] [options]
```

### endpoint

These commands manage Nexus Endpoints.

Nexus Endpoint commands follow this syntax:

```
temporal operator nexus endpoint [command] [options]
```

#### create

Create a Nexus Endpoint on the Server.

A Nexus Endpoint name is used in Workflow code to invoke Nexus Operations.
The endpoint target may either be a Worker, in which case
`--target-namespace` and `--target-task-queue` must both be provided, or
an external URL, in which case `--target-url` must be provided.

This command will fail if an Endpoint with the same name is already
registered.

```
temporal operator nexus endpoint create \
  --name your-endpoint \
  --target-namespace your-namespace \
  --target-task-queue your-task-queue \
  --description-file DESCRIPTION.md
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--description` | No | **string** Nexus Endpoint description. You may use Markdown formatting in the Nexus Endpoint description. |
| `--description-file` | No | **string** Path to the Nexus Endpoint description file. The contents of the description file may use Markdown formatting. |
| `--name` | Yes | **string** Endpoint name. |
| `--target-namespace` | No | **string** Namespace where a handler Worker polls for Nexus tasks. |
| `--target-task-queue` | No | **string** Task Queue that a handler Worker polls for Nexus tasks. |
| `--target-url` | No | **string** An external Nexus Endpoint that receives forwarded Nexus requests. May be used as an alternative to `--target-namespace` and `--target-task-queue`. _(Experimental)_ |

#### delete

Delete a Nexus Endpoint from the Server.

```
temporal operator nexus endpoint delete --name your-endpoint
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--name` | Yes | **string** Endpoint name. |

#### get

Get a Nexus Endpoint by name from the Server.

```
temporal operator nexus endpoint get --name your-endpoint
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--name` | Yes | **string** Endpoint name. |

#### list

List all Nexus Endpoints on the Server.

```
temporal operator nexus endpoint list
```

Use [global flags](#global-flags) to customize the connection to the Temporal Service for this command.

#### update

Update an existing Nexus Endpoint on the Server.

A Nexus Endpoint name is used in Workflow code to invoke Nexus Operations.
The Endpoint target may either be a Worker, in which case
`--target-namespace` and `--target-task-queue` must both be provided, or
an external URL, in which case `--target-url` must be provided.

The Endpoint is patched; existing fields for which flags are not provided
are left as they were.

Update only the target task queue:

```
temporal operator nexus endpoint update \
  --name your-endpoint \
  --target-task-queue your-other-queue
```

Update only the description:

```
temporal operator nexus endpoint update \
  --name your-endpoint \
  --description-file DESCRIPTION.md
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--description` | No | **string** Nexus Endpoint description. You may use Markdown formatting in the Nexus Endpoint description. |
| `--description-file` | No | **string** Path to the Nexus Endpoint description file. The contents of the description file may use Markdown formatting. |
| `--name` | Yes | **string** Endpoint name. |
| `--target-namespace` | No | **string** Namespace where a handler Worker polls for Nexus tasks. |
| `--target-task-queue` | No | **string** Task Queue that a handler Worker polls for Nexus tasks. |
| `--target-url` | No | **string** An external Nexus Endpoint that receives forwarded Nexus requests. May be used as an alternative to `--target-namespace` and `--target-task-queue`. _(Experimental)_ |
| `--unset-description` | No | **bool** Unset the description. |

## search-attribute

Create, list, or remove Search Attributes fields stored in a Workflow
Execution's metadata:

```
temporal operator search-attribute create \
    --name YourAttributeName \
    --type Keyword
```

Supported types include: Text, Keyword, Int, Double, Bool, Datetime, and
KeywordList.

If you wish to delete a Search Attribute, please contact support
at https://support.temporal.io.

### create

Add one or more custom Search Attributes:

```
temporal operator search-attribute create \
    --name YourAttributeName \
    --type Keyword
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--name` | Yes | **string[]** Search Attribute name. |
| `--type` | Yes | **string-enum[]** Search Attribute type. Accepted values: Text, Keyword, Int, Double, Bool, Datetime, KeywordList. |

### list

Display a list of active Search Attributes that can be assigned or used with
Workflow Queries. You can manage this list and add attributes as needed:

```
temporal operator search-attribute list
```

Use [global flags](#global-flags) to customize the connection to the Temporal Service for this command.

### remove

Remove custom Search Attributes from the options that can be assigned or used
with Workflow Queries.

```
temporal operator search-attribute remove \
    --name YourAttributeName
```

Remove attributes without confirmation:

```
temporal operator search-attribute remove \
    --name YourAttributeName \
    --yes
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--name` | Yes | **string[]** Search Attribute name. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm removal. |

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

## Temporal CLI schedule command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli/blob/main/internal/commandsgen/commands.yml via internal/cmd/gen-docs */}

This page provides a reference for the `temporal` CLI `schedule` command. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## backfill

Batch-execute actions that would have run during a specified time interval.
Use this command to fill in Workflow runs from when a Schedule was paused,
before a Schedule was created, from the future, or to re-process a previously
executed interval.

Backfills require a Schedule ID and the time period covered by the request.
It's best to use the `BufferAll` or `AllowAll` policies to avoid conflicts
and ensure no Workflow Executions are skipped.

For example:

```
temporal schedule backfill \
    --schedule-id "YourScheduleId" \
    --start-time "2022-05-01T00:00:00Z" \
    --end-time "2022-05-31T23:59:59Z" \
    --overlap-policy BufferAll
```

The policies include:

* **AllowAll**: Allow unlimited concurrent Workflow Executions. This
  significantly speeds up the backfilling process on systems that support
  concurrency. You must ensure running Workflow Executions do not interfere
  with each other.
* **BufferAll**: Buffer all incoming Workflow Executions while waiting for
  the running Workflow Execution to complete.
* **Skip**: If a previous Workflow Execution is still running, discard new
  Workflow Executions.
* **BufferOne**: Same as 'Skip' but buffer a single Workflow Execution to be
  run after the previous Execution completes. Discard other Workflow
  Executions.
* **CancelOther**: Cancel the running Workflow Execution and replace it with
  the incoming new Workflow Execution.
* **TerminateOther**: Terminate the running Workflow Execution and replace
  it with the incoming new Workflow Execution.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--end-time` | Yes | **timestamp** Backfill end time. |
| `--overlap-policy` | No | **string-enum** Policy for handling overlapping Workflow Executions. Accepted values: Skip, BufferOne, BufferAll, CancelOther, TerminateOther, AllowAll. |
| `--schedule-id`, `-s` | Yes | **string** Schedule ID. |
| `--start-time` | Yes | **timestamp** Backfill start time. |

## create

Create a new Schedule on the Temporal Service. A Schedule automatically starts
new Workflow Executions at the times you specify.

For example:

```
  temporal schedule create \
    --schedule-id "YourScheduleId" \
    --calendar '{"dayOfWeek":"Fri","hour":"3","minute":"30"}' \
    --workflow-id YourBaseWorkflowIdName \
    --task-queue YourTaskQueue \
    --type YourWorkflowType
```

Schedules support any combination of `--calendar`, `--interval`, and `--cron`:

* Shorthand `--interval` strings.
  For example: 45m (every 45 minutes) or 6h/5h (every 6 hours, at the top of
  the 5th hour).
* JSON `--calendar`, as in the preceding example.
* Unix-style `--cron` strings and robfig declarations
  (@daily/@weekly/@every X/etc).
  For example, every Friday at 12:30 PM: `30 12 * * Fri`.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--calendar` | No | **string[]** Calendar specification in JSON. For example: `{"dayOfWeek":"Fri","hour":"17","minute":"5"}`. |
| `--catchup-window` | No | **duration** Maximum catch-up time for when the Service is unavailable. |
| `--cron` | No | **string[]** Calendar specification in cron string format. For example: `"30 12 * * Fri"`. |
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
| `--schedule-memo` | No | **string[]** Set schedule memo using `KEY="VALUE` pairs. Keys must be identifiers, and values must be JSON values. For example: `'YourKey={"your": "value"}'`. Can be passed multiple times. |
| `--schedule-search-attribute` | No | **string[]** Set schedule Search Attributes using `KEY="VALUE` pairs. Keys must be identifiers, and values must be JSON values. For example: `'YourKey={"your": "value"}'`. Can be passed multiple times. |
| `--search-attribute` | No | **string[]** Search Attribute in `KEY=VALUE` format. Keys must be identifiers, and values must be JSON values. For example: `'YourKey={"your": "value"}'`. Can be passed multiple times. |
| `--start-time` | No | **timestamp** Schedule start time. |
| `--static-details` | No | **string** Static Workflow details for human consumption in UIs. Uses Temporal Markdown formatting, may be multiple lines. _(Experimental)_ |
| `--static-summary` | No | **string** Static Workflow summary for human consumption in UIs. Uses Temporal Markdown formatting, should be a single line. _(Experimental)_ |
| `--task-queue`, `-t` | Yes | **string** Workflow Task queue. |
| `--task-timeout` | No | **duration** Fail a Workflow Task if it lasts longer than `DURATION`. This is the Start-to-close timeout for a Workflow Task. |
| `--time-zone` | No | **string** Interpret calendar specs with the `TZ` time zone. For a list of time zones, see: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. |
| `--type` | Yes | **string** Workflow Type name. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. If not supplied, the Service generates a unique ID. |

## delete

Deletes a Schedule on the front end Service:

```
temporal schedule delete \
    --schedule-id YourScheduleId
```

Removing a Schedule won't affect the Workflow Executions it started that are
still running. To cancel or terminate these Workflow Executions, use `temporal
workflow delete` with the `TemporalScheduledById` Search Attribute instead.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--schedule-id`, `-s` | Yes | **string** Schedule ID. |

## describe

Show a Schedule configuration, including information about past, current, and
future Workflow runs:

```
temporal schedule describe \
    --schedule-id YourScheduleId
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--schedule-id`, `-s` | Yes | **string** Schedule ID. |

## list

Lists the Schedules hosted by a Namespace:

```
temporal schedule list \
    --namespace YourNamespace
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--long`, `-l` | No | **bool** Show detailed information. |
| `--query`, `-q` | No | **string** Filter results using given List Filter. |
| `--really-long` | No | **bool** Show extensive information in non-table form. |

## list-matching-times

Note: This is an experimental feature and may change in the future.

List the times a Schedule's spec would match within a given time
range. The time range may be in the past or future. Use this
command to preview when a Schedule will take actions without
actually running them.

For example:

```
  temporal schedule list-matching-times \
    --schedule-id "YourScheduleId" \
    --start-time "2024-01-01T00:00:00Z" \
    --end-time "2024-01-31T23:59:59Z"
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--end-time` | Yes | **timestamp** End of time range to list matching times. |
| `--schedule-id`, `-s` | Yes | **string** Schedule ID. |
| `--start-time` | Yes | **timestamp** Start of time range to list matching times. |

## toggle

Pause or unpause a Schedule by passing a flag with your desired state:

```
temporal schedule toggle \
    --schedule-id "YourScheduleId" \
    --pause \
    --reason "YourReason"
```

and

```
temporal schedule toggle
    --schedule-id "YourScheduleId" \
    --unpause \
    --reason "YourReason"
```

The `--reason` text updates the Schedule's `notes` field for operations
communication. It defaults to "(no reason provided)" if omitted. This field is
also visible on the Service Web UI.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--pause` | No | **bool** Pause the Schedule. |
| `--reason` | No | **string** Reason for pausing or unpausing the Schedule. |
| `--schedule-id`, `-s` | Yes | **string** Schedule ID. |
| `--unpause` | No | **bool** Unpause the Schedule. |

## trigger

Trigger a Schedule to run immediately:

```
temporal schedule trigger \
    --schedule-id "YourScheduleId"
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--overlap-policy` | No | **string-enum** Policy for handling overlapping Workflow Executions. Accepted values: Skip, BufferOne, BufferAll, CancelOther, TerminateOther, AllowAll. |
| `--schedule-id`, `-s` | Yes | **string** Schedule ID. |

## update

Update an existing Schedule with new configuration details, including time
specifications, action, and policies:

```
temporal schedule update \
    --schedule-id "YourScheduleId" \
    --workflow-type "NewWorkflowType"
```

This command performs a full replacement of the Schedule
configuration. Any options not provided will be reset to their default
values. You must re-specify all options, not just the ones you want to
change. To view the current configuration of a Schedule, use
`temporal schedule describe` before updating.

Schedule memo and search attributes cannot be updated with this
command. They are set only during Schedule creation and are not affected
by updates.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--calendar` | No | **string[]** Calendar specification in JSON. For example: `{"dayOfWeek":"Fri","hour":"17","minute":"5"}`. |
| `--catchup-window` | No | **duration** Maximum catch-up time for when the Service is unavailable. |
| `--cron` | No | **string[]** Calendar specification in cron string format. For example: `"30 12 * * Fri"`. |
