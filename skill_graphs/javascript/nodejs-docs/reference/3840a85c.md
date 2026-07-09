#### Static method: `Buffer.allocUnsafeSlow(size)`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafeslowsize)
Added in: v5.12.0History Version | Changes
---|---
v20.0.0 | Throw ERR_INVALID_ARG_TYPE or ERR_OUT_OF_RANGE instead of ERR_INVALID_ARG_VALUE for invalid input arguments.
v15.0.0 | Throw ERR_INVALID_ARG_VALUE instead of ERR_INVALID_OPT_VALUE for invalid input arguments.
  * `size` `Buffer`.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Allocates a new `Buffer` of `size` bytes. If `size` is larger than [`buffer.constants.MAX_LENGTH`](https://nodejs.org/docs/latest/api/buffer.html#bufferconstantsmax_length) or smaller than 0, [`ERR_OUT_OF_RANGE`](https://nodejs.org/docs/latest/api/errors.html#err_out_of_range) is thrown. A zero-length `Buffer` is created if `size` is 0.
The underlying memory for `Buffer` instances created in this way is _not initialized_. The contents of the newly created `Buffer` are unknown and _may contain sensitive data_. Use [`buf.fill(0)`](https://nodejs.org/docs/latest/api/buffer.html#buffillvalue-offset-end-encoding) to initialize such `Buffer` instances with zeroes.
When using [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) to allocate new `Buffer` instances, allocations less than `Buffer.poolSize >>> 1` (4KiB when default poolSize is used) are sliced from a single pre-allocated `Buffer`. This allows applications to avoid the garbage collection overhead of creating many individually allocated `Buffer` instances. This approach improves both performance and memory usage by eliminating the need to track and clean up as many individual `ArrayBuffer` objects.
However, in the case where a developer may need to retain a small chunk of memory from a pool for an indeterminate amount of time, it may be appropriate to create an un-pooled `Buffer` instance using `Buffer.allocUnsafeSlow()` and then copying out the relevant bits.
```
import { Buffer } from 'node:buffer';

// Need to keep around a few small chunks of memory.
const store = [];

socket.on('readable', () => {
  let data;
  while (null !== (data = readable.read())) {
    // Allocate for retained data.
    const sb = Buffer.allocUnsafeSlow(10);

    // Copy the data into the new allocation.
    data.copy(sb, 0, 0, 10);

    store.push(sb);
  }
});
const { Buffer } = require('node:buffer');

// Need to keep around a few small chunks of memory.
const store = [];

socket.on('readable', () => {
  let data;
  while (null !== (data = readable.read())) {
    // Allocate for retained data.
    const sb = Buffer.allocUnsafeSlow(10);

    // Copy the data into the new allocation.
    data.copy(sb, 0, 0, 10);

    store.push(sb);
  }
});
copy
```

A `TypeError` will be thrown if `size` is not a number.
#### Static method: `Buffer.byteLength(string[, encoding])`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferbytelengthstring-encoding)
Added in: v0.1.90History Version | Changes
---|---
v7.0.0 | Passing invalid input will now throw an error.
v5.10.0 | The `string` parameter can now be any `TypedArray`, `DataView` or `ArrayBuffer`.
  * `string` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` `string` is a string, this is its encoding. **Default:** `'utf8'`.
  * Returns: `string`.


Returns the byte length of a string when encoded using `encoding`. This is not the same as
For `'base64'`, `'base64url'`, and `'hex'`, this function assumes valid input. For strings that contain non-base64/hex-encoded data (e.g. whitespace), the return value might be greater than the length of a `Buffer` created from the string.
```
import { Buffer } from 'node:buffer';

const str = '\u00bd + \u00bc = \u00be';

console.log(`${str}: ${str.length} characters, ` +
            `${Buffer.byteLength(str, 'utf8')} bytes`);
// Prints: ½ + ¼ = ¾: 9 characters, 12 bytes
const { Buffer } = require('node:buffer');

const str = '\u00bd + \u00bc = \u00be';

console.log(`${str}: ${str.length} characters, ` +
            `${Buffer.byteLength(str, 'utf8')} bytes`);
// Prints: ½ + ¼ = ¾: 9 characters, 12 bytes
copy
```

When `string` is a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `.byteLength` is returned.
#### Static method: `Buffer.compare(buf1, buf2)`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-buffercomparebuf1-buf2)
Added in: v0.11.13History Version | Changes
---|---
v8.0.0 | The arguments can now be `Uint8Array`s.
  * `buf1` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `buf2` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: `-1`, `0`, or `1`, depending on the result of the comparison. See [`buf.compare()`](https://nodejs.org/docs/latest/api/buffer.html#bufcomparetarget-targetstart-targetend-sourcestart-sourceend) for details.


Compares `buf1` to `buf2`, typically for the purpose of sorting arrays of `Buffer` instances. This is equivalent to calling [`buf1.compare(buf2)`](https://nodejs.org/docs/latest/api/buffer.html#bufcomparetarget-targetstart-targetend-sourcestart-sourceend).
```
import { Buffer } from 'node:buffer';

const buf1 = Buffer.from('1234');
const buf2 = Buffer.from('0123');
const arr = [buf1, buf2];

console.log(arr.sort(Buffer.compare));
// Prints: [ <Buffer 30 31 32 33>, <Buffer 31 32 33 34> ]
// (This result is equal to: [buf2, buf1].)
const { Buffer } = require('node:buffer');

const buf1 = Buffer.from('1234');
const buf2 = Buffer.from('0123');
const arr = [buf1, buf2];

console.log(arr.sort(Buffer.compare));
// Prints: [ <Buffer 30 31 32 33>, <Buffer 31 32 33 34> ]
// (This result is equal to: [buf2, buf1].)
copy
```

#### Static method: `Buffer.concat(list[, totalLength])`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferconcatlist-totallength)
Added in: v0.7.11History Version | Changes
---|---
v8.0.0 | The elements of `list` can now be `Uint8Array`s.
  * `list` [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer` or
  * `totalLength` `Buffer` instances in `list` when concatenated.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Returns a new `Buffer` which is the result of concatenating all the `Buffer` instances in the `list` together.
If the list has no items, or if the `totalLength` is 0, then a new zero-length `Buffer` is returned.
If `totalLength` is not provided, it is calculated from the `Buffer` instances in `list` by adding their lengths.
If `totalLength` is provided, it must be an unsigned integer. If the combined length of the `Buffer`s in `list` exceeds `totalLength`, the result is truncated to `totalLength`. If the combined length of the `Buffer`s in `list` is less than `totalLength`, the remaining space is filled with zeros.
```
import { Buffer } from 'node:buffer';

// Create a single `Buffer` from a list of three `Buffer` instances.

const buf1 = Buffer.alloc(10);
const buf2 = Buffer.alloc(14);
const buf3 = Buffer.alloc(18);
const totalLength = buf1.length + buf2.length + buf3.length;

console.log(totalLength);
// Prints: 42

const bufA = Buffer.concat([buf1, buf2, buf3], totalLength);

console.log(bufA);
// Prints: <Buffer 00 00 00 00 ...>
console.log(bufA.length);
// Prints: 42
const { Buffer } = require('node:buffer');

// Create a single `Buffer` from a list of three `Buffer` instances.

const buf1 = Buffer.alloc(10);
const buf2 = Buffer.alloc(14);
const buf3 = Buffer.alloc(18);
const totalLength = buf1.length + buf2.length + buf3.length;

console.log(totalLength);
// Prints: 42

const bufA = Buffer.concat([buf1, buf2, buf3], totalLength);

console.log(bufA);
// Prints: <Buffer 00 00 00 00 ...>
console.log(bufA.length);
// Prints: 42
copy
```

`Buffer.concat()` may also use the internal `Buffer` pool like [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) does.
#### Static method: `Buffer.copyBytesFrom(view[, offset[, length]])`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-buffercopybytesfromview-offset-length)
Added in: v19.8.0, v18.16.0
  * `view`
  * `offset` `view`. **Default:** `0`.
  * `length` `view` to copy. **Default:** `view.length - offset`.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Copies the underlying memory of `view` into a new `Buffer`.
```
const u16 = new Uint16Array([0, 0xffff]);
const buf = Buffer.copyBytesFrom(u16, 1, 1);
u16[1] = 0;
console.log(buf.length); // 2
console.log(buf[0]); // 255
console.log(buf[1]); // 255
copy
```

#### Static method: `Buffer.from(array)`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarray)
Added in: v5.10.0
  * `array`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Allocates a new `Buffer` using an `array` of bytes in the range `0` – `255`. Array entries outside that range will be truncated to fit into it.
```
import { Buffer } from 'node:buffer';

// Creates a new Buffer containing the UTF-8 bytes of the string 'buffer'.
const buf = Buffer.from([0x62, 0x75, 0x66, 0x66, 0x65, 0x72]);
const { Buffer } = require('node:buffer');

// Creates a new Buffer containing the UTF-8 bytes of the string 'buffer'.
const buf = Buffer.from([0x62, 0x75, 0x66, 0x66, 0x65, 0x72]);
copy
```

If `array` is an `Array`-like object (that is, one with a `length` property of type `number`), it is treated as if it is an array, unless it is a `Buffer` or a `Uint8Array`. This means all other `TypedArray` variants get treated as an `Array`. To create a `Buffer` from the bytes backing a `TypedArray`, use [`Buffer.copyBytesFrom()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-buffercopybytesfromview-offset-length).
A `TypeError` will be thrown if `array` is not an `Array` or another type appropriate for `Buffer.from()` variants.
`Buffer.from(array)` and [`Buffer.from(string)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromstring-encoding) may also use the internal `Buffer` pool like [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) does.
#### Static method: `Buffer.from(arrayBuffer[, byteOffset[, length]])`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarraybuffer-byteoffset-length)
Added in: v5.10.0
  * `arrayBuffer` `.buffer` property of a
  * `byteOffset` **Default:** `0`.
  * `length` **Default:** `arrayBuffer.byteLength - byteOffset`.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


This creates a view of the `.buffer` property of a `Buffer` will share the same allocated memory as the `ArrayBuffer`.
```
import { Buffer } from 'node:buffer';

const arr = new Uint16Array(2);

arr[0] = 5000;
arr[1] = 4000;

// Shares memory with `arr`.
const buf = Buffer.from(arr.buffer);

console.log(buf);
// Prints: <Buffer 88 13 a0 0f>

// Changing the original Uint16Array changes the Buffer also.
arr[1] = 6000;

console.log(buf);
// Prints: <Buffer 88 13 70 17>
const { Buffer } = require('node:buffer');

const arr = new Uint16Array(2);

arr[0] = 5000;
arr[1] = 4000;

// Shares memory with `arr`.
const buf = Buffer.from(arr.buffer);

console.log(buf);
// Prints: <Buffer 88 13 a0 0f>

// Changing the original Uint16Array changes the Buffer also.
arr[1] = 6000;

console.log(buf);
// Prints: <Buffer 88 13 70 17>
copy
```

The optional `byteOffset` and `length` arguments specify a memory range within the `arrayBuffer` that will be shared by the `Buffer`.
```
import { Buffer } from 'node:buffer';

const ab = new ArrayBuffer(10);
const buf = Buffer.from(ab, 0, 2);

console.log(buf.length);
// Prints: 2
const { Buffer } = require('node:buffer');

const ab = new ArrayBuffer(10);
const buf = Buffer.from(ab, 0, 2);

console.log(buf.length);
// Prints: 2
copy
```

A `TypeError` will be thrown if `arrayBuffer` is not an `Buffer.from()` variants.
It is important to remember that a backing `ArrayBuffer` can cover a range of memory that extends beyond the bounds of a `TypedArray` view. A new `Buffer` created using the `buffer` property of a `TypedArray` may extend beyond the range of the `TypedArray`:
```
import { Buffer } from 'node:buffer';

const arrA = Uint8Array.from([0x63, 0x64, 0x65, 0x66]); // 4 elements
const arrB = new Uint8Array(arrA.buffer, 1, 2); // 2 elements
console.log(arrA.buffer === arrB.buffer); // true

const buf = Buffer.from(arrB.buffer);
console.log(buf);
// Prints: <Buffer 63 64 65 66>
const { Buffer } = require('node:buffer');

const arrA = Uint8Array.from([0x63, 0x64, 0x65, 0x66]); // 4 elements
const arrB = new Uint8Array(arrA.buffer, 1, 2); // 2 elements
console.log(arrA.buffer === arrB.buffer); // true

const buf = Buffer.from(arrB.buffer);
console.log(buf);
// Prints: <Buffer 63 64 65 66>
copy
```

#### Static method: `Buffer.from(buffer)`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfrombuffer)
Added in: v5.10.0
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer` or
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Copies the passed `buffer` data onto a new `Buffer` instance.
```
import { Buffer } from 'node:buffer';

const buf1 = Buffer.from('buffer');
const buf2 = Buffer.from(buf1);

buf1[0] = 0x61;

console.log(buf1.toString());
// Prints: auffer
console.log(buf2.toString());
// Prints: buffer
const { Buffer } = require('node:buffer');

const buf1 = Buffer.from('buffer');
const buf2 = Buffer.from(buf1);

buf1[0] = 0x61;

console.log(buf1.toString());
// Prints: auffer
console.log(buf2.toString());
// Prints: buffer
copy
```

A `TypeError` will be thrown if `buffer` is not a `Buffer` or another type appropriate for `Buffer.from()` variants.
#### Static method: `Buffer.from(object[, offsetOrEncoding[, length]])`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromobject-offsetorencoding-length)
Added in: v8.2.0
  * `object` `Symbol.toPrimitive` or `valueOf()`.
  * `offsetOrEncoding`
  * `length`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


For objects whose `valueOf()` function returns a value not strictly equal to `object`, returns `Buffer.from(object.valueOf(), offsetOrEncoding, length)`.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from(new String('this is a test'));
// Prints: <Buffer 74 68 69 73 20 69 73 20 61 20 74 65 73 74>
const { Buffer } = require('node:buffer');

const buf = Buffer.from(new String('this is a test'));
// Prints: <Buffer 74 68 69 73 20 69 73 20 61 20 74 65 73 74>
copy
```

For objects that support `Symbol.toPrimitive`, returns `Buffer.from(object[Symbol.toPrimitive]('string'), offsetOrEncoding)`.
```
import { Buffer } from 'node:buffer';

class Foo {
  [Symbol.toPrimitive]() {
    return 'this is a test';
  }
}

const buf = Buffer.from(new Foo(), 'utf8');
// Prints: <Buffer 74 68 69 73 20 69 73 20 61 20 74 65 73 74>
const { Buffer } = require('node:buffer');

class Foo {
  [Symbol.toPrimitive]() {
    return 'this is a test';
  }
}

const buf = Buffer.from(new Foo(), 'utf8');
// Prints: <Buffer 74 68 69 73 20 69 73 20 61 20 74 65 73 74>
copy
```

A `TypeError` will be thrown if `object` does not have the mentioned methods or is not of another type appropriate for `Buffer.from()` variants.
#### Static method: `Buffer.from(string[, encoding])`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromstring-encoding)
Added in: v5.10.0
  * `string`
  * `encoding` `string`. **Default:** `'utf8'`.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Creates a new `Buffer` containing `string`. The `encoding` parameter identifies the character encoding to be used when converting `string` into bytes.
```
import { Buffer } from 'node:buffer';

const buf1 = Buffer.from('this is a tést');
const buf2 = Buffer.from('7468697320697320612074c3a97374', 'hex');

console.log(buf1.toString());
// Prints: this is a tést
console.log(buf2.toString());
// Prints: this is a tést
console.log(buf1.toString('latin1'));
// Prints: this is a tÃ©st
const { Buffer } = require('node:buffer');

const buf1 = Buffer.from('this is a tést');
const buf2 = Buffer.from('7468697320697320612074c3a97374', 'hex');

console.log(buf1.toString());
// Prints: this is a tést
console.log(buf2.toString());
// Prints: this is a tést
console.log(buf1.toString('latin1'));
// Prints: this is a tÃ©st
copy
```

A `TypeError` will be thrown if `string` is not a string or another type appropriate for `Buffer.from()` variants.
[`Buffer.from(string)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromstring-encoding) may also use the internal `Buffer` pool like [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) does.
#### Static method: `Buffer.isBuffer(obj)`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferisbufferobj)
Added in: v0.1.101
  * `obj`
  * Returns:


Returns `true` if `obj` is a `Buffer`, `false` otherwise.
```
import { Buffer } from 'node:buffer';

Buffer.isBuffer(Buffer.alloc(10)); // true
Buffer.isBuffer(Buffer.from('foo')); // true
Buffer.isBuffer('a string'); // false
Buffer.isBuffer([]); // false
Buffer.isBuffer(new Uint8Array(1024)); // false
const { Buffer } = require('node:buffer');

Buffer.isBuffer(Buffer.alloc(10)); // true
Buffer.isBuffer(Buffer.from('foo')); // true
Buffer.isBuffer('a string'); // false
Buffer.isBuffer([]); // false
Buffer.isBuffer(new Uint8Array(1024)); // false
copy
```

#### Static method: `Buffer.isEncoding(encoding)`[#](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferisencodingencoding)
Added in: v0.9.1
  * `encoding`
  * Returns:


Returns `true` if `encoding` is the name of a supported character encoding, or `false` otherwise.
```
import { Buffer } from 'node:buffer';

console.log(Buffer.isEncoding('utf8'));
// Prints: true

console.log(Buffer.isEncoding('hex'));
// Prints: true

console.log(Buffer.isEncoding('utf/8'));
// Prints: false

console.log(Buffer.isEncoding(''));
// Prints: false
const { Buffer } = require('node:buffer');

console.log(Buffer.isEncoding('utf8'));
// Prints: true

console.log(Buffer.isEncoding('hex'));
// Prints: true

console.log(Buffer.isEncoding('utf/8'));
// Prints: false

console.log(Buffer.isEncoding(''));
// Prints: false
copy
```

####  `Buffer.poolSize`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferpoolsize)
Added in: v0.11.3
  * Type: **Default:** `8192`


This is the size (in bytes) of pre-allocated internal `Buffer` instances used for pooling. This value may be modified.
####  `buf[index]`[#](https://nodejs.org/docs/latest/api/buffer.html#bufindex)
  * `index`


The index operator `[index]` can be used to get and set the octet at position `index` in `buf`. The values refer to individual bytes, so the legal value range is between `0x00` and `0xFF` (hex) or `0` and `255` (decimal).
This operator is inherited from `Uint8Array`, so its behavior on out-of-bounds access is the same as `Uint8Array`. In other words, `buf[index]` returns `undefined` when `index` is negative or greater or equal to `buf.length`, and `buf[index] = value` does not modify the buffer if `index` is negative or `>= buf.length`.
```
import { Buffer } from 'node:buffer';

// Copy an ASCII string into a `Buffer` one byte at a time.
// (This only works for ASCII-only strings. In general, one should use
// `Buffer.from()` to perform this conversion.)

const str = 'Node.js';
const buf = Buffer.allocUnsafe(str.length);

for (let i = 0; i < str.length; i++) {
  buf[i] = str.charCodeAt(i);
}

console.log(buf.toString('utf8'));
// Prints: Node.js
const { Buffer } = require('node:buffer');

// Copy an ASCII string into a `Buffer` one byte at a time.
// (This only works for ASCII-only strings. In general, one should use
// `Buffer.from()` to perform this conversion.)

const str = 'Node.js';
const buf = Buffer.allocUnsafe(str.length);

for (let i = 0; i < str.length; i++) {
  buf[i] = str.charCodeAt(i);
}

console.log(buf.toString('utf8'));
// Prints: Node.js
copy
```

####  `buf.buffer`[#](https://nodejs.org/docs/latest/api/buffer.html#bufbuffer)
  * Type: `ArrayBuffer` object based on which this `Buffer` object is created.


This `ArrayBuffer` is not guaranteed to correspond exactly to the original `Buffer`. See the notes on `buf.byteOffset` for details.
```
import { Buffer } from 'node:buffer';

const arrayBuffer = new ArrayBuffer(16);
const buffer = Buffer.from(arrayBuffer);

console.log(buffer.buffer === arrayBuffer);
// Prints: true
const { Buffer } = require('node:buffer');

const arrayBuffer = new ArrayBuffer(16);
const buffer = Buffer.from(arrayBuffer);

console.log(buffer.buffer === arrayBuffer);
// Prints: true
copy
```

####  `buf.byteOffset`[#](https://nodejs.org/docs/latest/api/buffer.html#bufbyteoffset)
  * Type: `byteOffset` of the `Buffer`'s underlying `ArrayBuffer` object.


When setting `byteOffset` in `Buffer.from(ArrayBuffer, byteOffset, length)`, or sometimes when allocating a `Buffer` smaller than `Buffer.poolSize`, the buffer does not start from a zero offset on the underlying `ArrayBuffer`.
This can cause problems when accessing the underlying `ArrayBuffer` directly using `buf.buffer`, as other parts of the `ArrayBuffer` may be unrelated to the `Buffer` object itself.
A common issue when creating a `TypedArray` object that shares its memory with a `Buffer` is that in this case one needs to specify the `byteOffset` correctly:
```
import { Buffer } from 'node:buffer';

// Create a buffer smaller than `Buffer.poolSize`.
const nodeBuffer = Buffer.from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

// When casting the Node.js Buffer to an Int8Array, use the byteOffset
// to refer only to the part of `nodeBuffer.buffer` that contains the memory
// for `nodeBuffer`.
new Int8Array(nodeBuffer.buffer, nodeBuffer.byteOffset, nodeBuffer.length);
const { Buffer } = require('node:buffer');

// Create a buffer smaller than `Buffer.poolSize`.
const nodeBuffer = Buffer.from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);

// When casting the Node.js Buffer to an Int8Array, use the byteOffset
// to refer only to the part of `nodeBuffer.buffer` that contains the memory
// for `nodeBuffer`.
new Int8Array(nodeBuffer.buffer, nodeBuffer.byteOffset, nodeBuffer.length);
copy
```

####  `buf.compare(target[, targetStart[, targetEnd[, sourceStart[, sourceEnd]]]])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufcomparetarget-targetstart-targetend-sourcestart-sourceend)
Added in: v0.11.13History Version | Changes
---|---
v8.0.0 | The `target` parameter can now be a `Uint8Array`.
v5.11.0 | Additional parameters for specifying offsets are supported now.
  * `target` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer` or `buf`.
  * `targetStart` `target` at which to begin comparison. **Default:** `0`.
  * `targetEnd` `target` at which to end comparison (not inclusive). **Default:** `target.length`.
  * `sourceStart` `buf` at which to begin comparison. **Default:** `0`.
  * `sourceEnd` `buf` at which to end comparison (not inclusive). **Default:** [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength).
  * Returns:


Compares `buf` with `target` and returns a number indicating whether `buf` comes before, after, or is the same as `target` in sort order. Comparison is based on the actual sequence of bytes in each `Buffer`.
  * `0` is returned if `target` is the same as `buf`
  * `1` is returned if `target` should come _before_ `buf` when sorted.
  * `-1` is returned if `target` should come _after_ `buf` when sorted.

```
import { Buffer } from 'node:buffer';

const buf1 = Buffer.from('ABC');
const buf2 = Buffer.from('BCD');
const buf3 = Buffer.from('ABCD');

console.log(buf1.compare(buf1));
// Prints: 0
console.log(buf1.compare(buf2));
// Prints: -1
console.log(buf1.compare(buf3));
// Prints: -1
console.log(buf2.compare(buf1));
// Prints: 1
console.log(buf2.compare(buf3));
// Prints: 1
console.log([buf1, buf2, buf3].sort(Buffer.compare));
// Prints: [ <Buffer 41 42 43>, <Buffer 41 42 43 44>, <Buffer 42 43 44> ]
// (This result is equal to: [buf1, buf3, buf2].)
const { Buffer } = require('node:buffer');

const buf1 = Buffer.from('ABC');
const buf2 = Buffer.from('BCD');
const buf3 = Buffer.from('ABCD');

console.log(buf1.compare(buf1));
// Prints: 0
console.log(buf1.compare(buf2));
// Prints: -1
console.log(buf1.compare(buf3));
// Prints: -1
console.log(buf2.compare(buf1));
// Prints: 1
console.log(buf2.compare(buf3));
// Prints: 1
console.log([buf1, buf2, buf3].sort(Buffer.compare));
// Prints: [ <Buffer 41 42 43>, <Buffer 41 42 43 44>, <Buffer 42 43 44> ]
// (This result is equal to: [buf1, buf3, buf2].)
copy
```

The optional `targetStart`, `targetEnd`, `sourceStart`, and `sourceEnd` arguments can be used to limit the comparison to specific ranges within `target` and `buf` respectively.
```
import { Buffer } from 'node:buffer';

const buf1 = Buffer.from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
const buf2 = Buffer.from([5, 6, 7, 8, 9, 1, 2, 3, 4]);

console.log(buf1.compare(buf2, 5, 9, 0, 4));
// Prints: 0
console.log(buf1.compare(buf2, 0, 6, 4));
// Prints: -1
console.log(buf1.compare(buf2, 5, 6, 5));
