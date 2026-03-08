##  `useRouter()` hook[](https://nextjs.org/docs/pages/guides/redirecting#userouter-hook)
If you need to redirect inside a component, you can use the `push` method from the `useRouter` hook. For example:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()

  return (
    <button type="button" onClick={() => router.push('/dashboard')}>
      Dashboard
    </button>
  )
}
```

> **Good to know** :
>   * If you don't need to programmatically navigate a user, you should use a [`<Link>`](https://nextjs.org/docs/app/api-reference/components/link) component.
>

See the [`useRouter` API reference](https://nextjs.org/docs/pages/api-reference/functions/use-router) for more information.
