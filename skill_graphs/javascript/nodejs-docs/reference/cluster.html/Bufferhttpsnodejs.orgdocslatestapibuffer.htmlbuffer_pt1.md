## Buffer[#](https://nodejs.org/docs/latest/api/buffer.html#buffer)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
`Buffer` objects are used to represent a fixed-length sequence of bytes. Many Node.js APIs support `Buffer`s.
The `Buffer` class is a subclass of JavaScript's `Buffer`s are supported as well.
While the `Buffer` class is available within the global scope, it is still recommended to explicitly reference it via an import or require statement.
```
import { Buffer } from 'node:buffer';

// Creates a zero-filled Buffer of length 10.
const buf1 = Buffer.alloc(10);

// Creates a Buffer of length 10,
// filled with bytes which all have the value `1`.
const buf2 = Buffer.alloc(10, 1);

// Creates an uninitialized buffer of length 10.
// This is faster than calling Buffer.alloc() but the returned
// Buffer instance might contain old data that needs to be
// overwritten using fill(), write(), or other functions that fill the Buffer's
// contents.
const buf3 = Buffer.allocUnsafe(10);

// Creates a Buffer containing the bytes [1, 2, 3].
const buf4 = Buffer.from([1, 2, 3]);

// Creates a Buffer containing the bytes [1, 1, 1, 1] – the entries
// are all truncated using `(value & 255)` to fit into the range 0–255.
const buf5 = Buffer.from([257, 257.5, -255, '1']);

// Creates a Buffer containing the UTF-8-encoded bytes for the string 'tést':
// [0x74, 0xc3, 0xa9, 0x73, 0x74] (in hexadecimal notation)
// [116, 195, 169, 115, 116] (in decimal notation)
const buf6 = Buffer.from('tést');

// Creates a Buffer containing the Latin-1 bytes [0x74, 0xe9, 0x73, 0x74].
const buf7 = Buffer.from('tést', 'latin1');
const { Buffer } = require('node:buffer');

// Creates a zero-filled Buffer of length 10.
const buf1 = Buffer.alloc(10);

// Creates a Buffer of length 10,
// filled with bytes which all have the value `1`.
const buf2 = Buffer.alloc(10, 1);

// Creates an uninitialized buffer of length 10.
// This is faster than calling Buffer.alloc() but the returned
// Buffer instance might contain old data that needs to be
// overwritten using fill(), write(), or other functions that fill the Buffer's
// contents.
const buf3 = Buffer.allocUnsafe(10);

// Creates a Buffer containing the bytes [1, 2, 3].
const buf4 = Buffer.from([1, 2, 3]);

// Creates a Buffer containing the bytes [1, 1, 1, 1] – the entries
// are all truncated using `(value & 255)` to fit into the range 0–255.
const buf5 = Buffer.from([257, 257.5, -255, '1']);

// Creates a Buffer containing the UTF-8-encoded bytes for the string 'tést':
// [0x74, 0xc3, 0xa9, 0x73, 0x74] (in hexadecimal notation)
// [116, 195, 169, 115, 116] (in decimal notation)
const buf6 = Buffer.from('tést');

// Creates a Buffer containing the Latin-1 bytes [0x74, 0xe9, 0x73, 0x74].
const buf7 = Buffer.from('tést', 'latin1');
copy
```

### Buffers and character encodings[#](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings)
History Version | Changes
---|---
v15.7.0, v14.18.0 | Introduced `base64url` encoding.
v6.4.0 | Introduced `latin1` as an alias for `binary`.
v5.0.0 | Removed the deprecated `raw` and `raws` encodings.
When converting between `Buffer`s and strings, a character encoding may be specified. If no character encoding is specified, UTF-8 will be used as the default.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from('hello world', 'utf8');

console.log(buf.toString('hex'));
// Prints: 68656c6c6f20776f726c64
console.log(buf.toString('base64'));
// Prints: aGVsbG8gd29ybGQ=

console.log(Buffer.from('fhqwhgads', 'utf8'));
// Prints: <Buffer 66 68 71 77 68 67 61 64 73>
console.log(Buffer.from('fhqwhgads', 'utf16le'));
// Prints: <Buffer 66 00 68 00 71 00 77 00 68 00 67 00 61 00 64 00 73 00>
const { Buffer } = require('node:buffer');

const buf = Buffer.from('hello world', 'utf8');

