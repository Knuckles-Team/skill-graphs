  * `fs.constants.COPYFILE_EXCL`: The copy operation will fail if `dest` already exists.
  * `fs.constants.COPYFILE_FICLONE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then a fallback copy mechanism is used.
  * `fs.constants.COPYFILE_FICLONE_FORCE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then the operation will fail.

```
import { copyFileSync, constants } from 'node:fs';

// destination.txt will be created or overwritten by default.
copyFileSync('source.txt', 'destination.txt');
console.log('source.txt was copied to destination.txt');

// By using COPYFILE_EXCL, the operation will fail if destination.txt exists.
copyFileSync('source.txt', 'destination.txt', constants.COPYFILE_EXCL);
copy
```

####  `fs.cpSync(src, dest[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fscpsyncsrc-dest-options)
Added in: v16.7.0History Version | Changes
---|---
v22.3.0 | This API is no longer experimental.
v20.1.0, v18.17.0 | Accept an additional `mode` option to specify the copy behavior as the `mode` argument of `fs.copyFile()`.
v17.6.0, v16.15.0 | Accepts an additional `verbatimSymlinks` option to specify whether to perform path resolution for symlinks.
  * `src` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) source path to copy.
  * `dest` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) destination path to copy to.
  * `options`
    * `dereference` **Default:** `false`.
    * `errorOnExist` `force` is `false`, and the destination exists, throw an error. **Default:** `false`.
    * `filter` `true` to copy the item, `false` to ignore it. When ignoring a directory, all of its contents will be skipped as well. **Default:** `undefined`
      * `src`
      * `dest`
      * Returns: `Promise` value that is coercible to `boolean`.
    * `force` `errorOnExist` option to change this behavior. **Default:** `true`.
    * `mode` **Default:** `0`. See `mode` flag of [`fs.copyFileSync()`](https://nodejs.org/docs/latest/api/fs.html#fscopyfilesyncsrc-dest-mode).
    * `preserveTimestamps` `true` timestamps from `src` will be preserved. **Default:** `false`.
    * `recursive` **Default:** `false`
    * `verbatimSymlinks` `true`, path resolution for symlinks will be skipped. **Default:** `false`


Synchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.
When copying a directory to another directory, globs are not supported and behavior is similar to `cp dir1/ dir2/`.
####  `fs.existsSync(path)`[#](https://nodejs.org/docs/latest/api/fs.html#fsexistssyncpath)
Added in: v0.1.21History Version | Changes
---|---
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * Returns:


Returns `true` if the path exists, `false` otherwise.
For detailed information, see the documentation of the asynchronous version of this API: [`fs.exists()`](https://nodejs.org/docs/latest/api/fs.html#fsexistspath-callback).
`fs.exists()` is deprecated, but `fs.existsSync()` is not. The `callback` parameter to `fs.exists()` accepts parameters that are inconsistent with other Node.js callbacks. `fs.existsSync()` does not use a callback.
```
import { existsSync } from 'node:fs';

if (existsSync('/etc/passwd'))
  console.log('The path exists.');
copy
```

####  `fs.fchmodSync(fd, mode)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfchmodsyncfd-mode)
Added in: v0.4.7
  * `fd`
  * `mode`


Sets the permissions on the file. Returns `undefined`.
See the POSIX
####  `fs.fchownSync(fd, uid, gid)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfchownsyncfd-uid-gid)
Added in: v0.4.7
  * `fd`
  * `uid`
  * `gid`


Sets the owner of the file. Returns `undefined`.
See the POSIX
####  `fs.fdatasyncSync(fd)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfdatasyncsyncfd)
Added in: v0.1.96
  * `fd`


Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX `undefined`.
####  `fs.fstatSync(fd[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsfstatsyncfd-options)
Added in: v0.1.95History Version | Changes
---|---
v10.5.0 | Accepts an additional `options` object to specify whether the numeric values returned should be bigint.
  * `fd`
  * `options`
    * `bigint` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object should be `bigint`. **Default:** `false`.
  * Returns: [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats)


Retrieves the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) for the file descriptor.
See the POSIX
####  `fs.fsyncSync(fd)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfsyncsyncfd)
Added in: v0.1.96
  * `fd`


Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX `undefined`.
####  `fs.ftruncateSync(fd[, len])`[#](https://nodejs.org/docs/latest/api/fs.html#fsftruncatesyncfd-len)
Added in: v0.8.6
  * `fd`
  * `len` **Default:** `0`


Truncates the file descriptor. Returns `undefined`.
For detailed information, see the documentation of the asynchronous version of this API: [`fs.ftruncate()`](https://nodejs.org/docs/latest/api/fs.html#fsftruncatefd-len-callback).
####  `fs.futimesSync(fd, atime, mtime)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfutimessyncfd-atime-mtime)
Added in: v0.4.2History Version | Changes
---|---
v4.1.0 | Numeric strings, `NaN`, and `Infinity` are now allowed time specifiers.
  * `fd`
  * `atime`
  * `mtime`


Synchronous version of [`fs.futimes()`](https://nodejs.org/docs/latest/api/fs.html#fsfutimesfd-atime-mtime-callback). Returns `undefined`.
####  `fs.globSync(pattern[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsglobsyncpattern-options)
Added in: v22.0.0History Version | Changes
---|---
v24.1.0, v22.17.0 | Add support for `URL` instances for `cwd` option.
v24.0.0, v22.17.0 | Marking the API stable.
v23.7.0, v22.14.0 | Add support for `exclude` option to accept glob patterns.
v22.2.0 | Add support for `withFileTypes` as an option.
  * `pattern`
  * `options`
    * `cwd` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) current working directory. **Default:** `process.cwd()`
    * `exclude` `true` to exclude the item, `false` to include it. **Default:** `undefined`.
    * `withFileTypes` `true` if the glob should return paths as Dirents, `false` otherwise. **Default:** `false`.
  * Returns:

```
import { globSync } from 'node:fs';

console.log(globSync('**/*.js'));
const { globSync } = require('node:fs');

console.log(globSync('**/*.js'));
copy
```

####  `fs.lchmodSync(path, mode)`[#](https://nodejs.org/docs/latest/api/fs.html#fslchmodsyncpath-mode)
Deprecated in: v0.4.7
Stability: 0 - Deprecated
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `mode`


Changes the permissions on a symbolic link. Returns `undefined`.
This method is only implemented on macOS.
See the POSIX
####  `fs.lchownSync(path, uid, gid)`[#](https://nodejs.org/docs/latest/api/fs.html#fslchownsyncpath-uid-gid)
History Version | Changes
---|---
v10.6.0 | This API is no longer deprecated.
v0.4.7 | Documentation-only deprecation.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `uid`
  * `gid`


Set the owner for the path. Returns `undefined`.
See the POSIX
####  `fs.lutimesSync(path, atime, mtime)`[#](https://nodejs.org/docs/latest/api/fs.html#fslutimessyncpath-atime-mtime)
Added in: v14.5.0, v12.19.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `atime`
  * `mtime`


Change the file system timestamps of the symbolic link referenced by `path`. Returns `undefined`, or throws an exception when parameters are incorrect or the operation fails. This is the synchronous version of [`fs.lutimes()`](https://nodejs.org/docs/latest/api/fs.html#fslutimespath-atime-mtime-callback).
####  `fs.linkSync(existingPath, newPath)`[#](https://nodejs.org/docs/latest/api/fs.html#fslinksyncexistingpath-newpath)
Added in: v0.1.31History Version | Changes
---|---
v7.6.0 | The `existingPath` and `newPath` parameters can be WHATWG `URL` objects using `file:` protocol. Support is currently still _experimental_.
  * `existingPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `newPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)


Creates a new link from the `existingPath` to the `newPath`. See the POSIX `undefined`.
####  `fs.lstatSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fslstatsyncpath-options)
Added in: v0.1.30History Version | Changes
---|---
v15.3.0, v14.17.0 | Accepts a `throwIfNoEntry` option to specify whether an exception should be thrown if the entry does not exist.
v10.5.0 | Accepts an additional `options` object to specify whether the numeric values returned should be bigint.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `bigint` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object should be `bigint`. **Default:** `false`.
    * `throwIfNoEntry` `undefined`. **Default:** `true`.
  * Returns: [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats)


Retrieves the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) for the symbolic link referred to by `path`.
See the POSIX
####  `fs.mkdirSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsmkdirsyncpath-options)
Added in: v0.1.21History Version | Changes
---|---
v13.11.0, v12.17.0 | In `recursive` mode, the first created path is returned now.
v10.12.0 | The second argument can now be an `options` object with `recursive` and `mode` properties.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `recursive` **Default:** `false`
    * `mode` **Default:** `0o777`.
  * Returns:


Synchronously creates a directory. Returns `undefined`, or if `recursive` is `true`, the first directory path created. This is the synchronous version of [`fs.mkdir()`](https://nodejs.org/docs/latest/api/fs.html#fsmkdirpath-options-callback).
See the POSIX
####  `fs.mkdtempSync(prefix[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsmkdtempsyncprefix-options)
Added in: v5.10.0History Version | Changes
---|---
v20.6.0, v18.19.0 | The `prefix` parameter now accepts buffers and URL.
v16.5.0, v14.18.0 | The `prefix` parameter now accepts an empty string.
  * `prefix` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * Returns:


Returns the created directory path.
For detailed information, see the documentation of the asynchronous version of this API: [`fs.mkdtemp()`](https://nodejs.org/docs/latest/api/fs.html#fsmkdtempprefix-options-callback).
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.
####  `fs.mkdtempDisposableSync(prefix[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsmkdtempdisposablesyncprefix-options)
Added in: v24.4.0
  * `prefix` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * Returns:
    * `path`
    * `remove`
    * `[Symbol.dispose]` `remove`.


Returns a disposable object whose `path` property holds the created directory path. When the object is disposed, the directory and its contents will be removed if it still exists. If the directory cannot be deleted, disposal will throw an error. The object has a `remove()` method which will perform the same task.
For detailed information, see the documentation of [`fs.mkdtemp()`](https://nodejs.org/docs/latest/api/fs.html#fsmkdtempprefix-options-callback).
There is no callback-based version of this API because it is designed for use with the `using` syntax.
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.
####  `fs.opendirSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsopendirsyncpath-options)
Added in: v12.12.0History Version | Changes
---|---
v20.1.0, v18.17.0 | Added `recursive` option.
v13.1.0, v12.16.0 | The `bufferSize` option was introduced.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `bufferSize` **Default:** `32`
    * `recursive` **Default:** `false`
  * Returns: [`<fs.Dir>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir)


Synchronously open a directory. See
Creates an [`<fs.Dir>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir), which contains all further functions for reading from and cleaning up the directory.
The `encoding` option sets the encoding for the `path` while opening the directory and subsequent read operations.
####  `fs.openSync(path[, flags[, mode]])`[#](https://nodejs.org/docs/latest/api/fs.html#fsopensyncpath-flags-mode)
Added in: v0.1.21History Version | Changes
---|---
v11.1.0 | The `flags` argument is now optional and defaults to `'r'`.
v9.9.0 | The `as` and `as+` flags are supported now.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `flags` **Default:** `'r'`. See [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags).
  * `mode` **Default:** `0o666`
  * Returns:


Returns an integer representing the file descriptor.
For detailed information, see the documentation of the asynchronous version of this API: [`fs.open()`](https://nodejs.org/docs/latest/api/fs.html#fsopenpath-flags-mode-callback).
####  `fs.readdirSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsreaddirsyncpath-options)
Added in: v0.1.21History Version | Changes
---|---
v20.1.0, v18.17.0 | Added `recursive` option.
v10.10.0 | New option `withFileTypes` was added.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `withFileTypes` **Default:** `false`
    * `recursive` `true`, reads the contents of a directory recursively. In recursive mode, it will list all files, sub files, and directories. **Default:** `false`.
  * Returns: [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<fs.Dirent[]>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent)


Reads the contents of the directory.
See the POSIX
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the filenames returned. If the `encoding` is set to `'buffer'`, the filenames returned will be passed as [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) objects.
If `options.withFileTypes` is set to `true`, the result will contain [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) objects.
####  `fs.readFileSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadfilesyncpath-options)
Added in: v0.1.8History Version | Changes
---|---
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v5.0.0 | The `path` parameter can be a file descriptor now.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) |
  * `options`
    * `encoding` **Default:** `null`
    * `flag` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'r'`.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Returns the contents of the `path`.
For detailed information, see the documentation of the asynchronous version of this API: [`fs.readFile()`](https://nodejs.org/docs/latest/api/fs.html#fsreadfilepath-options-callback).
If the `encoding` option is specified then this function returns a string. Otherwise it returns a buffer.
Similar to [`fs.readFile()`](https://nodejs.org/docs/latest/api/fs.html#fsreadfilepath-options-callback), when the path is a directory, the behavior of `fs.readFileSync()` is platform-specific.
```
import { readFileSync } from 'node:fs';

// macOS, Linux, and Windows
readFileSync('<directory>');
// => [Error: EISDIR: illegal operation on a directory, read <directory>]

//  FreeBSD
readFileSync('<directory>'); // => <data>
copy
```

####  `fs.readlinkSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadlinksyncpath-options)
Added in: v0.1.31History Version | Changes
---|---
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Returns the symbolic link's string value.
See the POSIX
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the link path returned. If the `encoding` is set to `'buffer'`, the link path returned will be passed as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) object.
####  `fs.readSync(fd, buffer, offset, length[, position])`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadsyncfd-buffer-offset-length-position)
Added in: v0.1.21History Version | Changes
---|---
v10.10.0 | The `buffer` parameter can now be any `TypedArray` or a `DataView`.
v6.0.0 | The `length` parameter can now be `0`.
  * `fd`
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `offset`
  * `length`
  * `position` **Default:** `null`
  * Returns:


Returns the number of `bytesRead`.
For detailed information, see the documentation of the asynchronous version of this API: [`fs.read()`](https://nodejs.org/docs/latest/api/fs.html#fsreadfd-buffer-offset-length-position-callback).
####  `fs.readSync(fd, buffer[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadsyncfd-buffer-options)
Added in: v13.13.0, v12.17.0History Version | Changes
---|---
v13.13.0, v12.17.0 | Options object can be passed in to make offset, length, and position optional.
  * `fd`
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options`
    * `offset` **Default:** `0`
    * `length` **Default:** `buffer.byteLength - offset`
    * `position` **Default:** `null`
  * Returns:


Returns the number of `bytesRead`.
Similar to the above `fs.readSync` function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.
For detailed information, see the documentation of the asynchronous version of this API: [`fs.read()`](https://nodejs.org/docs/latest/api/fs.html#fsreadfd-buffer-offset-length-position-callback).
####  `fs.readvSync(fd, buffers[, position])`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadvsyncfd-buffers-position)
Added in: v13.13.0, v12.17.0
  * `fd`
  * `buffers`
  * `position` **Default:** `null`
  * Returns:


For detailed information, see the documentation of the asynchronous version of this API: [`fs.readv()`](https://nodejs.org/docs/latest/api/fs.html#fsreadvfd-buffers-position-callback).
####  `fs.realpathSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsrealpathsyncpath-options)
Added in: v0.1.31History Version | Changes
---|---
v8.0.0 | Pipe/Socket resolve support was added.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v6.4.0 | Calling `realpathSync` now works again for various edge cases on Windows.
v6.0.0 | The `cache` parameter was removed.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Returns the resolved pathname.
For detailed information, see the documentation of the asynchronous version of this API: [`fs.realpath()`](https://nodejs.org/docs/latest/api/fs.html#fsrealpathpath-options-callback).
####  `fs.realpathSync.native(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsrealpathsyncnativepath-options)
Added in: v9.2.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Synchronous
Only paths that can be converted to UTF8 strings are supported.
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the path returned. If the `encoding` is set to `'buffer'`, the path returned will be passed as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) object.
On Linux, when Node.js is linked against musl libc, the procfs file system must be mounted on `/proc` in order for this function to work. Glibc does not have this restriction.
####  `fs.renameSync(oldPath, newPath)`[#](https://nodejs.org/docs/latest/api/fs.html#fsrenamesyncoldpath-newpath)
Added in: v0.1.21History Version | Changes
---|---
v7.6.0 | The `oldPath` and `newPath` parameters can be WHATWG `URL` objects using `file:` protocol. Support is currently still _experimental_.
  * `oldPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `newPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)


Renames the file from `oldPath` to `newPath`. Returns `undefined`.
See the POSIX
####  `fs.rmdirSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsrmdirsyncpath-options)
Added in: v0.1.21History Version | Changes
---|---
v25.0.0 | Remove `recursive` option.
v16.0.0 | Using `fs.rmdirSync(path, { recursive: true })` on a `path` that is a file is no longer permitted and results in an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.
v16.0.0 | Using `fs.rmdirSync(path, { recursive: true })` on a `path` that does not exist is no longer permitted and results in a `ENOENT` error.
v16.0.0 | The `recursive` option is deprecated, using it triggers a deprecation warning.
v14.14.0 | The `recursive` option is deprecated, use `fs.rmSync` instead.
v13.3.0, v12.16.0 | The `maxBusyTries` option is renamed to `maxRetries`, and its default is 0. The `emfileWait` option has been removed, and `EMFILE` errors use the same retry logic as other errors. The `retryDelay` option is now supported. `ENFILE` errors are now retried.
v12.10.0 | The `recursive`, `maxBusyTries`, and `emfileWait` options are now supported.
v7.6.0 | The `path` parameters can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options` `recursive`, `maxBusyTries`, and `emfileWait` but they were deprecated and removed. The `options` argument is still accepted for backwards compatibility but it is not used.
