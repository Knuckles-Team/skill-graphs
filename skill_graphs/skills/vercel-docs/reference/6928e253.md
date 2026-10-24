##  [Optimizing ISR reads and writes](https://vercel.com/docs/how-vercel-cdn-works#optimizing-isr-reads-and-writes)[](https://vercel.com/docs/how-vercel-cdn-works#optimizing-isr-reads-and-writes)
You're charged based on the volume of data read from and written to the ISR cache, and the regions where reads and writes occur. To optimize ISR usage, consider the following strategies:
  * For content that rarely changes, set a longer [time-based revalidation](https://vercel.com/docs/incremental-static-regeneration/quickstart#time-based-revalidation) interval
  * If you have events that trigger data updates, use [on-demand revalidation](https://vercel.com/docs/incremental-static-regeneration/quickstart#on-demand-revalidation) instead of short revalidation intervals


When revalidation runs and the content hasn't changed from the previous version, no ISR write units are incurred. This applies to both time-based and on-demand revalidation.
Vercel's region-aware ISR architecture helps reduce ISR spend by keeping the durable cache close to your function and serving subsequent requests from CDN caches.
If you're seeing unexpected writes, the content has changed between revalidations. To debug:
  * Check that you're not using `new Date()` in the ISR output
  * Check that you're not using `Math.random()` in the ISR output
  * Check that no other non-deterministic code is included in the ISR output
