##  [Server-Side Rendering](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering)[](https://vercel.com/docs/getting-started-with-vercel#server-side-rendering)
Using SSR, or
You can enable SSR by [adding the Vercel adapter to your project](https://vercel.com/docs/getting-started-with-vercel#using-vercel's-features-with-astro).
If your Astro project is statically rendered, you can opt individual routes. To do so:
  1. Set your `output` option to `hybrid` in your `<PreferredExtension filename="astro.config" mjs />`:
astro.config.ts
TypeScript
TypeScript JavaScript Bash
```
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  output: 'hybrid',
  adapter: vercel({
    edgeMiddleware: true,
  }),
});
```

  2. Add `export const prerender = false;` to your components:
src/pages/mypage.astro
```
---
export const prerender = false;
// ...
---
<html>
  <!-- Server-rendered page here... -->
</html>
```



SSR with Astro on Vercel:
  * Scales to zero when not in use
  * Scales automatically with traffic increases
  * Has zero-configuration support for [`Cache-Control` headers](https://vercel.com/docs/cdn-cache), including `stale-while-revalidate`


###  [Static rendering](https://vercel.com/docs/getting-started-with-vercel#static-rendering)[](https://vercel.com/docs/getting-started-with-vercel#static-rendering)
Statically rendered, or pre-rendered, Astro apps can be deployed to Vercel with zero configuration. To enable Vercel features like Image Optimization or Web Analytics, see [Using Vercel's features with Astro](https://vercel.com/docs/getting-started-with-vercel#using-vercel's-features-with-astro).
You can opt individual routes into static rendering with `export const prerender = true` as shown below:
src/pages/mypage.astro
```
---
export const prerender = true;
// ...
---
<html>
  <!-- Static, pre-rendered page here... -->
</html>
```

Statically rendered Astro sites on Vercel:
  * Require zero configuration to deploy
  * Can use Vercel features with `astro.config.ts`
