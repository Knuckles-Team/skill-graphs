## Request Memoization[](https://nextjs.org/docs/app/guides/caching#request-memoization)
Next.js extends the [`fetch` API](https://nextjs.org/docs/app/guides/caching#fetch) to automatically **memoize** requests that have the same URL and options. This means you can call a fetch function for the same data in multiple places in a React component tree while only executing it once.
![Deduplicated Fetch Requests](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fdeduplicated-fetch-requests.png&w=3840&q=75)![Deduplicated Fetch Requests](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fdeduplicated-fetch-requests.png&w=3840&q=75)
For example, if you need to use the same data across a route (e.g. in a Layout, Page, and multiple components), you do not have to fetch data at the top of the tree, and forward props between components. Instead, you can fetch data in the components that need it without worrying about the performance implications of making multiple requests across the network for the same data.
app/example.tsx
TypeScript
JavaScript TypeScript
```
async function getItem() {
  // The `fetch` function is automatically memoized and the result
  // is cached
  const res = await fetch('https://.../item/1')
  return res.json()
}

// This function is called twice, but only executed the first time
const item = await getItem() // cache MISS

// The second call could be anywhere in your route
const item = await getItem() // cache HIT
```

**How Request Memoization Works**
![Diagram showing how fetch memoization works during React rendering.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Frequest-memoization.png&w=3840&q=75)![Diagram showing how fetch memoization works during React rendering.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Frequest-memoization.png&w=3840&q=75)
  * While rendering a route, the first time a particular request is called, its result will not be in memory and it'll be a cache `MISS`.
  * Therefore, the function will be executed, and the data will be fetched from the external source, and the result will be stored in memory.
  * Subsequent function calls of the request in the same render pass will be a cache `HIT`, and the data will be returned from memory without executing the function.
  * Once the route has been rendered and the rendering pass is complete, memory is "reset" and all request memoization entries are cleared.


> **Good to know** :
>   * Request memoization is a React feature, not a Next.js feature. It's included here to show how it interacts with the other caching mechanisms.
>   * Memoization only applies to the `GET` method in `fetch` requests.
>   * Memoization only applies to the React Component tree, this means:
>     * It applies to `fetch` requests in `generateMetadata`, `generateStaticParams`, Layouts, Pages, and other Server Components.
>     * It doesn't apply to `fetch` requests in Route Handlers as they are not a part of the React component tree.
>   * For cases where `fetch` is not suitable (e.g. some database clients, CMS clients, or GraphQL clients), you can use the [React `cache` function](https://nextjs.org/docs/app/guides/caching#react-cache-function) to memoize functions.
>

### Duration[](https://nextjs.org/docs/app/guides/caching#duration)
The cache lasts the lifetime of a server request until the React component tree has finished rendering.
### Revalidating[](https://nextjs.org/docs/app/guides/caching#revalidating)
Since the memoization is not shared across server requests and only applies during rendering, there is no need to revalidate it.
### Opting out[](https://nextjs.org/docs/app/guides/caching#opting-out)
Memoization only applies to the `GET` method in `fetch` requests, other methods, such as `POST` and `DELETE`, are not memoized. This default behavior is a React optimization and we do not recommend opting out of it.
To manage individual requests, you can use the
app/example.js
```
const { signal } = new AbortController()
fetch(url, { signal })
```
