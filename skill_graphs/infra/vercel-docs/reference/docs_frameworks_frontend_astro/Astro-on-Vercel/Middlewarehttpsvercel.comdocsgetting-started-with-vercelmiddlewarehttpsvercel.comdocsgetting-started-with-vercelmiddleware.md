##  [Middleware](https://vercel.com/docs/getting-started-with-vercel#middleware)[](https://vercel.com/docs/getting-started-with-vercel#middleware)
[Middleware](https://vercel.com/docs/routing-middleware) is a function that execute before a request is processed on a site, enabling you to modify the response. Because it runs before the cache, Middleware is an effective way to personalize statically generated content.
`middleware.ts` file in your `src` directory. The following example edits the global `locals` object, adding data which will be available in any `.astro` file:
src/middleware.ts
TypeScript
TypeScript JavaScript Bash
```
// This helper automatically types middleware params
import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware(({ locals }, next) => {
  // intercept data from a request
  // optionally, modify the properties in `locals`
  locals.title = 'New title';

  // return a Response or the result of calling `next()`
  return next();
});
```

**
Astro middleware is not the same as Vercel's Routing Middleware
**
, which has to be placed at the root directory of your project, outside `src`.
To add custom properties to `locals` in `middleware.ts`, you must declare a global namespace in your `env.d.ts` file:
src/env.d.ts
```
declare namespace App {
  interface Locals {
    title?: string;
  }
}
```

You can then access the data you added to `locals` in any `.astro` file, like so:
src/pages/middleware-title.astro
```
---
const { title } = Astro.locals;
---
<h1>{title}</h1>
<p>The name of this page is from middleware.</p>
```

###  [Deploying middleware at the Edge](https://vercel.com/docs/getting-started-with-vercel#deploying-middleware-at-the-edge)[](https://vercel.com/docs/getting-started-with-vercel#deploying-middleware-at-the-edge)
You can deploy Astro's middleware at the Edge, giving you access to data in the `RequestContext` and `Request`, and enabling you to use [Vercel's Routing Middleware helpers](https://vercel.com/docs/routing-middleware/api#routing-middleware-helper-methods), such as [`geolocation()`](https://vercel.com/docs/routing-middleware/api#geolocation) or [`ipAddress()`](https://vercel.com/docs/routing-middleware/api#geolocation).
To use Astro's middleware at the Edge, set `edgeMiddleware: true` in your `astro.config.ts` file:
astro.config.ts
TypeScript
TypeScript JavaScript Bash
```
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  output: 'server',
  adapter: vercel({
    edgeMiddleware: true,
  }),
});
```

If you're using [Vercel's Routing Middleware](https://vercel.com/docs/getting-started-with-vercel#using-vercel's-edge-middleware), you do not need to set `edgeMiddleware: true` in your `astro.config.ts` file.
See Astro's docs on
####  [Using `Astro.locals` in Routing Middleware](https://vercel.com/docs/getting-started-with-vercel#using-astro.locals-in-routing-middleware)[](https://vercel.com/docs/getting-started-with-vercel#using-astro.locals-in-routing-middleware)
The `Astro.locals` object exposes data to your `.astro` components, allowing you to dynamically modify your content with middleware. To make changes to `Astro.locals` in Astro's middleware at the edge:
  1. Add a new middleware file next to your `src/middleware.ts` and name it `src/vercel-edge-middleware.ts`. This file name is required to make changes to `Astro.locals`, this step is not required
  2. Return an object with the properties you want to add to `Astro.locals`:
For TypeScript, you must install [the `@vercel/functions` package](https://vercel.com/docs/routing-middleware/api#routing-middleware-helper-methods):
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/functions
```

```
yarn add @vercel/functions
```

```
npm i @vercel/functions
```

```
bun add @vercel/functions
```

Then, type your middleware function like so:
src/vercel-edge-middleware.ts
TypeScript
TypeScript JavaScript Bash
```
import type { RequestContext } from '@vercel/functions';

// Note the parameters are different from standard Astro middleware
export default function ({
  request,
  context,
}: {
  request: Request;
  context: RequestContext;
}) {
  // Return an Astro.locals object with a title property
  return {
    title: "Spider-man's blog",
  };
}
```



###  [Using Vercel's Routing Middleware](https://vercel.com/docs/getting-started-with-vercel#using-vercel's-routing-middleware)[](https://vercel.com/docs/getting-started-with-vercel#using-vercel's-routing-middleware)
Astro's middleware, which should be in `src/middleware.ts`, is distinct from Vercel Routing Middleware, which should be a `middleware.ts` file at the root of your project.
Vercel recommends using framework-native solutions. You should use Astro's middleware over Vercel's Routing Middleware wherever possible.
If you still want to use Vercel's Routing Middleware, see [the Quickstart](https://vercel.com/docs/routing-middleware/getting-started) to learn how.
###  [Rewrites](https://vercel.com/docs/getting-started-with-vercel#rewrites)[](https://vercel.com/docs/getting-started-with-vercel#rewrites)
Rewrites only work for static files with Astro. You must use [Vercel's Routing Middleware](https://vercel.com/docs/routing-middleware/api#match-paths-based-on-conditional-statements) for rewrites. You should not use `vercel.json` to rewrite URL paths with astro projects; doing so produces inconsistent behavior, and is not officially supported.
###  [Redirects](https://vercel.com/docs/getting-started-with-vercel#redirects)[](https://vercel.com/docs/getting-started-with-vercel#redirects)
In general, Vercel recommends using framework-native solutions, and Astro has [Vercel's Routing Middleware](https://vercel.com/docs/routing-middleware/getting-started).
####  [Redirects in your Astro config](https://vercel.com/docs/getting-started-with-vercel#redirects-in-your-astro-config)[](https://vercel.com/docs/getting-started-with-vercel#redirects-in-your-astro-config)
You can do redirects on Astro with `astro.config.ts` the `redirects` config option as shown below:
astro.config.ts
TypeScript
TypeScript JavaScript Bash
```
import { defineConfig } from 'astro/config';

export default defineConfig({
  redirects: {
    '/old-page': '/new-page',
  },
});
```

####  [Redirects in Server Endpoints](https://vercel.com/docs/getting-started-with-vercel#redirects-in-server-endpoints)[](https://vercel.com/docs/getting-started-with-vercel#redirects-in-server-endpoints)
You can also return a redirect from a Server Endpoint using the
src/pages/links/[id].ts
TypeScript
TypeScript JavaScript Bash
```
export async function GET({ params, redirect }): APIRoute {
  return redirect('/redirect-path', 307);
}
```

####  [Redirects in components](https://vercel.com/docs/getting-started-with-vercel#redirects-in-components)[](https://vercel.com/docs/getting-started-with-vercel#redirects-in-components)
You can redirect from within Astro components with
src/pages/account.astro
```
---
import { isLoggedIn } from '../utils';

const cookie = Astro.request.headers.get('cookie');

// If the user is not logged in, redirect them to the login page
if (!isLoggedIn(cookie)) {
  return Astro.redirect('/login');
}
---

<h1>You can only see this page while logged in</h1>
```

Astro Middleware on Vercel:
  * Executes before a request is processed on a site, allowing you to modify responses to user requests
  * Runs on _all_ requests, but can be scoped to specific paths [through a `matcher` config](https://vercel.com/docs/routing-middleware/api#match-paths-based-on-custom-matcher-config)
  * Uses Vercel's lightweight Edge Runtime to keep costs low and responses fast


[Learn more about Routing Middleware](https://vercel.com/docs/routing-middleware)
