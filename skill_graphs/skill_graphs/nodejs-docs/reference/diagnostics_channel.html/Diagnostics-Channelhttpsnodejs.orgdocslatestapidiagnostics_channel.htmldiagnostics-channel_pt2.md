
const channels = diagnostics_channel.tracingChannel('my-channel');

channels.tracePromise(async () => {
  // Do something
}, {
  some: 'thing',
});
const diagnostics_channel = require('node:diagnostics_channel');

const channels = diagnostics_channel.tracingChannel('my-channel');

channels.tracePromise(async () => {
  // Do something
}, {
  some: 'thing',
});
copy
```

#####  `tracingChannel.traceCallback(fn[, position[, context[, thisArg[, ...args]]]])`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchanneltracecallbackfn-position-context-thisarg-args)
Added in: v19.9.0, v18.19.0
  * `fn`
  * `position` `undefined` is passed)
  * `context` `{}` if `undefined` is passed)
  * `thisArg`
  * `...args`
  * Returns:


Trace a callback-receiving function call. The callback is expected to follow the error as first arg convention typically used. This will always produce a [`start` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#startevent) and [`end` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#endevent) around the synchronous portion of the function execution, and will produce a [`asyncStart` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncstartevent) and [`asyncEnd` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncendevent) around the callback execution. It may also produce an [`error` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#errorevent) if the given function throws or the first argument passed to the callback is set. This will run the given function using [`channel.runStores(context, ...)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelrunstorescontext-fn-thisarg-args) on the `start` channel which ensures all events should have any bound stores set to match this trace context.
To ensure only correct trace graphs are formed, events will only be published if subscribers are present prior to starting the trace. Subscriptions which are added after the trace begins will not receive future events from that trace, only future traces will be seen.
```
import diagnostics_channel from 'node:diagnostics_channel';

const channels = diagnostics_channel.tracingChannel('my-channel');

channels.traceCallback((arg1, callback) => {
  // Do something
  callback(null, 'result');
}, 1, {
  some: 'thing',
}, thisArg, arg1, callback);
const diagnostics_channel = require('node:diagnostics_channel');

const channels = diagnostics_channel.tracingChannel('my-channel');

channels.traceCallback((arg1, callback) => {
  // Do something
  callback(null, 'result');
}, 1, {
  some: 'thing',
}, thisArg, arg1, callback);
copy
```

