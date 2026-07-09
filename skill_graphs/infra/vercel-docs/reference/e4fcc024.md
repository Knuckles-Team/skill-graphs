# Add the Vercel Toolbar to your local environment
Last updated December 17, 2025
To enable the toolbar in your local environment, add it to your project using the
  1. ###  [Install the `@vercel/toolbar` package and link your project](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost#install-the-@vercel/toolbar-package-and-link-your-project)[](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost#install-the-@vercel/toolbar-package-and-link-your-project)
Install the package using the following command:
Terminal
![](https://7nyt0uhk7sse4zvn.public.blob.vercel-storage.com/docs-assets/static/topics/icons/pnpm.svg)pnpm bun yarn npm
```
pnpm i @vercel/toolbar
```

```
yarn add @vercel/toolbar
```

```
npm i @vercel/toolbar
```

```
bun add @vercel/toolbar
```

Then link your local project to your Vercel project with the [`vercel link`](https://vercel.com/docs/cli/link) command using [Vercel CLI](https://vercel.com/docs/cli).
terminal
```
vercel link [path-to-directory]
```

  2. ###  [Add the toolbar to your project](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost#add-the-toolbar-to-your-project)[](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost#add-the-toolbar-to-your-project)
To use the Vercel Toolbar locally in a Next.js project, define `withVercelToolbar` in your `next.config.js` file and export it, as shown below:
next.config.ts
Next.js (/app)
Next.js (/app) Next.js (/pages) SvelteKit Nuxt Other frameworks
TypeScript
TypeScript JavaScript Bash
```
import type { NextConfig } from 'next';
import createWithVercelToolbar from '@vercel/toolbar/plugins/next';

const nextConfig: NextConfig = {
  // Config options here
};

const withVercelToolbar = createWithVercelToolbar();
// Instead of export default nextConfig, do this:
export default withVercelToolbar(nextConfig);
```

Then add the following code to your `layout.tsx` or `layout.jsx` file:
app/layout.tsx
Next.js (/app)
Next.js (/app) Next.js (/pages) SvelteKit Nuxt Other frameworks
TypeScript
TypeScript JavaScript Bash
```
import { VercelToolbar } from '@vercel/toolbar/next';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const shouldInjectToolbar = process.env.NODE_ENV === 'development';
  return (
    <html lang="en">
      <body>
        {children}
        {shouldInjectToolbar && <VercelToolbar />}
      </body>
    </html>
  );
}
```



* * *
[ Previous Add to Environments ](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost)[ Next Add to Production ](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-production)
Was this helpful?
Send
Next.js (/app)
Choose a framework to optimize documentation to:
  * Next.js (/app)
  * Next.js (/pages)
  * SvelteKit
  * Nuxt
  * Other frameworks


On this page
  * [Install the @vercel/toolbar package and link your project](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost#install-the-@vercel/toolbar-package-and-link-your-project)
  * [Add the toolbar to your project](https://vercel.com/docs/vercel-toolbar/in-production-and-localhost/add-to-localhost#add-the-toolbar-to-your-project)


Copy as MarkdownGive feedbackAsk AI about this page
