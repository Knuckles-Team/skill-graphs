## Constraints[](https://nextjs.org/docs/app/api-reference/directives/use-cache#constraints)
Cached functions execute in an isolated environment. The following constraints ensure cache behavior remains predictable and secure.
### Runtime APIs[](https://nextjs.org/docs/app/api-reference/directives/use-cache#runtime-apis)
Cached functions and components **cannot** directly access runtime APIs like `cookies()`, `headers()`, or `searchParams`. Instead, read these values outside the cached scope and pass them as arguments.
### Runtime caching considerations[](https://nextjs.org/docs/app/api-reference/directives/use-cache#runtime-caching-considerations)
While `use cache` is designed primarily to include dynamic data in the static shell, it can also cache data at runtime using in-memory LRU (Least Recently Used) storage.
Runtime cache behavior depends on your hosting environment:
Environment | Runtime Caching Behavior
---|---
**Serverless** | Cache entries typically don't persist across requests (each request can be a different instance). Build-time caching works normally.
**Self-hosted** | Cache entries persist across requests. Control cache size with [`cacheMaxMemorySize`](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath).
If the default in-memory cache isn't enough, consider **[`use cache: remote`](https://nextjs.org/docs/app/api-reference/directives/use-cache-remote)**which allows platforms to provide a dedicated cache handler (like Redis or KV database). This helps reduce hits against data sources not scaled to your total traffic, though it comes with costs (storage, network latency, platform fees).
Very rarely, for compliance requirements or when you can't refactor your code to pass runtime data as arguments to a `use cache` scope, you might need [`use cache: private`](https://nextjs.org/docs/app/api-reference/directives/use-cache-private).
### React.cache isolation[](https://nextjs.org/docs/app/api-reference/directives/use-cache#reactcache-isolation)
`use cache` boundaries. Values stored via `React.cache` outside a `use cache` function are not visible inside it.
This means you cannot use `React.cache` to pass data into a `use cache` scope:
```
import { cache } from 'react'

const store = cache(() => ({ current: null as string | null }))

function Parent() {
  const shared = store()
  shared.current = 'value from parent'
  return <Child />
}

async function Child() {
  'use cache'
  const shared = store()
  // shared.current is null, not 'value from parent'
  // use cache has its own isolated React.cache scope
  return <div>{shared.current}</div>
}
```

This isolation ensures cached functions have predictable, self-contained behavior. To pass data into a `use cache` scope, use function arguments instead.
