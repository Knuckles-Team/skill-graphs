# Link Component
Last updated February 27, 2026
`<Link>` is a React component that extends the HTML `<a>` element to provide [prefetching](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) and client-side navigation between routes. It is the primary way to navigate between routes in Next.js.
Basic usage:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Page() {
  return <Link href="/dashboard">Dashboard</Link>
}
```
