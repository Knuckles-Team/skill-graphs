## Enhanced Routing and Navigation[](https://nextjs.org/docs/app/guides/upgrading/version-16#enhanced-routing-and-navigation)
**Next.js 16** includes a complete overhaul of the routing and navigation system, making page transitions leaner and faster. This optimizes how Next.js prefetches and caches navigation data:
  * **Layout deduplication** : When prefetching multiple URLs with a shared layout, the layout is downloaded once.
  * **Incremental prefetching** : Next.js only prefetches parts not already in cache, rather than entire pages.


These changes require **no code modifications** and are designed to improve performance across all apps.
However, you may see more individual prefetch requests with much lower total transfer sizes. We believe this is the right trade-off for nearly all applications.
If the increased request count causes issues, please let us know by creating an
