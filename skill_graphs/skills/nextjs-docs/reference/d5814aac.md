## Data Cache[](https://nextjs.org/docs/app/guides/caching#data-cache)
Next.js has a built-in Data Cache that **persists** the result of data fetches across incoming **server requests** and **deployments**. This is possible because Next.js extends the native `fetch` API to allow each request on the server to set its own persistent caching semantics.
> **Good to know** : In the browser, the `cache` option of `fetch` indicates how a request will interact with the browser's HTTP cache, in Next.js, the `cache` option indicates how a server-side request will interact with the server's Data Cache.
You can use the [`cache`](https://nextjs.org/docs/app/guides/caching#fetch-optionscache) and [`next.revalidate`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnextrevalidate) options of `fetch` to configure the caching behavior.
In development mode, `fetch` data is [reused for Hot Module Replacement (HMR)](https://nextjs.org/docs/app/api-reference/functions/fetch#fetch-default-auto-no-store-and-cache-no-store-not-showing-fresh-data-in-development), and caching options are ignored for [hard refreshes](https://nextjs.org/docs/app/api-reference/functions/fetch#hard-refresh-and-caching-in-development).
**How the Data Cache Works**
![Diagram showing how cached and uncached fetch requests interact with the Data Cache. Cached requests are stored in the Data Cache, and memoized, uncached requests are fetched from the data source, not stored in the Data Cache, and memoized.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fdata-cache.png&w=3840&q=75)![Diagram showing how cached and uncached fetch requests interact with the Data Cache. Cached requests are stored in the Data Cache, and memoized, uncached requests are fetched from the data source, not stored in the Data Cache, and memoized.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fdata-cache.png&w=3840&q=75)
  * The first time a `fetch` request with the `'force-cache'` option is called during rendering, Next.js checks the Data Cache for a cached response.
  * If a cached response is found, it's returned immediately and [memoized](https://nextjs.org/docs/app/guides/caching#request-memoization).
  * If a cached response is not found, the request is made to the data source, the result is stored in the Data Cache, and memoized.
  * For uncached data (e.g. no `cache` option defined or using `{ cache: 'no-store' }`), the result is always fetched from the data source, and memoized.
  * Whether the data is cached or uncached, the requests are always memoized to avoid making duplicate requests for the same data during a React render pass.


> **Differences between the Data Cache and Request Memoization**
> While both caching mechanisms help improve performance by reusing cached data, the Data Cache is persistent across incoming requests and deployments, whereas memoization only lasts the lifetime of a request.
### Duration[](https://nextjs.org/docs/app/guides/caching#duration-1)
The Data Cache is persistent across incoming requests and deployments unless you revalidate or opt-out.
### Revalidating[](https://nextjs.org/docs/app/guides/caching#revalidating-1)
Cached data can be revalidated in two ways, with:
  * **Time-based Revalidation** : Revalidate data after a certain amount of time has passed and a new request is made. This is useful for data that changes infrequently and freshness is not as critical.
  * **On-demand Revalidation:** Revalidate data based on an event (e.g. form submission). On-demand revalidation can use a tag-based or path-based approach to revalidate groups of data at once. This is useful when you want to ensure the latest data is shown as soon as possible (e.g. when content from your headless CMS is updated).


#### Time-based Revalidation[](https://nextjs.org/docs/app/guides/caching#time-based-revalidation)
To revalidate data at a timed interval, you can use the `next.revalidate` option of `fetch` to set the cache lifetime of a resource (in seconds).
```
// Revalidate at most every hour
fetch('https://...', { next: { revalidate: 3600 } })
```

Alternatively, you can use [Route Segment Config options](https://nextjs.org/docs/app/guides/caching#segment-config-options) to configure all `fetch` requests in a segment or for cases where you're not able to use `fetch`.
**How Time-based Revalidation Works**
![Diagram showing how time-based revalidation works, after the revalidation period, stale data is returned for the first request, then data is revalidated.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ftime-based-revalidation.png&w=3840&q=75)![Diagram showing how time-based revalidation works, after the revalidation period, stale data is returned for the first request, then data is revalidated.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ftime-based-revalidation.png&w=3840&q=75)
  * The first time a fetch request with `revalidate` is called, the data will be fetched from the external data source and stored in the Data Cache.
  * Any requests that are called within the specified timeframe (e.g. 60-seconds) will return the cached data.
  * After the timeframe, the next request will still return the cached (now stale) data.
    * Next.js will trigger a revalidation of the data in the background.
    * Once the data is fetched successfully, Next.js will update the Data Cache with the fresh data.
    * If the background revalidation fails, the previous data will be kept unaltered.


This is similar to
#### On-demand Revalidation[](https://nextjs.org/docs/app/guides/caching#on-demand-revalidation)
Data can be revalidated on-demand by path ([`revalidatePath`](https://nextjs.org/docs/app/guides/caching#revalidatepath)) or by cache tag ([`revalidateTag`](https://nextjs.org/docs/app/guides/caching#fetch-optionsnexttags-and-revalidatetag)).
**How On-Demand Revalidation Works**
![Diagram showing how on-demand revalidation works, the Data Cache is updated with fresh data after a revalidation request.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fon-demand-revalidation.png&w=3840&q=75)![Diagram showing how on-demand revalidation works, the Data Cache is updated with fresh data after a revalidation request.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fon-demand-revalidation.png&w=3840&q=75)
  * The first time a `fetch` request is called, the data will be fetched from the external data source and stored in the Data Cache.
  * When an on-demand revalidation is triggered, the appropriate cache entries will be purged from the cache.
    * This is different from time-based revalidation, which keeps the stale data in the cache until the fresh data is fetched.
  * The next time a request is made, it will be a cache `MISS` again, and the data will be fetched from the external data source and stored in the Data Cache.


### Opting out[](https://nextjs.org/docs/app/guides/caching#opting-out-1)
If you do _not_ want to cache the response from `fetch`, you can do the following:
```
let data = await fetch('https://api.vercel.app/blog', { cache: 'no-store' })
```
