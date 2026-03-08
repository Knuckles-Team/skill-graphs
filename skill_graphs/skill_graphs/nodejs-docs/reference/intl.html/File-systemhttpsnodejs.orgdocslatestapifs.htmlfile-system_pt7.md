The second argument is optional. If `options` is provided as a string, it specifies the `encoding`. Otherwise `options` should be passed as an object.
The listener callback gets two arguments `(eventType, filename)`. `eventType` is either `'rename'` or `'change'`, and `filename` is the name of the file which triggered the event.
On most platforms, `'rename'` is emitted whenever a filename appears or disappears in the directory.
The listener callback is attached to the `'change'` event fired by [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher), but it is not the same thing as the `'change'` value of `eventType`.
If a `signal` is passed, aborting the corresponding AbortController will close the returned [`<fs.FSWatcher>`](https://nodejs.org/docs/latest/api/fs.html#fsfswatcher).
##### Caveats[#](https://nodejs.org/docs/latest/api/fs.html#caveats)
The `fs.watch` API is not 100% consistent across platforms, and is unavailable in some situations.
On Windows, no events will be emitted if the watched directory is moved or renamed. An `EPERM` error is reported when the watched directory is deleted.
The `fs.watch` API does not provide any protection with respect to malicious actions on the file system. For example, on Windows it is implemented by monitoring changes in a directory versus specific files. This allows substitution of a file and fs reporting changes on the new file with the same filename.
###### Availability[#](https://nodejs.org/docs/latest/api/fs.html#availability)
This feature depends on the underlying operating system providing a way to be notified of file system changes.
  * On Linux systems, this uses
  * On BSD systems, this uses
  * On macOS, this uses
  * On SunOS systems (including Solaris and SmartOS), this uses
  * On Windows systems, this feature depends on
  * On AIX systems, this feature depends on
  * On IBM i systems, this feature is not supported.


If the underlying functionality is not available for some reason, then `fs.watch()` will not be able to function and may throw an exception. For example, watching files or directories can be unreliable, and in some cases impossible, on network file systems (NFS, SMB, etc) or host file systems when using virtualization software such as Vagrant or Docker.
It is still possible to use `fs.watchFile()`, which uses stat polling, but this method is slower and less reliable.
###### Inodes[#](https://nodejs.org/docs/latest/api/fs.html#inodes)
On Linux and macOS systems, `fs.watch()` resolves the path to an _original_ inode. Events for the new inode will not be emitted. This is expected behavior.
AIX files retain the same inode for the lifetime of a file. Saving and closing a watched file on AIX will result in two notifications (one for adding new content, and one for truncation).
###### Filename argument[#](https://nodejs.org/docs/latest/api/fs.html#filename-argument)
Providing `filename` argument in the callback is only supported on Linux, macOS, Windows, and AIX. Even on supported platforms, `filename` is not always guaranteed to be provided. Therefore, don't assume that `filename` argument is always provided in the callback, and have some fallback logic if it is `null`.
```
import { watch } from 'node:fs';
watch('somedir', (eventType, filename) => {
  console.log(`event type is: ${eventType}`);
  if (filename) {
    console.log(`filename provided: ${filename}`);
  } else {
    console.log('filename not provided');
  }
});
copy
```

####  `fs.watchFile(filename[, options], listener)`[#](https://nodejs.org/docs/latest/api/fs.html#fswatchfilefilename-options-listener)
Added in: v0.1.31History Version | Changes
---|---
v10.5.0 | The `bigint` option is now supported.
v7.6.0 | The `filename` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `filename` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `bigint` **Default:** `false`
    * `persistent` **Default:** `true`
    * `interval` **Default:** `5007`
  * `listener`
    * `current` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats)
    * `previous` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats)
  * Returns: [`<fs.StatWatcher>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatwatcher)


Watch for changes on `filename`. The callback `listener` will be called each time the file is accessed.
The `options` argument may be omitted. If provided, it should be an object. The `options` object may contain a boolean named `persistent` that indicates whether the process should continue to run as long as files are being watched. The `options` object may specify an `interval` property indicating how often the target should be polled in milliseconds.
The `listener` gets two arguments the current stat object and the previous stat object:
```
import { watchFile } from 'node:fs';

watchFile('message.text', (curr, prev) => {
  console.log(`the current mtime is: ${curr.mtime}`);
  console.log(`the previous mtime was: ${prev.mtime}`);
});
copy
```

These stat objects are instances of `fs.Stat`. If the `bigint` option is `true`, the numeric values in these objects are specified as `BigInt`s.
To be notified when the file was modified, not just accessed, it is necessary to compare `curr.mtimeMs` and `prev.mtimeMs`.
When an `fs.watchFile` operation results in an `ENOENT` error, it will invoke the listener once, with all the fields zeroed (or, for dates, the Unix Epoch). If the file is created later on, the listener will be called again, with the latest stat objects. This is a change in functionality since v0.10.
Using [`fs.watch()`](https://nodejs.org/docs/latest/api/fs.html#fswatchfilename-options-listener) is more efficient than `fs.watchFile` and `fs.unwatchFile`. `fs.watch` should be used instead of `fs.watchFile` and `fs.unwatchFile` when possible.
When a file being watched by `fs.watchFile()` disappears and reappears, then the contents of `previous` in the second callback event (the file's reappearance) will be the same as the contents of `previous` in the first callback event (its disappearance).
This happens when:
  * the file is deleted, followed by a restore
  * the file is renamed and then renamed a second time back to its original name


####  `fs.write(fd, buffer, offset[, length[, position]], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fswritefd-buffer-offset-length-position-callback)
Added in: v0.0.2History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v14.0.0 | The `buffer` parameter won't coerce unsupported input to strings anymore.
v10.10.0 | The `buffer` parameter can now be any `TypedArray` or a `DataView`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.4.0 | The `buffer` parameter can now be a `Uint8Array`.
v7.2.0 | The `offset` and `length` parameters are optional now.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `fd`
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `offset` **Default:** `0`
  * `length` **Default:** `buffer.byteLength - offset`
  * `position` **Default:** `null`
  * `callback`
    * `err`
    * `bytesWritten`
    * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Write `buffer` to the file specified by `fd`.
`offset` determines the part of the buffer to be written, and `length` is an integer specifying the number of bytes to write.
`position` refers to the offset from the beginning of the file where this data should be written. If `typeof position !== 'number'`, the data will be written at the current position. See
The callback will be given three arguments `(err, bytesWritten, buffer)` where `bytesWritten` specifies how many _bytes_ were written from `buffer`.
If this method is invoked as its [`util.promisify()`](https://nodejs.org/docs/latest/api/util.html#utilpromisifyoriginal)ed version, it returns a promise for an `Object` with `bytesWritten` and `buffer` properties.
It is unsafe to use `fs.write()` multiple times on the same file without waiting for the callback. For this scenario, [`fs.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options) is recommended.
On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.
####  `fs.write(fd, buffer[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fswritefd-buffer-options-callback)
Added in: v18.3.0, v16.17.0
  * `fd`
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options`
    * `offset` **Default:** `0`
    * `length` **Default:** `buffer.byteLength - offset`
    * `position` **Default:** `null`
  * `callback`
    * `err`
    * `bytesWritten`
    * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Write `buffer` to the file specified by `fd`.
Similar to the above `fs.write` function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.
####  `fs.write(fd, string[, position[, encoding]], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fswritefd-string-position-encoding-callback)
Added in: v0.11.5History Version | Changes
---|---
v19.0.0 | Passing to the `string` parameter an object with an own `toString` function is no longer supported.
v17.8.0 | Passing to the `string` parameter an object with an own `toString` function is deprecated.
v14.12.0 | The `string` parameter will stringify an object with an explicit `toString` function.
v14.0.0 | The `string` parameter won't coerce unsupported input to strings anymore.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.2.0 | The `position` parameter is optional now.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `fd`
  * `string`
  * `position` **Default:** `null`
  * `encoding` **Default:** `'utf8'`
  * `callback`
    * `err`
    * `written`
    * `string`


Write `string` to the file specified by `fd`. If `string` is not a string, an exception is thrown.
`position` refers to the offset from the beginning of the file where this data should be written. If `typeof position !== 'number'` the data will be written at the current position. See
`encoding` is the expected string encoding.
The callback will receive the arguments `(err, written, string)` where `written` specifies how many _bytes_ the passed string required to be written. Bytes written is not necessarily the same as string characters written. See [`Buffer.byteLength`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferbytelengthstring-encoding).
It is unsafe to use `fs.write()` multiple times on the same file without waiting for the callback. For this scenario, [`fs.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options) is recommended.
On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.
On Windows, if the file descriptor is connected to the console (e.g. `fd == 1` or `stdout`) a string containing non-ASCII characters will not be rendered properly by default, regardless of the encoding used. It is possible to configure the console to render UTF-8 properly by changing the active codepage with the `chcp 65001` command. See the
####  `fs.writeFile(file, data[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fswritefilefile-data-options-callback)
Added in: v0.1.29History Version | Changes
---|---
v21.0.0, v20.10.0 | The `flush` option is now supported.
v19.0.0 | Passing to the `string` parameter an object with an own `toString` function is no longer supported.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v17.8.0 | Passing to the `string` parameter an object with an own `toString` function is deprecated.
v16.0.0 | The error returned may be an `AggregateError` if more than one error is returned.
v15.2.0, v14.17.0 | The options argument may include an AbortSignal to abort an ongoing writeFile request.
v14.12.0 | The `data` parameter will stringify an object with an explicit `toString` function.
v14.0.0 | The `data` parameter won't coerce unsupported input to strings anymore.
v10.10.0 | The `data` parameter can now be any `TypedArray` or a `DataView`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.4.0 | The `data` parameter can now be a `Uint8Array`.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
v5.0.0 | The `file` parameter can be a file descriptor now.
  * `file` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) |
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `mode` **Default:** `0o666`
    * `flag` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'w'`.
    * `flush` `flush` is `true`, `fs.fsync()` is used to flush the data. **Default:** `false`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows aborting an in-progress writeFile
  * `callback`
    * `err`


When `file` is a filename, asynchronously writes data to the file, replacing the file if it already exists. `data` can be a string or a buffer.
When `file` is a file descriptor, the behavior is similar to calling `fs.write()` directly (which is recommended). See the notes below on using a file descriptor.
The `encoding` option is ignored if `data` is a buffer.
The `mode` option only affects the newly created file. See [`fs.open()`](https://nodejs.org/docs/latest/api/fs.html#fsopenpath-flags-mode-callback) for more details.
```
import { writeFile } from 'node:fs';
import { Buffer } from 'node:buffer';

const data = new Uint8Array(Buffer.from('Hello Node.js'));
writeFile('message.txt', data, (err) => {
  if (err) throw err;
  console.log('The file has been saved!');
});
copy
```

If `options` is a string, then it specifies the encoding:
```
import { writeFile } from 'node:fs';

writeFile('message.txt', 'Hello Node.js', 'utf8', callback);
copy
```

It is unsafe to use `fs.writeFile()` multiple times on the same file without waiting for the callback. For this scenario, [`fs.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options) is recommended.
Similarly to `fs.readFile` - `fs.writeFile` is a convenience method that performs multiple `write` calls internally to write the buffer passed to it. For performance sensitive code consider using [`fs.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options).
It is possible to use an [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) to cancel an `fs.writeFile()`. Cancellation is "best effort", and some amount of data is likely still to be written.
```
import { writeFile } from 'node:fs';
import { Buffer } from 'node:buffer';

const controller = new AbortController();
const { signal } = controller;
const data = new Uint8Array(Buffer.from('Hello Node.js'));
writeFile('message.txt', data, { signal }, (err) => {
  // When a request is aborted - the callback is called with an AbortError
});
// When the request should be aborted
controller.abort();
copy
```

Aborting an ongoing request does not abort individual operating system requests but rather the internal buffering `fs.writeFile` performs.
##### Using `fs.writeFile()` with file descriptors[#](https://nodejs.org/docs/latest/api/fs.html#using-fswritefile-with-file-descriptors)
When `file` is a file descriptor, the behavior is almost identical to directly calling `fs.write()` like:
```
import { write } from 'node:fs';
import { Buffer } from 'node:buffer';

write(fd, Buffer.from(data, options.encoding), callback);
copy
```

The difference from directly calling `fs.write()` is that under some unusual conditions, `fs.write()` might write only part of the buffer and need to be retried to write the remaining data, whereas `fs.writeFile()` retries until the data is entirely written (or an error occurs).
The implications of this are a common source of confusion. In the file descriptor case, the file is not replaced! The data is not necessarily written to the beginning of the file, and the file's original data may remain before and/or after the newly written data.
For example, if `fs.writeFile()` is called twice in a row, first to write the string `'Hello'`, then to write the string `', World'`, the file would contain `'Hello, World'`, and might contain some of the file's original data (depending on the size of the original file, and the position of the file descriptor). If a file name had been used instead of a descriptor, the file would be guaranteed to contain only `', World'`.
####  `fs.writev(fd, buffers[, position], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fswritevfd-buffers-position-callback)
Added in: v12.9.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `fd`
  * `buffers`
  * `position` **Default:** `null`
  * `callback`
    * `err`
    * `bytesWritten`
    * `buffers`


Write an array of `ArrayBufferView`s to the file specified by `fd` using `writev()`.
`position` is the offset from the beginning of the file where this data should be written. If `typeof position !== 'number'`, the data will be written at the current position.
The callback will be given three arguments: `err`, `bytesWritten`, and `buffers`. `bytesWritten` is how many bytes were written from `buffers`.
If this method is [`util.promisify()`](https://nodejs.org/docs/latest/api/util.html#utilpromisifyoriginal)ed, it returns a promise for an `Object` with `bytesWritten` and `buffers` properties.
It is unsafe to use `fs.writev()` multiple times on the same file without waiting for the callback. For this scenario, use [`fs.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options).
On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.
### Synchronous API[#](https://nodejs.org/docs/latest/api/fs.html#synchronous-api)
The synchronous APIs perform all operations synchronously, blocking the event loop until the operation completes or fails.
####  `fs.accessSync(path[, mode])`[#](https://nodejs.org/docs/latest/api/fs.html#fsaccesssyncpath-mode)
Added in: v0.11.15History Version | Changes
---|---
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `mode` **Default:** `fs.constants.F_OK`


Synchronously tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g. `fs.constants.W_OK | fs.constants.R_OK`). Check [File access constants](https://nodejs.org/docs/latest/api/fs.html#file-access-constants) for possible values of `mode`.
If any of the accessibility checks fail, an `Error` will be thrown. Otherwise, the method will return `undefined`.
```
import { accessSync, constants } from 'node:fs';

try {
  accessSync('etc/passwd', constants.R_OK | constants.W_OK);
  console.log('can read/write');
} catch (err) {
  console.error('no access!');
}
copy
```

####  `fs.appendFileSync(path, data[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsappendfilesyncpath-data-options)
Added in: v0.6.7History Version | Changes
---|---
v21.1.0, v20.10.0 | The `flush` option is now supported.
v7.0.0 | The passed `options` object will never be modified.
v5.0.0 | The `file` parameter can be a file descriptor now.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) |
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `mode` **Default:** `0o666`
    * `flag` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'a'`.
    * `flush` `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.


Synchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer).
The `mode` option only affects the newly created file. See [`fs.open()`](https://nodejs.org/docs/latest/api/fs.html#fsopenpath-flags-mode-callback) for more details.
```
import { appendFileSync } from 'node:fs';

try {
  appendFileSync('message.txt', 'data to append');
  console.log('The "data to append" was appended to file!');
} catch (err) {
  /* Handle the error */
}
copy
```

If `options` is a string, then it specifies the encoding:
```
import { appendFileSync } from 'node:fs';

appendFileSync('message.txt', 'data to append', 'utf8');
copy
```

The `path` may be specified as a numeric file descriptor that has been opened for appending (using `fs.open()` or `fs.openSync()`). The file descriptor will not be closed automatically.
```
import { openSync, closeSync, appendFileSync } from 'node:fs';

let fd;

try {
  fd = openSync('message.txt', 'a');
  appendFileSync(fd, 'data to append', 'utf8');
} catch (err) {
  /* Handle the error */
} finally {
  if (fd !== undefined)
    closeSync(fd);
}
copy
```

####  `fs.chmodSync(path, mode)`[#](https://nodejs.org/docs/latest/api/fs.html#fschmodsyncpath-mode)
Added in: v0.6.7History Version | Changes
---|---
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `mode`


For detailed information, see the documentation of the asynchronous version of this API: [`fs.chmod()`](https://nodejs.org/docs/latest/api/fs.html#fschmodpath-mode-callback).
See the POSIX
####  `fs.chownSync(path, uid, gid)`[#](https://nodejs.org/docs/latest/api/fs.html#fschownsyncpath-uid-gid)
Added in: v0.1.97History Version | Changes
---|---
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `uid`
  * `gid`


Synchronously changes owner and group of a file. Returns `undefined`. This is the synchronous version of [`fs.chown()`](https://nodejs.org/docs/latest/api/fs.html#fschownpath-uid-gid-callback).
See the POSIX
####  `fs.closeSync(fd)`[#](https://nodejs.org/docs/latest/api/fs.html#fsclosesyncfd)
Added in: v0.1.21
  * `fd`


Closes the file descriptor. Returns `undefined`.
Calling `fs.closeSync()` on any file descriptor (`fd`) that is currently in use through any other `fs` operation may lead to undefined behavior.
See the POSIX
####  `fs.copyFileSync(src, dest[, mode])`[#](https://nodejs.org/docs/latest/api/fs.html#fscopyfilesyncsrc-dest-mode)
Added in: v8.5.0History Version | Changes
---|---
v14.0.0 | Changed `flags` argument to `mode` and imposed stricter type validation.
  * `src` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) source filename to copy
  * `dest` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) destination filename of the copy operation
  * `mode` **Default:** `0`.


Synchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists. Returns `undefined`. Node.js makes no guarantees about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, Node.js will attempt to remove the destination.
`mode` is an optional integer that specifies the behavior of the copy operation. It is possible to create a mask consisting of the bitwise OR of two or more values (e.g. `fs.constants.COPYFILE_EXCL | fs.constants.COPYFILE_FICLONE`).
