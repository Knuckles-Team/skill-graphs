Custom `Duplex` streams _must_ call the `new stream.Duplex([options])` constructor and implement _both_ the [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) and `writable._write()` methods.
#####  `new stream.Duplex(options)`[#](https://nodejs.org/docs/latest/api/stream.html#new-streamduplexoptions)
History Version | Changes
---|---
v8.4.0 | The `readableHighWaterMark` and `writableHighWaterMark` options are supported now.
  * `options` `Writable` and `Readable` constructors. Also has the following fields:
    * `allowHalfOpen` `false`, then the stream will automatically end the writable side when the readable side ends. **Default:** `true`.
    * `readable` `Duplex` should be readable. **Default:** `true`.
    * `writable` `Duplex` should be writable. **Default:** `true`.
    * `readableObjectMode` `objectMode` for readable side of the stream. Has no effect if `objectMode` is `true`. **Default:** `false`.
    * `writableObjectMode` `objectMode` for writable side of the stream. Has no effect if `objectMode` is `true`. **Default:** `false`.
    * `readableHighWaterMark` `highWaterMark` for the readable side of the stream. Has no effect if `highWaterMark` is provided.
    * `writableHighWaterMark` `highWaterMark` for the writable side of the stream. Has no effect if `highWaterMark` is provided.

```
const { Duplex } = require('node:stream');

class MyDuplex extends Duplex {
  constructor(options) {
    super(options);
    // ...
  }
}
copy
```

Or, when using pre-ES6 style constructors:
```
const { Duplex } = require('node:stream');
const util = require('node:util');

function MyDuplex(options) {
  if (!(this instanceof MyDuplex))
    return new MyDuplex(options);
  Duplex.call(this, options);
}
util.inherits(MyDuplex, Duplex);
copy
```

Or, using the simplified constructor approach:
```
const { Duplex } = require('node:stream');

const myDuplex = new Duplex({
  read(size) {
    // ...
  },
  write(chunk, encoding, callback) {
    // ...
  },
});
copy
```

When using pipeline:
```
const { Transform, pipeline } = require('node:stream');
const fs = require('node:fs');

pipeline(
  fs.createReadStream('object.json')
    .setEncoding('utf8'),
  new Transform({
    decodeStrings: false, // Accept string input rather than Buffers
    construct(callback) {
      this.data = '';
      callback();
    },
    transform(chunk, encoding, callback) {
      this.data += chunk;
      callback();
    },
    flush(callback) {
      try {
        // Make sure is valid json.
        JSON.parse(this.data);
        this.push(this.data);
        callback();
      } catch (err) {
        callback(err);
      }
    },
  }),
  fs.createWriteStream('valid-object.json'),
  (err) => {
    if (err) {
      console.error('failed', err);
    } else {
      console.log('completed');
    }
  },
);
copy
```

##### An example duplex stream[#](https://nodejs.org/docs/latest/api/stream.html#an-example-duplex-stream)
The following illustrates a simple example of a `Duplex` stream that wraps a hypothetical lower-level source object to which data can be written, and from which data can be read, albeit using an API that is not compatible with Node.js streams. The following illustrates a simple example of a `Duplex` stream that buffers incoming written data via the [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) interface that is read back out via the [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) interface.
```
const { Duplex } = require('node:stream');
const kSource = Symbol('source');

class MyDuplex extends Duplex {
  constructor(source, options) {
    super(options);
    this[kSource] = source;
  }

  _write(chunk, encoding, callback) {
    // The underlying source only deals with strings.
    if (Buffer.isBuffer(chunk))
      chunk = chunk.toString();
    this[kSource].writeSomeData(chunk);
    callback();
  }

  _read(size) {
    this[kSource].fetchSomeData(size, (data, encoding) => {
      this.push(Buffer.from(data, encoding));
    });
  }
}
copy
```

The most important aspect of a `Duplex` stream is that the `Readable` and `Writable` sides operate independently of one another despite co-existing within a single object instance.
##### Object mode duplex streams[#](https://nodejs.org/docs/latest/api/stream.html#object-mode-duplex-streams)
For `Duplex` streams, `objectMode` can be set exclusively for either the `Readable` or `Writable` side using the `readableObjectMode` and `writableObjectMode` options respectively.
In the following example, for instance, a new `Transform` stream (which is a type of [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) stream) is created that has an object mode `Writable` side that accepts JavaScript numbers that are converted to hexadecimal strings on the `Readable` side.
```
const { Transform } = require('node:stream');

// All Transform streams are also Duplex Streams.
const myTransform = new Transform({
  writableObjectMode: true,

  transform(chunk, encoding, callback) {
    // Coerce the chunk to a number if necessary.
    chunk |= 0;

    // Transform the chunk into something else.
    const data = chunk.toString(16);

    // Push the data onto the readable queue.
    callback(null, '0'.repeat(data.length % 2) + data);
  },
});

myTransform.setEncoding('ascii');
myTransform.on('data', (chunk) => console.log(chunk));

myTransform.write(1);
// Prints: 01
myTransform.write(10);
// Prints: 0a
myTransform.write(100);
// Prints: 64
copy
```

