#####  `new URLPattern(obj[, baseURL][, options])`[#](https://nodejs.org/docs/latest/api/url.html#new-urlpatternobj-baseurl-options)
  * `obj`
  * `baseURL`
  * `options`


Parse the `Object` as an input pattern, and use it to instantiate a new `URLPattern` object. The object members can be any of `protocol`, `username`, `password`, `hostname`, `port`, `pathname`, `search`, `hash` or `baseURL`.
If `baseURL` is not specified, it defaults to `undefined`.
An option can have `ignoreCase` boolean attribute which enables case-insensitive matching if set to true.
The constructor can throw a `TypeError` to indicate parsing failure.
#####  `urlPattern.exec(input[, baseURL])`[#](https://nodejs.org/docs/latest/api/url.html#urlpatternexecinput-baseurl)
  * `input`
  * `baseURL`


Input can be a string or an object providing the individual URL parts. The object members can be any of `protocol`, `username`, `password`, `hostname`, `port`, `pathname`, `search`, `hash` or `baseURL`.
If `baseURL` is not specified, it will default to `undefined`.
Returns an object with an `inputs` key containing the array of arguments passed into the function and keys of the URL components which contains the matched input and matched groups.
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
copy
```

#####  `urlPattern.test(input[, baseURL])`[#](https://nodejs.org/docs/latest/api/url.html#urlpatterntestinput-baseurl)
  * `input`
  * `baseURL`


Input can be a string or an object providing the individual URL parts. The object members can be any of `protocol`, `username`, `password`, `hostname`, `port`, `pathname`, `search`, `hash` or `baseURL`.
If `baseURL` is not specified, it will default to `undefined`.
Returns a boolean indicating if the input matches the current pattern.
```
const myPattern = new URLPattern('https://nodejs.org/docs/latest/api/*.html');
console.log(myPattern.test('https://nodejs.org/docs/latest/api/dns.html'));
// Prints: true
copy
```

#### Class: `URLSearchParams`[#](https://nodejs.org/docs/latest/api/url.html#class-urlsearchparams)
Added in: v7.5.0, v6.13.0History Version | Changes
---|---
v10.0.0 | The class is now available on the global object.
The `URLSearchParams` API provides read and write access to the query of a `URL`. The `URLSearchParams` class can also be used standalone with one of the four following constructors. The `URLSearchParams` class is also available on the global object.
The WHATWG `URLSearchParams` interface and the [`querystring`](https://nodejs.org/docs/latest/api/querystring.html) module have similar purpose, but the purpose of the [`querystring`](https://nodejs.org/docs/latest/api/querystring.html) module is more general, as it allows the customization of delimiter characters (`&` and `=`). On the other hand, this API is designed purely for URL query strings.
```
const myURL = new URL('https://example.org/?abc=123');
console.log(myURL.searchParams.get('abc'));
// Prints 123

myURL.searchParams.append('abc', 'xyz');
console.log(myURL.href);
// Prints https://example.org/?abc=123&abc=xyz

myURL.searchParams.delete('abc');
myURL.searchParams.set('a', 'b');
console.log(myURL.href);
// Prints https://example.org/?a=b

const newSearchParams = new URLSearchParams(myURL.searchParams);
// The above is equivalent to
// const newSearchParams = new URLSearchParams(myURL.search);

newSearchParams.append('a', 'c');
console.log(myURL.href);
// Prints https://example.org/?a=b
console.log(newSearchParams.toString());
// Prints a=b&a=c

// newSearchParams.toString() is implicitly called
myURL.search = newSearchParams;
console.log(myURL.href);
// Prints https://example.org/?a=b&a=c
newSearchParams.delete('a');
console.log(myURL.href);
// Prints https://example.org/?a=b&a=c
copy
```

#####  `new URLSearchParams()`[#](https://nodejs.org/docs/latest/api/url.html#new-urlsearchparams)
Instantiate a new empty `URLSearchParams` object.
#####  `new URLSearchParams(string)`[#](https://nodejs.org/docs/latest/api/url.html#new-urlsearchparamsstring)
  * `string`


Parse the `string` as a query string, and use it to instantiate a new `URLSearchParams` object. A leading `'?'`, if present, is ignored.
```
let params;

