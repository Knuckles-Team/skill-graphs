##  `HttpRequest` objects[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#httprequest-objects "Link to this heading")

_class_ HttpRequest[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "Link to this definition")

### Attributes[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#attributes "Link to this heading")
All attributes should be considered read-only, unless stated otherwise.

HttpRequest.scheme[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.scheme "Link to this definition")

A string representing the scheme of the request (`http` or `https` usually).

HttpRequest.body[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.body "Link to this definition")

The raw HTTP request body as a bytestring. This is useful for processing data in different ways than conventional HTML forms: binary images, XML payload etc. For processing conventional form data, use [`HttpRequest.POST`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.POST "django.http.HttpRequest.POST").
You can also read from an `HttpRequest` using a file-like interface with [`HttpRequest.read()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.read "django.http.HttpRequest.read") or [`HttpRequest.readline()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.readline "django.http.HttpRequest.readline"). Accessing the `body` attribute _after_ reading the request with either of these I/O stream methods will produce a `RawPostDataException`.

HttpRequest.path[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.path "Link to this definition")

A string representing the full path to the requested page, not including the scheme, domain, or query string.
Example: `"/music/bands/the_beatles/"`

HttpRequest.path_info[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.path_info "Link to this definition")

Under some web server configurations, the portion of the URL after the host name is split up into a script prefix portion and a path info portion. The `path_info` attribute always contains the path info portion of the path, no matter what web server is being used. Using this instead of [`path`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.path "django.http.HttpRequest.path") can make your code easier to move between test and deployment servers.
For example, if the `WSGIScriptAlias` for your application is set to `"/minfo"`, then `path` might be `"/minfo/music/bands/the_beatles/"` and `path_info` would be `"/music/bands/the_beatles/"`.

HttpRequest.method[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method "Link to this definition")

A string representing the HTTP method used in the request. This is guaranteed to be uppercase. For example:
```
if request.method == "GET":
    do_something()
elif request.method == "POST":
    do_something_else()

```


HttpRequest.encoding[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.encoding "Link to this definition")

A string representing the current encoding used to decode form submission data (or `None`, which means the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_CHARSET) setting is used). You can write to this attribute to change the encoding used when accessing the form data. Any subsequent attribute accesses (such as reading from [`GET`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.GET "django.http.HttpRequest.GET") or [`POST`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.POST "django.http.HttpRequest.POST")) will use the new `encoding` value. Useful if you know the form data is not in the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_CHARSET) encoding.

HttpRequest.content_type[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.content_type "Link to this definition")

A string representing the MIME type of the request, parsed from the `CONTENT_TYPE` header.

HttpRequest.content_params[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.content_params "Link to this definition")

A dictionary of key/value parameters included in the `CONTENT_TYPE` header.

HttpRequest.GET[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.GET "Link to this definition")

A dictionary-like object containing all given HTTP GET parameters. See the [`QueryDict`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict "django.http.QueryDict") documentation below.

HttpRequest.POST[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.POST "Link to this definition")

A dictionary-like object containing all given HTTP POST parameters, providing that the request contains form data. See the [`QueryDict`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict "django.http.QueryDict") documentation below. If you need to access raw or non-form data posted in the request, access this through the [`HttpRequest.body`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.body "django.http.HttpRequest.body") attribute instead.
It’s possible that a request can come in via POST with an empty `POST` dictionary – if, say, a form is requested via the POST HTTP method but does not include form data. Therefore, you shouldn’t use `if request.POST` to check for use of the POST method; instead, use `if request.method == "POST"` (see [`HttpRequest.method`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.method "django.http.HttpRequest.method")).
`POST` does _not_ include file-upload information. See [`FILES`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.FILES "django.http.HttpRequest.FILES").

HttpRequest.COOKIES[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.COOKIES "Link to this definition")

A dictionary containing all cookies. Keys and values are strings.

HttpRequest.FILES[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.FILES "Link to this definition")

