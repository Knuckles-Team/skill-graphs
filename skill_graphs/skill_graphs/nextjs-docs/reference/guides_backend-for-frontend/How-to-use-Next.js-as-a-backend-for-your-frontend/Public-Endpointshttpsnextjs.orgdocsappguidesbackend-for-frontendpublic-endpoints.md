## Public Endpoints[](https://nextjs.org/docs/app/guides/backend-for-frontend#public-endpoints)
Route Handlers are public HTTP endpoints. Any client can access them.
Create a Route Handler using the `route.ts` or `route.js` file convention:
/app/api/route.ts
TypeScript
JavaScript TypeScript
```
export function GET(request: Request) {}
```

This handles `GET` requests sent to `/api`.
Use `try/catch` blocks for operations that may throw an exception:
/app/api/route.ts
TypeScript
JavaScript TypeScript
```
import { submit } from '@/lib/submit'

export async function POST(request: Request) {
  try {
    await submit(request)
    return new Response(null, { status: 204 })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected error'

    return new Response(message, { status: 500 })
  }
}
```

Avoid exposing sensitive information in error messages sent to the client.
To restrict access, implement authentication and authorization. See [Authentication](https://nextjs.org/docs/app/guides/authentication).
