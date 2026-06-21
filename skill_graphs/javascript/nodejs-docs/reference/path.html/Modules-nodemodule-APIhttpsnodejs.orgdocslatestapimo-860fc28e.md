  transferList: [port2],
});
copy
```

##### Asynchronous `resolve(specifier, context, nextResolve)`[#](https://nodejs.org/docs/latest/api/module.html#asynchronous-resolvespecifier-context-nextresolve)
History Version | Changes
---|---
v21.0.0, v20.10.0, v18.19.0 | The property `context.importAssertions` is replaced with `context.importAttributes`. Using the old name is still supported and will emit an experimental warning.
v18.6.0, v16.17.0 | Add support for chaining resolve hooks. Each hook must either call `nextResolve()` or include a `shortCircuit` property set to `true` in its return.
v17.1.0, v16.14.0 | Add support for import assertions.
  * `specifier`
  * `context`
    * `conditions` `package.json`
    * `importAttributes`
    * `parentURL`
  * `nextResolve` `resolve` hook in the chain, or the Node.js default `resolve` hook after the last user-supplied `resolve` hook
    * `specifier`
    * `context`
  * Returns: `Promise` that will resolve to such an object.
    * `format` `load` hook (it might be ignored). It can be a module format (such as `'commonjs'` or `'module'`) or an arbitrary value like `'css'` or `'yaml'`.
    * `importAttributes`
    * `shortCircuit` `resolve` hooks. **Default:** `false`
    * `url`


The asynchronous version works similarly to the synchronous version, only that the `nextResolve` function returns a `Promise`, and the `resolve` hook itself can return a `Promise`.
> **Warning** In the case of the asynchronous version, despite support for returning promises and async functions, calls to `resolve` may still block the main thread which can impact performance.
> **Warning** The `resolve` hook invoked for `require()` calls inside CommonJS modules customized by asynchronous hooks does not receive the original specifier passed to `require()`. Instead, it receives a URL already fully resolved using the default CommonJS resolution.
> **Warning** In the CommonJS modules that are customized by the asynchronous customization hooks, `require.resolve()` and `require()` will use `"import"` export condition instead of `"require"`, which may cause unexpected behaviors when loading dual packages.
```
export async function resolve(specifier, context, nextResolve) {
  // When calling `defaultResolve`, the arguments can be modified. For example,
  // to change the specifier or add conditions.
  if (specifier.includes('foo')) {
    specifier = specifier.replace('foo', 'bar');
    return nextResolve(specifier, {
      ...context,
      conditions: [...context.conditions, 'another-condition'],
    });
  }

  // The hook can also skips default resolution and provide a custom URL.
  if (specifier === 'special-module') {
    return {
      url: 'file:///path/to/special-module.mjs',
      format: 'module',
      shortCircuit: true,  // This is mandatory if not calling nextResolve().
    };
  }

  // If no customization is needed, defer to the next hook in the chain which would be the
  // Node.js default resolve if this is the last user-specified loader.
  return nextResolve(specifier);
}
copy
```

##### Asynchronous `load(url, context, nextLoad)`[#](https://nodejs.org/docs/latest/api/module.html#asynchronous-loadurl-context-nextload)
History Version | Changes
---|---
v22.6.0 | Add support for `source` with format `commonjs-typescript` and `module-typescript`.
v20.6.0 | Add support for `source` with format `commonjs`.
v18.6.0, v16.17.0 | Add support for chaining load hooks. Each hook must either call `nextLoad()` or include a `shortCircuit` property set to `true` in its return.
  * `url` `resolve` chain
  * `context`
    * `conditions` `package.json`
    * `format` `resolve` hook chain. This can be any string value as an input; input values do not need to conform to the list of acceptable return values described below.
    * `importAttributes`
  * `nextLoad` `load` hook in the chain, or the Node.js default `load` hook after the last user-supplied `load` hook
    * `url`
    * `context` `nextLoad`, if the module pointed to by `url` does not have explicit module type information, `context.format` is mandatory.
  * Returns: `Promise` that will resolve to such an object.
    * `format`
    * `shortCircuit` `load` hooks. **Default:** `false`
    * `source`


> **Warning** : The asynchronous `load` hook and namespaced exports from CommonJS modules are incompatible. Attempting to use them together will result in an empty object from the import. This may be addressed in the future. This does not apply to the synchronous `load` hook, in which case exports can be used as usual.
The asynchronous version works similarly to the synchronous version, though when using the asynchronous `load` hook, omitting vs providing a `source` for `'commonjs'` has very different effects:
  * When a `source` is provided, all `require` calls from this module will be processed by the ESM loader with registered `resolve` and `load` hooks; all `require.resolve` calls from this module will be processed by the ESM loader with registered `resolve` hooks; only a subset of the CommonJS API will be available (e.g. no `require.extensions`, no `require.cache`, no `require.resolve.paths`) and monkey-patching on the CommonJS module loader will not apply.
  * If `source` is undefined or `null`, it will be handled by the CommonJS module loader and `require`/`require.resolve` calls will not go through the registered hooks. This behavior for nullish `source` is temporary — in the future, nullish `source` will not be supported.


These caveats do not apply to the synchronous `load` hook, in which case the complete set of CommonJS APIs available to the customized CommonJS modules, and `require`/`require.resolve` always go through the registered hooks.
The Node.js internal asynchronous `load` implementation, which is the value of `next` for the last hook in the `load` chain, returns `null` for `source` when `format` is `'commonjs'` for backward compatibility. Here is an example hook that would opt-in to using the non-default behavior:
```
import { readFile } from 'node:fs/promises';

