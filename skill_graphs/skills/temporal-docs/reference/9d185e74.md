
## update

Update an API key's display name, description, or disabled status.
Only flags that are explicitly provided are changed.

Example:

```
temporal cloud apikey update --key-id my-key-id --display-name "New Name"
temporal cloud apikey update --key-id my-key-id --disabled=true
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--description` | No | **string** New description for the API key. |
| `--disabled` | No | **bool** Set to true to disable the API key, or false to enable it. |
| `--display-name` | No | **string** New display name for the API key. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--key-id` | Yes | **string** The ID of the API key to update. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
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

## Temporal CLI cloud async-operation command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud async-operation` commands. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## await

Wait for a Temporal Cloud async operation to reach a terminal state.
Polls the operation status until it completes, fails, or is cancelled.

Example:

```
temporal cloud async-operation await --async-operation-id my-op-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async-operation-id` | Yes | **string** The ID of the async operation to wait for. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). Default is 1s. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## get

Retrieve the status and details of a Temporal Cloud async operation.

Example:

```
temporal cloud async-operation get --async-operation-id my-op-id
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async-operation-id` | Yes | **string** The ID of the async operation to retrieve. |
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

## Temporal CLI cloud connectivity command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud connectivity` commands. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## delete

Delete a connectivity rule by its ID.

Example:

```
temporal cloud connectivity delete --id <connectivity-rule-id>
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--id` | Yes | **string** The ID of the connectivity rule. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## get

Get details of a specific connectivity rule by its ID.

Example:

```
temporal cloud connectivity get --id <connectivity-rule-id>
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--id` | Yes | **string** The ID of the connectivity rule. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## list

List connectivity rules, optionally filtered by namespace.

Example:

```
temporal cloud connectivity list --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | No | **string** Filter connectivity rules by namespace (e.g., 'my-namespace.my-account'). |
| `--page-size` | No | **int** Number of connectivity rules to return per page. |
| `--page-token` | No | **string** Page token for pagination. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## private

Commands for managing private connectivity rules.

### private create

Create a new private VPC connectivity rule. Requires --connection-id and --region.

Example:

```
temporal cloud connectivity private create --connection-id vpce-12345 --region aws-us-west-2
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--connection-id` | Yes | **string** The connection ID for private connectivity. |
| `--gcp-project-id` | No | **string** The GCP project ID (only for GCP private connectivity). |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--region` | Yes | **string** The region for private connectivity. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## public

Commands for managing public connectivity rules.

### public create

Create a new public internet connectivity rule.

Example:

```
temporal cloud connectivity public create
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--enable-stable-ips` | No | **bool** Connect the namespace via a predictable set of IPs on the public internet. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
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

## Temporal CLI cloud command reference

<ReleaseNoteHeader featureName="cloudCli" />

This section includes the command reference for the `temporal cloud` CLI extension.

- [account](/cli/command-reference/cloud/account)
- [apikey](/cli/command-reference/cloud/apikey)
- [async-operation](/cli/command-reference/cloud/async-operation)
- [connectivity](/cli/command-reference/cloud/connectivity)
- [login](/cli/command-reference/cloud/login)
- [logout](/cli/command-reference/cloud/logout)
- [namespace](/cli/command-reference/cloud/namespace)
- [nexus](/cli/command-reference/cloud/nexus)
- [region](/cli/command-reference/cloud/region)
- [service-account](/cli/command-reference/cloud/service-account)
- [user](/cli/command-reference/cloud/user)
- [user-group](/cli/command-reference/cloud/user-group)
- [whoami](/cli/command-reference/cloud/whoami)

---

## Temporal CLI cloud login command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud login` command.

Authenticate with Temporal Cloud using browser-based OAuth login.

This command opens your default browser to complete authentication. Once
logged in, your credentials are stored locally for subsequent commands.

Example:

```
temporal cloud login
```

For headless environments, use --disable-pop-up and follow the printed URL.

