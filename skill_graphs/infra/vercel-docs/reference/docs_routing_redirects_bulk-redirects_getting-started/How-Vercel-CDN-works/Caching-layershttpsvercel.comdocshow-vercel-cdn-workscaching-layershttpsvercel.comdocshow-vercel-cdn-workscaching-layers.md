##  [Caching layers](https://vercel.com/docs/how-vercel-cdn-works#caching-layers)[](https://vercel.com/docs/how-vercel-cdn-works#caching-layers)
Vercel maintains two tiers of caching. Together, they minimize how often your functions run:
  * [CDN cache](https://vercel.com/docs/caching/cdn-cache): It stores responses at the nearest PoP, closest to your visitors and is controlled by [`Cache-Control` headers](https://vercel.com/docs/caching/cache-control-headers) your functions return. A CDN hit serves the response without reaching your origin.
  * [ISR cache](https://vercel.com/docs/incremental-static-regeneration): A durable store in your configured [function region](https://vercel.com/docs/functions/configuring-functions/region): Vercel selects one region if you have multiple regions configured. It persists content for up to 31 days. When the CDN misses but the ISR cache has the content, Vercel serves it without invoking your function.
    * [Request collapsing](https://vercel.com/docs/incremental-static-regeneration/request-collapsing) further protects this layer by deduplicating concurrent requests to the same ISR path into a single function invocation.


For data fetched inside your functions (individual API calls, database queries), [runtime cache](https://vercel.com/docs/caching/runtime-cache) provides an additional caching layer that works alongside response caching.
