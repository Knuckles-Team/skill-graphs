## Examples[](https://nextjs.org/docs/app/api-reference/functions/forbidden#examples)
### Role-based route protection[](https://nextjs.org/docs/app/api-reference/functions/forbidden#role-based-route-protection)
You can use `forbidden` to restrict access to certain routes based on user roles. This ensures that users who are authenticated but lack the required permissions cannot access the route.
app/admin/page.tsx
TypeScript
JavaScript TypeScript
```
import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'

export default async function AdminPage() {
  const session = await verifySession()

  // Check if the user has the 'admin' role
  if (session.role !== 'admin') {
    forbidden()
  }

  // Render the admin page for authorized users
  return (
    <main>
      <h1>Admin Dashboard</h1>
      <p>Welcome, {session.user.name}!</p>
    </main>
  )
}
```

### Mutations with Server Actions[](https://nextjs.org/docs/app/api-reference/functions/forbidden#mutations-with-server-actions)
When implementing mutations in Server Actions, you can use `forbidden` to only allow users with a specific role to update sensitive data.
app/actions/update-role.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { verifySession } from '@/app/lib/dal'
import { forbidden } from 'next/navigation'
import db from '@/app/lib/db'

export async function updateRole(formData: FormData) {
  const session = await verifySession()

  // Ensure only admins can update roles
  if (session.role !== 'admin') {
    forbidden()
  }

  // Perform the role update for authorized users
  // ...
}
```
