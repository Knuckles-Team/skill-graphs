## Troubleshooting[](https://nextjs.org/docs/app/api-reference/functions/fetch#troubleshooting)
### Fetch default `auto no store` and `cache: 'no-store'` not showing fresh data in development[](https://nextjs.org/docs/app/api-reference/functions/fetch#fetch-default-auto-no-store-and-cache-no-store-not-showing-fresh-data-in-development)
Next.js caches `fetch` responses in Server Components across Hot Module Replacement (HMR) in local development for faster responses and to reduce costs for billed API calls.
By default, the [HMR cache](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache) applies to all fetch requests, including those with the default `auto no cache` and `cache: 'no-store'` option. This means uncached requests will not show fresh data between HMR refreshes. However, the cache will be cleared on navigation or full-page reloads.
See the [`serverComponentsHmrCache`](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache) docs for more information.
### Hard refresh and caching in development[](https://nextjs.org/docs/app/api-reference/functions/fetch#hard-refresh-and-caching-in-development)
In development mode, if the request includes the `cache-control: no-cache` header, `options.cache`, `options.next.revalidate`, and `options.next.tags` are ignored, and the `fetch` request is served from the source.
Browsers typically include `cache-control: no-cache` when the cache is disabled in developer tools or during a hard refresh.
