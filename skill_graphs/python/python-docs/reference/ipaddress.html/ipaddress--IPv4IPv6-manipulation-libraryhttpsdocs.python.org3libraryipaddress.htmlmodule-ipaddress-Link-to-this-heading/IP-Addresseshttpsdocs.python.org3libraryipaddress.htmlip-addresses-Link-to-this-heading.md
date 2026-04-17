## IP Addresses[¶](https://docs.python.org/3/library/ipaddress.html#ip-addresses "Link to this heading")
### Address objects[¶](https://docs.python.org/3/library/ipaddress.html#address-objects "Link to this heading")
The [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address") and [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address") objects share a lot of common attributes. Some attributes that are only meaningful for IPv6 addresses are also implemented by `IPv4Address` objects, in order to make it easier to write code that handles both IP versions correctly. Address objects are [hashable](https://docs.python.org/3/glossary.html#term-hashable), so they can be used as keys in dictionaries.

_class_ ipaddress.IPv4Address(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "Link to this definition")

Construct an IPv4 address. An [`AddressValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.AddressValueError "ipaddress.AddressValueError") is raised if _address_ is not a valid IPv4 address.
The following constitutes a valid IPv4 address:
  1. A string in decimal-dot notation, consisting of four decimal integers in the inclusive range 0–255, separated by dots (e.g. `192.168.0.1`). Each integer represents an octet (byte) in the address. Leading zeroes are not tolerated to prevent confusion with octal notation.
  2. An integer that fits into 32 bits.
  3. An integer packed into a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object of length 4 (most significant octet first).


Copy```
>>> ipaddress.IPv4Address('192.168.0.1')
IPv4Address('192.168.0.1')
>>> ipaddress.IPv4Address(3232235521)
IPv4Address('192.168.0.1')
>>> ipaddress.IPv4Address(b'\xC0\xA8\x00\x01')
IPv4Address('192.168.0.1')

```

Changed in version 3.8: Leading zeros are tolerated, even in ambiguous cases that look like octal notation.
Changed in version 3.9.5: Leading zeros are no longer tolerated and are treated as an error. IPv4 address strings are now parsed as strict as glibc [`inet_pton()`](https://docs.python.org/3/library/socket.html#socket.inet_pton "socket.inet_pton").

version[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.version "Link to this definition")

The appropriate version number: `4` for IPv4, `6` for IPv6.
Changed in version 3.14: Made available on the class.

max_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.max_prefixlen "Link to this definition")

The total number of bits in the address representation for this version: `32` for IPv4, `128` for IPv6.
The prefix defines the number of leading bits in an address that are compared to determine whether or not an address is part of a network.
Changed in version 3.14: Made available on the class.

compressed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.compressed "Link to this definition")


exploded[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.exploded "Link to this definition")

The string representation in dotted decimal notation. Leading zeroes are never included in the representation.
As IPv4 does not define a shorthand notation for addresses with octets set to zero, these two attributes are always the same as `str(addr)` for IPv4 addresses. Exposing these attributes makes it easier to write display code that can handle both IPv4 and IPv6 addresses.

packed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.packed "Link to this definition")

The binary representation of this address - a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object of the appropriate length (most significant octet first). This is 4 bytes for IPv4 and 16 bytes for IPv6.

reverse_pointer[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.reverse_pointer "Link to this definition")

The name of the reverse DNS PTR record for the IP address, e.g.:
Copy```
>>> ipaddress.ip_address("127.0.0.1").reverse_pointer
'1.0.0.127.in-addr.arpa'
>>> ipaddress.ip_address("2001:db8::1").reverse_pointer
'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa'

```

This is the name that could be used for performing a PTR lookup, not the resolved hostname itself.
Added in version 3.5.

is_multicast[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_multicast "Link to this definition")

`True` if the address is reserved for multicast use. See

is_private[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_private "Link to this definition")

`True` if the address is defined as not globally reachable by
  * `is_private` is `False` for the shared address space (`100.64.0.0/10`)
  * For IPv4-mapped IPv6-addresses the `is_private` value is determined by the semantics of the underlying IPv4 addresses and the following condition holds (see [`IPv6Address.ipv4_mapped`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.ipv4_mapped "ipaddress.IPv6Address.ipv4_mapped")):
Copy```
address.is_private == address.ipv4_mapped.is_private

```



`is_private` has value opposite to [`is_global`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_global "ipaddress.IPv4Address.is_global"), except for the shared address space (`100.64.0.0/10` range) where they are both `False`.
Changed in version 3.13: Fixed some false positives and false negatives.
  * `192.0.0.0/24` is considered private with the exception of `192.0.0.9/32` and `192.0.0.10/32` (previously: only the `192.0.0.0/29` sub-range was considered private).
  * `64:ff9b:1::/48` is considered private.
  * `2002::/16` is considered private.
  * There are exceptions within `2001::/23` (otherwise considered private): `2001:1::1/128`, `2001:1::2/128`, `2001:3::/32`, `2001:4:112::/48`, `2001:20::/28`, `2001:30::/28`. The exceptions are not considered private.



is_global[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_global "Link to this definition")

`True` if the address is defined as globally reachable by
For IPv4-mapped IPv6-addresses the `is_private` value is determined by the semantics of the underlying IPv4 addresses and the following condition holds (see [`IPv6Address.ipv4_mapped`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.ipv4_mapped "ipaddress.IPv6Address.ipv4_mapped")):
Copy```
address.is_global == address.ipv4_mapped.is_global

```

`is_global` has value opposite to [`is_private`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_private "ipaddress.IPv4Address.is_private"), except for the shared address space (`100.64.0.0/10` range) where they are both `False`.
Added in version 3.4.
Changed in version 3.13: Fixed some false positives and false negatives, see [`is_private`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_private "ipaddress.IPv4Address.is_private") for details.

is_unspecified[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_unspecified "Link to this definition")

`True` if the address is unspecified. See

is_reserved[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_reserved "Link to this definition")

`True` if the address is noted as reserved by the IETF. For IPv4, this is only `240.0.0.0/4`, the `Reserved` address block. For IPv6, this is all addresses `Reserved by IETF` for future use.
Note
For IPv4, `is_reserved` is not related to the address block value of the `Reserved-by-Protocol` column in
Caution
For IPv6, `fec0::/10` a former Site-Local scoped address prefix is currently excluded from that list (see [`is_site_local`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_site_local "ipaddress.IPv6Address.is_site_local") &

is_loopback[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_loopback "Link to this definition")

`True` if this is a loopback address. See

is_link_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_link_local "Link to this definition")

`True` if the address is reserved for link-local usage. See

ipv6_mapped[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.ipv6_mapped "Link to this definition")

`IPv4Address` object representing the IPv4-mapped IPv6 address. See
Added in version 3.13.

IPv4Address.__format__(_fmt_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.__format__ "Link to this definition")

Returns a string representation of the IP address, controlled by an explicit format string. _fmt_ can be one of the following: `'s'`, the default option, equivalent to [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str"), `'b'` for a zero-padded binary string, `'X'` or `'x'` for an uppercase or lowercase hexadecimal representation, or `'n'`, which is equivalent to `'b'` for IPv4 addresses and `'x'` for IPv6. For binary and hexadecimal representations, the form specifier `'#'` and the grouping option `'_'` are available. `__format__` is used by `format`, `str.format` and f-strings.
Copy```
>>> format(ipaddress.IPv4Address('192.168.0.1'))
'192.168.0.1'
>>> '{:#b}'.format(ipaddress.IPv4Address('192.168.0.1'))
'0b11000000101010000000000000000001'
>>> f'{ipaddress.IPv6Address("2001:db8::1000"):s}'
'2001:db8::1000'
>>> format(ipaddress.IPv6Address('2001:db8::1000'), '_X')
'2001_0DB8_0000_0000_0000_0000_0000_1000'
>>> '{:#_n}'.format(ipaddress.IPv6Address('2001:db8::1000'))
'0x2001_0db8_0000_0000_0000_0000_0000_1000'

```

Added in version 3.9.

_class_ ipaddress.IPv6Address(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "Link to this definition")

Construct an IPv6 address. An [`AddressValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.AddressValueError "ipaddress.AddressValueError") is raised if _address_ is not a valid IPv6 address.
The following constitutes a valid IPv6 address:
  1. A string consisting of eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons. This describes an _exploded_ (longhand) notation. The string can also be _compressed_ (shorthand notation) by various means. See `"0000:0000:0000:0000:0000:0abc:0007:0def"` can be compressed to `"::abc:7:def"`.
Optionally, the string may also have a scope zone ID, expressed with a suffix `%scope_id`. If present, the scope ID must be non-empty, and may not contain `%`. See `fe80::1234%1` might identify address `fe80::1234` on the first link of the node.
  2. An integer that fits into 128 bits.
  3. An integer packed into a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object of length 16, big-endian.


Copy```
>>> ipaddress.IPv6Address('2001:db8::1000')
IPv6Address('2001:db8::1000')
>>> ipaddress.IPv6Address('ff02::5678%1')
IPv6Address('ff02::5678%1')

```


compressed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.compressed "Link to this definition")

