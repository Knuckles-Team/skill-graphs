## HTTP/2[#](https://nodejs.org/docs/latest/api/http2.html#http2)
**Source Code:** Added in: v8.4.0History Version | Changes
---|---
v15.3.0, v14.17.0 | It is possible to abort a request with an AbortSignal.
v15.0.0 | Requests with the `host` header (with or without `:authority`) can now be sent/received.
v10.10.0 | HTTP/2 is now Stable. Previously, it had been Experimental.
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:http2` module provides an implementation of the
```
const http2 = require('node:http2');
copy
```

### Determining if crypto support is unavailable[#](https://nodejs.org/docs/latest/api/http2.html#determining-if-crypto-support-is-unavailable)
It is possible for Node.js to be built without including support for the `node:crypto` module. In such cases, attempting to `import` from `node:http2` or calling `require('node:http2')` will result in an error being thrown.
When using CommonJS, the error thrown can be caught using try/catch:
```
let http2;
try {
  http2 = require('node:http2');
} catch (err) {
  console.error('http2 support is disabled!');
}
copy
```

When using the lexical ESM `import` keyword, the error can only be caught if a handler for `process.on('uncaughtException')` is registered _before_ any attempt to load the module is made (using, for instance, a preload module).
When using ESM, if there is a chance that the code may be run on a build of Node.js where crypto support is not enabled, consider using the `import` keyword:
```
let http2;
try {
  http2 = await import('node:http2');
} catch (err) {
  console.error('http2 support is disabled!');
}
copy
```

### Core API[#](https://nodejs.org/docs/latest/api/http2.html#core-api)
The Core API provides a low-level interface designed specifically around support for HTTP/2 protocol features. It is specifically _not_ designed for compatibility with the existing [HTTP/1](https://nodejs.org/docs/latest/api/http.html) module API. However, the [Compatibility API](https://nodejs.org/docs/latest/api/http2.html#compatibility-api) is.
The `http2` Core API is much more symmetric between client and server than the `http` API. For instance, most events, like `'error'`, `'connect'` and `'stream'`, can be emitted either by client-side code or server-side code.
#### Server-side example[#](https://nodejs.org/docs/latest/api/http2.html#server-side-example)
The following illustrates a simple HTTP/2 server using the Core API. Since there are no browsers known that support [`http2.createSecureServer()`](https://nodejs.org/docs/latest/api/http2.html#http2createsecureserveroptions-onrequesthandler) is necessary when communicating with browser clients.
```
import { createSecureServer } from 'node:http2';
import { readFileSync } from 'node:fs';

const server = createSecureServer({
  key: readFileSync('localhost-privkey.pem'),
  cert: readFileSync('localhost-cert.pem'),
});

server.on('error', (err) => console.error(err));

server.on('stream', (stream, headers) => {
  // stream is a Duplex
  stream.respond({
    'content-type': 'text/html; charset=utf-8',
    ':status': 200,
  });
  stream.end('<h1>Hello World</h1>');
});

server.listen(8443);
const http2 = require('node:http2');
const fs = require('node:fs');

const server = http2.createSecureServer({
  key: fs.readFileSync('localhost-privkey.pem'),
  cert: fs.readFileSync('localhost-cert.pem'),
});
server.on('error', (err) => console.error(err));

server.on('stream', (stream, headers) => {
  // stream is a Duplex
  stream.respond({
    'content-type': 'text/html; charset=utf-8',
    ':status': 200,
  });
  stream.end('<h1>Hello World</h1>');
});

server.listen(8443);
copy
```

To generate the certificate and key for this example, run:
```
openssl req -x509 -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost' \
  -keyout localhost-privkey.pem -out localhost-cert.pem
copy
```

#### Client-side example[#](https://nodejs.org/docs/latest/api/http2.html#client-side-example)
The following illustrates an HTTP/2 client:
```
import { connect } from 'node:http2';
import { readFileSync } from 'node:fs';

const client = connect('https://localhost:8443', {
  ca: readFileSync('localhost-cert.pem'),
});
client.on('error', (err) => console.error(err));

const req = client.request({ ':path': '/' });

req.on('response', (headers, flags) => {
  for (const name in headers) {
    console.log(`${name}: ${headers[name]}`);
  }
});

req.setEncoding('utf8');
let data = '';
req.on('data', (chunk) => { data += chunk; });
req.on('end', () => {
  console.log(`\n${data}`);
  client.close();
});
req.end();
const http2 = require('node:http2');
const fs = require('node:fs');

