copy
```

Once the client receives the `SETTINGS` frame from the server indicating that the extended CONNECT may be used, it may send `CONNECT` requests that use the `':protocol'` HTTP/2 pseudo-header:
```
import { connect } from 'node:http2';
const client = connect('http://localhost:8080');
client.on('remoteSettings', (settings) => {
  if (settings.enableConnectProtocol) {
    const req = client.request({ ':method': 'CONNECT', ':protocol': 'foo' });
    // ...
  }
});
const http2 = require('node:http2');
const client = http2.connect('http://localhost:8080');
client.on('remoteSettings', (settings) => {
  if (settings.enableConnectProtocol) {
    const req = client.request({ ':method': 'CONNECT', ':protocol': 'foo' });
    // ...
  }
});
copy
```

### Compatibility API[#](https://nodejs.org/docs/latest/api/http2.html#compatibility-api)
The Compatibility API has the goal of providing a similar developer experience of HTTP/1 when using HTTP/2, making it possible to develop applications that support both [HTTP/1](https://nodejs.org/docs/latest/api/http.html) and HTTP/2. This API targets only the **public API** of the [HTTP/1](https://nodejs.org/docs/latest/api/http.html). However many modules use internal methods or state, and those _are not supported_ as it is a completely different implementation.
The following example creates an HTTP/2 server using the compatibility API:
```
import { createServer } from 'node:http2';
const server = createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html');
  res.setHeader('X-Foo', 'bar');
  res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
  res.end('ok');
});
const http2 = require('node:http2');
const server = http2.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html');
  res.setHeader('X-Foo', 'bar');
  res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
  res.end('ok');
});
copy
```

In order to create a mixed [HTTPS](https://nodejs.org/docs/latest/api/https.html) and HTTP/2 server, refer to the [ALPN negotiation](https://nodejs.org/docs/latest/api/http2.html#alpn-negotiation) section. Upgrading from non-tls HTTP/1 servers is not supported.
The HTTP/2 compatibility API is composed of [`Http2ServerRequest`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverrequest) and [`Http2ServerResponse`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverresponse). They aim at API compatibility with HTTP/1, but they do not hide the differences between the protocols. As an example, the status message for HTTP codes is ignored.
#### ALPN negotiation[#](https://nodejs.org/docs/latest/api/http2.html#alpn-negotiation)
ALPN negotiation allows supporting both [HTTPS](https://nodejs.org/docs/latest/api/https.html) and HTTP/2 over the same socket. The `req` and `res` objects can be either HTTP/1 or HTTP/2, and an application **must** restrict itself to the public API of [HTTP/1](https://nodejs.org/docs/latest/api/http.html), and detect if it is possible to use the more advanced features of HTTP/2.
The following example creates a server that supports both protocols:
```
import { createSecureServer } from 'node:http2';
import { readFileSync } from 'node:fs';

const cert = readFileSync('./cert.pem');
const key = readFileSync('./key.pem');

const server = createSecureServer(
  { cert, key, allowHTTP1: true },
  onRequest,
).listen(8000);

function onRequest(req, res) {
  // Detects if it is a HTTPS request or HTTP/2
  const { socket: { alpnProtocol } } = req.httpVersion === '2.0' ?
    req.stream.session : req;
  res.writeHead(200, { 'content-type': 'application/json' });
  res.end(JSON.stringify({
    alpnProtocol,
    httpVersion: req.httpVersion,
  }));
}
const { createSecureServer } = require('node:http2');
const { readFileSync } = require('node:fs');

const cert = readFileSync('./cert.pem');
const key = readFileSync('./key.pem');

const server = createSecureServer(
  { cert, key, allowHTTP1: true },
  onRequest,
).listen(4443);

