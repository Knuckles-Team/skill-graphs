# Analytics
Source: https://docs.postiz.com/cli/analytics

View platform and post-level analytics from the command line

## Platform Analytics

Get analytics for a specific integration/channel. Returns metrics like followers, impressions, and engagement over time.

```bash theme={null}
postiz analytics:platform <integration-id>
```

### Options

| Flag         | Description                              |
| ------------ | ---------------------------------------- |
| `-d, --date` | Number of days to look back (default: 7) |

### Examples

```bash theme={null}
