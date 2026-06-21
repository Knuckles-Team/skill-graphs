## SSL Sockets[¶](https://docs.python.org/3/library/ssl.html#ssl-sockets "Link to this heading")

_class_ ssl.SSLSocket(_socket.socket_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "Link to this definition")

SSL sockets provide the following methods of [Socket Objects](https://docs.python.org/3/library/socket.html#socket-objects):
  * [`accept()`](https://docs.python.org/3/library/socket.html#socket.socket.accept "socket.socket.accept")
  * [`bind()`](https://docs.python.org/3/library/socket.html#socket.socket.bind "socket.socket.bind")
  * [`close()`](https://docs.python.org/3/library/socket.html#socket.socket.close "socket.socket.close")
  * [`connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect")
  * [`detach()`](https://docs.python.org/3/library/socket.html#socket.socket.detach "socket.socket.detach")
  * [`fileno()`](https://docs.python.org/3/library/socket.html#socket.socket.fileno "socket.socket.fileno")
  * [`getpeername()`](https://docs.python.org/3/library/socket.html#socket.socket.getpeername "socket.socket.getpeername"), [`getsockname()`](https://docs.python.org/3/library/socket.html#socket.socket.getsockname "socket.socket.getsockname")
  * [`getsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.getsockopt "socket.socket.getsockopt"), [`setsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.setsockopt "socket.socket.setsockopt")
  * [`gettimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.gettimeout "socket.socket.gettimeout"), [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout"), [`setblocking()`](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "socket.socket.setblocking")
  * [`listen()`](https://docs.python.org/3/library/socket.html#socket.socket.listen "socket.socket.listen")
  * [`makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile")
  * [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv"), [`recv_into()`](https://docs.python.org/3/library/socket.html#socket.socket.recv_into "socket.socket.recv_into") (but passing a non-zero `flags` argument is not allowed)
  * [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send"), [`sendall()`](https://docs.python.org/3/library/socket.html#socket.socket.sendall "socket.socket.sendall") (with the same limitation)
  * [`sendfile()`](https://docs.python.org/3/library/socket.html#socket.socket.sendfile "socket.socket.sendfile") (but [`os.sendfile`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile") will be used for plain-text sockets only, else [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send") will be used)
  * [`shutdown()`](https://docs.python.org/3/library/socket.html#socket.socket.shutdown "socket.socket.shutdown")


However, since the SSL (and TLS) protocol has its own framing atop of TCP, the SSL sockets abstraction can, in certain respects, diverge from the specification of normal, OS-level sockets. See especially the [notes on non-blocking sockets](https://docs.python.org/3/library/ssl.html#ssl-nonblocking).
Instances of `SSLSocket` must be created using the [`SSLContext.wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket") method.
Changed in version 3.5: The `sendfile()` method was added.
Changed in version 3.5: The `shutdown()` does not reset the socket timeout each time bytes are received or sent. The socket timeout is now the maximum total duration of the shutdown.
Deprecated since version 3.6: It is deprecated to create a `SSLSocket` instance directly, use [`SSLContext.wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket") to wrap a socket.
Changed in version 3.7: `SSLSocket` instances must to created with [`wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket"). In earlier versions, it was possible to create instances directly. This was never documented or officially supported.
Changed in version 3.10: Python now uses `SSL_read_ex` and `SSL_write_ex` internally. The functions support reading and writing of data larger than 2 GB. Writing zero-length data no longer fails with a protocol violation error.
SSL sockets also have the following additional methods and attributes:

SSLSocket.read(_len =1024_, _buffer =None_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.read "Link to this definition")

Read up to _len_ bytes of data from the SSL socket and return the result as a `bytes` instance. If _buffer_ is specified, then read into the buffer instead, and return the number of bytes read.
Raise [`SSLWantReadError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantReadError "ssl.SSLWantReadError") or [`SSLWantWriteError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantWriteError "ssl.SSLWantWriteError") if the socket is [non-blocking](https://docs.python.org/3/library/ssl.html#ssl-nonblocking) and the read would block.
As at any time a re-negotiation is possible, a call to `read()` can also cause write operations.
Changed in version 3.5: The socket timeout is no longer reset each time bytes are received or sent. The socket timeout is now the maximum total duration to read up to _len_ bytes.
Deprecated since version 3.6: Use `recv()` instead of `read()`.

SSLSocket.write(_data_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.write "Link to this definition")

Write _data_ to the SSL socket and return the number of bytes written. The _data_ argument must be an object supporting the buffer interface.
Raise [`SSLWantReadError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantReadError "ssl.SSLWantReadError") or [`SSLWantWriteError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantWriteError "ssl.SSLWantWriteError") if the socket is [non-blocking](https://docs.python.org/3/library/ssl.html#ssl-nonblocking) and the write would block.
As at any time a re-negotiation is possible, a call to `write()` can also cause read operations.
Changed in version 3.5: The socket timeout is no longer reset each time bytes are received or sent. The socket timeout is now the maximum total duration to write _data_.
Deprecated since version 3.6: Use `send()` instead of `write()`.
Note
The [`read()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.read "ssl.SSLSocket.read") and [`write()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.write "ssl.SSLSocket.write") methods are the low-level methods that read and write unencrypted, application-level data and decrypt/encrypt it to encrypted, wire-level data. These methods require an active SSL connection, i.e. the handshake was completed and [`SSLSocket.unwrap()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.unwrap "ssl.SSLSocket.unwrap") was not called.
Normally you should use the socket API methods like [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv") and [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send") instead of these methods.

SSLSocket.do_handshake(_block =False_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.do_handshake "Link to this definition")

Perform the SSL setup handshake.
If _block_ is true and the timeout obtained by [`gettimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.gettimeout "socket.socket.gettimeout") is zero, the socket is set in blocking mode until the handshake is performed.
Changed in version 3.4: The handshake method also performs `match_hostname()` when the [`check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") attribute of the socket’s [`context`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.context "ssl.SSLSocket.context") is true.
Changed in version 3.5: The socket timeout is no longer reset each time bytes are received or sent. The socket timeout is now the maximum total duration of the handshake.
Changed in version 3.7: Hostname or IP address is matched by OpenSSL during handshake. The function `match_hostname()` is no longer used. In case OpenSSL refuses a hostname or IP address, the handshake is aborted early and a TLS alert message is sent to the peer.

SSLSocket.getpeercert(_binary_form =False_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert "Link to this definition")

If there is no certificate for the peer on the other end of the connection, return `None`. If the SSL handshake hasn’t been done yet, raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").
If the `binary_form` parameter is [`False`](https://docs.python.org/3/library/constants.html#False "False"), and a certificate was received from the peer, this method returns a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") instance. If the certificate was not validated, the dict is empty. If the certificate was validated, it returns a dict with several keys, amongst them `subject` (the principal for which the certificate was issued) and `issuer` (the principal issuing the certificate). If a certificate contains an instance of the _Subject Alternative Name_ extension (see `subjectAltName` key in the dictionary.
The `subject` and `issuer` fields are tuples containing the sequence of relative distinguished names (RDNs) given in the certificate’s data structure for the respective fields, and each RDN is a sequence of name-value pairs. Here is a real-world example:
Copy```
{'issuer': ((('countryName', 'IL'),),
            (('organizationName', 'StartCom Ltd.'),),
            (('organizationalUnitName',
              'Secure Digital Certificate Signing'),),
            (('commonName',
              'StartCom Class 2 Primary Intermediate Server CA'),)),
 'notAfter': 'Nov 22 08:15:19 2013 GMT',
 'notBefore': 'Nov 21 03:09:52 2011 GMT',
 'serialNumber': '95F0',
 'subject': ((('description', '571208-SLe257oHY9fVQ07Z'),),
             (('countryName', 'US'),),
             (('stateOrProvinceName', 'California'),),
             (('localityName', 'San Francisco'),),
             (('organizationName', 'Electronic Frontier Foundation, Inc.'),),
             (('commonName', '*.eff.org'),),
             (('emailAddress', 'hostmaster@eff.org'),)),
 'subjectAltName': (('DNS', '*.eff.org'), ('DNS', 'eff.org')),
 'version': 3}

```

If the `binary_form` parameter is [`True`](https://docs.python.org/3/library/constants.html#True "True"), and a certificate was provided, this method returns the DER-encoded form of the entire certificate as a sequence of bytes, or [`None`](https://docs.python.org/3/library/constants.html#None "None") if the peer did not provide a certificate. Whether the peer provides a certificate depends on the SSL socket’s role:
  * for a client SSL socket, the server will always provide a certificate, regardless of whether validation was required;
  * for a server SSL socket, the client will only provide a certificate when requested by the server; therefore `getpeercert()` will return [`None`](https://docs.python.org/3/library/constants.html#None "None") if you used [`CERT_NONE`](https://docs.python.org/3/library/ssl.html#ssl.CERT_NONE "ssl.CERT_NONE") (rather than [`CERT_OPTIONAL`](https://docs.python.org/3/library/ssl.html#ssl.CERT_OPTIONAL "ssl.CERT_OPTIONAL") or [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED")).


See also [`SSLContext.check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname").
Changed in version 3.2: The returned dictionary includes additional items such as `issuer` and `notBefore`.
Changed in version 3.4: [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised when the handshake isn’t done. The returned dictionary includes additional X509v3 extension items such as `crlDistributionPoints`, `caIssuers` and `OCSP` URIs.
Changed in version 3.9: IPv6 address strings no longer have a trailing new line.

SSLSocket.get_verified_chain()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_verified_chain "Link to this definition")

Returns verified certificate chain provided by the other end of the SSL channel as a list of DER-encoded bytes. If certificate verification was disabled method acts the same as [`get_unverified_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_unverified_chain "ssl.SSLSocket.get_unverified_chain").
Added in version 3.13.

SSLSocket.get_unverified_chain()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_unverified_chain "Link to this definition")

Returns raw certificate chain provided by the other end of the SSL channel as a list of DER-encoded bytes.
Added in version 3.13.

SSLSocket.cipher()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.cipher "Link to this definition")

Returns a three-value tuple containing the name of the cipher being used, the version of the SSL protocol that defines its use, and the number of secret bits being used. If no connection has been established, returns `None`.

SSLSocket.shared_ciphers()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.shared_ciphers "Link to this definition")

Return the list of ciphers available in both the client and server. Each entry of the returned list is a three-value tuple containing the name of the cipher, the version of the SSL protocol that defines its use, and the number of secret bits the cipher uses. `shared_ciphers()` returns `None` if no connection has been established or the socket is a client socket.
Added in version 3.5.

SSLSocket.compression()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.compression "Link to this definition")

Return the compression algorithm being used as a string, or `None` if the connection isn’t compressed.
If the higher-level protocol supports its own compression mechanism, you can use [`OP_NO_COMPRESSION`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_COMPRESSION "ssl.OP_NO_COMPRESSION") to disable SSL-level compression.
Added in version 3.3.

SSLSocket.get_channel_binding(_cb_type ='tls-unique'_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_channel_binding "Link to this definition")

Get channel binding data for current connection, as a bytes object. Returns `None` if not connected or the handshake has not been completed.
The _cb_type_ parameter allow selection of the desired channel binding type. Valid channel binding types are listed in the [`CHANNEL_BINDING_TYPES`](https://docs.python.org/3/library/ssl.html#ssl.CHANNEL_BINDING_TYPES "ssl.CHANNEL_BINDING_TYPES") list. Currently only the ‘tls-unique’ channel binding, defined by [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised if an unsupported channel binding type is requested.
Added in version 3.3.

SSLSocket.selected_alpn_protocol()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.selected_alpn_protocol "Link to this definition")

Return the protocol that was selected during the TLS handshake. If [`SSLContext.set_alpn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_alpn_protocols "ssl.SSLContext.set_alpn_protocols") was not called, if the other party does not support ALPN, if this socket does not support any of the client’s proposed protocols, or if the handshake has not happened yet, `None` is returned.
Added in version 3.5.

SSLSocket.selected_npn_protocol()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.selected_npn_protocol "Link to this definition")

Return the higher-level protocol that was selected during the TLS/SSL handshake. If [`SSLContext.set_npn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_npn_protocols "ssl.SSLContext.set_npn_protocols") was not called, or if the other party does not support NPN, or if the handshake has not yet happened, this will return `None`.
Added in version 3.3.
Deprecated since version 3.10: NPN has been superseded by ALPN

SSLSocket.unwrap()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.unwrap "Link to this definition")

Performs the SSL shutdown handshake, which removes the TLS layer from the underlying socket, and returns the underlying socket object. This can be used to go from encrypted operation over a connection to unencrypted. The returned socket should always be used for further communication with the other side of the connection, rather than the original socket.

SSLSocket.verify_client_post_handshake()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.verify_client_post_handshake "Link to this definition")

Requests post-handshake authentication (PHA) from a TLS 1.3 client. PHA can only be initiated for a TLS 1.3 connection from a server-side socket, after the initial TLS handshake and with PHA enabled on both sides, see [`SSLContext.post_handshake_auth`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.post_handshake_auth "ssl.SSLContext.post_handshake_auth").
The method does not perform a cert exchange immediately. The server-side sends a CertificateRequest during the next write event and expects the client to respond with a certificate on the next read event.
If any precondition isn’t met (e.g. not TLS 1.3, PHA not enabled), an [`SSLError`](https://docs.python.org/3/library/ssl.html#ssl.SSLError "ssl.SSLError") is raised.
Note
Only available with OpenSSL 1.1.1 and TLS 1.3 enabled. Without TLS 1.3 support, the method raises [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").
Added in version 3.8.

SSLSocket.version()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.version "Link to this definition")

Return the actual SSL protocol version negotiated by the connection as a string, or `None` if no secure connection is established. As of this writing, possible return values include `"SSLv2"`, `"SSLv3"`, `"TLSv1"`, `"TLSv1.1"` and `"TLSv1.2"`. Recent OpenSSL versions may define more return values.
Added in version 3.5.

SSLSocket.pending()[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.pending "Link to this definition")

Returns the number of already decrypted bytes available for read, pending on the connection.

SSLSocket.context[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.context "Link to this definition")

The [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") object this SSL socket is tied to.
Added in version 3.2.

SSLSocket.server_side[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.server_side "Link to this definition")

A boolean which is `True` for server-side sockets and `False` for client-side sockets.
Added in version 3.2.

SSLSocket.server_hostname[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.server_hostname "Link to this definition")

Hostname of the server: [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") type, or `None` for server-side socket or if the hostname was not specified in the constructor.
Added in version 3.2.
Changed in version 3.7: The attribute is now always ASCII text. When `server_hostname` is an internationalized domain name (IDN), this attribute now stores the A-label form (`"xn--pythn-mua.org"`), rather than the U-label form (`"pythön.org"`).

SSLSocket.session[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.session "Link to this definition")

The [`SSLSession`](https://docs.python.org/3/library/ssl.html#ssl.SSLSession "ssl.SSLSession") for this SSL connection. The session is available for client and server side sockets after the TLS handshake has been performed. For client sockets the session can be set before [`do_handshake()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.do_handshake "ssl.SSLSocket.do_handshake") has been called to reuse a session.
Added in version 3.6.

SSLSocket.session_reused[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.session_reused "Link to this definition")

Added in version 3.6.
## SSL Contexts[¶](https://docs.python.org/3/library/ssl.html#ssl-contexts "Link to this heading")
Added in version 3.2.
An SSL context holds various data longer-lived than single SSL connections, such as SSL configuration options, certificate(s) and private key(s). It also manages a cache of SSL sessions for server-side sockets, in order to speed up repeated connections from the same clients.

_class_ ssl.SSLContext(_protocol =None_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "Link to this definition")

Create a new SSL context. You may pass _protocol_ which must be one of the `PROTOCOL_*` constants defined in this module. The parameter specifies which version of the SSL protocol to use. Typically, the server chooses a particular protocol version, and the client must adapt to the server’s choice. Most of the versions are not interoperable with the other versions. If not specified, the default is [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS"); it provides the most compatibility with other versions.
Here’s a table showing which versions in a client (down the side) can connect to which versions in a server (along the top):
_client_ / **server** | **SSLv2** | **SSLv3** | **TLS** [[3]](https://docs.python.org/3/library/ssl.html#id9) | **TLSv1** | **TLSv1.1** | **TLSv1.2**
---|---|---|---|---|---|---
_SSLv2_ | yes | no | no [[1]](https://docs.python.org/3/library/ssl.html#id7) | no | no | no
_SSLv3_ | no | yes | no [[2]](https://docs.python.org/3/library/ssl.html#id8) | no | no | no
_TLS_ (_SSLv23_) [[3]](https://docs.python.org/3/library/ssl.html#id9) | no [[1]](https://docs.python.org/3/library/ssl.html#id7) | no [[2]](https://docs.python.org/3/library/ssl.html#id8) | yes | yes | yes | yes
_TLSv1_ | no | no | yes | yes | no | no
_TLSv1.1_ | no | no | yes | no | yes | no
_TLSv1.2_ | no | no | yes | no | no | yes
Footnotes
[1] ([1](https://docs.python.org/3/library/ssl.html#id2),[2](https://docs.python.org/3/library/ssl.html#id5))
`SSLContext` disables SSLv2 with [`OP_NO_SSLv2`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv2 "ssl.OP_NO_SSLv2") by default.
[2] ([1](https://docs.python.org/3/library/ssl.html#id3),[2](https://docs.python.org/3/library/ssl.html#id6))
`SSLContext` disables SSLv3 with [`OP_NO_SSLv3`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv3 "ssl.OP_NO_SSLv3") by default.
[3] ([1](https://docs.python.org/3/library/ssl.html#id1),[2](https://docs.python.org/3/library/ssl.html#id4))
TLS 1.3 protocol will be available with [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS") in OpenSSL >= 1.1.1. There is no dedicated PROTOCOL constant for just TLS 1.3.
See also
[`create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context") lets the `ssl` module choose security settings for a given purpose.
Changed in version 3.6: The context is created with secure default values. The options [`OP_NO_COMPRESSION`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_COMPRESSION "ssl.OP_NO_COMPRESSION"), [`OP_CIPHER_SERVER_PREFERENCE`](https://docs.python.org/3/library/ssl.html#ssl.OP_CIPHER_SERVER_PREFERENCE "ssl.OP_CIPHER_SERVER_PREFERENCE"), [`OP_SINGLE_DH_USE`](https://docs.python.org/3/library/ssl.html#ssl.OP_SINGLE_DH_USE "ssl.OP_SINGLE_DH_USE"), [`OP_SINGLE_ECDH_USE`](https://docs.python.org/3/library/ssl.html#ssl.OP_SINGLE_ECDH_USE "ssl.OP_SINGLE_ECDH_USE"), [`OP_NO_SSLv2`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv2 "ssl.OP_NO_SSLv2"), and [`OP_NO_SSLv3`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv3 "ssl.OP_NO_SSLv3") (except for [`PROTOCOL_SSLv3`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_SSLv3 "ssl.PROTOCOL_SSLv3")) are set by default. The initial cipher suite list contains only `HIGH` ciphers, no `NULL` ciphers and no `MD5` ciphers.
Deprecated since version 3.10: `SSLContext` without protocol argument is deprecated. The context class will either require [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") or [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "ssl.PROTOCOL_TLS_SERVER") protocol in the future.
Changed in version 3.10: The default cipher suites now include only secure AES and ChaCha20 ciphers with forward secrecy and security level 2. RSA and DH keys with less than 2048 bits and ECC keys with less than 224 bits are prohibited. [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS"), [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT"), and [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "ssl.PROTOCOL_TLS_SERVER") use TLS 1.2 as minimum TLS version.
