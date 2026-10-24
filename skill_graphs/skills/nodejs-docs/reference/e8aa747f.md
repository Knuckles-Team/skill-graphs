
myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
const EventEmitter = require('node:events');
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};

myEmitter.on('event', callbackA);

myEmitter.on('event', callbackB);

// callbackA removes listener callbackB but it will still be called.
// Internal listener array at time of emit [callbackA, callbackB]
myEmitter.emit('event');
// Prints:
//   A
//   B

// callbackB is now removed.
// Internal listener array [callbackA]
myEmitter.emit('event');
// Prints:
//   A
copy
```

Because listeners are managed using an internal array, calling this will change the position indexes of any listener registered _after_ the listener being removed. This will not impact the order in which listeners are called, but it means that any copies of the listener array as returned by the `emitter.listeners()` method will need to be recreated.
When a single function has been added as a handler multiple times for a single event (as in the example below), `removeListener()` will remove the most recently added instance. In the example the `once('ping')` listener is removed:
```
import { EventEmitter } from 'node:events';
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
const EventEmitter = require('node:events');
const ee = new EventEmitter();

function pong() {
  console.log('pong');
}

ee.on('ping', pong);
ee.once('ping', pong);
ee.removeListener('ping', pong);

ee.emit('ping');
ee.emit('ping');
copy
```

Returns a reference to the `EventEmitter`, so that calls can be chained.
####  `emitter.setMaxListeners(n)`[#](https://nodejs.org/docs/latest/api/events.html#emittersetmaxlistenersn)
Added in: v0.3.5
  * `n`
  * Returns: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


By default `EventEmitter`s will print a warning if more than `10` listeners are added for a particular event. This is a useful default that helps finding memory leaks. The `emitter.setMaxListeners()` method allows the limit to be modified for this specific `EventEmitter` instance. The value can be set to `Infinity` (or `0`) to indicate an unlimited number of listeners.
Returns a reference to the `EventEmitter`, so that calls can be chained.
####  `emitter.rawListeners(eventName)`[#](https://nodejs.org/docs/latest/api/events.html#emitterrawlistenerseventname)
Added in: v9.4.0
  * `eventName`
  * Returns:


Returns a copy of the array of listeners for the event named `eventName`, including any wrappers (such as those created by `.once()`).
```
import { EventEmitter } from 'node:events';
const emitter = new EventEmitter();
emitter.once('log', () => console.log('log once'));

// Returns a new Array with a function `onceWrapper` which has a property
// `listener` which contains the original listener bound above
const listeners = emitter.rawListeners('log');
const logFnWrapper = listeners[0];

// Logs "log once" to the console and does not unbind the `once` event
logFnWrapper.listener();

// Logs "log once" to the console and removes the listener
logFnWrapper();

emitter.on('log', () => console.log('log persistently'));
// Will return a new Array with a single function bound by `.on()` above
const newListeners = emitter.rawListeners('log');

// Logs "log persistently" twice
newListeners[0]();
emitter.emit('log');
const EventEmitter = require('node:events');
const emitter = new EventEmitter();
emitter.once('log', () => console.log('log once'));

// Returns a new Array with a function `onceWrapper` which has a property
// `listener` which contains the original listener bound above
const listeners = emitter.rawListeners('log');
const logFnWrapper = listeners[0];

// Logs "log once" to the console and does not unbind the `once` event
logFnWrapper.listener();

// Logs "log once" to the console and removes the listener
logFnWrapper();

emitter.on('log', () => console.log('log persistently'));
// Will return a new Array with a single function bound by `.on()` above
const newListeners = emitter.rawListeners('log');

