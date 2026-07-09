## Enabling Cache Components[](https://nextjs.org/docs/app/getting-started/cache-components#enabling-cache-components)
You can enable Cache Components (which includes PPR) by adding the [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) option to your Next config file:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

> **Good to know:** When Cache Components is enabled, `GET` Route Handlers follow the same prerendering model as pages. See [Route Handlers with Cache Components](https://nextjs.org/docs/app/getting-started/route-handlers#with-cache-components) for details.
