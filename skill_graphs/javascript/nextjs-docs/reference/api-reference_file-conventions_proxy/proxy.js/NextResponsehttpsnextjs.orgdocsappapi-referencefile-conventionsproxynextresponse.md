## NextResponse[](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#nextresponse)
The `NextResponse` API allows you to:
  * `redirect` the incoming request to a different URL
  * `rewrite` the response by displaying a given URL
  * Set request headers for API Routes, `getServerSideProps`, and `rewrite` destinations
  * Set response cookies
  * Set response headers


To produce a response from Proxy, you can:
  1. `rewrite` to a route ([Page](https://nextjs.org/docs/app/api-reference/file-conventions/page) or [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route)) that produces a response
  2. return a `NextResponse` directly. See [Producing a Response](https://nextjs.org/docs/app/api-reference/file-conventions/proxy#producing-a-response)


> **Good to know** : For redirects, you can also use `Response.redirect` instead of `NextResponse.redirect`.
