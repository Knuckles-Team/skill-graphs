[Skip to content](https://nodejs.org/docs/latest/api/timers.html#apicontent)
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
  * [](https://nodejs.org/docs/latest/api/timers.html#toc-picker)
    * [Timers](https://nodejs.org/docs/latest/api/timers.html#timers)
      * [Class: `Immediate`](https://nodejs.org/docs/latest/api/timers.html#class-immediate)
        * [`immediate.hasRef()`](https://nodejs.org/docs/latest/api/timers.html#immediatehasref)
        * [`immediate.ref()`](https://nodejs.org/docs/latest/api/timers.html#immediateref)
        * [`immediate.unref()`](https://nodejs.org/docs/latest/api/timers.html#immediateunref)
        * [`immediate[Symbol.dispose]()`](https://nodejs.org/docs/latest/api/timers.html#immediatesymboldispose)
      * [Class: `Timeout`](https://nodejs.org/docs/latest/api/timers.html#class-timeout)
        * [`timeout.close()`](https://nodejs.org/docs/latest/api/timers.html#timeoutclose)
        * [`timeout.hasRef()`](https://nodejs.org/docs/latest/api/timers.html#timeouthasref)
        * [`timeout.ref()`](https://nodejs.org/docs/latest/api/timers.html#timeoutref)
        * [`timeout.refresh()`](https://nodejs.org/docs/latest/api/timers.html#timeoutrefresh)
        * [`timeout.unref()`](https://nodejs.org/docs/latest/api/timers.html#timeoutunref)
        * [`timeout[Symbol.toPrimitive]()`](https://nodejs.org/docs/latest/api/timers.html#timeoutsymboltoprimitive)
        * [`timeout[Symbol.dispose]()`](https://nodejs.org/docs/latest/api/timers.html#timeoutsymboldispose)
      * [Scheduling timers](https://nodejs.org/docs/latest/api/timers.html#scheduling-timers)
        * [`setImmediate(callback[, ...args])`](https://nodejs.org/docs/latest/api/timers.html#setimmediatecallback-args)
        * [`setInterval(callback[, delay[, ...args]])`](https://nodejs.org/docs/latest/api/timers.html#setintervalcallback-delay-args)
        * [`setTimeout(callback[, delay[, ...args]])`](https://nodejs.org/docs/latest/api/timers.html#settimeoutcallback-delay-args)
      * [Cancelling timers](https://nodejs.org/docs/latest/api/timers.html#cancelling-timers)
        * [`clearImmediate(immediate)`](https://nodejs.org/docs/latest/api/timers.html#clearimmediateimmediate)
        * [`clearInterval(timeout)`](https://nodejs.org/docs/latest/api/timers.html#clearintervaltimeout)
        * [`clearTimeout(timeout)`](https://nodejs.org/docs/latest/api/timers.html#cleartimeouttimeout)
      * [Timers Promises API](https://nodejs.org/docs/latest/api/timers.html#timers-promises-api)
        * [`timersPromises.setTimeout([delay[, value[, options]]])`](https://nodejs.org/docs/latest/api/timers.html#timerspromisessettimeoutdelay-value-options)
        * [`timersPromises.setImmediate([value[, options]])`](https://nodejs.org/docs/latest/api/timers.html#timerspromisessetimmediatevalue-options)
        * [`timersPromises.setInterval([delay[, value[, options]]])`](https://nodejs.org/docs/latest/api/timers.html#timerspromisessetintervaldelay-value-options)
        * [`timersPromises.scheduler.wait(delay[, options])`](https://nodejs.org/docs/latest/api/timers.html#timerspromisesschedulerwaitdelay-options)
        * [`timersPromises.scheduler.yield()`](https://nodejs.org/docs/latest/api/timers.html#timerspromisesscheduleryield)
  * [](https://nodejs.org/docs/latest/api/timers.html#gtoc-picker)
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
  * [](https://nodejs.org/docs/latest/api/timers.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/timers.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/timers.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/timers.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/timers.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/timers.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/timers.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/timers.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/timers.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/timers.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/timers.html)
    11. [15.x ](https://nodejs.org/docs/latest-v15.x/api/timers.html)
    12. [14.x ](https://nodejs.org/docs/latest-v14.x/api/timers.html)
    13. [13.x ](https://nodejs.org/docs/latest-v13.x/api/timers.html)
    14. [12.x ](https://nodejs.org/docs/latest-v12.x/api/timers.html)
    15. [11.x ](https://nodejs.org/docs/latest-v11.x/api/timers.html)
    16. [10.x ](https://nodejs.org/docs/latest-v10.x/api/timers.html)
    17. [9.x ](https://nodejs.org/docs/latest-v9.x/api/timers.html)
    18. [8.x ](https://nodejs.org/docs/latest-v8.x/api/timers.html)
    19. [7.x ](https://nodejs.org/docs/latest-v7.x/api/timers.html)
    20. [6.x ](https://nodejs.org/docs/latest-v6.x/api/timers.html)
    21. [5.x ](https://nodejs.org/docs/latest-v5.x/api/timers.html)
    22. [4.x ](https://nodejs.org/docs/latest-v4.x/api/timers.html)
    23. [0.12.x ](https://nodejs.org/docs/latest-v0.12.x/api/timers.html)
    24. [0.10.x ](https://nodejs.org/docs/latest-v0.10.x/api/timers.html)
  * [ ](https://nodejs.org/docs/latest/api/timers.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/timers.json)


* * *
Table of contents
  * [Timers](https://nodejs.org/docs/latest/api/timers.html#timers)
    * [Class: `Immediate`](https://nodejs.org/docs/latest/api/timers.html#class-immediate)
      * [`immediate.hasRef()`](https://nodejs.org/docs/latest/api/timers.html#immediatehasref)
      * [`immediate.ref()`](https://nodejs.org/docs/latest/api/timers.html#immediateref)
      * [`immediate.unref()`](https://nodejs.org/docs/latest/api/timers.html#immediateunref)
      * [`immediate[Symbol.dispose]()`](https://nodejs.org/docs/latest/api/timers.html#immediatesymboldispose)
    * [Class: `Timeout`](https://nodejs.org/docs/latest/api/timers.html#class-timeout)
      * [`timeout.close()`](https://nodejs.org/docs/latest/api/timers.html#timeoutclose)
      * [`timeout.hasRef()`](https://nodejs.org/docs/latest/api/timers.html#timeouthasref)
      * [`timeout.ref()`](https://nodejs.org/docs/latest/api/timers.html#timeoutref)
      * [`timeout.refresh()`](https://nodejs.org/docs/latest/api/timers.html#timeoutrefresh)
      * [`timeout.unref()`](https://nodejs.org/docs/latest/api/timers.html#timeoutunref)
      * [`timeout[Symbol.toPrimitive]()`](https://nodejs.org/docs/latest/api/timers.html#timeoutsymboltoprimitive)
      * [`timeout[Symbol.dispose]()`](https://nodejs.org/docs/latest/api/timers.html#timeoutsymboldispose)
    * [Scheduling timers](https://nodejs.org/docs/latest/api/timers.html#scheduling-timers)
      * [`setImmediate(callback[, ...args])`](https://nodejs.org/docs/latest/api/timers.html#setimmediatecallback-args)
      * [`setInterval(callback[, delay[, ...args]])`](https://nodejs.org/docs/latest/api/timers.html#setintervalcallback-delay-args)
      * [`setTimeout(callback[, delay[, ...args]])`](https://nodejs.org/docs/latest/api/timers.html#settimeoutcallback-delay-args)
    * [Cancelling timers](https://nodejs.org/docs/latest/api/timers.html#cancelling-timers)
      * [`clearImmediate(immediate)`](https://nodejs.org/docs/latest/api/timers.html#clearimmediateimmediate)
      * [`clearInterval(timeout)`](https://nodejs.org/docs/latest/api/timers.html#clearintervaltimeout)
      * [`clearTimeout(timeout)`](https://nodejs.org/docs/latest/api/timers.html#cleartimeouttimeout)
    * [Timers Promises API](https://nodejs.org/docs/latest/api/timers.html#timers-promises-api)
      * [`timersPromises.setTimeout([delay[, value[, options]]])`](https://nodejs.org/docs/latest/api/timers.html#timerspromisessettimeoutdelay-value-options)
      * [`timersPromises.setImmediate([value[, options]])`](https://nodejs.org/docs/latest/api/timers.html#timerspromisessetimmediatevalue-options)
      * [`timersPromises.setInterval([delay[, value[, options]]])`](https://nodejs.org/docs/latest/api/timers.html#timerspromisessetintervaldelay-value-options)
      * [`timersPromises.scheduler.wait(delay[, options])`](https://nodejs.org/docs/latest/api/timers.html#timerspromisesschedulerwaitdelay-options)
      * [`timersPromises.scheduler.yield()`](https://nodejs.org/docs/latest/api/timers.html#timerspromisesscheduleryield)


## Timers[#](https://nodejs.org/docs/latest/api/timers.html#timers)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `timer` module exposes a global API for scheduling functions to be called at some future period of time. Because the timer functions are globals, there is no need to call `require('node:timers')` to use the API.
The timer functions within Node.js implement a similar API as the timers API provided by Web Browsers but use a different internal implementation that is built around the Node.js [Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#setimmediate-vs-settimeout).
### Class: `Immediate`[#](https://nodejs.org/docs/latest/api/timers.html#class-immediate)
This object is created internally and is returned from [`setImmediate()`](https://nodejs.org/docs/latest/api/timers.html#setimmediatecallback-args). It can be passed to [`clearImmediate()`](https://nodejs.org/docs/latest/api/timers.html#clearimmediateimmediate) in order to cancel the scheduled actions.
By default, when an immediate is scheduled, the Node.js event loop will continue running as long as the immediate is active. The `Immediate` object returned by [`setImmediate()`](https://nodejs.org/docs/latest/api/timers.html#setimmediatecallback-args) exports both `immediate.ref()` and `immediate.unref()` functions that can be used to control this default behavior.
####  `immediate.hasRef()`[#](https://nodejs.org/docs/latest/api/timers.html#immediatehasref)
Added in: v11.0.0
  * Returns:


If true, the `Immediate` object will keep the Node.js event loop active.
####  `immediate.ref()`[#](https://nodejs.org/docs/latest/api/timers.html#immediateref)
Added in: v9.7.0
  * Returns: [`<Immediate>`](https://nodejs.org/docs/latest/api/timers.html#class-immediate) a reference to `immediate`


When called, requests that the Node.js event loop _not_ exit so long as the `Immediate` is active. Calling `immediate.ref()` multiple times will have no effect.
By default, all `Immediate` objects are "ref'ed", making it normally unnecessary to call `immediate.ref()` unless `immediate.unref()` had been called previously.
####  `immediate.unref()`[#](https://nodejs.org/docs/latest/api/timers.html#immediateunref)
Added in: v9.7.0
  * Returns: [`<Immediate>`](https://nodejs.org/docs/latest/api/timers.html#class-immediate) a reference to `immediate`


When called, the active `Immediate` object will not require the Node.js event loop to remain active. If there is no other activity keeping the event loop running, the process may exit before the `Immediate` object's callback is invoked. Calling `immediate.unref()` multiple times will have no effect.
####  `immediate[Symbol.dispose]()`[#](https://nodejs.org/docs/latest/api/timers.html#immediatesymboldispose)
Added in: v20.5.0, v18.18.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Cancels the immediate. This is similar to calling `clearImmediate()`.
### Class: `Timeout`[#](https://nodejs.org/docs/latest/api/timers.html#class-timeout)
This object is created internally and is returned from [`setTimeout()`](https://nodejs.org/docs/latest/api/timers.html#settimeoutcallback-delay-args) and [`setInterval()`](https://nodejs.org/docs/latest/api/timers.html#setintervalcallback-delay-args). It can be passed to either [`clearTimeout()`](https://nodejs.org/docs/latest/api/timers.html#cleartimeouttimeout) or [`clearInterval()`](https://nodejs.org/docs/latest/api/timers.html#clearintervaltimeout) in order to cancel the scheduled actions.
By default, when a timer is scheduled using either [`setTimeout()`](https://nodejs.org/docs/latest/api/timers.html#settimeoutcallback-delay-args) or [`setInterval()`](https://nodejs.org/docs/latest/api/timers.html#setintervalcallback-delay-args), the Node.js event loop will continue running as long as the timer is active. Each of the `Timeout` objects returned by these functions export both `timeout.ref()` and `timeout.unref()` functions that can be used to control this default behavior.
####  `timeout.close()`[#](https://nodejs.org/docs/latest/api/timers.html#timeoutclose)
Added in: v0.9.1
Stability: 3 - Legacy: Use [`clearTimeout()`](https://nodejs.org/docs/latest/api/timers.html#cleartimeouttimeout) instead.
  * Returns: [`<Timeout>`](https://nodejs.org/docs/latest/api/timers.html#class-timeout) a reference to `timeout`


Cancels the timeout.
####  `timeout.hasRef()`[#](https://nodejs.org/docs/latest/api/timers.html#timeouthasref)
Added in: v11.0.0
  * Returns:


If true, the `Timeout` object will keep the Node.js event loop active.
####  `timeout.ref()`[#](https://nodejs.org/docs/latest/api/timers.html#timeoutref)
Added in: v0.9.1
  * Returns: [`<Timeout>`](https://nodejs.org/docs/latest/api/timers.html#class-timeout) a reference to `timeout`


When called, requests that the Node.js event loop _not_ exit so long as the `Timeout` is active. Calling `timeout.ref()` multiple times will have no effect.
By default, all `Timeout` objects are "ref'ed", making it normally unnecessary to call `timeout.ref()` unless `timeout.unref()` had been called previously.
####  `timeout.refresh()`[#](https://nodejs.org/docs/latest/api/timers.html#timeoutrefresh)
Added in: v10.2.0
  * Returns: [`<Timeout>`](https://nodejs.org/docs/latest/api/timers.html#class-timeout) a reference to `timeout`


Sets the timer's start time to the current time, and reschedules the timer to call its callback at the previously specified duration adjusted to the current time. This is useful for refreshing a timer without allocating a new JavaScript object.
Using this on a timer that has already called its callback will reactivate the timer.
####  `timeout.unref()`[#](https://nodejs.org/docs/latest/api/timers.html#timeoutunref)
Added in: v0.9.1
  * Returns: [`<Timeout>`](https://nodejs.org/docs/latest/api/timers.html#class-timeout) a reference to `timeout`


When called, the active `Timeout` object will not require the Node.js event loop to remain active. If there is no other activity keeping the event loop running, the process may exit before the `Timeout` object's callback is invoked. Calling `timeout.unref()` multiple times will have no effect.
####  `timeout[Symbol.toPrimitive]()`[#](https://nodejs.org/docs/latest/api/timers.html#timeoutsymboltoprimitive)
Added in: v14.9.0, v12.19.0
  * Returns: `timeout`


Coerce a `Timeout` to a primitive. The primitive can be used to clear the `Timeout`. The primitive can only be used in the same thread where the timeout was created. Therefore, to use it across [`worker_threads`](https://nodejs.org/docs/latest/api/worker_threads.html) it must first be passed to the correct thread. This allows enhanced compatibility with browser `setTimeout()` and `setInterval()` implementations.
####  `timeout[Symbol.dispose]()`[#](https://nodejs.org/docs/latest/api/timers.html#timeoutsymboldispose)
Added in: v20.5.0, v18.18.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Cancels the timeout.
### Scheduling timers[#](https://nodejs.org/docs/latest/api/timers.html#scheduling-timers)
A timer in Node.js is an internal construct that calls a given function after a certain period of time. When a timer's function is called varies depending on which method was used to create the timer and what other work the Node.js event loop is doing.
####  `setImmediate(callback[, ...args])`[#](https://nodejs.org/docs/latest/api/timers.html#setimmediatecallback-args)
Added in: v0.9.1History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `callback` [Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#setimmediate-vs-settimeout)
  * `...args` `callback` is called.
  * Returns: [`<Immediate>`](https://nodejs.org/docs/latest/api/timers.html#class-immediate) for use with [`clearImmediate()`](https://nodejs.org/docs/latest/api/timers.html#clearimmediateimmediate)


Schedules the "immediate" execution of the `callback` after I/O events' callbacks.
When multiple calls to `setImmediate()` are made, the `callback` functions are queued for execution in the order in which they are created. The entire callback queue is processed every event loop iteration. If an immediate timer is queued from inside an executing callback, that timer will not be triggered until the next event loop iteration.
If `callback` is not a function, a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) will be thrown.
This method has a custom variant for promises that is available using [`timersPromises.setImmediate()`](https://nodejs.org/docs/latest/api/timers.html#timerspromisessetimmediatevalue-options).
####  `setInterval(callback[, delay[, ...args]])`[#](https://nodejs.org/docs/latest/api/timers.html#setintervalcallback-delay-args)
Added in: v0.0.1History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `callback`
  * `delay` `callback`. **Default:** `1`.
  * `...args` `callback` is called.
  * Returns: [`<Timeout>`](https://nodejs.org/docs/latest/api/timers.html#class-timeout) for use with [`clearInterval()`](https://nodejs.org/docs/latest/api/timers.html#clearintervaltimeout)


Schedules repeated execution of `callback` every `delay` milliseconds.
When `delay` is larger than `2147483647` or less than `1` or `NaN`, the `delay` will be set to `1`. Non-integer delays are truncated to an integer.
If `callback` is not a function, a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) will be thrown.
This method has a custom variant for promises that is available using [`timersPromises.setInterval()`](https://nodejs.org/docs/latest/api/timers.html#timerspromisessetintervaldelay-value-options).
####  `setTimeout(callback[, delay[, ...args]])`[#](https://nodejs.org/docs/latest/api/timers.html#settimeoutcallback-delay-args)
Added in: v0.0.1History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `callback`
  * `delay` `callback`. **Default:** `1`.
  * `...args` `callback` is called.
  * Returns: [`<Timeout>`](https://nodejs.org/docs/latest/api/timers.html#class-timeout) for use with [`clearTimeout()`](https://nodejs.org/docs/latest/api/timers.html#cleartimeouttimeout)


Schedules execution of a one-time `callback` after `delay` milliseconds.
The `callback` will likely not be invoked in precisely `delay` milliseconds. Node.js makes no guarantees about the exact timing of when callbacks will fire, nor of their ordering. The callback will be called as close as possible to the time specified.
When `delay` is larger than `2147483647` or less than `1` or `NaN`, the `delay` will be set to `1`. Non-integer delays are truncated to an integer.
If `callback` is not a function, a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) will be thrown.
This method has a custom variant for promises that is available using [`timersPromises.setTimeout()`](https://nodejs.org/docs/latest/api/timers.html#timerspromisessettimeoutdelay-value-options).
### Cancelling timers[#](https://nodejs.org/docs/latest/api/timers.html#cancelling-timers)
The [`setImmediate()`](https://nodejs.org/docs/latest/api/timers.html#setimmediatecallback-args), [`setInterval()`](https://nodejs.org/docs/latest/api/timers.html#setintervalcallback-delay-args), and [`setTimeout()`](https://nodejs.org/docs/latest/api/timers.html#settimeoutcallback-delay-args) methods each return objects that represent the scheduled timers. These can be used to cancel the timer and prevent it from triggering.
For the promisified variants of [`setImmediate()`](https://nodejs.org/docs/latest/api/timers.html#setimmediatecallback-args) and [`setTimeout()`](https://nodejs.org/docs/latest/api/timers.html#settimeoutcallback-delay-args), an [`AbortController`](https://nodejs.org/docs/latest/api/globals.html#class-abortcontroller) may be used to cancel the timer. When canceled, the returned Promises will be rejected with an `'AbortError'`.
For `setImmediate()`:
```
import { setImmediate as setImmediatePromise } from 'node:timers/promises';

const ac = new AbortController();
const signal = ac.signal;

// We do not `await` the promise so `ac.abort()` is called concurrently.
setImmediatePromise('foobar', { signal })
  .then(console.log)
  .catch((err) => {
    if (err.name === 'AbortError')
      console.error('The immediate was aborted');
  });

ac.abort();
const { setImmediate: setImmediatePromise } = require('node:timers/promises');

const ac = new AbortController();
const signal = ac.signal;

setImmediatePromise('foobar', { signal })
  .then(console.log)
  .catch((err) => {
    if (err.name === 'AbortError')
      console.error('The immediate was aborted');
  });

ac.abort();
copy
```

For `setTimeout()`:
```
import { setTimeout as setTimeoutPromise } from 'node:timers/promises';

const ac = new AbortController();
const signal = ac.signal;

// We do not `await` the promise so `ac.abort()` is called concurrently.
setTimeoutPromise(1000, 'foobar', { signal })
  .then(console.log)
  .catch((err) => {
    if (err.name === 'AbortError')
      console.error('The timeout was aborted');
  });

ac.abort();
const { setTimeout: setTimeoutPromise } = require('node:timers/promises');

const ac = new AbortController();
const signal = ac.signal;

setTimeoutPromise(1000, 'foobar', { signal })
  .then(console.log)
  .catch((err) => {
    if (err.name === 'AbortError')
      console.error('The timeout was aborted');
  });

ac.abort();
copy
```

####  `clearImmediate(immediate)`[#](https://nodejs.org/docs/latest/api/timers.html#clearimmediateimmediate)
Added in: v0.9.1
  * `immediate` [`<Immediate>`](https://nodejs.org/docs/latest/api/timers.html#class-immediate) An `Immediate` object as returned by [`setImmediate()`](https://nodejs.org/docs/latest/api/timers.html#setimmediatecallback-args).


Cancels an `Immediate` object created by [`setImmediate()`](https://nodejs.org/docs/latest/api/timers.html#setimmediatecallback-args).
####  `clearInterval(timeout)`[#](https://nodejs.org/docs/latest/api/timers.html#clearintervaltimeout)
Added in: v0.0.1
  * `timeout` [`<Timeout>`](https://nodejs.org/docs/latest/api/timers.html#class-timeout) | `Timeout` object as returned by [`setInterval()`](https://nodejs.org/docs/latest/api/timers.html#setintervalcallback-delay-args) or the [primitive](https://nodejs.org/docs/latest/api/timers.html#timeoutsymboltoprimitive) of the `Timeout` object as a string or a number.


Cancels a `Timeout` object created by [`setInterval()`](https://nodejs.org/docs/latest/api/timers.html#setintervalcallback-delay-args).
####  `clearTimeout(timeout)`[#](https://nodejs.org/docs/latest/api/timers.html#cleartimeouttimeout)
Added in: v0.0.1
  * `timeout` [`<Timeout>`](https://nodejs.org/docs/latest/api/timers.html#class-timeout) | `Timeout` object as returned by [`setTimeout()`](https://nodejs.org/docs/latest/api/timers.html#settimeoutcallback-delay-args) or the [primitive](https://nodejs.org/docs/latest/api/timers.html#timeoutsymboltoprimitive) of the `Timeout` object as a string or a number.


Cancels a `Timeout` object created by [`setTimeout()`](https://nodejs.org/docs/latest/api/timers.html#settimeoutcallback-delay-args).
### Timers Promises API[#](https://nodejs.org/docs/latest/api/timers.html#timers-promises-api)
Added in: v15.0.0History Version | Changes
---|---
v16.0.0 | Graduated from experimental.
The `timers/promises` API provides an alternative set of timer functions that return `Promise` objects. The API is accessible via `require('node:timers/promises')`.
```
import {
  setTimeout,
  setImmediate,
  setInterval,
} from 'node:timers/promises';
const {
  setTimeout,
  setImmediate,
  setInterval,
} = require('node:timers/promises');
copy
```

####  `timersPromises.setTimeout([delay[, value[, options]]])`[#](https://nodejs.org/docs/latest/api/timers.html#timerspromisessettimeoutdelay-value-options)
Added in: v15.0.0
  * `delay` **Default:** `1`.
  * `value`
  * `options`
    * `ref` `false` to indicate that the scheduled `Timeout` should not require the Node.js event loop to remain active. **Default:** `true`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) An optional `AbortSignal` that can be used to cancel the scheduled `Timeout`.

```
import {
  setTimeout,
} from 'node:timers/promises';

const res = await setTimeout(100, 'result');

console.log(res);  // Prints 'result'
const {
  setTimeout,
} = require('node:timers/promises');

setTimeout(100, 'result').then((res) => {
  console.log(res);  // Prints 'result'
});
copy
```

####  `timersPromises.setImmediate([value[, options]])`[#](https://nodejs.org/docs/latest/api/timers.html#timerspromisessetimmediatevalue-options)
Added in: v15.0.0
  * `value`
  * `options`
    * `ref` `false` to indicate that the scheduled `Immediate` should not require the Node.js event loop to remain active. **Default:** `true`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) An optional `AbortSignal` that can be used to cancel the scheduled `Immediate`.

```
import {
  setImmediate,
} from 'node:timers/promises';

const res = await setImmediate('result');

console.log(res);  // Prints 'result'
const {
  setImmediate,
} = require('node:timers/promises');

setImmediate('result').then((res) => {
  console.log(res);  // Prints 'result'
});
copy
```

####  `timersPromises.setInterval([delay[, value[, options]]])`[#](https://nodejs.org/docs/latest/api/timers.html#timerspromisessetintervaldelay-value-options)
Added in: v15.9.0
Returns an async iterator that generates values in an interval of `delay` ms. If `ref` is `true`, you need to call `next()` of async iterator explicitly or implicitly to keep the event loop alive.
  * `delay` **Default:** `1`.
  * `value`
  * `options`
    * `ref` `false` to indicate that the scheduled `Timeout` between iterations should not require the Node.js event loop to remain active. **Default:** `true`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) An optional `AbortSignal` that can be used to cancel the scheduled `Timeout` between operations.

```
import {
  setInterval,
} from 'node:timers/promises';

const interval = 100;
for await (const startTime of setInterval(interval, Date.now())) {
  const now = Date.now();
  console.log(now);
  if ((now - startTime) > 1000)
    break;
}
console.log(Date.now());
const {
  setInterval,
} = require('node:timers/promises');
const interval = 100;

(async function() {
  for await (const startTime of setInterval(interval, Date.now())) {
    const now = Date.now();
    console.log(now);
    if ((now - startTime) > 1000)
      break;
  }
  console.log(Date.now());
})();
copy
```

####  `timersPromises.scheduler.wait(delay[, options])`[#](https://nodejs.org/docs/latest/api/timers.html#timerspromisesschedulerwaitdelay-options)
Added in: v17.3.0, v16.14.0
Stability: 1 - Experimental
  * `delay`
  * `options`
    * `ref` `false` to indicate that the scheduled `Timeout` should not require the Node.js event loop to remain active. **Default:** `true`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) An optional `AbortSignal` that can be used to cancel waiting.
  * Returns:


An experimental API defined by the
Calling `timersPromises.scheduler.wait(delay, options)` is equivalent to calling `timersPromises.setTimeout(delay, undefined, options)`.
```
import { scheduler } from 'node:timers/promises';

await scheduler.wait(1000); // Wait one second before continuing
copy
```

####  `timersPromises.scheduler.yield()`[#](https://nodejs.org/docs/latest/api/timers.html#timerspromisesscheduleryield)
Added in: v17.3.0, v16.14.0
Stability: 1 - Experimental
  * Returns:


An experimental API defined by the
Calling `timersPromises.scheduler.yield()` is equivalent to calling `timersPromises.setImmediate()` with no arguments.
