## Troubleshooting[](https://nextjs.org/docs/app/api-reference/directives/use-cache#troubleshooting)
### Debugging cache behavior[](https://nextjs.org/docs/app/api-reference/directives/use-cache#debugging-cache-behavior)
#### Verbose logging[](https://nextjs.org/docs/app/api-reference/directives/use-cache#verbose-logging)
Set `NEXT_PRIVATE_DEBUG_CACHE=1` for verbose cache logging:
```
NEXT_PRIVATE_DEBUG_CACHE=1 npm run dev
# or for production
NEXT_PRIVATE_DEBUG_CACHE=1 npm run start
```

> **Good to know:** This environment variable also logs ISR and other caching mechanisms. See [Verifying correct production behavior](https://nextjs.org/docs/app/guides/incremental-static-regeneration#verifying-correct-production-behavior) for more details.
#### Console log replays[](https://nextjs.org/docs/app/api-reference/directives/use-cache#console-log-replays)
In development, console logs from cached functions appear with a `Cache` prefix.
### Build Hangs (Cache Timeout)[](https://nextjs.org/docs/app/api-reference/directives/use-cache#build-hangs-cache-timeout)
If your build hangs, you're accessing Promises that resolve to dynamic or runtime data, created outside a `use cache` boundary. The cached function waits for data that can't resolve during the build, causing a timeout after 50 seconds.
When the build timeouts you'll see this error message:
> Error: Filling a cache during prerender timed out, likely because request-specific arguments such as params, searchParams, cookies() or dynamic data were used inside "use cache".
Common ways this happens: passing such Promises as props, accessing them via closure, or retrieving them from shared storage (Maps).
> **Good to know:** Directly calling `cookies()` or `headers()` inside `use cache` fails immediately with a [different error](https://nextjs.org/docs/messages/next-request-in-use-cache), not a timeout.
**Passing runtime data Promises as props:**
app/page.tsx
```
import { cookies } from 'next/headers'
import { Suspense } from 'react'

export default function Page() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Dynamic />
    </Suspense>
  )
}

async function Dynamic() {
  const cookieStore = cookies()
  return <Cached promise={cookieStore} /> // Build hangs
}

async function Cached({ promise }: { promise: Promise<unknown> }) {
  'use cache'
  const data = await promise // Waits for runtime data during build
  return <p>..</p>
}
```

Await the `cookies` store in the `Dynamic` component, and pass a cookie value to the `Cached` component.
**Shared deduplication storage:**
app/page.tsx
```
// Problem: Map stores dynamic Promises, accessed by cached code
import { Suspense } from 'react'

const cache = new Map<string, Promise<string>>()

export default function Page() {
  return (
    <>
      <Suspense fallback={<div>Loading...</div>}>
        <Dynamic id="data" />
      </Suspense>
      <Cached id="data" />
    </>
  )
}

async function Dynamic({ id }: { id: string }) {
  // Stores dynamic Promise in shared Map
  cache.set(
    id,
    fetch(`https://api.example.com/${id}`).then((r) => r.text())
  )
  return <p>Dynamic</p>
}

async function Cached({ id }: { id: string }) {
  'use cache'
  return <p>{await cache.get(id)}</p> // Build hangs - retrieves dynamic Promise
}
```

Use Next.js's built-in `fetch()` deduplication or use separate Maps for cached and uncached contexts.
