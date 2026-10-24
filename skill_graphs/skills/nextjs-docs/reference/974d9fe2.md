## Example[](https://nextjs.org/docs/app/api-reference/functions/redirect#example)
### Server Component[](https://nextjs.org/docs/app/api-reference/functions/redirect#server-component)
Invoking the `redirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.
app/team/[id]/page.tsx
TypeScript
JavaScript TypeScript
```
import { redirect } from 'next/navigation'

async function fetchTeam(id: string) {
  const res = await fetch('https://...')
  if (!res.ok) return undefined
  return res.json()
}

export default async function Profile({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const team = await fetchTeam(id)

  if (!team) {
    redirect('/login')
  }

  // ...
}
```

> **Good to know** : `redirect` does not require you to use `return redirect()` as it uses the TypeScript
### Client Component[](https://nextjs.org/docs/app/api-reference/functions/redirect#client-component)
`redirect` can be directly used in a Client Component.
components/client-redirect.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { redirect, usePathname } from 'next/navigation'

export function ClientRedirect() {
  const pathname = usePathname()

  if (pathname.startsWith('/admin') && !pathname.includes('/login')) {
    redirect('/admin/login')
  }

  return <div>Login Page</div>
}
```

> **Good to know** : When using `redirect` in a Client Component on initial page load during Server-Side Rendering (SSR), it will perform a server-side redirect.
`redirect` can be used in a Client Component through a Server Action. If you need to use an event handler to redirect the user, you can use the [`useRouter`](https://nextjs.org/docs/app/api-reference/functions/use-router) hook.
app/client-redirect.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import { navigate } from './actions'

export function ClientRedirect() {
  return (
    <form action={navigate}>
      <input type="text" name="id" />
      <button>Submit</button>
    </form>
  )
}
```

app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { redirect } from 'next/navigation'

export async function navigate(data: FormData) {
  redirect(`/posts/${data.get('id')}`)
}
```
