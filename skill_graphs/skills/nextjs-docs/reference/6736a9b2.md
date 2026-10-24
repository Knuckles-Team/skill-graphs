## Examples[](https://nextjs.org/docs/app/api-reference/functions/headers#examples)
### Using the Authorization header[](https://nextjs.org/docs/app/api-reference/functions/headers#using-the-authorization-header)
app/page.js
```
import { headers } from 'next/headers'

export default async function Page() {
  const authorization = (await headers()).get('authorization')
  const res = await fetch('...', {
    headers: { authorization }, // Forward the authorization header
  })
  const user = await res.json()

  return <h1>{user.name}</h1>
}
```
