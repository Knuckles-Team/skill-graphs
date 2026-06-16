namespace configuration.

Specify either --ca-certificate-file or --ca-certificate, but not both.

Example with file:

```
temporal cloud namespace cert-ca delete --namespace my-namespace.my-account --ca-certificate-file ca-cert.pem
```

Example with base64 encoded data:

```
temporal cloud namespace cert-ca delete --namespace my-namespace.my-account --ca-certificate <base64-encoded-cert>
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

### cert-ca list

Retrieve the list of client CA certificates configured for a Temporal Cloud
namespace. These certificates are used for client authentication.

Example:

```
temporal cloud namespace cert-ca list --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## cert-filter

Commands for managing certificate filters for Temporal Cloud namespaces.
Certificate filters restrict mTLS connections to client certificates with
specific distinguished name properties.

### cert-filter create

Add new certificate filters to a Temporal Cloud namespace. Certificate
filters restrict mTLS connections to client certificates whose distinguished
name properties match at least one of the filters.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--common-name` | No | **string** The common name (CN) field from the certificate's distinguished name. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--organization` | No | **string** The organization (O) field from the certificate's distinguished name. |
| `--organizational-unit` | No | **string** The organizational unit (OU) field from the certificate's distinguished name. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--subject-alternative-name` | No | **string** The subject alternative name (SAN) from the certificate. |

### cert-filter delete

Delete certificate filters from a Temporal Cloud namespace. Filters are
matched by exact field equality.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--common-name` | No | **string** The common name (CN) field from the certificate's distinguished name. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--organization` | No | **string** The organization (O) field from the certificate's distinguished name. |
| `--organizational-unit` | No | **string** The organizational unit (OU) field from the certificate's distinguished name. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--subject-alternative-name` | No | **string** The subject alternative name (SAN) from the certificate. |

### cert-filter list

List all certificate filters configured for a Temporal Cloud namespace.

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## codec

Commands for managing the codec server configuration of Temporal Cloud namespaces.

The codec server is used to encode and decode payloads for workflows and activities.

### codec delete

Delete the codec server configuration from a Temporal Cloud namespace.

Example:

```
temporal cloud namespace codec delete --namespace my-namespace.my-account
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
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### codec get

Retrieve the current codec server configuration for a Temporal Cloud namespace.

Example:

```
temporal cloud namespace codec get --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### codec set

Set the codec server configuration for a Temporal Cloud namespace.

Example:

```
temporal cloud namespace codec set --namespace my-namespace.my-account --endpoint https://my-codec.example.com
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--custom-error-message-default-link` | No | **string** A link to display alongside the custom error message for remote codec server errors. |
| `--custom-error-message-default-message` | No | **string** A custom message to display for remote codec server errors. |
| `--endpoint` | Yes | **string** The codec server endpoint URL. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--include-cross-origin-credentials` | No | **bool** Whether to include cross-origin credentials in requests to the codec server. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--pass-access-token` | No | **bool** Whether to pass the user access token to the codec server endpoint. |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## connectivity

Commands for attaching and detaching connectivity rules on a Temporal Cloud
namespace. Use 'cloud connectivity' to manage the rules themselves.

### connectivity attach

Attach an existing connectivity rule to a Temporal Cloud namespace.

Example:

```
temporal cloud namespace connectivity attach \
  --namespace my-namespace.my-account \
  --connectivity-rule-id <rule-id>
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--connectivity-rule-id` | Yes | **string[]** The ID of a connectivity rule to attach. Repeat to attach multiple. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### connectivity detach

Detach a connectivity rule from a Temporal Cloud namespace.

Example:

```
temporal cloud namespace connectivity detach \
  --namespace my-namespace.my-account \
  --connectivity-rule-id <rule-id>
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--connectivity-rule-id` | Yes | **string[]** The ID of a connectivity rule to detach. Repeat to detach multiple. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### connectivity list

List all connectivity rules currently attached to a Temporal Cloud namespace.

Example:

```
temporal cloud namespace connectivity list --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## create

Create a new Temporal Cloud namespace with the specified configuration.

Options are passed as individual flags. To create or update a namespace
using a full JSON specification, use 'namespace apply' instead.

Example:

```
temporal cloud namespace create --name my-namespace --region aws-us-east-1 --retention-days 30
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--api-key-auth-enabled` | No | **bool** Enable API key authentication for the namespace. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--ca-certificate` | No | **string** Base64-encoded CA certificate for mTLS authentication. Mutually exclusive with --ca-certificate-file. |
| `--ca-certificate-file` | No | **string** Path to a CA certificate PEM file for mTLS authentication. Mutually exclusive with --ca-certificate. |
| `--certificate-filter` | No | **string[]** Certificate filter as a JSON object (e.g. `'{"commonName":"foo"}'`). Repeat to add multiple. |
| `--certificate-filter-file` | No | **string** Path to a JSON file containing a certificate filter object. |
| `--codec-endpoint` | No | **string** HTTPS codec server endpoint URL. |
| `--codec-include-cross-origin-credentials` | No | **bool** Include cross-origin credentials in codec server requests. |
| `--codec-pass-access-token` | No | **bool** Pass the user access token to the codec server endpoint. |
| `--connection-rule-id` | No | **string[]** Private connectivity rule ID. Repeat to specify multiple. |
| `--enable-delete-protection` | No | **bool** Prevent accidental deletion of this namespace. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--name`, `-n` | Yes | **string** The name for the new namespace (becomes part of the namespace ID). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--region` | Yes | **string[]** Cloud region where the namespace will be hosted. Repeat to specify multiple regions for High Availability (e.g. --region aws-us-east-1 --region aws-us-west-2). |
| `--retention-days` | No | **int** Number of days to retain closed workflow history. If not specified, the server default applies. |
| `--search-attribute` | No | **string[]** Custom search attribute as 'name=Type' (e.g. --search-attribute myAttr=Keyword). Valid types: Text, Keyword, Int, Double, Bool, Datetime, KeywordList. Repeat to add multiple. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## delete

Delete a Temporal Cloud namespace and all associated data. This action is
irreversible and will permanently remove all workflows, activities, and
history within the namespace.

Example:

```
temporal cloud namespace delete --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the namespace does not exist. Without this flag, the command errors if the namespace is not found. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

## edit

Open a namespace configuration in your default editor for interactive
modification. After saving and closing the editor, the changes are
applied to Temporal Cloud.

The editor is determined by the EDITOR environment variable, falling
back to 'vi' if not set.

Example:

```
temporal cloud namespace edit --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if no changes were made in the editor. Without this flag, the command errors when the configuration is unchanged. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--verbose-diff` | No | **bool** Show detailed differences between the current and desired namespace configurations when changes are detected. |

## export

Commands for managing workflow history export sinks for Temporal Cloud namespaces.

Export sinks define destinations (S3 or GCS) to which workflow history is exported.

### export delete

Delete a workflow history export sink from a Temporal Cloud namespace.

Example:

```
temporal cloud namespace export delete --namespace my-namespace.my-account --sink-name my-sink
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
