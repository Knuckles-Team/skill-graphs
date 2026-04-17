##  [Using Vercel's features with Astro](https://vercel.com/docs/getting-started-with-vercel#using-vercel's-features-with-astro)[](https://vercel.com/docs/getting-started-with-vercel#using-vercel's-features-with-astro)
To deploy a server-rendered Astro app, or a static Astro site with Vercel features like Web Analytics and Image Optimization, you must:
  1. Add
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm astro add vercel
```

```
yarn astro add @astrojs/vercel
```

```
npx astro add @astrojs/vercel
```

```
bun add @astrojs/vercel
```

     * Or, manually installing the
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @astrojs/vercel
```

```
yarn add @astrojs/vercel
```

```
npm i @astrojs/vercel
```

```
bun add @astrojs/vercel
```



  1. Configure your project. In your `astro.config.ts` file, import either the `serverless` or `static` plugin, and set the output to `server` or `static` respectively:
Serverless SSRStatic
astro.config.ts
TypeScript
TypeScript JavaScript Bash
```
import { defineConfig } from 'astro/config';
// Import /serverless for a Serverless SSR site
import vercelServerless from '@astrojs/vercel/serverless';

export default defineConfig({
  output: 'server',
  adapter: vercelServerless(),
});
```

astro.config.ts
TypeScript
TypeScript JavaScript Bash
```
import { defineConfig } from 'astro/config';
// Import /static for a static site
import vercelStatic from '@astrojs/vercel/static';

export default defineConfig({
  // Must be 'static' or 'hybrid'
  output: 'static',
  adapter: vercelStatic(),
});
```

  2. Enable Vercel's features using Astro's [configuration options](https://vercel.com/docs/getting-started-with-vercel#configuration-options). The following example `astro.config.ts` enables Web Analytics and adds a maximum duration to Vercel Function routes:
astro.config.ts
TypeScript
TypeScript JavaScript Bash
```
import { defineConfig } from 'astro/config';
// Also can be @astrojs/vercel/static
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  // Also can be 'static' or 'hybrid'
  output: 'server',
  adapter: vercel({
    webAnalytics: {
      enabled: true,
    },
    maxDuration: 8,
  }),
});
```



###  [Configuration options](https://vercel.com/docs/getting-started-with-vercel#configuration-options)[](https://vercel.com/docs/getting-started-with-vercel#configuration-options)
The following configuration options enable Vercel's features for Astro deployments.
Option | type | Rendering | Purpose
---|---|---|---
[`maxDuration`](https://vercel.com/docs/functions/runtimes#max-duration) | `number` | Serverless | Extends or limits the maximum duration (in seconds) that Vercel functions can run before timing out.
[`webAnalytics`](https://vercel.com/docs/analytics) | `{enabled: boolean}` | Static, Serverless | Enables Vercel's [Web Analytics](https://vercel.com/docs/analytics). See [the quickstart](https://vercel.com/docs/analytics/quickstart) to set up analytics on your account.
| `boolean` | Static, Serverless | For astro versions `3` and up. Enables an automatically
| `string` | Static, Serverless | For astro versions `3` and up. Configure the
[`imagesConfig`](https://vercel.com/docs/build-output-api/v3/configuration#images) | `VercelImageConfig` | Static, Serverless | Defines the behavior of the Image Optimization API, allowing on-demand optimization at runtime. See [the Build Output API docs](https://vercel.com/docs/build-output-api/v3/configuration#images) for required options.
| `boolean` | Serverless | API routes are bundled into one function by default. Set this to true to split each route into separate functions.
| `boolean` | Serverless | Set to `true` to automatically convert Astro middleware to Routing Middleware, eliminating the need for a `middleware.ts` file.
| `string[]` | Serverless | Force files to be bundled with your Vercel functions.
| `string[]` | Serverless | Exclude files from being bundled with your Vercel functions. Also available with [`.vercelignore`](https://vercel.com/docs/deployments/vercel-ignore)
For more details on the configuration options, see
