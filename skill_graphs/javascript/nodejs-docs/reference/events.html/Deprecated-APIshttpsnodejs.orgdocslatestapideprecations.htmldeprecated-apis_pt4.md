```
const fsPromises = require('node:fs').promises;
async function openAndClose() {
  let filehandle;
  try {
    filehandle = await fsPromises.open('thefile.txt', 'r');
  } finally {
    if (filehandle !== undefined)
      await filehandle.close();
  }
}
copy
```

#### DEP0138: `process.mainModule`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0138-processmainmodule)
History Version | Changes
---|---
v14.0.0 | Documentation-only deprecation.
Type: Documentation-only
[`process.mainModule`](https://nodejs.org/docs/latest/api/process.html#processmainmodule) is a CommonJS-only feature while `process` global object is shared with non-CommonJS environment. Its use within ECMAScript modules is unsupported.
It is deprecated in favor of [`require.main`](https://nodejs.org/docs/latest/api/modules.html#accessing-the-main-module), because it serves the same purpose and is only available on CommonJS environment.
An automated migration is available (
```
npx codemod@latest @nodejs/process-main-module
copy
```

#### DEP0139: `process.umask()` with no arguments[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0139-processumask-with-no-arguments)
History Version | Changes
---|---
v14.0.0, v12.19.0 | Documentation-only deprecation.
Type: Documentation-only
Calling `process.umask()` with no argument causes the process-wide umask to be written twice. This introduces a race condition between threads, and is a potential security vulnerability. There is no safe, cross-platform alternative API.
#### DEP0140: Use `request.destroy()` instead of `request.abort()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0140-use-requestdestroy-instead-of-requestabort)
History Version | Changes
---|---
v14.1.0, v13.14.0 | Documentation-only deprecation.
Type: Documentation-only
Use [`request.destroy()`](https://nodejs.org/docs/latest/api/http.html#requestdestroyerror) instead of [`request.abort()`](https://nodejs.org/docs/latest/api/http.html#requestabort).
#### DEP0141: `repl.inputStream` and `repl.outputStream`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0141-replinputstream-and-reploutputstream)
History Version | Changes
---|---
v14.3.0 | Documentation-only deprecation with `--pending-deprecation` support.
Type: Documentation-only (supports [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation))
The `node:repl` module exported the input and output stream twice. Use `.input` instead of `.inputStream` and `.output` instead of `.outputStream`.
#### DEP0142: `repl._builtinLibs`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0142-repl-builtinlibs)
History Version | Changes
---|---
v14.3.0 | Documentation-only deprecation with `--pending-deprecation` support.
Type: Documentation-only (supports [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation))
The `node:repl` module exports a `_builtinLibs` property that contains an array of built-in modules. It was incomplete so far and instead it's better to rely upon `require('node:module').builtinModules`.
An automated migration is available (
```
npx codemod@latest @nodejs/repl-builtin-modules
copy
```

#### DEP0143: `Transform._transformState`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0143-transform-transformstate)
History Version | Changes
---|---
v15.0.0 | End-of-Life.
v14.5.0 | Runtime deprecation.
Type: End-of-Life
`Transform._transformState` will be removed in future versions where it is no longer required due to simplification of the implementation.
#### DEP0144: `module.parent`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0144-moduleparent)
History Version | Changes
---|---
v14.6.0, v12.19.0 | Documentation-only deprecation.
Type: Documentation-only (supports [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation))
A CommonJS module can access the first module that required it using `module.parent`. This feature is deprecated because it does not work consistently in the presence of ECMAScript modules and because it gives an inaccurate representation of the CommonJS module graph.
Some modules use it to check if they are the entry point of the current process. Instead, it is recommended to compare `require.main` and `module`:
```
if (require.main === module) {
  // Code section that will run only if current file is the entry point.
}
copy
```

When looking for the CommonJS modules that have required the current one, `require.cache` and `module.children` can be used:
```
const moduleParents = Object.values(require.cache)
  .filter((m) => m.children.includes(module));
copy
```

#### DEP0145: `socket.bufferSize`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0145-socketbuffersize)
History Version | Changes
---|---
v14.6.0 | Documentation-only deprecation.
Type: Documentation-only
[`socket.bufferSize`](https://nodejs.org/docs/latest/api/net.html#socketbuffersize) is just an alias for [`writable.writableLength`](https://nodejs.org/docs/latest/api/stream.html#writablewritablelength).
#### DEP0146: `new crypto.Certificate()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0146-new-cryptocertificate)
History Version | Changes
---|---
v14.9.0 | Documentation-only deprecation.
Type: Documentation-only
The [`crypto.Certificate()` constructor](https://nodejs.org/docs/latest/api/crypto.html#legacy-api) is deprecated. Use [static methods of `crypto.Certificate()`](https://nodejs.org/docs/latest/api/crypto.html#class-certificate) instead.
#### DEP0147: `fs.rmdir(path, { recursive: true })`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0147-fsrmdirpath-recursive-true)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v16.0.0 | Runtime deprecation.
v15.0.0 | Runtime deprecation for permissive behavior.
v14.14.0 | Documentation-only deprecation.
Type: End-of-Life
The `fs.rmdir`, `fs.rmdirSync`, and `fs.promises.rmdir` methods used to support a `recursive` option. That option has been removed.
Use `fs.rm(path, { recursive: true, force: true })`, `fs.rmSync(path, { recursive: true, force: true })` or `fs.promises.rm(path, { recursive: true, force: true })` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/rmdir
copy
```

#### DEP0148: Folder mappings in `"exports"` (trailing `"/"`)[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0148-folder-mappings-in-exports-trailing)
History Version | Changes
---|---
v17.0.0 | End-of-Life.
v16.0.0 | Runtime deprecation.
v15.1.0 | Runtime deprecation for self-referencing imports.
v14.13.0 | Documentation-only deprecation.
Type: End-of-Life
Using a trailing `"/"` to define subpath folder mappings in the [subpath exports](https://nodejs.org/docs/latest/api/packages.html#subpath-exports) or [subpath imports](https://nodejs.org/docs/latest/api/packages.html#subpath-imports) fields is no longer supported. Use [subpath patterns](https://nodejs.org/docs/latest/api/packages.html#subpath-patterns) instead.
#### DEP0149: `http.IncomingMessage#connection`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0149-httpincomingmessageconnection)
History Version | Changes
---|---
v16.0.0 | Documentation-only deprecation.
Type: Documentation-only
Prefer [`message.socket`](https://nodejs.org/docs/latest/api/http.html#messagesocket) over [`message.connection`](https://nodejs.org/docs/latest/api/http.html#messageconnection).
#### DEP0150: Changing the value of `process.config`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0150-changing-the-value-of-processconfig)
History Version | Changes
---|---
v19.0.0 | End-of-Life.
v16.0.0 | Runtime deprecation.
Type: End-of-Life
The `process.config` property provides access to Node.js compile-time settings. However, the property is mutable and therefore subject to tampering. The ability to change the value will be removed in a future version of Node.js.
#### DEP0151: Main index lookup and extension searching[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0151-main-index-lookup-and-extension-searching)
History Version | Changes
---|---
v16.0.0 | Runtime deprecation.
v15.8.0, v14.18.0 | Documentation-only deprecation with `--pending-deprecation` support.
Type: Runtime
Previously, `index.js` and extension searching lookups would apply to `import 'pkg'` main entry point resolution, even when resolving ES modules.
With this deprecation, all ES module main entry point resolutions require an explicit [`"exports"` or `"main"` entry](https://nodejs.org/docs/latest/api/packages.html#main-entry-point-export) with the exact file extension.
#### DEP0152: Extension PerformanceEntry properties[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0152-extension-performanceentry-properties)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v16.0.0 | Runtime deprecation.
Type: End-of-Life
The `'gc'`, `'http2'`, and `'http'` [`<PerformanceEntry>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry) object types used to have additional properties assigned to them that provide additional information. These properties are now available within the standard `detail` property of the `PerformanceEntry` object. The deprecated accessors have been removed.
#### DEP0153: `dns.lookup` and `dnsPromises.lookup` options type coercion[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0153-dnslookup-and-dnspromiseslookup-options-type-coercion)
History Version | Changes
---|---
v18.0.0 | End-of-Life.
v17.0.0 | Runtime deprecation.
v16.8.0 | Documentation-only deprecation.
Type: End-of-Life
Using a non-nullish non-integer value for `family` option, a non-nullish non-number value for `hints` option, a non-nullish non-boolean value for `all` option, or a non-nullish non-boolean value for `verbatim` option in [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) and [`dnsPromises.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnspromiseslookuphostname-options) throws an `ERR_INVALID_ARG_TYPE` error.
#### DEP0154: RSA-PSS generate key pair options[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0154-rsa-pss-generate-key-pair-options)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v20.0.0 | Runtime deprecation.
v16.10.0 | Documentation-only deprecation.
Type: End-of-Life
Use `'hashAlgorithm'` instead of `'hash'`, and `'mgf1HashAlgorithm'` instead of `'mgf1Hash'`.
An automated migration is available (
```
npx codemod@latest @nodejs/crypto-rsa-pss-update
copy
```

#### DEP0155: Trailing slashes in pattern specifier resolutions[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0155-trailing-slashes-in-pattern-specifier-resolutions)
History Version | Changes
---|---
v17.0.0 | Runtime deprecation.
v16.10.0 | Documentation-only deprecation with `--pending-deprecation` support.
Type: Runtime
The remapping of specifiers ending in `"/"` like `import 'pkg/x/'` is deprecated for package `"exports"` and `"imports"` pattern resolutions.
#### DEP0156: `.aborted` property and `'abort'`, `'aborted'` event in `http`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0156-aborted-property-and-abort-aborted-event-in-http)
History Version | Changes
---|---
v17.0.0, v16.12.0 | Documentation-only deprecation.
Type: Documentation-only
Move to [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) API instead, as the [`http.ClientRequest`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest), [`http.ServerResponse`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse), and [`http.IncomingMessage`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage) are all stream-based. Check `stream.destroyed` instead of the `.aborted` property, and listen for `'close'` instead of `'abort'`, `'aborted'` event.
The `.aborted` property and `'abort'` event are only useful for detecting `.abort()` calls. For closing a request early, use the Stream `.destroy([error])` then check the `.destroyed` property and `'close'` event should have the same effect. The receiving end should also check the [`readable.readableEnded`](https://nodejs.org/docs/latest/api/stream.html#readablereadableended) value on [`http.IncomingMessage`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage) to get whether it was an aborted or graceful destroy.
#### DEP0157: Thenable support in streams[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0157-thenable-support-in-streams)
History Version | Changes
---|---
v18.0.0 | End-of-life.
v17.2.0, v16.14.0 | Documentation-only deprecation.
Type: End-of-Life
An undocumented feature of Node.js streams was to support thenables in implementation methods. This is now deprecated, use callbacks instead and avoid use of async function for streams implementation methods.
This feature caused users to encounter unexpected problems where the user implements the function in callback style but uses e.g. an async method which would cause an error since mixing promise and callback semantics is not valid.
```
const w = new Writable({
  async final(callback) {
    await someOp();
    callback();
  },
});
copy
```

#### DEP0158: `buffer.slice(start, end)`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0158-bufferslicestart-end)
History Version | Changes
---|---
v17.5.0, v16.15.0 | Documentation-only deprecation.
Type: Documentation-only
This method was deprecated because it is not compatible with `Uint8Array.prototype.slice()`, which is a superclass of `Buffer`.
Use [`buffer.subarray`](https://nodejs.org/docs/latest/api/buffer.html#bufsubarraystart-end) which does the same thing instead.
#### DEP0159: `ERR_INVALID_CALLBACK`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0159-err-invalid-callback)
History Version | Changes
---|---
v18.0.0 | End-of-Life.
Type: End-of-Life
This error code was removed due to adding more confusion to the errors used for value type validation.
#### DEP0160: `process.on('multipleResolves', handler)`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0160-processonmultipleresolves-handler)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v18.0.0 | Runtime deprecation.
v17.6.0, v16.15.0 | Documentation-only deprecation.
Type: End-of-Life
This event was deprecated and removed because it did not work with V8 promise combinators which diminished its usefulness.
#### DEP0161: `process._getActiveRequests()` and `process._getActiveHandles()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0161-process-getactiverequests-and-process-getactivehandles)
History Version | Changes
---|---
v17.6.0, v16.15.0 | Documentation-only deprecation.
Type: Documentation-only
The `process._getActiveHandles()` and `process._getActiveRequests()` functions are not intended for public use and can be removed in future releases.
Use [`process.getActiveResourcesInfo()`](https://nodejs.org/docs/latest/api/process.html#processgetactiveresourcesinfo) to get a list of types of active resources and not the actual references.
#### DEP0162: `fs.write()`, `fs.writeFileSync()` coercion to string[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0162-fswrite-fswritefilesync-coercion-to-string)
History Version | Changes
---|---
v19.0.0 | End-of-Life.
v18.0.0 | Runtime deprecation.
v17.8.0, v16.15.0 | Documentation-only deprecation.
Type: End-of-Life
Implicit coercion of objects with own `toString` property, passed as second parameter in [`fs.write()`](https://nodejs.org/docs/latest/api/fs.html#fswritefd-buffer-offset-length-position-callback), [`fs.writeFile()`](https://nodejs.org/docs/latest/api/fs.html#fswritefilefile-data-options-callback), [`fs.appendFile()`](https://nodejs.org/docs/latest/api/fs.html#fsappendfilepath-data-options-callback), [`fs.writeFileSync()`](https://nodejs.org/docs/latest/api/fs.html#fswritefilesyncfile-data-options), and [`fs.appendFileSync()`](https://nodejs.org/docs/latest/api/fs.html#fsappendfilesyncpath-data-options) is deprecated. Convert them to primitive strings.
#### DEP0163: `channel.subscribe(onMessage)`, `channel.unsubscribe(onMessage)`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0163-channelsubscribeonmessage-channelunsubscribeonmessage)
History Version | Changes
---|---
v24.8.0, v22.20.0 | Deprecation revoked.
v18.7.0, v16.17.0 | Documentation-only deprecation.
Type: Deprecation revoked
These methods were deprecated because their use could leave the channel object vulnerable to being garbage-collected if not strongly referenced by the user. The deprecation was revoked because channel objects are now resistant to garbage collection when the channel has active subscribers.
#### DEP0164: `process.exit(code)`, `process.exitCode` coercion to integer[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0164-processexitcode-processexitcode-coercion-to-integer)
History Version | Changes
---|---
v20.0.0 | End-of-Life.
v19.0.0 | Runtime deprecation.
v18.10.0, v16.18.0 | Documentation-only deprecation of `process.exitCode` integer coercion.
v18.7.0, v16.17.0 | Documentation-only deprecation of `process.exit(code)` integer coercion.
Type: End-of-Life
Values other than `undefined`, `null`, integer numbers, and integer strings (e.g., `'1'`) are deprecated as value for the `code` parameter in [`process.exit()`](https://nodejs.org/docs/latest/api/process.html#processexitcode) and as value to assign to [`process.exitCode`](https://nodejs.org/docs/latest/api/process.html#processexitcode_1).
#### DEP0165: `--trace-atomics-wait`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0165-trace-atomics-wait)
History Version | Changes
---|---
v23.0.0 | End-of-Life.
v22.0.0 | Runtime deprecation.
v18.8.0, v16.18.0 | Documentation-only deprecation.
Type: End-of-Life
The `--trace-atomics-wait` flag has been removed because it uses the V8 hook `SetAtomicsWaitCallback`, that will be removed in a future V8 release.
#### DEP0166: Double slashes in imports and exports targets[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0166-double-slashes-in-imports-and-exports-targets)
History Version | Changes
---|---
v19.0.0 | Runtime deprecation.
v18.10.0 | Documentation-only deprecation with `--pending-deprecation` support.
Type: Runtime
Package imports and exports targets mapping into paths including a double slash (of _"/"_ or _"\"_) are deprecated and will fail with a resolution validation error in a future release. This same deprecation also applies to pattern matches starting or ending in a slash.
#### DEP0167: Weak `DiffieHellmanGroup` instances (`modp1`, `modp2`, `modp5`)[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0167-weak-diffiehellmangroup-instances-modp1-modp2-modp5)
History Version | Changes
---|---
v18.10.0, v16.18.0 | Documentation-only deprecation.
Type: Documentation-only
The well-known MODP groups `modp1`, `modp2`, and `modp5` are deprecated because they are not secure against practical attacks. See
These groups might be removed in future versions of Node.js. Applications that rely on these groups should evaluate using stronger MODP groups instead.
#### DEP0168: Unhandled exception in Node-API callbacks[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0168-unhandled-exception-in-node-api-callbacks)
History Version | Changes
---|---
v18.3.0, v16.17.0 | Runtime deprecation.
Type: Runtime
The implicit suppression of uncaught exceptions in Node-API callbacks is now deprecated.
Set the flag [`--force-node-api-uncaught-exceptions-policy`](https://nodejs.org/docs/latest/api/cli.html#--force-node-api-uncaught-exceptions-policy) to force Node.js to emit an [`'uncaughtException'`](https://nodejs.org/docs/latest/api/process.html#event-uncaughtexception) event if the exception is not handled in Node-API callbacks.
#### DEP0169: Insecure url.parse()[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0169-insecure-urlparse)
History Version | Changes
---|---
v24.0.0 | Application deprecation.
v19.9.0, v18.17.0 | Added support for `--pending-deprecation`.
v19.0.0, v18.13.0 | Documentation-only deprecation.
Type: Application (non-`node_modules` code only)
[`url.parse()`](https://nodejs.org/docs/latest/api/url.html#urlparseurlstring-parsequerystring-slashesdenotehost) behavior is not standardized and prone to errors that have security implications. Use the [WHATWG URL API](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) instead. CVEs are not issued for `url.parse()` vulnerabilities.
Passing a string argument to [`url.format()`](https://nodejs.org/docs/latest/api/url.html#urlformaturlobject) invokes `url.parse()` internally, and is therefore also covered by this deprecation.
#### DEP0170: Invalid port when using `url.parse()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0170-invalid-port-when-using-urlparse)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v20.0.0 | Runtime deprecation.
v19.2.0, v18.13.0 | Documentation-only deprecation.
Type: End-of-Life
[`url.parse()`](https://nodejs.org/docs/latest/api/url.html#urlparseurlstring-parsequerystring-slashesdenotehost) used to accept URLs with ports that are not numbers. This behavior might result in host name spoofing with unexpected input. These URLs will throw an error (which the [WHATWG URL API](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) also does).
#### DEP0171: Setters for `http.IncomingMessage` headers and trailers[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0171-setters-for-httpincomingmessage-headers-and-trailers)
History Version | Changes
---|---
v19.3.0, v18.13.0 | Documentation-only deprecation.
Type: Documentation-only
In a future version of Node.js, [`message.headers`](https://nodejs.org/docs/latest/api/http.html#messageheaders), [`message.headersDistinct`](https://nodejs.org/docs/latest/api/http.html#messageheadersdistinct), [`message.trailers`](https://nodejs.org/docs/latest/api/http.html#messagetrailers), and [`message.trailersDistinct`](https://nodejs.org/docs/latest/api/http.html#messagetrailersdistinct) will be read-only.
#### DEP0172: The `asyncResource` property of `AsyncResource` bound functions[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0172-the-asyncresource-property-of-asyncresource-bound-functions)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v20.0.0 | Runtime-deprecation.
Type: End-of-Life
Older versions of Node.js would add the `asyncResource` when a function is bound to an `AsyncResource`. It no longer does.
#### DEP0173: the `assert.CallTracker` class[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0173-the-assertcalltracker-class)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v20.1.0 | Runtime deprecation.
Type: End-of-Life
The `assert.CallTracker` API has been removed.
#### DEP0174: calling `promisify` on a function that returns a `Promise`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0174-calling-promisify-on-a-function-that-returns-a-promise)
History Version | Changes
---|---
v21.0.0 | Runtime deprecation.
v20.8.0 | Documentation-only deprecation.
Type: Runtime
Calling [`util.promisify`](https://nodejs.org/docs/latest/api/util.html#utilpromisifyoriginal) on a function that returns a `Promise` will ignore the result of said promise, which can lead to unhandled promise rejections.
#### DEP0175: `util.toUSVString`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0175-utiltousvstring)
History Version | Changes
---|---
v20.8.0 | Documentation-only deprecation.
Type: Documentation-only
The [`util.toUSVString()`](https://nodejs.org/docs/latest/api/util.html#utiltousvstringstring) API is deprecated. Please use
#### DEP0176: `fs.F_OK`, `fs.R_OK`, `fs.W_OK`, `fs.X_OK`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0176-fsf-ok-fsr-ok-fsw-ok-fsx-ok)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v24.0.0 | Runtime deprecation.
v20.8.0 | Documentation-only deprecation.
Type: End-of-Life
`F_OK`, `R_OK`, `W_OK` and `X_OK` getters exposed directly on `node:fs` were removed. Get them from `fs.constants` or `fs.promises.constants` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/fs-access-mode-constants
copy
```

#### DEP0177: `util.types.isWebAssemblyCompiledModule`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0177-utiltypesiswebassemblycompiledmodule)
History Version | Changes
---|---
v21.7.0, v20.12.0 | End-of-Life.
v21.3.0, v20.11.0 | A deprecation code has been assigned.
v14.0.0 | Documentation-only deprecation.
Type: End-of-Life
The `util.types.isWebAssemblyCompiledModule` API has been removed. Please use `value instanceof WebAssembly.Module` instead.
#### DEP0178: `dirent.path`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0178-direntpath)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v23.0.0 | Runtime deprecation.
v21.5.0, v20.12.0, v18.20.0 | Documentation-only deprecation.
Type: End-of-Life
The `dirent.path` property has been removed due to its lack of consistency across release lines. Please use [`dirent.parentPath`](https://nodejs.org/docs/latest/api/fs.html#direntparentpath) instead.
