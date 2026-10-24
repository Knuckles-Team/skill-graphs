## Behavior[](https://nextjs.org/docs/community/rspack#behavior)
### Behavior during pre-rendering[](https://nextjs.org/docs/community/rspack#behavior-during-pre-rendering)
For pages that are [statically optimized](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization), `useParams` will return `null` on the initial render. After hydration, the value will be updated to the actual params once the router is ready.
This is because params cannot be known during static generation for dynamic routes.
pages/shop/[slug].tsx
TypeScript
JavaScript TypeScript
```
import { useParams } from 'next/navigation'

export default function ShopPage() {
  const params = useParams<{ slug: string }>()

  if (!params) {
    // Return a fallback UI while params are loading
    // This prevents hydration mismatches
    return <ShopPageSkeleton />
  }

  return <>Shop: {params.slug}</>
}
```

### Using with `getServerSideProps`[](https://nextjs.org/docs/community/rspack#using-with-getserversideprops)
When using [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props), the page is server-rendered on each request and `useParams` will return the actual params immediately:
pages/shop/[slug].tsx
TypeScript
JavaScript TypeScript
```
import { useParams } from 'next/navigation'

export default function ShopPage() {
  const params = useParams<{ slug: string }>()

  // With getServerSideProps, this fallback is never rendered because
  // params is always available on the server. However, keeping
  // the fallback allows this component to be reused on other pages
  // that may not use getServerSideProps.
  if (!params) {
    return null
  }

  return <>Shop: {params.slug}</>
}

export async function getServerSideProps() {
  return { props: {} }
}
```

### Comparison with `router.query`[](https://nextjs.org/docs/community/rspack#comparison-with-routerquery)
`useParams` only returns the dynamic route parameters, whereas [`router.query`](https://nextjs.org/docs/pages/api-reference/functions/use-router#router-object) from `useRouter` includes both dynamic parameters and query string parameters.
pages/shop/[slug].tsx
TypeScript
JavaScript TypeScript
```
import { useRouter } from 'next/router'
import { useParams } from 'next/navigation'

export default function ShopPage() {
  const router = useRouter()
  const params = useParams()

  // URL -> /shop/shoes?color=red

  // router.query -> { slug: 'shoes', color: 'red' }
  // params -> { slug: 'shoes' }

  // ...
}
```
