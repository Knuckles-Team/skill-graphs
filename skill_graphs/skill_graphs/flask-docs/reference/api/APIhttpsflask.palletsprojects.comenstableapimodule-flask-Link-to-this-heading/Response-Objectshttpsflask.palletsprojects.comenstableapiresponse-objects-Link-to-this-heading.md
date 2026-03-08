## Response Objects[¶](https://flask.palletsprojects.com/en/stable/api/#response-objects "Link to this heading")

_class_ flask.Response(_response =None_, _status =None_, _headers =None_, _mimetype =None_, _content_type =None_, _direct_passthrough =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response "Link to this definition")

The response object that is used by default in Flask. Works like the response object from Werkzeug but is set to have an HTML mimetype by default. Quite often you don’t have to create this object yourself because [`make_response()`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.make_response "flask.Flask.make_response") will take care of that for you.
If you want to replace the response object used you can subclass this and set [`response_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.response_class "flask.Flask.response_class") to your subclass.
Changelog
Changed in version 1.0: JSON support is added to the response, like the request. This is useful when testing to get the test client response data as JSON.
Changed in version 1.0: Added [`max_cookie_size`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.max_cookie_size "flask.Response.max_cookie_size").

Parameters:

  * **response** (_[__]__|__[__]_)
  * **status** (_|__|__HTTPStatus_ _|__None_)
  * **headers** ([_Headers_](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.Headers "\(in Werkzeug v3.1.x\)"))
  * **mimetype** (_|__None_)
  * **content_type** (_|__None_)
  * **direct_passthrough** (



default_mimetype _: |__= 'text/html'_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.default_mimetype "Link to this definition")

the default mimetype if none is provided.

accept_ranges[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.accept_ranges "Link to this definition")

The `Accept-Ranges` header. Even though the name would indicate that multiple values are supported, it must be one string token only.
The values `'bytes'` and `'none'` are common.
Changelog
Added in version 0.7.

_property_ access_control_allow_credentials _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.access_control_allow_credentials "Link to this definition")

Whether credentials can be shared by the browser to JavaScript code. As part of the preflight request it indicates whether credentials can be used on the cross origin request.

access_control_allow_headers[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.access_control_allow_headers "Link to this definition")

Which headers can be sent with the cross origin request.

access_control_allow_methods[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.access_control_allow_methods "Link to this definition")

Which methods can be used for the cross origin request.

access_control_allow_origin[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.access_control_allow_origin "Link to this definition")

The origin or ‘*’ for any origin that may make cross origin requests.

access_control_expose_headers[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.access_control_expose_headers "Link to this definition")

Which headers can be shared by the browser to JavaScript code.

access_control_max_age[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.access_control_max_age "Link to this definition")

The maximum age in seconds the access control settings can be cached for.

add_etag(_overwrite =False_, _weak =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.add_etag "Link to this definition")

Add an etag for the current response if there is none yet.
Changelog
Changed in version 2.0: SHA-1 is used to generate the value. MD5 may not be available in some environments.

Parameters:

  * **overwrite** (
  * **weak** (



Return type:

None

age[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.age "Link to this definition")

The Age response-header field conveys the sender’s estimate of the amount of time since the response (or its revalidation) was generated at the origin server.
Age values are non-negative decimal integers, representing time in seconds.

_property_ allow _:[ HeaderSet](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.HeaderSet "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.allow "Link to this definition")

The Allow entity-header field lists the set of methods supported by the resource identified by the Request-URI. The purpose of this field is strictly to inform the recipient of valid methods associated with the resource. An Allow header field MUST be present in a 405 (Method Not Allowed) response.

automatically_set_content_length _= True_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.automatically_set_content_length "Link to this definition")

Should this response object automatically set the content-length header if possible? This is true by default.
Changelog
Added in version 0.8.

_property_ cache_control _:[ ResponseCacheControl](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.ResponseCacheControl "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.cache_control "Link to this definition")

The Cache-Control general-header field is used to specify directives that MUST be obeyed by all caching mechanisms along the request/response chain.

calculate_content_length()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.calculate_content_length "Link to this definition")

Returns the content length if available or `None` otherwise.

Return type:


call_on_close(_func_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.call_on_close "Link to this definition")

Adds a function to the internal list of functions that should be called as part of closing down the response. Since 0.7 this function also returns the function that was passed so that this can be used as a decorator.
Changelog
Added in version 0.6.

Parameters:

**func** (_[__[__]__,__]_)

Return type:


close()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.close "Link to this definition")

Close the wrapped response if possible. You can also use the object in a with statement which will automatically close it.
Changelog
Added in version 0.9: Can now be used in a with statement.

Return type:

None

content_encoding[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.content_encoding "Link to this definition")

The Content-Encoding entity-header field is used as a modifier to the media-type. When present, its value indicates what additional content codings have been applied to the entity-body, and thus what decoding mechanisms must be applied in order to obtain the media-type referenced by the Content-Type header field.

_property_ content_language _:[ HeaderSet](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.HeaderSet "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.content_language "Link to this definition")

The Content-Language entity-header field describes the natural language(s) of the intended audience for the enclosed entity. Note that this might not be equivalent to all the languages used within the entity-body.

content_length[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.content_length "Link to this definition")

The Content-Length entity-header field indicates the size of the entity-body, in decimal number of OCTETs, sent to the recipient or, in the case of the HEAD method, the size of the entity-body that would have been sent had the request been a GET.

content_location[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.content_location "Link to this definition")

The Content-Location entity-header field MAY be used to supply the resource location for the entity enclosed in the message when that entity is accessible from a location separate from the requested resource’s URI.

content_md5[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.content_md5 "Link to this definition")

The Content-MD5 entity-header field, as defined in RFC 1864, is an MD5 digest of the entity-body for the purpose of providing an end-to-end message integrity check (MIC) of the entity-body. (Note: a MIC is good for detecting accidental modification of the entity-body in transit, but is not proof against malicious attacks.)

_property_ content_range _:[ ContentRange](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.ContentRange "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.content_range "Link to this definition")

The `Content-Range` header as a [`ContentRange`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.ContentRange "\(in Werkzeug v3.1.x\)") object. Available even if the header is not set.
Changelog
Added in version 0.7.

_property_ content_security_policy _: ContentSecurityPolicy_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.content_security_policy "Link to this definition")

The `Content-Security-Policy` header as a `ContentSecurityPolicy` object. Available even if the header is not set.
The Content-Security-Policy header adds an additional layer of security to help detect and mitigate certain types of attacks.

_property_ content_security_policy_report_only _: ContentSecurityPolicy_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.content_security_policy_report_only "Link to this definition")

The `Content-Security-policy-report-only` header as a `ContentSecurityPolicy` object. Available even if the header is not set.
The Content-Security-Policy-Report-Only header adds a csp policy that is not enforced but is reported thereby helping detect certain types of attacks.

content_type[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.content_type "Link to this definition")

The Content-Type entity-header field indicates the media type of the entity-body sent to the recipient or, in the case of the HEAD method, the media type that would have been sent had the request been a GET.

cross_origin_embedder_policy[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.cross_origin_embedder_policy "Link to this definition")

Prevents a document from loading any cross-origin resources that do not explicitly grant the document permission. Values must be a member of the `werkzeug.http.COEP` enum.

cross_origin_opener_policy[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.cross_origin_opener_policy "Link to this definition")

Allows control over sharing of browsing context group with cross-origin documents. Values must be a member of the `werkzeug.http.COOP` enum.

_property_ data _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.data "Link to this definition")

A descriptor that calls [`get_data()`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.get_data "flask.Response.get_data") and [`set_data()`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.set_data "flask.Response.set_data").

date[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.date "Link to this definition")

The Date general-header field represents the date and time at which the message was originated, having the same semantics as orig-date in RFC 822.
Changelog
Changed in version 2.0: The datetime object is timezone-aware.

default_status _= 200_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.default_status "Link to this definition")

the default status if none is provided.

delete_cookie(_key_ , _path ='/'_, _domain =None_, _secure =False_, _httponly =False_, _samesite =None_, _partitioned =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.delete_cookie "Link to this definition")

Delete a cookie. Fails silently if key doesn’t exist.

Parameters:

  * **key** (
  * **path** (_|__None_) – if the cookie that should be deleted was limited to a path, the path has to be defined here.
  * **domain** (_|__None_) – if the cookie that should be deleted was limited to a domain, that domain has to be defined here.
  * **secure** (`True`, the cookie will only be available via HTTPS.
  * **httponly** (
  * **samesite** (_|__None_) – Limit the scope of the cookie to only be attached to requests that are “same-site”.
  * **partitioned** (`True`, the cookie will be partitioned.



Return type:

None

expires[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.expires "Link to this definition")

The Expires entity-header field gives the date/time after which the response is considered stale. A stale cache entry may not normally be returned by a cache.
Changelog
Changed in version 2.0: The datetime object is timezone-aware.

_classmethod_ force_type(_response_ , _environ =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.force_type "Link to this definition")

Enforce that the WSGI response is a response object of the current type. Werkzeug will use the [`Response`](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") internally in many situations like the exceptions. If you call `get_response()` on an exception you will get back a regular [`Response`](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") object, even if you are using a custom subclass.
This method can enforce a given response type, and it will also convert arbitrary WSGI callables into response objects if an environ is provided:
```
# convert a Werkzeug response object into an instance of the
# MyResponseClass subclass.
response = MyResponseClass.force_type(response)

# convert any WSGI application into a response object
response = MyResponseClass.force_type(response, environ)

```

This is especially useful if you want to post-process responses in the main dispatcher and use functionality provided by your subclass.
Keep in mind that this will modify response objects in place if possible!

Parameters:

  * **response** ([_Response_](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response")) – a response object or wsgi application.
  * **environ** (_WSGIEnvironment_ _|__None_) – a WSGI environment object.



Returns:

a response object.

Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response")

freeze()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.freeze "Link to this definition")

Make the response object ready to be pickled. Does the following:
  * Buffer the response into a list, ignoring `implicity_sequence_conversion` and [`direct_passthrough`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.direct_passthrough "flask.Response.direct_passthrough").
  * Set the `Content-Length` header.
  * Generate an `ETag` header if one is not already set.

Changelog
Changed in version 2.1: Removed the `no_etag` parameter.
Changed in version 2.0: An `ETag` header is always added.
Changed in version 0.6: The `Content-Length` header is set.

Return type:

None

_classmethod_ from_app(_app_ , _environ_ , _buffered =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.from_app "Link to this definition")

Create a new response object from an application output. This works best if you pass it an application that returns a generator all the time. Sometimes applications may use the `write()` callable returned by the `start_response` function. This tries to resolve such edge cases automatically. But if you don’t get the expected output you should set `buffered` to `True` which enforces buffering.

Parameters:

  * **app** (_WSGIApplication_) – the WSGI application to execute.
  * **environ** (_WSGIEnvironment_) – the WSGI environment to execute against.
  * **buffered** (`True` to enforce buffering.



Returns:

a response object.

Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response")

get_app_iter(_environ_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.get_app_iter "Link to this definition")

Returns the application iterator for the given environ. Depending on the request method and the current status code the return value might be an empty response rather than the one from the response.
If the request method is `HEAD` or the status code is in a range where the HTTP specification requires an empty response, an empty iterable is returned.
Changelog
Added in version 0.6.

Parameters:

**environ** (_WSGIEnvironment_) – the WSGI environment of the request.

Returns:

a response iterable.

Return type:

t.Iterable[

get_data(_as_text =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.get_data "Link to this definition")

The string representation of the response body. Whenever you call this property the response iterable is encoded and flattened. This can lead to unwanted behavior if you stream big data.
This behavior can be disabled by setting [`implicit_sequence_conversion`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.implicit_sequence_conversion "flask.Response.implicit_sequence_conversion") to `False`.
If `as_text` is set to `True` the return value will be a decoded string.
Changelog
Added in version 0.9.

Parameters:

**as_text** (

Return type:


get_etag()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.get_etag "Link to this definition")

Return a tuple in the form `(etag, is_weak)`. If there is no ETag the return value is `(None, None)`.

Return type:


get_json(_force =False_, _silent =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.get_json "Link to this definition")

Parse [`data`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.data "flask.Response.data") as JSON. Useful during testing.
If the mimetype does not indicate JSON (_application/json_ , see [`is_json`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.is_json "flask.Response.is_json")), this returns `None`.
Unlike [`Request.get_json()`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_json "flask.Request.get_json"), the result is not cached.

Parameters:

  * **force** (
  * **silent** (`None` instead.



Return type:


get_wsgi_headers(_environ_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.get_wsgi_headers "Link to this definition")

This is automatically called right before the response is started and returns headers modified for the given environment. It returns a copy of the headers from the response with some modifications applied if necessary.
For example the location header (if present) is joined with the root URL of the environment. Also the content length is automatically set to zero here for certain status codes.
Changelog
Changed in version 0.6: Previously that function was called `fix_headers` and modified the response object in place. Also since 0.6, IRIs in location and content-location headers are handled properly.
Also starting with 0.6, Werkzeug will attempt to set the content length if it is able to figure it out on its own. This is the case if all the strings in the response iterable are already encoded and the iterable is buffered.

Parameters:

**environ** (_WSGIEnvironment_) – the WSGI environment of the request.

Returns:

returns a new [`Headers`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.Headers "\(in Werkzeug v3.1.x\)") object.

Return type:

Headers

get_wsgi_response(_environ_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.get_wsgi_response "Link to this definition")

Returns the final WSGI response as tuple. The first item in the tuple is the application iterator, the second the status and the third the list of headers. The response returned is created specially for the given environment. For example if the request method in the WSGI environment is `'HEAD'` the response will be empty and only the headers and status code will be present.
Changelog
Added in version 0.6.

Parameters:

**environ** (_WSGIEnvironment_) – the WSGI environment of the request.

Returns:

an `(app_iter, status, headers)` tuple.

Return type:


implicit_sequence_conversion _= True_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.implicit_sequence_conversion "Link to this definition")

if set to `False` accessing properties on the response object will not try to consume the response iterator and convert it into a list.
Changelog
Added in version 0.6.2: That attribute was previously called `implicit_seqence_conversion`. (Notice the typo). If you did use this feature, you have to adapt your code to the name change.

_property_ is_json _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.is_json "Link to this definition")

Check if the mimetype indicates JSON data, either _application/json_ or _application/*+json_.

_property_ is_sequence _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.is_sequence "Link to this definition")

If the iterator is buffered, this property will be `True`. A response object will consider an iterator to be buffered if the response attribute is a list or tuple.
Changelog
Added in version 0.6.

_property_ is_streamed _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.is_streamed "Link to this definition")

If the response is streamed (the response is not an iterable with a length information) this property is `True`. In this case streamed means that there is no information about the number of iterations. This is usually `True` if a generator is passed to the response object.
This is useful for checking before applying some sort of post filtering that should not take place for streamed responses.

iter_encoded()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.iter_encoded "Link to this definition")

Iter the response encoded with the encoding of the response. If the response object is invoked as WSGI application the return value of this method is used as application iterator unless [`direct_passthrough`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.direct_passthrough "flask.Response.direct_passthrough") was activated.

Return type:


_property_ json _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.json "Link to this definition")

The parsed JSON data if [`mimetype`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.mimetype "flask.Response.mimetype") indicates JSON (_application/json_ , see [`is_json`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.is_json "flask.Response.is_json")).
Calls [`get_json()`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.get_json "flask.Response.get_json") with default arguments.

last_modified[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.last_modified "Link to this definition")

The Last-Modified entity-header field indicates the date and time at which the origin server believes the variant was last modified.
Changelog
Changed in version 2.0: The datetime object is timezone-aware.

location[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.location "Link to this definition")

The Location response-header field is used to redirect the recipient to a location other than the Request-URI for completion of the request or identification of a new resource.

make_conditional(_request_or_environ_ , _accept_ranges =False_, _complete_length =None_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.make_conditional "Link to this definition")

Make the response conditional to the request. This method works best if an etag was defined for the response already. The `add_etag` method can be used to do that. If called without etag just the date header is set.
This does nothing if the request method in the request or environ is anything but GET or HEAD.
For optimal performance when handling range requests, it’s recommended that your response data object implements `seekable`, `seek` and `tell` methods as described by `wrap_file()` automatically implement those methods.
It does not remove the body of the response because that’s something the `__call__()` function does for us automatically.
Returns self so that you can do `return resp.make_conditional(req)` but modifies the object in-place.

Parameters:

  * **request_or_environ** (_WSGIEnvironment_ _|_[_Request_](https://flask.palletsprojects.com/en/stable/api/#flask.Request "flask.Request")) – a request object or WSGI environment to be used to make the response conditional against.
  * **accept_ranges** (_|_`Accept-Ranges` header. If `False` (default), the header is not set. If `True`, it will be set to `"bytes"`. If it’s a string, it will use this value.
  * **complete_length** (_|__None_) – Will be used only in valid Range Requests. It will set `Content-Range` complete length value and compute `Content-Length` real value. This parameter is mandatory for successful Range Requests completion.



Raises:

[`RequestedRangeNotSatisfiable`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.RequestedRangeNotSatisfiable "\(in Werkzeug v3.1.x\)") if `Range` header could not be parsed or satisfied.

Return type:

[Response](https://flask.palletsprojects.com/en/stable/api/#flask.Response "flask.Response") Changelog
Changed in version 2.0: Range processing is skipped if length is 0 instead of raising a 416 Range Not Satisfiable error.

make_sequence()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.make_sequence "Link to this definition")

Converts the response iterator in a list. By default this happens automatically if required. If `implicit_sequence_conversion` is disabled, this method is not automatically called and some properties might raise exceptions. This also encodes all the items.
Changelog
Added in version 0.6.

Return type:

None

_property_ mimetype _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.mimetype "Link to this definition")

The mimetype (content type without charset etc.)

_property_ mimetype_params _:[,]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.mimetype_params "Link to this definition")

The mimetype parameters as dict. For example if the content type is `text/html; charset=utf-8` the params would be `{'charset': 'utf-8'}`.
Changelog
Added in version 0.5.

_property_ retry_after _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.retry_after "Link to this definition")

The Retry-After response-header field can be used with a 503 (Service Unavailable) response to indicate how long the service is expected to be unavailable to the requesting client.
Time in seconds until expiration or date.
Changelog
Changed in version 2.0: The datetime object is timezone-aware.

set_cookie(_key_ , _value =''_, _max_age =None_, _expires =None_, _path ='/'_, _domain =None_, _secure =False_, _httponly =False_, _samesite =None_, _partitioned =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.set_cookie "Link to this definition")

Sets a cookie.
A warning is raised if the size of the cookie header exceeds [`max_cookie_size`](https://flask.palletsprojects.com/en/stable/api/#flask.Response.max_cookie_size "flask.Response.max_cookie_size"), but the header will still be set.

Parameters:

  * **key** (
  * **value** (
  * **max_age** (_|__|__None_) – should be a number of seconds, or `None` (default) if the cookie should last only as long as the client’s browser session.
  * **expires** (_|__|__|__|__None_) – should be a `datetime` object or UNIX timestamp.
  * **path** (_|__None_) – limits the cookie to a given path, per default it will span the whole domain.
  * **domain** (_|__None_) – if you want to set a cross-domain cookie. For example, `domain="example.com"` will set a cookie that is readable by the domain `www.example.com`, `foo.example.com` etc. Otherwise, a cookie will only be readable by the domain that set it.
  * **secure** (`True`, the cookie will only be available via HTTPS.
  * **httponly** (
  * **samesite** (_|__None_) – Limit the scope of the cookie to only be attached to requests that are “same-site”.
  * **partitioned** (`True`, the cookie will be partitioned.



Return type:

None
Changed in version 3.1: The `partitioned` parameter was added.

set_data(_value_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.set_data "Link to this definition")

Sets a new string as response. The value must be a string or bytes. If a string is set it’s encoded to the charset of the response (utf-8 by default).
Changelog
Added in version 0.9.

Parameters:

**value** (_|_

Return type:

None

set_etag(_etag_ , _weak =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.set_etag "Link to this definition")

Set the etag, and override the old one if there was one.

Parameters:

  * **etag** (
  * **weak** (



Return type:

None

_property_ status _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.status "Link to this definition")

The HTTP status code as a string.

_property_ status_code _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.status_code "Link to this definition")

The HTTP status code as a number.

_property_ stream _: ResponseStream_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.stream "Link to this definition")

The response iterable as write-only stream.

_property_ vary _:[ HeaderSet](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.HeaderSet "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.vary "Link to this definition")

The Vary field value indicates the set of request-header fields that fully determines, while the response is fresh, whether a cache is permitted to use the response to reply to a subsequent request without revalidation.

_property_ www_authenticate _:[ WWWAuthenticate](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.WWWAuthenticate "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.www_authenticate "Link to this definition")

The `WWW-Authenticate` header parsed into a `WWWAuthenticate` object. Modifying the object will modify the header value.
This header is not set by default. To set this header, assign an instance of `WWWAuthenticate` to this attribute.
```
response.www_authenticate = WWWAuthenticate(
    "basic", {"realm": "Authentication Required"}
)

```

Multiple values for this header can be sent to give the client multiple options. Assign a list to set multiple headers. However, modifying the items in the list will not automatically update the header values, and accessing this attribute will only ever return the first value.
To unset this header, assign `None` or use `del`.
Changelog
Changed in version 2.3: This attribute can be assigned to set the header. A list can be assigned to set multiple header values. Use `del` to unset the header.
Changed in version 2.3: `WWWAuthenticate` is no longer a `dict`. The `token` attribute was added for auth challenges that use a token instead of parameters.

response _: t.Iterable[]|t.Iterable[]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.response "Link to this definition")

The response body to send as the WSGI iterable. A list of strings or bytes represents a fixed-length response, any other iterable is a streaming response. Strings are encoded to bytes as UTF-8.
Do not set to a plain string or bytes, that will cause sending the response to be very inefficient as it will iterate one byte at a time.

direct_passthrough[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.direct_passthrough "Link to this definition")

Pass the response body directly through as the WSGI iterable. This can be used when the body is a binary file or other iterator of bytes, to skip some unnecessary checks. Use [`send_file()`](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.utils.send_file "\(in Werkzeug v3.1.x\)") instead of setting this manually.

autocorrect_location_header _= False_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.autocorrect_location_header "Link to this definition")

If a redirect `Location` header is a relative URL, make it an absolute URL, including scheme and domain.
Changelog
Changed in version 2.1: This is disabled by default, so responses will send relative redirects.
Added in version 0.8.

_property_ max_cookie_size _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Response.max_cookie_size "Link to this definition")

Read-only view of the [`MAX_COOKIE_SIZE`](https://flask.palletsprojects.com/en/stable/config/#MAX_COOKIE_SIZE "MAX_COOKIE_SIZE") config key.
See [`max_cookie_size`](https://werkzeug.palletsprojects.com/en/stable/wrappers/#werkzeug.wrappers.Response.max_cookie_size "\(in Werkzeug v3.1.x\)") in Werkzeug’s docs.
