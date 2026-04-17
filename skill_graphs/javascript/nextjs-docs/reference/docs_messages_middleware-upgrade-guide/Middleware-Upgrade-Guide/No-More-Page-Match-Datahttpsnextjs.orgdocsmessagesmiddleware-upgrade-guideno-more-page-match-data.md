## No More Page Match Data[](https://nextjs.org/docs/messages/middleware-upgrade-guide#no-more-page-match-data)
### Summary of changes[](https://nextjs.org/docs/messages/middleware-upgrade-guide#summary-of-changes-4)
  * Use


### Explanation[](https://nextjs.org/docs/messages/middleware-upgrade-guide#explanation-4)
Currently, Middleware estimates whether you are serving an asset of a Page based on the Next.js routes manifest (internal configuration). This value is surfaced through `request.page`.
To make page and asset matching more accurate, we are now using the web standard `URLPattern` API.
### How to upgrade[](https://nextjs.org/docs/messages/middleware-upgrade-guide#how-to-upgrade-4)
Use
#### Before[](https://nextjs.org/docs/messages/middleware-upgrade-guide#before-3)
pages/_middleware.ts
```
import { NextResponse } from 'next/server'
import type { NextRequest, NextFetchEvent } from 'next/server'

export function middleware(request: NextRequest, event: NextFetchEvent) {
  const { params } = event.request.page
  const { locale, slug } = params

  if (locale && slug) {
    const { search, protocol, host } = request.nextUrl
    const url = new URL(`${protocol}//${locale}.${host}/${slug}${search}`)
    return NextResponse.redirect(url)
  }
}
```

#### After[](https://nextjs.org/docs/messages/middleware-upgrade-guide#after-3)
middleware.ts
```
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

const PATTERNS = [
  [
    new URLPattern({ pathname: '/:locale/:slug' }),
    ({ pathname }) => pathname.groups,
  ],
]

const params = (url) => {
  const input = url.split('?')[0]
  let result = {}

  for (const [pattern, handler] of PATTERNS) {
    const patternResult = pattern.exec(input)
    if (patternResult !== null && 'pathname' in patternResult) {
      result = handler(patternResult)
      break
    }
  }
  return result
}

export function middleware(request: NextRequest) {
  const { locale, slug } = params(request.url)

  if (locale && slug) {
    const { search, protocol, host } = request.nextUrl
    const url = new URL(`${protocol}//${locale}.${host}/${slug}${search}`)
    return NextResponse.redirect(url)
  }
}
```
