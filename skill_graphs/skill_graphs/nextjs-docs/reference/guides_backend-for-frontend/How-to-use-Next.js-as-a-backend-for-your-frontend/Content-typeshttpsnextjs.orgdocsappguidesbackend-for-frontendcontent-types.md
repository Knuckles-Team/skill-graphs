## Content types[](https://nextjs.org/docs/app/guides/backend-for-frontend#content-types)
Route Handlers let you serve non-UI responses, including JSON, XML, images, files, and plain text.
Next.js uses file conventions for common endpoints:
  * [`sitemap.xml`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)
  * [`opengraph-image.jpg`, `twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
  * [favicon, app icon, and apple-icon](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)
  * [`manifest.json`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
  * [`robots.txt`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)


You can also define custom ones, such as:
  * `llms.txt`
  * `rss.xml`
  * `.well-known`


For example, `app/rss.xml/route.ts` creates a Route Handler for `rss.xml`.
/app/rss.xml/route.ts
TypeScript
JavaScript TypeScript
```
export async function GET(request: Request) {
  const rssResponse = await fetch(/* rss endpoint */)
  const rssData = await rssResponse.json()

  const rssFeed = `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
 <title>${rssData.title}</title>
 <description>${rssData.description}</description>
 <link>${rssData.link}</link>
 <copyright>${rssData.copyright}</copyright>
 ${rssData.items.map((item) => {
   return `<item>
    <title>${item.title}</title>
    <description>${item.description}</description>
    <link>${item.link}</link>
    <pubDate>${item.publishDate}</pubDate>
    <guid isPermaLink="false">${item.guid}</guid>
 </item>`
 })}
</channel>
</rss>`

  const headers = new Headers({ 'content-type': 'application/xml' })

  return new Response(rssFeed, { headers })
}
```

Sanitize any input used to generate markup.
### Content negotiation[](https://nextjs.org/docs/app/guides/backend-for-frontend#content-negotiation)
You can use [rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites) with header matching to serve different content types from the same URL based on the request's `Accept` header. This is known as
For example, a documentation site might serve HTML pages to browsers and raw Markdown to AI agents from the same `/docs/…` URLs.
**1. Configure a rewrite that matches the`Accept` header:**
next.config.js
```
module.exports = {
  async rewrites() {
    return [
      {
        source: '/docs/:slug*',
        destination: '/docs/md/:slug*',
        has: [
          {
            type: 'header',
            key: 'accept',
            value: '(.*)text/markdown(.*)',
          },
        ],
      },
    ]
  },
}
```

When a request to `/docs/getting-started` includes `Accept: text/markdown`, the rewrite routes it to `/docs/md/getting-started`. A Route Handler at that path returns the Markdown response. Clients that do not send `text/markdown` in their `Accept` header continue to receive the normal HTML page.
**2. Create a Route Handler for the Markdown response:**
app/docs/md/[...slug]/route.ts
TypeScript
JavaScript TypeScript
```
import { getDocsMd, generateDocsStaticParams } from '@/lib/docs'

export async function generateStaticParams() {
  return generateDocsStaticParams()
}

export async function GET(_: Request, ctx: RouteContext<'/docs/md/[...slug]'>) {
  const { slug } = await ctx.params
  const mdDoc = await getDocsMd({ slug })

  if (mdDoc == null) {
    return new Response(null, { status: 404 })
  }

  return new Response(mdDoc, {
    headers: {
      'Content-Type': 'text/markdown; charset=utf-8',
      Vary: 'Accept',
    },
  })
}
```

The `Accept` request header. Without it, a shared cache could serve a cached Markdown response to a browser (or vice versa). Most hosting providers already include the `Accept` header in their cache key, but setting `Vary` explicitly ensures correct behavior across all CDNs and proxy caches.
`generateStaticParams` lets you pre-render the Markdown variants at build time so they can be served from the edge without hitting the origin server on every request.
**3. Test it with`curl` :**
```
# Returns Markdown
curl -H "Accept: text/markdown" https://example.com/docs/getting-started

# Returns the normal HTML page
curl https://example.com/docs/getting-started
```

> **Good to know:**
>   * The `/docs/md/...` route is still directly accessible without the rewrite. If you want to restrict it to only serve via the rewrite, use [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) to block direct requests that don't include the expected `Accept` header.
>   * For more advanced negotiation logic, you can use [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) instead of rewrites for more flexibility.
>

### Consuming request payloads[](https://nextjs.org/docs/app/guides/backend-for-frontend#consuming-request-payloads)
Use Request `.json()`, `.formData()`, or `.text()` to access the request body.
`GET` and `HEAD` requests don’t carry a body.
/app/api/echo-body/route.ts
TypeScript
JavaScript TypeScript
```
export async function POST(request: Request) {
  const res = await request.json()
  return Response.json({ res })
}
```

> **Good to know** : Validate data before passing it to other systems
/app/api/send-email/route.ts
TypeScript
JavaScript TypeScript
```
import { sendMail, validateInputs } from '@/lib/email-transporter'

export async function POST(request: Request) {
  const formData = await request.formData()
  const email = formData.get('email')
  const contents = formData.get('contents')

  try {
    await validateInputs({ email, contents })
    const info = await sendMail({ email, contents })

    return Response.json({ messageId: info.messageId })
  } catch (reason) {
    const message =
      reason instanceof Error ? reason.message : 'Unexpected exception'

    return new Response(message, { status: 500 })
  }
}
```

You can only read the request body once. Clone the request if you need to read it again:
/app/api/clone/route.ts
TypeScript
JavaScript TypeScript
```
export async function POST(request: Request) {
  try {
    const clonedRequest = request.clone()

    await request.body()
    await clonedRequest.body()
    await request.body() // Throws error

    return new Response(null, { status: 204 })
  } catch {
    return new Response(null, { status: 500 })
  }
}
```
