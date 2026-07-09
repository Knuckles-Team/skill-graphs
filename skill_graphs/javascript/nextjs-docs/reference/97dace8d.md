## Manual prefetch[](https://nextjs.org/docs/app/guides/prefetching#manual-prefetch)
To do manual prefetching, import the `useRouter` hook from `next/navigation`, and call `router.prefetch()` to warm routes outside the viewport or in response to analytics, hover, scroll, etc.
```
'use client'

import { useRouter } from 'next/navigation'
import { CustomLink } from '@components/link'

export function PricingCard() {
  const router = useRouter()

  return (
    <div onMouseEnter={() => router.prefetch('/pricing')}>
      {/* other UI elements */}
      <CustomLink href="/pricing">View Pricing</CustomLink>
    </div>
  )
}
```

If the intent is to prefetch a URL when a component loads, see the extending or rejecting a link [example].
