##  [Server-Side Rendering (SSR)](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr)[](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr)
Server-Side Rendering (SSR) allows you to render pages dynamically on the server. This is useful for pages where the rendered data needs to be unique on every request. For example, checking authentication or looking at the location of an incoming request.
Nuxt allows you to deploy your projects with a strategy called [in your Nuxt config](https://vercel.com/docs/getting-started-with-vercel#editing-your-nuxt-config).
When you deploy your app with Universal Rendering, it renders on the server once, then your client-side JavaScript code gets interpreted in the browser again once the page loads.
On Vercel, Nuxt apps are server-rendered by default
SSR with Nuxt on Vercel:
  * Scales to zero when not in use
  * Scales automatically with traffic increases
  * Allows you to opt individual routes out of SSR