params = new URLSearchParams('user=abc&query=xyz');
console.log(params.get('user'));
// Prints 'abc'
console.log(params.toString());
// Prints 'user=abc&query=xyz'

params = new URLSearchParams('?user=abc&query=xyz');
console.log(params.toString());
// Prints 'user=abc&query=xyz'
copy
```

#####  `new URLSearchParams(obj)`[#](https://nodejs.org/docs/latest/api/url.html#new-urlsearchparamsobj)
Added in: v7.10.0, v6.13.0
  * `obj`


Instantiate a new `URLSearchParams` object with a query hash map. The key and value of each property of `obj` are always coerced to strings.
Unlike [`querystring`](https://nodejs.org/docs/latest/api/querystring.html) module, duplicate keys in the form of array values are not allowed. Arrays are stringified using
```
const params = new URLSearchParams({
  user: 'abc',
  query: ['first', 'second'],
});
console.log(params.getAll('query'));
// Prints [ 'first,second' ]
console.log(params.toString());
// Prints 'user=abc&query=first%2Csecond'
copy
```

#####  `new URLSearchParams(iterable)`[#](https://nodejs.org/docs/latest/api/url.html#new-urlsearchparamsiterable)
Added in: v7.10.0, v6.13.0
  * `iterable`


Instantiate a new `URLSearchParams` object with an iterable map in a way that is similar to `iterable` can be an `Array` or any iterable object. That means `iterable` can be another `URLSearchParams`, in which case the constructor will simply create a clone of the provided `URLSearchParams`. Elements of `iterable` are key-value pairs, and can themselves be any iterable object.
Duplicate keys are allowed.
```
let params;

// Using an array
params = new URLSearchParams([
  ['user', 'abc'],
  ['query', 'first'],
  ['query', 'second'],
]);
console.log(params.toString());
// Prints 'user=abc&query=first&query=second'

// Using a Map object
const map = new Map();
map.set('user', 'abc');
map.set('query', 'xyz');
params = new URLSearchParams(map);
console.log(params.toString());
// Prints 'user=abc&query=xyz'

// Using a generator function
function* getQueryPairs() {
  yield ['user', 'abc'];
  yield ['query', 'first'];
  yield ['query', 'second'];
}
params = new URLSearchParams(getQueryPairs());
console.log(params.toString());
// Prints 'user=abc&query=first&query=second'

