## getStaticProps return values[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#getstaticprops-return-values)
The `getStaticProps` function should return an object containing either `props`, `redirect`, or `notFound` followed by an **optional** `revalidate` property.
###  `props`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#props)
The `props` object is a key-value pair, where each value is received by the page component. It should be a
```
export async function getStaticProps(context) {
  return {
    props: { message: `Next.js is awesome` }, // will be passed to the page component as props
  }
}
```

###  `revalidate`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#revalidate)
The `revalidate` property is the amount in seconds after which a page re-generation can occur (defaults to `false` or no revalidation).
```
// This function gets called at build time on server-side.
// It may be called again, on a serverless function, if
// revalidation is enabled and a new request comes in
export async function getStaticProps() {
  const res = await fetch('https://.../posts')
  const posts = await res.json()

  return {
    props: {
      posts,
    },
    // Next.js will attempt to re-generate the page:
    // - When a request comes in
    // - At most once every 10 seconds
    revalidate: 10, // In seconds
  }
}
```

Learn more about [Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration).
The cache status of a page leveraging ISR can be determined by reading the value of the `x-nextjs-cache` response header. The possible values are the following:
  * `MISS` - the path is not in the cache (occurs at most once, on the first visit)
  * `STALE` - the path is in the cache but exceeded the revalidate time so it will be updated in the background
  * `HIT` - the path is in the cache and has not exceeded the revalidate time


###  `notFound`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#notfound)
The `notFound` boolean allows the page to return a `404` status and [404 Page](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#404-page). With `notFound: true`, the page will return a `404` even if there was a successfully generated page before. This is meant to support use cases like user-generated content getting removed by its author. Note, `notFound` follows the same `revalidate` behavior [described here](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#revalidate).
```
export async function getStaticProps(context) {
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  if (!data) {
    return {
      notFound: true,
    }
  }

  return {
    props: { data }, // will be passed to the page component as props
  }
}
```

> **Good to know** : `notFound` is not needed for [`fallback: false`](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths#fallback-false) mode as only paths returned from `getStaticPaths` will be pre-rendered.
###  `redirect`[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#redirect)
The `redirect` object allows redirecting to internal or external resources. It should match the shape of `{ destination: string, permanent: boolean }`.
In some rare cases, you might need to assign a custom status code for older `HTTP` clients to properly redirect. In these cases, you can use the `statusCode` property instead of the `permanent` property, **but not both**. You can also set `basePath: false` similar to redirects in `next.config.js`.
```
export async function getStaticProps(context) {
  const res = await fetch(`https://...`)
  const data = await res.json()

  if (!data) {
    return {
      redirect: {
        destination: '/',
        permanent: false,
        // statusCode: 301
      },
    }
  }

  return {
    props: { data }, // will be passed to the page component as props
  }
}
```

If the redirects are known at build-time, they should be added in [`next.config.js`](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects) instead.
