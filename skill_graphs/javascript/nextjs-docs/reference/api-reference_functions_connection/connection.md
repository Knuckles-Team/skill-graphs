# connection
Last updated February 27, 2026
The `connection()` function allows you to indicate rendering should wait for an incoming user request before continuing.
It's useful when a component doesn't use [Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering), but you want it to be dynamically rendered at runtime and not statically rendered at build time. This usually occurs when you access external information that you intentionally want to change the result of a render, such as `Math.random()` or `new Date()`.
app/page.tsx
TypeScript
JavaScript TypeScript
```
import { connection } from 'next/server'

export default async function Page() {
  await connection()
  // Everything below will be excluded from prerendering
  const rand = Math.random()
  return <span>{rand}</span>
}
```
