##  `use cache` at runtime[](https://nextjs.org/docs/app/api-reference/directives/use-cache#use-cache-at-runtime)
On the **server** , cache entries are stored in-memory and respect the `revalidate` and `expire` times from your `cacheLife` configuration. You can customize the cache storage by configuring [`cacheHandlers`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers) in your `next.config.js` file.
On the **client** , content from the server cache is stored in the browser's memory for the duration defined by the `stale` time. The client router enforces a **minimum 30-second stale time** , regardless of configuration.
The `x-nextjs-stale-time` response header communicates cache lifetime from server to client, ensuring coordinated behavior.
