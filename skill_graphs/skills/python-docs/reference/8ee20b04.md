## HTTPErrorProcessor Objects[¶](https://docs.python.org/3/library/urllib.request.html#httperrorprocessor-objects "Link to this heading")

HTTPErrorProcessor.http_response(_request_ , _response_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPErrorProcessor.http_response "Link to this definition")

Process HTTP error responses.
For 200 error codes, the response object is returned immediately.
For non-200 error codes, this simply passes the job on to the `http_error_<type>()` handler methods, via [`OpenerDirector.error()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.OpenerDirector.error "urllib.request.OpenerDirector.error"). Eventually, [`HTTPDefaultErrorHandler`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPDefaultErrorHandler "urllib.request.HTTPDefaultErrorHandler") will raise an [`HTTPError`](https://docs.python.org/3/library/urllib.error.html#urllib.error.HTTPError "urllib.error.HTTPError") if no other handler handles the error.

HTTPErrorProcessor.https_response(_request_ , _response_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPErrorProcessor.https_response "Link to this definition")

Process HTTPS error responses.
The behavior is same as [`http_response()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPErrorProcessor.http_response "urllib.request.HTTPErrorProcessor.http_response").
