## Examples[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#examples)
### Displaying login UI to unauthenticated users[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#displaying-login-ui-to-unauthenticated-users)
You can use `unauthorized` function to display the `unauthorized.js` file with a login UI.
app/dashboard/page.tsx
TypeScript
JavaScript TypeScript
```
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export default async function DashboardPage() {
  const session = await verifySession()

  if (!session) {
    unauthorized()
  }

  return <div>Dashboard</div>
}
```

app/unauthorized.tsx
TypeScript
JavaScript TypeScript
```
import Login from '@/app/components/Login'

export default function UnauthorizedPage() {
  return (
    <main>
      <h1>401 - Unauthorized</h1>
      <p>Please log in to access this page.</p>
      <Login />
    </main>
  )
}
```

### Mutations with Server Actions[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#mutations-with-server-actions)
You can invoke `unauthorized` in Server Actions to ensure only authenticated users can perform specific mutations.
app/actions/update-profile.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'
import db from '@/app/lib/db'

export async function updateProfile(data: FormData) {
  const session = await verifySession()

  // If the user is not authenticated, return a 401
  if (!session) {
    unauthorized()
  }

  // Proceed with mutation
  // ...
}
```

### Fetching data with Route Handlers[](https://nextjs.org/docs/app/api-reference/functions/unauthorized#fetching-data-with-route-handlers)
You can use `unauthorized` in Route Handlers to ensure only authenticated users can access the endpoint.
app/api/profile/route.ts
TypeScript
JavaScript TypeScript
```
import { NextRequest, NextResponse } from 'next/server'
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export async function GET(req: NextRequest): Promise<NextResponse> {
  // Verify the user's session
  const session = await verifySession()

  // If no session exists, return a 401 and render unauthorized.tsx
  if (!session) {
    unauthorized()
  }

  // Fetch data
  // ...
}
```
