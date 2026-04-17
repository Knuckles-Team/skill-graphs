## Async Request APIs (Breaking change)[](https://nextjs.org/docs/app/guides/upgrading/version-16#async-request-apis-breaking-change)
Version 15 introduced [Async Request APIs](https://nextjs.org/docs/app/guides/upgrading/version-15#async-request-apis-breaking-change) as a breaking change, with **temporary** synchronous compatibility.
Starting with **Next.js 16** , synchronous access is fully removed. These APIs can only be accessed asynchronously.
  * [`cookies`](https://nextjs.org/docs/app/api-reference/functions/cookies)
  * [`headers`](https://nextjs.org/docs/app/api-reference/functions/headers)
  * [`draftMode`](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
  * `params` in [`layout.js`](https://nextjs.org/docs/app/api-reference/file-conventions/layout), [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page), [`route.js`](https://nextjs.org/docs/app/api-reference/file-conventions/route), [`default.js`](https://nextjs.org/docs/app/api-reference/file-conventions/default), [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image), [`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image), [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon), and [`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon).
  * `searchParams` in [`page.js`](https://nextjs.org/docs/app/api-reference/file-conventions/page)


Use the [codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#migrate-to-async-dynamic-apis) to migrate to async Dynamic APIs.
### Migrating types for async Dynamic APIs[](https://nextjs.org/docs/app/guides/upgrading/version-16#migrating-types-for-async-dynamic-apis)
To help migrate to async `params` and `searchParams`, you can run [`npx next typegen`](https://nextjs.org/docs/app/api-reference/cli/next#next-typegen-options) to automatically generate these globally available types helpers:
  * [`PageProps`](https://nextjs.org/docs/app/api-reference/file-conventions/page#page-props-helper)
  * [`LayoutProps`](https://nextjs.org/docs/app/api-reference/file-conventions/layout#layout-props-helper)
  * [`RouteContext`](https://nextjs.org/docs/app/api-reference/file-conventions/route#route-context-helper)


> **Good to know** : `typegen` was introduced in Next.js 15.5
This simplifies type-safe migration to the new async API pattern, and enables you to update your components with full type safety, for example:
/app/blog/[slug]/page.tsx
```
export default async function Page(props: PageProps<'/blog/[slug]'>) {
  const { slug } = await props.params
  const query = await props.searchParams
  return <h1>Blog Post: {slug}</h1>
}
```

This approach gives you fully type-safe access to `props.params`, including the `slug`, and to `searchParams`, directly within your page.
