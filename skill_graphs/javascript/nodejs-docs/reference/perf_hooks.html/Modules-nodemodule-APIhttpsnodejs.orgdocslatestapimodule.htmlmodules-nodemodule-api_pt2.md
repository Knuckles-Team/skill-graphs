  load(url, context, nextLoad) { /* implementation */ },
});
copy
```

###### Registering hooks before application code runs with flags[#](https://nodejs.org/docs/latest/api/module.html#registering-hooks-before-application-code-runs-with-flags)
The hooks can be registered before the application code is run by using the [`--import`](https://nodejs.org/docs/latest/api/cli.html#--importmodule) or [`--require`](https://nodejs.org/docs/latest/api/cli.html#-r---require-module) flag:
```
node --import ./register-hooks.js ./my-app.js
node --require ./register-hooks.js ./my-app.js
copy
```

The specifier passed to `--import` or `--require` can also come from a package:
```
node --import some-package/register ./my-app.js
node --require some-package/register ./my-app.js
copy
```

Where `some-package` has an [`"exports"`](https://nodejs.org/docs/latest/api/packages.html#exports) field defining the `/register` export to map to a file that calls `registerHooks()`, like the `register-hooks.js` examples above.
Using `--import` or `--require` ensures that the hooks are registered before any application code is loaded, including the entry point of the application and for any worker threads by default as well.
###### Registering hooks before application code runs programmatically[#](https://nodejs.org/docs/latest/api/module.html#registering-hooks-before-application-code-runs-programmatically)
Alternatively, `registerHooks()` can be called from the entry point.
If the entry point needs to load other modules and the loading process needs to be customized, load them using either `require()` or dynamic `import()` after the hooks are registered. Do not use static `import` statements to load modules that need to be customized in the same module that registers the hooks, because static `import` statements are evaluated before any code in the importer module is run, including the call to `registerHooks()`, regardless of where the static `import` statements appear in the importer module.
```
import { registerHooks } from 'node:module';

registerHooks({ /* implementation of synchronous hooks */ });

// If loaded using static import, the hooks would not be applied when loading
// my-app.mjs, because statically imported modules are all executed before its
// importer regardless of where the static import appears.
// import './my-app.mjs';

// my-app.mjs must be loaded dynamically to ensure the hooks are applied.
await import('./my-app.mjs');
const { registerHooks } = require('node:module');

registerHooks({ /* implementation of synchronous hooks */ });

import('./my-app.mjs');
// Or, if my-app.mjs does not have top-level await or it's a CommonJS module,
// require() can also be used:
// require('./my-app.mjs');
copy
```

###### Registering hooks before application code runs with a `data:` URL[#](https://nodejs.org/docs/latest/api/module.html#registering-hooks-before-application-code-runs-with-a-data-url)
Alternatively, inline JavaScript code can be embedded in `data:` URLs to register the hooks before the application code runs. For example,
```
node --import 'data:text/javascript,import {registerHooks} from "node:module"; registerHooks(/* hooks code */);' ./my-app.js
copy
```

##### Convention of hooks and chaining[#](https://nodejs.org/docs/latest/api/module.html#convention-of-hooks-and-chaining)
Hooks are part of a chain, even if that chain consists of only one custom (user-provided) hook and the default hook, which is always present.
Hook functions nest: each one must always return a plain object, and chaining happens as a result of each function calling `next<hookName>()`, which is a reference to the subsequent loader's hook (in LIFO order).
It's possible to call `registerHooks()` more than once:
```
// entrypoint.mjs
import { registerHooks } from 'node:module';

const hook1 = { /* implementation of hooks */ };
const hook2 = { /* implementation of hooks */ };
// hook2 runs before hook1.
registerHooks(hook1);
registerHooks(hook2);
// entrypoint.cjs
const { registerHooks } = require('node:module');

