## Breaking Changes[](https://nextjs.org/docs/pages/guides/upgrading/version-9#breaking-changes)
###  `@zeit/next-typescript` is no longer necessary[](https://nextjs.org/docs/pages/guides/upgrading/version-9#zeitnext-typescript-is-no-longer-necessary)
Next.js will now ignore usage `@zeit/next-typescript` and warn you to remove it. Please remove this plugin from your `next.config.js`.
Remove references to `@zeit/next-typescript/babel` from your custom `.babelrc` (if present).
The usage of `next.config.js`.
TypeScript Definitions are published with the `next` package, so you need to uninstall `@types/next` as they would conflict.
The following types are different:
> This list was created by the community to help you upgrade, if you find other differences please send a pull-request to this list to help other users.
From:
```
import { NextContext } from 'next'
import { NextAppContext, DefaultAppIProps } from 'next/app'
import { NextDocumentContext, DefaultDocumentIProps } from 'next/document'
```

to
```
import { NextPageContext } from 'next'
import { AppContext, AppInitialProps } from 'next/app'
import { DocumentContext, DocumentInitialProps } from 'next/document'
```

### The `config` key is now an export on a page[](https://nextjs.org/docs/pages/guides/upgrading/version-9#the-config-key-is-now-an-export-on-a-page)
You may no longer export a custom variable named `config` from a page (i.e. `export { config }` / `export const config ...`). This exported variable is now used to specify page-level Next.js configuration like Opt-in AMP and API Route features.
You must rename a non-Next.js-purposed `config` export to something different.
###  `next/dynamic` no longer renders "loading..." by default while loading[](https://nextjs.org/docs/pages/guides/upgrading/version-9#nextdynamic-no-longer-renders-loading-by-default-while-loading)
Dynamic components will not render anything by default while loading. You can still customize this behavior by setting the `loading` property:
```
import dynamic from 'next/dynamic'

const DynamicComponentWithCustomLoading = dynamic(
  () => import('../components/hello2'),
  {
    loading: () => <p>Loading</p>,
  }
)
```

###  `withAmp` has been removed in favor of an exported configuration object[](https://nextjs.org/docs/pages/guides/upgrading/version-9#withamp-has-been-removed-in-favor-of-an-exported-configuration-object)
Next.js now has the concept of page-level configuration, so the `withAmp` higher-order component has been removed for consistency.
This change can be **automatically migrated by running the following commands in the root of your Next.js project:**
Terminal
```
curl -L https://github.com/vercel/next-codemod/archive/master.tar.gz | tar -xz --strip=2 next-codemod-master/transforms/withamp-to-config.js npx jscodeshift -t ./withamp-to-config.js pages/**/*.js
```

To perform this migration by hand, or view what the codemod will produce, see below:
**Before**
```
import { withAmp } from 'next/amp'

function Home() {
  return <h1>My AMP Page</h1>
}

export default withAmp(Home)
// or
export default withAmp(Home, { hybrid: true })
```

**After**
```
export default function Home() {
  return <h1>My AMP Page</h1>
}

export const config = {
  amp: true,
  // or
  amp: 'hybrid',
}
```

###  `next export` no longer exports pages as `index.html`[](https://nextjs.org/docs/pages/guides/upgrading/version-9#next-export-no-longer-exports-pages-as-indexhtml)
Previously, exporting `pages/about.js` would result in `out/about/index.html`. This behavior has been changed to result in `out/about.html`.
You can revert to the previous behavior by creating a `next.config.js` with the following content:
next.config.js
```
module.exports = {
  trailingSlash: true,
}
```

###  `pages/api/` is treated differently[](https://nextjs.org/docs/pages/guides/upgrading/version-9#pagesapi-is-treated-differently)
Pages in `pages/api/` are now considered [API Routes](https://nextjs.org/blog/next-9#api-routes). Pages in this directory will no longer contain a client-side bundle.
