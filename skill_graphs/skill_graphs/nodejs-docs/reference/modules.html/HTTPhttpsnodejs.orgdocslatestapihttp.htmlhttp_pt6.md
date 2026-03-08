    * `port` **Default:** `defaultPort` if set, else `80`.
    * `protocol` **Default:** `'http:'`.
    * `setDefaultHeaders` `Connection`, `Content-Length`, `Transfer-Encoding`, and `Host`. If set to `false` then all necessary headers must be added manually. Defaults to `true`.
    * `setHost` `Host` header. If provided, this overrides `setDefaultHeaders`. Defaults to `true`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal): An AbortSignal that may be used to abort an ongoing request.
    * `socketPath` `host` or `port` is specified, as those specify a TCP Socket.
    * `timeout`
    * `uniqueHeaders` `; `.
  * `callback`
  * Returns: [`<http.ClientRequest>`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest)


`options` in [`socket.connect()`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener) are also supported.
Node.js maintains several connections per server to make HTTP requests. This function allows one to transparently issue requests.
`url` can be a string or a [`URL`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) object. If `url` is a string, it is automatically parsed with [`new URL()`](https://nodejs.org/docs/latest/api/url.html#new-urlinput-base). If it is a [`URL`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) object, it will be automatically converted to an ordinary `options` object.
If both `url` and `options` are specified, the objects are merged, with the `options` properties taking precedence.
The optional `callback` parameter will be added as a one-time listener for the [`'response'`](https://nodejs.org/docs/latest/api/http.html#event-response) event.
`http.request()` returns an instance of the [`http.ClientRequest`](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest) class. The `ClientRequest` instance is a writable stream. If one needs to upload a file with a POST request, then write to the `ClientRequest` object.
```
import http from 'node:http';
import { Buffer } from 'node:buffer';

const postData = JSON.stringify({
  'msg': 'Hello World!',
});

const options = {
  hostname: 'www.google.com',
  port: 80,
  path: '/upload',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(postData),
  },
};

const req = http.request(options, (res) => {
  console.log(`STATUS: ${res.statusCode}`);
  console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
  res.setEncoding('utf8');
  res.on('data', (chunk) => {
    console.log(`BODY: ${chunk}`);
  });
  res.on('end', () => {
    console.log('No more data in response.');
  });
});

req.on('error', (e) => {
  console.error(`problem with request: ${e.message}`);
});

// Write data to request body
req.write(postData);
req.end();
const http = require('node:http');

const postData = JSON.stringify({
  'msg': 'Hello World!',
});

const options = {
  hostname: 'www.google.com',
  port: 80,
  path: '/upload',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(postData),
  },
};

const req = http.request(options, (res) => {
  console.log(`STATUS: ${res.statusCode}`);
  console.log(`HEADERS: ${JSON.stringify(res.headers)}`);
  res.setEncoding('utf8');
  res.on('data', (chunk) => {
    console.log(`BODY: ${chunk}`);
  });
  res.on('end', () => {
    console.log('No more data in response.');
  });
});

req.on('error', (e) => {
  console.error(`problem with request: ${e.message}`);
});

// Write data to request body
req.write(postData);
req.end();
copy
```

In the example `req.end()` was called. With `http.request()` one must always call `req.end()` to signify the end of the request - even if there is no data being written to the request body.
If any error is encountered during the request (be that with DNS resolution, TCP level errors, or actual HTTP parse errors) an `'error'` event is emitted on the returned request object. As with all `'error'` events, if no listeners are registered the error will be thrown.
There are a few special headers that should be noted.
  * Sending a 'Connection: keep-alive' will notify Node.js that the connection to the server should be persisted until the next request.
  * Sending a 'Content-Length' header will disable the default chunked encoding.
  * Sending an 'Expect' header will immediately send the request headers. Usually, when sending 'Expect: 100-continue', both a timeout and a listener for the `'continue'` event should be set. See RFC 2616 Section 8.2.3 for more information.
  * Sending an Authorization header will override using the `auth` option to compute basic authentication.


Example using a [`URL`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) as `options`:
```
const options = new URL('http://abc:xyz@example.com');

const req = http.request(options, (res) => {
  // ...
});
copy
```

In a successful request, the following events will be emitted in the following order:
  * `'socket'`
  * `'response'`
    * `'data'` any number of times, on the `res` object (`'data'` will not be emitted at all if the response body is empty, for instance, in most redirects)
    * `'end'` on the `res` object
  * `'close'`


In the case of a connection error, the following events will be emitted:
  * `'socket'`
  * `'error'`
  * `'close'`


In the case of a premature connection close before the response is received, the following events will be emitted in the following order:
  * `'socket'`
  * `'error'` with an error with message `'Error: socket hang up'` and code `'ECONNRESET'`
  * `'close'`


In the case of a premature connection close after the response is received, the following events will be emitted in the following order:
  * `'socket'`
  * `'response'`
    * `'data'` any number of times, on the `res` object
  * (connection closed here)
  * `'aborted'` on the `res` object
  * `'close'`
  * `'error'` on the `res` object with an error with message `'Error: aborted'` and code `'ECONNRESET'`
  * `'close'` on the `res` object


If `req.destroy()` is called before a socket is assigned, the following events will be emitted in the following order:
  * (`req.destroy()` called here)
  * `'error'` with an error with message `'Error: socket hang up'` and code `'ECONNRESET'`, or the error with which `req.destroy()` was called
  * `'close'`


If `req.destroy()` is called before the connection succeeds, the following events will be emitted in the following order:
  * `'socket'`
  * (`req.destroy()` called here)
  * `'error'` with an error with message `'Error: socket hang up'` and code `'ECONNRESET'`, or the error with which `req.destroy()` was called
  * `'close'`


If `req.destroy()` is called after the response is received, the following events will be emitted in the following order:
  * `'socket'`
  * `'response'`
    * `'data'` any number of times, on the `res` object
  * (`req.destroy()` called here)
  * `'aborted'` on the `res` object
  * `'close'`
  * `'error'` on the `res` object with an error with message `'Error: aborted'` and code `'ECONNRESET'`, or the error with which `req.destroy()` was called
  * `'close'` on the `res` object


If `req.abort()` is called before a socket is assigned, the following events will be emitted in the following order:
  * (`req.abort()` called here)
  * `'abort'`
  * `'close'`


If `req.abort()` is called before the connection succeeds, the following events will be emitted in the following order:
  * `'socket'`
  * (`req.abort()` called here)
  * `'abort'`
  * `'error'` with an error with message `'Error: socket hang up'` and code `'ECONNRESET'`
  * `'close'`


If `req.abort()` is called after the response is received, the following events will be emitted in the following order:
  * `'socket'`
  * `'response'`
    * `'data'` any number of times, on the `res` object
  * (`req.abort()` called here)
  * `'abort'`
  * `'aborted'` on the `res` object
  * `'error'` on the `res` object with an error with message `'Error: aborted'` and code `'ECONNRESET'`.
  * `'close'`
  * `'close'` on the `res` object


Setting the `timeout` option or using the `setTimeout()` function will not abort the request or do anything besides add a `'timeout'` event.
Passing an `AbortSignal` and then calling `abort()` on the corresponding `AbortController` will behave the same way as calling `.destroy()` on the request. Specifically, the `'error'` event will be emitted with an error with the message `'AbortError: The operation was aborted'`, the code `'ABORT_ERR'` and the `cause`, if one was provided.
###  `http.validateHeaderName(name[, label])`[#](https://nodejs.org/docs/latest/api/http.html#httpvalidateheadernamename-label)
Added in: v14.3.0History Version | Changes
---|---
v19.5.0, v18.14.0 | The `label` parameter is added.
  * `name`
  * `label` **Default:** `'Header name'`.


Performs the low-level validations on the provided `name` that are done when `res.setHeader(name, value)` is called.
Passing illegal value as `name` will result in a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) being thrown, identified by `code: 'ERR_INVALID_HTTP_TOKEN'`.
It is not necessary to use this method before passing headers to an HTTP request or response. The HTTP module will automatically validate such headers.
Example:
```
import { validateHeaderName } from 'node:http';

try {
  validateHeaderName('');
} catch (err) {
  console.error(err instanceof TypeError); // --> true
  console.error(err.code); // --> 'ERR_INVALID_HTTP_TOKEN'
  console.error(err.message); // --> 'Header name must be a valid HTTP token [""]'
}
const { validateHeaderName } = require('node:http');

try {
  validateHeaderName('');
} catch (err) {
  console.error(err instanceof TypeError); // --> true
  console.error(err.code); // --> 'ERR_INVALID_HTTP_TOKEN'
  console.error(err.message); // --> 'Header name must be a valid HTTP token [""]'
}
copy
```

###  `http.validateHeaderValue(name, value)`[#](https://nodejs.org/docs/latest/api/http.html#httpvalidateheadervaluename-value)
Added in: v14.3.0
  * `name`
  * `value`


Performs the low-level validations on the provided `value` that are done when `res.setHeader(name, value)` is called.
Passing illegal value as `value` will result in a [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) being thrown.
  * Undefined value error is identified by `code: 'ERR_HTTP_INVALID_HEADER_VALUE'`.
  * Invalid value character error is identified by `code: 'ERR_INVALID_CHAR'`.


It is not necessary to use this method before passing headers to an HTTP request or response. The HTTP module will automatically validate such headers.
Examples:
```
import { validateHeaderValue } from 'node:http';

try {
  validateHeaderValue('x-my-header', undefined);
} catch (err) {
  console.error(err instanceof TypeError); // --> true
  console.error(err.code === 'ERR_HTTP_INVALID_HEADER_VALUE'); // --> true
  console.error(err.message); // --> 'Invalid value "undefined" for header "x-my-header"'
}

try {
  validateHeaderValue('x-my-header', 'oʊmɪɡə');
} catch (err) {
  console.error(err instanceof TypeError); // --> true
  console.error(err.code === 'ERR_INVALID_CHAR'); // --> true
  console.error(err.message); // --> 'Invalid character in header content ["x-my-header"]'
}
const { validateHeaderValue } = require('node:http');

try {
  validateHeaderValue('x-my-header', undefined);
} catch (err) {
  console.error(err instanceof TypeError); // --> true
  console.error(err.code === 'ERR_HTTP_INVALID_HEADER_VALUE'); // --> true
  console.error(err.message); // --> 'Invalid value "undefined" for header "x-my-header"'
}

try {
  validateHeaderValue('x-my-header', 'oʊmɪɡə');
} catch (err) {
  console.error(err instanceof TypeError); // --> true
  console.error(err.code === 'ERR_INVALID_CHAR'); // --> true
  console.error(err.message); // --> 'Invalid character in header content ["x-my-header"]'
}
copy
```

###  `http.setMaxIdleHTTPParsers(max)`[#](https://nodejs.org/docs/latest/api/http.html#httpsetmaxidlehttpparsersmax)
Added in: v18.8.0, v16.18.0
  * `max` **Default:** `1000`.


Set the maximum number of idle HTTP parsers.
###  `http.setGlobalProxyFromEnv([proxyEnv])`[#](https://nodejs.org/docs/latest/api/http.html#httpsetglobalproxyfromenvproxyenv)
Added in: v25.4.0
  * `proxyEnv` `proxyEnv` option accepted by [`Agent`](https://nodejs.org/docs/latest/api/http.html#class-httpagent). **Default:** `process.env`.
  * Returns: `http.setGlobalProxyFromEnv()` is invoked.


Dynamically resets the global configurations to enable built-in proxy support for `fetch()` and `http.request()`/`https.request()` at runtime, as an alternative to using the `--use-env-proxy` flag or `NODE_USE_ENV_PROXY` environment variable. It can also be used to override settings configured from the environment variables.
As this function resets the global configurations, any previously configured `http.globalAgent`, `https.globalAgent` or undici global dispatcher would be overridden after this function is invoked. It's recommended to invoke it before any requests are made and avoid invoking it in the middle of any requests.
See [Built-in Proxy Support](https://nodejs.org/docs/latest/api/http.html#built-in-proxy-support) for details on proxy URL formats and `NO_PROXY` syntax.
### Class: `WebSocket`[#](https://nodejs.org/docs/latest/api/http.html#class-websocket)
Added in: v22.5.0
A browser-compatible implementation of
### Built-in Proxy Support[#](https://nodejs.org/docs/latest/api/http.html#built-in-proxy-support)
Added in: v24.5.0
Stability: 1.1 - Active development
When Node.js creates the global agent, if the `NODE_USE_ENV_PROXY` environment variable is set to `1` or `--use-env-proxy` is enabled, the global agent will be constructed with `proxyEnv: process.env`, enabling proxy support based on the environment variables.
To enable proxy support dynamically and globally, use [`http.setGlobalProxyFromEnv()`](https://nodejs.org/docs/latest/api/http.html#httpsetglobalproxyfromenvproxyenv).
Custom agents can also be created with proxy support by passing a `proxyEnv` option when constructing the agent. The value can be `process.env` if they just want to inherit the configuration from the environment variables, or an object with specific setting overriding the environment.
The following properties of the `proxyEnv` are checked to configure proxy support.
  * `HTTP_PROXY` or `http_proxy`: Proxy server URL for HTTP requests. If both are set, `http_proxy` takes precedence.
  * `HTTPS_PROXY` or `https_proxy`: Proxy server URL for HTTPS requests. If both are set, `https_proxy` takes precedence.
  * `NO_PROXY` or `no_proxy`: Comma-separated list of hosts to bypass the proxy. If both are set, `no_proxy` takes precedence.


If the request is made to a Unix domain socket, the proxy settings will be ignored.
#### Proxy URL Format[#](https://nodejs.org/docs/latest/api/http.html#proxy-url-format)
Proxy URLs can use either HTTP or HTTPS protocols:
  * HTTP proxy: `http://proxy.example.com:8080`
  * HTTPS proxy: `https://proxy.example.com:8080`
  * Proxy with authentication: `http://username:password@proxy.example.com:8080`


####  `NO_PROXY` Format[#](https://nodejs.org/docs/latest/api/http.html#no-proxy-format)
The `NO_PROXY` environment variable supports several formats:
  * `*` - Bypass proxy for all hosts
  * `example.com` - Exact host name match
  * `.example.com` - Domain suffix match (matches `sub.example.com`)
  * `*.example.com` - Wildcard domain match
  * `192.168.1.100` - Exact IP address match
  * `192.168.1.1-192.168.1.100` - IP address range
  * `example.com:8080` - Hostname with specific port


Multiple entries should be separated by commas.
#### Example[#](https://nodejs.org/docs/latest/api/http.html#example)
To start a Node.js process with proxy support enabled for all requests sent through the default global agent, either use the `NODE_USE_ENV_PROXY` environment variable:
```
NODE_USE_ENV_PROXY=1 HTTP_PROXY=http://proxy.example.com:8080 NO_PROXY=localhost,127.0.0.1 node client.js
copy
```

Or the `--use-env-proxy` flag.
```
HTTP_PROXY=http://proxy.example.com:8080 NO_PROXY=localhost,127.0.0.1 node --use-env-proxy client.js
copy
```

To enable proxy support dynamically and globally with `process.env` (the default option of `http.setGlobalProxyFromEnv()`):
```
const http = require('node:http');

// Reads proxy-related environment variables from process.env
const restore = http.setGlobalProxyFromEnv();

// Subsequent requests will use the configured proxies from environment variables
http.get('http://www.example.com', (res) => {
  // This request will be proxied if HTTP_PROXY or http_proxy is set
});

fetch('https://www.example.com', (res) => {
  // This request will be proxied if HTTPS_PROXY or https_proxy is set
});

// To restore the original global agent and dispatcher settings, call the returned function.
// restore();
import http from 'node:http';

// Reads proxy-related environment variables from process.env
http.setGlobalProxyFromEnv();

// Subsequent requests will use the configured proxies from environment variables
http.get('http://www.example.com', (res) => {
  // This request will be proxied if HTTP_PROXY or http_proxy is set
});

fetch('https://www.example.com', (res) => {
  // This request will be proxied if HTTPS_PROXY or https_proxy is set
});

// To restore the original global agent and dispatcher settings, call the returned function.
// restore();
copy
```

To enable proxy support dynamically and globally with custom settings:
```
const http = require('node:http');

const restore = http.setGlobalProxyFromEnv({
  http_proxy: 'http://proxy.example.com:8080',
  https_proxy: 'https://proxy.example.com:8443',
  no_proxy: 'localhost,127.0.0.1,.internal.example.com',
});

// Subsequent requests will use the configured proxies
http.get('http://www.example.com', (res) => {
  // This request will be proxied through proxy.example.com:8080
});

fetch('https://www.example.com', (res) => {
  // This request will be proxied through proxy.example.com:8443
});
import http from 'node:http';

http.setGlobalProxyFromEnv({
  http_proxy: 'http://proxy.example.com:8080',
  https_proxy: 'https://proxy.example.com:8443',
  no_proxy: 'localhost,127.0.0.1,.internal.example.com',
});

// Subsequent requests will use the configured proxies
http.get('http://www.example.com', (res) => {
  // This request will be proxied through proxy.example.com:8080
});

fetch('https://www.example.com', (res) => {
  // This request will be proxied through proxy.example.com:8443
});
copy
```

To create a custom agent with built-in proxy support:
```
const http = require('node:http');

// Creating a custom agent with custom proxy support.
const agent = new http.Agent({ proxyEnv: { HTTP_PROXY: 'http://proxy.example.com:8080' } });

http.request({
  hostname: 'www.example.com',
  port: 80,
  path: '/',
  agent,
}, (res) => {
  // This request will be proxied through proxy.example.com:8080 using the HTTP protocol.
  console.log(`STATUS: ${res.statusCode}`);
});
copy
```

Alternatively, the following also works:
```
const http = require('node:http');
// Use lower-cased option name.
const agent1 = new http.Agent({ proxyEnv: { http_proxy: 'http://proxy.example.com:8080' } });
// Use values inherited from the environment variables, if the process is started with
// HTTP_PROXY=http://proxy.example.com:8080 this will use the proxy server specified
// in process.env.HTTP_PROXY.
const agent2 = new http.Agent({ proxyEnv: process.env });
copy
```