The short form of the address representation, with leading zeroes in groups omitted and the longest sequence of groups consisting entirely of zeroes collapsed to a single empty group.
This is also the value returned by `str(addr)` for IPv6 addresses.

exploded[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.exploded "Link to this definition")

The long form of the address representation, with all leading zeroes and groups consisting entirely of zeroes included.
For the following attributes and methods, see the corresponding documentation of the [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address") class:

packed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.packed "Link to this definition")


reverse_pointer[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.reverse_pointer "Link to this definition")


version[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.version "Link to this definition")


max_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.max_prefixlen "Link to this definition")


is_multicast[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_multicast "Link to this definition")


is_private[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_private "Link to this definition")


is_global[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_global "Link to this definition")

Added in version 3.4.

is_unspecified[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_unspecified "Link to this definition")


is_reserved[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_reserved "Link to this definition")


is_loopback[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_loopback "Link to this definition")


is_link_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_link_local "Link to this definition")


is_site_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.is_site_local "Link to this definition")

`True` if the address is reserved for site-local usage. Note that the site-local address space has been deprecated by [`is_private`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.is_private "ipaddress.IPv4Address.is_private") to test if this address is in the space of unique local addresses as defined by

ipv4_mapped[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.ipv4_mapped "Link to this definition")

For addresses that appear to be IPv4 mapped addresses (starting with `::FFFF/96`), this property will report the embedded IPv4 address. For any other address, this property will be `None`.

