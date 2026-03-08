####  `keyObject.symmetricKeySize`[#](https://nodejs.org/docs/latest/api/crypto.html#keyobjectsymmetrickeysize)
Added in: v11.6.0
  * Type:


For secret keys, this property represents the size of the key in bytes. This property is `undefined` for asymmetric keys.
####  `keyObject.toCryptoKey(algorithm, extractable, keyUsages)`[#](https://nodejs.org/docs/latest/api/crypto.html#keyobjecttocryptokeyalgorithm-extractable-keyusages)
Added in: v23.0.0, v22.10.0
  * `algorithm` [`<Algorithm>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-algorithm) | [`<RsaHashedImportParams>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-rsahashedimportparams) | [`<EcKeyImportParams>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-eckeyimportparams) | [`<HmacImportParams>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-hmacimportparams)


  * `extractable`
  * `keyUsages` [Key usages](https://nodejs.org/docs/latest/api/webcrypto.html#cryptokeyusages).
  * Returns: [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)


Converts a `KeyObject` instance to a `CryptoKey`.
####  `keyObject.type`[#](https://nodejs.org/docs/latest/api/crypto.html#keyobjecttype)
Added in: v11.6.0
  * Type:


Depending on the type of this `KeyObject`, this property is either `'secret'` for secret (symmetric) keys, `'public'` for public (asymmetric) keys or `'private'` for private (asymmetric) keys.
### Class: `Sign`[#](https://nodejs.org/docs/latest/api/crypto.html#class-sign)
Added in: v0.1.92
  * Extends: [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable)


The `Sign` class is a utility for generating signatures. It can be used in one of two ways:
  * As a writable [stream](https://nodejs.org/docs/latest/api/stream.html), where data to be signed is written and the [`sign.sign()`](https://nodejs.org/docs/latest/api/crypto.html#signsignprivatekey-outputencoding) method is used to generate and return the signature, or
  * Using the [`sign.update()`](https://nodejs.org/docs/latest/api/crypto.html#signupdatedata-inputencoding) and [`sign.sign()`](https://nodejs.org/docs/latest/api/crypto.html#signsignprivatekey-outputencoding) methods to produce the signature.


The [`crypto.createSign()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatesignalgorithm-options) method is used to create `Sign` instances. The argument is the string name of the hash function to use. `Sign` objects are not to be created directly using the `new` keyword.
Example: Using `Sign` and [`Verify`](https://nodejs.org/docs/latest/api/crypto.html#class-verify) objects as streams:
```
const {
  generateKeyPairSync,
  createSign,
  createVerify,
} = await import('node:crypto');

const { privateKey, publicKey } = generateKeyPairSync('ec', {
  namedCurve: 'sect239k1',
});

const sign = createSign('SHA256');
sign.write('some data to sign');
sign.end();
const signature = sign.sign(privateKey, 'hex');

const verify = createVerify('SHA256');
verify.write('some data to sign');
verify.end();
console.log(verify.verify(publicKey, signature, 'hex'));
// Prints: true
const {
  generateKeyPairSync,
  createSign,
  createVerify,
} = require('node:crypto');

const { privateKey, publicKey } = generateKeyPairSync('ec', {
  namedCurve: 'sect239k1',
});

const sign = createSign('SHA256');
sign.write('some data to sign');
sign.end();
const signature = sign.sign(privateKey, 'hex');

const verify = createVerify('SHA256');
verify.write('some data to sign');
verify.end();
console.log(verify.verify(publicKey, signature, 'hex'));
// Prints: true
copy
```

Example: Using the [`sign.update()`](https://nodejs.org/docs/latest/api/crypto.html#signupdatedata-inputencoding) and [`verify.update()`](https://nodejs.org/docs/latest/api/crypto.html#verifyupdatedata-inputencoding) methods:
```
const {
  generateKeyPairSync,
  createSign,
  createVerify,
} = await import('node:crypto');

const { privateKey, publicKey } = generateKeyPairSync('rsa', {
  modulusLength: 2048,
});

const sign = createSign('SHA256');
sign.update('some data to sign');
sign.end();
const signature = sign.sign(privateKey);

const verify = createVerify('SHA256');
verify.update('some data to sign');
verify.end();
console.log(verify.verify(publicKey, signature));
// Prints: true
const {
  generateKeyPairSync,
  createSign,
  createVerify,
} = require('node:crypto');

const { privateKey, publicKey } = generateKeyPairSync('rsa', {
  modulusLength: 2048,
});

const sign = createSign('SHA256');
sign.update('some data to sign');
sign.end();
const signature = sign.sign(privateKey);

const verify = createVerify('SHA256');
verify.update('some data to sign');
verify.end();
console.log(verify.verify(publicKey, signature));
// Prints: true
copy
```

####  `sign.sign(privateKey[, outputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#signsignprivatekey-outputencoding)
Added in: v0.1.92History Version | Changes
---|---
v15.0.0 | The privateKey can also be an ArrayBuffer and CryptoKey.
v13.2.0, v12.16.0 | This function now supports IEEE-P1363 DSA and ECDSA signatures.
v12.0.0 | This function now supports RSA-PSS keys.
v11.6.0 | This function now supports key objects.
v8.0.0 | Support for RSASSA-PSS and additional options was added.
  * `privateKey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)
    * `dsaEncoding`
    * `padding`
    * `saltLength`
  * `outputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the return value.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Calculates the signature on all the data passed through using either [`sign.update()`](https://nodejs.org/docs/latest/api/crypto.html#signupdatedata-inputencoding) or [`sign.write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback).
If `privateKey` is not a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject), this function behaves as if `privateKey` had been passed to [`crypto.createPrivateKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateprivatekeykey). If it is an object, the following additional properties can be passed:
  * `dsaEncoding`
    * `'der'` (default): DER-encoded ASN.1 signature structure encoding `(r, s)`.
    * `'ieee-p1363'`: Signature format `r || s` as proposed in IEEE-P1363.
  * `padding`
    * `crypto.constants.RSA_PKCS1_PADDING` (default)
    * `crypto.constants.RSA_PKCS1_PSS_PADDING`
`RSA_PKCS1_PSS_PADDING` will use MGF1 with the same hash function used to sign the message as specified in section 3.1 of
  * `saltLength` `RSA_PKCS1_PSS_PADDING`. The special value `crypto.constants.RSA_PSS_SALTLEN_DIGEST` sets the salt length to the digest size, `crypto.constants.RSA_PSS_SALTLEN_MAX_SIGN` (default) sets it to the maximum permissible value.


If `outputEncoding` is provided a string is returned; otherwise a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html) is returned.
The `Sign` object can not be again used after `sign.sign()` method has been called. Multiple calls to `sign.sign()` will result in an error being thrown.
####  `sign.update(data[, inputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#signupdatedata-inputencoding)
Added in: v0.1.92History Version | Changes
---|---
v6.0.0 | The default `inputEncoding` changed from `binary` to `utf8`.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `inputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `data` string.


Updates the `Sign` content with the given `data`, the encoding of which is given in `inputEncoding`. If `encoding` is not provided, and the `data` is a string, an encoding of `'utf8'` is enforced. If `data` is a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`, then `inputEncoding` is ignored.
This can be called many times with new data as it is streamed.
### Class: `Verify`[#](https://nodejs.org/docs/latest/api/crypto.html#class-verify)
Added in: v0.1.92
  * Extends: [`<stream.Writable>`](https://nodejs.org/docs/latest/api/stream.html#class-streamwritable)


The `Verify` class is a utility for verifying signatures. It can be used in one of two ways:
  * As a writable [stream](https://nodejs.org/docs/latest/api/stream.html) where written data is used to validate against the supplied signature, or
  * Using the [`verify.update()`](https://nodejs.org/docs/latest/api/crypto.html#verifyupdatedata-inputencoding) and [`verify.verify()`](https://nodejs.org/docs/latest/api/crypto.html#verifyverifyobject-signature-signatureencoding) methods to verify the signature.


The [`crypto.createVerify()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreateverifyalgorithm-options) method is used to create `Verify` instances. `Verify` objects are not to be created directly using the `new` keyword.
See [`Sign`](https://nodejs.org/docs/latest/api/crypto.html#class-sign) for examples.
####  `verify.update(data[, inputEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#verifyupdatedata-inputencoding)
Added in: v0.1.92History Version | Changes
---|---
v6.0.0 | The default `inputEncoding` changed from `binary` to `utf8`.
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `inputEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `data` string.


Updates the `Verify` content with the given `data`, the encoding of which is given in `inputEncoding`. If `inputEncoding` is not provided, and the `data` is a string, an encoding of `'utf8'` is enforced. If `data` is a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`, then `inputEncoding` is ignored.
This can be called many times with new data as it is streamed.
####  `verify.verify(object, signature[, signatureEncoding])`[#](https://nodejs.org/docs/latest/api/crypto.html#verifyverifyobject-signature-signatureencoding)
Added in: v0.1.92History Version | Changes
---|---
v15.0.0 | The object can also be an ArrayBuffer and CryptoKey.
v13.2.0, v12.16.0 | This function now supports IEEE-P1363 DSA and ECDSA signatures.
v12.0.0 | This function now supports RSA-PSS keys.
v11.7.0 | The key can now be a private key.
v8.0.0 | Support for RSASSA-PSS and additional options was added.
  * `object` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) | [`<CryptoKey>`](https://nodejs.org/docs/latest/api/webcrypto.html#class-cryptokey)
    * `dsaEncoding`
    * `padding`
    * `saltLength`
  * `signature` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `signatureEncoding` [encoding](https://nodejs.org/docs/latest/api/buffer.html#buffers-and-character-encodings) of the `signature` string.
  * Returns: `true` or `false` depending on the validity of the signature for the data and public key.


Verifies the provided data using the given `object` and `signature`.
If `object` is not a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject), this function behaves as if `object` had been passed to [`crypto.createPublicKey()`](https://nodejs.org/docs/latest/api/crypto.html#cryptocreatepublickeykey). If it is an object, the following additional properties can be passed:
  * `dsaEncoding`
    * `'der'` (default): DER-encoded ASN.1 signature structure encoding `(r, s)`.
    * `'ieee-p1363'`: Signature format `r || s` as proposed in IEEE-P1363.
  * `padding`
    * `crypto.constants.RSA_PKCS1_PADDING` (default)
    * `crypto.constants.RSA_PKCS1_PSS_PADDING`
`RSA_PKCS1_PSS_PADDING` will use MGF1 with the same hash function used to verify the message as specified in section 3.1 of
  * `saltLength` `RSA_PKCS1_PSS_PADDING`. The special value `crypto.constants.RSA_PSS_SALTLEN_DIGEST` sets the salt length to the digest size, `crypto.constants.RSA_PSS_SALTLEN_AUTO` (default) causes it to be determined automatically.


The `signature` argument is the previously calculated signature for the data, in the `signatureEncoding`. If a `signatureEncoding` is specified, the `signature` is expected to be a string; otherwise `signature` is expected to be a [`Buffer`](https://nodejs.org/docs/latest/api/buffer.html), `TypedArray`, or `DataView`.
The `verify` object can not be used again after `verify.verify()` has been called. Multiple calls to `verify.verify()` will result in an error being thrown.
Because public keys can be derived from private keys, a private key may be passed instead of a public key.
### Class: `X509Certificate`[#](https://nodejs.org/docs/latest/api/crypto.html#class-x509certificate)
Added in: v15.6.0
Encapsulates an X509 certificate and provides read-only access to its information.
```
const { X509Certificate } = await import('node:crypto');

const x509 = new X509Certificate('{... pem encoded cert ...}');

console.log(x509.subject);
const { X509Certificate } = require('node:crypto');

const x509 = new X509Certificate('{... pem encoded cert ...}');

console.log(x509.subject);
copy
```

####  `new X509Certificate(buffer)`[#](https://nodejs.org/docs/latest/api/crypto.html#new-x509certificatebuffer)
Added in: v15.6.0
  * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


####  `x509.ca`[#](https://nodejs.org/docs/latest/api/crypto.html#x509ca)
Added in: v15.6.0
  * Type: `true` if this is a Certificate Authority (CA) certificate.


####  `x509.checkEmail(email[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#x509checkemailemail-options)
Added in: v15.6.0History Version | Changes
---|---
v18.0.0 | The subject option now defaults to `'default'`.
v17.5.0, v16.14.1 | The `wildcards`, `partialWildcards`, `multiLabelWildcards`, and `singleLabelSubdomains` options have been removed since they had no effect.
v17.5.0, v16.15.0 | The subject option can now be set to `'default'`.
  * `email`
  * `options`
    * `subject` `'default'`, `'always'`, or `'never'`. **Default:** `'default'`.
  * Returns: `email` if the certificate matches, `undefined` if it does not.


Checks whether the certificate matches the given email address.
If the `'subject'` option is undefined or set to `'default'`, the certificate subject is only considered if the subject alternative name extension either does not exist or does not contain any email addresses.
If the `'subject'` option is set to `'always'` and if the subject alternative name extension either does not exist or does not contain a matching email address, the certificate subject is considered.
If the `'subject'` option is set to `'never'`, the certificate subject is never considered, even if the certificate contains no subject alternative names.
####  `x509.checkHost(name[, options])`[#](https://nodejs.org/docs/latest/api/crypto.html#x509checkhostname-options)
Added in: v15.6.0History Version | Changes
---|---
v18.0.0 | The subject option now defaults to `'default'`.
v17.5.0, v16.15.0 | The subject option can now be set to `'default'`.
  * `name`
  * `options`
    * `subject` `'default'`, `'always'`, or `'never'`. **Default:** `'default'`.
    * `wildcards` **Default:** `true`.
    * `partialWildcards` **Default:** `true`.
    * `multiLabelWildcards` **Default:** `false`.
    * `singleLabelSubdomains` **Default:** `false`.
  * Returns: `name`, or `undefined` if no subject name matches `name`.


Checks whether the certificate matches the given host name.
If the certificate matches the given host name, the matching subject name is returned. The returned name might be an exact match (e.g., `foo.example.com`) or it might contain wildcards (e.g., `*.example.com`). Because host name comparisons are case-insensitive, the returned subject name might also differ from the given `name` in capitalization.
If the `'subject'` option is undefined or set to `'default'`, the certificate subject is only considered if the subject alternative name extension either does not exist or does not contain any DNS names. This behavior is consistent with
If the `'subject'` option is set to `'always'` and if the subject alternative name extension either does not exist or does not contain a matching DNS name, the certificate subject is considered.
If the `'subject'` option is set to `'never'`, the certificate subject is never considered, even if the certificate contains no subject alternative names.
####  `x509.checkIP(ip)`[#](https://nodejs.org/docs/latest/api/crypto.html#x509checkipip)
Added in: v15.6.0History Version | Changes
---|---
v17.5.0, v16.14.1 | The `options` argument has been removed since it had no effect.
  * `ip`
  * Returns: `ip` if the certificate matches, `undefined` if it does not.


Checks whether the certificate matches the given IP address (IPv4 or IPv6).
Only `iPAddress` subject alternative names are considered, and they must match the given `ip` address exactly. Other subject alternative names as well as the subject field of the certificate are ignored.
####  `x509.checkIssued(otherCert)`[#](https://nodejs.org/docs/latest/api/crypto.html#x509checkissuedothercert)
Added in: v15.6.0
  * `otherCert` [`<X509Certificate>`](https://nodejs.org/docs/latest/api/crypto.html#class-x509certificate)
  * Returns:


Checks whether this certificate was potentially issued by the given `otherCert` by comparing the certificate metadata.
This is useful for pruning a list of possible issuer certificates which have been selected using a more rudimentary filtering routine, i.e. just based on subject and issuer names.
Finally, to verify that this certificate's signature was produced by a private key corresponding to `otherCert`'s public key use [`x509.verify(publicKey)`](https://nodejs.org/docs/latest/api/crypto.html#x509verifypublickey) with `otherCert`'s public key represented as a [`KeyObject`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) like so
```
if (!x509.verify(otherCert.publicKey)) {
  throw new Error('otherCert did not issue x509');
}
copy
```

####  `x509.checkPrivateKey(privateKey)`[#](https://nodejs.org/docs/latest/api/crypto.html#x509checkprivatekeyprivatekey)
Added in: v15.6.0
  * `privateKey` [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) A private key.
  * Returns:


Checks whether the public key for this certificate is consistent with the given private key.
####  `x509.fingerprint`[#](https://nodejs.org/docs/latest/api/crypto.html#x509fingerprint)
Added in: v15.6.0
  * Type:


The SHA-1 fingerprint of this certificate.
Because SHA-1 is cryptographically broken and because the security of SHA-1 is significantly worse than that of algorithms that are commonly used to sign certificates, consider using [`x509.fingerprint256`](https://nodejs.org/docs/latest/api/crypto.html#x509fingerprint256) instead.
####  `x509.fingerprint256`[#](https://nodejs.org/docs/latest/api/crypto.html#x509fingerprint256)
Added in: v15.6.0
  * Type:


The SHA-256 fingerprint of this certificate.
####  `x509.fingerprint512`[#](https://nodejs.org/docs/latest/api/crypto.html#x509fingerprint512)
Added in: v17.2.0, v16.14.0
  * Type:


The SHA-512 fingerprint of this certificate.
Because computing the SHA-256 fingerprint is usually faster and because it is only half the size of the SHA-512 fingerprint, [`x509.fingerprint256`](https://nodejs.org/docs/latest/api/crypto.html#x509fingerprint256) may be a better choice. While SHA-512 presumably provides a higher level of security in general, the security of SHA-256 matches that of most algorithms that are commonly used to sign certificates.
####  `x509.infoAccess`[#](https://nodejs.org/docs/latest/api/crypto.html#x509infoaccess)
Added in: v15.6.0History Version | Changes
---|---
v17.3.1, v16.13.2 | Parts of this string may be encoded as JSON string literals in response to CVE-2021-44532.
  * Type:


A textual representation of the certificate's authority information access extension.
This is a line feed separated list of access descriptions. Each line begins with the access method and the kind of the access location, followed by a colon and the value associated with the access location.
After the prefix denoting the access method and the kind of the access location, the remainder of each line might be enclosed in quotes to indicate that the value is a JSON string literal. For backward compatibility, Node.js only uses JSON string literals within this property when necessary to avoid ambiguity. Third-party code should be prepared to handle both possible entry formats.
####  `x509.issuer`[#](https://nodejs.org/docs/latest/api/crypto.html#x509issuer)
Added in: v15.6.0
  * Type:


The issuer identification included in this certificate.
####  `x509.issuerCertificate`[#](https://nodejs.org/docs/latest/api/crypto.html#x509issuercertificate)
Added in: v15.9.0
  * Type: [`<X509Certificate>`](https://nodejs.org/docs/latest/api/crypto.html#class-x509certificate)


The issuer certificate or `undefined` if the issuer certificate is not available.
####  `x509.keyUsage`[#](https://nodejs.org/docs/latest/api/crypto.html#x509keyusage)
Added in: v15.6.0
  * Type:


An array detailing the key extended usages for this certificate.
####  `x509.publicKey`[#](https://nodejs.org/docs/latest/api/crypto.html#x509publickey)
Added in: v15.6.0
  * Type: [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject)


The public key [`<KeyObject>`](https://nodejs.org/docs/latest/api/crypto.html#class-keyobject) for this certificate.
####  `x509.raw`[#](https://nodejs.org/docs/latest/api/crypto.html#x509raw)
Added in: v15.6.0
  * Type: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


A `Buffer` containing the DER encoding of this certificate.
####  `x509.serialNumber`[#](https://nodejs.org/docs/latest/api/crypto.html#x509serialnumber)
Added in: v15.6.0
  * Type:


The serial number of this certificate.
Serial numbers are assigned by certificate authorities and do not uniquely identify certificates. Consider using [`x509.fingerprint256`](https://nodejs.org/docs/latest/api/crypto.html#x509fingerprint256) as a unique identifier instead.
####  `x509.subject`[#](https://nodejs.org/docs/latest/api/crypto.html#x509subject)
Added in: v15.6.0
  * Type:


The complete subject of this certificate.
####  `x509.subjectAltName`[#](https://nodejs.org/docs/latest/api/crypto.html#x509subjectaltname)
Added in: v15.6.0History Version | Changes
---|---
v17.3.1, v16.13.2 | Parts of this string may be encoded as JSON string literals in response to CVE-2021-44532.
  * Type:


The subject alternative name specified for this certificate.
This is a comma-separated list of subject alternative names. Each entry begins with a string identifying the kind of the subject alternative name followed by a colon and the value associated with the entry.
Earlier versions of Node.js incorrectly assumed that it is safe to split this property at the two-character sequence `', '` (see
After the prefix denoting the type of the entry, the remainder of each entry might be enclosed in quotes to indicate that the value is a JSON string literal. For backward compatibility, Node.js only uses JSON string literals within this property when necessary to avoid ambiguity. Third-party code should be prepared to handle both possible entry formats.
####  `x509.toJSON()`[#](https://nodejs.org/docs/latest/api/crypto.html#x509tojson)
Added in: v15.6.0
  * Type:


There is no standard JSON encoding for X509 certificates. The `toJSON()` method returns a string containing the PEM encoded certificate.
####  `x509.toLegacyObject()`[#](https://nodejs.org/docs/latest/api/crypto.html#x509tolegacyobject)
Added in: v15.6.0
  * Type:


Returns information about this certificate using the legacy [certificate object](https://nodejs.org/docs/latest/api/tls.html#certificate-object) encoding.
####  `x509.toString()`[#](https://nodejs.org/docs/latest/api/crypto.html#x509tostring)
Added in: v15.6.0
  * Type:


Returns the PEM-encoded certificate.
####  `x509.validFrom`[#](https://nodejs.org/docs/latest/api/crypto.html#x509validfrom)
Added in: v15.6.0
  * Type:


The date/time from which this certificate is valid.
####  `x509.validFromDate`[#](https://nodejs.org/docs/latest/api/crypto.html#x509validfromdate)
Added in: v23.0.0, v22.10.0
  * Type:


The date/time from which this certificate is valid, encapsulated in a `Date` object.
####  `x509.validTo`[#](https://nodejs.org/docs/latest/api/crypto.html#x509validto)
Added in: v15.6.0
  * Type:


The date/time until which this certificate is valid.
####  `x509.validToDate`[#](https://nodejs.org/docs/latest/api/crypto.html#x509validtodate)
Added in: v23.0.0, v22.10.0
  * Type:


The date/time until which this certificate is valid, encapsulated in a `Date` object.
####  `x509.signatureAlgorithm`[#](https://nodejs.org/docs/latest/api/crypto.html#x509signaturealgorithm)
Added in: v24.9.0
  * Type:


The algorithm used to sign the certificate or `undefined` if the signature algorithm is unknown by OpenSSL.
####  `x509.signatureAlgorithmOid`[#](https://nodejs.org/docs/latest/api/crypto.html#x509signaturealgorithmoid)
