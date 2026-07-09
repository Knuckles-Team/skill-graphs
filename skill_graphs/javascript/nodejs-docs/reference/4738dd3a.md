####  `response.setTimeout(msecs[, callback])`[#](https://nodejs.org/docs/latest/api/http.html#responsesettimeoutmsecs-callback)
Added in: v0.9.12
  * `msecs`
  * `callback`
  * Returns: [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)


Sets the Socket's timeout value to `msecs`. If a callback is provided, then it is added as a listener on the `'timeout'` event on the response object.
If no `'timeout'` listener is added to the request, the response, or the server, then sockets are destroyed when they time out. If a handler is assigned to the request, the response, or the server's `'timeout'` events, timed out sockets must be handled explicitly.
####  `response.socket`[#](https://nodejs.org/docs/latest/api/http.html#responsesocket)
Added in: v0.3.0
  * Type: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


Reference to the underlying socket. Usually users will not want to access this property. In particular, the socket will not emit `'readable'` events because of how the protocol parser attaches to the socket. After `response.end()`, the property is nulled.
```
import http from 'node:http';
const server = http.createServer((req, res) => {
  const ip = res.socket.remoteAddress;
  const port = res.socket.remotePort;
  res.end(`Your IP address is ${ip} and your source port is ${port}.`);
}).listen(3000);
const http = require('node:http');
const server = http.createServer((req, res) => {
  const ip = res.socket.remoteAddress;
  const port = res.socket.remotePort;
  res.end(`Your IP address is ${ip} and your source port is ${port}.`);
}).listen(3000);
copy
```

