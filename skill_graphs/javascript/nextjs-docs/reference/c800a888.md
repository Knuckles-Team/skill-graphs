## Route Handlers[](https://nextjs.org/docs/app/guides/upgrading/version-15#route-handlers-1)
`GET` functions in [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route) are no longer cached by default. To opt `GET` methods into caching, you can use a [route config option](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config) such as `export const dynamic = 'force-static'` in your Route Handler file.
app/api/route.js
```
export const dynamic = 'force-static'

export async function GET() {}
```
