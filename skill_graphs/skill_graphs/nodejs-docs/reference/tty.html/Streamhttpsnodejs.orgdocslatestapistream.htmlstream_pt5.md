

A module method to pipe between streams and generators forwarding errors and properly cleaning up and provide a callback when the pipeline is complete.
```
const { pipeline } = require('node:stream');
const fs = require('node:fs');
const zlib = require('node:zlib');

// Use the pipeline API to easily pipe a series of streams
// together and get notified when the pipeline is fully done.

// A pipeline to gzip a potentially huge tar file efficiently:

pipeline(
  fs.createReadStream('archive.tar'),
  zlib.createGzip(),
  fs.createWriteStream('archive.tar.gz'),
  (err) => {
    if (err) {
      console.error('Pipeline failed.', err);
    } else {
      console.log('Pipeline succeeded.');
    }
  },
);
copy
```

The `pipeline` API provides a [promise version](https://nodejs.org/docs/latest/api/stream.html#streampipelinesource-transforms-destination-options).
`stream.pipeline()` will call `stream.destroy(err)` on all streams except:
  * `Readable` streams which have emitted `'end'` or `'close'`.
  * `Writable` streams which have emitted `'finish'` or `'close'`.


`stream.pipeline()` leaves dangling event listeners on the streams after the `callback` has been invoked. In the case of reuse of streams after failure, this can cause event listener leaks and swallowed errors. If the last stream is readable, dangling event listeners will be removed so that the last stream can be consumed later.
`stream.pipeline()` closes all the streams when an error is raised. The `IncomingRequest` usage with `pipeline` could lead to an unexpected behavior once it would destroy the socket without sending the expected response. See the example below:
```
const fs = require('node:fs');
const http = require('node:http');
const { pipeline } = require('node:stream');

const server = http.createServer((req, res) => {
  const fileStream = fs.createReadStream('./fileNotExist.txt');
  pipeline(fileStream, res, (err) => {
    if (err) {
      console.log(err); // No such file
      // this message can't be sent once `pipeline` already destroyed the socket
      return res.end('error!!!');
    }
  });
});
copy
```

####  `stream.compose(...streams)`[#](https://nodejs.org/docs/latest/api/stream.html#streamcomposestreams)
Added in: v16.9.0History Version | Changes
---|---
v21.1.0, v20.10.0 | Added support for stream class.
v19.8.0, v18.16.0 | Added support for webstreams.
Stability: 1 - `stream.compose` is experimental.
  * `streams` [`<Stream[]>`](https://nodejs.org/docs/latest/api/stream.html#stream) | [`<ReadableStream[]>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream) | [`<WritableStream[]>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream) | [`<TransformStream[]>`](https://nodejs.org/docs/latest/api/webstreams.html#class-transformstream) | [`<Duplex[]>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) |
  * Returns: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


Combines two or more streams into a `Duplex` stream that writes to the first stream and reads from the last. Each provided stream is piped into the next, using `stream.pipeline`. If any of the streams error then all are destroyed, including the outer `Duplex` stream.
Because `stream.compose` returns a new stream that in turn can (and should) be piped into other streams, it enables composition. In contrast, when passing streams to `stream.pipeline`, typically the first stream is a readable stream and the last a writable stream, forming a closed circuit.
If passed a `Function` it must be a factory method taking a `source` `Iterable`.
```
import { compose, Transform } from 'node:stream';

const removeSpaces = new Transform({
  transform(chunk, encoding, callback) {
    callback(null, String(chunk).replace(' ', ''));
  },
});

async function* toUpper(source) {
  for await (const chunk of source) {
    yield String(chunk).toUpperCase();
  }
}

let res = '';
for await (const buf of compose(removeSpaces, toUpper).end('hello world')) {
  res += buf;
}

console.log(res); // prints 'HELLOWORLD'
copy
```

`stream.compose` can be used to convert async iterables, generators and functions into streams.
  * `AsyncIterable` converts into a readable `Duplex`. Cannot yield `null`.
  * `AsyncGeneratorFunction` converts into a readable/writable transform `Duplex`. Must take a source `AsyncIterable` as first parameter. Cannot yield `null`.
  * `AsyncFunction` converts into a writable `Duplex`. Must return either `null` or `undefined`.

```
import { compose } from 'node:stream';
import { finished } from 'node:stream/promises';

// Convert AsyncIterable into readable Duplex.
const s1 = compose(async function*() {
  yield 'Hello';
  yield 'World';
}());

// Convert AsyncGenerator into transform Duplex.
const s2 = compose(async function*(source) {
  for await (const chunk of source) {
    yield String(chunk).toUpperCase();
  }
});

let res = '';

// Convert AsyncFunction into writable Duplex.
const s3 = compose(async function(source) {
  for await (const chunk of source) {
    res += chunk;
  }
});

await finished(compose(s1, s2, s3));

console.log(res); // prints 'HELLOWORLD'
copy
```

For convenience, the [`readable.compose(stream)`](https://nodejs.org/docs/latest/api/stream.html#readablecomposestream-options) method is available on [`<Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) and [`<Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) streams as a wrapper for this function.
####  `stream.isErrored(stream)`[#](https://nodejs.org/docs/latest/api/stream.html#streamiserroredstream)
Added in: v17.3.0, v16.14.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `stream` [`<Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) | [`<Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) | [`<Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) | [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream) | [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream)
  * Returns:


Returns whether the stream has encountered an error.
####  `stream.isReadable(stream)`[#](https://nodejs.org/docs/latest/api/stream.html#streamisreadablestream)
Added in: v17.4.0, v16.14.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `stream` [`<Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) | [`<Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) | [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream)
  * Returns: `null` if `stream` is not a valid `Readable`, `Duplex` or `ReadableStream`.


Returns whether the stream is readable.
####  `stream.isWritable(stream)`[#](https://nodejs.org/docs/latest/api/stream.html#streamiswritablestream)
  * `stream` [`<Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) | [`<Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) | [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream)
  * Returns: `null` if `stream` is not a valid `Writable`, `Duplex` or `WritableStream`.


Returns whether the stream is writable.
####  `stream.Readable.from(iterable[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#streamreadablefromiterable-options)
Added in: v12.3.0, v10.17.0
  * `iterable` `Symbol.asyncIterator` or `Symbol.iterator` iterable protocol. Emits an 'error' event if a null value is passed.
  * `options` `new stream.Readable([options])`. By default, `Readable.from()` will set `options.objectMode` to `true`, unless this is explicitly opted out by setting `options.objectMode` to `false`.
  * Returns: [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable)


A utility method for creating readable streams out of iterators.
```
const { Readable } = require('node:stream');

async function * generate() {
  yield 'hello';
  yield 'streams';
}

const readable = Readable.from(generate());

readable.on('data', (chunk) => {
  console.log(chunk);
});
copy
```

Calling `Readable.from(string)` or `Readable.from(buffer)` will not have the strings or buffers be iterated to match the other streams semantics for performance reasons.
If an `Iterable` object containing promises is passed as an argument, it might result in unhandled rejection.
```
const { Readable } = require('node:stream');

Readable.from([
  new Promise((resolve) => setTimeout(resolve('1'), 1500)),
  new Promise((_, reject) => setTimeout(reject(new Error('2')), 1000)), // Unhandled rejection
]);
copy
```

####  `stream.Readable.fromWeb(readableStream[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#streamreadablefromwebreadablestream-options)
Added in: v17.0.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `readableStream` [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream)
  * `options`
    * `encoding`
    * `highWaterMark`
    * `objectMode`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal)
  * Returns: [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable)


####  `stream.Readable.isDisturbed(stream)`[#](https://nodejs.org/docs/latest/api/stream.html#streamreadableisdisturbedstream)
Added in: v16.8.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `stream` [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) | [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream)
  * Returns: `boolean`


Returns whether the stream has been read from or cancelled.
####  `stream.Readable.toWeb(streamReadable[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#streamreadabletowebstreamreadable-options)
Added in: v17.0.0History Version | Changes
---|---
v25.4.0 | Add 'type' option to specify 'bytes'.
v24.0.0, v22.17.0 | Marking the API stable.
v18.7.0 | include strategy options on Readable.
  * `streamReadable` [`<stream.Readable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable)
  * `options`
    * `strategy`
      * `highWaterMark` `ReadableStream`) before backpressure is applied in reading from the given `stream.Readable`. If no value is provided, it will be taken from the given `stream.Readable`.
      * `size` `1` for all the chunks.
        * `chunk`
        * Returns:
    * `type` `ReadableStream`. Must be `'bytes'` or undefined.
  * Returns: [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream)


####  `stream.Writable.fromWeb(writableStream[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#streamwritablefromwebwritablestream-options)
Added in: v17.0.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `writableStream` [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream)
  * `options`
    * `decodeStrings`
    * `highWaterMark`
    * `objectMode`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal)
  * Returns: [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable)


####  `stream.Writable.toWeb(streamWritable)`[#](https://nodejs.org/docs/latest/api/stream.html#streamwritabletowebstreamwritable)
Added in: v17.0.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `streamWritable` [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable)
  * Returns: [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream)


####  `stream.Duplex.from(src)`[#](https://nodejs.org/docs/latest/api/stream.html#streamduplexfromsrc)
Added in: v16.8.0History Version | Changes
---|---
v19.5.0, v18.17.0 | The `src` argument can now be a `ReadableStream` or `WritableStream`.
  * `src` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) | [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) | [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream) | [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream)


A utility method for creating duplex streams.
  * `Stream` converts writable stream into writable `Duplex` and readable stream to `Duplex`.
  * `Blob` converts into readable `Duplex`.
  * `string` converts into readable `Duplex`.
  * `ArrayBuffer` converts into readable `Duplex`.
  * `AsyncIterable` converts into a readable `Duplex`. Cannot yield `null`.
  * `AsyncGeneratorFunction` converts into a readable/writable transform `Duplex`. Must take a source `AsyncIterable` as first parameter. Cannot yield `null`.
  * `AsyncFunction` converts into a writable `Duplex`. Must return either `null` or `undefined`
  * `Object ({ writable, readable })` converts `readable` and `writable` into `Stream` and then combines them into `Duplex` where the `Duplex` will write to the `writable` and read from the `readable`.
  * `Promise` converts into readable `Duplex`. Value `null` is ignored.
  * `ReadableStream` converts into readable `Duplex`.
  * `WritableStream` converts into writable `Duplex`.
  * Returns: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


If an `Iterable` object containing promises is passed as an argument, it might result in unhandled rejection.
```
const { Duplex } = require('node:stream');

Duplex.from([
  new Promise((resolve) => setTimeout(resolve('1'), 1500)),
  new Promise((_, reject) => setTimeout(reject(new Error('2')), 1000)), // Unhandled rejection
]);
copy
```

####  `stream.Duplex.fromWeb(pair[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#streamduplexfromwebpair-options)
Added in: v17.0.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `pair`
    * `readable` [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream)
    * `writable` [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream)
  * `options`
    * `allowHalfOpen`
    * `decodeStrings`
    * `encoding`
    * `highWaterMark`
    * `objectMode`
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal)
  * Returns: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)

```
import { Duplex } from 'node:stream';
import {
  ReadableStream,
  WritableStream,
} from 'node:stream/web';

const readable = new ReadableStream({
  start(controller) {
    controller.enqueue('world');
  },
});

const writable = new WritableStream({
  write(chunk) {
    console.log('writable', chunk);
  },
});

const pair = {
  readable,
  writable,
};
const duplex = Duplex.fromWeb(pair, { encoding: 'utf8', objectMode: true });

duplex.write('hello');

for await (const chunk of duplex) {
  console.log('readable', chunk);
}
const { Duplex } = require('node:stream');
const {
  ReadableStream,
  WritableStream,
} = require('node:stream/web');

const readable = new ReadableStream({
  start(controller) {
    controller.enqueue('world');
  },
});

const writable = new WritableStream({
  write(chunk) {
    console.log('writable', chunk);
  },
});

const pair = {
  readable,
  writable,
};
const duplex = Duplex.fromWeb(pair, { encoding: 'utf8', objectMode: true });

duplex.write('hello');
duplex.once('readable', () => console.log('readable', duplex.read()));
copy
```

####  `stream.Duplex.toWeb(streamDuplex[, options])`[#](https://nodejs.org/docs/latest/api/stream.html#streamduplextowebstreamduplex-options)
Added in: v17.0.0History Version | Changes
---|---
v25.7.0 | Added the 'readableType' option to specify the ReadableStream type. The 'type' option is deprecated.
v25.4.0 | Added the 'type' option to specify the ReadableStream type.
v24.0.0, v22.17.0 | Marking the API stable.
  * `streamDuplex` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)
  * `options`
    * `readableType` `ReadableStream` half of the created readable-writable pair. Must be `'bytes'` or undefined. (`options.type` is a deprecated alias for this option.)
  * Returns:
    * `readable` [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream)
    * `writable` [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream)

```
import { Duplex } from 'node:stream';

const duplex = Duplex({
  objectMode: true,
  read() {
    this.push('world');
    this.push(null);
  },
  write(chunk, encoding, callback) {
    console.log('writable', chunk);
    callback();
  },
});

const { readable, writable } = Duplex.toWeb(duplex);
writable.getWriter().write('hello');

const { value } = await readable.getReader().read();
console.log('readable', value);
const { Duplex } = require('node:stream');

const duplex = Duplex({
  objectMode: true,
  read() {
    this.push('world');
    this.push(null);
  },
  write(chunk, encoding, callback) {
    console.log('writable', chunk);
    callback();
  },
});

const { readable, writable } = Duplex.toWeb(duplex);
writable.getWriter().write('hello');

readable.getReader().read().then((result) => {
  console.log('readable', result.value);
});
copy
```

####  `stream.addAbortSignal(signal, stream)`[#](https://nodejs.org/docs/latest/api/stream.html#streamaddabortsignalsignal-stream)
Added in: v15.4.0History Version | Changes
---|---
v19.7.0, v18.16.0 | Added support for `ReadableStream` and `WritableStream`.
  * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) A signal representing possible cancellation
  * `stream` [`<Stream>`](https://nodejs.org/docs/latest/api/stream.html#stream) | [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream) | [`<WritableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-writablestream) A stream to attach a signal to.


Attaches an AbortSignal to a readable or writeable stream. This lets code control stream destruction using an `AbortController`.
Calling `abort` on the `AbortController` corresponding to the passed `AbortSignal` will behave the same way as calling `.destroy(new AbortError())` on the stream, and `controller.error(new AbortError())` for webstreams.
```
const fs = require('node:fs');

const controller = new AbortController();
const read = addAbortSignal(
  controller.signal,
  fs.createReadStream(('object.json')),
);
// Later, abort the operation closing the stream
controller.abort();
copy
```

Or using an `AbortSignal` with a readable stream as an async iterable:
```
const controller = new AbortController();
setTimeout(() => controller.abort(), 10_000); // set a timeout
const stream = addAbortSignal(
  controller.signal,
  fs.createReadStream(('object.json')),
);
(async () => {
  try {
    for await (const chunk of stream) {
      await process(chunk);
    }
  } catch (e) {
    if (e.name === 'AbortError') {
      // The operation was cancelled
    } else {
      throw e;
    }
  }
})();
copy
```

Or using an `AbortSignal` with a ReadableStream:
```
const controller = new AbortController();
const rs = new ReadableStream({
  start(controller) {
    controller.enqueue('hello');
    controller.enqueue('world');
    controller.close();
  },
});

addAbortSignal(controller.signal, rs);

finished(rs, (err) => {
  if (err) {
    if (err.name === 'AbortError') {
      // The operation was cancelled
    }
  }
});

const reader = rs.getReader();

reader.read().then(({ value, done }) => {
  console.log(value); // hello
  console.log(done); // false
  controller.abort();
});
copy
```

####  `stream.getDefaultHighWaterMark(objectMode)`[#](https://nodejs.org/docs/latest/api/stream.html#streamgetdefaulthighwatermarkobjectmode)
Added in: v19.9.0, v18.17.0
  * `objectMode`
  * Returns:


Returns the default highWaterMark used by streams. Defaults to `65536` (64 KiB), or `16` for `objectMode`.
####  `stream.setDefaultHighWaterMark(objectMode, value)`[#](https://nodejs.org/docs/latest/api/stream.html#streamsetdefaulthighwatermarkobjectmode-value)
Added in: v19.9.0, v18.17.0
  * `objectMode`
  * `value`


Sets the default highWaterMark used by streams.
### API for stream implementers[#](https://nodejs.org/docs/latest/api/stream.html#api-for-stream-implementers)
The `node:stream` module API has been designed to make it possible to easily implement streams using JavaScript's prototypal inheritance model.
First, a stream developer would declare a new JavaScript class that extends one of the four basic stream classes (`stream.Writable`, `stream.Readable`, `stream.Duplex`, or `stream.Transform`), making sure they call the appropriate parent class constructor:
```
const { Writable } = require('node:stream');

class MyWritable extends Writable {
  constructor({ highWaterMark, ...options }) {
    super({ highWaterMark });
    // ...
  }
}
copy
```

When extending streams, keep in mind what options the user can and should provide before forwarding these to the base constructor. For example, if the implementation makes assumptions in regard to the `autoDestroy` and `emitClose` options, do not allow the user to override these. Be explicit about what options are forwarded instead of implicitly forwarding all options.
The new stream class must then implement one or more specific methods, depending on the type of stream being created, as detailed in the chart below:
Use-case | Class | Method(s) to implement
---|---|---
Reading only | [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) | [`_read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize)
Writing only | [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) |  [`_write()`](https://nodejs.org/docs/latest/api/stream.html#writable_writechunk-encoding-callback), [`_writev()`](https://nodejs.org/docs/latest/api/stream.html#writable_writevchunks-callback), [`_final()`](https://nodejs.org/docs/latest/api/stream.html#writable_finalcallback)
Reading and writing | [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) |  [`_read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize), [`_write()`](https://nodejs.org/docs/latest/api/stream.html#writable_writechunk-encoding-callback), [`_writev()`](https://nodejs.org/docs/latest/api/stream.html#writable_writevchunks-callback), [`_final()`](https://nodejs.org/docs/latest/api/stream.html#writable_finalcallback)
Operate on written data, then read the result | [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform) |  [`_transform()`](https://nodejs.org/docs/latest/api/stream.html#transform_transformchunk-encoding-callback), [`_flush()`](https://nodejs.org/docs/latest/api/stream.html#transform_flushcallback), [`_final()`](https://nodejs.org/docs/latest/api/stream.html#writable_finalcallback)
The implementation code for a stream should _never_ call the "public" methods of a stream that are intended for use by consumers (as described in the [API for stream consumers](https://nodejs.org/docs/latest/api/stream.html#api-for-stream-consumers) section). Doing so may lead to adverse side effects in application code consuming the stream.
Avoid overriding public methods such as `write()`, `end()`, `cork()`, `uncork()`, `read()` and `destroy()`, or emitting internal events such as `'error'`, `'data'`, `'end'`, `'finish'` and `'close'` through `.emit()`. Doing so can break current and future stream invariants leading to behavior and/or compatibility issues with other streams, stream utilities, and user expectations.
#### Simplified construction[#](https://nodejs.org/docs/latest/api/stream.html#simplified-construction)
Added in: v1.2.0
For many simple cases, it is possible to create a stream without relying on inheritance. This can be accomplished by directly creating instances of the `stream.Writable`, `stream.Readable`, `stream.Duplex`, or `stream.Transform` objects and passing appropriate methods as constructor options.
```
const { Writable } = require('node:stream');

const myWritable = new Writable({
  construct(callback) {
    // Initialize state and load resources...
  },
  write(chunk, encoding, callback) {
    // ...
  },
  destroy() {
    // Free resources...
  },
});
copy
```

#### Implementing a writable stream[#](https://nodejs.org/docs/latest/api/stream.html#implementing-a-writable-stream)
The `stream.Writable` class is extended to implement a [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) stream.
Custom `Writable` streams _must_ call the `new stream.Writable([options])` constructor and implement the `writable._write()` and/or `writable._writev()` method.
#####  `new stream.Writable([options])`[#](https://nodejs.org/docs/latest/api/stream.html#new-streamwritableoptions)
History Version | Changes
---|---
v22.0.0 | bump default highWaterMark.
v15.5.0 | support passing in an AbortSignal.
v14.0.0 | Change `autoDestroy` option default to `true`.
