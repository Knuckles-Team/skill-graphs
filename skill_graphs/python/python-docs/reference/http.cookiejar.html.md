[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html)
    * [CookieJar and FileCookieJar Objects](https://docs.python.org/3/library/http.cookiejar.html#cookiejar-and-filecookiejar-objects)
    * [FileCookieJar subclasses and co-operation with web browsers](https://docs.python.org/3/library/http.cookiejar.html#filecookiejar-subclasses-and-co-operation-with-web-browsers)
    * [CookiePolicy Objects](https://docs.python.org/3/library/http.cookiejar.html#cookiepolicy-objects)
    * [DefaultCookiePolicy Objects](https://docs.python.org/3/library/http.cookiejar.html#defaultcookiepolicy-objects)
    * [Cookie Objects](https://docs.python.org/3/library/http.cookiejar.html#cookie-objects)
    * [Examples](https://docs.python.org/3/library/http.cookiejar.html#examples)


#### Previous topic
[`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html "previous chapter")
#### Next topic
[`xmlrpc` — XMLRPC server and client modules](https://docs.python.org/3/library/xmlrpc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=http.cookiejar+%E2%80%94+Cookie+handling+for+HTTP+clients&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.cookiejar.html&pagesource=library%2Fhttp.cookiejar.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xmlrpc.html "xmlrpc — XMLRPC server and client modules") |
  * [previous](https://docs.python.org/3/library/http.cookies.html "http.cookies — HTTP state management") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html)
  * |
  * Theme  Auto Light Dark |


#  `http.cookiejar` — Cookie handling for HTTP clients[¶](https://docs.python.org/3/library/http.cookiejar.html#module-http.cookiejar "Link to this heading")
**Source code:**
* * *
The `http.cookiejar` module defines classes for automatic handling of HTTP cookies. It is useful for accessing websites that require small pieces of data – _cookies_ – to be set on the client machine by an HTTP response from a web server, and then returned to the server in later HTTP requests.
Both the regular Netscape cookie protocol and the protocol defined by `http.cookiejar` attempts to follow the de-facto Netscape cookie protocol (which differs substantially from that set out in the original Netscape specification), including taking note of the `max-age` and `port` cookie-attributes introduced with RFC 2965.
Note
The various named parameters found in _Set-Cookie_ and _Set-Cookie2_ headers (eg. `domain` and `expires`) are conventionally referred to as _attributes_. To distinguish them from Python attributes, the documentation for this module uses the term _cookie-attribute_ instead.
The module defines the following exception:

_exception_ http.cookiejar.LoadError[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.LoadError "Link to this definition")

Instances of [`FileCookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") raise this exception on failure to load cookies from a file. `LoadError` is a subclass of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
Changed in version 3.3: `LoadError` used to be a subtype of [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError"), which is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").
The following classes are provided:

_class_ http.cookiejar.CookieJar(_policy =None_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "Link to this definition")

_policy_ is an object implementing the [`CookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") interface.
The `CookieJar` class stores HTTP cookies. It extracts cookies from HTTP requests, and returns them in HTTP responses. `CookieJar` instances automatically expire contained cookies when necessary. Subclasses are also responsible for storing and retrieving cookies from a file or database.

_class_ http.cookiejar.FileCookieJar(_filename =None_, _delayload =None_, _policy =None_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar "Link to this definition")

_policy_ is an object implementing the [`CookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") interface. For the other arguments, see the documentation for the corresponding attributes.
A [`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar") which can load cookies from, and perhaps save cookies to, a file on disk. Cookies are **NOT** loaded from the named file until either the [`load()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.load "http.cookiejar.FileCookieJar.load") or [`revert()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.revert "http.cookiejar.FileCookieJar.revert") method is called. Subclasses of this class are documented in section [FileCookieJar subclasses and co-operation with web browsers](https://docs.python.org/3/library/http.cookiejar.html#file-cookie-jar-classes).
This should not be initialized directly – use its subclasses below instead.
Changed in version 3.8: The filename parameter supports a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

_class_ http.cookiejar.CookiePolicy[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "Link to this definition")

This class is responsible for deciding whether each cookie should be accepted from / returned to the server.

_class_ http.cookiejar.DefaultCookiePolicy(_blocked_domains =None_, _allowed_domains =None_, _netscape =True_, _rfc2965 =False_, _rfc2109_as_netscape =None_, _hide_cookie2 =False_, _strict_domain =False_, _strict_rfc2965_unverifiable =True_, _strict_ns_unverifiable =False_, _strict_ns_domain =DefaultCookiePolicy.DomainLiberal_, _strict_ns_set_initial_dollar =False_, _strict_ns_set_path =False_, _secure_protocols =('https', 'wss')_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy "Link to this definition")

Constructor arguments should be passed as keyword arguments only. _blocked_domains_ is a sequence of domain names that we never accept cookies from, nor return cookies to. _allowed_domains_ if not [`None`](https://docs.python.org/3/library/constants.html#None "None"), this is a sequence of the only domains for which we accept and return cookies. _secure_protocols_ is a sequence of protocols for which secure cookies can be added to. By default _https_ and _wss_ (secure websocket) are considered secure protocols. For all other arguments, see the documentation for [`CookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") and `DefaultCookiePolicy` objects.
`DefaultCookiePolicy` implements the standard accept / reject rules for Netscape and _Set-Cookie_ header with a version cookie-attribute of 1) are treated according to the RFC 2965 rules. However, if RFC 2965 handling is turned off or [`rfc2109_as_netscape`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.rfc2109_as_netscape "http.cookiejar.DefaultCookiePolicy.rfc2109_as_netscape") is `True`, RFC 2109 cookies are ‘downgraded’ by the [`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar") instance to Netscape cookies, by setting the `version` attribute of the [`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie") instance to 0. `DefaultCookiePolicy` also provides some parameters to allow some fine-tuning of policy.

_class_ http.cookiejar.Cookie[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "Link to this definition")

This class represents Netscape, `http.cookiejar` construct their own `Cookie` instances. Instead, if necessary, call `make_cookies()` on a [`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar") instance.
See also

Module [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")

URL opening with automatic cookie handling.

Module [`http.cookies`](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "http.cookies: Support for HTTP state management \(cookies\).")

HTTP cookie classes, principally useful for server-side code. The `http.cookiejar` and [`http.cookies`](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "http.cookies: Support for HTTP state management \(cookies\).") modules do not depend on each other.
The specification of the original Netscape cookie protocol. Though this is still the dominant protocol, the ‘Netscape cookie protocol’ implemented by all the major browsers (and `http.cookiejar`) only bears a passing resemblance to the one sketched out in `cookie_spec.html`.
Obsoleted by _Set-Cookie_ with version=1.
The Netscape protocol with the bugs fixed. Uses _Set-Cookie2_ in place of _Set-Cookie_. Not widely used.
Unfinished errata to
## CookieJar and FileCookieJar Objects[¶](https://docs.python.org/3/library/http.cookiejar.html#cookiejar-and-filecookiejar-objects "Link to this heading")
[`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar") objects support the [iterator](https://docs.python.org/3/glossary.html#term-iterator) protocol for iterating over contained [`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie") objects.
[`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar") has the following methods:

CookieJar.add_cookie_header(_request_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.add_cookie_header "Link to this definition")

Add correct _Cookie_ header to _request_.
If policy allows (ie. the `rfc2965` and `hide_cookie2` attributes of the [`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar")’s [`CookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") instance are true and false respectively), the _Cookie2_ header is also added when appropriate.
The _request_ object (usually a [`urllib.request.Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") instance) must support the methods `get_full_url()`, `has_header()`, `get_header()`, `header_items()`, `add_unredirected_header()` and the attributes `host`, `type`, `unverifiable` and `origin_req_host` as documented by [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.").
Changed in version 3.3: _request_ object needs `origin_req_host` attribute. Dependency on a deprecated method `get_origin_req_host()` has been removed.

CookieJar.extract_cookies(_response_ , _request_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.extract_cookies "Link to this definition")

Extract cookies from HTTP _response_ and store them in the [`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar"), where allowed by policy.
The [`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar") will look for allowable _Set-Cookie_ and _Set-Cookie2_ headers in the _response_ argument, and store cookies as appropriate (subject to the [`CookiePolicy.set_ok()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.set_ok "http.cookiejar.CookiePolicy.set_ok") method’s approval).
The _response_ object (usually the result of a call to [`urllib.request.urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen"), or similar) should support an `info()` method, which returns an [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message") instance.
The _request_ object (usually a [`urllib.request.Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") instance) must support the method `get_full_url()` and the attributes `host`, `unverifiable` and `origin_req_host`, as documented by [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs."). The request is used to set default values for cookie-attributes as well as for checking that the cookie is allowed to be set.
Changed in version 3.3: _request_ object needs `origin_req_host` attribute. Dependency on a deprecated method `get_origin_req_host()` has been removed.

CookieJar.set_policy(_policy_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.set_policy "Link to this definition")

Set the [`CookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") instance to be used.

CookieJar.make_cookies(_response_ , _request_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.make_cookies "Link to this definition")

Return sequence of [`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie") objects extracted from _response_ object.
See the documentation for [`extract_cookies()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.extract_cookies "http.cookiejar.CookieJar.extract_cookies") for the interfaces required of the _response_ and _request_ arguments.

CookieJar.set_cookie_if_ok(_cookie_ , _request_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.set_cookie_if_ok "Link to this definition")

Set a [`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie") if policy says it’s OK to do so.

CookieJar.set_cookie(_cookie_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.set_cookie "Link to this definition")

Set a [`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie"), without checking with policy to see whether or not it should be set.

CookieJar.clear([_domain_[, _path_[, _name_]]])[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.clear "Link to this definition")

Clear some cookies.
If invoked without arguments, clear all cookies. If given a single argument, only cookies belonging to that _domain_ will be removed. If given two arguments, cookies belonging to the specified _domain_ and URL _path_ are removed. If given three arguments, then the cookie with the specified _domain_ , _path_ and _name_ is removed.
Raises [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") if no matching cookie exists.

CookieJar.clear_session_cookies()[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.clear_session_cookies "Link to this definition")

Discard all session cookies.
Discards all contained cookies that have a true `discard` attribute (usually because they had either no `max-age` or `expires` cookie-attribute, or an explicit `discard` cookie-attribute). For interactive browsers, the end of a session usually corresponds to closing the browser window.
Note that the `save()` method won’t save session cookies anyway, unless you ask otherwise by passing a true _ignore_discard_ argument.
[`FileCookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") implements the following additional methods:

FileCookieJar.save(_filename =None_, _ignore_discard =False_, _ignore_expires =False_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.save "Link to this definition")

Save cookies to a file.
This base class raises [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError"). Subclasses may leave this method unimplemented.
_filename_ is the name of file in which to save cookies. If _filename_ is not specified, `self.filename` is used (whose default is the value passed to the constructor, if any); if `self.filename` is [`None`](https://docs.python.org/3/library/constants.html#None "None"), [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.
_ignore_discard_ : save even cookies set to be discarded. _ignore_expires_ : save even cookies that have expired
The file is overwritten if it already exists, thus wiping all the cookies it contains. Saved cookies can be restored later using the [`load()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.load "http.cookiejar.FileCookieJar.load") or [`revert()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.revert "http.cookiejar.FileCookieJar.revert") methods.

FileCookieJar.load(_filename =None_, _ignore_discard =False_, _ignore_expires =False_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.load "Link to this definition")

Load cookies from a file.
Old cookies are kept unless overwritten by newly loaded ones.
Arguments are as for [`save()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.save "http.cookiejar.FileCookieJar.save").
The named file must be in the format understood by the class, or [`LoadError`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.LoadError "http.cookiejar.LoadError") will be raised. Also, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") may be raised, for example if the file does not exist.
Changed in version 3.3: [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") used to be raised, it is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

FileCookieJar.revert(_filename =None_, _ignore_discard =False_, _ignore_expires =False_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.revert "Link to this definition")

Clear all cookies and reload cookies from a saved file.
`revert()` can raise the same exceptions as [`load()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.load "http.cookiejar.FileCookieJar.load"). If there is a failure, the object’s state will not be altered.
[`FileCookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") instances have the following public attributes:

FileCookieJar.filename[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.filename "Link to this definition")

Filename of default file in which to keep cookies. This attribute may be assigned to.

FileCookieJar.delayload[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar.delayload "Link to this definition")

If true, load cookies lazily from disk. This attribute should not be assigned to. This is only a hint, since this only affects performance, not behaviour (unless the cookies on disk are changing). A [`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar") object may ignore it. None of the [`FileCookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") classes included in the standard library lazily loads cookies.
## FileCookieJar subclasses and co-operation with web browsers[¶](https://docs.python.org/3/library/http.cookiejar.html#filecookiejar-subclasses-and-co-operation-with-web-browsers "Link to this heading")
The following [`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar") subclasses are provided for reading and writing.

_class_ http.cookiejar.MozillaCookieJar(_filename =None_, _delayload =None_, _policy =None_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.MozillaCookieJar "Link to this definition")

A [`FileCookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") that can load from and save cookies to disk in the Mozilla `cookies.txt` file format (which is also used by curl and the Lynx and Netscape browsers).
Note
This loses information about `port`.
Warning
Back up your cookies before saving if you have cookies whose loss / corruption would be inconvenient (there are some subtleties which may lead to slight changes in the file over a load / save round-trip).
Also note that cookies saved while Mozilla is running will get clobbered by Mozilla.

_class_ http.cookiejar.LWPCookieJar(_filename =None_, _delayload =None_, _policy =None_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.LWPCookieJar "Link to this definition")

A [`FileCookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.FileCookieJar "http.cookiejar.FileCookieJar") that can load from and save cookies to disk in format compatible with the libwww-perl library’s `Set-Cookie3` file format. This is convenient if you want to store cookies in a human-readable file.
Changed in version 3.8: The filename parameter supports a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).
## CookiePolicy Objects[¶](https://docs.python.org/3/library/http.cookiejar.html#cookiepolicy-objects "Link to this heading")
Objects implementing the [`CookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") interface have the following methods:

CookiePolicy.set_ok(_cookie_ , _request_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.set_ok "Link to this definition")

Return boolean value indicating whether cookie should be accepted from server.
_cookie_ is a [`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie") instance. _request_ is an object implementing the interface defined by the documentation for [`CookieJar.extract_cookies()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.extract_cookies "http.cookiejar.CookieJar.extract_cookies").

CookiePolicy.return_ok(_cookie_ , _request_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.return_ok "Link to this definition")

Return boolean value indicating whether cookie should be returned to server.
_cookie_ is a [`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie") instance. _request_ is an object implementing the interface defined by the documentation for [`CookieJar.add_cookie_header()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar.add_cookie_header "http.cookiejar.CookieJar.add_cookie_header").

CookiePolicy.domain_return_ok(_domain_ , _request_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.domain_return_ok "Link to this definition")

Return `False` if cookies should not be returned, given cookie domain.
This method is an optimization. It removes the need for checking every cookie with a particular domain (which might involve reading many files). Returning true from `domain_return_ok()` and [`path_return_ok()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.path_return_ok "http.cookiejar.CookiePolicy.path_return_ok") leaves all the work to [`return_ok()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.return_ok "http.cookiejar.CookiePolicy.return_ok").
If `domain_return_ok()` returns true for the cookie domain, [`path_return_ok()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.path_return_ok "http.cookiejar.CookiePolicy.path_return_ok") is called for the cookie path. Otherwise, `path_return_ok()` and [`return_ok()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.return_ok "http.cookiejar.CookiePolicy.return_ok") are never called for that cookie domain. If `path_return_ok()` returns true, `return_ok()` is called with the [`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie") object itself for a full check. Otherwise, `return_ok()` is never called for that cookie path.
Note that `domain_return_ok()` is called for every _cookie_ domain, not just for the _request_ domain. For example, the function might be called with both `".example.com"` and `"www.example.com"` if the request domain is `"www.example.com"`. The same goes for [`path_return_ok()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.path_return_ok "http.cookiejar.CookiePolicy.path_return_ok").
The _request_ argument is as documented for [`return_ok()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.return_ok "http.cookiejar.CookiePolicy.return_ok").

CookiePolicy.path_return_ok(_path_ , _request_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.path_return_ok "Link to this definition")

Return `False` if cookies should not be returned, given cookie path.
See the documentation for [`domain_return_ok()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.domain_return_ok "http.cookiejar.CookiePolicy.domain_return_ok").
In addition to implementing the methods above, implementations of the [`CookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") interface must also supply the following attributes, indicating which protocols should be used, and how. All of these attributes may be assigned to.

CookiePolicy.netscape[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.netscape "Link to this definition")

Implement Netscape protocol.

CookiePolicy.rfc2965[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.rfc2965 "Link to this definition")

Implement

CookiePolicy.hide_cookie2[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy.hide_cookie2 "Link to this definition")

Don’t add _Cookie2_ header to requests (the presence of this header indicates to the server that we understand
The most useful way to define a [`CookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") class is by subclassing from [`DefaultCookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy") and overriding some or all of the methods above. `CookiePolicy` itself may be used as a ‘null policy’ to allow setting and receiving any and all cookies (this is unlikely to be useful).
## DefaultCookiePolicy Objects[¶](https://docs.python.org/3/library/http.cookiejar.html#defaultcookiepolicy-objects "Link to this heading")
Implements the standard rules for accepting and returning cookies.
Both
The easiest way to provide your own policy is to override this class and call its methods in your overridden implementations before adding your own additional checks:
Copy```
import http.cookiejar
class MyCookiePolicy(http.cookiejar.DefaultCookiePolicy):
    def set_ok(self, cookie, request):
        if not http.cookiejar.DefaultCookiePolicy.set_ok(self, cookie, request):
            return False
        if i_dont_want_to_store_this_cookie(cookie):
            return False
        return True

```

In addition to the features required to implement the [`CookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") interface, this class allows you to block and allow domains from setting and receiving cookies. There are also some strictness switches that allow you to tighten up the rather loose Netscape protocol rules a little bit (at the cost of blocking some benign cookies).
A domain blocklist and allowlist is provided (both off by default). Only domains not in the blocklist and present in the allowlist (if the allowlist is active) participate in cookie setting and returning. Use the _blocked_domains_ constructor argument, and `blocked_domains()` and `set_blocked_domains()` methods (and the corresponding argument and methods for _allowed_domains_). If you set an allowlist, you can turn it off again by setting it to [`None`](https://docs.python.org/3/library/constants.html#None "None").
Domains in block or allow lists that do not start with a dot must equal the cookie domain to be matched. For example, `"example.com"` matches a blocklist entry of `"example.com"`, but `"www.example.com"` does not. Domains that do start with a dot are matched by more specific domains too. For example, both `"www.example.com"` and `"www.coyote.example.com"` match `".example.com"` (but `"example.com"` itself does not). IP addresses are an exception, and must match exactly. For example, if blocked_domains contains `"192.168.1.2"` and `".168.1.2"`, 192.168.1.2 is blocked, but 193.168.1.2 is not.
[`DefaultCookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy") implements the following additional methods:

DefaultCookiePolicy.blocked_domains()[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.blocked_domains "Link to this definition")

Return the sequence of blocked domains (as a tuple).

DefaultCookiePolicy.set_blocked_domains(_blocked_domains_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.set_blocked_domains "Link to this definition")

Set the sequence of blocked domains.

DefaultCookiePolicy.is_blocked(_domain_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.is_blocked "Link to this definition")

Return `True` if _domain_ is on the blocklist for setting or receiving cookies.

DefaultCookiePolicy.allowed_domains()[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.allowed_domains "Link to this definition")

Return [`None`](https://docs.python.org/3/library/constants.html#None "None"), or the sequence of allowed domains (as a tuple).

DefaultCookiePolicy.set_allowed_domains(_allowed_domains_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.set_allowed_domains "Link to this definition")

Set the sequence of allowed domains, or [`None`](https://docs.python.org/3/library/constants.html#None "None").

DefaultCookiePolicy.is_not_allowed(_domain_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.is_not_allowed "Link to this definition")

Return `True` if _domain_ is not on the allowlist for setting or receiving cookies.
[`DefaultCookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy") instances have the following attributes, which are all initialised from the constructor arguments of the same name, and which may all be assigned to.

DefaultCookiePolicy.rfc2109_as_netscape[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.rfc2109_as_netscape "Link to this definition")

If true, request that the [`CookieJar`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookieJar "http.cookiejar.CookieJar") instance downgrade _Set-Cookie_ header with a version cookie-attribute of 1) to Netscape cookies by setting the version attribute of the [`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie") instance to 0. The default value is [`None`](https://docs.python.org/3/library/constants.html#None "None"), in which case RFC 2109 cookies are downgraded if and only if
General strictness switches:

DefaultCookiePolicy.strict_domain[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.strict_domain "Link to this definition")

Don’t allow sites to set two-component domains with country-code top-level domains like `.co.uk`, `.gov.uk`, `.co.nz`.etc. This is far from perfect and isn’t guaranteed to work!

DefaultCookiePolicy.strict_rfc2965_unverifiable[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.strict_rfc2965_unverifiable "Link to this definition")

Follow _never_ blocked on the basis of verifiability
Netscape protocol strictness switches:

DefaultCookiePolicy.strict_ns_unverifiable[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.strict_ns_unverifiable "Link to this definition")

Apply

DefaultCookiePolicy.strict_ns_domain[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.strict_ns_domain "Link to this definition")

Flags indicating how strict to be with domain-matching rules for Netscape cookies. See below for acceptable values.

DefaultCookiePolicy.strict_ns_set_initial_dollar[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.strict_ns_set_initial_dollar "Link to this definition")

Ignore cookies in Set-Cookie: headers that have names starting with `'$'`.

DefaultCookiePolicy.strict_ns_set_path[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.strict_ns_set_path "Link to this definition")

Don’t allow setting cookies whose path doesn’t path-match request URI.
[`strict_ns_domain`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.strict_ns_domain "http.cookiejar.DefaultCookiePolicy.strict_ns_domain") is a collection of flags. Its value is constructed by or-ing together (for example, `DomainStrictNoDots|DomainStrictNonDomain` means both flags are set).

DefaultCookiePolicy.DomainStrictNoDots[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.DomainStrictNoDots "Link to this definition")

When setting cookies, the ‘host prefix’ must not contain a dot (eg. `www.foo.bar.com` can’t set a cookie for `.bar.com`, because `www.foo` contains a dot).

DefaultCookiePolicy.DomainStrictNonDomain[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.DomainStrictNonDomain "Link to this definition")

Cookies that did not explicitly specify a `domain` cookie-attribute can only be returned to a domain equal to the domain that set the cookie (eg. `spam.example.com` won’t be returned cookies from `example.com` that had no `domain` cookie-attribute).

DefaultCookiePolicy.DomainRFC2965Match[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.DomainRFC2965Match "Link to this definition")

When setting cookies, require a full
The following attributes are provided for convenience, and are the most useful combinations of the above flags:

DefaultCookiePolicy.DomainLiberal[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.DomainLiberal "Link to this definition")

Equivalent to 0 (ie. all of the above Netscape domain strictness flags switched off).

DefaultCookiePolicy.DomainStrict[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy.DomainStrict "Link to this definition")

Equivalent to `DomainStrictNoDots|DomainStrictNonDomain`.
## Cookie Objects[¶](https://docs.python.org/3/library/http.cookiejar.html#cookie-objects "Link to this heading")
[`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie") instances have Python attributes roughly corresponding to the standard cookie-attributes specified in the various cookie standards. The correspondence is not one-to-one, because there are complicated rules for assigning default values, because the `max-age` and `expires` cookie-attributes contain equivalent information, and because `http.cookiejar` from version 1 to version 0 (Netscape) cookies.
Assignment to these attributes should not be necessary other than in rare circumstances in a [`CookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.CookiePolicy "http.cookiejar.CookiePolicy") method. The class does not enforce internal consistency, so you should know what you’re doing if you do that.

Cookie.version[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.version "Link to this definition")

Integer or [`None`](https://docs.python.org/3/library/constants.html#None "None"). Netscape cookies have [`version`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.version "http.cookiejar.Cookie.version") 0. `version` cookie-attribute of 1. However, note that `http.cookiejar` may ‘downgrade’ RFC 2109 cookies to Netscape cookies, in which case `version` is 0.

Cookie.name[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.name "Link to this definition")

Cookie name (a string).

Cookie.value[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.value "Link to this definition")

Cookie value (a string), or [`None`](https://docs.python.org/3/library/constants.html#None "None").

Cookie.port[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.port "Link to this definition")

String representing a port or a set of ports (eg. ‘80’, or ‘80,8080’), or [`None`](https://docs.python.org/3/library/constants.html#None "None").

Cookie.domain[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.domain "Link to this definition")

Cookie domain (a string).

Cookie.path[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.path "Link to this definition")

Cookie path (a string, eg. `'/acme/rocket_launchers'`).

Cookie.secure[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.secure "Link to this definition")

`True` if cookie should only be returned over a secure connection.

Cookie.expires[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.expires "Link to this definition")

Integer expiry date in seconds since epoch, or [`None`](https://docs.python.org/3/library/constants.html#None "None"). See also the [`is_expired()`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.is_expired "http.cookiejar.Cookie.is_expired") method.

Cookie.discard[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.discard "Link to this definition")

`True` if this is a session cookie.

Cookie.comment[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.comment "Link to this definition")

String comment from the server explaining the function of this cookie, or [`None`](https://docs.python.org/3/library/constants.html#None "None").

Cookie.comment_url[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.comment_url "Link to this definition")

URL linking to a comment from the server explaining the function of this cookie, or [`None`](https://docs.python.org/3/library/constants.html#None "None").

Cookie.rfc2109[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.rfc2109 "Link to this definition")

`True` if this cookie was received as an _Set-Cookie_ header, and the value of the Version cookie-attribute in that header was 1). This attribute is provided because `http.cookiejar` may ‘downgrade’ RFC 2109 cookies to Netscape cookies, in which case [`version`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.version "http.cookiejar.Cookie.version") is 0.

Cookie.port_specified[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.port_specified "Link to this definition")

`True` if a port or set of ports was explicitly specified by the server (in the _Set-Cookie_ / _Set-Cookie2_ header).

Cookie.domain_specified[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.domain_specified "Link to this definition")

`True` if a domain was explicitly specified by the server.

Cookie.domain_initial_dot[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.domain_initial_dot "Link to this definition")

`True` if the domain explicitly specified by the server began with a dot (`'.'`).
Cookies may have additional non-standard cookie-attributes. These may be accessed using the following methods:

Cookie.has_nonstandard_attr(_name_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.has_nonstandard_attr "Link to this definition")

Return `True` if cookie has the named cookie-attribute.

Cookie.get_nonstandard_attr(_name_ , _default =None_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.get_nonstandard_attr "Link to this definition")

If cookie has the named cookie-attribute, return its value. Otherwise, return _default_.

Cookie.set_nonstandard_attr(_name_ , _value_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.set_nonstandard_attr "Link to this definition")

Set the value of the named cookie-attribute.
The [`Cookie`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie "http.cookiejar.Cookie") class also defines the following method:

Cookie.is_expired(_now =None_)[¶](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.Cookie.is_expired "Link to this definition")

`True` if cookie has passed the time at which the server requested it should expire. If _now_ is given (in seconds since the epoch), return whether the cookie has expired at the specified time.
## Examples[¶](https://docs.python.org/3/library/http.cookiejar.html#examples "Link to this heading")
The first example shows the most common usage of `http.cookiejar`:
Copy```
import http.cookiejar, urllib.request
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")

```

This example illustrates how to open a URL using your Netscape, Mozilla, or Lynx cookies (assumes Unix/Netscape convention for location of the cookies file):
Copy```
import os, http.cookiejar, urllib.request
cj = http.cookiejar.MozillaCookieJar()
cj.load(os.path.join(os.path.expanduser("~"), ".netscape", "cookies.txt"))
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")

```

The next example illustrates the use of [`DefaultCookiePolicy`](https://docs.python.org/3/library/http.cookiejar.html#http.cookiejar.DefaultCookiePolicy "http.cookiejar.DefaultCookiePolicy"). Turn on
Copy```
import urllib.request
from http.cookiejar import CookieJar, DefaultCookiePolicy
policy = DefaultCookiePolicy(
    rfc2965=True, strict_ns_domain=Policy.DomainStrict,
    blocked_domains=["ads.net", ".ads.net"])
cj = CookieJar(policy)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://example.com/")

```

### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html)
    * [CookieJar and FileCookieJar Objects](https://docs.python.org/3/library/http.cookiejar.html#cookiejar-and-filecookiejar-objects)
    * [FileCookieJar subclasses and co-operation with web browsers](https://docs.python.org/3/library/http.cookiejar.html#filecookiejar-subclasses-and-co-operation-with-web-browsers)
    * [CookiePolicy Objects](https://docs.python.org/3/library/http.cookiejar.html#cookiepolicy-objects)
    * [DefaultCookiePolicy Objects](https://docs.python.org/3/library/http.cookiejar.html#defaultcookiepolicy-objects)
    * [Cookie Objects](https://docs.python.org/3/library/http.cookiejar.html#cookie-objects)
    * [Examples](https://docs.python.org/3/library/http.cookiejar.html#examples)


#### Previous topic
[`http.cookies` — HTTP state management](https://docs.python.org/3/library/http.cookies.html "previous chapter")
#### Next topic
[`xmlrpc` — XMLRPC server and client modules](https://docs.python.org/3/library/xmlrpc.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=http.cookiejar+%E2%80%94+Cookie+handling+for+HTTP+clients&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.cookiejar.html&pagesource=library%2Fhttp.cookiejar.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/xmlrpc.html "xmlrpc — XMLRPC server and client modules") |
  * [previous](https://docs.python.org/3/library/http.cookies.html "http.cookies — HTTP state management") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`http.cookiejar` — Cookie handling for HTTP clients](https://docs.python.org/3/library/http.cookiejar.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
