# Cloud profile for Temporal Cloud
[profile.cloud]
address = "your-namespace.a1b2c.tmprl.cloud:7233"
namespace = "your-namespace"
api_key = "your-api-key-here"
```

If you want to use mTLS authentication instead of an API key, replace the `api_key` field with your mTLS certificate and
private key:

```toml
