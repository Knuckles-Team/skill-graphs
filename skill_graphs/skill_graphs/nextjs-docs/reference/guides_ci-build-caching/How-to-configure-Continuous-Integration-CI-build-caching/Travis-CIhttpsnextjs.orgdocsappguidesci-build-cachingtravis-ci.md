## Travis CI[](https://nextjs.org/docs/app/guides/ci-build-caching#travis-ci)
Add or merge the following into your `.travis.yml`:
```
cache:
  directories:
    - $HOME/.cache/yarn
    - node_modules
    - .next/cache
```
