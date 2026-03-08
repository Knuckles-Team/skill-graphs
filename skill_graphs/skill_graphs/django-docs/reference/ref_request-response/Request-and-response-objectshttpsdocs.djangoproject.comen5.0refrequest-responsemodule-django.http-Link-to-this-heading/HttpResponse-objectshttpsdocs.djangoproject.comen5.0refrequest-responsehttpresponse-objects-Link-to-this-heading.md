##  `HttpResponse` objects[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#httpresponse-objects "Link to this heading")

_class_ HttpResponse[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponse)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "Link to this definition")

In contrast to [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") objects, which are created automatically by Django, [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") objects are your responsibility. Each view you write is responsible for instantiating, populating, and returning an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse").
The [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") class lives in the [`django.http`](https://docs.djangoproject.com/en/5.0/ref/request-response/#module-django.http "django.http: Classes dealing with HTTP requests and responses.") module.
### Usage[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#usage "Link to this heading")
#### Passing strings[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#passing-strings "Link to this heading")
Typical usage is to pass the contents of the page, as a string, bytestring, or [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") constructor:
```
>>> from django.http import HttpResponse
>>> response = HttpResponse("Here's the text of the web page.")
>>> response = HttpResponse("Text only, please.", content_type="text/plain")
>>> response = HttpResponse(b"Bytestrings are also accepted.")
>>> response = HttpResponse(memoryview(b"Memoryview as well."))

```

But if you want to add content incrementally, you can use `response` as a file-like object:
```
>>> response = HttpResponse()
>>> response.write("<p>Here's the text of the web page.</p>")
>>> response.write("<p>Here's another paragraph.</p>")

```

#### Passing iterators[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#passing-iterators "Link to this heading")
Finally, you can pass `HttpResponse` an iterator rather than strings. `HttpResponse` will consume the iterator immediately, store its content as a string, and discard it. Objects with a `close()` method such as files and generators are immediately closed.
If you need the response to be streamed from the iterator to the client, you must use the [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") class instead.
#### Setting header fields[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#setting-header-fields "Link to this heading")
To set or remove a header field in your response, use [`HttpResponse.headers`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.headers "django.http.HttpResponse.headers"):
```
>>> response = HttpResponse()
>>> response.headers["Age"] = 120
>>> del response.headers["Age"]

```

You can also manipulate headers by treating your response like a dictionary:
```
>>> response = HttpResponse()
>>> response["Age"] = 120
>>> del response["Age"]

```

This proxies to `HttpResponse.headers`, and is the original interface offered by `HttpResponse`.
When using this interface, unlike a dictionary, `del` doesn’t raise `KeyError` if the header field doesn’t exist.
You can also set headers on instantiation:
```
>>> response = HttpResponse(headers={"Age": 120})

```

For setting the `Cache-Control` and `Vary` header fields, it is recommended to use the [`patch_cache_control()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.patch_cache_control "django.utils.cache.patch_cache_control") and [`patch_vary_headers()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.patch_vary_headers "django.utils.cache.patch_vary_headers") methods from [`django.utils.cache`](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.cache "django.utils.cache: Helper functions for controlling caching."), since these fields can have multiple, comma-separated values. The “patch” methods ensure that other values, e.g. added by a middleware, are not removed.
HTTP header fields cannot contain newlines. An attempt to set a header field containing a newline character (CR or LF) will raise `BadHeaderError`
#### Telling the browser to treat the response as a file attachment[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#telling-the-browser-to-treat-the-response-as-a-file-attachment "Link to this heading")
To tell the browser to treat the response as a file attachment, set the `Content-Type` and `Content-Disposition` headers. For example, this is how you might return a Microsoft Excel spreadsheet:
```
>>> response = HttpResponse(
...     my_data,
...     headers={
...         "Content-Type": "application/vnd.ms-excel",
...         "Content-Disposition": 'attachment; filename="foo.xls"',
...     },
... )

```

There’s nothing Django-specific about the `Content-Disposition` header, but it’s easy to forget the syntax, so we’ve included it here.
### Attributes[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#id3 "Link to this heading")

HttpResponse.content[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.content "Link to this definition")

A bytestring representing the content, encoded from a string if necessary.

HttpResponse.cookies[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.cookies "Link to this definition")

A

HttpResponse.headers[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.headers "Link to this definition")

A case insensitive, dict-like object that provides an interface to all HTTP headers on the response, except a `Set-Cookie` header. See [Setting header fields](https://docs.djangoproject.com/en/5.0/ref/request-response/#setting-header-fields) and [`HttpResponse.cookies`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.cookies "django.http.HttpResponse.cookies").

HttpResponse.charset[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.charset "Link to this definition")

A string denoting the charset in which the response will be encoded. If not given at `HttpResponse` instantiation time, it will be extracted from `content_type` and if that is unsuccessful, the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_CHARSET) setting will be used.

HttpResponse.status_code[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.status_code "Link to this definition")

The
Unless [`reason_phrase`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.reason_phrase "django.http.HttpResponse.reason_phrase") is explicitly set, modifying the value of `status_code` outside the constructor will also modify the value of `reason_phrase`.

HttpResponse.reason_phrase[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.reason_phrase "Link to this definition")

The HTTP reason phrase for the response. It uses the
Unless explicitly set, `reason_phrase` is determined by the value of [`status_code`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.status_code "django.http.HttpResponse.status_code").

HttpResponse.streaming[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.streaming "Link to this definition")

This is always `False`.
This attribute exists so middleware can treat streaming responses differently from regular responses.

HttpResponse.closed[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.closed "Link to this definition")

`True` if the response has been closed.
### Methods[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#id4 "Link to this heading")

HttpResponse.__init__(_content =b''_, _content_type =None_, _status =200_, _reason =None_, _charset =None_, _headers =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponse.__init__)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.__init__ "Link to this definition")

Instantiates an `HttpResponse` object with the given page content, content type, and headers.
`content` is most commonly an iterator, bytestring,
`content_type` is the MIME type optionally completed by a character set encoding and is used to fill the HTTP `Content-Type` header. If not specified, it is formed by `'text/html'` and the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_CHARSET) settings, by default: `"text/html; charset=utf-8"`.
`status` is the `HTTPStatus.NO_CONTENT`.
`reason` is the HTTP response phrase. If not provided, a default phrase will be used.
`charset` is the charset in which the response will be encoded. If not given it will be extracted from `content_type`, and if that is unsuccessful, the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_CHARSET) setting will be used.
`headers` is a

