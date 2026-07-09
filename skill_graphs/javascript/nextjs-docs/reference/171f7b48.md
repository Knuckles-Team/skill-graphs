# headers
Last updated February 27, 2026
Headers allow you to set custom HTTP headers on the response to an incoming request on a given path.
To set custom HTTP headers you can use the `headers` key in `next.config.js`:
next.config.js
```
module.exports = {
  async headers() {
    return [
      {
        source: '/about',
        headers: [
          {
            key: 'x-custom-header',
            value: 'my custom header value',
          },
          {
            key: 'x-another-custom-header',
            value: 'my other custom header value',
          },
        ],
      },
    ]
  },
}
```

`headers` is an async function that expects an array to be returned holding objects with `source` and `headers` properties:
  * `source` is the incoming request path pattern.
  * `headers` is an array of response header objects, with `key` and `value` properties.
  * `basePath`: `false` or `undefined` - if false the basePath won't be included when matching, can be used for external rewrites only.
  * `locale`: `false` or `undefined` - whether the locale should not be included when matching.
  * `has` is an array of [has objects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.
  * `missing` is an array of [missing objects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#header-cookie-and-query-matching) with the `type`, `key` and `value` properties.


Headers are checked before the filesystem which includes pages and `/public` files.
