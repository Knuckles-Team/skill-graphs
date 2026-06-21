## Upgrading New Features[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#upgrading-new-features)
Next.js 13 introduced the new [App Router](https://nextjs.org/docs/app) with new features and conventions. The new Router is available in the `app` directory and co-exists with the `pages` directory.
Upgrading to Next.js 13 does **not** require using the App Router. You can continue using `pages` with new features that work in both directories, such as the updated [Image component](https://nextjs.org/docs/app/guides/migrating/app-router-migration#image-component), [Link component](https://nextjs.org/docs/app/guides/migrating/app-router-migration#link-component), [Script component](https://nextjs.org/docs/app/guides/migrating/app-router-migration#script-component), and [Font optimization](https://nextjs.org/docs/app/guides/migrating/app-router-migration#font-optimization).
###  `<Image/>` Component[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#image-component)
Next.js 12 introduced new improvements to the Image Component with a temporary import: `next/future/image`. These improvements included less client-side JavaScript, easier ways to extend and style images, better accessibility, and native browser lazy loading.
In version 13, this new behavior is now the default for `next/image`.
There are two codemods to help you migrate to the new Image Component:
  * [**`next-image-to-legacy-image`codemod**](https://nextjs.org/docs/app/guides/upgrading/codemods#next-image-to-legacy-image): Safely and automatically renames `next/image` imports to `next/legacy/image`. Existing components will maintain the same behavior.
  * [**`next-image-experimental`codemod**](https://nextjs.org/docs/app/guides/upgrading/codemods#next-image-experimental): Dangerously adds inline styles and removes unused props. This will change the behavior of existing components to match the new defaults. To use this codemod, you need to run the `next-image-to-legacy-image` codemod first.


###  `<Link>` Component[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#link-component)
The [`<Link>` Component](https://nextjs.org/docs/app/api-reference/components/link) no longer requires manually adding an `<a>` tag as a child. This behavior was added as an experimental option in [version 12.2](https://nextjs.org/blog/next-12-2) and is now the default. In Next.js 13, `<Link>` always renders `<a>` and allows you to forward props to the underlying tag.
For example:
```
import Link from 'next/link'

// Next.js 12: `<a>` has to be nested otherwise it's excluded
<Link href="/about">
  <a>About</a>
</Link>

// Next.js 13: `<Link>` always renders `<a>` under the hood
<Link href="/about">
  About
</Link>
```

To upgrade your links to Next.js 13, you can use the [`new-link` codemod](https://nextjs.org/docs/app/guides/upgrading/codemods#new-link).
###  `<Script>` Component[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#script-component)
The behavior of [`next/script`](https://nextjs.org/docs/app/api-reference/components/script) has been updated to support both `pages` and `app`, but some changes need to be made to ensure a smooth migration:
  * Move any `beforeInteractive` scripts you previously included in `_document.js` to the root layout file (`app/layout.tsx`).
  * The experimental `worker` strategy does not yet work in `app` and scripts denoted with this strategy will either have to be removed or modified to use a different strategy (e.g. `lazyOnload`).
  * `onLoad`, `onReady`, and `onError` handlers will not work in Server Components so make sure to move them to a [Client Component](https://nextjs.org/docs/app/getting-started/server-and-client-components) or remove them altogether.


### Font Optimization[](https://nextjs.org/docs/app/guides/migrating/app-router-migration#font-optimization)
Previously, Next.js helped you optimize fonts by [inlining font CSS](https://nextjs.org/docs/app/api-reference/components/font). Version 13 introduces the new [`next/font`](https://nextjs.org/docs/app/api-reference/components/font) module which gives you the ability to customize your font loading experience while still ensuring great performance and privacy. `next/font` is supported in both the `pages` and `app` directories.
While [inlining CSS](https://nextjs.org/docs/app/api-reference/components/font) still works in `pages`, it does not work in `app`. You should use [`next/font`](https://nextjs.org/docs/app/api-reference/components/font) instead.
See the [Font Optimization](https://nextjs.org/docs/app/api-reference/components/font) page to learn how to use `next/font`.
