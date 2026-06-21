## Reference[](https://nextjs.org/docs/pages/api-reference/config/eslint#reference)
The `eslint-config-next` package includes the `recommended` rule-sets from the following ESLint plugins:
### Rules[](https://nextjs.org/docs/pages/api-reference/config/eslint#rules)
The `@next/eslint-plugin-next` rules included are:
Enabled in recommended config | Rule | Description
---|---|---
| [@next/next/google-font-display](https://nextjs.org/docs/messages/google-font-display) | Enforce font-display behavior with Google Fonts.
| [@next/next/google-font-preconnect](https://nextjs.org/docs/messages/google-font-preconnect) | Ensure `preconnect` is used with Google Fonts.
| [@next/next/inline-script-id](https://nextjs.org/docs/messages/inline-script-id) | Enforce `id` attribute on `next/script` components with inline content.
| [@next/next/next-script-for-ga](https://nextjs.org/docs/messages/next-script-for-ga) | Prefer `next/script` component when using the inline script for Google Analytics.
| [@next/next/no-assign-module-variable](https://nextjs.org/docs/messages/no-assign-module-variable) | Prevent assignment to the `module` variable.
| [@next/next/no-async-client-component](https://nextjs.org/docs/messages/no-async-client-component) | Prevent Client Components from being async functions.
| [@next/next/no-before-interactive-script-outside-document](https://nextjs.org/docs/messages/no-before-interactive-script-outside-document) | Prevent usage of `next/script`'s `beforeInteractive` strategy outside of `pages/_document.js`.
| [@next/next/no-css-tags](https://nextjs.org/docs/messages/no-css-tags) | Prevent manual stylesheet tags.
| [@next/next/no-document-import-in-page](https://nextjs.org/docs/messages/no-document-import-in-page) | Prevent importing `next/document` outside of `pages/_document.js`.
| [@next/next/no-duplicate-head](https://nextjs.org/docs/messages/no-duplicate-head) | Prevent duplicate usage of `<Head>` in `pages/_document.js`.
| [@next/next/no-head-element](https://nextjs.org/docs/messages/no-head-element) | Prevent usage of `<head>` element.
| [@next/next/no-head-import-in-document](https://nextjs.org/docs/messages/no-head-import-in-document) | Prevent usage of `next/head` in `pages/_document.js`.
| [@next/next/no-html-link-for-pages](https://nextjs.org/docs/messages/no-html-link-for-pages) | Prevent usage of `<a>` elements to navigate to internal Next.js pages.
| [@next/next/no-img-element](https://nextjs.org/docs/messages/no-img-element) | Prevent usage of `<img>` element due to slower LCP and higher bandwidth.
| [@next/next/no-page-custom-font](https://nextjs.org/docs/messages/no-page-custom-font) | Prevent page-only custom fonts.
| [@next/next/no-script-component-in-head](https://nextjs.org/docs/messages/no-script-component-in-head) | Prevent usage of `next/script` in `next/head` component.
| [@next/next/no-styled-jsx-in-document](https://nextjs.org/docs/messages/no-styled-jsx-in-document) | Prevent usage of `styled-jsx` in `pages/_document.js`.
| [@next/next/no-sync-scripts](https://nextjs.org/docs/messages/no-sync-scripts) | Prevent synchronous scripts.
| [@next/next/no-title-in-document-head](https://nextjs.org/docs/messages/no-title-in-document-head) | Prevent usage of `<title>` with `Head` component from `next/document`.
| @next/next/no-typos | Prevent common typos in [Next.js's data fetching functions](https://nextjs.org/docs/pages/building-your-application/data-fetching)
| [@next/next/no-unwanted-polyfillio](https://nextjs.org/docs/messages/no-unwanted-polyfillio) | Prevent duplicate polyfills from Polyfill.io.
We recommend using an appropriate
`next lint` removal
Starting with Next.js 16, `next lint` is removed.
As part of the removal, the `eslint` option in your Next config file is no longer needed and can be safely removed.