scope_id[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.scope_id "Link to this definition")

For scoped addresses as defined by `None`.

sixtofour[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.sixtofour "Link to this definition")

For addresses that appear to be 6to4 addresses (starting with `2002::/16`) as defined by `None`.

teredo[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.teredo "Link to this definition")

For addresses that appear to be Teredo addresses (starting with `2001::/32`) as defined by `(server, client)` IP address pair. For any other address, this property will be `None`.

IPv6Address.__format__(_fmt_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.__format__ "Link to this definition")

Refer to the corresponding method documentation in [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address").
Added in version 3.9.
### Conversion to Strings and Integers[¶](https://docs.python.org/3/library/ipaddress.html#conversion-to-strings-and-integers "Link to this heading")
To interoperate with networking interfaces such as the socket module, addresses must be converted to strings or integers. This is handled using the [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") and [`int()`](https://docs.python.org/3/library/functions.html#int "int") builtin functions:
Copy```
>>> str(ipaddress.IPv4Address('192.168.0.1'))
'192.168.0.1'
>>> int(ipaddress.IPv4Address('192.168.0.1'))
3232235521
>>> str(ipaddress.IPv6Address('::1'))
'::1'
>>> int(ipaddress.IPv6Address('::1'))
1

```

Note that IPv6 scoped addresses are converted to integers without scope zone ID.
### Operators[¶](https://docs.python.org/3/library/ipaddress.html#operators "Link to this heading")
Address objects support some operators. Unless stated otherwise, operators can only be applied between compatible objects (i.e. IPv4 with IPv4, IPv6 with IPv6).
#### Comparison operators[¶](https://docs.python.org/3/library/ipaddress.html#comparison-operators "Link to this heading")
Address objects can be compared with the usual set of comparison operators. Same IPv6 addresses with different scope zone IDs are not equal. Some examples:
Copy```
>>> IPv4Address('127.0.0.2') > IPv4Address('127.0.0.1')
True
>>> IPv4Address('127.0.0.2') == IPv4Address('127.0.0.1')
False
>>> IPv4Address('127.0.0.2') != IPv4Address('127.0.0.1')
True
>>> IPv6Address('fe80::1234') == IPv6Address('fe80::1234%1')
False
>>> IPv6Address('fe80::1234%1') != IPv6Address('fe80::1234%2')
True

```

#### Arithmetic operators[¶](https://docs.python.org/3/library/ipaddress.html#arithmetic-operators "Link to this heading")
Integers can be added to or subtracted from address objects. Some examples:
Copy```
>>> IPv4Address('127.0.0.2') + 3
IPv4Address('127.0.0.5')
>>> IPv4Address('127.0.0.2') - 3
IPv4Address('126.255.255.255')
>>> IPv4Address('255.255.255.255') + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ipaddress.AddressValueError: 4294967296 (>= 2**32) is not permitted as an IPv4 address

```

## IP Network definitions[¶](https://docs.python.org/3/library/ipaddress.html#ip-network-definitions "Link to this heading")
The [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network") and [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network") objects provide a mechanism for defining and inspecting IP network definitions. A network definition consists of a _mask_ and a _network address_ , and as such defines a range of IP addresses that equal the network address when masked (binary AND) with the mask. For example, a network definition with the mask `255.255.255.0` and the network address `192.168.1.0` consists of IP addresses in the inclusive range `192.168.1.0` to `192.168.1.255`.
### Prefix, net mask and host mask[¶](https://docs.python.org/3/library/ipaddress.html#prefix-net-mask-and-host-mask "Link to this heading")
There are several equivalent ways to specify IP network masks. A _prefix_ `/<nbits>` is a notation that denotes how many high-order bits are set in the network mask. A _net mask_ is an IP address with some number of high-order bits set. Thus the prefix `/24` is equivalent to the net mask `255.255.255.0` in IPv4, or `ffff:ff00::` in IPv6. In addition, a _host mask_ is the logical inverse of a _net mask_ , and is sometimes used (for example in Cisco access control lists) to denote a network mask. The host mask equivalent to `/24` in IPv4 is `0.0.0.255`.
### Network objects[¶](https://docs.python.org/3/library/ipaddress.html#network-objects "Link to this heading")
All attributes implemented by address objects are implemented by network objects as well. In addition, network objects implement additional attributes. All of these are common between [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network") and [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network"), so to avoid duplication they are only documented for `IPv4Network`. Network objects are [hashable](https://docs.python.org/3/glossary.html#term-hashable), so they can be used as keys in dictionaries.

_class_ ipaddress.IPv4Network(_address_ , _strict =True_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "Link to this definition")

Construct an IPv4 network definition. _address_ can be one of the following:
  1. A string consisting of an IP address and an optional mask, separated by a slash (`/`). The IP address is the network address, and the mask can be either a single number, which means it’s a _prefix_ , or a string representation of an IPv4 address. If it’s the latter, the mask is interpreted as a _net mask_ if it starts with a non-zero field, or as a _host mask_ if it starts with a zero field, with the single exception of an all-zero mask which is treated as a _net mask_. If no mask is provided, it’s considered to be `/32`.
For example, the following _address_ specifications are equivalent: `192.168.1.0/24`, `192.168.1.0/255.255.255.0` and `192.168.1.0/0.0.0.255`.
  2. An integer that fits into 32 bits. This is equivalent to a single-address network, with the network address being _address_ and the mask being `/32`.
  3. An integer packed into a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object of length 4, big-endian. The interpretation is similar to an integer _address_.
  4. A two-tuple of an address description and a netmask, where the address description is either a string, a 32-bits integer, a 4-bytes packed integer, or an existing [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address") object; and the netmask is either an integer representing the prefix length (e.g. `24`) or a string representing the prefix mask (e.g. `255.255.255.0`).


An [`AddressValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.AddressValueError "ipaddress.AddressValueError") is raised if _address_ is not a valid IPv4 address. A [`NetmaskValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.NetmaskValueError "ipaddress.NetmaskValueError") is raised if the mask is not valid for an IPv4 address.
If _strict_ is `True` and host bits are set in the supplied address, then [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. Otherwise, the host bits are masked out to determine the appropriate network address.
Unless stated otherwise, all network methods accepting other network/address objects will raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if the argument’s IP version is incompatible to `self`.
Changed in version 3.5: Added the two-tuple form for the _address_ constructor parameter.

version[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.version "Link to this definition")


max_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.max_prefixlen "Link to this definition")

Refer to the corresponding attribute documentation in [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address").

is_multicast[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_multicast "Link to this definition")


is_private[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_private "Link to this definition")


is_unspecified[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_unspecified "Link to this definition")


is_reserved[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_reserved "Link to this definition")


is_loopback[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_loopback "Link to this definition")


is_link_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.is_link_local "Link to this definition")

These attributes are true for the network as a whole if they are true for both the network address and the broadcast address.

network_address[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.network_address "Link to this definition")

The network address for the network. The network address and the prefix length together uniquely define a network.

broadcast_address[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.broadcast_address "Link to this definition")

The broadcast address for the network. Packets sent to the broadcast address should be received by every host on the network.

hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.hostmask "Link to this definition")

The host mask, as an [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address") object.

netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.netmask "Link to this definition")

The net mask, as an [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address") object.

with_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.with_prefixlen "Link to this definition")


compressed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.compressed "Link to this definition")


exploded[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.exploded "Link to this definition")

A string representation of the network, with the mask in prefix notation.
`with_prefixlen` and `compressed` are always the same as `str(network)`. `exploded` uses the exploded form the network address.

with_netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.with_netmask "Link to this definition")

A string representation of the network, with the mask in net mask notation.

with_hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.with_hostmask "Link to this definition")

