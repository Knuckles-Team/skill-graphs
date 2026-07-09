## Diagnostics Channel[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#diagnostics-channel)
**Source Code:** Added in: v15.1.0, v14.17.0History Version | Changes
---|---
v19.2.0, v18.13.0 | diagnostics_channel is now Stable.
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:diagnostics_channel` module provides an API to create named channels to report arbitrary message data for diagnostics purposes.
It can be accessed using:
```
import diagnostics_channel from 'node:diagnostics_channel';
const diagnostics_channel = require('node:diagnostics_channel');
copy
```

It is intended that a module writer wanting to report diagnostics messages will create one or many top-level channels to report messages through. Channels may also be acquired at runtime but it is not encouraged due to the additional overhead of doing so. Channels may be exported for convenience, but as long as the name is known it can be acquired anywhere.
If you intend for your module to produce diagnostics data for others to consume it is recommended that you include documentation of what named channels are used along with the shape of the message data. Channel names should generally include the module name to avoid collisions with data from other modules.
### Public API[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#public-api)
#### Overview[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#overview)
Following is a simple overview of the public API.
```
import diagnostics_channel from 'node:diagnostics_channel';

// Get a reusable channel object
const channel = diagnostics_channel.channel('my-channel');

function onMessage(message, name) {
  // Received data
}

// Subscribe to the channel
diagnostics_channel.subscribe('my-channel', onMessage);

// Check if the channel has an active subscriber
if (channel.hasSubscribers) {
  // Publish data to the channel
  channel.publish({
    some: 'data',
  });
}

// Unsubscribe from the channel
diagnostics_channel.unsubscribe('my-channel', onMessage);
const diagnostics_channel = require('node:diagnostics_channel');

// Get a reusable channel object
const channel = diagnostics_channel.channel('my-channel');

function onMessage(message, name) {
  // Received data
}

// Subscribe to the channel
diagnostics_channel.subscribe('my-channel', onMessage);

// Check if the channel has an active subscriber
if (channel.hasSubscribers) {
  // Publish data to the channel
  channel.publish({
    some: 'data',
  });
}

// Unsubscribe from the channel
diagnostics_channel.unsubscribe('my-channel', onMessage);
copy
```

#####  `diagnostics_channel.hasSubscribers(name)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#diagnostics-channelhassubscribersname)
Added in: v15.1.0, v14.17.0
  * `name`
  * Returns:


Check if there are active subscribers to the named channel. This is helpful if the message you want to send might be expensive to prepare.
This API is optional but helpful when trying to publish messages from very performance-sensitive code.
```
import diagnostics_channel from 'node:diagnostics_channel';

if (diagnostics_channel.hasSubscribers('my-channel')) {
  // There are subscribers, prepare and publish message
}
const diagnostics_channel = require('node:diagnostics_channel');

if (diagnostics_channel.hasSubscribers('my-channel')) {
  // There are subscribers, prepare and publish message
}
copy
```

