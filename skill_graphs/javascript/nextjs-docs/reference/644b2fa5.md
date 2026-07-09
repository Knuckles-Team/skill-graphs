## New User-Agent Helper[](https://nextjs.org/docs/messages/middleware-upgrade-guide#new-user-agent-helper)
### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-3)
  * Accessing the user agent is no longer available on the request object
  * We've added a new `userAgent` helper to reduce Middleware size by `17kb`


### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-3)
To help reduce the size of your Middleware, we have extracted the user agent from the request object and created a new helper `userAgent`.
The helper is imported from `next/server` and allows you to opt in to using the user agent. The helper gives you access to the same properties that were available from the request object.
### How to upgrade[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-3)
  * Import the `userAgent` helper from `next/server`
  * Destructure the properties you need to work with


#### Before[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-2)
pages/_middleware.ts
```
import { NextRequest, NextResponse } from 'next/server'

export function middleware(request: NextRequest) {
  const url = request.nextUrl
  const viewport = request.ua.device.type === 'mobile' ? 'mobile' : 'desktop'
  url.searchParams.set('viewport', viewport)
  return NextResponse.rewrite(url)
}
```

#### After[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-2)
middleware.ts
```
import { NextRequest, NextResponse, userAgent } from 'next/server'

export function middleware(request: NextRequest) {
  const url = request.nextUrl
  const { device } = userAgent(request)
  const viewport = device.type === 'mobile' ? 'mobile' : 'desktop'
  url.searchParams.set('viewport', viewport)
  return NextResponse.rewrite(url)
}
```
