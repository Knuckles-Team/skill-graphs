Added in: v6.0.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `callback`
    * `err`
    * `addresses`


Uses the DNS protocol to resolve pointer records (`PTR` records) for the `hostname`. The `addresses` argument passed to the `callback` function will be an array of strings containing the reply records.
###  `dns.resolveSoa(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolvesoahostname-callback)
Added in: v0.11.10History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `callback`
    * `err`
    * `address`


Uses the DNS protocol to resolve a start of authority record (`SOA` record) for the `hostname`. The `address` argument passed to the `callback` function will be an object with the following properties:
  * `nsname`
  * `hostmaster`
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

###  `dns.resolveSrv(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolvesrvhostname-callback)
Added in: v0.1.27History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `callback`
    * `err`
    * `addresses`


Uses the DNS protocol to resolve service records (`SRV` records) for the `hostname`. The `addresses` argument passed to the `callback` function will be an array of objects with the following properties:
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

###  `dns.resolveTlsa(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolvetlsahostname-callback)
Added in: v23.9.0, v22.15.0
  * `hostname`
  * `callback`
    * `err`
    * `records`


Uses the DNS protocol to resolve certificate associations (`TLSA` records) for the `hostname`. The `records` argument passed to the `callback` function is an array of objects with these properties:
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

###  `dns.resolveTxt(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolvetxthostname-callback)
Added in: v0.1.27History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `callback`
    * `err`
    * `records`


Uses the DNS protocol to resolve text queries (`TXT` records) for the `hostname`. The `records` argument passed to the `callback` function is a two-dimensional array of the text records available for `hostname` (e.g. `[ ['v=spf1 ip4:0.0.0.0 ', '~all' ] ]`). Each sub-array contains TXT chunks of one record. Depending on the use case, these could be either joined together or treated separately.
###  `dns.reverse(ip, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsreverseip-callback)
Added in: v0.1.16
  * `ip`
  * `callback`
    * `err`
    * `hostnames`


