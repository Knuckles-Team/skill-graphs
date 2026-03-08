## Examples[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#examples)
### Enabling Draft Mode[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#enabling-draft-mode)
To enable Draft Mode, create a new [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route) and call the `enable()` method:
app/draft/route.ts
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

### Disabling Draft Mode[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#disabling-draft-mode)
By default, the Draft Mode session ends when the browser is closed.
To disable Draft Mode manually, call the `disable()` method in your [Route Handler](https://nextjs.org/docs/app/api-reference/file-conventions/route):
app/draft/route.ts
TypeScript
JavaScript TypeScript
```
import { draftMode } from 'next/headers'

export async function GET(request: Request) {
  const draft = await draftMode()
  draft.disable()
  return new Response('Draft mode is disabled')
}
```

Then, send a request to invoke the Route Handler. If calling the route using the [`<Link>` component](https://nextjs.org/docs/app/api-reference/components/link), you must pass `prefetch={false}` to prevent accidentally deleting the cookie on prefetch.
### Checking if Draft Mode is enabled[](https://nextjs.org/docs/app/api-reference/functions/draft-mode#checking-if-draft-mode-is-enabled)
You can check if Draft Mode is enabled in a Server Component with the `isEnabled` property:
app/page.ts
TypeScript
JavaScript TypeScript
```
import { draftMode } from 'next/headers'

export default async function Page() {
  const { isEnabled } = await draftMode()
  return (
    <main>
      <h1>My Blog Post</h1>
      <p>Draft Mode is currently {isEnabled ? 'Enabled' : 'Disabled'}</p>
    </main>
  )
}
```
