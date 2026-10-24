```
import './'; // unsupported
import './index.js'; // supported
import 'package-name'; // supported
copy
```

####  `ERR_UNSUPPORTED_ESM_URL_SCHEME`[#](https://nodejs.org/docs/latest/api/errors.html#err-unsupported-esm-url-scheme)
`import` with URL schemes other than `file` and `data` is unsupported.
####  `ERR_UNSUPPORTED_NODE_MODULES_TYPE_STRIPPING`[#](https://nodejs.org/docs/latest/api/errors.html#err-unsupported-node-modules-type-stripping)
Added in: v22.6.0
Type stripping is not supported for files descendent of a `node_modules` directory.
####  `ERR_UNSUPPORTED_RESOLVE_REQUEST`[#](https://nodejs.org/docs/latest/api/errors.html#err-unsupported-resolve-request)
An attempt was made to resolve an invalid module referrer. This can happen when importing or calling `import.meta.resolve()` with either:
  * a bare specifier that is not a builtin module from a module whose URL scheme is not `file`.
  * a

```
try {
  // Trying to import the package 'bare-specifier' from a `data:` URL module:
  await import('data:text/javascript,import "bare-specifier"');
} catch (e) {
  console.log(e.code); // ERR_UNSUPPORTED_RESOLVE_REQUEST
}
copy
```

