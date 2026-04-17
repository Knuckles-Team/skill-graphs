```
import { timerify, performance, PerformanceObserver } from 'node:perf_hooks';

function someFunction() {
  console.log('hello world');
}

const wrapped = timerify(someFunction);

const obs = new PerformanceObserver((list) => {
  console.log(list.getEntries()[0].duration);

  performance.clearMarks();
  performance.clearMeasures();
  obs.disconnect();
});
obs.observe({ entryTypes: ['function'] });

// A performance timeline entry will be created
wrapped();
const {
  timerify,
  performance,
  PerformanceObserver,
} = require('node:perf_hooks');

function someFunction() {
  console.log('hello world');
}

const wrapped = timerify(someFunction);

const obs = new PerformanceObserver((list) => {
  console.log(list.getEntries()[0].duration);

  performance.clearMarks();
  performance.clearMeasures();
  obs.disconnect();
});
obs.observe({ entryTypes: ['function'] });

// A performance timeline entry will be created
wrapped();
copy
```

If the wrapped function returns a promise, a finally handler will be attached to the promise and the duration will be reported once the finally handler is invoked.
### Class: `Histogram`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-histogram)
Added in: v11.10.0
####  `histogram.count`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramcount)
Added in: v17.4.0, v16.14.0
  * Type:


The number of samples recorded by the histogram.
####  `histogram.countBigInt`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramcountbigint)
Added in: v17.4.0, v16.14.0
  * Type:


The number of samples recorded by the histogram.
####  `histogram.exceeds`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramexceeds)
Added in: v11.10.0
  * Type:


The number of times the event loop delay exceeded the maximum 1 hour event loop delay threshold.
####  `histogram.exceedsBigInt`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramexceedsbigint)
Added in: v17.4.0, v16.14.0
  * Type:


The number of times the event loop delay exceeded the maximum 1 hour event loop delay threshold.
####  `histogram.max`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogrammax)
Added in: v11.10.0
  * Type:


The maximum recorded event loop delay.
####  `histogram.maxBigInt`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogrammaxbigint)
Added in: v17.4.0, v16.14.0
  * Type:


The maximum recorded event loop delay.
####  `histogram.mean`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogrammean)
Added in: v11.10.0
  * Type:


The mean of the recorded event loop delays.
####  `histogram.min`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogrammin)
Added in: v11.10.0
  * Type:


The minimum recorded event loop delay.
####  `histogram.minBigInt`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramminbigint)
Added in: v17.4.0, v16.14.0
  * Type:


The minimum recorded event loop delay.
####  `histogram.percentile(percentile)`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogrampercentilepercentile)
Added in: v11.10.0
  * `percentile`
  * Returns:


Returns the value at the given percentile.
####  `histogram.percentileBigInt(percentile)`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogrampercentilebigintpercentile)
Added in: v17.4.0, v16.14.0
  * `percentile`
  * Returns:


Returns the value at the given percentile.
####  `histogram.percentiles`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogrampercentiles)
Added in: v11.10.0
  * Type:


Returns a `Map` object detailing the accumulated percentile distribution.
####  `histogram.percentilesBigInt`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogrampercentilesbigint)
Added in: v17.4.0, v16.14.0
  * Type:


Returns a `Map` object detailing the accumulated percentile distribution.
####  `histogram.reset()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramreset)
Added in: v11.10.0
Resets the collected histogram data.
####  `histogram.stddev`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramstddev)
Added in: v11.10.0
  * Type:


The standard deviation of the recorded event loop delays.
### Class: `IntervalHistogram extends Histogram`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-intervalhistogram-extends-histogram)
A `Histogram` that is periodically updated on a given interval.
####  `histogram.disable()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramdisable)
Added in: v11.10.0
  * Returns:


Disables the update interval timer. Returns `true` if the timer was stopped, `false` if it was already stopped.
####  `histogram.enable()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramenable)
Added in: v11.10.0
  * Returns:


Enables the update interval timer. Returns `true` if the timer was started, `false` if it was already started.
####  `histogram[Symbol.dispose]()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramsymboldispose)
Added in: v24.2.0
Disables the update interval timer when the histogram is disposed.
```
const { monitorEventLoopDelay } = require('node:perf_hooks');
{
  using hist = monitorEventLoopDelay({ resolution: 20 });
  hist.enable();
  // The histogram will be disabled when the block is exited.
}
copy
```

