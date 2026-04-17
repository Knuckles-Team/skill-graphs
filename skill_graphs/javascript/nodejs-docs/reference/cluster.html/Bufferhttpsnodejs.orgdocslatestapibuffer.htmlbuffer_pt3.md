// Prints: 1
const { Buffer } = require('node:buffer');

const buf1 = Buffer.from([1, 2, 3, 4, 5, 6, 7, 8, 9]);
const buf2 = Buffer.from([5, 6, 7, 8, 9, 1, 2, 3, 4]);

console.log(buf1.compare(buf2, 5, 9, 0, 4));
// Prints: 0
console.log(buf1.compare(buf2, 0, 6, 4));
// Prints: -1
console.log(buf1.compare(buf2, 5, 6, 5));
// Prints: 1
copy
```

[`ERR_OUT_OF_RANGE`](https://nodejs.org/docs/latest/api/errors.html#err_out_of_range) is thrown if `targetStart < 0`, `sourceStart < 0`, `targetEnd > target.byteLength`, or `sourceEnd > source.byteLength`.
####  `buf.copy(target[, targetStart[, sourceStart[, sourceEnd]]])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufcopytarget-targetstart-sourcestart-sourceend)
Added in: v0.1.90
  * `target` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer` or
  * `targetStart` `target` at which to begin writing. **Default:** `0`.
  * `sourceStart` `buf` from which to begin copying. **Default:** `0`.
  * `sourceEnd` `buf` at which to stop copying (not inclusive). **Default:** [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength).
  * Returns:


Copies data from a region of `buf` to a region in `target`, even if the `target` memory region overlaps with `buf`.
`Buffer`s, although it takes different function arguments.
```
import { Buffer } from 'node:buffer';

// Create two `Buffer` instances.
const buf1 = Buffer.allocUnsafe(26);
const buf2 = Buffer.allocUnsafe(26).fill('!');

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf1[i] = i + 97;
}

// Copy `buf1` bytes 16 through 19 into `buf2` starting at byte 8 of `buf2`.
buf1.copy(buf2, 8, 16, 20);
// This is equivalent to:
// buf2.set(buf1.subarray(16, 20), 8);

console.log(buf2.toString('ascii', 0, 25));
// Prints: !!!!!!!!qrst!!!!!!!!!!!!!
const { Buffer } = require('node:buffer');

// Create two `Buffer` instances.
const buf1 = Buffer.allocUnsafe(26);
const buf2 = Buffer.allocUnsafe(26).fill('!');

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf1[i] = i + 97;
}

// Copy `buf1` bytes 16 through 19 into `buf2` starting at byte 8 of `buf2`.
buf1.copy(buf2, 8, 16, 20);
// This is equivalent to:
// buf2.set(buf1.subarray(16, 20), 8);

console.log(buf2.toString('ascii', 0, 25));
// Prints: !!!!!!!!qrst!!!!!!!!!!!!!
copy
```
```
import { Buffer } from 'node:buffer';

// Create a `Buffer` and copy data from one region to an overlapping region
// within the same `Buffer`.

const buf = Buffer.allocUnsafe(26);

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf[i] = i + 97;
}

buf.copy(buf, 0, 4, 10);

console.log(buf.toString());
// Prints: efghijghijklmnopqrstuvwxyz
const { Buffer } = require('node:buffer');

// Create a `Buffer` and copy data from one region to an overlapping region
// within the same `Buffer`.

const buf = Buffer.allocUnsafe(26);

for (let i = 0; i < 26; i++) {
  // 97 is the decimal ASCII value for 'a'.
  buf[i] = i + 97;
}

buf.copy(buf, 0, 4, 10);

console.log(buf.toString());
// Prints: efghijghijklmnopqrstuvwxyz
copy
```

####  `buf.entries()`[#](https://nodejs.org/docs/latest/api/buffer.html#bufentries)
Added in: v1.1.0
  * Returns:


Creates and returns an `[index, byte]` pairs from the contents of `buf`.
```
import { Buffer } from 'node:buffer';

// Log the entire contents of a `Buffer`.

const buf = Buffer.from('buffer');

for (const pair of buf.entries()) {
  console.log(pair);
}
// Prints:
//   [0, 98]
//   [1, 117]
//   [2, 102]
//   [3, 102]
//   [4, 101]
//   [5, 114]
const { Buffer } = require('node:buffer');

// Log the entire contents of a `Buffer`.

const buf = Buffer.from('buffer');

