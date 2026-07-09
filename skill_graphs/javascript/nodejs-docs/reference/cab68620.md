## DNS[#](https://nodejs.org/docs/latest/api/dns.html#dns)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:dns` module enables name resolution. For example, use it to look up IP addresses of host names.
Although named for the [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) uses the operating system facilities to perform name resolution. It may not need to perform any network communication. To perform name resolution the way other applications on the same system do, use [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback).
```
import dns from 'node:dns';

dns.lookup('example.org', (err, address, family) => {
  console.log('address: %j family: IPv%s', address, family);
});
// address: "2606:2800:21f:cb07:6820:80da:af6b:8b2c" family: IPv6
const dns = require('node:dns');

dns.lookup('example.org', (err, address, family) => {
  console.log('address: %j family: IPv%s', address, family);
});
// address: "2606:2800:21f:cb07:6820:80da:af6b:8b2c" family: IPv6
copy
```

All other functions in the `node:dns` module connect to an actual DNS server to perform name resolution. They will always use the network to perform DNS queries. These functions do not use the same set of configuration files used by [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback) (e.g. `/etc/hosts`). Use these functions to always perform DNS queries, bypassing other name-resolution facilities.
```
import dns from 'node:dns';

dns.resolve4('archive.org', (err, addresses) => {
  if (err) throw err;

  console.log(`addresses: ${JSON.stringify(addresses)}`);

  addresses.forEach((a) => {
    dns.reverse(a, (err, hostnames) => {
      if (err) {
        throw err;
      }
      console.log(`reverse for ${a}: ${JSON.stringify(hostnames)}`);
    });
  });
});
const dns = require('node:dns');

dns.resolve4('archive.org', (err, addresses) => {
  if (err) throw err;

  console.log(`addresses: ${JSON.stringify(addresses)}`);

  addresses.forEach((a) => {
    dns.reverse(a, (err, hostnames) => {
      if (err) {
        throw err;
      }
      console.log(`reverse for ${a}: ${JSON.stringify(hostnames)}`);
    });
  });
});
copy
```

