# Proxy
Last updated February 27, 2026
> **Note** : The `middleware` file convention is deprecated and has been renamed to `proxy`. See [Migration to Proxy](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#migration-to-proxy) for more details.
The `proxy.js|ts` file is used to write [Proxy](https://nextjs.org/docs/app/getting-started/proxy) and run code on the server before a request is completed. Then, based on the incoming request, you can modify the response by rewriting, redirecting, modifying the request or response headers, or responding directly.
Proxy executes before routes are rendered. It's particularly useful for implementing custom server-side logic like authentication, logging, or handling redirects.
> **Good to know** :
> Proxy is meant to be invoked separately of your render code and in optimized cases deployed to your CDN for fast redirect/rewrite handling, you should not attempt relying on shared modules or globals.
> To pass information from Proxy to your application, use [headers](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#setting-headers), [cookies](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#using-cookies), [rewrites](https://nextjs.org/docs/app/api-reference/functions/next-response#rewrite), [redirects](https://nextjs.org/docs/app/api-reference/functions/next-response#redirect), or the URL.
Create a `proxy.ts` (or `.js`) file in the project root, or inside `src` if applicable, so that it is located at the same level as `pages` or `app`.
If you’ve customized [`pageExtensions`](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions), for example to `.page.ts` or `.page.js`, name your file `proxy.page.ts` or `proxy.page.js` accordingly.
proxy.ts
TypeScript
JavaScript TypeScript
```
import { NextResponse, NextRequest } from 'next/server'

// This function can be marked `async` if using `await` inside
export function proxy(request: NextRequest) {
  return NextResponse.redirect(new URL('/home', request.url))
}

export const config = {
  matcher: '/about/:path*',
}
```
