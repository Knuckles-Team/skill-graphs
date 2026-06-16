# Reuse an existing credential
curl -X POST https://sync.trychroma.com/api/v1/sources \
  -H "x-chroma-token: $CHROMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "database_name": "my-db",
    "s3": {
      "bucket_name": "my-bucket",
      "region": "us-east-1",
      "collection_name": "my-collection",
      "aws_credential_id": 42
    }
  }'
