    * `blockList` [`<net.BlockList>`](https://nodejs.org/docs/latest/api/net.html#class-netblocklist) `blockList` can be used for disabling outbound access to specific IP addresses, IP ranges, or IP subnets.
    * `fd`
    * `keepAlive` `true`, it enables keep-alive functionality on the socket immediately after the connection is established, similarly on what is done in [`socket.setKeepAlive()`](https://nodejs.org/docs/latest/api/net.html#socketsetkeepaliveenable-initialdelay). **Default:** `false`.
    * `keepAliveInitialDelay` **Default:** `0`.
    * `noDelay` `true`, it disables the use of Nagle's algorithm immediately after the socket is established. **Default:** `false`.
    * `onread` `buffer` and passed to the supplied `callback` when data arrives on the socket. This will cause the streaming functionality to not provide any data. The socket will emit events like `'error'`, `'end'`, and `'close'` as usual. Methods like `pause()` and `resume()` will also behave as expected.
      * `buffer` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
      * `callback` `buffer` and a reference to `buffer`. Return `false` from this function to implicitly `pause()` the socket. This function will be executed in the global context.
    * `readable` `fd` is passed, otherwise ignored. **Default:** `false`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) An Abort signal that may be used to destroy the socket.
    * `typeOfService`
    * `writable` `fd` is passed, otherwise ignored. **Default:** `false`.
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)