A string representation of the network, with the mask in host mask notation.

num_addresses[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.num_addresses "Link to this definition")

The total number of addresses in the network.

prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.prefixlen "Link to this definition")

Length of the network prefix, in bits.

hosts()[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.hosts "Link to this definition")

Returns an iterator over the usable hosts in the network. The usable hosts are all the IP addresses that belong to the network, except the network address itself and the network broadcast address. For networks with a mask length of 31, the network address and network broadcast address are also included in the result. Networks with a mask of 32 will return a list containing the single host address.
Copy```
>>> list(ip_network('192.0.2.0/29').hosts())
[IPv4Address('192.0.2.1'), IPv4Address('192.0.2.2'),
 IPv4Address('192.0.2.3'), IPv4Address('192.0.2.4'),
 IPv4Address('192.0.2.5'), IPv4Address('192.0.2.6')]
>>> list(ip_network('192.0.2.0/31').hosts())
[IPv4Address('192.0.2.0'), IPv4Address('192.0.2.1')]
>>> list(ip_network('192.0.2.1/32').hosts())
[IPv4Address('192.0.2.1')]

```


overlaps(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.overlaps "Link to this definition")

`True` if this network is partly or wholly contained in _other_ or _other_ is wholly contained in this network.

address_exclude(_network_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.address_exclude "Link to this definition")

