# Change Post Status
Source: https://docs.postiz.com/public-api/posts/change-status

PUT /posts/{id}/status
Moves a post between `draft` and `schedule` state.

- `schedule` → sets the post state to `QUEUE` and (re)starts the publishing workflow so it will be published at its stored date.
- `draft` → sets the post state to `DRAFT` and terminates any currently running publishing workflow for the post, so it will not be published.

The post keeps its stored date; only the state (and the workflow) changes.