// Logs "log persistently" twice
newListeners[0]();
emitter.emit('log');
copy
```

####  `emitter[Symbol.for('nodejs.rejection')](err, eventName[, ...args])`[#](https://nodejs.org/docs/latest/api/events.html#emittersymbolfornodejsrejectionerr-eventname-args)
Added in: v13.4.0, v12.16.0History Version | Changes
---|---
v17.4.0, v16.14.0 | No longer experimental.
  * `err`
  * `eventName`
  * `...args`


The `Symbol.for('nodejs.rejection')` method is called in case a promise rejection happens when emitting an event and [`captureRejections`](https://nodejs.org/docs/latest/api/events.html#capture-rejections-of-promises) is enabled on the emitter. It is possible to use [`events.captureRejectionSymbol`](https://nodejs.org/docs/latest/api/events.html#eventscapturerejectionsymbol) in place of `Symbol.for('nodejs.rejection')`.
```
import { EventEmitter, captureRejectionSymbol } from 'node:events';

class MyClass extends EventEmitter {
  constructor() {
    super({ captureRejections: true });
  }

  [captureRejectionSymbol](err, event, ...args) {
    console.log('rejection happened for', event, 'with', err, ...args);
    this.destroy(err);
  }

  destroy(err) {
    // Tear the resource down here.
  }
}
const { EventEmitter, captureRejectionSymbol } = require('node:events');

class MyClass extends EventEmitter {
  constructor() {
    super({ captureRejections: true });
  }

  [captureRejectionSymbol](err, event, ...args) {
    console.log('rejection happened for', event, 'with', err, ...args);
    this.destroy(err);
  }

  destroy(err) {
    // Tear the resource down here.
  }
}
copy
```

###  `events.defaultMaxListeners`[#](https://nodejs.org/docs/latest/api/events.html#eventsdefaultmaxlisteners)
Added in: v0.11.2
By default, a maximum of `10` listeners can be registered for any single event. This limit can be changed for individual `EventEmitter` instances using the [`emitter.setMaxListeners(n)`](https://nodejs.org/docs/latest/api/events.html#emittersetmaxlistenersn) method. To change the default for _all_ `EventEmitter` instances, the `events.defaultMaxListeners` property can be used. If this value is not a positive number, a `RangeError` is thrown.
Take caution when setting the `events.defaultMaxListeners` because the change affects _all_ `EventEmitter` instances, including those created before the change is made. However, calling [`emitter.setMaxListeners(n)`](https://nodejs.org/docs/latest/api/events.html#emittersetmaxlistenersn) still has precedence over `events.defaultMaxListeners`.
This is not a hard limit. The `EventEmitter` instance will allow more listeners to be added but will output a trace warning to stderr indicating that a "possible EventEmitter memory leak" has been detected. For any single `EventEmitter`, the `emitter.getMaxListeners()` and `emitter.setMaxListeners()` methods can be used to temporarily avoid this warning:
`defaultMaxListeners` has no effect on `AbortSignal` instances. While it is still possible to use [`emitter.setMaxListeners(n)`](https://nodejs.org/docs/latest/api/events.html#emittersetmaxlistenersn) to set a warning limit for individual `AbortSignal` instances, per default `AbortSignal` instances will not warn.
```
import { EventEmitter } from 'node:events';
const emitter = new EventEmitter();
emitter.setMaxListeners(emitter.getMaxListeners() + 1);
emitter.once('event', () => {
  // do stuff
  emitter.setMaxListeners(Math.max(emitter.getMaxListeners() - 1, 0));
});
const EventEmitter = require('node:events');
const emitter = new EventEmitter();
emitter.setMaxListeners(emitter.getMaxListeners() + 1);
emitter.once('event', () => {
  // do stuff
  emitter.setMaxListeners(Math.max(emitter.getMaxListeners() - 1, 0));
});
copy
```

The [`--trace-warnings`](https://nodejs.org/docs/latest/api/cli.html#--trace-warnings) command-line flag can be used to display the stack trace for such warnings.
The emitted warning can be inspected with [`process.on('warning')`](https://nodejs.org/docs/latest/api/process.html#event-warning) and will have the additional `emitter`, `type`, and `count` properties, referring to the event emitter instance, the event's name and the number of attached listeners, respectively. Its `name` property is set to `'MaxListenersExceededWarning'`.
###  `events.errorMonitor`[#](https://nodejs.org/docs/latest/api/events.html#eventserrormonitor)
Added in: v13.6.0, v12.17.0
This symbol shall be used to install a listener for only monitoring `'error'` events. Listeners installed using this symbol are called before the regular `'error'` listeners are called.
Installing a listener using this symbol does not change the behavior once an `'error'` event is emitted. Therefore, the process will still crash if no regular `'error'` listener is installed.
###  `events.getEventListeners(emitterOrTarget, eventName)`[#](https://nodejs.org/docs/latest/api/events.html#eventsgeteventlistenersemitterortarget-eventname)
Added in: v15.2.0, v14.17.0
  * `emitterOrTarget` [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) | [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget)
  * `eventName`
  * Returns:


Returns a copy of the array of listeners for the event named `eventName`.
For `EventEmitter`s this behaves exactly the same as calling `.listeners` on the emitter.
For `EventTarget`s this is the only way to get the event listeners for the event target. This is useful for debugging and diagnostic purposes.
```
import { getEventListeners, EventEmitter } from 'node:events';

