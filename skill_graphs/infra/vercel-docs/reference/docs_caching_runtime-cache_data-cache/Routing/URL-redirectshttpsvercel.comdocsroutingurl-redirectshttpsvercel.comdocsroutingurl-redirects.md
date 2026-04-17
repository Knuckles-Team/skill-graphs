##  [URL redirects](https://vercel.com/docs/routing#url-redirects)[](https://vercel.com/docs/routing#url-redirects)
Redirects send the visitor's browser to a different URL with an HTTP status code (301, 302, 307, or 308). The visitor sees the new URL in their address bar.
Use redirects when you need to:
  * Preserve SEO after renaming or moving pages
  * Enforce HTTPS or add a trailing slash
  * Redirect users based on locale or region
  * Handle domain migrations


You can define redirects in `vercel.json` or through your framework's configuration. For large-scale URL changes, [bulk redirects](https://vercel.com/docs/routing/redirects/bulk-redirects) let you upload thousands of rules from a CSV file.
