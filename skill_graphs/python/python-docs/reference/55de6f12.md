## Interface objects[¶](https://docs.python.org/3/library/ipaddress.html#interface-objects "Link to this heading")
Interface objects are [hashable](https://docs.python.org/3/glossary.html#term-hashable), so they can be used as keys in dictionaries.

_class_ ipaddress.IPv4Interface(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface "Link to this definition")

Construct an IPv4 interface. The meaning of _address_ is as in the constructor of [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network"), except that arbitrary host addresses are always accepted.
`IPv4Interface` is a subclass of [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address"), so it inherits all the attributes from that class. In addition, the following attributes are available:

ip[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface.ip "Link to this definition")

The address ([`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")) without network information.
Copy```
>>> interface = IPv4Interface('192.0.2.5/24')
>>> interface.ip
IPv4Address('192.0.2.5')

```


network[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface.network "Link to this definition")

The network ([`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network")) this interface belongs to.
Copy```
>>> interface = IPv4Interface('192.0.2.5/24')
>>> interface.network
IPv4Network('192.0.2.0/24')

```


with_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface.with_prefixlen "Link to this definition")

A string representation of the interface with the mask in prefix notation.
Copy```
>>> interface = IPv4Interface('192.0.2.5/24')
>>> interface.with_prefixlen
'192.0.2.5/24'

```


with_netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface.with_netmask "Link to this definition")

A string representation of the interface with the network as a net mask.
Copy```
>>> interface = IPv4Interface('192.0.2.5/24')
>>> interface.with_netmask
'192.0.2.5/255.255.255.0'

```


with_hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface.with_hostmask "Link to this definition")

A string representation of the interface with the network as a host mask.
Copy```
>>> interface = IPv4Interface('192.0.2.5/24')
>>> interface.with_hostmask
'192.0.2.5/0.0.0.255'

```


_class_ ipaddress.IPv6Interface(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface "Link to this definition")

Construct an IPv6 interface. The meaning of _address_ is as in the constructor of [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network"), except that arbitrary host addresses are always accepted.
`IPv6Interface` is a subclass of [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address"), so it inherits all the attributes from that class. In addition, the following attributes are available:

ip[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface.ip "Link to this definition")


network[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface.network "Link to this definition")


with_prefixlen[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface.with_prefixlen "Link to this definition")


with_netmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface.with_netmask "Link to this definition")


with_hostmask[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface.with_hostmask "Link to this definition")

Refer to the corresponding attribute documentation in [`IPv4Interface`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface "ipaddress.IPv4Interface").
### Operators[¶](https://docs.python.org/3/library/ipaddress.html#id2 "Link to this heading")
Interface objects support some operators. Unless stated otherwise, operators can only be applied between compatible objects (i.e. IPv4 with IPv4, IPv6 with IPv6).
#### Logical operators[¶](https://docs.python.org/3/library/ipaddress.html#id3 "Link to this heading")
Interface objects can be compared with the usual set of logical operators.
For equality comparison (`==` and `!=`), both the IP address and network must be the same for the objects to be equal. An interface will not compare equal to any address or network object.
For ordering (`<`, `>`, etc) the rules are different. Interface and address objects with the same IP version can be compared, and the address objects will always sort before the interface objects. Two interface objects are first compared by their networks and, if those are the same, then by their IP addresses.
## Other Module Level Functions[¶](https://docs.python.org/3/library/ipaddress.html#other-module-level-functions "Link to this heading")
The module also provides the following module level functions:

ipaddress.v4_int_to_packed(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.v4_int_to_packed "Link to this definition")

Represent an address as 4 packed bytes in network (big-endian) order. _address_ is an integer representation of an IPv4 IP address. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the integer is negative or too large to be an IPv4 IP address.
Copy```
>>> ipaddress.ip_address(3221225985)
IPv4Address('192.0.2.1')
>>> ipaddress.v4_int_to_packed(3221225985)
b'\xc0\x00\x02\x01'

```


ipaddress.v6_int_to_packed(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.v6_int_to_packed "Link to this definition")

Represent an address as 16 packed bytes in network (big-endian) order. _address_ is an integer representation of an IPv6 IP address. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if the integer is negative or too large to be an IPv6 IP address.

ipaddress.summarize_address_range(_first_ , _last_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.summarize_address_range "Link to this definition")

Return an iterator of the summarized network range given the first and last IP addresses. _first_ is the first [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address") or [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address") in the range and _last_ is the last `IPv4Address` or `IPv6Address` in the range. A [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised if _first_ or _last_ are not IP addresses or are not of the same version. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if _last_ is not greater than _first_ or if _first_ address version is not 4 or 6.
Copy```
>>> [ipaddr for ipaddr in ipaddress.summarize_address_range(
...    ipaddress.IPv4Address('192.0.2.0'),
...    ipaddress.IPv4Address('192.0.2.130'))]
[IPv4Network('192.0.2.0/25'), IPv4Network('192.0.2.128/31'), IPv4Network('192.0.2.130/32')]

```


ipaddress.collapse_addresses(_addresses_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.collapse_addresses "Link to this definition")

Return an iterator of the collapsed [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network") or [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network") objects. _addresses_ is an [iterable](https://docs.python.org/3/glossary.html#term-iterable) of `IPv4Network` or `IPv6Network` objects. A [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised if _addresses_ contains mixed version objects.
Copy```
>>> [ipaddr for ipaddr in
... ipaddress.collapse_addresses([ipaddress.IPv4Network('192.0.2.0/25'),
... ipaddress.IPv4Network('192.0.2.128/25')])]
[IPv4Network('192.0.2.0/24')]

```


ipaddress.get_mixed_type_key(_obj_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.get_mixed_type_key "Link to this definition")

Return a key suitable for sorting between networks and addresses. Address and Network objects are not sortable by default; they’re fundamentally different, so the expression:
Copy```
IPv4Address('192.0.2.0') <= IPv4Network('192.0.2.0/24')

```

doesn’t make sense. There are some times however, where you may wish to have `ipaddress` sort these anyway. If you need to do this, you can use this function as the _key_ argument to [`sorted()`](https://docs.python.org/3/library/functions.html#sorted "sorted").
_obj_ is either a network or address object.
## Custom Exceptions[¶](https://docs.python.org/3/library/ipaddress.html#custom-exceptions "Link to this heading")
To support more specific error reporting from class constructors, the module defines the following exceptions:

_exception_ ipaddress.AddressValueError(_ValueError_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.AddressValueError "Link to this definition")

Any value error related to the address.

_exception_ ipaddress.NetmaskValueError(_ValueError_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.NetmaskValueError "Link to this definition")

Any value error related to the net mask.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html)
    * [Convenience factory functions](https://docs.python.org/3/library/ipaddress.html#convenience-factory-functions)
    * [IP Addresses](https://docs.python.org/3/library/ipaddress.html#ip-addresses)
      * [Address objects](https://docs.python.org/3/library/ipaddress.html#address-objects)
      * [Conversion to Strings and Integers](https://docs.python.org/3/library/ipaddress.html#conversion-to-strings-and-integers)
      * [Operators](https://docs.python.org/3/library/ipaddress.html#operators)
        * [Comparison operators](https://docs.python.org/3/library/ipaddress.html#comparison-operators)
        * [Arithmetic operators](https://docs.python.org/3/library/ipaddress.html#arithmetic-operators)
    * [IP Network definitions](https://docs.python.org/3/library/ipaddress.html#ip-network-definitions)
      * [Prefix, net mask and host mask](https://docs.python.org/3/library/ipaddress.html#prefix-net-mask-and-host-mask)
      * [Network objects](https://docs.python.org/3/library/ipaddress.html#network-objects)
      * [Operators](https://docs.python.org/3/library/ipaddress.html#id1)
        * [Logical operators](https://docs.python.org/3/library/ipaddress.html#logical-operators)
        * [Iteration](https://docs.python.org/3/library/ipaddress.html#iteration)
        * [Networks as containers of addresses](https://docs.python.org/3/library/ipaddress.html#networks-as-containers-of-addresses)
    * [Interface objects](https://docs.python.org/3/library/ipaddress.html#interface-objects)
      * [Operators](https://docs.python.org/3/library/ipaddress.html#id2)
        * [Logical operators](https://docs.python.org/3/library/ipaddress.html#id3)
    * [Other Module Level Functions](https://docs.python.org/3/library/ipaddress.html#other-module-level-functions)
    * [Custom Exceptions](https://docs.python.org/3/library/ipaddress.html#custom-exceptions)


#### Previous topic
[`xmlrpc.server` — Basic XML-RPC servers](https://docs.python.org/3/library/xmlrpc.server.html "previous chapter")
#### Next topic
[Multimedia Services](https://docs.python.org/3/library/mm.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=ipaddress+%E2%80%94+IPv4%2FIPv6+manipulation+library&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fipaddress.html&pagesource=library%2Fipaddress.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/mm.html "Multimedia Services") |
  * [previous](https://docs.python.org/3/library/xmlrpc.server.html "xmlrpc.server — Basic XML-RPC servers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`ipaddress` — IPv4/IPv6 manipulation library](https://docs.python.org/3/library/ipaddress.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