{
  const ee = new EventEmitter();
  const listener = () => console.log('Events are fun');
  ee.on('foo', listener);
  console.log(getEventListeners(ee, 'foo')); // [ [Function: listener] ]
}
{
  const et = new EventTarget();
  const listener = () => console.log('Events are fun');
  et.addEventListener('foo', listener);
  console.log(getEventListeners(et, 'foo')); // [ [Function: listener] ]
}
const { getEventListeners, EventEmitter } = require('node:events');

{
  const ee = new EventEmitter();
  const listener = () => console.log('Events are fun');
  ee.on('foo', listener);
  console.log(getEventListeners(ee, 'foo')); // [ [Function: listener] ]
}
{
  const et = new EventTarget();
  const listener = () => console.log('Events are fun');
  et.addEventListener('foo', listener);
  console.log(getEventListeners(et, 'foo')); // [ [Function: listener] ]
}
copy
```

###  `events.getMaxListeners(emitterOrTarget)`[#](https://nodejs.org/docs/latest/api/events.html#eventsgetmaxlistenersemitterortarget)
Added in: v19.9.0, v18.17.0
  * `emitterOrTarget` [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) | [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget)
  * Returns:


Returns the currently set max amount of listeners.
For `EventEmitter`s this behaves exactly the same as calling `.getMaxListeners` on the emitter.
For `EventTarget`s this is the only way to get the max event listeners for the event target. If the number of event handlers on a single EventTarget exceeds the max set, the EventTarget will print a warning.
```
import { getMaxListeners, setMaxListeners, EventEmitter } from 'node:events';

{
  const ee = new EventEmitter();
  console.log(getMaxListeners(ee)); // 10
  setMaxListeners(11, ee);
  console.log(getMaxListeners(ee)); // 11
}
{
  const et = new EventTarget();
  console.log(getMaxListeners(et)); // 10
  setMaxListeners(11, et);
  console.log(getMaxListeners(et)); // 11
}
const { getMaxListeners, setMaxListeners, EventEmitter } = require('node:events');

{
  const ee = new EventEmitter();
  console.log(getMaxListeners(ee)); // 10
  setMaxListeners(11, ee);
  console.log(getMaxListeners(ee)); // 11
}
{
  const et = new EventTarget();
  console.log(getMaxListeners(et)); // 10
  setMaxListeners(11, et);
  console.log(getMaxListeners(et)); // 11
}
copy
```

###  `events.once(emitter, name[, options])`[#](https://nodejs.org/docs/latest/api/events.html#eventsonceemitter-name-options)
Added in: v11.13.0, v10.16.0History Version | Changes
---|---
v15.0.0 | The `signal` option is supported now.
  * `emitter` [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)
  * `name`
  * `options`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) Can be used to cancel waiting for the event.
  * Returns:


Creates a `Promise` that is fulfilled when the `EventEmitter` emits the given event or that is rejected if the `EventEmitter` emits `'error'` while waiting. The `Promise` will resolve with an array of all the arguments emitted to the given event.
This method is intentionally generic and works with the web platform `'error'` event semantics and does not listen to the `'error'` event.
```
import { once, EventEmitter } from 'node:events';
import process from 'node:process';

