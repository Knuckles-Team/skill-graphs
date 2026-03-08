Caveats: on Windows only the write permission can be changed, and the distinction among the permissions of group, owner, or others is not implemented.
####  `fs.chown(path, uid, gid, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fschownpath-uid-gid-callback)
Added in: v0.1.97History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `uid`
  * `gid`
  * `callback`
    * `err`


Asynchronously changes owner and group of a file. No arguments other than a possible exception are given to the completion callback.
See the POSIX
####  `fs.close(fd[, callback])`[#](https://nodejs.org/docs/latest/api/fs.html#fsclosefd-callback)
Added in: v0.0.2History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v15.9.0, v14.17.0 | A default callback is now used if one is not provided.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `fd`
  * `callback`
    * `err`


Closes the file descriptor. No arguments other than a possible exception are given to the completion callback.
Calling `fs.close()` on any file descriptor (`fd`) that is currently in use through any other `fs` operation may lead to undefined behavior.
See the POSIX
####  `fs.copyFile(src, dest[, mode], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fscopyfilesrc-dest-mode-callback)
Added in: v8.5.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v14.0.0 | Changed `flags` argument to `mode` and imposed stricter type validation.
  * `src` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) source filename to copy
  * `dest` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) destination filename of the copy operation
  * `mode` **Default:** `0`.
  * `callback`
    * `err`


Asynchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists. No arguments other than a possible exception are given to the callback function. Node.js makes no guarantees about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, Node.js will attempt to remove the destination.
`mode` is an optional integer that specifies the behavior of the copy operation. It is possible to create a mask consisting of the bitwise OR of two or more values (e.g. `fs.constants.COPYFILE_EXCL | fs.constants.COPYFILE_FICLONE`).
  * `fs.constants.COPYFILE_EXCL`: The copy operation will fail if `dest` already exists.
  * `fs.constants.COPYFILE_FICLONE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then a fallback copy mechanism is used.
  * `fs.constants.COPYFILE_FICLONE_FORCE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then the operation will fail.

```
import { copyFile, constants } from 'node:fs';

function callback(err) {
  if (err) throw err;
  console.log('source.txt was copied to destination.txt');
}

// destination.txt will be created or overwritten by default.
copyFile('source.txt', 'destination.txt', callback);

// By using COPYFILE_EXCL, the operation will fail if destination.txt exists.
copyFile('source.txt', 'destination.txt', constants.COPYFILE_EXCL, callback);
copy
```

####  `fs.cp(src, dest[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fscpsrc-dest-options-callback)
Added in: v16.7.0History Version | Changes
---|---
v22.3.0 | This API is no longer experimental.
v20.1.0, v18.17.0 | Accept an additional `mode` option to specify the copy behavior as the `mode` argument of `fs.copyFile()`.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v17.6.0, v16.15.0 | Accepts an additional `verbatimSymlinks` option to specify whether to perform path resolution for symlinks.
  * `src` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) source path to copy.
  * `dest` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) destination path to copy to.
  * `options`
    * `dereference` **Default:** `false`.
    * `errorOnExist` `force` is `false`, and the destination exists, throw an error. **Default:** `false`.
    * `filter` `true` to copy the item, `false` to ignore it. When ignoring a directory, all of its contents will be skipped as well. Can also return a `Promise` that resolves to `true` or `false` **Default:** `undefined`.
      * `src`
      * `dest`
      * Returns: `boolean` or a `Promise` that fulfils with such value.
    * `force` `errorOnExist` option to change this behavior. **Default:** `true`.
    * `mode` **Default:** `0`. See `mode` flag of [`fs.copyFile()`](https://nodejs.org/docs/latest/api/fs.html#fscopyfilesrc-dest-mode-callback).
    * `preserveTimestamps` `true` timestamps from `src` will be preserved. **Default:** `false`.
    * `recursive` **Default:** `false`
    * `verbatimSymlinks` `true`, path resolution for symlinks will be skipped. **Default:** `false`
  * `callback`
    * `err`


Asynchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.
When copying a directory to another directory, globs are not supported and behavior is similar to `cp dir1/ dir2/`.
####  `fs.createReadStream(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fscreatereadstreampath-options)
Added in: v0.1.31History Version | Changes
---|---
v16.10.0 | The `fs` option does not need `open` method if an `fd` was provided.
v16.10.0 | The `fs` option does not need `close` method if `autoClose` is `false`.
v15.5.0 | Add support for `AbortSignal`.
v15.4.0 | The `fd` option accepts FileHandle arguments.
v14.0.0 | Change `emitClose` default to `true`.
v13.6.0, v12.17.0 | The `fs` options allow overriding the used `fs` implementation.
v12.10.0 | Enable `emitClose` option.
v11.0.0 | Impose new restrictions on `start` and `end`, throwing more appropriate errors in cases when we cannot reasonably handle the input values.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The passed `options` object will never be modified.
v2.3.0 | The passed `options` object can be a string now.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `flags` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'r'`.
    * `encoding` **Default:** `null`
    * `fd` [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) **Default:** `null`
    * `mode` **Default:** `0o666`
    * `autoClose` **Default:** `true`
    * `emitClose` **Default:** `true`
    * `start`
    * `end` **Default:** `Infinity`
    * `highWaterMark` **Default:** `64 * 1024`
    * `fs` **Default:** `null`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) | **Default:** `null`
  * Returns: [`<fs.ReadStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream)


