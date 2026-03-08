##  `NextResponse.redirect` in Proxy[](https://nextjs.org/docs/pages/guides/redirecting#nextresponseredirect-in-proxy)
Proxy allows you to run code before a request is completed. Then, based on the incoming request, redirect to a different URL using `NextResponse.redirect`. This is useful if you want to redirect users based on a condition (e.g. authentication, session management, etc) or have [a large number of redirects](https://nextjs.org/docs/pages/guides/redirecting#managing-redirects-at-scale-advanced).
For example, to redirect the user to a `/login` page if they are not authenticated:
proxy.ts
TypeScript
JavaScript TypeScript
```
import { NextResponse, NextRequest } from 'next/server'
import { authenticate } from 'auth-provider'

export function proxy(request: NextRequest) {
  const isAuthenticated = authenticate(request)

  // If the user is authenticated, continue as normal
  if (isAuthenticated) {
    return NextResponse.next()
  }

  // Redirect to login page if not authenticated
  return NextResponse.redirect(new URL('/login', request.url))
}

export const config = {
  matcher: '/dashboard/:path*',
}
```

> **Good to know** :
>   * Proxy runs **after** `redirects` in `next.config.js` and **before** rendering.
>

See the [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) documentation for more information.