console.log(buf.toString('hex'));
// Prints: 68656c6c6f20776f726c64
console.log(buf.toString('base64'));
// Prints: aGVsbG8gd29ybGQ=

console.log(Buffer.from('fhqwhgads', 'utf8'));
// Prints: <Buffer 66 68 71 77 68 67 61 64 73>
console.log(Buffer.from('fhqwhgads', 'utf16le'));
// Prints: <Buffer 66 00 68 00 71 00 77 00 68 00 67 00 61 00 64 00 73 00>
copy
```

Node.js buffers accept all case variations of encoding strings that they receive. For example, UTF-8 can be specified as `'utf8'`, `'UTF8'`, or `'uTf8'`.
The character encodings currently supported by Node.js are the following:
  * `'utf8'` (alias: `'utf-8'`): Multi-byte encoded Unicode characters. Many web pages and other document formats use `Buffer` into a string that does not exclusively contain valid UTF-8 data, the Unicode replacement character `U+FFFD` � will be used to represent those errors.
  * `'utf16le'` (alias: `'utf-16le'`): Multi-byte encoded Unicode characters. Unlike `'utf8'`, each character in the string will be encoded using either 2 or 4 bytes. Node.js only supports the
  * `'latin1'`: Latin-1 stands for `U+0000` to `U+00FF`. Each character is encoded using a single byte. Characters that do not fit into that range are truncated and will be mapped to characters in that range.


Converting a `Buffer` into a string using one of the above is referred to as decoding, and converting a string into a `Buffer` is referred to as encoding.
Node.js also supports the following binary-to-text encodings. For binary-to-text encodings, the naming convention is reversed: Converting a `Buffer` into a string is typically referred to as encoding, and converting a string into a `Buffer` as decoding.
  * `'base64'`: `Buffer` from a string, this encoding will also correctly accept "URL and Filename Safe Alphabet" as specified in
  * `'base64url'`: `Buffer` from a string, this encoding will also correctly accept regular base64-encoded strings. When encoding a `Buffer` to a string, this encoding will omit padding.
  * `'hex'`: Encode each byte as two hexadecimal characters. Data truncation may occur when decoding strings that do not exclusively consist of an even number of hexadecimal characters. See below for an example.


The following legacy character encodings are also supported:
  * `'ascii'`: For 7-bit `Buffer`, this is equivalent to using `'latin1'`. When decoding a `Buffer` into a string, using this encoding will additionally unset the highest bit of each byte before decoding as `'latin1'`. Generally, there should be no reason to use this encoding, as `'utf8'` (or, if the data is known to always be ASCII-only, `'latin1'`) will be a better choice when encoding or decoding ASCII-only text. It is only provided for legacy compatibility.
  * `'binary'`: Alias for `'latin1'`. The name of this encoding can be very misleading, as all of the encodings listed here convert between strings and binary data. For converting between strings and `Buffer`s, typically `'utf8'` is the right choice.
  * `'ucs2'`, `'ucs-2'`: Aliases of `'utf16le'`. UCS-2 used to refer to a variant of UTF-16 that did not support characters that had code points larger than U+FFFF. In Node.js, these code points are always supported.

```
import { Buffer } from 'node:buffer';

Buffer.from('1ag123', 'hex');
// Prints <Buffer 1a>, data truncated when first non-hexadecimal value
// ('g') encountered.

Buffer.from('1a7', 'hex');
// Prints <Buffer 1a>, data truncated when data ends in single digit ('7').

Buffer.from('1634', 'hex');
// Prints <Buffer 16 34>, all data represented.
const { Buffer } = require('node:buffer');

Buffer.from('1ag123', 'hex');
// Prints <Buffer 1a>, data truncated when first non-hexadecimal value
// ('g') encountered.

Buffer.from('1a7', 'hex');
// Prints <Buffer 1a>, data truncated when data ends in single digit ('7').

