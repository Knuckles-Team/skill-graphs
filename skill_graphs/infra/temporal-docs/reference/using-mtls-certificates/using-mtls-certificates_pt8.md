| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### endpoint allowed-namespace list

List all namespaces that are allowed to call this Nexus Endpoint.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--name` | Yes | **string** The name of the Nexus Endpoint. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### endpoint allowed-namespace remove

Remove namespaces from the list of allowed callers of this Nexus Endpoint.
Namespaces that are not currently allowed are silently ignored.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the Nexus Endpoint. |
| `--namespace` | Yes | **string[]** A namespace to remove. Can be specified multiple times. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### endpoint allowed-namespace set

Set the full list of namespaces that are allowed to call this Nexus Endpoint,
replacing any previously allowed namespaces.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the Nexus Endpoint. |
| `--namespace` | Yes | **string[]** A namespace to allow. Can be specified multiple times. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### endpoint create

Create a new Nexus Endpoint on the Cloud Account.
An endpoint name is used in workflow code to invoke Nexus operations.
The endpoint target is a worker and `--target-namespace` and `--target-task-queue`
must both be provided. This will fail if an endpoint with the same name is already registered.

Example:

```
temporal cloud nexus endpoint create --name my-endpoint --target-namespace my-ns.my-account --target-task-queue my-tq
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--allow-namespace` | No | **string[]** A namespace that is allowed to call this endpoint. Can be specified multiple times. |
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--description` | No | **string** An optional endpoint description in markdown format. |
| `--description-file` | No | **string** Path to a file containing an endpoint description in markdown format. Mutually exclusive with --description. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the Nexus Endpoint to create. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--target-namespace` | Yes | **string** The namespace in which a handler worker will be polling for Nexus tasks. |
| `--target-task-queue` | Yes | **string** The task queue on which a handler worker will be polling for Nexus tasks. |

### endpoint delete

Delete a Nexus Endpoint on the Cloud Account.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the Nexus Endpoint to delete. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### endpoint get

Get a Nexus Endpoint configuration from the Cloud Account.
Specify either `--name` or `--id` (exactly one is required).

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--id` | No | **string** The ID of the Nexus Endpoint to retrieve. |
| `--name` | No | **string** The name of the Nexus Endpoint to retrieve. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### endpoint list

List Nexus Endpoint configurations on the Cloud Account.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--page-size` | No | **int** Number of endpoints to return per page. If no page size is provided, it will default to 100. A maximum of 1000 endpoints can be fetched at a time. |
| `--page-token` | No | **string** Token for retrieving the next page of results. Initial value is empty string. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### endpoint update

Update an existing Nexus Endpoint on the Cloud Account.
An endpoint name is used in workflow code to invoke Nexus operations.

The endpoint is patched leaving any existing fields for which flags are not provided
as they were.

Example:

```
temporal cloud nexus endpoint update --name my-endpoint --target-namespace new-ns.my-account --target-task-queue new-tq
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--description` | No | **string** An optional endpoint description in markdown format. |
| `--description-file` | No | **string** Path to a file containing an endpoint description in markdown format. Mutually exclusive with --description. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the Nexus Endpoint to update. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--target-namespace` | No | **string** The namespace in which a handler worker will be polling for Nexus tasks. |
| `--target-task-queue` | No | **string** The task queue on which a handler worker will be polling for Nexus tasks. |
| `--unset-description` | No | **bool** Unset the endpoint description. Cannot be used with --description or --description-file. |

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

## Temporal CLI cloud region command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud region` commands. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## get

Get details for a specific Temporal Cloud region.

Example:

```
temporal cloud region get --region aws-us-east-1
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--region`, `-r` | Yes | **string** The ID of the region to get. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## list

List all available Temporal Cloud regions.

Example:

```
temporal cloud region list
```

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

## Temporal CLI cloud service-account command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud service-account` commands. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## create

Create a new Temporal Cloud service account with account-level access.
Optionally assign an account role and namespace-level permissions.

Account roles: owner, admin, developer, finance-admin, read, metrics-read.
Namespace access format: 'namespace=permission' where permission is one of: admin, write, read.

Example:

```
temporal cloud service-account create --name my-sa --account-role developer \
  --namespace-access my-namespace.my-account=write
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--account-role` | No | **string** The account-level role to assign. Valid values: owner, admin, developer, finance-admin, read, metrics-read. |
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--custom-role` | No | **string[]** Custom role ID to assign. Repeat to assign multiple. |
| `--description` | No | **string** An optional description for the service account. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the service account. Must be unique across all active service accounts. |
| `--namespace-access` | No | **string[]** Namespace access to grant, in the format 'namespace=permission'. Permission must be one of: admin, write, read. Can be repeated. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## create-namespace-scoped

Create a new Temporal Cloud service account scoped to a single namespace.

Example:

```
temporal cloud service-account create-namespace-scoped --name my-sa \
  --namespace my-namespace.my-account --namespace-permission write
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--description` | No | **string** An optional description for the service account. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the service account. Must be unique across all active service accounts. |
| `--namespace` | Yes | **string** The namespace to scope the service account to. |
| `--namespace-permission` | Yes | **string** The permission to grant on the namespace. Valid values: admin, write, read. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## delete

Delete a Temporal Cloud service account. This action is irreversible.

Example:

```
temporal cloud service-account delete --service-account-id my-sa-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-id` | Yes | **string** The ID of the service account to delete. |

## edit

Open a service account configuration in your default editor for interactive
modification. After saving and closing the editor, the changes are applied
to Temporal Cloud.

The editor is determined by the EDITOR environment variable, falling
back to 'vi' if not set.

Example:

```
temporal cloud service-account edit --service-account-id my-sa-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-id` | Yes | **string** The ID of the service account to edit. |
| `--verbose-diff` | No | **bool** Show detailed differences between the current and desired namespace configurations when changes are detected. |

## get

Retrieve the configuration and status of a Temporal Cloud service account.

Example:

```
temporal cloud service-account get --service-account-id my-sa-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-id` | Yes | **string** The ID of the service account to retrieve. |

## list

List all Temporal Cloud service accounts accessible with the current
authentication credentials.

Example:

```
temporal cloud service-account list
