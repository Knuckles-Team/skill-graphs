## OpenerDirector Objects[¶](https://docs.python.org/3/library/urllib.request.html#openerdirector-objects "Link to this heading")
[`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector") instances have the following methods:

OpenerDirector.add_handler(_handler_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector.add_handler "Link to this definition")

_handler_ should be an instance of [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler"). The following methods are searched, and added to the possible chains (note that HTTP errors are a special case). Note that, in the following, _protocol_ should be replaced with the actual protocol to handle, for example `http_response()` would be the HTTP protocol response handler. Also _type_ should be replaced with the actual HTTP code, for example `http_error_404()` would handle HTTP 404 errors.
  * `<protocol>_open()` — signal that the handler knows how to open _protocol_ URLs.
See [`BaseHandler.<protocol>_open()`](https://docs.python.org/3/library/urllib.request.html#protocol-open) for more information.
  * `http_error_<type>()` — signal that the handler knows how to handle HTTP errors with HTTP error code _type_.
See [`BaseHandler.http_error_<nnn>()`](https://docs.python.org/3/library/urllib.request.html#http-error-nnn) for more information.
  * `<protocol>_error()` — signal that the handler knows how to handle errors from (non-`http`) _protocol_.
  * `<protocol>_request()` — signal that the handler knows how to pre-process _protocol_ requests.
See [`BaseHandler.<protocol>_request()`](https://docs.python.org/3/library/urllib.request.html#protocol-request) for more information.
  * `<protocol>_response()` — signal that the handler knows how to post-process _protocol_ responses.
See [`BaseHandler.<protocol>_response()`](https://docs.python.org/3/library/urllib.request.html#protocol-response) for more information.



OpenerDirector.open(_url_ , _data=None_[, _timeout_])[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector.open "Link to this definition")

Open the given _url_ (which can be a request object or a string), optionally passing the given _data_. Arguments, return values and exceptions raised are the same as those of [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") (which simply calls the `open()` method on the currently installed global [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector")). The optional _timeout_ parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used). The timeout feature actually works only for HTTP, HTTPS and FTP connections.

OpenerDirector.error(_proto_ , _* args_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector.error "Link to this definition")

Handle an error of the given protocol. This will call the registered error handlers for the given protocol with the given arguments (which are protocol specific). The HTTP protocol is a special case which uses the HTTP response code to determine the specific error handler; refer to the `http_error_<type>()` methods of the handler classes.
Return values and exceptions raised are the same as those of [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen").
OpenerDirector objects open URLs in three stages:
The order in which these methods are called within each stage is determined by sorting the handler instances.
  1. Every handler with a method named like `<protocol>_request()` has that method called to pre-process the request.
  2. Handlers with a method named like `<protocol>_open()` are called to handle the request. This stage ends when a handler either returns a non-[`None`](https://docs.python.org/3/library/constants.html#None "None") value (ie. a response), or raises an exception (usually [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError")). Exceptions are allowed to propagate.
In fact, the above algorithm is first tried for methods named [`default_open()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.default_open "urllib.request.BaseHandler.default_open"). If all such methods return [`None`](https://docs.python.org/3/library/constants.html#None "None"), the algorithm is repeated for methods named like `<protocol>_open()`. If all such methods return `None`, the algorithm is repeated for methods named [`unknown_open()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.unknown_open "urllib.request.BaseHandler.unknown_open").
Note that the implementation of these methods may involve calls of the parent [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector") instance’s [`open()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector.open "urllib.request.OpenerDirector.open") and [`error()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector.error "urllib.request.OpenerDirector.error") methods.
  3. Every handler with a method named like `<protocol>_response()` has that method called to post-process the response.
