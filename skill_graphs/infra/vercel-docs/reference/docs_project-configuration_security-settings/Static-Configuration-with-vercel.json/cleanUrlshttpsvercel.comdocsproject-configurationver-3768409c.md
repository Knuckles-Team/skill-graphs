##  [cleanUrls](https://vercel.com/docs/project-configuration/vercel-json#cleanurls)[](https://vercel.com/docs/project-configuration/vercel-json#cleanurls)
Type: `Boolean`.
Default Value: `false`.
When set to `true`, all HTML files and Vercel functions will have their extension removed. When visiting a path that ends with the extension, a 308 response will redirect the client to the extensionless path.
For example, a static file named `about.html` will be served when visiting the `/about` path. Visiting `/about.html` will redirect to `/about`.
Similarly, a Vercel Function named `api/user.go` will be served when visiting `/api/user`. Visiting `/api/user.go` will redirect to `/api/user`.
vercel.json
```
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "cleanUrls": true
}
```

If you are using Next.js and running `vercel dev`, you will get a 404 error when visiting a route configured with `cleanUrls` locally. It does however work fine when deployed to Vercel. In the example above, visiting `/about` locally will give you a 404 with `vercel dev` but `/about` will render correctly on Vercel.
