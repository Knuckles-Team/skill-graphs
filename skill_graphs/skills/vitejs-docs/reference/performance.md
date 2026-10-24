[![](https://vite.dev/assets/footer-background.BIgtbvhx.jpg) ![Vite icon](data:image/svg+xml,%3csvg%20viewBox='0%200%2023%2014'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M20.7482%200H18.8887C21.641%203.93959%2021.6571%2010.0462%2018.8887%2014H20.7482C23.516%2010.0462%2023.4999%203.93959%2020.7482%200Z'%20fill='white'/%3e%3cpath%20d='M2.07027%203.05176e-05C-0.682028%203.93963%20-0.698142%2010.0463%202.07027%2014H3.92985C1.16208%2010.0463%201.1782%203.93963%203.92985%203.05176e-05H2.07027Z'%20fill='white'/%3e%3cpath%20d='M12.0135%2013.6771C11.815%2013.9298%2011.4089%2013.7892%2011.4089%2013.4683V10.3853C11.4089%2010.0114%2011.106%209.70849%2010.7321%209.70849H7.32818C7.05295%209.70849%206.89245%209.39716%207.05295%209.1735L9.29089%206.04026C9.61124%205.59228%209.29089%204.96963%208.73979%204.96963H4.62036C4.34513%204.96963%204.18463%204.65831%204.34512%204.43464L7.24632%200.372579C7.31013%200.283628%207.41262%200.230774%207.52155%200.230774H16.1671C16.4424%200.230774%2016.6029%200.5421%2016.4424%200.765765L14.2044%203.89901C13.8841%204.34698%2014.2044%204.96963%2014.7555%204.96963H18.1595C18.4418%204.96963%2018.6004%205.29514%2018.4257%205.51751L12.0142%2013.6777L12.0135%2013.6771Z'%20fill='white'/%3e%3c/svg%3e)Cloudflare supports Vite's mission ](https://vite.dev/blog/cloudflare-supports-vite)
[Skip to content](https://vite.dev/guide/performance#VPContent)
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
[简体中文](https://cn.vite.dev/guide/performance)
[日本語](https://ja.vite.dev/guide/performance)
[Español](https://es.vite.dev/guide/performance)
[Português](https://pt.vite.dev/guide/performance)
[한국어](https://ko.vite.dev/guide/performance)
[Deutsch](https://de.vite.dev/guide/performance)
[فارسی](https://fa.vite.dev/guide/performance)
Appearance
[](https://chat.vite.dev)
English
[简体中文](https://cn.vite.dev/guide/performance)
[日本語](https://ja.vite.dev/guide/performance)
[Español](https://es.vite.dev/guide/performance)
[Português](https://pt.vite.dev/guide/performance)
[한국어](https://ko.vite.dev/guide/performance)
[Deutsch](https://de.vite.dev/guide/performance)
[فارسی](https://fa.vite.dev/guide/performance)
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
  * [Review Your Browser Setup](https://vite.dev/guide/performance#review-your-browser-setup "Review Your Browser Setup")
  * [Audit Configured Vite Plugins](https://vite.dev/guide/performance#audit-configured-vite-plugins "Audit Configured Vite Plugins")
  * [Reduce Resolve Operations](https://vite.dev/guide/performance#reduce-resolve-operations "Reduce Resolve Operations")
  * [Avoid Barrel Files](https://vite.dev/guide/performance#avoid-barrel-files "Avoid Barrel Files")
  * [Warm Up Frequently Used Files](https://vite.dev/guide/performance#warm-up-frequently-used-files "Warm Up Frequently Used Files")
  * [Use Lesser or Native Tooling](https://vite.dev/guide/performance#use-lesser-or-native-tooling "Use Lesser or Native Tooling")

Are you an LLM? You can read better optimized documentation at /guide/performance.md for this page in Markdown format
# Performance [​](https://vite.dev/guide/performance#performance)
While Vite is fast by default, performance issues can creep in as the project's requirements grow. This guide aims to help you identify and fix common performance issues, such as:
  * Slow server starts
  * Slow page loads
  * Slow builds

## Review Your Browser Setup [​](https://vite.dev/guide/performance#review-your-browser-setup)
Some browser extensions may interfere with requests and slow down startup and reload times for large apps, especially when using browser dev tools. We recommend creating a dev-only profile without extensions, or switch to incognito mode, while using Vite's dev server in these cases. Incognito mode should also be faster than a regular profile without extensions.
The Vite dev server does hard caching of pre-bundled dependencies and implements fast 304 responses for source code. Disabling the cache while the Browser Dev Tools are open can have a big impact on startup and full-page reload times. Please check that "Disable Cache" isn't enabled while you work with the Vite server.
## Audit Configured Vite Plugins [​](https://vite.dev/guide/performance#audit-configured-vite-plugins)
Vite's internal and official plugins are optimized to do the least amount of work possible while providing compatibility with the broader ecosystem. For example, code transformations use regex in dev, but do a complete parse in build to ensure correctness.
However, the performance of community plugins is out of Vite's control, which may affect the developer experience. Here are a few things you can look out for when using additional Vite plugins:
  1. Large dependencies that are only used in certain cases should be dynamically imported to reduce the Node.js startup time. Example refactors:
  2. The `buildStart`, `config`, and `configResolved` hooks should not run long and extensive operations. These hooks are awaited during dev server startup, which delays when you can access the site in the browser.
  3. The `resolveId`, `load`, and `transform` hooks may cause some files to load slower than others. While sometimes unavoidable, it's still worth checking for possible areas to optimize. For example, checking if the `code` contains a specific keyword, or the `id` matches a specific extension, before doing the full transformation.
The longer it takes to transform a file, the more significant the request waterfall will be when loading the site in the browser.
You can inspect the duration it takes to transform a file using `vite --debug plugin-transform` or

Profiling
You can run `vite --profile`, visit the site, and press `p + enter` in your terminal to record a `.cpuprofile`. A tool like [share the profiles](https://chat.vite.dev) with the Vite team to help us identify performance issues.
## Reduce Resolve Operations [​](https://vite.dev/guide/performance#reduce-resolve-operations)
Resolving import paths can be an expensive operation when hitting its worst case often. For example, Vite supports "guessing" import paths with the [`resolve.extensions`](https://vite.dev/config/shared-options#resolve-extensions) option, which defaults to `['.mjs', '.js', '.mts', '.ts', '.jsx', '.tsx', '.json']`.
When you try to import `./Component.jsx` with `import './Component'`, Vite will run these steps to resolve it:
  1. Check if `./Component` exists, no.
  2. Check if `./Component.mjs` exists, no.
  3. Check if `./Component.js` exists, no.
  4. Check if `./Component.mts` exists, no.
  5. Check if `./Component.ts` exists, no.
  6. Check if `./Component.jsx` exists, yes!

As shown, a total of 6 filesystem checks is required to resolve an import path. The more implicit imports you have, the more time it adds up to resolve the paths.
Hence, it's usually better to be explicit with your import paths, e.g. `import './Component.jsx'`. You can also narrow down the list for `resolve.extensions` to reduce the general filesystem checks, but you have to make sure it works for files in `node_modules` too.
If you're a plugin author, make sure to only call
TypeScript
If you are using TypeScript, enable `"moduleResolution": "bundler"` and `"allowImportingTsExtensions": true` in your `tsconfig.json`'s `compilerOptions` to use `.ts` and `.tsx` extensions directly in your code.
## Avoid Barrel Files [​](https://vite.dev/guide/performance#avoid-barrel-files)
Barrel files are files that re-export the APIs of other files in the same directory. For example:
src/utils/index.js
js
```
export * from './color.js'
export * from './dom.js'
export * from './slash.js'
```

When you only import an individual API, e.g. `import { slash } from './utils'`, all the files in that barrel file need to be fetched and transformed as they may contain the `slash` API and may also contain side-effects that run on initialization. This means you're loading more files than required on the initial page load, resulting in a slower page load.
If possible, you should avoid barrel files and import the individual APIs directly, e.g. `import { slash } from './utils/slash.js'`. You can read
## Warm Up Frequently Used Files [​](https://vite.dev/guide/performance#warm-up-frequently-used-files)
The Vite dev server only transforms files as requested by the browser, which allows it to start up quickly and only apply transformations for used files. It can also pre-transform files if it anticipates certain files will be requested shortly. However, request waterfalls may still happen if some files take longer to transform than others. For example:
Given an import graph where the left file imports the right file:

```
main.js -> BigComponent.vue -> big-utils.js -> large-data.json
```

The import relationship can only be known after the file is transformed. If `BigComponent.vue` takes some time to transform, `big-utils.js` has to wait for its turn, and so on. This causes an internal waterfall even with pre-transformation built-in.
Vite allows you to warm up files that you know are frequently used, e.g. `big-utils.js`, using the [`server.warmup`](https://vite.dev/config/server-options#server-warmup) option. This way `big-utils.js` will be ready and cached to be served immediately when requested.
You can find files that are frequently used by running `vite --debug transform` and inspect the logs:
bash
```
vite:transform 28.72ms /@vite/client +1ms
vite:transform 62.95ms /src/components/BigComponent.vue +1ms
vite:transform 102.54ms /src/utils/big-utils.js +1ms
```

vite.config.js
js
```
export default defineConfig({
  server: {
    warmup: {
      clientFiles: [
        './src/components/BigComponent.vue',
        './src/utils/big-utils.js',
      ],
    },
  },
})
```

Note that you should only warm up files that are frequently used to not overload the Vite dev server on startup. Check the [`server.warmup`](https://vite.dev/config/server-options#server-warmup) option for more information.
Using [`--open` or `server.open`](https://vite.dev/config/server-options#server-open) also provides a performance boost, as Vite will automatically warm up the entry point of your app or the provided URL to open.
## Use Lesser or Native Tooling [​](https://vite.dev/guide/performance#use-lesser-or-native-tooling)
Keeping Vite fast with a growing codebase is about reducing the amount of work for the source files (JS/TS/CSS).
Examples of doing less work:
  * Use CSS instead of Sass/Less/Stylus when possible (nesting can be handled by PostCSS / Lightning CSS)
  * Don't transform SVGs into UI framework components (React, Vue, etc.). Import them as strings or URLs instead.

Examples of using native tooling:
While Vite core is based on native tooling, some features still use non-native tooling by default to provide better compatibility and feature set. But it may be worth the cost for larger applications.
  * Try out the experimental support for

Pager
[Previous pageTroubleshooting](https://vite.dev/guide/troubleshooting)
[Next pageMigration from v7](https://vite.dev/guide/migration)
© 2019-present VoidZero Inc. and Vite contributors. (012eb452)
