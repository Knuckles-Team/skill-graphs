####  `outgoingMessage.appendHeader(name, value)`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessageappendheadername-value)
Added in: v18.3.0, v16.17.0
  * `name`
  * `value`
  * Returns:


Append a single header value to the header object.
If the value is an array, this is equivalent to calling this method multiple times.
If there were no previous values for the header, this is equivalent to calling [`outgoingMessage.setHeader(name, value)`](https://nodejs.org/docs/latest/api/http.html#outgoingmessagesetheadername-value).
Depending of the value of `options.uniqueHeaders` when the client request or the server were created, this will end up in the header being sent multiple times or a single time with values joined using `; `.
####  `outgoingMessage.connection`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessageconnection)
Added in: v0.3.0Deprecated in: v15.12.0, v14.17.1
Stability: 0 - Deprecated: Use [`outgoingMessage.socket`](https://nodejs.org/docs/latest/api/http.html#outgoingmessagesocket) instead.
Alias of [`outgoingMessage.socket`](https://nodejs.org/docs/latest/api/http.html#outgoingmessagesocket).
####  `outgoingMessage.cork()`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagecork)
Added in: v13.2.0, v12.16.0
See [`writable.cork()`](https://nodejs.org/docs/latest/api/stream.html#writablecork).
####  `outgoingMessage.destroy([error])`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagedestroyerror)
Added in: v0.3.0
  * `error` `error` event
  * Returns:


Destroys the message. Once a socket is associated with the message and is connected, that socket will be destroyed as well.
####  `outgoingMessage.end(chunk[, encoding][, callback])`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessageendchunk-encoding-callback)
Added in: v0.1.90History Version | Changes
---|---
v15.0.0 | The `chunk` parameter can now be a `Uint8Array`.
v0.11.6 | add `callback` argument.
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` **Default** : `utf8`
  * `callback`
  * Returns:


Finishes the outgoing message. If any parts of the body are unsent, it will flush them to the underlying system. If the message is chunked, it will send the terminating chunk `0\r\n\r\n`, and send the trailers (if any).
If `chunk` is specified, it is equivalent to calling `outgoingMessage.write(chunk, encoding)`, followed by `outgoingMessage.end(callback)`.
If `callback` is provided, it will be called when the message is finished (equivalent to a listener of the `'finish'` event).
####  `outgoingMessage.flushHeaders()`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessageflushheaders)
Added in: v1.6.0
Flushes the message headers.
For efficiency reason, Node.js normally buffers the message headers until `outgoingMessage.end()` is called or the first chunk of message data is written. It then tries to pack the headers and data into a single TCP packet.
It is usually desired (it saves a TCP round-trip), but not when the first data is not sent until possibly much later. `outgoingMessage.flushHeaders()` bypasses the optimization and kickstarts the message.
####  `outgoingMessage.getHeader(name)`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagegetheadername)
Added in: v0.4.0
  * `name`
  * Returns:


Gets the value of the HTTP header with the given name. If that header is not set, the returned value will be `undefined`.
####  `outgoingMessage.getHeaderNames()`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagegetheadernames)
Added in: v7.7.0
  * Returns:


Returns an array containing the unique names of the current outgoing headers. All names are lowercase.
####  `outgoingMessage.getHeaders()`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagegetheaders)
Added in: v7.7.0
  * Returns:


Returns a shallow copy of the current outgoing headers. Since a shallow copy is used, array values may be mutated without additional calls to various header-related HTTP module methods. The keys of the returned object are the header names and the values are the respective header values. All header names are lowercase.
The object returned by the `outgoingMessage.getHeaders()` method does not prototypically inherit from the JavaScript `Object`. This means that typical `Object` methods such as `obj.toString()`, `obj.hasOwnProperty()`, and others are not defined and will not work.
```
outgoingMessage.setHeader('Foo', 'bar');
outgoingMessage.setHeader('Set-Cookie', ['foo=bar', 'bar=baz']);

const headers = outgoingMessage.getHeaders();
// headers === { foo: 'bar', 'set-cookie': ['foo=bar', 'bar=baz'] }
copy
```

####  `outgoingMessage.hasHeader(name)`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagehasheadername)
Added in: v7.7.0
  * `name`
  * Returns:


Returns `true` if the header identified by `name` is currently set in the outgoing headers. The header name is case-insensitive.
```
const hasContentType = outgoingMessage.hasHeader('content-type');
copy
```

####  `outgoingMessage.headersSent`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessageheaderssent)
Added in: v0.9.3
  * Type:


Read-only. `true` if the headers were sent, otherwise `false`.
####  `outgoingMessage.pipe()`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagepipe)
Added in: v9.0.0
Overrides the `stream.pipe()` method inherited from the legacy `Stream` class which is the parent class of `http.OutgoingMessage`.
Calling this method will throw an `Error` because `outgoingMessage` is a write-only stream.
####  `outgoingMessage.removeHeader(name)`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessageremoveheadername)
Added in: v0.4.0
  * `name`


Removes a header that is queued for implicit sending.
```
outgoingMessage.removeHeader('Content-Encoding');
copy
```

####  `outgoingMessage.setHeader(name, value)`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagesetheadername-value)
Added in: v0.4.0
  * `name`
  * `value`
  * Returns:


Sets a single header value. If the header already exists in the to-be-sent headers, its value will be replaced. Use an array of strings to send multiple headers with the same name.
####  `outgoingMessage.setHeaders(headers)`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagesetheadersheaders)
Added in: v19.6.0, v18.15.0
  * `headers`
  * Returns:


Sets multiple header values for implicit headers. `headers` must be an instance of [`Headers`](https://nodejs.org/docs/latest/api/globals.html#class-headers) or `Map`, if a header already exists in the to-be-sent headers, its value will be replaced.
```
const headers = new Headers({ foo: 'bar' });
outgoingMessage.setHeaders(headers);
copy
```

or
```
const headers = new Map([['foo', 'bar']]);
outgoingMessage.setHeaders(headers);
copy
```

When headers have been set with [`outgoingMessage.setHeaders()`](https://nodejs.org/docs/latest/api/http.html#outgoingmessagesetheadersheaders), they will be merged with any headers passed to [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers), with the headers passed to [`response.writeHead()`](https://nodejs.org/docs/latest/api/http.html#responsewriteheadstatuscode-statusmessage-headers) given precedence.
```
// Returns content-type = text/plain
const server = http.createServer((req, res) => {
  const headers = new Headers({ 'Content-Type': 'text/html' });
  res.setHeaders(headers);
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('ok');
});
copy
```

####  `outgoingMessage.setTimeout(msecs[, callback])`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagesettimeoutmsecs-callback)
Added in: v0.9.12
  * `msecs`
  * `callback` `timeout` event.
  * Returns:


Once a socket is associated with the message and is connected, [`socket.setTimeout()`](https://nodejs.org/docs/latest/api/net.html#socketsettimeouttimeout-callback) will be called with `msecs` as the first parameter.
####  `outgoingMessage.socket`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagesocket)
Added in: v0.3.0
  * Type: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


Reference to the underlying socket. Usually, users will not want to access this property.
After calling `outgoingMessage.end()`, this property will be nulled.
####  `outgoingMessage.uncork()`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessageuncork)
Added in: v13.2.0, v12.16.0
See [`writable.uncork()`](https://nodejs.org/docs/latest/api/stream.html#writableuncork)
####  `outgoingMessage.writableCorked`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagewritablecorked)
Added in: v13.2.0, v12.16.0
  * Type:


The number of times `outgoingMessage.cork()` has been called.
####  `outgoingMessage.writableEnded`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagewritableended)
Added in: v12.9.0
  * Type:


Is `true` if `outgoingMessage.end()` has been called. This property does not indicate whether the data has been flushed. For that purpose, use `message.writableFinished` instead.
####  `outgoingMessage.writableFinished`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagewritablefinished)
Added in: v12.7.0
  * Type:


Is `true` if all data has been flushed to the underlying system.
####  `outgoingMessage.writableHighWaterMark`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagewritablehighwatermark)
Added in: v12.9.0
  * Type:


The `highWaterMark` of the underlying socket if assigned. Otherwise, the default buffer level when [`writable.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) starts returning false (`16384`).
####  `outgoingMessage.writableLength`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagewritablelength)
Added in: v12.9.0
  * Type:


The number of buffered bytes.
####  `outgoingMessage.writableObjectMode`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagewritableobjectmode)
Added in: v12.9.0
  * Type:


Always `false`.
####  `outgoingMessage.write(chunk[, encoding][, callback])`[#](https://nodejs.org/docs/latest/api/http.html#outgoingmessagewritechunk-encoding-callback)
Added in: v0.1.29History Version | Changes
---|---
v15.0.0 | The `chunk` parameter can now be a `Uint8Array`.
v0.11.6 | The `callback` argument was added.
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` **Default** : `utf8`
  * `callback`
  * Returns:


Sends a chunk of the body. This method can be called multiple times.
The `encoding` argument is only relevant when `chunk` is a string. Defaults to `'utf8'`.
The `callback` argument is optional and will be called when this chunk of data is flushed.
Returns `true` if the entire data was flushed successfully to the kernel buffer. Returns `false` if all or part of the data was queued in the user memory. The `'drain'` event will be emitted when the buffer is free again.
###  `http.METHODS`[#](https://nodejs.org/docs/latest/api/http.html#httpmethods)
Added in: v0.11.8
  * Type:


A list of the HTTP methods that are supported by the parser.
###  `http.STATUS_CODES`[#](https://nodejs.org/docs/latest/api/http.html#httpstatus-codes)
Added in: v0.1.22
  * Type:


A collection of all the standard HTTP response status codes, and the short description of each. For example, `http.STATUS_CODES[404] === 'Not Found'`.
###  `http.createServer([options][, requestListener])`[#](https://nodejs.org/docs/latest/api/http.html#httpcreateserveroptions-requestlistener)
Added in: v0.1.13History Version | Changes
---|---
v25.1.0 | Add optimizeEmptyRequests option.
v24.9.0 | The `shouldUpgradeCallback` option is now supported.
v20.1.0, v18.17.0 | The `highWaterMark` option is supported now.
v18.0.0 | The `requestTimeout`, `headersTimeout`, `keepAliveTimeout`, and `connectionsCheckingInterval` options are supported now.
v18.0.0 | The `noDelay` option now defaults to `true`.
v17.7.0, v16.15.0 | The `noDelay`, `keepAlive` and `keepAliveInitialDelay` options are supported now.
v13.8.0, v12.15.0, v10.19.0 | The `insecureHTTPParser` option is supported now.
v13.3.0 | The `maxHeaderSize` option is supported now.
v9.6.0, v8.12.0 | The `options` argument is supported now.
  * `options`
    * `connectionsCheckingInterval`: Sets the interval value in milliseconds to check for request and headers timeout in incomplete requests. **Default:** `30000`.
    * `headersTimeout`: Sets the timeout value in milliseconds for receiving the complete HTTP headers from the client. See [`server.headersTimeout`](https://nodejs.org/docs/latest/api/http.html#serverheaderstimeout) for more information. **Default:** `60000`.
    * `highWaterMark` `socket`s' `readableHighWaterMark` and `writableHighWaterMark`. This affects `highWaterMark` property of both `IncomingMessage` and `ServerResponse`. **Default:** See [`stream.getDefaultHighWaterMark()`](https://nodejs.org/docs/latest/api/stream.html#streamgetdefaulthighwatermarkobjectmode).
    * `insecureHTTPParser` `true`, it will use a HTTP parser with leniency flags enabled. Using the insecure parser should be avoided. See [`--insecure-http-parser`](https://nodejs.org/docs/latest/api/cli.html#--insecure-http-parser) for more information. **Default:** `false`.
    * `IncomingMessage` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage) Specifies the `IncomingMessage` class to be used. Useful for extending the original `IncomingMessage`. **Default:** `IncomingMessage`.
    * `joinDuplicateHeaders` `true`, this option allows joining the field line values of multiple headers in a request with a comma (`, `) instead of discarding the duplicates. For more information, refer to [`message.headers`](https://nodejs.org/docs/latest/api/http.html#messageheaders). **Default:** `false`.
    * `keepAlive` `true`, it enables keep-alive functionality on the socket immediately after a new incoming connection is received, similarly on what is done in [`socket.setKeepAlive([enable][, initialDelay])`][`socket.setKeepAlive(enable, initialDelay)`]. **Default:** `false`.
    * `keepAliveInitialDelay` **Default:** `0`.
    * `keepAliveTimeout`: The number of milliseconds of inactivity a server needs to wait for additional incoming data, after it has finished writing the last response, before a socket will be destroyed. See [`server.keepAliveTimeout`](https://nodejs.org/docs/latest/api/http.html#serverkeepalivetimeout) for more information. **Default:** `5000`.
    * `maxHeaderSize` [`--max-http-header-size`](https://nodejs.org/docs/latest/api/cli.html#--max-http-header-sizesize) for requests received by this server, i.e. the maximum length of request headers in bytes. **Default:** 16384 (16 KiB).
    * `noDelay` `true`, it disables the use of Nagle's algorithm immediately after a new incoming connection is received. **Default:** `true`.
    * `requestTimeout`: Sets the timeout value in milliseconds for receiving the entire request from the client. See [`server.requestTimeout`](https://nodejs.org/docs/latest/api/http.html#serverrequesttimeout) for more information. **Default:** `300000`.
    * `requireHostHeader` `true`, it forces the server to respond with a 400 (Bad Request) status code to any HTTP/1.1 request message that lacks a Host header (as mandated by the specification). **Default:** `true`.
    * `ServerResponse` [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse) Specifies the `ServerResponse` class to be used. Useful for extending the original `ServerResponse`. **Default:** `ServerResponse`.
    * `shouldUpgradeCallback(request)` `'upgrade'` event (or their sockets will be destroyed, if no listener is registered) while rejected upgrades will fire a `'request'` event like any non-upgrade request. This options defaults to `() => server.listenerCount('upgrade') > 0`.
    * `uniqueHeaders` `; `.
    * `rejectNonStandardBodyWrites` `true`, an error is thrown when writing to an HTTP response which does not have a body. **Default:** `false`.
    * `optimizeEmptyRequests` `true`, requests without `Content-Length` or `Transfer-Encoding` headers (indicating no body) will be initialized with an already-ended body stream, so they will never emit any stream events (like `'data'` or `'end'`). You can use `req.readableEnded` to detect this case. **Default:** `false`.
  * `requestListener`
  * Returns: [`<http.Server>`](https://nodejs.org/docs/latest/api/http.html#class-httpserver)


Returns a new instance of [`http.Server`](https://nodejs.org/docs/latest/api/http.html#class-httpserver).
The `requestListener` is a function which is automatically added to the [`'request'`](https://nodejs.org/docs/latest/api/http.html#event-request) event.
```
import http from 'node:http';

// Create a local server to receive data from
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    data: 'Hello World!',
  }));
});

