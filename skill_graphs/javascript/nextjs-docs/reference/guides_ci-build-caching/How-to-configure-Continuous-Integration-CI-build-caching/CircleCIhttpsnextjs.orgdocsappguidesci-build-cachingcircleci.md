## CircleCI[](https://nextjs.org/docs/app/guides/ci-build-caching#circleci)
Edit your `save_cache` step in `.circleci/config.yml` to include `.next/cache`:
```
steps:
  - save_cache:
      key: dependency-cache-{{ checksum "yarn.lock" }}
      paths:
        - ./node_modules
        - ./.next/cache
```

If you do not have a `save_cache` key, please follow CircleCI's
