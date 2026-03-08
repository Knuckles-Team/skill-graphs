## GitLab CI[](https://nextjs.org/docs/app/guides/ci-build-caching#gitlab-ci)
Add or merge the following into your `.gitlab-ci.yml`:
```
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .next/cache/
```