This property is guaranteed to be an instance of the [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) class, a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), unless the user specified a socket type other than [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
####  `response.statusCode`[#](https://nodejs.org/docs/latest/api/http.html#responsestatuscode)
Added in: v0.4.0
  * Type: **Default:** `200`


When using implicit headers (not calling [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers) explicitly), this property controls the status code that will be sent to the client when the headers get flushed.
```
response.statusCode = 404;
copy
```

After response header was sent to the client, this property indicates the status code which was sent out.
####  `response.statusMessage`[#](https://nodejs.org/docs/latest/api/http.html#responsestatusmessage)
Added in: v0.11.8
  * Type:


When using implicit headers (not calling [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers) explicitly), this property controls the status message that will be sent to the client when the headers get flushed. If this is left as `undefined` then the standard message for the status code will be used.
```
response.statusMessage = 'Not found';
copy
```

After response header was sent to the client, this property indicates the status message which was sent out.
####  `response.strictContentLength`[#](https://nodejs.org/docs/latest/api/http.html#responsestrictcontentlength)
Added in: v18.10.0, v16.18.0
  * Type: **Default:** `false`


If set to `true`, Node.js will check whether the `Content-Length` header value and the size of the body, in bytes, are equal. Mismatching the `Content-Length` header value will result in an `Error` being thrown, identified by `code:` [`'ERR_HTTP_CONTENT_LENGTH_MISMATCH'`](https://nodejs.org/docs/latest/api/errors.html#err_http_content_length_mismatch).
####  `response.uncork()`[#](https://nodejs.org/docs/latest/api/http.html#responseuncork)
Added in: v13.2.0, v12.16.0
See [`writable.uncork()`](https://nodejs.org/docs/latest/api/stream.html#writableuncork).
####  `response.writableEnded`[#](https://nodejs.org/docs/latest/api/http.html#responsewritableended)
Added in: v12.9.0
  * Type:


Is `true` after [`response.end()`](https://nodejs.org/docs/latest/api/http.html#responseenddata-encoding-callback) has been called. This property does not indicate whether the data has been flushed, for this use [`response.writableFinished`](https://nodejs.org/docs/latest/api/http.html#responsewritablefinished) instead.
####  `response.writableFinished`[#](https://nodejs.org/docs/latest/api/http.html#responsewritablefinished)
Added in: v12.7.0
  * Type:


Is `true` if all data has been flushed to the underlying system, immediately before the [`'finish'`](https://nodejs.org/docs/latest/api/http.html#event-finish) event is emitted.
####  `response.write(chunk[, encoding][, callback])`[#](https://nodejs.org/docs/latest/api/http.html#responsewritechunk-encoding-callback)
Added in: v0.1.29History Version | Changes
---|---
v15.0.0 | The `chunk` parameter can now be a `Uint8Array`.
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` **Default:** `'utf8'`
  * `callback`
  * Returns:


If this method is called and [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers) has not been called, it will switch to implicit header mode and flush the implicit headers.
This sends a chunk of the response body. This method may be called multiple times to provide successive parts of the body.
If `rejectNonStandardBodyWrites` is set to true in `createServer` then writing to the body is not allowed when the request method or response status do not support content. If an attempt is made to write to the body for a HEAD request or as part of a `204` or `304`response, a synchronous `Error` with the code `ERR_HTTP_BODY_NOT_ALLOWED` is thrown.
`chunk` can be a string or a buffer. If `chunk` is a string, the second parameter specifies how to encode it into a byte stream. `callback` will be called when this chunk of data is flushed.
This is the raw HTTP body and has nothing to do with higher-level multi-part body encodings that may be used.
The first time [`response.write()`](https://nodejs.org/docs/latest/api/http.html#responsewritechunk-encoding-callback) is called, it will send the buffered header information and the first chunk of the body to the client. The second time [`response.write()`](https://nodejs.org/docs/latest/api/http.html#responsewritechunk-encoding-callback) is called, Node.js assumes data will be streamed, and sends the new data separately. That is, the response is buffered up to the first chunk of the body.
Returns `true` if the entire data was flushed successfully to the kernel buffer. Returns `false` if all or part of the data was queued in user memory. `'drain'` will be emitted when the buffer is free again.
####  `response.writeContinue()`[#](https://nodejs.org/docs/latest/api/http.html#responsewritecontinue)
Added in: v0.3.0
Sends an HTTP/1.1 100 Continue message to the client, indicating that the request body should be sent. See the [`'checkContinue'`](https://nodejs.org/docs/latest/api/http.html#event-checkcontinue) event on `Server`.
####  `response.writeEarlyHints(hints[, callback])`[#](https://nodejs.org/docs/latest/api/http.html#responsewriteearlyhintshints-callback)
Added in: v18.11.0History Version | Changes
---|---
v18.11.0 | Allow passing hints as an object.
  * `hints`
  * `callback`


Sends an HTTP/1.1 103 Early Hints message to the client with a Link header, indicating that the user agent can preload/preconnect the linked resources. The `hints` is an object containing the values of headers to be sent with early hints message. The optional `callback` argument will be called when the response message has been written.
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
  'x-trace-id': 'id for diagnostics',
});

const earlyHintsCallback = () => console.log('early hints message sent');
response.writeEarlyHints({
  'link': earlyHintsLinks,
}, earlyHintsCallback);
copy
```

####  `response.writeHead(statusCode[, statusMessage][, headers])`[#](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers)
Added in: v0.1.30History Version | Changes
---|---
v14.14.0 | Allow passing headers as an array.
v11.10.0, v10.17.0 | Return `this` from `writeHead()` to allow chaining with `end()`.
v5.11.0, v4.4.5 | A `RangeError` is thrown if `statusCode` is not a number in the range `[100, 999]`.
  * `statusCode`
  * `statusMessage`
  * `headers`
  * Returns: [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)


Sends a response header to the request. The status code is a 3-digit HTTP status code, like `404`. The last argument, `headers`, are the response headers. Optionally one can give a human-readable `statusMessage` as the second argument.
`headers` may be an `Array` where the keys and values are in the same list. It is _not_ a list of tuples. So, the even-numbered offsets are key values, and the odd-numbered offsets are the associated values. The array is in the same format as `request.rawHeaders`.
Returns a reference to the `ServerResponse`, so that calls can be chained.
```
const body = 'hello world';
response
  .writeHead(200, {
    'Content-Length': Buffer.byteLength(body),
    'Content-Type': 'text/plain',
  })
  .end(body);
copy
```

This method must only be called once on a message and it must be called before [`response.end()`](https://nodejs.org/docs/latest/api/http.html#responseenddata-encoding-callback) is called.
If [`response.write()`](https://nodejs.org/docs/latest/api/http.html#responsewritechunk-encoding-callback) or [`response.end()`](https://nodejs.org/docs/latest/api/http.html#responseenddata-encoding-callback) are called before calling this, the implicit/mutable headers will be calculated and call this function.
When headers have been set with [`response.setHeader()`](https://nodejs.org/docs/latest/api/http.html#responsesetheadername-value), they will be merged with any headers passed to [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers), with the headers passed to [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers) given precedence.
If this method is called and [`response.setHeader()`](https://nodejs.org/docs/latest/api/http.html#responsesetheadername-value) has not been called, it will directly write the supplied header values onto the network channel without caching internally, and the [`response.getHeader()`](https://nodejs.org/docs/latest/api/http.html#responsegetheadername) on the header will not yield the expected result. If progressive population of headers is desired with potential future retrieval and modification, use [`response.setHeader()`](https://nodejs.org/docs/latest/api/http.html#responsesetheadername-value) instead.
```
// Returns content-type = text/plain
const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html');
  res.setHeader('X-Foo', 'bar');
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('ok');
});
copy
```

`Content-Length` is read in bytes, not characters. Use [`Buffer.byteLength()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferbytelengthstring-encoding) to determine the length of the body in bytes. Node.js will check whether `Content-Length` and the length of the body which has been transmitted are equal or not.
Attempting to set a header field name or value that contains invalid characters will result in a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) being thrown.
####  `response.writeProcessing()`[#](https://nodejs.org/docs/latest/api/http.html#responsewriteprocessing)
Added in: v10.0.0
Sends a HTTP/1.1 102 Processing message to the client, indicating that the request body should be sent.
### Class: `http.IncomingMessage`[#](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
Added in: v0.1.17History Version | Changes
---|---
v15.5.0 | The `destroyed` value returns `true` after the incoming data is consumed.
v13.1.0, v12.16.0 | The `readableHighWaterMark` value mirrors that of the socket.
  * Extends: [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable)


An `IncomingMessage` object is created by [`http.Server`](https://nodejs.org/docs/latest/api/http.html#class-httpserver) or [`http.ClientRequest`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest) and passed as the first argument to the [`'request'`](https://nodejs.org/docs/latest/api/http.html#event-request) and [`'response'`](https://nodejs.org/docs/latest/api/http.html#event-response) event respectively. It may be used to access response status, headers, and data.
Different from its `socket` value which is a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), the `IncomingMessage` itself extends [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) and is created separately to parse and emit the incoming HTTP headers and payload, as the underlying socket may be reused multiple times in case of keep-alive.
#### Event: `'aborted'`[#](https://nodejs.org/docs/latest/api/http.html#event-aborted)
Added in: v0.3.8Deprecated in: v17.0.0, v16.12.0
Stability: 0 - Deprecated. Listen for `'close'` event instead.
Emitted when the request has been aborted.
#### Event: `'close'`[#](https://nodejs.org/docs/latest/api/http.html#event-close-3)
Added in: v0.4.2History Version | Changes
---|---
v16.0.0 | The close event is now emitted when the request has been completed and not when the underlying socket is closed.
Emitted when the request has been completed.
####  `message.aborted`[#](https://nodejs.org/docs/latest/api/http.html#messageaborted)
Added in: v10.1.0Deprecated in: v17.0.0, v16.12.0
Stability: 0 - Deprecated. Check `message.destroyed` from [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable).
  * Type:


The `message.aborted` property will be `true` if the request has been aborted.
####  `message.complete`[#](https://nodejs.org/docs/latest/api/http.html#messagecomplete)
Added in: v0.3.0
  * Type:


The `message.complete` property will be `true` if a complete HTTP message has been received and successfully parsed.
This property is particularly useful as a means of determining if a client or server fully transmitted a message before a connection was terminated:
```
const req = http.request({
  host: '127.0.0.1',
  port: 8080,
  method: 'POST',
}, (res) => {
  res.resume();
  res.on('end', () => {
    if (!res.complete)
      console.error(
        'The connection was terminated while the message was still being sent');
  });
});
copy
```

####  `message.connection`[#](https://nodejs.org/docs/latest/api/http.html#messageconnection)
Added in: v0.1.90Deprecated in: v16.0.0
Stability: 0 - Deprecated. Use [`message.socket`](https://nodejs.org/docs/latest/api/http.html#messagesocket).
Alias for [`message.socket`](https://nodejs.org/docs/latest/api/http.html#messagesocket).
####  `message.destroy([error])`[#](https://nodejs.org/docs/latest/api/http.html#messagedestroyerror)
Added in: v0.3.0History Version | Changes
---|---
v14.5.0, v12.19.0 | The function returns `this` for consistency with other Readable streams.
  * `error`
  * Returns:


Calls `destroy()` on the socket that received the `IncomingMessage`. If `error` is provided, an `'error'` event is emitted on the socket and `error` is passed as an argument to any listeners on the event.
####  `message.headers`[#](https://nodejs.org/docs/latest/api/http.html#messageheaders)
Added in: v0.1.5History Version | Changes
---|---
v19.5.0, v18.14.0 | The `joinDuplicateHeaders` option in the `http.request()` and `http.createServer()` functions ensures that duplicate headers are not discarded, but rather combined using a comma separator, in accordance with RFC 9110 Section 5.3.
v15.1.0 | `message.headers` is now lazily computed using an accessor property on the prototype and is no longer enumerable.
  * Type:


The request/response headers object.
Key-value pairs of header names and values. Header names are lower-cased.
```
// Prints something like:
//
// { 'user-agent': 'curl/7.22.0',
//   host: '127.0.0.1:8000',
//   accept: '*/*' }
console.log(request.headers);
copy
```

Duplicates in raw headers are handled in the following ways, depending on the header name:
  * Duplicates of `age`, `authorization`, `content-length`, `content-type`, `etag`, `expires`, `from`, `host`, `if-modified-since`, `if-unmodified-since`, `last-modified`, `location`, `max-forwards`, `proxy-authorization`, `referer`, `retry-after`, `server`, or `user-agent` are discarded. To allow duplicate values of the headers listed above to be joined, use the option `joinDuplicateHeaders` in [`http.request()`](https://nodejs.org/docs/latest/api/http.html#httprequestoptions-callback) and [`http.createServer()`](https://nodejs.org/docs/latest/api/http.html#httpcreateserveroptions-requestlistener). See RFC 9110 Section 5.3 for more information.
  * `set-cookie` is always an array. Duplicates are added to the array.
  * For duplicate `cookie` headers, the values are joined together with `; `.
  * For all other headers, the values are joined together with `, `.


####  `message.headersDistinct`[#](https://nodejs.org/docs/latest/api/http.html#messageheadersdistinct)
Added in: v18.3.0, v16.17.0
  * Type:


Similar to [`message.headers`](https://nodejs.org/docs/latest/api/http.html#messageheaders), but there is no join logic and the values are always arrays of strings, even for headers received just once.
```
// Prints something like:
//
// { 'user-agent': ['curl/7.22.0'],
//   host: ['127.0.0.1:8000'],
//   accept: ['*/*'] }
console.log(request.headersDistinct);
copy
```

####  `message.httpVersion`[#](https://nodejs.org/docs/latest/api/http.html#messagehttpversion)
Added in: v0.1.1
  * Type:


In case of server request, the HTTP version sent by the client. In the case of client response, the HTTP version of the connected-to server. Probably either `'1.1'` or `'1.0'`.
Also `message.httpVersionMajor` is the first integer and `message.httpVersionMinor` is the second.
####  `message.method`[#](https://nodejs.org/docs/latest/api/http.html#messagemethod)
Added in: v0.1.1
  * Type:


**Only valid for request obtained from[`http.Server`](https://nodejs.org/docs/latest/api/http.html#class-httpserver).**
The request method as a string. Read only. Examples: `'GET'`, `'DELETE'`.
####  `message.rawHeaders`[#](https://nodejs.org/docs/latest/api/http.html#messagerawheaders)
Added in: v0.11.6
  * Type:


The raw request/response headers list exactly as they were received.
The keys and values are in the same list. It is _not_ a list of tuples. So, the even-numbered offsets are key values, and the odd-numbered offsets are the associated values.
Header names are not lowercased, and duplicates are not merged.
```
// Prints something like:
//
// [ 'user-agent',
//   'this is invalid because there can be only one',
//   'User-Agent',
//   'curl/7.22.0',
//   'Host',
//   '127.0.0.1:8000',
//   'ACCEPT',
//   '*/*' ]
console.log(request.rawHeaders);
copy
```

####  `message.rawTrailers`[#](https://nodejs.org/docs/latest/api/http.html#messagerawtrailers)
Added in: v0.11.6
  * Type:


The raw request/response trailer keys and values exactly as they were received. Only populated at the `'end'` event.
####  `message.setTimeout(msecs[, callback])`[#](https://nodejs.org/docs/latest/api/http.html#messagesettimeoutmsecs-callback)
Added in: v0.5.9
  * `msecs`
  * `callback`
  * Returns: [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)


Calls `message.socket.setTimeout(msecs, callback)`.
####  `message.socket`[#](https://nodejs.org/docs/latest/api/http.html#messagesocket)
Added in: v0.3.0
  * Type: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


The [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) object associated with the connection.
With HTTPS support, use [`request.socket.getPeerCertificate()`](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetpeercertificatedetailed) to obtain the client's authentication details.
This property is guaranteed to be an instance of the [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) class, a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), unless the user specified a socket type other than [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) or internally nulled.
####  `message.statusCode`[#](https://nodejs.org/docs/latest/api/http.html#messagestatuscode)
Added in: v0.1.1
  * Type:


**Only valid for response obtained from[`http.ClientRequest`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest).**
The 3-digit HTTP response status code. E.G. `404`.
####  `message.statusMessage`[#](https://nodejs.org/docs/latest/api/http.html#messagestatusmessage)
Added in: v0.11.10
  * Type:


**Only valid for response obtained from[`http.ClientRequest`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest).**
The HTTP response status message (reason phrase). E.G. `OK` or `Internal Server Error`.
####  `message.trailers`[#](https://nodejs.org/docs/latest/api/http.html#messagetrailers)
Added in: v0.3.0
  * Type:


The request/response trailers object. Only populated at the `'end'` event.
####  `message.trailersDistinct`[#](https://nodejs.org/docs/latest/api/http.html#messagetrailersdistinct)
Added in: v18.3.0, v16.17.0
  * Type:


Similar to [`message.trailers`](https://nodejs.org/docs/latest/api/http.html#messagetrailers), but there is no join logic and the values are always arrays of strings, even for headers received just once. Only populated at the `'end'` event.
####  `message.url`[#](https://nodejs.org/docs/latest/api/http.html#messageurl)
Added in: v0.1.90
  * Type:


**Only valid for request obtained from[`http.Server`](https://nodejs.org/docs/latest/api/http.html#class-httpserver).**
Request URL string. This contains only the URL that is present in the actual HTTP request. Take the following request:
```
GET /status?name=ryan HTTP/1.1
Accept: text/plain
copy
```

To parse the URL into its parts:
```
new URL(`http://${process.env.HOST ?? 'localhost'}${request.url}`);
copy
```

When `request.url` is `'/status?name=ryan'` and `process.env.HOST` is undefined:
```
$ node
> new URL(`http://${process.env.HOST ?? 'localhost'}${request.url}`);
URL {
  href: 'http://localhost/status?name=ryan',
  origin: 'http://localhost',
  protocol: 'http:',
  username: '',
  password: '',
  host: 'localhost',
  hostname: 'localhost',
  port: '',
  pathname: '/status',
  search: '?name=ryan',
  searchParams: URLSearchParams { 'name' => 'ryan' },
  hash: ''
}
copy
```

Ensure that you set `process.env.HOST` to the server's host name, or consider replacing this part entirely. If using `req.headers.host`, ensure proper validation is used, as clients may specify a custom `Host` header.
### Class: `http.OutgoingMessage`[#](https://nodejs.org/docs/latest/api/http.html#class-httpoutgoingmessage)
Added in: v0.1.17
  * Extends: [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream)


This class serves as the parent class of [`http.ClientRequest`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest) and [`http.ServerResponse`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse). It is an abstract outgoing message from the perspective of the participants of an HTTP transaction.
#### Event: `'drain'`[#](https://nodejs.org/docs/latest/api/http.html#event-drain)
Added in: v0.3.6
Emitted when the buffer of the message is free again.
#### Event: `'finish'`[#](https://nodejs.org/docs/latest/api/http.html#event-finish-2)
Added in: v0.1.17
Emitted when the transmission is finished successfully.
#### Event: `'prefinish'`[#](https://nodejs.org/docs/latest/api/http.html#event-prefinish)
Added in: v0.11.6
Emitted after `outgoingMessage.end()` is called. When the event is emitted, all data has been processed but not necessarily completely flushed.
####  `outgoingMessage.addTrailers(headers)`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessageaddtrailersheaders)
Added in: v0.3.0
  * `headers`


Adds HTTP trailers (headers but at the end of the message) to the message.
Trailers will **only** be emitted if the message is chunked encoded. If not, the trailers will be silently discarded.
HTTP requires the `Trailer` header to be sent to emit trailers, with a list of header field names in its value, e.g.
```
message.writeHead(200, { 'Content-Type': 'text/plain',
                         'Trailer': 'Content-MD5' });
message.write(fileData);
message.addTrailers({ 'Content-MD5': '7895bf4b8828b55ceaf47747b4bca667' });
message.end();
copy
```

Attempting to set a header field name or value that contains invalid characters will result in a `TypeError` being thrown.
