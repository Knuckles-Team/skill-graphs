## Advanced Proxy flags[](https://nextjs.org/docs/pages/api-reference/file-conventions/proxy#advanced-proxy-flags)
In `v13.1` of Next.js two additional flags were introduced for proxy, `skipMiddlewareUrlNormalize` and `skipTrailingSlashRedirect` to handle advanced use cases.
`skipTrailingSlashRedirect` disables Next.js redirects for adding or removing trailing slashes. This allows custom handling inside proxy to maintain the trailing slash for some paths but not others, which can make incremental migrations easier.
next.config.js
```
module.exports = {
  skipTrailingSlashRedirect: true,
}
```

proxy.js
```
const legacyPrefixes = ['/docs', '/blog']

export default async function proxy(req) {
  const { pathname } = req.nextUrl

  if (legacyPrefixes.some((prefix) => pathname.startsWith(prefix))) {
    return NextResponse.next()
  }

  // apply trailing slash handling
  if (
    !pathname.endsWith('/') &&
    !pathname.match(/((?!\.well-known(?:\/.*)?)(?:[^/]+\/)*[^/]+\.\w+)/)
  ) {
    return NextResponse.redirect(
      new URL(`${req.nextUrl.pathname}/`, req.nextUrl)
    )
  }
}
```

`skipMiddlewareUrlNormalize` allows for disabling the URL normalization in Next.js to make handling direct visits and client-transitions the same. In some advanced cases, this option provides full control by using the original URL.
next.config.js
```
module.exports = {
  skipMiddlewareUrlNormalize: true,
}
```

proxy.js
```
export default async function proxy(req) {
  const { pathname } = req.nextUrl

  // GET /_next/data/build-id/hello.json

  console.log(pathname)
  // with the flag this now /_next/data/build-id/hello.json
  // without the flag this would be normalized to /hello
}
```
