## Security[](https://nextjs.org/docs/app/guides/backend-for-frontend#security)
### Working with headers[](https://nextjs.org/docs/app/guides/backend-for-frontend#working-with-headers)
Be deliberate about where headers go, and avoid directly passing incoming request headers to the outgoing response.
  * **Upstream request headers** : In Proxy, `NextResponse.next({ request: { headers } })` modifies the headers your server receives and does not expose them to the client.
  * **Response headers** : `new Response(..., { headers })`, `NextResponse.json(..., { headers })`, `NextResponse.next({ headers })`, or `response.headers.set(...)` send headers back to the client. If sensitive values were appended to these headers, they will be visible to clients.


Learn more in [NextResponse headers in Proxy](https://nextjs.org/docs/app/api-reference/functions/next-response#next).
### Rate limiting[](https://nextjs.org/docs/app/guides/backend-for-frontend#rate-limiting)
You can implement rate limiting in your Next.js backend. In addition to code-based checks, enable any rate limiting features provided by your host.
/app/resource/route.ts
TypeScript
JavaScript TypeScript
```
import { NextResponse } from 'next/server'
import { checkRateLimit } from '@/lib/rate-limit'

export async function POST(request: Request) {
  const { rateLimited } = await checkRateLimit(request)

  if (rateLimited) {
    return NextResponse.json({ error: 'Rate limit exceeded' }, { status: 429 })
  }

  return new Response(null, { status: 204 })
}
```

### Verify payloads[](https://nextjs.org/docs/app/guides/backend-for-frontend#verify-payloads)
Never trust incoming request data. Validate content type and size, and sanitize against XSS before use.
Use timeouts to prevent abuse and protect server resources.
Store user-generated static assets in dedicated services. When possible, upload them from the browser and store the returned URI in your database to reduce request size.
### Access to protected resources[](https://nextjs.org/docs/app/guides/backend-for-frontend#access-to-protected-resources)
Always verify credentials before granting access. Do not rely on proxy alone for authentication and authorization.
Remove sensitive or unnecessary data from responses and backend logs.
Rotate credentials and API keys regularly.
