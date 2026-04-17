## Folder and file conventions[](https://nextjs.org/docs/app/getting-started/project-structure#folder-and-file-conventions)
### Top-level folders[](https://nextjs.org/docs/app/getting-started/project-structure#top-level-folders)
Top-level folders are used to organize your application's code and static assets.
![Route segments to path segments](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ftop-level-folders.png&w=3840&q=75)![Route segments to path segments](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ftop-level-folders.png&w=3840&q=75)
|
---|---
[`app`](https://nextjs.org/docs/app) | App Router
[`pages`](https://nextjs.org/docs/pages/building-your-application/routing) | Pages Router
[`public`](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder) | Static assets to be served
[`src`](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder) | Optional application source folder
### Top-level files[](https://nextjs.org/docs/app/getting-started/project-structure#top-level-files)
Top-level files are used to configure your application, manage dependencies, run proxy, integrate monitoring tools, and define environment variables.
|
---|---
**Next.js** |
[`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js) | Configuration file for Next.js
[`package.json`](https://nextjs.org/docs/app/getting-started/installation#manual-installation) | Project dependencies and scripts
[`instrumentation.ts`](https://nextjs.org/docs/app/guides/instrumentation) | OpenTelemetry and Instrumentation file
[`proxy.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/proxy) | Next.js request proxy
[`.env`](https://nextjs.org/docs/app/guides/environment-variables) | Environment variables (should not be tracked by version control)
[`.env.local`](https://nextjs.org/docs/app/guides/environment-variables) | Local environment variables (should not be tracked by version control)
[`.env.production`](https://nextjs.org/docs/app/guides/environment-variables) | Production environment variables (should not be tracked by version control)
[`.env.development`](https://nextjs.org/docs/app/guides/environment-variables) | Development environment variables (should not be tracked by version control)
[`eslint.config.mjs`](https://nextjs.org/docs/app/api-reference/config/eslint) | Configuration file for ESLint
`.gitignore` | Git files and folders to ignore
[`next-env.d.ts`](https://nextjs.org/docs/app/api-reference/config/typescript#next-envdts) | TypeScript declaration file for Next.js (should not be tracked by version control)
`tsconfig.json` | Configuration file for TypeScript
`jsconfig.json` | Configuration file for JavaScript
### Routing Files[](https://nextjs.org/docs/app/getting-started/project-structure#routing-files)
Add `page` to expose a route, `layout` for shared UI such as header, nav, or footer, `loading` for skeletons, `error` for error boundaries, and `route` for APIs.
|  |
---|---|---
[`layout`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) |  `.js` `.jsx` `.tsx` | Layout
[`page`](https://nextjs.org/docs/app/api-reference/file-conventions/page) |  `.js` `.jsx` `.tsx` | Page
[`loading`](https://nextjs.org/docs/app/api-reference/file-conventions/loading) |  `.js` `.jsx` `.tsx` | Loading UI
[`not-found`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) |  `.js` `.jsx` `.tsx` | Not found UI
[`error`](https://nextjs.org/docs/app/api-reference/file-conventions/error) |  `.js` `.jsx` `.tsx` | Error UI
[`global-error`](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-error) |  `.js` `.jsx` `.tsx` | Global error UI
[`route`](https://nextjs.org/docs/app/api-reference/file-conventions/route) |  `.js` `.ts` | API endpoint
[`template`](https://nextjs.org/docs/app/api-reference/file-conventions/template) |  `.js` `.jsx` `.tsx` | Re-rendered layout
[`default`](https://nextjs.org/docs/app/api-reference/file-conventions/default) |  `.js` `.jsx` `.tsx` | Parallel route fallback page
### Nested routes[](https://nextjs.org/docs/app/getting-started/project-structure#nested-routes)
Folders define URL segments. Nesting folders nests segments. Layouts at any level wrap their child segments. A route becomes public when a `page` or `route` file exists.
Path | URL pattern | Notes
---|---|---
`app/layout.tsx` | — | Root layout wraps all routes
`app/blog/layout.tsx` | — | Wraps `/blog` and descendants
`app/page.tsx` | `/` | Public route
`app/blog/page.tsx` | `/blog` | Public route
`app/blog/authors/page.tsx` | `/blog/authors` | Public route
### Dynamic routes[](https://nextjs.org/docs/app/getting-started/project-structure#dynamic-routes)
Parameterize segments with square brackets. Use `[segment]` for a single param, `[...segment]` for catch‑all, and `[[...segment]]` for optional catch‑all. Access values via the [`params`](https://nextjs.org/docs/app/api-reference/file-conventions/page#params-optional) prop.
Path | URL pattern
---|---
`app/blog/[slug]/page.tsx` | `/blog/my-first-post`
`app/shop/[...slug]/page.tsx` |  `/shop/clothing`, `/shop/clothing/shirts`
`app/docs/[[...slug]]/page.tsx` |  `/docs`, `/docs/layouts-and-pages`, `/docs/api-reference/use-router`
### Route groups and private folders[](https://nextjs.org/docs/app/getting-started/project-structure#route-groups-and-private-folders)
Organize code without changing URLs with route groups [`(group)`](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups#convention), and colocate non-routable files with private folders [`_folder`](https://nextjs.org/docs/app/getting-started/project-structure#private-folders).
Path | URL pattern | Notes
---|---|---
`app/(marketing)/page.tsx` | `/` | Group omitted from URL
`app/(shop)/cart/page.tsx` | `/cart` | Share layouts within `(shop)`
`app/blog/_components/Post.tsx` | — | Not routable; safe place for UI utilities
`app/blog/_lib/data.ts` | — | Not routable; safe place for utils
### Parallel and Intercepted Routes[](https://nextjs.org/docs/app/getting-started/project-structure#parallel-and-intercepted-routes)
These features fit specific UI patterns, such as slot-based layouts or modal routing.
Use `@slot` for named slots rendered by a parent layout. Use intercept patterns to render another route inside the current layout without changing the URL, for example, to show a details view as a modal over a list.
Pattern (docs) | Meaning | Typical use case
---|---|---
[`@folder`](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#slots) | Named slot | Sidebar + main content
[`(.)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) | Intercept same level | Preview sibling route in a modal
[`(..)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) | Intercept parent | Open a child of the parent as an overlay
[`(..)(..)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) | Intercept two levels | Deeply nested overlay
[`(...)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) | Intercept from root | Show arbitrary route in current view
### Metadata file conventions[](https://nextjs.org/docs/app/getting-started/project-structure#metadata-file-conventions)
#### App icons[](https://nextjs.org/docs/app/getting-started/project-structure#app-icons)
|  |
---|---|---
[`favicon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon) | `.ico` | Favicon file
[`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon) |  `.ico` `.jpg` `.jpeg` `.png` `.svg` | App Icon file
[`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx) |  `.js` `.ts` `.tsx` | Generated App Icon
[`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon) |  `.jpg` `.jpeg`, `.png` | Apple App Icon file
[`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx) |  `.js` `.ts` `.tsx` | Generated Apple App Icon
#### Open Graph and Twitter images[](https://nextjs.org/docs/app/getting-started/project-structure#open-graph-and-twitter-images)
|  |
---|---|---
[`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image) |  `.jpg` `.jpeg` `.png` `.gif` | Open Graph image file
[`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx) |  `.js` `.ts` `.tsx` | Generated Open Graph image
[`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image) |  `.jpg` `.jpeg` `.png` `.gif` | Twitter image file
[`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx) |  `.js` `.ts` `.tsx` | Generated Twitter image
#### SEO[](https://nextjs.org/docs/app/getting-started/project-structure#seo)
|  |
---|---|---
[`sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#sitemap-files-xml) | `.xml` | Sitemap file
[`sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generating-a-sitemap-using-code-js-ts) |  `.js` `.ts` | Generated Sitemap
[`robots`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt) | `.txt` | Robots file
[`robots`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file) |  `.js` `.ts` | Generated Robots file
