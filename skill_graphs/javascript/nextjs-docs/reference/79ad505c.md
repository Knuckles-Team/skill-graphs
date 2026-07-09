# How to use Next.js as a backend for your frontend
Last updated February 27, 2026
Next.js supports the "Backend for Frontend" pattern. This lets you create public endpoints to handle HTTP requests and return any content type—not just HTML. You can also access data sources and perform side effects like updating remote data.
If you are starting a new project, using `create-next-app` with the `--api` flag automatically includes an example `route.ts` in your new project's `app/` folder, demonstrating how to create an API endpoint.
pnpmnpmyarnbun
Terminal
```
pnpm create next-app --api
```

> **Good to know** : Next.js backend capabilities are not a full backend replacement. They serve as an API layer that:
>   * is publicly reachable
>   * handles any HTTP request
>   * can return any content type
>

To implement this pattern, use:
  * [Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route)
  * [`proxy`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy)
  * In Pages Router, [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
