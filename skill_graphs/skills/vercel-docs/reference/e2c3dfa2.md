##  [Caching](https://vercel.com/docs/vercel-blob#caching)[](https://vercel.com/docs/vercel-blob#caching)
Vercel's [CDN cache](https://vercel.com/docs/cdn-cache) caches all blobs (private and public) for up to 1 month by default. You can customize this duration with the `cacheControlMaxAge` option when uploading.
The difference is in how the cache is reached:
  * Public blobs: The browser hits the CDN cache directly. Both the CDN and browser cache the blob. See [public storage caching](https://vercel.com/docs/vercel-blob/public-storage#caching) for full details.
  * Private blobs: Your [Function](https://vercel.com/docs/functions) fetches the blob through the CDN, then streams the response to the browser. You separately control browser caching through the `Cache-Control` header on your Function's response. See [private storage caching](https://vercel.com/docs/vercel-blob/private-storage#caching) for recommendations.


###  [Important considerations when updating blobs](https://vercel.com/docs/vercel-blob#important-considerations-when-updating-blobs)[](https://vercel.com/docs/vercel-blob#important-considerations-when-updating-blobs)
When you delete or update (overwrite) a blob, the changes may take up to 60 seconds to propagate through our cache. However, browser caching presents additional challenges:
  * While our cache can update to serve the latest content, browsers will continue serving the cached version
  * To force browsers to fetch the updated content, add a unique query parameter to the blob URL:


```
<img
  src="https://1sxstfwepd7zn41q.public.blob.vercel-storage.com/blob-oYnXSVczoLa9yBYMFJOSNdaiiervF5.png?v=123456"
/>
```

For more information about updating existing blobs, see the [overwriting blobs](https://vercel.com/docs/vercel-blob#overwriting-blobs) section.
###  [Best practice: Treat blobs as immutable](https://vercel.com/docs/vercel-blob#best-practice:-treat-blobs-as-immutable)[](https://vercel.com/docs/vercel-blob#best-practice:-treat-blobs-as-immutable)
For optimal performance and to avoid caching issues, consider treating blobs as immutable objects:
  * Instead of updating existing blobs, create new ones with different pathnames (or use `addRandomSuffix: true` option)
  * This approach avoids unexpected behaviors like outdated content appearing in your application


There are still valid use cases for mutable blobs with shorter cache durations, such as a single JSON file that's updated every 5 minutes with a top list of sales or other regularly refreshed data. For these scenarios, set an appropriate `cacheControlMaxAge` value and be mindful of caching behaviors.
