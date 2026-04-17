## No Response Body[](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-response-body)
### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-1)
  * Middleware can no longer produce a response body
  * If your Middleware _does_ respond with a body, a runtime error will be thrown
  * Migrate to using `rewrite`/`redirect` to pages/APIs handling a response


### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-1)
To respect the differences in client-side and server-side navigation, and to help ensure that developers do not build insecure Middleware, we are removing the ability to send response bodies in Middleware. This ensures that Middleware is only used to `rewrite`, `redirect`, or modify the incoming request (e.g. [setting cookies](https://nextjs.org/docs/messages/middleware-upgrade-guide#cookies-api-revamped)).
The following patterns will no longer work:
```
new Response('a text value')
new Response(streamOrBuffer)
new Response(JSON.stringify(obj), { headers: 'application/json' })
NextResponse.json()
```

### How to upgrade[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-1)
For cases where Middleware is used to respond (such as authorization), you should migrate to use `rewrite`/`redirect` to pages that show an authorization error, login forms, or to an API Route.
#### Before[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before)
pages/_middleware.ts
```
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { isAuthValid } from './lib/auth'

export function middleware(request: NextRequest) {
  // Example function to validate auth
  if (isAuthValid(request)) {
    return NextResponse.next()
  }

  return NextResponse.json({ message: 'Auth required' }, { status: 401 })
}
```

#### After[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after)
middleware.ts
```
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { isAuthValid } from './lib/auth'

export function middleware(request: NextRequest) {
  // Example function to validate auth
  if (isAuthValid(request)) {
    return NextResponse.next()
  }

  const loginUrl = new URL('/login', request.url)
  loginUrl.searchParams.set('from', request.nextUrl.pathname)

  return NextResponse.redirect(loginUrl)
}
```

#### Edge API Routes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#edge-api-routes)
If you were previously using Middleware to forward headers to an external API, you can now use [Edge API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes):
pages/api/proxy.ts
```
import { type NextRequest } from 'next/server'

export const config = {
  runtime: 'edge',
}

export default async function handler(req: NextRequest) {
  const authorization = req.cookies.get('authorization')
  return fetch('https://backend-api.com/api/protected', {
    method: req.method,
    headers: {
      authorization,
    },
    redirect: 'manual',
  })
}
```
