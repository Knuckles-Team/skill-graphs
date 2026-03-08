## Request Objects[¶](https://docs.python.org/3/library/urllib.request.html#request-objects "Link to this heading")
The following methods describe [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request")’s public interface, and so all may be overridden in subclasses. It also defines several public attributes that can be used by clients to inspect the parsed request.

Request.full_url[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.full_url "Link to this definition")

The original URL passed to the constructor.
Changed in version 3.4.
Request.full_url is a property with setter, getter and a deleter. Getting `full_url` returns the original request URL with the fragment, if it was present.

Request.type[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.type "Link to this definition")

The URI scheme.

Request.host[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.host "Link to this definition")

The URI authority, typically a host, but may also contain a port separated by a colon.

Request.origin_req_host[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.origin_req_host "Link to this definition")

The original host for the request, without port.

Request.selector[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.selector "Link to this definition")

The URI path. If the [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") uses a proxy, then selector will be the full URL that is passed to the proxy.

Request.data[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.data "Link to this definition")

The entity body for the request, or `None` if not specified.
Changed in version 3.4: Changing value of `Request.data` now deletes “Content-Length” header if it was previously set or calculated.

Request.unverifiable[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.unverifiable "Link to this definition")

boolean, indicates whether the request is unverifiable as defined by

Request.method[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.method "Link to this definition")

The HTTP request method to use. By default its value is [`None`](https://docs.python.org/3/library/constants.html#None "None"), which means that [`get_method()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.get_method "urllib.request.Request.get_method") will do its normal computation of the method to be used. Its value can be set (thus overriding the default computation in `get_method()`) either by providing a default value by setting it at the class level in a [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request") subclass, or by passing a value in to the `Request` constructor via the _method_ argument.
Added in version 3.3.
Changed in version 3.4: A default value can now be set in subclasses; previously it could only be set via the constructor argument.

Request.get_method()[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.get_method "Link to this definition")

Return a string indicating the HTTP request method. If [`Request.method`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.method "urllib.request.Request.method") is not `None`, return its value, otherwise return `'GET'` if [`Request.data`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.data "urllib.request.Request.data") is `None`, or `'POST'` if it’s not. This is only meaningful for HTTP requests.
Changed in version 3.3: get_method now looks at the value of [`Request.method`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.method "urllib.request.Request.method").

Request.add_header(_key_ , _val_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.add_header "Link to this definition")

Add another header to the request. Headers are currently ignored by all handlers except HTTP handlers, where they are added to the list of headers sent to the server. Note that there cannot be more than one header with the same name, and later calls will overwrite previous calls in case the _key_ collides. Currently, this is no loss of HTTP functionality, since all headers which have meaning when used more than once have a (header-specific) way of gaining the same functionality using only one header. Note that headers added using this method are also added to redirected requests.

Request.add_unredirected_header(_key_ , _header_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.add_unredirected_header "Link to this definition")

Add a header that will not be added to a redirected request.

Request.has_header(_header_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.has_header "Link to this definition")

Return whether the instance has the named header (checks both regular and unredirected).

Request.remove_header(_header_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.remove_header "Link to this definition")

Remove named header from the request instance (both from regular and unredirected headers).
Added in version 3.4.

Request.get_full_url()[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.get_full_url "Link to this definition")

Return the URL given in the constructor.
Changed in version 3.4.
Returns [`Request.full_url`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.full_url "urllib.request.Request.full_url")

Request.set_proxy(_host_ , _type_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.set_proxy "Link to this definition")

Prepare the request by connecting to a proxy server. The _host_ and _type_ will replace those of the instance, and the instance’s selector will be the original URL given in the constructor.

Request.get_header(_header_name_ , _default =None_)[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.get_header "Link to this definition")

Return the value of the given header. If the header is not present, return the default value.

Request.header_items()[¶](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.header_items "Link to this definition")

Return a list of tuples (header_name, header_value) of the Request headers.
Changed in version 3.4: The request methods add_data, has_data, get_data, get_type, get_host, get_selector, get_origin_req_host and is_unverifiable that were deprecated since 3.3 have been removed.
