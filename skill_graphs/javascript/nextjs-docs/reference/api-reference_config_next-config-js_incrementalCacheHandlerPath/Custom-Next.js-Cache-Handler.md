# Custom Next.js Cache Handler
Last updated February 27, 2026
You can configure the Next.js cache location if you want to persist cached pages and data to durable storage, or share the cache across multiple containers or instances of your Next.js application.
> **Good to know** : The `cacheHandler` (singular) configuration is specifically used by Next.js for server cache operations such as storing and revalidating ISR and route handler responses. It is **not** used by `'use cache'` directives. For `'use cache'` directives, use [`cacheHandlers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers) (plural) instead.
next.config.js
```
module.exports = {
  cacheHandler: require.resolve('./cache-handler.js'),
  cacheMaxMemorySize: 0, // disable default in-memory caching
}
```

View an example of a [custom cache handler](https://nextjs.org/docs/app/guides/self-hosting#configuring-caching) and learn more about the implementation.