const client = http2.connect('https://localhost:8443', {
  ca: fs.readFileSync('localhost-cert.pem'),
});
client.on('error', (err) => console.error(err));

const req = client.request({ ':path': '/' });

req.on('response', (headers, flags) => {
  for (const name in headers) {
    console.log(`${name}: ${headers[name]}`);
  }
});

req.setEncoding('utf8');
let data = '';
req.on('data', (chunk) => { data += chunk; });
req.on('end', () => {
  console.log(`\n${data}`);
  client.close();
});
req.end();
copy
```

#### Class: `Http2Session`[#](https://nodejs.org/docs/latest/api/http2.html#class-http2session)
Added in: v8.4.0
  * Extends: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


Instances of the `http2.Http2Session` class represent an active communications session between an HTTP/2 client and server. Instances of this class are _not_ intended to be constructed directly by user code.
Each `Http2Session` instance will exhibit slightly different behaviors depending on whether it is operating as a server or a client. The `http2session.type` property can be used to determine the mode in which an `Http2Session` is operating. On the server side, user code should rarely have occasion to work with the `Http2Session` object directly, with most actions typically taken through interactions with either the `Http2Server` or `Http2Stream` objects.
User code will not create `Http2Session` instances directly. Server-side `Http2Session` instances are created by the `Http2Server` instance when a new HTTP/2 connection is received. Client-side `Http2Session` instances are created using the `http2.connect()` method.
#####  `Http2Session` and sockets[#](https://nodejs.org/docs/latest/api/http2.html#http2session-and-sockets)
Every `Http2Session` instance is associated with exactly one [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) or [`tls.TLSSocket`](https://nodejs.org/docs/latest/api/tls.html#class-tlstlssocket) when it is created. When either the `Socket` or the `Http2Session` are destroyed, both will be destroyed.
Because of the specific serialization and processing requirements imposed by the HTTP/2 protocol, it is not recommended for user code to read data from or write data to a `Socket` instance bound to a `Http2Session`. Doing so can put the HTTP/2 session into an indeterminate state causing the session and the socket to become unusable.
Once a `Socket` has been bound to an `Http2Session`, user code should rely solely on the API of the `Http2Session`.
##### Event: `'close'`[#](https://nodejs.org/docs/latest/api/http2.html#event-close)
Added in: v8.4.0
The `'close'` event is emitted once the `Http2Session` has been destroyed. Its listener does not expect any arguments.
##### Event: `'connect'`[#](https://nodejs.org/docs/latest/api/http2.html#event-connect)
Added in: v8.4.0
  * `session` [`<Http2Session>`](https://nodejs.org/docs/latest/api/http2.html#class-http2session)
  * `socket` [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)


The `'connect'` event is emitted once the `Http2Session` has been successfully connected to the remote peer and communication may begin.
User code will typically not listen for this event directly.
##### Event: `'error'`[#](https://nodejs.org/docs/latest/api/http2.html#event-error)
Added in: v8.4.0
  * `error`


The `'error'` event is emitted when an error occurs during the processing of an `Http2Session`.
##### Event: `'frameError'`[#](https://nodejs.org/docs/latest/api/http2.html#event-frameerror)
Added in: v8.4.0
  * `type`
  * `code`
  * `id` `0` if the frame isn't associated with a stream).


The `'frameError'` event is emitted when an error occurs while attempting to send a frame on the session. If the frame that could not be sent is associated with a specific `Http2Stream`, an attempt to emit a `'frameError'` event on the `Http2Stream` is made.
If the `'frameError'` event is associated with a stream, the stream will be closed and destroyed immediately following the `'frameError'` event. If the event is not associated with a stream, the `Http2Session` will be shut down immediately following the `'frameError'` event.
##### Event: `'goaway'`[#](https://nodejs.org/docs/latest/api/http2.html#event-goaway)
Added in: v8.4.0
  * `errorCode` `GOAWAY` frame.
  * `lastStreamID` `0` if no ID is specified).
  * `opaqueData` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) If additional opaque data was included in the `GOAWAY` frame, a `Buffer` instance will be passed containing that data.


The `'goaway'` event is emitted when a `GOAWAY` frame is received.
The `Http2Session` instance will be shut down automatically when the `'goaway'` event is emitted.
##### Event: `'localSettings'`[#](https://nodejs.org/docs/latest/api/http2.html#event-localsettings)
Added in: v8.4.0
  * `settings` [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object) A copy of the `SETTINGS` frame received.


The `'localSettings'` event is emitted when an acknowledgment `SETTINGS` frame has been received.
When using `http2session.settings()` to submit new settings, the modified settings do not take effect until the `'localSettings'` event is emitted.
```
session.settings({ enablePush: false });

