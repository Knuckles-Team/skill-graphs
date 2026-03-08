
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
copy
```

####  `buf.values()`[#](https://nodejs.org/docs/latest/api/buffer.html#bufvalues)
Added in: v1.1.0
  * Returns:


Creates and returns an `buf` values (bytes). This function is called automatically when a `Buffer` is used in a `for..of` statement.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from('buffer');

for (const value of buf.values()) {
  console.log(value);
}
// Prints:
//   98
//   117
//   102
//   102
//   101
//   114

for (const value of buf) {
  console.log(value);
}
// Prints:
//   98
//   117
//   102
//   102
//   101
//   114
const { Buffer } = require('node:buffer');

const buf = Buffer.from('buffer');

for (const value of buf.values()) {
  console.log(value);
}
// Prints:
//   98
//   117
//   102
//   102
//   101
//   114

for (const value of buf) {
  console.log(value);
}
// Prints:
//   98
//   117
//   102
//   102
//   101
//   114
copy
```

####  `buf.write(string[, offset[, length]][, encoding])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwritestring-offset-length-encoding)
Added in: v0.1.90History Version | Changes
---|---
v25.5.0 | supports Uint8Array as `this` value.
  * `string` `buf`.
  * `offset` `string`. **Default:** `0`.
  * `length` `buf.length - offset`). **Default:** `buf.length - offset`.
  * `encoding` `string`. **Default:** `'utf8'`.
  * Returns:


Writes `string` to `buf` at `offset` according to the character encoding in `encoding`. The `length` parameter is the number of bytes to write. If `buf` did not contain enough space to fit the entire string, only part of `string` will be written. However, partially encoded characters will not be written.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.alloc(256);

const len = buf.write('\u00bd + \u00bc = \u00be', 0);

console.log(`${len} bytes: ${buf.toString('utf8', 0, len)}`);
// Prints: 12 bytes: ½ + ¼ = ¾

const buffer = Buffer.alloc(10);

const length = buffer.write('abcd', 8);

console.log(`${length} bytes: ${buffer.toString('utf8', 8, 10)}`);
// Prints: 2 bytes : ab
const { Buffer } = require('node:buffer');

const buf = Buffer.alloc(256);

const len = buf.write('\u00bd + \u00bc = \u00be', 0);

console.log(`${len} bytes: ${buf.toString('utf8', 0, len)}`);
// Prints: 12 bytes: ½ + ¼ = ¾

const buffer = Buffer.alloc(10);

const length = buffer.write('abcd', 8);

console.log(`${length} bytes: ${buffer.toString('utf8', 8, 10)}`);
// Prints: 2 bytes : ab
copy
```

####  `buf.writeBigInt64BE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwritebigint64bevalue-offset)
Added in: v12.0.0, v10.20.0
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as big-endian.
`value` is interpreted and written as a two's complement signed integer.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(8);

buf.writeBigInt64BE(0x0102030405060708n, 0);

console.log(buf);
// Prints: <Buffer 01 02 03 04 05 06 07 08>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(8);

buf.writeBigInt64BE(0x0102030405060708n, 0);

console.log(buf);
// Prints: <Buffer 01 02 03 04 05 06 07 08>
copy
```

####  `buf.writeBigInt64LE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwritebigint64levalue-offset)
Added in: v12.0.0, v10.20.0
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as little-endian.
`value` is interpreted and written as a two's complement signed integer.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(8);

buf.writeBigInt64LE(0x0102030405060708n, 0);

console.log(buf);
// Prints: <Buffer 08 07 06 05 04 03 02 01>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(8);

buf.writeBigInt64LE(0x0102030405060708n, 0);

console.log(buf);
// Prints: <Buffer 08 07 06 05 04 03 02 01>
copy
```

####  `buf.writeBigUInt64BE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwritebiguint64bevalue-offset)
Added in: v12.0.0, v10.20.0History Version | Changes
---|---
v14.10.0, v12.19.0 | This function is also available as `buf.writeBigUint64BE()`.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as big-endian.
This function is also available under the `writeBigUint64BE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(8);

buf.writeBigUInt64BE(0xdecafafecacefaden, 0);

console.log(buf);
// Prints: <Buffer de ca fa fe ca ce fa de>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(8);

buf.writeBigUInt64BE(0xdecafafecacefaden, 0);

console.log(buf);
// Prints: <Buffer de ca fa fe ca ce fa de>
copy
```

