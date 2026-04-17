##  [Usage](https://vercel.com/docs/vercel-blob/usage-and-pricing#usage)[](https://vercel.com/docs/vercel-blob/usage-and-pricing#usage)
Vercel Blob usage is measured based on the following:
  * Storage Size: Monthly average of your blob store size (GB-month)
  * Simple Operations: Counts when a blob is accessed by its URL and it's a cache MISS or when using the [`head()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#head) method
  * Advanced Operations: Counts when using [`put()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#put), [`copy()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#copy), or [`list()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#list) methods
  * Blob Data Transfer: Charged when blobs are downloaded or viewed
  * [Edge Requests](https://vercel.com/docs/pricing/networking#edge-requests): Each blob access by its URL counts as one Edge Request, regardless if it's a MISS or HIT
  * [Fast Origin Transfer](https://vercel.com/docs/pricing/networking#fast-origin-transfer): Applied only for cache MISS scenarios


See the [usage details](https://vercel.com/docs/vercel-blob/usage-and-pricing#usage-details) and [pricing example](https://vercel.com/docs/vercel-blob/usage-and-pricing#pricing-example) sections for more information on how usage is calculated.
Stored files are referred to as "blobs" once they're in the storage system, following cloud storage terminology.
