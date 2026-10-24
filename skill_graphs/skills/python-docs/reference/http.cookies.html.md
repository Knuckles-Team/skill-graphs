[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html)
    * [Cookie Objects](https://docs.python.org/3/library/http.cookies.html#cookie-objects)
    * [Morsel Objects](https://docs.python.org/3/library/http.cookies.html#morsel-objects)
    * [Example](https://docs.python.org/3/library/http.cookies.html#example)


#### Previous topic
[`http.server` — HTTP servers](https://docs.python.org/3/library/http.server.html "previous chapter")
#### Next topic
[`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=http.cookies+%E2%80%94+HTTP+state+management&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.cookies.html&pagesource=library%2Fhttp.cookies.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/http.cookiejar.html "http.cookiejar — Cookie handling for HTTP clients") |
  * [previous](https://docs.python.org/3/library/http.server.html "http.server — HTTP servers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html)
  * |
  * Theme  Auto Light Dark |


#  `http.cookies` — HTTP state management[¶](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "Link to this heading")
**Source code:**
* * *
The `http.cookies` module defines classes for abstracting the concept of cookies, an HTTP state management mechanism. It supports both simple string-only cookies, and provides an abstraction for having any serializable data-type as cookie value.
The module formerly strictly applied the parsing rules described in the
The character set, [`string.ascii_letters`](https://docs.python.org/3/library/string.html#string.ascii_letters "string.ascii_letters"), [`string.digits`](https://docs.python.org/3/library/string.html#string.digits "string.digits") and `!#$%&'*+-.^_`|~:` denote the set of valid characters allowed by this module in a cookie name (as [`key`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.key "http.cookies.Morsel.key")).
Changed in version 3.3: Allowed ‘:’ as a valid cookie name character.
Note
On encountering an invalid cookie, [`CookieError`](https://docs.python.org/3/library/http.cookies.html#http.cookies.CookieError "http.cookies.CookieError") is raised, so if your cookie data comes from a browser you should always prepare for invalid data and catch `CookieError` on parsing.

_exception_ http.cookies.CookieError[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.CookieError "Link to this definition")

Exception failing because of _Set-Cookie_ header, etc.

_class_ http.cookies.BaseCookie([_input_])[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie "Link to this definition")

This class is a dictionary-like object whose keys are strings and whose values are [`Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel") instances. Note that upon setting a key to a value, the value is first converted to a `Morsel` containing the key and the value.
If _input_ is given, it is passed to the [`load()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.load "http.cookies.BaseCookie.load") method.

_class_ http.cookies.SimpleCookie([_input_])[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.SimpleCookie "Link to this definition")

This class derives from [`BaseCookie`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie "http.cookies.BaseCookie") and overrides [`value_decode()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.value_decode "http.cookies.BaseCookie.value_decode") and [`value_encode()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.value_encode "http.cookies.BaseCookie.value_encode"). `SimpleCookie` supports strings as cookie values. When setting the value, `SimpleCookie` calls the builtin [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") to convert the value to a string. Values received from HTTP are kept as strings.
See also

Module [`http.cookiejar`](https://docs.python.org/3/library/http.cookiejar.html#module-http.cookiejar "http.cookiejar: Classes for automatic handling of HTTP cookies.")

HTTP cookie handling for web _clients_. The [`http.cookiejar`](https://docs.python.org/3/library/http.cookiejar.html#module-http.cookiejar "http.cookiejar: Classes for automatic handling of HTTP cookies.") and `http.cookies` modules do not depend on each other.
This is the state management specification implemented by this module.
## Cookie Objects[¶](https://docs.python.org/3/library/http.cookies.html#cookie-objects "Link to this heading")

BaseCookie.value_decode(_val_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.value_decode "Link to this definition")

Return a tuple `(real_value, coded_value)` from a string representation. `real_value` can be any type. This method does no decoding in [`BaseCookie`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie "http.cookies.BaseCookie") — it exists so it can be overridden.

BaseCookie.value_encode(_val_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.value_encode "Link to this definition")

Return a tuple `(real_value, coded_value)`. _val_ can be any type, but `coded_value` will always be converted to a string. This method does no encoding in [`BaseCookie`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie "http.cookies.BaseCookie") — it exists so it can be overridden.
In general, it should be the case that `value_encode()` and [`value_decode()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.value_decode "http.cookies.BaseCookie.value_decode") are inverses on the range of _value_decode_.

BaseCookie.output(_attrs =None_, _header ='Set-Cookie:'_, _sep ='\r\n'_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.output "Link to this definition")

Return a string representation suitable to be sent as HTTP headers. _attrs_ and _header_ are sent to each [`Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel")’s [`output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.output "http.cookies.Morsel.output") method. _sep_ is used to join the headers together, and is by default the combination `'\r\n'` (CRLF).

BaseCookie.js_output(_attrs =None_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.js_output "Link to this definition")

Return an embeddable JavaScript snippet, which, if run on a browser which supports JavaScript, will act the same as if the HTTP headers was sent.
The meaning for _attrs_ is the same as in [`output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.output "http.cookies.BaseCookie.output").

BaseCookie.load(_rawdata_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.load "Link to this definition")

If _rawdata_ is a string, parse it as an `HTTP_COOKIE` and add the values found there as [`Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel")s. If it is a dictionary, it is equivalent to:
Copy```
for k, v in rawdata.items():
    cookie[k] = v

```

## Morsel Objects[¶](https://docs.python.org/3/library/http.cookies.html#morsel-objects "Link to this heading")

_class_ http.cookies.Morsel[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "Link to this definition")

Abstract a key/value pair, which has some
Morsels are dictionary-like objects, whose set of keys is constant — the valid
>

expires[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.expires "Link to this definition")


path[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.path "Link to this definition")


comment[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.comment "Link to this definition")


domain[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.domain "Link to this definition")


max-age


secure[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.secure "Link to this definition")


version[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.version "Link to this definition")


httponly[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.httponly "Link to this definition")


samesite[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.samesite "Link to this definition")


partitioned[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.partitioned "Link to this definition")

The attribute [`httponly`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.httponly "http.cookies.Morsel.httponly") specifies that the cookie is only transferred in HTTP requests, and is not accessible through JavaScript. This is intended to mitigate some forms of cross-site scripting.
The attribute [`samesite`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.samesite "http.cookies.Morsel.samesite") controls when the browser sends the cookie with cross-site requests. This helps to mitigate CSRF attacks. Valid values are “Strict” (only sent with same-site requests), “Lax” (sent with same-site requests and top-level navigations), and “None” (sent with same-site and cross-site requests). When using “None”, the “secure” attribute must also be set, as required by modern browsers.
The attribute [`partitioned`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.partitioned "http.cookies.Morsel.partitioned") indicates to user agents that these cross-site cookies _should_ only be available in the same top-level context that the cookie was first set in. For this to be accepted by the user agent, you **must** also set `Secure`.
In addition, it is recommended to use the `__Host` prefix when setting partitioned cookies to make them bound to the hostname and not the registrable domain. Read
The keys are case-insensitive and their default value is `''`.
Changed in version 3.5: `__eq__()` now takes [`key`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.key "http.cookies.Morsel.key") and [`value`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.value "http.cookies.Morsel.value") into account.
Changed in version 3.7: Attributes [`key`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.key "http.cookies.Morsel.key"), [`value`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.value "http.cookies.Morsel.value") and [`coded_value`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.coded_value "http.cookies.Morsel.coded_value") are read-only. Use [`set()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.set "http.cookies.Morsel.set") for setting them.
Changed in version 3.8: Added support for the [`samesite`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.samesite "http.cookies.Morsel.samesite") attribute.
Changed in version 3.14: Added support for the [`partitioned`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.partitioned "http.cookies.Morsel.partitioned") attribute.

Morsel.value[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.value "Link to this definition")

The value of the cookie.

Morsel.coded_value[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.coded_value "Link to this definition")

The encoded value of the cookie — this is what should be sent.

Morsel.key[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.key "Link to this definition")

The name of the cookie.

Morsel.set(_key_ , _value_ , _coded_value_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.set "Link to this definition")

Set the _key_ , _value_ and _coded_value_ attributes.

Morsel.isReservedKey(_K_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.isReservedKey "Link to this definition")

Whether _K_ is a member of the set of keys of a [`Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel").

Morsel.output(_attrs =None_, _header ='Set-Cookie:'_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.output "Link to this definition")

Return a string representation of the Morsel, suitable to be sent as an HTTP header. By default, all the attributes are included, unless _attrs_ is given, in which case it should be a list of attributes to use. _header_ is by default `"Set-Cookie:"`.

Morsel.js_output(_attrs =None_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.js_output "Link to this definition")

Return an embeddable JavaScript snippet, which, if run on a browser which supports JavaScript, will act the same as if the HTTP header was sent.
The meaning for _attrs_ is the same as in [`output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.output "http.cookies.Morsel.output").

Morsel.OutputString(_attrs =None_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.OutputString "Link to this definition")

Return a string representing the Morsel, without any surrounding HTTP or JavaScript.
The meaning for _attrs_ is the same as in [`output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.output "http.cookies.Morsel.output").

Morsel.update(_values_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.update "Link to this definition")

Update the values in the Morsel dictionary with the values in the dictionary _values_. Raise an error if any of the keys in the _values_ dict is not a valid
Changed in version 3.5: an error is raised for invalid keys.

Morsel.copy(_value_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.copy "Link to this definition")

Return a shallow copy of the Morsel object.
Changed in version 3.5: return a Morsel object instead of a dict.

Morsel.setdefault(_key_ , _value =None_)[¶](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.setdefault "Link to this definition")

Raise an error if key is not a valid [`dict.setdefault()`](https://docs.python.org/3/library/stdtypes.html#dict.setdefault "dict.setdefault").
## Example[¶](https://docs.python.org/3/library/http.cookies.html#example "Link to this heading")
The following example demonstrates how to use the `http.cookies` module.
Copy```
>>> from http import cookies
>>> C = cookies.SimpleCookie()
>>> C["fig"] = "newton"
>>> C["sugar"] = "wafer"
>>> print(C) # generate HTTP headers
Set-Cookie: fig=newton
Set-Cookie: sugar=wafer
>>> print(C.output()) # same thing
Set-Cookie: fig=newton
Set-Cookie: sugar=wafer
>>> C = cookies.SimpleCookie()
>>> C["rocky"] = "road"
>>> C["rocky"]["path"] = "/cookie"
>>> print(C.output(header="Cookie:"))
Cookie: rocky=road; Path=/cookie
>>> print(C.output(attrs=[], header="Cookie:"))
Cookie: rocky=road
>>> C = cookies.SimpleCookie()
>>> C.load("chips=ahoy; vienna=finger") # load from a string (HTTP header)
>>> print(C)
Set-Cookie: chips=ahoy
Set-Cookie: vienna=finger
>>> C = cookies.SimpleCookie()
>>> C.load('keebler="E=everybody; L=\\"Loves\\"; fudge=;";')
>>> print(C)
Set-Cookie: keebler="E=everybody; L=\"Loves\"; fudge=;"
>>> C = cookies.SimpleCookie()
>>> C["oreo"] = "doublestuff"
>>> C["oreo"]["path"] = "/"
>>> print(C)
Set-Cookie: oreo=doublestuff; Path=/
>>> C = cookies.SimpleCookie()
>>> C["twix"] = "none for you"
>>> C["twix"].value
'none for you'
>>> C = cookies.SimpleCookie()
>>> C["number"] = 7 # equivalent to C["number"] = str(7)
>>> C["string"] = "seven"
>>> C["number"].value
'7'
>>> C["string"].value
'seven'
>>> print(C)
Set-Cookie: number=7
Set-Cookie: string=seven

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html)
    * [Cookie Objects](https://docs.python.org/3/library/http.cookies.html#cookie-objects)
    * [Morsel Objects](https://docs.python.org/3/library/http.cookies.html#morsel-objects)
    * [Example](https://docs.python.org/3/library/http.cookies.html#example)


#### Previous topic
[`http.server` — HTTP servers](https://docs.python.org/3/library/http.server.html "previous chapter")
#### Next topic
[`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=http.cookies+%E2%80%94+HTTP+state+management&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.cookies.html&pagesource=library%2Fhttp.cookies.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/http.cookiejar.html "http.cookiejar — Cookie handling for HTTP clients") |
  * [previous](https://docs.python.org/3/library/http.server.html "http.server — HTTP servers") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