const ee = new EventEmitter();

process.nextTick(() => {
  ee.emit('myevent', 42);
});

const [value] = await once(ee, 'myevent');
console.log(value);

const err = new Error('kaboom');
process.nextTick(() => {
  ee.emit('error', err);
});

try {
  await once(ee, 'myevent');
} catch (err) {
  console.error('error happened', err);
}
const { once, EventEmitter } = require('node:events');

async function run() {
  const ee = new EventEmitter();

  process.nextTick(() => {
    ee.emit('myevent', 42);
  });

  const [value] = await once(ee, 'myevent');
  console.log(value);

  const err = new Error('kaboom');
  process.nextTick(() => {
    ee.emit('error', err);
  });

  try {
    await once(ee, 'myevent');
  } catch (err) {
    console.error('error happened', err);
  }
}

run();
copy
```

The special handling of the `'error'` event is only used when `events.once()` is used to wait for another event. If `events.once()` is used to wait for the '`error'` event itself, then it is treated as any other kind of event without special handling:
```
import { EventEmitter, once } from 'node:events';

const ee = new EventEmitter();

once(ee, 'error')
  .then(([err]) => console.log('ok', err.message))
  .catch((err) => console.error('error', err.message));

ee.emit('error', new Error('boom'));

// Prints: ok boom
const { EventEmitter, once } = require('node:events');

const ee = new EventEmitter();

once(ee, 'error')
  .then(([err]) => console.log('ok', err.message))
  .catch((err) => console.error('error', err.message));

ee.emit('error', new Error('boom'));

// Prints: ok boom
copy
```

An [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) can be used to cancel waiting for the event:
```
import { EventEmitter, once } from 'node:events';

const ee = new EventEmitter();
const ac = new AbortController();

async function foo(emitter, event, signal) {
  try {
    await once(emitter, event, { signal });
    console.log('event emitted!');
  } catch (error) {
    if (error.name === 'AbortError') {
      console.error('Waiting for the event was canceled!');
    } else {
      console.error('There was an error', error.message);
    }
  }
}

foo(ee, 'foo', ac.signal);
ac.abort(); // Prints: Waiting for the event was canceled!
const { EventEmitter, once } = require('node:events');

const ee = new EventEmitter();
const ac = new AbortController();

async function foo(emitter, event, signal) {
  try {
    await once(emitter, event, { signal });
    console.log('event emitted!');
  } catch (error) {
    if (error.name === 'AbortError') {
      console.error('Waiting for the event was canceled!');
    } else {
      console.error('There was an error', error.message);
    }
  }
}

foo(ee, 'foo', ac.signal);
ac.abort(); // Prints: Waiting for the event was canceled!
copy
```

#### Caveats when awaiting multiple events[#](https://nodejs.org/docs/latest/api/events.html#caveats-when-awaiting-multiple-events)
It is important to be aware of execution order when using the `events.once()` method to await multiple events.
Conventional event listeners are called synchronously when the event is emitted. This guarantees that execution will not proceed beyond the emitted event until all listeners have finished executing.
The same is _not_ true when awaiting Promises returned by `events.once()`. Promise tasks are not handled until after the current execution stack runs to completion, which means that multiple events could be emitted before asynchronous execution continues from the relevant `await` statement.
As a result, events can be "missed" if a series of `await events.once()` statements is used to listen to multiple events, since there might be times where more than one event is emitted during the same phase of the event loop. (The same is true when using `process.nextTick()` to emit events, because the tasks queued by `process.nextTick()` are executed before Promise tasks.)
```
import { EventEmitter, once } from 'node:events';
import process from 'node:process';

const myEE = new EventEmitter();

async function listen() {
  await once(myEE, 'foo');
  console.log('foo');

  // This Promise will never resolve, because the 'bar' event will
  // have already been emitted before the next line is executed.
  await once(myEE, 'bar');
  console.log('bar');
}

process.nextTick(() => {
  myEE.emit('foo');
  myEE.emit('bar');
});

listen().then(() => console.log('done'));
const { EventEmitter, once } = require('node:events');

const myEE = new EventEmitter();

async function listen() {
  await once(myEE, 'foo');
  console.log('foo');

  // This Promise will never resolve, because the 'bar' event will
  // have already been emitted before the next line is executed.
  await once(myEE, 'bar');
  console.log('bar');
}

process.nextTick(() => {
  myEE.emit('foo');
  myEE.emit('bar');
});

listen().then(() => console.log('done'));
copy
```

