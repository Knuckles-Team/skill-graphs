## File system[#](https://nodejs.org/docs/latest/api/fs.html#file-system)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:fs` module enables interacting with the file system in a way modeled on standard POSIX functions.
To use the promise-based APIs:
```
import * as fs from 'node:fs/promises';
const fs = require('node:fs/promises');
copy
```

To use the callback and sync APIs:
```
import * as fs from 'node:fs';
const fs = require('node:fs');
copy
```

All file system operations have synchronous, callback, and promise-based forms, and are accessible using both CommonJS syntax and ES6 Modules (ESM).
### Promise example[#](https://nodejs.org/docs/latest/api/fs.html#promise-example)
Promise-based operations return a promise that is fulfilled when the asynchronous operation is complete.
```
import { unlink } from 'node:fs/promises';

try {
  await unlink('/tmp/hello');
  console.log('successfully deleted /tmp/hello');
} catch (error) {
  console.error('there was an error:', error.message);
}
const { unlink } = require('node:fs/promises');

(async function(path) {
  try {
    await unlink(path);
    console.log(`successfully deleted ${path}`);
  } catch (error) {
    console.error('there was an error:', error.message);
  }
})('/tmp/hello');
copy
```

### Callback example[#](https://nodejs.org/docs/latest/api/fs.html#callback-example)
The callback form takes a completion callback function as its last argument and invokes the operation asynchronously. The arguments passed to the completion callback depend on the method, but the first argument is always reserved for an exception. If the operation is completed successfully, then the first argument is `null` or `undefined`.
```
import { unlink } from 'node:fs';

unlink('/tmp/hello', (err) => {
  if (err) throw err;
  console.log('successfully deleted /tmp/hello');
});
const { unlink } = require('node:fs');

unlink('/tmp/hello', (err) => {
  if (err) throw err;
  console.log('successfully deleted /tmp/hello');
});
copy
```

The callback-based versions of the `node:fs` module APIs are preferable over the use of the promise APIs when maximal performance (both in terms of execution time and memory allocation) is required.
### Synchronous example[#](https://nodejs.org/docs/latest/api/fs.html#synchronous-example)
The synchronous APIs block the Node.js event loop and further JavaScript execution until the operation is complete. Exceptions are thrown immediately and can be handled using `try…catch`, or can be allowed to bubble up.
```
import { unlinkSync } from 'node:fs';

try {
  unlinkSync('/tmp/hello');
  console.log('successfully deleted /tmp/hello');
} catch (err) {
  // handle the error
}
const { unlinkSync } = require('node:fs');

try {
  unlinkSync('/tmp/hello');
  console.log('successfully deleted /tmp/hello');
} catch (err) {
  // handle the error
}
copy
```

### Promises API[#](https://nodejs.org/docs/latest/api/fs.html#promises-api)
Added in: v10.0.0History Version | Changes
---|---
v14.0.0 | Exposed as `require('fs/promises')`.
v11.14.0, v10.17.0 | This API is no longer experimental.
v10.1.0 | The API is accessible via `require('fs').promises` only.
The `fs/promises` API provides asynchronous file system methods that return promises.
The promise APIs use the underlying Node.js threadpool to perform file system operations off the event loop thread. These operations are not synchronized or threadsafe. Care must be taken when performing multiple concurrent modifications on the same file or data corruption may occur.
#### Class: `FileHandle`[#](https://nodejs.org/docs/latest/api/fs.html#class-filehandle)
Added in: v10.0.0
A [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) object is an object wrapper for a numeric file descriptor.
Instances of the [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) object are created by the `fsPromises.open()` method.
All [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) objects are [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)s.
If a [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) is not closed using the `filehandle.close()` method, it will try to automatically close the file descriptor and emit a process warning, helping to prevent memory leaks. Please do not rely on this behavior because it can be unreliable and the file may not be closed. Instead, always explicitly close [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle)s. Node.js may change this behavior in the future.
##### Event: `'close'`[#](https://nodejs.org/docs/latest/api/fs.html#event-close)
Added in: v15.4.0
The `'close'` event is emitted when the [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) has been closed and can no longer be used.
#####  `filehandle.appendFile(data[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandleappendfiledata-options)
Added in: v10.0.0History Version | Changes
---|---
v21.1.0, v20.10.0 | The `flush` option is now supported.
v15.14.0, v14.18.0 | The `data` argument supports `AsyncIterable`, `Iterable`, and `Stream`.
v14.0.0 | The `data` parameter won't coerce unsupported input to strings anymore.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream)
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) | **Default:** `undefined`
  * Returns: `undefined` upon success.


