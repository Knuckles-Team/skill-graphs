```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--page-size` | No | **int** Number of service accounts to return per page. Use for paginated results. |
| `--page-token` | No | **string** Token for retrieving the next page of results in a paginated list. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## set-custom-roles

Set the custom roles assigned to a Temporal Cloud service account.
Replaces the service account's current custom role list. Pass no
--custom-role flags to remove all custom roles.

Not valid for namespace-scoped service accounts.

Example:

```
temporal cloud service-account set-custom-roles --service-account-id my-sa-id \
  --custom-role role-id-1 --custom-role role-id-2
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--custom-role` | No | **string[]** Custom role ID to assign. Repeat to assign multiple. When provided, replaces the existing custom role list. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-id` | Yes | **string** The ID of the service account. |

## update

Update a Temporal Cloud service account. Only flags that are explicitly provided
are changed.

For account-scoped service accounts, use --account-role and/or --namespace-access.
For namespace-scoped service accounts, use --namespace-permission.

Namespace access format: 'namespace=permission' where permission is one of: admin, write, read.
Use 'namespace=' (empty permission) to remove access to a namespace.

Example:

```
temporal cloud service-account update --service-account-id my-sa-id --name new-name
temporal cloud service-account update --service-account-id my-sa-id --account-role admin
temporal cloud service-account update --service-account-id my-sa-id --namespace-permission write
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--account-role` | No | **string** The account-level role to assign. Valid values: owner, admin, developer, finance-admin, read, metrics-read. Only valid for account-scoped service accounts. |
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--custom-role` | No | **string[]** Custom role ID to assign. Repeat to assign multiple. When provided, replaces the existing custom role list. |
| `--description` | No | **string** New description for the service account. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name` | No | **string** New name for the service account. |
| `--namespace-access` | No | **string[]** Namespace access to set, in the format 'namespace=permission'. Use 'namespace=' to remove access. Permission must be one of: admin, write, read. Can be repeated. Only valid for account-scoped service accounts. |
| `--namespace-permission` | No | **string** The permission to grant on the scoped namespace. Valid values: admin, write, read. Only valid for namespace-scoped service accounts. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-id` | Yes | **string** The ID of the service account to update. |

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

## Temporal CLI cloud user-group command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud user-group` commands. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## apply

Apply a user group configuration to Temporal Cloud. Creates a new user group
if no group with the given display name exists, or updates the existing one
to match the specification.

The specification can be provided as inline JSON or loaded from a file
by prefixing the path with '@'.

Example with inline JSON:

```
temporal cloud user-group apply --spec '{"display_name": "Engineering", "cloud_group": {}, "access": {"account_access": {"role": "developer"}}}'
```

Example with file path:

