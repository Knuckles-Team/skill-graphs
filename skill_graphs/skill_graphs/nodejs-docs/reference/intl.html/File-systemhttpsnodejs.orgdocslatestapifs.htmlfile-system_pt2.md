

Write an array of
The promise is fulfilled with an object containing a two properties:
  * `bytesWritten`
  * `buffers` [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `buffers` input.


It is unsafe to call `writev()` multiple times on the same file without waiting for the promise to be fulfilled (or rejected).
On Linux, positional writes don't work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.
#####  `filehandle[Symbol.asyncDispose]()`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlesymbolasyncdispose)
Added in: v20.4.0, v18.18.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Calls `filehandle.close()` and returns a promise that fulfills when the filehandle is closed.
####  `fsPromises.access(path[, mode])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesaccesspath-mode)
Added in: v10.0.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `mode` **Default:** `fs.constants.F_OK`
  * Returns: `undefined` upon success.


Tests a user's permissions for the file or directory specified by `path`. The `mode` argument is an optional integer that specifies the accessibility checks to be performed. `mode` should be either the value `fs.constants.F_OK` or a mask consisting of the bitwise OR of any of `fs.constants.R_OK`, `fs.constants.W_OK`, and `fs.constants.X_OK` (e.g. `fs.constants.W_OK | fs.constants.R_OK`). Check [File access constants](https://nodejs.org/docs/latest/api/fs.html#file-access-constants) for possible values of `mode`.
If the accessibility check is successful, the promise is fulfilled with no value. If any of the accessibility checks fail, the promise is rejected with an `/etc/passwd` can be read and written by the current process.
```
import { access, constants } from 'node:fs/promises';

try {
  await access('/etc/passwd', constants.R_OK | constants.W_OK);
  console.log('can access');
} catch {
  console.error('cannot access');
}
copy
```

Using `fsPromises.access()` to check for the accessibility of a file before calling `fsPromises.open()` is not recommended. Doing so introduces a race condition, since other processes may change the file's state between the two calls. Instead, user code should open/read/write the file directly and handle the error raised if the file is not accessible.
####  `fsPromises.appendFile(path, data[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesappendfilepath-data-options)
Added in: v10.0.0History Version | Changes
---|---
v21.1.0, v20.10.0 | The `flush` option is now supported.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) | [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) filename or [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle)
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `mode` **Default:** `0o666`
    * `flag` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'a'`.
    * `flush` `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.
  * Returns: `undefined` upon success.


Asynchronously append data to a file, creating the file if it does not yet exist. `data` can be a string or a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer).
If `options` is a string, then it specifies the `encoding`.
The `mode` option only affects the newly created file. See [`fs.open()`](https://nodejs.org/docs/latest/api/fs.html#fsopenpath-flags-mode-callback) for more details.
The `path` may be specified as a [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) that has been opened for appending (using `fsPromises.open()`).
####  `fsPromises.chmod(path, mode)`[#](https://nodejs.org/docs/latest/api/fs.html#fspromiseschmodpath-mode)
Added in: v10.0.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `mode`
  * Returns: `undefined` upon success.


Changes the permissions of a file.
####  `fsPromises.chown(path, uid, gid)`[#](https://nodejs.org/docs/latest/api/fs.html#fspromiseschownpath-uid-gid)
Added in: v10.0.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `uid`
  * `gid`
  * Returns: `undefined` upon success.


Changes the ownership of a file.
####  `fsPromises.copyFile(src, dest[, mode])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisescopyfilesrc-dest-mode)
Added in: v10.0.0History Version | Changes
---|---
v14.0.0 | Changed `flags` argument to `mode` and imposed stricter type validation.
  * `src` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) source filename to copy
  * `dest` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) destination filename of the copy operation
  * `mode` `fs.constants.COPYFILE_EXCL | fs.constants.COPYFILE_FICLONE`) **Default:** `0`.
    * `fs.constants.COPYFILE_EXCL`: The copy operation will fail if `dest` already exists.
    * `fs.constants.COPYFILE_FICLONE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then a fallback copy mechanism is used.
    * `fs.constants.COPYFILE_FICLONE_FORCE`: The copy operation will attempt to create a copy-on-write reflink. If the platform does not support copy-on-write, then the operation will fail.
  * Returns: `undefined` upon success.


Asynchronously copies `src` to `dest`. By default, `dest` is overwritten if it already exists.
No guarantees are made about the atomicity of the copy operation. If an error occurs after the destination file has been opened for writing, an attempt will be made to remove the destination.
```
import { copyFile, constants } from 'node:fs/promises';

