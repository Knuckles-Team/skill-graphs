# useParams
Last updated February 27, 2026
`useParams` is a hook that lets you read a route's [dynamic params](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes) filled in by the current URL.
pages/shop/[slug].tsx
TypeScript
JavaScript TypeScript
```
import { useParams } from 'next/navigation'

export default function ShopPage() {
  const params = useParams<{ slug: string }>()

  if (!params) {
    // Render fallback UI while params are not yet available
    return null
  }

  // Route -> /shop/[slug]
  // URL -> /shop/shoes
  // `params` -> { slug: 'shoes' }
  return <>Shop: {params.slug}</>
}
```
