    * `origins` `ORIGIN` frame immediately following creation of a new server `Http2Session`.
    * `unknownProtocolTimeout` [`'unknownProtocol'`](https://nodejs.org/docs/latest/api/http2.html#event-unknownprotocol) event is emitted. If the socket has not been destroyed by that time the server will destroy it. **Default:** `10000`.
    * `strictFieldWhitespaceValidation` `true`, it turns on strict leading and trailing whitespace validation for HTTP/2 header field names and values as per **Default:** `true`.
    * `strictSingleValueFields` `true`, strict validation is used for headers and trailers defined as having only a single value, such that an error is thrown if multiple values are provided. **Default:** `true`.
    * `http1Options` `allowHTTP1` is `true`. These options are passed to the underlying HTTP/1 server. See [`http.createServer()`](https://nodejs.org/docs/latest/api/http.html#httpcreateserveroptions-requestlistener) for available options. Among others, the following are supported:
      * `IncomingMessage` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage) Specifies the `IncomingMessage` class to use for HTTP/1 fallback. **Default:** `http.IncomingMessage`.
      * `ServerResponse` [`<http.ServerResponse>`](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse) Specifies the `ServerResponse` class to use for HTTP/1 fallback. **Default:** `http.ServerResponse`.
      * `keepAliveTimeout` **Default:** `5000`.
  * `onRequestHandler` [Compatibility API](https://nodejs.org/docs/latest/api/http2.html#compatibility-api)
  * Returns: [`<Http2SecureServer>`](https://nodejs.org/docs/latest/api/http2.html#class-http2secureserver)


Returns a `tls.Server` instance that creates and manages `Http2Session` instances.
```
import { createSecureServer } from 'node:http2';
import { readFileSync } from 'node:fs';

const options = {
  key: readFileSync('server-key.pem'),
  cert: readFileSync('server-cert.pem'),
};

// Create a secure HTTP/2 server
const server = createSecureServer(options);

server.on('stream', (stream, headers) => {
  stream.respond({
    'content-type': 'text/html; charset=utf-8',
    ':status': 200,
  });
  stream.end('<h1>Hello World</h1>');
});

server.listen(8443);
const http2 = require('node:http2');
const fs = require('node:fs');

const options = {
  key: fs.readFileSync('server-key.pem'),
  cert: fs.readFileSync('server-cert.pem'),
};

// Create a secure HTTP/2 server
const server = http2.createSecureServer(options);

server.on('stream', (stream, headers) => {
  stream.respond({
    'content-type': 'text/html; charset=utf-8',
    ':status': 200,
  });
  stream.end('<h1>Hello World</h1>');
});

server.listen(8443);
copy
```

####  `http2.connect(authority[, options][, listener])`[#](https://nodejs.org/docs/latest/api/http2.html#http2connectauthority-options-listener)
Added in: v8.4.0History Version | Changes
---|---
v15.10.0, v14.16.0, v12.21.0, v10.24.0 | Added `unknownProtocolTimeout` option with a default of 10000.
v14.4.0, v12.18.0, v10.21.0 | Added `maxSettings` option with a default of 32.
v13.0.0 | The `PADDING_STRATEGY_CALLBACK` has been made equivalent to providing `PADDING_STRATEGY_ALIGNED` and `selectPadding` has been removed.
v8.9.3 | Added the `maxOutstandingPings` option with a default limit of 10.
v8.9.3 | Added the `maxHeaderListPairs` option with a default limit of 128 header pairs.
  * `authority` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) The remote HTTP/2 server to connect to. This must be in the form of a minimal, valid URL with the `http://` or `https://` prefix, host name, and IP port (if a non-default port is used). Userinfo (user ID and password), path, querystring, and fragment details in the URL will be ignored.
  * `options`
    * `maxDeflateDynamicTableSize` **Default:** `4Kib`.
    * `maxSettings` `SETTINGS` frame. The minimum value allowed is `1`. **Default:** `32`.
    * `maxSessionMemory``Http2Session` is permitted to use. The value is expressed in terms of number of megabytes, e.g. `1` equal 1 megabyte. The minimum value allowed is `1`. This is a credit based limit, existing `Http2Stream`s may cause this limit to be exceeded, but new `Http2Stream` instances will be rejected while this limit is exceeded. The current number of `Http2Stream` sessions, the current memory use of the header compression tables, current data queued to be sent, and unacknowledged `PING` and `SETTINGS` frames are all counted towards the current limit. **Default:** `10`.
    * `maxHeaderListPairs` [`server.maxHeadersCount`](https://nodejs.org/docs/latest/api/http.html#servermaxheaderscount) or [`request.maxHeadersCount`](https://nodejs.org/docs/latest/api/http.html#requestmaxheaderscount) in the `node:http` module. The minimum value is `1`. **Default:** `128`.
    * `maxOutstandingPings` **Default:** `10`.
    * `maxReservedRemoteStreams` 32-1. A negative value sets this option to the maximum allowed value. **Default:** `200`.
    * `maxSendHeaderBlockLength` `'frameError'` event being emitted and the stream being closed and destroyed.
    * `paddingStrategy` `HEADERS` and `DATA` frames. **Default:** `http2.constants.PADDING_STRATEGY_NONE`. Value may be one of:
      * `http2.constants.PADDING_STRATEGY_NONE`: No padding is applied.
      * `http2.constants.PADDING_STRATEGY_MAX`: The maximum amount of padding, determined by the internal implementation, is applied.
      * `http2.constants.PADDING_STRATEGY_ALIGNED`: Attempts to apply enough padding to ensure that the total frame length, including the 9-byte header, is a multiple of 8. For each frame, there is a maximum allowed number of padding bytes that is determined by current flow control state and settings. If this maximum is less than the calculated amount needed to ensure alignment, the maximum is used and the total frame length is not necessarily aligned at 8 bytes.
    * `peerMaxConcurrentStreams` `SETTINGS` frame had been received. Will be overridden if the remote peer sets its own value for `maxConcurrentStreams`. **Default:** `100`.
    * `protocol` `authority`. Value may be either `'http:'` or `'https:'`. **Default:** `'https:'`
    * `settings` [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object) The initial settings to send to the remote peer upon connection.
    * `remoteCustomSettings` `CustomSettings`-property of the received remoteSettings. Please see the `CustomSettings`-property of the `Http2Settings` object for more information, on the allowed setting types.
    * `createConnection` `URL` instance passed to `connect` and the `options` object, and returns any [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) stream that is to be used as the connection for this session.
    * `...options` [`net.connect()`](https://nodejs.org/docs/latest/api/net.html#netconnect) or [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback) options can be provided.
    * `unknownProtocolTimeout` [`'unknownProtocol'`](https://nodejs.org/docs/latest/api/http2.html#event-unknownprotocol) event is emitted. If the socket has not been destroyed by that time the server will destroy it. **Default:** `10000`.
    * `strictFieldWhitespaceValidation` `true`, it turns on strict leading and trailing whitespace validation for HTTP/2 header field names and values as per **Default:** `true`.
  * `listener` [`'connect'`](https://nodejs.org/docs/latest/api/http2.html#event-connect) event.
  * Returns: [`<ClientHttp2Session>`](https://nodejs.org/docs/latest/api/http2.html#class-clienthttp2session)


Returns a `ClientHttp2Session` instance.
```
import { connect } from 'node:http2';
const client = connect('https://localhost:1234');

/* Use the client */

client.close();
const http2 = require('node:http2');
const client = http2.connect('https://localhost:1234');

/* Use the client */

client.close();
copy
```

####  `http2.constants`[#](https://nodejs.org/docs/latest/api/http2.html#http2constants)
Added in: v8.4.0
##### Error codes for `RST_STREAM` and `GOAWAY`[#](https://nodejs.org/docs/latest/api/http2.html#error-codes-for-rst-stream-and-goaway)
Value | Name | Constant
---|---|---
`0x00` | No Error | `http2.constants.NGHTTP2_NO_ERROR`
`0x01` | Protocol Error | `http2.constants.NGHTTP2_PROTOCOL_ERROR`
`0x02` | Internal Error | `http2.constants.NGHTTP2_INTERNAL_ERROR`
`0x03` | Flow Control Error | `http2.constants.NGHTTP2_FLOW_CONTROL_ERROR`
`0x04` | Settings Timeout | `http2.constants.NGHTTP2_SETTINGS_TIMEOUT`
`0x05` | Stream Closed | `http2.constants.NGHTTP2_STREAM_CLOSED`
`0x06` | Frame Size Error | `http2.constants.NGHTTP2_FRAME_SIZE_ERROR`
`0x07` | Refused Stream | `http2.constants.NGHTTP2_REFUSED_STREAM`
`0x08` | Cancel | `http2.constants.NGHTTP2_CANCEL`
`0x09` | Compression Error | `http2.constants.NGHTTP2_COMPRESSION_ERROR`
`0x0a` | Connect Error | `http2.constants.NGHTTP2_CONNECT_ERROR`
`0x0b` | Enhance Your Calm | `http2.constants.NGHTTP2_ENHANCE_YOUR_CALM`
`0x0c` | Inadequate Security | `http2.constants.NGHTTP2_INADEQUATE_SECURITY`
`0x0d` | HTTP/1.1 Required | `http2.constants.NGHTTP2_HTTP_1_1_REQUIRED`
The `'timeout'` event is emitted when there is no activity on the Server for a given number of milliseconds set using `http2server.setTimeout()`.
####  `http2.getDefaultSettings()`[#](https://nodejs.org/docs/latest/api/http2.html#http2getdefaultsettings)
Added in: v8.4.0
  * Returns: [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object)


Returns an object containing the default settings for an `Http2Session` instance. This method returns a new object instance every time it is called so instances returned may be safely modified for use.
####  `http2.getPackedSettings([settings])`[#](https://nodejs.org/docs/latest/api/http2.html#http2getpackedsettingssettings)
Added in: v8.4.0
  * `settings` [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object)
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Returns a `Buffer` instance containing serialized representation of the given HTTP/2 settings as specified in the `HTTP2-Settings` header field.
```
import { getPackedSettings } from 'node:http2';

const packed = getPackedSettings({ enablePush: false });

console.log(packed.toString('base64'));
// Prints: AAIAAAAA
const http2 = require('node:http2');

const packed = http2.getPackedSettings({ enablePush: false });

console.log(packed.toString('base64'));
// Prints: AAIAAAAA
copy
```

####  `http2.getUnpackedSettings(buf)`[#](https://nodejs.org/docs/latest/api/http2.html#http2getunpackedsettingsbuf)
Added in: v8.4.0
  * `buf` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: [`<HTTP/2 Settings Object>`](https://nodejs.org/docs/latest/api/http2.html#settings-object)


Returns a [HTTP/2 Settings Object](https://nodejs.org/docs/latest/api/http2.html#settings-object) containing the deserialized settings from the given `Buffer` as generated by `http2.getPackedSettings()`.
####  `http2.performServerHandshake(socket[, options])`[#](https://nodejs.org/docs/latest/api/http2.html#http2performserverhandshakesocket-options)
Added in: v21.7.0, v20.12.0
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)
  * `options` [`http2.createServer()`](https://nodejs.org/docs/latest/api/http2.html#http2createserveroptions-onrequesthandler) option can be provided.
  * Returns: [`<ServerHttp2Session>`](https://nodejs.org/docs/latest/api/http2.html#class-serverhttp2session)


Create an HTTP/2 server session from an existing socket.
####  `http2.sensitiveHeaders`[#](https://nodejs.org/docs/latest/api/http2.html#http2sensitiveheaders)
Added in: v15.0.0, v14.18.0
  * Type:


This symbol can be set as a property on the HTTP/2 headers object with an array value in order to provide a list of headers considered sensitive. See [Sensitive headers](https://nodejs.org/docs/latest/api/http2.html#sensitive-headers) for more details.
#### Headers object[#](https://nodejs.org/docs/latest/api/http2.html#headers-object)
Headers are represented as own-properties on JavaScript objects. The property keys will be serialized to lower-case. Property values should be strings (if they are not they will be coerced to strings) or an `Array` of strings (in order to send more than one value per header field).
```
const headers = {
  ':status': '200',
  'content-type': 'text-plain',
  'ABC': ['has', 'more', 'than', 'one', 'value'],
};

stream.respond(headers);
copy
```

Header objects passed to callback functions will have a `null` prototype. This means that normal JavaScript object methods such as `Object.prototype.toString()` and `Object.prototype.hasOwnProperty()` will not work.
For incoming headers:
  * The `:status` header is converted to `number`.
  * Duplicates of `:status`, `:method`, `:authority`, `:scheme`, `:path`, `:protocol`, `age`, `authorization`, `access-control-allow-credentials`, `access-control-max-age`, `access-control-request-method`, `content-encoding`, `content-language`, `content-length`, `content-location`, `content-md5`, `content-range`, `content-type`, `date`, `dnt`, `etag`, `expires`, `from`, `host`, `if-match`, `if-modified-since`, `if-none-match`, `if-range`, `if-unmodified-since`, `last-modified`, `location`, `max-forwards`, `proxy-authorization`, `range`, `referer`,`retry-after`, `tk`, `upgrade-insecure-requests`, `user-agent` or `x-content-type-options` are discarded.
  * `set-cookie` is always an array. Duplicates are added to the array.
  * For duplicate `cookie` headers, the values are joined together with '; '.
  * For all other headers, the values are joined together with ', '.

```
import { createServer } from 'node:http2';
const server = createServer();
server.on('stream', (stream, headers) => {
  console.log(headers[':path']);
  console.log(headers.ABC);
});
const http2 = require('node:http2');
const server = http2.createServer();
server.on('stream', (stream, headers) => {
  console.log(headers[':path']);
  console.log(headers.ABC);
});
copy
```

##### Raw headers[#](https://nodejs.org/docs/latest/api/http2.html#raw-headers)
In some APIs, in addition to object format, headers can also be passed or accessed as a raw flat array, preserving details of ordering and duplicate keys to match the raw transmission format.
In this format the keys and values are in the same list. It is _not_ a list of tuples. So, the even-numbered offsets are key values, and the odd-numbered offsets are the associated values. Duplicate headers are not merged and so each key-value pair will appear separately.
This can be useful for cases such as proxies, where existing headers should be exactly forwarded as received, or as a performance optimization when the headers are already available in raw format.
```
const rawHeaders = [
  ':status',
  '404',
  'content-type',
  'text/plain',
];

stream.respond(rawHeaders);
copy
```

##### Sensitive headers[#](https://nodejs.org/docs/latest/api/http2.html#sensitive-headers)
HTTP2 headers can be marked as sensitive, which means that the HTTP/2 header compression algorithm will never index them. This can make sense for header values with low entropy and that may be considered valuable to an attacker, for example `Cookie` or `Authorization`. To achieve this, add the header name to the `[http2.sensitiveHeaders]` property as an array:
```
const headers = {
  ':status': '200',
  'content-type': 'text-plain',
  'cookie': 'some-cookie',
  'other-sensitive-header': 'very secret data',
  [http2.sensitiveHeaders]: ['cookie', 'other-sensitive-header'],
};

stream.respond(headers);
copy
```

For some headers, such as `Authorization` and short `Cookie` headers, this flag is set automatically.
This property is also set for received headers. It will contain the names of all headers marked as sensitive, including ones marked that way automatically.
For raw headers, this should still be set as a property on the array, like `rawHeadersArray[http2.sensitiveHeaders] = ['cookie']`, not as a separate key and value pair within the array itself.
#### Settings object[#](https://nodejs.org/docs/latest/api/http2.html#settings-object)
Added in: v8.4.0History Version | Changes
---|---
v12.12.0 | The `maxConcurrentStreams` setting is stricter.
v8.9.3 | The `maxHeaderListSize` setting is now strictly enforced.
The `http2.getDefaultSettings()`, `http2.getPackedSettings()`, `http2.createServer()`, `http2.createSecureServer()`, `http2session.settings()`, `http2session.localSettings`, and `http2session.remoteSettings` APIs either return or receive as input an object that defines configuration settings for an `Http2Session` object. These objects are ordinary JavaScript objects containing the following properties.
  * `headerTableSize` 32-1. **Default:** `4096`.
  * `enablePush` `true` if HTTP/2 Push Streams are to be permitted on the `Http2Session` instances. **Default:** `true`.
  * `initialWindowSize`  _sender's_ initial window size in bytes for stream-level flow control. The minimum allowed value is 0. The maximum allowed value is 232-1. **Default:** `65535`.
  * `maxFrameSize` 24-1. **Default:** `16384`.
  * `maxConcurrentStreams` `Http2Session`. There is no default value which implies, at least theoretically, 232-1 streams may be open concurrently at any given time in an `Http2Session`. The minimum value is 0. The maximum allowed value is 232-1. **Default:** `4294967295`.
  * `maxHeaderListSize` 32-1. **Default:** `65535`.
  * `maxHeaderSize` `maxHeaderListSize`.
  * `enableConnectProtocol``true` if the "Extended Connect Protocol" defined by `enableConnectProtocol` setting has been enabled for a given `Http2Session`, it cannot be disabled. **Default:** `false`.
  * `customSettings` `remoteCustomSettings` options of the server or client object. Do not mix the `customSettings`-mechanism for a settings id with interfaces for the natively handled settings, in case a setting becomes natively supported in a future node version.


All additional properties on the settings object are ignored.
#### Error handling[#](https://nodejs.org/docs/latest/api/http2.html#error-handling)
There are several types of error conditions that may arise when using the `node:http2` module:
Validation errors occur when an incorrect argument, option, or setting value is passed in. These will always be reported by a synchronous `throw`.
State errors occur when an action is attempted at an incorrect time (for instance, attempting to send data on a stream after it has closed). These will be reported using either a synchronous `throw` or via an `'error'` event on the `Http2Stream`, `Http2Session` or HTTP/2 Server objects, depending on where and when the error occurs.
Internal errors occur when an HTTP/2 session fails unexpectedly. These will be reported via an `'error'` event on the `Http2Session` or HTTP/2 Server objects.
Protocol errors occur when various HTTP/2 protocol constraints are violated. These will be reported using either a synchronous `throw` or via an `'error'` event on the `Http2Stream`, `Http2Session` or HTTP/2 Server objects, depending on where and when the error occurs.
#### Invalid character handling in header names and values[#](https://nodejs.org/docs/latest/api/http2.html#invalid-character-handling-in-header-names-and-values)
The HTTP/2 implementation applies stricter handling of invalid characters in HTTP header names and values than the HTTP/1 implementation.
Header field names are _case-insensitive_ and are transmitted over the wire strictly as lower-case strings. The API provided by Node.js allows header names to be set as mixed-case strings (e.g. `Content-Type`) but will convert those to lower-case (e.g. `content-type`) upon transmission.
Header field-names _must only_ contain one or more of the following ASCII characters: `a`-`z`, `A`-`Z`, `0`-`9`, `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `.`, `^`, `_`, ``` (backtick), `|`, and `~`.
Using invalid characters within an HTTP header field name will cause the stream to be closed with a protocol error being reported.
Header field values are handled with more leniency but _should_ not contain new-line or carriage return characters and _should_ be limited to US-ASCII characters, per the requirements of the HTTP specification.
#### Push streams on the client[#](https://nodejs.org/docs/latest/api/http2.html#push-streams-on-the-client)
To receive pushed streams on the client, set a listener for the `'stream'` event on the `ClientHttp2Session`:
```
import { connect } from 'node:http2';

const client = connect('http://localhost');

client.on('stream', (pushedStream, requestHeaders) => {
  pushedStream.on('push', (responseHeaders) => {
    // Process response headers
  });
  pushedStream.on('data', (chunk) => { /* handle pushed data */ });
});

const req = client.request({ ':path': '/' });
const http2 = require('node:http2');

const client = http2.connect('http://localhost');

client.on('stream', (pushedStream, requestHeaders) => {
  pushedStream.on('push', (responseHeaders) => {
    // Process response headers
  });
  pushedStream.on('data', (chunk) => { /* handle pushed data */ });
});

const req = client.request({ ':path': '/' });
copy
```

#### Supporting the `CONNECT` method[#](https://nodejs.org/docs/latest/api/http2.html#supporting-the-connect-method)
The `CONNECT` method is used to allow an HTTP/2 server to be used as a proxy for TCP/IP connections.
A simple TCP Server:
```
import { createServer } from 'node:net';

const server = createServer((socket) => {
  let name = '';
  socket.setEncoding('utf8');
  socket.on('data', (chunk) => name += chunk);
  socket.on('end', () => socket.end(`hello ${name}`));
});

server.listen(8000);
const net = require('node:net');

const server = net.createServer((socket) => {
  let name = '';
  socket.setEncoding('utf8');
  socket.on('data', (chunk) => name += chunk);
  socket.on('end', () => socket.end(`hello ${name}`));
});

server.listen(8000);
copy
```

An HTTP/2 CONNECT proxy:
```
import { createServer, constants } from 'node:http2';
const { NGHTTP2_REFUSED_STREAM, NGHTTP2_CONNECT_ERROR } = constants;
import { connect } from 'node:net';

const proxy = createServer();
proxy.on('stream', (stream, headers) => {
  if (headers[':method'] !== 'CONNECT') {
    // Only accept CONNECT requests
    stream.close(NGHTTP2_REFUSED_STREAM);
    return;
  }
  const auth = new URL(`tcp://${headers[':authority']}`);
  // It's a very good idea to verify that hostname and port are
  // things this proxy should be connecting to.
  const socket = connect(auth.port, auth.hostname, () => {
    stream.respond();
    socket.pipe(stream);
    stream.pipe(socket);
  });
  socket.on('error', (error) => {
    stream.close(NGHTTP2_CONNECT_ERROR);
  });
});

proxy.listen(8001);
const http2 = require('node:http2');
const { NGHTTP2_REFUSED_STREAM } = http2.constants;
const net = require('node:net');

const proxy = http2.createServer();
proxy.on('stream', (stream, headers) => {
  if (headers[':method'] !== 'CONNECT') {
    // Only accept CONNECT requests
    stream.close(NGHTTP2_REFUSED_STREAM);
    return;
  }
  const auth = new URL(`tcp://${headers[':authority']}`);
  // It's a very good idea to verify that hostname and port are
  // things this proxy should be connecting to.
  const socket = net.connect(auth.port, auth.hostname, () => {
    stream.respond();
    socket.pipe(stream);
    stream.pipe(socket);
  });
  socket.on('error', (error) => {
    stream.close(http2.constants.NGHTTP2_CONNECT_ERROR);
  });
});

proxy.listen(8001);
copy
```

An HTTP/2 CONNECT client:
```
import { connect, constants } from 'node:http2';

const client = connect('http://localhost:8001');

// Must not specify the ':path' and ':scheme' headers
// for CONNECT requests or an error will be thrown.
const req = client.request({
  ':method': 'CONNECT',
  ':authority': 'localhost:8000',
});

req.on('response', (headers) => {
  console.log(headers[constants.HTTP2_HEADER_STATUS]);
});
let data = '';
req.setEncoding('utf8');
req.on('data', (chunk) => data += chunk);
req.on('end', () => {
  console.log(`The server says: ${data}`);
  client.close();
});
req.end('Jane');
const http2 = require('node:http2');

const client = http2.connect('http://localhost:8001');

// Must not specify the ':path' and ':scheme' headers
// for CONNECT requests or an error will be thrown.
const req = client.request({
  ':method': 'CONNECT',
  ':authority': 'localhost:8000',
});

req.on('response', (headers) => {
  console.log(headers[http2.constants.HTTP2_HEADER_STATUS]);
});
let data = '';
req.setEncoding('utf8');
req.on('data', (chunk) => data += chunk);
req.on('end', () => {
  console.log(`The server says: ${data}`);
  client.close();
});
req.end('Jane');
copy
```

#### The extended `CONNECT` protocol[#](https://nodejs.org/docs/latest/api/http2.html#the-extended-connect-protocol)
`Http2Stream` using the `CONNECT` method as a tunnel for other communication protocols (such as WebSockets).
The use of the Extended CONNECT Protocol is enabled by HTTP/2 servers by using the `enableConnectProtocol` setting:
```
import { createServer } from 'node:http2';
const settings = { enableConnectProtocol: true };
const server = createServer({ settings });
const http2 = require('node:http2');
const settings = { enableConnectProtocol: true };
const server = http2.createServer({ settings });
