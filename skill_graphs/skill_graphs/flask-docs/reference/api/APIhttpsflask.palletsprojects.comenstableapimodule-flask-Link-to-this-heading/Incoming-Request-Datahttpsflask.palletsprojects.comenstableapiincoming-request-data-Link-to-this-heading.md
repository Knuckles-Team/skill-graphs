## Incoming Request Data[¶](https://flask.palletsprojects.com/en/stable/api/#incoming-request-data "Link to this heading")

_class_ flask.Request(_environ_ , _populate_request =True_, _shallow =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request "Link to this definition")

The request object used by default in Flask. Remembers the matched endpoint and view arguments.
It is what ends up as [`request`](https://flask.palletsprojects.com/en/stable/api/#flask.request "flask.request"). If you want to replace the request object used you can subclass this and set [`request_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Flask.request_class "flask.Flask.request_class") to your subclass.
The request object is a [`Request`](https://werkzeug.palletsprojects.com/en/stable/wrappers/#werkzeug.wrappers.Request "\(in Werkzeug v3.1.x\)") subclass and provides all of the attributes Werkzeug defines plus a few Flask specific ones.

Parameters:

  * **environ** (_WSGIEnvironment_)
  * **populate_request** (
  * **shallow** (



url_rule _: Rule|__= None_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.url_rule "Link to this definition")

The internal URL rule that matched the request. This can be useful to inspect which methods are allowed for the URL from a before/after handler (`request.url_rule.methods`) etc. Though if the request’s method was invalid for the URL rule, the valid list is available in `routing_exception.valid_methods` instead (an attribute of the Werkzeug exception [`MethodNotAllowed`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.MethodNotAllowed "\(in Werkzeug v3.1.x\)")) because the request was never internally bound.
Changelog
Added in version 0.6.

view_args _:[,t.Any]|__= None_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.view_args "Link to this definition")

A dict of view arguments that matched the request. If an exception happened when matching, this will be `None`.

routing_exception _: HTTPException|__= None_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.routing_exception "Link to this definition")

If matching the URL failed, this is the exception that will be raised / was raised as part of the request handling. This is usually a [`NotFound`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.NotFound "\(in Werkzeug v3.1.x\)") exception or something similar.

_property_ max_content_length _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.max_content_length "Link to this definition")

The maximum number of bytes that will be read during this request. If this limit is exceeded, a 413 [`RequestEntityTooLarge`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.RequestEntityTooLarge "\(in Werkzeug v3.1.x\)") error is raised. If it is set to `None`, no limit is enforced at the Flask application level. However, if it is `None` and the request has no `Content-Length` header and the WSGI server does not indicate that it terminates the stream, then no data is read to avoid an infinite stream.
Each request defaults to the [`MAX_CONTENT_LENGTH`](https://flask.palletsprojects.com/en/stable/config/#MAX_CONTENT_LENGTH "MAX_CONTENT_LENGTH") config, which defaults to `None`. It can be set on a specific `request` to apply the limit to that specific view. This should be set appropriately based on an application’s or view’s specific needs.
Changed in version 3.1: This can be set per-request.
Changelog
Changed in version 0.6: This is configurable through Flask config.

_property_ max_form_memory_size _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.max_form_memory_size "Link to this definition")

The maximum size in bytes any non-file form field may be in a `multipart/form-data` body. If this limit is exceeded, a 413 [`RequestEntityTooLarge`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.RequestEntityTooLarge "\(in Werkzeug v3.1.x\)") error is raised. If it is set to `None`, no limit is enforced at the Flask application level.
Each request defaults to the [`MAX_FORM_MEMORY_SIZE`](https://flask.palletsprojects.com/en/stable/config/#MAX_FORM_MEMORY_SIZE "MAX_FORM_MEMORY_SIZE") config, which defaults to `500_000`. It can be set on a specific `request` to apply the limit to that specific view. This should be set appropriately based on an application’s or view’s specific needs.
Changed in version 3.1: This is configurable through Flask config.

_property_ max_form_parts _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.max_form_parts "Link to this definition")

