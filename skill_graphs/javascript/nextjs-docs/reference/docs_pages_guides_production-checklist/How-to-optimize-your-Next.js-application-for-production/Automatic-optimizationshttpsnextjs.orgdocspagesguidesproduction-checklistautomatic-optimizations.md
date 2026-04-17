## Automatic optimizations[](https://nextjs.org/docs/pages/guides/production-checklist#automatic-optimizations)
These Next.js optimizations are enabled by default and require no configuration:
  * **[Code-splitting](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts):** Next.js automatically code-splits your application code by pages. This means only the code needed for the current page is loaded on navigation. You may also consider [lazy loading](https://nextjs.org/docs/pages/guides/lazy-loading) third-party libraries, where appropriate.
  * **[Prefetching](https://nextjs.org/docs/pages/api-reference/components/link#prefetch):** When a link to a new route enters the user's viewport, Next.js prefetches the route in background. This makes navigation to new routes almost instant. You can opt out of prefetching, where appropriate.
  * **[Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization):** Next.js automatically determines that a page is static (can be pre-rendered) if it has no blocking data requirements. Optimized pages can be cached, and served to the end-user from multiple CDN locations. You may opt into [Server-side Rendering](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props), where appropriate.


These defaults aim to improve your application's performance, and reduce the cost and amount of data transferred on each network request.
