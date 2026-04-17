## Examples[](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples)
### Using Client Components[](https://nextjs.org/docs/app/getting-started/server-and-client-components#using-client-components)
You can create a Client Component by adding the
app/ui/counter.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>{count} likes</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  )
}
```

`"use client"` is used to declare a **boundary** between the Server and Client module graphs (trees).
Once a file is marked with `"use client"`, **all its imports and child components are considered part of the client bundle**. This means you don't need to add the directive to every component that is intended for the client.
### Reducing JS bundle size[](https://nextjs.org/docs/app/getting-started/server-and-client-components#reducing-js-bundle-size)
To reduce the size of your client JavaScript bundles, add `'use client'` to specific interactive components instead of marking large parts of your UI as Client Components.
For example, the `<Layout>` component contains mostly static elements like a logo and navigation links, but includes an interactive search bar. `<Search />` is interactive and needs to be a Client Component, however, the rest of the layout can remain a Server Component.
app/layout.tsx
TypeScript
JavaScript TypeScript
```
// Client Component
import Search from './search'
// Server Component
import Logo from './logo'

// Layout is a Server Component by default
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <nav>
        <Logo />
        <Search />
      </nav>
      <main>{children}</main>
    </>
  )
}
```

app/ui/search.tsx
TypeScript
JavaScript TypeScript
```
'use client'

export default function Search() {
  // ...
}
```

### Passing data from Server to Client Components[](https://nextjs.org/docs/app/getting-started/server-and-client-components#passing-data-from-server-to-client-components)
You can pass data from Server Components to Client Components using props.
app/[id]/page.tsx
TypeScript
JavaScript TypeScript
```
import LikeButton from '@/app/ui/like-button'
import { getPost } from '@/lib/data'

export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const post = await getPost(id)

  return <LikeButton likes={post.likes} />
}
```

app/ui/like-button.tsx
TypeScript
JavaScript TypeScript
```
'use client'

export default function LikeButton({ likes }: { likes: number }) {
  // ...
}
```

Alternatively, you can stream data from a Server Component to a Client Component with the [example](https://nextjs.org/docs/app/getting-started/fetching-data#streaming-data-with-the-use-api).
> **Good to know** : Props passed to Client Components need to be
### Interleaving Server and Client Components[](https://nextjs.org/docs/app/getting-started/server-and-client-components#interleaving-server-and-client-components)
You can pass Server Components as a prop to a Client Component. This allows you to visually nest server-rendered UI within Client components.
A common pattern is to use `children` to create a _slot_ in a `<ClientComponent>`. For example, a `<Cart>` component that fetches data on the server, inside a `<Modal>` component that uses client state to toggle visibility.
app/ui/modal.tsx
TypeScript
JavaScript TypeScript
```
'use client'

export default function Modal({ children }: { children: React.ReactNode }) {
  return <div>{children}</div>
}
```

Then, in a parent Server Component (e.g.`<Page>`), you can pass a `<Cart>` as the child of the `<Modal>`:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Modal from './ui/modal'
import Cart from './ui/cart'

export default function Page() {
  return (
    <Modal>
      <Cart />
    </Modal>
  )
}
```

In this pattern, all Server Components will be rendered on the server ahead of time, including those as props. The resulting RSC payload will contain references of where Client Components should be rendered within the component tree.
### Context providers[](https://nextjs.org/docs/app/getting-started/server-and-client-components#context-providers)
To use context, create a Client Component that accepts `children`:
app/theme-provider.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { createContext } from 'react'

export const ThemeContext = createContext({})

export default function ThemeProvider({
  children,
}: {
  children: React.ReactNode
}) {
  return <ThemeContext.Provider value="dark">{children}</ThemeContext.Provider>
}
```

Then, import it into a Server Component (e.g. `layout`):
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import ThemeProvider from './theme-provider'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  )
}
```

Your Server Component will now be able to directly render your provider, and all other Client Components throughout your app will be able to consume this context.
> **Good to know** : You should render providers as deep as possible in the tree – notice how `ThemeProvider` only wraps `{children}` instead of the entire `<html>` document. This makes it easier for Next.js to optimize the static parts of your Server Components.
### Sharing data with context and React.cache[](https://nextjs.org/docs/app/getting-started/server-and-client-components#sharing-data-with-context-and-reactcache)
You can share fetched data across both Server and Client Components by combining
Create a cached function that fetches data:
app/lib/user.ts
TypeScript
JavaScript TypeScript
```
import { cache } from 'react'

export const getUser = cache(async () => {
  const res = await fetch('https://api.example.com/user')
  return res.json()
})
```

Create a context provider that stores the promise:
app/user-provider.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { createContext } from 'react'

type User = {
  id: string
  name: string
}

export const UserContext = createContext<Promise<User> | null>(null)

