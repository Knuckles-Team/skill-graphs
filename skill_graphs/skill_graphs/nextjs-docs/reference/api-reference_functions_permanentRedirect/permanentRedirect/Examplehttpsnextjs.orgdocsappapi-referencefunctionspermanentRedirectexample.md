## Example[](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect#example)
Invoking the `permanentRedirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.
app/team/[id]/page.js
```
import { permanentRedirect } from 'next/navigation'

async function fetchTeam(id) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}

export default async function Profile({ params }) {
  const { id } = await params
  const team = await fetchTeam(id)
  if (!team) {
    permanentRedirect('/login')
  }

  // ...
}
```

> **Good to know** : `permanentRedirect` does not require you to use `return permanentRedirect()` as it uses the TypeScript
### [redirect API Reference for the redirect function.](https://nextjs.org/docs/app/api-reference/functions/redirect)
[PreviousnotFound](https://nextjs.org/docs/app/api-reference/functions/not-found)[Nextredirect](https://nextjs.org/docs/app/api-reference/functions/redirect)
Was this helpful?
Send
