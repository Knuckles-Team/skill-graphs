[Skip to content](https://nodejs.org/docs/latest/api/async_context.html#apicontent)
[ Node.js ](https://nodejs.org/ "Go back to the home page")
* * *
  * [About this documentation](https://nodejs.org/docs/latest/api/documentation.html)
  * [Usage and example](https://nodejs.org/docs/latest/api/synopsis.html)
  * [Assertion testing](https://nodejs.org/docs/latest/api/assert.html)
  * [Asynchronous context tracking](https://nodejs.org/docs/latest/api/async_context.html)
  * [Async hooks](https://nodejs.org/docs/latest/api/async_hooks.html)
  * [Buffer](https://nodejs.org/docs/latest/api/buffer.html)
  * [C++ addons](https://nodejs.org/docs/latest/api/addons.html)
  * [C/C++ addons with Node-API](https://nodejs.org/docs/latest/api/n-api.html)
  * [C++ embedder API](https://nodejs.org/docs/latest/api/embedding.html)
  * [Child processes](https://nodejs.org/docs/latest/api/child_process.html)
  * [Cluster](https://nodejs.org/docs/latest/api/cluster.html)
  * [Command-line options](https://nodejs.org/docs/latest/api/cli.html)
  * [Console](https://nodejs.org/docs/latest/api/console.html)
  * [Crypto](https://nodejs.org/docs/latest/api/crypto.html)
  * [Debugger](https://nodejs.org/docs/latest/api/debugger.html)
  * [Deprecated APIs](https://nodejs.org/docs/latest/api/deprecations.html)
  * [Diagnostics Channel](https://nodejs.org/docs/latest/api/diagnostics_channel.html)
  * [DNS](https://nodejs.org/docs/latest/api/dns.html)
  * [Domain](https://nodejs.org/docs/latest/api/domain.html)
  * [Environment Variables](https://nodejs.org/docs/latest/api/environment_variables.html)
  * [Errors](https://nodejs.org/docs/latest/api/errors.html)
  * [Events](https://nodejs.org/docs/latest/api/events.html)
  * [File system](https://nodejs.org/docs/latest/api/fs.html)
  * [Globals](https://nodejs.org/docs/latest/api/globals.html)
  * [HTTP](https://nodejs.org/docs/latest/api/http.html)
  * [HTTP/2](https://nodejs.org/docs/latest/api/http2.html)
  * [HTTPS](https://nodejs.org/docs/latest/api/https.html)
  * [Inspector](https://nodejs.org/docs/latest/api/inspector.html)
  * [Internationalization](https://nodejs.org/docs/latest/api/intl.html)
  * [Modules: CommonJS modules](https://nodejs.org/docs/latest/api/modules.html)
  * [Modules: ECMAScript modules](https://nodejs.org/docs/latest/api/esm.html)
  * [Modules: `node:module` API](https://nodejs.org/docs/latest/api/module.html)
  * [Modules: Packages](https://nodejs.org/docs/latest/api/packages.html)
  * [Modules: TypeScript](https://nodejs.org/docs/latest/api/typescript.html)
  * [Net](https://nodejs.org/docs/latest/api/net.html)
  * [OS](https://nodejs.org/docs/latest/api/os.html)
  * [Path](https://nodejs.org/docs/latest/api/path.html)
  * [Performance hooks](https://nodejs.org/docs/latest/api/perf_hooks.html)
  * [Permissions](https://nodejs.org/docs/latest/api/permissions.html)
  * [Process](https://nodejs.org/docs/latest/api/process.html)
  * [Punycode](https://nodejs.org/docs/latest/api/punycode.html)
  * [Query strings](https://nodejs.org/docs/latest/api/querystring.html)
  * [Readline](https://nodejs.org/docs/latest/api/readline.html)
  * [REPL](https://nodejs.org/docs/latest/api/repl.html)
  * [Report](https://nodejs.org/docs/latest/api/report.html)
  * [Single executable applications](https://nodejs.org/docs/latest/api/single-executable-applications.html)
  * [SQLite](https://nodejs.org/docs/latest/api/sqlite.html)
  * [Stream](https://nodejs.org/docs/latest/api/stream.html)
  * [String decoder](https://nodejs.org/docs/latest/api/string_decoder.html)
  * [Test runner](https://nodejs.org/docs/latest/api/test.html)
  * [Timers](https://nodejs.org/docs/latest/api/timers.html)
  * [TLS/SSL](https://nodejs.org/docs/latest/api/tls.html)
  * [Trace events](https://nodejs.org/docs/latest/api/tracing.html)
  * [TTY](https://nodejs.org/docs/latest/api/tty.html)
  * [UDP/datagram](https://nodejs.org/docs/latest/api/dgram.html)
  * [URL](https://nodejs.org/docs/latest/api/url.html)
  * [Utilities](https://nodejs.org/docs/latest/api/util.html)
  * [V8](https://nodejs.org/docs/latest/api/v8.html)
  * [VM](https://nodejs.org/docs/latest/api/vm.html)
  * [WASI](https://nodejs.org/docs/latest/api/wasi.html)
  * [Web Crypto API](https://nodejs.org/docs/latest/api/webcrypto.html)
  * [Web Streams API](https://nodejs.org/docs/latest/api/webstreams.html)
  * [Worker threads](https://nodejs.org/docs/latest/api/worker_threads.html)
  * [Zlib](https://nodejs.org/docs/latest/api/zlib.html)


* * *
# Node.js v25.8.0 documentation
  * Node.js v25.8.0
  * [](https://nodejs.org/docs/latest/api/async_context.html#toc-picker)
    * [Asynchronous context tracking](https://nodejs.org/docs/latest/api/async_context.html#asynchronous-context-tracking)
      * [Introduction](https://nodejs.org/docs/latest/api/async_context.html#introduction)
      * [Class: `AsyncLocalStorage`](https://nodejs.org/docs/latest/api/async_context.html#class-asynclocalstorage)
        * [`new AsyncLocalStorage([options])`](https://nodejs.org/docs/latest/api/async_context.html#new-asynclocalstorageoptions)
        * [Static method: `AsyncLocalStorage.bind(fn)`](https://nodejs.org/docs/latest/api/async_context.html#static-method-asynclocalstoragebindfn)
        * [Static method: `AsyncLocalStorage.snapshot()`](https://nodejs.org/docs/latest/api/async_context.html#static-method-asynclocalstoragesnapshot)
        * [`asyncLocalStorage.disable()`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragedisable)
        * [`asyncLocalStorage.getStore()`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragegetstore)
        * [`asyncLocalStorage.enterWith(store)`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstorageenterwithstore)
        * [`asyncLocalStorage.name`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragename)
        * [`asyncLocalStorage.run(store, callback[, ...args])`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragerunstore-callback-args)
        * [`asyncLocalStorage.exit(callback[, ...args])`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstorageexitcallback-args)
        * [Usage with `async/await`](https://nodejs.org/docs/latest/api/async_context.html#usage-with-asyncawait)
        * [Troubleshooting: Context loss](https://nodejs.org/docs/latest/api/async_context.html#troubleshooting-context-loss)
      * [Class: `AsyncResource`](https://nodejs.org/docs/latest/api/async_context.html#class-asyncresource)
        * [`new AsyncResource(type[, options])`](https://nodejs.org/docs/latest/api/async_context.html#new-asyncresourcetype-options)
        * [Static method: `AsyncResource.bind(fn[, type[, thisArg]])`](https://nodejs.org/docs/latest/api/async_context.html#static-method-asyncresourcebindfn-type-thisarg)
        * [`asyncResource.bind(fn[, thisArg])`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourcebindfn-thisarg)
        * [`asyncResource.runInAsyncScope(fn[, thisArg, ...args])`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourceruninasyncscopefn-thisarg-args)
        * [`asyncResource.emitDestroy()`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourceemitdestroy)
        * [`asyncResource.asyncId()`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourceasyncid)
        * [`asyncResource.triggerAsyncId()`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourcetriggerasyncid)
        * [Using `AsyncResource` for a `Worker` thread pool](https://nodejs.org/docs/latest/api/async_context.html#using-asyncresource-for-a-worker-thread-pool)
        * [Integrating `AsyncResource` with `EventEmitter`](https://nodejs.org/docs/latest/api/async_context.html#integrating-asyncresource-with-eventemitter)
  * [](https://nodejs.org/docs/latest/api/async_context.html#gtoc-picker)
    * [Index](https://nodejs.org/docs/latest/api/index.html)
* * *
    * [About this documentation](https://nodejs.org/docs/latest/api/documentation.html)
    * [Usage and example](https://nodejs.org/docs/latest/api/synopsis.html)
    * [Assertion testing](https://nodejs.org/docs/latest/api/assert.html)
    * [Asynchronous context tracking](https://nodejs.org/docs/latest/api/async_context.html)
    * [Async hooks](https://nodejs.org/docs/latest/api/async_hooks.html)
    * [Buffer](https://nodejs.org/docs/latest/api/buffer.html)
    * [C++ addons](https://nodejs.org/docs/latest/api/addons.html)
    * [C/C++ addons with Node-API](https://nodejs.org/docs/latest/api/n-api.html)
    * [C++ embedder API](https://nodejs.org/docs/latest/api/embedding.html)
    * [Child processes](https://nodejs.org/docs/latest/api/child_process.html)
    * [Cluster](https://nodejs.org/docs/latest/api/cluster.html)
    * [Command-line options](https://nodejs.org/docs/latest/api/cli.html)
    * [Console](https://nodejs.org/docs/latest/api/console.html)
    * [Crypto](https://nodejs.org/docs/latest/api/crypto.html)
    * [Debugger](https://nodejs.org/docs/latest/api/debugger.html)
    * [Deprecated APIs](https://nodejs.org/docs/latest/api/deprecations.html)
    * [Diagnostics Channel](https://nodejs.org/docs/latest/api/diagnostics_channel.html)
    * [DNS](https://nodejs.org/docs/latest/api/dns.html)
    * [Domain](https://nodejs.org/docs/latest/api/domain.html)
    * [Environment Variables](https://nodejs.org/docs/latest/api/environment_variables.html)
    * [Errors](https://nodejs.org/docs/latest/api/errors.html)
    * [Events](https://nodejs.org/docs/latest/api/events.html)
    * [File system](https://nodejs.org/docs/latest/api/fs.html)
    * [Globals](https://nodejs.org/docs/latest/api/globals.html)
    * [HTTP](https://nodejs.org/docs/latest/api/http.html)
    * [HTTP/2](https://nodejs.org/docs/latest/api/http2.html)
    * [HTTPS](https://nodejs.org/docs/latest/api/https.html)
    * [Inspector](https://nodejs.org/docs/latest/api/inspector.html)
    * [Internationalization](https://nodejs.org/docs/latest/api/intl.html)
    * [Modules: CommonJS modules](https://nodejs.org/docs/latest/api/modules.html)
    * [Modules: ECMAScript modules](https://nodejs.org/docs/latest/api/esm.html)
    * [Modules: `node:module` API](https://nodejs.org/docs/latest/api/module.html)
    * [Modules: Packages](https://nodejs.org/docs/latest/api/packages.html)
    * [Modules: TypeScript](https://nodejs.org/docs/latest/api/typescript.html)
    * [Net](https://nodejs.org/docs/latest/api/net.html)
    * [OS](https://nodejs.org/docs/latest/api/os.html)
    * [Path](https://nodejs.org/docs/latest/api/path.html)
    * [Performance hooks](https://nodejs.org/docs/latest/api/perf_hooks.html)
    * [Permissions](https://nodejs.org/docs/latest/api/permissions.html)
    * [Process](https://nodejs.org/docs/latest/api/process.html)
    * [Punycode](https://nodejs.org/docs/latest/api/punycode.html)
    * [Query strings](https://nodejs.org/docs/latest/api/querystring.html)
    * [Readline](https://nodejs.org/docs/latest/api/readline.html)
    * [REPL](https://nodejs.org/docs/latest/api/repl.html)
    * [Report](https://nodejs.org/docs/latest/api/report.html)
    * [Single executable applications](https://nodejs.org/docs/latest/api/single-executable-applications.html)
    * [SQLite](https://nodejs.org/docs/latest/api/sqlite.html)
    * [Stream](https://nodejs.org/docs/latest/api/stream.html)
    * [String decoder](https://nodejs.org/docs/latest/api/string_decoder.html)
    * [Test runner](https://nodejs.org/docs/latest/api/test.html)
    * [Timers](https://nodejs.org/docs/latest/api/timers.html)
    * [TLS/SSL](https://nodejs.org/docs/latest/api/tls.html)
    * [Trace events](https://nodejs.org/docs/latest/api/tracing.html)
    * [TTY](https://nodejs.org/docs/latest/api/tty.html)
    * [UDP/datagram](https://nodejs.org/docs/latest/api/dgram.html)
    * [URL](https://nodejs.org/docs/latest/api/url.html)
    * [Utilities](https://nodejs.org/docs/latest/api/util.html)
    * [V8](https://nodejs.org/docs/latest/api/v8.html)
    * [VM](https://nodejs.org/docs/latest/api/vm.html)
    * [WASI](https://nodejs.org/docs/latest/api/wasi.html)
    * [Web Crypto API](https://nodejs.org/docs/latest/api/webcrypto.html)
    * [Web Streams API](https://nodejs.org/docs/latest/api/webstreams.html)
    * [Worker threads](https://nodejs.org/docs/latest/api/worker_threads.html)
    * [Zlib](https://nodejs.org/docs/latest/api/zlib.html)
  * [](https://nodejs.org/docs/latest/api/async_context.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/async_context.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/async_context.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/async_context.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/async_context.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/async_context.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/async_context.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/async_context.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/async_context.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/async_context.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/async_context.html)
  * [ ](https://nodejs.org/docs/latest/api/async_context.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/async_context.json)


* * *
Table of contents
  * [Asynchronous context tracking](https://nodejs.org/docs/latest/api/async_context.html#asynchronous-context-tracking)
    * [Introduction](https://nodejs.org/docs/latest/api/async_context.html#introduction)
    * [Class: `AsyncLocalStorage`](https://nodejs.org/docs/latest/api/async_context.html#class-asynclocalstorage)
      * [`new AsyncLocalStorage([options])`](https://nodejs.org/docs/latest/api/async_context.html#new-asynclocalstorageoptions)
      * [Static method: `AsyncLocalStorage.bind(fn)`](https://nodejs.org/docs/latest/api/async_context.html#static-method-asynclocalstoragebindfn)
      * [Static method: `AsyncLocalStorage.snapshot()`](https://nodejs.org/docs/latest/api/async_context.html#static-method-asynclocalstoragesnapshot)
      * [`asyncLocalStorage.disable()`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragedisable)
      * [`asyncLocalStorage.getStore()`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragegetstore)
      * [`asyncLocalStorage.enterWith(store)`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstorageenterwithstore)
      * [`asyncLocalStorage.name`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragename)
      * [`asyncLocalStorage.run(store, callback[, ...args])`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragerunstore-callback-args)
      * [`asyncLocalStorage.exit(callback[, ...args])`](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstorageexitcallback-args)
      * [Usage with `async/await`](https://nodejs.org/docs/latest/api/async_context.html#usage-with-asyncawait)
      * [Troubleshooting: Context loss](https://nodejs.org/docs/latest/api/async_context.html#troubleshooting-context-loss)
    * [Class: `AsyncResource`](https://nodejs.org/docs/latest/api/async_context.html#class-asyncresource)
      * [`new AsyncResource(type[, options])`](https://nodejs.org/docs/latest/api/async_context.html#new-asyncresourcetype-options)
      * [Static method: `AsyncResource.bind(fn[, type[, thisArg]])`](https://nodejs.org/docs/latest/api/async_context.html#static-method-asyncresourcebindfn-type-thisarg)
      * [`asyncResource.bind(fn[, thisArg])`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourcebindfn-thisarg)
      * [`asyncResource.runInAsyncScope(fn[, thisArg, ...args])`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourceruninasyncscopefn-thisarg-args)
      * [`asyncResource.emitDestroy()`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourceemitdestroy)
      * [`asyncResource.asyncId()`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourceasyncid)
      * [`asyncResource.triggerAsyncId()`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourcetriggerasyncid)
      * [Using `AsyncResource` for a `Worker` thread pool](https://nodejs.org/docs/latest/api/async_context.html#using-asyncresource-for-a-worker-thread-pool)
      * [Integrating `AsyncResource` with `EventEmitter`](https://nodejs.org/docs/latest/api/async_context.html#integrating-asyncresource-with-eventemitter)


## Asynchronous context tracking[#](https://nodejs.org/docs/latest/api/async_context.html#asynchronous-context-tracking)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
### Introduction[#](https://nodejs.org/docs/latest/api/async_context.html#introduction)
These classes are used to associate state and propagate it throughout callbacks and promise chains. They allow storing data throughout the lifetime of a web request or any other asynchronous duration. It is similar to thread-local storage in other languages.
The `AsyncLocalStorage` and `AsyncResource` classes are part of the `node:async_hooks` module:
```
import { AsyncLocalStorage, AsyncResource } from 'node:async_hooks';
const { AsyncLocalStorage, AsyncResource } = require('node:async_hooks');
copy
```

### Class: `AsyncLocalStorage`[#](https://nodejs.org/docs/latest/api/async_context.html#class-asynclocalstorage)
Added in: v13.10.0, v12.17.0History Version | Changes
---|---
v16.4.0 | AsyncLocalStorage is now Stable. Previously, it had been Experimental.
This class creates stores that stay coherent through asynchronous operations.
While you can create your own implementation on top of the `node:async_hooks` module, `AsyncLocalStorage` should be preferred as it is a performant and memory safe implementation that involves significant optimizations that are non-obvious to implement.
The following example uses `AsyncLocalStorage` to build a simple logger that assigns IDs to incoming HTTP requests and includes them in messages logged within each request.
```
import http from 'node:http';
import { AsyncLocalStorage } from 'node:async_hooks';

const asyncLocalStorage = new AsyncLocalStorage();

function logWithId(msg) {
  const id = asyncLocalStorage.getStore();
  console.log(`${id !== undefined ? id : '-'}:`, msg);
}

let idSeq = 0;
http.createServer((req, res) => {
  asyncLocalStorage.run(idSeq++, () => {
    logWithId('start');
    // Imagine any chain of async operations here
    setImmediate(() => {
      logWithId('finish');
      res.end();
    });
  });
}).listen(8080);

http.get('http://localhost:8080');
http.get('http://localhost:8080');
// Prints:
//   0: start
//   0: finish
//   1: start
//   1: finish
const http = require('node:http');
const { AsyncLocalStorage } = require('node:async_hooks');

const asyncLocalStorage = new AsyncLocalStorage();

function logWithId(msg) {
  const id = asyncLocalStorage.getStore();
  console.log(`${id !== undefined ? id : '-'}:`, msg);
}

let idSeq = 0;
http.createServer((req, res) => {
  asyncLocalStorage.run(idSeq++, () => {
    logWithId('start');
    // Imagine any chain of async operations here
    setImmediate(() => {
      logWithId('finish');
      res.end();
    });
  });
}).listen(8080);

http.get('http://localhost:8080');
http.get('http://localhost:8080');
// Prints:
//   0: start
//   0: finish
//   1: start
//   1: finish
copy
```

Each instance of `AsyncLocalStorage` maintains an independent storage context. Multiple instances can safely exist simultaneously without risk of interfering with each other's data.
####  `new AsyncLocalStorage([options])`[#](https://nodejs.org/docs/latest/api/async_context.html#new-asynclocalstorageoptions)
Added in: v13.10.0, v12.17.0History Version | Changes
---|---
v24.0.0 | Add `defaultValue` and `name` options.
v19.7.0, v18.16.0 | Removed experimental onPropagate option.
v19.2.0, v18.13.0 | Add option onPropagate.
  * `options`
    * `defaultValue`
    * `name` `AsyncLocalStorage` value.


Creates a new instance of `AsyncLocalStorage`. Store is only provided within a `run()` call or after an `enterWith()` call.
#### Static method: `AsyncLocalStorage.bind(fn)`[#](https://nodejs.org/docs/latest/api/async_context.html#static-method-asynclocalstoragebindfn)
Added in: v19.8.0, v18.16.0History Version | Changes
---|---
v23.11.0, v22.15.0 | Marking the API stable.
  * `fn`
  * Returns: `fn` within the captured execution context.


Binds the given function to the current execution context.
#### Static method: `AsyncLocalStorage.snapshot()`[#](https://nodejs.org/docs/latest/api/async_context.html#static-method-asynclocalstoragesnapshot)
Added in: v19.8.0, v18.16.0History Version | Changes
---|---
v23.11.0, v22.15.0 | Marking the API stable.
  * Returns: `(fn: (...args) : R, ...args) : R`.


Captures the current execution context and returns a function that accepts a function as an argument. Whenever the returned function is called, it calls the function passed to it within the captured context.
```
const asyncLocalStorage = new AsyncLocalStorage();
const runInAsyncScope = asyncLocalStorage.run(123, () => AsyncLocalStorage.snapshot());
const result = asyncLocalStorage.run(321, () => runInAsyncScope(() => asyncLocalStorage.getStore()));
console.log(result);  // returns 123
copy
```

AsyncLocalStorage.snapshot() can replace the use of AsyncResource for simple async context tracking purposes, for example:
```
class Foo {
  #runInAsyncScope = AsyncLocalStorage.snapshot();

  get() { return this.#runInAsyncScope(() => asyncLocalStorage.getStore()); }
}

const foo = asyncLocalStorage.run(123, () => new Foo());
console.log(asyncLocalStorage.run(321, () => foo.get())); // returns 123
copy
```

####  `asyncLocalStorage.disable()`[#](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragedisable)
Added in: v13.10.0, v12.17.0
Stability: 1 - Experimental
Disables the instance of `AsyncLocalStorage`. All subsequent calls to `asyncLocalStorage.getStore()` will return `undefined` until `asyncLocalStorage.run()` or `asyncLocalStorage.enterWith()` is called again.
When calling `asyncLocalStorage.disable()`, all current contexts linked to the instance will be exited.
Calling `asyncLocalStorage.disable()` is required before the `asyncLocalStorage` can be garbage collected. This does not apply to stores provided by the `asyncLocalStorage`, as those objects are garbage collected along with the corresponding async resources.
Use this method when the `asyncLocalStorage` is not in use anymore in the current process.
####  `asyncLocalStorage.getStore()`[#](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragegetstore)
Added in: v13.10.0, v12.17.0
  * Returns:


Returns the current store. If called outside of an asynchronous context initialized by calling `asyncLocalStorage.run()` or `asyncLocalStorage.enterWith()`, it returns `undefined`.
####  `asyncLocalStorage.enterWith(store)`[#](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstorageenterwithstore)
Added in: v13.11.0, v12.17.0
Stability: 1 - Experimental
  * `store`


Transitions into the context for the remainder of the current synchronous execution and then persists the store through any following asynchronous calls.
Example:
```
const store = { id: 1 };
// Replaces previous store with the given store object
asyncLocalStorage.enterWith(store);
asyncLocalStorage.getStore(); // Returns the store object
someAsyncOperation(() => {
  asyncLocalStorage.getStore(); // Returns the same object
});
copy
```

This transition will continue for the _entire_ synchronous execution. This means that if, for example, the context is entered within an event handler subsequent event handlers will also run within that context unless specifically bound to another context with an `AsyncResource`. That is why `run()` should be preferred over `enterWith()` unless there are strong reasons to use the latter method.
```
const store = { id: 1 };

emitter.on('my-event', () => {
  asyncLocalStorage.enterWith(store);
});
emitter.on('my-event', () => {
  asyncLocalStorage.getStore(); // Returns the same object
});

asyncLocalStorage.getStore(); // Returns undefined
emitter.emit('my-event');
asyncLocalStorage.getStore(); // Returns the same object
copy
```

####  `asyncLocalStorage.name`[#](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragename)
Added in: v24.0.0
  * Type:


The name of the `AsyncLocalStorage` instance if provided.
####  `asyncLocalStorage.run(store, callback[, ...args])`[#](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstoragerunstore-callback-args)
Added in: v13.10.0, v12.17.0
  * `store`
  * `callback`
  * `...args`


Runs a function synchronously within a context and returns its return value. The store is not accessible outside of the callback function. The store is accessible to any asynchronous operations created within the callback.
The optional `args` are passed to the callback function.
If the callback function throws an error, the error is thrown by `run()` too. The stacktrace is not impacted by this call and the context is exited.
Example:
```
const store = { id: 2 };
try {
  asyncLocalStorage.run(store, () => {
    asyncLocalStorage.getStore(); // Returns the store object
    setTimeout(() => {
      asyncLocalStorage.getStore(); // Returns the store object
    }, 200);
    throw new Error();
  });
} catch (e) {
  asyncLocalStorage.getStore(); // Returns undefined
  // The error will be caught here
}
copy
```

####  `asyncLocalStorage.exit(callback[, ...args])`[#](https://nodejs.org/docs/latest/api/async_context.html#asynclocalstorageexitcallback-args)
Added in: v13.10.0, v12.17.0
Stability: 1 - Experimental
  * `callback`
  * `...args`


Runs a function synchronously outside of a context and returns its return value. The store is not accessible within the callback function or the asynchronous operations created within the callback. Any `getStore()` call done within the callback function will always return `undefined`.
The optional `args` are passed to the callback function.
If the callback function throws an error, the error is thrown by `exit()` too. The stacktrace is not impacted by this call and the context is re-entered.
Example:
```
// Within a call to run
try {
  asyncLocalStorage.getStore(); // Returns the store object or value
  asyncLocalStorage.exit(() => {
    asyncLocalStorage.getStore(); // Returns undefined
    throw new Error();
  });
} catch (e) {
  asyncLocalStorage.getStore(); // Returns the same object or value
  // The error will be caught here
}
copy
```

#### Usage with `async/await`[#](https://nodejs.org/docs/latest/api/async_context.html#usage-with-asyncawait)
If, within an async function, only one `await` call is to run within a context, the following pattern should be used:
```
async function fn() {
  await asyncLocalStorage.run(new Map(), () => {
    asyncLocalStorage.getStore().set('key', value);
    return foo(); // The return value of foo will be awaited
  });
}
copy
```

In this example, the store is only available in the callback function and the functions called by `foo`. Outside of `run`, calling `getStore` will return `undefined`.
#### Troubleshooting: Context loss[#](https://nodejs.org/docs/latest/api/async_context.html#troubleshooting-context-loss)
In most cases, `AsyncLocalStorage` works without issues. In rare situations, the current store is lost in one of the asynchronous operations.
If your code is callback-based, it is enough to promisify it with [`util.promisify()`](https://nodejs.org/docs/latest/api/util.html#utilpromisifyoriginal) so it starts working with native promises.
If you need to use a callback-based API or your code assumes a custom thenable implementation, use the [`AsyncResource`](https://nodejs.org/docs/latest/api/async_context.html#class-asyncresource) class to associate the asynchronous operation with the correct execution context. Find the function call responsible for the context loss by logging the content of `asyncLocalStorage.getStore()` after the calls you suspect are responsible for the loss. When the code logs `undefined`, the last callback called is probably responsible for the context loss.
### Class: `AsyncResource`[#](https://nodejs.org/docs/latest/api/async_context.html#class-asyncresource)
History Version | Changes
---|---
v16.4.0 | AsyncResource is now Stable. Previously, it had been Experimental.
The class `AsyncResource` is designed to be extended by the embedder's async resources. Using this, users can easily trigger the lifetime events of their own resources.
The `init` hook will trigger when an `AsyncResource` is instantiated.
The following is an overview of the `AsyncResource` API.
```
import { AsyncResource, executionAsyncId } from 'node:async_hooks';

// AsyncResource() is meant to be extended. Instantiating a
// new AsyncResource() also triggers init. If triggerAsyncId is omitted then
// async_hook.executionAsyncId() is used.
const asyncResource = new AsyncResource(
  type, { triggerAsyncId: executionAsyncId(), requireManualDestroy: false },
);

// Run a function in the execution context of the resource. This will
// * establish the context of the resource
// * trigger the AsyncHooks before callbacks
// * call the provided function `fn` with the supplied arguments
// * trigger the AsyncHooks after callbacks
// * restore the original execution context
asyncResource.runInAsyncScope(fn, thisArg, ...args);

// Call AsyncHooks destroy callbacks.
asyncResource.emitDestroy();

// Return the unique ID assigned to the AsyncResource instance.
asyncResource.asyncId();

// Return the trigger ID for the AsyncResource instance.
asyncResource.triggerAsyncId();
const { AsyncResource, executionAsyncId } = require('node:async_hooks');

// AsyncResource() is meant to be extended. Instantiating a
// new AsyncResource() also triggers init. If triggerAsyncId is omitted then
// async_hook.executionAsyncId() is used.
const asyncResource = new AsyncResource(
  type, { triggerAsyncId: executionAsyncId(), requireManualDestroy: false },
);

// Run a function in the execution context of the resource. This will
// * establish the context of the resource
// * trigger the AsyncHooks before callbacks
// * call the provided function `fn` with the supplied arguments
// * trigger the AsyncHooks after callbacks
// * restore the original execution context
asyncResource.runInAsyncScope(fn, thisArg, ...args);

// Call AsyncHooks destroy callbacks.
asyncResource.emitDestroy();

// Return the unique ID assigned to the AsyncResource instance.
asyncResource.asyncId();

// Return the trigger ID for the AsyncResource instance.
asyncResource.triggerAsyncId();
copy
```

####  `new AsyncResource(type[, options])`[#](https://nodejs.org/docs/latest/api/async_context.html#new-asyncresourcetype-options)
  * `type`
  * `options`
    * `triggerAsyncId` **Default:** `executionAsyncId()`.
    * `requireManualDestroy` `true`, disables `emitDestroy` when the object is garbage collected. This usually does not need to be set (even if `emitDestroy` is called manually), unless the resource's `asyncId` is retrieved and the sensitive API's `emitDestroy` is called with it. When set to `false`, the `emitDestroy` call on garbage collection will only take place if there is at least one active `destroy` hook. **Default:** `false`.


Example usage:
```
class DBQuery extends AsyncResource {
  constructor(db) {
    super('DBQuery');
    this.db = db;
  }

  getInfo(query, callback) {
    this.db.get(query, (err, data) => {
      this.runInAsyncScope(callback, null, err, data);
    });
  }

  close() {
    this.db = null;
    this.emitDestroy();
  }
}
copy
```

#### Static method: `AsyncResource.bind(fn[, type[, thisArg]])`[#](https://nodejs.org/docs/latest/api/async_context.html#static-method-asyncresourcebindfn-type-thisarg)
Added in: v14.8.0, v12.19.0History Version | Changes
---|---
v20.0.0 | The `asyncResource` property added to the bound function has been deprecated and will be removed in a future version.
v17.8.0, v16.15.0 | Changed the default when `thisArg` is undefined to use `this` from the caller.
v16.0.0 | Added optional thisArg.
  * `fn`
  * `type` `AsyncResource`.
  * `thisArg`


Binds the given function to the current execution context.
####  `asyncResource.bind(fn[, thisArg])`[#](https://nodejs.org/docs/latest/api/async_context.html#asyncresourcebindfn-thisarg)
Added in: v14.8.0, v12.19.0History Version | Changes
---|---
v20.0.0 | The `asyncResource` property added to the bound function has been deprecated and will be removed in a future version.
v17.8.0, v16.15.0 | Changed the default when `thisArg` is undefined to use `this` from the caller.
v16.0.0 | Added optional thisArg.
  * `fn` `AsyncResource`.
  * `thisArg`


Binds the given function to execute to this `AsyncResource`'s scope.
####  `asyncResource.runInAsyncScope(fn[, thisArg, ...args])`[#](https://nodejs.org/docs/latest/api/async_context.html#asyncresourceruninasyncscopefn-thisarg-args)
Added in: v9.6.0
  * `fn`
  * `thisArg`
  * `...args`


Call the provided function with the provided arguments in the execution context of the async resource. This will establish the context, trigger the AsyncHooks before callbacks, call the function, trigger the AsyncHooks after callbacks, and then restore the original execution context.
####  `asyncResource.emitDestroy()`[#](https://nodejs.org/docs/latest/api/async_context.html#asyncresourceemitdestroy)
  * Returns: [`<AsyncResource>`](https://nodejs.org/docs/latest/api/async_hooks.html#class-asyncresource) A reference to `asyncResource`.


Call all `destroy` hooks. This should only ever be called once. An error will be thrown if it is called more than once. This **must** be manually called. If the resource is left to be collected by the GC then the `destroy` hooks will never be called.
####  `asyncResource.asyncId()`[#](https://nodejs.org/docs/latest/api/async_context.html#asyncresourceasyncid)
  * Returns: `asyncId` assigned to the resource.


####  `asyncResource.triggerAsyncId()`[#](https://nodejs.org/docs/latest/api/async_context.html#asyncresourcetriggerasyncid)
  * Returns: `triggerAsyncId` that is passed to the `AsyncResource` constructor.


#### Using `AsyncResource` for a `Worker` thread pool[#](https://nodejs.org/docs/latest/api/async_context.html#using-asyncresource-for-a-worker-thread-pool)
The following example shows how to use the `AsyncResource` class to properly provide async tracking for a [`Worker`](https://nodejs.org/docs/latest/api/worker_threads.html#class-worker) pool. Other resource pools, such as database connection pools, can follow a similar model.
Assuming that the task is adding two numbers, using a file named `task_processor.js` with the following content:
```
import { parentPort } from 'node:worker_threads';
parentPort.on('message', (task) => {
  parentPort.postMessage(task.a + task.b);
});
const { parentPort } = require('node:worker_threads');
parentPort.on('message', (task) => {
  parentPort.postMessage(task.a + task.b);
});
copy
```

a Worker pool around it could use the following structure:
```
import { AsyncResource } from 'node:async_hooks';
import { EventEmitter } from 'node:events';
import { Worker } from 'node:worker_threads';

const kTaskInfo = Symbol('kTaskInfo');
const kWorkerFreedEvent = Symbol('kWorkerFreedEvent');

class WorkerPoolTaskInfo extends AsyncResource {
  constructor(callback) {
    super('WorkerPoolTaskInfo');
    this.callback = callback;
  }

  done(err, result) {
    this.runInAsyncScope(this.callback, null, err, result);
    this.emitDestroy();  // `TaskInfo`s are used only once.
  }
}

export default class WorkerPool extends EventEmitter {
  constructor(numThreads) {
    super();
    this.numThreads = numThreads;
    this.workers = [];
    this.freeWorkers = [];
    this.tasks = [];

    for (let i = 0; i < numThreads; i++)
      this.addNewWorker();

    // Any time the kWorkerFreedEvent is emitted, dispatch
    // the next task pending in the queue, if any.
    this.on(kWorkerFreedEvent, () => {
      if (this.tasks.length > 0) {
        const { task, callback } = this.tasks.shift();
        this.runTask(task, callback);
      }
    });
  }

  addNewWorker() {
    const worker = new Worker(new URL('task_processor.js', import.meta.url));
    worker.on('message', (result) => {
      // In case of success: Call the callback that was passed to `runTask`,
      // remove the `TaskInfo` associated with the Worker, and mark it as free
      // again.
      worker[kTaskInfo].done(null, result);
      worker[kTaskInfo] = null;
      this.freeWorkers.push(worker);
      this.emit(kWorkerFreedEvent);
    });
    worker.on('error', (err) => {
      // In case of an uncaught exception: Call the callback that was passed to
      // `runTask` with the error.
      if (worker[kTaskInfo])
        worker[kTaskInfo].done(err, null);
      else
        this.emit('error', err);
      // Remove the worker from the list and start a new Worker to replace the
      // current one.
      this.workers.splice(this.workers.indexOf(worker), 1);
      this.addNewWorker();
    });
    this.workers.push(worker);
    this.freeWorkers.push(worker);
    this.emit(kWorkerFreedEvent);
  }

  runTask(task, callback) {
    if (this.freeWorkers.length === 0) {
      // No free threads, wait until a worker thread becomes free.
      this.tasks.push({ task, callback });
      return;
    }

    const worker = this.freeWorkers.pop();
    worker[kTaskInfo] = new WorkerPoolTaskInfo(callback);
    worker.postMessage(task);
  }

  close() {
    for (const worker of this.workers) worker.terminate();
  }
}
const { AsyncResource } = require('node:async_hooks');
const { EventEmitter } = require('node:events');
const path = require('node:path');
const { Worker } = require('node:worker_threads');

const kTaskInfo = Symbol('kTaskInfo');
const kWorkerFreedEvent = Symbol('kWorkerFreedEvent');

class WorkerPoolTaskInfo extends AsyncResource {
  constructor(callback) {
    super('WorkerPoolTaskInfo');
    this.callback = callback;
  }

  done(err, result) {
    this.runInAsyncScope(this.callback, null, err, result);
    this.emitDestroy();  // `TaskInfo`s are used only once.
  }
}

class WorkerPool extends EventEmitter {
  constructor(numThreads) {
    super();
    this.numThreads = numThreads;
    this.workers = [];
    this.freeWorkers = [];
    this.tasks = [];

    for (let i = 0; i < numThreads; i++)
      this.addNewWorker();

    // Any time the kWorkerFreedEvent is emitted, dispatch
    // the next task pending in the queue, if any.
    this.on(kWorkerFreedEvent, () => {
      if (this.tasks.length > 0) {
        const { task, callback } = this.tasks.shift();
        this.runTask(task, callback);
      }
    });
  }

  addNewWorker() {
    const worker = new Worker(path.resolve(__dirname, 'task_processor.js'));
    worker.on('message', (result) => {
      // In case of success: Call the callback that was passed to `runTask`,
      // remove the `TaskInfo` associated with the Worker, and mark it as free
      // again.
      worker[kTaskInfo].done(null, result);
      worker[kTaskInfo] = null;
      this.freeWorkers.push(worker);
      this.emit(kWorkerFreedEvent);
    });
    worker.on('error', (err) => {
      // In case of an uncaught exception: Call the callback that was passed to
      // `runTask` with the error.
      if (worker[kTaskInfo])
        worker[kTaskInfo].done(err, null);
      else
        this.emit('error', err);
      // Remove the worker from the list and start a new Worker to replace the
      // current one.
      this.workers.splice(this.workers.indexOf(worker), 1);
      this.addNewWorker();
    });
    this.workers.push(worker);
    this.freeWorkers.push(worker);
    this.emit(kWorkerFreedEvent);
  }

  runTask(task, callback) {
    if (this.freeWorkers.length === 0) {
      // No free threads, wait until a worker thread becomes free.
      this.tasks.push({ task, callback });
      return;
    }

    const worker = this.freeWorkers.pop();
    worker[kTaskInfo] = new WorkerPoolTaskInfo(callback);
    worker.postMessage(task);
  }

  close() {
    for (const worker of this.workers) worker.terminate();
  }
}

module.exports = WorkerPool;
copy
```

Without the explicit tracking added by the `WorkerPoolTaskInfo` objects, it would appear that the callbacks are associated with the individual `Worker` objects. However, the creation of the `Worker`s is not associated with the creation of the tasks and does not provide information about when tasks were scheduled.
This pool could be used as follows:
```
import WorkerPool from './worker_pool.js';
import os from 'node:os';

const pool = new WorkerPool(os.availableParallelism());

let finished = 0;
for (let i = 0; i < 10; i++) {
  pool.runTask({ a: 42, b: 100 }, (err, result) => {
    console.log(i, err, result);
    if (++finished === 10)
      pool.close();
  });
}
const WorkerPool = require('./worker_pool.js');
const os = require('node:os');

const pool = new WorkerPool(os.availableParallelism());

let finished = 0;
for (let i = 0; i < 10; i++) {
  pool.runTask({ a: 42, b: 100 }, (err, result) => {
    console.log(i, err, result);
    if (++finished === 10)
      pool.close();
  });
}
copy
```

#### Integrating `AsyncResource` with `EventEmitter`[#](https://nodejs.org/docs/latest/api/async_context.html#integrating-asyncresource-with-eventemitter)
Event listeners triggered by an [`EventEmitter`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) may be run in a different execution context than the one that was active when `eventEmitter.on()` was called.
The following example shows how to use the `AsyncResource` class to properly associate an event listener with the correct execution context. The same approach can be applied to a [`Stream`](https://nodejs.org/docs/latest/api/stream.html#stream) or a similar event-driven class.
```
import { createServer } from 'node:http';
import { AsyncResource, executionAsyncId } from 'node:async_hooks';

const server = createServer((req, res) => {
  req.on('close', AsyncResource.bind(() => {
    // Execution context is bound to the current outer scope.
  }));
  req.on('close', () => {
    // Execution context is bound to the scope that caused 'close' to emit.
  });
  res.end();
}).listen(3000);
const { createServer } = require('node:http');
const { AsyncResource, executionAsyncId } = require('node:async_hooks');

const server = createServer((req, res) => {
  req.on('close', AsyncResource.bind(() => {
    // Execution context is bound to the current outer scope.
  }));
  req.on('close', () => {
    // Execution context is bound to the scope that caused 'close' to emit.
  });
  res.end();
}).listen(3000);
copy
```