####  `buf.writeBigUInt64LE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwritebiguint64levalue-offset)
Added in: v12.0.0, v10.20.0History Version | Changes
---|---
v14.10.0, v12.19.0 | This function is also available as `buf.writeBigUint64LE()`.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as little-endian
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(8);

buf.writeBigUInt64LE(0xdecafafecacefaden, 0);

console.log(buf);
// Prints: <Buffer de fa ce ca fe fa ca de>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(8);

buf.writeBigUInt64LE(0xdecafafecacefaden, 0);

console.log(buf);
// Prints: <Buffer de fa ce ca fe fa ca de>
copy
```

This function is also available under the `writeBigUint64LE` alias.
####  `buf.writeDoubleBE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwritedoublebevalue-offset)
Added in: v0.11.15History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as big-endian. The `value` must be a JavaScript number. Behavior is undefined when `value` is anything other than a JavaScript number.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(8);

buf.writeDoubleBE(123.456, 0);

console.log(buf);
// Prints: <Buffer 40 5e dd 2f 1a 9f be 77>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(8);

buf.writeDoubleBE(123.456, 0);

console.log(buf);
// Prints: <Buffer 40 5e dd 2f 1a 9f be 77>
copy
```

####  `buf.writeDoubleLE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwritedoublelevalue-offset)
Added in: v0.11.15History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as little-endian. The `value` must be a JavaScript number. Behavior is undefined when `value` is anything other than a JavaScript number.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(8);

buf.writeDoubleLE(123.456, 0);

console.log(buf);
// Prints: <Buffer 77 be 9f 1a 2f dd 5e 40>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(8);

buf.writeDoubleLE(123.456, 0);

console.log(buf);
// Prints: <Buffer 77 be 9f 1a 2f dd 5e 40>
copy
```

####  `buf.writeFloatBE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwritefloatbevalue-offset)
Added in: v0.11.15History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as big-endian. Behavior is undefined when `value` is anything other than a JavaScript number.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeFloatBE(0xcafebabe, 0);

console.log(buf);
// Prints: <Buffer 4f 4a fe bb>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(4);

buf.writeFloatBE(0xcafebabe, 0);

console.log(buf);
// Prints: <Buffer 4f 4a fe bb>
copy
```

####  `buf.writeFloatLE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwritefloatlevalue-offset)
Added in: v0.11.15History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as little-endian. Behavior is undefined when `value` is anything other than a JavaScript number.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeFloatLE(0xcafebabe, 0);

console.log(buf);
// Prints: <Buffer bb fe 4a 4f>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(4);

buf.writeFloatLE(0xcafebabe, 0);

console.log(buf);
// Prints: <Buffer bb fe 4a 4f>
copy
```

####  `buf.writeInt8(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteint8value-offset)
Added in: v0.5.0History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 1`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset`. `value` must be a valid signed 8-bit integer. Behavior is undefined when `value` is anything other than a signed 8-bit integer.
`value` is interpreted and written as a two's complement signed integer.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(2);

buf.writeInt8(2, 0);
buf.writeInt8(-2, 1);

console.log(buf);
// Prints: <Buffer 02 fe>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(2);

buf.writeInt8(2, 0);
buf.writeInt8(-2, 1);

console.log(buf);
// Prints: <Buffer 02 fe>
copy
```

####  `buf.writeInt16BE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteint16bevalue-offset)
Added in: v0.5.5History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 2`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as big-endian. The `value` must be a valid signed 16-bit integer. Behavior is undefined when `value` is anything other than a signed 16-bit integer.
The `value` is interpreted and written as a two's complement signed integer.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(2);

buf.writeInt16BE(0x0102, 0);

console.log(buf);
// Prints: <Buffer 01 02>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(2);

buf.writeInt16BE(0x0102, 0);

console.log(buf);
// Prints: <Buffer 01 02>
copy
```

####  `buf.writeInt16LE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteint16levalue-offset)
Added in: v0.5.5History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 2`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as little-endian. The `value` must be a valid signed 16-bit integer. Behavior is undefined when `value` is anything other than a signed 16-bit integer.
The `value` is interpreted and written as a two's complement signed integer.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(2);

buf.writeInt16LE(0x0304, 0);

console.log(buf);
// Prints: <Buffer 04 03>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(2);

buf.writeInt16LE(0x0304, 0);

console.log(buf);
// Prints: <Buffer 04 03>
copy
```

