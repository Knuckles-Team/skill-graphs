##  [trailingSlash](https://vercel.com/docs/project-configuration/vercel-json#trailingslash)[](https://vercel.com/docs/project-configuration/vercel-json#trailingslash)
Type: `Boolean`.
Default Value: `undefined`.
###  [false](https://vercel.com/docs/project-configuration/vercel-json#false)[](https://vercel.com/docs/project-configuration/vercel-json#false)
When `trailingSlash: false`, visiting a path that ends with a forward slash will respond with a 308 status code and redirect to the path without the trailing slash.
For example, the `/about/` path will redirect to `/about`.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "trailingSlash": false
}
```

###  [true](https://vercel.com/docs/project-configuration/vercel-json#true)[](https://vercel.com/docs/project-configuration/vercel-json#true)
When `trailingSlash: true`, visiting a path that does not end with a forward slash will respond with a 308 status code and redirect to the path with a trailing slash.
For example, the `/about` path will redirect to `/about/`.
However, paths with a file extension will not redirect to a trailing slash.
For example, the `/about/styles.css` path will not redirect, but the `/about/styles` path will redirect to `/about/styles/`.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "trailingSlash": true
}
```

###  [undefined](https://vercel.com/docs/project-configuration/vercel-json#undefined)[](https://vercel.com/docs/project-configuration/vercel-json#undefined)
When `trailingSlash: undefined`, visiting a path with or without a trailing slash will not redirect.
For example, both `/about` and `/about/` will serve the same content without redirecting.
This is not recommended because it could lead to search engines indexing two different pages with duplicate content.
