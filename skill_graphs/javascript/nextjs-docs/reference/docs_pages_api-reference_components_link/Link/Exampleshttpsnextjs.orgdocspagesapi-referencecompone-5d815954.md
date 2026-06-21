## Examples[](https://nextjs.org/docs/pages/api-reference/components/link#examples)
The following examples demonstrate how to use the `<Link>` component in different scenarios.
### Linking to dynamic route segments[](https://nextjs.org/docs/pages/api-reference/components/link#linking-to-dynamic-route-segments-1)
For [dynamic route segments](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#convention), it can be handy to use template literals to create the link's path.
For example, you can generate a list of links to the dynamic route `pages/blog/[slug].js`
pages/blog/index.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

function Posts({ posts }) {
  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>
          <Link href={`/blog/${post.slug}`}>{post.title}</Link>
        </li>
      ))}
    </ul>
  )
}
```

### Scrolling to an `id`[](https://nextjs.org/docs/pages/api-reference/components/link#scrolling-to-an-id)
If you'd like to scroll to a specific `id` on navigation, you can append your URL with a `#` hash link or just pass a hash link to the `href` prop. This is possible since `<Link>` renders to an `<a>` element.
```
<Link href="/dashboard#settings">Settings</Link>

// Output
<a href="/dashboard#settings">Settings</a>
```

### Passing a URL Object[](https://nextjs.org/docs/pages/api-reference/components/link#passing-a-url-object)
`Link` can also receive a URL object and it will automatically format it to create the URL string:
pages/index.ts
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

function Home() {
  return (
    <ul>
      <li>
        <Link
          href={{
            pathname: '/about',
            query: { name: 'test' },
          }}
        >
          About us
        </Link>
      </li>
      <li>
        <Link
          href={{
            pathname: '/blog/[slug]',
            query: { slug: 'my-post' },
          }}
        >
          Blog Post
        </Link>
      </li>
    </ul>
  )
}

export default Home
```

The above example has a link to:
  * A predefined route: `/about?name=test`
  * A [dynamic route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#convention): `/blog/my-post`


You can use every property as defined in the
### Replace the URL instead of push[](https://nextjs.org/docs/pages/api-reference/components/link#replace-the-url-instead-of-push)
The default behavior of the `Link` component is to `push` a new URL into the `history` stack. You can use the `replace` prop to prevent adding a new entry, as in the following example:
pages/index.js
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/about" replace>
      About us
    </Link>
  )
}
```

### Disable scrolling to the top of the page[](https://nextjs.org/docs/pages/api-reference/components/link#disable-scrolling-to-the-top-of-the-page)
The default behavior of `Link` is to scroll to the top of the page. When there is a hash defined it will scroll to the specific id, like a normal `<a>` tag. To prevent scrolling to the top / hash `scroll={false}` can be added to `Link`:
pages/index.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Home() {
  return (
    <Link href="/#hashid" scroll={false}>
      Disables scrolling to the top
    </Link>
  )
}
```

### Scroll offset with sticky headers[](https://nextjs.org/docs/pages/api-reference/components/link#scroll-offset-with-sticky-headers)
Because Next.js skips sticky and fixed positioned elements when finding the scroll target, content may end up behind a sticky header after navigation. For example, if your layout has a sticky header:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import './globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <header className="sticky top-0 h-16 bg-white">
          {/* Navigation */}
        </header>
        {children}
      </body>
    </html>
  )
}
```

You can account for its height using
app/globals.css
```
html {
  scroll-padding-top: 64px; /* Match the height of your sticky header */
}
```

This is a browser CSS property that offsets scroll-based positioning. It applies whenever Next.js uses the native `#id`) navigation. Alternatively, you can use
### Prefetching links in Proxy[](https://nextjs.org/docs/pages/api-reference/components/link#prefetching-links-in-proxy)
It's common to use [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) for authentication or other purposes that involve rewriting the user to a different page. In order for the `<Link />` component to properly prefetch links with rewrites via Proxy, you need to tell Next.js both the URL to display and the URL to prefetch. This is required to avoid un-necessary fetches to proxy to know the correct route to prefetch.
For example, if you want to serve a `/dashboard` route that has authenticated and visitor views, you can add the following in your Proxy to redirect the user to the correct page:
proxy.ts
TypeScript
JavaScript TypeScript
```
import { NextResponse } from 'next/server'

export function proxy(request: Request) {
  const nextUrl = request.nextUrl
  if (nextUrl.pathname === '/dashboard') {
    if (request.cookies.authToken) {
      return NextResponse.rewrite(new URL('/auth/dashboard', request.url))
    } else {
      return NextResponse.rewrite(new URL('/public/dashboard', request.url))
    }
  }
}
```

In this case, you would want to use the following code in your `<Link />` component:
pages/index.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import Link from 'next/link'
import useIsAuthed from './hooks/useIsAuthed' // Your auth hook

export default function Home() {
  const isAuthed = useIsAuthed()
  const path = isAuthed ? '/auth/dashboard' : '/public/dashboard'
  return (
    <Link as="/dashboard" href={path}>
      Dashboard
    </Link>
  )
}
```

> **Good to know** : If you're using [Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes#convention), you'll need to adapt your `as` and `href` props. For example, if you have a Dynamic Route like `/dashboard/authed/[user]` that you want to present differently via proxy, you would write: `<Link href={{ pathname: '/dashboard/authed/[user]', query: { user: username } }} as="/dashboard/[user]">Profile</Link>`.