To catch multiple events, create all of the Promises _before_ awaiting any of them. This is usually made easier by using `Promise.all()`, `Promise.race()`, or `Promise.allSettled()`:
```
import { EventEmitter, once } from 'node:events';
import process from 'node:process';

const myEE = new EventEmitter();

async function listen() {
  await Promise.all([
    once(myEE, 'foo'),
    once(myEE, 'bar'),
  ]);
  console.log('foo', 'bar');
}

process.nextTick(() => {
  myEE.emit('foo');
  myEE.emit('bar');
});

listen().then(() => console.log('done'));
const { EventEmitter, once } = require('node:events');

const myEE = new EventEmitter();

async function listen() {
  await Promise.all([
    once(myEE, 'bar'),
    once(myEE, 'foo'),
  ]);
  console.log('foo', 'bar');
}

process.nextTick(() => {
  myEE.emit('foo');
  myEE.emit('bar');
});

listen().then(() => console.log('done'));
copy
```

###  `events.captureRejections`[#](https://nodejs.org/docs/latest/api/events.html#eventscapturerejections)
Added in: v13.4.0, v12.16.0History Version | Changes
---|---
v17.4.0, v16.14.0 | No longer experimental.
  * Type:


Change the default `captureRejections` option on all new `EventEmitter` objects.
###  `events.captureRejectionSymbol`[#](https://nodejs.org/docs/latest/api/events.html#eventscapturerejectionsymbol)
Added in: v13.4.0, v12.16.0History Version | Changes
---|---
v17.4.0, v16.14.0 | No longer experimental.
  * Type: `Symbol.for('nodejs.rejection')`


See how to write a custom [rejection handler](https://nodejs.org/docs/latest/api/events.html#emittersymbolfornodejsrejectionerr-eventname-args).
###  `events.listenerCount(emitterOrTarget, eventName)`[#](https://nodejs.org/docs/latest/api/events.html#eventslistenercountemitterortarget-eventname)
Added in: v0.9.12History Version | Changes
---|---
v25.4.0 | Now accepts EventTarget arguments.
v25.4.0 | Deprecation revoked.
v3.2.0 | Documentation-only deprecation.
  * `emitterOrTarget` [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) | [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget)
  * `eventName`
  * Returns:


Returns the number of registered listeners for the event named `eventName`.
For `EventEmitter`s this behaves exactly the same as calling `.listenerCount` on the emitter.
For `EventTarget`s this is the only way to obtain the listener count. This can be useful for debugging and diagnostic purposes.
```
import { EventEmitter, listenerCount } from 'node:events';

{
  const ee = new EventEmitter();
  ee.on('event', () => {});
  ee.on('event', () => {});
  console.log(listenerCount(ee, 'event')); // 2
}
{
  const et = new EventTarget();
  et.addEventListener('event', () => {});
  et.addEventListener('event', () => {});
  console.log(listenerCount(et, 'event')); // 2
}
const { EventEmitter, listenerCount } = require('node:events');

{
  const ee = new EventEmitter();
  ee.on('event', () => {});
  ee.on('event', () => {});
  console.log(listenerCount(ee, 'event')); // 2
}
{
  const et = new EventTarget();
  et.addEventListener('event', () => {});
  et.addEventListener('event', () => {});
  console.log(listenerCount(et, 'event')); // 2
}
copy
```

###  `events.on(emitter, eventName[, options])`[#](https://nodejs.org/docs/latest/api/events.html#eventsonemitter-eventname-options)
Added in: v13.6.0, v12.16.0History Version | Changes
---|---
v22.0.0, v20.13.0 | Support `highWaterMark` and `lowWaterMark` options, For consistency. Old options are still supported.
v20.0.0 | The `close`, `highWatermark`, and `lowWatermark` options are supported now.
  * `emitter` [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)
  * `eventName`
  * `options`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) Can be used to cancel awaiting events.
    * `close`
    * `highWaterMark` **Default:** `Number.MAX_SAFE_INTEGER` The high watermark. The emitter is paused every time the size of events being buffered is higher than it. Supported only on emitters implementing `pause()` and `resume()` methods.
    * `lowWaterMark` **Default:** `1` The low watermark. The emitter is resumed every time the size of events being buffered is lower than it. Supported only on emitters implementing `pause()` and `resume()` methods.
  * Returns: `eventName` events emitted by the `emitter`

