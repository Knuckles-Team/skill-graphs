```
import { createServer } from 'node:http2';

const server = createServer();
server.on('session', (session) => {
  // Set altsvc for origin https://example.org:80
  session.altsvc('h2=":8000"', 'https://example.org:80');
});

server.on('stream', (stream) => {
  // Set altsvc for a specific stream
  stream.session.altsvc('h2=":8000"', stream.id);
});
const http2 = require('node:http2');

const server = http2.createServer();
server.on('session', (session) => {
  // Set altsvc for origin https://example.org:80
  session.altsvc('h2=":8000"', 'https://example.org:80');
});

server.on('stream', (stream) => {
  // Set altsvc for a specific stream
  stream.session.altsvc('h2=":8000"', stream.id);
});
copy
```

Sending an `ALTSVC` frame with a specific stream ID indicates that the alternate service is associated with the origin of the given `Http2Stream`.
The `alt` and origin string _must_ contain only ASCII bytes and are strictly interpreted as a sequence of ASCII bytes. The special value `'clear'` may be passed to clear any previously set alternative service for a given domain.
When a string is passed for the `originOrStream` argument, it will be parsed as a URL and the origin will be derived. For instance, the origin for the HTTP URL `'https://example.org/foo/bar'` is the ASCII string `'https://example.org'`. An error will be thrown if either the given string cannot be parsed as a URL or if a valid origin cannot be derived.
A `URL` object, or any object with an `origin` property, may be passed as `originOrStream`, in which case the value of the `origin` property will be used. The value of the `origin` property _must_ be a properly serialized ASCII origin.
##### Specifying alternative services[#](https://nodejs.org/docs/latest/api/http2.html#specifying-alternative-services)
The format of the `alt` parameter is strictly defined by
For example, the value `'h2="example.org:81"'` indicates that the HTTP/2 protocol is available on the host `'example.org'` on TCP/IP port 81. The host and port _must_ be contained within the quote (`"`) characters.
Multiple alternatives may be specified, for instance: `'h2="example.org:81", h2=":82"'`.
The protocol identifier (`'h2'` in the examples) may be any valid
The syntax of these values is not validated by the Node.js implementation and are passed through as provided by the user or received from the peer.
#####  `serverhttp2session.origin(...origins)`[#](https://nodejs.org/docs/latest/api/http2.html#serverhttp2sessionoriginorigins)
Added in: v10.12.0
  * `origins` { string | URL | Object } One or more URL Strings passed as separate arguments.


