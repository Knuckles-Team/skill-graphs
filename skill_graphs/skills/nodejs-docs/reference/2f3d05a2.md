## Crypto[#](https://nodejs.org/docs/latest/api/crypto.html#crypto)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:crypto` module provides cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.
```
const { createHmac } = await import('node:crypto');

const secret = 'abcdefg';
const hash = createHmac('sha256', secret)
               .update('I love cupcakes')
               .digest('hex');
console.log(hash);
// Prints:
//   c0fa1bc00531bd78ef38c628449c5102aeabd49b5dc3a2a516ea6ea959d6658e
const { createHmac } = require('node:crypto');

const secret = 'abcdefg';
const hash = createHmac('sha256', secret)
               .update('I love cupcakes')
               .digest('hex');
console.log(hash);
// Prints:
//   c0fa1bc00531bd78ef38c628449c5102aeabd49b5dc3a2a516ea6ea959d6658e
copy
```

### Determining if crypto support is unavailable[#](https://nodejs.org/docs/latest/api/crypto.html#determining-if-crypto-support-is-unavailable)
It is possible for Node.js to be built without including support for the `node:crypto` module. In such cases, attempting to `import` from `crypto` or calling `require('node:crypto')` will result in an error being thrown.
When using CommonJS, the error thrown can be caught using try/catch:
```
let crypto;
try {
  crypto = require('node:crypto');
} catch (err) {
  console.error('crypto support is disabled!');
}
copy
```

When using the lexical ESM `import` keyword, the error can only be caught if a handler for `process.on('uncaughtException')` is registered _before_ any attempt to load the module is made (using, for instance, a preload module).
When using ESM, if there is a chance that the code may be run on a build of Node.js where crypto support is not enabled, consider using the `import` keyword:
```
let crypto;
try {
  crypto = await import('node:crypto');
} catch (err) {
  console.error('crypto support is disabled!');
}
copy
```