function onRequest(req, res) {
  // Detects if it is a HTTPS request or HTTP/2
  const { socket: { alpnProtocol } } = req.httpVersion === '2.0' ?
    req.stream.session : req;
  res.writeHead(200, { 'content-type': 'application/json' });
  res.end(JSON.stringify({
    alpnProtocol,
    httpVersion: req.httpVersion,
  }));
}
copy
```

The `'request'` event works identically on both [HTTPS](https://nodejs.org/docs/latest/api/https.html) and HTTP/2.
#### Class: `http2.Http2ServerRequest`[#](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverrequest)
Added in: v8.4.0
  * Extends: [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable)


A `Http2ServerRequest` object is created by [`http2.Server`](https://nodejs.org/docs/latest/api/http2.html#class-http2server) or [`http2.SecureServer`](https://nodejs.org/docs/latest/api/http2.html#class-http2secureserver) and passed as the first argument to the [`'request'`](https://nodejs.org/docs/latest/api/http2.html#event-request) event. It may be used to access a request status, headers, and data.
##### Event: `'aborted'`[#](https://nodejs.org/docs/latest/api/http2.html#event-aborted-1)
Added in: v8.4.0
The `'aborted'` event is emitted whenever a `Http2ServerRequest` instance is abnormally aborted in mid-communication.
The `'aborted'` event will only be emitted if the `Http2ServerRequest` writable side has not been ended.
##### Event: `'close'`[#](https://nodejs.org/docs/latest/api/http2.html#event-close-2)
Added in: v8.4.0
Indicates that the underlying [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) was closed. Just like `'end'`, this event occurs only once per response.
#####  `request.aborted`[#](https://nodejs.org/docs/latest/api/http2.html#requestaborted)
Added in: v10.1.0
  * Type:


The `request.aborted` property will be `true` if the request has been aborted.
#####  `request.authority`[#](https://nodejs.org/docs/latest/api/http2.html#requestauthority)
Added in: v8.4.0
  * Type:


The request authority pseudo header field. Because HTTP/2 allows requests to set either `:authority` or `host`, this value is derived from `req.headers[':authority']` if present. Otherwise, it is derived from `req.headers['host']`.
#####  `request.complete`[#](https://nodejs.org/docs/latest/api/http2.html#requestcomplete)
Added in: v12.10.0
  * Type:


The `request.complete` property will be `true` if the request has been completed, aborted, or destroyed.
#####  `request.connection`[#](https://nodejs.org/docs/latest/api/http2.html#requestconnection)
Added in: v8.4.0Deprecated in: v13.0.0
Stability: 0 - Deprecated. Use [`request.socket`](https://nodejs.org/docs/latest/api/http2.html#requestsocket).
  * Type: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) | [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket)


See [`request.socket`](https://nodejs.org/docs/latest/api/http2.html#requestsocket).
#####  `request.destroy([error])`[#](https://nodejs.org/docs/latest/api/http2.html#requestdestroyerror)
Added in: v8.4.0
  * `error`


Calls `destroy()` on the [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) that received the [`Http2ServerRequest`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverrequest). If `error` is provided, an `'error'` event is emitted and `error` is passed as an argument to any listeners on the event.
It does nothing if the stream was already destroyed.
#####  `request.headers`[#](https://nodejs.org/docs/latest/api/http2.html#requestheaders)
Added in: v8.4.0
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

See [HTTP/2 Headers Object](https://nodejs.org/docs/latest/api/http2.html#headers-object).
In HTTP/2, the request path, host name, protocol, and method are represented as special headers prefixed with the `:` character (e.g. `':path'`). These special headers will be included in the `request.headers` object. Care must be taken not to inadvertently modify these special headers or errors may occur. For instance, removing all headers from the request will cause errors to occur:
```
removeAllHeaders(request.headers);
assert(request.url);   // Fails because the :path header has been removed
copy
```

#####  `request.httpVersion`[#](https://nodejs.org/docs/latest/api/http2.html#requesthttpversion)
Added in: v8.4.0
  * Type:


In case of server request, the HTTP version sent by the client. In the case of client response, the HTTP version of the connected-to server. Returns `'2.0'`.
Also `message.httpVersionMajor` is the first integer and `message.httpVersionMinor` is the second.
#####  `request.method`[#](https://nodejs.org/docs/latest/api/http2.html#requestmethod)
Added in: v8.4.0
  * Type:


The request method as a string. Read-only. Examples: `'GET'`, `'DELETE'`.
#####  `request.rawHeaders`[#](https://nodejs.org/docs/latest/api/http2.html#requestrawheaders)
Added in: v8.4.0
  * Type: {HTTP/2 Raw Headers}


The raw request/response headers list exactly as they were received.
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

#####  `request.rawTrailers`[#](https://nodejs.org/docs/latest/api/http2.html#requestrawtrailers)
Added in: v8.4.0
  * Type:


The raw request/response trailer keys and values exactly as they were received. Only populated at the `'end'` event.
#####  `request.scheme`[#](https://nodejs.org/docs/latest/api/http2.html#requestscheme)
Added in: v8.4.0
  * Type:


The request scheme pseudo header field indicating the scheme portion of the target URL.
#####  `request.setTimeout(msecs, callback)`[#](https://nodejs.org/docs/latest/api/http2.html#requestsettimeoutmsecs-callback)
Added in: v8.4.0
  * `msecs`
  * `callback`
  * Returns: [`<http2.Http2ServerRequest>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverrequest)