Submits an `ORIGIN` frame (as defined by
```
import { createSecureServer } from 'node:http2';
const options = getSecureOptionsSomehow();
const server = createSecureServer(options);
server.on('stream', (stream) => {
  stream.respond();
  stream.end('ok');
});
server.on('session', (session) => {
  session.origin('https://example.com', 'https://example.org');
});
const http2 = require('node:http2');
const options = getSecureOptionsSomehow();
const server = http2.createSecureServer(options);
server.on('stream', (stream) => {
  stream.respond();
  stream.end('ok');
});
server.on('session', (session) => {
  session.origin('https://example.com', 'https://example.org');
});
copy
```

When a string is passed as an `origin`, it will be parsed as a URL and the origin will be derived. For instance, the origin for the HTTP URL `'https://example.org/foo/bar'` is the ASCII string `'https://example.org'`. An error will be thrown if either the given string cannot be parsed as a URL or if a valid origin cannot be derived.
A `URL` object, or any object with an `origin` property, may be passed as an `origin`, in which case the value of the `origin` property will be used. The value of the `origin` property _must_ be a properly serialized ASCII origin.
Alternatively, the `origins` option may be used when creating a new HTTP/2 server using the `http2.createSecureServer()` method:
```
import { createSecureServer } from 'node:http2';
const options = getSecureOptionsSomehow();
options.origins = ['https://example.com', 'https://example.org'];
const server = createSecureServer(options);
server.on('stream', (stream) => {
  stream.respond();
  stream.end('ok');
});
const http2 = require('node:http2');
const options = getSecureOptionsSomehow();
options.origins = ['https://example.com', 'https://example.org'];
const server = http2.createSecureServer(options);
server.on('stream', (stream) => {
  stream.respond();
  stream.end('ok');
});
copy
```

#### Class: `ClientHttp2Session`[#](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2session)
Added in: v8.4.0
  * Extends: [`<Http2Session>`](https://nodejs.org/docs/latest/api/http2.html#class-http2session)


##### Event: `'altsvc'`[#](https://nodejs.org/docs/latest/api/http2.html#event-altsvc)
Added in: v9.4.0
  * `alt`
  * `origin`
  * `streamId`


The `'altsvc'` event is emitted whenever an `ALTSVC` frame is received by the client. The event is emitted with the `ALTSVC` value, origin, and stream ID. If no `origin` is provided in the `ALTSVC` frame, `origin` will be an empty string.
```
import { connect } from 'node:http2';
const client = connect('https://example.org');

client.on('altsvc', (alt, origin, streamId) => {
  console.log(alt);
  console.log(origin);
  console.log(streamId);
});
const http2 = require('node:http2');
const client = http2.connect('https://example.org');

client.on('altsvc', (alt, origin, streamId) => {
  console.log(alt);
  console.log(origin);
  console.log(streamId);
});
copy
```

##### Event: `'origin'`[#](https://nodejs.org/docs/latest/api/http2.html#event-origin)
Added in: v10.12.0
  * `origins`


The `'origin'` event is emitted whenever an `ORIGIN` frame is received by the client. The event is emitted with an array of `origin` strings. The `http2session.originSet` will be updated to include the received origins.
```
import { connect } from 'node:http2';
const client = connect('https://example.org');

client.on('origin', (origins) => {
  for (let n = 0; n < origins.length; n++)
    console.log(origins[n]);
});
const http2 = require('node:http2');
const client = http2.connect('https://example.org');

client.on('origin', (origins) => {
  for (let n = 0; n < origins.length; n++)
    console.log(origins[n]);
});
copy
```

The `'origin'` event is only emitted when using a secure TLS connection.
#####  `clienthttp2session.request(headers[, options])`[#](https://nodejs.org/docs/latest/api/http2.html#clienthttp2sessionrequestheaders-options)
Added in: v8.4.0History Version | Changes
---|---
v24.2.0 | The `weight` option is now ignored, setting it will trigger a runtime warning.
v24.2.0, v22.17.0 | Following the deprecation of priority signaling as of RFC 9113, `weight` option is deprecated.
v24.0.0, v22.17.0 | Allow passing headers in raw array format.
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * `options`
    * `endStream` `true` if the `Http2Stream` _writable_ side should be closed initially, such as when sending a `GET` request that should not expect a payload body.
    * `exclusive` `true` and `parent` identifies a parent Stream, the created stream is made the sole direct dependency of the parent, with all other existing dependents made a dependent of the newly created stream. **Default:** `false`.
    * `parent`
    * `waitForTrailers` `true`, the `Http2Stream` will emit the `'wantTrailers'` event after the final `DATA` frame has been sent.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) An AbortSignal that may be used to abort an ongoing request.
  * Returns: [`<ClientHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream)


For HTTP/2 Client `Http2Session` instances only, the `http2session.request()` creates and returns an `Http2Stream` instance that can be used to send an HTTP/2 request to the connected server.
When a `ClientHttp2Session` is first created, the socket may not yet be connected. if `clienthttp2session.request()` is called during this time, the actual request will be deferred until the socket is ready to go. If the `session` is closed before the actual request be executed, an `ERR_HTTP2_GOAWAY_SESSION` is thrown.
This method is only available if `http2session.type` is equal to `http2.constants.NGHTTP2_SESSION_CLIENT`.
```
import { connect, constants } from 'node:http2';
const clientSession = connect('https://localhost:1234');
const {
  HTTP2_HEADER_PATH,
  HTTP2_HEADER_STATUS,
} = constants;

const req = clientSession.request({ [HTTP2_HEADER_PATH]: '/' });
req.on('response', (headers) => {
  console.log(headers[HTTP2_HEADER_STATUS]);
  req.on('data', (chunk) => { /* .. */ });
  req.on('end', () => { /* .. */ });
});
const http2 = require('node:http2');
const clientSession = http2.connect('https://localhost:1234');
const {
  HTTP2_HEADER_PATH,
  HTTP2_HEADER_STATUS,
} = http2.constants;

const req = clientSession.request({ [HTTP2_HEADER_PATH]: '/' });
req.on('response', (headers) => {
  console.log(headers[HTTP2_HEADER_STATUS]);
  req.on('data', (chunk) => { /* .. */ });
  req.on('end', () => { /* .. */ });
});
copy
```

When the `options.waitForTrailers` option is set, the `'wantTrailers'` event is emitted immediately after queuing the last chunk of payload data to be sent. The `http2stream.sendTrailers()` method can then be called to send trailing headers to the peer.
When `options.waitForTrailers` is set, the `Http2Stream` will not automatically close when the final `DATA` frame is transmitted. User code must call either `http2stream.sendTrailers()` or `http2stream.close()` to close the `Http2Stream`.
When `options.signal` is set with an `AbortSignal` and then `abort` on the corresponding `AbortController` is called, the request will emit an `'error'` event with an `AbortError` error.
The `:method` and `:path` pseudo-headers are not specified within `headers`, they respectively default to:
  * `:method` = `'GET'`
  * `:path` = `/`


#### Class: `Http2Stream`[#](https://nodejs.org/docs/latest/api/http2.html#class-http2stream)
Added in: v8.4.0
  * Extends: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


Each instance of the `Http2Stream` class represents a bidirectional HTTP/2 communications stream over an `Http2Session` instance. Any single `Http2Session` may have up to 231-1 `Http2Stream` instances over its lifetime.
User code will not construct `Http2Stream` instances directly. Rather, these are created, managed, and provided to user code through the `Http2Session` instance. On the server, `Http2Stream` instances are created either in response to an incoming HTTP request (and handed off to user code via the `'stream'` event), or in response to a call to the `http2stream.pushStream()` method. On the client, `Http2Stream` instances are created and returned when either the `http2session.request()` method is called, or in response to an incoming `'push'` event.
The `Http2Stream` class is a base for the [`ServerHttp2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2stream) and [`ClientHttp2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream) classes, each of which is used specifically by either the Server or Client side, respectively.
All `Http2Stream` instances are [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) streams. The `Writable` side of the `Duplex` is used to send data to the connected peer, while the `Readable` side is used to receive data sent by the connected peer.
The default text character encoding for an `Http2Stream` is UTF-8. When using an `Http2Stream` to send text, use the `'content-type'` header to set the character encoding.
```
stream.respond({
  'content-type': 'text/html; charset=utf-8',
  ':status': 200,
});
copy
```

#####  `Http2Stream` Lifecycle[#](https://nodejs.org/docs/latest/api/http2.html#http2stream-lifecycle)
###### Creation[#](https://nodejs.org/docs/latest/api/http2.html#creation)
On the server side, instances of [`ServerHttp2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2stream) are created either when:
  * A new HTTP/2 `HEADERS` frame with a previously unused stream ID is received;
  * The `http2stream.pushStream()` method is called.


On the client side, instances of [`ClientHttp2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream) are created when the `http2session.request()` method is called.
On the client, the `Http2Stream` instance returned by `http2session.request()` may not be immediately ready for use if the parent `Http2Session` has not yet been fully established. In such cases, operations called on the `Http2Stream` will be buffered until the `'ready'` event is emitted. User code should rarely, if ever, need to handle the `'ready'` event directly. The ready status of an `Http2Stream` can be determined by checking the value of `http2stream.id`. If the value is `undefined`, the stream is not yet ready for use.
###### Destruction[#](https://nodejs.org/docs/latest/api/http2.html#destruction)
All [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) instances are destroyed either when:
  * An `RST_STREAM` frame for the stream is received by the connected peer, and (for client streams only) pending data has been read.
  * The `http2stream.close()` method is called, and (for client streams only) pending data has been read.
  * The `http2stream.destroy()` or `http2session.destroy()` methods are called.


When an `Http2Stream` instance is destroyed, an attempt will be made to send an `RST_STREAM` frame to the connected peer.
When the `Http2Stream` instance is destroyed, the `'close'` event will be emitted. Because `Http2Stream` is an instance of `stream.Duplex`, the `'end'` event will also be emitted if the stream data is currently flowing. The `'error'` event may also be emitted if `http2stream.destroy()` was called with an `Error` passed as the first argument.
After the `Http2Stream` has been destroyed, the `http2stream.destroyed` property will be `true` and the `http2stream.rstCode` property will specify the `RST_STREAM` error code. The `Http2Stream` instance is no longer usable once destroyed.
##### Event: `'aborted'`[#](https://nodejs.org/docs/latest/api/http2.html#event-aborted)
Added in: v8.4.0
The `'aborted'` event is emitted whenever a `Http2Stream` instance is abnormally aborted in mid-communication. Its listener does not expect any arguments.
The `'aborted'` event will only be emitted if the `Http2Stream` writable side has not been ended.
##### Event: `'close'`[#](https://nodejs.org/docs/latest/api/http2.html#event-close-1)
Added in: v8.4.0
The `'close'` event is emitted when the `Http2Stream` is destroyed. Once this event is emitted, the `Http2Stream` instance is no longer usable.
The HTTP/2 error code used when closing the stream can be retrieved using the `http2stream.rstCode` property. If the code is any value other than `NGHTTP2_NO_ERROR` (`0`), an `'error'` event will have also been emitted.
##### Event: `'error'`[#](https://nodejs.org/docs/latest/api/http2.html#event-error-1)
Added in: v8.4.0
  * `error`


The `'error'` event is emitted when an error occurs during the processing of an `Http2Stream`.
##### Event: `'frameError'`[#](https://nodejs.org/docs/latest/api/http2.html#event-frameerror-1)
Added in: v8.4.0
  * `type`
  * `code`
  * `id` `0` if the frame isn't associated with a stream).


The `'frameError'` event is emitted when an error occurs while attempting to send a frame. When invoked, the handler function will receive an integer argument identifying the frame type, and an integer argument identifying the error code. The `Http2Stream` instance will be destroyed immediately after the `'frameError'` event is emitted.
##### Event: `'ready'`[#](https://nodejs.org/docs/latest/api/http2.html#event-ready)
Added in: v8.4.0
The `'ready'` event is emitted when the `Http2Stream` has been opened, has been assigned an `id`, and can be used. The listener does not expect any arguments.
##### Event: `'timeout'`[#](https://nodejs.org/docs/latest/api/http2.html#event-timeout-1)
Added in: v8.4.0
The `'timeout'` event is emitted after no activity is received for this `Http2Stream` within the number of milliseconds set using `http2stream.setTimeout()`. Its listener does not expect any arguments.
##### Event: `'trailers'`[#](https://nodejs.org/docs/latest/api/http2.html#event-trailers)
Added in: v8.4.0
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object) An object describing the headers
  * `flags`


The `'trailers'` event is emitted when a block of headers associated with trailing header fields is received. The listener callback is passed the [HTTP/2 Headers Object](https://nodejs.org/docs/latest/api/http2.html#headers-object) and flags associated with the headers.
This event might not be emitted if `http2stream.end()` is called before trailers are received and the incoming data is not being read or listened for.
```
stream.on('trailers', (headers, flags) => {
  console.log(headers);
});
copy
```

##### Event: `'wantTrailers'`[#](https://nodejs.org/docs/latest/api/http2.html#event-wanttrailers)
Added in: v10.0.0
The `'wantTrailers'` event is emitted when the `Http2Stream` has queued the final `DATA` frame to be sent on a frame and the `Http2Stream` is ready to send trailing headers. When initiating a request or response, the `waitForTrailers` option must be set for this event to be emitted.
#####  `http2stream.aborted`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamaborted)
Added in: v8.4.0
  * Type:


Set to `true` if the `Http2Stream` instance was aborted abnormally. When set, the `'aborted'` event will have been emitted.
#####  `http2stream.bufferSize`[#](https://nodejs.org/docs/latest/api/http2.html#http2streambuffersize)
Added in: v11.2.0, v10.16.0
  * Type:


This property shows the number of characters currently buffered to be written. See [`net.Socket.bufferSize`](https://nodejs.org/docs/latest/api/net.html#socketbuffersize) for details.
#####  `http2stream.close(code[, callback])`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamclosecode-callback)
Added in: v8.4.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `code` **Default:** `http2.constants.NGHTTP2_NO_ERROR` (`0x00`).
  * `callback` `'close'` event.


Closes the `Http2Stream` instance by sending an `RST_STREAM` frame to the connected HTTP/2 peer.
#####  `http2stream.closed`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamclosed)
Added in: v9.4.0
  * Type:


Set to `true` if the `Http2Stream` instance has been closed.
#####  `http2stream.destroyed`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamdestroyed)
Added in: v8.4.0
  * Type:


Set to `true` if the `Http2Stream` instance has been destroyed and is no longer usable.
#####  `http2stream.endAfterHeaders`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamendafterheaders)
Added in: v10.11.0
  * Type:


Set to `true` if the `END_STREAM` flag was set in the request or response HEADERS frame received, indicating that no additional data should be received and the readable side of the `Http2Stream` will be closed.
#####  `http2stream.id`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamid)
Added in: v8.4.0
  * Type:


The numeric stream identifier of this `Http2Stream` instance. Set to `undefined` if the stream identifier has not yet been assigned.
#####  `http2stream.pending`[#](https://nodejs.org/docs/latest/api/http2.html#http2streampending)
Added in: v9.4.0
  * Type:


Set to `true` if the `Http2Stream` instance has not yet been assigned a numeric stream identifier.
#####  `http2stream.priority(options)`[#](https://nodejs.org/docs/latest/api/http2.html#http2streampriorityoptions)
Added in: v8.4.0Deprecated in: v24.2.0, v22.17.0History Version | Changes
---|---
v24.2.0 | This method no longer sets the priority of the stream. Using it now triggers a runtime warning.
Stability: 0 - Deprecated: support for priority signaling has been deprecated in the
Empty method, only there to maintain some backward compatibility.
#####  `http2stream.rstCode`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamrstcode)
Added in: v8.4.0
  * Type:


Set to the `RST_STREAM` [error code](https://nodejs.org/docs/latest/api/http2.html#error-codes-for-rst_stream-and-goaway) reported when the `Http2Stream` is destroyed after either receiving an `RST_STREAM` frame from the connected peer, calling `http2stream.close()`, or `http2stream.destroy()`. Will be `undefined` if the `Http2Stream` has not been closed.
#####  `http2stream.sentHeaders`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamsentheaders)
Added in: v9.5.0
  * Type: [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)


An object containing the outbound headers sent for this `Http2Stream`.
#####  `http2stream.sentInfoHeaders`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamsentinfoheaders)
Added in: v9.5.0
  * Type: [`<HTTP/2 Headers Object[]>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)


An array of objects containing the outbound informational (additional) headers sent for this `Http2Stream`.
#####  `http2stream.sentTrailers`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamsenttrailers)
Added in: v9.5.0
  * Type: [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)


An object containing the outbound trailers sent for this `HttpStream`.
#####  `http2stream.session`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamsession)
Added in: v8.4.0
  * Type: [`<Http2Session>`](https://nodejs.org/docs/latest/api/http2.html#class-http2session)


A reference to the `Http2Session` instance that owns this `Http2Stream`. The value will be `undefined` after the `Http2Stream` instance is destroyed.
#####  `http2stream.setTimeout(msecs, callback)`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamsettimeoutmsecs-callback)
Added in: v8.4.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `msecs`
  * `callback`

```
import { connect, constants } from 'node:http2';
const client = connect('http://example.org:8000');
const { NGHTTP2_CANCEL } = constants;
const req = client.request({ ':path': '/' });

// Cancel the stream if there's no activity after 5 seconds
req.setTimeout(5000, () => req.close(NGHTTP2_CANCEL));
const http2 = require('node:http2');
const client = http2.connect('http://example.org:8000');
const { NGHTTP2_CANCEL } = http2.constants;
const req = client.request({ ':path': '/' });

// Cancel the stream if there's no activity after 5 seconds
req.setTimeout(5000, () => req.close(NGHTTP2_CANCEL));
copy
```

#####  `http2stream.state`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamstate)
Added in: v8.4.0History Version | Changes
---|---
v24.2.0 | The `state.weight` property is now always set to 16 and `sumDependencyWeight` is always set to 0.
v24.2.0, v22.17.0 | Following the deprecation of priority signaling as of RFC 9113, `weight` and `sumDependencyWeight` options are deprecated.
Provides miscellaneous information about the current state of the `Http2Stream`.
  * Type:
    * `localWindowSize` `Http2Stream` without receiving a `WINDOW_UPDATE`.
    * `state` `Http2Stream` as determined by `nghttp2`.
    * `localClose` `1` if this `Http2Stream` has been closed locally.
    * `remoteClose` `1` if this `Http2Stream` has been closed remotely.
    * `sumDependencyWeight` `0`.
    * `weight` `16`.


A current state of this `Http2Stream`.
#####  `http2stream.sendTrailers(headers)`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamsendtrailersheaders)
Added in: v10.0.0
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)


Sends a trailing `HEADERS` frame to the connected HTTP/2 peer. This method will cause the `Http2Stream` to be immediately closed and must only be called after the `'wantTrailers'` event has been emitted. When sending a request or sending a response, the `options.waitForTrailers` option must be set in order to keep the `Http2Stream` open after the final `DATA` frame so that trailers can be sent.
```
import { createServer } from 'node:http2';
const server = createServer();
server.on('stream', (stream) => {
  stream.respond(undefined, { waitForTrailers: true });
  stream.on('wantTrailers', () => {
    stream.sendTrailers({ xyz: 'abc' });
  });
  stream.end('Hello World');
});
const http2 = require('node:http2');
const server = http2.createServer();
server.on('stream', (stream) => {
  stream.respond(undefined, { waitForTrailers: true });
  stream.on('wantTrailers', () => {
    stream.sendTrailers({ xyz: 'abc' });
  });
  stream.end('Hello World');
});
copy
```

The HTTP/1 specification forbids trailers from containing HTTP/2 pseudo-header fields (e.g. `':method'`, `':path'`, etc).
#### Class: `ClientHttp2Stream`[#](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2stream)
Added in: v8.4.0
  * Extends [`<Http2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream)
