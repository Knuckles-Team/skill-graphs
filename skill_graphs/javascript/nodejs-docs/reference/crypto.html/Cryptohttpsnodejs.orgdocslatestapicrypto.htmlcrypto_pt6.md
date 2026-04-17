If the format is `'pem'`, the `'key'` may also be an X.509 certificate.
Because public keys can be derived from private keys, a private key may be passed instead of a public key. In that case, this function behaves as if [`crypto.createPrivateKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateprivatekeykey) had been called, except that the type of the returned `KeyObject` will be `'public'` and that the private key cannot be extracted from the returned `KeyObject`. Similarly, if a `KeyObject` with type `'private'` is given, a new `KeyObject` with type `'public'` will be returned and it will be impossible to extract the private key from the returned object.
####  `crypto.createSecretKey(key[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatesecretkeykey-encoding)
Added in: v11.6.0History Version | Changes
---|---
v18.8.0, v16.18.0 | The key can now be zero-length.
v15.0.0 | The key can also be an ArrayBuffer or string. The encoding argument was added. The key cannot contain more than 2 ** 32 - 1 bytes.
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` `key` is a string.
  * Returns: [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)


Creates and returns a new key object containing a secret key for symmetric encryption or `Hmac`.
####  `crypto.createSign(algorithm[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatesignalgorithm-options)
Added in: v0.1.92
  * `algorithm`
  * `options` [`stream.Writable` options](https://nodejs.org/docs/latest/api/stream.html#new-streamwritableoptions)
  * Returns: [`<Sign>`](https://nodejs.org/docs/latest/api/crypto.html#class-sign)


Creates and returns a `Sign` object that uses the given `algorithm`. Use [`crypto.getHashes()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogethashes) to obtain the names of the available digest algorithms. Optional `options` argument controls the `stream.Writable` behavior.
In some cases, a `Sign` instance can be created using the name of a signature algorithm, such as `'RSA-SHA256'`, instead of a digest algorithm. This will use the corresponding digest algorithm. This does not work for all signature algorithms, such as `'ecdsa-with-SHA256'`, so it is best to always use digest algorithm names.
####  `crypto.createVerify(algorithm[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateverifyalgorithm-options)
Added in: v0.1.92
  * `algorithm`
  * `options` [`stream.Writable` options](https://nodejs.org/docs/latest/api/stream.html#new-streamwritableoptions)
  * Returns: [`<Verify>`](https://nodejs.org/docs/latest/api/crypto.html#class-verify)


Creates and returns a `Verify` object that uses the given algorithm. Use [`crypto.getHashes()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogethashes) to obtain an array of names of the available signing algorithms. Optional `options` argument controls the `stream.Writable` behavior.
In some cases, a `Verify` instance can be created using the name of a signature algorithm, such as `'RSA-SHA256'`, instead of a digest algorithm. This will use the corresponding digest algorithm. This does not work for all signature algorithms, such as `'ecdsa-with-SHA256'`, so it is best to always use digest algorithm names.
####  `crypto.decapsulate(key, ciphertext[, callback])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptodecapsulatekey-ciphertext-callback)
Added in: v24.7.0
Stability: 1.2 - Release candidate
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) Private Key
  * `ciphertext` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `callback`
    * `err`
    * `sharedKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) if the `callback` function is not provided.


Key decapsulation using a KEM algorithm with a private key.
Supported key types and their KEM algorithms are:
  * `'rsa'`[2](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl30) RSA Secret Value Encapsulation
  * `'ec'`[3](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl32) DHKEM(P-256, HKDF-SHA256), DHKEM(P-384, HKDF-SHA256), DHKEM(P-521, HKDF-SHA256)
  * `'x25519'`[3](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl32) DHKEM(X25519, HKDF-SHA256)
  * `'x448'`[3](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl32) DHKEM(X448, HKDF-SHA512)
  * `'ml-kem-512'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) ML-KEM
  * `'ml-kem-768'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) ML-KEM
  * `'ml-kem-1024'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) ML-KEM


If `key` is not a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject), this function behaves as if `key` had been passed to [`crypto.createPrivateKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateprivatekeykey).
If the `callback` function is provided this function uses libuv's threadpool.
####  `crypto.diffieHellman(options[, callback])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptodiffiehellmanoptions-callback)
Added in: v13.9.0, v12.17.0History Version | Changes
---|---
v23.11.0 | Optional callback argument added.
  * `options`
    * `privateKey` [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)
    * `publicKey` [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)
  * `callback`
    * `err`
    * `secret` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) if the `callback` function is not provided.


Computes the Diffie-Hellman shared secret based on a `privateKey` and a `publicKey`. Both keys must have the same `asymmetricKeyType` and must support either the DH or ECDH operation.
If the `callback` function is provided this function uses libuv's threadpool.
####  `crypto.encapsulate(key[, callback])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptoencapsulatekey-callback)
Added in: v24.7.0
Stability: 1.2 - Release candidate
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) Public Key
  * `callback`
    * `err`
    * `result`
      * `sharedKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)
      * `ciphertext` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)
  * Returns: `callback` function is not provided.
    * `sharedKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)
    * `ciphertext` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Key encapsulation using a KEM algorithm with a public key.
Supported key types and their KEM algorithms are:
  * `'rsa'`[2](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl30) RSA Secret Value Encapsulation
  * `'ec'`[3](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl32) DHKEM(P-256, HKDF-SHA256), DHKEM(P-384, HKDF-SHA256), DHKEM(P-521, HKDF-SHA256)
  * `'x25519'`[3](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl32) DHKEM(X25519, HKDF-SHA256)
  * `'x448'`[3](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl32) DHKEM(X448, HKDF-SHA512)
  * `'ml-kem-512'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) ML-KEM
  * `'ml-kem-768'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) ML-KEM
  * `'ml-kem-1024'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) ML-KEM


If `key` is not a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject), this function behaves as if `key` had been passed to [`crypto.createPublicKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatepublickeykey).
If the `callback` function is provided this function uses libuv's threadpool.
####  `crypto.fips`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptofips)
Added in: v6.0.0Deprecated in: v10.0.0
Stability: 0 - Deprecated
Property for checking and controlling whether a FIPS compliant crypto provider is currently in use. Setting to true requires a FIPS build of Node.js.
This property is deprecated. Please use `crypto.setFips()` and `crypto.getFips()` instead.
####  `crypto.generateKey(type, options, callback)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogeneratekeytype-options-callback)
Added in: v15.0.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `type` `'hmac'` and `'aes'`.
  * `options`
    * `length`
      * If `type` is `'hmac'`, the minimum is 8, and the maximum length is 231-1. If the value is not a multiple of 8, the generated key will be truncated to `Math.floor(length / 8)`.
      * If `type` is `'aes'`, the length must be one of `128`, `192`, or `256`.
  * `callback`
    * `err`
    * `key` [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)


