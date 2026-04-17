
const compressedKey = ecdh.getPublicKey('hex', 'compressed');

const uncompressedKey = ECDH.convertKey(compressedKey,
                                        'secp256k1',
                                        'hex',
                                        'hex',
                                        'uncompressed');

// The converted key and the uncompressed public key should be the same
console.log(uncompressedKey === ecdh.getPublicKey('hex'));
const {
  createECDH,
  ECDH,
} = require('node:crypto');

const ecdh = createECDH('secp256k1');
ecdh.generateKeys();

const compressedKey = ecdh.getPublicKey('hex', 'compressed');

const uncompressedKey = ECDH.convertKey(compressedKey,
                                        'secp256k1',
                                        'hex',
                                        'hex',
                                        'uncompressed');

// The converted key and the uncompressed public key should be the same
console.log(uncompressedKey === ecdh.getPublicKey('hex'));
copy
```

####  `ecdh.computeSecret(otherPublicKey[, inputEncoding][, outputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#ecdhcomputesecretotherpublickey-inputencoding-outputencoding)
Added in: v0.11.14History Version | Changes
---|---
v10.0.0 | Changed error format to better support invalid public key error.
v6.0.0 | The default `inputEncoding` changed from `binary` to `utf8`.
  * `otherPublicKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `inputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `otherPublicKey` string.
  * `outputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Computes the shared secret using `otherPublicKey` as the other party's public key and returns the computed shared secret. The supplied key is interpreted using specified `inputEncoding`, and the returned secret is encoded using the specified `outputEncoding`. If the `inputEncoding` is not provided, `otherPublicKey` is expected to be a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`.
If `outputEncoding` is given a string will be returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
`ecdh.computeSecret` will throw an `ERR_CRYPTO_ECDH_INVALID_PUBLIC_KEY` error when `otherPublicKey` lies outside of the elliptic curve. Since `otherPublicKey` is usually supplied from a remote user over an insecure network, be sure to handle this exception accordingly.
####  `ecdh.generateKeys([encoding[, format]])`[#](https://nodejs.org/docs/latest/api/crypto.html#ecdhgeneratekeysencoding-format)
Added in: v0.11.14
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * `format` **Default:** `'uncompressed'`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Generates private and public EC Diffie-Hellman key values, and returns the public key in the specified `format` and `encoding`. This key should be transferred to the other party.
The `format` argument specifies point encoding and can be `'compressed'` or `'uncompressed'`. If `format` is not specified, the point will be returned in `'uncompressed'` format.
If `encoding` is provided a string is returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
####  `ecdh.getPrivateKey([encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#ecdhgetprivatekeyencoding)
Added in: v0.11.14
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `encoding`.


If `encoding` is specified, a string is returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
####  `ecdh.getPublicKey([encoding][, format])`[#](https://nodejs.org/docs/latest/api/crypto.html#ecdhgetpublickeyencoding-format)
Added in: v0.11.14
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * `format` **Default:** `'uncompressed'`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `encoding` and `format`.


The `format` argument specifies point encoding and can be `'compressed'` or `'uncompressed'`. If `format` is not specified the point will be returned in `'uncompressed'` format.
If `encoding` is specified, a string is returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
####  `ecdh.setPrivateKey(privateKey[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#ecdhsetprivatekeyprivatekey-encoding)
Added in: v0.11.14
  * `privateKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `privateKey` string.


Sets the EC Diffie-Hellman private key. If `encoding` is provided, `privateKey` is expected to be a string; otherwise `privateKey` is expected to be a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`.
If `privateKey` is not valid for the curve specified when the `ECDH` object was created, an error is thrown. Upon setting the private key, the associated public point (key) is also generated and set in the `ECDH` object.
####  `ecdh.setPublicKey(publicKey[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#ecdhsetpublickeypublickey-encoding)
Added in: v0.11.14Deprecated in: v5.2.0
Stability: 0 - Deprecated
  * `publicKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `publicKey` string.


Sets the EC Diffie-Hellman public key. If `encoding` is provided `publicKey` is expected to be a string; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView` is expected.
There is not normally a reason to call this method because `ECDH` only requires a private key and the other party's public key to compute the shared secret. Typically either [`ecdh.generateKeys()`](https://nodejs.org/docs/latest/api/crypto.html#ecdhgeneratekeysencoding-format) or [`ecdh.setPrivateKey()`](https://nodejs.org/docs/latest/api/crypto.html#ecdhsetprivatekeyprivatekey-encoding) will be called. The [`ecdh.setPrivateKey()`](https://nodejs.org/docs/latest/api/crypto.html#ecdhsetprivatekeyprivatekey-encoding) method attempts to generate the public point/key associated with the private key being set.
Example (obtaining a shared secret):
```
const {
  createECDH,
  createHash,
} = await import('node:crypto');

const alice = createECDH('secp256k1');
const bob = createECDH('secp256k1');

// This is a shortcut way of specifying one of Alice's previous private
// keys. It would be unwise to use such a predictable private key in a real
// application.
alice.setPrivateKey(
  createHash('sha256').update('alice', 'utf8').digest(),
);

// Bob uses a newly generated cryptographically strong
// pseudorandom key pair
bob.generateKeys();

const aliceSecret = alice.computeSecret(bob.getPublicKey(), null, 'hex');
const bobSecret = bob.computeSecret(alice.getPublicKey(), null, 'hex');

// aliceSecret and bobSecret should be the same shared secret value
console.log(aliceSecret === bobSecret);
const {
  createECDH,
  createHash,
} = require('node:crypto');

const alice = createECDH('secp256k1');
const bob = createECDH('secp256k1');

// This is a shortcut way of specifying one of Alice's previous private
// keys. It would be unwise to use such a predictable private key in a real
// application.
alice.setPrivateKey(
  createHash('sha256').update('alice', 'utf8').digest(),
);

// Bob uses a newly generated cryptographically strong
// pseudorandom key pair
bob.generateKeys();

const aliceSecret = alice.computeSecret(bob.getPublicKey(), null, 'hex');
const bobSecret = bob.computeSecret(alice.getPublicKey(), null, 'hex');

// aliceSecret and bobSecret should be the same shared secret value
console.log(aliceSecret === bobSecret);
copy
```

### Class: `Hash`[#](https://nodejs.org/docs/latest/api/crypto.html#class-hash)
Added in: v0.1.92
  * Extends: [`<stream.Transform>`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform)


The `Hash` class is a utility for creating hash digests of data. It can be used in one of two ways:
  * As a [stream](https://nodejs.org/docs/latest/api/stream.html) that is both readable and writable, where data is written to produce a computed hash digest on the readable side, or
  * Using the [`hash.update()`](https://nodejs.org/docs/latest/api/crypto.html#hashupdatedata-inputencoding) and [`hash.digest()`](https://nodejs.org/docs/latest/api/crypto.html#hashdigestencoding) methods to produce the computed hash.


The [`crypto.createHash()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatehashalgorithm-options) method is used to create `Hash` instances. `Hash` objects are not to be created directly using the `new` keyword.
Example: Using `Hash` objects as streams:
```
const {
  createHash,
} = await import('node:crypto');

const hash = createHash('sha256');

hash.on('readable', () => {
  // Only one element is going to be produced by the
  // hash stream.
  const data = hash.read();
  if (data) {
    console.log(data.toString('hex'));
    // Prints:
    //   6a2da20943931e9834fc12cfe5bb47bbd9ae43489a30726962b576f4e3993e50
  }
});

hash.write('some data to hash');
hash.end();
const {
  createHash,
} = require('node:crypto');

const hash = createHash('sha256');

hash.on('readable', () => {
  // Only one element is going to be produced by the
  // hash stream.
  const data = hash.read();
  if (data) {
    console.log(data.toString('hex'));
    // Prints:
    //   6a2da20943931e9834fc12cfe5bb47bbd9ae43489a30726962b576f4e3993e50
  }
});

hash.write('some data to hash');
hash.end();
copy
```

Example: Using `Hash` and piped streams:
```
import { createReadStream } from 'node:fs';
import { stdout } from 'node:process';
const { createHash } = await import('node:crypto');

const hash = createHash('sha256');

const input = createReadStream('test.js');
input.pipe(hash).setEncoding('hex').pipe(stdout);
const { createReadStream } = require('node:fs');
const { createHash } = require('node:crypto');
const { stdout } = require('node:process');

const hash = createHash('sha256');

const input = createReadStream('test.js');
input.pipe(hash).setEncoding('hex').pipe(stdout);
copy
```

Example: Using the [`hash.update()`](https://nodejs.org/docs/latest/api/crypto.html#hashupdatedata-inputencoding) and [`hash.digest()`](https://nodejs.org/docs/latest/api/crypto.html#hashdigestencoding) methods:
```
const {
  createHash,
} = await import('node:crypto');

const hash = createHash('sha256');

hash.update('some data to hash');
console.log(hash.digest('hex'));
// Prints:
//   6a2da20943931e9834fc12cfe5bb47bbd9ae43489a30726962b576f4e3993e50
const {
  createHash,
} = require('node:crypto');

const hash = createHash('sha256');

hash.update('some data to hash');
console.log(hash.digest('hex'));
// Prints:
//   6a2da20943931e9834fc12cfe5bb47bbd9ae43489a30726962b576f4e3993e50
copy
```

####  `hash.copy([options])`[#](https://nodejs.org/docs/latest/api/crypto.html#hashcopyoptions)
Added in: v13.1.0
  * `options` [`stream.transform` options](https://nodejs.org/docs/latest/api/stream.html#new-streamtransformoptions)
  * Returns: [`<Hash>`](https://nodejs.org/docs/latest/api/crypto.html#class-hash)


Creates a new `Hash` object that contains a deep copy of the internal state of the current `Hash` object.
The optional `options` argument controls stream behavior. For XOF hash functions such as `'shake256'`, the `outputLength` option can be used to specify the desired output length in bytes.
An error is thrown when an attempt is made to copy the `Hash` object after its [`hash.digest()`](https://nodejs.org/docs/latest/api/crypto.html#hashdigestencoding) method has been called.
```
// Calculate a rolling hash.
const {
  createHash,
} = await import('node:crypto');

const hash = createHash('sha256');

hash.update('one');
console.log(hash.copy().digest('hex'));

hash.update('two');
console.log(hash.copy().digest('hex'));

hash.update('three');
console.log(hash.copy().digest('hex'));

// Etc.
// Calculate a rolling hash.
const {
  createHash,
} = require('node:crypto');

const hash = createHash('sha256');

hash.update('one');
console.log(hash.copy().digest('hex'));

hash.update('two');
console.log(hash.copy().digest('hex'));

hash.update('three');
console.log(hash.copy().digest('hex'));

// Etc.
copy
```

####  `hash.digest([encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#hashdigestencoding)
Added in: v0.1.92
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Calculates the digest of all of the data passed to be hashed (using the [`hash.update()`](https://nodejs.org/docs/latest/api/crypto.html#hashupdatedata-inputencoding) method). If `encoding` is provided a string will be returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
The `Hash` object can not be used again after `hash.digest()` method has been called. Multiple calls will cause an error to be thrown.
####  `hash.update(data[, inputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#hashupdatedata-inputencoding)
Added in: v0.1.92History Version | Changes
---|---
v6.0.0 | The default `inputEncoding` changed from `binary` to `utf8`.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `inputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `data` string.


Updates the hash content with the given `data`, the encoding of which is given in `inputEncoding`. If `encoding` is not provided, and the `data` is a string, an encoding of `'utf8'` is enforced. If `data` is a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`, then `inputEncoding` is ignored.
This can be called many times with new data as it is streamed.
### Class: `Hmac`[#](https://nodejs.org/docs/latest/api/crypto.html#class-hmac)
Added in: v0.1.94
  * Extends: [`<stream.Transform>`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform)


The `Hmac` class is a utility for creating cryptographic HMAC digests. It can be used in one of two ways:
  * As a [stream](https://nodejs.org/docs/latest/api/stream.html) that is both readable and writable, where data is written to produce a computed HMAC digest on the readable side, or
  * Using the [`hmac.update()`](https://nodejs.org/docs/latest/api/crypto.html#hmacupdatedata-inputencoding) and [`hmac.digest()`](https://nodejs.org/docs/latest/api/crypto.html#hmacdigestencoding) methods to produce the computed HMAC digest.


The [`crypto.createHmac()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatehmacalgorithm-key-options) method is used to create `Hmac` instances. `Hmac` objects are not to be created directly using the `new` keyword.
Example: Using `Hmac` objects as streams:
```
const {
  createHmac,
} = await import('node:crypto');

const hmac = createHmac('sha256', 'a secret');

hmac.on('readable', () => {
  // Only one element is going to be produced by the
  // hash stream.
  const data = hmac.read();
  if (data) {
    console.log(data.toString('hex'));
    // Prints:
    //   7fd04df92f636fd450bc841c9418e5825c17f33ad9c87c518115a45971f7f77e
  }
});

hmac.write('some data to hash');
hmac.end();
const {
  createHmac,
} = require('node:crypto');

const hmac = createHmac('sha256', 'a secret');

hmac.on('readable', () => {
  // Only one element is going to be produced by the
  // hash stream.
  const data = hmac.read();
  if (data) {
    console.log(data.toString('hex'));
    // Prints:
    //   7fd04df92f636fd450bc841c9418e5825c17f33ad9c87c518115a45971f7f77e
  }
});

hmac.write('some data to hash');
hmac.end();
copy
```

Example: Using `Hmac` and piped streams:
```
import { createReadStream } from 'node:fs';
import { stdout } from 'node:process';
const {
  createHmac,
} = await import('node:crypto');

const hmac = createHmac('sha256', 'a secret');

const input = createReadStream('test.js');
input.pipe(hmac).pipe(stdout);
const {
  createReadStream,
} = require('node:fs');
const {
  createHmac,
} = require('node:crypto');
const { stdout } = require('node:process');

const hmac = createHmac('sha256', 'a secret');

const input = createReadStream('test.js');
input.pipe(hmac).pipe(stdout);
copy
```

Example: Using the [`hmac.update()`](https://nodejs.org/docs/latest/api/crypto.html#hmacupdatedata-inputencoding) and [`hmac.digest()`](https://nodejs.org/docs/latest/api/crypto.html#hmacdigestencoding) methods:
```
const {
  createHmac,
} = await import('node:crypto');

const hmac = createHmac('sha256', 'a secret');

hmac.update('some data to hash');
console.log(hmac.digest('hex'));
// Prints:
//   7fd04df92f636fd450bc841c9418e5825c17f33ad9c87c518115a45971f7f77e
const {
  createHmac,
} = require('node:crypto');

const hmac = createHmac('sha256', 'a secret');

hmac.update('some data to hash');
console.log(hmac.digest('hex'));
// Prints:
//   7fd04df92f636fd450bc841c9418e5825c17f33ad9c87c518115a45971f7f77e
copy
```

####  `hmac.digest([encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#hmacdigestencoding)
Added in: v0.1.94
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Calculates the HMAC digest of all of the data passed using [`hmac.update()`](https://nodejs.org/docs/latest/api/crypto.html#hmacupdatedata-inputencoding). If `encoding` is provided a string is returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned;
The `Hmac` object can not be used again after `hmac.digest()` has been called. Multiple calls to `hmac.digest()` will result in an error being thrown.
####  `hmac.update(data[, inputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#hmacupdatedata-inputencoding)
Added in: v0.1.94History Version | Changes
---|---
v6.0.0 | The default `inputEncoding` changed from `binary` to `utf8`.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `inputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `data` string.


Updates the `Hmac` content with the given `data`, the encoding of which is given in `inputEncoding`. If `encoding` is not provided, and the `data` is a string, an encoding of `'utf8'` is enforced. If `data` is a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`, then `inputEncoding` is ignored.
This can be called many times with new data as it is streamed.
### Class: `KeyObject`[#](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)
Added in: v11.6.0History Version | Changes
---|---
v24.6.0 | Add support for ML-DSA keys.
v14.5.0, v12.19.0 | Instances of this class can now be passed to worker threads using `postMessage`.
v11.13.0 | This class is now exported.
Node.js uses a `KeyObject` class to represent a symmetric or asymmetric key, and each kind of key exposes different functions. The [`crypto.createSecretKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatesecretkeykey-encoding), [`crypto.createPublicKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatepublickeykey) and [`crypto.createPrivateKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateprivatekeykey) methods are used to create `KeyObject` instances. `KeyObject` objects are not to be created directly using the `new` keyword.
Most applications should consider using the new `KeyObject` API instead of passing keys as strings or `Buffer`s due to improved security features.
`KeyObject` instances can be passed to other threads via [`postMessage()`](https://nodejs.org/docs/latest/api/worker_threads.html#portpostmessagevalue-transferlist). The receiver obtains a cloned `KeyObject`, and the `KeyObject` does not need to be listed in the `transferList` argument.
#### Static method: `KeyObject.from(key)`[#](https://nodejs.org/docs/latest/api/crypto.html#static-method-keyobjectfromkey)
Added in: v15.0.0
  * `key` [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)
  * Returns: [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)


Example: Converting a `CryptoKey` instance to a `KeyObject`:
```
const { KeyObject } = await import('node:crypto');
const { subtle } = globalThis.crypto;

const key = await subtle.generateKey({
  name: 'HMAC',
  hash: 'SHA-256',
  length: 256,
}, true, ['sign', 'verify']);

const keyObject = KeyObject.from(key);
console.log(keyObject.symmetricKeySize);
// Prints: 32 (symmetric key size in bytes)
const { KeyObject } = require('node:crypto');
const { subtle } = globalThis.crypto;

(async function() {
  const key = await subtle.generateKey({
    name: 'HMAC',
    hash: 'SHA-256',
    length: 256,
  }, true, ['sign', 'verify']);

  const keyObject = KeyObject.from(key);
  console.log(keyObject.symmetricKeySize);
  // Prints: 32 (symmetric key size in bytes)
})();
copy
```

####  `keyObject.asymmetricKeyDetails`[#](https://nodejs.org/docs/latest/api/crypto.html#keyobjectasymmetrickeydetails)
Added in: v15.7.0History Version | Changes
---|---
v16.9.0 | Expose `RSASSA-PSS-params` sequence parameters for RSA-PSS keys.
  * Type:
    * `modulusLength`
    * `publicExponent`
    * `hashAlgorithm`
    * `mgf1HashAlgorithm`
    * `saltLength`
    * `divisorLength` `q` in bits (DSA).
    * `namedCurve`


This property exists only on asymmetric keys. Depending on the type of the key, this object contains information about the key. None of the information obtained through this property can be used to uniquely identify a key or to compromise the security of the key.
For RSA-PSS keys, if the key material contains a `RSASSA-PSS-params` sequence, the `hashAlgorithm`, `mgf1HashAlgorithm`, and `saltLength` properties will be set.
Other key details might be exposed via this API using additional attributes.
####  `keyObject.asymmetricKeyType`[#](https://nodejs.org/docs/latest/api/crypto.html#keyobjectasymmetrickeytype)
Added in: v11.6.0History Version | Changes
---|---
v24.8.0 | Add support for SLH-DSA keys.
v24.7.0 | Add support for ML-KEM keys.
v24.6.0 | Add support for ML-DSA keys.
v13.9.0, v12.17.0 | Added support for `'dh'`.
v12.0.0 | Added support for `'rsa-pss'`.
v12.0.0 | This property now returns `undefined` for KeyObject instances of unrecognized type instead of aborting.
v12.0.0 | Added support for `'x25519'` and `'x448'`.
v12.0.0 | Added support for `'ed25519'` and `'ed448'`.
  * Type:


For asymmetric keys, this property represents the type of the key. See the supported [asymmetric key types](https://nodejs.org/docs/latest/api/crypto.html#asymmetric-key-types).
This property is `undefined` for unrecognized `KeyObject` types and symmetric keys.
####  `keyObject.equals(otherKeyObject)`[#](https://nodejs.org/docs/latest/api/crypto.html#keyobjectequalsotherkeyobject)
Added in: v17.7.0, v16.15.0
  * `otherKeyObject` [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) A `KeyObject` with which to compare `keyObject`.
  * Returns:


Returns `true` or `false` depending on whether the keys have exactly the same type, value, and parameters. This method is not
####  `keyObject.export([options])`[#](https://nodejs.org/docs/latest/api/crypto.html#keyobjectexportoptions)
Added in: v11.6.0History Version | Changes
---|---
v15.9.0 | Added support for `'jwk'` format.
  * `options`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


For symmetric keys, the following encoding options can be used:
  * `format` `'buffer'` (default) or `'jwk'`.


For public keys, the following encoding options can be used:
  * `type` `'pkcs1'` (RSA only) or `'spki'`.
  * `format` `'pem'`, `'der'`, or `'jwk'`.


For private keys, the following encoding options can be used:
  * `type` `'pkcs1'` (RSA only), `'pkcs8'` or `'sec1'` (EC only).
  * `format` `'pem'`, `'der'`, or `'jwk'`.
  * `cipher` `cipher` and `passphrase` using PKCS#5 v2.0 password based encryption.
  * `passphrase` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The passphrase to use for encryption, see `cipher`.


The result type depends on the selected encoding format, when PEM the result is a string, when DER it will be a buffer containing the data encoded as DER, when
When
PKCS#1, SEC1, and PKCS#8 type keys can be encrypted by using a combination of the `cipher` and `format` options. The PKCS#8 `type` can be used with any `format` to encrypt any key algorithm (RSA, EC, or DH) by specifying a `cipher`. PKCS#1 and SEC1 can only be encrypted by specifying a `cipher` when the PEM `format` is used. For maximum compatibility, use PKCS#8 for encrypted private keys. Since PKCS#8 defines its own encryption mechanism, PEM-level encryption is not supported when encrypting a PKCS#8 key. See
