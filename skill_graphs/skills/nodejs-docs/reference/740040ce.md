The `FORCE_COLOR` environment variable is used to enable ANSI colorized output. The value may be:
  * `1`, `true`, or the empty string `''` indicate 16-color support,
  * `2` to indicate 256-color support, or
  * `3` to indicate 16 million-color support.


When `FORCE_COLOR` is used and set to a supported value, both the `NO_COLOR`, and `NODE_DISABLE_COLORS` environment variables are ignored.
Any other value will result in colorized output being disabled.
####  `NODE_COMPILE_CACHE=dir`[#](https://nodejs.org/docs/latest/api/cli.html#node-compile-cachedir)
Added in: v22.1.0History Version | Changes
---|---
v25.4.0 | This feature is no longer experimental.
Enable the [module compile cache](https://nodejs.org/docs/latest/api/module.html#module-compile-cache) for the Node.js instance. See the documentation of [module compile cache](https://nodejs.org/docs/latest/api/module.html#module-compile-cache) for details.
####  `NODE_COMPILE_CACHE_PORTABLE=1`[#](https://nodejs.org/docs/latest/api/cli.html#node-compile-cache-portable1)
When set to 1, the [module compile cache](https://nodejs.org/docs/latest/api/module.html#module-compile-cache) can be reused across different directory locations as long as the module layout relative to the cache directory remains the same.
####  `NODE_DEBUG=module[,…]`[#](https://nodejs.org/docs/latest/api/cli.html#node-debugmodule)
Added in: v0.1.32
`','`-separated list of core modules that should print debug information.
####  `NODE_DEBUG_NATIVE=module[,…]`[#](https://nodejs.org/docs/latest/api/cli.html#node-debug-nativemodule)
`','`-separated list of core C++ modules that should print debug information.
####  `NODE_DISABLE_COLORS=1`[#](https://nodejs.org/docs/latest/api/cli.html#node-disable-colors1)
Added in: v0.3.0
When set, colors will not be used in the REPL.
####  `NODE_DISABLE_COMPILE_CACHE=1`[#](https://nodejs.org/docs/latest/api/cli.html#node-disable-compile-cache1)
Added in: v22.8.0
Stability: 1.1 - Active Development
Disable the [module compile cache](https://nodejs.org/docs/latest/api/module.html#module-compile-cache) for the Node.js instance. See the documentation of [module compile cache](https://nodejs.org/docs/latest/api/module.html#module-compile-cache) for details.
####  `NODE_EXTRA_CA_CERTS=file`[#](https://nodejs.org/docs/latest/api/cli.html#node-extra-ca-certsfile)
Added in: v7.3.0
When set, the well known "root" CAs (like VeriSign) will be extended with the extra certificates in `file`. The file should consist of one or more trusted certificates in PEM format. A message will be emitted (once) with [`process.emitWarning()`](https://nodejs.org/docs/latest/api/process.html#processemitwarningwarning-options) if the file is missing or malformed, but any errors are otherwise ignored.
Neither the well known nor extra certificates are used when the `ca` options property is explicitly specified for a TLS or HTTPS client or server.
This environment variable is ignored when `node` runs as setuid root or has Linux file capabilities set.
The `NODE_EXTRA_CA_CERTS` environment variable is only read when the Node.js process is first launched. Changing the value at runtime using `process.env.NODE_EXTRA_CA_CERTS` has no effect on the current process.
####  `NODE_ICU_DATA=file`[#](https://nodejs.org/docs/latest/api/cli.html#node-icu-datafile)
Added in: v0.11.15
Data path for ICU (`Intl` object) data. Will extend linked-in data when compiled with small-icu support.
####  `NODE_NO_WARNINGS=1`[#](https://nodejs.org/docs/latest/api/cli.html#node-no-warnings1)
Added in: v6.11.0
When set to `1`, process warnings are silenced.
####  `NODE_OPTIONS=options...`[#](https://nodejs.org/docs/latest/api/cli.html#node-optionsoptions)
Added in: v8.0.0
A space-separated list of command-line options. `options...` are interpreted before command-line options, so command-line options will override or compound after anything in `options...`. Node.js will exit with an error if an option that is not allowed in the environment is used, such as `-p` or a script file.
If an option value contains a space, it can be escaped using double quotes:
```
NODE_OPTIONS='--require "./my path/file.js"'
copy
```

A singleton flag passed as a command-line option will override the same flag passed into `NODE_OPTIONS`:
```
# The inspector will be available on port 5555
NODE_OPTIONS='--inspect=localhost:4444' node --inspect=localhost:5555
copy
```

A flag that can be passed multiple times will be treated as if its `NODE_OPTIONS` instances were passed first, and then its command-line instances afterwards:
```
NODE_OPTIONS='--require "./a.js"' node --require "./b.js"
# is equivalent to:
node --require "./a.js" --require "./b.js"
copy
```

Node.js options that are allowed are in the following list. If an option supports both --XX and --no-XX variants, they are both supported but only one is included in the list below.
  * `--allow-addons`
  * `--allow-child-process`
  * `--allow-fs-read`
  * `--allow-fs-write`
  * `--allow-inspector`
  * `--allow-net`
  * `--allow-wasi`
  * `--allow-worker`
  * `--conditions`, `-C`
  * `--cpu-prof-dir`
  * `--cpu-prof-interval`
  * `--cpu-prof-name`
  * `--cpu-prof`
  * `--diagnostic-dir`
  * `--disable-proto`
  * `--disable-sigusr1`
  * `--disable-warning`
  * `--disable-wasm-trap-handler`
  * `--dns-result-order`
  * `--enable-fips`
  * `--enable-network-family-autoselection`
  * `--enable-source-maps`
  * `--entry-url`
  * `--experimental-abortcontroller`
  * `--experimental-addon-modules`
  * `--experimental-detect-module`
  * `--experimental-eventsource`
  * `--experimental-import-meta-resolve`
  * `--experimental-json-modules`
  * `--experimental-loader`
  * `--experimental-modules`
  * `--experimental-print-required-tla`
  * `--experimental-quic`
  * `--experimental-require-module`
  * `--experimental-shadow-realm`
  * `--experimental-specifier-resolution`
  * `--experimental-test-isolation`
  * `--experimental-top-level-await`
  * `--experimental-transform-types`
  * `--experimental-vm-modules`
  * `--experimental-wasi-unstable-preview1`
  * `--force-context-aware`
  * `--force-fips`
  * `--force-node-api-uncaught-exceptions-policy`
  * `--frozen-intrinsics`
  * `--heap-prof-dir`
  * `--heap-prof-interval`
  * `--heap-prof-name`
  * `--heap-prof`
  * `--heapsnapshot-near-heap-limit`
  * `--heapsnapshot-signal`
  * `--http-parser`
  * `--icu-data-dir`
  * `--import`
  * `--input-type`
  * `--insecure-http-parser`
  * `--inspect-brk`
  * `--inspect-port`, `--debug-port`
  * `--inspect-publish-uid`
  * `--inspect-wait`
  * `--inspect`
  * `--localstorage-file`
  * `--max-http-header-size`
  * `--max-old-space-size-percentage`
  * `--napi-modules`
  * `--network-family-autoselection-attempt-timeout`
  * `--no-addons`
  * `--no-async-context-frame`
  * `--no-deprecation`
  * `--no-experimental-global-navigator`
  * `--no-experimental-repl-await`
  * `--no-experimental-sqlite`
  * `--no-experimental-strip-types`
  * `--no-experimental-websocket`
  * `--no-experimental-webstorage`
  * `--no-extra-info-on-fatal-exception`
  * `--no-force-async-hooks-checks`
  * `--no-global-search-paths`
  * `--no-network-family-autoselection`
  * `--no-strip-types`
  * `--no-warnings`
  * `--no-webstorage`
  * `--node-memory-debug`
  * `--openssl-config`
  * `--openssl-legacy-provider`
  * `--openssl-shared-config`
  * `--pending-deprecation`
  * `--permission-audit`
  * `--permission`
  * `--preserve-symlinks-main`
  * `--preserve-symlinks`
  * `--prof-process`
  * `--redirect-warnings`
  * `--report-compact`
  * `--report-dir`, `--report-directory`
  * `--report-exclude-env`
  * `--report-exclude-network`
  * `--report-filename`
  * `--report-on-fatalerror`
  * `--report-on-signal`
  * `--report-signal`
  * `--report-uncaught-exception`
  * `--require-module`
  * `--require`, `-r`
  * `--secure-heap-min`
  * `--secure-heap`
  * `--snapshot-blob`
  * `--test-coverage-branches`
  * `--test-coverage-exclude`
  * `--test-coverage-functions`
  * `--test-coverage-include`
  * `--test-coverage-lines`
  * `--test-global-setup`
  * `--test-isolation`
  * `--test-name-pattern`
  * `--test-only`
  * `--test-reporter-destination`
  * `--test-reporter`
  * `--test-rerun-failures`
  * `--test-shard`
  * `--test-skip-pattern`
  * `--throw-deprecation`
  * `--title`
  * `--tls-cipher-list`
  * `--tls-keylog`
  * `--tls-max-v1.2`
  * `--tls-max-v1.3`
  * `--tls-min-v1.0`
  * `--tls-min-v1.1`
  * `--tls-min-v1.2`
  * `--tls-min-v1.3`
  * `--trace-deprecation`
  * `--trace-env-js-stack`
  * `--trace-env-native-stack`
  * `--trace-env`
  * `--trace-event-categories`
  * `--trace-event-file-pattern`
  * `--trace-events-enabled`
  * `--trace-exit`
  * `--trace-require-module`
  * `--trace-sigint`
  * `--trace-sync-io`
  * `--trace-tls`
  * `--trace-uncaught`
  * `--trace-warnings`
  * `--track-heap-objects`
  * `--unhandled-rejections`
  * `--use-bundled-ca`
  * `--use-env-proxy`
  * `--use-largepages`
  * `--use-openssl-ca`
  * `--use-system-ca`
  * `--v8-pool-size`
  * `--watch-kill-signal`
  * `--watch-path`
  * `--watch-preserve-output`
  * `--watch`
  * `--zero-fill-buffers`


V8 options that are allowed are:
  * `--abort-on-uncaught-exception`
  * `--disallow-code-generation-from-strings`
  * `--enable-etw-stack-walking`
  * `--expose-gc`
  * `--interpreted-frames-native-stack`
  * `--jitless`
  * `--max-old-space-size`
  * `--max-semi-space-size`
  * `--perf-basic-prof-only-functions`
  * `--perf-basic-prof`
  * `--perf-prof-unwinding-info`
  * `--perf-prof`
  * `--stack-trace-limit`


`--perf-basic-prof-only-functions`, `--perf-basic-prof`, `--perf-prof-unwinding-info`, and `--perf-prof` are only available on Linux.
`--enable-etw-stack-walking` is only available on Windows.
####  `NODE_PATH=path[:…]`[#](https://nodejs.org/docs/latest/api/cli.html#node-pathpath)
Added in: v0.1.32
`':'`-separated list of directories prefixed to the module search path.
On Windows, this is a `';'`-separated list instead.
####  `NODE_PENDING_DEPRECATION=1`[#](https://nodejs.org/docs/latest/api/cli.html#node-pending-deprecation1)
Added in: v8.0.0
When set to `1`, emit pending deprecation warnings.
Pending deprecations are generally identical to a runtime deprecation with the notable exception that they are turned _off_ by default and will not be emitted unless either the `--pending-deprecation` command-line flag, or the `NODE_PENDING_DEPRECATION=1` environment variable, is set. Pending deprecations are used to provide a kind of selective "early warning" mechanism that developers may leverage to detect deprecated API usage.
####  `NODE_PENDING_PIPE_INSTANCES=instances`[#](https://nodejs.org/docs/latest/api/cli.html#node-pending-pipe-instancesinstances)
Set the number of pending pipe instance handles when the pipe server is waiting for connections. This setting applies to Windows only.
####  `NODE_PRESERVE_SYMLINKS=1`[#](https://nodejs.org/docs/latest/api/cli.html#node-preserve-symlinks1)
Added in: v7.1.0
When set to `1`, instructs the module loader to preserve symbolic links when resolving and caching modules.
####  `NODE_REDIRECT_WARNINGS=file`[#](https://nodejs.org/docs/latest/api/cli.html#node-redirect-warningsfile)
Added in: v8.0.0
When set, process warnings will be emitted to the given file instead of printing to stderr. The file will be created if it does not exist, and will be appended to if it does. If an error occurs while attempting to write the warning to the file, the warning will be written to stderr instead. This is equivalent to using the `--redirect-warnings=file` command-line flag.
####  `NODE_REPL_EXTERNAL_MODULE=file`[#](https://nodejs.org/docs/latest/api/cli.html#node-repl-external-modulefile)
Added in: v13.0.0, v12.16.0History Version | Changes
---|---
v22.3.0, v20.16.0 | Remove the possibility to use this env var with kDisableNodeOptionsEnv for embedders.
Path to a Node.js module which will be loaded in place of the built-in REPL. Overriding this value to an empty string (`''`) will use the built-in REPL.
####  `NODE_REPL_HISTORY=file`[#](https://nodejs.org/docs/latest/api/cli.html#node-repl-historyfile)
Added in: v3.0.0
Path to the file used to store the persistent REPL history. The default path is `~/.node_repl_history`, which is overridden by this variable. Setting the value to an empty string (`''` or `' '`) disables persistent REPL history.
####  `NODE_SKIP_PLATFORM_CHECK=value`[#](https://nodejs.org/docs/latest/api/cli.html#node-skip-platform-checkvalue)
Added in: v14.5.0
If `value` equals `'1'`, the check for a supported platform is skipped during Node.js startup. Node.js might not execute correctly. Any issues encountered on unsupported platforms will not be fixed.
####  `NODE_TEST_CONTEXT=value`[#](https://nodejs.org/docs/latest/api/cli.html#node-test-contextvalue)
If `value` equals `'child'`, test reporter options will be overridden and test output will be sent to stdout in the TAP format. If any other value is provided, Node.js makes no guarantees about the reporter format used or its stability.
####  `NODE_TLS_REJECT_UNAUTHORIZED=value`[#](https://nodejs.org/docs/latest/api/cli.html#node-tls-reject-unauthorizedvalue)
If `value` equals `'0'`, certificate validation is disabled for TLS connections. This makes TLS, and HTTPS by extension, insecure. The use of this environment variable is strongly discouraged.
####  `NODE_USE_ENV_PROXY=1`[#](https://nodejs.org/docs/latest/api/cli.html#node-use-env-proxy1)
Added in: v24.0.0
Stability: 1.1 - Active Development
When enabled, Node.js parses the `HTTP_PROXY`, `HTTPS_PROXY` and `NO_PROXY` environment variables during startup, and tunnels requests over the specified proxy.
This can also be enabled using the [`--use-env-proxy`](https://nodejs.org/docs/latest/api/cli.html#--use-env-proxy) command-line flag. When both are set, `--use-env-proxy` takes precedence.
####  `NODE_USE_SYSTEM_CA=1`[#](https://nodejs.org/docs/latest/api/cli.html#node-use-system-ca1)
Added in: v24.6.0, v22.19.0
Node.js uses the trusted CA certificates present in the system store along with the `--use-bundled-ca` option and the `NODE_EXTRA_CA_CERTS` environment variable.
This can also be enabled using the [`--use-system-ca`](https://nodejs.org/docs/latest/api/cli.html#--use-system-ca) command-line flag. When both are set, `--use-system-ca` takes precedence.
####  `NODE_V8_COVERAGE=dir`[#](https://nodejs.org/docs/latest/api/cli.html#node-v8-coveragedir)
When set, Node.js will begin outputting `coverage` prefix).
`NODE_V8_COVERAGE` will automatically propagate to subprocesses, making it easier to instrument applications that call the `child_process.spawn()` family of functions. `NODE_V8_COVERAGE` can be set to an empty string, to prevent propagation.
##### Coverage output[#](https://nodejs.org/docs/latest/api/cli.html#coverage-output)
Coverage is output as an array of `result`:
```
{
  "result": [
    {
      "scriptId": "67",
      "url": "internal/tty.js",
      "functions": []
    }
  ]
}
copy
```

##### Source map cache[#](https://nodejs.org/docs/latest/api/cli.html#source-map-cache)
Stability: 1 - Experimental
If found, source map data is appended to the top-level key `source-map-cache` on the JSON coverage object.
`source-map-cache` is an object with keys representing the files source maps were extracted from, and values which include the raw source-map URL (in the key `url`), the parsed Source Map v3 information (in the key `data`), and the line lengths of the source file (in the key `lineLengths`).
```
{
  "result": [
    {
      "scriptId": "68",
      "url": "file:///absolute/path/to/source.js",
      "functions": []
    }
  ],
  "source-map-cache": {
    "file:///absolute/path/to/source.js": {
      "url": "./path-to-map.json",
      "data": {
        "version": 3,
        "sources": [
          "file:///absolute/path/to/original.js"
        ],
        "names": [
          "Foo",
          "console",
          "info"
        ],
        "mappings": "MAAMA,IACJC,YAAaC",
        "sourceRoot": "./"
      },
      "lineLengths": [
        13,
        62,
        38,
        27
      ]
    }
  }
}
copy
```

####  `NO_COLOR=<any>`[#](https://nodejs.org/docs/latest/api/cli.html#no-colorany)
`NODE_DISABLE_COLORS`. The value of the environment variable is arbitrary.
####  `OPENSSL_CONF=file`[#](https://nodejs.org/docs/latest/api/cli.html#openssl-conffile)
Added in: v6.11.0
Load an OpenSSL configuration file on startup. Among other uses, this can be used to enable FIPS-compliant crypto if Node.js is built with `./configure --openssl-fips`.
If the [`--openssl-config`](https://nodejs.org/docs/latest/api/cli.html#--openssl-configfile) command-line option is used, the environment variable is ignored.
####  `SSL_CERT_DIR=dir`[#](https://nodejs.org/docs/latest/api/cli.html#ssl-cert-dirdir)
Added in: v7.7.0
If `--use-openssl-ca` is enabled, or if `--use-system-ca` is enabled on platforms other than macOS and Windows, this overrides and sets OpenSSL's directory containing trusted certificates.
Be aware that unless the child environment is explicitly set, this environment variable will be inherited by any child processes, and if they use OpenSSL, it may cause them to trust the same CAs as node.
####  `SSL_CERT_FILE=file`[#](https://nodejs.org/docs/latest/api/cli.html#ssl-cert-filefile)
Added in: v7.7.0
If `--use-openssl-ca` is enabled, or if `--use-system-ca` is enabled on platforms other than macOS and Windows, this overrides and sets OpenSSL's file containing trusted certificates.
Be aware that unless the child environment is explicitly set, this environment variable will be inherited by any child processes, and if they use OpenSSL, it may cause them to trust the same CAs as node.
####  `TZ`[#](https://nodejs.org/docs/latest/api/cli.html#tz)
Added in: v0.0.1History Version | Changes
---|---
v16.2.0 | Changing the TZ variable using process.env.TZ = changes the timezone on Windows as well.
v13.0.0 | Changing the TZ variable using process.env.TZ = changes the timezone on POSIX systems.
The `TZ` environment variable is used to specify the timezone configuration.
While Node.js does not support all of the various `'Etc/UTC'`, `'Europe/Paris'`, or `'America/New_York'`). It may support a few other abbreviations or aliases, but these are strongly discouraged and not guaranteed.
```
$ TZ=Europe/Dublin node -pe "new Date().toString()"
Wed May 12 2021 20:30:48 GMT+0100 (Irish Standard Time)
copy
```

####  `UV_THREADPOOL_SIZE=size`[#](https://nodejs.org/docs/latest/api/cli.html#uv-threadpool-sizesize)
Set the number of threads used in libuv's threadpool to `size` threads.
Asynchronous system APIs are used by Node.js whenever possible, but where they do not exist, libuv's threadpool is used to create asynchronous node APIs based on synchronous system APIs. Node.js APIs that use the threadpool are:
  * all `fs` APIs, other than the file watcher APIs and those that are explicitly synchronous
  * asynchronous crypto APIs such as `crypto.pbkdf2()`, `crypto.scrypt()`, `crypto.randomBytes()`, `crypto.randomFill()`, `crypto.generateKeyPair()`
  * `dns.lookup()`
  * all `zlib` APIs, other than those that are explicitly synchronous


Because libuv's threadpool has a fixed size, it means that if for whatever reason any of these APIs takes a long time, other (seemingly unrelated) APIs that run in libuv's threadpool will experience degraded performance. In order to mitigate this issue, one potential solution is to increase the size of libuv's threadpool by setting the `'UV_THREADPOOL_SIZE'` environment variable to a value greater than `4` (its current default value). However, setting this from inside the process using `process.env.UV_THREADPOOL_SIZE=size` is not guaranteed to work as the threadpool would have been created as part of the runtime initialisation much before user code is run. For more information, see the
### Useful V8 options[#](https://nodejs.org/docs/latest/api/cli.html#useful-v8-options)
V8 has its own set of CLI options. Any V8 CLI option that is provided to `node` will be passed on to V8 to handle. V8's options have _no stability guarantee_. The V8 team themselves don't consider them to be part of their formal API, and reserve the right to change them at any time. Likewise, they are not covered by the Node.js stability guarantees. Many of the V8 options are of interest only to V8 developers. Despite this, there is a small set of V8 options that are widely applicable to Node.js, and they are documented here:
####  `--abort-on-uncaught-exception`[#](https://nodejs.org/docs/latest/api/cli.html#abort-on-uncaught-exception-1)
####  `--disallow-code-generation-from-strings`[#](https://nodejs.org/docs/latest/api/cli.html#disallow-code-generation-from-strings-1)
####  `--enable-etw-stack-walking`[#](https://nodejs.org/docs/latest/api/cli.html#enable-etw-stack-walking)
####  `--expose-gc`[#](https://nodejs.org/docs/latest/api/cli.html#expose-gc-1)
####  `--harmony-shadow-realm`[#](https://nodejs.org/docs/latest/api/cli.html#harmony-shadow-realm)
####  `--heap-snapshot-on-oom`[#](https://nodejs.org/docs/latest/api/cli.html#heap-snapshot-on-oom)
####  `--interpreted-frames-native-stack`[#](https://nodejs.org/docs/latest/api/cli.html#interpreted-frames-native-stack)
####  `--jitless`[#](https://nodejs.org/docs/latest/api/cli.html#jitless-1)
####  `--max-old-space-size=SIZE` (in MiB)[#](https://nodejs.org/docs/latest/api/cli.html#max-old-space-sizesize-in-mib)
Sets the max memory size of V8's old memory section. As memory consumption approaches the limit, V8 will spend more time on garbage collection in an effort to free unused memory.
On a machine with 2 GiB of memory, consider setting this to 1536 (1.5 GiB) to leave some memory for other uses and avoid swapping.
```
node --max-old-space-size=1536 index.js
copy
```

####  `--max-semi-space-size=SIZE` (in MiB)[#](https://nodejs.org/docs/latest/api/cli.html#max-semi-space-sizesize-in-mib)
Sets the maximum
Since the young generation size of the V8 heap is three times (see
The default value depends on the memory limit. For example, on 64-bit systems with a memory limit of 512 MiB, the max size of a semi-space defaults to 1 MiB. For memory limits up to and including 2GiB, the default max size of a semi-space will be less than 16 MiB on 64-bit systems.
To get the best configuration for your application, you should try different max-semi-space-size values when running benchmarks for your application.
For example, benchmark on a 64-bit systems:
```
for MiB in 16 32 64 128; do
    node --max-semi-space-size=$MiB index.js
done
copy
```

####  `--perf-basic-prof`[#](https://nodejs.org/docs/latest/api/cli.html#perf-basic-prof)
####  `--perf-basic-prof-only-functions`[#](https://nodejs.org/docs/latest/api/cli.html#perf-basic-prof-only-functions)
####  `--perf-prof`[#](https://nodejs.org/docs/latest/api/cli.html#perf-prof)
####  `--perf-prof-unwinding-info`[#](https://nodejs.org/docs/latest/api/cli.html#perf-prof-unwinding-info)
####  `--prof`[#](https://nodejs.org/docs/latest/api/cli.html#prof-1)
####  `--security-revert`[#](https://nodejs.org/docs/latest/api/cli.html#security-revert)
####  `--stack-trace-limit=limit`[#](https://nodejs.org/docs/latest/api/cli.html#stack-trace-limitlimit)
The maximum number of stack frames to collect in an error's stack trace. Setting it to 0 disables stack trace collection. The default value is 10.
```
node --stack-trace-limit=12 -p -e "Error.stackTraceLimit" # prints 12
copy
```
