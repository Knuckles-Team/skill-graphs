Added in: v24.9.0
  * Type:


The OID of the algorithm used to sign the certificate.
####  `x509.verify(publicKey)`[#](https://nodejs.org/docs/latest/api/crypto.html#x509verifypublickey)
Added in: v15.6.0
  * `publicKey` [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) A public key.
  * Returns:


Verifies that this certificate was signed by the given public key. Does not perform any other validation checks on the certificate.
###  `node:crypto` module methods and properties[#](https://nodejs.org/docs/latest/api/crypto.html#nodecrypto-module-methods-and-properties)
####  `crypto.argon2(algorithm, parameters, callback)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptoargon2algorithm-parameters-callback)
Added in: v24.7.0
Stability: 1.2 - Release candidate
  * `algorithm` `"argon2d"`, `"argon2i"` or `"argon2id"`.
  * `parameters`
    * `message` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `nonce` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `parallelism` `2**24-1`.
    * `tagLength` `2**32-1`.
    * `memory` `8 * parallelism` and less than `2**32-1`. The actual number of blocks is rounded down to the nearest multiple of `4 * parallelism`.
    * `passes` `2**32-1`.
    * `secret` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | **NOT** be stored with the derived key. This is known as pepper in password hashing applications. If used, must have a length not greater than `2**32-1` bytes.
    * `associatedData` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `2**32-1` bytes.
  * `callback`
    * `err`
    * `derivedKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Provides an asynchronous
The `nonce` should be as unique as possible. It is recommended that a nonce is random and at least 16 bytes long. See
When passing strings for `message`, `nonce`, `secret` or `associatedData`, please consider [caveats when using strings as inputs to cryptographic APIs](https://nodejs.org/docs/latest/api/crypto.html#using-strings-as-inputs-to-cryptographic-apis).
The `callback` function is called with two arguments: `err` and `derivedKey`. `err` is an exception object when key derivation fails, otherwise `err` is `null`. `derivedKey` is passed to the callback as a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html).
An exception is thrown when any of the input arguments specify invalid values or types.
```
const { argon2, randomBytes } = await import('node:crypto');

const parameters = {
  message: 'password',
  nonce: randomBytes(16),
  parallelism: 4,
  tagLength: 64,
  memory: 65536,
  passes: 3,
};

argon2('argon2id', parameters, (err, derivedKey) => {
  if (err) throw err;
  console.log(derivedKey.toString('hex'));  // 'af91dad...9520f15'
});
const { argon2, randomBytes } = require('node:crypto');

const parameters = {
  message: 'password',
  nonce: randomBytes(16),
  parallelism: 4,
  tagLength: 64,
  memory: 65536,
  passes: 3,
};

argon2('argon2id', parameters, (err, derivedKey) => {
  if (err) throw err;
  console.log(derivedKey.toString('hex'));  // 'af91dad...9520f15'
});
copy
```

####  `crypto.argon2Sync(algorithm, parameters)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptoargon2syncalgorithm-parameters)
Added in: v24.7.0
Stability: 1.2 - Release candidate
  * `algorithm` `"argon2d"`, `"argon2i"` or `"argon2id"`.
  * `parameters`
    * `message` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `nonce` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `parallelism` `2**24-1`.
    * `tagLength` `2**32-1`.
    * `memory` `8 * parallelism` and less than `2**32-1`. The actual number of blocks is rounded down to the nearest multiple of `4 * parallelism`.
    * `passes` `2**32-1`.
    * `secret` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | **NOT** be stored with the derived key. This is known as pepper in password hashing applications. If used, must have a length not greater than `2**32-1` bytes.
    * `associatedData` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `2**32-1` bytes.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Provides a synchronous
