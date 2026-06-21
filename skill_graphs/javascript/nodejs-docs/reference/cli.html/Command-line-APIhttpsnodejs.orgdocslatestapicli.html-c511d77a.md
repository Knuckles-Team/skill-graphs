v15.11.0, v14.18.0 | This API is no longer experimental.
Enable
When using a transpiler, such as TypeScript, stack traces thrown by an application reference the transpiled code, not the original source position. `--enable-source-maps` enables caching of Source Maps and makes a best effort to report stack traces relative to the original source file.
Overriding `Error.prepareStackTrace` may prevent `--enable-source-maps` from modifying the stack trace. Call and return the results of the original `Error.prepareStackTrace` in the overriding function to modify the stack trace with source maps.
```
const originalPrepareStackTrace = Error.prepareStackTrace;
Error.prepareStackTrace = (error, trace) => {
  // Modify error and trace and format stack trace with
  // original Error.prepareStackTrace.
  return originalPrepareStackTrace(error, trace);
};
copy
```

Note, enabling source maps can introduce latency to your application when `Error.stack` is accessed. If you access `Error.stack` frequently in your application, take into account the performance implications of `--enable-source-maps`.
####  `--entry-url`[#](https://nodejs.org/docs/latest/api/cli.html#entry-url)
Added in: v23.0.0, v22.10.0
Stability: 1 - Experimental
When present, Node.js will interpret the entry point as a URL, rather than a path.
Follows [ECMAScript module](https://nodejs.org/docs/latest/api/esm.html#modules-ecmascript-modules) resolution rules.
Any query parameter or hash in the URL will be accessible via [`import.meta.url`](https://nodejs.org/docs/latest/api/esm.html#importmetaurl).
```
node --entry-url 'file:///path/to/file.js?queryparams=work#and-hashes-too'
node --entry-url 'file.ts?query#hash'
node --entry-url 'data:text/javascript,console.log("Hello")'
copy
```

####  `--env-file-if-exists=file`[#](https://nodejs.org/docs/latest/api/cli.html#env-file-if-existsfile)
Added in: v22.9.0History Version | Changes
---|---
v24.10.0 | The `--env-file-if-exists` flag is no longer experimental.
Behavior is the same as [`--env-file`](https://nodejs.org/docs/latest/api/cli.html#--env-filefile), but an error is not thrown if the file does not exist.
####  `--env-file=file`[#](https://nodejs.org/docs/latest/api/cli.html#env-filefile)
Added in: v20.6.0History Version | Changes
---|---
v24.10.0 | The `--env-file` flag is no longer experimental.
v21.7.0, v20.12.0 | Add support to multi-line values.
Loads environment variables from a file relative to the current directory, making them available to applications on `process.env`. The [environment variables which configure Node.js](https://nodejs.org/docs/latest/api/cli.html#environment-variables_1), such as `NODE_OPTIONS`, are parsed and applied. If the same variable is defined in the environment and in the file, the value from the environment takes precedence.
You can pass multiple `--env-file` arguments. Subsequent files override pre-existing variables defined in previous files.
An error is thrown if the file does not exist.
```
node --env-file=.env --env-file=.development.env index.js
copy
```

The format of the file should be one line per key-value pair of environment variable name and value separated by `=`:
```
PORT=3000
copy
```

Any text after a `#` is treated as a comment:
```
# This is a comment
PORT=3000 # This is also a comment
copy
```

Values can start and end with the following quotes: ```, `"` or `'`. They are omitted from the values.
```
USERNAME="nodejs" # will result in `nodejs` as the value.
copy
```

Multi-line values are supported:
```
MULTI_LINE="THIS IS
A MULTILINE"
# will result in `THIS IS\nA MULTILINE` as the value.
copy
```

Export keyword before a key is ignored:
```
export USERNAME="nodejs" # will result in `nodejs` as the value.
copy
```

If you want to load environment variables from a file that may not exist, you can use the [`--env-file-if-exists`](https://nodejs.org/docs/latest/api/cli.html#--env-file-if-existsfile) flag instead.
####  `-e`, `--eval "script"`[#](https://nodejs.org/docs/latest/api/cli.html#e-eval-script)
Added in: v0.5.2History Version | Changes
---|---
v22.6.0 | Eval now supports experimental type-stripping.
v5.11.0 | Built-in libraries are now available as predefined variables.
Evaluate the following argument as JavaScript. The modules which are predefined in the REPL can also be used in `script`.
On Windows, using `cmd.exe` a single quote will not work correctly because it only recognizes double `"` for quoting. In Powershell or Git bash, both `'` and `"` are usable.
It is possible to run code containing inline types unless the [`--no-strip-types`](https://nodejs.org/docs/latest/api/cli.html#--no-strip-types) flag is provided.
####  `--experimental-addon-modules`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-addon-modules)
Added in: v23.6.0, v22.20.0
Stability: 1.0 - Early development
Enable experimental import support for `.node` addons.
####  `--experimental-config-file=config`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-config-fileconfig)
Added in: v23.10.0, v22.16.0
Stability: 1.0 - Early development
If present, Node.js will look for a configuration file at the specified path. Node.js will read the configuration file and apply the settings. The configuration file should be a JSON file with the following structure. `vX.Y.Z` in the `$schema` must be replaced with the version of Node.js you are using.
```
{
  "$schema": "https://nodejs.org/dist/vX.Y.Z/docs/node-config-schema.json",
  "nodeOptions": {
    "import": [
      "amaro/strip"
    ],
    "watch-path": "src",
    "watch-preserve-output": true
  },
  "test": {
    "test-isolation": "process"
  },
  "watch": {
    "watch-preserve-output": true
  }
}
copy
```

The configuration file supports namespace-specific options:
  * The `nodeOptions` field contains CLI flags that are allowed in [`NODE_OPTIONS`](https://nodejs.org/docs/latest/api/cli.html#node_optionsoptions).
  * Namespace fields like `test`, `watch`, and `permission` contain configuration specific to that subsystem.


When a namespace is present in the configuration file, Node.js automatically enables the corresponding flag (e.g., `--test`, `--watch`, `--permission`). This allows you to configure subsystem-specific options without explicitly passing the flag on the command line.
For example:
```
{
  "test": {
    "test-isolation": "process"
  }
}
copy
```

is equivalent to:
```
node --test --test-isolation=process
copy
```

To disable the automatic flag while still using namespace options, you can explicitly set the flag to `false` within the namespace:
```
{
  "test": {
    "test": false,
    "test-isolation": "process"
  }
}
copy
```

No-op flags are not supported. Not all V8 flags are currently supported.
It is possible to use the [official JSON schema](https://nodejs.org/docs/latest/node-config-schema.json) to validate the configuration file, which may vary depending on the Node.js version. Each key in the configuration file corresponds to a flag that can be passed as a command-line argument. The value of the key is the value that would be passed to the flag.
For example, the configuration file above is equivalent to the following command-line arguments:
```
node --import amaro/strip --watch-path=src --watch-preserve-output --test-isolation=process
copy
```

The priority in configuration is as follows:
  1. NODE_OPTIONS and command-line options
  2. Configuration file
  3. Dotenv NODE_OPTIONS


Values in the configuration file will not override the values in the environment variables and command-line options, but will override the values in the `NODE_OPTIONS` env file parsed by the `--env-file` flag.
Keys cannot be duplicated within the same or different namespaces.
The configuration parser will throw an error if the configuration file contains unknown keys or keys that cannot be used in a namespace.
Node.js will not sanitize or perform validation on the user-provided configuration, so **NEVER** use untrusted configuration files.
####  `--experimental-default-config-file`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-default-config-file)
Added in: v23.10.0, v22.16.0
Stability: 1.0 - Early development
If the `--experimental-default-config-file` flag is present, Node.js will look for a `node.config.json` file in the current working directory and load it as a as configuration file.
####  `--experimental-eventsource`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-eventsource)
Added in: v22.3.0, v20.18.0
Enable exposition of
####  `--experimental-import-meta-resolve`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-import-meta-resolve)
Added in: v13.9.0, v12.16.2History Version | Changes
---|---
v20.6.0, v18.19.0 | synchronous import.meta.resolve made available by default, with the flag retained for enabling the experimental second argument as previously supported.
Enable experimental `import.meta.resolve()` parent URL support, which allows passing a second `parentURL` argument for contextual resolution.
Previously gated the entire `import.meta.resolve` feature.
####  `--experimental-inspector-network-resource`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-inspector-network-resource)
Added in: v24.5.0, v22.19.0
Stability: 1.1 - Active Development
Enable experimental support for inspector network resources.
####  `--experimental-loader=module`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-loadermodule)
Added in: v8.8.0History Version | Changes
---|---
v23.6.1, v22.13.1, v20.18.2 | Using this feature with the permission model enabled requires passing `--allow-worker`.
v12.11.1 | This flag was renamed from `--loader` to `--experimental-loader`.
> This flag is discouraged and may be removed in a future version of Node.js. Please use [`--import` with `register()`](https://nodejs.org/docs/latest/api/module.html#registration-of-asynchronous-customization-hooks) instead.
Specify the `module` containing exported [asynchronous module customization hooks](https://nodejs.org/docs/latest/api/module.html#asynchronous-customization-hooks). `module` may be any string accepted as an [`import` specifier](https://nodejs.org/docs/latest/api/esm.html#import-specifiers).
This feature requires `--allow-worker` if used with the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model).
####  `--experimental-network-inspection`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-network-inspection)
Added in: v22.6.0, v20.18.0
Stability: 1 - Experimental
Enable experimental support for the network inspection with Chrome DevTools.
####  `--experimental-print-required-tla`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-print-required-tla)
Added in: v22.0.0, v20.17.0
If the ES module being `require()`'d contains top-level `await`, this flag allows Node.js to evaluate the module, try to locate the top-level awaits, and print their location to help users find them.
####  `--experimental-quic`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-quic)
Added in: v25.0.0
Stability: 1.1 - Active development
Enable experimental support for the QUIC protocol.
####  `--experimental-sea-config`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-sea-config)
Added in: v20.0.0
Stability: 1 - Experimental
Use this flag to generate a blob that can be injected into the Node.js binary to produce a [single executable application](https://nodejs.org/docs/latest/api/single-executable-applications.html). See the documentation about [this configuration](https://nodejs.org/docs/latest/api/single-executable-applications.html#1-generating-single-executable-preparation-blobs) for details.
####  `--experimental-shadow-realm`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-shadow-realm)
Added in: v19.0.0, v18.13.0
Use this flag to enable
####  `--experimental-storage-inspection`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-storage-inspection)
Added in: v25.5.0
Stability: 1.1 - Active Development
Enable experimental support for storage inspection
####  `--experimental-test-coverage`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-test-coverage)
Added in: v19.7.0, v18.15.0History Version | Changes
---|---
v20.1.0, v18.17.0 | This option can be used with `--test`.
When used in conjunction with the `node:test` module, a code coverage report is generated as part of the test runner output. If no tests are run, a coverage report is not generated. See the documentation on [collecting code coverage from tests](https://nodejs.org/docs/latest/api/test.html#collecting-code-coverage) for more details.
####  `--experimental-test-module-mocks`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-test-module-mocks)
Added in: v22.3.0, v20.18.0History Version | Changes
---|---
v23.6.1, v22.13.1, v20.18.2 | Using this feature with the permission model enabled requires passing `--allow-worker`.
Stability: 1.0 - Early development
Enable module mocking in the test runner.
This feature requires `--allow-worker` if used with the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model).
####  `--experimental-transform-types`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-transform-types)
Added in: v22.7.0
Stability: 1.2 - Release candidate
Enables the transformation of TypeScript-only syntax into JavaScript code. Implies `--enable-source-maps`.
####  `--experimental-vm-modules`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-vm-modules)
Added in: v9.6.0
Enable experimental ES Module support in the `node:vm` module.
####  `--experimental-wasi-unstable-preview1`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-wasi-unstable-preview1)
Added in: v13.3.0, v12.16.0History Version | Changes
---|---
v20.0.0, v18.17.0 | This option is no longer required as WASI is enabled by default, but can still be passed.
v13.6.0 | changed from `--experimental-wasi-unstable-preview0` to `--experimental-wasi-unstable-preview1`.
Enable experimental WebAssembly System Interface (WASI) support.
####  `--experimental-worker-inspection`[#](https://nodejs.org/docs/latest/api/cli.html#experimental-worker-inspection)
Added in: v24.1.0, v22.17.0
Stability: 1.1 - Active Development
Enable experimental support for the worker inspection with Chrome DevTools.
####  `--expose-gc`[#](https://nodejs.org/docs/latest/api/cli.html#expose-gc)
Added in: v22.3.0, v20.18.0
Stability: 1 - Experimental. This flag is inherited from V8 and is subject to change upstream.
This flag will expose the gc extension from V8.
```
if (globalThis.gc) {
  globalThis.gc();
}
copy
```

####  `--force-context-aware`[#](https://nodejs.org/docs/latest/api/cli.html#force-context-aware)
Added in: v12.12.0
Disable loading native addons that are not [context-aware](https://nodejs.org/docs/latest/api/addons.html#context-aware-addons).
####  `--force-fips`[#](https://nodejs.org/docs/latest/api/cli.html#force-fips)
Added in: v6.0.0
Force FIPS-compliant crypto on startup. (Cannot be disabled from script code.) (Same requirements as `--enable-fips`.)
####  `--force-node-api-uncaught-exceptions-policy`[#](https://nodejs.org/docs/latest/api/cli.html#force-node-api-uncaught-exceptions-policy)
Added in: v18.3.0, v16.17.0
Enforces `uncaughtException` event on Node-API asynchronous callbacks.
To prevent from an existing add-on from crashing the process, this flag is not enabled by default. In the future, this flag will be enabled by default to enforce the correct behavior.
####  `--frozen-intrinsics`[#](https://nodejs.org/docs/latest/api/cli.html#frozen-intrinsics)
Added in: v11.12.0
Stability: 1 - Experimental
Enable experimental frozen intrinsics like `Array` and `Object`.
Only the root context is supported. There is no guarantee that `globalThis.Array` is indeed the default intrinsic reference. Code may break under this flag.
To allow polyfills to be added, [`--require`](https://nodejs.org/docs/latest/api/cli.html#-r---require-module) and [`--import`](https://nodejs.org/docs/latest/api/cli.html#--importmodule) both run before freezing intrinsics.
####  `--heap-prof`[#](https://nodejs.org/docs/latest/api/cli.html#heap-prof)
Added in: v12.4.0History Version | Changes
---|---
v22.4.0, v20.16.0 | The `--heap-prof` flags are now stable.
Starts the V8 heap profiler on start up, and writes the heap profile to disk before exit.
If `--heap-prof-dir` is not specified, the generated profile is placed in the current working directory.
If `--heap-prof-name` is not specified, the generated profile is named `Heap.${yyyymmdd}.${hhmmss}.${pid}.${tid}.${seq}.heapprofile`.
```
$ node --heap-prof index.js
$ ls *.heapprofile
Heap.20190409.202950.15293.0.001.heapprofile
copy
```

####  `--heap-prof-dir`[#](https://nodejs.org/docs/latest/api/cli.html#heap-prof-dir)
Added in: v12.4.0History Version | Changes
---|---
v22.4.0, v20.16.0 | The `--heap-prof` flags are now stable.
Specify the directory where the heap profiles generated by `--heap-prof` will be placed.
The default value is controlled by the [`--diagnostic-dir`](https://nodejs.org/docs/latest/api/cli.html#--diagnostic-dirdirectory) command-line option.
####  `--heap-prof-interval`[#](https://nodejs.org/docs/latest/api/cli.html#heap-prof-interval)
Added in: v12.4.0History Version | Changes
---|---
v22.4.0, v20.16.0 | The `--heap-prof` flags are now stable.
Specify the average sampling interval in bytes for the heap profiles generated by `--heap-prof`. The default is 512 * 1024 bytes.
####  `--heap-prof-name`[#](https://nodejs.org/docs/latest/api/cli.html#heap-prof-name)
Added in: v12.4.0History Version | Changes
---|---
v22.4.0, v20.16.0 | The `--heap-prof` flags are now stable.
Specify the file name of the heap profile generated by `--heap-prof`.
####  `--heapsnapshot-near-heap-limit=max_count`[#](https://nodejs.org/docs/latest/api/cli.html#heapsnapshot-near-heap-limitmax-count)
Added in: v15.1.0, v14.18.0History Version | Changes
---|---
v25.4.0 | The flag is no longer experimental.
Writes a V8 heap snapshot to disk when the V8 heap usage is approaching the heap limit. `count` should be a non-negative integer (in which case Node.js will write no more than `max_count` snapshots to disk).
When generating snapshots, garbage collection may be triggered and bring the heap usage down. Therefore multiple snapshots may be written to disk before the Node.js instance finally runs out of memory. These heap snapshots can be compared to determine what objects are being allocated during the time consecutive snapshots are taken. It's not guaranteed that Node.js will write exactly `max_count` snapshots to disk, but it will try its best to generate at least one and up to `max_count` snapshots before the Node.js instance runs out of memory when `max_count` is greater than `0`.
Generating V8 snapshots takes time and memory (both memory managed by the V8 heap and native memory outside the V8 heap). The bigger the heap is, the more resources it needs. Node.js will adjust the V8 heap to accommodate the additional V8 heap memory overhead, and try its best to avoid using up all the memory available to the process. When the process uses more memory than the system deems appropriate, the process may be terminated abruptly by the system, depending on the system configuration.
```
$ node --max-old-space-size=100 --heapsnapshot-near-heap-limit=3 index.js
Wrote snapshot to Heap.20200430.100036.49580.0.001.heapsnapshot
Wrote snapshot to Heap.20200430.100037.49580.0.002.heapsnapshot
Wrote snapshot to Heap.20200430.100038.49580.0.003.heapsnapshot

<--- Last few GCs --->

[49580:0x110000000]     4826 ms: Mark-sweep 130.6 (147.8) -> 130.5 (147.8) MB, 27.4 / 0.0 ms  (average mu = 0.126, current mu = 0.034) allocation failure scavenge might not succeed
[49580:0x110000000]     4845 ms: Mark-sweep 130.6 (147.8) -> 130.6 (147.8) MB, 18.8 / 0.0 ms  (average mu = 0.088, current mu = 0.031) allocation failure scavenge might not succeed


<--- JS stacktrace --->

FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory
....
copy
```

####  `--heapsnapshot-signal=signal`[#](https://nodejs.org/docs/latest/api/cli.html#heapsnapshot-signalsignal)
Added in: v12.0.0
Enables a signal handler that causes the Node.js process to write a heap dump when the specified signal is received. `signal` must be a valid signal name. Disabled by default.
```
$ node --heapsnapshot-signal=SIGUSR2 index.js &
$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
node         1  5.5  6.1 787252 247004 ?       Ssl  16:43   0:02 node --heapsnapshot-signal=SIGUSR2 index.js
$ kill -USR2 1
$ ls
Heap.20190718.133405.15554.0.001.heapsnapshot
copy
```

####  `-h`, `--help`[#](https://nodejs.org/docs/latest/api/cli.html#h-help)
Added in: v0.1.3
Print node command-line options. The output of this option is less detailed than this document.
####  `--icu-data-dir=file`[#](https://nodejs.org/docs/latest/api/cli.html#icu-data-dirfile)
Added in: v0.11.15
Specify ICU data load path. (Overrides `NODE_ICU_DATA`.)
####  `--import=module`[#](https://nodejs.org/docs/latest/api/cli.html#importmodule)
Added in: v19.0.0, v18.18.0
Stability: 1 - Experimental
Preload the specified module at startup. If the flag is provided several times, each module will be executed sequentially in the order they appear, starting with the ones provided in [`NODE_OPTIONS`](https://nodejs.org/docs/latest/api/cli.html#node_optionsoptions).
Follows [ECMAScript module](https://nodejs.org/docs/latest/api/esm.html#modules-ecmascript-modules) resolution rules. Use [`--require`](https://nodejs.org/docs/latest/api/cli.html#-r---require-module) to load a [CommonJS module](https://nodejs.org/docs/latest/api/modules.html). Modules preloaded with `--require` will run before modules preloaded with `--import`.
Modules are preloaded into the main thread as well as any worker threads, forked processes, or clustered processes.
####  `--input-type=type`[#](https://nodejs.org/docs/latest/api/cli.html#input-typetype)
Added in: v12.0.0History Version | Changes
---|---
v23.6.0, v22.18.0 | Add support for `-typescript` values.
v22.7.0, v20.19.0 | ESM syntax detection is enabled by default.
This configures Node.js to interpret `--eval` or `STDIN` input as CommonJS or as an ES module. Valid values are `"commonjs"`, `"module"`, `"module-typescript"` and `"commonjs-typescript"`. The `"-typescript"` values are not available with the flag `--no-strip-types`. The default is no value, or `"commonjs"` if `--no-experimental-detect-module` is passed.
If `--input-type` is not provided, Node.js will try to detect the syntax with the following steps:
  1. Run the input as CommonJS.
  2. If step 1 fails, run the input as an ES module.
  3. If step 2 fails with a SyntaxError, strip the types.
  4. If step 3 fails with an error code [`ERR_UNSUPPORTED_TYPESCRIPT_SYNTAX`](https://nodejs.org/docs/latest/api/errors.html#err_unsupported_typescript_syntax) or [`ERR_INVALID_TYPESCRIPT_SYNTAX`](https://nodejs.org/docs/latest/api/errors.html#err_invalid_typescript_syntax), throw the error from step 2, including the TypeScript error in the message, else run as CommonJS.
  5. If step 4 fails, run the input as an ES module.


To avoid the delay of multiple syntax detection passes, the `--input-type=type` flag can be used to specify how the `--eval` input should be interpreted.
The REPL does not support this option. Usage of `--input-type=module` with [`--print`](https://nodejs.org/docs/latest/api/cli.html#-p---print-script) will throw an error, as `--print` does not support ES module syntax.
####  `--insecure-http-parser`[#](https://nodejs.org/docs/latest/api/cli.html#insecure-http-parser)
Added in: v13.4.0, v12.15.0, v10.19.0
Enable leniency flags on the HTTP parser. This may allow interoperability with non-conformant HTTP implementations.
When enabled, the parser will accept the following:
  * Invalid HTTP headers values.
  * Invalid HTTP versions.
  * Allow message containing both `Transfer-Encoding` and `Content-Length` headers.
  * Allow extra data after message when `Connection: close` is present.
  * Allow extra transfer encodings after `chunked` has been provided.
  * Allow `\n` to be used as token separator instead of `\r\n`.
  * Allow `\r\n` not to be provided after a chunk.
  * Allow spaces to be present after a chunk size and before `\r\n`.


All the above will expose your application to request smuggling or poisoning attack. Avoid using this option.
####  `--inspect-brk[=[host:]port]`[#](https://nodejs.org/docs/latest/api/cli.html#inspect-brkhostport)
Added in: v7.6.0
Activate inspector on `host:port` and break at start of user script. Default `host:port` is `127.0.0.1:9229`. If port `0` is specified, a random available port will be used.
See [V8 Inspector integration for Node.js](https://nodejs.org/docs/latest/api/debugger.html#v8-inspector-integration-for-nodejs) for further explanation on Node.js debugger.
See the [security warning](https://nodejs.org/docs/latest/api/cli.html#warning-binding-inspector-to-a-public-ipport-combination-is-insecure) below regarding the `host` parameter usage.
####  `--inspect-port=[host:]port`[#](https://nodejs.org/docs/latest/api/cli.html#inspect-porthostport)
Added in: v7.6.0
Set the `host:port` to be used when the inspector is activated. Useful when activating the inspector by sending the `SIGUSR1` signal. Except when [`--disable-sigusr1`](https://nodejs.org/docs/latest/api/cli.html#--disable-sigusr1) is passed.