```
import { on, EventEmitter } from 'node:events';
import process from 'node:process';

const ee = new EventEmitter();

// Emit later on
process.nextTick(() => {
  ee.emit('foo', 'bar');
  ee.emit('foo', 42);
});

for await (const event of on(ee, 'foo')) {
  // The execution of this inner block is synchronous and it
  // processes one event at a time (even with await). Do not use
  // if concurrent execution is required.
  console.log(event); // prints ['bar'] [42]
}
// Unreachable here
const { on, EventEmitter } = require('node:events');

(async () => {
  const ee = new EventEmitter();

  // Emit later on
  process.nextTick(() => {
    ee.emit('foo', 'bar');
    ee.emit('foo', 42);
  });

  for await (const event of on(ee, 'foo')) {
    // The execution of this inner block is synchronous and it
    // processes one event at a time (even with await). Do not use
    // if concurrent execution is required.
    console.log(event); // prints ['bar'] [42]
  }
  // Unreachable here
})();
copy
```

Returns an `AsyncIterator` that iterates `eventName` events. It will throw if the `EventEmitter` emits `'error'`. It removes all listeners when exiting the loop. The `value` returned by each iteration is an array composed of the emitted event arguments.
An [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) can be used to cancel waiting on events:
```
import { on, EventEmitter } from 'node:events';
import process from 'node:process';

const ac = new AbortController();

(async () => {
  const ee = new EventEmitter();

  // Emit later on
  process.nextTick(() => {
    ee.emit('foo', 'bar');
    ee.emit('foo', 42);
  });

  for await (const event of on(ee, 'foo', { signal: ac.signal })) {
    // The execution of this inner block is synchronous and it
    // processes one event at a time (even with await). Do not use
    // if concurrent execution is required.
    console.log(event); // prints ['bar'] [42]
  }
  // Unreachable here
})();

process.nextTick(() => ac.abort());
const { on, EventEmitter } = require('node:events');

const ac = new AbortController();

(async () => {
  const ee = new EventEmitter();

  // Emit later on
  process.nextTick(() => {
    ee.emit('foo', 'bar');
    ee.emit('foo', 42);
  });

  for await (const event of on(ee, 'foo', { signal: ac.signal })) {
    // The execution of this inner block is synchronous and it
    // processes one event at a time (even with await). Do not use
    // if concurrent execution is required.
    console.log(event); // prints ['bar'] [42]
  }
  // Unreachable here
})();

process.nextTick(() => ac.abort());
copy
```

###  `events.setMaxListeners(n[, ...eventTargets])`[#](https://nodejs.org/docs/latest/api/events.html#eventssetmaxlistenersn-eventtargets)
