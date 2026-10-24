## Possible Ways to Fix It[](https://nextjs.org/docs/messages/no-html-link-for-pages#possible-ways-to-fix-it)
Make sure to import the `Link` component and wrap anchor elements that route to different page routes.
**Before:**
pages/index.js
```
function Home() {
  return (
    <div>
      <a href="/about">About Us</a>
    </div>
  )
}
```

**After:**
pages/index.js
```
import Link from 'next/link'

function Home() {
  return (
    <div>
      <Link href="/about">About Us</Link>
    </div>
  )
}

export default Home
```

### Options[](https://nextjs.org/docs/messages/no-html-link-for-pages#options)
####  `pagesDir`[](https://nextjs.org/docs/messages/no-html-link-for-pages#pagesdir)
This rule can normally locate your `pages` directory automatically.
If you're working in a monorepo, we recommend configuring the [`rootDir`](https://nextjs.org/docs/pages/api-reference/config/eslint#specifying-a-root-directory-within-a-monorepo) setting in `eslint-plugin-next`, which `pagesDir` will use to locate your `pages` directory.
In some cases, you may also need to configure this rule directly by providing a `pages` directory. This can be a path or an array of paths.
eslint.config.json
```
{
  "rules": {
    "@next/next/no-html-link-for-pages": ["error", "packages/my-app/pages/"]
  }
}
```
