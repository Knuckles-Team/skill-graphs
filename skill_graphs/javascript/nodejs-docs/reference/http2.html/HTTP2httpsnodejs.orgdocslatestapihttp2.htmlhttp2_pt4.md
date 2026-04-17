If `callback` is provided, it is not invoked until all active sessions have been closed, although the server has already stopped allowing new sessions. See [`net.Server.close()`](https://nodejs.org/docs/latest/api/net.html#serverclosecallback) for more details.
#####  `server[Symbol.asyncDispose]()`[#](https://nodejs.org/docs/latest/api/http2.html#serversymbolasyncdispose)
Added in: v20.4.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Calls [`server.close()`](https://nodejs.org/docs/latest/api/http2.html#serverclosecallback) and returns a promise that fulfills when the server has closed.
#####  `server.setTimeout([msecs][, callback])`[#](https://nodejs.org/docs/latest/api/http2.html#serversettimeoutmsecs-callback)
Added in: v8.4.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v13.0.0 | The default timeout changed from 120s to 0 (no timeout).
  * `msecs` **Default:** 0 (no timeout)
  * `callback`
  * Returns: [`<Http2Server>`](https://nodejs.org/docs/latest/api/http2.html#class-http2server)


Used to set the timeout value for http2 server requests, and sets a callback function that is called when there is no activity on the `Http2Server` after `msecs` milliseconds.
The given callback is registered as a listener on the `'timeout'` event.
In case if `callback` is not a function, a new `ERR_INVALID_ARG_TYPE` error will be thrown.
#####  `server.timeout`[#](https://nodejs.org/docs/latest/api/http2.html#servertimeout)
Added in: v8.4.0History Version | Changes
---|---
v13.0.0 | The default timeout changed from 120s to 0 (no timeout).
  * Type: **Default:** 0 (no timeout)


The number of milliseconds of inactivity before a socket is presumed to have timed out.
A value of `0` will disable the timeout behavior on incoming connections.
The socket timeout logic is set up on connection, so changing this value only affects new connections to the server, not any existing connections.
#####  `server.updateSettings([settings])`[#](https://nodejs.org/docs/latest/api/http2.html#serverupdatesettingssettings)
Added in: v15.1.0, v14.17.0
  * `settings` [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object)


Used to update the server with the provided settings.
Throws `ERR_HTTP2_INVALID_SETTING_VALUE` for invalid `settings` values.
Throws `ERR_INVALID_ARG_TYPE` for invalid `settings` argument.
#### Class: `Http2SecureServer`[#](https://nodejs.org/docs/latest/api/http2.html#class-http2secureserver)
Added in: v8.4.0
  * Extends: [`<tls.Server>`](https://nodejs.org/docs/latest/api/tls.html#class-tlsserver)


Instances of `Http2SecureServer` are created using the `http2.createSecureServer()` function. The `Http2SecureServer` class is not exported directly by the `node:http2` module.
##### Event: `'checkContinue'`[#](https://nodejs.org/docs/latest/api/http2.html#event-checkcontinue-1)
Added in: v8.5.0
  * `request` [`<http2.Http2ServerRequest>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverrequest)
  * `response` [`<http2.Http2ServerResponse>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverresponse)


If a [`'request'`](https://nodejs.org/docs/latest/api/http2.html#event-request) listener is registered or [`http2.createSecureServer()`](https://nodejs.org/docs/latest/api/http2.html#http2createsecureserveroptions-onrequesthandler) is supplied a callback function, the `'checkContinue'` event is emitted each time a request with an HTTP `Expect: 100-continue` is received. If this event is not listened for, the server will automatically respond with a status `100 Continue` as appropriate.
Handling this event involves calling [`response.writeContinue()`](https://nodejs.org/docs/latest/api/http2.html#responsewritecontinue) if the client should continue to send the request body, or generating an appropriate HTTP response (e.g. 400 Bad Request) if the client should not continue to send the request body.
When this event is emitted and handled, the [`'request'`](https://nodejs.org/docs/latest/api/http2.html#event-request) event will not be emitted.
##### Event: `'connection'`[#](https://nodejs.org/docs/latest/api/http2.html#event-connection-1)
Added in: v8.4.0
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


This event is emitted when a new TCP stream is established, before the TLS handshake begins. `socket` is typically an object of type [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket). Usually users will not want to access this event.
This event can also be explicitly emitted by users to inject connections into the HTTP server. In that case, any [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) stream can be passed.
##### Event: `'request'`[#](https://nodejs.org/docs/latest/api/http2.html#event-request-1)
Added in: v8.4.0
  * `request` [`<http2.Http2ServerRequest>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverrequest)
  * `response` [`<http2.Http2ServerResponse>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverresponse)


Emitted each time there is a request. There may be multiple requests per session. See the [Compatibility API](https://nodejs.org/docs/latest/api/http2.html#compatibility-api).
##### Event: `'session'`[#](https://nodejs.org/docs/latest/api/http2.html#event-session-1)
Added in: v8.4.0
  * `session` [`<ServerHttp2Session>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2session)


The `'session'` event is emitted when a new `Http2Session` is created by the `Http2SecureServer`.
##### Event: `'sessionError'`[#](https://nodejs.org/docs/latest/api/http2.html#event-sessionerror-1)
Added in: v8.4.0
  * `error`
  * `session` [`<ServerHttp2Session>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2session)


The `'sessionError'` event is emitted when an `'error'` event is emitted by an `Http2Session` object associated with the `Http2SecureServer`.
##### Event: `'stream'`[#](https://nodejs.org/docs/latest/api/http2.html#event-stream-2)
Added in: v8.4.0
  * `stream` [`<Http2Stream>`](https://nodejs.org/docs/latest/api/http2.html#class-http2stream) A reference to the stream
  * `headers` [`<HTTP/2 Headers Object>`](https://nodejs.org/docs/latest/api/http2.html#headers-object) An object describing the headers
  * `flags`
  * `rawHeaders` {HTTP/2 Raw Headers} An array containing the raw headers


The `'stream'` event is emitted when a `'stream'` event has been emitted by an `Http2Session` associated with the server.
See also [`Http2Session`'s `'stream'` event](https://nodejs.org/docs/latest/api/http2.html#event-stream).
```
import { createSecureServer, constants } from 'node:http2';
const {
  HTTP2_HEADER_METHOD,
  HTTP2_HEADER_PATH,
  HTTP2_HEADER_STATUS,
  HTTP2_HEADER_CONTENT_TYPE,
} = constants;

const options = getOptionsSomehow();

const server = createSecureServer(options);
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

const options = getOptionsSomehow();

const server = http2.createSecureServer(options);
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

##### Event: `'timeout'`[#](https://nodejs.org/docs/latest/api/http2.html#event-timeout-3)
Added in: v8.4.0
The `'timeout'` event is emitted when there is no activity on the Server for a given number of milliseconds set using `http2secureServer.setTimeout()`. **Default:** 2 minutes.
##### Event: `'unknownProtocol'`[#](https://nodejs.org/docs/latest/api/http2.html#event-unknownprotocol)
Added in: v8.4.0History Version | Changes
---|---
v19.0.0 | This event will only be emitted if the client did not transmit an ALPN extension during the TLS handshake.
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


The `'unknownProtocol'` event is emitted when a connecting client fails to negotiate an allowed protocol (i.e. HTTP/2 or HTTP/1.1). The event handler receives the socket for handling. If no listener is registered for this event, the connection is terminated. A timeout may be specified using the `'unknownProtocolTimeout'` option passed to [`http2.createSecureServer()`](https://nodejs.org/docs/latest/api/http2.html#http2createsecureserveroptions-onrequesthandler).
In earlier versions of Node.js, this event would be emitted if `allowHTTP1` is `false` and, during the TLS handshake, the client either does not send an ALPN extension or sends an ALPN extension that does not include HTTP/2 (`h2`). Newer versions of Node.js only emit this event if `allowHTTP1` is `false` and the client does not send an ALPN extension. If the client sends an ALPN extension that does not include HTTP/2 (or HTTP/1.1 if `allowHTTP1` is `true`), the TLS handshake will fail and no secure connection will be established.
See the [Compatibility API](https://nodejs.org/docs/latest/api/http2.html#compatibility-api).
#####  `server.close([callback])`[#](https://nodejs.org/docs/latest/api/http2.html#serverclosecallback-1)
Added in: v8.4.0
  * `callback`


Stops the server from establishing new sessions. This does not prevent new request streams from being created due to the persistent nature of HTTP/2 sessions. To gracefully shut down the server, call [`http2session.close()`](https://nodejs.org/docs/latest/api/http2.html#http2sessionclosecallback) on all active sessions.
If `callback` is provided, it is not invoked until all active sessions have been closed, although the server has already stopped allowing new sessions. See [`tls.Server.close()`](https://nodejs.org/docs/latest/api/tls.html#serverclosecallback) for more details.
#####  `server.setTimeout([msecs][, callback])`[#](https://nodejs.org/docs/latest/api/http2.html#serversettimeoutmsecs-callback-1)
Added in: v8.4.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `msecs` **Default:** `120000` (2 minutes)
  * `callback`
  * Returns: [`<Http2SecureServer>`](https://nodejs.org/docs/latest/api/http2.html#class-http2secureserver)


Used to set the timeout value for http2 secure server requests, and sets a callback function that is called when there is no activity on the `Http2SecureServer` after `msecs` milliseconds.
The given callback is registered as a listener on the `'timeout'` event.
In case if `callback` is not a function, a new `ERR_INVALID_ARG_TYPE` error will be thrown.
#####  `server.timeout`[#](https://nodejs.org/docs/latest/api/http2.html#servertimeout-1)
Added in: v8.4.0History Version | Changes
---|---
v13.0.0 | The default timeout changed from 120s to 0 (no timeout).
  * Type: **Default:** 0 (no timeout)


The number of milliseconds of inactivity before a socket is presumed to have timed out.
A value of `0` will disable the timeout behavior on incoming connections.
The socket timeout logic is set up on connection, so changing this value only affects new connections to the server, not any existing connections.
#####  `server.updateSettings([settings])`[#](https://nodejs.org/docs/latest/api/http2.html#serverupdatesettingssettings-1)
Added in: v15.1.0, v14.17.0
  * `settings` [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object)


Used to update the server with the provided settings.
Throws `ERR_HTTP2_INVALID_SETTING_VALUE` for invalid `settings` values.
Throws `ERR_INVALID_ARG_TYPE` for invalid `settings` argument.
####  `http2.createServer([options][, onRequestHandler])`[#](https://nodejs.org/docs/latest/api/http2.html#http2createserveroptions-onrequesthandler)
Added in: v8.4.0History Version | Changes
---|---
v25.7.0 | Added the `strictSingleValueFields` option.
v25.7.0 | Added `http1Options` option. The `Http1IncomingMessage` and `Http1ServerResponse` options are now deprecated.
v23.0.0, v22.10.0 | Added `streamResetBurst` and `streamResetRate`.
v15.10.0, v14.16.0, v12.21.0, v10.24.0 | Added `unknownProtocolTimeout` option with a default of 10000.
v14.4.0, v12.18.0, v10.21.0 | Added `maxSettings` option with a default of 32.
v13.3.0, v12.16.0 | Added `maxSessionRejectedStreams` option with a default of 100.
v13.3.0, v12.16.0 | Added `maxSessionInvalidFrames` option with a default of 1000.
v13.0.0 | The `PADDING_STRATEGY_CALLBACK` has been made equivalent to providing `PADDING_STRATEGY_ALIGNED` and `selectPadding` has been removed.
v12.4.0 | The `options` parameter now supports `net.createServer()` options.
v9.6.0 | Added the `Http1IncomingMessage` and `Http1ServerResponse` option.
v8.9.3 | Added the `maxOutstandingPings` option with a default limit of 10.
v8.9.3 | Added the `maxHeaderListPairs` option with a default limit of 128 header pairs.
  * `options`
    * `maxDeflateDynamicTableSize` **Default:** `4Kib`.
    * `maxSettings` `SETTINGS` frame. The minimum value allowed is `1`. **Default:** `32`.
    * `maxSessionMemory``Http2Session` is permitted to use. The value is expressed in terms of number of megabytes, e.g. `1` equal 1 megabyte. The minimum value allowed is `1`. This is a credit based limit, existing `Http2Stream`s may cause this limit to be exceeded, but new `Http2Stream` instances will be rejected while this limit is exceeded. The current number of `Http2Stream` sessions, the current memory use of the header compression tables, current data queued to be sent, and unacknowledged `PING` and `SETTINGS` frames are all counted towards the current limit. **Default:** `10`.
    * `maxHeaderListPairs` [`server.maxHeadersCount`](https://nodejs.org/docs/latest/api/http.html#servermaxheaderscount) or [`request.maxHeadersCount`](https://nodejs.org/docs/latest/api/http.html#requestmaxheaderscount) in the `node:http` module. The minimum value is `4`. **Default:** `128`.
    * `maxOutstandingPings` **Default:** `10`.
    * `maxSendHeaderBlockLength` `'frameError'` event being emitted and the stream being closed and destroyed. While this sets the maximum allowed size to the entire block of headers, `nghttp2` (the internal http2 library) has a limit of `65536` for each decompressed key/value pair.
    * `paddingStrategy` `HEADERS` and `DATA` frames. **Default:** `http2.constants.PADDING_STRATEGY_NONE`. Value may be one of:
      * `http2.constants.PADDING_STRATEGY_NONE`: No padding is applied.
      * `http2.constants.PADDING_STRATEGY_MAX`: The maximum amount of padding, determined by the internal implementation, is applied.
      * `http2.constants.PADDING_STRATEGY_ALIGNED`: Attempts to apply enough padding to ensure that the total frame length, including the 9-byte header, is a multiple of 8. For each frame, there is a maximum allowed number of padding bytes that is determined by current flow control state and settings. If this maximum is less than the calculated amount needed to ensure alignment, the maximum is used and the total frame length is not necessarily aligned at 8 bytes.
    * `peerMaxConcurrentStreams` `SETTINGS` frame had been received. Will be overridden if the remote peer sets its own value for `maxConcurrentStreams`. **Default:** `100`.
    * `maxSessionInvalidFrames` **Default:** `1000`.
    * `maxSessionRejectedStreams` `NGHTTP2_ENHANCE_YOUR_CALM` error that should tell the peer to not open any more streams, continuing to open streams is therefore regarded as a sign of a misbehaving peer. **Default:** `100`.
    * `settings` [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object) The initial settings to send to the remote peer upon connection.
    * `streamResetBurst` `streamResetRate`
    * `remoteCustomSettings` `CustomSettings`-property of the received remoteSettings. Please see the `CustomSettings`-property of the `Http2Settings` object for more information, on the allowed setting types.
    * `Http1IncomingMessage` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage) Specifies the `IncomingMessage` class to used for HTTP/1 fallback. Useful for extending the original `http.IncomingMessage`. **Default:** `http.IncomingMessage`. **Deprecated.** Use `http1Options.IncomingMessage` instead. See [DEP0202](https://nodejs.org/docs/latest/api/deprecations.html#dep0202-http1incomingmessage-and-http1serverresponse-options-of-http2-servers).
    * `Http1ServerResponse` [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse) Specifies the `ServerResponse` class to used for HTTP/1 fallback. Useful for extending the original `http.ServerResponse`. **Default:** `http.ServerResponse`. **Deprecated.** Use `http1Options.ServerResponse` instead. See [DEP0202](https://nodejs.org/docs/latest/api/deprecations.html#dep0202-http1incomingmessage-and-http1serverresponse-options-of-http2-servers).
    * `http1Options` `allowHTTP1` is `true`. These options are passed to the underlying HTTP/1 server. See [`http.createServer()`](https://nodejs.org/docs/latest/api/http.html#httpcreateserveroptions-requestlistener) for available options. Among others, the following are supported:
      * `IncomingMessage` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage) Specifies the `IncomingMessage` class to use for HTTP/1 fallback. **Default:** `http.IncomingMessage`.
      * `ServerResponse` [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse) Specifies the `ServerResponse` class to use for HTTP/1 fallback. **Default:** `http.ServerResponse`.
      * `keepAliveTimeout` **Default:** `5000`.
    * `Http2ServerRequest` [`<http2.Http2ServerRequest>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverrequest) Specifies the `Http2ServerRequest` class to use. Useful for extending the original `Http2ServerRequest`. **Default:** `Http2ServerRequest`.
    * `Http2ServerResponse` [`<http2.Http2ServerResponse>`](https://nodejs.org/docs/latest/api/http2.html#class-http2http2serverresponse) Specifies the `Http2ServerResponse` class to use. Useful for extending the original `Http2ServerResponse`. **Default:** `Http2ServerResponse`.
    * `unknownProtocolTimeout` [`'unknownProtocol'`](https://nodejs.org/docs/latest/api/http2.html#event-unknownprotocol) is emitted. If the socket has not been destroyed by that time the server will destroy it. **Default:** `10000`.
    * `strictFieldWhitespaceValidation` `true`, it turns on strict leading and trailing whitespace validation for HTTP/2 header field names and values as per **Default:** `true`.
    * `strictSingleValueFields` `true`, strict validation is used for headers and trailers defined as having only a single value, such that an error is thrown if multiple values are provided. **Default:** `true`.
    * `...options` [`net.createServer()`](https://nodejs.org/docs/latest/api/net.html#netcreateserveroptions-connectionlistener) option can be provided.
  * `onRequestHandler` [Compatibility API](https://nodejs.org/docs/latest/api/http2.html#compatibility-api)
  * Returns: [`<Http2Server>`](https://nodejs.org/docs/latest/api/http2.html#class-http2server)


Returns a `net.Server` instance that creates and manages `Http2Session` instances.
Since there are no browsers known that support [`http2.createSecureServer()`](https://nodejs.org/docs/latest/api/http2.html#http2createsecureserveroptions-onrequesthandler) is necessary when communicating with browser clients.
```
import { createServer } from 'node:http2';

// Create an unencrypted HTTP/2 server.
// Since there are no browsers known that support
// unencrypted HTTP/2, the use of `createSecureServer()`
// is necessary when communicating with browser clients.
const server = createServer();

server.on('stream', (stream, headers) => {
  stream.respond({
    'content-type': 'text/html; charset=utf-8',
    ':status': 200,
  });
  stream.end('<h1>Hello World</h1>');
});

server.listen(8000);
const http2 = require('node:http2');

// Create an unencrypted HTTP/2 server.
// Since there are no browsers known that support
// unencrypted HTTP/2, the use of `http2.createSecureServer()`
// is necessary when communicating with browser clients.
const server = http2.createServer();

server.on('stream', (stream, headers) => {
  stream.respond({
    'content-type': 'text/html; charset=utf-8',
    ':status': 200,
  });
  stream.end('<h1>Hello World</h1>');
});

server.listen(8000);
copy
```

####  `http2.createSecureServer(options[, onRequestHandler])`[#](https://nodejs.org/docs/latest/api/http2.html#http2createsecureserveroptions-onrequesthandler)
Added in: v8.4.0History Version | Changes
---|---
v25.7.0 | Added the `strictSingleValueFields` option.
v25.7.0 | Added `http1Options` option.
v15.10.0, v14.16.0, v12.21.0, v10.24.0 | Added `unknownProtocolTimeout` option with a default of 10000.
v14.4.0, v12.18.0, v10.21.0 | Added `maxSettings` option with a default of 32.
v13.3.0, v12.16.0 | Added `maxSessionRejectedStreams` option with a default of 100.
v13.3.0, v12.16.0 | Added `maxSessionInvalidFrames` option with a default of 1000.
v13.0.0 | The `PADDING_STRATEGY_CALLBACK` has been made equivalent to providing `PADDING_STRATEGY_ALIGNED` and `selectPadding` has been removed.
v10.12.0 | Added the `origins` option to automatically send an `ORIGIN` frame on `Http2Session` startup.
v8.9.3 | Added the `maxOutstandingPings` option with a default limit of 10.
v8.9.3 | Added the `maxHeaderListPairs` option with a default limit of 128 header pairs.
  * `options`
    * `allowHTTP1` `true`. See the [`'unknownProtocol'`](https://nodejs.org/docs/latest/api/http2.html#event-unknownprotocol) event. See [ALPN negotiation](https://nodejs.org/docs/latest/api/http2.html#alpn-negotiation). **Default:** `false`.
    * `maxDeflateDynamicTableSize` **Default:** `4Kib`.
    * `maxSettings` `SETTINGS` frame. The minimum value allowed is `1`. **Default:** `32`.
    * `maxSessionMemory``Http2Session` is permitted to use. The value is expressed in terms of number of megabytes, e.g. `1` equal 1 megabyte. The minimum value allowed is `1`. This is a credit based limit, existing `Http2Stream`s may cause this limit to be exceeded, but new `Http2Stream` instances will be rejected while this limit is exceeded. The current number of `Http2Stream` sessions, the current memory use of the header compression tables, current data queued to be sent, and unacknowledged `PING` and `SETTINGS` frames are all counted towards the current limit. **Default:** `10`.
    * `maxHeaderListPairs` [`server.maxHeadersCount`](https://nodejs.org/docs/latest/api/http.html#servermaxheaderscount) or [`request.maxHeadersCount`](https://nodejs.org/docs/latest/api/http.html#requestmaxheaderscount) in the `node:http` module. The minimum value is `4`. **Default:** `128`.
    * `maxOutstandingPings` **Default:** `10`.
    * `maxSendHeaderBlockLength` `'frameError'` event being emitted and the stream being closed and destroyed.
    * `paddingStrategy` `HEADERS` and `DATA` frames. **Default:** `http2.constants.PADDING_STRATEGY_NONE`. Value may be one of:
      * `http2.constants.PADDING_STRATEGY_NONE`: No padding is applied.
      * `http2.constants.PADDING_STRATEGY_MAX`: The maximum amount of padding, determined by the internal implementation, is applied.
      * `http2.constants.PADDING_STRATEGY_ALIGNED`: Attempts to apply enough padding to ensure that the total frame length, including the 9-byte header, is a multiple of 8. For each frame, there is a maximum allowed number of padding bytes that is determined by current flow control state and settings. If this maximum is less than the calculated amount needed to ensure alignment, the maximum is used and the total frame length is not necessarily aligned at 8 bytes.
    * `peerMaxConcurrentStreams` `SETTINGS` frame had been received. Will be overridden if the remote peer sets its own value for `maxConcurrentStreams`. **Default:** `100`.
    * `maxSessionInvalidFrames` **Default:** `1000`.
    * `maxSessionRejectedStreams` `NGHTTP2_ENHANCE_YOUR_CALM` error that should tell the peer to not open any more streams, continuing to open streams is therefore regarded as a sign of a misbehaving peer. **Default:** `100`.
    * `settings` [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object) The initial settings to send to the remote peer upon connection.
    * `streamResetBurst` `streamResetRate`
    * `remoteCustomSettings` `customSettings`-property of the received remoteSettings. Please see the `customSettings`-property of the `Http2Settings` object for more information, on the allowed setting types.
    * `...options` [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener) options can be provided. For servers, the identity options (`pfx` or `key`/`cert`) are usually required.