const hook1 = { /* implementation of hooks */ };
const hook2 = { /* implementation of hooks */ };
// hook2 runs before hook1.
registerHooks(hook1);
registerHooks(hook2);
copy
```

In this example, the registered hooks will form chains. These chains run last-in, first-out (LIFO). If both `hook1` and `hook2` define a `resolve` hook, they will be called like so (note the right-to-left, starting with `hook2.resolve`, then `hook1.resolve`, then the Node.js default):
Node.js default `resolve` ← `hook1.resolve` ← `hook2.resolve`
The same applies to all the other hooks.
A hook that returns a value lacking a required property triggers an exception. A hook that returns without calling `next<hookName>()` _and_ without returning `shortCircuit: true` also triggers an exception. These errors are to help prevent unintentional breaks in the chain. Return `shortCircuit: true` from a hook to signal that the chain is intentionally ending at your hook.
If a hook should be applied when loading other hook modules, the other hook modules should be loaded after the hook is registered.
##### Hook functions accepted by `module.registerHooks()`[#](https://nodejs.org/docs/latest/api/module.html#hook-functions-accepted-by-moduleregisterhooks)
Added in: v23.5.0, v22.15.0
The `module.registerHooks()` method accepts the following synchronous hook functions.
```
function resolve(specifier, context, nextResolve) {
  // Take an `import` or `require` specifier and resolve it to a URL.
}

function load(url, context, nextLoad) {
  // Take a resolved URL and return the source code to be evaluated.
}
copy
```

Synchronous hooks are run in the same thread and the same
Unlike the asynchronous hooks, the synchronous hooks are not inherited into child worker threads by default, though if the hooks are registered using a file preloaded by [`--import`](https://nodejs.org/docs/latest/api/cli.html#--importmodule) or [`--require`](https://nodejs.org/docs/latest/api/cli.html#-r---require-module), child worker threads can inherit the preloaded scripts via `process.execArgv` inheritance. See [the documentation of `Worker`](https://nodejs.org/docs/latest/api/worker_threads.html#new-workerfilename-options) for details.
##### Synchronous `resolve(specifier, context, nextResolve)`[#](https://nodejs.org/docs/latest/api/module.html#synchronous-resolvespecifier-context-nextresolve)
History Version | Changes
---|---
v23.5.0, v22.15.0 | Add support for synchronous and in-thread hooks.
  * `specifier`
  * `context`
    * `conditions` `package.json`
    * `importAttributes`
    * `parentURL`
  * `nextResolve` `resolve` hook in the chain, or the Node.js default `resolve` hook after the last user-supplied `resolve` hook
    * `specifier`
    * `context`
  * Returns:
    * `format` `load` hook (it might be ignored). It can be a module format (such as `'commonjs'` or `'module'`) or an arbitrary value like `'css'` or `'yaml'`.
    * `importAttributes`
    * `shortCircuit` `resolve` hooks. **Default:** `false`
    * `url`


The `resolve` hook chain is responsible for telling Node.js where to find and how to cache a given `import` statement or expression, or `require` call. It can optionally return a format (such as `'module'`) as a hint to the `load` hook. If a format is specified, the `load` hook is ultimately responsible for providing the final `format` value (and it is free to ignore the hint provided by `resolve`); if `resolve` provides a `format`, a custom `load` hook is required even if only to pass the value to the Node.js default `load` hook.
Import type attributes are part of the cache key for saving loaded modules into the internal module cache. The `resolve` hook is responsible for returning an `importAttributes` object if the module should be cached with different attributes than were present in the source code.
The `conditions` property in `context` is an array of conditions that will be used to match [package exports conditions](https://nodejs.org/docs/latest/api/packages.html#conditional-exports) for this resolution request. They can be used for looking up conditional mappings elsewhere or to modify the list when calling the default resolution logic.
The current [package exports conditions](https://nodejs.org/docs/latest/api/packages.html#conditional-exports) are always in the `context.conditions` array passed into the hook. To guarantee _default Node.js module specifier resolution behavior_ when calling `defaultResolve`, the `context.conditions` array passed to it _must_ include _all_ elements of the `context.conditions` array originally passed into the `resolve` hook.
```
import { registerHooks } from 'node:module';