try {
  await copyFile('source.txt', 'destination.txt');
  console.log('source.txt was copied to destination.txt');
} catch {
  console.error('The file could not be copied');
}

// By using COPYFILE_EXCL, the operation will fail if destination.txt exists.
try {
  await copyFile('source.txt', 'destination.txt', constants.COPYFILE_EXCL);
  console.log('source.txt was copied to destination.txt');
} catch {
  console.error('The file could not be copied');
}
copy
```

####  `fsPromises.cp(src, dest[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisescpsrc-dest-options)
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
    * `filter` `true` to copy the item, `false` to ignore it. When ignoring a directory, all of its contents will be skipped as well. Can also return a `Promise` that resolves to `true` or `false` **Default:** `undefined`.
      * `src`
      * `dest`
      * Returns: `boolean` or a `Promise` that fulfils with such value.
    * `force` `errorOnExist` option to change this behavior. **Default:** `true`.
    * `mode` **Default:** `0`. See `mode` flag of [`fsPromises.copyFile()`](https://nodejs.org/docs/latest/api/fs.html#fspromisescopyfilesrc-dest-mode).
    * `preserveTimestamps` `true` timestamps from `src` will be preserved. **Default:** `false`.
    * `recursive` **Default:** `false`
    * `verbatimSymlinks` `true`, path resolution for symlinks will be skipped. **Default:** `false`
  * Returns: `undefined` upon success.


Asynchronously copies the entire directory structure from `src` to `dest`, including subdirectories and files.
When copying a directory to another directory, globs are not supported and behavior is similar to `cp dir1/ dir2/`.
####  `fsPromises.glob(pattern[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesglobpattern-options)
Added in: v22.0.0History Version | Changes
---|---
v24.1.0, v22.17.0 | Add support for `URL` instances for `cwd` option.
v24.0.0, v22.17.0 | Marking the API stable.
v23.7.0, v22.14.0 | Add support for `exclude` option to accept glob patterns.
v22.2.0 | Add support for `withFileTypes` as an option.
  * `pattern`
  * `options`
    * `cwd` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) current working directory. **Default:** `process.cwd()`
    * `exclude` `true` to exclude the item, `false` to include it. **Default:** `undefined`. If a string array is provided, each string should be a glob pattern that specifies paths to exclude. Note: Negation patterns (e.g., '!foo.js') are not supported.
    * `withFileTypes` `true` if the glob should return paths as Dirents, `false` otherwise. **Default:** `false`.
  * Returns:

```
import { glob } from 'node:fs/promises';

for await (const entry of glob('**/*.js'))
  console.log(entry);
const { glob } = require('node:fs/promises');

(async () => {
  for await (const entry of glob('**/*.js'))
    console.log(entry);
})();
copy
```

####  `fsPromises.lchmod(path, mode)`[#](https://nodejs.org/docs/latest/api/fs.html#fspromiseslchmodpath-mode)
Deprecated in: v10.0.0
Stability: 0 - Deprecated
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `mode`
  * Returns: `undefined` upon success.


Changes the permissions on a symbolic link.
This method is only implemented on macOS.
####  `fsPromises.lchown(path, uid, gid)`[#](https://nodejs.org/docs/latest/api/fs.html#fspromiseslchownpath-uid-gid)
Added in: v10.0.0History Version | Changes
---|---
v10.6.0 | This API is no longer deprecated.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `uid`
  * `gid`
  * Returns: `undefined` upon success.


Changes the ownership on a symbolic link.
####  `fsPromises.lutimes(path, atime, mtime)`[#](https://nodejs.org/docs/latest/api/fs.html#fspromiseslutimespath-atime-mtime)
Added in: v14.5.0, v12.19.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `atime`
  * `mtime`
  * Returns: `undefined` upon success.


Changes the access and modification times of a file in the same way as [`fsPromises.utimes()`](https://nodejs.org/docs/latest/api/fs.html#fspromisesutimespath-atime-mtime), with the difference that if the path refers to a symbolic link, then the link is not dereferenced: instead, the timestamps of the symbolic link itself are changed.
####  `fsPromises.link(existingPath, newPath)`[#](https://nodejs.org/docs/latest/api/fs.html#fspromiseslinkexistingpath-newpath)
Added in: v10.0.0
  * `existingPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `newPath` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * Returns: `undefined` upon success.


Creates a new link from the `existingPath` to the `newPath`. See the POSIX
####  `fsPromises.lstat(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromiseslstatpath-options)
Added in: v10.0.0History Version | Changes
---|---
v10.5.0 | Accepts an additional `options` object to specify whether the numeric values returned should be bigint.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `bigint` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object should be `bigint`. **Default:** `false`.
  * Returns: [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object for the given symbolic link `path`.


Equivalent to [`fsPromises.stat()`](https://nodejs.org/docs/latest/api/fs.html#fspromisesstatpath-options) unless `path` refers to a symbolic link, in which case the link itself is stat-ed, not the file that it refers to. Refer to the POSIX
####  `fsPromises.mkdir(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesmkdirpath-options)
Added in: v10.0.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `recursive` **Default:** `false`
    * `mode` [File modes](https://nodejs.org/docs/latest/api/fs.html#file-modes) for more details. **Default:** `0o777`.
  * Returns: `undefined` if `recursive` is `false`, or the first directory path created if `recursive` is `true`.


Asynchronously creates a directory.
The optional `options` argument can be an integer specifying `mode` (permission and sticky bits), or an object with a `mode` property and a `recursive` property indicating whether parent directories should be created. Calling `fsPromises.mkdir()` when `path` is a directory that exists results in a rejection only when `recursive` is false.
```
import { mkdir } from 'node:fs/promises';

try {
  const projectFolder = new URL('./test/project/', import.meta.url);
  const createDir = await mkdir(projectFolder, { recursive: true });

  console.log(`created ${createDir}`);
} catch (err) {
  console.error(err.message);
}
const { mkdir } = require('node:fs/promises');
const { join } = require('node:path');

async function makeDirectory() {
  const projectFolder = join(__dirname, 'test', 'project');
  const dirCreation = await mkdir(projectFolder, { recursive: true });

  console.log(dirCreation);
  return dirCreation;
}

makeDirectory().catch(console.error);
copy
```

####  `fsPromises.mkdtemp(prefix[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesmkdtempprefix-options)
Added in: v10.0.0History Version | Changes
---|---
v20.6.0, v18.19.0 | The `prefix` parameter now accepts buffers and URL.
v16.5.0, v14.18.0 | The `prefix` parameter now accepts an empty string.
  * `prefix` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * Returns:


Creates a unique temporary directory. A unique directory name is generated by appending six random characters to the end of the provided `prefix`. Due to platform inconsistencies, avoid trailing `X` characters in `prefix`. Some platforms, notably the BSDs, can return more than six random characters, and replace trailing `X` characters in `prefix` with random characters.
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.
```
import { mkdtemp } from 'node:fs/promises';
import { join } from 'node:path';
import { tmpdir } from 'node:os';

try {
  await mkdtemp(join(tmpdir(), 'foo-'));
} catch (err) {
  console.error(err);
}
copy
```

The `fsPromises.mkdtemp()` method will append the six randomly selected characters directly to the `prefix` string. For instance, given a directory `/tmp`, if the intention is to create a temporary directory _within_ `/tmp`, the `prefix` must end with a trailing platform-specific path separator (`require('node:path').sep`).
####  `fsPromises.mkdtempDisposable(prefix[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesmkdtempdisposableprefix-options)
Added in: v24.4.0
  * `prefix` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * Returns:
    * `path`
    * `remove`
    * `[Symbol.asyncDispose]` `remove`.


The resulting Promise holds an async-disposable object whose `path` property holds the created directory path. When the object is disposed, the directory and its contents will be removed asynchronously if it still exists. If the directory cannot be deleted, disposal will throw an error. The object has an async `remove()` method which will perform the same task.
Both this function and the disposal function on the resulting object are async, so it should be used with `await` + `await using` as in `await using dir = await fsPromises.mkdtempDisposable('prefix')`.
For detailed information, see the documentation of [`fsPromises.mkdtemp()`](https://nodejs.org/docs/latest/api/fs.html#fspromisesmkdtempprefix-options).
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use.
####  `fsPromises.open(path, flags[, mode])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesopenpath-flags-mode)
Added in: v10.0.0History Version | Changes
---|---
v11.1.0 | The `flags` argument is now optional and defaults to `'r'`.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `flags` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'r'`.
  * `mode` [File modes](https://nodejs.org/docs/latest/api/fs.html#file-modes) for more details. **Default:** `0o666` (readable and writable)
  * Returns: [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) object.


Opens a [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle).
Refer to the POSIX
Some characters (`< > : " / \ | ? *`) are reserved under Windows as documented by
####  `fsPromises.opendir(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesopendirpath-options)
Added in: v12.12.0History Version | Changes
---|---
v20.1.0, v18.17.0 | Added `recursive` option.
v13.1.0, v12.16.0 | The `bufferSize` option was introduced.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `bufferSize` **Default:** `32`
    * `recursive` `Dir` will be an **Default:** `false`
  * Returns: [`<fs.Dir>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir).


Asynchronously open a directory for iterative scanning. See the POSIX
Creates an [`<fs.Dir>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdir), which contains all further functions for reading from and cleaning up the directory.
The `encoding` option sets the encoding for the `path` while opening the directory and subsequent read operations.
Example using async iteration:
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
####  `fsPromises.readdir(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesreaddirpath-options)
Added in: v10.0.0History Version | Changes
---|---
v20.1.0, v18.17.0 | Added `recursive` option.
v10.11.0 | New option `withFileTypes` was added.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `withFileTypes` **Default:** `false`
    * `recursive` `true`, reads the contents of a directory recursively. In recursive mode, it will list all files, sub files, and directories. **Default:** `false`.
  * Returns: `'.'` and `'..'`.


Reads the contents of a directory.
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the filenames. If the `encoding` is set to `'buffer'`, the filenames returned will be passed as [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) objects.
If `options.withFileTypes` is set to `true`, the returned array will contain [`<fs.Dirent>`](https://nodejs.org/docs/latest/api/fs.html#class-fsdirent) objects.
```
import { readdir } from 'node:fs/promises';

try {
  const files = await readdir(path);
  for (const file of files)
    console.log(file);
} catch (err) {
  console.error(err);
}
copy
```

####  `fsPromises.readFile(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesreadfilepath-options)
Added in: v10.0.0History Version | Changes
---|---
v15.2.0, v14.17.0 | The options argument may include an AbortSignal to abort an ongoing readFile request.
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) | [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) filename or `FileHandle`
  * `options`
    * `encoding` **Default:** `null`
    * `flag` [support of file system `flags`](https://nodejs.org/docs/latest/api/fs.html#file-system-flags). **Default:** `'r'`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows aborting an in-progress readFile
  * Returns:


Asynchronously reads the entire contents of a file.
If no encoding is specified (using `options.encoding`), the data is returned as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) object. Otherwise, the data will be a string.
If `options` is a string, then it specifies the encoding.
When the `path` is a directory, the behavior of `fsPromises.readFile()` is platform-specific. On macOS, Linux, and Windows, the promise will be rejected with an error. On FreeBSD, a representation of the directory's contents will be returned.
An example of reading a `package.json` file located in the same directory of the running code:
```
import { readFile } from 'node:fs/promises';
try {
  const filePath = new URL('./package.json', import.meta.url);
  const contents = await readFile(filePath, { encoding: 'utf8' });
  console.log(contents);
} catch (err) {
  console.error(err.message);
}
const { readFile } = require('node:fs/promises');
const { resolve } = require('node:path');
async function logFile() {
  try {
    const filePath = resolve('./package.json');
    const contents = await readFile(filePath, { encoding: 'utf8' });
    console.log(contents);
  } catch (err) {
    console.error(err.message);
  }
}
logFile();
copy
```

It is possible to abort an ongoing `readFile` using an [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal). If a request is aborted the promise returned is rejected with an `AbortError`:
```
import { readFile } from 'node:fs/promises';

try {
  const controller = new AbortController();
  const { signal } = controller;
  const promise = readFile(fileName, { signal });

  // Abort the request before the promise settles.
  controller.abort();

  await promise;
} catch (err) {
  // When a request is aborted - err is an AbortError
  console.error(err);
}
copy
```

Aborting an ongoing request does not abort individual operating system requests but rather the internal buffering `fs.readFile` performs.
Any specified [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) has to support reading.
####  `fsPromises.readlink(path[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#fspromisesreadlinkpath-options)
Added in: v10.0.0
  * `path` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
  * `options`
    * `encoding` **Default:** `'utf8'`
  * Returns: `linkString` upon success.


Reads the contents of the symbolic link referred to by `path`. See the POSIX `linkString` upon success.
The optional `options` argument can be a string specifying an encoding, or an object with an `encoding` property specifying the character encoding to use for the link path returned. If the `encoding` is set to `'buffer'`, the link path returned will be passed as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) object.
