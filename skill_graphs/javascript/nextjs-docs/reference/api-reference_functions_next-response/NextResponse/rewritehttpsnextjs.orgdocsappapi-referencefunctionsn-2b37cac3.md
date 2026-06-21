##  `rewrite()`[](https://nextjs.org/docs/app/api-reference/functions/next-response#rewrite)
Produce a response that rewrites (proxies) the given
```
import { NextResponse } from 'next/server'

// Incoming request: /about, browser shows /about
// Rewritten request: /proxy, browser shows /about
return NextResponse.rewrite(new URL('/proxy', request.url))
```
