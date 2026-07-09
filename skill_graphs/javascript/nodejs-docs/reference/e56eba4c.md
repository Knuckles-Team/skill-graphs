Added in: v8.5.0
  * Type:


The high resolution millisecond timestamp at which the Node.js process was initialized.
####  `performanceNodeTiming.uvMetricsInfo`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodetiminguvmetricsinfo)
Added in: v22.8.0, v20.18.0
  * Returns:
    * `loopCount`
    * `events`
    * `eventsWaiting`


This is a wrapper to the `uv_metrics_info` function. It returns the current set of event loop metrics.
It is recommended to use this property inside a function whose execution was scheduled using `setImmediate` to avoid collecting metrics before finishing all operations scheduled during the current loop iteration.
```
const { performance } = require('node:perf_hooks');

setImmediate(() => {
  console.log(performance.nodeTiming.uvMetricsInfo);
});
import { performance } from 'node:perf_hooks';

setImmediate(() => {
  console.log(performance.nodeTiming.uvMetricsInfo);
});
copy
```

####  `performanceNodeTiming.v8Start`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodetimingv8start)
Added in: v8.5.0
  * Type:


The high resolution millisecond timestamp at which the V8 platform was initialized.
### Class: `PerformanceResourceTiming`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceresourcetiming)
Added in: v18.2.0, v16.17.0
  * Extends: [`<PerformanceEntry>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


Provides detailed network timing data regarding the loading of an application's resources.
The constructor of this class is not exposed to users directly.
####  `performanceResourceTiming.workerStart`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingworkerstart)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp at immediately before dispatching the `fetch` request. If the resource is not intercepted by a worker the property will always return 0.
####  `performanceResourceTiming.redirectStart`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingredirectstart)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp that represents the start time of the fetch which initiates the redirect.
####  `performanceResourceTiming.redirectEnd`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingredirectend)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp that will be created immediately after receiving the last byte of the response of the last redirect.
####  `performanceResourceTiming.fetchStart`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingfetchstart)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp immediately before the Node.js starts to fetch the resource.
####  `performanceResourceTiming.domainLookupStart`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingdomainlookupstart)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp immediately before the Node.js starts the domain name lookup for the resource.
####  `performanceResourceTiming.domainLookupEnd`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingdomainlookupend)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp representing the time immediately after the Node.js finished the domain name lookup for the resource.
####  `performanceResourceTiming.connectStart`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingconnectstart)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp representing the time immediately before Node.js starts to establish the connection to the server to retrieve the resource.
####  `performanceResourceTiming.connectEnd`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingconnectend)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp representing the time immediately after Node.js finishes establishing the connection to the server to retrieve the resource.
####  `performanceResourceTiming.secureConnectionStart`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingsecureconnectionstart)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp representing the time immediately before Node.js starts the handshake process to secure the current connection.
####  `performanceResourceTiming.requestStart`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingrequeststart)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp representing the time immediately before Node.js receives the first byte of the response from the server.
####  `performanceResourceTiming.responseEnd`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingresponseend)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


The high resolution millisecond timestamp representing the time immediately after Node.js receives the last byte of the resource or immediately before the transport connection is closed, whichever comes first.
####  `performanceResourceTiming.transferSize`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingtransfersize)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


A number representing the size (in octets) of the fetched resource. The size includes the response header fields plus the response payload body.
####  `performanceResourceTiming.encodedBodySize`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingencodedbodysize)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


A number representing the size (in octets) received from the fetch (HTTP or cache), of the payload body, before removing any applied content-codings.
####  `performanceResourceTiming.decodedBodySize`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingdecodedbodysize)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceResourceTiming` object as the receiver.
  * Type:


A number representing the size (in octets) received from the fetch (HTTP or cache), of the message body, after removing any applied content-codings.
####  `performanceResourceTiming.toJSON()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceresourcetimingtojson)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `PerformanceResourceTiming` object as the receiver.
Returns a `object` that is the JSON representation of the `PerformanceResourceTiming` object
### Class: `PerformanceObserver`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceobserver)
Added in: v8.5.0
####  `PerformanceObserver.supportedEntryTypes`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceobserversupportedentrytypes)
Added in: v16.0.0
  * Type:


Get supported types.
####  `new PerformanceObserver(callback)`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#new-performanceobservercallback)
Added in: v8.5.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `callback`
    * `list` [`<PerformanceObserverEntryList>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceobserverentrylist)
    * `observer` [`<PerformanceObserver>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceobserver)


`PerformanceObserver` objects provide notifications when new `PerformanceEntry` instances have been added to the Performance Timeline.
```
import { performance, PerformanceObserver } from 'node:perf_hooks';

const obs = new PerformanceObserver((list, observer) => {
  console.log(list.getEntries());

  performance.clearMarks();
  performance.clearMeasures();
  observer.disconnect();
});
obs.observe({ entryTypes: ['mark'], buffered: true });

performance.mark('test');
const {
  performance,
  PerformanceObserver,
} = require('node:perf_hooks');

const obs = new PerformanceObserver((list, observer) => {
  console.log(list.getEntries());

  performance.clearMarks();
  performance.clearMeasures();
  observer.disconnect();
});
obs.observe({ entryTypes: ['mark'], buffered: true });

performance.mark('test');
copy
```

Because `PerformanceObserver` instances introduce their own additional performance overhead, instances should not be left subscribed to notifications indefinitely. Users should disconnect observers as soon as they are no longer needed.
The `callback` is invoked when a `PerformanceObserver` is notified about new `PerformanceEntry` instances. The callback receives a `PerformanceObserverEntryList` instance and a reference to the `PerformanceObserver`.
####  `performanceObserver.disconnect()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceobserverdisconnect)
Added in: v8.5.0
Disconnects the `PerformanceObserver` instance from all notifications.
####  `performanceObserver.observe(options)`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceobserverobserveoptions)
Added in: v8.5.0History Version | Changes
---|---
v16.7.0 | Updated to conform to Performance Timeline Level 2. The buffered option has been added back.
v16.0.0 | Updated to conform to User Timing Level 3. The buffered option has been removed.
  * `options`
    * `type` [`<PerformanceEntry>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry) type. Must not be given if `entryTypes` is already specified.
    * `entryTypes` [`<PerformanceEntry>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry) instances the observer is interested in. If not provided an error will be thrown.
    * `buffered` `PerformanceEntry` buffered entries. If false, only `PerformanceEntry`s created after the time point are sent to the observer callback. **Default:** `false`.


Subscribes the [`<PerformanceObserver>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceobserver) instance to notifications of new [`<PerformanceEntry>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry) instances identified either by `options.entryTypes` or `options.type`:
```
import { performance, PerformanceObserver } from 'node:perf_hooks';

const obs = new PerformanceObserver((list, observer) => {
  // Called once asynchronously. `list` contains three items.
});
obs.observe({ type: 'mark' });

for (let n = 0; n < 3; n++)
  performance.mark(`test${n}`);
const {
  performance,
  PerformanceObserver,
} = require('node:perf_hooks');

const obs = new PerformanceObserver((list, observer) => {
  // Called once asynchronously. `list` contains three items.
});
obs.observe({ type: 'mark' });

for (let n = 0; n < 3; n++)
  performance.mark(`test${n}`);
copy
```

####  `performanceObserver.takeRecords()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceobservertakerecords)
Added in: v16.0.0
  * Returns: [`<PerformanceEntry[]>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry) Current list of entries stored in the performance observer, emptying it out.


### Class: `PerformanceObserverEntryList`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceobserverentrylist)
Added in: v8.5.0
The `PerformanceObserverEntryList` class is used to provide access to the `PerformanceEntry` instances passed to a `PerformanceObserver`. The constructor of this class is not exposed to users.
####  `performanceObserverEntryList.getEntries()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceobserverentrylistgetentries)
Added in: v8.5.0
  * Returns: [`<PerformanceEntry[]>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


Returns a list of `PerformanceEntry` objects in chronological order with respect to `performanceEntry.startTime`.
```
import { performance, PerformanceObserver } from 'node:perf_hooks';

const obs = new PerformanceObserver((perfObserverList, observer) => {
  console.log(perfObserverList.getEntries());
  /**
   * [
   *   PerformanceEntry {
   *     name: 'test',
   *     entryType: 'mark',
   *     startTime: 81.465639,
   *     duration: 0,
   *     detail: null
   *   },
   *   PerformanceEntry {
   *     name: 'meow',
   *     entryType: 'mark',
   *     startTime: 81.860064,
   *     duration: 0,
   *     detail: null
   *   }
   * ]
   */

  performance.clearMarks();
  performance.clearMeasures();
  observer.disconnect();
});
obs.observe({ type: 'mark' });

performance.mark('test');
performance.mark('meow');
const {
  performance,
  PerformanceObserver,
} = require('node:perf_hooks');

const obs = new PerformanceObserver((perfObserverList, observer) => {
  console.log(perfObserverList.getEntries());
  /**
   * [
   *   PerformanceEntry {
   *     name: 'test',
   *     entryType: 'mark',
   *     startTime: 81.465639,
   *     duration: 0,
   *     detail: null
   *   },
   *   PerformanceEntry {
   *     name: 'meow',
   *     entryType: 'mark',
   *     startTime: 81.860064,
   *     duration: 0,
   *     detail: null
   *   }
   * ]
   */

  performance.clearMarks();
  performance.clearMeasures();
  observer.disconnect();
});
obs.observe({ type: 'mark' });

performance.mark('test');
performance.mark('meow');
copy
```

####  `performanceObserverEntryList.getEntriesByName(name[, type])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceobserverentrylistgetentriesbynamename-type)
Added in: v8.5.0
  * `name`
  * `type`
  * Returns: [`<PerformanceEntry[]>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


Returns a list of `PerformanceEntry` objects in chronological order with respect to `performanceEntry.startTime` whose `performanceEntry.name` is equal to `name`, and optionally, whose `performanceEntry.entryType` is equal to `type`.
```
import { performance, PerformanceObserver } from 'node:perf_hooks';

const obs = new PerformanceObserver((perfObserverList, observer) => {
  console.log(perfObserverList.getEntriesByName('meow'));
  /**
   * [
   *   PerformanceEntry {
   *     name: 'meow',
   *     entryType: 'mark',
   *     startTime: 98.545991,
   *     duration: 0,
   *     detail: null
   *   }
   * ]
   */
  console.log(perfObserverList.getEntriesByName('nope')); // []

  console.log(perfObserverList.getEntriesByName('test', 'mark'));
  /**
   * [
   *   PerformanceEntry {
   *     name: 'test',
   *     entryType: 'mark',
   *     startTime: 63.518931,
   *     duration: 0,
   *     detail: null
   *   }
   * ]
   */
  console.log(perfObserverList.getEntriesByName('test', 'measure')); // []

  performance.clearMarks();
  performance.clearMeasures();
  observer.disconnect();
});
obs.observe({ entryTypes: ['mark', 'measure'] });

performance.mark('test');
performance.mark('meow');
const {
  performance,
  PerformanceObserver,
} = require('node:perf_hooks');

const obs = new PerformanceObserver((perfObserverList, observer) => {
  console.log(perfObserverList.getEntriesByName('meow'));
  /**
   * [
   *   PerformanceEntry {
   *     name: 'meow',
   *     entryType: 'mark',
   *     startTime: 98.545991,
   *     duration: 0,
   *     detail: null
   *   }
   * ]
   */
  console.log(perfObserverList.getEntriesByName('nope')); // []

  console.log(perfObserverList.getEntriesByName('test', 'mark'));
  /**
   * [
   *   PerformanceEntry {
   *     name: 'test',
   *     entryType: 'mark',
   *     startTime: 63.518931,
   *     duration: 0,
   *     detail: null
   *   }
   * ]
   */
  console.log(perfObserverList.getEntriesByName('test', 'measure')); // []

  performance.clearMarks();
  performance.clearMeasures();
  observer.disconnect();
});
obs.observe({ entryTypes: ['mark', 'measure'] });

performance.mark('test');
performance.mark('meow');
copy
```

####  `performanceObserverEntryList.getEntriesByType(type)`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceobserverentrylistgetentriesbytypetype)
Added in: v8.5.0
  * `type`
  * Returns: [`<PerformanceEntry[]>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


Returns a list of `PerformanceEntry` objects in chronological order with respect to `performanceEntry.startTime` whose `performanceEntry.entryType` is equal to `type`.
```
import { performance, PerformanceObserver } from 'node:perf_hooks';

const obs = new PerformanceObserver((perfObserverList, observer) => {
  console.log(perfObserverList.getEntriesByType('mark'));
  /**
   * [
   *   PerformanceEntry {
   *     name: 'test',
   *     entryType: 'mark',
   *     startTime: 55.897834,
   *     duration: 0,
   *     detail: null
   *   },
   *   PerformanceEntry {
   *     name: 'meow',
   *     entryType: 'mark',
   *     startTime: 56.350146,
   *     duration: 0,
   *     detail: null
   *   }
   * ]
   */
  performance.clearMarks();
  performance.clearMeasures();
  observer.disconnect();
});
obs.observe({ type: 'mark' });

performance.mark('test');
performance.mark('meow');
const {
  performance,
  PerformanceObserver,
} = require('node:perf_hooks');

const obs = new PerformanceObserver((perfObserverList, observer) => {
  console.log(perfObserverList.getEntriesByType('mark'));
  /**
   * [
   *   PerformanceEntry {
   *     name: 'test',
   *     entryType: 'mark',
   *     startTime: 55.897834,
   *     duration: 0,
   *     detail: null
   *   },
   *   PerformanceEntry {
   *     name: 'meow',
   *     entryType: 'mark',
   *     startTime: 56.350146,
   *     duration: 0,
   *     detail: null
   *   }
   * ]
   */
  performance.clearMarks();
  performance.clearMeasures();
  observer.disconnect();
});
obs.observe({ type: 'mark' });

performance.mark('test');
performance.mark('meow');
copy
```

###  `perf_hooks.createHistogram([options])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#perf-hookscreatehistogramoptions)
Added in: v15.9.0, v14.18.0
  * `options`
    * `lowest` **Default:** `1`.
    * `highest` `lowest`. **Default:** `Number.MAX_SAFE_INTEGER`.
    * `figures` `1` and `5`. **Default:** `3`.
  * Returns: [`<RecordableHistogram>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-recordablehistogram-extends-histogram)


Returns a [`<RecordableHistogram>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-recordablehistogram-extends-histogram).
###  `perf_hooks.eventLoopUtilization([utilization1[, utilization2]])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#perf-hookseventlooputilizationutilization1-utilization2)
Added in: v25.2.0
  * `utilization1` `eventLoopUtilization()`.
  * `utilization2` `eventLoopUtilization()` prior to `utilization1`.
  * Returns:
    * `idle`
    * `active`
    * `utilization`


The `eventLoopUtilization()` function returns an object that contains the cumulative duration of time the event loop has been both idle and active as a high resolution milliseconds timer. The `utilization` value is the calculated Event Loop Utilization (ELU).
If bootstrapping has not yet finished on the main thread the properties have the value of `0`. The ELU is immediately available on [Worker threads](https://nodejs.org/docs/latest/api/worker_threads.html#worker-threads) since bootstrap happens within the event loop.
Both `utilization1` and `utilization2` are optional parameters.
If `utilization1` is passed, then the delta between the current call's `active` and `idle` times, as well as the corresponding `utilization` value are calculated and returned (similar to [`process.hrtime()`](https://nodejs.org/docs/latest/api/process.html#processhrtimetime)).
If `utilization1` and `utilization2` are both passed, then the delta is calculated between the two arguments. This is a convenience option because, unlike [`process.hrtime()`](https://nodejs.org/docs/latest/api/process.html#processhrtimetime), calculating the ELU is more complex than a single subtraction.
ELU is similar to CPU utilization, except that it only measures event loop statistics and not CPU usage. It represents the percentage of time the event loop has spent outside the event loop's event provider (e.g. `epoll_wait`). No other CPU idle time is taken into consideration. The following is an example of how a mostly idle process will have a high ELU.
```
import { eventLoopUtilization } from 'node:perf_hooks';
import { spawnSync } from 'node:child_process';

setImmediate(() => {
  const elu = eventLoopUtilization();
  spawnSync('sleep', ['5']);
  console.log(eventLoopUtilization(elu).utilization);
});
'use strict';
const { eventLoopUtilization } = require('node:perf_hooks');
const { spawnSync } = require('node:child_process');

setImmediate(() => {
  const elu = eventLoopUtilization();
  spawnSync('sleep', ['5']);
  console.log(eventLoopUtilization(elu).utilization);
});
copy
```

Although the CPU is mostly idle while running this script, the value of `utilization` is `1`. This is because the call to [`child_process.spawnSync()`](https://nodejs.org/docs/latest/api/child_process.html#child_processspawnsynccommand-args-options) blocks the event loop from proceeding.
Passing in a user-defined object instead of the result of a previous call to `eventLoopUtilization()` will lead to undefined behavior. The return values are not guaranteed to reflect any correct state of the event loop.
###  `perf_hooks.monitorEventLoopDelay([options])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#perf-hooksmonitoreventloopdelayoptions)
Added in: v11.10.0
  * `options`
    * `resolution` **Default:** `10`.
  * Returns: [`<IntervalHistogram>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-intervalhistogram-extends-histogram)


_This property is an extension by Node.js. It is not available in Web browsers._
Creates an `IntervalHistogram` object that samples and reports the event loop delay over time. The delays will be reported in nanoseconds.
Using a timer to detect approximate event loop delay works because the execution of timers is tied specifically to the lifecycle of the libuv event loop. That is, a delay in the loop will cause a delay in the execution of the timer, and those delays are specifically what this API is intended to detect.
```
import { monitorEventLoopDelay } from 'node:perf_hooks';

const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();
// Do something.
h.disable();
console.log(h.min);
console.log(h.max);
console.log(h.mean);
console.log(h.stddev);
console.log(h.percentiles);
console.log(h.percentile(50));
console.log(h.percentile(99));
const { monitorEventLoopDelay } = require('node:perf_hooks');
const h = monitorEventLoopDelay({ resolution: 20 });
h.enable();
// Do something.
h.disable();
console.log(h.min);
console.log(h.max);
console.log(h.mean);
console.log(h.stddev);
console.log(h.percentiles);
console.log(h.percentile(50));
console.log(h.percentile(99));
copy
```

###  `perf_hooks.timerify(fn[, options])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#perf-hookstimerifyfn-options)
Added in: v25.2.0
  * `fn`
  * `options`
    * `histogram` [`<RecordableHistogram>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-recordablehistogram-extends-histogram) A histogram object created using `perf_hooks.createHistogram()` that will record runtime durations in nanoseconds.


_This property is an extension by Node.js. It is not available in Web browsers._
Wraps a function within a new function that measures the running time of the wrapped function. A `PerformanceObserver` must be subscribed to the `'function'` event type in order for the timing details to be accessed.
