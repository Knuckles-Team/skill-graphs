##  `notFound()`[](https://nextjs.org/docs/app/api-reference/functions/not-found#notfound)
Invoking the `notFound()` function throws a `NEXT_HTTP_ERROR_FALLBACK;404` error and terminates rendering of the route segment in which it was thrown. Specifying a [**not-found** file](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) allows you to gracefully handle such errors by rendering a Not Found UI within the segment.
app/user/[id]/page.js
```
import { notFound } from 'next/navigation'

async function fetchUser(id) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}

export default async function Profile({ params }) {
  const { id } = await params
  const user = await fetchUser(id)

  if (!user) {
    notFound()
  }

  // ...
}
```

> **Good to know** : `notFound()` does not require you to use `return notFound()` due to using the TypeScript