####  `buf.writeInt32BE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteint32bevalue-offset)
Added in: v0.5.5History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as big-endian. The `value` must be a valid signed 32-bit integer. Behavior is undefined when `value` is anything other than a signed 32-bit integer.
The `value` is interpreted and written as a two's complement signed integer.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeInt32BE(0x01020304, 0);

console.log(buf);
// Prints: <Buffer 01 02 03 04>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(4);

buf.writeInt32BE(0x01020304, 0);

console.log(buf);
// Prints: <Buffer 01 02 03 04>
copy
```

####  `buf.writeInt32LE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteint32levalue-offset)
Added in: v0.5.5History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as little-endian. The `value` must be a valid signed 32-bit integer. Behavior is undefined when `value` is anything other than a signed 32-bit integer.
The `value` is interpreted and written as a two's complement signed integer.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeInt32LE(0x05060708, 0);

console.log(buf);
// Prints: <Buffer 08 07 06 05>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(4);

buf.writeInt32LE(0x05060708, 0);

console.log(buf);
// Prints: <Buffer 08 07 06 05>
copy
```

####  `buf.writeIntBE(value, offset, byteLength)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteintbevalue-offset-bytelength)
Added in: v0.11.15History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset and `byteLength` to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - byteLength`.
  * `byteLength` `0 < byteLength <= 6`.
  * Returns: `offset` plus the number of bytes written.


Writes `byteLength` bytes of `value` to `buf` at the specified `offset` as big-endian. Supports up to 48 bits of accuracy. Behavior is undefined when `value` is anything other than a signed integer.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(6);

buf.writeIntBE(0x1234567890ab, 0, 6);

console.log(buf);
// Prints: <Buffer 12 34 56 78 90 ab>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(6);

buf.writeIntBE(0x1234567890ab, 0, 6);

console.log(buf);
// Prints: <Buffer 12 34 56 78 90 ab>
copy
```

####  `buf.writeIntLE(value, offset, byteLength)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteintlevalue-offset-bytelength)
Added in: v0.11.15History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset and `byteLength` to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - byteLength`.
  * `byteLength` `0 < byteLength <= 6`.
  * Returns: `offset` plus the number of bytes written.


Writes `byteLength` bytes of `value` to `buf` at the specified `offset` as little-endian. Supports up to 48 bits of accuracy. Behavior is undefined when `value` is anything other than a signed integer.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(6);

buf.writeIntLE(0x1234567890ab, 0, 6);

console.log(buf);
// Prints: <Buffer ab 90 78 56 34 12>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(6);

buf.writeIntLE(0x1234567890ab, 0, 6);

console.log(buf);
// Prints: <Buffer ab 90 78 56 34 12>
copy
```

####  `buf.writeUInt8(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteuint8value-offset)
Added in: v0.5.0History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.writeUint8()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 1`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset`. `value` must be a valid unsigned 8-bit integer. Behavior is undefined when `value` is anything other than an unsigned 8-bit integer.
This function is also available under the `writeUint8` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeUInt8(0x3, 0);
buf.writeUInt8(0x4, 1);
buf.writeUInt8(0x23, 2);
buf.writeUInt8(0x42, 3);

console.log(buf);
// Prints: <Buffer 03 04 23 42>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(4);

buf.writeUInt8(0x3, 0);
buf.writeUInt8(0x4, 1);
buf.writeUInt8(0x23, 2);
buf.writeUInt8(0x42, 3);

console.log(buf);
// Prints: <Buffer 03 04 23 42>
copy
```

####  `buf.writeUInt16BE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteuint16bevalue-offset)
Added in: v0.5.5History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.writeUint16BE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 2`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as big-endian. The `value` must be a valid unsigned 16-bit integer. Behavior is undefined when `value` is anything other than an unsigned 16-bit integer.
This function is also available under the `writeUint16BE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeUInt16BE(0xdead, 0);
buf.writeUInt16BE(0xbeef, 2);

console.log(buf);
// Prints: <Buffer de ad be ef>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(4);

buf.writeUInt16BE(0xdead, 0);
buf.writeUInt16BE(0xbeef, 2);

