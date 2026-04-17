# unauthorized
This feature is currently experimental and subject to change, it's not recommended for production. Try it out and share your feedback on
Last updated February 27, 2026
The `unauthorized` function throws an error that renders a Next.js 401 error page. It's useful for handling authorization errors in your application. You can customize the UI using the [`unauthorized.js` file](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized).
To start using `unauthorized`, enable the experimental [`authInterrupts`](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts) configuration option in your `next.config.js` file:
next.config.ts
TypeScript
JavaScript TypeScript
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  experimental: {
    authInterrupts: true,
  },
}

export default nextConfig
```

`unauthorized` can be invoked in [Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), [Server Functions](https://nextjs.org/docs/app/getting-started/updating-data), and [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route).
app/dashboard/page.tsx
TypeScript
JavaScript TypeScript
```
import { verifySession } from '@/app/lib/dal'
import { unauthorized } from 'next/navigation'

export default async function DashboardPage() {
  const session = await verifySession()

  if (!session) {
    unauthorized()
  }

  // Render the dashboard for authenticated users
  return (
    <main>
      <h1>Welcome to the Dashboard</h1>
      <p>Hi, {session.user.name}.</p>
    </main>
  )
}
```
