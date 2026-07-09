## Travis CI[](https://nextjs.org/docs/pages/guides/ci-build-caching#travis-ci)
Add or merge the following into your `.travis.yml`:
```
cache:
  directories:
    - $HOME/.cache/yarn
    - node_modules
    - .next/cache
```