function resolve(specifier, context, nextResolve) {
  // When calling `defaultResolve`, the arguments can be modified. For example,
  // to change the specifier or to add applicable export conditions.
  if (specifier.includes('foo')) {
    specifier = specifier.replace('foo', 'bar');
    return nextResolve(specifier, {
      ...context,
      conditions: [...context.conditions, 'another-condition'],
    });
  }

  // The hook can also skip default resolution and provide a custom URL.
  if (specifier === 'special-module') {
    return {
      url: 'file:///path/to/special-module.mjs',
      format: 'module',
      shortCircuit: true,  // This is mandatory if nextResolve() is not called.
    };
  }

  // If no customization is needed, defer to the next hook in the chain which would be the
  // Node.js default resolve if this is the last user-specified loader.
  return nextResolve(specifier);
}

registerHooks({ resolve });
copy
```

##### Synchronous `load(url, context, nextLoad)`[#](https://nodejs.org/docs/latest/api/module.html#synchronous-loadurl-context-nextload)
History Version | Changes
---|---
v23.5.0, v22.15.0 | Add support for synchronous and in-thread version.
  * `url` `resolve` chain
  * `context`
    * `conditions` `package.json`
    * `format` `resolve` hook chain. This can be any string value as an input; input values do not need to conform to the list of acceptable return values described below.
    * `importAttributes`
  * `nextLoad` `load` hook in the chain, or the Node.js default `load` hook after the last user-supplied `load` hook
    * `url`
    * `context` `nextLoad`, if the module pointed to by `url` does not have explicit module type information, `context.format` is mandatory.
  * Returns:
    * `format` [below](https://nodejs.org/docs/latest/api/module.html#accepted-final-formats-returned-by-load).
    * `shortCircuit` `load` hooks. **Default:** `false`
    * `source`


The `load` hook provides a way to define a custom method for retrieving the source code of a resolved URL. This would allow a loader to potentially avoid reading files from disk. It could also be used to map an unrecognized format to a supported one, for example `yaml` to `module`.
```
import { registerHooks } from 'node:module';
import { Buffer } from 'node:buffer';

function load(url, context, nextLoad) {
  // The hook can skip default loading and provide a custom source code.
  if (url === 'special-module') {
    return {
      source: 'export const special = 42;',
      format: 'module',
      shortCircuit: true,  // This is mandatory if nextLoad() is not called.
    };
  }

  // It's possible to modify the source code loaded by the next - possibly default - step,
  // for example, replacing 'foo' with 'bar' in the source code of the module.
  const result = nextLoad(url, context);
  const source = typeof result.source === 'string' ?
    result.source : Buffer.from(result.source).toString('utf8');
  return {
    source: source.replace(/foo/g, 'bar'),
    ...result,
  };
}

