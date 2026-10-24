## Examples[](https://nextjs.org/docs/app/api-reference/functions/after#examples)
### With request APIs[](https://nextjs.org/docs/app/api-reference/functions/after#with-request-apis)
Whether you can use request APIs like [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) and [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers) inside `after` depends on where `after` is called from.
#### In Route Handlers and Server Functions[](https://nextjs.org/docs/app/api-reference/functions/after#in-route-handlers-and-server-functions)
You can call `cookies` and `headers` directly inside the `after` callback when used in [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) and [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data). This is useful for logging activity after a mutation or API request. For example:
app/api/route.ts
TypeScript
JavaScript TypeScript
```
import { after } from 'next/server'
import { cookies, headers } from 'next/headers'
import { logUserAction } from '@/app/utils'

export async function POST(request: Request) {
  // Perform mutation
  // ...

  // Log user activity for analytics
  after(async () => {
    const userAgent = (await headers()).get('user-agent') || 'unknown'
    const sessionCookie =
      (await cookies()).get('session-id')?.value || 'anonymous'

    logUserAction({ sessionCookie, userAgent })
  })

  return new Response(JSON.stringify({ status: 'success' }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  })
}
```

#### In Server Components (pages and layouts)[](https://nextjs.org/docs/app/api-reference/functions/after#in-server-components-pages-and-layouts)
[Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) (including pages, layouts, and `generateMetadata`) **cannot** use `cookies`, `headers`, or other [Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) inside `after`. This is because Next.js needs to know which part of the component tree accesses request data to support [Partial Prerendering](https://nextjs.org/docs/app/glossary#partial-prerendering-ppr) and [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components), but `after` runs after React's rendering lifecycle.
If you need request data inside an `after` callback in a Server Component, read it beforehand and pass the values in:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { after } from 'next/server'
import { cookies, headers } from 'next/headers'
import { logUserAction } from '@/app/utils'

export default async function Page() {
  // Read request data before `after` — this is allowed
  // These calls will be read during the component's rendering lifecycle
  const userAgent = (await headers()).get('user-agent') || 'unknown'
  const sessionCookie =
    (await cookies()).get('session-id')?.value || 'anonymous'

  after(() => {
    // Use the values read above
    logUserAction({ sessionCookie, userAgent })
  })

  return <h1>My Page</h1>
}
```

Calling `cookies()` or `headers()` inside the `after` callback in a Server Component will throw a runtime error.
#### With Cache Components[](https://nextjs.org/docs/app/api-reference/functions/after#with-cache-components)
When using [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components), components that access request data like `cookies` or `headers` must be wrapped in
You can combine this pattern with `after` by reading request data in a dynamic component and passing it into `after`:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { Suspense } from 'react'
import { after } from 'next/server'
import { cookies } from 'next/headers'
import { logUserAction } from '@/app/utils'

export default function Page() {
  return (
    <>
      <h1>Part of the static shell</h1>
      <Suspense fallback={<p>Loading...</p>}>
        <DynamicContent />
      </Suspense>
    </>
  )
}

async function DynamicContent() {
  const sessionCookie =
    (await cookies()).get('session-id')?.value || 'anonymous'

  // Schedule work after the response is sent
  after(() => {
    logUserAction({ sessionCookie })
  })

  return <p>Your session: {sessionCookie}</p>
}
```

In this example, `<h1>` and the `<Suspense>` fallback are included in the static shell. `DynamicContent` reads the cookie during rendering and passes it into `after` via closure. Since `cookies()` is called _outside_ the `after` callback (during the component's render), this works correctly.
