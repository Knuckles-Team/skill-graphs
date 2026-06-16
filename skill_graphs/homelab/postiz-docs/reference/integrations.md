# Integrations
Source: https://docs.postiz.com/cli/integrations

Discover connected accounts, settings schemas, and dynamic tools

## Listing Integrations

List all connected social media accounts to get their IDs:

```bash theme={null}
postiz integrations:list
```

This returns a JSON array of integrations. Use `jq` to extract specific fields:

```bash theme={null}
