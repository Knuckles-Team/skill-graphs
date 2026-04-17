##  [Vercel Functions](https://vercel.com/docs/getting-started-with-vercel#vercel-functions)[](https://vercel.com/docs/getting-started-with-vercel#vercel-functions)
[Vercel Functions](https://vercel.com/docs/functions) enable developers to write functions that use resources that scale up and down based on traffic demands. This prevents them from failing during peak hours, but keeps them from running up high costs during periods of low activity.
Nuxt deploys routes defined in `/server/api`, `/server/routes`, and `/server/middleware` as one server-rendered Function by default. Nuxt Pages, APIs, and Middleware routes get bundled into a single Vercel Function.
The following is an example of a basic API Route in Nuxt:
server/api/hello.ts
TypeScript
TypeScript JavaScript Bash
```
export default defineEventHandler(() => 'Hello World!');
```

You can test your API Routes with `nuxt dev`.
