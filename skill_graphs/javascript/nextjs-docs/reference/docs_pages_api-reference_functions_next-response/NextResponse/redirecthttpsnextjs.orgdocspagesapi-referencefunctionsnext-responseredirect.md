##  `redirect()`[](https://nextjs.org/docs/pages/api-reference/functions/next-response#redirect)
Produce a response that redirects to a
```
import { NextResponse } from 'next/server'

return NextResponse.redirect(new URL('/new', request.url))
```

The `NextResponse.redirect()` method. For example, you can use the `request.nextUrl` property to get the current URL, and then modify it to redirect to a different URL.
```
import { NextResponse } from 'next/server'

// Given an incoming request...
const loginUrl = new URL('/login', request.url)
// Add ?from=/incoming-url to the /login URL
loginUrl.searchParams.set('from', request.nextUrl.pathname)
// And redirect to the new URL
return NextResponse.redirect(loginUrl)
```
