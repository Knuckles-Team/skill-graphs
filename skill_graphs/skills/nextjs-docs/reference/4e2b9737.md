## Nesting Client Components within Server Components[](https://nextjs.org/docs/app/api-reference/directives/use-client#nesting-client-components-within-server-components)
Combining Server and Client Components allows you to build applications that are both performant and interactive:
  1. **Server Components** : Use for static content, data fetching, and SEO-friendly elements.
  2. **Client Components** : Use for interactive elements that require state, effects, or browser APIs.
  3. **Component composition** : Nest Client Components within Server Components as needed for a clear separation of server and client logic.


In the following example:
  * `Header` is a Server Component handling static content.
  * `Counter` is a Client Component enabling interactivity within the page.


app/page.tsx
TypeScript
JavaScript TypeScript
```
import Header from './header'
import Counter from './counter' // This is a Client Component

export default function Page() {
  return (
    <div>
      <Header />
      <Counter />
    </div>
  )
}
```
