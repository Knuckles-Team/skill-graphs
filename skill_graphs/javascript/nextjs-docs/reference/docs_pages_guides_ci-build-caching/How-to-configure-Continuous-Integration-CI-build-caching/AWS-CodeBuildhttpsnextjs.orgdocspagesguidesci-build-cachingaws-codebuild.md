## AWS CodeBuild[](https://nextjs.org/docs/pages/guides/ci-build-caching#aws-codebuild)
Add (or merge in) the following to your `buildspec.yml`:
```
cache:
  paths:
    - 'node_modules/**/*' # Cache `node_modules` for faster `yarn` or `npm i`
    - '.next/cache/**/*' # Cache Next.js for faster application rebuilds
```
