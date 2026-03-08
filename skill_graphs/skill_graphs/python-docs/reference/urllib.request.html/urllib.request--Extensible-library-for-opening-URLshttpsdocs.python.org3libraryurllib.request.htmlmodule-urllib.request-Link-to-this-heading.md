#  `urllib.request` — Extensible library for opening URLs[¶](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "Link to this heading")
**Source code:**
* * *
The `urllib.request` module defines functions and classes which help in opening URLs (mostly HTTP) in a complex world — basic and digest authentication, redirections, cookies and more.
See also
The
Warning
On macOS it is unsafe to use this module in programs using [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork") because the [`getproxies()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.getproxies "urllib.request.getproxies") implementation for macOS uses a higher-level system API. Set the environment variable `no_proxy` to `*` to avoid this problem (e.g. `os.environ["no_proxy"] = "*"`).
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
The `urllib.request` module defines the following functions:

urllib.request.urlopen(_url_ , _data=None_ , [_timeout_ , ]_*_ , _context=None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "Link to this definition")

Open _url_ , which can be either a string containing a valid, properly encoded URL, or a [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") object.
_data_ must be an object specifying additional data to be sent to the server, or `None` if no such data is needed. See [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") for details.
urllib.request module uses HTTP/1.1 and includes `Connection:close` header in its HTTP requests.
The optional _timeout_ parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used). This actually only works for HTTP, HTTPS and FTP connections.
If _context_ is specified, it must be a [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") instance describing the various SSL options. See [`HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "http.client.HTTPSConnection") for more details.
This function always returns an object which can work as a [context manager](https://docs.python.org/3/glossary.html#term-context-manager) and has the properties _url_ , _headers_ , and _status_. See [`urllib.response.addinfourl`](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl "urllib.response.addinfourl") for more detail on these properties.
For HTTP and HTTPS URLs, this function returns a [`http.client.HTTPResponse`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse "http.client.HTTPResponse") object slightly modified. In addition to the three new methods above, the msg attribute contains the same information as the [`reason`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.reason "http.client.HTTPResponse.reason") attribute — the reason phrase returned by server — instead of the response headers as it is specified in the documentation for `HTTPResponse`.
For FTP, file, and data URLs, this function returns a [`urllib.response.addinfourl`](https://docs.python.org/3/library/urllib.request.html#urllib.response.addinfourl "urllib.response.addinfourl") object.
Raises [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError") on protocol errors.
Note that `None` may be returned if no handler handles the request (though the default installed global [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector") uses [`UnknownHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.UnknownHandler "urllib.request.UnknownHandler") to ensure this never happens).
In addition, if proxy settings are detected (for example, when a `*_proxy` environment variable like `http_proxy` is set), [`ProxyHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyHandler "urllib.request.ProxyHandler") is default installed and makes sure the requests are handled through the proxy.
The legacy `urllib.urlopen` function from Python 2.6 and earlier has been discontinued; [`urllib.request.urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") corresponds to the old `urllib2.urlopen`. Proxy handling, which was done by passing a dictionary parameter to `urllib.urlopen`, can be obtained by using [`ProxyHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyHandler "urllib.request.ProxyHandler") objects.
The default opener raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `urllib.Request` with arguments `fullurl`, `data`, `headers`, `method` taken from the request object.
Changed in version 3.2: _cafile_ and _capath_ were added.
HTTPS virtual hosts are now supported if possible (that is, if [`ssl.HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "ssl.HAS_SNI") is true).
_data_ can be an iterable object.
Changed in version 3.3: _cadefault_ was added.
Changed in version 3.4.3: _context_ was added.
Changed in version 3.10: HTTPS connection now send an ALPN extension with protocol indicator `http/1.1` when no _context_ is given. Custom _context_ should set ALPN protocols with [`set_alpn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_alpn_protocols "ssl.SSLContext.set_alpn_protocols").
Changed in version 3.13: Remove _cafile_ , _capath_ and _cadefault_ parameters: use the _context_ parameter instead.

urllib.request.install_opener(_opener_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.install_opener "Link to this definition")

Install an [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector") instance as the default global opener. Installing an opener is only necessary if you want urlopen to use that opener; otherwise, simply call [`OpenerDirector.open()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector.open "urllib.request.OpenerDirector.open") instead of [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen"). The code does not check for a real `OpenerDirector`, and any class with the appropriate interface will work.

urllib.request.build_opener([_handler_ , _..._])[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.build_opener "Link to this definition")

Return an [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector") instance, which chains the handlers in the order given. _handler_ s can be either instances of [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler"), or subclasses of `BaseHandler` (in which case it must be possible to call the constructor without any parameters). Instances of the following classes will be in front of the _handler_ s, unless the _handler_ s contain them, instances of them or subclasses of them: [`ProxyHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyHandler "urllib.request.ProxyHandler") (if proxy settings are detected), [`UnknownHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.UnknownHandler "urllib.request.UnknownHandler"), [`HTTPHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPHandler "urllib.request.HTTPHandler"), [`HTTPDefaultErrorHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPDefaultErrorHandler "urllib.request.HTTPDefaultErrorHandler"), [`HTTPRedirectHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler "urllib.request.HTTPRedirectHandler"), [`FTPHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.FTPHandler "urllib.request.FTPHandler"), [`FileHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.FileHandler "urllib.request.FileHandler"), [`HTTPErrorProcessor`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPErrorProcessor "urllib.request.HTTPErrorProcessor").
If the Python installation has SSL support (i.e., if the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects") module can be imported), [`HTTPSHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPSHandler "urllib.request.HTTPSHandler") will also be added.
A [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler") subclass may also change its `handler_order` attribute to modify its position in the handlers list.

urllib.request.pathname2url(_path_ , _*_ , _add_scheme =False_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.pathname2url "Link to this definition")

Convert the given local path to a `file:` URL. This function uses [`quote()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote "urllib.parse.quote") function to encode the path.
If _add_scheme_ is false (the default), the return value omits the `file:` scheme prefix. Set _add_scheme_ to true to return a complete URL.
This example shows the function being used on Windows:
Copy```
>>> from urllib.request import pathname2url
>>> path = 'C:\\Program Files'
>>> pathname2url(path, add_scheme=True)
'file:///C:/Program%20Files'

```

Changed in version 3.14: Windows drive letters are no longer converted to uppercase, and `:` characters not following a drive letter no longer cause an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception to be raised on Windows.
Changed in version 3.14: Paths beginning with a slash are converted to URLs with authority sections. For example, the path `/etc/hosts` is converted to the URL `///etc/hosts`.
Changed in version 3.14: The _add_scheme_ parameter was added.

urllib.request.url2pathname(_url_ , _*_ , _require_scheme =False_, _resolve_host =False_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.url2pathname "Link to this definition")

Convert the given `file:` URL to a local path. This function uses [`unquote()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.unquote "urllib.parse.unquote") to decode the URL.
If _require_scheme_ is false (the default), the given value should omit a `file:` scheme prefix. If _require_scheme_ is set to true, the given value should include the prefix; a [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError") is raised if it doesn’t.
The URL authority is discarded if it is empty, `localhost`, or the local hostname. Otherwise, if _resolve_host_ is set to true, the authority is resolved using [`socket.gethostbyname()`](https://docs.python.org/3/library/socket.html#socket.gethostbyname "socket.gethostbyname") and discarded if it matches a local IP address (as per [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError") is raised.
This example shows the function being used on Windows:
Copy```
>>> from urllib.request import url2pathname
>>> url = 'file:///C:/Program%20Files'
>>> url2pathname(url, require_scheme=True)
'C:\\Program Files'

```

Changed in version 3.14: Windows drive letters are no longer converted to uppercase, and `:` characters not following a drive letter no longer cause an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") exception to be raised on Windows.
Changed in version 3.14: The URL authority is discarded if it matches the local hostname. Otherwise, if the authority isn’t empty or `localhost`, then on Windows a UNC path is returned (as before), and on other platforms a [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError") is raised.
Changed in version 3.14: The URL query and fragment components are discarded if present.
Changed in version 3.14: The _require_scheme_ and _resolve_host_ parameters were added.

urllib.request.getproxies()[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.getproxies "Link to this definition")

This helper function returns a dictionary of scheme to proxy server URL mappings. It scans the environment for variables named `<scheme>_proxy`, in a case insensitive approach, for all operating systems first, and when it cannot find it, looks for proxy information from System Configuration for macOS and Windows Systems Registry for Windows. If both lowercase and uppercase environment variables exist (and disagree), lowercase is preferred.
Note
If the environment variable `REQUEST_METHOD` is set, which usually indicates your script is running in a CGI environment, the environment variable `HTTP_PROXY` (uppercase `_PROXY`) will be ignored. This is because that variable can be injected by a client using the “Proxy:” HTTP header. If you need to use an HTTP proxy in a CGI environment, either use `ProxyHandler` explicitly, or make sure the variable name is in lowercase (or at least the `_proxy` suffix).
The following classes are provided:

_class_ urllib.request.Request(_url_ , _data =None_, _headers ={}_, _origin_req_host =None_, _unverifiable =False_, _method =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "Link to this definition")

This class is an abstraction of a URL request.
_url_ should be a string containing a valid, properly encoded URL.
_data_ must be an object specifying additional data to send to the server, or `None` if no such data is needed. Currently HTTP requests are the only ones that use _data_. The supported object types include bytes, file-like objects, and iterables of bytes-like objects. If no `Content-Length` nor `Transfer-Encoding` header field has been provided, [`HTTPHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPHandler "urllib.request.HTTPHandler") will set these headers according to the type of _data_. `Content-Length` will be used to send bytes objects, while `Transfer-Encoding: chunked` as specified in
For an HTTP POST request method, _data_ should be a buffer in the standard _application/x-www-form-urlencoded_ format. The [`urllib.parse.urlencode()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode "urllib.parse.urlencode") function takes a mapping or sequence of 2-tuples and returns an ASCII string in this format. It should be encoded to bytes before being used as the _data_ parameter.
_headers_ should be a dictionary, and will be treated as if [`add_header()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.add_header "urllib.request.Request.add_header") was called with each key and value as arguments. This is often used to “spoof” the `User-Agent` header value, which is used by a browser to identify itself – some HTTP servers only allow requests coming from common browsers as opposed to scripts. For example, Mozilla Firefox may identify itself as `"Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"`, while [`urllib`](https://docs.python.org/3/library/urllib.html#module-urllib "urllib")’s default user agent string is `"Python-urllib/2.6"` (on Python 2.6). All header keys are sent in camel case.
An appropriate `Content-Type` header should be included if the _data_ argument is present. If this header has not been provided and _data_ is not `None`, `Content-Type: application/x-www-form-urlencoded` will be added as a default.
The next two arguments are only of interest for correct handling of third-party HTTP cookies:
_origin_req_host_ should be the request-host of the origin transaction, as defined by `http.cookiejar.request_host(self)`. This is the host name or IP address of the original request that was initiated by the user. For example, if the request is for an image in an HTML document, this should be the request-host of the request for the page containing the image.
_unverifiable_ should indicate whether the request is unverifiable, as defined by `False`. An unverifiable request is one whose URL the user did not have the option to approve. For example, if the request is for an image in an HTML document, and the user had no option to approve the automatic fetching of the image, this should be true.
_method_ should be a string that indicates the HTTP request method that will be used (e.g. `'HEAD'`). If provided, its value is stored in the [`method`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.method "urllib.request.Request.method") attribute and is used by [`get_method()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.get_method "urllib.request.Request.get_method"). The default is `'GET'` if _data_ is `None` or `'POST'` otherwise. Subclasses may indicate a different default method by setting the `method` attribute in the class itself.
Note
The request will not work as expected if the data object is unable to deliver its content more than once (e.g. a file or an iterable that can produce the content only once) and the request is retried for HTTP redirects or authentication. The _data_ is sent to the HTTP server right away after the headers. There is no support for a 100-continue expectation in the library.
Changed in version 3.3: [`Request.method`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.method "urllib.request.Request.method") argument is added to the Request class.
Changed in version 3.4: Default [`Request.method`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.method "urllib.request.Request.method") may be indicated at the class level.
Changed in version 3.6: Do not raise an error if the `Content-Length` has not been provided and _data_ is neither `None` nor a bytes object. Fall back to use chunked transfer encoding instead.

_class_ urllib.request.OpenerDirector[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "Link to this definition")

The `OpenerDirector` class opens URLs via [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler")s chained together. It manages the chaining of handlers, and recovery from errors.

_class_ urllib.request.BaseHandler[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "Link to this definition")

This is the base class for all registered handlers — and handles only the simple mechanics of registration.

_class_ urllib.request.HTTPDefaultErrorHandler[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPDefaultErrorHandler "Link to this definition")

A class which defines a default handler for HTTP error responses; all responses are turned into [`HTTPError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError "urllib.error.HTTPError") exceptions.

_class_ urllib.request.HTTPRedirectHandler[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler "Link to this definition")

A class to handle redirections.

_class_ urllib.request.HTTPCookieProcessor(_cookiejar =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPCookieProcessor "Link to this definition")

A class to handle HTTP Cookies.

_class_ urllib.request.ProxyHandler(_proxies =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyHandler "Link to this definition")

Cause requests to go through a proxy. If _proxies_ is given, it must be a dictionary mapping protocol names to URLs of proxies. The default is to read the list of proxies from the environment variables `<protocol>_proxy`. If no proxy environment variables are set, then in a Windows environment proxy settings are obtained from the registry’s Internet Settings section, and in a macOS environment proxy information is retrieved from the System Configuration Framework.
To disable autodetected proxy pass an empty dictionary.
The `no_proxy` environment variable can be used to specify hosts which shouldn’t be reached via proxy; if set, it should be a comma-separated list of hostname suffixes, optionally with `:port` appended, for example `cern.ch,ncsa.uiuc.edu,some.host:8080`.
Note
`HTTP_PROXY` will be ignored if a variable `REQUEST_METHOD` is set; see the documentation on [`getproxies()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.getproxies "urllib.request.getproxies").

_class_ urllib.request.HTTPPasswordMgr[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr "Link to this definition")

Keep a database of `(realm, uri) -> (user, password)` mappings.

_class_ urllib.request.HTTPPasswordMgrWithDefaultRealm[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithDefaultRealm "Link to this definition")

Keep a database of `(realm, uri) -> (user, password)` mappings. A realm of `None` is considered a catch-all realm, which is searched if no other realm fits.

_class_ urllib.request.HTTPPasswordMgrWithPriorAuth[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithPriorAuth "Link to this definition")

A variant of [`HTTPPasswordMgrWithDefaultRealm`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithDefaultRealm "urllib.request.HTTPPasswordMgrWithDefaultRealm") that also has a database of `uri -> is_authenticated` mappings. Can be used by a BasicAuth handler to determine when to send authentication credentials immediately instead of waiting for a `401` response first.
Added in version 3.5.

_class_ urllib.request.AbstractBasicAuthHandler(_password_mgr =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.AbstractBasicAuthHandler "Link to this definition")

This is a mixin class that helps with HTTP authentication, both to the remote host and to a proxy. _password_mgr_ , if given, should be something that is compatible with [`HTTPPasswordMgr`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr "urllib.request.HTTPPasswordMgr"); refer to section [HTTPPasswordMgr Objects](https://docs.python.org/3/library/urllib.request.html#http-password-mgr) for information on the interface that must be supported. If _passwd_mgr_ also provides `is_authenticated` and `update_authenticated` methods (see [HTTPPasswordMgrWithPriorAuth Objects](https://docs.python.org/3/library/urllib.request.html#http-password-mgr-with-prior-auth)), then the handler will use the `is_authenticated` result for a given URI to determine whether or not to send authentication credentials with the request. If `is_authenticated` returns `True` for the URI, credentials are sent. If `is_authenticated` is `False`, credentials are not sent, and then if a `401` response is received the request is re-sent with the authentication credentials. If authentication succeeds, `update_authenticated` is called to set `is_authenticated` `True` for the URI, so that subsequent requests to the URI or any of its super-URIs will automatically include the authentication credentials.
Added in version 3.5: Added `is_authenticated` support.

_class_ urllib.request.HTTPBasicAuthHandler(_password_mgr =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPBasicAuthHandler "Link to this definition")

Handle authentication with the remote host. _password_mgr_ , if given, should be something that is compatible with [`HTTPPasswordMgr`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr "urllib.request.HTTPPasswordMgr"); refer to section [HTTPPasswordMgr Objects](https://docs.python.org/3/library/urllib.request.html#http-password-mgr) for information on the interface that must be supported. HTTPBasicAuthHandler will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") when presented with a wrong Authentication scheme.

_class_ urllib.request.ProxyBasicAuthHandler(_password_mgr =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyBasicAuthHandler "Link to this definition")

Handle authentication with the proxy. _password_mgr_ , if given, should be something that is compatible with [`HTTPPasswordMgr`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr "urllib.request.HTTPPasswordMgr"); refer to section [HTTPPasswordMgr Objects](https://docs.python.org/3/library/urllib.request.html#http-password-mgr) for information on the interface that must be supported.

_class_ urllib.request.AbstractDigestAuthHandler(_password_mgr =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.AbstractDigestAuthHandler "Link to this definition")

This is a mixin class that helps with HTTP authentication, both to the remote host and to a proxy. _password_mgr_ , if given, should be something that is compatible with [`HTTPPasswordMgr`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr "urllib.request.HTTPPasswordMgr"); refer to section [HTTPPasswordMgr Objects](https://docs.python.org/3/library/urllib.request.html#http-password-mgr) for information on the interface that must be supported.
Changed in version 3.14: Added support for HTTP digest authentication algorithm `SHA-256`.

_class_ urllib.request.HTTPDigestAuthHandler(_password_mgr =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPDigestAuthHandler "Link to this definition")

Handle authentication with the remote host. _password_mgr_ , if given, should be something that is compatible with [`HTTPPasswordMgr`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr "urllib.request.HTTPPasswordMgr"); refer to section [HTTPPasswordMgr Objects](https://docs.python.org/3/library/urllib.request.html#http-password-mgr) for information on the interface that must be supported. When both Digest Authentication Handler and Basic Authentication Handler are both added, Digest Authentication is always tried first. If the Digest Authentication returns a 40x response again, it is sent to Basic Authentication handler to Handle. This Handler method will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") when presented with an authentication scheme other than Digest or Basic.
Changed in version 3.3: Raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") on unsupported Authentication Scheme.

_class_ urllib.request.ProxyDigestAuthHandler(_password_mgr =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.ProxyDigestAuthHandler "Link to this definition")

Handle authentication with the proxy. _password_mgr_ , if given, should be something that is compatible with [`HTTPPasswordMgr`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgr "urllib.request.HTTPPasswordMgr"); refer to section [HTTPPasswordMgr Objects](https://docs.python.org/3/library/urllib.request.html#http-password-mgr) for information on the interface that must be supported.

_class_ urllib.request.HTTPHandler[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPHandler "Link to this definition")

A class to handle opening of HTTP URLs.

_class_ urllib.request.HTTPSHandler(_debuglevel =0_, _context =None_, _check_hostname =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPSHandler "Link to this definition")

A class to handle opening of HTTPS URLs. _context_ and _check_hostname_ have the same meaning as in [`http.client.HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "http.client.HTTPSConnection").
Changed in version 3.2: _context_ and _check_hostname_ were added.

_class_ urllib.request.FileHandler[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.FileHandler "Link to this definition")

Open local files.

_class_ urllib.request.DataHandler[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.DataHandler "Link to this definition")

Open data URLs.
Added in version 3.4.

_class_ urllib.request.FTPHandler[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.FTPHandler "Link to this definition")

Open FTP URLs.

_class_ urllib.request.CacheFTPHandler[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.CacheFTPHandler "Link to this definition")

Open FTP URLs, keeping a cache of open FTP connections to minimize delays.

_class_ urllib.request.UnknownHandler[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.UnknownHandler "Link to this definition")

A catch-all class to handle unknown URLs.

_class_ urllib.request.HTTPErrorProcessor[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPErrorProcessor "Link to this definition")

Process HTTP error responses.
