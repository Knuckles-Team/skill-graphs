copy
```

####  `buf.readInt8([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadint8offset)
Added in: v0.5.0History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 1`. **Default:** `0`.
  * Returns:


Reads a signed 8-bit integer from `buf` at the specified `offset`.
Integers read from a `Buffer` are interpreted as two's complement signed values.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([-1, 5]);

console.log(buf.readInt8(0));
// Prints: -1
console.log(buf.readInt8(1));
// Prints: 5
console.log(buf.readInt8(2));
// Throws ERR_OUT_OF_RANGE.
const { Buffer } = require('node:buffer');

const buf = Buffer.from([-1, 5]);

console.log(buf.readInt8(0));
// Prints: -1
console.log(buf.readInt8(1));
// Prints: 5
console.log(buf.readInt8(2));
// Throws ERR_OUT_OF_RANGE.
copy
```

####  `buf.readInt16BE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadint16beoffset)
Added in: v0.5.5History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 2`. **Default:** `0`.
  * Returns:


Reads a signed, big-endian 16-bit integer from `buf` at the specified `offset`.
Integers read from a `Buffer` are interpreted as two's complement signed values.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0, 5]);

console.log(buf.readInt16BE(0));
// Prints: 5
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0, 5]);

console.log(buf.readInt16BE(0));
// Prints: 5
copy
```

####  `buf.readInt16LE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadint16leoffset)
Added in: v0.5.5History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 2`. **Default:** `0`.
  * Returns:


Reads a signed, little-endian 16-bit integer from `buf` at the specified `offset`.
Integers read from a `Buffer` are interpreted as two's complement signed values.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0, 5]);

console.log(buf.readInt16LE(0));
// Prints: 1280
console.log(buf.readInt16LE(1));
// Throws ERR_OUT_OF_RANGE.
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0, 5]);

console.log(buf.readInt16LE(0));
// Prints: 1280
console.log(buf.readInt16LE(1));
// Throws ERR_OUT_OF_RANGE.
copy
```

####  `buf.readInt32BE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadint32beoffset)
Added in: v0.5.5History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns:


Reads a signed, big-endian 32-bit integer from `buf` at the specified `offset`.
Integers read from a `Buffer` are interpreted as two's complement signed values.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0, 0, 0, 5]);

console.log(buf.readInt32BE(0));
// Prints: 5
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0, 0, 0, 5]);

console.log(buf.readInt32BE(0));
// Prints: 5
copy
```

####  `buf.readInt32LE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadint32leoffset)
Added in: v0.5.5History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns:


Reads a signed, little-endian 32-bit integer from `buf` at the specified `offset`.
Integers read from a `Buffer` are interpreted as two's complement signed values.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0, 0, 0, 5]);

console.log(buf.readInt32LE(0));
// Prints: 83886080
console.log(buf.readInt32LE(1));
// Throws ERR_OUT_OF_RANGE.
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0, 0, 0, 5]);

console.log(buf.readInt32LE(0));
// Prints: 83886080
console.log(buf.readInt32LE(1));
// Throws ERR_OUT_OF_RANGE.
copy
```

####  `buf.readIntBE(offset, byteLength)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadintbeoffset-bytelength)
Added in: v0.11.15History Version | Changes
---|---
v25.5.0 | supports Uint8Array as `this` value.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset and `byteLength` to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - byteLength`.
  * `byteLength` `0 < byteLength <= 6`.
  * Returns:


Reads `byteLength` number of bytes from `buf` at the specified `offset` and interprets the result as a big-endian, two's complement signed value supporting up to 48 bits of accuracy.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);

console.log(buf.readIntBE(0, 6).toString(16));
// Prints: 1234567890ab
console.log(buf.readIntBE(1, 6).toString(16));
// Throws ERR_OUT_OF_RANGE.
console.log(buf.readIntBE(1, 0).toString(16));
// Throws ERR_OUT_OF_RANGE.
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);

console.log(buf.readIntBE(0, 6).toString(16));
// Prints: 1234567890ab
console.log(buf.readIntBE(1, 6).toString(16));
// Throws ERR_OUT_OF_RANGE.
console.log(buf.readIntBE(1, 0).toString(16));
// Throws ERR_OUT_OF_RANGE.
copy
```