// Asynchronous version accepted by module.register(). This fix is not needed
// for the synchronous version accepted by module.registerHooks().
export async function load(url, context, nextLoad) {
  const result = await nextLoad(url, context);
  if (result.format === 'commonjs') {
    result.source ??= await readFile(new URL(result.responseURL ?? url));
  }
  return result;
}
copy
```

This doesn't apply to the synchronous `load` hook either, in which case the `source` returned contains source code loaded by the next hook, regardless of module format.
#### Examples[#](https://nodejs.org/docs/latest/api/module.html#examples)
The various module customization hooks can be used together to accomplish wide-ranging customizations of the Node.js code loading and evaluation behaviors.
##### Import from HTTPS[#](https://nodejs.org/docs/latest/api/module.html#import-from-https)
The hook below registers hooks to enable rudimentary support for such specifiers. While this may seem like a significant improvement to Node.js core functionality, there are substantial downsides to actually using these hooks: performance is much slower than loading files from disk, there is no caching, and there is no security.
```
// https-hooks.mjs
import { get } from 'node:https';

export function load(url, context, nextLoad) {
  // For JavaScript to be loaded over the network, we need to fetch and
  // return it.
  if (url.startsWith('https://')) {
    return new Promise((resolve, reject) => {
      get(url, (res) => {
        let data = '';
        res.setEncoding('utf8');
        res.on('data', (chunk) => data += chunk);
        res.on('end', () => resolve({
          // This example assumes all network-provided JavaScript is ES module
          // code.
          format: 'module',
          shortCircuit: true,
          source: data,
        }));
      }).on('error', (err) => reject(err));
    });
  }

  // Let Node.js handle all other URLs.
  return nextLoad(url);
}
// main.mjs
import { VERSION } from 'https://coffeescript.org/browser-compiler-modern/coffeescript.js';

