##  [Using Vite community plugins](https://vercel.com/docs/getting-started-with-vercel#using-vite-community-plugins)[](https://vercel.com/docs/getting-started-with-vercel#using-vite-community-plugins)
Although Vite offers modern features like [SSR](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr) and [Vercel functions](https://vercel.com/docs/getting-started-with-vercel#vercel-functions) out of the box, implementing those features can sometimes require complex configuration steps. Because of this, many Vite users prefer to use
Vite's plugins are based on
We recommend using Vite plugins to configure your project when possible.
###  [`vite-plugin-vercel`](https://vercel.com/docs/getting-started-with-vercel#vite-plugin-vercel)[](https://vercel.com/docs/getting-started-with-vercel#vite-plugin-vercel)
[the Build Output API spec](https://vercel.com/docs/build-output-api/v3). It enables your Vite apps to use the following Vercel features:
  * [Server-Side Rendering (SSR)](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr)
  * [Vercel functions](https://vercel.com/docs/getting-started-with-vercel#vercel-functions)
  * [Incremental Static Regeneration](https://vercel.com/docs/incremental-static-regeneration)
  * [Static Site Generation](https://vercel.com/docs/build-output-api/v3/primitives#static-files)


When using the Vercel CLI, set the port as an environment variable. To allow Vite to access this, include the environment variable in your `vite.config` file:
vite.config.ts
TypeScript
TypeScript JavaScript Bash
```
import { defineConfig } from 'vite';
import vercel from 'vite-plugin-vercel';

export default defineConfig({
  server: {
    port: process.env.PORT as unknown as number,
  },
  plugins: [vercel()],
});
```

###  [`vite-plugin-ssr`](https://vercel.com/docs/getting-started-with-vercel#vite-plugin-ssr)[](https://vercel.com/docs/getting-started-with-vercel#vite-plugin-ssr)
[the Build Output API spec](https://vercel.com/docs/build-output-api/v3). It enables your Vite apps to do the following:
  * [Server-Side Rendering (SSR)](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering-ssr)
  * [Vercel functions](https://vercel.com/docs/getting-started-with-vercel#vercel-functions)
  * [Static Site Generation](https://vercel.com/docs/build-output-api/v3/primitives#static-files)
