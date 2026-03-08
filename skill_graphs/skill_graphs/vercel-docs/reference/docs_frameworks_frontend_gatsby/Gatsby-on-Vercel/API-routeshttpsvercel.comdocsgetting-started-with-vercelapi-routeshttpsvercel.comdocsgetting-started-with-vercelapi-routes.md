##  [API routes](https://vercel.com/docs/getting-started-with-vercel#api-routes)[](https://vercel.com/docs/getting-started-with-vercel#api-routes)
You can add API Routes to your Gatsby site using the framework's native support for the `src/api` directory. Doing so will deploy your routes as [Vercel functions](https://vercel.com/docs/functions). These Vercel functions can be used to fetch data from external sources, or to add custom endpoints to your application.
The following example demonstrates a basic API Route using Vercel functions:
src/api/handler.ts
TypeScript
TypeScript JavaScript Bash
```
import type { VercelRequest, VercelResponse } from '@vercel/node';

export default function handler(
  request: VercelRequest,
  response: VercelResponse,
) {
  response.status(200).json({
    body: request.body,
    query: request.query,
    cookies: request.cookies,
  });
}
```

To view your route locally, run the following command in your terminal:
terminal
```
gatsby develop
```

Then navigate to `http://localhost:8000/api/handler` in your web browser.
###  [Dynamic API routes](https://vercel.com/docs/getting-started-with-vercel#dynamic-api-routes)[](https://vercel.com/docs/getting-started-with-vercel#dynamic-api-routes)
Vercel does not currently have first-class support for dynamic API routes in Gatsby. For now, using them requires the workaround described in this section.
To use Gatsby's Dynamic API routes on Vercel, you must:
  1. Define your dynamic routes in a `vercel.json` file at the root directory of your project, as shown below:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/api/blog/:id",
      "destination": "/api/blog/[id]"
    }
  ]
}
```

  2. Read your dynamic parameters from `req.query`, as shown below:
api/blog/[id].ts
TypeScript
TypeScript JavaScript Bash
```
import type { VercelRequest, VercelResponse } from '@vercel/node';

export default function handler(
  request: VercelRequest & { params: { id: string } },
  response: VercelResponse,
) {
  console.log(`/api/blog/${request.query.id}`);
  response.status(200).json({
    body: request.body,
    query: request.query,
    cookies: request.cookies,
  });
}
```



Although typically you'd access the dynamic parameter with `request.param` when using Gatsby, you must use `request.query` on Vercel.
###  [Splat API routes](https://vercel.com/docs/getting-started-with-vercel#splat-api-routes)[](https://vercel.com/docs/getting-started-with-vercel#splat-api-routes)
Splat API routes are dynamic wildcard routes that will match anything after the splat (`[...]`). Vercel does not currently have first-class support for splat API routes in Gatsby. For now, using them requires the workaround described in this section.
To use Gatsby's splat API routes on Vercel, you must:
  1. Define your splat routes in a `vercel.json` file at the root directory of your project, as shown below:
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/api/products/:path*",
      "destination": "/api/products/[...]"
    }
  ]
}
```

  2. Read your dynamic parameters from `req.query.path`, as shown below:
api/products/[...].ts
TypeScript
TypeScript JavaScript Bash
```
import type { VercelRequest, VercelResponse } from '@vercel/node';

export default function handler(
  request: VercelRequest & { params: { path: string } },
  response: VercelResponse,
) {
  console.log(`/api/products/${request.query.path}`);
  response.status(200).json({
    body: request.body,
    query: request.query,
    cookies: request.cookies,
  });
}
```



To summarize, API Routes with Gatsby on Vercel:
  * Scale to zero when not in use
  * Scale automatically with traffic increases
  * Can be tested as Vercel Functions in your local environment
