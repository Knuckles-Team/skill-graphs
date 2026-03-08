## Server Forms[](https://nextjs.org/docs/pages/guides/forms#server-forms)
To handle form submissions on the server, create an API endpoint that securely mutates data.
pages/api/submit.ts
TypeScript
JavaScript TypeScript
```
import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const data = req.body
  const id = await createItem(data)
  res.status(200).json({ id })
}
```

Then, call the API Route from the client with an event handler:
pages/index.tsx
TypeScript
JavaScript TypeScript
```
import { FormEvent } from 'react'

export default function Page() {
  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    const formData = new FormData(event.currentTarget)
    const response = await fetch('/api/submit', {
      method: 'POST',
      body: formData,
    })

    // Handle response if necessary
    const data = await response.json()
    // ...
  }

  return (
    <form onSubmit={onSubmit}>
      <input type="text" name="name" />
      <button type="submit">Submit</button>
    </form>
  )
}
```

> **Good to know:**
>   * API Routes
>   * Since API Routes run on the server, we're able to use sensitive values (like API keys) through [Environment Variables](https://nextjs.org/docs/pages/guides/environment-variables) without exposing them to the client. This is critical for the security of your application.
>