#####  `diagnostics_channel.channel(name)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#diagnostics-channelchannelname)
Added in: v15.1.0, v14.17.0
  * `name`
  * Returns: [`<Channel>`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#class-channel) The named channel object


This is the primary entry-point for anyone wanting to publish to a named channel. It produces a channel object which is optimized to reduce overhead at publish time as much as possible.
```
import diagnostics_channel from 'node:diagnostics_channel';

const channel = diagnostics_channel.channel('my-channel');
const diagnostics_channel = require('node:diagnostics_channel');

const channel = diagnostics_channel.channel('my-channel');
copy
```

#####  `diagnostics_channel.subscribe(name, onMessage)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#diagnostics-channelsubscribename-onmessage)
Added in: v18.7.0, v16.17.0
  * `name`
  * `onMessage`
    * `message`
    * `name`


Register a message handler to subscribe to this channel. This message handler will be run synchronously whenever a message is published to the channel. Any errors thrown in the message handler will trigger an [`'uncaughtException'`](https://nodejs.org/docs/latest/api/process.html#event-uncaughtexception).
```
import diagnostics_channel from 'node:diagnostics_channel';

diagnostics_channel.subscribe('my-channel', (message, name) => {
  // Received data
});
const diagnostics_channel = require('node:diagnostics_channel');

diagnostics_channel.subscribe('my-channel', (message, name) => {
  // Received data
});
copy
```

#####  `diagnostics_channel.unsubscribe(name, onMessage)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#diagnostics-channelunsubscribename-onmessage)
Added in: v18.7.0, v16.17.0
  * `name`
  * `onMessage`
  * Returns: `true` if the handler was found, `false` otherwise.


Remove a message handler previously registered to this channel with [`diagnostics_channel.subscribe(name, onMessage)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#diagnostics_channelsubscribename-onmessage).
```
import diagnostics_channel from 'node:diagnostics_channel';

function onMessage(message, name) {
  // Received data
}

diagnostics_channel.subscribe('my-channel', onMessage);

diagnostics_channel.unsubscribe('my-channel', onMessage);
const diagnostics_channel = require('node:diagnostics_channel');

function onMessage(message, name) {
  // Received data
}

diagnostics_channel.subscribe('my-channel', onMessage);

diagnostics_channel.unsubscribe('my-channel', onMessage);
copy
```

#####  `diagnostics_channel.tracingChannel(nameOrChannels)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#diagnostics-channeltracingchannelnameorchannels)
Added in: v19.9.0, v18.19.0
Stability: 1 - Experimental
  * `nameOrChannels` [`<TracingChannel>`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#class-tracingchannel) Channel name or object containing all the [TracingChannel Channels](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannel-channels)
  * Returns: [`<TracingChannel>`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#class-tracingchannel) Collection of channels to trace with


Creates a [`TracingChannel`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#class-tracingchannel) wrapper for the given [TracingChannel Channels](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannel-channels). If a name is given, the corresponding tracing channels will be created in the form of `tracing:${name}:${eventType}` where `eventType` corresponds to the types of [TracingChannel Channels](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannel-channels).
```
import diagnostics_channel from 'node:diagnostics_channel';

const channelsByName = diagnostics_channel.tracingChannel('my-channel');

// or...

const channelsByCollection = diagnostics_channel.tracingChannel({
  start: diagnostics_channel.channel('tracing:my-channel:start'),
  end: diagnostics_channel.channel('tracing:my-channel:end'),
  asyncStart: diagnostics_channel.channel('tracing:my-channel:asyncStart'),
  asyncEnd: diagnostics_channel.channel('tracing:my-channel:asyncEnd'),
  error: diagnostics_channel.channel('tracing:my-channel:error'),
});
const diagnostics_channel = require('node:diagnostics_channel');

const channelsByName = diagnostics_channel.tracingChannel('my-channel');

// or...

const channelsByCollection = diagnostics_channel.tracingChannel({
  start: diagnostics_channel.channel('tracing:my-channel:start'),
  end: diagnostics_channel.channel('tracing:my-channel:end'),
  asyncStart: diagnostics_channel.channel('tracing:my-channel:asyncStart'),
  asyncEnd: diagnostics_channel.channel('tracing:my-channel:asyncEnd'),
  error: diagnostics_channel.channel('tracing:my-channel:error'),
});
copy
```

#### Class: `Channel`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#class-channel)
Added in: v15.1.0, v14.17.0
The class `Channel` represents an individual named channel within the data pipeline. It is used to track subscribers and to publish messages when there are subscribers present. It exists as a separate object to avoid channel lookups at publish time, enabling very fast publish speeds and allowing for heavy use while incurring very minimal cost. Channels are created with [`diagnostics_channel.channel(name)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#diagnostics_channelchannelname), constructing a channel directly with `new Channel(name)` is not supported.
#####  `channel.hasSubscribers`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelhassubscribers)
Added in: v15.1.0, v14.17.0
  * Returns:


Check if there are active subscribers to this channel. This is helpful if the message you want to send might be expensive to prepare.
This API is optional but helpful when trying to publish messages from very performance-sensitive code.
```
import diagnostics_channel from 'node:diagnostics_channel';

const channel = diagnostics_channel.channel('my-channel');

if (channel.hasSubscribers) {
  // There are subscribers, prepare and publish message
}
const diagnostics_channel = require('node:diagnostics_channel');

const channel = diagnostics_channel.channel('my-channel');

if (channel.hasSubscribers) {
  // There are subscribers, prepare and publish message
}
copy
```

#####  `channel.publish(message)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelpublishmessage)
Added in: v15.1.0, v14.17.0
  * `message`


Publish a message to any subscribers to the channel. This will trigger message handlers synchronously so they will execute within the same context.
```
import diagnostics_channel from 'node:diagnostics_channel';

const channel = diagnostics_channel.channel('my-channel');

channel.publish({
  some: 'message',
});
const diagnostics_channel = require('node:diagnostics_channel');

const channel = diagnostics_channel.channel('my-channel');

channel.publish({
  some: 'message',
});
copy
```

#####  `channel.subscribe(onMessage)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelsubscribeonmessage)
Added in: v15.1.0, v14.17.0History Version | Changes
---|---
v24.8.0, v22.20.0 | Deprecation revoked.
v18.7.0, v16.17.0 | Documentation-only deprecation.
  * `onMessage`
    * `message`
    * `name`


Register a message handler to subscribe to this channel. This message handler will be run synchronously whenever a message is published to the channel. Any errors thrown in the message handler will trigger an [`'uncaughtException'`](https://nodejs.org/docs/latest/api/process.html#event-uncaughtexception).
```
import diagnostics_channel from 'node:diagnostics_channel';

const channel = diagnostics_channel.channel('my-channel');

channel.subscribe((message, name) => {
  // Received data
});
const diagnostics_channel = require('node:diagnostics_channel');

const channel = diagnostics_channel.channel('my-channel');

channel.subscribe((message, name) => {
  // Received data
});
copy
```

#####  `channel.unsubscribe(onMessage)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelunsubscribeonmessage)
Added in: v15.1.0, v14.17.0History Version | Changes
---|---
v24.8.0, v22.20.0 | Deprecation revoked.
v18.7.0, v16.17.0 | Documentation-only deprecation.
v17.1.0, v16.14.0, v14.19.0 | Added return value. Added to channels without subscribers.
  * `onMessage`
  * Returns: `true` if the handler was found, `false` otherwise.


Remove a message handler previously registered to this channel with [`channel.subscribe(onMessage)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelsubscribeonmessage).
```
import diagnostics_channel from 'node:diagnostics_channel';

const channel = diagnostics_channel.channel('my-channel');

function onMessage(message, name) {
  // Received data
}

channel.subscribe(onMessage);

channel.unsubscribe(onMessage);
const diagnostics_channel = require('node:diagnostics_channel');

const channel = diagnostics_channel.channel('my-channel');

function onMessage(message, name) {
  // Received data
}

channel.subscribe(onMessage);

channel.unsubscribe(onMessage);
copy
```

#####  `channel.bindStore(store[, transform])`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelbindstorestore-transform)
Added in: v19.9.0, v18.19.0
Stability: 1 - Experimental
  * `store` [`<AsyncLocalStorage>`](https://nodejs.org/docs/latest/api/async_context.html#class-asynclocalstorage) The store to which to bind the context data
  * `transform`


When [`channel.runStores(context, ...)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelrunstorescontext-fn-thisarg-args) is called, the given context data will be applied to any store bound to the channel. If the store has already been bound the previous `transform` function will be replaced with the new one. The `transform` function may be omitted to set the given context data as the context directly.
```
import diagnostics_channel from 'node:diagnostics_channel';
import { AsyncLocalStorage } from 'node:async_hooks';

const store = new AsyncLocalStorage();

const channel = diagnostics_channel.channel('my-channel');

channel.bindStore(store, (data) => {
  return { data };
});
const diagnostics_channel = require('node:diagnostics_channel');
const { AsyncLocalStorage } = require('node:async_hooks');

const store = new AsyncLocalStorage();

const channel = diagnostics_channel.channel('my-channel');

channel.bindStore(store, (data) => {
  return { data };
});
copy
```

#####  `channel.unbindStore(store)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelunbindstorestore)
Added in: v19.9.0, v18.19.0
Stability: 1 - Experimental
  * `store` [`<AsyncLocalStorage>`](https://nodejs.org/docs/latest/api/async_context.html#class-asynclocalstorage) The store to unbind from the channel.
  * Returns: `true` if the store was found, `false` otherwise.


Remove a message handler previously registered to this channel with [`channel.bindStore(store)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelbindstorestore-transform).
```
import diagnostics_channel from 'node:diagnostics_channel';
import { AsyncLocalStorage } from 'node:async_hooks';

const store = new AsyncLocalStorage();

const channel = diagnostics_channel.channel('my-channel');

channel.bindStore(store);
channel.unbindStore(store);
const diagnostics_channel = require('node:diagnostics_channel');
const { AsyncLocalStorage } = require('node:async_hooks');

const store = new AsyncLocalStorage();

const channel = diagnostics_channel.channel('my-channel');

channel.bindStore(store);
channel.unbindStore(store);
copy
```

#####  `channel.runStores(context, fn[, thisArg[, ...args]])`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelrunstorescontext-fn-thisarg-args)
Added in: v19.9.0, v18.19.0
Stability: 1 - Experimental
  * `context`
  * `fn`
  * `thisArg`
  * `...args`


Applies the given data to any AsyncLocalStorage instances bound to the channel for the duration of the given function, then publishes to the channel within the scope of that data is applied to the stores.
If a transform function was given to [`channel.bindStore(store)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelbindstorestore-transform) it will be applied to transform the message data before it becomes the context value for the store. The prior storage context is accessible from within the transform function in cases where context linking is required.
The context applied to the store should be accessible in any async code which continues from execution which began during the given function, however there are some situations in which [context loss](https://nodejs.org/docs/latest/api/async_context.html#troubleshooting-context-loss) may occur.
```
import diagnostics_channel from 'node:diagnostics_channel';
import { AsyncLocalStorage } from 'node:async_hooks';

const store = new AsyncLocalStorage();

const channel = diagnostics_channel.channel('my-channel');

channel.bindStore(store, (message) => {
  const parent = store.getStore();
  return new Span(message, parent);
});
channel.runStores({ some: 'message' }, () => {
  store.getStore(); // Span({ some: 'message' })
});
const diagnostics_channel = require('node:diagnostics_channel');
const { AsyncLocalStorage } = require('node:async_hooks');

const store = new AsyncLocalStorage();

const channel = diagnostics_channel.channel('my-channel');

channel.bindStore(store, (message) => {
  const parent = store.getStore();
  return new Span(message, parent);
});
channel.runStores({ some: 'message' }, () => {
  store.getStore(); // Span({ some: 'message' })
});
copy
```

#### Class: `TracingChannel`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#class-tracingchannel)
Added in: v19.9.0, v18.19.0
Stability: 1 - Experimental
The class `TracingChannel` is a collection of [TracingChannel Channels](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannel-channels) which together express a single traceable action. It is used to formalize and simplify the process of producing events for tracing application flow. [`diagnostics_channel.tracingChannel()`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#diagnostics_channeltracingchannelnameorchannels) is used to construct a `TracingChannel`. As with `Channel` it is recommended to create and reuse a single `TracingChannel` at the top-level of the file rather than creating them dynamically.
#####  `tracingChannel.subscribe(subscribers)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannelsubscribesubscribers)
Added in: v19.9.0, v18.19.0
  * `subscribers` [TracingChannel Channels](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannel-channels) subscribers
    * `start` [`start` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#startevent) subscriber
    * `end` [`end` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#endevent) subscriber
    * `asyncStart` [`asyncStart` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncstartevent) subscriber
    * `asyncEnd` [`asyncEnd` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncendevent) subscriber
    * `error` [`error` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#errorevent) subscriber


Helper to subscribe a collection of functions to the corresponding channels. This is the same as calling [`channel.subscribe(onMessage)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelsubscribeonmessage) on each channel individually.
```
import diagnostics_channel from 'node:diagnostics_channel';

const channels = diagnostics_channel.tracingChannel('my-channel');

channels.subscribe({
  start(message) {
    // Handle start message
  },
  end(message) {
    // Handle end message
  },
  asyncStart(message) {
    // Handle asyncStart message
  },
  asyncEnd(message) {
    // Handle asyncEnd message
  },
  error(message) {
    // Handle error message
  },
});
const diagnostics_channel = require('node:diagnostics_channel');

const channels = diagnostics_channel.tracingChannel('my-channel');

channels.subscribe({
  start(message) {
    // Handle start message
  },
  end(message) {
    // Handle end message
  },
  asyncStart(message) {
    // Handle asyncStart message
  },
  asyncEnd(message) {
    // Handle asyncEnd message
  },
  error(message) {
    // Handle error message
  },
});
copy
```

#####  `tracingChannel.unsubscribe(subscribers)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannelunsubscribesubscribers)
Added in: v19.9.0, v18.19.0
  * `subscribers` [TracingChannel Channels](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannel-channels) subscribers
    * `start` [`start` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#startevent) subscriber
    * `end` [`end` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#endevent) subscriber
    * `asyncStart` [`asyncStart` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncstartevent) subscriber
    * `asyncEnd` [`asyncEnd` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncendevent) subscriber
    * `error` [`error` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#errorevent) subscriber
  * Returns: `true` if all handlers were successfully unsubscribed, and `false` otherwise.


Helper to unsubscribe a collection of functions from the corresponding channels. This is the same as calling [`channel.unsubscribe(onMessage)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelunsubscribeonmessage) on each channel individually.
```
import diagnostics_channel from 'node:diagnostics_channel';

const channels = diagnostics_channel.tracingChannel('my-channel');

channels.unsubscribe({
  start(message) {
    // Handle start message
  },
  end(message) {
    // Handle end message
  },
  asyncStart(message) {
    // Handle asyncStart message
  },
  asyncEnd(message) {
    // Handle asyncEnd message
  },
  error(message) {
    // Handle error message
  },
});
const diagnostics_channel = require('node:diagnostics_channel');

const channels = diagnostics_channel.tracingChannel('my-channel');

channels.unsubscribe({
  start(message) {
    // Handle start message
  },
  end(message) {
    // Handle end message
  },
  asyncStart(message) {
    // Handle asyncStart message
  },
  asyncEnd(message) {
    // Handle asyncEnd message
  },
  error(message) {
    // Handle error message
  },
});
copy
```

#####  `tracingChannel.traceSync(fn[, context[, thisArg[, ...args]]])`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchanneltracesyncfn-context-thisarg-args)
Added in: v19.9.0, v18.19.0
  * `fn`
  * `context`
  * `thisArg`
  * `...args`
  * Returns:


Trace a synchronous function call. This will always produce a [`start` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#startevent) and [`end` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#endevent) around the execution and may produce an [`error` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#errorevent) if the given function throws an error. This will run the given function using [`channel.runStores(context, ...)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelrunstorescontext-fn-thisarg-args) on the `start` channel which ensures all events should have any bound stores set to match this trace context.
To ensure only correct trace graphs are formed, events will only be published if subscribers are present prior to starting the trace. Subscriptions which are added after the trace begins will not receive future events from that trace, only future traces will be seen.
```
import diagnostics_channel from 'node:diagnostics_channel';

const channels = diagnostics_channel.tracingChannel('my-channel');

channels.traceSync(() => {
  // Do something
}, {
  some: 'thing',
});
const diagnostics_channel = require('node:diagnostics_channel');

const channels = diagnostics_channel.tracingChannel('my-channel');

channels.traceSync(() => {
  // Do something
}, {
  some: 'thing',
});
copy
```

#####  `tracingChannel.tracePromise(fn[, context[, thisArg[, ...args]]])`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchanneltracepromisefn-context-thisarg-args)
Added in: v19.9.0, v18.19.0
  * `fn`
  * `context`
  * `thisArg`
  * `...args`
  * Returns:


Trace a promise-returning function call. This will always produce a [`start` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#startevent) and [`end` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#endevent) around the synchronous portion of the function execution, and will produce an [`asyncStart` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncstartevent) and [`asyncEnd` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncendevent) when a promise continuation is reached. It may also produce an [`error` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#errorevent) if the given function throws an error or the returned promise rejects. This will run the given function using [`channel.runStores(context, ...)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelrunstorescontext-fn-thisarg-args) on the `start` channel which ensures all events should have any bound stores set to match this trace context.
To ensure only correct trace graphs are formed, events will only be published if subscribers are present prior to starting the trace. Subscriptions which are added after the trace begins will not receive future events from that trace, only future traces will be seen.
```
import diagnostics_channel from 'node:diagnostics_channel';
