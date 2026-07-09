## Examples[](https://nextjs.org/docs/app/api-reference/components/link#examples)
The following examples demonstrate how to use the `<Link>` component in different scenarios.
### Linking to dynamic route segments[](https://nextjs.org/docs/app/api-reference/components/link#linking-to-dynamic-route-segments)
When linking to [dynamic segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes), you can use
app/blog/post-list.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

interface Post {
  id: number
  title: string
  slug: string
}

export default function PostList({ posts }: { posts: Post[] }) {
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

### Checking active links[](https://nextjs.org/docs/app/api-reference/components/link#checking-active-links)
You can use [`usePathname()`](https://nextjs.org/docs/app/api-reference/functions/use-pathname) to determine if a link is active. For example, to add a class to the active link, you can check if the current `pathname` matches the `href` of the link:
app/ui/nav-links.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { usePathname } from 'next/navigation'
import Link from 'next/link'

export function Links() {
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

### Scrolling to an `id`[](https://nextjs.org/docs/app/api-reference/components/link#scrolling-to-an-id)
If you'd like to scroll to a specific `id` on navigation, you can append your URL with a `#` hash link or just pass a hash link to the `href` prop. This is possible since `<Link>` renders to an `<a>` element.
```
<Link href="/dashboard#settings">Settings</Link>

// Output
<a href="/dashboard#settings">Settings</a>
```

> **Good to know** :
>   * Next.js will scroll to the [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page) if it is not visible in the viewport upon navigation.
>

### Replace the URL instead of push[](https://nextjs.org/docs/app/api-reference/components/link#replace-the-url-instead-of-push)
The default behavior of the `Link` component is to `push` a new URL into the `history` stack. You can use the `replace` prop to prevent adding a new entry, as in the following example:
app/page.js
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/about" replace>
      About us
    </Link>
  )
}
```

### Disable scrolling to the top of the page[](https://nextjs.org/docs/app/api-reference/components/link#disable-scrolling-to-the-top-of-the-page)
The default scrolling behavior of `<Link>` in Next.js **is to maintain scroll position** , similar to how browsers handle back and forwards navigation. When you navigate to a new [Page](https://nextjs.org/docs/app/api-reference/file-conventions/page), scroll position will stay the same as long as the Page is visible in the viewport.
However, if the Page is not visible in the viewport, Next.js will scroll to the top of the first Page element. If you'd like to disable this behavior, you can pass `scroll={false}` to the `<Link>` component, or `scroll: false` to `router.push()` or `router.replace()`.
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Link from 'next/link'

export default function Page() {
  return (
    <Link href="/#hashid" scroll={false}>
      Disables scrolling to the top
    </Link>
  )
}
```

Using `router.push()` or `router.replace()`:
```
// useRouter
import { useRouter } from 'next/navigation'

const router = useRouter()

router.push('/dashboard', { scroll: false })
```

### Scroll offset with sticky headers[](https://nextjs.org/docs/app/api-reference/components/link#scroll-offset-with-sticky-headers)
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
### Prefetching links in Proxy[](https://nextjs.org/docs/app/api-reference/components/link#prefetching-links-in-proxy)
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
app/page.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import Link from 'next/link'
import useIsAuthed from './hooks/useIsAuthed' // Your auth hook

export default function Page() {
  const isAuthed = useIsAuthed()
  const path = isAuthed ? '/auth/dashboard' : '/public/dashboard'
  return (
    <Link as="/dashboard" href={path}>
      Dashboard
    </Link>
  )
}
```

### Blocking navigation[](https://nextjs.org/docs/app/api-reference/components/link#blocking-navigation)
You can use the `onNavigate` prop to block navigation when certain conditions are met, such as when a form has unsaved changes. When you need to block navigation across multiple components in your app (like preventing navigation from any link while a form is being edited), React Context provides a clean way to share this blocking state. First, create a context to track the navigation blocking state:
app/contexts/navigation-blocker.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { createContext, useState, useContext } from 'react'

interface NavigationBlockerContextType {
  isBlocked: boolean
  setIsBlocked: (isBlocked: boolean) => void
}

export const NavigationBlockerContext =
  createContext<NavigationBlockerContextType>({
    isBlocked: false,
    setIsBlocked: () => {},
  })

export function NavigationBlockerProvider({
  children,
}: {
  children: React.ReactNode
}) {
  const [isBlocked, setIsBlocked] = useState(false)

  return (
    <NavigationBlockerContext.Provider value={{ isBlocked, setIsBlocked }}>
      {children}
    </NavigationBlockerContext.Provider>
  )
}

export function useNavigationBlocker() {
  return useContext(NavigationBlockerContext)
}
```

Create a form component that uses the context:
app/components/form.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useNavigationBlocker } from '../contexts/navigation-blocker'

export default function Form() {
  const { setIsBlocked } = useNavigationBlocker()

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault()
        setIsBlocked(false)
      }}
      onChange={() => setIsBlocked(true)}
    >
      <input type="text" name="name" />
      <button type="submit">Save</button>
    </form>
  )
}
```

Create a custom Link component that blocks navigation:
app/components/custom-link.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import Link from 'next/link'
import { useNavigationBlocker } from '../contexts/navigation-blocker'

interface CustomLinkProps extends React.ComponentProps<typeof Link> {
  children: React.ReactNode
}

export function CustomLink({ children, ...props }: CustomLinkProps) {
  const { isBlocked } = useNavigationBlocker()

  return (
    <Link
      onNavigate={(e) => {
        if (
          isBlocked &&
          !window.confirm('You have unsaved changes. Leave anyway?')
        ) {
          e.preventDefault()
        }
      }}
      {...props}
    >
      {children}
    </Link>
  )
}
```

Create a navigation component:
app/components/nav.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { CustomLink as Link } from './custom-link'

export default function Nav() {
  return (
    <nav>
      <Link href="/">Home</Link>
      <Link href="/about">About</Link>
    </nav>
  )
}
```

Finally, wrap your app with the `NavigationBlockerProvider` in the root layout and use the components in your page:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { NavigationBlockerProvider } from './contexts/navigation-blocker'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <NavigationBlockerProvider>{children}</NavigationBlockerProvider>
      </body>
    </html>
  )
}
```

Then, use the `Nav` and `Form` components in your page:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Nav from './components/nav'
import Form from './components/form'

export default function Page() {
  return (
    <div>
      <Nav />
      <main>
        <h1>Welcome to the Dashboard</h1>
        <Form />
      </main>
    </div>
  )
}
```

When a user tries to navigate away using `CustomLink` while the form has unsaved changes, they'll be prompted to confirm before leaving.