// Each key-value pair must have exactly two elements
new URLSearchParams([
  ['user', 'abc', 'error'],
]);
// Throws TypeError [ERR_INVALID_TUPLE]:
//        Each query pair must be an iterable [name, value] tuple
copy
```

#####  `urlSearchParams.append(name, value)`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamsappendname-value)
  * `name`
  * `value`


Append a new name-value pair to the query string.
#####  `urlSearchParams.delete(name[, value])`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamsdeletename-value)
History Version | Changes
---|---
v20.2.0, v18.18.0 | Add support for optional `value` argument.
  * `name`
  * `value`


If `value` is provided, removes all name-value pairs where name is `name` and value is `value`..
If `value` is not provided, removes all name-value pairs whose name is `name`.
#####  `urlSearchParams.entries()`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamsentries)
  * Returns:


Returns an ES6 `Iterator` over each of the name-value pairs in the query. Each item of the iterator is a JavaScript `Array`. The first item of the `Array` is the `name`, the second item of the `Array` is the `value`.
Alias for [`urlSearchParams[Symbol.iterator]()`](https://nodejs.org/docs/latest/api/url.html#urlsearchparamssymboliterator).
#####  `urlSearchParams.forEach(fn[, thisArg])`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamsforeachfn-thisarg)
History Version | Changes
---|---
v18.0.0 | Passing an invalid callback to the `fn` argument now throws `ERR_INVALID_ARG_TYPE` instead of `ERR_INVALID_CALLBACK`.
  * `fn`
  * `thisArg` `this` value for when `fn` is called


Iterates over each name-value pair in the query and invokes the given function.
```
const myURL = new URL('https://example.org/?a=b&c=d');
myURL.searchParams.forEach((value, name, searchParams) => {
  console.log(name, value, myURL.searchParams === searchParams);
});
// Prints:
//   a b true
//   c d true
copy
```

#####  `urlSearchParams.get(name)`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamsgetname)
  * `name`
  * Returns: `null` if there is no name-value pair with the given `name`.


Returns the value of the first name-value pair whose name is `name`. If there are no such pairs, `null` is returned.
#####  `urlSearchParams.getAll(name)`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamsgetallname)
  * `name`
  * Returns:


Returns the values of all name-value pairs whose name is `name`. If there are no such pairs, an empty array is returned.
#####  `urlSearchParams.has(name[, value])`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamshasname-value)
History Version | Changes
---|---
v20.2.0, v18.18.0 | Add support for optional `value` argument.
  * `name`
  * `value`
  * Returns:


Checks if the `URLSearchParams` object contains key-value pair(s) based on `name` and an optional `value` argument.
If `value` is provided, returns `true` when name-value pair with same `name` and `value` exists.
If `value` is not provided, returns `true` if there is at least one name-value pair whose name is `name`.
#####  `urlSearchParams.keys()`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamskeys)
  * Returns:


Returns an ES6 `Iterator` over the names of each name-value pair.
```
const params = new URLSearchParams('foo=bar&foo=baz');
for (const name of params.keys()) {
  console.log(name);
}
// Prints:
//   foo
//   foo
copy
```

#####  `urlSearchParams.set(name, value)`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamssetname-value)
  * `name`
  * `value`


Sets the value in the `URLSearchParams` object associated with `name` to `value`. If there are any pre-existing name-value pairs whose names are `name`, set the first such pair's value to `value` and remove all others. If not, append the name-value pair to the query string.
```
const params = new URLSearchParams();
params.append('foo', 'bar');
params.append('foo', 'baz');
params.append('abc', 'def');
console.log(params.toString());
// Prints foo=bar&foo=baz&abc=def

params.set('foo', 'def');
params.set('xyz', 'opq');
console.log(params.toString());
// Prints foo=def&abc=def&xyz=opq
copy
```

#####  `urlSearchParams.size`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamssize)
Added in: v19.8.0, v18.16.0
The total number of parameter entries.
#####  `urlSearchParams.sort()`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamssort)
Added in: v7.7.0, v6.13.0
Sort all existing name-value pairs in-place by their names. Sorting is done with a
This method can be used, in particular, to increase cache hits.
```
const params = new URLSearchParams('query[]=abc&type=search&query[]=123');
params.sort();
console.log(params.toString());
// Prints query%5B%5D=abc&query%5B%5D=123&type=search
copy
```

#####  `urlSearchParams.toString()`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamstostring)
  * Returns:


Returns the search parameters serialized as a string, with characters percent-encoded where necessary.
#####  `urlSearchParams.values()`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamsvalues)
  * Returns:


Returns an ES6 `Iterator` over the values of each name-value pair.
#####  `urlSearchParams[Symbol.iterator]()`[#](https://nodejs.org/docs/latest/api/url.html#urlsearchparamssymboliterator)
  * Returns:


Returns an ES6 `Iterator` over each of the name-value pairs in the query string. Each item of the iterator is a JavaScript `Array`. The first item of the `Array` is the `name`, the second item of the `Array` is the `value`.
Alias for [`urlSearchParams.entries()`](https://nodejs.org/docs/latest/api/url.html#urlsearchparamsentries).
```
const params = new URLSearchParams('foo=bar&xyz=baz');
for (const [name, value] of params) {
  console.log(name, value);
}
// Prints:
//   foo bar
//   xyz baz
copy
```

####  `url.domainToASCII(domain)`[#](https://nodejs.org/docs/latest/api/url.html#urldomaintoasciidomain)
Added in: v7.4.0, v6.13.0History Version | Changes
---|---
v20.0.0, v18.17.0 | ICU requirement is removed.
  * `domain`
  * Returns:


Returns the `domain`. If `domain` is an invalid domain, the empty string is returned.
It performs the inverse operation to [`url.domainToUnicode()`](https://nodejs.org/docs/latest/api/url.html#urldomaintounicodedomain).
```
import url from 'node:url';

