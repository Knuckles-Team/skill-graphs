The optional `callback` parameter will be added as a one-time listener for the [`'timeout'`](https://nodejs.org/docs/latest/api/net.html#event-timeout) event.
####  `socket.getTypeOfService()`[#](https://nodejs.org/docs/latest/api/net.html#socketgettypeofservice)
Added in: v25.6.0
  * Returns:


Returns the current Type of Service (TOS) field for IPv4 packets or Traffic Class for IPv6 packets for this socket.
`setTypeOfService()` may be called before the socket is connected; the value will be cached and applied when the socket establishes a connection. `getTypeOfService()` will return the currently set value even before connection.
On some platforms (e.g., Linux), certain TOS/ECN bits may be masked or ignored, and behavior can differ between IPv4 and IPv6 or dual-stack sockets. Callers should verify platform-specific semantics.
####  `socket.setTypeOfService(tos)`[#](https://nodejs.org/docs/latest/api/net.html#socketsettypeofservicetos)
Added in: v25.6.0
  * `tos`
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Sets the Type of Service (TOS) field for IPv4 packets or Traffic Class for IPv6 Packets sent from this socket. This can be used to prioritize network traffic.
`setTypeOfService()` may be called before the socket is connected; the value will be cached and applied when the socket establishes a connection. `getTypeOfService()` will return the currently set value even before connection.
On some platforms (e.g., Linux), certain TOS/ECN bits may be masked or ignored, and behavior can differ between IPv4 and IPv6 or dual-stack sockets. Callers should verify platform-specific semantics.
####  `socket.timeout`[#](https://nodejs.org/docs/latest/api/net.html#sockettimeout)
Added in: v10.7.0
  * Type:


The socket timeout in milliseconds as set by [`socket.setTimeout()`](https://nodejs.org/docs/latest/api/net.html#socketsettimeouttimeout-callback). It is `undefined` if a timeout has not been set.
####  `socket.unref()`[#](https://nodejs.org/docs/latest/api/net.html#socketunref)
Added in: v0.9.1
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The socket itself.


Calling `unref()` on a socket will allow the program to exit if this is the only active socket in the event system. If the socket is already `unref`ed calling `unref()` again will have no effect.
####  `socket.write(data[, encoding][, callback])`[#](https://nodejs.org/docs/latest/api/net.html#socketwritedata-encoding-callback)
Added in: v0.1.90
  * `data` [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) |
  * `encoding` `string`. **Default:** `utf8`.
  * `callback`
  * Returns:


Sends data on the socket. The second parameter specifies the encoding in the case of a string. It defaults to UTF8 encoding.
Returns `true` if the entire data was flushed successfully to the kernel buffer. Returns `false` if all or part of the data was queued in user memory. [`'drain'`](https://nodejs.org/docs/latest/api/net.html#event-drain) will be emitted when the buffer is again free.
The optional `callback` parameter will be executed when the data is finally written out, which may not be immediately.
See `Writable` stream [`write()`](https://nodejs.org/docs/latest/api/stream.html#writablewritechunk-encoding-callback) method for more information.
####  `socket.readyState`[#](https://nodejs.org/docs/latest/api/net.html#socketreadystate)
Added in: v0.5.0
  * Type:


This property represents the state of the connection as a string.
  * If the stream is connecting `socket.readyState` is `opening`.
  * If the stream is readable and writable, it is `open`.
  * If the stream is readable and not writable, it is `readOnly`.
  * If the stream is not readable and writable, it is `writeOnly`.


###  `net.connect()`[#](https://nodejs.org/docs/latest/api/net.html#netconnect)
Aliases to [`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnection).
Possible signatures:
  * [`net.connect(options[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#netconnectoptions-connectlistener)
  * [`net.connect(path[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#netconnectpath-connectlistener) for [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) connections.
  * [`net.connect(port[, host][, connectListener])`](https://nodejs.org/docs/latest/api/net.html#netconnectport-host-connectlistener) for TCP connections.


####  `net.connect(options[, connectListener])`[#](https://nodejs.org/docs/latest/api/net.html#netconnectoptions-connectlistener)
Added in: v0.7.0
  * `options`
  * `connectListener`
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)


Alias to [`net.createConnection(options[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionoptions-connectlistener).
####  `net.connect(path[, connectListener])`[#](https://nodejs.org/docs/latest/api/net.html#netconnectpath-connectlistener)
Added in: v0.1.90
  * `path`
  * `connectListener`
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)


Alias to [`net.createConnection(path[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionpath-connectlistener).
####  `net.connect(port[, host][, connectListener])`[#](https://nodejs.org/docs/latest/api/net.html#netconnectport-host-connectlistener)
Added in: v0.1.90
  * `port`
  * `host`
  * `connectListener`
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)


Alias to [`net.createConnection(port[, host][, connectListener])`](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionport-host-connectlistener).
###  `net.createConnection()`[#](https://nodejs.org/docs/latest/api/net.html#netcreateconnection)
A factory function, which creates a new [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket), immediately initiates connection with [`socket.connect()`](https://nodejs.org/docs/latest/api/net.html#socketconnect), then returns the `net.Socket` that starts the connection.
When the connection is established, a [`'connect'`](https://nodejs.org/docs/latest/api/net.html#event-connect) event will be emitted on the returned socket. The last parameter `connectListener`, if supplied, will be added as a listener for the [`'connect'`](https://nodejs.org/docs/latest/api/net.html#event-connect) event **once**.
Possible signatures:
  * [`net.createConnection(options[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionoptions-connectlistener)
  * [`net.createConnection(path[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionpath-connectlistener) for [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) connections.
  * [`net.createConnection(port[, host][, connectListener])`](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionport-host-connectlistener) for TCP connections.


The [`net.connect()`](https://nodejs.org/docs/latest/api/net.html#netconnect) function is an alias to this function.
####  `net.createConnection(options[, connectListener])`[#](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionoptions-connectlistener)
Added in: v0.1.90
  * `options` [`new net.Socket([options])`](https://nodejs.org/docs/latest/api/net.html#new-netsocketoptions) call and the [`socket.connect(options[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener) method.
  * `connectListener` [`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnection) functions. If supplied, will be added as a listener for the [`'connect'`](https://nodejs.org/docs/latest/api/net.html#event-connect) event on the returned socket once.
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The newly created socket used to start the connection.


For available options, see [`new net.Socket([options])`](https://nodejs.org/docs/latest/api/net.html#new-netsocketoptions) and [`socket.connect(options[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener).
Additional options:
  * `timeout` [`socket.setTimeout(timeout)`](https://nodejs.org/docs/latest/api/net.html#socketsettimeouttimeout-callback) after the socket is created, but before it starts the connection.


Following is an example of a client of the echo server described in the [`net.createServer()`](https://nodejs.org/docs/latest/api/net.html#netcreateserveroptions-connectionlistener) section:
```
import net from 'node:net';
const client = net.createConnection({ port: 8124 }, () => {
  // 'connect' listener.
  console.log('connected to server!');
  client.write('world!\r\n');
});
client.on('data', (data) => {
  console.log(data.toString());
  client.end();
});
client.on('end', () => {
  console.log('disconnected from server');
});
const net = require('node:net');
const client = net.createConnection({ port: 8124 }, () => {
  // 'connect' listener.
  console.log('connected to server!');
  client.write('world!\r\n');
});
client.on('data', (data) => {
  console.log(data.toString());
  client.end();
});
client.on('end', () => {
  console.log('disconnected from server');
});
copy
```

To connect on the socket `/tmp/echo.sock`:
```
const client = net.createConnection({ path: '/tmp/echo.sock' });
copy
```

Following is an example of a client using the `port` and `onread` option. In this case, the `onread` option will be only used to call `new net.Socket([options])` and the `port` option will be used to call `socket.connect(options[, connectListener])`.
```
import net from 'node:net';
import { Buffer } from 'node:buffer';
net.createConnection({
  port: 8124,
  onread: {
    // Reuses a 4KiB Buffer for every read from the socket.
    buffer: Buffer.alloc(4 * 1024),
    callback: function(nread, buf) {
      // Received data is available in `buf` from 0 to `nread`.
      console.log(buf.toString('utf8', 0, nread));
    },
  },
});
const net = require('node:net');
net.createConnection({
  port: 8124,
  onread: {
    // Reuses a 4KiB Buffer for every read from the socket.
    buffer: Buffer.alloc(4 * 1024),
    callback: function(nread, buf) {
      // Received data is available in `buf` from 0 to `nread`.
      console.log(buf.toString('utf8', 0, nread));
    },
  },
});
copy
```

####  `net.createConnection(path[, connectListener])`[#](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionpath-connectlistener)
Added in: v0.1.90
  * `path` [`socket.connect(path[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectpath-connectlistener). See [Identifying paths for IPC connections](https://nodejs.org/docs/latest/api/net.html#identifying-paths-for-ipc-connections).
  * `connectListener` [`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnection) functions, an "once" listener for the `'connect'` event on the initiating socket. Will be passed to [`socket.connect(path[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectpath-connectlistener).
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The newly created socket used to start the connection.


Initiates an [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) connection.
This function creates a new [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) with all options set to default, immediately initiates connection with [`socket.connect(path[, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectpath-connectlistener), then returns the `net.Socket` that starts the connection.
####  `net.createConnection(port[, host][, connectListener])`[#](https://nodejs.org/docs/latest/api/net.html#netcreateconnectionport-host-connectlistener)
Added in: v0.1.90
  * `port` [`socket.connect(port[, host][, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectport-host-connectlistener).
  * `host` [`socket.connect(port[, host][, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectport-host-connectlistener). **Default:** `'localhost'`.
  * `connectListener` [`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnection) functions, an "once" listener for the `'connect'` event on the initiating socket. Will be passed to [`socket.connect(port[, host][, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectport-host-connectlistener).
  * Returns: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The newly created socket used to start the connection.


Initiates a TCP connection.
This function creates a new [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) with all options set to default, immediately initiates connection with [`socket.connect(port[, host][, connectListener])`](https://nodejs.org/docs/latest/api/net.html#socketconnectport-host-connectlistener), then returns the `net.Socket` that starts the connection.
###  `net.createServer([options][, connectionListener])`[#](https://nodejs.org/docs/latest/api/net.html#netcreateserveroptions-connectionlistener)
Added in: v0.5.0History Version | Changes
---|---
v20.1.0, v18.17.0 | The `highWaterMark` option is supported now.
v17.7.0, v16.15.0 | The `noDelay`, `keepAlive`, and `keepAliveInitialDelay` options are supported now.
  * `options`
    * `allowHalfOpen` `false`, then the socket will automatically end the writable side when the readable side ends. **Default:** `false`.
    * `highWaterMark` [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket)s' `readableHighWaterMark` and `writableHighWaterMark`. **Default:** See [`stream.getDefaultHighWaterMark()`](https://nodejs.org/docs/latest/api/stream.html#streamgetdefaulthighwatermarkobjectmode).
    * `keepAlive` `true`, it enables keep-alive functionality on the socket immediately after a new incoming connection is received, similarly on what is done in [`socket.setKeepAlive()`](https://nodejs.org/docs/latest/api/net.html#socketsetkeepaliveenable-initialdelay). **Default:** `false`.
    * `keepAliveInitialDelay` **Default:** `0`.
    * `noDelay` `true`, it disables the use of Nagle's algorithm immediately after a new incoming connection is received. **Default:** `false`.
    * `pauseOnConnect` **Default:** `false`.
    * `blockList` [`<net.BlockList>`](https://nodejs.org/docs/latest/api/net.html#class-netblocklist) `blockList` can be used for disabling inbound access to specific IP addresses, IP ranges, or IP subnets. This does not work if the server is behind a reverse proxy, NAT, etc. because the address checked against the block list is the address of the proxy, or the one specified by the NAT.
  * `connectionListener` [`'connection'`](https://nodejs.org/docs/latest/api/net.html#event-connection) event.
  * Returns: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Creates a new TCP or [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) server.
If `allowHalfOpen` is set to `true`, when the other end of the socket signals the end of transmission, the server will only send back the end of transmission when [`socket.end()`](https://nodejs.org/docs/latest/api/net.html#socketenddata-encoding-callback) is explicitly called. For example, in the context of TCP, when a FIN packed is received, a FIN packed is sent back only when [`socket.end()`](https://nodejs.org/docs/latest/api/net.html#socketenddata-encoding-callback) is explicitly called. Until then the connection is half-closed (non-readable but still writable). See [`'end'`](https://nodejs.org/docs/latest/api/net.html#event-end) event and
If `pauseOnConnect` is set to `true`, then the socket associated with each incoming connection will be paused, and no data will be read from its handle. This allows connections to be passed between processes without any data being read by the original process. To begin reading data from a paused socket, call [`socket.resume()`](https://nodejs.org/docs/latest/api/net.html#socketresume).
The server can be a TCP server or an [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) server, depending on what it [`listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) to.
Here is an example of a TCP echo server which listens for connections on port 8124:
```
import net from 'node:net';
const server = net.createServer((c) => {
  // 'connection' listener.
  console.log('client connected');
  c.on('end', () => {
    console.log('client disconnected');
  });
  c.write('hello\r\n');
  c.pipe(c);
});
server.on('error', (err) => {
  throw err;
});
server.listen(8124, () => {
  console.log('server bound');
});
const net = require('node:net');
const server = net.createServer((c) => {
  // 'connection' listener.
  console.log('client connected');
  c.on('end', () => {
    console.log('client disconnected');
  });
  c.write('hello\r\n');
  c.pipe(c);
});
server.on('error', (err) => {
  throw err;
});
server.listen(8124, () => {
  console.log('server bound');
});
copy
```

Test this by using `telnet`:
```
telnet localhost 8124
copy
```

To listen on the socket `/tmp/echo.sock`:
```
server.listen('/tmp/echo.sock', () => {
  console.log('server bound');
});
copy
```

Use `nc` to connect to a Unix domain socket server:
```
nc -U /tmp/echo.sock
copy
```

###  `net.getDefaultAutoSelectFamily()`[#](https://nodejs.org/docs/latest/api/net.html#netgetdefaultautoselectfamily)
Added in: v19.4.0
Gets the current default value of the `autoSelectFamily` option of [`socket.connect(options)`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener). The initial default value is `true`, unless the command line option `--no-network-family-autoselection` is provided.
  * Returns: `autoSelectFamily` option.


###  `net.setDefaultAutoSelectFamily(value)`[#](https://nodejs.org/docs/latest/api/net.html#netsetdefaultautoselectfamilyvalue)
Added in: v19.4.0
Sets the default value of the `autoSelectFamily` option of [`socket.connect(options)`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener).
  * `value` `true`, unless the command line option `--no-network-family-autoselection` is provided.


###  `net.getDefaultAutoSelectFamilyAttemptTimeout()`[#](https://nodejs.org/docs/latest/api/net.html#netgetdefaultautoselectfamilyattempttimeout)
Added in: v19.8.0, v18.18.0
Gets the current default value of the `autoSelectFamilyAttemptTimeout` option of [`socket.connect(options)`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener). The initial default value is `500` or the value specified via the command line option `--network-family-autoselection-attempt-timeout`.
  * Returns: `autoSelectFamilyAttemptTimeout` option.


###  `net.setDefaultAutoSelectFamilyAttemptTimeout(value)`[#](https://nodejs.org/docs/latest/api/net.html#netsetdefaultautoselectfamilyattempttimeoutvalue)
Added in: v19.8.0, v18.18.0
Sets the default value of the `autoSelectFamilyAttemptTimeout` option of [`socket.connect(options)`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener).
  * `value` `10`, the value `10` is used instead. The initial default value is `250` or the value specified via the command line option `--network-family-autoselection-attempt-timeout`.


###  `net.isIP(input)`[#](https://nodejs.org/docs/latest/api/net.html#netisipinput)
Added in: v0.3.0
  * `input`
  * Returns:


Returns `6` if `input` is an IPv6 address. Returns `4` if `input` is an IPv4 address in `0`.
```
net.isIP('::1'); // returns 6
net.isIP('127.0.0.1'); // returns 4
net.isIP('127.000.000.001'); // returns 0
net.isIP('127.0.0.1/24'); // returns 0
net.isIP('fhqwhgads'); // returns 0
copy
```

###  `net.isIPv4(input)`[#](https://nodejs.org/docs/latest/api/net.html#netisipv4input)
Added in: v0.3.0
  * `input`
  * Returns:


Returns `true` if `input` is an IPv4 address in `false`.
```
net.isIPv4('127.0.0.1'); // returns true
net.isIPv4('127.000.000.001'); // returns false
net.isIPv4('127.0.0.1/24'); // returns false
net.isIPv4('fhqwhgads'); // returns false
copy
```

###  `net.isIPv6(input)`[#](https://nodejs.org/docs/latest/api/net.html#netisipv6input)
Added in: v0.3.0
  * `input`
  * Returns:


Returns `true` if `input` is an IPv6 address. Otherwise, returns `false`.
```
net.isIPv6('::1'); // returns true
net.isIPv6('fhqwhgads'); // returns false
copy
```
