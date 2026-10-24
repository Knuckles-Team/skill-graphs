  * `serial`
  * `refresh`
  * `retry`
  * `expire`
  * `minttl`

```
{
  nsname: 'ns.example.com',
  hostmaster: 'root.example.com',
  serial: 2013101809,
  refresh: 10000,
  retry: 2400,
  expire: 604800,
  minttl: 3600
}
copy
```

####  `dnsPromises.resolveSrv(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvesrvhostname)
Added in: v10.6.0
  * `hostname`


Uses the DNS protocol to resolve service records (`SRV` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with the following properties:
  * `priority`
  * `weight`
  * `port`
  * `name`

```
{
  priority: 10,
  weight: 5,
  port: 21223,
  name: 'service.example.com'
}
copy
```

####  `dnsPromises.resolveTlsa(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvetlsahostname)
Added in: v23.9.0, v22.15.0
  * `hostname`


Uses the DNS protocol to resolve certificate associations (`TLSA` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with these properties:
  * `certUsage`
  * `selector`
  * `match`
  * `data`

```
{
  certUsage: 3,
  selector: 1,
  match: 1,
  data: [ArrayBuffer]
}
copy
```

####  `dnsPromises.resolveTxt(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvetxthostname)
Added in: v10.6.0
  * `hostname`


Uses the DNS protocol to resolve text queries (`TXT` records) for the `hostname`. On success, the `Promise` is resolved with a two-dimensional array of the text records available for `hostname` (e.g. `[ ['v=spf1 ip4:0.0.0.0 ', '~all' ] ]`). Each sub-array contains TXT chunks of one record. Depending on the use case, these could be either joined together or treated separately.
####  `dnsPromises.reverse(ip)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesreverseip)
Added in: v10.6.0
  * `ip`


Performs a reverse DNS query that resolves an IPv4 or IPv6 address to an array of host names.
On error, the `Promise` is rejected with an [`Error`](https://nodejs.org/docs/latest/api/errors.html#class-error) object, where `err.code` is one of the [DNS error codes](https://nodejs.org/docs/latest/api/dns.html#error-codes).
####  `dnsPromises.setDefaultResultOrder(order)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisessetdefaultresultorderorder)
Added in: v16.4.0, v14.18.0History Version | Changes
---|---
v22.1.0, v20.13.0 | The `ipv6first` value is supported now.
v17.0.0 | Changed default value to `verbatim`.
  * `order` `'ipv4first'`, `'ipv6first'` or `'verbatim'`.


Set the default value of `order` in [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) and [`dnsPromises.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnspromiseslookuphostname-options). The value could be:
  * `ipv4first`: sets default `order` to `ipv4first`.
  * `ipv6first`: sets default `order` to `ipv6first`.
  * `verbatim`: sets default `order` to `verbatim`.


The default is `verbatim` and [`dnsPromises.setDefaultResultOrder()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisessetdefaultresultorderorder) have higher priority than [`--dns-result-order`](https://nodejs.org/docs/latest/api/cli.html#--dns-result-orderorder). When using [worker threads](https://nodejs.org/docs/latest/api/worker_threads.html), [`dnsPromises.setDefaultResultOrder()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisessetdefaultresultorderorder) from the main thread won't affect the default dns orders in workers.
####  `dnsPromises.getDefaultResultOrder()`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesgetdefaultresultorder)
Added in: v20.1.0, v18.17.0
Get the value of `dnsOrder`.
####  `dnsPromises.setServers(servers)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisessetserversservers)
Added in: v10.6.0
  * `servers`


Sets the IP address and port of servers to be used when performing DNS resolution. The `servers` argument is an array of
```
dnsPromises.setServers([
  '8.8.8.8',
  '[2001:4860:4860::8888]',
  '8.8.8.8:1053',
  '[2001:4860:4860::8888]:1053',
]);
copy
```

An error will be thrown if an invalid address is provided.
The `dnsPromises.setServers()` method must not be called while a DNS query is in progress.
This method works much like `NOTFOUND` error, the `resolve()` method will _not_ attempt to resolve with subsequent servers provided. Fallback DNS servers will only be used if the earlier ones time out or result in some other error.
### Error codes[#](https://nodejs.org/docs/latest/api/dns.html#error-codes)
Each DNS query can return one of the following error codes:
  * `dns.NODATA`: DNS server returned an answer with no data.
  * `dns.FORMERR`: DNS server claims query was misformatted.
  * `dns.SERVFAIL`: DNS server returned general failure.
  * `dns.NOTFOUND`: Domain name not found.
  * `dns.NOTIMP`: DNS server does not implement the requested operation.
  * `dns.REFUSED`: DNS server refused query.
  * `dns.BADQUERY`: Misformatted DNS query.
  * `dns.BADNAME`: Misformatted host name.
  * `dns.BADFAMILY`: Unsupported address family.
  * `dns.BADRESP`: Misformatted DNS reply.
  * `dns.CONNREFUSED`: Could not contact DNS servers.
  * `dns.TIMEOUT`: Timeout while contacting DNS servers.
  * `dns.EOF`: End of file.
  * `dns.FILE`: Error reading file.
  * `dns.NOMEM`: Out of memory.
  * `dns.DESTRUCTION`: Channel is being destroyed.
  * `dns.BADSTR`: Misformatted string.
  * `dns.BADFLAGS`: Illegal flags specified.
  * `dns.NONAME`: Given host name is not numeric.
  * `dns.BADHINTS`: Illegal hints flags specified.
  * `dns.NOTINITIALIZED`: c-ares library initialization not yet performed.
  * `dns.LOADIPHLPAPI`: Error loading `iphlpapi.dll`.
  * `dns.ADDRGETNETWORKPARAMS`: Could not find `GetNetworkParams` function.
  * `dns.CANCELLED`: DNS query cancelled.


The `dnsPromises` API also exports the above error codes, e.g., `dnsPromises.NODATA`.
### Implementation considerations[#](https://nodejs.org/docs/latest/api/dns.html#implementation-considerations)
Although [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) and the various `dns.resolve*()/dns.reverse()` functions have the same goal of associating a network name with a network address (or vice versa), their behavior is quite different. These differences can have subtle but significant consequences on the behavior of Node.js programs.
####  `dns.lookup()`[#](https://nodejs.org/docs/latest/api/dns.html#dnslookup)
Under the hood, [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) uses the same operating system facilities as most other programs. For instance, [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) will almost always resolve a given name the same way as the `ping` command. On most POSIX-like operating systems, the behavior of the [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) function can be modified by changing settings in
Though the call to `dns.lookup()` will be asynchronous from JavaScript's perspective, it is implemented as a synchronous call to [`UV_THREADPOOL_SIZE`](https://nodejs.org/docs/latest/api/cli.html#uv_threadpool_sizesize) documentation for more information.
Various networking APIs will call `dns.lookup()` internally to resolve host names. If that is an issue, consider resolving the host name to an address using `dns.resolve()` and using the address instead of a host name. Also, some networking APIs (such as [`socket.connect()`](https://nodejs.org/docs/latest/api/net.html#socketconnectoptions-connectlistener) and [`dgram.createSocket()`](https://nodejs.org/docs/latest/api/dgram.html#dgramcreatesocketoptions-callback)) allow the default resolver, `dns.lookup()`, to be replaced.
####  `dns.resolve()`, `dns.resolve*()`, and `dns.reverse()`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolve-dnsresolve-and-dnsreverse)
These functions are implemented quite differently than [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback). They do not use _always_ perform a DNS query on the network. This network communication is always done asynchronously and does not use libuv's threadpool.
As a result, these functions cannot have the same negative impact on other processing that happens on libuv's threadpool that [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) can have.
They do not use the same set of configuration files that [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) uses. For instance, they do not use the configuration from `/etc/hosts`.