####  `ERR_UNSUPPORTED_TYPESCRIPT_SYNTAX`[#](https://nodejs.org/docs/latest/api/errors.html#err-unsupported-typescript-syntax)
Added in: v23.7.0, v22.14.0
The provided TypeScript syntax is unsupported. This could happen when using TypeScript syntax that requires transformation with [type-stripping](https://nodejs.org/docs/latest/api/typescript.html#type-stripping).
####  `ERR_USE_AFTER_CLOSE`[#](https://nodejs.org/docs/latest/api/errors.html#err-use-after-close)
An attempt was made to use something that was already closed.
####  `ERR_VALID_PERFORMANCE_ENTRY_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-valid-performance-entry-type)
While using the Performance Timing API (`perf_hooks`), no valid performance entry types are found.
####  `ERR_VM_DYNAMIC_IMPORT_CALLBACK_MISSING`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-dynamic-import-callback-missing)
A dynamic import callback was not specified.
####  `ERR_VM_DYNAMIC_IMPORT_CALLBACK_MISSING_FLAG`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-dynamic-import-callback-missing-flag)
A dynamic import callback was invoked without `--experimental-vm-modules`.
####  `ERR_VM_MODULE_ALREADY_LINKED`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-module-already-linked)
The module attempted to be linked is not eligible for linking, because of one of the following reasons:
  * It has already been linked (`linkingStatus` is `'linked'`)
  * It is being linked (`linkingStatus` is `'linking'`)
  * Linking has failed for this module (`linkingStatus` is `'errored'`)


####  `ERR_VM_MODULE_CACHED_DATA_REJECTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-module-cached-data-rejected)
The `cachedData` option passed to a module constructor is invalid.
####  `ERR_VM_MODULE_CANNOT_CREATE_CACHED_DATA`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-module-cannot-create-cached-data)
Cached data cannot be created for modules which have already been evaluated.
####  `ERR_VM_MODULE_DIFFERENT_CONTEXT`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-module-different-context)
The module being returned from the linker function is from a different context than the parent module. Linked modules must share the same context.
####  `ERR_VM_MODULE_LINK_FAILURE`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-module-link-failure)
The module was unable to be linked due to a failure.
####  `ERR_VM_MODULE_NOT_MODULE`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-module-not-module)
The fulfilled value of a linking promise is not a `vm.Module` object.
####  `ERR_VM_MODULE_STATUS`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-module-status)
The current module's status does not allow for this operation. The specific meaning of the error depends on the specific function.
####  `ERR_WASI_ALREADY_STARTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-wasi-already-started)
The WASI instance has already started.
####  `ERR_WASI_NOT_STARTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-wasi-not-started)
The WASI instance has not been started.
####  `ERR_WEBASSEMBLY_NOT_SUPPORTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-webassembly-not-supported)
A feature requiring WebAssembly was used, but WebAssembly is not supported or has been disabled in the current environment (for example, when running with `--jitless`).
####  `ERR_WEBASSEMBLY_RESPONSE`[#](https://nodejs.org/docs/latest/api/errors.html#err-webassembly-response)
Added in: v18.1.0
The `Response` that has been passed to `WebAssembly.compileStreaming` or to `WebAssembly.instantiateStreaming` is not a valid WebAssembly response.
####  `ERR_WORKER_INIT_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-init-failed)
The `Worker` initialization failed.
####  `ERR_WORKER_INVALID_EXEC_ARGV`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-invalid-exec-argv)
The `execArgv` option passed to the `Worker` constructor contains invalid flags.
####  `ERR_WORKER_MESSAGING_ERRORED`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-messaging-errored)
Added in: v22.5.0
Stability: 1.1 - Active development
The destination thread threw an error while processing a message sent via [`postMessageToThread()`](https://nodejs.org/docs/latest/api/worker_threads.html#worker_threadspostmessagetothreadthreadid-value-transferlist-timeout).
####  `ERR_WORKER_MESSAGING_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-messaging-failed)
Added in: v22.5.0
Stability: 1.1 - Active development
The thread requested in [`postMessageToThread()`](https://nodejs.org/docs/latest/api/worker_threads.html#worker_threadspostmessagetothreadthreadid-value-transferlist-timeout) is invalid or has no `workerMessage` listener.
####  `ERR_WORKER_MESSAGING_SAME_THREAD`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-messaging-same-thread)
Added in: v22.5.0
Stability: 1.1 - Active development
The thread id requested in [`postMessageToThread()`](https://nodejs.org/docs/latest/api/worker_threads.html#worker_threadspostmessagetothreadthreadid-value-transferlist-timeout) is the current thread id.
####  `ERR_WORKER_MESSAGING_TIMEOUT`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-messaging-timeout)
Added in: v22.5.0
Stability: 1.1 - Active development
Sending a message via [`postMessageToThread()`](https://nodejs.org/docs/latest/api/worker_threads.html#worker_threadspostmessagetothreadthreadid-value-transferlist-timeout) timed out.
####  `ERR_WORKER_NOT_RUNNING`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-not-running)
An operation failed because the `Worker` instance is not currently running.
####  `ERR_WORKER_OUT_OF_MEMORY`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-out-of-memory)
The `Worker` instance terminated because it reached its memory limit.
####  `ERR_WORKER_PATH`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-path)
The path for the main script of a worker is neither an absolute path nor a relative path starting with `./` or `../`.
####  `ERR_WORKER_UNSERIALIZABLE_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-unserializable-error)
All attempts at serializing an uncaught exception from a worker thread failed.
####  `ERR_WORKER_UNSUPPORTED_OPERATION`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-unsupported-operation)
The requested functionality is not supported in worker threads.
####  `ERR_ZLIB_INITIALIZATION_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-zlib-initialization-failed)
Creation of a [`zlib`](https://nodejs.org/docs/latest/api/zlib.html) object failed due to incorrect configuration.
####  `ERR_ZSTD_INVALID_PARAM`[#](https://nodejs.org/docs/latest/api/errors.html#err-zstd-invalid-param)
An invalid parameter key was passed during construction of a Zstd stream.
####  `HPE_CHUNK_EXTENSIONS_OVERFLOW`[#](https://nodejs.org/docs/latest/api/errors.html#hpe-chunk-extensions-overflow)
Added in: v21.6.2, v20.11.1, v18.19.1
Too much data was received for a chunk extensions. In order to protect against malicious or malconfigured clients, if more than 16 KiB of data is received then an `Error` with this code will be emitted.
####  `HPE_HEADER_OVERFLOW`[#](https://nodejs.org/docs/latest/api/errors.html#hpe-header-overflow)
History Version | Changes
---|---
v11.4.0, v10.15.0 | Max header size in `http_parser` was set to 8 KiB.
Too much HTTP header data was received. In order to protect against malicious or malconfigured clients, if more than `maxHeaderSize` of HTTP header data is received then HTTP parsing will abort without a request or response object being created, and an `Error` with this code will be emitted.
####  `HPE_UNEXPECTED_CONTENT_LENGTH`[#](https://nodejs.org/docs/latest/api/errors.html#hpe-unexpected-content-length)
Server is sending both a `Content-Length` header and `Transfer-Encoding: chunked`.
`Transfer-Encoding: chunked` allows the server to maintain an HTTP persistent connection for dynamically generated content. In this case, the `Content-Length` HTTP header cannot be used.
Use `Content-Length` or `Transfer-Encoding: chunked`.
####  `MODULE_NOT_FOUND`[#](https://nodejs.org/docs/latest/api/errors.html#module-not-found)
History Version | Changes
---|---
v12.0.0 | Added `requireStack` property.
A module file could not be resolved by the CommonJS modules loader while attempting a [`require()`](https://nodejs.org/docs/latest/api/modules.html#requireid) operation or when loading the program entry point.
### Legacy Node.js error codes[#](https://nodejs.org/docs/latest/api/errors.html#legacy-nodejs-error-codes)
Stability: 0 - Deprecated. These error codes are either inconsistent, or have been removed.
####  `ERR_CANNOT_TRANSFER_OBJECT`[#](https://nodejs.org/docs/latest/api/errors.html#err-cannot-transfer-object)
Added in: v10.5.0Removed in: v12.5.0
The value passed to `postMessage()` contained an object that is not supported for transferring.
####  `ERR_CPU_USAGE`[#](https://nodejs.org/docs/latest/api/errors.html#err-cpu-usage)
Removed in: v15.0.0
The native call from `process.cpuUsage` could not be processed.
####  `ERR_CRYPTO_HASH_DIGEST_NO_UTF16`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-hash-digest-no-utf16)
Added in: v9.0.0Removed in: v12.12.0
The UTF-16 encoding was used with [`hash.digest()`](https://nodejs.org/docs/latest/api/crypto.html#hashdigestencoding). While the `hash.digest()` method does allow an `encoding` argument to be passed in, causing the method to return a string rather than a `Buffer`, the UTF-16 encoding (e.g. `ucs` or `utf16le`) is not supported.
####  `ERR_CRYPTO_SCRYPT_INVALID_PARAMETER`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-scrypt-invalid-parameter)
Removed in: v23.0.0
An incompatible combination of options was passed to [`crypto.scrypt()`](https://nodejs.org/docs/latest/api/crypto.html#cryptoscryptpassword-salt-keylen-options-callback) or [`crypto.scryptSync()`](https://nodejs.org/docs/latest/api/crypto.html#cryptoscryptsyncpassword-salt-keylen-options). New versions of Node.js use the error code [`ERR_INCOMPATIBLE_OPTION_PAIR`](https://nodejs.org/docs/latest/api/errors.html#err_incompatible_option_pair) instead, which is consistent with other APIs.
####  `ERR_FS_INVALID_SYMLINK_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-invalid-symlink-type)
Removed in: v23.0.0
An invalid symlink type was passed to the [`fs.symlink()`](https://nodejs.org/docs/latest/api/fs.html#fssymlinktarget-path-type-callback) or [`fs.symlinkSync()`](https://nodejs.org/docs/latest/api/fs.html#fssymlinksynctarget-path-type) methods.
####  `ERR_HTTP2_FRAME_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-frame-error)
Added in: v9.0.0Removed in: v10.0.0
Used when a failure occurs sending an individual frame on the HTTP/2 session.
####  `ERR_HTTP2_HEADERS_OBJECT`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-headers-object)
Added in: v9.0.0Removed in: v10.0.0
Used when an HTTP/2 Headers Object is expected.
####  `ERR_HTTP2_HEADER_REQUIRED`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-header-required)
Added in: v9.0.0Removed in: v10.0.0
Used when a required header is missing in an HTTP/2 message.
####  `ERR_HTTP2_INFO_HEADERS_AFTER_RESPOND`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-info-headers-after-respond)
Added in: v9.0.0Removed in: v10.0.0
HTTP/2 informational headers must only be sent _prior_ to calling the `Http2Stream.prototype.respond()` method.
####  `ERR_HTTP2_STREAM_CLOSED`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-stream-closed)
Added in: v9.0.0Removed in: v10.0.0
Used when an action has been performed on an HTTP/2 Stream that has already been closed.
####  `ERR_HTTP_INVALID_CHAR`[#](https://nodejs.org/docs/latest/api/errors.html#err-http-invalid-char)
Added in: v9.0.0Removed in: v10.0.0
Used when an invalid character is found in an HTTP response status message (reason phrase).
####  `ERR_IMPORT_ASSERTION_TYPE_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-import-assertion-type-failed)
Added in: v17.1.0, v16.14.0Removed in: v21.1.0
An import assertion has failed, preventing the specified module to be imported.
####  `ERR_IMPORT_ASSERTION_TYPE_MISSING`[#](https://nodejs.org/docs/latest/api/errors.html#err-import-assertion-type-missing)
Added in: v17.1.0, v16.14.0Removed in: v21.1.0
An import assertion is missing, preventing the specified module to be imported.
####  `ERR_IMPORT_ASSERTION_TYPE_UNSUPPORTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-import-assertion-type-unsupported)
Added in: v17.1.0, v16.14.0Removed in: v21.1.0
An import attribute is not supported by this version of Node.js.
####  `ERR_INDEX_OUT_OF_RANGE`[#](https://nodejs.org/docs/latest/api/errors.html#err-index-out-of-range)
Added in: v10.0.0Removed in: v11.0.0
A given index was out of the accepted range (e.g. negative offsets).
####  `ERR_INVALID_OPT_VALUE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-opt-value)
Added in: v8.0.0Removed in: v15.0.0
An invalid or unexpected value was passed in an options object.
####  `ERR_INVALID_OPT_VALUE_ENCODING`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-opt-value-encoding)
Added in: v9.0.0Removed in: v15.0.0
An invalid or unknown file encoding was passed.
####  `ERR_INVALID_PERFORMANCE_MARK`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-performance-mark)
Added in: v8.5.0Removed in: v16.7.0
While using the Performance Timing API (`perf_hooks`), a performance mark is invalid.
####  `ERR_INVALID_TRANSFER_OBJECT`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-transfer-object)
Removed in: v21.0.0History Version | Changes
---|---
v21.0.0 | A `DOMException` is thrown instead.
An invalid transfer object was passed to `postMessage()`.
####  `ERR_MANIFEST_ASSERT_INTEGRITY`[#](https://nodejs.org/docs/latest/api/errors.html#err-manifest-assert-integrity)
Removed in: v22.2.0
An attempt was made to load a resource, but the resource did not match the integrity defined by the policy manifest. See the documentation for policy manifests for more information.
####  `ERR_MANIFEST_DEPENDENCY_MISSING`[#](https://nodejs.org/docs/latest/api/errors.html#err-manifest-dependency-missing)
Removed in: v22.2.0
An attempt was made to load a resource, but the resource was not listed as a dependency from the location that attempted to load it. See the documentation for policy manifests for more information.
####  `ERR_MANIFEST_INTEGRITY_MISMATCH`[#](https://nodejs.org/docs/latest/api/errors.html#err-manifest-integrity-mismatch)
Removed in: v22.2.0
An attempt was made to load a policy manifest, but the manifest had multiple entries for a resource which did not match each other. Update the manifest entries to match in order to resolve this error. See the documentation for policy manifests for more information.
####  `ERR_MANIFEST_INVALID_RESOURCE_FIELD`[#](https://nodejs.org/docs/latest/api/errors.html#err-manifest-invalid-resource-field)
Removed in: v22.2.0
A policy manifest resource had an invalid value for one of its fields. Update the manifest entry to match in order to resolve this error. See the documentation for policy manifests for more information.
####  `ERR_MANIFEST_INVALID_SPECIFIER`[#](https://nodejs.org/docs/latest/api/errors.html#err-manifest-invalid-specifier)
Removed in: v22.2.0
A policy manifest resource had an invalid value for one of its dependency mappings. Update the manifest entry to match to resolve this error. See the documentation for policy manifests for more information.
####  `ERR_MANIFEST_PARSE_POLICY`[#](https://nodejs.org/docs/latest/api/errors.html#err-manifest-parse-policy)
Removed in: v22.2.0
An attempt was made to load a policy manifest, but the manifest was unable to be parsed. See the documentation for policy manifests for more information.
####  `ERR_MANIFEST_TDZ`[#](https://nodejs.org/docs/latest/api/errors.html#err-manifest-tdz)
Removed in: v22.2.0
An attempt was made to read from a policy manifest, but the manifest initialization has not yet taken place. This is likely a bug in Node.js.
####  `ERR_MANIFEST_UNKNOWN_ONERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-manifest-unknown-onerror)
Removed in: v22.2.0
A policy manifest was loaded, but had an unknown value for its "onerror" behavior. See the documentation for policy manifests for more information.
####  `ERR_MISSING_MESSAGE_PORT_IN_TRANSFER_LIST`[#](https://nodejs.org/docs/latest/api/errors.html#err-missing-message-port-in-transfer-list)
Removed in: v15.0.0
This error code was replaced by [`ERR_MISSING_TRANSFERABLE_IN_TRANSFER_LIST`](https://nodejs.org/docs/latest/api/errors.html#err_missing_transferable_in_transfer_list) in Node.js 15.0.0, because it is no longer accurate as other types of transferable objects also exist now.
####  `ERR_MISSING_TRANSFERABLE_IN_TRANSFER_LIST`[#](https://nodejs.org/docs/latest/api/errors.html#err-missing-transferable-in-transfer-list)
Added in: v15.0.0Removed in: v21.0.0History Version | Changes
---|---
v21.0.0 | A `DOMException` is thrown instead.
An object that needs to be explicitly listed in the `transferList` argument is in the object passed to a [`postMessage()`](https://nodejs.org/docs/latest/api/worker_threads.html#portpostmessagevalue-transferlist) call, but is not provided in the `transferList` for that call. Usually, this is a `MessagePort`.
In Node.js versions prior to v15.0.0, the error code being used here was [`ERR_MISSING_MESSAGE_PORT_IN_TRANSFER_LIST`](https://nodejs.org/docs/latest/api/errors.html#err_missing_message_port_in_transfer_list). However, the set of transferable object types has been expanded to cover more types than `MessagePort`.
####  `ERR_NAPI_CONS_PROTOTYPE_OBJECT`[#](https://nodejs.org/docs/latest/api/errors.html#err-napi-cons-prototype-object)
Added in: v9.0.0Removed in: v10.0.0
Used by the `Node-API` when `Constructor.prototype` is not an object.
####  `ERR_NAPI_TSFN_START_IDLE_LOOP`[#](https://nodejs.org/docs/latest/api/errors.html#err-napi-tsfn-start-idle-loop)
Added in: v10.6.0, v8.16.0Removed in: v14.2.0, v12.17.0
On the main thread, values are removed from the queue associated with the thread-safe function in an idle loop. This error indicates that an error has occurred when attempting to start the loop.
####  `ERR_NAPI_TSFN_STOP_IDLE_LOOP`[#](https://nodejs.org/docs/latest/api/errors.html#err-napi-tsfn-stop-idle-loop)
Added in: v10.6.0, v8.16.0Removed in: v14.2.0, v12.17.0
Once no more items are left in the queue, the idle loop must be suspended. This error indicates that the idle loop has failed to stop.
####  `ERR_NO_LONGER_SUPPORTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-no-longer-supported)
A Node.js API was called in an unsupported manner, such as `Buffer.write(string, encoding, offset[, length])`.
####  `ERR_OUTOFMEMORY`[#](https://nodejs.org/docs/latest/api/errors.html#err-outofmemory)
Added in: v9.0.0Removed in: v10.0.0
Used generically to identify that an operation caused an out of memory condition.
####  `ERR_PARSE_HISTORY_DATA`[#](https://nodejs.org/docs/latest/api/errors.html#err-parse-history-data)
Added in: v9.0.0Removed in: v10.0.0
The `node:repl` module was unable to parse data from the REPL history file.
####  `ERR_SOCKET_CANNOT_SEND`[#](https://nodejs.org/docs/latest/api/errors.html#err-socket-cannot-send)
Added in: v9.0.0Removed in: v14.0.0
Data could not be sent on a socket.
####  `ERR_STDERR_CLOSE`[#](https://nodejs.org/docs/latest/api/errors.html#err-stderr-close)
Removed in: v10.12.0History Version | Changes
---|---
v10.12.0 | Rather than emitting an error, `process.stderr.end()` now only closes the stream side but not the underlying resource, making this error obsolete.
An attempt was made to close the `process.stderr` stream. By design, Node.js does not allow `stdout` or `stderr` streams to be closed by user code.
####  `ERR_STDOUT_CLOSE`[#](https://nodejs.org/docs/latest/api/errors.html#err-stdout-close)
Removed in: v10.12.0History Version | Changes
---|---
v10.12.0 | Rather than emitting an error, `process.stderr.end()` now only closes the stream side but not the underlying resource, making this error obsolete.
An attempt was made to close the `process.stdout` stream. By design, Node.js does not allow `stdout` or `stderr` streams to be closed by user code.
####  `ERR_STREAM_READ_NOT_IMPLEMENTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-stream-read-not-implemented)
Added in: v9.0.0Removed in: v10.0.0
Used when an attempt is made to use a readable stream that has not implemented [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize).
####  `ERR_TAP_LEXER_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-tap-lexer-error)
An error representing a failing lexer state.
####  `ERR_TAP_PARSER_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-tap-parser-error)
An error representing a failing parser state. Additional information about the token causing the error is available via the `cause` property.
####  `ERR_TAP_VALIDATION_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-tap-validation-error)
This error represents a failed TAP validation.
####  `ERR_TLS_RENEGOTIATION_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-tls-renegotiation-failed)
Added in: v9.0.0Removed in: v10.0.0
Used when a TLS renegotiation request has failed in a non-specific way.
####  `ERR_TRANSFERRING_EXTERNALIZED_SHAREDARRAYBUFFER`[#](https://nodejs.org/docs/latest/api/errors.html#err-transferring-externalized-sharedarraybuffer)
Added in: v10.5.0Removed in: v14.0.0
A `SharedArrayBuffer` whose memory is not managed by the JavaScript engine or by Node.js was encountered during serialization. Such a `SharedArrayBuffer` cannot be serialized.
This can only happen when native addons create `SharedArrayBuffer`s in "externalized" mode, or put existing `SharedArrayBuffer` into externalized mode.
####  `ERR_UNKNOWN_STDIN_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-unknown-stdin-type)
Added in: v8.0.0Removed in: v11.7.0
An attempt was made to launch a Node.js process with an unknown `stdin` file type. This error is usually an indication of a bug within Node.js itself, although it is possible for user code to trigger it.
####  `ERR_UNKNOWN_STREAM_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-unknown-stream-type)
Added in: v8.0.0Removed in: v11.7.0
An attempt was made to launch a Node.js process with an unknown `stdout` or `stderr` file type. This error is usually an indication of a bug within Node.js itself, although it is possible for user code to trigger it.
####  `ERR_V8BREAKITERATOR`[#](https://nodejs.org/docs/latest/api/errors.html#err-v8breakiterator)
The V8 `BreakIterator` API was used but the full ICU data set is not installed.
####  `ERR_VALUE_OUT_OF_RANGE`[#](https://nodejs.org/docs/latest/api/errors.html#err-value-out-of-range)
Added in: v9.0.0Removed in: v10.0.0
Used when a given value is out of the accepted range.
####  `ERR_VM_MODULE_LINKING_ERRORED`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-module-linking-errored)
Added in: v10.0.0Removed in: v18.1.0, v16.17.0
The linker function returned a module for which linking has failed.
####  `ERR_VM_MODULE_NOT_LINKED`[#](https://nodejs.org/docs/latest/api/errors.html#err-vm-module-not-linked)
The module must be successfully linked before instantiation.
####  `ERR_WORKER_UNSUPPORTED_EXTENSION`[#](https://nodejs.org/docs/latest/api/errors.html#err-worker-unsupported-extension)
Added in: v11.0.0Removed in: v16.9.0
The pathname used for the main script of a worker has an unknown file extension.
####  `ERR_ZLIB_BINDING_CLOSED`[#](https://nodejs.org/docs/latest/api/errors.html#err-zlib-binding-closed)
Added in: v9.0.0Removed in: v10.0.0
Used when an attempt is made to use a `zlib` object after it has already been closed.
### OpenSSL Error Codes[#](https://nodejs.org/docs/latest/api/errors.html#openssl-error-codes)
#### Time Validity Errors[#](https://nodejs.org/docs/latest/api/errors.html#time-validity-errors)
#####  `CERT_NOT_YET_VALID`[#](https://nodejs.org/docs/latest/api/errors.html#cert-not-yet-valid)
The certificate is not yet valid: the notBefore date is after the current time.
