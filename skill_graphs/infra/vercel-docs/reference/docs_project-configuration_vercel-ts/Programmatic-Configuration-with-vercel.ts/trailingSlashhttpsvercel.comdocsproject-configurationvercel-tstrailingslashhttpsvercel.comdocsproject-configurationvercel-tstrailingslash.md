##  [trailingSlash](https://vercel.com/docs/project-configuration/vercel-ts#trailingslash)[](https://vercel.com/docs/project-configuration/vercel-ts#trailingslash)
Type: `Boolean`.
Default Value: `undefined`.
###  [false](https://vercel.com/docs/project-configuration/vercel-ts#false)[](https://vercel.com/docs/project-configuration/vercel-ts#false)
When `trailingSlash: false`, visiting a path that ends with a forward slash will respond with a 308 status code and redirect to the path without the trailing slash.
For example, the `/about/` path will redirect to `/about`.
vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  trailingSlash: false,
};
```

###  [true](https://vercel.com/docs/project-configuration/vercel-ts#true)[](https://vercel.com/docs/project-configuration/vercel-ts#true)
When `trailingSlash: true`, visiting a path that does not end with a forward slash will respond with a 308 status code and redirect to the path with a trailing slash.
For example, the `/about` path will redirect to `/about/`.
However, paths with a file extension will not redirect to a trailing slash.
For example, the `/about/styles.css` path will not redirect, but the `/about/styles` path will redirect to `/about/styles/`.
vercel.ts
```
import type { VercelConfig } from '@vercel/config/v1';

export const config: VercelConfig = {
  trailingSlash: true,
};
```

###  [undefined](https://vercel.com/docs/project-configuration/vercel-ts#undefined)[](https://vercel.com/docs/project-configuration/vercel-ts#undefined)
When `trailingSlash: undefined`, visiting a path with or without a trailing slash will not redirect.
For example, both `/about` and `/about/` will serve the same content without redirecting.
This is not recommended because it could lead to search engines indexing two different pages with duplicate content.
