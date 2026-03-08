The returned object mimics the interface of objects created by [`crypto.createDiffieHellman()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatediffiehellmanprime-primeencoding-generator-generatorencoding), but will not allow changing the keys (with [`diffieHellman.setPublicKey()`](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmansetpublickeypublickey-encoding), for example). The advantage of using this method is that the parties do not have to generate nor exchange a group modulus beforehand, saving both processor and communication time.
Example (obtaining a shared secret):
```
const {
  getDiffieHellman,
} = await import('node:crypto');
const alice = getDiffieHellman('modp14');
const bob = getDiffieHellman('modp14');

alice.generateKeys();
bob.generateKeys();

const aliceSecret = alice.computeSecret(bob.getPublicKey(), null, 'hex');
const bobSecret = bob.computeSecret(alice.getPublicKey(), null, 'hex');

/* aliceSecret and bobSecret should be the same */
console.log(aliceSecret === bobSecret);
const {
  getDiffieHellman,
} = require('node:crypto');

const alice = getDiffieHellman('modp14');
const bob = getDiffieHellman('modp14');

alice.generateKeys();
bob.generateKeys();

const aliceSecret = alice.computeSecret(bob.getPublicKey(), null, 'hex');
const bobSecret = bob.computeSecret(alice.getPublicKey(), null, 'hex');

/* aliceSecret and bobSecret should be the same */
console.log(aliceSecret === bobSecret);
copy
```

####  `crypto.getFips()`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogetfips)
Added in: v10.0.0
  * Returns: `1` if and only if a FIPS compliant crypto provider is currently in use, `0` otherwise. A future semver-major release may change the return type of this API to a


####  `crypto.getHashes()`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogethashes)
Added in: v0.9.3
  * Returns: `'RSA-SHA256'`. Hash algorithms are also called "digest" algorithms.

```
const {
  getHashes,
} = await import('node:crypto');

console.log(getHashes()); // ['DSA', 'DSA-SHA', 'DSA-SHA1', ...]
const {
  getHashes,
} = require('node:crypto');

console.log(getHashes()); // ['DSA', 'DSA-SHA', 'DSA-SHA1', ...]
copy
```

####  `crypto.getRandomValues(typedArray)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogetrandomvaluestypedarray)
Added in: v17.4.0
  * `typedArray` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `typedArray`.


