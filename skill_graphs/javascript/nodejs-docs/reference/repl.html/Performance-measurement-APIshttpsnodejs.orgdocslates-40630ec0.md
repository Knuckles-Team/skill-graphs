## Performance measurement APIs[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performance-measurement-apis)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
This module provides an implementation of a subset of the W3C
Node.js supports the following
```
import { performance, PerformanceObserver } from 'node:perf_hooks';

const obs = new PerformanceObserver((items) => {
  console.log(items.getEntries()[0].duration);
  performance.clearMarks();
});
obs.observe({ type: 'measure' });
performance.measure('Start to Now');

performance.mark('A');
doSomeLongRunningProcess(() => {
  performance.measure('A to Now', 'A');

  performance.mark('B');
  performance.measure('A to B', 'A', 'B');
});
const { PerformanceObserver, performance } = require('node:perf_hooks');

const obs = new PerformanceObserver((items) => {
  console.log(items.getEntries()[0].duration);
});
obs.observe({ type: 'measure' });
performance.measure('Start to Now');

performance.mark('A');
(async function doSomeLongRunningProcess() {
  await new Promise((r) => setTimeout(r, 5000));
  performance.measure('A to Now', 'A');

  performance.mark('B');
  performance.measure('A to B', 'A', 'B');
})();
copy
```

###  `perf_hooks.performance`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#perf-hooksperformance)
Added in: v8.5.0
An object that can be used to collect performance metrics from the current Node.js instance. It is similar to
####  `performance.clearMarks([name])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceclearmarksname)
Added in: v8.5.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver.
  * `name`


If `name` is not provided, removes all `PerformanceMark` objects from the Performance Timeline. If `name` is provided, removes only the named mark.
####  `performance.clearMeasures([name])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceclearmeasuresname)
Added in: v16.7.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver.
  * `name`


If `name` is not provided, removes all `PerformanceMeasure` objects from the Performance Timeline. If `name` is provided, removes only the named measure.
####  `performance.clearResourceTimings([name])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceclearresourcetimingsname)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver.
  * `name`


If `name` is not provided, removes all `PerformanceResourceTiming` objects from the Resource Timeline. If `name` is provided, removes only the named resource.
####  `performance.eventLoopUtilization([utilization1[, utilization2]])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceeventlooputilizationutilization1-utilization2)
Added in: v14.10.0, v12.19.0History Version | Changes
---|---
v25.2.0 | Added `perf_hooks.eventLoopUtilization` alias.
  * `utilization1` `eventLoopUtilization()`.
  * `utilization2` `eventLoopUtilization()` prior to `utilization1`.
  * Returns:
    * `idle`
    * `active`
    * `utilization`


