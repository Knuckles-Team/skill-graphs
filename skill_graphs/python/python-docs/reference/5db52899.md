## BaseHandler Objects[¶](https://docs.python.org/3/library/urllib.request.html#basehandler-objects "Link to this heading")
[`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler") objects provide a couple of methods that are directly useful, and others that are meant to be used by derived classes. These are intended for direct use:

BaseHandler.add_parent(_director_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.add_parent "Link to this definition")

Add a director as parent.

BaseHandler.close()[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.close "Link to this definition")

Remove any parents.
The following attribute and methods should only be used by classes derived from [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler").
Note
The convention has been adopted that subclasses defining `<protocol>_request()` or `<protocol>_response()` methods are named `*Processor`; all others are named `*Handler`.

BaseHandler.parent[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.parent "Link to this definition")

A valid [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector"), which can be used to open using a different protocol, or handle errors.

BaseHandler.default_open(_req_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.default_open "Link to this definition")

This method is _not_ defined in [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler"), but subclasses should define it if they want to catch all URLs.
This method, if implemented, will be called by the parent [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector"). It should return a file-like object as described in the return value of the [`open()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector.open "urllib.request.OpenerDirector.open") method of `OpenerDirector`, or `None`. It should raise [`URLError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.URLError "urllib.error.URLError"), unless a truly exceptional thing happens (for example, [`MemoryError`](https://docs.python.org/3/library/exceptions.html#MemoryError "MemoryError") should not be mapped to `URLError`).
This method will be called before any protocol-specific open method.

BaseHandler.<protocol>_open(req)

This method is _not_ defined in [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler"), but subclasses should define it if they want to handle URLs with the given protocol.
This method, if defined, will be called by the parent [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector"). Return values should be the same as for [`default_open()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.default_open "urllib.request.BaseHandler.default_open").

BaseHandler.unknown_open(_req_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.unknown_open "Link to this definition")

This method is _not_ defined in [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler"), but subclasses should define it if they want to catch all URLs with no specific registered handler to open it.
This method, if implemented, will be called by the [`parent`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.parent "urllib.request.BaseHandler.parent") [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector"). Return values should be the same as for [`default_open()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.default_open "urllib.request.BaseHandler.default_open").

BaseHandler.http_error_default(_req_ , _fp_ , _code_ , _msg_ , _hdrs_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.http_error_default "Link to this definition")

This method is _not_ defined in [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler"), but subclasses should override it if they intend to provide a catch-all for otherwise unhandled HTTP errors. It will be called automatically by the [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector") getting the error, and should not normally be called in other circumstances.
[`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector") will call this method with five positional arguments:
  1. a [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") object,
  2. a file-like object with the HTTP error body,
  3. the three-digit code of the error, as a string,
  4. the user-visible explanation of the code, as a string, and
  5. the headers of the error, as a mapping object.


Return values and exceptions raised should be the same as those of [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen").

BaseHandler.http_error_<nnn>(req, fp, code, msg, hdrs)

_nnn_ should be a three-digit HTTP error code. This method is also not defined in [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler"), but will be called, if it exists, on an instance of a subclass, when an HTTP error with code _nnn_ occurs.
Subclasses should override this method to handle specific HTTP errors.
Arguments, return values and exceptions raised should be the same as for [`http_error_default()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler.http_error_default "urllib.request.BaseHandler.http_error_default").

BaseHandler.<protocol>_request(req)

This method is _not_ defined in [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler"), but subclasses should define it if they want to pre-process requests of the given protocol.
This method, if defined, will be called by the parent [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector"). _req_ will be a [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") object. The return value should be a `Request` object.

BaseHandler.<protocol>_response(req, response)

This method is _not_ defined in [`BaseHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.BaseHandler "urllib.request.BaseHandler"), but subclasses should define it if they want to post-process responses of the given protocol.
This method, if defined, will be called by the parent [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector"). _req_ will be a [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") object. _response_ will be an object implementing the same interface as the return value of [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen"). The return value should implement the same interface as the return value of `urlopen()`.
