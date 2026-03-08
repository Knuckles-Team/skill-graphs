Example: Using `Decipheriv` objects as streams:
```
import { Buffer } from 'node:buffer';
const {
  scryptSync,
  createDecipheriv,
} = await import('node:crypto');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';
// Key length is dependent on the algorithm. In this case for aes192, it is
// 24 bytes (192 bits).
// Use the async `crypto.scrypt()` instead.
const key = scryptSync(password, 'salt', 24);
// The IV is usually passed along with the ciphertext.
const iv = Buffer.alloc(16, 0); // Initialization vector.

const decipher = createDecipheriv(algorithm, key, iv);

let decrypted = '';
decipher.on('readable', () => {
  let chunk;
  while (null !== (chunk = decipher.read())) {
    decrypted += chunk.toString('utf8');
  }
});
decipher.on('end', () => {
  console.log(decrypted);
  // Prints: some clear text data
});

// Encrypted with same algorithm, key and iv.
const encrypted =
  'e5f79c5915c02171eec6b212d5520d44480993d7d622a7c4c2da32f6efda0ffa';
decipher.write(encrypted, 'hex');
decipher.end();
const {
  scryptSync,
  createDecipheriv,
} = require('node:crypto');
const { Buffer } = require('node:buffer');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';
// Key length is dependent on the algorithm. In this case for aes192, it is
// 24 bytes (192 bits).
// Use the async `crypto.scrypt()` instead.
const key = scryptSync(password, 'salt', 24);
// The IV is usually passed along with the ciphertext.
const iv = Buffer.alloc(16, 0); // Initialization vector.

const decipher = createDecipheriv(algorithm, key, iv);

let decrypted = '';
decipher.on('readable', () => {
  let chunk;
  while (null !== (chunk = decipher.read())) {
    decrypted += chunk.toString('utf8');
  }
});
decipher.on('end', () => {
  console.log(decrypted);
  // Prints: some clear text data
});

// Encrypted with same algorithm, key and iv.
const encrypted =
  'e5f79c5915c02171eec6b212d5520d44480993d7d622a7c4c2da32f6efda0ffa';
decipher.write(encrypted, 'hex');
decipher.end();
copy
```

Example: Using `Decipheriv` and piped streams:
```
import {
  createReadStream,
  createWriteStream,
} from 'node:fs';
import { Buffer } from 'node:buffer';
const {
  scryptSync,
  createDecipheriv,
} = await import('node:crypto');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';
// Use the async `crypto.scrypt()` instead.
const key = scryptSync(password, 'salt', 24);
// The IV is usually passed along with the ciphertext.
const iv = Buffer.alloc(16, 0); // Initialization vector.

const decipher = createDecipheriv(algorithm, key, iv);

const input = createReadStream('test.enc');
const output = createWriteStream('test.js');

input.pipe(decipher).pipe(output);
const {
  createReadStream,
  createWriteStream,
} = require('node:fs');
const {
  scryptSync,
  createDecipheriv,
} = require('node:crypto');
const { Buffer } = require('node:buffer');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';
// Use the async `crypto.scrypt()` instead.
const key = scryptSync(password, 'salt', 24);
// The IV is usually passed along with the ciphertext.
const iv = Buffer.alloc(16, 0); // Initialization vector.

const decipher = createDecipheriv(algorithm, key, iv);

const input = createReadStream('test.enc');
const output = createWriteStream('test.js');

input.pipe(decipher).pipe(output);
copy
```