Alias of [`filehandle.writeFile()`](https://nodejs.org/docs/latest/api/fs.html#filehandlewritefiledata-options).
When operating on file handles, the mode cannot be changed from what it was set to with [`fsPromises.open()`](https://nodejs.org/docs/latest/api/fs.html#fspromisesopenpath-flags-mode). Therefore, this is equivalent to [`filehandle.writeFile()`](https://nodejs.org/docs/latest/api/fs.html#filehandlewritefiledata-options).
#####  `filehandle.chmod(mode)`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlechmodmode)
Added in: v10.0.0
  * `mode`
  * Returns: `undefined` upon success.


Modifies the permissions on the file. See
#####  `filehandle.chown(uid, gid)`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlechownuid-gid)
Added in: v10.0.0
  * `uid`
  * `gid`
  * Returns: `undefined` upon success.


Changes the ownership of the file. A wrapper for
#####  `filehandle.close()`[#](https://nodejs.org/docs/latest/api/fs.html#filehandleclose)
Added in: v10.0.0
  * Returns: `undefined` upon success.


Closes the file handle after waiting for any pending operation on the handle to complete.
```
import { open } from 'node:fs/promises';

let filehandle;
try {
  filehandle = await open('thefile.txt', 'r');
} finally {
  await filehandle?.close();
}
copy
```

#####  `filehandle.createReadStream([options])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlecreatereadstreamoptions)
Added in: v16.11.0
  * `options`
    * `encoding` **Default:** `null`
    * `autoClose` **Default:** `true`
    * `emitClose` **Default:** `true`
    * `start`
    * `end` **Default:** `Infinity`
    * `highWaterMark` **Default:** `64 * 1024`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) | **Default:** `undefined`
  * Returns: [`<fs.ReadStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream)


`options` can include `start` and `end` values to read a range of bytes from the file instead of the entire file. Both `start` and `end` are inclusive and start counting at 0, allowed values are in the [0, `start` is omitted or `undefined`, `filehandle.createReadStream()` reads sequentially from the current file position. The `encoding` can be any one of those accepted by [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer).
If the `FileHandle` points to a character device that only supports blocking reads (such as keyboard or sound card), read operations do not finish until data is available. This can prevent the process from exiting and the stream from closing naturally.
By default, the stream will emit a `'close'` event after it has been destroyed. Set the `emitClose` option to `false` to change this behavior.
```
import { open } from 'node:fs/promises';

const fd = await open('/dev/input/event0');
// Create a stream from some character device.
const stream = fd.createReadStream();
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
An example to read the last 10 bytes of a file which is 100 bytes long:
```
import { open } from 'node:fs/promises';

const fd = await open('sample.txt');
fd.createReadStream({ start: 90, end: 99 });
copy
```

#####  `filehandle.createWriteStream([options])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlecreatewritestreamoptions)
Added in: v16.11.0History Version | Changes
---|---
v21.0.0, v20.10.0 | The `flush` option is now supported.
  * `options`
    * `encoding` **Default:** `'utf8'`
    * `autoClose` **Default:** `true`
    * `emitClose` **Default:** `true`
    * `start`
    * `highWaterMark` **Default:** `16384`
    * `flush` `true`, the underlying file descriptor is flushed prior to closing it. **Default:** `false`.
  * Returns: [`<fs.WriteStream>`](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream)


`options` may also include a `start` option to allow writing data at some position past the beginning of the file, allowed values are in the [0, `flags` `open` option to be set to `r+` rather than the default `r`. The `encoding` can be any one of those accepted by [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer).
If `autoClose` is set to true (default behavior) on `'error'` or `'finish'` the file descriptor will be closed automatically. If `autoClose` is false, then the file descriptor won't be closed, even if there's an error. It is the application's responsibility to close it and make sure there's no file descriptor leak.
By default, the stream will emit a `'close'` event after it has been destroyed. Set the `emitClose` option to `false` to change this behavior.
#####  `filehandle.datasync()`[#](https://nodejs.org/docs/latest/api/fs.html#filehandledatasync)
Added in: v10.0.0
  * Returns: `undefined` upon success.


Forces all currently queued I/O operations associated with the file to the operating system's synchronized I/O completion state. Refer to the POSIX
Unlike `filehandle.sync` this method does not flush modified metadata.
#####  `filehandle.fd`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlefd)
Added in: v10.0.0
  * Type: [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) object.


#####  `filehandle.read(buffer, offset, length, position)`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlereadbuffer-offset-length-position)
Added in: v10.0.0History Version | Changes
---|---
v21.0.0 | Accepts bigint values as `position`.
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `offset` **Default:** `0`
  * `length` **Default:** `buffer.byteLength - offset`
  * `position` `null` or `-1`, data will be read from the current file position, and the position will be updated. If `position` is a non-negative integer, the current file position will remain unchanged. **Default:** `null`
  * Returns:
    * `bytesRead`
    * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `buffer` argument.


Reads data from the file and stores that in the given buffer.
If the file is not modified concurrently, the end-of-file is reached when the number of bytes read is zero.
#####  `filehandle.read([options])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlereadoptions)
Added in: v13.11.0, v12.17.0History Version | Changes
---|---
v21.0.0 | Accepts bigint values as `position`.
  * `options`
    * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | **Default:** `Buffer.alloc(16384)`
    * `offset` **Default:** `0`
    * `length` **Default:** `buffer.byteLength - offset`
    * `position` `null` or `-1`, data will be read from the current file position, and the position will be updated. If `position` is a non-negative integer, the current file position will remain unchanged. **Default:** : `null`
  * Returns:
    * `bytesRead`
    * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `buffer` argument.


Reads data from the file and stores that in the given buffer.
If the file is not modified concurrently, the end-of-file is reached when the number of bytes read is zero.
#####  `filehandle.read(buffer[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlereadbuffer-options)
Added in: v18.2.0, v16.17.0History Version | Changes
---|---
v21.0.0 | Accepts bigint values as `position`.
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options`
    * `offset` **Default:** `0`
    * `length` **Default:** `buffer.byteLength - offset`
    * `position` `null` or `-1`, data will be read from the current file position, and the position will be updated. If `position` is a non-negative integer, the current file position will remain unchanged. **Default:** : `null`
  * Returns:
    * `bytesRead`
    * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `buffer` argument.


Reads data from the file and stores that in the given buffer.
If the file is not modified concurrently, the end-of-file is reached when the number of bytes read is zero.
#####  `filehandle.readableWebStream([options])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlereadablewebstreamoptions)
Added in: v17.0.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
v23.8.0, v22.15.0 | Removed option to create a 'bytes' stream. Streams are now always 'bytes' streams.
v20.0.0, v18.17.0 | Added option to create a 'bytes' stream.
  * `options`
    * `autoClose` [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) to be closed when the stream is closed. **Default:** `false`
  * Returns: [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream)


Returns a byte-oriented `ReadableStream` that may be used to read the file's contents.
An error will be thrown if this method is called more than once or is called after the `FileHandle` is closed or closing.
```
import {
  open,
} from 'node:fs/promises';

const file = await open('./some/file/to/read');

for await (const chunk of file.readableWebStream())
  console.log(chunk);

await file.close();
const {
  open,
} = require('node:fs/promises');

(async () => {
  const file = await open('./some/file/to/read');

  for await (const chunk of file.readableWebStream())
    console.log(chunk);

  await file.close();
})();
copy
```

While the `ReadableStream` will read the file to completion, it will not close the `FileHandle` automatically. User code must still call the `fileHandle.close()` method unless the `autoClose` option is set to `true`.
#####  `filehandle.readFile(options)`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlereadfileoptions)
Added in: v10.0.0
  * `options`
    * `encoding` **Default:** `null`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows aborting an in-progress readFile
  * Returns: `options.encoding`), the data is returned as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) object. Otherwise, the data will be a string.


