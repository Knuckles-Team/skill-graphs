## Cookies API Revamped[](https://nextjs.org/docs/messages/middleware-upgrade-guide#cookies-api-revamped)
### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-2)
Added | Removed
---|---
`cookies.set` | `cookie`
`cookies.delete` | `clearCookie`
`cookies.getWithOptions` | `cookies`
### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-2)
Based on beta feedback, we are changing the Cookies API in `NextRequest` and `NextResponse` to align more to a `get`/`set` model. The `Cookies` API extends Map, including methods like
### How to upgrade[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-2)
`NextResponse` now has a `cookies` instance with:
  * `cookies.delete`
  * `cookies.set`
  * `cookies.getWithOptions`


As well as other extended methods from `Map`.
#### Before[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-1)
pages/_middleware.ts
```
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  // create an instance of the class to access the public methods. This uses `next()`,
  // you could use `redirect()` or `rewrite()` as well
  let response = NextResponse.next()
  // get the cookies from the request
  let cookieFromRequest = request.cookies['my-cookie']
  // set the `cookie`
  response.cookie('hello', 'world')
  // set the `cookie` with options
  const cookieWithOptions = response.cookie('hello', 'world', {
    path: '/',
    maxAge: 1000 * 60 * 60 * 24 * 7,
    httpOnly: true,
    sameSite: 'strict',
    domain: 'example.com',
  })
  // clear the `cookie`
  response.clearCookie('hello')

  return response
}
```

#### After[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-1)
middleware.ts
```
export function middleware() {
  const response = new NextResponse()

  // set a cookie
  response.cookies.set('vercel', 'fast')

  // set another cookie with options
  response.cookies.set('nextjs', 'awesome', { path: '/test' })

  // get all the details of a cookie
  const { value, ...options } = response.cookies.getWithOptions('vercel')
  console.log(value) // => 'fast'
  console.log(options) // => { name: 'vercel', Path: '/test' }

  // deleting a cookie will mark it as expired
  response.cookies.delete('vercel')

  return response
}
```
