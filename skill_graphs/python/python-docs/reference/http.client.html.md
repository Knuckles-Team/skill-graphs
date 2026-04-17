[ ![Python logo](https://docs.python.org/3/_static/py.svg) ](https://www.python.org/) 3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
Theme  Auto Light Dark
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`http.client` — HTTP protocol client](https://docs.python.org/3/library/http.client.html)
    * [HTTPConnection Objects](https://docs.python.org/3/library/http.client.html#httpconnection-objects)
    * [HTTPResponse Objects](https://docs.python.org/3/library/http.client.html#httpresponse-objects)
    * [Examples](https://docs.python.org/3/library/http.client.html#examples)
    * [HTTPMessage Objects](https://docs.python.org/3/library/http.client.html#httpmessage-objects)


#### Previous topic
[`http` — HTTP modules](https://docs.python.org/3/library/http.html "previous chapter")
#### Next topic
[`ftplib` — FTP protocol client](https://docs.python.org/3/library/ftplib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=http.client+%E2%80%94+HTTP+protocol+client&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.client.html&pagesource=library%2Fhttp.client.rst)


### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ftplib.html "ftplib — FTP protocol client") |
  * [previous](https://docs.python.org/3/library/http.html "http — HTTP modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`http.client` — HTTP protocol client](https://docs.python.org/3/library/http.client.html)
  * |
  * Theme  Auto Light Dark |


#  `http.client` — HTTP protocol client[¶](https://docs.python.org/3/library/http.client.html#module-http.client "Link to this heading")
**Source code:**
* * *
This module defines classes that implement the client side of the HTTP and HTTPS protocols. It is normally not used directly — the module [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.") uses it to handle URLs that use HTTP and HTTPS.
See also
The
Note
HTTPS support is only available if Python was compiled with SSL support (through the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects") module).
[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.
This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.
The module provides the following classes:

_class_ http.client.HTTPConnection(_host_ , _port=None_ , [_timeout_ , ]_source_address=None_ , _blocksize=8192_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection "Link to this definition")

An `HTTPConnection` instance represents one transaction with an HTTP server. It should be instantiated by passing it a host and optional port number. If no port number is passed, the port is extracted from the host string if it has the form `host:port`, else the default HTTP port (80) is used. If the optional _timeout_ parameter is given, blocking operations (like connection attempts) will timeout after that many seconds (if it is not given, the global default timeout setting is used). The optional _source_address_ parameter may be a tuple of a (host, port) to use as the source address the HTTP connection is made from. The optional _blocksize_ parameter sets the buffer size in bytes for sending a file-like message body.
For example, the following calls all create instances that connect to the server at the same host and port:
Copy```
>>> h1 = http.client.HTTPConnection('www.python.org')
>>> h2 = http.client.HTTPConnection('www.python.org:80')
>>> h3 = http.client.HTTPConnection('www.python.org', 80)
>>> h4 = http.client.HTTPConnection('www.python.org', 80, timeout=10)

```

Changed in version 3.2: _source_address_ was added.
Changed in version 3.4: The _strict_ parameter was removed. HTTP 0.9-style “Simple Responses” are no longer supported.
Changed in version 3.7: _blocksize_ parameter was added.

_class_ http.client.HTTPSConnection(_host_ , _port=None_ , _*_ , [_timeout_ , ]_source_address=None_ , _context=None_ , _blocksize=8192_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "Link to this definition")

A subclass of [`HTTPConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection "http.client.HTTPConnection") that uses SSL for communication with secure servers. Default port is `443`. If _context_ is specified, it must be a [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") instance describing the various SSL options.
Please read [Security considerations](https://docs.python.org/3/library/ssl.html#ssl-security) for more information on best practices.
Changed in version 3.2: _source_address_ , _context_ and _check_hostname_ were added.
Changed in version 3.2: This class now supports HTTPS virtual hosts if possible (that is, if [`ssl.HAS_SNI`](https://docs.python.org/3/library/ssl.html#ssl.HAS_SNI "ssl.HAS_SNI") is true).
Changed in version 3.4: The _strict_ parameter was removed. HTTP 0.9-style “Simple Responses” are no longer supported.
Changed in version 3.4.3: This class now performs all the necessary certificate and hostname checks by default. To revert to the previous, unverified, behavior `ssl._create_unverified_context()` can be passed to the _context_ parameter.
Changed in version 3.8: This class now enables TLS 1.3 [`ssl.SSLContext.post_handshake_auth`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.post_handshake_auth "ssl.SSLContext.post_handshake_auth") for the default _context_ or when _cert_file_ is passed with a custom _context_.
Changed in version 3.10: This class now sends an ALPN extension with protocol indicator `http/1.1` when no _context_ is given. Custom _context_ should set ALPN protocols with [`set_alpn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_alpn_protocols "ssl.SSLContext.set_alpn_protocols").
Changed in version 3.12: The deprecated _key_file_ , _cert_file_ and _check_hostname_ parameters have been removed.

_class_ http.client.HTTPResponse(_sock_ , _debuglevel =0_, _method =None_, _url =None_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse "Link to this definition")

Class whose instances are returned upon successful connection. Not instantiated directly by user.
Changed in version 3.4: The _strict_ parameter was removed. HTTP 0.9 style “Simple Responses” are no longer supported.
This module provides the following function:

http.client.parse_headers(_fp_)[¶](https://docs.python.org/3/library/http.client.html#http.client.parse_headers "Link to this definition")

Parse the headers from a file pointer _fp_ representing a HTTP request/response. The file has to be a [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") reader (i.e. not text) and must provide a valid
This function returns an instance of [`http.client.HTTPMessage`](https://docs.python.org/3/library/http.client.html#http.client.HTTPMessage "http.client.HTTPMessage") that holds the header fields, but no payload (the same as [`HTTPResponse.msg`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.msg "http.client.HTTPResponse.msg") and [`http.server.BaseHTTPRequestHandler.headers`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.headers "http.server.BaseHTTPRequestHandler.headers")). After returning, the file pointer _fp_ is ready to read the HTTP body.
Note
[`parse_headers()`](https://docs.python.org/3/library/http.client.html#http.client.parse_headers "http.client.parse_headers") does not parse the start-line of a HTTP message; it only parses the `Name: value` lines. The file has to be ready to read these field lines, so the first line should already be consumed before calling the function.
The following exceptions are raised as appropriate:

_exception_ http.client.HTTPException[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPException "Link to this definition")

The base class of the other exceptions in this module. It is a subclass of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception").

_exception_ http.client.NotConnected[¶](https://docs.python.org/3/library/http.client.html#http.client.NotConnected "Link to this definition")

A subclass of [`HTTPException`](https://docs.python.org/3/library/http.client.html#http.client.HTTPException "http.client.HTTPException").

_exception_ http.client.InvalidURL[¶](https://docs.python.org/3/library/http.client.html#http.client.InvalidURL "Link to this definition")

A subclass of [`HTTPException`](https://docs.python.org/3/library/http.client.html#http.client.HTTPException "http.client.HTTPException"), raised if a port is given and is either non-numeric or empty.

_exception_ http.client.UnknownProtocol[¶](https://docs.python.org/3/library/http.client.html#http.client.UnknownProtocol "Link to this definition")

A subclass of [`HTTPException`](https://docs.python.org/3/library/http.client.html#http.client.HTTPException "http.client.HTTPException").

_exception_ http.client.UnknownTransferEncoding[¶](https://docs.python.org/3/library/http.client.html#http.client.UnknownTransferEncoding "Link to this definition")

A subclass of [`HTTPException`](https://docs.python.org/3/library/http.client.html#http.client.HTTPException "http.client.HTTPException").

_exception_ http.client.UnimplementedFileMode[¶](https://docs.python.org/3/library/http.client.html#http.client.UnimplementedFileMode "Link to this definition")

A subclass of [`HTTPException`](https://docs.python.org/3/library/http.client.html#http.client.HTTPException "http.client.HTTPException").

_exception_ http.client.IncompleteRead[¶](https://docs.python.org/3/library/http.client.html#http.client.IncompleteRead "Link to this definition")

A subclass of [`HTTPException`](https://docs.python.org/3/library/http.client.html#http.client.HTTPException "http.client.HTTPException").

_exception_ http.client.ImproperConnectionState[¶](https://docs.python.org/3/library/http.client.html#http.client.ImproperConnectionState "Link to this definition")

A subclass of [`HTTPException`](https://docs.python.org/3/library/http.client.html#http.client.HTTPException "http.client.HTTPException").

_exception_ http.client.CannotSendRequest[¶](https://docs.python.org/3/library/http.client.html#http.client.CannotSendRequest "Link to this definition")

A subclass of [`ImproperConnectionState`](https://docs.python.org/3/library/http.client.html#http.client.ImproperConnectionState "http.client.ImproperConnectionState").

_exception_ http.client.CannotSendHeader[¶](https://docs.python.org/3/library/http.client.html#http.client.CannotSendHeader "Link to this definition")

A subclass of [`ImproperConnectionState`](https://docs.python.org/3/library/http.client.html#http.client.ImproperConnectionState "http.client.ImproperConnectionState").

_exception_ http.client.ResponseNotReady[¶](https://docs.python.org/3/library/http.client.html#http.client.ResponseNotReady "Link to this definition")

A subclass of [`ImproperConnectionState`](https://docs.python.org/3/library/http.client.html#http.client.ImproperConnectionState "http.client.ImproperConnectionState").

_exception_ http.client.BadStatusLine[¶](https://docs.python.org/3/library/http.client.html#http.client.BadStatusLine "Link to this definition")

A subclass of [`HTTPException`](https://docs.python.org/3/library/http.client.html#http.client.HTTPException "http.client.HTTPException"). Raised if a server responds with a HTTP status code that we don’t understand.

_exception_ http.client.LineTooLong[¶](https://docs.python.org/3/library/http.client.html#http.client.LineTooLong "Link to this definition")

A subclass of [`HTTPException`](https://docs.python.org/3/library/http.client.html#http.client.HTTPException "http.client.HTTPException"). Raised if an excessively long line is received in the HTTP protocol from the server.

_exception_ http.client.RemoteDisconnected[¶](https://docs.python.org/3/library/http.client.html#http.client.RemoteDisconnected "Link to this definition")

A subclass of [`ConnectionResetError`](https://docs.python.org/3/library/exceptions.html#ConnectionResetError "ConnectionResetError") and [`BadStatusLine`](https://docs.python.org/3/library/http.client.html#http.client.BadStatusLine "http.client.BadStatusLine"). Raised by [`HTTPConnection.getresponse()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.getresponse "http.client.HTTPConnection.getresponse") when the attempt to read the response results in no data read from the connection, indicating that the remote end has closed the connection.
Added in version 3.5: Previously, [`BadStatusLine`](https://docs.python.org/3/library/http.client.html#http.client.BadStatusLine "http.client.BadStatusLine")`('')` was raised.
The constants defined in this module are:

http.client.HTTP_PORT[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTP_PORT "Link to this definition")

The default port for the HTTP protocol (always `80`).

http.client.HTTPS_PORT[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPS_PORT "Link to this definition")

The default port for the HTTPS protocol (always `443`).

http.client.responses[¶](https://docs.python.org/3/library/http.client.html#http.client.responses "Link to this definition")

This dictionary maps the HTTP 1.1 status codes to the W3C names.
Example: `http.client.responses[http.client.NOT_FOUND]` is `'Not Found'`.
See [HTTP status codes](https://docs.python.org/3/library/http.html#http-status-codes) for a list of HTTP status codes that are available in this module as constants.
## HTTPConnection Objects[¶](https://docs.python.org/3/library/http.client.html#httpconnection-objects "Link to this heading")
[`HTTPConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection "http.client.HTTPConnection") instances have the following methods:

HTTPConnection.request(_method_ , _url_ , _body =None_, _headers ={}_, _*_ , _encode_chunked =False_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.request "Link to this definition")

This will send a request to the server using the HTTP request method _method_ and the request URI _url_. The provided _url_ must be an absolute path to conform with `OPTIONS` or `CONNECT` methods).
If _body_ is specified, the specified data is sent after the headers are finished. It may be a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object), an open [file object](https://docs.python.org/3/glossary.html#term-file-object), or an iterable of [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). If _body_ is a string, it is encoded as ISO-8859-1, the default for HTTP. If it is a bytes-like object, the bytes are sent as is. If it is a file object, the contents of the file is sent; this file object should support at least the `read()` method. If the file object is an instance of [`io.TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase"), the data returned by the `read()` method will be encoded as ISO-8859-1, otherwise the data returned by `read()` is sent as is. If _body_ is an iterable, the elements of the iterable are sent as is until the iterable is exhausted.
The _headers_ argument should be a mapping of extra HTTP headers to send with the request. A `OPTIONS` or `CONNECT` methods).
If _headers_ contains neither Content-Length nor Transfer-Encoding, but there is a request body, one of those header fields will be added automatically. If _body_ is `None`, the Content-Length header is set to `0` for methods that expect a body (`PUT`, `POST`, and `PATCH`). If _body_ is a string or a bytes-like object that is not also a [file](https://docs.python.org/3/glossary.html#term-file-object), the Content-Length header is set to its length. Any other type of _body_ (files and iterables in general) will be chunk-encoded, and the Transfer-Encoding header will automatically be set instead of Content-Length.
The _encode_chunked_ argument is only relevant if Transfer-Encoding is specified in _headers_. If _encode_chunked_ is `False`, the HTTPConnection object assumes that all encoding is handled by the calling code. If it is `True`, the body will be chunk-encoded.
For example, to perform a `GET` request to `https://docs.python.org/3/`:
Copy```
>>> import http.client
>>> host = "docs.python.org"
>>> conn = http.client.HTTPSConnection(host)
>>> conn.request("GET", "/3/", headers={"Host": host})
>>> response = conn.getresponse()
>>> print(response.status, response.reason)
200 OK

```

Note
Chunked transfer encoding has been added to the HTTP protocol version 1.1. Unless the HTTP server is known to handle HTTP 1.1, the caller must either specify the Content-Length, or must pass a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or bytes-like object that is not also a file as the body representation.
Note
Note that you must have read the whole response or call [`close()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.close "http.client.HTTPConnection.close") if [`getresponse()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.getresponse "http.client.HTTPConnection.getresponse") raised an non-[`ConnectionError`](https://docs.python.org/3/library/exceptions.html#ConnectionError "ConnectionError") exception before you can send a new request to the server.
Changed in version 3.2: _body_ can now be an iterable.
Changed in version 3.6: If neither Content-Length nor Transfer-Encoding are set in _headers_ , file and iterable _body_ objects are now chunk-encoded. The _encode_chunked_ argument was added. No attempt is made to determine the Content-Length for file objects.

HTTPConnection.getresponse()[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.getresponse "Link to this definition")

Should be called after a request is sent to get the response from the server. Returns an [`HTTPResponse`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse "http.client.HTTPResponse") instance.
Changed in version 3.5: If a [`ConnectionError`](https://docs.python.org/3/library/exceptions.html#ConnectionError "ConnectionError") or subclass is raised, the [`HTTPConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection "http.client.HTTPConnection") object will be ready to reconnect when a new request is sent.
Note that this does not apply to [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError")s raised by the underlying socket. Instead the caller is responsible to call [`close()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.close "http.client.HTTPConnection.close") on the existing connection.

HTTPConnection.set_debuglevel(_level_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.set_debuglevel "Link to this definition")

Set the debugging level. The default debug level is `0`, meaning no debugging output is printed. Any value greater than `0` will cause all currently defined debug output to be printed to stdout. The `debuglevel` is passed to any new [`HTTPResponse`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse "http.client.HTTPResponse") objects that are created.
Added in version 3.1.

HTTPConnection.set_tunnel(_host_ , _port =None_, _headers =None_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.set_tunnel "Link to this definition")

Set the host and the port for HTTP Connect Tunnelling. This allows running the connection through a proxy server.
The _host_ and _port_ arguments specify the endpoint of the tunneled connection (i.e. the address included in the CONNECT request, _not_ the address of the proxy server).
The _headers_ argument should be a mapping of extra HTTP headers to send with the CONNECT request.
As HTTP/1.1 is used for HTTP CONNECT tunnelling request, `Host:` header must be provided, matching the authority-form of the request target provided as the destination for the CONNECT request. If a HTTP `Host:` header is not provided via the headers argument, one is generated and transmitted automatically.
For example, to tunnel through a HTTPS proxy server running locally on port 8080, we would pass the address of the proxy to the [`HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "http.client.HTTPSConnection") constructor, and the address of the host that we eventually want to reach to the `set_tunnel()` method:
Copy```
>>> import http.client
>>> conn = http.client.HTTPSConnection("localhost", 8080)
>>> conn.set_tunnel("www.python.org")
>>> conn.request("HEAD","/index.html")

```

Added in version 3.2.
Changed in version 3.12: HTTP CONNECT tunnelling requests use protocol HTTP/1.1, upgraded from protocol HTTP/1.0. `Host:` HTTP headers are mandatory for HTTP/1.1, so one will be automatically generated and transmitted if not provided in the headers argument.

HTTPConnection.get_proxy_response_headers()[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.get_proxy_response_headers "Link to this definition")

Returns a dictionary with the headers of the response received from the proxy server to the CONNECT request.
If the CONNECT request was not sent, the method returns `None`.
Added in version 3.12.

HTTPConnection.connect()[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.connect "Link to this definition")

Connect to the server specified when the object was created. By default, this is called automatically when making a request if the client does not already have a connection.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `http.client.connect` with arguments `self`, `host`, `port`.

HTTPConnection.close()[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.close "Link to this definition")

Close the connection to the server.

HTTPConnection.blocksize[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.blocksize "Link to this definition")

Buffer size in bytes for sending a file-like message body.
Added in version 3.7.
As an alternative to using the [`request()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.request "http.client.HTTPConnection.request") method described above, you can also send your request step by step, by using the four functions below.

HTTPConnection.putrequest(_method_ , _url_ , _skip_host =False_, _skip_accept_encoding =False_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.putrequest "Link to this definition")

This should be the first call after the connection to the server has been made. It sends a line to the server consisting of the _method_ string, the _url_ string, and the HTTP version (`HTTP/1.1`). To disable automatic sending of `Host:` or `Accept-Encoding:` headers (for example to accept additional content encodings), specify _skip_host_ or _skip_accept_encoding_ with non-False values.

HTTPConnection.putheader(_header_ , _argument_[, _..._])[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.putheader "Link to this definition")

Send an

HTTPConnection.endheaders(_message_body =None_, _*_ , _encode_chunked =False_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.endheaders "Link to this definition")

Send a blank line to the server, signalling the end of the headers. The optional _message_body_ argument can be used to pass a message body associated with the request.
If _encode_chunked_ is `True`, the result of each iteration of _message_body_ will be chunk-encoded as specified in _message_body_. If _message_body_ implements the [buffer interface](https://docs.python.org/3/c-api/buffer.html#bufferobjects) the encoding will result in a single chunk. If _message_body_ is a [`collections.abc.Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable"), each iteration of _message_body_ will result in a chunk. If _message_body_ is a [file object](https://docs.python.org/3/glossary.html#term-file-object), each call to `.read()` will result in a chunk. The method automatically signals the end of the chunk-encoded data immediately after _message_body_.
Note
Due to the chunked encoding specification, empty chunks yielded by an iterator body will be ignored by the chunk-encoder. This is to avoid premature termination of the read of the request by the target server due to malformed encoding.
Changed in version 3.6: Added chunked encoding support and the _encode_chunked_ parameter.

HTTPConnection.send(_data_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.send "Link to this definition")

Send data to the server. This should be used directly only after the [`endheaders()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.endheaders "http.client.HTTPConnection.endheaders") method has been called and before [`getresponse()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.getresponse "http.client.HTTPConnection.getresponse") is called.
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `http.client.send` with arguments `self`, `data`.
## HTTPResponse Objects[¶](https://docs.python.org/3/library/http.client.html#httpresponse-objects "Link to this heading")
An [`HTTPResponse`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse "http.client.HTTPResponse") instance wraps the HTTP response from the server. It provides access to the request headers and the entity body. The response is an iterable object and can be used in a with statement.
Changed in version 3.5: The [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") interface is now implemented and all of its reader operations are supported.

HTTPResponse.read([_amt_])[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.read "Link to this definition")

Reads and returns the response body, or up to the next _amt_ bytes.

HTTPResponse.readinto(_b_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.readinto "Link to this definition")

Reads up to the next len(b) bytes of the response body into the buffer _b_. Returns the number of bytes read.
Added in version 3.3.

HTTPResponse.getheader(_name_ , _default =None_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.getheader "Link to this definition")

Return the value of the header _name_ , or _default_ if there is no header matching _name_. If there is more than one header with the name _name_ , return all of the values joined by ‘, ‘. If _default_ is any iterable other than a single string, its elements are similarly returned joined by commas.

HTTPResponse.getheaders()[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.getheaders "Link to this definition")

Return a list of (header, value) tuples.

HTTPResponse.fileno()[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.fileno "Link to this definition")

Return the `fileno` of the underlying socket.

HTTPResponse.msg[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.msg "Link to this definition")

A [`http.client.HTTPMessage`](https://docs.python.org/3/library/http.client.html#http.client.HTTPMessage "http.client.HTTPMessage") instance containing the response headers. `http.client.HTTPMessage` is a subclass of [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message").

HTTPResponse.version[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.version "Link to this definition")

HTTP protocol version used by server. 10 for HTTP/1.0, 11 for HTTP/1.1.

HTTPResponse.url[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.url "Link to this definition")

URL of the resource retrieved, commonly used to determine if a redirect was followed.

HTTPResponse.headers[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.headers "Link to this definition")

Headers of the response in the form of an [`email.message.EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage") instance.

HTTPResponse.status[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.status "Link to this definition")

Status code returned by server.

HTTPResponse.reason[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.reason "Link to this definition")

Reason phrase returned by server.

HTTPResponse.debuglevel[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.debuglevel "Link to this definition")

A debugging hook. If [`debuglevel`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.debuglevel "http.client.HTTPResponse.debuglevel") is greater than zero, messages will be printed to stdout as the response is read and parsed.

HTTPResponse.closed[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.closed "Link to this definition")

Is `True` if the stream is closed.

HTTPResponse.geturl()[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.geturl "Link to this definition")

Deprecated since version 3.9: Deprecated in favor of [`url`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.url "http.client.HTTPResponse.url").

HTTPResponse.info()[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.info "Link to this definition")

Deprecated since version 3.9: Deprecated in favor of [`headers`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.headers "http.client.HTTPResponse.headers").

HTTPResponse.getcode()[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.getcode "Link to this definition")

Deprecated since version 3.9: Deprecated in favor of [`status`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.status "http.client.HTTPResponse.status").
## Examples[¶](https://docs.python.org/3/library/http.client.html#examples "Link to this heading")
Here is an example session that uses the `GET` method:
Copy```
>>> import http.client
>>> conn = http.client.HTTPSConnection("www.python.org")
>>> conn.request("GET", "/")
>>> r1 = conn.getresponse()
>>> print(r1.status, r1.reason)
200 OK
>>> data1 = r1.read()  # This will return entire content.
>>> # The following example demonstrates reading data in chunks.
>>> conn.request("GET", "/")
>>> r1 = conn.getresponse()
>>> while chunk := r1.read(200):
...     print(repr(chunk))
b'<!doctype html>\n<!--[if"...
...
>>> # Example of an invalid request
>>> conn = http.client.HTTPSConnection("docs.python.org")
>>> conn.request("GET", "/parrot.spam")
>>> r2 = conn.getresponse()
>>> print(r2.status, r2.reason)
404 Not Found
>>> data2 = r2.read()
>>> conn.close()

```

Here is an example session that uses the `HEAD` method. Note that the `HEAD` method never returns any data.
Copy```
>>> import http.client
>>> conn = http.client.HTTPSConnection("www.python.org")
>>> conn.request("HEAD", "/")
>>> res = conn.getresponse()
>>> print(res.status, res.reason)
200 OK
>>> data = res.read()
>>> print(len(data))
0
>>> data == b''
True

```

Here is an example session that uses the `POST` method:
Copy```
>>> import http.client, urllib.parse
>>> params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
>>> headers = {"Content-type": "application/x-www-form-urlencoded",
...            "Accept": "text/plain"}
>>> conn = http.client.HTTPConnection("bugs.python.org")
>>> conn.request("POST", "", params, headers)
>>> response = conn.getresponse()
>>> print(response.status, response.reason)
302 Found
>>> data = response.read()
>>> data
b'Redirecting to <a href="https://bugs.python.org/issue12524">https://bugs.python.org/issue12524</a>'
>>> conn.close()

```

Client side HTTP `PUT` requests are very similar to `POST` requests. The difference lies only on the server side where HTTP servers will allow resources to be created via `PUT` requests. It should be noted that custom HTTP methods are also handled in [`urllib.request.Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") by setting the appropriate method attribute. Here is an example session that uses the `PUT` method:
Copy```
>>> # This creates an HTTP request
>>> # with the content of BODY as the enclosed representation
>>> # for the resource http://localhost:8080/file
...
>>> import http.client
>>> BODY = "***filecontents***"
>>> conn = http.client.HTTPConnection("localhost", 8080)
>>> conn.request("PUT", "/file", BODY)
>>> response = conn.getresponse()
>>> print(response.status, response.reason)
200, OK

```

## HTTPMessage Objects[¶](https://docs.python.org/3/library/http.client.html#httpmessage-objects "Link to this heading")

_class_ http.client.HTTPMessage(_email.message.Message_)[¶](https://docs.python.org/3/library/http.client.html#http.client.HTTPMessage "Link to this definition")

An [`http.client.HTTPMessage`](https://docs.python.org/3/library/http.client.html#http.client.HTTPMessage "http.client.HTTPMessage") instance holds the headers from an HTTP response. It is implemented using the [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message") class.
### [Table of Contents](https://docs.python.org/3/contents.html)
  * [`http.client` — HTTP protocol client](https://docs.python.org/3/library/http.client.html)
    * [HTTPConnection Objects](https://docs.python.org/3/library/http.client.html#httpconnection-objects)
    * [HTTPResponse Objects](https://docs.python.org/3/library/http.client.html#httpresponse-objects)
    * [Examples](https://docs.python.org/3/library/http.client.html#examples)
    * [HTTPMessage Objects](https://docs.python.org/3/library/http.client.html#httpmessage-objects)


#### Previous topic
[`http` — HTTP modules](https://docs.python.org/3/library/http.html "previous chapter")
#### Next topic
[`ftplib` — FTP protocol client](https://docs.python.org/3/library/ftplib.html "next chapter")
### This page
  * [Report a bug](https://docs.python.org/3/bugs.html)
  * [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=http.client+%E2%80%94+HTTP+protocol+client&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.client.html&pagesource=library%2Fhttp.client.rst)


«
### Navigation
  * [index](https://docs.python.org/3/genindex.html "General Index")
  * [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") |
  * [next](https://docs.python.org/3/library/ftplib.html "ftplib — FTP protocol client") |
  * [previous](https://docs.python.org/3/library/http.html "http — HTTP modules") |
  * ![Python logo](https://docs.python.org/3/_static/py.svg)
  * [Python](https://www.python.org/) »
  * Greek | Ελληνικά English Spanish | español French | français Italian | italiano Japanese | 日本語 Korean | 한국어 Polish | polski Brazilian Portuguese | Português brasileiro Romanian | Românește Turkish | Türkçe Simplified Chinese | 简体中文 Traditional Chinese | 繁體中文
3.16 dev (3.15) 3.14.3 3.13 3.12 3.11 3.10 3.9 3.8 3.7 3.6 3.5 3.4 3.3 3.2 3.1 3.0 2.7 2.6
  * [3.14.3 Documentation](https://docs.python.org/3/index.html) »
  * [The Python Standard Library](https://docs.python.org/3/library/index.html) »
  * [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
  * [`http.client` — HTTP protocol client](https://docs.python.org/3/library/http.client.html)
  * |
  * Theme  Auto Light Dark |


© [Copyright](https://docs.python.org/3/copyright.html) 2001 Python Software Foundation.
This page is licensed under the Python Software Foundation License Version 2.
Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
See [History and License](https://docs.python.org/license.html) for more information.

The Python Software Foundation is a non-profit corporation. [Please donate.](https://www.python.org/psf/donations/)

Last updated on Mar 08, 2026 (06:37 UTC). [Found a bug](https://docs.python.org/bugs.html)?
Created using
  *[*]: Keyword-only parameters separator (PEP 3102)