HttpResponse.__setitem__(_header_ , _value_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.__setitem__ "Link to this definition")

Sets the given header name to the given value. Both `header` and `value` should be strings.

HttpResponse.__delitem__(_header_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.__delitem__ "Link to this definition")

Deletes the header with the given name. Fails silently if the header doesn’t exist. Case-insensitive.

HttpResponse.__getitem__(_header_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.__getitem__ "Link to this definition")

Returns the value for the given header name. Case-insensitive.

HttpResponse.get(_header_ , _alternate =None_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.get "Link to this definition")

Returns the value for the given header, or an `alternate` if the header doesn’t exist.

HttpResponse.has_header(_header_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.has_header "Link to this definition")

Returns `True` or `False` based on a case-insensitive check for a header with the given name.

HttpResponse.items()[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.items "Link to this definition")

Acts like

HttpResponse.setdefault(_header_ , _value_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.setdefault "Link to this definition")

Sets a header unless it has already been set.

HttpResponse.set_cookie(_key_ , _value =''_, _max_age =None_, _expires =None_, _path ='/'_, _domain =None_, _secure =False_, _httponly =False_, _samesite =None_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.set_cookie "Link to this definition")

Sets a cookie. The parameters are the same as in the
  * `max_age` should be a `None` (default) if the cookie should last only as long as the client’s browser session. If `expires` is not specified, it will be calculated.
  * `expires` should either be a string in the format `"Wdy, DD-Mon-YY HH:MM:SS GMT"` or a `datetime.datetime` object in UTC. If `expires` is a `datetime` object, the `max_age` will be calculated.
  * Use `domain` if you want to set a cross-domain cookie. For example, `domain="example.com"` will set a cookie that is readable by the domains www.example.com, blog.example.com, etc. Otherwise, a cookie will only be readable by the domain that set it.
  * Use `secure=True` if you want the cookie to be only sent to the server when a request is made with the `https` scheme.
  * Use `httponly=True` if you want to prevent client-side JavaScript from having access to the cookie.
  * Use `samesite='Strict'` or `samesite='Lax'` to tell the browser not to send this cookie when performing a cross-origin request.
Use `samesite='None'` (string) to explicitly state that this cookie is sent with all same-site and cross-site requests.


Warning

HttpResponse.set_signed_cookie(_key_ , _value_ , _salt =''_, _max_age =None_, _expires =None_, _path ='/'_, _domain =None_, _secure =False_, _httponly =False_, _samesite =None_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.set_signed_cookie "Link to this definition")

