## What can make transitions slow?[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#what-can-make-transitions-slow)
These Next.js optimizations make navigation fast and responsive. However, under certain conditions, transitions can still _feel_ slow. Here are some common causes and how to improve the user experience:
### Dynamic routes without `loading.tsx`[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#dynamic-routes-without-loadingtsx)
When navigating to a dynamic route, the client must wait for the server response before showing the result. This can give the users the impression that the app is not responding.
We recommend adding `loading.tsx` to dynamic routes to enable partial prefetching, trigger immediate navigation, and display a loading UI while the route renders.
app/blog/[slug]/loading.tsx
TypeScript
JavaScript TypeScript
```
export default function Loading() {
  return <LoadingSkeleton />
}
```

> **Good to know** : In development mode, you can use the Next.js Devtools to identify if the route is static or dynamic. See [`devIndicators`](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators) for more information.
### Dynamic segments without `generateStaticParams`[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#dynamic-segments-without-generatestaticparams)
If a [dynamic segment](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) could be prerendered but isn't because it's missing [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params), the route will fallback to dynamic rendering at request time.
Ensure the route is statically generated at build time by adding `generateStaticParams`:
app/blog/[slug]/page.tsx
TypeScript
JavaScript TypeScript
```
export async function generateStaticParams() {
  const posts = await fetch('https://.../posts').then((res) => res.json())

  return posts.map((post) => ({
    slug: post.slug,
  }))
}

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  // ...
}
```

### Slow networks[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#slow-networks)
On slow or unstable networks, prefetching may not finish before the user clicks a link. This can affect both static and dynamic routes. In these cases, the `loading.js` fallback may not appear immediately because it hasn't been prefetched yet.
To improve perceived performance, you can use the [`useLinkStatus` hook](https://nextjs.org/docs/app/api-reference/functions/use-link-status) to show immediate feedback while the transition is in progress.
app/ui/loading-indicator.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useLinkStatus } from 'next/link'

export default function LoadingIndicator() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}
```

You can "debounce" the hint by adding an initial animation delay (e.g. 100ms) and starting as invisible (e.g. `opacity: 0`). This means the loading indicator will only be shown if the navigation takes longer than the specified delay. See the [`useLinkStatus` reference](https://nextjs.org/docs/app/api-reference/functions/use-link-status#gracefully-handling-fast-navigation) for a CSS example.
> **Good to know** : You can use other visual feedback patterns like a progress bar. View an example
### Disabling prefetching[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#disabling-prefetching)
You can opt out of prefetching by setting the `prefetch` prop to `false` on the `<Link>` component. This is useful to avoid unnecessary usage of resources when rendering large lists of links (e.g. an infinite scroll table).
```
<Link prefetch={false} href="/blog">
  Blog
</Link>
```

However, disabling prefetching comes with trade-offs:
  * **Static routes** will only be fetched when the user clicks the link.
  * **Dynamic routes** will need to be rendered on the server first before the client can navigate to it.


To reduce resource usage without fully disabling prefetch, you can prefetch only on hover. This limits prefetching to routes the user is more _likely_ to visit, rather than all links in the viewport.
app/ui/hover-prefetch-link.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import Link from 'next/link'
import { useState } from 'react'

function HoverPrefetchLink({
  href,
  children,
}: {
  href: string
  children: React.ReactNode
}) {
  const [active, setActive] = useState(false)

  return (
    <Link
      href={href}
      prefetch={active ? null : false}
      onMouseEnter={() => setActive(true)}
    >
      {children}
    </Link>
  )
}
```

### Hydration not completed[](https://nextjs.org/docs/app/getting-started/linking-and-navigating#hydration-not-completed)
`<Link>` is a Client Component and must be hydrated before it can prefetch routes. On the initial visit, large JavaScript bundles can delay hydration, preventing prefetching from starting right away.
React mitigates this with Selective Hydration and you can further improve this by:
  * Using the [`@next/bundle-analyzer`](https://nextjs.org/docs/app/guides/package-bundling#nextbundle-analyzer-for-webpack) plugin to identify and reduce bundle size by removing large dependencies.
  * Moving logic from the client to the server where possible. See the [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) docs for guidance.
