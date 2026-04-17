## Examples[](https://nextjs.org/docs/app/guides/single-page-applications#examples)
Let's explore common patterns used to build SPAs and how Next.js solves them.
### Using React’s `use` within a Context Provider[](https://nextjs.org/docs/app/guides/single-page-applications#using-reacts-use-within-a-context-provider)
We recommend fetching data in a parent component (or layout), returning the Promise, and then unwrapping the value in a Client Component with React’s
Next.js can start data fetching early on the server. In this example, that’s the root layout — the entry point to your application. The server can immediately begin streaming a response to the client.
By “hoisting” your data fetching to the root layout, Next.js starts the specified requests on the server early before any other components in your application. This eliminates client waterfalls and prevents having multiple roundtrips between client and server. It can also significantly improve performance, as your server is closer (and ideally colocated) to where your database is located.
For example, update your root layout to call the Promise, but do _not_ await it.
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { UserProvider } from './user-provider'
import { getUser } from './user' // some server-side function

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  let userPromise = getUser() // do NOT await

  return (
    <html lang="en">
      <body>
        <UserProvider userPromise={userPromise}>{children}</UserProvider>
      </body>
    </html>
  )
}
```

While you can [defer and pass a single Promise](https://nextjs.org/docs/app/getting-started/fetching-data#streaming-data-with-the-use-api) as a prop to a Client Component, we generally see this pattern paired with a React context provider. This enables easier access from Client Components with a custom React Hook.
You can forward a Promise to the React context provider:
app/user-provider.ts
TypeScript
JavaScript TypeScript
```
'use client';

import { createContext, useContext, ReactNode } from 'react';

type User = any;
type UserContextType = {
  userPromise: Promise<User | null>;
};

const UserContext = createContext<UserContextType | null>(null);

export function useUser(): UserContextType {
  let context = useContext(UserContext);
  if (context === null) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
}

export function UserProvider({
  children,
  userPromise
}: {
  children: ReactNode;
  userPromise: Promise<User | null>;
}) {
  return (
    <UserContext.Provider value={{ userPromise }}>
      {children}
    </UserContext.Provider>
  );
}
```

Finally, you can call the `useUser()` custom hook in any Client Component and unwrap the Promise:
app/profile.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { use } from 'react'
import { useUser } from './user-provider'

export function Profile() {
  const { userPromise } = useUser()
  const user = use(userPromise)

  return '...'
}
```

The component that consumes the Promise (e.g. `Profile` above) will be suspended. This enables partial hydration. You can see the streamed and prerendered HTML before JavaScript has finished loading.
### SPAs with SWR[](https://nextjs.org/docs/app/guides/single-page-applications#spas-with-swr)
With SWR 2.3.0 (and React 19+), you can gradually adopt server features alongside your existing SWR-based client data fetching code. This is an abstraction of the above `use()` pattern. This means you can move data fetching between the client and server-side, or use both:
  * **Client-only:** `useSWR(key, fetcher)`
  * **Server-only:** `useSWR(key)` + RSC-provided data
  * **Mixed:** `useSWR(key, fetcher)` + RSC-provided data


For example, wrap your application with `<SWRConfig>` and a `fallback`:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import { SWRConfig } from 'swr'
import { getUser } from './user' // some server-side function

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <SWRConfig
      value={{
        fallback: {
          // We do NOT await getUser() here
          // Only components that read this data will suspend
          '/api/user': getUser(),
        },
      }}
    >
      {children}
    </SWRConfig>
  )
}
```

Because this is a Server Component, `getUser()` can securely read cookies, headers, or talk to your database. No separate API route is needed. Client components below the `<SWRConfig>` can call `useSWR()` with the same key to retrieve the user data. The component code with `useSWR` **does not require any changes** from your existing client-fetching solution.
app/profile.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import useSWR from 'swr'

export function Profile() {
  const fetcher = (url) => fetch(url).then((res) => res.json())
  // The same SWR pattern you already know
  const { data, error } = useSWR('/api/user', fetcher)

  return '...'
}
```

