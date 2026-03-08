##  [Vercel Functions](https://vercel.com/docs/getting-started-with-vercel#vercel-functions)[](https://vercel.com/docs/getting-started-with-vercel#vercel-functions)
Vercel Functions scale up and down their resource consumption based on traffic demands. This scaling prevents them from failing during peak hours, but keeps them from running up high costs during periods of low activity.
If your project uses [a Vite community plugin](https://vercel.com/docs/getting-started-with-vercel#using-vite-community-plugins), such as
If you're using a framework built on Vite, check that framework's official documentation or [our dedicated framework docs](https://vercel.com/docs/frameworks). Some frameworks built on Vite, such as [SvelteKit](https://vercel.com/docs/frameworks/sveltekit), support Functions natively. We recommend using that framework's method for implementing Functions.
If you're not using a framework or plugin that supports Vercel Functions, you can still use them in your project by creating routes in an `api` directory at the root of your project.
The following example demonstrates a basic Vercel Function defined in an `api` directory:
api/handler.ts
TypeScript
TypeScript JavaScript Bash
```
import type { VercelRequest, VercelResponse } from '@vercel/node';

export default function handler(
  request: VercelRequest,
  response: VercelResponse,
) {
  response.status(200).json({
    body: request.body,
    query: request.query,
    cookies: request.cookies,
  });
}
```

To summarize, Vercel Functions on Vercel:
  * Scales to zero when not in use
  * Scales automatically with traffic increases
  * Support standard `URLPattern`, `Response`, and more


[Learn more about Vercel Functions](https://vercel.com/docs/functions)