Example: Using the [`decipher.update()`](https://nodejs.org/docs/latest/api/crypto.html#decipherupdatedata-inputencoding-outputencoding) and [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding) methods:
```
import { Buffer } from 'node:buffer';
const {
  scryptSync,
  createDecipheriv,
} = await import('node:crypto');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';
// Use the async `crypto.scrypt()` instead.
const key = scryptSync(password, 'salt', 24);
// The IV is usually passed along with the ciphertext.
const iv = Buffer.alloc(16, 0); // Initialization vector.

const decipher = createDecipheriv(algorithm, key, iv);

// Encrypted using same algorithm, key and iv.
const encrypted =
  'e5f79c5915c02171eec6b212d5520d44480993d7d622a7c4c2da32f6efda0ffa';
let decrypted = decipher.update(encrypted, 'hex', 'utf8');
decrypted += decipher.final('utf8');
console.log(decrypted);
// Prints: some clear text data
const {
  scryptSync,
  createDecipheriv,
} = require('node:crypto');
const { Buffer } = require('node:buffer');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';
// Use the async `crypto.scrypt()` instead.
const key = scryptSync(password, 'salt', 24);
// The IV is usually passed along with the ciphertext.
const iv = Buffer.alloc(16, 0); // Initialization vector.

const decipher = createDecipheriv(algorithm, key, iv);

// Encrypted using same algorithm, key and iv.
const encrypted =
  'e5f79c5915c02171eec6b212d5520d44480993d7d622a7c4c2da32f6efda0ffa';
let decrypted = decipher.update(encrypted, 'hex', 'utf8');
decrypted += decipher.final('utf8');
console.log(decrypted);
// Prints: some clear text data
copy
```

####  `decipher.final([outputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding)
Added in: v0.1.94
  * `outputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `outputEncoding` is specified, a string is returned. If an `outputEncoding` is not provided, a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.


Once the `decipher.final()` method has been called, the `Decipheriv` object can no longer be used to decrypt data. Attempts to call `decipher.final()` more than once will result in an error being thrown.
####  `decipher.setAAD(buffer[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#deciphersetaadbuffer-options)
Added in: v1.0.0History Version | Changes
---|---
v15.0.0 | The buffer argument can be a string or ArrayBuffer and is limited to no more than 2 ** 31 - 1 bytes.
v7.2.0 | This method now returns a reference to `decipher`.
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options` [`stream.transform` options](https://nodejs.org/docs/latest/api/stream.html#new-streamtransformoptions)
    * `plaintextLength`
    * `encoding` `buffer` is a string.
  * Returns: [`<Decipheriv>`](https://nodejs.org/docs/latest/api/crypto.html#class-decipheriv) The same Decipher for method chaining.


When using an authenticated encryption mode (`GCM`, `CCM`, `OCB`, and `chacha20-poly1305` are currently supported), the `decipher.setAAD()` method sets the value used for the _additional authenticated data_ (AAD) input parameter.
The `options` argument is optional for `GCM`. When using `CCM`, the `plaintextLength` option must be specified and its value must match the length of the ciphertext in bytes. See [CCM mode](https://nodejs.org/docs/latest/api/crypto.html#ccm-mode).
The `decipher.setAAD()` method must be called before [`decipher.update()`](https://nodejs.org/docs/latest/api/crypto.html#decipherupdatedata-inputencoding-outputencoding).
When passing a string as the `buffer`, please consider [caveats when using strings as inputs to cryptographic APIs](https://nodejs.org/docs/latest/api/crypto.html#using-strings-as-inputs-to-cryptographic-apis).
####  `decipher.setAuthTag(buffer[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#deciphersetauthtagbuffer-encoding)
Added in: v1.0.0History Version | Changes
---|---
v22.0.0, v20.13.0 | Using GCM tag lengths other than 128 bits without specifying the `authTagLength` option when creating `decipher` is deprecated.
v15.0.0 | The buffer argument can be a string or ArrayBuffer and is limited to no more than 2 ** 31 - 1 bytes.
v11.0.0 | This method now throws if the GCM tag length is invalid.
v7.2.0 | This method now returns a reference to `decipher`.
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` `buffer` is a string.
  * Returns: [`<Decipheriv>`](https://nodejs.org/docs/latest/api/crypto.html#class-decipheriv) The same Decipher for method chaining.


When using an authenticated encryption mode (`GCM`, `CCM`, `OCB`, and `chacha20-poly1305` are currently supported), the `decipher.setAuthTag()` method is used to pass in the received _authentication tag_. If no tag is provided, or if the cipher text has been tampered with, [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding) will throw, indicating that the cipher text should be discarded due to failed authentication. If the tag length is invalid according to `authTagLength` option, `decipher.setAuthTag()` will throw an error.
The `decipher.setAuthTag()` method must be called before [`decipher.update()`](https://nodejs.org/docs/latest/api/crypto.html#decipherupdatedata-inputencoding-outputencoding) for `CCM` mode or before [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding) for `GCM` and `OCB` modes and `chacha20-poly1305`. `decipher.setAuthTag()` can only be called once.
Because the `node:crypto` module was originally designed to closely mirror OpenSSL's behavior, this function permits short GCM authentication tags unless an explicit authentication tag length was passed to [`crypto.createDecipheriv()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatedecipherivalgorithm-key-iv-options) when the `decipher` object was created. This behavior is deprecated and subject to change (see [DEP0182](https://nodejs.org/docs/latest/api/deprecations.html#dep0182-short-gcm-authentication-tags-without-explicit-authtaglength)). **In the meantime, applications should either set the`authTagLength` option when calling `createDecipheriv()` or check the actual authentication tag length before passing it to `setAuthTag()`.**
When passing a string as the authentication tag, please consider [caveats when using strings as inputs to cryptographic APIs](https://nodejs.org/docs/latest/api/crypto.html#using-strings-as-inputs-to-cryptographic-apis).
####  `decipher.setAutoPadding([autoPadding])`[#](https://nodejs.org/docs/latest/api/crypto.html#deciphersetautopaddingautopadding)
Added in: v0.7.1
  * `autoPadding` **Default:** `true`
  * Returns: [`<Decipheriv>`](https://nodejs.org/docs/latest/api/crypto.html#class-decipheriv) The same Decipher for method chaining.


When data has been encrypted without standard block padding, calling `decipher.setAutoPadding(false)` will disable automatic padding to prevent [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding) from checking for and removing padding.
Turning auto padding off will only work if the input data's length is a multiple of the ciphers block size.
The `decipher.setAutoPadding()` method must be called before [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding).
####  `decipher.update(data[, inputEncoding][, outputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#decipherupdatedata-inputencoding-outputencoding)
Added in: v0.1.94History Version | Changes
---|---
v6.0.0 | The default `inputEncoding` changed from `binary` to `utf8`.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `inputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `data` string.
  * `outputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Updates the decipher with `data`. If the `inputEncoding` argument is given, the `data` argument is a string using the specified encoding. If the `inputEncoding` argument is not given, `data` must be a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html). If `data` is a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) then `inputEncoding` is ignored.
The `outputEncoding` specifies the output format of the enciphered data. If the `outputEncoding` is specified, a string using the specified encoding is returned. If no `outputEncoding` is provided, a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
The `decipher.update()` method can be called multiple times with new data until [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding) is called. Calling `decipher.update()` after [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding) will result in an error being thrown.
Even if the underlying cipher implements authentication, the authenticity and integrity of the plaintext returned from this function may be uncertain at this time. For authenticated encryption algorithms, authenticity is generally only established when the application calls [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding).
### Class: `DiffieHellman`[#](https://nodejs.org/docs/latest/api/crypto.html#class-diffiehellman)
Added in: v0.5.0
The `DiffieHellman` class is a utility for creating Diffie-Hellman key exchanges.
Instances of the `DiffieHellman` class can be created using the [`crypto.createDiffieHellman()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatediffiehellmanprime-primeencoding-generator-generatorencoding) function.
```
import assert from 'node:assert';

const {
  createDiffieHellman,
} = await import('node:crypto');

// Generate Alice's keys...
const alice = createDiffieHellman(2048);
const aliceKey = alice.generateKeys();

// Generate Bob's keys...
const bob = createDiffieHellman(alice.getPrime(), alice.getGenerator());
const bobKey = bob.generateKeys();

// Exchange and generate the secret...
const aliceSecret = alice.computeSecret(bobKey);
const bobSecret = bob.computeSecret(aliceKey);

// OK
assert.strictEqual(aliceSecret.toString('hex'), bobSecret.toString('hex'));
const assert = require('node:assert');

const {
  createDiffieHellman,
} = require('node:crypto');

// Generate Alice's keys...
const alice = createDiffieHellman(2048);
const aliceKey = alice.generateKeys();

// Generate Bob's keys...
const bob = createDiffieHellman(alice.getPrime(), alice.getGenerator());
const bobKey = bob.generateKeys();

// Exchange and generate the secret...
const aliceSecret = alice.computeSecret(bobKey);
const bobSecret = bob.computeSecret(aliceKey);

// OK
assert.strictEqual(aliceSecret.toString('hex'), bobSecret.toString('hex'));
copy
```

####  `diffieHellman.computeSecret(otherPublicKey[, inputEncoding][, outputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmancomputesecretotherpublickey-inputencoding-outputencoding)
Added in: v0.5.0
  * `otherPublicKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `inputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of an `otherPublicKey` string.
  * `outputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Computes the shared secret using `otherPublicKey` as the other party's public key and returns the computed shared secret. The supplied key is interpreted using the specified `inputEncoding`, and secret is encoded using specified `outputEncoding`. If the `inputEncoding` is not provided, `otherPublicKey` is expected to be a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`.
If `outputEncoding` is given a string is returned; otherwise, a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
####  `diffieHellman.generateKeys([encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmangeneratekeysencoding)
Added in: v0.5.0
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Generates private and public Diffie-Hellman key values unless they have been generated or computed already, and returns the public key in the specified `encoding`. This key should be transferred to the other party. If `encoding` is provided a string is returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
This function is a thin wrapper around
####  `diffieHellman.getGenerator([encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmangetgeneratorencoding)
Added in: v0.5.0
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Returns the Diffie-Hellman generator in the specified `encoding`. If `encoding` is provided a string is returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
####  `diffieHellman.getPrime([encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmangetprimeencoding)
Added in: v0.5.0
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Returns the Diffie-Hellman prime in the specified `encoding`. If `encoding` is provided a string is returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
####  `diffieHellman.getPrivateKey([encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmangetprivatekeyencoding)
Added in: v0.5.0
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Returns the Diffie-Hellman private key in the specified `encoding`. If `encoding` is provided a string is returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
####  `diffieHellman.getPublicKey([encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmangetpublickeyencoding)
Added in: v0.5.0
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Returns the Diffie-Hellman public key in the specified `encoding`. If `encoding` is provided a string is returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
####  `diffieHellman.setPrivateKey(privateKey[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmansetprivatekeyprivatekey-encoding)
Added in: v0.5.0
  * `privateKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `privateKey` string.


Sets the Diffie-Hellman private key. If the `encoding` argument is provided, `privateKey` is expected to be a string. If no `encoding` is provided, `privateKey` is expected to be a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`.
This function does not automatically compute the associated public key. Either [`diffieHellman.setPublicKey()`](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmansetpublickeypublickey-encoding) or [`diffieHellman.generateKeys()`](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmangeneratekeysencoding) can be used to manually provide the public key or to automatically derive it.
####  `diffieHellman.setPublicKey(publicKey[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmansetpublickeypublickey-encoding)
Added in: v0.5.0
  * `publicKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `publicKey` string.


Sets the Diffie-Hellman public key. If the `encoding` argument is provided, `publicKey` is expected to be a string. If no `encoding` is provided, `publicKey` is expected to be a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`.
####  `diffieHellman.verifyError`[#](https://nodejs.org/docs/latest/api/crypto.html#diffiehellmanverifyerror)
Added in: v0.11.12
A bit field containing any warnings and/or errors resulting from a check performed during initialization of the `DiffieHellman` object.
The following values are valid for this property (as defined in `node:constants` module):
  * `DH_CHECK_P_NOT_SAFE_PRIME`
  * `DH_CHECK_P_NOT_PRIME`
  * `DH_UNABLE_TO_CHECK_GENERATOR`
  * `DH_NOT_SUITABLE_GENERATOR`


### Class: `DiffieHellmanGroup`[#](https://nodejs.org/docs/latest/api/crypto.html#class-diffiehellmangroup)
Added in: v0.7.5
The `DiffieHellmanGroup` class takes a well-known modp group as its argument. It works the same as `DiffieHellman`, except that it does not allow changing its keys after creation. In other words, it does not implement `setPublicKey()` or `setPrivateKey()` methods.
```
const { createDiffieHellmanGroup } = await import('node:crypto');
const dh = createDiffieHellmanGroup('modp16');
const { createDiffieHellmanGroup } = require('node:crypto');
const dh = createDiffieHellmanGroup('modp16');
copy
```

The following groups are supported:
  * `'modp14'` (2048 bits,
  * `'modp15'` (3072 bits,
  * `'modp16'` (4096 bits,
  * `'modp17'` (6144 bits,
  * `'modp18'` (8192 bits,


The following groups are still supported but deprecated (see [Caveats](https://nodejs.org/docs/latest/api/crypto.html#support-for-weak-or-compromised-algorithms)):
  * `'modp1'` (768 bits,
  * `'modp2'` (1024 bits,
  * `'modp5'` (1536 bits,


These deprecated groups might be removed in future versions of Node.js.
### Class: `ECDH`[#](https://nodejs.org/docs/latest/api/crypto.html#class-ecdh)
Added in: v0.11.14
The `ECDH` class is a utility for creating Elliptic Curve Diffie-Hellman (ECDH) key exchanges.
Instances of the `ECDH` class can be created using the [`crypto.createECDH()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateecdhcurvename) function.
```
import assert from 'node:assert';

const {
  createECDH,
} = await import('node:crypto');

// Generate Alice's keys...
const alice = createECDH('secp521r1');
const aliceKey = alice.generateKeys();

// Generate Bob's keys...
const bob = createECDH('secp521r1');
const bobKey = bob.generateKeys();

// Exchange and generate the secret...
const aliceSecret = alice.computeSecret(bobKey);
const bobSecret = bob.computeSecret(aliceKey);

assert.strictEqual(aliceSecret.toString('hex'), bobSecret.toString('hex'));
// OK
const assert = require('node:assert');

const {
  createECDH,
} = require('node:crypto');

// Generate Alice's keys...
const alice = createECDH('secp521r1');
const aliceKey = alice.generateKeys();

// Generate Bob's keys...
const bob = createECDH('secp521r1');
const bobKey = bob.generateKeys();

// Exchange and generate the secret...
const aliceSecret = alice.computeSecret(bobKey);
const bobSecret = bob.computeSecret(aliceKey);

assert.strictEqual(aliceSecret.toString('hex'), bobSecret.toString('hex'));
// OK
copy
```

#### Static method: `ECDH.convertKey(key, curve[, inputEncoding[, outputEncoding[, format]]])`[#](https://nodejs.org/docs/latest/api/crypto.html#static-method-ecdhconvertkeykey-curve-inputencoding-outputencoding-format)
Added in: v10.0.0
  * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `curve`
  * `inputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `key` string.
  * `outputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * `format` **Default:** `'uncompressed'`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Converts the EC Diffie-Hellman public key specified by `key` and `curve` to the format specified by `format`. The `format` argument specifies point encoding and can be `'compressed'`, `'uncompressed'` or `'hybrid'`. The supplied key is interpreted using the specified `inputEncoding`, and the returned key is encoded using the specified `outputEncoding`.
Use [`crypto.getCurves()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogetcurves) to obtain a list of available curve names. On recent OpenSSL releases, `openssl ecparam -list_curves` will also display the name and description of each available elliptic curve.
If `format` is not specified the point will be returned in `'uncompressed'` format.
If the `inputEncoding` is not provided, `key` is expected to be a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`.
Example (uncompressing a key):
```
const {
  createECDH,
  ECDH,
} = await import('node:crypto');

const ecdh = createECDH('secp256k1');
ecdh.generateKeys();
