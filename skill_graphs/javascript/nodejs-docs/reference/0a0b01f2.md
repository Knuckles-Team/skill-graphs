## Modules: ECMAScript modules[#](https://nodejs.org/docs/latest/api/esm.html#modules-ecmascript-modules)
Added in: v8.5.0History Version | Changes
---|---
v23.1.0, v22.12.0, v20.18.3, v18.20.5 | Import attributes are no longer experimental.
v22.0.0 | Drop support for import assertions.
v21.0.0, v20.10.0, v18.20.0 | Add experimental support for import attributes.
v20.0.0, v18.19.0 | Module customization hooks are executed off the main thread.
v18.6.0, v16.17.0 | Add support for chaining module customization hooks.
v17.1.0, v16.14.0 | Add experimental support for import assertions.
v17.0.0, v16.12.0 | Consolidate customization hooks, removed `getFormat`, `getSource`, `transformSource`, and `getGlobalPreloadCode` hooks added `load` and `globalPreload` hooks allowed returning `format` from either `resolve` or `load` hooks.
v15.3.0, v14.17.0, v12.22.0 | Stabilize modules implementation.
v14.13.0, v12.20.0 | Support for detection of CommonJS named exports.
v14.8.0 | Unflag Top-Level Await.
v14.0.0, v13.14.0, v12.20.0 | Remove experimental modules warning.
v13.2.0, v12.17.0 | Loading ECMAScript modules no longer requires a command-line flag.
v12.0.0 | Add support for ES modules using `.js` file extension via `package.json` `"type"` field.
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
### Introduction[#](https://nodejs.org/docs/latest/api/esm.html#introduction)
ECMAScript modules are
The following example of an ES module exports a function:
```
// addTwo.mjs
function addTwo(num) {
  return num + 2;
}

export { addTwo };
copy
```

The following example of an ES module imports the function from `addTwo.mjs`:
```
// app.mjs
import { addTwo } from './addTwo.mjs';

// Prints: 6
console.log(addTwo(4));
copy
```

