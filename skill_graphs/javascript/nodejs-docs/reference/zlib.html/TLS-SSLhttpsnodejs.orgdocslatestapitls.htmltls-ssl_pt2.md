  if (tlsSocket.remoteAddress !== '...')
    return; // Only log keys for a particular IP
  logFile.write(line);
});
copy
```

#### Event: `'newSession'`[#](https://nodejs.org/docs/latest/api/tls.html#event-newsession)
Added in: v0.9.2History Version | Changes
---|---
v0.11.12 | The `callback` argument is now supported.
The `'newSession'` event is emitted upon creation of a new TLS session. This may be used to store sessions in external storage. The data should be provided to the [`'resumeSession'`](https://nodejs.org/docs/latest/api/tls.html#event-resumesession) callback.
The listener callback is passed three arguments when called:
  * `sessionId` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The TLS session identifier
  * `sessionData` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The TLS session data
  * `callback`


Listening for this event will have an effect only on connections established after the addition of the event listener.
#### Event: `'OCSPRequest'`[#](https://nodejs.org/docs/latest/api/tls.html#event-ocsprequest)
Added in: v0.11.13
The `'OCSPRequest'` event is emitted when the client sends a certificate status request. The listener callback is passed three arguments when called:
  * `certificate` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The server certificate
  * `issuer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The issuer's certificate
  * `callback`


The server's current certificate can be parsed to obtain the OCSP URL and certificate ID; after obtaining an OCSP response, `callback(null, resp)` is then invoked, where `resp` is a `Buffer` instance containing the OCSP response. Both `certificate` and `issuer` are `Buffer` DER-representations of the primary and issuer's certificates. These can be used to obtain the OCSP certificate ID and OCSP endpoint URL.
Alternatively, `callback(null, null)` may be called, indicating that there was no OCSP response.
Calling `callback(err)` will result in a `socket.destroy(err)` call.
The typical flow of an OCSP request is as follows:
  1. Client connects to the server and sends an `'OCSPRequest'` (via the status info extension in ClientHello).
  2. Server receives the request and emits the `'OCSPRequest'` event, calling the listener if registered.
  3. Server extracts the OCSP URL from either the `certificate` or `issuer` and performs an
  4. Server receives `'OCSPResponse'` from the CA and sends it back to the client via the `callback` argument
  5. Client validates the response and either destroys the socket or performs a handshake.


The `issuer` can be `null` if the certificate is either self-signed or the issuer is not in the root certificates list. (An issuer may be provided via the `ca` option when establishing the TLS connection.)
Listening for this event will have an effect only on connections established after the addition of the event listener.
An npm module like
#### Event: `'resumeSession'`[#](https://nodejs.org/docs/latest/api/tls.html#event-resumesession)
Added in: v0.9.2
The `'resumeSession'` event is emitted when the client requests to resume a previous TLS session. The listener callback is passed two arguments when called:
  * `sessionId` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The TLS session identifier
  * `callback` `callback([err[, sessionData]])`
    * `err`
    * `sessionData` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