A convenient alias for [`crypto.webcrypto.getRandomValues()`](https://nodejs.org/docs/latest/api/webcrypto.html#cryptogetrandomvaluestypedarray). This implementation is not compliant with the Web Crypto spec, to write web-compatible code use [`crypto.webcrypto.getRandomValues()`](https://nodejs.org/docs/latest/api/webcrypto.html#cryptogetrandomvaluestypedarray) instead.
####  `crypto.hash(algorithm, data[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptohashalgorithm-data-options)
Added in: v21.7.0, v20.12.0History Version | Changes
---|---
v25.4.0 | This API is no longer experimental.
v24.4.0 | The `outputLength` option was added for XOF hash functions.
  * `algorithm`
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `data` is a string, it will be encoded as UTF-8 before being hashed. If a different input encoding is desired for a string input, user could encode the string into a `TypedArray` using either `TextEncoder` or `Buffer.from()` and passing the encoded `TypedArray` into this API instead.
  * `options`
    * `outputEncoding` [Encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) used to encode the returned digest. **Default:** `'hex'`.
    * `outputLength`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


A utility for creating one-shot hash digests of data. It can be faster than the object-based `crypto.createHash()` when hashing a smaller amount of data (<= 5MB) that's readily available. If the data can be big or if it is streamed, it's still recommended to use `crypto.createHash()` instead.
The `algorithm` is dependent on the available algorithms supported by the version of OpenSSL on the platform. Examples are `'sha256'`, `'sha512'`, etc. On recent releases of OpenSSL, `openssl list -digest-algorithms` will display the available digest algorithms.
If `options` is a string, then it specifies the `outputEncoding`.
Example:
```
const crypto = require('node:crypto');
const { Buffer } = require('node:buffer');

// Hashing a string and return the result as a hex-encoded string.
const string = 'Node.js';
// 10b3493287f831e81a438811a1ffba01f8cec4b7
console.log(crypto.hash('sha1', string));

// Encode a base64-encoded string into a Buffer, hash it and return
// the result as a buffer.
const base64 = 'Tm9kZS5qcw==';
// <Buffer 10 b3 49 32 87 f8 31 e8 1a 43 88 11 a1 ff ba 01 f8 ce c4 b7>
console.log(crypto.hash('sha1', Buffer.from(base64, 'base64'), 'buffer'));
import crypto from 'node:crypto';
import { Buffer } from 'node:buffer';

// Hashing a string and return the result as a hex-encoded string.
const string = 'Node.js';
// 10b3493287f831e81a438811a1ffba01f8cec4b7
console.log(crypto.hash('sha1', string));

// Encode a base64-encoded string into a Buffer, hash it and return
// the result as a buffer.
const base64 = 'Tm9kZS5qcw==';
// <Buffer 10 b3 49 32 87 f8 31 e8 1a 43 88 11 a1 ff ba 01 f8 ce c4 b7>
console.log(crypto.hash('sha1', Buffer.from(base64, 'base64'), 'buffer'));
copy
```

####  `crypto.hkdf(digest, ikm, salt, info, keylen, callback)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptohkdfdigest-ikm-salt-info-keylen-callback)
Added in: v15.0.0History Version | Changes
---|---
v18.8.0, v16.18.0 | The input keying material can now be zero-length.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `digest`
  * `ikm` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) The input keying material. Must be provided but can be zero-length.
  * `salt` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `info` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `keylen` `255` times the number of bytes produced by the selected digest function (e.g. `sha512` generates 64-byte hashes, making the maximum HKDF output 16320 bytes).
  * `callback`
    * `err`
    * `derivedKey`


HKDF is a simple key derivation function defined in RFC 5869. The given `ikm`, `salt` and `info` are used with the `digest` to derive a key of `keylen` bytes.
The supplied `callback` function is called with two arguments: `err` and `derivedKey`. If an errors occurs while deriving the key, `err` will be set; otherwise `err` will be `null`. The successfully generated `derivedKey` will be passed to the callback as an
```
import { Buffer } from 'node:buffer';
const {
  hkdf,
} = await import('node:crypto');

hkdf('sha512', 'key', 'salt', 'info', 64, (err, derivedKey) => {
  if (err) throw err;
  console.log(Buffer.from(derivedKey).toString('hex'));  // '24156e2...5391653'
});
const {
  hkdf,
} = require('node:crypto');
const { Buffer } = require('node:buffer');

hkdf('sha512', 'key', 'salt', 'info', 64, (err, derivedKey) => {
  if (err) throw err;
  console.log(Buffer.from(derivedKey).toString('hex'));  // '24156e2...5391653'
});
copy
```

####  `crypto.hkdfSync(digest, ikm, salt, info, keylen)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptohkdfsyncdigest-ikm-salt-info-keylen)
Added in: v15.0.0History Version | Changes
---|---
v18.8.0, v16.18.0 | The input keying material can now be zero-length.
  * `digest`
  * `ikm` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) The input keying material. Must be provided but can be zero-length.
  * `salt` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `info` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `keylen` `255` times the number of bytes produced by the selected digest function (e.g. `sha512` generates 64-byte hashes, making the maximum HKDF output 16320 bytes).
  * Returns:


Provides a synchronous HKDF key derivation function as defined in RFC 5869. The given `ikm`, `salt` and `info` are used with the `digest` to derive a key of `keylen` bytes.
The successfully generated `derivedKey` will be returned as an
An error will be thrown if any of the input arguments specify invalid values or types, or if the derived key cannot be generated.
```
import { Buffer } from 'node:buffer';
const {
  hkdfSync,
} = await import('node:crypto');

const derivedKey = hkdfSync('sha512', 'key', 'salt', 'info', 64);
console.log(Buffer.from(derivedKey).toString('hex'));  // '24156e2...5391653'
const {
  hkdfSync,
} = require('node:crypto');
const { Buffer } = require('node:buffer');

const derivedKey = hkdfSync('sha512', 'key', 'salt', 'info', 64);
console.log(Buffer.from(derivedKey).toString('hex'));  // '24156e2...5391653'
copy
```