Asynchronously generates a new random secret key of the given `length`. The `type` will determine which validations will be performed on the `length`.
```
const {
  generateKey,
} = await import('node:crypto');

generateKey('hmac', { length: 512 }, (err, key) => {
  if (err) throw err;
  console.log(key.export().toString('hex'));  // 46e..........620
});
const {
  generateKey,
} = require('node:crypto');

generateKey('hmac', { length: 512 }, (err, key) => {
  if (err) throw err;
  console.log(key.export().toString('hex'));  // 46e..........620
});
copy
```

The size of a generated HMAC key should not exceed the block size of the underlying hash function. See [`crypto.createHmac()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatehmacalgorithm-key-options) for more information.
####  `crypto.generateKeyPair(type, options, callback)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogeneratekeypairtype-options-callback)
Added in: v10.12.0History Version | Changes
---|---
v24.8.0 | Add support for SLH-DSA key pairs.
v24.7.0 | Add support for ML-KEM key pairs.
v24.6.0 | Add support for ML-DSA key pairs.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v16.10.0 | Add ability to define `RSASSA-PSS-params` sequence parameters for RSA-PSS keys pairs.
v13.9.0, v12.17.0 | Add support for Diffie-Hellman.
v12.0.0 | Add support for RSA-PSS key pairs.
v12.0.0 | Add ability to generate X25519 and X448 key pairs.
v12.0.0 | Add ability to generate Ed25519 and Ed448 key pairs.
v11.6.0 | The `generateKeyPair` and `generateKeyPairSync` functions now produce key objects if no encoding was specified.
  * `type` [asymmetric key types](https://nodejs.org/docs/latest/api/crypto.html#asymmetric-key-types).
  * `options`
    * `modulusLength`
    * `publicExponent` **Default:** `0x10001`.
    * `hashAlgorithm`
    * `mgf1HashAlgorithm`
    * `saltLength`
    * `divisorLength` `q` in bits (DSA).
    * `namedCurve`
    * `prime` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The prime parameter (DH).
    * `primeLength`
    * `generator` **Default:** `2`.
    * `groupName` [`crypto.getDiffieHellman()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogetdiffiehellmangroupname).
    * `paramEncoding` `'named'` or `'explicit'` (EC). **Default:** `'named'`.
    * `publicKeyEncoding` [`keyObject.export()`](https://nodejs.org/docs/latest/api/crypto.html#keyobjectexportoptions).
    * `privateKeyEncoding` [`keyObject.export()`](https://nodejs.org/docs/latest/api/crypto.html#keyobjectexportoptions).
  * `callback`
    * `err`
    * `publicKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)
    * `privateKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)


Generates a new asymmetric key pair of the given `type`. See the supported [asymmetric key types](https://nodejs.org/docs/latest/api/crypto.html#asymmetric-key-types).
If a `publicKeyEncoding` or `privateKeyEncoding` was specified, this function behaves as if [`keyObject.export()`](https://nodejs.org/docs/latest/api/crypto.html#keyobjectexportoptions) had been called on its result. Otherwise, the respective part of the key is returned as a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject).
It is recommended to encode public keys as `'spki'` and private keys as `'pkcs8'` with encryption for long-term storage:
```
const {
  generateKeyPair,
} = await import('node:crypto');

generateKeyPair('rsa', {
  modulusLength: 4096,
  publicKeyEncoding: {
    type: 'spki',
    format: 'pem',
  },
  privateKeyEncoding: {
    type: 'pkcs8',
    format: 'pem',
    cipher: 'aes-256-cbc',
    passphrase: 'top secret',
  },
}, (err, publicKey, privateKey) => {
  // Handle errors and use the generated key pair.
});
const {
  generateKeyPair,
} = require('node:crypto');

generateKeyPair('rsa', {
  modulusLength: 4096,
  publicKeyEncoding: {
    type: 'spki',
    format: 'pem',
  },
  privateKeyEncoding: {
    type: 'pkcs8',
    format: 'pem',
    cipher: 'aes-256-cbc',
    passphrase: 'top secret',
  },
}, (err, publicKey, privateKey) => {
  // Handle errors and use the generated key pair.
});
copy
```

On completion, `callback` will be called with `err` set to `undefined` and `publicKey` / `privateKey` representing the generated key pair.
If this method is invoked as its [`util.promisify()`](https://nodejs.org/docs/latest/api/util.html#utilpromisifyoriginal)ed version, it returns a `Promise` for an `Object` with `publicKey` and `privateKey` properties.
####  `crypto.generateKeyPairSync(type, options)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogeneratekeypairsynctype-options)
Added in: v10.12.0History Version | Changes
---|---
v24.8.0 | Add support for SLH-DSA key pairs.
v24.7.0 | Add support for ML-KEM key pairs.
v24.6.0 | Add support for ML-DSA key pairs.
v16.10.0 | Add ability to define `RSASSA-PSS-params` sequence parameters for RSA-PSS keys pairs.
v13.9.0, v12.17.0 | Add support for Diffie-Hellman.
v12.0.0 | Add support for RSA-PSS key pairs.
v12.0.0 | Add ability to generate X25519 and X448 key pairs.
v12.0.0 | Add ability to generate Ed25519 and Ed448 key pairs.
v11.6.0 | The `generateKeyPair` and `generateKeyPairSync` functions now produce key objects if no encoding was specified.
  * `type` [asymmetric key types](https://nodejs.org/docs/latest/api/crypto.html#asymmetric-key-types).
  * `options`
    * `modulusLength`
    * `publicExponent` **Default:** `0x10001`.
    * `hashAlgorithm`
    * `mgf1HashAlgorithm`
    * `saltLength`
    * `divisorLength` `q` in bits (DSA).
    * `namedCurve`
    * `prime` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The prime parameter (DH).
    * `primeLength`
    * `generator` **Default:** `2`.
    * `groupName` [`crypto.getDiffieHellman()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogetdiffiehellmangroupname).
    * `paramEncoding` `'named'` or `'explicit'` (EC). **Default:** `'named'`.
    * `publicKeyEncoding` [`keyObject.export()`](https://nodejs.org/docs/latest/api/crypto.html#keyobjectexportoptions).
    * `privateKeyEncoding` [`keyObject.export()`](https://nodejs.org/docs/latest/api/crypto.html#keyobjectexportoptions).
  * Returns:
    * `publicKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)
    * `privateKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)


Generates a new asymmetric key pair of the given `type`. See the supported [asymmetric key types](https://nodejs.org/docs/latest/api/crypto.html#asymmetric-key-types).
If a `publicKeyEncoding` or `privateKeyEncoding` was specified, this function behaves as if [`keyObject.export()`](https://nodejs.org/docs/latest/api/crypto.html#keyobjectexportoptions) had been called on its result. Otherwise, the respective part of the key is returned as a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject).
When encoding public keys, it is recommended to use `'spki'`. When encoding private keys, it is recommended to use `'pkcs8'` with a strong passphrase, and to keep the passphrase confidential.
```
const {
  generateKeyPairSync,
} = await import('node:crypto');

const {
  publicKey,
  privateKey,
} = generateKeyPairSync('rsa', {
  modulusLength: 4096,
  publicKeyEncoding: {
    type: 'spki',
    format: 'pem',
  },
  privateKeyEncoding: {
    type: 'pkcs8',
    format: 'pem',
    cipher: 'aes-256-cbc',
    passphrase: 'top secret',
  },
});
const {
  generateKeyPairSync,
} = require('node:crypto');

const {
  publicKey,
  privateKey,
} = generateKeyPairSync('rsa', {
  modulusLength: 4096,
  publicKeyEncoding: {
    type: 'spki',
    format: 'pem',
  },
  privateKeyEncoding: {
    type: 'pkcs8',
    format: 'pem',
    cipher: 'aes-256-cbc',
    passphrase: 'top secret',
  },
});
copy
```

The return value `{ publicKey, privateKey }` represents the generated key pair. When PEM encoding was selected, the respective key will be a string, otherwise it will be a buffer containing the data encoded as DER.
####  `crypto.generateKeySync(type, options)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogeneratekeysynctype-options)
Added in: v15.0.0
  * `type` `'hmac'` and `'aes'`.
  * `options`
    * `length`
      * If `type` is `'hmac'`, the minimum is 8, and the maximum length is 231-1. If the value is not a multiple of 8, the generated key will be truncated to `Math.floor(length / 8)`.
      * If `type` is `'aes'`, the length must be one of `128`, `192`, or `256`.
  * Returns: [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)


