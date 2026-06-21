## When does getStaticProps run[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#when-does-getstaticprops-run)
`getStaticProps` always runs on the server and never on the client. You can validate code written inside `getStaticProps` is removed from the client-side bundle
  * `getStaticProps` always runs during `next build`
  * `getStaticProps` runs in the background when using [`fallback: true`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true)
  * `getStaticProps` is called before initial render when using [`fallback: blocking`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-blocking)
  * `getStaticProps` runs in the background when using `revalidate`
  * `getStaticProps` runs on-demand in the background when using [`revalidate()`](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath)


When combined with [Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration), `getStaticProps` will run in the background while the stale page is being revalidated, and the fresh page served to the browser.
`getStaticProps` does not have access to the incoming request (such as query parameters or HTTP headers) as it generates static HTML. If you need access to the request for your page, consider using [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy) in addition to `getStaticProps`.
