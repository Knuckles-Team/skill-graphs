v6.0.0 | Documentation-only deprecation.
v0.11.15 | Deprecation revoked.
v0.11.3 | Runtime deprecation.
Type: End-of-Life
The `tls.SecurePair` class is deprecated. Please use [`tls.TLSSocket`](https://nodejs.org/docs/latest/api/tls.html#class-tlstlssocket) instead.
#### DEP0044: `util.isArray()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0044-utilisarray)
History Version | Changes
---|---
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: Runtime
The [`util.isArray()`](https://nodejs.org/docs/latest/api/util.html#utilisarrayobject) API is deprecated. Please use `Array.isArray()` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0045: `util.isBoolean()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0045-utilisboolean)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isBoolean()` API has been removed. Please use `typeof arg === 'boolean'` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0046: `util.isBuffer()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0046-utilisbuffer)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isBuffer()` API has been removed. Please use [`Buffer.isBuffer()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferisbufferobj) instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0047: `util.isDate()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0047-utilisdate)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isDate()` API has been removed. Please use `arg instanceof Date` instead.
Also for stronger approaches, consider using: `Date.prototype.toString.call(arg) === '[object Date]' && !isNaN(arg)`. This can also be used in a `try/catch` block to handle invalid date objects.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0048: `util.isError()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0048-utiliserror)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isError()` API has been removed. Please use `Error.isError(arg)`.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0049: `util.isFunction()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0049-utilisfunction)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isFunction()` API has been removed. Please use `typeof arg === 'function'` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0050: `util.isNull()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0050-utilisnull)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isNull()` API has been removed. Please use `arg === null` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0051: `util.isNullOrUndefined()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0051-utilisnullorundefined)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isNullOrUndefined()` API has been removed. Please use `arg === null || arg === undefined` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0052: `util.isNumber()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0052-utilisnumber)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isNumber()` API has been removed. Please use `typeof arg === 'number'` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0053: `util.isObject()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0053-utilisobject)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isObject()` API has been removed. Please use `arg && typeof arg === 'object'` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0054: `util.isPrimitive()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0054-utilisprimitive)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isPrimitive()` API has been removed. Please use `Object(arg) !== arg` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0055: `util.isRegExp()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0055-utilisregexp)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isRegExp()` API has been removed. Please use `arg instanceof RegExp` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0056: `util.isString()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0056-utilisstring)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isString()` API has been removed. Please use `typeof arg === 'string'` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0057: `util.isSymbol()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0057-utilissymbol)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isSymbol()` API has been removed. Please use `typeof arg === 'symbol'` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0058: `util.isUndefined()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0058-utilisundefined)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0, v4.8.6 | A deprecation code has been assigned.
v4.0.0, v3.3.1 | Documentation-only deprecation.
Type: End-of-Life
The `util.isUndefined()` API has been removed. Please use `arg === undefined` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-is
copy
```

#### DEP0059: `util.log()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0059-utillog)
History Version | Changes
---|---
v23.0.0 | End-of-Life deprecation.
v22.0.0 | Runtime deprecation.
v6.12.0 | A deprecation code has been assigned.
v6.0.0 | Documentation-only deprecation.
Type: End-of-Life
The `util.log()` API has been removed because it's an unmaintained legacy API that was exposed to user land by accident. Instead, consider the following alternatives based on your specific needs:
  * **Third-Party Logging Libraries**
  * **Use`console.log(new Date().toLocaleString(), message)`**


By adopting one of these alternatives, you can transition away from `util.log()` and choose a logging strategy that aligns with the specific requirements and complexity of your application.
An automated migration is available (
```
npx codemod@latest @nodejs/util-log-to-console-log
copy
```

#### DEP0060: `util._extend()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0060-util-extend)
History Version | Changes
---|---
v22.0.0 | Runtime deprecation.
v6.12.0 | A deprecation code has been assigned.
v6.0.0 | Documentation-only deprecation.
Type: Runtime
The [`util._extend()`](https://nodejs.org/docs/latest/api/util.html#util_extendtarget-source) API is deprecated because it's an unmaintained legacy API that was exposed to user land by accident. Please use `target = Object.assign(target, source)` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/util-extend-to-object-assign
copy
```

#### DEP0061: `fs.SyncWriteStream`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0061-fssyncwritestream)
History Version | Changes
---|---
v11.0.0 | End-of-Life.
v8.0.0 | Runtime deprecation.
v7.0.0 | Documentation-only deprecation.
Type: End-of-Life
The `fs.SyncWriteStream` class was never intended to be a publicly accessible API and has been removed. No alternative API is available. Please use a userland alternative.
#### DEP0062: `node --debug`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0062-node-debug)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v8.0.0 | Runtime deprecation.
Type: End-of-Life
`--debug` activates the legacy V8 debugger interface, which was removed as of V8 5.8. It is replaced by Inspector which is activated with `--inspect` instead.
#### DEP0063: `ServerResponse.prototype.writeHeader()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0063-serverresponseprototypewriteheader)
History Version | Changes
---|---
v25.0.0 | Runtime deprecation.
v8.0.0 | Documentation-only deprecation.
Type: Runtime
The `node:http` module `ServerResponse.prototype.writeHeader()` API is deprecated. Please use `ServerResponse.prototype.writeHead()` instead.
The `ServerResponse.prototype.writeHeader()` method was never documented as an officially supported API.
#### DEP0064: `tls.createSecurePair()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0064-tlscreatesecurepair)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v8.0.0 | Runtime deprecation.
v6.12.0 | A deprecation code has been assigned.
v6.0.0 | Documentation-only deprecation.
v0.11.15 | Deprecation revoked.
v0.11.3 | Runtime deprecation.
Type: End-of-Life
The `tls.createSecurePair()` API was deprecated in documentation in Node.js 0.11.3. Users should use `tls.Socket` instead.
#### DEP0065: `repl.REPL_MODE_MAGIC` and `NODE_REPL_MODE=magic`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0065-replrepl-mode-magic-and-node-repl-modemagic)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
v8.0.0 | Documentation-only deprecation.
Type: End-of-Life
The `node:repl` module's `REPL_MODE_MAGIC` constant, used for `replMode` option, has been removed. Its behavior has been functionally identical to that of `REPL_MODE_SLOPPY` since Node.js 6.0.0, when V8 5.0 was imported. Please use `REPL_MODE_SLOPPY` instead.
The `NODE_REPL_MODE` environment variable is used to set the underlying `replMode` of an interactive `node` session. Its value, `magic`, is also removed. Please use `sloppy` instead.
#### DEP0066: `OutgoingMessage.prototype._headers, OutgoingMessage.prototype._headerNames`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0066-outgoingmessageprototype-headers-outgoingmessageprototype-headernames)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v12.0.0 | Runtime deprecation.
v8.0.0 | Documentation-only deprecation.
Type: End-of-Life
The `node:http` module `OutgoingMessage.prototype._headers` and `OutgoingMessage.prototype._headerNames` properties are deprecated. Use one of the public methods (e.g. `OutgoingMessage.prototype.getHeader()`, `OutgoingMessage.prototype.getHeaders()`, `OutgoingMessage.prototype.getHeaderNames()`, `OutgoingMessage.prototype.getRawHeaderNames()`, `OutgoingMessage.prototype.hasHeader()`, `OutgoingMessage.prototype.removeHeader()`, `OutgoingMessage.prototype.setHeader()`) for working with outgoing headers.
The `OutgoingMessage.prototype._headers` and `OutgoingMessage.prototype._headerNames` properties were never documented as officially supported properties.
An automated migration is available (
```
npx codemod@latest @nodejs/http-outgoingmessage-headers
copy
```

#### DEP0067: `OutgoingMessage.prototype._renderHeaders`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0067-outgoingmessageprototype-renderheaders)
History Version | Changes
---|---
v8.0.0 | Documentation-only deprecation.
Type: Documentation-only
The `node:http` module `OutgoingMessage.prototype._renderHeaders()` API is deprecated.
The `OutgoingMessage.prototype._renderHeaders` property was never documented as an officially supported API.
#### DEP0068: `node debug`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0068-node-debug)
History Version | Changes
---|---
v15.0.0 | The legacy `node debug` command was removed.
v8.0.0 | Runtime deprecation.
Type: End-of-Life
`node debug` corresponds to the legacy CLI debugger which has been replaced with a V8-inspector based CLI debugger available through `node inspect`.
#### DEP0069: `vm.runInDebugContext(string)`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0069-vmrunindebugcontextstring)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
v9.0.0 | Runtime deprecation.
v8.0.0 | Documentation-only deprecation.
Type: End-of-Life
DebugContext has been removed in V8 and is not available in Node.js 10+.
DebugContext was an experimental API.
#### DEP0070: `async_hooks.currentId()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0070-async-hookscurrentid)
History Version | Changes
---|---
v9.0.0 | End-of-Life.
v8.2.0 | Runtime deprecation.
Type: End-of-Life
`async_hooks.currentId()` was renamed to `async_hooks.executionAsyncId()` for clarity.
This change was made while `async_hooks` was an experimental API.
#### DEP0071: `async_hooks.triggerId()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0071-async-hookstriggerid)
History Version | Changes
---|---
v9.0.0 | End-of-Life.
v8.2.0 | Runtime deprecation.
Type: End-of-Life
`async_hooks.triggerId()` was renamed to `async_hooks.triggerAsyncId()` for clarity.
This change was made while `async_hooks` was an experimental API.
#### DEP0072: `async_hooks.AsyncResource.triggerId()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0072-async-hooksasyncresourcetriggerid)
History Version | Changes
---|---
v9.0.0 | End-of-Life.
v8.2.0 | Runtime deprecation.
Type: End-of-Life
`async_hooks.AsyncResource.triggerId()` was renamed to `async_hooks.AsyncResource.triggerAsyncId()` for clarity.
This change was made while `async_hooks` was an experimental API.
#### DEP0073: Several internal properties of `net.Server`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0073-several-internal-properties-of-netserver)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
v9.0.0 | Runtime deprecation.
Type: End-of-Life
Accessing several internal, undocumented properties of `net.Server` instances with inappropriate names is deprecated.
As the original API was undocumented and not generally useful for non-internal code, no replacement API is provided.
#### DEP0074: `REPLServer.bufferedCommand`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0074-replserverbufferedcommand)
History Version | Changes
---|---
v15.0.0 | End-of-Life.
v9.0.0 | Runtime deprecation.
Type: End-of-Life
The `REPLServer.bufferedCommand` property was deprecated in favor of [`REPLServer.clearBufferedCommand()`](https://nodejs.org/docs/latest/api/repl.html#replserverclearbufferedcommand).
#### DEP0075: `REPLServer.parseREPLKeyword()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0075-replserverparsereplkeyword)
History Version | Changes
---|---
v15.0.0 | End-of-Life.
v9.0.0 | Runtime deprecation.
Type: End-of-Life
`REPLServer.parseREPLKeyword()` was removed from userland visibility.
#### DEP0076: `tls.parseCertString()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0076-tlsparsecertstring)
History Version | Changes
---|---
v18.0.0 | End-of-Life.
v9.0.0 | Runtime deprecation.
v8.6.0 | Documentation-only deprecation.
Type: End-of-Life
`tls.parseCertString()` was a trivial parsing helper that was made public by mistake. While it was supposed to parse certificate subject and issuer strings, it never handled multi-value Relative Distinguished Names correctly.
Earlier versions of this document suggested using `querystring.parse()` as an alternative to `tls.parseCertString()`. However, `querystring.parse()` also does not handle all certificate subjects correctly and should not be used.
#### DEP0077: `Module._debug()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0077-module-debug)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v9.0.0 | Runtime deprecation.
Type: End-of-Life
`Module._debug()` has been removed.
The `Module._debug()` function was never documented as an officially supported API.
#### DEP0078: `REPLServer.turnOffEditorMode()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0078-replserverturnoffeditormode)
History Version | Changes
---|---
v15.0.0 | End-of-Life.
v9.0.0 | Runtime deprecation.
Type: End-of-Life
`REPLServer.turnOffEditorMode()` was removed from userland visibility.
#### DEP0079: Custom inspection function on objects via `.inspect()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0079-custom-inspection-function-on-objects-via-inspect)
History Version | Changes
---|---
v11.0.0 | End-of-Life.
v10.0.0 | Runtime deprecation.
v8.7.0 | Documentation-only deprecation.
Type: End-of-Life
Using a property named `inspect` on an object to specify a custom inspection function for [`util.inspect()`](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options) is deprecated. Use [`util.inspect.custom`](https://nodejs.org/docs/latest/api/util.html#utilinspectcustom) instead. For backward compatibility with Node.js prior to version 6.4.0, both can be specified.
#### DEP0080: `path._makeLong()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0080-path-makelong)
History Version | Changes
---|---
v9.0.0 | Documentation-only deprecation.
Type: Documentation-only
The internal `path._makeLong()` was not intended for public use. However, userland modules have found it useful. The internal API is deprecated and replaced with an identical, public `path.toNamespacedPath()` method.
#### DEP0081: `fs.truncate()` using a file descriptor[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0081-fstruncate-using-a-file-descriptor)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v9.0.0 | Runtime deprecation.
Type: End-of-Life
`fs.truncate()` `fs.truncateSync()` usage with a file descriptor is deprecated. Please use `fs.ftruncate()` or `fs.ftruncateSync()` to work with file descriptors.
An automated migration is available (
```
npx codemod@latest @nodejs/fs-truncate-fd-deprecation
copy
```

#### DEP0082: `REPLServer.prototype.memory()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0082-replserverprototypememory)
History Version | Changes
---|---
v15.0.0 | End-of-Life.
v9.0.0 | Runtime deprecation.
Type: End-of-Life
`REPLServer.prototype.memory()` is only necessary for the internal mechanics of the `REPLServer` itself. Do not use this function.
#### DEP0083: Disabling ECDH by setting `ecdhCurve` to `false`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0083-disabling-ecdh-by-setting-ecdhcurve-to-false)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
v9.2.0 | Runtime deprecation.
Type: End-of-Life
The `ecdhCurve` option to `tls.createSecureContext()` and `tls.TLSSocket` could be set to `false` to disable ECDH entirely on the server only. This mode was deprecated in preparation for migrating to OpenSSL 1.1.0 and consistency with the client and is now unsupported. Use the `ciphers` parameter instead.
#### DEP0084: requiring bundled internal dependencies[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0084-requiring-bundled-internal-dependencies)
History Version | Changes
---|---
v12.0.0 | This functionality has been removed.
v10.0.0 | Runtime deprecation.
Type: End-of-Life
Since Node.js versions 4.4.0 and 5.2.0, several modules only intended for internal usage were mistakenly exposed to user code through `require()`. These modules were:
  * `v8/tools/codemap`
  * `v8/tools/consarray`
  * `v8/tools/csvparser`
  * `v8/tools/logreader`
  * `v8/tools/profile_view`
  * `v8/tools/profile`
  * `v8/tools/SourceMap`
  * `v8/tools/splaytree`
  * `v8/tools/tickprocessor-driver`
  * `v8/tools/tickprocessor`
  * `node-inspect/lib/_inspect` (from 7.6.0)
  * `node-inspect/lib/internal/inspect_client` (from 7.6.0)
  * `node-inspect/lib/internal/inspect_repl` (from 7.6.0)


The `v8/*` modules do not have any exports, and if not imported in a specific order would in fact throw errors. As such there are virtually no legitimate use cases for importing them through `require()`.
On the other hand, `node-inspect` can be installed locally through a package manager, as it is published on the npm registry under the same name. No source code modification is necessary if that is done.
#### DEP0085: AsyncHooks sensitive API[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0085-asynchooks-sensitive-api)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
v9.4.0, v8.10.0 | Runtime deprecation.
Type: End-of-Life
The AsyncHooks sensitive API was never documented and had various minor issues. Use the `AsyncResource` API instead. See
#### DEP0086: Remove `runInAsyncIdScope`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0086-remove-runinasyncidscope)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
v9.4.0, v8.10.0 | Runtime deprecation.
Type: End-of-Life
`runInAsyncIdScope` doesn't emit the `'before'` or `'after'` event and can thus cause a lot of issues. See
#### DEP0089: `require('node:assert')`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0089-requirenodeassert)
History Version | Changes
---|---
v12.8.0 | Deprecation revoked.
v9.9.0, v8.13.0 | Documentation-only deprecation.
Type: Deprecation revoked
Importing assert directly was not recommended as the exposed functions use loose equality checks. The deprecation was revoked because use of the `node:assert` module is not discouraged, and the deprecation caused developer confusion.
#### DEP0090: Invalid GCM authentication tag lengths[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0090-invalid-gcm-authentication-tag-lengths)
History Version | Changes
---|---
v11.0.0 | End-of-Life.
v10.0.0 | Runtime deprecation.
Type: End-of-Life
Node.js used to support all GCM authentication tag lengths which are accepted by OpenSSL when calling [`decipher.setAuthTag()`](https://nodejs.org/docs/latest/api/crypto.html#deciphersetauthtagbuffer-encoding). Beginning with Node.js v11.0.0, only authentication tag lengths of 128, 120, 112, 104, 96, 64, and 32 bits are allowed. Authentication tags of other lengths are invalid per
#### DEP0091: `crypto.DEFAULT_ENCODING`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0091-cryptodefault-encoding)
History Version | Changes
---|---
v20.0.0 | End-of-Life.
v10.0.0 | Runtime deprecation.
Type: End-of-Life
The `crypto.DEFAULT_ENCODING` property only existed for compatibility with Node.js releases prior to versions 0.9.3 and has been removed.
#### DEP0092: Top-level `this` bound to `module.exports`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0092-top-level-this-bound-to-moduleexports)
History Version | Changes
---|---
v10.0.0 | Documentation-only deprecation.
Type: Documentation-only
Assigning properties to the top-level `this` as an alternative to `module.exports` is deprecated. Developers should use `exports` or `module.exports` instead.
#### DEP0093: `crypto.fips` is deprecated and replaced[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0093-cryptofips-is-deprecated-and-replaced)
