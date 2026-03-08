## Examples[](https://nextjs.org/docs/community/rspack#examples)
### Sharing components with App Router[](https://nextjs.org/docs/community/rspack#sharing-components-with-app-router)
`useParams` from `next/navigation` works in both the Pages Router and App Router. This allows you to create shared components that work in either context:
components/breadcrumb.tsx
TypeScript
JavaScript TypeScript
```
import { useParams } from 'next/navigation'

// This component works in both pages/ and app/
export function Breadcrumb() {
  const params = useParams<{ slug: string }>()

  if (!params) {
    // Fallback for Pages Router during pre-rendering
    return <nav>Home / ...</nav>
  }

  return <nav>Home / {params.slug}</nav>
}
```

> **Good to know** : When using this component in the App Router, `useParams` never returns `null`, so the fallback branch will not be rendered.