####  `buf.readIntLE(offset, byteLength)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadintleoffset-bytelength)
Added in: v0.11.15History Version | Changes
---|---
v25.5.0 | supports Uint8Array as `this` value.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset and `byteLength` to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - byteLength`.
  * `byteLength` `0 < byteLength <= 6`.
  * Returns:


Reads `byteLength` number of bytes from `buf` at the specified `offset` and interprets the result as a little-endian, two's complement signed value supporting up to 48 bits of accuracy.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);

console.log(buf.readIntLE(0, 6).toString(16));
// Prints: -546f87a9cbee
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);

console.log(buf.readIntLE(0, 6).toString(16));
// Prints: -546f87a9cbee
copy
```

####  `buf.readUInt8([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreaduint8offset)
Added in: v0.5.0History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.readUint8()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 1`. **Default:** `0`.
  * Returns:


Reads an unsigned 8-bit integer from `buf` at the specified `offset`.
This function is also available under the `readUint8` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([1, -2]);

console.log(buf.readUInt8(0));
// Prints: 1
console.log(buf.readUInt8(1));
// Prints: 254
console.log(buf.readUInt8(2));
// Throws ERR_OUT_OF_RANGE.
const { Buffer } = require('node:buffer');

const buf = Buffer.from([1, -2]);

console.log(buf.readUInt8(0));
// Prints: 1
console.log(buf.readUInt8(1));
// Prints: 254
console.log(buf.readUInt8(2));
// Throws ERR_OUT_OF_RANGE.
copy
```

####  `buf.readUInt16BE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreaduint16beoffset)
Added in: v0.5.5History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.readUint16BE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 2`. **Default:** `0`.
  * Returns:


Reads an unsigned, big-endian 16-bit integer from `buf` at the specified `offset`.
This function is also available under the `readUint16BE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x12, 0x34, 0x56]);

console.log(buf.readUInt16BE(0).toString(16));
// Prints: 1234
console.log(buf.readUInt16BE(1).toString(16));
// Prints: 3456
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x12, 0x34, 0x56]);

console.log(buf.readUInt16BE(0).toString(16));
// Prints: 1234
console.log(buf.readUInt16BE(1).toString(16));
// Prints: 3456
copy
```

####  `buf.readUInt16LE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreaduint16leoffset)
Added in: v0.5.5History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.readUint16LE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 2`. **Default:** `0`.
  * Returns:


Reads an unsigned, little-endian 16-bit integer from `buf` at the specified `offset`.
This function is also available under the `readUint16LE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x12, 0x34, 0x56]);

console.log(buf.readUInt16LE(0).toString(16));
// Prints: 3412
console.log(buf.readUInt16LE(1).toString(16));
// Prints: 5634
console.log(buf.readUInt16LE(2).toString(16));
// Throws ERR_OUT_OF_RANGE.
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x12, 0x34, 0x56]);

console.log(buf.readUInt16LE(0).toString(16));
// Prints: 3412
console.log(buf.readUInt16LE(1).toString(16));
// Prints: 5634
console.log(buf.readUInt16LE(2).toString(16));
// Throws ERR_OUT_OF_RANGE.
copy
```

####  `buf.readUInt32BE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreaduint32beoffset)
Added in: v0.5.5History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.readUint32BE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns:


Reads an unsigned, big-endian 32-bit integer from `buf` at the specified `offset`.
This function is also available under the `readUint32BE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78]);

console.log(buf.readUInt32BE(0).toString(16));
// Prints: 12345678
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78]);

console.log(buf.readUInt32BE(0).toString(16));
// Prints: 12345678
copy
```

####  `buf.readUInt32LE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreaduint32leoffset)
Added in: v0.5.5History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.readUint32LE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns:


Reads an unsigned, little-endian 32-bit integer from `buf` at the specified `offset`.
This function is also available under the `readUint32LE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78]);

console.log(buf.readUInt32LE(0).toString(16));
// Prints: 78563412
console.log(buf.readUInt32LE(1).toString(16));
// Throws ERR_OUT_OF_RANGE.
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78]);

console.log(buf.readUInt32LE(0).toString(16));
// Prints: 78563412
console.log(buf.readUInt32LE(1).toString(16));
// Throws ERR_OUT_OF_RANGE.
copy
```

####  `buf.readUIntBE(offset, byteLength)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreaduintbeoffset-bytelength)
Added in: v0.11.15History Version | Changes
---|---
v25.5.0 | supports Uint8Array as `this` value.
v14.9.0, v12.19.0 | This function is also available as `buf.readUintBE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset and `byteLength` to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - byteLength`.
  * `byteLength` `0 < byteLength <= 6`.
  * Returns:


