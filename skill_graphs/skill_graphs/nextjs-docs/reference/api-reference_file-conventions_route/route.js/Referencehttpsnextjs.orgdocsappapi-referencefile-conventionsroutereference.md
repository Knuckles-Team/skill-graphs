## Reference[](https://nextjs.org/docs/app/api-reference/file-conventions/route#reference)
### HTTP Methods[](https://nextjs.org/docs/app/api-reference/file-conventions/route#http-methods)
A **route** file allows you to create custom request handlers for a given route. The following `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, and `OPTIONS`.
route.ts
TypeScript
JavaScript TypeScript
```
export async function GET(request: Request) {}

export async function HEAD(request: Request) {}

export async function POST(request: Request) {}

export async function PUT(request: Request) {}

export async function DELETE(request: Request) {}

export async function PATCH(request: Request) {}

// If `OPTIONS` is not defined, Next.js will automatically implement `OPTIONS` and set the appropriate Response `Allow` header depending on the other methods defined in the Route Handler.
export async function OPTIONS(request: Request) {}
```

### Parameters[](https://nextjs.org/docs/app/api-reference/file-conventions/route#parameters)
####  `request` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/route#request-optional)
The `request` object is a [NextRequest](https://nextjs.org/docs/app/api-reference/functions/next-request) object, which is an extension of the Web `NextRequest` gives you further control over the incoming request, including easily accessing `cookies` and an extended, parsed, URL object `nextUrl`.
route.ts
TypeScript
JavaScript TypeScript
```
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const url = request.nextUrl
}
```

####  `context` (optional)[](https://nextjs.org/docs/app/api-reference/file-conventions/route#context-optional)
  * **`params`**: a promise that resolves to an object containing the[dynamic route parameters](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) for the current route.


app/dashboard/[team]/route.ts
TypeScript
JavaScript TypeScript
```
export async function GET(
  request: Request,
  { params }: { params: Promise<{ team: string }> }
) {
  const { team } = await params
}
```

Example | URL | `params`
---|---|---
`app/dashboard/[team]/route.js` | `/dashboard/1` | `Promise<{ team: '1' }>`
`app/shop/[tag]/[item]/route.js` | `/shop/1/2` | `Promise<{ tag: '1', item: '2' }>`
`app/blog/[...slug]/route.js` | `/blog/1/2` | `Promise<{ slug: ['1', '2'] }>`
### Route Context Helper[](https://nextjs.org/docs/app/api-reference/file-conventions/route#route-context-helper)
You can type the Route Handler context using `RouteContext` to get strongly typed `params` from a route literal. `RouteContext` is a globally available helper.
app/users/[id]/route.ts
```
import type { NextRequest } from 'next/server'

export async function GET(_req: NextRequest, ctx: RouteContext<'/users/[id]'>) {
  const { id } = await ctx.params
  return Response.json({ id })
}
```

> **Good to know**
>   * Types are generated during `next dev`, `next build` or `next typegen`.
>   * After type generation, the `RouteContext` helper is globally available. It doesn't need to be imported.
>
