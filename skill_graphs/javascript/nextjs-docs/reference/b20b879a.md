## Managing redirects at scale (advanced)[](https://nextjs.org/docs/pages/guides/redirecting#managing-redirects-at-scale-advanced)
To manage a large number of redirects (1000+), you may consider creating a custom solution using Proxy. This allows you to handle redirects programmatically without having to redeploy your application.
To do this, you'll need to consider:
  1. Creating and storing a redirect map.
  2. Optimizing data lookup performance.


> **Next.js Example** : See our
### 1. Creating and storing a redirect map[](https://nextjs.org/docs/pages/guides/redirecting#1-creating-and-storing-a-redirect-map)
A redirect map is a list of redirects that you can store in a database (usually a key-value store) or JSON file.
Consider the following data structure:
```
{
  "/old": {
    "destination": "/new",
    "permanent": true
  },
  "/blog/post-old": {
    "destination": "/blog/post-new",
    "permanent": true
  }
}
```

In [Proxy](https://nextjs.org/docs/app/api-reference/file-conventions/proxy), you can read from a database such as Vercel's
proxy.ts
TypeScript
JavaScript TypeScript
```
import { NextResponse, NextRequest } from 'next/server'
import { get } from '@vercel/edge-config'

type RedirectEntry = {
  destination: string
  permanent: boolean
}

export async function proxy(request: NextRequest) {
  const pathname = request.nextUrl.pathname
  const redirectData = await get(pathname)

  if (redirectData && typeof redirectData === 'string') {
    const redirectEntry: RedirectEntry = JSON.parse(redirectData)
    const statusCode = redirectEntry.permanent ? 308 : 307
    return NextResponse.redirect(redirectEntry.destination, statusCode)
  }

  // No redirect found, continue without redirecting
  return NextResponse.next()
}
```

### 2. Optimizing data lookup performance[](https://nextjs.org/docs/pages/guides/redirecting#2-optimizing-data-lookup-performance)
Reading a large dataset for every incoming request can be slow and expensive. There are two ways you can optimize data lookup performance:
  * Use a database that is optimized for fast reads
  * Use a data lookup strategy such as a **before** reading the larger redirects file or database.


Considering the previous example, you can import a generated bloom filter file into Proxy, then, check if the incoming request pathname exists in the bloom filter.
If it does, forward the request to a  [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes) which will check the actual file and redirect the user to the appropriate URL. This avoids importing a large redirects file into Proxy, which can slow down every incoming request.
proxy.ts
TypeScript
JavaScript TypeScript
```
import { NextResponse, NextRequest } from 'next/server'
import { ScalableBloomFilter } from 'bloom-filters'
import GeneratedBloomFilter from './redirects/bloom-filter.json'

type RedirectEntry = {
  destination: string
  permanent: boolean
}

// Initialize bloom filter from a generated JSON file
const bloomFilter = ScalableBloomFilter.fromJSON(GeneratedBloomFilter as any)

export async function proxy(request: NextRequest) {
  // Get the path for the incoming request
  const pathname = request.nextUrl.pathname

  // Check if the path is in the bloom filter
  if (bloomFilter.has(pathname)) {
    // Forward the pathname to the Route Handler
    const api = new URL(
      `/api/redirects?pathname=${encodeURIComponent(request.nextUrl.pathname)}`,
      request.nextUrl.origin
    )

    try {
      // Fetch redirect data from the Route Handler
      const redirectData = await fetch(api)

      if (redirectData.ok) {
        const redirectEntry: RedirectEntry | undefined =
          await redirectData.json()

        if (redirectEntry) {
          // Determine the status code
          const statusCode = redirectEntry.permanent ? 308 : 307

          // Redirect to the destination
          return NextResponse.redirect(redirectEntry.destination, statusCode)
        }
      }
    } catch (error) {
      console.error(error)
    }
  }

  // No redirect found, continue the request without redirecting
  return NextResponse.next()
}
```

Then, in the API Route:
pages/api/redirects.ts
TypeScript
JavaScript TypeScript
```
import type { NextApiRequest, NextApiResponse } from 'next'
import redirects from '@/app/redirects/redirects.json'

type RedirectEntry = {
  destination: string
  permanent: boolean
}

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const pathname = req.query.pathname
  if (!pathname) {
    return res.status(400).json({ message: 'Bad Request' })
  }

  // Get the redirect entry from the redirects.json file
  const redirect = (redirects as Record<string, RedirectEntry>)[pathname]

  // Account for bloom filter false positives
  if (!redirect) {
    return res.status(400).json({ message: 'No redirect' })
  }

  // Return the redirect entry
  return res.json(redirect)
}
```

> **Good to know:**
>   * To generate a bloom filter, you can use a library like
>   * You should validate requests made to your Route Handler to prevent malicious requests.
>

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
