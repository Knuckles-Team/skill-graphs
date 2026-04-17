## Examples[](https://nextjs.org/docs/app/api-reference/directives/use-cache#examples)
### Caching an entire route with `use cache`[](https://nextjs.org/docs/app/api-reference/directives/use-cache#caching-an-entire-route-with-use-cache)
To pre-render an entire route, add `use cache` to the top of **both** the `layout` and `page` files. Each of these segments are treated as separate entry points in your application, and will be cached independently.
app/layout.tsx
TypeScript
JavaScript TypeScript
```
'use cache'

export default async function Layout({ children }: { children: ReactNode }) {
  return <div>{children}</div>
}
```

Any components imported and nested in `page` file are part of the cache output associated with the `page`.
app/page.tsx
TypeScript
JavaScript TypeScript
```
'use cache'

async function Users() {
  const users = await fetch('/api/users')
  // loop through users
}

export default async function Page() {
  return (
    <main>
      <Users />
    </main>
  )
}
```

> **Good to know** :
>   * If `use cache` is added only to the `layout` or the `page`, only that route segment and any components imported into it will be cached.
>

### Caching a component's output with `use cache`[](https://nextjs.org/docs/app/api-reference/directives/use-cache#caching-a-components-output-with-use-cache)
You can use `use cache` at the component level to cache any fetches or computations performed within that component. The cache entry will be reused as long as the serialized props produce the same value in each instance.
app/components/bookings.tsx
TypeScript
JavaScript TypeScript
```
export async function Bookings({ type = 'haircut' }: BookingsProps) {
  'use cache'
  async function getBookingsData() {
    const data = await fetch(`/api/bookings?type=${encodeURIComponent(type)}`)
    return data
  }
  return //...
}

interface BookingsProps {
  type: string
}
```

### Caching function output with `use cache`[](https://nextjs.org/docs/app/api-reference/directives/use-cache#caching-function-output-with-use-cache)
Since you can add `use cache` to any asynchronous function, you aren't limited to caching components or routes only. You might want to cache a network request, a database query, or a slow computation.
app/actions.ts
TypeScript
JavaScript TypeScript
```
export async function getData() {
  'use cache'

  const data = await fetch('/api/data')
  return data
}
```

### Interleaving[](https://nextjs.org/docs/app/api-reference/directives/use-cache#interleaving)
In React, composition with `children` or slots is a well-known pattern for building flexible components. When using `use cache`, you can continue to compose your UI in this way. Anything included as `children`, or other compositional slots, in the returned JSX will be passed through the cached component without affecting its cache entry.
As long as you don't directly reference any of the JSX slots inside the body of the cacheable function itself, their presence in the returned output won't affect the cache entry.
app/page.tsx
TypeScript
JavaScript TypeScript
```
export default async function Page() {
  const uncachedData = await getData()
  return (
    // Pass compositional slots as props, e.g. header and children
    <CacheComponent header={<h1>Home</h1>}>
      {/* DynamicComponent is provided as the children slot */}
      <DynamicComponent data={uncachedData} />
    </CacheComponent>
  )
}

async function CacheComponent({
  header, // header: a compositional slot, injected as a prop
  children, // children: another slot for nested composition
}: {
  header: ReactNode
  children: ReactNode
}) {
  'use cache'
  const cachedData = await fetch('/api/cached-data')
  return (
    <div>
      {header}
      <PrerenderedComponent data={cachedData} />
      {children}
    </div>
  )
}
```

You can also pass Server Actions through cached components to Client Components without invoking them inside the cacheable function.
app/page.tsx
TypeScript
JavaScript TypeScript
```
import ClientComponent from './ClientComponent'

export default async function Page() {
  const performUpdate = async () => {
    'use server'
    // Perform some server-side update
    await db.update(...)
  }

  return <CachedComponent performUpdate={performUpdate} />
}

async function CachedComponent({
  performUpdate,
}: {
  performUpdate: () => Promise<void>
}) {
  'use cache'
  // Do not call performUpdate here
  return <ClientComponent action={performUpdate} />
}
```

app/ClientComponent.tsx
TypeScript
JavaScript TypeScript
```
'use client'

export default function ClientComponent({
  action,
}: {
  action: () => Promise<void>
}) {
  return <button onClick={action}>Update</button>
}
```
