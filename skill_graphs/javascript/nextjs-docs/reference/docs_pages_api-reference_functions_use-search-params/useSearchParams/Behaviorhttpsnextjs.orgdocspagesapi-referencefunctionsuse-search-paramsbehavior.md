## Behavior[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#behavior)
### Behavior during pre-rendering[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#behavior-during-pre-rendering)
For pages that are [statically optimized](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization) (not using `getServerSideProps`), `useSearchParams` will return `null` during pre-rendering. After hydration, the value will be updated to the actual search params.
This is because search params cannot be known during static generation as they depend on the request.
pages/dashboard.tsx
TypeScript
JavaScript TypeScript
```
import { useSearchParams } from 'next/navigation'

export default function Dashboard() {
  const searchParams = useSearchParams()

  if (!searchParams) {
    // Return a fallback UI while search params are loading
    // This prevents hydration mismatches
    return <DashboardSkeleton />
  }

  const search = searchParams.get('search')

  return <>Search: {search}</>
}
```

### Using with `getServerSideProps`[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#using-with-getserversideprops)
When using [`getServerSideProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props), the page is server-rendered on each request and `useSearchParams` will return the actual search params immediately:
pages/dashboard.tsx
TypeScript
JavaScript TypeScript
```
import { useSearchParams } from 'next/navigation'

export default function Dashboard() {
  const searchParams = useSearchParams()

  // With getServerSideProps, this fallback is never rendered because
  // searchParams is always available on the server. However, keeping
  // the fallback allows this component to be reused on other pages
  // that may not use getServerSideProps.
  if (!searchParams) {
    return null
  }

  const search = searchParams.get('search')

  return <>Search: {search}</>
}

export async function getServerSideProps() {
  return { props: {} }
}
```
