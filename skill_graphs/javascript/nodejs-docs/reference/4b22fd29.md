v7.0.0 | Calling this constructor emits a deprecation warning now.
Stability: 0 - Deprecated: Use [`Buffer.from(array)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarray) instead.
  * `array`


See [`Buffer.from(array)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarray).
####  `new Buffer(arrayBuffer[, byteOffset[, length]])`[#](https://nodejs.org/docs/latest/api/buffer.html#new-bufferarraybuffer-byteoffset-length)
Added in: v3.0.0Deprecated in: v6.0.0History Version | Changes
---|---
v10.0.0 | Calling this constructor emits a deprecation warning when run from code outside the `node_modules` directory.
v7.2.1 | Calling this constructor no longer emits a deprecation warning.
v7.0.0 | Calling this constructor emits a deprecation warning now.
v6.0.0 | The `byteOffset` and `length` parameters are supported now.
Stability: 0 - Deprecated: Use [`Buffer.from(arrayBuffer[, byteOffset[, length]])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarraybuffer-byteoffset-length) instead.
  * `arrayBuffer` `.buffer` property of a
  * `byteOffset` **Default:** `0`.
  * `length` **Default:** `arrayBuffer.byteLength - byteOffset`.


See [`Buffer.from(arrayBuffer[, byteOffset[, length]])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarraybuffer-byteoffset-length).
####  `new Buffer(buffer)`[#](https://nodejs.org/docs/latest/api/buffer.html#new-bufferbuffer)
Deprecated in: v6.0.0History Version | Changes
---|---
v10.0.0 | Calling this constructor emits a deprecation warning when run from code outside the `node_modules` directory.
v7.2.1 | Calling this constructor no longer emits a deprecation warning.
v7.0.0 | Calling this constructor emits a deprecation warning now.
Stability: 0 - Deprecated: Use [`Buffer.from(buffer)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfrombuffer) instead.
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer` or


See [`Buffer.from(buffer)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfrombuffer).
####  `new Buffer(size)`[#](https://nodejs.org/docs/latest/api/buffer.html#new-buffersize)
Deprecated in: v6.0.0History Version | Changes
---|---
v10.0.0 | Calling this constructor emits a deprecation warning when run from code outside the `node_modules` directory.
v8.0.0 | The `new Buffer(size)` will return zero-filled memory by default.
v7.2.1 | Calling this constructor no longer emits a deprecation warning.
v7.0.0 | Calling this constructor emits a deprecation warning now.
Stability: 0 - Deprecated: Use [`Buffer.alloc()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocsize-fill-encoding) instead (also see [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize)).
  * `size` `Buffer`.


See [`Buffer.alloc()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocsize-fill-encoding) and [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize). This variant of the constructor is equivalent to [`Buffer.alloc()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocsize-fill-encoding).
####  `new Buffer(string[, encoding])`[#](https://nodejs.org/docs/latest/api/buffer.html#new-bufferstring-encoding)
Deprecated in: v6.0.0History Version | Changes
---|---
v10.0.0 | Calling this constructor emits a deprecation warning when run from code outside the `node_modules` directory.
v7.2.1 | Calling this constructor no longer emits a deprecation warning.
v7.0.0 | Calling this constructor emits a deprecation warning now.
Stability: 0 - Deprecated: Use [`Buffer.from(string[, encoding])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromstring-encoding) instead.
  * `string`
  * `encoding` `string`. **Default:** `'utf8'`.


See [`Buffer.from(string[, encoding])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromstring-encoding).
### Class: `File`[#](https://nodejs.org/docs/latest/api/buffer.html#class-file)
Added in: v19.2.0, v18.13.0History Version | Changes
---|---
v23.0.0 | Makes File instances cloneable.
v20.0.0 | No longer experimental.
  * Extends: [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob)


A [`<File>`](https://nodejs.org/docs/latest/api/buffer.html#class-file) provides information about files.
####  `new buffer.File(sources, fileName[, options])`[#](https://nodejs.org/docs/latest/api/buffer.html#new-bufferfilesources-filename-options)
Added in: v19.2.0, v18.13.0
  * `sources` [`<Blob[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) | [`<File[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-file) An array of string, [`<File>`](https://nodejs.org/docs/latest/api/buffer.html#class-file), or [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) objects, or any mix of such objects, that will be stored within the `File`.
  * `fileName`
  * `options`
    * `endings` `'transparent'` or `'native'`. When set to `'native'`, line endings in string source parts will be converted to the platform native line-ending as specified by `require('node:os').EOL`.
    * `type`
    * `lastModified` **Default:** `Date.now()`.


####  `file.name`[#](https://nodejs.org/docs/latest/api/buffer.html#filename)
Added in: v19.2.0, v18.13.0
  * Type:


The name of the `File`.
####  `file.lastModified`[#](https://nodejs.org/docs/latest/api/buffer.html#filelastmodified)
Added in: v19.2.0, v18.13.0
  * Type:


The last modified date of the `File`.
###  `node:buffer` module APIs[#](https://nodejs.org/docs/latest/api/buffer.html#nodebuffer-module-apis)
While, the `Buffer` object is available as a global, there are additional `Buffer`-related APIs that are available only via the `node:buffer` module accessed using `require('node:buffer')`.
####  `buffer.atob(data)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferatobdata)
Added in: v15.13.0, v14.17.0
Stability: 3 - Legacy. Use `Buffer.from(data, 'base64')` instead.
  * `data`


Decodes a string of Base64-encoded data into bytes, and encodes those bytes into a string using Latin-1 (ISO-8859-1).
The `data` may be any JavaScript-value that can be coerced into a string.
**This function is only provided for compatibility with legacy web platform APIs and should never be used in new code, because they use strings to represent binary data and predate the introduction of typed arrays in JavaScript. For code running using Node.js APIs, converting between base64-encoded strings and binary data should be performed using`Buffer.from(str, 'base64')` and `buf.toString('base64')`.**
An automated migration is available (
```
npx codemod@latest @nodejs/buffer-atob-btoa
copy
```

####  `buffer.btoa(data)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferbtoadata)
Added in: v15.13.0, v14.17.0
Stability: 3 - Legacy. Use `buf.toString('base64')` instead.
  * `data`


Decodes a string into bytes using Latin-1 (ISO-8859), and encodes those bytes into a string using Base64.
The `data` may be any JavaScript-value that can be coerced into a string.
**This function is only provided for compatibility with legacy web platform APIs and should never be used in new code, because they use strings to represent binary data and predate the introduction of typed arrays in JavaScript. For code running using Node.js APIs, converting between base64-encoded strings and binary data should be performed using`Buffer.from(str, 'base64')` and `buf.toString('base64')`.**
An automated migration is available (
```
npx codemod@latest @nodejs/buffer-atob-btoa
copy
```

####  `buffer.isAscii(input)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferisasciiinput)
Added in: v19.6.0, v18.15.0
  * `input` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns:


This function returns `true` if `input` contains only valid ASCII-encoded data, including the case in which `input` is empty.
Throws if the `input` is a detached array buffer.
####  `buffer.isUtf8(input)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferisutf8input)
Added in: v19.4.0, v18.14.0
  * `input` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns:


This function returns `true` if `input` contains only valid UTF-8-encoded data, including the case in which `input` is empty.
Throws if the `input` is a detached array buffer.
####  `buffer.INSPECT_MAX_BYTES`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferinspect-max-bytes)
Added in: v0.5.4
  * Type: **Default:** `50`


Returns the maximum number of bytes that will be returned when `buf.inspect()` is called. This can be overridden by user modules. See [`util.inspect()`](https://nodejs.org/docs/latest/api/util.html#utilinspectobject-options) for more details on `buf.inspect()` behavior.
####  `buffer.kMaxLength`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferkmaxlength)
Added in: v3.0.0
  * Type: `Buffer` instance.


An alias for [`buffer.constants.MAX_LENGTH`](https://nodejs.org/docs/latest/api/buffer.html#bufferconstantsmax_length).
####  `buffer.kStringMaxLength`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferkstringmaxlength)
Added in: v3.0.0
  * Type: `string` instance.


An alias for [`buffer.constants.MAX_STRING_LENGTH`](https://nodejs.org/docs/latest/api/buffer.html#bufferconstantsmax_string_length).
####  `buffer.resolveObjectURL(id)`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferresolveobjecturlid)
Added in: v16.7.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `id` `'blob:nodedata:...` URL string returned by a prior call to `URL.createObjectURL()`.
  * Returns: [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob)


Resolves a `'blob:nodedata:...'` an associated [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) object registered using a prior call to `URL.createObjectURL()`.
####  `buffer.transcode(source, fromEnc, toEnc)`[#](https://nodejs.org/docs/latest/api/buffer.html#buffertranscodesource-fromenc-toenc)
Added in: v7.1.0History Version | Changes
---|---
v8.0.0 | The `source` parameter can now be a `Uint8Array`.
  * `source` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer` or `Uint8Array` instance.
  * `fromEnc`
  * `toEnc`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Re-encodes the given `Buffer` or `Uint8Array` instance from one character encoding to another. Returns a new `Buffer` instance.
Throws if the `fromEnc` or `toEnc` specify invalid character encodings or if conversion from `fromEnc` to `toEnc` is not permitted.
Encodings supported by `buffer.transcode()` are: `'ascii'`, `'utf8'`, `'utf16le'`, `'ucs2'`, `'latin1'`, and `'binary'`.
The transcoding process will use substitution characters if a given byte sequence cannot be adequately represented in the target encoding. For instance:
```
import { Buffer, transcode } from 'node:buffer';

const newBuf = transcode(Buffer.from('€'), 'utf8', 'ascii');
console.log(newBuf.toString('ascii'));
// Prints: '?'
const { Buffer, transcode } = require('node:buffer');

const newBuf = transcode(Buffer.from('€'), 'utf8', 'ascii');
console.log(newBuf.toString('ascii'));
// Prints: '?'
copy
```

Because the Euro (`€`) sign is not representable in US-ASCII, it is replaced with `?` in the transcoded `Buffer`.
#### Buffer constants[#](https://nodejs.org/docs/latest/api/buffer.html#buffer-constants)
Added in: v8.2.0
#####  `buffer.constants.MAX_LENGTH`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferconstantsmax-length)
Added in: v8.2.0History Version | Changes
---|---
v22.0.0 | Value is changed to 253 - 1 on 64-bit architectures, and 231 - 1 on 32-bit architectures.
v15.0.0 | Value is changed to 232 on 64-bit architectures.
v14.0.0 | Value is changed from 231 - 1 to 232 - 1 on 64-bit architectures.
  * Type: `Buffer` instance.


On 32-bit architectures, this value is equal to 231 - 1 (about 2 GiB).
On 64-bit architectures, this value is equal to 53 - 1, about 8 PiB).
It reflects
This value is also available as [`buffer.kMaxLength`](https://nodejs.org/docs/latest/api/buffer.html#bufferkmaxlength).
#####  `buffer.constants.MAX_STRING_LENGTH`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferconstantsmax-string-length)
Added in: v8.2.0
  * Type: `string` instance.


Represents the largest `length` that a `string` primitive can have, counted in UTF-16 code units.
This value may depend on the JS engine that is being used.
###  `Buffer.from()`, `Buffer.alloc()`, and `Buffer.allocUnsafe()`[#](https://nodejs.org/docs/latest/api/buffer.html#bufferfrom-bufferalloc-and-bufferallocunsafe)
In versions of Node.js prior to 6.0.0, `Buffer` instances were created using the `Buffer` constructor function, which allocates the returned `Buffer` differently based on what arguments are provided:
  * Passing a number as the first argument to `Buffer()` (e.g. `new Buffer(10)`) allocates a new `Buffer` object of the specified size. Prior to Node.js 8.0.0, the memory allocated for such `Buffer` instances is _not_ initialized and _can contain sensitive data_. Such `Buffer` instances _must_ be subsequently initialized by using either [`buf.fill(0)`](https://nodejs.org/docs/latest/api/buffer.html#buffillvalue-offset-end-encoding) or by writing to the entire `Buffer` before reading data from the `Buffer`. While this behavior is _intentional_ to improve performance, development experience has demonstrated that a more explicit distinction is required between creating a fast-but-uninitialized `Buffer` versus creating a slower-but-safer `Buffer`. Since Node.js 8.0.0, `Buffer(num)` and `new Buffer(num)` return a `Buffer` with initialized memory.
  * Passing a string, array, or `Buffer` as the first argument copies the passed object's data into the `Buffer`.
  * Passing an `Buffer` that shares allocated memory with the given array buffer.


Because the behavior of `new Buffer()` is different depending on the type of the first argument, security and reliability issues can be inadvertently introduced into applications when argument validation or `Buffer` initialization is not performed.
For example, if an attacker can cause an application to receive a number where a string is expected, the application may call `new Buffer(100)` instead of `new Buffer("100")`, leading it to allocate a 100 byte buffer instead of allocating a 3 byte buffer with content `"100"`. This is commonly possible using JSON API calls. Since JSON distinguishes between numeric and string types, it allows injection of numbers where a naively written application that does not validate its input sufficiently might expect to always receive a string. Before Node.js 8.0.0, the 100 byte buffer might contain arbitrary pre-existing in-memory data, so may be used to expose in-memory secrets to a remote attacker. Since Node.js 8.0.0, exposure of memory cannot occur because the data is zero-filled. However, other attacks are still possible, such as causing very large buffers to be allocated by the server, leading to performance degradation or crashing on memory exhaustion.
To make the creation of `Buffer` instances more reliable and less error-prone, the various forms of the `new Buffer()` constructor have been **deprecated** and replaced by separate `Buffer.from()`, [`Buffer.alloc()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocsize-fill-encoding), and [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) methods.
_Developers should migrate all existing uses of the`new Buffer()` constructors to one of these new APIs._
  * [`Buffer.from(array)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarray) returns a new `Buffer` that _contains a copy_ of the provided octets.
  * [`Buffer.from(arrayBuffer[, byteOffset[, length]])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarraybuffer-byteoffset-length) returns a new `Buffer` that _shares the same allocated memory_ as the given
  * [`Buffer.from(buffer)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfrombuffer) returns a new `Buffer` that _contains a copy_ of the contents of the given `Buffer`.
  * [`Buffer.from(string[, encoding])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromstring-encoding) returns a new `Buffer` that _contains a copy_ of the provided string.
  * [`Buffer.alloc(size[, fill[, encoding]])`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocsize-fill-encoding) returns a new initialized `Buffer` of the specified size. This method is slower than [`Buffer.allocUnsafe(size)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) but guarantees that newly created `Buffer` instances never contain old data that is potentially sensitive. A `TypeError` will be thrown if `size` is not a number.
  * [`Buffer.allocUnsafe(size)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) and [`Buffer.allocUnsafeSlow(size)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafeslowsize) each return a new uninitialized `Buffer` of the specified `size`. Because the `Buffer` is uninitialized, the allocated segment of memory might contain old data that is potentially sensitive.


`Buffer` instances returned by [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize), [`Buffer.from(string)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromstring-encoding), [`Buffer.concat()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferconcatlist-totallength) and [`Buffer.from(array)`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferfromarray) _may_ be allocated off a shared internal memory pool if `size` is less than or equal to half [`Buffer.poolSize`](https://nodejs.org/docs/latest/api/buffer.html#bufferpoolsize). Instances returned by [`Buffer.allocUnsafeSlow()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafeslowsize) _never_ use the shared internal memory pool.
#### The `--zero-fill-buffers` command-line option[#](https://nodejs.org/docs/latest/api/buffer.html#the-zero-fill-buffers-command-line-option)
Added in: v5.10.0
Node.js can be started using the `--zero-fill-buffers` command-line option to cause all newly-allocated `Buffer` instances to be zero-filled upon creation by default. Without the option, buffers created with [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) and [`Buffer.allocUnsafeSlow()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafeslowsize) are not zero-filled. Use of this flag can have a measurable negative impact on performance. Use the `--zero-fill-buffers` option only when necessary to enforce that newly allocated `Buffer` instances cannot contain old data that is potentially sensitive.
```
$ node --zero-fill-buffers
> Buffer.allocUnsafe(5);
<Buffer 00 00 00 00 00>
copy
```

#### What makes `Buffer.allocUnsafe()` and `Buffer.allocUnsafeSlow()` "unsafe"?[#](https://nodejs.org/docs/latest/api/buffer.html#what-makes-bufferallocunsafe-and-bufferallocunsafeslow-unsafe)
When calling [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) and [`Buffer.allocUnsafeSlow()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafeslowsize), the segment of allocated memory is _uninitialized_ (it is not zeroed-out). While this design makes the allocation of memory quite fast, the allocated segment of memory might contain old data that is potentially sensitive. Using a `Buffer` created by [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize) without _completely_ overwriting the memory can allow this old data to be leaked when the `Buffer` memory is read.
While there are clear performance advantages to using [`Buffer.allocUnsafe()`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferallocunsafesize), extra care _must_ be taken in order to avoid introducing security vulnerabilities into an application.