Node.js fully supports ECMAScript modules as they are currently specified and provides interoperability between them and its original module format, [CommonJS](https://nodejs.org/docs/latest/api/modules.html).
### Enabling[#](https://nodejs.org/docs/latest/api/esm.html#enabling)
Node.js has two module systems: [CommonJS](https://nodejs.org/docs/latest/api/modules.html) modules and ECMAScript modules.
Authors can tell Node.js to interpret JavaScript as an ES module via the `.mjs` file extension, the `package.json` [`"type"`](https://nodejs.org/docs/latest/api/packages.html#type) field with a value `"module"`, or the [`--input-type`](https://nodejs.org/docs/latest/api/cli.html#--input-typetype) flag with a value of `"module"`. These are explicit markers of code being intended to run as an ES module.
Inversely, authors can explicitly tell Node.js to interpret JavaScript as CommonJS via the `.cjs` file extension, the `package.json` [`"type"`](https://nodejs.org/docs/latest/api/packages.html#type) field with a value `"commonjs"`, or the [`--input-type`](https://nodejs.org/docs/latest/api/cli.html#--input-typetype) flag with a value of `"commonjs"`.
When code lacks explicit markers for either module system, Node.js will inspect the source code of a module to look for ES module syntax. If such syntax is found, Node.js will run the code as an ES module; otherwise it will run the module as CommonJS. See [Determining module system](https://nodejs.org/docs/latest/api/packages.html#determining-module-system) for more details.
### Packages[#](https://nodejs.org/docs/latest/api/esm.html#packages)
This section was moved to [Modules: Packages](https://nodejs.org/docs/latest/api/packages.html).
###  `import` Specifiers[#](https://nodejs.org/docs/latest/api/esm.html#import-specifiers)
#### Terminology[#](https://nodejs.org/docs/latest/api/esm.html#terminology)
The _specifier_ of an `import` statement is the string after the `from` keyword, e.g. `'node:path'` in `import { sep } from 'node:path'`. Specifiers are also used in `export from` statements, and as the argument to an `import()` expression.
There are three types of specifiers:
  * _Relative specifiers_ like `'./startup.js'` or `'../config.mjs'`. They refer to a path relative to the location of the importing file. _The file extension is always necessary for these._
  * _Bare specifiers_ like `'some-package'` or `'some-package/shuffle'`. They can refer to the main entry point of a package by the package name, or a specific feature module within a package prefixed by the package name as per the examples respectively. _Including the file extension is only necessary for packages without an[`"exports"`](https://nodejs.org/docs/latest/api/packages.html#exports) field._
  * _Absolute specifiers_ like `'file:///opt/nodejs/config.js'`. They refer directly and explicitly to a full path.


Bare specifier resolutions are handled by the [Node.js module resolution and loading algorithm](https://nodejs.org/docs/latest/api/esm.html#resolution-algorithm-specification). All other specifier resolutions are always only resolved with the standard relative
Like in CommonJS, module files within packages can be accessed by appending a path to the package name unless the package's [`package.json`](https://nodejs.org/docs/latest/api/packages.html#nodejs-packagejson-field-definitions) contains an [`"exports"`](https://nodejs.org/docs/latest/api/packages.html#exports) field, in which case files within packages can only be accessed via the paths defined in [`"exports"`](https://nodejs.org/docs/latest/api/packages.html#exports).
For details on these package resolution rules that apply to bare specifiers in the Node.js module resolution, see the [packages documentation](https://nodejs.org/docs/latest/api/packages.html).
#### Mandatory file extensions[#](https://nodejs.org/docs/latest/api/esm.html#mandatory-file-extensions)
A file extension must be provided when using the `import` keyword to resolve relative or absolute specifiers. Directory indexes (e.g. `'./startup/index.js'`) must also be fully specified.
This behavior matches how `import` behaves in browser environments, assuming a typically configured server.
#### URLs[#](https://nodejs.org/docs/latest/api/esm.html#urls)
ES modules are resolved and cached as URLs. This means that special characters must be [percent-encoded](https://nodejs.org/docs/latest/api/url.html#percent-encoding-in-urls), such as `#` with `%23` and `?` with `%3F`.
`file:`, `node:`, and `data:` URL schemes are supported. A specifier like `'https://example.com/app.js'` is not supported natively in Node.js unless using a [custom HTTPS loader](https://nodejs.org/docs/latest/api/module.html#import-from-https).
#####  `file:` URLs[#](https://nodejs.org/docs/latest/api/esm.html#file-urls)
Modules are loaded multiple times if the `import` specifier used to resolve them has a different query or fragment.
```
import './foo.mjs?query=1'; // loads ./foo.mjs with query of "?query=1"
import './foo.mjs?query=2'; // loads ./foo.mjs with query of "?query=2"
copy
```

The volume root may be referenced via `/`, `//`, or `file:///`. Given the differences between [url.pathToFileURL](https://nodejs.org/docs/latest/api/url.html#urlpathtofileurlpath-options) when importing a path.
#####  `data:` imports[#](https://nodejs.org/docs/latest/api/esm.html#data-imports)
Added in: v12.10.0
  * `text/javascript` for ES modules
  * `application/json` for JSON
  * `application/wasm` for Wasm

```
import 'data:text/javascript,console.log("hello!");';
import _ from 'data:application/json,"world!"' with { type: 'json' };
copy
```

`data:` URLs only resolve [bare specifiers](https://nodejs.org/docs/latest/api/esm.html#terminology) for builtin modules and [absolute specifiers](https://nodejs.org/docs/latest/api/esm.html#terminology). Resolving [relative specifiers](https://nodejs.org/docs/latest/api/esm.html#terminology) does not work because `data:` is not a `./foo` from `data:text/javascript,import "./foo";` fails to resolve because there is no concept of relative resolution for `data:` URLs.
#####  `node:` imports[#](https://nodejs.org/docs/latest/api/esm.html#node-imports)
Added in: v14.13.1, v12.20.0History Version | Changes
---|---
v16.0.0, v14.18.0 | Added `node:` import support to `require(...)`.
`node:` URLs are supported as an alternative means to load Node.js builtin modules. This URL scheme allows for builtin modules to be referenced by valid absolute URL strings.
```
import fs from 'node:fs/promises';
copy
```

### Import attributes[#](https://nodejs.org/docs/latest/api/esm.html#import-attributes)
Added in: v17.1.0, v16.14.0History Version | Changes
---|---
v21.0.0, v20.10.0, v18.20.0 | Switch from Import Assertions to Import Attributes.
```
import fooData from './foo.json' with { type: 'json' };

const { default: barData } =
  await import('./bar.json', { with: { type: 'json' } });
copy
```

Node.js only supports the `type` attribute, for which it supports the following values:
Attribute `type` | Needed for
---|---
`'json'` | [JSON modules](https://nodejs.org/docs/latest/api/esm.html#json-modules)
The `type: 'json'` attribute is mandatory when importing JSON modules.
### Built-in modules[#](https://nodejs.org/docs/latest/api/esm.html#built-in-modules)
[Built-in modules](https://nodejs.org/docs/latest/api/modules.html#built-in-modules) provide named exports of their public API. A default export is also provided which is the value of the CommonJS exports. The default export can be used for, among other things, modifying the named exports. Named exports of built-in modules are updated only by calling [`module.syncBuiltinESMExports()`](https://nodejs.org/docs/latest/api/module.html#modulesyncbuiltinesmexports).
```
import EventEmitter from 'node:events';
const e = new EventEmitter();
copy
```
```
import { readFile } from 'node:fs';
readFile('./foo.txt', (err, source) => {
  if (err) {
    console.error(err);
  } else {
    console.log(source);
  }
});
copy
```
```
import fs, { readFileSync } from 'node:fs';
import { syncBuiltinESMExports } from 'node:module';
import { Buffer } from 'node:buffer';

fs.readFileSync = () => Buffer.from('Hello, ESM');
syncBuiltinESMExports();

fs.readFileSync === readFileSync;
copy
```

> When importing built-in modules, all the named exports (i.e. properties of the module exports object) are populated even if they are not individually accessed. This can make initial imports of built-in modules slightly slower compared to loading them with `require()` or `process.getBuiltinModule()`, where the module exports object is evaluated immediately, but some of its properties may only be initialized when first accessed individually.
###  `import()` expressions[#](https://nodejs.org/docs/latest/api/esm.html#import-expressions)
###  `import.meta`[#](https://nodejs.org/docs/latest/api/esm.html#importmeta)
  * Type:


The `import.meta` meta property is an `Object` that contains the following properties. It is only supported in ES modules.
####  `import.meta.dirname`[#](https://nodejs.org/docs/latest/api/esm.html#importmetadirname)
Added in: v21.2.0, v20.11.0History Version | Changes
---|---
v24.0.0, v22.16.0 | This property is no longer experimental.
  * Type:


This is the same as the [`path.dirname()`](https://nodejs.org/docs/latest/api/path.html#pathdirnamepath) of the [`import.meta.filename`](https://nodejs.org/docs/latest/api/esm.html#importmetafilename).
> **Caveat** : only present on `file:` modules.
####  `import.meta.filename`[#](https://nodejs.org/docs/latest/api/esm.html#importmetafilename)
Added in: v21.2.0, v20.11.0History Version | Changes
---|---
v24.0.0, v22.16.0 | This property is no longer experimental.
  * Type:


This is the same as the [`url.fileURLToPath()`](https://nodejs.org/docs/latest/api/url.html#urlfileurltopathurl-options) of the [`import.meta.url`](https://nodejs.org/docs/latest/api/esm.html#importmetaurl).
> **Caveat** only local modules support this property. Modules not using the `file:` protocol will not provide it.
####  `import.meta.url`[#](https://nodejs.org/docs/latest/api/esm.html#importmetaurl)
  * Type: `file:` URL of the module.


This is defined exactly the same as it is in browsers providing the URL of the current module file.
This enables useful patterns such as relative file loading:
```
import { readFileSync } from 'node:fs';
const buffer = readFileSync(new URL('./data.proto', import.meta.url));
copy
```

####  `import.meta.main`[#](https://nodejs.org/docs/latest/api/esm.html#importmetamain)
Added in: v24.2.0, v22.18.0
Stability: 1.0 - Early development
  * Type: `true` when the current module is the entry point of the current process; `false` otherwise.


Equivalent to `require.main === module` in CommonJS.
Analogous to Python's `__name__ == "__main__"`.
```
export function foo() {
  return 'Hello, world';
}

function main() {
  const message = foo();
  console.log(message);
}

if (import.meta.main) main();
// `foo` can be imported from another module without possible side-effects from `main`
copy
```

####  `import.meta.resolve(specifier)`[#](https://nodejs.org/docs/latest/api/esm.html#importmetaresolvespecifier)
Added in: v13.9.0, v12.16.2History Version | Changes
---|---
v20.6.0, v18.19.0 | No longer behind `--experimental-import-meta-resolve` CLI flag, except for the non-standard `parentURL` parameter.
v20.6.0, v18.19.0 | This API no longer throws when targeting `file:` URLs that do not map to an existing file on the local FS.
v20.0.0, v18.19.0 | This API now returns a string synchronously instead of a Promise.
v16.2.0, v14.18.0 | Add support for WHATWG `URL` object to `parentURL` parameter.
Stability: 1.2 - Release candidate
  * `specifier`
  * Returns:

```
const dependencyAsset = import.meta.resolve('component-lib/asset.css');
// file:///app/node_modules/component-lib/asset.css
import.meta.resolve('./dep.js');
// file:///app/dep.js
copy
```

All features of the Node.js module resolution are supported. Dependency resolutions are subject to the permitted exports resolutions within the package.
**Caveats** :
  * This can result in synchronous file-system operations, which can impact performance similarly to `require.resolve`.
  * This feature is not available within custom loaders (it would create a deadlock).


**Non-standard API** :
When using the `--experimental-import-meta-resolve` flag, that function accepts a second argument:
  * `parent` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) An optional absolute parent module URL to resolve from. **Default:** `import.meta.url`


### Interoperability with CommonJS[#](https://nodejs.org/docs/latest/api/esm.html#interoperability-with-commonjs)
####  `import` statements[#](https://nodejs.org/docs/latest/api/esm.html#import-statements)
An `import` statement can reference an ES module or a CommonJS module. `import` statements are permitted only in ES modules, but dynamic [`import()`](https://nodejs.org/docs/latest/api/esm.html#import-expressions) expressions are supported in CommonJS for loading ES modules.
When importing [CommonJS modules](https://nodejs.org/docs/latest/api/esm.html#commonjs-namespaces), the `module.exports` object is provided as the default export. Named exports may be available, provided by static analysis as a convenience for better ecosystem compatibility.
####  `require`[#](https://nodejs.org/docs/latest/api/esm.html#require)
The CommonJS module `require` currently only supports loading synchronous ES modules (that is, ES modules that do not use top-level `await`).
See [Loading ECMAScript modules using `require()`](https://nodejs.org/docs/latest/api/modules.html#loading-ecmascript-modules-using-require) for details.
#### CommonJS Namespaces[#](https://nodejs.org/docs/latest/api/esm.html#commonjs-namespaces)
Added in: v14.13.0History Version | Changes
---|---
v23.0.0 | Added `'module.exports'` export marker to CJS namespaces.
CommonJS modules consist of a `module.exports` object which can be of any type.
To support this, when importing CommonJS from an ECMAScript module, a namespace wrapper for the CommonJS module is constructed, which always provides a `default` export key pointing to the CommonJS `module.exports` value.
In addition, a heuristic static analysis is performed against the source text of the CommonJS module to get a best-effort static list of exports to provide on the namespace from values on `module.exports`. This is necessary since these namespaces must be constructed prior to the evaluation of the CJS module.
These CommonJS namespace objects also provide the `default` export as a `'module.exports'` named export, in order to unambiguously indicate that their representation in CommonJS uses this value, and not the namespace value. This mirrors the semantics of the handling of the `'module.exports'` export name in [`require(esm)`](https://nodejs.org/docs/latest/api/modules.html#loading-ecmascript-modules-using-require) interop support.
When importing a CommonJS module, it can be reliably imported using the ES module default import or its corresponding sugar syntax:
```
import { default as cjs } from 'cjs';
// Identical to the above
import cjsSugar from 'cjs';

console.log(cjs);
console.log(cjs === cjsSugar);
// Prints:
//   <module.exports>
//   true
copy
```

This Module Namespace Exotic Object can be directly observed either when using `import * as m from 'cjs'` or a dynamic import:
```
import * as m from 'cjs';
console.log(m);
console.log(m === await import('cjs'));
// Prints:
//   [Module] { default: <module.exports>, 'module.exports': <module.exports> }
//   true
copy
```

For better compatibility with existing usage in the JS ecosystem, Node.js in addition attempts to determine the CommonJS named exports of every imported CommonJS module to provide them as separate ES module exports using a static analysis process.
For example, consider a CommonJS module written:
```
// cjs.cjs
exports.name = 'exported';
copy
```

The preceding module supports named imports in ES modules:
```
import { name } from './cjs.cjs';
console.log(name);
// Prints: 'exported'

import cjs from './cjs.cjs';
console.log(cjs);
// Prints: { name: 'exported' }

import * as m from './cjs.cjs';
console.log(m);
// Prints:
//   [Module] {
//     default: { name: 'exported' },
//     'module.exports': { name: 'exported' },
//     name: 'exported'
//   }
copy
```

As can be seen from the last example of the Module Namespace Exotic Object being logged, the `name` export is copied off of the `module.exports` object and set directly on the ES module namespace when the module is imported.
Live binding updates or new exports added to `module.exports` are not detected for these named exports.
The detection of named exports is based on common syntax patterns but does not always correctly detect named exports. In these cases, using the default import form described above can be a better option.
Named exports detection covers many common export patterns, reexport patterns and build tool and transpiler outputs. See
#### Differences between ES modules and CommonJS[#](https://nodejs.org/docs/latest/api/esm.html#differences-between-es-modules-and-commonjs)
##### No `require`, `exports`, or `module.exports`[#](https://nodejs.org/docs/latest/api/esm.html#no-require-exports-or-moduleexports)
In most cases, the ES module `import` can be used to load CommonJS modules.
If needed, a `require` function can be constructed within an ES module using [`module.createRequire()`](https://nodejs.org/docs/latest/api/module.html#modulecreaterequirefilename).
##### No `__filename` or `__dirname`[#](https://nodejs.org/docs/latest/api/esm.html#no-filename-or-dirname)
These CommonJS variables are not available in ES modules.
`__filename` and `__dirname` use cases can be replicated via [`import.meta.filename`](https://nodejs.org/docs/latest/api/esm.html#importmetafilename) and [`import.meta.dirname`](https://nodejs.org/docs/latest/api/esm.html#importmetadirname).
##### No Addon Loading[#](https://nodejs.org/docs/latest/api/esm.html#no-addon-loading)
[Addons](https://nodejs.org/docs/latest/api/addons.html) are not currently supported with ES module imports.
They can instead be loaded with [`module.createRequire()`](https://nodejs.org/docs/latest/api/module.html#modulecreaterequirefilename) or [`process.dlopen`](https://nodejs.org/docs/latest/api/process.html#processdlopenmodule-filename-flags).
##### No `require.main`[#](https://nodejs.org/docs/latest/api/esm.html#no-requiremain)
To replace `require.main === module`, there is the [`import.meta.main`](https://nodejs.org/docs/latest/api/esm.html#importmetamain) API.
##### No `require.resolve`[#](https://nodejs.org/docs/latest/api/esm.html#no-requireresolve)
Relative resolution can be handled via `new URL('./local', import.meta.url)`.
For a complete `require.resolve` replacement, there is the [import.meta.resolve](https://nodejs.org/docs/latest/api/esm.html#importmetaresolvespecifier) API.
Alternatively `module.createRequire()` can be used.
##### No `NODE_PATH`[#](https://nodejs.org/docs/latest/api/esm.html#no-node-path)
`NODE_PATH` is not part of resolving `import` specifiers. Please use symlinks if this behavior is desired.
##### No `require.extensions`[#](https://nodejs.org/docs/latest/api/esm.html#no-requireextensions)
`require.extensions` is not used by `import`. Module customization hooks can provide a replacement.
##### No `require.cache`[#](https://nodejs.org/docs/latest/api/esm.html#no-requirecache)
`require.cache` is not used by `import` as the ES module loader has its own separate cache.
### JSON modules[#](https://nodejs.org/docs/latest/api/esm.html#json-modules)
History Version | Changes
---|---
v23.1.0, v22.12.0, v20.18.3, v18.20.5 | JSON modules are no longer experimental.
JSON files can be referenced by `import`:
```
import packageConfig from './package.json' with { type: 'json' };
copy
```

The `with { type: 'json' }` syntax is mandatory; see [Import Attributes](https://nodejs.org/docs/latest/api/esm.html#import-attributes).
The imported JSON only exposes a `default` export. There is no support for named exports. A cache entry is created in the CommonJS cache to avoid duplication. The same object is returned in CommonJS if the JSON module has already been imported from the same path.
### Wasm modules[#](https://nodejs.org/docs/latest/api/esm.html#wasm-modules)
History Version | Changes
---|---
v24.5.0, v22.19.0 | Wasm modules no longer require the `--experimental-wasm-modules` flag.
Importing both WebAssembly module instances and WebAssembly source phase imports is supported.
Both of these integrations are in line with the
#### Wasm Source Phase Imports[#](https://nodejs.org/docs/latest/api/esm.html#wasm-source-phase-imports)
Added in: v24.0.0
Stability: 1.2 - Release candidate
The `import source` keyword combination to import a `WebAssembly.Module` object directly, instead of getting a module instance already instantiated with its dependencies.
This is useful when needing custom instantiations for Wasm, while still resolving and loading it through the ES module integration.
For example, to create multiple instances of a module, or to pass custom imports into a new instance of `library.wasm`:
```
import source libraryModule from './library.wasm';

const instance1 = await WebAssembly.instantiate(libraryModule, importObject1);

const instance2 = await WebAssembly.instantiate(libraryModule, importObject2);
copy
```

In addition to the static source phase, there is also a dynamic variant of the source phase via the `import.source` dynamic phase import syntax:
```
const dynamicLibrary = await import.source('./library.wasm');

const instance = await WebAssembly.instantiate(dynamicLibrary, importObject);
copy
```

#### JavaScript String Builtins[#](https://nodejs.org/docs/latest/api/esm.html#javascript-string-builtins)
Added in: v24.5.0, v22.19.0
Stability: 1.2 - Release candidate
When importing WebAssembly modules, the `wasm:js-string` namespace.
For example, the following Wasm module exports a string `getLength` function using the `wasm:js-string` `length` builtin:
```
(module
  ;; Compile-time import of the string length builtin.
  (import "wasm:js-string" "length" (func $string_length (param externref) (result i32)))

  ;; Define getLength, taking a JS value parameter assumed to be a string,
  ;; calling string length on it and returning the result.
  (func $getLength (param $str externref) (result i32)
    local.get $str
    call $string_length
  )

  ;; Export the getLength function.
  (export "getLength" (func $get_length))
)
copy
```
```
import { getLength } from './string-len.wasm';
getLength('foo'); // Returns 3.
copy
```

Wasm builtins are compile-time imports that are linked during module compilation rather than during instantiation. They do not behave like normal module graph imports and they cannot be inspected via `WebAssembly.Module.imports(mod)` or virtualized unless recompiling the module using the direct `WebAssembly.compile` API with string builtins disabled.
Importing a module in the source phase before it has been instantiated will also use the compile-time builtins automatically:
```
import source mod from './string-len.wasm';
const { exports: { getLength } } = await WebAssembly.instantiate(mod, {});
getLength('foo'); // Also returns 3.
copy
```

#### Wasm Instance Phase Imports[#](https://nodejs.org/docs/latest/api/esm.html#wasm-instance-phase-imports)
Stability: 1.1 - Active development
Instance imports allow any `.wasm` files to be imported as normal modules, supporting their module imports in turn.
For example, an `index.js` containing:
```
import * as M from './library.wasm';
console.log(M);
copy
```

executed under:
```
node index.mjs
copy
```

would provide the exports interface for the instantiation of `library.wasm`.
#### Reserved Wasm Namespaces[#](https://nodejs.org/docs/latest/api/esm.html#reserved-wasm-namespaces)
Added in: v24.5.0, v22.19.0
When importing WebAssembly module instances, they cannot use import module names or import/export names that start with reserved prefixes:
  * `wasm-js:` - reserved in all module import names, module names and export names.
  * `wasm:` - reserved in module import names and export names (imported module names are allowed in order to support future builtin polyfills).


Importing a module using the above reserved names will throw a `WebAssembly.LinkError`.
### Top-level `await`[#](https://nodejs.org/docs/latest/api/esm.html#top-level-await)
Added in: v14.8.0
The `await` keyword may be used in the top level body of an ECMAScript module.
Assuming an `a.mjs` with
```
export const five = await Promise.resolve(5);
copy
```

And a `b.mjs` with
```
import { five } from './a.mjs';

console.log(five); // Logs `5`
copy
```
```
node b.mjs # works
copy
```

If a top level `await` expression never resolves, the `node` process will exit with a `13` [status code](https://nodejs.org/docs/latest/api/process.html#exit-codes).
```
import { spawn } from 'node:child_process';
import { execPath } from 'node:process';

spawn(execPath, [
  '--input-type=module',
  '--eval',
  // Never-resolving Promise:
  'await new Promise(() => {})',
]).once('exit', (code) => {
  console.log(code); // Logs `13`
});
copy
```

### Loaders[#](https://nodejs.org/docs/latest/api/esm.html#loaders)
The former Loaders documentation is now at [Modules: Customization hooks](https://nodejs.org/docs/latest/api/module.html#customization-hooks).
### Resolution and loading algorithm[#](https://nodejs.org/docs/latest/api/esm.html#resolution-and-loading-algorithm)
#### Features[#](https://nodejs.org/docs/latest/api/esm.html#features)
The default resolver has the following properties:
  * FileURL-based resolution as is used by ES modules
  * Relative and absolute URL resolution
  * No default extensions
  * No folder mains
  * Bare specifier package resolution lookup through node_modules
  * Does not fail on unknown extensions or protocols
  * Can optionally provide a hint of the format to the loading phase


The default loader has the following properties
  * Support for builtin module loading via `node:` URLs
  * Support for "inline" module loading via `data:` URLs
  * Support for `file:` module loading
  * Fails on any other URL protocol
  * Fails on unknown extensions for `file:` loading (supports only `.cjs`, `.js`, and `.mjs`)


#### Resolution algorithm[#](https://nodejs.org/docs/latest/api/esm.html#resolution-algorithm)
The algorithm to load an ES module specifier is given through the **ESM_RESOLVE** method below. It returns the resolved URL for a module specifier relative to a parentURL.
The resolution algorithm determines the full resolved URL for a module load, along with its suggested module format. The resolution algorithm does not determine whether the resolved URL protocol can be loaded, or whether the file extensions are permitted, instead these validations are applied by Node.js during the load phase (for example, if it was asked to load a URL that has a protocol that is not `file:`, `data:` or `node:`.
The algorithm also tries to determine the format of the file based on the extension (see `ESM_FILE_FORMAT` algorithm below). If it does not recognize the file extension (eg if it is not `.mjs`, `.cjs`, or `.json`), then a format of `undefined` is returned, which will throw during the load phase.
The algorithm to determine the module format of a resolved URL is provided by **ESM_FILE_FORMAT** , which returns the unique module format for any file. The _"module"_ format is returned for an ECMAScript Module, while the _"commonjs"_ format is used to indicate loading through the legacy CommonJS loader. Additional formats such as _"addon"_ can be extended in future updates.
In the following algorithms, all subroutine errors are propagated as errors of these top-level routines unless stated otherwise.
_defaultConditions_ is the conditional environment name array, `["node", "import"]`.
The resolver can throw the following errors:
  * _Invalid Module Specifier_ : Module specifier is an invalid URL, package name or package subpath specifier.
  * _Invalid Package Configuration_ : package.json configuration is invalid or contains an invalid configuration.
  * _Invalid Package Target_ : Package exports or imports define a target module for the package that is an invalid type or string target.
  * _Package Path Not Exported_ : Package exports do not define or permit a target subpath in the package for the given module.
  * _Package Import Not Defined_ : Package imports do not define the specifier.
  * _Module Not Found_ : The package or module requested does not exist.
  * _Unsupported Directory Import_ : The resolved path corresponds to a directory, which is not a supported target for module imports.


#### Resolution Algorithm Specification[#](https://nodejs.org/docs/latest/api/esm.html#resolution-algorithm-specification)
**ESM_RESOLVE**(_specifier_ , _parentURL_)
>   1. Let _resolved_ be **undefined**.
>   2. If _specifier_ is a valid URL, then
>     1. Set _resolved_ to the result of parsing and reserializing _specifier_ as a URL.
>   3. Otherwise, if _specifier_ starts with _"/"_ , _"./"_ , or _"../"_ , then
>     1. Set _resolved_ to the URL resolution of _specifier_ relative to _parentURL_.
>   4. Otherwise, if _specifier_ starts with _"#"_ , then
>     1. Set _resolved_ to the result of **PACKAGE_IMPORTS_RESOLVE**(_specifier_ , _parentURL_ , _defaultConditions_).
>   5. Otherwise,
>     1. Note: _specifier_ is now a bare specifier.
>     2. Set _resolved_ the result of **PACKAGE_RESOLVE**(_specifier_ , _parentURL_).
>   6. Let _format_ be **undefined**.
>   7. If _resolved_ is a _"file:"_ URL, then
>     1. If _resolved_ contains any percent encodings of _"/"_ or _"\"_ (_"%2F"_ and _"%5C"_ respectively), then
>       1. Throw an _Invalid Module Specifier_ error.
>     2. If the file at _resolved_ is a directory, then
>       1. Throw an _Unsupported Directory Import_ error.
>     3. If the file at _resolved_ does not exist, then
>       1. Throw a _Module Not Found_ error.
>     4. Set _resolved_ to the real path of _resolved_ , maintaining the same URL querystring and fragment components.
>     5. Set _format_ to the result of **ESM_FILE_FORMAT**(_resolved_).
>   8. Otherwise,
>     1. Set _format_ the module format of the content type associated with the URL _resolved_.
>   9. Return _format_ and _resolved_ to the loading phase
>

**PACKAGE_RESOLVE**(_packageSpecifier_ , _parentURL_)
>   1. Let _packageName_ be **undefined**.
>   2. If _packageSpecifier_ is an empty string, then
>     1. Throw an _Invalid Module Specifier_ error.
>   3. If _packageSpecifier_ is a Node.js builtin module name, then
>     1. Return the string _"node:"_ concatenated with _packageSpecifier_.
>   4. If _packageSpecifier_ does not start with _"@"_ , then
>     1. Set _packageName_ to the substring of _packageSpecifier_ until the first _"/"_ separator or the end of the string.
>   5. Otherwise,
>     1. If _packageSpecifier_ does not contain a _"/"_ separator, then
>       1. Throw an _Invalid Module Specifier_ error.
>     2. Set _packageName_ to the substring of _packageSpecifier_ until the second _"/"_ separator or the end of the string.
>   6. If _packageName_ starts with _"."_ or contains _"\"_ or _"%"_ , then
>     1. Throw an _Invalid Module Specifier_ error.
>   7. Let _packageSubpath_ be _"."_ concatenated with the substring of _packageSpecifier_ from the position at the length of _packageName_.
>   8. Let _selfUrl_ be the result of **PACKAGE_SELF_RESOLVE**(_packageName_ , _packageSubpath_ , _parentURL_).
>   9. If _selfUrl_ is not **undefined** , return _selfUrl_.
>   10. While _parentURL_ is not the file system root,
>     1. Let _packageURL_ be the URL resolution of _"node_modules/"_ concatenated with _packageName_ , relative to _parentURL_.
>     2. Set _parentURL_ to the parent folder URL of _parentURL_.
>     3. If the folder at _packageURL_ does not exist, then
>       1. Continue the next loop iteration.
>     4. Let _pjson_ be the result of **READ_PACKAGE_JSON**(_packageURL_).
>     5. If _pjson_ is not **null** and _pjson_._exports_ is not **null** or **undefined** , then
>       1. Return the result of **PACKAGE_EXPORTS_RESOLVE**(_packageURL_ , _packageSubpath_ , _pjson.exports_ , _defaultConditions_).
>     6. Otherwise, if _packageSubpath_ is equal to _"."_ , then
>       1. If _pjson.main_ is a string, then
>         1. Return the URL resolution of _main_ in _packageURL_.
>     7. Otherwise,
>       1. Return the URL resolution of _packageSubpath_ in _packageURL_.
>   11. Throw a _Module Not Found_ error.
>

**PACKAGE_SELF_RESOLVE**(_packageName_ , _packageSubpath_ , _parentURL_)
>   1. Let _packageURL_ be the result of **LOOKUP_PACKAGE_SCOPE**(_parentURL_).
>   2. If _packageURL_ is **null** , then
>     1. Return **undefined**.
>   3. Let _pjson_ be the result of **READ_PACKAGE_JSON**(_packageURL_).
>   4. If _pjson_ is **null** or if _pjson_._exports_ is **null** or **undefined** , then
>     1. Return **undefined**.
>   5. If _pjson.name_ is equal to _packageName_ , then
>     1. Return the result of **PACKAGE_EXPORTS_RESOLVE**(_packageURL_ , _packageSubpath_ , _pjson.exports_ , _defaultConditions_).
>   6. Otherwise, return **undefined**.
>

**PACKAGE_EXPORTS_RESOLVE**(_packageURL_ , _subpath_ , _exports_ , _conditions_)
Note: This function is directly invoked by the CommonJS resolution algorithm.
>   1. If _exports_ is an Object with both a key starting with _"."_ and a key not starting with _"."_ , throw an _Invalid Package Configuration_ error.
>   2. If _subpath_ is equal to _"."_ , then
>     1. Let _mainExport_ be **undefined**.
>     2. If _exports_ is a String or Array, or an Object containing no keys starting with _"."_ , then
>       1. Set _mainExport_ to _exports_.
>     3. Otherwise if _exports_ is an Object containing a _"."_ property, then
>       1. Set _mainExport_ to _exports_[_"."_].
>     4. If _mainExport_ is not **undefined** , then
>       1. Let _resolved_ be the result of **PACKAGE_TARGET_RESOLVE**( _packageURL_ , _mainExport_ , **null** , **false** , _conditions_).
>       2. If _resolved_ is not **null** or **undefined** , return _resolved_.
>   3. Otherwise, if _exports_ is an Object and all keys of _exports_ start with _"."_ , then
>     1. Assert: _subpath_ begins with _"./"_.
>     2. Let _resolved_ be the result of **PACKAGE_IMPORTS_EXPORTS_RESOLVE**( _subpath_ , _exports_ , _packageURL_ , **false** , _conditions_).
>     3. If _resolved_ is not **null** or **undefined** , return _resolved_.
>   4. Throw a _Package Path Not Exported_ error.
>

**PACKAGE_IMPORTS_RESOLVE**(_specifier_ , _parentURL_ , _conditions_)
Note: This function is directly invoked by the CommonJS resolution algorithm.
>   1. Assert: _specifier_ begins with _"#"_.
>   2. If _specifier_ is exactly equal to _"#"_ , then
>     1. Throw an _Invalid Module Specifier_ error.
>   3. Let _packageURL_ be the result of **LOOKUP_PACKAGE_SCOPE**(_parentURL_).
>   4. If _packageURL_ is not **null** , then
>     1. Let _pjson_ be the result of **READ_PACKAGE_JSON**(_packageURL_).
>     2. If _pjson.imports_ is a non-null Object, then
>       1. Let _resolved_ be the result of **PACKAGE_IMPORTS_EXPORTS_RESOLVE**( _specifier_ , _pjson.imports_ , _packageURL_ , **true** , _conditions_).
>       2. If _resolved_ is not **null** or **undefined** , return _resolved_.
>   5. Throw a _Package Import Not Defined_ error.
>

**PACKAGE_IMPORTS_EXPORTS_RESOLVE**(_matchKey_ , _matchObj_ , _packageURL_ , _isImports_ , _conditions_)
>   1. If _matchKey_ ends in _"/"_ , then
>     1. Throw an _Invalid Module Specifier_ error.
>   2. If _matchKey_ is a key of _matchObj_ and does not contain _"*"_ , then
>     1. Let _target_ be the value of _matchObj_[_matchKey_].
>     2. Return the result of **PACKAGE_TARGET_RESOLVE**(_packageURL_ , _target_ , **null** , _isImports_ , _conditions_).
>   3. Let _expansionKeys_ be the list of keys of _matchObj_ containing only a single _"*"_ , sorted by the sorting function **PATTERN_KEY_COMPARE** which orders in descending order of specificity.
>   4. For each key _expansionKey_ in _expansionKeys_ , do
>     1. Let _patternBase_ be the substring of _expansionKey_ up to but excluding the first _"*"_ character.
>     2. If _matchKey_ starts with but is not equal to _patternBase_ , then
>       1. Let _patternTrailer_ be the substring of _expansionKey_ from the index after the first _"*"_ character.
>       2. If _patternTrailer_ has zero length, or if _matchKey_ ends with _patternTrailer_ and the length of _matchKey_ is greater than or equal to the length of _expansionKey_ , then
>         1. Let _target_ be the value of _matchObj_[_expansionKey_].
>         2. Let _patternMatch_ be the substring of _matchKey_ starting at the index of the length of _patternBase_ up to the length of _matchKey_ minus the length of _patternTrailer_.
>         3. Return the result of **PACKAGE_TARGET_RESOLVE**(_packageURL_ , _target_ , _patternMatch_ , _isImports_ , _conditions_).
>   5. Return **null**.
>

**PATTERN_KEY_COMPARE**(_keyA_ , _keyB_)
>   1. Assert: _keyA_ contains only a single _"*"_.
>   2. Assert: _keyB_ contains only a single _"*"_.
>   3. Let _baseLengthA_ be the index of _"*"_ in _keyA_.
>   4. Let _baseLengthB_ be the index of _"*"_ in _keyB_.
>   5. If _baseLengthA_ is greater than _baseLengthB_ , return -1.
>   6. If _baseLengthB_ is greater than _baseLengthA_ , return 1.
>   7. If the length of _keyA_ is greater than the length of _keyB_ , return -1.
>   8. If the length of _keyB_ is greater than the length of _keyA_ , return 1.
>   9. Return 0.
>

**PACKAGE_TARGET_RESOLVE**(_packageURL_ , _target_ , _patternMatch_ , _isImports_ , _conditions_)
>   1. If _target_ is a String, then
>     1. If _target_ does not start with _"./"_ , then
>       1. If _isImports_ is **false** , or if _target_ starts with _"../"_ or _"/"_ , or if _target_ is a valid URL, then
>         1. Throw an _Invalid Package Target_ error.
>       2. If _patternMatch_ is a String, then
>         1. Return **PACKAGE_RESOLVE**(_target_ with every instance of _"*"_ replaced by _patternMatch_ , _packageURL_ + _"/"_).
>       3. Return **PACKAGE_RESOLVE**(_target_ , _packageURL_ + _"/"_).
>     2. If _target_ split on _"/"_ or _"\"_ contains any _""_ , _"."_ , _".."_ , or _"node_modules"_ segments after the first _"."_ segment, case insensitive and including percent encoded variants, throw an _Invalid Package Target_ error.
>     3. Let _resolvedTarget_ be the URL resolution of the concatenation of _packageURL_ and _target_.
>     4. Assert: _packageURL_ is contained in _resolvedTarget_.
>     5. If _patternMatch_ is **null** , then
>       1. Return _resolvedTarget_.
>     6. If _patternMatch_ split on _"/"_ or _"\"_ contains any _""_ , _"."_ , _".."_ , or _"node_modules"_ segments, case insensitive and including percent encoded variants, throw an _Invalid Module Specifier_ error.
>     7. Return the URL resolution of _resolvedTarget_ with every instance of _"*"_ replaced with _patternMatch_.
>   2. Otherwise, if _target_ is a non-null Object, then
>     1. If _target_ contains any index property keys, as defined in ECMA-262 _Invalid Package Configuration_ error.
>     2. For each property _p_ of _target_ , in object insertion order as,
>       1. If _p_ equals _"default"_ or _conditions_ contains an entry for _p_ , then
>         1. Let _targetValue_ be the value of the _p_ property in _target_.
>         2. Let _resolved_ be the result of **PACKAGE_TARGET_RESOLVE**( _packageURL_ , _targetValue_ , _patternMatch_ , _isImports_ , _conditions_).
>         3. If _resolved_ is equal to **undefined** , continue the loop.
>         4. Return _resolved_.
>     3. Return **undefined**.
>   3. Otherwise, if _target_ is an Array, then
>     1. If _target.length is zero, return **null**.
>     2. For each item _targetValue_ in _target_ , do
>       1. Let _resolved_ be the result of **PACKAGE_TARGET_RESOLVE**( _packageURL_ , _targetValue_ , _patternMatch_ , _isImports_ , _conditions_), continuing the loop on any _Invalid Package Target_ error.
>       2. If _resolved_ is **undefined** , continue the loop.
>       3. Return _resolved_.
>     3. Return or throw the last fallback resolution **null** return or error.
>   4. Otherwise, if _target_ is _null_ , return **null**.
>   5. Otherwise throw an _Invalid Package Target_ error.
>

**ESM_FILE_FORMAT**(_url_)
>   1. Assert: _url_ corresponds to an existing file.
>   2. If _url_ ends in _".mjs"_ , then
>     1. Return _"module"_.
>   3. If _url_ ends in _".cjs"_ , then
>     1. Return _"commonjs"_.
>   4. If _url_ ends in _".json"_ , then
>     1. Return _"json"_.
>   5. If _url_ ends in _".wasm"_ , then
>     1. Return _"wasm"_.
>   6. If `--experimental-addon-modules` is enabled and _url_ ends in _".node"_ , then
>     1. Return _"addon"_.
>   7. Let _packageURL_ be the result of **LOOKUP_PACKAGE_SCOPE**(_url_).
>   8. Let _pjson_ be the result of **READ_PACKAGE_JSON**(_packageURL_).
>   9. Let _packageType_ be **null**.
>   10. If _pjson?.type_ is _"module"_ or _"commonjs"_ , then
>     1. Set _packageType_ to _pjson.type_.
>   11. If _url_ ends in _".js"_ , then
>     1. If _packageType_ is not **null** , then
>       1. Return _packageType_.
>     2. If the result of **DETECT_MODULE_SYNTAX**(_source_) is true, then
>       1. Return _"module"_.
>     3. Return _"commonjs"_.
>   12. If _url_ does not have any extension, then
>     1. If _packageType_ is _"module"_ and the file at _url_ contains the "application/wasm" content type header for a WebAssembly module, then
>       1. Return _"wasm"_.
>     2. If _packageType_ is not **null** , then
>       1. Return _packageType_.
>     3. If the result of **DETECT_MODULE_SYNTAX**(_source_) is true, then
>       1. Return _"module"_.
>     4. Return _"commonjs"_.
>   13. Return **undefined** (will throw during load phase).
>

**LOOKUP_PACKAGE_SCOPE**(_url_)
>   1. Let _scopeURL_ be _url_.
>   2. While _scopeURL_ is not the file system root,
>     1. Set _scopeURL_ to the parent URL of _scopeURL_.
>     2. If _scopeURL_ ends in a _"node_modules"_ path segment, return **null**.
>     3. Let _pjsonURL_ be the resolution of _"package.json"_ within _scopeURL_.
>     4. if the file at _pjsonURL_ exists, then
>       1. Return _scopeURL_.
>   3. Return **null**.
>

**READ_PACKAGE_JSON**(_packageURL_)
>   1. Let _pjsonURL_ be the resolution of _"package.json"_ within _packageURL_.
>   2. If the file at _pjsonURL_ does not exist, then
>     1. Return **null**.
>   3. If the file at _packageURL_ does not parse as valid JSON, then
>     1. Throw an _Invalid Package Configuration_ error.
>   4. Return the parsed JSON source of the file at _pjsonURL_.
>

**DETECT_MODULE_SYNTAX**(_source_)
>   1. Parse _source_ as an ECMAScript module.
>   2. If the parse is successful, then
>     1. If _source_ contains top-level `await`, static `import` or `export` statements, or `import.meta`, return **true**.
>     2. If _source_ contains a top-level lexical declaration (`const`, `let`, or `class`) of any of the CommonJS wrapper variables (`require`, `exports`, `module`, `__filename`, or `__dirname`) then return **true**.
>   3. Return **false**.
>

#### Customizing ESM specifier resolution algorithm[#](https://nodejs.org/docs/latest/api/esm.html#customizing-esm-specifier-resolution-algorithm)
[Module customization hooks](https://nodejs.org/docs/latest/api/module.html#customization-hooks) provide a mechanism for customizing the ESM specifier resolution algorithm. An example that provides CommonJS-style resolution for ESM specifiers is
