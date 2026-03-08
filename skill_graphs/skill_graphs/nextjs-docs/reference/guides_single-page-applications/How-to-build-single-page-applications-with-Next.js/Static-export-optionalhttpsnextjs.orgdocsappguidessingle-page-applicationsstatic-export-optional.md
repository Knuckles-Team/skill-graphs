## Static export (optional)[](https://nextjs.org/docs/app/guides/single-page-applications#static-export-optional)
Next.js also supports generating a fully [static site](https://nextjs.org/docs/app/guides/static-exports). This has some advantages over strict SPAs:
  * **Automatic code-splitting** : Instead of shipping a single `index.html`, Next.js will generate an HTML file per route, so your visitors get the content faster without waiting for the client JavaScript bundle.
  * **Improved user experience:** Instead of a minimal skeleton for all routes, you get fully rendered pages for each route. When users navigate client side, transitions remain instant and SPA-like.


To enable a static export, update your configuration:
next.config.ts
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  output: 'export',
}

export default nextConfig
```

After running `next build`, Next.js will create an `out` folder with the HTML/CSS/JS assets for your application.
> **Note:** Next.js server features are not supported with static exports. [Learn more](https://nextjs.org/docs/app/guides/static-exports#unsupported-features).