| Flag | Required | Description |
|------|----------|-------------|
| `--audience` | No | **string** OAuth audience parameter for token generation. |
| `--client-id` | No | **string** OAuth client identifier for authentication. |
| `--domain` | No | **string** Authentication domain for the OAuth provider. |
| `--redirect-url` | No | **string** Redirect URL for OAuth authentication flow. |
| `--reset` | No | **bool** Clear stored login credentials and configuration, then re-authenticate. Use this if you need to switch accounts or fix authentication issues. |

---

## Temporal CLI cloud logout command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud logout` command.

Log out from Temporal Cloud by clearing stored authentication tokens
and credentials from the local configuration.

Example:

```
temporal cloud logout
```

| Flag | Required | Description |
|------|----------|-------------|
| `--domain` | No | **string** Authentication domain for the OAuth provider. |

---

## Temporal CLI cloud namespace command reference

{/* NOTE: This is an auto-generated file. Any edit to this file will be overwritten.
This file is generated from https://github.com/temporalio/cli via cmd/gen-docs */}

<ReleaseNoteHeader featureName="cloudCli" />

This page provides a reference for the `temporal cloud namespace` commands. The flags applicable to each subcommand are presented in a table within the heading for the subcommand. Refer to [Global Flags](#global-flags) for flags that you can use with every subcommand.

## apply

Apply a namespace configuration to Temporal Cloud. Creates a new namespace
if it doesn't exist, or updates an existing one to match the specification.

The specification can be provided as inline JSON or loaded from a file
by prefixing the path with '@'.

Example with inline JSON:

```
temporal cloud namespace apply --spec '{"name": "namespace-name", "region": "us-west-2", "retention_days": 7}'
```

Example with file path:

```
temporal cloud namespace apply --spec @namespace-spec.json
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the namespace already matches the specification. Without this flag, the command errors when no changes are needed. |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--spec` | Yes | **string** Namespace configuration in JSON format. Provide inline JSON directly, or use '@path/to/file.json' to load from a file. |
| `--verbose-diff` | No | **bool** Show detailed differences between the current and desired namespace configurations when changes are detected. |

## capacity

Commands for managing the capacity of Temporal Cloud namespaces.

Capacity controls whether a namespace runs in on-demand mode or
provisioned mode (with a fixed TRU allocation).

### capacity get

Retrieve capacity information for a Temporal Cloud namespace, including
the current mode (on-demand or provisioned), mode options, and recent usage stats.

Example:

```
temporal cloud namespace capacity get --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### capacity update

Update the capacity of a Temporal Cloud namespace. Choose either on-demand
mode or provisioned mode (with a fixed TRU allocation).

Example (switch to on-demand):

```
temporal cloud namespace capacity update --namespace my-namespace.my-account --capacity-mode on_demand
```

Example (switch to provisioned with 4 TRUs):

```
temporal cloud namespace capacity update --namespace my-namespace.my-account --capacity-mode provisioned --capacity-value 4
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--capacity-mode` | Yes | **string-enum** Capacity mode for the namespace. Must be either 'on_demand' or 'provisioned'. Accepted values: on_demand, provisioned. |
| `--capacity-value` | No | **float** The provisioned capacity in Temporal Resource Units (TRUs). Required and must be greater than 0 when --capacity-mode is 'provisioned'. Ignored when --capacity-mode is 'on_demand'. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## cert-ca

Commands for managing the client CA certificates of Temporal Cloud namespaces.

### cert-ca create

Add client CA certificates to a Temporal Cloud namespace from a PEM file
or base64 encoded string. These certificates are used to verify client
connections and enable mTLS authentication.

Specify either --ca-certificate-file or --ca-certificate, but not both.

Example with file:

```
temporal cloud namespace cert-ca create --namespace my-namespace.my-account --ca-certificate-file ca-cert.pem
```

Example with base64 encoded data:

```
temporal cloud namespace cert-ca create --namespace my-namespace.my-account --ca-certificate <base64-encoded-cert>
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--ca-certificate` | No | **string** Base64-encoded CA certificate for mTLS authentication. Mutually exclusive with --ca-certificate-file. |
| `--ca-certificate-file` | No | **string** Path to a CA certificate PEM file for mTLS authentication. Mutually exclusive with --ca-certificate. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### cert-ca delete

Delete client CA certificates from a Temporal Cloud namespace. This operation
requires confirmation and will remove the specified certificates from the
