# Upload metadata file to trigger indexing
aws s3 cp report.meta.json s3://my-bucket/docs/report.meta.json
```

## Multi-Tenant Buckets

S3 Sync supports multi-tenant setups where a single bucket serves multiple tenants.

**Path prefixes** restrict which S3 keys a source can sync. When a `path_prefix` is configured, only objects whose key starts with that prefix can be synced — invocations for keys outside the prefix will be rejected. Create one source per tenant with a distinct prefix (e.g. `tenant-a/`, `tenant-b/`) to enforce isolation within a shared bucket.

**Metadata files** offer another approach to multi-tenancy. In metadata mode, each `.meta.json` file can specify a `target_collection_name`, routing different files to different collections. This lets you partition data per tenant at the collection level without needing separate sources or path prefixes.
