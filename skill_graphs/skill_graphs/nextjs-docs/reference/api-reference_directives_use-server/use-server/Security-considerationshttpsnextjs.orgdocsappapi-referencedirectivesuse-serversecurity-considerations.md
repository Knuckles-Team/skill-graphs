## Security considerations[](https://nextjs.org/docs/app/api-reference/directives/use-server#security-considerations)
When using the `use server` directive, it's important to ensure that all server-side logic is secure and that sensitive data remains protected.
### Authentication and authorization[](https://nextjs.org/docs/app/api-reference/directives/use-server#authentication-and-authorization)
Always authenticate and authorize users before performing sensitive server-side operations.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { db } from '@/lib/db' // Your database client
import { authenticate } from '@/lib/auth' // Your authentication library

export async function createUser(
  data: { name: string; email: string },
  token: string
) {
  const user = authenticate(token)
  if (!user) {
    throw new Error('Unauthorized')
  }
  const newUser = await db.user.create({ data })
  return newUser
}
```