console.log(url.domainToASCII('español.com'));
// Prints xn--espaol-zwa.com
console.log(url.domainToASCII('中文.com'));
// Prints xn--fiq228c.com
console.log(url.domainToASCII('xn--iñvalid.com'));
// Prints an empty string
const url = require('node:url');

console.log(url.domainToASCII('español.com'));
// Prints xn--espaol-zwa.com
console.log(url.domainToASCII('中文.com'));
// Prints xn--fiq228c.com
console.log(url.domainToASCII('xn--iñvalid.com'));
// Prints an empty string
copy
```

####  `url.domainToUnicode(domain)`[#](https://nodejs.org/docs/latest/api/url.html#urldomaintounicodedomain)
Added in: v7.4.0, v6.13.0History Version | Changes
---|---
v20.0.0, v18.17.0 | ICU requirement is removed.
  * `domain`
  * Returns:


Returns the Unicode serialization of the `domain`. If `domain` is an invalid domain, the empty string is returned.
It performs the inverse operation to [`url.domainToASCII()`](https://nodejs.org/docs/latest/api/url.html#urldomaintoasciidomain).
```
import url from 'node:url';

console.log(url.domainToUnicode('xn--espaol-zwa.com'));
// Prints español.com
console.log(url.domainToUnicode('xn--fiq228c.com'));
// Prints 中文.com
console.log(url.domainToUnicode('xn--iñvalid.com'));
// Prints an empty string
const url = require('node:url');

console.log(url.domainToUnicode('xn--espaol-zwa.com'));
// Prints español.com
console.log(url.domainToUnicode('xn--fiq228c.com'));
// Prints 中文.com
console.log(url.domainToUnicode('xn--iñvalid.com'));
// Prints an empty string
copy
```

####  `url.fileURLToPath(url[, options])`[#](https://nodejs.org/docs/latest/api/url.html#urlfileurltopathurl-options)
Added in: v10.12.0History Version | Changes
---|---
v22.1.0, v20.13.0 | The `options` argument can now be used to determine how to parse the `path` argument.
  * `url` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) |
  * `options`
    * `windows` `true` if the `path` should be return as a windows filepath, `false` for posix, and `undefined` for the system default. **Default:** `undefined`.
  * Returns:


This function ensures the correct decodings of percent-encoded characters as well as ensuring a cross-platform valid absolute path string.
**Security Considerations:**
This function decodes percent-encoded characters, including encoded dot-segments (`%2e` as `.` and `%2e%2e` as `..`), and then normalizes the resulting path. This means that encoded directory traversal sequences (such as `%2e%2e`) are decoded and processed as actual path traversal, even though encoded slashes (`%2F`, `%5C`) are correctly rejected.
**Applications must not rely on`fileURLToPath()` alone to prevent directory traversal attacks.** Always perform explicit path validation and security checks on the returned path value to ensure it remains within expected boundaries before using it for file system operations.
```
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);

new URL('file:///C:/path/').pathname;      // Incorrect: /C:/path/
fileURLToPath('file:///C:/path/');         // Correct:   C:\path\ (Windows)

new URL('file://nas/foo.txt').pathname;    // Incorrect: /foo.txt
fileURLToPath('file://nas/foo.txt');       // Correct:   \\nas\foo.txt (Windows)

new URL('file:///你好.txt').pathname;      // Incorrect: /%E4%BD%A0%E5%A5%BD.txt
fileURLToPath('file:///你好.txt');         // Correct:   /你好.txt (POSIX)

new URL('file:///hello world').pathname;   // Incorrect: /hello%20world
fileURLToPath('file:///hello world');      // Correct:   /hello world (POSIX)
const { fileURLToPath } = require('node:url');
new URL('file:///C:/path/').pathname;      // Incorrect: /C:/path/
fileURLToPath('file:///C:/path/');         // Correct:   C:\path\ (Windows)

new URL('file://nas/foo.txt').pathname;    // Incorrect: /foo.txt
fileURLToPath('file://nas/foo.txt');       // Correct:   \\nas\foo.txt (Windows)

