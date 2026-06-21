## Redirects[](https://nextjs.org/docs/app/guides/backend-for-frontend#redirects)
app/api/route.ts
TypeScript
JavaScript TypeScript
```
import { redirect } from 'next/navigation'

export async function GET(request: Request) {
  redirect('https://nextjs.org/')
}
```

Learn more about redirects in [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect) and [`permanentRedirect`](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)
