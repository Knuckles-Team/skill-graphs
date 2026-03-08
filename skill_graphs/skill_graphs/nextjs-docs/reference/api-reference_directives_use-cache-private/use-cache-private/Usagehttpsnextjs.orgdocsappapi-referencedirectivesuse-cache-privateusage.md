## Usage[](https://nextjs.org/docs/app/api-reference/directives/use-cache-private#usage)
To use `'use cache: private'`, enable the [`cacheComponents`](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents) flag in your `next.config.ts` file:
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

Then add `'use cache: private'` to your function along with a `cacheLife` configuration.
> **Good to know** : This directive is not available in Route Handlers.
### Basic example[](https://nextjs.org/docs/app/api-reference/directives/use-cache-private#basic-example)
In this example, we demonstrate that you can access cookies within a `'use cache: private'` scope:
app/product/[id]/page.tsx
TypeScript
JavaScript TypeScript
```
import { Suspense } from 'react'
import { cookies } from 'next/headers'
import { cacheLife, cacheTag } from 'next/cache'

export async function generateStaticParams() {
  return [{ id: '1' }]
}

export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params

  return (
    <div>
      <ProductDetails id={id} />
      <Suspense fallback={<div>Loading recommendations...</div>}>
        <Recommendations productId={id} />
      </Suspense>
    </div>
  )
}

async function Recommendations({ productId }: { productId: string }) {
  const recommendations = await getRecommendations(productId)

  return (
    <div>
      {recommendations.map((rec) => (
        <ProductCard key={rec.id} product={rec} />
      ))}
    </div>
  )
}

async function getRecommendations(productId: string) {
  'use cache: private'
  cacheTag(`recommendations-${productId}`)
  cacheLife({ stale: 60 })

  // Access cookies within private cache functions
  const sessionId = (await cookies()).get('session-id')?.value || 'guest'

  return getPersonalizedRecommendations(productId, sessionId)
}
```

> **Good to know** : The `stale` time must be at least 30 seconds for runtime prefetching to work. See [`cacheLife` client router cache behavior](https://nextjs.org/docs/app/api-reference/functions/cacheLife#client-router-cache-behavior) for details.