console.log(VERSION);
copy
```

With the preceding hooks module, running `node --import 'data:text/javascript,import { register } from "node:module"; import { pathToFileURL } from "node:url"; register(pathToFileURL("./https-hooks.mjs"));' ./main.mjs` prints the current version of CoffeeScript per the module at the URL in `main.mjs`.
##### Transpilation[#](https://nodejs.org/docs/latest/api/module.html#transpilation)
Sources that are in formats Node.js doesn't understand can be converted into JavaScript using the [`load` hook](https://nodejs.org/docs/latest/api/module.html#synchronous-loadurl-context-nextload).
This is less performant than transpiling source files before running Node.js; transpiler hooks should only be used for development and testing purposes.
###### Asynchronous version[#](https://nodejs.org/docs/latest/api/module.html#asynchronous-version)
```
// coffeescript-hooks.mjs
import { readFile } from 'node:fs/promises';
import { findPackageJSON } from 'node:module';
import coffeescript from 'coffeescript';

const extensionsRegex = /\.(coffee|litcoffee|coffee\.md)$/;

export async function load(url, context, nextLoad) {
  if (extensionsRegex.test(url)) {
    // CoffeeScript files can be either CommonJS or ES modules. Use a custom format
    // to tell Node.js not to detect its module type.
    const { source: rawSource } = await nextLoad(url, { ...context, format: 'coffee' });
    // This hook converts CoffeeScript source code into JavaScript source code
    // for all imported CoffeeScript files.
    const transformedSource = coffeescript.compile(rawSource.toString(), url);

    // To determine how Node.js would interpret the transpilation result,
    // search up the file system for the nearest parent package.json file
    // and read its "type" field.
    return {
      format: await getPackageType(url),
      shortCircuit: true,
      source: transformedSource,
    };
  }

  // Let Node.js handle all other URLs.
  return nextLoad(url, context);
}

async function getPackageType(url) {
  // `url` is only a file path during the first iteration when passed the
  // resolved url from the load() hook
  // an actual file path from load() will contain a file extension as it's
  // required by the spec
  // this simple truthy check for whether `url` contains a file extension will
  // work for most projects but does not cover some edge-cases (such as
  // extensionless files or a url ending in a trailing space)
  const pJson = findPackageJSON(url);

  return readFile(pJson, 'utf8')
    .then(JSON.parse)
    .then((json) => json?.type)
    .catch(() => undefined);
}
copy
```

###### Synchronous version[#](https://nodejs.org/docs/latest/api/module.html#synchronous-version)
```
// coffeescript-sync-hooks.mjs
import { readFileSync } from 'node:fs';
import { registerHooks, findPackageJSON } from 'node:module';
import coffeescript from 'coffeescript';

const extensionsRegex = /\.(coffee|litcoffee|coffee\.md)$/;

function load(url, context, nextLoad) {
  if (extensionsRegex.test(url)) {
    const { source: rawSource } = nextLoad(url, { ...context, format: 'coffee' });
    const transformedSource = coffeescript.compile(rawSource.toString(), url);

    return {
      format: getPackageType(url),
      shortCircuit: true,
      source: transformedSource,
    };
  }

  return nextLoad(url, context);
}

function getPackageType(url) {
  const pJson = findPackageJSON(url);
  if (!pJson) {
    return undefined;
  }
  try {
    const file = readFileSync(pJson, 'utf-8');
    return JSON.parse(file)?.type;
  } catch {
    return undefined;
  }
}

registerHooks({ load });
copy
```

##### Running hooks[#](https://nodejs.org/docs/latest/api/module.html#running-hooks)
```
# main.coffee
import { scream } from './scream.coffee'
console.log scream 'hello, world'

