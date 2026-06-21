## Prefetching static vs. dynamic routes[](https://nextjs.org/docs/app/guides/prefetching#prefetching-static-vs-dynamic-routes)
| **Static page** | **Dynamic page**
---|---|---
**Prefetched** | Yes, full route | No, unless [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading)
[**Client Cache TTL**](https://nextjs.org/docs/app/guides/caching#full-route-cache) | 5 min (default) | Off, unless [enabled](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes)
**Server roundtrip on click** | No | Yes, streamed after [shell](https://nextjs.org/docs/app/getting-started/cache-components)
> **Good to know:** During the initial navigation, the browser fetches the HTML, JavaScript, and React Server Components (RSC) Payload. For subsequent navigations, the browser will fetch the RSC Payload for Server Components and JS bundle for Client Components.