Creates a new socket object.
The newly created socket can be either a TCP socket or a streaming [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) endpoint, depending on what it [`connect()`](https://nodejs.org/docs/latest/api/net.html#socketconnect) to.
#### Event: `'close'`[#](https://nodejs.org/docs/latest/api/net.html#event-close-1)
Added in: v0.1.90
  * `hadError` `true` if the socket had a transmission error.


Emitted once the socket is fully closed. The argument `hadError` is a boolean which says if the socket was closed due to a transmission error.
#### Event: `'connect'`[#](https://nodejs.org/docs/latest/api/net.html#event-connect)
Added in: v0.1.90
Emitted when a socket connection is successfully established. See [`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnection).
#### Event: `'connectionAttempt'`[#](https://nodejs.org/docs/latest/api/net.html#event-connectionattempt)
Added in: v21.6.0, v20.12.0
  * `ip`
  * `port`
  * `family` `6` for IPv6 or `4` for IPv4.


Emitted when a new connection attempt is started. This may be emitted multiple times if the family autoselection algorithm is enabled in [`socket.connect(options)`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener).
#### Event: `'connectionAttemptFailed'`[#](https://nodejs.org/docs/latest/api/net.html#event-connectionattemptfailed)
Added in: v21.6.0, v20.12.0
  * `ip`
  * `port`
  * `family` `6` for IPv6 or `4` for IPv4.
  * `error`


Emitted when a connection attempt failed. This may be emitted multiple times if the family autoselection algorithm is enabled in [`socket.connect(options)`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener).
#### Event: `'connectionAttemptTimeout'`[#](https://nodejs.org/docs/latest/api/net.html#event-connectionattempttimeout)
Added in: v21.6.0, v20.12.0
  * `ip`
  * `port`
  * `family` `6` for IPv6 or `4` for IPv4.


Emitted when a connection attempt timed out. This is only emitted (and may be emitted multiple times) if the family autoselection algorithm is enabled in [`socket.connect(options)`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener).
#### Event: `'data'`[#](https://nodejs.org/docs/latest/api/net.html#event-data)
Added in: v0.1.90
  * Type: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |


Emitted when data is received. The argument `data` will be a `Buffer` or `String`. Encoding of data is set by [`socket.setEncoding()`](https://nodejs.org/docs/latest/api/net.html#socketsetencodingencoding).
The data will be lost if there is no listener when a `Socket` emits a `'data'` event.
#### Event: `'drain'`[#](https://nodejs.org/docs/latest/api/net.html#event-drain)
Added in: v0.1.90
Emitted when the write buffer becomes empty. Can be used to throttle uploads.
See also: the return values of `socket.write()`.
#### Event: `'end'`[#](https://nodejs.org/docs/latest/api/net.html#event-end)
Added in: v0.1.90
Emitted when the other end of the socket signals the end of transmission, thus ending the readable side of the socket.
By default (`allowHalfOpen` is `false`) the socket will send an end of transmission packet back and destroy its file descriptor once it has written out its pending write queue. However, if `allowHalfOpen` is set to `true`, the socket will not automatically [`end()`](https://nodejs.org/docs/latest/api/net.html#socketenddata-encoding-callback) its writable side, allowing the user to write arbitrary amounts of data. The user must call [`end()`](https://nodejs.org/docs/latest/api/net.html#socketenddata-encoding-callback) explicitly to close the connection (i.e. sending a FIN packet back).
#### Event: `'error'`[#](https://nodejs.org/docs/latest/api/net.html#event-error-1)
Added in: v0.1.90
  * Type:


Emitted when an error occurs. The `'close'` event will be called directly following this event.
#### Event: `'lookup'`[#](https://nodejs.org/docs/latest/api/net.html#event-lookup)
Added in: v0.11.3History Version | Changes
---|---
v5.10.0 | The `host` parameter is supported now.
Emitted after resolving the host name but before connecting. Not applicable to Unix sockets.
  * `err` [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback).
  * `address`
  * `family` [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback).
  * `host`


#### Event: `'ready'`[#](https://nodejs.org/docs/latest/api/net.html#event-ready)
Added in: v9.11.0
Emitted when a socket is ready to be used.
Triggered immediately after `'connect'`.
#### Event: `'timeout'`[#](https://nodejs.org/docs/latest/api/net.html#event-timeout)
Added in: v0.1.90
Emitted if the socket times out from inactivity. This is only to notify that the socket has been idle. The user must manually close the connection.
See also: [`socket.setTimeout()`](https://nodejs.org/docs/latest/api/net.html#socketsettimeouttimeout-callback).
####  `socket.address()`[#](https://nodejs.org/docs/latest/api/net.html#socketaddress)
Added in: v0.1.90History Version | Changes
---|---
v18.4.0 | The `family` property now returns a string instead of a number.
v18.0.0 | The `family` property now returns a number instead of a string.
  * Returns:


Returns the bound `address`, the address `family` name and `port` of the socket as reported by the operating system: `{ port: 12346, family: 'IPv4', address: '127.0.0.1' }`
####  `socket.autoSelectFamilyAttemptedAddresses`[#](https://nodejs.org/docs/latest/api/net.html#socketautoselectfamilyattemptedaddresses)
Added in: v19.4.0, v18.18.0
  * Type:


This property is only present if the family autoselection algorithm is enabled in [`socket.connect(options)`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener) and it is an array of the addresses that have been attempted.
Each address is a string in the form of `$IP:$PORT`. If the connection was successful, then the last address is the one that the socket is currently connected to.
####  `socket.bufferSize`[#](https://nodejs.org/docs/latest/api/net.html#socketbuffersize)
Added in: v0.3.8Deprecated in: v14.6.0
Stability: 0 - Deprecated: Use [`writable.writableLength`](https://nodejs.org/docs/latest/api/stream.html#writablewritablelength) instead.
  * Type:


This property shows the number of characters buffered for writing. The buffer may contain strings whose length after encoding is not yet known. So this number is only an approximation of the number of bytes in the buffer.
`net.Socket` has the property that `socket.write()` always works. This is to help users get up and running quickly. The computer cannot always keep up with the amount of data that is written to a socket. The network connection simply might be too slow. Node.js will internally queue up the data written to a socket and send it out over the wire when it is possible.
The consequence of this internal buffering is that memory may grow. Users who experience large or growing `bufferSize` should attempt to "throttle" the data flows in their program with [`socket.pause()`](https://nodejs.org/docs/latest/api/net.html#socketpause) and [`socket.resume()`](https://nodejs.org/docs/latest/api/net.html#socketresume).
####  `socket.bytesRead`[#](https://nodejs.org/docs/latest/api/net.html#socketbytesread)
Added in: v0.5.3
  * Type:


The amount of received bytes.
####  `socket.bytesWritten`[#](https://nodejs.org/docs/latest/api/net.html#socketbyteswritten)
Added in: v0.5.3
  * Type:


The amount of bytes sent.
####  `socket.connect()`[#](https://nodejs.org/docs/latest/api/net.html#socketconnect)
Initiate a connection on a given socket.
Possible signatures:
  * [`socket.connect(options[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener)
  * [`socket.connect(path[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectpath-connectlistener) for [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) connections.
  * [`socket.connect(port[, host][, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectport-host-connectlistener) for TCP connections.
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


This function is asynchronous. When the connection is established, the [`'connect'`](https://nodejs.org/docs/latest/api/net.html#event-connect) event will be emitted. If there is a problem connecting, instead of a [`'connect'`](https://nodejs.org/docs/latest/api/net.html#event-connect) event, an [`'error'`](https://nodejs.org/docs/latest/api/net.html#event-error_1) event will be emitted with the error passed to the [`'error'`](https://nodejs.org/docs/latest/api/net.html#event-error_1) listener. The last parameter `connectListener`, if supplied, will be added as a listener for the [`'connect'`](https://nodejs.org/docs/latest/api/net.html#event-connect) event **once**.
This function should only be used for reconnecting a socket after `'close'` has been emitted or otherwise it may lead to undefined behavior.
#####  `socket.connect(options[, connectListener])`[#](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener)
Added in: v0.1.90History Version | Changes
---|---
v20.0.0, v18.18.0 | The default value for the autoSelectFamily option is now true. The `--enable-network-family-autoselection` CLI flag has been renamed to `--network-family-autoselection`. The old name is now an alias but it is discouraged.
v19.4.0 | The default value for autoSelectFamily option can be changed at runtime using `setDefaultAutoSelectFamily` or via the command line option `--enable-network-family-autoselection`.
v19.3.0, v18.13.0 | Added the `autoSelectFamily` option.
v17.7.0, v16.15.0 | The `noDelay`, `keepAlive`, and `keepAliveInitialDelay` options are supported now.
v6.0.0 | The `hints` option defaults to `0` in all cases now. Previously, in the absence of the `family` option it would default to `dns.ADDRCONFIG | dns.V4MAPPED`.
v5.11.0 | The `hints` option is supported now.
  * `options`
  * `connectListener` [`socket.connect()`](https://nodejs.org/docs/latest/api/net.html#socketconnect) methods. Will be added as a listener for the [`'connect'`](https://nodejs.org/docs/latest/api/net.html#event-connect) event once.
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Initiate a connection on a given socket. Normally this method is not needed, the socket should be created and opened with [`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnection). Use this only when implementing a custom Socket.
For TCP connections, available `options` are:
  * `autoSelectFamily` `true`, it enables a family autodetection algorithm that loosely implements section 5 of `all` option passed to lookup is set to `true` and the sockets attempts to connect to all obtained IPv6 and IPv4 addresses, in sequence, until a connection is established. The first returned AAAA address is tried first, then the first returned A address, then the second returned AAAA address and so on. Each connection attempt (but the last one) is given the amount of time specified by the `autoSelectFamilyAttemptTimeout` option before timing out and trying the next address. Ignored if the `family` option is not `0` or if `localAddress` is set. Connection errors are not emitted if at least one connection succeeds. If all connections attempts fails, a single `AggregateError` with all failed attempts is emitted. **Default:** [`net.getDefaultAutoSelectFamily()`](https://nodejs.org/docs/latest/api/net.html#netgetdefaultautoselectfamily).
  * `autoSelectFamilyAttemptTimeout` `autoSelectFamily` option. If set to a positive integer less than `10`, then the value `10` will be used instead. **Default:** [`net.getDefaultAutoSelectFamilyAttemptTimeout()`](https://nodejs.org/docs/latest/api/net.html#netgetdefaultautoselectfamilyattempttimeout).
  * `family` `4`, `6`, or `0`. The value `0` indicates that both IPv4 and IPv6 addresses are allowed. **Default:** `0`.
  * `hints` [`dns.lookup()` hints](https://nodejs.org/docs/latest/api/dns.html#supported-getaddrinfo-flags).
  * `host` **Default:** `'localhost'`.
  * `localAddress`
  * `localPort`
  * `lookup` **Default:** [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback).
  * `port`


For [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) connections, available `options` are:
  * `path` [Identifying paths for IPC connections](https://nodejs.org/docs/latest/api/net.html#identifying-paths-for-ipc-connections). If provided, the TCP-specific options above are ignored.


#####  `socket.connect(path[, connectListener])`[#](https://nodejs.org/docs/latest/api/net.html#socketconnectpath-connectlistener)
  * `path` [Identifying paths for IPC connections](https://nodejs.org/docs/latest/api/net.html#identifying-paths-for-ipc-connections).
  * `connectListener` [`socket.connect()`](https://nodejs.org/docs/latest/api/net.html#socketconnect) methods. Will be added as a listener for the [`'connect'`](https://nodejs.org/docs/latest/api/net.html#event-connect) event once.
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Initiate an [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) connection on the given socket.
Alias to [`socket.connect(options[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener) called with `{ path: path }` as `options`.
#####  `socket.connect(port[, host][, connectListener])`[#](https://nodejs.org/docs/latest/api/net.html#socketconnectport-host-connectlistener)
Added in: v0.1.90
  * `port`
  * `host`
  * `connectListener` [`socket.connect()`](https://nodejs.org/docs/latest/api/net.html#socketconnect) methods. Will be added as a listener for the [`'connect'`](https://nodejs.org/docs/latest/api/net.html#event-connect) event once.
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Initiate a TCP connection on the given socket.
Alias to [`socket.connect(options[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener) called with `{port: port, host: host}` as `options`.
####  `socket.connecting`[#](https://nodejs.org/docs/latest/api/net.html#socketconnecting)
Added in: v6.1.0
  * Type:


If `true`, [`socket.connect(options[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener) was called and has not yet finished. It will stay `true` until the socket becomes connected, then it is set to `false` and the `'connect'` event is emitted. Note that the [`socket.connect(options[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener) callback is a listener for the `'connect'` event.
####  `socket.destroy([error])`[#](https://nodejs.org/docs/latest/api/net.html#socketdestroyerror)
Added in: v0.1.90
  * `error`
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)


Ensures that no more I/O activity happens on this socket. Destroys the stream and closes the connection.
See [`writable.destroy()`](https://nodejs.org/docs/latest/api/stream.html#writabledestroyerror) for further details.
####  `socket.destroyed`[#](https://nodejs.org/docs/latest/api/net.html#socketdestroyed)
  * Type:


See [`writable.destroyed`](https://nodejs.org/docs/latest/api/stream.html#writabledestroyed) for further details.
####  `socket.destroySoon()`[#](https://nodejs.org/docs/latest/api/net.html#socketdestroysoon)
Added in: v0.3.4
Destroys the socket after all data is written. If the `'finish'` event was already emitted the socket is destroyed immediately. If the socket is still writable it implicitly calls `socket.end()`.
####  `socket.end([data[, encoding]][, callback])`[#](https://nodejs.org/docs/latest/api/net.html#socketenddata-encoding-callback)
Added in: v0.1.90
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` `string`. **Default:** `'utf8'`.
  * `callback`
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Half-closes the socket. i.e., it sends a FIN packet. It is possible the server will still send some data.
See [`writable.end()`](https://nodejs.org/docs/latest/api/stream.html#writableendchunk-encoding-callback) for further details.
####  `socket.localAddress`[#](https://nodejs.org/docs/latest/api/net.html#socketlocaladdress)
Added in: v0.9.6
  * Type:


The string representation of the local IP address the remote client is connecting on. For example, in a server listening on `'0.0.0.0'`, if a client connects on `'192.168.1.1'`, the value of `socket.localAddress` would be `'192.168.1.1'`.
####  `socket.localPort`[#](https://nodejs.org/docs/latest/api/net.html#socketlocalport)
Added in: v0.9.6
  * Type:


The numeric representation of the local port. For example, `80` or `21`.
####  `socket.localFamily`[#](https://nodejs.org/docs/latest/api/net.html#socketlocalfamily)
Added in: v18.8.0, v16.18.0
  * Type:


The string representation of the local IP family. `'IPv4'` or `'IPv6'`.
####  `socket.pause()`[#](https://nodejs.org/docs/latest/api/net.html#socketpause)
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Pauses the reading of data. That is, [`'data'`](https://nodejs.org/docs/latest/api/net.html#event-data) events will not be emitted. Useful to throttle back an upload.
####  `socket.pending`[#](https://nodejs.org/docs/latest/api/net.html#socketpending)
Added in: v11.2.0, v10.16.0
  * Type:


This is `true` if the socket is not connected yet, either because `.connect()` has not yet been called or because it is still in the process of connecting (see [`socket.connecting`](https://nodejs.org/docs/latest/api/net.html#socketconnecting)).
####  `socket.ref()`[#](https://nodejs.org/docs/latest/api/net.html#socketref)
Added in: v0.9.1
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Opposite of `unref()`, calling `ref()` on a previously `unref`ed socket will _not_ let the program exit if it's the only socket left (the default behavior). If the socket is `ref`ed calling `ref` again will have no effect.
####  `socket.remoteAddress`[#](https://nodejs.org/docs/latest/api/net.html#socketremoteaddress)
Added in: v0.5.10
  * Type:


The string representation of the remote IP address. For example, `'74.125.127.100'` or `'2001:4860:a005::68'`. Value may be `undefined` if the socket is destroyed (for example, if the client disconnected).
####  `socket.remoteFamily`[#](https://nodejs.org/docs/latest/api/net.html#socketremotefamily)
Added in: v0.11.14
  * Type:


The string representation of the remote IP family. `'IPv4'` or `'IPv6'`. Value may be `undefined` if the socket is destroyed (for example, if the client disconnected).
####  `socket.remotePort`[#](https://nodejs.org/docs/latest/api/net.html#socketremoteport)
Added in: v0.5.10
  * Type:


The numeric representation of the remote port. For example, `80` or `21`. Value may be `undefined` if the socket is destroyed (for example, if the client disconnected).
####  `socket.resetAndDestroy()`[#](https://nodejs.org/docs/latest/api/net.html#socketresetanddestroy)
Added in: v18.3.0, v16.17.0
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)


Close the TCP connection by sending an RST packet and destroy the stream. If this TCP socket is in connecting status, it will send an RST packet and destroy this TCP socket once it is connected. Otherwise, it will call `socket.destroy` with an `ERR_SOCKET_CLOSED` Error. If this is not a TCP socket (for example, a pipe), calling this method will immediately throw an `ERR_INVALID_HANDLE_TYPE` Error.
####  `socket.resume()`[#](https://nodejs.org/docs/latest/api/net.html#socketresume)
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Resumes reading after a call to [`socket.pause()`](https://nodejs.org/docs/latest/api/net.html#socketpause).
####  `socket.setEncoding([encoding])`[#](https://nodejs.org/docs/latest/api/net.html#socketsetencodingencoding)
Added in: v0.1.90
  * `encoding`
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Set the encoding for the socket as a [Readable Stream](https://nodejs.org/docs/latest/api/stream.html#class-streamreadable). See [`readable.setEncoding()`](https://nodejs.org/docs/latest/api/stream.html#readablesetencodingencoding) for more information.
####  `socket.setKeepAlive([enable][, initialDelay])`[#](https://nodejs.org/docs/latest/api/net.html#socketsetkeepaliveenable-initialdelay)
Added in: v0.1.92History Version | Changes
---|---
v13.12.0, v12.17.0 | New defaults for `TCP_KEEPCNT` and `TCP_KEEPINTVL` socket options were added.
  * `enable` **Default:** `false`
  * `initialDelay` **Default:** `0`
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Enable/disable keep-alive functionality, and optionally set the initial delay before the first keepalive probe is sent on an idle socket.
Set `initialDelay` (in milliseconds) to set the delay between the last data packet received and the first keepalive probe. Setting `0` for `initialDelay` will leave the value unchanged from the default (or previous) setting.
Enabling the keep-alive functionality will set the following socket options:
  * `SO_KEEPALIVE=1`
  * `TCP_KEEPIDLE=initialDelay`
  * `TCP_KEEPCNT=10`
  * `TCP_KEEPINTVL=1`


####  `socket.setNoDelay([noDelay])`[#](https://nodejs.org/docs/latest/api/net.html#socketsetnodelaynodelay)
Added in: v0.1.90
  * `noDelay` **Default:** `true`
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Enable/disable the use of Nagle's algorithm.
When a TCP connection is created, it will have Nagle's algorithm enabled.
Nagle's algorithm delays data before it is sent via the network. It attempts to optimize throughput at the expense of latency.
Passing `true` for `noDelay` or not passing an argument will disable Nagle's algorithm for the socket. Passing `false` for `noDelay` will enable Nagle's algorithm.
####  `socket.setTimeout(timeout[, callback])`[#](https://nodejs.org/docs/latest/api/net.html#socketsettimeouttimeout-callback)
Added in: v0.1.90History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `timeout`
  * `callback`
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Sets the socket to timeout after `timeout` milliseconds of inactivity on the socket. By default `net.Socket` do not have a timeout.
When an idle timeout is triggered the socket will receive a [`'timeout'`](https://nodejs.org/docs/latest/api/net.html#event-timeout) event but the connection will not be severed. The user must manually call [`socket.end()`](https://nodejs.org/docs/latest/api/net.html#socketenddata-encoding-callback) or [`socket.destroy()`](https://nodejs.org/docs/latest/api/net.html#socketdestroyerror) to end the connection.
```
socket.setTimeout(3000);
socket.on('timeout', () => {
  console.log('socket timeout');
  socket.end();
});
copy
```

If `timeout` is 0, then the existing idle timeout is disabled.
