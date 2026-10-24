Added in: v15.4.0
  * `n` `EventTarget` event.
  * `...eventsTargets` [`<EventTarget[]>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) | [`<EventEmitter[]>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) Zero or more [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) or [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) instances. If none are specified, `n` is set as the default max for all newly created [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) and [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) objects.

```
import { setMaxListeners, EventEmitter } from 'node:events';

const target = new EventTarget();
const emitter = new EventEmitter();

setMaxListeners(5, target, emitter);
const {
  setMaxListeners,
  EventEmitter,
} = require('node:events');

const target = new EventTarget();
const emitter = new EventEmitter();

setMaxListeners(5, target, emitter);
copy
```

###  `events.addAbortListener(signal, listener)`[#](https://nodejs.org/docs/latest/api/events.html#eventsaddabortlistenersignal-listener)
Added in: v20.5.0, v18.18.0History Version | Changes
---|---
v24.0.0, v22.16.0 | Change stability index for this feature from Experimental to Stable.
  * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal)
  * `listener` [`<EventListener>`](https://nodejs.org/docs/latest/api/events.html#event-listener)
  * Returns: `abort` listener.


Listens once to the `abort` event on the provided `signal`.
Listening to the `abort` event on abort signals is unsafe and may lead to resource leaks since another third party with the signal can call [`e.stopImmediatePropagation()`](https://nodejs.org/docs/latest/api/events.html#eventstopimmediatepropagation). Unfortunately Node.js cannot change this since it would violate the web standard. Additionally, the original API makes it easy to forget to remove listeners.
This API allows safely using `AbortSignal`s in Node.js APIs by solving these two issues by listening to the event such that `stopImmediatePropagation` does not prevent the listener from running.
Returns a disposable so that it may be unsubscribed from more easily.
```
const { addAbortListener } = require('node:events');

function example(signal) {
  signal.addEventListener('abort', (e) => e.stopImmediatePropagation());
  // addAbortListener() returns a disposable, so the `using` keyword ensures
  // the abort listener is automatically removed when this scope exits.
  using _ = addAbortListener(signal, (e) => {
    // Do something when signal is aborted.
  });
}
import { addAbortListener } from 'node:events';

function example(signal) {
  signal.addEventListener('abort', (e) => e.stopImmediatePropagation());
  // addAbortListener() returns a disposable, so the `using` keyword ensures
  // the abort listener is automatically removed when this scope exits.
  using _ = addAbortListener(signal, (e) => {
    // Do something when signal is aborted.
  });
}
copy
```

### Class: `events.EventEmitterAsyncResource extends EventEmitter`[#](https://nodejs.org/docs/latest/api/events.html#class-eventseventemitterasyncresource-extends-eventemitter)
Added in: v17.4.0, v16.14.0
Integrates `EventEmitter` with [`<AsyncResource>`](https://nodejs.org/docs/latest/api/async_hooks.html#class-asyncresource) for `EventEmitter`s that require manual async tracking. Specifically, all events emitted by instances of `events.EventEmitterAsyncResource` will run within its [async context](https://nodejs.org/docs/latest/api/async_context.html).
```
import { EventEmitterAsyncResource, EventEmitter } from 'node:events';
import { notStrictEqual, strictEqual } from 'node:assert';
import { executionAsyncId, triggerAsyncId } from 'node:async_hooks';

// Async tracking tooling will identify this as 'Q'.
const ee1 = new EventEmitterAsyncResource({ name: 'Q' });

// 'foo' listeners will run in the EventEmitters async context.
ee1.on('foo', () => {
  strictEqual(executionAsyncId(), ee1.asyncId);
  strictEqual(triggerAsyncId(), ee1.triggerAsyncId);
});

const ee2 = new EventEmitter();

// 'foo' listeners on ordinary EventEmitters that do not track async
// context, however, run in the same async context as the emit().
ee2.on('foo', () => {
  notStrictEqual(executionAsyncId(), ee2.asyncId);
  notStrictEqual(triggerAsyncId(), ee2.triggerAsyncId);
});

Promise.resolve().then(() => {
  ee1.emit('foo');
  ee2.emit('foo');
});
const { EventEmitterAsyncResource, EventEmitter } = require('node:events');
const { notStrictEqual, strictEqual } = require('node:assert');
const { executionAsyncId, triggerAsyncId } = require('node:async_hooks');

// Async tracking tooling will identify this as 'Q'.
const ee1 = new EventEmitterAsyncResource({ name: 'Q' });

// 'foo' listeners will run in the EventEmitters async context.
ee1.on('foo', () => {
  strictEqual(executionAsyncId(), ee1.asyncId);
  strictEqual(triggerAsyncId(), ee1.triggerAsyncId);
});

const ee2 = new EventEmitter();

// 'foo' listeners on ordinary EventEmitters that do not track async
// context, however, run in the same async context as the emit().
ee2.on('foo', () => {
  notStrictEqual(executionAsyncId(), ee2.asyncId);
  notStrictEqual(triggerAsyncId(), ee2.triggerAsyncId);
});

Promise.resolve().then(() => {
  ee1.emit('foo');
  ee2.emit('foo');
});
copy
```

The `EventEmitterAsyncResource` class has the same methods and takes the same options as `EventEmitter` and `AsyncResource` themselves.
####  `new events.EventEmitterAsyncResource([options])`[#](https://nodejs.org/docs/latest/api/events.html#new-eventseventemitterasyncresourceoptions)
  * `options`
    * `captureRejections` [automatic capturing of promise rejection](https://nodejs.org/docs/latest/api/events.html#capture-rejections-of-promises). **Default:** `false`.
    * `name` **Default:**
    * `triggerAsyncId` **Default:** `executionAsyncId()`.
    * `requireManualDestroy` `true`, disables `emitDestroy` when the object is garbage collected. This usually does not need to be set (even if `emitDestroy` is called manually), unless the resource's `asyncId` is retrieved and the sensitive API's `emitDestroy` is called with it. When set to `false`, the `emitDestroy` call on garbage collection will only take place if there is at least one active `destroy` hook. **Default:** `false`.


####  `eventemitterasyncresource.asyncId`[#](https://nodejs.org/docs/latest/api/events.html#eventemitterasyncresourceasyncid)
  * Type: `asyncId` assigned to the resource.


####  `eventemitterasyncresource.asyncResource`[#](https://nodejs.org/docs/latest/api/events.html#eventemitterasyncresourceasyncresource)
  * Type: [`<AsyncResource>`](https://nodejs.org/docs/latest/api/async_hooks.html#class-asyncresource) The underlying [`<AsyncResource>`](https://nodejs.org/docs/latest/api/async_hooks.html#class-asyncresource).


The returned `AsyncResource` object has an additional `eventEmitter` property that provides a reference to this `EventEmitterAsyncResource`.
####  `eventemitterasyncresource.emitDestroy()`[#](https://nodejs.org/docs/latest/api/events.html#eventemitterasyncresourceemitdestroy)
Call all `destroy` hooks. This should only ever be called once. An error will be thrown if it is called more than once. This **must** be manually called. If the resource is left to be collected by the GC then the `destroy` hooks will never be called.
####  `eventemitterasyncresource.triggerAsyncId`[#](https://nodejs.org/docs/latest/api/events.html#eventemitterasyncresourcetriggerasyncid)
  * Type: `triggerAsyncId` that is passed to the `AsyncResource` constructor.


###  `EventTarget` and `Event` API[#](https://nodejs.org/docs/latest/api/events.html#eventtarget-and-event-api)
Added in: v14.5.0History Version | Changes
---|---
v16.0.0 | changed EventTarget error handling.
v15.4.0 | No longer experimental.
v15.0.0 | The `EventTarget` and `Event` classes are now available as globals.
The `EventTarget` and `Event` objects are a Node.js-specific implementation of the
```
const target = new EventTarget();

target.addEventListener('foo', (event) => {
  console.log('foo event happened!');
});
copy
```

#### Node.js `EventTarget` vs. DOM `EventTarget`[#](https://nodejs.org/docs/latest/api/events.html#nodejs-eventtarget-vs-dom-eventtarget)
There are two key differences between the Node.js `EventTarget` and the
  1. Whereas DOM `EventTarget` instances _may_ be hierarchical, there is no concept of hierarchy and event propagation in Node.js. That is, an event dispatched to an `EventTarget` does not propagate through a hierarchy of nested target objects that may each have their own set of handlers for the event.
  2. In the Node.js `EventTarget`, if an event listener is an async function or returns a `Promise`, and the returned `Promise` rejects, the rejection is automatically captured and handled the same way as a listener that throws synchronously (see [`EventTarget` error handling](https://nodejs.org/docs/latest/api/events.html#eventtarget-error-handling) for details).


####  `NodeEventTarget` vs. `EventEmitter`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtarget-vs-eventemitter)
The `NodeEventTarget` object implements a modified subset of the `EventEmitter` API that allows it to closely _emulate_ an `EventEmitter` in certain situations. A `NodeEventTarget` is _not_ an instance of `EventEmitter` and cannot be used in place of an `EventEmitter` in most cases.
  1. Unlike `EventEmitter`, any given `listener` can be registered at most once per event `type`. Attempts to register a `listener` multiple times are ignored.
  2. The `NodeEventTarget` does not emulate the full `EventEmitter` API. Specifically the `prependListener()`, `prependOnceListener()`, `rawListeners()`, and `errorMonitor` APIs are not emulated. The `'newListener'` and `'removeListener'` events will also not be emitted.
  3. The `NodeEventTarget` does not implement any special default behavior for events with type `'error'`.
  4. The `NodeEventTarget` supports `EventListener` objects as well as functions as handlers for all event types.


#### Event listener[#](https://nodejs.org/docs/latest/api/events.html#event-listener)
Event listeners registered for an event `type` may either be JavaScript functions or objects with a `handleEvent` property whose value is a function.
In either case, the handler function is invoked with the `event` argument passed to the `eventTarget.dispatchEvent()` function.
Async functions may be used as event listeners. If an async handler function rejects, the rejection is captured and handled as described in [`EventTarget` error handling](https://nodejs.org/docs/latest/api/events.html#eventtarget-error-handling).
An error thrown by one handler function does not prevent the other handlers from being invoked.
The return value of a handler function is ignored.
Handlers are always invoked in the order they were added.
Handler functions may mutate the `event` object.
```
function handler1(event) {
  console.log(event.type);  // Prints 'foo'
  event.a = 1;
}

async function handler2(event) {
  console.log(event.type);  // Prints 'foo'
  console.log(event.a);  // Prints 1
}

const handler3 = {
  handleEvent(event) {
    console.log(event.type);  // Prints 'foo'
  },
};

const handler4 = {
  async handleEvent(event) {
    console.log(event.type);  // Prints 'foo'
  },
};

const target = new EventTarget();

target.addEventListener('foo', handler1);
target.addEventListener('foo', handler2);
target.addEventListener('foo', handler3);
target.addEventListener('foo', handler4, { once: true });
copy
```

####  `EventTarget` error handling[#](https://nodejs.org/docs/latest/api/events.html#eventtarget-error-handling)
When a registered event listener throws (or returns a Promise that rejects), by default the error is treated as an uncaught exception on `process.nextTick()`. This means uncaught exceptions in `EventTarget`s will terminate the Node.js process by default.
Throwing within an event listener will _not_ stop the other registered handlers from being invoked.
The `EventTarget` does not implement any special default handling for `'error'` type events like `EventEmitter`.
Currently errors are first forwarded to the `process.on('error')` event before reaching `process.on('uncaughtException')`. This behavior is deprecated and will change in a future release to align `EventTarget` with other Node.js APIs. Any code relying on the `process.on('error')` event should be aligned with the new behavior.
#### Class: `Event`[#](https://nodejs.org/docs/latest/api/events.html#class-event)
Added in: v14.5.0History Version | Changes
---|---
v15.0.0 | The `Event` class is now available through the global object.
The `Event` object is an adaptation of the
#####  `event.bubbles`[#](https://nodejs.org/docs/latest/api/events.html#eventbubbles)
Added in: v14.5.0
  * Type: `false`.


This is not used in Node.js and is provided purely for completeness.
#####  `event.cancelBubble`[#](https://nodejs.org/docs/latest/api/events.html#eventcancelbubble)
Added in: v14.5.0
Stability: 3 - Legacy: Use [`event.stopPropagation()`](https://nodejs.org/docs/latest/api/events.html#eventstoppropagation) instead.
  * Type:


Alias for `event.stopPropagation()` if set to `true`. This is not used in Node.js and is provided purely for completeness.
#####  `event.cancelable`[#](https://nodejs.org/docs/latest/api/events.html#eventcancelable)
Added in: v14.5.0
  * Type: `cancelable` option.


#####  `event.composed`[#](https://nodejs.org/docs/latest/api/events.html#eventcomposed)
Added in: v14.5.0
  * Type: `false`.


This is not used in Node.js and is provided purely for completeness.
#####  `event.composedPath()`[#](https://nodejs.org/docs/latest/api/events.html#eventcomposedpath)
Added in: v14.5.0
Returns an array containing the current `EventTarget` as the only entry or empty if the event is not being dispatched. This is not used in Node.js and is provided purely for completeness.
#####  `event.currentTarget`[#](https://nodejs.org/docs/latest/api/events.html#eventcurrenttarget)
Added in: v14.5.0
  * Type: [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) The `EventTarget` dispatching the event.


Alias for `event.target`.
#####  `event.defaultPrevented`[#](https://nodejs.org/docs/latest/api/events.html#eventdefaultprevented)
Added in: v14.5.0
  * Type:


Is `true` if `cancelable` is `true` and `event.preventDefault()` has been called.
#####  `event.eventPhase`[#](https://nodejs.org/docs/latest/api/events.html#eventeventphase)
Added in: v14.5.0
  * Type: `0` while an event is not being dispatched, `2` while it is being dispatched.


This is not used in Node.js and is provided purely for completeness.
#####  `event.initEvent(type[, bubbles[, cancelable]])`[#](https://nodejs.org/docs/latest/api/events.html#eventiniteventtype-bubbles-cancelable)
Added in: v19.5.0
Stability: 3 - Legacy: The WHATWG spec considers it deprecated and users shouldn't use it at all.
  * `type`
  * `bubbles`
  * `cancelable`


Redundant with event constructors and incapable of setting `composed`. This is not used in Node.js and is provided purely for completeness.
#####  `event.isTrusted`[#](https://nodejs.org/docs/latest/api/events.html#eventistrusted)
Added in: v14.5.0
  * Type:


The [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) `"abort"` event is emitted with `isTrusted` set to `true`. The value is `false` in all other cases.
#####  `event.preventDefault()`[#](https://nodejs.org/docs/latest/api/events.html#eventpreventdefault)
Added in: v14.5.0
Sets the `defaultPrevented` property to `true` if `cancelable` is `true`.
#####  `event.returnValue`[#](https://nodejs.org/docs/latest/api/events.html#eventreturnvalue)
Added in: v14.5.0
Stability: 3 - Legacy: Use [`event.defaultPrevented`](https://nodejs.org/docs/latest/api/events.html#eventdefaultprevented) instead.
  * Type:


The value of `event.returnValue` is always the opposite of `event.defaultPrevented`. This is not used in Node.js and is provided purely for completeness.
#####  `event.srcElement`[#](https://nodejs.org/docs/latest/api/events.html#eventsrcelement)
Added in: v14.5.0
Stability: 3 - Legacy: Use [`event.target`](https://nodejs.org/docs/latest/api/events.html#eventtarget) instead.
  * Type: [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) The `EventTarget` dispatching the event.


Alias for `event.target`.
#####  `event.stopImmediatePropagation()`[#](https://nodejs.org/docs/latest/api/events.html#eventstopimmediatepropagation)
Added in: v14.5.0
Stops the invocation of event listeners after the current one completes.
#####  `event.stopPropagation()`[#](https://nodejs.org/docs/latest/api/events.html#eventstoppropagation)
Added in: v14.5.0
This is not used in Node.js and is provided purely for completeness.
#####  `event.target`[#](https://nodejs.org/docs/latest/api/events.html#eventtarget)
Added in: v14.5.0
  * Type: [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) The `EventTarget` dispatching the event.


#####  `event.timeStamp`[#](https://nodejs.org/docs/latest/api/events.html#eventtimestamp)
Added in: v14.5.0
  * Type:


The millisecond timestamp when the `Event` object was created.
#####  `event.type`[#](https://nodejs.org/docs/latest/api/events.html#eventtype)
Added in: v14.5.0
  * Type:


The event type identifier.
#### Class: `EventTarget`[#](https://nodejs.org/docs/latest/api/events.html#class-eventtarget)
Added in: v14.5.0History Version | Changes
---|---
v15.0.0 | The `EventTarget` class is now available through the global object.
#####  `eventTarget.addEventListener(type, listener[, options])`[#](https://nodejs.org/docs/latest/api/events.html#eventtargetaddeventlistenertype-listener-options)
Added in: v14.5.0History Version | Changes
---|---
v15.4.0 | add support for `signal` option.
  * `type`
  * `listener` [`<EventListener>`](https://nodejs.org/docs/latest/api/events.html#event-listener)
  * `options`
    * `once` `true`, the listener is automatically removed when it is first invoked. **Default:** `false`.
    * `passive` `true`, serves as a hint that the listener will not call the `Event` object's `preventDefault()` method. **Default:** `false`.
    * `capture` **Default:** `false`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) The listener will be removed when the given AbortSignal object's `abort()` method is called.


Adds a new handler for the `type` event. Any given `listener` is added only once per `type` and per `capture` option value.
If the `once` option is `true`, the `listener` is removed after the next time a `type` event is dispatched.
The `capture` option is not used by Node.js in any functional way other than tracking registered event listeners per the `EventTarget` specification. Specifically, the `capture` option is used as part of the key when registering a `listener`. Any individual `listener` may be added once with `capture = false`, and once with `capture = true`.
```
function handler(event) {}

const target = new EventTarget();
target.addEventListener('foo', handler, { capture: true });  // first
target.addEventListener('foo', handler, { capture: false }); // second

// Removes the second instance of handler
target.removeEventListener('foo', handler);

// Removes the first instance of handler
target.removeEventListener('foo', handler, { capture: true });
copy
```

#####  `eventTarget.dispatchEvent(event)`[#](https://nodejs.org/docs/latest/api/events.html#eventtargetdispatcheventevent)
Added in: v14.5.0
  * `event` [`<Event>`](https://nodejs.org/docs/latest/api/events.html#class-event)
  * Returns: `true` if either event's `cancelable` attribute value is false or its `preventDefault()` method was not invoked, otherwise `false`.


Dispatches the `event` to the list of handlers for `event.type`.
The registered event listeners is synchronously invoked in the order they were registered.
#####  `eventTarget.removeEventListener(type, listener[, options])`[#](https://nodejs.org/docs/latest/api/events.html#eventtargetremoveeventlistenertype-listener-options)
Added in: v14.5.0
  * `type`
  * `listener` [`<EventListener>`](https://nodejs.org/docs/latest/api/events.html#event-listener)
  * `options`
    * `capture`


Removes the `listener` from the list of handlers for event `type`.
#### Class: `CustomEvent`[#](https://nodejs.org/docs/latest/api/events.html#class-customevent)
Added in: v18.7.0, v16.17.0History Version | Changes
---|---
v23.0.0 | No longer experimental.
v22.1.0, v20.13.0 | CustomEvent is now stable.
v19.0.0 | No longer behind `--experimental-global-customevent` CLI flag.
  * Extends: [`<Event>`](https://nodejs.org/docs/latest/api/events.html#class-event)


The `CustomEvent` object is an adaptation of the
#####  `event.detail`[#](https://nodejs.org/docs/latest/api/events.html#eventdetail)
Added in: v18.7.0, v16.17.0History Version | Changes
---|---
v22.1.0, v20.13.0 | CustomEvent is now stable.
  * Type:


Read-only.
#### Class: `NodeEventTarget`[#](https://nodejs.org/docs/latest/api/events.html#class-nodeeventtarget)
Added in: v14.5.0
  * Extends: [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget)


The `NodeEventTarget` is a Node.js-specific extension to `EventTarget` that emulates a subset of the `EventEmitter` API.
#####  `nodeEventTarget.addListener(type, listener)`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargetaddlistenertype-listener)
Added in: v14.5.0
  * `type`
  * `listener` [`<EventListener>`](https://nodejs.org/docs/latest/api/events.html#event-listener)
  * Returns: [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) this


Node.js-specific extension to the `EventTarget` class that emulates the equivalent `EventEmitter` API. The only difference between `addListener()` and `addEventListener()` is that `addListener()` will return a reference to the `EventTarget`.
#####  `nodeEventTarget.emit(type, arg)`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargetemittype-arg)
Added in: v15.2.0
  * `type`
  * `arg`
  * Returns: `true` if event listeners registered for the `type` exist, otherwise `false`.


Node.js-specific extension to the `EventTarget` class that dispatches the `arg` to the list of handlers for `type`.
#####  `nodeEventTarget.eventNames()`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargeteventnames)
Added in: v14.5.0
  * Returns:


Node.js-specific extension to the `EventTarget` class that returns an array of event `type` names for which event listeners are registered.
#####  `nodeEventTarget.listenerCount(type)`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargetlistenercounttype)
Added in: v14.5.0
  * `type`
  * Returns:


Node.js-specific extension to the `EventTarget` class that returns the number of event listeners registered for the `type`.
#####  `nodeEventTarget.setMaxListeners(n)`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargetsetmaxlistenersn)
Added in: v14.5.0
  * `n`


Node.js-specific extension to the `EventTarget` class that sets the number of max event listeners as `n`.
#####  `nodeEventTarget.getMaxListeners()`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargetgetmaxlisteners)
Added in: v14.5.0
  * Returns:


Node.js-specific extension to the `EventTarget` class that returns the number of max event listeners.
#####  `nodeEventTarget.off(type, listener[, options])`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargetofftype-listener-options)
Added in: v14.5.0
  * `type`
  * `listener` [`<EventListener>`](https://nodejs.org/docs/latest/api/events.html#event-listener)
  * `options`
    * `capture`
  * Returns: [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) this


Node.js-specific alias for `eventTarget.removeEventListener()`.
#####  `nodeEventTarget.on(type, listener)`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargetontype-listener)
Added in: v14.5.0
  * `type`
  * `listener` [`<EventListener>`](https://nodejs.org/docs/latest/api/events.html#event-listener)
  * Returns: [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) this


Node.js-specific alias for `eventTarget.addEventListener()`.
#####  `nodeEventTarget.once(type, listener)`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargetoncetype-listener)
Added in: v14.5.0
  * `type`
  * `listener` [`<EventListener>`](https://nodejs.org/docs/latest/api/events.html#event-listener)
  * Returns: [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) this


Node.js-specific extension to the `EventTarget` class that adds a `once` listener for the given event `type`. This is equivalent to calling `on` with the `once` option set to `true`.
#####  `nodeEventTarget.removeAllListeners([type])`[#](https://nodejs.org/docs/latest/api/events.html#nodeeventtargetremovealllistenerstype)
Added in: v14.5.0
  * `type`
  * Returns: [`<EventTarget>`](https://nodejs.org/docs/latest/api/events.html#class-eventtarget) this


Node.js-specific extension to the `EventTarget` class. If `type` is specified, removes all registered listeners for `type`, otherwise removes all registered listeners.