Reads `byteLength` number of bytes from `buf` at the specified `offset` and interprets the result as an unsigned big-endian integer supporting up to 48 bits of accuracy.
This function is also available under the `readUintBE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);

console.log(buf.readUIntBE(0, 6).toString(16));
// Prints: 1234567890ab
console.log(buf.readUIntBE(1, 6).toString(16));
// Throws ERR_OUT_OF_RANGE.
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);

console.log(buf.readUIntBE(0, 6).toString(16));
// Prints: 1234567890ab
console.log(buf.readUIntBE(1, 6).toString(16));
// Throws ERR_OUT_OF_RANGE.
copy
```

####  `buf.readUIntLE(offset, byteLength)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreaduintleoffset-bytelength)
Added in: v0.11.15History Version | Changes
---|---
v25.5.0 | supports Uint8Array as `this` value.
v14.9.0, v12.19.0 | This function is also available as `buf.readUintLE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset and `byteLength` to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - byteLength`.
  * `byteLength` `0 < byteLength <= 6`.
  * Returns:


Reads `byteLength` number of bytes from `buf` at the specified `offset` and interprets the result as an unsigned, little-endian integer supporting up to 48 bits of accuracy.
This function is also available under the `readUintLE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);

console.log(buf.readUIntLE(0, 6).toString(16));
// Prints: ab9078563412
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x12, 0x34, 0x56, 0x78, 0x90, 0xab]);

console.log(buf.readUIntLE(0, 6).toString(16));
// Prints: ab9078563412
copy
```

####  `buf.subarray([start[, end]])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufsubarraystart-end)
Added in: v3.0.0
  * `start` `Buffer` will start. **Default:** `0`.
  * `end` `Buffer` will end (not inclusive). **Default:** [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength).
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Returns a new `Buffer` that references the same memory as the original, but offset and cropped by the `start` and `end` indexes.
Specifying `end` greater than [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength) will return the same result as that of `end` equal to [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength).
This method is inherited from
Modifying the new `Buffer` slice will modify the memory in the original `Buffer` because the allocated memory of the two objects overlap.
```
import { Buffer } from 'node:buffer';

// Create a `Buffer` with the ASCII alphabet, take a slice, and modify one byte
// from the original `Buffer`.

const buf1 = Buffer.allocUnsafe(26);

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf1[i] = i + 97;
}

const buf2 = buf1.subarray(0, 3);

console.log(buf2.toString('ascii', 0, buf2.length));
// Prints: abc

buf1[0] = 33;

console.log(buf2.toString('ascii', 0, buf2.length));
// Prints: !bc
const { Buffer } = require('node:buffer');

// Create a `Buffer` with the ASCII alphabet, take a slice, and modify one byte
// from the original `Buffer`.

const buf1 = Buffer.allocUnsafe(26);

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf1[i] = i + 97;
}

const buf2 = buf1.subarray(0, 3);

console.log(buf2.toString('ascii', 0, buf2.length));
// Prints: abc

buf1[0] = 33;

console.log(buf2.toString('ascii', 0, buf2.length));
// Prints: !bc
copy
```

Specifying negative indexes causes the slice to be generated relative to the end of `buf` rather than the beginning.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from('buffer');

console.log(buf.subarray(-6, -1).toString());
// Prints: buffe
// (Equivalent to buf.subarray(0, 5).)

console.log(buf.subarray(-6, -2).toString());
// Prints: buff
// (Equivalent to buf.subarray(0, 4).)

console.log(buf.subarray(-5, -2).toString());
// Prints: uff
// (Equivalent to buf.subarray(1, 4).)
const { Buffer } = require('node:buffer');

const buf = Buffer.from('buffer');

console.log(buf.subarray(-6, -1).toString());
// Prints: buffe
// (Equivalent to buf.subarray(0, 5).)

console.log(buf.subarray(-6, -2).toString());
// Prints: buff
// (Equivalent to buf.subarray(0, 4).)

