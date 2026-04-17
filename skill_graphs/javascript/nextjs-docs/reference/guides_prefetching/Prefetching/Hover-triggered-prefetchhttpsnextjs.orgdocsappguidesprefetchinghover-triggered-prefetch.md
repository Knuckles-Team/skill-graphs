## Hover-triggered prefetch[](https://nextjs.org/docs/app/guides/prefetching#hover-triggered-prefetch)
> **Proceed with caution:** Extending `Link` opts you into maintaining prefetching, cache invalidation, and accessibility concerns. Proceed only if defaults are insufficient.
Next.js tries to do the right prefetching by default, but power users can eject and modify based on their needs. You have the control between performance and resource consumption.
For example, you might have to only trigger prefetches on hover, instead of when entering the viewport (the default behavior):
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

`prefetch={null}` restores default (static) prefetching once the user shows intent.
