##  `redirects` in `next.config.js`[](https://nextjs.org/docs/pages/guides/redirecting#redirects-in-nextconfigjs)
The `redirects` option in the `next.config.js` file allows you to redirect an incoming request path to a different destination path. This is useful when you change the URL structure of pages or have a list of redirects that are known ahead of time.
`redirects` supports [path](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#path-matching), [header, cookie, and query matching](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching), giving you the flexibility to redirect users based on an incoming request.
To use `redirects`, add the option to your `next.config.js` file:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  async redirects() {
    return [
      // Basic redirect
      {
        source: '/about',
        destination: '/',
        permanent: true,
      },
      // Wildcard path matching
      {
        source: '/blog/:slug',
        destination: '/news/:slug',
        permanent: true,
      },
    ]
  },
}

export default nextConfig
```

See the [`redirects` API reference](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects) for more information.
> **Good to know** :
>   * `redirects` can return a 307 (Temporary Redirect) or 308 (Permanent Redirect) status code with the `permanent` option.
>   * `redirects` may have a limit on platforms. For example, on Vercel, there's a limit of 1,024 redirects. To manage a large number of redirects (1000+), consider creating a custom solution using [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy). See [managing redirects at scale](https://nextjs.org/docs/pages/guides/redirecting#managing-redirects-at-scale-advanced) for more.
>   * `redirects` runs **before** Proxy.
>
