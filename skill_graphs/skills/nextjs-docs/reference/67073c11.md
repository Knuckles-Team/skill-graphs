## Defer rendering to request time[](https://nextjs.org/docs/app/getting-started/cache-components#defer-rendering-to-request-time)
During prerendering, when Next.js encounters work it can't complete (like network requests, accessing request data, or async operations), it requires you to explicitly handle it. To defer rendering to request time, a parent component must provide fallback UI using a Suspense boundary. The fallback becomes part of the static shell while the actual content resolves at request time.
Place Suspense boundaries as close as possible to the components that need them. This maximizes the amount of content in the static shell, since everything outside the boundary can still prerender normally.
> **Good to know** : With Suspense boundaries, multiple dynamic sections can render in parallel rather than blocking each other, reducing total load time.
### Dynamic content[](https://nextjs.org/docs/app/getting-started/cache-components#dynamic-content)
External systems provide content asynchronously, which often takes an unpredictable time to resolve and may even fail. This is why prerendering doesn't execute them automatically.
In general, when you need the latest data from the source on each request (like real-time feeds or personalized content), defer rendering by providing fallback UI with a Suspense boundary.
For example, the `DynamicContent` component below uses multiple operations that are not automatically prerendered.
page.tsx
```
import { Suspense } from 'react'
import fs from 'node:fs/promises'

async function DynamicContent() {
  // Network request
  const data = await fetch('https://api.example.com/data')

  // Database query
  const users = await db.query('SELECT * FROM users')

  // Async file system operation
  const file = await fs.readFile('..', 'utf-8')

  // Simulating external system delay
  await new Promise((resolve) => setTimeout(resolve, 100))

  return <div>Not in the static shell</div>
}
```

To use `DynamicContent` within a page, wrap it in `<Suspense>` to define fallback UI:
page.tsx
```
export default async function Page(props) {
  return (
    <>
      <h1>Part of the static shell</h1>
      {/* <p>Loading..</p> is part of the static shell */}
      <Suspense fallback={<p>Loading..</p>}>
        <DynamicContent />
        <div>Sibling excluded from static shell</div>
      </Suspense>
    </>
  )
}
```

Prerendering stops at the `fetch` request. The request itself is not started, and any code after it is not executed.
The fallback (`<p>Loading...</p>`) is included in the static shell, while the component's content streams at request time.
In this example, since all operations (network request, database query, file read, and timeout) run sequentially within the same component, the content won't appear until they all complete.
> **Good to know** : For dynamic content that doesn't change frequently, you can use `use cache` to include the dynamic data in the static shell instead of streaming it. See the [during prerendering](https://nextjs.org/docs/app/getting-started/cache-components#during-prerendering) section for an example.
### Runtime data[](https://nextjs.org/docs/app/getting-started/cache-components#runtime-data)
A specific type of dynamic data that requires request context, only available when a user makes a request.
  * [`cookies()`](https://nextjs.org/docs/app/api-reference/functions/cookies) - User's cookie data
  * [`headers()`](https://nextjs.org/docs/app/api-reference/functions/headers) - Request headers
  * [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) - URL query parameters
  * [`params`](https://nextjs.org/docs/app/api-reference/file-conventions/page#params-optional) - Dynamic route parameters (unless at least one sample is provided via [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)). See [Dynamic Routes with Cache Components](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#with-cache-components) for detailed patterns.


page.tsx
```
import { cookies, headers } from 'next/headers'
import { Suspense } from 'react'

async function RuntimeData({ searchParams }) {
  // Accessing request data
  const cookieStore = await cookies()
  const headerStore = await headers()
  const search = await searchParams

  return <div>Not in the static shell</div>
}
```

To use the `RuntimeData` component, wrap it in a `<Suspense>` boundary:
page.tsx
```
export default async function Page(props) {
  return (
    <>
      <h1>Part of the static shell</h1>
      {/* <p>Loading..</p> is part of the static shell */}
      <Suspense fallback={<p>Loading..</p>}>
        <RuntimeData searchParams={props.searchParams} />
        <div>Sibling excluded from static shell</div>
      </Suspense>
    </>
  )
}
```

Use [`connection()`](https://nextjs.org/docs/app/api-reference/functions/connection) if you need to defer to request time without accessing any of the runtime APIs above.
> **Good to know** : Runtime data cannot be cached with `use cache` because it requires request context. Components that access runtime APIs must always be wrapped in `<Suspense>`. However, you can extract values from runtime data and pass them as arguments to cached functions. See the [with runtime data](https://nextjs.org/docs/app/getting-started/cache-components#with-runtime-data) section for an example.
One approach for reading runtime data like cookies without blocking the static shell is to pass a promise to a client context provider. See [Sharing data with context and React.cache](https://nextjs.org/docs/app/getting-started/server-and-client-components#sharing-data-with-context-and-reactcache) for an example.
> **Good to know:** `React.cache` operates in an isolated scope inside `use cache` boundaries. See [React.cache isolation](https://nextjs.org/docs/app/api-reference/directives/use-cache#reactcache-isolation) for more information.
### Non-deterministic operations[](https://nextjs.org/docs/app/getting-started/cache-components#non-deterministic-operations)
Operations like `Math.random()`, `Date.now()`, or `crypto.randomUUID()` produce different values each time they execute. To ensure these run at request time (generating unique values per request), Cache Components requires you to explicitly signal this intent by calling these operations after dynamic or runtime data access.
```
import { connection } from 'next/server'
import { Suspense } from 'react'

async function UniqueContent() {
  // Explicitly defer to request time
  await connection()

  // Non-deterministic operations
  const random = Math.random()
  const now = Date.now()
  const date = new Date()
  const uuid = crypto.randomUUID()
  const bytes = crypto.getRandomValues(new Uint8Array(16))

  return (
    <div>
      <p>{random}</p>
      <p>{now}</p>
      <p>{date.getTime()}</p>
      <p>{uuid}</p>
      <p>{bytes}</p>
    </div>
  )
}
```

Because the `UniqueContent` component defers to request time, to use it within a route, it must be wrapped in `<Suspense>`:
page.tsx
```
export default async function Page() {
  return (
    // <p>Loading..</p> is part of the static shell
    <Suspense fallback={<p>Loading..</p>}>
      <UniqueContent />
    </Suspense>
  )
}
```

Every incoming request would see different random numbers, date, etc.
> **Good to know** : You can cache non-deterministic operations with `use cache`. See the [with non-deterministic operations](https://nextjs.org/docs/app/getting-started/cache-components#with-non-deterministic-operations) section for examples.
