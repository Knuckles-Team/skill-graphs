## Possible Ways to Fix It[](https://nextjs.org/docs/messages/missing-suspense-with-csr-bailout#possible-ways-to-fix-it)
You have a few options depending on your intent:
  * To keep the route statically generated, wrap the smallest subtree that calls `useSearchParams()` in `Suspense`, for example you may move its usage into a child Client Component and render that component wrapped with `Suspense`. This preserves the static shell and avoids a full CSR bailout.
  * To make the route dynamically rendered, use the [`connection`](https://nextjs.org/docs/app/api-reference/functions/connection) function in a Server Component (e.g. the Page or a wrapping Layout). This waits for an incoming request and excludes everything below from prerendering.


app/page.tsx
TypeScript
JavaScript TypeScript
```
import { connection } from 'next/server'

export default async function Page() {
  await connection()
  return <div>...</div>
}
```

  * Before the `connection` API was available setting `export const dynamic = 'force-dynamic'` in a Server Component `page.tsx`, or `layout.tsx`, opted the route into on-demand rendering. Note that setting `dynamic` in a Client Component (`'use client'`) `page.tsx` has no effect.


app/layout.tsx
TypeScript
JavaScript TypeScript
```
export const dynamic = 'force-dynamic'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return children
}
```

  * Alternatively, a Server Component Page can pass the `searchParams` value down to Client Components. In a Client Component, you can unwrap it with React's `use()` (ensure a surrounding `Suspense` boundary). See [What to use and when](https://nextjs.org/docs/app/getting-started/layouts-and-pages#what-to-use-and-when).


app/page.tsx
TypeScript
JavaScript TypeScript
```
import { Suspense } from 'react'
import ClientSearch from './client-search'

export default function Page({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>
}) {
  return (
    <Suspense fallback={<>...</>}>
      <ClientSearch searchParams={searchParams} />
    </Suspense>
  )
}
```

app/client-search.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { use } from 'react'

export default function ClientSearch({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>
}) {
  const params = use(searchParams)
  return <div>Query: {params.q}</div>
}
```

  * Consider making the Page a Server Component again and isolating Client-only code (that uses `useSearchParams`) into child Client Components.


app/search.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useSearchParams } from 'next/navigation'
import { Suspense } from 'react'

function Search() {
  const searchParams = useSearchParams()

  return <input placeholder="Search..." />
}

export function Searchbar() {
  return (
    // You could have a loading skeleton as the `fallback` too
    <Suspense>
      <Search />
    </Suspense>
  )
}
```
