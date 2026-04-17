## You might not need `useLinkStatus`[](https://nextjs.org/docs/app/api-reference/functions/use-link-status#you-might-not-need-uselinkstatus)
Before adding inline feedback, consider if:
  * The destination is static and prefetched in production, so the pending phase may be skipped.
  * The route has a `loading.js` file, enabling instant transitions with a route-level fallback.


Navigation is typically fast. Use `useLinkStatus` as a quick patch when you identify a slow transition, then iterate to fix the root cause with prefetching or a `loading.js` fallback.
