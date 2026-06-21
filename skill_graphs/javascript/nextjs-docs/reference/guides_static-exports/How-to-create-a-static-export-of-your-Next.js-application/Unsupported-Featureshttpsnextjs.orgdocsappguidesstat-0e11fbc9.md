## Unsupported Features[](https://nextjs.org/docs/app/guides/static-exports#unsupported-features)
Features that require a Node.js server, or dynamic logic that cannot be computed during the build process, are **not** supported:
  * [Dynamic Routes](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) with `dynamicParams: true`
  * [Dynamic Routes](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) without `generateStaticParams()`
  * [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) that rely on Request
  * [Cookies](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [Rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)
  * [Redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)
  * [Headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)
  * [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  * [Incremental Static Regeneration](https://nextjs.org/docs/app/guides/incremental-static-regeneration)
  * [Image Optimization](https://nextjs.org/docs/app/api-reference/components/image) with the default `loader`
  * [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode)
  * [Server Actions](https://nextjs.org/docs/app/getting-started/updating-data)
  * [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes)


Attempting to use any of these features with `next dev` will result in an error, similar to setting the [`dynamic`](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config#dynamic) option to `error` in the root layout.
```
export const dynamic = 'error'
```
