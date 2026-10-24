## Prefetching optimizations[](https://nextjs.org/docs/app/guides/prefetching#prefetching-optimizations)
### Client cache[](https://nextjs.org/docs/app/guides/prefetching#client-cache)
Next.js stores prefetched React Server Component payloads in memory, keyed by route segments. When navigating between sibling routes (e.g. `/dashboard/settings` → `/dashboard/analytics`), it reuses the parent layout and only fetches the updated leaf page. This reduces network traffic and improves navigation speed.
### Prefetch scheduling[](https://nextjs.org/docs/app/guides/prefetching#prefetch-scheduling)
Next.js maintains a small task queue, which prefetches in the following order:
  1. Links in the viewport
  2. Links showing user intent (hover or touch)
  3. Newer links replace older ones
  4. Links scrolled off-screen are discarded


The scheduler prioritizes likely navigations while minimizing unused downloads.
### Partial Prerendering (PPR)[](https://nextjs.org/docs/app/guides/prefetching#partial-prerendering-ppr)
When PPR is enabled, a page is divided into a static shell and a streamed dynamic section:
  * The shell, which can be prefetched, streams immediately
  * Dynamic data streams when ready
  * Data invalidations (`revalidateTag`, `revalidatePath`) silently refresh associated prefetches
