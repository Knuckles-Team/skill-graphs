## Usage[](https://nextjs.org/docs/app/api-reference/directives/use-cache#usage)
`use cache` is a Cache Components feature. To enable it, add the [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) option to your `next.config.ts` file:
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

Then, add `use cache` at the file, component, or function level:
```
// File level
'use cache'

export default async function Page() {
  // ...
}

// Component level
export async function MyComponent() {
  'use cache'
  return <></>
}

// Function level
export async function getData() {
  'use cache'
  const data = await fetch('/api/data')
  return data
}
```

> **Good to know** : When used at file level, all function exports must be async functions.
