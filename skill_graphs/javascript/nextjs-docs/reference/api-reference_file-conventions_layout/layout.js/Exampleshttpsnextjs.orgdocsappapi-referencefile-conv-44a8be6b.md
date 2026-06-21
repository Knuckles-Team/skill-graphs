## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#examples)
### Metadata[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#metadata)
You can modify the `<head>` HTML elements such as `title` and `meta` using the [`metadata` object](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#the-metadata-object) or [`generateMetadata` function](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#generatemetadata-function).
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Next.js',
}

export default function Layout({ children }: { children: React.ReactNode }) {
  return '...'
}
```

> **Good to know** : You should **not** manually add `<head>` tags such as `<title>` and `<meta>` to root layouts. Instead, use the [Metadata APIs](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) which automatically handles advanced requirements such as streaming and de-duplicating `<head>` elements.
### Active Nav Links[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#active-nav-links)
You can use the [`usePathname`](https://nextjs.org/docs/app/api-reference/functions/use-pathname) hook to determine if a nav link is active.
Since `usePathname` is a client hook, you need to extract the nav links into a Client Component, which can be imported into your layout:
app/ui/nav-links.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { usePathname } from 'next/navigation'
import Link from 'next/link'

export function NavLinks() {
  const pathname = usePathname()

  return (
    <nav>
      <Link className={`link ${pathname === '/' ? 'active' : ''}`} href="/">
        Home
      </Link>

      <Link
        className={`link ${pathname === '/about' ? 'active' : ''}`}
        href="/about"
      >
        About
      </Link>
    </nav>
  )
}
```

app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { NavLinks } from '@/app/ui/nav-links'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <NavLinks />
        <main>{children}</main>
      </body>
    </html>
  )
}
```

### Displaying content based on `params`[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#displaying-content-based-on-params)
Using [dynamic route segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes), you can display or fetch specific content based on the `params` prop.
app/dashboard/layout.tsx
TypeScript
JavaScript TypeScript
```
export default async function DashboardLayout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Promise<{ team: string }>
}) {
  const { team } = await params

  return (
    <section>
      <header>
        <h1>Welcome to {team}'s Dashboard</h1>
      </header>
      <main>{children}</main>
    </section>
  )
}
```

### Reading `params` in Client Components[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#reading-params-in-client-components)
To use `params` in a Client Component (which cannot be `async`), you can use React's
app/page.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { use } from 'react'

export default function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = use(params)
}
```