####  `crypto.pbkdf2(password, salt, iterations, keylen, digest, callback)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptopbkdf2password-salt-iterations-keylen-digest-callback)
Added in: v0.5.5History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v15.0.0 | The password and salt arguments can also be ArrayBuffer instances.
v14.0.0 | The `iterations` parameter is now restricted to positive values. Earlier releases treated other values as one.
v8.0.0 | The `digest` parameter is always required now.
v6.0.0 | Calling this function without passing the `digest` parameter is deprecated now and will emit a warning.
v6.0.0 | The default encoding for `password` if it is a string changed from `binary` to `utf8`.
  * `password` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `salt` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `iterations`
  * `keylen`
  * `digest`
  * `callback`
    * `err`
    * `derivedKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Provides an asynchronous Password-Based Key Derivation Function 2 (PBKDF2) implementation. A selected HMAC digest algorithm specified by `digest` is applied to derive a key of the requested byte length (`keylen`) from the `password`, `salt` and `iterations`.
The supplied `callback` function is called with two arguments: `err` and `derivedKey`. If an error occurs while deriving the key, `err` will be set; otherwise `err` will be `null`. By default, the successfully generated `derivedKey` will be passed to the callback as a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html). An error will be thrown if any of the input arguments specify invalid values or types.
The `iterations` argument must be a number set as high as possible. The higher the number of iterations, the more secure the derived key will be, but will take a longer amount of time to complete.
The `salt` should be as unique as possible. It is recommended that a salt is random and at least 16 bytes long. See
When passing strings for `password` or `salt`, please consider [caveats when using strings as inputs to cryptographic APIs](https://nodejs.org/docs/latest/api/crypto.html#using-strings-as-inputs-to-cryptographic-apis).
```
const {
  pbkdf2,
} = await import('node:crypto');

pbkdf2('secret', 'salt', 100000, 64, 'sha512', (err, derivedKey) => {
  if (err) throw err;
  console.log(derivedKey.toString('hex'));  // '3745e48...08d59ae'
});
const {
  pbkdf2,
} = require('node:crypto');

pbkdf2('secret', 'salt', 100000, 64, 'sha512', (err, derivedKey) => {
  if (err) throw err;
  console.log(derivedKey.toString('hex'));  // '3745e48...08d59ae'
});
copy
```

An array of supported digest functions can be retrieved using [`crypto.getHashes()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogethashes).
This API uses libuv's threadpool, which can have surprising and negative performance implications for some applications; see the [`UV_THREADPOOL_SIZE`](https://nodejs.org/docs/latest/api/cli.html#uv_threadpool_sizesize) documentation for more information.
####  `crypto.pbkdf2Sync(password, salt, iterations, keylen, digest)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptopbkdf2syncpassword-salt-iterations-keylen-digest)
Added in: v0.9.3History Version | Changes
---|---
v14.0.0 | The `iterations` parameter is now restricted to positive values. Earlier releases treated other values as one.
v6.0.0 | Calling this function without passing the `digest` parameter is deprecated now and will emit a warning.
v6.0.0 | The default encoding for `password` if it is a string changed from `binary` to `utf8`.
  * `password` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `salt` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `iterations`
  * `keylen`
  * `digest`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Provides a synchronous Password-Based Key Derivation Function 2 (PBKDF2) implementation. A selected HMAC digest algorithm specified by `digest` is applied to derive a key of the requested byte length (`keylen`) from the `password`, `salt` and `iterations`.
