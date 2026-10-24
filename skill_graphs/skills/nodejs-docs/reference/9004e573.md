An automated migration is available (
```
npx codemod@latest @nodejs/dirent-path-to-parent-path
copy
```

#### DEP0179: `Hash` constructor[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0179-hash-constructor)
History Version | Changes
---|---
v22.0.0 | Runtime deprecation.
v21.5.0, v20.12.0 | Documentation-only deprecation.
Type: Runtime
Calling `Hash` class directly with `Hash()` or `new Hash()` is deprecated due to being internals, not intended for public use. Please use the [`crypto.createHash()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatehashalgorithm-options) method to create Hash instances.
#### DEP0180: `fs.Stats` constructor[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0180-fsstats-constructor)
History Version | Changes
---|---
v22.0.0 | Runtime deprecation.
v20.13.0 | Documentation-only deprecation.
Type: Runtime
Calling `fs.Stats` class directly with `Stats()` or `new Stats()` is deprecated due to being internals, not intended for public use.
#### DEP0181: `Hmac` constructor[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0181-hmac-constructor)
History Version | Changes
---|---
v22.0.0 | Runtime deprecation.
v20.13.0 | Documentation-only deprecation.
Type: Runtime
Calling `Hmac` class directly with `Hmac()` or `new Hmac()` is deprecated due to being internals, not intended for public use. Please use the [`crypto.createHmac()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatehmacalgorithm-key-options) method to create Hmac instances.
#### DEP0182: Short GCM authentication tags without explicit `authTagLength`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0182-short-gcm-authentication-tags-without-explicit-authtaglength)
History Version | Changes
---|---
v23.0.0 | Runtime deprecation.
v20.13.0 | Documentation-only deprecation.
Type: Runtime
Applications that intend to use authentication tags that are shorter than the default authentication tag length must set the `authTagLength` option of the [`crypto.createDecipheriv()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatedecipherivalgorithm-key-iv-options) function to the appropriate length.
For ciphers in GCM mode, the [`decipher.setAuthTag()`](https://nodejs.org/docs/latest/api/crypto.html#deciphersetauthtagbuffer-encoding) function accepts authentication tags of any valid length (see [DEP0090](https://nodejs.org/docs/latest/api/deprecations.html#DEP0090)). This behavior is deprecated to better align with recommendations per
#### DEP0183: OpenSSL engine-based APIs[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0183-openssl-engine-based-apis)
History Version | Changes
---|---
v22.4.0, v20.16.0 | Documentation-only deprecation.
Type: Documentation-only
OpenSSL 3 has deprecated support for custom engines with a recommendation to switch to its new provider model. The `clientCertEngine` option for `https.request()`, [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions), and [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener); the `privateKeyEngine` and `privateKeyIdentifier` for [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions); and [`crypto.setEngine()`](https://nodejs.org/docs/latest/api/crypto.html#cryptosetengineengine-flags) all depend on this functionality from OpenSSL.
#### DEP0184: Instantiating `node:zlib` classes without `new`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0184-instantiating-nodezlib-classes-without-new)
History Version | Changes
---|---
v24.0.0 | Runtime deprecation.
v22.9.0, v20.18.0 | Documentation-only deprecation.
Type: Runtime
Instantiating classes without the `new` qualifier exported by the `node:zlib` module is deprecated. It is recommended to use the `new` qualifier instead. This applies to all Zlib classes, such as `Deflate`, `DeflateRaw`, `Gunzip`, `Inflate`, `InflateRaw`, `Unzip`, and `Zlib`.
#### DEP0185: Instantiating `node:repl` classes without `new`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0185-instantiating-noderepl-classes-without-new)
History Version | Changes
---|---
v25.0.0 | End-of-Life.
v24.0.0 | Runtime deprecation.
v22.9.0, v20.18.0 | Documentation-only deprecation.
Type: End-of-Life
Instantiating classes without the `new` qualifier exported by the `node:repl` module is deprecated. The `new` qualifier must be used instead. This applies to all REPL classes, including `REPLServer` and `Recoverable`.
An automated migration is available (
```
npx codemod@latest @nodejs/repl-classes-with-new
copy
```

#### DEP0187: Passing invalid argument types to `fs.existsSync`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0187-passing-invalid-argument-types-to-fsexistssync)
History Version | Changes
---|---
v24.0.0 | Runtime deprecation.
v23.4.0, v22.13.0, v20.19.3 | Documentation-only.
Type: Runtime
Passing non-supported argument types is deprecated and, instead of returning `false`, will throw an error in a future version.
#### DEP0188: `process.features.ipv6` and `process.features.uv`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0188-processfeaturesipv6-and-processfeaturesuv)
History Version | Changes
---|---
v23.4.0, v22.13.0 | Documentation-only deprecation.
Type: Documentation-only
These properties are unconditionally `true`. Any checks based on these properties are redundant.
#### DEP0189: `process.features.tls_*`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0189-processfeaturestls)
History Version | Changes
---|---
v23.4.0, v22.13.0 | Documentation-only deprecation.
Type: Documentation-only
`process.features.tls_alpn`, `process.features.tls_ocsp`, and `process.features.tls_sni` are deprecated, as their values are guaranteed to be identical to that of `process.features.tls`.
#### DEP0190: Passing `args` to `node:child_process` `execFile`/`spawn` with `shell` option `true`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0190-passing-args-to-nodechild-process-execfilespawn-with-shell-option-true)
History Version | Changes
---|---
v24.0.0 | Runtime deprecation.
v23.11.0, v22.15.0 | Documentation-only deprecation.
Type: Runtime
When an `args` array is passed to [`child_process.execFile`](https://nodejs.org/docs/latest/api/child_process.html#child_processexecfilefile-args-options-callback) or [`child_process.spawn`](https://nodejs.org/docs/latest/api/child_process.html#child_processspawncommand-args-options) with the option `{ shell: true }`, the values are not escaped, only space-separated, which can lead to shell injection.
#### DEP0191: `repl.builtinModules`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0191-replbuiltinmodules)
History Version | Changes
---|---
v24.0.0, v22.16.0 | Documentation-only deprecation with `--pending-deprecation` support.
Type: Documentation-only (supports [`--pending-deprecation`](https://nodejs.org/docs/latest/api/cli.html#--pending-deprecation))
The `node:repl` module exports a `builtinModules` property that contains an array of built-in modules. This was incomplete and matched the already deprecated `repl._builtinLibs` ([DEP0142](https://nodejs.org/docs/latest/api/deprecations.html#dep0142-repl_builtinlibs)) instead it's better to rely upon `require('node:module').builtinModules`.
An automated migration is available (
```
npx codemod@latest @nodejs/repl-builtin-modules
copy
```

#### DEP0192: `require('node:_tls_common')` and `require('node:_tls_wrap')`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0192-requirenode-tls-common-and-requirenode-tls-wrap)
History Version | Changes
---|---
v24.2.0, v22.17.0 | Runtime deprecation.
Type: Runtime
The `node:_tls_common` and `node:_tls_wrap` modules are deprecated as they should be considered an internal nodejs implementation rather than a public facing API, use `node:tls` instead.
#### DEP0193: `require('node:_stream_*')`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0193-requirenode-stream)
History Version | Changes
---|---
v24.2.0, v22.17.0 | Runtime deprecation.
Type: Runtime
The `node:_stream_duplex`, `node:_stream_passthrough`, `node:_stream_readable`, `node:_stream_transform`, `node:_stream_wrap` and `node:_stream_writable` modules are deprecated as they should be considered an internal nodejs implementation rather than a public facing API, use `node:stream` instead.
#### DEP0194: HTTP/2 priority signaling[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0194-http2-priority-signaling)
History Version | Changes
---|---
v24.2.0 | End-of-Life.
v24.2.0, v22.17.0 | Documentation-only deprecation.
Type: End-of-Life
The support for priority signaling has been removed following its deprecation in the
#### DEP0195: Instantiating `node:http` classes without `new`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0195-instantiating-nodehttp-classes-without-new)
History Version | Changes
---|---
v24.2.0, v22.17.0 | Documentation-only deprecation.
Type: Documentation-only
Instantiating classes without the `new` qualifier exported by the `node:http` module is deprecated. It is recommended to use the `new` qualifier instead. This applies to all http classes, such as `OutgoingMessage`, `IncomingMessage`, `ServerResponse` and `ClientRequest`.
An automated migration is available (
```
npx codemod@latest @nodejs/http-classes-with-new
copy
```

#### DEP0196: Calling `node:child_process` functions with `options.shell` as an empty string[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0196-calling-nodechild-process-functions-with-optionsshell-as-an-empty-string)
History Version | Changes
---|---
v24.2.0, v22.17.0 | Documentation-only deprecation.
Type: Documentation-only
Calling the process-spawning functions with `{ shell: '' }` is almost certainly unintentional, and can cause aberrant behavior.
To make [`child_process.execFile`](https://nodejs.org/docs/latest/api/child_process.html#child_processexecfilefile-args-options-callback) or [`child_process.spawn`](https://nodejs.org/docs/latest/api/child_process.html#child_processspawncommand-args-options) invoke the default shell, use `{ shell: true }`. If the intention is not to invoke a shell (default behavior), either omit the `shell` option, or set it to `false` or a nullish value.
To make [`child_process.exec`](https://nodejs.org/docs/latest/api/child_process.html#child_processexeccommand-options-callback) invoke the default shell, either omit the `shell` option, or set it to a nullish value. If the intention is not to invoke a shell, use [`child_process.execFile`](https://nodejs.org/docs/latest/api/child_process.html#child_processexecfilefile-args-options-callback) instead.
#### DEP0197: `util.types.isNativeError()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0197-utiltypesisnativeerror)
History Version | Changes
---|---
v24.2.0 | Documentation-only deprecation.
Type: Documentation-only
The [`util.types.isNativeError`](https://nodejs.org/docs/latest/api/util.html#utiltypesisnativeerrorvalue) API is deprecated. Please use
An automated migration is available (
```
npx codemod@latest @nodejs/types-is-native-error
copy
```

#### DEP0198: Creating SHAKE-128 and SHAKE-256 digests without an explicit `options.outputLength`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0198-creating-shake-128-and-shake-256-digests-without-an-explicit-optionsoutputlength)
History Version | Changes
---|---
v25.0.0 | Runtime deprecation.
v24.4.0, v22.18.0, v20.19.5 | Documentation-only deprecation with support for `--pending-deprecation`.
Type: Runtime
Creating SHAKE-128 and SHAKE-256 digests without an explicit `options.outputLength` is deprecated.
#### DEP0199: `require('node:_http_*')`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0199-requirenode-http)
History Version | Changes
---|---
v24.6.0, v22.19.0 | Documentation-only deprecation.
Type: Documentation-only
The `node:_http_agent`, `node:_http_client`, `node:_http_common`, `node:_http_incoming`, `node:_http_outgoing` and `node:_http_server` modules are deprecated as they should be considered an internal nodejs implementation rather than a public facing API, use `node:http` instead.
#### DEP0200: Closing fs.Dir on garbage collection[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0200-closing-fsdir-on-garbage-collection)
History Version | Changes
---|---
v24.9.0 | Documentation-only deprecation.
Type: Documentation-only
Allowing a [`fs.Dir`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir) object to be closed on garbage collection is deprecated. In the future, doing so might result in a thrown error that will terminate the process.
Please ensure that all `fs.Dir` objects are explicitly closed using `Dir.prototype.close()` or `using` keyword:
```
import { opendir } from 'node:fs/promises';

{
  await using dir = await opendir('/async/disposable/directory');
} // Closed by dir[Symbol.asyncDispose]()

{
  using dir = await opendir('/sync/disposable/directory');
} // Closed by dir[Symbol.dispose]()

{
  const dir = await opendir('/unconditionally/iterated/directory');
  for await (const entry of dir) {
    // process an entry
  } // Closed by iterator
}

{
  let dir;
  try {
    dir = await opendir('/legacy/closeable/directory');
  } finally {
    await dir?.close();
  }
}
copy
```

#### DEP0201: Passing `options.type` to `Duplex.toWeb()`[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0201-passing-optionstype-to-duplextoweb)
History Version | Changes
---|---
v25.7.0 | Documentation-only deprecation.
Type: Documentation-only
Passing the `type` option to [`Duplex.toWeb()`](https://nodejs.org/docs/latest/api/stream.html#streamduplextowebstreamduplex-options) is deprecated. To specify the type of the readable half of the constructed readable-writable pair, use the `readableType` option instead.
#### DEP0202: `Http1IncomingMessage` and `Http1ServerResponse` options of HTTP/2 servers[#](https://nodejs.org/docs/latest/api/deprecations.html#dep0202-http1incomingmessage-and-http1serverresponse-options-of-http2-servers)
History Version | Changes
---|---
v25.7.0 | Documentation-only deprecation.
Type: Documentation-only
The `Http1IncomingMessage` and `Http1ServerResponse` options of [`http2.createServer()`](https://nodejs.org/docs/latest/api/http2.html#http2createserveroptions-onrequesthandler) and [`http2.createSecureServer()`](https://nodejs.org/docs/latest/api/http2.html#http2createsecureserveroptions-onrequesthandler) are deprecated. Use `http1Options.IncomingMessage` and `http1Options.ServerResponse` instead.
```
// Deprecated
const server = http2.createSecureServer({
  allowHTTP1: true,
  Http1IncomingMessage: MyIncomingMessage,
  Http1ServerResponse: MyServerResponse,
});
// Use this instead
const server = http2.createSecureServer({
  allowHTTP1: true,
  http1Options: {
    IncomingMessage: MyIncomingMessage,
    ServerResponse: MyServerResponse,
  },
});
copy
```