registerHooks({ resolve });
copy
```

In a more advanced scenario, this can also be used to transform an unsupported source to a supported one (see [Examples](https://nodejs.org/docs/latest/api/module.html#examples) below).
###### Accepted final formats returned by `load`[#](https://nodejs.org/docs/latest/api/module.html#accepted-final-formats-returned-by-load)
The final value of `format` must be one of the following:
`format` | Description | Acceptable types for `source` returned by `load`
---|---|---
`'addon'` | Load a Node.js addon |
`'builtin'` | Load a Node.js builtin module |
`'commonjs-typescript'` | Load a Node.js CommonJS module with TypeScript syntax |
`'commonjs'` | Load a Node.js CommonJS module |
`'json'` | Load a JSON file |
`'module-typescript'` | Load an ES module with TypeScript syntax |
`'module'` | Load an ES module |
`'wasm'` | Load a WebAssembly module |
The value of `source` is ignored for format `'builtin'` because currently it is not possible to replace the value of a Node.js builtin (core) module.
> These types all correspond to classes defined in ECMAScript.
  * The specific
  * The specific


If the source value of a text-based format (i.e., `'json'`, `'module'`) is not a string, it is converted to a string using [`util.TextDecoder`](https://nodejs.org/docs/latest/api/util.html#class-utiltextdecoder).
#### Asynchronous customization hooks[#](https://nodejs.org/docs/latest/api/module.html#asynchronous-customization-hooks)
Stability: 1.1 - Active Development
##### Caveats of asynchronous customization hooks[#](https://nodejs.org/docs/latest/api/module.html#caveats-of-asynchronous-customization-hooks)
The asynchronous customization hooks have many caveats and it is uncertain if their issues can be resolved. Users are encouraged to use the synchronous customization hooks via `module.registerHooks()` instead to avoid these caveats.
  * Asynchronous hooks run on a separate thread, so the hook functions cannot directly mutate the global state of the modules being customized. It's typical to use message channels and atomics to pass data between the two or to affect control flows. See [Communication with asynchronous module customization hooks](https://nodejs.org/docs/latest/api/module.html#communication-with-asynchronous-module-customization-hooks).
  * Asynchronous hooks do not affect all `require()` calls in the module graph.
    * Custom `require` functions created using `module.createRequire()` are not affected.
    * If the asynchronous `load` hook does not override the `source` for CommonJS modules that go through it, the child modules loaded by those CommonJS modules via built-in `require()` would not be affected by the asynchronous hooks either.
  * There are several caveats that the asynchronous hooks need to handle when customizing CommonJS modules. See [asynchronous `resolve` hook](https://nodejs.org/docs/latest/api/module.html#asynchronous-resolvespecifier-context-nextresolve) and [asynchronous `load` hook](https://nodejs.org/docs/latest/api/module.html#asynchronous-loadurl-context-nextload) for details.
  * When `require()` calls inside CommonJS modules are customized by asynchronous hooks, Node.js may need to load the source code of the CommonJS module multiple times to maintain compatibility with existing CommonJS monkey-patching. If the module code changes between loads, this may lead to unexpected behaviors.
    * As a side effect, if both asynchronous hooks and synchronous hooks are registered and the asynchronous hooks choose to customize the CommonJS module, the synchronous hooks may be invoked multiple times for the `require()` calls in that CommonJS module.


##### Registration of asynchronous customization hooks[#](https://nodejs.org/docs/latest/api/module.html#registration-of-asynchronous-customization-hooks)
Asynchronous customization hooks are registered using [`module.register()`](https://nodejs.org/docs/latest/api/module.html#moduleregisterspecifier-parenturl-options) which takes a path or URL to another module that exports the [asynchronous hook functions](https://nodejs.org/docs/latest/api/module.html#asynchronous-hooks-accepted-by-moduleregister).
Similar to `registerHooks()`, `register()` can be called in a module preloaded by `--import` or `--require`, or called directly within the entry point.
```
// Use module.register() to register asynchronous hooks in a dedicated thread.
import { register } from 'node:module';
register('./hooks.mjs', import.meta.url);

// If my-app.mjs is loaded statically here as `import './my-app.mjs'`, since ESM
// dependencies are evaluated before the module that imports them,
// it's loaded _before_ the hooks are registered above and won't be affected.
// To ensure the hooks are applied, dynamic import() must be used to load ESM
// after the hooks are registered.
import('./my-app.mjs');
const { register } = require('node:module');
const { pathToFileURL } = require('node:url');
// Use module.register() to register asynchronous hooks in a dedicated thread.
register('./hooks.mjs', pathToFileURL(__filename));

import('./my-app.mjs');
copy
```

In `hooks.mjs`:
```
// hooks.mjs
export async function resolve(specifier, context, nextResolve) {
  /* implementation */
}
export async function load(url, context, nextLoad) {
  /* implementation */
}
copy
```

Unlike synchronous hooks, the asynchronous hooks would not run for these modules loaded in the file that calls `register()`:
```
// register-hooks.js
import { register, createRequire } from 'node:module';
register('./hooks.mjs', import.meta.url);