Synchronously generates a new random secret key of the given `length`. The `type` will determine which validations will be performed on the `length`.
```
const {
  generateKeySync,
} = await import('node:crypto');

const key = generateKeySync('hmac', { length: 512 });
console.log(key.export().toString('hex'));  // e89..........41e
const {
  generateKeySync,
} = require('node:crypto');

const key = generateKeySync('hmac', { length: 512 });
console.log(key.export().toString('hex'));  // e89..........41e
copy
```

The size of a generated HMAC key should not exceed the block size of the underlying hash function. See [`crypto.createHmac()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatehmacalgorithm-key-options) for more information.
####  `crypto.generatePrime(size[, options], callback)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogenerateprimesize-options-callback)
Added in: v15.8.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `size`
  * `options`
    * `add` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `rem` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `safe` **Default:** `false`.
    * `bigint` `true`, the generated prime is returned as a `bigint`.
  * `callback`
    * `err`
    * `prime`


Generates a pseudorandom prime of `size` bits.
If `options.safe` is `true`, the prime will be a safe prime -- that is, `(prime - 1) / 2` will also be a prime.
The `options.add` and `options.rem` parameters can be used to enforce additional requirements, e.g., for Diffie-Hellman:
  * If `options.add` and `options.rem` are both set, the prime will satisfy the condition that `prime % add = rem`.
  * If only `options.add` is set and `options.safe` is not `true`, the prime will satisfy the condition that `prime % add = 1`.
  * If only `options.add` is set and `options.safe` is set to `true`, the prime will instead satisfy the condition that `prime % add = 3`. This is necessary because `prime % add = 1` for `options.add > 2` would contradict the condition enforced by `options.safe`.
  * `options.rem` is ignored if `options.add` is not given.


