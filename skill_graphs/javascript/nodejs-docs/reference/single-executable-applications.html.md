[Skip to content](https://nodejs.org/docs/latest/api/punycode.html#apicontent)
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
  * [](https://nodejs.org/docs/latest/api/punycode.html#toc-picker)
    * [Punycode](https://nodejs.org/docs/latest/api/punycode.html#punycode)
      * [`punycode.decode(string)`](https://nodejs.org/docs/latest/api/punycode.html#punycodedecodestring)
      * [`punycode.encode(string)`](https://nodejs.org/docs/latest/api/punycode.html#punycodeencodestring)
      * [`punycode.toASCII(domain)`](https://nodejs.org/docs/latest/api/punycode.html#punycodetoasciidomain)
      * [`punycode.toUnicode(domain)`](https://nodejs.org/docs/latest/api/punycode.html#punycodetounicodedomain)
      * [`punycode.ucs2`](https://nodejs.org/docs/latest/api/punycode.html#punycodeucs2)
        * [`punycode.ucs2.decode(string)`](https://nodejs.org/docs/latest/api/punycode.html#punycodeucs2decodestring)
        * [`punycode.ucs2.encode(codePoints)`](https://nodejs.org/docs/latest/api/punycode.html#punycodeucs2encodecodepoints)
      * [`punycode.version`](https://nodejs.org/docs/latest/api/punycode.html#punycodeversion)
  * [](https://nodejs.org/docs/latest/api/punycode.html#gtoc-picker)
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
  * [](https://nodejs.org/docs/latest/api/punycode.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/punycode.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/punycode.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/punycode.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/punycode.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/punycode.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/punycode.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/punycode.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/punycode.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/punycode.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/punycode.html)
    11. [15.x ](https://nodejs.org/docs/latest-v15.x/api/punycode.html)
    12. [14.x ](https://nodejs.org/docs/latest-v14.x/api/punycode.html)
    13. [13.x ](https://nodejs.org/docs/latest-v13.x/api/punycode.html)
    14. [12.x ](https://nodejs.org/docs/latest-v12.x/api/punycode.html)
    15. [11.x ](https://nodejs.org/docs/latest-v11.x/api/punycode.html)
    16. [10.x ](https://nodejs.org/docs/latest-v10.x/api/punycode.html)
    17. [9.x ](https://nodejs.org/docs/latest-v9.x/api/punycode.html)
    18. [8.x ](https://nodejs.org/docs/latest-v8.x/api/punycode.html)
    19. [7.x ](https://nodejs.org/docs/latest-v7.x/api/punycode.html)
    20. [6.x ](https://nodejs.org/docs/latest-v6.x/api/punycode.html)
    21. [5.x ](https://nodejs.org/docs/latest-v5.x/api/punycode.html)
    22. [4.x ](https://nodejs.org/docs/latest-v4.x/api/punycode.html)
    23. [0.12.x ](https://nodejs.org/docs/latest-v0.12.x/api/punycode.html)
    24. [0.10.x ](https://nodejs.org/docs/latest-v0.10.x/api/punycode.html)
  * [ ](https://nodejs.org/docs/latest/api/punycode.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/punycode.json)


* * *
Table of contents
  * [Punycode](https://nodejs.org/docs/latest/api/punycode.html#punycode)
    * [`punycode.decode(string)`](https://nodejs.org/docs/latest/api/punycode.html#punycodedecodestring)
    * [`punycode.encode(string)`](https://nodejs.org/docs/latest/api/punycode.html#punycodeencodestring)
    * [`punycode.toASCII(domain)`](https://nodejs.org/docs/latest/api/punycode.html#punycodetoasciidomain)
    * [`punycode.toUnicode(domain)`](https://nodejs.org/docs/latest/api/punycode.html#punycodetounicodedomain)
    * [`punycode.ucs2`](https://nodejs.org/docs/latest/api/punycode.html#punycodeucs2)
      * [`punycode.ucs2.decode(string)`](https://nodejs.org/docs/latest/api/punycode.html#punycodeucs2decodestring)
      * [`punycode.ucs2.encode(codePoints)`](https://nodejs.org/docs/latest/api/punycode.html#punycodeucs2encodecodepoints)
    * [`punycode.version`](https://nodejs.org/docs/latest/api/punycode.html#punycodeversion)


## Punycode[#](https://nodejs.org/docs/latest/api/punycode.html#punycode)
**Source Code:** Deprecated in: v7.0.0
[Stability: 0](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Deprecated
**The version of the punycode module bundled in Node.js is being deprecated.** In a future major version of Node.js this module will be removed. Users currently depending on the `punycode` module should switch to using the userland-provided [`url.domainToASCII`](https://nodejs.org/docs/latest/api/url.html#urldomaintoasciidomain) or, more generally, the [WHATWG URL API](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api).
The `punycode` module is a bundled version of the
```
const punycode = require('node:punycode');
copy
```

`'example'` is `'例'`. The Internationalized Domain Name, `'例.com'` (equivalent to `'example.com'`) is represented by Punycode as the ASCII string `'xn--fsq.com'`.
The `punycode` module provides a simple implementation of the Punycode standard.
The `punycode` module is a third-party dependency used by Node.js and made available to developers as a convenience. Fixes or other modifications to the module must be directed to the
###  `punycode.decode(string)`[#](https://nodejs.org/docs/latest/api/punycode.html#punycodedecodestring)
Added in: v0.5.1
  * `string`


The `punycode.decode()` method converts a
```
punycode.decode('maana-pta'); // 'mañana'
punycode.decode('--dqo34k'); // '☃-⌘'
copy
```

###  `punycode.encode(string)`[#](https://nodejs.org/docs/latest/api/punycode.html#punycodeencodestring)
Added in: v0.5.1
  * `string`


The `punycode.encode()` method converts a string of Unicode codepoints to a
```
punycode.encode('mañana'); // 'maana-pta'
punycode.encode('☃-⌘'); // '--dqo34k'
copy
```

###  `punycode.toASCII(domain)`[#](https://nodejs.org/docs/latest/api/punycode.html#punycodetoasciidomain)
Added in: v0.6.1
  * `domain`


The `punycode.toASCII()` method converts a Unicode string representing an Internationalized Domain Name to `punycode.toASCII()` on a string that already only contains ASCII characters will have no effect.
```
// encode domain names
punycode.toASCII('mañana.com');  // 'xn--maana-pta.com'
punycode.toASCII('☃-⌘.com');   // 'xn----dqo34k.com'
punycode.toASCII('example.com'); // 'example.com'
copy
```

###  `punycode.toUnicode(domain)`[#](https://nodejs.org/docs/latest/api/punycode.html#punycodetounicodedomain)
Added in: v0.6.1
  * `domain`


The `punycode.toUnicode()` method converts a string representing a domain name containing
```
// decode domain names
punycode.toUnicode('xn--maana-pta.com'); // 'mañana.com'
punycode.toUnicode('xn----dqo34k.com');  // '☃-⌘.com'
punycode.toUnicode('example.com');       // 'example.com'
copy
```

###  `punycode.ucs2`[#](https://nodejs.org/docs/latest/api/punycode.html#punycodeucs2)
Added in: v0.7.0
####  `punycode.ucs2.decode(string)`[#](https://nodejs.org/docs/latest/api/punycode.html#punycodeucs2decodestring)
Added in: v0.7.0
  * `string`


The `punycode.ucs2.decode()` method returns an array containing the numeric codepoint values of each Unicode symbol in the string.
```
punycode.ucs2.decode('abc'); // [0x61, 0x62, 0x63]
// surrogate pair for U+1D306 tetragram for centre:
punycode.ucs2.decode('\uD834\uDF06'); // [0x1D306]
copy
```

####  `punycode.ucs2.encode(codePoints)`[#](https://nodejs.org/docs/latest/api/punycode.html#punycodeucs2encodecodepoints)
Added in: v0.7.0
  * `codePoints`


The `punycode.ucs2.encode()` method returns a string based on an array of numeric code point values.
```
punycode.ucs2.encode([0x61, 0x62, 0x63]); // 'abc'
punycode.ucs2.encode([0x1D306]); // '\uD834\uDF06'
copy
```

###  `punycode.version`[#](https://nodejs.org/docs/latest/api/punycode.html#punycodeversion)
Added in: v0.6.1
  * Type:


Returns a string identifying the current
