## Examples[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#examples)
### Using preset profiles[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#using-preset-profiles-1)
The simplest way to configure caching is using preset profiles. Choose one that matches your content's update pattern:
app/blog/[slug]/page.tsx
```
import { cacheLife } from 'next/cache'

export default async function BlogPost() {
  'use cache'
  cacheLife('days') // Blog posts updated daily

  const post = await fetchBlogPost()
  return <article>{post.content}</article>
}
```

app/products/[id]/page.tsx
```
import { cacheLife } from 'next/cache'

export default async function ProductPage() {
  'use cache'
  cacheLife('hours') // Product data updated multiple times per day

  const product = await fetchProduct()
  return <div>{product.name}</div>
}
```

### Custom profiles for specific needs[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#custom-profiles-for-specific-needs)
Define custom profiles when preset options don't match your requirements:
next.config.ts
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  cacheComponents: true,
  cacheLife: {
    editorial: {
      stale: 600, // 10 minutes
      revalidate: 3600, // 1 hour
      expire: 86400, // 1 day
    },
    marketing: {
      stale: 300, // 5 minutes
      revalidate: 1800, // 30 minutes
      expire: 43200, // 12 hours
    },
  },
}

export default nextConfig
```

Then use these profiles throughout your application:
app/editorial/page.tsx
```
import { cacheLife } from 'next/cache'

export default async function EditorialPage() {
  'use cache'
  cacheLife('editorial')
  // ...
}
```

### Inline profiles for unique cases[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#inline-profiles-for-unique-cases)
Use inline profiles when a specific function needs one-off caching behavior:
app/api/limited-offer/route.ts
```
import { cacheLife } from 'next/cache'
import { getDb } from '@lib/db'

async function getLimitedOffer() {
  'use cache'

  cacheLife({
    stale: 60, // 1 minute
    revalidate: 300, // 5 minutes
    expire: 3600, // 1 hour
  })

  const offer = await getDb().offer.findFirst({
    where: { type: 'limited' },
    orderBy: { created_at: 'desc' },
  })

  return offer
}

export async function GET() {
  const offer = await getLimitedOffer()

  return Response.json(offer)
}
```

### Caching individual functions[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#caching-individual-functions)
Apply caching to utility functions for granular control:
lib/api.ts
```
import { cacheLife } from 'next/cache'

export async function getSettings() {
  'use cache'
  cacheLife('max') // Settings rarely change

  return await fetchSettings()
}
```

lib/stats.ts
```
import { cacheLife } from 'next/cache'

export async function getRealtimeStats() {
  'use cache'
  cacheLife('seconds') // Stats update constantly

  return await fetchStats()
}
```

### Nested caching behavior[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#nested-caching-behavior)
When you nest `use cache` directives (a cached function or component using another cached function or component), the outer cache's behavior depends on whether it has an explicit `cacheLife`.
#### With explicit outer cacheLife[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#with-explicit-outer-cachelife)
The outer cache uses its own lifetime, regardless of inner cache lifetimes. When the outer cache hits, it returns the complete output including all nested data. An explicit `cacheLife` always takes precedence, whether it's longer or shorter than inner lifetimes.
app/dashboard/page.tsx
```
import { cacheLife } from 'next/cache'
import { Widget } from './widget'

export default async function Dashboard() {
  'use cache'
  cacheLife('hours') // Outer scope sets its own lifetime

  return (
    <div>
      <h1>Dashboard</h1>
      <Widget /> {/* Inner scope has 'minutes' lifetime */}
    </div>
  )
}
```

#### Without explicit outer cacheLife[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#without-explicit-outer-cachelife)
If you don't call `cacheLife` in the outer cache, it uses the `default` profile (15 min revalidate). Inner caches with shorter lifetimes can reduce the outer cache's `default` lifetime. Inner caches with longer lifetimes cannot extend it beyond the default.
app/dashboard/page.tsx
```
import { Widget } from './widget'

export default async function Dashboard() {
  'use cache'
  // No cacheLife call - uses default (15 min)
  // If Widget has 5 min → Dashboard becomes 5 min
  // If Widget has 1 hour → Dashboard stays 15 min

  return (
    <div>
      <h1>Dashboard</h1>
      <Widget />
    </div>
  )
}
```

**It is recommended to specify an explicit`cacheLife`.** With explicit lifetime values, you can inspect a cached function or component and immediately know its behavior without tracing through nested caches. Without explicit lifetime values, the behavior becomes dependent on inner cache lifetimes, making it harder to reason about.
### Conditional cache lifetimes[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#conditional-cache-lifetimes)
You can call `cacheLife` conditionally in different code paths to set different cache durations based on your application logic:
lib/posts.ts
```
import { cacheLife, cacheTag } from 'next/cache'

async function getPostContent(slug: string) {
  'use cache'

  const post = await fetchPost(slug)

  // Tag the cache entry for targeted revalidation
  cacheTag(`post-${slug}`)

  if (!post) {
    // Content may not be published yet or could be in draft
    // Cache briefly to reduce database load
    cacheLife('minutes')
    return null
  }

  // Published content can be cached longer
  cacheLife('days')

  // Return only the necessary data to keep cache size minimal
  return post.data
}
```

This pattern is useful when different outcomes need different cache durations, for example, when an item is missing but is likely to be available later.
#### Using dynamic cache lifetimes from data[](https://nextjs.org/docs/app/api-reference/functions/cacheLife#using-dynamic-cache-lifetimes-from-data)
If you want to calculate cache lifetime at runtime, for example by reading it from the fetched data, use an [inline cache profile](https://nextjs.org/docs/app/api-reference/functions/cacheLife#inline-cache-profiles) object:
lib/posts.ts
```
import { cacheLife, cacheTag } from 'next/cache'

async function getPostContent(slug: string) {
  'use cache'

  const post = await fetchPost(slug)
  cacheTag(`post-${slug}`)

  if (!post) {
    cacheLife('minutes')
    return null
  }

  // Use cache timing from CMS data directly as an object
  cacheLife({
    // Ensure post.revalidateSeconds is a number in seconds
    // stale and expire inherit from 'default' profile
    revalidate: post.revalidateSeconds ?? 3600,
  })

  return post.data
}
```
