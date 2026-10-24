  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) Network socket between the server and client
  * `head` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The first packet of the tunneling stream (may be empty)


Emitted each time a client requests an HTTP `CONNECT` method. If this event is not listened for, then clients requesting a `CONNECT` method will have their connections closed.
This event is guaranteed to be passed an instance of the [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) class, a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), unless the user specifies a socket type other than [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
After this event is emitted, the request's socket will not have a `'data'` event listener, meaning it will need to be bound in order to handle data sent to the server on that socket.
#### Event: `'connection'`[#](https://nodejs.org/docs/latest/api/http.html#event-connection)
Added in: v0.1.0
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


This event is emitted when a new TCP stream is established. `socket` is typically an object of type [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket). Usually users will not want to access this event. In particular, the socket will not emit `'readable'` events because of how the protocol parser attaches to the socket. The `socket` can also be accessed at `request.socket`.
This event can also be explicitly emitted by users to inject connections into the HTTP server. In that case, any [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) stream can be passed.
If `socket.setTimeout()` is called here, the timeout will be replaced with `server.keepAliveTimeout` when the socket has served a request (if `server.keepAliveTimeout` is non-zero).
This event is guaranteed to be passed an instance of the [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) class, a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), unless the user specifies a socket type other than [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
#### Event: `'dropRequest'`[#](https://nodejs.org/docs/latest/api/http.html#event-droprequest)
Added in: v18.7.0, v16.17.0
  * `request` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage) Arguments for the HTTP request, as it is in the [`'request'`](https://nodejs.org/docs/latest/api/http.html#event-request) event
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) Network socket between the server and client


When the number of requests on a socket reaches the threshold of `server.maxRequestsPerSocket`, the server will drop new requests and emit `'dropRequest'` event instead, then send `503` to client.
#### Event: `'request'`[#](https://nodejs.org/docs/latest/api/http.html#event-request)
Added in: v0.1.0
  * `request` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
  * `response` [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)


Emitted each time there is a request. There may be multiple requests per connection (in the case of HTTP Keep-Alive connections).
#### Event: `'upgrade'`[#](https://nodejs.org/docs/latest/api/http.html#event-upgrade-1)
Added in: v0.1.94History Version | Changes
---|---
v24.9.0 | Whether this event is fired can now be controlled by the `shouldUpgradeCallback` and sockets will be destroyed if upgraded while no event handler is listening.
v10.0.0 | Not listening to this event no longer causes the socket to be destroyed if a client sends an Upgrade header.
  * `request` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage) Arguments for the HTTP request, as it is in the [`'request'`](https://nodejs.org/docs/latest/api/http.html#event-request) event
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) Network socket between the server and client
  * `head` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The first packet of the upgraded stream (may be empty)


