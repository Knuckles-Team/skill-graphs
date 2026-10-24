## Notes on non-blocking sockets[¶](https://docs.python.org/3/library/ssl.html#notes-on-non-blocking-sockets "Link to this heading")
SSL sockets behave slightly different than regular sockets in non-blocking mode. When working with non-blocking sockets, there are thus several things you need to be aware of:
  * Most [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket") methods will raise either [`SSLWantWriteError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantWriteError "ssl.SSLWantWriteError") or [`SSLWantReadError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantReadError "ssl.SSLWantReadError") instead of [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") if an I/O operation would block. `SSLWantReadError` will be raised if a read operation on the underlying socket is necessary, and `SSLWantWriteError` for a write operation on the underlying socket. Note that attempts to _write_ to an SSL socket may require _reading_ from the underlying socket first, and attempts to _read_ from the SSL socket may require a prior _write_ to the underlying socket.
Changed in version 3.5: In earlier Python versions, the `SSLSocket.send()` method returned zero instead of raising [`SSLWantWriteError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantWriteError "ssl.SSLWantWriteError") or [`SSLWantReadError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantReadError "ssl.SSLWantReadError").
  * Calling [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select") tells you that the OS-level socket can be read from (or written to), but it does not imply that there is sufficient data at the upper SSL layer. For example, only part of an SSL frame might have arrived. Therefore, you must be ready to handle `SSLSocket.recv()` and `SSLSocket.send()` failures, and retry after another call to `select()`.
  * Conversely, since the SSL layer has its own framing, a SSL socket may still have data available for reading without [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select") being aware of it. Therefore, you should first call `SSLSocket.recv()` to drain any potentially available data, and then only block on a `select()` call if still necessary.
(of course, similar provisions apply when using other primitives such as [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll"), or those in the [`selectors`](https://docs.python.org/3/library/selectors.html#module-selectors "selectors: High-level I/O multiplexing.") module)
  * The SSL handshake itself will be non-blocking: the [`SSLSocket.do_handshake()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.do_handshake "ssl.SSLSocket.do_handshake") method has to be retried until it returns successfully. Here is a synopsis using [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select") to wait for the socket’s readiness:
Copy```
while True:
    try:
        sock.do_handshake()
        break
    except ssl.SSLWantReadError:
        select.select([sock], [], [])
    except ssl.SSLWantWriteError:
        select.select([], [sock], [])

```



See also
The [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") module supports [non-blocking SSL sockets](https://docs.python.org/3/library/ssl.html#ssl-nonblocking) and provides a higher level [Streams API](https://docs.python.org/3/library/asyncio-stream.html#asyncio-streams). It polls for events using the [`selectors`](https://docs.python.org/3/library/selectors.html#module-selectors "selectors: High-level I/O multiplexing.") module and handles [`SSLWantWriteError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantWriteError "ssl.SSLWantWriteError"), [`SSLWantReadError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantReadError "ssl.SSLWantReadError") and [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") exceptions. It runs the SSL handshake asynchronously as well.
## Memory BIO Support[¶](https://docs.python.org/3/library/ssl.html#memory-bio-support "Link to this heading")
Added in version 3.5.
Ever since the SSL module was introduced in Python 2.6, the [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket") class has provided two related but distinct areas of functionality:
  * SSL protocol handling
  * Network IO


The network IO API is identical to that provided by [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket"), from which [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket") also inherits. This allows an SSL socket to be used as a drop-in replacement for a regular socket, making it very easy to add SSL support to an existing application.
Combining SSL protocol handling and network IO usually works well, but there are some cases where it doesn’t. An example is async IO frameworks that want to use a different IO multiplexing model than the “select/poll on a file descriptor” (readiness based) model that is assumed by [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket") and by the internal OpenSSL socket IO routines. This is mostly relevant for platforms like Windows where this model is not efficient. For this purpose, a reduced scope variant of [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket") called [`SSLObject`](https://docs.python.org/3/library/ssl.html#ssl.SSLObject "ssl.SSLObject") is provided.

_class_ ssl.SSLObject[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLObject "Link to this definition")

A reduced-scope variant of [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket") representing an SSL protocol instance that does not contain any network IO methods. This class is typically used by framework authors that want to implement asynchronous IO for SSL through memory buffers.
This class implements an interface on top of a low-level SSL object as implemented by OpenSSL. This object captures the state of an SSL connection but does not provide any network IO itself. IO needs to be performed through separate “BIO” objects which are OpenSSL’s IO abstraction layer.
This class has no public constructor. An `SSLObject` instance must be created using the [`wrap_bio()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_bio "ssl.SSLContext.wrap_bio") method. This method will create the `SSLObject` instance and bind it to a pair of BIOs. The _incoming_ BIO is used to pass data from Python to the SSL protocol instance, while the _outgoing_ BIO is used to pass data the other way around.
The following methods are available:
  * [`context`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.context "ssl.SSLSocket.context")
  * [`server_side`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.server_side "ssl.SSLSocket.server_side")
  * [`server_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.server_hostname "ssl.SSLSocket.server_hostname")
  * [`session`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.session "ssl.SSLSocket.session")
  * [`session_reused`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.session_reused "ssl.SSLSocket.session_reused")
  * [`read()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.read "ssl.SSLSocket.read")
  * [`write()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.write "ssl.SSLSocket.write")
  * [`getpeercert()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert "ssl.SSLSocket.getpeercert")
  * [`get_verified_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_verified_chain "ssl.SSLSocket.get_verified_chain")
  * [`get_unverified_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_unverified_chain "ssl.SSLSocket.get_unverified_chain")
  * [`selected_alpn_protocol()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.selected_alpn_protocol "ssl.SSLSocket.selected_alpn_protocol")
  * [`selected_npn_protocol()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.selected_npn_protocol "ssl.SSLSocket.selected_npn_protocol")
  * [`cipher()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.cipher "ssl.SSLSocket.cipher")
  * [`shared_ciphers()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.shared_ciphers "ssl.SSLSocket.shared_ciphers")
  * [`compression()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.compression "ssl.SSLSocket.compression")
  * [`pending()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.pending "ssl.SSLSocket.pending")
  * [`do_handshake()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.do_handshake "ssl.SSLSocket.do_handshake")
  * [`verify_client_post_handshake()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.verify_client_post_handshake "ssl.SSLSocket.verify_client_post_handshake")
  * [`unwrap()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.unwrap "ssl.SSLSocket.unwrap")
  * [`get_channel_binding()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_channel_binding "ssl.SSLSocket.get_channel_binding")
  * [`version()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.version "ssl.SSLSocket.version")


When compared to [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket"), this object lacks the following features:
  * Any form of network IO; `recv()` and `send()` read and write only to the underlying [`MemoryBIO`](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO "ssl.MemoryBIO") buffers.
  * There is no _do_handshake_on_connect_ machinery. You must always manually call [`do_handshake()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.do_handshake "ssl.SSLSocket.do_handshake") to start the handshake.
  * There is no handling of _suppress_ragged_eofs_. All end-of-file conditions that are in violation of the protocol are reported via the [`SSLEOFError`](https://docs.python.org/3/library/ssl.html#ssl.SSLEOFError "ssl.SSLEOFError") exception.
  * The method [`unwrap()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.unwrap "ssl.SSLSocket.unwrap") call does not return anything, unlike for an SSL socket where it returns the underlying socket.
  * The _server_name_callback_ callback passed to [`SSLContext.set_servername_callback()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_servername_callback "ssl.SSLContext.set_servername_callback") will get an `SSLObject` instance instead of a [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket") instance as its first parameter.


Some notes related to the use of `SSLObject`:
  * All IO on an `SSLObject` is [non-blocking](https://docs.python.org/3/library/ssl.html#ssl-nonblocking). This means that for example [`read()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.read "ssl.SSLSocket.read") will raise an [`SSLWantReadError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantReadError "ssl.SSLWantReadError") if it needs more data than the incoming BIO has available.


Changed in version 3.7: `SSLObject` instances must be created with [`wrap_bio()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_bio "ssl.SSLContext.wrap_bio"). In earlier versions, it was possible to create instances directly. This was never documented or officially supported.
An SSLObject communicates with the outside world using memory buffers. The class [`MemoryBIO`](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO "ssl.MemoryBIO") provides a memory buffer that can be used for this purpose. It wraps an OpenSSL memory BIO (Basic IO) object:

_class_ ssl.MemoryBIO[¶](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO "Link to this definition")

A memory buffer that can be used to pass data between Python and an SSL protocol instance.

pending[¶](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO.pending "Link to this definition")

Return the number of bytes currently in the memory buffer.

eof[¶](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO.eof "Link to this definition")

A boolean indicating whether the memory BIO is current at the end-of-file position.

read(_n =-1_, _/_)[¶](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO.read "Link to this definition")

Read up to _n_ bytes from the memory buffer. If _n_ is not specified or negative, all bytes are returned.

write(_buf_ , _/_)[¶](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO.write "Link to this definition")

Write the bytes from _buf_ to the memory BIO. The _buf_ argument must be an object supporting the buffer protocol.
The return value is the number of bytes written, which is always equal to the length of _buf_.

write_eof()[¶](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO.write_eof "Link to this definition")

Write an EOF marker to the memory BIO. After this method has been called, it is illegal to call [`write()`](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO.write "ssl.MemoryBIO.write"). The attribute [`eof`](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO.eof "ssl.MemoryBIO.eof") will become true after all data currently in the buffer has been read.
## SSL session[¶](https://docs.python.org/3/library/ssl.html#ssl-session "Link to this heading")
Added in version 3.6.

_class_ ssl.SSLSession[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSession "Link to this definition")

Session object used by [`session`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.session "ssl.SSLSocket.session").

id[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSession.id "Link to this definition")


time[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSession.time "Link to this definition")


timeout[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSession.timeout "Link to this definition")


ticket_lifetime_hint[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSession.ticket_lifetime_hint "Link to this definition")


has_ticket[¶](https://docs.python.org/3/library/ssl.html#ssl.SSLSession.has_ticket "Link to this definition")

## Security considerations[¶](https://docs.python.org/3/library/ssl.html#security-considerations "Link to this heading")
### Best defaults[¶](https://docs.python.org/3/library/ssl.html#best-defaults "Link to this heading")
For **client use** , if you don’t have any special requirements for your security policy, it is highly recommended that you use the [`create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context") function to create your SSL context. It will load the system’s trusted CA certificates, enable certificate validation and hostname checking, and try to choose reasonably secure protocol and cipher settings.
For example, here is how you would use the [`smtplib.SMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "smtplib.SMTP") class to create a trusted, secure connection to a SMTP server:
Copy```
>>> import ssl, smtplib
>>> smtp = smtplib.SMTP("mail.python.org", port=587)
>>> context = ssl.create_default_context()
>>> smtp.starttls(context=context)
(220, b'2.0.0 Ready to start TLS')

```

If a client certificate is needed for the connection, it can be added with [`SSLContext.load_cert_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain "ssl.SSLContext.load_cert_chain").
By contrast, if you create the SSL context by calling the [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") constructor yourself, it will not have certificate validation nor hostname checking enabled by default. If you do so, please read the paragraphs below to achieve a good security level.
### Manual settings[¶](https://docs.python.org/3/library/ssl.html#manual-settings "Link to this heading")
#### Verifying certificates[¶](https://docs.python.org/3/library/ssl.html#verifying-certificates "Link to this heading")
When calling the [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") constructor directly, [`CERT_NONE`](https://docs.python.org/3/library/ssl.html#ssl.CERT_NONE "ssl.CERT_NONE") is the default. Since it does not authenticate the other peer, it can be insecure, especially in client mode where most of the time you would like to ensure the authenticity of the server you’re talking to. Therefore, when in client mode, it is highly recommended to use [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED"). However, it is in itself not sufficient; you also have to check that the server certificate, which can be obtained by calling [`SSLSocket.getpeercert()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert "ssl.SSLSocket.getpeercert"), matches the desired service. For many protocols and applications, the service can be identified by the hostname. This common check is automatically performed when [`SSLContext.check_hostname`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.check_hostname "ssl.SSLContext.check_hostname") is enabled.
Changed in version 3.7: Hostname matchings is now performed by OpenSSL. Python no longer uses `match_hostname()`.
In server mode, if you want to authenticate your clients using the SSL layer (rather than using a higher-level authentication mechanism), you’ll also have to specify [`CERT_REQUIRED`](https://docs.python.org/3/library/ssl.html#ssl.CERT_REQUIRED "ssl.CERT_REQUIRED") and similarly check the client certificate.
#### Protocol versions[¶](https://docs.python.org/3/library/ssl.html#protocol-versions "Link to this heading")
SSL versions 2 and 3 are considered insecure and are therefore dangerous to use. If you want maximum compatibility between clients and servers, it is recommended to use [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") or [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "ssl.PROTOCOL_TLS_SERVER") as the protocol version. SSLv2 and SSLv3 are disabled by default.
Copy```
>>> client_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
>>> client_context.minimum_version = ssl.TLSVersion.TLSv1_3
>>> client_context.maximum_version = ssl.TLSVersion.TLSv1_3

```

The SSL context created above will only allow TLSv1.3 and later (if supported by your system) connections to a server. [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") implies certificate validation and hostname checks by default. You have to load certificates into the context.
#### Cipher selection[¶](https://docs.python.org/3/library/ssl.html#cipher-selection "Link to this heading")
If you have advanced security requirements, fine-tuning of the ciphers enabled when negotiating a SSL session is possible through the [`SSLContext.set_ciphers()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ciphers "ssl.SSLContext.set_ciphers") method. Starting from Python 3.2.3, the ssl module disables certain weak ciphers by default, but you may want to further restrict the cipher choice. Be sure to read OpenSSL’s documentation about the [`SSLContext.get_ciphers()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.get_ciphers "ssl.SSLContext.get_ciphers") or the `openssl ciphers` command on your system.
### Multi-processing[¶](https://docs.python.org/3/library/ssl.html#multi-processing "Link to this heading")
If using this module as part of a multi-processed application (using, for example the [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") or [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures "concurrent.futures: Execute computations concurrently using threads or processes.") modules), be aware that OpenSSL’s internal random number generator does not properly handle forked processes. Applications must change the PRNG state of the parent process if they use any SSL feature with [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork"). Any successful call of [`RAND_add()`](https://docs.python.org/3/library/ssl.html#ssl.RAND_add "ssl.RAND_add") or [`RAND_bytes()`](https://docs.python.org/3/library/ssl.html#ssl.RAND_bytes "ssl.RAND_bytes") is sufficient.
## TLS 1.3[¶](https://docs.python.org/3/library/ssl.html#tls-1-3 "Link to this heading")
Added in version 3.7.
The TLS 1.3 protocol behaves slightly differently than previous version of TLS/SSL. Some new TLS 1.3 features are not yet available.
  * TLS 1.3 uses a disjunct set of cipher suites. All AES-GCM and ChaCha20 cipher suites are enabled by default. The method [`SSLContext.set_ciphers()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ciphers "ssl.SSLContext.set_ciphers") cannot enable or disable any TLS 1.3 ciphers yet, but [`SSLContext.get_ciphers()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.get_ciphers "ssl.SSLContext.get_ciphers") returns them.
  * Session tickets are no longer sent as part of the initial handshake and are handled differently. [`SSLSocket.session`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.session "ssl.SSLSocket.session") and [`SSLSession`](https://docs.python.org/3/library/ssl.html#ssl.SSLSession "ssl.SSLSession") are not compatible with TLS 1.3.
  * Client-side certificates are also no longer verified during the initial handshake. A server can request a certificate at any time. Clients process certificate requests while they send or receive application data from the server.
  * TLS 1.3 features like early data, deferred TLS client cert request, signature algorithm configuration, and rekeying are not supported yet.


See also

Class [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")

Documentation of underlying [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") class
Intro from the Apache HTTP Server documentation
Steve Kent
Donald E. Eastlake, Jeffrey I. Schiller, Steve Crocker
David Cooper et al.
Tim Dierks and Eric Rescorla.
Donald E. Eastlake
IANA
IETF
Mozilla
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html)
    * [Functions, Constants, and Exceptions](https://docs.python.org/3/library/ssl.html#functions-constants-and-exceptions)
      * [Socket creation](https://docs.python.org/3/library/ssl.html#socket-creation)
      * [Context creation](https://docs.python.org/3/library/ssl.html#context-creation)
      * [Exceptions](https://docs.python.org/3/library/ssl.html#exceptions)
      * [Random generation](https://docs.python.org/3/library/ssl.html#random-generation)
      * [Certificate handling](https://docs.python.org/3/library/ssl.html#certificate-handling)
      * [Constants](https://docs.python.org/3/library/ssl.html#constants)
    * [SSL Sockets](https://docs.python.org/3/library/ssl.html#ssl-sockets)
    * [SSL Contexts](https://docs.python.org/3/library/ssl.html#ssl-contexts)
    * [Certificates](https://docs.python.org/3/library/ssl.html#certificates)
      * [Certificate chains](https://docs.python.org/3/library/ssl.html#certificate-chains)
      * [CA certificates](https://docs.python.org/3/library/ssl.html#ca-certificates)
      * [Combined key and certificate](https://docs.python.org/3/library/ssl.html#combined-key-and-certificate)
      * [Self-signed certificates](https://docs.python.org/3/library/ssl.html#self-signed-certificates)
    * [Examples](https://docs.python.org/3/library/ssl.html#examples)
      * [Testing for SSL support](https://docs.python.org/3/library/ssl.html#testing-for-ssl-support)
      * [Client-side operation](https://docs.python.org/3/library/ssl.html#client-side-operation)
      * [Server-side operation](https://docs.python.org/3/library/ssl.html#server-side-operation)
    * [Notes on non-blocking sockets](https://docs.python.org/3/library/ssl.html#notes-on-non-blocking-sockets)
    * [Memory BIO Support](https://docs.python.org/3/library/ssl.html#memory-bio-support)
    * [SSL session](https://docs.python.org/3/library/ssl.html#ssl-session)
    * [Security considerations](https://docs.python.org/3/library/ssl.html#security-considerations)
      * [Best defaults](https://docs.python.org/3/library/ssl.html#best-defaults)
      * [Manual settings](https://docs.python.org/3/library/ssl.html#manual-settings)
        * [Verifying certificates](https://docs.python.org/3/library/ssl.html#verifying-certificates)
        * [Protocol versions](https://docs.python.org/3/library/ssl.html#protocol-versions)
        * [Cipher selection](https://docs.python.org/3/library/ssl.html#cipher-selection)
      * [Multi-processing](https://docs.python.org/3/library/ssl.html#multi-processing)
    * [TLS 1.3](https://docs.python.org/3/library/ssl.html#tls-1-3)


#### Previous topic
[`socket` — Low-level networking interface](https://docs.python.org/3/library/socket.html "previous chapter")
#### Next topic
[`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=ssl+%E2%80%94+TLS%2FSSL+wrapper+for+socket+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fssl.html&pagesource=library%2Fssl.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/select.html "select — Waiting for I/O completion") |
  * [previous](https://docs.python.org/3/library/socket.html "socket — Low-level networking interface") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
  * [`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