Asynchronously reads the entire contents of a file.
If `options` is a string, then it specifies the `encoding`.
The [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) has to support reading.
If one or more `filehandle.read()` calls are made on a file handle and then a `filehandle.readFile()` call is made, the data will be read from the current position till the end of the file. It doesn't always read from the beginning of the file.
#####  `filehandle.readLines([options])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlereadlinesoptions)
Added in: v18.11.0
  * `options`
    * `encoding` **Default:** `null`
    * `autoClose` **Default:** `true`
    * `emitClose` **Default:** `true`
    * `start`
    * `end` **Default:** `Infinity`
    * `highWaterMark` **Default:** `64 * 1024`
  * Returns: [`<readline.InterfaceConstructor>`](https://nodejs.org/docs/latest/api/readline.html#class-readlineinterfaceconstructor)


Convenience method to create a `readline` interface and stream over the file. See [`filehandle.createReadStream()`](https://nodejs.org/docs/latest/api/fs.html#filehandlecreatereadstreamoptions) for the options.
```
import { open } from 'node:fs/promises';

const file = await open('./some/file/to/read');

for await (const line of file.readLines()) {
  console.log(line);
}
const { open } = require('node:fs/promises');

(async () => {
  const file = await open('./some/file/to/read');

  for await (const line of file.readLines()) {
    console.log(line);
  }
})();
copy
```

#####  `filehandle.readv(buffers[, position])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlereadvbuffers-position)
Added in: v13.13.0, v12.17.0
  * `buffers` [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `position` `position` is not a `number`, the data will be read from the current position. **Default:** `null`
  * Returns:
    * `bytesRead`
    * `buffers` [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `buffers` input.


Read from a file and write to an array of
#####  `filehandle.stat([options])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlestatoptions)
Added in: v10.0.0History Version | Changes
---|---
v10.5.0 | Accepts an additional `options` object to specify whether the numeric values returned should be bigint.
  * `options`
    * `bigint` [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) object should be `bigint`. **Default:** `false`.
  * Returns: [`<fs.Stats>`](https://nodejs.org/docs/latest/api/fs.html#class-fsstats) for the file.


#####  `filehandle.sync()`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlesync)
Added in: v10.0.0
  * Returns: `undefined` upon success.


Request that all data for the open file descriptor is flushed to the storage device. The specific implementation is operating system and device specific. Refer to the POSIX
#####  `filehandle.truncate(len)`[#](https://nodejs.org/docs/latest/api/fs.html#filehandletruncatelen)
Added in: v10.0.0
  * `len` **Default:** `0`
  * Returns: `undefined` upon success.


Truncates the file.
If the file was larger than `len` bytes, only the first `len` bytes will be retained in the file.
The following example retains only the first four bytes of the file:
```
import { open } from 'node:fs/promises';

let filehandle = null;
try {
  filehandle = await open('temp.txt', 'r+');
  await filehandle.truncate(4);
} finally {
  await filehandle?.close();
}
copy
```

If the file previously was shorter than `len` bytes, it is extended, and the extended part is filled with null bytes (`'\0'`):
If `len` is negative then `0` will be used.
#####  `filehandle.utimes(atime, mtime)`[#](https://nodejs.org/docs/latest/api/fs.html#filehandleutimesatime-mtime)
Added in: v10.0.0
  * `atime`
  * `mtime`
  * Returns:


Change the file system timestamps of the object referenced by the [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) then fulfills the promise with no arguments upon success.
#####  `filehandle.write(buffer, offset[, length[, position]])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlewritebuffer-offset-length-position)
Added in: v10.0.0History Version | Changes
---|---
v14.0.0 | The `buffer` parameter won't coerce unsupported input to buffers anymore.
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `offset` `buffer` where the data to write begins.
  * `length` `buffer` to write. **Default:** `buffer.byteLength - offset`
  * `position` `buffer` should be written. If `position` is not a `number`, the data will be written at the current position. See the POSIX **Default:** `null`
  * Returns:


Write `buffer` to the file.
The promise is fulfilled with an object containing two properties:
  * `bytesWritten`
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `buffer` written.


It is unsafe to use `filehandle.write()` multiple times on the same file without waiting for the promise to be fulfilled (or rejected). For this scenario, use [`filehandle.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#filehandlecreatewritestreamoptions).
On Linux, positional writes do not work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.
#####  `filehandle.write(buffer[, options])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlewritebuffer-options)
Added in: v18.3.0, v16.17.0
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options`
    * `offset` **Default:** `0`
    * `length` **Default:** `buffer.byteLength - offset`
    * `position` **Default:** `null`
  * Returns:


Write `buffer` to the file.
Similar to the above `filehandle.write` function, this version takes an optional `options` object. If no `options` object is specified, it will default with the above values.
#####  `filehandle.write(string[, position[, encoding]])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlewritestring-position-encoding)
Added in: v10.0.0History Version | Changes
---|---
v14.0.0 | The `string` parameter won't coerce unsupported input to strings anymore.
  * `string`
  * `position` `string` should be written. If `position` is not a `number` the data will be written at the current position. See the POSIX **Default:** `null`
  * `encoding` **Default:** `'utf8'`
  * Returns:


Write `string` to the file. If `string` is not a string, the promise is rejected with an error.
The promise is fulfilled with an object containing two properties:
  * `bytesWritten`
  * `buffer` `string` written.


It is unsafe to use `filehandle.write()` multiple times on the same file without waiting for the promise to be fulfilled (or rejected). For this scenario, use [`filehandle.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#filehandlecreatewritestreamoptions).
On Linux, positional writes do not work when the file is opened in append mode. The kernel ignores the position argument and always appends the data to the end of the file.
#####  `filehandle.writeFile(data, options)`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlewritefiledata-options)
Added in: v10.0.0History Version | Changes
---|---
v15.14.0, v14.18.0 | The `data` argument supports `AsyncIterable`, `Iterable`, and `Stream`.
v14.0.0 | The `data` parameter won't coerce unsupported input to strings anymore.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream)
  * `options`
    * `encoding` `data` is a string. **Default:** `'utf8'`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) | **Default:** `undefined`
  * Returns:


Asynchronously writes data to a file, replacing the file if it already exists. `data` can be a string, a buffer, an
If `options` is a string, then it specifies the `encoding`.
The [`<FileHandle>`](https://nodejs.org/docs/latest/api/fs.html#class-filehandle) has to support writing.
It is unsafe to use `filehandle.writeFile()` multiple times on the same file without waiting for the promise to be fulfilled (or rejected).
If one or more `filehandle.write()` calls are made on a file handle and then a `filehandle.writeFile()` call is made, the data will be written from the current position till the end of the file. It doesn't always write from the beginning of the file.
#####  `filehandle.writev(buffers[, position])`[#](https://nodejs.org/docs/latest/api/fs.html#filehandlewritevbuffers-position)
Added in: v12.9.0
  * `buffers` [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `position` `buffers` should be written. If `position` is not a `number`, the data will be written at the current position. **Default:** `null`
  * Returns:
