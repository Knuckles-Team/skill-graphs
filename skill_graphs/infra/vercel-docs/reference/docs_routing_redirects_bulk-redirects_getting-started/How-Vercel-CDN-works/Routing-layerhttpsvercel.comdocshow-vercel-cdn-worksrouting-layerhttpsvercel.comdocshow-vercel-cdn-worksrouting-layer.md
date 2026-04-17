##  [Routing layer](https://vercel.com/docs/how-vercel-cdn-works#routing-layer)[](https://vercel.com/docs/how-vercel-cdn-works#routing-layer)
Before the CDN checks any cache, it evaluates routing rules in order:
  1. [Redirects](https://vercel.com/docs/routing/redirects): Return a new URL to the client (e.g., enforce HTTPS, move pages, localize paths)
  2. [Rewrites](https://vercel.com/docs/routing/rewrites): Map a public URL to a different backend path without changing what the visitor sees
  3. [Headers](https://vercel.com/docs/headers): Add or modify request and response headers, including [security headers](https://vercel.com/docs/cdn-security/security-headers) and [cache-control directives](https://vercel.com/docs/caching/cache-control-headers)


If a redirect matches, the CDN responds immediately. Rewrites and header rules continue through the remaining layers.
