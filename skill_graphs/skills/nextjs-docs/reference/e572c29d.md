## Possible Ways to Fix It[](https://nextjs.org/docs/messages/next-request-in-use-cache#possible-ways-to-fix-it)
Instead of calling this inside the `"use cache"` function, move it outside the function and pass the value in as an argument. The specific value will now be part of the cache key through its arguments.
Before:
app/page.js
```
import { cookies } from 'next/headers'

async function getExampleData() {
  "use cache"
  const isLoggedIn = (await cookies()).has('token')
  ...
}

export default async function Page() {
  const data = await getExampleData()
  return ...
}
```

After:
app/page.js
```
import { cookies } from 'next/headers'

async function getExampleData(isLoggedIn) {
  "use cache"
  ...
}

export default async function Page() {
  const isLoggedIn = (await cookies()).has('token')
  const data = await getExampleData(isLoggedIn)
  return ...
}
```
