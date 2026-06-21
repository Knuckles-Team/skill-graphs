## Context Providers[](https://nextjs.org/docs/app/guides/authentication#context-providers)
Using context providers for auth works due to [interleaving](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples#interleaving-server-and-client-components). However, React `context` is not supported in Server Components, making them only applicable to Client Components.
This works, but any child Server Components will be rendered on the server first, and will not have access to the context provider’s session data:
app/layout.ts
TypeScript
JavaScript TypeScript
```
import { ContextProvider } from 'auth-lib'

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <ContextProvider>{children}</ContextProvider>
      </body>
    </html>
  )
}
```

```
'use client';

import { useSession } from "auth-lib";

export default function Profile() {
  const { userId } = useSession();
  const { data } = useSWR(`/api/user/${userId}`, fetcher)

  return (
    // ...
  );
}
```

If session data is needed in Client Components (e.g. for client-side data fetching), use React’s