new URL('file:///你好.txt').pathname;      // Incorrect: /%E4%BD%A0%E5%A5%BD.txt
fileURLToPath('file:///你好.txt');         // Correct:   /你好.txt (POSIX)

new URL('file:///hello world').pathname;   // Incorrect: /hello%20world
fileURLToPath('file:///hello world');      // Correct:   /hello world (POSIX)
copy
```

####  `url.fileURLToPathBuffer(url[, options])`[#](https://nodejs.org/docs/latest/api/url.html#urlfileurltopathbufferurl-options)
  * `url` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) |
  * `options`
    * `windows` `true` if the `path` should be return as a windows filepath, `false` for posix, and `undefined` for the system default. **Default:** `undefined`.
  * Returns: [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer) The fully-resolved platform-specific Node.js file path as a [`<Buffer>`](https://nodejs.org/docs/latest/api/buffer.html#class-buffer).


Like `url.fileURLToPath(...)` except that instead of returning a string representation of the path, a `Buffer` is returned. This conversion is helpful when the input URL contains percent-encoded segments that are not valid UTF-8 / Unicode sequences.
**Security Considerations:**
This function has the same security considerations as [`url.fileURLToPath()`](https://nodejs.org/docs/latest/api/url.html#urlfileurltopathurl-options). It decodes percent-encoded characters, including encoded dot-segments (`%2e` as `.` and `%2e%2e` as `..`), and normalizes the path. **Applications must not rely on this function alone to prevent directory traversal attacks.** Always perform explicit path validation on the returned buffer value before using it for file system operations.
####  `url.format(URL[, options])`[#](https://nodejs.org/docs/latest/api/url.html#urlformaturl-options)
Added in: v7.6.0
  * `URL` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) A [WHATWG URL](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) object
  * `options`
    * `auth` `true` if the serialized URL string should include the username and password, `false` otherwise. **Default:** `true`.
    * `fragment` `true` if the serialized URL string should include the fragment, `false` otherwise. **Default:** `true`.
    * `search` `true` if the serialized URL string should include the search query, `false` otherwise. **Default:** `true`.
    * `unicode` `true` if Unicode characters appearing in the host component of the URL string should be encoded directly as opposed to being Punycode encoded. **Default:** `false`.
  * Returns:


Returns a customizable serialization of a URL `String` representation of a [WHATWG URL](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) object.
The URL object has both a `toString()` method and `href` property that return string serializations of the URL. These are not, however, customizable in any way. The `url.format(URL[, options])` method allows for basic customization of the output.
```
import url from 'node:url';
const myURL = new URL('https://a:b@測試?abc#foo');

console.log(myURL.href);
// Prints https://a:b@xn--g6w251d/?abc#foo

console.log(myURL.toString());
// Prints https://a:b@xn--g6w251d/?abc#foo

console.log(url.format(myURL, { fragment: false, unicode: true, auth: false }));
// Prints 'https://測試/?abc'
const url = require('node:url');
const myURL = new URL('https://a:b@測試?abc#foo');

console.log(myURL.href);
// Prints https://a:b@xn--g6w251d/?abc#foo

console.log(myURL.toString());
// Prints https://a:b@xn--g6w251d/?abc#foo

console.log(url.format(myURL, { fragment: false, unicode: true, auth: false }));
// Prints 'https://測試/?abc'
copy
```

####  `url.pathToFileURL(path[, options])`[#](https://nodejs.org/docs/latest/api/url.html#urlpathtofileurlpath-options)
Added in: v10.12.0History Version | Changes
---|---
v22.1.0, v20.13.0 | The `options` argument can now be used to determine how to return the `path` value.
  * `path`
  * `options`
    * `windows` `true` if the `path` should be treated as a windows filepath, `false` for posix, and `undefined` for the system default. **Default:** `undefined`.
  * Returns: [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) The file URL object.


This function ensures that `path` is resolved absolutely, and that the URL control characters are correctly encoded when converting into a File URL.
```
import { pathToFileURL } from 'node:url';

new URL('/foo#1', 'file:');           // Incorrect: file:///foo#1
pathToFileURL('/foo#1');              // Correct:   file:///foo%231 (POSIX)

