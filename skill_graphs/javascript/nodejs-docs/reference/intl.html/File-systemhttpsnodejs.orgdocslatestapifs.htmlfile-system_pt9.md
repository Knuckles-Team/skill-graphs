

Synchronous `undefined`.
Using `fs.rmdirSync()` on a file (not a directory) results in an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.
To get a behavior similar to the `rm -rf` Unix command, use [`fs.rmSync()`](https://nodejs.org/docs/latest/api/fs.html#fsrmsyncpath-options) with options `{ recursive: true, force: true }`.
####  `fs.rmSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsrmsyncpath-options)
Added in: v14.14.0History Version | Changes
---|---
v17.3.0, v16.14.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `force` `true`, exceptions will be ignored if `path` does not exist. **Default:** `false`.
    * `maxRetries` `EBUSY`, `EMFILE`, `ENFILE`, `ENOTEMPTY`, or `EPERM` error is encountered, Node.js will retry the operation with a linear backoff wait of `retryDelay` milliseconds longer on each try. This option represents the number of retries. This option is ignored if the `recursive` option is not `true`. **Default:** `0`.
    * `recursive` `true`, perform a recursive directory removal. In recursive mode operations are retried on failure. **Default:** `false`.
    * `retryDelay` `recursive` option is not `true`. **Default:** `100`.


Synchronously removes files and directories (modeled on the standard POSIX `rm` utility). Returns `undefined`.
####  `fs.statSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsstatsyncpath-options)
Added in: v0.1.21History Version | Changes
---|---
v15.3.0, v14.17.0 | Accepts a `throwIfNoEntry` option to specify whether an exception should be thrown if the entry does not exist.
v10.5.0 | Accepts an additional `options` object to specify whether the numeric values returned should be bigint.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `bigint` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object should be `bigint`. **Default:** `false`.
    * `throwIfNoEntry` `undefined`. **Default:** `true`.
  * Returns: [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats)


Retrieves the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) for the path.
####  `fs.statfsSync(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsstatfssyncpath-options)
Added in: v19.6.0, v18.15.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `bigint` [`<fs.StatFs>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatfs) object should be `bigint`. **Default:** `false`.
  * Returns: [`<fs.StatFs>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatfs)


