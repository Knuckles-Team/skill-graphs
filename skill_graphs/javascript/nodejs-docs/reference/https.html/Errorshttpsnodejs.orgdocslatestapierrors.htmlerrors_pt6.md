#####  `CERT_HAS_EXPIRED`[#](https://nodejs.org/docs/latest/api/errors.html#cert-has-expired)
The certificate has expired: the notAfter date is before the current time.
#####  `CRL_NOT_YET_VALID`[#](https://nodejs.org/docs/latest/api/errors.html#crl-not-yet-valid)
The certificate revocation list (CRL) has a future issue date.
#####  `CRL_HAS_EXPIRED`[#](https://nodejs.org/docs/latest/api/errors.html#crl-has-expired)
The certificate revocation list (CRL) has expired.
#####  `CERT_REVOKED`[#](https://nodejs.org/docs/latest/api/errors.html#cert-revoked)
The certificate has been revoked; it is on a certificate revocation list (CRL).
#### Trust or Chain Related Errors[#](https://nodejs.org/docs/latest/api/errors.html#trust-or-chain-related-errors)
#####  `UNABLE_TO_GET_ISSUER_CERT`[#](https://nodejs.org/docs/latest/api/errors.html#unable-to-get-issuer-cert)
The issuer certificate of a looked up certificate could not be found. This normally means the list of trusted certificates is not complete.
#####  `UNABLE_TO_GET_ISSUER_CERT_LOCALLY`[#](https://nodejs.org/docs/latest/api/errors.html#unable-to-get-issuer-cert-locally)
The certificate’s issuer is not known. This is the case if the issuer is not included in the trusted certificate list.
#####  `DEPTH_ZERO_SELF_SIGNED_CERT`[#](https://nodejs.org/docs/latest/api/errors.html#depth-zero-self-signed-cert)
The passed certificate is self-signed and the same certificate cannot be found in the list of trusted certificates.
#####  `SELF_SIGNED_CERT_IN_CHAIN`[#](https://nodejs.org/docs/latest/api/errors.html#self-signed-cert-in-chain)
The certificate’s issuer is not known. This is the case if the issuer is not included in the trusted certificate list.
#####  `CERT_CHAIN_TOO_LONG`[#](https://nodejs.org/docs/latest/api/errors.html#cert-chain-too-long)
The certificate chain length is greater than the maximum depth.
#####  `UNABLE_TO_GET_CRL`[#](https://nodejs.org/docs/latest/api/errors.html#unable-to-get-crl)
The CRL reference by the certificate could not be found.
#####  `UNABLE_TO_VERIFY_LEAF_SIGNATURE`[#](https://nodejs.org/docs/latest/api/errors.html#unable-to-verify-leaf-signature)
No signatures could be verified because the chain contains only one certificate and it is not self signed.
#####  `CERT_UNTRUSTED`[#](https://nodejs.org/docs/latest/api/errors.html#cert-untrusted)
The root certificate authority (CA) is not marked as trusted for the specified purpose.
#### Basic Extension Errors[#](https://nodejs.org/docs/latest/api/errors.html#basic-extension-errors)
#####  `INVALID_CA`[#](https://nodejs.org/docs/latest/api/errors.html#invalid-ca)
A CA certificate is invalid. Either it is not a CA or its extensions are not consistent with the supplied purpose.
#####  `PATH_LENGTH_EXCEEDED`[#](https://nodejs.org/docs/latest/api/errors.html#path-length-exceeded)
The basicConstraints pathlength parameter has been exceeded.
#### Name Related Errors[#](https://nodejs.org/docs/latest/api/errors.html#name-related-errors)
#####  `HOSTNAME_MISMATCH`[#](https://nodejs.org/docs/latest/api/errors.html#hostname-mismatch)
Certificate does not match provided name.
#### Usage and Policy Errors[#](https://nodejs.org/docs/latest/api/errors.html#usage-and-policy-errors)
#####  `INVALID_PURPOSE`[#](https://nodejs.org/docs/latest/api/errors.html#invalid-purpose)
The supplied certificate cannot be used for the specified purpose.
#####  `CERT_REJECTED`[#](https://nodejs.org/docs/latest/api/errors.html#cert-rejected)
The root CA is marked to reject the specified purpose.
#### Formatting Errors[#](https://nodejs.org/docs/latest/api/errors.html#formatting-errors)
#####  `CERT_SIGNATURE_FAILURE`[#](https://nodejs.org/docs/latest/api/errors.html#cert-signature-failure)
The signature of the certificate is invalid.
#####  `CRL_SIGNATURE_FAILURE`[#](https://nodejs.org/docs/latest/api/errors.html#crl-signature-failure)
The signature of the certificate revocation list (CRL) is invalid.
#####  `ERROR_IN_CERT_NOT_BEFORE_FIELD`[#](https://nodejs.org/docs/latest/api/errors.html#error-in-cert-not-before-field)
The certificate notBefore field contains an invalid time.
#####  `ERROR_IN_CERT_NOT_AFTER_FIELD`[#](https://nodejs.org/docs/latest/api/errors.html#error-in-cert-not-after-field)
The certificate notAfter field contains an invalid time.
#####  `ERROR_IN_CRL_LAST_UPDATE_FIELD`[#](https://nodejs.org/docs/latest/api/errors.html#error-in-crl-last-update-field)
The CRL lastUpdate field contains an invalid time.
#####  `ERROR_IN_CRL_NEXT_UPDATE_FIELD`[#](https://nodejs.org/docs/latest/api/errors.html#error-in-crl-next-update-field)
The CRL nextUpdate field contains an invalid time.
#####  `UNABLE_TO_DECRYPT_CERT_SIGNATURE`[#](https://nodejs.org/docs/latest/api/errors.html#unable-to-decrypt-cert-signature)
The certificate signature could not be decrypted. This means that the actual signature value could not be determined rather than it not matching the expected value, this is only meaningful for RSA keys.
#####  `UNABLE_TO_DECRYPT_CRL_SIGNATURE`[#](https://nodejs.org/docs/latest/api/errors.html#unable-to-decrypt-crl-signature)
The certificate revocation list (CRL) signature could not be decrypted: this means that the actual signature value could not be determined rather than it not matching the expected value.
#####  `UNABLE_TO_DECODE_ISSUER_PUBLIC_KEY`[#](https://nodejs.org/docs/latest/api/errors.html#unable-to-decode-issuer-public-key)
The public key in the certificate SubjectPublicKeyInfo could not be read.
#### Other OpenSSL Errors[#](https://nodejs.org/docs/latest/api/errors.html#other-openssl-errors)
#####  `OUT_OF_MEM`[#](https://nodejs.org/docs/latest/api/errors.html#out-of-mem)
An error occurred trying to allocate memory. This should never happen.