If an error occurs an `Error` will be thrown, otherwise the derived key will be returned as a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html).
The `iterations` argument must be a number set as high as possible. The higher the number of iterations, the more secure the derived key will be, but will take a longer amount of time to complete.
The `salt` should be as unique as possible. It is recommended that a salt is random and at least 16 bytes long. See
When passing strings for `password` or `salt`, please consider [caveats when using strings as inputs to cryptographic APIs](https://nodejs.org/docs/latest/api/crypto.html#using-strings-as-inputs-to-cryptographic-apis).
```
const {
  pbkdf2Sync,
} = await import('node:crypto');

const key = pbkdf2Sync('secret', 'salt', 100000, 64, 'sha512');
console.log(key.toString('hex'));  // '3745e48...08d59ae'
const {
  pbkdf2Sync,
} = require('node:crypto');

const key = pbkdf2Sync('secret', 'salt', 100000, 64, 'sha512');
console.log(key.toString('hex'));  // '3745e48...08d59ae'
copy
```

An array of supported digest functions can be retrieved using [`crypto.getHashes()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogethashes).
####  `crypto.privateDecrypt(privateKey, buffer)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptoprivatedecryptprivatekey-buffer)
Added in: v0.11.14History Version | Changes
---|---
v21.6.2, v20.11.1, v18.19.1 | The `RSA_PKCS1_PADDING` padding was disabled unless the OpenSSL build supports implicit rejection.
v15.0.0 | Added string, ArrayBuffer, and CryptoKey as allowable key types. The oaepLabel can be an ArrayBuffer. The buffer can be a string or ArrayBuffer. All types that accept buffers are limited to a maximum of 2 ** 31 - 1 bytes.
v12.11.0 | The `oaepLabel` option was added.
v12.9.0 | The `oaepHash` option was added.
v11.6.0 | This function now supports key objects.
  * `privateKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)
    * `oaepHash` **Default:** `'sha1'`
    * `oaepLabel` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `padding` [`<crypto.constants>`](https://nodejs.org/docs/latest/api/crypto.html#cryptoconstants) An optional padding value defined in `crypto.constants`, which may be: `crypto.constants.RSA_NO_PADDING`, `crypto.constants.RSA_PKCS1_PADDING`, or `crypto.constants.RSA_PKCS1_OAEP_PADDING`.
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A new `Buffer` with the decrypted content.


Decrypts `buffer` with `privateKey`. `buffer` was previously encrypted using the corresponding public key, for example using [`crypto.publicEncrypt()`](https://nodejs.org/docs/latest/api/crypto.html#cryptopublicencryptkey-buffer).
If `privateKey` is not a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject), this function behaves as if `privateKey` had been passed to [`crypto.createPrivateKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateprivatekeykey). If it is an object, the `padding` property can be passed. Otherwise, this function uses `RSA_PKCS1_OAEP_PADDING`.
Using `crypto.constants.RSA_PKCS1_PADDING` in [`crypto.privateDecrypt()`](https://nodejs.org/docs/latest/api/crypto.html#cryptoprivatedecryptprivatekey-buffer) requires OpenSSL to support implicit rejection (`rsa_pkcs1_implicit_rejection`). If the version of OpenSSL used by Node.js does not support this feature, attempting to use `RSA_PKCS1_PADDING` will fail.
####  `crypto.privateEncrypt(privateKey, buffer)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptoprivateencryptprivatekey-buffer)
Added in: v1.1.0History Version | Changes
---|---
v15.0.0 | Added string, ArrayBuffer, and CryptoKey as allowable key types. The passphrase can be an ArrayBuffer. The buffer can be a string or ArrayBuffer. All types that accept buffers are limited to a maximum of 2 ** 31 - 1 bytes.
v11.6.0 | This function now supports key objects.
  * `privateKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)
    * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey) A PEM encoded private key.
    * `passphrase` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `padding` [`<crypto.constants>`](https://nodejs.org/docs/latest/api/crypto.html#cryptoconstants) An optional padding value defined in `crypto.constants`, which may be: `crypto.constants.RSA_NO_PADDING` or `crypto.constants.RSA_PKCS1_PADDING`.
    * `encoding` `buffer`, `key`, or `passphrase` are strings.
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A new `Buffer` with the encrypted content.


Encrypts `buffer` with `privateKey`. The returned data can be decrypted using the corresponding public key, for example using [`crypto.publicDecrypt()`](https://nodejs.org/docs/latest/api/crypto.html#cryptopublicdecryptkey-buffer).
If `privateKey` is not a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject), this function behaves as if `privateKey` had been passed to [`crypto.createPrivateKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateprivatekeykey). If it is an object, the `padding` property can be passed. Otherwise, this function uses `RSA_PKCS1_PADDING`.
####  `crypto.publicDecrypt(key, buffer)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptopublicdecryptkey-buffer)
Added in: v1.1.0History Version | Changes
---|---
v15.0.0 | Added string, ArrayBuffer, and CryptoKey as allowable key types. The passphrase can be an ArrayBuffer. The buffer can be a string or ArrayBuffer. All types that accept buffers are limited to a maximum of 2 ** 31 - 1 bytes.
v11.6.0 | This function now supports key objects.
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)
    * `passphrase` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `padding` [`<crypto.constants>`](https://nodejs.org/docs/latest/api/crypto.html#cryptoconstants) An optional padding value defined in `crypto.constants`, which may be: `crypto.constants.RSA_NO_PADDING` or `crypto.constants.RSA_PKCS1_PADDING`.
    * `encoding` `buffer`, `key`, or `passphrase` are strings.
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A new `Buffer` with the decrypted content.


Decrypts `buffer` with `key`.`buffer` was previously encrypted using the corresponding private key, for example using [`crypto.privateEncrypt()`](https://nodejs.org/docs/latest/api/crypto.html#cryptoprivateencryptprivatekey-buffer).
If `key` is not a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject), this function behaves as if `key` had been passed to [`crypto.createPublicKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatepublickeykey). If it is an object, the `padding` property can be passed. Otherwise, this function uses `RSA_PKCS1_PADDING`.
Because RSA public keys can be derived from private keys, a private key may be passed instead of a public key.
####  `crypto.publicEncrypt(key, buffer)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptopublicencryptkey-buffer)
Added in: v0.11.14History Version | Changes
---|---
v15.0.0 | Added string, ArrayBuffer, and CryptoKey as allowable key types. The oaepLabel and passphrase can be ArrayBuffers. The buffer can be a string or ArrayBuffer. All types that accept buffers are limited to a maximum of 2 ** 31 - 1 bytes.
v12.11.0 | The `oaepLabel` option was added.
v12.9.0 | The `oaepHash` option was added.
v11.6.0 | This function now supports key objects.
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)
    * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey) A PEM encoded public or private key, [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject), or [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey).
    * `oaepHash` **Default:** `'sha1'`
    * `oaepLabel` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `passphrase` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `padding` [`<crypto.constants>`](https://nodejs.org/docs/latest/api/crypto.html#cryptoconstants) An optional padding value defined in `crypto.constants`, which may be: `crypto.constants.RSA_NO_PADDING`, `crypto.constants.RSA_PKCS1_PADDING`, or `crypto.constants.RSA_PKCS1_OAEP_PADDING`.
    * `encoding` `buffer`, `key`, `oaepLabel`, or `passphrase` are strings.
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A new `Buffer` with the encrypted content.


Encrypts the content of `buffer` with `key` and returns a new [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) with encrypted content. The returned data can be decrypted using the corresponding private key, for example using [`crypto.privateDecrypt()`](https://nodejs.org/docs/latest/api/crypto.html#cryptoprivatedecryptprivatekey-buffer).
If `key` is not a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject), this function behaves as if `key` had been passed to [`crypto.createPublicKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatepublickeykey). If it is an object, the `padding` property can be passed. Otherwise, this function uses `RSA_PKCS1_OAEP_PADDING`.
Because RSA public keys can be derived from private keys, a private key may be passed instead of a public key.
####  `crypto.randomBytes(size[, callback])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptorandombytessize-callback)
Added in: v0.5.8History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v9.0.0 | Passing `null` as the `callback` argument now throws `ERR_INVALID_CALLBACK`.
  * `size` `size` must not be larger than `2**31 - 1`.
  * `callback`
    * `err`
    * `buf` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) if the `callback` function is not provided.


Generates cryptographically strong pseudorandom data. The `size` argument is a number indicating the number of bytes to generate.
