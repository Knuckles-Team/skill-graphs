## HTTP[#](https://nodejs.org/docs/latest/api/http.html#http)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
This module, containing both a client and server, can be imported via `require('node:http')` (CommonJS) or `import * as http from 'node:http'` (ES module).
The HTTP interfaces in Node.js are designed to support many features of the protocol which have been traditionally difficult to use. In particular, large, possibly chunk-encoded, messages. The interface is careful to never buffer entire requests or responses, so the user is able to stream data.
HTTP message headers are represented by an object like this:
```
{ "content-length": "123",
  "content-type": "text/plain",
  "connection": "keep-alive",
  "host": "example.com",
  "accept": "*/*" }
copy
```

Keys are lowercased. Values are not modified.
In order to support the full spectrum of possible HTTP applications, the Node.js HTTP API is very low-level. It deals with stream handling and message parsing only. It parses a message into headers and body but it does not parse the actual headers or the body.
See [`message.headers`](https://nodejs.org/docs/latest/api/http.html#messageheaders) for details on how duplicate headers are handled.
The raw headers as they were received are retained in the `rawHeaders` property, which is an array of `[key, value, key2, value2, ...]`. For example, the previous message header object might have a `rawHeaders` list like the following:
```
[ 'ConTent-Length', '123456',
  'content-LENGTH', '123',
  'content-type', 'text/plain',
  'CONNECTION', 'keep-alive',
  'Host', 'example.com',
  'accepT', '*/*' ]
copy
```

### Class: `http.Agent`[#](https://nodejs.org/docs/latest/api/http.html#class-httpagent)
Added in: v0.3.4
An `Agent` is responsible for managing connection persistence and reuse for HTTP clients. It maintains a queue of pending requests for a given host and port, reusing a single socket connection for each until the queue is empty, at which time the socket is either destroyed or put into a pool where it is kept to be used again for requests to the same host and port. Whether it is destroyed or pooled depends on the `keepAlive` [option](https://nodejs.org/docs/latest/api/http.html#new-agentoptions).
Pooled connections have TCP Keep-Alive enabled for them, but servers may still close idle connections, in which case they will be removed from the pool and a new connection will be made when a new HTTP request is made for that host and port. Servers may also refuse to allow multiple requests over the same connection, in which case the connection will have to be remade for every request and cannot be pooled. The `Agent` will still make the requests to that server, but each one will occur over a new connection.
When a connection is closed by the client or the server, it is removed from the pool. Any unused sockets in the pool will be unrefed so as not to keep the Node.js process running when there are no outstanding requests. (see [`socket.unref()`](https://nodejs.org/docs/latest/api/net.html#socketunref)).
It is good practice, to [`destroy()`](https://nodejs.org/docs/latest/api/http.html#agentdestroy) an `Agent` instance when it is no longer in use, because unused sockets consume OS resources.
Sockets are removed from an agent when the socket emits either a `'close'` event or an `'agentRemove'` event. When intending to keep one HTTP request open for a long time without keeping it in the agent, something like the following may be done:
```
http.get(options, (res) => {
  // Do stuff
}).on('socket', (socket) => {
  socket.emit('agentRemove');
});
copy
```

An agent may also be used for an individual request. By providing `{agent: false}` as an option to the `http.get()` or `http.request()` functions, a one-time use `Agent` with default options will be used for the client connection.
`agent:false`:
```
http.get({
  hostname: 'localhost',
  port: 80,
  path: '/',
  agent: false,  // Create a new agent just for this one request
}, (res) => {
  // Do stuff with response
});
copy
```

####  `new Agent([options])`[#](https://nodejs.org/docs/latest/api/http.html#new-agentoptions)
Added in: v0.3.4History Version | Changes
---|---
v24.7.0, v22.20.0 | Add support for `agentKeepAliveTimeoutBuffer`.
v24.5.0 | Add support for `proxyEnv`.
v24.5.0 | Add support for `defaultPort` and `protocol`.
v15.6.0, v14.17.0 | Change the default scheduling from 'fifo' to 'lifo'.
v14.5.0, v12.19.0 | Add `maxTotalSockets` option to agent constructor.
v14.5.0, v12.20.0 | Add `scheduling` option to specify the free socket scheduling strategy.
  * `options`
    * `keepAlive` `keep-alive` value of the `Connection` header. The `Connection: keep-alive` header is always sent when using an agent except when the `Connection` header is explicitly specified or when the `keepAlive` and `maxSockets` options are respectively set to `false` and `Infinity`, in which case `Connection: close` will be used. **Default:** `false`.
    * `keepAliveMsecs` `keepAlive` option, specifies the [initial delay](https://nodejs.org/docs/latest/api/net.html#socketsetkeepaliveenable-initialdelay) for TCP Keep-Alive packets. Ignored when the `keepAlive` option is `false` or `undefined`. **Default:** `1000`.
    * `agentKeepAliveTimeoutBuffer` `keep-alive: timeout=...` hint when determining socket expiration time. This buffer helps ensure the agent closes the socket slightly before the server does, reducing the chance of sending a request on a socket that’s about to be closed by the server. **Default:** `1000`.
    * `maxSockets` `maxSockets` value is reached. If the host attempts to open more connections than `maxSockets`, the additional requests will enter into a pending request queue, and will enter active connection state when an existing connection terminates. This makes sure there are at most `maxSockets` active connections at any point in time, from a given host. **Default:** `Infinity`.
    * `maxTotalSockets` **Default:** `Infinity`.
    * `maxFreeSockets` `keepAlive` is set to `true`. **Default:** `256`.
    * `scheduling` `'fifo'` or `'lifo'`. The main difference between the two scheduling strategies is that `'lifo'` selects the most recently used socket, while `'fifo'` selects the least recently used socket. In case of a low rate of request per second, the `'lifo'` scheduling will lower the risk of picking a socket that might have been closed by the server due to inactivity. In case of a high rate of request per second, the `'fifo'` scheduling will maximize the number of open sockets, while the `'lifo'` scheduling will keep it as low as possible. **Default:** `'lifo'`.
    * `timeout`
    * `proxyEnv` [Built-in Proxy Support](https://nodejs.org/docs/latest/api/http.html#built-in-proxy-support) for details. **Default:** `undefined`
      * `HTTP_PROXY`
      * `HTTPS_PROXY`
      * `NO_PROXY`
      * `http_proxy` `HTTP_PROXY`. If both are set, `http_proxy` takes precedence.
      * `https_proxy` `HTTPS_PROXY`. If both are set, `https_proxy` takes precedence.
      * `no_proxy` `NO_PROXY`. If both are set, `no_proxy` takes precedence.
    * `defaultPort` **Default:** `80`.
    * `protocol` **Default:** `'http:'`.


`options` in [`socket.connect()`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener) are also supported.
To configure any of them, a custom [`http.Agent`](https://nodejs.org/docs/latest/api/http.html#class-httpagent) instance must be created.
```
import { Agent, request } from 'node:http';
const keepAliveAgent = new Agent({ keepAlive: true });
options.agent = keepAliveAgent;
request(options, onResponseCallback);
const http = require('node:http');
const keepAliveAgent = new http.Agent({ keepAlive: true });
options.agent = keepAliveAgent;
http.request(options, onResponseCallback);
copy
```

####  `agent.createConnection(options[, callback])`[#](https://nodejs.org/docs/latest/api/http.html#agentcreateconnectionoptions-callback)
Added in: v0.11.4
  * `options` [`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionoptions-connectlistener) for the format of the options. For custom agents, this object is passed to the custom `createConnection` function.
  * `callback` `createConnection` implementation when the socket is created, especially for asynchronous operations.
    * `err`
    * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) The created socket.
  * Returns: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) The created socket. This is returned by the default implementation or by a custom synchronous `createConnection` implementation. If a custom `createConnection` uses the `callback` for asynchronous operation, this return value might not be the primary way to obtain the socket.


Produces a socket/stream to be used for HTTP requests.
By default, this function behaves identically to [`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionoptions-connectlistener), synchronously returning the created socket. The optional `callback` parameter in the signature is **not** used by this default implementation.
However, custom agents may override this method to provide greater flexibility, for example, to create sockets asynchronously. When overriding `createConnection`:
  1. **Synchronous socket creation** : The overriding method can return the socket/stream directly.
  2. **Asynchronous socket creation** : The overriding method can accept the `callback` and pass the created socket/stream to it (e.g., `callback(null, newSocket)`). If an error occurs during socket creation, it should be passed as the first argument to the `callback` (e.g., `callback(err)`).


The agent will call the provided `createConnection` function with `options` and this internal `callback`. The `callback` provided by the agent has a signature of `(err, stream)`.
####  `agent.keepSocketAlive(socket)`[#](https://nodejs.org/docs/latest/api/http.html#agentkeepsocketalivesocket)
Added in: v8.1.0
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


Called when `socket` is detached from a request and could be persisted by the `Agent`. Default behavior is to:
```
socket.setKeepAlive(true, this.keepAliveMsecs);
socket.unref();
return true;
copy
```

This method can be overridden by a particular `Agent` subclass. If this method returns a falsy value, the socket will be destroyed instead of persisting it for use with the next request.
The `socket` argument can be an instance of [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket), a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex).
####  `agent.reuseSocket(socket, request)`[#](https://nodejs.org/docs/latest/api/http.html#agentreusesocketsocket-request)
Added in: v8.1.0
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)
  * `request` [`<http.ClientRequest>`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest)


Called when `socket` is attached to `request` after being persisted because of the keep-alive options. Default behavior is to:
```
socket.ref();
copy
```

This method can be overridden by a particular `Agent` subclass.
The `socket` argument can be an instance of [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket), a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex).
####  `agent.destroy()`[#](https://nodejs.org/docs/latest/api/http.html#agentdestroy)
Added in: v0.11.4
Destroy any sockets that are currently in use by the agent.
It is usually not necessary to do this. However, if using an agent with `keepAlive` enabled, then it is best to explicitly shut down the agent when it is no longer needed. Otherwise, sockets might stay open for quite a long time before the server terminates them.
####  `agent.freeSockets`[#](https://nodejs.org/docs/latest/api/http.html#agentfreesockets)
Added in: v0.11.4History Version | Changes
---|---
v16.0.0 | The property now has a `null` prototype.
  * Type:


An object which contains arrays of sockets currently awaiting use by the agent when `keepAlive` is enabled. Do not modify.
Sockets in the `freeSockets` list will be automatically destroyed and removed from the array on `'timeout'`.
####  `agent.getName([options])`[#](https://nodejs.org/docs/latest/api/http.html#agentgetnameoptions)
Added in: v0.11.4History Version | Changes
---|---
v17.7.0, v16.15.0 | The `options` parameter is now optional.
  * `options`
    * `host`
    * `port`
    * `localAddress`
    * `family` `undefined`.
  * Returns:


Get a unique name for a set of request options, to determine whether a connection can be reused. For an HTTP agent, this returns `host:port:localAddress` or `host:port:localAddress:family`. For an HTTPS agent, the name includes the CA, cert, ciphers, and other HTTPS/TLS-specific options that determine socket reusability.
####  `agent.maxFreeSockets`[#](https://nodejs.org/docs/latest/api/http.html#agentmaxfreesockets)
Added in: v0.11.7
  * Type:


By default set to 256. For agents with `keepAlive` enabled, this sets the maximum number of sockets that will be left open in the free state.
####  `agent.maxSockets`[#](https://nodejs.org/docs/latest/api/http.html#agentmaxsockets)
Added in: v0.3.6
  * Type:


By default set to `Infinity`. Determines how many concurrent sockets the agent can have open per origin. Origin is the returned value of [`agent.getName()`](https://nodejs.org/docs/latest/api/http.html#agentgetnameoptions).
####  `agent.maxTotalSockets`[#](https://nodejs.org/docs/latest/api/http.html#agentmaxtotalsockets)
Added in: v14.5.0, v12.19.0
  * Type:


By default set to `Infinity`. Determines how many concurrent sockets the agent can have open. Unlike `maxSockets`, this parameter applies across all origins.
####  `agent.requests`[#](https://nodejs.org/docs/latest/api/http.html#agentrequests)
Added in: v0.5.9History Version | Changes
---|---
v16.0.0 | The property now has a `null` prototype.
  * Type:


An object which contains queues of requests that have not yet been assigned to sockets. Do not modify.
####  `agent.sockets`[#](https://nodejs.org/docs/latest/api/http.html#agentsockets)
Added in: v0.3.6History Version | Changes
---|---
v16.0.0 | The property now has a `null` prototype.
  * Type:


An object which contains arrays of sockets currently in use by the agent. Do not modify.
### Class: `http.ClientRequest`[#](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest)
Added in: v0.1.17
  * Extends: [`<http.OutgoingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpoutgoingmessage)


This object is created internally and returned from [`http.request()`](https://nodejs.org/docs/latest/api/http.html#httprequestoptions-callback). It represents an _in-progress_ request whose header has already been queued. The header is still mutable using the [`setHeader(name, value)`](https://nodejs.org/docs/latest/api/http.html#requestsetheadername-value), [`getHeader(name)`](https://nodejs.org/docs/latest/api/http.html#requestgetheadername), [`removeHeader(name)`](https://nodejs.org/docs/latest/api/http.html#requestremoveheadername) API. The actual header will be sent along with the first data chunk or when calling [`request.end()`](https://nodejs.org/docs/latest/api/http.html#requestenddata-encoding-callback).
To get the response, add a listener for [`'response'`](https://nodejs.org/docs/latest/api/http.html#event-response) to the request object. [`'response'`](https://nodejs.org/docs/latest/api/http.html#event-response) will be emitted from the request object when the response headers have been received. The [`'response'`](https://nodejs.org/docs/latest/api/http.html#event-response) event is executed with one argument which is an instance of [`http.IncomingMessage`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage).
During the [`'response'`](https://nodejs.org/docs/latest/api/http.html#event-response) event, one can add listeners to the response object; particularly to listen for the `'data'` event.
If no [`'response'`](https://nodejs.org/docs/latest/api/http.html#event-response) handler is added, then the response will be entirely discarded. However, if a [`'response'`](https://nodejs.org/docs/latest/api/http.html#event-response) event handler is added, then the data from the response object **must** be consumed, either by calling `response.read()` whenever there is a `'readable'` event, or by adding a `'data'` handler, or by calling the `.resume()` method. Until the data is consumed, the `'end'` event will not fire. Also, until the data is read it will consume memory that can eventually lead to a 'process out of memory' error.
For backward compatibility, `res` will only emit `'error'` if there is an `'error'` listener registered.
Set `Content-Length` header to limit the response body size. If [`response.strictContentLength`](https://nodejs.org/docs/latest/api/http.html#responsestrictcontentlength) is set to `true`, mismatching the `Content-Length` header value will result in an `Error` being thrown, identified by `code:` [`'ERR_HTTP_CONTENT_LENGTH_MISMATCH'`](https://nodejs.org/docs/latest/api/errors.html#err_http_content_length_mismatch).
`Content-Length` value should be in bytes, not characters. Use [`Buffer.byteLength()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferbytelengthstring-encoding) to determine the length of the body in bytes.
#### Event: `'abort'`[#](https://nodejs.org/docs/latest/api/http.html#event-abort)
Added in: v1.4.1Deprecated in: v17.0.0, v16.12.0
Stability: 0 - Deprecated. Listen for the `'close'` event instead.
Emitted when the request has been aborted by the client. This event is only emitted on the first call to `abort()`.
#### Event: `'close'`[#](https://nodejs.org/docs/latest/api/http.html#event-close)
Added in: v0.5.4
Indicates that the request is completed, or its underlying connection was terminated prematurely (before the response completion).
#### Event: `'connect'`[#](https://nodejs.org/docs/latest/api/http.html#event-connect)
Added in: v0.7.0
  * `response` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)
  * `head` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Emitted each time a server responds to a request with a `CONNECT` method. If this event is not being listened for, clients receiving a `CONNECT` method will have their connections closed.
This event is guaranteed to be passed an instance of the [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) class, a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), unless the user specifies a socket type other than [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
A client and server pair demonstrating how to listen for the `'connect'` event:
```
import { createServer, request } from 'node:http';
import { connect } from 'node:net';
import { URL } from 'node:url';

// Create an HTTP tunneling proxy
const proxy = createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('okay');
});
proxy.on('connect', (req, clientSocket, head) => {
  // Connect to an origin server
  const { port, hostname } = new URL(`http://${req.url}`);
  const serverSocket = connect(port || 80, hostname, () => {
    clientSocket.write('HTTP/1.1 200 Connection Established\r\n' +
                    'Proxy-agent: Node.js-Proxy\r\n' +
                    '\r\n');
    serverSocket.write(head);
    serverSocket.pipe(clientSocket);
    clientSocket.pipe(serverSocket);
  });
});

// Now that proxy is running
proxy.listen(1337, '127.0.0.1', () => {

  // Make a request to a tunneling proxy
  const options = {
    port: 1337,
    host: '127.0.0.1',
    method: 'CONNECT',
    path: 'www.google.com:80',
  };

  const req = request(options);
  req.end();

  req.on('connect', (res, socket, head) => {
    console.log('got connected!');

    // Make a request over an HTTP tunnel
    socket.write('GET / HTTP/1.1\r\n' +
                 'Host: www.google.com:80\r\n' +
                 'Connection: close\r\n' +
                 '\r\n');
    socket.on('data', (chunk) => {
      console.log(chunk.toString());
    });
    socket.on('end', () => {
      proxy.close();
    });
  });
});
const http = require('node:http');
const net = require('node:net');
const { URL } = require('node:url');

// Create an HTTP tunneling proxy
const proxy = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('okay');
});
proxy.on('connect', (req, clientSocket, head) => {
  // Connect to an origin server
  const { port, hostname } = new URL(`http://${req.url}`);
  const serverSocket = net.connect(port || 80, hostname, () => {
    clientSocket.write('HTTP/1.1 200 Connection Established\r\n' +
                    'Proxy-agent: Node.js-Proxy\r\n' +
                    '\r\n');
    serverSocket.write(head);
    serverSocket.pipe(clientSocket);
    clientSocket.pipe(serverSocket);
  });
});

// Now that proxy is running
proxy.listen(1337, '127.0.0.1', () => {

  // Make a request to a tunneling proxy
  const options = {
    port: 1337,
    host: '127.0.0.1',
    method: 'CONNECT',
    path: 'www.google.com:80',
  };

  const req = http.request(options);
  req.end();

  req.on('connect', (res, socket, head) => {
    console.log('got connected!');

    // Make a request over an HTTP tunnel
    socket.write('GET / HTTP/1.1\r\n' +
                 'Host: www.google.com:80\r\n' +
                 'Connection: close\r\n' +
                 '\r\n');
    socket.on('data', (chunk) => {
      console.log(chunk.toString());
    });
    socket.on('end', () => {
      proxy.close();
    });
  });
});
copy
```

#### Event: `'continue'`[#](https://nodejs.org/docs/latest/api/http.html#event-continue)
Added in: v0.3.2
Emitted when the server sends a '100 Continue' HTTP response, usually because the request contained 'Expect: 100-continue'. This is an instruction that the client should send the request body.
#### Event: `'finish'`[#](https://nodejs.org/docs/latest/api/http.html#event-finish)
Added in: v0.3.6
Emitted when the request has been sent. More specifically, this event is emitted when the last segment of the request headers and body have been handed off to the operating system for transmission over the network. It does not imply that the server has received anything yet.
#### Event: `'information'`[#](https://nodejs.org/docs/latest/api/http.html#event-information)
Added in: v10.0.0
  * `info`
    * `httpVersion`
    * `httpVersionMajor`
    * `httpVersionMinor`
    * `statusCode`
    * `statusMessage`
    * `headers`
    * `rawHeaders`


Emitted when the server sends a 1xx intermediate response (excluding 101 Upgrade). The listeners of this event will receive an object containing the HTTP version, status code, status message, key-value headers object, and array with the raw header names followed by their respective values.
```
import { request } from 'node:http';

const options = {
  host: '127.0.0.1',
  port: 8080,
  path: '/length_request',
};

// Make a request
const req = request(options);
req.end();

req.on('information', (info) => {
  console.log(`Got information prior to main response: ${info.statusCode}`);
});
const http = require('node:http');

const options = {
  host: '127.0.0.1',
  port: 8080,
  path: '/length_request',
};

// Make a request
const req = http.request(options);
req.end();

req.on('information', (info) => {
  console.log(`Got information prior to main response: ${info.statusCode}`);
});
copy
```

101 Upgrade statuses do not fire this event due to their break from the traditional HTTP request/response chain, such as web sockets, in-place TLS upgrades, or HTTP 2.0. To be notified of 101 Upgrade notices, listen for the [`'upgrade'`](https://nodejs.org/docs/latest/api/http.html#event-upgrade) event instead.
#### Event: `'response'`[#](https://nodejs.org/docs/latest/api/http.html#event-response)
Added in: v0.1.0
  * `response` [`<http.IncomingMessage>`](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)


Emitted when a response is received to this request. This event is emitted only once.
#### Event: `'socket'`[#](https://nodejs.org/docs/latest/api/http.html#event-socket)
Added in: v0.5.3
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


This event is guaranteed to be passed an instance of the [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) class, a subclass of [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex), unless the user specifies a socket type other than [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
#### Event: `'timeout'`[#](https://nodejs.org/docs/latest/api/http.html#event-timeout)
Added in: v0.7.8
Emitted when the underlying socket times out from inactivity. This only notifies that the socket has been idle. The request must be destroyed manually.
See also: [`request.setTimeout()`](https://nodejs.org/docs/latest/api/http.html#requestsettimeouttimeout-callback).