Both `options.add` and `options.rem` must be encoded as big-endian sequences if given as an `ArrayBuffer`, `SharedArrayBuffer`, `TypedArray`, `Buffer`, or `DataView`.
By default, the prime is encoded as a big-endian sequence of octets in an `bigint` option is `true`, then a
The `size` of the prime will have a direct impact on how long it takes to generate the prime. The larger the size, the longer it will take. Because we use OpenSSL's `BN_generate_prime_ex` function, which provides only minimal control over our ability to interrupt the generation process, it is not recommended to generate overly large primes, as doing so may make the process unresponsive.
####  `crypto.generatePrimeSync(size[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogenerateprimesyncsize-options)
Added in: v15.8.0
  * `size`
  * `options`
    * `add` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `rem` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
    * `safe` **Default:** `false`.
    * `bigint` `true`, the generated prime is returned as a `bigint`.
  * Returns:


Generates a pseudorandom prime of `size` bits.
If `options.safe` is `true`, the prime will be a safe prime -- that is, `(prime - 1) / 2` will also be a prime.
The `options.add` and `options.rem` parameters can be used to enforce additional requirements, e.g., for Diffie-Hellman:
  * If `options.add` and `options.rem` are both set, the prime will satisfy the condition that `prime % add = rem`.
  * If only `options.add` is set and `options.safe` is not `true`, the prime will satisfy the condition that `prime % add = 1`.
  * If only `options.add` is set and `options.safe` is set to `true`, the prime will instead satisfy the condition that `prime % add = 3`. This is necessary because `prime % add = 1` for `options.add > 2` would contradict the condition enforced by `options.safe`.
  * `options.rem` is ignored if `options.add` is not given.