### Asymmetric key types[#](https://nodejs.org/docs/latest/api/crypto.html#asymmetric-key-types)
The following table lists the asymmetric key types recognized by the [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) API:
Key Type | Description | OID
---|---|---
`'dh'` | Diffie-Hellman | 1.2.840.113549.1.3.1
`'dsa'` | DSA | 1.2.840.10040.4.1
`'ec'` | Elliptic curve | 1.2.840.10045.2.1
`'ed25519'` | Ed25519 | 1.3.101.112
`'ed448'` | Ed448 | 1.3.101.113
`'ml-dsa-44'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | ML-DSA-44 | 2.16.840.1.101.3.4.3.17
`'ml-dsa-65'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | ML-DSA-65 | 2.16.840.1.101.3.4.3.18
`'ml-dsa-87'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | ML-DSA-87 | 2.16.840.1.101.3.4.3.19
`'ml-kem-512'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | ML-KEM-512 | 2.16.840.1.101.3.4.4.1
`'ml-kem-768'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | ML-KEM-768 | 2.16.840.1.101.3.4.4.2
`'ml-kem-1024'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | ML-KEM-1024 | 2.16.840.1.101.3.4.4.3
`'rsa-pss'` | RSA PSS | 1.2.840.113549.1.1.10
`'rsa'` | RSA | 1.2.840.113549.1.1.1
`'slh-dsa-sha2-128f'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHA2-128f | 2.16.840.1.101.3.4.3.21
`'slh-dsa-sha2-128s'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHA2-128s | 2.16.840.1.101.3.4.3.20
`'slh-dsa-sha2-192f'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHA2-192f | 2.16.840.1.101.3.4.3.23
`'slh-dsa-sha2-192s'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHA2-192s | 2.16.840.1.101.3.4.3.22
`'slh-dsa-sha2-256f'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHA2-256f | 2.16.840.1.101.3.4.3.25
`'slh-dsa-sha2-256s'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHA2-256s | 2.16.840.1.101.3.4.3.24
`'slh-dsa-shake-128f'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHAKE-128f | 2.16.840.1.101.3.4.3.27
`'slh-dsa-shake-128s'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHAKE-128s | 2.16.840.1.101.3.4.3.26
`'slh-dsa-shake-192f'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHAKE-192f | 2.16.840.1.101.3.4.3.29
`'slh-dsa-shake-192s'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHAKE-192s | 2.16.840.1.101.3.4.3.28
`'slh-dsa-shake-256f'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHAKE-256f | 2.16.840.1.101.3.4.3.31
`'slh-dsa-shake-256s'`[1](https://nodejs.org/docs/latest/api/crypto.html#user-content-fn-openssl35) | SLH-DSA-SHAKE-256s | 2.16.840.1.101.3.4.3.30
`'x25519'` | X25519 | 1.3.101.110
`'x448'` | X448 | 1.3.101.111
### Class: `Certificate`[#](https://nodejs.org/docs/latest/api/crypto.html#class-certificate)
Added in: v0.11.8
SPKAC is a Certificate Signing Request mechanism originally implemented by Netscape and was specified formally as part of HTML5's `keygen` element.
`<keygen>` is deprecated since
The `node:crypto` module provides the `Certificate` class for working with SPKAC data. The most common usage is handling output generated by the HTML5 `<keygen>` element. Node.js uses
#### Static method: `Certificate.exportChallenge(spkac[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#static-method-certificateexportchallengespkac-encoding)
Added in: v9.0.0History Version | Changes
---|---
v15.0.0 | The spkac argument can be an ArrayBuffer. Limited the size of the spkac argument to a maximum of 2**31 - 1 bytes.
  * `spkac` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `spkac` string.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The challenge component of the `spkac` data structure, which includes a public key and a challenge.

```
const { Certificate } = await import('node:crypto');
const spkac = getSpkacSomehow();
const challenge = Certificate.exportChallenge(spkac);
console.log(challenge.toString('utf8'));
// Prints: the challenge as a UTF8 string
const { Certificate } = require('node:crypto');
const spkac = getSpkacSomehow();
const challenge = Certificate.exportChallenge(spkac);
console.log(challenge.toString('utf8'));
// Prints: the challenge as a UTF8 string
copy
```

#### Static method: `Certificate.exportPublicKey(spkac[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#static-method-certificateexportpublickeyspkac-encoding)
Added in: v9.0.0History Version | Changes
---|---
v15.0.0 | The spkac argument can be an ArrayBuffer. Limited the size of the spkac argument to a maximum of 2**31 - 1 bytes.
  * `spkac` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `spkac` string.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The public key component of the `spkac` data structure, which includes a public key and a challenge.

```
const { Certificate } = await import('node:crypto');
const spkac = getSpkacSomehow();
const publicKey = Certificate.exportPublicKey(spkac);
console.log(publicKey);
// Prints: the public key as <Buffer ...>
const { Certificate } = require('node:crypto');
const spkac = getSpkacSomehow();
const publicKey = Certificate.exportPublicKey(spkac);
console.log(publicKey);
// Prints: the public key as <Buffer ...>
copy
```

#### Static method: `Certificate.verifySpkac(spkac[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#static-method-certificateverifyspkacspkac-encoding)
Added in: v9.0.0History Version | Changes
---|---
v15.0.0 | The spkac argument can be an ArrayBuffer. Added encoding. Limited the size of the spkac argument to a maximum of 2**31 - 1 bytes.
  * `spkac` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `spkac` string.
  * Returns: `true` if the given `spkac` data structure is valid, `false` otherwise.

```
import { Buffer } from 'node:buffer';
const { Certificate } = await import('node:crypto');

const spkac = getSpkacSomehow();
console.log(Certificate.verifySpkac(Buffer.from(spkac)));
// Prints: true or false
const { Buffer } = require('node:buffer');
const { Certificate } = require('node:crypto');

const spkac = getSpkacSomehow();
console.log(Certificate.verifySpkac(Buffer.from(spkac)));
// Prints: true or false
copy
```

#### Legacy API[#](https://nodejs.org/docs/latest/api/crypto.html#legacy-api)
Stability: 0 - Deprecated
As a legacy interface, it is possible to create new instances of the `crypto.Certificate` class as illustrated in the examples below.
#####  `new crypto.Certificate()`[#](https://nodejs.org/docs/latest/api/crypto.html#new-cryptocertificate)
Instances of the `Certificate` class can be created using the `new` keyword or by calling `crypto.Certificate()` as a function:
```
const { Certificate } = await import('node:crypto');

const cert1 = new Certificate();
const cert2 = Certificate();
const { Certificate } = require('node:crypto');

const cert1 = new Certificate();
const cert2 = Certificate();
copy
```

#####  `certificate.exportChallenge(spkac[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#certificateexportchallengespkac-encoding)
Added in: v0.11.8
  * `spkac` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `spkac` string.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The challenge component of the `spkac` data structure, which includes a public key and a challenge.

```
const { Certificate } = await import('node:crypto');
const cert = Certificate();
const spkac = getSpkacSomehow();
const challenge = cert.exportChallenge(spkac);
console.log(challenge.toString('utf8'));
// Prints: the challenge as a UTF8 string
const { Certificate } = require('node:crypto');
const cert = Certificate();
const spkac = getSpkacSomehow();
const challenge = cert.exportChallenge(spkac);
console.log(challenge.toString('utf8'));
// Prints: the challenge as a UTF8 string
copy
```

#####  `certificate.exportPublicKey(spkac[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#certificateexportpublickeyspkac-encoding)
Added in: v0.11.8
  * `spkac` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `spkac` string.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The public key component of the `spkac` data structure, which includes a public key and a challenge.

```
const { Certificate } = await import('node:crypto');
const cert = Certificate();
const spkac = getSpkacSomehow();
const publicKey = cert.exportPublicKey(spkac);
console.log(publicKey);
// Prints: the public key as <Buffer ...>
const { Certificate } = require('node:crypto');
const cert = Certificate();
const spkac = getSpkacSomehow();
const publicKey = cert.exportPublicKey(spkac);
console.log(publicKey);
// Prints: the public key as <Buffer ...>
copy
```

#####  `certificate.verifySpkac(spkac[, encoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#certificateverifyspkacspkac-encoding)
Added in: v0.11.8
  * `spkac` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `spkac` string.
  * Returns: `true` if the given `spkac` data structure is valid, `false` otherwise.

```
import { Buffer } from 'node:buffer';
const { Certificate } = await import('node:crypto');

const cert = Certificate();
const spkac = getSpkacSomehow();
console.log(cert.verifySpkac(Buffer.from(spkac)));
// Prints: true or false
const { Buffer } = require('node:buffer');
const { Certificate } = require('node:crypto');

const cert = Certificate();
const spkac = getSpkacSomehow();
console.log(cert.verifySpkac(Buffer.from(spkac)));
// Prints: true or false
copy
```

### Class: `Cipheriv`[#](https://nodejs.org/docs/latest/api/crypto.html#class-cipheriv)
Added in: v0.1.94
  * Extends: [`<stream.Transform>`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform)


Instances of the `Cipheriv` class are used to encrypt data. The class can be used in one of two ways:
  * As a [stream](https://nodejs.org/docs/latest/api/stream.html) that is both readable and writable, where plain unencrypted data is written to produce encrypted data on the readable side, or
  * Using the [`cipher.update()`](https://nodejs.org/docs/latest/api/crypto.html#cipherupdatedata-inputencoding-outputencoding) and [`cipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#cipherfinaloutputencoding) methods to produce the encrypted data.


The [`crypto.createCipheriv()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatecipherivalgorithm-key-iv-options) method is used to create `Cipheriv` instances. `Cipheriv` objects are not to be created directly using the `new` keyword.
Example: Using `Cipheriv` objects as streams:
```
const {
  scrypt,
  randomFill,
  createCipheriv,
} = await import('node:crypto');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';

// First, we'll generate the key. The key length is dependent on the algorithm.
// In this case for aes192, it is 24 bytes (192 bits).
scrypt(password, 'salt', 24, (err, key) => {
  if (err) throw err;
  // Then, we'll generate a random initialization vector
  randomFill(new Uint8Array(16), (err, iv) => {
    if (err) throw err;

    // Once we have the key and iv, we can create and use the cipher...
    const cipher = createCipheriv(algorithm, key, iv);

    let encrypted = '';
    cipher.setEncoding('hex');

    cipher.on('data', (chunk) => encrypted += chunk);
    cipher.on('end', () => console.log(encrypted));

    cipher.write('some clear text data');
    cipher.end();
  });
});
const {
  scrypt,
  randomFill,
  createCipheriv,
} = require('node:crypto');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';

// First, we'll generate the key. The key length is dependent on the algorithm.
// In this case for aes192, it is 24 bytes (192 bits).
scrypt(password, 'salt', 24, (err, key) => {
  if (err) throw err;
  // Then, we'll generate a random initialization vector
  randomFill(new Uint8Array(16), (err, iv) => {
    if (err) throw err;

    // Once we have the key and iv, we can create and use the cipher...
    const cipher = createCipheriv(algorithm, key, iv);

    let encrypted = '';
    cipher.setEncoding('hex');

    cipher.on('data', (chunk) => encrypted += chunk);
    cipher.on('end', () => console.log(encrypted));

    cipher.write('some clear text data');
    cipher.end();
  });
});
copy
```

Example: Using `Cipheriv` and piped streams:
```
import {
  createReadStream,
  createWriteStream,
} from 'node:fs';

import {
  pipeline,
} from 'node:stream';

const {
  scrypt,
  randomFill,
  createCipheriv,
} = await import('node:crypto');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';

// First, we'll generate the key. The key length is dependent on the algorithm.
// In this case for aes192, it is 24 bytes (192 bits).
scrypt(password, 'salt', 24, (err, key) => {
  if (err) throw err;
  // Then, we'll generate a random initialization vector
  randomFill(new Uint8Array(16), (err, iv) => {
    if (err) throw err;

    const cipher = createCipheriv(algorithm, key, iv);

    const input = createReadStream('test.js');
    const output = createWriteStream('test.enc');

    pipeline(input, cipher, output, (err) => {
      if (err) throw err;
    });
  });
});
const {
  createReadStream,
  createWriteStream,
} = require('node:fs');

const {
  pipeline,
} = require('node:stream');

const {
  scrypt,
  randomFill,
  createCipheriv,
} = require('node:crypto');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';

// First, we'll generate the key. The key length is dependent on the algorithm.
// In this case for aes192, it is 24 bytes (192 bits).
scrypt(password, 'salt', 24, (err, key) => {
  if (err) throw err;
  // Then, we'll generate a random initialization vector
  randomFill(new Uint8Array(16), (err, iv) => {
    if (err) throw err;

    const cipher = createCipheriv(algorithm, key, iv);

    const input = createReadStream('test.js');
    const output = createWriteStream('test.enc');

    pipeline(input, cipher, output, (err) => {
      if (err) throw err;
    });
  });
});
copy
```

Example: Using the [`cipher.update()`](https://nodejs.org/docs/latest/api/crypto.html#cipherupdatedata-inputencoding-outputencoding) and [`cipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#cipherfinaloutputencoding) methods:
```
const {
  scrypt,
  randomFill,
  createCipheriv,
} = await import('node:crypto');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';

// First, we'll generate the key. The key length is dependent on the algorithm.
// In this case for aes192, it is 24 bytes (192 bits).
scrypt(password, 'salt', 24, (err, key) => {
  if (err) throw err;
  // Then, we'll generate a random initialization vector
  randomFill(new Uint8Array(16), (err, iv) => {
    if (err) throw err;

    const cipher = createCipheriv(algorithm, key, iv);

    let encrypted = cipher.update('some clear text data', 'utf8', 'hex');
    encrypted += cipher.final('hex');
    console.log(encrypted);
  });
});
const {
  scrypt,
  randomFill,
  createCipheriv,
} = require('node:crypto');

const algorithm = 'aes-192-cbc';
const password = 'Password used to generate key';

// First, we'll generate the key. The key length is dependent on the algorithm.
// In this case for aes192, it is 24 bytes (192 bits).
scrypt(password, 'salt', 24, (err, key) => {
  if (err) throw err;
  // Then, we'll generate a random initialization vector
  randomFill(new Uint8Array(16), (err, iv) => {
    if (err) throw err;

    const cipher = createCipheriv(algorithm, key, iv);

    let encrypted = cipher.update('some clear text data', 'utf8', 'hex');
    encrypted += cipher.final('hex');
    console.log(encrypted);
  });
});
copy
```

####  `cipher.final([outputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#cipherfinaloutputencoding)
Added in: v0.1.94
  * `outputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `outputEncoding` is specified, a string is returned. If an `outputEncoding` is not provided, a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.


Once the `cipher.final()` method has been called, the `Cipheriv` object can no longer be used to encrypt data. Attempts to call `cipher.final()` more than once will result in an error being thrown.
####  `cipher.getAuthTag()`[#](https://nodejs.org/docs/latest/api/crypto.html#ciphergetauthtag)
Added in: v1.0.0
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) When using an authenticated encryption mode (`GCM`, `CCM`, `OCB`, and `chacha20-poly1305` are currently supported), the `cipher.getAuthTag()` method returns a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) containing the _authentication tag_ that has been computed from the given data.


The `cipher.getAuthTag()` method should only be called after encryption has been completed using the [`cipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#cipherfinaloutputencoding) method.
If the `authTagLength` option was set during the `cipher` instance's creation, this function will return exactly `authTagLength` bytes.
####  `cipher.setAAD(buffer[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#ciphersetaadbuffer-options)
Added in: v1.0.0
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `options` [`stream.transform` options](https://nodejs.org/docs/latest/api/stream.html#new-streamtransformoptions)
    * `plaintextLength`
    * `encoding` `buffer` is a string.
  * Returns: [`<Cipheriv>`](https://nodejs.org/docs/latest/api/crypto.html#class-cipheriv) The same `Cipheriv` instance for method chaining.


When using an authenticated encryption mode (`GCM`, `CCM`, `OCB`, and `chacha20-poly1305` are currently supported), the `cipher.setAAD()` method sets the value used for the _additional authenticated data_ (AAD) input parameter.
The `plaintextLength` option is optional for `GCM` and `OCB`. When using `CCM`, the `plaintextLength` option must be specified and its value must match the length of the plaintext in bytes. See [CCM mode](https://nodejs.org/docs/latest/api/crypto.html#ccm-mode).
The `cipher.setAAD()` method must be called before [`cipher.update()`](https://nodejs.org/docs/latest/api/crypto.html#cipherupdatedata-inputencoding-outputencoding).
####  `cipher.setAutoPadding([autoPadding])`[#](https://nodejs.org/docs/latest/api/crypto.html#ciphersetautopaddingautopadding)
Added in: v0.7.1
  * `autoPadding` **Default:** `true`
  * Returns: [`<Cipheriv>`](https://nodejs.org/docs/latest/api/crypto.html#class-cipheriv) The same `Cipheriv` instance for method chaining.


When using block encryption algorithms, the `Cipheriv` class will automatically add padding to the input data to the appropriate block size. To disable the default padding call `cipher.setAutoPadding(false)`.
When `autoPadding` is `false`, the length of the entire input data must be a multiple of the cipher's block size or [`cipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#cipherfinaloutputencoding) will throw an error. Disabling automatic padding is useful for non-standard padding, for instance using `0x0` instead of PKCS padding.
The `cipher.setAutoPadding()` method must be called before [`cipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#cipherfinaloutputencoding).
####  `cipher.update(data[, inputEncoding][, outputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#cipherupdatedata-inputencoding-outputencoding)
Added in: v0.1.94History Version | Changes
---|---
v6.0.0 | The default `inputEncoding` changed from `binary` to `utf8`.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `inputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the data.
  * `outputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Updates the cipher with `data`. If the `inputEncoding` argument is given, the `data` argument is a string using the specified encoding. If the `inputEncoding` argument is not given, `data` must be a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`. If `data` is a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`, then `inputEncoding` is ignored.
The `outputEncoding` specifies the output format of the enciphered data. If the `outputEncoding` is specified, a string using the specified encoding is returned. If no `outputEncoding` is provided, a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
The `cipher.update()` method can be called multiple times with new data until [`cipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#cipherfinaloutputencoding) is called. Calling `cipher.update()` after [`cipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#cipherfinaloutputencoding) will result in an error being thrown.
### Class: `Decipheriv`[#](https://nodejs.org/docs/latest/api/crypto.html#class-decipheriv)
Added in: v0.1.94
  * Extends: [`<stream.Transform>`](https://nodejs.org/docs/latest/api/stream.html#class-streamtransform)


Instances of the `Decipheriv` class are used to decrypt data. The class can be used in one of two ways:
  * As a [stream](https://nodejs.org/docs/latest/api/stream.html) that is both readable and writable, where plain encrypted data is written to produce unencrypted data on the readable side, or
  * Using the [`decipher.update()`](https://nodejs.org/docs/latest/api/crypto.html#decipherupdatedata-inputencoding-outputencoding) and [`decipher.final()`](https://nodejs.org/docs/latest/api/crypto.html#decipherfinaloutputencoding) methods to produce the unencrypted data.


The [`crypto.createDecipheriv()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatedecipherivalgorithm-key-iv-options) method is used to create `Decipheriv` instances. `Decipheriv` objects are not to be created directly using the `new` keyword.
