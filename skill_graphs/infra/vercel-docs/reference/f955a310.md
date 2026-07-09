##  [Simple operations](https://vercel.com/docs/vercel-blob#simple-operations)[](https://vercel.com/docs/vercel-blob#simple-operations)
Simple operations in Vercel Blob are specific read actions counted for billing purposes:
  * When the [`head()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#head) method is called to retrieve blob metadata
  * When a blob is accessed by its URL and it's a cache MISS


A cache MISS occurs when the blob is accessed for the first time or when its previously cached version has expired. Note that blob URL access resulting in a cache HIT does not count as a Simple Operation.
