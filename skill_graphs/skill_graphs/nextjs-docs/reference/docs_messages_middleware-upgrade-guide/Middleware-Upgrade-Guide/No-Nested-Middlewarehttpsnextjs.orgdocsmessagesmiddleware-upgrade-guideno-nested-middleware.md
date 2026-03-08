## No Nested Middleware[](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-nested-middleware)
### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes)
  * Define a single Middleware file next to your `pages` folder
  * No need to prefix the file with an underscore
  * A custom matcher can be used to define matching routes using an exported config object


### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation)
Previously, you could create a `_middleware.ts` file under the `pages` directory at any level. Middleware execution was based on the file path where it was created.
Based on customer feedback, we have replaced this API with a single root Middleware, which provides the following improvements:
  * **Faster execution with lower latency** : With nested Middleware, a single request could invoke multiple Middleware functions. A single Middleware means a single function execution, which is more efficient.
  * **Less expensive** : Middleware usage is billed per invocation. Using nested Middleware, a single request could invoke multiple Middleware functions, meaning multiple Middleware charges per request. A single Middleware means a single invocation per request and is more cost effective.
  * **Middleware can conveniently filter on things besides routes** : With nested Middleware, the Middleware files were located in the `pages` directory and Middleware was executed based on request paths. By moving to a single root Middleware, you can still execute code based on request paths, but you can now more conveniently execute Middleware based on other conditions, like `cookies` or the presence of a request header.
  * **Deterministic execution ordering** : With nested Middleware, a single request could match multiple Middleware functions. For example, a request to `/dashboard/users/*` would invoke Middleware defined in both `/dashboard/users/_middleware.ts` and `/dashboard/_middleware.js`. However, the execution order is difficult to reason about. Moving to a single, root Middleware more explicitly defines execution order.
  * **Supports Next.js Layouts (RFC)** : Moving to a single, root Middleware helps support the new [Layouts (RFC) in Next.js](https://nextjs.org/blog/layouts-rfc).


### How to upgrade[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade)
You should declare **one single Middleware file** in your application, which should be located next to the `pages` directory and named **without** an `_` prefix. Your Middleware file can still have either a `.ts` or `.js` extension.
Middleware will be invoked for **every route in the app** , and a custom matcher can be used to define matching filters. The following is an example for a Middleware that triggers for `/about/*` and `/dashboard/:path*`, the custom matcher is defined in an exported config object:
middleware.ts
```
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  return NextResponse.rewrite(new URL('/about-2', request.url))
}

// Supports both a single string value or an array of matchers
export const config = {
  matcher: ['/about/:path*', '/dashboard/:path*'],
}
```

The matcher config also allows full regex so matching like negative lookaheads or character matching is supported. An example of a negative lookahead to match all except specific paths can be seen here:
middleware.ts
```
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - favicon.ico (favicon file)
     */
    '/((?!api|_next/static|favicon.ico).*)',
  ],
}
```

While the config option is preferred since it doesn't get invoked on every request, you can also use conditional statements to only run the Middleware when it matches specific paths. One advantage of using conditionals is defining explicit ordering for when Middleware executes. The following example shows how you can merge two previously nested Middleware:
middleware.ts
```
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  if (request.nextUrl.pathname.startsWith('/about')) {
    // This logic is only applied to /about
  }

  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    // This logic is only applied to /dashboard
  }
}
```
