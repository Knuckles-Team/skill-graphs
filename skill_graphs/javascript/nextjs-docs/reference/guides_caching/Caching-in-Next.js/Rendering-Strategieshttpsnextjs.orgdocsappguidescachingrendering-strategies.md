## Rendering Strategies[](https://nextjs.org/docs/app/guides/caching#rendering-strategies)
To understand how caching works in Next.js, it's helpful to understand the rendering strategies available. The rendering strategy determines when your route's HTML is generated, which directly impacts what can be cached.
### Static Rendering[](https://nextjs.org/docs/app/guides/caching#static-rendering)
With Static Rendering, routes are rendered at **build time** or in the background after [data revalidation](https://nextjs.org/docs/app/guides/incremental-static-regeneration). The result is cached and can be reused across requests. Static routes are fully cached in the [Full Route Cache](https://nextjs.org/docs/app/guides/caching#full-route-cache).
### Dynamic Rendering[](https://nextjs.org/docs/app/guides/caching#dynamic-rendering)
With Dynamic Rendering, routes are rendered at **request time**. This happens when your route uses request-specific information like cookies, headers, or search params.
A route becomes dynamic when it uses any of these APIs:
  * [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection)
  * [`draftMode`](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
  * [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional)
  * [`unstable_noStore`](https://nextjs.org/docs/app/api-reference/functions/unstable_noStore)
  * [`fetch`](https://nextjs.org/docs/app/api-reference/functions/fetch) with `{ cache: 'no-store' }`


Dynamic routes are not cached in the Full Route Cache, but can still use the [Data Cache](https://nextjs.org/docs/app/guides/caching#data-cache) for data requests.
> **Good to know** : You can use [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components) to mix static and dynamic rendering within the same route.
