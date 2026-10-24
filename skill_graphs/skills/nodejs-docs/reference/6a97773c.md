

For EC keys, the following properties may be defined:
  * `pubkey` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The public key.
  * `bits` `256`.
  * `asn1Curve` `'prime256v1'`.
  * `nistCurve` `'P-256'`.


Example certificate:
```
{ subject:
   { OU: [ 'Domain Control Validated', 'PositiveSSL Wildcard' ],
     CN: '*.nodejs.org' },
  issuer:
   { C: 'GB',
     ST: 'Greater Manchester',
     L: 'Salford',
     O: 'COMODO CA Limited',
     CN: 'COMODO RSA Domain Validation Secure Server CA' },
  subjectaltname: 'DNS:*.nodejs.org, DNS:nodejs.org',
  infoAccess:
   { 'CA Issuers - URI':
      [ 'http://crt.comodoca.com/COMODORSADomainValidationSecureServerCA.crt' ],
     'OCSP - URI': [ 'http://ocsp.comodoca.com' ] },
  modulus: 'B56CE45CB740B09A13F64AC543B712FF9EE8E4C284B542A1708A27E82A8D151CA178153E12E6DDA15BF70FFD96CB8A88618641BDFCCA03527E665B70D779C8A349A6F88FD4EF6557180BD4C98192872BCFE3AF56E863C09DDD8BC1EC58DF9D94F914F0369102B2870BECFA1348A0838C9C49BD1C20124B442477572347047506B1FCD658A80D0C44BCC16BC5C5496CFE6E4A8428EF654CD3D8972BF6E5BFAD59C93006830B5EB1056BBB38B53D1464FA6E02BFDF2FF66CD949486F0775EC43034EC2602AEFBF1703AD221DAA2A88353C3B6A688EFE8387811F645CEED7B3FE46E1F8B9F59FAD028F349B9BC14211D5830994D055EEA3D547911E07A0ADDEB8A82B9188E58720D95CD478EEC9AF1F17BE8141BE80906F1A339445A7EB5B285F68039B0F294598A7D1C0005FC22B5271B0752F58CCDEF8C8FD856FB7AE21C80B8A2CE983AE94046E53EDE4CB89F42502D31B5360771C01C80155918637490550E3F555E2EE75CC8C636DDE3633CFEDD62E91BF0F7688273694EEEBA20C2FC9F14A2A435517BC1D7373922463409AB603295CEB0BB53787A334C9CA3CA8B30005C5A62FC0715083462E00719A8FA3ED0A9828C3871360A73F8B04A4FC1E71302844E9BB9940B77E745C9D91F226D71AFCAD4B113AAF68D92B24DDB4A2136B55A1CD1ADF39605B63CB639038ED0F4C987689866743A68769CC55847E4A06D6E2E3F1',
  exponent: '0x10001',
  pubkey: <Buffer ... >,
  valid_from: 'Aug 14 00:00:00 2017 GMT',
  valid_to: 'Nov 20 23:59:59 2019 GMT',
  fingerprint: '01:02:59:D9:C3:D2:0D:08:F7:82:4E:44:A4:B4:53:C5:E2:3A:87:4D',
  fingerprint256: '69:AE:1A:6A:D4:3D:C6:C1:1B:EA:C6:23:DE:BA:2A:14:62:62:93:5C:7A:EA:06:41:9B:0B:BC:87:CE:48:4E:02',
  fingerprint512: '19:2B:3E:C3:B3:5B:32:E8:AE:BB:78:97:27:E4:BA:6C:39:C9:92:79:4F:31:46:39:E2:70:E5:5F:89:42:17:C9:E8:64:CA:FF:BB:72:56:73:6E:28:8A:92:7E:A3:2A:15:8B:C2:E0:45:CA:C3:BC:EA:40:52:EC:CA:A2:68:CB:32',
  ext_key_usage: [ '1.3.6.1.5.5.7.3.1', '1.3.6.1.5.5.7.3.2' ],
  serialNumber: '66593D57F20CBC573E433381B5FEC280',
  raw: <Buffer ... > }
copy
```

