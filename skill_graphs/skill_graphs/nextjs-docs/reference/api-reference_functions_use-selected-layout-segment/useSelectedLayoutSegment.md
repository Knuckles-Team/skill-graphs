# useSelectedLayoutSegment
Last updated February 27, 2026
`useSelectedLayoutSegment` is a **Client Component** hook that lets you read the active route segment **one level below** the Layout it is called from.
It is useful for navigation UI, such as tabs inside a parent layout that change style depending on the active child segment.
app/example-client-component.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { useSelectedLayoutSegment } from 'next/navigation'

export default function ExampleClientComponent() {
  const segment = useSelectedLayoutSegment()

  return <p>Active segment: {segment}</p>
}
```

> **Good to know** :
>   * Since `useSelectedLayoutSegment` is a [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) hook, and Layouts are [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) by default, `useSelectedLayoutSegment` is usually called via a Client Component that is imported into a Layout.
>   * `useSelectedLayoutSegment` only returns the segment one level down. To return all active segments, see [`useSelectedLayoutSegments`](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments)
>   * For [catch-all](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments) routes, the matched segments are returned as a single joined string. For example, given `app/blog/[...slug]/page.js`, calling from `app/blog/layout.js` when visiting `/blog/a/b/c` returns `'a/b/c'`.
>
