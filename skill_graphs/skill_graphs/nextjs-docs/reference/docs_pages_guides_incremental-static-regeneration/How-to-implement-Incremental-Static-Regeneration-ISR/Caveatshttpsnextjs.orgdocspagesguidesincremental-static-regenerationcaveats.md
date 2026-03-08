## Caveats[](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#caveats)
  * ISR is only supported when using the Node.js runtime (default).
  * ISR is not supported when creating a [Static Export](https://nextjs.org/docs/app/guides/static-exports).
  * Proxy won't be executed for on-demand ISR requests, meaning any path rewrites or logic in Proxy will not be applied. Ensure you are revalidating the exact path. For example, `/post/1` instead of a rewritten `/post-1`.
