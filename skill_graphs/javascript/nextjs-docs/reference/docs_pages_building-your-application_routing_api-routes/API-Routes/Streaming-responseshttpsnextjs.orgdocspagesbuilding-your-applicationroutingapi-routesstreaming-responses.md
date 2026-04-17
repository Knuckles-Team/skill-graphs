## Streaming responses[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#streaming-responses)
While the Pages Router does support streaming responses with API Routes, we recommend incrementally adopting the App Router and using [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) if you are on Next.js 14+.
Here's how you can stream a response from an API Route with `writeHead`:
pages/api/hello.ts
TypeScript
JavaScript TypeScript
```
import { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-store',
  })
  let i = 0
  while (i < 10) {
    res.write(`data: ${i}\n\n`)
    i++
    await new Promise((resolve) => setTimeout(resolve, 1000))
  }
  res.end()
}
```

Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
