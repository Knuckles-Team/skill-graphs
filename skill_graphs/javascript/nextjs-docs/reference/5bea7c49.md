## Examples[](https://nextjs.org/docs/app/guides/lazy-loading#examples)
### Importing Client Components[](https://nextjs.org/docs/app/guides/lazy-loading#importing-client-components)
app/page.js
```
'use client'

import { useState } from 'react'
import dynamic from 'next/dynamic'

// Client Components:
const ComponentA = dynamic(() => import('../components/A'))
const ComponentB = dynamic(() => import('../components/B'))
const ComponentC = dynamic(() => import('../components/C'), { ssr: false })

export default function ClientComponentExample() {
  const [showMore, setShowMore] = useState(false)

  return (
    <div>
      {/* Load immediately, but in a separate client bundle */}
      <ComponentA />

      {/* Load on demand, only when/if the condition is met */}
      {showMore && <ComponentB />}
      <button onClick={() => setShowMore(!showMore)}>Toggle</button>

      {/* Load only on the client side */}
      <ComponentC />
    </div>
  )
}
```

> **Note:** When a Server Component dynamically imports a Client Component, automatic **not** supported.
### Skipping SSR[](https://nextjs.org/docs/app/guides/lazy-loading#skipping-ssr)
When using `React.lazy()` and Suspense, Client Components will be
> **Note:** `ssr: false` option will only work for Client Components, move it into Client Components ensure the client code-splitting working properly.
If you want to disable pre-rendering for a Client Component, you can use the `ssr` option set to `false`:
```
const ComponentC = dynamic(() => import('../components/C'), { ssr: false })
```

### Importing Server Components[](https://nextjs.org/docs/app/guides/lazy-loading#importing-server-components)
If you dynamically import a Server Component, only the Client Components that are children of the Server Component will be lazy-loaded - not the Server Component itself. It will also help preload the static assets such as CSS when you're using it in Server Components.
app/page.js
```
import dynamic from 'next/dynamic'

// Server Component:
const ServerComponent = dynamic(() => import('../components/ServerComponent'))

export default function ServerComponentExample() {
  return (
    <div>
      <ServerComponent />
    </div>
  )
}
```

> **Note:** `ssr: false` option is not supported in Server Components. You will see an error if you try to use it in Server Components. `ssr: false` is not allowed with `next/dynamic` in Server Components. Please move it into a Client Component.
### Loading External Libraries[](https://nextjs.org/docs/app/guides/lazy-loading#loading-external-libraries)
External libraries can be loaded on demand using the `fuse.js` for fuzzy search. The module is only loaded on the client after the user types in the search input.
app/page.js
```
'use client'

import { useState } from 'react'

const names = ['Tim', 'Joe', 'Bel', 'Lee']

export default function Page() {
  const [results, setResults] = useState()

  return (
    <div>
      <input
        type="text"
        placeholder="Search"
        onChange={async (e) => {
          const { value } = e.currentTarget
          // Dynamically load fuse.js
          const Fuse = (await import('fuse.js')).default
          const fuse = new Fuse(names)

          setResults(fuse.search(value))
        }}
      />
      <pre>Results: {JSON.stringify(results, null, 2)}</pre>
    </div>
  )
}
```

### Adding a custom loading component[](https://nextjs.org/docs/app/guides/lazy-loading#adding-a-custom-loading-component)
app/page.js
```
'use client'

import dynamic from 'next/dynamic'

const WithCustomLoading = dynamic(
  () => import('../components/WithCustomLoading'),
  {
    loading: () => <p>Loading...</p>,
  }
)

export default function Page() {
  return (
    <div>
      {/* The loading component will be rendered while  <WithCustomLoading/> is loading */}
      <WithCustomLoading />
    </div>
  )
}
```

### Importing Named Exports[](https://nextjs.org/docs/app/guides/lazy-loading#importing-named-exports)
To dynamically import a named export, you can return it from the Promise returned by
components/hello.js
```
'use client'

export function Hello() {
  return <p>Hello!</p>
}
```

app/page.js
```
import dynamic from 'next/dynamic'

const ClientComponent = dynamic(() =>
  import('../components/hello').then((mod) => mod.Hello)
)
```

[PreviousJSON-LD](https://nextjs.org/docs/app/guides/json-ld)[NextDevelopment Environment](https://nextjs.org/docs/app/guides/local-development)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
