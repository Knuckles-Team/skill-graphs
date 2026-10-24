####  `ERR_AMBIGUOUS_ARGUMENT`[#](https://nodejs.org/docs/latest/api/errors.html#err-ambiguous-argument)
A function argument is being used in a way that suggests that the function signature may be misunderstood. This is thrown by the `node:assert` module when the `message` parameter in `assert.throws(block, message)` matches the error message thrown by `block` because that usage suggests that the user believes `message` is the expected message rather than the message the `AssertionError` will display if `block` does not throw.
####  `ERR_ARG_NOT_ITERABLE`[#](https://nodejs.org/docs/latest/api/errors.html#err-arg-not-iterable)
An iterable argument (i.e. a value that works with `for...of` loops) was required, but not provided to a Node.js API.
####  `ERR_ASSERTION`[#](https://nodejs.org/docs/latest/api/errors.html#err-assertion)
A special type of error that can be triggered whenever Node.js detects an exceptional logic violation that should never occur. These are raised typically by the `node:assert` module.
####  `ERR_ASYNC_CALLBACK`[#](https://nodejs.org/docs/latest/api/errors.html#err-async-callback)
An attempt was made to register something that is not a function as an `AsyncHooks` callback.
####  `ERR_ASYNC_LOADER_REQUEST_NEVER_SETTLED`[#](https://nodejs.org/docs/latest/api/errors.html#err-async-loader-request-never-settled)
An operation related to module loading is customized by an asynchronous loader hook that never settled the promise before the loader thread exits.
####  `ERR_ASYNC_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-async-type)
The type of an asynchronous resource was invalid. Users are also able to define their own types if using the public embedder API.
####  `ERR_BROTLI_COMPRESSION_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-brotli-compression-failed)
Data passed to a Brotli stream was not successfully compressed.
####  `ERR_BROTLI_INVALID_PARAM`[#](https://nodejs.org/docs/latest/api/errors.html#err-brotli-invalid-param)
An invalid parameter key was passed during construction of a Brotli stream.
####  `ERR_BUFFER_CONTEXT_NOT_AVAILABLE`[#](https://nodejs.org/docs/latest/api/errors.html#err-buffer-context-not-available)
An attempt was made to create a Node.js `Buffer` instance from addon or embedder code, while in a JS engine Context that is not associated with a Node.js instance. The data passed to the `Buffer` method will have been released by the time the method returns.
When encountering this error, a possible alternative to creating a `Buffer` instance is to create a normal `Uint8Array`, which only differs in the prototype of the resulting object. `Uint8Array`s are generally accepted in all Node.js core APIs where `Buffer`s are; they are available in all Contexts.
####  `ERR_BUFFER_OUT_OF_BOUNDS`[#](https://nodejs.org/docs/latest/api/errors.html#err-buffer-out-of-bounds)
An operation outside the bounds of a `Buffer` was attempted.
####  `ERR_BUFFER_TOO_LARGE`[#](https://nodejs.org/docs/latest/api/errors.html#err-buffer-too-large)
An attempt has been made to create a `Buffer` larger than the maximum allowed size.
####  `ERR_CANNOT_WATCH_SIGINT`[#](https://nodejs.org/docs/latest/api/errors.html#err-cannot-watch-sigint)
Node.js was unable to watch for the `SIGINT` signal.
####  `ERR_CHILD_CLOSED_BEFORE_REPLY`[#](https://nodejs.org/docs/latest/api/errors.html#err-child-closed-before-reply)
A child process was closed before the parent received a reply.
####  `ERR_CHILD_PROCESS_IPC_REQUIRED`[#](https://nodejs.org/docs/latest/api/errors.html#err-child-process-ipc-required)
Used when a child process is being forked without specifying an IPC channel.
####  `ERR_CHILD_PROCESS_STDIO_MAXBUFFER`[#](https://nodejs.org/docs/latest/api/errors.html#err-child-process-stdio-maxbuffer)
Used when the main process is trying to read data from the child process's STDERR/STDOUT, and the data's length is longer than the `maxBuffer` option.
####  `ERR_CLOSED_MESSAGE_PORT`[#](https://nodejs.org/docs/latest/api/errors.html#err-closed-message-port)
Added in: v10.5.0History Version | Changes
---|---
v16.2.0, v14.17.1 | The error message was reintroduced.
v11.12.0 | The error message was removed.
There was an attempt to use a `MessagePort` instance in a closed state, usually after `.close()` has been called.
####  `ERR_CONSOLE_WRITABLE_STREAM`[#](https://nodejs.org/docs/latest/api/errors.html#err-console-writable-stream)
`Console` was instantiated without `stdout` stream, or `Console` has a non-writable `stdout` or `stderr` stream.
####  `ERR_CONSTRUCT_CALL_INVALID`[#](https://nodejs.org/docs/latest/api/errors.html#err-construct-call-invalid)
Added in: v12.5.0
A class constructor was called that is not callable.
####  `ERR_CONSTRUCT_CALL_REQUIRED`[#](https://nodejs.org/docs/latest/api/errors.html#err-construct-call-required)
A constructor for a class was called without `new`.
####  `ERR_CONTEXT_NOT_INITIALIZED`[#](https://nodejs.org/docs/latest/api/errors.html#err-context-not-initialized)
The vm context passed into the API is not yet initialized. This could happen when an error occurs (and is caught) during the creation of the context, for example, when the allocation fails or the maximum call stack size is reached when the context is created.
####  `ERR_CPU_PROFILE_ALREADY_STARTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-cpu-profile-already-started)
Added in: v24.8.0, v22.20.0
The CPU profile with the given name is already started.
####  `ERR_CPU_PROFILE_NOT_STARTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-cpu-profile-not-started)
Added in: v24.8.0, v22.20.0
The CPU profile with the given name is not started.
####  `ERR_CPU_PROFILE_TOO_MANY`[#](https://nodejs.org/docs/latest/api/errors.html#err-cpu-profile-too-many)
Added in: v24.8.0, v22.20.0
There are too many CPU profiles being collected.
####  `ERR_CRYPTO_ARGON2_NOT_SUPPORTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-argon2-not-supported)
Argon2 is not supported by the current version of OpenSSL being used.
####  `ERR_CRYPTO_CUSTOM_ENGINE_NOT_SUPPORTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-custom-engine-not-supported)
An OpenSSL engine was requested (for example, through the `clientCertEngine` or `privateKeyEngine` TLS options) that is not supported by the version of OpenSSL being used, likely due to the compile-time flag `OPENSSL_NO_ENGINE`.
####  `ERR_CRYPTO_ECDH_INVALID_FORMAT`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-ecdh-invalid-format)
An invalid value for the `format` argument was passed to the `crypto.ECDH()` class `getPublicKey()` method.
####  `ERR_CRYPTO_ECDH_INVALID_PUBLIC_KEY`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-ecdh-invalid-public-key)
An invalid value for the `key` argument has been passed to the `crypto.ECDH()` class `computeSecret()` method. It means that the public key lies outside of the elliptic curve.
####  `ERR_CRYPTO_ENGINE_UNKNOWN`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-engine-unknown)
An invalid crypto engine identifier was passed to [`require('node:crypto').setEngine()`](https://nodejs.org/docs/latest/api/crypto.html#cryptosetengineengine-flags).
####  `ERR_CRYPTO_FIPS_FORCED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-fips-forced)
The [`--force-fips`](https://nodejs.org/docs/latest/api/cli.html#--force-fips) command-line argument was used but there was an attempt to enable or disable FIPS mode in the `node:crypto` module.
####  `ERR_CRYPTO_FIPS_UNAVAILABLE`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-fips-unavailable)
An attempt was made to enable or disable FIPS mode, but FIPS mode was not available.
####  `ERR_CRYPTO_HASH_FINALIZED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-hash-finalized)
[`hash.digest()`](https://nodejs.org/docs/latest/api/crypto.html#hashdigestencoding) was called multiple times. The `hash.digest()` method must be called no more than one time per instance of a `Hash` object.
####  `ERR_CRYPTO_HASH_UPDATE_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-hash-update-failed)
[`hash.update()`](https://nodejs.org/docs/latest/api/crypto.html#hashupdatedata-inputencoding) failed for any reason. This should rarely, if ever, happen.
####  `ERR_CRYPTO_INCOMPATIBLE_KEY`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-incompatible-key)
The given crypto keys are incompatible with the attempted operation.
####  `ERR_CRYPTO_INCOMPATIBLE_KEY_OPTIONS`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-incompatible-key-options)
The selected public or private key encoding is incompatible with other options.
####  `ERR_CRYPTO_INITIALIZATION_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-initialization-failed)
Added in: v15.0.0
Initialization of the crypto subsystem failed.
####  `ERR_CRYPTO_INVALID_AUTH_TAG`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-auth-tag)
Added in: v15.0.0
An invalid authentication tag was provided.
####  `ERR_CRYPTO_INVALID_COUNTER`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-counter)
Added in: v15.0.0
An invalid counter was provided for a counter-mode cipher.
####  `ERR_CRYPTO_INVALID_CURVE`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-curve)
Added in: v15.0.0
An invalid elliptic-curve was provided.
####  `ERR_CRYPTO_INVALID_DIGEST`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-digest)
An invalid [crypto digest algorithm](https://nodejs.org/docs/latest/api/crypto.html#cryptogethashes) was specified.
####  `ERR_CRYPTO_INVALID_IV`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-iv)
Added in: v15.0.0
An invalid initialization vector was provided.
####  `ERR_CRYPTO_INVALID_JWK`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-jwk)
Added in: v15.0.0
An invalid JSON Web Key was provided.
####  `ERR_CRYPTO_INVALID_KEYLEN`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-keylen)
Added in: v15.0.0
An invalid key length was provided.
####  `ERR_CRYPTO_INVALID_KEYPAIR`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-keypair)
Added in: v15.0.0
An invalid key pair was provided.
####  `ERR_CRYPTO_INVALID_KEYTYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-keytype)
Added in: v15.0.0
An invalid key type was provided.
####  `ERR_CRYPTO_INVALID_KEY_OBJECT_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-key-object-type)
The given crypto key object's type is invalid for the attempted operation.
####  `ERR_CRYPTO_INVALID_MESSAGELEN`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-messagelen)
Added in: v15.0.0
An invalid message length was provided.
####  `ERR_CRYPTO_INVALID_SCRYPT_PARAMS`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-scrypt-params)
Added in: v15.0.0
One or more [`crypto.scrypt()`](https://nodejs.org/docs/latest/api/crypto.html#cryptoscryptpassword-salt-keylen-options-callback) or [`crypto.scryptSync()`](https://nodejs.org/docs/latest/api/crypto.html#cryptoscryptsyncpassword-salt-keylen-options) parameters are outside their legal range.
####  `ERR_CRYPTO_INVALID_STATE`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-state)
A crypto method was used on an object that was in an invalid state. For instance, calling [`cipher.getAuthTag()`](https://nodejs.org/docs/latest/api/crypto.html#ciphergetauthtag) before calling `cipher.final()`.
####  `ERR_CRYPTO_INVALID_TAG_LENGTH`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-invalid-tag-length)
Added in: v15.0.0
An invalid authentication tag length was provided.
####  `ERR_CRYPTO_JOB_INIT_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-job-init-failed)
Added in: v15.0.0
Initialization of an asynchronous crypto operation failed.
####  `ERR_CRYPTO_JWK_UNSUPPORTED_CURVE`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-jwk-unsupported-curve)
Key's Elliptic Curve is not registered for use in the
####  `ERR_CRYPTO_JWK_UNSUPPORTED_KEY_TYPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-jwk-unsupported-key-type)
Key's Asymmetric Key Type is not registered for use in the
####  `ERR_CRYPTO_KEM_NOT_SUPPORTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-kem-not-supported)
Added in: v24.7.0
Attempted to use KEM operations while Node.js was not compiled with OpenSSL with KEM support.
####  `ERR_CRYPTO_OPERATION_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-operation-failed)
Added in: v15.0.0
A crypto operation failed for an otherwise unspecified reason.
####  `ERR_CRYPTO_PBKDF2_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-pbkdf2-error)
The PBKDF2 algorithm failed for unspecified reasons. OpenSSL does not provide more details and therefore neither does Node.js.
####  `ERR_CRYPTO_SCRYPT_NOT_SUPPORTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-scrypt-not-supported)
Node.js was compiled without `scrypt` support. Not possible with the official release binaries but can happen with custom builds, including distro builds.
####  `ERR_CRYPTO_SIGN_KEY_REQUIRED`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-sign-key-required)
A signing `key` was not provided to the [`sign.sign()`](https://nodejs.org/docs/latest/api/crypto.html#signsignprivatekey-outputencoding) method.
####  `ERR_CRYPTO_TIMING_SAFE_EQUAL_LENGTH`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-timing-safe-equal-length)
[`crypto.timingSafeEqual()`](https://nodejs.org/docs/latest/api/crypto.html#cryptotimingsafeequala-b) was called with `Buffer`, `TypedArray`, or `DataView` arguments of different lengths.
####  `ERR_CRYPTO_UNKNOWN_CIPHER`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-unknown-cipher)
An unknown cipher was specified.
####  `ERR_CRYPTO_UNKNOWN_DH_GROUP`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-unknown-dh-group)
An unknown Diffie-Hellman group name was given. See [`crypto.getDiffieHellman()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogetdiffiehellmangroupname) for a list of valid group names.
####  `ERR_CRYPTO_UNSUPPORTED_OPERATION`[#](https://nodejs.org/docs/latest/api/errors.html#err-crypto-unsupported-operation)
Added in: v15.0.0, v14.18.0
An attempt to invoke an unsupported crypto operation was made.
####  `ERR_DEBUGGER_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-debugger-error)
Added in: v16.4.0, v14.17.4
An error occurred with the [debugger](https://nodejs.org/docs/latest/api/debugger.html).
####  `ERR_DEBUGGER_STARTUP_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-debugger-startup-error)
Added in: v16.4.0, v14.17.4
The [debugger](https://nodejs.org/docs/latest/api/debugger.html) timed out waiting for the required host/port to be free.
####  `ERR_DIR_CLOSED`[#](https://nodejs.org/docs/latest/api/errors.html#err-dir-closed)
The [`fs.Dir`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir) was previously closed.
####  `ERR_DIR_CONCURRENT_OPERATION`[#](https://nodejs.org/docs/latest/api/errors.html#err-dir-concurrent-operation)
Added in: v14.3.0
A synchronous read or close call was attempted on an [`fs.Dir`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir) which has ongoing asynchronous operations.
####  `ERR_DLOPEN_DISABLED`[#](https://nodejs.org/docs/latest/api/errors.html#err-dlopen-disabled)
Added in: v16.10.0, v14.19.0
Loading native addons has been disabled using [`--no-addons`](https://nodejs.org/docs/latest/api/cli.html#--no-addons).
####  `ERR_DLOPEN_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-dlopen-failed)
Added in: v15.0.0
A call to `process.dlopen()` failed.
####  `ERR_DNS_SET_SERVERS_FAILED`[#](https://nodejs.org/docs/latest/api/errors.html#err-dns-set-servers-failed)
`c-ares` failed to set the DNS server.
####  `ERR_DOMAIN_CALLBACK_NOT_AVAILABLE`[#](https://nodejs.org/docs/latest/api/errors.html#err-domain-callback-not-available)
The `node:domain` module was not usable since it could not establish the required error handling hooks, because [`process.setUncaughtExceptionCaptureCallback()`](https://nodejs.org/docs/latest/api/process.html#processsetuncaughtexceptioncapturecallbackfn) had been called at an earlier point in time.
####  `ERR_DOMAIN_CANNOT_SET_UNCAUGHT_EXCEPTION_CAPTURE`[#](https://nodejs.org/docs/latest/api/errors.html#err-domain-cannot-set-uncaught-exception-capture)
[`process.setUncaughtExceptionCaptureCallback()`](https://nodejs.org/docs/latest/api/process.html#processsetuncaughtexceptioncapturecallbackfn) could not be called because the `node:domain` module has been loaded at an earlier point in time.
The stack trace is extended to include the point in time at which the `node:domain` module had been loaded.
####  `ERR_DUPLICATE_STARTUP_SNAPSHOT_MAIN_FUNCTION`[#](https://nodejs.org/docs/latest/api/errors.html#err-duplicate-startup-snapshot-main-function)
[`v8.startupSnapshot.setDeserializeMainFunction()`](https://nodejs.org/docs/latest/api/v8.html#v8startupsnapshotsetdeserializemainfunctioncallback-data) could not be called because it had already been called before.
####  `ERR_ENCODING_INVALID_ENCODED_DATA`[#](https://nodejs.org/docs/latest/api/errors.html#err-encoding-invalid-encoded-data)
Data provided to `TextDecoder()` API was invalid according to the encoding provided.
####  `ERR_ENCODING_NOT_SUPPORTED`[#](https://nodejs.org/docs/latest/api/errors.html#err-encoding-not-supported)
Encoding provided to `TextDecoder()` API was not one of the [WHATWG Supported Encodings](https://nodejs.org/docs/latest/api/util.html#whatwg-supported-encodings).
####  `ERR_EVAL_ESM_CANNOT_PRINT`[#](https://nodejs.org/docs/latest/api/errors.html#err-eval-esm-cannot-print)
`--print` cannot be used with ESM input.
####  `ERR_EVENT_RECURSION`[#](https://nodejs.org/docs/latest/api/errors.html#err-event-recursion)
Thrown when an attempt is made to recursively dispatch an event on `EventTarget`.
####  `ERR_EXECUTION_ENVIRONMENT_NOT_AVAILABLE`[#](https://nodejs.org/docs/latest/api/errors.html#err-execution-environment-not-available)
The JS execution context is not associated with a Node.js environment. This may occur when Node.js is used as an embedded library and some hooks for the JS engine are not set up properly.
####  `ERR_FALSY_VALUE_REJECTION`[#](https://nodejs.org/docs/latest/api/errors.html#err-falsy-value-rejection)
A `Promise` that was callbackified via `util.callbackify()` was rejected with a falsy value.
####  `ERR_FEATURE_UNAVAILABLE_ON_PLATFORM`[#](https://nodejs.org/docs/latest/api/errors.html#err-feature-unavailable-on-platform)
Added in: v14.0.0
Used when a feature that is not available to the current platform which is running Node.js is used.
####  `ERR_FS_CP_DIR_TO_NON_DIR`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-cp-dir-to-non-dir)
Added in: v16.7.0
An attempt was made to copy a directory to a non-directory (file, symlink, etc.) using [`fs.cp()`](https://nodejs.org/docs/latest/api/fs.html#fscpsrc-dest-options-callback).
####  `ERR_FS_CP_EEXIST`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-cp-eexist)
Added in: v16.7.0
An attempt was made to copy over a file that already existed with [`fs.cp()`](https://nodejs.org/docs/latest/api/fs.html#fscpsrc-dest-options-callback), with the `force` and `errorOnExist` set to `true`.
####  `ERR_FS_CP_EINVAL`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-cp-einval)
Added in: v16.7.0
When using [`fs.cp()`](https://nodejs.org/docs/latest/api/fs.html#fscpsrc-dest-options-callback), `src` or `dest` pointed to an invalid path.
####  `ERR_FS_CP_FIFO_PIPE`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-cp-fifo-pipe)
Added in: v16.7.0
An attempt was made to copy a named pipe with [`fs.cp()`](https://nodejs.org/docs/latest/api/fs.html#fscpsrc-dest-options-callback).
####  `ERR_FS_CP_NON_DIR_TO_DIR`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-cp-non-dir-to-dir)
Added in: v16.7.0
An attempt was made to copy a non-directory (file, symlink, etc.) to a directory using [`fs.cp()`](https://nodejs.org/docs/latest/api/fs.html#fscpsrc-dest-options-callback).
####  `ERR_FS_CP_SOCKET`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-cp-socket)
Added in: v16.7.0
An attempt was made to copy to a socket with [`fs.cp()`](https://nodejs.org/docs/latest/api/fs.html#fscpsrc-dest-options-callback).
####  `ERR_FS_CP_SYMLINK_TO_SUBDIRECTORY`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-cp-symlink-to-subdirectory)
Added in: v16.7.0
When using [`fs.cp()`](https://nodejs.org/docs/latest/api/fs.html#fscpsrc-dest-options-callback), a symlink in `dest` pointed to a subdirectory of `src`.
####  `ERR_FS_CP_UNKNOWN`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-cp-unknown)
Added in: v16.7.0
An attempt was made to copy to an unknown file type with [`fs.cp()`](https://nodejs.org/docs/latest/api/fs.html#fscpsrc-dest-options-callback).
####  `ERR_FS_EISDIR`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-eisdir)
Path is a directory.
####  `ERR_FS_FILE_TOO_LARGE`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-file-too-large)
An attempt was made to read a file larger than the supported 2 GiB limit for `fs.readFile()`. This is not a limitation of `Buffer`, but an internal I/O constraint. For handling larger files, consider using `fs.createReadStream()` to read the file in chunks.
####  `ERR_FS_WATCH_QUEUE_OVERFLOW`[#](https://nodejs.org/docs/latest/api/errors.html#err-fs-watch-queue-overflow)
The number of file system events queued without being handled exceeded the size specified in `maxQueue` in `fs.watch()`.
####  `ERR_HTTP2_ALTSVC_INVALID_ORIGIN`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-altsvc-invalid-origin)
HTTP/2 ALTSVC frames require a valid origin.
####  `ERR_HTTP2_ALTSVC_LENGTH`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-altsvc-length)
HTTP/2 ALTSVC frames are limited to a maximum of 16,382 payload bytes.
####  `ERR_HTTP2_CONNECT_AUTHORITY`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-connect-authority)
For HTTP/2 requests using the `CONNECT` method, the `:authority` pseudo-header is required.
####  `ERR_HTTP2_CONNECT_PATH`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-connect-path)
For HTTP/2 requests using the `CONNECT` method, the `:path` pseudo-header is forbidden.
####  `ERR_HTTP2_CONNECT_SCHEME`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-connect-scheme)
For HTTP/2 requests using the `CONNECT` method, the `:scheme` pseudo-header is forbidden.
####  `ERR_HTTP2_ERROR`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-error)
A non-specific HTTP/2 error has occurred.
####  `ERR_HTTP2_GOAWAY_SESSION`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-goaway-session)
New HTTP/2 Streams may not be opened after the `Http2Session` has received a `GOAWAY` frame from the connected peer.
####  `ERR_HTTP2_HEADERS_AFTER_RESPOND`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-headers-after-respond)
An additional headers was specified after an HTTP/2 response was initiated.
####  `ERR_HTTP2_HEADERS_SENT`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-headers-sent)
An attempt was made to send multiple response headers.
####  `ERR_HTTP2_HEADER_SINGLE_VALUE`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-header-single-value)
Multiple values were provided for an HTTP/2 header field that was required to have only a single value.
####  `ERR_HTTP2_INFO_STATUS_NOT_ALLOWED`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-info-status-not-allowed)
Informational HTTP status codes (`1xx`) may not be set as the response status code on HTTP/2 responses.
####  `ERR_HTTP2_INVALID_CONNECTION_HEADERS`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-invalid-connection-headers)
HTTP/1 connection specific headers are forbidden to be used in HTTP/2 requests and responses.
####  `ERR_HTTP2_INVALID_HEADER_VALUE`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-invalid-header-value)
An invalid HTTP/2 header value was specified.
####  `ERR_HTTP2_INVALID_INFO_STATUS`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-invalid-info-status)
An invalid HTTP informational status code has been specified. Informational status codes must be an integer between `100` and `199` (inclusive).
####  `ERR_HTTP2_INVALID_ORIGIN`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-invalid-origin)
HTTP/2 `ORIGIN` frames require a valid origin.
####  `ERR_HTTP2_INVALID_PACKED_SETTINGS_LENGTH`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-invalid-packed-settings-length)
Input `Buffer` and `Uint8Array` instances passed to the `http2.getUnpackedSettings()` API must have a length that is a multiple of six.
####  `ERR_HTTP2_INVALID_PSEUDOHEADER`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-invalid-pseudoheader)
Only valid HTTP/2 pseudoheaders (`:status`, `:path`, `:authority`, `:scheme`, and `:method`) may be used.
####  `ERR_HTTP2_INVALID_SESSION`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-invalid-session)
An action was performed on an `Http2Session` object that had already been destroyed.
####  `ERR_HTTP2_INVALID_SETTING_VALUE`[#](https://nodejs.org/docs/latest/api/errors.html#err-http2-invalid-setting-value)