Sets the [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream)'s timeout value to `msecs`. If a callback is provided, then it is added as a listener on the `'timeout'` event on the response object.
If no `'timeout'` listener is added to the request, the response, or the server, then [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream)s are destroyed when they time out. If a handler is assigned to the request, the response, or the server's `'timeout'` events, timed out sockets must be handled explicitly.
#####  `request.socket`[#](https://nodejs.org/docs/latest/api/http2.html#requestsocket)
Added in: v8.4.0
  * Type: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) | [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket)


Returns a `Proxy` object that acts as a `net.Socket` (or `tls.TLSSocket`) but applies getters, setters, and methods based on HTTP/2 logic.
`destroyed`, `readable`, and `writable` properties will be retrieved from and set on `request.stream`.
`destroy`, `emit`, `end`, `on` and `once` methods will be called on `request.stream`.
`setTimeout` method will be called on `request.stream.session`.
`pause`, `read`, `resume`, and `write` will throw an error with code `ERR_HTTP2_NO_SOCKET_MANIPULATION`. See [`Http2Session` and Sockets](https://nodejs.org/docs/latest/api/http2.html#http2session-and-sockets) for more information.
All other interactions will be routed directly to the socket. With TLS support, use [`request.socket.getPeerCertificate()`](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetpeercertificatedetailed) to obtain the client's authentication details.
#####  `request.stream`[#](https://nodejs.org/docs/latest/api/http2.html#requeststream)
Added in: v8.4.0
  * Type: [`<Http2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream)


The [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) object backing the request.
#####  `request.trailers`[#](https://nodejs.org/docs/latest/api/http2.html#requesttrailers)
Added in: v8.4.0
  * Type:


The request/response trailers object. Only populated at the `'end'` event.
#####  `request.url`[#](https://nodejs.org/docs/latest/api/http2.html#requesturl)
Added in: v8.4.0
  * Type:


Request URL string. This contains only the URL that is present in the actual HTTP request. If the request is:
```
GET /status?name=ryan HTTP/1.1
Accept: text/plain
copy
```

Then `request.url` will be:
```
'/status?name=ryan'
copy
```

To parse the url into its parts, `new URL()` can be used:
```
$ node
> new URL('/status?name=ryan', 'http://example.com')
URL {
  href: 'http://example.com/status?name=ryan',
  origin: 'http://example.com',
  protocol: 'http:',
  username: '',
  password: '',
  host: 'example.com',
  hostname: 'example.com',
  port: '',
  pathname: '/status',
  search: '?name=ryan',
  searchParams: URLSearchParams { 'name' => 'ryan' },
  hash: ''
}
copy
```

#### Class: `http2.Http2ServerResponse`[#](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverresponse)
Added in: v8.4.0
  * Extends: [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream)


This object is created internally by an HTTP server, not by the user. It is passed as the second parameter to the [`'request'`](https://nodejs.org/docs/latest/api/http2.html#event-request) event.
##### Event: `'close'`[#](https://nodejs.org/docs/latest/api/http2.html#event-close-3)
Added in: v8.4.0
Indicates that the underlying [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) was terminated before [`response.end()`](https://nodejs.org/docs/latest/api/http2.html#responseenddata-encoding-callback) was called or able to flush.
##### Event: `'finish'`[#](https://nodejs.org/docs/latest/api/http2.html#event-finish)
Added in: v8.4.0
Emitted when the response has been sent. More specifically, this event is emitted when the last segment of the response headers and body have been handed off to the HTTP/2 multiplexing for transmission over the network. It does not imply that the client has received anything yet.
After this event, no more events will be emitted on the response object.
#####  `response.addTrailers(headers)`[#](https://nodejs.org/docs/latest/api/http2.html#responseaddtrailersheaders)
Added in: v8.4.0
  * `headers`


This method adds HTTP trailing headers (a header but at the end of the message) to the response.
Attempting to set a header field name or value that contains invalid characters will result in a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) being thrown.
#####  `response.appendHeader(name, value)`[#](https://nodejs.org/docs/latest/api/http2.html#responseappendheadername-value)
Added in: v21.7.0, v20.12.0
  * `name`
  * `value`


Append a single header value to the header object.
If the value is an array, this is equivalent to calling this method multiple times.
If there were no previous values for the header, this is equivalent to calling [`response.setHeader()`](https://nodejs.org/docs/latest/api/http2.html#responsesetheadername-value).
Attempting to set a header field name or value that contains invalid characters will result in a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) being thrown.
```
// Returns headers including "set-cookie: a" and "set-cookie: b"
const server = http2.createServer((req, res) => {
  res.setHeader('set-cookie', 'a');
  res.appendHeader('set-cookie', 'b');
  res.writeHead(200);
  res.end('ok');
});
copy
```

#####  `response.connection`[#](https://nodejs.org/docs/latest/api/http2.html#responseconnection)
Added in: v8.4.0Deprecated in: v13.0.0
Stability: 0 - Deprecated. Use [`response.socket`](https://nodejs.org/docs/latest/api/http2.html#responsesocket).
  * Type: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) | [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket)


See [`response.socket`](https://nodejs.org/docs/latest/api/http2.html#responsesocket).
#####  `response.createPushResponse(headers, callback)`[#](https://nodejs.org/docs/latest/api/http2.html#responsecreatepushresponseheaders-callback)
Added in: v8.4.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object) An object describing the headers
  * `callback` `http2stream.pushStream()` is finished, or either when the attempt to create the pushed `Http2Stream` has failed or has been rejected, or the state of `Http2ServerRequest` is closed prior to calling the `http2stream.pushStream()` method
    * `err`
    * `res` [`<http2.Http2ServerResponse>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverresponse) The newly-created `Http2ServerResponse` object


Call [`http2stream.pushStream()`](https://nodejs.org/docs/latest/api/http2.html#http2streampushstreamheaders-options-callback) with the given headers, and wrap the given [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) on a newly created `Http2ServerResponse` as the callback parameter if successful. When `Http2ServerRequest` is closed, the callback is called with an error `ERR_HTTP2_INVALID_STREAM`.
#####  `response.end([data[, encoding]][, callback])`[#](https://nodejs.org/docs/latest/api/http2.html#responseenddata-encoding-callback)
Added in: v8.4.0History Version | Changes
---|---
v10.0.0 | This method now returns a reference to `ServerResponse`.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding`
  * `callback`
  * Returns:


This method signals to the server that all of the response headers and body have been sent; that server should consider this message complete. The method, `response.end()`, MUST be called on each response.
If `data` is specified, it is equivalent to calling [`response.write(data, encoding)`](https://nodejs.org/docs/latest/api/http.html#responsewritechunk-encoding-callback) followed by `response.end(callback)`.
If `callback` is specified, it will be called when the response stream is finished.
#####  `response.finished`[#](https://nodejs.org/docs/latest/api/http2.html#responsefinished)
Added in: v8.4.0Deprecated in: v13.4.0, v12.16.0
Stability: 0 - Deprecated. Use [`response.writableEnded`](https://nodejs.org/docs/latest/api/http2.html#responsewritableended).
  * Type:


Boolean value that indicates whether the response has completed. Starts as `false`. After [`response.end()`](https://nodejs.org/docs/latest/api/http2.html#responseenddata-encoding-callback) executes, the value will be `true`.
#####  `response.getHeader(name)`[#](https://nodejs.org/docs/latest/api/http2.html#responsegetheadername)
Added in: v8.4.0
  * `name`
  * Returns:


Reads out a header that has already been queued but not sent to the client. The name is case-insensitive.
```
const contentType = response.getHeader('content-type');
copy
```

#####  `response.getHeaderNames()`[#](https://nodejs.org/docs/latest/api/http2.html#responsegetheadernames)
Added in: v8.4.0
  * Returns:


Returns an array containing the unique names of the current outgoing headers. All header names are lowercase.
```
response.setHeader('Foo', 'bar');
response.setHeader('Set-Cookie', ['foo=bar', 'bar=baz']);

const headerNames = response.getHeaderNames();
// headerNames === ['foo', 'set-cookie']
copy
```

#####  `response.getHeaders()`[#](https://nodejs.org/docs/latest/api/http2.html#responsegetheaders)
Added in: v8.4.0
  * Returns:


Returns a shallow copy of the current outgoing headers. Since a shallow copy is used, array values may be mutated without additional calls to various header-related http module methods. The keys of the returned object are the header names and the values are the respective header values. All header names are lowercase.
The object returned by the `response.getHeaders()` method _does not_ prototypically inherit from the JavaScript `Object`. This means that typical `Object` methods such as `obj.toString()`, `obj.hasOwnProperty()`, and others are not defined and _will not work_.
```
response.setHeader('Foo', 'bar');
response.setHeader('Set-Cookie', ['foo=bar', 'bar=baz']);

const headers = response.getHeaders();
// headers === { foo: 'bar', 'set-cookie': ['foo=bar', 'bar=baz'] }
copy
```

#####  `response.hasHeader(name)`[#](https://nodejs.org/docs/latest/api/http2.html#responsehasheadername)
Added in: v8.4.0
  * `name`
  * Returns:


Returns `true` if the header identified by `name` is currently set in the outgoing headers. The header name matching is case-insensitive.
```
const hasContentType = response.hasHeader('content-type');
copy
```

#####  `response.headersSent`[#](https://nodejs.org/docs/latest/api/http2.html#responseheaderssent)
Added in: v8.4.0
  * Type:


True if headers were sent, false otherwise (read-only).
#####  `response.removeHeader(name)`[#](https://nodejs.org/docs/latest/api/http2.html#responseremoveheadername)
Added in: v8.4.0
  * `name`


Removes a header that has been queued for implicit sending.
```
response.removeHeader('Content-Encoding');
copy
```

#####  `response.req`[#](https://nodejs.org/docs/latest/api/http2.html#responsereq)
Added in: v15.7.0
  * Type: [`<http2.Http2ServerRequest>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverrequest)


A reference to the original HTTP2 `request` object.
#####  `response.sendDate`[#](https://nodejs.org/docs/latest/api/http2.html#responsesenddate)
Added in: v8.4.0
  * Type:


When true, the Date header will be automatically generated and sent in the response if it is not already present in the headers. Defaults to true.
This should only be disabled for testing; HTTP requires the Date header in responses.
#####  `response.setHeader(name, value)`[#](https://nodejs.org/docs/latest/api/http2.html#responsesetheadername-value)
Added in: v8.4.0
  * `name`
  * `value`


Sets a single header value for implicit headers. If this header already exists in the to-be-sent headers, its value will be replaced. Use an array of strings here to send multiple headers with the same name.
```
response.setHeader('Content-Type', 'text/html; charset=utf-8');
copy
```

or
```
response.setHeader('Set-Cookie', ['type=ninja', 'language=javascript']);
copy
```

Attempting to set a header field name or value that contains invalid characters will result in a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) being thrown.
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