for (const pair of buf.entries()) {
  console.log(pair);
}
// Prints:
//   [0, 98]
//   [1, 117]
//   [2, 102]
//   [3, 102]
//   [4, 101]
//   [5, 114]
copy
```

####  `buf.equals(otherBuffer)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufequalsotherbuffer)
Added in: v0.11.13History Version | Changes
---|---
v8.0.0 | The arguments can now be `Uint8Array`s.
  * `otherBuffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer` or `buf`.
  * Returns:


Returns `true` if both `buf` and `otherBuffer` have exactly the same bytes, `false` otherwise. Equivalent to [`buf.compare(otherBuffer) === 0`](https://nodejs.org/docs/latest/api/buffer.html#bufcomparetarget-targetstart-targetend-sourcestart-sourceend).
```
import { Buffer } from 'node:buffer';

const buf1 = Buffer.from('ABC');
const buf2 = Buffer.from('414243', 'hex');
const buf3 = Buffer.from('ABCD');

console.log(buf1.equals(buf2));
// Prints: true
console.log(buf1.equals(buf3));
// Prints: false
const { Buffer } = require('node:buffer');

const buf1 = Buffer.from('ABC');
const buf2 = Buffer.from('414243', 'hex');
const buf3 = Buffer.from('ABCD');

console.log(buf1.equals(buf2));
// Prints: true
console.log(buf1.equals(buf3));
// Prints: false
copy
```

####  `buf.fill(value[, offset[, end]][, encoding])`[#](https://nodejs.org/docs/latest/api/buffer.html#buffillvalue-offset-end-encoding)
Added in: v0.5.0History Version | Changes
---|---
v11.0.0 | Throws `ERR_OUT_OF_RANGE` instead of `ERR_INDEX_OUT_OF_RANGE`.
v10.0.0 | Negative `end` values throw an `ERR_INDEX_OUT_OF_RANGE` error.
v10.0.0 | Attempting to fill a non-zero length buffer with a zero length buffer triggers a thrown exception.
v10.0.0 | Specifying an invalid string for `value` triggers a thrown exception.
v5.7.0 | The `encoding` parameter is supported now.
  * `value` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `buf`. Empty value (string, Uint8Array, Buffer) is coerced to `0`.
  * `offset` `buf`. **Default:** `0`.
  * `end` `buf` (not inclusive). **Default:** [`buf.length`](https://nodejs.org/docs/latest/api/buffer.html#buflength).
  * `encoding` `value` if `value` is a string. **Default:** `'utf8'`.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A reference to `buf`.


Fills `buf` with the specified `value`. If the `offset` and `end` are not given, the entire `buf` will be filled:
```
import { Buffer } from 'node:buffer';

// Fill a `Buffer` with the ASCII character 'h'.

const b = Buffer.allocUnsafe(50).fill('h');

console.log(b.toString());
// Prints: hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

// Fill a buffer with empty string
const c = Buffer.allocUnsafe(5).fill('');

console.log(c.fill(''));
// Prints: <Buffer 00 00 00 00 00>
const { Buffer } = require('node:buffer');

// Fill a `Buffer` with the ASCII character 'h'.

const b = Buffer.allocUnsafe(50).fill('h');

console.log(b.toString());
// Prints: hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

// Fill a buffer with empty string
const c = Buffer.allocUnsafe(5).fill('');

console.log(c.fill(''));
// Prints: <Buffer 00 00 00 00 00>
copy
```

`value` is coerced to a `uint32` value if it is not a string, `Buffer`, or integer. If the resulting integer is greater than `255` (decimal), `buf` will be filled with `value & 255`.
If the final write of a `fill()` operation falls on a multi-byte character, then only the bytes of that character that fit into `buf` are written:
```
import { Buffer } from 'node:buffer';

// Fill a `Buffer` with character that takes up two bytes in UTF-8.

console.log(Buffer.allocUnsafe(5).fill('\u0222'));
// Prints: <Buffer c8 a2 c8 a2 c8>
const { Buffer } = require('node:buffer');

// Fill a `Buffer` with character that takes up two bytes in UTF-8.

console.log(Buffer.allocUnsafe(5).fill('\u0222'));
// Prints: <Buffer c8 a2 c8 a2 c8>
copy
```

If `value` contains invalid characters, it is truncated; if no valid fill data remains, an exception is thrown:
```
import { Buffer } from 'node:buffer';

const buf = Buffer.allocUnsafe(5);

console.log(buf.fill('a'));
// Prints: <Buffer 61 61 61 61 61>
console.log(buf.fill('aazz', 'hex'));
// Prints: <Buffer aa aa aa aa aa>
console.log(buf.fill('zz', 'hex'));
// Throws an exception.
const { Buffer } = require('node:buffer');

const buf = Buffer.allocUnsafe(5);

console.log(buf.fill('a'));
// Prints: <Buffer 61 61 61 61 61>
console.log(buf.fill('aazz', 'hex'));
// Prints: <Buffer aa aa aa aa aa>
console.log(buf.fill('zz', 'hex'));
// Throws an exception.
copy
```

####  `buf.includes(value[, byteOffset][, encoding])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufincludesvalue-byteoffset-encoding)
Added in: v5.3.0History Version | Changes
---|---
v25.5.0 | supports Uint8Array as `this` value.
  * `value` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `byteOffset` `buf`. If negative, then offset is calculated from the end of `buf`. **Default:** `0`.
  * `encoding` `value` is a string, this is its encoding. **Default:** `'utf8'`.
  * Returns: `true` if `value` was found in `buf`, `false` otherwise.


Equivalent to [`buf.indexOf() !== -1`](https://nodejs.org/docs/latest/api/buffer.html#bufindexofvalue-byteoffset-encoding).
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from('this is a buffer');

console.log(buf.includes('this'));
// Prints: true
console.log(buf.includes('is'));
// Prints: true
console.log(buf.includes(Buffer.from('a buffer')));
// Prints: true
console.log(buf.includes(97));
// Prints: true (97 is the decimal ASCII value for 'a')
console.log(buf.includes(Buffer.from('a buffer example')));
// Prints: false
console.log(buf.includes(Buffer.from('a buffer example').slice(0, 8)));
// Prints: true
console.log(buf.includes('this', 4));
// Prints: false
const { Buffer } = require('node:buffer');

const buf = Buffer.from('this is a buffer');

console.log(buf.includes('this'));
// Prints: true
console.log(buf.includes('is'));
// Prints: true
console.log(buf.includes(Buffer.from('a buffer')));
// Prints: true
console.log(buf.includes(97));
// Prints: true (97 is the decimal ASCII value for 'a')
console.log(buf.includes(Buffer.from('a buffer example')));
// Prints: false
console.log(buf.includes(Buffer.from('a buffer example').slice(0, 8)));
// Prints: true
console.log(buf.includes('this', 4));
// Prints: false
copy
```

####  `buf.indexOf(value[, byteOffset][, encoding])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufindexofvalue-byteoffset-encoding)
Added in: v1.5.0History Version | Changes
---|---
v8.0.0 | The `value` can now be a `Uint8Array`.
v5.7.0, v4.4.0 | When `encoding` is being passed, the `byteOffset` parameter is no longer required.
  * `value` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `byteOffset` `buf`. If negative, then offset is calculated from the end of `buf`. **Default:** `0`.
  * `encoding` `value` is a string, this is the encoding used to determine the binary representation of the string that will be searched for in `buf`. **Default:** `'utf8'`.
  * Returns: `value` in `buf`, or `-1` if `buf` does not contain `value`.


If `value` is:
  * a string, `value` is interpreted according to the character encoding in `encoding`.
  * a `Buffer` or `value` will be used in its entirety. To compare a partial `Buffer`, use [`buf.subarray`](https://nodejs.org/docs/latest/api/buffer.html#bufsubarraystart-end).
  * a number, `value` will be interpreted as an unsigned 8-bit integer value between `0` and `255`.

```
import { Buffer } from 'node:buffer';

const buf = Buffer.from('this is a buffer');

console.log(buf.indexOf('this'));
// Prints: 0
console.log(buf.indexOf('is'));
// Prints: 2
console.log(buf.indexOf(Buffer.from('a buffer')));
// Prints: 8
console.log(buf.indexOf(97));
// Prints: 8 (97 is the decimal ASCII value for 'a')
console.log(buf.indexOf(Buffer.from('a buffer example')));
// Prints: -1
console.log(buf.indexOf(Buffer.from('a buffer example').slice(0, 8)));
// Prints: 8

const utf16Buffer = Buffer.from('\u039a\u0391\u03a3\u03a3\u0395', 'utf16le');

console.log(utf16Buffer.indexOf('\u03a3', 0, 'utf16le'));
// Prints: 4
console.log(utf16Buffer.indexOf('\u03a3', -4, 'utf16le'));
// Prints: 6
const { Buffer } = require('node:buffer');

const buf = Buffer.from('this is a buffer');

console.log(buf.indexOf('this'));
// Prints: 0
console.log(buf.indexOf('is'));
// Prints: 2
console.log(buf.indexOf(Buffer.from('a buffer')));
// Prints: 8
console.log(buf.indexOf(97));
// Prints: 8 (97 is the decimal ASCII value for 'a')
console.log(buf.indexOf(Buffer.from('a buffer example')));
// Prints: -1
console.log(buf.indexOf(Buffer.from('a buffer example').slice(0, 8)));
// Prints: 8

const utf16Buffer = Buffer.from('\u039a\u0391\u03a3\u03a3\u0395', 'utf16le');

console.log(utf16Buffer.indexOf('\u03a3', 0, 'utf16le'));
// Prints: 4
console.log(utf16Buffer.indexOf('\u03a3', -4, 'utf16le'));
// Prints: 6
copy
```

If `value` is not a string, number, or `Buffer`, this method will throw a `TypeError`. If `value` is a number, it will be coerced to a valid byte value, an integer between 0 and 255.
If `byteOffset` is not a number, it will be coerced to a number. If the result of coercion is `NaN` or `0`, then the entire buffer will be searched. This behavior matches
```
import { Buffer } from 'node:buffer';

const b = Buffer.from('abcdef');

// Passing a value that's a number, but not a valid byte.
// Prints: 2, equivalent to searching for 99 or 'c'.
console.log(b.indexOf(99.9));
console.log(b.indexOf(256 + 99));

// Passing a byteOffset that coerces to NaN or 0.
// Prints: 1, searching the whole buffer.
console.log(b.indexOf('b', undefined));
console.log(b.indexOf('b', {}));
console.log(b.indexOf('b', null));
console.log(b.indexOf('b', []));
const { Buffer } = require('node:buffer');

const b = Buffer.from('abcdef');

// Passing a value that's a number, but not a valid byte.
// Prints: 2, equivalent to searching for 99 or 'c'.
console.log(b.indexOf(99.9));
console.log(b.indexOf(256 + 99));

// Passing a byteOffset that coerces to NaN or 0.
// Prints: 1, searching the whole buffer.
console.log(b.indexOf('b', undefined));
console.log(b.indexOf('b', {}));
console.log(b.indexOf('b', null));
console.log(b.indexOf('b', []));
copy
```

If `value` is an empty string or empty `Buffer` and `byteOffset` is less than `buf.length`, `byteOffset` will be returned. If `value` is empty and `byteOffset` is at least `buf.length`, `buf.length` will be returned.
####  `buf.keys()`[#](https://nodejs.org/docs/latest/api/buffer.html#bufkeys)
Added in: v1.1.0
  * Returns:


Creates and returns an `buf` keys (indexes).
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from('buffer');

for (const key of buf.keys()) {
  console.log(key);
}
// Prints:
//   0
//   1
//   2
//   3
//   4
//   5
const { Buffer } = require('node:buffer');

const buf = Buffer.from('buffer');

for (const key of buf.keys()) {
  console.log(key);
}
// Prints:
//   0
//   1
//   2
//   3
//   4
//   5
copy
```

####  `buf.lastIndexOf(value[, byteOffset][, encoding])`[#](https://nodejs.org/docs/latest/api/buffer.html#buflastindexofvalue-byteoffset-encoding)
Added in: v6.0.0History Version | Changes
---|---
v8.0.0 | The `value` can now be a `Uint8Array`.
  * `value` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `byteOffset` `buf`. If negative, then offset is calculated from the end of `buf`. **Default:** `buf.length - 1`.
  * `encoding` `value` is a string, this is the encoding used to determine the binary representation of the string that will be searched for in `buf`. **Default:** `'utf8'`.
  * Returns: `value` in `buf`, or `-1` if `buf` does not contain `value`.


Identical to [`buf.indexOf()`](https://nodejs.org/docs/latest/api/buffer.html#bufindexofvalue-byteoffset-encoding), except the last occurrence of `value` is found rather than the first occurrence.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from('this buffer is a buffer');

console.log(buf.lastIndexOf('this'));
// Prints: 0
console.log(buf.lastIndexOf('buffer'));
// Prints: 17
console.log(buf.lastIndexOf(Buffer.from('buffer')));
// Prints: 17
console.log(buf.lastIndexOf(97));
// Prints: 15 (97 is the decimal ASCII value for 'a')
console.log(buf.lastIndexOf(Buffer.from('yolo')));
// Prints: -1
console.log(buf.lastIndexOf('buffer', 5));
// Prints: 5
console.log(buf.lastIndexOf('buffer', 4));
// Prints: -1

const utf16Buffer = Buffer.from('\u039a\u0391\u03a3\u03a3\u0395', 'utf16le');

console.log(utf16Buffer.lastIndexOf('\u03a3', undefined, 'utf16le'));
// Prints: 6
console.log(utf16Buffer.lastIndexOf('\u03a3', -5, 'utf16le'));
// Prints: 4
const { Buffer } = require('node:buffer');

const buf = Buffer.from('this buffer is a buffer');

console.log(buf.lastIndexOf('this'));
// Prints: 0
console.log(buf.lastIndexOf('buffer'));
// Prints: 17
console.log(buf.lastIndexOf(Buffer.from('buffer')));
// Prints: 17
console.log(buf.lastIndexOf(97));
// Prints: 15 (97 is the decimal ASCII value for 'a')
console.log(buf.lastIndexOf(Buffer.from('yolo')));
// Prints: -1
console.log(buf.lastIndexOf('buffer', 5));
// Prints: 5
console.log(buf.lastIndexOf('buffer', 4));
// Prints: -1

const utf16Buffer = Buffer.from('\u039a\u0391\u03a3\u03a3\u0395', 'utf16le');

console.log(utf16Buffer.lastIndexOf('\u03a3', undefined, 'utf16le'));
// Prints: 6
console.log(utf16Buffer.lastIndexOf('\u03a3', -5, 'utf16le'));
// Prints: 4
copy
```

If `value` is not a string, number, or `Buffer`, this method will throw a `TypeError`. If `value` is a number, it will be coerced to a valid byte value, an integer between 0 and 255.
If `byteOffset` is not a number, it will be coerced to a number. Any arguments that coerce to `NaN`, like `{}` or `undefined`, will search the whole buffer. This behavior matches
```
import { Buffer } from 'node:buffer';

const b = Buffer.from('abcdef');

// Passing a value that's a number, but not a valid byte.
// Prints: 2, equivalent to searching for 99 or 'c'.
console.log(b.lastIndexOf(99.9));
console.log(b.lastIndexOf(256 + 99));

// Passing a byteOffset that coerces to NaN.
// Prints: 1, searching the whole buffer.
console.log(b.lastIndexOf('b', undefined));
console.log(b.lastIndexOf('b', {}));

// Passing a byteOffset that coerces to 0.
// Prints: -1, equivalent to passing 0.
console.log(b.lastIndexOf('b', null));
console.log(b.lastIndexOf('b', []));
const { Buffer } = require('node:buffer');

const b = Buffer.from('abcdef');

// Passing a value that's a number, but not a valid byte.
// Prints: 2, equivalent to searching for 99 or 'c'.
console.log(b.lastIndexOf(99.9));
console.log(b.lastIndexOf(256 + 99));

// Passing a byteOffset that coerces to NaN.
// Prints: 1, searching the whole buffer.
console.log(b.lastIndexOf('b', undefined));
console.log(b.lastIndexOf('b', {}));

// Passing a byteOffset that coerces to 0.
// Prints: -1, equivalent to passing 0.
console.log(b.lastIndexOf('b', null));
console.log(b.lastIndexOf('b', []));
copy
```

If `value` is an empty string or empty `Buffer`, `byteOffset` will be returned.
####  `buf.length`[#](https://nodejs.org/docs/latest/api/buffer.html#buflength)
Added in: v0.1.90
  * Type:


Returns the number of bytes in `buf`.
```
import { Buffer } from 'node:buffer';

// Create a `Buffer` and write a shorter string to it using UTF-8.

const buf = Buffer.alloc(1234);

console.log(buf.length);
// Prints: 1234

buf.write('some string', 0, 'utf8');

console.log(buf.length);
// Prints: 1234
const { Buffer } = require('node:buffer');

// Create a `Buffer` and write a shorter string to it using UTF-8.

const buf = Buffer.alloc(1234);

console.log(buf.length);
// Prints: 1234

buf.write('some string', 0, 'utf8');

console.log(buf.length);
// Prints: 1234
copy
```

####  `buf.parent`[#](https://nodejs.org/docs/latest/api/buffer.html#bufparent)
Deprecated in: v8.0.0
Stability: 0 - Deprecated: Use [`buf.buffer`](https://nodejs.org/docs/latest/api/buffer.html#bufbuffer) instead.
The `buf.parent` property is a deprecated alias for `buf.buffer`.
####  `buf.readBigInt64BE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadbigint64beoffset)
Added in: v12.0.0, v10.20.0
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns:


Reads a signed, big-endian 64-bit integer from `buf` at the specified `offset`.
Integers read from a `Buffer` are interpreted as two's complement signed values.
####  `buf.readBigInt64LE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadbigint64leoffset)
Added in: v12.0.0, v10.20.0
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns:


Reads a signed, little-endian 64-bit integer from `buf` at the specified `offset`.
Integers read from a `Buffer` are interpreted as two's complement signed values.
####  `buf.readBigUInt64BE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadbiguint64beoffset)
Added in: v12.0.0, v10.20.0History Version | Changes
---|---
v14.10.0, v12.19.0 | This function is also available as `buf.readBigUint64BE()`.
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns:


Reads an unsigned, big-endian 64-bit integer from `buf` at the specified `offset`.
This function is also available under the `readBigUint64BE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff]);

console.log(buf.readBigUInt64BE(0));
// Prints: 4294967295n
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff]);

console.log(buf.readBigUInt64BE(0));
// Prints: 4294967295n
copy
```

####  `buf.readBigUInt64LE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadbiguint64leoffset)
Added in: v12.0.0, v10.20.0History Version | Changes
---|---
v14.10.0, v12.19.0 | This function is also available as `buf.readBigUint64LE()`.
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns:


Reads an unsigned, little-endian 64-bit integer from `buf` at the specified `offset`.
This function is also available under the `readBigUint64LE` alias.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff]);

console.log(buf.readBigUInt64LE(0));
// Prints: 18446744069414584320n
const { Buffer } = require('node:buffer');

const buf = Buffer.from([0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff]);

console.log(buf.readBigUInt64LE(0));
// Prints: 18446744069414584320n
copy
```

####  `buf.readDoubleBE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreaddoublebeoffset)
Added in: v0.11.15History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns:


Reads a 64-bit, big-endian double from `buf` at the specified `offset`.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);

