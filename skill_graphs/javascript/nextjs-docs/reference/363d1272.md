## Cache-Control[](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers#cache-control)
Next.js sets the `Cache-Control` header of `public, max-age=31536000, immutable` for truly immutable assets. It cannot be overridden. These immutable files contain a SHA-hash in the file name, so they can be safely cached indefinitely. For example, [Static Image Imports](https://nextjs.org/docs/app/getting-started/images#local-images). You cannot set `Cache-Control` headers in `next.config.js` for these assets.
However, you can set `Cache-Control` headers for other responses or data.
If you need to revalidate the cache of a page that has been [statically generated](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation), you can do so by setting the `revalidate` prop in the page's [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) function.
To cache the response from an [API Route](https://nextjs.org/docs/pages/building-your-application/routing/api-routes), you can use `res.setHeader`:
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
  res.setHeader('Cache-Control', 's-maxage=86400')
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

You can also use caching headers (`Cache-Control`) inside `getServerSideProps` to cache dynamic responses. For example, using
pages/index.tsx
TypeScript
JavaScript TypeScript
```
import { GetStaticProps, GetStaticPaths, GetServerSideProps } from 'next'

// This value is considered fresh for ten seconds (s-maxage=10).
// If a request is repeated within the next 10 seconds, the previously
// cached value will still be fresh. If the request is repeated before 59 seconds,
// the cached value will be stale but still render (stale-while-revalidate=59).
//
// In the background, a revalidation request will be made to populate the cache
// with a fresh value. If you refresh the page, you will see the new value.
export const getServerSideProps = (async (context) => {
  context.res.setHeader(
    'Cache-Control',
    'public, s-maxage=10, stale-while-revalidate=59'
  )

  return {
    props: {},
  }
}) satisfies GetServerSideProps
```
