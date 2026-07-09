```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--region` | Yes | **string** The region ID to remove (e.g., aws-us-west-2). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### ha region list

List all regions and their states for a Temporal Cloud namespace.

Example:

```
temporal cloud namespace ha region list --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### ha update

Update the High Availability configuration for a Temporal Cloud namespace.
Use --disable-auto-failover to toggle Temporal-managed automatic failover.
Use --disable-passive-poller-forwarding to toggle passive poller forwarding.

Example:

```
temporal cloud namespace ha update --namespace my-namespace.my-account --disable-auto-failover true --disable-passive-poller-forwarding false
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--disable-auto-failover` | No | **bool** Set to true to disable Temporal-managed automatic failover for the namespace. Set to false to re-enable automatic failover. |
| `--disable-passive-poller-forwarding` | No | **bool** Set to true to disable passive poller forwarding for the namespace. Set to false to re-enable passive poller forwarding. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## lifecycle

Commands for managing lifecycle settings of Temporal Cloud namespaces.

Lifecycle settings control the behavior and protection of namespaces,
including delete protection to prevent accidental deletion.

### lifecycle get

Retrieve the current lifecycle configuration for a Temporal Cloud namespace.
Lifecycle settings include delete protection status.

Example:

```
temporal cloud namespace lifecycle get --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### lifecycle set

Set the lifecycle configuration for a Temporal Cloud namespace.
Lifecycle settings include delete protection to prevent accidental deletion.

Example:

```
temporal cloud namespace lifecycle set --namespace my-namespace.my-account --enable-delete-protection true
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--enable-delete-protection` | Yes | **bool** Enable or disable delete protection for the namespace. When enabled, the namespace cannot be deleted until this flag is set to false. |
| `--idempotent` | No | **bool** Succeed silently if the lifecycle configuration is already set to the specified value. Without this flag, the command errors when no change is needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--resource-version` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--verbose-diff` | No | **bool** Show detailed differences between the current and desired namespace configurations when changes are detected. |

## list

List all Temporal Cloud namespaces accessible with the current
authentication credentials.

Example:

```
temporal cloud namespace list
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--name` | No | **string** Filter namespaces by the name as defined in the specification of the namespace. |
| `--page-size` | No | **int** Number of namespaces to return per page. Use for paginated results. |
| `--page-token` | No | **string** Token for retrieving the next page of results in a paginated list. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## retention

Commands for managing data retention settings of Temporal Cloud namespaces.

Retention determines how long closed workflow history data are stored before
being automatically deleted.

### retention get

Retrieve the current data retention period for a Temporal Cloud namespace.
The retention period defines how long closed workflow history data are stored.

Example:

```
temporal cloud namespace retention get --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### retention set

Set the data retention period for a Temporal Cloud namespace. The
retention period defines how long closed workflow history data are stored.

Example:

```
temporal cloud namespace retention set --namespace my-namespace.my-account --retention-days 14
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--retention-days` | Yes | **int** New retention period in days for closed workflow history data. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## search-attribute

Commands for managing custom search attributes for Temporal Cloud namespaces.
Search attributes enable filtering and searching workflows by custom fields.

### search-attribute create

Create a new custom search attribute for a Temporal Cloud namespace.

Example:

```
temporal cloud namespace search-attribute create --namespace my-namespace.my-account --name MyField --type Keyword
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the search attribute to create. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--type` | Yes | **string** The type of the search attribute. Valid values: Text, Keyword, Int, Double, Bool, Datetime, KeywordList. |

### search-attribute list

List all custom search attributes configured for a Temporal Cloud namespace.

Example:

```
temporal cloud namespace search-attribute list --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### search-attribute rename

Rename an existing custom search attribute for a Temporal Cloud namespace.
This operation preserves all existing data associated with the search attribute.

Example:

```
temporal cloud namespace search-attribute rename --namespace my-namespace.my-account --existing-name OldField --new-name NewField
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--existing-name` | Yes | **string** The current name of the search attribute to rename. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--new-name` | Yes | **string** The new name for the search attribute. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## tag

Commands for managing tags of Temporal Cloud namespaces.

Tags are key-value pairs used for organization and categorization of namespaces.

### tag create

Create a new tag for a Temporal Cloud namespace. Fails if a tag with
the specified key already exists.

Example:

```
temporal cloud namespace tag create --namespace my-namespace.my-account --key environment --value production
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--key` | Yes | **string** The tag key. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--value` | Yes | **string** The tag value. |

### tag delete

Delete a tag from a Temporal Cloud namespace by its key.

Example:

```
temporal cloud namespace tag delete --namespace my-namespace.my-account --key environment
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--key` | Yes | **string** The tag key to delete. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### tag list

List all tags configured for a Temporal Cloud namespace.

Example:

```
temporal cloud namespace tag list --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### tag update

Update the value of an existing tag for a Temporal Cloud namespace.
Fails if the specified tag key does not exist.

Example:

```
temporal cloud namespace tag update --namespace my-namespace.my-account --key environment --value staging
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--key` | Yes | **string** The tag key to update. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--value` | Yes | **string** The new value for the tag. |

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

## Temporal CLI cloud nexus command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud nexus` commands. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## endpoint

Commands for managing Nexus Endpoints in Temporal Cloud.

### endpoint allowed-namespace

Commands for managing allowed namespaces for Nexus Endpoints.

#### endpoint allowed-namespace add

Add namespaces that are allowed to call this Nexus Endpoint.
Namespaces that are already allowed are silently ignored.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | Yes | **string** The name of the Nexus Endpoint. |
| `--namespace` | Yes | **string[]** A namespace to allow. Can be specified multiple times. |
