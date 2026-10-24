    * `withFileTypes` `true` if the glob should return paths as Dirents, `false` otherwise. **Default:** `false`.
  * `callback`
    * `err`
  * Retrieves the files matching the specified pattern.

```
import { glob } from 'node:fs';

glob('**/*.js', (err, matches) => {
  if (err) throw err;
  console.log(matches);
});
const { glob } = require('node:fs');

glob('**/*.js', (err, matches) => {
  if (err) throw err;
  console.log(matches);
});
copy
```

####  `fs.lchmod(path, mode, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fslchmodpath-mode-callback)
Deprecated in: v0.4.7History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v16.0.0 | The error returned may be an `AggregateError` if more than one error is returned.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
Stability: 0 - Deprecated
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `mode`
  * `callback`
    * `err`


Changes the permissions on a symbolic link. No arguments other than a possible exception are given to the completion callback.
This method is only implemented on macOS.
See the POSIX
####  `fs.lchown(path, uid, gid, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fslchownpath-uid-gid-callback)
History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.6.0 | This API is no longer deprecated.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
v0.4.7 | Documentation-only deprecation.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `uid`
  * `gid`
  * `callback`
    * `err`


Set the owner of the symbolic link. No arguments other than a possible exception are given to the completion callback.
See the POSIX
####  `fs.lutimes(path, atime, mtime, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fslutimespath-atime-mtime-callback)
Added in: v14.5.0, v12.19.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `atime`
  * `mtime`
  * `callback`
    * `err`


Changes the access and modification times of a file in the same way as [`fs.utimes()`](https://nodejs.org/docs/latest/api/fs.html#fsutimespath-atime-mtime-callback), with the difference that if the path refers to a symbolic link, then the link is not dereferenced: instead, the timestamps of the symbolic link itself are changed.
No arguments other than a possible exception are given to the completion callback.
####  `fs.link(existingPath, newPath, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fslinkexistingpath-newpath-callback)
Added in: v0.1.31History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `existingPath` and `newPath` parameters can be WHATWG `URL` objects using `file:` protocol. Support is currently still _experimental_.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `existingPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `newPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `callback`
    * `err`


Creates a new link from the `existingPath` to the `newPath`. See the POSIX
####  `fs.lstat(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fslstatpath-options-callback)
Added in: v0.1.30History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.5.0 | Accepts an additional `options` object to specify whether the numeric values returned should be bigint.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `bigint` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object should be `bigint`. **Default:** `false`.
  * `callback`
    * `err`
    * `stats` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats)


