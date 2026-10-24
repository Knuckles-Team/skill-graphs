  1. Any specified file descriptor has to support reading.
  2. If a file descriptor is specified as the `path`, it will not be closed automatically.
  3. The reading will begin at the current position. For example, if the file already had `'Hello World'` and six bytes are read with the file descriptor, the call to `fs.readFile()` with the same file descriptor, would give `'World'`, rather than `'Hello World'`.


##### Performance Considerations[#](https://nodejs.org/docs/latest/api/fs.html#performance-considerations)
The `fs.readFile()` method asynchronously reads the contents of a file into memory one chunk at a time, allowing the event loop to turn between each chunk. This allows the read operation to have less impact on other activity that may be using the underlying libuv thread pool but means that it will take longer to read a complete file into memory.
The additional read overhead can vary broadly on different systems and depends on the type of file being read. If the file type is not a regular file (a pipe for instance) and Node.js is unable to determine an actual file size, each read operation will load on 64 KiB of data. For regular files, each read will process 512 KiB of data.
For applications that require as-fast-as-possible reading of file contents, it is better to use `fs.read()` directly and for application code to manage reading the full contents of the file itself.
The Node.js GitHub issue `fs.readFile()` for multiple file sizes in different Node.js versions.
####  `fs.readlink(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadlinkpath-options-callback)
Added in: v0.1.31History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * `callback`
    * `err`
    * `linkString` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Reads the contents of the symbolic link referred to by `path`. The callback gets two arguments `(err, linkString)`.
See the POSIX
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the link path passed to the callback. If the `encoding` is set to `'buffer'`, the link path returned will be passed as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) object.
####  `fs.readv(fd, buffers[, position], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadvfd-buffers-position-callback)
Added in: v13.13.0, v12.17.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `fd`
  * `buffers`
  * `position` **Default:** `null`
  * `callback`
    * `err`
    * `bytesRead`
    * `buffers`


