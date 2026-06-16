# Manage bulk export destinations
Source: https://docs.langchain.com/langsmith/data-export-destinations

Configure and manage S3-compatible export destinations for LangSmith bulk exports.

<Note>
  **For self-hosted, GCP EU, GCP APAC, and AWS US SaaS**

  Update the LangSmith URL in the requests below for self-hosted installs, GCP EU (`eu.api.smith.langchain.com`), GCP APAC (`apac.api.smith.langchain.com`), or AWS US (`aws.api.smith.langchain.com`).
</Note>

A destination is a named configuration that tells LangSmith where to write exported trace data. You [create a destination](/langsmith/data-export#1-create-a-destination) once, then reference it by ID when [creating export jobs](/langsmith/data-export#2-create-an-export-job). LangSmith currently supports S3 and any S3-compatible bucket (such as GCS or MinIO) as a destination. Exported data is written in [Parquet](https://parquet.apache.org/docs/overview/) columnar format and contains equivalent fields to the [Run data format](/langsmith/run-data-format).

This page covers:

* The [configuration fields](#configuration-fields) needed to set up a destination.
* Required bucket [permissions](#permissions-required) for AWS S3 and GCS.
* How to [create a destination](#create-a-destination) via the API, including provider-specific examples and credential options.
* How to [rotate destination credentials](#rotate-destination-credentials) without recreating the destination.
* How to [debug destination errors](#debug-destination-errors).

## Configuration fields

The following information is needed to configure a destination:

* **Bucket Name**: The name of the S3 bucket where the data will be exported to.
* **Prefix**: The root prefix within the bucket where the data will be exported to.
* **S3 Region**: The region of the bucket—required for AWS S3 buckets.
* **Endpoint URL**: The endpoint URL for the S3 bucket—required for S3 API compatible buckets.
* **Access Key**: The access key for the S3 bucket.
* **Secret Key**: The secret key for the S3 bucket.
* **Include Bucket in Prefix** (optional): Whether to include the bucket name as part of the path prefix. Defaults to `true`. Set to `false` when using virtual-hosted style endpoints where the bucket name is already in the endpoint URL.
* **S3 Config Options** (`config_kwargs_s3`, optional): Advanced S3 addressing style and request settings passed to botocore. The most common use is setting `addressing_style` for S3-compatible services that require virtual-hosted or path-style requests:
  * `"virtual"`: bucket name is part of the hostname (e.g. `bucket.endpoint/key`). Required for some S3-compatible services such as Volcengine TOS.
  * `"path"`: bucket name is part of the URL path (e.g. `endpoint/bucket/key`).
  * `"auto"` (default): boto3 decides based on the endpoint.

We support any S3 compatible bucket. For non-AWS buckets such as GCS or MinIO, you will need to provide the endpoint URL.

## Permissions required

Both the `backend` and `queue` services require write access to the destination bucket:

* The `backend` service attempts to write a test file to the destination bucket when the export destination is created. It will delete the test file if it has permission to do so (delete access is optional).
* The `queue` service is responsible for bulk export execution and uploading the files to the bucket.

### AWS S3 permissions

The minimal AWS S3 permission policy relies on the following permissions:

* `s3:PutObject` (required): Allows writing Parquet files to the bucket.
* `s3:DeleteObject` (optional): Cleans up test files during destination creation. If this permission isn't present, the file is left under the `/tmp` directory after destination creation.
* `s3:GetObject` (optional but recommended): Verifies file size after writing.
* `s3:AbortMultipartUpload` (optional but recommended): Avoids dangling multipart uploads.

Minimal IAM policy example:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::YOUR_BUCKET_NAME/*"
      ]
    }
  ]
}
```

Recommended IAM policy example with additional permissions:

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::YOUR_BUCKET_NAME/*"
      ]
    }
  ]
}
```

### Google Cloud Storage (GCS) permissions

When using GCS with the S3-compatible XML API, the following IAM permissions are required:

* `storage.objects.create` (required): Allows writing files to the bucket.
* `storage.objects.delete` (optional): Cleans up test files during destination creation. If this permission isn't present, the file is left under the `/tmp` directory after destination creation.
* `storage.objects.get` (optional but recommended): Verifies file size after writing.

These permissions can be granted through the "Storage Object Admin" predefined role or a custom role.

## Create a destination

The following example demonstrates how to create a destination using cURL. Replace the placeholder values with your actual configuration details.
Note that credentials will be stored securely in an encrypted form in our system.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request POST \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports/destinations' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
  --data '{
    "destination_type": "s3",
    "display_name": "My S3 Destination",
    "config": {
      "bucket_name": "your-s3-bucket-name",
      "prefix": "root_folder_prefix",
      "region": "your aws s3 region",
      "endpoint_url": "your endpoint url for s3 compatible buckets",
      "include_bucket_in_prefix": true // defaults to true, can be omitted
    },
    "credentials": {
      "access_key_id": "YOUR_S3_ACCESS_KEY_ID",
      "secret_access_key": "YOUR_S3_SECRET_ACCESS_KEY"
    }
  }'
```

Use the returned `id` to reference this destination in subsequent bulk export operations.

**If you receive an error while creating a destination, see [Debug destination errors](#debug-destination-errors) for details on how to debug this.**

### Credentials configuration

<Note>**Requires LangSmith Helm version >= `0.10.34` (application version >= `0.10.91`)**</Note>

We support the following additional credentials formats besides static `access_key_id` and `secret_access_key`:

* To use [temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) that include an AWS session token,
  additionally provide the `credentials.session_token` key when creating the bulk export destination.
* (Self-hosted only): To use environment-based credentials such as with [AWS IAM Roles for Service Accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) (IRSA),
  omit the `credentials` key from the request when creating the bulk export destination.
  In this case, the [standard Boto3 credentials locations](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#credentials) will be checked in the order defined by the library.

### AWS S3 bucket

For AWS S3, you can leave off the `endpoint_url` and supply the region that matches the region of your bucket.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request POST \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports/destinations' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
  --data '{
    "destination_type": "s3",
    "display_name": "My AWS S3 Destination",
    "config": {
      "bucket_name": "my_bucket",
      "prefix": "data_exports",
      "region": "us-east-1"
    },
    "credentials": {
      "access_key_id": "YOUR_S3_ACCESS_KEY_ID",
      "secret_access_key": "YOUR_S3_SECRET_ACCESS_KEY"
    }
  }'
```

### Google GCS XML S3 compatible bucket

When using Google's GCS bucket, you need to use the XML S3 compatible API, and supply the `endpoint_url`
which is typically `https://storage.googleapis.com`.
Here is an example of the API request when using the GCS XML API which is compatible with S3:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request POST \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports/destinations' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
  --data '{
    "destination_type": "s3",
    "display_name": "My GCS Destination",
    "config": {
      "bucket_name": "my_bucket",
      "prefix": "data_exports",
      "endpoint_url": "https://storage.googleapis.com"
      "include_bucket_in_prefix": true // defaults to true, can be omitted
    },
    "credentials": {
      "access_key_id": "YOUR_S3_ACCESS_KEY_ID",
      "secret_access_key": "YOUR_S3_SECRET_ACCESS_KEY"
    }
  }'
```

See [Google documentation](https://cloud.google.com/storage/docs/interoperability#xml_api) for more info

### S3-compatible bucket with virtual-hosted style addressing

Some S3-compatible services (such as Volcengine TOS) require virtual-hosted style addressing, where the bucket name is part of the hostname rather than the URL path. Use `config_kwargs_s3` with `addressing_style: "virtual"` to enable this:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request POST \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports/destinations' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
  --data '{
    "destination_type": "s3",
    "display_name": "My Volcengine TOS Destination",
    "config": {
      "bucket_name": "my_bucket",
      "prefix": "data_exports",
      "endpoint_url": "https://tos-s3-cn-beijing.volces.com",
      "config_kwargs_s3": {
        "addressing_style": "virtual"
      }
    },
    "credentials": {
      "access_key_id": "YOUR_ACCESS_KEY_ID",
      "secret_access_key": "YOUR_SECRET_ACCESS_KEY"
    }
  }'
```

### S3-compatible bucket with virtual-hosted style endpoint

If your endpoint URL already includes the bucket name (virtual-hosted style), set `include_bucket_in_prefix` to `false` to avoid duplicating the bucket name in the path:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request POST \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports/destinations' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
  --data '{
    "destination_type": "s3",
    "display_name": "My Virtual-Hosted Destination",
    "config": {
      "bucket_name": "my_bucket",
      "prefix": "data_exports",
      "endpoint_url": "https://my_bucket.s3.us-east-1.amazonaws.com",
      "include_bucket_in_prefix": false
    },
    "credentials": {
      "access_key_id": "YOUR_S3_ACCESS_KEY_ID",
      "secret_access_key": "YOUR_S3_SECRET_ACCESS_KEY"
    }
  }'
```

## Rotate destination credentials

Use `PATCH /api/v1/bulk-exports/destinations/{destination_id}` to update the credentials on an existing destination. This lets you rotate or replace credentials without recreating the destination or its associated bulk exports. The destination configuration (bucket, prefix, region, endpoint, etc.) is unchanged—only the credentials are replaced.

### Credential rotation behavior

The changeover is not instantaneous:

* **New bulk export runs** use the updated credentials immediately after the PATCH completes.
* **Already running bulk export runs** continue using the previous credentials until they finish.
* **Both sets of credentials are active simultaneously** during the transition period. This window lasts up to the maximum runtime of a single bulk export run.

Plan your rotation accordingly: the old credentials must remain valid until all in-flight runs complete.

### Request

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request PATCH \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports/destinations/{destination_id}' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
  --data '{
    "credentials": {
      "access_key_id": "YOUR_NEW_ACCESS_KEY_ID",
      "secret_access_key": "YOUR_NEW_SECRET_ACCESS_KEY"
    }
  }'
```

The `session_token` field is optional, which you can include for [temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html).

[**Required permission**](/langsmith/organization-workspace-operations): `bulk-exports:manage` (or `workspaces:manage`, which historically granted this access).

Before storing new credentials, LangSmith validates them by performing a test write to the bucket using the existing destination configuration. The request fails with `400` if the credentials do not have sufficient write permissions. If the request fails, refer to [Debug destination errors](#debug-destination-errors).

### Response

Returns the updated destination object. Credential values are never returned—only the credential field names are included in the response under `credentials_keys`.

```json theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
{
  "id": "destination-uuid",
  "tenant_id": "tenant-uuid",
  "created_at": "2025-01-01T00:00:00Z",
  "updated_at": "2025-06-01T00:00:00Z",
  "credentials_keys": ["access_key_id", "secret_access_key"]
}
```

### Rotation checklist

1. Provision new credentials in your cloud provider with write access to the destination bucket and prefix.
2. Call the PATCH endpoint with the new credentials. LangSmith validates them before saving.
3. Keep old credentials active until all in-flight bulk export runs finish (up to the [maximum run duration](/langsmith/data-export-monitor#automatic-retry-behavior)).
4. Revoke old credentials once no runs are using them.

## Debug destination errors

The destinations API endpoint will validate that the destination and credentials are valid and that write access
is present for the bucket.

If you receive an error, and would like to debug this error, you can use the [AWS CLI](https://aws.amazon.com/cli/)
to test the connectivity to the bucket. You should be able to write a file with the CLI using the same
data that you supplied to the destinations API above.

**AWS S3:**

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
aws configure

# set the same access key credentials and region as you used for the destination
> AWS Access Key ID: <access_key_id>
> AWS Secret Access Key: <secret_access_key>
> Default region name [us-east-1]: <region>

# List buckets
aws s3 ls /

# test write permissions
touch ./test.txt
aws s3 cp ./test.txt s3://<bucket-name>/tmp/test.txt
```

**GCS Compatible Buckets:**

You will need to supply the endpoint\_url with `--endpoint-url` option.
For GCS, the `endpoint_url` is typically `https://storage.googleapis.com`:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
aws configure

# set the same access key credentials and region as you used for the destination
> AWS Access Key ID: <access_key_id>
> AWS Secret Access Key: <secret_access_key>
> Default region name [us-east-1]: <region>

# List buckets
aws s3 --endpoint-url=<endpoint_url> ls /

# test write permissions
touch ./test.txt
aws s3 --endpoint-url=<endpoint_url> cp ./test.txt s3://<bucket-name>/tmp/test.txt
```

### Common errors

Here are some common errors:

| Error                              | Description                                                                                                                                                                                                                                                                                              |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access denied                      | The blob store credentials or bucket are not valid. This error occurs when the provided access key and secret key combination doesn't have the necessary permissions to access the specified bucket or perform the required operations.                                                                  |
| Bucket is not valid                | The specified blob store bucket is not valid. This error is thrown when the bucket doesn't exist or there is not enough access to perform writes on the bucket.                                                                                                                                          |
| Key ID you provided does not exist | The blob store credentials provided are not valid. This error occurs when the access key ID used for authentication is not a valid key.                                                                                                                                                                  |
| Invalid endpoint                   | The endpoint\_url provided is invalid. This error is raised when the specified endpoint is an invalid endpoint. Only S3 compatible endpoints are supported, for example `https://storage.googleapis.com` for GCS, `https://play.min.io` for minio, etc. If using AWS, you should omit the endpoint\_url. |
| InvalidBucketName                  | The S3-compatible service rejected the request due to addressing style mismatch. Some services require virtual-hosted style addressing. Set `config_kwargs_s3: {"addressing_style": "virtual"}` in your destination config to resolve this.                                                              |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/data-export-destinations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Import exported data
Source: https://docs.langchain.com/langsmith/data-export-downstream

Import LangSmith bulk-exported Parquet data into BigQuery, Snowflake, Redshift, Clickhouse, or DuckDB.

Importing data from S3 and Parquet format is commonly supported by the majority of analytical systems. See below for documentation links:

## BigQuery

To import your data into BigQuery, see [Loading Data from Parquet](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-parquet) and also
[Hive Partitioned loads](https://cloud.google.com/bigquery/docs/hive-partitioned-loads-gcs).

## Snowflake

You can load data into Snowflake from S3 by following the [Load from Cloud Document](https://docs.snowflake.com/en/user-guide/tutorials/load-from-cloud-tutorial).

## RedShift

You can COPY data from S3 or Parquet into Amazon Redshift by following the [AWS COPY command documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html).

## Clickhouse

You can directly query data in S3 / Parquet format in Clickhouse. As an example, if using GCS, you can query the data as follows:

```sql theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
SELECT count(distinct id) FROM s3('https://storage.googleapis.com/<bucket>/<prefix>/export_id=<export_id>/**',
 'access_key_id', 'access_secret', 'Parquet')
```

See [Clickhouse S3 Integration Documentation](https://clickhouse.com/docs/en/engines/table-engines/integrations/s3) for more information.

## DuckDB

You can query the data from S3 in-memory with SQL using DuckDB. See [S3 import Documentation](https://duckdb.org/docs/guides/network_cloud_storage/s3_import.html).

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/data-export-downstream.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# Monitor and troubleshoot bulk exports
Source: https://docs.langchain.com/langsmith/data-export-monitor

Monitor bulk export status, manage running exports, and troubleshoot failures.

Once you have [created an export job](/langsmith/data-export#2-create-an-export-job), you can use the APIs on this page to track its progress, inspect individual runs, and stop it if needed. This page also covers how LangSmith handles failures automatically, and what to do when an export fails after exhausting retries.

This page covers:

* [Monitoring export status](#monitor-export-status) and [listing runs](#list-runs-for-an-export) for a specific export.
* [Listing all exports](#list-all-exports) in your workspace.
* [Stopping an export](#stop-an-export).
* [Failure modes and retry policy](#failure-modes-and-retry-policy), including automatic retry behavior, failure scenarios, status lifecycle, concurrency limits, and progress tracking.
* [Troubleshooting failed exports](#troubleshooting-failed-exports).

<Note>
  **For self-hosted, GCP EU, GCP APAC, and AWS US SaaS**

  Update the LangSmith URL in the requests below for self-hosted installs, GCP EU (`eu.api.smith.langchain.com`), GCP APAC (`apac.api.smith.langchain.com`), or AWS US (`aws.api.smith.langchain.com`).
</Note>

## Monitor export status

To monitor the status of an export job, use the following cURL command:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request GET \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports/{export_id}' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID'
```

Replace `{export_id}` with the ID of the export you want to monitor. This command retrieves the current status of the specified export job.

## List runs for an export

An export is typically broken up into multiple runs which correspond to a specific date partition to export.
To list all runs associated with a specific export, use the following cURL command:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request GET \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports/{export_id}/runs' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID'
```

This command fetches all runs related to the specified export, providing details such as run ID, status, creation time, rows exported, etc.

## List all exports

To retrieve a list of all export jobs, use the following cURL command:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request GET \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID'
```

This command returns a list of all export jobs along with their current statuses and creation timestamps.

## Stop an export

To stop an existing export, use the following cURL command:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl --request PATCH \
  --url 'https://api.smith.langchain.com/api/v1/bulk-exports/{export_id}' \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_API_KEY' \
  --header 'X-Tenant-Id: YOUR_WORKSPACE_ID' \
  --data '{
    "status": "Cancelled"
}'
```

Replace `{export_id}` with the ID of the export you wish to cancel. Note that a job cannot be restarted once it has been cancelled,
you will need to create a new export job instead.

## Failure modes and retry policy

LangSmith bulk exports handle transient failures and infrastructure issues automatically to ensure resilience.

Each bulk export is divided into multiple *runs*, where each run processes data for a [specific date partition](/langsmith/data-export#partitioning-scheme) (typically organized by day). Runs are processed independently, which enables:

* Parallel processing of different time periods.
* Independent retry logic for each run.
* Resumption from specific checkpoints if interrupted.

Each run (date range) in your export has its own [failure handling](#failure-scenarios) and [retry budget](#automatic-retry-behavior). If a run fails after exhausting all retries, the entire export is marked as `FAILED`.

### Automatic retry behavior

Export jobs automatically retry transient failures with the following behavior:

* **Maximum retry attempts**: 20 retries per run (subject to change).
* **Retry delay**: 30 seconds between attempts (fixed, no exponential backoff).
* **Run timeout**: 4 hours maximum per run.
* **Overall workflow timeout**: 72 hours for the entire export.

### Failure scenarios

| Failure type                    | Cause                                                                                                                                                                                                                                           | Automatic retry?                                    | Action required                                                                                                              |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Infrastructure interruption** | [Deployments](/langsmith/deployment), server restarts, worker crashes                                                                                                                                                                           | Yes, automatically requeued with remaining retries. | None, jobs resume automatically.                                                                                             |
| **Run timeout**                 | Single run exceeds 4-hour limit                                                                                                                                                                                                                 | Yes, retried up to 20 times (subject to change).    | If persistent, narrow date range, add filters, or [limit the exported fields](/langsmith/data-export#limit-exported-fields). |
| **Workflow timeout**            | Entire export exceeds 72 hours                                                                                                                                                                                                                  | No                                                  | Reduce export scope (date range, filters) or break into smaller exports.                                                     |
| **Storage/destination errors**  | [Invalid credentials](/langsmith/data-export-destinations#credentials-configuration), [missing bucket](/langsmith/data-export-destinations#configuration-fields), [permission issues](/langsmith/data-export-destinations#permissions-required) | No                                                  | Fix destination configuration and create new export.                                                                         |
| **Destination deleted**         | Bucket removed during export                                                                                                                                                                                                                    | No                                                  | Recreate destination and restart export.                                                                                     |
| **Terminal processing errors**  | Data serialization issues, resource exhaustion                                                                                                                                                                                                  | Yes, retried up to 20 times (subject to change).    | Check run error details; may require investigation.                                                                          |

<Note>
  Any single run failure (after all retries are exhausted) causes the entire export to fail.
</Note>

### Export status lifecycle

Exports can have the following statuses:

| Status      | Description                                             |
| ----------- | ------------------------------------------------------- |
| `CREATED`   | Export has been created but not yet started processing. |
| `RUNNING`   | Export is actively processing runs.                     |
| `COMPLETED` | All runs successfully exported.                         |
| `FAILED`    | One or more runs failed after exhausting retries.       |
| `CANCELLED` | Export was manually cancelled by user.                  |
| `TIMEDOUT`  | Export exceeded the 48-hour workflow timeout.           |

Individual runs can have the same possible statuses: `CREATED`, `RUNNING`, `COMPLETED`, `FAILED`, `CANCELLED`, or `TIMEDOUT`.

### Concurrency and rate limits

To ensure system stability, exports are subject to the following limits:

* **Maximum concurrent runs per export**: 45
* **Maximum concurrent exports per workspace**: 15

If you have multiple exports running, new run jobs will queue until capacity becomes available.

### Progress tracking and resumability

The export system maintains detailed progress metadata for each run:

* Latest cursor position in the data stream.
* Number of rows exported.
* List of Parquet files written.

This progress tracking enables:

* **Graceful resumption**: If a run is interrupted (e.g., by a deployment), it resumes from the last checkpoint rather than starting over.
* **Progress monitoring**: Track how much data has been exported through the API.
* **Efficient retries**: Failed runs don't re-export data that was already successfully written.

### Troubleshooting failed exports

If your export fails, follow these steps:

1. **Check the export status**: Use the [`GET /api/v1/bulk-exports/{export_id}` endpoint](/langsmith/smith-api/bulk-exports/get-bulk-export) to retrieve the export details and status.
2. **Review run errors**: You can monitor your runs using the [List Runs API](#list-runs-for-an-export). Each run includes an `errors` field with detailed error messages keyed by retry attempt (e.g., `retry_0`, `retry_1`).
3. **Verify destination access**: Ensure your [destination bucket](/langsmith/data-export-destinations#configuration-fields) still exists and [credentials](/langsmith/data-export-destinations#credentials-configuration) are valid.
4. **Check run size**: If you see timeout errors, your date partitions may contain too much data. It may be helpful to [limit the exported fields](/langsmith/data-export#limit-exported-fields).
5. **Review system limits**: Ensure you're not hitting [concurrency limits](#concurrency-and-rate-limits) (5 runs per export, 3 exports per workspace).

For storage-related errors, you can test your destination configuration using the AWS CLI or gsutil before retrying the export.

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/data-export-monitor.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>

# LangSmith data plane
Source: https://docs.langchain.com/langsmith/data-plane

The *data plane* consists of your [Agent Servers](/langsmith/agent-server) (deployments), their supporting infrastructure, and the "listener" application that continuously polls for updates from the [LangSmith control plane](/langsmith/control-plane).

## Server infrastructure

In addition to the [Agent Server](/langsmith/agent-server) itself, the following infrastructure components for each server are also included in the broad definition of "data plane":

* **PostgreSQL**: persistence layer for user, run, and memory data.
* **Redis**: communication and ephemeral metadata for workers.
* **Secrets store**: secure management of environment secrets.
* **Autoscalers**: scale server containers based on load.

## "Listener" application

The data plane "listener" application periodically calls [control plane APIs](/langsmith/control-plane#control-plane-api) to:

* Determine if new deployments should be created.
* Determine if existing deployments should be updated (i.e. new revisions).
* Determine if existing deployments should be deleted.

In other words, the data plane "listener" reads the latest state of the control plane (desired state) and takes action to reconcile outstanding deployments (current state) to match the latest state.

## PostgreSQL

PostgreSQL stores server resources (threads, runs, assistants, crons) and items saved in the [long-term memory store](/oss/python/langgraph/stores). It is also the default backend for [checkpoints](/oss/python/langgraph/persistence) (graph execution state). You can optionally store checkpoints in MongoDB instead—see [Configure checkpointer backend](/langsmith/configure-checkpointer). PostgreSQL is always required regardless of the checkpointer backend.

## Redis

Redis is used in each Agent Server as a way for server and queue workers to communicate, and to store ephemeral metadata. No user or run data is stored in Redis.

### Communication

All runs in an Agent Server are executed by a pool of background workers that are part of each deployment. In order to enable some features for those runs (such as cancellation and output streaming) we need a channel for two-way communication between the server and the worker handling a particular run. We use Redis to organize that communication.

1. A Redis list is used as a mechanism to wake up a worker as soon as a new run is created. Only a sentinel value is stored in this list, no actual run information. The run information is then retrieved from PostgreSQL by the worker.
2. A combination of a Redis string and Redis PubSub channel is used for the server to communicate a run cancellation request to the appropriate worker.
3. A Redis PubSub channel is used by the worker to broadcast streaming output from an agent while the run is being handled. Any open `/stream` request in the server will subscribe to that channel and forward any events to the response as they arrive. No events are stored in Redis at any time.

### Ephemeral metadata

Runs in an Agent Server may be retried for specific failures (currently only for transient PostgreSQL errors encountered during the run). In order to limit the number of retries (currently limited to 3 attempts per run) we record the attempt number in a Redis string when it is picked up. This contains no run-specific info other than its ID, and expires after a short delay.

## Data plane features

This section describes various features of the data plane.

### Data region

<Info>
  **Only for Cloud**
  Data regions are only applicable for [Cloud](/langsmith/cloud) deployments.
</Info>

Deployments can be created in 2 data regions: US and EU

The data region for a deployment is implied by the data region of the LangSmith organization where the deployment is created. Deployments and the underlying database for the deployments cannot be migrated between data regions.

### Autoscaling

[`Production` type](/langsmith/control-plane#deployment-types) deployments automatically scale up to 10 containers. Scaling is based on 3 metrics:

1. CPU utilization
2. Memory utilization
3. Number of pending (in progress) [runs](/langsmith/runs)

For CPU utilization, the autoscaler targets 75% utilization. This means the autoscaler will scale the number of containers up or down to ensure that CPU utilization is at or near 75%. For memory utilization, the autoscaler targets 75% utilization as well.

For number of pending runs, the autoscaler targets 10 pending runs. For example, if the current number of containers is 1, but the number of pending runs is 20, the autoscaler will scale up the deployment to 2 containers (20 pending runs / 2 containers = 10 pending runs per container).

Each metric is computed independently and the autoscaler will determine the scaling action based on the metric that results in the largest number of containers.

These metrics don't all apply to every container type. [Queue workers](/langsmith/agent-server#runtime-architecture) scale on pending run count—when the backlog grows, more workers spin up to drain it. [API servers](/langsmith/agent-server#runtime-architecture) scale on CPU and memory, responding to client request volume. This means a spike in run submissions won't slow down read operations like fetching thread state. For self-hosted configuration details, see [Configure Agent Server for scale](/langsmith/agent-server-scale).

Scale down actions are delayed for 30 minutes before any action is taken. In other words, if the autoscaler decides to scale down a deployment, it will first wait for 30 minutes before scaling down. After 30 minutes, the metrics are recomputed and the deployment will scale down if the recomputed metrics result in a lower number of containers than the current number. Otherwise, the deployment remains scaled up. This "cool down" period ensures that deployments do not scale up and down too frequently.

### Static IP addresses

<Info>
  **Only for Cloud**
  Static IP addresses are only available for [Cloud](/langsmith/cloud) deployments.
</Info>

All traffic from deployments created after January 6th 2025 will come through a NAT gateway. This NAT gateway will have several static IP addresses depending on the data region. For the list of static IP addresses, refer to the [Allowlist IP addresses table](/langsmith/deploy-to-cloud#allowlist-ip-addresses).

### Payload size

<Info>
  **Only for Cloud**
  Payload size restrictions are only applicable to [Cloud](/langsmith/cloud) deployments.
</Info>

The maximum payload size for all requests sent to [Cloud](/langsmith/cloud) deployments is 25 MB. Attempting to send a request with a payload larger than 25 MB will result in a `413 Payload Too Large` error.

### Custom PostgreSQL

<Info>
  Custom PostgreSQL instances are only available for [self-hosted](/langsmith/self-hosted) deployments.
</Info>

A custom PostgreSQL instance can be used instead of the [one automatically created by the control plane](/langsmith/control-plane#database-provisioning). Specify the [`POSTGRES_URI_CUSTOM`](/langsmith/env-var#postgres_uri_custom) environment variable to use a custom PostgreSQL instance.

Multiple deployments can share the same PostgreSQL instance. For example, for `Deployment A`, `POSTGRES_URI_CUSTOM` can be set to `postgres://<user>:<password>@/<database_name_1>?host=<hostname_1>` and for `Deployment B`, `POSTGRES_URI_CUSTOM` can be set to `postgres://<user>:<password>@/<database_name_2>?host=<hostname_1>`. `<database_name_1>` and `database_name_2` are different databases within the same instance, but `<hostname_1>` is shared. **The same database cannot be used for separate deployments**.

### Custom Redis

<Info>
  Custom Redis instances are only available for [Self-Hosted](/langsmith/self-hosted) deployments.
</Info>

A custom Redis instance can be used instead of the one automatically created by the control plane. Specify the [REDIS\_URI\_CUSTOM](/langsmith/env-var#redis_uri_custom) environment variable to use a custom Redis instance.

Multiple deployments can share the same Redis instance. For example, for `Deployment A`, `REDIS_URI_CUSTOM` can be set to `redis://<hostname_1>:<port>/1` and for `Deployment B`, `REDIS_URI_CUSTOM` can be set to `redis://<hostname_1>:<port>/2`. `1` and `2` are different database numbers within the same instance, but `<hostname_1>` is shared. **The same database number cannot be used for separate deployments**.

### MongoDB checkpointing

<Info>
  Available for [Cloud](/langsmith/cloud) (with an externally managed MongoDB instance) and [Standalone](/langsmith/deploy-standalone-server) deployments.
</Info>

You can use MongoDB as an alternative backend for checkpoint storage. When configured, MongoDB handles only checkpoint data—PostgreSQL remains required for all other server resources.

See [Configure checkpointer backend](/langsmith/configure-checkpointer) for setup instructions.

### LangSmith tracing

Agent Server is automatically configured to send traces to LangSmith. See the table below for details with respect to each deployment option.

| Cloud                                  | Hybrid                                                    | Self-Hosted                                                                                |
| -------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Required<br />Trace to LangSmith SaaS. | Optional<br />Disable tracing or trace to LangSmith SaaS. | Optional<br />Disable tracing, trace to LangSmith SaaS, or trace to Self-Hosted LangSmith. |

### Telemetry

Agent Server is automatically configured to report telemetry metadata for billing purposes. See the table below for details with respect to each deployment option.

| Cloud                             | Hybrid                            | Self-Hosted                                                                                                              |
| --------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Telemetry sent to LangSmith SaaS. | Telemetry sent to LangSmith SaaS. | Self-reported usage (audit) for air-gapped license key.<br />Telemetry sent to LangSmith SaaS for LangSmith License Key. |

### Licensing

Agent Server is automatically configured to perform license key validation. See the table below for details with respect to each deployment option.

| Cloud                                               | Hybrid                                              | Self-Hosted                                                                      |
| --------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------- |
| LangSmith API Key validated against LangSmith SaaS. | LangSmith API Key validated against LangSmith SaaS. | Air-gapped license key or Platform License Key validated against LangSmith SaaS. |

***

<div>
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/data-plane.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