console.log(buf.subarray(-5, -2).toString());
// Prints: uff
// (Equivalent to buf.subarray(1, 4).)
copy
```

####  `buf.slice([start[, end]])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufslicestart-end)
Added in: v0.3.0History Version | Changes
---|---
v17.5.0, v16.15.0 | The buf.slice() method has been deprecated.
v7.1.0, v6.9.2 | Coercing the offsets to integers now handles values outside the 32-bit integer range properly.
v7.0.0 | All offsets are now coerced to integers before doing any calculations with them.
Stability: 0 - Deprecated: Use [`buf.subarray`](https://nodejs.org/docs/latest/api/buffer.html#bufsubarraystart-end) instead.
  * `start` `Buffer` will start. **Default:** `0`.
  * `end` `Buffer` will end (not inclusive). **Default:** [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength).
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Returns a new `Buffer` that references the same memory as the original, but offset and cropped by the `start` and `end` indexes.
This method is not compatible with the `Uint8Array.prototype.slice()`, which is a superclass of `Buffer`. To copy the slice, use `Uint8Array.prototype.slice()`.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from('buffer');

const copiedBuf = Uint8Array.prototype.slice.call(buf);
copiedBuf[0]++;
console.log(copiedBuf.toString());
// Prints: cuffer

console.log(buf.toString());
// Prints: buffer

// With buf.slice(), the original buffer is modified.
const notReallyCopiedBuf = buf.slice();
notReallyCopiedBuf[0]++;
console.log(notReallyCopiedBuf.toString());
// Prints: cuffer
console.log(buf.toString());
// Also prints: cuffer (!)
const { Buffer } = require('node:buffer');

const buf = Buffer.from('buffer');

const copiedBuf = Uint8Array.prototype.slice.call(buf);
copiedBuf[0]++;
console.log(copiedBuf.toString());
// Prints: cuffer

console.log(buf.toString());
// Prints: buffer

// With buf.slice(), the original buffer is modified.
const notReallyCopiedBuf = buf.slice();
notReallyCopiedBuf[0]++;
console.log(notReallyCopiedBuf.toString());
// Prints: cuffer
console.log(buf.toString());
// Also prints: cuffer (!)
copy
```

####  `buf.swap16()`[#](https://nodejs.org/docs/latest/api/buffer.html#bufswap16)
Added in: v5.10.0
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A reference to `buf`.


Interprets `buf` as an array of unsigned 16-bit integers and swaps the byte order _in-place_. Throws [`ERR_INVALID_BUFFER_SIZE`](https://nodejs.org/docs/latest/api/errors.html#err_invalid_buffer_size) if [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength) is not a multiple of 2.
```
import { Buffer } from 'node:buffer';

const buf1 = Buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);

console.log(buf1);
// Prints: <Buffer 01 02 03 04 05 06 07 08>

buf1.swap16();

console.log(buf1);
// Prints: <Buffer 02 01 04 03 06 05 08 07>

const buf2 = Buffer.from([0x1, 0x2, 0x3]);

buf2.swap16();
// Throws ERR_INVALID_BUFFER_SIZE.
const { Buffer } = require('node:buffer');

const buf1 = Buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);

console.log(buf1);
// Prints: <Buffer 01 02 03 04 05 06 07 08>

buf1.swap16();

console.log(buf1);
// Prints: <Buffer 02 01 04 03 06 05 08 07>

const buf2 = Buffer.from([0x1, 0x2, 0x3]);

buf2.swap16();
// Throws ERR_INVALID_BUFFER_SIZE.
copy
```

One convenient use of `buf.swap16()` is to perform a fast in-place conversion between UTF-16 little-endian and UTF-16 big-endian:
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from('This is little-endian UTF-16', 'utf16le');
buf.swap16(); // Convert to big-endian UTF-16 text.
const { Buffer } = require('node:buffer');

const buf = Buffer.from('This is little-endian UTF-16', 'utf16le');
buf.swap16(); // Convert to big-endian UTF-16 text.
copy
```

####  `buf.swap32()`[#](https://nodejs.org/docs/latest/api/buffer.html#bufswap32)
Added in: v5.10.0
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A reference to `buf`.