Computes the network definitions resulting from removing the given _network_ from this one. Returns an iterator of network objects. Raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if _network_ is not completely contained in this network.
Copy```
>>> n1 = ip_network('192.0.2.0/28')
>>> n2 = ip_network('192.0.2.1/32')
>>> list(n1.address_exclude(n2))
[IPv4Network('192.0.2.8/29'), IPv4Network('192.0.2.4/30'),
 IPv4Network('192.0.2.2/31'), IPv4Network('192.0.2.0/32')]

```


subnets(_prefixlen_diff =1_, _new_prefix =None_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.subnets "Link to this definition")

The subnets that join to make the current network definition, depending on the argument values. _prefixlen_diff_ is the amount our prefix length should be increased by. _new_prefix_ is the desired new prefix of the subnets; it must be larger than our prefix. One and only one of _prefixlen_diff_ and _new_prefix_ must be set. Returns an iterator of network objects.
Copy```
>>> list(ip_network('192.0.2.0/24').subnets())
[IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')]
>>> list(ip_network('192.0.2.0/24').subnets(prefixlen_diff=2))
[IPv4Network('192.0.2.0/26'), IPv4Network('192.0.2.64/26'),
 IPv4Network('192.0.2.128/26'), IPv4Network('192.0.2.192/26')]
>>> list(ip_network('192.0.2.0/24').subnets(new_prefix=26))
[IPv4Network('192.0.2.0/26'), IPv4Network('192.0.2.64/26'),
 IPv4Network('192.0.2.128/26'), IPv4Network('192.0.2.192/26')]
>>> list(ip_network('192.0.2.0/24').subnets(new_prefix=23))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('new prefix must be longer')
ValueError: new prefix must be longer
>>> list(ip_network('192.0.2.0/24').subnets(new_prefix=25))
[IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/25')]

```


