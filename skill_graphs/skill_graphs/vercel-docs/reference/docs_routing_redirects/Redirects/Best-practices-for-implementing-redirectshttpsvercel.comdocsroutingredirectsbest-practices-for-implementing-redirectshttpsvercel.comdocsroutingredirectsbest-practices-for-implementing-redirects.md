##  [Best practices for implementing redirects](https://vercel.com/docs/routing/redirects#best-practices-for-implementing-redirects)[](https://vercel.com/docs/routing/redirects#best-practices-for-implementing-redirects)
There are some best practices to keep in mind when implementing redirects in your application:
  1. Test thoroughly: Test your redirects thoroughly to ensure they work as expected. Use a [preview deployment](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) to test redirects before deploying them to production
  2. Use relative paths: Use relative paths in your `destination` field to avoid hardcoding your domain name
  3. Use permanent redirects: Use [permanent redirects](https://vercel.com/docs/routing/redirects#adding-redirects) for permanent URL changes and [temporary redirects](https://vercel.com/docs/routing/redirects#adding-redirects) for temporary changes
  4. Use wildcards carefully: Wildcards can be powerful but should be used with caution. For example, if you use a wildcard in a source rule that matches any URL path, you could inadvertently redirect all incoming requests to a single destination, effectively breaking your site.
  5. Prioritize HTTPS: Use redirects to enforce HTTPS for all requests to your domain


* * *
[ Previous Routing ](https://vercel.com/docs/routing)[ Next Configuration Redirects ](https://vercel.com/docs/routing/redirects/configuration-redirects)
Was this helpful?
Send
Next.js (/app)
Choose a framework to optimize documentation to:
  * Next.js (/app)
  * Next.js (/pages)
  * SvelteKit
  * Nuxt
  * Other frameworks


On this page
  * [Use cases](https://vercel.com/docs/routing/redirects#use-cases)
  * [Implementing redirects](https://vercel.com/docs/routing/redirects#implementing-redirects)
  * [Vercel Functions](https://vercel.com/docs/routing/redirects#vercel-functions)
  * [Middleware](https://vercel.com/docs/routing/redirects#middleware)
  * [Domain Redirects](https://vercel.com/docs/routing/redirects#domain-redirects)
  * [Firewall Redirects](https://vercel.com/docs/routing/redirects#firewall-redirects)
  * [Redirect status codes](https://vercel.com/docs/routing/redirects#redirect-status-codes)
  * [Observing redirects](https://vercel.com/docs/routing/redirects#observing-redirects)
  * [Draining redirects](https://vercel.com/docs/routing/redirects#draining-redirects)
  * [Automatic URL normalization](https://vercel.com/docs/routing/redirects#automatic-url-normalization)
  * [Consecutive slashes](https://vercel.com/docs/routing/redirects#consecutive-slashes)
  * [Case sensitivity](https://vercel.com/docs/routing/redirects#case-sensitivity)
  * [Best practices for implementing redirects](https://vercel.com/docs/routing/redirects#best-practices-for-implementing-redirects)


Copy as MarkdownGive feedbackAsk AI about this page
