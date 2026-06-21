## Context parameter[](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props#context-parameter)
The `context` parameter is an object containing the following keys:
Name | Description
---|---
`params` | If this page uses a [dynamic route](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes), `params` contains the route parameters. If the page name is `[id].js`, then `params` will look like `{ id: ... }`.
`req` |  `cookies` prop, which is an object with string keys mapping to string values of cookies.
`res` |
`query` | An object representing the query string, including dynamic route parameters.
`preview` | (Deprecated for `draftMode`) `preview` is `true` if the page is in the [Preview Mode](https://nextjs.org/docs/pages/guides/preview-mode) and `false` otherwise.
`previewData` | (Deprecated for `draftMode`) The [preview](https://nextjs.org/docs/pages/guides/preview-mode) data set by `setPreviewData`.
`draftMode` |  `draftMode` is `true` if the page is in the [Draft Mode](https://nextjs.org/docs/pages/guides/draft-mode) and `false` otherwise.
`resolvedUrl` | A normalized version of the request `URL` that strips the `_next/data` prefix for client transitions and includes original query values.
`locale` | Contains the active locale (if enabled).
`locales` | Contains all supported locales (if enabled).
`defaultLocale` | Contains the configured default locale (if enabled).
