
Write TLS keys to a keylog file, whenever key material is generated or received. The keylog file is designed for debugging purposes only. The file format is specified by NSS and used by many traffic analyzers such as Wireshark. The log file is opened in append-only mode. Writes are synchronized between threads, but not between processes.
Added in version 3.8.

SSLContext.maximum_version[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.maximum_version "Link to this definition")

A [`TLSVersion`](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion "ssl.TLSVersion") enum member representing the highest supported TLS version. The value defaults to [`TLSVersion.MAXIMUM_SUPPORTED`](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.MAXIMUM_SUPPORTED "ssl.TLSVersion.MAXIMUM_SUPPORTED"). The attribute is read-only for protocols other than [`PROTOCOL_TLS`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS "ssl.PROTOCOL_TLS"), [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT"), and [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "ssl.PROTOCOL_TLS_SERVER").
The attributes `maximum_version`, [`minimum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.minimum_version "ssl.SSLContext.minimum_version") and [`SSLContext.options`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.options "ssl.SSLContext.options") all affect the supported SSL and TLS versions of the context. The implementation does not prevent invalid combination. For example a context with [`OP_NO_TLSv1_2`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_TLSv1_2 "ssl.OP_NO_TLSv1_2") in `options` and `maximum_version` set to [`TLSVersion.TLSv1_2`](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.TLSv1_2 "ssl.TLSVersion.TLSv1_2") will not be able to establish a TLS 1.2 connection.
Added in version 3.7.

SSLContext.minimum_version[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.minimum_version "Link to this definition")

Like [`SSLContext.maximum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.maximum_version "ssl.SSLContext.maximum_version") except it is the lowest supported version or [`TLSVersion.MINIMUM_SUPPORTED`](https://docs.python.org/3/library/ssl.html#ssl.TLSVersion.MINIMUM_SUPPORTED "ssl.TLSVersion.MINIMUM_SUPPORTED").
Added in version 3.7.

SSLContext.num_tickets[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.num_tickets "Link to this definition")

Control the number of TLS 1.3 session tickets of a [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "ssl.PROTOCOL_TLS_SERVER") context. The setting has no impact on TLS 1.0 to 1.2 connections.
Added in version 3.8.

SSLContext.options[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.options "Link to this definition")

An integer representing the set of SSL options enabled on this context. The default value is [`OP_ALL`](https://docs.python.org/3/library/ssl.html#ssl.OP_ALL "ssl.OP_ALL"), but you can specify other options such as [`OP_NO_SSLv2`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv2 "ssl.OP_NO_SSLv2") by ORing them together.
Changed in version 3.6: `SSLContext.options` returns [`Options`](https://docs.python.org/3/library/ssl.html#ssl.Options "ssl.Options") flags:
Copy```
>>> ssl.create_default_context().options
<Options.OP_ALL|OP_NO_SSLv3|OP_NO_SSLv2|OP_NO_COMPRESSION: 2197947391>

```

Deprecated since version 3.7: All `OP_NO_SSL*` and `OP_NO_TLS*` options have been deprecated since Python 3.7. Use [`SSLContext.minimum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.minimum_version "ssl.SSLContext.minimum_version") and [`SSLContext.maximum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.maximum_version "ssl.SSLContext.maximum_version") instead.

SSLContext.post_handshake_auth[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.post_handshake_auth "Link to this definition")

Enable TLS 1.3 post-handshake client authentication. Post-handshake auth is disabled by default and a server can only request a TLS client certificate during the initial handshake. When enabled, a server may request a TLS client certificate at any time after the handshake.
When enabled on client-side sockets, the client signals the server that it supports post-handshake authentication.
When enabled on server-side sockets, [`SSLContext.verify_mode`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode "ssl.SSLContext.verify_mode") must be set to [`CERT_OPTIONAL`](https://docs.python.org/3/library/ssl.html#ssl.CERT_OPTIONAL "ssl.CERT_OPTIONAL") or [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED"), too. The actual client cert exchange is delayed until [`SSLSocket.verify_client_post_handshake()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.verify_client_post_handshake "ssl.SSLSocket.verify_client_post_handshake") is called and some I/O is performed.
Added in version 3.8.

SSLContext.protocol[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.protocol "Link to this definition")

The protocol version chosen when constructing the context. This attribute is read-only.

SSLContext.hostname_checks_common_name[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.hostname_checks_common_name "Link to this definition")

Whether [`check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") falls back to verify the cert’s subject common name in the absence of a subject alternative name extension (default: true).
Added in version 3.7.
Changed in version 3.10: The flag had no effect with OpenSSL before version 1.1.1l. Python 3.8.9, 3.9.3, and 3.10 include workarounds for previous versions.

SSLContext.security_level[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.security_level "Link to this definition")

An integer representing the
Added in version 3.10.

SSLContext.verify_flags[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_flags "Link to this definition")

The flags for certificate verification operations. You can set flags like [`VERIFY_CRL_CHECK_LEAF`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_CRL_CHECK_LEAF "ssl.VERIFY_CRL_CHECK_LEAF") by ORing them together. By default OpenSSL does neither require nor verify certificate revocation lists (CRLs).
Added in version 3.4.
Changed in version 3.6: `SSLContext.verify_flags` returns [`VerifyFlags`](https://docs.python.org/3/library/ssl.html#ssl.VerifyFlags "ssl.VerifyFlags") flags:
Copy```
>>> ssl.create_default_context().verify_flags
<VerifyFlags.VERIFY_X509_TRUSTED_FIRST: 32768>

```


SSLContext.verify_mode[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.verify_mode "Link to this definition")

Whether to try to verify other peers’ certificates and how to behave if verification fails. This attribute must be one of [`CERT_NONE`](https://docs.python.org/3/library/ssl.html#ssl.CERT_NONE "ssl.CERT_NONE"), [`CERT_OPTIONAL`](https://docs.python.org/3/library/ssl.html#ssl.CERT_OPTIONAL "ssl.CERT_OPTIONAL") or [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED").
Changed in version 3.6: `SSLContext.verify_mode` returns [`VerifyMode`](https://docs.python.org/3/library/ssl.html#ssl.VerifyMode "ssl.VerifyMode") enum:
Copy```
>>> ssl.create_default_context().verify_mode
<VerifyMode.CERT_REQUIRED: 2>

```


SSLContext.set_psk_client_callback(_callback_)[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_psk_client_callback "Link to this definition")

Enables TLS-PSK (pre-shared key) authentication on a client-side connection.
In general, certificate based authentication should be preferred over this method.
The parameter `callback` is a callable object with the signature: `def callback(hint: str | None) -> tuple[str | None, bytes]`. The `hint` parameter is an optional identity hint sent by the server. The return value is a tuple in the form (client-identity, psk). Client-identity is an optional string which may be used by the server to select a corresponding PSK for the client. The string must be less than or equal to `256` octets when UTF-8 encoded. PSK is a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) representing the pre-shared key. Return a zero length PSK to reject the connection.
Setting `callback` to [`None`](https://docs.python.org/3/library/constants.html#None "None") removes any existing callback.
Note
When using TLS 1.3:
  * the `hint` parameter is always [`None`](https://docs.python.org/3/library/constants.html#None "None").
  * client-identity must be a non-empty string.


Example usage:
Copy```
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
context.maximum_version = ssl.TLSVersion.TLSv1_2
context.set_ciphers('PSK')
