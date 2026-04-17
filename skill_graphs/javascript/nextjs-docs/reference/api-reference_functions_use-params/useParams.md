# useParams
Last updated February 27, 2026
`useParams` is a **Client Component** hook that lets you read a route's [dynamic params](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) filled in by the current URL.
app/example-client-component.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useParams } from 'next/navigation'

export default function ExampleClientComponent() {
  const params = useParams<{ tag: string; item: string }>()

  // Route -> /shop/[tag]/[item]
  // URL -> /shop/shoes/nike-air-max-97
  // `params` -> { tag: 'shoes', item: 'nike-air-max-97' }
  console.log(params)

  return '...'
}
```