import { version } from 'node:process'
console.log "Brought to you by Node.js version #{version}"
copy
```
```
# scream.coffee
export scream = (str) -> str.toUpperCase()
copy
```

For the sake of running the example, add a `package.json` file containing the module type of the CoffeeScript files.
```
{
  "type": "module"
}
copy
```

This is only for running the example. In real world loaders, `getPackageType()` must be able to return an `format` known to Node.js even in the absence of an explicit type in a `package.json`, or otherwise the `nextLoad` call would throw `ERR_UNKNOWN_FILE_EXTENSION` (if undefined) or `ERR_UNKNOWN_MODULE_FORMAT` (if it's not a known format listed in the [load hook](https://nodejs.org/docs/latest/api/module.html#synchronous-loadurl-context-nextload) documentation).
With the preceding hooks modules, running `node --import 'data:text/javascript,import { register } from "node:module"; import { pathToFileURL } from "node:url"; register(pathToFileURL("./coffeescript-hooks.mjs"));' ./main.coffee` or `node --import ./coffeescript-sync-hooks.mjs ./main.coffee` causes `main.coffee` to be turned into JavaScript after its source code is loaded from disk but before Node.js executes it; and so on for any `.coffee`, `.litcoffee` or `.coffee.md` files referenced via `import` statements of any loaded file.
##### Import maps[#](https://nodejs.org/docs/latest/api/module.html#import-maps)
The previous two examples defined `load` hooks. This is an example of a `resolve` hook. This hooks module reads an `import-map.json` file that defines which specifiers to override to other URLs (this is a very simplistic implementation of a small subset of the "import maps" specification).
###### Asynchronous version[#](https://nodejs.org/docs/latest/api/module.html#asynchronous-version-1)
```
// import-map-hooks.js
import fs from 'node:fs/promises';

const { imports } = JSON.parse(await fs.readFile('import-map.json'));

export async function resolve(specifier, context, nextResolve) {
  if (Object.hasOwn(imports, specifier)) {
    return nextResolve(imports[specifier], context);
  }

  return nextResolve(specifier, context);
}
copy
```

###### Synchronous version[#](https://nodejs.org/docs/latest/api/module.html#synchronous-version-1)
```
// import-map-sync-hooks.js
import fs from 'node:fs/promises';
import module from 'node:module';

const { imports } = JSON.parse(fs.readFileSync('import-map.json', 'utf-8'));

function resolve(specifier, context, nextResolve) {
  if (Object.hasOwn(imports, specifier)) {
    return nextResolve(imports[specifier], context);
  }

  return nextResolve(specifier, context);
}

