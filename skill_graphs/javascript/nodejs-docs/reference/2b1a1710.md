v11.2.0, v10.16.0 | Add `autoDestroy` option to automatically `destroy()` the stream when it emits `'finish'` or errors.
v10.0.0 | Add `emitClose` option to specify if `'close'` is emitted on destroy.
  * `options`
    * `highWaterMark` [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) starts returning `false`. **Default:** `65536` (64 KiB), or `16` for `objectMode` streams.
    * `decodeStrings` `string`s passed to [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) to `Buffer`s (with the encoding specified in the [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) call) before passing them to [`stream._write()`](https://nodejs.org/docs/latest/api/stream.html#writable_writechunk-encoding-callback). Other types of data are not converted (i.e. `Buffer`s are not decoded into `string`s). Setting to false will prevent `string`s from being converted. **Default:** `true`.
    * `defaultEncoding` [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback). **Default:** `'utf8'`.
    * `objectMode` [`stream.write(anyObj)`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) is a valid operation. When set, it becomes possible to write JavaScript values other than string, [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer), **Default:** `false`.
    * `emitClose` `'close'` after it has been destroyed. **Default:** `true`.
    * `write` [`stream._write()`](https://nodejs.org/docs/latest/api/stream.html#writable_writechunk-encoding-callback) method.
    * `writev` [`stream._writev()`](https://nodejs.org/docs/latest/api/stream.html#writable_writevchunks-callback) method.
    * `destroy` [`stream._destroy()`](https://nodejs.org/docs/latest/api/stream.html#writable_destroyerr-callback) method.
    * `final` [`stream._final()`](https://nodejs.org/docs/latest/api/stream.html#writable_finalcallback) method.
    * `construct` [`stream._construct()`](https://nodejs.org/docs/latest/api/stream.html#writable_constructcallback) method.
    * `autoDestroy` `.destroy()` on itself after ending. **Default:** `true`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) A signal representing possible cancellation.

```
const { Writable } = require('node:stream');

class MyWritable extends Writable {
  constructor(options) {
    // Calls the stream.Writable() constructor.
    super(options);
    // ...
  }
}
copy
```

Or, when using pre-ES6 style constructors:
```
const { Writable } = require('node:stream');
const util = require('node:util');

function MyWritable(options) {
  if (!(this instanceof MyWritable))
    return new MyWritable(options);
  Writable.call(this, options);
}
util.inherits(MyWritable, Writable);
copy
```

Or, using the simplified constructor approach:
```
const { Writable } = require('node:stream');

const myWritable = new Writable({
  write(chunk, encoding, callback) {
    // ...
  },
  writev(chunks, callback) {
    // ...
  },
});
copy
```

Calling `abort` on the `AbortController` corresponding to the passed `AbortSignal` will behave the same way as calling `.destroy(new AbortError())` on the writeable stream.
```
const { Writable } = require('node:stream');

const controller = new AbortController();
const myWritable = new Writable({
  write(chunk, encoding, callback) {
    // ...
  },
  writev(chunks, callback) {
    // ...
  },
  signal: controller.signal,
});
// Later, abort the operation closing the stream
controller.abort();
copy
```

#####  `writable._construct(callback)`[#](https://nodejs.org/docs/latest/api/stream.html#writable-constructcallback)
Added in: v15.0.0
  * `callback`


The `_construct()` method MUST NOT be called directly. It may be implemented by child classes, and if so, will be called by the internal `Writable` class methods only.
This optional function will be called in a tick after the stream constructor has returned, delaying any `_write()`, `_final()` and `_destroy()` calls until `callback` is called. This is useful to initialize state or asynchronously initialize resources before the stream can be used.
```
const { Writable } = require('node:stream');
const fs = require('node:fs');

class WriteStream extends Writable {
  constructor(filename) {
    super();
    this.filename = filename;
    this.fd = null;
  }
  _construct(callback) {
    fs.open(this.filename, 'w', (err, fd) => {
      if (err) {
        callback(err);
      } else {
        this.fd = fd;
        callback();
      }
    });
  }
  _write(chunk, encoding, callback) {
    fs.write(this.fd, chunk, callback);
  }
  _destroy(err, callback) {
    if (this.fd) {
      fs.close(this.fd, (er) => callback(er || err));
    } else {
      callback(err);
    }
  }
}
copy
```

#####  `writable._write(chunk, encoding, callback)`[#](https://nodejs.org/docs/latest/api/stream.html#writable-writechunk-encoding-callback)
History Version | Changes
---|---
v12.11.0 | _write() is optional when providing _writev().
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer` to be written, converted from the `string` passed to [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback). If the stream's `decodeStrings` option is `false` or the stream is operating in object mode, the chunk will not be converted & will be whatever was passed to [`stream.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback).
  * `encoding` `encoding` is the character encoding of that string. If chunk is a `Buffer`, or if the stream is operating in object mode, `encoding` may be ignored.
  * `callback`


All `Writable` stream implementations must provide a [`writable._write()`](https://nodejs.org/docs/latest/api/stream.html#writable_writechunk-encoding-callback) and/or [`writable._writev()`](https://nodejs.org/docs/latest/api/stream.html#writable_writevchunks-callback) method to send data to the underlying resource.
[`Transform`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform) streams provide their own implementation of the [`writable._write()`](https://nodejs.org/docs/latest/api/stream.html#writable_writechunk-encoding-callback).
This function MUST NOT be called by application code directly. It should be implemented by child classes, and called by the internal `Writable` class methods only.
The `callback` function must be called synchronously inside of `writable._write()` or asynchronously (i.e. different tick) to signal either that the write completed successfully or failed with an error. The first argument passed to the `callback` must be the `Error` object if the call failed or `null` if the write succeeded.
All calls to `writable.write()` that occur between the time `writable._write()` is called and the `callback` is called will cause the written data to be buffered. When the `callback` is invoked, the stream might emit a [`'drain'`](https://nodejs.org/docs/latest/api/stream.html#event-drain) event. If a stream implementation is capable of processing multiple chunks of data at once, the `writable._writev()` method should be implemented.
If the `decodeStrings` property is explicitly set to `false` in the constructor options, then `chunk` will remain the same object that is passed to `.write()`, and may be a string rather than a `Buffer`. This is to support implementations that have an optimized handling for certain string data encodings. In that case, the `encoding` argument will indicate the character encoding of the string. Otherwise, the `encoding` argument can be safely ignored.
The `writable._write()` method is prefixed with an underscore because it is internal to the class that defines it, and should never be called directly by user programs.
#####  `writable._writev(chunks, callback)`[#](https://nodejs.org/docs/latest/api/stream.html#writable-writevchunks-callback)
  * `chunks`
    * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `chunk` will be a string if the `Writable` was created with the `decodeStrings` option set to `false` and a string was passed to `write()`.
    * `encoding` `chunk`. If `chunk` is a `Buffer`, the `encoding` will be `'buffer'`.
  * `callback`


This function MUST NOT be called by application code directly. It should be implemented by child classes, and called by the internal `Writable` class methods only.
The `writable._writev()` method may be implemented in addition or alternatively to `writable._write()` in stream implementations that are capable of processing multiple chunks of data at once. If implemented and if there is buffered data from previous writes, `_writev()` will be called instead of `_write()`.
The `writable._writev()` method is prefixed with an underscore because it is internal to the class that defines it, and should never be called directly by user programs.
#####  `writable._destroy(err, callback)`[#](https://nodejs.org/docs/latest/api/stream.html#writable-destroyerr-callback)
Added in: v8.0.0
  * `err`
  * `callback`


The `_destroy()` method is called by [`writable.destroy()`](https://nodejs.org/docs/latest/api/stream.html#writabledestroyerror). It can be overridden by child classes but it **must not** be called directly.
#####  `writable._final(callback)`[#](https://nodejs.org/docs/latest/api/stream.html#writable-finalcallback)
Added in: v8.0.0
  * `callback`


The `_final()` method **must not** be called directly. It may be implemented by child classes, and if so, will be called by the internal `Writable` class methods only.
This optional function will be called before the stream closes, delaying the `'finish'` event until `callback` is called. This is useful to close resources or write buffered data before a stream ends.
##### Errors while writing[#](https://nodejs.org/docs/latest/api/stream.html#errors-while-writing)
Errors occurring during the processing of the [`writable._write()`](https://nodejs.org/docs/latest/api/stream.html#writable_writechunk-encoding-callback), [`writable._writev()`](https://nodejs.org/docs/latest/api/stream.html#writable_writevchunks-callback) and [`writable._final()`](https://nodejs.org/docs/latest/api/stream.html#writable_finalcallback) methods must be propagated by invoking the callback and passing the error as the first argument. Throwing an `Error` from within these methods or manually emitting an `'error'` event results in undefined behavior.
If a `Readable` stream pipes into a `Writable` stream when `Writable` emits an error, the `Readable` stream will be unpiped.
```
const { Writable } = require('node:stream');

const myWritable = new Writable({
  write(chunk, encoding, callback) {
    if (chunk.toString().indexOf('a') >= 0) {
      callback(new Error('chunk is invalid'));
    } else {
      callback();
    }
  },
});
copy
```

##### An example writable stream[#](https://nodejs.org/docs/latest/api/stream.html#an-example-writable-stream)
The following illustrates a rather simplistic (and somewhat pointless) custom `Writable` stream implementation. While this specific `Writable` stream instance is not of any real particular usefulness, the example illustrates each of the required elements of a custom [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable) stream instance:
```
const { Writable } = require('node:stream');

class MyWritable extends Writable {
  _write(chunk, encoding, callback) {
    if (chunk.toString().indexOf('a') >= 0) {
      callback(new Error('chunk is invalid'));
    } else {
      callback();
    }
  }
}
copy
```

##### Decoding buffers in a writable stream[#](https://nodejs.org/docs/latest/api/stream.html#decoding-buffers-in-a-writable-stream)
Decoding buffers is a common task, for instance, when using transformers whose input is a string. This is not a trivial process when using multi-byte characters encoding, such as UTF-8. The following example shows how to decode multi-byte strings using `StringDecoder` and [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable).
```
const { Writable } = require('node:stream');
const { StringDecoder } = require('node:string_decoder');

class StringWritable extends Writable {
  constructor(options) {
    super(options);
    this._decoder = new StringDecoder(options?.defaultEncoding);
    this.data = '';
  }
  _write(chunk, encoding, callback) {
    if (encoding === 'buffer') {
      chunk = this._decoder.write(chunk);
    }
    this.data += chunk;
    callback();
  }
  _final(callback) {
    this.data += this._decoder.end();
    callback();
  }
}

const euro = [[0xE2, 0x82], [0xAC]].map(Buffer.from);
const w = new StringWritable();

w.write('currency: ');
w.write(euro[0]);
w.end(euro[1]);

console.log(w.data); // currency: €
copy
```

#### Implementing a readable stream[#](https://nodejs.org/docs/latest/api/stream.html#implementing-a-readable-stream)
The `stream.Readable` class is extended to implement a [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) stream.
Custom `Readable` streams _must_ call the `new stream.Readable([options])` constructor and implement the [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) method.
#####  `new stream.Readable([options])`[#](https://nodejs.org/docs/latest/api/stream.html#new-streamreadableoptions)
History Version | Changes
---|---
v22.0.0 | bump default highWaterMark.
v15.5.0 | support passing in an AbortSignal.
v14.0.0 | Change `autoDestroy` option default to `true`.
v11.2.0, v10.16.0 | Add `autoDestroy` option to automatically `destroy()` the stream when it emits `'end'` or errors.
  * `options`
    * `highWaterMark` [number of bytes](https://nodejs.org/docs/latest/api/stream.html#highwatermark-discrepancy-after-calling-readablesetencoding) to store in the internal buffer before ceasing to read from the underlying resource. **Default:** `65536` (64 KiB), or `16` for `objectMode` streams.
    * `encoding` **Default:** `null`.
    * `objectMode` [`stream.read(n)`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize) returns a single value instead of a `Buffer` of size `n`. **Default:** `false`.
    * `emitClose` `'close'` after it has been destroyed. **Default:** `true`.
    * `read` [`stream._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) method.
    * `destroy` [`stream._destroy()`](https://nodejs.org/docs/latest/api/stream.html#readable_destroyerr-callback) method.
    * `construct` [`stream._construct()`](https://nodejs.org/docs/latest/api/stream.html#readable_constructcallback) method.
    * `autoDestroy` `.destroy()` on itself after ending. **Default:** `true`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) A signal representing possible cancellation.

```
const { Readable } = require('node:stream');

class MyReadable extends Readable {
  constructor(options) {
    // Calls the stream.Readable(options) constructor.
    super(options);
    // ...
  }
}
copy
```

Or, when using pre-ES6 style constructors:
```
const { Readable } = require('node:stream');
const util = require('node:util');

function MyReadable(options) {
  if (!(this instanceof MyReadable))
    return new MyReadable(options);
  Readable.call(this, options);
}
util.inherits(MyReadable, Readable);
copy
```

Or, using the simplified constructor approach:
```
const { Readable } = require('node:stream');

const myReadable = new Readable({
  read(size) {
    // ...
  },
});
copy
```

Calling `abort` on the `AbortController` corresponding to the passed `AbortSignal` will behave the same way as calling `.destroy(new AbortError())` on the readable created.
```
const { Readable } = require('node:stream');
const controller = new AbortController();
const read = new Readable({
  read(size) {
    // ...
  },
  signal: controller.signal,
});
// Later, abort the operation closing the stream
controller.abort();
copy
```

#####  `readable._construct(callback)`[#](https://nodejs.org/docs/latest/api/stream.html#readable-constructcallback)
Added in: v15.0.0
  * `callback`


The `_construct()` method MUST NOT be called directly. It may be implemented by child classes, and if so, will be called by the internal `Readable` class methods only.
This optional function will be scheduled in the next tick by the stream constructor, delaying any `_read()` and `_destroy()` calls until `callback` is called. This is useful to initialize state or asynchronously initialize resources before the stream can be used.
```
const { Readable } = require('node:stream');
const fs = require('node:fs');

class ReadStream extends Readable {
  constructor(filename) {
    super();
    this.filename = filename;
    this.fd = null;
  }
  _construct(callback) {
    fs.open(this.filename, (err, fd) => {
      if (err) {
        callback(err);
      } else {
        this.fd = fd;
        callback();
      }
    });
  }
  _read(n) {
    const buf = Buffer.alloc(n);
    fs.read(this.fd, buf, 0, n, null, (err, bytesRead) => {
      if (err) {
        this.destroy(err);
      } else {
        this.push(bytesRead > 0 ? buf.slice(0, bytesRead) : null);
      }
    });
  }
  _destroy(err, callback) {
    if (this.fd) {
      fs.close(this.fd, (er) => callback(er || err));
    } else {
      callback(err);
    }
  }
}
copy
```

#####  `readable._read(size)`[#](https://nodejs.org/docs/latest/api/stream.html#readable-readsize)
Added in: v0.9.4
  * `size`


This function MUST NOT be called by application code directly. It should be implemented by child classes, and called by the internal `Readable` class methods only.
All `Readable` stream implementations must provide an implementation of the [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) method to fetch data from the underlying resource.
When [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) is called, if data is available from the resource, the implementation should begin pushing that data into the read queue using the [`this.push(dataChunk)`](https://nodejs.org/docs/latest/api/stream.html#readablepushchunk-encoding) method. `_read()` will be called again after each call to [`this.push(dataChunk)`](https://nodejs.org/docs/latest/api/stream.html#readablepushchunk-encoding) once the stream is ready to accept more data. `_read()` may continue reading from the resource and pushing data until `readable.push()` returns `false`. Only when `_read()` is called again after it has stopped should it resume pushing additional data into the queue.
Once the [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) method has been called, it will not be called again until more data is pushed through the [`readable.push()`](https://nodejs.org/docs/latest/api/stream.html#readablepushchunk-encoding) method. Empty data such as empty buffers and strings will not cause [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) to be called.
The `size` argument is advisory. For implementations where a "read" is a single operation that returns data can use the `size` argument to determine how much data to fetch. Other implementations may ignore this argument and simply provide data whenever it becomes available. There is no need to "wait" until `size` bytes are available before calling [`stream.push(chunk)`](https://nodejs.org/docs/latest/api/stream.html#readablepushchunk-encoding).
The [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) method is prefixed with an underscore because it is internal to the class that defines it, and should never be called directly by user programs.
#####  `readable._destroy(err, callback)`[#](https://nodejs.org/docs/latest/api/stream.html#readable-destroyerr-callback)
Added in: v8.0.0
  * `err`
  * `callback`


The `_destroy()` method is called by [`readable.destroy()`](https://nodejs.org/docs/latest/api/stream.html#readabledestroyerror). It can be overridden by child classes but it **must not** be called directly.
#####  `readable.push(chunk[, encoding])`[#](https://nodejs.org/docs/latest/api/stream.html#readablepushchunk-encoding)
History Version | Changes
---|---
v22.0.0, v20.13.0 | The `chunk` argument can now be a `TypedArray` or `DataView` instance.
v8.0.0 | The `chunk` argument can now be a `Uint8Array` instance.
  * `chunk` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `chunk` must be a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer), `chunk` may be any JavaScript value.
  * `encoding` `Buffer` encoding, such as `'utf8'` or `'ascii'`.
  * Returns: `true` if additional chunks of data may continue to be pushed; `false` otherwise.


When `chunk` is a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer), `chunk` of data will be added to the internal queue for users of the stream to consume. Passing `chunk` as `null` signals the end of the stream (EOF), after which no more data can be written.
When the `Readable` is operating in paused mode, the data added with `readable.push()` can be read out by calling the [`readable.read()`](https://nodejs.org/docs/latest/api/stream.html#readablereadsize) method when the [`'readable'`](https://nodejs.org/docs/latest/api/stream.html#event-readable) event is emitted.
When the `Readable` is operating in flowing mode, the data added with `readable.push()` will be delivered by emitting a `'data'` event.
The `readable.push()` method is designed to be as flexible as possible. For example, when wrapping a lower-level source that provides some form of pause/resume mechanism, and a data callback, the low-level source can be wrapped by the custom `Readable` instance:
```
// `_source` is an object with readStop() and readStart() methods,
// and an `ondata` member that gets called when it has data, and
// an `onend` member that gets called when the data is over.

class SourceWrapper extends Readable {
  constructor(options) {
    super(options);

    this._source = getLowLevelSourceObject();

    // Every time there's data, push it into the internal buffer.
    this._source.ondata = (chunk) => {
      // If push() returns false, then stop reading from source.
      if (!this.push(chunk))
        this._source.readStop();
    };

    // When the source ends, push the EOF-signaling `null` chunk.
    this._source.onend = () => {
      this.push(null);
    };
  }
  // _read() will be called when the stream wants to pull more data in.
  // The advisory size argument is ignored in this case.
  _read(size) {
    this._source.readStart();
  }
}
copy
```

The `readable.push()` method is used to push the content into the internal buffer. It can be driven by the [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) method.
For streams not operating in object mode, if the `chunk` parameter of `readable.push()` is `undefined`, it will be treated as empty string or buffer. See [`readable.push('')`](https://nodejs.org/docs/latest/api/stream.html#readablepush) for more information.
##### Errors while reading[#](https://nodejs.org/docs/latest/api/stream.html#errors-while-reading)
Errors occurring during processing of the [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) must be propagated through the [`readable.destroy(err)`](https://nodejs.org/docs/latest/api/stream.html#readable_destroyerr-callback) method. Throwing an `Error` from within [`readable._read()`](https://nodejs.org/docs/latest/api/stream.html#readable_readsize) or manually emitting an `'error'` event results in undefined behavior.
```
const { Readable } = require('node:stream');

const myReadable = new Readable({
  read(size) {
    const err = checkSomeErrorCondition();
    if (err) {
      this.destroy(err);
    } else {
      // Do some work.
    }
  },
});
copy
```

##### An example counting stream[#](https://nodejs.org/docs/latest/api/stream.html#an-example-counting-stream)
The following is a basic example of a `Readable` stream that emits the numerals from 1 to 1,000,000 in ascending order, and then ends.
```
const { Readable } = require('node:stream');

class Counter extends Readable {
  constructor(opt) {
    super(opt);
    this._max = 1000000;
    this._index = 1;
  }

  _read() {
    const i = this._index++;
    if (i > this._max)
      this.push(null);
    else {
      const str = String(i);
      const buf = Buffer.from(str, 'ascii');
      this.push(buf);
    }
  }
}
copy
```

#### Implementing a duplex stream[#](https://nodejs.org/docs/latest/api/stream.html#implementing-a-duplex-stream)
A [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) stream is one that implements both [`Readable`](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable) and [`Writable`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable), such as a TCP socket connection.
Because JavaScript does not have support for multiple inheritance, the `stream.Duplex` class is extended to implement a [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) stream (as opposed to extending the `stream.Readable` _and_ `stream.Writable` classes).
The `stream.Duplex` class prototypically inherits from `stream.Readable` and parasitically from `stream.Writable`, but `instanceof` will work properly for both base classes due to overriding `stream.Writable`.
