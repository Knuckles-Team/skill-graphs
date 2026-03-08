

socket.HV_GUID_PARENT[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_PARENT "Link to this definition")

Constants for Windows Hyper-V sockets for host/guest communications.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Added in version 3.12.

socket.ETHERTYPE_ARP[¶](https://docs.python.org/3/library/socket.html#socket.ETHERTYPE_ARP "Link to this definition")


socket.ETHERTYPE_IP[¶](https://docs.python.org/3/library/socket.html#socket.ETHERTYPE_IP "Link to this definition")


socket.ETHERTYPE_IPV6[¶](https://docs.python.org/3/library/socket.html#socket.ETHERTYPE_IPV6 "Link to this definition")


socket.ETHERTYPE_VLAN[¶](https://docs.python.org/3/library/socket.html#socket.ETHERTYPE_VLAN "Link to this definition")

[Availability](https://docs.python.org/3/library/intro.html#availability): Linux, FreeBSD, macOS.
Added in version 3.12.

socket.SHUT_RD[¶](https://docs.python.org/3/library/socket.html#socket.SHUT_RD "Link to this definition")


socket.SHUT_WR[¶](https://docs.python.org/3/library/socket.html#socket.SHUT_WR "Link to this definition")


socket.SHUT_RDWR[¶](https://docs.python.org/3/library/socket.html#socket.SHUT_RDWR "Link to this definition")

These constants are used by the [`shutdown()`](https://docs.python.org/3/library/socket.html#socket.socket.shutdown "socket.socket.shutdown") method of socket objects.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
### Functions[¶](https://docs.python.org/3/library/socket.html#functions "Link to this heading")
#### Creating sockets[¶](https://docs.python.org/3/library/socket.html#creating-sockets "Link to this heading")
The following functions all create [socket objects](https://docs.python.org/3/library/socket.html#socket-objects).

_class_ socket.socket(_family =AF_INET_, _type =SOCK_STREAM_, _proto =0_, _fileno =None_)[¶](https://docs.python.org/3/library/socket.html#socket.socket "Link to this definition")

Create a new socket using the given address family, socket type and protocol number. The address family should be [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET") (the default), [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6"), [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX"), [`AF_CAN`](https://docs.python.org/3/library/socket.html#socket.AF_CAN "socket.AF_CAN"), [`AF_PACKET`](https://docs.python.org/3/library/socket.html#socket.AF_PACKET "socket.AF_PACKET"), or [`AF_RDS`](https://docs.python.org/3/library/socket.html#socket.AF_RDS "socket.AF_RDS"). The socket type should be [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM") (the default), [`SOCK_DGRAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "socket.SOCK_DGRAM"), [`SOCK_RAW`](https://docs.python.org/3/library/socket.html#socket.SOCK_RAW "socket.SOCK_RAW") or perhaps one of the other `SOCK_` constants. The protocol number is usually zero and may be omitted or in the case where the address family is `AF_CAN` the protocol should be one of `CAN_RAW`, [`CAN_BCM`](https://docs.python.org/3/library/socket.html#socket.CAN_BCM "socket.CAN_BCM"), [`CAN_ISOTP`](https://docs.python.org/3/library/socket.html#socket.CAN_ISOTP "socket.CAN_ISOTP") or [`CAN_J1939`](https://docs.python.org/3/library/socket.html#socket.CAN_J1939 "socket.CAN_J1939").
If _fileno_ is specified, the values for _family_ , _type_ , and _proto_ are auto-detected from the specified file descriptor. Auto-detection can be overruled by calling the function with explicit _family_ , _type_ , or _proto_ arguments. This only affects how Python represents e.g. the return value of [`socket.getpeername()`](https://docs.python.org/3/library/socket.html#socket.socket.getpeername "socket.socket.getpeername") but not the actual OS resource. Unlike [`socket.fromfd()`](https://docs.python.org/3/library/socket.html#socket.fromfd "socket.fromfd"), _fileno_ will return the same socket and not a duplicate. This may help close a detached socket using [`socket.close()`](https://docs.python.org/3/library/socket.html#socket.close "socket.close").
The newly created socket is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.__new__` with arguments `self`, `family`, `type`, `protocol`.
Changed in version 3.3: The AF_CAN family was added. The AF_RDS family was added.
Changed in version 3.4: The CAN_BCM protocol was added.
Changed in version 3.4: The returned socket is now non-inheritable.
Changed in version 3.7: The CAN_ISOTP protocol was added.
Changed in version 3.7: When [`SOCK_NONBLOCK`](https://docs.python.org/3/library/socket.html#socket.SOCK_NONBLOCK "socket.SOCK_NONBLOCK") or [`SOCK_CLOEXEC`](https://docs.python.org/3/library/socket.html#socket.SOCK_CLOEXEC "socket.SOCK_CLOEXEC") bit flags are applied to _type_ they are cleared, and [`socket.type`](https://docs.python.org/3/library/socket.html#socket.socket.type "socket.socket.type") will not reflect them. They are still passed to the underlying system `socket()` call. Therefore,
Copy```
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM | socket.SOCK_NONBLOCK)

```

will still create a non-blocking socket on OSes that support `SOCK_NONBLOCK`, but `sock.type` will be set to `socket.SOCK_STREAM`.
Changed in version 3.9: The CAN_J1939 protocol was added.
Changed in version 3.10: The IPPROTO_MPTCP protocol was added.

socket.socketpair([_family_[, _type_[, _proto_]]])[¶](https://docs.python.org/3/library/socket.html#socket.socketpair "Link to this definition")

Build a pair of connected socket objects using the given address family, socket type, and protocol number. Address family, socket type, and protocol number are as for the [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket") function above. The default family is [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX") if defined on the platform; otherwise, the default is [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET").
The newly created sockets are [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
Changed in version 3.2: The returned socket objects now support the whole socket API, rather than a subset.
Changed in version 3.4: The returned sockets are now non-inheritable.
Changed in version 3.5: Windows support added.

socket.create_connection(_address_ , _timeout =GLOBAL_DEFAULT_, _source_address =None_, _*_ , _all_errors =False_)[¶](https://docs.python.org/3/library/socket.html#socket.create_connection "Link to this definition")

Connect to a TCP service listening on the internet _address_ (a 2-tuple `(host, port)`), and return the socket object. This is a higher-level function than [`socket.connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect"): if _host_ is a non-numeric hostname, it will try to resolve it for both [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET") and [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6"), and then try to connect to all possible addresses in turn until a connection succeeds. This makes it easy to write clients that are compatible to both IPv4 and IPv6.
Passing the optional _timeout_ parameter will set the timeout on the socket instance before attempting to connect. If no _timeout_ is supplied, the global default timeout setting returned by [`getdefaulttimeout()`](https://docs.python.org/3/library/socket.html#socket.getdefaulttimeout "socket.getdefaulttimeout") is used.
If supplied, _source_address_ must be a 2-tuple `(host, port)` for the socket to bind to as its source address before connecting. If host or port are ‘’ or 0 respectively the OS default behavior will be used.
When a connection cannot be created, an exception is raised. By default, it is the exception from the last address in the list. If _all_errors_ is `True`, it is an [`ExceptionGroup`](https://docs.python.org/3/library/exceptions.html#ExceptionGroup "ExceptionGroup") containing the errors of all attempts.
Changed in version 3.2: _source_address_ was added.
Changed in version 3.11: _all_errors_ was added.

socket.create_server(_address_ , _*_ , _family =AF_INET_, _backlog =None_, _reuse_port =False_, _dualstack_ipv6 =False_)[¶](https://docs.python.org/3/library/socket.html#socket.create_server "Link to this definition")

Convenience function which creates a TCP socket bound to _address_ (a 2-tuple `(host, port)`) and returns the socket object.
_family_ should be either [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET") or [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6"). _backlog_ is the queue size passed to [`socket.listen()`](https://docs.python.org/3/library/socket.html#socket.socket.listen "socket.socket.listen"); if not specified , a default reasonable value is chosen. _reuse_port_ dictates whether to set the `SO_REUSEPORT` socket option.
If _dualstack_ipv6_ is true, _family_ is [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6") and the platform supports it the socket will be able to accept both IPv4 and IPv6 connections, else it will raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). Most POSIX platforms and Windows are supposed to support this functionality. When this functionality is enabled the address returned by [`socket.getpeername()`](https://docs.python.org/3/library/socket.html#socket.socket.getpeername "socket.socket.getpeername") when an IPv4 connection occurs will be an IPv6 address represented as an IPv4-mapped IPv6 address. If _dualstack_ipv6_ is false it will explicitly disable this functionality on platforms that enable it by default (e.g. Linux). This parameter can be used in conjunction with [`has_dualstack_ipv6()`](https://docs.python.org/3/library/socket.html#socket.has_dualstack_ipv6 "socket.has_dualstack_ipv6"):
Copy```
import socket

addr = ("", 8080)  # all interfaces, port 8080
if socket.has_dualstack_ipv6():
    s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
else:
    s = socket.create_server(addr)

```

Note
On POSIX platforms the `SO_REUSEADDR` socket option is set in order to immediately reuse previous sockets which were bound on the same _address_ and remained in TIME_WAIT state.
Added in version 3.8.

socket.has_dualstack_ipv6()[¶](https://docs.python.org/3/library/socket.html#socket.has_dualstack_ipv6 "Link to this definition")

Return `True` if the platform supports creating a TCP socket which can handle both IPv4 and IPv6 connections.
Added in version 3.8.

socket.fromfd(_fd_ , _family_ , _type_ , _proto =0_)[¶](https://docs.python.org/3/library/socket.html#socket.fromfd "Link to this definition")

Duplicate the file descriptor _fd_ (an integer as returned by a file object’s [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno") method) and build a socket object from the result. Address family, socket type and protocol number are as for the [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket") function above. The file descriptor should refer to a socket, but this is not checked — subsequent operations on the object may fail if the file descriptor is invalid. This function is rarely needed, but can be used to get or set socket options on a socket passed to a program as standard input or output (such as a server started by the Unix inet daemon). The socket is assumed to be in blocking mode.
The newly created socket is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).
Changed in version 3.4: The returned socket is now non-inheritable.

socket.fromshare(_data_)[¶](https://docs.python.org/3/library/socket.html#socket.fromshare "Link to this definition")

Instantiate a socket from data obtained from the [`socket.share()`](https://docs.python.org/3/library/socket.html#socket.socket.share "socket.socket.share") method. The socket is assumed to be in blocking mode.
[Availability](https://docs.python.org/3/library/intro.html#availability): Windows.
Added in version 3.3.

socket.SocketType[¶](https://docs.python.org/3/library/socket.html#socket.SocketType "Link to this definition")

This is a Python type object that represents the socket object type. It is the same as `type(socket(...))`.
#### Other functions[¶](https://docs.python.org/3/library/socket.html#other-functions "Link to this heading")
The `socket` module also offers various network-related services:

socket.close(_fd_)[¶](https://docs.python.org/3/library/socket.html#socket.close "Link to this definition")

Close a socket file descriptor. This is like [`os.close()`](https://docs.python.org/3/library/os.html#os.close "os.close"), but for sockets. On some platforms (most notably Windows) `os.close()` does not work for socket file descriptors.
Added in version 3.7.

socket.getaddrinfo(_host_ , _port_ , _family =AF_UNSPEC_, _type =0_, _proto =0_, _flags =0_)[¶](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "Link to this definition")

This function wraps the C function `getaddrinfo` of the underlying system.
Translate the _host_ /_port_ argument into a sequence of 5-tuples that contain all the necessary arguments for creating a socket connected to that service. _host_ is a domain name, a string representation of an IPv4/v6 address or `None`. _port_ is a string service name such as `'http'`, a numeric port number or `None`. By passing `None` as the value of _host_ and _port_ , you can pass `NULL` to the underlying C API.
The _family_ , _type_ and _proto_ arguments can be optionally specified in order to provide options and limit the list of addresses returned. Pass their default values ([`AF_UNSPEC`](https://docs.python.org/3/library/socket.html#socket.AF_UNSPEC "socket.AF_UNSPEC"), 0, and 0, respectively) to not limit the results. See the note below for details.
The _flags_ argument can be one or several of the `AI_*` constants, and will influence how results are computed and returned. For example, `AI_NUMERICHOST` will disable domain name resolution and will raise an error if _host_ is a domain name.
The function returns a list of 5-tuples with the following structure:
`(family, type, proto, canonname, sockaddr)`
In these tuples, _family_ , _type_ , _proto_ are all integers and are meant to be passed to the [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket") function. _canonname_ will be a string representing the canonical name of the _host_ if `AI_CANONNAME` is part of the _flags_ argument; else _canonname_ will be empty. _sockaddr_ is a tuple describing a socket address, whose format depends on the returned _family_ (a `(address, port)` 2-tuple for [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET"), a `(address, port, flowinfo, scope_id)` 4-tuple for [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")), and is meant to be passed to the [`socket.connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect") method.
Note
If you intend to use results from `getaddrinfo()` to create a socket (rather than, for example, retrieve _canonname_), consider limiting the results by _type_ (e.g. [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM") or [`SOCK_DGRAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "socket.SOCK_DGRAM")) and/or _proto_ (e.g. `IPPROTO_TCP` or `IPPROTO_UDP`) that your application can handle.
The behavior with default values of _family_ , _type_ , _proto_ and _flags_ is system-specific.
Many systems (for example, most Linux configurations) will return a sorted list of all matching addresses. These addresses should generally be tried in order until a connection succeeds (possibly tried in parallel, for example, using a _type_ and/or _proto_ can help eliminate unsuccessful or unusable connection attempts.
Some systems will, however, only return a single address. (For example, this was reported on Solaris and AIX configurations.) On these systems, limiting the _type_ and/or _proto_ helps ensure that this address is usable.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.getaddrinfo` with arguments `host`, `port`, `family`, `type`, `protocol`.
The following example fetches address information for a hypothetical TCP connection to `example.org` on port 80 (results may differ on your system if IPv6 isn’t enabled):
Copy```
>>> socket.getaddrinfo("example.org", 80, proto=socket.IPPROTO_TCP)
[(socket.AF_INET6, socket.SOCK_STREAM,
 6, '', ('2606:2800:220:1:248:1893:25c8:1946', 80, 0, 0)),
 (socket.AF_INET, socket.SOCK_STREAM,
 6, '', ('93.184.216.34', 80))]

```

Changed in version 3.2: parameters can now be passed using keyword arguments.
Changed in version 3.7: for IPv6 multicast addresses, string representing an address will not contain `%scope_id` part.

socket.getfqdn([_name_])[¶](https://docs.python.org/3/library/socket.html#socket.getfqdn "Link to this definition")

Return a fully qualified domain name for _name_. If _name_ is omitted or empty, it is interpreted as the local host. To find the fully qualified name, the hostname returned by [`gethostbyaddr()`](https://docs.python.org/3/library/socket.html#socket.gethostbyaddr "socket.gethostbyaddr") is checked, followed by aliases for the host, if available. The first name which includes a period is selected. In case no fully qualified domain name is available and _name_ was provided, it is returned unchanged. If _name_ was empty or equal to `'0.0.0.0'`, the hostname from [`gethostname()`](https://docs.python.org/3/library/socket.html#socket.gethostname "socket.gethostname") is returned.

socket.gethostbyname(_hostname_)[¶](https://docs.python.org/3/library/socket.html#socket.gethostbyname "Link to this definition")

Translate a host name to IPv4 address format. The IPv4 address is returned as a string, such as `'100.50.200.5'`. If the host name is an IPv4 address itself it is returned unchanged. See [`gethostbyname_ex()`](https://docs.python.org/3/library/socket.html#socket.gethostbyname_ex "socket.gethostbyname_ex") for a more complete interface. `gethostbyname()` does not support IPv6 name resolution, and [`getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo") should be used instead for IPv4/v6 dual stack support.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.gethostbyname` with argument `hostname`.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.gethostbyname_ex(_hostname_)[¶](https://docs.python.org/3/library/socket.html#socket.gethostbyname_ex "Link to this definition")

Translate a host name to IPv4 address format, extended interface. Return a 3-tuple `(hostname, aliaslist, ipaddrlist)` where _hostname_ is the host’s primary host name, _aliaslist_ is a (possibly empty) list of alternative host names for the same address, and _ipaddrlist_ is a list of IPv4 addresses for the same interface on the same host (often but not always a single address). `gethostbyname_ex()` does not support IPv6 name resolution, and [`getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo") should be used instead for IPv4/v6 dual stack support.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.gethostbyname` with argument `hostname`.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.gethostname()[¶](https://docs.python.org/3/library/socket.html#socket.gethostname "Link to this definition")

Return a string containing the hostname of the machine where the Python interpreter is currently executing.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.gethostname` with no arguments.
Note: `gethostname()` doesn’t always return the fully qualified domain name; use [`getfqdn()`](https://docs.python.org/3/library/socket.html#socket.getfqdn "socket.getfqdn") for that.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.gethostbyaddr(_ip_address_)[¶](https://docs.python.org/3/library/socket.html#socket.gethostbyaddr "Link to this definition")

Return a 3-tuple `(hostname, aliaslist, ipaddrlist)` where _hostname_ is the primary host name responding to the given _ip_address_ , _aliaslist_ is a (possibly empty) list of alternative host names for the same address, and _ipaddrlist_ is a list of IPv4/v6 addresses for the same interface on the same host (most likely containing only a single address). To find the fully qualified domain name, use the function [`getfqdn()`](https://docs.python.org/3/library/socket.html#socket.getfqdn "socket.getfqdn"). `gethostbyaddr()` supports both IPv4 and IPv6.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.gethostbyaddr` with argument `ip_address`.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.getnameinfo(_sockaddr_ , _flags_)[¶](https://docs.python.org/3/library/socket.html#socket.getnameinfo "Link to this definition")

Translate a socket address _sockaddr_ into a 2-tuple `(host, port)`. Depending on the settings of _flags_ , the result can contain a fully qualified domain name or numeric address representation in _host_. Similarly, _port_ can contain a string port name or a numeric port number.
For IPv6 addresses, `%scope_id` is appended to the host part if _sockaddr_ contains meaningful _scope_id_. Usually this happens for multicast addresses.
For more information about _flags_ you can consult
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.getnameinfo` with argument `sockaddr`.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.getprotobyname(_protocolname_)[¶](https://docs.python.org/3/library/socket.html#socket.getprotobyname "Link to this definition")

Translate an internet protocol name (for example, `'icmp'`) to a constant suitable for passing as the (optional) third argument to the [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket") function. This is usually only needed for sockets opened in “raw” mode ([`SOCK_RAW`](https://docs.python.org/3/library/socket.html#socket.SOCK_RAW "socket.SOCK_RAW")); for the normal socket modes, the correct protocol is chosen automatically if the protocol is omitted or zero.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.getservbyname(_servicename_[, _protocolname_])[¶](https://docs.python.org/3/library/socket.html#socket.getservbyname "Link to this definition")

Translate an internet service name and protocol name to a port number for that service. The optional protocol name, if given, should be `'tcp'` or `'udp'`, otherwise any protocol will match.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.getservbyname` with arguments `servicename`, `protocolname`.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.getservbyport(_port_[, _protocolname_])[¶](https://docs.python.org/3/library/socket.html#socket.getservbyport "Link to this definition")

Translate an internet port number and protocol name to a service name for that service. The optional protocol name, if given, should be `'tcp'` or `'udp'`, otherwise any protocol will match.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `socket.getservbyport` with arguments `port`, `protocolname`.
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

socket.ntohl(_x_)[¶](https://docs.python.org/3/library/socket.html#socket.ntohl "Link to this definition")

Convert 32-bit positive integers from network to host byte order. On machines where the host byte order is the same as network byte order, this is a no-op; otherwise, it performs a 4-byte swap operation.

socket.ntohs(_x_)[¶](https://docs.python.org/3/library/socket.html#socket.ntohs "Link to this definition")

Convert 16-bit positive integers from network to host byte order. On machines where the host byte order is the same as network byte order, this is a no-op; otherwise, it performs a 2-byte swap operation.
Changed in version 3.10: Raises [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") if _x_ does not fit in a 16-bit unsigned integer.

socket.htonl(_x_)[¶](https://docs.python.org/3/library/socket.html#socket.htonl "Link to this definition")

Convert 32-bit positive integers from host to network byte order. On machines where the host byte order is the same as network byte order, this is a no-op; otherwise, it performs a 4-byte swap operation.
