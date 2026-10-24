![node.js](https://nodejs.org/docs/latest-v0.12.x/api/assets/logo.svg)
  * [Home](http://nodejs.org)
  * [Downloads](http://nodejs.org/download/)
  * [Docs](http://nodejs.org/documentation/)
  * [Community](http://nodejs.org/community/)
  * [About](http://nodejs.org/about/)
  * [Jobs](http://jobs.nodejs.org)
  * [Blog](http://blog.nodejs.org)


  * [About Docs](http://nodejs.org/documentation/)
  * [Tutorials](http://nodejs.org/documentation/tutorials/)
  * [Contributing](http://nodejs.org/documentation/contributing/)
  * [Workflow](http://nodejs.org/documentation/workflow/)
  * [Localization](http://nodejs.org/documentation/localization/)
  * [API Docs](http://nodejs.org/api/)


# Node.js v0.12.18 Manual & Documentation
[Index](https://nodejs.org/docs/latest-v0.12.x/api/index.html) | [View on single page](https://nodejs.org/docs/latest-v0.12.x/api/all.html) | [View as JSON](https://nodejs.org/docs/latest-v0.12.x/api/timers.json)
* * *
## Table of Contents
  * [Timers](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_timers)
    * [setTimeout(callback, delay[, arg][, ...])](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_settimeout_callback_delay_arg)
    * [clearTimeout(timeoutObject)](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_cleartimeout_timeoutobject)
    * [setInterval(callback, delay[, arg][, ...])](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_setinterval_callback_delay_arg)
    * [clearInterval(intervalObject)](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_clearinterval_intervalobject)
    * [unref()](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_unref)
    * [ref()](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_ref)
    * [setImmediate(callback[, arg][, ...])](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_setimmediate_callback_arg)
    * [clearImmediate(immediateObject)](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_clearimmediate_immediateobject)


# Timers[#](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_timers)
```
Stability: 5 - Locked
```

All of the timer functions are globals. You do not need to `require()` this module in order to use them.
## setTimeout(callback, delay[, arg][, ...])[#](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_settimeout_callback_delay_arg)
To schedule execution of a one-time `callback` after `delay` milliseconds. Returns a `timeoutObject` for possible use with `clearTimeout()`. Optionally you can also pass arguments to the callback.
It is important to note that your callback will probably not be called in exactly `delay` milliseconds - Node.js makes no guarantees about the exact timing of when the callback will fire, nor of the ordering things will fire in. The callback will be called as close as possible to the time specified.
## clearTimeout(timeoutObject)[#](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_cleartimeout_timeoutobject)
Prevents a timeout from triggering.
## setInterval(callback, delay[, arg][, ...])[#](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_setinterval_callback_delay_arg)
To schedule the repeated execution of `callback` every `delay` milliseconds. Returns a `intervalObject` for possible use with `clearInterval()`. Optionally you can also pass arguments to the callback.
## clearInterval(intervalObject)[#](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_clearinterval_intervalobject)
Stops an interval from triggering.
## unref()[#](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_unref)
The opaque value returned by `setTimeout` and `setInterval` also has the method `timer.unref()` which will allow you to create a timer that is active but if it is the only item left in the event loop won't keep the program running. If the timer is already `unref`d calling `unref` again will have no effect.
In the case of `setTimeout` when you `unref` you create a separate timer that will wakeup the event loop, creating too many of these may adversely effect event loop performance -- use wisely.
## ref()[#](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_ref)
If you had previously `unref()`d a timer you can call `ref()` to explicitly request the timer hold the program open. If the timer is already `ref`d calling `ref` again will have no effect.
## setImmediate(callback[, arg][, ...])[#](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_setimmediate_callback_arg)
To schedule the "immediate" execution of `callback` after I/O events callbacks and before `setTimeout` and `setInterval` . Returns an `immediateObject` for possible use with `clearImmediate()`. Optionally you can also pass arguments to the callback.
Callbacks for immediates are queued in the order in which they were created. The entire callback queue is processed every event loop iteration. If you queue an immediate from inside an executing callback, that immediate won't fire until the next event loop iteration.
## clearImmediate(immediateObject)[#](https://nodejs.org/docs/latest-v0.12.x/api/timers.html#timers_clearimmediate_immediateobject)
Stops an immediate from triggering.
  * [Downloads](http://nodejs.org/download/)


  * [Documentation](http://nodejs.org/documentation/)
  * [API Docs](http://nodejs.org/api/)
  * [Tutorials](http://nodejs.org/documentation/tutorials/)
  * [Localization](http://nodejs.org/documentation/localization/)


  * [Community](http://nodejs.org/community/)


  * [About](http://nodejs.org/about/)
  * [Organization](http://nodejs.org/about/organization/)
  * [Core Team](http://nodejs.org/about/core-team/)
  * [Resources](http://nodejs.org/about/resources/)


  * [Blog](http://blog.nodejs.org)


Copyright 2014 [trademark](https://nodejs.org/images/trademark-policy.pdf) of Joyent, Inc.
