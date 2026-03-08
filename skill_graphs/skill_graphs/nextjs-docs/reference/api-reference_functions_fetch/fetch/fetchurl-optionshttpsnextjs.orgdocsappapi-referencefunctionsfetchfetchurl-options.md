##  `fetch(url, options)`[](https://nextjs.org/docs/app/api-reference/functions/fetch#fetchurl-options)
Since Next.js extends the
###  `options.cache`[](https://nextjs.org/docs/app/api-reference/functions/fetch#optionscache)
Configure how the request should interact with Next.js [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache).
```
fetch(`https://...`, { cache: 'force-cache' | 'no-store' })
```

  * **`auto no cache`**(default): Next.js fetches the resource from the remote server on every request in development, but will fetch once during`next build` because the route will be statically prerendered. If [Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) are detected on the route, Next.js will fetch the resource on every request.
  * **`no-store`**: Next.js fetches the resource from the remote server on every request, even if Dynamic APIs are not detected on the route.
  * **`force-cache`**: Next.js looks for a matching request in its Data Cache.
    * If there is a match and it is fresh, it will be returned from the cache.
    * If there is no match or a stale match, Next.js will fetch the resource from the remote server and update the cache with the downloaded resource.


###  `options.next.revalidate`[](https://nextjs.org/docs/app/api-reference/functions/fetch#optionsnextrevalidate)
```
fetch(`https://...`, { next: { revalidate: false | 0 | number } })
```

Set the cache lifetime of a resource (in seconds). [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache).
  * **`false`**- Cache the resource indefinitely. Semantically equivalent to`revalidate: Infinity`. The HTTP cache may evict older resources over time.
  * **`0`**- Prevent the resource from being cached.
  * **`number`**- (in seconds) Specify the resource should have a cache lifetime of at most`n` seconds.


> **Good to know** :
>   * If an individual `fetch()` request sets a `revalidate` number lower than the [default `revalidate`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#revalidate) of a route, the whole route revalidation interval will be decreased.
>   * If two fetch requests with the same URL in the same route have different `revalidate` values, the lower value will be used.
>   * Conflicting options such as `{ revalidate: 3600, cache: 'no-store' }` are not allowed, both will be ignored, and in development mode a warning will be printed to the terminal.
>

###  `options.next.tags`[](https://nextjs.org/docs/app/api-reference/functions/fetch#optionsnexttags)
```
fetch(`https://...`, { next: { tags: ['collection'] } })
```

Set the cache tags of a resource. Data can then be revalidated on-demand using [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag). The max length for a custom tag is 256 characters and the max tag items is 128.
