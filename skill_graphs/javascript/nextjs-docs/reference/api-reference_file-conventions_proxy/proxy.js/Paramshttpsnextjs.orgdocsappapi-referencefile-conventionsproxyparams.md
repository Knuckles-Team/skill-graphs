## Params[](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#params)
###  `request`[](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#request)
When defining Proxy, the default export function accepts a single parameter, `request`. This parameter is an instance of `NextRequest`, which represents the incoming HTTP request.
proxy.ts
TypeScript
JavaScript TypeScript
```
import type { NextRequest } from 'next/server'

export function proxy(request: NextRequest) {
  // Proxy logic goes here
}
```

> **Good to know** :
>   * `NextRequest` is a type that represents incoming HTTP requests in Next.js Proxy, whereas [`NextResponse`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#nextresponse) is a class used to manipulate and send back HTTP responses.
>
