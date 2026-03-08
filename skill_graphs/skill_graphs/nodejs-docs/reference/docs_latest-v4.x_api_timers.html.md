[ Node.js ](https://nodejs.org/ "Go back to the home page")
  * [About these Docs](https://nodejs.org/docs/latest-v4.x/api/documentation.html)
  * [Usage & Example](https://nodejs.org/docs/latest-v4.x/api/synopsis.html)


  * [Assertion Testing](https://nodejs.org/docs/latest-v4.x/api/assert.html)
  * [Buffer](https://nodejs.org/docs/latest-v4.x/api/buffer.html)
  * [C/C++ Addons](https://nodejs.org/docs/latest-v4.x/api/addons.html)
  * [Child Processes](https://nodejs.org/docs/latest-v4.x/api/child_process.html)
  * [Cluster](https://nodejs.org/docs/latest-v4.x/api/cluster.html)
  * [Command Line Options](https://nodejs.org/docs/latest-v4.x/api/cli.html)
  * [Console](https://nodejs.org/docs/latest-v4.x/api/console.html)
  * [Crypto](https://nodejs.org/docs/latest-v4.x/api/crypto.html)
  * [Debugger](https://nodejs.org/docs/latest-v4.x/api/debugger.html)
  * [DNS](https://nodejs.org/docs/latest-v4.x/api/dns.html)
  * [Domain](https://nodejs.org/docs/latest-v4.x/api/domain.html)
  * [Errors](https://nodejs.org/docs/latest-v4.x/api/errors.html)
  * [Events](https://nodejs.org/docs/latest-v4.x/api/events.html)
  * [File System](https://nodejs.org/docs/latest-v4.x/api/fs.html)
  * [Globals](https://nodejs.org/docs/latest-v4.x/api/globals.html)
  * [HTTP](https://nodejs.org/docs/latest-v4.x/api/http.html)
  * [HTTPS](https://nodejs.org/docs/latest-v4.x/api/https.html)
  * [Modules](https://nodejs.org/docs/latest-v4.x/api/modules.html)
  * [Net](https://nodejs.org/docs/latest-v4.x/api/net.html)
  * [OS](https://nodejs.org/docs/latest-v4.x/api/os.html)
  * [Path](https://nodejs.org/docs/latest-v4.x/api/path.html)
  * [Process](https://nodejs.org/docs/latest-v4.x/api/process.html)
  * [Punycode](https://nodejs.org/docs/latest-v4.x/api/punycode.html)
  * [Query Strings](https://nodejs.org/docs/latest-v4.x/api/querystring.html)
  * [Readline](https://nodejs.org/docs/latest-v4.x/api/readline.html)
  * [REPL](https://nodejs.org/docs/latest-v4.x/api/repl.html)
  * [Stream](https://nodejs.org/docs/latest-v4.x/api/stream.html)
  * [String Decoder](https://nodejs.org/docs/latest-v4.x/api/string_decoder.html)
  * [Timers](https://nodejs.org/docs/latest-v4.x/api/timers.html)
  * [TLS/SSL](https://nodejs.org/docs/latest-v4.x/api/tls.html)
  * [TTY](https://nodejs.org/docs/latest-v4.x/api/tty.html)
  * [UDP/Datagram](https://nodejs.org/docs/latest-v4.x/api/dgram.html)
  * [URL](https://nodejs.org/docs/latest-v4.x/api/url.html)
  * [Utilities](https://nodejs.org/docs/latest-v4.x/api/util.html)
  * [V8](https://nodejs.org/docs/latest-v4.x/api/v8.html)
  * [VM](https://nodejs.org/docs/latest-v4.x/api/vm.html)
  * [ZLIB](https://nodejs.org/docs/latest-v4.x/api/zlib.html)


# Node.js v4.9.1 Documentation
[Index](https://nodejs.org/docs/latest-v4.x/api/index.html) | [View on single page](https://nodejs.org/docs/latest-v4.x/api/all.html) | [View as JSON](https://nodejs.org/docs/latest-v4.x/api/timers.json)
* * *
## Table of Contents
  * [Timers](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_timers)
    * [clearImmediate(immediateObject)](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_clearimmediate_immediateobject)
    * [clearInterval(intervalObject)](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_clearinterval_intervalobject)
    * [clearTimeout(timeoutObject)](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_cleartimeout_timeoutobject)
    * [ref()](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_ref)
    * [setImmediate(callback[, arg][, ...])](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_setimmediate_callback_arg)
    * [setInterval(callback, delay[, arg][, ...])](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_setinterval_callback_delay_arg)
    * [setTimeout(callback, delay[, arg][, ...])](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_settimeout_callback_delay_arg)
    * [unref()](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_unref)


# Timers[#](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_timers)
```
Stability: 3 - Locked
```

All of the timer functions are globals. You do not need to `require()` this module in order to use them.
## clearImmediate(immediateObject)[#](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_clearimmediate_immediateobject)
Added in: v0.9.1
Stops an `immediateObject`, as created by [`setImmediate`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_setimmediate_callback_arg), from triggering.
## clearInterval(intervalObject)[#](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_clearinterval_intervalobject)
Added in: v0.0.1
Stops an `intervalObject`, as created by [`setInterval`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_setinterval_callback_delay_arg), from triggering.
## clearTimeout(timeoutObject)[#](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_cleartimeout_timeoutobject)
Added in: v0.0.1
Prevents a `timeoutObject`, as created by [`setTimeout`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_settimeout_callback_delay_arg), from triggering.
## ref()[#](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_ref)
Added in: v0.9.1
If a timer was previously `unref()`d, then `ref()` can be called to explicitly request the timer hold the program open. If the timer is already `ref`d calling `ref` again will have no effect.
Returns the timer.
## setImmediate(callback[, arg][, ...])[#](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_setimmediate_callback_arg)
Added in: v0.9.1
Schedules "immediate" execution of `callback` after I/O events' callbacks and before timers set by [`setTimeout`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_settimeout_callback_delay_arg) and [`setInterval`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_setinterval_callback_delay_arg) are triggered. Returns an `immediateObject` for possible use with [`clearImmediate`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_clearimmediate_immediateobject). Additional optional arguments may be passed to the callback.
Callbacks for immediates are queued in the order in which they were created. The entire callback queue is processed every event loop iteration. If an immediate is queued from inside an executing callback, that immediate won't fire until the next event loop iteration.
## setInterval(callback, delay[, arg][, ...])[#](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_setinterval_callback_delay_arg)
Added in: v0.0.1
Schedules repeated execution of `callback` every `delay` milliseconds. Returns a `intervalObject` for possible use with [`clearInterval`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_clearinterval_intervalobject). Additional optional arguments may be passed to the callback.
To follow browser behavior, when using delays larger than 2147483647 milliseconds (approximately 25 days) or less than 1, Node.js will use 1 as the `delay`.
## setTimeout(callback, delay[, arg][, ...])[#](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_settimeout_callback_delay_arg)
Added in: v0.0.1
Schedules execution of a one-time `callback` after `delay` milliseconds. Returns a `timeoutObject` for possible use with [`clearTimeout`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_cleartimeout_timeoutobject). Additional optional arguments may be passed to the callback.
The callback will likely not be invoked in precisely `delay` milliseconds. Node.js makes no guarantees about the exact timing of when callbacks will fire, nor of their ordering. The callback will be called as close as possible to the time specified.
To follow browser behavior, when using delays larger than 2147483647 milliseconds (approximately 25 days) or less than 1, the timeout is executed immediately, as if the `delay` was set to 1.
## unref()[#](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_unref)
Added in: v0.9.1
The opaque value returned by [`setTimeout`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_settimeout_callback_delay_arg) and [`setInterval`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_setinterval_callback_delay_arg) also has the method `timer.unref()` which allows the creation of a timer that is active but if it is the only item left in the event loop, it won't keep the program running. If the timer is already `unref`d calling `unref` again will have no effect.
In the case of [`setTimeout`](https://nodejs.org/docs/latest-v4.x/api/timers.html#timers_settimeout_callback_delay_arg), `unref` creates a separate timer that will wakeup the event loop, creating too many of these may adversely effect event loop performance -- use wisely.
Returns the timer.
