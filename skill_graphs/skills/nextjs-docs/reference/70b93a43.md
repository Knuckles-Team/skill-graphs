# rewrites
Last updated February 27, 2026
Rewrites allow you to map an incoming request path to a different destination path.
Rewrites act as a URL proxy and mask the destination path, making it appear the user hasn't changed their location on the site. In contrast, [redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects) will reroute to a new page and show the URL changes.
To use rewrites you can use the `rewrites` key in `next.config.js`:
next.config.js
```
module.exports = {
  async rewrites() {
    return [
      {
        source: '/about',
        destination: '/',
      },
    ]
  },
}
```

Rewrites are applied to client-side routing. In the example above, navigating to `<Link href="/about">` will serve content from `/` while keeping the URL as `/about`.
`rewrites` is an async function that expects to return either an array or an object of arrays (see below) holding objects with `source` and `destination` properties:
  * `source`: `String` - is the incoming request path pattern.
  * `destination`: `String` is the path you want to route to.
  * `basePath`: `false` or `undefined` - if false the basePath won't be included when matching, can be used for external rewrites only.
  * `locale`: `false` or `undefined` - whether the locale should not be included when matching.
  * `has` is an array of [has objects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.
  * `missing` is an array of [missing objects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.


When the `rewrites` function returns an array, rewrites are applied after checking the filesystem (pages and `/public` files) and before dynamic routes. When the `rewrites` function returns an object of arrays with a specific shape, this behavior can be changed and more finely controlled, as of `v10.1` of Next.js:
next.config.js
```
module.exports = {
  async rewrites() {
    return {
      beforeFiles: [
        // These rewrites are checked after headers/redirects
        // and before all files including _next/public files which
        // allows overriding page files
        {
          source: '/some-page',
          destination: '/somewhere-else',
          has: [{ type: 'query', key: 'overrideMe' }],
        },
      ],
      afterFiles: [
        // These rewrites are checked after pages/public files
        // are checked but before dynamic routes
        {
          source: '/non-existent',
          destination: '/somewhere-else',
        },
      ],
      fallback: [
        // These rewrites are checked after both pages/public files
        // and dynamic routes are checked
        {
          source: '/:path*',
          destination: `https://my-old-site.com/:path*`,
        },
      ],
    }
  },
}
```

> **Good to know** : rewrites in `beforeFiles` do not check the filesystem/dynamic routes immediately after matching a source, they continue until all `beforeFiles` have been checked.
The order Next.js routes are checked is:
  1. [headers](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers) are checked/applied
  2. [redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects) are checked/applied
  3. `beforeFiles` rewrites are checked/applied
  4. static files from the [public directory](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder), `_next/static` files, and non-dynamic pages are checked/served
  5. `afterFiles` rewrites are checked/applied, if one of these rewrites is matched we check dynamic routes/static files after each match
  6. `fallback` rewrites are checked/applied, these are applied before rendering the 404 page and after dynamic routes/all static assets have been checked. If you use [fallback: true/'blocking'](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-true) in `getStaticPaths`, the fallback `rewrites` defined in your `next.config.js` will _not_ be run.