session.on('localSettings', (settings) => {
  /* Use the new settings */
});
copy
```

##### Event: `'ping'`[#](https://nodejs.org/docs/latest/api/http2.html#event-ping)
Added in: v10.12.0
  * `payload` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The `PING` frame 8-byte payload


The `'ping'` event is emitted whenever a `PING` frame is received from the connected peer.
##### Event: `'remoteSettings'`[#](https://nodejs.org/docs/latest/api/http2.html#event-remotesettings)
Added in: v8.4.0
  * `settings` [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object) A copy of the `SETTINGS` frame received.


The `'remoteSettings'` event is emitted when a new `SETTINGS` frame is received from the connected peer.
```
session.on('remoteSettings', (settings) => {
  /* Use the new settings */
});
copy
```

##### Event: `'stream'`[#](https://nodejs.org/docs/latest/api/http2.html#event-stream)
Added in: v8.4.0
  * `stream` [`<Http2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) A reference to the stream
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object) An object describing the headers
  * `flags`
  * `rawHeaders` {HTTP/2 Raw Headers} An array containing the raw headers


The `'stream'` event is emitted when a new `Http2Stream` is created.
```
session.on('stream', (stream, headers, flags) => {
  const method = headers[':method'];
  const path = headers[':path'];
  // ...
  stream.respond({
    ':status': 200,
    'content-type': 'text/plain; charset=utf-8',
  });
  stream.write('hello ');
  stream.end('world');
});
copy
```

On the server side, user code will typically not listen for this event directly, and would instead register a handler for the `'stream'` event emitted by the `net.Server` or `tls.Server` instances returned by `http2.createServer()` and `http2.createSecureServer()`, respectively, as in the example below:
```
import { createServer } from 'node:http2';

// Create an unencrypted HTTP/2 server
const server = createServer();

server.on('stream', (stream, headers) => {
  stream.respond({
    'content-type': 'text/html; charset=utf-8',
    ':status': 200,
  });
  stream.on('error', (error) => console.error(error));
  stream.end('<h1>Hello World</h1>');
});

server.listen(8000);
const http2 = require('node:http2');

// Create an unencrypted HTTP/2 server
const server = http2.createServer();

server.on('stream', (stream, headers) => {
  stream.respond({
    'content-type': 'text/html; charset=utf-8',
    ':status': 200,
  });
  stream.on('error', (error) => console.error(error));
  stream.end('<h1>Hello World</h1>');
});

server.listen(8000);
copy
```

Even though HTTP/2 streams and network sockets are not in a 1:1 correspondence, a network error will destroy each individual stream and must be handled on the stream level, as shown above.
##### Event: `'timeout'`[#](https://nodejs.org/docs/latest/api/http2.html#event-timeout)
Added in: v8.4.0
After the `http2session.setTimeout()` method is used to set the timeout period for this `Http2Session`, the `'timeout'` event is emitted if there is no activity on the `Http2Session` after the configured number of milliseconds. Its listener does not expect any arguments.
```
session.setTimeout(2000);
session.on('timeout', () => { /* .. */ });
copy
```

#####  `http2session.alpnProtocol`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionalpnprotocol)
Added in: v9.4.0
  * Type:


Value will be `undefined` if the `Http2Session` is not yet connected to a socket, `h2c` if the `Http2Session` is not connected to a `TLSSocket`, or will return the value of the connected `TLSSocket`'s own `alpnProtocol` property.
#####  `http2session.close([callback])`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionclosecallback)
Added in: v9.4.0
  * `callback`


Gracefully closes the `Http2Session`, allowing any existing streams to complete on their own and preventing new `Http2Stream` instances from being created. Once closed, `http2session.destroy()` _might_ be called if there are no open `Http2Stream` instances.
If specified, the `callback` function is registered as a handler for the `'close'` event.
#####  `http2session.closed`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionclosed)
Added in: v9.4.0
  * Type:


Will be `true` if this `Http2Session` instance has been closed, otherwise `false`.
#####  `http2session.connecting`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionconnecting)
Added in: v10.0.0
  * Type:


