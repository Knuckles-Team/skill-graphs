## Examples[](https://nextjs.org/docs/app/api-reference/functions/use-router#examples)
### Router events[](https://nextjs.org/docs/app/api-reference/functions/use-router#router-events)
You can listen for page changes by composing other Client Component hooks like `usePathname` and `useSearchParams`.
app/components/navigation-events.js
```
'use client'

import { useEffect } from 'react'
import { usePathname, useSearchParams } from 'next/navigation'

export function NavigationEvents() {
  const pathname = usePathname()
  const searchParams = useSearchParams()

  useEffect(() => {
    const url = `${pathname}?${searchParams}`
    console.log(url)
    // You can now use the current URL
    // ...
  }, [pathname, searchParams])

  return '...'
}
```

Which can be imported into a layout.
app/layout.js
```
import { Suspense } from 'react'
import { NavigationEvents } from './components/navigation-events'

export default function Layout({ children }) {
  return (
    <html lang="en">
      <body>
        {children}

        <Suspense fallback={null}>
          <NavigationEvents />
        </Suspense>
      </body>
    </html>
  )
}
```

> **Good to know** : `<NavigationEvents>` is wrapped in a [`Suspense` boundary](https://nextjs.org/docs/app/api-reference/file-conventions/loading#examples) because[`useSearchParams()`](https://nextjs.org/docs/app/api-reference/functions/use-search-params) causes client-side rendering up to the closest `Suspense` boundary during [static rendering](https://nextjs.org/docs/app/guides/caching#static-rendering). [Learn more](https://nextjs.org/docs/app/api-reference/functions/use-search-params#behavior).
### Disabling scroll to top[](https://nextjs.org/docs/app/api-reference/functions/use-router#disabling-scroll-to-top)
By default, Next.js will scroll to the top of the page when navigating to a new route. You can disable this behavior by passing `scroll: false` to `router.push()` or `router.replace()`.
app/example-client-component.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useRouter } from 'next/navigation'

export default function Page() {
  const router = useRouter()

  return (
    <button
      type="button"
      onClick={() => router.push('/dashboard', { scroll: false })}
    >
      Dashboard
    </button>
  )
}
```