This is an alias of [`perf_hooks.eventLoopUtilization()`](https://nodejs.org/docs/latest/api/perf_hooks.html#perf_hookseventlooputilizationutilization1-utilization2).
_This property is an extension by Node.js. It is not available in Web browsers._
####  `performance.getEntries()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancegetentries)
Added in: v16.7.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver.
  * Returns: [`<PerformanceEntry[]>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


Returns a list of `PerformanceEntry` objects in chronological order with respect to `performanceEntry.startTime`. If you are only interested in performance entries of certain types or that have certain names, see `performance.getEntriesByType()` and `performance.getEntriesByName()`.
####  `performance.getEntriesByName(name[, type])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancegetentriesbynamename-type)
Added in: v16.7.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver.
  * `name`
  * `type`
  * Returns: [`<PerformanceEntry[]>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


Returns a list of `PerformanceEntry` objects in chronological order with respect to `performanceEntry.startTime` whose `performanceEntry.name` is equal to `name`, and optionally, whose `performanceEntry.entryType` is equal to `type`.
####  `performance.getEntriesByType(type)`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancegetentriesbytypetype)
Added in: v16.7.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver.
  * `type`
  * Returns: [`<PerformanceEntry[]>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


Returns a list of `PerformanceEntry` objects in chronological order with respect to `performanceEntry.startTime` whose `performanceEntry.entryType` is equal to `type`.
####  `performance.mark(name[, options])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancemarkname-options)
Added in: v8.5.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver. The name argument is no longer optional.
v16.0.0 | Updated to conform to the User Timing Level 3 specification.
  * `name`
  * `options`
    * `detail`
    * `startTime` **Default** : `performance.now()`.


Creates a new `PerformanceMark` entry in the Performance Timeline. A `PerformanceMark` is a subclass of `PerformanceEntry` whose `performanceEntry.entryType` is always `'mark'`, and whose `performanceEntry.duration` is always `0`. Performance marks are used to mark specific significant moments in the Performance Timeline.
The created `PerformanceMark` entry is put in the global Performance Timeline and can be queried with `performance.getEntries`, `performance.getEntriesByName`, and `performance.getEntriesByType`. When the observation is performed, the entries should be cleared from the global Performance Timeline manually with `performance.clearMarks`.
####  `performance.markResourceTiming(timingInfo, requestedUrl, initiatorType, global, cacheMode, bodyInfo, responseStatus[, deliveryType])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancemarkresourcetimingtiminginfo-requestedurl-initiatortype-global-cachemode-bodyinfo-responsestatus-deliverytype)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v22.2.0 | Added bodyInfo, responseStatus, and deliveryType arguments.
  * `timingInfo`
  * `requestedUrl`
  * `initiatorType`
  * `global`
  * `cacheMode`
  * `bodyInfo`
  * `responseStatus`
  * `deliveryType` **Default:** `''`.


_This property is an extension by Node.js. It is not available in Web browsers._
Creates a new `PerformanceResourceTiming` entry in the Resource Timeline. A `PerformanceResourceTiming` is a subclass of `PerformanceEntry` whose `performanceEntry.entryType` is always `'resource'`. Performance resources are used to mark moments in the Resource Timeline.
The created `PerformanceMark` entry is put in the global Resource Timeline and can be queried with `performance.getEntries`, `performance.getEntriesByName`, and `performance.getEntriesByType`. When the observation is performed, the entries should be cleared from the global Performance Timeline manually with `performance.clearResourceTimings`.
####  `performance.measure(name[, startMarkOrOptions[, endMark]])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancemeasurename-startmarkoroptions-endmark)
Added in: v8.5.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver.
v16.0.0 | Updated to conform to the User Timing Level 3 specification.
v13.13.0, v12.16.3 | Make `startMark` and `endMark` parameters optional.
  * `name`
  * `startMarkOrOptions`
    * `detail`
    * `duration`
    * `end`
    * `start`
  * `endMark` `startMarkOrOptions` is an


Creates a new `PerformanceMeasure` entry in the Performance Timeline. A `PerformanceMeasure` is a subclass of `PerformanceEntry` whose `performanceEntry.entryType` is always `'measure'`, and whose `performanceEntry.duration` measures the number of milliseconds elapsed since `startMark` and `endMark`.
The `startMark` argument may identify any _existing_ `PerformanceMark` in the Performance Timeline, or _may_ identify any of the timestamp properties provided by the `PerformanceNodeTiming` class. If the named `startMark` does not exist, an error is thrown.
The optional `endMark` argument must identify any _existing_ `PerformanceMark` in the Performance Timeline or any of the timestamp properties provided by the `PerformanceNodeTiming` class. `endMark` will be `performance.now()` if no parameter is passed, otherwise if the named `endMark` does not exist, an error will be thrown.
The created `PerformanceMeasure` entry is put in the global Performance Timeline and can be queried with `performance.getEntries`, `performance.getEntriesByName`, and `performance.getEntriesByType`. When the observation is performed, the entries should be cleared from the global Performance Timeline manually with `performance.clearMeasures`.
####  `performance.nodeTiming`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodetiming)
Added in: v8.5.0
  * Type: [`<PerformanceNodeTiming>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performancenodetiming)


_This property is an extension by Node.js. It is not available in Web browsers._
An instance of the `PerformanceNodeTiming` class that provides performance metrics for specific Node.js operational milestones.
####  `performance.now()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenow)
Added in: v8.5.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver.
  * Returns:


Returns the current high resolution millisecond timestamp, where 0 represents the start of the current `node` process.
####  `performance.setResourceTimingBufferSize(maxSize)`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancesetresourcetimingbuffersizemaxsize)
Added in: v18.8.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver.
Sets the global performance resource timing buffer size to the specified number of "resource" type performance entry objects.
By default the max buffer size is set to 250.
####  `performance.timeOrigin`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancetimeorigin)
Added in: v8.5.0
  * Type:


The `node` process began, measured in Unix time.
####  `performance.timerify(fn[, options])`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancetimerifyfn-options)
Added in: v8.5.0History Version | Changes
---|---
v25.2.0 | Added `perf_hooks.timerify` alias.
v16.0.0 | Added the histogram option.
v16.0.0 | Re-implemented to use pure-JavaScript and the ability to time async functions.
  * `fn`
  * `options`
    * `histogram` [`<RecordableHistogram>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-recordablehistogram-extends-histogram) A histogram object created using `perf_hooks.createHistogram()` that will record runtime durations in nanoseconds.


This is an alias of [`perf_hooks.timerify()`](https://nodejs.org/docs/latest/api/perf_hooks.html#perf_hookstimerifyfn-options).
_This property is an extension by Node.js. It is not available in Web browsers._
####  `performance.toJSON()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancetojson)
Added in: v16.1.0History Version | Changes
---|---
v19.0.0 | This method must be called with the `performance` object as the receiver.
An object which is JSON representation of the `performance` object. It is similar to
##### Event: `'resourcetimingbufferfull'`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#event-resourcetimingbufferfull)
Added in: v18.8.0
The `'resourcetimingbufferfull'` event is fired when the global performance resource timing buffer is full. Adjust resource timing buffer size with `performance.setResourceTimingBufferSize()` or clear the buffer with `performance.clearResourceTimings()` in the event listener to allow more entries to be added to the performance timeline buffer.
### Class: `PerformanceEntry`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)
Added in: v8.5.0
The constructor of this class is not exposed to users directly.
####  `performanceEntry.duration`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceentryduration)
Added in: v8.5.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceEntry` object as the receiver.
  * Type:


The total number of milliseconds elapsed for this entry. This value will not be meaningful for all Performance Entry types.
####  `performanceEntry.entryType`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceentryentrytype)
Added in: v8.5.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceEntry` object as the receiver.
  * Type:


The type of the performance entry. It may be one of:
  * `'dns'` (Node.js only)
  * `'function'` (Node.js only)
  * `'gc'` (Node.js only)
  * `'http2'` (Node.js only)
  * `'http'` (Node.js only)
  * `'mark'` (available on the Web)
  * `'measure'` (available on the Web)
  * `'net'` (Node.js only)
  * `'node'` (Node.js only)
  * `'resource'` (available on the Web)


####  `performanceEntry.name`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceentryname)
Added in: v8.5.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceEntry` object as the receiver.
  * Type:


The name of the performance entry.
####  `performanceEntry.startTime`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performanceentrystarttime)
Added in: v8.5.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceEntry` object as the receiver.
  * Type:


The high resolution millisecond timestamp marking the starting time of the Performance Entry.
### Class: `PerformanceMark`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performancemark)
Added in: v18.2.0, v16.17.0
  * Extends: [`<PerformanceEntry>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


Exposes marks created via the `Performance.mark()` method.
####  `performanceMark.detail`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancemarkdetail)
Added in: v16.0.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceMark` object as the receiver.
  * Type:


Additional detail specified when creating with `Performance.mark()` method.
### Class: `PerformanceMeasure`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performancemeasure)
Added in: v18.2.0, v16.17.0
  * Extends: [`<PerformanceEntry>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


Exposes measures created via the `Performance.measure()` method.
The constructor of this class is not exposed to users directly.
####  `performanceMeasure.detail`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancemeasuredetail)
Added in: v16.0.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceMeasure` object as the receiver.
  * Type:


Additional detail specified when creating with `Performance.measure()` method.
### Class: `PerformanceNodeEntry`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performancenodeentry)
Added in: v19.0.0
  * Extends: [`<PerformanceEntry>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


_This class is an extension by Node.js. It is not available in Web browsers._
Provides detailed Node.js timing data.
The constructor of this class is not exposed to users directly.
####  `performanceNodeEntry.detail`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodeentrydetail)
Added in: v16.0.0History Version | Changes
---|---
v19.0.0 | This property getter must be called with the `PerformanceNodeEntry` object as the receiver.
  * Type:


Additional detail specific to the `entryType`.
####  `performanceNodeEntry.flags`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodeentryflags)
Added in: v13.9.0, v12.17.0History Version | Changes
---|---
v16.0.0 | Runtime deprecated. Now moved to the detail property when entryType is 'gc'.
Stability: 0 - Deprecated: Use `performanceNodeEntry.detail` instead.
  * Type:


When `performanceEntry.entryType` is equal to `'gc'`, the `performance.flags` property contains additional information about garbage collection operation. The value may be one of:
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_NO`
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_CONSTRUCT_RETAINED`
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_FORCED`
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_SYNCHRONOUS_PHANTOM_PROCESSING`
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_ALL_AVAILABLE_GARBAGE`
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_ALL_EXTERNAL_MEMORY`
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_SCHEDULE_IDLE`


####  `performanceNodeEntry.kind`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodeentrykind)
Added in: v8.5.0History Version | Changes
---|---
v16.0.0 | Runtime deprecated. Now moved to the detail property when entryType is 'gc'.
Stability: 0 - Deprecated: Use `performanceNodeEntry.detail` instead.
  * Type:


When `performanceEntry.entryType` is equal to `'gc'`, the `performance.kind` property identifies the type of garbage collection operation that occurred. The value may be one of:
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_MAJOR`
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_MINOR`
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_INCREMENTAL`
  * `perf_hooks.constants.NODE_PERFORMANCE_GC_WEAKCB`


#### Garbage Collection ('gc') Details[#](https://nodejs.org/docs/latest/api/perf_hooks.html#garbage-collection-gc-details)
When `performanceEntry.type` is equal to `'gc'`, the `performanceNodeEntry.detail` property will be an
  * `kind`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_MAJOR`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_MINOR`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_INCREMENTAL`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_WEAKCB`
  * `flags`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_NO`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_CONSTRUCT_RETAINED`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_FORCED`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_SYNCHRONOUS_PHANTOM_PROCESSING`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_ALL_AVAILABLE_GARBAGE`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_ALL_EXTERNAL_MEMORY`
    * `perf_hooks.constants.NODE_PERFORMANCE_GC_FLAGS_SCHEDULE_IDLE`


#### HTTP ('http') Details[#](https://nodejs.org/docs/latest/api/perf_hooks.html#http-http-details)
When `performanceEntry.type` is equal to `'http'`, the `performanceNodeEntry.detail` property will be an
If `performanceEntry.name` is equal to `HttpClient`, the `detail` will contain the following properties: `req`, `res`. And the `req` property will be an `method`, `url`, `headers`, the `res` property will be an `statusCode`, `statusMessage`, `headers`.
If `performanceEntry.name` is equal to `HttpRequest`, the `detail` will contain the following properties: `req`, `res`. And the `req` property will be an `method`, `url`, `headers`, the `res` property will be an `statusCode`, `statusMessage`, `headers`.
This could add additional memory overhead and should only be used for diagnostic purposes, not left turned on in production by default.
#### HTTP/2 ('http2') Details[#](https://nodejs.org/docs/latest/api/perf_hooks.html#http2-http2-details)
When `performanceEntry.type` is equal to `'http2'`, the `performanceNodeEntry.detail` property will be an
If `performanceEntry.name` is equal to `Http2Stream`, the `detail` will contain the following properties:
  * `bytesRead` `DATA` frame bytes received for this `Http2Stream`.
  * `bytesWritten` `DATA` frame bytes sent for this `Http2Stream`.
  * `id` `Http2Stream`
  * `timeToFirstByte` `PerformanceEntry` `startTime` and the reception of the first `DATA` frame.
  * `timeToFirstByteSent` `PerformanceEntry` `startTime` and sending of the first `DATA` frame.
  * `timeToFirstHeader` `PerformanceEntry` `startTime` and the reception of the first header.


If `performanceEntry.name` is equal to `Http2Session`, the `detail` will contain the following properties:
  * `bytesRead` `Http2Session`.
  * `bytesWritten` `Http2Session`.
  * `framesReceived` `Http2Session`.
  * `framesSent` `Http2Session`.
  * `maxConcurrentStreams` `Http2Session`.
  * `pingRTT` `PING` frame and the reception of its acknowledgment. Only present if a `PING` frame has been sent on the `Http2Session`.
  * `streamAverageDuration` `Http2Stream` instances.
  * `streamCount` `Http2Stream` instances processed by the `Http2Session`.
  * `type` `'server'` or `'client'` to identify the type of `Http2Session`.


#### Timerify ('function') Details[#](https://nodejs.org/docs/latest/api/perf_hooks.html#timerify-function-details)
When `performanceEntry.type` is equal to `'function'`, the `performanceNodeEntry.detail` property will be an
#### Net ('net') Details[#](https://nodejs.org/docs/latest/api/perf_hooks.html#net-net-details)
When `performanceEntry.type` is equal to `'net'`, the `performanceNodeEntry.detail` property will be an
If `performanceEntry.name` is equal to `connect`, the `detail` will contain the following properties: `host`, `port`.
#### DNS ('dns') Details[#](https://nodejs.org/docs/latest/api/perf_hooks.html#dns-dns-details)
When `performanceEntry.type` is equal to `'dns'`, the `performanceNodeEntry.detail` property will be an
If `performanceEntry.name` is equal to `lookup`, the `detail` will contain the following properties: `hostname`, `family`, `hints`, `verbatim`, `addresses`.
If `performanceEntry.name` is equal to `lookupService`, the `detail` will contain the following properties: `host`, `port`, `hostname`, `service`.
If `performanceEntry.name` is equal to `queryxxx` or `getHostByAddr`, the `detail` will contain the following properties: `host`, `ttl`, `result`. The value of `result` is same as the result of `queryxxx` or `getHostByAddr`.
### Class: `PerformanceNodeTiming`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performancenodetiming)
Added in: v8.5.0
  * Extends: [`<PerformanceEntry>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-performanceentry)


_This property is an extension by Node.js. It is not available in Web browsers._
Provides timing details for Node.js itself. The constructor of this class is not exposed to users.
####  `performanceNodeTiming.bootstrapComplete`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodetimingbootstrapcomplete)
Added in: v8.5.0
  * Type:


The high resolution millisecond timestamp at which the Node.js process completed bootstrapping. If bootstrapping has not yet finished, the property has the value of -1.
####  `performanceNodeTiming.environment`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodetimingenvironment)
Added in: v8.5.0
  * Type:


The high resolution millisecond timestamp at which the Node.js environment was initialized.
####  `performanceNodeTiming.idleTime`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodetimingidletime)
Added in: v14.10.0, v12.19.0
  * Type:


The high resolution millisecond timestamp of the amount of time the event loop has been idle within the event loop's event provider (e.g. `epoll_wait`). This does not take CPU usage into consideration. If the event loop has not yet started (e.g., in the first tick of the main script), the property has the value of 0.
####  `performanceNodeTiming.loopExit`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodetimingloopexit)
Added in: v8.5.0
  * Type:


The high resolution millisecond timestamp at which the Node.js event loop exited. If the event loop has not yet exited, the property has the value of -1. It can only have a value of not -1 in a handler of the [`'exit'`](https://nodejs.org/docs/latest/api/process.html#event-exit) event.
####  `performanceNodeTiming.loopStart`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodetimingloopstart)
Added in: v8.5.0
  * Type:


The high resolution millisecond timestamp at which the Node.js event loop started. If the event loop has not yet started (e.g., in the first tick of the main script), the property has the value of -1.
####  `performanceNodeTiming.nodeStart`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#performancenodetimingnodestart)
