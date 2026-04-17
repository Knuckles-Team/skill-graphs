## Caveats[](https://nextjs.org/docs/app/guides/incremental-static-regeneration#caveats)
  * ISR is only supported when using the Node.js runtime (default).
  * ISR is not supported when creating a [Static Export](https://nextjs.org/docs/app/guides/static-exports).
  * If you have multiple `fetch` requests in a statically rendered route, and each has a different `revalidate` frequency, the lowest time will be used for ISR. However, those revalidate frequencies will still be respected by the [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache).
  * If any of the `fetch` requests used on a route have a `revalidate` time of `0`, or an explicit `no-store`, the route will be [dynamically rendered](https://nextjs.org/docs/app/guides/caching#dynamic-rendering).
  * Proxy won't be executed for on-demand ISR requests, meaning any path rewrites or logic in Proxy will not be applied. Ensure you are revalidating the exact path. For example, `/post/1` instead of a rewritten `/post-1`.
