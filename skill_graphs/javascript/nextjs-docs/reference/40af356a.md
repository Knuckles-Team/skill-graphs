## Environment Variables[](https://nextjs.org/docs/app/guides/self-hosting#environment-variables)
Next.js can support both build time and runtime environment variables.
**By default, environment variables are only available on the server**. To expose an environment variable to the browser, it must be prefixed with `NEXT_PUBLIC_`. However, these public environment variables will be inlined into the JavaScript bundle during `next build`.
You safely read environment variables on the server during dynamic rendering.
app/page.ts
TypeScript
JavaScript TypeScript
```
import { connection } from 'next/server'

export default async function Component() {
  await connection()
  // cookies, headers, and other Dynamic APIs
  // will also opt into dynamic rendering, meaning
  // this env variable is evaluated at runtime
  const value = process.env.MY_VALUE
  // ...
}
```

This allows you to use a singular Docker image that can be promoted through multiple environments with different values.
> **Good to know:**
>   * You can run code on server startup using the [`register` function](https://nextjs.org/docs/app/guides/instrumentation).
>
