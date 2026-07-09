| `--headers` | No | **string[]** Temporal workflow headers in 'KEY=VALUE' format. Keys must be identifiers, and values must be JSON values. May be passed multiple times to set multiple Temporal headers. Note: These are workflow headers, not gRPC headers. |
| `--heartbeat-timeout` | No | **duration** Maximum permitted time between successful worker heartbeats. |
| `--query`, `-q` | No | **string** Content for an SQL-like `QUERY` List Filter. You must set either --workflow-id or --query. Note: Using --query for batch activity operations is an experimental feature and may change in the future. |
| `--reason` | No | **string** Reason for batch operation. Only use with --query. Defaults to user name. |
| `--restore-original-options` | No | **bool** Restore the original options of the activity. |
| `--retry-backoff-coefficient` | No | **float** Coefficient used to calculate the next retry interval. The next retry interval is previous interval multiplied by the backoff coefficient. Must be 1 or larger. |
| `--retry-initial-interval` | No | **duration** Interval of the first retry. If retryBackoffCoefficient is 1.0 then it is used for all retries. |
| `--retry-maximum-attempts` | No | **int** Maximum number of attempts. When exceeded the retries stop even if not expired yet. Setting this value to 1 disables retries. Setting this value to 0 means unlimited attempts(up to the timeouts). |
| `--retry-maximum-interval` | No | **duration** Maximum interval between retries. Exponential backoff leads to interval increase. This value is the cap of the increase. |
| `--rps` | No | **float** Limit batch's requests per second. Only allowed if query is present. |
| `--run-id`, `-r` | No | **string** Run ID. Only use with --workflow-id. Cannot use with --query. |
| `--schedule-to-close-timeout` | No | **duration** Indicates how long the caller is willing to wait for an activity completion. Limits how long retries will be attempted. |
| `--schedule-to-start-timeout` | No | **duration** Limits time an activity task can stay in a task queue before a worker picks it up. This timeout is always non retryable, as all a retry would achieve is to put it back into the same queue. Defaults to the schedule-to-close timeout or workflow execution timeout if not specified. |
| `--start-to-close-timeout` | No | **duration** Maximum time an activity is allowed to execute after being picked up by a worker. This timeout is always retryable. |
| `--task-queue` | No | **string** Name of the task queue for the Activity. |
| `--workflow-id`, `-w` | No | **string** Workflow ID. You must set either --workflow-id or --query. |
| `--yes`, `-y` | No | **bool** Don't prompt to confirm signaling. Only allowed when --query is present. |

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

## Temporal CLI batch command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli/blob/main/internal/commandsgen/commands.yml via internal/cmd/gen-docs */}

This page provides a reference for the `temporal` CLI `batch` command. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## describe

Show the progress of an ongoing batch job. Pass a valid job ID to display its
information:

```
temporal batch describe \
    --job-id YourJobId
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--job-id` | Yes | **string** Batch job ID. |

## list

Return a list of batch jobs on the Service or within a single Namespace. For
example, list the batch jobs for "YourNamespace":

```
temporal batch list \
    --namespace YourNamespace
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--limit` | No | **int** Maximum number of batch jobs to display. |

## terminate

Terminate a batch job with the provided job ID. You must provide a reason for
the termination. The Service stores this explanation as metadata for the
termination event for later reference:

```
temporal batch terminate \
    --job-id YourJobId \
    --reason YourTerminationReason
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--job-id` | Yes | **string** Job ID to terminate. |
| `--reason` | Yes | **string** Reason for terminating the batch job. |

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

## Temporal CLI cloud account command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud account` commands. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## audit-log

Commands for working with account audit logs.

### audit-log list

Returns a paginated list of audit logs for the account, optionally filtered by time range.

Example:
  temporal cloud account audit-log get --page-size 50
  temporal cloud account audit-log get --start-time 2024-01-01T00:00:00Z --end-time 2024-02-01T00:00:00Z

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--end-time` | No | **timestamp** Filter for logs before this UTC time (RFC3339 format, e.g. 2024-02-01T00:00:00Z). Defaults to current time. |
| `--page-size` | No | **int** Number of logs to retrieve per page. Cannot exceed 1000. Defaults to 100. |
| `--page-token` | No | **string** Page token from a previous response to retrieve the next page. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--start-time` | No | **timestamp** Filter for logs at or after this UTC time (RFC3339 format, e.g. 2024-01-01T00:00:00Z). Defaults to 30 days ago. |

### audit-log sink

Commands for working with account audit log sinks.

#### audit-log sink delete

Delete an audit log sink for the account. This action is irreversible.

Example:
  temporal cloud account audit-log sink delete --name my-sink

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the audit log sink to delete. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### audit-log sink disable

Disable an audit log sink for the account.

Example:
  temporal cloud account audit-log sink disable --name my-sink

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the audit log sink to disable. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### audit-log sink enable

Enable an audit log sink for the account.

Example:
  temporal cloud account audit-log sink enable --name my-sink

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the audit log sink to enable. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### audit-log sink get

Returns the details of an audit log sink for the account.

Example:
  temporal cloud account audit-log sink get --name my-sink

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--name` | Yes | **string** The name of the audit log sink to get. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### audit-log sink kinesis

Commands for managing Kinesis-based audit log sinks.

##### audit-log sink kinesis create

Create an account audit log sink that streams audit events to Amazon Kinesis.

Temporal Cloud assumes the specified IAM role to write events to the Kinesis
stream identified by the destination URI.

Example:
  temporal cloud account audit-log sink kinesis create \
    --name my-sink \
    --role-name MyRole \
    --destination-uri arn:aws:kinesis:us-east-1:123456789012:stream/MyStream \
    --region us-east-1

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--destination-uri` | Yes | **string** ARN of the Kinesis stream to deliver audit log events to. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** Name of the audit log sink. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--region` | Yes | **string** AWS region where the Kinesis stream is located (e.g. us-east-1). |
| `--role-name` | Yes | **string** Name of the IAM role that Temporal Cloud assumes to write to the Kinesis stream. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

##### audit-log sink kinesis update

Update an existing Kinesis audit log sink. Only the flags you provide are changed;
omitted string flags retain their current values.

Example:
  temporal cloud account audit-log sink kinesis update \
    --name my-sink \
    --role-name NewRole

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--destination-uri` | No | **string** ARN of the Kinesis stream to deliver audit log events to. If omitted, the current value is kept. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** Name of the audit log sink to update. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--region` | No | **string** AWS region where the Kinesis stream is located (e.g. us-east-1). If omitted, the current value is kept. |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--role-name` | No | **string** Name of the IAM role that Temporal Cloud assumes to write to the Kinesis stream. If omitted, the current value is kept. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

##### audit-log sink kinesis validate

Validate an audit log sink configuration against Amazon Kinesis without creating it.
Use this to verify that the IAM role and Kinesis stream are correctly configured
before creating or updating the sink.

Example:
  temporal cloud account audit-log sink kinesis validate \
    --name my-sink \
    --role-name MyRole \
    --destination-uri arn:aws:kinesis:us-east-1:123456789012:stream/MyStream \
    --region us-east-1

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--destination-uri` | Yes | **string** ARN of the Kinesis stream to deliver audit log events to. |
| `--region` | Yes | **string** AWS region where the Kinesis stream is located (e.g. us-east-1). |
| `--role-name` | Yes | **string** Name of the IAM role that Temporal Cloud assumes to write to the Kinesis stream. |
