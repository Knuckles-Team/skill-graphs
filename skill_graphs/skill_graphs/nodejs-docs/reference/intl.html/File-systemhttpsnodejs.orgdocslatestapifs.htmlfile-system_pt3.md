####  `fsPromises.realpath(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesrealpathpath-options)
Added in: v10.0.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * Returns:


Determines the actual location of `path` using the same semantics as the `fs.realpath.native()` function.
Only paths that can be converted to UTF8 strings are supported.
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the path. If the `encoding` is set to `'buffer'`, the path returned will be passed as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) object.
On Linux, when Node.js is linked against musl libc, the procfs file system must be mounted on `/proc` in order for this function to work. Glibc does not have this restriction.
####  `fsPromises.rename(oldPath, newPath)`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesrenameoldpath-newpath)
Added in: v10.0.0
  * `oldPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `newPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * Returns: `undefined` upon success.


Renames `oldPath` to `newPath`.
####  `fsPromises.rmdir(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesrmdirpath-options)
Added in: v10.0.0History Version | Changes
---|---
v25.0.0 | Remove `recursive` option.
v16.0.0 | Using `fsPromises.rmdir(path, { recursive: true })` on a `path` that is a file is no longer permitted and results in an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.
v16.0.0 | Using `fsPromises.rmdir(path, { recursive: true })` on a `path` that does not exist is no longer permitted and results in a `ENOENT` error.
v16.0.0 | The `recursive` option is deprecated, using it triggers a deprecation warning.
v14.14.0 | The `recursive` option is deprecated, use `fsPromises.rm` instead.
v13.3.0, v12.16.0 | The `maxBusyTries` option is renamed to `maxRetries`, and its default is 0. The `emfileWait` option has been removed, and `EMFILE` errors use the same retry logic as other errors. The `retryDelay` option is now supported. `ENFILE` errors are now retried.
v12.10.0 | The `recursive`, `maxBusyTries`, and `emfileWait` options are now supported.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options` `recursive`, `maxBusyTries`, and `emfileWait` but they were deprecated and removed. The `options` argument is still accepted for backwards compatibility but it is not used.
  * Returns: `undefined` upon success.


Removes the directory identified by `path`.
Using `fsPromises.rmdir()` on a file (not a directory) results in the promise being rejected with an `ENOENT` error on Windows and an `ENOTDIR` error on POSIX.
To get a behavior similar to the `rm -rf` Unix command, use [`fsPromises.rm()`](https://nodejs.org/docs/latest/api/fs.html#fspromisesrmpath-options) with options `{ recursive: true, force: true }`.
####  `fsPromises.rm(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesrmpath-options)
Added in: v14.14.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `force` `true`, exceptions will be ignored if `path` does not exist. **Default:** `false`.
    * `maxRetries` `EBUSY`, `EMFILE`, `ENFILE`, `ENOTEMPTY`, or `EPERM` error is encountered, Node.js will retry the operation with a linear backoff wait of `retryDelay` milliseconds longer on each try. This option represents the number of retries. This option is ignored if the `recursive` option is not `true`. **Default:** `0`.
    * `recursive` `true`, perform a recursive directory removal. In recursive mode operations are retried on failure. **Default:** `false`.
    * `retryDelay` `recursive` option is not `true`. **Default:** `100`.
  * Returns: `undefined` upon success.