Will be `true` if this `Http2Session` instance is still connecting, will be set to `false` before emitting `connect` event and/or calling the `http2.connect` callback.
#####  `http2session.destroy([error][, code])`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessiondestroyerror-code)
Added in: v8.4.0
  * `error` `Error` object if the `Http2Session` is being destroyed due to an error.
  * `code` `GOAWAY` frame. If unspecified, and `error` is not undefined, the default is `INTERNAL_ERROR`, otherwise defaults to `NO_ERROR`.


Immediately terminates the `Http2Session` and the associated `net.Socket` or `tls.TLSSocket`.
Once destroyed, the `Http2Session` will emit the `'close'` event. If `error` is not undefined, an `'error'` event will be emitted immediately before the `'close'` event.
If there are any remaining open `Http2Streams` associated with the `Http2Session`, those will also be destroyed.
#####  `http2session.destroyed`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessiondestroyed)
Added in: v8.4.0
  * Type:


Will be `true` if this `Http2Session` instance has been destroyed and must no longer be used, otherwise `false`.
#####  `http2session.encrypted`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionencrypted)
Added in: v9.4.0
  * Type:


Value is `undefined` if the `Http2Session` session socket has not yet been connected, `true` if the `Http2Session` is connected with a `TLSSocket`, and `false` if the `Http2Session` is connected to any other kind of socket or stream.
#####  `http2session.goaway([code[, lastStreamID[, opaqueData]]])`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessiongoawaycode-laststreamid-opaquedata)
Added in: v9.4.0
  * `code`
  * `lastStreamID` `Http2Stream`
  * `opaqueData` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `TypedArray` or `DataView` instance containing additional data to be carried within the `GOAWAY` frame.


Transmits a `GOAWAY` frame to the connected peer _without_ shutting down the `Http2Session`.
#####  `http2session.localSettings`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionlocalsettings)
Added in: v8.4.0
  * Type: [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object)


A prototype-less object describing the current local settings of this `Http2Session`. The local settings are local to _this_ `Http2Session` instance.
#####  `http2session.originSet`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionoriginset)
Added in: v9.4.0
  * Type:


If the `Http2Session` is connected to a `TLSSocket`, the `originSet` property will return an `Array` of origins for which the `Http2Session` may be considered authoritative.
The `originSet` property is only available when using a secure TLS connection.
#####  `http2session.pendingSettingsAck`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionpendingsettingsack)
Added in: v8.4.0
  * Type:


Indicates whether the `Http2Session` is currently waiting for acknowledgment of a sent `SETTINGS` frame. Will be `true` after calling the `http2session.settings()` method. Will be `false` once all sent `SETTINGS` frames have been acknowledged.
#####  `http2session.ping([payload, ]callback)`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionpingpayload-callback)
Added in: v8.9.3History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `payload` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `callback`
  * Returns:


Sends a `PING` frame to the connected HTTP/2 peer. A `callback` function must be provided. The method will return `true` if the `PING` was sent, `false` otherwise.
The maximum number of outstanding (unacknowledged) pings is determined by the `maxOutstandingPings` configuration option. The default maximum is 10.
If provided, the `payload` must be a `Buffer`, `TypedArray`, or `DataView` containing 8 bytes of data that will be transmitted with the `PING` and returned with the ping acknowledgment.
The callback will be invoked with three arguments: an error argument that will be `null` if the `PING` was successfully acknowledged, a `duration` argument that reports the number of milliseconds elapsed since the ping was sent and the acknowledgment was received, and a `Buffer` containing the 8-byte `PING` payload.
```
session.ping(Buffer.from('abcdefgh'), (err, duration, payload) => {
  if (!err) {
    console.log(`Ping acknowledged in ${duration} milliseconds`);
    console.log(`With payload '${payload.toString()}'`);
  }
});
copy
```

