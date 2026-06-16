# Last 90 days
postiz analytics:platform your-integration-id -d 90
```

The response is an array of metrics, each with daily data points:

```json theme={null}
[
  {
    "label": "Followers",
    "data": [
      { "total": "1250", "date": "2025-01-01" },
      { "total": "1280", "date": "2025-01-02" }
    ],
    "percentageChange": 2.4
  },
  {
    "label": "Impressions",
    "data": [
      { "total": "5000", "date": "2025-01-01" },
      { "total": "5200", "date": "2025-01-02" }
    ],
    "percentageChange": 4.0
  }
]
```

<Note>
  The metrics returned depend on the platform. For example, X returns followers and impressions, while YouTube may return subscribers and views.
</Note>

## Post Analytics

Get analytics for a specific published post. Returns metrics like likes, comments, shares, and impressions.

```bash theme={null}
postiz analytics:post <post-id>
```

### Options

| Flag         | Description                              |
| ------------ | ---------------------------------------- |
| `-d, --date` | Number of days to look back (default: 7) |

### Examples

```bash theme={null}
