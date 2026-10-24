##  [Limits](https://vercel.com/docs/vercel-blob/usage-and-pricing#limits)[](https://vercel.com/docs/vercel-blob/usage-and-pricing#limits)
Vercel Blob has certain [limits](https://vercel.com/docs/limits) that you should be aware of when designing your application.
###  [Operation rate limits](https://vercel.com/docs/vercel-blob/usage-and-pricing#operation-rate-limits)[](https://vercel.com/docs/vercel-blob/usage-and-pricing#operation-rate-limits)
Plan | Simple Operations | Advanced Operations
---|---|---
Hobby | 1,200/min (20/s) | 900/min (15/s)
Pro | 7,200/min (120/s) | 4,500/min (75/s)
Enterprise | 9,000/min (150/s) | 7,500/min (125/s)
Note: Rate limits are based on the number of operations, not HTTP requests. For example, when using `del([pathnames])` to delete multiple blobs in one call, each blob deletion counts as a separate operation toward your rate limit. Deleting 100 blobs in a batch counts as 100 operations, not one.
###  [Size limits](https://vercel.com/docs/vercel-blob/usage-and-pricing#size-limits)[](https://vercel.com/docs/vercel-blob/usage-and-pricing#size-limits)
  * Cache Size Limit: 512 MB per blob
    * Blobs larger than 512 MB will not be cached
    * Accessing these blobs will always count as a cache MISS (generating one [Simple Operation](https://vercel.com/docs/vercel-blob#simple-operations))
    * These large blobs will also incur [Fast Origin Transfer](https://vercel.com/docs/manage-cdn-usage#fast-origin-transfer) charges for each access
  * Maximum File Size: 5TB (5,000GB)
    * This is the absolute maximum size for any individual file uploaded to Vercel Blob
    * For files larger than 100MB, we recommend using [multipart uploads](https://vercel.com/docs/vercel-blob#multipart-uploads)
