Added in: v18.8.0
Stability: 1 - Experimental
When used with `--build-snapshot`, `--snapshot-blob` specifies the path where the generated snapshot blob is written to. If not specified, the generated blob is written to `snapshot.blob` in the current working directory.
When used without `--build-snapshot`, `--snapshot-blob` specifies the path to the blob that is used to restore the application state.
When loading a snapshot, Node.js checks that:
  1. The version, architecture, and platform of the running Node.js binary are exactly the same as that of the binary that generates the snapshot.
  2. The V8 flags and CPU features are compatible with that of the binary that generates the snapshot.


If they don't match, Node.js refuses to load the snapshot and exits with status code 1.
####  `--test`[#](https://nodejs.org/docs/latest/api/cli.html#test)
Added in: v18.1.0, v16.17.0History Version | Changes
---|---
v20.0.0 | The test runner is now stable.
v19.2.0, v18.13.0 | Test runner now supports running in watch mode.
Starts the Node.js command line test runner. This flag cannot be combined with `--watch-path`, `--check`, `--eval`, `--interactive`, or the inspector. See the documentation on [running tests from the command line](https://nodejs.org/docs/latest/api/test.html#running-tests-from-the-command-line) for more details.
####  `--test-concurrency`[#](https://nodejs.org/docs/latest/api/cli.html#test-concurrency)
Added in: v21.0.0, v20.10.0, v18.19.0
The maximum number of test files that the test runner CLI will execute concurrently. If `--test-isolation` is set to `'none'`, this flag is ignored and concurrency is one. Otherwise, concurrency defaults to `os.availableParallelism() - 1`.
####  `--test-coverage-branches=threshold`[#](https://nodejs.org/docs/latest/api/cli.html#test-coverage-branchesthreshold)
Added in: v22.8.0
Stability: 1 - Experimental
Require a minimum percent of covered branches. If code coverage does not reach the threshold specified, the process will exit with code `1`.
####  `--test-coverage-exclude`[#](https://nodejs.org/docs/latest/api/cli.html#test-coverage-exclude)
Added in: v22.5.0
Stability: 1 - Experimental
Excludes specific files from code coverage using a glob pattern, which can match both absolute and relative file paths.
This option may be specified multiple times to exclude multiple glob patterns.
If both `--test-coverage-exclude` and `--test-coverage-include` are provided, files must meet **both** criteria to be included in the coverage report.
By default all the matching test files are excluded from the coverage report. Specifying this option will override the default behavior.
####  `--test-coverage-functions=threshold`[#](https://nodejs.org/docs/latest/api/cli.html#test-coverage-functionsthreshold)
Added in: v22.8.0
Stability: 1 - Experimental
Require a minimum percent of covered functions. If code coverage does not reach the threshold specified, the process will exit with code `1`.
####  `--test-coverage-include`[#](https://nodejs.org/docs/latest/api/cli.html#test-coverage-include)
Added in: v22.5.0
Stability: 1 - Experimental
Includes specific files in code coverage using a glob pattern, which can match both absolute and relative file paths.
This option may be specified multiple times to include multiple glob patterns.
If both `--test-coverage-exclude` and `--test-coverage-include` are provided, files must meet **both** criteria to be included in the coverage report.
####  `--test-coverage-lines=threshold`[#](https://nodejs.org/docs/latest/api/cli.html#test-coverage-linesthreshold)
Added in: v22.8.0
Stability: 1 - Experimental
Require a minimum percent of covered lines. If code coverage does not reach the threshold specified, the process will exit with code `1`.
####  `--test-force-exit`[#](https://nodejs.org/docs/latest/api/cli.html#test-force-exit)
Added in: v22.0.0, v20.14.0
Configures the test runner to exit the process once all known tests have finished executing even if the event loop would otherwise remain active.
####  `--test-global-setup=module`[#](https://nodejs.org/docs/latest/api/cli.html#test-global-setupmodule)
Added in: v24.0.0
Stability: 1.0 - Early development
Specify a module that will be evaluated before all tests are executed and can be used to setup global state or fixtures for tests.
See the documentation on [global setup and teardown](https://nodejs.org/docs/latest/api/test.html#global-setup-and-teardown) for more details.
####  `--test-isolation=mode`[#](https://nodejs.org/docs/latest/api/cli.html#test-isolationmode)
Added in: v22.8.0History Version | Changes
---|---
v23.6.0 | This flag was renamed from `--experimental-test-isolation` to `--test-isolation`.
Configures the type of test isolation used in the test runner. When `mode` is `'process'`, each test file is run in a separate child process. When `mode` is `'none'`, all test files run in the same process as the test runner. The default isolation mode is `'process'`. This flag is ignored if the `--test` flag is not present. See the [test runner execution model](https://nodejs.org/docs/latest/api/test.html#test-runner-execution-model) section for more information.
####  `--test-name-pattern`[#](https://nodejs.org/docs/latest/api/cli.html#test-name-pattern)
Added in: v18.11.0History Version | Changes
---|---
v20.0.0 | The test runner is now stable.
A regular expression that configures the test runner to only execute tests whose name matches the provided pattern. See the documentation on [filtering tests by name](https://nodejs.org/docs/latest/api/test.html#filtering-tests-by-name) for more details.
If both `--test-name-pattern` and `--test-skip-pattern` are supplied, tests must satisfy **both** requirements in order to be executed.
####  `--test-only`[#](https://nodejs.org/docs/latest/api/cli.html#test-only)
Added in: v18.0.0, v16.17.0History Version | Changes
---|---
v20.0.0 | The test runner is now stable.
Configures the test runner to only execute top level tests that have the `only` option set. This flag is not necessary when test isolation is disabled.
####  `--test-reporter`[#](https://nodejs.org/docs/latest/api/cli.html#test-reporter)
Added in: v19.6.0, v18.15.0History Version | Changes
---|---
v20.0.0 | The test runner is now stable.
A test reporter to use when running tests. See the documentation on [test reporters](https://nodejs.org/docs/latest/api/test.html#test-reporters) for more details.
####  `--test-reporter-destination`[#](https://nodejs.org/docs/latest/api/cli.html#test-reporter-destination)
Added in: v19.6.0, v18.15.0History Version | Changes
---|---
v20.0.0 | The test runner is now stable.
The destination for the corresponding test reporter. See the documentation on [test reporters](https://nodejs.org/docs/latest/api/test.html#test-reporters) for more details.
####  `--test-rerun-failures`[#](https://nodejs.org/docs/latest/api/cli.html#test-rerun-failures)
Added in: v24.7.0
A path to a file allowing the test runner to persist the state of the test suite between runs. The test runner will use this file to determine which tests have already succeeded or failed, allowing for re-running of failed tests without having to re-run the entire test suite. The test runner will create this file if it does not exist. See the documentation on [test reruns](https://nodejs.org/docs/latest/api/test.html#rerunning-failed-tests) for more details.
####  `--test-shard`[#](https://nodejs.org/docs/latest/api/cli.html#test-shard)
Added in: v20.5.0, v18.19.0
Test suite shard to execute in a format of `<index>/<total>`, where
  * `index` is a positive integer, index of divided parts.
  * `total` is a positive integer, total of divided part.


This command will divide all tests files into `total` equal parts, and will run only those that happen to be in an `index` part.
For example, to split your tests suite into three parts, use this:
```
node --test --test-shard=1/3
node --test --test-shard=2/3
node --test --test-shard=3/3
copy
```

####  `--test-skip-pattern`[#](https://nodejs.org/docs/latest/api/cli.html#test-skip-pattern)
Added in: v22.1.0
A regular expression that configures the test runner to skip tests whose name matches the provided pattern. See the documentation on [filtering tests by name](https://nodejs.org/docs/latest/api/test.html#filtering-tests-by-name) for more details.
If both `--test-name-pattern` and `--test-skip-pattern` are supplied, tests must satisfy **both** requirements in order to be executed.
####  `--test-timeout`[#](https://nodejs.org/docs/latest/api/cli.html#test-timeout)
Added in: v21.2.0, v20.11.0
A number of milliseconds the test execution will fail after. If unspecified, subtests inherit this value from their parent. The default value is `Infinity`.
####  `--test-update-snapshots`[#](https://nodejs.org/docs/latest/api/cli.html#test-update-snapshots)
Added in: v22.3.0History Version | Changes
---|---
v23.4.0, v22.13.0 | Snapshot testing is no longer experimental.
Regenerates the snapshot files used by the test runner for [snapshot testing](https://nodejs.org/docs/latest/api/test.html#snapshot-testing).
####  `--throw-deprecation`[#](https://nodejs.org/docs/latest/api/cli.html#throw-deprecation)
Added in: v0.11.14
Throw errors for deprecations.
####  `--title=title`[#](https://nodejs.org/docs/latest/api/cli.html#titletitle)
Added in: v10.7.0
Set `process.title` on startup.
####  `--tls-cipher-list=list`[#](https://nodejs.org/docs/latest/api/cli.html#tls-cipher-listlist)
Added in: v4.0.0
Specify an alternative default TLS cipher list. Requires Node.js to be built with crypto support (default).
####  `--tls-keylog=file`[#](https://nodejs.org/docs/latest/api/cli.html#tls-keylogfile)
Added in: v13.2.0, v12.16.0
Log TLS key material to a file. The key material is in NSS `SSLKEYLOGFILE` format and can be used by software (such as Wireshark) to decrypt the TLS traffic.
####  `--tls-max-v1.2`[#](https://nodejs.org/docs/latest/api/cli.html#tls-max-v12)
Added in: v12.0.0, v10.20.0
Set [`tls.DEFAULT_MAX_VERSION`](https://nodejs.org/docs/latest/api/tls.html#tlsdefault_max_version) to 'TLSv1.2'. Use to disable support for TLSv1.3.
####  `--tls-max-v1.3`[#](https://nodejs.org/docs/latest/api/cli.html#tls-max-v13)
Added in: v12.0.0
Set default [`tls.DEFAULT_MAX_VERSION`](https://nodejs.org/docs/latest/api/tls.html#tlsdefault_max_version) to 'TLSv1.3'. Use to enable support for TLSv1.3.
####  `--tls-min-v1.0`[#](https://nodejs.org/docs/latest/api/cli.html#tls-min-v10)
Added in: v12.0.0, v10.20.0
Set default [`tls.DEFAULT_MIN_VERSION`](https://nodejs.org/docs/latest/api/tls.html#tlsdefault_min_version) to 'TLSv1'. Use for compatibility with old TLS clients or servers.
####  `--tls-min-v1.1`[#](https://nodejs.org/docs/latest/api/cli.html#tls-min-v11)
Added in: v12.0.0, v10.20.0
Set default [`tls.DEFAULT_MIN_VERSION`](https://nodejs.org/docs/latest/api/tls.html#tlsdefault_min_version) to 'TLSv1.1'. Use for compatibility with old TLS clients or servers.
####  `--tls-min-v1.2`[#](https://nodejs.org/docs/latest/api/cli.html#tls-min-v12)
Added in: v12.2.0, v10.20.0
Set default [`tls.DEFAULT_MIN_VERSION`](https://nodejs.org/docs/latest/api/tls.html#tlsdefault_min_version) to 'TLSv1.2'. This is the default for 12.x and later, but the option is supported for compatibility with older Node.js versions.
####  `--tls-min-v1.3`[#](https://nodejs.org/docs/latest/api/cli.html#tls-min-v13)
Added in: v12.0.0
Set default [`tls.DEFAULT_MIN_VERSION`](https://nodejs.org/docs/latest/api/tls.html#tlsdefault_min_version) to 'TLSv1.3'. Use to disable support for TLSv1.2, which is not as secure as TLSv1.3.
####  `--trace-deprecation`[#](https://nodejs.org/docs/latest/api/cli.html#trace-deprecation)
Added in: v0.8.0
Print stack traces for deprecations.
####  `--trace-env`[#](https://nodejs.org/docs/latest/api/cli.html#trace-env)
Added in: v23.4.0, v22.13.0
Print information about any access to environment variables done in the current Node.js instance to stderr, including:
  * The environment variable reads that Node.js does internally.
  * Writes in the form of `process.env.KEY = "SOME VALUE"`.
  * Reads in the form of `process.env.KEY`.
  * Definitions in the form of `Object.defineProperty(process.env, 'KEY', {...})`.
  * Queries in the form of `Object.hasOwn(process.env, 'KEY')`, `process.env.hasOwnProperty('KEY')` or `'KEY' in process.env`.
  * Deletions in the form of `delete process.env.KEY`.
  * Enumerations inf the form of `...process.env` or `Object.keys(process.env)`.


Only the names of the environment variables being accessed are printed. The values are not printed.
To print the stack trace of the access, use `--trace-env-js-stack` and/or `--trace-env-native-stack`.
####  `--trace-env-js-stack`[#](https://nodejs.org/docs/latest/api/cli.html#trace-env-js-stack)
Added in: v23.4.0, v22.13.0
In addition to what `--trace-env` does, this prints the JavaScript stack trace of the access.
####  `--trace-env-native-stack`[#](https://nodejs.org/docs/latest/api/cli.html#trace-env-native-stack)
Added in: v23.4.0, v22.13.0
In addition to what `--trace-env` does, this prints the native stack trace of the access.
####  `--trace-event-categories`[#](https://nodejs.org/docs/latest/api/cli.html#trace-event-categories)
Added in: v7.7.0
A comma separated list of categories that should be traced when trace event tracing is enabled using `--trace-events-enabled`.
####  `--trace-event-file-pattern`[#](https://nodejs.org/docs/latest/api/cli.html#trace-event-file-pattern)
Added in: v9.8.0
Template string specifying the filepath for the trace event data, it supports `${rotation}` and `${pid}`.
####  `--trace-events-enabled`[#](https://nodejs.org/docs/latest/api/cli.html#trace-events-enabled)
Added in: v7.7.0
Enables the collection of trace event tracing information.
####  `--trace-exit`[#](https://nodejs.org/docs/latest/api/cli.html#trace-exit)
Added in: v13.5.0, v12.16.0
Prints a stack trace whenever an environment is exited proactively, i.e. invoking `process.exit()`.
####  `--trace-require-module=mode`[#](https://nodejs.org/docs/latest/api/cli.html#trace-require-modulemode)
Added in: v23.5.0, v22.13.0, v20.19.0
Prints information about usage of [Loading ECMAScript modules using `require()`](https://nodejs.org/docs/latest/api/modules.html#loading-ecmascript-modules-using-require).
When `mode` is `all`, all usage is printed. When `mode` is `no-node-modules`, usage from the `node_modules` folder is excluded.
####  `--trace-sigint`[#](https://nodejs.org/docs/latest/api/cli.html#trace-sigint)
Added in: v13.9.0, v12.17.0
Prints a stack trace on SIGINT.
####  `--trace-sync-io`[#](https://nodejs.org/docs/latest/api/cli.html#trace-sync-io)
Added in: v2.1.0
Prints a stack trace whenever synchronous I/O is detected after the first turn of the event loop.
####  `--trace-tls`[#](https://nodejs.org/docs/latest/api/cli.html#trace-tls)
Added in: v12.2.0
Prints TLS packet trace information to `stderr`. This can be used to debug TLS connection problems.
####  `--trace-uncaught`[#](https://nodejs.org/docs/latest/api/cli.html#trace-uncaught)
Added in: v13.1.0
Print stack traces for uncaught exceptions; usually, the stack trace associated with the creation of an `Error` is printed, whereas this makes Node.js also print the stack trace associated with throwing the value (which does not need to be an `Error` instance).
Enabling this option may affect garbage collection behavior negatively.
####  `--trace-warnings`[#](https://nodejs.org/docs/latest/api/cli.html#trace-warnings)
Added in: v6.0.0
Print stack traces for process warnings (including deprecations).
####  `--track-heap-objects`[#](https://nodejs.org/docs/latest/api/cli.html#track-heap-objects)
Added in: v2.4.0
Track heap object allocations for heap snapshots.
####  `--unhandled-rejections=mode`[#](https://nodejs.org/docs/latest/api/cli.html#unhandled-rejectionsmode)
Added in: v12.0.0, v10.17.0History Version | Changes
---|---
v15.0.0 | Changed default mode to `throw`. Previously, a warning was emitted.
Using this flag allows to change what should happen when an unhandled rejection occurs. One of the following modes can be chosen:
  * `throw`: Emit [`unhandledRejection`](https://nodejs.org/docs/latest/api/process.html#event-unhandledrejection). If this hook is not set, raise the unhandled rejection as an uncaught exception. This is the default.
  * `strict`: Raise the unhandled rejection as an uncaught exception. If the exception is handled, [`unhandledRejection`](https://nodejs.org/docs/latest/api/process.html#event-unhandledrejection) is emitted.
  * `warn`: Always trigger a warning, no matter if the [`unhandledRejection`](https://nodejs.org/docs/latest/api/process.html#event-unhandledrejection) hook is set or not but do not print the deprecation warning.
  * `warn-with-error-code`: Emit [`unhandledRejection`](https://nodejs.org/docs/latest/api/process.html#event-unhandledrejection). If this hook is not set, trigger a warning, and set the process exit code to 1.
  * `none`: Silence all warnings.


If a rejection happens during the command line entry point's ES module static loading phase, it will always raise it as an uncaught exception.
####  `--use-bundled-ca`, `--use-openssl-ca`[#](https://nodejs.org/docs/latest/api/cli.html#use-bundled-ca-use-openssl-ca)
Added in: v6.11.0
Use bundled Mozilla CA store as supplied by current Node.js version or use OpenSSL's default CA store. The default store is selectable at build-time.
The bundled CA store, as supplied by Node.js, is a snapshot of Mozilla CA store that is fixed at release time. It is identical on all supported platforms.
Using OpenSSL store allows for external modifications of the store. For most Linux and BSD distributions, this store is maintained by the distribution maintainers and system administrators. OpenSSL CA store location is dependent on configuration of the OpenSSL library but this can be altered at runtime using environment variables.
See `SSL_CERT_DIR` and `SSL_CERT_FILE`.
####  `--use-env-proxy`[#](https://nodejs.org/docs/latest/api/cli.html#use-env-proxy)
Added in: v24.5.0
Stability: 1.1 - Active Development
When enabled, Node.js parses the `HTTP_PROXY`, `HTTPS_PROXY` and `NO_PROXY` environment variables during startup, and tunnels requests over the specified proxy.
This is equivalent to setting the [`NODE_USE_ENV_PROXY=1`](https://nodejs.org/docs/latest/api/cli.html#node_use_env_proxy1) environment variable. When both are set, `--use-env-proxy` takes precedence.
####  `--use-largepages=mode`[#](https://nodejs.org/docs/latest/api/cli.html#use-largepagesmode)
Added in: v13.6.0, v12.17.0
Re-map the Node.js static code to large memory pages at startup. If supported on the target system, this will cause the Node.js static code to be moved onto 2 MiB pages instead of 4 KiB pages.
The following values are valid for `mode`:
  * `off`: No mapping will be attempted. This is the default.
  * `on`: If supported by the OS, mapping will be attempted. Failure to map will be ignored and a message will be printed to standard error.
  * `silent`: If supported by the OS, mapping will be attempted. Failure to map will be ignored and will not be reported.


####  `--use-system-ca`[#](https://nodejs.org/docs/latest/api/cli.html#use-system-ca)
Added in: v23.8.0History Version | Changes
---|---
v23.9.0 | Added support on non-Windows and non-macOS.
Node.js uses the trusted CA certificates present in the system store along with the `--use-bundled-ca` option and the `NODE_EXTRA_CA_CERTS` environment variable. On platforms other than Windows and macOS, this loads certificates from the directory and file trusted by OpenSSL, similar to `--use-openssl-ca`, with the difference being that it caches the certificates after first load.
On Windows and macOS, the certificate trust policy is similar to
On macOS, the following settings are respected:
  * Default and System Keychains
    * Trust:
      * Any certificate where the “When using this certificate” flag is set to “Always Trust” or
      * Any certificate where the “Secure Sockets Layer (SSL)” flag is set to “Always Trust”.
    * The certificate must also be valid, with "X.509 Basic Policy" set to “Always Trust”.


On Windows, the following settings are respected:
  * Local Machine (accessed via `certlm.msc`)
    * Trust:
      * Trusted Root Certification Authorities
      * Trusted People
      * Enterprise Trust -> Enterprise -> Trusted Root Certification Authorities
      * Enterprise Trust -> Enterprise -> Trusted People
      * Enterprise Trust -> Group Policy -> Trusted Root Certification Authorities
      * Enterprise Trust -> Group Policy -> Trusted People
  * Current User (accessed via `certmgr.msc`)
    * Trust:
      * Trusted Root Certification Authorities
      * Enterprise Trust -> Group Policy -> Trusted Root Certification Authorities


On Windows and macOS, Node.js would check that the user settings for the trusted certificates do not forbid them for TLS server authentication before using them.
Node.js currently does not support distrust/revocation of certificates from another source based on system settings.
On other systems, Node.js loads certificates from the default certificate file (typically `/etc/ssl/cert.pem`) and default certificate directory (typically `/etc/ssl/certs`) that the version of OpenSSL that Node.js links to respects. This typically works with the convention on major Linux distributions and other Unix-like systems. If the overriding OpenSSL environment variables (typically `SSL_CERT_FILE` and `SSL_CERT_DIR`, depending on the configuration of the OpenSSL that Node.js links to) are set, the specified paths will be used to load certificates instead. These environment variables can be used as workarounds if the conventional paths used by the version of OpenSSL Node.js links to are not consistent with the system configuration that the users have for some reason.
####  `--v8-options`[#](https://nodejs.org/docs/latest/api/cli.html#v8-options)
Added in: v0.1.3
Print V8 command-line options.
####  `--v8-pool-size=num`[#](https://nodejs.org/docs/latest/api/cli.html#v8-pool-sizenum)
Added in: v5.10.0
Set V8's thread pool size which will be used to allocate background jobs.
If set to `0` then Node.js will choose an appropriate size of the thread pool based on an estimate of the amount of parallelism.
The amount of parallelism refers to the number of computations that can be carried out simultaneously in a given machine. In general, it's the same as the amount of CPUs, but it may diverge in environments such as VMs or containers.
####  `-v`, `--version`[#](https://nodejs.org/docs/latest/api/cli.html#v-version)
Added in: v0.1.3
Print node's version.
####  `--watch`[#](https://nodejs.org/docs/latest/api/cli.html#watch)
Added in: v18.11.0, v16.19.0History Version | Changes
---|---
v22.0.0, v20.13.0 | Watch mode is now stable.
v19.2.0, v18.13.0 | Test runner now supports running in watch mode.
Starts Node.js in watch mode. When in watch mode, changes in the watched files cause the Node.js process to restart. By default, watch mode will watch the entry point and any required or imported module. Use `--watch-path` to specify what paths to watch.
This flag cannot be combined with `--check`, `--eval`, `--interactive`, or the REPL.
Note: The `--watch` flag requires a file path as an argument and is incompatible with `--run` or inline script input, as `--run` takes precedence and ignores watch mode. If no file is provided, Node.js will exit with status code `9`.
```
node --watch index.js
copy
```

####  `--watch-kill-signal`[#](https://nodejs.org/docs/latest/api/cli.html#watch-kill-signal)
Added in: v24.4.0, v22.18.0
Stability: 1.1 - Active Development
Customizes the signal sent to the process on watch mode restarts.
```
node --watch --watch-kill-signal SIGINT test.js
copy
```

####  `--watch-path`[#](https://nodejs.org/docs/latest/api/cli.html#watch-path)
Added in: v18.11.0, v16.19.0History Version | Changes
---|---
v22.0.0, v20.13.0 | Watch mode is now stable.
Starts Node.js in watch mode and specifies what paths to watch. When in watch mode, changes in the watched paths cause the Node.js process to restart. This will turn off watching of required or imported modules, even when used in combination with `--watch`.
This flag cannot be combined with `--check`, `--eval`, `--interactive`, `--test`, or the REPL.
Note: Using `--watch-path` implicitly enables `--watch`, which requires a file path and is incompatible with `--run`, as `--run` takes precedence and ignores watch mode.
```
node --watch-path=./src --watch-path=./tests index.js
copy
```

This option is only supported on macOS and Windows. An `ERR_FEATURE_UNAVAILABLE_ON_PLATFORM` exception will be thrown when the option is used on a platform that does not support it.
####  `--watch-preserve-output`[#](https://nodejs.org/docs/latest/api/cli.html#watch-preserve-output)
Added in: v19.3.0, v18.13.0
Disable the clearing of the console when watch mode restarts the process.
```
node --watch --watch-preserve-output test.js
copy
```

####  `--zero-fill-buffers`[#](https://nodejs.org/docs/latest/api/cli.html#zero-fill-buffers)
Added in: v6.0.0
Automatically zero-fills all newly allocated [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) instances.
### Environment variables[#](https://nodejs.org/docs/latest/api/cli.html#environment-variables-1)
Stability: 2 - Stable
####  `FORCE_COLOR=[1, 2, 3]`[#](https://nodejs.org/docs/latest/api/cli.html#force-color1-2-3)
