##  `redirect` function[](https://nextjs.org/docs/app/guides/redirecting#redirect-function)
The `redirect` function allows you to redirect the user to another URL. You can call `redirect` in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route), and [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data).
`redirect` is often used after a mutation or event. For example, creating a post:
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { redirect } from 'next/navigation'
import { revalidatePath } from 'next/cache'

export async function createPost(id: string) {
  try {
    // Call database
  } catch (error) {
    // Handle errors
  }

  revalidatePath('/posts') // Update cached posts
  redirect(`/post/${id}`) // Navigate to the new post page
}
```

> **Good to know** :
>   * `redirect` returns a 307 (Temporary Redirect) status code by default. When used in a Server Action, it returns a 303 (See Other), which is commonly used for redirecting to a success page as a result of a POST request.
>   * `redirect` throws an error so it should be called **outside** the `try` block when using `try/catch` statements.
>   * `redirect` can be called in Client Components during the rendering process but not in event handlers. You can use the [`useRouter` hook](https://nextjs.org/docs/app/guides/redirecting#userouter-hook) instead.
>   * `redirect` also accepts absolute URLs and can be used to redirect to external links.
>   * If you'd like to redirect before the render process, use [`next.config.js`](https://nextjs.org/docs/app/guides/redirecting#redirects-in-nextconfigjs) or [Proxy](https://nextjs.org/docs/app/guides/redirecting#nextresponseredirect-in-proxy).
>

See the [`redirect` API reference](https://nextjs.org/docs/app/api-reference/functions/redirect) for more information.
