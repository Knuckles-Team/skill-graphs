## The test client[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#the-test-client "Link to this heading")
The test client is a Python class that acts as a dummy web browser, allowing you to test your views and interact with your Django-powered application programmatically.
Some of the things you can do with the test client are:
  * Simulate GET and POST requests on a URL and observe the response – everything from low-level HTTP (result headers and status codes) to page content.
  * See the chain of redirects (if any) and check the URL and status code at each step.
  * Test that a given request is rendered by a given Django template, with a template context that contains certain values.


Note that the test client is not intended to be a replacement for
  * Use Django’s test client to establish that the correct template is being rendered and that the template is passed the correct context data.
  * Use [`RequestFactory`](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#django.test.RequestFactory "django.test.RequestFactory") to test view functions directly, bypassing the routing and middleware layers.
  * Use in-browser frameworks like _rendered_ HTML and the _behavior_ of web pages, namely JavaScript functionality. Django also provides special support for those frameworks; see the section on [`LiveServerTestCase`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.LiveServerTestCase "django.test.LiveServerTestCase") for more details.


A comprehensive test suite should use a combination of all of these test types.
### Overview and a quick example[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#overview-and-a-quick-example "Link to this heading")
To use the test client, instantiate `django.test.Client` and retrieve web pages:
```
>>> from django.test import Client
>>> c = Client()
>>> response = c.post("/login/", {"username": "john", "password": "smith"})
>>> response.status_code
200
>>> response = c.get("/customer/details/")
>>> response.content
b'<!DOCTYPE html...'

```

As this example suggests, you can instantiate `Client` from within a session of the Python interactive interpreter.
Note a few important things about how the test client works:
  * The test client does _not_ require the web server to be running. In fact, it will run just fine with no web server running at all! That’s because it avoids the overhead of HTTP and deals directly with the Django framework. This helps make the unit tests run quickly.
  * When retrieving pages, remember to specify the _path_ of the URL, not the whole domain. For example, this is correct:
```
>>> c.get("/login/")

```

This is incorrect:
```
>>> c.get("https://www.example.com/login/")

```

The test client is not capable of retrieving web pages that are not powered by your Django project. If you need to retrieve other web pages, use a Python standard library module such as
  * To resolve URLs, the test client uses whatever URLconf is pointed-to by your [`ROOT_URLCONF`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-ROOT_URLCONF) setting.
  * Although the above example would work in the Python interactive interpreter, some of the test client’s functionality, notably the template-related functionality, is only available _while tests are running_.
The reason for this is that Django’s test runner performs a bit of black magic in order to determine which template was loaded by a given view. This black magic (essentially a patching of Django’s template system in memory) only happens during test running.
  * By default, the test client will disable any CSRF checks performed by your site.
If, for some reason, you _want_ the test client to perform CSRF checks, you can create an instance of the test client that enforces CSRF checks. To do this, pass in the `enforce_csrf_checks` argument when you construct your client:
```
>>> from django.test import Client
>>> csrf_client = Client(enforce_csrf_checks=True)

```



### Making requests[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#making-requests "Link to this heading")
Use the `django.test.Client` class to make requests.

_class_ Client(_enforce_csrf_checks =False_, _raise_request_exception =True_, _json_encoder =DjangoJSONEncoder_, _*_ , _headers =None_, _** defaults_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/client/#Client)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client "Link to this definition")

A testing HTTP client. Takes several arguments that can customize behavior.
`headers` allows you to specify default headers that will be sent with every request. For example, to set a `User-Agent` header:
```
client = Client(headers={"user-agent": "curl/7.79.1"})

```

Arbitrary keyword arguments in `**defaults` set WSGI
```
client = Client(SCRIPT_NAME="/app/")

```

Note
Keyword arguments starting with a `HTTP_` prefix are set as headers, but the `headers` parameter should be preferred for readability.
The values from the `headers` and `extra` keyword arguments passed to [`get()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get"), [`post()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.post "django.test.Client.post"), etc. have precedence over the defaults passed to the class constructor.
The `enforce_csrf_checks` argument can be used to test CSRF protection (see above).
The `raise_request_exception` argument allows controlling whether or not exceptions raised during the request should also be raised in the test. Defaults to `True`.
The `json_encoder` argument allows setting a custom JSON encoder for the JSON serialization that’s described in [`post()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.post "django.test.Client.post").
Once you have a `Client` instance, you can call any of the following methods:
Changed in Django 4.2:
The `headers` parameter was added.

get(_path_ , _data =None_, _follow =False_, _secure =False_, _*_ , _headers =None_, _** extra_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/client/#Client.get)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get "Link to this definition")

Makes a GET request on the provided `path` and returns a `Response` object, which is documented below.
The key-value pairs in the `data` dictionary are used to create a GET data payload. For example:
```
>>> c = Client()
>>> c.get("/customers/details/", {"name": "fred", "age": 7})

```

…will result in the evaluation of a GET request equivalent to:
```
/customers/details/?name=fred&age=7

```

The `headers` parameter can be used to specify headers to be sent in the request. For example:
```
>>> c = Client()
>>> c.get(
...     "/customers/details/",
...     {"name": "fred", "age": 7},
...     headers={"accept": "application/json"},
... )

```

…will send the HTTP header `HTTP_ACCEPT` to the details view, which is a good way to test code paths that use the [`django.http.HttpRequest.accepts()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.accepts "django.http.HttpRequest.accepts") method.
Arbitrary keyword arguments set WSGI
```
>>> c = Client()
>>> c.get("/", SCRIPT_NAME="/app/")

```

If you already have the GET arguments in URL-encoded form, you can use that encoding instead of using the data argument. For example, the previous GET request could also be posed as:
```
>>> c = Client()
>>> c.get("/customers/details/?name=fred&age=7")

```

If you provide a URL with both an encoded GET data and a data argument, the data argument will take precedence.
If you set `follow` to `True` the client will follow any redirects and a `redirect_chain` attribute will be set in the response object containing tuples of the intermediate urls and status codes.
If you had a URL `/redirect_me/` that redirected to `/next/`, that redirected to `/final/`, this is what you’d see:
```
>>> response = c.get("/redirect_me/", follow=True)
>>> response.redirect_chain
[('http://testserver/next/', 302), ('http://testserver/final/', 302)]

```

If you set `secure` to `True` the client will emulate an HTTPS request.
Changed in Django 4.2:
The `headers` parameter was added.

post(_path_ , _data =None_, _content_type =MULTIPART_CONTENT_, _follow =False_, _secure =False_, _*_ , _headers =None_, _** extra_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/client/#Client.post)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.post "Link to this definition")

Makes a POST request on the provided `path` and returns a `Response` object, which is documented below.
The key-value pairs in the `data` dictionary are used to submit POST data. For example:
```
>>> c = Client()
>>> c.post("/login/", {"name": "fred", "passwd": "secret"})

```

…will result in the evaluation of a POST request to this URL:
```
/login/

```

…with this POST data:
```
name=fred&passwd=secret

```

If you provide `content_type` as _application/json_ , the `data` is serialized using [`DjangoJSONEncoder`](https://docs.djangoproject.com/en/5.0/topics/serialization/#django.core.serializers.json.DjangoJSONEncoder "django.core.serializers.json.DjangoJSONEncoder") by default, and can be overridden by providing a `json_encoder` argument to [`Client`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client "django.test.Client"). This serialization also happens for [`put()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.put "django.test.Client.put"), [`patch()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.patch "django.test.Client.patch"), and [`delete()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.delete "django.test.Client.delete") requests.
If you provide any other `content_type` (e.g. _text/xml_ for an XML payload), the contents of `data` are sent as-is in the POST request, using `content_type` in the HTTP `Content-Type` header.
If you don’t provide a value for `content_type`, the values in `data` will be transmitted with a content type of _multipart/form-data_. In this case, the key-value pairs in `data` will be encoded as a multipart message and used to create the POST data payload.
To submit multiple values for a given key – for example, to specify the selections for a `<select multiple>` – provide the values as a list or tuple for the required key. For example, this value of `data` would submit three selected values for the field named `choices`:
```
{"choices": ["a", "b", "d"]}

```

Submitting files is a special case. To POST a file, you need only provide the file field name as a key, and a file handle to the file you wish to upload as a value. For example, if your form has fields `name` and `attachment`, the latter a [`FileField`](https://docs.djangoproject.com/en/5.0/ref/forms/fields/#django.forms.FileField "django.forms.FileField"):
```
>>> c = Client()
>>> with open("wishlist.doc", "rb") as fp:
...     c.post("/customers/wishes/", {"name": "fred", "attachment": fp})
...

```

You may also provide any file-like object (e.g., [`ImageField`](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ImageField "django.db.models.ImageField"), the object needs a `name` attribute that passes the [`validate_image_file_extension`](https://docs.djangoproject.com/en/5.0/ref/validators/#django.core.validators.validate_image_file_extension "django.core.validators.validate_image_file_extension") validator. For example:
```
>>> from io import BytesIO
>>> img = BytesIO(
...     b"GIF89a\x01\x00\x01\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00"
...     b"\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01\x00\x00"
... )
>>> img.name = "myimage.gif"

```

Note that if you wish to use the same file handle for multiple `post()` calls then you will need to manually reset the file pointer between posts. The easiest way to do this is to manually close the file after it has been provided to `post()`, as demonstrated above.
You should also ensure that the file is opened in a way that allows the data to be read. If your file contains binary data such as an image, this means you will need to open the file in `rb` (read binary) mode.
The `headers` and `extra` parameters acts the same as for [`Client.get()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").
If the URL you request with a POST contains encoded parameters, these parameters will be made available in the request.GET data. For example, if you were to make the request:
```
>>> c.post("/login/?visitor=true", {"name": "fred", "passwd": "secret"})

```

… the view handling this request could interrogate request.POST to retrieve the username and password, and could interrogate request.GET to determine if the user was a visitor.
If you set `follow` to `True` the client will follow any redirects and a `redirect_chain` attribute will be set in the response object containing tuples of the intermediate urls and status codes.
If you set `secure` to `True` the client will emulate an HTTPS request.
Changed in Django 4.2:
The `headers` parameter was added.

head(_path_ , _data =None_, _follow =False_, _secure =False_, _*_ , _headers =None_, _** extra_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/client/#Client.head)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.head "Link to this definition")

Makes a HEAD request on the provided `path` and returns a `Response` object. This method works just like [`Client.get()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get"), including the `follow`, `secure`, `headers`, and `extra` parameters, except it does not return a message body.
Changed in Django 4.2:
The `headers` parameter was added.

options(_path_ , _data =''_, _content_type ='application/octet-stream'_, _follow =False_, _secure =False_, _*_ , _headers =None_, _** extra_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/client/#Client.options)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.options "Link to this definition")

Makes an OPTIONS request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.
When `data` is provided, it is used as the request body, and a `Content-Type` header is set to `content_type`.
The `follow`, `secure`, `headers`, and `extra` parameters act the same as for [`Client.get()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").
Changed in Django 4.2:
The `headers` parameter was added.

put(_path_ , _data =''_, _content_type ='application/octet-stream'_, _follow =False_, _secure =False_, _*_ , _headers =None_, _** extra_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/client/#Client.put)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.put "Link to this definition")

Makes a PUT request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.
When `data` is provided, it is used as the request body, and a `Content-Type` header is set to `content_type`.
The `follow`, `secure`, `headers`, and `extra` parameters act the same as for [`Client.get()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").
Changed in Django 4.2:
The `headers` parameter was added.

patch(_path_ , _data =''_, _content_type ='application/octet-stream'_, _follow =False_, _secure =False_, _*_ , _headers =None_, _** extra_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/client/#Client.patch)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.patch "Link to this definition")

Makes a PATCH request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.
The `follow`, `secure`, `headers`, and `extra` parameters act the same as for [`Client.get()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").
Changed in Django 4.2:
The `headers` parameter was added.

delete(_path_ , _data =''_, _content_type ='application/octet-stream'_, _follow =False_, _secure =False_, _*_ , _headers =None_, _** extra_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/client/#Client.delete)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.delete "Link to this definition")

Makes a DELETE request on the provided `path` and returns a `Response` object. Useful for testing RESTful interfaces.
When `data` is provided, it is used as the request body, and a `Content-Type` header is set to `content_type`.
The `follow`, `secure`, `headers`, and `extra` parameters act the same as for [`Client.get()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").
Changed in Django 4.2:
The `headers` parameter was added.

trace(_path_ , _follow =False_, _secure =False_, _*_ , _headers =None_, _** extra_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/client/#Client.trace)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.trace "Link to this definition")

Makes a TRACE request on the provided `path` and returns a `Response` object. Useful for simulating diagnostic probes.
Unlike the other request methods, `data` is not provided as a keyword parameter in order to comply with
The `follow`, `secure`, `headers`, and `extra` parameters act the same as for [`Client.get()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get").
Changed in Django 4.2:
The `headers` parameter was added.

login(_** credentials_)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.login "Link to this definition")


alogin(_** credentials_)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.alogin "Link to this definition")

_Asynchronous version_ : `alogin()`
If your site uses Django’s [authentication system](https://docs.djangoproject.com/en/5.0/topics/auth/) and you deal with logging in users, you can use the test client’s `login()` method to simulate the effect of a user logging into the site.
After you call this method, the test client will have all the cookies and session data required to pass any login-based tests that may form part of a view.
The format of the `credentials` argument depends on which [authentication backend](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#authentication-backends) you’re using (which is configured by your [`AUTHENTICATION_BACKENDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-AUTHENTICATION_BACKENDS) setting). If you’re using the standard authentication backend provided by Django (`ModelBackend`), `credentials` should be the user’s username and password, provided as keyword arguments:
```
>>> c = Client()
>>> c.login(username="fred", password="secret")

# Now you can access a view that's only available to logged-in users.

```

If you’re using a different authentication backend, this method may require different credentials. It requires whichever credentials are required by your backend’s `authenticate()` method.
`login()` returns `True` if it the credentials were accepted and login was successful.
Finally, you’ll need to remember to create user accounts before you can use this method. As we explained above, the test runner is executed using a test database, which contains no users by default. As a result, user accounts that are valid on your production site will not work under test conditions. You’ll need to create users as part of the test suite – either manually (using the Django model API) or with a test fixture. Remember that if you want your test user to have a password, you can’t set the user’s password by setting the password attribute directly – you must use the [`set_password()`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User.set_password "django.contrib.auth.models.User.set_password") function to store a correctly hashed password. Alternatively, you can use the [`create_user()`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user "django.contrib.auth.models.UserManager.create_user") helper method to create a new user with a correctly hashed password.
Changed in Django 5.0:
`alogin()` method was added.

force_login(_user_ , _backend =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.force_login "Link to this definition")


aforce_login(_user_ , _backend =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.aforce_login "Link to this definition")

_Asynchronous version_ : `aforce_login()`
If your site uses Django’s [authentication system](https://docs.djangoproject.com/en/5.0/topics/auth/), you can use the `force_login()` method to simulate the effect of a user logging into the site. Use this method instead of [`login()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.login "django.test.Client.login") when a test requires a user be logged in and the details of how a user logged in aren’t important.
Unlike `login()`, this method skips the authentication and verification steps: inactive users ([`is_active=False`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User.is_active "django.contrib.auth.models.User.is_active")) are permitted to login and the user’s credentials don’t need to be provided.
The user will have its `backend` attribute set to the value of the `backend` argument (which should be a dotted Python path string), or to `settings.AUTHENTICATION_BACKENDS[0]` if a value isn’t provided. The [`authenticate()`](https://docs.djangoproject.com/en/5.0/topics/auth/default/#django.contrib.auth.authenticate "django.contrib.auth.authenticate") function called by [`login()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.login "django.test.Client.login") normally annotates the user like this.
This method is faster than `login()` since the expensive password hashing algorithms are bypassed. Also, you can speed up `login()` by [using a weaker hasher while testing](https://docs.djangoproject.com/en/5.0/topics/testing/overview/#speeding-up-tests-auth-hashers).
Changed in Django 5.0:
`aforce_login()` method was added.

logout()[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.logout "Link to this definition")


alogout()[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.alogout "Link to this definition")

_Asynchronous version_ : `alogout()`
If your site uses Django’s [authentication system](https://docs.djangoproject.com/en/5.0/topics/auth/), the `logout()` method can be used to simulate the effect of a user logging out of your site.
After you call this method, the test client will have all the cookies and session data cleared to defaults. Subsequent requests will appear to come from an [`AnonymousUser`](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.AnonymousUser "django.contrib.auth.models.AnonymousUser").
Changed in Django 5.0:
`alogout()` method was added.
### Testing responses[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#testing-responses "Link to this heading")
The `get()` and `post()` methods both return a `Response` object. This `Response` object is _not_ the same as the `HttpResponse` object returned by Django views; the test response object has some additional data useful for test code to verify.
Specifically, a `Response` object has the following attributes:

_class_ Response[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response "Link to this definition")


client[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.client "Link to this definition")

The test client that was used to make the request that resulted in the response.

content[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.content "Link to this definition")

The body of the response, as a bytestring. This is the final page content as rendered by the view, or any error message.

context[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.context "Link to this definition")

The template `Context` instance that was used to render the template that produced the response content.
If the rendered page used multiple templates, then `context` will be a list of `Context` objects, in the order in which they were rendered.
Regardless of the number of templates used during rendering, you can retrieve context values using the `[]` operator. For example, the context variable `name` could be retrieved using:
```
>>> response = client.get("/foo/")
>>> response.context["name"]
'Arthur'

```

Not using Django templates?
This attribute is only populated when using the [`DjangoTemplates`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") backend. If you’re using another template engine, [`context_data`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.context_data "django.template.response.SimpleTemplateResponse.context_data") may be a suitable alternative on responses with that attribute.

exc_info[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.exc_info "Link to this definition")

A tuple of three values that provides information about the unhandled exception, if any, that occurred during the view.
The values are (type, value, traceback), the same as returned by Python’s
  * _type_ : The type of the exception.
  * _value_ : The exception instance.
  * _traceback_ : A traceback object which encapsulates the call stack at the point where the exception originally occurred.


If no exception occurred, then `exc_info` will be `None`.

json(_** kwargs_)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.json "Link to this definition")

The body of the response, parsed as JSON. Extra keyword arguments are passed to
```
>>> response = client.get("/foo/")
>>> response.json()["name"]
'Arthur'

```

If the `Content-Type` header is not `"application/json"`, then a

request[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.request "Link to this definition")

The request data that stimulated the response.

wsgi_request[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.wsgi_request "Link to this definition")

The `WSGIRequest` instance generated by the test handler that generated the response.

status_code[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.status_code "Link to this definition")

The HTTP status of the response, as an integer. For a full list of defined codes, see the

templates[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.templates "Link to this definition")

A list of `Template` instances used to render the final content, in the order they were rendered. For each template in the list, use `template.name` to get the template’s file name, if the template was loaded from a file. (The name is a string such as `'admin/index.html'`.)
Not using Django templates?
This attribute is only populated when using the [`DjangoTemplates`](https://docs.djangoproject.com/en/5.0/topics/templates/#django.template.backends.django.DjangoTemplates "django.template.backends.django.DjangoTemplates") backend. If you’re using another template engine, [`template_name`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.SimpleTemplateResponse.template_name "django.template.response.SimpleTemplateResponse.template_name") may be a suitable alternative if you only need the name of the template used for rendering.

resolver_match[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.resolver_match "Link to this definition")

An instance of [`ResolverMatch`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch "django.urls.ResolverMatch") for the response. You can use the [`func`](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/#django.urls.ResolverMatch.func "django.urls.ResolverMatch.func") attribute, for example, to verify the view that served the response:
```
# my_view here is a function based view.
self.assertEqual(response.resolver_match.func, my_view)

# Class-based views need to compare the view_class, as the
# functions generated by as_view() won't be equal.
self.assertIs(response.resolver_match.func.view_class, MyView)

```

If the given URL is not found, accessing this attribute will raise a [`Resolver404`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.urls.Resolver404 "django.urls.Resolver404") exception.
As with a normal response, you can also access the headers through [`HttpResponse.headers`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.headers "django.http.HttpResponse.headers"). For example, you could determine the content type of a response using `response.headers['Content-Type']`.
### Exceptions[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#exceptions "Link to this heading")
If you point the test client at a view that raises an exception and `Client.raise_request_exception` is `True`, that exception will be visible in the test case. You can then use a standard `try ... except` block or
The only exceptions that are not visible to the test client are [`Http404`](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404 "django.http.Http404"), [`PermissionDenied`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.PermissionDenied "django.core.exceptions.PermissionDenied"), [`SuspiciousOperation`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.SuspiciousOperation "django.core.exceptions.SuspiciousOperation"). Django catches these exceptions internally and converts them into the appropriate HTTP response codes. In these cases, you can check `response.status_code` in your test.
If `Client.raise_request_exception` is `False`, the test client will return a 500 response as would be returned to a browser. The response has the attribute [`exc_info`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Response.exc_info "django.test.Response.exc_info") to provide information about the unhandled exception.
### Persistent state[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#persistent-state "Link to this heading")
The test client is stateful. If a response returns a cookie, then that cookie will be stored in the test client and sent with all subsequent `get()` and `post()` requests.
Expiration policies for these cookies are not followed. If you want a cookie to expire, either delete it manually or create a new `Client` instance (which will effectively delete all cookies).
A test client has attributes that store persistent state information. You can access these properties as part of a test condition.

Client.cookies[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.cookies "Link to this definition")

A Python

Client.session[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.session "Link to this definition")

A dictionary-like object containing session information. See the [session documentation](https://docs.djangoproject.com/en/5.0/topics/http/sessions/) for full details.
To modify the session and then save it, it must be stored in a variable first (because a new `SessionStore` is created every time this property is accessed):
```
def test_something(self):
    session = self.client.session
    session["somekey"] = "test"
    session.save()

```


Client.asession()[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.asession "Link to this definition")

New in Django 5.0.
This is similar to the [`session`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.session "django.test.Client.session") attribute but it works in async contexts.
### Setting the language[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#setting-the-language "Link to this heading")
When testing applications that support internationalization and localization, you might want to set the language for a test client request. The method for doing so depends on whether or not the [`LocaleMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.locale.LocaleMiddleware "django.middleware.locale.LocaleMiddleware") is enabled.
If the middleware is enabled, the language can be set by creating a cookie with a name of [`LANGUAGE_COOKIE_NAME`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-LANGUAGE_COOKIE_NAME) and a value of the language code:
```
from django.conf import settings


def test_language_using_cookie(self):
    self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: "fr"})
    response = self.client.get("/")
    self.assertEqual(response.content, b"Bienvenue sur mon site.")

```

or by including the `Accept-Language` HTTP header in the request:
```
def test_language_using_header(self):
    response = self.client.get("/", headers={"accept-language": "fr"})
    self.assertEqual(response.content, b"Bienvenue sur mon site.")

```

Note
When using these methods, ensure to reset the active language at the end of each test:
```
def tearDown(self):
    translation.activate(settings.LANGUAGE_CODE)

```

More details are in [How Django discovers language preference](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#how-django-discovers-language-preference).
If the middleware isn’t enabled, the active language may be set using [`translation.override()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.translation.override "django.utils.translation.override"):
```
from django.utils import translation


def test_language_using_override(self):
    with translation.override("fr"):
        response = self.client.get("/")
    self.assertEqual(response.content, b"Bienvenue sur mon site.")

```

More details are in [Explicitly setting the active language](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#explicitly-setting-the-active-language).
### Example[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#example "Link to this heading")
The following is a unit test using the test client:
```
import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get("/customer/details/")

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context["customers"]), 5)

```

See also
[`django.test.RequestFactory`](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#django.test.RequestFactory "django.test.RequestFactory")
