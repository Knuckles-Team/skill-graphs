# useRouter
Last updated February 27, 2026
The `useRouter` hook allows you to programmatically change routes inside [Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components).
> **Recommendation:** Use the [`<Link>` component](https://nextjs.org/docs/app/api-reference/components/link) for navigation unless you have a specific requirement for using `useRouter`.
app/example-client-component.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.push('/dashboard')}>
      Dashboard
    </button>
  )
}
```