#### Cloning an `IntervalHistogram`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#cloning-an-intervalhistogram)
[`<IntervalHistogram>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-intervalhistogram-extends-histogram) instances can be cloned via [`<MessagePort>`](https://nodejs.org/docs/latest/api/worker_threads.html#class-messageport). On the receiving end, the histogram is cloned as a plain [`<Histogram>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-histogram) object that does not implement the `enable()` and `disable()` methods.
### Class: `RecordableHistogram extends Histogram`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#class-recordablehistogram-extends-histogram)
Added in: v15.9.0, v14.18.0
####  `histogram.add(other)`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramaddother)
Added in: v17.4.0, v16.14.0
  * `other` [`<RecordableHistogram>`](https://nodejs.org/docs/latest/api/perf_hooks.html#class-recordablehistogram-extends-histogram)


Adds the values from `other` to this histogram.
####  `histogram.record(val)`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramrecordval)
Added in: v15.9.0, v14.18.0
  * `val`


####  `histogram.recordDelta()`[#](https://nodejs.org/docs/latest/api/perf_hooks.html#histogramrecorddelta)
Added in: v15.9.0, v14.18.0
Calculates the amount of time (in nanoseconds) that has passed since the previous call to `recordDelta()` and records that amount in the histogram.
### Examples[#](https://nodejs.org/docs/latest/api/perf_hooks.html#examples)
#### Measuring the duration of async operations[#](https://nodejs.org/docs/latest/api/perf_hooks.html#measuring-the-duration-of-async-operations)
The following example uses the [Async Hooks](https://nodejs.org/docs/latest/api/async_hooks.html) and Performance APIs to measure the actual duration of a Timeout operation (including the amount of time it took to execute the callback).
```
import { createHook } from 'node:async_hooks';
import { performance, PerformanceObserver } from 'node:perf_hooks';

const set = new Set();
const hook = createHook({
  init(id, type) {
    if (type === 'Timeout') {
      performance.mark(`Timeout-${id}-Init`);
      set.add(id);
    }
  },
  destroy(id) {
    if (set.has(id)) {
      set.delete(id);
      performance.mark(`Timeout-${id}-Destroy`);
      performance.measure(`Timeout-${id}`,
                          `Timeout-${id}-Init`,
                          `Timeout-${id}-Destroy`);
    }
  },
});
hook.enable();

const obs = new PerformanceObserver((list, observer) => {
  console.log(list.getEntries()[0]);
  performance.clearMarks();
  performance.clearMeasures();
  observer.disconnect();
});
obs.observe({ entryTypes: ['measure'], buffered: true });

setTimeout(() => {}, 1000);
'use strict';
const async_hooks = require('node:async_hooks');
const {
  performance,
  PerformanceObserver,
} = require('node:perf_hooks');

const set = new Set();
const hook = async_hooks.createHook({
  init(id, type) {
    if (type === 'Timeout') {
      performance.mark(`Timeout-${id}-Init`);
      set.add(id);
    }
  },
  destroy(id) {
    if (set.has(id)) {
      set.delete(id);
      performance.mark(`Timeout-${id}-Destroy`);
      performance.measure(`Timeout-${id}`,
                          `Timeout-${id}-Init`,
                          `Timeout-${id}-Destroy`);
    }
  },
});
hook.enable();

const obs = new PerformanceObserver((list, observer) => {
  console.log(list.getEntries()[0]);
  performance.clearMarks();
  performance.clearMeasures();
  observer.disconnect();
});
obs.observe({ entryTypes: ['measure'] });

setTimeout(() => {}, 1000);
copy
```

#### Measuring how long it takes to load dependencies[#](https://nodejs.org/docs/latest/api/perf_hooks.html#measuring-how-long-it-takes-to-load-dependencies)
The following example measures the duration of `require()` operations to load dependencies:
```
import { performance, PerformanceObserver } from 'node:perf_hooks';

// Activate the observer
const obs = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  entries.forEach((entry) => {
    console.log(`import('${entry[0]}')`, entry.duration);
  });
  performance.clearMarks();
  performance.clearMeasures();
  obs.disconnect();
});
obs.observe({ entryTypes: ['function'], buffered: true });

const timedImport = performance.timerify(async (module) => {
  return await import(module);
});

await timedImport('some-module');
'use strict';
const {
  performance,
  PerformanceObserver,
} = require('node:perf_hooks');
const mod = require('node:module');

// Monkey patch the require function
mod.Module.prototype.require =
  performance.timerify(mod.Module.prototype.require);
require = performance.timerify(require);

// Activate the observer
const obs = new PerformanceObserver((list) => {
  const entries = list.getEntries();
  entries.forEach((entry) => {
    console.log(`require('${entry[0]}')`, entry.duration);
  });
  performance.clearMarks();
  performance.clearMeasures();
  obs.disconnect();
});
obs.observe({ entryTypes: ['function'] });

require('some-module');
copy
```

#### Measuring how long one HTTP round-trip takes[#](https://nodejs.org/docs/latest/api/perf_hooks.html#measuring-how-long-one-http-round-trip-takes)
The following example is used to trace the time spent by HTTP client (`OutgoingMessage`) and HTTP request (`IncomingMessage`). For HTTP client, it means the time interval between starting the request and receiving the response, and for HTTP request, it means the time interval between receiving the request and sending the response:
```
import { PerformanceObserver } from 'node:perf_hooks';
import { createServer, get } from 'node:http';

const obs = new PerformanceObserver((items) => {
  items.getEntries().forEach((item) => {
    console.log(item);
  });
});

obs.observe({ entryTypes: ['http'] });

const PORT = 8080;

createServer((req, res) => {
  res.end('ok');
}).listen(PORT, () => {
  get(`http://127.0.0.1:${PORT}`);
});
'use strict';
const { PerformanceObserver } = require('node:perf_hooks');
const http = require('node:http');

