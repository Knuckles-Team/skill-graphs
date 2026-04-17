## Examples[](https://nextjs.org/docs/app/api-reference/functions/cookies#examples)
### Getting a cookie[](https://nextjs.org/docs/app/api-reference/functions/cookies#getting-a-cookie)
You can use the `(await cookies()).get('name')` method to get a single cookie:
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  const theme = cookieStore.get('theme')
  return '...'
}
```

### Getting all cookies[](https://nextjs.org/docs/app/api-reference/functions/cookies#getting-all-cookies)
You can use the `(await cookies()).getAll()` method to get all cookies with a matching name. If `name` is unspecified, it returns all the available cookies.
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  return cookieStore.getAll().map((cookie) => (
    <div key={cookie.name}>
      <p>Name: {cookie.name}</p>
      <p>Value: {cookie.value}</p>
    </div>
  ))
}
```

### Setting a cookie[](https://nextjs.org/docs/app/api-reference/functions/cookies#setting-a-cookie)
You can use the `(await cookies()).set(name, value, options)` method in a [Server Function](https://nextjs.org/docs/app/getting-started/updating-data) or [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) to set a cookie. The [`options` object](https://nextjs.org/docs/app/api-reference/functions/cookies#options) is optional.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { cookies } from 'next/headers'

export async function create(data) {
  const cookieStore = await cookies()

  cookieStore.set('name', 'lee')
  // or
  cookieStore.set('name', 'lee', { secure: true })
  // or
  cookieStore.set({
    name: 'name',
    value: 'lee',
    httpOnly: true,
    path: '/',
  })
}
```

### Checking if a cookie exists[](https://nextjs.org/docs/app/api-reference/functions/cookies#checking-if-a-cookie-exists)
You can use the `(await cookies()).has(name)` method to check if a cookie exists:
app/page.ts
TypeScript
JavaScript TypeScript
```
import { cookies } from 'next/headers'

export default async function Page() {
  const cookieStore = await cookies()
  const hasCookie = cookieStore.has('theme')
  return '...'
}
```

### Deleting cookies[](https://nextjs.org/docs/app/api-reference/functions/cookies#deleting-cookies)
There are three ways you can delete a cookie.
Using the `delete()` method:
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { cookies } from 'next/headers'

export async function deleteCookie(data) {
  const cookieStore = await cookies()
  cookieStore.delete('name')
}
```

Setting a new cookie with the same name and an empty value:
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { cookies } from 'next/headers'

export async function deleteCookie(data) {
  const cookieStore = await cookies()
  cookieStore.set('name', '')
}
```

Setting the `maxAge` to 0 will immediately expire a cookie. `maxAge` accepts a value in seconds.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { cookies } from 'next/headers'

export async function deleteCookie(data) {
  const cookieStore = await cookies()
  cookieStore.set('name', 'value', { maxAge: 0 })
}
```
