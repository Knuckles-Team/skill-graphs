## Usage[](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife#usage)
To define a profile, enable the [`cacheComponents` flag](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) and add the cache profile in the `cacheLife` object in the `next.config.js` file. For example, a `blog` profile:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
  cacheLife: {
    blog: {
      stale: 3600, // 1 hour
      revalidate: 900, // 15 minutes
      expire: 86400, // 1 day
    },
  },
}

export default nextConfig
```

You can now use this custom `blog` configuration in your component or function as follows:
app/actions.ts
TypeScript
JavaScript TypeScript
```
import { cacheLife } from 'next/cache'

export async function getCachedData() {
  'use cache'
  cacheLife('blog')
  const data = await fetch('/api/data')
  return data
}
```
