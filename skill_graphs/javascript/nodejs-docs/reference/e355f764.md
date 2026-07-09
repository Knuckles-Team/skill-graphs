## Net[#](https://nodejs.org/docs/latest/api/net.html#net)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:net` module provides an asynchronous network API for creating stream-based TCP or [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) servers ([`net.createServer()`](https://nodejs.org/docs/latest/api/net.html#netcreateserveroptions-connectionlistener)) and clients ([`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnection)).
It can be accessed using:
```
import net from 'node:net';
const net = require('node:net');
copy
```

### IPC support[#](https://nodejs.org/docs/latest/api/net.html#ipc-support)
History Version | Changes
---|---
v20.8.0 | Support binding to abstract Unix domain socket path like `\0abstract`. We can bind '\0' for Node.js `< v20.4.0`.
The `node:net` module supports IPC with named pipes on Windows, and Unix domain sockets on other operating systems.
#### Identifying paths for IPC connections[#](https://nodejs.org/docs/latest/api/net.html#identifying-paths-for-ipc-connections)
[`net.connect()`](https://nodejs.org/docs/latest/api/net.html#netconnect), [`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnection), [`server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten), and [`socket.connect()`](https://nodejs.org/docs/latest/api/net.html#socketconnect) take a `path` parameter to identify IPC endpoints.
On Unix, the local domain is also known as the Unix domain. The path is a file system pathname. It will throw an error when the length of pathname is greater than the length of `sizeof(sockaddr_un.sun_path)`. Typical values are 107 bytes on Linux and 103 bytes on macOS. If a Node.js API abstraction creates the Unix domain socket, it will unlink the Unix domain socket as well. For example, [`net.createServer()`](https://nodejs.org/docs/latest/api/net.html#netcreateserveroptions-connectionlistener) may create a Unix domain socket and [`server.close()`](https://nodejs.org/docs/latest/api/net.html#serverclosecallback) will unlink it. But if a user creates the Unix domain socket outside of these abstractions, the user will need to remove it. The same applies when a Node.js API creates a Unix domain socket but the program then crashes. In short, a Unix domain socket will be visible in the file system and will persist until unlinked. On Linux, You can use Unix abstract socket by adding `\0` to the beginning of the path, such as `\0abstract`. The path to the Unix abstract socket is not visible in the file system and it will disappear automatically when all open references to the socket are closed.
On Windows, the local domain is implemented using a named pipe. The path _must_ refer to an entry in `\\?\pipe\` or `\\.\pipe\`. Any characters are permitted, but the latter may do some processing of pipe names, such as resolving `..` sequences. Despite how it might look, the pipe namespace is flat. Pipes will _not persist_. They are removed when the last reference to them is closed. Unlike Unix domain sockets, Windows will close and remove the pipe when the owning process exits.
JavaScript string escaping requires paths to be specified with extra backslash escaping such as:
```
net.createServer().listen(
  path.join('\\\\?\\pipe', process.cwd(), 'myctl'));
copy
```

### Class: `net.BlockList`[#](https://nodejs.org/docs/latest/api/net.html#class-netblocklist)
Added in: v15.0.0, v14.18.0
The `BlockList` object can be used with some network APIs to specify rules for disabling inbound or outbound access to specific IP addresses, IP ranges, or IP subnets.
####  `blockList.addAddress(address[, type])`[#](https://nodejs.org/docs/latest/api/net.html#blocklistaddaddressaddress-type)
Added in: v15.0.0, v14.18.0
  * `address` [`<net.SocketAddress>`](https://nodejs.org/docs/latest/api/net.html#class-netsocketaddress) An IPv4 or IPv6 address.
  * `type` `'ipv4'` or `'ipv6'`. **Default:** `'ipv4'`.


Adds a rule to block the given IP address.
####  `blockList.addRange(start, end[, type])`[#](https://nodejs.org/docs/latest/api/net.html#blocklistaddrangestart-end-type)
Added in: v15.0.0, v14.18.0
  * `start` [`<net.SocketAddress>`](https://nodejs.org/docs/latest/api/net.html#class-netsocketaddress) The starting IPv4 or IPv6 address in the range.
  * `end` [`<net.SocketAddress>`](https://nodejs.org/docs/latest/api/net.html#class-netsocketaddress) The ending IPv4 or IPv6 address in the range.
  * `type` `'ipv4'` or `'ipv6'`. **Default:** `'ipv4'`.


Adds a rule to block a range of IP addresses from `start` (inclusive) to `end` (inclusive).
####  `blockList.addSubnet(net, prefix[, type])`[#](https://nodejs.org/docs/latest/api/net.html#blocklistaddsubnetnet-prefix-type)
Added in: v15.0.0, v14.18.0
  * `net` [`<net.SocketAddress>`](https://nodejs.org/docs/latest/api/net.html#class-netsocketaddress) The network IPv4 or IPv6 address.
  * `prefix` `0` and `32`. For IPv6, this must be between `0` and `128`.
  * `type` `'ipv4'` or `'ipv6'`. **Default:** `'ipv4'`.


Adds a rule to block a range of IP addresses specified as a subnet mask.
####  `blockList.check(address[, type])`[#](https://nodejs.org/docs/latest/api/net.html#blocklistcheckaddress-type)
Added in: v15.0.0, v14.18.0
  * `address` [`<net.SocketAddress>`](https://nodejs.org/docs/latest/api/net.html#class-netsocketaddress) The IP address to check
  * `type` `'ipv4'` or `'ipv6'`. **Default:** `'ipv4'`.
  * Returns:


Returns `true` if the given IP address matches any of the rules added to the `BlockList`.
```
const blockList = new net.BlockList();
blockList.addAddress('123.123.123.123');
blockList.addRange('10.0.0.1', '10.0.0.10');
blockList.addSubnet('8592:757c:efae:4e45::', 64, 'ipv6');

console.log(blockList.check('123.123.123.123'));  // Prints: true
console.log(blockList.check('10.0.0.3'));  // Prints: true
console.log(blockList.check('222.111.111.222'));  // Prints: false

// IPv6 notation for IPv4 addresses works:
console.log(blockList.check('::ffff:7b7b:7b7b', 'ipv6')); // Prints: true
console.log(blockList.check('::ffff:123.123.123.123', 'ipv6')); // Prints: true
copy
```

####  `blockList.rules`[#](https://nodejs.org/docs/latest/api/net.html#blocklistrules)
Added in: v15.0.0, v14.18.0
  * Type:


The list of rules added to the blocklist.
####  `BlockList.isBlockList(value)`[#](https://nodejs.org/docs/latest/api/net.html#blocklistisblocklistvalue)
Added in: v23.4.0, v22.13.0
  * `value`
  * Returns `true` if the `value` is a `net.BlockList`.


####  `blockList.fromJSON(value)`[#](https://nodejs.org/docs/latest/api/net.html#blocklistfromjsonvalue)
Stability: 1 - Experimental
```
const blockList = new net.BlockList();
const data = [
  'Subnet: IPv4 192.168.1.0/24',
  'Address: IPv4 10.0.0.5',
  'Range: IPv4 192.168.2.1-192.168.2.10',
  'Range: IPv4 10.0.0.1-10.0.0.10',
];
blockList.fromJSON(data);
blockList.fromJSON(JSON.stringify(data));
copy
```

  * `value` Blocklist.rules


####  `blockList.toJSON()`[#](https://nodejs.org/docs/latest/api/net.html#blocklisttojson)
Stability: 1 - Experimental
  * Returns Blocklist.rules


### Class: `net.SocketAddress`[#](https://nodejs.org/docs/latest/api/net.html#class-netsocketaddress)
Added in: v15.14.0, v14.18.0
####  `new net.SocketAddress([options])`[#](https://nodejs.org/docs/latest/api/net.html#new-netsocketaddressoptions)
Added in: v15.14.0, v14.18.0
  * `options`
    * `address` **Default** : `'127.0.0.1'` if `family` is `'ipv4'`; `'::'` if `family` is `'ipv6'`.
    * `family` `'ipv4'` or `'ipv6'`. **Default** : `'ipv4'`.
    * `flowlabel` `family` is `'ipv6'`.
    * `port`


####  `socketaddress.address`[#](https://nodejs.org/docs/latest/api/net.html#socketaddressaddress)
Added in: v15.14.0, v14.18.0
  * Type:


####  `socketaddress.family`[#](https://nodejs.org/docs/latest/api/net.html#socketaddressfamily)
Added in: v15.14.0, v14.18.0
  * Type: `'ipv4'` or `'ipv6'`.


####  `socketaddress.flowlabel`[#](https://nodejs.org/docs/latest/api/net.html#socketaddressflowlabel)
Added in: v15.14.0, v14.18.0
  * Type:


####  `socketaddress.port`[#](https://nodejs.org/docs/latest/api/net.html#socketaddressport)
Added in: v15.14.0, v14.18.0
  * Type:


####  `SocketAddress.parse(input)`[#](https://nodejs.org/docs/latest/api/net.html#socketaddressparseinput)
Added in: v23.4.0, v22.13.0
  * `input` `123.1.2.3:1234` or `[1::1]:1234`.
  * Returns: [`<net.SocketAddress>`](https://nodejs.org/docs/latest/api/net.html#class-netsocketaddress) Returns a `SocketAddress` if parsing was successful. Otherwise returns `undefined`.


### Class: `net.Server`[#](https://nodejs.org/docs/latest/api/net.html#class-netserver)
Added in: v0.1.90
  * Extends: [`<EventEmitter>`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter)


This class is used to create a TCP or [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) server.
####  `new net.Server([options][, connectionListener])`[#](https://nodejs.org/docs/latest/api/net.html#new-netserveroptions-connectionlistener)
  * `options` [`net.createServer([options][, connectionListener])`](https://nodejs.org/docs/latest/api/net.html#netcreateserveroptions-connectionlistener).
  * `connectionListener` [`'connection'`](https://nodejs.org/docs/latest/api/net.html#event-connection) event.
  * Returns: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


`net.Server` is an [`EventEmitter`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter) with the following events:
#### Event: `'close'`[#](https://nodejs.org/docs/latest/api/net.html#event-close)
Added in: v0.5.0
Emitted when the server closes. If connections exist, this event is not emitted until all connections are ended.
#### Event: `'connection'`[#](https://nodejs.org/docs/latest/api/net.html#event-connection)
Added in: v0.1.90
  * Type: [`<net.Socket>`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) The connection object


Emitted when a new connection is made. `socket` is an instance of `net.Socket`.
#### Event: `'error'`[#](https://nodejs.org/docs/latest/api/net.html#event-error)
Added in: v0.1.90
  * Type:


Emitted when an error occurs. Unlike [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket), the [`'close'`](https://nodejs.org/docs/latest/api/net.html#event-close) event will **not** be emitted directly following this event unless [`server.close()`](https://nodejs.org/docs/latest/api/net.html#serverclosecallback) is manually called. See the example in discussion of [`server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten).
#### Event: `'listening'`[#](https://nodejs.org/docs/latest/api/net.html#event-listening)
Added in: v0.1.90
Emitted when the server has been bound after calling [`server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten).
#### Event: `'drop'`[#](https://nodejs.org/docs/latest/api/net.html#event-drop)
Added in: v18.6.0, v16.17.0
When the number of connections reaches the threshold of `server.maxConnections`, the server will drop new connections and emit `'drop'` event instead. If it is a TCP server, the argument is as follows, otherwise the argument is `undefined`.
  * `data`
    * `localAddress`
    * `localPort`
    * `localFamily`
    * `remoteAddress`
    * `remotePort`
    * `remoteFamily` `'IPv4'` or `'IPv6'`.


####  `server.address()`[#](https://nodejs.org/docs/latest/api/net.html#serveraddress)
Added in: v0.1.90History Version | Changes
---|---
v18.4.0 | The `family` property now returns a string instead of a number.
v18.0.0 | The `family` property now returns a number instead of a string.
  * Returns:


Returns the bound `address`, the address `family` name, and `port` of the server as reported by the operating system if listening on an IP socket (useful to find which port was assigned when getting an OS-assigned address): `{ port: 12346, family: 'IPv4', address: '127.0.0.1' }`.
For a server listening on a pipe or Unix domain socket, the name is returned as a string.
```
const server = net.createServer((socket) => {
  socket.end('goodbye\n');
}).on('error', (err) => {
  // Handle errors here.
  throw err;
});

// Grab an arbitrary unused port.
server.listen(() => {
  console.log('opened server on', server.address());
});
copy
```

`server.address()` returns `null` before the `'listening'` event has been emitted or after calling `server.close()`.
####  `server.close([callback])`[#](https://nodejs.org/docs/latest/api/net.html#serverclosecallback)
Added in: v0.1.90
  * `callback`
  * Returns: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Stops the server from accepting new connections and keeps existing connections. This function is asynchronous, the server is finally closed when all connections are ended and the server emits a [`'close'`](https://nodejs.org/docs/latest/api/net.html#event-close) event. The optional `callback` will be called once the `'close'` event occurs. Unlike that event, it will be called with an `Error` as its only argument if the server was not open when it was closed.
####  `server[Symbol.asyncDispose]()`[#](https://nodejs.org/docs/latest/api/net.html#serversymbolasyncdispose)
Added in: v20.5.0, v18.18.0History Version | Changes
---|---
v24.2.0 | No longer experimental.
Calls [`server.close()`](https://nodejs.org/docs/latest/api/net.html#serverclosecallback) and returns a promise that fulfills when the server has closed.
####  `server.getConnections(callback)`[#](https://nodejs.org/docs/latest/api/net.html#servergetconnectionscallback)
Added in: v0.9.7
  * `callback`
  * Returns: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Asynchronously get the number of concurrent connections on the server. Works when sockets were sent to forks.
Callback should take two arguments `err` and `count`.
####  `server.listen()`[#](https://nodejs.org/docs/latest/api/net.html#serverlisten)
Start a server listening for connections. A `net.Server` can be a TCP or an [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) server depending on what it listens to.
Possible signatures:
  * [`server.listen(handle[, backlog][, callback])`](https://nodejs.org/docs/latest/api/net.html#serverlistenhandle-backlog-callback)
  * [`server.listen(options[, callback])`](https://nodejs.org/docs/latest/api/net.html#serverlistenoptions-callback)
  * [`server.listen(path[, backlog][, callback])`](https://nodejs.org/docs/latest/api/net.html#serverlistenpath-backlog-callback) for [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) servers
  * [`server.listen([port[, host[, backlog]]][, callback])`](https://nodejs.org/docs/latest/api/net.html#serverlistenport-host-backlog-callback) for TCP servers


This function is asynchronous. When the server starts listening, the [`'listening'`](https://nodejs.org/docs/latest/api/net.html#event-listening) event will be emitted. The last parameter `callback` will be added as a listener for the [`'listening'`](https://nodejs.org/docs/latest/api/net.html#event-listening) event.
All `listen()` methods can take a `backlog` parameter to specify the maximum length of the queue of pending connections. The actual length will be determined by the OS through sysctl settings such as `tcp_max_syn_backlog` and `somaxconn` on Linux. The default value of this parameter is 511 (not 512).
All [`net.Socket`](https://nodejs.org/docs/latest/api/net.html#class-netsocket) are set to `SO_REUSEADDR` (see
The `server.listen()` method can be called again if and only if there was an error during the first `server.listen()` call or `server.close()` has been called. Otherwise, an `ERR_SERVER_ALREADY_LISTEN` error will be thrown.
One of the most common errors raised when listening is `EADDRINUSE`. This happens when another server is already listening on the requested `port`/`path`/`handle`. One way to handle this would be to retry after a certain amount of time:
```
server.on('error', (e) => {
  if (e.code === 'EADDRINUSE') {
    console.error('Address in use, retrying...');
    setTimeout(() => {
      server.close();
      server.listen(PORT, HOST);
    }, 1000);
  }
});
copy
```

#####  `server.listen(handle[, backlog][, callback])`[#](https://nodejs.org/docs/latest/api/net.html#serverlistenhandle-backlog-callback)
Added in: v0.5.10
  * `handle`
  * `backlog` [`server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) functions
  * `callback`
  * Returns: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Start a server listening for connections on a given `handle` that has already been bound to a port, a Unix domain socket, or a Windows named pipe.
The `handle` object can be either a server, a socket (anything with an underlying `_handle` member), or an object with an `fd` member that is a valid file descriptor.
Listening on a file descriptor is not supported on Windows.
#####  `server.listen(options[, callback])`[#](https://nodejs.org/docs/latest/api/net.html#serverlistenoptions-callback)
Added in: v0.11.14History Version | Changes
---|---
v23.1.0, v22.12.0 | The `reusePort` option is supported.
v15.6.0 | AbortSignal support was added.
v11.4.0 | The `ipv6Only` option is supported.
  * `options`
    * `backlog` [`server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) functions.
    * `exclusive` **Default:** `false`
    * `host`
    * `ipv6Only` `ipv6Only` to `true` will disable dual-stack support, i.e., binding to host `::` won't make `0.0.0.0` be bound. **Default:** `false`.
    * `reusePort` `reusePort` to `true` allows multiple sockets on the same host to bind to the same port. Incoming connections are distributed by the operating system to listening sockets. This option is available only on some platforms, such as Linux 3.9+, DragonFlyBSD 3.6+, FreeBSD 12.0+, Solaris 11.4, and AIX 7.2.5+. On unsupported platforms, this option raises an error. **Default:** `false`.
    * `path` `port` is specified. See [Identifying paths for IPC connections](https://nodejs.org/docs/latest/api/net.html#identifying-paths-for-ipc-connections).
    * `port`
    * `readableAll` **Default:** `false`.
    * `signal` [`<AbortSignal>`](https://nodejs.org/docs/latest/api/globals.html#class-abortsignal) An AbortSignal that may be used to close a listening server.
    * `writableAll` **Default:** `false`.
  * `callback`
  * Returns: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


If `port` is specified, it behaves the same as [`server.listen([port[, host[, backlog]]][, callback])`](https://nodejs.org/docs/latest/api/net.html#serverlistenport-host-backlog-callback). Otherwise, if `path` is specified, it behaves the same as [`server.listen(path[, backlog][, callback])`](https://nodejs.org/docs/latest/api/net.html#serverlistenpath-backlog-callback). If none of them is specified, an error will be thrown.
If `exclusive` is `false` (default), then cluster workers will use the same underlying handle, allowing connection handling duties to be shared. When `exclusive` is `true`, the handle is not shared, and attempted port sharing results in an error. An example which listens on an exclusive port is shown below.
```
server.listen({
  host: 'localhost',
  port: 80,
  exclusive: true,
});
copy
```

When `exclusive` is `true` and the underlying handle is shared, it is possible that several workers query a handle with different backlogs. In this case, the first `backlog` passed to the master process will be used.
Starting an IPC server as root may cause the server path to be inaccessible for unprivileged users. Using `readableAll` and `writableAll` will make the server accessible for all users.
If the `signal` option is enabled, calling `.abort()` on the corresponding `AbortController` is similar to calling `.close()` on the server:
```
const controller = new AbortController();
server.listen({
  host: 'localhost',
  port: 80,
  signal: controller.signal,
});
// Later, when you want to close the server.
controller.abort();
copy
```

#####  `server.listen(path[, backlog][, callback])`[#](https://nodejs.org/docs/latest/api/net.html#serverlistenpath-backlog-callback)
Added in: v0.1.90
  * `path` [Identifying paths for IPC connections](https://nodejs.org/docs/latest/api/net.html#identifying-paths-for-ipc-connections).
  * `backlog` [`server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) functions.
  * `callback`
  * Returns: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Start an [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) server listening for connections on the given `path`.
#####  `server.listen([port[, host[, backlog]]][, callback])`[#](https://nodejs.org/docs/latest/api/net.html#serverlistenport-host-backlog-callback)
Added in: v0.1.90
  * `port`
  * `host`
  * `backlog` [`server.listen()`](https://nodejs.org/docs/latest/api/net.html#serverlisten) functions.
  * `callback`
  * Returns: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Start a TCP server listening for connections on the given `port` and `host`.
If `port` is omitted or is 0, the operating system will assign an arbitrary unused port, which can be retrieved by using `server.address().port` after the [`'listening'`](https://nodejs.org/docs/latest/api/net.html#event-listening) event has been emitted.
If `host` is omitted, the server will accept connections on the `::`) when IPv6 is available, or the `0.0.0.0`) otherwise.
In most operating systems, listening to the `::`) may cause the `net.Server` to also listen on the `0.0.0.0`).
####  `server.listening`[#](https://nodejs.org/docs/latest/api/net.html#serverlistening)
Added in: v5.7.0
  * Type:


