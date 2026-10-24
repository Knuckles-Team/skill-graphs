## Known gaps with webpack[](https://nextjs.org/docs/pages/api-reference/turbopack#known-gaps-with-webpack)
There are a number of non-trivial behavior differences between webpack and Turbopack that are important to be aware of when migrating an application. Generally, these are less of a concern for new applications.
### Filesystem Root[](https://nextjs.org/docs/pages/api-reference/turbopack#filesystem-root)
Turbopack uses the root directory to resolve modules. Files outside of the project root are not resolved.
For example, when linking dependencies outside the project root (via `npm link`, `yarn link`, `pnpm link`, etc.), those linked files will not be resolved by default. To resolve these files, you must configure the root option to the parent directory of both the project and the linked dependencies.
You can configure the filesystem root using [turbopack.root](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#root-directory) option in `next.config.js`.
### CSS Module Ordering[](https://nextjs.org/docs/pages/api-reference/turbopack#css-module-ordering)
Turbopack will follow JS import order to order [CSS modules](https://nextjs.org/docs/app/getting-started/css#css-modules) which are not otherwise ordered. For example:
components/BlogPost.jsx
```
import utilStyles from './utils.module.css'
import buttonStyles from './button.module.css'
export default function BlogPost() {
  return (
    <div className={utilStyles.container}>
      <button className={buttonStyles.primary}>Click me</button>
    </div>
  )
}
```

In this example, Turbopack will ensure that `utils.module.css` will appear before `button.module.css` in the produced CSS chunk, following the import order
Webpack generally does this as well, but there are cases where it will ignore JS inferred ordering, for example if it infers the JS file is side-effect-free.
This can lead to subtle rendering changes when adopting Turbopack, if applications have come to rely on an arbitrary ordering. Generally, the solution is easy, e.g. have `button.module.css` `@import utils.module.css` to force the ordering, or identify the conflicting rules and change them to not target the same properties.
### Sass node_modules imports[](https://nextjs.org/docs/pages/api-reference/turbopack#sass-node_modules-imports)
Turbopack supports importing `node_modules` Sass files out of the box. Webpack supports a legacy tilde `~` syntax for this, which is not supported by Turbopack.
From:
styles/globals.scss
```
@import '~bootstrap/dist/css/bootstrap.min.css';
```

To:
styles/globals.scss
```
@import 'bootstrap/dist/css/bootstrap.min.css';
```

If you can't update the imports, you can add a `turbopack.resolveAlias` configuration to map the `~` syntax to the actual path:
next.config.js
```
module.exports = {
  turbopack: {
    resolveAlias: {
      '~*': '*',
    },
  },
}
```

### Build Caching[](https://nextjs.org/docs/pages/api-reference/turbopack#build-caching)
Webpack supports
  * [`experimental.turbopackFileSystemCacheForDev`](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache) is enabled by default
  * [`experimental.turbopackFileSystemCacheForBuild`](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache) is currently opt-in


> **Good to know:** For this reason, when comparing webpack and Turbopack performance, make sure to delete the `.next` folder between builds to see a fair cold build comparison or enable the turbopack filesystem cache feature to compare warm builds.
### Webpack plugins[](https://nextjs.org/docs/pages/api-reference/turbopack#webpack-plugins)
Turbopack does not support webpack plugins. This affects third-party tools that rely on webpack's plugin system for integration. We do support [webpack loaders](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#configuring-webpack-loaders). If you depend on webpack plugins, you'll need to find Turbopack-compatible alternatives or continue using webpack until equivalent functionality is available.
