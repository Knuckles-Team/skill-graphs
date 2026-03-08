## NextRequest and NextResponse[](https://nextjs.org/docs/app/guides/backend-for-frontend#nextrequest-and-nextresponse)
Next.js extends the
Both provide methods for reading and manipulating cookies.
`NextRequest` includes the [`nextUrl`](https://nextjs.org/docs/app/api-reference/functions/next-request#nexturl) property, which exposes parsed values from the incoming request, for example, it makes it easier to access request pathname and search params.
`NextResponse` provides helpers like `next()`, `json()`, `redirect()`, and `rewrite()`.
You can pass `NextRequest` to any function expecting `Request`. Likewise, you can return `NextResponse` where a `Response` is expected.
/app/echo-pathname/route.ts
TypeScript
JavaScript TypeScript
```
import { type NextRequest, NextResponse } from 'next/server'

export async function GET(request: NextRequest) {
  const nextUrl = request.nextUrl

  if (nextUrl.searchParams.get('redirect')) {
    return NextResponse.redirect(new URL('/', request.url))
  }

  if (nextUrl.searchParams.get('rewrite')) {
    return NextResponse.rewrite(new URL('/', request.url))
  }

  return NextResponse.json({ pathname: nextUrl.pathname })
}
```

Learn more about [`NextRequest`](https://nextjs.org/docs/app/api-reference/functions/next-request) and [`NextResponse`](https://nextjs.org/docs/app/api-reference/functions/next-response).
