[Skip to content](https://nodejs.org/docs/latest/api/path.html#apicontent)
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
  * [](https://nodejs.org/docs/latest/api/path.html#toc-picker)
    * [Path](https://nodejs.org/docs/latest/api/path.html#path)
      * [Windows vs. POSIX](https://nodejs.org/docs/latest/api/path.html#windows-vs-posix)
      * [`path.basename(path[, suffix])`](https://nodejs.org/docs/latest/api/path.html#pathbasenamepath-suffix)
      * [`path.delimiter`](https://nodejs.org/docs/latest/api/path.html#pathdelimiter)
      * [`path.dirname(path)`](https://nodejs.org/docs/latest/api/path.html#pathdirnamepath)
      * [`path.extname(path)`](https://nodejs.org/docs/latest/api/path.html#pathextnamepath)
      * [`path.format(pathObject)`](https://nodejs.org/docs/latest/api/path.html#pathformatpathobject)
      * [`path.matchesGlob(path, pattern)`](https://nodejs.org/docs/latest/api/path.html#pathmatchesglobpath-pattern)
      * [`path.isAbsolute(path)`](https://nodejs.org/docs/latest/api/path.html#pathisabsolutepath)
      * [`path.join([...paths])`](https://nodejs.org/docs/latest/api/path.html#pathjoinpaths)
      * [`path.normalize(path)`](https://nodejs.org/docs/latest/api/path.html#pathnormalizepath)
      * [`path.parse(path)`](https://nodejs.org/docs/latest/api/path.html#pathparsepath)
      * [`path.posix`](https://nodejs.org/docs/latest/api/path.html#pathposix)
      * [`path.relative(from, to)`](https://nodejs.org/docs/latest/api/path.html#pathrelativefrom-to)
      * [`path.resolve([...paths])`](https://nodejs.org/docs/latest/api/path.html#pathresolvepaths)
      * [`path.sep`](https://nodejs.org/docs/latest/api/path.html#pathsep)
      * [`path.toNamespacedPath(path)`](https://nodejs.org/docs/latest/api/path.html#pathtonamespacedpathpath)
      * [`path.win32`](https://nodejs.org/docs/latest/api/path.html#pathwin32)
  * [](https://nodejs.org/docs/latest/api/path.html#gtoc-picker)
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
  * [](https://nodejs.org/docs/latest/api/path.html#alt-docs)
    1. [25.x ](https://nodejs.org/docs/latest-v25.x/api/path.html)
    2. [24.x ](https://nodejs.org/docs/latest-v24.x/api/path.html)
    3. [23.x ](https://nodejs.org/docs/latest-v23.x/api/path.html)
    4. [22.x **LTS**](https://nodejs.org/docs/latest-v22.x/api/path.html)
    5. [21.x ](https://nodejs.org/docs/latest-v21.x/api/path.html)
    6. [20.x **LTS**](https://nodejs.org/docs/latest-v20.x/api/path.html)
    7. [19.x ](https://nodejs.org/docs/latest-v19.x/api/path.html)
    8. [18.x ](https://nodejs.org/docs/latest-v18.x/api/path.html)
    9. [17.x ](https://nodejs.org/docs/latest-v17.x/api/path.html)
    10. [16.x ](https://nodejs.org/docs/latest-v16.x/api/path.html)
    11. [15.x ](https://nodejs.org/docs/latest-v15.x/api/path.html)
    12. [14.x ](https://nodejs.org/docs/latest-v14.x/api/path.html)
    13. [13.x ](https://nodejs.org/docs/latest-v13.x/api/path.html)
    14. [12.x ](https://nodejs.org/docs/latest-v12.x/api/path.html)
    15. [11.x ](https://nodejs.org/docs/latest-v11.x/api/path.html)
    16. [10.x ](https://nodejs.org/docs/latest-v10.x/api/path.html)
    17. [9.x ](https://nodejs.org/docs/latest-v9.x/api/path.html)
    18. [8.x ](https://nodejs.org/docs/latest-v8.x/api/path.html)
    19. [7.x ](https://nodejs.org/docs/latest-v7.x/api/path.html)
    20. [6.x ](https://nodejs.org/docs/latest-v6.x/api/path.html)
    21. [5.x ](https://nodejs.org/docs/latest-v5.x/api/path.html)
    22. [4.x ](https://nodejs.org/docs/latest-v4.x/api/path.html)
    23. [0.12.x ](https://nodejs.org/docs/latest-v0.12.x/api/path.html)
    24. [0.10.x ](https://nodejs.org/docs/latest-v0.10.x/api/path.html)
  * [ ](https://nodejs.org/docs/latest/api/path.html#options-picker)
    * [View on single page](https://nodejs.org/docs/latest/api/all.html)
    * [View as JSON](https://nodejs.org/docs/latest/api/path.json)


* * *
Table of contents
  * [Path](https://nodejs.org/docs/latest/api/path.html#path)
    * [Windows vs. POSIX](https://nodejs.org/docs/latest/api/path.html#windows-vs-posix)
    * [`path.basename(path[, suffix])`](https://nodejs.org/docs/latest/api/path.html#pathbasenamepath-suffix)
    * [`path.delimiter`](https://nodejs.org/docs/latest/api/path.html#pathdelimiter)
    * [`path.dirname(path)`](https://nodejs.org/docs/latest/api/path.html#pathdirnamepath)
    * [`path.extname(path)`](https://nodejs.org/docs/latest/api/path.html#pathextnamepath)
    * [`path.format(pathObject)`](https://nodejs.org/docs/latest/api/path.html#pathformatpathobject)
    * [`path.matchesGlob(path, pattern)`](https://nodejs.org/docs/latest/api/path.html#pathmatchesglobpath-pattern)
    * [`path.isAbsolute(path)`](https://nodejs.org/docs/latest/api/path.html#pathisabsolutepath)
    * [`path.join([...paths])`](https://nodejs.org/docs/latest/api/path.html#pathjoinpaths)
    * [`path.normalize(path)`](https://nodejs.org/docs/latest/api/path.html#pathnormalizepath)
    * [`path.parse(path)`](https://nodejs.org/docs/latest/api/path.html#pathparsepath)
    * [`path.posix`](https://nodejs.org/docs/latest/api/path.html#pathposix)
    * [`path.relative(from, to)`](https://nodejs.org/docs/latest/api/path.html#pathrelativefrom-to)
    * [`path.resolve([...paths])`](https://nodejs.org/docs/latest/api/path.html#pathresolvepaths)
    * [`path.sep`](https://nodejs.org/docs/latest/api/path.html#pathsep)
    * [`path.toNamespacedPath(path)`](https://nodejs.org/docs/latest/api/path.html#pathtonamespacedpathpath)
    * [`path.win32`](https://nodejs.org/docs/latest/api/path.html#pathwin32)


## Path[#](https://nodejs.org/docs/latest/api/path.html#path)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:path` module provides utilities for working with file and directory paths. It can be accessed using:
```
const path = require('node:path');
import path from 'node:path';
copy
```

### Windows vs. POSIX[#](https://nodejs.org/docs/latest/api/path.html#windows-vs-posix)
The default operation of the `node:path` module varies based on the operating system on which a Node.js application is running. Specifically, when running on a Windows operating system, the `node:path` module will assume that Windows-style paths are being used.
So using `path.basename()` might yield different results on POSIX and Windows:
On POSIX:
```
path.basename('C:\\temp\\myfile.html');
// Returns: 'C:\\temp\\myfile.html'
copy
```

On Windows:
```
path.basename('C:\\temp\\myfile.html');
// Returns: 'myfile.html'
copy
```

To achieve consistent results when working with Windows file paths on any operating system, use [`path.win32`](https://nodejs.org/docs/latest/api/path.html#pathwin32):
On POSIX and Windows:
```
path.win32.basename('C:\\temp\\myfile.html');
// Returns: 'myfile.html'
copy
```

To achieve consistent results when working with POSIX file paths on any operating system, use [`path.posix`](https://nodejs.org/docs/latest/api/path.html#pathposix):
On POSIX and Windows:
```
path.posix.basename('/tmp/myfile.html');
// Returns: 'myfile.html'
copy
```

On Windows Node.js follows the concept of per-drive working directory. This behavior can be observed when using a drive path without a backslash. For example, `path.resolve('C:\\')` can potentially return a different result than `path.resolve('C:')`. For more information, see
###  `path.basename(path[, suffix])`[#](https://nodejs.org/docs/latest/api/path.html#pathbasenamepath-suffix)
Added in: v0.1.25History Version | Changes
---|---
v6.0.0 | Passing a non-string as the `path` argument will throw now.
  * `path`
  * `suffix`
  * Returns:


The `path.basename()` method returns the last portion of a `path`, similar to the Unix `basename` command. Trailing [directory separators](https://nodejs.org/docs/latest/api/path.html#pathsep) are ignored.
```
path.basename('/foo/bar/baz/asdf/quux.html');
// Returns: 'quux.html'

path.basename('/foo/bar/baz/asdf/quux.html', '.html');
// Returns: 'quux'
copy
```

Although Windows usually treats file names, including file extensions, in a case-insensitive manner, this function does not. For example, `C:\\foo.html` and `C:\\foo.HTML` refer to the same file, but `basename` treats the extension as a case-sensitive string:
```
path.win32.basename('C:\\foo.html', '.html');
// Returns: 'foo'

path.win32.basename('C:\\foo.HTML', '.html');
// Returns: 'foo.HTML'
copy
```

A [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) is thrown if `path` is not a string or if `suffix` is given and is not a string.
###  `path.delimiter`[#](https://nodejs.org/docs/latest/api/path.html#pathdelimiter)
Added in: v0.9.3
  * Type:


Provides the platform-specific path delimiter:
  * `;` for Windows
  * `:` for POSIX


For example, on POSIX:
```
console.log(process.env.PATH);
// Prints: '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin'

process.env.PATH.split(path.delimiter);
// Returns: ['/usr/bin', '/bin', '/usr/sbin', '/sbin', '/usr/local/bin']
copy
```

On Windows:
```
console.log(process.env.PATH);
// Prints: 'C:\Windows\system32;C:\Windows;C:\Program Files\node\'

process.env.PATH.split(path.delimiter);
// Returns ['C:\\Windows\\system32', 'C:\\Windows', 'C:\\Program Files\\node\\']
copy
```

###  `path.dirname(path)`[#](https://nodejs.org/docs/latest/api/path.html#pathdirnamepath)
Added in: v0.1.16History Version | Changes
---|---
v6.0.0 | Passing a non-string as the `path` argument will throw now.
  * `path`
  * Returns:


The `path.dirname()` method returns the directory name of a `path`, similar to the Unix `dirname` command. Trailing directory separators are ignored, see [`path.sep`](https://nodejs.org/docs/latest/api/path.html#pathsep).
```
path.dirname('/foo/bar/baz/asdf/quux');
// Returns: '/foo/bar/baz/asdf'
copy
```

A [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) is thrown if `path` is not a string.
###  `path.extname(path)`[#](https://nodejs.org/docs/latest/api/path.html#pathextnamepath)
Added in: v0.1.25History Version | Changes
---|---
v6.0.0 | Passing a non-string as the `path` argument will throw now.
  * `path`
  * Returns:


The `path.extname()` method returns the extension of the `path`, from the last occurrence of the `.` (period) character to end of string in the last portion of the `path`. If there is no `.` in the last portion of the `path`, or if there are no `.` characters other than the first character of the basename of `path` (see `path.basename()`) , an empty string is returned.
```
path.extname('index.html');
// Returns: '.html'

path.extname('index.coffee.md');
// Returns: '.md'

path.extname('index.');
// Returns: '.'

path.extname('index');
// Returns: ''

path.extname('.index');
// Returns: ''

path.extname('.index.md');
// Returns: '.md'
copy
```

A [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) is thrown if `path` is not a string.
###  `path.format(pathObject)`[#](https://nodejs.org/docs/latest/api/path.html#pathformatpathobject)
Added in: v0.11.15History Version | Changes
---|---
v19.0.0 | The dot will be added if it is not specified in `ext`.
  * `pathObject`
    * `dir`
    * `root`
    * `base`
    * `name`
    * `ext`
  * Returns:


The `path.format()` method returns a path string from an object. This is the opposite of [`path.parse()`](https://nodejs.org/docs/latest/api/path.html#pathparsepath).
When providing properties to the `pathObject` remember that there are combinations where one property has priority over another:
  * `pathObject.root` is ignored if `pathObject.dir` is provided
  * `pathObject.ext` and `pathObject.name` are ignored if `pathObject.base` exists


For example, on POSIX:
```
// If `dir`, `root` and `base` are provided,
// `${dir}${path.sep}${base}`
// will be returned. `root` is ignored.
path.format({
  root: '/ignored',
  dir: '/home/user/dir',
  base: 'file.txt',
});
// Returns: '/home/user/dir/file.txt'

// `root` will be used if `dir` is not specified.
// If only `root` is provided or `dir` is equal to `root` then the
// platform separator will not be included. `ext` will be ignored.
path.format({
  root: '/',
  base: 'file.txt',
  ext: 'ignored',
});
// Returns: '/file.txt'

// `name` + `ext` will be used if `base` is not specified.
path.format({
  root: '/',
  name: 'file',
  ext: '.txt',
});
// Returns: '/file.txt'

// The dot will be added if it is not specified in `ext`.
path.format({
  root: '/',
  name: 'file',
  ext: 'txt',
});
// Returns: '/file.txt'
copy
```

On Windows:
```
path.format({
  dir: 'C:\\path\\dir',
  base: 'file.txt',
});
// Returns: 'C:\\path\\dir\\file.txt'
copy
```

###  `path.matchesGlob(path, pattern)`[#](https://nodejs.org/docs/latest/api/path.html#pathmatchesglobpath-pattern)
Added in: v22.5.0, v20.17.0History Version | Changes
---|---
v24.8.0, v22.20.0 | Marking the API stable.
  * `path`
  * `pattern`
  * Returns: `path` matched the `pattern`.


The `path.matchesGlob()` method determines if `path` matches the `pattern`.
For example:
```
path.matchesGlob('/foo/bar', '/foo/*'); // true
path.matchesGlob('/foo/bar*', 'foo/bird'); // false
copy
```

A [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) is thrown if `path` or `pattern` are not strings.
###  `path.isAbsolute(path)`[#](https://nodejs.org/docs/latest/api/path.html#pathisabsolutepath)
Added in: v0.11.2
  * `path`
  * Returns:


The `path.isAbsolute()` method determines if the literal `path` is absolute. Therefore, it’s not safe for mitigating path traversals.
If the given `path` is a zero-length string, `false` will be returned.
For example, on POSIX:
```
path.isAbsolute('/foo/bar');   // true
path.isAbsolute('/baz/..');    // true
path.isAbsolute('/baz/../..'); // true
path.isAbsolute('qux/');       // false
path.isAbsolute('.');          // false
copy
```

On Windows:
```
path.isAbsolute('//server');    // true
path.isAbsolute('\\\\server');  // true
path.isAbsolute('C:/foo/..');   // true
path.isAbsolute('C:\\foo\\..'); // true
path.isAbsolute('bar\\baz');    // false
path.isAbsolute('bar/baz');     // false
path.isAbsolute('.');           // false
copy
```

A [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) is thrown if `path` is not a string.
###  `path.join([...paths])`[#](https://nodejs.org/docs/latest/api/path.html#pathjoinpaths)
Added in: v0.1.16
  * `...paths`
  * Returns:


The `path.join()` method joins all given `path` segments together using the platform-specific separator as a delimiter, then normalizes the resulting path.
Zero-length `path` segments are ignored. If the joined path string is a zero-length string then `'.'` will be returned, representing the current working directory.
```
path.join('/foo', 'bar', 'baz/asdf', 'quux', '..');
// Returns: '/foo/bar/baz/asdf'

path.join('foo', {}, 'bar');
// Throws 'TypeError: Path must be a string. Received {}'
copy
```

A [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) is thrown if any of the path segments is not a string.
###  `path.normalize(path)`[#](https://nodejs.org/docs/latest/api/path.html#pathnormalizepath)
Added in: v0.1.23
  * `path`
  * Returns:


The `path.normalize()` method normalizes the given `path`, resolving `'..'` and `'.'` segments.
When multiple, sequential path segment separation characters are found (e.g. `/` on POSIX and either `\` or `/` on Windows), they are replaced by a single instance of the platform-specific path segment separator (`/` on POSIX and `\` on Windows). Trailing separators are preserved.
If the `path` is a zero-length string, `'.'` is returned, representing the current working directory.
On POSIX, the types of normalization applied by this function do not strictly adhere to the POSIX specification. For example, this function will replace two leading forward slashes with a single slash as if it was a regular absolute path, whereas a few POSIX systems assign special meaning to paths beginning with exactly two forward slashes. Similarly, other substitutions performed by this function, such as removing `..` segments, may change how the underlying system resolves the path.
For example, on POSIX:
```
path.normalize('/foo/bar//baz/asdf/quux/..');
// Returns: '/foo/bar/baz/asdf'
copy
```

On Windows:
```
path.normalize('C:\\temp\\\\foo\\bar\\..\\');
// Returns: 'C:\\temp\\foo\\'
copy
```

Since Windows recognizes multiple path separators, both separators will be replaced by instances of the Windows preferred separator (`\`):
```
path.win32.normalize('C:////temp\\\\/\\/\\/foo/bar');
// Returns: 'C:\\temp\\foo\\bar'
copy
```

A [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) is thrown if `path` is not a string.
###  `path.parse(path)`[#](https://nodejs.org/docs/latest/api/path.html#pathparsepath)
Added in: v0.11.15
  * `path`
  * Returns:


The `path.parse()` method returns an object whose properties represent significant elements of the `path`. Trailing directory separators are ignored, see [`path.sep`](https://nodejs.org/docs/latest/api/path.html#pathsep).
The returned object will have the following properties:
  * `dir`
  * `root`
  * `base`
  * `name`
  * `ext`


For example, on POSIX:
```
path.parse('/home/user/dir/file.txt');
// Returns:
// { root: '/',
//   dir: '/home/user/dir',
//   base: 'file.txt',
//   ext: '.txt',
//   name: 'file' }
copy
```
```
┌─────────────────────┬────────────┐
│          dir        │    base    │
├──────┬              ├──────┬─────┤
│ root │              │ name │ ext │
"  /    home/user/dir / file  .txt "
└──────┴──────────────┴──────┴─────┘
(All spaces in the "" line should be ignored. They are purely for formatting.)
copy
```

On Windows:
```
path.parse('C:\\path\\dir\\file.txt');
// Returns:
// { root: 'C:\\',
//   dir: 'C:\\path\\dir',
//   base: 'file.txt',
//   ext: '.txt',
//   name: 'file' }
copy
```
```
┌─────────────────────┬────────────┐
│          dir        │    base    │
├──────┬              ├──────┬─────┤
│ root │              │ name │ ext │
" C:\      path\dir   \ file  .txt "
└──────┴──────────────┴──────┴─────┘
(All spaces in the "" line should be ignored. They are purely for formatting.)
copy
```

A [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) is thrown if `path` is not a string.
###  `path.posix`[#](https://nodejs.org/docs/latest/api/path.html#pathposix)
Added in: v0.11.15History Version | Changes
---|---
v15.3.0 | Exposed as `require('path/posix')`.
  * Type:


The `path.posix` property provides access to POSIX specific implementations of the `path` methods.
The API is accessible via `require('node:path').posix` or `require('node:path/posix')`.
###  `path.relative(from, to)`[#](https://nodejs.org/docs/latest/api/path.html#pathrelativefrom-to)
Added in: v0.5.0History Version | Changes
---|---
v6.8.0 | On Windows, the leading slashes for UNC paths are now included in the return value.
  * `from`
  * `to`
  * Returns:


The `path.relative()` method returns the relative path from `from` to `to` based on the current working directory. If `from` and `to` each resolve to the same path (after calling `path.resolve()` on each), a zero-length string is returned.
If a zero-length string is passed as `from` or `to`, the current working directory will be used instead of the zero-length strings.
For example, on POSIX:
```
path.relative('/data/orandea/test/aaa', '/data/orandea/impl/bbb');
// Returns: '../../impl/bbb'
copy
```

On Windows:
```
path.relative('C:\\orandea\\test\\aaa', 'C:\\orandea\\impl\\bbb');
// Returns: '..\\..\\impl\\bbb'
copy
```

A [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) is thrown if either `from` or `to` is not a string.
###  `path.resolve([...paths])`[#](https://nodejs.org/docs/latest/api/path.html#pathresolvepaths)
Added in: v0.3.4
  * `...paths`
  * Returns:


The `path.resolve()` method resolves a sequence of paths or path segments into an absolute path.
The given sequence of paths is processed from right to left, with each subsequent `path` prepended until an absolute path is constructed. For instance, given the sequence of path segments: `/foo`, `/bar`, `baz`, calling `path.resolve('/foo', '/bar', 'baz')` would return `/bar/baz` because `'baz'` is not an absolute path but `'/bar' + '/' + 'baz'` is.
If, after processing all given `path` segments, an absolute path has not yet been generated, the current working directory is used.
The resulting path is normalized and trailing slashes are removed unless the path is resolved to the root directory.
Zero-length `path` segments are ignored.
If no `path` segments are passed, `path.resolve()` will return the absolute path of the current working directory.
```
path.resolve('/foo/bar', './baz');
// Returns: '/foo/bar/baz'

path.resolve('/foo/bar', '/tmp/file/');
// Returns: '/tmp/file'

path.resolve('wwwroot', 'static_files/png/', '../gif/image.gif');
// If the current working directory is /home/myself/node,
// this returns '/home/myself/node/wwwroot/static_files/gif/image.gif'
copy
```

A [`TypeError`](https://nodejs.org/docs/latest/api/errors.html#class-typeerror) is thrown if any of the arguments is not a string.
###  `path.sep`[#](https://nodejs.org/docs/latest/api/path.html#pathsep)
Added in: v0.7.9
  * Type:


Provides the platform-specific path segment separator:
  * `\` on Windows
  * `/` on POSIX


For example, on POSIX:
```
'foo/bar/baz'.split(path.sep);
// Returns: ['foo', 'bar', 'baz']
copy
```

On Windows:
```
'foo\\bar\\baz'.split(path.sep);
// Returns: ['foo', 'bar', 'baz']
copy
```

On Windows, both the forward slash (`/`) and backward slash (`\`) are accepted as path segment separators; however, the `path` methods only add backward slashes (`\`).
###  `path.toNamespacedPath(path)`[#](https://nodejs.org/docs/latest/api/path.html#pathtonamespacedpathpath)
Added in: v9.0.0
  * `path`
  * Returns:


On Windows systems only, returns an equivalent `path`. If `path` is not a string, `path` will be returned without modifications.
This method is meaningful only on Windows systems. On POSIX systems, the method is non-operational and always returns `path` without modifications.
###  `path.win32`[#](https://nodejs.org/docs/latest/api/path.html#pathwin32)
Added in: v0.11.15History Version | Changes
---|---
v15.3.0 | Exposed as `require('path/win32')`.
  * Type:


The `path.win32` property provides access to Windows-specific implementations of the `path` methods.
The API is accessible via `require('node:path').win32` or `require('node:path/win32')`.
