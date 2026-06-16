[![](https://vite.dev/assets/footer-background.BIgtbvhx.jpg) ![Vite icon](data:image/svg+xml,%3csvg%20viewBox='0%200%2023%2014'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M20.7482%200H18.8887C21.641%203.93959%2021.6571%2010.0462%2018.8887%2014H20.7482C23.516%2010.0462%2023.4999%203.93959%2020.7482%200Z'%20fill='white'/%3e%3cpath%20d='M2.07027%203.05176e-05C-0.682028%203.93963%20-0.698142%2010.0463%202.07027%2014H3.92985C1.16208%2010.0463%201.1782%203.93963%203.92985%203.05176e-05H2.07027Z'%20fill='white'/%3e%3cpath%20d='M12.0135%2013.6771C11.815%2013.9298%2011.4089%2013.7892%2011.4089%2013.4683V10.3853C11.4089%2010.0114%2011.106%209.70849%2010.7321%209.70849H7.32818C7.05295%209.70849%206.89245%209.39716%207.05295%209.1735L9.29089%206.04026C9.61124%205.59228%209.29089%204.96963%208.73979%204.96963H4.62036C4.34513%204.96963%204.18463%204.65831%204.34512%204.43464L7.24632%200.372579C7.31013%200.283628%207.41262%200.230774%207.52155%200.230774H16.1671C16.4424%200.230774%2016.6029%200.5421%2016.4424%200.765765L14.2044%203.89901C13.8841%204.34698%2014.2044%204.96963%2014.7555%204.96963H18.1595C18.4418%204.96963%2018.6004%205.29514%2018.4257%205.51751L12.0142%2013.6777L12.0135%2013.6771Z'%20fill='white'/%3e%3c/svg%3e)Cloudflare supports Vite's mission ](https://vite.dev/blog/cloudflare-supports-vite)
[Skip to content](https://vite.dev/guide/dep-pre-bundling#VPContent)
[![Vite](https://vite.dev/assets/vite-dark.D2ACe7TL.svg)![Vite](https://vite.dev/assets/vite-light.t8GCa_VF.svg)](https://vite.dev/)
Main Navigation [Guide](https://vite.dev/guide/)[Config](https://vite.dev/config/)[Plugins](https://vite.dev/plugins/)
Resources
[Team](https://vite.dev/team)
[Blog](https://vite.dev/blog)
[Releases](https://vite.dev/releases)
[Acknowledgements](https://vite.dev/acknowledgements)
[Plugin Registry](https://registry.vite.dev/plugins)
[Discord Chat](https://chat.vite.dev)
v8.0.16
[Unreleased Docs](https://main.vite.dev)
[Vite 7 Docs](https://v7.vite.dev)
[Vite 6 Docs](https://v6.vite.dev)
[Vite 5 Docs](https://v5.vite.dev)
[Vite 4 Docs](https://v4.vite.dev)
[Vite 3 Docs](https://v3.vite.dev)
[Vite 2 Docs](https://v2.vite.dev)
Search`⌘``Ctrl``K`
English
[简体中文](https://cn.vite.dev/guide/dep-pre-bundling)
[日本語](https://ja.vite.dev/guide/dep-pre-bundling)
[Español](https://es.vite.dev/guide/dep-pre-bundling)
[Português](https://pt.vite.dev/guide/dep-pre-bundling)
[한국어](https://ko.vite.dev/guide/dep-pre-bundling)
[Deutsch](https://de.vite.dev/guide/dep-pre-bundling)
[فارسی](https://fa.vite.dev/guide/dep-pre-bundling)
Appearance
[](https://chat.vite.dev)
English
[简体中文](https://cn.vite.dev/guide/dep-pre-bundling)
[日本語](https://ja.vite.dev/guide/dep-pre-bundling)
[Español](https://es.vite.dev/guide/dep-pre-bundling)
[Português](https://pt.vite.dev/guide/dep-pre-bundling)
[한국어](https://ko.vite.dev/guide/dep-pre-bundling)
[Deutsch](https://de.vite.dev/guide/dep-pre-bundling)
[فارسی](https://fa.vite.dev/guide/dep-pre-bundling)
[](https://chat.vite.dev)
Menu
On this page
Sidebar Navigation
## Introduction
[Getting Started ](https://vite.dev/guide/)
[Philosophy ](https://vite.dev/guide/philosophy)
[Why Vite ](https://vite.dev/guide/why)
## Guide
[Features ](https://vite.dev/guide/features)
[CLI ](https://vite.dev/guide/cli)
[Using Plugins ](https://vite.dev/guide/using-plugins)
[Dependency Pre-Bundling ](https://vite.dev/guide/dep-pre-bundling)
[Static Asset Handling ](https://vite.dev/guide/assets)
[Building for Production ](https://vite.dev/guide/build)
[Deploying a Static Site ](https://vite.dev/guide/static-deploy)
[Env Variables and Modes ](https://vite.dev/guide/env-and-mode)
[Server-Side Rendering (SSR) ](https://vite.dev/guide/ssr)
[Backend Integration ](https://vite.dev/guide/backend-integration)
[Troubleshooting ](https://vite.dev/guide/troubleshooting)
[Performance ](https://vite.dev/guide/performance)
[Migration from v7 ](https://vite.dev/guide/migration)
[Breaking Changes ](https://vite.dev/changes/)
## APIs
[Plugin API ](https://vite.dev/guide/api-plugin)
[HMR API ](https://vite.dev/guide/api-hmr)
[JavaScript API ](https://vite.dev/guide/api-javascript)
[Config Reference ](https://vite.dev/config/)
## Environment API
[Introduction ](https://vite.dev/guide/api-environment)
[Environment Instances ](https://vite.dev/guide/api-environment-instances)
[Plugins ](https://vite.dev/guide/api-environment-plugins)
[Frameworks ](https://vite.dev/guide/api-environment-frameworks)
[Runtimes ](https://vite.dev/guide/api-environment-runtimes)
On this page
  * [The Why](https://vite.dev/guide/dep-pre-bundling#the-why "The Why")
  * [Automatic Dependency Discovery](https://vite.dev/guide/dep-pre-bundling#automatic-dependency-discovery "Automatic Dependency Discovery")
  * [Monorepos and Linked Dependencies](https://vite.dev/guide/dep-pre-bundling#monorepos-and-linked-dependencies "Monorepos and Linked Dependencies")
  * [Customizing the Behavior](https://vite.dev/guide/dep-pre-bundling#customizing-the-behavior "Customizing the Behavior")
  * [Caching](https://vite.dev/guide/dep-pre-bundling#caching "Caching")
    * [File System Cache](https://vite.dev/guide/dep-pre-bundling#file-system-cache "File System Cache")
    * [Browser Cache](https://vite.dev/guide/dep-pre-bundling#browser-cache "Browser Cache")

Are you an LLM? You can read better optimized documentation at /guide/dep-pre-bundling.md for this page in Markdown format
# Dependency Pre-Bundling [​](https://vite.dev/guide/dep-pre-bundling#dependency-pre-bundling)
When you run `vite` for the first time, Vite prebundles your project dependencies before loading your site locally. It is done automatically and transparently by default.
## The Why [​](https://vite.dev/guide/dep-pre-bundling#the-why)
This is Vite performing what we call "dependency pre-bundling". This process serves two purposes:
  1. **CommonJS and UMD compatibility:** During development, Vite serves all code as native ESM. Therefore, Vite must convert dependencies that are shipped as CommonJS or UMD into ESM first.
When converting CommonJS dependencies, Vite performs smart import analysis so that named imports to CommonJS modules will work as expected even if the exports are dynamically assigned (e.g. React):
js
```
// works as expected
import React, { useState } from 'react'
```

  2. **Performance:** Vite converts ESM dependencies with many internal modules into a single module to improve subsequent page load performance.
Some packages ship their ES modules builds as many separate files importing one another. For example, `import { debounce } from 'lodash-es'`, the browser fires off 600+ HTTP requests at the same time! Even though the server has no problem handling them, the large amount of requests create a network congestion on the browser side, causing the page to load noticeably slower.
By pre-bundling `lodash-es` into a single module, we now only need one HTTP request instead!

NOTE
Dependency pre-bundling only applies in development mode.
## Automatic Dependency Discovery [​](https://vite.dev/guide/dep-pre-bundling#automatic-dependency-discovery)
If an existing cache is not found, Vite will crawl your source code and automatically discover dependency imports (i.e. "bare imports" that expect to be resolved from `node_modules`) and use these found imports as entry points for the pre-bundle. The pre-bundling is performed with
After the server has already started, if a new dependency import is encountered that isn't already in the cache, Vite will re-run the dep bundling process and reload the page if needed.
## Monorepos and Linked Dependencies [​](https://vite.dev/guide/dep-pre-bundling#monorepos-and-linked-dependencies)
In a monorepo setup, a dependency may be a linked package from the same repo. Vite automatically detects dependencies that are not resolved from `node_modules` and treats the linked dep as source code. It will not attempt to bundle the linked dep, and will analyze the linked dep's dependency list instead.
However, this requires the linked dep to be exported as ESM. If not, you can add the dependency to [`optimizeDeps.include`](https://vite.dev/config/dep-optimization-options#optimizedeps-include) in your config.
vite.config.js
js
```
export default

defineConfig

({

optimizeDeps

: {

include

: ['linked-dep'],
  },
})
```

When making changes to the linked dep, restart the dev server with the `--force` command line option for the changes to take effect.
## Customizing the Behavior [​](https://vite.dev/guide/dep-pre-bundling#customizing-the-behavior)
The default dependency discovery heuristics may not always be desirable. In cases where you want to explicitly include/exclude dependencies from the list, use the [`optimizeDeps` config options](https://vite.dev/config/dep-optimization-options).
A typical use case for `optimizeDeps.include` or `optimizeDeps.exclude` is when you have an import that is not directly discoverable in the source code. For example, maybe the import is created as a result of a plugin transform. This means Vite won't be able to discover the import on the initial scan - it can only discover it after the file is requested by the browser and transformed. This will cause the server to immediately re-bundle after server start.
Both `include` and `exclude` can be used to deal with this. If the dependency is large (with many internal modules) or is CommonJS, then you should include it; If the dependency is small and is already valid ESM, you can exclude it and let the browser load it directly.
You can further customize Rolldown too with the [`optimizeDeps.rolldownOptions` option](https://vite.dev/config/dep-optimization-options#optimizedeps-rolldownoptions). For example, adding a Rolldown plugin to handle special files in dependencies or changing the
## Caching [​](https://vite.dev/guide/dep-pre-bundling#caching)
### File System Cache [​](https://vite.dev/guide/dep-pre-bundling#file-system-cache)
Vite caches the pre-bundled dependencies in `node_modules/.vite`. It determines whether it needs to re-run the pre-bundling step based on a few sources:
  * Package manager lockfile content, e.g. `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml` or `bun.lock`.
  * Patches folder modification time.
  * Relevant fields in your `vite.config.js`, if present.
  * `NODE_ENV` value.

The pre-bundling step will only need to be re-run when one of the above has changed.
If for some reason you want to force Vite to re-bundle deps, you can either start the dev server with the `--force` command line option, or manually delete the `node_modules/.vite` cache directory.
### Browser Cache [​](https://vite.dev/guide/dep-pre-bundling#browser-cache)
Resolved dependency requests are strongly cached with HTTP headers `max-age=31536000,immutable` to improve page reload performance during dev. Once cached, these requests will never hit the dev server again. They are auto invalidated by the appended version query if a different version is installed (as reflected in your package manager lockfile). If you want to debug your dependencies by making local edits, you can:
  1. Temporarily disable cache via the Network tab of your browser devtools.
  2. Restart Vite dev server with the `--force` flag to re-bundle the deps.
  3. Reload the page.

Pager
[Previous pageUsing Plugins](https://vite.dev/guide/using-plugins)
[Next pageStatic Asset Handling](https://vite.dev/guide/assets)
© 2019-present VoidZero Inc. and Vite contributors. (012eb452)
