See also: [`writable.uncork()`](https://nodejs.org/docs/latest/api/stream.html#writableuncork), [`writable._writev()`](https://nodejs.org/docs/latest/api/stream.html#writable_writevchunks-callback).
######  `writable.destroy([error])`[#](https://nodejs.org/docs/latest/api/stream.html#writabledestroyerror)
Added in: v8.0.0History Version | Changes
---|---
v14.0.0 | Work as a no-op on a stream that has already been destroyed.
  * `error` `'error'` event.
  * Returns:


Destroy the stream. Optionally emit an `'error'` event, and emit a `'close'` event (unless `emitClose` is set to `false`). After this call, the writable stream has ended and subsequent calls to `write()` or `end()` will result in an `ERR_STREAM_DESTROYED` error. This is a destructive and immediate way to destroy a stream. Previous calls to `write()` may not have drained, and may trigger an `ERR_STREAM_DESTROYED` error. Use `end()` instead of destroy if data should flush before close, or wait for the `'drain'` event before destroying the stream.
```
const { Writable } = require('node:stream');

const myStream = new Writable();

const fooErr = new Error('foo error');
myStream.destroy(fooErr);
myStream.on('error', (fooErr) => console.error(fooErr.message)); // foo error
const { Writable } = require('node:stream');

const myStream = new Writable();

myStream.destroy();
myStream.on('error', function wontHappen() {});
copy
```
```
const { Writable } = require('node:stream');

const myStream = new Writable();
myStream.destroy();

myStream.write('foo', (error) => console.error(error.code));
// ERR_STREAM_DESTROYED
copy
```

Once `destroy()` has been called any further calls will be a no-op and no further errors except from `_destroy()` may be emitted as `'error'`.
Implementers should not override this method, but instead implement [`writable._destroy()`](https://nodejs.org/docs/latest/api/stream.html#writable_destroyerr-callback).
######  `writable.closed`[#](https://nodejs.org/docs/latest/api/stream.html#writableclosed)
Added in: v18.0.0
  * Type:


Is `true` after `'close'` has been emitted.
######  `writable.destroyed`[#](https://nodejs.org/docs/latest/api/stream.html#writabledestroyed)
Added in: v8.0.0
  * Type:


Is `true` after [`writable.destroy()`](https://nodejs.org/docs/latest/api/stream.html#writabledestroyerror) has been called.
```
const { Writable } = require('node:stream');

const myStream = new Writable();

console.log(myStream.destroyed); // false
myStream.destroy();
console.log(myStream.destroyed); // true
copy
```

######  `writable.end([chunk[, encoding]][, callback])`[#](https://nodejs.org/docs/latest/api/stream.html#writableendchunk-encoding-callback)
Added in: v0.9.4History Version | Changes
---|---
v22.0.0, v20.13.0 | The `chunk` argument can now be a `TypedArray` or `DataView` instance.
v15.0.0 | The `callback` is invoked before 'finish' or on error.
v14.0.0 | The `callback` is invoked if 'finish' or 'error' is emitted.
v10.0.0 | This method now returns a reference to `writable`.
v8.0.0 | The `chunk` argument can now be a `Uint8Array` instance.
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `chunk` must be a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer), `chunk` may be any JavaScript value other than `null`.
  * `encoding` `chunk` is a string
  * `callback`
  * Returns:


Calling the `writable.end()` method signals that no more data will be written to the [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable). The optional `chunk` and `encoding` arguments allow one final additional chunk of data to be written immediately before closing the stream.
Calling the [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) method after calling [`stream.end()`](https://nodejs.org/docs/latest/api/stream.html#writableendchunk-encoding-callback) will raise an error.
```
// Write 'hello, ' and then end with 'world!'.
const fs = require('node:fs');
const file = fs.createWriteStream('example.txt');
file.write('hello, ');
file.end('world!');
// Writing more now is not allowed!
copy
```

######  `writable.setDefaultEncoding(encoding)`[#](https://nodejs.org/docs/latest/api/stream.html#writablesetdefaultencodingencoding)
Added in: v0.11.15History Version | Changes
---|---
v6.1.0 | This method now returns a reference to `writable`.
  * `encoding`
  * Returns:


The `writable.setDefaultEncoding()` method sets the default `encoding` for a [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) stream.
######  `writable.uncork()`[#](https://nodejs.org/docs/latest/api/stream.html#writableuncork)
Added in: v0.11.2
The `writable.uncork()` method flushes all data buffered since [`stream.cork()`](https://nodejs.org/docs/latest/api/stream.html#writablecork) was called.
When using [`writable.cork()`](https://nodejs.org/docs/latest/api/stream.html#writablecork) and `writable.uncork()` to manage the buffering of writes to a stream, defer calls to `writable.uncork()` using `process.nextTick()`. Doing so allows batching of all `writable.write()` calls that occur within a given Node.js event loop phase.
```
stream.cork();
stream.write('some ');
stream.write('data ');
process.nextTick(() => stream.uncork());
copy
```

If the [`writable.cork()`](https://nodejs.org/docs/latest/api/stream.html#writablecork) method is called multiple times on a stream, the same number of calls to `writable.uncork()` must be called to flush the buffered data.
```
stream.cork();
stream.write('some ');
stream.cork();
stream.write('data ');
process.nextTick(() => {
  stream.uncork();
  // The data will not be flushed until uncork() is called a second time.
  stream.uncork();
});
copy
```

See also: [`writable.cork()`](https://nodejs.org/docs/latest/api/stream.html#writablecork).
######  `writable.writable`[#](https://nodejs.org/docs/latest/api/stream.html#writablewritable)
Added in: v11.4.0
  * Type:


Is `true` if it is safe to call [`writable.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback), which means the stream has not been destroyed, errored, or ended.
######  `writable.writableAborted`[#](https://nodejs.org/docs/latest/api/stream.html#writablewritableaborted)
Added in: v18.0.0, v16.17.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * Type:


Returns whether the stream was destroyed or errored before emitting `'finish'`.
######  `writable.writableEnded`[#](https://nodejs.org/docs/latest/api/stream.html#writablewritableended)
Added in: v12.9.0
  * Type:


Is `true` after [`writable.end()`](https://nodejs.org/docs/latest/api/stream.html#writableendchunk-encoding-callback) has been called. This property does not indicate whether the data has been flushed, for this use [`writable.writableFinished`](https://nodejs.org/docs/latest/api/stream.html#writablewritablefinished) instead.
######  `writable.writableCorked`[#](https://nodejs.org/docs/latest/api/stream.html#writablewritablecorked)
Added in: v13.2.0, v12.16.0
  * Type:


Number of times [`writable.uncork()`](https://nodejs.org/docs/latest/api/stream.html#writableuncork) needs to be called in order to fully uncork the stream.
######  `writable.errored`[#](https://nodejs.org/docs/latest/api/stream.html#writableerrored)
Added in: v18.0.0
  * Type:


Returns error if the stream has been destroyed with an error.
######  `writable.writableFinished`[#](https://nodejs.org/docs/latest/api/stream.html#writablewritablefinished)
Added in: v12.6.0
  * Type:


Is set to `true` immediately before the [`'finish'`](https://nodejs.org/docs/latest/api/stream.html#event-finish) event is emitted.
######  `writable.writableHighWaterMark`[#](https://nodejs.org/docs/latest/api/stream.html#writablewritablehighwatermark)
Added in: v9.3.0
  * Type:


Return the value of `highWaterMark` passed when creating this `Writable`.
######  `writable.writableLength`[#](https://nodejs.org/docs/latest/api/stream.html#writablewritablelength)
Added in: v9.4.0
  * Type:


This property contains the number of bytes (or objects) in the queue ready to be written. The value provides introspection data regarding the status of the `highWaterMark`.
######  `writable.writableNeedDrain`[#](https://nodejs.org/docs/latest/api/stream.html#writablewritableneeddrain)
Added in: v15.2.0, v14.17.0
  * Type:


Is `true` if the stream's buffer has been full and stream will emit `'drain'`.
######  `writable.writableObjectMode`[#](https://nodejs.org/docs/latest/api/stream.html#writablewritableobjectmode)
Added in: v12.3.0
  * Type:


Getter for the property `objectMode` of a given `Writable` stream.
######  `writable[Symbol.asyncDispose]()`[#](https://nodejs.org/docs/latest/api/stream.html#writablesymbolasyncdispose)
Added in: v22.4.0, v20.16.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Calls [`writable.destroy()`](https://nodejs.org/docs/latest/api/stream.html#writabledestroyerror) with an `AbortError` and returns a promise that fulfills when the stream is finished.
######  `writable.write(chunk[, encoding][, callback])`[#](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback)
Added in: v0.9.4History Version | Changes
---|---
v22.0.0, v20.13.0 | The `chunk` argument can now be a `TypedArray` or `DataView` instance.
v8.0.0 | The `chunk` argument can now be a `Uint8Array` instance.
v6.0.0 | Passing `null` as the `chunk` parameter will always be considered invalid now, even in object mode.
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `chunk` must be a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer), `chunk` may be any JavaScript value other than `null`.
  * `encoding` `chunk` is a string. **Default:** `'utf8'`
  * `callback`
  * Returns: `false` if the stream wishes for the calling code to wait for the `'drain'` event to be emitted before continuing to write additional data; otherwise `true`.


The `writable.write()` method writes some data to the stream, and calls the supplied `callback` once the data has been fully handled. If an error occurs, the `callback` will be called with the error as its first argument. The `callback` is called asynchronously and before `'error'` is emitted.
The return value is `true` if the internal buffer is less than the `highWaterMark` configured when the stream was created after admitting `chunk`. If `false` is returned, further attempts to write data to the stream should stop until the [`'drain'`](https://nodejs.org/docs/latest/api/stream.html#event-drain) event is emitted.
While a stream is not draining, calls to `write()` will buffer `chunk`, and return false. Once all currently buffered chunks are drained (accepted for delivery by the operating system), the `'drain'` event will be emitted. Once `write()` returns false, do not write more chunks until the `'drain'` event is emitted. While calling `write()` on a stream that is not draining is allowed, Node.js will buffer all written chunks until maximum memory usage occurs, at which point it will abort unconditionally. Even before it aborts, high memory usage will cause poor garbage collector performance and high RSS (which is not typically released back to the system, even after the memory is no longer required). Since TCP sockets may never drain if the remote peer does not read the data, writing a socket that is not draining may lead to a remotely exploitable vulnerability.
Writing data while the stream is not draining is particularly problematic for a [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform), because the `Transform` streams are paused by default until they are piped or a `'data'` or `'readable'` event handler is added.
If the data to be written can be generated or fetched on demand, it is recommended to encapsulate the logic into a [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) and use [`stream.pipe()`](https://nodejs.org/docs/latest/api/stream.html#readablepipedestination-options). However, if calling `write()` is preferred, it is possible to respect backpressure and avoid memory issues using the [`'drain'`](https://nodejs.org/docs/latest/api/stream.html#event-drain) event:
```
function write(data, cb) {
  if (!stream.write(data)) {
    stream.once('drain', cb);
  } else {
    process.nextTick(cb);
  }
}

// Wait for cb to be called before doing any other write.
write('hello', () => {
  console.log('Write completed, do more writes now.');
});
copy
```

A `Writable` stream in object mode will always ignore the `encoding` argument.
#### Readable streams[#](https://nodejs.org/docs/latest/api/stream.html#readable-streams)
Readable streams are an abstraction for a _source_ from which data is consumed.
Examples of `Readable` streams include:
  * [HTTP responses, on the client](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
  * [HTTP requests, on the server](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage)
  * [fs read streams](https://nodejs.org/docs/latest/api/fs.html#class-fsreadstream)
  * [zlib streams](https://nodejs.org/docs/latest/api/zlib.html)
  * [crypto streams](https://nodejs.org/docs/latest/api/crypto.html)
  * [TCP sockets](https://nodejs.org/docs/latest/api/net.html#class-netsocket)
  * [child process stdout and stderr](https://nodejs.org/docs/latest/api/child_process.html#subprocessstdout)
  * [`process.stdin`](https://nodejs.org/docs/latest/api/process.html#processstdin)


All [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) streams implement the interface defined by the `stream.Readable` class.
##### Two reading modes[#](https://nodejs.org/docs/latest/api/stream.html#two-reading-modes)
`Readable` streams effectively operate in one of two modes: flowing and paused. These modes are separate from [object mode](https://nodejs.org/docs/latest/api/stream.html#object-mode). A [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) stream can be in object mode or not, regardless of whether it is in flowing mode or paused mode.
  * In flowing mode, data is read from the underlying system automatically and provided to an application as quickly as possible using events via the [`EventEmitter`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) interface.
  * In paused mode, the [`stream.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize) method must be called explicitly to read chunks of data from the stream.


All [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) streams begin in paused mode but can be switched to flowing mode in one of the following ways:
  * Adding a [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) event handler.
  * Calling the [`stream.resume()`](https://nodejs.org/docs/latest/api/stream.html#readableresume) method.
  * Calling the [`stream.pipe()`](https://nodejs.org/docs/latest/api/stream.html#readablepipedestination-options) method to send the data to a [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable).


The `Readable` can switch back to paused mode using one of the following:
  * If there are no pipe destinations, by calling the [`stream.pause()`](https://nodejs.org/docs/latest/api/stream.html#readablepause) method.
  * If there are pipe destinations, by removing all pipe destinations. Multiple pipe destinations may be removed by calling the [`stream.unpipe()`](https://nodejs.org/docs/latest/api/stream.html#readableunpipedestination) method.


The important concept to remember is that a `Readable` will not generate data until a mechanism for either consuming or ignoring that data is provided. If the consuming mechanism is disabled or taken away, the `Readable` will _attempt_ to stop generating the data.
For backward compatibility reasons, removing [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) event handlers will **not** automatically pause the stream. Also, if there are piped destinations, then calling [`stream.pause()`](https://nodejs.org/docs/latest/api/stream.html#readablepause) will not guarantee that the stream will _remain_ paused once those destinations drain and ask for more data.
If a [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) is switched into flowing mode and there are no consumers available to handle the data, that data will be lost. This can occur, for instance, when the `readable.resume()` method is called without a listener attached to the `'data'` event, or when a `'data'` event handler is removed from the stream.
Adding a [`'readable'`](https://nodejs.org/docs/latest/api/stream.html#event-readable) event handler automatically makes the stream stop flowing, and the data has to be consumed via [`readable.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize). If the [`'readable'`](https://nodejs.org/docs/latest/api/stream.html#event-readable) event handler is removed, then the stream will start flowing again if there is a [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) event handler.
##### Three states[#](https://nodejs.org/docs/latest/api/stream.html#three-states)
The "two modes" of operation for a `Readable` stream are a simplified abstraction for the more complicated internal state management that is happening within the `Readable` stream implementation.
Specifically, at any given point in time, every `Readable` is in one of three possible states:
  * `readable.readableFlowing === null`
  * `readable.readableFlowing === false`
  * `readable.readableFlowing === true`


When `readable.readableFlowing` is `null`, no mechanism for consuming the stream's data is provided. Therefore, the stream will not generate data. While in this state, attaching a listener for the `'data'` event, calling the `readable.pipe()` method, or calling the `readable.resume()` method will switch `readable.readableFlowing` to `true`, causing the `Readable` to begin actively emitting events as data is generated.
Calling `readable.pause()`, `readable.unpipe()`, or receiving backpressure will cause the `readable.readableFlowing` to be set as `false`, temporarily halting the flowing of events but _not_ halting the generation of data. While in this state, attaching a listener for the `'data'` event will not switch `readable.readableFlowing` to `true`.
```
const { PassThrough, Writable } = require('node:stream');
const pass = new PassThrough();
const writable = new Writable();

pass.pipe(writable);
pass.unpipe(writable);
// readableFlowing is now false.

pass.on('data', (chunk) => { console.log(chunk.toString()); });
// readableFlowing is still false.
pass.write('ok');  // Will not emit 'data'.
pass.resume();     // Must be called to make stream emit 'data'.
// readableFlowing is now true.
copy
```

While `readable.readableFlowing` is `false`, data may be accumulating within the stream's internal buffer.
##### Choose one API style[#](https://nodejs.org/docs/latest/api/stream.html#choose-one-api-style)
The `Readable` stream API evolved across multiple Node.js versions and provides multiple methods of consuming stream data. In general, developers should choose _one_ of the methods of consuming data and _should never_ use multiple methods to consume data from a single stream. Specifically, using a combination of `on('data')`, `on('readable')`, `pipe()`, or async iterators could lead to unintuitive behavior.
##### Class: `stream.Readable`[#](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable)
Added in: v0.9.4
###### Event: `'close'`[#](https://nodejs.org/docs/latest/api/stream.html#event-close-1)
Added in: v0.9.4History Version | Changes
---|---
v10.0.0 | Add `emitClose` option to specify if `'close'` is emitted on destroy.
The `'close'` event is emitted when the stream and any of its underlying resources (a file descriptor, for example) have been closed. The event indicates that no more events will be emitted, and no further computation will occur.
A [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) stream will always emit the `'close'` event if it is created with the `emitClose` option.
###### Event: `'data'`[#](https://nodejs.org/docs/latest/api/stream.html#event-data)
Added in: v0.9.4
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer`. For streams that are in object mode, the chunk can be any JavaScript value other than `null`.


The `'data'` event is emitted whenever the stream is relinquishing ownership of a chunk of data to a consumer. This may occur whenever the stream is switched in flowing mode by calling `readable.pipe()`, `readable.resume()`, or by attaching a listener callback to the `'data'` event. The `'data'` event will also be emitted whenever the `readable.read()` method is called and a chunk of data is available to be returned.
Attaching a `'data'` event listener to a stream that has not been explicitly paused will switch the stream into flowing mode. Data will then be passed as soon as it is available.
The listener callback will be passed the chunk of data as a string if a default encoding has been specified for the stream using the `readable.setEncoding()` method; otherwise the data will be passed as a `Buffer`.
```
const readable = getReadableStreamSomehow();
readable.on('data', (chunk) => {
  console.log(`Received ${chunk.length} bytes of data.`);
});
copy
```

###### Event: `'end'`[#](https://nodejs.org/docs/latest/api/stream.html#event-end)
Added in: v0.9.4
The `'end'` event is emitted when there is no more data to be consumed from the stream.
The `'end'` event **will not be emitted** unless the data is completely consumed. This can be accomplished by switching the stream into flowing mode, or by calling [`stream.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize) repeatedly until all data has been consumed.
```
const readable = getReadableStreamSomehow();
readable.on('data', (chunk) => {
  console.log(`Received ${chunk.length} bytes of data.`);
});
readable.on('end', () => {
  console.log('There will be no more data.');
});
copy
```

###### Event: `'error'`[#](https://nodejs.org/docs/latest/api/stream.html#event-error-1)
Added in: v0.9.4
  * Type:


The `'error'` event may be emitted by a `Readable` implementation at any time. Typically, this may occur if the underlying stream is unable to generate data due to an underlying internal failure, or when a stream implementation attempts to push an invalid chunk of data.
The listener callback will be passed a single `Error` object.
###### Event: `'pause'`[#](https://nodejs.org/docs/latest/api/stream.html#event-pause)
Added in: v0.9.4
The `'pause'` event is emitted when [`stream.pause()`](https://nodejs.org/docs/latest/api/stream.html#readablepause) is called and `readableFlowing` is not `false`.
###### Event: `'readable'`[#](https://nodejs.org/docs/latest/api/stream.html#event-readable)
Added in: v0.9.4History Version | Changes
---|---
v10.0.0 | The `'readable'` is always emitted in the next tick after `.push()` is called.
v10.0.0 | Using `'readable'` requires calling `.read()`.
The `'readable'` event is emitted when there is data available to be read from the stream, up to the configured high water mark (`state.highWaterMark`). Effectively, it indicates that the stream has new information within the buffer. If data is available within this buffer, [`stream.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize) can be called to retrieve that data. Additionally, the `'readable'` event may also be emitted when the end of the stream has been reached.
```
const readable = getReadableStreamSomehow();
readable.on('readable', function() {
  // There is some data to read now.
  let data;

  while ((data = this.read()) !== null) {
    console.log(data);
  }
});
copy
```

If the end of the stream has been reached, calling [`stream.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize) will return `null` and trigger the `'end'` event. This is also true if there never was any data to be read. For instance, in the following example, `foo.txt` is an empty file:
```
const fs = require('node:fs');
const rr = fs.createReadStream('foo.txt');
rr.on('readable', () => {
  console.log(`readable: ${rr.read()}`);
});
rr.on('end', () => {
  console.log('end');
});
copy
```

The output of running this script is:
```
$ node test.js
readable: null
end
copy
```

In some cases, attaching a listener for the `'readable'` event will cause some amount of data to be read into an internal buffer.
In general, the `readable.pipe()` and `'data'` event mechanisms are easier to understand than the `'readable'` event. However, handling `'readable'` might result in increased throughput.
If both `'readable'` and [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) are used at the same time, `'readable'` takes precedence in controlling the flow, i.e. `'data'` will be emitted only when [`stream.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize) is called. The `readableFlowing` property would become `false`. If there are `'data'` listeners when `'readable'` is removed, the stream will start flowing, i.e. `'data'` events will be emitted without calling `.resume()`.
