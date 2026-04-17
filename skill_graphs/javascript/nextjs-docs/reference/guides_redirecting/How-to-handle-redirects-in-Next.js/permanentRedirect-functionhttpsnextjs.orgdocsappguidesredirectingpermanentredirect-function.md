##  `permanentRedirect` function[](https://nextjs.org/docs/app/guides/redirecting#permanentredirect-function)
The `permanentRedirect` function allows you to **permanently** redirect the user to another URL. You can call `permanentRedirect` in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route), and [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data).
`permanentRedirect` is often used after a mutation or event that changes an entity's canonical URL, such as updating a user's profile URL after they change their username:
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { permanentRedirect } from 'next/navigation'
import { revalidateTag } from 'next/cache'

export async function updateUsername(username: string, formData: FormData) {
  try {
    // Call database
  } catch (error) {
    // Handle errors
  }

  revalidateTag('username') // Update all references to the username
  permanentRedirect(`/profile/${username}`) // Navigate to the new user profile
}
```

> **Good to know** :
>   * `permanentRedirect` returns a 308 (permanent redirect) status code by default.
>   * `permanentRedirect` also accepts absolute URLs and can be used to redirect to external links.
>   * If you'd like to redirect before the render process, use [`next.config.js`](https://nextjs.org/docs/app/guides/redirecting#redirects-in-nextconfigjs) or [Proxy](https://nextjs.org/docs/app/guides/redirecting#nextresponseredirect-in-proxy).
>

See the [`permanentRedirect` API reference](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect) for more information.