// Asynchronous hooks does not affect modules loaded via custom require()
// functions created by module.createRequire().
const userRequire = createRequire(__filename);
userRequire('./my-app-2.cjs');  // Hooks won't affect this
// register-hooks.js
const { register, createRequire } = require('node:module');
const { pathToFileURL } = require('node:url');
register('./hooks.mjs', pathToFileURL(__filename));

// Asynchronous hooks does not affect modules loaded via built-in require()
// in the module calling `register()`
require('./my-app-2.cjs');  // Hooks won't affect this
// .. or custom require() functions created by module.createRequire().
const userRequire = createRequire(__filename);
userRequire('./my-app-3.cjs');  // Hooks won't affect this
copy
```

Asynchronous hooks can also be registered using a `data:` URL with the `--import` flag:
```
node --import 'data:text/javascript,import { register } from "node:module"; import { pathToFileURL } from "node:url"; register("my-instrumentation", pathToFileURL("./"));' ./my-app.js
copy
```

##### Chaining of asynchronous customization hooks[#](https://nodejs.org/docs/latest/api/module.html#chaining-of-asynchronous-customization-hooks)
Chaining of `register()` work similarly to `registerHooks()`. If synchronous and asynchronous hooks are mixed, the synchronous hooks are always run first before the asynchronous hooks start running, that is, in the last synchronous hook being run, its next hook includes invocation of the asynchronous hooks.
```
// entrypoint.mjs
import { register } from 'node:module';

register('./foo.mjs', import.meta.url);
register('./bar.mjs', import.meta.url);
await import('./my-app.mjs');
// entrypoint.cjs
const { register } = require('node:module');
const { pathToFileURL } = require('node:url');

const parentURL = pathToFileURL(__filename);
register('./foo.mjs', parentURL);
register('./bar.mjs', parentURL);
import('./my-app.mjs');
copy
```

If `foo.mjs` and `bar.mjs` define a `resolve` hook, they will be called like so (note the right-to-left, starting with `./bar.mjs`, then `./foo.mjs`, then the Node.js default):
Node.js default ← `./foo.mjs` ← `./bar.mjs`
When using the asynchronous hooks, the registered hooks also affect subsequent `register` calls, which takes care of loading hook modules. In the example above, `bar.mjs` will be resolved and loaded via the hooks registered by `foo.mjs` (because `foo`'s hooks will have already been added to the chain). This allows for things like writing hooks in non-JavaScript languages, so long as earlier registered hooks transpile into JavaScript.
The `register()` method cannot be called from the thread running the hook module that exports the asynchronous hooks or its dependencies.
##### Communication with asynchronous module customization hooks[#](https://nodejs.org/docs/latest/api/module.html#communication-with-asynchronous-module-customization-hooks)
Asynchronous hooks run on a dedicated thread, separate from the main thread that runs application code. This means mutating global variables won't affect the other thread(s), and message channels must be used to communicate between the threads.
The `register` method can be used to pass data to an [`initialize`](https://nodejs.org/docs/latest/api/module.html#initialize) hook. The data passed to the hook may include transferable objects like ports.
```
import { register } from 'node:module';
import { MessageChannel } from 'node:worker_threads';

// This example demonstrates how a message channel can be used to
// communicate with the hooks, by sending `port2` to the hooks.
const { port1, port2 } = new MessageChannel();

port1.on('message', (msg) => {
  console.log(msg);
});
port1.unref();

register('./my-hooks.mjs', {
  parentURL: import.meta.url,
  data: { number: 1, port: port2 },
  transferList: [port2],
});
const { register } = require('node:module');
const { pathToFileURL } = require('node:url');
const { MessageChannel } = require('node:worker_threads');

