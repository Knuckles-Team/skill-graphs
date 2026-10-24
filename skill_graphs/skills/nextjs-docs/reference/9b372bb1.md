# useSearchParams
Last updated February 27, 2026
`useSearchParams` is a **Client Component** hook that lets you read the current URL's **query string**.
`useSearchParams` returns a **read-only** version of the
app/dashboard/search-bar.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useSearchParams } from 'next/navigation'

export default function SearchBar() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  // URL -> `/dashboard?search=my-project`
  // `search` -> 'my-project'
  return <>Search: {search}</>
}
```
