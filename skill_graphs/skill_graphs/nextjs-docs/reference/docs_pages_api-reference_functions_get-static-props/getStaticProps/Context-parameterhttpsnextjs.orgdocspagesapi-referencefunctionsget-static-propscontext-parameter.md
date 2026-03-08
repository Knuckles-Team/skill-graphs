## Context parameter[](https://nextjs.org/docs/pages/api-reference/functions/get-static-props#context-parameter)
The `context` parameter is an object containing the following keys:
Name | Description
---|---
`params` | Contains the route parameters for pages using [dynamic routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes). For example, if the page name is `[id].js`, then `params` will look like `{ id: ... }`. You should use this together with `getStaticPaths`, which we'll explain later.
`preview` | (Deprecated for `draftMode`) `preview` is `true` if the page is in the [Preview Mode](https://nextjs.org/docs/pages/guides/preview-mode) and `false` otherwise.
`previewData` | (Deprecated for `draftMode`) The [preview](https://nextjs.org/docs/pages/guides/preview-mode) data set by `setPreviewData`.
`draftMode` |  `draftMode` is `true` if the page is in the [Draft Mode](https://nextjs.org/docs/pages/guides/draft-mode) and `false` otherwise.
`locale` | Contains the active locale (if enabled).
`locales` | Contains all supported locales (if enabled).
`defaultLocale` | Contains the configured default locale (if enabled).
`revalidateReason` | Provides a reason for why the function was called. Can be one of: "build" (run at build time), "stale" (revalidate period expired, or running in [development mode](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props#runs-on-every-request-in-development)), "on-demand" (triggered via [on-demand revalidation](https://nextjs.org/docs/pages/guides/incremental-static-regeneration#on-demand-revalidation-with-revalidatepath))
