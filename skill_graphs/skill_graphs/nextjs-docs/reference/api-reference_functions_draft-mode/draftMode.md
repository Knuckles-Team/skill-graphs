# draftMode
Last updated February 27, 2026
`draftMode` is an **async** function allows you to enable and disable [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode), as well as check if Draft Mode is enabled in a [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components).
app/page.ts
TypeScript
JavaScript TypeScript
```
import { draftMode } from 'next/headers'

export default async function Page() {
  const { isEnabled } = await draftMode()
}
```
