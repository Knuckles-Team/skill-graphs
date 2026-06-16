# Get just the follower count trend
postiz analytics:platform integration-id -d 30 | jq '.[] | select(.label=="Followers")'
