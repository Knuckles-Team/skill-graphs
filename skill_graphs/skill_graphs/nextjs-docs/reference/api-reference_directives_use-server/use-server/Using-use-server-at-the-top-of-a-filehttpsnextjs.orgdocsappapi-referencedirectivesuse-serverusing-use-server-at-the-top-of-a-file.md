## Using `use server` at the top of a file[](https://nextjs.org/docs/app/api-reference/directives/use-server#using-use-server-at-the-top-of-a-file)
The following example shows a file with a `use server` directive at the top. All functions in the file are executed on the server.
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'
import { db } from '@/lib/db' // Your database client

export async function createUser(data: { name: string; email: string }) {
  const user = await db.user.create({ data })
  return user
}
```

### Using Server Functions in a Client Component[](https://nextjs.org/docs/app/api-reference/directives/use-server#using-server-functions-in-a-client-component)
To use Server Functions in Client Components you need to create your Server Functions in a dedicated file using the `use server` directive at the top of the file. These Server Functions can then be imported into Client and Server Components and executed.
Assuming you have a `fetchUsers` Server Function in `actions.ts`:
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'
import { db } from '@/lib/db' // Your database client

export async function fetchUsers() {
  const users = await db.user.findMany()
  return users
}
```

Then you can import the `fetchUsers` Server Function into a Client Component and execute it on the client-side.
app/components/my-button.tsx
TypeScript
JavaScript TypeScript
```
'use client'
import { fetchUsers } from '../actions'

export default function MyButton() {
  return <button onClick={() => fetchUsers()}>Fetch Users</button>
}
```