server.listen(8000);
const http = require('node:http');

// Create a local server to receive data from
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    data: 'Hello World!',
  }));
});

server.listen(8000);
copy
```
```
import http from 'node:http';

// Create a local server to receive data from
const server = http.createServer();

// Listen to the request event
server.on('request', (request, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    data: 'Hello World!',
  }));
});

server.listen(8000);
const http = require('node:http');

// Create a local server to receive data from
const server = http.createServer();

// Listen to the request event
server.on('request', (request, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    data: 'Hello World!',
  }));
});

server.listen(8000);
copy
```

###  `http.get(options[, callback])`[#](https://nodejs.org/docs/latest/api/http.html#httpgetoptions-callback)
###  `http.get(url[, options][, callback])`[#](https://nodejs.org/docs/latest/api/http.html#httpgeturl-options-callback)
Added in: v0.3.6History Version | Changes
---|---
v10.9.0 | The `url` parameter can now be passed along with a separate `options` object.
v7.5.0 | The `options` parameter can be a WHATWG `URL` object.
  * `url` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options` `options` as [`http.request()`](https://nodejs.org/docs/latest/api/http.html#httprequestoptions-callback), with the method set to GET by default.
  * `callback`
  * Returns: [`<http.ClientRequest>`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest)


Since most requests are GET requests without bodies, Node.js provides this convenience method. The only difference between this method and [`http.request()`](https://nodejs.org/docs/latest/api/http.html#httprequestoptions-callback) is that it sets the method to GET by default and calls `req.end()` automatically. The callback must take care to consume the response data for reasons stated in [`http.ClientRequest`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest) section.
The `callback` is invoked with a single argument that is an instance of [`http.IncomingMessage`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage).
JSON fetching example:
```
http.get('http://localhost:8000/', (res) => {
  const { statusCode } = res;
  const contentType = res.headers['content-type'];

  let error;
  // Any 2xx status code signals a successful response but
  // here we're only checking for 200.
  if (statusCode !== 200) {
    error = new Error('Request Failed.\n' +
                      `Status Code: ${statusCode}`);
  } else if (!/^application\/json/.test(contentType)) {
    error = new Error('Invalid content-type.\n' +
                      `Expected application/json but received ${contentType}`);
  }
  if (error) {
    console.error(error.message);
    // Consume response data to free up memory
    res.resume();
    return;
  }

  res.setEncoding('utf8');
  let rawData = '';
  res.on('data', (chunk) => { rawData += chunk; });
  res.on('end', () => {
    try {
      const parsedData = JSON.parse(rawData);
      console.log(parsedData);
    } catch (e) {
      console.error(e.message);
    }
  });
}).on('error', (e) => {
  console.error(`Got error: ${e.message}`);
});

// Create a local server to receive data from
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({
    data: 'Hello World!',
  }));
});

server.listen(8000);
copy
```

###  `http.globalAgent`[#](https://nodejs.org/docs/latest/api/http.html#httpglobalagent)
Added in: v0.5.9History Version | Changes
---|---
v19.0.0 | The agent now uses HTTP Keep-Alive and a 5 second timeout by default.
  * Type: [`<http.Agent>`](https://nodejs.org/docs/latest/api/http.html#class-httpagent)


Global instance of `Agent` which is used as the default for all HTTP client requests. Diverges from a default `Agent` configuration by having `keepAlive` enabled and a `timeout` of 5 seconds.
###  `http.maxHeaderSize`[#](https://nodejs.org/docs/latest/api/http.html#httpmaxheadersize)
Added in: v11.6.0, v10.15.0
  * Type:


Read-only property specifying the maximum allowed size of HTTP headers in bytes. Defaults to 16 KiB. Configurable using the [`--max-http-header-size`](https://nodejs.org/docs/latest/api/cli.html#--max-http-header-sizesize) CLI option.
This can be overridden for servers and client requests by passing the `maxHeaderSize` option.
###  `http.request(options[, callback])`[#](https://nodejs.org/docs/latest/api/http.html#httprequestoptions-callback)
###  `http.request(url[, options][, callback])`[#](https://nodejs.org/docs/latest/api/http.html#httprequesturl-options-callback)
Added in: v0.3.6History Version | Changes
---|---
v16.7.0, v14.18.0 | When using a `URL` object parsed username and password will now be properly URI decoded.
v15.3.0, v14.17.0 | It is possible to abort a request with an AbortSignal.
v13.8.0, v12.15.0, v10.19.0 | The `insecureHTTPParser` option is supported now.
v13.3.0 | The `maxHeaderSize` option is supported now.
v10.9.0 | The `url` parameter can now be passed along with a separate `options` object.
v7.5.0 | The `options` parameter can be a WHATWG `URL` object.
  * `url` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `agent` [`<http.Agent>`](https://nodejs.org/docs/latest/api/http.html#class-httpagent) | [`Agent`](https://nodejs.org/docs/latest/api/http.html#class-httpagent) behavior. Possible values:
      * `undefined` (default): use [`http.globalAgent`](https://nodejs.org/docs/latest/api/http.html#httpglobalagent) for this host and port.
      * `Agent` object: explicitly use the passed in `Agent`.
      * `false`: causes a new `Agent` with default values to be used.
    * `auth` `'user:password'`) to compute an Authorization header.
    * `createConnection` `agent` option is not used. This can be used to avoid creating a custom `Agent` class just to override the default `createConnection` function. See [`agent.createConnection()`](https://nodejs.org/docs/latest/api/http.html#agentcreateconnectionoptions-callback) for more details. Any [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) stream is a valid return value.
    * `defaultPort` **Default:** `agent.defaultPort` if an `Agent` is used, else `undefined`.
    * `family` `host` or `hostname`. Valid values are `4` or `6`. When unspecified, both IP v4 and v6 will be used.
    * `headers` [`message.rawHeaders`](https://nodejs.org/docs/latest/api/http.html#messagerawheaders).
    * `hints` [`dns.lookup()` hints](https://nodejs.org/docs/latest/api/dns.html#supported-getaddrinfo-flags).
    * `host` **Default:** `'localhost'`.
    * `hostname` `host`. To support [`url.parse()`](https://nodejs.org/docs/latest/api/url.html#urlparseurlstring-parsequerystring-slashesdenotehost), `hostname` will be used if both `host` and `hostname` are specified.
    * `insecureHTTPParser` `true`, it will use a HTTP parser with leniency flags enabled. Using the insecure parser should be avoided. See [`--insecure-http-parser`](https://nodejs.org/docs/latest/api/cli.html#--insecure-http-parser) for more information. **Default:** `false`
    * `joinDuplicateHeaders` `, ` instead of discarding the duplicates. See [`message.headers`](https://nodejs.org/docs/latest/api/http.html#messageheaders) for more information. **Default:** `false`.
    * `localAddress`
    * `localPort`
    * `lookup` **Default:** [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback).
    * `maxHeaderSize` [`--max-http-header-size`](https://nodejs.org/docs/latest/api/cli.html#--max-http-header-sizesize) (the maximum length of response headers in bytes) for responses received from the server. **Default:** 16384 (16 KiB).
    * `method` **Default:** `'GET'`.
    * `path` `'/index.html?page=12'`. An exception is thrown when the request path contains illegal characters. Currently, only spaces are rejected but that may change in the future. **Default:** `'/'`.
