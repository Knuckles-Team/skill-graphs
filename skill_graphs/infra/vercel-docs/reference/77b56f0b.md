##  [Server-Side Rendering (SSR)](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr)[](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr)
Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request.
Vite exposes we recommend [using a Vite community plugin](https://vercel.com/docs/getting-started-with-vercel#using-vite-community-plugins).
See
To summarize, SSR with Vite on Vercel:
  * Scales to zero when not in use
  * Scales automatically with traffic increases
  * Has zero-configuration support for [`Cache-Control`](https://vercel.com/docs/cdn-cache) headers, including `stale-while-revalidate`
