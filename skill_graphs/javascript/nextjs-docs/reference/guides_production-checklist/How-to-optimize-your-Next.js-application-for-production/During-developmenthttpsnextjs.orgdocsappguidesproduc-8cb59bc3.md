## During development[](https://nextjs.org/docs/app/guides/production-checklist#during-development)
While building your application, we recommend using the following features to ensure the best performance and user experience:
### Routing and rendering[](https://nextjs.org/docs/app/guides/production-checklist#routing-and-rendering)
  * **[Layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout):** Use layouts to share UI across pages and enable [partial rendering](https://nextjs.org/docs/app/getting-started/linking-and-navigating#client-side-transitions) on navigation.
  * **[`<Link>`component](https://nextjs.org/docs/app/api-reference/components/link):** Use the `<Link>` component for [client-side navigation and prefetching](https://nextjs.org/docs/app/getting-started/linking-and-navigating#how-navigation-works).
  * **[Error Handling](https://nextjs.org/docs/app/getting-started/error-handling):** Gracefully handle [catch-all errors](https://nextjs.org/docs/app/getting-started/error-handling) and [404 errors](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) in production by creating custom error pages.
  * **[Client and Server Components](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples):** Follow the recommended composition patterns for Server and Client Components, and check the placement of your [`"use client"` boundaries](https://nextjs.org/docs/app/getting-started/server-and-client-components#examples#moving-client-components-down-the-tree) to avoid unnecessarily increasing your client-side JavaScript bundle.
  * **[Dynamic APIs](https://nextjs.org/docs/app/guides/caching#dynamic-rendering):** Be aware that Dynamic APIs like [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies) and the [`searchParams`](https://nextjs.org/docs/app/api-reference/file-conventions/page#searchparams-optional) prop will opt the entire route into [Dynamic Rendering](https://nextjs.org/docs/app/guides/caching#dynamic-rendering) (or your whole application if used in the [Root Layout](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout)). Ensure Dynamic API usage is intentional and wrap them in `<Suspense>` boundaries where appropriate.


> **Good to know** : [Partial Prerendering (experimental)](https://nextjs.org/blog/next-14#partial-prerendering-preview) will allow parts of a route to be dynamic without opting the whole route into dynamic rendering.
### Data fetching and caching[](https://nextjs.org/docs/app/guides/production-checklist#data-fetching-and-caching)
  * **[Server Components](https://nextjs.org/docs/app/getting-started/fetching-data):** Leverage the benefits of fetching data on the server using Server Components.
  * **[Route Handlers](https://nextjs.org/docs/app/api-reference/file-conventions/route):** Use Route Handlers to access your backend resources from Client Components. But do not call Route Handlers from Server Components to avoid an additional server request.
  * **[Streaming](https://nextjs.org/docs/app/api-reference/file-conventions/loading):** Use Loading UI and React Suspense to progressively send UI from the server to the client, and prevent the whole route from blocking while data is being fetched.
  * **[Parallel Data Fetching](https://nextjs.org/docs/app/getting-started/fetching-data#parallel-data-fetching):** Reduce network waterfalls by fetching data in parallel, where appropriate. Also, consider [preloading data](https://nextjs.org/docs/app/getting-started/fetching-data#preloading-data) where appropriate.
  * **[Data Caching](https://nextjs.org/docs/app/guides/caching#data-cache):** Verify whether your data requests are being cached or not, and opt into caching, where appropriate. Ensure requests that don't use `fetch` are [cached](https://nextjs.org/docs/app/api-reference/functions/unstable_cache).
  * **[Static Images](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder):** Use the `public` directory to automatically cache your application's static assets, e.g. images.


### UI and accessibility[](https://nextjs.org/docs/app/guides/production-checklist#ui-and-accessibility)
  * **[Forms and Validation](https://nextjs.org/docs/app/guides/forms):** Use Server Actions to handle form submissions, server-side validation, and handle errors.
  * **[Global Error UI](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-error):** Add `app/global-error.tsx` to provide consistent, accessible fallback UI and recovery for uncaught errors across your app.
  * **[Global 404](https://nextjs.org/docs/app/api-reference/file-conventions/not-found#global-not-foundjs-experimental):** Add `app/global-not-found.tsx` to serve an accessible 404 for unmatched routes across your app.


  * **[Font Module](https://nextjs.org/docs/app/api-reference/components/font):** Optimize fonts by using the Font Module, which automatically hosts your font files with other static assets, removes external network requests, and reduces
  * **[`<Image>`Component](https://nextjs.org/docs/app/api-reference/components/image):** Optimize images by using the Image Component, which automatically optimizes images, prevents layout shift, and serves them in modern formats like WebP.
  * **[`<Script>`Component](https://nextjs.org/docs/app/guides/scripts):** Optimize third-party scripts by using the Script Component, which automatically defers scripts and prevents them from blocking the main thread.
  * **[ESLint](https://nextjs.org/docs/architecture/accessibility#linting):** Use the built-in `eslint-plugin-jsx-a11y` plugin to catch accessibility issues early.


### Security[](https://nextjs.org/docs/app/guides/production-checklist#security)
  * **[Tainting](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint):** Prevent sensitive data from being exposed to the client by tainting data objects and/or specific values.
  * **[Server Actions](https://nextjs.org/docs/app/getting-started/updating-data):** Ensure users are authorized to call Server Actions. Review the recommended [security practices](https://nextjs.org/blog/security-nextjs-server-components-actions).


  * **[Environment Variables](https://nextjs.org/docs/app/guides/environment-variables):** Ensure your `.env.*` files are added to `.gitignore` and only public variables are prefixed with `NEXT_PUBLIC_`.
  * **[Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy):** Consider adding a Content Security Policy to protect your application against various security threats such as cross-site scripting, clickjacking, and other code injection attacks.


### Metadata and SEO[](https://nextjs.org/docs/app/guides/production-checklist#metadata-and-seo)
  * **[Metadata API](https://nextjs.org/docs/app/getting-started/metadata-and-og-images):** Use the Metadata API to improve your application's Search Engine Optimization (SEO) by adding page titles, descriptions, and more.
  * **[Open Graph (OG) images](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image):** Create OG images to prepare your application for social sharing.
  * **[Sitemaps](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps) and [Robots](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots):** Help Search Engines crawl and index your pages by generating sitemaps and robots files.


### Type safety[](https://nextjs.org/docs/app/guides/production-checklist#type-safety)
  * **TypeScript and[TS Plugin](https://nextjs.org/docs/app/api-reference/config/typescript):** Use TypeScript and the TypeScript plugin for better type-safety, and to help you catch errors early.