See the [Implementation considerations section](https://nodejs.org/docs/latest/api/dns.html#implementation-considerations) for more information.
### Class: `dns.Resolver`[#](https://nodejs.org/docs/latest/api/dns.html#class-dnsresolver)
Added in: v8.3.0
An independent resolver for DNS requests.
Creating a new resolver uses the default server settings. Setting the servers used for a resolver using [`resolver.setServers()`](https://nodejs.org/docs/latest/api/dns.html#dnssetserversservers) does not affect other resolvers:
```
import { Resolver } from 'node:dns';
const resolver = new Resolver();
resolver.setServers(['4.4.4.4']);

// This request will use the server at 4.4.4.4, independent of global settings.
resolver.resolve4('example.org', (err, addresses) => {
  // ...
});
const { Resolver } = require('node:dns');
const resolver = new Resolver();
resolver.setServers(['4.4.4.4']);

// This request will use the server at 4.4.4.4, independent of global settings.
resolver.resolve4('example.org', (err, addresses) => {
  // ...
});
copy
```

The following methods from the `node:dns` module are available:
  * [`resolver.getServers()`](https://nodejs.org/docs/latest/api/dns.html#dnsgetservers)
  * [`resolver.resolve()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvehostname-rrtype-callback)
  * [`resolver.resolve4()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolve4hostname-options-callback)
  * [`resolver.resolve6()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolve6hostname-options-callback)
  * [`resolver.resolveAny()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolveanyhostname-callback)
  * [`resolver.resolveCaa()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvecaahostname-callback)
  * [`resolver.resolveCname()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvecnamehostname-callback)
  * [`resolver.resolveMx()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvemxhostname-callback)
  * [`resolver.resolveNaptr()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvenaptrhostname-callback)
  * [`resolver.resolveNs()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvenshostname-callback)
  * [`resolver.resolvePtr()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolveptrhostname-callback)
  * [`resolver.resolveSoa()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvesoahostname-callback)
  * [`resolver.resolveSrv()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvesrvhostname-callback)
  * [`resolver.resolveTlsa()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvetlsahostname-callback)
  * [`resolver.resolveTxt()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvetxthostname-callback)
  * [`resolver.reverse()`](https://nodejs.org/docs/latest/api/dns.html#dnsreverseip-callback)
  * [`resolver.setServers()`](https://nodejs.org/docs/latest/api/dns.html#dnssetserversservers)


####  `Resolver([options])`[#](https://nodejs.org/docs/latest/api/dns.html#resolveroptions)
Added in: v8.3.0History Version | Changes
---|---
v16.7.0, v14.18.0 | The `options` object now accepts a `tries` option.
v12.18.3 | The constructor now accepts an `options` object. The single supported option is `timeout`.
Create a new resolver.
  * `options`
    * `timeout` `-1` to use the default timeout.
    * `tries` **Default:** `4`
    * `maxTimeout` **Default:** `0`, disabled.


####  `resolver.cancel()`[#](https://nodejs.org/docs/latest/api/dns.html#resolvercancel)
Added in: v8.3.0
Cancel all outstanding DNS queries made by this resolver. The corresponding callbacks will be called with an error with code `ECANCELLED`.
####  `resolver.setLocalAddress([ipv4][, ipv6])`[#](https://nodejs.org/docs/latest/api/dns.html#resolversetlocaladdressipv4-ipv6)
Added in: v15.1.0, v14.17.0
  * `ipv4` **Default:** `'0.0.0.0'`
  * `ipv6` **Default:** `'::0'`


The resolver instance will send its requests from the specified IP address. This allows programs to specify outbound interfaces when used on multi-homed systems.
If a v4 or v6 address is not specified, it is set to the default and the operating system will choose a local address automatically.
The resolver will use the v4 local address when making requests to IPv4 DNS servers, and the v6 local address when making requests to IPv6 DNS servers. The `rrtype` of resolution requests has no impact on the local address used.
###  `dns.getServers()`[#](https://nodejs.org/docs/latest/api/dns.html#dnsgetservers)
Added in: v0.11.3
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

###  `dns.lookup(hostname[, options], callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback)
Added in: v0.1.90History Version | Changes
---|---
v22.1.0, v20.13.0 | The `verbatim` option is now deprecated in favor of the new `order` option.
v18.4.0 | For compatibility with `node:net`, when passing an option object the `family` option can be the string `'IPv4'` or the string `'IPv6'`.
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v17.0.0 | The `verbatim` options defaults to `true` now.
v8.5.0 | The `verbatim` option is supported now.
v1.2.0 | The `all` option is supported now.
  * `hostname`
  * `options`
    * `family` `4`, `6`, or `0`. For backward compatibility reasons,`'IPv4'` and `'IPv6'` are interpreted as `4` and `6` respectively. The value `0` indicates that either an IPv4 or IPv6 address is returned. If the value `0` is used with `{ all: true }` (see below), either one of or both IPv4 and IPv6 addresses are returned, depending on the system's DNS resolver. **Default:** `0`.
    * `hints` [supported `getaddrinfo` flags](https://nodejs.org/docs/latest/api/dns.html#supported-getaddrinfo-flags). Multiple flags may be passed by bitwise `OR`ing their values.
    * `all` `true`, the callback returns all resolved addresses in an array. Otherwise, returns a single address. **Default:** `false`.
    * `order` `verbatim`, the resolved addresses are return unsorted. When `ipv4first`, the resolved addresses are sorted by placing IPv4 addresses before IPv6 addresses. When `ipv6first`, the resolved addresses are sorted by placing IPv6 addresses before IPv4 addresses. **Default:** `verbatim` (addresses are not reordered). Default value is configurable using [`dns.setDefaultResultOrder()`](https://nodejs.org/docs/latest/api/dns.html#dnssetdefaultresultorderorder) or [`--dns-result-order`](https://nodejs.org/docs/latest/api/cli.html#--dns-result-orderorder).
    * `verbatim` `true`, the callback receives IPv4 and IPv6 addresses in the order the DNS resolver returned them. When `false`, IPv4 addresses are placed before IPv6 addresses. This option will be deprecated in favor of `order`. When both are specified, `order` has higher precedence. New code should only use `order`. **Default:** `true` (addresses are not reordered). Default value is configurable using [`dns.setDefaultResultOrder()`](https://nodejs.org/docs/latest/api/dns.html#dnssetdefaultresultorderorder) or [`--dns-result-order`](https://nodejs.org/docs/latest/api/cli.html#--dns-result-orderorder).
  * `callback`
    * `err`
    * `address`
    * `family` `4` or `6`, denoting the family of `address`, or `0` if the address is not an IPv4 or IPv6 address. `0` is a likely indicator of a bug in the name resolution service used by the operating system.


Resolves a host name (e.g. `'nodejs.org'`) into the first found A (IPv4) or AAAA (IPv6) record. All `option` properties are optional. If `options` is an integer, then it must be `4` or `6` – if `options` is not provided, then either IPv4 or IPv6 addresses, or both, are returned if found.
With the `all` option set to `true`, the arguments for `callback` change to `(err, addresses)`, with `addresses` being an array of objects with the properties `address` and `family`.
On error, `err` is an [`Error`](https://nodejs.org/docs/latest/api/errors.html#class-error) object, where `err.code` is the error code. Keep in mind that `err.code` will be set to `'ENOTFOUND'` not only when the host name does not exist but also when the lookup fails in other ways such as no available file descriptors.
`dns.lookup()` does not necessarily have anything to do with the DNS protocol. The implementation uses an operating system facility that can associate names with addresses and vice versa. This implementation can have subtle but important consequences on the behavior of any Node.js program. Please take some time to consult the [Implementation considerations section](https://nodejs.org/docs/latest/api/dns.html#implementation-considerations) before using `dns.lookup()`.
Example usage:
```
import dns from 'node:dns';
const options = {
  family: 6,
  hints: dns.ADDRCONFIG | dns.V4MAPPED,
};
dns.lookup('example.org', options, (err, address, family) =>
  console.log('address: %j family: IPv%s', address, family));
// address: "2606:2800:21f:cb07:6820:80da:af6b:8b2c" family: IPv6

// When options.all is true, the result will be an Array.
options.all = true;
dns.lookup('example.org', options, (err, addresses) =>
  console.log('addresses: %j', addresses));
// addresses: [{"address":"2606:2800:21f:cb07:6820:80da:af6b:8b2c","family":6}]
const dns = require('node:dns');
const options = {
  family: 6,
  hints: dns.ADDRCONFIG | dns.V4MAPPED,
};
dns.lookup('example.org', options, (err, address, family) =>
  console.log('address: %j family: IPv%s', address, family));
// address: "2606:2800:21f:cb07:6820:80da:af6b:8b2c" family: IPv6

// When options.all is true, the result will be an Array.
options.all = true;
dns.lookup('example.org', options, (err, addresses) =>
  console.log('addresses: %j', addresses));
// addresses: [{"address":"2606:2800:21f:cb07:6820:80da:af6b:8b2c","family":6}]
copy
```

If this method is invoked as its [`util.promisify()`](https://nodejs.org/docs/latest/api/util.html#utilpromisifyoriginal)ed version, and `all` is not set to `true`, it returns a `Promise` for an `Object` with `address` and `family` properties.
#### Supported getaddrinfo flags[#](https://nodejs.org/docs/latest/api/dns.html#supported-getaddrinfo-flags)
History Version | Changes
---|---
v13.13.0, v12.17.0 | Added support for the `dns.ALL` flag.
The following flags can be passed as hints to [`dns.lookup()`](https://nodejs.org/docs/latest/api/dns.html#dnslookuphostname-options-callback).
  * `dns.ADDRCONFIG`: Limits returned address types to the types of non-loopback addresses configured on the system. For example, IPv4 addresses are only returned if the current system has at least one IPv4 address configured.
  * `dns.V4MAPPED`: If the IPv6 family was specified, but no IPv6 addresses were found, then return IPv4 mapped IPv6 addresses. It is not supported on some operating systems (e.g. FreeBSD 10.1).
  * `dns.ALL`: If `dns.V4MAPPED` is specified, return resolved IPv6 addresses as well as IPv4 mapped IPv6 addresses.


###  `dns.lookupService(address, port, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnslookupserviceaddress-port-callback)
Added in: v0.11.14History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `address`
  * `port`
  * `callback`
    * `err`
    * `hostname` `example.com`
    * `service` `http`


Resolves the given `address` and `port` into a host name and service using the operating system's underlying `getnameinfo` implementation.
If `address` is not a valid IP address, a `TypeError` will be thrown. The `port` will be coerced to a number. If it is not a legal port, a `TypeError` will be thrown.
On an error, `err` is an [`Error`](https://nodejs.org/docs/latest/api/errors.html#class-error) object, where `err.code` is the error code.
```
import dns from 'node:dns';
dns.lookupService('127.0.0.1', 22, (err, hostname, service) => {
  console.log(hostname, service);
  // Prints: localhost ssh
});
const dns = require('node:dns');
dns.lookupService('127.0.0.1', 22, (err, hostname, service) => {
  console.log(hostname, service);
  // Prints: localhost ssh
});
copy
```

If this method is invoked as its [`util.promisify()`](https://nodejs.org/docs/latest/api/util.html#utilpromisifyoriginal)ed version, it returns a `Promise` for an `Object` with `hostname` and `service` properties.
###  `dns.resolve(hostname[, rrtype], callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolvehostname-rrtype-callback)
Added in: v0.1.27History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `rrtype` **Default:** `'A'`.
  * `callback`
    * `err`
    * `records`


Uses the DNS protocol to resolve a host name (e.g. `'nodejs.org'`) into an array of the resource records. The `callback` function has arguments `(err, records)`. When successful, `records` will be an array of resource records. The type and structure of individual results varies based on `rrtype`:
`rrtype` |  `records` contains | Result type | Shorthand method
---|---|---|---
`'A'` | IPv4 addresses (default) |  | [`dns.resolve4()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolve4hostname-options-callback)
`'AAAA'` | IPv6 addresses |  | [`dns.resolve6()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolve6hostname-options-callback)
`'ANY'` | any records |  | [`dns.resolveAny()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolveanyhostname-callback)
`'CAA'` | CA authorization records |  | [`dns.resolveCaa()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvecaahostname-callback)
`'CNAME'` | canonical name records |  | [`dns.resolveCname()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvecnamehostname-callback)
`'MX'` | mail exchange records |  | [`dns.resolveMx()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvemxhostname-callback)
`'NAPTR'` | name authority pointer records |  | [`dns.resolveNaptr()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvenaptrhostname-callback)
`'NS'` | name server records |  | [`dns.resolveNs()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvenshostname-callback)
`'PTR'` | pointer records |  | [`dns.resolvePtr()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolveptrhostname-callback)
`'SOA'` | start of authority records |  | [`dns.resolveSoa()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvesoahostname-callback)
`'SRV'` | service records |  | [`dns.resolveSrv()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvesrvhostname-callback)
`'TLSA'` | certificate associations |  | [`dns.resolveTlsa()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvetlsahostname-callback)
`'TXT'` | text records |  | [`dns.resolveTxt()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvetxthostname-callback)
On error, `err` is an [`Error`](https://nodejs.org/docs/latest/api/errors.html#class-error) object, where `err.code` is one of the [DNS error codes](https://nodejs.org/docs/latest/api/dns.html#error-codes).
###  `dns.resolve4(hostname[, options], callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolve4hostname-options-callback)
Added in: v0.1.16History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v7.2.0 | This method now supports passing `options`, specifically `options.ttl`.
  * `hostname`
  * `options`
    * `ttl` `true`, the callback receives an array of `{ address: '1.2.3.4', ttl: 60 }` objects rather than an array of strings, with the TTL expressed in seconds.
  * `callback`
    * `err`
    * `addresses`


Uses the DNS protocol to resolve a IPv4 addresses (`A` records) for the `hostname`. The `addresses` argument passed to the `callback` function will contain an array of IPv4 addresses (e.g. `['74.125.79.104', '74.125.79.105', '74.125.79.106']`).
###  `dns.resolve6(hostname[, options], callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolve6hostname-options-callback)
Added in: v0.1.16History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
v7.2.0 | This method now supports passing `options`, specifically `options.ttl`.
  * `hostname`
  * `options`
    * `ttl` `true`, the callback receives an array of `{ address: '0:1:2:3:4:5:6:7', ttl: 60 }` objects rather than an array of strings, with the TTL expressed in seconds.
  * `callback`
    * `err`
    * `addresses`


Uses the DNS protocol to resolve IPv6 addresses (`AAAA` records) for the `hostname`. The `addresses` argument passed to the `callback` function will contain an array of IPv6 addresses.
###  `dns.resolveAny(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolveanyhostname-callback)
History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `callback`
    * `err`
    * `ret`


Uses the DNS protocol to resolve all records (also known as `ANY` or `*` query). The `ret` argument passed to the `callback` function will be an array containing various types of records. Each object has a property `type` that indicates the type of the current record. And depending on the `type`, additional properties will be present on the object:
Type | Properties
---|---
`'A'` |  `address`/`ttl`
`'AAAA'` |  `address`/`ttl`
`'CAA'` | Refer to [`dns.resolveCaa()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvecaahostname-callback)
`'CNAME'` | `value`
`'MX'` | Refer to [`dns.resolveMx()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvemxhostname-callback)
`'NAPTR'` | Refer to [`dns.resolveNaptr()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvenaptrhostname-callback)
`'NS'` | `value`
`'PTR'` | `value`
`'SOA'` | Refer to [`dns.resolveSoa()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvesoahostname-callback)
`'SRV'` | Refer to [`dns.resolveSrv()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvesrvhostname-callback)
`'TLSA'` | Refer to [`dns.resolveTlsa()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvetlsahostname-callback)
`'TXT'` | This type of record contains an array property called `entries` which refers to [`dns.resolveTxt()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvetxthostname-callback), e.g. `{ entries: ['...'], type: 'TXT' }`
Here is an example of the `ret` object passed to the callback:
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

DNS server operators may choose not to respond to `ANY` queries. It may be better to call individual methods like [`dns.resolve4()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolve4hostname-options-callback), [`dns.resolveMx()`](https://nodejs.org/docs/latest/api/dns.html#dnsresolvemxhostname-callback), and so on. For more details, see
###  `dns.resolveCname(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolvecnamehostname-callback)
Added in: v0.3.2History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `callback`
    * `err`
    * `addresses`


Uses the DNS protocol to resolve `CNAME` records for the `hostname`. The `addresses` argument passed to the `callback` function will contain an array of canonical name records available for the `hostname` (e.g. `['bar.example.com']`).
###  `dns.resolveCaa(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolvecaahostname-callback)
Added in: v15.0.0, v14.17.0History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `callback`
    * `err`
    * `records`


Uses the DNS protocol to resolve `CAA` records for the `hostname`. The `addresses` argument passed to the `callback` function will contain an array of certification authority authorization records available for the `hostname` (e.g. `[{critical: 0, iodef: 'mailto:pki@example.com'}, {critical: 128, issue: 'pki.example.com'}]`).
###  `dns.resolveMx(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolvemxhostname-callback)
Added in: v0.1.27History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `callback`
    * `err`
    * `addresses`


Uses the DNS protocol to resolve mail exchange records (`MX` records) for the `hostname`. The `addresses` argument passed to the `callback` function will contain an array of objects containing both a `priority` and `exchange` property (e.g. `[{priority: 10, exchange: 'mx.example.com'}, ...]`).
###  `dns.resolveNaptr(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolvenaptrhostname-callback)
Added in: v0.9.12History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `callback`
    * `err`
    * `addresses`


Uses the DNS protocol to resolve regular expression-based records (`NAPTR` records) for the `hostname`. The `addresses` argument passed to the `callback` function will contain an array of objects with the following properties:
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

###  `dns.resolveNs(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolvenshostname-callback)
Added in: v0.1.90History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `callback` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `hostname`
  * `callback`
    * `err`
    * `addresses`


Uses the DNS protocol to resolve name server records (`NS` records) for the `hostname`. The `addresses` argument passed to the `callback` function will contain an array of name server records available for `hostname` (e.g. `['ns1.example.com', 'ns2.example.com']`).
###  `dns.resolvePtr(hostname, callback)`[#](https://nodejs.org/docs/latest/api/dns.html#dnsresolveptrhostname-callback)
