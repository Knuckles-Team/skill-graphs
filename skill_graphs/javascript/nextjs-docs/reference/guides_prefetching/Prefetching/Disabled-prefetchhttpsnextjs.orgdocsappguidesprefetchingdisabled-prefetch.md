## Disabled prefetch[](https://nextjs.org/docs/app/guides/prefetching#disabled-prefetch)
You can fully disable prefetching for certain routes for more fine-grained control over resource consumption.
```
'use client'

import Link, { LinkProps } from 'next/link'

function NoPrefetchLink({
  prefetch,
  ...rest
}: LinkProps & { children: React.ReactNode }) {
  return <Link {...rest} prefetch={false} />
}
```

For example, you may still want to have consistent usage of `<Link>` in your application, but links in your footer might not need to be prefetched when entering the viewport.
