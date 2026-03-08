## HTTP Methods[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#http-methods)
To handle different HTTP methods in an API route, you can use `req.method` in your request handler, like so:
pages/api/hello.ts
TypeScript
JavaScript TypeScript
```
import type { NextApiRequest, NextApiResponse } from 'next'

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    // Process a POST request
  } else {
    // Handle any other HTTP method
  }
}
```