Buffer.from('1634', 'hex');
// Prints <Buffer 16 34>, all data represented.
copy
```

Modern Web browsers follow the `'latin1'` and `'ISO-8859-1'` to `'win-1252'`. This means that while doing something like `http.get()`, if the returned charset is one of those listed in the WHATWG specification it is possible that the server actually returned `'win-1252'`-encoded data, and using `'latin1'` encoding may incorrectly decode the characters.
### Buffers and TypedArrays[#](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-typedarrays)
History Version | Changes
---|---
v3.0.0 | The `Buffer` class now inherits from `Uint8Array`.
`Buffer` instances are also JavaScript `Buffer`s. There are, however, subtle incompatibilities between the `Buffer` API and the
In particular:
  * While `TypedArray`, [`Buffer.prototype.slice()`](https://nodejs.org/docs/latest/api/buffer.html#bufslicestart-end) creates a view over the existing `Buffer` without copying. This behavior can be surprising, and only exists for legacy compatibility. [`Buffer.prototype.slice()`](https://nodejs.org/docs/latest/api/buffer.html#bufslicestart-end) on both `Buffer`s and other `TypedArray`s and should be preferred.
  * [`buf.toString()`](https://nodejs.org/docs/latest/api/buffer.html#buftostringencoding-start-end) is incompatible with its `TypedArray` equivalent.
  * A number of methods, e.g. [`buf.indexOf()`](https://nodejs.org/docs/latest/api/buffer.html#bufindexofvalue-byteoffset-encoding), support additional arguments.


There are two ways to create new `Buffer`:
  * Passing a `Buffer` to a `Buffer`'s contents, interpreted as an array of integers, and not as a byte sequence of the target type.

```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([1, 2, 3, 4]);
const uint32array = new Uint32Array(buf);

console.log(uint32array);

// Prints: Uint32Array(4) [ 1, 2, 3, 4 ]
const { Buffer } = require('node:buffer');

const buf = Buffer.from([1, 2, 3, 4]);
const uint32array = new Uint32Array(buf);

console.log(uint32array);

// Prints: Uint32Array(4) [ 1, 2, 3, 4 ]
copy
```

  * Passing the `Buffer`'s underlying `Buffer`.

```
import { Buffer } from 'node:buffer';

const buf = Buffer.from('hello', 'utf16le');
const uint16array = new Uint16Array(
  buf.buffer,
  buf.byteOffset,
  buf.length / Uint16Array.BYTES_PER_ELEMENT);

console.log(uint16array);

// Prints: Uint16Array(5) [ 104, 101, 108, 108, 111 ]
const { Buffer } = require('node:buffer');

const buf = Buffer.from('hello', 'utf16le');
const uint16array = new Uint16Array(
  buf.buffer,
  buf.byteOffset,
  buf.length / Uint16Array.BYTES_PER_ELEMENT);

console.log(uint16array);

// Prints: Uint16Array(5) [ 104, 101, 108, 108, 111 ]
copy
```

It is possible to create a new `Buffer` that shares the same allocated memory as a `TypedArray` object's `.buffer` property in the same way. [`Buffer.from()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarraybuffer-byteoffset-length) behaves like `new Uint8Array()` in this context.
```
import { Buffer } from 'node:buffer';

const arr = new Uint16Array(2);

arr[0] = 5000;
arr[1] = 4000;

// Copies the contents of `arr`.
const buf1 = Buffer.from(arr);

// Shares memory with `arr`.
const buf2 = Buffer.from(arr.buffer);

console.log(buf1);
// Prints: <Buffer 88 a0>
console.log(buf2);
// Prints: <Buffer 88 13 a0 0f>

arr[1] = 6000;

console.log(buf1);
// Prints: <Buffer 88 a0>
console.log(buf2);
// Prints: <Buffer 88 13 70 17>
const { Buffer } = require('node:buffer');

const arr = new Uint16Array(2);

arr[0] = 5000;
arr[1] = 4000;

// Copies the contents of `arr`.
const buf1 = Buffer.from(arr);

// Shares memory with `arr`.
const buf2 = Buffer.from(arr.buffer);

console.log(buf1);
// Prints: <Buffer 88 a0>
console.log(buf2);
// Prints: <Buffer 88 13 a0 0f>

arr[1] = 6000;

console.log(buf1);
// Prints: <Buffer 88 a0>
console.log(buf2);
// Prints: <Buffer 88 13 70 17>
copy
```

When creating a `Buffer` using a `.buffer`, it is possible to use only a portion of the underlying `byteOffset` and `length` parameters.
```
import { Buffer } from 'node:buffer';

const arr = new Uint16Array(20);
const buf = Buffer.from(arr.buffer, 0, 16);

console.log(buf.length);
// Prints: 16
const { Buffer } = require('node:buffer');

const arr = new Uint16Array(20);
const buf = Buffer.from(arr.buffer, 0, 16);

console.log(buf.length);
// Prints: 16
copy
```

