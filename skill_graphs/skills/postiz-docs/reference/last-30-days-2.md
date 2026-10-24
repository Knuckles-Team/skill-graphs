# Last 30 days
postiz analytics:post your-post-id -d 30
```

The response follows the same format as platform analytics:

```json theme={null}
[
  {
    "label": "Likes",
    "data": [
      { "total": "150", "date": "2025-01-01" },
      { "total": "175", "date": "2025-01-02" }
    ],
    "percentageChange": 16.7
  },
  {
    "label": "Comments",
    "data": [
      { "total": "25", "date": "2025-01-01" },
      { "total": "30", "date": "2025-01-02" }
    ],
    "percentageChange": 20.0
  }
]
```

<Tip>
  Post analytics are only available for published posts. Draft or queued posts won't return analytics data.
</Tip>

## Scripting with Analytics

Extract specific metrics using `jq`:

```bash theme={null}
