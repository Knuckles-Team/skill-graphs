##  [Caching data](https://vercel.com/docs/functions/runtimes#caching-data)[](https://vercel.com/docs/functions/runtimes#caching-data)
A runtime can retain an archive of up to 100 MB of the filesystem at build time. The cache key is generated as a combination of:
  * Project name
  * [Team ID](https://vercel.com/docs/accounts#find-your-team-id) or User ID
  * Entrypoint path (e.g., `api/users/index.go`)
  * Runtime identifier including version (e.g.: `@vercel/go@0.0.1`)


The cache will be invalidated if any of those items changes. You can bypass the cache by running `vercel -f`.
