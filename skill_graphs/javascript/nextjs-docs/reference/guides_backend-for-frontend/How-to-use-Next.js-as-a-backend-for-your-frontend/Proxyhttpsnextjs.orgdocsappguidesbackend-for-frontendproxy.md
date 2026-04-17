## Proxy[](https://nextjs.org/docs/app/guides/backend-for-frontend#proxy)
Only one `proxy` file is allowed per project. Use `config.matcher` to target specific paths. Learn more about [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy).
Use `proxy` to generate a response before the request reaches a route path.
proxy.ts
TypeScript
JavaScript TypeScript
```
import { isAuthenticated } from '@lib/auth'

export const config = {
  matcher: '/api/:function*',
}

export function proxy(request: Request) {
  if (!isAuthenticated(request)) {
    return Response.json(
      { success: false, message: 'authentication failed' },
      { status: 401 }
    )
  }
}
```

You can also proxy requests using `proxy`:
proxy.ts
TypeScript
JavaScript TypeScript
```
import { NextResponse } from 'next/server'

export function proxy(request: Request) {
  if (request.nextUrl.pathname === '/proxy-this-path') {
    const rewriteUrl = new URL('https://nextjs.org')
    return NextResponse.rewrite(rewriteUrl)
  }
}
```

Another type of response `proxy` can produce are redirects:
proxy.ts
TypeScript
JavaScript TypeScript
```
import { NextResponse } from 'next/server'

export function proxy(request: Request) {
  if (request.nextUrl.pathname === '/v1/docs') {
    request.nextUrl.pathname = '/v2/docs'
    return NextResponse.redirect(request.nextUrl)
  }
}
```
