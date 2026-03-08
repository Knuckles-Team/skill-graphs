## Stream[#](https://nodejs.org/docs/latest/api/stream.html#stream)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
A stream is an abstract interface for working with streaming data in Node.js. The `node:stream` module provides an API for implementing the stream interface.
There are many stream objects provided by Node.js. For instance, a [request to an HTTP server](https://nodejs.org/docs/latest/api/http.html#class-httpincomingmessage) and [`process.stdout`](https://nodejs.org/docs/latest/api/process.html#processstdout) are both stream instances.
Streams can be readable, writable, or both. All streams are instances of [`EventEmitter`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter).
To access the `node:stream` module:
```
const stream = require('node:stream');
copy
```

The `node:stream` module is useful for creating new types of stream instances. It is usually not necessary to use the `node:stream` module to consume streams.
### Organization of this document[#](https://nodejs.org/docs/latest/api/stream.html#organization-of-this-document)
This document contains two primary sections and a third section for notes. The first section explains how to use existing streams within an application. The second section explains how to create new types of streams.
### Types of streams[#](https://nodejs.org/docs/latest/api/stream.html#types-of-streams)
There are four fundamental stream types within Node.js:
  * [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable): streams to which data can be written (for example, [`fs.createWriteStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatewritestreampath-options)).
  * [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable): streams from which data can be read (for example, [`fs.createReadStream()`](https://nodejs.org/docs/latest/api/fs.html#fscreatereadstreampath-options)).
  * [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex): streams that are both `Readable` and `Writable` (for example, [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)).
  * [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform): `Duplex` streams that can modify or transform the data as it is written and read (for example, [`zlib.createDeflate()`](https://nodejs.org/docs/latest/api/zlib.html#zlibcreatedeflateoptions)).


Additionally, this module includes the utility functions [`stream.duplexPair()`](https://nodejs.org/docs/latest/api/stream.html#streamduplexpairoptions), [`stream.pipeline()`](https://nodejs.org/docs/latest/api/stream.html#streampipelinesource-transforms-destination-callback), [`stream.finished()`](https://nodejs.org/docs/latest/api/stream.html#streamfinishedstream-options-callback) [`stream.Readable.from()`](https://nodejs.org/docs/latest/api/stream.html#streamreadablefromiterable-options), and [`stream.addAbortSignal()`](https://nodejs.org/docs/latest/api/stream.html#streamaddabortsignalsignal-stream).
#### Streams Promises API[#](https://nodejs.org/docs/latest/api/stream.html#streams-promises-api)
Added in: v15.0.0
The `stream/promises` API provides an alternative set of asynchronous utility functions for streams that return `Promise` objects rather than using callbacks. The API is accessible via `require('node:stream/promises')` or `require('node:stream').promises`.
####  `stream.pipeline(streams[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#streampipelinestreams-options)
####  `stream.pipeline(source[, ...transforms], destination[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#streampipelinesource-transforms-destination-options)
Added in: v15.0.0History Version | Changes
---|---
v18.0.0, v17.2.0, v16.14.0 | Add the `end` option, which can be set to `false` to prevent automatically closing the destination stream when the source ends.
  * `streams` [`<Stream[]>`](https://nodejs.org/docs/latest/api/stream.html#stream) |
  * `source` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) |
    * Returns:
  * `...transforms` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) |
    * `source`
    * Returns:
  * `destination` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) |
    * `source`
    * Returns:
  * `options`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal)
    * `end` `false`. **Default:** `true`.
  * Returns:

```
const { pipeline } = require('node:stream/promises');
const fs = require('node:fs');
const zlib = require('node:zlib');

async function run() {
  await pipeline(
    fs.createReadStream('archive.tar'),
    zlib.createGzip(),
    fs.createWriteStream('archive.tar.gz'),
  );
  console.log('Pipeline succeeded.');
}

run().catch(console.error);
import { pipeline } from 'node:stream/promises';
import { createReadStream, createWriteStream } from 'node:fs';
import { createGzip } from 'node:zlib';

await pipeline(
  createReadStream('archive.tar'),
  createGzip(),
  createWriteStream('archive.tar.gz'),
);
console.log('Pipeline succeeded.');
copy
```

To use an `AbortSignal`, pass it inside an options object, as the last argument. When the signal is aborted, `destroy` will be called on the underlying pipeline, with an `AbortError`.
```
const { pipeline } = require('node:stream/promises');
const fs = require('node:fs');
const zlib = require('node:zlib');

async function run() {
  const ac = new AbortController();
  const signal = ac.signal;

  setImmediate(() => ac.abort());
  await pipeline(
    fs.createReadStream('archive.tar'),
    zlib.createGzip(),
    fs.createWriteStream('archive.tar.gz'),
    { signal },
  );
}

run().catch(console.error); // AbortError
import { pipeline } from 'node:stream/promises';
import { createReadStream, createWriteStream } from 'node:fs';
import { createGzip } from 'node:zlib';

const ac = new AbortController();
const { signal } = ac;
setImmediate(() => ac.abort());
try {
  await pipeline(
    createReadStream('archive.tar'),
    createGzip(),
    createWriteStream('archive.tar.gz'),
    { signal },
  );
} catch (err) {
  console.error(err); // AbortError
}
copy
```

The `pipeline` API also supports async generators:
```
const { pipeline } = require('node:stream/promises');
const fs = require('node:fs');

async function run() {
  await pipeline(
    fs.createReadStream('lowercase.txt'),
    async function* (source, { signal }) {
      source.setEncoding('utf8');  // Work with strings rather than `Buffer`s.
      for await (const chunk of source) {
        yield await processChunk(chunk, { signal });
      }
    },
    fs.createWriteStream('uppercase.txt'),
  );
  console.log('Pipeline succeeded.');
}

run().catch(console.error);
import { pipeline } from 'node:stream/promises';
import { createReadStream, createWriteStream } from 'node:fs';

await pipeline(
  createReadStream('lowercase.txt'),
  async function* (source, { signal }) {
    source.setEncoding('utf8');  // Work with strings rather than `Buffer`s.
    for await (const chunk of source) {
      yield await processChunk(chunk, { signal });
    }
  },
  createWriteStream('uppercase.txt'),
);
console.log('Pipeline succeeded.');
copy
```

Remember to handle the `signal` argument passed into the async generator. Especially in the case where the async generator is the source for the pipeline (i.e. first argument) or the pipeline will never complete.
```
const { pipeline } = require('node:stream/promises');
const fs = require('node:fs');

async function run() {
  await pipeline(
    async function* ({ signal }) {
      await someLongRunningfn({ signal });
      yield 'asd';
    },
    fs.createWriteStream('uppercase.txt'),
  );
  console.log('Pipeline succeeded.');
}

run().catch(console.error);
import { pipeline } from 'node:stream/promises';
import fs from 'node:fs';
await pipeline(
  async function* ({ signal }) {
    await someLongRunningfn({ signal });
    yield 'asd';
  },
  fs.createWriteStream('uppercase.txt'),
);
console.log('Pipeline succeeded.');
copy
```

The `pipeline` API provides [callback version](https://nodejs.org/docs/latest/api/stream.html#streampipelinesource-transforms-destination-callback):
####  `stream.finished(stream[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#streamfinishedstream-options)
Added in: v15.0.0History Version | Changes
---|---
v19.5.0, v18.14.0 | Added support for `ReadableStream` and `WritableStream`.
v19.1.0, v18.13.0 | The `cleanup` option was added.
  * `stream` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) | [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream) | [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream) A readable and/or writable stream/webstream.
  * `options`
    * `error`
    * `readable`
    * `writable`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) |
    * `cleanup` `true`, removes the listeners registered by this function before the promise is fulfilled. **Default:** `false`.
  * Returns:

```
const { finished } = require('node:stream/promises');
const fs = require('node:fs');

const rs = fs.createReadStream('archive.tar');

async function run() {
  await finished(rs);
  console.log('Stream is done reading.');
}

run().catch(console.error);
rs.resume(); // Drain the stream.
import { finished } from 'node:stream/promises';
import { createReadStream } from 'node:fs';

const rs = createReadStream('archive.tar');

async function run() {
  await finished(rs);
  console.log('Stream is done reading.');
}

run().catch(console.error);
rs.resume(); // Drain the stream.
copy
```

The `finished` API also provides a [callback version](https://nodejs.org/docs/latest/api/stream.html#streamfinishedstream-options-callback).
`stream.finished()` leaves dangling event listeners (in particular `'error'`, `'end'`, `'finish'` and `'close'`) after the returned promise is resolved or rejected. The reason for this is so that unexpected `'error'` events (due to incorrect stream implementations) do not cause unexpected crashes. If this is unwanted behavior then `options.cleanup` should be set to `true`:
```
await finished(rs, { cleanup: true });
copy
```

#### Object mode[#](https://nodejs.org/docs/latest/api/stream.html#object-mode)
All streams created by Node.js APIs operate exclusively on strings, [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer),
  * `Strings` and `Buffers` are the most common types used with streams.
  * `TypedArray` and `DataView` lets you handle binary data with types like `Int32Array` or `Uint8Array`. When you write a TypedArray or DataView to a stream, Node.js processes the raw bytes.


It is possible, however, for stream implementations to work with other types of JavaScript values (with the exception of `null`, which serves a special purpose within streams). Such streams are considered to operate in "object mode".
Stream instances are switched into object mode using the `objectMode` option when the stream is created. Attempting to switch an existing stream into object mode is not safe.
#### Buffering[#](https://nodejs.org/docs/latest/api/stream.html#buffering)
Both [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) and [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) streams will store data in an internal buffer.
The amount of data potentially buffered depends on the `highWaterMark` option passed into the stream's constructor. For normal streams, the `highWaterMark` option specifies a [total number of bytes](https://nodejs.org/docs/latest/api/stream.html#highwatermark-discrepancy-after-calling-readablesetencoding). For streams operating in object mode, the `highWaterMark` specifies a total number of objects. For streams operating on (but not decoding) strings, the `highWaterMark` specifies a total number of UTF-16 code units.
Data is buffered in `Readable` streams when the implementation calls [`stream.push(chunk)`](https://nodejs.org/docs/latest/api/stream.html#readablepushchunk-encoding). If the consumer of the Stream does not call [`stream.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize), the data will sit in the internal queue until it is consumed.
Once the total size of the internal read buffer reaches the threshold specified by `highWaterMark`, the stream will temporarily stop reading data from the underlying resource until the data currently buffered can be consumed (that is, the stream will stop calling the internal [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) method that is used to fill the read buffer).
Data is buffered in `Writable` streams when the [`writable.write(chunk)`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) method is called repeatedly. While the total size of the internal write buffer is below the threshold set by `highWaterMark`, calls to `writable.write()` will return `true`. Once the size of the internal buffer reaches or exceeds the `highWaterMark`, `false` will be returned.
A key goal of the `stream` API, particularly the [`stream.pipe()`](https://nodejs.org/docs/latest/api/stream.html#readablepipedestination-options) method, is to limit the buffering of data to acceptable levels such that sources and destinations of differing speeds will not overwhelm the available memory.
The `highWaterMark` option is a threshold, not a limit: it dictates the amount of data that a stream buffers before it stops asking for more data. It does not enforce a strict memory limitation in general. Specific stream implementations may choose to enforce stricter limits but doing so is optional.
Because [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) and [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform) streams are both `Readable` and `Writable`, each maintains _two_ separate internal buffers used for reading and writing, allowing each side to operate independently of the other while maintaining an appropriate and efficient flow of data. For example, [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) instances are [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) streams whose `Readable` side allows consumption of data received _from_ the socket and whose `Writable` side allows writing data _to_ the socket. Because data may be written to the socket at a faster or slower rate than data is received, each side should operate (and buffer) independently of the other.
The mechanics of the internal buffering are an internal implementation detail and may be changed at any time. However, for certain advanced implementations, the internal buffers can be retrieved using `writable.writableBuffer` or `readable.readableBuffer`. Use of these undocumented properties is discouraged.
### API for stream consumers[#](https://nodejs.org/docs/latest/api/stream.html#api-for-stream-consumers)
Almost all Node.js applications, no matter how simple, use streams in some manner. The following is an example of using streams in a Node.js application that implements an HTTP server:
```
const http = require('node:http');

const server = http.createServer((req, res) => {
  // `req` is an http.IncomingMessage, which is a readable stream.
  // `res` is an http.ServerResponse, which is a writable stream.

  let body = '';
  // Get the data as utf8 strings.
  // If an encoding is not set, Buffer objects will be received.
  req.setEncoding('utf8');

  // Readable streams emit 'data' events once a listener is added.
  req.on('data', (chunk) => {
    body += chunk;
  });

  // The 'end' event indicates that the entire body has been received.
  req.on('end', () => {
    try {
      const data = JSON.parse(body);
      // Write back something interesting to the user:
      res.write(typeof data);
      res.end();
    } catch (er) {
      // uh oh! bad json!
      res.statusCode = 400;
      return res.end(`error: ${er.message}`);
    }
  });
});

server.listen(1337);

// $ curl localhost:1337 -d "{}"
// object
// $ curl localhost:1337 -d "\"foo\""
// string
// $ curl localhost:1337 -d "not json"
// error: Unexpected token 'o', "not json" is not valid JSON
copy
```

[`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) streams (such as `res` in the example) expose methods such as `write()` and `end()` that are used to write data onto the stream.
[`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) streams use the [`EventEmitter`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) API for notifying application code when data is available to be read off the stream. That available data can be read from the stream in multiple ways.
Both [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) and [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) streams use the [`EventEmitter`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) API in various ways to communicate the current state of the stream.
[`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) and [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform) streams are both [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) and [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable).
Applications that are either writing data to or consuming data from a stream are not required to implement the stream interfaces directly and will generally have no reason to call `require('node:stream')`.
Developers wishing to implement new types of streams should refer to the section [API for stream implementers](https://nodejs.org/docs/latest/api/stream.html#api-for-stream-implementers).
#### Writable streams[#](https://nodejs.org/docs/latest/api/stream.html#writable-streams)
Writable streams are an abstraction for a _destination_ to which data is written.
Examples of [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) streams include:
  * [HTTP requests, on the client](https://nodejs.org/docs/latest/api/http.html#class-httpclientrequest)
  * [HTTP responses, on the server](https://nodejs.org/docs/latest/api/http.html#class-httpserverresponse)
  * [fs write streams](https://nodejs.org/docs/latest/api/fs.html#class-fswritestream)
  * [zlib streams](https://nodejs.org/docs/latest/api/zlib.html)
  * [crypto streams](https://nodejs.org/docs/latest/api/crypto.html)
  * [TCP sockets](https://nodejs.org/docs/latest/api/net.html#class-netsocket)
  * [child process stdin](https://nodejs.org/docs/latest/api/child_process.html#subprocessstdin)
  * [`process.stdout`](https://nodejs.org/docs/latest/api/process.html#processstdout), [`process.stderr`](https://nodejs.org/docs/latest/api/process.html#processstderr)


Some of these examples are actually [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) streams that implement the [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) interface.
All [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) streams implement the interface defined by the `stream.Writable` class.
While specific instances of [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) streams may differ in various ways, all `Writable` streams follow the same fundamental usage pattern as illustrated in the example below:
```
const myStream = getWritableStreamSomehow();
myStream.write('some data');
myStream.write('some more data');
myStream.end('done writing data');
copy
```

##### Class: `stream.Writable`[#](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable)
Added in: v0.9.4
###### Event: `'close'`[#](https://nodejs.org/docs/latest/api/stream.html#event-close)
Added in: v0.9.4History Version | Changes
---|---
v10.0.0 | Add `emitClose` option to specify if `'close'` is emitted on destroy.
The `'close'` event is emitted when the stream and any of its underlying resources (a file descriptor, for example) have been closed. The event indicates that no more events will be emitted, and no further computation will occur.
A [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) stream will always emit the `'close'` event if it is created with the `emitClose` option.
###### Event: `'drain'`[#](https://nodejs.org/docs/latest/api/stream.html#event-drain)
Added in: v0.9.4
If a call to [`stream.write(chunk)`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) returns `false`, the `'drain'` event will be emitted when it is appropriate to resume writing data to the stream.
```
// Write the data to the supplied writable stream one million times.
// Be attentive to back-pressure.
function writeOneMillionTimes(writer, data, encoding, callback) {
  let i = 1000000;
  write();
  function write() {
    let ok = true;
    do {
      i--;
      if (i === 0) {
        // Last time!
        writer.write(data, encoding, callback);
      } else {
        // See if we should continue, or wait.
        // Don't pass the callback, because we're not done yet.
        ok = writer.write(data, encoding);
      }
    } while (i > 0 && ok);
    if (i > 0) {
      // Had to stop early!
      // Write some more once it drains.
      writer.once('drain', write);
    }
  }
}
copy
```

###### Event: `'error'`[#](https://nodejs.org/docs/latest/api/stream.html#event-error)
Added in: v0.9.4
  * Type:


The `'error'` event is emitted if an error occurred while writing or piping data. The listener callback is passed a single `Error` argument when called.
The stream is closed when the `'error'` event is emitted unless the [`autoDestroy`](https://nodejs.org/docs/latest/api/stream.html#new-streamwritableoptions) option was set to `false` when creating the stream.
After `'error'`, no further events other than `'close'` _should_ be emitted (including `'error'` events).
###### Event: `'finish'`[#](https://nodejs.org/docs/latest/api/stream.html#event-finish)
Added in: v0.9.4
The `'finish'` event is emitted after the [`stream.end()`](https://nodejs.org/docs/latest/api/stream.html#writableendchunk-encoding-callback) method has been called, and all data has been flushed to the underlying system.
```
const writer = getWritableStreamSomehow();
for (let i = 0; i < 100; i++) {
  writer.write(`hello, #${i}!\n`);
}
writer.on('finish', () => {
  console.log('All writes are now complete.');
});
writer.end('This is the end\n');
copy
```

###### Event: `'pipe'`[#](https://nodejs.org/docs/latest/api/stream.html#event-pipe)
Added in: v0.9.4
  * `src` [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) source stream that is piping to this writable


The `'pipe'` event is emitted when the [`stream.pipe()`](https://nodejs.org/docs/latest/api/stream.html#readablepipedestination-options) method is called on a readable stream, adding this writable to its set of destinations.
```
const writer = getWritableStreamSomehow();
const reader = getReadableStreamSomehow();
writer.on('pipe', (src) => {
  console.log('Something is piping into the writer.');
  assert.equal(src, reader);
});
reader.pipe(writer);
copy
```

###### Event: `'unpipe'`[#](https://nodejs.org/docs/latest/api/stream.html#event-unpipe)
Added in: v0.9.4
  * `src` [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) The source stream that [unpiped](https://nodejs.org/docs/latest/api/stream.html#readableunpipedestination) this writable


The `'unpipe'` event is emitted when the [`stream.unpipe()`](https://nodejs.org/docs/latest/api/stream.html#readableunpipedestination) method is called on a [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) stream, removing this [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) from its set of destinations.
This is also emitted in case this [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) stream emits an error when a [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) stream pipes into it.
```
const writer = getWritableStreamSomehow();
const reader = getReadableStreamSomehow();
writer.on('unpipe', (src) => {
  console.log('Something has stopped piping into the writer.');
  assert.equal(src, reader);
});
reader.pipe(writer);
reader.unpipe(writer);
copy
```

######  `writable.cork()`[#](https://nodejs.org/docs/latest/api/stream.html#writablecork)
Added in: v0.11.2
The `writable.cork()` method forces all written data to be buffered in memory. The buffered data will be flushed when either the [`stream.uncork()`](https://nodejs.org/docs/latest/api/stream.html#writableuncork) or [`stream.end()`](https://nodejs.org/docs/latest/api/stream.html#writableendchunk-encoding-callback) methods are called.
The primary intent of `writable.cork()` is to accommodate a situation in which several small chunks are written to the stream in rapid succession. Instead of immediately forwarding them to the underlying destination, `writable.cork()` buffers all the chunks until `writable.uncork()` is called, which will pass them all to `writable._writev()`, if present. This prevents a head-of-line blocking situation where data is being buffered while waiting for the first small chunk to be processed. However, use of `writable.cork()` without implementing `writable._writev()` may have an adverse effect on throughput.
