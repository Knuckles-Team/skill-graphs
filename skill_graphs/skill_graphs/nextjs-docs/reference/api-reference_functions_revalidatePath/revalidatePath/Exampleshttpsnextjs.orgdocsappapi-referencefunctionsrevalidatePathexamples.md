## Examples[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#examples)
### Revalidating a specific URL[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-specific-url)
```
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/post-1')
```

This will invalidate one specific URL for revalidation on the next page visit.
### Revalidating a Page path[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-page-path)
```
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/[slug]', 'page')
// or with route groups
revalidatePath('/(main)/blog/[slug]', 'page')
```

This will invalidate any URL that matches the provided `page` file for revalidation on the next page visit. This will _not_ invalidate pages beneath the specific page. For example, `/blog/[slug]` won't invalidate `/blog/[slug]/[author]`.
### Revalidating a Layout path[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-a-layout-path)
```
import { revalidatePath } from 'next/cache'
revalidatePath('/blog/[slug]', 'layout')
// or with route groups
revalidatePath('/(main)/post/[slug]', 'layout')
```

This will invalidate any URL that matches the provided `layout` file for revalidation on the next page visit. This will cause pages beneath with the same layout to be invalidated and revalidated on the next visit. For example, in the above case, `/blog/[slug]/[another]` would also be invalidated and revalidated on the next visit.
### Revalidating all data[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#revalidating-all-data)
```
import { revalidatePath } from 'next/cache'

revalidatePath('/', 'layout')
```

This will purge the Client-side Router Cache, and invalidate the Data Cache for revalidation on the next page visit.
### Server Function[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#server-function)
app/actions.ts
TypeScript
JavaScript TypeScript
```
'use server'

import { revalidatePath } from 'next/cache'

export default async function submit() {
  await submitForm()
  revalidatePath('/')
}
```

### Route Handler[](https://nextjs.org/docs/app/api-reference/functions/revalidatePath#route-handler)
app/api/revalidate/route.ts
TypeScript
JavaScript TypeScript
```
import { revalidatePath } from 'next/cache'
import type { NextRequest } from 'next/server'

export async function GET(request: NextRequest) {
  const path = request.nextUrl.searchParams.get('path')

  if (path) {
    revalidatePath(path)
    return Response.json({ revalidated: true, now: Date.now() })
  }

  return Response.json({
    revalidated: false,
    now: Date.now(),
    message: 'Missing path to revalidate',
  })
}
```

[Previousrefresh](https://nextjs.org/docs/app/api-reference/functions/refresh)[NextrevalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)
Was this helpful?
Send
* * *
* * *
#### Resources
[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Next.js Conf](https://nextjs.org/conf)[Evals](https://nextjs.org/evals)
#### More
[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)
#### About Vercel
#### Legal
Cookie Preferences
#### Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe
© 2026 Vercel, Inc.
* * *
* * *