The `nonce` should be as unique as possible. It is recommended that a nonce is random and at least 16 bytes long. See
When passing strings for `message`, `nonce`, `secret` or `associatedData`, please consider [caveats when using strings as inputs to cryptographic APIs](https://nodejs.org/docs/latest/api/crypto.html#using-strings-as-inputs-to-cryptographic-apis).
An exception is thrown when key derivation fails, otherwise the derived key is returned as a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html).
An exception is thrown when any of the input arguments specify invalid values or types.
```
const { argon2Sync, randomBytes } = await import('node:crypto');

const parameters = {
  message: 'password',
  nonce: randomBytes(16),
  parallelism: 4,
  tagLength: 64,
  memory: 65536,
  passes: 3,
};

const derivedKey = argon2Sync('argon2id', parameters);
console.log(derivedKey.toString('hex'));  // 'af91dad...9520f15'
const { argon2Sync, randomBytes } = require('node:crypto');

const parameters = {
  message: 'password',
  nonce: randomBytes(16),
  parallelism: 4,
  tagLength: 64,
  memory: 65536,
  passes: 3,
};

const derivedKey = argon2Sync('argon2id', parameters);
console.log(derivedKey.toString('hex'));  // 'af91dad...9520f15'
copy
```

####  `crypto.checkPrime(candidate[, options], callback)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocheckprimecandidate-options-callback)
Added in: v15.8.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `candidate` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options`
    * `checks` `0` (zero), a number of checks is used that yields a false positive rate of at most 2-64 for random input. Care must be used when selecting a number of checks. Refer to the OpenSSL documentation for the `nchecks` options for more details. **Default:** `0`
  * `callback`
    * `err`
    * `result` `true` if the candidate is a prime with an error probability less than `0.25 ** options.checks`.


Checks the primality of the `candidate`.
####  `crypto.checkPrimeSync(candidate[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocheckprimesynccandidate-options)
Added in: v15.8.0
  * `candidate` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options`
    * `checks` `0` (zero), a number of checks is used that yields a false positive rate of at most 2-64 for random input. Care must be used when selecting a number of checks. Refer to the OpenSSL documentation for the `nchecks` options for more details. **Default:** `0`
  * Returns: `true` if the candidate is a prime with an error probability less than `0.25 ** options.checks`.


Checks the primality of the `candidate`.
####  `crypto.constants`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptoconstants)
Added in: v6.3.0
  * Type:


An object containing commonly used constants for crypto and security related operations. The specific constants currently defined are described in [Crypto constants](https://nodejs.org/docs/latest/api/crypto.html#crypto-constants).
####  `crypto.createCipheriv(algorithm, key, iv[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatecipherivalgorithm-key-iv-options)
Added in: v0.1.94History Version | Changes
---|---
v17.9.0, v16.17.0 | The `authTagLength` option is now optional when using the `chacha20-poly1305` cipher and defaults to 16 bytes.
v15.0.0 | The password and iv arguments can be an ArrayBuffer and are each limited to a maximum of 2 ** 31 - 1 bytes.
v11.6.0 | The `key` argument can now be a `KeyObject`.
v11.2.0, v10.17.0 | The cipher `chacha20-poly1305` (the IETF variant of ChaCha20-Poly1305) is now supported.
v10.10.0 | Ciphers in OCB mode are now supported.
v10.2.0 | The `authTagLength` option can now be used to produce shorter authentication tags in GCM mode and defaults to 16 bytes.
v9.9.0 | The `iv` parameter may now be `null` for ciphers which do not need an initialization vector.
  * `algorithm`
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)
  * `iv` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options` [`stream.transform` options](https://nodejs.org/docs/latest/api/stream.html#new-streamtransformoptions)
  * Returns: [`<Cipheriv>`](https://nodejs.org/docs/latest/api/crypto.html#class-cipheriv)


Creates and returns a `Cipheriv` object, with the given `algorithm`, `key` and initialization vector (`iv`).
The `options` argument controls stream behavior and is optional except when a cipher in CCM or OCB mode (e.g. `'aes-128-ccm'`) is used. In that case, the `authTagLength` option is required and specifies the length of the authentication tag in bytes, see [CCM mode](https://nodejs.org/docs/latest/api/crypto.html#ccm-mode). In GCM mode, the `authTagLength` option is not required but can be used to set the length of the authentication tag that will be returned by `getAuthTag()` and defaults to 16 bytes. For `chacha20-poly1305`, the `authTagLength` option defaults to 16 bytes.
The `algorithm` is dependent on OpenSSL, examples are `'aes192'`, etc. On recent OpenSSL releases, `openssl list -cipher-algorithms` will display the available cipher algorithms.
The `key` is the raw key used by the `algorithm` and `iv` is an `'utf8'` encoded strings, [Buffers](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`s. The `key` may optionally be a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) of type `secret`. If the cipher does not need an initialization vector, `iv` may be `null`.
When passing strings for `key` or `iv`, please consider [caveats when using strings as inputs to cryptographic APIs](https://nodejs.org/docs/latest/api/crypto.html#using-strings-as-inputs-to-cryptographic-apis).
Initialization vectors should be unpredictable and unique; ideally, they will be cryptographically random. They do not have to be secret: IVs are typically just added to ciphertext messages unencrypted. It may sound contradictory that something has to be unpredictable and unique, but does not have to be secret; remember that an attacker must not be able to predict ahead of time what a given IV will be.
####  `crypto.createDecipheriv(algorithm, key, iv[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatedecipherivalgorithm-key-iv-options)
Added in: v0.1.94History Version | Changes
---|---
v17.9.0, v16.17.0 | The `authTagLength` option is now optional when using the `chacha20-poly1305` cipher and defaults to 16 bytes.
v11.6.0 | The `key` argument can now be a `KeyObject`.
v11.2.0, v10.17.0 | The cipher `chacha20-poly1305` (the IETF variant of ChaCha20-Poly1305) is now supported.
v10.10.0 | Ciphers in OCB mode are now supported.
v10.2.0 | The `authTagLength` option can now be used to restrict accepted GCM authentication tag lengths.
v9.9.0 | The `iv` parameter may now be `null` for ciphers which do not need an initialization vector.
  * `algorithm`
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)
  * `iv` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options` [`stream.transform` options](https://nodejs.org/docs/latest/api/stream.html#new-streamtransformoptions)
  * Returns: [`<Decipheriv>`](https://nodejs.org/docs/latest/api/crypto.html#class-decipheriv)


Creates and returns a `Decipheriv` object that uses the given `algorithm`, `key` and initialization vector (`iv`).
The `options` argument controls stream behavior and is optional except when a cipher in CCM or OCB mode (e.g. `'aes-128-ccm'`) is used. In that case, the `authTagLength` option is required and specifies the length of the authentication tag in bytes, see [CCM mode](https://nodejs.org/docs/latest/api/crypto.html#ccm-mode). For `chacha20-poly1305`, the `authTagLength` option defaults to 16 bytes and must be set to a different value if a different length is used. For AES-GCM, the `authTagLength` option has no default value when decrypting, and `setAuthTag()` will accept arbitrarily short authentication tags. This behavior is deprecated and subject to change (see [DEP0182](https://nodejs.org/docs/latest/api/deprecations.html#dep0182-short-gcm-authentication-tags-without-explicit-authtaglength)). **In the meantime, applications should either set the`authTagLength` option or check the actual authentication tag length before passing it to `setAuthTag()`.**
The `algorithm` is dependent on OpenSSL, examples are `'aes192'`, etc. On recent OpenSSL releases, `openssl list -cipher-algorithms` will display the available cipher algorithms.
The `key` is the raw key used by the `algorithm` and `iv` is an `'utf8'` encoded strings, [Buffers](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`s. The `key` may optionally be a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) of type `secret`. If the cipher does not need an initialization vector, `iv` may be `null`.
When passing strings for `key` or `iv`, please consider [caveats when using strings as inputs to cryptographic APIs](https://nodejs.org/docs/latest/api/crypto.html#using-strings-as-inputs-to-cryptographic-apis).
Initialization vectors should be unpredictable and unique; ideally, they will be cryptographically random. They do not have to be secret: IVs are typically just added to ciphertext messages unencrypted. It may sound contradictory that something has to be unpredictable and unique, but does not have to be secret; remember that an attacker must not be able to predict ahead of time what a given IV will be.
####  `crypto.createDiffieHellman(prime[, primeEncoding][, generator][, generatorEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatediffiehellmanprime-primeencoding-generator-generatorencoding)
Added in: v0.11.12History Version | Changes
---|---
v8.0.0 | The `prime` argument can be any `TypedArray` or `DataView` now.
v8.0.0 | The `prime` argument can be a `Uint8Array` now.
v6.0.0 | The default for the encoding parameters changed from `binary` to `utf8`.
  * `prime` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `primeEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `prime` string.
  * `generator` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | **Default:** `2`
  * `generatorEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `generator` string.
  * Returns: [`<DiffieHellman>`](https://nodejs.org/docs/latest/api/crypto.html#class-diffiehellman)


Creates a `DiffieHellman` key exchange object using the supplied `prime` and an optional specific `generator`.
The `generator` argument can be a number, string, or [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html). If `generator` is not specified, the value `2` is used.
If `primeEncoding` is specified, `prime` is expected to be a string; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView` is expected.
If `generatorEncoding` is specified, `generator` is expected to be a string; otherwise a number, [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView` is expected.
####  `crypto.createDiffieHellman(primeLength[, generator])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatediffiehellmanprimelength-generator)
Added in: v0.5.0
  * `primeLength`
  * `generator` **Default:** `2`
  * Returns: [`<DiffieHellman>`](https://nodejs.org/docs/latest/api/crypto.html#class-diffiehellman)


Creates a `DiffieHellman` key exchange object and generates a prime of `primeLength` bits using an optional specific numeric `generator`. If `generator` is not specified, the value `2` is used.
####  `crypto.createDiffieHellmanGroup(name)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatediffiehellmangroupname)
Added in: v0.9.3
  * `name`
  * Returns: [`<DiffieHellmanGroup>`](https://nodejs.org/docs/latest/api/crypto.html#class-diffiehellmangroup)


An alias for [`crypto.getDiffieHellman()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogetdiffiehellmangroupname)
####  `crypto.createECDH(curveName)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateecdhcurvename)
Added in: v0.11.14
  * `curveName`
  * Returns: [`<ECDH>`](https://nodejs.org/docs/latest/api/crypto.html#class-ecdh)


Creates an Elliptic Curve Diffie-Hellman (`ECDH`) key exchange object using a predefined curve specified by the `curveName` string. Use [`crypto.getCurves()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogetcurves) to obtain a list of available curve names. On recent OpenSSL releases, `openssl ecparam -list_curves` will also display the name and description of each available elliptic curve.
####  `crypto.createHash(algorithm[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatehashalgorithm-options)
Added in: v0.1.92History Version | Changes
---|---
v12.8.0 | The `outputLength` option was added for XOF hash functions.
  * `algorithm`
  * `options` [`stream.transform` options](https://nodejs.org/docs/latest/api/stream.html#new-streamtransformoptions)
  * Returns: [`<Hash>`](https://nodejs.org/docs/latest/api/crypto.html#class-hash)


Creates and returns a `Hash` object that can be used to generate hash digests using the given `algorithm`. Optional `options` argument controls stream behavior. For XOF hash functions such as `'shake256'`, the `outputLength` option can be used to specify the desired output length in bytes.
The `algorithm` is dependent on the available algorithms supported by the version of OpenSSL on the platform. Examples are `'sha256'`, `'sha512'`, etc. On recent releases of OpenSSL, `openssl list -digest-algorithms` will display the available digest algorithms.
Example: generating the sha256 sum of a file
```
import {
  createReadStream,
} from 'node:fs';
import { argv } from 'node:process';
const {
  createHash,
} = await import('node:crypto');

const filename = argv[2];

const hash = createHash('sha256');

const input = createReadStream(filename);
input.on('readable', () => {
  // Only one element is going to be produced by the
  // hash stream.
  const data = input.read();
  if (data)
    hash.update(data);
  else {
    console.log(`${hash.digest('hex')} ${filename}`);
  }
});
const {
  createReadStream,
} = require('node:fs');
const {
  createHash,
} = require('node:crypto');
const { argv } = require('node:process');

const filename = argv[2];

const hash = createHash('sha256');

const input = createReadStream(filename);
input.on('readable', () => {
  // Only one element is going to be produced by the
  // hash stream.
  const data = input.read();
  if (data)
    hash.update(data);
  else {
    console.log(`${hash.digest('hex')} ${filename}`);
  }
});
copy
```

####  `crypto.createHmac(algorithm, key[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatehmacalgorithm-key-options)
Added in: v0.1.94History Version | Changes
---|---
v15.0.0 | The key can also be an ArrayBuffer or CryptoKey. The encoding option was added. The key cannot contain more than 2 ** 32 - 1 bytes.
v11.6.0 | The `key` argument can now be a `KeyObject`.
  * `algorithm`
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)
  * `options` [`stream.transform` options](https://nodejs.org/docs/latest/api/stream.html#new-streamtransformoptions)
    * `encoding` `key` is a string.
  * Returns: [`<Hmac>`](https://nodejs.org/docs/latest/api/crypto.html#class-hmac)


Creates and returns an `Hmac` object that uses the given `algorithm` and `key`. Optional `options` argument controls stream behavior.
The `algorithm` is dependent on the available algorithms supported by the version of OpenSSL on the platform. Examples are `'sha256'`, `'sha512'`, etc. On recent releases of OpenSSL, `openssl list -digest-algorithms` will display the available digest algorithms.
The `key` is the HMAC key used to generate the cryptographic HMAC hash. If it is a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject), its type must be `secret`. If it is a string, please consider [caveats when using strings as inputs to cryptographic APIs](https://nodejs.org/docs/latest/api/crypto.html#using-strings-as-inputs-to-cryptographic-apis). If it was obtained from a cryptographically secure source of entropy, such as [`crypto.randomBytes()`](https://nodejs.org/docs/latest/api/crypto.html#cryptorandombytessize-callback) or [`crypto.generateKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogeneratekeytype-options-callback), its length should not exceed the block size of `algorithm` (e.g., 512 bits for SHA-256).
Example: generating the sha256 HMAC of a file
```
import {
  createReadStream,
} from 'node:fs';
import { argv } from 'node:process';
const {
  createHmac,
} = await import('node:crypto');

const filename = argv[2];

const hmac = createHmac('sha256', 'a secret');

const input = createReadStream(filename);
input.on('readable', () => {
  // Only one element is going to be produced by the
  // hash stream.
  const data = input.read();
  if (data)
    hmac.update(data);
  else {
    console.log(`${hmac.digest('hex')} ${filename}`);
  }
});
const {
  createReadStream,
} = require('node:fs');
const {
  createHmac,
} = require('node:crypto');
const { argv } = require('node:process');

const filename = argv[2];

const hmac = createHmac('sha256', 'a secret');

const input = createReadStream(filename);
input.on('readable', () => {
  // Only one element is going to be produced by the
  // hash stream.
  const data = input.read();
  if (data)
    hmac.update(data);
  else {
    console.log(`${hmac.digest('hex')} ${filename}`);
  }
});
copy
```

####  `crypto.createPrivateKey(key)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateprivatekeykey)
Added in: v11.6.0History Version | Changes
---|---
v24.6.0 | Add support for ML-DSA keys.
v15.12.0 | The key can also be a JWK object.
v15.0.0 | The key can also be an ArrayBuffer. The encoding option was added. The key cannot contain more than 2 ** 32 - 1 bytes.
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `format` `'pem'`, `'der'`, or '`'jwk'`. **Default:** `'pem'`.
    * `type` `'pkcs1'`, `'pkcs8'` or `'sec1'`. This option is required only if the `format` is `'der'` and ignored otherwise.
    * `passphrase` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The passphrase to use for decryption.
    * `encoding` `key` is a string.
  * Returns: [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)


Creates and returns a new key object containing a private key. If `key` is a string or `Buffer`, `format` is assumed to be `'pem'`; otherwise, `key` must be an object with the properties described above.
If the private key is encrypted, a `passphrase` must be specified. The length of the passphrase is limited to 1024 bytes.
####  `crypto.createPublicKey(key)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatepublickeykey)
Added in: v11.6.0History Version | Changes
---|---
v24.6.0 | Add support for ML-DSA keys.
v15.12.0 | The key can also be a JWK object.
v15.0.0 | The key can also be an ArrayBuffer. The encoding option was added. The key cannot contain more than 2 ** 32 - 1 bytes.
v11.13.0 | The `key` argument can now be a `KeyObject` with type `private`.
v11.7.0 | The `key` argument can now be a private key.
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `format` `'pem'`, `'der'`, or `'jwk'`. **Default:** `'pem'`.
    * `type` `'pkcs1'` or `'spki'`. This option is required only if the `format` is `'der'` and ignored otherwise.
    * `encoding` `key` is a string.
  * Returns: [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)


Creates and returns a new key object containing a public key. If `key` is a string or `Buffer`, `format` is assumed to be `'pem'`; if `key` is a `KeyObject` with type `'private'`, the public key is derived from the given private key; otherwise, `key` must be an object with the properties described above.
