##  [Routing Middleware](https://vercel.com/docs/getting-started-with-vercel#routing-middleware)[](https://vercel.com/docs/getting-started-with-vercel#routing-middleware)
Gatsby does not have native framework support for using [Routing Middleware](https://vercel.com/docs/routing-middleware).
However, you can still use Routing Middleware with your Gatsby site by creating a `middeware.js` or `middeware.ts` file in your project's root directory.
The following example demonstrates middleware that adds security headers to responses sent to users who visit the `/example` route in your Gatsby application:
middleware.ts
TypeScript
TypeScript JavaScript Bash
```
import { next } from '@vercel/functions';

export const config = {
  // Only run the middleware on the example route
  matcher: '/example',
};

export default function middleware(request: Request): Response {
  return next({
    headers: {
      'Referrer-Policy': 'origin-when-cross-origin',
      'X-Frame-Options': 'DENY',
      'X-Content-Type-Options': 'nosniff',
      'X-DNS-Prefetch-Control': 'on',
      'Strict-Transport-Security':
        'max-age=31536000; includeSubDomains; preload',
    },
  });
}
```

To summarize, Routing Middleware with Gatsby on Vercel:
  * Executes before a request is processed on a site, allowing you to modify responses to user requests
  * Runs on _all_ requests, but can be scoped to specific paths [through a `matcher` config](https://vercel.com/docs/routing-middleware/api#match-paths-based-on-custom-matcher-config)
  * Uses our lightweight Edge Runtime to keep costs low and responses fast


[Learn more about Routing Middleware](https://vercel.com/docs/routing-middleware)
