## Possible Ways to Fix It[](https://nextjs.org/docs/messages/sync-dynamic-apis#possible-ways-to-fix-it)
The [`next-async-request-api` codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#next-async-request-api) can fix many of these cases automatically:
Terminal
```
npx @next/codemod@canary next-async-request-api .
```

The codemod cannot cover all cases, so you may need to manually adjust some code.
If the warning occurred on the Server (e.g. a route handler, or a Server Component), you must `await` the dynamic API to access its properties:
app/[id]/page.js
```
async function Page({ params }) {
  // asynchronous access of `params.id`.
  const { id } = await params
  return <p>ID: {id}</p>
}
```

If the warning occurred in a synchronous component (e.g. a Client component), you must use `React.use()` to unwrap the Promise first:
app/[id]/page.js
```
'use client'
import * as React from 'react'

function Page({ params }) {
  // asynchronous access of `params.id`.
  const { id } = React.use(params)
  return <p>ID: {id}</p>
}
```

### Unmigratable Cases[](https://nextjs.org/docs/messages/sync-dynamic-apis#unmigratable-cases)
If Next.js codemod found anything that is not able to be migrated by the codemod, it will leave a comment with `@next-codemod-error` prefix and the suggested action, for example: In this case, you need to manually await the call to `cookies()`, and change the function to async. Then refactor the usages of the function to be properly awaited:
```
export function MyCookiesComponent() {
  const c =
    /* @next-codemod-error Manually await this call and refactor the function to be async */
    cookies()
  return c.get('name')
}
```

### Enforced Migration with Linter[](https://nextjs.org/docs/messages/sync-dynamic-apis#enforced-migration-with-linter)
If you didn't address the comments that starting with `@next-codemod-error` left by the codemod, Next.js will error in both dev and build to enforce you to address the issues. You can review the changes and follow the suggestion in the comments. You can either make the necessary changes and remove the comment, or replace the comment prefix `@next-codemod-error` with `@next-codemod-ignore` If there's no action to be taken, the comment prefix `@next-codemod-ignore` will bypass the build error.
```
- /* @next-codemod-error <suggested message> */
+ /* @next-codemod-ignore */
```

> **Good to know** :
> You can delay unwrapping the Promise (either with `await` or `React.use`) until you actually need to consume the value. This will allow Next.js to statically render more of your page.
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