####  `tlsSocket.getPeerFinished()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetpeerfinished)
Added in: v9.9.0
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Finished` message that is expected or has actually been received from the socket as part of a SSL/TLS handshake, or `undefined` if there is no `Finished` message so far.


As the `Finished` messages are message digests of the complete handshake (with a total of 192 bits for TLS 1.0 and more for SSL 3.0), they can be used for external authentication procedures when the authentication provided by SSL/TLS is not desired or is not enough.
Corresponds to the `SSL_get_peer_finished` routine in OpenSSL and may be used to implement the `tls-unique` channel binding from
####  `tlsSocket.getPeerX509Certificate()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetpeerx509certificate)
Added in: v15.9.0
  * Returns: [`<X509Certificate>`](https://nodejs.org/docs/latest/api/crypto.html#class-x509certificate)


Returns the peer certificate as an [`<X509Certificate>`](https://nodejs.org/docs/latest/api/crypto.html#class-x509certificate) object.
If there is no peer certificate, or the socket has been destroyed, `undefined` will be returned.
####  `tlsSocket.getProtocol()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetprotocol)
Added in: v5.7.0
  * Returns:


Returns a string containing the negotiated SSL/TLS protocol version of the current connection. The value `'unknown'` will be returned for connected sockets that have not completed the handshaking process. The value `null` will be returned for server sockets or disconnected client sockets.
Protocol versions are:
  * `'SSLv3'`
  * `'TLSv1'`
  * `'TLSv1.1'`
  * `'TLSv1.2'`
  * `'TLSv1.3'`


See the OpenSSL
####  `tlsSocket.getSession()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetsession)
Added in: v0.11.4
  * Type: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


Returns the TLS session data or `undefined` if no session was negotiated. On the client, the data can be provided to the `session` option of [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback) to resume the connection. On the server, it may be useful for debugging.
See [Session Resumption](https://nodejs.org/docs/latest/api/tls.html#session-resumption) for more information.
Note: `getSession()` works only for TLSv1.2 and below. For TLSv1.3, applications must use the [`'session'`](https://nodejs.org/docs/latest/api/tls.html#event-session) event (it also works for TLSv1.2 and below).
####  `tlsSocket.getSharedSigalgs()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetsharedsigalgs)
Added in: v12.11.0
  * Returns:


See
####  `tlsSocket.getTLSTicket()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgettlsticket)
Added in: v0.11.4
  * Type: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer)


For a client, returns the TLS session ticket if one is available, or `undefined`. For a server, always returns `undefined`.
It may be useful for debugging.
See [Session Resumption](https://nodejs.org/docs/latest/api/tls.html#session-resumption) for more information.
####  `tlsSocket.getX509Certificate()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketgetx509certificate)
Added in: v15.9.0
  * Returns: [`<X509Certificate>`](https://nodejs.org/docs/latest/api/crypto.html#class-x509certificate)


Returns the local certificate as an [`<X509Certificate>`](https://nodejs.org/docs/latest/api/crypto.html#class-x509certificate) object.
If there is no local certificate, or the socket has been destroyed, `undefined` will be returned.
####  `tlsSocket.isSessionReused()`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketissessionreused)
Added in: v0.5.6
  * Returns: `true` if the session was reused, `false` otherwise.


See [Session Resumption](https://nodejs.org/docs/latest/api/tls.html#session-resumption) for more information.
####  `tlsSocket.localAddress`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketlocaladdress)
Added in: v0.11.4
  * Type:


Returns the string representation of the local IP address.
####  `tlsSocket.localPort`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketlocalport)
Added in: v0.11.4
  * Type:


Returns the numeric representation of the local port.
####  `tlsSocket.remoteAddress`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketremoteaddress)
Added in: v0.11.4
  * Type:


Returns the string representation of the remote IP address. For example, `'74.125.127.100'` or `'2001:4860:a005::68'`.
####  `tlsSocket.remoteFamily`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketremotefamily)
Added in: v0.11.4
  * Type:


Returns the string representation of the remote IP family. `'IPv4'` or `'IPv6'`.
####  `tlsSocket.remotePort`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketremoteport)
Added in: v0.11.4
  * Type:


Returns the numeric representation of the remote port. For example, `443`.
####  `tlsSocket.renegotiate(options, callback)`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketrenegotiateoptions-callback)
Added in: v0.11.8History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `options`
    * `rejectUnauthorized` `false`, the server certificate is verified against the list of supplied CAs. An `'error'` event is emitted if verification fails; `err.code` contains the OpenSSL error code. **Default:** `true`.
    * `requestCert`
  * `callback` `renegotiate()` returned `true`, callback is attached once to the [`'secure'`](https://nodejs.org/docs/latest/api/tls.html#event-secure) event. If `renegotiate()` returned `false`, `callback` will be called in the next tick with an error, unless the `tlsSocket` has been destroyed, in which case `callback` will not be called at all.
  * Returns: `true` if renegotiation was initiated, `false` otherwise.


The `tlsSocket.renegotiate()` method initiates a TLS renegotiation process. Upon completion, the `callback` function will be passed a single argument that is either an `Error` (if the request failed) or `null`.
This method can be used to request a peer's certificate after the secure connection has been established.
When running as the server, the socket will be destroyed with an error after `handshakeTimeout` timeout.
For TLSv1.3, renegotiation cannot be initiated, it is not supported by the protocol.
####  `tlsSocket.setKeyCert(context)`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketsetkeycertcontext)
Added in: v22.5.0, v20.17.0
  * `context` [`<tls.SecureContext>`](https://nodejs.org/docs/latest/api/tls.html#class-tlssecurecontext) An object containing at least `key` and `cert` properties from the [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) `options`, or a TLS context object created with [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) itself.


The `tlsSocket.setKeyCert()` method sets the private key and certificate to use for the socket. This is mainly useful if you wish to select a server certificate from a TLS server's `ALPNCallback`.
####  `tlsSocket.setMaxSendFragment(size)`[#](https://nodejs.org/docs/latest/api/tls.html#tlssocketsetmaxsendfragmentsize)
Added in: v0.11.11
  * `size` `16384`. **Default:** `16384`.
  * Returns:


The `tlsSocket.setMaxSendFragment()` method sets the maximum TLS fragment size. Returns `true` if setting the limit succeeded; `false` otherwise.
Smaller fragment sizes decrease the buffering latency on the client: larger fragments are buffered by the TLS layer until the entire fragment is received and its integrity is verified; large fragments can span multiple roundtrips and their processing can be delayed due to packet loss or reordering. However, smaller fragments add extra TLS framing bytes and CPU overhead, which may decrease overall server throughput.
###  `tls.checkServerIdentity(hostname, cert)`[#](https://nodejs.org/docs/latest/api/tls.html#tlscheckserveridentityhostname-cert)
Added in: v0.8.4History Version | Changes
---|---
v17.3.1, v16.13.2, v14.18.3, v12.22.9 | Support for `uniformResourceIdentifier` subject alternative names has been disabled in response to CVE-2021-44531.
  * `hostname`
  * `cert` [certificate object](https://nodejs.org/docs/latest/api/tls.html#certificate-object) representing the peer's certificate.
  * Returns:


Verifies the certificate `cert` is issued to `hostname`.
Returns `reason`, `host`, and `cert` on failure. On success, returns
This function is intended to be used in combination with the `checkServerIdentity` option that can be passed to [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback) and as such operates on a [certificate object](https://nodejs.org/docs/latest/api/tls.html#certificate-object). For other purposes, consider using [`x509.checkHost()`](https://nodejs.org/docs/latest/api/crypto.html#x509checkhostname-options) instead.
This function can be overwritten by providing an alternative function as the `options.checkServerIdentity` option that is passed to `tls.connect()`. The overwriting function can call `tls.checkServerIdentity()` of course, to augment the checks done with additional verification.
This function is only called if the certificate passed all other checks, such as being issued by trusted CA (`options.ca`).
Earlier versions of Node.js incorrectly accepted certificates for a given `hostname` if a matching `uniformResourceIdentifier` subject alternative name was present (see `uniformResourceIdentifier` subject alternative names can use a custom `options.checkServerIdentity` function that implements the desired behavior.
###  `tls.connect(options[, callback])`[#](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback)
Added in: v0.11.3History Version | Changes
---|---
v15.1.0, v14.18.0 | Added `onread` option.
v14.1.0, v13.14.0 | The `highWaterMark` option is accepted now.
v13.6.0, v12.16.0 | The `pskCallback` option is now supported.
v12.9.0 | Support the `allowHalfOpen` option.
v12.4.0 | The `hints` option is now supported.
v12.2.0 | The `enableTrace` option is now supported.
v11.8.0, v10.16.0 | The `timeout` option is supported now.
v8.0.0 | The `lookup` option is supported now.
v8.0.0 | The `ALPNProtocols` option can be a `TypedArray` or `DataView` now.
v5.3.0, v4.7.0 | The `secureContext` option is supported now.
v5.0.0 | ALPN options are supported now.
  * `options`
    * `enableTrace`: See [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener)
    * `host` **Default:** `'localhost'`.
    * `port`
    * `path` `host` and `port` are ignored.
    * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) Establish secure connection on a given socket rather than creating a new socket. Typically, this is an instance of [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket), but any `Duplex` stream is allowed. If this option is specified, `path`, `host`, and `port` are ignored, except for certificate validation. Usually, a socket is already connected when passed to `tls.connect()`, but it can be connected later. Connection/disconnection/destruction of `socket` is the user's responsibility; calling `tls.connect()` will not cause `net.connect()` to be called.
    * `allowHalfOpen` `false`, then the socket will automatically end the writable side when the readable side ends. If the `socket` option is set, this option has no effect. See the `allowHalfOpen` option of [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) for details. **Default:** `false`.
    * `rejectUnauthorized` `false`, the server certificate is verified against the list of supplied CAs. An `'error'` event is emitted if verification fails; `err.code` contains the OpenSSL error code. **Default:** `true`.
    * `pskCallback` [Pre-shared keys](https://nodejs.org/docs/latest/api/tls.html#pre-shared-keys).
    * `ALPNProtocols` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer`, `TypedArray`, or `DataView` containing the supported ALPN protocols. Buffers should have the format `[len][name][len][name]...` e.g. `'\x08http/1.1\x08http/1.0'`, where the `len` byte is the length of the next protocol name. Passing an array is usually much simpler, e.g. `['http/1.1', 'http/1.0']`. Protocols earlier in the list have higher preference than those later.
    * `servername` `SNICallback` option to [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener).
    * `checkServerIdentity(servername, cert)` `tls.checkServerIdentity()` function) when checking the server's host name (or the provided `servername` when explicitly set) against the certificate. This should return an `undefined` if the `servername` and `cert` are verified.
    * `session` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) A `Buffer` instance, containing TLS session.
    * `requestOCSP` `true`, specifies that the OCSP status request extension will be added to the client hello and an `'OCSPResponse'` event will be emitted on the socket before establishing a secure communication.
    * `minDHSize` `minDHSize`, the TLS connection is destroyed and an error is thrown. **Default:** `1024`.
    * `highWaterMark` `highWaterMark` parameter. **Default:** `16 * 1024`.
    * `timeout`: [`socket.setTimeout(timeout)`](https://nodejs.org/docs/latest/api/net.html#socketsettimeouttimeout-callback) after the socket is created, but before it starts the connection.
    * `secureContext`: TLS context object created with [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions). If a `secureContext` is _not_ provided, one will be created by passing the entire `options` object to `tls.createSecureContext()`.
    * `onread` `socket` option is missing, incoming data is stored in a single `buffer` and passed to the supplied `callback` when data arrives on the socket, otherwise the option is ignored. See the `onread` option of [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) for details.
    * ...: [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) options that are used if the `secureContext` option is missing, otherwise they are ignored.
    * ...: Any [`socket.connect()`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener) option not already listed.
  * `callback`
  * Returns: [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket)


The `callback` function, if specified, will be added as a listener for the [`'secureConnect'`](https://nodejs.org/docs/latest/api/tls.html#event-secureconnect) event.
`tls.connect()` returns a [`tls.TLSSocket`](https://nodejs.org/docs/latest/api/tls.html#class-tlstlssocket) object.
Unlike the `https` API, `tls.connect()` does not enable the SNI (Server Name Indication) extension by default, which may cause some servers to return an incorrect certificate or reject the connection altogether. To enable SNI, set the `servername` option in addition to `host`.
The following illustrates a client for the echo server example from [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener):
```
// Assumes an echo server that is listening on port 8000.
import { connect } from 'node:tls';
import { readFileSync } from 'node:fs';
import { stdin } from 'node:process';

const options = {
  // Necessary only if the server requires client certificate authentication.
  key: readFileSync('client-key.pem'),
  cert: readFileSync('client-cert.pem'),

  // Necessary only if the server uses a self-signed certificate.
  ca: [ readFileSync('server-cert.pem') ],

  // Necessary only if the server's cert isn't for "localhost".
  checkServerIdentity: () => { return null; },
};

const socket = connect(8000, options, () => {
  console.log('client connected',
              socket.authorized ? 'authorized' : 'unauthorized');
  stdin.pipe(socket);
  stdin.resume();
});
socket.setEncoding('utf8');
socket.on('data', (data) => {
  console.log(data);
});
socket.on('end', () => {
  console.log('server ends connection');
});
// Assumes an echo server that is listening on port 8000.
const { connect } = require('node:tls');
const { readFileSync } = require('node:fs');

const options = {
  // Necessary only if the server requires client certificate authentication.
  key: readFileSync('client-key.pem'),
  cert: readFileSync('client-cert.pem'),

  // Necessary only if the server uses a self-signed certificate.
  ca: [ readFileSync('server-cert.pem') ],

  // Necessary only if the server's cert isn't for "localhost".
  checkServerIdentity: () => { return null; },
};

const socket = connect(8000, options, () => {
  console.log('client connected',
              socket.authorized ? 'authorized' : 'unauthorized');
  process.stdin.pipe(socket);
  process.stdin.resume();
});
socket.setEncoding('utf8');
socket.on('data', (data) => {
  console.log(data);
});
socket.on('end', () => {
  console.log('server ends connection');
});
copy
```

To generate the certificate and key for this example, run:
```
openssl req -x509 -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost' \
  -keyout client-key.pem -out client-cert.pem
copy
```

Then, to generate the `server-cert.pem` certificate for this example, run:
```
openssl pkcs12 -certpbe AES-256-CBC -export -out server-cert.pem \
  -inkey client-key.pem -in client-cert.pem
copy
```

###  `tls.connect(path[, options][, callback])`[#](https://nodejs.org/docs/latest/api/tls.html#tlsconnectpath-options-callback)
Added in: v0.11.3
  * `path` `options.path`.
  * `options` [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback).
  * `callback` [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback).
  * Returns: [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket)


Same as [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback) except that `path` can be provided as an argument instead of an option.
A path option, if specified, will take precedence over the path argument.
###  `tls.connect(port[, host][, options][, callback])`[#](https://nodejs.org/docs/latest/api/tls.html#tlsconnectport-host-options-callback)
Added in: v0.11.3
  * `port` `options.port`.
  * `host` `options.host`.
  * `options` [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback).
  * `callback` [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback).
  * Returns: [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket)


Same as [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback) except that `port` and `host` can be provided as arguments instead of options.
A port or host option, if specified, will take precedence over any port or host argument.
###  `tls.createSecureContext([options])`[#](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions)
Added in: v0.11.13History Version | Changes
---|---
v22.9.0, v20.18.0 | The `allowPartialTrustChain` option has been added.
v22.4.0, v20.16.0 | The `clientCertEngine`, `privateKeyEngine` and `privateKeyIdentifier` options depend on custom engine support in OpenSSL which is deprecated in OpenSSL 3.
v19.8.0, v18.16.0 | The `dhparam` option can now be set to `'auto'` to enable DHE with appropriate well-known parameters.
v12.12.0 | Added `privateKeyIdentifier` and `privateKeyEngine` options to get private key from an OpenSSL engine.
v12.11.0 | Added `sigalgs` option to override supported signature algorithms.
v12.0.0 | TLSv1.3 support added.
v11.5.0 | The `ca:` option now supports `BEGIN TRUSTED CERTIFICATE`.
v11.4.0, v10.16.0 | The `minVersion` and `maxVersion` can be used to restrict the allowed TLS protocol versions.
v10.0.0 | The `ecdhCurve` cannot be set to `false` anymore due to a change in OpenSSL.
v9.3.0 | The `options` parameter can now include `clientCertEngine`.
v9.0.0 | The `ecdhCurve` option can now be multiple `':'` separated curve names or `'auto'`.
v7.3.0 | If the `key` option is an array, individual entries do not need a `passphrase` property anymore. `Array` entries can also just be `string`s or `Buffer`s now.
v5.2.0 | The `ca` option can now be a single string containing multiple CA certificates.
  * `options`
    * `allowPartialTrustChain`
    * `ca` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) Optionally override the trusted CA certificates. If not specified, the CA certificates trusted by default are the same as the ones returned by [`tls.getCACertificates()`](https://nodejs.org/docs/latest/api/tls.html#tlsgetcacertificatestype) using the `default` type. If specified, the default list would be completely replaced (instead of being concatenated) by the certificates in the `ca` option. Users need to concatenate manually if they wish to add additional certificates instead of completely overriding the default. The value can be a string or `Buffer`, or an `Array` of strings and/or `Buffer`s. Any string or `Buffer` can contain multiple PEM CAs concatenated together. The peer's certificate must be chainable to a CA trusted by the server for the connection to be authenticated. When using certificates that are not chainable to a well-known CA, the certificate's CA must be explicitly specified as a trusted or the connection will fail to authenticate. If the peer uses a certificate that doesn't match or chain to one of the default CAs, use the `ca` option to provide a CA certificate that the peer's certificate can match or chain to. For self-signed certificates, the certificate is its own CA, and must be provided. For PEM encoded certificates, supported types are "TRUSTED CERTIFICATE", "X509 CERTIFICATE", and "CERTIFICATE".
    * `cert` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) Cert chains in PEM format. One cert chain should be provided per private key. Each cert chain should consist of the PEM formatted certificate for a provided private `key`, followed by the PEM formatted intermediate certificates (if any), in order, and not including the root CA (the root CA must be pre-known to the peer, see `ca`). When providing multiple cert chains, they do not have to be in the same order as their private keys in `key`. If the intermediate certificates are not provided, the peer will not be able to validate the certificate, and the handshake will fail.