#####  `response.setTimeout(msecs[, callback])`[#](https://nodejs.org/docs/latest/api/http2.html#responsesettimeoutmsecs-callback)
Added in: v8.4.0
  * `msecs`
  * `callback`
  * Returns: [`<http2.Http2ServerResponse>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverresponse)


Sets the [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream)'s timeout value to `msecs`. If a callback is provided, then it is added as a listener on the `'timeout'` event on the response object.
If no `'timeout'` listener is added to the request, the response, or the server, then [`Http2Stream`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream)s are destroyed when they time out. If a handler is assigned to the request, the response, or the server's `'timeout'` events, timed out sockets must be handled explicitly.
#####  `response.socket`[#](https://nodejs.org/docs/latest/api/http2.html#responsesocket)
Added in: v8.4.0
  * Type: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) | [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket)


Returns a `Proxy` object that acts as a `net.Socket` (or `tls.TLSSocket`) but applies getters, setters, and methods based on HTTP/2 logic.
`destroyed`, `readable`, and `writable` properties will be retrieved from and set on `response.stream`.
`destroy`, `emit`, `end`, `on` and `once` methods will be called on `response.stream`.
`setTimeout` method will be called on `response.stream.session`.
`pause`, `read`, `resume`, and `write` will throw an error with code `ERR_HTTP2_NO_SOCKET_MANIPULATION`. See [`Http2Session` and Sockets](https://nodejs.org/docs/latest/api/http2.html#http2session-and-sockets) for more information.
