| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### audit-log sink list

Returns a paginated list of audit log sinks for the account.

Example:
  temporal cloud account audit-log sink list
  temporal cloud account audit-log sink list --page-size 50

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--page-size` | No | **int** Number of sinks to retrieve per page. Cannot exceed 1000. Defaults to 100. |
| `--page-token` | No | **string** Page token from a previous response to retrieve the next page. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### audit-log sink pubsub

Commands for managing PubSub audit log sinks.

##### audit-log sink pubsub create

Creates a new PubSub audit log sink for the account using Google Cloud Pub/Sub.

Example:

```
temporal cloud account audit-log sink pubsub create \
  --name my-sink \
  --service-account-email my-sa@my-project.iam.gserviceaccount.com \
  --topic-name my-topic
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the audit log sink. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-email` | Yes | **string** The email of the GCP service account that Temporal Cloud impersonates for writing records to the customer's PubSub topic (e.g. my-sa@my-project.iam.gserviceaccount.com). The service account ID and GCP project ID are parsed from this email. |
| `--topic-name` | Yes | **string** The destination PubSub topic name where audit logs will be sent. |

##### audit-log sink pubsub update

Updates an existing PubSub audit log sink for the account.

Example:

```
temporal cloud account audit-log sink pubsub update \
  --name my-sink \
  --service-account-email new-sa@new-project.iam.gserviceaccount.com \
  --topic-name new-topic
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the audit log sink to update. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-email` | No | **string** The email of the GCP service account that Temporal Cloud impersonates for writing records to the customer's PubSub topic (e.g. my-sa@my-project.iam.gserviceaccount.com). The service account ID and GCP project ID are parsed from this email. |
| `--topic-name` | No | **string** The destination PubSub topic name where audit logs will be sent. |

##### audit-log sink pubsub validate

Validates a PubSub audit log sink specification without creating or modifying any resources.

Example:

```
temporal cloud account audit-log sink pubsub validate \
  --name my-sink \
  --service-account-email my-sa@my-project.iam.gserviceaccount.com \
  --topic-name my-topic
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-email` | Yes | **string** The email of the GCP service account that Temporal Cloud impersonates for writing records to the customer's PubSub topic (e.g. my-sa@my-project.iam.gserviceaccount.com). The service account ID and GCP project ID are parsed from this email. |
| `--topic-name` | Yes | **string** The destination PubSub topic name where audit logs will be sent. |

## metrics

Commands for managing the Temporal Cloud account metrics configuration.

### metrics cert-ca

Commands for managing the CA certificates used to authenticate clients
accessing the Temporal Cloud account metrics endpoint.

#### metrics cert-ca create

Add a CA certificate to the list of accepted client CA certificates for
the Temporal Cloud account metrics endpoint.

Example:
  temporal cloud account metrics cert-ca create --ca-certificate-file /path/to/cert.pem
  temporal cloud account metrics cert-ca create --ca-certificate \<base64-encoded-cert\>

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--ca-certificate` | No | **string** Base64-encoded CA certificate for mTLS authentication. Mutually exclusive with --ca-certificate-file. |
| `--ca-certificate-file` | No | **string** Path to a CA certificate PEM file for mTLS authentication. Mutually exclusive with --ca-certificate. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### metrics cert-ca delete

Remove a CA certificate from the list of accepted client CA certificates for
the Temporal Cloud account metrics endpoint.

Example:
  temporal cloud account metrics cert-ca delete --ca-certificate-file /path/to/cert.pem
  temporal cloud account metrics cert-ca delete --ca-certificate \<base64-encoded-cert\>

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--ca-certificate` | No | **string** Base64-encoded CA certificate for mTLS authentication. Mutually exclusive with --ca-certificate-file. |
| `--ca-certificate-file` | No | **string** Path to a CA certificate PEM file for mTLS authentication. Mutually exclusive with --ca-certificate. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### metrics cert-ca list

List the CA certificates accepted for authenticating clients accessing
the Temporal Cloud account metrics endpoint.

Example:
  temporal cloud account metrics cert-ca list

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## Global Flags

The following options can be used with any command.

| Flag | Required | Description | Default |
|------|----------|-------------|--------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |  |
| `--auto-confirm` | No | **bool** Automatically confirm prompts and actions that require user confirmation. Useful for scripting and automation. |  |
| `--config-dir` | No | **string** Directory path where CLI configuration files are stored, including authentication tokens and settings. |  |
| `--disable-pop-up` | No | **bool** Prevent the CLI from opening a browser window during authentication. Useful for headless environments or when using alternative auth methods. |  |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. | `saas-api.tmprl.cloud:443` |

---

## Temporal CLI cloud apikey command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud apikey` commands. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## create-for-me