The event listener should perform a lookup in external storage for the `sessionData` saved by the [`'newSession'`](https://nodejs.org/docs/latest/api/tls.html#event-newsession) event handler using the given `sessionId`. If found, call `callback(null, sessionData)` to resume the session. If not found, the session cannot be resumed. `callback()` must be called without `sessionData` so that the handshake can continue and a new session can be created. It is possible to call `callback(err)` to terminate the incoming connection and destroy the socket.
Listening for this event will have an effect only on connections established after the addition of the event listener.
The following illustrates resuming a TLS session:
```
const tlsSessionStore = {};
server.on('newSession', (id, data, cb) => {
  tlsSessionStore[id.toString('hex')] = data;
  cb();
});
server.on('resumeSession', (id, cb) => {
  cb(null, tlsSessionStore[id.toString('hex')] || null);
});
copy
```

#### Event: `'secureConnection'`[#](https://nodejs.org/docs/latest/api/tls.html#event-secureconnection)
Added in: v0.3.2
The `'secureConnection'` event is emitted after the handshaking process for a new connection has successfully completed. The listener callback is passed a single argument when called:
  * `tlsSocket` [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket) The established TLS socket.


The `tlsSocket.authorized` property is a `boolean` indicating whether the client has been verified by one of the supplied Certificate Authorities for the server. If `tlsSocket.authorized` is `false`, then `socket.authorizationError` is set to describe how authorization failed. Depending on the settings of the TLS server, unauthorized connections may still be accepted.
The `tlsSocket.alpnProtocol` property is a string that contains the selected ALPN protocol. When ALPN has no selected protocol because the client or the server did not send an ALPN extension, `tlsSocket.alpnProtocol` equals `false`.
The `tlsSocket.servername` property is a string containing the server name requested via SNI.
#### Event: `'tlsClientError'`[#](https://nodejs.org/docs/latest/api/tls.html#event-tlsclienterror)
Added in: v6.0.0
The `'tlsClientError'` event is emitted when an error occurs before a secure connection is established. The listener callback is passed two arguments when called:
  * `exception` `Error` object describing the error
  * `tlsSocket` [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket) The `tls.TLSSocket` instance from which the error originated.


####  `server.addContext(hostname, context)`[#](https://nodejs.org/docs/latest/api/tls.html#serveraddcontexthostname-context)
Added in: v0.5.3
  * `hostname` `'*'`)
  * `context` [`<tls.SecureContext>`](https://nodejs.org/docs/latest/api/tls.html#class-tlssecurecontext) An object containing any of the possible properties from the [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) `options` arguments (e.g. `key`, `cert`, `ca`, etc), or a TLS context object created with [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) itself.


The `server.addContext()` method adds a secure context that will be used if the client request's SNI name matches the supplied `hostname` (or wildcard).
When there are multiple matching contexts, the most recently added one is used.
####  `server.address()`[#](https://nodejs.org/docs/latest/api/tls.html#serveraddress)
Added in: v0.6.0
  * Returns:


Returns the bound address, the address family name, and port of the server as reported by the operating system. See [`net.Server.address()`](https://nodejs.org/docs/latest/api/net.html#serveraddress) for more information.
####  `server.close([callback])`[#](https://nodejs.org/docs/latest/api/tls.html#serverclosecallback)
Added in: v0.3.2
  * `callback` `'close'` event.
  * Returns: [`<tls.Server>`](https://nodejs.org/docs/latest/api/tls.html#class-tlsserver)


The `server.close()` method stops the server from accepting new connections.
This function operates asynchronously. The `'close'` event will be emitted when the server has no more open connections.
####  `server.getTicketKeys()`[#](https://nodejs.org/docs/latest/api/tls.html#servergetticketkeys)
Added in: v3.0.0
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A 48-byte buffer containing the session ticket keys.


Returns the session ticket keys.
See [Session Resumption](https://nodejs.org/docs/latest/api/tls.html#session-resumption) for more information.
####  `server.listen()`[#](https://nodejs.org/docs/latest/api/tls.html#serverlisten)
Starts the server listening for encrypted connections. This method is identical to [`server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) from [`net.Server`](https://nodejs.org/docs/latest/api/net.html#class-netserver).
####  `server.setSecureContext(options)`[#](https://nodejs.org/docs/latest/api/tls.html#serversetsecurecontextoptions)
Added in: v11.0.0
  * `options` [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) `options` arguments (e.g. `key`, `cert`, `ca`, etc).


The `server.setSecureContext()` method replaces the secure context of an existing server. Existing connections to the server are not interrupted.
####  `server.setTicketKeys(keys)`[#](https://nodejs.org/docs/latest/api/tls.html#serversetticketkeyskeys)
Added in: v3.0.0
  * `keys` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Sets the session ticket keys.
Changes to the ticket keys are effective only for future server connections. Existing or currently pending server connections will use the previous keys.
See [Session Resumption](https://nodejs.org/docs/latest/api/tls.html#session-resumption) for more information.
### Class: `tls.TLSSocket`[#](https://nodejs.org/docs/latest/api/tls.html#class-tlstlssocket)
Added in: v0.11.4
  * Extends: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)


Performs transparent encryption of written data and all required TLS negotiation.
Instances of `tls.TLSSocket` implement the duplex [Stream](https://nodejs.org/docs/latest/api/stream.html#stream) interface.
Methods that return TLS connection metadata (e.g. [`tls.TLSSocket.getPeerCertificate()`](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetpeercertificatedetailed)) will only return data while the connection is open.
####  `new tls.TLSSocket(socket[, options])`[#](https://nodejs.org/docs/latest/api/tls.html#new-tlstlssocketsocket-options)
Added in: v0.11.4History Version | Changes
---|---
v12.2.0 | The `enableTrace` option is now supported.
v5.0.0 | ALPN options are supported now.
  * `socket` [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) | [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) On the server side, any `Duplex` stream. On the client side, any instance of [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) (for generic `Duplex` stream support on the client side, [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback) must be used).
  * `options`
    * `enableTrace`: See [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener)
    * `isServer`: The SSL/TLS protocol is asymmetrical, TLSSockets must know if they are to behave as a server or a client. If `true` the TLS socket will be instantiated as a server. **Default:** `false`.
    * `server` [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver) A [`net.Server`](https://nodejs.org/docs/latest/api/net.html#class-netserver) instance.
    * `requestCert`: Whether to authenticate the remote peer by requesting a certificate. Clients always request a server certificate. Servers (`isServer` is true) may set `requestCert` to true to request a client certificate.
    * `rejectUnauthorized`: See [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener)
    * `ALPNProtocols`: See [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener)
    * `SNICallback`: See [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener)
    * `ALPNCallback`: See [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener)
    * `session` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A `Buffer` instance containing a TLS session.
    * `requestOCSP` `true`, specifies that the OCSP status request extension will be added to the client hello and an `'OCSPResponse'` event will be emitted on the socket before establishing a secure communication
    * `secureContext`: TLS context object created with [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions). If a `secureContext` is _not_ provided, one will be created by passing the entire `options` object to `tls.createSecureContext()`.
    * ...: [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) options that are used if the `secureContext` option is missing. Otherwise, they are ignored.


Construct a new `tls.TLSSocket` object from an existing TCP socket.
#### Event: `'keylog'`[#](https://nodejs.org/docs/latest/api/tls.html#event-keylog-1)
Added in: v12.3.0, v10.20.0
  * `line` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) Line of ASCII text, in NSS `SSLKEYLOGFILE` format.


The `keylog` event is emitted on a `tls.TLSSocket` when key material is generated or received by the socket. This keying material can be stored for debugging, as it allows captured TLS traffic to be decrypted. It may be emitted multiple times, before or after the handshake completes.
A typical use case is to append received lines to a common text file, which is later used by software (such as Wireshark) to decrypt the traffic:
```
const logFile = fs.createWriteStream('/tmp/ssl-keys.log', { flags: 'a' });
// ...
tlsSocket.on('keylog', (line) => logFile.write(line));
copy
```

#### Event: `'OCSPResponse'`[#](https://nodejs.org/docs/latest/api/tls.html#event-ocspresponse)
Added in: v0.11.13
The `'OCSPResponse'` event is emitted if the `requestOCSP` option was set when the `tls.TLSSocket` was created and an OCSP response has been received. The listener callback is passed a single argument when called:
  * `response` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The server's OCSP response


Typically, the `response` is a digitally signed object from the server's CA that contains information about server's certificate revocation status.
#### Event: `'secure'`[#](https://nodejs.org/docs/latest/api/tls.html#event-secure)
Added in: v0.11.4
The `'secure'` event is emitted after the TLS handshake has successfully completed and a secure connection has been established.
This event is emitted on both client and server [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket) instances, including sockets created using the `new tls.TLSSocket()` constructor.
#### Event: `'secureConnect'`[#](https://nodejs.org/docs/latest/api/tls.html#event-secureconnect)
Added in: v0.11.4
The `'secureConnect'` event is emitted after the handshaking process for a new connection has successfully completed. The listener callback will be called regardless of whether or not the server's certificate has been authorized. It is the client's responsibility to check the `tlsSocket.authorized` property to determine if the server certificate was signed by one of the specified CAs. If `tlsSocket.authorized === false`, then the error can be found by examining the `tlsSocket.authorizationError` property. If ALPN was used, the `tlsSocket.alpnProtocol` property can be checked to determine the negotiated protocol.
The `'secureConnect'` event is not emitted when a [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket) is created using the `new tls.TLSSocket()` constructor.
#### Event: `'session'`[#](https://nodejs.org/docs/latest/api/tls.html#event-session)
Added in: v11.10.0
  * `session` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


The `'session'` event is emitted on a client `tls.TLSSocket` when a new session or TLS ticket is available. This may or may not be before the handshake is complete, depending on the TLS protocol version that was negotiated. The event is not emitted on the server, or if a new session was not created, for example, when the connection was resumed. For some TLS protocol versions the event may be emitted multiple times, in which case all the sessions can be used for resumption.
On the client, the `session` can be provided to the `session` option of [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback) to resume the connection.
See [Session Resumption](https://nodejs.org/docs/latest/api/tls.html#session-resumption) for more information.
For TLSv1.2 and below, [`tls.TLSSocket.getSession()`](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetsession) can be called once the handshake is complete. For TLSv1.3, only ticket-based resumption is allowed by the protocol, multiple tickets are sent, and the tickets aren't sent until after the handshake completes. So it is necessary to wait for the `'session'` event to get a resumable session. Applications should use the `'session'` event instead of `getSession()` to ensure they will work for all TLS versions. Applications that only expect to get or use one session should listen for this event only once:
```
tlsSocket.once('session', (session) => {
  // The session can be used immediately or later.
  tls.connect({
    session: session,
    // Other connect options...
  });
});
copy
```

####  `tlsSocket.address()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketaddress)
Added in: v0.11.4History Version | Changes
---|---
v18.4.0 | The `family` property now returns a string instead of a number.
v18.0.0 | The `family` property now returns a number instead of a string.
  * Returns:


Returns the bound `address`, the address `family` name, and `port` of the underlying socket as reported by the operating system: `{ port: 12346, family: 'IPv4', address: '127.0.0.1' }`.
####  `tlsSocket.authorizationError`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketauthorizationerror)
Added in: v0.11.4
Returns the reason why the peer's certificate was not been verified. This property is set only when `tlsSocket.authorized === false`.
####  `tlsSocket.authorized`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketauthorized)
Added in: v0.11.4
  * Type:


This property is `true` if the peer certificate was signed by one of the CAs specified when creating the `tls.TLSSocket` instance, otherwise `false`.
####  `tlsSocket.disableRenegotiation()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketdisablerenegotiation)
Added in: v8.4.0
Disables TLS renegotiation for this `TLSSocket` instance. Once called, attempts to renegotiate will trigger an `'error'` event on the `TLSSocket`.
####  `tlsSocket.enableTrace()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketenabletrace)
Added in: v12.2.0
When enabled, TLS packet trace information is written to `stderr`. This can be used to debug TLS connection problems.
The format of the output is identical to the output of `openssl s_client -trace` or `openssl s_server -trace`. While it is produced by OpenSSL's `SSL_trace()` function, the format is undocumented, can change without notice, and should not be relied on.
####  `tlsSocket.encrypted`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketencrypted)
Added in: v0.11.4
Always returns `true`. This may be used to distinguish TLS sockets from regular `net.Socket` instances.
####  `tlsSocket.exportKeyingMaterial(length, label[, context])`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketexportkeyingmateriallength-label-context)
Added in: v13.10.0, v12.17.0
  * `length`
  * `label`
  * `context` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) Optionally provide a context.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) requested bytes of the keying material


Keying material is used for validations to prevent different kind of attacks in network protocols, for example in the specifications of IEEE 802.1X.
Example
```
const keyingMaterial = tlsSocket.exportKeyingMaterial(
  128,
  'client finished');

/*
 Example return value of keyingMaterial:
 <Buffer 76 26 af 99 c5 56 8e 42 09 91 ef 9f 93 cb ad 6c 7b 65 f8 53 f1 d8 d9
    12 5a 33 b8 b5 25 df 7b 37 9f e0 e2 4f b8 67 83 a3 2f cd 5d 41 42 4c 91
    74 ef 2c ... 78 more bytes>
*/
copy
```

See the OpenSSL
####  `tlsSocket.getCertificate()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetcertificate)
Added in: v11.2.0
  * Returns:


Returns an object representing the local certificate. The returned object has some properties corresponding to the fields of the certificate.
See [`tls.TLSSocket.getPeerCertificate()`](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetpeercertificatedetailed) for an example of the certificate structure.
If there is no local certificate, an empty object will be returned. If the socket has been destroyed, `null` will be returned.
####  `tlsSocket.getCipher()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetcipher)
Added in: v0.11.4History Version | Changes
---|---
v13.4.0, v12.16.0 | Return the IETF cipher name as `standardName`.
v12.0.0 | Return the minimum cipher version, instead of a fixed string (`'TLSv1/SSLv3'`).
  * Returns:
    * `name`
    * `standardName`
    * `version` [`tls.TLSSocket.getProtocol()`](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetprotocol).


Returns an object containing information on the negotiated cipher suite.
For example, a TLSv1.2 protocol with AES256-SHA cipher:
```
{
    "name": "AES256-SHA",
    "standardName": "TLS_RSA_WITH_AES_256_CBC_SHA",
    "version": "SSLv3"
}
copy
```

See
####  `tlsSocket.getEphemeralKeyInfo()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetephemeralkeyinfo)
Added in: v5.0.0
  * Returns:


Returns an object representing the type, name, and size of parameter of an ephemeral key exchange in [perfect forward secrecy](https://nodejs.org/docs/latest/api/tls.html#perfect-forward-secrecy) on a client connection. It returns an empty object when the key exchange is not ephemeral. As this is only supported on a client socket; `null` is returned if called on a server socket. The supported types are `'DH'` and `'ECDH'`. The `name` property is available only when type is `'ECDH'`.
For example: `{ type: 'ECDH', name: 'prime256v1', size: 256 }`.
####  `tlsSocket.getFinished()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetfinished)
Added in: v9.9.0
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Finished` message that has been sent to the socket as part of a SSL/TLS handshake, or `undefined` if no `Finished` message has been sent yet.


As the `Finished` messages are message digests of the complete handshake (with a total of 192 bits for TLS 1.0 and more for SSL 3.0), they can be used for external authentication procedures when the authentication provided by SSL/TLS is not desired or is not enough.
Corresponds to the `SSL_get_finished` routine in OpenSSL and may be used to implement the `tls-unique` channel binding from
####  `tlsSocket.getPeerCertificate([detailed])`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetpeercertificatedetailed)
Added in: v0.11.4
  * `detailed` `true`, otherwise include just the peer's certificate.
  * Returns:


Returns an object representing the peer's certificate. If the peer does not provide a certificate, an empty object will be returned. If the socket has been destroyed, `null` will be returned.
If the full certificate chain was requested, each certificate will include an `issuerCertificate` property containing an object representing its issuer's certificate.
##### Certificate object[#](https://nodejs.org/docs/latest/api/tls.html#certificate-object)
History Version | Changes
---|---
v19.1.0, v18.13.0 | Add "ca" property.
v17.2.0, v16.14.0 | Add fingerprint512.
v11.4.0 | Support Elliptic Curve public key info.
A certificate object has properties corresponding to the fields of the certificate.
  * `ca` `true` if a Certificate Authority (CA), `false` otherwise.
  * `raw` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The DER encoded X.509 certificate data.
  * `subject` `C`), StateOrProvince (`ST`), Locality (`L`), Organization (`O`), OrganizationalUnit (`OU`), and CommonName (`CN`). The CommonName is typically a DNS name with TLS certificates. Example: `{C: 'UK', ST: 'BC', L: 'Metro', O: 'Node Fans', OU: 'Docs', CN: 'example.com'}`.
  * `issuer` `subject`.
  * `valid_from`
  * `valid_to`
  * `serialNumber` `'B9B0D332A1AA5635'`.
  * `fingerprint` `:` separated hexadecimal string. Example: `'2A:7A:C2:DD:...'`.
  * `fingerprint256` `:` separated hexadecimal string. Example: `'2A:7A:C2:DD:...'`.
  * `fingerprint512` `:` separated hexadecimal string. Example: `'2A:7A:C2:DD:...'`.
  * `ext_key_usage`
  * `subjectaltname` `subject` names.
  * `infoAccess`
  * `issuerCertificate`


The certificate may contain information about the public key, depending on the key type.
For RSA keys, the following properties may be defined:
  * `bits` `1024`.
  * `exponent` `'0x010001'`.
  * `modulus` `'B56CE45CB7...'`.
  * `pubkey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The public key.