// This example showcases how a message channel can be used to
// communicate with the hooks, by sending `port2` to the hooks.
const { port1, port2 } = new MessageChannel();

port1.on('message', (msg) => {
  console.log(msg);
});
port1.unref();

register('./my-hooks.mjs', {
  parentURL: pathToFileURL(__filename),
  data: { number: 1, port: port2 },
  transferList: [port2],
});
copy
```

##### Asynchronous hooks accepted by `module.register()`[#](https://nodejs.org/docs/latest/api/module.html#asynchronous-hooks-accepted-by-moduleregister)
Added in: v8.8.0History Version | Changes
---|---
v20.6.0, v18.19.0 | Added `initialize` hook to replace `globalPreload`.
v18.6.0, v16.17.0 | Add support for chaining loaders.
v16.12.0 | Removed `getFormat`, `getSource`, `transformSource`, and `globalPreload`; added `load` hook and `getGlobalPreload` hook.
The [`register`](https://nodejs.org/docs/latest/api/module.html#moduleregisterspecifier-parenturl-options) method can be used to register a module that exports a set of hooks. The hooks are functions that are called by Node.js to customize the module resolution and loading process. The exported functions must have specific names and signatures, and they must be exported as named exports.
```
export async function initialize({ number, port }) {
  // Receives data from `register`.
}

export async function resolve(specifier, context, nextResolve) {
  // Take an `import` or `require` specifier and resolve it to a URL.
}

export async function load(url, context, nextLoad) {
  // Take a resolved URL and return the source code to be evaluated.
}
copy
```

Asynchronous hooks are run in a separate thread, isolated from the main thread where application code runs. That means it is a different `console.log`) to complete. They are inherited into child workers by default.
#####  `initialize()`[#](https://nodejs.org/docs/latest/api/module.html#initialize)
Added in: v20.6.0, v18.19.0
  * `data` `register(loader, import.meta.url, { data })`.


The `initialize` hook is only accepted by [`register`](https://nodejs.org/docs/latest/api/module.html#moduleregisterspecifier-parenturl-options). `registerHooks()` does not support nor need it since initialization done for synchronous hooks can be run directly before the call to `registerHooks()`.
The `initialize` hook provides a way to define a custom function that runs in the hooks thread when the hooks module is initialized. Initialization happens when the hooks module is registered via [`register`](https://nodejs.org/docs/latest/api/module.html#moduleregisterspecifier-parenturl-options).
This hook can receive data from a [`register`](https://nodejs.org/docs/latest/api/module.html#moduleregisterspecifier-parenturl-options) invocation, including ports and other transferable objects. The return value of `initialize` can be a
Module customization code:
```
// path-to-my-hooks.js

export async function initialize({ number, port }) {
  port.postMessage(`increment: ${number + 1}`);
}
copy
```

Caller code:
```
import assert from 'node:assert';
import { register } from 'node:module';
import { MessageChannel } from 'node:worker_threads';

// This example showcases how a message channel can be used to communicate
// between the main (application) thread and the hooks running on the hooks
// thread, by sending `port2` to the `initialize` hook.
const { port1, port2 } = new MessageChannel();

port1.on('message', (msg) => {
  assert.strictEqual(msg, 'increment: 2');
});
port1.unref();

register('./path-to-my-hooks.js', {
  parentURL: import.meta.url,
  data: { number: 1, port: port2 },
  transferList: [port2],
});
const assert = require('node:assert');
const { register } = require('node:module');
const { pathToFileURL } = require('node:url');
const { MessageChannel } = require('node:worker_threads');

// This example showcases how a message channel can be used to communicate
// between the main (application) thread and the hooks running on the hooks
// thread, by sending `port2` to the `initialize` hook.
const { port1, port2 } = new MessageChannel();

port1.on('message', (msg) => {
  assert.strictEqual(msg, 'increment: 2');
});
port1.unref();

register('./path-to-my-hooks.js', {
  parentURL: pathToFileURL(__filename),
  data: { number: 1, port: port2 },