new URL('/some/path%.c', 'file:');    // Incorrect: file:///some/path%.c
pathToFileURL('/some/path%.c');       // Correct:   file:///some/path%25.c (POSIX)
const { pathToFileURL } = require('node:url');
new URL(__filename);                  // Incorrect: throws (POSIX)
new URL(__filename);                  // Incorrect: C:\... (Windows)
pathToFileURL(__filename);            // Correct:   file:///... (POSIX)
pathToFileURL(__filename);            // Correct:   file:///C:/... (Windows)

new URL('/foo#1', 'file:');           // Incorrect: file:///foo#1
pathToFileURL('/foo#1');              // Correct:   file:///foo%231 (POSIX)

new URL('/some/path%.c', 'file:');    // Incorrect: file:///some/path%.c
pathToFileURL('/some/path%.c');       // Correct:   file:///some/path%25.c (POSIX)
copy
```

####  `url.urlToHttpOptions(url)`[#](https://nodejs.org/docs/latest/api/url.html#urlurltohttpoptionsurl)
Added in: v15.7.0, v14.18.0History Version | Changes
---|---
v19.9.0, v18.17.0 | The returned object will also contain all the own enumerable properties of the `url` argument.
  * `url` [`<URL>`](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) The [WHATWG URL](https://nodejs.org/docs/latest/api/url.html#the-whatwg-url-api) object to convert to an options object.
  * Returns:
    * `protocol`
    * `hostname`
    * `hash`
    * `search`
    * `pathname`
    * `path` `'/index.html?page=12'`. An exception is thrown when the request path contains illegal characters. Currently, only spaces are rejected but that may change in the future.
    * `href`
    * `port`
    * `auth` `'user:password'` to compute an Authorization header.


This utility function converts a URL object into an ordinary options object as expected by the [`http.request()`](https://nodejs.org/docs/latest/api/http.html#httprequestoptions-callback) and [`https.request()`](https://nodejs.org/docs/latest/api/https.html#httpsrequestoptions-callback) APIs.
```
import { urlToHttpOptions } from 'node:url';
const myURL = new URL('https://a:b@測試?abc#foo');

console.log(urlToHttpOptions(myURL));
/*
{
  protocol: 'https:',
  hostname: 'xn--g6w251d',
  hash: '#foo',
  search: '?abc',
  pathname: '/',
  path: '/?abc',
  href: 'https://a:b@xn--g6w251d/?abc#foo',
  auth: 'a:b'
}
*/
const { urlToHttpOptions } = require('node:url');
const myURL = new URL('https://a:b@測試?abc#foo');

console.log(urlToHttpOptions(myURL));
/*
{
  protocol: 'https:',
  hostname: 'xn--g6w251d',
  hash: '#foo',
  search: '?abc',
  pathname: '/',
  path: '/?abc',
  href: 'https://a:b@xn--g6w251d/?abc#foo',
  auth: 'a:b'
}
*/
copy
```

### Legacy URL API[#](https://nodejs.org/docs/latest/api/url.html#legacy-url-api)
History Version | Changes
---|---
v15.13.0, v14.17.0 | Deprecation revoked. Status changed to "Legacy".
v11.0.0 | This API is deprecated.
Stability: 3 - Legacy: Use the WHATWG URL API instead.
#### Legacy `urlObject`[#](https://nodejs.org/docs/latest/api/url.html#legacy-urlobject)
History Version | Changes
---|---
v15.13.0, v14.17.0 | Deprecation revoked. Status changed to "Legacy".
v11.0.0 | The Legacy URL API is deprecated. Use the WHATWG URL API.
The legacy `urlObject` (`require('node:url').Url` or `import { Url } from 'node:url'`) is created and returned by the `url.parse()` function.
#####  `urlObject.auth`[#](https://nodejs.org/docs/latest/api/url.html#urlobjectauth)
The `auth` property is the username and password portion of the URL, also referred to as _userinfo_. This string subset follows the `protocol` and double slashes (if present) and precedes the `host` component, delimited by `@`. The string is either the username, or it is the username and password separated by `:`.
