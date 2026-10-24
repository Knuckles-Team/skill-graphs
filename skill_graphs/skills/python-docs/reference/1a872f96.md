## HTTPRedirectHandler Objects[¶](https://docs.python.org/3/library/urllib.request.html#httpredirecthandler-objects "Link to this heading")
Note
Some HTTP redirections require action from this module’s client code. If this is the case, [`HTTPError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError "urllib.error.HTTPError") is raised. See
An [`HTTPError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError "urllib.error.HTTPError") exception raised as a security consideration if the HTTPRedirectHandler is presented with a redirected URL which is not an HTTP, HTTPS or FTP URL.

HTTPRedirectHandler.redirect_request(_req_ , _fp_ , _code_ , _msg_ , _hdrs_ , _newurl_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler.redirect_request "Link to this definition")

Return a [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") or `None` in response to a redirect. This is called by the default implementations of the `http_error_30*()` methods when a redirection is received from the server. If a redirection should take place, return a new `Request` to allow `http_error_30*()` to perform the redirect to _newurl_. Otherwise, raise [`HTTPError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError "urllib.error.HTTPError") if no other handler should try to handle this URL, or return `None` if you can’t but another handler might.
Note
The default implementation of this method does not strictly follow `POST` requests must not be automatically redirected without confirmation by the user. In reality, browsers do allow automatic redirection of these responses, changing the POST to a `GET`, and the default implementation reproduces this behavior.

HTTPRedirectHandler.http_error_301(_req_ , _fp_ , _code_ , _msg_ , _hdrs_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler.http_error_301 "Link to this definition")

Redirect to the `Location:` or `URI:` URL. This method is called by the parent [`OpenerDirector`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector "urllib.request.OpenerDirector") when getting an HTTP ‘moved permanently’ response.

HTTPRedirectHandler.http_error_302(_req_ , _fp_ , _code_ , _msg_ , _hdrs_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler.http_error_302 "Link to this definition")

The same as [`http_error_301()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler.http_error_301 "urllib.request.HTTPRedirectHandler.http_error_301"), but called for the ‘found’ response.

HTTPRedirectHandler.http_error_303(_req_ , _fp_ , _code_ , _msg_ , _hdrs_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler.http_error_303 "Link to this definition")

The same as [`http_error_301()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler.http_error_301 "urllib.request.HTTPRedirectHandler.http_error_301"), but called for the ‘see other’ response.

HTTPRedirectHandler.http_error_307(_req_ , _fp_ , _code_ , _msg_ , _hdrs_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler.http_error_307 "Link to this definition")

The same as [`http_error_301()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler.http_error_301 "urllib.request.HTTPRedirectHandler.http_error_301"), but called for the ‘temporary redirect’ response. It does not allow changing the request method from `POST` to `GET`.

HTTPRedirectHandler.http_error_308(_req_ , _fp_ , _code_ , _msg_ , _hdrs_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler.http_error_308 "Link to this definition")

The same as [`http_error_301()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPRedirectHandler.http_error_301 "urllib.request.HTTPRedirectHandler.http_error_301"), but called for the ‘permanent redirect’ response. It does not allow changing the request method from `POST` to `GET`.
Added in version 3.11.
