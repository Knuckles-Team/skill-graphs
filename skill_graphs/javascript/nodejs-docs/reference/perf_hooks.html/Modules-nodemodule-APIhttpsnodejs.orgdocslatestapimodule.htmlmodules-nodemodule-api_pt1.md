## Modules: `node:module` API[#](https://nodejs.org/docs/latest/api/module.html#modules-nodemodule-api)
Added in: v0.3.7
### The `Module` object[#](https://nodejs.org/docs/latest/api/module.html#the-module-object)
  * Type:


Provides general utility methods when interacting with instances of `Module`, the [`module`](https://nodejs.org/docs/latest/api/module.html#the-module-object) variable often seen in [CommonJS](https://nodejs.org/docs/latest/api/modules.html) modules. Accessed via `import 'node:module'` or `require('node:module')`.
####  `module.builtinModules`[#](https://nodejs.org/docs/latest/api/module.html#modulebuiltinmodules)
Added in: v9.3.0, v8.10.0, v6.13.0History Version | Changes
---|---
v23.5.0 | The list now also contains prefix-only modules.
  * Type:


A list of the names of all modules provided by Node.js. Can be used to verify if a module is maintained by a third party or not.
`module` in this context isn't the same object that's provided by the [module wrapper](https://nodejs.org/docs/latest/api/modules.html#the-module-wrapper). To access it, require the `Module` module:
```
// module.mjs
// In an ECMAScript module
import { builtinModules as builtin } from 'node:module';
// module.cjs
// In a CommonJS module
const builtin = require('node:module').builtinModules;
copy
```

####  `module.createRequire(filename)`[#](https://nodejs.org/docs/latest/api/module.html#modulecreaterequirefilename)
Added in: v12.2.0
  * `filename` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) Filename to be used to construct the require function. Must be a file URL object, file URL string, or absolute path string.
  * Returns: [`<require>`](https://nodejs.org/docs/latest/api/modules.html#requireid) Require function

```
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);

// sibling-module.js is a CommonJS module.
const siblingModule = require('./sibling-module');
copy
```

####  `module.findPackageJSON(specifier[, base])`[#](https://nodejs.org/docs/latest/api/module.html#modulefindpackagejsonspecifier-base)
Added in: v23.2.0, v22.14.0
[Stability: 1.1](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Active Development
  * `specifier` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) The specifier for the module whose `package.json` to retrieve. When passing a _bare specifier_ , the `package.json` at the root of the package is returned. When passing a _relative specifier_ or an _absolute specifier_ , the closest parent `package.json` is returned.
  * `base` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) The absolute location (`file:` URL string or FS path) of the containing module. For CJS, use `__filename` (not `__dirname`!); for ESM, use `import.meta.url`. You do not need to pass it if `specifier` is an `absolute specifier`.
  * Returns: `package.json` is found. When `specifier` is a package, the package's root `package.json`; when a relative or unresolved, the closest `package.json` to the `specifier`.


> **Caveat** : Do not use this to try to determine module format. There are many things affecting that determination; the `type` field of package.json is the _least_ definitive (ex file extension supersedes it, and a loader hook supersedes that).
> **Caveat** : This currently leverages only the built-in default resolver; if [`resolve` customization hooks](https://nodejs.org/docs/latest/api/module.html#synchronous-resolvespecifier-context-nextresolve) are registered, they will not affect the resolution. This may change in the future.
```
// /path/to/project/packages/bar/bar.js
import { findPackageJSON } from 'node:module';

findPackageJSON('..', import.meta.url);
// '/path/to/project/package.json'
// Same result when passing an absolute specifier instead:
findPackageJSON(new URL('../', import.meta.url));
findPackageJSON(import.meta.resolve('../'));

findPackageJSON('some-package', import.meta.url);
// '/path/to/project/packages/bar/node_modules/some-package/package.json'
// When passing an absolute specifier, you might get a different result if the
// resolved module is inside a subfolder that has nested `package.json`.
findPackageJSON(import.meta.resolve('some-package'));
// '/path/to/project/packages/bar/node_modules/some-package/some-subfolder/package.json'

findPackageJSON('@foo/qux', import.meta.url);
// '/path/to/project/packages/qux/package.json'
// /path/to/project/packages/bar/bar.js
const { findPackageJSON } = require('node:module');
const { pathToFileURL } = require('node:url');
const path = require('node:path');

findPackageJSON('..', __filename);
// '/path/to/project/package.json'
// Same result when passing an absolute specifier instead:
findPackageJSON(pathToFileURL(path.join(__dirname, '..')));

findPackageJSON('some-package', __filename);
// '/path/to/project/packages/bar/node_modules/some-package/package.json'
// When passing an absolute specifier, you might get a different result if the
// resolved module is inside a subfolder that has nested `package.json`.
findPackageJSON(pathToFileURL(require.resolve('some-package')));
// '/path/to/project/packages/bar/node_modules/some-package/some-subfolder/package.json'

findPackageJSON('@foo/qux', __filename);
// '/path/to/project/packages/qux/package.json'
copy
```

####  `module.isBuiltin(moduleName)`[#](https://nodejs.org/docs/latest/api/module.html#moduleisbuiltinmodulename)
Added in: v18.6.0, v16.17.0
  * `moduleName`
  * Returns:

```
import { isBuiltin } from 'node:module';
isBuiltin('node:fs'); // true
isBuiltin('fs'); // true
isBuiltin('wss'); // false
copy
```

####  `module.register(specifier[, parentURL][, options])`[#](https://nodejs.org/docs/latest/api/module.html#moduleregisterspecifier-parenturl-options)
Added in: v20.6.0, v18.19.0History Version | Changes
---|---
v23.6.1, v22.13.1, v20.18.2 | Using this feature with the permission model enabled requires passing `--allow-worker`.
v20.8.0, v18.19.0 | Add support for WHATWG URL instances.
Stability: 1.1 - Active development
  * `specifier` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) Customization hooks to be registered; this should be the same string that would be passed to `import()`, except that if it is relative, it is resolved relative to `parentURL`.
  * `parentURL` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) If you want to resolve `specifier` relative to a base URL, such as `import.meta.url`, you can pass that URL here. **Default:** `'data:'`
  * `options`
    * `parentURL` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) If you want to resolve `specifier` relative to a base URL, such as `import.meta.url`, you can pass that URL here. This property is ignored if the `parentURL` is supplied as the second argument. **Default:** `'data:'`
    * `data` [`initialize`](https://nodejs.org/docs/latest/api/module.html#initialize) hook.
    * `transferList` [transferable objects](https://nodejs.org/docs/latest/api/worker_threads.html#portpostmessagevalue-transferlist) to be passed into the `initialize` hook.


Register a module that exports [hooks](https://nodejs.org/docs/latest/api/module.html#customization-hooks) that customize Node.js module resolution and loading behavior. See [Customization hooks](https://nodejs.org/docs/latest/api/module.html#customization-hooks).
This feature requires `--allow-worker` if used with the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model).
####  `module.registerHooks(options)`[#](https://nodejs.org/docs/latest/api/module.html#moduleregisterhooksoptions)
Added in: v23.5.0, v22.15.0History Version | Changes
---|---
v25.4.0 | Synchronous and in-thread hooks are now release candidate.
Stability: 1.2 - Release candidate
  * `options`
    * `load` [load hook](https://nodejs.org/docs/latest/api/module.html#synchronous-loadurl-context-nextload). **Default:** `undefined`.
    * `resolve` [resolve hook](https://nodejs.org/docs/latest/api/module.html#synchronous-resolvespecifier-context-nextresolve). **Default:** `undefined`.


Register [hooks](https://nodejs.org/docs/latest/api/module.html#customization-hooks) that customize Node.js module resolution and loading behavior. See [Customization hooks](https://nodejs.org/docs/latest/api/module.html#customization-hooks).
####  `module.stripTypeScriptTypes(code[, options])`[#](https://nodejs.org/docs/latest/api/module.html#modulestriptypescripttypescode-options)
Added in: v23.2.0, v22.13.0
Stability: 1.2 - Release candidate
  * `code`
  * `options`
    * `mode` **Default:** `'strip'`. Possible values are:
      * `'strip'` Only strip type annotations without performing the transformation of TypeScript features.
      * `'transform'` Strip type annotations and transform TypeScript features to JavaScript.
    * `sourceMap` **Default:** `false`. Only when `mode` is `'transform'`, if `true`, a source map will be generated for the transformed code.
    * `sourceUrl`
  * Returns:


`module.stripTypeScriptTypes()` removes type annotations from TypeScript code. It can be used to strip type annotations from TypeScript code before running it with `vm.runInContext()` or `vm.compileFunction()`.
By default, it will throw an error if the code contains TypeScript features that require transformation such as `Enums`, see [type-stripping](https://nodejs.org/docs/latest/api/typescript.html#type-stripping) for more information.
When mode is `'transform'`, it also transforms TypeScript features to JavaScript, see [transform TypeScript features](https://nodejs.org/docs/latest/api/typescript.html#typescript-features) for more information.
When mode is `'strip'`, source maps are not generated, because locations are preserved. If `sourceMap` is provided, when mode is `'strip'`, an error will be thrown.
_WARNING_ : The output of this function should not be considered stable across Node.js versions, due to changes in the TypeScript parser.
```
import { stripTypeScriptTypes } from 'node:module';
const code = 'const a: number = 1;';
const strippedCode = stripTypeScriptTypes(code);
console.log(strippedCode);
// Prints: const a         = 1;
const { stripTypeScriptTypes } = require('node:module');
const code = 'const a: number = 1;';
const strippedCode = stripTypeScriptTypes(code);
console.log(strippedCode);
// Prints: const a         = 1;
copy
```

If `sourceUrl` is provided, it will be used appended as a comment at the end of the output:
```
import { stripTypeScriptTypes } from 'node:module';
const code = 'const a: number = 1;';
const strippedCode = stripTypeScriptTypes(code, { mode: 'strip', sourceUrl: 'source.ts' });
console.log(strippedCode);
// Prints: const a         = 1\n\n//# sourceURL=source.ts;
const { stripTypeScriptTypes } = require('node:module');
const code = 'const a: number = 1;';
const strippedCode = stripTypeScriptTypes(code, { mode: 'strip', sourceUrl: 'source.ts' });
console.log(strippedCode);
// Prints: const a         = 1\n\n//# sourceURL=source.ts;
copy
```

When `mode` is `'transform'`, the code is transformed to JavaScript:
```
import { stripTypeScriptTypes } from 'node:module';
const code = `
  namespace MathUtil {
    export const add = (a: number, b: number) => a + b;
  }`;
const strippedCode = stripTypeScriptTypes(code, { mode: 'transform', sourceMap: true });
console.log(strippedCode);
// Prints:
// var MathUtil;
// (function(MathUtil) {
//     MathUtil.add = (a, b)=>a + b;
// })(MathUtil || (MathUtil = {}));
// # sourceMappingURL=data:application/json;base64, ...
const { stripTypeScriptTypes } = require('node:module');
const code = `
  namespace MathUtil {
    export const add = (a: number, b: number) => a + b;
  }`;
const strippedCode = stripTypeScriptTypes(code, { mode: 'transform', sourceMap: true });
console.log(strippedCode);
// Prints:
// var MathUtil;
// (function(MathUtil) {
//     MathUtil.add = (a, b)=>a + b;
// })(MathUtil || (MathUtil = {}));
// # sourceMappingURL=data:application/json;base64, ...
copy
```

####  `module.syncBuiltinESMExports()`[#](https://nodejs.org/docs/latest/api/module.html#modulesyncbuiltinesmexports)
Added in: v12.12.0
The `module.syncBuiltinESMExports()` method updates all the live bindings for builtin [ES Modules](https://nodejs.org/docs/latest/api/esm.html) to match the properties of the [CommonJS](https://nodejs.org/docs/latest/api/modules.html) exports. It does not add or remove exported names from the [ES Modules](https://nodejs.org/docs/latest/api/esm.html).
```
const fs = require('node:fs');
const assert = require('node:assert');
const { syncBuiltinESMExports } = require('node:module');

fs.readFile = newAPI;

delete fs.readFileSync;

function newAPI() {
  // ...
}

fs.newAPI = newAPI;

syncBuiltinESMExports();

import('node:fs').then((esmFS) => {
  // It syncs the existing readFile property with the new value
  assert.strictEqual(esmFS.readFile, newAPI);
  // readFileSync has been deleted from the required fs
  assert.strictEqual('readFileSync' in fs, false);
  // syncBuiltinESMExports() does not remove readFileSync from esmFS
  assert.strictEqual('readFileSync' in esmFS, true);
  // syncBuiltinESMExports() does not add names
  assert.strictEqual(esmFS.newAPI, undefined);
});
copy
```

### Module compile cache[#](https://nodejs.org/docs/latest/api/module.html#module-compile-cache)
Added in: v22.1.0History Version | Changes
---|---
v22.8.0 | add initial JavaScript APIs for runtime access.
The module compile cache can be enabled either using the [`module.enableCompileCache()`](https://nodejs.org/docs/latest/api/module.html#moduleenablecompilecacheoptions) method or the [`NODE_COMPILE_CACHE=dir`](https://nodejs.org/docs/latest/api/cli.html#node_compile_cachedir) environment variable. After it is enabled, whenever Node.js compiles a CommonJS, a ECMAScript Module, or a TypeScript module, it will use on-disk
To clean up the generated compile cache on disk, simply remove the cache directory. The cache directory will be recreated the next time the same directory is used for for compile cache storage. To avoid filling up the disk with stale cache, it is recommended to use a directory under the [`os.tmpdir()`](https://nodejs.org/docs/latest/api/os.html#ostmpdir). If the compile cache is enabled by a call to [`module.enableCompileCache()`](https://nodejs.org/docs/latest/api/module.html#moduleenablecompilecacheoptions) without specifying the `directory`, Node.js will use the [`NODE_COMPILE_CACHE=dir`](https://nodejs.org/docs/latest/api/cli.html#node_compile_cachedir) environment variable if it's set, or defaults to `path.join(os.tmpdir(), 'node-compile-cache')` otherwise. To locate the compile cache directory used by a running Node.js instance, use [`module.getCompileCacheDir()`](https://nodejs.org/docs/latest/api/module.html#modulegetcompilecachedir).
The enabled module compile cache can be disabled by the [`NODE_DISABLE_COMPILE_CACHE=1`](https://nodejs.org/docs/latest/api/cli.html#node_disable_compile_cache1) environment variable. This can be useful when the compile cache leads to unexpected or undesired behaviors (e.g. less precise test coverage).
At the moment, when the compile cache is enabled and a module is loaded afresh, the code cache is generated from the compiled code immediately, but will only be written to disk when the Node.js instance is about to exit. This is subject to change. The [`module.flushCompileCache()`](https://nodejs.org/docs/latest/api/module.html#moduleflushcompilecache) method can be used to ensure the accumulated code cache is flushed to disk in case the application wants to spawn other Node.js instances and let them share the cache long before the parent exits.
The compile cache layout on disk is an implementation detail and should not be relied upon. The compile cache generated is typically only reusable in the same version of Node.js, and should be not assumed to be compatible across different versions of Node.js.
#### Portability of the compile cache[#](https://nodejs.org/docs/latest/api/module.html#portability-of-the-compile-cache)
By default, caches are invalidated when the absolute paths of the modules being cached are changed. To keep the cache working after moving the project directory, enable portable compile cache. This allows previously compiled modules to be reused across different directory locations as long as the layout relative to the cache directory remains the same. This would be done on a best-effort basis. If Node.js cannot compute the location of a module relative to the cache directory, the module will not be cached.
There are two ways to enable the portable mode:
  1. Using the portable option in [`module.enableCompileCache()`](https://nodejs.org/docs/latest/api/module.html#moduleenablecompilecacheoptions):
```
// Non-portable cache (default): cache breaks if project is moved
module.enableCompileCache({ directory: '/path/to/cache/storage/dir' });

// Portable cache: cache works after the project is moved
module.enableCompileCache({ directory: '/path/to/cache/storage/dir', portable: true });
copy
```

  2. Setting the environment variable: [`NODE_COMPILE_CACHE_PORTABLE=1`](https://nodejs.org/docs/latest/api/cli.html#node_compile_cache_portable1)


#### Limitations of the compile cache[#](https://nodejs.org/docs/latest/api/module.html#limitations-of-the-compile-cache)
Currently when using the compile cache with
Compilation cache generated by one version of Node.js can not be reused by a different version of Node.js. Cache generated by different versions of Node.js will be stored separately if the same base directory is used to persist the cache, so they can co-exist.
####  `module.constants.compileCacheStatus`[#](https://nodejs.org/docs/latest/api/module.html#moduleconstantscompilecachestatus)
Added in: v22.8.0History Version | Changes
---|---
v25.4.0 | This feature is no longer experimental.
The following constants are returned as the `status` field in the object returned by [`module.enableCompileCache()`](https://nodejs.org/docs/latest/api/module.html#moduleenablecompilecacheoptions) to indicate the result of the attempt to enable the [module compile cache](https://nodejs.org/docs/latest/api/module.html#module-compile-cache).
Constant | Description
---|---
`ENABLED` | Node.js has enabled the compile cache successfully. The directory used to store the compile cache will be returned in the `directory` field in the returned object.
`ALREADY_ENABLED` | The compile cache has already been enabled before, either by a previous call to `module.enableCompileCache()`, or by the `NODE_COMPILE_CACHE=dir` environment variable. The directory used to store the compile cache will be returned in the `directory` field in the returned object.
`FAILED` | Node.js fails to enable the compile cache. This can be caused by the lack of permission to use the specified directory, or various kinds of file system errors. The detail of the failure will be returned in the `message` field in the returned object.
`DISABLED` | Node.js cannot enable the compile cache because the environment variable `NODE_DISABLE_COMPILE_CACHE=1` has been set.
####  `module.enableCompileCache([options])`[#](https://nodejs.org/docs/latest/api/module.html#moduleenablecompilecacheoptions)
Added in: v22.8.0History Version | Changes
---|---
v25.4.0 | This feature is no longer experimental.
v25.0.0 | Add `portable` option to enable portable compile cache.
v25.0.0 | Rename the unreleased `path` option to `directory` to maintain consistency.
  * `options` `options.directory`.
    * `directory` [`NODE_COMPILE_CACHE=dir`](https://nodejs.org/docs/latest/api/cli.html#node_compile_cachedir) environment variable will be used if it's set, or `path.join(os.tmpdir(), 'node-compile-cache')` otherwise.
    * `portable` `true`, enables portable compile cache so that the cache can be reused even if the project directory is moved. This is a best-effort feature. If not specified, it will depend on whether the environment variable [`NODE_COMPILE_CACHE_PORTABLE=1`](https://nodejs.org/docs/latest/api/cli.html#node_compile_cache_portable1) is set.
  * Returns:
    * `status` [`module.constants.compileCacheStatus`](https://nodejs.org/docs/latest/api/module.html#moduleconstantscompilecachestatus)
    * `message` `status` is `module.constants.compileCacheStatus.FAILED`.
    * `directory` `status` is `module.constants.compileCacheStatus.ENABLED` or `module.constants.compileCacheStatus.ALREADY_ENABLED`.


Enable [module compile cache](https://nodejs.org/docs/latest/api/module.html#module-compile-cache) in the current Node.js instance.
For general use cases, it's recommended to call `module.enableCompileCache()` without specifying the `options.directory`, so that the directory can be overridden by the `NODE_COMPILE_CACHE` environment variable when necessary.
Since compile cache is supposed to be a optimization that is not mission critical, this method is designed to not throw any exception when the compile cache cannot be enabled. Instead, it will return an object containing an error message in the `message` field to aid debugging. If compile cache is enabled successfully, the `directory` field in the returned object contains the path to the directory where the compile cache is stored. The `status` field in the returned object would be one of the `module.constants.compileCacheStatus` values to indicate the result of the attempt to enable the [module compile cache](https://nodejs.org/docs/latest/api/module.html#module-compile-cache).
This method only affects the current Node.js instance. To enable it in child worker threads, either call this method in child worker threads too, or set the `process.env.NODE_COMPILE_CACHE` value to compile cache directory so the behavior can be inherited into the child workers. The directory can be obtained either from the `directory` field returned by this method, or with [`module.getCompileCacheDir()`](https://nodejs.org/docs/latest/api/module.html#modulegetcompilecachedir).
####  `module.flushCompileCache()`[#](https://nodejs.org/docs/latest/api/module.html#moduleflushcompilecache)
Added in: v23.0.0, v22.10.0History Version | Changes
---|---
v25.4.0 | This feature is no longer experimental.
Flush the [module compile cache](https://nodejs.org/docs/latest/api/module.html#module-compile-cache) accumulated from modules already loaded in the current Node.js instance to disk. This returns after all the flushing file system operations come to an end, no matter they succeed or not. If there are any errors, this will fail silently, since compile cache misses should not interfere with the actual operation of the application.
####  `module.getCompileCacheDir()`[#](https://nodejs.org/docs/latest/api/module.html#modulegetcompilecachedir)
Added in: v22.8.0History Version | Changes
---|---
v25.4.0 | This feature is no longer experimental.
  * Returns: [module compile cache](https://nodejs.org/docs/latest/api/module.html#module-compile-cache) directory if it is enabled, or `undefined` otherwise.


### Customization Hooks[#](https://nodejs.org/docs/latest/api/module.html#customization-hooks)
Added in: v8.8.0History Version | Changes
---|---
v25.4.0 | Synchronous and in-thread hooks are now release candidate.
v23.5.0, v22.15.0 | Add support for synchronous and in-thread hooks.
v20.6.0, v18.19.0 | Added `initialize` hook to replace `globalPreload`.
v18.6.0, v16.17.0 | Add support for chaining loaders.
v16.12.0 | Removed `getFormat`, `getSource`, `transformSource`, and `globalPreload`; added `load` hook and `getGlobalPreload` hook.
Node.js currently supports two types of module customization hooks:
  1. [`module.registerHooks(options)`](https://nodejs.org/docs/latest/api/module.html#moduleregisterhooksoptions): takes synchronous hook functions that are run directly on the thread where the modules are loaded.
  2. [`module.register(specifier[, parentURL][, options])`](https://nodejs.org/docs/latest/api/module.html#moduleregisterspecifier-parenturl-options): takes specifier to a module that exports asynchronous hook functions. The functions are run on a separate loader thread.


The asynchronous hooks incur extra overhead from inter-thread communication, and have [several caveats](https://nodejs.org/docs/latest/api/module.html#caveats-of-asynchronous-customization-hooks) especially when customizing CommonJS modules in the module graph. In most cases, it's recommended to use synchronous hooks via `module.registerHooks()` for simplicity.
#### Synchronous customization hooks[#](https://nodejs.org/docs/latest/api/module.html#synchronous-customization-hooks)
Stability: 1.2 - Release candidate
##### Registration of synchronous customization hooks[#](https://nodejs.org/docs/latest/api/module.html#registration-of-synchronous-customization-hooks)
To register synchronous customization hooks, use [`module.registerHooks()`](https://nodejs.org/docs/latest/api/module.html#moduleregisterhooksoptions), which takes [synchronous hook functions](https://nodejs.org/docs/latest/api/module.html#hook-functions-accepted-by-moduleregisterhooks) directly in-line.
```
// register-hooks.js
import { registerHooks } from 'node:module';
registerHooks({
  resolve(specifier, context, nextResolve) { /* implementation */ },
  load(url, context, nextLoad) { /* implementation */ },
});
// register-hooks.js
const { registerHooks } = require('node:module');
registerHooks({
  resolve(specifier, context, nextResolve) { /* implementation */ },
