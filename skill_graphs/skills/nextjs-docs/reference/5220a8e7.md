## During development[](https://nextjs.org/docs/pages/guides/production-checklist#during-development)
While building your application, we recommend using the following features to ensure the best performance and user experience:
### Routing and rendering[](https://nextjs.org/docs/pages/guides/production-checklist#routing-and-rendering)
  * **[`<Link>`component](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating):** Use the `<Link>` component for client-side navigation and prefetching.
  * **[Custom Errors](https://nextjs.org/docs/pages/building-your-application/routing/custom-error):** Gracefully handle [500](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#500-page) and [404 errors](https://nextjs.org/docs/pages/building-your-application/routing/custom-error#404-page)


### Data fetching and caching[](https://nextjs.org/docs/pages/guides/production-checklist#data-fetching-and-caching)
  * **[API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes):** Use Route Handlers to access your backend resources, and prevent sensitive secrets from being exposed to the client.
  * **[Data Caching](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props):** Verify whether your data requests are being cached or not, and opt into caching, where appropriate. Ensure requests that don't use `getStaticProps` are cached where appropriate.
  * **[Incremental Static Regeneration](https://nextjs.org/docs/pages/guides/incremental-static-regeneration):** Use Incremental Static Regeneration to update static pages after they've been built, without rebuilding your entire site.
  * **[Static Images](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder):** Use the `public` directory to automatically cache your application's static assets, e.g. images.


### UI and accessibility[](https://nextjs.org/docs/pages/guides/production-checklist#ui-and-accessibility)
  * **[Font Module](https://nextjs.org/docs/app/api-reference/components/font):** Optimize fonts by using the Font Module, which automatically hosts your font files with other static assets, removes external network requests, and reduces
  * **[`<Image>`Component](https://nextjs.org/docs/app/api-reference/components/image):** Optimize images by using the Image Component, which automatically optimizes images, prevents layout shift, and serves them in modern formats like WebP.
  * **[`<Script>`Component](https://nextjs.org/docs/app/guides/scripts):** Optimize third-party scripts by using the Script Component, which automatically defers scripts and prevents them from blocking the main thread.
  * **[ESLint](https://nextjs.org/docs/architecture/accessibility#linting):** Use the built-in `eslint-plugin-jsx-a11y` plugin to catch accessibility issues early.


### Security[](https://nextjs.org/docs/pages/guides/production-checklist#security)
  * **[Environment Variables](https://nextjs.org/docs/app/guides/environment-variables):** Ensure your `.env.*` files are added to `.gitignore` and only public variables are prefixed with `NEXT_PUBLIC_`.
  * **[Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy):** Consider adding a Content Security Policy to protect your application against various security threats such as cross-site scripting, clickjacking, and other code injection attacks.


### Metadata and SEO[](https://nextjs.org/docs/pages/guides/production-checklist#metadata-and-seo)
  * **[`<Head>`Component](https://nextjs.org/docs/pages/api-reference/components/head):** Use the `next/head` component to add page titles, descriptions, and more.


### Type safety[](https://nextjs.org/docs/pages/guides/production-checklist#type-safety)
  * **TypeScript and[TS Plugin](https://nextjs.org/docs/app/api-reference/config/typescript):** Use TypeScript and the TypeScript plugin for better type-safety, and to help you catch errors early.