```
temporal cloud user-group apply --spec @user-group-spec.json
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
| `--spec` | Yes | **string** User group configuration in JSON format. Provide inline JSON directly, or use '@path/to/file.json' to load from a file. |
| `--verbose-diff` | No | **bool** Show detailed differences between the current and desired namespace configurations when changes are detected. |

## create-cloud-group

Create a new Temporal Cloud-managed user group. Members can be managed
using the add-member and remove-member commands.

Account roles: owner, admin, developer, finance-admin, read, metrics-read.
Namespace access format: 'namespace=permission' where permission is one of: admin, write, read.

Example:

```
temporal cloud user-group create-cloud-group --display-name "Engineering" \
  --account-role developer \
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
| `--display-name` | Yes | **string** The display name of the user group. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace-access` | No | **string[]** Namespace access to grant, in the format 'namespace=permission'. Permission must be one of: admin, write, read. Can be repeated. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## create-google-group

Create a new user group backed by a Google Group. Members are managed
via the Google Group itself.

Account roles: owner, admin, developer, finance-admin, read, metrics-read.
Namespace access format: 'namespace=permission' where permission is one of: admin, write, read.

Example:

```
temporal cloud user-group create-google-group --display-name "Platform" \
  --google-group-email platform@example.com \
  --account-role developer
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--account-role` | No | **string** The account-level role to assign. Valid values: owner, admin, developer, finance-admin, read, metrics-read. |
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--custom-role` | No | **string[]** Custom role ID to assign. Repeat to assign multiple. |
| `--display-name` | Yes | **string** The display name of the user group. |
| `--google-group-email` | Yes | **string** The email address of the Google Group. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace-access` | No | **string[]** Namespace access to grant, in the format 'namespace=permission'. Permission must be one of: admin, write, read. Can be repeated. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## create-scim-group

Create a new user group backed by a SCIM identity provider group.
Members are managed via the upstream identity provider.

Account roles: owner, admin, developer, finance-admin, read, metrics-read.
Namespace access format: 'namespace=permission' where permission is one of: admin, write, read.

Example:

```
temporal cloud user-group create-scim-group --display-name "Security" \
  --scim-idp-id idp-group-id-123 \
  --account-role read
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--account-role` | No | **string** The account-level role to assign. Valid values: owner, admin, developer, finance-admin, read, metrics-read. |
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--custom-role` | No | **string[]** Custom role ID to assign. Repeat to assign multiple. |
| `--display-name` | Yes | **string** The display name of the user group. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace-access` | No | **string[]** Namespace access to grant, in the format 'namespace=permission'. Permission must be one of: admin, write, read. Can be repeated. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--scim-idp-id` | Yes | **string** The identity provider ID for the SCIM group. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## delete

Delete a Temporal Cloud user group. This action is irreversible.

Example:

```
temporal cloud user-group delete --group-id my-group-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--group-id` | Yes | **string** The ID of the user group. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## edit

Open a user group configuration in your default editor for interactive
modification. After saving and closing the editor, the changes are
applied to Temporal Cloud.

The editor is determined by the EDITOR environment variable, falling
back to 'vi' if not set.

Example:

```
temporal cloud user-group edit --group-id my-group-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--group-id` | Yes | **string** The ID of the user group. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--verbose-diff` | No | **bool** Show detailed differences between the current and desired namespace configurations when changes are detected. |

## get

Retrieve the configuration and status of a Temporal Cloud user group.

Example:

```
temporal cloud user-group get --group-id my-group-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--group-id` | Yes | **string** The ID of the user group. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## list

List all Temporal Cloud user groups accessible with the current
authentication credentials.

Example:

```
temporal cloud user-group list
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--display-name` | No | **string** Filter user groups by display name. |
| `--google-group-email-address` | No | **string** Filter user groups by Google group email address. |
| `--namespace` | No | **string** Filter user groups by the namespace they have access to. |
| `--page-size` | No | **int** Number of user groups to return per page. Use for paginated results. |
| `--page-token` | No | **string** Token for retrieving the next page of results in a paginated list. |
| `--scim-group-idp-id` | No | **string** Filter user groups by SCIM group IDP ID. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## members

Commands for managing members of Temporal Cloud user groups.

### members add

Add a user to a Temporal Cloud user group.

Specify the user with either --user-id or --user-email (not both).

Example:

```
temporal cloud user-group members add --group-id my-group-id --user-id my-user-id
temporal cloud user-group members add --group-id my-group-id --user-email alice@example.com
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--group-id` | Yes | **string** The ID of the user group. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--user-email` | No | **string** The email address of the user. Mutually exclusive with --user-id. |
| `--user-id` | No | **string** The ID of the user. Mutually exclusive with --user-email. |

### members list

List all members of a Temporal Cloud user group.

Example:

```
temporal cloud user-group members list --group-id my-group-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--group-id` | Yes | **string** The ID of the user group. |
| `--page-size` | No | **int** Number of members to return per page. Use for paginated results. |
| `--page-token` | No | **string** Token for retrieving the next page of results in a paginated list. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### members remove

Remove a user from a Temporal Cloud user group.

Specify the user with either --user-id or --user-email (not both).

Example:

```
temporal cloud user-group members remove --group-id my-group-id --user-id my-user-id
temporal cloud user-group members remove --group-id my-group-id --user-email alice@example.com
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--group-id` | Yes | **string** The ID of the user group. |
