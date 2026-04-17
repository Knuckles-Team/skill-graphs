## Library patterns[](https://nextjs.org/docs/app/guides/backend-for-frontend#library-patterns)
Community libraries often use the factory pattern for Route Handlers.
/app/api/[...path]/route.ts
```
import { createHandler } from 'third-party-library'

const handler = createHandler({
  /* library-specific options */
})

export const GET = handler
// or
export { handler as POST }
```

This creates a shared handler for `GET` and `POST` requests. The library customizes behavior based on the `method` and `pathname` in the request.
Libraries can also provide a `proxy` factory.
proxy.ts
```
import { createMiddleware } from 'third-party-library'

export default createMiddleware()
```

> **Good to know** : Third-party libraries may still refer to `proxy` as `middleware`.
