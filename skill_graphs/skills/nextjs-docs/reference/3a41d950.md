## Authorization[](https://nextjs.org/docs/pages/guides/authentication#authorization)
Once a user is authenticated and a session is created, you can implement authorization to control what the user can access and do within your application.
There are two main types of authorization checks:
  1. **Optimistic** : Checks if the user is authorized to access a route or perform an action using the session data stored in the cookie. These checks are useful for quick operations, such as showing/hiding UI elements or redirecting users based on permissions or roles.
  2. **Secure** : Checks if the user is authorized to access a route or perform an action using the session data stored in the database. These checks are more secure and are used for operations that require access to sensitive data or actions.


For both cases, we recommend:
  * Creating a [Data Access Layer](https://nextjs.org/docs/pages/guides/authentication#creating-a-data-access-layer-dal) to centralize your authorization logic
  * Using [Data Transfer Objects (DTO)](https://nextjs.org/docs/pages/guides/authentication#using-data-transfer-objects-dto) to only return the necessary data
  * Optionally use [Proxy](https://nextjs.org/docs/pages/guides/authentication#optimistic-checks-with-proxy-optional) to perform optimistic checks.


### Optimistic checks with Proxy (Optional)[](https://nextjs.org/docs/pages/guides/authentication#optimistic-checks-with-proxy-optional)
There are some cases where you may want to use [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) and redirect users based on permissions:
  * To perform optimistic checks. Since Proxy runs on every route, it's a good way to centralize redirect logic and pre-filter unauthorized users.
  * To protect static routes that share data between users (e.g. content behind a paywall).


However, since Proxy runs on every route, including [prefetched](https://nextjs.org/docs/app/getting-started/linking-and-navigating#prefetching) routes, it's important to only read the session from the cookie (optimistic checks), and avoid database checks to prevent performance issues.
For example:
proxy.ts
TypeScript
JavaScript TypeScript
```
import { NextRequest, NextResponse } from 'next/server'
import { decrypt } from '@/app/lib/session'
import { cookies } from 'next/headers'

// 1. Specify protected and public routes
const protectedRoutes = ['/dashboard']
const publicRoutes = ['/login', '/signup', '/']

export default async function proxy(req: NextRequest) {
  // 2. Check if the current route is protected or public
  const path = req.nextUrl.pathname
  const isProtectedRoute = protectedRoutes.includes(path)
  const isPublicRoute = publicRoutes.includes(path)

  // 3. Decrypt the session from the cookie
  const cookie = (await cookies()).get('session')?.value
  const session = await decrypt(cookie)

  // 4. Redirect to /login if the user is not authenticated
  if (isProtectedRoute && !session?.userId) {
    return NextResponse.redirect(new URL('/login', req.nextUrl))
  }

  // 5. Redirect to /dashboard if the user is authenticated
  if (
    isPublicRoute &&
    session?.userId &&
    !req.nextUrl.pathname.startsWith('/dashboard')
  ) {
    return NextResponse.redirect(new URL('/dashboard', req.nextUrl))
  }

  return NextResponse.next()
}

// Routes Proxy should not run on
export const config = {
  matcher: ['/((?!api|_next/static|_next/image|.*\\.png$).*)'],
}
```

While Proxy can be useful for initial checks, it should not be your only line of defense in protecting your data. The majority of security checks should be performed as close as possible to your data source, see [Data Access Layer](https://nextjs.org/docs/pages/guides/authentication#creating-a-data-access-layer-dal) for more information.
> **Tips** :
>   * In Proxy, you can also read cookies using `req.cookies.get('session').value`.
>   * Proxy uses the Node.js runtime, check if your Auth library and session management library are compatible. You may need to use [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)
>   * You can use the `matcher` property in the Proxy to specify which routes Proxy should run on. Although, for auth, it's recommended Proxy runs on all routes.
>

### Creating a Data Access Layer (DAL)[](https://nextjs.org/docs/pages/guides/authentication#creating-a-data-access-layer-dal-1)
#### Protecting API Routes[](https://nextjs.org/docs/pages/guides/authentication#protecting-api-routes)
API Routes in Next.js are essential for handling server-side logic and data management. It's crucial to secure these routes to ensure that only authorized users can access specific functionalities. This typically involves verifying the user's authentication status and their role-based permissions.
Here's an example of securing an API Route:
pages/api/route.ts
TypeScript
JavaScript TypeScript
```
import { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const session = await getSession(req)

  // Check if the user is authenticated
  if (!session) {
    res.status(401).json({
      error: 'User is not authenticated',
    })
    return
  }

  // Check if the user has the 'admin' role
  if (session.user.role !== 'admin') {
    res.status(401).json({
      error: 'Unauthorized access: User does not have admin privileges.',
    })
    return
  }

  // Proceed with the route for authorized users
  // ... implementation of the API Route
}
```

This example demonstrates an API Route with a two-tier security check for authentication and authorization. It first checks for an active session, and then verifies if the logged-in user is an 'admin'. This approach ensures secure access, limited to authenticated and authorized users, maintaining robust security for request processing.
