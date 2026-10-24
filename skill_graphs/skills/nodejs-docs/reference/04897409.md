## TLS (SSL)[#](https://nodejs.org/docs/latest/api/tls.html#tls-ssl)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:tls` module provides an implementation of the Transport Layer Security (TLS) and Secure Socket Layer (SSL) protocols that is built on top of OpenSSL. The module can be accessed using:
```
import tls from 'node:tls';
const tls = require('node:tls');
copy
```

### Determining if crypto support is unavailable[#](https://nodejs.org/docs/latest/api/tls.html#determining-if-crypto-support-is-unavailable)
It is possible for Node.js to be built without including support for the `node:crypto` module. In such cases, attempting to `import` from `tls` or calling `require('node:tls')` will result in an error being thrown.
When using CommonJS, the error thrown can be caught using try/catch:
```
let tls;
try {
  tls = require('node:tls');
} catch (err) {
  console.error('tls support is disabled!');
}
copy
```

When using the lexical ESM `import` keyword, the error can only be caught if a handler for `process.on('uncaughtException')` is registered _before_ any attempt to load the module is made (using, for instance, a preload module).
When using ESM, if there is a chance that the code may be run on a build of Node.js where crypto support is not enabled, consider using the `import` keyword:
```
let tls;
try {
  tls = await import('node:tls');
} catch (err) {
  console.error('tls support is disabled!');
}
copy
```

### TLS/SSL concepts[#](https://nodejs.org/docs/latest/api/tls.html#tlsssl-concepts)
TLS/SSL is a set of protocols that rely on a public key infrastructure (PKI) to enable secure communication between a client and a server. For most common cases, each server must have a private key.
Private keys can be generated in multiple ways. The example below illustrates use of the OpenSSL command-line interface to generate a 2048-bit RSA private key:
```
openssl genrsa -out ryans-key.pem 2048
copy
```

With TLS/SSL, all servers (and some clients) must have a _certificate_. Certificates are _public keys_ that correspond to a private key, and that are digitally signed either by a Certificate Authority or by the owner of the private key (such certificates are referred to as "self-signed"). The first step to obtaining a certificate is to create a _Certificate Signing Request_ (CSR) file.
The OpenSSL command-line interface can be used to generate a CSR for a private key:
```
openssl req -new -sha256 -key ryans-key.pem -out ryans-csr.pem
copy
```

Once the CSR file is generated, it can either be sent to a Certificate Authority for signing or used to generate a self-signed certificate.
Creating a self-signed certificate using the OpenSSL command-line interface is illustrated in the example below:
```
openssl x509 -req -in ryans-csr.pem -signkey ryans-key.pem -out ryans-cert.pem
copy
```

Once the certificate is generated, it can be used to generate a `.pfx` or `.p12` file:
```
openssl pkcs12 -export -in ryans-cert.pem -inkey ryans-key.pem \
      -certfile ca-cert.pem -out ryans.pfx
copy
```

Where:
  * `in`: is the signed certificate
  * `inkey`: is the associated private key
  * `certfile`: is a concatenation of all Certificate Authority (CA) certs into a single file, e.g. `cat ca1-cert.pem ca2-cert.pem > ca-cert.pem`


#### Perfect forward secrecy[#](https://nodejs.org/docs/latest/api/tls.html#perfect-forward-secrecy)
The term _perfect forward secrecy_ describes a feature of key-agreement (i.e., key-exchange) methods. That is, the server and client keys are used to negotiate new temporary keys that are used specifically and only for the current communication session. Practically, this means that even if the server's private key is compromised, communication can only be decrypted by eavesdroppers if the attacker manages to obtain the key-pair specifically generated for the session.
Perfect forward secrecy is achieved by randomly generating a key pair for key-agreement on every TLS/SSL handshake (in contrast to using the same key for all sessions). Methods implementing this technique are called "ephemeral".
Currently two methods are commonly used to achieve perfect forward secrecy (note the character "E" appended to the traditional abbreviations):
Perfect forward secrecy using ECDHE is enabled by default. The `ecdhCurve` option can be used when creating a TLS server to customize the list of supported ECDH curves to use. See [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener) for more info.
DHE is disabled by default but can be enabled alongside ECDHE by setting the `dhparam` option to `'auto'`. Custom DHE parameters are also supported but discouraged in favor of automatically selected, well-known parameters.
Perfect forward secrecy was optional up to TLSv1.2. As of TLSv1.3, (EC)DHE is always used (with the exception of PSK-only connections).
#### ALPN and SNI[#](https://nodejs.org/docs/latest/api/tls.html#alpn-and-sni)
ALPN (Application-Layer Protocol Negotiation Extension) and SNI (Server Name Indication) are TLS handshake extensions:
  * ALPN: Allows the use of one TLS server for multiple protocols (HTTP, HTTP/2)
  * SNI: Allows the use of one TLS server for multiple hostnames with different certificates.


