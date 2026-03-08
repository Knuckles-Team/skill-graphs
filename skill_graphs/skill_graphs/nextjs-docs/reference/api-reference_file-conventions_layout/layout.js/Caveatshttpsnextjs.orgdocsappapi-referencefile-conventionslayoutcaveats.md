## Caveats[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#caveats)
### Request Object[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#request-object)
Layouts are cached in the client during navigation to avoid unnecessary server requests.
[Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout) do not rerender. They can be cached and reused to avoid unnecessary computation when navigating between pages. By restricting layouts from accessing the raw request, Next.js can prevent the execution of potentially slow or expensive user code within the layout, which could negatively impact performance.
To access the request object, you can use [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers) and [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) APIs in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) and Functions.
app/shop/layout.tsx
TypeScript
JavaScript TypeScript
```
import { cookies } from 'next/headers'

export default async function Layout({ children }) {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

### Query params[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#query-params)
Layouts do not rerender on navigation, so they cannot access search params which would otherwise become stale.
To access updated query parameters, you can use the Page [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) prop, or read them inside a Client Component using the [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) hook. Since Client Components re-render on navigation, they have access to the latest query parameters.
app/ui/search.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useSearchParams } from 'next/navigation'

export default function Search() {
  const searchParams = useSearchParams()

  const search = searchParams.get('search')

  return '...'
}
```

app/shop/layout.tsx
TypeScript
JavaScript TypeScript
```
import Search from '@/app/ui/search'

export default function Layout({ children }) {
  return (
    <>
      <Search />
      {children}
    </>
  )
}
```

### Pathname[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#pathname)
Layouts do not re-render on navigation, so they do not access pathname which would otherwise become stale.
To access the current pathname, you can read it inside a Client Component using the [`usePathname`](https://nextjs.org/docs/app/api-reference/functions/use-pathname) hook. Since Client Components re-render during navigation, they have access to the latest pathname.
app/ui/breadcrumbs.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { usePathname } from 'next/navigation'

// Simplified breadcrumbs logic
export default function Breadcrumbs() {
  const pathname = usePathname()
  const segments = pathname.split('/')

  return (
    <nav>
      {segments.map((segment, index) => (
        <span key={index}>
          {' > '}
          {segment}
        </span>
      ))}
    </nav>
  )
}
```

app/docs/layout.tsx
TypeScript
JavaScript TypeScript
```
import { Breadcrumbs } from '@/app/ui/Breadcrumbs'

export default function Layout({ children }) {
  return (
    <>
      <Breadcrumbs />
      <main>{children}</main>
    </>
  )
}
```

### Fetching Data[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#fetching-data)
Layouts cannot pass data to their `children`. However, you can fetch the same data in a route more than once, and use React
Alternatively, when using [`fetch`](https://nextjs.org/docs/app/api-reference/functions/fetch)in Next.js, requests are automatically deduped.
app/lib/data.ts
TypeScript
JavaScript TypeScript
```
export async function getUser(id: string) {
  const res = await fetch(`https://.../users/${id}`)
  return res.json()
}
```

app/dashboard/layout.tsx
TypeScript
JavaScript TypeScript
```
import { getUser } from '@/app/lib/data'
import { UserName } from '@/app/ui/user-name'

export default async function Layout({ children }) {
  const user = await getUser('1')

  return (
    <>
      <nav>
        {/* ... */}
        <UserName user={user.name} />
      </nav>
      {children}
    </>
  )
}
```

app/dashboard/page.tsx
TypeScript
JavaScript TypeScript
```
import { getUser } from '@/app/lib/data'
import { UserName } from '@/app/ui/user-name'

export default async function Page() {
  const user = await getUser('1')

  return (
    <div>
      <h1>Welcome {user.name}</h1>
    </div>
  )
}
```

### Accessing child segments[](https://nextjs.org/docs/app/api-reference/file-conventions/layout#accessing-child-segments)
Layouts do not have access to the route segments below itself. To access all route segments, you can use [`useSelectedLayoutSegment`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment) or [`useSelectedLayoutSegments`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments) in a Client Component.
app/ui/nav-link.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import Link from 'next/link'
import { useSelectedLayoutSegment } from 'next/navigation'

export default function NavLink({
  slug,
  children,
}: {
  slug: string
  children: React.ReactNode
}) {
  const segment = useSelectedLayoutSegment()
  const isActive = slug === segment

  return (
    <Link
      href={`/blog/${slug}`}
      // Change style depending on whether the link is active
      style={{ fontWeight: isActive ? 'bold' : 'normal' }}
    >
      {children}
    </Link>
  )
}
```

app/blog/layout.tsx
TypeScript
JavaScript TypeScript
```
import { NavLink } from './nav-link'
import getPosts from './get-posts'

export default async function Layout({
  children,
}: {
  children: React.ReactNode
}) {
  const featuredPosts = await getPosts()
  return (
    <div>
      {featuredPosts.map((post) => (
        <div key={post.id}>
          <NavLink slug={post.slug}>{post.title}</NavLink>
        </div>
      ))}
      <div>{children}</div>
    </div>
  )
}
```
