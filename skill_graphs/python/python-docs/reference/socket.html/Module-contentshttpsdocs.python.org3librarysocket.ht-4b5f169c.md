
Receive data from the socket. The return value is a pair `(bytes, address)` where _bytes_ is a bytes object representing the data received and _address_ is the address of the socket sending the data. See the Unix manual page _flags_ ; it defaults to zero. (The format of _address_ depends on the address family — see above.)
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).
Changed in version 3.7: For multicast IPv6 address, first item of _address_ does not contain `%scope_id` part anymore. In order to get full IPv6 address use [`getnameinfo()`](https://docs.python.org/3/library/socket.html#socket.getnameinfo "socket.getnameinfo").

socket.recvmsg(_bufsize_[, _ancbufsize_[, _flags_]])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "Link to this definition")

Receive normal data (up to _bufsize_ bytes) and ancillary data from the socket. The _ancbufsize_ argument sets the size in bytes of the internal buffer used to receive the ancillary data; it defaults to 0, meaning that no ancillary data will be received. Appropriate buffer sizes for ancillary data can be calculated using [`CMSG_SPACE()`](https://docs.python.org/3/library/socket.html#socket.CMSG_SPACE "socket.CMSG_SPACE") or [`CMSG_LEN()`](https://docs.python.org/3/library/socket.html#socket.CMSG_LEN "socket.CMSG_LEN"), and items which do not fit into the buffer might be truncated or discarded. The _flags_ argument defaults to 0 and has the same meaning as for [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv").
The return value is a 4-tuple: `(data, ancdata, msg_flags, address)`. The _data_ item is a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object holding the non-ancillary data received. The _ancdata_ item is a list of zero or more tuples `(cmsg_level, cmsg_type, cmsg_data)` representing the ancillary data (control messages) received: _cmsg_level_ and _cmsg_type_ are integers specifying the protocol level and protocol-specific type respectively, and _cmsg_data_ is a `bytes` object holding the associated data. The _msg_flags_ item is the bitwise OR of various flags indicating conditions on the received message; see your system documentation for details. If the receiving socket is unconnected, _address_ is the address of the sending socket, if available; otherwise, its value is unspecified.
On some systems, [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg") and `recvmsg()` can be used to pass file descriptors between processes over an [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX") socket. When this facility is used (it is often restricted to [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM") sockets), `recvmsg()` will return, in its ancillary data, items of the form `(socket.SOL_SOCKET, socket.SCM_RIGHTS, fds)`, where _fds_ is a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object representing the new file descriptors as a binary array of the native C int type. If `recvmsg()` raises an exception after the system call returns, it will first attempt to close any file descriptors received via this mechanism.
Some systems do not indicate the truncated length of ancillary data items which have been only partially received. If an item appears to extend beyond the end of the buffer, `recvmsg()` will issue a [`RuntimeWarning`](https://docs.python.org/3/library/exceptions.html#RuntimeWarning "RuntimeWarning"), and will return the part of it which is inside the buffer provided it has not been truncated before the start of its associated data.
On systems which support the `SCM_RIGHTS` mechanism, the following function will receive up to _maxfds_ file descriptors, returning the message data and a list containing the descriptors (while ignoring unexpected conditions such as unrelated control messages being received). See also [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg").
Copy```
import socket, array

def recv_fds(sock, msglen, maxfds):
    fds = array.array("i")   # Array of ints
    msg, ancdata, flags, addr = sock.recvmsg(msglen, socket.CMSG_LEN(maxfds * fds.itemsize))
    for cmsg_level, cmsg_type, cmsg_data in ancdata:
        if cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS:
            # Append data, ignoring any truncated integers at the end.
            fds.frombytes(cmsg_data[:len(cmsg_data) - (len(cmsg_data) % fds.itemsize)])
    return msg, list(fds)

```

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Most Unix platforms.
Added in version 3.3.
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

socket.recvmsg_into(_buffers_[, _ancbufsize_[, _flags_]])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg_into "Link to this definition")

Receive normal data and ancillary data from the socket, behaving as [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg") would, but scatter the non-ancillary data into a series of buffers instead of returning a new bytes object. The _buffers_ argument must be an iterable of objects that export writable buffers (e.g. [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") objects); these will be filled with successive chunks of the non-ancillary data until it has all been written or there are no more buffers. The operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf") value `SC_IOV_MAX`) on the number of buffers that can be used. The _ancbufsize_ and _flags_ arguments have the same meaning as for `recvmsg()`.
The return value is a 4-tuple: `(nbytes, ancdata, msg_flags, address)`, where _nbytes_ is the total number of bytes of non-ancillary data written into the buffers, and _ancdata_ , _msg_flags_ and _address_ are the same as for [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg").
Example:
Copy```
>>> import socket
>>> s1, s2 = socket.socketpair()
>>> b1 = bytearray(b'----')
>>> b2 = bytearray(b'0123456789')
>>> b3 = bytearray(b'--------------')
>>> s1.send(b'Mary had a little lamb')
22
>>> s2.recvmsg_into([b1, memoryview(b2)[2:9], b3])
(22, [], 0, None)
>>> [b1, b2, b3]
[bytearray(b'Mary'), bytearray(b'01 had a 9'), bytearray(b'little lamb---')]

```

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.
Most Unix platforms.
Added in version 3.3.

socket.recvfrom_into(_buffer_[, _nbytes_[, _flags_]])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recvfrom_into "Link to this definition")

Receive data from the socket, writing it into _buffer_ instead of creating a new bytestring. The return value is a pair `(nbytes, address)` where _nbytes_ is the number of bytes received and _address_ is the address of the socket sending the data. See the Unix manual page _flags_ ; it defaults to zero. (The format of _address_ depends on the address family — see above.)

socket.recv_into(_buffer_[, _nbytes_[, _flags_]])[¶](https://docs.python.org/3/library/socket.html#socket.socket.recv_into "Link to this definition")

Receive up to _nbytes_ bytes from the socket, storing the data into a buffer rather than creating a new bytestring. If _nbytes_ is not specified (or 0), receive up to the size available in the given buffer. Returns the number of bytes received. See the Unix manual page _flags_ ; it defaults to zero.

socket.send(_bytes_[, _flags_])[¶](https://docs.python.org/3/library/socket.html#socket.socket.send "Link to this definition")

Send data to the socket. The socket must be connected to a remote socket. The optional _flags_ argument has the same meaning as for [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv") above. Returns the number of bytes sent. Applications are responsible for checking that all data has been sent; if only some of the data was transmitted, the application needs to attempt delivery of the remaining data. For further information on this topic, consult the [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html#socket-howto).
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

socket.sendall(_bytes_[, _flags_])[¶](https://docs.python.org/3/library/socket.html#socket.socket.sendall "Link to this definition")

Send data to the socket. The socket must be connected to a remote socket. The optional _flags_ argument has the same meaning as for [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv") above. Unlike [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send"), this method continues to send data from _bytes_ until either all data has been sent or an error occurs. `None` is returned on success. On error, an exception is raised, and there is no way to determine how much data, if any, was successfully sent.
Changed in version 3.5: The socket timeout is no longer reset each time data is sent successfully. The socket timeout is now the maximum total duration to send all data.
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

socket.sendto(_bytes_ , _address_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.sendto "Link to this definition")


socket.sendto(_bytes_ , _flags_ , _address_)

Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by _address_. The optional _flags_ argument has the same meaning as for [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv") above. Return the number of bytes sent. (The format of _address_ depends on the address family — see above.)
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.sendto` with arguments `self`, `address`.
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

socket.sendmsg(_buffers_[, _ancdata_[, _flags_[, _address_]]])[¶](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "Link to this definition")

Send normal and ancillary data to the socket, gathering the non-ancillary data from a series of buffers and concatenating it into a single message. The _buffers_ argument specifies the non-ancillary data as an iterable of [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) (e.g. [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects); the operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf") value `SC_IOV_MAX`) on the number of buffers that can be used. The _ancdata_ argument specifies the ancillary data (control messages) as an iterable of zero or more tuples `(cmsg_level, cmsg_type, cmsg_data)`, where _cmsg_level_ and _cmsg_type_ are integers specifying the protocol level and protocol-specific type respectively, and _cmsg_data_ is a bytes-like object holding the associated data. Note that some systems (in particular, systems without [`CMSG_SPACE()`](https://docs.python.org/3/library/socket.html#socket.CMSG_SPACE "socket.CMSG_SPACE")) might support sending only one control message per call. The _flags_ argument defaults to 0 and has the same meaning as for [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send"). If _address_ is supplied and not `None`, it sets a destination address for the message. The return value is the number of bytes of non-ancillary data sent.
The following function sends the list of file descriptors _fds_ over an [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX") socket, on systems which support the `SCM_RIGHTS` mechanism. See also [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg").
Copy```
import socket, array

def send_fds(sock, msg, fds):
    return sock.sendmsg([msg], [(socket.SOL_SOCKET, socket.SCM_RIGHTS, array.array("i", fds))])

```

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI.
Most Unix platforms.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.sendmsg` with arguments `self`, `address`.
Added in version 3.3.
Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the method now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") exception (see [**PEP 475**](https://peps.python.org/pep-0475/) for the rationale).

socket.sendmsg_afalg([_msg_ , ]_*_ , _op_[, _iv_[, _assoclen_[, _flags_]]])[¶](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg_afalg "Link to this definition")

Specialized version of [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg") for [`AF_ALG`](https://docs.python.org/3/library/socket.html#socket.AF_ALG "socket.AF_ALG") socket. Set mode, IV, AEAD associated data length and flags for `AF_ALG` socket.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.38.
Added in version 3.6.

socket.sendfile(_file_ , _offset =0_, _count =None_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.sendfile "Link to this definition")

Send a file until EOF is reached by using high-performance [`os.sendfile`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile") and return the total number of bytes which were sent. _file_ must be a regular file object opened in binary mode. If `os.sendfile` is not available (e.g. Windows) or _file_ is not a regular file [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send") will be used instead. _offset_ tells from where to start reading the file. If specified, _count_ is the total number of bytes to transmit as opposed to sending the file until EOF is reached. File position is updated on return or also in case of error in which case [`file.tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell") can be used to figure out the number of bytes which were sent. The socket must be of [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM") type. Non-blocking sockets are not supported.
Added in version 3.5.

socket.set_inheritable(_inheritable_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.set_inheritable "Link to this definition")

Set the [inheritable flag](https://docs.python.org/3/library/os.html#fd-inheritance) of the socket’s file descriptor or socket’s handle.
Added in version 3.4.

socket.setblocking(_flag_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "Link to this definition")

Set blocking or non-blocking mode of the socket: if _flag_ is false, the socket is set to non-blocking, else to blocking mode.
This method is a shorthand for certain [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout") calls:
  * `sock.setblocking(True)` is equivalent to `sock.settimeout(None)`
  * `sock.setblocking(False)` is equivalent to `sock.settimeout(0.0)`


Changed in version 3.7: The method no longer applies [`SOCK_NONBLOCK`](https://docs.python.org/3/library/socket.html#socket.SOCK_NONBLOCK "socket.SOCK_NONBLOCK") flag on [`socket.type`](https://docs.python.org/3/library/socket.html#socket.socket.type "socket.socket.type").

socket.settimeout(_value_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "Link to this definition")

Set a timeout on blocking socket operations. The _value_ argument can be a nonnegative floating-point number expressing seconds, or `None`. If a non-zero value is given, subsequent socket operations will raise a [`timeout`](https://docs.python.org/3/library/socket.html#socket.timeout "socket.timeout") exception if the timeout period _value_ has elapsed before the operation has completed. If zero is given, the socket is put in non-blocking mode. If `None` is given, the socket is put in blocking mode.
For further information, please consult the [notes on socket timeouts](https://docs.python.org/3/library/socket.html#socket-timeouts).
Changed in version 3.7: The method no longer toggles [`SOCK_NONBLOCK`](https://docs.python.org/3/library/socket.html#socket.SOCK_NONBLOCK "socket.SOCK_NONBLOCK") flag on [`socket.type`](https://docs.python.org/3/library/socket.html#socket.socket.type "socket.socket.type").

socket.setsockopt(_level_ , _optname_ , _value :[int](https://docs.python.org/3/library/functions.html#int "int")|[Buffer](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.setsockopt "Link to this definition")


socket.setsockopt(_level_ , _optname_ , _None_ , _optlen: int_)

Set the value of the given socket option (see the Unix manual page SO_* etc. <socket-unix-constants>). The value can be an integer, `None` or a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) representing a buffer. In the latter case it is up to the caller to ensure that the bytestring contains the proper bits (see the optional built-in module [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.") for a way to encode C structures as bytestrings). When _value_ is set to `None`, _optlen_ argument is required. It’s equivalent to calling `setsockopt()` C function with `optval=NULL` and `optlen=optlen`.
Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) is now accepted.
Changed in version 3.6: setsockopt(level, optname, None, optlen: int) form added.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.shutdown(_how_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.shutdown "Link to this definition")

Shut down one or both halves of the connection. If _how_ is [`SHUT_RD`](https://docs.python.org/3/library/socket.html#socket.SHUT_RD "socket.SHUT_RD"), further receives are disallowed. If _how_ is [`SHUT_WR`](https://docs.python.org/3/library/socket.html#socket.SHUT_WR "socket.SHUT_WR"), further sends are disallowed. If _how_ is [`SHUT_RDWR`](https://docs.python.org/3/library/socket.html#socket.SHUT_RDWR "socket.SHUT_RDWR"), further sends and receives are disallowed.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.share(_process_id_)[¶](https://docs.python.org/3/library/socket.html#socket.socket.share "Link to this definition")

Duplicate a socket and prepare it for sharing with a target process. The target process must be provided with _process_id_. The resulting bytes object can then be passed to the target process using some form of interprocess communication and the socket can be recreated there using [`fromshare()`](https://docs.python.org/3/library/socket.html#socket.fromshare "socket.fromshare"). Once this method has been called, it is safe to close the socket since the operating system has already duplicated it for the target process.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Added in version 3.3.
Note that there are no methods `read()` or `write()`; use [`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv") and [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send") without _flags_ argument instead.
Socket objects also have these (read-only) attributes that correspond to the values given to the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket") constructor.

socket.family[¶](https://docs.python.org/3/library/socket.html#socket.socket.family "Link to this definition")

The socket family.

socket.type[¶](https://docs.python.org/3/library/socket.html#socket.socket.type "Link to this definition")

The socket type.

socket.proto[¶](https://docs.python.org/3/library/socket.html#socket.socket.proto "Link to this definition")

The socket protocol.
