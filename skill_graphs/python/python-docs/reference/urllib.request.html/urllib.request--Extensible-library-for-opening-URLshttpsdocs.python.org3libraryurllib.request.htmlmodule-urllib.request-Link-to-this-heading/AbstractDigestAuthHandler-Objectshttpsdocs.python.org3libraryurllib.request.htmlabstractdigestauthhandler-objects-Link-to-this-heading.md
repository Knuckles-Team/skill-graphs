## AbstractDigestAuthHandler Objects[¶](https://docs.python.org/3/library/urllib.request.html#abstractdigestauthhandler-objects "Link to this heading")

AbstractDigestAuthHandler.http_error_auth_reqed(_authreq_ , _host_ , _req_ , _headers_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.AbstractDigestAuthHandler.http_error_auth_reqed "Link to this definition")

_authreq_ should be the name of the header where the information about the realm is included in the request, _host_ should be the host to authenticate to, _req_ should be the (failed) [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") object, and _headers_ should be the error headers.
