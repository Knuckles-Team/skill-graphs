An invalid value has been specified for an HTTP/2 setting.
####  `ERR_HTTP2_INVALID_STREAM`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-invalid-stream)
An operation was performed on a stream that had already been destroyed.
####  `ERR_HTTP2_MAX_PENDING_SETTINGS_ACK`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-max-pending-settings-ack)
Whenever an HTTP/2 `SETTINGS` frame is sent to a connected peer, the peer is required to send an acknowledgment that it has received and applied the new `SETTINGS`. By default, a maximum number of unacknowledged `SETTINGS` frames may be sent at any given time. This error code is used when that limit has been reached.
####  `ERR_HTTP2_NESTED_PUSH`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-nested-push)
An attempt was made to initiate a new push stream from within a push stream. Nested push streams are not permitted.
####  `ERR_HTTP2_NO_MEM`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-no-mem)
Out of memory when using the `http2session.setLocalWindowSize(windowSize)` API.
####  `ERR_HTTP2_NO_SOCKET_MANIPULATION`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-no-socket-manipulation)
An attempt was made to directly manipulate (read, write, pause, resume, etc.) a socket attached to an `Http2Session`.
####  `ERR_HTTP2_ORIGIN_LENGTH`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-origin-length)
HTTP/2 `ORIGIN` frames are limited to a length of 16382 bytes.
####  `ERR_HTTP2_OUT_OF_STREAMS`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-out-of-streams)
The number of streams created on a single HTTP/2 session reached the maximum limit.
####  `ERR_HTTP2_PAYLOAD_FORBIDDEN`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-payload-forbidden)
A message payload was specified for an HTTP response code for which a payload is forbidden.
####  `ERR_HTTP2_PING_CANCEL`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-ping-cancel)
An HTTP/2 ping was canceled.
####  `ERR_HTTP2_PING_LENGTH`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-ping-length)
HTTP/2 ping payloads must be exactly 8 bytes in length.
####  `ERR_HTTP2_PSEUDOHEADER_NOT_ALLOWED`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-pseudoheader-not-allowed)
An HTTP/2 pseudo-header has been used inappropriately. Pseudo-headers are header key names that begin with the `:` prefix.
####  `ERR_HTTP2_PUSH_DISABLED`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-push-disabled)
An attempt was made to create a push stream, which had been disabled by the client.
####  `ERR_HTTP2_SEND_FILE`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-send-file)
An attempt was made to use the `Http2Stream.prototype.responseWithFile()` API to send a directory.
####  `ERR_HTTP2_SEND_FILE_NOSEEK`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-send-file-noseek)
An attempt was made to use the `Http2Stream.prototype.responseWithFile()` API to send something other than a regular file, but `offset` or `length` options were provided.
####  `ERR_HTTP2_SESSION_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-session-error)
The `Http2Session` closed with a non-zero error code.
####  `ERR_HTTP2_SETTINGS_CANCEL`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-settings-cancel)
The `Http2Session` settings canceled.
####  `ERR_HTTP2_SOCKET_BOUND`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-socket-bound)
An attempt was made to connect a `Http2Session` object to a `net.Socket` or `tls.TLSSocket` that had already been bound to another `Http2Session` object.
####  `ERR_HTTP2_SOCKET_UNBOUND`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-socket-unbound)
An attempt was made to use the `socket` property of an `Http2Session` that has already been closed.
####  `ERR_HTTP2_STATUS_101`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-status-101)
Use of the `101` Informational status code is forbidden in HTTP/2.
####  `ERR_HTTP2_STATUS_INVALID`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-status-invalid)
An invalid HTTP status code has been specified. Status codes must be an integer between `100` and `599` (inclusive).
####  `ERR_HTTP2_STREAM_CANCEL`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-stream-cancel)
An `Http2Stream` was destroyed before any data was transmitted to the connected peer.
####  `ERR_HTTP2_STREAM_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-stream-error)
A non-zero error code was been specified in an `RST_STREAM` frame.
####  `ERR_HTTP2_STREAM_SELF_DEPENDENCY`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-stream-self-dependency)
When setting the priority for an HTTP/2 stream, the stream may be marked as a dependency for a parent stream. This error code is used when an attempt is made to mark a stream and dependent of itself.
####  `ERR_HTTP2_TOO_MANY_CUSTOM_SETTINGS`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-too-many-custom-settings)
The number of supported custom settings (10) has been exceeded.
####  `ERR_HTTP2_TOO_MANY_INVALID_FRAMES`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-too-many-invalid-frames)
Added in: v15.14.0
The limit of acceptable invalid HTTP/2 protocol frames sent by the peer, as specified through the `maxSessionInvalidFrames` option, has been exceeded.
####  `ERR_HTTP2_TRAILERS_ALREADY_SENT`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-trailers-already-sent)
Trailing headers have already been sent on the `Http2Stream`.
####  `ERR_HTTP2_TRAILERS_NOT_READY`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-trailers-not-ready)
The `http2stream.sendTrailers()` method cannot be called until after the `'wantTrailers'` event is emitted on an `Http2Stream` object. The `'wantTrailers'` event will only be emitted if the `waitForTrailers` option is set for the `Http2Stream`.
####  `ERR_HTTP2_UNSUPPORTED_PROTOCOL`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-unsupported-protocol)
`http2.connect()` was passed a URL that uses any protocol other than `http:` or `https:`.
####  `ERR_HTTP_BODY_NOT_ALLOWED`[#](https://nodejs.org/docs/latest/api/errors.html#err-http-body-not-allowed)
An error is thrown when writing to an HTTP response which does not allow contents.
####  `ERR_HTTP_CONTENT_LENGTH_MISMATCH`[#](https://nodejs.org/docs/latest/api/errors.html#err-http-content-length-mismatch)
Response body size doesn't match with the specified content-length header value.
####  `ERR_HTTP_HEADERS_SENT`[#](https://nodejs.org/docs/latest/api/errors.html#err-http-headers-sent)
An attempt was made to add more headers after the headers had already been sent.
####  `ERR_HTTP_INVALID_HEADER_VALUE`[#](https://nodejs.org/docs/latest/api/errors.html#err-http-invalid-header-value)
An invalid HTTP header value was specified.
####  `ERR_HTTP_INVALID_STATUS_CODE`[#](https://nodejs.org/docs/latest/api/errors.html#err-http-invalid-status-code)
Status code was outside the regular status code range (100-999).
####  `ERR_HTTP_REQUEST_TIMEOUT`[#](https://nodejs.org/docs/latest/api/errors.html#err-http-request-timeout)
The client has not sent the entire request within the allowed time.
####  `ERR_HTTP_SOCKET_ASSIGNED`[#](https://nodejs.org/docs/latest/api/errors.html#err-http-socket-assigned)
The given [`ServerResponse`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse) was already assigned a socket.
####  `ERR_HTTP_SOCKET_ENCODING`[#](https://nodejs.org/docs/latest/api/errors.html#err-http-socket-encoding)
Changing the socket encoding is not allowed per
####  `ERR_HTTP_TRAILER_INVALID`[#](https://nodejs.org/docs/latest/api/errors.html#err-http-trailer-invalid)
The `Trailer` header was set even though the transfer encoding does not support that.
####  `ERR_ILLEGAL_CONSTRUCTOR`[#](https://nodejs.org/docs/latest/api/errors.html#err-illegal-constructor)
An attempt was made to construct an object using a non-public constructor.
####  `ERR_IMPORT_ATTRIBUTE_MISSING`[#](https://nodejs.org/docs/latest/api/errors.html#err-import-attribute-missing)
Added in: v21.1.0
An import attribute is missing, preventing the specified module to be imported.
####  `ERR_IMPORT_ATTRIBUTE_TYPE_INCOMPATIBLE`[#](https://nodejs.org/docs/latest/api/errors.html#err-import-attribute-type-incompatible)
Added in: v21.1.0
An import `type` attribute was provided, but the specified module is of a different type.
####  `ERR_IMPORT_ATTRIBUTE_UNSUPPORTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-import-attribute-unsupported)
Added in: v21.0.0, v20.10.0, v18.19.0
An import attribute is not supported by this version of Node.js.
####  `ERR_INCOMPATIBLE_OPTION_PAIR`[#](https://nodejs.org/docs/latest/api/errors.html#err-incompatible-option-pair)
An option pair is incompatible with each other and cannot be used at the same time.
####  `ERR_INPUT_TYPE_NOT_ALLOWED`[#](https://nodejs.org/docs/latest/api/errors.html#err-input-type-not-allowed)
The `--input-type` flag was used to attempt to execute a file. This flag can only be used with input via `--eval`, `--print`, or `STDIN`.
####  `ERR_INSPECTOR_ALREADY_ACTIVATED`[#](https://nodejs.org/docs/latest/api/errors.html#err-inspector-already-activated)
While using the `node:inspector` module, an attempt was made to activate the inspector when it already started to listen on a port. Use `inspector.close()` before activating it on a different address.
####  `ERR_INSPECTOR_ALREADY_CONNECTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-inspector-already-connected)
While using the `node:inspector` module, an attempt was made to connect when the inspector was already connected.
####  `ERR_INSPECTOR_CLOSED`[#](https://nodejs.org/docs/latest/api/errors.html#err-inspector-closed)
While using the `node:inspector` module, an attempt was made to use the inspector after the session had already closed.
####  `ERR_INSPECTOR_COMMAND`[#](https://nodejs.org/docs/latest/api/errors.html#err-inspector-command)
An error occurred while issuing a command via the `node:inspector` module.
####  `ERR_INSPECTOR_NOT_ACTIVE`[#](https://nodejs.org/docs/latest/api/errors.html#err-inspector-not-active)
The `inspector` is not active when `inspector.waitForDebugger()` is called.
####  `ERR_INSPECTOR_NOT_AVAILABLE`[#](https://nodejs.org/docs/latest/api/errors.html#err-inspector-not-available)
The `node:inspector` module is not available for use.
####  `ERR_INSPECTOR_NOT_CONNECTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-inspector-not-connected)
While using the `node:inspector` module, an attempt was made to use the inspector before it was connected.
####  `ERR_INSPECTOR_NOT_WORKER`[#](https://nodejs.org/docs/latest/api/errors.html#err-inspector-not-worker)
An API was called on the main thread that can only be used from the worker thread.
####  `ERR_INTERNAL_ASSERTION`[#](https://nodejs.org/docs/latest/api/errors.html#err-internal-assertion)
There was a bug in Node.js or incorrect usage of Node.js internals. To fix the error, open an issue at
####  `ERR_INVALID_ADDRESS`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-address)
The provided address is not understood by the Node.js API.
####  `ERR_INVALID_ADDRESS_FAMILY`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-address-family)
The provided address family is not understood by the Node.js API.
####  `ERR_INVALID_ARG_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-arg-type)
An argument of the wrong type was passed to a Node.js API.
####  `ERR_INVALID_ARG_VALUE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-arg-value)
An invalid or unsupported value was passed for a given argument.
####  `ERR_INVALID_ASYNC_ID`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-async-id)
An invalid `asyncId` or `triggerAsyncId` was passed using `AsyncHooks`. An id less than -1 should never happen.
####  `ERR_INVALID_BUFFER_SIZE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-buffer-size)
A swap was performed on a `Buffer` but its size was not compatible with the operation.
####  `ERR_INVALID_CHAR`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-char)
Invalid characters were detected in headers.
####  `ERR_INVALID_CURSOR_POS`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-cursor-pos)
A cursor on a given stream cannot be moved to a specified row without a specified column.
####  `ERR_INVALID_FD`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-fd)
A file descriptor ('fd') was not valid (e.g. it was a negative value).
####  `ERR_INVALID_FD_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-fd-type)
A file descriptor ('fd') type was not valid.
####  `ERR_INVALID_FILE_URL_HOST`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-file-url-host)
A Node.js API that consumes `file:` URLs (such as certain functions in the [`fs`](https://nodejs.org/docs/latest/api/fs.html) module) encountered a file URL with an incompatible host. This situation can only occur on Unix-like systems where only `localhost` or an empty host is supported.
####  `ERR_INVALID_FILE_URL_PATH`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-file-url-path)
A Node.js API that consumes `file:` URLs (such as certain functions in the [`fs`](https://nodejs.org/docs/latest/api/fs.html) module) encountered a file URL with an incompatible path. The exact semantics for determining whether a path can be used is platform-dependent.
The thrown error object includes an `input` property that contains the URL object of the invalid `file:` URL.
####  `ERR_INVALID_HANDLE_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-handle-type)
An attempt was made to send an unsupported "handle" over an IPC communication channel to a child process. See [`subprocess.send()`](https://nodejs.org/docs/latest/api/child_process.html#subprocesssendmessage-sendhandle-options-callback) and [`process.send()`](https://nodejs.org/docs/latest/api/process.html#processsendmessage-sendhandle-options-callback) for more information.
####  `ERR_INVALID_HTTP_TOKEN`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-http-token)
An invalid HTTP token was supplied.
####  `ERR_INVALID_IP_ADDRESS`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-ip-address)
An IP address is not valid.
####  `ERR_INVALID_MIME_SYNTAX`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-mime-syntax)
The syntax of a MIME is not valid.
####  `ERR_INVALID_MODULE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-module)
Added in: v15.0.0, v14.18.0
An attempt was made to load a module that does not exist or was otherwise not valid.
####  `ERR_INVALID_MODULE_SPECIFIER`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-module-specifier)
The imported module string is an invalid URL, package name, or package subpath specifier.
####  `ERR_INVALID_OBJECT_DEFINE_PROPERTY`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-object-define-property)
An error occurred while setting an invalid attribute on the property of an object.
####  `ERR_INVALID_PACKAGE_CONFIG`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-package-config)
An invalid [`package.json`](https://nodejs.org/docs/latest/api/packages.html#nodejs-packagejson-field-definitions) file failed parsing.
####  `ERR_INVALID_PACKAGE_TARGET`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-package-target)
The `package.json` [`"exports"`](https://nodejs.org/docs/latest/api/packages.html#exports) field contains an invalid target mapping value for the attempted module resolution.
####  `ERR_INVALID_PROTOCOL`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-protocol)
An invalid `options.protocol` was passed to `http.request()`.
####  `ERR_INVALID_REPL_EVAL_CONFIG`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-repl-eval-config)
Both `breakEvalOnSigint` and `eval` options were set in the [`REPL`](https://nodejs.org/docs/latest/api/repl.html) config, which is not supported.
####  `ERR_INVALID_REPL_INPUT`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-repl-input)
The input may not be used in the [`REPL`](https://nodejs.org/docs/latest/api/repl.html). The conditions under which this error is used are described in the [`REPL`](https://nodejs.org/docs/latest/api/repl.html) documentation.
####  `ERR_INVALID_RETURN_PROPERTY`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-return-property)
Thrown in case a function option does not provide a valid value for one of its returned object properties on execution.
####  `ERR_INVALID_RETURN_PROPERTY_VALUE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-return-property-value)
Thrown in case a function option does not provide an expected value type for one of its returned object properties on execution.
####  `ERR_INVALID_RETURN_VALUE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-return-value)
Thrown in case a function option does not return an expected value type on execution, such as when a function is expected to return a promise.
####  `ERR_INVALID_STATE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-state)
Added in: v15.0.0
Indicates that an operation cannot be completed due to an invalid state. For instance, an object may have already been destroyed, or may be performing another operation.
####  `ERR_INVALID_SYNC_FORK_INPUT`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-sync-fork-input)
A `Buffer`, `TypedArray`, `DataView`, or `string` was provided as stdio input to an asynchronous fork. See the documentation for the [`child_process`](https://nodejs.org/docs/latest/api/child_process.html) module for more information.
####  `ERR_INVALID_THIS`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-this)
A Node.js API function was called with an incompatible `this` value.
```
const urlSearchParams = new URLSearchParams('foo=bar&baz=new');

const buf = Buffer.alloc(1);
urlSearchParams.has.call(buf, 'foo');
// Throws a TypeError with code 'ERR_INVALID_THIS'
copy
```

####  `ERR_INVALID_TUPLE`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-tuple)
An element in the `iterable` provided to the [WHATWG](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) [`URLSearchParams` constructor](https://nodejs.org/docs/latest/api/url.html#new-urlsearchparamsiterable) did not represent a `[name, value]` tuple – that is, if an element is not iterable, or does not consist of exactly two elements.
####  `ERR_INVALID_TYPESCRIPT_SYNTAX`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-typescript-syntax)
Added in: v23.0.0, v22.10.0History Version | Changes
---|---
v23.7.0, v22.14.0 | This error is no longer thrown on valid yet unsupported syntax.
The provided TypeScript syntax is not valid.
####  `ERR_INVALID_URI`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-uri)
An invalid URI was passed.
####  `ERR_INVALID_URL`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-url)
An invalid URL was passed to the [WHATWG](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) [`URL` constructor](https://nodejs.org/docs/latest/api/url.html#new-urlinput-base) or the legacy [`url.parse()`](https://nodejs.org/docs/latest/api/url.html#urlparseurlstring-parsequerystring-slashesdenotehost) to be parsed. The thrown error object typically has an additional property `'input'` that contains the URL that failed to parse.
####  `ERR_INVALID_URL_PATTERN`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-url-pattern)
An invalid URLPattern was passed to the [WHATWG](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) [`URLPattern` constructor](https://nodejs.org/docs/latest/api/url.html#new-urlpatternstring-baseurl-options) to be parsed.
####  `ERR_INVALID_URL_SCHEME`[#](https://nodejs.org/docs/latest/api/errors.html#err-invalid-url-scheme)
An attempt was made to use a URL of an incompatible scheme (protocol) for a specific purpose. It is only used in the [WHATWG URL API](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) support in the [`fs`](https://nodejs.org/docs/latest/api/fs.html) module (which only accepts URLs with `'file'` scheme), but may be used in other Node.js APIs as well in the future.
####  `ERR_IPC_CHANNEL_CLOSED`[#](https://nodejs.org/docs/latest/api/errors.html#err-ipc-channel-closed)
An attempt was made to use an IPC communication channel that was already closed.
####  `ERR_IPC_DISCONNECTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-ipc-disconnected)
An attempt was made to disconnect an IPC communication channel that was already disconnected. See the documentation for the [`child_process`](https://nodejs.org/docs/latest/api/child_process.html) module for more information.
####  `ERR_IPC_ONE_PIPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-ipc-one-pipe)
An attempt was made to create a child Node.js process using more than one IPC communication channel. See the documentation for the [`child_process`](https://nodejs.org/docs/latest/api/child_process.html) module for more information.
####  `ERR_IPC_SYNC_FORK`[#](https://nodejs.org/docs/latest/api/errors.html#err-ipc-sync-fork)
An attempt was made to open an IPC communication channel with a synchronously forked Node.js process. See the documentation for the [`child_process`](https://nodejs.org/docs/latest/api/child_process.html) module for more information.
####  `ERR_IP_BLOCKED`[#](https://nodejs.org/docs/latest/api/errors.html#err-ip-blocked)
IP is blocked by `net.BlockList`.
####  `ERR_LOADER_CHAIN_INCOMPLETE`[#](https://nodejs.org/docs/latest/api/errors.html#err-loader-chain-incomplete)
Added in: v18.6.0, v16.17.0
An ESM loader hook returned without calling `next()` and without explicitly signaling a short circuit.
####  `ERR_LOAD_SQLITE_EXTENSION`[#](https://nodejs.org/docs/latest/api/errors.html#err-load-sqlite-extension)
Added in: v23.5.0, v22.13.0
An error occurred while loading a SQLite extension.
####  `ERR_MEMORY_ALLOCATION_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-memory-allocation-failed)
An attempt was made to allocate memory (usually in the C++ layer) but it failed.
####  `ERR_MESSAGE_TARGET_CONTEXT_UNAVAILABLE`[#](https://nodejs.org/docs/latest/api/errors.html#err-message-target-context-unavailable)
Added in: v14.5.0, v12.19.0
A message posted to a [`MessagePort`](https://nodejs.org/docs/latest/api/worker_threads.html#class-messageport) could not be deserialized in the target [vm](https://nodejs.org/docs/latest/api/vm.html) `Context`. Not all Node.js objects can be successfully instantiated in any context at this time, and attempting to transfer them using `postMessage()` can fail on the receiving side in that case.
####  `ERR_METHOD_NOT_IMPLEMENTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-method-not-implemented)
A method is required but not implemented.
####  `ERR_MISSING_ARGS`[#](https://nodejs.org/docs/latest/api/errors.html#err-missing-args)
A required argument of a Node.js API was not passed. This is only used for strict compliance with the API specification (which in some cases may accept `func(undefined)` but not `func()`). In most native Node.js APIs, `func(undefined)` and `func()` are treated identically, and the [`ERR_INVALID_ARG_TYPE`](https://nodejs.org/docs/latest/api/errors.html#err_invalid_arg_type) error code may be used instead.
####  `ERR_MISSING_OPTION`[#](https://nodejs.org/docs/latest/api/errors.html#err-missing-option)
For APIs that accept options objects, some options might be mandatory. This code is thrown if a required option is missing.
####  `ERR_MISSING_PASSPHRASE`[#](https://nodejs.org/docs/latest/api/errors.html#err-missing-passphrase)
An attempt was made to read an encrypted key without specifying a passphrase.
####  `ERR_MISSING_PLATFORM_FOR_WORKER`[#](https://nodejs.org/docs/latest/api/errors.html#err-missing-platform-for-worker)
The V8 platform used by this instance of Node.js does not support creating Workers. This is caused by lack of embedder support for Workers. In particular, this error will not occur with standard builds of Node.js.
####  `ERR_MODULE_LINK_MISMATCH`[#](https://nodejs.org/docs/latest/api/errors.html#err-module-link-mismatch)
A module can not be linked because the same module requests in it are not resolved to the same module.
####  `ERR_MODULE_NOT_FOUND`[#](https://nodejs.org/docs/latest/api/errors.html#err-module-not-found)
A module file could not be resolved by the ECMAScript modules loader while attempting an `import` operation or when loading the program entry point.
####  `ERR_MULTIPLE_CALLBACK`[#](https://nodejs.org/docs/latest/api/errors.html#err-multiple-callback)
A callback was called more than once.
A callback is almost always meant to only be called once as the query can either be fulfilled or rejected but not both at the same time. The latter would be possible by calling a callback more than once.
####  `ERR_NAPI_CONS_FUNCTION`[#](https://nodejs.org/docs/latest/api/errors.html#err-napi-cons-function)
While using `Node-API`, a constructor passed was not a function.
####  `ERR_NAPI_INVALID_DATAVIEW_ARGS`[#](https://nodejs.org/docs/latest/api/errors.html#err-napi-invalid-dataview-args)
While calling `napi_create_dataview()`, a given `offset` was outside the bounds of the dataview or `offset + length` was larger than a length of given `buffer`.
