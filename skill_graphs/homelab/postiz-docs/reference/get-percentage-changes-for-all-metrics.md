# Get percentage changes for all metrics
postiz analytics:platform integration-id | jq '.[] | {label, percentageChange}'
