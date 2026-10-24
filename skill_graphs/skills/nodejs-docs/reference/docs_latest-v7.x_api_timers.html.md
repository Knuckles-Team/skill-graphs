[ Node.js ](https://nodejs.org/ "Go back to the home page")
  * [About these Docs](https://nodejs.org/docs/latest-v7.x/api/documentation.html)
  * [Usage & Example](https://nodejs.org/docs/latest-v7.x/api/synopsis.html)


  * [Assertion Testing](https://nodejs.org/docs/latest-v7.x/api/assert.html)
  * [Buffer](https://nodejs.org/docs/latest-v7.x/api/buffer.html)
  * [C/C++ Addons](https://nodejs.org/docs/latest-v7.x/api/addons.html)
  * [Child Processes](https://nodejs.org/docs/latest-v7.x/api/child_process.html)
  * [Cluster](https://nodejs.org/docs/latest-v7.x/api/cluster.html)
  * [Command Line Options](https://nodejs.org/docs/latest-v7.x/api/cli.html)
  * [Console](https://nodejs.org/docs/latest-v7.x/api/console.html)
  * [Crypto](https://nodejs.org/docs/latest-v7.x/api/crypto.html)
  * [Debugger](https://nodejs.org/docs/latest-v7.x/api/debugger.html)
  * [Deprecated APIs](https://nodejs.org/docs/latest-v7.x/api/deprecations.html)
  * [DNS](https://nodejs.org/docs/latest-v7.x/api/dns.html)
  * [Domain](https://nodejs.org/docs/latest-v7.x/api/domain.html)
  * [Errors](https://nodejs.org/docs/latest-v7.x/api/errors.html)
  * [Events](https://nodejs.org/docs/latest-v7.x/api/events.html)
  * [File System](https://nodejs.org/docs/latest-v7.x/api/fs.html)
  * [Globals](https://nodejs.org/docs/latest-v7.x/api/globals.html)
  * [HTTP](https://nodejs.org/docs/latest-v7.x/api/http.html)
  * [HTTPS](https://nodejs.org/docs/latest-v7.x/api/https.html)
  * [Modules](https://nodejs.org/docs/latest-v7.x/api/modules.html)
  * [Net](https://nodejs.org/docs/latest-v7.x/api/net.html)
  * [OS](https://nodejs.org/docs/latest-v7.x/api/os.html)
  * [Path](https://nodejs.org/docs/latest-v7.x/api/path.html)
  * [Process](https://nodejs.org/docs/latest-v7.x/api/process.html)
  * [Punycode](https://nodejs.org/docs/latest-v7.x/api/punycode.html)
  * [Query Strings](https://nodejs.org/docs/latest-v7.x/api/querystring.html)
  * [Readline](https://nodejs.org/docs/latest-v7.x/api/readline.html)
  * [REPL](https://nodejs.org/docs/latest-v7.x/api/repl.html)
  * [Stream](https://nodejs.org/docs/latest-v7.x/api/stream.html)
  * [String Decoder](https://nodejs.org/docs/latest-v7.x/api/string_decoder.html)
  * [Timers](https://nodejs.org/docs/latest-v7.x/api/timers.html)
  * [TLS/SSL](https://nodejs.org/docs/latest-v7.x/api/tls.html)
  * [Tracing](https://nodejs.org/docs/latest-v7.x/api/tracing.html)
  * [TTY](https://nodejs.org/docs/latest-v7.x/api/tty.html)
  * [UDP/Datagram](https://nodejs.org/docs/latest-v7.x/api/dgram.html)
  * [URL](https://nodejs.org/docs/latest-v7.x/api/url.html)
  * [Utilities](https://nodejs.org/docs/latest-v7.x/api/util.html)
  * [V8](https://nodejs.org/docs/latest-v7.x/api/v8.html)
  * [VM](https://nodejs.org/docs/latest-v7.x/api/vm.html)
  * [ZLIB](https://nodejs.org/docs/latest-v7.x/api/zlib.html)


# Node.js v7.10.1 Documentation
[Index](https://nodejs.org/docs/latest-v7.x/api/index.html) | [View on single page](https://nodejs.org/docs/latest-v7.x/api/all.html) | [View as JSON](https://nodejs.org/docs/latest-v7.x/api/timers.json)
* * *
## Table of Contents
  * [Timers](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_timers)
    * [Class: Immediate](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_class_immediate)
    * [Class: Timeout](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_class_timeout)
      * [timeout.ref()](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_timeout_ref)
      * [timeout.unref()](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_timeout_unref)
    * [Scheduling Timers](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_scheduling_timers)
      * [setImmediate(callback[, ...args])](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setimmediate_callback_args)
      * [setInterval(callback, delay[, ...args])](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setinterval_callback_delay_args)
      * [setTimeout(callback, delay[, ...args])](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_settimeout_callback_delay_args)
    * [Cancelling Timers](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_cancelling_timers)
      * [clearImmediate(immediate)](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_clearimmediate_immediate)
      * [clearInterval(timeout)](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_clearinterval_timeout)
      * [clearTimeout(timeout)](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_cleartimeout_timeout)


# Timers[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_timers)
```
Stability[: 2](https://nodejs.org/docs/latest-v7.x/api/documentation.html#documentation_stability_index) - Stable
```

The `timer` module exposes a global API for scheduling functions to be called at some future period of time. Because the timer functions are globals, there is no need to call `require('timers')` to use the API.
The timer functions within Node.js implement a similar API as the timers API provided by Web Browsers but use a different internal implementation that is built around [the Node.js Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick).
## Class: Immediate[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_class_immediate)
This object is created internally and is returned from [`setImmediate()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setimmediate_callback_args). It can be passed to [`clearImmediate()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_clearimmediate_immediate) in order to cancel the scheduled actions.
## Class: Timeout[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_class_timeout)
This object is created internally and is returned from [`setTimeout()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_settimeout_callback_delay_args) and [`setInterval()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setinterval_callback_delay_args). It can be passed to [`clearTimeout()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_cleartimeout_timeout) or [`clearInterval()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_clearinterval_timeout) (respectively) in order to cancel the scheduled actions.
By default, when a timer is scheduled using either [`setTimeout()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_settimeout_callback_delay_args) or [`setInterval()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setinterval_callback_delay_args), the Node.js event loop will continue running as long as the timer is active. Each of the `Timeout` objects returned by these functions export both `timeout.ref()` and `timeout.unref()` functions that can be used to control this default behavior.
### timeout.ref()[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_timeout_ref)
Added in: v0.9.1
When called, requests that the Node.js event loop _not_ exit so long as the `Timeout` is active. Calling `timeout.ref()` multiple times will have no effect.
_Note_ : By default, all `Timeout` objects are "ref'd", making it normally unnecessary to call `timeout.ref()` unless `timeout.unref()` had been called previously.
Returns a reference to the `Timeout`.
### timeout.unref()[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_timeout_unref)
Added in: v0.9.1
When called, the active `Timeout` object will not require the Node.js event loop to remain active. If there is no other activity keeping the event loop running, the process may exit before the `Timeout` object's callback is invoked. Calling `timeout.unref()` multiple times will have no effect.
_Note_ : Calling `timeout.unref()` creates an internal timer that will wake the Node.js event loop. Creating too many of these can adversely impact performance of the Node.js application.
Returns a reference to the `Timeout`.
## Scheduling Timers[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_scheduling_timers)
A timer in Node.js is an internal construct that calls a given function after a certain period of time. When a timer's function is called varies depending on which method was used to create the timer and what other work the Node.js event loop is doing.
### setImmediate(callback[, ...args])[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setimmediate_callback_args)
Added in: v0.9.1
  * `callback` [the Node.js Event Loop](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick)
  * `...args` <any> Optional arguments to pass when the `callback` is called.


Schedules the "immediate" execution of the `callback` after I/O events' callbacks. Returns an `Immediate` for use with [`clearImmediate()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_clearimmediate_immediate).
When multiple calls to `setImmediate()` are made, the `callback` functions are queued for execution in the order in which they are created. The entire callback queue is processed every event loop iteration. If an immediate timer is queued from inside an executing callback, that timer will not be triggered until the next event loop iteration.
If `callback` is not a function, a [`TypeError`](https://nodejs.org/docs/latest-v7.x/api/errors.html#errors_class_typeerror) will be thrown.
### setInterval(callback, delay[, ...args])[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setinterval_callback_delay_args)
Added in: v0.0.1
  * `callback`
  * `delay` `callback`.
  * `...args` <any> Optional arguments to pass when the `callback` is called.


Schedules repeated execution of `callback` every `delay` milliseconds. Returns a `Timeout` for use with [`clearInterval()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_clearinterval_timeout).
When `delay` is larger than `2147483647` or less than `1`, the `delay` will be set to `1`.
If `callback` is not a function, a [`TypeError`](https://nodejs.org/docs/latest-v7.x/api/errors.html#errors_class_typeerror) will be thrown.
### setTimeout(callback, delay[, ...args])[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_settimeout_callback_delay_args)
Added in: v0.0.1
  * `callback`
  * `delay` `callback`.
  * `...args` <any> Optional arguments to pass when the `callback` is called.


Schedules execution of a one-time `callback` after `delay` milliseconds. Returns a `Timeout` for use with [`clearTimeout()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_cleartimeout_timeout).
The `callback` will likely not be invoked in precisely `delay` milliseconds. Node.js makes no guarantees about the exact timing of when callbacks will fire, nor of their ordering. The callback will be called as close as possible to the time specified.
_Note_ : When `delay` is larger than `2147483647` or less than `1`, the `delay` will be set to `1`.
If `callback` is not a function, a [`TypeError`](https://nodejs.org/docs/latest-v7.x/api/errors.html#errors_class_typeerror) will be thrown.
## Cancelling Timers[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_cancelling_timers)
The [`setImmediate()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setimmediate_callback_args), [`setInterval()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setinterval_callback_delay_args), and [`setTimeout()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_settimeout_callback_delay_args) methods each return objects that represent the scheduled timers. These can be used to cancel the timer and prevent it from triggering.
### clearImmediate(immediate)[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_clearimmediate_immediate)
Added in: v0.9.1
  * `immediate` <Immediate> An `Immediate` object as returned by [`setImmediate()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setimmediate_callback_args).


Cancels an `Immediate` object created by [`setImmediate()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setimmediate_callback_args).
### clearInterval(timeout)[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_clearinterval_timeout)
Added in: v0.0.1
  * `timeout` <Timeout> A `Timeout` object as returned by [`setInterval()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setinterval_callback_delay_args).


Cancels a `Timeout` object created by [`setInterval()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_setinterval_callback_delay_args).
### clearTimeout(timeout)[#](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_cleartimeout_timeout)
Added in: v0.0.1
  * `timeout` <Timeout> A `Timeout` object as returned by [`setTimeout()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_settimeout_callback_delay_args).


Cancels a `Timeout` object created by [`setTimeout()`](https://nodejs.org/docs/latest-v7.x/api/timers.html#timers_settimeout_callback_delay_args).