export default function UserProvider({
  children,
  userPromise,
}: {
  children: React.ReactNode
  userPromise: Promise<User>
}) {
  return <UserContext value={userPromise}>{children}</UserContext>
}
```

In a layout, pass the promise to the provider without awaiting:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import UserProvider from './user-provider'
import { getUser } from './lib/user'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const userPromise = getUser() // Don't await

  return (
    <html>
      <body>
        <UserProvider userPromise={userPromise}>{children}</UserProvider>
      </body>
    </html>
  )
}
```

Client Components use `<Suspense>` for fallback UI:
app/ui/profile.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { use, useContext } from 'react'
import { UserContext } from '../user-provider'

export function Profile() {
  const userPromise = useContext(UserContext)
  if (!userPromise) {
    throw new Error('useContext must be used within a UserProvider')
  }
  const user = use(userPromise)
  return <p>Welcome, {user.name}</p>
}
```

app/page.tsx
TypeScript
JavaScript TypeScript
```
import { Suspense } from 'react'
import { Profile } from './ui/profile'

export default function Page() {
  return (
    <Suspense fallback={<div>Loading profile...</div>}>
      <Profile />
    </Suspense>
  )
}
```

Server Components can also call `getUser()` directly:
app/dashboard/page.tsx
TypeScript
JavaScript TypeScript
```
import { getUser } from '../lib/user'

export default async function DashboardPage() {
  const user = await getUser() // Cached - same request, no duplicate fetch
  return <h1>Dashboard for {user.name}</h1>
}
```

Since `getUser` is wrapped with `React.cache`, multiple calls within the same request return the same memoized result, whether called directly in Server Components or resolved via context in Client Components.
> **Good to know** : `React.cache` is scoped to the current request only. Each request gets its own memoization scope with no sharing between requests.
### Third-party components[](https://nextjs.org/docs/app/getting-started/server-and-client-components#third-party-components)
When using a third-party component that relies on client-only features, you can wrap it in a Client Component to ensure it works as expected.
For example, the `<Carousel />` can be imported from the `acme-carousel` package. This component uses `useState`, but it doesn't yet have the `"use client"` directive.
If you use `<Carousel />` within a Client Component, it will work as expected:
app/gallery.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useState } from 'react'
import { Carousel } from 'acme-carousel'

export default function Gallery() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div>
      <button onClick={() => setIsOpen(true)}>View pictures</button>
      {/* Works, since Carousel is used within a Client Component */}
      {isOpen && <Carousel />}
    </div>
  )
}
```

However, if you try to use it directly within a Server Component, you'll see an error. This is because Next.js doesn't know `<Carousel />` is using client-only features.
To fix this, you can wrap third-party components that rely on client-only features in your own Client Components:
app/carousel.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { Carousel } from 'acme-carousel'

export default Carousel
```

Now, you can use `<Carousel />` directly within a Server Component:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import Carousel from './carousel'

export default function Page() {
  return (
    <div>
      <p>View pictures</p>
      {/*  Works, since Carousel is a Client Component */}
      <Carousel />
    </div>
  )
}
```

> **Advice for Library Authors**
> If you’re building a component library, add the `"use client"` directive to entry points that rely on client-only features. This lets your users import components into Server Components without needing to create wrappers.
> It's worth noting some bundlers might strip out `"use client"` directives. You can find an example of how to configure esbuild to include the `"use client"` directive in the
### Preventing environment poisoning[](https://nextjs.org/docs/app/getting-started/server-and-client-components#preventing-environment-poisoning)
JavaScript modules can be shared between both Server and Client Components modules. This means it's possible to accidentally import server-only code into the client. For example, consider the following function:
lib/data.ts
TypeScript
JavaScript TypeScript
```
export async function getData() {
  const res = await fetch('https://external-service.com/data', {
    headers: {
      authorization: process.env.API_KEY,
    },
  })

  return res.json()
}
```

This function contains an `API_KEY` that should never be exposed to the client.
In Next.js, only environment variables prefixed with `NEXT_PUBLIC_` are included in the client bundle. If variables are not prefixed, Next.js replaces them with an empty string.
As a result, even though `getData()` can be imported and executed on the client, it won't work as expected.
To prevent accidental usage in Client Components, you can use the
Then, import the package into a file that contains server-only code:
lib/data.js
```
import 'server-only'

export async function getData() {
  const res = await fetch('https://external-service.com/data', {
    headers: {
      authorization: process.env.API_KEY,
    },
  })

  return res.json()
}
```

Now, if you try to import the module into a Client Component, there will be a build-time error.
The corresponding `window` object.
In Next.js, installing `server-only` or `client-only` is **optional**. However, if your linting rules flag extraneous dependencies, you may install them to avoid issues.
pnpmnpmyarnbun
Terminal
```
pnpm add server-only
```

Next.js handles `server-only` and `client-only` imports internally to provide clearer error messages when a module is used in the wrong environment. The contents of these packages from NPM are not used by Next.js.
Next.js also provides its own type declarations for `server-only` and `client-only`, for TypeScript configurations where