supernet(_prefixlen_diff =1_, _new_prefix =None_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.supernet "Link to this definition")

The supernet containing this network definition, depending on the argument values. _prefixlen_diff_ is the amount our prefix length should be decreased by. _new_prefix_ is the desired new prefix of the supernet; it must be smaller than our prefix. One and only one of _prefixlen_diff_ and _new_prefix_ must be set. Returns a single network object.
Copy```
>>> ip_network('192.0.2.0/24').supernet()
IPv4Network('192.0.2.0/23')
>>> ip_network('192.0.2.0/24').supernet(prefixlen_diff=2)
IPv4Network('192.0.0.0/22')
>>> ip_network('192.0.2.0/24').supernet(new_prefix=20)
IPv4Network('192.0.0.0/20')

```


subnet_of(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.subnet_of "Link to this definition")

Return `True` if this network is a subnet of _other_.
Copy```
>>> a = ip_network('192.168.1.0/24')
>>> b = ip_network('192.168.1.128/30')
>>> b.subnet_of(a)
True

```

Added in version 3.7.

supernet_of(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.supernet_of "Link to this definition")

Return `True` if this network is a supernet of _other_.
Copy```
>>> a = ip_network('192.168.1.0/24')
>>> b = ip_network('192.168.1.128/30')
>>> a.supernet_of(b)
True

```

Added in version 3.7.

compare_networks(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.compare_networks "Link to this definition")

Compare this network to _other_. In this comparison only the network addresses are considered; host bits aren’t. Returns either `-1`, `0` or `1`.
Copy```
>>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.2/32'))
-1
>>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.0/32'))
1
>>> ip_network('192.0.2.1/32').compare_networks(ip_network('192.0.2.1/32'))
0

```

Deprecated since version 3.7: It uses the same ordering and comparison algorithm as “<”, “==”, and “>”

_class_ ipaddress.IPv6Network(_address_ , _strict =True_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "Link to this definition")

Construct an IPv6 network definition. _address_ can be one of the following:
  1. A string consisting of an IP address and an optional prefix length, separated by a slash (`/`). The IP address is the network address, and the prefix length must be a single number, the _prefix_. If no prefix length is provided, it’s considered to be `/128`.
