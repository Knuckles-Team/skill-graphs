| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--sink-name` | Yes | **string** The name of the export sink. |

### export disable

Disable a workflow history export sink for a Temporal Cloud namespace.
The sink configuration is preserved and can be re-enabled later.

Example:

```
temporal cloud namespace export disable --namespace my-namespace.my-account --sink-name my-sink
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
| `--sink-name` | Yes | **string** The name of the export sink. |

### export enable

Enable a previously disabled workflow history export sink for a Temporal Cloud namespace.

Example:

```
temporal cloud namespace export enable --namespace my-namespace.my-account --sink-name my-sink
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
| `--sink-name` | Yes | **string** The name of the export sink. |

### export gcs

Commands for managing GCS workflow history export sinks for Temporal Cloud namespaces.

#### export gcs create

Create a new GCS workflow history export sink for a Temporal Cloud namespace.
The sink is created in the enabled state.

Example:

```
temporal cloud namespace export gcs create --namespace my-namespace.my-account --sink-name my-sink \
  --service-account-email my-service-account@my-project.iam.gserviceaccount.com \
  --bucket-name my-bucket --region us-central1
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--bucket-name` | Yes | **string** The name of the destination GCS bucket. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--region` | Yes | **string** The GCS bucket region. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-email` | Yes | **string** The email of the customer service account that Temporal Cloud impersonates for writing to GCS (e.g. my-sa@my-project.iam.gserviceaccount.com). The service account ID and GCP project ID are parsed from this email. |
| `--sink-name` | Yes | **string** The name of the export sink. |

#### export gcs update

Update the configuration of an existing GCS workflow history export sink.
Only the flags you provide are changed; omitted flags keep their current
values. The enabled/disabled state and region are also preserved.

Example (rotate service account only):

```
temporal cloud namespace export gcs update --namespace my-namespace.my-account --sink-name my-sink \
  --service-account-email my-new-service-account@my-project.iam.gserviceaccount.com
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--bucket-name` | No | **string** The name of the destination GCS bucket. If omitted, the current value is kept. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-email` | No | **string** The email of the customer service account that Temporal Cloud impersonates for writing to GCS (e.g. my-sa@my-project.iam.gserviceaccount.com). The service account ID and GCP project ID are parsed from this email. If omitted, the current value is kept. |
| `--sink-name` | Yes | **string** The name of the export sink. |

#### export gcs validate

Validate a GCS workflow history export sink configuration without creating or updating it.
A successful response means the configuration is valid.

Example:

```
temporal cloud namespace export gcs validate --namespace my-namespace.my-account --sink-name my-sink \
  --service-account-email my-service-account@my-project.iam.gserviceaccount.com \
  --bucket-name my-bucket --region us-central1
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--bucket-name` | Yes | **string** The name of the destination GCS bucket. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--region` | Yes | **string** The GCS bucket region. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--service-account-email` | Yes | **string** The email of the customer service account that Temporal Cloud impersonates for writing to GCS (e.g. my-sa@my-project.iam.gserviceaccount.com). The service account ID and GCP project ID are parsed from this email. |
| `--sink-name` | Yes | **string** The name of the export sink. |

### export get

Retrieve the configuration and status of a workflow history export sink for a
Temporal Cloud namespace.

Example:

```
temporal cloud namespace export get --namespace my-namespace.my-account --sink-name my-sink
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--sink-name` | Yes | **string** The name of the export sink. |

### export list

List all workflow history export sinks configured for a Temporal Cloud namespace.

Example:

```
temporal cloud namespace export list --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### export s3

Commands for managing S3 workflow history export sinks for Temporal Cloud namespaces.

#### export s3 create

Create a new S3 workflow history export sink for a Temporal Cloud namespace.
The sink is created in the enabled state.

Example:

```
temporal cloud namespace export s3 create --namespace my-namespace.my-account --sink-name my-sink \
  --role-arn arn:aws:iam::123456789012:role/my-role --bucket-name my-bucket \
  --region us-east-1
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--bucket-name` | Yes | **string** The name of the destination S3 bucket. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--kms-arn` | No | **string** The AWS KMS key ARN for server-side encryption of exported data. Optional. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--region` | Yes | **string** The AWS region where the S3 bucket is located. |
| `--role-arn` | Yes | **string** The IAM role ARN that Temporal Cloud assumes for writing to S3 (e.g. arn:aws:iam::123456789012:role/my-role). The role name and AWS account ID are parsed from this ARN. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--sink-name` | Yes | **string** The name of the export sink. |

#### export s3 update

Update the configuration of an existing S3 workflow history export sink.
Only the flags you provide are changed; omitted flags keep their current
values. The enabled/disabled state and region are also preserved.

