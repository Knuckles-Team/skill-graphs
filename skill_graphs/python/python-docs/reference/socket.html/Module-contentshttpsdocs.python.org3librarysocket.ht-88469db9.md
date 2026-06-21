## Module contents[¶](https://docs.python.org/3/library/socket.html#module-contents "Link to this heading")
The module `socket` exports the following elements.
### Exceptions[¶](https://docs.python.org/3/library/socket.html#exceptions "Link to this heading")

_exception_ socket.error[¶](https://docs.python.org/3/library/socket.html#socket.error "Link to this definition")

A deprecated alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
Changed in version 3.3: Following [**PEP 3151**](https://peps.python.org/pep-3151/), this class was made an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

_exception_ socket.herror[¶](https://docs.python.org/3/library/socket.html#socket.herror "Link to this definition")

A subclass of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), this exception is raised for address-related errors, i.e. for functions that use _h_errno_ in the POSIX C API, including [`gethostbyname_ex()`](https://docs.python.org/3/library/socket.html#socket.gethostbyname_ex "socket.gethostbyname_ex") and [`gethostbyaddr()`](https://docs.python.org/3/library/socket.html#socket.gethostbyaddr "socket.gethostbyaddr"). The accompanying value is a pair `(h_errno, string)` representing an error returned by a library call. _h_errno_ is a numeric value, while _string_ represents the description of _h_errno_ , as returned by the `hstrerror()` C function.
Changed in version 3.3: This class was made a subclass of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

_exception_ socket.gaierror[¶](https://docs.python.org/3/library/socket.html#socket.gaierror "Link to this definition")

A subclass of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), this exception is raised for address-related errors by [`getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo") and [`getnameinfo()`](https://docs.python.org/3/library/socket.html#socket.getnameinfo "socket.getnameinfo"). The accompanying value is a pair `(error, string)` representing an error returned by a library call. _string_ represents the description of _error_ , as returned by the `gai_strerror()` C function. The numeric _error_ value will match one of the `EAI_*` constants defined in this module.
Changed in version 3.3: This class was made a subclass of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

_exception_ socket.timeout[¶](https://docs.python.org/3/library/socket.html#socket.timeout "Link to this definition")

A deprecated alias of [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError").
A subclass of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), this exception is raised when a timeout occurs on a socket which has had timeouts enabled via a prior call to [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout") (or implicitly through [`setdefaulttimeout()`](https://docs.python.org/3/library/socket.html#socket.setdefaulttimeout "socket.setdefaulttimeout")). The accompanying value is a string whose value is currently always “timed out”.
Changed in version 3.3: This class was made a subclass of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
Changed in version 3.10: This class was made an alias of [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError").
### Constants[¶](https://docs.python.org/3/library/socket.html#constants "Link to this heading")
The AF_* and SOCK_* constants are now `AddressFamily` and `SocketKind` [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") collections.
Added in version 3.4.

socket.AF_UNIX[¶](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "Link to this definition")


socket.AF_INET[¶](https://docs.python.org/3/library/socket.html#socket.AF_INET "Link to this definition")


socket.AF_INET6[¶](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "Link to this definition")

These constants represent the address (and protocol) families, used for the first argument to [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket"). If the [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX") constant is not defined then this protocol is unsupported. More constants may be available depending on the system.

socket.AF_UNSPEC[¶](https://docs.python.org/3/library/socket.html#socket.AF_UNSPEC "Link to this definition")

[`AF_UNSPEC`](https://docs.python.org/3/library/socket.html#socket.AF_UNSPEC "socket.AF_UNSPEC") means that [`getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo") should return socket addresses for any address family (either IPv4, IPv6, or any other) that can be used.

socket.SOCK_STREAM[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "Link to this definition")


socket.SOCK_DGRAM[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "Link to this definition")


socket.SOCK_RAW[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_RAW "Link to this definition")


socket.SOCK_RDM[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_RDM "Link to this definition")


socket.SOCK_SEQPACKET[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_SEQPACKET "Link to this definition")

These constants represent the socket types, used for the second argument to [`socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket"). More constants may be available depending on the system. (Only [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM") and [`SOCK_DGRAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "socket.SOCK_DGRAM") appear to be generally useful.)

socket.SOCK_CLOEXEC[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_CLOEXEC "Link to this definition")


socket.SOCK_NONBLOCK[¶](https://docs.python.org/3/library/socket.html#socket.SOCK_NONBLOCK "Link to this definition")

These two constants, if defined, can be combined with the socket types and allow you to set some flags atomically (thus avoiding possible race conditions and the need for separate calls).
See also
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.27.
Added in version 3.2.

SO_*


socket.SOMAXCONN[¶](https://docs.python.org/3/library/socket.html#socket.SOMAXCONN "Link to this definition")


MSG_*


SOL_*


SCM_*


IPPROTO_*


IPPORT_*


INADDR_*


IP_*


IPV6_*


EAI_*


AI_*


NI_*


TCP_*

Many constants of these forms, documented in the Unix documentation on sockets and/or the IP protocol, are also defined in the socket module. They are generally used in arguments to the [`setsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.setsockopt "socket.socket.setsockopt") and [`getsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.getsockopt "socket.socket.getsockopt") methods of socket objects. In most cases, only those symbols that are defined in the Unix header files are defined; for a few symbols, default values are provided.
Changed in version 3.6: `SO_DOMAIN`, `SO_PROTOCOL`, `SO_PEERSEC`, `SO_PASSSEC`, `TCP_USER_TIMEOUT`, `TCP_CONGESTION` were added.
Changed in version 3.6.5: Added support for `TCP_FASTOPEN`, `TCP_KEEPCNT` on Windows platforms when available.
Changed in version 3.7: `TCP_NOTSENT_LOWAT` was added.
Added support for `TCP_KEEPIDLE`, `TCP_KEEPINTVL` on Windows platforms when available.
Changed in version 3.10: `IP_RECVTOS` was added. Added `TCP_KEEPALIVE`. On MacOS this constant can be used in the same way that `TCP_KEEPIDLE` is used on Linux.
Changed in version 3.11: Added `TCP_CONNECTION_INFO`. On MacOS this constant can be used in the same way that `TCP_INFO` is used on Linux and BSD.
Changed in version 3.12: Added `SO_RTABLE` and `SO_USER_COOKIE`. On OpenBSD and FreeBSD respectively those constants can be used in the same way that `SO_MARK` is used on Linux. Also added missing TCP socket options from Linux: `TCP_MD5SIG`, `TCP_THIN_LINEAR_TIMEOUTS`, `TCP_THIN_DUPACK`, `TCP_REPAIR`, `TCP_REPAIR_QUEUE`, `TCP_QUEUE_SEQ`, `TCP_REPAIR_OPTIONS`, `TCP_TIMESTAMP`, `TCP_CC_INFO`, `TCP_SAVE_SYN`, `TCP_SAVED_SYN`, `TCP_REPAIR_WINDOW`, `TCP_FASTOPEN_CONNECT`, `TCP_ULP`, `TCP_MD5SIG_EXT`, `TCP_FASTOPEN_KEY`, `TCP_FASTOPEN_NO_COOKIE`, `TCP_ZEROCOPY_RECEIVE`, `TCP_INQ`, `TCP_TX_DELAY`. Added `IP_PKTINFO`, `IP_UNBLOCK_SOURCE`, `IP_BLOCK_SOURCE`, `IP_ADD_SOURCE_MEMBERSHIP`, `IP_DROP_SOURCE_MEMBERSHIP`.
Changed in version 3.13: Added `SO_BINDTOIFINDEX`. On Linux this constant can be used in the same way that `SO_BINDTODEVICE` is used, but with the index of a network interface instead of its name.
Changed in version 3.14: Added missing `IP_FREEBIND`, `IP_RECVERR`, `IPV6_RECVERR`, `IP_RECVTTL`, and `IP_RECVORIGDSTADDR` on Linux.
Changed in version 3.14: Added support for `TCP_QUICKACK` on Windows platforms when available.

socket.AF_CAN[¶](https://docs.python.org/3/library/socket.html#socket.AF_CAN "Link to this definition")


socket.PF_CAN[¶](https://docs.python.org/3/library/socket.html#socket.PF_CAN "Link to this definition")


SOL_CAN_*


CAN_*

Many constants of these forms, documented in the Linux documentation, are also defined in the socket module.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.25, NetBSD >= 8.
Added in version 3.3.
Changed in version 3.11: NetBSD support was added.
Changed in version 3.14: Restored missing `CAN_RAW_ERR_FILTER` on Linux.

socket.CAN_BCM[¶](https://docs.python.org/3/library/socket.html#socket.CAN_BCM "Link to this definition")


CAN_BCM_*

CAN_BCM, in the CAN protocol family, is the broadcast manager (BCM) protocol. Broadcast manager constants, documented in the Linux documentation, are also defined in the socket module.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.25.
Note
The `CAN_BCM_CAN_FD_FRAME` flag is only available on Linux >= 4.8.
Added in version 3.4.

socket.CAN_RAW_FD_FRAMES[¶](https://docs.python.org/3/library/socket.html#socket.CAN_RAW_FD_FRAMES "Link to this definition")

Enables CAN FD support in a CAN_RAW socket. This is disabled by default. This allows your application to send both CAN and CAN FD frames; however, you must accept both CAN and CAN FD frames when reading from the socket.
This constant is documented in the Linux documentation.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 3.6.
Added in version 3.5.

socket.CAN_RAW_JOIN_FILTERS[¶](https://docs.python.org/3/library/socket.html#socket.CAN_RAW_JOIN_FILTERS "Link to this definition")

Joins the applied CAN filters such that only CAN frames that match all given CAN filters are passed to user space.
This constant is documented in the Linux documentation.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 4.1.
Added in version 3.9.

socket.CAN_ISOTP[¶](https://docs.python.org/3/library/socket.html#socket.CAN_ISOTP "Link to this definition")

CAN_ISOTP, in the CAN protocol family, is the ISO-TP (ISO 15765-2) protocol. ISO-TP constants, documented in the Linux documentation.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.25.
Added in version 3.7.

socket.CAN_J1939[¶](https://docs.python.org/3/library/socket.html#socket.CAN_J1939 "Link to this definition")

CAN_J1939, in the CAN protocol family, is the SAE J1939 protocol. J1939 constants, documented in the Linux documentation.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 5.4.
Added in version 3.9.

socket.AF_DIVERT[¶](https://docs.python.org/3/library/socket.html#socket.AF_DIVERT "Link to this definition")


socket.PF_DIVERT[¶](https://docs.python.org/3/library/socket.html#socket.PF_DIVERT "Link to this definition")

These two constants, documented in the FreeBSD divert(4) manual page, are also defined in the socket module.
[Availability](https://docs.python.org/3/library/intro.html#availability): FreeBSD >= 14.0.
Added in version 3.12.

socket.AF_PACKET[¶](https://docs.python.org/3/library/socket.html#socket.AF_PACKET "Link to this definition")


socket.PF_PACKET[¶](https://docs.python.org/3/library/socket.html#socket.PF_PACKET "Link to this definition")


PACKET_*

Many constants of these forms, documented in the Linux documentation, are also defined in the socket module.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.2.

socket.ETH_P_ALL[¶](https://docs.python.org/3/library/socket.html#socket.ETH_P_ALL "Link to this definition")

`ETH_P_ALL` can be used in the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket") constructor as _proto_ for the [`AF_PACKET`](https://docs.python.org/3/library/socket.html#socket.AF_PACKET "socket.AF_PACKET") family in order to capture every packet, regardless of protocol.
For more information, see the
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux.
Added in version 3.12.

socket.AF_RDS[¶](https://docs.python.org/3/library/socket.html#socket.AF_RDS "Link to this definition")


socket.PF_RDS[¶](https://docs.python.org/3/library/socket.html#socket.PF_RDS "Link to this definition")


socket.SOL_RDS[¶](https://docs.python.org/3/library/socket.html#socket.SOL_RDS "Link to this definition")


RDS_*

Many constants of these forms, documented in the Linux documentation, are also defined in the socket module.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.30.
Added in version 3.3.

socket.SIO_RCVALL[¶](https://docs.python.org/3/library/socket.html#socket.SIO_RCVALL "Link to this definition")


socket.SIO_KEEPALIVE_VALS[¶](https://docs.python.org/3/library/socket.html#socket.SIO_KEEPALIVE_VALS "Link to this definition")


socket.SIO_LOOPBACK_FAST_PATH[¶](https://docs.python.org/3/library/socket.html#socket.SIO_LOOPBACK_FAST_PATH "Link to this definition")


RCVALL_*

Constants for Windows’ WSAIoctl(). The constants are used as arguments to the [`ioctl()`](https://docs.python.org/3/library/socket.html#socket.socket.ioctl "socket.socket.ioctl") method of socket objects.
Changed in version 3.6: `SIO_LOOPBACK_FAST_PATH` was added.

TIPC_*

TIPC related constants, matching the ones exported by the C socket API. See the TIPC documentation for more information.

socket.AF_ALG[¶](https://docs.python.org/3/library/socket.html#socket.AF_ALG "Link to this definition")


socket.SOL_ALG[¶](https://docs.python.org/3/library/socket.html#socket.SOL_ALG "Link to this definition")


ALG_*

Constants for Linux Kernel cryptography.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.38.
Added in version 3.6.

socket.AF_VSOCK[¶](https://docs.python.org/3/library/socket.html#socket.AF_VSOCK "Link to this definition")


socket.IOCTL_VM_SOCKETS_GET_LOCAL_CID[¶](https://docs.python.org/3/library/socket.html#socket.IOCTL_VM_SOCKETS_GET_LOCAL_CID "Link to this definition")


VMADDR*


SO_VM*

Constants for Linux host/guest communication.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 4.8.
Added in version 3.7.

socket.AF_LINK[¶](https://docs.python.org/3/library/socket.html#socket.AF_LINK "Link to this definition")

[Availability](https://docs.python.org/3/library/intro.html#availability): BSD, macOS.
Added in version 3.4.

socket.has_ipv6[¶](https://docs.python.org/3/library/socket.html#socket.has_ipv6 "Link to this definition")

This constant contains a boolean value which indicates if IPv6 is supported on this platform.

socket.AF_BLUETOOTH[¶](https://docs.python.org/3/library/socket.html#socket.AF_BLUETOOTH "Link to this definition")


socket.BTPROTO_L2CAP[¶](https://docs.python.org/3/library/socket.html#socket.BTPROTO_L2CAP "Link to this definition")


socket.BTPROTO_RFCOMM[¶](https://docs.python.org/3/library/socket.html#socket.BTPROTO_RFCOMM "Link to this definition")


socket.BTPROTO_HCI[¶](https://docs.python.org/3/library/socket.html#socket.BTPROTO_HCI "Link to this definition")


socket.BTPROTO_SCO[¶](https://docs.python.org/3/library/socket.html#socket.BTPROTO_SCO "Link to this definition")

Integer constants for use with Bluetooth addresses.

socket.BDADDR_ANY[¶](https://docs.python.org/3/library/socket.html#socket.BDADDR_ANY "Link to this definition")


socket.BDADDR_LOCAL[¶](https://docs.python.org/3/library/socket.html#socket.BDADDR_LOCAL "Link to this definition")

These are string constants containing Bluetooth addresses with special meanings. For example, [`BDADDR_ANY`](https://docs.python.org/3/library/socket.html#socket.BDADDR_ANY "socket.BDADDR_ANY") can be used to indicate any address when specifying the binding socket with [`BTPROTO_RFCOMM`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_RFCOMM "socket.BTPROTO_RFCOMM").

socket.BDADDR_BREDR[¶](https://docs.python.org/3/library/socket.html#socket.BDADDR_BREDR "Link to this definition")


socket.BDADDR_LE_PUBLIC[¶](https://docs.python.org/3/library/socket.html#socket.BDADDR_LE_PUBLIC "Link to this definition")


socket.BDADDR_LE_RANDOM[¶](https://docs.python.org/3/library/socket.html#socket.BDADDR_LE_RANDOM "Link to this definition")

These constants describe the Bluetooth address type when binding or connecting a [`BTPROTO_L2CAP`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_L2CAP "socket.BTPROTO_L2CAP") socket.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux, FreeBSD
Added in version 3.14.

socket.SOL_RFCOMM[¶](https://docs.python.org/3/library/socket.html#socket.SOL_RFCOMM "Link to this definition")


socket.SOL_L2CAP[¶](https://docs.python.org/3/library/socket.html#socket.SOL_L2CAP "Link to this definition")


socket.SOL_HCI[¶](https://docs.python.org/3/library/socket.html#socket.SOL_HCI "Link to this definition")


socket.SOL_SCO[¶](https://docs.python.org/3/library/socket.html#socket.SOL_SCO "Link to this definition")


socket.SOL_BLUETOOTH[¶](https://docs.python.org/3/library/socket.html#socket.SOL_BLUETOOTH "Link to this definition")

Used in the level argument to the [`setsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.setsockopt "socket.socket.setsockopt") and [`getsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.getsockopt "socket.socket.getsockopt") methods of Bluetooth socket objects.
[`SOL_BLUETOOTH`](https://docs.python.org/3/library/socket.html#socket.SOL_BLUETOOTH "socket.SOL_BLUETOOTH") is only available on Linux. Other constants are available if the corresponding protocol is supported.

SO_L2CAP_*


socket.L2CAP_LM[¶](https://docs.python.org/3/library/socket.html#socket.L2CAP_LM "Link to this definition")


L2CAP_LM_*


SO_RFCOMM_*


RFCOMM_LM_*


SO_SCO_*


SO_BTH_*


BT_*

Used in the option name and value argument to the [`setsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.setsockopt "socket.socket.setsockopt") and [`getsockopt()`](https://docs.python.org/3/library/socket.html#socket.socket.getsockopt "socket.socket.getsockopt") methods of Bluetooth socket objects.
`BT_*` and [`L2CAP_LM`](https://docs.python.org/3/library/socket.html#socket.L2CAP_LM "socket.L2CAP_LM") are only available on Linux. `SO_BTH_*` are only available on Windows. Other constants may be available on Linux and various BSD platforms.
Added in version 3.14.

socket.HCI_FILTER[¶](https://docs.python.org/3/library/socket.html#socket.HCI_FILTER "Link to this definition")


socket.HCI_TIME_STAMP[¶](https://docs.python.org/3/library/socket.html#socket.HCI_TIME_STAMP "Link to this definition")


socket.HCI_DATA_DIR[¶](https://docs.python.org/3/library/socket.html#socket.HCI_DATA_DIR "Link to this definition")


socket.SO_HCI_EVT_FILTER[¶](https://docs.python.org/3/library/socket.html#socket.SO_HCI_EVT_FILTER "Link to this definition")


socket.SO_HCI_PKT_FILTER[¶](https://docs.python.org/3/library/socket.html#socket.SO_HCI_PKT_FILTER "Link to this definition")

Option names for use with [`BTPROTO_HCI`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_HCI "socket.BTPROTO_HCI"). Availability and format of the option values depend on platform.
Changed in version 3.14: Added `SO_HCI_EVT_FILTER` and `SO_HCI_PKT_FILTER` on NetBSD and DragonFly BSD. Added `HCI_DATA_DIR` on FreeBSD, NetBSD and DragonFly BSD.

socket.HCI_DEV_NONE[¶](https://docs.python.org/3/library/socket.html#socket.HCI_DEV_NONE "Link to this definition")

The `device_id` value used to create an HCI socket that isn’t specific to a single Bluetooth adapter.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux
Added in version 3.14.

socket.HCI_CHANNEL_RAW[¶](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_RAW "Link to this definition")


socket.HCI_CHANNEL_USER[¶](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_USER "Link to this definition")


socket.HCI_CHANNEL_MONITOR[¶](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_MONITOR "Link to this definition")


socket.HCI_CHANNEL_CONTROL[¶](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_CONTROL "Link to this definition")


socket.HCI_CHANNEL_LOGGING[¶](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_LOGGING "Link to this definition")

Possible values for `channel` field in the [`BTPROTO_HCI`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_HCI "socket.BTPROTO_HCI") address.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux
Added in version 3.14.

socket.AF_QIPCRTR[¶](https://docs.python.org/3/library/socket.html#socket.AF_QIPCRTR "Link to this definition")

Constant for Qualcomm’s IPC router protocol, used to communicate with service providing remote processors.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 4.7.

socket.SCM_CREDS2[¶](https://docs.python.org/3/library/socket.html#socket.SCM_CREDS2 "Link to this definition")


socket.LOCAL_CREDS[¶](https://docs.python.org/3/library/socket.html#socket.LOCAL_CREDS "Link to this definition")


socket.LOCAL_CREDS_PERSISTENT[¶](https://docs.python.org/3/library/socket.html#socket.LOCAL_CREDS_PERSISTENT "Link to this definition")

LOCAL_CREDS and LOCAL_CREDS_PERSISTENT can be used with SOCK_DGRAM, SOCK_STREAM sockets, equivalent to Linux/DragonFlyBSD SO_PASSCRED, while LOCAL_CREDS sends the credentials at first read, LOCAL_CREDS_PERSISTENT sends for each read, SCM_CREDS2 must be then used for the latter for the message type.
Added in version 3.11.
[Availability](https://docs.python.org/3/library/intro.html#availability): FreeBSD.

socket.SO_INCOMING_CPU[¶](https://docs.python.org/3/library/socket.html#socket.SO_INCOMING_CPU "Link to this definition")

Constant to optimize CPU locality, to be used in conjunction with `SO_REUSEPORT`.
Added in version 3.11.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 3.9

socket.SO_REUSEPORT_LB[¶](https://docs.python.org/3/library/socket.html#socket.SO_REUSEPORT_LB "Link to this definition")

> Constant to enable duplicate address and port bindings with load balancing.
Added in version 3.14.
[Availability](https://docs.python.org/3/library/intro.html#availability): FreeBSD >= 12.0

socket.AF_HYPERV[¶](https://docs.python.org/3/library/socket.html#socket.AF_HYPERV "Link to this definition")


socket.HV_PROTOCOL_RAW[¶](https://docs.python.org/3/library/socket.html#socket.HV_PROTOCOL_RAW "Link to this definition")


socket.HVSOCKET_CONNECT_TIMEOUT[¶](https://docs.python.org/3/library/socket.html#socket.HVSOCKET_CONNECT_TIMEOUT "Link to this definition")


socket.HVSOCKET_CONNECT_TIMEOUT_MAX[¶](https://docs.python.org/3/library/socket.html#socket.HVSOCKET_CONNECT_TIMEOUT_MAX "Link to this definition")


socket.HVSOCKET_CONNECTED_SUSPEND[¶](https://docs.python.org/3/library/socket.html#socket.HVSOCKET_CONNECTED_SUSPEND "Link to this definition")


socket.HVSOCKET_ADDRESS_FLAG_PASSTHRU[¶](https://docs.python.org/3/library/socket.html#socket.HVSOCKET_ADDRESS_FLAG_PASSTHRU "Link to this definition")


socket.HV_GUID_ZERO[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_ZERO "Link to this definition")


socket.HV_GUID_WILDCARD[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_WILDCARD "Link to this definition")


socket.HV_GUID_BROADCAST[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_BROADCAST "Link to this definition")


socket.HV_GUID_CHILDREN[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_CHILDREN "Link to this definition")


socket.HV_GUID_LOOPBACK[¶](https://docs.python.org/3/library/socket.html#socket.HV_GUID_LOOPBACK "Link to this definition")