Note that currently expanded netmasks are not supported. That means `2001:db00::0/24` is a valid argument while `2001:db00::0/ffff:ff00::` is not.
  2. An integer that fits into 128 bits. This is equivalent to a single-address network, with the network address being _address_ and the mask being `/128`.
  3. An integer packed into a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object of length 16, big-endian. The interpretation is similar to an integer _address_.
  4. A two-tuple of an address description and a netmask, where the address description is either a string, a 128-bits integer, a 16-bytes packed integer, or an existing [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address") object; and the netmask is an integer representing the prefix length.


An [`AddressValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.AddressValueError "ipaddress.AddressValueError") is raised if _address_ is not a valid IPv6 address. A [`NetmaskValueError`](https://docs.python.org/3/library/ipaddress.html#ipaddress.NetmaskValueError "ipaddress.NetmaskValueError") is raised if the mask is not valid for an IPv6 address.
If _strict_ is `True` and host bits are set in the supplied address, then [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. Otherwise, the host bits are masked out to determine the appropriate network address.
Changed in version 3.5: Added the two-tuple form for the _address_ constructor parameter.

version[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.version "Link to this definition")


max_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.max_prefixlen "Link to this definition")


is_multicast[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_multicast "Link to this definition")


is_private[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_private "Link to this definition")


is_unspecified[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_unspecified "Link to this definition")


is_reserved[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_reserved "Link to this definition")


is_loopback[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_loopback "Link to this definition")


is_link_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_link_local "Link to this definition")


network_address[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.network_address "Link to this definition")


broadcast_address[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.broadcast_address "Link to this definition")


hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.hostmask "Link to this definition")


netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.netmask "Link to this definition")


with_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.with_prefixlen "Link to this definition")


compressed[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.compressed "Link to this definition")


exploded[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.exploded "Link to this definition")


with_netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.with_netmask "Link to this definition")


with_hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.with_hostmask "Link to this definition")


num_addresses[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.num_addresses "Link to this definition")


prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.prefixlen "Link to this definition")


hosts()[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.hosts "Link to this definition")

Returns an iterator over the usable hosts in the network. The usable hosts are all the IP addresses that belong to the network, except the Subnet-Router anycast address. For networks with a mask length of 127, the Subnet-Router anycast address is also included in the result. Networks with a mask of 128 will return a list containing the single host address.

overlaps(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.overlaps "Link to this definition")


address_exclude(_network_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.address_exclude "Link to this definition")


subnets(_prefixlen_diff =1_, _new_prefix =None_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.subnets "Link to this definition")


supernet(_prefixlen_diff =1_, _new_prefix =None_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.supernet "Link to this definition")


subnet_of(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.subnet_of "Link to this definition")


supernet_of(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.supernet_of "Link to this definition")


compare_networks(_other_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.compare_networks "Link to this definition")

Refer to the corresponding attribute documentation in [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network").

is_site_local[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network.is_site_local "Link to this definition")

This attribute is true for the network as a whole if it is true for both the network address and the broadcast address.
### Operators[¶](https://docs.python.org/3/library/ipaddress.html#id1 "Link to this heading")
Network objects support some operators. Unless stated otherwise, operators can only be applied between compatible objects (i.e. IPv4 with IPv4, IPv6 with IPv6).
#### Logical operators[¶](https://docs.python.org/3/library/ipaddress.html#logical-operators "Link to this heading")
Network objects can be compared with the usual set of logical operators. Network objects are ordered first by network address, then by net mask.
#### Iteration[¶](https://docs.python.org/3/library/ipaddress.html#iteration "Link to this heading")
Network objects can be iterated to list all the addresses belonging to the network. For iteration, _all_ hosts are returned, including unusable hosts (for usable hosts, use the [`hosts()`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.hosts "ipaddress.IPv4Network.hosts") method). An example:
Copy```
>>> for addr in IPv4Network('192.0.2.0/28'):
...     addr
...
IPv4Address('192.0.2.0')
IPv4Address('192.0.2.1')
IPv4Address('192.0.2.2')
IPv4Address('192.0.2.3')
IPv4Address('192.0.2.4')
IPv4Address('192.0.2.5')
IPv4Address('192.0.2.6')
IPv4Address('192.0.2.7')
IPv4Address('192.0.2.8')
IPv4Address('192.0.2.9')
IPv4Address('192.0.2.10')
IPv4Address('192.0.2.11')
IPv4Address('192.0.2.12')
IPv4Address('192.0.2.13')
IPv4Address('192.0.2.14')
IPv4Address('192.0.2.15')

```

#### Networks as containers of addresses[¶](https://docs.python.org/3/library/ipaddress.html#networks-as-containers-of-addresses "Link to this heading")
Network objects can act as containers of addresses. Some examples:
Copy```
>>> IPv4Network('192.0.2.0/28')[0]
IPv4Address('192.0.2.0')
>>> IPv4Network('192.0.2.0/28')[15]
IPv4Address('192.0.2.15')
>>> IPv4Address('192.0.2.6') in IPv4Network('192.0.2.0/28')
True
>>> IPv4Address('192.0.3.6') in IPv4Network('192.0.2.0/28')
False

```
