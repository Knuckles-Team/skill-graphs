# cookies
Last updated February 27, 2026
`cookies` is an **async** function that allows you to read the HTTP incoming request cookies in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), and read/write outgoing request cookies in [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data) or [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route).
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