Retrieves the [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) for the symbolic link referred to by the path. The callback gets two arguments `(err, stats)` where `stats` is a [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object. `lstat()` is identical to `stat()`, except that if `path` is a symbolic link, then the link itself is stat-ed, not the file that it refers to.
See the POSIX
####  `fs.mkdir(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsmkdirpath-options-callback)
Added in: v0.1.8History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v13.11.0, v12.17.0 | In `recursive` mode, the callback now receives the first created path as an argument.
v10.12.0 | The second argument can now be an `options` object with `recursive` and `mode` properties.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `recursive` **Default:** `false`
    * `mode` [File modes](https://nodejs.org/docs/latest/api/fs.html#file-modes) for more details. **Default:** `0o777`.
  * `callback`
    * `err`
    * `path` `recursive` set to `true`.


Asynchronously creates a directory.
The callback is given a possible exception and, if `recursive` is `true`, the first directory path created, `(err[, path])`. `path` can still be `undefined` when `recursive` is `true`, if no directory was created (for instance, if it was previously created).
The optional `options` argument can be an integer specifying `mode` (permission and sticky bits), or an object with a `mode` property and a `recursive` property indicating whether parent directories should be created. Calling `fs.mkdir()` when `path` is a directory that exists results in an error only when `recursive` is false. If `recursive` is false and the directory exists, an `EEXIST` error occurs.
```
import { mkdir } from 'node:fs';

// Create ./tmp/a/apple, regardless of whether ./tmp and ./tmp/a exist.
mkdir('./tmp/a/apple', { recursive: true }, (err) => {
  if (err) throw err;
});
copy
```

On Windows, using `fs.mkdir()` on the root directory even with recursion will result in an error:
```
import { mkdir } from 'node:fs';

mkdir('/', { recursive: true }, (err) => {
  // => [Error: EPERM: operation not permitted, mkdir 'C:\']
});
copy
```

See the POSIX
####  `fs.mkdtemp(prefix[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsmkdtempprefix-options-callback)
Added in: v5.10.0History Version | Changes
---|---
v20.6.0, v18.19.0 | The `prefix` parameter now accepts buffers and URL.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v16.5.0, v14.18.0 | The `prefix` parameter now accepts an empty string.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
v6.2.1 | The `callback` parameter is optional now.
  * `prefix` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * `callback`
    * `err`
    * `directory`


Creates a unique temporary directory.
Generates six random characters to be appended behind a required `prefix` to create a unique temporary directory. Due to platform inconsistencies, avoid trailing `X` characters in `prefix`. Some platforms, notably the BSDs, can return more than six random characters, and replace trailing `X` characters in `prefix` with random characters.
The created directory path is passed as a string to the callback's second parameter.
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.
```
import { mkdtemp } from 'node:fs';
import { join } from 'node:path';
import { tmpdir } from 'node:os';

mkdtemp(join(tmpdir(), 'foo-'), (err, directory) => {
  if (err) throw err;
  console.log(directory);
  // Prints: /tmp/foo-itXde2 or C:\Users\...\AppData\Local\Temp\foo-itXde2
});
copy
```

The `fs.mkdtemp()` method will append the six randomly selected characters directly to the `prefix` string. For instance, given a directory `/tmp`, if the intention is to create a temporary directory _within_ `/tmp`, the `prefix` must end with a trailing platform-specific path separator (`require('node:path').sep`).
```
import { tmpdir } from 'node:os';
import { mkdtemp } from 'node:fs';

// The parent directory for the new temporary directory
const tmpDir = tmpdir();

// This method is *INCORRECT*:
mkdtemp(tmpDir, (err, directory) => {
  if (err) throw err;
  console.log(directory);
  // Will print something similar to `/tmpabc123`.
  // A new temporary directory is created at the file system root
  // rather than *within* the /tmp directory.
});

// This method is *CORRECT*:
import { sep } from 'node:path';
mkdtemp(`${tmpDir}${sep}`, (err, directory) => {
  if (err) throw err;
  console.log(directory);
  // Will print something similar to `/tmp/abc123`.
  // A new temporary directory is created within
  // the /tmp directory.
});
copy
```

####  `fs.open(path[, flags[, mode]], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsopenpath-flags-mode-callback)
Added in: v0.0.2History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v11.1.0 | The `flags` argument is now optional and defaults to `'r'`.
v9.9.0 | The `as` and `as+` flags are supported now.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `flags` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'r'`.
  * `mode` **Default:** `0o666` (readable and writable)
  * `callback`
    * `err`
    * `fd`


Asynchronous file open. See the POSIX
`mode` sets the file mode (permission and sticky bits), but only if the file was created. On Windows, only the write permission can be manipulated; see [`fs.chmod()`](https://nodejs.org/docs/latest/api/fs.html#fschmodpath-mode-callback).
The callback gets two arguments `(err, fd)`.
Some characters (`< > : " / \ | ? *`) are reserved under Windows as documented by
Functions based on `fs.open()` exhibit this behavior as well: `fs.writeFile()`, `fs.readFile()`, etc.
####  `fs.openAsBlob(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fsopenasblobpath-options)
Added in: v19.8.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `type`
  * Returns: [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) upon success.


Returns a [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) whose data is backed by the given file.
The file must not be modified after the [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) is created. Any modifications will cause reading the [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) data to fail with a `DOMException` error. Synchronous stat operations on the file when the `Blob` is created, and before each read in order to detect whether the file data has been modified on disk.
```
import { openAsBlob } from 'node:fs';

const blob = await openAsBlob('the.file.txt');
const ab = await blob.arrayBuffer();
blob.stream();
const { openAsBlob } = require('node:fs');

(async () => {
  const blob = await openAsBlob('the.file.txt');
  const ab = await blob.arrayBuffer();
  blob.stream();
})();
copy
```

####  `fs.opendir(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsopendirpath-options-callback)
Added in: v12.12.0History Version | Changes
---|---
v20.1.0, v18.17.0 | Added `recursive` option.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v13.1.0, v12.16.0 | The `bufferSize` option was introduced.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `bufferSize` **Default:** `32`
    * `recursive` **Default:** `false`
  * `callback`
    * `err`
    * `dir` [`<fs.Dir>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir)


Asynchronously open a directory. See the POSIX
Creates an [`<fs.Dir>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir), which contains all further functions for reading from and cleaning up the directory.
The `encoding` option sets the encoding for the `path` while opening the directory and subsequent read operations.
####  `fs.read(fd, buffer, offset, length, position, callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadfd-buffer-offset-length-position-callback)
Added in: v0.0.2History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.10.0 | The `buffer` parameter can now be any `TypedArray`, or a `DataView`.
v7.4.0 | The `buffer` parameter can now be a `Uint8Array`.
v6.0.0 | The `length` parameter can now be `0`.
  * `fd`
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `offset` `buffer` to write the data to.
  * `length`
  * `position` `position` is `null` or `-1 `, data will be read from the current file position, and the file position will be updated. If `position` is a non-negative integer, the file position will be unchanged.
  * `callback`
    * `err`
    * `bytesRead`
    * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Read data from the file specified by `fd`.
The callback is given the three arguments, `(err, bytesRead, buffer)`.
If the file is not modified concurrently, the end-of-file is reached when the number of bytes read is zero.
If this method is invoked as its [`util.promisify()`](https://nodejs.org/docs/latest/api/util.html#utilpromisifyoriginal)ed version, it returns a promise for an `Object` with `bytesRead` and `buffer` properties.
The `fs.read()` method reads data from the file specified by the file descriptor (`fd`). The `length` argument indicates the maximum number of bytes that Node.js will attempt to read from the kernel. However, the actual number of bytes read (`bytesRead`) can be lower than the specified `length` for various reasons.
For example:
  * If the file is shorter than the specified `length`, `bytesRead` will be set to the actual number of bytes read.
  * If the file encounters EOF (End of File) before the buffer could be filled, Node.js will read all available bytes until EOF is encountered, and the `bytesRead` parameter in the callback will indicate the actual number of bytes read, which may be less than the specified `length`.
  * If the file is on a slow network `filesystem` or encounters any other issue during reading, `bytesRead` can be lower than the specified `length`.


Therefore, when using `fs.read()`, it's important to check the `bytesRead` value to determine how many bytes were actually read from the file. Depending on your application logic, you may need to handle cases where `bytesRead` is lower than the specified `length`, such as by wrapping the read call in a loop if you require a minimum amount of bytes.
This behavior is similar to the POSIX `preadv2` function.
####  `fs.read(fd[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadfd-options-callback)
Added in: v13.11.0, v12.17.0History Version | Changes
---|---
v13.11.0, v12.17.0 | Options object can be passed in to make buffer, offset, length, and position optional.
  * `fd`
  * `options`
    * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | **Default:** `Buffer.alloc(16384)`
    * `offset` **Default:** `0`
    * `length` **Default:** `buffer.byteLength - offset`
    * `position` **Default:** `null`
  * `callback`
    * `err`
    * `bytesRead`
    * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Similar to the [`fs.read()`](https://nodejs.org/docs/latest/api/fs.html#fsreadfd-buffer-offset-length-position-callback) function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.
####  `fs.read(fd, buffer[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadfd-buffer-options-callback)
Added in: v18.2.0, v16.17.0
  * `fd`
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options`
    * `offset` **Default:** `0`
    * `length` **Default:** `buffer.byteLength - offset`
    * `position` **Default:** `null`
  * `callback`
    * `err`
    * `bytesRead`
    * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Similar to the [`fs.read()`](https://nodejs.org/docs/latest/api/fs.html#fsreadfd-buffer-offset-length-position-callback) function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.
####  `fs.readdir(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsreaddirpath-options-callback)
Added in: v0.1.8History Version | Changes
---|---
v20.1.0, v18.17.0 | Added `recursive` option.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v10.10.0 | New option `withFileTypes` was added.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
v6.0.0 | The `options` parameter was added.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `withFileTypes` **Default:** `false`
    * `recursive` `true`, reads the contents of a directory recursively. In recursive mode, it will list all files, sub files and directories. **Default:** `false`.
  * `callback`
    * `err`
    * `files` [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<fs.Dirent[]>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent)


Reads the contents of a directory. The callback gets two arguments `(err, files)` where `files` is an array of the names of the files in the directory excluding `'.'` and `'..'`.
See the POSIX
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the filenames passed to the callback. If the `encoding` is set to `'buffer'`, the filenames returned will be passed as [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) objects.
If `options.withFileTypes` is set to `true`, the `files` array will contain [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) objects.
####  `fs.readFile(path[, options], callback)`[#](https://nodejs.org/docs/latest/api/fs.html#fsreadfilepath-options-callback)
Added in: v0.1.29History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v16.0.0 | The error returned may be an `AggregateError` if more than one error is returned.
v15.2.0, v14.17.0 | The options argument may include an AbortSignal to abort an ongoing readFile request.
v10.0.0 | The `callback` parameter is no longer optional. Not passing it will throw a `TypeError` at runtime.
v7.6.0 | The `path` parameter can be a WHATWG `URL` object using `file:` protocol.
v7.0.0 | The `callback` parameter is no longer optional. Not passing it will emit a deprecation warning with id DEP0013.
v5.1.0 | The `callback` will always be called with `null` as the `error` parameter in case of success.
v5.0.0 | The `path` parameter can be a file descriptor now.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) |
  * `options`
    * `encoding` **Default:** `null`
    * `flag` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'r'`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows aborting an in-progress readFile
  * `callback`
    * `err`
    * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Asynchronously reads the entire contents of a file.
```
import { readFile } from 'node:fs';

readFile('/etc/passwd', (err, data) => {
  if (err) throw err;
  console.log(data);
});
copy
```

The callback is passed two arguments `(err, data)`, where `data` is the contents of the file.
If no encoding is specified, then the raw buffer is returned.
If `options` is a string, then it specifies the encoding:
```
import { readFile } from 'node:fs';

readFile('/etc/passwd', 'utf8', callback);
copy
```

When the path is a directory, the behavior of `fs.readFile()` and [`fs.readFileSync()`](https://nodejs.org/docs/latest/api/fs.html#fsreadfilesyncpath-options) is platform-specific. On macOS, Linux, and Windows, an error will be returned. On FreeBSD, a representation of the directory's contents will be returned.
```
import { readFile } from 'node:fs';

// macOS, Linux, and Windows
readFile('<directory>', (err, data) => {
  // => [Error: EISDIR: illegal operation on a directory, read <directory>]
});

//  FreeBSD
readFile('<directory>', (err, data) => {
  // => null, <data>
});
copy
```

It is possible to abort an ongoing request using an `AbortSignal`. If a request is aborted the callback is called with an `AbortError`:
```
import { readFile } from 'node:fs';

const controller = new AbortController();
const signal = controller.signal;
readFile(fileInfo[0].name, { signal }, (err, buf) => {
  // ...
});
// When you want to abort the request
controller.abort();
copy
```

The `fs.readFile()` function buffers the entire file. To minimize memory costs, when possible prefer streaming via `fs.createReadStream()`.
Aborting an ongoing request does not abort individual operating system requests but rather the internal buffering `fs.readFile` performs.
##### File descriptors[#](https://nodejs.org/docs/latest/api/fs.html#file-descriptors)
