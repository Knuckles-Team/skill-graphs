## Socket families[¶](https://docs.python.org/3/library/socket.html#socket-families "Link to this heading")
Depending on the system and the build options, various socket families are supported by this module.
The address format required by a particular socket object is automatically selected based on the address family specified when the socket object was created. Socket addresses are represented as follows:
  * The address of an [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX") socket bound to a file system node is represented as a string, using the file system encoding and the `'surrogateescape'` error handler (see [**PEP 383**](https://peps.python.org/pep-0383/)). An address in Linux’s abstract namespace is returned as a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) with an initial null byte; note that sockets in this namespace can communicate with normal file system sockets, so programs intended to run on Linux may need to deal with both types of address. A string or bytes-like object can be used for either type of address when passing it as an argument.
Changed in version 3.3: Previously, [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX") socket paths were assumed to use UTF-8 encoding.
Changed in version 3.5: Writable [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) is now accepted.


  * A pair `(host, port)` is used for the [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET") address family, where _host_ is a string representing either a hostname in internet domain notation like `'daring.cwi.nl'` or an IPv4 address like `'100.50.200.5'`, and _port_ is an integer.
    * For IPv4 addresses, two special forms are accepted instead of a host address: `''` represents `INADDR_ANY`, which is used to bind to all interfaces, and the string `'<broadcast>'` represents `INADDR_BROADCAST`. This behavior is not compatible with IPv6, therefore, you may want to avoid these if you intend to support IPv6 with your Python programs.
  * For [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6") address family, a four-tuple `(host, port, flowinfo, scope_id)` is used, where _flowinfo_ and _scope_id_ represent the `sin6_flowinfo` and `sin6_scope_id` members in `struct sockaddr_in6` in C. For `socket` module methods, _flowinfo_ and _scope_id_ can be omitted just for backward compatibility. Note, however, omission of _scope_id_ can cause problems in manipulating scoped IPv6 addresses.
Changed in version 3.7: For multicast addresses (with _scope_id_ meaningful) _address_ may not contain `%scope_id` (or `zone id`) part. This information is superfluous and may be safely omitted (recommended).
  * `AF_NETLINK` sockets are represented as pairs `(pid, groups)`.
  * Linux-only support for TIPC is available using the `AF_TIPC` address family. TIPC is an open, non-IP based networked protocol designed for use in clustered computer environments. Addresses are represented by a tuple, and the fields depend on the address type. The general tuple form is `(addr_type, v1, v2, v3 [, scope])`, where:
    * _addr_type_ is one of `TIPC_ADDR_NAMESEQ`, `TIPC_ADDR_NAME`, or `TIPC_ADDR_ID`.
    * _scope_ is one of `TIPC_ZONE_SCOPE`, `TIPC_CLUSTER_SCOPE`, and `TIPC_NODE_SCOPE`.
    * If _addr_type_ is `TIPC_ADDR_NAME`, then _v1_ is the server type, _v2_ is the port identifier, and _v3_ should be 0.
If _addr_type_ is `TIPC_ADDR_NAMESEQ`, then _v1_ is the server type, _v2_ is the lower port number, and _v3_ is the upper port number.
If _addr_type_ is `TIPC_ADDR_ID`, then _v1_ is the node, _v2_ is the reference, and _v3_ should be set to 0.
  * A tuple `(interface, )` is used for the [`AF_CAN`](https://docs.python.org/3/library/socket.html#socket.AF_CAN "socket.AF_CAN") address family, where _interface_ is a string representing a network interface name like `'can0'`. The network interface name `''` can be used to receive packets from all network interfaces of this family.
    * [`CAN_ISOTP`](https://docs.python.org/3/library/socket.html#socket.CAN_ISOTP "socket.CAN_ISOTP") protocol requires a tuple `(interface, rx_addr, tx_addr)` where both additional parameters are unsigned long integer that represent a CAN identifier (standard or extended).
    * [`CAN_J1939`](https://docs.python.org/3/library/socket.html#socket.CAN_J1939 "socket.CAN_J1939") protocol requires a tuple `(interface, name, pgn, addr)` where additional parameters are 64-bit unsigned integer representing the ECU name, a 32-bit unsigned integer representing the Parameter Group Number (PGN), and an 8-bit integer representing the address.
  * A string or a tuple `(id, unit)` is used for the `SYSPROTO_CONTROL` protocol of the `PF_SYSTEM` family. The string is the name of a kernel control using a dynamically assigned ID. The tuple can be used if ID and unit number of the kernel control are known or if a registered ID is used.
Added in version 3.3.
  * [`AF_BLUETOOTH`](https://docs.python.org/3/library/socket.html#socket.AF_BLUETOOTH "socket.AF_BLUETOOTH") supports the following protocols and address formats:
    * [`BTPROTO_L2CAP`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_L2CAP "socket.BTPROTO_L2CAP") accepts a tuple `(bdaddr, psm[, cid[, bdaddr_type]])` where:
      * `bdaddr` is a string specifying the Bluetooth address.
      * `psm` is an integer specifying the Protocol/Service Multiplexer.
      * `cid` is an optional integer specifying the Channel Identifier. If not given, defaults to zero.
      * `bdaddr_type` is an optional integer specifying the address type; one of [`BDADDR_BREDR`](https://docs.python.org/3/library/socket.html#socket.BDADDR_BREDR "socket.BDADDR_BREDR") (default), [`BDADDR_LE_PUBLIC`](https://docs.python.org/3/library/socket.html#socket.BDADDR_LE_PUBLIC "socket.BDADDR_LE_PUBLIC"), [`BDADDR_LE_RANDOM`](https://docs.python.org/3/library/socket.html#socket.BDADDR_LE_RANDOM "socket.BDADDR_LE_RANDOM").
Changed in version 3.14: Added `cid` and `bdaddr_type` fields.
    * [`BTPROTO_RFCOMM`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_RFCOMM "socket.BTPROTO_RFCOMM") accepts `(bdaddr, channel)` where `bdaddr` is the Bluetooth address as a string and `channel` is an integer.
    * [`BTPROTO_HCI`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_HCI "socket.BTPROTO_HCI") accepts a format that depends on your OS.
      * On Linux it accepts an integer `device_id` or a tuple `(device_id, [channel])` where `device_id` specifies the number of the Bluetooth device, and `channel` is an optional integer specifying the HCI channel ([`HCI_CHANNEL_RAW`](https://docs.python.org/3/library/socket.html#socket.HCI_CHANNEL_RAW "socket.HCI_CHANNEL_RAW") by default).
      * On FreeBSD, NetBSD and DragonFly BSD it accepts `bdaddr` where `bdaddr` is the Bluetooth address as a string.
Changed in version 3.2: NetBSD and DragonFlyBSD support added.
Changed in version 3.13.3: FreeBSD support added.
Changed in version 3.14: Added `channel` field. `device_id` not packed in a tuple is now accepted.
    * [`BTPROTO_SCO`](https://docs.python.org/3/library/socket.html#socket.BTPROTO_SCO "socket.BTPROTO_SCO") accepts `bdaddr` where `bdaddr` is the Bluetooth address as a string or a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object. (ex. `'12:23:34:45:56:67'` or `b'12:23:34:45:56:67'`)
Changed in version 3.14: FreeBSD support added.
  * [`AF_ALG`](https://docs.python.org/3/library/socket.html#socket.AF_ALG "socket.AF_ALG") is a Linux-only socket based interface to Kernel cryptography. An algorithm socket is configured with a tuple of two to four elements `(type, name [, feat [, mask]])`, where:
    * _type_ is the algorithm type as string, e.g. `aead`, `hash`, `skcipher` or `rng`.
    * _name_ is the algorithm name and operation mode as string, e.g. `sha256`, `hmac(sha256)`, `cbc(aes)` or `drbg_nopr_ctr_aes256`.
    * _feat_ and _mask_ are unsigned 32bit integers.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.38.
Some algorithm types require more recent Kernels.
Added in version 3.6.
  * [`AF_VSOCK`](https://docs.python.org/3/library/socket.html#socket.AF_VSOCK "socket.AF_VSOCK") allows communication between virtual machines and their hosts. The sockets are represented as a `(CID, port)` tuple where the context ID or CID and port are integers.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 3.9
See
Added in version 3.7.
  * [`AF_PACKET`](https://docs.python.org/3/library/socket.html#socket.AF_PACKET "socket.AF_PACKET") is a low-level interface directly to network devices. The addresses are represented by the tuple `(ifname, proto[, pkttype[, hatype[, addr]]])` where:
    * _ifname_ - String specifying the device name.
    * _proto_ - The Ethernet protocol number. May be [`ETH_P_ALL`](https://docs.python.org/3/library/socket.html#socket.ETH_P_ALL "socket.ETH_P_ALL") to capture all protocols, one of the [ETHERTYPE_* constants](https://docs.python.org/3/library/socket.html#socket-ethernet-types) or any other Ethernet protocol number.
    * _pkttype_ - Optional integer specifying the packet type:
      * `PACKET_HOST` (the default) - Packet addressed to the local host.
      * `PACKET_BROADCAST` - Physical-layer broadcast packet.
      * `PACKET_MULTICAST` - Packet sent to a physical-layer multicast address.
      * `PACKET_OTHERHOST` - Packet to some other host that has been caught by a device driver in promiscuous mode.
      * `PACKET_OUTGOING` - Packet originating from the local host that is looped back to a packet socket.
    * _hatype_ - Optional integer specifying the ARP hardware address type.
    * _addr_ - Optional bytes-like object specifying the hardware physical address, whose interpretation depends on the device.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.2.
  * [`AF_QIPCRTR`](https://docs.python.org/3/library/socket.html#socket.AF_QIPCRTR "socket.AF_QIPCRTR") is a Linux-only socket based interface for communicating with services running on co-processors in Qualcomm platforms. The address family is represented as a `(node, port)` tuple where the _node_ and _port_ are non-negative integers.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 4.7.
Added in version 3.8.
  * `IPPROTO_UDPLITE` is a variant of UDP which allows you to specify what portion of a packet is covered with the checksum. It adds two socket options that you can change. `self.setsockopt(IPPROTO_UDPLITE, UDPLITE_SEND_CSCOV, length)` will change what portion of outgoing packets are covered by the checksum and `self.setsockopt(IPPROTO_UDPLITE, UDPLITE_RECV_CSCOV, length)` will filter out packets which cover too little of their data. In both cases `length` should be in `range(8, 2**16, 8)`.
Such a socket should be constructed with `socket(AF_INET, SOCK_DGRAM, IPPROTO_UDPLITE)` for IPv4 or `socket(AF_INET6, SOCK_DGRAM, IPPROTO_UDPLITE)` for IPv6.
[Availability](https://docs.python.org/3/library/intro.html#availability): Linux >= 2.6.20, FreeBSD >= 10.1
Added in version 3.9.
  * [`AF_HYPERV`](https://docs.python.org/3/library/socket.html#socket.AF_HYPERV "socket.AF_HYPERV") is a Windows-only socket based interface for communicating with Hyper-V hosts and guests. The address family is represented as a `(vm_id, service_id)` tuple where the `vm_id` and `service_id` are UUID strings.
The `vm_id` is the virtual machine identifier or a set of known VMID values if the target is not a specific virtual machine. Known VMID constants defined on `socket` are:
    * `HV_GUID_ZERO`
    * `HV_GUID_BROADCAST`
    * `HV_GUID_WILDCARD` - Used to bind on itself and accept connections from all partitions.
    * `HV_GUID_CHILDREN` - Used to bind on itself and accept connection from child partitions.
    * `HV_GUID_LOOPBACK` - Used as a target to itself.
    * `HV_GUID_PARENT` - When used as a bind accepts connection from the parent partition. When used as an address target it will connect to the parent partition.
The `service_id` is the service identifier of the registered service.
Added in version 3.12.


If you use a hostname in the _host_ portion of IPv4/v6 socket address, the program may show a nondeterministic behavior, as Python uses the first address returned from the DNS resolution. The socket address will be resolved differently into an actual IPv4/v6 address, depending on the results from DNS resolution and/or the host configuration. For deterministic behavior use a numeric address in _host_ portion.
All errors raise exceptions. The normal exceptions for invalid argument types and out-of-memory conditions can be raised. Errors related to socket or address semantics raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") or one of its subclasses.
Non-blocking mode is supported through [`setblocking()`](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "socket.socket.setblocking"). A generalization of this based on timeouts is supported through [`settimeout()`](https://docs.python.org/3/library/socket.html#socket.socket.settimeout "socket.socket.settimeout").
