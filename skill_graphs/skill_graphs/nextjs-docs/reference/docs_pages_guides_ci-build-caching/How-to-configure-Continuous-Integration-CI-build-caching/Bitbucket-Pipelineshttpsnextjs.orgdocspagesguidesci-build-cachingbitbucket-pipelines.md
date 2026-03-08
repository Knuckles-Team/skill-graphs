## Bitbucket Pipelines[](https://nextjs.org/docs/pages/guides/ci-build-caching#bitbucket-pipelines)
Add or merge the following into your `bitbucket-pipelines.yml` at the top level (same level as `pipelines`):
```
definitions:
  caches:
    nextcache: .next/cache
```

Then reference it in the `caches` section of your pipeline's `step`:
```
- step:
    name: your_step_name
    caches:
      - node
      - nextcache
```
