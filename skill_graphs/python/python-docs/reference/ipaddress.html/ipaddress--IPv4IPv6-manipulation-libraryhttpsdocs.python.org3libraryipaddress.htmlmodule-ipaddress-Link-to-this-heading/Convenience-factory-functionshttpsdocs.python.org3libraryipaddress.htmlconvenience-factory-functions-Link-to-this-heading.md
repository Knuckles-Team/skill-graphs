## Convenience factory functions[¶](https://docs.python.org/3/library/ipaddress.html#convenience-factory-functions "Link to this heading")
The `ipaddress` module provides factory functions to conveniently create IP addresses, networks and interfaces:

ipaddress.ip_address(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.ip_address "Link to this definition")

Return an [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address") or [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address") object depending on the IP address passed as argument. Either IPv4 or IPv6 addresses may be supplied; integers less than `2**32` will be considered to be IPv4 by default. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if _address_ does not represent a valid IPv4 or IPv6 address.
Copy```
>>> ipaddress.ip_address('192.168.0.1')
IPv4Address('192.168.0.1')
>>> ipaddress.ip_address('2001:db8::')
IPv6Address('2001:db8::')

```


ipaddress.ip_network(_address_ , _strict =True_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.ip_network "Link to this definition")

Return an [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network") or [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network") object depending on the IP address passed as argument. _address_ is a string or integer representing the IP network. Either IPv4 or IPv6 networks may be supplied; integers less than `2**32` will be considered to be IPv4 by default. _strict_ is passed to `IPv4Network` or `IPv6Network` constructor. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if _address_ does not represent a valid IPv4 or IPv6 address, or if the network has host bits set.
Copy```
>>> ipaddress.ip_network('192.168.0.0/28')
IPv4Network('192.168.0.0/28')

```


ipaddress.ip_interface(_address_)[¶](https://docs.python.org/3/library/ipaddress.html#ipaddress.ip_interface "Link to this definition")

Return an [`IPv4Interface`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Interface "ipaddress.IPv4Interface") or [`IPv6Interface`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Interface "ipaddress.IPv6Interface") object depending on the IP address passed as argument. _address_ is a string or integer representing the IP address. Either IPv4 or IPv6 addresses may be supplied; integers less than `2**32` will be considered to be IPv4 by default. A [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if _address_ does not represent a valid IPv4 or IPv6 address.
One downside of these convenience functions is that the need to handle both IPv4 and IPv6 formats means that error messages provide minimal information on the precise error, as the functions don’t know whether the IPv4 or IPv6 format was intended. More detailed error reporting can be obtained by calling the appropriate version specific class constructors directly.
