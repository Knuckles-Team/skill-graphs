## Examples[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#examples)
### Updating search params[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#updating-search-params)
You can use the [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router) hook to update search params:
pages/dashboard.tsx
TypeScript
JavaScript TypeScript
```
import { useRouter } from 'next/router'
import { useSearchParams } from 'next/navigation'
import { useCallback } from 'react'

export default function Dashboard() {
  const router = useRouter()
  const searchParams = useSearchParams()

  const createQueryString = useCallback(
    (name: string, value: string) => {
      const params = new URLSearchParams(searchParams?.toString())
      params.set(name, value)
      return params.toString()
    },
    [searchParams]
  )

  if (!searchParams) {
    return null
  }

  return (
    <>
      <p>Sort By</p>
      <button
        onClick={() => {
          router.push(router.pathname + '?' + createQueryString('sort', 'asc'))
        }}
      >
        ASC
      </button>
      <button
        onClick={() => {
          router.push(router.pathname + '?' + createQueryString('sort', 'desc'))
        }}
      >
        DESC
      </button>
    </>
  )
}
```

### Sharing components with App Router[](https://nextjs.org/docs/pages/api-reference/functions/use-search-params#sharing-components-with-app-router)
`useSearchParams` from `next/navigation` works in both the Pages Router and App Router. This allows you to create shared components that work in either context:
components/search-bar.tsx
TypeScript
JavaScript TypeScript
```
import { useSearchParams } from 'next/navigation'

// This component works in both pages/ and app/
export function SearchBar() {
  const searchParams = useSearchParams()

  if (!searchParams) {
    // Fallback for Pages Router during pre-rendering
    return <input defaultValue="" placeholder="Search..." />
  }

  const search = searchParams.get('search') ?? ''

  return <input defaultValue={search} placeholder="Search..." />
}
```

> **Good to know** : When using this component in the App Router, wrap it in a `<Suspense>` boundary for [static rendering](https://nextjs.org/docs/app/api-reference/functions/use-search-params#static-rendering) support.
