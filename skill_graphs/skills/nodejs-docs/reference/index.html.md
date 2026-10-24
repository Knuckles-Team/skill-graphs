[Skip to content](https://nodejs.org/docs/latest/api/tracing.html#apicontent)
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
  * [](https://nodejs.org/docs/latest/api/tracing.html#toc-picker)
    * [Trace events](https://nodejs.org/docs/latest/api/tracing.html#trace-events)
      * [The `node:trace_events` module](https://nodejs.org/docs/latest/api/tracing.html#the-nodetrace-events-module)
        * [`Tracing` object](https://nodejs.org/docs/latest/api/tracing.html#tracing-object)
          * [`tracing.categories`](https://nodejs.org/docs/latest/api/tracing.html#tracingcategories)
          * [`tracing.disable()`](https://nodejs.org/docs/latest/api/tracing.html#tracingdisable)
          * [`tracing.enable()`](https://nodejs.org/docs/latest/api/tracing.html#tracingenable)
          * [`tracing.enabled`](https://nodejs.org/docs/latest/api/tracing.html#tracingenabled)
        * [`trace_events.createTracing(options)`](https://nodejs.org/docs/latest/api/tracing.html#trace-eventscreatetracingoptions)
        * [`trace_events.getEnabledCategories()`](https://nodejs.org/docs/latest/api/tracing.html#trace-eventsgetenabledcategories)
      * [Examples](https://nodejs.org/docs/latest/api/tracing.html#examples)
        * [Collect trace events data by inspector](https://nodejs.org/docs/latest/api/tracing.html#collect-trace-events-data-by-inspector)
  * [](https://nodejs.org/docs/latest/api/tracing.html#gtoc-picker)
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
  * [](https://nodejs.org/docs/latest/api/tracing.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/tracing.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/tracing.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/tracing.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/tracing.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/tracing.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/tracing.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/tracing.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/tracing.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/tracing.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/tracing.html)
    11. [15.x ](https://nodejs.org/docs/latest-v15.x/api/tracing.html)
    12. [14.x ](https://nodejs.org/docs/latest-v14.x/api/tracing.html)
    13. [13.x ](https://nodejs.org/docs/latest-v13.x/api/tracing.html)
    14. [12.x ](https://nodejs.org/docs/latest-v12.x/api/tracing.html)
    15. [11.x ](https://nodejs.org/docs/latest-v11.x/api/tracing.html)
    16. [10.x ](https://nodejs.org/docs/latest-v10.x/api/tracing.html)
    17. [9.x ](https://nodejs.org/docs/latest-v9.x/api/tracing.html)
    18. [8.x ](https://nodejs.org/docs/latest-v8.x/api/tracing.html)
    19. [7.x ](https://nodejs.org/docs/latest-v7.x/api/tracing.html)
  * [ ](https://nodejs.org/docs/latest/api/tracing.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/tracing.json)


* * *
Table of contents
  * [Trace events](https://nodejs.org/docs/latest/api/tracing.html#trace-events)
    * [The `node:trace_events` module](https://nodejs.org/docs/latest/api/tracing.html#the-nodetrace-events-module)
      * [`Tracing` object](https://nodejs.org/docs/latest/api/tracing.html#tracing-object)
        * [`tracing.categories`](https://nodejs.org/docs/latest/api/tracing.html#tracingcategories)
        * [`tracing.disable()`](https://nodejs.org/docs/latest/api/tracing.html#tracingdisable)
        * [`tracing.enable()`](https://nodejs.org/docs/latest/api/tracing.html#tracingenable)
        * [`tracing.enabled`](https://nodejs.org/docs/latest/api/tracing.html#tracingenabled)
      * [`trace_events.createTracing(options)`](https://nodejs.org/docs/latest/api/tracing.html#trace-eventscreatetracingoptions)
      * [`trace_events.getEnabledCategories()`](https://nodejs.org/docs/latest/api/tracing.html#trace-eventsgetenabledcategories)
    * [Examples](https://nodejs.org/docs/latest/api/tracing.html#examples)
      * [Collect trace events data by inspector](https://nodejs.org/docs/latest/api/tracing.html#collect-trace-events-data-by-inspector)


## Trace events[#](https://nodejs.org/docs/latest/api/tracing.html#trace-events)
**Source Code:**
[Stability: 1](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Experimental
The `node:trace_events` module provides a mechanism to centralize tracing information generated by V8, Node.js core, and userspace code.
Tracing can be enabled with the `--trace-event-categories` command-line flag or by using the `node:trace_events` module. The `--trace-event-categories` flag accepts a list of comma-separated category names.
The available categories are:
  * `node`: An empty placeholder.
  * `node.async_hooks`: Enables capture of detailed [`async_hooks`](https://nodejs.org/docs/latest/api/async_hooks.html) trace data. The [`async_hooks`](https://nodejs.org/docs/latest/api/async_hooks.html) events have a unique `asyncId` and a special `triggerId` `triggerAsyncId` property.
  * `node.bootstrap`: Enables capture of Node.js bootstrap milestones.
  * `node.console`: Enables capture of `console.time()` and `console.count()` output.
  * `node.threadpoolwork.sync`: Enables capture of trace data for threadpool synchronous operations, such as `blob`, `zlib`, `crypto` and `node_api`.
  * `node.threadpoolwork.async`: Enables capture of trace data for threadpool asynchronous operations, such as `blob`, `zlib`, `crypto` and `node_api`.
  * `node.dns.native`: Enables capture of trace data for DNS queries.
  * `node.net.native`: Enables capture of trace data for network.
  * `node.environment`: Enables capture of Node.js Environment milestones.
  * `node.fs.sync`: Enables capture of trace data for file system sync methods.
  * `node.fs_dir.sync`: Enables capture of trace data for file system sync directory methods.
  * `node.fs.async`: Enables capture of trace data for file system async methods.
  * `node.fs_dir.async`: Enables capture of trace data for file system async directory methods.
  * `node.perf`: Enables capture of [Performance API](https://nodejs.org/docs/latest/api/perf_hooks.html) measurements.
    * `node.perf.usertiming`: Enables capture of only Performance API User Timing measures and marks.
    * `node.perf.timerify`: Enables capture of only Performance API timerify measurements.
  * `node.promises.rejections`: Enables capture of trace data tracking the number of unhandled Promise rejections and handled-after-rejections.
  * `node.vm.script`: Enables capture of trace data for the `node:vm` module's `runInNewContext()`, `runInContext()`, and `runInThisContext()` methods.
  * `v8`: The [V8](https://nodejs.org/docs/latest/api/v8.html) events are GC, compiling, and execution related.
  * `node.http`: Enables capture of trace data for http request / response.
  * `node.module_timer`: Enables capture of trace data for CJS Module loading.


By default the `node`, `node.async_hooks`, and `v8` categories are enabled.
```
node --trace-event-categories v8,node,node.async_hooks server.js
copy
```

Prior versions of Node.js required the use of the `--trace-events-enabled` flag to enable trace events. This requirement has been removed. However, the `--trace-events-enabled` flag _may_ still be used and will enable the `node`, `node.async_hooks`, and `v8` trace event categories by default.
```
node --trace-events-enabled

# is equivalent to

node --trace-event-categories v8,node,node.async_hooks
copy
```

Alternatively, trace events may be enabled using the `node:trace_events` module:
```
import { createTracing } from 'node:trace_events';
const tracing = createTracing({ categories: ['node.perf'] });
tracing.enable();  // Enable trace event capture for the 'node.perf' category

// do work

tracing.disable();  // Disable trace event capture for the 'node.perf' category
const { createTracing } = require('node:trace_events');
const tracing = createTracing({ categories: ['node.perf'] });
tracing.enable();  // Enable trace event capture for the 'node.perf' category

// do work

tracing.disable();  // Disable trace event capture for the 'node.perf' category
copy
```

Running Node.js with tracing enabled will produce log files that can be opened in the
The logging file is by default called `node_trace.${rotation}.log`, where `${rotation}` is an incrementing log-rotation id. The filepath pattern can be specified with `--trace-event-file-pattern` that accepts a template string that supports `${rotation}` and `${pid}`:
```
node --trace-event-categories v8 --trace-event-file-pattern '${pid}-${rotation}.log' server.js
copy
```

To guarantee that the log file is properly generated after signal events like `SIGINT`, `SIGTERM`, or `SIGBREAK`, make sure to have the appropriate handlers in your code, such as:
```
process.on('SIGINT', function onSigint() {
  console.info('Received SIGINT.');
  process.exit(130);  // Or applicable exit code depending on OS and signal
});
copy
```

The tracing system uses the same time source as the one used by `process.hrtime()`. However the trace-event timestamps are expressed in microseconds, unlike `process.hrtime()` which returns nanoseconds.
The features from this module are not available in [`Worker`](https://nodejs.org/docs/latest/api/worker_threads.html#class-worker) threads.
### The `node:trace_events` module[#](https://nodejs.org/docs/latest/api/tracing.html#the-nodetrace-events-module)
Added in: v10.0.0
####  `Tracing` object[#](https://nodejs.org/docs/latest/api/tracing.html#tracing-object)
Added in: v10.0.0
The `Tracing` object is used to enable or disable tracing for sets of categories. Instances are created using the `trace_events.createTracing()` method.
When created, the `Tracing` object is disabled. Calling the `tracing.enable()` method adds the categories to the set of enabled trace event categories. Calling `tracing.disable()` will remove the categories from the set of enabled trace event categories.
#####  `tracing.categories`[#](https://nodejs.org/docs/latest/api/tracing.html#tracingcategories)
Added in: v10.0.0
  * Type:


A comma-separated list of the trace event categories covered by this `Tracing` object.
#####  `tracing.disable()`[#](https://nodejs.org/docs/latest/api/tracing.html#tracingdisable)
Added in: v10.0.0
Disables this `Tracing` object.
Only trace event categories _not_ covered by other enabled `Tracing` objects and _not_ specified by the `--trace-event-categories` flag will be disabled.
```
import { createTracing, getEnabledCategories } from 'node:trace_events';
const t1 = createTracing({ categories: ['node', 'v8'] });
const t2 = createTracing({ categories: ['node.perf', 'node'] });
t1.enable();
t2.enable();

// Prints 'node,node.perf,v8'
console.log(getEnabledCategories());

t2.disable(); // Will only disable emission of the 'node.perf' category

// Prints 'node,v8'
console.log(getEnabledCategories());
const { createTracing, getEnabledCategories } = require('node:trace_events');
const t1 = createTracing({ categories: ['node', 'v8'] });
const t2 = createTracing({ categories: ['node.perf', 'node'] });
t1.enable();
t2.enable();

// Prints 'node,node.perf,v8'
console.log(getEnabledCategories());

t2.disable(); // Will only disable emission of the 'node.perf' category

// Prints 'node,v8'
console.log(getEnabledCategories());
copy
```

#####  `tracing.enable()`[#](https://nodejs.org/docs/latest/api/tracing.html#tracingenable)
Added in: v10.0.0
Enables this `Tracing` object for the set of categories covered by the `Tracing` object.
#####  `tracing.enabled`[#](https://nodejs.org/docs/latest/api/tracing.html#tracingenabled)
Added in: v10.0.0
  * Type: `true` only if the `Tracing` object has been enabled.


####  `trace_events.createTracing(options)`[#](https://nodejs.org/docs/latest/api/tracing.html#trace-eventscreatetracingoptions)
Added in: v10.0.0
  * `options`
    * `categories`
  * Returns: [`<Tracing>`](https://nodejs.org/docs/latest/api/tracing.html#tracing-object).


Creates and returns a `Tracing` object for the given set of `categories`.
```
import { createTracing } from 'node:trace_events';
const categories = ['node.perf', 'node.async_hooks'];
const tracing = createTracing({ categories });
tracing.enable();
// do stuff
tracing.disable();
const { createTracing } = require('node:trace_events');
const categories = ['node.perf', 'node.async_hooks'];
const tracing = createTracing({ categories });
tracing.enable();
// do stuff
tracing.disable();
copy
```

####  `trace_events.getEnabledCategories()`[#](https://nodejs.org/docs/latest/api/tracing.html#trace-eventsgetenabledcategories)
Added in: v10.0.0
  * Returns:


Returns a comma-separated list of all currently-enabled trace event categories. The current set of enabled trace event categories is determined by the _union_ of all currently-enabled `Tracing` objects and any categories enabled using the `--trace-event-categories` flag.
Given the file `test.js` below, the command `node --trace-event-categories node.perf test.js` will print `'node.async_hooks,node.perf'` to the console.
```
import { createTracing, getEnabledCategories } from 'node:trace_events';
const t1 = createTracing({ categories: ['node.async_hooks'] });
const t2 = createTracing({ categories: ['node.perf'] });
const t3 = createTracing({ categories: ['v8'] });

t1.enable();
t2.enable();

console.log(getEnabledCategories());
const { createTracing, getEnabledCategories } = require('node:trace_events');
const t1 = createTracing({ categories: ['node.async_hooks'] });
const t2 = createTracing({ categories: ['node.perf'] });
const t3 = createTracing({ categories: ['v8'] });

t1.enable();
t2.enable();

console.log(getEnabledCategories());
copy
```

### Examples[#](https://nodejs.org/docs/latest/api/tracing.html#examples)
#### Collect trace events data by inspector[#](https://nodejs.org/docs/latest/api/tracing.html#collect-trace-events-data-by-inspector)
```
import { Session } from 'node:inspector';
const session = new Session();
session.connect();

function post(message, data) {
  return new Promise((resolve, reject) => {
    session.post(message, data, (err, result) => {
      if (err)
        reject(new Error(JSON.stringify(err)));
      else
        resolve(result);
    });
  });
}

async function collect() {
  const data = [];
  session.on('NodeTracing.dataCollected', (chunk) => data.push(chunk));
  session.on('NodeTracing.tracingComplete', () => {
    // done
  });
  const traceConfig = { includedCategories: ['v8'] };
  await post('NodeTracing.start', { traceConfig });
  // do something
  setTimeout(() => {
    post('NodeTracing.stop').then(() => {
      session.disconnect();
      console.log(data);
    });
  }, 1000);
}

collect();
'use strict';

const { Session } = require('node:inspector');
const session = new Session();
session.connect();

function post(message, data) {
  return new Promise((resolve, reject) => {
    session.post(message, data, (err, result) => {
      if (err)
        reject(new Error(JSON.stringify(err)));
      else
        resolve(result);
    });
  });
}

async function collect() {
  const data = [];
  session.on('NodeTracing.dataCollected', (chunk) => data.push(chunk));
  session.on('NodeTracing.tracingComplete', () => {
    // done
  });
  const traceConfig = { includedCategories: ['v8'] };
  await post('NodeTracing.start', { traceConfig });
  // do something
  setTimeout(() => {
    post('NodeTracing.stop').then(() => {
      session.disconnect();
      console.log(data);
    });
  }, 1000);
}

collect();
copy
```
