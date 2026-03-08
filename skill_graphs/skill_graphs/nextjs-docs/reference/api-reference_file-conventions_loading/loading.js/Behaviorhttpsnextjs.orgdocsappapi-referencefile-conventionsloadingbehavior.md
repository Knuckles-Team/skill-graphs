## Behavior[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#behavior)
### Navigation[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#navigation)
  * The Fallback UI is [prefetched](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching), making navigation immediate unless prefetching hasn't completed.
  * Navigation is interruptible, meaning changing routes does not need to wait for the content of the route to fully load before navigating to another route.
  * Shared layouts remain interactive while new route segments load.


### Instant Loading States[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#instant-loading-states)
An instant loading state is fallback UI that is shown immediately upon navigation. You can pre-render loading indicators such as skeletons and spinners, or a small but meaningful part of future screens such as a cover photo, title, etc. This helps users understand the app is responding and provides a better user experience.
Create a loading state by adding a `loading.js` file inside a folder.
![loading.js special file](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Floading-special-file.png&w=3840&q=75)![loading.js special file](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Floading-special-file.png&w=3840&q=75)
app/dashboard/loading.tsx
TypeScript
JavaScript TypeScript
```
export default function Loading() {
  // You can add any UI inside Loading, including a Skeleton.
  return <LoadingSkeleton />
}
```

In the same folder, `loading.js` will be nested inside `layout.js`. It will automatically wrap the `page.js` file and any children below in a `<Suspense>` boundary.
![loading.js overview](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Floading-overview.png&w=3840&q=75)![loading.js overview](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Floading-overview.png&w=3840&q=75)
### SEO[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#seo)
  * For bots that only scrape static HTML, and cannot execute JavaScript like a full browser, such as Twitterbot, Next.js resolves [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) before streaming UI, and metadata is placed in the `<head>` of the initial HTML.
  * Otherwise, [streaming metadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#streaming-metadata) may be used. Next.js automatically detects user agents to choose between blocking and streaming behavior.
  * Since streaming is server-rendered, it does not impact SEO. You can use the


### Status Codes[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#status-codes)
When streaming, a `200` status code will be returned to signal that the request was successful.
The server can still communicate errors or issues to the client within the streamed content itself, for example, when using [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect) or [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found). Because the response headers have already been sent to the client, the status code of the response cannot be updated.
For example, when a 404 page is streamed to the client, Next.js includes a `<meta name="robots" content="noindex">` tag in the streamed HTML. This prevents search engines from indexing that URL even if the HTTP status is 200. See Google’s guidance on the
Some crawlers may label these responses as “soft 404s”. In the streaming case, this does not lead to indexation because the page is explicitly marked `noindex` in the HTML.
If you need a 404 status, for compliance or analytics, ensure the resource exists before the response body is streamed, so that the server can set the HTTP status code.
You can run this check in [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) to rewrite missing slugs to a not-found route, or [produce a 404 response](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#producing-a-response). Keep proxy checks fast, and avoid fetching full content there.
When is the response body streamed?
The response body starts streaming when a Suspense fallback renders (for example, a `loading.tsx`) or when a Server Component suspends under a `Suspense` boundary. Place `notFound()` before those boundaries and before any `await` that may suspend.
To start streaming, the response headers must be set. This is why it is not possible to change the status code after streaming started.
### Browser limits[](https://nextjs.org/docs/app/api-reference/file-conventions/loading#browser-limits)
