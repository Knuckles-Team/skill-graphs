##  [Advanced operations](https://vercel.com/docs/vercel-blob#advanced-operations)[](https://vercel.com/docs/vercel-blob#advanced-operations)
Advanced operations in Vercel Blob are write, copy, and listing actions counted for billing purposes:
  * When the [`put()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#put) method is called to upload a blob
  * When the [`upload()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#upload) method is used for client-side uploads
  * When the [`copy()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#copy) method is called to copy an existing blob
  * When the [`list()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#list) method is called to list blobs in your store


###  [Dashboard usage counts as operations](https://vercel.com/docs/vercel-blob#dashboard-usage-counts-as-operations)[](https://vercel.com/docs/vercel-blob#dashboard-usage-counts-as-operations)
Using the Vercel Blob file browser in your dashboard will count as operations. Each time you refresh the blob list, upload files through the dashboard, or view blob details, these actions use the same API methods that count toward your usage limits and billing.
Common dashboard actions that count as operations:
  * Refreshing the file browser: Uses `list()` to display your blobs
  * Uploading files via dashboard: Uses `put()` for each file uploaded
  * Viewing blob details: May trigger additional API calls
  * Navigating folders: Uses `list()` with different prefixes


If you notice unexpected increases in your operations count, check whether team members are browsing your blob store through the Vercel dashboard.
For [multipart uploads](https://vercel.com/docs/vercel-blob#multipart-uploads), multiple advanced operations are counted:
  * One operation when starting the upload
  * One operation for each part uploaded
  * One operation for completing the upload


Delete operations using the [`del()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#del) are free of charge. They are considered advanced operations for [operation rate limits](https://vercel.com/docs/vercel-blob/usage-and-pricing#operation-rate-limits) but not for billing.
