## Step 1: Create a Route Handler[](https://nextjs.org/docs/app/guides/draft-mode#step-1-create-a-route-handler)
Create a [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route). It can have any name, for example, `app/api/draft/route.ts`.
app/api/draft/route.ts
TypeScript
JavaScript TypeScript
```
export async function GET(request: Request) {
  return new Response('')
}
```

Then, import the [`draftMode`](https://nextjs.org/docs/app/api-reference/functions/draft-mode) function and call the `enable()` method.
app/api/draft/route.ts
TypeScript
JavaScript TypeScript
```
import { draftMode } from 'next/headers'

export async function GET(request: Request) {
  const draft = await draftMode()
  draft.enable()
  return new Response('Draft mode is enabled')
}
```

This will set a **cookie** to enable draft mode. Subsequent requests containing this cookie will trigger draft mode and change the behavior of statically generated pages.
You can test this manually by visiting `/api/draft` and looking at your browser’s developer tools. Notice the `Set-Cookie` response header with a cookie named `__prerender_bypass`.