The `fallback` data can be prerendered and included in the initial HTML response, then immediately read in the child components using `useSWR`. SWR’s polling, revalidation, and caching still run **client-side only** , so it preserves all the interactivity you rely on for an SPA.
Since the initial `fallback` data is automatically handled by Next.js, you can now delete any conditional logic previously needed to check if `data` was `undefined`. When the data is loading, the closest `<Suspense>` boundary will be suspended.
| SWR | RSC | RSC + SWR
---|---|---|---
SSR data |  |  |
Streaming while SSR |  |  |
Deduplicate requests |  |  |
Client-side features |  |  |
### SPAs with React Query[](https://nextjs.org/docs/app/guides/single-page-applications#spas-with-react-query)
You can use React Query with Next.js on both the client and server. This enables you to build both strict SPAs, as well as take advantage of server features in Next.js paired with React Query.
Learn more in the
### Rendering components only in the browser[](https://nextjs.org/docs/app/guides/single-page-applications#rendering-components-only-in-the-browser)
Client components are `next build`. If you want to disable prerendering for a Client Component and only load it in the browser environment, you can use [`next/dynamic`](https://nextjs.org/docs/app/guides/lazy-loading#nextdynamic):
```
import dynamic from 'next/dynamic'

const ClientOnlyComponent = dynamic(() => import('./component'), {
  ssr: false,
})
```

This can be useful for third-party libraries that rely on browser APIs like `window` or `document`. You can also add a `useEffect` that checks for the existence of these APIs, and if they do not exist, return `null` or a loading state which would be prerendered.
### Shallow routing on the client[](https://nextjs.org/docs/app/guides/single-page-applications#shallow-routing-on-the-client)
If you are migrating from a strict SPA like [Create React App](https://nextjs.org/docs/app/guides/migrating/from-create-react-app) or [Vite](https://nextjs.org/docs/app/guides/migrating/from-vite), you might have existing code which shallow routes to update the URL state. This can be useful for manual transitions between views in your application _without_ using the default Next.js file-system routing.
Next.js allows you to use the native
`pushState` and `replaceState` calls integrate into the Next.js Router, allowing you to sync with [`usePathname`](https://nextjs.org/docs/app/api-reference/functions/use-pathname) and [`useSearchParams`](https://nextjs.org/docs/app/api-reference/functions/use-search-params).
```
'use client'

import { useSearchParams } from 'next/navigation'

export default function SortProducts() {
  const searchParams = useSearchParams()

  function updateSorting(sortOrder: string) {
    const urlSearchParams = new URLSearchParams(searchParams.toString())
    urlSearchParams.set('sort', sortOrder)
    window.history.pushState(null, '', `?${urlSearchParams.toString()}`)
  }

  return (
    <>
      <button onClick={() => updateSorting('asc')}>Sort Ascending</button>
      <button onClick={() => updateSorting('desc')}>Sort Descending</button>
    </>
  )
}
```

Learn more about how [routing and navigation](https://nextjs.org/docs/app/getting-started/linking-and-navigating#how-navigation-works) work in Next.js.
### Using Server Actions in Client Components[](https://nextjs.org/docs/app/guides/single-page-applications#using-server-actions-in-client-components)
You can progressively adopt Server Actions while still using Client Components. This allows you to remove boilerplate code to call an API route, and instead use React features like `useActionState` to handle loading and error states.
For example, create your first Server Action:
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

export async function create() {}
```

You can import and use a Server Action from the client, similar to calling a JavaScript function. You do not need to create an API endpoint manually:
app/button.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { create } from './actions'

export function Button() {
  return <button onClick={() => create()}>Create</button>
}
```

Learn more about [mutating data with Server Actions](https://nextjs.org/docs/app/getting-started/updating-data).
