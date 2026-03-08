All other interactions will be routed directly to the socket.
```
import { createServer } from 'node:http2';
const server = createServer((req, res) => {
  const ip = req.socket.remoteAddress;
  const port = req.socket.remotePort;
  res.end(`Your IP address is ${ip} and your source port is ${port}.`);
}).listen(3000);
const http2 = require('node:http2');
const server = http2.createServer((req, res) => {
  const ip = req.socket.remoteAddress;
  const port = req.socket.remotePort;
  res.end(`Your IP address is ${ip} and your source port is ${port}.`);
}).listen(3000);
copy
```

#####  `response.statusCode`[#](https://nodejs.org/docs/latest/api/http2.html#responsestatuscode)
Added in: v8.4.0
  * Type:


When using implicit headers (not calling [`response.writeHead()`](https://nodejs.org/docs/latest/api/http2.html#responsewriteheadstatuscode-statusmessage-headers) explicitly), this property controls the status code that will be sent to the client when the headers get flushed.
```
response.statusCode = 404;
copy
```

After response header was sent to the client, this property indicates the status code which was sent out.
#####  `response.statusMessage`[#](https://nodejs.org/docs/latest/api/http2.html#responsestatusmessage)
Added in: v8.4.0
  * Type:


Status message is not supported by HTTP/2 (RFC 7540 8.1.2.4). It returns an empty string.
#####  `response.stream`[#](https://nodejs.org/docs/latest/api/http2.html#responsestream)
Added in: v8.4.0
  * Type: [`<Http2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream)


The [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) object backing the response.
#####  `response.writableEnded`[#](https://nodejs.org/docs/latest/api/http2.html#responsewritableended)
Added in: v12.9.0
  * Type:


Is `true` after [`response.end()`](https://nodejs.org/docs/latest/api/http2.html#responseenddata-encoding-callback) has been called. This property does not indicate whether the data has been flushed, for this use [`writable.writableFinished`](https://nodejs.org/docs/latest/api/stream.html#writablewritablefinished) instead.
#####  `response.write(chunk[, encoding][, callback])`[#](https://nodejs.org/docs/latest/api/http2.html#responsewritechunk-encoding-callback)
Added in: v8.4.0
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding`
  * `callback`
  * Returns:


If this method is called and [`response.writeHead()`](https://nodejs.org/docs/latest/api/http2.html#responsewriteheadstatuscode-statusmessage-headers) has not been called, it will switch to implicit header mode and flush the implicit headers.
This sends a chunk of the response body. This method may be called multiple times to provide successive parts of the body.
In the `node:http` module, the response body is omitted when the request is a HEAD request. Similarly, the `204` and `304` responses _must not_ include a message body.
`chunk` can be a string or a buffer. If `chunk` is a string, the second parameter specifies how to encode it into a byte stream. By default the `encoding` is `'utf8'`. `callback` will be called when this chunk of data is flushed.
This is the raw HTTP body and has nothing to do with higher-level multi-part body encodings that may be used.
The first time [`response.write()`](https://nodejs.org/docs/latest/api/http2.html#responsewritechunk-encoding-callback) is called, it will send the buffered header information and the first chunk of the body to the client. The second time [`response.write()`](https://nodejs.org/docs/latest/api/http2.html#responsewritechunk-encoding-callback) is called, Node.js assumes data will be streamed, and sends the new data separately. That is, the response is buffered up to the first chunk of the body.
Returns `true` if the entire data was flushed successfully to the kernel buffer. Returns `false` if all or part of the data was queued in user memory. `'drain'` will be emitted when the buffer is free again.
#####  `response.writeContinue()`[#](https://nodejs.org/docs/latest/api/http2.html#responsewritecontinue)
Added in: v8.4.0
Sends a status `100 Continue` to the client, indicating that the request body should be sent. See the [`'checkContinue'`](https://nodejs.org/docs/latest/api/http2.html#event-checkcontinue) event on `Http2Server` and `Http2SecureServer`.
#####  `response.writeEarlyHints(hints)`[#](https://nodejs.org/docs/latest/api/http2.html#responsewriteearlyhintshints)
Added in: v18.11.0
  * `hints`


Sends a status `103 Early Hints` to the client with a Link header, indicating that the user agent can preload/preconnect the linked resources. The `hints` is an object containing the values of headers to be sent with early hints message.
**Example**
```
const earlyHintsLink = '</styles.css>; rel=preload; as=style';
response.writeEarlyHints({
  'link': earlyHintsLink,
});

const earlyHintsLinks = [
  '</styles.css>; rel=preload; as=style',
  '</scripts.js>; rel=preload; as=script',
];
response.writeEarlyHints({
  'link': earlyHintsLinks,
});
copy
```

#####  `response.writeHead(statusCode[, statusMessage][, headers])`[#](https://nodejs.org/docs/latest/api/http2.html#responsewriteheadstatuscode-statusmessage-headers)
Added in: v8.4.0History Version | Changes
---|---
v11.10.0, v10.17.0 | Return `this` from `writeHead()` to allow chaining with `end()`.
  * `statusCode`
  * `statusMessage`
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object)
  * Returns: [`<http2.Http2ServerResponse>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverresponse)


Sends a response header to the request. The status code is a 3-digit HTTP status code, like `404`. The last argument, `headers`, are the response headers.
Returns a reference to the `Http2ServerResponse`, so that calls can be chained.
For compatibility with [HTTP/1](https://nodejs.org/docs/latest/api/http.html), a human-readable `statusMessage` may be passed as the second argument. However, because the `statusMessage` has no meaning within HTTP/2, the argument will have no effect and a process warning will be emitted.
```
const body = 'hello world';
response.writeHead(200, {
  'Content-Length': Buffer.byteLength(body),
  'Content-Type': 'text/plain; charset=utf-8',
});
copy
```

`Content-Length` is given in bytes not characters. The `Buffer.byteLength()` API may be used to determine the number of bytes in a given encoding. On outbound messages, Node.js does not check if Content-Length and the length of the body being transmitted are equal or not. However, when receiving messages, Node.js will automatically reject messages when the `Content-Length` does not match the actual payload size.
This method may be called at most one time on a message before [`response.end()`](https://nodejs.org/docs/latest/api/http2.html#responseenddata-encoding-callback) is called.
If [`response.write()`](https://nodejs.org/docs/latest/api/http2.html#responsewritechunk-encoding-callback) or [`response.end()`](https://nodejs.org/docs/latest/api/http2.html#responseenddata-encoding-callback) are called before calling this, the implicit/mutable headers will be calculated and call this function.
When headers have been set with [`response.setHeader()`](https://nodejs.org/docs/latest/api/http2.html#responsesetheadername-value), they will be merged with any headers passed to [`response.writeHead()`](https://nodejs.org/docs/latest/api/http2.html#responsewriteheadstatuscode-statusmessage-headers), with the headers passed to [`response.writeHead()`](https://nodejs.org/docs/latest/api/http2.html#responsewriteheadstatuscode-statusmessage-headers) given precedence.
```
// Returns content-type = text/plain
const server = http2.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.setHeader('X-Foo', 'bar');
  res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
  res.end('ok');
});
copy
```

Attempting to set a header field name or value that contains invalid characters will result in a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) being thrown.
### Collecting HTTP/2 performance metrics[#](https://nodejs.org/docs/latest/api/http2.html#collecting-http2-performance-metrics)
The [Performance Observer](https://nodejs.org/docs/latest/api/perf_hooks.html) API can be used to collect basic performance metrics for each `Http2Session` and `Http2Stream` instance.
```
import { PerformanceObserver } from 'node:perf_hooks';

const obs = new PerformanceObserver((items) => {
  const entry = items.getEntries()[0];
  console.log(entry.entryType);  // prints 'http2'
  if (entry.name === 'Http2Session') {
    // Entry contains statistics about the Http2Session
  } else if (entry.name === 'Http2Stream') {
    // Entry contains statistics about the Http2Stream
  }
});
obs.observe({ entryTypes: ['http2'] });
const { PerformanceObserver } = require('node:perf_hooks');

const obs = new PerformanceObserver((items) => {
  const entry = items.getEntries()[0];
  console.log(entry.entryType);  // prints 'http2'
  if (entry.name === 'Http2Session') {
    // Entry contains statistics about the Http2Session
  } else if (entry.name === 'Http2Stream') {
    // Entry contains statistics about the Http2Stream
  }
});
obs.observe({ entryTypes: ['http2'] });
copy
```

The `entryType` property of the `PerformanceEntry` will be equal to `'http2'`.
The `name` property of the `PerformanceEntry` will be equal to either `'Http2Stream'` or `'Http2Session'`.
If `name` is equal to `Http2Stream`, the `PerformanceEntry` will contain the following additional properties:
  * `bytesRead` `DATA` frame bytes received for this `Http2Stream`.
  * `bytesWritten` `DATA` frame bytes sent for this `Http2Stream`.
  * `id` `Http2Stream`
  * `timeToFirstByte` `PerformanceEntry` `startTime` and the reception of the first `DATA` frame.
  * `timeToFirstByteSent` `PerformanceEntry` `startTime` and sending of the first `DATA` frame.
  * `timeToFirstHeader` `PerformanceEntry` `startTime` and the reception of the first header.


If `name` is equal to `Http2Session`, the `PerformanceEntry` will contain the following additional properties:
  * `bytesRead` `Http2Session`.
  * `bytesWritten` `Http2Session`.
  * `framesReceived` `Http2Session`.
  * `framesSent` `Http2Session`.
  * `maxConcurrentStreams` `Http2Session`.
  * `pingRTT` `PING` frame and the reception of its acknowledgment. Only present if a `PING` frame has been sent on the `Http2Session`.
  * `streamAverageDuration` `Http2Stream` instances.
  * `streamCount` `Http2Stream` instances processed by the `Http2Session`.
  * `type` `'server'` or `'client'` to identify the type of `Http2Session`.


### Note on `:authority` and `host`[#](https://nodejs.org/docs/latest/api/http2.html#note-on-authority-and-host)
HTTP/2 requires requests to have either the `:authority` pseudo-header or the `host` header. Prefer `:authority` when constructing an HTTP/2 request directly, and `host` when converting from HTTP/1 (in proxies, for instance).
The compatibility API falls back to `host` if `:authority` is not present. See [`request.authority`](https://nodejs.org/docs/latest/api/http2.html#requestauthority) for more information. However, if you don't use the compatibility API (or use `req.headers` directly), you need to implement any fall-back behavior yourself.