Like [`set_cookie()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.set_cookie "django.http.HttpResponse.set_cookie"), but [cryptographic signing](https://docs.djangoproject.com/en/5.0/topics/signing/) the cookie before setting it. Use in conjunction with [`HttpRequest.get_signed_cookie()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_signed_cookie "django.http.HttpRequest.get_signed_cookie"). You can use the optional `salt` argument for added key strength, but you will need to remember to pass it to the corresponding [`HttpRequest.get_signed_cookie()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_signed_cookie "django.http.HttpRequest.get_signed_cookie") call.

HttpResponse.delete_cookie(_key_ , _path ='/'_, _domain =None_, _samesite =None_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.delete_cookie "Link to this definition")

Deletes the cookie with the given key. Fails silently if the key doesn’t exist.
Due to the way cookies work, `path` and `domain` should be the same values you used in `set_cookie()` – otherwise the cookie may not be deleted.

HttpResponse.close()[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.close "Link to this definition")

This method is called at the end of the request directly by the WSGI server.

HttpResponse.write(_content_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponse.write)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.write "Link to this definition")

This method makes an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") instance a file-like object.

HttpResponse.flush()[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.flush "Link to this definition")

This method makes an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") instance a file-like object.

HttpResponse.tell()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponse.tell)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.tell "Link to this definition")

This method makes an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") instance a file-like object.

HttpResponse.getvalue()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponse.getvalue)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.getvalue "Link to this definition")

Returns the value of [`HttpResponse.content`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.content "django.http.HttpResponse.content"). This method makes an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") instance a stream-like object.

HttpResponse.readable()[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.readable "Link to this definition")

Always `False`. This method makes an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") instance a stream-like object.

HttpResponse.seekable()[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.seekable "Link to this definition")

Always `False`. This method makes an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") instance a stream-like object.

HttpResponse.writable()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponse.writable)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.writable "Link to this definition")

Always `True`. This method makes an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") instance a stream-like object.

HttpResponse.writelines(_lines_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponse.writelines)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.writelines "Link to this definition")

Writes a list of lines to the response. Line separators are not added. This method makes an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") instance a stream-like object.
###  `HttpResponse` subclasses[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#httpresponse-subclasses "Link to this heading")
Django includes a number of `HttpResponse` subclasses that handle different types of HTTP responses. Like `HttpResponse`, these subclasses live in [`django.http`](https://docs.djangoproject.com/en/5.0/ref/request-response/#module-django.http "django.http: Classes dealing with HTTP requests and responses.").

_class_ HttpResponseRedirect[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponseRedirect)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect "Link to this definition")

The first argument to the constructor is required – the path to redirect to. This can be a fully qualified URL (e.g. `'https://www.yahoo.com/search/'`), an absolute path with no domain (e.g. `'/search/'`), or even a relative path (e.g. `'search/'`). In that last case, the client browser will reconstruct the full URL itself according to the current path. See [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") for other optional constructor arguments. Note that this returns an HTTP status code 302.

url[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect.url "Link to this definition")

This read-only attribute represents the URL the response will redirect to (equivalent to the `Location` response header).

_class_ HttpResponsePermanentRedirect[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponsePermanentRedirect)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponsePermanentRedirect "Link to this definition")

Like [`HttpResponseRedirect`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseRedirect "django.http.HttpResponseRedirect"), but it returns a permanent redirect (HTTP status code 301) instead of a “found” redirect (status code 302).

_class_ HttpResponseNotModified[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponseNotModified)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotModified "Link to this definition")

The constructor doesn’t take any arguments and no content should be added to this response. Use this to designate that a page hasn’t been modified since the user’s last request (status code 304).

_class_ HttpResponseBadRequest[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponseBadRequest)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseBadRequest "Link to this definition")

Acts just like [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") but uses a 400 status code.

_class_ HttpResponseNotFound[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponseNotFound)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotFound "Link to this definition")

Acts just like [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") but uses a 404 status code.

_class_ HttpResponseForbidden[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponseForbidden)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseForbidden "Link to this definition")

Acts just like [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") but uses a 403 status code.

_class_ HttpResponseNotAllowed[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponseNotAllowed)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseNotAllowed "Link to this definition")

Like [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse"), but uses a 405 status code. The first argument to the constructor is required: a list of permitted methods (e.g. `['GET', 'POST']`).

_class_ HttpResponseGone[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponseGone)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseGone "Link to this definition")

Acts just like [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") but uses a 410 status code.

_class_ HttpResponseServerError[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/response/#HttpResponseServerError)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponseServerError "Link to this definition")

Acts just like [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") but uses a 500 status code.
Note
If a custom subclass of [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") implements a `render` method, Django will treat it as emulating a [`SimpleTemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse "django.template.response.SimpleTemplateResponse"), and the `render` method must itself return a valid response object.
#### Custom response classes[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#custom-response-classes "Link to this heading")
If you find yourself needing a response class that Django doesn’t provide, you can create it with the help of
```
from http import HTTPStatus
from django.http import HttpResponse


class HttpResponseNoContent(HttpResponse):
    status_code = HTTPStatus.NO_CONTENT

```