Both `options.add` and `options.rem` must be encoded as big-endian sequences if given as an `ArrayBuffer`, `SharedArrayBuffer`, `TypedArray`, `Buffer`, or `DataView`.
By default, the prime is encoded as a big-endian sequence of octets in an `bigint` option is `true`, then a
The `size` of the prime will have a direct impact on how long it takes to generate the prime. The larger the size, the longer it will take. Because we use OpenSSL's `BN_generate_prime_ex` function, which provides only minimal control over our ability to interrupt the generation process, it is not recommended to generate overly large primes, as doing so may make the process unresponsive.
####  `crypto.getCipherInfo(nameOrNid[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogetcipherinfonameornid-options)
Added in: v15.0.0
  * `nameOrNid`
  * `options`
    * `keyLength`
    * `ivLength`
  * Returns:
    * `name`
    * `nid`
    * `blockSize` `mode` is `'stream'`.
    * `ivLength`
    * `keyLength`
    * `mode` `'cbc'`, `'ccm'`, `'cfb'`, `'ctr'`, `'ecb'`, `'gcm'`, `'ocb'`, `'ofb'`, `'stream'`, `'wrap'`, `'xts'`.


Returns information about a given cipher.
Some ciphers accept variable length keys and initialization vectors. By default, the `crypto.getCipherInfo()` method will return the default values for these ciphers. To test if a given key length or iv length is acceptable for given cipher, use the `keyLength` and `ivLength` options. If the given values are unacceptable, `undefined` will be returned.
####  `crypto.getCiphers()`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogetciphers)
Added in: v0.9.3
  * Returns:

```
const {
  getCiphers,
} = await import('node:crypto');

console.log(getCiphers()); // ['aes-128-cbc', 'aes-128-ccm', ...]
const {
  getCiphers,
} = require('node:crypto');

console.log(getCiphers()); // ['aes-128-cbc', 'aes-128-ccm', ...]
copy
```

####  `crypto.getCurves()`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogetcurves)
Added in: v2.3.0
  * Returns:

```
const {
  getCurves,
} = await import('node:crypto');

console.log(getCurves()); // ['Oakley-EC2N-3', 'Oakley-EC2N-4', ...]
const {
  getCurves,
} = require('node:crypto');

console.log(getCurves()); // ['Oakley-EC2N-3', 'Oakley-EC2N-4', ...]
copy
```

####  `crypto.getDiffieHellman(groupName)`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptogetdiffiehellmangroupname)
Added in: v0.7.5
  * `groupName`
  * Returns: [`<DiffieHellmanGroup>`](https://nodejs.org/docs/latest/api/crypto.html#class-diffiehellmangroup)


Creates a predefined `DiffieHellmanGroup` key exchange object. The supported groups are listed in the documentation for [`DiffieHellmanGroup`](https://nodejs.org/docs/latest/api/crypto.html#class-diffiehellmangroup).
