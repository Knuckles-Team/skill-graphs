## Deprecated APIs[#](https://nodejs.org/docs/latest/api/deprecations.html#deprecated-apis)
Node.js APIs might be deprecated for any of the following reasons:
  * Use of the API is unsafe.
  * An improved alternative API is available.
  * Breaking changes to the API are expected in a future major release.


Node.js uses four kinds of deprecations:
  * Documentation-only
  * Application (non-`node_modules` code only)
  * Runtime (all code)
  * End-of-Life


A Documentation-only deprecation is one that is expressed only within the Node.js API docs. These generate no side-effects while running Node.js. Some Documentation-only deprecations trigger a runtime warning when launched with [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation) flag (or its alternative, `NODE_PENDING_DEPRECATION=1` environment variable), similarly to Runtime deprecations below. Documentation-only deprecations that support that flag are explicitly labeled as such in the [list of Deprecated APIs](https://nodejs.org/docs/latest/api/deprecations.html#list-of-deprecated-apis).
An Application deprecation for only non-`node_modules` code will, by default, generate a process warning that will be printed to `stderr` the first time the deprecated API is used in code that's not loaded from `node_modules`. When the [`--throw-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--throw-deprecation) command-line flag is used, a Runtime deprecation will cause an error to be thrown. When [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation) is used, warnings will also be emitted for code loaded from `node_modules`.
A runtime deprecation for all code is similar to the runtime deprecation for non-`node_modules` code, except that it also emits a warning for code loaded from `node_modules`.
An End-of-Life deprecation is used when functionality is or will soon be removed from Node.js.
### Revoking deprecations[#](https://nodejs.org/docs/latest/api/deprecations.html#revoking-deprecations)
Occasionally, the deprecation of an API might be reversed. In such situations, this document will be updated with information relevant to the decision. However, the deprecation identifier will not be modified.
### List of deprecated APIs[#](https://nodejs.org/docs/latest/api/deprecations.html#list-of-deprecated-apis)
#### DEP0001: `http.OutgoingMessage.prototype.flush`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0001-httpoutgoingmessageprototypeflush)
History Version | Changes
---|---
v14.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v1.6.0 | Runtime deprecation.
Type: End-of-Life
`OutgoingMessage.prototype.flush()` has been removed. Use `OutgoingMessage.prototype.flushHeaders()` instead.
#### DEP0002: `require('_linklist')`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0002-require-linklist)
History Version | Changes
---|---
v8.0.0 | End-of-Life.
v6.12.0 | A deprecation code has been assigned.
v5.0.0 | Runtime deprecation.
Type: End-of-Life
The `_linklist` module is deprecated. Please use a userland alternative.
#### DEP0003: `_writableState.buffer`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0003-writablestatebuffer)
History Version | Changes
---|---
v14.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.11.15 | Runtime deprecation.
Type: End-of-Life
The `_writableState.buffer` has been removed. Use `_writableState.getBuffer()` instead.
#### DEP0004: `CryptoStream.prototype.readyState`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0004-cryptostreamprototypereadystate)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.4.0 | Documentation-only deprecation.
Type: End-of-Life
The `CryptoStream.prototype.readyState` property was removed.
#### DEP0005: `Buffer()` constructor[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0005-buffer-constructor)
History Version | Changes
---|---
v10.0.0 | Runtime deprecation.
v6.12.0 | A deprecation code has been assigned.
v6.0.0 | Documentation-only deprecation.
Type: Application (non-`node_modules` code only)
The `Buffer()` function and `new Buffer()` constructor are deprecated due to API usability issues that can lead to accidental security issues.
As an alternative, use one of the following methods of constructing `Buffer` objects:
  * [`Buffer.alloc(size[, fill[, encoding]])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocsize-fill-encoding): Create a `Buffer` with _initialized_ memory.
  * [`Buffer.allocUnsafe(size)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize): Create a `Buffer` with _uninitialized_ memory.
  * [`Buffer.allocUnsafeSlow(size)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafeslowsize): Create a `Buffer` with _uninitialized_ memory.
  * [`Buffer.from(array)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarray): Create a `Buffer` with a copy of `array`
  * [`Buffer.from(arrayBuffer[, byteOffset[, length]])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarraybuffer-byteoffset-length) - Create a `Buffer` that wraps the given `arrayBuffer`.
  * [`Buffer.from(buffer)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfrombuffer): Create a `Buffer` that copies `buffer`.
  * [`Buffer.from(string[, encoding])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromstring-encoding): Create a `Buffer` that copies `string`.


Without `--pending-deprecation`, runtime warnings occur only for code not in `node_modules`. This means there will not be deprecation warnings for `Buffer()` usage in dependencies. With `--pending-deprecation`, a runtime warning results no matter where the `Buffer()` usage occurs.
#### DEP0006: `child_process` `options.customFds`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0006-child-process-optionscustomfds)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.11.14 | Runtime deprecation.
v0.5.10 | Documentation-only deprecation.
Type: End-of-Life
Within the [`child_process`](https://nodejs.org/docs/latest/api/child_process.html) module's `spawn()`, `fork()`, and `exec()` methods, the `options.customFds` option is deprecated. The `options.stdio` option should be used instead.
#### DEP0007: Replace `cluster` `worker.suicide` with `worker.exitedAfterDisconnect`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0007-replace-cluster-workersuicide-with-workerexitedafterdisconnect)
History Version | Changes
---|---
v9.0.0 | End-of-Life.
v7.0.0 | Runtime deprecation.
v6.12.0 | A deprecation code has been assigned.
v6.0.0 | Documentation-only deprecation.
Type: End-of-Life
In an earlier version of the Node.js `cluster`, a boolean property with the name `suicide` was added to the `Worker` object. The intent of this property was to provide an indication of how and why the `Worker` instance exited. In Node.js 6.0.0, the old property was deprecated and replaced with a new [`worker.exitedAfterDisconnect`](https://nodejs.org/docs/latest/api/cluster.html#workerexitedafterdisconnect) property. The old property name did not precisely describe the actual semantics and was unnecessarily emotion-laden.
#### DEP0008: `require('node:constants')`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0008-requirenodeconstants)
History Version | Changes
---|---
v6.12.0 | A deprecation code has been assigned.
v6.3.0 | Documentation-only deprecation.
Type: Documentation-only
The `node:constants` module is deprecated. When requiring access to constants relevant to specific Node.js builtin modules, developers should instead refer to the `constants` property exposed by the relevant module. For instance, `require('node:fs').constants` and `require('node:os').constants`.
#### DEP0009: `crypto.pbkdf2` without digest[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0009-cryptopbkdf2-without-digest)
History Version | Changes
---|---
v14.0.0 | End-of-Life (for `digest === null`).
v11.0.0 | Runtime deprecation (for `digest === null`).
v8.0.0 | End-of-Life (for `digest === undefined`).
v6.12.0 | A deprecation code has been assigned.
v6.0.0 | Runtime deprecation (for `digest === undefined`).
Type: End-of-Life
Use of the [`crypto.pbkdf2()`](https://nodejs.org/docs/latest/api/crypto.html#cryptopbkdf2password-salt-iterations-keylen-digest-callback) API without specifying a digest was deprecated in Node.js 6.0 because the method defaulted to using the non-recommended `'SHA1'` digest. Previously, a deprecation warning was printed. Starting in Node.js 8.0.0, calling `crypto.pbkdf2()` or `crypto.pbkdf2Sync()` with `digest` set to `undefined` will throw a `TypeError`.
Beginning in Node.js 11.0.0, calling these functions with `digest` set to `null` would print a deprecation warning to align with the behavior when `digest` is `undefined`.
Now, however, passing either `undefined` or `null` will throw a `TypeError`.
#### DEP0010: `crypto.createCredentials`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0010-cryptocreatecredentials)
History Version | Changes
---|---
v11.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.11.13 | Runtime deprecation.
Type: End-of-Life
The `crypto.createCredentials()` API was removed. Please use [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) instead.
#### DEP0011: `crypto.Credentials`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0011-cryptocredentials)
History Version | Changes
---|---
v11.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.11.13 | Runtime deprecation.
Type: End-of-Life
The `crypto.Credentials` class was removed. Please use [`tls.SecureContext`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) instead.
#### DEP0012: `Domain.dispose`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0012-domaindispose)
History Version | Changes
---|---
v9.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.11.7 | Runtime deprecation.
Type: End-of-Life
`Domain.dispose()` has been removed. Recover from failed I/O actions explicitly via error event handlers set on the domain instead.
#### DEP0013: `fs` asynchronous function without callback[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0013-fs-asynchronous-function-without-callback)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
v7.0.0 | Runtime deprecation.
Type: End-of-Life
Calling an asynchronous function without a callback throws a `TypeError` in Node.js 10.0.0 onwards. See
#### DEP0014: `fs.read` legacy String interface[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0014-fsread-legacy-string-interface)
History Version | Changes
---|---
v8.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v6.0.0 | Runtime deprecation.
v0.1.96 | Documentation-only deprecation.
Type: End-of-Life
The [`fs.read()`](https://nodejs.org/docs/latest/api/fs.html#fsreadfd-buffer-offset-length-position-callback) legacy `String` interface is deprecated. Use the `Buffer` API as mentioned in the documentation instead.
#### DEP0015: `fs.readSync` legacy String interface[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0015-fsreadsync-legacy-string-interface)
History Version | Changes
---|---
v8.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v6.0.0 | Runtime deprecation.
v0.1.96 | Documentation-only deprecation.
Type: End-of-Life
The [`fs.readSync()`](https://nodejs.org/docs/latest/api/fs.html#fsreadsyncfd-buffer-offset-length-position) legacy `String` interface is deprecated. Use the `Buffer` API as mentioned in the documentation instead.
#### DEP0016: `GLOBAL`/`root`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0016-globalroot)
History Version | Changes
---|---
v14.0.0 | End-of-Life.
v6.12.0 | A deprecation code has been assigned.
v6.0.0 | Runtime deprecation.
Type: End-of-Life
The `GLOBAL` and `root` aliases for the `global` property were deprecated in Node.js 6.0.0 and have since been removed.
#### DEP0017: `Intl.v8BreakIterator`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0017-intlv8breakiterator)
History Version | Changes
---|---
v9.0.0 | End-of-Life.
v7.0.0 | Runtime deprecation.
Type: End-of-Life
`Intl.v8BreakIterator` was a non-standard extension and has been removed. See
#### DEP0018: Unhandled promise rejections[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0018-unhandled-promise-rejections)
History Version | Changes
---|---
v15.0.0 | End-of-Life.
v7.0.0 | Runtime deprecation.
Type: End-of-Life
Unhandled promise rejections are deprecated. By default, promise rejections that are not handled terminate the Node.js process with a non-zero exit code. To change the way Node.js treats unhandled rejections, use the [`--unhandled-rejections`](https://nodejs.org/docs/latest/api/cli.html#--unhandled-rejectionsmode) command-line option.
#### DEP0019: `require('.')` resolved outside directory[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0019-require-resolved-outside-directory)
History Version | Changes
---|---
v12.0.0 | Removed functionality.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v1.8.1 | Runtime deprecation.
Type: End-of-Life
In certain cases, `require('.')` could resolve outside the package directory. This behavior has been removed.
#### DEP0020: `Server.connections`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0020-serverconnections)
History Version | Changes
---|---
v15.0.0 | Server.connections has been removed.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.9.7 | Runtime deprecation.
Type: End-of-Life
The `Server.connections` property was deprecated in Node.js 0.9.7 and has been removed. Please use the [`Server.getConnections()`](https://nodejs.org/docs/latest/api/net.html#servergetconnectionscallback) method instead.
#### DEP0021: `Server.listenFD`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0021-serverlistenfd)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.7.12 | Runtime deprecation.
Type: End-of-Life
The `Server.listenFD()` method was deprecated and removed. Please use [`Server.listen({fd: <number>})`](https://nodejs.org/docs/latest/api/net.html#serverlistenhandle-backlog-callback) instead.
#### DEP0022: `os.tmpDir()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0022-ostmpdir)
History Version | Changes
---|---
v14.0.0 | End-of-Life.
v7.0.0 | Runtime deprecation.
Type: End-of-Life
The `os.tmpDir()` API was deprecated in Node.js 7.0.0 and has since been removed. Please use [`os.tmpdir()`](https://nodejs.org/docs/latest/api/os.html#ostmpdir) instead.
An automated migration is available (
```
npx codemod@latest @nodejs/tmpDir-to-tmpdir
copy
```

#### DEP0023: `os.getNetworkInterfaces()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0023-osgetnetworkinterfaces)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.6.0 | Runtime deprecation.
Type: End-of-Life
The `os.getNetworkInterfaces()` method is deprecated. Please use the [`os.networkInterfaces()`](https://nodejs.org/docs/latest/api/os.html#osnetworkinterfaces) method instead.
#### DEP0024: `REPLServer.prototype.convertToContext()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0024-replserverprototypeconverttocontext)
History Version | Changes
---|---
v9.0.0 | End-of-Life.
v7.0.0 | Runtime deprecation.
Type: End-of-Life
The `REPLServer.prototype.convertToContext()` API has been removed.
#### DEP0025: `require('node:sys')`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0025-requirenodesys)
History Version | Changes
---|---
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v1.0.0 | Runtime deprecation.
Type: Runtime
The `node:sys` module is deprecated. Please use the [`util`](https://nodejs.org/docs/latest/api/util.html) module instead.
#### DEP0026: `util.print()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0026-utilprint)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.11.3 | Runtime deprecation.
Type: End-of-Life
`util.print()` has been removed. Please use [`console.log()`](https://nodejs.org/docs/latest/api/console.html#consolelogdata-args) instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-print-to-console-log
copy
```

#### DEP0027: `util.puts()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0027-utilputs)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.11.3 | Runtime deprecation.
Type: End-of-Life
`util.puts()` has been removed. Please use [`console.log()`](https://nodejs.org/docs/latest/api/console.html#consolelogdata-args) instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-print-to-console-log
copy
```

#### DEP0028: `util.debug()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0028-utildebug)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.11.3 | Runtime deprecation.
Type: End-of-Life
`util.debug()` has been removed. Please use [`console.error()`](https://nodejs.org/docs/latest/api/console.html#consoleerrordata-args) instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-print-to-console-log
copy
```

#### DEP0029: `util.error()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0029-utilerror)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.11.3 | Runtime deprecation.
Type: End-of-Life
`util.error()` has been removed. Please use [`console.error()`](https://nodejs.org/docs/latest/api/console.html#consoleerrordata-args) instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-print-to-console-log
copy
```

#### DEP0030: `SlowBuffer`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0030-slowbuffer)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v24.0.0 | Runtime deprecation.
v6.12.0 | A deprecation code has been assigned.
v6.0.0 | Documentation-only deprecation.
Type: End-of-Life
The `SlowBuffer` class has been removed. Please use [`Buffer.allocUnsafeSlow(size)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafeslowsize) instead.
An automated migration is available (
```
npx codemod@latest @nodejs/slow-buffer-to-buffer-alloc-unsafe-slow
copy
```

#### DEP0031: `ecdh.setPublicKey()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0031-ecdhsetpublickey)
History Version | Changes
---|---
v25.0.0 | Runtime deprecation.
v6.12.0 | A deprecation code has been assigned.
v5.2.0 | Documentation-only deprecation.
Type: Runtime
The [`ecdh.setPublicKey()`](https://nodejs.org/docs/latest/api/crypto.html#ecdhsetpublickeypublickey-encoding) method is now deprecated as its inclusion in the API is not useful.
#### DEP0032: `node:domain` module[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0032-nodedomain-module)
History Version | Changes
---|---
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v1.4.2 | Documentation-only deprecation.
Type: Documentation-only
The [`domain`](https://nodejs.org/docs/latest/api/domain.html) module is deprecated and should not be used.
#### DEP0033: `EventEmitter.listenerCount()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0033-eventemitterlistenercount)
History Version | Changes
---|---
v25.4.0 | Deprecation revoked.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v3.2.0 | Documentation-only deprecation.
Type: Revoked
The [`events.listenerCount(emitter, eventName)`](https://nodejs.org/docs/latest/api/events.html#eventslistenercountemitterortarget-eventname) API was deprecated, as it provided identical functionality to [`emitter.listenerCount(eventName)`](https://nodejs.org/docs/latest/api/events.html#emitterlistenercounteventname-listener). The deprecation was revoked because this function has been repurposed to also accept [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) arguments.
#### DEP0034: `fs.exists(path, callback)`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0034-fsexistspath-callback)
History Version | Changes
---|---
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v1.0.0 | Documentation-only deprecation.
Type: Documentation-only
The [`fs.exists(path, callback)`](https://nodejs.org/docs/latest/api/fs.html#fsexistspath-callback) API is deprecated. Please use [`fs.stat()`](https://nodejs.org/docs/latest/api/fs.html#fsstatpath-options-callback) or [`fs.access()`](https://nodejs.org/docs/latest/api/fs.html#fsaccesspath-mode-callback) instead.
#### DEP0035: `fs.lchmod(path, mode, callback)`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0035-fslchmodpath-mode-callback)
History Version | Changes
---|---
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.4.7 | Documentation-only deprecation.
Type: Documentation-only
The [`fs.lchmod(path, mode, callback)`](https://nodejs.org/docs/latest/api/fs.html#fslchmodpath-mode-callback) API is deprecated.
#### DEP0036: `fs.lchmodSync(path, mode)`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0036-fslchmodsyncpath-mode)
History Version | Changes
---|---
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.4.7 | Documentation-only deprecation.
Type: Documentation-only
The [`fs.lchmodSync(path, mode)`](https://nodejs.org/docs/latest/api/fs.html#fslchmodsyncpath-mode) API is deprecated.
#### DEP0037: `fs.lchown(path, uid, gid, callback)`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0037-fslchownpath-uid-gid-callback)
History Version | Changes
---|---
v10.6.0 | Deprecation revoked.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.4.7 | Documentation-only deprecation.
Type: Deprecation revoked
The [`fs.lchown(path, uid, gid, callback)`](https://nodejs.org/docs/latest/api/fs.html#fslchownpath-uid-gid-callback) API was deprecated. The deprecation was revoked because the requisite supporting APIs were added in libuv.
#### DEP0038: `fs.lchownSync(path, uid, gid)`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0038-fslchownsyncpath-uid-gid)
History Version | Changes
---|---
v10.6.0 | Deprecation revoked.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.4.7 | Documentation-only deprecation.
Type: Deprecation revoked
The [`fs.lchownSync(path, uid, gid)`](https://nodejs.org/docs/latest/api/fs.html#fslchownsyncpath-uid-gid) API was deprecated. The deprecation was revoked because the requisite supporting APIs were added in libuv.
#### DEP0039: `require.extensions`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0039-requireextensions)
History Version | Changes
---|---
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.10.6 | Documentation-only deprecation.
Type: Documentation-only
The [`require.extensions`](https://nodejs.org/docs/latest/api/modules.html#requireextensions) property is deprecated.
#### DEP0040: `node:punycode` module[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0040-nodepunycode-module)
History Version | Changes
---|---
v23.7.0, v22.14.0 | Application deprecation.
v21.0.0 | Runtime deprecation.
v16.6.0 | Added support for `--pending-deprecation`.
v7.0.0 | Documentation-only deprecation.
Type: Application (non-`node_modules` code only)
The [`punycode`](https://nodejs.org/docs/latest/api/punycode.html) module is deprecated. Please use a userland alternative instead.
#### DEP0041: `NODE_REPL_HISTORY_FILE` environment variable[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0041-node-repl-history-file-environment-variable)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v3.0.0 | Documentation-only deprecation.
Type: End-of-Life
The `NODE_REPL_HISTORY_FILE` environment variable was removed. Please use `NODE_REPL_HISTORY` instead.
#### DEP0042: `tls.CryptoStream`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0042-tlscryptostream)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v0.11.3 | Documentation-only deprecation.
Type: End-of-Life
The `tls.CryptoStream` class was removed. Please use [`tls.TLSSocket`](https://nodejs.org/docs/latest/api/tls.html#class-tlstlssocket) instead.
#### DEP0043: `tls.SecurePair`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0043-tlssecurepair)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v8.0.0 | Runtime deprecation.
v6.12.0 | A deprecation code has been assigned.