const obs = new PerformanceObserver((items) => {
  items.getEntries().forEach((item) => {
    console.log(item);
  });
});

obs.observe({ entryTypes: ['http'] });

const PORT = 8080;

http.createServer((req, res) => {
  res.end('ok');
}).listen(PORT, () => {
  http.get(`http://127.0.0.1:${PORT}`);
});
copy
```

#### Measuring how long the `net.connect` (only for TCP) takes when the connection is successful[#](https://nodejs.org/docs/latest/api/perf_hooks.html#measuring-how-long-the-netconnect-only-for-tcp-takes-when-the-connection-is-successful)
```
import { PerformanceObserver } from 'node:perf_hooks';
import { connect, createServer } from 'node:net';

const obs = new PerformanceObserver((items) => {
  items.getEntries().forEach((item) => {
    console.log(item);
  });
});
obs.observe({ entryTypes: ['net'] });
const PORT = 8080;
createServer((socket) => {
  socket.destroy();
}).listen(PORT, () => {
  connect(PORT);
});
'use strict';
const { PerformanceObserver } = require('node:perf_hooks');
const net = require('node:net');
const obs = new PerformanceObserver((items) => {
  items.getEntries().forEach((item) => {
    console.log(item);
  });
});
obs.observe({ entryTypes: ['net'] });
const PORT = 8080;
net.createServer((socket) => {
  socket.destroy();
}).listen(PORT, () => {
  net.connect(PORT);
});
copy
```

#### Measuring how long the DNS takes when the request is successful[#](https://nodejs.org/docs/latest/api/perf_hooks.html#measuring-how-long-the-dns-takes-when-the-request-is-successful)
```
import { PerformanceObserver } from 'node:perf_hooks';
import { lookup, promises } from 'node:dns';

const obs = new PerformanceObserver((items) => {
  items.getEntries().forEach((item) => {
    console.log(item);
  });
});
obs.observe({ entryTypes: ['dns'] });
lookup('localhost', () => {});
promises.resolve('localhost');
'use strict';
const { PerformanceObserver } = require('node:perf_hooks');
const dns = require('node:dns');
const obs = new PerformanceObserver((items) => {
  items.getEntries().forEach((item) => {
    console.log(item);
  });
});
obs.observe({ entryTypes: ['dns'] });
dns.lookup('localhost', () => {});
dns.promises.resolve('localhost');
copy
```
