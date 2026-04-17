# useSearchParams
Last updated February 27, 2026
`useSearchParams` is a hook that lets you read the current URL's **query string**.
`useSearchParams` returns a **read-only** version of the
pages/dashboard.tsx
TypeScript
JavaScript TypeScript
```
import { useSearchParams } from 'next/navigation'

export default function Dashboard() {
  const searchParams = useSearchParams()

  if (!searchParams) {
    // Render fallback UI while search params are not yet available
    return null
  }

  const search = searchParams.get('search')

  // URL -> `/dashboard?search=my-project`
  // `search` -> 'my-project'
  return <>Search: {search}</>
}
```
