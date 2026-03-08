#### Event: `'upgrade'`[#](https://nodejs.org/docs/latest/api/http.html#event-upgrade)
Added in: v0.1.94
  * `response` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)
  * `head` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Emitted each time a server responds to a request with an upgrade. If this event is not being listened for and the response status code is 101 Switching Protocols, clients receiving an upgrade header will have their connections closed.
This event is guaranteed to be passed an instance of the [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) class, a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), unless the user specifies a socket type other than [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
A client server pair demonstrating how to listen for the `'upgrade'` event.
```
import http from 'node:http';
import process from 'node:process';

// Create an HTTP server
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('okay');
});
server.on('upgrade', (req, socket, head) => {
  socket.write('HTTP/1.1 101 Web Socket Protocol Handshake\r\n' +
               'Upgrade: WebSocket\r\n' +
               'Connection: Upgrade\r\n' +
               '\r\n');

  socket.pipe(socket); // echo back
});

// Now that server is running
server.listen(1337, '127.0.0.1', () => {

  // make a request
  const options = {
    port: 1337,
    host: '127.0.0.1',
    headers: {
      'Connection': 'Upgrade',
      'Upgrade': 'websocket',
    },
  };

  const req = http.request(options);
  req.end();

  req.on('upgrade', (res, socket, upgradeHead) => {
    console.log('got upgraded!');
    socket.end();
    process.exit(0);
  });
});
const http = require('node:http');

// Create an HTTP server
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('okay');
});
server.on('upgrade', (req, socket, head) => {
  socket.write('HTTP/1.1 101 Web Socket Protocol Handshake\r\n' +
               'Upgrade: WebSocket\r\n' +
               'Connection: Upgrade\r\n' +
               '\r\n');

  socket.pipe(socket); // echo back
});

// Now that server is running
server.listen(1337, '127.0.0.1', () => {

  // make a request
  const options = {
    port: 1337,
    host: '127.0.0.1',
    headers: {
      'Connection': 'Upgrade',
      'Upgrade': 'websocket',
    },
  };

  const req = http.request(options);
  req.end();

  req.on('upgrade', (res, socket, upgradeHead) => {
    console.log('got upgraded!');
    socket.end();
    process.exit(0);
  });
});
copy
```

####  `request.abort()`[#](https://nodejs.org/docs/latest/api/http.html#requestabort)
Added in: v0.3.8Deprecated in: v14.1.0, v13.14.0
Stability: 0 - Deprecated: Use [`request.destroy()`](https://nodejs.org/docs/latest/api/http.html#requestdestroyerror) instead.
Marks the request as aborting. Calling this will cause remaining data in the response to be dropped and the socket to be destroyed.
####  `request.aborted`[#](https://nodejs.org/docs/latest/api/http.html#requestaborted)
Added in: v0.11.14Deprecated in: v17.0.0, v16.12.0History Version | Changes
---|---
v11.0.0 | The `aborted` property is no longer a timestamp number.
Stability: 0 - Deprecated. Check [`request.destroyed`](https://nodejs.org/docs/latest/api/http.html#requestdestroyed) instead.
  * Type:


The `request.aborted` property will be `true` if the request has been aborted.
####  `request.connection`[#](https://nodejs.org/docs/latest/api/http.html#requestconnection)
Added in: v0.3.0Deprecated in: v13.0.0
Stability: 0 - Deprecated. Use [`request.socket`](https://nodejs.org/docs/latest/api/http.html#requestsocket).
  * Type: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


See [`request.socket`](https://nodejs.org/docs/latest/api/http.html#requestsocket).
####  `request.cork()`[#](https://nodejs.org/docs/latest/api/http.html#requestcork)
Added in: v13.2.0, v12.16.0
See [`writable.cork()`](https://nodejs.org/docs/latest/api/stream.html#writablecork).
####  `request.end([data[, encoding]][, callback])`[#](https://nodejs.org/docs/latest/api/http.html#requestenddata-encoding-callback)
Added in: v0.1.90History Version | Changes
---|---
v15.0.0 | The `data` parameter can now be a `Uint8Array`.
v10.0.0 | This method now returns a reference to `ClientRequest`.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding`
  * `callback`
  * Returns:


Finishes sending the request. If any parts of the body are unsent, it will flush them to the stream. If the request is chunked, this will send the terminating `'0\r\n\r\n'`.
If `data` is specified, it is equivalent to calling [`request.write(data, encoding)`](https://nodejs.org/docs/latest/api/http.html#requestwritechunk-encoding-callback) followed by `request.end(callback)`.
If `callback` is specified, it will be called when the request stream is finished.
####  `request.destroy([error])`[#](https://nodejs.org/docs/latest/api/http.html#requestdestroyerror)
Added in: v0.3.0History Version | Changes
---|---
v14.5.0 | The function returns `this` for consistency with other Readable streams.
  * `error` `'error'` event.
  * Returns:


Destroy the request. Optionally emit an `'error'` event, and emit a `'close'` event. Calling this will cause remaining data in the response to be dropped and the socket to be destroyed.
See [`writable.destroy()`](https://nodejs.org/docs/latest/api/stream.html#writabledestroyerror) for further details.
#####  `request.destroyed`[#](https://nodejs.org/docs/latest/api/http.html#requestdestroyed)
Added in: v14.1.0, v13.14.0
  * Type:


Is `true` after [`request.destroy()`](https://nodejs.org/docs/latest/api/http.html#requestdestroyerror) has been called.
See [`writable.destroyed`](https://nodejs.org/docs/latest/api/stream.html#writabledestroyed) for further details.
####  `request.finished`[#](https://nodejs.org/docs/latest/api/http.html#requestfinished)
Added in: v0.0.1Deprecated in: v13.4.0, v12.16.0
Stability: 0 - Deprecated. Use [`request.writableEnded`](https://nodejs.org/docs/latest/api/http.html#requestwritableended).
  * Type:


The `request.finished` property will be `true` if [`request.end()`](https://nodejs.org/docs/latest/api/http.html#requestenddata-encoding-callback) has been called. `request.end()` will automatically be called if the request was initiated via [`http.get()`](https://nodejs.org/docs/latest/api/http.html#httpgetoptions-callback).
####  `request.flushHeaders()`[#](https://nodejs.org/docs/latest/api/http.html#requestflushheaders)
Added in: v1.6.0
Flushes the request headers.
For efficiency reasons, Node.js normally buffers the request headers until `request.end()` is called or the first chunk of request data is written. It then tries to pack the request headers and data into a single TCP packet.
That's usually desired (it saves a TCP round-trip), but not when the first data is not sent until possibly much later. `request.flushHeaders()` bypasses the optimization and kickstarts the request.
####  `request.getHeader(name)`[#](https://nodejs.org/docs/latest/api/http.html#requestgetheadername)
Added in: v1.6.0
  * `name`
  * Returns:


Reads out a header on the request. The name is case-insensitive. The type of the return value depends on the arguments provided to [`request.setHeader()`](https://nodejs.org/docs/latest/api/http.html#requestsetheadername-value).
```
request.setHeader('content-type', 'text/html');
request.setHeader('Content-Length', Buffer.byteLength(body));
request.setHeader('Cookie', ['type=ninja', 'language=javascript']);
const contentType = request.getHeader('Content-Type');
// 'contentType' is 'text/html'
const contentLength = request.getHeader('Content-Length');
// 'contentLength' is of type number
const cookie = request.getHeader('Cookie');
// 'cookie' is of type string[]
copy
```

####  `request.getHeaderNames()`[#](https://nodejs.org/docs/latest/api/http.html#requestgetheadernames)
Added in: v7.7.0
  * Returns:


Returns an array containing the unique names of the current outgoing headers. All header names are lowercase.
```
request.setHeader('Foo', 'bar');
request.setHeader('Cookie', ['foo=bar', 'bar=baz']);

const headerNames = request.getHeaderNames();
// headerNames === ['foo', 'cookie']
copy
```

####  `request.getHeaders()`[#](https://nodejs.org/docs/latest/api/http.html#requestgetheaders)
Added in: v7.7.0
  * Returns:


Returns a shallow copy of the current outgoing headers. Since a shallow copy is used, array values may be mutated without additional calls to various header-related http module methods. The keys of the returned object are the header names and the values are the respective header values. All header names are lowercase.
The object returned by the `request.getHeaders()` method _does not_ prototypically inherit from the JavaScript `Object`. This means that typical `Object` methods such as `obj.toString()`, `obj.hasOwnProperty()`, and others are not defined and _will not work_.
```
request.setHeader('Foo', 'bar');
request.setHeader('Cookie', ['foo=bar', 'bar=baz']);

const headers = request.getHeaders();
// headers === { foo: 'bar', 'cookie': ['foo=bar', 'bar=baz'] }
copy
```

####  `request.getRawHeaderNames()`[#](https://nodejs.org/docs/latest/api/http.html#requestgetrawheadernames)
Added in: v15.13.0, v14.17.0
  * Returns:


Returns an array containing the unique names of the current outgoing raw headers. Header names are returned with their exact casing being set.
```
request.setHeader('Foo', 'bar');
request.setHeader('Set-Cookie', ['foo=bar', 'bar=baz']);

const headerNames = request.getRawHeaderNames();
// headerNames === ['Foo', 'Set-Cookie']
copy
```

####  `request.hasHeader(name)`[#](https://nodejs.org/docs/latest/api/http.html#requesthasheadername)
Added in: v7.7.0
  * `name`
  * Returns:


Returns `true` if the header identified by `name` is currently set in the outgoing headers. The header name matching is case-insensitive.
```
const hasContentType = request.hasHeader('content-type');
copy
```

####  `request.maxHeadersCount`[#](https://nodejs.org/docs/latest/api/http.html#requestmaxheaderscount)
  * Type: **Default:** `2000`


Limits maximum response headers count. If set to 0, no limit will be applied.
####  `request.path`[#](https://nodejs.org/docs/latest/api/http.html#requestpath)
Added in: v0.4.0
  * Type:


####  `request.method`[#](https://nodejs.org/docs/latest/api/http.html#requestmethod)
Added in: v0.1.97
  * Type:


####  `request.host`[#](https://nodejs.org/docs/latest/api/http.html#requesthost)
Added in: v14.5.0, v12.19.0
  * Type:


####  `request.protocol`[#](https://nodejs.org/docs/latest/api/http.html#requestprotocol)
Added in: v14.5.0, v12.19.0
  * Type:


####  `request.removeHeader(name)`[#](https://nodejs.org/docs/latest/api/http.html#requestremoveheadername)
Added in: v1.6.0
  * `name`


Removes a header that's already defined into headers object.
```
request.removeHeader('Content-Type');
copy
```

####  `request.reusedSocket`[#](https://nodejs.org/docs/latest/api/http.html#requestreusedsocket)
Added in: v13.0.0, v12.16.0
  * Type:


When sending request through a keep-alive enabled agent, the underlying socket might be reused. But if server closes connection at unfortunate time, client may run into a 'ECONNRESET' error.
```
import http from 'node:http';
const agent = new http.Agent({ keepAlive: true });

// Server has a 5 seconds keep-alive timeout by default
http
  .createServer((req, res) => {
    res.write('hello\n');
    res.end();
  })
  .listen(3000);

setInterval(() => {
  // Adapting a keep-alive agent
  http.get('http://localhost:3000', { agent }, (res) => {
    res.on('data', (data) => {
      // Do nothing
    });
  });
}, 5000); // Sending request on 5s interval so it's easy to hit idle timeout
const http = require('node:http');
const agent = new http.Agent({ keepAlive: true });

// Server has a 5 seconds keep-alive timeout by default
http
  .createServer((req, res) => {
    res.write('hello\n');
    res.end();
  })
  .listen(3000);

setInterval(() => {
  // Adapting a keep-alive agent
  http.get('http://localhost:3000', { agent }, (res) => {
    res.on('data', (data) => {
      // Do nothing
    });
  });
}, 5000); // Sending request on 5s interval so it's easy to hit idle timeout
copy
```

By marking a request whether it reused socket or not, we can do automatic error retry base on it.
```
import http from 'node:http';
const agent = new http.Agent({ keepAlive: true });

function retriableRequest() {
  const req = http
    .get('http://localhost:3000', { agent }, (res) => {
      // ...
    })
    .on('error', (err) => {
      // Check if retry is needed
      if (req.reusedSocket && err.code === 'ECONNRESET') {
        retriableRequest();
      }
    });
}

retriableRequest();
const http = require('node:http');
const agent = new http.Agent({ keepAlive: true });

function retriableRequest() {
  const req = http
    .get('http://localhost:3000', { agent }, (res) => {
      // ...
    })
    .on('error', (err) => {
      // Check if retry is needed
      if (req.reusedSocket && err.code === 'ECONNRESET') {
        retriableRequest();
      }
    });
}

retriableRequest();
copy
```

####  `request.setHeader(name, value)`[#](https://nodejs.org/docs/latest/api/http.html#requestsetheadername-value)
Added in: v1.6.0
  * `name`
  * `value`


Sets a single header value for headers object. If this header already exists in the to-be-sent headers, its value will be replaced. Use an array of strings here to send multiple headers with the same name. Non-string values will be stored without modification. Therefore, [`request.getHeader()`](https://nodejs.org/docs/latest/api/http.html#requestgetheadername) may return non-string values. However, the non-string values will be converted to strings for network transmission.
```
request.setHeader('Content-Type', 'application/json');
copy
```

or
```
request.setHeader('Cookie', ['type=ninja', 'language=javascript']);
copy
```

When the value is a string an exception will be thrown if it contains characters outside the `latin1` encoding.
If you need to pass UTF-8 characters in the value please encode the value using the
```
const filename = 'Rock 🎵.txt';
request.setHeader('Content-Disposition', `attachment; filename*=utf-8''${encodeURIComponent(filename)}`);
copy
```

####  `request.setNoDelay([noDelay])`[#](https://nodejs.org/docs/latest/api/http.html#requestsetnodelaynodelay)
Added in: v0.5.9
  * `noDelay`


Once a socket is assigned to this request and is connected [`socket.setNoDelay()`](https://nodejs.org/docs/latest/api/net.html#socketsetnodelaynodelay) will be called.
####  `request.setSocketKeepAlive([enable][, initialDelay])`[#](https://nodejs.org/docs/latest/api/http.html#requestsetsocketkeepaliveenable-initialdelay)
Added in: v0.5.9
  * `enable`
  * `initialDelay`


Once a socket is assigned to this request and is connected [`socket.setKeepAlive()`](https://nodejs.org/docs/latest/api/net.html#socketsetkeepaliveenable-initialdelay) will be called.
####  `request.setTimeout(timeout[, callback])`[#](https://nodejs.org/docs/latest/api/http.html#requestsettimeouttimeout-callback)
Added in: v0.5.9History Version | Changes
---|---
v9.0.0 | Consistently set socket timeout only when the socket connects.
  * `timeout`
  * `callback` `'timeout'` event.
  * Returns: [`<http.ClientRequest>`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest)


Once a socket is assigned to this request and is connected [`socket.setTimeout()`](https://nodejs.org/docs/latest/api/net.html#socketsettimeouttimeout-callback) will be called.
####  `request.socket`[#](https://nodejs.org/docs/latest/api/http.html#requestsocket)
Added in: v0.3.0
  * Type: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


Reference to the underlying socket. Usually users will not want to access this property. In particular, the socket will not emit `'readable'` events because of how the protocol parser attaches to the socket.
```
import http from 'node:http';
const options = {
  host: 'www.google.com',
};
const req = http.get(options);
req.end();
req.once('response', (res) => {
  const ip = req.socket.localAddress;
  const port = req.socket.localPort;
  console.log(`Your IP address is ${ip} and your source port is ${port}.`);
  // Consume response object
});
const http = require('node:http');
const options = {
  host: 'www.google.com',
};
const req = http.get(options);
req.end();
req.once('response', (res) => {
  const ip = req.socket.localAddress;
  const port = req.socket.localPort;
  console.log(`Your IP address is ${ip} and your source port is ${port}.`);
  // Consume response object
});
copy
```

This property is guaranteed to be an instance of the [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) class, a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), unless the user specified a socket type other than [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
####  `request.uncork()`[#](https://nodejs.org/docs/latest/api/http.html#requestuncork)
Added in: v13.2.0, v12.16.0
See [`writable.uncork()`](https://nodejs.org/docs/latest/api/stream.html#writableuncork).
####  `request.writableEnded`[#](https://nodejs.org/docs/latest/api/http.html#requestwritableended)
Added in: v12.9.0
  * Type:


Is `true` after [`request.end()`](https://nodejs.org/docs/latest/api/http.html#requestenddata-encoding-callback) has been called. This property does not indicate whether the data has been flushed, for this use [`request.writableFinished`](https://nodejs.org/docs/latest/api/http.html#requestwritablefinished) instead.
####  `request.writableFinished`[#](https://nodejs.org/docs/latest/api/http.html#requestwritablefinished)
Added in: v12.7.0
  * Type:


Is `true` if all data has been flushed to the underlying system, immediately before the [`'finish'`](https://nodejs.org/docs/latest/api/http.html#event-finish) event is emitted.
####  `request.write(chunk[, encoding][, callback])`[#](https://nodejs.org/docs/latest/api/http.html#requestwritechunk-encoding-callback)
Added in: v0.1.29History Version | Changes
---|---
v15.0.0 | The `chunk` parameter can now be a `Uint8Array`.
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding`
  * `callback`
  * Returns:


Sends a chunk of the body. This method can be called multiple times. If no `Content-Length` is set, data will automatically be encoded in HTTP Chunked transfer encoding, so that server knows when the data ends. The `Transfer-Encoding: chunked` header is added. Calling [`request.end()`](https://nodejs.org/docs/latest/api/http.html#requestenddata-encoding-callback) is necessary to finish sending the request.
The `encoding` argument is optional and only applies when `chunk` is a string. Defaults to `'utf8'`.
The `callback` argument is optional and will be called when this chunk of data is flushed, but only if the chunk is non-empty.
Returns `true` if the entire data was flushed successfully to the kernel buffer. Returns `false` if all or part of the data was queued in user memory. `'drain'` will be emitted when the buffer is free again.
When `write` function is called with empty string or buffer, it does nothing and waits for more input.
### Class: `http.Server`[#](https://nodejs.org/docs/latest/api/http.html#class-httpserver)
Added in: v0.1.17
  * Extends: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


#### Event: `'checkContinue'`[#](https://nodejs.org/docs/latest/api/http.html#event-checkcontinue)
Added in: v0.3.0
  * `request` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
  * `response` [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)


Emitted each time a request with an HTTP `Expect: 100-continue` is received. If this event is not listened for, the server will automatically respond with a `100 Continue` as appropriate.
Handling this event involves calling [`response.writeContinue()`](https://nodejs.org/docs/latest/api/http.html#responsewritecontinue) if the client should continue to send the request body, or generating an appropriate HTTP response (e.g. 400 Bad Request) if the client should not continue to send the request body.
When this event is emitted and handled, the [`'request'`](https://nodejs.org/docs/latest/api/http.html#event-request) event will not be emitted.
#### Event: `'checkExpectation'`[#](https://nodejs.org/docs/latest/api/http.html#event-checkexpectation)
Added in: v5.5.0
  * `request` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
  * `response` [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)


Emitted each time a request with an HTTP `Expect` header is received, where the value is not `100-continue`. If this event is not listened for, the server will automatically respond with a `417 Expectation Failed` as appropriate.
When this event is emitted and handled, the [`'request'`](https://nodejs.org/docs/latest/api/http.html#event-request) event will not be emitted.
#### Event: `'clientError'`[#](https://nodejs.org/docs/latest/api/http.html#event-clienterror)
Added in: v0.1.94History Version | Changes
---|---
v12.0.0 | The default behavior will return a 431 Request Header Fields Too Large if a HPE_HEADER_OVERFLOW error occurs.
v9.4.0 | The `rawPacket` is the current buffer that just parsed. Adding this buffer to the error object of `'clientError'` event is to make it possible that developers can log the broken packet.
v6.0.0 | The default action of calling `.destroy()` on the `socket` will no longer take place if there are listeners attached for `'clientError'`.
  * `exception`
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


If a client connection emits an `'error'` event, it will be forwarded here. Listener of this event is responsible for closing/destroying the underlying socket. For example, one may wish to more gracefully close the socket with a custom HTTP response instead of abruptly severing the connection. The socket **must be closed or destroyed** before the listener ends.
This event is guaranteed to be passed an instance of the [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) class, a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), unless the user specifies a socket type other than [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
Default behavior is to try close the socket with a HTTP '400 Bad Request', or a HTTP '431 Request Header Fields Too Large' in the case of a [`HPE_HEADER_OVERFLOW`](https://nodejs.org/docs/latest/api/errors.html#hpe_header_overflow) error. If the socket is not writable or headers of the current attached [`http.ServerResponse`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse) has been sent, it is immediately destroyed.
`socket` is the [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) object that the error originated from.
```
import http from 'node:http';

const server = http.createServer((req, res) => {
  res.end();
});
server.on('clientError', (err, socket) => {
  socket.end('HTTP/1.1 400 Bad Request\r\n\r\n');
});
server.listen(8000);
const http = require('node:http');

const server = http.createServer((req, res) => {
  res.end();
});
server.on('clientError', (err, socket) => {
  socket.end('HTTP/1.1 400 Bad Request\r\n\r\n');
});
server.listen(8000);
copy
```

When the `'clientError'` event occurs, there is no `request` or `response` object, so any HTTP response sent, including response headers and payload, _must_ be written directly to the `socket` object. Care must be taken to ensure the response is a properly formatted HTTP response message.
`err` is an instance of `Error` with two extra columns:
  * `bytesParsed`: the bytes count of request packet that Node.js may have parsed correctly;
  * `rawPacket`: the raw packet of current request.


In some cases, the client has already received the response and/or the socket has already been destroyed, like in case of `ECONNRESET` errors. Before trying to send data to the socket, it is better to check that it is still writable.
```
server.on('clientError', (err, socket) => {
  if (err.code === 'ECONNRESET' || !socket.writable) {
    return;
  }

  socket.end('HTTP/1.1 400 Bad Request\r\n\r\n');
});
copy
```

#### Event: `'close'`[#](https://nodejs.org/docs/latest/api/http.html#event-close-1)
Added in: v0.1.4
Emitted when the server closes.
#### Event: `'connect'`[#](https://nodejs.org/docs/latest/api/http.html#event-connect-1)
Added in: v0.7.0
  * `request` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage) Arguments for the HTTP request, as it is in the [`'request'`](https://nodejs.org/docs/latest/api/http.html#event-request) event
