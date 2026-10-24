History Version | Changes
---|---
v23.0.0 | Runtime deprecation.
v10.0.0 | Documentation-only deprecation.
Type: Runtime
The [`crypto.fips`](https://nodejs.org/docs/latest/api/crypto.html#cryptofips) property is deprecated. Please use `crypto.setFips()` and `crypto.getFips()` instead.
An automated migration is available (
```
npx codemod@latest @nodejs/crypto-fips-to-getFips
copy
```

#### DEP0094: Using `assert.fail()` with more than one argument[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0094-using-assertfail-with-more-than-one-argument)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v10.0.0 | Runtime deprecation.
Type: End-of-Life
Using `assert.fail()` with more than one argument is deprecated. Use `assert.fail()` with only one argument or use a different `node:assert` module method.
#### DEP0095: `timers.enroll()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0095-timersenroll)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v10.0.0 | Runtime deprecation.
Type: End-of-Life
`timers.enroll()` has been removed. Please use the publicly documented [`setTimeout()`](https://nodejs.org/docs/latest/api/timers.html#settimeoutcallback-delay-args) or [`setInterval()`](https://nodejs.org/docs/latest/api/timers.html#setintervalcallback-delay-args) instead.
#### DEP0096: `timers.unenroll()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0096-timersunenroll)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v10.0.0 | Runtime deprecation.
Type: End-of-Life
`timers.unenroll()` has been removed. Please use the publicly documented [`clearTimeout()`](https://nodejs.org/docs/latest/api/timers.html#cleartimeouttimeout) or [`clearInterval()`](https://nodejs.org/docs/latest/api/timers.html#clearintervaltimeout) instead.
#### DEP0097: `MakeCallback` with `domain` property[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0097-makecallback-with-domain-property)
History Version | Changes
---|---
v10.0.0 | Runtime deprecation.
Type: Runtime
Users of `MakeCallback` that add the `domain` property to carry context, should start using the `async_context` variant of `MakeCallback` or `CallbackScope`, or the high-level `AsyncResource` class.
#### DEP0098: AsyncHooks embedder `AsyncResource.emitBefore` and `AsyncResource.emitAfter` APIs[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0098-asynchooks-embedder-asyncresourceemitbefore-and-asyncresourceemitafter-apis)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v10.0.0, v9.6.0, v8.12.0 | Runtime deprecation.
Type: End-of-Life
The embedded API provided by AsyncHooks exposes `.emitBefore()` and `.emitAfter()` methods which are very easy to use incorrectly which can lead to unrecoverable errors.
Use [`asyncResource.runInAsyncScope()`](https://nodejs.org/docs/latest/api/async_context.html#asyncresourceruninasyncscopefn-thisarg-args) API instead which provides a much safer, and more convenient, alternative. See
#### DEP0099: Async context-unaware `node::MakeCallback` C++ APIs[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0099-async-context-unaware-nodemakecallback-c-apis)
History Version | Changes
---|---
v10.0.0 | Compile-time deprecation.
Type: Compile-time
Certain versions of `node::MakeCallback` APIs available to native addons are deprecated. Please use the versions of the API that accept an `async_context` parameter.
#### DEP0100: `process.assert()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0100-processassert)
History Version | Changes
---|---
v23.0.0 | End-of-Life.
v10.0.0 | Runtime deprecation.
v0.3.7 | Documentation-only deprecation.
Type: End-of-Life
`process.assert()` is deprecated. Please use the [`assert`](https://nodejs.org/docs/latest/api/assert.html) module instead.
This was never a documented feature.
An automated migration is available (
```
npx codemod@latest @nodejs/process-assert-to-node-assert
copy
```

#### DEP0101: `--with-lttng`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0101-with-lttng)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
Type: End-of-Life
The `--with-lttng` compile-time option has been removed.
#### DEP0102: Using `noAssert` in `Buffer#(read|write)` operations[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0102-using-noassert-in-bufferreadwrite-operations)
History Version | Changes
---|---
v10.0.0 | End-of-Life.
Type: End-of-Life
Using the `noAssert` argument has no functionality anymore. All input is verified regardless of the value of `noAssert`. Skipping the verification could lead to hard-to-find errors and crashes.
#### DEP0103: `process.binding('util').is[...]` typechecks[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0103-processbindingutilis-typechecks)
History Version | Changes
---|---
v10.9.0 | Superseded by [DEP0111](https://nodejs.org/docs/latest/api/deprecations.html#DEP0111).
v10.0.0 | Documentation-only deprecation.
Type: Documentation-only (supports [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation))
Using `process.binding()` in general should be avoided. The type checking methods in particular can be replaced by using [`util.types`](https://nodejs.org/docs/latest/api/util.html#utiltypes).
This deprecation has been superseded by the deprecation of the `process.binding()` API ([DEP0111](https://nodejs.org/docs/latest/api/deprecations.html#DEP0111)).
#### DEP0104: `process.env` string coercion[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0104-processenv-string-coercion)
History Version | Changes
---|---
v10.0.0 | Documentation-only deprecation with `--pending-deprecation` support.
Type: Documentation-only (supports [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation))
When assigning a non-string property to [`process.env`](https://nodejs.org/docs/latest/api/process.html#processenv), the assigned value is implicitly converted to a string. This behavior is deprecated if the assigned value is not a string, boolean, or number. In the future, such assignment might result in a thrown error. Please convert the property to a string before assigning it to `process.env`.
#### DEP0105: `decipher.finaltol`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0105-decipherfinaltol)
History Version | Changes
---|---
v11.0.0 | End-of-Life.
v10.0.0 | Runtime deprecation.
Type: End-of-Life
`decipher.finaltol()` has never been documented and was an alias for [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding). This API has been removed, and it is recommended to use [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding) instead.
#### DEP0106: `crypto.createCipher` and `crypto.createDecipher`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0106-cryptocreatecipher-and-cryptocreatedecipher)
History Version | Changes
---|---
v22.0.0 | End-of-Life.
v11.0.0 | Runtime deprecation.
v10.0.0 | Documentation-only deprecation.
Type: End-of-Life
`crypto.createCipher()` and `crypto.createDecipher()` have been removed as they use a weak key derivation function (MD5 with no salt) and static initialization vectors. It is recommended to derive a key using [`crypto.pbkdf2()`](https://nodejs.org/docs/latest/api/crypto.html#cryptopbkdf2password-salt-iterations-keylen-digest-callback) or [`crypto.scrypt()`](https://nodejs.org/docs/latest/api/crypto.html#cryptoscryptpassword-salt-keylen-options-callback) with random salts and to use [`crypto.createCipheriv()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatecipherivalgorithm-key-iv-options) and [`crypto.createDecipheriv()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatedecipherivalgorithm-key-iv-options) to obtain the [`Cipheriv`](https://nodejs.org/docs/latest/api/crypto.html#class-cipheriv) and [`Decipheriv`](https://nodejs.org/docs/latest/api/crypto.html#class-decipheriv) objects respectively.
#### DEP0107: `tls.convertNPNProtocols()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0107-tlsconvertnpnprotocols)
History Version | Changes
---|---
v11.0.0 | End-of-Life.
v10.0.0 | Runtime deprecation.
Type: End-of-Life
This was an undocumented helper function not intended for use outside Node.js core and obsoleted by the removal of NPN (Next Protocol Negotiation) support.
#### DEP0108: `zlib.bytesRead`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0108-zlibbytesread)
History Version | Changes
---|---
v23.0.0 | End-of-Life.
v11.0.0 | Runtime deprecation.
v10.0.0 | Documentation-only deprecation.
Type: End-of-Life
Deprecated alias for [`zlib.bytesWritten`](https://nodejs.org/docs/latest/api/zlib.html#zlibbyteswritten). This original name was chosen because it also made sense to interpret the value as the number of bytes read by the engine, but is inconsistent with other streams in Node.js that expose values under these names.
An automated migration is available (
```
npx codemod@latest @nodejs/zlib-bytesread-to-byteswritten
copy
```

#### DEP0109: `http`, `https`, and `tls` support for invalid URLs[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0109-http-https-and-tls-support-for-invalid-urls)
History Version | Changes
---|---
v16.0.0 | End-of-Life.
v11.0.0 | Runtime deprecation.
Type: End-of-Life
Some previously supported (but strictly invalid) URLs were accepted through the [`http.request()`](https://nodejs.org/docs/latest/api/http.html#httprequestoptions-callback), [`http.get()`](https://nodejs.org/docs/latest/api/http.html#httpgetoptions-callback), [`https.request()`](https://nodejs.org/docs/latest/api/https.html#httpsrequestoptions-callback), [`https.get()`](https://nodejs.org/docs/latest/api/https.html#httpsgetoptions-callback), and [`tls.checkServerIdentity()`](https://nodejs.org/docs/latest/api/tls.html#tlscheckserveridentityhostname-cert) APIs because those were accepted by the legacy `url.parse()` API. The mentioned APIs now use the WHATWG URL parser that requires strictly valid URLs. Passing an invalid URL is deprecated and support will be removed in the future.
#### DEP0110: `vm.Script` cached data[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0110-vmscript-cached-data)
History Version | Changes
---|---
v10.6.0 | Documentation-only deprecation.
Type: Documentation-only
The `produceCachedData` option is deprecated. Use [`script.createCachedData()`](https://nodejs.org/docs/latest/api/vm.html#scriptcreatecacheddata) instead.
#### DEP0111: `process.binding()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0111-processbinding)
History Version | Changes
---|---
v11.12.0 | Added support for `--pending-deprecation`.
v10.9.0 | Documentation-only deprecation.
Type: Documentation-only (supports [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation))
`process.binding()` is for use by Node.js internal code only.
While `process.binding()` has not reached End-of-Life status in general, it is unavailable when the [permission model](https://nodejs.org/docs/latest/api/permissions.html#permission-model) is enabled.
#### DEP0112: `dgram` private APIs[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0112-dgram-private-apis)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v11.0.0 | Runtime deprecation.
Type: End-of-Life
The `node:dgram` module previously contained several APIs that were never meant to accessed outside of Node.js core: `Socket.prototype._handle`, `Socket.prototype._receiving`, `Socket.prototype._bindState`, `Socket.prototype._queue`, `Socket.prototype._reuseAddr`, `Socket.prototype._healthCheck()`, `Socket.prototype._stopReceiving()`, and `dgram._createSocketHandle()`. These have been removed.
#### DEP0113: `Cipher.setAuthTag()`, `Decipher.getAuthTag()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0113-ciphersetauthtag-deciphergetauthtag)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v11.0.0 | Runtime deprecation.
Type: End-of-Life
`Cipher.setAuthTag()` and `Decipher.getAuthTag()` are no longer available. They were never documented and would throw when called.
#### DEP0114: `crypto._toBuf()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0114-crypto-tobuf)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v11.0.0 | Runtime deprecation.
Type: End-of-Life
The `crypto._toBuf()` function was not designed to be used by modules outside of Node.js core and was removed.
#### DEP0115: `crypto.prng()`, `crypto.pseudoRandomBytes()`, `crypto.rng()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0115-cryptoprng-cryptopseudorandombytes-cryptorng)
History Version | Changes
---|---
v11.0.0 | Documentation-only deprecation with `--pending-deprecation` support.
Type: Documentation-only (supports [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation))
In recent versions of Node.js, there is no difference between [`crypto.randomBytes()`](https://nodejs.org/docs/latest/api/crypto.html#cryptorandombytessize-callback) and `crypto.pseudoRandomBytes()`. The latter is deprecated along with the undocumented aliases `crypto.prng()` and `crypto.rng()` in favor of [`crypto.randomBytes()`](https://nodejs.org/docs/latest/api/crypto.html#cryptorandombytessize-callback) and might be removed in a future release.
#### DEP0116: Legacy URL API[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0116-legacy-url-api)
History Version | Changes
---|---
v19.0.0, v18.13.0 | `url.parse()` is deprecated again in DEP0169.
v15.13.0, v14.17.0 | Deprecation revoked. Status changed to "Legacy".
v11.0.0 | Documentation-only deprecation.
Type: Deprecation revoked
The [legacy URL API](https://nodejs.org/docs/latest/api/url.html#legacy-url-api) is deprecated. This includes [`url.format()`](https://nodejs.org/docs/latest/api/url.html#urlformaturlobject), [`url.parse()`](https://nodejs.org/docs/latest/api/url.html#urlparseurlstring-parsequerystring-slashesdenotehost), [`url.resolve()`](https://nodejs.org/docs/latest/api/url.html#urlresolvefrom-to), and the [legacy `urlObject`](https://nodejs.org/docs/latest/api/url.html#legacy-urlobject). Please use the [WHATWG URL API](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) instead.
An automated migration is available (
```
npx codemod@latest @nodejs/node-url-to-whatwg-url
copy
```

#### DEP0117: Native crypto handles[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0117-native-crypto-handles)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v11.0.0 | Runtime deprecation.
Type: End-of-Life
Previous versions of Node.js exposed handles to internal native objects through the `_handle` property of the `Cipher`, `Decipher`, `DiffieHellman`, `DiffieHellmanGroup`, `ECDH`, `Hash`, `Hmac`, `Sign`, and `Verify` classes. The `_handle` property has been removed because improper use of the native object can lead to crashing the application.
#### DEP0118: `dns.lookup()` support for a falsy host name[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0118-dnslookup-support-for-a-falsy-host-name)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v11.0.0 | Runtime deprecation.
Type: End-of-Life
Previous versions of Node.js supported `dns.lookup()` with a falsy host name like `dns.lookup(false)` due to backward compatibility. This has been removed.
#### DEP0119: `process.binding('uv').errname()` private API[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0119-processbindinguverrname-private-api)
History Version | Changes
---|---
v11.0.0 | Documentation-only deprecation with `--pending-deprecation` support.
Type: Documentation-only (supports [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation))
`process.binding('uv').errname()` is deprecated. Please use [`util.getSystemErrorName()`](https://nodejs.org/docs/latest/api/util.html#utilgetsystemerrornameerr) instead.
#### DEP0120: Windows Performance Counter support[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0120-windows-performance-counter-support)
History Version | Changes
---|---
v12.0.0 | End-of-Life.
v11.0.0 | Runtime deprecation.
Type: End-of-Life
Windows Performance Counter support has been removed from Node.js. The undocumented `COUNTER_NET_SERVER_CONNECTION()`, `COUNTER_NET_SERVER_CONNECTION_CLOSE()`, `COUNTER_HTTP_SERVER_REQUEST()`, `COUNTER_HTTP_SERVER_RESPONSE()`, `COUNTER_HTTP_CLIENT_REQUEST()`, and `COUNTER_HTTP_CLIENT_RESPONSE()` functions have been deprecated.
#### DEP0121: `net._setSimultaneousAccepts()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0121-net-setsimultaneousaccepts)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v12.0.0 | Runtime deprecation.
Type: End-of-Life
The undocumented `net._setSimultaneousAccepts()` function was originally intended for debugging and performance tuning when using the `node:child_process` and `node:cluster` modules on Windows. The function is not generally useful and is being removed. See discussion here:
#### DEP0122: `tls` `Server.prototype.setOptions()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0122-tls-serverprototypesetoptions)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v12.0.0 | Runtime deprecation.
Type: End-of-Life
Please use `Server.prototype.setSecureContext()` instead.
#### DEP0123: setting the TLS ServerName to an IP address[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0123-setting-the-tls-servername-to-an-ip-address)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v12.0.0 | Runtime deprecation.
Type: End-of-Life
Setting the TLS ServerName to an IP address is not permitted by
#### DEP0124: using `REPLServer.rli`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0124-using-replserverrli)
History Version | Changes
---|---
v15.0.0 | End-of-Life.
v12.0.0 | Runtime deprecation.
Type: End-of-Life
This property is a reference to the instance itself.
#### DEP0125: `require('node:_stream_wrap')`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0125-requirenode-stream-wrap)
History Version | Changes
---|---
v12.0.0 | Runtime deprecation.
Type: Runtime
The `node:_stream_wrap` module is deprecated.
#### DEP0126: `timers.active()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0126-timersactive)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v11.14.0 | Runtime deprecation.
Type: End-of-Life
The previously undocumented `timers.active()` has been removed. Please use the publicly documented [`timeout.refresh()`](https://nodejs.org/docs/latest/api/timers.html#timeoutrefresh) instead. If re-referencing the timeout is necessary, [`timeout.ref()`](https://nodejs.org/docs/latest/api/timers.html#timeoutref) can be used with no performance impact since Node.js 10.
#### DEP0127: `timers._unrefActive()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0127-timers-unrefactive)
History Version | Changes
---|---
v24.0.0 | End-of-Life.
v11.14.0 | Runtime deprecation.
Type: End-of-Life
The previously undocumented and "private" `timers._unrefActive()` has been removed. Please use the publicly documented [`timeout.refresh()`](https://nodejs.org/docs/latest/api/timers.html#timeoutrefresh) instead. If unreferencing the timeout is necessary, [`timeout.unref()`](https://nodejs.org/docs/latest/api/timers.html#timeoutunref) can be used with no performance impact since Node.js 10.
#### DEP0128: modules with an invalid `main` entry and an `index.js` file[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0128-modules-with-an-invalid-main-entry-and-an-indexjs-file)
History Version | Changes
---|---
v16.0.0 | Runtime deprecation.
v12.0.0 | Documentation-only.
Type: Runtime
Modules that have an invalid `main` entry (e.g., `./does-not-exist.js`) and also have an `index.js` file in the top level directory will resolve the `index.js` file. That is deprecated and is going to throw an error in future Node.js versions.
#### DEP0129: `ChildProcess._channel`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0129-childprocess-channel)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v13.0.0 | Runtime deprecation.
v11.14.0 | Documentation-only.
Type: End-of-Life
The `_channel` property of child process objects returned by `spawn()` and similar functions is not intended for public use. Use `ChildProcess.channel` instead.
#### DEP0130: `Module.createRequireFromPath()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0130-modulecreaterequirefrompath)
History Version | Changes
---|---
v16.0.0 | End-of-life.
v13.0.0 | Runtime deprecation.
v12.2.0 | Documentation-only.
Type: End-of-Life
Use [`module.createRequire()`](https://nodejs.org/docs/latest/api/module.html#modulecreaterequirefilename) instead.
An automated migration is available (
```
npx codemod@latest @nodejs/create-require-from-path
copy
```

#### DEP0131: Legacy HTTP parser[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0131-legacy-http-parser)
History Version | Changes
---|---
v13.0.0 | This feature has been removed.
v12.22.0 | Runtime deprecation.
v12.3.0 | Documentation-only.
Type: End-of-Life
The legacy HTTP parser, used by default in versions of Node.js prior to 12.0.0, is deprecated and has been removed in v13.0.0. Prior to v13.0.0, the `--http-parser=legacy` command-line flag could be used to revert to using the legacy parser.
#### DEP0132: `worker.terminate()` with callback[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0132-workerterminate-with-callback)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v12.5.0 | Runtime deprecation.
Type: End-of-Life
Passing a callback to [`worker.terminate()`](https://nodejs.org/docs/latest/api/worker_threads.html#workerterminate) is deprecated. Use the returned `Promise` instead, or a listener to the worker's `'exit'` event.
#### DEP0133: `http` `connection`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0133-http-connection)
History Version | Changes
---|---
v12.12.0 | Documentation-only deprecation.
Type: Documentation-only
Prefer [`response.socket`](https://nodejs.org/docs/latest/api/http.html#responsesocket) over [`response.connection`](https://nodejs.org/docs/latest/api/http.html#responseconnection) and [`request.socket`](https://nodejs.org/docs/latest/api/http.html#requestsocket) over [`request.connection`](https://nodejs.org/docs/latest/api/http.html#requestconnection).
#### DEP0134: `process._tickCallback`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0134-process-tickcallback)
History Version | Changes
---|---
v12.12.0 | Documentation-only deprecation with `--pending-deprecation` support.
Type: Documentation-only (supports [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation))
The `process._tickCallback` property was never documented as an officially supported API.
#### DEP0135: `WriteStream.open()` and `ReadStream.open()` are internal[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0135-writestreamopen-and-readstreamopen-are-internal)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v13.0.0 | Runtime deprecation.
Type: End-of-Life
[`WriteStream.open()`](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream) and [`ReadStream.open()`](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream) are undocumented internal APIs that do not make sense to use in userland. File streams should always be opened through their corresponding factory methods [`fs.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options) and [`fs.createReadStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatereadstreampath-options)) or by passing a file descriptor in options.
#### DEP0136: `http` `finished`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0136-http-finished)
History Version | Changes
---|---
v13.4.0, v12.16.0 | Documentation-only deprecation.
Type: Documentation-only
[`response.finished`](https://nodejs.org/docs/latest/api/http.html#responsefinished) indicates whether [`response.end()`](https://nodejs.org/docs/latest/api/http.html#responseenddata-encoding-callback) has been called, not whether `'finish'` has been emitted and the underlying data is flushed.
Use [`response.writableFinished`](https://nodejs.org/docs/latest/api/http.html#responsewritablefinished) or [`response.writableEnded`](https://nodejs.org/docs/latest/api/http.html#responsewritableended) accordingly instead to avoid the ambiguity.
To maintain existing behavior `response.finished` should be replaced with `response.writableEnded`.
#### DEP0137: Closing fs.FileHandle on garbage collection[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0137-closing-fsfilehandle-on-garbage-collection)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v14.0.0 | Runtime deprecation.
Type: End-of-Life
Allowing a [`fs.FileHandle`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) object to be closed on garbage collection used to be allowed, but now throws an error.
Please ensure that all `fs.FileHandle` objects are explicitly closed using `FileHandle.prototype.close()` when the `fs.FileHandle` is no longer needed:
