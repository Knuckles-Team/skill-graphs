##  [schema autocomplete](https://vercel.com/docs/project-configuration/vercel-ts#schema-autocomplete)[](https://vercel.com/docs/project-configuration/vercel-ts#schema-autocomplete)
Via the types imported from the `@vercel/config` package, autocomplete for all config properties and helpers are automatically available in `vercel.ts`.
vercel.ts
```
import { routes, type VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  rewrites: [routes.rewrite('/about', '/about-our-company.html')],
  // add more properties here
};
```