Performs a reverse DNS query that resolves an IPv4 or IPv6 address to an array of host names.
On error, `err` is an [`Error`](https://nodejs.org/docs/latest/api/errors.html#class-error) object, where `err.code` is one of the [DNS error codes](https://nodejs.org/docs/latest/api/dns.html#error-codes).
###  `dns.setDefaultResultOrder(order)`[#](https://nodejs.org/docs/latest/api/dns.html#dnssetdefaultresultorderorder)
Added in: v16.4.0, v14.18.0History Version | Changes
---|---
v22.1.0, v20.13.0 | The `ipv6first` value is supported now.
v17.0.0 | Changed default value to `verbatim`.
  * `order` `'ipv4first'`, `'ipv6first'` or `'verbatim'`.


Set the default value of `order` in [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) and [`dnsPromises.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnspromiseslookuphostname-options). The value could be:
  * `ipv4first`: sets default `order` to `ipv4first`.
  * `ipv6first`: sets default `order` to `ipv6first`.
  * `verbatim`: sets default `order` to `verbatim`.


The default is `verbatim` and [`dns.setDefaultResultOrder()`](https://nodejs.org/docs/latest/api/dns.html#dnssetdefaultresultorderorder) have higher priority than [`--dns-result-order`](https://nodejs.org/docs/latest/api/cli.html#--dns-result-orderorder). When using [worker threads](https://nodejs.org/docs/latest/api/worker_threads.html), [`dns.setDefaultResultOrder()`](https://nodejs.org/docs/latest/api/dns.html#dnssetdefaultresultorderorder) from the main thread won't affect the default dns orders in workers.
###  `dns.getDefaultResultOrder()`[#](https://nodejs.org/docs/latest/api/dns.html#dnsgetdefaultresultorder)
Added in: v20.1.0, v18.17.0History Version | Changes
---|---
v22.1.0, v20.13.0 | The `ipv6first` value is supported now.
Get the default value for `order` in [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) and [`dnsPromises.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnspromiseslookuphostname-options). The value could be:
  * `ipv4first`: for `order` defaulting to `ipv4first`.
  * `ipv6first`: for `order` defaulting to `ipv6first`.
  * `verbatim`: for `order` defaulting to `verbatim`.


###  `dns.setServers(servers)`[#](https://nodejs.org/docs/latest/api/dns.html#dnssetserversservers)
Added in: v0.11.3
  * `servers`


Sets the IP address and port of servers to be used when performing DNS resolution. The `servers` argument is an array of
```
dns.setServers([
  '8.8.8.8',
  '[2001:4860:4860::8888]',
  '8.8.8.8:1053',
  '[2001:4860:4860::8888]:1053',
]);
copy
```

An error will be thrown if an invalid address is provided.
The `dns.setServers()` method must not be called while a DNS query is in progress.
The [`dns.setServers()`](https://nodejs.org/docs/latest/api/dns.html#dnssetserversservers) method affects only [`dns.resolve()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvehostname-rrtype-callback), `dns.resolve*()` and [`dns.reverse()`](https://nodejs.org/docs/latest/api/dns.html#dnsreverseip-callback) (and specifically _not_ [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback)).
This method works much like `NOTFOUND` error, the `resolve()` method will _not_ attempt to resolve with subsequent servers provided. Fallback DNS servers will only be used if the earlier ones time out or result in some other error.
### DNS promises API[#](https://nodejs.org/docs/latest/api/dns.html#dns-promises-api)
Added in: v10.6.0History Version | Changes
---|---
v15.0.0 | Exposed as `require('dns/promises')`.
v11.14.0, v10.17.0 | This API is no longer experimental.
The `dns.promises` API provides an alternative set of asynchronous DNS methods that return `Promise` objects rather than using callbacks. The API is accessible via `require('node:dns').promises` or `require('node:dns/promises')`.
#### Class: `dnsPromises.Resolver`[#](https://nodejs.org/docs/latest/api/dns.html#class-dnspromisesresolver)
Added in: v10.6.0
An independent resolver for DNS requests.
Creating a new resolver uses the default server settings. Setting the servers used for a resolver using [`resolver.setServers()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisessetserversservers) does not affect other resolvers:
```
import { Resolver } from 'node:dns/promises';
const resolver = new Resolver();
resolver.setServers(['4.4.4.4']);

// This request will use the server at 4.4.4.4, independent of global settings.
const addresses = await resolver.resolve4('example.org');
const { Resolver } = require('node:dns').promises;
const resolver = new Resolver();
resolver.setServers(['4.4.4.4']);

// This request will use the server at 4.4.4.4, independent of global settings.
resolver.resolve4('example.org').then((addresses) => {
  // ...
});

// Alternatively, the same code can be written using async-await style.
(async function() {
  const addresses = await resolver.resolve4('example.org');
})();
copy
```

The following methods from the `dnsPromises` API are available:
  * [`resolver.getServers()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesgetservers)
  * [`resolver.resolve()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvehostname-rrtype)
  * [`resolver.resolve4()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolve4hostname-options)
  * [`resolver.resolve6()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolve6hostname-options)
  * [`resolver.resolveAny()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolveanyhostname)
  * [`resolver.resolveCaa()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvecaahostname)
  * [`resolver.resolveCname()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvecnamehostname)
  * [`resolver.resolveMx()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvemxhostname)
  * [`resolver.resolveNaptr()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvenaptrhostname)
  * [`resolver.resolveNs()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvenshostname)
  * [`resolver.resolvePtr()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolveptrhostname)
  * [`resolver.resolveSoa()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvesoahostname)
  * [`resolver.resolveSrv()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvesrvhostname)
  * [`resolver.resolveTlsa()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvetlsahostname)
  * [`resolver.resolveTxt()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvetxthostname)
  * [`resolver.reverse()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesreverseip)
  * [`resolver.setServers()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisessetserversservers)


####  `resolver.cancel()`[#](https://nodejs.org/docs/latest/api/dns.html#resolvercancel-1)
Added in: v15.3.0, v14.17.0
Cancel all outstanding DNS queries made by this resolver. The corresponding promises will be rejected with an error with the code `ECANCELLED`.
####  `dnsPromises.getServers()`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesgetservers)
Added in: v10.6.0
  * Returns:


Returns an array of IP address strings, formatted according to
```
[
  '8.8.8.8',
  '2001:4860:4860::8888',
  '8.8.8.8:1053',
  '[2001:4860:4860::8888]:1053',
]
copy
```

####  `dnsPromises.lookup(hostname[, options])`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromiseslookuphostname-options)
Added in: v10.6.0History Version | Changes
---|---
v22.1.0, v20.13.0 | The `verbatim` option is now deprecated in favor of the new `order` option.
  * `hostname`
  * `options`
    * `family` `4`, `6`, or `0`. The value `0` indicates that either an IPv4 or IPv6 address is returned. If the value `0` is used with `{ all: true }` (see below), either one of or both IPv4 and IPv6 addresses are returned, depending on the system's DNS resolver. **Default:** `0`.
    * `hints` [supported `getaddrinfo` flags](https://nodejs.org/docs/latest/api/dns.html#supported-getaddrinfo-flags). Multiple flags may be passed by bitwise `OR`ing their values.
    * `all` `true`, the `Promise` is resolved with all addresses in an array. Otherwise, returns a single address. **Default:** `false`.
    * `order` `verbatim`, the `Promise` is resolved with IPv4 and IPv6 addresses in the order the DNS resolver returned them. When `ipv4first`, IPv4 addresses are placed before IPv6 addresses. When `ipv6first`, IPv6 addresses are placed before IPv4 addresses. **Default:** `verbatim` (addresses are not reordered). Default value is configurable using [`dns.setDefaultResultOrder()`](https://nodejs.org/docs/latest/api/dns.html#dnssetdefaultresultorderorder) or [`--dns-result-order`](https://nodejs.org/docs/latest/api/cli.html#--dns-result-orderorder). New code should use `{ order: 'verbatim' }`.
    * `verbatim` `true`, the `Promise` is resolved with IPv4 and IPv6 addresses in the order the DNS resolver returned them. When `false`, IPv4 addresses are placed before IPv6 addresses. This option will be deprecated in favor of `order`. When both are specified, `order` has higher precedence. New code should only use `order`. **Default:** currently `false` (addresses are reordered) but this is expected to change in the not too distant future. Default value is configurable using [`dns.setDefaultResultOrder()`](https://nodejs.org/docs/latest/api/dns.html#dnssetdefaultresultorderorder) or [`--dns-result-order`](https://nodejs.org/docs/latest/api/cli.html#--dns-result-orderorder).


Resolves a host name (e.g. `'nodejs.org'`) into the first found A (IPv4) or AAAA (IPv6) record. All `option` properties are optional. If `options` is an integer, then it must be `4` or `6` – if `options` is not provided, then either IPv4 or IPv6 addresses, or both, are returned if found.
With the `all` option set to `true`, the `Promise` is resolved with `addresses` being an array of objects with the properties `address` and `family`.
On error, the `Promise` is rejected with an [`Error`](https://nodejs.org/docs/latest/api/errors.html#class-error) object, where `err.code` is the error code. Keep in mind that `err.code` will be set to `'ENOTFOUND'` not only when the host name does not exist but also when the lookup fails in other ways such as no available file descriptors.
[`dnsPromises.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnspromiseslookuphostname-options) does not necessarily have anything to do with the DNS protocol. The implementation uses an operating system facility that can associate names with addresses and vice versa. This implementation can have subtle but important consequences on the behavior of any Node.js program. Please take some time to consult the [Implementation considerations section](https://nodejs.org/docs/latest/api/dns.html#implementation-considerations) before using `dnsPromises.lookup()`.
Example usage:
```
import dns from 'node:dns';
const dnsPromises = dns.promises;
const options = {
  family: 6,
  hints: dns.ADDRCONFIG | dns.V4MAPPED,
};

await dnsPromises.lookup('example.org', options).then((result) => {
  console.log('address: %j family: IPv%s', result.address, result.family);
  // address: "2606:2800:21f:cb07:6820:80da:af6b:8b2c" family: IPv6
});

// When options.all is true, the result will be an Array.
options.all = true;
await dnsPromises.lookup('example.org', options).then((result) => {
  console.log('addresses: %j', result);
  // addresses: [{"address":"2606:2800:21f:cb07:6820:80da:af6b:8b2c","family":6}]
});
const dns = require('node:dns');
const dnsPromises = dns.promises;
const options = {
  family: 6,
  hints: dns.ADDRCONFIG | dns.V4MAPPED,
};

dnsPromises.lookup('example.org', options).then((result) => {
  console.log('address: %j family: IPv%s', result.address, result.family);
  // address: "2606:2800:21f:cb07:6820:80da:af6b:8b2c" family: IPv6
});

// When options.all is true, the result will be an Array.
options.all = true;
dnsPromises.lookup('example.org', options).then((result) => {
  console.log('addresses: %j', result);
  // addresses: [{"address":"2606:2800:21f:cb07:6820:80da:af6b:8b2c","family":6}]
});
copy
```

####  `dnsPromises.lookupService(address, port)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromiseslookupserviceaddress-port)
Added in: v10.6.0
  * `address`
  * `port`


Resolves the given `address` and `port` into a host name and service using the operating system's underlying `getnameinfo` implementation.
If `address` is not a valid IP address, a `TypeError` will be thrown. The `port` will be coerced to a number. If it is not a legal port, a `TypeError` will be thrown.
On error, the `Promise` is rejected with an [`Error`](https://nodejs.org/docs/latest/api/errors.html#class-error) object, where `err.code` is the error code.
```
import dnsPromises from 'node:dns/promises';
const result = await dnsPromises.lookupService('127.0.0.1', 22);

console.log(result.hostname, result.service); // Prints: localhost ssh
const dnsPromises = require('node:dns').promises;
dnsPromises.lookupService('127.0.0.1', 22).then((result) => {
  console.log(result.hostname, result.service);
  // Prints: localhost ssh
});
copy
```

####  `dnsPromises.resolve(hostname[, rrtype])`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvehostname-rrtype)
Added in: v10.6.0
  * `hostname`
  * `rrtype` **Default:** `'A'`.


Uses the DNS protocol to resolve a host name (e.g. `'nodejs.org'`) into an array of the resource records. When successful, the `Promise` is resolved with an array of resource records. The type and structure of individual results vary based on `rrtype`:
`rrtype` |  `records` contains | Result type | Shorthand method
---|---|---|---
`'A'` | IPv4 addresses (default) |  | [`dnsPromises.resolve4()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolve4hostname-options)
`'AAAA'` | IPv6 addresses |  | [`dnsPromises.resolve6()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolve6hostname-options)
`'ANY'` | any records |  | [`dnsPromises.resolveAny()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolveanyhostname)
`'CAA'` | CA authorization records |  | [`dnsPromises.resolveCaa()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvecaahostname)
`'CNAME'` | canonical name records |  | [`dnsPromises.resolveCname()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvecnamehostname)
`'MX'` | mail exchange records |  | [`dnsPromises.resolveMx()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvemxhostname)
`'NAPTR'` | name authority pointer records |  | [`dnsPromises.resolveNaptr()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvenaptrhostname)
`'NS'` | name server records |  | [`dnsPromises.resolveNs()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvenshostname)
`'PTR'` | pointer records |  | [`dnsPromises.resolvePtr()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolveptrhostname)
`'SOA'` | start of authority records |  | [`dnsPromises.resolveSoa()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvesoahostname)
`'SRV'` | service records |  | [`dnsPromises.resolveSrv()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvesrvhostname)
`'TLSA'` | certificate associations |  | [`dnsPromises.resolveTlsa()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvetlsahostname)
`'TXT'` | text records |  | [`dnsPromises.resolveTxt()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvetxthostname)
On error, the `Promise` is rejected with an [`Error`](https://nodejs.org/docs/latest/api/errors.html#class-error) object, where `err.code` is one of the [DNS error codes](https://nodejs.org/docs/latest/api/dns.html#error-codes).
####  `dnsPromises.resolve4(hostname[, options])`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolve4hostname-options)
Added in: v10.6.0
  * `hostname`
  * `options`
    * `ttl` `true`, the `Promise` is resolved with an array of `{ address: '1.2.3.4', ttl: 60 }` objects rather than an array of strings, with the TTL expressed in seconds.


Uses the DNS protocol to resolve IPv4 addresses (`A` records) for the `hostname`. On success, the `Promise` is resolved with an array of IPv4 addresses (e.g. `['74.125.79.104', '74.125.79.105', '74.125.79.106']`).
####  `dnsPromises.resolve6(hostname[, options])`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolve6hostname-options)
Added in: v10.6.0
  * `hostname`
  * `options`
    * `ttl` `true`, the `Promise` is resolved with an array of `{ address: '0:1:2:3:4:5:6:7', ttl: 60 }` objects rather than an array of strings, with the TTL expressed in seconds.


Uses the DNS protocol to resolve IPv6 addresses (`AAAA` records) for the `hostname`. On success, the `Promise` is resolved with an array of IPv6 addresses.
####  `dnsPromises.resolveAny(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolveanyhostname)
Added in: v10.6.0
  * `hostname`


Uses the DNS protocol to resolve all records (also known as `ANY` or `*` query). On success, the `Promise` is resolved with an array containing various types of records. Each object has a property `type` that indicates the type of the current record. And depending on the `type`, additional properties will be present on the object:
Type | Properties
---|---
`'A'` |  `address`/`ttl`
`'AAAA'` |  `address`/`ttl`
`'CAA'` | Refer to [`dnsPromises.resolveCaa()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvecaahostname)
`'CNAME'` | `value`
`'MX'` | Refer to [`dnsPromises.resolveMx()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvemxhostname)
`'NAPTR'` | Refer to [`dnsPromises.resolveNaptr()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvenaptrhostname)
`'NS'` | `value`
`'PTR'` | `value`
`'SOA'` | Refer to [`dnsPromises.resolveSoa()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvesoahostname)
`'SRV'` | Refer to [`dnsPromises.resolveSrv()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvesrvhostname)
`'TLSA'` | Refer to [`dnsPromises.resolveTlsa()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvetlsahostname)
`'TXT'` | This type of record contains an array property called `entries` which refers to [`dnsPromises.resolveTxt()`](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvetxthostname), e.g. `{ entries: ['...'], type: 'TXT' }`
Here is an example of the result object:
```
[ { type: 'A', address: '127.0.0.1', ttl: 299 },
  { type: 'CNAME', value: 'example.com' },
  { type: 'MX', exchange: 'alt4.aspmx.l.example.com', priority: 50 },
  { type: 'NS', value: 'ns1.example.com' },
  { type: 'TXT', entries: [ 'v=spf1 include:_spf.example.com ~all' ] },
  { type: 'SOA',
    nsname: 'ns1.example.com',
    hostmaster: 'admin.example.com',
    serial: 156696742,
    refresh: 900,
    retry: 900,
    expire: 1800,
    minttl: 60 } ]
copy
```

####  `dnsPromises.resolveCaa(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvecaahostname)
Added in: v15.0.0, v14.17.0
  * `hostname`


Uses the DNS protocol to resolve `CAA` records for the `hostname`. On success, the `Promise` is resolved with an array of objects containing available certification authority authorization records available for the `hostname` (e.g. `[{critical: 0, iodef: 'mailto:pki@example.com'},{critical: 128, issue: 'pki.example.com'}]`).
####  `dnsPromises.resolveCname(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvecnamehostname)
Added in: v10.6.0
  * `hostname`


Uses the DNS protocol to resolve `CNAME` records for the `hostname`. On success, the `Promise` is resolved with an array of canonical name records available for the `hostname` (e.g. `['bar.example.com']`).
####  `dnsPromises.resolveMx(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvemxhostname)
Added in: v10.6.0
  * `hostname`


Uses the DNS protocol to resolve mail exchange records (`MX` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects containing both a `priority` and `exchange` property (e.g. `[{priority: 10, exchange: 'mx.example.com'}, ...]`).
####  `dnsPromises.resolveNaptr(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvenaptrhostname)
Added in: v10.6.0
  * `hostname`


Uses the DNS protocol to resolve regular expression-based records (`NAPTR` records) for the `hostname`. On success, the `Promise` is resolved with an array of objects with the following properties:
  * `flags`
  * `service`
  * `regexp`
  * `replacement`
  * `order`
  * `preference`

```
{
  flags: 's',
  service: 'SIP+D2U',
  regexp: '',
  replacement: '_sip._udp.example.com',
  order: 30,
  preference: 100
}
copy
```

####  `dnsPromises.resolveNs(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvenshostname)
Added in: v10.6.0
  * `hostname`


Uses the DNS protocol to resolve name server records (`NS` records) for the `hostname`. On success, the `Promise` is resolved with an array of name server records available for `hostname` (e.g. `['ns1.example.com', 'ns2.example.com']`).
####  `dnsPromises.resolvePtr(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolveptrhostname)
Added in: v10.6.0
  * `hostname`


Uses the DNS protocol to resolve pointer records (`PTR` records) for the `hostname`. On success, the `Promise` is resolved with an array of strings containing the reply records.
####  `dnsPromises.resolveSoa(hostname)`[#](https://nodejs.org/docs/latest/api/dns.html#dnspromisesresolvesoahostname)
Added in: v10.6.0
  * `hostname`


Uses the DNS protocol to resolve a start of authority record (`SOA` record) for the `hostname`. On success, the `Promise` is resolved with an object with the following properties:
  * `nsname`
  * `hostmaster`
