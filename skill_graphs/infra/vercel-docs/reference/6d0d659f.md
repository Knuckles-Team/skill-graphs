##  [Usage details](https://vercel.com/docs/vercel-blob/usage-and-pricing#usage-details)[](https://vercel.com/docs/vercel-blob/usage-and-pricing#usage-details)
  * Cache HITs do not count as Simple Operations
  * Cache HITs do not incur Fast Origin Transfer charges
  * The maximum size of a blob in cache is [512 MB](https://vercel.com/usage-and-pricing#size-limits). Any blob larger than this will generate a cache MISS on every access, resulting in a Fast Origin Transfer and Edge Request charge each time it is accessed
  * Uploads do not incur data transfer charges when using [Client Uploads](https://vercel.com/docs/vercel-blob/client-upload)
  * Uploads incur [Fast Data Transfer](https://vercel.com/docs/manage-cdn-usage#fast-data-transfer) charges when using [Server Uploads](https://vercel.com/docs/vercel-blob/server-upload) if your Vercel application is the one receiving the file upload
  * [Multipart uploads](https://vercel.com/docs/vercel-blob/using-blob-sdk#multipart-uploads) count as multiple Advanced Operations: one when starting, one per part, one for completion
  * [`del()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#del) operations are free
  * Dashboard interactions count as operations: Each time you interact with the Vercel dashboard to browse your blob store, upload files, or view blob details, these actions count as Advanced Operations and will appear in your usage metrics.
