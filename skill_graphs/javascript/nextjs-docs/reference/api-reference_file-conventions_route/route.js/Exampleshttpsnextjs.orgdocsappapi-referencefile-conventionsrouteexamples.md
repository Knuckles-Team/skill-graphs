## Examples[](https://nextjs.org/docs/app/api-reference/file-conventions/route#examples)
### Cookies[](https://nextjs.org/docs/app/api-reference/file-conventions/route#cookies)
You can read or set cookies with [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) from `next/headers`.
route.ts
TypeScript
JavaScript TypeScript
```
import { cookies } from 'next/headers'

export async function GET(request: NextRequest) {
  const cookieStore = await cookies()

  const a = cookieStore.get('a')
  const b = cookieStore.set('b', '1')
  const c = cookieStore.delete('c')
}
```

Alternatively, you can return a new `Response` using the
app/api/route.ts
TypeScript
JavaScript TypeScript
```
import { cookies } from 'next/headers'

export async function GET(request: Request) {
  const cookieStore = await cookies()
  const token = cookieStore.get('token')

  return new Response('Hello, Next.js!', {
    status: 200,
    headers: { 'Set-Cookie': `token=${token.value}` },
  })
}
```

You can also use the underlying Web APIs to read cookies from the request ([`NextRequest`](https://nextjs.org/docs/app/api-reference/functions/next-request)):
app/api/route.ts
TypeScript
JavaScript TypeScript
```
import { type NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const token = request.cookies.get('token')
}
```

### Headers[](https://nextjs.org/docs/app/api-reference/file-conventions/route#headers)
You can read headers with [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers) from `next/headers`.
route.ts
TypeScript
JavaScript TypeScript
```
import { headers } from 'next/headers'
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const headersList = await headers()
  const referer = headersList.get('referer')
}
```

This `headers` instance is read-only. To set headers, you need to return a new `Response` with new `headers`.
app/api/route.ts
TypeScript
JavaScript TypeScript
```
import { headers } from 'next/headers'

export async function GET(request: Request) {
  const headersList = await headers()
  const referer = headersList.get('referer')

  return new Response('Hello, Next.js!', {
    status: 200,
    headers: { referer: referer },
  })
}
```

You can also use the underlying Web APIs to read headers from the request ([`NextRequest`](https://nextjs.org/docs/app/api-reference/functions/next-request)):
app/api/route.ts
TypeScript
JavaScript TypeScript
```
import { type NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const requestHeaders = new Headers(request.headers)
}
```

### Revalidating Cached Data[](https://nextjs.org/docs/app/api-reference/file-conventions/route#revalidating-cached-data)
You can [revalidate cached data](https://nextjs.org/docs/app/guides/incremental-static-regeneration) using the `revalidate` route segment config option.
app/posts/route.ts
TypeScript
JavaScript TypeScript
```
export const revalidate = 60

export async function GET() {
  const data = await fetch('https://api.vercel.app/blog')
  const posts = await data.json()

  return Response.json(posts)
}
```

### Redirects[](https://nextjs.org/docs/app/api-reference/file-conventions/route#redirects)
app/api/route.ts
TypeScript
JavaScript TypeScript
```
import { redirect } from 'next/navigation'

export async function GET(request: Request) {
  redirect('https://nextjs.org/')
}
```

### Dynamic Route Segments[](https://nextjs.org/docs/app/api-reference/file-conventions/route#dynamic-route-segments)
Route Handlers can use [Dynamic Segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes) to create request handlers from dynamic data.
app/items/[slug]/route.ts
TypeScript
JavaScript TypeScript
```
export async function GET(
  request: Request,
  { params }: { params: Promise<{ slug: string }> }
) {
  const { slug } = await params // 'a', 'b', or 'c'
}
```

Route | Example URL | `params`
---|---|---
`app/items/[slug]/route.js` | `/items/a` | `Promise<{ slug: 'a' }>`
`app/items/[slug]/route.js` | `/items/b` | `Promise<{ slug: 'b' }>`
`app/items/[slug]/route.js` | `/items/c` | `Promise<{ slug: 'c' }>`
#### Static Generation with `generateStaticParams`[](https://nextjs.org/docs/app/api-reference/file-conventions/route#static-generation-with-generatestaticparams)
You can use [`generateStaticParams`](https://nextjs.org/docs/app/api-reference/functions/generate-static-params) with dynamic Route Handlers to statically generate responses at build time for specified params, while handling other params dynamically at request time.
When using [Cache Components](https://nextjs.org/docs/app/getting-started/cache-components), you can combine `generateStaticParams` with `use cache` to enable data caching for both prerendered and runtime params.
See the [generateStaticParams with Route Handlers](https://nextjs.org/docs/app/api-reference/functions/generate-static-params#with-route-handlers) documentation for examples and details.
### URL Query Parameters[](https://nextjs.org/docs/app/api-reference/file-conventions/route#url-query-parameters)
The request object passed to the Route Handler is a `NextRequest` instance, which includes [some additional convenience methods](https://nextjs.org/docs/app/api-reference/functions/next-request#nexturl), such as those for more easily handling query parameters.
app/api/search/route.ts
TypeScript
JavaScript TypeScript
```
import { type NextRequest } from 'next/server'

export function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams
  const query = searchParams.get('query')
  // query is "hello" for /api/search?query=hello
}
```

### Streaming[](https://nextjs.org/docs/app/api-reference/file-conventions/route#streaming)
Streaming is commonly used in combination with Large Language Models (LLMs), such as OpenAI, for AI-generated content. Learn more about the
app/api/chat/route.ts
TypeScript
JavaScript TypeScript
```
import { openai } from '@ai-sdk/openai'
import { StreamingTextResponse, streamText } from 'ai'

export async function POST(req: Request) {
  const { messages } = await req.json()
  const result = await streamText({
    model: openai('gpt-4-turbo'),
    messages,
  })

  return new StreamingTextResponse(result.toAIStream())
}
```

These abstractions use the Web APIs to create a stream. You can also use the underlying Web APIs directly.
app/api/route.ts
TypeScript
JavaScript TypeScript
```
// https://developer.mozilla.org/docs/Web/API/ReadableStream#convert_async_iterator_to_stream
function iteratorToStream(iterator: any) {
  return new ReadableStream({
    async pull(controller) {
      const { value, done } = await iterator.next()

      if (done) {
        controller.close()
      } else {
        controller.enqueue(value)
      }
    },
  })
}

function sleep(time: number) {
  return new Promise((resolve) => {
    setTimeout(resolve, time)
  })
}

const encoder = new TextEncoder()

async function* makeIterator() {
  yield encoder.encode('<p>One</p>')
  await sleep(200)
  yield encoder.encode('<p>Two</p>')
  await sleep(200)
  yield encoder.encode('<p>Three</p>')
}

export async function GET() {
  const iterator = makeIterator()
  const stream = iteratorToStream(iterator)

  return new Response(stream)
}
```

### Request Body[](https://nextjs.org/docs/app/api-reference/file-conventions/route#request-body)
You can read the `Request` body using the standard Web API methods:
app/items/route.ts
TypeScript
JavaScript TypeScript
```
export async function POST(request: Request) {
  const res = await request.json()
  return Response.json({ res })
}
```

### Request Body FormData[](https://nextjs.org/docs/app/api-reference/file-conventions/route#request-body-formdata)
You can read the `FormData` using the `request.formData()` function:
app/items/route.ts
TypeScript
JavaScript TypeScript
```
export async function POST(request: Request) {
  const formData = await request.formData()
  const name = formData.get('name')
  const email = formData.get('email')
  return Response.json({ name, email })
}
```

Since `formData` data are all strings, you may want to use `number`).
### CORS[](https://nextjs.org/docs/app/api-reference/file-conventions/route#cors)
You can set CORS headers for a specific Route Handler using the standard Web API methods:
app/api/route.ts
TypeScript
JavaScript TypeScript
```
export async function GET(request: Request) {
  return new Response('Hello, Next.js!', {
    status: 200,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    },
  })
}
```

> **Good to know** :
>   * To add CORS headers to multiple Route Handlers, you can use [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#cors) or the [`next.config.js` file](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers#cors).
>

### Webhooks[](https://nextjs.org/docs/app/api-reference/file-conventions/route#webhooks)
You can use a Route Handler to receive webhooks from third-party services:
app/api/route.ts
TypeScript
JavaScript TypeScript
```
export async function POST(request: Request) {
  try {
    const text = await request.text()
    // Process the webhook payload
  } catch (error) {
    return new Response(`Webhook error: ${error.message}`, {
      status: 400,
    })
  }

  return new Response('Success!', {
    status: 200,
  })
}
```

Notably, unlike API Routes with the Pages Router, you do not need to use `bodyParser` to use any additional configuration.
### Non-UI Responses[](https://nextjs.org/docs/app/api-reference/file-conventions/route#non-ui-responses)
You can use Route Handlers to return non-UI content. Note that [`sitemap.xml`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generating-a-sitemap-using-code-js-ts), [`robots.txt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file), [`app icons`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx), and [open graph images](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image) all have built-in support.
app/rss.xml/route.ts
TypeScript
JavaScript TypeScript
```
export async function GET() {
  return new Response(
    `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>Next.js Documentation</title>
  <link>https://nextjs.org/docs</link>
  <description>The React Framework for the Web</description>
</channel>

</rss>`,
    {
      headers: {
        'Content-Type': 'text/xml',
      },
    }
  )
}
```

### Segment Config Options[](https://nextjs.org/docs/app/api-reference/file-conventions/route#segment-config-options)
Route Handlers use the same [route segment configuration](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) as pages and layouts.
app/items/route.ts
TypeScript
JavaScript TypeScript
```
export const dynamic = 'auto'
export const dynamicParams = true
export const revalidate = false
export const fetchCache = 'auto'
export const runtime = 'nodejs'
export const preferredRegion = 'auto'
```

See the [API reference](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) for more details.