A dictionary-like object containing all uploaded files. Each key in `FILES` is the `name` from the `<input type="file" name="">`. Each value in `FILES` is an [`UploadedFile`](https://docs.djangoproject.com/en/5.0/ref/files/uploads/#django.core.files.uploadedfile.UploadedFile "django.core.files.uploadedfile.UploadedFile").
See [Managing files](https://docs.djangoproject.com/en/5.0/topics/files/) for more information.
`FILES` will only contain data if the request method was POST and the `<form>` that posted to the request had `enctype="multipart/form-data"`. Otherwise, `FILES` will be a blank dictionary-like object.

HttpRequest.META[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.META "Link to this definition")

A dictionary containing all available HTTP headers. Available headers depend on the client and server, but here are some examples:
  * `CONTENT_LENGTH` – The length of the request body (as a string).
  * `CONTENT_TYPE` – The MIME type of the request body.
  * `HTTP_ACCEPT` – Acceptable content types for the response.
  * `HTTP_ACCEPT_ENCODING` – Acceptable encodings for the response.
  * `HTTP_ACCEPT_LANGUAGE` – Acceptable languages for the response.
  * `HTTP_HOST` – The HTTP Host header sent by the client.
  * `HTTP_REFERER` – The referring page, if any.
  * `HTTP_USER_AGENT` – The client’s user-agent string.
  * `QUERY_STRING` – The query string, as a single (unparsed) string.
  * `REMOTE_ADDR` – The IP address of the client.
  * `REMOTE_HOST` – The hostname of the client.
  * `REMOTE_USER` – The user authenticated by the web server, if any.
  * `REQUEST_METHOD` – A string such as `"GET"` or `"POST"`.
  * `SERVER_NAME` – The hostname of the server.
  * `SERVER_PORT` – The port of the server (as a string).


With the exception of `CONTENT_LENGTH` and `CONTENT_TYPE`, as given above, any HTTP headers in the request are converted to `META` keys by converting all characters to uppercase, replacing any hyphens with underscores and adding an `HTTP_` prefix to the name. So, for example, a header called `X-Bender` would be mapped to the `META` key `HTTP_X_BENDER`.
Note that [`runserver`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-runserver) strips all headers with underscores in the name, so you won’t see them in `META`. This prevents header-spoofing based on ambiguity between underscores and dashes both being normalizing to underscores in WSGI environment variables. It matches the behavior of web servers like Nginx and Apache 2.4+.
[`HttpRequest.headers`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.headers "django.http.HttpRequest.headers") is a simpler way to access all HTTP-prefixed headers, plus `CONTENT_LENGTH` and `CONTENT_TYPE`.

HttpRequest.headers[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.headers "Link to this definition")

A case insensitive, dict-like object that provides access to all HTTP-prefixed headers (plus `Content-Length` and `Content-Type`) from the request.
The name of each header is stylized with title-casing (e.g. `User-Agent`) when it’s displayed. You can access headers case-insensitively:
```
>>> request.headers
{'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6', ...}

>>> "User-Agent" in request.headers
True
>>> "user-agent" in request.headers
True

>>> request.headers["User-Agent"]
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)
>>> request.headers["user-agent"]
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)

>>> request.headers.get("User-Agent")
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)
>>> request.headers.get("user-agent")
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)

```

For use in, for example, Django templates, headers can also be looked up using underscores in place of hyphens:
```
{{ request.headers.user_agent }}

```


HttpRequest.resolver_match[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.resolver_match "Link to this definition")

An instance of [`ResolverMatch`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch "django.urls.ResolverMatch") representing the resolved URL. This attribute is only set after URL resolving took place, which means it’s available in all views but not in middleware which are executed before URL resolving takes place (you can use it in [`process_view()`](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#process_view "process_view") though).
### Attributes set by application code[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#attributes-set-by-application-code "Link to this heading")
Django doesn’t set these attributes itself but makes use of them if set by your application.

HttpRequest.current_app[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.current_app "Link to this definition")

The [`url`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatetag-url) template tag will use its value as the `current_app` argument to [`reverse()`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.reverse "django.urls.reverse").

HttpRequest.urlconf[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.urlconf "Link to this definition")

This will be used as the root URLconf for the current request, overriding the [`ROOT_URLCONF`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ROOT_URLCONF) setting. See [How Django processes a request](https://docs.djangoproject.com/en/5.0/topics/http/urls/#how-django-processes-a-request) for details.
`urlconf` can be set to `None` to revert any changes made by previous middleware and return to using the [`ROOT_URLCONF`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ROOT_URLCONF).

HttpRequest.exception_reporter_filter[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.exception_reporter_filter "Link to this definition")

This will be used instead of [`DEFAULT_EXCEPTION_REPORTER_FILTER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_EXCEPTION_REPORTER_FILTER) for the current request. See [Custom error reports](https://docs.djangoproject.com/en/5.0/howto/error-reporting/#custom-error-reports) for details.

HttpRequest.exception_reporter_class[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.exception_reporter_class "Link to this definition")

This will be used instead of [`DEFAULT_EXCEPTION_REPORTER`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_EXCEPTION_REPORTER) for the current request. See [Custom error reports](https://docs.djangoproject.com/en/5.0/howto/error-reporting/#custom-error-reports) for details.
### Attributes set by middleware[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#attributes-set-by-middleware "Link to this heading")
Some of the middleware included in Django’s contrib apps set attributes on the request. If you don’t see the attribute on a request, be sure the appropriate middleware class is listed in [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE).

HttpRequest.session[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.session "Link to this definition")

From the [`SessionMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware "django.contrib.sessions.middleware.SessionMiddleware"): A readable and writable, dictionary-like object that represents the current session.

HttpRequest.site[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.site "Link to this definition")

From the [`CurrentSiteMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.sites.middleware.CurrentSiteMiddleware "django.contrib.sites.middleware.CurrentSiteMiddleware"): An instance of [`Site`](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/#django.contrib.sites.models.Site "django.contrib.sites.models.Site") or [`RequestSite`](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/#django.contrib.sites.requests.RequestSite "django.contrib.sites.requests.RequestSite") as returned by [`get_current_site()`](https://docs.djangoproject.com/en/5.0/ref/contrib/sites/#django.contrib.sites.shortcuts.get_current_site "django.contrib.sites.shortcuts.get_current_site") representing the current site.

HttpRequest.user[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.user "Link to this definition")

From the [`AuthenticationMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware "django.contrib.auth.middleware.AuthenticationMiddleware"): An instance of [`AUTH_USER_MODEL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-AUTH_USER_MODEL) representing the currently logged-in user. If the user isn’t currently logged in, `user` will be set to an instance of [`AnonymousUser`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.AnonymousUser "django.contrib.auth.models.AnonymousUser"). You can tell them apart with [`is_authenticated`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated "django.contrib.auth.models.User.is_authenticated"), like so:
```
if request.user.is_authenticated:
    ...  # Do something for logged-in users.
else:
    ...  # Do something for anonymous users.

```

The [`auser()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.auser "django.http.HttpRequest.auser") method does the same thing but can be used from async contexts.
### Methods[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#methods "Link to this heading")

HttpRequest.auser()[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.auser "Link to this definition")

New in Django 5.0.
From the [`AuthenticationMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware "django.contrib.auth.middleware.AuthenticationMiddleware"): Coroutine. Returns an instance of [`AUTH_USER_MODEL`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-AUTH_USER_MODEL) representing the currently logged-in user. If the user isn’t currently logged in, `auser` will return an instance of [`AnonymousUser`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.AnonymousUser "django.contrib.auth.models.AnonymousUser"). This is similar to the [`user`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.user "django.http.HttpRequest.user") attribute but it works in async contexts.

HttpRequest.get_host()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.get_host)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_host "Link to this definition")

Returns the originating host of the request using information from the `HTTP_X_FORWARDED_HOST` (if [`USE_X_FORWARDED_HOST`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_X_FORWARDED_HOST) is enabled) and `HTTP_HOST` headers, in that order. If they don’t provide a value, the method uses a combination of `SERVER_NAME` and `SERVER_PORT` as detailed in
Example: `"127.0.0.1:8000"`
Raises `django.core.exceptions.DisallowedHost` if the host is not in [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ALLOWED_HOSTS) or the domain name is invalid according to
Note
The [`get_host()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host") method fails when the host is behind multiple proxies. One solution is to use middleware to rewrite the proxy headers, as in the following example:
```
class MultipleProxyMiddleware:
    FORWARDED_FOR_FIELDS = [
        "HTTP_X_FORWARDED_FOR",
        "HTTP_X_FORWARDED_HOST",
        "HTTP_X_FORWARDED_SERVER",
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Rewrites the proxy headers so that only the most
        recent proxy is used.
        """
        for field in self.FORWARDED_FOR_FIELDS:
            if field in request.META:
                if "," in request.META[field]:
                    parts = request.META[field].split(",")
                    request.META[field] = parts[-1].strip()
        return self.get_response(request)

```

This middleware should be positioned before any other middleware that relies on the value of [`get_host()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_host "django.http.HttpRequest.get_host") – for instance, [`CommonMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.CommonMiddleware "django.middleware.common.CommonMiddleware") or [`CsrfViewMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.csrf.CsrfViewMiddleware "django.middleware.csrf.CsrfViewMiddleware").

HttpRequest.get_port()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.get_port)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_port "Link to this definition")

Returns the originating port of the request using information from the `HTTP_X_FORWARDED_PORT` (if [`USE_X_FORWARDED_PORT`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_X_FORWARDED_PORT) is enabled) and `SERVER_PORT` `META` variables, in that order.

HttpRequest.get_full_path()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.get_full_path)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_full_path "Link to this definition")

Returns the `path`, plus an appended query string, if applicable.
Example: `"/music/bands/the_beatles/?print=true"`

HttpRequest.get_full_path_info()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.get_full_path_info)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_full_path_info "Link to this definition")

Like [`get_full_path()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_full_path "django.http.HttpRequest.get_full_path"), but uses [`path_info`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.path_info "django.http.HttpRequest.path_info") instead of [`path`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.path "django.http.HttpRequest.path").
Example: `"/minfo/music/bands/the_beatles/?print=true"`

HttpRequest.build_absolute_uri(_location =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.build_absolute_uri)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.build_absolute_uri "Link to this definition")

Returns the absolute URI form of `location`. If no location is provided, the location will be set to `request.get_full_path()`.
If the location is already an absolute URI, it will not be altered. Otherwise the absolute URI is built using the server variables available in this request. For example:
```
>>> request.build_absolute_uri()
'https://example.com/music/bands/the_beatles/?print=true'
>>> request.build_absolute_uri("/bands/")
'https://example.com/bands/'
>>> request.build_absolute_uri("https://example2.com/bands/")
'https://example2.com/bands/'

```

Note
Mixing HTTP and HTTPS on the same site is discouraged, therefore [`build_absolute_uri()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.build_absolute_uri "django.http.HttpRequest.build_absolute_uri") will always generate an absolute URI with the same scheme the current request has. If you need to redirect users to HTTPS, it’s best to let your web server redirect all HTTP traffic to HTTPS.

HttpRequest.get_signed_cookie(_key_ , _default =RAISE_ERROR_, _salt =''_, _max_age =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.get_signed_cookie)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.get_signed_cookie "Link to this definition")

Returns a cookie value for a signed cookie, or raises a `django.core.signing.BadSignature` exception if the signature is no longer valid. If you provide the `default` argument the exception will be suppressed and that default value will be returned instead.
The optional `salt` argument can be used to provide extra protection against brute force attacks on your secret key. If supplied, the `max_age` argument will be checked against the signed timestamp attached to the cookie value to ensure the cookie is not older than `max_age` seconds.
For example:
```
>>> request.get_signed_cookie("name")
'Tony'
>>> request.get_signed_cookie("name", salt="name-salt")
'Tony' # assuming cookie was set using the same salt
>>> request.get_signed_cookie("nonexistent-cookie")
KeyError: 'nonexistent-cookie'
>>> request.get_signed_cookie("nonexistent-cookie", False)
False
>>> request.get_signed_cookie("cookie-that-was-tampered-with")
BadSignature: ...
>>> request.get_signed_cookie("name", max_age=60)
SignatureExpired: Signature age 1677.3839159 > 60 seconds
>>> request.get_signed_cookie("name", False, max_age=60)
False

```

See [cryptographic signing](https://docs.djangoproject.com/en/5.0/topics/signing/) for more information.

HttpRequest.is_secure()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.is_secure)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.is_secure "Link to this definition")

Returns `True` if the request is secure; that is, if it was made with HTTPS.

HttpRequest.accepts(_mime_type_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.accepts)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.accepts "Link to this definition")

Returns `True` if the request `Accept` header matches the `mime_type` argument:
```
>>> request.accepts("text/html")
True

```

Most browsers send `Accept: */*` by default, so this would return `True` for all content types. Setting an explicit `Accept` header in API requests can be useful for returning a different content type for those consumers only. See [Content negotiation example](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-editing/#content-negotiation-example) of using `accepts()` to return different content to API consumers.
If a response varies depending on the content of the `Accept` header and you are using some form of caching like Django’s [`cache middleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#module-django.middleware.cache "django.middleware.cache: Middleware for the site-wide cache."), you should decorate the view with [`vary_on_headers('Accept')`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.vary.vary_on_headers "django.views.decorators.vary.vary_on_headers") so that the responses are properly cached.

HttpRequest.read(_size =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.read)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.read "Link to this definition")


HttpRequest.readline()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.readline)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.readline "Link to this definition")


HttpRequest.readlines()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.readlines)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.readlines "Link to this definition")


HttpRequest.__iter__()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#HttpRequest.__iter__)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.__iter__ "Link to this definition")

Methods implementing a file-like interface for reading from an `HttpRequest` instance. This makes it possible to consume an incoming request in a streaming fashion. A common use-case would be to process a big XML payload with an iterative parser without constructing a whole XML tree in memory.
Given this standard interface, an `HttpRequest` instance can be passed directly to an XML parser such as
```
import xml.etree.ElementTree as ET

for element in ET.iterparse(request):
    process(element)

```
