## Migration Steps[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#migration-steps)
Our goal is to get a working Next.js application as quickly as possible so that you can then adopt Next.js features incrementally. To begin with, we’ll treat your application as a purely client-side application ([SPA](https://nextjs.org/docs/app/guides/single-page-applications)) without immediately replacing your existing router. This reduces complexity and merge conflicts.
> **Note** : If you are using advanced CRA configurations such as a custom `homepage` field in your `package.json`, a custom service worker, or specific Babel/webpack tweaks, please see the **Additional Considerations** section at the end of this guide for tips on replicating or adapting these features in Next.js.
### Step 1: Install the Next.js Dependency[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-1-install-the-nextjs-dependency)
Install Next.js in your existing project:
pnpmnpmyarnbun
Terminal
```
pnpm add next@latest
```

### Step 2: Create the Next.js Configuration File[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-2-create-the-nextjs-configuration-file)
Create a `next.config.ts` at the root of your project (same level as your `package.json`). This file holds your [Next.js configuration options](https://nextjs.org/docs/app/api-reference/config/next-config-js).
next.config.ts
```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  output: 'export', // Outputs a Single-Page Application (SPA)
  distDir: 'build', // Changes the build output directory to `build`
}

export default nextConfig
```

> **Note** : Using `output: 'export'` means you’re doing a static export. You will **not** have access to server-side features like SSR or APIs. You can remove this line to leverage Next.js server features.
### Step 3: Create the Root Layout[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-3-create-the-root-layout)
A Next.js [App Router](https://nextjs.org/docs/app) application must include a [root layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout) file, which is a [React Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) that will wrap all your pages.
The closest equivalent of the root layout file in a CRA application is `public/index.html`, which includes your `<html>`, `<head>`, and `<body>` tags.
  1. Create a new `app` directory inside your `src` folder (or at your project root if you prefer `app` at the root).
  2. Inside the `app` directory, create a `layout.tsx` (or `layout.js`) file:


app/layout.tsx
TypeScript
JavaScript TypeScript
```
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return '...'
}
```

Now copy the content of your old `index.html` into this `<RootLayout>` component. Replace `body div#root` (and `body noscript`) with `<div id="root">{children}</div>`.
app/layout.tsx
TypeScript
JavaScript TypeScript
```
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <meta charSet="UTF-8" />
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

> **Good to know** : Next.js ignores CRA’s `public/manifest.json`, additional iconography, and [testing configuration](https://nextjs.org/docs/app/guides/testing) by default. If you need these, Next.js has support with its [Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images) and [Testing](https://nextjs.org/docs/app/guides/testing) setup.
### Step 4: Metadata[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-4-metadata)
Next.js automatically includes the `<meta charset="UTF-8" />` and `<meta name="viewport" content="width=device-width, initial-scale=1" />` tags, so you can remove them from `<head>`:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

Any [metadata files](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#file-based-metadata) such as `favicon.ico`, `icon.png`, `robots.txt` are automatically added to the application `<head>` tag as long as you have them placed into the top level of the `app` directory. After moving [all supported files](https://nextjs.org/docs/app/getting-started/metadata-and-og-images#file-based-metadata) into the `app` directory you can safely delete their `<link>` tags:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <title>React App</title>
        <meta name="description" content="Web site created..." />
      </head>
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

Finally, Next.js can manage your last `<head>` tags with the [Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images). Move your final metadata info into an exported [`metadata` object](https://nextjs.org/docs/app/api-reference/functions/generate-metadata#metadata-object):
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'React App',
  description: 'Web site created with Next.js.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

With the above changes, you shifted from declaring everything in your `index.html` to using Next.js' convention-based approach built into the framework ([Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)). This approach enables you to more easily improve your SEO and web shareability of your pages.
### Step 5: Styles[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-5-styles)
Like CRA, Next.js supports [CSS Modules](https://nextjs.org/docs/app/getting-started/css#css-modules) out of the box. It also supports [global CSS imports](https://nextjs.org/docs/app/getting-started/css#global-css).
If you have a global CSS file, import it into your `app/layout.tsx`:
app/layout.tsx
TypeScript
JavaScript TypeScript
```
import '../index.css'

export const metadata = {
  title: 'React App',
  description: 'Web site created with Next.js.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <div id="root">{children}</div>
      </body>
    </html>
  )
}
```

If you're using Tailwind CSS, see our [installation docs](https://nextjs.org/docs/app/getting-started/css#tailwind-css).
### Step 6: Create the Entrypoint Page[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-6-create-the-entrypoint-page)
Create React App uses `src/index.tsx` (or `index.js`) as the entry point. In Next.js (App Router), each folder inside the `app` directory corresponds to a route, and each folder should have a `page.tsx`.
Since we want to keep the app as an SPA for now and intercept **all** routes, we’ll use an [optional catch-all route](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#optional-catch-all-segments).
  1. **Create a`[[...slug]]` directory inside `app`.**


```
app
 ┣ [[...slug]]
 ┃ ┗ page.tsx
 ┣ layout.tsx
```

  1. **Add the following to`page.tsx`** :


app/[[...slug]]/page.tsx
TypeScript
JavaScript TypeScript
```
export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return '...' // We'll update this
}
```

This tells Next.js to generate a single route for the empty slug (`/`), effectively mapping **all** routes to the same page. This page is a [Server Component](https://nextjs.org/docs/app/getting-started/server-and-client-components), prerendered into static HTML.
### Step 7: Add a Client-Only Entrypoint[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-7-add-a-client-only-entrypoint)
Next, we’ll embed your CRA’s root App component inside a [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) so that all logic remains client-side. If this is your first time using Next.js, it's worth knowing that clients components (by default) are still prerendered on the server. You can think about them as having the additional capability of running client-side JavaScript.
Create a `client.tsx` (or `client.js`) in `app/[[...slug]]/`:
app/[[...slug]]/client.tsx
TypeScript
JavaScript TypeScript
```
'use client'

import dynamic from 'next/dynamic'

const App = dynamic(() => import('../../App'), { ssr: false })

export function ClientOnly() {
  return <App />
}
```

  * The `'use client'` directive makes this file a **Client Component**.
  * The `dynamic` import with `ssr: false` disables server-side rendering for the `<App />` component, making it truly client-only (SPA).


Now update your `page.tsx` (or `page.js`) to use your new component:
app/[[...slug]]/page.tsx
TypeScript
JavaScript TypeScript
```
import { ClientOnly } from './client'

export function generateStaticParams() {
  return [{ slug: [''] }]
}

export default function Page() {
  return <ClientOnly />
}
```

### Step 8: Update Static Image Imports[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-8-update-static-image-imports)
In CRA, importing an image file returns its public URL as a string:
```
import image from './img.png'

export default function App() {
  return <img src={image} />
}
```

With Next.js, static image imports return an object. The object can then be used directly with the Next.js [`<Image>` component](https://nextjs.org/docs/app/api-reference/components/image), or you can use the object's `src` property with your existing `<img>` tag.
The `<Image>` component has the added benefits of [automatic image optimization](https://nextjs.org/docs/app/api-reference/components/image). The `<Image>` component automatically sets the `width` and `height` attributes of the resulting `<img>` based on the image's dimensions. This prevents layout shifts when the image loads. However, this can cause issues if your app contains images with only one of their dimensions being styled without the other styled to `auto`. When not styled to `auto`, the dimension will default to the `<img>` dimension attribute's value, which can cause the image to appear distorted.
Keeping the `<img>` tag will reduce the amount of changes in your application and prevent the above issues. You can then optionally later migrate to the `<Image>` component to take advantage of optimizing images by [configuring a loader](https://nextjs.org/docs/app/api-reference/components/image#loader), or moving to the default Next.js server which has automatic image optimization.
**Convert absolute import paths for images imported from`/public` into relative imports:**
```
// Before
import logo from '/logo.png'

// After
import logo from '../public/logo.png'
```

**Pass the image`src` property instead of the whole image object to your `<img>` tag:**
```
// Before
<img src={logo} />

// After
<img src={logo.src} />
```

Alternatively, you can reference the public URL for the image asset based on the filename. For example, `public/logo.png` will serve the image at `/logo.png` for your application, which would be the `src` value.
> **Warning:** If you're using TypeScript, you might encounter type errors when accessing the `src` property. To fix them, you need to add `next-env.d.ts` to the `tsconfig.json` file. Next.js will automatically generate this file when you run your application on step 9.
### Step 9: Migrate Environment Variables[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-9-migrate-environment-variables)
Next.js supports [environment variables](https://nextjs.org/docs/app/guides/environment-variables) similarly to CRA but **requires** a `NEXT_PUBLIC_` prefix for any variable you want to expose in the browser.
The main difference is the prefix used to expose environment variables on the client-side. Change all environment variables with the `REACT_APP_` prefix to `NEXT_PUBLIC_`.
### Step 10: Update Scripts in `package.json`[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-10-update-scripts-in-packagejson)
Update your `package.json` scripts to use Next.js commands. Also, add `.next` and `next-env.d.ts` to your `.gitignore`:
package.json
```
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "npx serve@latest ./build"
  }
}
```

.gitignore
```
# ...
.next
next-env.d.ts
```

Now you can run:
pnpmnpmyarnbun
Terminal
```
pnpm dev
```

Open
### Step 11: Clean Up[](https://nextjs.org/docs/app/guides/migrating/from-create-react-app#step-11-clean-up)
You can now remove artifacts that are specific to Create React App:
  * `public/index.html`
  * `src/index.tsx`
  * `src/react-app-env.d.ts`
  * The `reportWebVitals` setup
  * The `react-scripts` dependency (uninstall it from `package.json`)
