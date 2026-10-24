
socket.htons(_x_)[¶](https://docs.python.org/3/library/socket.html#socket.htons "Link to this definition")

Convert 16-bit positive integers from host to network byte order. On machines where the host byte order is the same as network byte order, this is a no-op; otherwise, it performs a 2-byte swap operation.
Changed in version 3.10: Raises [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") if _x_ does not fit in a 16-bit unsigned integer.

socket.inet_aton(_ip_string_)[¶](https://docs.python.org/3/library/socket.html#socket.inet_aton "Link to this definition")

Convert an IPv4 address from dotted-quad string format (for example, ‘123.45.67.89’) to 32-bit packed binary format, as a bytes object four characters in length. This is useful when conversing with a program that uses the standard C library and needs objects of type `in_addr`, which is the C type for the 32-bit packed binary this function returns.
`inet_aton()` also accepts strings with less than three dots; see the Unix manual page
If the IPv4 address string passed to this function is invalid, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") will be raised. Note that exactly what is valid depends on the underlying C implementation of `inet_aton()`.
`inet_aton()` does not support IPv6, and [`inet_pton()`](https://docs.python.org/3/library/socket.html#socket.inet_pton "socket.inet_pton") should be used instead for IPv4/v6 dual stack support.

socket.inet_ntoa(_packed_ip_)[¶](https://docs.python.org/3/library/socket.html#socket.inet_ntoa "Link to this definition")

Convert a 32-bit packed IPv4 address (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) four bytes in length) to its standard dotted-quad string representation (for example, ‘123.45.67.89’). This is useful when conversing with a program that uses the standard C library and needs objects of type `in_addr`, which is the C type for the 32-bit packed binary data this function takes as an argument.
If the byte sequence passed to this function is not exactly 4 bytes in length, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") will be raised. `inet_ntoa()` does not support IPv6, and [`inet_ntop()`](https://docs.python.org/3/library/socket.html#socket.inet_ntop "socket.inet_ntop") should be used instead for IPv4/v6 dual stack support.
Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) is now accepted.

socket.inet_pton(_address_family_ , _ip_string_)[¶](https://docs.python.org/3/library/socket.html#socket.inet_pton "Link to this definition")

Convert an IP address from its family-specific string format to a packed, binary format. `inet_pton()` is useful when a library or network protocol calls for an object of type `in_addr` (similar to [`inet_aton()`](https://docs.python.org/3/library/socket.html#socket.inet_aton "socket.inet_aton")) or `in6_addr`.
Supported values for _address_family_ are currently [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET") and [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6"). If the IP address string _ip_string_ is invalid, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") will be raised. Note that exactly what is valid depends on both the value of _address_family_ and the underlying implementation of `inet_pton()`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Changed in version 3.4: Windows support added

socket.inet_ntop(_address_family_ , _packed_ip_)[¶](https://docs.python.org/3/library/socket.html#socket.inet_ntop "Link to this definition")

Convert a packed IP address (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) of some number of bytes) to its standard, family-specific string representation (for example, `'7.10.0.5'` or `'5aef:2b::8'`). `inet_ntop()` is useful when a library or network protocol returns an object of type `in_addr` (similar to [`inet_ntoa()`](https://docs.python.org/3/library/socket.html#socket.inet_ntoa "socket.inet_ntoa")) or `in6_addr`.
Supported values for _address_family_ are currently [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET") and [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6"). If the bytes object _packed_ip_ is not the correct length for the specified address family, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised. [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised for errors from the call to `inet_ntop()`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.
Changed in version 3.4: Windows support added
Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) is now accepted.

socket.CMSG_LEN(_length_)[¶](https://docs.python.org/3/library/socket.html#socket.CMSG_LEN "Link to this definition")

Return the total length, without trailing padding, of an ancillary data item with associated data of the given _length_. This value can often be used as the buffer size for [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg") to receive a single item of ancillary data, but [`CMSG_SPACE()`](https://docs.python.org/3/library/socket.html#socket.CMSG_SPACE "socket.CMSG_SPACE") and thus include space for padding, even when the item will be the last in the buffer. Raises [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") if _length_ is outside the permissible range of values.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Most Unix platforms.
Added in version 3.3.

socket.CMSG_SPACE(_length_)[¶](https://docs.python.org/3/library/socket.html#socket.CMSG_SPACE "Link to this definition")

Return the buffer size needed for [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg") to receive an ancillary data item with associated data of the given _length_ , along with any trailing padding. The buffer space needed to receive multiple items is the sum of the `CMSG_SPACE()` values for their associated data lengths. Raises [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") if _length_ is outside the permissible range of values.
Note that some systems might support ancillary data without providing this function. Also note that setting the buffer size using the results of this function may not precisely limit the amount of ancillary data that can be received, since additional data may be able to fit into the padding area.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
most Unix platforms.
Added in version 3.3.

socket.getdefaulttimeout()[¶](https://docs.python.org/3/library/socket.html#socket.getdefaulttimeout "Link to this definition")

Return the default timeout in seconds (float) for new socket objects. A value of `None` indicates that new socket objects have no timeout. When the socket module is first imported, the default is `None`.

socket.setdefaulttimeout(_timeout_)[¶](https://docs.python.org/3/library/socket.html#socket.setdefaulttimeout "Link to this definition")

Set the default timeout in seconds (float) for new socket objects. When the socket module is first imported, the default is `None`. See [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout") for possible values and their respective meanings.

socket.sethostname(_name_)[¶](https://docs.python.org/3/library/socket.html#socket.sethostname "Link to this definition")

Set the machine’s hostname to _name_. This will raise an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if you don’t have enough rights.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.sethostname` with argument `name`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not Android.
Added in version 3.3.

socket.if_nameindex()[¶](https://docs.python.org/3/library/socket.html#socket.if_nameindex "Link to this definition")

Return a list of network interface information (index int, name string) tuples. [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if the system call fails.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI.
Added in version 3.3.
Changed in version 3.8: Windows support was added.
Note
On Windows network interfaces have different names in different contexts (all names are examples):
  * UUID: `{FB605B73-AAC2-49A6-9A2F-25416AEA0573}`
  * name: `ethernet_32770`
  * friendly name: `vEthernet (nat)`
  * description: `Hyper-V Virtual Ethernet Adapter`


This function returns names of the second form from the list, `ethernet_32770` in this example case.

socket.if_nametoindex(_if_name_)[¶](https://docs.python.org/3/library/socket.html#socket.if_nametoindex "Link to this definition")

Return a network interface index number corresponding to an interface name. [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if no interface with the given name exists.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI.
Added in version 3.3.
Changed in version 3.8: Windows support was added.
See also
“Interface name” is a name as documented in [`if_nameindex()`](https://docs.python.org/3/library/socket.html#socket.if_nameindex "socket.if_nameindex").

socket.if_indextoname(_if_index_)[¶](https://docs.python.org/3/library/socket.html#socket.if_indextoname "Link to this definition")

Return a network interface name corresponding to an interface index number. [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if no interface with the given index exists.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows, not WASI.
Added in version 3.3.
Changed in version 3.8: Windows support was added.
See also
“Interface name” is a name as documented in [`if_nameindex()`](https://docs.python.org/3/library/socket.html#socket.if_nameindex "socket.if_nameindex").

socket.send_fds(_sock_ , _buffers_ , _fds_[, _flags_[, _address_]])[¶](https://docs.python.org/3/library/socket.html#socket.send_fds "Link to this definition")

Send the list of file descriptors _fds_ over an [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX") socket _sock_. The _fds_ parameter is a sequence of file descriptors. Consult [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg") for the documentation of these parameters.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Unix platforms supporting [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg") and `SCM_RIGHTS` mechanism.
Added in version 3.9.

socket.recv_fds(_sock_ , _bufsize_ , _maxfds_[, _flags_])[¶](https://docs.python.org/3/library/socket.html#socket.recv_fds "Link to this definition")

Receive up to _maxfds_ file descriptors from an [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX") socket _sock_. Return `(msg, list(fds), flags, addr)`. Consult [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg") for the documentation of these parameters.
[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Unix platforms supporting [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg") and `SCM_RIGHTS` mechanism.
Added in version 3.9.
Note
Any truncated integers at the end of the list of file descriptors.
## Socket Objects[¶](https://docs.python.org/3/library/socket.html#socket-objects "Link to this heading")
Socket objects have the following methods. Except for [`makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile"), these correspond to Unix system calls applicable to sockets.
Changed in version 3.2: Support for the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol was added. Exiting the context manager is equivalent to calling [`close()`](https://docs.python.org/3/library/socket.html#socket.close "socket.close").

socket.accept()[¶](https://docs.python.org/3/library/socket.html#socket.socket.accept "Link to this definition")

Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair `(conn, address)` where _conn_ is a _new_ socket object usable to send and receive data on the connection, and _address_ is the address bound to the socket on the other end of the connection.
The newly created socket is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
Changed in version 3.4: The socket is now non-inheritable.
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

socket.bind(_address_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.bind "Link to this definition")

Bind the socket to _address_. The socket must not already be bound. (The format of _address_ depends on the address family — see above.)
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.bind` with arguments `self`, `address`.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.close()[¶](https://docs.python.org/3/library/socket.html#socket.socket.close "Link to this definition")

Mark the socket closed. The underlying system resource (e.g. a file descriptor) is also closed when all file objects from [`makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile") are closed. Once that happens, all future operations on the socket object will fail. The remote end will receive no more data (after queued data is flushed).
Sockets are automatically closed when they are garbage-collected, but it is recommended to `close()` them explicitly, or to use a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement around them.
Changed in version 3.6: [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is now raised if an error occurs when the underlying `close()` call is made.
Note
`close()` releases the resource associated with a connection but does not necessarily close the connection immediately. If you want to close the connection in a timely fashion, call [`shutdown()`](https://docs.python.org/3/library/socket.html#socket.socket.shutdown "socket.socket.shutdown") before `close()`.

socket.connect(_address_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.connect "Link to this definition")

Connect to a remote socket at _address_. (The format of _address_ depends on the address family — see above.)
If the connection is interrupted by a signal, the method waits until the connection completes, or raises a [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError") on timeout, if the signal handler doesn’t raise an exception and the socket is blocking or has a timeout. For non-blocking sockets, the method raises an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception if the connection is interrupted by a signal (or the exception raised by the signal handler).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.connect` with arguments `self`, `address`.
Changed in version 3.5: The method now waits until the connection completes instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception if the connection is interrupted by a signal, the signal handler doesn’t raise an exception and the socket is blocking or has a timeout (see the [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.connect_ex(_address_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.connect_ex "Link to this definition")

Like `connect(address)`, but return an error indicator instead of raising an exception for errors returned by the C-level `connect()` call (other problems, such as “host not found,” can still raise exceptions). The error indicator is `0` if the operation succeeded, otherwise the value of the `errno` variable. This is useful to support, for example, asynchronous connects.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.connect` with arguments `self`, `address`.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.detach()[¶](https://docs.python.org/3/library/socket.html#socket.socket.detach "Link to this definition")

Put the socket object into closed state without actually closing the underlying file descriptor. The file descriptor is returned, and can be reused for other purposes.
Added in version 3.2.

socket.dup()[¶](https://docs.python.org/3/library/socket.html#socket.socket.dup "Link to this definition")

Duplicate the socket.
The newly created socket is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
Changed in version 3.4: The socket is now non-inheritable.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.fileno()[¶](https://docs.python.org/3/library/socket.html#socket.socket.fileno "Link to this definition")

Return the socket’s file descriptor (a small integer), or -1 on failure. This is useful with [`select.select()`](https://docs.python.org/3/library/select.html#select.select "select.select").
Under Windows the small integer returned by this method cannot be used where a file descriptor can be used (such as [`os.fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen")). Unix does not have this limitation.

socket.get_inheritable()[¶](https://docs.python.org/3/library/socket.html#socket.socket.get_inheritable "Link to this definition")

Get the [inheritable flag](https://docs.python.org/3/library/os.html#fd-inheritance) of the socket’s file descriptor or socket’s handle: `True` if the socket can be inherited in child processes, `False` if it cannot.
Added in version 3.4.

socket.getpeername()[¶](https://docs.python.org/3/library/socket.html#socket.socket.getpeername "Link to this definition")

Return the remote address to which the socket is connected. This is useful to find out the port number of a remote IPv4/v6 socket, for instance. (The format of the address returned depends on the address family — see above.) On some systems this function is not supported.

socket.getsockname()[¶](https://docs.python.org/3/library/socket.html#socket.socket.getsockname "Link to this definition")

Return the socket’s own address. This is useful to find out the port number of an IPv4/v6 socket, for instance. (The format of the address returned depends on the address family — see above.)

socket.getsockopt(_level_ , _optname_[, _buflen_])[¶](https://docs.python.org/3/library/socket.html#socket.socket.getsockopt "Link to this definition")

Return the value of the given socket option (see the Unix man page [SO_* etc.](https://docs.python.org/3/library/socket.html#socket-unix-constants)) are defined in this module. If _buflen_ is absent, an integer option is assumed and its integer value is returned by the function. If _buflen_ is present, it specifies the maximum length of the buffer used to receive the option in, and this buffer is returned as a bytes object. It is up to the caller to decode the contents of the buffer (see the optional built-in module [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.") for a way to decode C structures encoded as byte strings).
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.getblocking()[¶](https://docs.python.org/3/library/socket.html#socket.socket.getblocking "Link to this definition")

Return `True` if socket is in blocking mode, `False` if in non-blocking.
This is equivalent to checking `socket.gettimeout() != 0`.
Added in version 3.7.

socket.gettimeout()[¶](https://docs.python.org/3/library/socket.html#socket.socket.gettimeout "Link to this definition")

Return the timeout in seconds (float) associated with socket operations, or `None` if no timeout is set. This reflects the last call to [`setblocking()`](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "socket.socket.setblocking") or [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout").

socket.ioctl(_control_ , _option_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.ioctl "Link to this definition")

The `ioctl()` method is a limited interface to the WSAIoctl system interface. Please refer to the
On other platforms, the generic [`fcntl.fcntl()`](https://docs.python.org/3/library/fcntl.html#fcntl.fcntl "fcntl.fcntl") and [`fcntl.ioctl()`](https://docs.python.org/3/library/fcntl.html#fcntl.ioctl "fcntl.ioctl") functions may be used; they accept a socket object as their first argument.
Currently only the following control codes are supported: `SIO_RCVALL`, `SIO_KEEPALIVE_VALS`, and `SIO_LOOPBACK_FAST_PATH`.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows
Changed in version 3.6: `SIO_LOOPBACK_FAST_PATH` was added.

socket.listen([_backlog_])[¶](https://docs.python.org/3/library/socket.html#socket.socket.listen "Link to this definition")

Enable a server to accept connections. If _backlog_ is specified, it must be at least 0 (if it is lower, it is set to 0); it specifies the number of unaccepted connections that the system will allow before refusing new connections. If not specified, a default reasonable value is chosen.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
Changed in version 3.5: The _backlog_ parameter is now optional.

socket.makefile(_mode ='r'_, _buffering =None_, _*_ , _encoding =None_, _errors =None_, _newline =None_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.makefile "Link to this definition")

Return a [file object](https://docs.python.org/3/glossary.html#term-file-object) associated with the socket. The exact returned type depends on the arguments given to `makefile()`. These arguments are interpreted the same way as by the built-in [`open()`](https://docs.python.org/3/library/functions.html#open "open") function, except the only supported _mode_ values are `'r'` (default), `'w'`, `'b'`, or a combination of those.
The socket must be in blocking mode; it can have a timeout, but the file object’s internal buffer may end up in an inconsistent state if a timeout occurs.
Closing the file object returned by `makefile()` won’t close the original socket unless all other file objects have been closed and [`socket.close()`](https://docs.python.org/3/library/socket.html#socket.close "socket.close") has been called on the socket object.
Note
On Windows, the file-like object created by `makefile()` cannot be used where a file object with a file descriptor is expected, such as the stream arguments of [`subprocess.Popen()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen").

socket.recv(_bufsize_[, _flags_])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recv "Link to this definition")

Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by _bufsize_. A returned empty bytes object indicates that the client has disconnected. See the Unix manual page _flags_ ; it defaults to zero.
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

socket.recvfrom(_bufsize_[, _flags_])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recvfrom "Link to this definition")
