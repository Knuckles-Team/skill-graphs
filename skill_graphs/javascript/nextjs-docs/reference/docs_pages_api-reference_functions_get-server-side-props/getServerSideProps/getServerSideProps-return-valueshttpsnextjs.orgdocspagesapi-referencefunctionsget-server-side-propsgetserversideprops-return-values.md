## getServerSideProps return values[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#getserversideprops-return-values)
The `getServerSideProps` function should return an object with **any one of the following** properties:
###  `props`[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#props)
The `props` object is a key-value pair, where each value is received by the page component. It should be a
```
export async function getServerSideProps(context) {
  return {
    props: { message: `Next.js is awesome` }, // will be passed to the page component as props
  }
}
```

###  `notFound`[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#notfound)
The `notFound` boolean allows the page to return a `404` status and [404 Page](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#404-page). With `notFound: true`, the page will return a `404` even if there was a successfully generated page before. This is meant to support use cases like user-generated content getting removed by its author.
```
export async function getServerSideProps(context) {
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

###  `redirect`[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#redirect)
The `redirect` object allows redirecting to internal and external resources. It should match the shape of `{ destination: string, permanent: boolean }`. In some rare cases, you might need to assign a custom status code for older `HTTP` clients to properly redirect. In these cases, you can use the `statusCode` property instead of the `permanent` property, but not both.
```
export async function getServerSideProps(context) {
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  if (!data) {
    return {
      redirect: {
        destination: '/',
        permanent: false,
      },
    }
  }

  return {
    props: {}, // will be passed to the page component as props
  }
}
```
