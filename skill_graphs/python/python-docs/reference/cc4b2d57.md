Note
`SSLContext` only supports limited mutation once it has been used by a connection. Adding new certificates to the internal trust store is allowed, but changing ciphers, verification settings, or mTLS certificates may result in surprising behavior.
Note
`SSLContext` is designed to be shared and used by multiple connections. Thus, it is thread-safe as long as it is not reconfigured after being used by a connection.
[`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") objects have the following methods and attributes:

SSLContext.cert_store_stats()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.cert_store_stats "Link to this definition")

Get statistics about quantities of loaded X.509 certificates, count of X.509 certificates flagged as CA certificates and certificate revocation lists as dictionary.
Example for a context with one CA cert and one other cert:
Copy```
>>> context.cert_store_stats()
{'crl': 0, 'x509_ca': 1, 'x509': 2}

```

Added in version 3.4.

SSLContext.load_cert_chain(_certfile_ , _keyfile =None_, _password =None_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain "Link to this definition")

Load a private key and the corresponding certificate. The _certfile_ string must be the path to a single file in PEM format containing the certificate as well as any number of CA certificates needed to establish the certificate’s authenticity. The _keyfile_ string, if present, must point to a file containing the private key. Otherwise the private key will be taken from _certfile_ as well. See the discussion of [Certificates](https://docs.python.org/3/library/ssl.html#ssl-certificates) for more information on how the certificate is stored in the _certfile_.
The _password_ argument may be a function to call to get the password for decrypting the private key. It will only be called if the private key is encrypted and a password is necessary. It will be called with no arguments, and it should return a string, bytes, or bytearray. If the return value is a string it will be encoded as UTF-8 before using it to decrypt the key. Alternatively a string, bytes, or bytearray value may be supplied directly as the _password_ argument. It will be ignored if the private key is not encrypted and no password is needed.
If the _password_ argument is not specified and a password is required, OpenSSL’s built-in password prompting mechanism will be used to interactively prompt the user for a password.
An [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") is raised if the private key doesn’t match with the certificate.
Changed in version 3.3: New optional argument _password_.

SSLContext.load_default_certs(_purpose =Purpose.SERVER_AUTH_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_default_certs "Link to this definition")

Load a set of default “certification authority” (CA) certificates from default locations. On Windows it loads CA certs from the `CA` and `ROOT` system stores. On all systems it calls [`SSLContext.set_default_verify_paths()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_default_verify_paths "ssl.SSLContext.set_default_verify_paths"). In the future the method may load CA certificates from other locations, too.
The _purpose_ flag specifies what kind of CA certificates are loaded. The default settings [`Purpose.SERVER_AUTH`](https://docs.python.org/3/library/ssl.html#ssl.Purpose.SERVER_AUTH "ssl.Purpose.SERVER_AUTH") loads certificates, that are flagged and trusted for TLS web server authentication (client side sockets). [`Purpose.CLIENT_AUTH`](https://docs.python.org/3/library/ssl.html#ssl.Purpose.CLIENT_AUTH "ssl.Purpose.CLIENT_AUTH") loads CA certificates for client certificate verification on the server side.
Added in version 3.4.

SSLContext.load_verify_locations(_cafile =None_, _capath =None_, _cadata =None_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations "Link to this definition")

Load a set of “certification authority” (CA) certificates used to validate other peers’ certificates when [`verify_mode`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode "ssl.SSLContext.verify_mode") is other than [`CERT_NONE`](https://docs.python.org/3/library/ssl.html#ssl.CERT_NONE "ssl.CERT_NONE"). At least one of _cafile_ or _capath_ must be specified.
This method can also load certification revocation lists (CRLs) in PEM or DER format. In order to make use of CRLs, [`SSLContext.verify_flags`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_flags "ssl.SSLContext.verify_flags") must be configured properly.
The _cafile_ string, if present, is the path to a file of concatenated CA certificates in PEM format. See the discussion of [Certificates](https://docs.python.org/3/library/ssl.html#ssl-certificates) for more information about how to arrange the certificates in this file.
The _capath_ string, if present, is the path to a directory containing several CA certificates in PEM format, following an
The _cadata_ object, if present, is either an ASCII string of one or more PEM-encoded certificates or a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) of DER-encoded certificates. Like with _capath_ extra lines around PEM-encoded certificates are ignored but at least one certificate must be present.
Changed in version 3.4: New optional argument _cadata_

SSLContext.get_ca_certs(_binary_form =False_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.get_ca_certs "Link to this definition")

Get a list of loaded “certification authority” (CA) certificates. If the `binary_form` parameter is [`False`](https://docs.python.org/3/library/constants.html#False "False") each list entry is a dict like the output of [`SSLSocket.getpeercert()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert "ssl.SSLSocket.getpeercert"). Otherwise the method returns a list of DER-encoded certificates. The returned list does not contain certificates from _capath_ unless a certificate was requested and loaded by a SSL connection.
Note
Certificates in a capath directory aren’t loaded unless they have been used at least once.
Added in version 3.4.

SSLContext.get_ciphers()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.get_ciphers "Link to this definition")

Get a list of enabled ciphers. The list is in order of cipher priority. See [`SSLContext.set_ciphers()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ciphers "ssl.SSLContext.set_ciphers").
Example:
Copy```
>>> ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
>>> ctx.set_ciphers('ECDHE+AESGCM:!ECDSA')
>>> ctx.get_ciphers()
[{'aead': True,
  'alg_bits': 256,
  'auth': 'auth-rsa',
  'description': 'ECDHE-RSA-AES256-GCM-SHA384 TLSv1.2 Kx=ECDH     Au=RSA  '
                 'Enc=AESGCM(256) Mac=AEAD',
  'digest': None,
  'id': 50380848,
  'kea': 'kx-ecdhe',
  'name': 'ECDHE-RSA-AES256-GCM-SHA384',
  'protocol': 'TLSv1.2',
  'strength_bits': 256,
  'symmetric': 'aes-256-gcm'},
 {'aead': True,
  'alg_bits': 128,
  'auth': 'auth-rsa',
  'description': 'ECDHE-RSA-AES128-GCM-SHA256 TLSv1.2 Kx=ECDH     Au=RSA  '
                 'Enc=AESGCM(128) Mac=AEAD',
  'digest': None,
  'id': 50380847,
  'kea': 'kx-ecdhe',
  'name': 'ECDHE-RSA-AES128-GCM-SHA256',
  'protocol': 'TLSv1.2',
  'strength_bits': 128,
  'symmetric': 'aes-128-gcm'}]

```

Added in version 3.6.

SSLContext.set_default_verify_paths()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_default_verify_paths "Link to this definition")

Load a set of default “certification authority” (CA) certificates from a filesystem path defined when building the OpenSSL library. Unfortunately, there’s no easy way to know whether this method succeeds: no error is returned if no certificates are to be found. When the OpenSSL library is provided as part of the operating system, though, it is likely to be configured properly.

SSLContext.set_ciphers(_ciphers_ , _/_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ciphers "Link to this definition")

Set the available ciphers for sockets created with this context. It should be a string in the [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") will be raised.
Note
when connected, the [`SSLSocket.cipher()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.cipher "ssl.SSLSocket.cipher") method of SSL sockets will give the currently selected cipher.
TLS 1.3 cipher suites cannot be disabled with `set_ciphers()`.

SSLContext.set_alpn_protocols(_alpn_protocols_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_alpn_protocols "Link to this definition")

Specify which protocols the socket should advertise during the SSL/TLS handshake. It should be a list of ASCII strings, like `['http/1.1', 'spdy/2']`, ordered by preference. The selection of a protocol will happen during the handshake, and will play out according to [`SSLSocket.selected_alpn_protocol()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.selected_alpn_protocol "ssl.SSLSocket.selected_alpn_protocol") method will return the agreed-upon protocol.
This method will raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") if [`HAS_ALPN`](https://docs.python.org/3/library/ssl.html#ssl.HAS_ALPN "ssl.HAS_ALPN") is `False`.
Added in version 3.5.

SSLContext.set_npn_protocols(_npn_protocols_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_npn_protocols "Link to this definition")

Specify which protocols the socket should advertise during the SSL/TLS handshake. It should be a list of strings, like `['http/1.1', 'spdy/2']`, ordered by preference. The selection of a protocol will happen during the handshake, and will play out according to the [`SSLSocket.selected_npn_protocol()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.selected_npn_protocol "ssl.SSLSocket.selected_npn_protocol") method will return the agreed-upon protocol.
This method will raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") if [`HAS_NPN`](https://docs.python.org/3/library/ssl.html#ssl.HAS_NPN "ssl.HAS_NPN") is `False`.
Added in version 3.3.
Deprecated since version 3.10: NPN has been superseded by ALPN

SSLContext.sni_callback[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.sni_callback "Link to this definition")

Register a callback function that will be called after the TLS Client Hello handshake message has been received by the SSL/TLS server when the TLS client specifies a server name indication. The server name indication mechanism is specified in
Only one callback can be set per `SSLContext`. If _sni_callback_ is set to `None` then the callback is disabled. Calling this function a subsequent time will disable the previously registered callback.
The callback function will be called with three arguments; the first being the [`ssl.SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket"), the second is a string that represents the server name that the client is intending to communicate (or [`None`](https://docs.python.org/3/library/constants.html#None "None") if the TLS Client Hello does not contain a server name) and the third argument is the original [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext"). The server name argument is text. For internationalized domain name, the server name is an IDN A-label (`"xn--pythn-mua.org"`).
A typical use of this callback is to change the [`ssl.SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket")’s [`SSLSocket.context`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.context "ssl.SSLSocket.context") attribute to a new object of type [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") representing a certificate chain that matches the server name.
Due to the early negotiation phase of the TLS connection, only limited methods and attributes are usable like [`SSLSocket.selected_alpn_protocol()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.selected_alpn_protocol "ssl.SSLSocket.selected_alpn_protocol") and [`SSLSocket.context`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.context "ssl.SSLSocket.context"). The [`SSLSocket.getpeercert()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert "ssl.SSLSocket.getpeercert"), [`SSLSocket.get_verified_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_verified_chain "ssl.SSLSocket.get_verified_chain"), [`SSLSocket.get_unverified_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_unverified_chain "ssl.SSLSocket.get_unverified_chain") [`SSLSocket.cipher()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.cipher "ssl.SSLSocket.cipher") and [`SSLSocket.compression()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.compression "ssl.SSLSocket.compression") methods require that the TLS connection has progressed beyond the TLS Client Hello and therefore will not return meaningful values nor can they be called safely.
The _sni_callback_ function must return `None` to allow the TLS negotiation to continue. If a TLS failure is required, a constant [`ALERT_DESCRIPTION_*`](https://docs.python.org/3/library/ssl.html#ssl.ALERT_DESCRIPTION_INTERNAL_ERROR "ssl.ALERT_DESCRIPTION_INTERNAL_ERROR") can be returned. Other return values will result in a TLS fatal error with `ALERT_DESCRIPTION_INTERNAL_ERROR`.
If an exception is raised from the _sni_callback_ function the TLS connection will terminate with a fatal TLS alert message [`ALERT_DESCRIPTION_HANDSHAKE_FAILURE`](https://docs.python.org/3/library/ssl.html#ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE "ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE").
This method will raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") if the OpenSSL library had OPENSSL_NO_TLSEXT defined when it was built.
Added in version 3.7.

SSLContext.set_servername_callback(_server_name_callback_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_servername_callback "Link to this definition")

This is a legacy API retained for backwards compatibility. When possible, you should use [`sni_callback`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.sni_callback "ssl.SSLContext.sni_callback") instead. The given _server_name_callback_ is similar to _sni_callback_ , except that when the server hostname is an IDN-encoded internationalized domain name, the _server_name_callback_ receives a decoded U-label (`"pythön.org"`).
If there is a decoding error on the server name, the TLS connection will terminate with an [`ALERT_DESCRIPTION_INTERNAL_ERROR`](https://docs.python.org/3/library/ssl.html#ssl.ALERT_DESCRIPTION_INTERNAL_ERROR "ssl.ALERT_DESCRIPTION_INTERNAL_ERROR") fatal TLS alert message to the client.
Added in version 3.4.

SSLContext.load_dh_params(_dhfile_ , _/_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_dh_params "Link to this definition")

Load the key generation parameters for Diffie-Hellman (DH) key exchange. Using DH key exchange improves forward secrecy at the expense of computational resources (both on the server and on the client). The _dhfile_ parameter should be the path to a file containing DH parameters in PEM format.
This setting doesn’t apply to client sockets. You can also use the [`OP_SINGLE_DH_USE`](https://docs.python.org/3/library/ssl.html#ssl.OP_SINGLE_DH_USE "ssl.OP_SINGLE_DH_USE") option to further improve security.
Added in version 3.3.

SSLContext.set_ecdh_curve(_curve_name_ , _/_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ecdh_curve "Link to this definition")

Set the curve name for Elliptic Curve-based Diffie-Hellman (ECDH) key exchange. ECDH is significantly faster than regular DH while arguably as secure. The _curve_name_ parameter should be a string describing a well-known elliptic curve, for example `prime256v1` for a widely supported curve.
This setting doesn’t apply to client sockets. You can also use the [`OP_SINGLE_ECDH_USE`](https://docs.python.org/3/library/ssl.html#ssl.OP_SINGLE_ECDH_USE "ssl.OP_SINGLE_ECDH_USE") option to further improve security.
This method is not available if [`HAS_ECDH`](https://docs.python.org/3/library/ssl.html#ssl.HAS_ECDH "ssl.HAS_ECDH") is `False`.
Added in version 3.3.
See also
Vincent Bernat.

SSLContext.wrap_socket(_sock_ , _server_side =False_, _do_handshake_on_connect =True_, _suppress_ragged_eofs =True_, _server_hostname =None_, _session =None_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "Link to this definition")

Wrap an existing Python socket _sock_ and return an instance of [`SSLContext.sslsocket_class`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.sslsocket_class "ssl.SSLContext.sslsocket_class") (default [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket")). The returned SSL socket is tied to the context, its settings and certificates. _sock_ must be a [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM") socket; other socket types are unsupported.
The parameter `server_side` is a boolean which identifies whether server-side or client-side behavior is desired from this socket.
For client-side sockets, the context construction is lazy; if the underlying socket isn’t connected yet, the context construction will be performed after `connect()` is called on the socket. For server-side sockets, if the socket has no remote peer, it is assumed to be a listening socket, and the server-side SSL wrapping is automatically performed on client connections accepted via the `accept()` method. The method may raise [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError").
On client connections, the optional parameter _server_hostname_ specifies the hostname of the service which we are connecting to. This allows a single server to host multiple SSL-based services with distinct certificates, quite similarly to HTTP virtual hosts. Specifying _server_hostname_ will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if _server_side_ is true.
The parameter `do_handshake_on_connect` specifies whether to do the SSL handshake automatically after doing a `socket.connect()`, or whether the application program will call it explicitly, by invoking the [`SSLSocket.do_handshake()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.do_handshake "ssl.SSLSocket.do_handshake") method. Calling `SSLSocket.do_handshake()` explicitly gives the program control over the blocking behavior of the socket I/O involved in the handshake.
The parameter `suppress_ragged_eofs` specifies how the `SSLSocket.recv()` method should signal unexpected EOF from the other end of the connection. If specified as [`True`](https://docs.python.org/3/library/constants.html#True "True") (the default), it returns a normal EOF (an empty bytes object) in response to unexpected EOF errors raised from the underlying socket; if [`False`](https://docs.python.org/3/library/constants.html#False "False"), it will raise the exceptions back to the caller.
_session_ , see [`session`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.session "ssl.SSLSocket.session").
To wrap an [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket") in another `SSLSocket`, use [`SSLContext.wrap_bio()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_bio "ssl.SSLContext.wrap_bio").
Changed in version 3.5: Always allow a server_hostname to be passed, even if OpenSSL does not have SNI.
Changed in version 3.6: _session_ argument was added.
Changed in version 3.7: The method returns an instance of [`SSLContext.sslsocket_class`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.sslsocket_class "ssl.SSLContext.sslsocket_class") instead of hard-coded [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket").

SSLContext.sslsocket_class[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.sslsocket_class "Link to this definition")

The return type of [`SSLContext.wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket"), defaults to [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket"). The attribute can be assigned to on instances of [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") in order to return a custom subclass of `SSLSocket`.
Added in version 3.7.

SSLContext.wrap_bio(_incoming_ , _outgoing_ , _server_side =False_, _server_hostname =None_, _session =None_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_bio "Link to this definition")

Wrap the BIO objects _incoming_ and _outgoing_ and return an instance of [`SSLContext.sslobject_class`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.sslobject_class "ssl.SSLContext.sslobject_class") (default [`SSLObject`](https://docs.python.org/3/library/ssl.html#ssl.SSLObject "ssl.SSLObject")). The SSL routines will read input data from the incoming BIO and write data to the outgoing BIO.
The _server_side_ , _server_hostname_ and _session_ parameters have the same meaning as in [`SSLContext.wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket").
Changed in version 3.6: _session_ argument was added.
Changed in version 3.7: The method returns an instance of [`SSLContext.sslobject_class`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.sslobject_class "ssl.SSLContext.sslobject_class") instead of hard-coded [`SSLObject`](https://docs.python.org/3/library/ssl.html#ssl.SSLObject "ssl.SSLObject").

SSLContext.sslobject_class[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.sslobject_class "Link to this definition")

The return type of [`SSLContext.wrap_bio()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_bio "ssl.SSLContext.wrap_bio"), defaults to [`SSLObject`](https://docs.python.org/3/library/ssl.html#ssl.SSLObject "ssl.SSLObject"). The attribute can be overridden on instance of class in order to return a custom subclass of `SSLObject`.
Added in version 3.7.

SSLContext.session_stats()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.session_stats "Link to this definition")

Get statistics about the SSL sessions created or managed by this context. A dictionary is returned which maps the names of each
Copy```
>>> stats = context.session_stats()
>>> stats['hits'], stats['misses']
(0, 0)

```


SSLContext.check_hostname[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "Link to this definition")

Whether to match the peer cert’s hostname in [`SSLSocket.do_handshake()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.do_handshake "ssl.SSLSocket.do_handshake"). The context’s [`verify_mode`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode "ssl.SSLContext.verify_mode") must be set to [`CERT_OPTIONAL`](https://docs.python.org/3/library/ssl.html#ssl.CERT_OPTIONAL "ssl.CERT_OPTIONAL") or [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED"), and you must pass _server_hostname_ to [`wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket") in order to match the hostname. Enabling hostname checking automatically sets `verify_mode` from [`CERT_NONE`](https://docs.python.org/3/library/ssl.html#ssl.CERT_NONE "ssl.CERT_NONE") to `CERT_REQUIRED`. It cannot be set back to `CERT_NONE` as long as hostname checking is enabled. The [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") protocol enables hostname checking by default. With other protocols, hostname checking must be enabled explicitly.
Example:
Copy```
import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname='www.verisign.com')
ssl_sock.connect(('www.verisign.com', 443))

```

Added in version 3.4.
Changed in version 3.7: [`verify_mode`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode "ssl.SSLContext.verify_mode") is now automatically changed to [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED") when hostname checking is enabled and `verify_mode` is [`CERT_NONE`](https://docs.python.org/3/library/ssl.html#ssl.CERT_NONE "ssl.CERT_NONE"). Previously the same operation would have failed with a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

SSLContext.keylog_filename[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.keylog_filename "Link to this definition")
