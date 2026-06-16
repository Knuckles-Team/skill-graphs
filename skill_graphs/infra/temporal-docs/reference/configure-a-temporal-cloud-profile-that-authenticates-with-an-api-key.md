# Configure a Temporal Cloud profile that authenticates with an API key
temporal --profile prod config set --prop address --value "<region>.<cloud_provider>.api.temporal.io:7233"
temporal --profile prod config set --prop namespace --value "<namespace_id>.<account_id>"
temporal --profile prod config set --prop api_key --value "<your-api-key>"
```

  </TabItem>
  <TabItem value="api-key-advanced" label="API key + advanced options">

This example shows how to set up a more advanced Temporal Cloud profile with TLS overrides and custom gRPC metadata.

```bash
