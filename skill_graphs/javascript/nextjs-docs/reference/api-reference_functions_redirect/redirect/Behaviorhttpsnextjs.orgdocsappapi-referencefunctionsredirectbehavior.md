## Behavior[](https://nextjs.org/docs/app/api-reference/functions/redirect#behavior)
  * In Server Actions and Route Handlers, redirect should be called **outside** the `try` block when using `try/catch` statements.
  * If you prefer to return a 308 (Permanent) HTTP redirect instead of 307 (Temporary), you can use the [`permanentRedirect` function](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect) instead.
  * `redirect` throws an error so it should be called **outside** the `try` block when using `try/catch` statements.
  * `redirect` can be called in Client Components during the rendering process but not in event handlers. You can use the [`useRouter` hook](https://nextjs.org/docs/app/api-reference/functions/use-router) instead.
  * `redirect` also accepts absolute URLs and can be used to redirect to external links.
  * If you'd like to redirect before the render process, use [`next.config.js`](https://nextjs.org/docs/app/guides/redirecting#redirects-in-nextconfigjs) or [Proxy](https://nextjs.org/docs/app/guides/redirecting#nextresponseredirect-in-proxy).