console.log(buf);
// Prints: <Buffer de ad be ef>
copy
```

####  `buf.writeUInt16LE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteuint16levalue-offset)
Added in: v0.5.5History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.writeUint16LE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 2`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as little-endian. The `value` must be a valid unsigned 16-bit integer. Behavior is undefined when `value` is anything other than an unsigned 16-bit integer.
This function is also available under the `writeUint16LE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeUInt16LE(0xdead, 0);
buf.writeUInt16LE(0xbeef, 2);

console.log(buf);
// Prints: <Buffer ad de ef be>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(4);

buf.writeUInt16LE(0xdead, 0);
buf.writeUInt16LE(0xbeef, 2);

console.log(buf);
// Prints: <Buffer ad de ef be>
copy
```

####  `buf.writeUInt32BE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteuint32bevalue-offset)
Added in: v0.5.5History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.writeUint32BE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as big-endian. The `value` must be a valid unsigned 32-bit integer. Behavior is undefined when `value` is anything other than an unsigned 32-bit integer.
This function is also available under the `writeUint32BE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeUInt32BE(0xfeedface, 0);

console.log(buf);
// Prints: <Buffer fe ed fa ce>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(4);

buf.writeUInt32BE(0xfeedface, 0);

console.log(buf);
// Prints: <Buffer fe ed fa ce>
copy
```

####  `buf.writeUInt32LE(value[, offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteuint32levalue-offset)
Added in: v0.5.5History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.writeUint32LE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns: `offset` plus the number of bytes written.


Writes `value` to `buf` at the specified `offset` as little-endian. The `value` must be a valid unsigned 32-bit integer. Behavior is undefined when `value` is anything other than an unsigned 32-bit integer.
This function is also available under the `writeUint32LE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(4);

buf.writeUInt32LE(0xfeedface, 0);

console.log(buf);
// Prints: <Buffer ce fa ed fe>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(4);

buf.writeUInt32LE(0xfeedface, 0);

console.log(buf);
// Prints: <Buffer ce fa ed fe>
copy
```

####  `buf.writeUIntBE(value, offset, byteLength)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteuintbevalue-offset-bytelength)
Added in: v0.5.5History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.writeUintBE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset and `byteLength` to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - byteLength`.
  * `byteLength` `0 < byteLength <= 6`.
  * Returns: `offset` plus the number of bytes written.


Writes `byteLength` bytes of `value` to `buf` at the specified `offset` as big-endian. Supports up to 48 bits of accuracy. Behavior is undefined when `value` is anything other than an unsigned integer.
This function is also available under the `writeUintBE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(6);

buf.writeUIntBE(0x1234567890ab, 0, 6);

console.log(buf);
// Prints: <Buffer 12 34 56 78 90 ab>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(6);

buf.writeUIntBE(0x1234567890ab, 0, 6);

console.log(buf);
// Prints: <Buffer 12 34 56 78 90 ab>
copy
```

####  `buf.writeUIntLE(value, offset, byteLength)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufwriteuintlevalue-offset-bytelength)
Added in: v0.5.5History Version | Changes
---|---
v14.9.0, v12.19.0 | This function is also available as `buf.writeUintLE()`.
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset and `byteLength` to `uint32` anymore.
  * `value` `buf`.
  * `offset` `0 <= offset <= buf.length - byteLength`.
  * `byteLength` `0 < byteLength <= 6`.
  * Returns: `offset` plus the number of bytes written.


Writes `byteLength` bytes of `value` to `buf` at the specified `offset` as little-endian. Supports up to 48 bits of accuracy. Behavior is undefined when `value` is anything other than an unsigned integer.
This function is also available under the `writeUintLE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(6);

buf.writeUIntLE(0x1234567890ab, 0, 6);

console.log(buf);
// Prints: <Buffer ab 90 78 56 34 12>
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(6);

buf.writeUIntLE(0x1234567890ab, 0, 6);

console.log(buf);
// Prints: <Buffer ab 90 78 56 34 12>
copy
```

####  `new Buffer(array)`[#](https://nodejs.org/docs/latest/api/buffer.html#new-bufferarray)
Deprecated in: v6.0.0History Version | Changes
---|---
v10.0.0 | Calling this constructor emits a deprecation warning when run from code outside the `node_modules` directory.
v7.2.1 | Calling this constructor no longer emits a deprecation warning.
