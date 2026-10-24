## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents#usage)
To enable the `cacheComponents` flag, set it to `true` in your `next.config.ts` file:
next.config.ts
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
}

export default nextConfig
```

When `cacheComponents` is enabled, you can use the following cache functions and configurations:
  * The [`use cache` directive](https://nextjs.org/docs/app/api-reference/directives/use-cache)
  * The [`cacheLife` function](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife) with `use cache`
  * The [`cacheTag` function](https://nextjs.org/docs/app/api-reference/functions/cacheTag)
