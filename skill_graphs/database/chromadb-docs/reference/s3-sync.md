# S3 Sync
Source: https://docs.trychroma.com/cloud/sync/s3

Sync files from Amazon S3 into Chroma Cloud.

S3 Sync lets you connect an Amazon S3 bucket to Chroma Cloud and sync files into collections. It supports documents (PDFs, Office files, images, ebooks), code, and plain text. Collections are created automatically if they don't already exist.

S3 Sync is designed for **append-only** workloads — it indexes new files but does not handle updates or deletes. If you re-sync the same object key, a new copy will be indexed. Creating a source does not automatically sync existing files in the bucket. Each file must be synced individually via an invocation. Configure [Auto-sync](#auto-sync) to automatically sync new uploads.

The Sync API uses your Chroma Cloud API key for authentication. See the [Sync API Reference](/reference/sync-api) for all endpoints.

## Walkthrough

### Creating an S3 Source via the Dashboard

1. Navigate to a database in Chroma Cloud and select **Sync** from the menu.
2. Click **Create** and select **S3** as the source type.
3. Enter your AWS access key ID and secret access key in the **AWS Credentials** step. The credentials are saved on your team and a credential ID is allocated; you can reuse that ID on subsequent sources via the API.
4. Enter the AWS region and bucket name.
5. Configure a collection name and optional path prefix to limit which keys can be synced.
6. Click **Sync** and enter an S3 object key to index.

## AWS Credentials

AWS credentials are managed at the team level and referenced from S3 sources by `aws_credential_id`. The first time you create an S3 source — whether via the dashboard or the API — Chroma saves the access key on your team and allocates a credential ID. Subsequent sources can reuse that ID without resending the secret.

### Supplying credentials via the API

When creating an S3 source via the API, you have two options. Provide **either**:

* `aws_credential_id`: an integer ID returned from a previously saved credential, **or**
* `aws_access_key_id` + `aws_secret_access_key`: an inline access key. Chroma stores the credential on your team and returns a credential ID that can be reused on subsequent sources.

```bash theme={null}
