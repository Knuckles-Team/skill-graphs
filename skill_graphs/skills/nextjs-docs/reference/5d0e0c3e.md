## Imperative Routing[](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating#imperative-routing)
[`next/link`](https://nextjs.org/docs/pages/api-reference/components/link) should be able to cover most of your routing needs, but you can also do client-side navigations without it, take a look at the [documentation for `next/router`](https://nextjs.org/docs/pages/api-reference/functions/use-router).
The following example shows how to do basic page navigations with [`useRouter`](https://nextjs.org/docs/pages/api-reference/functions/use-router):
```
import { useRouter } from 'next/router'

export default function ReadMore() {
  const router = useRouter()

  return (
    <button onClick={() => router.push('/about')}>
      Click here to read more
    </button>
  )
}
```
