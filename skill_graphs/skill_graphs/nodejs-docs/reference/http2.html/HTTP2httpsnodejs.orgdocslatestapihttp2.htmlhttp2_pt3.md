

The `ClientHttp2Stream` class is an extension of `Http2Stream` that is used exclusively on HTTP/2 Clients. `Http2Stream` instances on the client provide events such as `'response'` and `'push'` that are only relevant on the client.
##### Event: `'continue'`[#](https://nodejs.org/docs/latest/api/http2.html#event-continue)
Added in: v8.5.0
Emitted when the server sends a `100 Continue` status, usually because the request contained `Expect: 100-continue`. This is an instruction that the client should send the request body.
##### Event: `'headers'`[#](https://nodejs.org/docs/latest/api/http2.html#event-headers)
Added in: v8.4.0
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * `flags`
  * `rawHeaders` {HTTP/2 Raw Headers}


The `'headers'` event is emitted when an additional block of headers is received for a stream, such as when a block of `1xx` informational headers is received. The listener callback is passed the [HTTP/2 Headers Object](https://nodejs.org/docs/latest/api/http2.html#headers-object), flags associated with the headers, and the headers in raw format (see [HTTP/2 Raw Headers](https://nodejs.org/docs/latest/api/http2.html#raw-headers)).
```
stream.on('headers', (headers, flags) => {
  console.log(headers);
});
copy
```

##### Event: `'push'`[#](https://nodejs.org/docs/latest/api/http2.html#event-push)
Added in: v8.4.0
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * `flags`


The `'push'` event is emitted when response headers for a Server Push stream are received. The listener callback is passed the [HTTP/2 Headers Object](https://nodejs.org/docs/latest/api/http2.html#headers-object) and flags associated with the headers.
```
stream.on('push', (headers, flags) => {
  console.log(headers);
});
copy
```

##### Event: `'response'`[#](https://nodejs.org/docs/latest/api/http2.html#event-response)
Added in: v8.4.0
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * `flags`
  * `rawHeaders` {HTTP/2 Raw Headers}


The `'response'` event is emitted when a response `HEADERS` frame has been received for this stream from the connected HTTP/2 server. The listener is invoked with three arguments: an `Object` containing the received [HTTP/2 Headers Object](https://nodejs.org/docs/latest/api/http2.html#headers-object), flags associated with the headers, and the headers in raw format (see [HTTP/2 Raw Headers](https://nodejs.org/docs/latest/api/http2.html#raw-headers)).
```
import { connect } from 'node:http2';
const client = connect('https://localhost');
const req = client.request({ ':path': '/' });
req.on('response', (headers, flags) => {
  console.log(headers[':status']);
});
const http2 = require('node:http2');
const client = http2.connect('https://localhost');
const req = client.request({ ':path': '/' });
req.on('response', (headers, flags) => {
  console.log(headers[':status']);
});
copy
```

#### Class: `ServerHttp2Stream`[#](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2stream)
Added in: v8.4.0
  * Extends: [`<Http2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream)


The `ServerHttp2Stream` class is an extension of [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) that is used exclusively on HTTP/2 Servers. `Http2Stream` instances on the server provide additional methods such as `http2stream.pushStream()` and `http2stream.respond()` that are only relevant on the server.
#####  `http2stream.additionalHeaders(headers)`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamadditionalheadersheaders)
Added in: v8.4.0
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)


Sends an additional informational `HEADERS` frame to the connected HTTP/2 peer.
#####  `http2stream.headersSent`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamheaderssent)
Added in: v8.4.0
  * Type:


True if headers were sent, false otherwise (read-only).
#####  `http2stream.pushAllowed`[#](https://nodejs.org/docs/latest/api/http2.html#http2streampushallowed)
Added in: v8.4.0
  * Type:


Read-only property mapped to the `SETTINGS_ENABLE_PUSH` flag of the remote client's most recent `SETTINGS` frame. Will be `true` if the remote peer accepts push streams, `false` otherwise. Settings are the same for every `Http2Stream` in the same `Http2Session`.
#####  `http2stream.pushStream(headers[, options], callback)`[#](https://nodejs.org/docs/latest/api/http2.html#http2streampushstreamheaders-options-callback)
Added in: v8.4.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * `options`
    * `exclusive` `true` and `parent` identifies a parent Stream, the created stream is made the sole direct dependency of the parent, with all other existing dependents made a dependent of the newly created stream. **Default:** `false`.
    * `parent`
  * `callback`
    * `err`
    * `pushStream` [`<ServerHttp2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2stream) The returned `pushStream` object.
    * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object) Headers object the `pushStream` was initiated with.


Initiates a push stream. The callback is invoked with the new `Http2Stream` instance created for the push stream passed as the second argument, or an `Error` passed as the first argument.
```
import { createServer } from 'node:http2';
const server = createServer();
server.on('stream', (stream) => {
  stream.respond({ ':status': 200 });
  stream.pushStream({ ':path': '/' }, (err, pushStream, headers) => {
    if (err) throw err;
    pushStream.respond({ ':status': 200 });
    pushStream.end('some pushed data');
  });
  stream.end('some data');
});
const http2 = require('node:http2');
const server = http2.createServer();
server.on('stream', (stream) => {
  stream.respond({ ':status': 200 });
  stream.pushStream({ ':path': '/' }, (err, pushStream, headers) => {
    if (err) throw err;
    pushStream.respond({ ':status': 200 });
    pushStream.end('some pushed data');
  });
  stream.end('some data');
});
copy
```

Setting the weight of a push stream is not allowed in the `HEADERS` frame. Pass a `weight` value to `http2stream.priority` with the `silent` option set to `true` to enable server-side bandwidth balancing between concurrent streams.
Calling `http2stream.pushStream()` from within a pushed stream is not permitted and will throw an error.
#####  `http2stream.respond([headers[, options]])`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamrespondheaders-options)
Added in: v8.4.0History Version | Changes
---|---
v24.7.0, v22.20.0 | Allow passing headers in raw array format.
v14.5.0, v12.19.0 | Allow explicitly setting date headers.
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * `options`
    * `endStream` `true` to indicate that the response will not include payload data.
    * `waitForTrailers` `true`, the `Http2Stream` will emit the `'wantTrailers'` event after the final `DATA` frame has been sent.

```
import { createServer } from 'node:http2';
const server = createServer();
server.on('stream', (stream) => {
  stream.respond({ ':status': 200 });
  stream.end('some data');
});
const http2 = require('node:http2');
const server = http2.createServer();
server.on('stream', (stream) => {
  stream.respond({ ':status': 200 });
  stream.end('some data');
});
copy
```

Initiates a response. When the `options.waitForTrailers` option is set, the `'wantTrailers'` event will be emitted immediately after queuing the last chunk of payload data to be sent. The `http2stream.sendTrailers()` method can then be used to sent trailing header fields to the peer.
When `options.waitForTrailers` is set, the `Http2Stream` will not automatically close when the final `DATA` frame is transmitted. User code must call either `http2stream.sendTrailers()` or `http2stream.close()` to close the `Http2Stream`.
```
import { createServer } from 'node:http2';
const server = createServer();
server.on('stream', (stream) => {
  stream.respond({ ':status': 200 }, { waitForTrailers: true });
  stream.on('wantTrailers', () => {
    stream.sendTrailers({ ABC: 'some value to send' });
  });
  stream.end('some data');
});
const http2 = require('node:http2');
const server = http2.createServer();
server.on('stream', (stream) => {
  stream.respond({ ':status': 200 }, { waitForTrailers: true });
  stream.on('wantTrailers', () => {
    stream.sendTrailers({ ABC: 'some value to send' });
  });
  stream.end('some data');
});
copy
```

#####  `http2stream.respondWithFD(fd[, headers[, options]])`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamrespondwithfdfd-headers-options)
Added in: v8.4.0History Version | Changes
---|---
v14.5.0, v12.19.0 | Allow explicitly setting date headers.
v12.12.0 | The `fd` option may now be a `FileHandle`.
v10.0.0 | Any readable file descriptor, not necessarily for a regular file, is supported now.
  * `fd` [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) A readable file descriptor.
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * `options`
    * `statCheck`
    * `waitForTrailers` `true`, the `Http2Stream` will emit the `'wantTrailers'` event after the final `DATA` frame has been sent.
    * `offset`
    * `length`


Initiates a response whose data is read from the given file descriptor. No validation is performed on the given file descriptor. If an error occurs while attempting to read data using the file descriptor, the `Http2Stream` will be closed using an `RST_STREAM` frame using the standard `INTERNAL_ERROR` code.
When used, the `Http2Stream` object's `Duplex` interface will be closed automatically.
```
import { createServer } from 'node:http2';
import { openSync, fstatSync, closeSync } from 'node:fs';

const server = createServer();
server.on('stream', (stream) => {
  const fd = openSync('/some/file', 'r');

  const stat = fstatSync(fd);
  const headers = {
    'content-length': stat.size,
    'last-modified': stat.mtime.toUTCString(),
    'content-type': 'text/plain; charset=utf-8',
  };
  stream.respondWithFD(fd, headers);
  stream.on('close', () => closeSync(fd));
});
const http2 = require('node:http2');
const fs = require('node:fs');

const server = http2.createServer();
server.on('stream', (stream) => {
  const fd = fs.openSync('/some/file', 'r');

  const stat = fs.fstatSync(fd);
  const headers = {
    'content-length': stat.size,
    'last-modified': stat.mtime.toUTCString(),
    'content-type': 'text/plain; charset=utf-8',
  };
  stream.respondWithFD(fd, headers);
  stream.on('close', () => fs.closeSync(fd));
});
copy
```

The optional `options.statCheck` function may be specified to give user code an opportunity to set additional content headers based on the `fs.Stat` details of the given fd. If the `statCheck` function is provided, the `http2stream.respondWithFD()` method will perform an `fs.fstat()` call to collect details on the provided file descriptor.
The `offset` and `length` options may be used to limit the response to a specific range subset. This can be used, for instance, to support HTTP Range requests.
The file descriptor or `FileHandle` is not closed when the stream is closed, so it will need to be closed manually once it is no longer needed. Using the same file descriptor concurrently for multiple streams is not supported and may result in data loss. Reusing a file descriptor after a stream has finished is supported.
When the `options.waitForTrailers` option is set, the `'wantTrailers'` event will be emitted immediately after queuing the last chunk of payload data to be sent. The `http2stream.sendTrailers()` method can then be used to sent trailing header fields to the peer.
When `options.waitForTrailers` is set, the `Http2Stream` will not automatically close when the final `DATA` frame is transmitted. User code _must_ call either `http2stream.sendTrailers()` or `http2stream.close()` to close the `Http2Stream`.
```
import { createServer } from 'node:http2';
import { openSync, fstatSync, closeSync } from 'node:fs';

const server = createServer();
server.on('stream', (stream) => {
  const fd = openSync('/some/file', 'r');

  const stat = fstatSync(fd);
  const headers = {
    'content-length': stat.size,
    'last-modified': stat.mtime.toUTCString(),
    'content-type': 'text/plain; charset=utf-8',
  };
  stream.respondWithFD(fd, headers, { waitForTrailers: true });
  stream.on('wantTrailers', () => {
    stream.sendTrailers({ ABC: 'some value to send' });
  });

  stream.on('close', () => closeSync(fd));
});
const http2 = require('node:http2');
const fs = require('node:fs');

const server = http2.createServer();
server.on('stream', (stream) => {
  const fd = fs.openSync('/some/file', 'r');

  const stat = fs.fstatSync(fd);
  const headers = {
    'content-length': stat.size,
    'last-modified': stat.mtime.toUTCString(),
    'content-type': 'text/plain; charset=utf-8',
  };
  stream.respondWithFD(fd, headers, { waitForTrailers: true });
  stream.on('wantTrailers', () => {
    stream.sendTrailers({ ABC: 'some value to send' });
  });

  stream.on('close', () => fs.closeSync(fd));
});
copy
```

#####  `http2stream.respondWithFile(path[, headers[, options]])`[#](https://nodejs.org/docs/latest/api/http2.html#http2streamrespondwithfilepath-headers-options)
Added in: v8.4.0History Version | Changes
---|---
v14.5.0, v12.19.0 | Allow explicitly setting date headers.
v10.0.0 | Any readable file, not necessarily a regular file, is supported now.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * `options`
    * `statCheck`
    * `onError`
    * `waitForTrailers` `true`, the `Http2Stream` will emit the `'wantTrailers'` event after the final `DATA` frame has been sent.
    * `offset`
    * `length`


Sends a regular file as the response. The `path` must specify a regular file or an `'error'` event will be emitted on the `Http2Stream` object.
When used, the `Http2Stream` object's `Duplex` interface will be closed automatically.
The optional `options.statCheck` function may be specified to give user code an opportunity to set additional content headers based on the `fs.Stat` details of the given file:
If an error occurs while attempting to read the file data, the `Http2Stream` will be closed using an `RST_STREAM` frame using the standard `INTERNAL_ERROR` code. If the `onError` callback is defined, then it will be called. Otherwise the stream will be destroyed.
Example using a file path:
```
import { createServer } from 'node:http2';
const server = createServer();
server.on('stream', (stream) => {
  function statCheck(stat, headers) {
    headers['last-modified'] = stat.mtime.toUTCString();
  }

  function onError(err) {
    // stream.respond() can throw if the stream has been destroyed by
    // the other side.
    try {
      if (err.code === 'ENOENT') {
        stream.respond({ ':status': 404 });
      } else {
        stream.respond({ ':status': 500 });
      }
    } catch (err) {
      // Perform actual error handling.
      console.error(err);
    }
    stream.end();
  }

  stream.respondWithFile('/some/file',
                         { 'content-type': 'text/plain; charset=utf-8' },
                         { statCheck, onError });
});
const http2 = require('node:http2');
const server = http2.createServer();
server.on('stream', (stream) => {
  function statCheck(stat, headers) {
    headers['last-modified'] = stat.mtime.toUTCString();
  }

  function onError(err) {
    // stream.respond() can throw if the stream has been destroyed by
    // the other side.
    try {
      if (err.code === 'ENOENT') {
        stream.respond({ ':status': 404 });
      } else {
        stream.respond({ ':status': 500 });
      }
    } catch (err) {
      // Perform actual error handling.
      console.error(err);
    }
    stream.end();
  }

  stream.respondWithFile('/some/file',
                         { 'content-type': 'text/plain; charset=utf-8' },
                         { statCheck, onError });
});
copy
```

The `options.statCheck` function may also be used to cancel the send operation by returning `false`. For instance, a conditional request may check the stat results to determine if the file has been modified to return an appropriate `304` response:
```
import { createServer } from 'node:http2';
const server = createServer();
server.on('stream', (stream) => {
  function statCheck(stat, headers) {
    // Check the stat here...
    stream.respond({ ':status': 304 });
    return false; // Cancel the send operation
  }
  stream.respondWithFile('/some/file',
                         { 'content-type': 'text/plain; charset=utf-8' },
                         { statCheck });
});
const http2 = require('node:http2');
const server = http2.createServer();
server.on('stream', (stream) => {
  function statCheck(stat, headers) {
    // Check the stat here...
    stream.respond({ ':status': 304 });
    return false; // Cancel the send operation
  }
  stream.respondWithFile('/some/file',
                         { 'content-type': 'text/plain; charset=utf-8' },
                         { statCheck });
});
copy
```

The `content-length` header field will be automatically set.
The `offset` and `length` options may be used to limit the response to a specific range subset. This can be used, for instance, to support HTTP Range requests.
The `options.onError` function may also be used to handle all the errors that could happen before the delivery of the file is initiated. The default behavior is to destroy the stream.
When the `options.waitForTrailers` option is set, the `'wantTrailers'` event will be emitted immediately after queuing the last chunk of payload data to be sent. The `http2stream.sendTrailers()` method can then be used to sent trailing header fields to the peer.
When `options.waitForTrailers` is set, the `Http2Stream` will not automatically close when the final `DATA` frame is transmitted. User code must call either `http2stream.sendTrailers()` or `http2stream.close()` to close the `Http2Stream`.
```
import { createServer } from 'node:http2';
const server = createServer();
server.on('stream', (stream) => {
  stream.respondWithFile('/some/file',
                         { 'content-type': 'text/plain; charset=utf-8' },
                         { waitForTrailers: true });
  stream.on('wantTrailers', () => {
    stream.sendTrailers({ ABC: 'some value to send' });
  });
});
const http2 = require('node:http2');
const server = http2.createServer();
server.on('stream', (stream) => {
  stream.respondWithFile('/some/file',
                         { 'content-type': 'text/plain; charset=utf-8' },
                         { waitForTrailers: true });
  stream.on('wantTrailers', () => {
    stream.sendTrailers({ ABC: 'some value to send' });
  });
});
copy
```

#### Class: `Http2Server`[#](https://nodejs.org/docs/latest/api/http2.html#class-http2server)
Added in: v8.4.0
  * Extends: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Instances of `Http2Server` are created using the `http2.createServer()` function. The `Http2Server` class is not exported directly by the `node:http2` module.
##### Event: `'checkContinue'`[#](https://nodejs.org/docs/latest/api/http2.html#event-checkcontinue)
Added in: v8.5.0
  * `request` [`<http2.Http2ServerRequest>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverrequest)
  * `response` [`<http2.Http2ServerResponse>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverresponse)


If a [`'request'`](https://nodejs.org/docs/latest/api/http2.html#event-request) listener is registered or [`http2.createServer()`](https://nodejs.org/docs/latest/api/http2.html#http2createserveroptions-onrequesthandler) is supplied a callback function, the `'checkContinue'` event is emitted each time a request with an HTTP `Expect: 100-continue` is received. If this event is not listened for, the server will automatically respond with a status `100 Continue` as appropriate.
Handling this event involves calling [`response.writeContinue()`](https://nodejs.org/docs/latest/api/http2.html#responsewritecontinue) if the client should continue to send the request body, or generating an appropriate HTTP response (e.g. 400 Bad Request) if the client should not continue to send the request body.
When this event is emitted and handled, the [`'request'`](https://nodejs.org/docs/latest/api/http2.html#event-request) event will not be emitted.
##### Event: `'connection'`[#](https://nodejs.org/docs/latest/api/http2.html#event-connection)
Added in: v8.4.0
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


This event is emitted when a new TCP stream is established. `socket` is typically an object of type [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket). Usually users will not want to access this event.
This event can also be explicitly emitted by users to inject connections into the HTTP server. In that case, any [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) stream can be passed.
##### Event: `'request'`[#](https://nodejs.org/docs/latest/api/http2.html#event-request)
Added in: v8.4.0
  * `request` [`<http2.Http2ServerRequest>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverrequest)
  * `response` [`<http2.Http2ServerResponse>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverresponse)


Emitted each time there is a request. There may be multiple requests per session. See the [Compatibility API](https://nodejs.org/docs/latest/api/http2.html#compatibility-api).
##### Event: `'session'`[#](https://nodejs.org/docs/latest/api/http2.html#event-session)
Added in: v8.4.0
  * `session` [`<ServerHttp2Session>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2session)


The `'session'` event is emitted when a new `Http2Session` is created by the `Http2Server`.
##### Event: `'sessionError'`[#](https://nodejs.org/docs/latest/api/http2.html#event-sessionerror)
Added in: v8.4.0
  * `error`
  * `session` [`<ServerHttp2Session>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2session)


The `'sessionError'` event is emitted when an `'error'` event is emitted by an `Http2Session` object associated with the `Http2Server`.
##### Event: `'stream'`[#](https://nodejs.org/docs/latest/api/http2.html#event-stream-1)
Added in: v8.4.0
  * `stream` [`<Http2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) A reference to the stream
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object) An object describing the headers
  * `flags`
  * `rawHeaders` {HTTP/2 Raw Headers} An array containing the raw headers


The `'stream'` event is emitted when a `'stream'` event has been emitted by an `Http2Session` associated with the server.
See also [`Http2Session`'s `'stream'` event](https://nodejs.org/docs/latest/api/http2.html#event-stream).
```
import { createServer, constants } from 'node:http2';
const {
  HTTP2_HEADER_METHOD,
  HTTP2_HEADER_PATH,
  HTTP2_HEADER_STATUS,
  HTTP2_HEADER_CONTENT_TYPE,
} = constants;

const server = createServer();
server.on('stream', (stream, headers, flags) => {
  const method = headers[HTTP2_HEADER_METHOD];
  const path = headers[HTTP2_HEADER_PATH];
  // ...
  stream.respond({
    [HTTP2_HEADER_STATUS]: 200,
    [HTTP2_HEADER_CONTENT_TYPE]: 'text/plain; charset=utf-8',
  });
  stream.write('hello ');
  stream.end('world');
});
const http2 = require('node:http2');
const {
  HTTP2_HEADER_METHOD,
  HTTP2_HEADER_PATH,
  HTTP2_HEADER_STATUS,
  HTTP2_HEADER_CONTENT_TYPE,
} = http2.constants;

const server = http2.createServer();
server.on('stream', (stream, headers, flags) => {
  const method = headers[HTTP2_HEADER_METHOD];
  const path = headers[HTTP2_HEADER_PATH];
  // ...
  stream.respond({
    [HTTP2_HEADER_STATUS]: 200,
    [HTTP2_HEADER_CONTENT_TYPE]: 'text/plain; charset=utf-8',
  });
  stream.write('hello ');
  stream.end('world');
});
copy
```

##### Event: `'timeout'`[#](https://nodejs.org/docs/latest/api/http2.html#event-timeout-2)
Added in: v8.4.0History Version | Changes
---|---
v13.0.0 | The default timeout changed from 120s to 0 (no timeout).
The `'timeout'` event is emitted when there is no activity on the Server for a given number of milliseconds set using `http2server.setTimeout()`. **Default:** 0 (no timeout)
#####  `server.close([callback])`[#](https://nodejs.org/docs/latest/api/http2.html#serverclosecallback)
Added in: v8.4.0
  * `callback`


Stops the server from establishing new sessions. This does not prevent new request streams from being created due to the persistent nature of HTTP/2 sessions. To gracefully shut down the server, call [`http2session.close()`](https://nodejs.org/docs/latest/api/http2.html#http2sessionclosecallback) on all active sessions.
