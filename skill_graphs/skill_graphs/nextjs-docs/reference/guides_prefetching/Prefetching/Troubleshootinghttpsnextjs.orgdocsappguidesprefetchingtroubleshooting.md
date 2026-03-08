## Troubleshooting[](https://nextjs.org/docs/app/guides/prefetching#troubleshooting)
### Triggering unwanted side-effects during prefetching[](https://nextjs.org/docs/app/guides/prefetching#triggering-unwanted-side-effects-during-prefetching)
If your layouts or pages are not
To avoid this, you should move side-effects to a `useEffect` hook or a Server Action triggered from a Client Component.
**Before** :
app/dashboard/layout.tsx
TypeScript
JavaScript TypeScript
```
import { trackPageView } from '@/lib/analytics'

export default function Layout({ children }: { children: React.ReactNode }) {
  // This runs during prefetch
  trackPageView()

  return <div>{children}</div>
}
```

**After** :
app/ui/analytics-tracker.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useEffect } from 'react'
import { trackPageView } from '@/lib/analytics'

export function AnalyticsTracker() {
  useEffect(() => {
    trackPageView()
  }, [])

  return null
}
```

app/dashboard/layout.tsx
TypeScript
JavaScript TypeScript
```
import { AnalyticsTracker } from '@/app/ui/analytics-tracker'

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <AnalyticsTracker />
      {children}
    </div>
  )
}
```

### Preventing too many prefetches[](https://nextjs.org/docs/app/guides/prefetching#preventing-too-many-prefetches)
Next.js automatically prefetches links in the viewport when using the `<Link>` component.
There may be cases where you want to prevent this to avoid unnecessary usage of resources, such as when rendering a large list of links (e.g. an infinite scroll table).
You can disable prefetching by setting the `prefetch` prop of the `<Link>` component to `false`.
app/ui/no-prefetch-link.tsx
TypeScript
JavaScript TypeScript
```
<Link prefetch={false} href={`/blog/${post.id}`}>
  {post.title}
</Link>
```

However, this means static routes will only be fetched on click, and dynamic routes will wait for the server to render before navigating.
To reduce resource usage without disabling prefetch entirely, you can defer prefetching until the user hovers over a link. This targets only links the user is likely to visit.
app/ui/hover-prefetch-link.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import Link from 'next/link'
import { useState } from 'react'

export function HoverPrefetchLink({
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

[PreviousPackage Bundling](https://nextjs.org/docs/app/guides/package-bundling)[NextProduction](https://nextjs.org/docs/app/guides/production-checklist)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