Read from a file specified by `fd` and write to an array of `ArrayBufferView`s using `readv()`.
`position` is the offset from the beginning of the file from where data should be read. If `typeof position !== 'number'`, the data will be read from the current position.
The callback will be given three arguments: `err`, `bytesRead`, and `buffers`. `bytesRead` is how many bytes were read from the file.
If this method is invoked as its [`util.promisify()`](https://nodejs.org/docs/latest/api/util.html#utilpromisifyoriginal)ed version, it returns a promise for an `Object` with `bytesRead` and `buffers` properties.
####  `fs.realpath(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsrealpathpath-options-callback)
Added in: v0.1.31History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v8.0.0 | Pipe/Socket resolve support was added.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
v6.4.0 | Calling `realpath` now works again for various edge cases on Windows.
v6.0.0 | The `cache` parameter was removed.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * `callback`
    * `err`
    * `resolvedPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Asynchronously computes the canonical pathname by resolving `.`, `..`, and symbolic links.
A canonical pathname is not necessarily unique. Hard links and bind mounts can expose a file system entity through many pathnames.
This function behaves like
  1. No case conversion is performed on case-insensitive file systems.
  2. The maximum number of symbolic links is platform-independent and generally (much) higher than what the native


The `callback` gets two arguments `(err, resolvedPath)`. May use `process.cwd` to resolve relative paths.
Only paths that can be converted to UTF8 strings are supported.
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the path passed to the callback. If the `encoding` is set to `'buffer'`, the path returned will be passed as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) object.
If `path` resolves to a socket or a pipe, the function will return a system dependent name for that object.
A path that does not exist results in an ENOENT error. `error.path` is the absolute file path.
####  `fs.realpath.native(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsrealpathnativepath-options-callback)
Added in: v9.2.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * `callback`
    * `err`
    * `resolvedPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Asynchronous
The `callback` gets two arguments `(err, resolvedPath)`.
Only paths that can be converted to UTF8 strings are supported.
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the path passed to the callback. If the `encoding` is set to `'buffer'`, the path returned will be passed as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) object.
On Linux, when Node.js is linked against musl libc, the procfs file system must be mounted on `/proc` in order for this function to work. Glibc does not have this restriction.
####  `fs.rename(oldPath, newPath, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsrenameoldpath-newpath-callback)
Added in: v0.0.2History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `oldPath` and `newPath` parameters can be WHATWG `URL` objects using `file:` protocol. Support is currently still _experimental_.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `oldPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `newPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `callback`
    * `err`


Asynchronously rename file at `oldPath` to the pathname provided as `newPath`. In the case that `newPath` already exists, it will be overwritten. If there is a directory at `newPath`, an error will be raised instead. No arguments other than a possible exception are given to the completion callback.
See also:
```
import { rename } from 'node:fs';

rename('oldFile.txt', 'newFile.txt', (err) => {
  if (err) throw err;
  console.log('Rename complete!');
});
copy
```

####  `fs.rmdir(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsrmdirpath-options-callback)
Added in: v0.0.2History Version | Changes
---|---
v25.0.0 | Remove `recursive` option.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v16.0.0 | Using `fs.rmdir(path, { recursive: true })` on a `path` that is a file is no longer permitted and results in an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.
v16.0.0 | Using `fs.rmdir(path, { recursive: true })` on a `path` that does not exist is no longer permitted and results in a `ENOENT` error.
v16.0.0 | The `recursive` option is deprecated, using it triggers a deprecation warning.
v14.14.0 | The `recursive` option is deprecated, use `fs.rm` instead.
v13.3.0, v12.16.0 | The `maxBusyTries` option is renamed to `maxRetries`, and its default is 0. The `emfileWait` option has been removed, and `EMFILE` errors use the same retry logic as other errors. The `retryDelay` option is now supported. `ENFILE` errors are now retried.
v12.10.0 | The `recursive`, `maxBusyTries`, and `emfileWait` options are now supported.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `path` parameters can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options` `recursive`, `maxBusyTries`, and `emfileWait` but they were deprecated and removed. The `options` argument is still accepted for backwards compatibility but it is not used.
  * `callback`
    * `err`


Asynchronous
Using `fs.rmdir()` on a file (not a directory) results in an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.
To get a behavior similar to the `rm -rf` Unix command, use [`fs.rm()`](https://nodejs.org/docs/latest/api/fs.html#fsrmpath-options-callback) with options `{ recursive: true, force: true }`.
####  `fs.rm(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsrmpath-options-callback)
Added in: v14.14.0History Version | Changes
---|---
v17.3.0, v16.14.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `force` `true`, exceptions will be ignored if `path` does not exist. **Default:** `false`.
    * `maxRetries` `EBUSY`, `EMFILE`, `ENFILE`, `ENOTEMPTY`, or `EPERM` error is encountered, Node.js will retry the operation with a linear backoff wait of `retryDelay` milliseconds longer on each try. This option represents the number of retries. This option is ignored if the `recursive` option is not `true`. **Default:** `0`.
    * `recursive` `true`, perform a recursive removal. In recursive mode operations are retried on failure. **Default:** `false`.
    * `retryDelay` `recursive` option is not `true`. **Default:** `100`.
  * `callback`
    * `err`


Asynchronously removes files and directories (modeled on the standard POSIX `rm` utility). No arguments other than a possible exception are given to the completion callback.
####  `fs.stat(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsstatpath-options-callback)
Added in: v0.0.2History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.5.0 | Accepts an additional `options` object to specify whether the numeric values returned should be bigint.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `bigint` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object should be `bigint`. **Default:** `false`.
    * `throwIfNoEntry` `undefined`. **Default:** `true`.
  * `callback`
    * `err`
    * `stats` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats)


