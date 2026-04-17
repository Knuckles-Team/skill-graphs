# useLinkStatus
Last updated February 27, 2026
The `useLinkStatus` hook lets you track the **pending** state of a `<Link>`. Use it for subtle, inline feedback, for example a shimmer effect over the clicked link, while navigation completes. Prefer route-level fallbacks with `loading.js`, and prefetching for instant transitions.
`useLinkStatus` is useful when:
  * [Prefetching](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) is disabled or in progress meaning navigation is blocked.
  * The destination route is dynamic **and** doesn't include a [`loading.js`](https://nextjs.org/docs/app/api-reference/file-conventions/loading) file that would allow an instant navigation.


app/hint.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import Link from 'next/link'
import { useLinkStatus } from 'next/link'

function Hint() {
  const { pending } = useLinkStatus()
  return (
    <span aria-hidden className={`link-hint ${pending ? 'is-pending' : ''}`} />
  )
}

export default function Header() {
  return (
    <header>
      <Link href="/dashboard" prefetch={false}>
        <span className="label">Dashboard</span> <Hint />
      </Link>
    </header>
  )
}
```

> **Good to know** :
>   * `useLinkStatus` must be used within a descendant component of a `Link` component
>   * The hook is most useful when `prefetch={false}` is set on the `Link` component
>   * If the linked route has been prefetched, the pending state will be skipped
>   * When clicking multiple links in quick succession, only the last link's pending state is shown
>   * This hook is not supported in the Pages Router and always returns `{ pending: false }`
>   * Inline indicators can easily introduce layout shifts. Prefer a fixed-size, always-rendered hint element and toggle its opacity, or use an animation.
>
