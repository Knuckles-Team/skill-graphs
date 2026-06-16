[![](https://vite.dev/assets/footer-background.BIgtbvhx.jpg) ![Vite icon](data:image/svg+xml,%3csvg%20viewBox='0%200%2023%2014'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M20.7482%200H18.8887C21.641%203.93959%2021.6571%2010.0462%2018.8887%2014H20.7482C23.516%2010.0462%2023.4999%203.93959%2020.7482%200Z'%20fill='white'/%3e%3cpath%20d='M2.07027%203.05176e-05C-0.682028%203.93963%20-0.698142%2010.0463%202.07027%2014H3.92985C1.16208%2010.0463%201.1782%203.93963%203.92985%203.05176e-05H2.07027Z'%20fill='white'/%3e%3cpath%20d='M12.0135%2013.6771C11.815%2013.9298%2011.4089%2013.7892%2011.4089%2013.4683V10.3853C11.4089%2010.0114%2011.106%209.70849%2010.7321%209.70849H7.32818C7.05295%209.70849%206.89245%209.39716%207.05295%209.1735L9.29089%206.04026C9.61124%205.59228%209.29089%204.96963%208.73979%204.96963H4.62036C4.34513%204.96963%204.18463%204.65831%204.34512%204.43464L7.24632%200.372579C7.31013%200.283628%207.41262%200.230774%207.52155%200.230774H16.1671C16.4424%200.230774%2016.6029%200.5421%2016.4424%200.765765L14.2044%203.89901C13.8841%204.34698%2014.2044%204.96963%2014.7555%204.96963H18.1595C18.4418%204.96963%2018.6004%205.29514%2018.4257%205.51751L12.0142%2013.6777L12.0135%2013.6771Z'%20fill='white'/%3e%3c/svg%3e)Cloudflare supports Vite's mission ](https://vite.dev/blog/cloudflare-supports-vite)
[Skip to content](https://vite.dev/guide/migration#VPContent)
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
[简体中文](https://cn.vite.dev/guide/migration)
[日本語](https://ja.vite.dev/guide/migration)
[Español](https://es.vite.dev/guide/migration)
[Português](https://pt.vite.dev/guide/migration)
[한국어](https://ko.vite.dev/guide/migration)
[Deutsch](https://de.vite.dev/guide/migration)
[فارسی](https://fa.vite.dev/guide/migration)
Appearance
[](https://chat.vite.dev)
English
[简体中文](https://cn.vite.dev/guide/migration)
[日本語](https://ja.vite.dev/guide/migration)
[Español](https://es.vite.dev/guide/migration)
[Português](https://pt.vite.dev/guide/migration)
[한국어](https://ko.vite.dev/guide/migration)
[Deutsch](https://de.vite.dev/guide/migration)
[فارسی](https://fa.vite.dev/guide/migration)
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
  * [Default Browser Target Change NRV](https://vite.dev/guide/migration#default-browser-target-change "Default Browser Target Change NRV")
  * [Rolldown](https://vite.dev/guide/migration#rolldown "Rolldown")
    * [Gradual Migration](https://vite.dev/guide/migration#gradual-migration "Gradual Migration")
    * [Dependency Optimizer Now Uses Rolldown](https://vite.dev/guide/migration#dependency-optimizer-now-uses-rolldown "Dependency Optimizer Now Uses Rolldown")
    * [JavaScript Transforms by Oxc](https://vite.dev/guide/migration#javascript-transforms-by-oxc "JavaScript Transforms by Oxc")
    * [JavaScript Minification by Oxc](https://vite.dev/guide/migration#javascript-minification-by-oxc "JavaScript Minification by Oxc")
    * [CSS Minification by Lightning CSS](https://vite.dev/guide/migration#css-minification-by-lightning-css "CSS Minification by Lightning CSS")
    * [Consistent CommonJS Interop](https://vite.dev/guide/migration#consistent-commonjs-interop "Consistent CommonJS Interop")
    * [Removed Module Resolution Using Format Sniffing](https://vite.dev/guide/migration#removed-module-resolution-using-format-sniffing "Removed Module Resolution Using Format Sniffing")
    * [Require Calls For Externalized Modules](https://vite.dev/guide/migration#require-calls-for-externalized-modules "Require Calls For Externalized Modules")
    * [import.meta.url in UMD / IIFE](https://vite.dev/guide/migration#import-meta-url-in-umd-iife "import.meta.url in UMD / IIFE")
    * [Removed build.rollupOptions.watch.chokidar option](https://vite.dev/guide/migration#removed-build-rollupoptions-watch-chokidar-option "Removed build.rollupOptions.watch.chokidar option")
    * [Removed object form build.rollupOptions.output.manualChunks and deprecate function form one](https://vite.dev/guide/migration#removed-object-form-build-rollupoptions-output-manualchunks-and-deprecate-function-form-one "Removed object form build.rollupOptions.output.manualChunks and deprecate function form one")
    * [build() Throws BundleError](https://vite.dev/guide/migration#build-throws-bundleerror "build\(\) Throws BundleError")
    * [Module Type Support and Auto Detection](https://vite.dev/guide/migration#module-type-support-and-auto-detection "Module Type Support and Auto Detection")
    * [Other Related Deprecations](https://vite.dev/guide/migration#other-related-deprecations "Other Related Deprecations")
  * [Removed Deprecated Features NRV](https://vite.dev/guide/migration#removed-deprecated-features "Removed Deprecated Features NRV")
  * [Advanced](https://vite.dev/guide/migration#advanced "Advanced")
  * [Migration from v6](https://vite.dev/guide/migration#migration-from-v6 "Migration from v6")

Are you an LLM? You can read better optimized documentation at /guide/migration.md for this page in Markdown format
# Migration from v7 [​](https://vite.dev/guide/migration#migration-from-v7)
If you are migrating from `rolldown-vite`, the technical preview release for Rolldown integrated Vite for v6 & v7, only the sections with NRV in the title are applicable.
## Default Browser Target Change [NRV](https://vite.dev/guide/migration#migration-from-v7) [​](https://vite.dev/guide/migration#default-browser-target-change)
The default browser value of `build.target` and `'baseline-widely-available'`, is updated to newer browser version:
  * Chrome 107 → 111
  * Edge 107 → 111
  * Firefox 104 → 114
  * Safari 16.0 → 16.4

These browser versions align with
## Rolldown [​](https://vite.dev/guide/migration#rolldown)
Vite 8 uses
### Gradual Migration [​](https://vite.dev/guide/migration#gradual-migration)
The `rolldown-vite` package implements Vite 7 with Rolldown, without other Vite 8 changes. This can be used as an intermediate step to migrate to Vite 8. See [the Rolldown Integration guide](https://v7.vite.dev/guide/rolldown) in the Vite 7 docs to switch to `rolldown-vite` from Vite 7.
For users migrating from `rolldown-vite` to Vite 8, you can undo the dependency changes in `package.json` and update to Vite 8:
json
```
{
  "devDependencies": {
    "vite": "npm:rolldown-vite@7.2.2"
    "vite": "^8.0.0"
  }
}
```

### Dependency Optimizer Now Uses Rolldown [​](https://vite.dev/guide/migration#dependency-optimizer-now-uses-rolldown)
Rolldown is now used for dependency optimization instead of esbuild. Vite still supports [`optimizeDeps.esbuildOptions`](https://vite.dev/config/dep-optimization-options#optimizedeps-esbuildoptions) for backward compatibility by converting it to [`optimizeDeps.rolldownOptions`](https://vite.dev/config/dep-optimization-options#optimizedeps-rolldownoptions) automatically. `optimizeDeps.esbuildOptions` is now deprecated and will be removed in the future and we encourage you to migrate to `optimizeDeps.rolldownOptions`.
The following options are converted automatically:
You can get the options set by the compatibility layer from the `configResolved` hook:
js
```
const plugin = {
  name: 'log-config',
  configResolved(config) {
    console.log('options', config.optimizeDeps.rolldownOptions)
  },
},
```

### JavaScript Transforms by Oxc [​](https://vite.dev/guide/migration#javascript-transforms-by-oxc)
Oxc is now used for JavaScript transformation instead of esbuild. Vite still supports the [`esbuild`](https://vite.dev/config/shared-options#esbuild) option for backward compatibility by converting it to [`oxc`](https://vite.dev/config/shared-options#oxc) automatically. `esbuild` is now deprecated and will be removed in the future and we encourage you to migrate to `oxc`.
The following options are converted automatically:
  * `esbuild.jsxInject` -> `oxc.jsxInject`
  * `esbuild.include` -> `oxc.include`
  * `esbuild.exclude` -> `oxc.exclude`
  *     * `esbuild.jsx: 'preserve'` -> `oxc.jsx: 'preserve'`
    * `esbuild.jsx: 'automatic'` -> `oxc.jsx: { runtime: 'automatic' }`
      * `oxc.jsx.importSource`
    * `esbuild.jsx: 'transform'` -> `oxc.jsx: { runtime: 'classic' }`
      * `oxc.jsx.pragma`
      * `oxc.jsx.pragmaFrag`
    * `oxc.jsx.development`
    * `oxc.jsx.pure`

The
You can get the options set by the compatibility layer from the `configResolved` hook:
js
```
const plugin = {
  name: 'log-config',
  configResolved(config) {
    console.log('options', config.oxc)
  },
},
```

Currently, the Oxc transformer does not support lowering native decorators as we are waiting for the specification to progress, see (
Workaround for lowering native decorators
You can use
**Using Babel:**
npmYarnpnpmBunDeno
bash
```
$ npm install -D @rolldown/plugin-babel @babel/plugin-proposal-decorators
```

bash
```
$ yarn add -D @rolldown/plugin-babel @babel/plugin-proposal-decorators
```

bash
```
$ pnpm add -D @rolldown/plugin-babel @babel/plugin-proposal-decorators
```

bash
```
$ bun add -D @rolldown/plugin-babel @babel/plugin-proposal-decorators
```

bash
```
$ deno add -D npm:@rolldown/plugin-babel npm:@babel/plugin-proposal-decorators
```

vite.config.ts
ts
```
import { defineConfig } from 'vite'
import babel from '@rolldown/plugin-babel'

function decoratorPreset(options: Record<string, unknown>) {
  return {
    preset: () => ({
      plugins: [['@babel/plugin-proposal-decorators', options]],
    }),
    rolldown: {
      // Only run this transform if the file contains a decorator.
      filter: {
        code: '@',
      },
    },
  }
}

export default defineConfig({
  plugins: [babel({ presets: [decoratorPreset({ version: '2023-11' })] })],
})
```

**Using SWC:**
npmYarnpnpmBunDeno
bash
```
$ npm install -D @rollup/plugin-swc @swc/core
```

bash
```
$ yarn add -D @rollup/plugin-swc @swc/core
```

bash
```
$ pnpm add -D @rollup/plugin-swc @swc/core
```

bash
```
$ bun add -D @rollup/plugin-swc @swc/core
```

bash
```
$ deno add -D npm:@rollup/plugin-swc npm:@swc/core
```

js
```
import { defineConfig, withFilter } from 'vite'

export default defineConfig({
  // ...
  plugins: [
    withFilter(
      swc({
        swc: {
          jsc: {
            parser: { decorators: true, decoratorsBeforeExport: true },
            transform: { decoratorVersion: '2023-11' },
          },
        },
      }),
      // Only run this transform if the file contains a decorator.
      { transform: { code: '@' } },
    ),
  ],
})
```

#### esbuild Fallbacks [​](https://vite.dev/guide/migration#esbuild-fallbacks)
`esbuild` is no longer directly used by Vite and is now an optional dependency. If you are using a plugin that uses the `transformWithEsbuild` function, you need to install `esbuild` as a `devDependency`. The `transformWithEsbuild` function is deprecated and will be removed in the future. We recommend migrating to the new `transformWithOxc` function instead.
### JavaScript Minification by Oxc [​](https://vite.dev/guide/migration#javascript-minification-by-oxc)
The Oxc Minifier is now used for JavaScript minification instead of esbuild. You can use the deprecated [`build.minify: 'esbuild'`](https://vite.dev/config/build-options#build-minify) option to switch back to esbuild. This configuration option will be removed in the future and you need install `esbuild` as a `devDependency` as Vite no longer relies on esbuild directly.
If you were using the `esbuild.minify*` options to control minification behavior, you can now use `build.rolldownOptions.output.minify` instead. If you were using the `esbuild.drop` option, you can now use
Property mangling and its related options (
esbuild and Oxc Minifier make slightly different assumptions about source code. In case you suspect the minifier is causing breakage in your code, you can compare these assumptions here:
Please report any issues you find related to minification in your JavaScript apps.
### CSS Minification by Lightning CSS [​](https://vite.dev/guide/migration#css-minification-by-lightning-css)
[`build.cssMinify: 'esbuild'`](https://vite.dev/config/build-options#build-cssminify) option to switch back to esbuild. Note that you need to install `esbuild` as a `devDependency`.
Lightning CSS supports better syntax lowering and your CSS bundle size might increase slightly.
### Consistent CommonJS Interop [​](https://vite.dev/guide/migration#consistent-commonjs-interop)
The `default` import from a CommonJS (CJS) module is now handled in a consistent way.
If it matches one of the following conditions, the `default` import is the `module.exports` value of the importee CJS module. Otherwise, the `default` import is the `module.exports.default` value of the importee CJS module:
  * The importer is `.mjs` or `.mts`.
  * The closest `package.json` for the importer has a `type` field set to `module`.
  * The `module.exports.__esModule` value of the importee CJS module is not set to true.

The previous behavior
In development, if it matches one of the following conditions, the `default` import is the `module.exports` value of the importee CJS module. Otherwise, the `default` import is the `module.exports.default` value of the importee CJS module:
  * _The importer is included in the dependency optimization_ and `.mjs` or `.mts`.
  * _The importer is included in the dependency optimization_ and the closest `package.json` for the importer has a `type` field set to `module`.
  * The `module.exports.__esModule` value of the importee CJS module is not set to true.

In build, the conditions were:
  * The `module.exports.__esModule` value of the importee CJS module is not set to true.
  * _`default`property of`module.exports` does not exist_.

(assuming `'auto'`)
See Rolldown's docs about this problem for more details:
This change may break some existing code importing CJS modules. You can use the deprecated `legacy.inconsistentCjsInterop: true` option to temporarily restore the previous behavior. If you find a package that is affected by this change, please report it to the package author or send them a pull request. Make sure to link to the Rolldown documentation above so that the author can understand the context.
### Removed Module Resolution Using Format Sniffing [​](https://vite.dev/guide/migration#removed-module-resolution-using-format-sniffing)
When both `browser` and `module` fields are present in `package.json`, Vite used to resolve the field based on the content of the file and it used to pick the ESM file for browsers. This was introduced because some packages were using the `module` field to point to ESM files for Node.js and some other packages were using the `browser` field to point to UMD files for browsers. Given that the modern `exports` field solved this problem and is now adopted by many packages, Vite no longer uses this heuristic and always respects the order of the [`resolve.mainFields`](https://vite.dev/config/shared-options#resolve-mainfields) option. If you were relying on this behavior, you can use the [`resolve.alias`](https://vite.dev/config/shared-options#resolve-alias) option to map the field to the desired file or apply a patch with your package manager (e.g. `patch-package`, `pnpm patch`).
### Require Calls For Externalized Modules [​](https://vite.dev/guide/migration#require-calls-for-externalized-modules)
`require` calls for externalized modules are now preserved as `require` calls and not converted to `import` statements. This is to preserve the semantics of `require` calls. If you want to convert them to `import` statements, you can use `vite`.
js
```
import { defineConfig, esmExternalRequirePlugin } from 'vite'

export default defineConfig({
  // ...
  plugins: [
    esmExternalRequirePlugin({
      external: ['react', 'vue', /^node:/],
    }),
  ],
})
```

See Rolldown's docs for more details:
###  `import.meta.url` in UMD / IIFE [​](https://vite.dev/guide/migration#import-meta-url-in-umd-iife)
`import.meta.url` is no longer polyfilled in UMD / IIFE output formats. It will be replaced with `undefined` by default. If you prefer the previous behavior, you can use the [`define`](https://vite.dev/config/shared-options#define) option with
### Removed `build.rollupOptions.watch.chokidar` option [​](https://vite.dev/guide/migration#removed-build-rollupoptions-watch-chokidar-option)
The `build.rollupOptions.watch.chokidar` option was removed. Please migrate to the
### Removed object form `build.rollupOptions.output.manualChunks` and deprecate function form one [​](https://vite.dev/guide/migration#removed-object-form-build-rollupoptions-output-manualchunks-and-deprecate-function-form-one)
The object form `output.manualChunks` option is not supported anymore. The function form `output.manualChunks` is deprecated. Rolldown has the more flexible `codeSplitting`:
###  `build()` Throws `BundleError` [​](https://vite.dev/guide/migration#build-throws-bundleerror)
_This change only affects JS API users._
`build()` now throws a `BundleError` is typed as `Error & { errors?: RolldownError[] }` and it wraps the individual errors in an `errors` array. If you need the individual errors, you need to access `.errors`:
js
```
try {
  await build()
} catch (e) {
  if (e.errors) {
    for (const error of e.errors) {
      console.log(error.code) // error code
    }
  }
}
```

### Module Type Support and Auto Detection [​](https://vite.dev/guide/migration#module-type-support-and-auto-detection)
_This change only affects plugin authors._
Rolldown has experimental support for `load` or `transform` hooks, you may need to add `moduleType: 'js'` to the returned value:
js
```
const plugin = {
  name: 'txt-loader',
  load(id) {
    if (id.endsWith('.txt')) {
      const content = fs.readFile(id, 'utf-8')
      return {
        code: `export default ${JSON.stringify(content)}`,
        moduleType: 'js',
      }
    }
  },
}
```

### Other Related Deprecations [​](https://vite.dev/guide/migration#other-related-deprecations)
The following options are deprecated and will be removed in the future:
  * `build.rollupOptions`: renamed to `build.rolldownOptions`
  * `worker.rollupOptions`: renamed to `worker.rolldownOptions`
  * `build.commonjsOptions`: it is now no-op
  * `build.dynamicImportVarsOptions.warnOnError`: it is now no-op
  * `resolve.alias[].customResolver`: Use a custom plugin with `resolveId` hook and `enforce: 'pre'` instead

## Removed Deprecated Features [NRV](https://vite.dev/guide/migration#migration-from-v7) [​](https://vite.dev/guide/migration#removed-deprecated-features)
  * Passing an URL to `import.meta.hot.accept` is no longer supported. Please pass an id instead. (

## Advanced [​](https://vite.dev/guide/migration#advanced)
These breaking changes are expected to only affect a minority of use cases:
  * TypeScript legacy namespace is only supported partially. See
  * `define` does not share reference for objects: When you pass an object as a value to `define`, each variable will have a separate copy of the object. See
  * `bundle` object changes (`bundle` is an object passed in `generateBundle` / `writeBundle` hooks, returned by `build` function):
    * Assigning to `bundle[foo]` is not supported. This is discouraged by Rollup as well. Please use `this.emitFile()` instead.
    * the reference is not shared across the hooks (
    * `structuredClone(bundle)` errors with `DataCloneError: #<Object> could not be cloned`. This is not supported anymore. Please clone it with `structuredClone({ ...bundle })`. (
  * All parallel hooks in Rollup works as sequential hooks. See
  * `"use strict";` is not injected sometimes. See
  * Transforming to ES5 and below with plugin-legacy is not supported (
  * Passing the same browser with multiple versions of it to `build.target` option now errors: esbuild selects the latest version of it, which was probably not what you intended.
  * Missing support by Rolldown: The following features are not supported by Rolldown and is no longer supported by Vite.
    * `build.rollupOptions.output.format: 'system'` (
    * `build.rollupOptions.output.format: 'amd'` (
    * `shouldTransformCachedModule` hook (
    * `resolveImportMeta` hook (
    * `renderDynamicImport` hook (
    * `resolveFileUrl` hook
  * `parseAst` / `parseAstAsync` functions are now deprecated in favor of `parseSync` / `parse` functions which have more features.
  * comments are removed before the `renderChunk` hook instead of after the `renderChunk` hook
  * comments other than the ones listed

## Migration from v6 [​](https://vite.dev/guide/migration#migration-from-v6)
Check the [Migration from v6 Guide](https://v7.vite.dev/guide/migration) in the Vite v7 docs first to see the needed changes to port your app to Vite 7, and then proceed with the changes on this page.
Pager
[Previous pagePerformance](https://vite.dev/guide/performance)
[Next pageBreaking Changes](https://vite.dev/changes/)
© 2019-present VoidZero Inc. and Vite contributors. (012eb452)
