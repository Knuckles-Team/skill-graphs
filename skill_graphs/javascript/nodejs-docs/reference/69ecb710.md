## URL[#](https://nodejs.org/docs/latest/api/url.html#url)
**Source Code:**
[Stability: 2](https://nodejs.org/docs/latest/api/documentation.html#stability-index) - Stable
The `node:url` module provides utilities for URL resolution and parsing. It can be accessed using:
```
import url from 'node:url';
const url = require('node:url');
copy
```

### URL strings and URL objects[#](https://nodejs.org/docs/latest/api/url.html#url-strings-and-url-objects)
A URL string is a structured string containing multiple meaningful components. When parsed, a URL object is returned containing properties for each of these components.
The `node:url` module provides two APIs for working with URLs: a legacy API that is Node.js specific, and a newer API that implements the same
A comparison between the WHATWG and legacy APIs is provided below. Above the URL `'https://user:pass@sub.example.com:8080/p/a/t/h?query=string#hash'`, properties of an object returned by the legacy `url.parse()` are shown. Below it are properties of a WHATWG `URL` object.
WHATWG URL's `origin` property includes `protocol` and `host`, but not `username` or `password`.
```
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                              href                                              │
├──────────┬──┬─────────────────────┬────────────────────────┬───────────────────────────┬───────┤
│ protocol │  │        auth         │          host          │           path            │ hash  │
│          │  │                     ├─────────────────┬──────┼──────────┬────────────────┤       │
│          │  │                     │    hostname     │ port │ pathname │     search     │       │
│          │  │                     │                 │      │          ├─┬──────────────┤       │
│          │  │                     │                 │      │          │ │    query     │       │
"  https:   //    user   :   pass   @ sub.example.com : 8080   /p/a/t/h  ?  query=string   #hash "
│          │  │          │          │    hostname     │ port │          │                │       │
│          │  │          │          ├─────────────────┴──────┤          │                │       │
│ protocol │  │ username │ password │          host          │          │                │       │
├──────────┴──┼──────────┴──────────┼────────────────────────┤          │                │       │
│   origin    │                     │         origin         │ pathname │     search     │ hash  │
├─────────────┴─────────────────────┴────────────────────────┴──────────┴────────────────┴───────┤
│                                              href                                              │
└────────────────────────────────────────────────────────────────────────────────────────────────┘
(All spaces in the "" line should be ignored. They are purely for formatting.)
copy
```

Parsing the URL string using the WHATWG API:
```
const myURL =
  new URL('https://user:pass@sub.example.com:8080/p/a/t/h?query=string#hash');
copy
```

Parsing the URL string using the legacy API:
```
import url from 'node:url';
const myURL =
  url.parse('https://user:pass@sub.example.com:8080/p/a/t/h?query=string#hash');
const url = require('node:url');
const myURL =
  url.parse('https://user:pass@sub.example.com:8080/p/a/t/h?query=string#hash');
copy
```

#### Constructing a URL from component parts and getting the constructed string[#](https://nodejs.org/docs/latest/api/url.html#constructing-a-url-from-component-parts-and-getting-the-constructed-string)
It is possible to construct a WHATWG URL from component parts using either the property setters or a template literal string:
```
const myURL = new URL('https://example.org');
myURL.pathname = '/a/b/c';
myURL.search = '?d=e';
myURL.hash = '#fgh';
copy
```
```
const pathname = '/a/b/c';
const search = '?d=e';
const hash = '#fgh';
const myURL = new URL(`https://example.org${pathname}${search}${hash}`);
copy
```

To get the constructed URL string, use the `href` property accessor:
```
console.log(myURL.href);
copy
```

### The WHATWG URL API[#](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api)
#### Class: `URL`[#](https://nodejs.org/docs/latest/api/url.html#class-url)
Added in: v7.0.0, v6.13.0History Version | Changes
---|---
v10.0.0 | The class is now available on the global object.
Browser-compatible `URL` class, implemented by following the WHATWG URL Standard. `URL` class is also available on the global object.
In accordance with browser conventions, all properties of `URL` objects are implemented as getters and setters on the class prototype, rather than as data properties on the object itself. Thus, unlike [legacy `urlObject`](https://nodejs.org/docs/latest/api/url.html#legacy-urlobject)s, using the `delete` keyword on any properties of `URL` objects (e.g. `delete myURL.protocol`, `delete myURL.pathname`, etc) has no effect but will still return `true`.
#####  `new URL(input[, base])`[#](https://nodejs.org/docs/latest/api/url.html#new-urlinput-base)
History Version | Changes
---|---
v20.0.0, v18.17.0 | ICU requirement is removed.
  * `input` `input` is relative, then `base` is required. If `input` is absolute, the `base` is ignored. If `input` is not a string, it is
  * `base` `input` is not absolute. If `base` is not a string, it is


Creates a new `URL` object by parsing the `input` relative to the `base`. If `base` is passed as a string, it will be parsed equivalent to `new URL(base)`.
```
const myURL = new URL('/foo', 'https://example.org/');
// https://example.org/foo
copy
```

The URL constructor is accessible as a property on the global object. It can also be imported from the built-in url module:
```
import { URL } from 'node:url';
console.log(URL === globalThis.URL); // Prints 'true'.
console.log(URL === require('node:url').URL); // Prints 'true'.
copy
```

A `TypeError` will be thrown if the `input` or `base` are not valid URLs. Note that an effort will be made to coerce the given values into strings. For instance:
```
const myURL = new URL({ toString: () => 'https://example.org/' });
// https://example.org/
copy
```

Unicode characters appearing within the host name of `input` will be automatically converted to ASCII using the
```
const myURL = new URL('https://測試');
// https://xn--g6w251d/
copy
```

In cases where it is not known in advance if `input` is an absolute URL and a `base` is provided, it is advised to validate that the `origin` of the `URL` object is what is expected.
```
let myURL = new URL('http://Example.com/', 'https://example.org/');
// http://example.com/

myURL = new URL('https://Example.com/', 'https://example.org/');
// https://example.com/

myURL = new URL('foo://Example.com/', 'https://example.org/');
// foo://Example.com/

myURL = new URL('http:Example.com/', 'https://example.org/');
// http://example.com/

myURL = new URL('https:Example.com/', 'https://example.org/');
// https://example.org/Example.com/

myURL = new URL('foo:Example.com/', 'https://example.org/');
// foo:Example.com/
copy
```

#####  `url.hash`[#](https://nodejs.org/docs/latest/api/url.html#urlhash)
  * Type:


Gets and sets the fragment portion of the URL.
```
const myURL = new URL('https://example.org/foo#bar');
console.log(myURL.hash);
// Prints #bar

myURL.hash = 'baz';
console.log(myURL.href);
// Prints https://example.org/foo#baz
copy
```

Invalid URL characters included in the value assigned to the `hash` property are [percent-encoded](https://nodejs.org/docs/latest/api/url.html#percent-encoding-in-urls). The selection of which characters to percent-encode may vary somewhat from what the [`url.parse()`](https://nodejs.org/docs/latest/api/url.html#urlparseurlstring-parsequerystring-slashesdenotehost) and [`url.format()`](https://nodejs.org/docs/latest/api/url.html#urlformaturlobject) methods would produce.
#####  `url.host`[#](https://nodejs.org/docs/latest/api/url.html#urlhost)
  * Type:


Gets and sets the host portion of the URL.
```
const myURL = new URL('https://example.org:81/foo');
console.log(myURL.host);
// Prints example.org:81

myURL.host = 'example.com:82';
console.log(myURL.href);
// Prints https://example.com:82/foo
copy
```

Invalid host values assigned to the `host` property are ignored.
#####  `url.hostname`[#](https://nodejs.org/docs/latest/api/url.html#urlhostname)
  * Type:


Gets and sets the host name portion of the URL. The key difference between `url.host` and `url.hostname` is that `url.hostname` does _not_ include the port.
```
const myURL = new URL('https://example.org:81/foo');
console.log(myURL.hostname);
// Prints example.org

// Setting the hostname does not change the port
myURL.hostname = 'example.com';
console.log(myURL.href);
// Prints https://example.com:81/foo

// Use myURL.host to change the hostname and port
myURL.host = 'example.org:82';
console.log(myURL.href);
// Prints https://example.org:82/foo
copy
```

Invalid host name values assigned to the `hostname` property are ignored.
#####  `url.href`[#](https://nodejs.org/docs/latest/api/url.html#urlhref)
  * Type:


Gets and sets the serialized URL.
```
const myURL = new URL('https://example.org/foo');
console.log(myURL.href);
// Prints https://example.org/foo

myURL.href = 'https://example.com/bar';
console.log(myURL.href);
// Prints https://example.com/bar
copy
```

Getting the value of the `href` property is equivalent to calling [`url.toString()`](https://nodejs.org/docs/latest/api/url.html#urltostring).
Setting the value of this property to a new value is equivalent to creating a new `URL` object using [`new URL(value)`](https://nodejs.org/docs/latest/api/url.html#new-urlinput-base). Each of the `URL` object's properties will be modified.
If the value assigned to the `href` property is not a valid URL, a `TypeError` will be thrown.
#####  `url.origin`[#](https://nodejs.org/docs/latest/api/url.html#urlorigin)
History Version | Changes
---|---
v15.0.0 | The scheme "gopher" is no longer special and `url.origin` now returns `'null'` for it.
  * Type:


Gets the read-only serialization of the URL's origin.
```
const myURL = new URL('https://example.org/foo/bar?baz');
console.log(myURL.origin);
// Prints https://example.org
copy
```
```
const idnURL = new URL('https://測試');
console.log(idnURL.origin);
// Prints https://xn--g6w251d

console.log(idnURL.hostname);
// Prints xn--g6w251d
copy
```

#####  `url.password`[#](https://nodejs.org/docs/latest/api/url.html#urlpassword)
  * Type:


Gets and sets the password portion of the URL.
```
const myURL = new URL('https://abc:xyz@example.com');
console.log(myURL.password);
// Prints xyz

myURL.password = '123';
console.log(myURL.href);
// Prints https://abc:123@example.com/
copy
```

Invalid URL characters included in the value assigned to the `password` property are [percent-encoded](https://nodejs.org/docs/latest/api/url.html#percent-encoding-in-urls). The selection of which characters to percent-encode may vary somewhat from what the [`url.parse()`](https://nodejs.org/docs/latest/api/url.html#urlparseurlstring-parsequerystring-slashesdenotehost) and [`url.format()`](https://nodejs.org/docs/latest/api/url.html#urlformaturlobject) methods would produce.
#####  `url.pathname`[#](https://nodejs.org/docs/latest/api/url.html#urlpathname)
  * Type:


Gets and sets the path portion of the URL.
```
const myURL = new URL('https://example.org/abc/xyz?123');
console.log(myURL.pathname);
// Prints /abc/xyz

myURL.pathname = '/abcdef';
console.log(myURL.href);
// Prints https://example.org/abcdef?123
copy
```

Invalid URL characters included in the value assigned to the `pathname` property are [percent-encoded](https://nodejs.org/docs/latest/api/url.html#percent-encoding-in-urls). The selection of which characters to percent-encode may vary somewhat from what the [`url.parse()`](https://nodejs.org/docs/latest/api/url.html#urlparseurlstring-parsequerystring-slashesdenotehost) and [`url.format()`](https://nodejs.org/docs/latest/api/url.html#urlformaturlobject) methods would produce.
#####  `url.port`[#](https://nodejs.org/docs/latest/api/url.html#urlport)
History Version | Changes
---|---
v15.0.0 | The scheme "gopher" is no longer special.
  * Type:


Gets and sets the port portion of the URL.
The port value may be a number or a string containing a number in the range `0` to `65535` (inclusive). Setting the value to the default port of the `URL` objects given `protocol` will result in the `port` value becoming the empty string (`''`).
The port value can be an empty string in which case the port depends on the protocol/scheme:
protocol | port
---|---
"ftp" | 21
"file" |
"http" | 80
"https" | 443
"ws" | 80
"wss" | 443
Upon assigning a value to the port, the value will first be converted to a string using `.toString()`.
If that string is invalid but it begins with a number, the leading number is assigned to `port`. If the number lies outside the range denoted above, it is ignored.
```
const myURL = new URL('https://example.org:8888');
console.log(myURL.port);
// Prints 8888

// Default ports are automatically transformed to the empty string
// (HTTPS protocol's default port is 443)
myURL.port = '443';
console.log(myURL.port);
// Prints the empty string
console.log(myURL.href);
// Prints https://example.org/

myURL.port = 1234;
console.log(myURL.port);
// Prints 1234
console.log(myURL.href);
// Prints https://example.org:1234/

// Completely invalid port strings are ignored
myURL.port = 'abcd';
console.log(myURL.port);
// Prints 1234

// Leading numbers are treated as a port number
myURL.port = '5678abcd';
console.log(myURL.port);
// Prints 5678

// Non-integers are truncated
myURL.port = 1234.5678;
console.log(myURL.port);
// Prints 1234

// Out-of-range numbers which are not represented in scientific notation
// will be ignored.
myURL.port = 1e10; // 10000000000, will be range-checked as described below
console.log(myURL.port);
// Prints 1234
copy
```

Numbers which contain a decimal point, such as floating-point numbers or numbers in scientific notation, are not an exception to this rule. Leading numbers up to the decimal point will be set as the URL's port, assuming they are valid:
```
myURL.port = 4.567e21;
console.log(myURL.port);
// Prints 4 (because it is the leading number in the string '4.567e21')
copy
```

#####  `url.protocol`[#](https://nodejs.org/docs/latest/api/url.html#urlprotocol)
  * Type:


Gets and sets the protocol portion of the URL.
```
const myURL = new URL('https://example.org');
console.log(myURL.protocol);
// Prints https:

myURL.protocol = 'ftp';
console.log(myURL.href);
// Prints ftp://example.org/
copy
```

Invalid URL protocol values assigned to the `protocol` property are ignored.
###### Special schemes[#](https://nodejs.org/docs/latest/api/url.html#special-schemes)
History Version | Changes
---|---
v15.0.0 | The scheme "gopher" is no longer special.
The _special_ in terms of how they are parsed and serialized. When a URL is parsed using one of these special protocols, the `url.protocol` property may be changed to another special protocol but cannot be changed to a non-special protocol, and vice versa.
For instance, changing from `http` to `https` works:
```
const u = new URL('http://example.org');
u.protocol = 'https';
console.log(u.href);
// https://example.org/
copy
```

However, changing from `http` to a hypothetical `fish` protocol does not because the new protocol is not special.
```
const u = new URL('http://example.org');
u.protocol = 'fish';
console.log(u.href);
// http://example.org/
copy
```

Likewise, changing from a non-special protocol to a special protocol is also not permitted:
```
const u = new URL('fish://example.org');
u.protocol = 'http';
console.log(u.href);
// fish://example.org
copy
```

According to the WHATWG URL Standard, special protocol schemes are `ftp`, `file`, `http`, `https`, `ws`, and `wss`.
#####  `url.search`[#](https://nodejs.org/docs/latest/api/url.html#urlsearch)
  * Type:


Gets and sets the serialized query portion of the URL.
```
const myURL = new URL('https://example.org/abc?123');
console.log(myURL.search);
// Prints ?123

myURL.search = 'abc=xyz';
console.log(myURL.href);
// Prints https://example.org/abc?abc=xyz
copy
```

Any invalid URL characters appearing in the value assigned the `search` property will be [percent-encoded](https://nodejs.org/docs/latest/api/url.html#percent-encoding-in-urls). The selection of which characters to percent-encode may vary somewhat from what the [`url.parse()`](https://nodejs.org/docs/latest/api/url.html#urlparseurlstring-parsequerystring-slashesdenotehost) and [`url.format()`](https://nodejs.org/docs/latest/api/url.html#urlformaturlobject) methods would produce.
#####  `url.searchParams`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparams)
  * Type: [`<URLSearchParams>`](https://nodejs.org/docs/latest/api/url.html#class-urlsearchparams)


Gets the [`URLSearchParams`](https://nodejs.org/docs/latest/api/url.html#class-urlsearchparams) object representing the query parameters of the URL. This property is read-only but the `URLSearchParams` object it provides can be used to mutate the URL instance; to replace the entirety of query parameters of the URL, use the [`url.search`](https://nodejs.org/docs/latest/api/url.html#urlsearch) setter. See [`URLSearchParams`](https://nodejs.org/docs/latest/api/url.html#class-urlsearchparams) documentation for details.
Use care when using `.searchParams` to modify the `URL` because, per the WHATWG specification, the `URLSearchParams` object uses different rules to determine which characters to percent-encode. For instance, the `URL` object will not percent encode the ASCII tilde (`~`) character, while `URLSearchParams` will always encode it:
```
const myURL = new URL('https://example.org/abc?foo=~bar');

console.log(myURL.search);  // prints ?foo=~bar

// Modify the URL via searchParams...
myURL.searchParams.sort();

console.log(myURL.search);  // prints ?foo=%7Ebar
copy
```

#####  `url.username`[#](https://nodejs.org/docs/latest/api/url.html#urlusername)
  * Type:


Gets and sets the username portion of the URL.
```
const myURL = new URL('https://abc:xyz@example.com');
console.log(myURL.username);
// Prints abc

myURL.username = '123';
console.log(myURL.href);
// Prints https://123:xyz@example.com/
copy
```

Any invalid URL characters appearing in the value assigned the `username` property will be [percent-encoded](https://nodejs.org/docs/latest/api/url.html#percent-encoding-in-urls). The selection of which characters to percent-encode may vary somewhat from what the [`url.parse()`](https://nodejs.org/docs/latest/api/url.html#urlparseurlstring-parsequerystring-slashesdenotehost) and [`url.format()`](https://nodejs.org/docs/latest/api/url.html#urlformaturlobject) methods would produce.
#####  `url.toString()`[#](https://nodejs.org/docs/latest/api/url.html#urltostring)
  * Returns:


The `toString()` method on the `URL` object returns the serialized URL. The value returned is equivalent to that of [`url.href`](https://nodejs.org/docs/latest/api/url.html#urlhref) and [`url.toJSON()`](https://nodejs.org/docs/latest/api/url.html#urltojson).
#####  `url.toJSON()`[#](https://nodejs.org/docs/latest/api/url.html#urltojson)
Added in: v7.7.0, v6.13.0
  * Returns:


The `toJSON()` method on the `URL` object returns the serialized URL. The value returned is equivalent to that of [`url.href`](https://nodejs.org/docs/latest/api/url.html#urlhref) and [`url.toString()`](https://nodejs.org/docs/latest/api/url.html#urltostring).
This method is automatically called when an `URL` object is serialized with
```
const myURLs = [
  new URL('https://www.example.com'),
  new URL('https://test.example.org'),
];
console.log(JSON.stringify(myURLs));
// Prints ["https://www.example.com/","https://test.example.org/"]
copy
```

#####  `URL.createObjectURL(blob)`[#](https://nodejs.org/docs/latest/api/url.html#urlcreateobjecturlblob)
Added in: v16.7.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `blob` [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob)
  * Returns:


Creates a `'blob:nodedata:...'` URL string that represents the given [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) object and can be used to retrieve the `Blob` later.
```
const {
  Blob,
  resolveObjectURL,
} = require('node:buffer');

const blob = new Blob(['hello']);
const id = URL.createObjectURL(blob);

// later...

const otherBlob = resolveObjectURL(id);
console.log(otherBlob.size);
copy
```

The data stored by the registered [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) will be retained in memory until `URL.revokeObjectURL()` is called to remove it.
`Blob` objects are registered within the current thread. If using Worker Threads, `Blob` objects registered within one Worker will not be available to other workers or the main thread.
#####  `URL.revokeObjectURL(id)`[#](https://nodejs.org/docs/latest/api/url.html#urlrevokeobjecturlid)
Added in: v16.7.0History Version | Changes
---|---
v24.0.0, v22.17.0 | Marking the API stable.
  * `id` `'blob:nodedata:...` URL string returned by a prior call to `URL.createObjectURL()`.


Removes the stored [`<Blob>`](https://nodejs.org/docs/latest/api/buffer.html#class-blob) identified by the given ID. Attempting to revoke a ID that isn't registered will silently fail.
#####  `URL.canParse(input[, base])`[#](https://nodejs.org/docs/latest/api/url.html#urlcanparseinput-base)
Added in: v19.9.0, v18.17.0
  * `input` `input` is relative, then `base` is required. If `input` is absolute, the `base` is ignored. If `input` is not a string, it is
  * `base` `input` is not absolute. If `base` is not a string, it is
  * Returns:


Checks if an `input` relative to the `base` can be parsed to a `URL`.
```
const isValid = URL.canParse('/foo', 'https://example.org/'); // true

const isNotValid = URL.canParse('/foo'); // false
copy
```

#####  `URL.parse(input[, base])`[#](https://nodejs.org/docs/latest/api/url.html#urlparseinput-base)
Added in: v22.1.0
  * `input` `input` is relative, then `base` is required. If `input` is absolute, the `base` is ignored. If `input` is not a string, it is
  * `base` `input` is not absolute. If `base` is not a string, it is
  * Returns: [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) |


Parses a string as a URL. If `base` is provided, it will be used as the base URL for the purpose of resolving non-absolute `input` URLs. Returns `null` if the parameters can't be resolved to a valid URL.
#### Class: `URLPattern`[#](https://nodejs.org/docs/latest/api/url.html#class-urlpattern)
Added in: v23.8.0
Stability: 1 - Experimental
The `URLPattern` API provides an interface to match URLs or parts of URLs against a pattern.
```
const myPattern = new URLPattern('https://nodejs.org/docs/latest/api/*.html');
console.log(myPattern.exec('https://nodejs.org/docs/latest/api/dns.html'));
// Prints:
// {
//  "hash": { "groups": {  "0": "" },  "input": "" },
//  "hostname": { "groups": {}, "input": "nodejs.org" },
//  "inputs": [
//    "https://nodejs.org/docs/latest/api/dns.html"
//  ],
//  "password": { "groups": { "0": "" }, "input": "" },
//  "pathname": { "groups": { "0": "dns" }, "input": "/docs/latest/api/dns.html" },
//  "port": { "groups": {}, "input": "" },
//  "protocol": { "groups": {}, "input": "https" },
//  "search": { "groups": { "0": "" }, "input": "" },
//  "username": { "groups": { "0": "" }, "input": "" }
// }

console.log(myPattern.test('https://nodejs.org/docs/latest/api/dns.html'));
// Prints: true
copy
```

#####  `new URLPattern()`[#](https://nodejs.org/docs/latest/api/url.html#new-urlpattern)
Instantiate a new empty `URLPattern` object.
#####  `new URLPattern(string[, baseURL][, options])`[#](https://nodejs.org/docs/latest/api/url.html#new-urlpatternstring-baseurl-options)
  * `string`
  * `baseURL`
  * `options`


Parse the `string` as a URL, and use it to instantiate a new `URLPattern` object.
If `baseURL` is not specified, it defaults to `undefined`.
An option can have `ignoreCase` boolean attribute which enables case-insensitive matching if set to true.
The constructor can throw a `TypeError` to indicate parsing failure.
