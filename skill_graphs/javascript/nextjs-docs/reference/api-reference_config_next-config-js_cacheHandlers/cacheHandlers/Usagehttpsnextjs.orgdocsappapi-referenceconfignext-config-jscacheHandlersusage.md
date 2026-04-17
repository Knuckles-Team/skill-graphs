## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#usage)
To configure custom cache handlers:
  1. Define your cache handler in a separate file, see [examples](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#examples) for implementation details.
  2. Reference the file path in your Next config file


next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheHandlers: {
    default: require.resolve('./cache-handlers/default-handler.js'),
    remote: require.resolve('./cache-handlers/remote-handler.js'),
  },
}

export default nextConfig
```

### Handler types[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheHandlers#handler-types)
  * **`default`**: Used by the`'use cache'` directive
  * **`remote`**: Used by the`'use cache: remote'` directive


If you don't configure `cacheHandlers`, Next.js uses an in-memory LRU (Least Recently Used) cache for both `default` and `remote`. You can view the
You can also define additional named handlers (e.g., `sessions`, `analytics`) and reference them with `'use cache: <name>'`.
Note that `'use cache: private'` does not use cache handlers and cannot be customized.
