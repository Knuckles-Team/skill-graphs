[Skip to content](https://nodejs.org/docs/latest/api/console.html#apicontent)
[ Node.js ](https://nodejs.org/ "Go back to the home page")
* * *
  * [About this documentation](https://nodejs.org/docs/latest/api/documentation.html)
  * [Usage and example](https://nodejs.org/docs/latest/api/synopsis.html)
  * [Assertion testing](https://nodejs.org/docs/latest/api/assert.html)
  * [Asynchronous context tracking](https://nodejs.org/docs/latest/api/async_context.html)
  * [Async hooks](https://nodejs.org/docs/latest/api/async_hooks.html)
  * [Buffer](https://nodejs.org/docs/latest/api/buffer.html)
  * [C++ addons](https://nodejs.org/docs/latest/api/addons.html)
  * [C/C++ addons with Node-API](https://nodejs.org/docs/latest/api/n-api.html)
  * [C++ embedder API](https://nodejs.org/docs/latest/api/embedding.html)
  * [Child processes](https://nodejs.org/docs/latest/api/child_process.html)
  * [Cluster](https://nodejs.org/docs/latest/api/cluster.html)
  * [Command-line options](https://nodejs.org/docs/latest/api/cli.html)
  * [Console](https://nodejs.org/docs/latest/api/console.html)
  * [Crypto](https://nodejs.org/docs/latest/api/crypto.html)
  * [Debugger](https://nodejs.org/docs/latest/api/debugger.html)
  * [Deprecated APIs](https://nodejs.org/docs/latest/api/deprecations.html)
  * [Diagnostics Channel](https://nodejs.org/docs/latest/api/diagnostics_channel.html)
  * [DNS](https://nodejs.org/docs/latest/api/dns.html)
  * [Domain](https://nodejs.org/docs/latest/api/domain.html)
  * [Environment Variables](https://nodejs.org/docs/latest/api/environment_variables.html)
  * [Errors](https://nodejs.org/docs/latest/api/errors.html)
  * [Events](https://nodejs.org/docs/latest/api/events.html)
  * [File system](https://nodejs.org/docs/latest/api/fs.html)
  * [Globals](https://nodejs.org/docs/latest/api/globals.html)
  * [HTTP](https://nodejs.org/docs/latest/api/http.html)
  * [HTTP/2](https://nodejs.org/docs/latest/api/http2.html)
  * [HTTPS](https://nodejs.org/docs/latest/api/https.html)
  * [Inspector](https://nodejs.org/docs/latest/api/inspector.html)
  * [Internationalization](https://nodejs.org/docs/latest/api/intl.html)
  * [Modules: CommonJS modules](https://nodejs.org/docs/latest/api/modules.html)
  * [Modules: ECMAScript modules](https://nodejs.org/docs/latest/api/esm.html)
  * [Modules: `node:module` API](https://nodejs.org/docs/latest/api/module.html)
  * [Modules: Packages](https://nodejs.org/docs/latest/api/packages.html)
  * [Modules: TypeScript](https://nodejs.org/docs/latest/api/typescript.html)
  * [Net](https://nodejs.org/docs/latest/api/net.html)
  * [OS](https://nodejs.org/docs/latest/api/os.html)
  * [Path](https://nodejs.org/docs/latest/api/path.html)
  * [Performance hooks](https://nodejs.org/docs/latest/api/perf_hooks.html)
  * [Permissions](https://nodejs.org/docs/latest/api/permissions.html)
  * [Process](https://nodejs.org/docs/latest/api/process.html)
  * [Punycode](https://nodejs.org/docs/latest/api/punycode.html)
  * [Query strings](https://nodejs.org/docs/latest/api/querystring.html)
  * [Readline](https://nodejs.org/docs/latest/api/readline.html)
  * [REPL](https://nodejs.org/docs/latest/api/repl.html)
  * [Report](https://nodejs.org/docs/latest/api/report.html)
  * [Single executable applications](https://nodejs.org/docs/latest/api/single-executable-applications.html)
  * [SQLite](https://nodejs.org/docs/latest/api/sqlite.html)
  * [Stream](https://nodejs.org/docs/latest/api/stream.html)
  * [String decoder](https://nodejs.org/docs/latest/api/string_decoder.html)
  * [Test runner](https://nodejs.org/docs/latest/api/test.html)
  * [Timers](https://nodejs.org/docs/latest/api/timers.html)
  * [TLS/SSL](https://nodejs.org/docs/latest/api/tls.html)
  * [Trace events](https://nodejs.org/docs/latest/api/tracing.html)
  * [TTY](https://nodejs.org/docs/latest/api/tty.html)
  * [UDP/datagram](https://nodejs.org/docs/latest/api/dgram.html)
  * [URL](https://nodejs.org/docs/latest/api/url.html)
  * [Utilities](https://nodejs.org/docs/latest/api/util.html)
  * [V8](https://nodejs.org/docs/latest/api/v8.html)
  * [VM](https://nodejs.org/docs/latest/api/vm.html)
  * [WASI](https://nodejs.org/docs/latest/api/wasi.html)
  * [Web Crypto API](https://nodejs.org/docs/latest/api/webcrypto.html)
  * [Web Streams API](https://nodejs.org/docs/latest/api/webstreams.html)
  * [Worker threads](https://nodejs.org/docs/latest/api/worker_threads.html)
  * [Zlib](https://nodejs.org/docs/latest/api/zlib.html)


* * *
# Node.js v25.8.0 documentation
  * Node.js v25.8.0
  * [](https://nodejs.org/docs/latest/api/console.html#toc-picker)
    * [Console](https://nodejs.org/docs/latest/api/console.html#console)
      * [Class: `Console`](https://nodejs.org/docs/latest/api/console.html#class-console)
        * [`new Console(stdout[, stderr][, ignoreErrors])`](https://nodejs.org/docs/latest/api/console.html#new-consolestdout-stderr-ignoreerrors)
        * [`new Console(options)`](https://nodejs.org/docs/latest/api/console.html#new-consoleoptions)
        * [`console.assert(value[, ...message])`](https://nodejs.org/docs/latest/api/console.html#consoleassertvalue-message)
        * [`console.clear()`](https://nodejs.org/docs/latest/api/console.html#consoleclear)
        * [`console.count([label])`](https://nodejs.org/docs/latest/api/console.html#consolecountlabel)
        * [`console.countReset([label])`](https://nodejs.org/docs/latest/api/console.html#consolecountresetlabel)
        * [`console.debug(data[, ...args])`](https://nodejs.org/docs/latest/api/console.html#consoledebugdata-args)
        * [`console.dir(obj[, options])`](https://nodejs.org/docs/latest/api/console.html#consoledirobj-options)
        * [`console.dirxml(...data)`](https://nodejs.org/docs/latest/api/console.html#consoledirxmldata)
        * [`console.error([data][, ...args])`](https://nodejs.org/docs/latest/api/console.html#consoleerrordata-args)
        * [`console.group([...label])`](https://nodejs.org/docs/latest/api/console.html#consolegrouplabel)
        * [`console.groupCollapsed()`](https://nodejs.org/docs/latest/api/console.html#consolegroupcollapsed)
        * [`console.groupEnd()`](https://nodejs.org/docs/latest/api/console.html#consolegroupend)
        * [`console.info([data][, ...args])`](https://nodejs.org/docs/latest/api/console.html#consoleinfodata-args)
        * [`console.log([data][, ...args])`](https://nodejs.org/docs/latest/api/console.html#consolelogdata-args)
        * [`console.table(tabularData[, properties])`](https://nodejs.org/docs/latest/api/console.html#consoletabletabulardata-properties)
        * [`console.time([label])`](https://nodejs.org/docs/latest/api/console.html#consoletimelabel)
        * [`console.timeEnd([label])`](https://nodejs.org/docs/latest/api/console.html#consoletimeendlabel)
        * [`console.timeLog([label][, ...data])`](https://nodejs.org/docs/latest/api/console.html#consoletimeloglabel-data)
        * [`console.trace([message][, ...args])`](https://nodejs.org/docs/latest/api/console.html#consoletracemessage-args)
        * [`console.warn([data][, ...args])`](https://nodejs.org/docs/latest/api/console.html#consolewarndata-args)
      * [Inspector only methods](https://nodejs.org/docs/latest/api/console.html#inspector-only-methods)
        * [`console.profile([label])`](https://nodejs.org/docs/latest/api/console.html#consoleprofilelabel)
        * [`console.profileEnd([label])`](https://nodejs.org/docs/latest/api/console.html#consoleprofileendlabel)
        * [`console.timeStamp([label])`](https://nodejs.org/docs/latest/api/console.html#consoletimestamplabel)
  * [](https://nodejs.org/docs/latest/api/console.html#gtoc-picker)
    * [Index](https://nodejs.org/docs/latest/api/index.html)
* * *
    * [About this documentation](https://nodejs.org/docs/latest/api/documentation.html)
    * [Usage and example](https://nodejs.org/docs/latest/api/synopsis.html)
    * [Assertion testing](https://nodejs.org/docs/latest/api/assert.html)
    * [Asynchronous context tracking](https://nodejs.org/docs/latest/api/async_context.html)
    * [Async hooks](https://nodejs.org/docs/latest/api/async_hooks.html)
    * [Buffer](https://nodejs.org/docs/latest/api/buffer.html)
    * [C++ addons](https://nodejs.org/docs/latest/api/addons.html)
    * [C/C++ addons with Node-API](https://nodejs.org/docs/latest/api/n-api.html)
    * [C++ embedder API](https://nodejs.org/docs/latest/api/embedding.html)
    * [Child processes](https://nodejs.org/docs/latest/api/child_process.html)
    * [Cluster](https://nodejs.org/docs/latest/api/cluster.html)
    * [Command-line options](https://nodejs.org/docs/latest/api/cli.html)
    * [Console](https://nodejs.org/docs/latest/api/console.html)
    * [Crypto](https://nodejs.org/docs/latest/api/crypto.html)
    * [Debugger](https://nodejs.org/docs/latest/api/debugger.html)
    * [Deprecated APIs](https://nodejs.org/docs/latest/api/deprecations.html)
    * [Diagnostics Channel](https://nodejs.org/docs/latest/api/diagnostics_channel.html)
    * [DNS](https://nodejs.org/docs/latest/api/dns.html)
    * [Domain](https://nodejs.org/docs/latest/api/domain.html)
    * [Environment Variables](https://nodejs.org/docs/latest/api/environment_variables.html)
    * [Errors](https://nodejs.org/docs/latest/api/errors.html)
    * [Events](https://nodejs.org/docs/latest/api/events.html)
    * [File system](https://nodejs.org/docs/latest/api/fs.html)
    * [Globals](https://nodejs.org/docs/latest/api/globals.html)
    * [HTTP](https://nodejs.org/docs/latest/api/http.html)
    * [HTTP/2](https://nodejs.org/docs/latest/api/http2.html)
    * [HTTPS](https://nodejs.org/docs/latest/api/https.html)
    * [Inspector](https://nodejs.org/docs/latest/api/inspector.html)
    * [Internationalization](https://nodejs.org/docs/latest/api/intl.html)
    * [Modules: CommonJS modules](https://nodejs.org/docs/latest/api/modules.html)
    * [Modules: ECMAScript modules](https://nodejs.org/docs/latest/api/esm.html)
    * [Modules: `node:module` API](https://nodejs.org/docs/latest/api/module.html)
    * [Modules: Packages](https://nodejs.org/docs/latest/api/packages.html)
    * [Modules: TypeScript](https://nodejs.org/docs/latest/api/typescript.html)
    * [Net](https://nodejs.org/docs/latest/api/net.html)
    * [OS](https://nodejs.org/docs/latest/api/os.html)
    * [Path](https://nodejs.org/docs/latest/api/path.html)
    * [Performance hooks](https://nodejs.org/docs/latest/api/perf_hooks.html)
    * [Permissions](https://nodejs.org/docs/latest/api/permissions.html)
    * [Process](https://nodejs.org/docs/latest/api/process.html)
    * [Punycode](https://nodejs.org/docs/latest/api/punycode.html)
    * [Query strings](https://nodejs.org/docs/latest/api/querystring.html)
    * [Readline](https://nodejs.org/docs/latest/api/readline.html)
    * [REPL](https://nodejs.org/docs/latest/api/repl.html)
    * [Report](https://nodejs.org/docs/latest/api/report.html)
    * [Single executable applications](https://nodejs.org/docs/latest/api/single-executable-applications.html)
    * [SQLite](https://nodejs.org/docs/latest/api/sqlite.html)
    * [Stream](https://nodejs.org/docs/latest/api/stream.html)
    * [String decoder](https://nodejs.org/docs/latest/api/string_decoder.html)
    * [Test runner](https://nodejs.org/docs/latest/api/test.html)
    * [Timers](https://nodejs.org/docs/latest/api/timers.html)
    * [TLS/SSL](https://nodejs.org/docs/latest/api/tls.html)
    * [Trace events](https://nodejs.org/docs/latest/api/tracing.html)
    * [TTY](https://nodejs.org/docs/latest/api/tty.html)
    * [UDP/datagram](https://nodejs.org/docs/latest/api/dgram.html)
    * [URL](https://nodejs.org/docs/latest/api/url.html)
    * [Utilities](https://nodejs.org/docs/latest/api/util.html)
    * [V8](https://nodejs.org/docs/latest/api/v8.html)
    * [VM](https://nodejs.org/docs/latest/api/vm.html)
    * [WASI](https://nodejs.org/docs/latest/api/wasi.html)
    * [Web Crypto API](https://nodejs.org/docs/latest/api/webcrypto.html)
    * [Web Streams API](https://nodejs.org/docs/latest/api/webstreams.html)
    * [Worker threads](https://nodejs.org/docs/latest/api/worker_threads.html)
    * [Zlib](https://nodejs.org/docs/latest/api/zlib.html)
  * [](https://nodejs.org/docs/latest/api/console.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/console.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/console.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/console.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/console.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/console.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/console.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/console.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/console.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/console.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/console.html)
    11. [15.x ](https://nodejs.org/docs/latest-v15.x/api/console.html)
    12. [14.x ](https://nodejs.org/docs/latest-v14.x/api/console.html)
    13. [13.x ](https://nodejs.org/docs/latest-v13.x/api/console.html)
    14. [12.x ](https://nodejs.org/docs/latest-v12.x/api/console.html)
    15. [11.x ](https://nodejs.org/docs/latest-v11.x/api/console.html)
    16. [10.x ](https://nodejs.org/docs/latest-v10.x/api/console.html)
    17. [9.x ](https://nodejs.org/docs/latest-v9.x/api/console.html)
    18. [8.x ](https://nodejs.org/docs/latest-v8.x/api/console.html)
    19. [7.x ](https://nodejs.org/docs/latest-v7.x/api/console.html)
    20. [6.x ](https://nodejs.org/docs/latest-v6.x/api/console.html)
    21. [5.x ](https://nodejs.org/docs/latest-v5.x/api/console.html)
    22. [4.x ](https://nodejs.org/docs/latest-v4.x/api/console.html)
    23. [0.12.x ](https://nodejs.org/docs/latest-v0.12.x/api/console.html)
    24. [0.10.x ](https://nodejs.org/docs/latest-v0.10.x/api/console.html)
  * [ ](https://nodejs.org/docs/latest/api/console.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/console.json)


* * *
Table of contents
  * [Console](https://nodejs.org/docs/latest/api/console.html#console)
    * [Class: `Console`](https://nodejs.org/docs/latest/api/console.html#class-console)
      * [`new Console(stdout[, stderr][, ignoreErrors])`](https://nodejs.org/docs/latest/api/console.html#new-consolestdout-stderr-ignoreerrors)
      * [`new Console(options)`](https://nodejs.org/docs/latest/api/console.html#new-consoleoptions)
      * [`console.assert(value[, ...message])`](https://nodejs.org/docs/latest/api/console.html#consoleassertvalue-message)
      * [`console.clear()`](https://nodejs.org/docs/latest/api/console.html#consoleclear)
      * [`console.count([label])`](https://nodejs.org/docs/latest/api/console.html#consolecountlabel)
      * [`console.countReset([label])`](https://nodejs.org/docs/latest/api/console.html#consolecountresetlabel)
      * [`console.debug(data[, ...args])`](https://nodejs.org/docs/latest/api/console.html#consoledebugdata-args)
      * [`console.dir(obj[, options])`](https://nodejs.org/docs/latest/api/console.html#consoledirobj-options)
      * [`console.dirxml(...data)`](https://nodejs.org/docs/latest/api/console.html#consoledirxmldata)
      * [`console.error([data][, ...args])`](https://nodejs.org/docs/latest/api/console.html#consoleerrordata-args)
      * [`console.group([...label])`](https://nodejs.org/docs/latest/api/console.html#consolegrouplabel)
      * [`console.groupCollapsed()`](https://nodejs.org/docs/latest/api/console.html#consolegroupcollapsed)
      * [`console.groupEnd()`](https://nodejs.org/docs/latest/api/console.html#consolegroupend)
      * [`console.info([data][, ...args])`](https://nodejs.org/docs/latest/api/console.html#consoleinfodata-args)
      * [`console.log([data][, ...args])`](https://nodejs.org/docs/latest/api/console.html#consolelogdata-args)
      * [`console.table(tabularData[, properties])`](https://nodejs.org/docs/latest/api/console.html#consoletabletabulardata-properties)
      * [`console.time([label])`](https://nodejs.org/docs/latest/api/console.html#consoletimelabel)
      * [`console.timeEnd([label])`](https://nodejs.org/docs/latest/api/console.html#consoletimeendlabel)
      * [`console.timeLog([label][, ...data])`](https://nodejs.org/docs/latest/api/console.html#consoletimeloglabel-data)
      * [`console.trace([message][, ...args])`](https://nodejs.org/docs/latest/api/console.html#consoletracemessage-args)
      * [`console.warn([data][, ...args])`](https://nodejs.org/docs/latest/api/console.html#consolewarndata-args)
    * [Inspector only methods](https://nodejs.org/docs/latest/api/console.html#inspector-only-methods)
      * [`console.profile([label])`](https://nodejs.org/docs/latest/api/console.html#consoleprofilelabel)
      * [`console.profileEnd([label])`](https://nodejs.org/docs/latest/api/console.html#consoleprofileendlabel)
      * [`console.timeStamp([label])`](https://nodejs.org/docs/latest/api/console.html#consoletimestamplabel)


## Console[#](https://nodejs.org/docs/latest/api/console.html#console)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:console` module provides a simple debugging console that is similar to the JavaScript console mechanism provided by web browsers.
The module exports two specific components:
  * A `Console` class with methods such as `console.log()`, `console.error()`, and `console.warn()` that can be used to write to any Node.js stream.
  * A global `console` instance configured to write to [`process.stdout`](https://nodejs.org/docs/latest/api/process.html#processstdout) and [`process.stderr`](https://nodejs.org/docs/latest/api/process.html#processstderr). The global `console` can be used without calling `require('node:console')`.


_**Warning**_ : The global console object's methods are neither consistently synchronous like the browser APIs they resemble, nor are they consistently asynchronous like all other Node.js streams. Programs that desire to depend on the synchronous / asynchronous behavior of the console functions should first figure out the nature of console's backing stream. This is because the stream is dependent on the underlying platform and standard stream configuration of the current process. See the [note on process I/O](https://nodejs.org/docs/latest/api/process.html#a-note-on-process-io) for more information.
Example using the global `console`:
```
console.log('hello world');
// Prints: hello world, to stdout
console.log('hello %s', 'world');
// Prints: hello world, to stdout
console.error(new Error('Whoops, something bad happened'));
// Prints error message and stack trace to stderr:
//   Error: Whoops, something bad happened
//     at [eval]:5:15
//     at Script.runInThisContext (node:vm:132:18)
//     at Object.runInThisContext (node:vm:309:38)
//     at node:internal/process/execution:77:19
//     at [eval]-wrapper:6:22
//     at evalScript (node:internal/process/execution:76:60)
//     at node:internal/main/eval_string:23:3

const name = 'Will Robinson';
console.warn(`Danger ${name}! Danger!`);
// Prints: Danger Will Robinson! Danger!, to stderr
copy
```

Example using the `Console` class:
```
const out = getStreamSomehow();
const err = getStreamSomehow();
const myConsole = new console.Console(out, err);

myConsole.log('hello world');
// Prints: hello world, to out
myConsole.log('hello %s', 'world');
// Prints: hello world, to out
myConsole.error(new Error('Whoops, something bad happened'));
// Prints: [Error: Whoops, something bad happened], to err

const name = 'Will Robinson';
myConsole.warn(`Danger ${name}! Danger!`);
// Prints: Danger Will Robinson! Danger!, to err
copy
```

### Class: `Console`[#](https://nodejs.org/docs/latest/api/console.html#class-console)
History Version | Changes
---|---
v8.0.0 | Errors that occur while writing to the underlying streams will now be ignored by default.
The `Console` class can be used to create a simple logger with configurable output streams and can be accessed using either `require('node:console').Console` or `console.Console` (or their destructured counterparts):
```
import { Console } from 'node:console';
const { Console } = require('node:console');
copy
```
```
const { Console } = console;
copy
```

####  `new Console(stdout[, stderr][, ignoreErrors])`[#](https://nodejs.org/docs/latest/api/console.html#new-consolestdout-stderr-ignoreerrors)
####  `new Console(options)`[#](https://nodejs.org/docs/latest/api/console.html#new-consoleoptions)
History Version | Changes
---|---
v24.10.0 | The `inspectOptions` option can be a `Map` from stream to options.
v14.2.0, v12.17.0 | The `groupIndentation` option was introduced.
v11.7.0 | The `inspectOptions` option is introduced.
v10.0.0 | The `Console` constructor now supports an `options` argument, and the `colorMode` option was introduced.
v8.0.0 | The `ignoreErrors` option was introduced.
  * `options`
    * `stdout` [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable)
    * `stderr` [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable)
    * `ignoreErrors` **Default:** `true`.
    * `colorMode` `Console` instance. Setting to `true` enables coloring while inspecting values. Setting to `false` disables coloring while inspecting values. Setting to `'auto'` makes color support depend on the value of the `isTTY` property and the value returned by `getColorDepth()` on the respective stream. This option can not be used, if `inspectOptions.colors` is set as well. **Default:** `'auto'`.
    * `inspectOptions` [`util.inspect()`](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options). Can be an options object or, if different options for stdout and stderr are desired, a `Map` from stream objects to options.
    * `groupIndentation` **Default:** `2`.


Creates a new `Console` with one or two writable stream instances. `stdout` is a writable stream to print log or info output. `stderr` is used for warning or error output. If `stderr` is not provided, `stdout` is used for `stderr`.
```
import { createWriteStream } from 'node:fs';
import { Console } from 'node:console';
// Alternatively
// const { Console } = console;

const output = createWriteStream('./stdout.log');
const errorOutput = createWriteStream('./stderr.log');
// Custom simple logger
const logger = new Console({ stdout: output, stderr: errorOutput });
// use it like console
const count = 5;
logger.log('count: %d', count);
// In stdout.log: count 5
const fs = require('node:fs');
const { Console } = require('node:console');
// Alternatively
// const { Console } = console;

const output = fs.createWriteStream('./stdout.log');
const errorOutput = fs.createWriteStream('./stderr.log');
// Custom simple logger
const logger = new Console({ stdout: output, stderr: errorOutput });
// use it like console
const count = 5;
logger.log('count: %d', count);
// In stdout.log: count 5
copy
```

The global `console` is a special `Console` whose output is sent to [`process.stdout`](https://nodejs.org/docs/latest/api/process.html#processstdout) and [`process.stderr`](https://nodejs.org/docs/latest/api/process.html#processstderr). It is equivalent to calling:
```
new Console({ stdout: process.stdout, stderr: process.stderr });
copy
```

####  `console.assert(value[, ...message])`[#](https://nodejs.org/docs/latest/api/console.html#consoleassertvalue-message)
Added in: v0.1.101History Version | Changes
---|---
v10.0.0 | The implementation is now spec compliant and does not throw anymore.
  * `value`
  * `...message` `value` are used as error message.


`console.assert()` writes a message if `value` is `"Assertion failed"`. If provided, `message` is formatted using [`util.format()`](https://nodejs.org/docs/latest/api/util.html#utilformatformat-args).
If `value` is
```
console.assert(true, 'does nothing');

console.assert(false, 'Whoops %s work', 'didn\'t');
// Assertion failed: Whoops didn't work

console.assert();
// Assertion failed
copy
```

####  `console.clear()`[#](https://nodejs.org/docs/latest/api/console.html#consoleclear)
Added in: v8.3.0
When `stdout` is a TTY, calling `console.clear()` will attempt to clear the TTY. When `stdout` is not a TTY, this method does nothing.
The specific operation of `console.clear()` can vary across operating systems and terminal types. For most Linux operating systems, `console.clear()` operates similarly to the `clear` shell command. On Windows, `console.clear()` will clear only the output in the current terminal viewport for the Node.js binary.
####  `console.count([label])`[#](https://nodejs.org/docs/latest/api/console.html#consolecountlabel)
Added in: v8.3.0
  * `label` **Default:** `'default'`.


Maintains an internal counter specific to `label` and outputs to `stdout` the number of times `console.count()` has been called with the given `label`.
```
> console.count()
default: 1
undefined
> console.count('default')
default: 2
undefined
> console.count('abc')
abc: 1
undefined
> console.count('xyz')
xyz: 1
undefined
> console.count('abc')
abc: 2
undefined
> console.count()
default: 3
undefined
>
copy
```

####  `console.countReset([label])`[#](https://nodejs.org/docs/latest/api/console.html#consolecountresetlabel)
Added in: v8.3.0
  * `label` **Default:** `'default'`.


Resets the internal counter specific to `label`.
```
> console.count('abc');
abc: 1
undefined
> console.countReset('abc');
undefined
> console.count('abc');
abc: 1
undefined
>
copy
```

####  `console.debug(data[, ...args])`[#](https://nodejs.org/docs/latest/api/console.html#consoledebugdata-args)
Added in: v8.0.0History Version | Changes
---|---
v8.10.0 | `console.debug` is now an alias for `console.log`.
  * `data`
  * `...args`


The `console.debug()` function is an alias for [`console.log()`](https://nodejs.org/docs/latest/api/console.html#consolelogdata-args).
####  `console.dir(obj[, options])`[#](https://nodejs.org/docs/latest/api/console.html#consoledirobj-options)
Added in: v0.1.101
  * `obj`
  * `options`
    * `showHidden` `true` then the object's non-enumerable and symbol properties will be shown too. **Default:** `false`.
    * `depth` [`util.inspect()`](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options) how many times to recurse while formatting the object. This is useful for inspecting large complicated objects. To make it recurse indefinitely, pass `null`. **Default:** `2`.
    * `colors` `true`, then the output will be styled with ANSI color codes. Colors are customizable; see [customizing `util.inspect()` colors](https://nodejs.org/docs/latest/api/util.html#customizing-utilinspect-colors). **Default:** `false`.


Uses [`util.inspect()`](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options) on `obj` and prints the resulting string to `stdout`. This function bypasses any custom `inspect()` function defined on `obj`.
####  `console.dirxml(...data)`[#](https://nodejs.org/docs/latest/api/console.html#consoledirxmldata)
Added in: v8.0.0History Version | Changes
---|---
v9.3.0 | `console.dirxml` now calls `console.log` for its arguments.
  * `...data`


This method calls `console.log()` passing it the arguments received. This method does not produce any XML formatting.
####  `console.error([data][, ...args])`[#](https://nodejs.org/docs/latest/api/console.html#consoleerrordata-args)
Added in: v0.1.100
  * `data`
  * `...args`


Prints to `stderr` with newline. Multiple arguments can be passed, with the first used as the primary message and all additional used as substitution values similar to [`util.format()`](https://nodejs.org/docs/latest/api/util.html#utilformatformat-args)).
```
const code = 5;
console.error('error #%d', code);
// Prints: error #5, to stderr
console.error('error', code);
// Prints: error 5, to stderr
copy
```

If formatting elements (e.g. `%d`) are not found in the first string then [`util.inspect()`](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options) is called on each argument and the resulting string values are concatenated. See [`util.format()`](https://nodejs.org/docs/latest/api/util.html#utilformatformat-args) for more information.
####  `console.group([...label])`[#](https://nodejs.org/docs/latest/api/console.html#consolegrouplabel)
Added in: v8.5.0
  * `...label`


Increases indentation of subsequent lines by spaces for `groupIndentation` length.
If one or more `label`s are provided, those are printed first without the additional indentation.
####  `console.groupCollapsed()`[#](https://nodejs.org/docs/latest/api/console.html#consolegroupcollapsed)
Added in: v8.5.0
An alias for [`console.group()`](https://nodejs.org/docs/latest/api/console.html#consolegrouplabel).
####  `console.groupEnd()`[#](https://nodejs.org/docs/latest/api/console.html#consolegroupend)
Added in: v8.5.0
Decreases indentation of subsequent lines by spaces for `groupIndentation` length.
####  `console.info([data][, ...args])`[#](https://nodejs.org/docs/latest/api/console.html#consoleinfodata-args)
Added in: v0.1.100
  * `data`
  * `...args`


The `console.info()` function is an alias for [`console.log()`](https://nodejs.org/docs/latest/api/console.html#consolelogdata-args).
####  `console.log([data][, ...args])`[#](https://nodejs.org/docs/latest/api/console.html#consolelogdata-args)
Added in: v0.1.100
  * `data`
  * `...args`


Prints to `stdout` with newline. Multiple arguments can be passed, with the first used as the primary message and all additional used as substitution values similar to [`util.format()`](https://nodejs.org/docs/latest/api/util.html#utilformatformat-args)).
```
const count = 5;
console.log('count: %d', count);
// Prints: count: 5, to stdout
console.log('count:', count);
// Prints: count: 5, to stdout
copy
```

See [`util.format()`](https://nodejs.org/docs/latest/api/util.html#utilformatformat-args) for more information.
####  `console.table(tabularData[, properties])`[#](https://nodejs.org/docs/latest/api/console.html#consoletabletabulardata-properties)
Added in: v10.0.0
  * `tabularData`
  * `properties`


Try to construct a table with the columns of the properties of `tabularData` (or use `properties`) and rows of `tabularData` and log it. Falls back to just logging the argument if it can't be parsed as tabular.
```
// These can't be parsed as tabular data
console.table(Symbol());
// Symbol()

console.table(undefined);
// undefined

console.table([{ a: 1, b: 'Y' }, { a: 'Z', b: 2 }]);
// ┌─────────┬─────┬─────┐
// │ (index) │ a   │ b   │
// ├─────────┼─────┼─────┤
// │ 0       │ 1   │ 'Y' │
// │ 1       │ 'Z' │ 2   │
// └─────────┴─────┴─────┘

console.table([{ a: 1, b: 'Y' }, { a: 'Z', b: 2 }], ['a']);
// ┌─────────┬─────┐
// │ (index) │ a   │
// ├─────────┼─────┤
// │ 0       │ 1   │
// │ 1       │ 'Z' │
// └─────────┴─────┘
copy
```

####  `console.time([label])`[#](https://nodejs.org/docs/latest/api/console.html#consoletimelabel)
Added in: v0.1.104
  * `label` **Default:** `'default'`


Starts a timer that can be used to compute the duration of an operation. Timers are identified by a unique `label`. Use the same `label` when calling [`console.timeEnd()`](https://nodejs.org/docs/latest/api/console.html#consoletimeendlabel) to stop the timer and output the elapsed time in suitable time units to `stdout`. For example, if the elapsed time is 3869ms, `console.timeEnd()` displays "3.869s".
####  `console.timeEnd([label])`[#](https://nodejs.org/docs/latest/api/console.html#consoletimeendlabel)
Added in: v0.1.104History Version | Changes
---|---
v13.0.0 | The elapsed time is displayed with a suitable time unit.
v6.0.0 | This method no longer supports multiple calls that don't map to individual `console.time()` calls; see below for details.
  * `label` **Default:** `'default'`


Stops a timer that was previously started by calling [`console.time()`](https://nodejs.org/docs/latest/api/console.html#consoletimelabel) and prints the result to `stdout`:
```
console.time('bunch-of-stuff');
// Do a bunch of stuff.
console.timeEnd('bunch-of-stuff');
// Prints: bunch-of-stuff: 225.438ms
copy
```

####  `console.timeLog([label][, ...data])`[#](https://nodejs.org/docs/latest/api/console.html#consoletimeloglabel-data)
Added in: v10.7.0
  * `label` **Default:** `'default'`
  * `...data`


For a timer that was previously started by calling [`console.time()`](https://nodejs.org/docs/latest/api/console.html#consoletimelabel), prints the elapsed time and other `data` arguments to `stdout`:
```
console.time('process');
const value = expensiveProcess1(); // Returns 42
console.timeLog('process', value);
// Prints "process: 365.227ms 42".
doExpensiveProcess2(value);
console.timeEnd('process');
copy
```

####  `console.trace([message][, ...args])`[#](https://nodejs.org/docs/latest/api/console.html#consoletracemessage-args)
Added in: v0.1.104
  * `message`
  * `...args`


Prints to `stderr` the string `'Trace: '`, followed by the [`util.format()`](https://nodejs.org/docs/latest/api/util.html#utilformatformat-args) formatted message and stack trace to the current position in the code.
```
console.trace('Show me');
// Prints: (stack trace will vary based on where trace is called)
//  Trace: Show me
//    at repl:2:9
//    at REPLServer.defaultEval (repl.js:248:27)
//    at bound (domain.js:287:14)
//    at REPLServer.runBound [as eval] (domain.js:300:12)
//    at REPLServer.<anonymous> (repl.js:412:12)
//    at emitOne (events.js:82:20)
//    at REPLServer.emit (events.js:169:7)
//    at REPLServer.Interface._onLine (readline.js:210:10)
//    at REPLServer.Interface._line (readline.js:549:8)
//    at REPLServer.Interface._ttyWrite (readline.js:826:14)
copy
```

####  `console.warn([data][, ...args])`[#](https://nodejs.org/docs/latest/api/console.html#consolewarndata-args)
Added in: v0.1.100
  * `data`
  * `...args`


The `console.warn()` function is an alias for [`console.error()`](https://nodejs.org/docs/latest/api/console.html#consoleerrordata-args).
### Inspector only methods[#](https://nodejs.org/docs/latest/api/console.html#inspector-only-methods)
The following methods are exposed by the V8 engine in the general API but do not display anything unless used in conjunction with the [inspector](https://nodejs.org/docs/latest/api/debugger.html) (`--inspect` flag).
####  `console.profile([label])`[#](https://nodejs.org/docs/latest/api/console.html#consoleprofilelabel)
Added in: v8.0.0
  * `label`


This method does not display anything unless used in the inspector. The `console.profile()` method starts a JavaScript CPU profile with an optional label until [`console.profileEnd()`](https://nodejs.org/docs/latest/api/console.html#consoleprofileendlabel) is called. The profile is then added to the **Profile** panel of the inspector.
```
console.profile('MyLabel');
// Some code
console.profileEnd('MyLabel');
// Adds the profile 'MyLabel' to the Profiles panel of the inspector.
copy
```

####  `console.profileEnd([label])`[#](https://nodejs.org/docs/latest/api/console.html#consoleprofileendlabel)
Added in: v8.0.0
  * `label`


This method does not display anything unless used in the inspector. Stops the current JavaScript CPU profiling session if one has been started and prints the report to the **Profiles** panel of the inspector. See [`console.profile()`](https://nodejs.org/docs/latest/api/console.html#consoleprofilelabel) for an example.
If this method is called without a label, the most recently started profile is stopped.
####  `console.timeStamp([label])`[#](https://nodejs.org/docs/latest/api/console.html#consoletimestamplabel)
Added in: v8.0.0
  * `label`


This method does not display anything unless used in the inspector. The `console.timeStamp()` method adds an event with the label `'label'` to the **Timeline** panel of the inspector.
