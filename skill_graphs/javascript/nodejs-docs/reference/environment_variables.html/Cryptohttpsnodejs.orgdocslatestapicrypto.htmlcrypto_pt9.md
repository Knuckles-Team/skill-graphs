####  `crypto.webcrypto`[#](https://nodejs.org/docs/latest/api/crypto.html#cryptowebcrypto)
Added in: v15.0.0
Type: [`<Crypto>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-crypto) An implementation of the Web Crypto API standard.
See the [Web Crypto API documentation](https://nodejs.org/docs/latest/api/webcrypto.html) for details.
### Notes[#](https://nodejs.org/docs/latest/api/crypto.html#notes)
#### Using strings as inputs to cryptographic APIs[#](https://nodejs.org/docs/latest/api/crypto.html#using-strings-as-inputs-to-cryptographic-apis)
For historical reasons, many cryptographic APIs provided by Node.js accept strings as inputs where the underlying cryptographic algorithm works on byte sequences. These instances include plaintexts, ciphertexts, symmetric keys, initialization vectors, passphrases, salts, authentication tags, and additional authenticated data.
When passing strings to cryptographic APIs, consider the following factors.
  * Not all byte sequences are valid UTF-8 strings. Therefore, when a byte sequence of length `n` is derived from a string, its entropy is generally lower than the entropy of a random or pseudorandom `n` byte sequence. For example, no UTF-8 string will result in the byte sequence `c0 af`. Secret keys should almost exclusively be random or pseudorandom byte sequences.
  * Similarly, when converting random or pseudorandom byte sequences to UTF-8 strings, subsequences that do not represent valid code points may be replaced by the Unicode replacement character (`U+FFFD`). The byte representation of the resulting Unicode string may, therefore, not be equal to the byte sequence that the string was created from.
```
const original = [0xc0, 0xaf];
const bytesAsString = Buffer.from(original).toString('utf8');
const stringAsBytes = Buffer.from(bytesAsString, 'utf8');
console.log(stringAsBytes);
// Prints '<Buffer ef bf bd ef bf bd>'.
copy
```

The outputs of ciphers, hash functions, signature algorithms, and key derivation functions are pseudorandom byte sequences and should not be used as Unicode strings.
  * When strings are obtained from user input, some Unicode characters can be represented in multiple equivalent ways that result in different byte sequences. For example, when passing a user passphrase to a key derivation function, such as PBKDF2 or scrypt, the result of the key derivation function depends on whether the string uses composed or decomposed characters. Node.js does not normalize character representations. Developers should consider using


#### Legacy streams API (prior to Node.js 0.10)[#](https://nodejs.org/docs/latest/api/crypto.html#legacy-streams-api-prior-to-nodejs-010)
The Crypto module was added to Node.js before there was the concept of a unified Stream API, and before there were [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) objects for handling binary data. As such, many `crypto` classes have methods not typically found on other Node.js classes that implement the [streams](https://nodejs.org/docs/latest/api/stream.html) API (e.g. `update()`, `final()`, or `digest()`). Also, many methods accepted and returned `'latin1'` encoded strings by default rather than `Buffer`s. This default was changed in Node.js 0.9.3 to use [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) objects by default instead.
#### Support for weak or compromised algorithms[#](https://nodejs.org/docs/latest/api/crypto.html#support-for-weak-or-compromised-algorithms)
The `node:crypto` module still supports some algorithms which are already compromised and are not recommended for use. The API also allows the use of ciphers and hashes with a small key size that are too weak for safe use.
Users should take full responsibility for selecting the crypto algorithm and key size according to their security requirements.
Based on the recommendations of
  * MD5 and SHA-1 are no longer acceptable where collision resistance is required such as digital signatures.
  * The key used with RSA, DSA, and DH algorithms is recommended to have at least 2048 bits and that of the curve of ECDSA and ECDH at least 224 bits, to be safe to use for several years.
  * The DH groups of `modp1`, `modp2` and `modp5` have a key size smaller than 2048 bits and are not recommended.


See the reference for other recommendations and details.
Some algorithms that have known weaknesses and are of little relevance in practice are only available through the [legacy provider](https://nodejs.org/docs/latest/api/cli.html#--openssl-legacy-provider), which is not enabled by default.
#### CCM mode[#](https://nodejs.org/docs/latest/api/crypto.html#ccm-mode)
CCM is one of the supported
  * The authentication tag length must be specified during cipher creation by setting the `authTagLength` option and must be one of 4, 6, 8, 10, 12, 14 or 16 bytes.
  * The length of the initialization vector (nonce) `N` must be between 7 and 13 bytes (`7 ≤ N ≤ 13`).
  * The length of the plaintext is limited to `2 ** (8 * (15 - N))` bytes.
  * When decrypting, the authentication tag must be set via `setAuthTag()` before calling `update()`. Otherwise, decryption will fail and `final()` will throw an error in compliance with section 2.6 of
  * Using stream methods such as `write(data)`, `end(data)` or `pipe()` in CCM mode might fail as CCM cannot handle more than one chunk of data per instance.
  * When passing additional authenticated data (AAD), the length of the actual message in bytes must be passed to `setAAD()` via the `plaintextLength` option. Many crypto libraries include the authentication tag in the ciphertext, which means that they produce ciphertexts of the length `plaintextLength + authTagLength`. Node.js does not include the authentication tag, so the ciphertext length is always `plaintextLength`. This is not necessary if no AAD is used.
  * As CCM processes the whole message at once, `update()` must be called exactly once.
  * Even though calling `update()` is sufficient to encrypt/decrypt the message, applications _must_ call `final()` to compute or verify the authentication tag.

```
import { Buffer } from 'node:buffer';
const {
  createCipheriv,
  createDecipheriv,
  randomBytes,
} = await import('node:crypto');

const key = 'keykeykeykeykeykeykeykey';
const nonce = randomBytes(12);

const aad = Buffer.from('0123456789', 'hex');

const cipher = createCipheriv('aes-192-ccm', key, nonce, {
  authTagLength: 16,
});
const plaintext = 'Hello world';
cipher.setAAD(aad, {
  plaintextLength: Buffer.byteLength(plaintext),
});
const ciphertext = cipher.update(plaintext, 'utf8');
cipher.final();
const tag = cipher.getAuthTag();

// Now transmit { ciphertext, nonce, tag }.

const decipher = createDecipheriv('aes-192-ccm', key, nonce, {
  authTagLength: 16,
});
decipher.setAuthTag(tag);
decipher.setAAD(aad, {
  plaintextLength: ciphertext.length,
});
const receivedPlaintext = decipher.update(ciphertext, null, 'utf8');

try {
  decipher.final();
} catch (err) {
  throw new Error('Authentication failed!', { cause: err });
}

console.log(receivedPlaintext);
const { Buffer } = require('node:buffer');
const {
  createCipheriv,
  createDecipheriv,
  randomBytes,
} = require('node:crypto');

const key = 'keykeykeykeykeykeykeykey';
const nonce = randomBytes(12);

const aad = Buffer.from('0123456789', 'hex');

const cipher = createCipheriv('aes-192-ccm', key, nonce, {
  authTagLength: 16,
});
const plaintext = 'Hello world';
cipher.setAAD(aad, {
  plaintextLength: Buffer.byteLength(plaintext),
});
const ciphertext = cipher.update(plaintext, 'utf8');
cipher.final();
const tag = cipher.getAuthTag();

// Now transmit { ciphertext, nonce, tag }.

const decipher = createDecipheriv('aes-192-ccm', key, nonce, {
  authTagLength: 16,
});
decipher.setAuthTag(tag);
decipher.setAAD(aad, {
  plaintextLength: ciphertext.length,
});
const receivedPlaintext = decipher.update(ciphertext, null, 'utf8');

try {
  decipher.final();
} catch (err) {
  throw new Error('Authentication failed!', { cause: err });
}

console.log(receivedPlaintext);
copy
```

#### FIPS mode[#](https://nodejs.org/docs/latest/api/crypto.html#fips-mode)
When using OpenSSL 3, Node.js supports FIPS 140-2 when used with an appropriate OpenSSL 3 provider, such as the
For FIPS support in Node.js you will need:
  * A correctly installed OpenSSL 3 FIPS provider.
  * An OpenSSL 3
  * An OpenSSL 3 configuration file that references the FIPS module configuration file.


Node.js will need to be configured with an OpenSSL configuration file that points to the FIPS provider. An example configuration file looks like this:
```
nodejs_conf = nodejs_init

.include /<absolute path>/fipsmodule.cnf

[nodejs_init]
providers = provider_sect

[provider_sect]
default = default_sect
# The fips section name should match the section name inside the
# included fipsmodule.cnf.
fips = fips_sect

[default_sect]
activate = 1
copy
```

where `fipsmodule.cnf` is the FIPS module configuration file generated from the FIPS provider installation step:
```
openssl fipsinstall
copy
```

Set the `OPENSSL_CONF` environment variable to point to your configuration file and `OPENSSL_MODULES` to the location of the FIPS provider dynamic library. e.g.
```
export OPENSSL_CONF=/<path to configuration file>/nodejs.cnf
export OPENSSL_MODULES=/<path to openssl lib>/ossl-modules
copy
```

FIPS mode can then be enabled in Node.js either by:
  * Starting Node.js with `--enable-fips` or `--force-fips` command line flags.
  * Programmatically calling `crypto.setFips(true)`.


Optionally FIPS mode can be enabled in Node.js via the OpenSSL configuration file. e.g.
```
nodejs_conf = nodejs_init

.include /<absolute path>/fipsmodule.cnf

[nodejs_init]
providers = provider_sect
alg_section = algorithm_sect

[provider_sect]
default = default_sect
# The fips section name should match the section name inside the
# included fipsmodule.cnf.
fips = fips_sect

[default_sect]
activate = 1

[algorithm_sect]
default_properties = fips=yes
copy
```

### Crypto constants[#](https://nodejs.org/docs/latest/api/crypto.html#crypto-constants)
The following constants exported by `crypto.constants` apply to various uses of the `node:crypto`, `node:tls`, and `node:https` modules and are generally specific to OpenSSL.
#### OpenSSL options[#](https://nodejs.org/docs/latest/api/crypto.html#openssl-options)
See the
Constant | Description
---|---
`SSL_OP_ALL` | Applies multiple bug workarounds within OpenSSL. See
`SSL_OP_ALLOW_NO_DHE_KEX` | Instructs OpenSSL to allow a non-[EC]DHE-based key exchange mode for TLS v1.3
`SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION` | Allows legacy insecure renegotiation between OpenSSL and unpatched clients or servers. See
`SSL_OP_CIPHER_SERVER_PREFERENCE` | Attempts to use the server's preferences instead of the client's when selecting a cipher. Behavior depends on protocol version. See
`SSL_OP_CISCO_ANYCONNECT` | Instructs OpenSSL to use Cisco's version identifier of DTLS_BAD_VER.
`SSL_OP_COOKIE_EXCHANGE` | Instructs OpenSSL to turn on cookie exchange.
`SSL_OP_CRYPTOPRO_TLSEXT_BUG` | Instructs OpenSSL to add server-hello extension from an early version of the cryptopro draft.
`SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS` | Instructs OpenSSL to disable a SSL 3.0/TLS 1.0 vulnerability workaround added in OpenSSL 0.9.6d.
`SSL_OP_LEGACY_SERVER_CONNECT` | Allows initial connection to servers that do not support RI.
`SSL_OP_NO_COMPRESSION` | Instructs OpenSSL to disable support for SSL/TLS compression.
`SSL_OP_NO_ENCRYPT_THEN_MAC` | Instructs OpenSSL to disable encrypt-then-MAC.
`SSL_OP_NO_QUERY_MTU` |
`SSL_OP_NO_RENEGOTIATION` | Instructs OpenSSL to disable renegotiation.
`SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION` | Instructs OpenSSL to always start a new session when performing renegotiation.
`SSL_OP_NO_SSLv2` | Instructs OpenSSL to turn off SSL v2
`SSL_OP_NO_SSLv3` | Instructs OpenSSL to turn off SSL v3
`SSL_OP_NO_TICKET` | Instructs OpenSSL to disable use of RFC4507bis tickets.
`SSL_OP_NO_TLSv1` | Instructs OpenSSL to turn off TLS v1
`SSL_OP_NO_TLSv1_1` | Instructs OpenSSL to turn off TLS v1.1
`SSL_OP_NO_TLSv1_2` | Instructs OpenSSL to turn off TLS v1.2
`SSL_OP_NO_TLSv1_3` | Instructs OpenSSL to turn off TLS v1.3
`SSL_OP_PRIORITIZE_CHACHA` | Instructs OpenSSL server to prioritize ChaCha20-Poly1305 when the client does. This option has no effect if `SSL_OP_CIPHER_SERVER_PREFERENCE` is not enabled.
`SSL_OP_TLS_ROLLBACK_BUG` | Instructs OpenSSL to disable version rollback attack detection.
#### OpenSSL engine constants[#](https://nodejs.org/docs/latest/api/crypto.html#openssl-engine-constants)
Constant | Description
---|---
`ENGINE_METHOD_RSA` | Limit engine usage to RSA
`ENGINE_METHOD_DSA` | Limit engine usage to DSA
`ENGINE_METHOD_DH` | Limit engine usage to DH
`ENGINE_METHOD_RAND` | Limit engine usage to RAND
`ENGINE_METHOD_EC` | Limit engine usage to EC
`ENGINE_METHOD_CIPHERS` | Limit engine usage to CIPHERS
`ENGINE_METHOD_DIGESTS` | Limit engine usage to DIGESTS
`ENGINE_METHOD_PKEY_METHS` | Limit engine usage to PKEY_METHS
`ENGINE_METHOD_PKEY_ASN1_METHS` | Limit engine usage to PKEY_ASN1_METHS
`ENGINE_METHOD_ALL` |
`ENGINE_METHOD_NONE` |
#### Other OpenSSL constants[#](https://nodejs.org/docs/latest/api/crypto.html#other-openssl-constants)
Constant | Description
---|---
`DH_CHECK_P_NOT_SAFE_PRIME` |
`DH_CHECK_P_NOT_PRIME` |
`DH_UNABLE_TO_CHECK_GENERATOR` |
`DH_NOT_SUITABLE_GENERATOR` |
`RSA_PKCS1_PADDING` |
`RSA_SSLV23_PADDING` |
`RSA_NO_PADDING` |
`RSA_PKCS1_OAEP_PADDING` |
`RSA_X931_PADDING` |
`RSA_PKCS1_PSS_PADDING` |
`RSA_PSS_SALTLEN_DIGEST` | Sets the salt length for `RSA_PKCS1_PSS_PADDING` to the digest size when signing or verifying.
`RSA_PSS_SALTLEN_MAX_SIGN` | Sets the salt length for `RSA_PKCS1_PSS_PADDING` to the maximum permissible value when signing data.
`RSA_PSS_SALTLEN_AUTO` | Causes the salt length for `RSA_PKCS1_PSS_PADDING` to be determined automatically when verifying a signature.
`POINT_CONVERSION_COMPRESSED` |
`POINT_CONVERSION_UNCOMPRESSED` |
`POINT_CONVERSION_HYBRID` |
#### Node.js crypto constants[#](https://nodejs.org/docs/latest/api/crypto.html#nodejs-crypto-constants)
Constant | Description
---|---
`defaultCoreCipherList` | Specifies the built-in default cipher list used by Node.js.
`defaultCipherList` | Specifies the active default cipher list used by the current Node.js process.
