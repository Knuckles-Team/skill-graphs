This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!
[Skip to main content](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#main-content)
[Django](https://www.djangoproject.com/)
The web framework for perfectionists with deadlines.
Menu Main navigation
  * [Overview](https://www.djangoproject.com/start/overview/)
  * [Download](https://www.djangoproject.com/download/)
  * [Documentation](https://docs.djangoproject.com/)
  * [News](https://www.djangoproject.com/weblog/)
  * [Issues](https://code.djangoproject.com/)
  * [Community](https://www.djangoproject.com/community/)
  * [Foundation](https://www.djangoproject.com/foundation/)
  * [♥ Donate](https://www.djangoproject.com/fundraising/)


Search Submit
Toggle theme (current theme: auto)
Toggle theme (current theme: light)
Toggle theme (current theme: dark)
Toggle Light / Dark / Auto color theme
[Documentation](https://docs.djangoproject.com/en/5.0/)
  * [ Getting Help ](https://docs.djangoproject.com/en/5.0/faq/help/)


  * Language: **en**
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.0/topics/http/middleware/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.0/topics/http/middleware/)
  * [pl](https://docs.djangoproject.com/pl/5.0/topics/http/middleware/)
  * [ko](https://docs.djangoproject.com/ko/5.0/topics/http/middleware/)
  * [ja](https://docs.djangoproject.com/ja/5.0/topics/http/middleware/)
  * [it](https://docs.djangoproject.com/it/5.0/topics/http/middleware/)
  * [id](https://docs.djangoproject.com/id/5.0/topics/http/middleware/)
  * [fr](https://docs.djangoproject.com/fr/5.0/topics/http/middleware/)
  * [es](https://docs.djangoproject.com/es/5.0/topics/http/middleware/)
  * [el](https://docs.djangoproject.com/el/5.0/topics/http/middleware/)


  * Documentation version: **5.0**
  * [dev](https://docs.djangoproject.com/en/dev/topics/http/middleware/)
  * [6.0](https://docs.djangoproject.com/en/6.0/topics/http/middleware/)
  * [5.2](https://docs.djangoproject.com/en/5.2/topics/http/middleware/)
  * [5.1](https://docs.djangoproject.com/en/5.1/topics/http/middleware/)
  * [4.2](https://docs.djangoproject.com/en/4.2/topics/http/middleware/)
  * [4.1](https://docs.djangoproject.com/en/4.1/topics/http/middleware/)
  * [4.0](https://docs.djangoproject.com/en/4.0/topics/http/middleware/)
  * [3.2](https://docs.djangoproject.com/en/3.2/topics/http/middleware/)
  * [3.1](https://docs.djangoproject.com/en/3.1/topics/http/middleware/)
  * [3.0](https://docs.djangoproject.com/en/3.0/topics/http/middleware/)
  * [2.2](https://docs.djangoproject.com/en/2.2/topics/http/middleware/)
  * [2.1](https://docs.djangoproject.com/en/2.1/topics/http/middleware/)
  * [2.0](https://docs.djangoproject.com/en/2.0/topics/http/middleware/)
  * [1.11](https://docs.djangoproject.com/en/1.11/topics/http/middleware/)
  * [1.10](https://docs.djangoproject.com/en/1.10/topics/http/middleware/)
  * [1.8](https://docs.djangoproject.com/en/1.8/topics/http/middleware/)


  * [](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#top)


# Middleware[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#middleware "Link to this heading")
Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level “plugin” system for globally altering Django’s input or output.
Each middleware component is responsible for doing some specific function. For example, Django includes a middleware component, [`AuthenticationMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware "django.contrib.auth.middleware.AuthenticationMiddleware"), that associates users with requests using sessions.
This document explains how middleware works, how you activate middleware, and how to write your own middleware. Django ships with some built-in middleware you can use right out of the box. They’re documented in the [built-in middleware reference](https://docs.djangoproject.com/en/5.0/ref/middleware/).
## Writing your own middleware[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#writing-your-own-middleware "Link to this heading")
A middleware factory is a callable that takes a `get_response` callable and returns a middleware. A middleware is a callable that takes a request and returns a response, just like a view.
A middleware can be written as a function that looks like this:
```
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

```

Or it can be written as a class whose instances are callable, like this:
```
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

```

The `get_response` callable provided by Django might be the actual view (if this is the last listed middleware) or it might be the next middleware in the chain. The current middleware doesn’t need to know or care what exactly it is, just that it represents whatever comes next.
The above is a slight simplification – the `get_response` callable for the last middleware in the chain won’t be the actual view but rather a wrapper method from the handler which takes care of applying [view middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#view-middleware), calling the view with appropriate URL arguments, and applying [template-response](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#template-response-middleware) and [exception](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#exception-middleware) middleware.
Middleware can either support only synchronous Python (the default), only asynchronous Python, or both. See [Asynchronous support](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#async-middleware) for details of how to advertise what you support, and know what kind of request you are getting.
Middleware can live anywhere on your Python path.
###  `__init__(get_response)`[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#init-get-response "Link to this heading")
Middleware factories must accept a `get_response` argument. You can also initialize some global state for the middleware. Keep in mind a couple of caveats:
  * Django initializes your middleware with only the `get_response` argument, so you can’t define `__init__()` as requiring any other arguments.
  * Unlike the `__call__()` method which is called once per request, `__init__()` is called only _once_ , when the web server starts.


### Marking middleware as unused[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#marking-middleware-as-unused "Link to this heading")
It’s sometimes useful to determine at startup time whether a piece of middleware should be used. In these cases, your middleware’s `__init__()` method may raise [`MiddlewareNotUsed`](https://docs.djangoproject.com/en/5.0/ref/exceptions/#django.core.exceptions.MiddlewareNotUsed "django.core.exceptions.MiddlewareNotUsed"). Django will then remove that middleware from the middleware process and log a debug message to the [django.request](https://docs.djangoproject.com/en/5.0/ref/logging/#django-request-logger) logger when [`DEBUG`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG) is `True`.
## Activating middleware[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#activating-middleware "Link to this heading")
To activate a middleware component, add it to the [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) list in your Django settings.
In [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE), each middleware component is represented by a string: the full Python path to the middleware factory’s class or function name. For example, here’s the default value created by [`django-admin startproject`](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-startproject):
```
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

```

A Django installation doesn’t require any middleware — [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) can be empty, if you’d like — but it’s strongly suggested that you at least use [`CommonMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.common.CommonMiddleware "django.middleware.common.CommonMiddleware").
The order in [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) matters because a middleware can depend on other middleware. For instance, [`AuthenticationMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware "django.contrib.auth.middleware.AuthenticationMiddleware") stores the authenticated user in the session; therefore, it must run after [`SessionMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware "django.contrib.sessions.middleware.SessionMiddleware"). See [Middleware ordering](https://docs.djangoproject.com/en/5.0/ref/middleware/#middleware-ordering) for some common hints about ordering of Django middleware classes.
## Middleware order and layering[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#middleware-order-and-layering "Link to this heading")
During the request phase, before calling the view, Django applies middleware in the order it’s defined in [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE), top-down.
You can think of it like an onion: each middleware class is a “layer” that wraps the view, which is in the core of the onion. If the request passes through all the layers of the onion (each one calls `get_response` to pass the request in to the next layer), all the way to the view at the core, the response will then pass through every layer (in reverse order) on the way back out.
If one of the layers decides to short-circuit and return a response without ever calling its `get_response`, none of the layers of the onion inside that layer (including the view) will see the request or the response. The response will only return through the same layers that the request passed in through.
## Other middleware hooks[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#other-middleware-hooks "Link to this heading")
Besides the basic request/response middleware pattern described earlier, you can add three other special methods to class-based middleware:
###  `process_view()`[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#process-view "Link to this heading")

process_view(_request_ , _view_func_ , _view_args_ , _view_kwargs_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#process_view "Link to this definition")

`request` is an [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") object. `view_func` is the Python function that Django is about to use. (It’s the actual function object, not the name of the function as a string.) `view_args` is a list of positional arguments that will be passed to the view, and `view_kwargs` is a dictionary of keyword arguments that will be passed to the view. Neither `view_args` nor `view_kwargs` include the first view argument (`request`).
`process_view()` is called just before Django calls the view.
It should return either `None` or an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") object. If it returns `None`, Django will continue processing this request, executing any other `process_view()` middleware and, then, the appropriate view. If it returns an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") object, Django won’t bother calling the appropriate view; it’ll apply response middleware to that [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") and return the result.
Note
Accessing [`request.POST`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.POST "django.http.HttpRequest.POST") inside middleware before the view runs or in `process_view()` will prevent any view running after the middleware from being able to [modify the upload handlers for the request](https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/#modifying-upload-handlers-on-the-fly), and should normally be avoided.
The [`CsrfViewMiddleware`](https://docs.djangoproject.com/en/5.0/ref/middleware/#django.middleware.csrf.CsrfViewMiddleware "django.middleware.csrf.CsrfViewMiddleware") class can be considered an exception, as it provides the [`csrf_exempt()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_exempt "django.views.decorators.csrf.csrf_exempt") and [`csrf_protect()`](https://docs.djangoproject.com/en/5.0/ref/csrf/#django.views.decorators.csrf.csrf_protect "django.views.decorators.csrf.csrf_protect") decorators which allow views to explicitly control at what point the CSRF validation should occur.
###  `process_exception()`[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#process-exception "Link to this heading")

process_exception(_request_ , _exception_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#process_exception "Link to this definition")

`request` is an [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") object. `exception` is an `Exception` object raised by the view function.
Django calls `process_exception()` when a view raises an exception. `process_exception()` should return either `None` or an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") object. If it returns an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") object, the template response and response middleware will be applied and the resulting response returned to the browser. Otherwise, [default exception handling](https://docs.djangoproject.com/en/5.0/ref/views/#error-views) kicks in.
Again, middleware are run in reverse order during the response phase, which includes `process_exception`. If an exception middleware returns a response, the `process_exception` methods of the middleware classes above that middleware won’t be called at all.
###  `process_template_response()`[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#process-template-response "Link to this heading")

process_template_response(_request_ , _response_)[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#process_template_response "Link to this definition")

`request` is an [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") object. `response` is the [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") object (or equivalent) returned by a Django view or by a middleware.
`process_template_response()` is called just after the view has finished executing, if the response instance has a `render()` method, indicating that it is a [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") or equivalent.
It must return a response object that implements a `render` method. It could alter the given `response` by changing `response.template_name` and `response.context_data`, or it could create and return a brand-new [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse") or equivalent.
You don’t need to explicitly render responses – responses will be automatically rendered once all template response middleware has been called.
Middleware are run in reverse order during the response phase, which includes `process_template_response()`.
## Dealing with streaming responses[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#dealing-with-streaming-responses "Link to this heading")
Unlike [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse"), [`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") does not have a `content` attribute. As a result, middleware can no longer assume that all responses will have a `content` attribute. If they need access to the content, they must test for streaming responses and adjust their behavior accordingly:
```
if response.streaming:
    response.streaming_content = wrap_streaming_content(response.streaming_content)
else:
    response.content = alter_content(response.content)

```

Note
`streaming_content` should be assumed to be too large to hold in memory. Response middleware may wrap it in a new generator, but must not consume it. Wrapping is typically implemented as follows:
```
def wrap_streaming_content(content):
    for chunk in content:
        yield alter_content(chunk)

```

[`StreamingHttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse "django.http.StreamingHttpResponse") allows both synchronous and asynchronous iterators. The wrapping function must match. Check [`StreamingHttpResponse.is_async`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.StreamingHttpResponse.is_async "django.http.StreamingHttpResponse.is_async") if your middleware needs to support both types of iterator.
Changed in Django 4.2:
Support for streaming responses with asynchronous iterators was added.
## Exception handling[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#exception-handling "Link to this heading")
Django automatically converts exceptions raised by the view or by middleware into an appropriate HTTP response with an error status code. [Certain exceptions](https://docs.djangoproject.com/en/5.0/ref/views/#error-views) are converted to 4xx status codes, while an unknown exception is converted to a 500 status code.
This conversion takes place before and after each middleware (you can think of it as the thin film in between each layer of the onion), so that every middleware can always rely on getting some kind of HTTP response back from calling its `get_response` callable. Middleware don’t need to worry about wrapping their call to `get_response` in a `try/except` and handling an exception that might have been raised by a later middleware or the view. Even if the very next middleware in the chain raises an [`Http404`](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404 "django.http.Http404") exception, for example, your middleware won’t see that exception; instead it will get an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") object with a [`status_code`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse.status_code "django.http.HttpResponse.status_code") of 404.
You can set [`DEBUG_PROPAGATE_EXCEPTIONS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEBUG_PROPAGATE_EXCEPTIONS) to `True` to skip this conversion and propagate exceptions upward.
## Asynchronous support[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#asynchronous-support "Link to this heading")
Middleware can support any combination of synchronous and asynchronous requests. Django will adapt requests to fit the middleware’s requirements if it cannot support both, but at a performance penalty.
By default, Django assumes that your middleware is capable of handling only synchronous requests. To change these assumptions, set the following attributes on your middleware factory function or class:
  * `sync_capable` is a boolean indicating if the middleware can handle synchronous requests. Defaults to `True`.
  * `async_capable` is a boolean indicating if the middleware can handle asynchronous requests. Defaults to `False`.


If your middleware has both `sync_capable = True` and `async_capable = True`, then Django will pass it the request without converting it. In this case, you can work out if your middleware will receive async requests by checking if the `get_response` object you are passed is a coroutine function, using `asgiref.sync.iscoroutinefunction`.
The `django.utils.decorators` module contains [`sync_only_middleware()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.decorators.sync_only_middleware "django.utils.decorators.sync_only_middleware"), [`async_only_middleware()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.decorators.async_only_middleware "django.utils.decorators.async_only_middleware"), and [`sync_and_async_middleware()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.decorators.sync_and_async_middleware "django.utils.decorators.sync_and_async_middleware") decorators that allow you to apply these flags to middleware factory functions.
The returned callable must match the sync or async nature of the `get_response` method. If you have an asynchronous `get_response`, you must return a coroutine function (`async def`).
`process_view`, `process_template_response` and `process_exception` methods, if they are provided, should also be adapted to match the sync/async mode. However, Django will individually adapt them as required if you do not, at an additional performance penalty.
Here’s an example of how to create a middleware function that supports both:
```
from asgiref.sync import iscoroutinefunction
from django.utils.decorators import sync_and_async_middleware


@sync_and_async_middleware
def simple_middleware(get_response):
    # One-time configuration and initialization goes here.
    if iscoroutinefunction(get_response):

        async def middleware(request):
            # Do something here!
            response = await get_response(request)
            return response

    else:

        def middleware(request):
            # Do something here!
            response = get_response(request)
            return response

    return middleware

```

Note
If you declare a hybrid middleware that supports both synchronous and asynchronous calls, the kind of call you get may not match the underlying view. Django will optimize the middleware call stack to have as few sync/async transitions as possible.
Thus, even if you are wrapping an async view, you may be called in sync mode if there is other, synchronous middleware between you and the view.
When using an asynchronous class-based middleware, you must ensure that instances are correctly marked as coroutine functions:
```
from asgiref.sync import iscoroutinefunction, markcoroutinefunction


class AsyncMiddleware:
    async_capable = True
    sync_capable = False

    def __init__(self, get_response):
        self.get_response = get_response
        if iscoroutinefunction(self.get_response):
            markcoroutinefunction(self)

    async def __call__(self, request):
        response = await self.get_response(request)
        # Some logic ...
        return response

```

## Upgrading pre-Django 1.10-style middleware[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#upgrading-pre-django-1-10-style-middleware "Link to this heading")

_class_ django.utils.deprecation.MiddlewareMixin[¶](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#django.utils.deprecation.MiddlewareMixin "Link to this definition")

Django provides `django.utils.deprecation.MiddlewareMixin` to ease creating middleware classes that are compatible with both [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) and the old `MIDDLEWARE_CLASSES`, and support synchronous and asynchronous requests. All middleware classes included with Django are compatible with both settings.
The mixin provides an `__init__()` method that requires a `get_response` argument and stores it in `self.get_response`.
The `__call__()` method:
  1. Calls `self.process_request(request)` (if defined).
  2. Calls `self.get_response(request)` to get the response from later middleware and the view.
  3. Calls `self.process_response(request, response)` (if defined).
  4. Returns the response.


If used with `MIDDLEWARE_CLASSES`, the `__call__()` method will never be used; Django calls `process_request()` and `process_response()` directly.
In most cases, inheriting from this mixin will be sufficient to make an old-style middleware compatible with the new system with sufficient backwards-compatibility. The new short-circuiting semantics will be harmless or even beneficial to the existing middleware. In a few cases, a middleware class may need some changes to adjust to the new semantics.
These are the behavioral differences between using [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) and `MIDDLEWARE_CLASSES`:
  1. Under `MIDDLEWARE_CLASSES`, every middleware will always have its `process_response` method called, even if an earlier middleware short-circuited by returning a response from its `process_request` method. Under [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE), middleware behaves more like an onion: the layers that a response goes through on the way out are the same layers that saw the request on the way in. If a middleware short-circuits, only that middleware and the ones before it in [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) will see the response.
  2. Under `MIDDLEWARE_CLASSES`, `process_exception` is applied to exceptions raised from a middleware `process_request` method. Under [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE), `process_exception` applies only to exceptions raised from the view (or from the `render` method of a [`TemplateResponse`](https://docs.djangoproject.com/en/5.0/ref/template-response/#django.template.response.TemplateResponse "django.template.response.TemplateResponse")). Exceptions raised from a middleware are converted to the appropriate HTTP response and then passed to the next middleware.
  3. Under `MIDDLEWARE_CLASSES`, if a `process_response` method raises an exception, the `process_response` methods of all earlier middleware are skipped and a `500 Internal Server Error` HTTP response is always returned (even if the exception raised was e.g. an [`Http404`](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404 "django.http.Http404")). Under [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE), an exception raised from a middleware will immediately be converted to the appropriate HTTP response, and then the next middleware in line will see that response. Middleware are never skipped due to a middleware raising an exception.

Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/http/generic-views/)
[How to use sessions ](https://docs.djangoproject.com/en/5.0/topics/http/sessions/)
[](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#top)
## Additional Information
### Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * [ Hristo Trendafilov donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)


### Contents
  * [Middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/)
    * [Writing your own middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#writing-your-own-middleware)
      * [`__init__(get_response)`](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#init-get-response)
      * [Marking middleware as unused](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#marking-middleware-as-unused)
    * [Activating middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#activating-middleware)
    * [Middleware order and layering](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#middleware-order-and-layering)
    * [Other middleware hooks](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#other-middleware-hooks)
      * [`process_view()`](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#process-view)
      * [`process_exception()`](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#process-exception)
      * [`process_template_response()`](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#process-template-response)
    * [Dealing with streaming responses](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#dealing-with-streaming-responses)
    * [Exception handling](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#exception-handling)
    * [Asynchronous support](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#asynchronous-support)
    * [Upgrading pre-Django 1.10-style middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#upgrading-pre-django-1-10-style-middleware)


### Browse
  * Prev: [Generic views](https://docs.djangoproject.com/en/5.0/topics/http/generic-views/)
  * Next: [How to use sessions](https://docs.djangoproject.com/en/5.0/topics/http/sessions/)
  * [Table of contents](https://docs.djangoproject.com/en/5.0/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.0/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.0/py-modindex/)


### You are here:
  * [Django 5.0 documentation](https://docs.djangoproject.com/en/5.0/)
    * [Using Django](https://docs.djangoproject.com/en/5.0/topics/)
      * [Handling HTTP requests](https://docs.djangoproject.com/en/5.0/topics/http/)
        * Middleware


### Getting help

[FAQ](https://docs.djangoproject.com/en/5.0/faq/)
    Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
    Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
    Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
    Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
    Report bugs with Django or Django documentation in our ticket tracker.
### Download:
Offline (Django 5.0): [HTML](https://media.djangoproject.com/docs/django-docs-5.0-en.zip) |
Provided by
### Diamond and Platinum Members
  * **JetBrains**


  * **Sentry**


  * **Kraken Tech**


## Django Links
### Learn More
  * [About Django](https://www.djangoproject.com/start/overview/)
  * [Getting Started with Django](https://www.djangoproject.com/start/)
  * [Team Organization](https://www.djangoproject.com/foundation/teams/)
  * [Django Software Foundation](https://www.djangoproject.com/foundation/)
  * [Code of Conduct](https://www.djangoproject.com/conduct/)
  * [Diversity Statement](https://www.djangoproject.com/diversity/)


### Get Involved
  * [Join a Group](https://www.djangoproject.com/community/)
  * [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
  * [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
  * [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
  * [Individual membership](https://www.djangoproject.com/foundation/individual-members/)


### Get Help
  * [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
  * [Django Discord](https://chat.djangoproject.com)
  * [Official Django Forum](https://forum.djangoproject.com/)


### Follow Us
  * [News RSS](https://www.djangoproject.com/rss/weblog/)


### Support Us
  * [Sponsor Django](https://www.djangoproject.com/fundraising/)
  * [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
  * [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)


[Django](https://www.djangoproject.com/)
  * Hosting by [In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
  * Design by &


© 2005-2026 [ Django Software Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a [registered trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.