Interprets `buf` as an array of unsigned 32-bit integers and swaps the byte order _in-place_. Throws [`ERR_INVALID_BUFFER_SIZE`](https://nodejs.org/docs/latest/api/errors.html#err_invalid_buffer_size) if [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength) is not a multiple of 4.
```
import { Buffer } from 'node:buffer';

const buf1 = Buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);

console.log(buf1);
// Prints: <Buffer 01 02 03 04 05 06 07 08>

buf1.swap32();

console.log(buf1);
// Prints: <Buffer 04 03 02 01 08 07 06 05>

const buf2 = Buffer.from([0x1, 0x2, 0x3]);

buf2.swap32();
// Throws ERR_INVALID_BUFFER_SIZE.
const { Buffer } = require('node:buffer');

const buf1 = Buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);

console.log(buf1);
// Prints: <Buffer 01 02 03 04 05 06 07 08>

buf1.swap32();

console.log(buf1);
// Prints: <Buffer 04 03 02 01 08 07 06 05>

const buf2 = Buffer.from([0x1, 0x2, 0x3]);

buf2.swap32();
// Throws ERR_INVALID_BUFFER_SIZE.
copy
```

####  `buf.swap64()`[#](https://nodejs.org/docs/latest/api/buffer.html#bufswap64)
Added in: v6.3.0
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A reference to `buf`.


Interprets `buf` as an array of 64-bit numbers and swaps byte order _in-place_. Throws [`ERR_INVALID_BUFFER_SIZE`](https://nodejs.org/docs/latest/api/errors.html#err_invalid_buffer_size) if [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength) is not a multiple of 8.
```
import { Buffer } from 'node:buffer';

const buf1 = Buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);

console.log(buf1);
// Prints: <Buffer 01 02 03 04 05 06 07 08>

buf1.swap64();

console.log(buf1);
// Prints: <Buffer 08 07 06 05 04 03 02 01>

const buf2 = Buffer.from([0x1, 0x2, 0x3]);

buf2.swap64();
// Throws ERR_INVALID_BUFFER_SIZE.
const { Buffer } = require('node:buffer');

const buf1 = Buffer.from([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8]);

console.log(buf1);
// Prints: <Buffer 01 02 03 04 05 06 07 08>

buf1.swap64();

console.log(buf1);
// Prints: <Buffer 08 07 06 05 04 03 02 01>

const buf2 = Buffer.from([0x1, 0x2, 0x3]);

buf2.swap64();
// Throws ERR_INVALID_BUFFER_SIZE.
copy
```

####  `buf.toJSON()`[#](https://nodejs.org/docs/latest/api/buffer.html#buftojson)
Added in: v0.9.2
  * Returns:


Returns a JSON representation of `buf`. `Buffer` instance.
`Buffer.from()` accepts objects in the format returned from this method. In particular, `Buffer.from(buf.toJSON())` works like `Buffer.from(buf)`.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x1, 0x2, 0x3, 0x4, 0x5]);
const json = JSON.stringify(buf);

console.log(json);
// Prints: {"type":"Buffer","data":[1,2,3,4,5]}

const copy = JSON.parse(json, (key, value) => {
  return value && value.type === 'Buffer' ?
    Buffer.from(value) :
    value;
});

console.log(copy);
// Prints: <Buffer 01 02 03 04 05>
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x1, 0x2, 0x3, 0x4, 0x5]);
const json = JSON.stringify(buf);

console.log(json);
// Prints: {"type":"Buffer","data":[1,2,3,4,5]}

const copy = JSON.parse(json, (key, value) => {
  return value && value.type === 'Buffer' ?
    Buffer.from(value) :
    value;
});

console.log(copy);
// Prints: <Buffer 01 02 03 04 05>
copy
```

####  `buf.toString([encoding[, start[, end]]])`[#](https://nodejs.org/docs/latest/api/buffer.html#buftostringencoding-start-end)
Added in: v0.1.90History Version | Changes
---|---
v25.5.0 | supports Uint8Array as `this` value.
  * `encoding` **Default:** `'utf8'`.
  * `start` **Default:** `0`.
  * `end` **Default:** [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength).
  * Returns:


Decodes `buf` to a string according to the specified character encoding in `encoding`. `start` and `end` may be passed to decode only a subset of `buf`.
If `encoding` is `'utf8'` and a byte sequence in the input is not valid UTF-8, then each invalid byte is replaced with the replacement character `U+FFFD`.
The maximum length of a string instance (in UTF-16 code units) is available as [`buffer.constants.MAX_STRING_LENGTH`](https://nodejs.org/docs/latest/api/buffer.html#bufferconstantsmax_string_length).
```
import { Buffer } from 'node:buffer';

const buf1 = Buffer.allocUnsafe(26);

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf1[i] = i + 97;
}

console.log(buf1.toString('utf8'));
// Prints: abcdefghijklmnopqrstuvwxyz
console.log(buf1.toString('utf8', 0, 5));
// Prints: abcde

const buf2 = Buffer.from('tést');

console.log(buf2.toString('hex'));
// Prints: 74c3a97374
console.log(buf2.toString('utf8', 0, 3));
// Prints: té
console.log(buf2.toString(undefined, 0, 3));
// Prints: té
const { Buffer } = require('node:buffer');
