## Behavior[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#behavior)
### Static Rendering[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#static-rendering)
If a route is [statically rendered](https://nextjs.org/docs/app/guides/caching#static-rendering), calling `useSearchParams` will cause the Client Component tree up to the closest [`Suspense` boundary](https://nextjs.org/docs/app/api-reference/file-conventions/loading#examples) to be client-side rendered.
This allows a part of the route to be statically rendered while the dynamic part that uses `useSearchParams` is client-side rendered.
We recommend wrapping the Client Component that uses `useSearchParams` in a `<Suspense/>` boundary. This will allow any Client Components above it to be statically rendered and sent as part of initial HTML. [Example](https://nextjs.org/docs/app/api-reference/functions/use-search-params#static-rendering).
For example:
app/dashboard/search-bar.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  // This will not be logged on the server when using static rendering
  console.log(search)

  return <>Search: {search}</>
}
```

app/dashboard/page.tsx
TypeScript
JavaScript TypeScript
```
import { Suspense } from 'react'
import SearchBar from './search-bar'

// This component passed as a fallback to the Suspense boundary
// will be rendered in place of the search bar in the initial HTML.
// When the value is available during React hydration the fallback
// will be replaced with the `<SearchBar>` component.
function SearchBarFallback() {
  return <>placeholder</>
}

export default function Page() {
  return (
    <>
      <nav>
        <Suspense fallback={<SearchBarFallback />}>
          <SearchBar />
        </Suspense>
      </nav>
      <h1>Dashboard</h1>
    </>
  )
}
```

> **Good to know** :
>   * In development, routes are rendered on-demand, so `useSearchParams` doesn't suspend and things may appear to work without `Suspense`.
>   * During production builds, a [static page](https://nextjs.org/docs/app/guides/caching#static-rendering) that calls `useSearchParams` from a Client Component must be wrapped in a `Suspense` boundary, otherwise the build fails with the [Missing Suspense boundary with useSearchParams](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout) error.
>   * If you intend the route to be dynamically rendered, prefer using the [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection) function first in a Server Component to wait for an incoming request, this excludes everything below from prerendering. See what makes a route dynamic in the [Dynamic Rendering guide](https://nextjs.org/docs/app/guides/caching#dynamic-rendering).
>   * If you're already in a Server Component Page, consider using the [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) and passing the values to Client Components.
>   * You can also pass the Page [`searchParams` prop](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) directly to a Client Component and unwrap it with React's `use()`. Although this will suspend, so the Client Component should be wrapped with a `Suspense` boundary.
>

### Dynamic Rendering[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#dynamic-rendering)
If a route is [dynamically rendered](https://nextjs.org/docs/app/guides/caching#dynamic-rendering), `useSearchParams` will be available on the server during the initial server render of the Client Component.
For example:
app/dashboard/search-bar.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  // This will be logged on the server during the initial render
  // and on the client on subsequent navigations.
  console.log(search)

  return <>Search: {search}</>
}
```

app/dashboard/page.tsx
TypeScript
JavaScript TypeScript
```
import { connection } from 'next/server'
import SearchBar from './search-bar'

export default async function Page() {
  await connection()
  return (
    <>
      <nav>
        <SearchBar />
      </nav>
      <h1>Dashboard</h1>
    </>
  )
}
```

> **Good to know** :
>   * Previously, setting `export const dynamic = 'force-dynamic'` on the page was used to force dynamic rendering. Prefer using [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection) instead, as it semantically ties dynamic rendering to the incoming request.
>

### Server Components[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#server-components)
#### Pages[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#pages)
To access search params in [Pages](https://nextjs.org/docs/app/api-reference/file-conventions/page) (Server Components), use the [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) prop.
#### Layouts[](https://nextjs.org/docs/app/api-reference/functions/use-search-params#layouts)
Unlike Pages, [Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout) (Server Components) **do not** receive the `searchParams` prop. This is because a shared layout is [not re-rendered during navigation](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) which could lead to stale `searchParams` between navigations. View [detailed explanation](https://nextjs.org/docs/app/api-reference/file-conventions/layout#query-params).
Instead, use the Page [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page) prop or the [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) hook in a Client Component, which is re-rendered on the client with the latest `searchParams`.
