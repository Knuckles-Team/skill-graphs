## Headers with basePath support[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#headers-with-basepath-support)
When leveraging [`basePath` support](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath) with headers each `source` is automatically prefixed with the `basePath` unless you add `basePath: false` to the header:
next.config.js
```
module.exports = {
  basePath: '/docs',

  async headers() {
    return [
      {
        source: '/with-basePath', // becomes /docs/with-basePath
        headers: [
          {
            key: 'x-hello',
            value: 'world',
          },
        ],
      },
      {
        source: '/without-basePath', // is not modified since basePath: false is set
        headers: [
          {
            key: 'x-hello',
            value: 'world',
          },
        ],
        basePath: false,
      },
    ]
  },
}
```