#### Pre-shared keys[#](https://nodejs.org/docs/latest/api/tls.html#pre-shared-keys)
TLS-PSK support is available as an alternative to normal certificate-based authentication. It uses a pre-shared key instead of certificates to authenticate a TLS connection, providing mutual authentication. TLS-PSK and public key infrastructure are not mutually exclusive. Clients and servers can accommodate both, choosing either of them during the normal cipher negotiation step.
TLS-PSK is only a good choice where means exist to securely share a key with every connecting machine, so it does not replace the public key infrastructure (PKI) for the majority of TLS uses. The TLS-PSK implementation in OpenSSL has seen many security flaws in recent years, mostly because it is used only by a minority of applications. Please consider all alternative solutions before switching to PSK ciphers. Upon generating PSK it is of critical importance to use sufficient entropy as discussed in
PSK ciphers are disabled by default, and using TLS-PSK thus requires explicitly specifying a cipher suite with the `ciphers` option. The list of available ciphers can be retrieved via `openssl ciphers -v 'PSK'`. All TLS 1.3 ciphers are eligible for PSK and can be retrieved via `openssl ciphers -v -s -tls1_3 -psk`. On the client connection, a custom `checkServerIdentity` should be passed because the default one will fail in the absence of a certificate.
According to the
The current implementation doesn't support asynchronous PSK callbacks due to the limitations of the underlying OpenSSL API.
To use TLS-PSK, client and server must specify the `pskCallback` option, a function that returns the PSK to use (which must be compatible with the selected cipher's digest).
It will be called first on the client:
  * `hint` `null` if TLS 1.3 is used.
  * Returns: `{ psk: <Buffer|TypedArray|DataView>, identity: <string> }` or `null`.


Then on the server:
  * `socket` [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket) the server socket instance, equivalent to `this`.
  * `identity`
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `null`).


