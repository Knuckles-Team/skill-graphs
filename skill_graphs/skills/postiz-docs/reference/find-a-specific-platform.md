# Find a specific platform
postiz integrations:list | jq '.[] | select(.identifier=="reddit")'
```

### Filtering by Group

If your channels are organized into groups (customers), filter the list to a single group with `--group`:

```bash theme={null}
postiz integrations:list --group "customer-id"
```

## Listing Groups

List all groups (customers) for your organization to get their IDs:

```bash theme={null}
postiz integrations:groups
```

This returns a JSON array of `{id, name}` objects. Use a group's `id` with `integrations:list --group` to filter channels:

```bash theme={null}