Create a new API key owned by the currently authenticated user.
The token is printed once on creation and cannot be retrieved again.

Example:

```
temporal cloud apikey create-for-me --display-name "My Key"
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--description` | No | **string** An optional description for the API key. |
| `--display-name` | Yes | **string** A human-readable display name for the API key. |
| `--expiry-duration` | No | **duration** Expiry duration relative to now (e.g. 30d, 24h, 90m). Supports days (d), hours (h), minutes (m), and seconds (s). Mutually exclusive with --expiry-time. |
| `--expiry-time` | No | **timestamp** Expiry time for the API key in RFC3339 format (e.g. 2025-12-31T00:00:00Z). Mutually exclusive with --expiry-duration. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## create-for-service-account

Create a new API key owned by the specified service account.
The token is printed once on creation and cannot be retrieved again.

Example:

```
temporal cloud apikey create-for-service-account --service-account-id my-sa-id --display-name "My Key"
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--description` | No | **string** An optional description for the API key. |
| `--display-name` | Yes | **string** A human-readable display name for the API key. |
| `--expiry-duration` | No | **duration** Expiry duration relative to now (e.g. 30d, 24h, 90m). Supports days (d), hours (h), minutes (m), and seconds (s). Mutually exclusive with --expiry-time. |
| `--expiry-time` | No | **timestamp** Expiry time for the API key in RFC3339 format (e.g. 2025-12-31T00:00:00Z). Mutually exclusive with --expiry-duration. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-id` | Yes | **string** The ID of the service account to create the API key for. |

## delete

Delete a Temporal Cloud API key. This action is irreversible.

Example:

```
temporal cloud apikey delete --key-id my-key-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--key-id` | Yes | **string** The ID of the API key to delete. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## disable

Disable a Temporal Cloud API key. Disabled keys cannot be used for authentication.

Example:

```
temporal cloud apikey disable --key-id my-key-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--key-id` | Yes | **string** The ID of the API key to disable. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## edit

Open an API key configuration in your default editor for interactive
modification. After saving and closing the editor, the changes are
applied to Temporal Cloud.

The editor is determined by the EDITOR environment variable, falling
back to 'vi' if not set.

Example:

```
temporal cloud apikey edit --key-id my-key-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--key-id` | Yes | **string** The ID of the API key to edit. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--verbose-diff` | No | **bool** Show detailed differences between the current and desired namespace configurations when changes are detected. |

## enable

Enable a previously disabled Temporal Cloud API key.

Example:

```
temporal cloud apikey enable --key-id my-key-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--key-id` | Yes | **string** The ID of the API key to enable. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## get

Retrieve the configuration and status of a Temporal Cloud API key.

Example:

```
temporal cloud apikey get --key-id my-key-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--key-id` | Yes | **string** The ID of the API key to retrieve. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## list

List API keys. Optionally filter by user ID, user email, or service account ID.
At most one filter may be specified.

Example:

```
temporal cloud apikey list
temporal cloud apikey list --user-id my-user-id
temporal cloud apikey list --service-account-id my-sa-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--page-size` | No | **int** Number of API keys to return per page. |
| `--page-token` | No | **string** Token for retrieving the next page of results. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-id` | No | **string** Filter API keys by service account ID. Mutually exclusive with --user-id and --user-email. |
| `--user-email` | No | **string** Filter API keys by user email. Mutually exclusive with --user-id and --service-account-id. |
| `--user-id` | No | **string** Filter API keys by user ID. Mutually exclusive with --user-email and --service-account-id. |
