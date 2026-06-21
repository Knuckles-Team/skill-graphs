## Edge Cases[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#edge-cases)
### Caching with Server-Side Rendering (SSR)[](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props#caching-with-server-side-rendering-ssr)
You can use caching headers (`Cache-Control`) inside `getServerSideProps` to cache dynamic responses. For example, using
```
// This value is considered fresh for ten seconds (s-maxage=10).
// If a request is repeated within the next 10 seconds, the previously
// cached value will still be fresh. If the request is repeated before 59 seconds,
// the cached value will be stale but still render (stale-while-revalidate=59).
//
// In the background, a revalidation request will be made to populate the cache
// with a fresh value. If you refresh the page, you will see the new value.
export async function getServerSideProps({ req, res }) {
  res.setHeader(
    'Cache-Control',
    'public, s-maxage=10, stale-while-revalidate=59'
  )

  return {
    props: {},
  }
}
```

However, before reaching for `cache-control`, we recommend seeing if [`getStaticProps`](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props) with [ISR](https://nextjs.org/docs/pages/guides/incremental-static-regeneration) is a better fit for your use case.
Was this helpful?
Send
