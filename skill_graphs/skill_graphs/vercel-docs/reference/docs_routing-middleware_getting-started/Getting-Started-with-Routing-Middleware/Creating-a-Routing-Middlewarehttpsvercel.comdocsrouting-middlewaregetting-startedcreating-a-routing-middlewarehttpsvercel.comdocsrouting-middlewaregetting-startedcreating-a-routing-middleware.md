##  [Creating a Routing Middleware](https://vercel.com/docs/routing-middleware/getting-started#creating-a-routing-middleware)[](https://vercel.com/docs/routing-middleware/getting-started#creating-a-routing-middleware)
The following steps will guide you through creating your first Routing Middleware.
  1. ###  [Create a new file for your Routing Middleware](https://vercel.com/docs/routing-middleware/getting-started#create-a-new-file-for-your-routing-middleware)[](https://vercel.com/docs/routing-middleware/getting-started#create-a-new-file-for-your-routing-middleware)
Create a file called `middleware.ts` in your project root (same level as your `package.json`) and add the following code:
middleware.ts
```
export const config = {
  runtime: 'nodejs', // optional: use 'nodejs' or omit for 'edge' (default)
};

export default function middleware(request: Request) {
  console.log('Request to:', request.url);
  return new Response('Logging request URL from Middleware');
}
```

     * Every request to your site will trigger this function
     * You log the request URL to see what's being accessed
     * You return a response to prove the middleware is running
     * The `runtime` config is optional and defaults to `edge`. To use Bun, set [`bunVersion`](https://vercel.com/docs/project-configuration#bunversion) in `vercel.json` instead
Deploy your project and visit any page. You should see "Logging request URL from Middleware" instead of your normal page content.
  2. ###  [Redirecting users](https://vercel.com/docs/routing-middleware/getting-started#redirecting-users)[](https://vercel.com/docs/routing-middleware/getting-started#redirecting-users)
To redirect users based on their URL, add a new route to your project called `/blog`, and modify your `middleware.ts` to include a redirect condition.
middleware.ts
```
export const config = {
  runtime: 'nodejs', // optional: use 'nodejs' or omit for 'edge' (default)
};

export default function middleware(request: Request) {
  const url = new URL(request.url);

  // Redirect old blog path to new one
  if (url.pathname === '/old-blog') {
    return new Response(null, {
      status: 302,
      headers: { Location: '/blog' },
    });
  }

  // Let other requests continue normally
  return new Response('Other pages work normally');
}
```

     * You use `new URL(request.url)` to parse the incoming URL
     * You check if the path matches `/old-blog`
     * If it does, you return a redirect response (status 302)
     * The `Location` header tells the browser where to go
Try visiting `/old-blog` - you should be redirected to `/blog`.
  3. ###  [Configure which paths trigger the middleware](https://vercel.com/docs/routing-middleware/getting-started#configure-which-paths-trigger-the-middleware)[](https://vercel.com/docs/routing-middleware/getting-started#configure-which-paths-trigger-the-middleware)
By default, Routing Middleware runs on every request. To limit it to specific paths, you can use the [`config`](https://vercel.com/docs/routing-middleware/api#config-object) object:
middleware.ts
```
export default function middleware(request: Request) {
  const url = new URL(request.url);

  // Only handle specific redirects
  if (url.pathname === '/old-blog') {
    return new Response(null, {
      status: 302,
      headers: { Location: '/blog' },
    });
  }

  return new Response('Middleware processed this request');
}

// Configure which paths trigger the Middleware
export const config = {
  matcher: [
    // Run on all paths except static files
    '/((?!_next/static|_next/image|favicon.ico).*)',
    // Or be more specific:
    // '/blog/:path*',
    // '/api/:path*'
  ],
};
```

     * The [`matcher`](https://vercel.com/docs/routing-middleware/api#match-paths-based-on-custom-matcher-config) array defines which paths trigger your Routing Middleware
     * The regex excludes static files (images, CSS, etc.) for better performance
     * You can also use simple patterns like `/blog/:path*` for specific sections
See the [API Reference](https://vercel.com/docs/routing-middleware/api) for more details on the `config` object and matcher patterns.
  4. ###  [Debugging Routing Middleware](https://vercel.com/docs/routing-middleware/getting-started#debugging-routing-middleware)[](https://vercel.com/docs/routing-middleware/getting-started#debugging-routing-middleware)
When things don't work as expected:
    1. Check the logs: Use `console.log()` liberally and check your [Vercel dashboard](https://vercel.com/dashboard) Logs section in the sidebar
    2. Test the matcher: Make sure your paths are actually triggering the Routing Middleware
    3. Verify headers: Log `request.headers` to see what's available
    4. Test locally: Routing Middleware works in development too so you can debug before deploying
middleware.ts
```
export default function middleware(request: Request) {
  // Debug logging
  console.log('URL:', request.url);
  console.log('Method:', request.method);
  console.log('Headers:', Object.fromEntries(request.headers.entries()));

  // Your middleware logic here...
}
```
