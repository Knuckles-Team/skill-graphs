## Events[#](https://nodejs.org/docs/latest/api/events.html#events)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
Much of the Node.js core API is built around an idiomatic asynchronous event-driven architecture in which certain kinds of objects (called "emitters") emit named events that cause `Function` objects ("listeners") to be called.
For instance: a [`net.Server`](https://nodejs.org/docs/latest/api/net.html#class-netserver) object emits an event each time a peer connects to it; a [`fs.ReadStream`](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream) emits an event when the file is opened; a [stream](https://nodejs.org/docs/latest/api/stream.html) emits an event whenever data is available to be read.
All objects that emit events are instances of the `EventEmitter` class. These objects expose an `eventEmitter.on()` function that allows one or more functions to be attached to named events emitted by the object. Typically, event names are camel-cased strings but any valid JavaScript property key can be used.
When the `EventEmitter` object emits an event, all of the functions attached to that specific event are called _synchronously_. Any values returned by the called listeners are _ignored_ and discarded.
The following example shows a simple `EventEmitter` instance with a single listener. The `eventEmitter.on()` method is used to register listeners, while the `eventEmitter.emit()` method is used to trigger the event.
```
import { EventEmitter } from 'node:events';

class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('event', () => {
  console.log('an event occurred!');
});
myEmitter.emit('event');
const EventEmitter = require('node:events');

class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('event', () => {
  console.log('an event occurred!');
});
myEmitter.emit('event');
copy
```

### Passing arguments and `this` to listeners[#](https://nodejs.org/docs/latest/api/events.html#passing-arguments-and-this-to-listeners)
The `eventEmitter.emit()` method allows an arbitrary set of arguments to be passed to the listener functions. Keep in mind that when an ordinary listener function is called, the standard `this` keyword is intentionally set to reference the `EventEmitter` instance to which the listener is attached.
```
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
myEmitter.on('event', function(a, b) {
  console.log(a, b, this, this === myEmitter);
  // Prints:
  //   a b MyEmitter {
  //     _events: [Object: null prototype] { event: [Function (anonymous)] },
  //     _eventsCount: 1,
  //     _maxListeners: undefined,
  //     Symbol(shapeMode): false,
  //     Symbol(kCapture): false
  //   } true
});
myEmitter.emit('event', 'a', 'b');
const EventEmitter = require('node:events');
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
myEmitter.on('event', function(a, b) {
  console.log(a, b, this, this === myEmitter);
  // Prints:
  //   a b MyEmitter {
  //     _events: [Object: null prototype] { event: [Function (anonymous)] },
  //     _eventsCount: 1,
  //     _maxListeners: undefined,
  //     Symbol(shapeMode): false,
  //     Symbol(kCapture): false
  //   } true
});
myEmitter.emit('event', 'a', 'b');
copy
```

It is possible to use ES6 Arrow Functions as listeners, however, when doing so, the `this` keyword will no longer reference the `EventEmitter` instance:
```
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
myEmitter.on('event', (a, b) => {
  console.log(a, b, this);
  // Prints: a b undefined
});
myEmitter.emit('event', 'a', 'b');
const EventEmitter = require('node:events');
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
myEmitter.on('event', (a, b) => {
  console.log(a, b, this);
  // Prints: a b {}
});
myEmitter.emit('event', 'a', 'b');
copy
```

### Asynchronous vs. synchronous[#](https://nodejs.org/docs/latest/api/events.html#asynchronous-vs-synchronous)
The `EventEmitter` calls all listeners synchronously in the order in which they were registered. This ensures the proper sequencing of events and helps avoid race conditions and logic errors. When appropriate, listener functions can switch to an asynchronous mode of operation using the `setImmediate()` or `process.nextTick()` methods:
```
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
myEmitter.on('event', (a, b) => {
  setImmediate(() => {
    console.log('this happens asynchronously');
  });
});
myEmitter.emit('event', 'a', 'b');
const EventEmitter = require('node:events');
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
myEmitter.on('event', (a, b) => {
  setImmediate(() => {
    console.log('this happens asynchronously');
  });
});
myEmitter.emit('event', 'a', 'b');
copy
```

### Handling events only once[#](https://nodejs.org/docs/latest/api/events.html#handling-events-only-once)
When a listener is registered using the `eventEmitter.on()` method, that listener is invoked _every time_ the named event is emitted.
```
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
let m = 0;
myEmitter.on('event', () => {
  console.log(++m);
});
myEmitter.emit('event');
// Prints: 1
myEmitter.emit('event');
// Prints: 2
const EventEmitter = require('node:events');
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
let m = 0;
myEmitter.on('event', () => {
  console.log(++m);
});
myEmitter.emit('event');
// Prints: 1
myEmitter.emit('event');
// Prints: 2
copy
```

Using the `eventEmitter.once()` method, it is possible to register a listener that is called at most once for a particular event. Once the event is emitted, the listener is unregistered and _then_ called.
```
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
let m = 0;
myEmitter.once('event', () => {
  console.log(++m);
});
myEmitter.emit('event');
// Prints: 1
myEmitter.emit('event');
// Ignored
const EventEmitter = require('node:events');
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
let m = 0;
myEmitter.once('event', () => {
  console.log(++m);
});
myEmitter.emit('event');
// Prints: 1
myEmitter.emit('event');
// Ignored
copy
```

### Error events[#](https://nodejs.org/docs/latest/api/events.html#error-events)
When an error occurs within an `EventEmitter` instance, the typical action is for an `'error'` event to be emitted. These are treated as special cases within Node.js.
If an `EventEmitter` does _not_ have at least one listener registered for the `'error'` event, and an `'error'` event is emitted, the error is thrown, a stack trace is printed, and the Node.js process exits.
```
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
myEmitter.emit('error', new Error('whoops!'));
// Throws and crashes Node.js
const EventEmitter = require('node:events');
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
myEmitter.emit('error', new Error('whoops!'));
// Throws and crashes Node.js
copy
```

To guard against crashing the Node.js process the [`domain`](https://nodejs.org/docs/latest/api/domain.html) module can be used. (Note, however, that the `node:domain` module is deprecated.)
As a best practice, listeners should always be added for the `'error'` events.
```
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
myEmitter.on('error', (err) => {
  console.error('whoops! there was an error');
});
myEmitter.emit('error', new Error('whoops!'));
// Prints: whoops! there was an error
const EventEmitter = require('node:events');
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();
myEmitter.on('error', (err) => {
  console.error('whoops! there was an error');
});
myEmitter.emit('error', new Error('whoops!'));
// Prints: whoops! there was an error
copy
```

It is possible to monitor `'error'` events without consuming the emitted error by installing a listener using the symbol `events.errorMonitor`.
```
import { EventEmitter, errorMonitor } from 'node:events';

const myEmitter = new EventEmitter();
myEmitter.on(errorMonitor, (err) => {
  MyMonitoringTool.log(err);
});
myEmitter.emit('error', new Error('whoops!'));
// Still throws and crashes Node.js
const { EventEmitter, errorMonitor } = require('node:events');

const myEmitter = new EventEmitter();
myEmitter.on(errorMonitor, (err) => {
  MyMonitoringTool.log(err);
});
myEmitter.emit('error', new Error('whoops!'));
// Still throws and crashes Node.js
copy
```

### Capture rejections of promises[#](https://nodejs.org/docs/latest/api/events.html#capture-rejections-of-promises)
Using `async` functions with event handlers is problematic, because it can lead to an unhandled rejection in case of a thrown exception:
```
import { EventEmitter } from 'node:events';
const ee = new EventEmitter();
ee.on('something', async (value) => {
  throw new Error('kaboom');
});
const EventEmitter = require('node:events');
const ee = new EventEmitter();
ee.on('something', async (value) => {
  throw new Error('kaboom');
});
copy
```

The `captureRejections` option in the `EventEmitter` constructor or the global setting change this behavior, installing a `.then(undefined, handler)` handler on the `Promise`. This handler routes the exception asynchronously to the [`Symbol.for('nodejs.rejection')`](https://nodejs.org/docs/latest/api/events.html#emittersymbolfornodejsrejectionerr-eventname-args) method if there is one, or to [`'error'`](https://nodejs.org/docs/latest/api/events.html#error-events) event handler if there is none.
```
import { EventEmitter } from 'node:events';
const ee1 = new EventEmitter({ captureRejections: true });
ee1.on('something', async (value) => {
  throw new Error('kaboom');
});

ee1.on('error', console.log);

const ee2 = new EventEmitter({ captureRejections: true });
ee2.on('something', async (value) => {
  throw new Error('kaboom');
});

ee2[Symbol.for('nodejs.rejection')] = console.log;
const EventEmitter = require('node:events');
const ee1 = new EventEmitter({ captureRejections: true });
ee1.on('something', async (value) => {
  throw new Error('kaboom');
});

ee1.on('error', console.log);

const ee2 = new EventEmitter({ captureRejections: true });
ee2.on('something', async (value) => {
  throw new Error('kaboom');
});

ee2[Symbol.for('nodejs.rejection')] = console.log;
copy
```

Setting `events.captureRejections = true` will change the default for all new instances of `EventEmitter`.
```
import { EventEmitter } from 'node:events';

EventEmitter.captureRejections = true;
const ee1 = new EventEmitter();
ee1.on('something', async (value) => {
  throw new Error('kaboom');
});

ee1.on('error', console.log);
const events = require('node:events');
events.captureRejections = true;
const ee1 = new events.EventEmitter();
ee1.on('something', async (value) => {
  throw new Error('kaboom');
});

ee1.on('error', console.log);
copy
```

The `'error'` events that are generated by the `captureRejections` behavior do not have a catch handler to avoid infinite error loops: the recommendation is to **not use`async` functions as `'error'` event handlers**.
### Class: `EventEmitter`[#](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)
Added in: v0.1.26History Version | Changes
---|---
v13.4.0, v12.16.0 | Added captureRejections option.
The `EventEmitter` class is defined and exposed by the `node:events` module:
```
import { EventEmitter } from 'node:events';
const EventEmitter = require('node:events');
copy
```

All `EventEmitter`s emit the event `'newListener'` when new listeners are added and `'removeListener'` when existing listeners are removed.
It supports the following option:
  * `captureRejections` [automatic capturing of promise rejection](https://nodejs.org/docs/latest/api/events.html#capture-rejections-of-promises). **Default:** `false`.


#### Event: `'newListener'`[#](https://nodejs.org/docs/latest/api/events.html#event-newlistener)
Added in: v0.1.26
  * `eventName`
  * `listener`


The `EventEmitter` instance will emit its own `'newListener'` event _before_ a listener is added to its internal array of listeners.
Listeners registered for the `'newListener'` event are passed the event name and a reference to the listener being added.
The fact that the event is triggered before adding the listener has a subtle but important side effect: any _additional_ listeners registered to the same `name` _within_ the `'newListener'` callback are inserted _before_ the listener that is in the process of being added.
```
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
// Only do this once so we don't loop forever
myEmitter.once('newListener', (event, listener) => {
  if (event === 'event') {
    // Insert a new listener in front
    myEmitter.on('event', () => {
      console.log('B');
    });
  }
});
myEmitter.on('event', () => {
  console.log('A');
});
myEmitter.emit('event');
// Prints:
//   B
//   A
const EventEmitter = require('node:events');
class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
// Only do this once so we don't loop forever
myEmitter.once('newListener', (event, listener) => {
  if (event === 'event') {
    // Insert a new listener in front
    myEmitter.on('event', () => {
      console.log('B');
    });
  }
});
myEmitter.on('event', () => {
  console.log('A');
});
myEmitter.emit('event');
// Prints:
//   B
//   A
copy
```

#### Event: `'removeListener'`[#](https://nodejs.org/docs/latest/api/events.html#event-removelistener)
Added in: v0.9.3History Version | Changes
---|---
v6.1.0, v4.7.0 | For listeners attached using `.once()`, the `listener` argument now yields the original listener function.
  * `eventName`
  * `listener`


The `'removeListener'` event is emitted _after_ the `listener` is removed.
####  `emitter.addListener(eventName, listener)`[#](https://nodejs.org/docs/latest/api/events.html#emitteraddlistenereventname-listener)
Added in: v0.1.26
  * `eventName`
  * `listener`


Alias for `emitter.on(eventName, listener)`.
####  `emitter.emit(eventName[, ...args])`[#](https://nodejs.org/docs/latest/api/events.html#emitteremiteventname-args)
Added in: v0.1.26
  * `eventName`
  * `...args`
  * Returns:


Synchronously calls each of the listeners registered for the event named `eventName`, in the order they were registered, passing the supplied arguments to each.
Returns `true` if the event had listeners, `false` otherwise.
```
import { EventEmitter } from 'node:events';
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

console.log(myEmitter.listeners('event'));

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// [
//   [Function: firstListener],
//   [Function: secondListener],
//   [Function: thirdListener]
// ]
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
const EventEmitter = require('node:events');
const myEmitter = new EventEmitter();

// First listener
myEmitter.on('event', function firstListener() {
  console.log('Helloooo! first listener');
});
// Second listener
myEmitter.on('event', function secondListener(arg1, arg2) {
  console.log(`event with parameters ${arg1}, ${arg2} in second listener`);
});
// Third listener
myEmitter.on('event', function thirdListener(...args) {
  const parameters = args.join(', ');
  console.log(`event with parameters ${parameters} in third listener`);
});

console.log(myEmitter.listeners('event'));

myEmitter.emit('event', 1, 2, 3, 4, 5);

// Prints:
// [
//   [Function: firstListener],
//   [Function: secondListener],
//   [Function: thirdListener]
// ]
// Helloooo! first listener
// event with parameters 1, 2 in second listener
// event with parameters 1, 2, 3, 4, 5 in third listener
copy
```

####  `emitter.eventNames()`[#](https://nodejs.org/docs/latest/api/events.html#emittereventnames)
Added in: v6.0.0
  * Returns:


Returns an array listing the events for which the emitter has registered listeners.
```
import { EventEmitter } from 'node:events';

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
const EventEmitter = require('node:events');

const myEE = new EventEmitter();
myEE.on('foo', () => {});
myEE.on('bar', () => {});

const sym = Symbol('symbol');
myEE.on(sym, () => {});

console.log(myEE.eventNames());
// Prints: [ 'foo', 'bar', Symbol(symbol) ]
copy
```

####  `emitter.getMaxListeners()`[#](https://nodejs.org/docs/latest/api/events.html#emittergetmaxlisteners)
Added in: v1.0.0
  * Returns:


Returns the current max listener value for the `EventEmitter` which is either set by [`emitter.setMaxListeners(n)`](https://nodejs.org/docs/latest/api/events.html#emittersetmaxlistenersn) or defaults to [`events.defaultMaxListeners`](https://nodejs.org/docs/latest/api/events.html#eventsdefaultmaxlisteners).
####  `emitter.listenerCount(eventName[, listener])`[#](https://nodejs.org/docs/latest/api/events.html#emitterlistenercounteventname-listener)
Added in: v3.2.0History Version | Changes
---|---
v19.8.0, v18.16.0 | Added the `listener` argument.
  * `eventName`
  * `listener`
  * Returns:


Returns the number of listeners listening for the event named `eventName`. If `listener` is provided, it will return how many times the listener is found in the list of the listeners of the event.
####  `emitter.listeners(eventName)`[#](https://nodejs.org/docs/latest/api/events.html#emitterlistenerseventname)
Added in: v0.1.26History Version | Changes
---|---
v7.0.0 | For listeners attached using `.once()` this returns the original listeners instead of wrapper functions now.
  * `eventName`
  * Returns:


Returns a copy of the array of listeners for the event named `eventName`.
```
server.on('connection', (stream) => {
  console.log('someone connected!');
});
console.log(util.inspect(server.listeners('connection')));
// Prints: [ [Function] ]
copy
```

####  `emitter.off(eventName, listener)`[#](https://nodejs.org/docs/latest/api/events.html#emitteroffeventname-listener)
Added in: v10.0.0
  * `eventName`
  * `listener`
  * Returns: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


Alias for [`emitter.removeListener()`](https://nodejs.org/docs/latest/api/events.html#emitterremovelistenereventname-listener).
####  `emitter.on(eventName, listener)`[#](https://nodejs.org/docs/latest/api/events.html#emitteroneventname-listener)
Added in: v0.1.101
  * `eventName`
  * `listener`
  * Returns: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


Adds the `listener` function to the end of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName` and `listener` will result in the `listener` being added, and called, multiple times.
```
server.on('connection', (stream) => {
  console.log('someone connected!');
});
copy
```

Returns a reference to the `EventEmitter`, so that calls can be chained.
By default, event listeners are invoked in the order they are added. The `emitter.prependListener()` method can be used as an alternative to add the event listener to the beginning of the listeners array.
```
import { EventEmitter } from 'node:events';
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
const EventEmitter = require('node:events');
const myEE = new EventEmitter();
myEE.on('foo', () => console.log('a'));
myEE.prependListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
copy
```

####  `emitter.once(eventName, listener)`[#](https://nodejs.org/docs/latest/api/events.html#emitteronceeventname-listener)
Added in: v0.3.0
  * `eventName`
  * `listener`
  * Returns: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


Adds a **one-time** `listener` function for the event named `eventName`. The next time `eventName` is triggered, this listener is removed and then invoked.
```
server.once('connection', (stream) => {
  console.log('Ah, we have our first user!');
});
copy
```

Returns a reference to the `EventEmitter`, so that calls can be chained.
By default, event listeners are invoked in the order they are added. The `emitter.prependOnceListener()` method can be used as an alternative to add the event listener to the beginning of the listeners array.
```
import { EventEmitter } from 'node:events';
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
const EventEmitter = require('node:events');
const myEE = new EventEmitter();
myEE.once('foo', () => console.log('a'));
myEE.prependOnceListener('foo', () => console.log('b'));
myEE.emit('foo');
// Prints:
//   b
//   a
copy
```

####  `emitter.prependListener(eventName, listener)`[#](https://nodejs.org/docs/latest/api/events.html#emitterprependlistenereventname-listener)
Added in: v6.0.0
  * `eventName`
  * `listener`
  * Returns: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


Adds the `listener` function to the _beginning_ of the listeners array for the event named `eventName`. No checks are made to see if the `listener` has already been added. Multiple calls passing the same combination of `eventName` and `listener` will result in the `listener` being added, and called, multiple times.
```
server.prependListener('connection', (stream) => {
  console.log('someone connected!');
});
copy
```

Returns a reference to the `EventEmitter`, so that calls can be chained.
####  `emitter.prependOnceListener(eventName, listener)`[#](https://nodejs.org/docs/latest/api/events.html#emitterprependoncelistenereventname-listener)
Added in: v6.0.0
  * `eventName`
  * `listener`
  * Returns: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


Adds a **one-time** `listener` function for the event named `eventName` to the _beginning_ of the listeners array. The next time `eventName` is triggered, this listener is removed, and then invoked.
```
server.prependOnceListener('connection', (stream) => {
  console.log('Ah, we have our first user!');
});
copy
```

Returns a reference to the `EventEmitter`, so that calls can be chained.
####  `emitter.removeAllListeners([eventName])`[#](https://nodejs.org/docs/latest/api/events.html#emitterremovealllistenerseventname)
Added in: v0.1.26
  * `eventName`
  * Returns: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


Removes all listeners, or those of the specified `eventName`.
It is bad practice to remove listeners added elsewhere in the code, particularly when the `EventEmitter` instance was created by some other component or module (e.g. sockets or file streams).
Returns a reference to the `EventEmitter`, so that calls can be chained.
####  `emitter.removeListener(eventName, listener)`[#](https://nodejs.org/docs/latest/api/events.html#emitterremovelistenereventname-listener)
Added in: v0.1.26
  * `eventName`
  * `listener`
  * Returns: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


Removes the specified `listener` from the listener array for the event named `eventName`.
```
const callback = (stream) => {
  console.log('someone connected!');
};
server.on('connection', callback);
// ...
server.removeListener('connection', callback);
copy
```

`removeListener()` will remove, at most, one instance of a listener from the listener array. If any single listener has been added multiple times to the listener array for the specified `eventName`, then `removeListener()` must be called multiple times to remove each instance.
Once an event is emitted, all listeners attached to it at the time of emitting are called in order. This implies that any `removeListener()` or `removeAllListeners()` calls _after_ emitting and _before_ the last listener finishes execution will not remove them from `emit()` in progress. Subsequent events behave as expected.
```
import { EventEmitter } from 'node:events';
class MyEmitter extends EventEmitter {}
const myEmitter = new MyEmitter();

const callbackA = () => {
  console.log('A');
  myEmitter.removeListener('event', callbackB);
};

const callbackB = () => {
  console.log('B');
};
