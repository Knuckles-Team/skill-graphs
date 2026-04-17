## Response Helpers[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#response-helpers)
The `res`) includes a set of Express.js-like helper methods to improve the developer experience and increase the speed of creating new API endpoints.
The included helpers are:
  * `res.status(code)` - A function to set the status code. `code` must be a valid
  * `res.json(body)` - Sends a JSON response. `body` must be a
  * `res.send(body)` - Sends the HTTP response. `body` can be a `string`, an `object` or a `Buffer`
  * `res.redirect([status,] path)` - Redirects to a specified path or URL. `status` must be a valid `status` defaults to "307" "Temporary redirect".
  * `res.revalidate(urlPath)` - [Revalidate a page on demand](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath) using `getStaticProps`. `urlPath` must be a `string`.


### Setting the status code of a response[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#setting-the-status-code-of-a-response)
When sending a response back to the client, you can set the status code of the response.
The following example sets the status code of the response to `200` (`OK`) and returns a `message` property with the value of `Hello from Next.js!` as a JSON response:
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
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

### Sending a JSON response[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#sending-a-json-response)
When sending a response back to the client you can send a JSON response, this must be a
The following example sends a JSON response with the status code `200` (`OK`) and the result of the async operation. It's contained in a try catch block to handle any errors that may occur, with the appropriate status code and error message caught and sent back to the client:
pages/api/hello.ts
TypeScript
JavaScript TypeScript
```
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const result = await someAsyncOperation()
    res.status(200).json({ result })
  } catch (err) {
    res.status(500).json({ error: 'failed to load data' })
  }
}
```

### Sending a HTTP response[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#sending-a-http-response)
Sending an HTTP response works the same way as when sending a JSON response. The only difference is that the response body can be a `string`, an `object` or a `Buffer`.
The following example sends a HTTP response with the status code `200` (`OK`) and the result of the async operation.
pages/api/hello.ts
TypeScript
JavaScript TypeScript
```
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const result = await someAsyncOperation()
    res.status(200).send({ result })
  } catch (err) {
    res.status(500).send({ error: 'failed to fetch data' })
  }
}
```

### Redirects to a specified path or URL[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#redirects-to-a-specified-path-or-url)
Taking a form as an example, you may want to redirect your client to a specified path or URL once they have submitted the form.
The following example redirects the client to the `/` path if the form is successfully submitted:
pages/api/hello.ts
TypeScript
JavaScript TypeScript
```
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const { name, message } = req.body

  try {
    await handleFormInputAsync({ name, message })
    res.redirect(307, '/')
  } catch (err) {
    res.status(500).send({ error: 'Failed to fetch data' })
  }
}
```

### Adding TypeScript types[](https://nextjs.org/docs/pages/building-your-application/routing/api-routes#adding-typescript-types)
You can make your API Routes more type-safe by importing the `NextApiRequest` and `NextApiResponse` types from `next`, in addition to those, you can also type your response data:
```
import type { NextApiRequest, NextApiResponse } from 'next'

type ResponseData = {
  message: string
}

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<ResponseData>
) {
  res.status(200).json({ message: 'Hello from Next.js!' })
}
```

> **Good to know** : The body of `NextApiRequest` is `any` because the client may include any payload. You should validate the type/shape of the body at runtime before using it.
