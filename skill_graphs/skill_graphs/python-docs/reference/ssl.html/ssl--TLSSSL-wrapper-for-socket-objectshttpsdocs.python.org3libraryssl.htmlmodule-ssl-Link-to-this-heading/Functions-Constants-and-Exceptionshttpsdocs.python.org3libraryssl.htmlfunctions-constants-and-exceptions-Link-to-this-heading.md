## Functions, Constants, and Exceptions[¶](https://docs.python.org/3/library/ssl.html#functions-constants-and-exceptions "Link to this heading")
### Socket creation[¶](https://docs.python.org/3/library/ssl.html#socket-creation "Link to this heading")
Instances of [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket") must be created using the [`SSLContext.wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket") method. The helper function [`create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context") returns a new context with secure default settings.
Client socket example with default context and IPv4/IPv6 dual stack:
Copy```
import socket
import ssl

hostname = 'www.python.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())

```

Client socket example with custom context and IPv4:
Copy```
hostname = 'www.python.org'
# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('path/to/cabundle.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())

```

Server socket example listening on localhost IPv4:
Copy```
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('/path/to/certchain.pem', '/path/to/private.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('127.0.0.1', 8443))
    sock.listen(5)
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        ...

```

### Context creation[¶](https://docs.python.org/3/library/ssl.html#context-creation "Link to this heading")
A convenience function helps create [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") objects for common purposes.

ssl.create_default_context(_purpose =Purpose.SERVER_AUTH_, _*_ , _cafile =None_, _capath =None_, _cadata =None_)[¶](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "Link to this definition")

Return a new [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") object with default settings for the given _purpose_. The settings are chosen by the `ssl` module, and usually represent a higher security level than when calling the `SSLContext` constructor directly.
_cafile_ , _capath_ , _cadata_ represent optional CA certificates to trust for certificate verification, as in [`SSLContext.load_verify_locations()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations "ssl.SSLContext.load_verify_locations"). If all three are [`None`](https://docs.python.org/3/library/constants.html#None "None"), this function can choose to trust the system’s default CA certificates instead.
The settings are: [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") or [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "ssl.PROTOCOL_TLS_SERVER"), [`OP_NO_SSLv2`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv2 "ssl.OP_NO_SSLv2"), and [`OP_NO_SSLv3`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv3 "ssl.OP_NO_SSLv3") with high encryption cipher suites without RC4 and without unauthenticated cipher suites. Passing [`SERVER_AUTH`](https://docs.python.org/3/library/ssl.html#ssl.Purpose.SERVER_AUTH "ssl.Purpose.SERVER_AUTH") as _purpose_ sets [`verify_mode`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode "ssl.SSLContext.verify_mode") to [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED") and either loads CA certificates (when at least one of _cafile_ , _capath_ or _cadata_ is given) or uses [`SSLContext.load_default_certs()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_default_certs "ssl.SSLContext.load_default_certs") to load default CA certificates.
When [`keylog_filename`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.keylog_filename "ssl.SSLContext.keylog_filename") is supported and the environment variable `SSLKEYLOGFILE` is set, `create_default_context()` enables key logging.
The default settings for this context include [`VERIFY_X509_PARTIAL_CHAIN`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN "ssl.VERIFY_X509_PARTIAL_CHAIN") and [`VERIFY_X509_STRICT`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_STRICT "ssl.VERIFY_X509_STRICT"). These make the underlying OpenSSL implementation behave more like a conforming implementation of
Note
The protocol, options, cipher and other settings may change to more restrictive values anytime without prior deprecation. The values represent a fair balance between compatibility and security.
If your application needs specific settings, you should create a [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") and apply the settings yourself.
Note
If you find that when certain older clients or servers attempt to connect with a [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") created by this function that they get an error stating “Protocol or cipher suite mismatch”, it may be that they only support SSL3.0 which this function excludes using the [`OP_NO_SSLv3`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv3 "ssl.OP_NO_SSLv3"). SSL3.0 is widely considered to be
Copy```
ctx = ssl.create_default_context(Purpose.CLIENT_AUTH)
ctx.options &= ~ssl.OP_NO_SSLv3

```

Note
This context enables [`VERIFY_X509_STRICT`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_STRICT "ssl.VERIFY_X509_STRICT") by default, which may reject pre-
Copy```
ctx = ssl.create_default_context()
ctx.verify_flags &= ~ssl.VERIFY_X509_STRICT

```

Added in version 3.4.
Changed in version 3.4.4: RC4 was dropped from the default cipher string.
Changed in version 3.6: ChaCha20/Poly1305 was added to the default cipher string.
3DES was dropped from the default cipher string.
Changed in version 3.8: Support for key logging to `SSLKEYLOGFILE` was added.
Changed in version 3.10: The context now uses [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") or [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "ssl.PROTOCOL_TLS_SERVER") protocol instead of generic [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS").
Changed in version 3.13: The context now uses [`VERIFY_X509_PARTIAL_CHAIN`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN "ssl.VERIFY_X509_PARTIAL_CHAIN") and [`VERIFY_X509_STRICT`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_STRICT "ssl.VERIFY_X509_STRICT") in its default verify flags.
### Exceptions[¶](https://docs.python.org/3/library/ssl.html#exceptions "Link to this heading")

_exception_ ssl.SSLError[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLError "Link to this definition")

Raised to signal an error from the underlying SSL implementation (currently provided by the OpenSSL library). This signifies some problem in the higher-level encryption and authentication layer that’s superimposed on the underlying network connection. This error is a subtype of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"). The error code and message of `SSLError` instances are provided by the OpenSSL library.
Changed in version 3.3: `SSLError` used to be a subtype of [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "socket.error").

library[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLError.library "Link to this definition")

A string mnemonic designating the OpenSSL submodule in which the error occurred, such as `SSL`, `PEM` or `X509`. The range of possible values depends on the OpenSSL version.
Added in version 3.3.

reason[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLError.reason "Link to this definition")

A string mnemonic designating the reason this error occurred, for example `CERTIFICATE_VERIFY_FAILED`. The range of possible values depends on the OpenSSL version.
Added in version 3.3.

_exception_ ssl.SSLZeroReturnError[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLZeroReturnError "Link to this definition")

A subclass of [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") raised when trying to read or write and the SSL connection has been closed cleanly. Note that this doesn’t mean that the underlying transport (read TCP) has been closed.
Added in version 3.3.

_exception_ ssl.SSLWantReadError[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLWantReadError "Link to this definition")

A subclass of [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") raised by a [non-blocking SSL socket](https://docs.python.org/3/library/ssl.html#ssl-nonblocking) when trying to read or write data, but more data needs to be received on the underlying TCP transport before the request can be fulfilled.
Added in version 3.3.

_exception_ ssl.SSLWantWriteError[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLWantWriteError "Link to this definition")

A subclass of [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") raised by a [non-blocking SSL socket](https://docs.python.org/3/library/ssl.html#ssl-nonblocking) when trying to read or write data, but more data needs to be sent on the underlying TCP transport before the request can be fulfilled.
Added in version 3.3.

_exception_ ssl.SSLSyscallError[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSyscallError "Link to this definition")

A subclass of [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") raised when a system error was encountered while trying to fulfill an operation on a SSL socket. Unfortunately, there is no easy way to inspect the original errno number.
Added in version 3.3.

_exception_ ssl.SSLEOFError[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLEOFError "Link to this definition")

A subclass of [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") raised when the SSL connection has been terminated abruptly. Generally, you shouldn’t try to reuse the underlying transport when this error is encountered.
Added in version 3.3.

_exception_ ssl.SSLCertVerificationError[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLCertVerificationError "Link to this definition")

A subclass of [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") raised when certificate validation has failed.
Added in version 3.7.

verify_code[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLCertVerificationError.verify_code "Link to this definition")

A numeric error number that denotes the verification error.

verify_message[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLCertVerificationError.verify_message "Link to this definition")

A human readable string of the verification error.

_exception_ ssl.CertificateError[¶](https://docs.python.org/3/library/ssl.html#ssl.CertificateError "Link to this definition")

An alias for [`SSLCertVerificationError`](https://docs.python.org/3/library/ssl.html#ssl.SSLCertVerificationError "ssl.SSLCertVerificationError").
Changed in version 3.7: The exception is now an alias for [`SSLCertVerificationError`](https://docs.python.org/3/library/ssl.html#ssl.SSLCertVerificationError "ssl.SSLCertVerificationError").
### Random generation[¶](https://docs.python.org/3/library/ssl.html#random-generation "Link to this heading")

ssl.RAND_bytes(_num_ , _/_)[¶](https://docs.python.org/3/library/ssl.html#ssl.RAND_bytes "Link to this definition")

Return _num_ cryptographically strong pseudo-random bytes. Raises an [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") if the PRNG has not been seeded with enough data or if the operation is not supported by the current RAND method. [`RAND_status()`](https://docs.python.org/3/library/ssl.html#ssl.RAND_status "ssl.RAND_status") can be used to check the status of the PRNG and [`RAND_add()`](https://docs.python.org/3/library/ssl.html#ssl.RAND_add "ssl.RAND_add") can be used to seed the PRNG.
For almost all applications [`os.urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom") is preferable.
Read the Wikipedia article,
Added in version 3.3.

ssl.RAND_status()[¶](https://docs.python.org/3/library/ssl.html#ssl.RAND_status "Link to this definition")

Return `True` if the SSL pseudo-random number generator has been seeded with ‘enough’ randomness, and `False` otherwise. You can use `ssl.RAND_egd()` and [`ssl.RAND_add()`](https://docs.python.org/3/library/ssl.html#ssl.RAND_add "ssl.RAND_add") to increase the randomness of the pseudo-random number generator.

ssl.RAND_add(_bytes_ , _entropy_ , _/_)[¶](https://docs.python.org/3/library/ssl.html#ssl.RAND_add "Link to this definition")

Mix the given _bytes_ into the SSL pseudo-random number generator. The parameter _entropy_ (a float) is a lower bound on the entropy contained in string (so you can always use `0.0`). See
Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) is now accepted.
### Certificate handling[¶](https://docs.python.org/3/library/ssl.html#certificate-handling "Link to this heading")

ssl.cert_time_to_seconds(_cert_time_)[¶](https://docs.python.org/3/library/ssl.html#ssl.cert_time_to_seconds "Link to this definition")

Return the time in seconds since the Epoch, given the `cert_time` string representing the “notBefore” or “notAfter” date from a certificate in `"%b %d %H:%M:%S %Y %Z"` strptime format (C locale).
Here’s an example:
Copy```
>>> import ssl
>>> timestamp = ssl.cert_time_to_seconds("Jan  5 09:34:43 2018 GMT")
>>> timestamp
1515144883
>>> from datetime import datetime
>>> print(datetime.utcfromtimestamp(timestamp))
2018-01-05 09:34:43

```

“notBefore” or “notAfter” dates must use GMT (
Changed in version 3.5: Interpret the input time as a time in UTC as specified by ‘GMT’ timezone in the input string. Local timezone was used previously. Return an integer (no fractions of a second in the input format)

ssl.get_server_certificate(_addr_ , _ssl_version=PROTOCOL_TLS_CLIENT_ , _ca_certs=None_[, _timeout_])[¶](https://docs.python.org/3/library/ssl.html#ssl.get_server_certificate "Link to this definition")

Given the address `addr` of an SSL-protected server, as a (_hostname_ , _port-number_) pair, fetches the server’s certificate, and returns it as a PEM-encoded string. If `ssl_version` is specified, uses that version of the SSL protocol to attempt to connect to the server. If _ca_certs_ is specified, it should be a file containing a list of root certificates, the same format as used for the _cafile_ parameter in [`SSLContext.load_verify_locations()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations "ssl.SSLContext.load_verify_locations"). The call will attempt to validate the server certificate against that set of root certificates, and will fail if the validation attempt fails. A timeout can be specified with the `timeout` parameter.
Changed in version 3.3: This function is now IPv6-compatible.
Changed in version 3.5: The default _ssl_version_ is changed from [`PROTOCOL_SSLv3`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_SSLv3 "ssl.PROTOCOL_SSLv3") to [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS") for maximum compatibility with modern servers.
Changed in version 3.10: The _timeout_ parameter was added.

ssl.DER_cert_to_PEM_cert(_der_cert_bytes_)[¶](https://docs.python.org/3/library/ssl.html#ssl.DER_cert_to_PEM_cert "Link to this definition")

Given a certificate as a DER-encoded blob of bytes, returns a PEM-encoded string version of the same certificate.

ssl.PEM_cert_to_DER_cert(_pem_cert_string_)[¶](https://docs.python.org/3/library/ssl.html#ssl.PEM_cert_to_DER_cert "Link to this definition")

Given a certificate as an ASCII PEM string, returns a DER-encoded sequence of bytes for that same certificate.

ssl.get_default_verify_paths()[¶](https://docs.python.org/3/library/ssl.html#ssl.get_default_verify_paths "Link to this definition")

Returns a named tuple with paths to OpenSSL’s default cafile and capath. The paths are the same as used by [`SSLContext.set_default_verify_paths()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_default_verify_paths "ssl.SSLContext.set_default_verify_paths"). The return value is a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple) `DefaultVerifyPaths`:
  * `cafile` - resolved path to cafile or `None` if the file doesn’t exist,
  * `capath` - resolved path to capath or `None` if the directory doesn’t exist,
  * `openssl_cafile_env` - OpenSSL’s environment key that points to a cafile,
  * `openssl_cafile` - hard coded path to a cafile,
  * `openssl_capath_env` - OpenSSL’s environment key that points to a capath,
  * `openssl_capath` - hard coded path to a capath directory


Added in version 3.4.

ssl.enum_certificates(_store_name_)[¶](https://docs.python.org/3/library/ssl.html#ssl.enum_certificates "Link to this definition")

Retrieve certificates from Windows’ system cert store. _store_name_ may be one of `CA`, `ROOT` or `MY`. Windows may provide additional cert stores, too.
The function returns a list of (cert_bytes, encoding_type, trust) tuples. The encoding_type specifies the encoding of cert_bytes. It is either `x509_asn` for X.509 ASN.1 data or `pkcs_7_asn` for PKCS#7 ASN.1 data. Trust specifies the purpose of the certificate as a set of OIDS or exactly `True` if the certificate is trustworthy for all purposes.
Example:
Copy```
>>> ssl.enum_certificates("CA")
[(b'data...', 'x509_asn', {'1.3.6.1.5.5.7.3.1', '1.3.6.1.5.5.7.3.2'}),
 (b'data...', 'x509_asn', True)]

```

[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Added in version 3.4.

ssl.enum_crls(_store_name_)[¶](https://docs.python.org/3/library/ssl.html#ssl.enum_crls "Link to this definition")

Retrieve CRLs from Windows’ system cert store. _store_name_ may be one of `CA`, `ROOT` or `MY`. Windows may provide additional cert stores, too.
The function returns a list of (cert_bytes, encoding_type, trust) tuples. The encoding_type specifies the encoding of cert_bytes. It is either `x509_asn` for X.509 ASN.1 data or `pkcs_7_asn` for PKCS#7 ASN.1 data.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Added in version 3.4.
### Constants[¶](https://docs.python.org/3/library/ssl.html#constants "Link to this heading")
> All constants are now [`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") or [`enum.IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") collections.
> Added in version 3.6.

ssl.CERT_NONE[¶](https://docs.python.org/3/library/ssl.html#ssl.CERT_NONE "Link to this definition")

Possible value for [`SSLContext.verify_mode`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode "ssl.SSLContext.verify_mode"). Except for [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT"), it is the default mode. With client-side sockets, just about any cert is accepted. Validation errors, such as untrusted or expired cert, are ignored and do not abort the TLS/SSL handshake.
In server mode, no certificate is requested from the client, so the client does not send any for client cert authentication.
See the discussion of [Security considerations](https://docs.python.org/3/library/ssl.html#ssl-security) below.

ssl.CERT_OPTIONAL[¶](https://docs.python.org/3/library/ssl.html#ssl.CERT_OPTIONAL "Link to this definition")

Possible value for [`SSLContext.verify_mode`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode "ssl.SSLContext.verify_mode"). In client mode, [`CERT_OPTIONAL`](https://docs.python.org/3/library/ssl.html#ssl.CERT_OPTIONAL "ssl.CERT_OPTIONAL") has the same meaning as [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED"). It is recommended to use `CERT_REQUIRED` for client-side sockets instead.
In server mode, a client certificate request is sent to the client. The client may either ignore the request or send a certificate in order perform TLS client cert authentication. If the client chooses to send a certificate, it is verified. Any verification error immediately aborts the TLS handshake.
Use of this setting requires a valid set of CA certificates to be passed to [`SSLContext.load_verify_locations()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations "ssl.SSLContext.load_verify_locations").

ssl.CERT_REQUIRED[¶](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "Link to this definition")

Possible value for [`SSLContext.verify_mode`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode "ssl.SSLContext.verify_mode"). In this mode, certificates are required from the other side of the socket connection; an [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") will be raised if no certificate is provided, or if its validation fails. This mode is **not** sufficient to verify a certificate in client mode as it does not match hostnames. [`check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") must be enabled as well to verify the authenticity of a cert. [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") uses [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED") and enables `check_hostname` by default.
With server socket, this mode provides mandatory TLS client cert authentication. A client certificate request is sent to the client and the client must provide a valid and trusted certificate.
Use of this setting requires a valid set of CA certificates to be passed to [`SSLContext.load_verify_locations()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations "ssl.SSLContext.load_verify_locations").

_class_ ssl.VerifyMode[¶](https://docs.python.org/3/library/ssl.html#ssl.VerifyMode "Link to this definition")

[`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") collection of CERT_* constants.
Added in version 3.6.

ssl.VERIFY_DEFAULT[¶](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_DEFAULT "Link to this definition")

Possible value for [`SSLContext.verify_flags`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_flags "ssl.SSLContext.verify_flags"). In this mode, certificate revocation lists (CRLs) are not checked. By default OpenSSL does neither require nor verify CRLs.
Added in version 3.4.

ssl.VERIFY_CRL_CHECK_LEAF[¶](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_CRL_CHECK_LEAF "Link to this definition")

Possible value for [`SSLContext.verify_flags`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_flags "ssl.SSLContext.verify_flags"). In this mode, only the peer cert is checked but none of the intermediate CA certificates. The mode requires a valid CRL that is signed by the peer cert’s issuer (its direct ancestor CA). If no proper CRL has been loaded with [`SSLContext.load_verify_locations`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations "ssl.SSLContext.load_verify_locations"), validation will fail.
Added in version 3.4.

ssl.VERIFY_CRL_CHECK_CHAIN[¶](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_CRL_CHECK_CHAIN "Link to this definition")

Possible value for [`SSLContext.verify_flags`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_flags "ssl.SSLContext.verify_flags"). In this mode, CRLs of all certificates in the peer cert chain are checked.
Added in version 3.4.

ssl.VERIFY_X509_STRICT[¶](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_STRICT "Link to this definition")

Possible value for [`SSLContext.verify_flags`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_flags "ssl.SSLContext.verify_flags") to disable workarounds for broken X.509 certificates.
Added in version 3.4.

ssl.VERIFY_ALLOW_PROXY_CERTS[¶](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_ALLOW_PROXY_CERTS "Link to this definition")

Possible value for [`SSLContext.verify_flags`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_flags "ssl.SSLContext.verify_flags") to enables proxy certificate verification.
Added in version 3.10.

ssl.VERIFY_X509_TRUSTED_FIRST[¶](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_TRUSTED_FIRST "Link to this definition")

Possible value for [`SSLContext.verify_flags`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_flags "ssl.SSLContext.verify_flags"). It instructs OpenSSL to prefer trusted certificates when building the trust chain to validate a certificate. This flag is enabled by default.
Added in version 3.4.4.

ssl.VERIFY_X509_PARTIAL_CHAIN[¶](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN "Link to this definition")

Possible value for [`SSLContext.verify_flags`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_flags "ssl.SSLContext.verify_flags"). It instructs OpenSSL to accept intermediate CAs in the trust store to be treated as trust-anchors, in the same way as the self-signed root CA certificates. This makes it possible to trust certificates issued by an intermediate CA without having to trust its ancestor root CA.
Added in version 3.10.

_class_ ssl.VerifyFlags[¶](https://docs.python.org/3/library/ssl.html#ssl.VerifyFlags "Link to this definition")

[`enum.IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") collection of VERIFY_* constants.
Added in version 3.6.

ssl.PROTOCOL_TLS[¶](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "Link to this definition")

Selects the highest protocol version that both the client and server support. Despite the name, this option can select both “SSL” and “TLS” protocols.
Added in version 3.6.
Deprecated since version 3.10: TLS clients and servers require different default settings for secure communication. The generic TLS protocol constant is deprecated in favor of [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") and [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "ssl.PROTOCOL_TLS_SERVER").

ssl.PROTOCOL_TLS_CLIENT[¶](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "Link to this definition")

Auto-negotiate the highest protocol version that both the client and server support, and configure the context client-side connections. The protocol enables [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED") and [`check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") by default.
Added in version 3.6.

ssl.PROTOCOL_TLS_SERVER[¶](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "Link to this definition")

Auto-negotiate the highest protocol version that both the client and server support, and configure the context server-side connections.
Added in version 3.6.

ssl.PROTOCOL_SSLv23[¶](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_SSLv23 "Link to this definition")

Alias for [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS").
Deprecated since version 3.6: Use [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS") instead.

ssl.PROTOCOL_SSLv3[¶](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_SSLv3 "Link to this definition")

Selects SSL version 3 as the channel encryption protocol.
This protocol is not available if OpenSSL is compiled with the `no-ssl3` option.
Warning
SSL version 3 is insecure. Its use is highly discouraged.
Deprecated since version 3.6: OpenSSL has deprecated all version specific protocols. Use the default protocol [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "ssl.PROTOCOL_TLS_SERVER") or [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") with [`SSLContext.minimum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.minimum_version "ssl.SSLContext.minimum_version") and [`SSLContext.maximum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.maximum_version "ssl.SSLContext.maximum_version") instead.

ssl.PROTOCOL_TLSv1[¶](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLSv1 "Link to this definition")

Selects TLS version 1.0 as the channel encryption protocol.
Deprecated since version 3.6: OpenSSL has deprecated all version specific protocols.

ssl.PROTOCOL_TLSv1_1[¶](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLSv1_1 "Link to this definition")

Selects TLS version 1.1 as the channel encryption protocol. Available only with openssl version 1.0.1+.
Added in version 3.4.
Deprecated since version 3.6: OpenSSL has deprecated all version specific protocols.

ssl.PROTOCOL_TLSv1_2[¶](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLSv1_2 "Link to this definition")

Selects TLS version 1.2 as the channel encryption protocol. Available only with openssl version 1.0.1+.
Added in version 3.4.
Deprecated since version 3.6: OpenSSL has deprecated all version specific protocols.

ssl.OP_ALL[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_ALL "Link to this definition")

Enables workarounds for various bugs present in other SSL implementations. This option is set by default. It does not necessarily set the same flags as OpenSSL’s `SSL_OP_ALL` constant.
Added in version 3.2.

ssl.OP_NO_SSLv2[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv2 "Link to this definition")

Prevents an SSLv2 connection. This option is only applicable in conjunction with [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS"). It prevents the peers from choosing SSLv2 as the protocol version.
Added in version 3.2.
Deprecated since version 3.6: SSLv2 is deprecated

ssl.OP_NO_SSLv3[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv3 "Link to this definition")

Prevents an SSLv3 connection. This option is only applicable in conjunction with [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS"). It prevents the peers from choosing SSLv3 as the protocol version.
Added in version 3.2.
Deprecated since version 3.6: SSLv3 is deprecated

ssl.OP_NO_TLSv1[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_TLSv1 "Link to this definition")

Prevents a TLSv1 connection. This option is only applicable in conjunction with [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS"). It prevents the peers from choosing TLSv1 as the protocol version.
Added in version 3.2.
Deprecated since version 3.7: The option is deprecated since OpenSSL 1.1.0, use the new [`SSLContext.minimum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.minimum_version "ssl.SSLContext.minimum_version") and [`SSLContext.maximum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.maximum_version "ssl.SSLContext.maximum_version") instead.

ssl.OP_NO_TLSv1_1[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_TLSv1_1 "Link to this definition")

Prevents a TLSv1.1 connection. This option is only applicable in conjunction with [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS"). It prevents the peers from choosing TLSv1.1 as the protocol version. Available only with openssl version 1.0.1+.
Added in version 3.4.
Deprecated since version 3.7: The option is deprecated since OpenSSL 1.1.0.

ssl.OP_NO_TLSv1_2[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_TLSv1_2 "Link to this definition")

Prevents a TLSv1.2 connection. This option is only applicable in conjunction with [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS"). It prevents the peers from choosing TLSv1.2 as the protocol version. Available only with openssl version 1.0.1+.
Added in version 3.4.
Deprecated since version 3.7: The option is deprecated since OpenSSL 1.1.0.

ssl.OP_NO_TLSv1_3[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_TLSv1_3 "Link to this definition")

Prevents a TLSv1.3 connection. This option is only applicable in conjunction with [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS"). It prevents the peers from choosing TLSv1.3 as the protocol version. TLS 1.3 is available with OpenSSL 1.1.1 or later. When Python has been compiled against an older version of OpenSSL, the flag defaults to _0_.
Added in version 3.6.3.
Deprecated since version 3.7: The option is deprecated since OpenSSL 1.1.0. It was added to 2.7.15 and 3.6.3 for backwards compatibility with OpenSSL 1.0.2.

ssl.OP_NO_RENEGOTIATION[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_RENEGOTIATION "Link to this definition")

Disable all renegotiation in TLSv1.2 and earlier. Do not send HelloRequest messages, and ignore renegotiation requests via ClientHello.
This option is only available with OpenSSL 1.1.0h and later.
Added in version 3.7.

ssl.OP_CIPHER_SERVER_PREFERENCE[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_CIPHER_SERVER_PREFERENCE "Link to this definition")

Use the server’s cipher ordering preference, rather than the client’s. This option has no effect on client sockets and SSLv2 server sockets.
Added in version 3.3.

ssl.OP_SINGLE_DH_USE[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_SINGLE_DH_USE "Link to this definition")

Prevents reuse of the same DH key for distinct SSL sessions. This improves forward secrecy but requires more computational resources. This option only applies to server sockets.
Added in version 3.3.

ssl.OP_SINGLE_ECDH_USE[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_SINGLE_ECDH_USE "Link to this definition")

Prevents reuse of the same ECDH key for distinct SSL sessions. This improves forward secrecy but requires more computational resources. This option only applies to server sockets.
Added in version 3.3.

ssl.OP_ENABLE_MIDDLEBOX_COMPAT[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_ENABLE_MIDDLEBOX_COMPAT "Link to this definition")

Send dummy Change Cipher Spec (CCS) messages in TLS 1.3 handshake to make a TLS 1.3 connection look more like a TLS 1.2 connection.
This option is only available with OpenSSL 1.1.1 and later.
Added in version 3.8.

ssl.OP_NO_COMPRESSION[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_COMPRESSION "Link to this definition")

Disable compression on the SSL channel. This is useful if the application protocol supports its own compression scheme.
Added in version 3.3.

_class_ ssl.Options[¶](https://docs.python.org/3/library/ssl.html#ssl.Options "Link to this definition")

[`enum.IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") collection of OP_* constants.

ssl.OP_NO_TICKET[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_TICKET "Link to this definition")

Prevent client side from requesting a session ticket.
Added in version 3.6.

ssl.OP_IGNORE_UNEXPECTED_EOF[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_IGNORE_UNEXPECTED_EOF "Link to this definition")

Ignore unexpected shutdown of TLS connections.
This option is only available with OpenSSL 3.0.0 and later.
Added in version 3.10.

ssl.OP_ENABLE_KTLS[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_ENABLE_KTLS "Link to this definition")

Enable the use of the kernel TLS. To benefit from the feature, OpenSSL must have been compiled with support for it, and the negotiated cipher suites and extensions must be supported by it (a list of supported ones may vary by platform and kernel version).
Note that with enabled kernel TLS some cryptographic operations are performed by the kernel directly and not via any available OpenSSL Providers. This might be undesirable if, for example, the application requires all cryptographic operations to be performed by the FIPS provider.
This option is only available with OpenSSL 3.0.0 and later.
Added in version 3.12.

ssl.OP_LEGACY_SERVER_CONNECT[¶](https://docs.python.org/3/library/ssl.html#ssl.OP_LEGACY_SERVER_CONNECT "Link to this definition")

Allow legacy insecure renegotiation between OpenSSL and unpatched servers only.
Added in version 3.12.

ssl.HAS_ALPN[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_ALPN "Link to this definition")

Whether the OpenSSL library has built-in support for the _Application-Layer Protocol Negotiation_ TLS extension as described in
Added in version 3.5.

ssl.HAS_NEVER_CHECK_COMMON_NAME[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_NEVER_CHECK_COMMON_NAME "Link to this definition")

Whether the OpenSSL library has built-in support not checking subject common name and [`SSLContext.hostname_checks_common_name`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.hostname_checks_common_name "ssl.SSLContext.hostname_checks_common_name") is writeable.
Added in version 3.7.

ssl.HAS_ECDH[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_ECDH "Link to this definition")

Whether the OpenSSL library has built-in support for the Elliptic Curve-based Diffie-Hellman key exchange. This should be true unless the feature was explicitly disabled by the distributor.
Added in version 3.3.

ssl.HAS_SNI[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "Link to this definition")

Whether the OpenSSL library has built-in support for the _Server Name Indication_ extension (as defined in
Added in version 3.2.

ssl.HAS_NPN[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_NPN "Link to this definition")

Whether the OpenSSL library has built-in support for the _Next Protocol Negotiation_ as described in the [`SSLContext.set_npn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_npn_protocols "ssl.SSLContext.set_npn_protocols") method to advertise which protocols you want to support.
Added in version 3.3.

ssl.HAS_SSLv2[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_SSLv2 "Link to this definition")

Whether the OpenSSL library has built-in support for the SSL 2.0 protocol.
Added in version 3.7.

ssl.HAS_SSLv3[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_SSLv3 "Link to this definition")

Whether the OpenSSL library has built-in support for the SSL 3.0 protocol.
Added in version 3.7.

ssl.HAS_TLSv1[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_TLSv1 "Link to this definition")

Whether the OpenSSL library has built-in support for the TLS 1.0 protocol.
Added in version 3.7.

ssl.HAS_TLSv1_1[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_TLSv1_1 "Link to this definition")

Whether the OpenSSL library has built-in support for the TLS 1.1 protocol.
Added in version 3.7.

ssl.HAS_TLSv1_2[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_TLSv1_2 "Link to this definition")

Whether the OpenSSL library has built-in support for the TLS 1.2 protocol.
Added in version 3.7.

ssl.HAS_TLSv1_3[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_TLSv1_3 "Link to this definition")

Whether the OpenSSL library has built-in support for the TLS 1.3 protocol.
Added in version 3.7.

ssl.HAS_PSK[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_PSK "Link to this definition")

Whether the OpenSSL library has built-in support for TLS-PSK.
Added in version 3.13.

ssl.HAS_PHA[¶](https://docs.python.org/3/library/ssl.html#ssl.HAS_PHA "Link to this definition")

Whether the OpenSSL library has built-in support for TLS-PHA.
Added in version 3.14.

ssl.CHANNEL_BINDING_TYPES[¶](https://docs.python.org/3/library/ssl.html#ssl.CHANNEL_BINDING_TYPES "Link to this definition")

List of supported TLS channel binding types. Strings in this list can be used as arguments to [`SSLSocket.get_channel_binding()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_channel_binding "ssl.SSLSocket.get_channel_binding").
Added in version 3.3.

ssl.OPENSSL_VERSION[¶](https://docs.python.org/3/library/ssl.html#ssl.OPENSSL_VERSION "Link to this definition")

The version string of the OpenSSL library loaded by the interpreter:
Copy```
>>> ssl.OPENSSL_VERSION
'OpenSSL 1.0.2k  26 Jan 2017'

```

Added in version 3.2.

ssl.OPENSSL_VERSION_INFO[¶](https://docs.python.org/3/library/ssl.html#ssl.OPENSSL_VERSION_INFO "Link to this definition")

A tuple of five integers representing version information about the OpenSSL library:
Copy```
>>> ssl.OPENSSL_VERSION_INFO
(1, 0, 2, 11, 15)

```

Added in version 3.2.

ssl.OPENSSL_VERSION_NUMBER[¶](https://docs.python.org/3/library/ssl.html#ssl.OPENSSL_VERSION_NUMBER "Link to this definition")

The raw version number of the OpenSSL library, as a single integer:
Copy```
>>> ssl.OPENSSL_VERSION_NUMBER
268443839
>>> hex(ssl.OPENSSL_VERSION_NUMBER)
'0x100020bf'

```

Added in version 3.2.

ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE[¶](https://docs.python.org/3/library/ssl.html#ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE "Link to this definition")


ssl.ALERT_DESCRIPTION_INTERNAL_ERROR[¶](https://docs.python.org/3/library/ssl.html#ssl.ALERT_DESCRIPTION_INTERNAL_ERROR "Link to this definition")


ALERT_DESCRIPTION_*

Alert Descriptions from
Used as the return value of the callback function in [`SSLContext.set_servername_callback()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_servername_callback "ssl.SSLContext.set_servername_callback").
Added in version 3.4.

_class_ ssl.AlertDescription[¶](https://docs.python.org/3/library/ssl.html#ssl.AlertDescription "Link to this definition")

[`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") collection of ALERT_DESCRIPTION_* constants.
Added in version 3.6.

Purpose.SERVER_AUTH[¶](https://docs.python.org/3/library/ssl.html#ssl.Purpose.SERVER_AUTH "Link to this definition")

Option for [`create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context") and [`SSLContext.load_default_certs()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_default_certs "ssl.SSLContext.load_default_certs"). This value indicates that the context may be used to authenticate web servers (therefore, it will be used to create client-side sockets).
Added in version 3.4.

Purpose.CLIENT_AUTH[¶](https://docs.python.org/3/library/ssl.html#ssl.Purpose.CLIENT_AUTH "Link to this definition")

Option for [`create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context") and [`SSLContext.load_default_certs()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_default_certs "ssl.SSLContext.load_default_certs"). This value indicates that the context may be used to authenticate web clients (therefore, it will be used to create server-side sockets).
Added in version 3.4.

_class_ ssl.SSLErrorNumber[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLErrorNumber "Link to this definition")

[`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") collection of SSL_ERROR_* constants.
Added in version 3.6.

_class_ ssl.TLSVersion[¶](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion "Link to this definition")

[`enum.IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") collection of SSL and TLS versions for [`SSLContext.maximum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.maximum_version "ssl.SSLContext.maximum_version") and [`SSLContext.minimum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.minimum_version "ssl.SSLContext.minimum_version").
Added in version 3.7.

TLSVersion.MINIMUM_SUPPORTED[¶](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.MINIMUM_SUPPORTED "Link to this definition")


TLSVersion.MAXIMUM_SUPPORTED[¶](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.MAXIMUM_SUPPORTED "Link to this definition")

The minimum or maximum supported SSL or TLS version. These are magic constants. Their values don’t reflect the lowest and highest available TLS/SSL versions.

TLSVersion.SSLv3[¶](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.SSLv3 "Link to this definition")


TLSVersion.TLSv1[¶](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.TLSv1 "Link to this definition")


TLSVersion.TLSv1_1[¶](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.TLSv1_1 "Link to this definition")


TLSVersion.TLSv1_2[¶](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.TLSv1_2 "Link to this definition")


TLSVersion.TLSv1_3[¶](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.TLSv1_3 "Link to this definition")

SSL 3.0 to TLS 1.3.
Deprecated since version 3.10: All [`TLSVersion`](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion "ssl.TLSVersion") members except [`TLSVersion.TLSv1_2`](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.TLSv1_2 "ssl.TLSVersion.TLSv1_2") and `TLSVersion.TLSv1_3` are deprecated.
