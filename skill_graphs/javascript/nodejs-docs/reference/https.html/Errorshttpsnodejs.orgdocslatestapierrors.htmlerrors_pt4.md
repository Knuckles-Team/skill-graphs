####  `ERR_NAPI_INVALID_TYPEDARRAY_ALIGNMENT`[#](https://nodejs.org/docs/latest/api/errors.html#err-napi-invalid-typedarray-alignment)
While calling `napi_create_typedarray()`, the provided `offset` was not a multiple of the element size.
####  `ERR_NAPI_INVALID_TYPEDARRAY_LENGTH`[#](https://nodejs.org/docs/latest/api/errors.html#err-napi-invalid-typedarray-length)
While calling `napi_create_typedarray()`, `(length * size_of_element) + byte_offset` was larger than the length of given `buffer`.
####  `ERR_NAPI_TSFN_CALL_JS`[#](https://nodejs.org/docs/latest/api/errors.html#err-napi-tsfn-call-js)
An error occurred while invoking the JavaScript portion of the thread-safe function.
####  `ERR_NAPI_TSFN_GET_UNDEFINED`[#](https://nodejs.org/docs/latest/api/errors.html#err-napi-tsfn-get-undefined)
An error occurred while attempting to retrieve the JavaScript `undefined` value.
####  `ERR_NON_CONTEXT_AWARE_DISABLED`[#](https://nodejs.org/docs/latest/api/errors.html#err-non-context-aware-disabled)
A non-context-aware native addon was loaded in a process that disallows them.
####  `ERR_NOT_BUILDING_SNAPSHOT`[#](https://nodejs.org/docs/latest/api/errors.html#err-not-building-snapshot)
An attempt was made to use operations that can only be used when building V8 startup snapshot even though Node.js isn't building one.
####  `ERR_NOT_IN_SINGLE_EXECUTABLE_APPLICATION`[#](https://nodejs.org/docs/latest/api/errors.html#err-not-in-single-executable-application)
Added in: v21.7.0, v20.12.0
The operation cannot be performed when it's not in a single-executable application.
####  `ERR_NOT_SUPPORTED_IN_SNAPSHOT`[#](https://nodejs.org/docs/latest/api/errors.html#err-not-supported-in-snapshot)
An attempt was made to perform operations that are not supported when building a startup snapshot.
####  `ERR_NO_CRYPTO`[#](https://nodejs.org/docs/latest/api/errors.html#err-no-crypto)
An attempt was made to use crypto features while Node.js was not compiled with OpenSSL crypto support.
####  `ERR_NO_ICU`[#](https://nodejs.org/docs/latest/api/errors.html#err-no-icu)
An attempt was made to use features that require [ICU](https://nodejs.org/docs/latest/api/intl.html#internationalization-support), but Node.js was not compiled with ICU support.
####  `ERR_NO_TYPESCRIPT`[#](https://nodejs.org/docs/latest/api/errors.html#err-no-typescript)
Added in: v23.0.0, v22.12.0
An attempt was made to use features that require [Native TypeScript support](https://nodejs.org/docs/latest/api/typescript.html#type-stripping), but Node.js was not compiled with TypeScript support.
####  `ERR_OPERATION_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-operation-failed)
Added in: v15.0.0
An operation failed. This is typically used to signal the general failure of an asynchronous operation.
####  `ERR_OPTIONS_BEFORE_BOOTSTRAPPING`[#](https://nodejs.org/docs/latest/api/errors.html#err-options-before-bootstrapping)
Added in: v23.10.0, v22.16.0
An attempt was made to get options before the bootstrapping was completed.
####  `ERR_OUT_OF_RANGE`[#](https://nodejs.org/docs/latest/api/errors.html#err-out-of-range)
A given value is out of the accepted range.
####  `ERR_PACKAGE_IMPORT_NOT_DEFINED`[#](https://nodejs.org/docs/latest/api/errors.html#err-package-import-not-defined)
The `package.json` [`"imports"`](https://nodejs.org/docs/latest/api/packages.html#imports) field does not define the given internal package specifier mapping.
####  `ERR_PACKAGE_PATH_NOT_EXPORTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-package-path-not-exported)
The `package.json` [`"exports"`](https://nodejs.org/docs/latest/api/packages.html#exports) field does not export the requested subpath. Because exports are encapsulated, private internal modules that are not exported cannot be imported through the package resolution, unless using an absolute URL.
####  `ERR_PARSE_ARGS_INVALID_OPTION_VALUE`[#](https://nodejs.org/docs/latest/api/errors.html#err-parse-args-invalid-option-value)
Added in: v18.3.0, v16.17.0
When `strict` set to `true`, thrown by [`util.parseArgs()`](https://nodejs.org/docs/latest/api/util.html#utilparseargsconfig) if a
####  `ERR_PARSE_ARGS_UNEXPECTED_POSITIONAL`[#](https://nodejs.org/docs/latest/api/errors.html#err-parse-args-unexpected-positional)
Added in: v18.3.0, v16.17.0
Thrown by [`util.parseArgs()`](https://nodejs.org/docs/latest/api/util.html#utilparseargsconfig), when a positional argument is provided and `allowPositionals` is set to `false`.
####  `ERR_PARSE_ARGS_UNKNOWN_OPTION`[#](https://nodejs.org/docs/latest/api/errors.html#err-parse-args-unknown-option)
Added in: v18.3.0, v16.17.0
When `strict` set to `true`, thrown by [`util.parseArgs()`](https://nodejs.org/docs/latest/api/util.html#utilparseargsconfig) if an argument is not configured in `options`.
####  `ERR_PERFORMANCE_INVALID_TIMESTAMP`[#](https://nodejs.org/docs/latest/api/errors.html#err-performance-invalid-timestamp)
An invalid timestamp value was provided for a performance mark or measure.
####  `ERR_PERFORMANCE_MEASURE_INVALID_OPTIONS`[#](https://nodejs.org/docs/latest/api/errors.html#err-performance-measure-invalid-options)
Invalid options were provided for a performance measure.
####  `ERR_PROTO_ACCESS`[#](https://nodejs.org/docs/latest/api/errors.html#err-proto-access)
Accessing `Object.prototype.__proto__` has been forbidden using [`--disable-proto=throw`](https://nodejs.org/docs/latest/api/cli.html#--disable-protomode).
####  `ERR_PROXY_INVALID_CONFIG`[#](https://nodejs.org/docs/latest/api/errors.html#err-proxy-invalid-config)
Failed to proxy a request because the proxy configuration is invalid.
####  `ERR_PROXY_TUNNEL`[#](https://nodejs.org/docs/latest/api/errors.html#err-proxy-tunnel)
Failed to establish proxy tunnel when `NODE_USE_ENV_PROXY` or `--use-env-proxy` is enabled.
####  `ERR_QUIC_APPLICATION_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-quic-application-error)
Added in: v23.4.0, v22.13.0
[Stability: 1](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Experimental
A QUIC application error occurred.
####  `ERR_QUIC_CONNECTION_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-quic-connection-failed)
Added in: v23.0.0, v22.10.0
Stability: 1 - Experimental
Establishing a QUIC connection failed.
####  `ERR_QUIC_ENDPOINT_CLOSED`[#](https://nodejs.org/docs/latest/api/errors.html#err-quic-endpoint-closed)
Added in: v23.0.0, v22.10.0
Stability: 1 - Experimental
A QUIC Endpoint closed with an error.
####  `ERR_QUIC_OPEN_STREAM_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-quic-open-stream-failed)
Added in: v23.0.0, v22.10.0
Stability: 1 - Experimental
Opening a QUIC stream failed.
####  `ERR_QUIC_TRANSPORT_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-quic-transport-error)
Added in: v23.4.0, v22.13.0
Stability: 1 - Experimental
A QUIC transport error occurred.
####  `ERR_QUIC_VERSION_NEGOTIATION_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-quic-version-negotiation-error)
Added in: v23.4.0, v22.13.0
Stability: 1 - Experimental
A QUIC session failed because version negotiation is required.
####  `ERR_REQUIRE_ASYNC_MODULE`[#](https://nodejs.org/docs/latest/api/errors.html#err-require-async-module)
When trying to `require()` a [ES Module](https://nodejs.org/docs/latest/api/esm.html), the module turns out to be asynchronous. That is, it contains top-level await.
To see where the top-level await is, use `--experimental-print-required-tla` (this would execute the modules before looking for the top-level awaits).
####  `ERR_REQUIRE_CYCLE_MODULE`[#](https://nodejs.org/docs/latest/api/errors.html#err-require-cycle-module)
When trying to `require()` a [ES Module](https://nodejs.org/docs/latest/api/esm.html), a CommonJS to ESM or ESM to CommonJS edge participates in an immediate cycle. This is not allowed because ES Modules cannot be evaluated while they are already being evaluated.
To avoid the cycle, the `require()` call involved in a cycle should not happen at the top-level of either an ES Module (via `createRequire()`) or a CommonJS module, and should be done lazily in an inner function.
####  `ERR_REQUIRE_ESM`[#](https://nodejs.org/docs/latest/api/errors.html#err-require-esm)
History Version | Changes
---|---
v23.0.0, v22.12.0, v20.19.0 | require() now supports loading synchronous ES modules by default.
Stability: 0 - Deprecated
An attempt was made to `require()` an [ES Module](https://nodejs.org/docs/latest/api/esm.html).
This error has been deprecated since `require()` now supports loading synchronous ES modules. When `require()` encounters an ES module that contains top-level `await`, it will throw [`ERR_REQUIRE_ASYNC_MODULE`](https://nodejs.org/docs/latest/api/errors.html#err_require_async_module) instead.
####  `ERR_SCRIPT_EXECUTION_INTERRUPTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-script-execution-interrupted)
Script execution was interrupted by `SIGINT` (For example, `Ctrl`+`C` was pressed.)
####  `ERR_SCRIPT_EXECUTION_TIMEOUT`[#](https://nodejs.org/docs/latest/api/errors.html#err-script-execution-timeout)
Script execution timed out, possibly due to bugs in the script being executed.
####  `ERR_SERVER_ALREADY_LISTEN`[#](https://nodejs.org/docs/latest/api/errors.html#err-server-already-listen)
The [`server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) method was called while a `net.Server` was already listening. This applies to all instances of `net.Server`, including HTTP, HTTPS, and HTTP/2 `Server` instances.
####  `ERR_SERVER_NOT_RUNNING`[#](https://nodejs.org/docs/latest/api/errors.html#err-server-not-running)
The [`server.close()`](https://nodejs.org/docs/latest/api/net.html#serverclosecallback) method was called when a `net.Server` was not running. This applies to all instances of `net.Server`, including HTTP, HTTPS, and HTTP/2 `Server` instances.
####  `ERR_SINGLE_EXECUTABLE_APPLICATION_ASSET_NOT_FOUND`[#](https://nodejs.org/docs/latest/api/errors.html#err-single-executable-application-asset-not-found)
Added in: v21.7.0, v20.12.0
A key was passed to single executable application APIs to identify an asset, but no match could be found.
####  `ERR_SOCKET_ALREADY_BOUND`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-already-bound)
An attempt was made to bind a socket that has already been bound.
####  `ERR_SOCKET_BAD_BUFFER_SIZE`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-bad-buffer-size)
An invalid (negative) size was passed for either the `recvBufferSize` or `sendBufferSize` options in [`dgram.createSocket()`](https://nodejs.org/docs/latest/api/dgram.html#dgramcreatesocketoptions-callback).
####  `ERR_SOCKET_BAD_PORT`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-bad-port)
An API function expecting a port >= 0 and < 65536 received an invalid value.
####  `ERR_SOCKET_BAD_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-bad-type)
An API function expecting a socket type (`udp4` or `udp6`) received an invalid value.
####  `ERR_SOCKET_BUFFER_SIZE`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-buffer-size)
While using [`dgram.createSocket()`](https://nodejs.org/docs/latest/api/dgram.html#dgramcreatesocketoptions-callback), the size of the receive or send `Buffer` could not be determined.
####  `ERR_SOCKET_CLOSED`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-closed)
An attempt was made to operate on an already closed socket.
####  `ERR_SOCKET_CLOSED_BEFORE_CONNECTION`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-closed-before-connection)
When calling [`net.Socket.write()`](https://nodejs.org/docs/latest/api/net.html#socketwritedata-encoding-callback) on a connecting socket and the socket was closed before the connection was established.
####  `ERR_SOCKET_CONNECTION_TIMEOUT`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-connection-timeout)
The socket was unable to connect to any address returned by the DNS within the allowed timeout when using the family autoselection algorithm.
####  `ERR_SOCKET_DGRAM_IS_CONNECTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-dgram-is-connected)
A [`dgram.connect()`](https://nodejs.org/docs/latest/api/dgram.html#socketconnectport-address-callback) call was made on an already connected socket.
####  `ERR_SOCKET_DGRAM_NOT_CONNECTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-dgram-not-connected)
A [`dgram.disconnect()`](https://nodejs.org/docs/latest/api/dgram.html#socketdisconnect) or [`dgram.remoteAddress()`](https://nodejs.org/docs/latest/api/dgram.html#socketremoteaddress) call was made on a disconnected socket.
####  `ERR_SOCKET_DGRAM_NOT_RUNNING`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-dgram-not-running)
A call was made and the UDP subsystem was not running.
####  `ERR_SOURCE_MAP_CORRUPT`[#](https://nodejs.org/docs/latest/api/errors.html#err-source-map-corrupt)
The source map could not be parsed because it does not exist, or is corrupt.
####  `ERR_SOURCE_MAP_MISSING_SOURCE`[#](https://nodejs.org/docs/latest/api/errors.html#err-source-map-missing-source)
A file imported from a source map was not found.
####  `ERR_SOURCE_PHASE_NOT_DEFINED`[#](https://nodejs.org/docs/latest/api/errors.html#err-source-phase-not-defined)
Added in: v24.0.0
The provided module import does not provide a source phase imports representation for source phase import syntax `import source x from 'x'` or `import.source(x)`.
####  `ERR_SQLITE_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-sqlite-error)
Added in: v22.5.0
An error was returned from [SQLite](https://nodejs.org/docs/latest/api/sqlite.html).
####  `ERR_SRI_PARSE`[#](https://nodejs.org/docs/latest/api/errors.html#err-sri-parse)
A string was provided for a Subresource Integrity check, but was unable to be parsed. Check the format of integrity attributes by looking at the
####  `ERR_STREAM_ALREADY_FINISHED`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-already-finished)
A stream method was called that cannot complete because the stream was finished.
####  `ERR_STREAM_CANNOT_PIPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-cannot-pipe)
An attempt was made to call [`stream.pipe()`](https://nodejs.org/docs/latest/api/stream.html#readablepipedestination-options) on a [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) stream.
####  `ERR_STREAM_DESTROYED`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-destroyed)
A stream method was called that cannot complete because the stream was destroyed using `stream.destroy()`.
####  `ERR_STREAM_NULL_VALUES`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-null-values)
An attempt was made to call [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) with a `null` chunk.
####  `ERR_STREAM_PREMATURE_CLOSE`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-premature-close)
An error returned by `stream.finished()` and `stream.pipeline()`, when a stream or a pipeline ends non gracefully with no explicit error.
####  `ERR_STREAM_PUSH_AFTER_EOF`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-push-after-eof)
An attempt was made to call [`stream.push()`](https://nodejs.org/docs/latest/api/stream.html#readablepushchunk-encoding) after a `null`(EOF) had been pushed to the stream.
####  `ERR_STREAM_UNABLE_TO_PIPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-unable-to-pipe)
An attempt was made to pipe to a closed or destroyed stream in a pipeline.
####  `ERR_STREAM_UNSHIFT_AFTER_END_EVENT`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-unshift-after-end-event)
An attempt was made to call [`stream.unshift()`](https://nodejs.org/docs/latest/api/stream.html#readableunshiftchunk-encoding) after the `'end'` event was emitted.
####  `ERR_STREAM_WRAP`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-wrap)
Prevents an abort if a string decoder was set on the Socket or if the decoder is in `objectMode`.
```
const Socket = require('node:net').Socket;
const instance = new Socket();

instance.setEncoding('utf8');
copy
```

####  `ERR_STREAM_WRITE_AFTER_END`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-write-after-end)
An attempt was made to call [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) after `stream.end()` has been called.
####  `ERR_STRING_TOO_LONG`[#](https://nodejs.org/docs/latest/api/errors.html#err-string-too-long)
An attempt has been made to create a string longer than the maximum allowed length.
####  `ERR_SYNTHETIC`[#](https://nodejs.org/docs/latest/api/errors.html#err-synthetic)
An artificial error object used to capture the call stack for diagnostic reports.
####  `ERR_SYSTEM_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-system-error)
An unspecified or non-specific system error has occurred within the Node.js process. The error object will have an `err.info` object property with additional details.
####  `ERR_TEST_FAILURE`[#](https://nodejs.org/docs/latest/api/errors.html#err-test-failure)
This error represents a failed test. Additional information about the failure is available via the `cause` property. The `failureType` property specifies what the test was doing when the failure occurred.
####  `ERR_TLS_ALPN_CALLBACK_INVALID_RESULT`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-alpn-callback-invalid-result)
This error is thrown when an `ALPNCallback` returns a value that is not in the list of ALPN protocols offered by the client.
####  `ERR_TLS_ALPN_CALLBACK_WITH_PROTOCOLS`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-alpn-callback-with-protocols)
This error is thrown when creating a `TLSServer` if the TLS options include both `ALPNProtocols` and `ALPNCallback`. These options are mutually exclusive.
####  `ERR_TLS_CERT_ALTNAME_FORMAT`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-cert-altname-format)
This error is thrown by `checkServerIdentity` if a user-supplied `subjectaltname` property violates encoding rules. Certificate objects produced by Node.js itself always comply with encoding rules and will never cause this error.
####  `ERR_TLS_CERT_ALTNAME_INVALID`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-cert-altname-invalid)
While using TLS, the host name/IP of the peer did not match any of the `subjectAltNames` in its certificate.
####  `ERR_TLS_DH_PARAM_SIZE`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-dh-param-size)
While using TLS, the parameter offered for the Diffie-Hellman (`DH`) key-agreement protocol is too small. By default, the key length must be greater than or equal to 1024 bits to avoid vulnerabilities, even though it is strongly recommended to use 2048 bits or larger for stronger security.
####  `ERR_TLS_HANDSHAKE_TIMEOUT`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-handshake-timeout)
A TLS/SSL handshake timed out. In this case, the server must also abort the connection.
####  `ERR_TLS_INVALID_CONTEXT`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-invalid-context)
Added in: v13.3.0
The context must be a `SecureContext`.
####  `ERR_TLS_INVALID_PROTOCOL_METHOD`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-invalid-protocol-method)
The specified `secureProtocol` method is invalid. It is either unknown, or disabled because it is insecure.
####  `ERR_TLS_INVALID_PROTOCOL_VERSION`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-invalid-protocol-version)
Valid TLS protocol versions are `'TLSv1'`, `'TLSv1.1'`, or `'TLSv1.2'`.
####  `ERR_TLS_INVALID_STATE`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-invalid-state)
Added in: v13.10.0, v12.17.0
The TLS socket must be connected and securely established. Ensure the 'secure' event is emitted before continuing.
####  `ERR_TLS_PROTOCOL_VERSION_CONFLICT`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-protocol-version-conflict)
Attempting to set a TLS protocol `minVersion` or `maxVersion` conflicts with an attempt to set the `secureProtocol` explicitly. Use one mechanism or the other.
####  `ERR_TLS_PSK_SET_IDENTITY_HINT_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-psk-set-identity-hint-failed)
Failed to set PSK identity hint. Hint may be too long.
####  `ERR_TLS_RENEGOTIATION_DISABLED`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-renegotiation-disabled)
An attempt was made to renegotiate TLS on a socket instance with renegotiation disabled.
####  `ERR_TLS_REQUIRED_SERVER_NAME`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-required-server-name)
While using TLS, the `server.addContext()` method was called without providing a host name in the first parameter.
####  `ERR_TLS_SESSION_ATTACK`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-session-attack)
An excessive amount of TLS renegotiations is detected, which is a potential vector for denial-of-service attacks.
####  `ERR_TLS_SNI_FROM_SERVER`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-sni-from-server)
An attempt was made to issue Server Name Indication from a TLS server-side socket, which is only valid from a client.
####  `ERR_TRACE_EVENTS_CATEGORY_REQUIRED`[#](https://nodejs.org/docs/latest/api/errors.html#err-trace-events-category-required)
The `trace_events.createTracing()` method requires at least one trace event category.
####  `ERR_TRACE_EVENTS_UNAVAILABLE`[#](https://nodejs.org/docs/latest/api/errors.html#err-trace-events-unavailable)
The `node:trace_events` module could not be loaded because Node.js was compiled with the `--without-v8-platform` flag.
####  `ERR_TRAILING_JUNK_AFTER_STREAM_END`[#](https://nodejs.org/docs/latest/api/errors.html#err-trailing-junk-after-stream-end)
Trailing junk found after the end of the compressed stream. This error is thrown when extra, unexpected data is detected after the end of a compressed stream (for example, in zlib or gzip decompression).
####  `ERR_TRANSFORM_ALREADY_TRANSFORMING`[#](https://nodejs.org/docs/latest/api/errors.html#err-transform-already-transforming)
A `Transform` stream finished while it was still transforming.
####  `ERR_TRANSFORM_WITH_LENGTH_0`[#](https://nodejs.org/docs/latest/api/errors.html#err-transform-with-length-0)
A `Transform` stream finished with data still in the write buffer.
####  `ERR_TTY_INIT_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-tty-init-failed)
The initialization of a TTY failed due to a system error.
####  `ERR_UNAVAILABLE_DURING_EXIT`[#](https://nodejs.org/docs/latest/api/errors.html#err-unavailable-during-exit)
Function was called within a [`process.on('exit')`](https://nodejs.org/docs/latest/api/process.html#event-exit) handler that shouldn't be called within [`process.on('exit')`](https://nodejs.org/docs/latest/api/process.html#event-exit) handler.
####  `ERR_UNCAUGHT_EXCEPTION_CAPTURE_ALREADY_SET`[#](https://nodejs.org/docs/latest/api/errors.html#err-uncaught-exception-capture-already-set)
[`process.setUncaughtExceptionCaptureCallback()`](https://nodejs.org/docs/latest/api/process.html#processsetuncaughtexceptioncapturecallbackfn) was called twice, without first resetting the callback to `null`.
This error is designed to prevent accidentally overwriting a callback registered from another module.
####  `ERR_UNESCAPED_CHARACTERS`[#](https://nodejs.org/docs/latest/api/errors.html#err-unescaped-characters)
A string that contained unescaped characters was received.
####  `ERR_UNHANDLED_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-unhandled-error)
An unhandled error occurred (for instance, when an `'error'` event is emitted by an [`EventEmitter`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) but an `'error'` handler is not registered).
####  `ERR_UNKNOWN_BUILTIN_MODULE`[#](https://nodejs.org/docs/latest/api/errors.html#err-unknown-builtin-module)
Used to identify a specific kind of internal Node.js error that should not typically be triggered by user code. Instances of this error point to an internal bug within the Node.js binary itself.
####  `ERR_UNKNOWN_CREDENTIAL`[#](https://nodejs.org/docs/latest/api/errors.html#err-unknown-credential)
A Unix group or user identifier that does not exist was passed.
####  `ERR_UNKNOWN_ENCODING`[#](https://nodejs.org/docs/latest/api/errors.html#err-unknown-encoding)
An invalid or unknown encoding option was passed to an API.
####  `ERR_UNKNOWN_FILE_EXTENSION`[#](https://nodejs.org/docs/latest/api/errors.html#err-unknown-file-extension)
An attempt was made to load a module with an unknown or unsupported file extension.
####  `ERR_UNKNOWN_MODULE_FORMAT`[#](https://nodejs.org/docs/latest/api/errors.html#err-unknown-module-format)
An attempt was made to load a module with an unknown or unsupported format.
####  `ERR_UNKNOWN_SIGNAL`[#](https://nodejs.org/docs/latest/api/errors.html#err-unknown-signal)
An invalid or unknown process signal was passed to an API expecting a valid signal (such as [`subprocess.kill()`](https://nodejs.org/docs/latest/api/child_process.html#subprocesskillsignal)).
####  `ERR_UNSUPPORTED_DIR_IMPORT`[#](https://nodejs.org/docs/latest/api/errors.html#err-unsupported-dir-import)
`import` a directory URL is unsupported. Instead, [self-reference a package using its name](https://nodejs.org/docs/latest/api/packages.html#self-referencing-a-package-using-its-name) and [define a custom subpath](https://nodejs.org/docs/latest/api/packages.html#subpath-exports) in the [`"exports"`](https://nodejs.org/docs/latest/api/packages.html#exports) field of the [`package.json`](https://nodejs.org/docs/latest/api/packages.html#nodejs-packagejson-field-definitions) file.
