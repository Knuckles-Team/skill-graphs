## Proxying to a backend[](https://nextjs.org/docs/app/guides/backend-for-frontend#proxying-to-a-backend)
You can use a Route Handler as a `proxy` to another backend. Add validation logic before forwarding the request.
/app/api/[...slug]/route.ts
TypeScript
JavaScript TypeScript
```
import { isValidRequest } from '@/lib/utils'

export async function POST(request: Request, { params }) {
  const clonedRequest = request.clone()
  const isValid = await isValidRequest(clonedRequest)

  if (!isValid) {
    return new Response(null, { status: 400, statusText: 'Bad Request' })
  }

  const { slug } = await params
  const pathname = slug.join('/')
  const proxyURL = new URL(pathname, 'https://nextjs.org')
  const proxyRequest = new Request(proxyURL, request)

  try {
    return fetch(proxyRequest)
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'

    return new Response(message, { status: 500 })
  }
}
```

Or use:
  * `proxy` [rewrites](https://nextjs.org/docs/app/guides/backend-for-frontend#proxy)
  * [`rewrites`](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites) in `next.config.js`.