Removes files and directories (modeled on the standard POSIX `rm` utility).
####  `fsPromises.stat(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesstatpath-options)
Added in: v10.0.0History Version | Changes
---|---
v10.5.0 | Accepts an additional `options` object to specify whether the numeric values returned should be bigint.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `bigint` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object should be `bigint`. **Default:** `false`.
    * `throwIfNoEntry` `undefined`. **Default:** `true`.
  * Returns: [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object for the given `path`.


####  `fsPromises.statfs(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesstatfspath-options)
Added in: v19.6.0, v18.15.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `bigint` [`<fs.StatFs>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatfs) object should be `bigint`. **Default:** `false`.
  * Returns: [`<fs.StatFs>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstatfs) object for the given `path`.


####  `fsPromises.symlink(target, path[, type])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisessymlinktarget-path-type)
Added in: v10.0.0History Version | Changes
---|---
v19.0.0 | If the `type` argument is `null` or omitted, Node.js will autodetect `target` type and automatically select `dir` or `file`.
  * `target` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `type` **Default:** `null`
  * Returns: `undefined` upon success.


Creates a symbolic link.
The `type` argument is only used on Windows platforms and can be one of `'dir'`, `'file'`, or `'junction'`. If the `type` argument is `null`, Node.js will autodetect `target` type and use `'file'` or `'dir'`. If the `target` does not exist, `'file'` will be used. Windows junction points require the destination path to be absolute. When using `'junction'`, the `target` argument will automatically be normalized to absolute path. Junction points on NTFS volumes can only point to directories.
####  `fsPromises.truncate(path[, len])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisestruncatepath-len)
Added in: v10.0.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `len` **Default:** `0`
  * Returns: `undefined` upon success.


Truncates (shortens or extends the length) of the content at `path` to `len` bytes.
####  `fsPromises.unlink(path)`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesunlinkpath)
Added in: v10.0.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * Returns: `undefined` upon success.


If `path` refers to a symbolic link, then the link is removed without affecting the file or directory to which that link refers. If the `path` refers to a file path that is not a symbolic link, the file is deleted. See the POSIX
####  `fsPromises.utimes(path, atime, mtime)`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesutimespath-atime-mtime)
Added in: v10.0.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `atime`
  * `mtime`
  * Returns: `undefined` upon success.


Change the file system timestamps of the object referenced by `path`.
The `atime` and `mtime` arguments follow these rules:
  * Values can be either numbers representing Unix epoch time, `Date`s, or a numeric string like `'123456789.0'`.
  * If the value can not be converted to a number, or is `NaN`, `Infinity`, or `-Infinity`, an `Error` will be thrown.


####  `fsPromises.watch(filename[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromiseswatchfilename-options)
Added in: v15.9.0, v14.18.0
  * `filename` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `persistent` **Default:** `true`.
    * `recursive` [caveats](https://nodejs.org/docs/latest/api/fs.html#caveats)). **Default:** `false`.
    * `encoding` **Default:** `'utf8'`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) An [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) used to signal when the watcher should stop.
    * `maxQueue` **Default:** `2048`.
    * `overflow` `'ignore'` or `'throw'` when there are more events to be queued than `maxQueue` allows. `'ignore'` means overflow events are dropped and a warning is emitted, while `'throw'` means to throw an exception. **Default:** `'ignore'`.
    * `ignore` `true` to ignore. **Default:** `undefined`.
  * Returns:
    * `eventType`
    * `filename` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Returns an async iterator that watches for changes on `filename`, where `filename` is either a file or a directory.
```
const { watch } = require('node:fs/promises');

const ac = new AbortController();
const { signal } = ac;
setTimeout(() => ac.abort(), 10000);

(async () => {
  try {
    const watcher = watch(__filename, { signal });
    for await (const event of watcher)
      console.log(event);
  } catch (err) {
    if (err.name === 'AbortError')
      return;
    throw err;
  }
})();
copy
```

On most platforms, `'rename'` is emitted whenever a filename appears or disappears in the directory.
All the [caveats](https://nodejs.org/docs/latest/api/fs.html#caveats) for `fs.watch()` also apply to `fsPromises.watch()`.
####  `fsPromises.writeFile(file, data[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromiseswritefilefile-data-options)
Added in: v10.0.0History Version | Changes
---|---
v21.0.0, v20.10.0 | The `flush` option is now supported.
v15.14.0, v14.18.0 | The `data` argument supports `AsyncIterable`, `Iterable`, and `Stream`.
v15.2.0, v14.17.0 | The options argument may include an AbortSignal to abort an ongoing writeFile request.
v14.0.0 | The `data` parameter won't coerce unsupported input to strings anymore.
  * `file` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) | [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) filename or `FileHandle`
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `mode` **Default:** `0o666`
    * `flag` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'w'`.
    * `flush` `flush` is `true`, `filehandle.sync()` is used to flush the data. **Default:** `false`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows aborting an in-progress writeFile
  * Returns: `undefined` upon success.


Asynchronously writes data to a file, replacing the file if it already exists. `data` can be a string, a buffer, an
The `encoding` option is ignored if `data` is a buffer.
If `options` is a string, then it specifies the encoding.
The `mode` option only affects the newly created file. See [`fs.open()`](https://nodejs.org/docs/latest/api/fs.html#fsopenpath-flags-mode-callback) for more details.
Any specified [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) has to support writing.
It is unsafe to use `fsPromises.writeFile()` multiple times on the same file without waiting for the promise to be settled.
Similarly to `fsPromises.readFile` - `fsPromises.writeFile` is a convenience method that performs multiple `write` calls internally to write the buffer passed to it. For performance sensitive code consider using [`fs.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options) or [`filehandle.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#filehandlecreatewritestreamoptions).
It is possible to use an [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) to cancel an `fsPromises.writeFile()`. Cancellation is "best effort", and some amount of data is likely still to be written.
```
import { writeFile } from 'node:fs/promises';
import { Buffer } from 'node:buffer';

try {
  const controller = new AbortController();
  const { signal } = controller;
  const data = new Uint8Array(Buffer.from('Hello Node.js'));
  const promise = writeFile('message.txt', data, { signal });

  // Abort the request before the promise settles.
  controller.abort();

  await promise;
} catch (err) {
  // When a request is aborted - err is an AbortError
  console.error(err);
}
copy
```

Aborting an ongoing request does not abort individual operating system requests but rather the internal buffering `fs.writeFile` performs.
####  `fsPromises.constants`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesconstants)
Added in: v18.4.0, v16.17.0
  * Type:


Returns an object containing commonly used constants for file system operations. The object is the same as `fs.constants`. See [FS constants](https://nodejs.org/docs/latest/api/fs.html#fs-constants) for more details.
### Callback API[#](https://nodejs.org/docs/latest/api/fs.html#callback-api)
The callback APIs perform all operations asynchronously, without blocking the event loop, then invoke a callback function upon completion or error.
The callback APIs use the underlying Node.js threadpool to perform file system operations off the event loop thread. These operations are not synchronized or threadsafe. Care must be taken when performing multiple concurrent modifications on the same file or data corruption may occur.
####  `fs.access(path[, mode], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsaccesspath-mode-callback)
Added in: v0.11.15History Version | Changes
---|---
v25.0.0 | The constants `fs.F_OK`, `fs.R_OK`, `fs.W_OK` and `fs.X_OK` which were present directly on `fs` are removed.
v20.8.0 | The constants `fs.F_OK`, `fs.R_OK`, `fs.W_OK` and `fs.X_OK` which were present directly on `fs` are deprecated.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v6.3.0 | The constants like `fs.R_OK`, etc which were present directly on `fs` were moved into `fs.constants` as a soft deprecation. Thus for Node.js `< v6.3.0` use `fs` to access those constants, or do something like `(fs.constants || fs).R_OK` to work with all versions.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `mode` **Default:** `fs.constants.F_OK`
  * `callback`
    * `err`


Tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g. `fs.constants.W_OK | fs.constants.R_OK`). Check [File access constants](https://nodejs.org/docs/latest/api/fs.html#file-access-constants) for possible values of `mode`.
The final argument, `callback`, is a callback function that is invoked with a possible error argument. If any of the accessibility checks fail, the error argument will be an `Error` object. The following examples check if `package.json` exists, and if it is readable or writable.
```
import { access, constants } from 'node:fs';

const file = 'package.json';

// Check if the file exists in the current directory.
access(file, constants.F_OK, (err) => {
  console.log(`${file} ${err ? 'does not exist' : 'exists'}`);
});

// Check if the file is readable.
access(file, constants.R_OK, (err) => {
  console.log(`${file} ${err ? 'is not readable' : 'is readable'}`);
});

// Check if the file is writable.
access(file, constants.W_OK, (err) => {
  console.log(`${file} ${err ? 'is not writable' : 'is writable'}`);
});

// Check if the file is readable and writable.
access(file, constants.R_OK | constants.W_OK, (err) => {
  console.log(`${file} ${err ? 'is not' : 'is'} readable and writable`);
});
copy
```

Do not use `fs.access()` to check for the accessibility of a file before calling `fs.open()`, `fs.readFile()`, or `fs.writeFile()`. Doing so introduces a race condition, since other processes may change the file's state between the two calls. Instead, user code should open/read/write the file directly and handle the error raised if the file is not accessible.
**write (NOT RECOMMENDED)**
```
import { access, open, close } from 'node:fs';

access('myfile', (err) => {
  if (!err) {
    console.error('myfile already exists');
    return;
  }

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
import { access, open, close } from 'node:fs';
access('myfile', (err) => {
  if (err) {
    if (err.code === 'ENOENT') {
      console.error('myfile does not exist');
      return;
    }

    throw err;
  }

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

The "not recommended" examples above check for accessibility and then use the file; the "recommended" examples are better because they use the file directly and handle the error, if any.
In general, check for the accessibility of a file only if the file will not be used directly, for example when its accessibility is a signal from another process.
On Windows, access-control policies (ACLs) on a directory may limit access to a file or directory. The `fs.access()` function, however, does not check the ACL and therefore may report that a path is accessible even if the ACL restricts the user from reading or writing to it.
####  `fs.appendFile(path, data[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsappendfilepath-data-options-callback)
Added in: v0.6.7History Version | Changes
---|---
v21.1.0, v20.10.0 | The `flush` option is now supported.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
v7.0.0 | The passed `options` object will never be modified.
v5.0.0 | The `file` parameter can be a file descriptor now.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) |
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `mode` **Default:** `0o666`
    * `flag` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'a'`.
    * `flush` `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.
  * `callback`
    * `err`


Asynchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer).
The `mode` option only affects the newly created file. See [`fs.open()`](https://nodejs.org/docs/latest/api/fs.html#fsopenpath-flags-mode-callback) for more details.
```
import { appendFile } from 'node:fs';

appendFile('message.txt', 'data to append', (err) => {
  if (err) throw err;
  console.log('The "data to append" was appended to file!');
});
copy
```

If `options` is a string, then it specifies the encoding:
```
import { appendFile } from 'node:fs';

appendFile('message.txt', 'data to append', 'utf8', callback);
copy
```

The `path` may be specified as a numeric file descriptor that has been opened for appending (using `fs.open()` or `fs.openSync()`). The file descriptor will not be closed automatically.
```
import { open, close, appendFile } from 'node:fs';

function closeFd(fd) {
  close(fd, (err) => {
    if (err) throw err;
  });
}

open('message.txt', 'a', (err, fd) => {
  if (err) throw err;

  try {
    appendFile(fd, 'data to append', 'utf8', (err) => {
      closeFd(fd);
      if (err) throw err;
    });
  } catch (err) {
    closeFd(fd);
    throw err;
  }
});
copy
```

####  `fs.chmod(path, mode, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fschmodpath-mode-callback)
Added in: v0.1.30History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `mode`
  * `callback`
    * `err`


Asynchronously changes the permissions of a file. No arguments other than a possible exception are given to the completion callback.
See the POSIX
```
import { chmod } from 'node:fs';

chmod('my_file.txt', 0o775, (err) => {
  if (err) throw err;
  console.log('The permissions for file "my_file.txt" have been changed!');
});
copy
```

##### File modes[#](https://nodejs.org/docs/latest/api/fs.html#file-modes)
The `mode` argument used in both the `fs.chmod()` and `fs.chmodSync()` methods is a numeric bitmask created using a logical OR of the following constants:
Constant | Octal | Description
---|---|---
`fs.constants.S_IRUSR` | `0o400` | read by owner
`fs.constants.S_IWUSR` | `0o200` | write by owner
`fs.constants.S_IXUSR` | `0o100` | execute/search by owner
`fs.constants.S_IRGRP` | `0o40` | read by group
`fs.constants.S_IWGRP` | `0o20` | write by group
`fs.constants.S_IXGRP` | `0o10` | execute/search by group
`fs.constants.S_IROTH` | `0o4` | read by others
`fs.constants.S_IWOTH` | `0o2` | write by others
`fs.constants.S_IXOTH` | `0o1` | execute/search by others
An easier method of constructing the `mode` is to use a sequence of three octal digits (e.g. `765`). The left-most digit (`7` in the example), specifies the permissions for the file owner. The middle digit (`6` in the example), specifies permissions for the group. The right-most digit (`5` in the example), specifies the permissions for others.
Number | Description
---|---
`7` | read, write, and execute
`6` | read and write
`5` | read and execute
`4` | read only
`3` | write and execute
`2` | write only
`1` | execute only
`0` | no permission
For example, the octal value `0o765` means:
  * The owner may read, write, and execute the file.
  * The group may read and write the file.
  * Others may read and execute the file.


When using raw numbers where file modes are expected, any value larger than `0o777` may result in platform-specific behaviors that are not supported to work consistently. Therefore constants like `S_ISVTX`, `S_ISGID`, or `S_ISUID` are not exposed in `fs.constants`.