Emitted each time a client's HTTP upgrade request is accepted. By default all HTTP upgrade requests are ignored (i.e. only regular `'request'` events are emitted, sticking with the normal HTTP request/response flow) unless you listen to this event, in which case they are all accepted (i.e. the `'upgrade'` event is emitted instead, and future communication must handled directly through the raw socket). You can control this more precisely by using the server `shouldUpgradeCallback` option.
Listening to this event is optional and clients cannot insist on a protocol change.
After this event is emitted, the request's socket will not have a `'data'` event listener, meaning it will need to be bound in order to handle data sent to the server on that socket.
If an upgrade is accepted by `shouldUpgradeCallback` but no event handler is registered then the socket is destroyed, resulting in an immediate connection closure for the client.
This event is guaranteed to be passed an instance of the [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) class, a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), unless the user specifies a socket type other than [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
####  `server.close([callback])`[#](https://nodejs.org/docs/latest/api/http.html#serverclosecallback)
Added in: v0.1.90History Version | Changes
---|---
v19.0.0 | The method closes idle connections before returning.
  * `callback`


Stops the server from accepting new connections and closes all connections connected to this server which are not sending a request or waiting for a response. See [`net.Server.close()`](https://nodejs.org/docs/latest/api/net.html#serverclosecallback).
```
const http = require('node:http');

const server = http.createServer({ keepAliveTimeout: 60000 }, (req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    data: 'Hello World!',
  }));
});

server.listen(8000);
// Close the server after 10 seconds
setTimeout(() => {
  server.close(() => {
    console.log('server on port 8000 closed successfully');
  });
}, 10000);
copy
```

####  `server.closeAllConnections()`[#](https://nodejs.org/docs/latest/api/http.html#servercloseallconnections)
Added in: v18.2.0
Closes all established HTTP(S) connections connected to this server, including active connections connected to this server which are sending a request or waiting for a response. This does _not_ destroy sockets upgraded to a different protocol, such as WebSocket or HTTP/2.
> This is a forceful way of closing all connections and should be used with caution. Whenever using this in conjunction with `server.close`, calling this _after_ `server.close` is recommended as to avoid race conditions where new connections are created between a call to this and a call to `server.close`.
```
const http = require('node:http');

const server = http.createServer({ keepAliveTimeout: 60000 }, (req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    data: 'Hello World!',
  }));
});

server.listen(8000);
// Close the server after 10 seconds
setTimeout(() => {
  server.close(() => {
    console.log('server on port 8000 closed successfully');
  });
  // Closes all connections, ensuring the server closes successfully
  server.closeAllConnections();
}, 10000);
copy
```

####  `server.closeIdleConnections()`[#](https://nodejs.org/docs/latest/api/http.html#servercloseidleconnections)
Added in: v18.2.0
Closes all connections connected to this server which are not sending a request or waiting for a response.
> Starting with Node.js 19.0.0, there's no need for calling this method in conjunction with `server.close` to reap `keep-alive` connections. Using it won't cause any harm though, and it can be useful to ensure backwards compatibility for libraries and applications that need to support versions older than 19.0.0. Whenever using this in conjunction with `server.close`, calling this _after_ `server.close` is recommended as to avoid race conditions where new connections are created between a call to this and a call to `server.close`.
```
const http = require('node:http');

const server = http.createServer({ keepAliveTimeout: 60000 }, (req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    data: 'Hello World!',
  }));
});

server.listen(8000);
// Close the server after 10 seconds
setTimeout(() => {
  server.close(() => {
    console.log('server on port 8000 closed successfully');
  });
  // Closes idle connections, such as keep-alive connections. Server will close
  // once remaining active connections are terminated
  server.closeIdleConnections();
}, 10000);
copy
```

####  `server.headersTimeout`[#](https://nodejs.org/docs/latest/api/http.html#serverheaderstimeout)
Added in: v11.3.0, v10.14.0History Version | Changes
---|---
v19.4.0, v18.14.0 | The default is now set to the minimum between 60000 (60 seconds) or `requestTimeout`.
  * Type: **Default:** The minimum between [`server.requestTimeout`](https://nodejs.org/docs/latest/api/http.html#serverrequesttimeout) or `60000`.


Limit the amount of time the parser will wait to receive the complete HTTP headers.
If the timeout expires, the server responds with status 408 without forwarding the request to the request listener and then closes the connection.
It must be set to a non-zero value (e.g. 120 seconds) to protect against potential Denial-of-Service attacks in case the server is deployed without a reverse proxy in front.
####  `server.listen()`[#](https://nodejs.org/docs/latest/api/http.html#serverlisten)
Starts the HTTP server listening for connections. This method is identical to [`server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) from [`net.Server`](https://nodejs.org/docs/latest/api/net.html#class-netserver).
####  `server.listening`[#](https://nodejs.org/docs/latest/api/http.html#serverlistening)
Added in: v5.7.0
  * Type:


####  `server.maxHeadersCount`[#](https://nodejs.org/docs/latest/api/http.html#servermaxheaderscount)
Added in: v0.7.0
  * Type: **Default:** `2000`


Limits maximum incoming headers count. If set to 0, no limit will be applied.
####  `server.requestTimeout`[#](https://nodejs.org/docs/latest/api/http.html#serverrequesttimeout)
Added in: v14.11.0History Version | Changes
---|---
v18.0.0 | The default request timeout changed from no timeout to 300s (5 minutes).
  * Type: **Default:** `300000`


Sets the timeout value in milliseconds for receiving the entire request from the client.
If the timeout expires, the server responds with status 408 without forwarding the request to the request listener and then closes the connection.
It must be set to a non-zero value (e.g. 120 seconds) to protect against potential Denial-of-Service attacks in case the server is deployed without a reverse proxy in front.
####  `server.setTimeout([msecs][, callback])`[#](https://nodejs.org/docs/latest/api/http.html#serversettimeoutmsecs-callback)
Added in: v0.9.12History Version | Changes
---|---
v13.0.0 | The default timeout changed from 120s to 0 (no timeout).
  * `msecs` **Default:** 0 (no timeout)
  * `callback`
  * Returns: [`<http.Server>`](https://nodejs.org/docs/latest/api/http.html#class-httpserver)


Sets the timeout value for sockets, and emits a `'timeout'` event on the Server object, passing the socket as an argument, if a timeout occurs.
If there is a `'timeout'` event listener on the Server object, then it will be called with the timed-out socket as an argument.
By default, the Server does not timeout sockets. However, if a callback is assigned to the Server's `'timeout'` event, timeouts must be handled explicitly.
####  `server.maxRequestsPerSocket`[#](https://nodejs.org/docs/latest/api/http.html#servermaxrequestspersocket)
Added in: v16.10.0
  * Type: **Default:** 0 (no limit)


The maximum number of requests socket can handle before closing keep alive connection.
A value of `0` will disable the limit.
When the limit is reached it will set the `Connection` header value to `close`, but will not actually close the connection, subsequent requests sent after the limit is reached will get `503 Service Unavailable` as a response.
####  `server.timeout`[#](https://nodejs.org/docs/latest/api/http.html#servertimeout)
Added in: v0.9.12History Version | Changes
---|---
v13.0.0 | The default timeout changed from 120s to 0 (no timeout).
  * Type: **Default:** 0 (no timeout)


The number of milliseconds of inactivity before a socket is presumed to have timed out.
A value of `0` will disable the timeout behavior on incoming connections.
The socket timeout logic is set up on connection, so changing this value only affects new connections to the server, not any existing connections.
####  `server.keepAliveTimeout`[#](https://nodejs.org/docs/latest/api/http.html#serverkeepalivetimeout)
Added in: v8.0.0
  * Type: **Default:** `5000` (5 seconds).


The number of milliseconds of inactivity a server needs to wait for additional incoming data, after it has finished writing the last response, before a socket will be destroyed.
This timeout value is combined with the [`server.keepAliveTimeoutBuffer`](https://nodejs.org/docs/latest/api/http.html#serverkeepalivetimeoutbuffer) option to determine the actual socket timeout, calculated as: socketTimeout = keepAliveTimeout + keepAliveTimeoutBuffer If the server receives new data before the keep-alive timeout has fired, it will reset the regular inactivity timeout, i.e., [`server.timeout`](https://nodejs.org/docs/latest/api/http.html#servertimeout).
A value of `0` will disable the keep-alive timeout behavior on incoming connections. A value of `0` makes the HTTP server behave similarly to Node.js versions prior to 8.0.0, which did not have a keep-alive timeout.
The socket timeout logic is set up on connection, so changing this value only affects new connections to the server, not any existing connections.
####  `server.keepAliveTimeoutBuffer`[#](https://nodejs.org/docs/latest/api/http.html#serverkeepalivetimeoutbuffer)
Added in: v24.6.0, v22.19.0
  * Type: **Default:** `1000` (1 second).


An additional buffer time added to the [`server.keepAliveTimeout`](https://nodejs.org/docs/latest/api/http.html#serverkeepalivetimeout) to extend the internal socket timeout.
This buffer helps reduce connection reset (`ECONNRESET`) errors by increasing the socket timeout slightly beyond the advertised keep-alive timeout.
This option applies only to new incoming connections.
####  `server[Symbol.asyncDispose]()`[#](https://nodejs.org/docs/latest/api/http.html#serversymbolasyncdispose)
Added in: v20.4.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Calls [`server.close()`](https://nodejs.org/docs/latest/api/http.html#serverclosecallback) and returns a promise that fulfills when the server has closed.
### Class: `http.ServerResponse`[#](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)
Added in: v0.1.17
  * Extends: [`<http.OutgoingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpoutgoingmessage)


This object is created internally by an HTTP server, not by the user. It is passed as the second parameter to the [`'request'`](https://nodejs.org/docs/latest/api/http.html#event-request) event.
#### Event: `'close'`[#](https://nodejs.org/docs/latest/api/http.html#event-close-2)
Added in: v0.6.7
Indicates that the response is completed, or its underlying connection was terminated prematurely (before the response completion).
#### Event: `'finish'`[#](https://nodejs.org/docs/latest/api/http.html#event-finish-1)
Added in: v0.3.6
Emitted when the response has been sent. More specifically, this event is emitted when the last segment of the response headers and body have been handed off to the operating system for transmission over the network. It does not imply that the client has received anything yet.
####  `response.addTrailers(headers)`[#](https://nodejs.org/docs/latest/api/http.html#responseaddtrailersheaders)
Added in: v0.3.0
  * `headers`


This method adds HTTP trailing headers (a header but at the end of the message) to the response.
Trailers will **only** be emitted if chunked encoding is used for the response; if it is not (e.g. if the request was HTTP/1.0), they will be silently discarded.
HTTP requires the `Trailer` header to be sent in order to emit trailers, with a list of the header fields in its value. E.g.,
```
response.writeHead(200, { 'Content-Type': 'text/plain',
                          'Trailer': 'Content-MD5' });
response.write(fileData);
response.addTrailers({ 'Content-MD5': '7895bf4b8828b55ceaf47747b4bca667' });
response.end();
copy
```

Attempting to set a header field name or value that contains invalid characters will result in a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) being thrown.
####  `response.connection`[#](https://nodejs.org/docs/latest/api/http.html#responseconnection)
Added in: v0.3.0Deprecated in: v13.0.0
Stability: 0 - Deprecated. Use [`response.socket`](https://nodejs.org/docs/latest/api/http.html#responsesocket).
  * Type: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


See [`response.socket`](https://nodejs.org/docs/latest/api/http.html#responsesocket).
####  `response.cork()`[#](https://nodejs.org/docs/latest/api/http.html#responsecork)
Added in: v13.2.0, v12.16.0
See [`writable.cork()`](https://nodejs.org/docs/latest/api/stream.html#writablecork).
####  `response.end([data[, encoding]][, callback])`[#](https://nodejs.org/docs/latest/api/http.html#responseenddata-encoding-callback)
Added in: v0.1.90History Version | Changes
---|---
v15.0.0 | The `data` parameter can now be a `Uint8Array`.
v10.0.0 | This method now returns a reference to `ServerResponse`.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding`
  * `callback`
  * Returns:


This method signals to the server that all of the response headers and body have been sent; that server should consider this message complete. The method, `response.end()`, MUST be called on each response.
If `data` is specified, it is similar in effect to calling [`response.write(data, encoding)`](https://nodejs.org/docs/latest/api/http.html#responsewritechunk-encoding-callback) followed by `response.end(callback)`.
If `callback` is specified, it will be called when the response stream is finished.
####  `response.finished`[#](https://nodejs.org/docs/latest/api/http.html#responsefinished)
Added in: v0.0.2Deprecated in: v13.4.0, v12.16.0
Stability: 0 - Deprecated. Use [`response.writableEnded`](https://nodejs.org/docs/latest/api/http.html#responsewritableended).
  * Type:


The `response.finished` property will be `true` if [`response.end()`](https://nodejs.org/docs/latest/api/http.html#responseenddata-encoding-callback) has been called.
####  `response.flushHeaders()`[#](https://nodejs.org/docs/latest/api/http.html#responseflushheaders)
Added in: v1.6.0
Flushes the response headers. See also: [`request.flushHeaders()`](https://nodejs.org/docs/latest/api/http.html#requestflushheaders).
####  `response.getHeader(name)`[#](https://nodejs.org/docs/latest/api/http.html#responsegetheadername)
Added in: v0.4.0
  * `name`
  * Returns:


Reads out a header that's already been queued but not sent to the client. The name is case-insensitive. The type of the return value depends on the arguments provided to [`response.setHeader()`](https://nodejs.org/docs/latest/api/http.html#responsesetheadername-value).
```
response.setHeader('Content-Type', 'text/html');
response.setHeader('Content-Length', Buffer.byteLength(body));
response.setHeader('Set-Cookie', ['type=ninja', 'language=javascript']);
const contentType = response.getHeader('content-type');
// contentType is 'text/html'
const contentLength = response.getHeader('Content-Length');
// contentLength is of type number
const setCookie = response.getHeader('set-cookie');
// setCookie is of type string[]
copy
```

####  `response.getHeaderNames()`[#](https://nodejs.org/docs/latest/api/http.html#responsegetheadernames)
Added in: v7.7.0
  * Returns:


Returns an array containing the unique names of the current outgoing headers. All header names are lowercase.
```
response.setHeader('Foo', 'bar');
response.setHeader('Set-Cookie', ['foo=bar', 'bar=baz']);

const headerNames = response.getHeaderNames();
// headerNames === ['foo', 'set-cookie']
copy
```

####  `response.getHeaders()`[#](https://nodejs.org/docs/latest/api/http.html#responsegetheaders)
Added in: v7.7.0
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

####  `response.hasHeader(name)`[#](https://nodejs.org/docs/latest/api/http.html#responsehasheadername)
Added in: v7.7.0
  * `name`
  * Returns:


Returns `true` if the header identified by `name` is currently set in the outgoing headers. The header name matching is case-insensitive.
```
const hasContentType = response.hasHeader('content-type');
copy
```

####  `response.headersSent`[#](https://nodejs.org/docs/latest/api/http.html#responseheaderssent)
Added in: v0.9.3
  * Type:


Boolean (read-only). True if headers were sent, false otherwise.
####  `response.removeHeader(name)`[#](https://nodejs.org/docs/latest/api/http.html#responseremoveheadername)
Added in: v0.4.0
  * `name`


Removes a header that's queued for implicit sending.
```
response.removeHeader('Content-Encoding');
copy
```

####  `response.req`[#](https://nodejs.org/docs/latest/api/http.html#responsereq)
Added in: v15.7.0
  * Type: [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)


A reference to the original HTTP `request` object.
####  `response.sendDate`[#](https://nodejs.org/docs/latest/api/http.html#responsesenddate)
Added in: v0.7.5
  * Type:


When true, the Date header will be automatically generated and sent in the response if it is not already present in the headers. Defaults to true.
This should only be disabled for testing; HTTP requires the Date header in responses.
####  `response.setHeader(name, value)`[#](https://nodejs.org/docs/latest/api/http.html#responsesetheadername-value)
Added in: v0.4.0
  * `name`
  * `value`
  * Returns: [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)


Returns the response object.
Sets a single header value for implicit headers. If this header already exists in the to-be-sent headers, its value will be replaced. Use an array of strings here to send multiple headers with the same name. Non-string values will be stored without modification. Therefore, [`response.getHeader()`](https://nodejs.org/docs/latest/api/http.html#responsegetheadername) may return non-string values. However, the non-string values will be converted to strings for network transmission. The same response object is returned to the caller, to enable call chaining.
```
response.setHeader('Content-Type', 'text/html');
copy
```

or
```
response.setHeader('Set-Cookie', ['type=ninja', 'language=javascript']);
copy
```

Attempting to set a header field name or value that contains invalid characters will result in a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) being thrown.
When headers have been set with [`response.setHeader()`](https://nodejs.org/docs/latest/api/http.html#responsesetheadername-value), they will be merged with any headers passed to [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers), with the headers passed to [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers) given precedence.
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

If [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers) method is called and this method has not been called, it will directly write the supplied header values onto the network channel without caching internally, and the [`response.getHeader()`](https://nodejs.org/docs/latest/api/http.html#responsegetheadername) on the header will not yield the expected result. If progressive population of headers is desired with potential future retrieval and modification, use [`response.setHeader()`](https://nodejs.org/docs/latest/api/http.html#responsesetheadername-value) instead of [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers).