If the `payload` argument is not specified, the default payload will be the 64-bit timestamp (little endian) marking the start of the `PING` duration.
#####  `http2session.ref()`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionref)
Added in: v9.4.0
Calls [`ref()`](https://nodejs.org/docs/latest/api/net.html#socketref) on this `Http2Session` instance's underlying [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
#####  `http2session.remoteSettings`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionremotesettings)
Added in: v8.4.0
  * Type: [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object)


A prototype-less object describing the current remote settings of this `Http2Session`. The remote settings are set by the _connected_ HTTP/2 peer.
#####  `http2session.setLocalWindowSize(windowSize)`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionsetlocalwindowsizewindowsize)
Added in: v15.3.0, v14.18.0
  * `windowSize`


Sets the local endpoint's window size. The `windowSize` is the total window size to set, not the delta.
```
import { createServer } from 'node:http2';

const server = createServer();
const expectedWindowSize = 2 ** 20;
server.on('session', (session) => {

  // Set local window size to be 2 ** 20
  session.setLocalWindowSize(expectedWindowSize);
});
const http2 = require('node:http2');

const server = http2.createServer();
const expectedWindowSize = 2 ** 20;
server.on('session', (session) => {

  // Set local window size to be 2 ** 20
  session.setLocalWindowSize(expectedWindowSize);
});
copy
```

For http2 clients the proper event is either `'connect'` or `'remoteSettings'`.
#####  `http2session.setTimeout(msecs, callback)`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionsettimeoutmsecs-callback)
Added in: v8.4.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `msecs`
  * `callback`


Used to set a callback function that is called when there is no activity on the `Http2Session` after `msecs` milliseconds. The given `callback` is registered as a listener on the `'timeout'` event.
#####  `http2session.socket`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionsocket)
Added in: v8.4.0
  * Type: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) | [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket)


Returns a `Proxy` object that acts as a `net.Socket` (or `tls.TLSSocket`) but limits available methods to ones safe to use with HTTP/2.
`destroy`, `emit`, `end`, `pause`, `read`, `resume`, and `write` will throw an error with code `ERR_HTTP2_NO_SOCKET_MANIPULATION`. See [`Http2Session` and Sockets](https://nodejs.org/docs/latest/api/http2.html#http2session-and-sockets) for more information.
`setTimeout` method will be called on this `Http2Session`.
All other interactions will be routed directly to the socket.
#####  `http2session.state`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionstate)
Added in: v8.4.0
Provides miscellaneous information about the current state of the `Http2Session`.
  * Type:
    * `effectiveLocalWindowSize` `Http2Session`.
    * `effectiveRecvDataLength` `WINDOW_UPDATE`.
    * `nextStreamID` `Http2Stream` is created by this `Http2Session`.
    * `localWindowSize` `WINDOW_UPDATE`.
    * `lastProcStreamID` `Http2Stream` for which a `HEADERS` or `DATA` frame was most recently received.
    * `remoteWindowSize` `Http2Session` may send without receiving a `WINDOW_UPDATE`.
    * `outboundQueueSize` `Http2Session`.
    * `deflateDynamicTableSize`
    * `inflateDynamicTableSize`


An object describing the current status of this `Http2Session`.
#####  `http2session.settings([settings][, callback])`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionsettingssettings-callback)
Added in: v8.4.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `settings` [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object)
  * `callback`
    * `err`
    * `settings` [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object) The updated `settings` object.
    * `duration`


Updates the current local settings for this `Http2Session` and sends a new `SETTINGS` frame to the connected HTTP/2 peer.
Once called, the `http2session.pendingSettingsAck` property will be `true` while the session is waiting for the remote peer to acknowledge the new settings.
The new settings will not become effective until the `SETTINGS` acknowledgment is received and the `'localSettings'` event is emitted. It is possible to send multiple `SETTINGS` frames while acknowledgment is still pending.
#####  `http2session.type`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessiontype)
Added in: v8.4.0
  * Type:


The `http2session.type` will be equal to `http2.constants.NGHTTP2_SESSION_SERVER` if this `Http2Session` instance is a server, and `http2.constants.NGHTTP2_SESSION_CLIENT` if the instance is a client.
#####  `http2session.unref()`[#](https://nodejs.org/docs/latest/api/http2.html#http2sessionunref)
Added in: v9.4.0
Calls [`unref()`](https://nodejs.org/docs/latest/api/net.html#socketunref) on this `Http2Session` instance's underlying [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
#### Class: `ServerHttp2Session`[#](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2session)
Added in: v8.4.0
  * Extends: [`<Http2Session>`](https://nodejs.org/docs/latest/api/http2.html#class-http2session)


#####  `serverhttp2session.altsvc(alt, originOrStream)`[#](https://nodejs.org/docs/latest/api/http2.html#serverhttp2sessionaltsvcalt-originorstream)
Added in: v9.4.0
  * `alt`
  * `originOrStream` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) | `Object` with an `origin` property) or the numeric identifier of an active `Http2Stream` as given by the `http2stream.id` property.


Submits an `ALTSVC` frame (as defined by
