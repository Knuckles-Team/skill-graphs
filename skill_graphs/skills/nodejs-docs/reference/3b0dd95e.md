###### Event: `'resume'`[#](https://nodejs.org/docs/latest/api/stream.html#event-resume)
Added in: v0.9.4
The `'resume'` event is emitted when [`stream.resume()`](https://nodejs.org/docs/latest/api/stream.html#readableresume) is called and `readableFlowing` is not `true`.
######  `readable.destroy([error])`[#](https://nodejs.org/docs/latest/api/stream.html#readabledestroyerror)
Added in: v8.0.0History Version | Changes
---|---
v14.0.0 | Work as a no-op on a stream that has already been destroyed.
  * `error` `'error'` event
  * Returns:


Destroy the stream. Optionally emit an `'error'` event, and emit a `'close'` event (unless `emitClose` is set to `false`). After this call, the readable stream will release any internal resources and subsequent calls to `push()` will be ignored.
Once `destroy()` has been called any further calls will be a no-op and no further errors except from `_destroy()` may be emitted as `'error'`.
Implementers should not override this method, but instead implement [`readable._destroy()`](https://nodejs.org/docs/latest/api/stream.html#readable_destroyerr-callback).
######  `readable.closed`[#](https://nodejs.org/docs/latest/api/stream.html#readableclosed)
Added in: v18.0.0
  * Type:


Is `true` after `'close'` has been emitted.
######  `readable.destroyed`[#](https://nodejs.org/docs/latest/api/stream.html#readabledestroyed)
Added in: v8.0.0
  * Type:


Is `true` after [`readable.destroy()`](https://nodejs.org/docs/latest/api/stream.html#readabledestroyerror) has been called.
######  `readable.isPaused()`[#](https://nodejs.org/docs/latest/api/stream.html#readableispaused)
Added in: v0.11.14
  * Returns:


The `readable.isPaused()` method returns the current operating state of the `Readable`. This is used primarily by the mechanism that underlies the `readable.pipe()` method. In most typical cases, there will be no reason to use this method directly.
```
const readable = new stream.Readable();

readable.isPaused(); // === false
readable.pause();
readable.isPaused(); // === true
readable.resume();
readable.isPaused(); // === false
copy
```

######  `readable.pause()`[#](https://nodejs.org/docs/latest/api/stream.html#readablepause)
Added in: v0.9.4
  * Returns:


The `readable.pause()` method will cause a stream in flowing mode to stop emitting [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) events, switching out of flowing mode. Any data that becomes available will remain in the internal buffer.
```
const readable = getReadableStreamSomehow();
readable.on('data', (chunk) => {
  console.log(`Received ${chunk.length} bytes of data.`);
  readable.pause();
  console.log('There will be no additional data for 1 second.');
  setTimeout(() => {
    console.log('Now data will start flowing again.');
    readable.resume();
  }, 1000);
});
copy
```

The `readable.pause()` method has no effect if there is a `'readable'` event listener.
######  `readable.pipe(destination[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readablepipedestination-options)
Added in: v0.9.4
  * `destination` [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) The destination for writing data
  * `options`
    * `end` **Default:** `true`.
  * Returns: [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) The  _destination_ , allowing for a chain of pipes if it is a [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) or a [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform) stream


The `readable.pipe()` method attaches a [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) stream to the `readable`, causing it to switch automatically into flowing mode and push all of its data to the attached [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable). The flow of data will be automatically managed so that the destination `Writable` stream is not overwhelmed by a faster `Readable` stream.
The following example pipes all of the data from the `readable` into a file named `file.txt`:
```
const fs = require('node:fs');
const readable = getReadableStreamSomehow();
const writable = fs.createWriteStream('file.txt');
// All the data from readable goes into 'file.txt'.
readable.pipe(writable);
copy
```

It is possible to attach multiple `Writable` streams to a single `Readable` stream.
The `readable.pipe()` method returns a reference to the _destination_ stream making it possible to set up chains of piped streams:
```
const fs = require('node:fs');
const zlib = require('node:zlib');
const r = fs.createReadStream('file.txt');
const z = zlib.createGzip();
const w = fs.createWriteStream('file.txt.gz');
r.pipe(z).pipe(w);
copy
```

By default, [`stream.end()`](https://nodejs.org/docs/latest/api/stream.html#writableendchunk-encoding-callback) is called on the destination `Writable` stream when the source `Readable` stream emits [`'end'`](https://nodejs.org/docs/latest/api/stream.html#event-end), so that the destination is no longer writable. To disable this default behavior, the `end` option can be passed as `false`, causing the destination stream to remain open:
```
reader.pipe(writer, { end: false });
reader.on('end', () => {
  writer.end('Goodbye\n');
});
copy
```

One important caveat is that if the `Readable` stream emits an error during processing, the `Writable` destination _is not closed_ automatically. If an error occurs, it will be necessary to _manually_ close each stream in order to prevent memory leaks.
The [`process.stderr`](https://nodejs.org/docs/latest/api/process.html#processstderr) and [`process.stdout`](https://nodejs.org/docs/latest/api/process.html#processstdout) `Writable` streams are never closed until the Node.js process exits, regardless of the specified options.
######  `readable.read([size])`[#](https://nodejs.org/docs/latest/api/stream.html#readablereadsize)
Added in: v0.9.4
  * `size`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


The `readable.read()` method reads data out of the internal buffer and returns it. If no data is available to be read, `null` is returned. By default, the data is returned as a `Buffer` object unless an encoding has been specified using the `readable.setEncoding()` method or the stream is operating in object mode.
The optional `size` argument specifies a specific number of bytes to read. If `size` bytes are not available to be read, `null` will be returned _unless_ the stream has ended, in which case all of the data remaining in the internal buffer will be returned.
If the `size` argument is not specified, all of the data contained in the internal buffer will be returned.
The `size` argument must be less than or equal to 1 GiB.
The `readable.read()` method should only be called on `Readable` streams operating in paused mode. In flowing mode, `readable.read()` is called automatically until the internal buffer is fully drained.
```
const readable = getReadableStreamSomehow();

// 'readable' may be triggered multiple times as data is buffered in
readable.on('readable', () => {
  let chunk;
  console.log('Stream is readable (new data received in buffer)');
  // Use a loop to make sure we read all currently available data
  while (null !== (chunk = readable.read())) {
    console.log(`Read ${chunk.length} bytes of data...`);
  }
});

// 'end' will be triggered once when there is no more data available
readable.on('end', () => {
  console.log('Reached end of stream.');
});
copy
```

Each call to `readable.read()` returns a chunk of data or `null`, signifying that there's no more data to read at that moment. These chunks aren't automatically concatenated. Because a single `read()` call does not return all the data, using a while loop may be necessary to continuously read chunks until all data is retrieved. When reading a large file, `.read()` might return `null` temporarily, indicating that it has consumed all buffered content but there may be more data yet to be buffered. In such cases, a new `'readable'` event is emitted once there's more data in the buffer, and the `'end'` event signifies the end of data transmission.
Therefore to read a file's whole contents from a `readable`, it is necessary to collect chunks across multiple `'readable'` events:
```
const chunks = [];

readable.on('readable', () => {
  let chunk;
  while (null !== (chunk = readable.read())) {
    chunks.push(chunk);
  }
});

readable.on('end', () => {
  const content = chunks.join('');
});
copy
```

A `Readable` stream in object mode will always return a single item from a call to [`readable.read(size)`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize), regardless of the value of the `size` argument.
If the `readable.read()` method returns a chunk of data, a `'data'` event will also be emitted.
Calling [`stream.read([size])`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize) after the [`'end'`](https://nodejs.org/docs/latest/api/stream.html#event-end) event has been emitted will return `null`. No runtime error will be raised.
######  `readable.readable`[#](https://nodejs.org/docs/latest/api/stream.html#readablereadable)
Added in: v11.4.0
  * Type:


Is `true` if it is safe to call [`readable.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize), which means the stream has not been destroyed or emitted `'error'` or `'end'`.
######  `readable.readableAborted`[#](https://nodejs.org/docs/latest/api/stream.html#readablereadableaborted)
Added in: v16.8.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * Type:


Returns whether the stream was destroyed or errored before emitting `'end'`.
######  `readable.readableDidRead`[#](https://nodejs.org/docs/latest/api/stream.html#readablereadabledidread)
Added in: v16.7.0, v14.18.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * Type:


Returns whether `'data'` has been emitted.
######  `readable.readableEncoding`[#](https://nodejs.org/docs/latest/api/stream.html#readablereadableencoding)
Added in: v12.7.0
  * Type:


Getter for the property `encoding` of a given `Readable` stream. The `encoding` property can be set using the [`readable.setEncoding()`](https://nodejs.org/docs/latest/api/stream.html#readablesetencodingencoding) method.
######  `readable.readableEnded`[#](https://nodejs.org/docs/latest/api/stream.html#readablereadableended)
Added in: v12.9.0
  * Type:


Becomes `true` when [`'end'`](https://nodejs.org/docs/latest/api/stream.html#event-end) event is emitted.
######  `readable.errored`[#](https://nodejs.org/docs/latest/api/stream.html#readableerrored)
Added in: v18.0.0
  * Type:


Returns error if the stream has been destroyed with an error.
######  `readable.readableFlowing`[#](https://nodejs.org/docs/latest/api/stream.html#readablereadableflowing)
Added in: v9.4.0
  * Type:


This property reflects the current state of a `Readable` stream as described in the [Three states](https://nodejs.org/docs/latest/api/stream.html#three-states) section.
######  `readable.readableHighWaterMark`[#](https://nodejs.org/docs/latest/api/stream.html#readablereadablehighwatermark)
Added in: v9.3.0
  * Type:


Returns the value of `highWaterMark` passed when creating this `Readable`.
######  `readable.readableLength`[#](https://nodejs.org/docs/latest/api/stream.html#readablereadablelength)
Added in: v9.4.0
  * Type:


This property contains the number of bytes (or objects) in the queue ready to be read. The value provides introspection data regarding the status of the `highWaterMark`.
######  `readable.readableObjectMode`[#](https://nodejs.org/docs/latest/api/stream.html#readablereadableobjectmode)
Added in: v12.3.0
  * Type:


Getter for the property `objectMode` of a given `Readable` stream.
######  `readable.resume()`[#](https://nodejs.org/docs/latest/api/stream.html#readableresume)
Added in: v0.9.4History Version | Changes
---|---
v10.0.0 | The `resume()` has no effect if there is a `'readable'` event listening.
  * Returns:


The `readable.resume()` method causes an explicitly paused `Readable` stream to resume emitting [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) events, switching the stream into flowing mode.
The `readable.resume()` method can be used to fully consume the data from a stream without actually processing any of that data:
```
getReadableStreamSomehow()
  .resume()
  .on('end', () => {
    console.log('Reached the end, but did not read anything.');
  });
copy
```

The `readable.resume()` method has no effect if there is a `'readable'` event listener.
######  `readable.setEncoding(encoding)`[#](https://nodejs.org/docs/latest/api/stream.html#readablesetencodingencoding)
Added in: v0.9.4
  * `encoding`
  * Returns:


The `readable.setEncoding()` method sets the character encoding for data read from the `Readable` stream.
By default, no encoding is assigned and stream data will be returned as `Buffer` objects. Setting an encoding causes the stream data to be returned as strings of the specified encoding rather than as `Buffer` objects. For instance, calling `readable.setEncoding('utf8')` will cause the output data to be interpreted as UTF-8 data, and passed as strings. Calling `readable.setEncoding('hex')` will cause the data to be encoded in hexadecimal string format.
The `Readable` stream will properly handle multi-byte characters delivered through the stream that would otherwise become improperly decoded if simply pulled from the stream as `Buffer` objects.
```
const readable = getReadableStreamSomehow();
readable.setEncoding('utf8');
readable.on('data', (chunk) => {
  assert.equal(typeof chunk, 'string');
  console.log('Got %d characters of string data:', chunk.length);
});
copy
```

######  `readable.unpipe([destination])`[#](https://nodejs.org/docs/latest/api/stream.html#readableunpipedestination)
Added in: v0.9.4
  * `destination` [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) Optional specific stream to unpipe
  * Returns:


The `readable.unpipe()` method detaches a `Writable` stream previously attached using the [`stream.pipe()`](https://nodejs.org/docs/latest/api/stream.html#readablepipedestination-options) method.
If the `destination` is not specified, then _all_ pipes are detached.
If the `destination` is specified, but no pipe is set up for it, then the method does nothing.
```
const fs = require('node:fs');
const readable = getReadableStreamSomehow();
const writable = fs.createWriteStream('file.txt');
// All the data from readable goes into 'file.txt',
// but only for the first second.
readable.pipe(writable);
setTimeout(() => {
  console.log('Stop writing to file.txt.');
  readable.unpipe(writable);
  console.log('Manually close the file stream.');
  writable.end();
}, 1000);
copy
```

######  `readable.unshift(chunk[, encoding])`[#](https://nodejs.org/docs/latest/api/stream.html#readableunshiftchunk-encoding)
Added in: v0.9.11History Version | Changes
---|---
v22.0.0, v20.13.0 | The `chunk` argument can now be a `TypedArray` or `DataView` instance.
v8.0.0 | The `chunk` argument can now be a `Uint8Array` instance.
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `chunk` must be a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer), `null`. For object mode streams, `chunk` may be any JavaScript value.
  * `encoding` `Buffer` encoding, such as `'utf8'` or `'ascii'`.


Passing `chunk` as `null` signals the end of the stream (EOF) and behaves the same as `readable.push(null)`, after which no more data can be written. The EOF signal is put at the end of the buffer and any buffered data will still be flushed.
The `readable.unshift()` method pushes a chunk of data back into the internal buffer. This is useful in certain situations where a stream is being consumed by code that needs to "un-consume" some amount of data that it has optimistically pulled out of the source, so that the data can be passed on to some other party.
The `stream.unshift(chunk)` method cannot be called after the [`'end'`](https://nodejs.org/docs/latest/api/stream.html#event-end) event has been emitted or a runtime error will be thrown.
Developers using `stream.unshift()` often should consider switching to use of a [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform) stream instead. See the [API for stream implementers](https://nodejs.org/docs/latest/api/stream.html#api-for-stream-implementers) section for more information.
```
// Pull off a header delimited by \n\n.
// Use unshift() if we get too much.
// Call the callback with (error, header, stream).
const { StringDecoder } = require('node:string_decoder');
function parseHeader(stream, callback) {
  stream.on('error', callback);
  stream.on('readable', onReadable);
  const decoder = new StringDecoder('utf8');
  let header = '';
  function onReadable() {
    let chunk;
    while (null !== (chunk = stream.read())) {
      const str = decoder.write(chunk);
      if (str.includes('\n\n')) {
        // Found the header boundary.
        const split = str.split(/\n\n/);
        header += split.shift();
        const remaining = split.join('\n\n');
        const buf = Buffer.from(remaining, 'utf8');
        stream.removeListener('error', callback);
        // Remove the 'readable' listener before unshifting.
        stream.removeListener('readable', onReadable);
        if (buf.length)
          stream.unshift(buf);
        // Now the body of the message can be read from the stream.
        callback(null, header, stream);
        return;
      }
      // Still reading the header.
      header += str;
    }
  }
}
copy
```

Unlike [`stream.push(chunk)`](https://nodejs.org/docs/latest/api/stream.html#readablepushchunk-encoding), `stream.unshift(chunk)` will not end the reading process by resetting the internal reading state of the stream. This can cause unexpected results if `readable.unshift()` is called during a read (i.e. from within a [`stream._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) implementation on a custom stream). Following the call to `readable.unshift()` with an immediate [`stream.push('')`](https://nodejs.org/docs/latest/api/stream.html#readablepushchunk-encoding) will reset the reading state appropriately, however it is best to simply avoid calling `readable.unshift()` while in the process of performing a read.
######  `readable.wrap(stream)`[#](https://nodejs.org/docs/latest/api/stream.html#readablewrapstream)
Added in: v0.9.4
  * `stream` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) An "old style" readable stream
  * Returns:


Prior to Node.js 0.10, streams did not implement the entire `node:stream` module API as it is currently defined. (See [Compatibility](https://nodejs.org/docs/latest/api/stream.html#compatibility-with-older-nodejs-versions) for more information.)
When using an older Node.js library that emits [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) events and has a [`stream.pause()`](https://nodejs.org/docs/latest/api/stream.html#readablepause) method that is advisory only, the `readable.wrap()` method can be used to create a [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) stream that uses the old stream as its data source.
It will rarely be necessary to use `readable.wrap()` but the method has been provided as a convenience for interacting with older Node.js applications and libraries.
```
const { OldReader } = require('./old-api-module.js');
const { Readable } = require('node:stream');
const oreader = new OldReader();
const myReader = new Readable().wrap(oreader);

myReader.on('readable', () => {
  myReader.read(); // etc.
});
copy
```

######  `readable[Symbol.asyncIterator]()`[#](https://nodejs.org/docs/latest/api/stream.html#readablesymbolasynciterator)
Added in: v10.0.0History Version | Changes
---|---
v11.14.0 | Symbol.asyncIterator support is no longer experimental.
  * Returns:

```
const fs = require('node:fs');

async function print(readable) {
  readable.setEncoding('utf8');
  let data = '';
  for await (const chunk of readable) {
    data += chunk;
  }
  console.log(data);
}

print(fs.createReadStream('file')).catch(console.error);
copy
```

If the loop terminates with a `break`, `return`, or a `throw`, the stream will be destroyed. In other terms, iterating over a stream will consume the stream fully. The stream will be read in chunks of size equal to the `highWaterMark` option. In the code example above, data will be in a single chunk if the file has less then 64 KiB of data because no `highWaterMark` option is provided to [`fs.createReadStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatereadstreampath-options).
######  `readable[Symbol.asyncDispose]()`[#](https://nodejs.org/docs/latest/api/stream.html#readablesymbolasyncdispose)
Added in: v20.4.0, v18.18.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Calls [`readable.destroy()`](https://nodejs.org/docs/latest/api/stream.html#readabledestroyerror) with an `AbortError` and returns a promise that fulfills when the stream is finished.
######  `readable.compose(stream[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readablecomposestream-options)
Added in: v19.1.0, v18.13.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `stream` [`<Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) | [`<Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) | [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream) | [`<TransformStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-transformstream) |
  * `options`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns: [`<Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) a stream composed with the stream `stream`.

```
import { Readable } from 'node:stream';

async function* splitToWords(source) {
  for await (const chunk of source) {
    const words = String(chunk).split(' ');

    for (const word of words) {
      yield word;
    }
  }
}

const wordsStream = Readable.from(['text passed through', 'composed stream']).compose(splitToWords);
const words = await wordsStream.toArray();

console.log(words); // prints ['text', 'passed', 'through', 'composed', 'stream']
copy
```

`readable.compose(s)` is equivalent to `stream.compose(readable, s)`.
This method also allows for an [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) to be provided, which will destroy the composed stream when aborted.
See [`stream.compose(...streams)`](https://nodejs.org/docs/latest/api/stream.html#streamcomposestreams) for more information.
######  `readable.iterator([options])`[#](https://nodejs.org/docs/latest/api/stream.html#readableiteratoroptions)
Added in: v16.3.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `options`
    * `destroyOnReturn` `false`, calling `return` on the async iterator, or exiting a `for await...of` iteration using a `break`, `return`, or `throw` will not destroy the stream. **Default:** `true`.
  * Returns:


The iterator created by this method gives users the option to cancel the destruction of the stream if the `for await...of` loop is exited by `return`, `break`, or `throw`, or if the iterator should destroy the stream if the stream emitted an error during iteration.
```
const { Readable } = require('node:stream');

async function printIterator(readable) {
  for await (const chunk of readable.iterator({ destroyOnReturn: false })) {
    console.log(chunk); // 1
    break;
  }

  console.log(readable.destroyed); // false

  for await (const chunk of readable.iterator({ destroyOnReturn: false })) {
    console.log(chunk); // Will print 2 and then 3
  }

  console.log(readable.destroyed); // True, stream was totally consumed
}

async function printSymbolAsyncIterator(readable) {
  for await (const chunk of readable) {
    console.log(chunk); // 1
    break;
  }

  console.log(readable.destroyed); // true
}

async function showBoth() {
  await printIterator(Readable.from([1, 2, 3]));
  await printSymbolAsyncIterator(Readable.from([1, 2, 3]));
}

showBoth();
copy
```

######  `readable.map(fn[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#readablemapfn-options)
Added in: v17.4.0, v16.14.0History Version | Changes
---|---
v20.7.0, v18.19.0 | added `highWaterMark` in options.
Stability: 1 - Experimental
  * `fn`
    * `data`
    * `options`
      * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) aborted if the stream is destroyed allowing to abort the `fn` call early.
  * `options`
    * `concurrency` `fn` to call on the stream at once. **Default:** `1`.
    * `highWaterMark` **Default:** `concurrency * 2 - 1`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) allows destroying the stream if the signal is aborted.
  * Returns: [`<Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) a stream mapped with the function `fn`.
