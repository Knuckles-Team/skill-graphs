##  [Vercel Functions](https://vercel.com/docs/getting-started-with-vercel#vercel-functions)[](https://vercel.com/docs/getting-started-with-vercel#vercel-functions)
[Vercel Functions](https://vercel.com/docs/functions) use resources that scale up and down based on traffic demands. This makes them reliable during peak hours, but low cost during slow periods.
When you [enable SSR with Astro's Vercel adapter](https://vercel.com/docs/getting-started-with-vercel#using-vercel's-features-with-astro), all of your routes will be server-rendered as Vercel functions by default. Astro's
When defining an Endpoint, you must name each function after the HTTP method it represents. The following example defines basic HTTP methods in a Server Endpoint:
src/pages/methods.json.ts
TypeScript
TypeScript JavaScript Bash
```
import { APIRoute } from 'astro/dist/@types/astro';

export const GET: APIRoute = ({ params, request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a GET!',
    }),
  );
};

export const POST: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a POST!',
    }),
  );
};

export const DELETE: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: 'This was a DELETE!',
    }),
  );
};

// ALL matches any method that you haven't implemented.
export const ALL: APIRoute = ({ request }) => {
  return new Response(
    JSON.stringify({
      message: `This was a ${request.method}!`,
    }),
  );
};
```

Astro removes the final file during the build process, so the name of the file should include the extension of the data you want serve (for example `example.png.js` will become `/example.png`).
Vercel Functions with Astro on Vercel:
  * Scale to zero when not in use
  * Scale automatically as traffic increases


[Learn more about Vercel Functions](https://vercel.com/docs/functions)
