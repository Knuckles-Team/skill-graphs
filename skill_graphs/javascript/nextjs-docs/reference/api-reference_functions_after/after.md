# after
Last updated February 27, 2026
`after` allows you to schedule work to be executed after a response (or prerender) is finished. This is useful for tasks and other side effects that should not block the response, such as logging and analytics.
It can be used in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) (including [`generateMetadata`](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)), [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data), [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route), and [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy).
The function accepts a callback that will be executed after the response (or prerender) is finished:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { after } from 'next/server'
// Custom logging function
import { log } from '@/app/utils'

export default function Layout({ children }: { children: React.ReactNode }) {
  after(() => {
    // Execute after the layout is rendered and sent to the user
    log()
  })
  return <>{children}</>
}
```

> **Good to know:** `after` is not a [Dynamic API](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) and calling it does not cause a route to become dynamic. If it's used within a static page, the callback will execute at build time, or whenever a page is revalidated.
