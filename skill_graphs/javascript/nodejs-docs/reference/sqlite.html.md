[Skip to content](https://nodejs.org/docs/latest/api/querystring.html#apicontent)
[ Node.js ](https://nodejs.org/ "Go back to the home page")
* * *
  * [About this documentation](https://nodejs.org/docs/latest/api/documentation.html)
  * [Usage and example](https://nodejs.org/docs/latest/api/synopsis.html)
  * [Assertion testing](https://nodejs.org/docs/latest/api/assert.html)
  * [Asynchronous context tracking](https://nodejs.org/docs/latest/api/async_context.html)
  * [Async hooks](https://nodejs.org/docs/latest/api/async_hooks.html)
  * [Buffer](https://nodejs.org/docs/latest/api/buffer.html)
  * [C++ addons](https://nodejs.org/docs/latest/api/addons.html)
  * [C/C++ addons with Node-API](https://nodejs.org/docs/latest/api/n-api.html)
  * [C++ embedder API](https://nodejs.org/docs/latest/api/embedding.html)
  * [Child processes](https://nodejs.org/docs/latest/api/child_process.html)
  * [Cluster](https://nodejs.org/docs/latest/api/cluster.html)
  * [Command-line options](https://nodejs.org/docs/latest/api/cli.html)
  * [Console](https://nodejs.org/docs/latest/api/console.html)
  * [Crypto](https://nodejs.org/docs/latest/api/crypto.html)
  * [Debugger](https://nodejs.org/docs/latest/api/debugger.html)
  * [Deprecated APIs](https://nodejs.org/docs/latest/api/deprecations.html)
  * [Diagnostics Channel](https://nodejs.org/docs/latest/api/diagnostics_channel.html)
  * [DNS](https://nodejs.org/docs/latest/api/dns.html)
  * [Domain](https://nodejs.org/docs/latest/api/domain.html)
  * [Environment Variables](https://nodejs.org/docs/latest/api/environment_variables.html)
  * [Errors](https://nodejs.org/docs/latest/api/errors.html)
  * [Events](https://nodejs.org/docs/latest/api/events.html)
  * [File system](https://nodejs.org/docs/latest/api/fs.html)
  * [Globals](https://nodejs.org/docs/latest/api/globals.html)
  * [HTTP](https://nodejs.org/docs/latest/api/http.html)
  * [HTTP/2](https://nodejs.org/docs/latest/api/http2.html)
  * [HTTPS](https://nodejs.org/docs/latest/api/https.html)
  * [Inspector](https://nodejs.org/docs/latest/api/inspector.html)
  * [Internationalization](https://nodejs.org/docs/latest/api/intl.html)
  * [Modules: CommonJS modules](https://nodejs.org/docs/latest/api/modules.html)
  * [Modules: ECMAScript modules](https://nodejs.org/docs/latest/api/esm.html)
  * [Modules: `node:module` API](https://nodejs.org/docs/latest/api/module.html)
  * [Modules: Packages](https://nodejs.org/docs/latest/api/packages.html)
  * [Modules: TypeScript](https://nodejs.org/docs/latest/api/typescript.html)
  * [Net](https://nodejs.org/docs/latest/api/net.html)
  * [OS](https://nodejs.org/docs/latest/api/os.html)
  * [Path](https://nodejs.org/docs/latest/api/path.html)
  * [Performance hooks](https://nodejs.org/docs/latest/api/perf_hooks.html)
  * [Permissions](https://nodejs.org/docs/latest/api/permissions.html)
  * [Process](https://nodejs.org/docs/latest/api/process.html)
  * [Punycode](https://nodejs.org/docs/latest/api/punycode.html)
  * [Query strings](https://nodejs.org/docs/latest/api/querystring.html)
  * [Readline](https://nodejs.org/docs/latest/api/readline.html)
  * [REPL](https://nodejs.org/docs/latest/api/repl.html)
  * [Report](https://nodejs.org/docs/latest/api/report.html)
  * [Single executable applications](https://nodejs.org/docs/latest/api/single-executable-applications.html)
  * [SQLite](https://nodejs.org/docs/latest/api/sqlite.html)
  * [Stream](https://nodejs.org/docs/latest/api/stream.html)
  * [String decoder](https://nodejs.org/docs/latest/api/string_decoder.html)
  * [Test runner](https://nodejs.org/docs/latest/api/test.html)
  * [Timers](https://nodejs.org/docs/latest/api/timers.html)
  * [TLS/SSL](https://nodejs.org/docs/latest/api/tls.html)
  * [Trace events](https://nodejs.org/docs/latest/api/tracing.html)
  * [TTY](https://nodejs.org/docs/latest/api/tty.html)
  * [UDP/datagram](https://nodejs.org/docs/latest/api/dgram.html)
  * [URL](https://nodejs.org/docs/latest/api/url.html)
  * [Utilities](https://nodejs.org/docs/latest/api/util.html)
  * [V8](https://nodejs.org/docs/latest/api/v8.html)
  * [VM](https://nodejs.org/docs/latest/api/vm.html)
  * [WASI](https://nodejs.org/docs/latest/api/wasi.html)
  * [Web Crypto API](https://nodejs.org/docs/latest/api/webcrypto.html)
  * [Web Streams API](https://nodejs.org/docs/latest/api/webstreams.html)
  * [Worker threads](https://nodejs.org/docs/latest/api/worker_threads.html)
  * [Zlib](https://nodejs.org/docs/latest/api/zlib.html)


* * *
# Node.js v25.8.0 documentation
  * Node.js v25.8.0
  * [](https://nodejs.org/docs/latest/api/querystring.html#toc-picker)
    * [Query string](https://nodejs.org/docs/latest/api/querystring.html#query-string)
      * [`querystring.decode()`](https://nodejs.org/docs/latest/api/querystring.html#querystringdecode)
      * [`querystring.encode()`](https://nodejs.org/docs/latest/api/querystring.html#querystringencode)
      * [`querystring.escape(str)`](https://nodejs.org/docs/latest/api/querystring.html#querystringescapestr)
      * [`querystring.parse(str[, sep[, eq[, options]]])`](https://nodejs.org/docs/latest/api/querystring.html#querystringparsestr-sep-eq-options)
      * [`querystring.stringify(obj[, sep[, eq[, options]]])`](https://nodejs.org/docs/latest/api/querystring.html#querystringstringifyobj-sep-eq-options)
      * [`querystring.unescape(str)`](https://nodejs.org/docs/latest/api/querystring.html#querystringunescapestr)
  * [](https://nodejs.org/docs/latest/api/querystring.html#gtoc-picker)
    * [Index](https://nodejs.org/docs/latest/api/index.html)
* * *
    * [About this documentation](https://nodejs.org/docs/latest/api/documentation.html)
    * [Usage and example](https://nodejs.org/docs/latest/api/synopsis.html)
    * [Assertion testing](https://nodejs.org/docs/latest/api/assert.html)
    * [Asynchronous context tracking](https://nodejs.org/docs/latest/api/async_context.html)
    * [Async hooks](https://nodejs.org/docs/latest/api/async_hooks.html)
    * [Buffer](https://nodejs.org/docs/latest/api/buffer.html)
    * [C++ addons](https://nodejs.org/docs/latest/api/addons.html)
    * [C/C++ addons with Node-API](https://nodejs.org/docs/latest/api/n-api.html)
    * [C++ embedder API](https://nodejs.org/docs/latest/api/embedding.html)
    * [Child processes](https://nodejs.org/docs/latest/api/child_process.html)
    * [Cluster](https://nodejs.org/docs/latest/api/cluster.html)
    * [Command-line options](https://nodejs.org/docs/latest/api/cli.html)
    * [Console](https://nodejs.org/docs/latest/api/console.html)
    * [Crypto](https://nodejs.org/docs/latest/api/crypto.html)
    * [Debugger](https://nodejs.org/docs/latest/api/debugger.html)
    * [Deprecated APIs](https://nodejs.org/docs/latest/api/deprecations.html)
    * [Diagnostics Channel](https://nodejs.org/docs/latest/api/diagnostics_channel.html)
    * [DNS](https://nodejs.org/docs/latest/api/dns.html)
    * [Domain](https://nodejs.org/docs/latest/api/domain.html)
    * [Environment Variables](https://nodejs.org/docs/latest/api/environment_variables.html)
    * [Errors](https://nodejs.org/docs/latest/api/errors.html)
    * [Events](https://nodejs.org/docs/latest/api/events.html)
    * [File system](https://nodejs.org/docs/latest/api/fs.html)
    * [Globals](https://nodejs.org/docs/latest/api/globals.html)
    * [HTTP](https://nodejs.org/docs/latest/api/http.html)
    * [HTTP/2](https://nodejs.org/docs/latest/api/http2.html)
    * [HTTPS](https://nodejs.org/docs/latest/api/https.html)
    * [Inspector](https://nodejs.org/docs/latest/api/inspector.html)
    * [Internationalization](https://nodejs.org/docs/latest/api/intl.html)
    * [Modules: CommonJS modules](https://nodejs.org/docs/latest/api/modules.html)
    * [Modules: ECMAScript modules](https://nodejs.org/docs/latest/api/esm.html)
    * [Modules: `node:module` API](https://nodejs.org/docs/latest/api/module.html)
    * [Modules: Packages](https://nodejs.org/docs/latest/api/packages.html)
    * [Modules: TypeScript](https://nodejs.org/docs/latest/api/typescript.html)
    * [Net](https://nodejs.org/docs/latest/api/net.html)
    * [OS](https://nodejs.org/docs/latest/api/os.html)
    * [Path](https://nodejs.org/docs/latest/api/path.html)
    * [Performance hooks](https://nodejs.org/docs/latest/api/perf_hooks.html)
    * [Permissions](https://nodejs.org/docs/latest/api/permissions.html)
    * [Process](https://nodejs.org/docs/latest/api/process.html)
    * [Punycode](https://nodejs.org/docs/latest/api/punycode.html)
    * [Query strings](https://nodejs.org/docs/latest/api/querystring.html)
    * [Readline](https://nodejs.org/docs/latest/api/readline.html)
    * [REPL](https://nodejs.org/docs/latest/api/repl.html)
    * [Report](https://nodejs.org/docs/latest/api/report.html)
    * [Single executable applications](https://nodejs.org/docs/latest/api/single-executable-applications.html)
    * [SQLite](https://nodejs.org/docs/latest/api/sqlite.html)
    * [Stream](https://nodejs.org/docs/latest/api/stream.html)
    * [String decoder](https://nodejs.org/docs/latest/api/string_decoder.html)
    * [Test runner](https://nodejs.org/docs/latest/api/test.html)
    * [Timers](https://nodejs.org/docs/latest/api/timers.html)
    * [TLS/SSL](https://nodejs.org/docs/latest/api/tls.html)
    * [Trace events](https://nodejs.org/docs/latest/api/tracing.html)
    * [TTY](https://nodejs.org/docs/latest/api/tty.html)
    * [UDP/datagram](https://nodejs.org/docs/latest/api/dgram.html)
    * [URL](https://nodejs.org/docs/latest/api/url.html)
    * [Utilities](https://nodejs.org/docs/latest/api/util.html)
    * [V8](https://nodejs.org/docs/latest/api/v8.html)
    * [VM](https://nodejs.org/docs/latest/api/vm.html)
    * [WASI](https://nodejs.org/docs/latest/api/wasi.html)
    * [Web Crypto API](https://nodejs.org/docs/latest/api/webcrypto.html)
    * [Web Streams API](https://nodejs.org/docs/latest/api/webstreams.html)
    * [Worker threads](https://nodejs.org/docs/latest/api/worker_threads.html)
    * [Zlib](https://nodejs.org/docs/latest/api/zlib.html)
  * [](https://nodejs.org/docs/latest/api/querystring.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/querystring.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/querystring.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/querystring.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/querystring.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/querystring.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/querystring.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/querystring.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/querystring.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/querystring.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/querystring.html)
    11. [15.x ](https://nodejs.org/docs/latest-v15.x/api/querystring.html)
    12. [14.x ](https://nodejs.org/docs/latest-v14.x/api/querystring.html)
    13. [13.x ](https://nodejs.org/docs/latest-v13.x/api/querystring.html)
    14. [12.x ](https://nodejs.org/docs/latest-v12.x/api/querystring.html)
    15. [11.x ](https://nodejs.org/docs/latest-v11.x/api/querystring.html)
    16. [10.x ](https://nodejs.org/docs/latest-v10.x/api/querystring.html)
    17. [9.x ](https://nodejs.org/docs/latest-v9.x/api/querystring.html)
    18. [8.x ](https://nodejs.org/docs/latest-v8.x/api/querystring.html)
    19. [7.x ](https://nodejs.org/docs/latest-v7.x/api/querystring.html)
    20. [6.x ](https://nodejs.org/docs/latest-v6.x/api/querystring.html)
    21. [5.x ](https://nodejs.org/docs/latest-v5.x/api/querystring.html)
    22. [4.x ](https://nodejs.org/docs/latest-v4.x/api/querystring.html)
    23. [0.12.x ](https://nodejs.org/docs/latest-v0.12.x/api/querystring.html)
    24. [0.10.x ](https://nodejs.org/docs/latest-v0.10.x/api/querystring.html)
  * [ ](https://nodejs.org/docs/latest/api/querystring.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/querystring.json)


* * *
Table of contents
  * [Query string](https://nodejs.org/docs/latest/api/querystring.html#query-string)
    * [`querystring.decode()`](https://nodejs.org/docs/latest/api/querystring.html#querystringdecode)
    * [`querystring.encode()`](https://nodejs.org/docs/latest/api/querystring.html#querystringencode)
    * [`querystring.escape(str)`](https://nodejs.org/docs/latest/api/querystring.html#querystringescapestr)
    * [`querystring.parse(str[, sep[, eq[, options]]])`](https://nodejs.org/docs/latest/api/querystring.html#querystringparsestr-sep-eq-options)
    * [`querystring.stringify(obj[, sep[, eq[, options]]])`](https://nodejs.org/docs/latest/api/querystring.html#querystringstringifyobj-sep-eq-options)
    * [`querystring.unescape(str)`](https://nodejs.org/docs/latest/api/querystring.html#querystringunescapestr)


## Query string[#](https://nodejs.org/docs/latest/api/querystring.html#query-string)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:querystring` module provides utilities for parsing and formatting URL query strings. It can be accessed using:
```
const querystring = require('node:querystring');
copy
```

`querystring` is more performant than [`<URLSearchParams>`](https://nodejs.org/docs/latest/api/url.html#class-urlsearchparams) but is not a standardized API. Use [`<URLSearchParams>`](https://nodejs.org/docs/latest/api/url.html#class-urlsearchparams) when performance is not critical or when compatibility with browser code is desirable.
###  `querystring.decode()`[#](https://nodejs.org/docs/latest/api/querystring.html#querystringdecode)
Added in: v0.1.99
The `querystring.decode()` function is an alias for `querystring.parse()`.
###  `querystring.encode()`[#](https://nodejs.org/docs/latest/api/querystring.html#querystringencode)
Added in: v0.1.99
The `querystring.encode()` function is an alias for `querystring.stringify()`.
###  `querystring.escape(str)`[#](https://nodejs.org/docs/latest/api/querystring.html#querystringescapestr)
Added in: v0.1.25
  * `str`


The `querystring.escape()` method performs URL percent-encoding on the given `str` in a manner that is optimized for the specific requirements of URL query strings.
The `querystring.escape()` method is used by `querystring.stringify()` and is generally not expected to be used directly. It is exported primarily to allow application code to provide a replacement percent-encoding implementation if necessary by assigning `querystring.escape` to an alternative function.
###  `querystring.parse(str[, sep[, eq[, options]]])`[#](https://nodejs.org/docs/latest/api/querystring.html#querystringparsestr-sep-eq-options)
Added in: v0.1.25History Version | Changes
---|---
v8.0.0 | Multiple empty entries are now parsed correctly (e.g. `&=&=`).
v6.0.0 | The returned object no longer inherits from `Object.prototype`.
v6.0.0, v4.2.4 | The `eq` parameter may now have a length of more than `1`.
  * `str`
  * `sep` **Default:** `'&'`.
  * `eq` **Default:** `'='`.
  * `options`
    * `decodeURIComponent` **Default:** `querystring.unescape()`.
    * `maxKeys` `0` to remove key counting limitations. **Default:** `1000`.


The `querystring.parse()` method parses a URL query string (`str`) into a collection of key and value pairs.
For example, the query string `'foo=bar&abc=xyz&abc=123'` is parsed into:
```
{
  "foo": "bar",
  "abc": ["xyz", "123"]
}
copy
```

The object returned by the `querystring.parse()` method _does not_ prototypically inherit from the JavaScript `Object`. This means that typical `Object` methods such as `obj.toString()`, `obj.hasOwnProperty()`, and others are not defined and _will not work_.
By default, percent-encoded characters within the query string will be assumed to use UTF-8 encoding. If an alternative character encoding is used, then an alternative `decodeURIComponent` option will need to be specified:
```
// Assuming gbkDecodeURIComponent function already exists...

querystring.parse('w=%D6%D0%CE%C4&foo=bar', null, null,
                  { decodeURIComponent: gbkDecodeURIComponent });
copy
```

###  `querystring.stringify(obj[, sep[, eq[, options]]])`[#](https://nodejs.org/docs/latest/api/querystring.html#querystringstringifyobj-sep-eq-options)
Added in: v0.1.25
  * `obj`
  * `sep` **Default:** `'&'`.
  * `eq` **Default:** `'='`.
  * `options`
    * `encodeURIComponent` **Default:** `querystring.escape()`.


The `querystring.stringify()` method produces a URL query string from a given `obj` by iterating through the object's "own properties".
It serializes the following types of values passed in `obj`:
```
querystring.stringify({ foo: 'bar', baz: ['qux', 'quux'], corge: '' });
// Returns 'foo=bar&baz=qux&baz=quux&corge='

querystring.stringify({ foo: 'bar', baz: 'qux' }, ';', ':');
// Returns 'foo:bar;baz:qux'
copy
```

By default, characters requiring percent-encoding within the query string will be encoded as UTF-8. If an alternative encoding is required, then an alternative `encodeURIComponent` option will need to be specified:
```
// Assuming gbkEncodeURIComponent function already exists,

querystring.stringify({ w: '中文', foo: 'bar' }, null, null,
                      { encodeURIComponent: gbkEncodeURIComponent });
copy
```

###  `querystring.unescape(str)`[#](https://nodejs.org/docs/latest/api/querystring.html#querystringunescapestr)
Added in: v0.1.25
  * `str`


The `querystring.unescape()` method performs decoding of URL percent-encoded characters on the given `str`.
The `querystring.unescape()` method is used by `querystring.parse()` and is generally not expected to be used directly. It is exported primarily to allow application code to provide a replacement decoding implementation if necessary by assigning `querystring.unescape` to an alternative function.
By default, the `querystring.unescape()` method will attempt to use the JavaScript built-in `decodeURIComponent()` method to decode. If that fails, a safer equivalent that does not throw on malformed URLs will be used.
