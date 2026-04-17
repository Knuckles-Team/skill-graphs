# API Routes
Last updated February 27, 2026
Examples
> **Good to know** : If you are using the App Router, you can use [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) or [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) instead of API Routes.
API routes provide a solution to build a **public API** with Next.js.
Any file inside the folder `pages/api` is mapped to `/api/*` and will be treated as an API endpoint instead of a `page`. They are server-side only bundles and won't increase your client-side bundle size.
For example, the following API route returns a JSON response with a status code of `200`:
pages/api/hello.ts
TypeScript
JavaScript TypeScript
```
import type { NextApiRequest, NextApiResponse } from 'next'

type ResponseData = {
  message: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

> **Good to know** :
>   * API Routes **same-origin only** by default. You can customize such behavior by wrapping the request handler with the
>   * API Routes can't be used with [static exports](https://nextjs.org/docs/pages/guides/static-exports). However, [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) in the App Router can.
>   * API Routes will be affected by [`pageExtensions` configuration](https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions) in `next.config.js`.
>