The `Buffer.from()` and
The `Buffer.from()` method, however, does not support the use of a mapping function:
  * [`Buffer.from(array)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarray)
  * [`Buffer.from(buffer)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfrombuffer)
  * [`Buffer.from(arrayBuffer[, byteOffset[, length]])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarraybuffer-byteoffset-length)
  * [`Buffer.from(string[, encoding])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromstring-encoding)


#### Buffer methods are callable with `Uint8Array` instances[#](https://nodejs.org/docs/latest/api/buffer.html#buffer-methods-are-callable-with-uint8array-instances)
All methods on the Buffer prototype are callable with a `Uint8Array` instance.
```
const { toString, write } = Buffer.prototype;

const uint8array = new Uint8Array(5);

write.call(uint8array, 'hello', 0, 5, 'utf8'); // 5
// <Uint8Array 68 65 6c 6c 6f>

toString.call(uint8array, 'utf8'); // 'hello'
copy
```

### Buffers and iteration[#](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-iteration)
`Buffer` instances can be iterated over using `for..of` syntax:
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([1, 2, 3]);

for (const b of buf) {
  console.log(b);
}
// Prints:
//   1
//   2
//   3
const { Buffer } = require('node:buffer');

const buf = Buffer.from([1, 2, 3]);

for (const b of buf) {
  console.log(b);
}
// Prints:
//   1
//   2
//   3
copy
```

Additionally, the [`buf.values()`](https://nodejs.org/docs/latest/api/buffer.html#bufvalues), [`buf.keys()`](https://nodejs.org/docs/latest/api/buffer.html#bufkeys), and [`buf.entries()`](https://nodejs.org/docs/latest/api/buffer.html#bufentries) methods can be used to create iterators.
### Class: `Blob`[#](https://nodejs.org/docs/latest/api/buffer.html#class-blob)
Added in: v15.7.0, v14.18.0History Version | Changes
---|---
v18.0.0, v16.17.0 | No longer experimental.
A [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) encapsulates immutable, raw data that can be safely shared across multiple worker threads.
####  `new buffer.Blob([sources[, options]])`[#](https://nodejs.org/docs/latest/api/buffer.html#new-bufferblobsources-options)
Added in: v15.7.0, v14.18.0History Version | Changes
---|---
v16.7.0 | Added the standard `endings` option to replace line-endings, and removed the non-standard `encoding` option.
  * `sources` [`<Blob[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) An array of string, [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) objects, or any mix of such objects, that will be stored within the `Blob`.
  * `options`
    * `endings` `'transparent'` or `'native'`. When set to `'native'`, line endings in string source parts will be converted to the platform native line-ending as specified by `require('node:os').EOL`.
    * `type` `type` to convey the MIME media type of the data, however no validation of the type format is performed.


