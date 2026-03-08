##  [Limits and usage](https://vercel.com/docs/routing#limits-and-usage)[](https://vercel.com/docs/routing#limits-and-usage)
Data cache property | Limit
---|---
Item size | 2 MB (items larger won't be cached)
Tags per item | 128 tags
Maximum tag length | 256 bytes
###  [Storage and eviction](https://vercel.com/docs/routing#storage-and-eviction)[](https://vercel.com/docs/routing#storage-and-eviction)
Each project has a fixed storage limit for cached data. When your project reaches this limit, Vercel uses a least recently used (LRU) eviction policy: it removes the entries that haven't been accessed recently first. You can monitor your cache size and eviction activity in the [Runtime Cache section of Observability](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fobservability%2Fruntime-cache&title=Go+to+Observability+Runtime+Cache) section in the sidebar under your project.
###  [How data cache works with other caches](https://vercel.com/docs/routing#how-data-cache-works-with-other-caches)[](https://vercel.com/docs/routing#how-data-cache-works-with-other-caches)
Data cache works alongside [Incremental Static Regeneration](https://vercel.com/docs/incremental-static-regeneration) (ISR) and [CDN Cache](https://vercel.com/docs/cdn-cache):
Scenario | Cache layer
---|---
Entirely static pages | ISR
Pages with mix of static and dynamic data | Data cache + ISR
Data fetched during function execution | Data cache
Complete HTTP responses (images, fonts, etc.) | CDN cache
When a page contains entirely static data, Vercel uses ISR to generate the whole page. When a page contains a mix of static and dynamic data, the dynamic data is re-fetched when rendering the page. Data cache stores the static portion to avoid slow origin fetches.
Both Data cache and ISR support time-based revalidation, on-demand revalidation, and tag-based revalidation.