Example (rotate IAM role only):

```
temporal cloud namespace export s3 update --namespace my-namespace.my-account --sink-name my-sink \
  --role-arn arn:aws:iam::123456789012:role/my-new-role
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--async` | No | **bool** Return immediately after initiating the operation instead of waiting for completion. Use the returned operation ID to check status later. |
| `--async-operation-id` | No | **string** Custom identifier for tracking this async operation. If not provided, a unique ID is generated automatically. |
| `--bucket-name` | No | **string** The name of the destination S3 bucket. If omitted, the current value is kept. |
| `--idempotent` | No | **bool** Succeed silently if the resource already exists or matches the specification. Without this flag, the command errors when no changes are needed. |
| `--kms-arn` | No | **string** The AWS KMS key ARN for server-side encryption of exported data. If omitted, the current value is kept. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--poll-interval` | No | **duration** Time to wait between status checks when waiting for operation completion. Cannot be greater than 10 minutes. Supports minutes (m) and seconds (s). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--role-arn` | No | **string** The IAM role ARN that Temporal Cloud assumes for writing to S3 (e.g. arn:aws:iam::123456789012:role/my-role). The role name and AWS account ID are parsed from this ARN. If omitted, the current value is kept. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--sink-name` | Yes | **string** The name of the export sink. |

#### export s3 validate

Validate an S3 workflow history export sink configuration without creating or updating it.
A successful response means the configuration is valid.

Example:

```
temporal cloud namespace export s3 validate --namespace my-namespace.my-account --sink-name my-sink \
  --role-arn arn:aws:iam::123456789012:role/my-role --bucket-name my-bucket \
  --region us-east-1
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--bucket-name` | Yes | **string** The name of the destination S3 bucket. |
| `--kms-arn` | No | **string** The AWS KMS key ARN for server-side encryption of exported data. Optional. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--region` | Yes | **string** The AWS region where the S3 bucket is located. |
| `--role-arn` | Yes | **string** The IAM role ARN that Temporal Cloud assumes for writing to S3 (e.g. arn:aws:iam::123456789012:role/my-role). The role name and AWS account ID are parsed from this ARN. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--sink-name` | Yes | **string** The name of the export sink. |

## get

Retrieve the configuration and status of a Temporal Cloud namespace.

Returns details including region, retention period, endpoints, and
certificate information.

Example:

```
temporal cloud namespace get --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |
| `--spec` | No | **bool** Output only the namespace specification in JSON format, omitting metadata and status information. |

## ha

Commands for managing High Availability (HA) settings of Temporal Cloud namespaces.

HA settings control active region, managed failover, and replica regions.

### ha failover

Trigger a failover for a Temporal Cloud namespace to a different region.
The target region must already be a replica region of the namespace.

Example:

```
temporal cloud namespace ha failover --namespace my-namespace.my-account --region aws-us-west-2
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
| `--region` | Yes | **string** The target region to failover to (e.g., aws-us-west-2). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### ha get

Retrieve the current High Availability configuration for a Temporal Cloud namespace.
Shows the active region, whether managed failover is enabled, and whether passive poller forwarding is enabled.

Example:

```
temporal cloud namespace ha get --namespace my-namespace.my-account
```

Use the following options to change the behavior of this command. You can also use any of the [global flags](#global-flags) that apply to all subcommands.

| Flag | Required | Description |
|------|----------|-------------|
| `--api-key` | No | **string** API key for authenticating with Temporal Cloud. Can be used instead of interactive login for automation and CI/CD pipelines. |
| `--namespace`, `-n` | Yes | **string** The fully qualified namespace name in the format 'namespace.account' (e.g., 'my-namespace.my-account'). |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

### ha region

Commands for managing replica regions of Temporal Cloud namespaces.

#### ha region add

Add a replica region to a Temporal Cloud namespace. The region will be added
as a passive replica and can later be used for failover.

Example:

```
temporal cloud namespace ha region add --namespace my-namespace.my-account --region aws-us-west-2
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
| `--region` | Yes | **string** The region ID to add as a replica (e.g., aws-us-west-2). |
| `--resource-version`, `-v` | No | **string** Resource version for optimistic concurrency control. If not provided, the current version is fetched automatically. |
| `--server` | No | **string** Override the Temporal Cloud API server address. Used for connecting to non-production environments. |

#### ha region delete

Remove a replica region from a Temporal Cloud namespace. Note that a 7-day
cooldown period applies before the same region can be re-added.

Example:

```
temporal cloud namespace ha region delete --namespace my-namespace.my-account --region aws-us-west-2