Creates a new `Blob` object containing a concatenation of the given sources.
[`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) sources are copied into the 'Blob' and can therefore be safely modified after the 'Blob' is created.
String sources are encoded as UTF-8 byte sequences and copied into the Blob. Unmatched surrogate pairs within each string part will be replaced by Unicode U+FFFD replacement characters.
####  `blob.arrayBuffer()`[#](https://nodejs.org/docs/latest/api/buffer.html#blobarraybuffer)
Added in: v15.7.0, v14.18.0
  * Returns:


Returns a promise that fulfills with an `Blob` data.
####  `blob.bytes()`[#](https://nodejs.org/docs/latest/api/buffer.html#blobbytes)
Added in: v22.3.0, v20.16.0
The `blob.bytes()` method returns the byte of the `Blob` object as a `Promise<Uint8Array>`.
```
const blob = new Blob(['hello']);
blob.bytes().then((bytes) => {
  console.log(bytes); // Outputs: Uint8Array(5) [ 104, 101, 108, 108, 111 ]
});
copy
```

####  `blob.size`[#](https://nodejs.org/docs/latest/api/buffer.html#blobsize)
Added in: v15.7.0, v14.18.0
The total size of the `Blob` in bytes.
####  `blob.slice([start[, end[, type]]])`[#](https://nodejs.org/docs/latest/api/buffer.html#blobslicestart-end-type)
Added in: v15.7.0, v14.18.0
  * `start`
  * `end`
  * `type` `Blob`


Creates and returns a new `Blob` containing a subset of this `Blob` objects data. The original `Blob` is not altered.
####  `blob.stream()`[#](https://nodejs.org/docs/latest/api/buffer.html#blobstream)
Added in: v16.7.0
  * Returns: [`<ReadableStream>`](https://nodejs.org/docs/latest/api/webstreams.html#class-readablestream)


Returns a new `ReadableStream` that allows the content of the `Blob` to be read.
####  `blob.text()`[#](https://nodejs.org/docs/latest/api/buffer.html#blobtext)
Added in: v15.7.0, v14.18.0
  * Returns:


Returns a promise that fulfills with the contents of the `Blob` decoded as a UTF-8 string.
####  `blob.type`[#](https://nodejs.org/docs/latest/api/buffer.html#blobtype)
Added in: v15.7.0, v14.18.0
  * Type:


The content-type of the `Blob`.
####  `Blob` objects and `MessageChannel`[#](https://nodejs.org/docs/latest/api/buffer.html#blob-objects-and-messagechannel)
Once a [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) object is created, it can be sent via `MessagePort` to multiple destinations without transferring or immediately copying the data. The data contained by the `Blob` is copied only when the `arrayBuffer()` or `text()` methods are called.
```
import { Blob } from 'node:buffer';
import { setTimeout as delay } from 'node:timers/promises';

const blob = new Blob(['hello there']);

const mc1 = new MessageChannel();
const mc2 = new MessageChannel();

mc1.port1.onmessage = async ({ data }) => {
  console.log(await data.arrayBuffer());
  mc1.port1.close();
};

mc2.port1.onmessage = async ({ data }) => {
  await delay(1000);
  console.log(await data.arrayBuffer());
  mc2.port1.close();
};

mc1.port2.postMessage(blob);
mc2.port2.postMessage(blob);

// The Blob is still usable after posting.
blob.text().then(console.log);
const { Blob } = require('node:buffer');
const { setTimeout: delay } = require('node:timers/promises');

const blob = new Blob(['hello there']);

const mc1 = new MessageChannel();
const mc2 = new MessageChannel();

mc1.port1.onmessage = async ({ data }) => {
  console.log(await data.arrayBuffer());
  mc1.port1.close();
};

mc2.port1.onmessage = async ({ data }) => {
  await delay(1000);
  console.log(await data.arrayBuffer());
  mc2.port1.close();
};

mc1.port2.postMessage(blob);
mc2.port2.postMessage(blob);

// The Blob is still usable after posting.
blob.text().then(console.log);
copy
```

### Class: `Buffer`[#](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)
The `Buffer` class is a global type for dealing with binary data directly. It can be constructed in a variety of ways.
#### Static method: `Buffer.alloc(size[, fill[, encoding]])`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocsize-fill-encoding)
Added in: v5.10.0History Version | Changes
---|---
v20.0.0 | Throw ERR_INVALID_ARG_TYPE or ERR_OUT_OF_RANGE instead of ERR_INVALID_ARG_VALUE for invalid input arguments.
v15.0.0 | Throw ERR_INVALID_ARG_VALUE instead of ERR_INVALID_OPT_VALUE for invalid input arguments.
v10.0.0 | Attempting to fill a non-zero length buffer with a zero length buffer triggers a thrown exception.
v10.0.0 | Specifying an invalid string for `fill` triggers a thrown exception.
v8.9.3 | Specifying an invalid string for `fill` now results in a zero-filled buffer.
  * `size` `Buffer`.
  * `fill` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer` with. **Default:** `0`.
  * `encoding` `fill` is a string, this is its encoding. **Default:** `'utf8'`.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Allocates a new `Buffer` of `size` bytes. If `fill` is `undefined`, the `Buffer` will be zero-filled.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.alloc(5);

console.log(buf);
// Prints: <Buffer 00 00 00 00 00>
const { Buffer } = require('node:buffer');

const buf = Buffer.alloc(5);

console.log(buf);
// Prints: <Buffer 00 00 00 00 00>
copy
```

If `size` is larger than [`buffer.constants.MAX_LENGTH`](https://nodejs.org/docs/latest/api/buffer.html#bufferconstantsmax_length) or smaller than 0, [`ERR_OUT_OF_RANGE`](https://nodejs.org/docs/latest/api/errors.html#err_out_of_range) is thrown.
If `fill` is specified, the allocated `Buffer` will be initialized by calling [`buf.fill(fill)`](https://nodejs.org/docs/latest/api/buffer.html#buffillvalue-offset-end-encoding).
```
import { Buffer } from 'node:buffer';

const buf = Buffer.alloc(5, 'a');

console.log(buf);
// Prints: <Buffer 61 61 61 61 61>
const { Buffer } = require('node:buffer');

const buf = Buffer.alloc(5, 'a');

console.log(buf);
// Prints: <Buffer 61 61 61 61 61>
copy
```

If both `fill` and `encoding` are specified, the allocated `Buffer` will be initialized by calling [`buf.fill(fill, encoding)`](https://nodejs.org/docs/latest/api/buffer.html#buffillvalue-offset-end-encoding).
```
import { Buffer } from 'node:buffer';

const buf = Buffer.alloc(11, 'aGVsbG8gd29ybGQ=', 'base64');

console.log(buf);
// Prints: <Buffer 68 65 6c 6c 6f 20 77 6f 72 6c 64>
const { Buffer } = require('node:buffer');

const buf = Buffer.alloc(11, 'aGVsbG8gd29ybGQ=', 'base64');

console.log(buf);
// Prints: <Buffer 68 65 6c 6c 6f 20 77 6f 72 6c 64>
copy
```

Calling [`Buffer.alloc()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocsize-fill-encoding) can be measurably slower than the alternative [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) but ensures that the newly created `Buffer` instance contents will never contain sensitive data from previous allocations, including data that might not have been allocated for `Buffer`s.
A `TypeError` will be thrown if `size` is not a number.
#### Static method: `Buffer.allocUnsafe(size)`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize)
Added in: v5.10.0History Version | Changes
---|---
v20.0.0 | Throw ERR_INVALID_ARG_TYPE or ERR_OUT_OF_RANGE instead of ERR_INVALID_ARG_VALUE for invalid input arguments.
v15.0.0 | Throw ERR_INVALID_ARG_VALUE instead of ERR_INVALID_OPT_VALUE for invalid input arguments.
v7.0.0 | Passing a negative `size` will now throw an error.
  * `size` `Buffer`.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Allocates a new `Buffer` of `size` bytes. If `size` is larger than [`buffer.constants.MAX_LENGTH`](https://nodejs.org/docs/latest/api/buffer.html#bufferconstantsmax_length) or smaller than 0, [`ERR_OUT_OF_RANGE`](https://nodejs.org/docs/latest/api/errors.html#err_out_of_range) is thrown.
The underlying memory for `Buffer` instances created in this way is _not initialized_. The contents of the newly created `Buffer` are unknown and _may contain sensitive data_. Use [`Buffer.alloc()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocsize-fill-encoding) instead to initialize `Buffer` instances with zeroes.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(10);

console.log(buf);
// Prints (contents may vary): <Buffer a0 8b 28 3f 01 00 00 00 50 32>

buf.fill(0);

console.log(buf);
// Prints: <Buffer 00 00 00 00 00 00 00 00 00 00>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(10);

console.log(buf);
// Prints (contents may vary): <Buffer a0 8b 28 3f 01 00 00 00 50 32>

buf.fill(0);

console.log(buf);
// Prints: <Buffer 00 00 00 00 00 00 00 00 00 00>
copy
```

A `TypeError` will be thrown if `size` is not a number.
The `Buffer` module pre-allocates an internal `Buffer` instance of size [`Buffer.poolSize`](https://nodejs.org/docs/latest/api/buffer.html#bufferpoolsize) that is used as a pool for the fast allocation of new `Buffer` instances created using [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize), [`Buffer.from(array)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarray), [`Buffer.from(string)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromstring-encoding), and [`Buffer.concat()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferconcatlist-totallength) only when `size` is less than `Buffer.poolSize >>> 1` (floor of [`Buffer.poolSize`](https://nodejs.org/docs/latest/api/buffer.html#bufferpoolsize) divided by two).
Use of this pre-allocated internal memory pool is a key difference between calling `Buffer.alloc(size, fill)` vs. `Buffer.allocUnsafe(size).fill(fill)`. Specifically, `Buffer.alloc(size, fill)` will _never_ use the internal `Buffer` pool, while `Buffer.allocUnsafe(size).fill(fill)` _will_ use the internal `Buffer` pool if `size` is less than or equal to half [`Buffer.poolSize`](https://nodejs.org/docs/latest/api/buffer.html#bufferpoolsize). The difference is subtle but can be important when an application requires the additional performance that [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) provides.
