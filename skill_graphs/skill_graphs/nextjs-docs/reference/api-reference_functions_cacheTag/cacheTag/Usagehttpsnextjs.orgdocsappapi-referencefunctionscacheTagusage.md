## Usage[](https://nextjs.org/docs/app/api-reference/functions/cacheTag#usage)
To use `cacheTag`, enable the [`cacheComponents` flag](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) in your `next.config.js` file:
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

The `cacheTag` function takes one or more string values.
app/data.ts
TypeScript
JavaScript TypeScript
```
import { cacheTag } from 'next/cache'

export async function getData() {
  'use cache'
  cacheTag('my-data')
  const data = await fetch('/api/data')
  return data
}
```

You can then purge the cache on-demand using [`revalidateTag`](https://nextjs.org/docs/app/api-reference/functions/revalidateTag) API in another function, for example, a [route handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) or [Server Action](https://nextjs.org/docs/app/getting-started/updating-data):
app/action.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { revalidateTag } from 'next/cache'

export default async function submit() {
  await addPost()
  revalidateTag('my-data')
}
```