`options` can include `start` and `end` values to read a range of bytes from the file instead of the entire file. Both `start` and `end` are inclusive and start counting at 0, allowed values are in the [0, `fd` is specified and `start` is omitted or `undefined`, `fs.createReadStream()` reads sequentially from the current file position. The `encoding` can be any one of those accepted by [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer).
If `fd` is specified, `ReadStream` will ignore the `path` argument and will use the specified file descriptor. This means that no `'open'` event will be emitted. `fd` should be blocking; non-blocking `fd`s should be passed to [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
If `fd` points to a character device that only supports blocking reads (such as keyboard or sound card), read operations do not finish until data is available. This can prevent the process from exiting and the stream from closing naturally.
By default, the stream will emit a `'close'` event after it has been destroyed. Set the `emitClose` option to `false` to change this behavior.
By providing the `fs` option, it is possible to override the corresponding `fs` implementations for `open`, `read`, and `close`. When providing the `fs` option, an override for `read` is required. If no `fd` is provided, an override for `open` is also required. If `autoClose` is `true`, an override for `close` is also required.
```
import { createReadStream } from 'node:fs';

// Create a stream from some character device.
const stream = createReadStream('/dev/input/event0');
setTimeout(() => {
  stream.close(); // This may not close the stream.
  // Artificially marking end-of-stream, as if the underlying resource had
  // indicated end-of-file by itself, allows the stream to close.
  // This does not cancel pending read operations, and if there is such an
  // operation, the process may still not be able to exit successfully
  // until it finishes.
  stream.push(null);
  stream.read(0);
}, 100);
copy
```

If `autoClose` is false, then the file descriptor won't be closed, even if there's an error. It is the application's responsibility to close it and make sure there's no file descriptor leak. If `autoClose` is set to true (default behavior), on `'error'` or `'end'` the file descriptor will be closed automatically.
`mode` sets the file mode (permission and sticky bits), but only if the file was created.
An example to read the last 10 bytes of a file which is 100 bytes long:
```
import { createReadStream } from 'node:fs';

createReadStream('sample.txt', { start: 90, end: 99 });
copy
```

If `options` is a string, then it specifies the encoding.
####  `fs.createWriteStream(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options)
Added in: v0.1.31History Version | Changes
---|---
v21.0.0, v20.10.0 | The `flush` option is now supported.
v16.10.0 | The `fs` option does not need `open` method if an `fd` was provided.
v16.10.0 | The `fs` option does not need `close` method if `autoClose` is `false`.
v15.5.0 | Add support for `AbortSignal`.
v15.4.0 | The `fd` option accepts FileHandle arguments.
v14.0.0 | Change `emitClose` default to `true`.
v13.6.0, v12.17.0 | The `fs` options allow overriding the used `fs` implementation.
v12.10.0 | Enable `emitClose` option.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The passed `options` object will never be modified.
v5.5.0 | The `autoClose` option is supported now.
v2.3.0 | The passed `options` object can be a string now.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `flags` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'w'`.
    * `encoding` **Default:** `'utf8'`
    * `fd` [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) **Default:** `null`
    * `mode` **Default:** `0o666`
    * `autoClose` **Default:** `true`
    * `emitClose` **Default:** `true`
    * `start`
    * `fs` **Default:** `null`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) | **Default:** `null`
    * `highWaterMark` **Default:** `16384`
    * `flush` `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.
  * Returns: [`<fs.WriteStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream)


`options` may also include a `start` option to allow writing data at some position past the beginning of the file, allowed values are in the [0, `flags` option to be set to `r+` rather than the default `w`. The `encoding` can be any one of those accepted by [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer).
If `autoClose` is set to true (default behavior) on `'error'` or `'finish'` the file descriptor will be closed automatically. If `autoClose` is false, then the file descriptor won't be closed, even if there's an error. It is the application's responsibility to close it and make sure there's no file descriptor leak.
By default, the stream will emit a `'close'` event after it has been destroyed. Set the `emitClose` option to `false` to change this behavior.
By providing the `fs` option it is possible to override the corresponding `fs` implementations for `open`, `write`, `writev`, and `close`. Overriding `write()` without `writev()` can reduce performance as some optimizations (`_writev()`) will be disabled. When providing the `fs` option, overrides for at least one of `write` and `writev` are required. If no `fd` option is supplied, an override for `open` is also required. If `autoClose` is `true`, an override for `close` is also required.
Like [`<fs.ReadStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream), if `fd` is specified, [`<fs.WriteStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream) will ignore the `path` argument and will use the specified file descriptor. This means that no `'open'` event will be emitted. `fd` should be blocking; non-blocking `fd`s should be passed to [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket).
If `options` is a string, then it specifies the encoding.
####  `fs.exists(path, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsexistspath-callback)
Added in: v0.0.2Deprecated in: v1.0.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
Stability: 0 - Deprecated: Use [`fs.stat()`](https://nodejs.org/docs/latest/api/fs.html#fsstatpath-options-callback) or [`fs.access()`](https://nodejs.org/docs/latest/api/fs.html#fsaccesspath-mode-callback) instead.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `callback`
    * `exists`


Test whether or not the element at the given `path` exists by checking with the file system. Then call the `callback` argument with either true or false:
```
import { exists } from 'node:fs';

exists('/etc/passwd', (e) => {
  console.log(e ? 'it exists' : 'no passwd!');
});
copy
```

**The parameters for this callback are not consistent with other Node.js callbacks.** Normally, the first parameter to a Node.js callback is an `err` parameter, optionally followed by other parameters. The `fs.exists()` callback has only one boolean parameter. This is one reason `fs.access()` is recommended instead of `fs.exists()`.
If `path` is a symbolic link, it is followed. Thus, if `path` exists but points to a non-existent element, the callback will receive the value `false`.
Using `fs.exists()` to check for the existence of a file before calling `fs.open()`, `fs.readFile()`, or `fs.writeFile()` is not recommended. Doing so introduces a race condition, since other processes may change the file's state between the two calls. Instead, user code should open/read/write the file directly and handle the error raised if the file does not exist.
**write (NOT RECOMMENDED)**
```
import { exists, open, close } from 'node:fs';

exists('myfile', (e) => {
  if (e) {
    console.error('myfile already exists');
  } else {
    open('myfile', 'wx', (err, fd) => {
      if (err) throw err;

      try {
        writeMyData(fd);
      } finally {
        close(fd, (err) => {
          if (err) throw err;
        });
      }
    });
  }
});
copy
```

**write (RECOMMENDED)**
```
import { open, close } from 'node:fs';
open('myfile', 'wx', (err, fd) => {
  if (err) {
    if (err.code === 'EEXIST') {
      console.error('myfile already exists');
      return;
    }

    throw err;
  }

  try {
    writeMyData(fd);
  } finally {
    close(fd, (err) => {
      if (err) throw err;
    });
  }
});
copy
```

**read (NOT RECOMMENDED)**
```
import { open, close, exists } from 'node:fs';

exists('myfile', (e) => {
  if (e) {
    open('myfile', 'r', (err, fd) => {
      if (err) throw err;

      try {
        readMyData(fd);
      } finally {
        close(fd, (err) => {
          if (err) throw err;
        });
      }
    });
  } else {
    console.error('myfile does not exist');
  }
});
copy
```

**read (RECOMMENDED)**
```
import { open, close } from 'node:fs';

open('myfile', 'r', (err, fd) => {
  if (err) {
    if (err.code === 'ENOENT') {
      console.error('myfile does not exist');
      return;
    }

    throw err;
  }

  try {
    readMyData(fd);
  } finally {
    close(fd, (err) => {
      if (err) throw err;
    });
  }
});
copy
```

The "not recommended" examples above check for existence and then use the file; the "recommended" examples are better because they use the file directly and handle the error, if any.
In general, check for the existence of a file only if the file won't be used directly, for example when its existence is a signal from another process.
####  `fs.fchmod(fd, mode, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfchmodfd-mode-callback)
Added in: v0.4.7History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `fd`
  * `mode`
  * `callback`
    * `err`


Sets the permissions on the file. No arguments other than a possible exception are given to the completion callback.
See the POSIX
####  `fs.fchown(fd, uid, gid, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfchownfd-uid-gid-callback)
Added in: v0.4.7History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `fd`
  * `uid`
  * `gid`
  * `callback`
    * `err`


Sets the owner of the file. No arguments other than a possible exception are given to the completion callback.
See the POSIX
####  `fs.fdatasync(fd, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfdatasyncfd-callback)
Added in: v0.1.96History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `fd`
  * `callback`
    * `err`


Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX
####  `fs.fstat(fd[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfstatfd-options-callback)
Added in: v0.1.95History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.5.0 | Accepts an additional `options` object to specify whether the numeric values returned should be bigint.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `fd`
  * `options`
    * `bigint` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object should be `bigint`. **Default:** `false`.
  * `callback`
    * `err`
    * `stats` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats)


Invokes the callback with the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) for the file descriptor.
See the POSIX
####  `fs.fsync(fd, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfsyncfd-callback)
Added in: v0.1.96History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `fd`
  * `callback`
    * `err`


Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX
####  `fs.ftruncate(fd[, len], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsftruncatefd-len-callback)
Added in: v0.8.6History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `fd`
  * `len` **Default:** `0`
  * `callback`
    * `err`


Truncates the file descriptor. No arguments other than a possible exception are given to the completion callback.
See the POSIX
If the file referred to by the file descriptor was larger than `len` bytes, only the first `len` bytes will be retained in the file.
For example, the following program retains only the first four bytes of the file:
```
import { open, close, ftruncate } from 'node:fs';

function closeFd(fd) {
  close(fd, (err) => {
    if (err) throw err;
  });
}

open('temp.txt', 'r+', (err, fd) => {
  if (err) throw err;

  try {
    ftruncate(fd, 4, (err) => {
      closeFd(fd);
      if (err) throw err;
    });
  } catch (err) {
    closeFd(fd);
    if (err) throw err;
  }
});
copy
```

If the file previously was shorter than `len` bytes, it is extended, and the extended part is filled with null bytes (`'\0'`):
If `len` is negative then `0` will be used.
####  `fs.futimes(fd, atime, mtime, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsfutimesfd-atime-mtime-callback)
Added in: v0.4.2History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
v4.1.0 | Numeric strings, `NaN`, and `Infinity` are now allowed time specifiers.
  * `fd`
  * `atime`
  * `mtime`
  * `callback`
    * `err`


Change the file system timestamps of the object referenced by the supplied file descriptor. See [`fs.utimes()`](https://nodejs.org/docs/latest/api/fs.html#fsutimespath-atime-mtime-callback).
####  `fs.glob(pattern[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsglobpattern-options-callback)
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
