## AbstractBasicAuthHandler Objects[¶](https://docs.python.org/3/library/urllib.request.html#abstractbasicauthhandler-objects "Link to this heading")

AbstractBasicAuthHandler.http_error_auth_reqed(_authreq_ , _host_ , _req_ , _headers_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.AbstractBasicAuthHandler.http_error_auth_reqed "Link to this definition")

Handle an authentication request by getting a user/password pair, and re-trying the request. _authreq_ should be the name of the header where the information about the realm is included in the request, _host_ specifies the URL and path to authenticate for, _req_ should be the (failed) [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") object, and _headers_ should be the error headers.
_host_ is either an authority (e.g. `"python.org"`) or a URL containing an authority component (e.g. `"http://python.org/"`). In either case, the authority must not contain a userinfo component (so, `"python.org"` and `"python.org:80"` are fine, `"joe:password@python.org"` is not).
