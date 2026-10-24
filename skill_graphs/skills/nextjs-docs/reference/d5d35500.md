# headers
Last updated February 27, 2026
`headers` is an **async** function that allows you to **read** the HTTP incoming request headers from a [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components).
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { headers } from 'next/headers'

export default async function Page() {
  const headersList = await headers()
  const userAgent = headersList.get('user-agent')
}
```
