## Unsupported Features[](https://nextjs.org/docs/pages/guides/static-exports#unsupported-features)
Features that require a Node.js server, or dynamic logic that cannot be computed during the build process, are **not** supported:
  * [Internationalized Routing](https://nextjs.org/docs/pages/guides/internationalization)
  * [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
  * [Rewrites](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites)
  * [Redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects)
  * [Headers](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers)
  * [Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy)
  * [Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)
  * [Image Optimization](https://nextjs.org/docs/pages/api-reference/components/image) with the default `loader`
  * [Draft Mode](https://nextjs.org/docs/pages/guides/draft-mode)
  * [`getStaticPaths` with `fallback: true`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true)
  * [`getStaticPaths` with `fallback: 'blocking'`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-blocking)
  * [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)
