## Dynamic API Routes[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#dynamic-api-routes)
API Routes support [dynamic routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes), and follow the same file naming rules used for `pages/`.
pages/api/post/[pid].ts
TypeScript
JavaScript TypeScript
```
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { pid } = req.query
  res.end(`Post: ${pid}`)
}
```

Now, a request to `/api/post/abc` will respond with the text: `Post: abc`.
### Catch all API routes[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#catch-all-api-routes)
API Routes can be extended to catch all paths by adding three dots (`...`) inside the brackets. For example:
  * `pages/api/post/[...slug].js` matches `/api/post/a`, but also `/api/post/a/b`, `/api/post/a/b/c` and so on.


> **Good to know** : You can use names other than `slug`, such as: `[...param]`
Matched parameters will be sent as a query parameter (`slug` in the example) to the page, and it will always be an array, so, the path `/api/post/a` will have the following `query` object:
```
{ "slug": ["a"] }
```

And in the case of `/api/post/a/b`, and any other matching path, new parameters will be added to the array, like so:
```
{ "slug": ["a", "b"] }
```

For example:
pages/api/post/[...slug].ts
TypeScript
JavaScript TypeScript
```
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { slug } = req.query
  res.end(`Post: ${slug.join(', ')}`)
}
```

Now, a request to `/api/post/a/b/c` will respond with the text: `Post: a, b, c`.
### Optional catch all API routes[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#optional-catch-all-api-routes)
Catch all routes can be made optional by including the parameter in double brackets (`[[...slug]]`).
For example, `pages/api/post/[[...slug]].js` will match `/api/post`, `/api/post/a`, `/api/post/a/b`, and so on.
The main difference between catch all and optional catch all routes is that with optional, the route without the parameter is also matched (`/api/post` in the example above).
The `query` objects are as follows:
```
{ } // GET `/api/post` (empty object)
{ "slug": ["a"] } // `GET /api/post/a` (single-element array)
{ "slug": ["a", "b"] } // `GET /api/post/a/b` (multi-element array)
```

### Caveats[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#caveats)
  * Predefined API routes take precedence over dynamic API routes, and dynamic API routes over catch all API routes. Take a look at the following examples:
    * `pages/api/post/create.js` - Will match `/api/post/create`
    * `pages/api/post/[pid].js` - Will match `/api/post/1`, `/api/post/abc`, etc. But not `/api/post/create`
    * `pages/api/post/[...slug].js` - Will match `/api/post/1/2`, `/api/post/a/b/c`, etc. But not `/api/post/create`, `/api/post/abc`
