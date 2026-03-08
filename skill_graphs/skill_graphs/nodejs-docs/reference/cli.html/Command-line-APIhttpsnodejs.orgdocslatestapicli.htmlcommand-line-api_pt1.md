## Command-line API[#](https://nodejs.org/docs/latest/api/cli.html#command-line-api)
Node.js comes with a variety of CLI options. These options expose built-in debugging, multiple ways to execute scripts, and other helpful runtime options.
To view this documentation as a manual page in a terminal, run `man node`.
### Synopsis[#](https://nodejs.org/docs/latest/api/cli.html#synopsis)
`node [options] [V8 options] [<program-entry-point> | -e "script" | -] [--] [arguments]`
`node inspect [<program-entry-point> | -e "script" | <host>:<port>] …`
`node --v8-options`
Execute without arguments to start the [REPL](https://nodejs.org/docs/latest/api/repl.html).
For more info about `node inspect`, see the [debugger](https://nodejs.org/docs/latest/api/debugger.html) documentation.
### Program entry point[#](https://nodejs.org/docs/latest/api/cli.html#program-entry-point)
The program entry point is a specifier-like string. If the string is not an absolute path, it's resolved as a relative path from the current working directory. That entry point string is then resolved as if it's been requested by `require()` from the current working directory. If no corresponding file is found, an error is thrown.
By default, the resolved path is also loaded as if it's been requested by `require()`, unless one of the conditions below apply—then it's loaded as if it's been requested by `import()`:
  * The program was started with a command-line flag that forces the entry point to be loaded with ECMAScript module loader, such as `--import`.
  * The file has an `.mjs`, `.mts` or `.wasm` extension.
  * The file does not have a `.cjs` extension, and the nearest parent `package.json` file contains a top-level [`"type"`](https://nodejs.org/docs/latest/api/packages.html#type) field with a value of `"module"`.


See [module resolution and loading](https://nodejs.org/docs/latest/api/packages.html#module-resolution-and-loading) for more details.
### Options[#](https://nodejs.org/docs/latest/api/cli.html#options)
History Version | Changes
---|---
v10.12.0 | Underscores instead of dashes are now allowed for Node.js options as well, in addition to V8 options.
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
All options, including V8 options, allow words to be separated by both dashes (`-`) or underscores (`_`). For example, `--pending-deprecation` is equivalent to `--pending_deprecation`.
If an option that takes a single value (such as `--max-http-header-size`) is passed more than once, then the last passed value is used. Options from the command line take precedence over options passed through the [`NODE_OPTIONS`](https://nodejs.org/docs/latest/api/cli.html#node_optionsoptions) environment variable.
Alias for stdin. Analogous to the use of `-` in other command-line utilities, meaning that the script is read from stdin, and the rest of the options are passed to that script.
Added in: v8.0.0
Indicate the end of node options. Pass the rest of the arguments to the script. If no script filename or eval/print script is supplied prior to this, then the next argument is used as a script filename.
Added in: v6.11.0
####  `--abort-on-uncaught-exception`[#](https://nodejs.org/docs/latest/api/cli.html#abort-on-uncaught-exception)
Added in: v0.10.8
Aborting instead of exiting causes a core file to be generated for post-mortem analysis using a debugger (such as `lldb`, `gdb`, and `mdb`).
If this flag is passed, the behavior can still be set to not abort through [`process.setUncaughtExceptionCaptureCallback()`](https://nodejs.org/docs/latest/api/process.html#processsetuncaughtexceptioncapturecallbackfn) (and through usage of the `node:domain` module that uses it).
####  `--allow-addons`[#](https://nodejs.org/docs/latest/api/cli.html#allow-addons)
Added in: v21.6.0, v20.12.0
Stability: 1.1 - Active development
When using the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model), the process will not be able to use native addons by default. Attempts to do so will throw an `ERR_DLOPEN_DISABLED` unless the user explicitly passes the `--allow-addons` flag when starting Node.js.
Example:
```
// Attempt to require an native addon
require('nodejs-addon-example');
copy
```
```
$ node --permission --allow-fs-read=* index.js
node:internal/modules/cjs/loader:1319
  return process.dlopen(module, path.toNamespacedPath(filename));
                 ^

Error: Cannot load native addon because loading addons is disabled.
    at Module._extensions..node (node:internal/modules/cjs/loader:1319:18)
    at Module.load (node:internal/modules/cjs/loader:1091:32)
    at Module._load (node:internal/modules/cjs/loader:938:12)
    at Module.require (node:internal/modules/cjs/loader:1115:19)
    at require (node:internal/modules/helpers:130:18)
    at Object.<anonymous> (/home/index.js:1:15)
    at Module._compile (node:internal/modules/cjs/loader:1233:14)
    at Module._extensions..js (node:internal/modules/cjs/loader:1287:10)
    at Module.load (node:internal/modules/cjs/loader:1091:32)
    at Module._load (node:internal/modules/cjs/loader:938:12) {
  code: 'ERR_DLOPEN_DISABLED'
}
copy
```

####  `--allow-child-process`[#](https://nodejs.org/docs/latest/api/cli.html#allow-child-process)
Added in: v20.0.0History Version | Changes
---|---
v24.4.0, v22.18.0 | When spawning process with the permission model enabled. The flags are inherit to the child Node.js process through NODE_OPTIONS environment variable.
Stability: 1.1 - Active development
When using the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model), the process will not be able to spawn any child process by default. Attempts to do so will throw an `ERR_ACCESS_DENIED` unless the user explicitly passes the `--allow-child-process` flag when starting Node.js.
Example:
```
const childProcess = require('node:child_process');
// Attempt to bypass the permission
childProcess.spawn('node', ['-e', 'require("fs").writeFileSync("/new-file", "example")']);
copy
```
```
$ node --permission --allow-fs-read=* index.js
node:internal/child_process:388
  const err = this._handle.spawn(options);
                           ^
Error: Access to this API has been restricted
    at ChildProcess.spawn (node:internal/child_process:388:28)
    at node:internal/main/run_main_module:17:47 {
  code: 'ERR_ACCESS_DENIED',
  permission: 'ChildProcess'
}
copy
```

The `child_process.fork()` API inherits the execution arguments from the parent process. This means that if Node.js is started with the Permission Model enabled and the `--allow-child-process` flag is set, any child process created using `child_process.fork()` will automatically receive all relevant Permission Model flags.
This behavior also applies to `child_process.spawn()`, but in that case, the flags are propagated via the `NODE_OPTIONS` environment variable rather than directly through the process arguments.
####  `--allow-fs-read`[#](https://nodejs.org/docs/latest/api/cli.html#allow-fs-read)
Added in: v20.0.0History Version | Changes
---|---
v24.2.0, v22.17.0 | Entrypoints of your application are allowed to be read implicitly.
v23.5.0, v22.13.0 | Permission Model and --allow-fs flags are stable.
v20.7.0 | Paths delimited by comma (`,`) are no longer allowed.
This flag configures file system read permissions using the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model).
The valid arguments for the `--allow-fs-read` flag are:
  * `*` - To allow all `FileSystemRead` operations.
  * Multiple paths can be allowed using multiple `--allow-fs-read` flags. Example `--allow-fs-read=/folder1/ --allow-fs-read=/folder1/`


Examples can be found in the [File System Permissions](https://nodejs.org/docs/latest/api/permissions.html#file-system-permissions) documentation.
The initializer module and custom `--require` modules has a implicit read permission.
```
$ node --permission -r custom-require.js -r custom-require-2.js index.js
copy
```

  * The `custom-require.js`, `custom-require-2.js`, and `index.js` will be by default in the allowed read list.

```
process.has('fs.read', 'index.js'); // true
process.has('fs.read', 'custom-require.js'); // true
process.has('fs.read', 'custom-require-2.js'); // true
copy
```

####  `--allow-fs-write`[#](https://nodejs.org/docs/latest/api/cli.html#allow-fs-write)
Added in: v20.0.0History Version | Changes
---|---
v23.5.0, v22.13.0 | Permission Model and --allow-fs flags are stable.
v20.7.0 | Paths delimited by comma (`,`) are no longer allowed.
This flag configures file system write permissions using the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model).
The valid arguments for the `--allow-fs-write` flag are:
  * `*` - To allow all `FileSystemWrite` operations.
  * Multiple paths can be allowed using multiple `--allow-fs-write` flags. Example `--allow-fs-write=/folder1/ --allow-fs-write=/folder1/`


Paths delimited by comma (`,`) are no longer allowed. When passing a single flag with a comma a warning will be displayed.
Examples can be found in the [File System Permissions](https://nodejs.org/docs/latest/api/permissions.html#file-system-permissions) documentation.
####  `--allow-inspector`[#](https://nodejs.org/docs/latest/api/cli.html#allow-inspector)
Added in: v25.0.0
Stability: 1.0 - Early development
When using the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model), the process will not be able to connect through inspector protocol.
Attempts to do so will throw an `ERR_ACCESS_DENIED` unless the user explicitly passes the `--allow-inspector` flag when starting Node.js.
Example:
```
const { Session } = require('node:inspector/promises');

const session = new Session();
session.connect();
copy
```
```
$ node --permission index.js
Error: connect ERR_ACCESS_DENIED Access to this API has been restricted. Use --allow-inspector to manage permissions.
  code: 'ERR_ACCESS_DENIED',
}
copy
```

####  `--allow-net`[#](https://nodejs.org/docs/latest/api/cli.html#allow-net)
Added in: v25.0.0
Stability: 1.1 - Active development
When using the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model), the process will not be able to access network by default. Attempts to do so will throw an `ERR_ACCESS_DENIED` unless the user explicitly passes the `--allow-net` flag when starting Node.js.
Example:
```
const http = require('node:http');
// Attempt to bypass the permission
const req = http.get('http://example.com', () => {});

req.on('error', (err) => {
  console.log('err', err);
});
copy
```
```
$ node --permission index.js
Error: connect ERR_ACCESS_DENIED Access to this API has been restricted. Use --allow-net to manage permissions.
  code: 'ERR_ACCESS_DENIED',
}
copy
```

####  `--allow-wasi`[#](https://nodejs.org/docs/latest/api/cli.html#allow-wasi)
Added in: v22.3.0, v20.16.0
Stability: 1.1 - Active development
When using the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model), the process will not be capable of creating any WASI instances by default. For security reasons, the call will throw an `ERR_ACCESS_DENIED` unless the user explicitly passes the flag `--allow-wasi` in the main Node.js process.
Example:
```
const { WASI } = require('node:wasi');
// Attempt to bypass the permission
new WASI({
  version: 'preview1',
  // Attempt to mount the whole filesystem
  preopens: {
    '/': '/',
  },
});
copy
```
```
$ node --permission --allow-fs-read=* index.js

Error: Access to this API has been restricted
    at node:internal/main/run_main_module:30:49 {
  code: 'ERR_ACCESS_DENIED',
  permission: 'WASI',
}
copy
```

####  `--allow-worker`[#](https://nodejs.org/docs/latest/api/cli.html#allow-worker)
Added in: v20.0.0
Stability: 1.1 - Active development
When using the [Permission Model](https://nodejs.org/docs/latest/api/permissions.html#permission-model), the process will not be able to create any worker threads by default. For security reasons, the call will throw an `ERR_ACCESS_DENIED` unless the user explicitly pass the flag `--allow-worker` in the main Node.js process.
Example:
```
const { Worker } = require('node:worker_threads');
// Attempt to bypass the permission
new Worker(__filename);
copy
```
```
$ node --permission --allow-fs-read=* index.js

Error: Access to this API has been restricted
    at node:internal/main/run_main_module:17:47 {
  code: 'ERR_ACCESS_DENIED',
  permission: 'WorkerThreads'
}
copy
```

####  `--build-sea=config`[#](https://nodejs.org/docs/latest/api/cli.html#build-seaconfig)
Added in: v25.5.0
Stability: 1.1 - Active development
Generates a [single executable application](https://nodejs.org/docs/latest/api/single-executable-applications.html) from a JSON configuration file. The argument must be a path to the configuration file. If the path is not absolute, it is resolved relative to the current working directory.
For configuration fields, cross-platform notes, and asset APIs, see the [single executable application](https://nodejs.org/docs/latest/api/single-executable-applications.html) documentation.
####  `--build-snapshot`[#](https://nodejs.org/docs/latest/api/cli.html#build-snapshot)
Added in: v18.8.0History Version | Changes
---|---
v25.4.0 | The snapshot building process is no longer experimental.
Generates a snapshot blob when the process exits and writes it to disk, which can be loaded later with `--snapshot-blob`.
When building the snapshot, if `--snapshot-blob` is not specified, the generated blob will be written, by default, to `snapshot.blob` in the current working directory. Otherwise it will be written to the path specified by `--snapshot-blob`.
```
$ echo "globalThis.foo = 'I am from the snapshot'" > snapshot.js

# Run snapshot.js to initialize the application and snapshot the
# state of it into snapshot.blob.
$ node --snapshot-blob snapshot.blob --build-snapshot snapshot.js

$ echo "console.log(globalThis.foo)" > index.js

# Load the generated snapshot and start the application from index.js.
$ node --snapshot-blob snapshot.blob index.js
I am from the snapshot
copy
```

The [`v8.startupSnapshot` API](https://nodejs.org/docs/latest/api/v8.html#startup-snapshot-api) can be used to specify an entry point at snapshot building time, thus avoiding the need of an additional entry script at deserialization time:
```
$ echo "require('v8').startupSnapshot.setDeserializeMainFunction(() => console.log('I am from the snapshot'))" > snapshot.js
$ node --snapshot-blob snapshot.blob --build-snapshot snapshot.js
$ node --snapshot-blob snapshot.blob
I am from the snapshot
copy
```

For more information, check out the [`v8.startupSnapshot` API](https://nodejs.org/docs/latest/api/v8.html#startup-snapshot-api) documentation.
The snapshot currently only supports loading a single entrypoint during the snapshot building process, which can load built-in modules, but not additional user-land modules. Users can bundle their applications into a single script with their bundler of choice before building a snapshot.
As it's complicated to ensure the serializablility of all built-in modules, which are also growing over time, only a subset of the built-in modules are well tested to be serializable during the snapshot building process. The Node.js core test suite checks that a few fairly complex applications can be snapshotted. The list of built-in modules being [`v8.startupSnapshot.setDeserializeMainFunction()`](https://nodejs.org/docs/latest/api/v8.html#v8startupsnapshotsetdeserializemainfunctioncallback-data) or [`v8.startupSnapshot.addDeserializeCallback()`](https://nodejs.org/docs/latest/api/v8.html#v8startupsnapshotadddeserializecallbackcallback-data). If serialization for an additional module during the snapshot building process is needed, please file a request in the
####  `--build-snapshot-config`[#](https://nodejs.org/docs/latest/api/cli.html#build-snapshot-config)
Added in: v21.6.0, v20.12.0History Version | Changes
---|---
v25.4.0 | The snapshot building process is no longer experimental.
Specifies the path to a JSON configuration file which configures snapshot creation behavior.
The following options are currently supported:
  * `builder` [`--build-snapshot`](https://nodejs.org/docs/latest/api/cli.html#--build-snapshot) had been passed with `builder` as the main script name.
  * `withoutCodeCache`


When using this flag, additional script files provided on the command line will not be executed and instead be interpreted as regular command line arguments.
####  `-c`, `--check`[#](https://nodejs.org/docs/latest/api/cli.html#c-check)
Added in: v5.0.0, v4.2.0History Version | Changes
---|---
v10.0.0 | The `--require` option is now supported when checking a file.
Syntax check the script without executing.
####  `--completion-bash`[#](https://nodejs.org/docs/latest/api/cli.html#completion-bash)
Added in: v10.12.0
Print source-able bash completion script for Node.js.
```
node --completion-bash > node_bash_completion
source node_bash_completion
copy
```

####  `-C condition`, `--conditions=condition`[#](https://nodejs.org/docs/latest/api/cli.html#c-condition-conditionscondition)
Added in: v14.9.0, v12.19.0History Version | Changes
---|---
v22.9.0, v20.18.0 | The flag is no longer experimental.
Provide custom [conditional exports](https://nodejs.org/docs/latest/api/packages.html#conditional-exports) resolution conditions.
Any number of custom string condition names are permitted.
The default Node.js conditions of `"node"`, `"default"`, `"import"`, and `"require"` will always apply as defined.
For example, to run a module with "development" resolutions:
```
node -C development app.js
copy
```

####  `--cpu-prof`[#](https://nodejs.org/docs/latest/api/cli.html#cpu-prof)
Added in: v12.0.0History Version | Changes
---|---
v22.4.0, v20.16.0 | The `--cpu-prof` flags are now stable.
Starts the V8 CPU profiler on start up, and writes the CPU profile to disk before exit.
If `--cpu-prof-dir` is not specified, the generated profile is placed in the current working directory.
If `--cpu-prof-name` is not specified, the generated profile is named `CPU.${yyyymmdd}.${hhmmss}.${pid}.${tid}.${seq}.cpuprofile`.
```
$ node --cpu-prof index.js
$ ls *.cpuprofile
CPU.20190409.202950.15293.0.0.cpuprofile
copy
```

If `--cpu-prof-name` is specified, the provided value is used as a template for the file name. The following placeholder is supported and will be substituted at runtime:
  * `${pid}` — the current process ID

```
$ node --cpu-prof --cpu-prof-name 'CPU.${pid}.cpuprofile' index.js
$ ls *.cpuprofile
CPU.15293.cpuprofile
copy
```

####  `--cpu-prof-dir`[#](https://nodejs.org/docs/latest/api/cli.html#cpu-prof-dir)
Added in: v12.0.0History Version | Changes
---|---
v22.4.0, v20.16.0 | The `--cpu-prof` flags are now stable.
Specify the directory where the CPU profiles generated by `--cpu-prof` will be placed.
The default value is controlled by the [`--diagnostic-dir`](https://nodejs.org/docs/latest/api/cli.html#--diagnostic-dirdirectory) command-line option.
####  `--cpu-prof-interval`[#](https://nodejs.org/docs/latest/api/cli.html#cpu-prof-interval)
Added in: v12.2.0History Version | Changes
---|---
v22.4.0, v20.16.0 | The `--cpu-prof` flags are now stable.
Specify the sampling interval in microseconds for the CPU profiles generated by `--cpu-prof`. The default is 1000 microseconds.
####  `--cpu-prof-name`[#](https://nodejs.org/docs/latest/api/cli.html#cpu-prof-name)
Added in: v12.0.0History Version | Changes
---|---
v22.4.0, v20.16.0 | The `--cpu-prof` flags are now stable.
Specify the file name of the CPU profile generated by `--cpu-prof`.
####  `--diagnostic-dir=directory`[#](https://nodejs.org/docs/latest/api/cli.html#diagnostic-dirdirectory)
Set the directory to which all diagnostic output files are written. Defaults to current working directory.
Affects the default output directory of:
  * [`--cpu-prof-dir`](https://nodejs.org/docs/latest/api/cli.html#--cpu-prof-dir)
  * [`--heap-prof-dir`](https://nodejs.org/docs/latest/api/cli.html#--heap-prof-dir)
  * [`--redirect-warnings`](https://nodejs.org/docs/latest/api/cli.html#--redirect-warningsfile)


####  `--disable-proto=mode`[#](https://nodejs.org/docs/latest/api/cli.html#disable-protomode)
Added in: v13.12.0, v12.17.0
Disable the `Object.prototype.__proto__` property. If `mode` is `delete`, the property is removed entirely. If `mode` is `throw`, accesses to the property throw an exception with the code `ERR_PROTO_ACCESS`.
####  `--disable-sigusr1`[#](https://nodejs.org/docs/latest/api/cli.html#disable-sigusr1)
Added in: v23.7.0, v22.14.0History Version | Changes
---|---
v24.8.0, v22.20.0 | The option is no longer experimental.
Disable the ability of starting a debugging session by sending a `SIGUSR1` signal to the process.
####  `--disable-warning=code-or-type`[#](https://nodejs.org/docs/latest/api/cli.html#disable-warningcode-or-type)
Added in: v21.3.0, v20.11.0
Stability: 1.1 - Active development
Disable specific process warnings by `code` or `type`.
Warnings emitted from [`process.emitWarning()`](https://nodejs.org/docs/latest/api/process.html#processemitwarningwarning-options) may contain a `code` and a `type`. This option will not-emit warnings that have a matching `code` or `type`.
List of [deprecation warnings](https://nodejs.org/docs/latest/api/deprecations.html#list-of-deprecated-apis).
The Node.js core warning types are: `DeprecationWarning` and `ExperimentalWarning`
For example, the following script will not emit [DEP0025 `require('node:sys')`](https://nodejs.org/docs/latest/api/deprecations.html#dep0025-requirenodesys) when executed with `node --disable-warning=DEP0025`:
```
import sys from 'node:sys';
const sys = require('node:sys');
copy
```

For example, the following script will emit the [DEP0025 `require('node:sys')`](https://nodejs.org/docs/latest/api/deprecations.html#dep0025-requirenodesys), but not any Experimental Warnings (such as [ExperimentalWarning: `vm.measureMemory` is an experimental feature](https://nodejs.org/docs/latest/api/vm.html#vmmeasurememoryoptions) in <=v21) when executed with `node --disable-warning=ExperimentalWarning`:
```
import sys from 'node:sys';
import vm from 'node:vm';

vm.measureMemory();
const sys = require('node:sys');
const vm = require('node:vm');

vm.measureMemory();
copy
```

####  `--disable-wasm-trap-handler`[#](https://nodejs.org/docs/latest/api/cli.html#disable-wasm-trap-handler)
Added in: v22.2.0, v20.15.0
By default, Node.js enables trap-handler-based WebAssembly bound checks. As a result, V8 does not need to insert inline bound checks in the code compiled from WebAssembly which may speed up WebAssembly execution significantly, but this optimization requires allocating a big virtual memory cage (currently 10GB). If the Node.js process does not have access to a large enough virtual memory address space due to system configurations or hardware limitations, users won't be able to run any WebAssembly that involves allocation in this virtual memory cage and will see an out-of-memory error.
```
$ ulimit -v 5000000
$ node -p "new WebAssembly.Memory({ initial: 10, maximum: 100 });"
[eval]:1
new WebAssembly.Memory({ initial: 10, maximum: 100 });
^

RangeError: WebAssembly.Memory(): could not allocate memory
    at [eval]:1:1
    at runScriptInThisContext (node:internal/vm:209:10)
    at node:internal/process/execution:118:14
    at [eval]-wrapper:6:24
    at runScript (node:internal/process/execution:101:62)
    at evalScript (node:internal/process/execution:136:3)
    at node:internal/main/eval_string:49:3

copy
```

`--disable-wasm-trap-handler` disables this optimization so that users can at least run WebAssembly (with less optimal performance) when the virtual memory address space available to their Node.js process is lower than what the V8 WebAssembly memory cage needs.
####  `--disallow-code-generation-from-strings`[#](https://nodejs.org/docs/latest/api/cli.html#disallow-code-generation-from-strings)
Added in: v9.8.0
Make built-in language features like `eval` and `new Function` that generate code from strings throw an exception instead. This does not affect the Node.js `node:vm` module.
####  `--dns-result-order=order`[#](https://nodejs.org/docs/latest/api/cli.html#dns-result-orderorder)
Added in: v16.4.0, v14.18.0History Version | Changes
---|---
v22.1.0, v20.13.0 | The `ipv6first` is supported now.
v17.0.0 | Changed default value to `verbatim`.
Set the default value of `order` in [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) and [`dnsPromises.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnspromiseslookuphostname-options). The value could be:
  * `ipv4first`: sets default `order` to `ipv4first`.
  * `ipv6first`: sets default `order` to `ipv6first`.
  * `verbatim`: sets default `order` to `verbatim`.


The default is `verbatim` and [`dns.setDefaultResultOrder()`](https://nodejs.org/docs/latest/api/dns.html#dnssetdefaultresultorderorder) have higher priority than `--dns-result-order`.
####  `--enable-fips`[#](https://nodejs.org/docs/latest/api/cli.html#enable-fips)
Added in: v6.0.0
Enable FIPS-compliant crypto at startup. (Requires Node.js to be built against FIPS-compatible OpenSSL.)
####  `--enable-source-maps`[#](https://nodejs.org/docs/latest/api/cli.html#enable-source-maps)
Added in: v12.12.0History Version | Changes
---|---
