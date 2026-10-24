# useSelectedLayoutSegments
Last updated February 27, 2026
`useSelectedLayoutSegments` is a **Client Component** hook that lets you read the active route segments **below** the Layout it is called from.
It is useful for creating UI in parent Layouts that need knowledge of active child segments such as breadcrumbs.
app/example-client-component.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useSelectedLayoutSegments } from 'next/navigation'

export default function ExampleClientComponent() {
  const segments = useSelectedLayoutSegments()

  return (
    <ul>
      {segments.map((segment, index) => (
        <li key={index}>{segment}</li>
      ))}
    </ul>
  )
}
```

> **Good to know** :
>   * Since `useSelectedLayoutSegments` is a [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) hook, and Layouts are [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) by default, `useSelectedLayoutSegments` is usually called via a Client Component that is imported into a Layout.
>   * The returned segments include [Route Groups](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups), which you might not want to be included in your UI. You can use the
>   * For [catch-all](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments) routes, the matched segments are returned as a single joined string within the array. For example, given `app/blog/[...slug]/page.js`, calling from `app/layout.js` when visiting `/blog/a/b/c` returns `['blog', 'a/b/c']`, not `['blog', 'a', 'b', 'c']`.
>