####  `server.maxConnections`[#](https://nodejs.org/docs/latest/api/net.html#servermaxconnections)
Added in: v0.2.0History Version | Changes
---|---
v21.0.0 | Setting `maxConnections` to `0` drops all the incoming connections. Previously, it was interpreted as `Infinity`.
  * Type:


When the number of connections reaches the `server.maxConnections` threshold:
  1. If the process is not running in cluster mode, Node.js will close the connection.
  2. If the process is running in cluster mode, Node.js will, by default, route the connection to another worker process. To close the connection instead, set [`server.dropMaxConnection`](https://nodejs.org/docs/latest/api/net.html#serverdropmaxconnection) to `true`.


It is not recommended to use this option once a socket has been sent to a child with [`child_process.fork()`](https://nodejs.org/docs/latest/api/child_process.html#child_processforkmodulepath-args-options).
####  `server.dropMaxConnection`[#](https://nodejs.org/docs/latest/api/net.html#serverdropmaxconnection)
Added in: v23.1.0, v22.12.0
  * Type:


Set this property to `true` to begin closing connections once the number of connections reaches the [`server.maxConnections`](https://nodejs.org/docs/latest/api/net.html#servermaxconnections) threshold. This setting is only effective in cluster mode.
####  `server.ref()`[#](https://nodejs.org/docs/latest/api/net.html#serverref)
Added in: v0.9.1
  * Returns: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Opposite of `unref()`, calling `ref()` on a previously `unref`ed server will _not_ let the program exit if it's the only server left (the default behavior). If the server is `ref`ed calling `ref()` again will have no effect.
####  `server.unref()`[#](https://nodejs.org/docs/latest/api/net.html#serverunref)
Added in: v0.9.1
  * Returns: [`<net.Server>`](https://nodejs.org/docs/latest/api/net.html#class-netserver)


Calling `unref()` on a server will allow the program to exit if this is the only active server in the event system. If the server is already `unref`ed calling `unref()` again will have no effect.
### Class: `net.Socket`[#](https://nodejs.org/docs/latest/api/net.html#class-netsocket)
Added in: v0.3.4
  * Extends: [`<stream.Duplex>`](https://nodejs.org/docs/latest/api/stream.html#class-streamduplex)


This class is an abstraction of a TCP socket or a streaming [IPC](https://nodejs.org/docs/latest/api/net.html#ipc-support) endpoint (uses named pipes on Windows, and Unix domain sockets otherwise). It is also an [`EventEmitter`](https://nodejs.org/docs/latest/api/events.html#class-eventemitter).
A `net.Socket` can be created by the user and used directly to interact with a server. For example, it is returned by [`net.createConnection()`](https://nodejs.org/docs/latest/api/net.html#netcreateconnection), so the user can use it to talk to the server.
It can also be created by Node.js and passed to the user when a connection is received. For example, it is passed to the listeners of a [`'connection'`](https://nodejs.org/docs/latest/api/net.html#event-connection) event emitted on a [`net.Server`](https://nodejs.org/docs/latest/api/net.html#class-netserver), so the user can use it to interact with the client.
####  `new net.Socket([options])`[#](https://nodejs.org/docs/latest/api/net.html#new-netsocketoptions)
Added in: v0.3.4History Version | Changes
---|---
v25.6.0 | Added `typeOfService` option.
v15.14.0 | AbortSignal support was added.
v12.10.0 | Added `onread` option.
  * `options`
    * `allowHalfOpen` `false`, then the socket will automatically end the writable side when the readable side ends. See [`net.createServer()`](https://nodejs.org/docs/latest/api/net.html#netcreateserveroptions-connectionlistener) and the [`'end'`](https://nodejs.org/docs/latest/api/net.html#event-end) event for details. **Default:** `false`.
