# redirects
Last updated February 27, 2026
Redirects allow you to redirect an incoming request path to a different destination path.
To use redirects you can use the `redirects` key in `next.config.js`:
next.config.js
```
module.exports = {
  async redirects() {
    return [
      {
        source: '/about',
        destination: '/',
        permanent: true,
      },
    ]
  },
}
```

`redirects` is an async function that expects an array to be returned holding objects with `source`, `destination`, and `permanent` properties:
  * `source` is the incoming request path pattern.
  * `destination` is the path you want to route to.
  * `permanent` `true` or `false` - if `true` will use the 308 status code which instructs clients/search engines to cache the redirect forever, if `false` will use the 307 status code which is temporary and is not cached.


> **Why does Next.js use 307 and 308?** Traditionally a 302 was used for a temporary redirect, and a 301 for a permanent redirect, but many browsers changed the request method of the redirect to `GET`, regardless of the original method. For example, if the browser made a request to `POST /v1/users` which returned status code `302` with location `/v2/users`, the subsequent request might be `GET /v2/users` instead of the expected `POST /v2/users`. Next.js uses the 307 temporary redirect, and 308 permanent redirect status codes to explicitly preserve the request method used.
  * `basePath`: `false` or `undefined` - if false the `basePath` won't be included when matching, can be used for external redirects only.
  * `locale`: `false` or `undefined` - whether the locale should not be included when matching.
  * `has` is an array of [has objects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.
  * `missing` is an array of [missing objects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.


Redirects are checked before the filesystem which includes pages and `/public` files.
When using the Pages Router, redirects are not applied to client-side routing (`Link`, `router.push`) unless [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) is present and matches the path.
When a redirect is applied, any query values provided in the request will be passed through to the redirect destination. For example, see the following redirect configuration:
```
{
  source: '/old-blog/:path*',
  destination: '/blog/:path*',
  permanent: false
}
```

> **Good to know** : Remember to include the forward slash `/` before the colon `:` in path parameters of the `source` and `destination` paths, otherwise the path will be treated as a literal string and you run the risk of causing infinite redirects.
When `/old-blog/post-1?hello=world` is requested, the client will be redirected to `/blog/post-1?hello=world`.