Asynchronous `(err, stats)` where `stats` is an [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object.
In case of an error, the `err.code` will be one of [Common System Errors](https://nodejs.org/docs/latest/api/errors.html#common-system-errors).
[`fs.stat()`](https://nodejs.org/docs/latest/api/fs.html#fsstatpath-options-callback) follows symbolic links. Use [`fs.lstat()`](https://nodejs.org/docs/latest/api/fs.html#fslstatpath-options-callback) to look at the links themselves.
Using `fs.stat()` to check for the existence of a file before calling `fs.open()`, `fs.readFile()`, or `fs.writeFile()` is not recommended. Instead, user code should open/read/write the file directly and handle the error raised if the file is not available.
To check if a file exists without manipulating it afterwards, [`fs.access()`](https://nodejs.org/docs/latest/api/fs.html#fsaccesspath-mode-callback) is recommended.
For example, given the following directory structure:
```
- txtDir
-- file.txt
- app.js
copy
```

The next program will check for the stats of the given paths:
```
import { stat } from 'node:fs';

const pathsToCheck = ['./txtDir', './txtDir/file.txt'];

for (let i = 0; i < pathsToCheck.length; i++) {
  stat(pathsToCheck[i], (err, stats) => {
    console.log(stats.isDirectory());
    console.log(stats);
  });
}
copy
```

The resulting output will resemble:
```
true
Stats {
  dev: 16777220,
  mode: 16877,
  nlink: 3,
  uid: 501,
  gid: 20,
  rdev: 0,
  blksize: 4096,
  ino: 14214262,
  size: 96,
  blocks: 0,
  atimeMs: 1561174653071.963,
  mtimeMs: 1561174614583.3518,
  ctimeMs: 1561174626623.5366,
  birthtimeMs: 1561174126937.2893,
  atime: 2019-06-22T03:37:33.072Z,
  mtime: 2019-06-22T03:36:54.583Z,
  ctime: 2019-06-22T03:37:06.624Z,
  birthtime: 2019-06-22T03:28:46.937Z
}
false
Stats {
  dev: 16777220,
  mode: 33188,
  nlink: 1,
  uid: 501,
  gid: 20,
  rdev: 0,
  blksize: 4096,
  ino: 14214074,
  size: 8,
  blocks: 8,
  atimeMs: 1561174616618.8555,
  mtimeMs: 1561174614584,
  ctimeMs: 1561174614583.8145,
  birthtimeMs: 1561174007710.7478,
  atime: 2019-06-22T03:36:56.619Z,
  mtime: 2019-06-22T03:36:54.584Z,
  ctime: 2019-06-22T03:36:54.584Z,
  birthtime: 2019-06-22T03:26:47.711Z
}
copy
```

####  `fs.statfs(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsstatfspath-options-callback)
Added in: v19.6.0, v18.15.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `bigint` [`<fs.StatFs>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatfs) object should be `bigint`. **Default:** `false`.
  * `callback`
    * `err`
    * `stats` [`<fs.StatFs>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatfs)


Asynchronous `path`. The callback gets two arguments `(err, stats)` where `stats` is an [`<fs.StatFs>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatfs) object.
In case of an error, the `err.code` will be one of [Common System Errors](https://nodejs.org/docs/latest/api/errors.html#common-system-errors).
####  `fs.symlink(target, path[, type], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fssymlinktarget-path-type-callback)
Added in: v0.1.31History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v12.0.0 | If the `type` argument is left undefined, Node will autodetect `target` type and automatically select `dir` or `file`.
v7.6.0 | The `target` and `path` parameters can be WHATWG `URL` objects using `file:` protocol. Support is currently still _experimental_.
  * `target` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `type` **Default:** `null`
  * `callback`
    * `err`


Creates the link called `path` pointing to `target`. No arguments other than a possible exception are given to the completion callback.
See the POSIX
The `type` argument is only available on Windows and ignored on other platforms. It can be set to `'dir'`, `'file'`, or `'junction'`. If the `type` argument is `null`, Node.js will autodetect `target` type and use `'file'` or `'dir'`. If the `target` does not exist, `'file'` will be used. Windows junction points require the destination path to be absolute. When using `'junction'`, the `target` argument will automatically be normalized to absolute path. Junction points on NTFS volumes can only point to directories.
Relative targets are relative to the link's parent directory.
```
import { symlink } from 'node:fs';

symlink('./mew', './mewtwo', callback);
copy
```

The above example creates a symbolic link `mewtwo` which points to `mew` in the same directory:
```
$ tree .
.
├── mew
└── mewtwo -> ./mew
copy
```

####  `fs.truncate(path[, len], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fstruncatepath-len-callback)
Added in: v0.8.6History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v16.0.0 | The error returned may be an `AggregateError` if more than one error is returned.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `len` **Default:** `0`
  * `callback`
    * `err`


Truncates the file. No arguments other than a possible exception are given to the completion callback. A file descriptor can also be passed as the first argument. In this case, `fs.ftruncate()` is called.
```
import { truncate } from 'node:fs';
// Assuming that 'path/file.txt' is a regular file.
truncate('path/file.txt', (err) => {
  if (err) throw err;
  console.log('path/file.txt was truncated');
});
const { truncate } = require('node:fs');
// Assuming that 'path/file.txt' is a regular file.
truncate('path/file.txt', (err) => {
  if (err) throw err;
  console.log('path/file.txt was truncated');
});
copy
```

Passing a file descriptor is deprecated and may result in an error being thrown in the future.
See the POSIX
####  `fs.unlink(path, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsunlinkpath-callback)
Added in: v0.0.2History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `callback`
    * `err`


Asynchronously removes a file or symbolic link. No arguments other than a possible exception are given to the completion callback.
```
import { unlink } from 'node:fs';
// Assuming that 'path/file.txt' is a regular file.
unlink('path/file.txt', (err) => {
  if (err) throw err;
  console.log('path/file.txt was deleted');
});
copy
```

`fs.unlink()` will not work on a directory, empty or otherwise. To remove a directory, use [`fs.rmdir()`](https://nodejs.org/docs/latest/api/fs.html#fsrmdirpath-options-callback).
See the POSIX
####  `fs.unwatchFile(filename[, listener])`[#](https://nodejs.org/docs/latest/api/fs.html#fsunwatchfilefilename-listener)
Added in: v0.1.31
  * `filename` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `listener` `fs.watchFile()`


Stop watching for changes on `filename`. If `listener` is specified, only that particular listener is removed. Otherwise, _all_ listeners are removed, effectively stopping watching of `filename`.
Calling `fs.unwatchFile()` with a filename that is not being watched is a no-op, not an error.
Using [`fs.watch()`](https://nodejs.org/docs/latest/api/fs.html#fswatchfilename-options-listener) is more efficient than `fs.watchFile()` and `fs.unwatchFile()`. `fs.watch()` should be used instead of `fs.watchFile()` and `fs.unwatchFile()` when possible.
####  `fs.utimes(path, atime, mtime, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsutimespath-atime-mtime-callback)
Added in: v0.4.2History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v8.0.0 | `NaN`, `Infinity`, and `-Infinity` are no longer valid time specifiers.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
v4.1.0 | Numeric strings, `NaN`, and `Infinity` are now allowed time specifiers.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `atime`
  * `mtime`
  * `callback`
    * `err`


Change the file system timestamps of the object referenced by `path`.
The `atime` and `mtime` arguments follow these rules:
  * Values can be either numbers representing Unix epoch time in seconds, `Date`s, or a numeric string like `'123456789.0'`.
  * If the value can not be converted to a number, or is `NaN`, `Infinity`, or `-Infinity`, an `Error` will be thrown.


####  `fs.watch(filename[, options][, listener])`[#](https://nodejs.org/docs/latest/api/fs.html#fswatchfilename-options-listener)
Added in: v0.5.10History Version | Changes
---|---
v19.1.0 | Added recursive support for Linux, AIX and IBMi.
v15.9.0, v14.17.0 | Added support for closing the watcher with an AbortSignal.
v7.6.0 | The `filename` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The passed `options` object will never be modified.
  * `filename` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `persistent` **Default:** `true`.
    * `recursive` [caveats](https://nodejs.org/docs/latest/api/fs.html#caveats)). **Default:** `false`.
    * `encoding` **Default:** `'utf8'`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows closing the watcher with an AbortSignal.
    * `ignore` `true` to ignore. **Default:** `undefined`.
  * `listener` **Default:** `undefined`
    * `eventType`
    * `filename` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher)


Watch for changes on `filename`, where `filename` is either a file or a directory.
