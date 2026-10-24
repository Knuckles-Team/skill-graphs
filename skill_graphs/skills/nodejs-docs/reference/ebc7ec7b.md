Default host is `127.0.0.1`. If port `0` is specified, a random available port will be used.
See the [security warning](https://nodejs.org/docs/latest/api/cli.html#warning-binding-inspector-to-a-public-ipport-combination-is-insecure) below regarding the `host` parameter usage.
####  `--inspect-publish-uid=stderr,http`[#](https://nodejs.org/docs/latest/api/cli.html#inspect-publish-uidstderrhttp)
Specify ways of the inspector web socket url exposure.
By default inspector websocket url is available in stderr and under `/json/list` endpoint on `http://host:port/json/list`.
####  `--inspect-wait[=[host:]port]`[#](https://nodejs.org/docs/latest/api/cli.html#inspect-waithostport)
Added in: v22.2.0, v20.15.0
Activate inspector on `host:port` and wait for debugger to be attached. Default `host:port` is `127.0.0.1:9229`. If port `0` is specified, a random available port will be used.
See [V8 Inspector integration for Node.js](https://nodejs.org/docs/latest/api/debugger.html#v8-inspector-integration-for-nodejs) for further explanation on Node.js debugger.
See the [security warning](https://nodejs.org/docs/latest/api/cli.html#warning-binding-inspector-to-a-public-ipport-combination-is-insecure) below regarding the `host` parameter usage.
####  `--inspect[=[host:]port]`[#](https://nodejs.org/docs/latest/api/cli.html#inspecthostport)
Added in: v6.3.0
Activate inspector on `host:port`. Default is `127.0.0.1:9229`. If port `0` is specified, a random available port will be used.
V8 inspector integration allows tools such as Chrome DevTools and IDEs to debug and profile Node.js instances. The tools attach to Node.js instances via a tcp port and communicate using the [V8 Inspector integration for Node.js](https://nodejs.org/docs/latest/api/debugger.html#v8-inspector-integration-for-nodejs) for further explanation on Node.js debugger.
##### Warning: binding inspector to a public IP:port combination is insecure[#](https://nodejs.org/docs/latest/api/cli.html#warning-binding-inspector-to-a-public-ipport-combination-is-insecure)
Binding the inspector to a public IP (including `0.0.0.0`) with an open port is insecure, as it allows external hosts to connect to the inspector and perform a
If specifying a host, make sure that either:
  * The host is not accessible from public networks.
  * A firewall disallows unwanted connections on the port.


**More specifically,`--inspect=0.0.0.0` is insecure if the port (`9229` by default) is not firewall-protected.**
See the [debugging security implications](https://nodejs.org/en/docs/guides/debugging-getting-started/#security-implications) section for more information.
####  `-i`, `--interactive`[#](https://nodejs.org/docs/latest/api/cli.html#i-interactive)
Added in: v0.7.7
Opens the REPL even if stdin does not appear to be a terminal.
####  `--jitless`[#](https://nodejs.org/docs/latest/api/cli.html#jitless)
Added in: v12.0.0
Stability: 1 - Experimental. This flag is inherited from V8 and is subject to change upstream.
Disable
####  `--localstorage-file=file`[#](https://nodejs.org/docs/latest/api/cli.html#localstorage-filefile)
Added in: v22.4.0
Stability: 1.2 - Release candidate.
The file used to store `localStorage` data. If the file does not exist, it is created the first time `localStorage` is accessed. The same file may be shared between multiple Node.js processes concurrently.
####  `--max-http-header-size=size`[#](https://nodejs.org/docs/latest/api/cli.html#max-http-header-sizesize)
Added in: v11.6.0, v10.15.0History Version | Changes
---|---
v13.13.0 | Change maximum default size of HTTP headers from 8 KiB to 16 KiB.
Specify the maximum size, in bytes, of HTTP headers. Defaults to 16 KiB.
####  `--max-old-space-size-percentage=percentage`[#](https://nodejs.org/docs/latest/api/cli.html#max-old-space-size-percentagepercentage)
Sets the maximum memory size of V8's old memory section as a percentage of available system memory. This flag takes precedence over `--max-old-space-size` when both are specified.
The `percentage` parameter must be a number greater than 0 and up to 100, representing the percentage of available system memory to allocate to the V8 heap.
**Note:** This flag utilizes `--max-old-space-size`, which may be unreliable on 32-bit platforms due to integer overflow issues.
```
# Using 50% of available system memory
node --max-old-space-size-percentage=50 index.js

# Using 75% of available system memory
node --max-old-space-size-percentage=75 index.js
copy
```

####  `--napi-modules`[#](https://nodejs.org/docs/latest/api/cli.html#napi-modules)
Added in: v7.10.0
This option is a no-op. It is kept for compatibility.
####  `--network-family-autoselection-attempt-timeout`[#](https://nodejs.org/docs/latest/api/cli.html#network-family-autoselection-attempt-timeout)
Added in: v22.1.0, v20.13.0
Sets the default value for the network family autoselection attempt timeout. For more information, see [`net.getDefaultAutoSelectFamilyAttemptTimeout()`](https://nodejs.org/docs/latest/api/net.html#netgetdefaultautoselectfamilyattempttimeout).
####  `--no-addons`[#](https://nodejs.org/docs/latest/api/cli.html#no-addons)
Added in: v16.10.0, v14.19.0
Disable the `node-addons` exports condition as well as disable loading native addons. When `--no-addons` is specified, calling `process.dlopen` or requiring a native C++ addon will fail and throw an exception.
####  `--no-async-context-frame`[#](https://nodejs.org/docs/latest/api/cli.html#no-async-context-frame)
Added in: v24.0.0
Disables the use of [`AsyncLocalStorage`](https://nodejs.org/docs/latest/api/async_context.html#class-asynclocalstorage) backed by `AsyncContextFrame` and uses the prior implementation which relied on async_hooks. The previous model is retained for compatibility with Electron and for cases where the context flow may differ. However, if a difference in flow is found please report it.
####  `--no-deprecation`[#](https://nodejs.org/docs/latest/api/cli.html#no-deprecation)
Added in: v0.8.0
Silence deprecation warnings.
####  `--no-experimental-detect-module`[#](https://nodejs.org/docs/latest/api/cli.html#no-experimental-detect-module)
Added in: v21.1.0, v20.10.0History Version | Changes
---|---
v22.7.0, v20.19.0 | Syntax detection is enabled by default.
Disable using [syntax detection](https://nodejs.org/docs/latest/api/packages.html#syntax-detection) to determine module type.
####  `--no-experimental-global-navigator`[#](https://nodejs.org/docs/latest/api/cli.html#no-experimental-global-navigator)
Added in: v21.2.0
Stability: 1 - Experimental
Disable exposition of [Navigator API](https://nodejs.org/docs/latest/api/globals.html#navigator) on the global scope.
####  `--no-experimental-repl-await`[#](https://nodejs.org/docs/latest/api/cli.html#no-experimental-repl-await)
Added in: v16.6.0
Use this flag to disable top-level await in REPL.
####  `--no-experimental-require-module`[#](https://nodejs.org/docs/latest/api/cli.html#no-experimental-require-module)
Added in: v22.0.0, v20.17.0History Version | Changes
---|---
v25.4.0 | The flag was renamed from `--no-experimental-require-module` to `--no-require-module`, with the former marked as legacy.
v23.0.0, v22.12.0, v20.19.0 | This is now false by default.
Stability: 3 - Legacy: Use [`--no-require-module`](https://nodejs.org/docs/latest/api/cli.html#--no-require-module) instead.
Legacy alias for [`--no-require-module`](https://nodejs.org/docs/latest/api/cli.html#--no-require-module).
####  `--no-experimental-sqlite`[#](https://nodejs.org/docs/latest/api/cli.html#no-experimental-sqlite)
Added in: v22.5.0History Version | Changes
---|---
v23.4.0, v22.13.0 | SQLite is unflagged but still experimental.
Disable the experimental [`node:sqlite`](https://nodejs.org/docs/latest/api/sqlite.html) module.
####  `--no-experimental-websocket`[#](https://nodejs.org/docs/latest/api/cli.html#no-experimental-websocket)
Added in: v22.0.0
Disable exposition of
####  `--no-experimental-webstorage`[#](https://nodejs.org/docs/latest/api/cli.html#no-experimental-webstorage)
Added in: v22.4.0History Version | Changes
---|---
v25.0.0 | The feature is now enabled by default.
Stability: 1.2 - Release candidate.
Disable
####  `--no-extra-info-on-fatal-exception`[#](https://nodejs.org/docs/latest/api/cli.html#no-extra-info-on-fatal-exception)
Added in: v17.0.0
Hide extra information on fatal exception that causes exit.
####  `--no-force-async-hooks-checks`[#](https://nodejs.org/docs/latest/api/cli.html#no-force-async-hooks-checks)
Added in: v9.0.0
Disables runtime checks for `async_hooks`. These will still be enabled dynamically when `async_hooks` is enabled.
####  `--no-global-search-paths`[#](https://nodejs.org/docs/latest/api/cli.html#no-global-search-paths)
Added in: v16.10.0
Do not search modules from global paths like `$HOME/.node_modules` and `$NODE_PATH`.
####  `--no-network-family-autoselection`[#](https://nodejs.org/docs/latest/api/cli.html#no-network-family-autoselection)
Added in: v19.4.0History Version | Changes
---|---
v20.0.0 | The flag was renamed from `--no-enable-network-family-autoselection` to `--no-network-family-autoselection`. The old name can still work as an alias.
Disables the family autoselection algorithm unless connection options explicitly enables it.
####  `--no-require-module`[#](https://nodejs.org/docs/latest/api/cli.html#no-require-module)
Added in: v22.0.0, v20.17.0History Version | Changes
---|---
v25.4.0 | This flag is no longer experimental.
v25.4.0 | This flag was renamed from `--no-experimental-require-module` to `--no-require-module`.
v23.0.0, v22.12.0, v20.19.0 | This is now false by default.
Disable support for loading a synchronous ES module graph in `require()`.
See [Loading ECMAScript modules using `require()`](https://nodejs.org/docs/latest/api/modules.html#loading-ecmascript-modules-using-require).
####  `--no-strip-types`[#](https://nodejs.org/docs/latest/api/cli.html#no-strip-types)
Added in: v22.6.0History Version | Changes
---|---
v25.2.0 | Type stripping is now stable, the flag was renamed from `--no-experimental-strip-types` to `--no-strip-types`.
v23.6.0, v22.18.0 | Type stripping is enabled by default.
Disable type-stripping for TypeScript files. For more information, see the [TypeScript type-stripping](https://nodejs.org/docs/latest/api/typescript.html#type-stripping) documentation.
####  `--no-warnings`[#](https://nodejs.org/docs/latest/api/cli.html#no-warnings)
Added in: v6.0.0
Silence all process warnings (including deprecations).
####  `--node-memory-debug`[#](https://nodejs.org/docs/latest/api/cli.html#node-memory-debug)
Added in: v15.0.0, v14.18.0
Enable extra debug checks for memory leaks in Node.js internals. This is usually only useful for developers debugging Node.js itself.
####  `--openssl-config=file`[#](https://nodejs.org/docs/latest/api/cli.html#openssl-configfile)
Added in: v6.9.0
Load an OpenSSL configuration file on startup. Among other uses, this can be used to enable FIPS-compliant crypto if Node.js is built against FIPS-enabled OpenSSL.
####  `--openssl-legacy-provider`[#](https://nodejs.org/docs/latest/api/cli.html#openssl-legacy-provider)
Added in: v17.0.0, v16.17.0
Enable OpenSSL 3.0 legacy provider. For more information please see
####  `--openssl-shared-config`[#](https://nodejs.org/docs/latest/api/cli.html#openssl-shared-config)
Added in: v18.5.0, v16.17.0, v14.21.0
Enable OpenSSL default configuration section, `openssl_conf` to be read from the OpenSSL configuration file. The default configuration file is named `openssl.cnf` but this can be changed using the environment variable `OPENSSL_CONF`, or by using the command line option `--openssl-config`. The location of the default OpenSSL configuration file depends on how OpenSSL is being linked to Node.js. Sharing the OpenSSL configuration may have unwanted implications and it is recommended to use a configuration section specific to Node.js which is `nodejs_conf` and is default when this option is not used.
####  `--pending-deprecation`[#](https://nodejs.org/docs/latest/api/cli.html#pending-deprecation)
Added in: v8.0.0
Emit pending deprecation warnings.
Pending deprecations are generally identical to a runtime deprecation with the notable exception that they are turned _off_ by default and will not be emitted unless either the `--pending-deprecation` command-line flag, or the `NODE_PENDING_DEPRECATION=1` environment variable, is set. Pending deprecations are used to provide a kind of selective "early warning" mechanism that developers may leverage to detect deprecated API usage.
####  `--permission`[#](https://nodejs.org/docs/latest/api/cli.html#permission)
Added in: v20.0.0History Version | Changes
---|---
v23.5.0, v22.13.0 | Permission Model is now stable.
Enable the Permission Model for current process. When enabled, the following permissions are restricted:
  * File System - manageable through [`--allow-fs-read`](https://nodejs.org/docs/latest/api/cli.html#--allow-fs-read), [`--allow-fs-write`](https://nodejs.org/docs/latest/api/cli.html#--allow-fs-write) flags
  * Network - manageable through [`--allow-net`](https://nodejs.org/docs/latest/api/cli.html#--allow-net) flag
  * Child Process - manageable through [`--allow-child-process`](https://nodejs.org/docs/latest/api/cli.html#--allow-child-process) flag
  * Worker Threads - manageable through [`--allow-worker`](https://nodejs.org/docs/latest/api/cli.html#--allow-worker) flag
  * WASI - manageable through [`--allow-wasi`](https://nodejs.org/docs/latest/api/cli.html#--allow-wasi) flag
  * Addons - manageable through [`--allow-addons`](https://nodejs.org/docs/latest/api/cli.html#--allow-addons) flag


####  `--permission-audit`[#](https://nodejs.org/docs/latest/api/cli.html#permission-audit)
Added in: v25.8.0
Enable audit only for the permission model. When enabled, permission checks are performed but access is not denied. Instead, a warning is emitted for each permission violation via diagnostics channel.
####  `--preserve-symlinks`[#](https://nodejs.org/docs/latest/api/cli.html#preserve-symlinks)
Added in: v6.3.0
Instructs the module loader to preserve symbolic links when resolving and caching modules.
By default, when Node.js loads a module from a path that is symbolically linked to a different on-disk location, Node.js will dereference the link and use the actual on-disk "real path" of the module as both an identifier and as a root path to locate other dependency modules. In most cases, this default behavior is acceptable. However, when using symbolically linked peer dependencies, as illustrated in the example below, the default behavior causes an exception to be thrown if `moduleA` attempts to require `moduleB` as a peer dependency:
```
{appDir}
 ├── app
 │   ├── index.js
 │   └── node_modules
 │       ├── moduleA -> {appDir}/moduleA
 │       └── moduleB
 │           ├── index.js
 │           └── package.json
 └── moduleA
     ├── index.js
     └── package.json
copy
```

The `--preserve-symlinks` command-line flag instructs Node.js to use the symlink path for modules as opposed to the real path, allowing symbolically linked peer dependencies to be found.
Note, however, that using `--preserve-symlinks` can have other side effects. Specifically, symbolically linked _native_ modules can fail to load if those are linked from more than one location in the dependency tree (Node.js would see those as two separate modules and would attempt to load the module multiple times, causing an exception to be thrown).
The `--preserve-symlinks` flag does not apply to the main module, which allows `node --preserve-symlinks node_module/.bin/<foo>` to work. To apply the same behavior for the main module, also use `--preserve-symlinks-main`.
####  `--preserve-symlinks-main`[#](https://nodejs.org/docs/latest/api/cli.html#preserve-symlinks-main)
Added in: v10.2.0
Instructs the module loader to preserve symbolic links when resolving and caching the main module (`require.main`).
This flag exists so that the main module can be opted-in to the same behavior that `--preserve-symlinks` gives to all other imports; they are separate flags, however, for backward compatibility with older Node.js versions.
`--preserve-symlinks-main` does not imply `--preserve-symlinks`; use `--preserve-symlinks-main` in addition to `--preserve-symlinks` when it is not desirable to follow symlinks before resolving relative paths.
See [`--preserve-symlinks`](https://nodejs.org/docs/latest/api/cli.html#--preserve-symlinks) for more information.
####  `-p`, `--print "script"`[#](https://nodejs.org/docs/latest/api/cli.html#p-print-script)
Added in: v0.6.4History Version | Changes
---|---
v5.11.0 | Built-in libraries are now available as predefined variables.
Identical to `-e` but prints the result.
####  `--prof`[#](https://nodejs.org/docs/latest/api/cli.html#prof)
Added in: v2.0.0
Generate V8 profiler output.
####  `--prof-process`[#](https://nodejs.org/docs/latest/api/cli.html#prof-process)
Added in: v5.2.0
Process V8 profiler output generated using the V8 option `--prof`.
####  `--redirect-warnings=file`[#](https://nodejs.org/docs/latest/api/cli.html#redirect-warningsfile)
Added in: v8.0.0
Write process warnings to the given file instead of printing to stderr. The file will be created if it does not exist, and will be appended to if it does. If an error occurs while attempting to write the warning to the file, the warning will be written to stderr instead.
The `file` name may be an absolute path. If it is not, the default directory it will be written to is controlled by the [`--diagnostic-dir`](https://nodejs.org/docs/latest/api/cli.html#--diagnostic-dirdirectory) command-line option.
####  `--report-compact`[#](https://nodejs.org/docs/latest/api/cli.html#report-compact)
Added in: v13.12.0, v12.17.0
Write reports in a compact format, single-line JSON, more easily consumable by log processing systems than the default multi-line format designed for human consumption.
####  `--report-dir=directory`, `--report-directory=directory`[#](https://nodejs.org/docs/latest/api/cli.html#report-dirdirectory-report-directorydirectory)
Added in: v11.8.0History Version | Changes
---|---
v13.12.0, v12.17.0 | This option is no longer experimental.
v12.0.0 | Changed from `--diagnostic-report-directory` to `--report-directory`.
Location at which the report will be generated.
####  `--report-exclude-env`[#](https://nodejs.org/docs/latest/api/cli.html#report-exclude-env)
Added in: v23.3.0, v22.13.0
When `--report-exclude-env` is passed the diagnostic report generated will not contain the `environmentVariables` data.
####  `--report-exclude-network`[#](https://nodejs.org/docs/latest/api/cli.html#report-exclude-network)
Added in: v22.0.0, v20.13.0
Exclude `header.networkInterfaces` from the diagnostic report. By default this is not set and the network interfaces are included.
####  `--report-filename=filename`[#](https://nodejs.org/docs/latest/api/cli.html#report-filenamefilename)
Added in: v11.8.0History Version | Changes
---|---
v13.12.0, v12.17.0 | This option is no longer experimental.
v12.0.0 | changed from `--diagnostic-report-filename` to `--report-filename`.
Name of the file to which the report will be written.
If the filename is set to `'stdout'` or `'stderr'`, the report is written to the stdout or stderr of the process respectively.
####  `--report-on-fatalerror`[#](https://nodejs.org/docs/latest/api/cli.html#report-on-fatalerror)
Added in: v11.8.0History Version | Changes
---|---
v14.0.0, v13.14.0, v12.17.0 | This option is no longer experimental.
v12.0.0 | changed from `--diagnostic-report-on-fatalerror` to `--report-on-fatalerror`.
Enables the report to be triggered on fatal errors (internal errors within the Node.js runtime such as out of memory) that lead to termination of the application. Useful to inspect various diagnostic data elements such as heap, stack, event loop state, resource consumption etc. to reason about the fatal error.
####  `--report-on-signal`[#](https://nodejs.org/docs/latest/api/cli.html#report-on-signal)
Added in: v11.8.0History Version | Changes
---|---
v13.12.0, v12.17.0 | This option is no longer experimental.
v12.0.0 | changed from `--diagnostic-report-on-signal` to `--report-on-signal`.
Enables report to be generated upon receiving the specified (or predefined) signal to the running Node.js process. The signal to trigger the report is specified through `--report-signal`.
####  `--report-signal=signal`[#](https://nodejs.org/docs/latest/api/cli.html#report-signalsignal)
Added in: v11.8.0History Version | Changes
---|---
v13.12.0, v12.17.0 | This option is no longer experimental.
v12.0.0 | changed from `--diagnostic-report-signal` to `--report-signal`.
Sets or resets the signal for report generation (not supported on Windows). Default signal is `SIGUSR2`.
####  `--report-uncaught-exception`[#](https://nodejs.org/docs/latest/api/cli.html#report-uncaught-exception)
Added in: v11.8.0History Version | Changes
---|---
v18.8.0, v16.18.0 | Report is not generated if the uncaught exception is handled.
v13.12.0, v12.17.0 | This option is no longer experimental.
v12.0.0 | changed from `--diagnostic-report-uncaught-exception` to `--report-uncaught-exception`.
Enables report to be generated when the process exits due to an uncaught exception. Useful when inspecting the JavaScript stack in conjunction with native stack and other runtime environment data.
####  `-r`, `--require module`[#](https://nodejs.org/docs/latest/api/cli.html#r-require-module)
Added in: v1.6.0History Version | Changes
---|---
v23.0.0, v22.12.0, v20.19.0 | This option also supports ECMAScript module.
Preload the specified module at startup.
Follows `require()`'s module resolution rules. `module` may be either a path to a file, or a node module name.
Modules preloaded with `--require` will run before modules preloaded with `--import`.
Modules are preloaded into the main thread as well as any worker threads, forked processes, or clustered processes.
####  `--run`[#](https://nodejs.org/docs/latest/api/cli.html#run)
Added in: v22.0.0History Version | Changes
---|---
v22.3.0 | NODE_RUN_SCRIPT_NAME environment variable is added.
v22.3.0 | NODE_RUN_PACKAGE_JSON_PATH environment variable is added.
v22.3.0 | Traverses up to the root directory and finds a `package.json` file to run the command from, and updates `PATH` environment variable accordingly.
This runs a specified command from a package.json's `"scripts"` object. If a missing `"command"` is provided, it will list the available scripts.
`--run` will traverse up to the root directory and finds a `package.json` file to run the command from.
`--run` prepends `./node_modules/.bin` for each ancestor of the current directory, to the `PATH` in order to execute the binaries from different folders where multiple `node_modules` directories are present, if `ancestor-folder/node_modules/.bin` is a directory.
`--run` executes the command in the directory containing the related `package.json`.
For example, the following command will run the `test` script of the `package.json` in the current folder:
```
$ node --run test
copy
```

You can also pass arguments to the command. Any argument after `--` will be appended to the script:
```
$ node --run test -- --verbose
copy
```

##### Intentional limitations[#](https://nodejs.org/docs/latest/api/cli.html#intentional-limitations)
`node --run` is not meant to match the behaviors of `npm run` or of the `run` commands of other package managers. The Node.js implementation is intentionally more limited, in order to focus on top performance for the most common use cases. Some features of other `run` implementations that are intentionally excluded are:
  * Running `pre` or `post` scripts in addition to the specified script.
  * Defining package manager-specific environment variables.


##### Environment variables[#](https://nodejs.org/docs/latest/api/cli.html#environment-variables)
The following environment variables are set when running a script with `--run`:
  * `NODE_RUN_SCRIPT_NAME`: The name of the script being run. For example, if `--run` is used to run `test`, the value of this variable will be `test`.
  * `NODE_RUN_PACKAGE_JSON_PATH`: The path to the `package.json` that is being processed.


####  `--secure-heap-min=n`[#](https://nodejs.org/docs/latest/api/cli.html#secure-heap-minn)
Added in: v15.6.0
When using `--secure-heap`, the `--secure-heap-min` flag specifies the minimum allocation from the secure heap. The minimum value is `2`. The maximum value is the lesser of `--secure-heap` or `2147483647`. The value given must be a power of two.
####  `--secure-heap=n`[#](https://nodejs.org/docs/latest/api/cli.html#secure-heapn)
Added in: v15.6.0
Initializes an OpenSSL secure heap of `n` bytes. When initialized, the secure heap is used for selected types of allocations within OpenSSL during key generation and other operations. This is useful, for instance, to prevent sensitive information from leaking due to pointer overruns or underruns.
The secure heap is a fixed size and cannot be resized at runtime so, if used, it is important to select a large enough heap to cover all application uses.
The heap size given must be a power of two. Any value less than 2 will disable the secure heap.
The secure heap is disabled by default.
The secure heap is not available on Windows.
See
####  `--snapshot-blob=path`[#](https://nodejs.org/docs/latest/api/cli.html#snapshot-blobpath)