#### Implementing a transform stream[#](https://nodejs.org/docs/latest/api/stream.html#implementing-a-transform-stream)
A [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform) stream is a [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) stream where the output is computed in some way from the input. Examples include [zlib](https://nodejs.org/docs/latest/api/zlib.html) streams or [crypto](https://nodejs.org/docs/latest/api/crypto.html) streams that compress, encrypt, or decrypt data.
There is no requirement that the output be the same size as the input, the same number of chunks, or arrive at the same time. For example, a `Hash` stream will only ever have a single chunk of output which is provided when the input is ended. A `zlib` stream will produce output that is either much smaller or much larger than its input.
The `stream.Transform` class is extended to implement a [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform) stream.
The `stream.Transform` class prototypically inherits from `stream.Duplex` and implements its own versions of the `writable._write()` and [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) methods. Custom `Transform` implementations _must_ implement the [`transform._transform()`](https://nodejs.org/docs/latest/api/stream.html#transform_transformchunk-encoding-callback) method and _may_ also implement the [`transform._flush()`](https://nodejs.org/docs/latest/api/stream.html#transform_flushcallback) method.
Care must be taken when using `Transform` streams in that data written to the stream can cause the `Writable` side of the stream to become paused if the output on the `Readable` side is not consumed.
#####  `new stream.Transform([options])`[#](https://nodejs.org/docs/latest/api/stream.html#new-streamtransformoptions)
  * `options` `Writable` and `Readable` constructors. Also has the following fields:
    * `transform` [`stream._transform()`](https://nodejs.org/docs/latest/api/stream.html#transform_transformchunk-encoding-callback) method.
    * `flush` [`stream._flush()`](https://nodejs.org/docs/latest/api/stream.html#transform_flushcallback) method.

```
const { Transform } = require('node:stream');

class MyTransform extends Transform {
  constructor(options) {
    super(options);
    // ...
  }
}
copy
```

Or, when using pre-ES6 style constructors:
```
const { Transform } = require('node:stream');
const util = require('node:util');

function MyTransform(options) {
  if (!(this instanceof MyTransform))
    return new MyTransform(options);
  Transform.call(this, options);
}
util.inherits(MyTransform, Transform);
copy
```

Or, using the simplified constructor approach:
```
const { Transform } = require('node:stream');

const myTransform = new Transform({
  transform(chunk, encoding, callback) {
    // ...
  },
});
copy
```

##### Event: `'end'`[#](https://nodejs.org/docs/latest/api/stream.html#event-end-1)
The [`'end'`](https://nodejs.org/docs/latest/api/stream.html#event-end) event is from the `stream.Readable` class. The `'end'` event is emitted after all data has been output, which occurs after the callback in [`transform._flush()`](https://nodejs.org/docs/latest/api/stream.html#transform_flushcallback) has been called. In the case of an error, `'end'` should not be emitted.
##### Event: `'finish'`[#](https://nodejs.org/docs/latest/api/stream.html#event-finish-1)
The [`'finish'`](https://nodejs.org/docs/latest/api/stream.html#event-finish) event is from the `stream.Writable` class. The `'finish'` event is emitted after [`stream.end()`](https://nodejs.org/docs/latest/api/stream.html#writableendchunk-encoding-callback) is called and all chunks have been processed by [`stream._transform()`](https://nodejs.org/docs/latest/api/stream.html#transform_transformchunk-encoding-callback). In the case of an error, `'finish'` should not be emitted.
#####  `transform._flush(callback)`[#](https://nodejs.org/docs/latest/api/stream.html#transform-flushcallback)
  * `callback`


This function MUST NOT be called by application code directly. It should be implemented by child classes, and called by the internal `Readable` class methods only.
In some cases, a transform operation may need to emit an additional bit of data at the end of the stream. For example, a `zlib` compression stream will store an amount of internal state used to optimally compress the output. When the stream ends, however, that additional data needs to be flushed so that the compressed data will be complete.
Custom [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform) implementations _may_ implement the `transform._flush()` method. This will be called when there is no more written data to be consumed, but before the [`'end'`](https://nodejs.org/docs/latest/api/stream.html#event-end) event is emitted signaling the end of the [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) stream.
Within the `transform._flush()` implementation, the `transform.push()` method may be called zero or more times, as appropriate. The `callback` function must be called when the flush operation is complete.
The `transform._flush()` method is prefixed with an underscore because it is internal to the class that defines it, and should never be called directly by user programs.
#####  `transform._transform(chunk, encoding, callback)`[#](https://nodejs.org/docs/latest/api/stream.html#transform-transformchunk-encoding-callback)
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer` to be transformed, converted from the `string` passed to [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback). If the stream's `decodeStrings` option is `false` or the stream is operating in object mode, the chunk will not be converted & will be whatever was passed to [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback).
  * `encoding` `'buffer'`. Ignore it in that case.
  * `callback` `chunk` has been processed.


This function MUST NOT be called by application code directly. It should be implemented by child classes, and called by the internal `Readable` class methods only.
All `Transform` stream implementations must provide a `_transform()` method to accept input and produce output. The `transform._transform()` implementation handles the bytes being written, computes an output, then passes that output off to the readable portion using the `transform.push()` method.
The `transform.push()` method may be called zero or more times to generate output from a single input chunk, depending on how much is to be output as a result of the chunk.
It is possible that no output is generated from any given chunk of input data.
The `callback` function must be called only when the current chunk is completely consumed. The first argument passed to the `callback` must be an `Error` object if an error occurred while processing the input or `null` otherwise. If a second argument is passed to the `callback`, it will be forwarded on to the `transform.push()` method, but only if the first argument is falsy. In other words, the following are equivalent:
```
transform.prototype._transform = function(data, encoding, callback) {
  this.push(data);
  callback();
};

transform.prototype._transform = function(data, encoding, callback) {
  callback(null, data);
};
copy
```

The `transform._transform()` method is prefixed with an underscore because it is internal to the class that defines it, and should never be called directly by user programs.
`transform._transform()` is never called in parallel; streams implement a queue mechanism, and to receive the next chunk, `callback` must be called, either synchronously or asynchronously.
##### Class: `stream.PassThrough`[#](https://nodejs.org/docs/latest/api/stream.html#class-streampassthrough)
The `stream.PassThrough` class is a trivial implementation of a [`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform) stream that simply passes the input bytes across to the output. Its purpose is primarily for examples and testing, but there are some use cases where `stream.PassThrough` is useful as a building block for novel sorts of streams.
### Additional notes[#](https://nodejs.org/docs/latest/api/stream.html#additional-notes)
#### Streams compatibility with async generators and async iterators[#](https://nodejs.org/docs/latest/api/stream.html#streams-compatibility-with-async-generators-and-async-iterators)
With the support of async generators and iterators in JavaScript, async generators are effectively a first-class language-level stream construct at this point.
Some common interop cases of using Node.js streams with async generators and async iterators are provided below.
##### Consuming readable streams with async iterators[#](https://nodejs.org/docs/latest/api/stream.html#consuming-readable-streams-with-async-iterators)
```
(async function() {
  for await (const chunk of readable) {
    console.log(chunk);
  }
})();
copy
```

Async iterators register a permanent error handler on the stream to prevent any unhandled post-destroy errors.
##### Creating readable streams with async generators[#](https://nodejs.org/docs/latest/api/stream.html#creating-readable-streams-with-async-generators)
A Node.js readable stream can be created from an asynchronous generator using the `Readable.from()` utility method:
```
const { Readable } = require('node:stream');

const ac = new AbortController();
const signal = ac.signal;

async function * generate() {
  yield 'a';
  await someLongRunningFn({ signal });
  yield 'b';
  yield 'c';
}

const readable = Readable.from(generate());
readable.on('close', () => {
  ac.abort();
});

readable.on('data', (chunk) => {
  console.log(chunk);
});
copy
```

##### Piping to writable streams from async iterators[#](https://nodejs.org/docs/latest/api/stream.html#piping-to-writable-streams-from-async-iterators)
When writing to a writable stream from an async iterator, ensure correct handling of backpressure and errors. [`stream.pipeline()`](https://nodejs.org/docs/latest/api/stream.html#streampipelinesource-transforms-destination-callback) abstracts away the handling of backpressure and backpressure-related errors:
```
const fs = require('node:fs');
const { pipeline } = require('node:stream');
const { pipeline: pipelinePromise } = require('node:stream/promises');

const writable = fs.createWriteStream('./file');

const ac = new AbortController();
const signal = ac.signal;

const iterator = createIterator({ signal });

// Callback Pattern
pipeline(iterator, writable, (err, value) => {
  if (err) {
    console.error(err);
  } else {
    console.log(value, 'value returned');
  }
}).on('close', () => {
  ac.abort();
});

// Promise Pattern
pipelinePromise(iterator, writable)
  .then((value) => {
    console.log(value, 'value returned');
  })
  .catch((err) => {
    console.error(err);
    ac.abort();
  });
copy
```

#### Compatibility with older Node.js versions[#](https://nodejs.org/docs/latest/api/stream.html#compatibility-with-older-nodejs-versions)
Prior to Node.js 0.10, the `Readable` stream interface was simpler, but also less powerful and less useful.
  * Rather than waiting for calls to the [`stream.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize) method, [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) events would begin emitting immediately. Applications that would need to perform some amount of work to decide how to handle data were required to store read data into buffers so the data would not be lost.
  * The [`stream.pause()`](https://nodejs.org/docs/latest/api/stream.html#readablepause) method was advisory, rather than guaranteed. This meant that it was still necessary to be prepared to receive [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) events _even when the stream was in a paused state_.


In Node.js 0.10, the [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) class was added. For backward compatibility with older Node.js programs, `Readable` streams switch into "flowing mode" when a [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) event handler is added, or when the [`stream.resume()`](https://nodejs.org/docs/latest/api/stream.html#readableresume) method is called. The effect is that, even when not using the new [`stream.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize) method and [`'readable'`](https://nodejs.org/docs/latest/api/stream.html#event-readable) event, it is no longer necessary to worry about losing [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) chunks.
While most applications will continue to function normally, this introduces an edge case in the following conditions:
  * No [`'data'`](https://nodejs.org/docs/latest/api/stream.html#event-data) event listener is added.
  * The [`stream.resume()`](https://nodejs.org/docs/latest/api/stream.html#readableresume) method is never called.
  * The stream is not piped to any writable destination.


For example, consider the following code:
```
// WARNING!  BROKEN!
net.createServer((socket) => {

  // We add an 'end' listener, but never consume the data.
  socket.on('end', () => {
    // It will never get here.
    socket.end('The message was received but was not processed.\n');
  });

}).listen(1337);
copy
```

Prior to Node.js 0.10, the incoming message data would be simply discarded. However, in Node.js 0.10 and beyond, the socket remains paused forever.
The workaround in this situation is to call the [`stream.resume()`](https://nodejs.org/docs/latest/api/stream.html#readableresume) method to begin the flow of data:
```
// Workaround.
net.createServer((socket) => {
  socket.on('end', () => {
    socket.end('The message was received but was not processed.\n');
  });

  // Start the flow of data, discarding it.
  socket.resume();
}).listen(1337);
copy
```

In addition to new `Readable` streams switching into flowing mode, pre-0.10 style streams can be wrapped in a `Readable` class using the [`readable.wrap()`](https://nodejs.org/docs/latest/api/stream.html#readablewrapstream) method.
####  `readable.read(0)`[#](https://nodejs.org/docs/latest/api/stream.html#readableread0)
There are some cases where it is necessary to trigger a refresh of the underlying readable stream mechanisms, without actually consuming any data. In such cases, it is possible to call `readable.read(0)`, which will always return `null`.
If the internal read buffer is below the `highWaterMark`, and the stream is not currently reading, then calling `stream.read(0)` will trigger a low-level [`stream._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) call.
While most applications will almost never need to do this, there are situations within Node.js where this is done, particularly in the `Readable` stream class internals.
####  `readable.push('')`[#](https://nodejs.org/docs/latest/api/stream.html#readablepush)
Use of `readable.push('')` is not recommended.
Pushing a zero-byte [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer), _is_ a call to [`readable.push()`](https://nodejs.org/docs/latest/api/stream.html#readablepushchunk-encoding), the call will end the reading process. However, because the argument is an empty string, no data is added to the readable buffer so there is nothing for a user to consume.
####  `highWaterMark` discrepancy after calling `readable.setEncoding()`[#](https://nodejs.org/docs/latest/api/stream.html#highwatermark-discrepancy-after-calling-readablesetencoding)
The use of `readable.setEncoding()` will change the behavior of how the `highWaterMark` operates in non-object mode.
Typically, the size of the current buffer is measured against the `highWaterMark` in _bytes_. However, after `setEncoding()` is called, the comparison function will begin to measure the buffer's size in _characters_.
This is not a problem in common cases with `latin1` or `ascii`. But it is advised to be mindful about this behavior when working with strings that could contain multi-byte characters.
