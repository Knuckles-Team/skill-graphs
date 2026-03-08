##  [`Cache-Control` headers](https://vercel.com/docs/getting-started-with-vercel#cache-control-headers)[](https://vercel.com/docs/getting-started-with-vercel#cache-control-headers)
Vercel's [CDN](https://vercel.com/docs/cdn) caches your content at the edge in order to serve data to your users as fast as possible. [Static caching](https://vercel.com/docs/cdn-cache#static-files-caching) works with zero configuration.
By adding a `Cache-Control` header to responses returned by your React Router routes, you can specify a set of caching rules for both client (browser) requests and server responses. A cache must obey the requirements defined in the Cache-Control header.
React Router supports defining response headers by exporting a
The following example demonstrates a route that adds `Cache-Control` headers which instruct the route to:
  * Return cached content for requests repeated within 1 second without revalidating the content
  * For requests repeated after 1 second, but before 60 seconds have passed, return the cached content and mark it as stale. The stale content will be revalidated in the background with a fresh value from your


/app/routes/example.tsx
TypeScript
TypeScript JavaScript Bash
```
import { Route } from './+types/some-route';

export function headers(_: Route.HeadersArgs) {
  return {
    'Cache-Control': 's-maxage=1, stale-while-revalidate=59',
  };
}

export async function loader() {
  // Fetch data necessary to render content
}
```

See [our docs on cache limits](https://vercel.com/docs/cdn-cache#limits) to learn the max size and lifetime of caches stored on Vercel.
To summarize, using `Cache-Control` headers with React Router on Vercel:
  * Allow you to cache responses for server-rendered React Router apps using Vercel Functions
  * Allow you to serve content from the cache _while updating the cache in the background_ with `stale-while-revalidate`


[Learn more about caching](https://vercel.com/docs/cdn-cache#how-to-cache-responses)