The maximum number of fields that may be present in a `multipart/form-data` body. If this limit is exceeded, a 413 [`RequestEntityTooLarge`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.RequestEntityTooLarge "\(in Werkzeug v3.1.x\)") error is raised. If it is set to `None`, no limit is enforced at the Flask application level.
Each request defaults to the [`MAX_FORM_PARTS`](https://flask.palletsprojects.com/en/stable/config/#MAX_FORM_PARTS "MAX_FORM_PARTS") config, which defaults to `1_000`. It can be set on a specific `request` to apply the limit to that specific view. This should be set appropriately based on an application’s or view’s specific needs.
Changed in version 3.1: This is configurable through Flask config.

_property_ endpoint _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.endpoint "Link to this definition")

The endpoint that matched the request URL.
This will be `None` if matching failed or has not been performed yet.
This in combination with [`view_args`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.view_args "flask.Request.view_args") can be used to reconstruct the same URL or a modified URL.

_property_ blueprint _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.blueprint "Link to this definition")

The registered name of the current blueprint.
This will be `None` if the endpoint is not part of a blueprint, or if URL matching failed or has not been performed yet.
This does not necessarily match the name the blueprint was created with. It may have been nested, or registered with a different name.

_property_ blueprints _:[]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.blueprints "Link to this definition")

The registered names of the current blueprint upwards through parent blueprints.
This will be an empty list if there is no current blueprint, or if URL matching failed.
Changelog
Added in version 2.0.1.

on_json_loading_failed(_e_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.on_json_loading_failed "Link to this definition")

Called if [`get_json()`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_json "flask.Request.get_json") fails and isn’t silenced.
If this method returns a value, it is used as the return value for [`get_json()`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_json "flask.Request.get_json"). The default implementation raises [`BadRequest`](https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.BadRequest "\(in Werkzeug v3.1.x\)").

Parameters:

**e** (_|__None_) – If parsing failed, this is the exception. It will be `None` if the content type wasn’t `application/json`.

Return type:
Changelog
Changed in version 2.3: Raise a 415 error instead of 400.