A return value of `null` stops the negotiation process and sends an `unknown_psk_identity` alert message to the other party. If the server wishes to hide the fact that the PSK identity was not known, the callback must provide some random data as `psk` to make the connection fail with `decrypt_error` before negotiation is finished.
#### Client-initiated renegotiation attack mitigation[#](https://nodejs.org/docs/latest/api/tls.html#client-initiated-renegotiation-attack-mitigation)
The TLS protocol allows clients to renegotiate certain aspects of the TLS session. Unfortunately, session renegotiation requires a disproportionate amount of server-side resources, making it a potential vector for denial-of-service attacks.
To mitigate the risk, renegotiation is limited to three times every ten minutes. An `'error'` event is emitted on the [`tls.TLSSocket`](https://nodejs.org/docs/latest/api/tls.html#class-tlstlssocket) instance when this threshold is exceeded. The limits are configurable:
  * `tls.CLIENT_RENEG_LIMIT` **Default:** `3`.
  * `tls.CLIENT_RENEG_WINDOW` **Default:** `600` (10 minutes).


The default renegotiation limits should not be modified without a full understanding of the implications and risks.
TLSv1.3 does not support renegotiation.
#### Session resumption[#](https://nodejs.org/docs/latest/api/tls.html#session-resumption)
Establishing a TLS session can be relatively slow. The process can be sped up by saving and later reusing the session state. There are several mechanisms to do so, discussed here from oldest to newest (and preferred).
##### Session identifiers[#](https://nodejs.org/docs/latest/api/tls.html#session-identifiers)
Servers generate a unique ID for new connections and send it to the client. Clients and servers save the session state. When reconnecting, clients send the ID of their saved session state and if the server also has the state for that ID, it can agree to use it. Otherwise, the server will create a new session. See
Resumption using session identifiers is supported by most web browsers when making HTTPS requests.
For Node.js, clients wait for the [`'session'`](https://nodejs.org/docs/latest/api/tls.html#event-session) event to get the session data, and provide the data to the `session` option of a subsequent [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback) to reuse the session. Servers must implement handlers for the [`'newSession'`](https://nodejs.org/docs/latest/api/tls.html#event-newsession) and [`'resumeSession'`](https://nodejs.org/docs/latest/api/tls.html#event-resumesession) events to save and restore the session data using the session ID as the lookup key to reuse sessions. To reuse sessions across load balancers or cluster workers, servers must use a shared session cache (such as Redis) in their session handlers.
##### Session tickets[#](https://nodejs.org/docs/latest/api/tls.html#session-tickets)
The servers encrypt the entire session state and send it to the client as a "ticket". When reconnecting, the state is sent to the server in the initial connection. This mechanism avoids the need for a server-side session cache. If the server doesn't use the ticket, for any reason (failure to decrypt it, it's too old, etc.), it will create a new session and send a new ticket. See
Resumption using session tickets is becoming commonly supported by many web browsers when making HTTPS requests.
For Node.js, clients use the same APIs for resumption with session identifiers as for resumption with session tickets. For debugging, if [`tls.TLSSocket.getTLSTicket()`](https://nodejs.org/docs/latest/api/tls.html#tlssocketgettlsticket) returns a value, the session data contains a ticket, otherwise it contains client-side session state.
With TLSv1.3, be aware that multiple tickets may be sent by the server, resulting in multiple `'session'` events, see [`'session'`](https://nodejs.org/docs/latest/api/tls.html#event-session) for more information.
Single process servers need no specific implementation to use session tickets. To use session tickets across server restarts or load balancers, servers must all have the same ticket keys. There are three 16-byte keys internally, but the tls API exposes them as a single 48-byte buffer for convenience.
It's possible to get the ticket keys by calling [`server.getTicketKeys()`](https://nodejs.org/docs/latest/api/tls.html#servergetticketkeys) on one server instance and then distribute them, but it is more reasonable to securely generate 48 bytes of secure random data and set them with the `ticketKeys` option of [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener). The keys should be regularly regenerated and server's keys can be reset with [`server.setTicketKeys()`](https://nodejs.org/docs/latest/api/tls.html#serversetticketkeyskeys).
Session ticket keys are cryptographic keys, and they _**must be stored securely**_. With TLS 1.2 and below, if they are compromised all sessions that used tickets encrypted with them can be decrypted. They should not be stored on disk, and they should be regenerated regularly.
If clients advertise support for tickets, the server will send them. The server can disable tickets by supplying `require('node:constants').SSL_OP_NO_TICKET` in `secureOptions`.
Both session identifiers and session tickets timeout, causing the server to create new sessions. The timeout can be configured with the `sessionTimeout` option of [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener).
For all the mechanisms, when resumption fails, servers will create new sessions. Since failing to resume the session does not cause TLS/HTTPS connection failures, it is easy to not notice unnecessarily poor TLS performance. The OpenSSL CLI can be used to verify that servers are resuming sessions. Use the `-reconnect` option to `openssl s_client`, for example:
```
openssl s_client -connect localhost:443 -reconnect
copy
```

Read through the debug output. The first connection should say "New", for example:
```
New, TLSv1.2, Cipher is ECDHE-RSA-AES128-GCM-SHA256
copy
```

Subsequent connections should say "Reused", for example:
```
Reused, TLSv1.2, Cipher is ECDHE-RSA-AES128-GCM-SHA256
copy
```

### Modifying the default TLS cipher suite[#](https://nodejs.org/docs/latest/api/tls.html#modifying-the-default-tls-cipher-suite)
Node.js is built with a default suite of enabled and disabled TLS ciphers. This default cipher list can be configured when building Node.js to allow distributions to provide their own default list.
The following command can be used to show the default cipher suite:
```
node -p crypto.constants.defaultCoreCipherList | tr ':' '\n'
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_GCM_SHA256
ECDHE-RSA-AES128-GCM-SHA256
ECDHE-ECDSA-AES128-GCM-SHA256
ECDHE-RSA-AES256-GCM-SHA384
ECDHE-ECDSA-AES256-GCM-SHA384
DHE-RSA-AES128-GCM-SHA256
ECDHE-RSA-AES128-SHA256
DHE-RSA-AES128-SHA256
ECDHE-RSA-AES256-SHA384
DHE-RSA-AES256-SHA384
ECDHE-RSA-AES256-SHA256
DHE-RSA-AES256-SHA256
HIGH
!annul
!eNULL
!EXPORT
!DES
!RC4
!MD5
!PSK
!SRP
!CAMELLIA
copy
```

This default can be replaced entirely using the [`--tls-cipher-list`](https://nodejs.org/docs/latest/api/cli.html#--tls-cipher-listlist) command-line switch (directly, or via the [`NODE_OPTIONS`](https://nodejs.org/docs/latest/api/cli.html#node_optionsoptions) environment variable). For instance, the following makes `ECDHE-RSA-AES128-GCM-SHA256:!RC4` the default TLS cipher suite:
```
node --tls-cipher-list='ECDHE-RSA-AES128-GCM-SHA256:!RC4' server.js

export NODE_OPTIONS=--tls-cipher-list='ECDHE-RSA-AES128-GCM-SHA256:!RC4'
node server.js
copy
```

To verify, use the following command to show the set cipher list, note the difference between `defaultCoreCipherList` and `defaultCipherList`:
```
node --tls-cipher-list='ECDHE-RSA-AES128-GCM-SHA256:!RC4' -p crypto.constants.defaultCipherList | tr ':' '\n'
ECDHE-RSA-AES128-GCM-SHA256
!RC4
copy
```

i.e. the `defaultCoreCipherList` list is set at compilation time and the `defaultCipherList` is set at runtime.
To modify the default cipher suites from within the runtime, modify the `tls.DEFAULT_CIPHERS` variable, this must be performed before listening on any sockets, it will not affect sockets already opened. For example:
```
// Remove Obsolete CBC Ciphers and RSA Key Exchange based Ciphers as they don't provide Forward Secrecy
tls.DEFAULT_CIPHERS +=
  ':!ECDHE-RSA-AES128-SHA:!ECDHE-RSA-AES128-SHA256:!ECDHE-RSA-AES256-SHA:!ECDHE-RSA-AES256-SHA384' +
  ':!ECDHE-ECDSA-AES128-SHA:!ECDHE-ECDSA-AES128-SHA256:!ECDHE-ECDSA-AES256-SHA:!ECDHE-ECDSA-AES256-SHA384' +
  ':!kRSA';
copy
```

The default can also be replaced on a per client or server basis using the `ciphers` option from [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions), which is also available in [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener), [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback), and when creating new [`tls.TLSSocket`](https://nodejs.org/docs/latest/api/tls.html#class-tlstlssocket)s.
The ciphers list can contain a mixture of TLSv1.3 cipher suite names, the ones that start with `'TLS_'`, and specifications for TLSv1.2 and below cipher suites. The TLSv1.2 ciphers support a legacy specification format, consult the OpenSSL _not_ apply to TLSv1.3 ciphers. The TLSv1.3 suites can only be enabled by including their full name in the cipher list. They cannot, for example, be enabled or disabled by using the legacy TLSv1.2 `'EECDH'` or `'!EECDH'` specification.
Despite the relative order of TLSv1.3 and TLSv1.2 cipher suites, the TLSv1.3 protocol is significantly more secure than TLSv1.2, and will always be chosen over TLSv1.2 if the handshake indicates it is supported, and if any TLSv1.3 cipher suites are enabled.
The default cipher suite included within Node.js has been carefully selected to reflect current security best practices and risk mitigation. Changing the default cipher suite can have a significant impact on the security of an application. The `--tls-cipher-list` switch and `ciphers` option should by used only if absolutely necessary.
The default cipher suite prefers GCM ciphers for _some_ backward compatibility.
Old clients that rely on insecure and deprecated RC4 or DES-based ciphers (like Internet Explorer 6) cannot complete the handshaking process with the default configuration. If these clients _must_ be supported, the
There are only five TLSv1.3 cipher suites:
  * `'TLS_AES_256_GCM_SHA384'`
  * `'TLS_CHACHA20_POLY1305_SHA256'`
  * `'TLS_AES_128_GCM_SHA256'`
  * `'TLS_AES_128_CCM_SHA256'`
  * `'TLS_AES_128_CCM_8_SHA256'`


The first three are enabled by default. The two `CCM`-based suites are supported by TLSv1.3 because they may be more performant on constrained systems, but they are not enabled by default since they offer less security.
### OpenSSL security level[#](https://nodejs.org/docs/latest/api/tls.html#openssl-security-level)
The OpenSSL library enforces security levels to control the minimum acceptable level of security for cryptographic operations. OpenSSL's security levels range from 0 to 5, with each level imposing stricter security requirements. The default security level is 2, which is generally suitable for most modern applications. However, some legacy features and protocols, such as TLSv1, require a lower security level (`SECLEVEL=0`) to function properly. For more detailed information, please refer to the
#### Setting security levels[#](https://nodejs.org/docs/latest/api/tls.html#setting-security-levels)
To adjust the security level in your Node.js application, you can include `@SECLEVEL=X` within a cipher string, where `X` is the desired security level. For example, to set the security level to 0 while using the default OpenSSL cipher list, you could use:
```
import { createServer, connect } from 'node:tls';
const port = 443;

createServer({ ciphers: 'DEFAULT@SECLEVEL=0', minVersion: 'TLSv1' }, function(socket) {
  console.log('Client connected with protocol:', socket.getProtocol());
  socket.end();
  this.close();
})
.listen(port, () => {
  connect(port, { ciphers: 'DEFAULT@SECLEVEL=0', maxVersion: 'TLSv1' });
});
const { createServer, connect } = require('node:tls');
const port = 443;

createServer({ ciphers: 'DEFAULT@SECLEVEL=0', minVersion: 'TLSv1' }, function(socket) {
  console.log('Client connected with protocol:', socket.getProtocol());
  socket.end();
  this.close();
})
.listen(port, () => {
  connect(port, { ciphers: 'DEFAULT@SECLEVEL=0', maxVersion: 'TLSv1' });
});
copy
```

This approach sets the security level to 0, allowing the use of legacy features while still leveraging the default OpenSSL ciphers.
#### Using [`--tls-cipher-list`](https://nodejs.org/docs/latest/api/cli.html#--tls-cipher-listlist)[#](https://nodejs.org/docs/latest/api/tls.html#using-tls-cipher-list)
You can also set the security level and ciphers from the command line using the `--tls-cipher-list=DEFAULT@SECLEVEL=X` as described in [Modifying the default TLS cipher suite](https://nodejs.org/docs/latest/api/tls.html#modifying-the-default-tls-cipher-suite). However, it is generally discouraged to use the command line option for setting ciphers and it is preferable to configure the ciphers for individual contexts within your application code, as this approach provides finer control and reduces the risk of globally downgrading the security level.
### X509 certificate error codes[#](https://nodejs.org/docs/latest/api/tls.html#x509-certificate-error-codes)
Multiple functions can fail due to certificate errors that are reported by OpenSSL. In such a case, the function provides an `code` which can take one of the following values:
  * `'UNABLE_TO_GET_ISSUER_CERT'`: Unable to get issuer certificate.
  * `'UNABLE_TO_GET_CRL'`: Unable to get certificate CRL.
  * `'UNABLE_TO_DECRYPT_CERT_SIGNATURE'`: Unable to decrypt certificate's signature.
  * `'UNABLE_TO_DECRYPT_CRL_SIGNATURE'`: Unable to decrypt CRL's signature.
  * `'UNABLE_TO_DECODE_ISSUER_PUBLIC_KEY'`: Unable to decode issuer public key.
  * `'CERT_SIGNATURE_FAILURE'`: Certificate signature failure.
  * `'CRL_SIGNATURE_FAILURE'`: CRL signature failure.
  * `'CERT_NOT_YET_VALID'`: Certificate is not yet valid.
  * `'CERT_HAS_EXPIRED'`: Certificate has expired.
  * `'CRL_NOT_YET_VALID'`: CRL is not yet valid.
  * `'CRL_HAS_EXPIRED'`: CRL has expired.
  * `'ERROR_IN_CERT_NOT_BEFORE_FIELD'`: Format error in certificate's notBefore field.
  * `'ERROR_IN_CERT_NOT_AFTER_FIELD'`: Format error in certificate's notAfter field.
  * `'ERROR_IN_CRL_LAST_UPDATE_FIELD'`: Format error in CRL's lastUpdate field.
  * `'ERROR_IN_CRL_NEXT_UPDATE_FIELD'`: Format error in CRL's nextUpdate field.
  * `'OUT_OF_MEM'`: Out of memory.
  * `'DEPTH_ZERO_SELF_SIGNED_CERT'`: Self signed certificate.
  * `'SELF_SIGNED_CERT_IN_CHAIN'`: Self signed certificate in certificate chain.
  * `'UNABLE_TO_GET_ISSUER_CERT_LOCALLY'`: Unable to get local issuer certificate.
  * `'UNABLE_TO_VERIFY_LEAF_SIGNATURE'`: Unable to verify the first certificate.
  * `'CERT_CHAIN_TOO_LONG'`: Certificate chain too long.
  * `'CERT_REVOKED'`: Certificate revoked.
  * `'INVALID_CA'`: Invalid CA certificate.
  * `'PATH_LENGTH_EXCEEDED'`: Path length constraint exceeded.
  * `'INVALID_PURPOSE'`: Unsupported certificate purpose.
  * `'CERT_UNTRUSTED'`: Certificate not trusted.
  * `'CERT_REJECTED'`: Certificate rejected.
  * `'HOSTNAME_MISMATCH'`: Hostname mismatch.


When certificate errors like `UNABLE_TO_VERIFY_LEAF_SIGNATURE`, `DEPTH_ZERO_SELF_SIGNED_CERT`, or `UNABLE_TO_GET_ISSUER_CERT` occur, Node.js appends a hint suggesting that if the root CA is installed locally, try running with the `--use-system-ca` flag to direct developers towards a secure solution, to prevent unsafe workarounds.
### Class: `tls.Server`[#](https://nodejs.org/docs/latest/api/tls.html#class-tlsserver)
Added in: v0.3.2
  * Extends: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Accepts encrypted connections using TLS or SSL.
#### Event: `'connection'`[#](https://nodejs.org/docs/latest/api/tls.html#event-connection)
Added in: v0.3.2
  * `socket` [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


This event is emitted when a new TCP stream is established, before the TLS handshake begins. `socket` is typically an object of type [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) but will not receive events unlike the socket created from the [`net.Server`](https://nodejs.org/docs/latest/api/net.html#class-netserver) `'connection'` event. Usually users will not want to access this event.
This event can also be explicitly emitted by users to inject connections into the TLS server. In that case, any [`Duplex`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex) stream can be passed.
#### Event: `'keylog'`[#](https://nodejs.org/docs/latest/api/tls.html#event-keylog)
Added in: v12.3.0, v10.20.0
  * `line` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) Line of ASCII text, in NSS `SSLKEYLOGFILE` format.
  * `tlsSocket` [`<tls.TLSSocket>`](https://nodejs.org/docs/latest/api/tls.html#tlstlssocket) The `tls.TLSSocket` instance on which it was generated.


The `keylog` event is emitted when key material is generated or received by a connection to this server (typically before handshake has completed, but not necessarily). This keying material can be stored for debugging, as it allows captured TLS traffic to be decrypted. It may be emitted multiple times for each socket.
A typical use case is to append received lines to a common text file, which is later used by software (such as Wireshark) to decrypt the traffic:
```
const logFile = fs.createWriteStream('/tmp/ssl-keys.log', { flags: 'a' });
// ...
server.on('keylog', (line, tlsSocket) => {
