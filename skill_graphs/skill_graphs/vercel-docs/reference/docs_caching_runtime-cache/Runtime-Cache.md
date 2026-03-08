# Runtime Cache
Last updated February 9, 2026
Runtime Cache is available on [all plans](https://vercel.com/docs/plans)
Runtime cache is a regional, ephemeral cache you can use for storing and retrieving data across Vercel Functions, Routing middleware, and build execution within a Vercel region. It lets you cache data close to where your code runs, reduce duplicate work, and control invalidation with TTLs and tags.
Runtime cache may not share the same cache between build time and runtime depending on whether the region where the build executed matches the runtime region.
  * Find out [how runtime cache works](https://vercel.com/docs/regions#how-runtime-cache-works)
  * [When to use it](https://vercel.com/docs/regions#when-to-use-runtime-cache)
  * Get started with the [framework-specific examples](https://vercel.com/docs/regions#using-runtime-cache)


For caching complete HTTP responses (entire pages, API responses) in Vercel regions, see [CDN cache](https://vercel.com/docs/cdn-cache). For caching build artifacts, see [Remote cache](https://vercel.com/docs/monorepos/remote-caching).
