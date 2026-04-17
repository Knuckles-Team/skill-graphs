##  [Rewrites within your application](https://vercel.com/docs/routing#rewrites-within-your-application)[](https://vercel.com/docs/routing#rewrites-within-your-application)
Same-application rewrites map a public URL to a different page or route inside your Vercel project. The visitor's browser still shows the original URL.
Use internal rewrites when you need to:
  * Serve different content at the same URL (A/B testing, feature flags)
  * Create clean public URLs that map to dynamic routes
  * Maintain backward-compatible URLs after restructuring your app


```
{
  "rewrites": [
    { "source": "/blog/:slug", "destination": "/posts/:slug" }
  ]
}
```
