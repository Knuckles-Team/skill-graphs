##  [Caching](https://vercel.com/docs/vercel-blob/public-storage#caching)[](https://vercel.com/docs/vercel-blob/public-storage#caching)
When you request a public blob URL, the content is cached in two places:
  1. Vercel's [CDN cache](https://vercel.com/docs/cdn-cache)
  2. Your browser's cache


Both caches store blobs for up to 1 month by default to ensure optimal performance when serving content. While both systems aim to respect this duration, blobs may occasionally expire earlier.
Vercel will cache blobs up to [512 MB](https://vercel.com/docs/vercel-blob/usage-and-pricing#size-limits). Bigger blobs will always be served from the origin (your store).
###  [Configuring cache duration](https://vercel.com/docs/vercel-blob/public-storage#configuring-cache-duration)[](https://vercel.com/docs/vercel-blob/public-storage#configuring-cache-duration)
You can customize the caching duration using the [`cacheControlMaxAge`](https://vercel.com/docs/vercel-blob/using-blob-sdk#put) option in the [`put()`](https://vercel.com/docs/storage/vercel-blob/using-blob-sdk#put) and [`handleUpload`](https://vercel.com/docs/storage/vercel-blob/using-blob-sdk#handleupload) methods.
The minimum configurable value is 60 seconds (1 minute). This represents the maximum time needed for our cache to update content behind a blob URL. For applications requiring faster updates, consider using a [Vercel function](https://vercel.com/docs/functions) instead.
See [caching best practices](https://vercel.com/docs/vercel-blob#caching) on the overview page for guidance on updating and overwriting blobs.
###  [Browser caching with conditional requests](https://vercel.com/docs/vercel-blob/public-storage#browser-caching-with-conditional-requests)[](https://vercel.com/docs/vercel-blob/public-storage#browser-caching-with-conditional-requests)
When a browser requests a public blob URL, the CDN automatically includes an `ETag` header in the response. On subsequent requests, the browser sends an `If-None-Match` header with the cached ETag. If the blob hasn't changed, the CDN responds with `304 Not Modified` and the browser uses its cached copy, avoiding a full re-download.
This works automatically for public blobs accessed by URL. You don't need to write any code to benefit from conditional requests.
If you're using [`get()`](https://vercel.com/docs/vercel-blob/using-blob-sdk#get) to process public blobs server-side, you can also pass the `ifNoneMatch` option to avoid re-downloading unchanged blobs:
```
import { get } from '@vercel/blob';

const result = await get('images/hero.png', {
  access: 'public',
  ifNoneMatch: previousEtag,
});

if (result.statusCode === 304) {
  // Blob hasn't changed, use the version you already have
}
```
