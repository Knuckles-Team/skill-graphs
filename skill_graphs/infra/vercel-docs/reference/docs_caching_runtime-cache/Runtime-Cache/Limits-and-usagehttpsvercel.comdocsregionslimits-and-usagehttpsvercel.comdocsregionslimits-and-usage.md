##  [Limits and usage](https://vercel.com/docs/regions#limits-and-usage)[](https://vercel.com/docs/regions#limits-and-usage)
Runtime Cache property | Limit
---|---
Item size | 2 MB
Tags per item | 64 tags
Maximum tag length | 256 bytes
TTL and tag updates aren't reconciled between deployments. If you need to update cache behavior after a deployment, purge the runtime cache or modify the cache key.
Runtime cache operates independently from [Incremental Static Regeneration](https://vercel.com/docs/incremental-static-regeneration). If you use both caching layers, manage them separately using their respective invalidation methods or use the same cache tag for both to manage them together.
###  [Storage and eviction](https://vercel.com/docs/regions#storage-and-eviction)[](https://vercel.com/docs/regions#storage-and-eviction)
Each project has a fixed storage limit. When your project reaches this limit, Vercel uses a least recently used (LRU) eviction policy: it removes the entries that haven't been accessed recently first. You can monitor your cache size and eviction activity in the [Runtime Cache](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability%2Fruntime-cache&title=Go+to+Runtime+cache+Observability) section of the Observability tab.
Usage of runtime cache is charged. Learn more about [pricing](https://vercel.com/docs/pricing/regional-pricing).
* * *
[ Previous How Vercel CDN works ](https://vercel.com/docs/how-vercel-cdn-works)[ Next Routing ](https://vercel.com/docs/routing)
Was this helpful?
Send
On this page
  * [When to use runtime cache](https://vercel.com/docs/regions#when-to-use-runtime-cache)
  * [How runtime cache works](https://vercel.com/docs/regions#how-runtime-cache-works)
  * [Using runtime cache](https://vercel.com/docs/regions#using-runtime-cache)
  * [Runtime cache with any framework](https://vercel.com/docs/regions#runtime-cache-with-any-framework)
  * [Runtime cache with Next.js](https://vercel.com/docs/regions#runtime-cache-with-next.js)
  * [Next.js 16 and above](https://vercel.com/docs/regions#next.js-16-and-above)
  * [Using use cache: remote](https://vercel.com/docs/regions#using-use-cache:-remote)
  * [Using fetch with force-cache](https://vercel.com/docs/regions#using-fetch-with-force-cache)
  * [Next.js 15](https://vercel.com/docs/regions#next.js-15)
  * [Using fetch with cache options](https://vercel.com/docs/regions#using-fetch-with-cache-options)
  * [Using unstable_cache](https://vercel.com/docs/regions#using-unstable_cache)
  * [Next.js 14 and below](https://vercel.com/docs/regions#next.js-14-and-below)
  * [Revalidation](https://vercel.com/docs/regions#revalidation)
  * [Time-based revalidation](https://vercel.com/docs/regions#time-based-revalidation)
  * [Tag-based revalidation](https://vercel.com/docs/regions#tag-based-revalidation)
  * [Path-based revalidation](https://vercel.com/docs/regions#path-based-revalidation)
  * [Working with CDN cache](https://vercel.com/docs/regions#working-with-cdn-cache)
  * [Observability](https://vercel.com/docs/regions#observability)
  * [Limits and usage](https://vercel.com/docs/regions#limits-and-usage)
  * [Storage and eviction](https://vercel.com/docs/regions#storage-and-eviction)


Copy as MarkdownGive feedbackAsk AI about this page
