# Get the latest total for each post metric
postiz analytics:post post-id | jq '.[] | {label, latest: .data[-1].total}'
```
