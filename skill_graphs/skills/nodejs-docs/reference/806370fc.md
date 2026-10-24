    * `sigalgs` `SHA256`, `MD5` etc.), public key algorithms (`RSA-PSS`, `ECDSA` etc.), combination of both (e.g 'RSA+SHA384') or TLS v1.3 scheme names (e.g. `rsa_pss_pss_sha512`). See
    * `ciphers` [Modifying the default TLS cipher suite](https://nodejs.org/docs/latest/api/tls.html#modifying-the-default-tls-cipher-suite). Permitted ciphers can be obtained via [`tls.getCiphers()`](https://nodejs.org/docs/latest/api/tls.html#tlsgetciphers). Cipher names must be uppercased in order for OpenSSL to accept them.
    * `clientCertEngine` **Deprecated.**
    * `crl` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) PEM formatted CRLs (Certificate Revocation Lists).
    * `dhparam` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) `'auto'` or custom Diffie-Hellman parameters, required for non-ECDHE [perfect forward secrecy](https://nodejs.org/docs/latest/api/tls.html#perfect-forward-secrecy). If omitted or invalid, the parameters are silently discarded and DHE ciphers will not be available. [perfect forward secrecy](https://nodejs.org/docs/latest/api/tls.html#perfect-forward-secrecy) will still be available.
    * `ecdhCurve` `P-521:P-384:P-256`, to use for ECDH key agreement. Set to `auto` to select the curve automatically. Use [`crypto.getCurves()`](https://nodejs.org/docs/latest/api/crypto.html#cryptogetcurves) to obtain a list of available curve names. On recent releases, `openssl ecparam -list_curves` will also display the name and description of each available elliptic curve. **Default:** [`tls.DEFAULT_ECDH_CURVE`](https://nodejs.org/docs/latest/api/tls.html#tlsdefault_ecdh_curve).
    * `honorCipherOrder` `true`, causes `SSL_OP_CIPHER_SERVER_PREFERENCE` to be set in `secureOptions`, see [OpenSSL Options](https://nodejs.org/docs/latest/api/crypto.html#openssl-options) for more information.
    * `key` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `options.passphrase`. Multiple keys using different algorithms can be provided either as an array of unencrypted key strings or buffers, or an array of objects in the form `{pem: <string|buffer>[, passphrase: <string>]}`. The object form can only occur in an array. `object.passphrase` is optional. Encrypted keys will be decrypted with `object.passphrase` if provided, or `options.passphrase` if it is not.
    * `privateKeyEngine` `privateKeyIdentifier`. **Deprecated.**
    * `privateKeyIdentifier` `privateKeyEngine`. Should not be set together with `key`, because both options define a private key in different ways. **Deprecated.**
    * `maxVersion` `'TLSv1.3'`, `'TLSv1.2'`, `'TLSv1.1'`, or `'TLSv1'`. Cannot be specified along with the `secureProtocol` option; use one or the other. **Default:** [`tls.DEFAULT_MAX_VERSION`](https://nodejs.org/docs/latest/api/tls.html#tlsdefault_max_version).
    * `minVersion` `'TLSv1.3'`, `'TLSv1.2'`, `'TLSv1.1'`, or `'TLSv1'`. Cannot be specified along with the `secureProtocol` option; use one or the other. Avoid setting to less than TLSv1.2, but it may be required for interoperability. Versions before TLSv1.2 may require downgrading the [OpenSSL Security Level](https://nodejs.org/docs/latest/api/tls.html#openssl-security-level). **Default:** [`tls.DEFAULT_MIN_VERSION`](https://nodejs.org/docs/latest/api/tls.html#tlsdefault_min_version).
    * `passphrase`
    * `pfx` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | [`<Buffer[]>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `pfx` is an alternative to providing `key` and `cert` individually. PFX is usually encrypted, if it is, `passphrase` will be used to decrypt it. Multiple PFX can be provided either as an array of unencrypted PFX buffers, or an array of objects in the form `{buf: <string|buffer>[, passphrase: <string>]}`. The object form can only occur in an array. `object.passphrase` is optional. Encrypted PFX will be decrypted with `object.passphrase` if provided, or `options.passphrase` if it is not.
    * `secureOptions` `SSL_OP_*` options from [OpenSSL Options](https://nodejs.org/docs/latest/api/crypto.html#openssl-options).
    * `secureProtocol` `minVersion` and `maxVersion` instead. The possible values are listed as `'TLSv1_1_method'` to force TLS version 1.1, or `'TLS_method'` to allow any TLS protocol version up to TLSv1.3. It is not recommended to use TLS versions less than 1.2, but it may be required for interoperability. **Default:** none, see `minVersion`.
    * `sessionIdContext`
    * `ticketKeys` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) 48-bytes of cryptographically strong pseudorandom data. See [Session Resumption](https://nodejs.org/docs/latest/api/tls.html#session-resumption) for more information.
    * `sessionTimeout` [Session Resumption](https://nodejs.org/docs/latest/api/tls.html#session-resumption) for more information. **Default:** `300`.


[`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener) sets the default value of the `honorCipherOrder` option to `true`, other APIs that create secure contexts leave it unset.
[`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener) uses a 128 bit truncated SHA1 hash value generated from `process.argv` as the default value of the `sessionIdContext` option, other APIs that create secure contexts have no default value.
The `tls.createSecureContext()` method creates a `SecureContext` object. It is usable as an argument to several `tls` APIs, such as [`server.addContext()`](https://nodejs.org/docs/latest/api/tls.html#serveraddcontexthostname-context), but has no public methods. The [`tls.Server`](https://nodejs.org/docs/latest/api/tls.html#class-tlsserver) constructor and the [`tls.createServer()`](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener) method do not support the `secureContext` option.
A key is _required_ for ciphers that use certificates. Either `key` or `pfx` can be used to provide it.
If the `ca` option is not given, then Node.js will default to using
Custom DHE parameters are discouraged in favor of the new `dhparam: 'auto'` option. When set to `'auto'`, well-known DHE parameters of sufficient strength will be selected automatically. Otherwise, if necessary, `openssl dhparam` can be used to create custom parameters. The key length must be greater than or equal to 1024 bits or else an error will be thrown. Although 1024 bits is permissible, use 2048 bits or larger for stronger security.
###  `tls.createServer([options][, secureConnectionListener])`[#](https://nodejs.org/docs/latest/api/tls.html#tlscreateserveroptions-secureconnectionlistener)
Added in: v0.3.2History Version | Changes
---|---
v22.4.0, v20.16.0 | The `clientCertEngine` option depends on custom engine support in OpenSSL which is deprecated in OpenSSL 3.
v20.4.0, v18.19.0 | The `options` parameter can now include `ALPNCallback`.
v19.0.0 | If `ALPNProtocols` is set, incoming connections that send an ALPN extension with no supported protocols are terminated with a fatal `no_application_protocol` alert.
v12.3.0 | The `options` parameter now supports `net.createServer()` options.
v9.3.0 | The `options` parameter can now include `clientCertEngine`.
v8.0.0 | The `ALPNProtocols` option can be a `TypedArray` or `DataView` now.
v5.0.0 | ALPN options are supported now.
  * `options`
    * `ALPNProtocols` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) | `Buffer`, `TypedArray`, or `DataView` containing the supported ALPN protocols. Buffers should have the format `[len][name][len][name]...` e.g. `0x05hello0x05world`, where the first byte is the length of the next protocol name. Passing an array is usually much simpler, e.g. `['hello', 'world']`. (Protocols should be ordered by their priority.)
    * `ALPNCallback` `servername` and `protocols` fields, respectively containing the server name from the SNI extension (if any) and an array of ALPN protocol name strings. The callback must return either one of the strings listed in `protocols`, which will be returned to the client as the selected ALPN protocol, or `undefined`, to reject the connection with a fatal alert. If a string is returned that does not match one of the client's ALPN protocols, an error will be thrown. This option cannot be used with the `ALPNProtocols` option, and setting both options will throw an error.
    * `clientCertEngine` **Deprecated.**
    * `enableTrace` `true`, [`tls.TLSSocket.enableTrace()`](https://nodejs.org/docs/latest/api/tls.html#tlssocketenabletrace) will be called on new connections. Tracing can be enabled after the secure connection is established, but this option must be used to trace the secure connection setup. **Default:** `false`.
    * `handshakeTimeout` `'tlsClientError'` is emitted on the `tls.Server` object whenever a handshake times out. **Default:** `120000` (120 seconds).
    * `rejectUnauthorized` `false` the server will reject any connection which is not authorized with the list of supplied CAs. This option only has an effect if `requestCert` is `true`. **Default:** `true`.
    * `requestCert` `true` the server will request a certificate from clients that connect and attempt to verify that certificate. **Default:** `false`.
    * `sessionTimeout` [Session Resumption](https://nodejs.org/docs/latest/api/tls.html#session-resumption) for more information. **Default:** `300`.
    * `SNICallback(servername, callback)` `servername` and `callback`. `callback` is an error-first callback that takes two optional arguments: `error` and `ctx`. `ctx`, if provided, is a `SecureContext` instance. [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) can be used to get a proper `SecureContext`. If `callback` is called with a falsy `ctx` argument, the default secure context of the server will be used. If `SNICallback` wasn't provided the default callback with high-level API will be used (see below).
    * `ticketKeys` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) 48-bytes of cryptographically strong pseudorandom data. See [Session Resumption](https://nodejs.org/docs/latest/api/tls.html#session-resumption) for more information.
    * `pskCallback` [Pre-shared keys](https://nodejs.org/docs/latest/api/tls.html#pre-shared-keys).
    * `pskIdentityHint` `'tlsClientError'` will be emitted with `'ERR_TLS_PSK_SET_IDENTITY_HINT_FAILED'` code.
    * ...: Any [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) option can be provided. For servers, the identity options (`pfx`, `key`/`cert`, or `pskCallback`) are usually required.
    * ...: Any [`net.createServer()`](https://nodejs.org/docs/latest/api/net.html#netcreateserveroptions-connectionlistener) option can be provided.
  * `secureConnectionListener`
  * Returns: [`<tls.Server>`](https://nodejs.org/docs/latest/api/tls.html#class-tlsserver)


Creates a new [`tls.Server`](https://nodejs.org/docs/latest/api/tls.html#class-tlsserver). The `secureConnectionListener`, if provided, is automatically set as a listener for the [`'secureConnection'`](https://nodejs.org/docs/latest/api/tls.html#event-secureconnection) event.
The `ticketKeys` options is automatically shared between `node:cluster` module workers.
The following illustrates a simple echo server:
```
import { createServer } from 'node:tls';
import { readFileSync } from 'node:fs';

const options = {
  key: readFileSync('server-key.pem'),
  cert: readFileSync('server-cert.pem'),

  // This is necessary only if using client certificate authentication.
  requestCert: true,

  // This is necessary only if the client uses a self-signed certificate.
  ca: [ readFileSync('client-cert.pem') ],
};

const server = createServer(options, (socket) => {
  console.log('server connected',
              socket.authorized ? 'authorized' : 'unauthorized');
  socket.write('welcome!\n');
  socket.setEncoding('utf8');
  socket.pipe(socket);
});
server.listen(8000, () => {
  console.log('server bound');
});
const { createServer } = require('node:tls');
const { readFileSync } = require('node:fs');

const options = {
  key: readFileSync('server-key.pem'),
  cert: readFileSync('server-cert.pem'),

  // This is necessary only if using client certificate authentication.
  requestCert: true,

  // This is necessary only if the client uses a self-signed certificate.
  ca: [ readFileSync('client-cert.pem') ],
};

const server = createServer(options, (socket) => {
  console.log('server connected',
              socket.authorized ? 'authorized' : 'unauthorized');
  socket.write('welcome!\n');
  socket.setEncoding('utf8');
  socket.pipe(socket);
});
server.listen(8000, () => {
  console.log('server bound');
});
copy
```

To generate the certificate and key for this example, run:
```
openssl req -x509 -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost' \
  -keyout server-key.pem -out server-cert.pem
copy
```

Then, to generate the `client-cert.pem` certificate for this example, run:
```
openssl pkcs12 -certpbe AES-256-CBC -export -out client-cert.pem \
  -inkey server-key.pem -in server-cert.pem
copy
```

The server can be tested by connecting to it using the example client from [`tls.connect()`](https://nodejs.org/docs/latest/api/tls.html#tlsconnectoptions-callback).
###  `tls.setDefaultCACertificates(certs)`[#](https://nodejs.org/docs/latest/api/tls.html#tlssetdefaultcacertificatescerts)
Added in: v24.5.0, v22.19.0
  * `certs`


Sets the default CA certificates used by Node.js TLS clients. If the provided certificates are parsed successfully, they will become the default CA certificate list returned by [`tls.getCACertificates()`](https://nodejs.org/docs/latest/api/tls.html#tlsgetcacertificatestype) and used by subsequent TLS connections that don't specify their own CA certificates. The certificates will be deduplicated before being set as the default.
This function only affects the current Node.js thread. Previous sessions cached by the HTTPS agent won't be affected by this change, so this method should be called before any unwanted cacheable TLS connections are made.
To use system CA certificates as the default:
```
const tls = require('node:tls');
tls.setDefaultCACertificates(tls.getCACertificates('system'));
import tls from 'node:tls';
tls.setDefaultCACertificates(tls.getCACertificates('system'));
copy
```

This function completely replaces the default CA certificate list. To add additional certificates to the existing defaults, get the current certificates and append to them:
```
const tls = require('node:tls');
const currentCerts = tls.getCACertificates('default');
const additionalCerts = ['-----BEGIN CERTIFICATE-----\n...'];
tls.setDefaultCACertificates([...currentCerts, ...additionalCerts]);
import tls from 'node:tls';
const currentCerts = tls.getCACertificates('default');
const additionalCerts = ['-----BEGIN CERTIFICATE-----\n...'];
tls.setDefaultCACertificates([...currentCerts, ...additionalCerts]);
copy
```

###  `tls.getCACertificates([type])`[#](https://nodejs.org/docs/latest/api/tls.html#tlsgetcacertificatestype)
Added in: v23.10.0, v22.15.0
  * `type` `"default"`, `"system"`, `"bundled"` and `"extra"`. **Default:** `"default"`.
  * Returns:


Returns an array containing the CA certificates from various sources, depending on `type`:
  * `"default"`: return the CA certificates that will be used by the Node.js TLS clients by default.
    * When [`--use-bundled-ca`](https://nodejs.org/docs/latest/api/cli.html#--use-bundled-ca---use-openssl-ca) is enabled (default), or [`--use-openssl-ca`](https://nodejs.org/docs/latest/api/cli.html#--use-bundled-ca---use-openssl-ca) is not enabled, this would include CA certificates from the bundled Mozilla CA store.
    * When [`--use-system-ca`](https://nodejs.org/docs/latest/api/cli.html#--use-system-ca) is enabled, this would also include certificates from the system's trusted store.
    * When [`NODE_EXTRA_CA_CERTS`](https://nodejs.org/docs/latest/api/cli.html#node_extra_ca_certsfile) is used, this would also include certificates loaded from the specified file.
  * `"system"`: return the CA certificates that are loaded from the system's trusted store, according to rules set by [`--use-system-ca`](https://nodejs.org/docs/latest/api/cli.html#--use-system-ca). This can be used to get the certificates from the system when [`--use-system-ca`](https://nodejs.org/docs/latest/api/cli.html#--use-system-ca) is not enabled.
  * `"bundled"`: return the CA certificates from the bundled Mozilla CA store. This would be the same as [`tls.rootCertificates`](https://nodejs.org/docs/latest/api/tls.html#tlsrootcertificates).
  * `"extra"`: return the CA certificates loaded from [`NODE_EXTRA_CA_CERTS`](https://nodejs.org/docs/latest/api/cli.html#node_extra_ca_certsfile). It's an empty array if [`NODE_EXTRA_CA_CERTS`](https://nodejs.org/docs/latest/api/cli.html#node_extra_ca_certsfile) is not set.


###  `tls.getCiphers()`[#](https://nodejs.org/docs/latest/api/tls.html#tlsgetciphers)
Added in: v0.10.2
  * Returns:


Returns an array with the names of the supported TLS ciphers. The names are lower-case for historical reasons, but must be uppercased to be used in the `ciphers` option of [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions).
Not all supported ciphers are enabled by default. See [Modifying the default TLS cipher suite](https://nodejs.org/docs/latest/api/tls.html#modifying-the-default-tls-cipher-suite).
Cipher names that start with `'tls_'` are for TLSv1.3, all the others are for TLSv1.2 and below.
```
console.log(tls.getCiphers()); // ['aes128-gcm-sha256', 'aes128-sha', ...]
copy
```

###  `tls.rootCertificates`[#](https://nodejs.org/docs/latest/api/tls.html#tlsrootcertificates)
Added in: v12.3.0
  * Type:


An immutable array of strings representing the root certificates (in PEM format) from the bundled Mozilla CA store as supplied by the current Node.js version.
The bundled CA store, as supplied by Node.js, is a snapshot of Mozilla CA store that is fixed at release time. It is identical on all supported platforms.
To get the actual CA certificates used by the current Node.js instance, which may include certificates loaded from the system store (if `--use-system-ca` is used) or loaded from a file indicated by `NODE_EXTRA_CA_CERTS`, use [`tls.getCACertificates()`](https://nodejs.org/docs/latest/api/tls.html#tlsgetcacertificatestype).
###  `tls.DEFAULT_ECDH_CURVE`[#](https://nodejs.org/docs/latest/api/tls.html#tlsdefault-ecdh-curve)
Added in: v0.11.13History Version | Changes
---|---
v10.0.0 | Default value changed to `'auto'`.
The default curve name to use for ECDH key agreement in a tls server. The default value is `'auto'`. See [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions) for further information.
###  `tls.DEFAULT_MAX_VERSION`[#](https://nodejs.org/docs/latest/api/tls.html#tlsdefault-max-version)
Added in: v11.4.0
  * Type: `maxVersion` option of [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions). It can be assigned any of the supported TLS protocol versions, `'TLSv1.3'`, `'TLSv1.2'`, `'TLSv1.1'`, or `'TLSv1'`. **Default:** `'TLSv1.3'`, unless changed using CLI options. Using `--tls-max-v1.2` sets the default to `'TLSv1.2'`. Using `--tls-max-v1.3` sets the default to `'TLSv1.3'`. If multiple of the options are provided, the highest maximum is used.


###  `tls.DEFAULT_MIN_VERSION`[#](https://nodejs.org/docs/latest/api/tls.html#tlsdefault-min-version)
Added in: v11.4.0
  * Type: `minVersion` option of [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions). It can be assigned any of the supported TLS protocol versions, `'TLSv1.3'`, `'TLSv1.2'`, `'TLSv1.1'`, or `'TLSv1'`. Versions before TLSv1.2 may require downgrading the [OpenSSL Security Level](https://nodejs.org/docs/latest/api/tls.html#openssl-security-level). **Default:** `'TLSv1.2'`, unless changed using CLI options. Using `--tls-min-v1.0` sets the default to `'TLSv1'`. Using `--tls-min-v1.1` sets the default to `'TLSv1.1'`. Using `--tls-min-v1.3` sets the default to `'TLSv1.3'`. If multiple of the options are provided, the lowest minimum is used.


###  `tls.DEFAULT_CIPHERS`[#](https://nodejs.org/docs/latest/api/tls.html#tlsdefault-ciphers)
Added in: v0.11.3
  * Type: `ciphers` option of [`tls.createSecureContext()`](https://nodejs.org/docs/latest/api/tls.html#tlscreatesecurecontextoptions). It can be assigned any of the supported OpenSSL ciphers. Defaults to the content of `crypto.constants.defaultCoreCipherList`, unless changed using CLI options using `--tls-default-ciphers`.