module.registerHooks({ resolve });
copy
```

###### Using the hooks[#](https://nodejs.org/docs/latest/api/module.html#using-the-hooks)
With these files:
```
// main.js
import 'a-module';
// some-module.js
console.log('some module!');
copy
```

Running `node --import 'data:text/javascript,import { register } from "node:module"; import { pathToFileURL } from "node:url"; register(pathToFileURL("./import-map-hooks.js"));' main.js` or `node --import ./import-map-sync-hooks.js main.js` should print `some module!`.
### Source Map Support[#](https://nodejs.org/docs/latest/api/module.html#source-map-support)
Added in: v13.7.0, v12.17.0
Stability: 1 - Experimental
Node.js supports TC39 ECMA-426
The APIs in this section are helpers for interacting with the source map cache. This cache is populated when source map parsing is enabled and
To enable source map parsing, Node.js must be run with the flag [`--enable-source-maps`](https://nodejs.org/docs/latest/api/cli.html#--enable-source-maps), or with code coverage enabled by setting [`NODE_V8_COVERAGE=dir`](https://nodejs.org/docs/latest/api/cli.html#node_v8_coveragedir), or be enabled programmatically via [`module.setSourceMapsSupport()`](https://nodejs.org/docs/latest/api/module.html#modulesetsourcemapssupportenabled-options).
```
// module.mjs
// In an ECMAScript module
import { findSourceMap, SourceMap } from 'node:module';
// module.cjs
// In a CommonJS module
const { findSourceMap, SourceMap } = require('node:module');
copy
```

####  `module.getSourceMapsSupport()`[#](https://nodejs.org/docs/latest/api/module.html#modulegetsourcemapssupport)
Added in: v23.7.0, v22.14.0
  * Returns:
    * `enabled`
    * `nodeModules` `node_modules`.
    * `generatedCode` `eval` or `new Function`.


This method returns whether the
####  `module.findSourceMap(path)`[#](https://nodejs.org/docs/latest/api/module.html#modulefindsourcemappath)
Added in: v13.7.0, v12.17.0
  * `path`
  * Returns: [`<module.SourceMap>`](https://nodejs.org/docs/latest/api/module.html#class-modulesourcemap) | `module.SourceMap` if a source map is found, `undefined` otherwise.


`path` is the resolved path for the file for which a corresponding source map should be fetched.
####  `module.setSourceMapsSupport(enabled[, options])`[#](https://nodejs.org/docs/latest/api/module.html#modulesetsourcemapssupportenabled-options)
Added in: v23.7.0, v22.14.0
  * `enabled`
  * `options`
    * `nodeModules` `node_modules`. **Default:** `false`.
    * `generatedCode` `eval` or `new Function`. **Default:** `false`.


This function enables or disables the
It provides same features as launching Node.js process with commandline options `--enable-source-maps`, with additional options to alter the support for files in `node_modules` or generated codes.
Only source maps in JavaScript files that are loaded after source maps has been enabled will be parsed and loaded. Preferably, use the commandline options `--enable-source-maps` to avoid losing track of source maps of modules loaded before this API call.
#### Class: `module.SourceMap`[#](https://nodejs.org/docs/latest/api/module.html#class-modulesourcemap)
Added in: v13.7.0, v12.17.0
#####  `new SourceMap(payload[, { lineLengths }])`[#](https://nodejs.org/docs/latest/api/module.html#new-sourcemappayload-linelengths)
History Version | Changes
---|---
v20.5.0 | Add support for `lineLengths`.
  * `payload`
  * `lineLengths`


Creates a new `sourceMap` instance.
`payload` is an object with keys matching the
  * `file`
  * `version`
  * `sources`
  * `sourcesContent`
  * `names`
  * `mappings`
  * `sourceRoot`


`lineLengths` is an optional array of the length of each line in the generated code.
#####  `sourceMap.payload`[#](https://nodejs.org/docs/latest/api/module.html#sourcemappayload)
  * Returns:


Getter for the payload used to construct the [`SourceMap`](https://nodejs.org/docs/latest/api/module.html#class-modulesourcemap) instance.
#####  `sourceMap.findEntry(lineOffset, columnOffset)`[#](https://nodejs.org/docs/latest/api/module.html#sourcemapfindentrylineoffset-columnoffset)
  * `lineOffset`
  * `columnOffset`
  * Returns:


Given a line offset and column offset in the generated source file, returns an object representing the SourceMap range in the original file if found, or an empty object if not.
The object returned contains the following keys:
  * `generatedLine`
  * `generatedColumn`
  * `originalSource`
  * `originalLine`
  * `originalColumn`
  * `name`


The returned value represents the raw range as it appears in the SourceMap, based on zero-indexed offsets, _not_ 1-indexed line and column numbers as they appear in Error messages and CallSite objects.
To get the corresponding 1-indexed line and column numbers from a lineNumber and columnNumber as they are reported by Error stacks and CallSite objects, use `sourceMap.findOrigin(lineNumber, columnNumber)`
#####  `sourceMap.findOrigin(lineNumber, columnNumber)`[#](https://nodejs.org/docs/latest/api/module.html#sourcemapfindoriginlinenumber-columnnumber)
Added in: v20.4.0, v18.18.0
  * `lineNumber`
  * `columnNumber`
  * Returns:


Given a 1-indexed `lineNumber` and `columnNumber` from a call site in the generated source, find the corresponding call site location in the original source.
If the `lineNumber` and `columnNumber` provided are not found in any source map, then an empty object is returned. Otherwise, the returned object contains the following keys:
  * `name`
  * `fileName`
  * `lineNumber`
  * `columnNumber`
