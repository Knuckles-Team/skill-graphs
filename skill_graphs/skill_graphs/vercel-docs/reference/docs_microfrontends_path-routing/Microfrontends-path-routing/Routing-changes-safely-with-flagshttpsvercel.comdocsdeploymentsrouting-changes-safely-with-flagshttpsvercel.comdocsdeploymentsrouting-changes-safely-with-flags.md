##  [Routing changes safely with flags](https://vercel.com/docs/deployments#routing-changes-safely-with-flags)[](https://vercel.com/docs/deployments#routing-changes-safely-with-flags)
This is only compatible with Next.js.
If you want to dynamically control the routing for a path, you can use flags to make sure that the change is safe before enabling the routing change permanently. Instead of automatically routing the path to the microfrontend, the request will be sent to the default application which then decides whether the request should be routed to the microfrontend.
This is compatible with the
If using this with the Flags SDK, make sure to share the same value of the `FLAGS_SECRET` environment between all microfrontends in the same group.
  1. ###  [Specify a flag name](https://vercel.com/docs/deployments#specify-a-flag-name)[](https://vercel.com/docs/deployments#specify-a-flag-name)
In your `microfrontends.json` file, add a name in the `flag` field for the group of paths:
microfrontends.json
```
{
  "$schema": "https://openapi.vercel.sh/microfrontends.json",
  "applications": {
    "web": {},
    "docs": {
      "routing": [
        {
          "flag": "name-of-feature-flag",
          "paths": ["/flagged-path"]
        }
      ]
    }
  }
}
```

Instead of being automatically routed to the `docs` microfrontend, requests to `/flagged-path` will now be routed to the default application to make the decision about routing.
  2. ###  [Add microfrontends middleware](https://vercel.com/docs/deployments#add-microfrontends-middleware)[](https://vercel.com/docs/deployments#add-microfrontends-middleware)
The `@vercel/microfrontends` package uses middleware to route requests to the correct location for flagged paths and based on what microfrontends were deployed for your commit. Only the default application needs microfrontends middleware.
You can add it to your Next.js application with the following code:
middleware.ts
```
import type { NextRequest } from 'next/server';
import { runMicrofrontendsMiddleware } from '@vercel/microfrontends/next/middleware';

export async function middleware(request: NextRequest) {
  const response = await runMicrofrontendsMiddleware({
    request,
    flagValues: {
      'name-of-feature-flag': async () => { ... },
    }
  });
  if (response) {
    return response;
  }
}

// Define routes or paths where this middleware should apply
export const config = {
  matcher: [
    '/.well-known/vercel/microfrontends/client-config', // For prefetch optimizations for flagged paths
    '/flagged/path',
  ],
};
```

Your middleware matcher should include `/.well-known/vercel/microfrontends/client-config`. This endpoint is used by the client to know which application the path is being routed to for prefetch optimizations. The client will make a request to this well known endpoint to fetch the result of the path routing decision for this session.
Make sure that any flagged paths are also configured in the
Any function that returns `Promise<boolean>` can be used as the implementation of the flag. This also works directly with [feature flags](https://vercel.com/docs/feature-flags) on Vercel.
If the flag returns true, the microfrontends middleware will route the path to the microfrontend specified in `microfrontends.json`. If it returns false, the request will continue to be handled by the default application.
We recommend setting up [`validateMiddlewareConfig`](https://vercel.com/docs/microfrontends/troubleshooting#validatemiddlewareconfig) and [`validateMiddlewareOnFlaggedPaths`](https://vercel.com/docs/microfrontends/troubleshooting#validatemiddlewareonflaggedpaths) tests to prevent many common middleware misconfigurations.
