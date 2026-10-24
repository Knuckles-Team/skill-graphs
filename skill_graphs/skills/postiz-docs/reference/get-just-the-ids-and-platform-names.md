# Get just the IDs and platform names
postiz integrations:list | jq '.[] | {id, identifier}'
```

```bash theme={null}
