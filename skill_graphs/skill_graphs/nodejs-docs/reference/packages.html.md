[Skip to content](https://nodejs.org/docs/latest/api/intl.html#apicontent)
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
  * [](https://nodejs.org/docs/latest/api/intl.html#toc-picker)
    * [Internationalization support](https://nodejs.org/docs/latest/api/intl.html#internationalization-support)
      * [Options for building Node.js](https://nodejs.org/docs/latest/api/intl.html#options-for-building-nodejs)
        * [Disable all internationalization features (`none`)](https://nodejs.org/docs/latest/api/intl.html#disable-all-internationalization-features-none)
        * [Build with a pre-installed ICU (`system-icu`)](https://nodejs.org/docs/latest/api/intl.html#build-with-a-pre-installed-icu-system-icu)
        * [Embed a limited set of ICU data (`small-icu`)](https://nodejs.org/docs/latest/api/intl.html#embed-a-limited-set-of-icu-data-small-icu)
          * [Providing ICU data at runtime](https://nodejs.org/docs/latest/api/intl.html#providing-icu-data-at-runtime)
        * [Embed the entire ICU (`full-icu`)](https://nodejs.org/docs/latest/api/intl.html#embed-the-entire-icu-full-icu)
      * [Detecting internationalization support](https://nodejs.org/docs/latest/api/intl.html#detecting-internationalization-support)
  * [](https://nodejs.org/docs/latest/api/intl.html#gtoc-picker)
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
  * [](https://nodejs.org/docs/latest/api/intl.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/intl.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/intl.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/intl.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/intl.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/intl.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/intl.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/intl.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/intl.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/intl.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/intl.html)
    11. [15.x ](https://nodejs.org/docs/latest-v15.x/api/intl.html)
    12. [14.x ](https://nodejs.org/docs/latest-v14.x/api/intl.html)
    13. [13.x ](https://nodejs.org/docs/latest-v13.x/api/intl.html)
    14. [12.x ](https://nodejs.org/docs/latest-v12.x/api/intl.html)
    15. [11.x ](https://nodejs.org/docs/latest-v11.x/api/intl.html)
    16. [10.x ](https://nodejs.org/docs/latest-v10.x/api/intl.html)
    17. [9.x ](https://nodejs.org/docs/latest-v9.x/api/intl.html)
    18. [8.x ](https://nodejs.org/docs/latest-v8.x/api/intl.html)
  * [ ](https://nodejs.org/docs/latest/api/intl.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/intl.json)


* * *
Table of contents
  * [Internationalization support](https://nodejs.org/docs/latest/api/intl.html#internationalization-support)
    * [Options for building Node.js](https://nodejs.org/docs/latest/api/intl.html#options-for-building-nodejs)
      * [Disable all internationalization features (`none`)](https://nodejs.org/docs/latest/api/intl.html#disable-all-internationalization-features-none)
      * [Build with a pre-installed ICU (`system-icu`)](https://nodejs.org/docs/latest/api/intl.html#build-with-a-pre-installed-icu-system-icu)
      * [Embed a limited set of ICU data (`small-icu`)](https://nodejs.org/docs/latest/api/intl.html#embed-a-limited-set-of-icu-data-small-icu)
        * [Providing ICU data at runtime](https://nodejs.org/docs/latest/api/intl.html#providing-icu-data-at-runtime)
      * [Embed the entire ICU (`full-icu`)](https://nodejs.org/docs/latest/api/intl.html#embed-the-entire-icu-full-icu)
    * [Detecting internationalization support](https://nodejs.org/docs/latest/api/intl.html#detecting-internationalization-support)


## Internationalization support[#](https://nodejs.org/docs/latest/api/intl.html#internationalization-support)
Node.js has many features that make it easier to write internationalized programs. Some of them are:
  * Locale-sensitive or Unicode-aware functions in the
  * All functionality described in the
    * Locale-sensitive methods like
  * The [WHATWG URL parser](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)'s
  * [`require('node:buffer').transcode()`](https://nodejs.org/docs/latest/api/buffer.html#buffertranscodesource-fromenc-toenc)
  * More accurate [REPL](https://nodejs.org/docs/latest/api/repl.html#repl) line editing
  * [`require('node:util').TextDecoder`](https://nodejs.org/docs/latest/api/util.html#class-utiltextdecoder)


Node.js and the underlying V8 engine use
### Options for building Node.js[#](https://nodejs.org/docs/latest/api/intl.html#options-for-building-nodejs)
To control how ICU is used in Node.js, four `configure` options are available during compilation. Additional details on how to compile Node.js are documented in
  * `--with-intl=none`/`--without-intl`
  * `--with-intl=system-icu`
  * `--with-intl=small-icu`
  * `--with-intl=full-icu` (default)


An overview of available Node.js and JavaScript features for each `configure` option:
Feature | `none` | `system-icu` | `small-icu` | `full-icu`
---|---|---|---|---
| none (function is no-op) | full | full | full
`String.prototype.to*Case()` | full | full | full | full
| none (object does not exist) | partial/full (depends on OS) | partial (English-only) | full
| partial (not locale-aware) | full | full | full
`String.prototype.toLocale*Case()` | partial (not locale-aware) | full | full | full
| partial (not locale-aware) | partial/full (depends on OS) | partial (English-only) | full
`Date.prototype.toLocale*String()` | partial (not locale-aware) | partial/full (depends on OS) | partial (English-only) | full
[Legacy URL Parser](https://nodejs.org/docs/latest/api/url.html#legacy-url-api) | partial (no IDN support) | full | full | full
[WHATWG URL Parser](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) | partial (no IDN support) | full | full | full
[`require('node:buffer').transcode()`](https://nodejs.org/docs/latest/api/buffer.html#buffertranscodesource-fromenc-toenc) | none (function does not exist) | full | full | full
[REPL](https://nodejs.org/docs/latest/api/repl.html#repl) | partial (inaccurate line editing) | full | full | full
[`require('node:util').TextDecoder`](https://nodejs.org/docs/latest/api/util.html#class-utiltextdecoder) | partial (basic encodings support) | partial/full (depends on OS) | partial (Unicode-only) | full
| none (invalid `RegExp` error) | full | full | full
The "(not locale-aware)" designation denotes that the function carries out its operation just like the non-`Locale` version of the function, if one exists. For example, under `none` mode, `Date.prototype.toLocaleString()`'s operation is identical to that of `Date.prototype.toString()`.
#### Disable all internationalization features (`none`)[#](https://nodejs.org/docs/latest/api/intl.html#disable-all-internationalization-features-none)
If this option is chosen, ICU is disabled and most internationalization features mentioned above will be **unavailable** in the resulting `node` binary.
#### Build with a pre-installed ICU (`system-icu`)[#](https://nodejs.org/docs/latest/api/intl.html#build-with-a-pre-installed-icu-system-icu)
Node.js can link against an ICU build already installed on the system. In fact, most Linux distributions already come with ICU installed, and this option would make it possible to reuse the same set of data used by other components in the OS.
Functionalities that only require the ICU library itself, such as [WHATWG URL parser](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api), are fully supported under `system-icu`. Features that require ICU locale data in addition, such as _may_ be fully or partially supported, depending on the completeness of the ICU data installed on the system.
#### Embed a limited set of ICU data (`small-icu`)[#](https://nodejs.org/docs/latest/api/intl.html#embed-a-limited-set-of-icu-data-small-icu)
This option makes the resulting binary link against the ICU library statically, and includes a subset of ICU data (typically only the English locale) within the `node` executable.
Functionalities that only require the ICU library itself, such as [WHATWG URL parser](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api), are fully supported under `small-icu`. Features that require ICU locale data in addition, such as
```
const january = new Date(9e8);
const english = new Intl.DateTimeFormat('en', { month: 'long' });
const spanish = new Intl.DateTimeFormat('es', { month: 'long' });

console.log(english.format(january));
// Prints "January"
console.log(spanish.format(january));
// Prints either "M01" or "January" on small-icu, depending on the user’s default locale
// Should print "enero"
copy
```

This mode provides a balance between features and binary size.
##### Providing ICU data at runtime[#](https://nodejs.org/docs/latest/api/intl.html#providing-icu-data-at-runtime)
If the `small-icu` option is used, one can still provide additional locale data at runtime so that the JS methods would work for all ICU locales. Assuming the data file is stored at `/runtime/directory/with/dat/file`, it can be made available to ICU through either:
  * The `--with-icu-default-data-dir` configure option:
```
./configure --with-icu-default-data-dir=/runtime/directory/with/dat/file --with-intl=small-icu
copy
```

This only embeds the default data directory path into the binary. The actual data file is going to be loaded at runtime from this directory path.
  * The [`NODE_ICU_DATA`](https://nodejs.org/docs/latest/api/cli.html#node_icu_datafile) environment variable:
```
env NODE_ICU_DATA=/runtime/directory/with/dat/file node
copy
```

  * The [`--icu-data-dir`](https://nodejs.org/docs/latest/api/cli.html#--icu-data-dirfile) CLI parameter:
```
node --icu-data-dir=/runtime/directory/with/dat/file
copy
```



When more than one of them is specified, the `--icu-data-dir` CLI parameter has the highest precedence, then the `NODE_ICU_DATA` environment variable, then the `--with-icu-default-data-dir` configure option.
ICU is able to automatically find and load a variety of data formats, but the data must be appropriate for the ICU version, and the file correctly named. The most common name for the data file is `icudtX[bl].dat`, where `X` denotes the intended ICU version, and `b` or `l` indicates the system's endianness. Node.js would fail to load if the expected data file cannot be read from the specified directory. The name of the data file corresponding to the current Node.js version can be computed with:
```
`icudt${process.versions.icu.split('.')[0]}${os.endianness()[0].toLowerCase()}.dat`;
copy
```

Check
The `node` executable and downloading the appropriate data file. After installing the module through `npm i full-icu`, the data file will be available at `./node_modules/full-icu`. This path can be then passed either to `NODE_ICU_DATA` or `--icu-data-dir` as shown above to enable full `Intl` support.
#### Embed the entire ICU (`full-icu`)[#](https://nodejs.org/docs/latest/api/intl.html#embed-the-entire-icu-full-icu)
This option makes the resulting binary link against ICU statically and include a full set of ICU data. A binary created this way has no further external dependencies and supports all locales, but might be rather large. This is the default behavior if no `--with-intl` flag is passed. The official binaries are also built in this mode.
### Detecting internationalization support[#](https://nodejs.org/docs/latest/api/intl.html#detecting-internationalization-support)
To verify that ICU is enabled at all (`system-icu`, `small-icu`, or `full-icu`), simply checking the existence of `Intl` should suffice:
```
const hasICU = typeof Intl === 'object';
copy
```

Alternatively, checking for `process.versions.icu`, a property defined only when ICU is enabled, works too:
```
const hasICU = typeof process.versions.icu === 'string';
copy
```

To check for support for a non-English locale (i.e. `full-icu` or `system-icu`),
```
const hasFullICU = (() => {
  try {
    const january = new Date(9e8);
    const spanish = new Intl.DateTimeFormat('es', { month: 'long' });
    return spanish.format(january) === 'enero';
  } catch (err) {
    return false;
  }
})();
copy
```

For more verbose tests for `Intl` support, the following resources may be found to be helpful:
  * `Intl` support is built correctly.