_property_ accept_charsets _:[ CharsetAccept](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.CharsetAccept "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.accept_charsets "Link to this definition")

List of charsets this client supports as [`CharsetAccept`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.CharsetAccept "\(in Werkzeug v3.1.x\)") object.

_property_ accept_encodings _:[ Accept](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.Accept "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.accept_encodings "Link to this definition")

List of encodings this client accepts. Encodings in a HTTP term are compression encodings such as gzip. For charsets have a look at `accept_charset`.

_property_ accept_languages _:[ LanguageAccept](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.LanguageAccept "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.accept_languages "Link to this definition")

List of languages this client accepts as [`LanguageAccept`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.LanguageAccept "\(in Werkzeug v3.1.x\)") object.

_property_ accept_mimetypes _:[ MIMEAccept](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.MIMEAccept "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.accept_mimetypes "Link to this definition")

List of mimetypes this client supports as [`MIMEAccept`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.MIMEAccept "\(in Werkzeug v3.1.x\)") object.

access_control_request_headers[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.access_control_request_headers "Link to this definition")

Sent with a preflight request to indicate which headers will be sent with the cross origin request. Set `access_control_allow_headers` on the response to indicate which headers are allowed.

access_control_request_method[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.access_control_request_method "Link to this definition")

Sent with a preflight request to indicate which method will be used for the cross origin request. Set `access_control_allow_methods` on the response to indicate which methods are allowed.

_property_ access_route _:[]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.access_route "Link to this definition")

If a forwarded header exists this is a list of all ip addresses from the client ip to the last proxy server.

_classmethod_ application(_f_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.application "Link to this definition")

Decorate a function as responder that accepts the request as the last argument. This works like the `responder()` decorator but the function is passed the request object as the last argument and the request object will be closed automatically:
```
@Request.application
def my_wsgi_app(request):
    return Response('Hello World!')

```

As of Werkzeug 0.14 HTTP exceptions are automatically caught and converted to responses instead of failing.

Parameters:

**f** (_t.Callable_ _[__[_[_Request_](https://flask.palletsprojects.com/en/stable/api/#flask.Request "flask.Request") _]__,__WSGIApplication_ _]_) – the WSGI callable to decorate

Returns:

a new WSGI callable

Return type:

WSGIApplication

_property_ args _:[ MultiDict](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.MultiDict "\(in Werkzeug v3.1.x\)")[,]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.args "Link to this definition")

The parsed URL parameters (the part in the URL after the question mark).
By default an `ImmutableMultiDict` is returned from this function. This can be changed by setting [`parameter_storage_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.parameter_storage_class "flask.Request.parameter_storage_class") to a different type. This might be necessary if the order of the form data is important.
Changelog
Changed in version 2.3: Invalid bytes remain percent encoded.

_property_ authorization _:[ Authorization](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.Authorization "\(in Werkzeug v3.1.x\)")|_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.authorization "Link to this definition")

The `Authorization` header parsed into an `Authorization` object. `None` if the header is not present.
Changelog
Changed in version 2.3: `Authorization` is no longer a `dict`. The `token` attribute was added for auth schemes that use a token instead of parameters.

_property_ base_url _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.base_url "Link to this definition")

Like [`url`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.url "flask.Request.url") but without the query string.

_property_ cache_control _:[ RequestCacheControl](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.RequestCacheControl "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.cache_control "Link to this definition")

A [`RequestCacheControl`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.RequestCacheControl "\(in Werkzeug v3.1.x\)") object for the incoming cache control headers.

close()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.close "Link to this definition")

Closes associated resources of this request object. This closes all file handles explicitly. You can also use the request object in a with statement which will automatically close it.
Changelog
Added in version 0.9.

Return type:

None

content_encoding[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.content_encoding "Link to this definition")

The Content-Encoding entity-header field is used as a modifier to the media-type. When present, its value indicates what additional content codings have been applied to the entity-body, and thus what decoding mechanisms must be applied in order to obtain the media-type referenced by the Content-Type header field.
Changelog
Added in version 0.9.

_property_ content_length _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.content_length "Link to this definition")

The Content-Length entity-header field indicates the size of the entity-body in bytes or, in the case of the HEAD method, the size of the entity-body that would have been sent had the request been a GET.

content_md5[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.content_md5 "Link to this definition")

The Content-MD5 entity-header field, as defined in RFC 1864, is an MD5 digest of the entity-body for the purpose of providing an end-to-end message integrity check (MIC) of the entity-body. (Note: a MIC is good for detecting accidental modification of the entity-body in transit, but is not proof against malicious attacks.)
Changelog
Added in version 0.9.

content_type[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.content_type "Link to this definition")

The Content-Type entity-header field indicates the media type of the entity-body sent to the recipient or, in the case of the HEAD method, the media type that would have been sent had the request been a GET.

_property_ cookies _: ImmutableMultiDict[,]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.cookies "Link to this definition")

A

_property_ data _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.data "Link to this definition")

The raw data read from [`stream`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.stream "flask.Request.stream"). Will be empty if the request represents form data.
To get the raw data even if it represents form data, use [`get_data()`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_data "flask.Request.get_data").

date[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.date "Link to this definition")

The Date general-header field represents the date and time at which the message was originated, having the same semantics as orig-date in RFC 822.
Changelog
Changed in version 2.0: The datetime object is timezone-aware.

dict_storage_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.dict_storage_class "Link to this definition")

alias of `ImmutableMultiDict`

_property_ files _: ImmutableMultiDict[,[FileStorage](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.FileStorage "\(in Werkzeug v3.1.x\)")]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.files "Link to this definition")

[`MultiDict`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.MultiDict "\(in Werkzeug v3.1.x\)") object containing all uploaded files. Each key in [`files`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.files "flask.Request.files") is the name from the `<input type="file" name="">`. Each value in [`files`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.files "flask.Request.files") is a Werkzeug [`FileStorage`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.FileStorage "\(in Werkzeug v3.1.x\)") object.
It basically behaves like a standard file object you know from Python, with the difference that it also has a [`save()`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.FileStorage.save "\(in Werkzeug v3.1.x\)") function that can store the file on the filesystem.
Note that [`files`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.files "flask.Request.files") will only contain data if the request method was POST, PUT or PATCH and the `<form>` that posted to the request had `enctype="multipart/form-data"`. It will be empty otherwise.
See the [`MultiDict`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.MultiDict "\(in Werkzeug v3.1.x\)") / [`FileStorage`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.FileStorage "\(in Werkzeug v3.1.x\)") documentation for more details about the used data structure.

_property_ form _: ImmutableMultiDict[,]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.form "Link to this definition")

The form parameters. By default an `ImmutableMultiDict` is returned from this function. This can be changed by setting [`parameter_storage_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.parameter_storage_class "flask.Request.parameter_storage_class") to a different type. This might be necessary if the order of the form data is important.
Please keep in mind that file uploads will not end up here, but instead in the [`files`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.files "flask.Request.files") attribute.
Changelog
Changed in version 0.9: Previous to Werkzeug 0.9 this would only contain form data for POST and PUT requests.

form_data_parser_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.form_data_parser_class "Link to this definition")

alias of [`FormDataParser`](https://werkzeug.palletsprojects.com/en/stable/http/#werkzeug.formparser.FormDataParser "\(in Werkzeug v3.1.x\)")

_classmethod_ from_values(_* args_, _** kwargs_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.from_values "Link to this definition")

Create a new request object based on the values provided. If environ is given missing values are filled from there. This method is useful for small scripts when you need to simulate a request from an URL. Do not use this method for unittesting, there is a full featured client object (`Client`) that allows to create multipart requests, support for cookies etc.
This accepts the same options as the [`EnvironBuilder`](https://werkzeug.palletsprojects.com/en/stable/test/#werkzeug.test.EnvironBuilder "\(in Werkzeug v3.1.x\)").
Changelog
Changed in version 0.5: This method now accepts the same arguments as [`EnvironBuilder`](https://werkzeug.palletsprojects.com/en/stable/test/#werkzeug.test.EnvironBuilder "\(in Werkzeug v3.1.x\)"). Because of this the `environ` parameter is now called `environ_overrides`.

Returns:

request object

Parameters:

  * **args** (
  * **kwargs** (



Return type:

[_Request_](https://werkzeug.palletsprojects.com/en/stable/wrappers/#werkzeug.wrappers.Request "\(in Werkzeug v3.1.x\)")

_property_ full_path _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.full_path "Link to this definition")

Requested path, including the query string.

get_data(_cache =True_, _as_text =False_, _parse_form_data =False_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_data "Link to this definition")

This reads the buffered incoming data from the client into one bytes object. By default this is cached but that behavior can be changed by setting `cache` to `False`.
Usually it’s a bad idea to call this method without checking the content length first as a client could send dozens of megabytes or more to cause memory problems on the server.
Note that if the form data was already parsed this method will not return anything as form data parsing does not cache the data like this method does. To implicitly invoke form data parsing function set `parse_form_data` to `True`. When this is done the return value of this method will be an empty string if the form parser handles the data. This generally is not necessary as if the whole data is cached (which is the default) the form parser will used the cached data to parse the form data. Please be generally aware of checking the content length first in any case before calling this method to avoid exhausting server memory.
If `as_text` is set to `True` the return value will be a decoded string.
Changelog
Added in version 0.9.

Parameters:

  * **cache** (
  * **as_text** (
  * **parse_form_data** (



Return type:


get_json(_force =False_, _silent =False_, _cache =True_)[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_json "Link to this definition")

Parse [`data`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.data "flask.Request.data") as JSON.
If the mimetype does not indicate JSON (_application/json_ , see [`is_json`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.is_json "flask.Request.is_json")), or parsing fails, [`on_json_loading_failed()`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.on_json_loading_failed "flask.Request.on_json_loading_failed") is called and its return value is used as the return value. By default this raises a 415 Unsupported Media Type resp.

Parameters:

  * **force** (
  * **silent** (`None` instead.
  * **cache** (



Return type:
Changelog
Changed in version 2.3: Raise a 415 error instead of 400.
Changed in version 2.1: Raise a 400 error if the content type is incorrect.

_property_ host _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.host "Link to this definition")

The host name the request was made to, including the port if it’s non-standard. Validated with [`trusted_hosts`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.trusted_hosts "flask.Request.trusted_hosts").

_property_ host_url _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.host_url "Link to this definition")

The request URL scheme and host only.

_property_ if_match _:[ ETags](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.ETags "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.if_match "Link to this definition")

An object containing all the etags in the `If-Match` header.

Return type:

[`ETags`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.ETags "\(in Werkzeug v3.1.x\)")

_property_ if_modified_since _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.if_modified_since "Link to this definition")

The parsed `If-Modified-Since` header as a datetime object.
Changelog
Changed in version 2.0: The datetime object is timezone-aware.

_property_ if_none_match _:[ ETags](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.ETags "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.if_none_match "Link to this definition")

An object containing all the etags in the `If-None-Match` header.

Return type:

[`ETags`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.ETags "\(in Werkzeug v3.1.x\)")

_property_ if_range _:[ IfRange](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.IfRange "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.if_range "Link to this definition")

The parsed `If-Range` header.
Changelog
Changed in version 2.0: `IfRange.date` is timezone-aware.
Added in version 0.7.

_property_ if_unmodified_since _: |_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.if_unmodified_since "Link to this definition")

The parsed `If-Unmodified-Since` header as a datetime object.
Changelog
Changed in version 2.0: The datetime object is timezone-aware.

input_stream[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.input_stream "Link to this definition")

The raw WSGI input stream, without any safety checks.
This is dangerous to use. It does not guard against infinite streams or reading past [`content_length`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.content_length "flask.Request.content_length") or [`max_content_length`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.max_content_length "flask.Request.max_content_length").
Use [`stream`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.stream "flask.Request.stream") instead.

_property_ is_json _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.is_json "Link to this definition")

Check if the mimetype indicates JSON data, either _application/json_ or _application/*+json_.

is_multiprocess[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.is_multiprocess "Link to this definition")

boolean that is `True` if the application is served by a WSGI server that spawns multiple processes.

is_multithread[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.is_multithread "Link to this definition")

boolean that is `True` if the application is served by a multithreaded WSGI server.

is_run_once[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.is_run_once "Link to this definition")

boolean that is `True` if the application will be executed only once in a process lifetime. This is the case for CGI for example, but it’s not guaranteed that the execution only happens one time.

_property_ is_secure _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.is_secure "Link to this definition")

`True` if the request was made with a secure protocol (HTTPS or WSS).

_property_ json _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.json "Link to this definition")

The parsed JSON data if [`mimetype`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.mimetype "flask.Request.mimetype") indicates JSON (_application/json_ , see [`is_json`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.is_json "flask.Request.is_json")).
Calls [`get_json()`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_json "flask.Request.get_json") with default arguments.
If the request content type is not `application/json`, this will raise a 415 Unsupported Media Type error.
Changelog
Changed in version 2.3: Raise a 415 error instead of 400.
Changed in version 2.1: Raise a 400 error if the content type is incorrect.

list_storage_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.list_storage_class "Link to this definition")

alias of [`ImmutableList`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.ImmutableList "\(in Werkzeug v3.1.x\)")

make_form_data_parser()[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.make_form_data_parser "Link to this definition")

Creates the form data parser. Instantiates the [`form_data_parser_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.form_data_parser_class "flask.Request.form_data_parser_class") with some parameters.
Changelog
Added in version 0.8.

Return type:

[_FormDataParser_](https://werkzeug.palletsprojects.com/en/stable/http/#werkzeug.formparser.FormDataParser "\(in Werkzeug v3.1.x\)")

max_forwards[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.max_forwards "Link to this definition")

The Max-Forwards request-header field provides a mechanism with the TRACE and OPTIONS methods to limit the number of proxies or gateways that can forward the request to the next inbound server.

_property_ mimetype _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.mimetype "Link to this definition")

Like [`content_type`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.content_type "flask.Request.content_type"), but without parameters (eg, without charset, type etc.) and always lowercase. For example if the content type is `text/HTML; charset=utf-8` the mimetype would be `'text/html'`.

_property_ mimetype_params _:[,]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.mimetype_params "Link to this definition")

The mimetype parameters as dict. For example if the content type is `text/html; charset=utf-8` the params would be `{'charset': 'utf-8'}`.

origin[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.origin "Link to this definition")

The host that the request originated from. Set `access_control_allow_origin` on the response to indicate which origins are allowed.

parameter_storage_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.parameter_storage_class "Link to this definition")

alias of `ImmutableMultiDict`

_property_ pragma _:[ HeaderSet](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.HeaderSet "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.pragma "Link to this definition")

The Pragma general-header field is used to include implementation-specific directives that might apply to any recipient along the request/response chain. All pragma directives specify optional behavior from the viewpoint of the protocol; however, some systems MAY require that behavior be consistent with the directives.

_property_ range _:[ Range](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.Range "\(in Werkzeug v3.1.x\)")|_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.range "Link to this definition")

The parsed `Range` header.
Changelog
Added in version 0.7.

Return type:

[`Range`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.Range "\(in Werkzeug v3.1.x\)")

referrer[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.referrer "Link to this definition")

The Referer[sic] request-header field allows the client to specify, for the server’s benefit, the address (URI) of the resource from which the Request-URI was obtained (the “referrer”, although the header field is misspelled).

remote_user[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.remote_user "Link to this definition")

If the server supports user authentication, and the script is protected, this attribute contains the username the user has authenticated as.

_property_ root_url _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.root_url "Link to this definition")

The request URL scheme, host, and root path. This is the root that the application is accessed from.

_property_ script_root _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.script_root "Link to this definition")

Alias for `self.root_path`. `environ["SCRIPT_NAME"]` without a trailing slash.

_property_ stream _:[]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.stream "Link to this definition")

The WSGI input stream, with safety checks. This stream can only be consumed once.
Use [`get_data()`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_data "flask.Request.get_data") to get the full data as bytes or text. The [`data`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.data "flask.Request.data") attribute will contain the full bytes only if they do not represent form data. The [`form`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.form "flask.Request.form") attribute will contain the parsed form data in that case.
Unlike [`input_stream`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.input_stream "flask.Request.input_stream"), this stream guards against infinite streams or reading past [`content_length`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.content_length "flask.Request.content_length") or [`max_content_length`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.max_content_length "flask.Request.max_content_length").
If `max_content_length` is set, it can be enforced on streams if `wsgi.input_terminated` is set. Otherwise, an empty stream is returned.
If the limit is reached before the underlying stream is exhausted (such as a file that is too large, or an infinite stream), the remaining contents of the stream cannot be read safely. Depending on how the server handles this, clients may show a “connection reset” failure instead of seeing the 413 response.
Changelog
Changed in version 2.3: Check `max_content_length` preemptively and while reading.
Changed in version 0.9: The stream is always set (but may be consumed) even if form parsing was accessed first.

trusted_hosts _:[]|__= None_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.trusted_hosts "Link to this definition")

Valid host names when handling requests. By default all hosts are trusted, which means that whatever the client says the host is will be accepted.
Because `Host` and `X-Forwarded-Host` headers can be set to any value by a malicious client, it is recommended to either set this property or implement similar validation in the proxy (if the application is being run behind one).
Changelog
Added in version 0.9.

_property_ url _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.url "Link to this definition")

The full request URL with the scheme, host, root path, path, and query string.

_property_ url_root _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.url_root "Link to this definition")

Alias for [`root_url`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.root_url "flask.Request.root_url"). The URL with scheme, host, and root path. For example, `https://example.com/app/`.

_property_ user_agent _:[ UserAgent](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.user_agent.UserAgent "\(in Werkzeug v3.1.x\)")_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.user_agent "Link to this definition")

The user agent. Use `user_agent.string` to get the header value. Set [`user_agent_class`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.user_agent_class "flask.Request.user_agent_class") to a subclass of [`UserAgent`](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.user_agent.UserAgent "\(in Werkzeug v3.1.x\)") to provide parsing for the other properties or other extended data.
Changelog
Changed in version 2.1: The built-in parser was removed. Set `user_agent_class` to a `UserAgent` subclass to parse data from the string.

user_agent_class[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.user_agent_class "Link to this definition")

alias of [`UserAgent`](https://werkzeug.palletsprojects.com/en/stable/utils/#werkzeug.user_agent.UserAgent "\(in Werkzeug v3.1.x\)")

_property_ values _:[ CombinedMultiDict](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.CombinedMultiDict "\(in Werkzeug v3.1.x\)")[,]_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.values "Link to this definition")

A [`werkzeug.datastructures.CombinedMultiDict`](https://werkzeug.palletsprojects.com/en/stable/datastructures/#werkzeug.datastructures.CombinedMultiDict "\(in Werkzeug v3.1.x\)") that combines [`args`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.args "flask.Request.args") and [`form`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.form "flask.Request.form").
For GET requests, only `args` are present, not `form`.
Changelog
Changed in version 2.0: For GET requests, only `args` are present, not `form`.

_property_ want_form_data_parsed _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.want_form_data_parsed "Link to this definition")

`True` if the request method carries content. By default this is true if a `Content-Type` is sent.
Changelog
Added in version 0.8.

environ _: WSGIEnvironment_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.environ "Link to this definition")

The WSGI environment containing HTTP headers and information from the WSGI server.

shallow _:_[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.shallow "Link to this definition")

Set when creating the request object. If `True`, reading from the request body will cause a `RuntimeException`. Useful to prevent modifying the stream from middleware.

method[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.method "Link to this definition")

The method the request was made with, such as `GET`.

scheme[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.scheme "Link to this definition")

The URL scheme of the protocol the request used, such as `https` or `wss`.

server[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.server "Link to this definition")

The address of the server. `(host, port)`, `(path, None)` for unix sockets, or `None` if not known.

root_path[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.root_path "Link to this definition")

The prefix that the application is mounted under, without a trailing slash. [`path`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.path "flask.Request.path") comes after this.

path[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.path "Link to this definition")

The path part of the URL after [`root_path`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.root_path "flask.Request.root_path"). This is the path used for routing within the application.

query_string[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.query_string "Link to this definition")

The part of the URL after the “?”. This is the raw value, use [`args`](https://flask.palletsprojects.com/en/stable/api/#flask.Request.args "flask.Request.args") for the parsed values.

headers[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.headers "Link to this definition")

The headers received with the request.

remote_addr[¶](https://flask.palletsprojects.com/en/stable/api/#flask.Request.remote_addr "Link to this definition")

The address of the client sending the request.

flask.request[¶](https://flask.palletsprojects.com/en/stable/api/#flask.request "Link to this definition")

To access incoming request data, you can use the global `request` object. Flask parses incoming request data for you and gives you access to it through that global object. Internally Flask makes sure that you always get the correct data for the active thread if you are in a multithreaded environment.
This is a proxy. See [Notes On Proxies](https://flask.palletsprojects.com/en/stable/reqcontext/#notes-on-proxies) for more information.
The request object is an instance of a [`Request`](https://flask.palletsprojects.com/en/stable/api/#flask.Request "flask.Request").