The callback will also be run with [`channel.runStores(context, ...)`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#channelrunstorescontext-fn-thisarg-args) which enables context loss recovery in some cases.
```
import diagnostics_channel from 'node:diagnostics_channel';
import { AsyncLocalStorage } from 'node:async_hooks';

const channels = diagnostics_channel.tracingChannel('my-channel');
const myStore = new AsyncLocalStorage();

// The start channel sets the initial store data to something
// and stores that store data value on the trace context object
channels.start.bindStore(myStore, (data) => {
  const span = new Span(data);
  data.span = span;
  return span;
});

// Then asyncStart can restore from that data it stored previously
channels.asyncStart.bindStore(myStore, (data) => {
  return data.span;
});
const diagnostics_channel = require('node:diagnostics_channel');
const { AsyncLocalStorage } = require('node:async_hooks');

const channels = diagnostics_channel.tracingChannel('my-channel');
const myStore = new AsyncLocalStorage();

// The start channel sets the initial store data to something
// and stores that store data value on the trace context object
channels.start.bindStore(myStore, (data) => {
  const span = new Span(data);
  data.span = span;
  return span;
});

// Then asyncStart can restore from that data it stored previously
channels.asyncStart.bindStore(myStore, (data) => {
  return data.span;
});
copy
```

#####  `tracingChannel.hasSubscribers`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannelhassubscribers)
Added in: v22.0.0, v20.13.0
  * Returns: `true` if any of the individual channels has a subscriber, `false` if not.


This is a helper method available on a [`TracingChannel`](https://nodejs.org/docs/latest/api/diagnostics_channel.html#class-tracingchannel) instance to check if any of the [TracingChannel Channels](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannel-channels) have subscribers. A `true` is returned if any of them have at least one subscriber, a `false` is returned otherwise.
```
import diagnostics_channel from 'node:diagnostics_channel';

const channels = diagnostics_channel.tracingChannel('my-channel');

if (channels.hasSubscribers) {
  // Do something
}
const diagnostics_channel = require('node:diagnostics_channel');

const channels = diagnostics_channel.tracingChannel('my-channel');

if (channels.hasSubscribers) {
  // Do something
}
copy
```

#### TracingChannel Channels[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#tracingchannel-channels)
A TracingChannel is a collection of several diagnostics_channels representing specific points in the execution lifecycle of a single traceable action. The behavior is split into five diagnostics_channels consisting of `start`, `end`, `asyncStart`, `asyncEnd`, and `error`. A single traceable action will share the same event object between all events, this can be helpful for managing correlation through a weakmap.
These event objects will be extended with `result` or `error` values when the task "completes". In the case of a synchronous task the `result` will be the return value and the `error` will be anything thrown from the function. With callback-based async functions the `result` will be the second argument of the callback while the `error` will either be a thrown error visible in the `end` event or the first callback argument in either of the `asyncStart` or `asyncEnd` events.
To ensure only correct trace graphs are formed, events should only be published if subscribers are present prior to starting the trace. Subscriptions which are added after the trace begins should not receive future events from that trace, only future traces will be seen.
Tracing channels should follow a naming pattern of:
  * `tracing:module.class.method:start` or `tracing:module.function:start`
  * `tracing:module.class.method:end` or `tracing:module.function:end`
  * `tracing:module.class.method:asyncStart` or `tracing:module.function:asyncStart`
  * `tracing:module.class.method:asyncEnd` or `tracing:module.function:asyncEnd`
  * `tracing:module.class.method:error` or `tracing:module.function:error`


#####  `start(event)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#startevent)
  * Name: `tracing:${name}:start`


The `start` event represents the point at which a function is called. At this point the event data may contain function arguments or anything else available at the very start of the execution of the function.
#####  `end(event)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#endevent)
  * Name: `tracing:${name}:end`


The `end` event represents the point at which a function call returns a value. In the case of an async function this is when the promise returned not when the function itself makes a return statement internally. At this point, if the traced function was synchronous the `result` field will be set to the return value of the function. Alternatively, the `error` field may be present to represent any thrown errors.
It is recommended to listen specifically to the `error` event to track errors as it may be possible for a traceable action to produce multiple errors. For example, an async task which fails may be started internally before the sync part of the task then throws an error.
#####  `asyncStart(event)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncstartevent)
  * Name: `tracing:${name}:asyncStart`


The `asyncStart` event represents the callback or continuation of a traceable function being reached. At this point things like callback arguments may be available, or anything else expressing the "result" of the action.
For callbacks-based functions, the first argument of the callback will be assigned to the `error` field, if not `undefined` or `null`, and the second argument will be assigned to the `result` field.
For promises, the argument to the `resolve` path will be assigned to `result` or the argument to the `reject` path will be assign to `error`.
It is recommended to listen specifically to the `error` event to track errors as it may be possible for a traceable action to produce multiple errors. For example, an async task which fails may be started internally before the sync part of the task then throws an error.
#####  `asyncEnd(event)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncendevent)
  * Name: `tracing:${name}:asyncEnd`


The `asyncEnd` event represents the callback of an asynchronous function returning. It's not likely event data will change after the `asyncStart` event, however it may be useful to see the point where the callback completes.
#####  `error(event)`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#errorevent)
  * Name: `tracing:${name}:error`


The `error` event represents any error produced by the traceable function either synchronously or asynchronously. If an error is thrown in the synchronous portion of the traced function the error will be assigned to the `error` field of the event and the `error` event will be triggered. If an error is received asynchronously through a callback or promise rejection it will also be assigned to the `error` field of the event and trigger the `error` event.
It is possible for a single traceable function call to produce errors multiple times so this should be considered when consuming this event. For example, if another async task is triggered internally which fails and then the sync part of the function then throws and error two `error` events will be emitted, one for the sync error and one for the async error.
#### Built-in Channels[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#built-in-channels)
##### Console[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#console)
Stability: 1 - Experimental
###### Event: `'console.log'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-consolelog)
  * `args`


Emitted when `console.log()` is called. Receives and array of the arguments passed to `console.log()`.
###### Event: `'console.info'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-consoleinfo)
  * `args`


Emitted when `console.info()` is called. Receives and array of the arguments passed to `console.info()`.
###### Event: `'console.debug'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-consoledebug)
  * `args`


Emitted when `console.debug()` is called. Receives and array of the arguments passed to `console.debug()`.
###### Event: `'console.warn'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-consolewarn)
  * `args`


Emitted when `console.warn()` is called. Receives and array of the arguments passed to `console.warn()`.
###### Event: `'console.error'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-consoleerror)
  * `args`


Emitted when `console.error()` is called. Receives and array of the arguments passed to `console.error()`.
##### HTTP[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#http)
Stability: 1 - Experimental
###### Event: `'http.client.request.created'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-httpclientrequestcreated)
  * `request` [`<http.ClientRequest>`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest)


Emitted when client creates a request object. Unlike `http.client.request.start`, this event is emitted before the request has been sent.
###### Event: `'http.client.request.start'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-httpclientrequeststart)
  * `request` [`<http.ClientRequest>`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest)


Emitted when client starts a request.
###### Event: `'http.client.request.error'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-httpclientrequesterror)
  * `request` [`<http.ClientRequest>`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest)
  * `error`


Emitted when an error occurs during a client request.
###### Event: `'http.client.response.finish'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-httpclientresponsefinish)
  * `request` [`<http.ClientRequest>`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest)
  * `response` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)


Emitted when client receives a response.
###### Event: `'http.server.request.start'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-httpserverrequeststart)
  * `request` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
  * `response` [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)
  * `socket` [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)
  * `server` [`<http.Server>`](https://nodejs.org/docs/latest/api/http.html#class-httpserver)


Emitted when server receives a request.
###### Event: `'http.server.response.created'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-httpserverresponsecreated)
  * `request` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
  * `response` [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)


Emitted when server creates a response. The event is emitted before the response is sent.
###### Event: `'http.server.response.finish'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-httpserverresponsefinish)
  * `request` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
  * `response` [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)
  * `socket` [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)
  * `server` [`<http.Server>`](https://nodejs.org/docs/latest/api/http.html#class-httpserver)


Emitted when server sends a response.
##### HTTP/2[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#http2)
Stability: 1 - Experimental
###### Event: `'http2.client.stream.created'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2clientstreamcreated)
  * `stream` [`<ClientHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream)
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)


Emitted when a stream is created on the client.
###### Event: `'http2.client.stream.start'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2clientstreamstart)
  * `stream` [`<ClientHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream)
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)


Emitted when a stream is started on the client.
###### Event: `'http2.client.stream.error'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2clientstreamerror)
  * `stream` [`<ClientHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream)
  * `error`


Emitted when an error occurs during the processing of a stream on the client.
###### Event: `'http2.client.stream.finish'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2clientstreamfinish)
  * `stream` [`<ClientHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream)
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * `flags`


Emitted when a stream is received on the client.
###### Event: `'http2.client.stream.bodyChunkSent'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2clientstreambodychunksent)
  * `stream` [`<ClientHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream)
  * `writev`
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `encoding`
  * `encoding`


Emitted when a chunk of the client stream body is being sent.
###### Event: `'http2.client.stream.bodySent'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2clientstreambodysent)
  * `stream` [`<ClientHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream)


Emitted after the client stream body has been fully sent.
###### Event: `'http2.client.stream.close'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2clientstreamclose)
  * `stream` [`<ClientHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream)


Emitted when a stream is closed on the client. The HTTP/2 error code used when closing the stream can be retrieved using the `stream.rstCode` property.
###### Event: `'http2.server.stream.created'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2serverstreamcreated)
  * `stream` [`<ServerHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2stream)
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)


Emitted when a stream is created on the server.
###### Event: `'http2.server.stream.start'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2serverstreamstart)
  * `stream` [`<ServerHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2stream)
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)


Emitted when a stream is started on the server.
###### Event: `'http2.server.stream.error'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2serverstreamerror)
  * `stream` [`<ServerHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2stream)
  * `error`


Emitted when an error occurs during the processing of a stream on the server.
###### Event: `'http2.server.stream.finish'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2serverstreamfinish)
  * `stream` [`<ServerHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2stream)
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * `flags`


Emitted when a stream is sent on the server.
###### Event: `'http2.server.stream.close'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-http2serverstreamclose)
  * `stream` [`<ServerHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2stream)


Emitted when a stream is closed on the server. The HTTP/2 error code used when closing the stream can be retrieved using the `stream.rstCode` property.
##### Modules[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#modules)
Stability: 1 - Experimental
###### Event: `'module.require.start'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-modulerequirestart)
  * `event`
    * `id` Argument passed to `require()`. Module name.
    * `parentFilename` Name of the module that attempted to require(id).


Emitted when `require()` is executed. See [`start` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#startevent).
###### Event: `'module.require.end'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-modulerequireend)
  * `event`
    * `id` Argument passed to `require()`. Module name.
    * `parentFilename` Name of the module that attempted to require(id).


Emitted when a `require()` call returns. See [`end` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#endevent).
###### Event: `'module.require.error'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-modulerequireerror)
  * `event`
    * `id` Argument passed to `require()`. Module name.
    * `parentFilename` Name of the module that attempted to require(id).
  * `error`


Emitted when a `require()` throws an error. See [`error` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#errorevent).
###### Event: `'module.import.asyncStart'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-moduleimportasyncstart)
  * `event`
    * `id` Argument passed to `import()`. Module name.
    * `parentURL` URL object of the module that attempted to import(id).


Emitted when `import()` is invoked. See [`asyncStart` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncstartevent).
###### Event: `'module.import.asyncEnd'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-moduleimportasyncend)
  * `event`
    * `id` Argument passed to `import()`. Module name.
    * `parentURL` URL object of the module that attempted to import(id).


Emitted when `import()` has completed. See [`asyncEnd` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#asyncendevent).
###### Event: `'module.import.error'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-moduleimporterror)
  * `event`
    * `id` Argument passed to `import()`. Module name.
    * `parentURL` URL object of the module that attempted to import(id).
  * `error`


Emitted when a `import()` throws an error. See [`error` event](https://nodejs.org/docs/latest/api/diagnostics_channel.html#errorevent).
##### NET[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#net)
Stability: 1 - Experimental
###### Event: `'net.client.socket'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-netclientsocket)
  * `socket` [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) | [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket)


Emitted when a new TCP or pipe client socket connection is created.
###### Event: `'net.server.socket'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-netserversocket)
  * `socket` [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)


Emitted when a new TCP or pipe connection is received.
###### Event: `'tracing:net.server.listen:asyncStart'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-tracingnetserverlistenasyncstart)
  * `server` [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)
  * `options`


Emitted when [`net.Server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) is invoked, before the port or pipe is actually setup.
###### Event: `'tracing:net.server.listen:asyncEnd'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-tracingnetserverlistenasyncend)
  * `server` [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Emitted when [`net.Server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) has completed and thus the server is ready to accept connection.
###### Event: `'tracing:net.server.listen:error'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-tracingnetserverlistenerror)
  * `server` [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)
  * `error`


Emitted when [`net.Server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) is returning an error.
##### UDP[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#udp)
Stability: 1 - Experimental
###### Event: `'udp.socket'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-udpsocket)
  * `socket` [`<dgram.Socket>`](https://nodejs.org/docs/latest/api/dgram.html#class-dgramsocket)


Emitted when a new UDP socket is created.
##### Process[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#process)
Added in: v16.18.0
Stability: 1 - Experimental
###### Event: `'child_process'`[#](https://nodejs.org/docs/latest/api/diagnostics_channel.html#event-child-process)
  * `process` [`<ChildProcess>`](https://nodejs.org/docs/latest/api/child_process.html#class-childprocess)


Emitted when a new process is created.
`tracing:child_process.spawn:start`
  * `process` [`<ChildProcess>`](https://nodejs.org/docs/latest/api/child_process.html#class-childprocess)
  * `options`


Emitted when [`child_process.spawn()`](https://nodejs.org/docs/latest/api/child_process.html#child_processspawncommand-args-options) is invoked, before the process is actually spawned.
`tracing:child_process.spawn:end`
  * `process` [`<ChildProcess>`](https://nodejs.org/docs/latest/api/child_process.html#class-childprocess)


Emitted when [`child_process.spawn()`](https://nodejs.org/docs/latest/api/child_process.html#child_processspawncommand-args-options) has completed successfully and the process has been created.
