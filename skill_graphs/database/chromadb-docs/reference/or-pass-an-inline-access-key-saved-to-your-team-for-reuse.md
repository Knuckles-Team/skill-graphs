# Or pass an inline access key (saved to your team for reuse)
curl -X POST https://sync.trychroma.com/api/v1/sources \
  -H "x-chroma-token: $CHROMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "database_name": "my-db",
    "s3": {
      "bucket_name": "my-bucket",
      "region": "us-east-1",
      "collection_name": "my-collection",
      "aws_access_key_id": "AKIA...",
      "aws_secret_access_key": "..."
    }
  }'
```

The IAM user behind the credential needs `s3:GetObject` (and `s3:ListBucket` if you use a path prefix) on the bucket. For [Auto-Sync](#auto-sync), no extra permissions are required on the credential itself; events flow through an SQS queue managed by Chroma.

## S3 Source Configuration

| Parameter               | Required | Description                                                                                                                                   |
| ----------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `bucket_name`           | Yes      | S3 bucket name.                                                                                                                               |
| `region`                | Yes      | AWS region of the bucket.                                                                                                                     |
| `collection_name`       | Yes      | Default target collection name for synced data.                                                                                               |
| `aws_credential_id`     | \*       | ID of AWS credentials saved in the Chroma dashboard. Mutually exclusive with the inline access-key fields.                                    |
| `aws_access_key_id`     | \*       | Inline AWS access key ID. Required together with `aws_secret_access_key` if `aws_credential_id` is not provided.                              |
| `aws_secret_access_key` | \*       | Inline AWS secret access key. Required together with `aws_access_key_id` if `aws_credential_id` is not provided.                              |
| `path_prefix`           | No       | Limits which S3 keys can be synced. Only keys starting with this prefix are allowed. Useful for [multi-tenant setups](#multi-tenant-buckets). |
| `auto_sync`             | No       | Auto-sync mode: `none` (default), `direct`, or `metadata`. Configured by Chroma during [Auto-Sync](#auto-sync) setup.                         |

\* Provide either `aws_credential_id`, or both `aws_access_key_id` and `aws_secret_access_key`.

## S3 Invocation Parameters

| Parameter                | Required | Description                                                                                                                                                                                                |
| ------------------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `object_key`             | Yes      | Full S3 object key to sync. This is always relative to the bucket root, even if a `path_prefix` is configured on the source. The key must start with the `path_prefix` or the invocation will be rejected. |
| `custom_id`              | No       | Custom document ID (max 120 bytes). Chunk IDs become `custom_id-{chunk}` instead of `sha256(object_key)-{chunk}`. Stored as `custom_id` metadata on each chunk.                                            |
| `metadata`               | No       | Additional metadata merged with standard chunk metadata. Values can be scalars (string, number, boolean, or null) or homogeneous arrays of scalars (e.g. `["action", "comedy"]`).                          |
| `target_collection_name` | No       | Overrides the source's `collection_name`. Collection is created if it doesn't exist.                                                                                                                       |

## Supported File Types

File types are detected by filename suffix.

### Document Types

Document files are converted to markdown and incur a \$0.01/page extraction fee. Tables, headings, and structure are preserved. Images within documents get text descriptions extracted, but the images themselves are not stored.

| Format        | Extensions                                                |
| ------------- | --------------------------------------------------------- |
| PDF           | `.pdf`                                                    |
| Word          | `.doc`, `.docx`, `.odt`                                   |
| Spreadsheets  | `.xls`, `.xlsx`, `.xlsm`, `.xltx`, `.csv`, `.ods`         |
| Presentations | `.ppt`, `.pptx`, `.odp`                                   |
| HTML          | `.html`                                                   |
| Ebooks        | `.epub`                                                   |
| Images        | `.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.tiff`, `.tif` |

### Other Files

All other files must contain valid UTF-8 text. Non-UTF-8 files will fail.

### Limits

* **Database region**: Chroma Sync is currently only available for Chroma databases hosted in `aws-us-east-1`. Databases in `gcp-europe-west1` cannot use Sync yet. See [Regions](/cloud/getting-started#regions). The S3 bucket itself can be in any AWS region — that is what the source's `region` field controls.
* **Maximum file size**: 200 MB per file.
* **Maximum document pages**: 7,000 pages per document. Documents exceeding this limit will fail.

Contact [support@trychroma.com](mailto:support@trychroma.com) if you need these limits raised.

## Chunking

Files are chunked using a three-stage pipeline:

1. **Tree-sitter syntax-aware chunking** — if the file extension maps to a known programming language, chunking respects function boundaries, class definitions, and code structure.
2. **Tree-sitter markdown chunking** — if the content is markdown (e.g. from document extraction), chunking respects headings, sections, and paragraph boundaries.
3. **Line-based chunking** — fallback for other text content (max 10 lines, max 4096 bytes per chunk).

## Auto-Sync

Auto-sync lets S3 file uploads automatically trigger indexing without manual API calls.

### Setup

Chroma runs one SQS queue per AWS region. To enable auto-sync:

1. Contact Chroma at [support@trychroma.com](mailto:support@trychroma.com) with your AWS region.
2. Chroma will provide the SQS queue ARN for your region.
3. Configure [S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-event-notifications.html) on your bucket to send `s3:ObjectCreated:*` events to that queue.

### Direct Mode

When Chroma configures your source for direct mode (`auto_sync: "direct"`), every file upload to your bucket triggers indexing of that file. This is the simplest setup when filenames are stable identifiers. If a `.meta.json` file is uploaded, it is processed as metadata mode for that file.

### Metadata Mode

When Chroma configures your source for metadata mode (`auto_sync: "metadata"`), only `.meta.json` file uploads trigger indexing. This gives you low-level control over each file's document ID, additional metadata, and target collection. It also lets you choose which files to index — only files referenced by a `.meta.json` are processed.

### Metadata File Format

A metadata file is any file with a `.meta.json` suffix. It can have any name and be in any folder, as long as it falls within the source's `path_prefix` (if one is configured).

```json theme={null}
{
  "version": "chroma-v1",
  "id": "unique-document-id",
  "path": "path/to/document.pdf",
  "target_collection_name": "my-collection",
  "metadata": {
    "author": "Jane Doe",
    "year": 2024,
    "tags": ["quarterly", "finance"]
  }
}
```

| Field                    | Required | Description                                                                                                     |
| ------------------------ | -------- | --------------------------------------------------------------------------------------------------------------- |
| `version`                | Yes      | Must be `"chroma-v1"`.                                                                                          |
| `id`                     | Yes      | Custom ID for the document in Chroma.                                                                           |
| `path`                   | Yes      | Full S3 object key of the document to index.                                                                    |
| `target_collection_name` | No       | Overrides the target collection (created if it doesn't exist).                                                  |
| `metadata`               | No       | Additional metadata. Values can be scalars (string, number, boolean, or null) or homogeneous arrays of scalars. |

### Example Workflow

```bash theme={null}