Synchronous `path`.
In case of an error, the `err.code` will be one of [Common System Errors](https://nodejs.org/docs/latest/api/errors.html#common-system-errors).
####  `fs.symlinkSync(target, path[, type])`[#](https://nodejs.org/docs/latest/api/fs.html#fssymlinksynctarget-path-type)
Added in: v0.1.31History Version | Changes
---|---
v12.0.0 | If the `type` argument is left undefined, Node will autodetect `target` type and automatically select `dir` or `file`.
v7.6.0 | The `target` and `path` parameters can be WHATWG `URL` objects using `file:` protocol. Support is currently still _experimental_.
  * `target` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `type` **Default:** `null`
  * Returns: `undefined`.


For detailed information, see the documentation of the asynchronous version of this API: [`fs.symlink()`](https://nodejs.org/docs/latest/api/fs.html#fssymlinktarget-path-type-callback).
####  `fs.truncateSync(path[, len])`[#](https://nodejs.org/docs/latest/api/fs.html#fstruncatesyncpath-len)
Added in: v0.8.6
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `len` **Default:** `0`


Truncates the file. Returns `undefined`. A file descriptor can also be passed as the first argument. In this case, `fs.ftruncateSync()` is called.
Passing a file descriptor is deprecated and may result in an error being thrown in the future.
####  `fs.unlinkSync(path)`[#](https://nodejs.org/docs/latest/api/fs.html#fsunlinksyncpath)
Added in: v0.1.21History Version | Changes
---|---
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)


Synchronous `undefined`.
####  `fs.utimesSync(path, atime, mtime)`[#](https://nodejs.org/docs/latest/api/fs.html#fsutimessyncpath-atime-mtime)
Added in: v0.4.2History Version | Changes
---|---
v8.0.0 | `NaN`, `Infinity`, and `-Infinity` are no longer valid time specifiers.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v4.1.0 | Numeric strings, `NaN`, and `Infinity` are now allowed time specifiers.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `atime`
  * `mtime`
  * Returns: `undefined`.


For detailed information, see the documentation of the asynchronous version of this API: [`fs.utimes()`](https://nodejs.org/docs/latest/api/fs.html#fsutimespath-atime-mtime-callback).
####  `fs.writeFileSync(file, data[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fswritefilesyncfile-data-options)
Added in: v0.1.29History Version | Changes
---|---
v21.0.0, v20.10.0 | The `flush` option is now supported.
v19.0.0 | Passing to the `data` parameter an object with an own `toString` function is no longer supported.
v17.8.0 | Passing to the `data` parameter an object with an own `toString` function is deprecated.
v14.12.0 | The `data` parameter will stringify an object with an explicit `toString` function.
v14.0.0 | The `data` parameter won't coerce unsupported input to strings anymore.
v10.10.0 | The `data` parameter can now be any `TypedArray` or a `DataView`.
v7.4.0 | The `data` parameter can now be a `Uint8Array`.
v5.0.0 | The `file` parameter can be a file descriptor now.
  * `file` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) |
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `mode` **Default:** `0o666`
    * `flag` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'w'`.
    * `flush` `flush` is `true`, `fs.fsyncSync()` is used to flush the data.
  * Returns: `undefined`.


The `mode` option only affects the newly created file. See [`fs.open()`](https://nodejs.org/docs/latest/api/fs.html#fsopenpath-flags-mode-callback) for more details.
For detailed information, see the documentation of the asynchronous version of this API: [`fs.writeFile()`](https://nodejs.org/docs/latest/api/fs.html#fswritefilefile-data-options-callback).
####  `fs.writeSync(fd, buffer, offset[, length[, position]])`[#](https://nodejs.org/docs/latest/api/fs.html#fswritesyncfd-buffer-offset-length-position)
Added in: v0.1.21History Version | Changes
---|---
v14.0.0 | The `buffer` parameter won't coerce unsupported input to strings anymore.
v10.10.0 | The `buffer` parameter can now be any `TypedArray` or a `DataView`.
v7.4.0 | The `buffer` parameter can now be a `Uint8Array`.
v7.2.0 | The `offset` and `length` parameters are optional now.
  * `fd`
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `offset` **Default:** `0`
  * `length` **Default:** `buffer.byteLength - offset`
  * `position` **Default:** `null`
  * Returns:


For detailed information, see the documentation of the asynchronous version of this API: [`fs.write(fd, buffer...)`](https://nodejs.org/docs/latest/api/fs.html#fswritefd-buffer-offset-length-position-callback).
####  `fs.writeSync(fd, buffer[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fswritesyncfd-buffer-options)
Added in: v18.3.0, v16.17.0
  * `fd`
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options`
    * `offset` **Default:** `0`
    * `length` **Default:** `buffer.byteLength - offset`
    * `position` **Default:** `null`
  * Returns:


For detailed information, see the documentation of the asynchronous version of this API: [`fs.write(fd, buffer...)`](https://nodejs.org/docs/latest/api/fs.html#fswritefd-buffer-offset-length-position-callback).
####  `fs.writeSync(fd, string[, position[, encoding]])`[#](https://nodejs.org/docs/latest/api/fs.html#fswritesyncfd-string-position-encoding)
Added in: v0.11.5History Version | Changes
---|---
v14.0.0 | The `string` parameter won't coerce unsupported input to strings anymore.
v7.2.0 | The `position` parameter is optional now.
  * `fd`
  * `string`
  * `position` **Default:** `null`
  * `encoding` **Default:** `'utf8'`
  * Returns:


For detailed information, see the documentation of the asynchronous version of this API: [`fs.write(fd, string...)`](https://nodejs.org/docs/latest/api/fs.html#fswritefd-string-position-encoding-callback).
####  `fs.writevSync(fd, buffers[, position])`[#](https://nodejs.org/docs/latest/api/fs.html#fswritevsyncfd-buffers-position)
Added in: v12.9.0
  * `fd`
  * `buffers`
  * `position` **Default:** `null`
  * Returns:


For detailed information, see the documentation of the asynchronous version of this API: [`fs.writev()`](https://nodejs.org/docs/latest/api/fs.html#fswritevfd-buffers-position-callback).
### Common Objects[#](https://nodejs.org/docs/latest/api/fs.html#common-objects)
The common objects are shared by all of the file system API variants (promise, callback, and synchronous).
#### Class: `fs.Dir`[#](https://nodejs.org/docs/latest/api/fs.html#class-fsdir)
Added in: v12.12.0
A class representing a directory stream.
Created by [`fs.opendir()`](https://nodejs.org/docs/latest/api/fs.html#fsopendirpath-options-callback), [`fs.opendirSync()`](https://nodejs.org/docs/latest/api/fs.html#fsopendirsyncpath-options), or [`fsPromises.opendir()`](https://nodejs.org/docs/latest/api/fs.html#fspromisesopendirpath-options).
```
import { opendir } from 'node:fs/promises';

try {
  const dir = await opendir('./');
  for await (const dirent of dir)
    console.log(dirent.name);
} catch (err) {
  console.error(err);
}
copy
```

When using the async iterator, the [`<fs.Dir>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir) object will be automatically closed after the iterator exits.
#####  `dir.close()`[#](https://nodejs.org/docs/latest/api/fs.html#dirclose)
Added in: v12.12.0
  * Returns:


Asynchronously close the directory's underlying resource handle. Subsequent reads will result in errors.
A promise is returned that will be fulfilled after the resource has been closed.
#####  `dir.close(callback)`[#](https://nodejs.org/docs/latest/api/fs.html#dirclosecallback)
Added in: v12.12.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `callback`
    * `err`


Asynchronously close the directory's underlying resource handle. Subsequent reads will result in errors.
The `callback` will be called after the resource handle has been closed.
#####  `dir.closeSync()`[#](https://nodejs.org/docs/latest/api/fs.html#dirclosesync)
Added in: v12.12.0
Synchronously close the directory's underlying resource handle. Subsequent reads will result in errors.
#####  `dir.path`[#](https://nodejs.org/docs/latest/api/fs.html#dirpath)
Added in: v12.12.0
  * Type:


The read-only path of this directory as was provided to [`fs.opendir()`](https://nodejs.org/docs/latest/api/fs.html#fsopendirpath-options-callback), [`fs.opendirSync()`](https://nodejs.org/docs/latest/api/fs.html#fsopendirsyncpath-options), or [`fsPromises.opendir()`](https://nodejs.org/docs/latest/api/fs.html#fspromisesopendirpath-options).
#####  `dir.read()`[#](https://nodejs.org/docs/latest/api/fs.html#dirread)
Added in: v12.12.0
  * Returns: [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) |


Asynchronously read the next directory entry via [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent).
A promise is returned that will be fulfilled with an [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent), or `null` if there are no more directory entries to read.
Directory entries returned by this function are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.
#####  `dir.read(callback)`[#](https://nodejs.org/docs/latest/api/fs.html#dirreadcallback)
Added in: v12.12.0
  * `callback`
    * `err`
    * `dirent` [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) |


Asynchronously read the next directory entry via [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent).
After the read is completed, the `callback` will be called with an [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent), or `null` if there are no more directory entries to read.
Directory entries returned by this function are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.
#####  `dir.readSync()`[#](https://nodejs.org/docs/latest/api/fs.html#dirreadsync)
Added in: v12.12.0
  * Returns: [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) |


Synchronously read the next directory entry as an [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent). See the POSIX
If there are no more directory entries to read, `null` will be returned.
Directory entries returned by this function are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.
#####  `dir[Symbol.asyncIterator]()`[#](https://nodejs.org/docs/latest/api/fs.html#dirsymbolasynciterator)
Added in: v12.12.0
  * Returns: [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent)


Asynchronously iterates over the directory until all entries have been read. Refer to the POSIX
Entries returned by the async iterator are always an [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent). The `null` case from `dir.read()` is handled internally.
See [`<fs.Dir>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir) for an example.
Directory entries returned by this iterator are in no particular order as provided by the operating system's underlying directory mechanisms. Entries added or removed while iterating over the directory might not be included in the iteration results.
#####  `dir[Symbol.asyncDispose]()`[#](https://nodejs.org/docs/latest/api/fs.html#dirsymbolasyncdispose)
Added in: v24.1.0, v22.1.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Calls `dir.close()` if the directory handle is open, and returns a promise that fulfills when disposal is complete.
#####  `dir[Symbol.dispose]()`[#](https://nodejs.org/docs/latest/api/fs.html#dirsymboldispose)
Added in: v24.1.0, v22.1.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Calls `dir.closeSync()` if the directory handle is open, and returns `undefined`.
#### Class: `fs.Dirent`[#](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent)
Added in: v10.10.0
A representation of a directory entry, which can be a file or a subdirectory within the directory, as returned by reading from an [`<fs.Dir>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir). The directory entry is a combination of the file name and file type pairs.
Additionally, when [`fs.readdir()`](https://nodejs.org/docs/latest/api/fs.html#fsreaddirpath-options-callback) or [`fs.readdirSync()`](https://nodejs.org/docs/latest/api/fs.html#fsreaddirsyncpath-options) is called with the `withFileTypes` option set to `true`, the resulting array is filled with [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) objects, rather than strings or [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)s.
#####  `dirent.isBlockDevice()`[#](https://nodejs.org/docs/latest/api/fs.html#direntisblockdevice)
Added in: v10.10.0
  * Returns:


Returns `true` if the [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) object describes a block device.
#####  `dirent.isCharacterDevice()`[#](https://nodejs.org/docs/latest/api/fs.html#direntischaracterdevice)
Added in: v10.10.0
  * Returns:


Returns `true` if the [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) object describes a character device.
#####  `dirent.isDirectory()`[#](https://nodejs.org/docs/latest/api/fs.html#direntisdirectory)
Added in: v10.10.0
  * Returns:


Returns `true` if the [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) object describes a file system directory.
#####  `dirent.isFIFO()`[#](https://nodejs.org/docs/latest/api/fs.html#direntisfifo)
Added in: v10.10.0
  * Returns:


Returns `true` if the [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) object describes a first-in-first-out (FIFO) pipe.
#####  `dirent.isFile()`[#](https://nodejs.org/docs/latest/api/fs.html#direntisfile)
Added in: v10.10.0
  * Returns:


Returns `true` if the [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) object describes a regular file.
#####  `dirent.isSocket()`[#](https://nodejs.org/docs/latest/api/fs.html#direntissocket)
Added in: v10.10.0
  * Returns:


Returns `true` if the [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) object describes a socket.
#####  `dirent.isSymbolicLink()`[#](https://nodejs.org/docs/latest/api/fs.html#direntissymboliclink)
Added in: v10.10.0
  * Returns:


Returns `true` if the [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) object describes a symbolic link.
#####  `dirent.name`[#](https://nodejs.org/docs/latest/api/fs.html#direntname)
Added in: v10.10.0
  * Type: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


The file name that this [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) object refers to. The type of this value is determined by the `options.encoding` passed to [`fs.readdir()`](https://nodejs.org/docs/latest/api/fs.html#fsreaddirpath-options-callback) or [`fs.readdirSync()`](https://nodejs.org/docs/latest/api/fs.html#fsreaddirsyncpath-options).
#####  `dirent.parentPath`[#](https://nodejs.org/docs/latest/api/fs.html#direntparentpath)
Added in: v21.4.0, v20.12.0, v18.20.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * Type:


The path to the parent directory of the file this [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) object refers to.
#### Class: `fs.FSWatcher`[#](https://nodejs.org/docs/latest/api/fs.html#class-fsfswatcher)
Added in: v0.5.8
  * Extends [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


A successful call to [`fs.watch()`](https://nodejs.org/docs/latest/api/fs.html#fswatchfilename-options-listener) method will return a new [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher) object.
All [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher) objects emit a `'change'` event whenever a specific watched file is modified.
##### Event: `'change'`[#](https://nodejs.org/docs/latest/api/fs.html#event-change)
Added in: v0.5.8
  * `eventType`
  * `filename` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The filename that changed (if relevant/available)


Emitted when something changes in a watched directory or file. See more details in [`fs.watch()`](https://nodejs.org/docs/latest/api/fs.html#fswatchfilename-options-listener).
The `filename` argument may not be provided depending on operating system support. If `filename` is provided, it will be provided as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) if `fs.watch()` is called with its `encoding` option set to `'buffer'`, otherwise `filename` will be a UTF-8 string.
```
import { watch } from 'node:fs';
// Example when handled through fs.watch() listener
watch('./tmp', { encoding: 'buffer' }, (eventType, filename) => {
  if (filename) {
    console.log(filename);
    // Prints: <Buffer ...>
  }
});
copy
```

##### Event: `'close'`[#](https://nodejs.org/docs/latest/api/fs.html#event-close-1)
Added in: v10.0.0
Emitted when the watcher stops watching for changes. The closed [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher) object is no longer usable in the event handler.
##### Event: `'error'`[#](https://nodejs.org/docs/latest/api/fs.html#event-error)
Added in: v0.5.8
  * `error`


Emitted when an error occurs while watching the file. The errored [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher) object is no longer usable in the event handler.
#####  `watcher.close()`[#](https://nodejs.org/docs/latest/api/fs.html#watcherclose)
Added in: v0.5.8
Stop watching for changes on the given [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher). Once stopped, the [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher) object is no longer usable.
#####  `watcher.ref()`[#](https://nodejs.org/docs/latest/api/fs.html#watcherref)
Added in: v14.3.0, v12.20.0
  * Returns: [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher)


When called, requests that the Node.js event loop _not_ exit so long as the [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher) is active. Calling `watcher.ref()` multiple times will have no effect.
By default, all [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher) objects are "ref'ed", making it normally unnecessary to call `watcher.ref()` unless `watcher.unref()` had been called previously.
#####  `watcher.unref()`[#](https://nodejs.org/docs/latest/api/fs.html#watcherunref)
Added in: v14.3.0, v12.20.0
  * Returns: [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher)


When called, the active [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher) object will not require the Node.js event loop to remain active. If there is no other activity keeping the event loop running, the process may exit before the [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher) object's callback is invoked. Calling `watcher.unref()` multiple times will have no effect.
#### Class: `fs.StatWatcher`[#](https://nodejs.org/docs/latest/api/fs.html#class-fsstatwatcher)
Added in: v14.3.0, v12.20.0
  * Extends [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


A successful call to `fs.watchFile()` method will return a new [`<fs.StatWatcher>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatwatcher) object.
#####  `watcher.ref()`[#](https://nodejs.org/docs/latest/api/fs.html#watcherref-1)
Added in: v14.3.0, v12.20.0
  * Returns: [`<fs.StatWatcher>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatwatcher)


When called, requests that the Node.js event loop _not_ exit so long as the [`<fs.StatWatcher>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatwatcher) is active. Calling `watcher.ref()` multiple times will have no effect.
By default, all [`<fs.StatWatcher>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatwatcher) objects are "ref'ed", making it normally unnecessary to call `watcher.ref()` unless `watcher.unref()` had been called previously.
#####  `watcher.unref()`[#](https://nodejs.org/docs/latest/api/fs.html#watcherunref-1)
Added in: v14.3.0, v12.20.0
  * Returns: [`<fs.StatWatcher>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatwatcher)


When called, the active [`<fs.StatWatcher>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatwatcher) object will not require the Node.js event loop to remain active. If there is no other activity keeping the event loop running, the process may exit before the [`<fs.StatWatcher>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatwatcher) object's callback is invoked. Calling `watcher.unref()` multiple times will have no effect.