console.log(buf.readDoubleBE(0));
// Prints: 8.20788039913184e-304
const { Buffer } = require('node:buffer');

const buf = Buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);

console.log(buf.readDoubleBE(0));
// Prints: 8.20788039913184e-304
copy
```

####  `buf.readDoubleLE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreaddoubleleoffset)
Added in: v0.11.15History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 8`. **Default:** `0`.
  * Returns:


Reads a 64-bit, little-endian double from `buf` at the specified `offset`.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);

console.log(buf.readDoubleLE(0));
// Prints: 5.447603722011605e-270
console.log(buf.readDoubleLE(1));
// Throws ERR_OUT_OF_RANGE.
const { Buffer } = require('node:buffer');

const buf = Buffer.from([1, 2, 3, 4, 5, 6, 7, 8]);

console.log(buf.readDoubleLE(0));
// Prints: 5.447603722011605e-270
console.log(buf.readDoubleLE(1));
// Throws ERR_OUT_OF_RANGE.
copy
```

####  `buf.readFloatBE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadfloatbeoffset)
Added in: v0.11.15History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns:


Reads a 32-bit, big-endian float from `buf` at the specified `offset`.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([1, 2, 3, 4]);

console.log(buf.readFloatBE(0));
// Prints: 2.387939260590663e-38
const { Buffer } = require('node:buffer');

const buf = Buffer.from([1, 2, 3, 4]);

console.log(buf.readFloatBE(0));
// Prints: 2.387939260590663e-38
copy
```

####  `buf.readFloatLE([offset])`[#](https://nodejs.org/docs/latest/api/buffer.html#bufreadfloatleoffset)
Added in: v0.11.15History Version | Changes
---|---
v10.0.0 | Removed `noAssert` and no implicit coercion of the offset to `uint32` anymore.
  * `offset` `0 <= offset <= buf.length - 4`. **Default:** `0`.
  * Returns:


Reads a 32-bit, little-endian float from `buf` at the specified `offset`.
```
import { Buffer } from 'node:buffer';

const buf = Buffer.from([1, 2, 3, 4]);

console.log(buf.readFloatLE(0));
// Prints: 1.539989614439558e-36
console.log(buf.readFloatLE(1));
// Throws ERR_OUT_OF_RANGE.
const { Buffer } = require('node:buffer');

const buf = Buffer.from([1, 2, 3, 4]);

console.log(buf.readFloatLE(0));
// Prints: 1.539989614439558e-36
console.log(buf.readFloatLE(1));
// Throws ERR_OUT_OF_RANGE.
