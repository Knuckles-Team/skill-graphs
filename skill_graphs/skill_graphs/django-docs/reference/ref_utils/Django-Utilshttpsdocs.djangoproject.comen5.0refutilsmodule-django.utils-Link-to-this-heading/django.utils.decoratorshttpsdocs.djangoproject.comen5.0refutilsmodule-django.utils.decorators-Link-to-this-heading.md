##  `django.utils.decorators`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.decorators "Link to this heading")

method_decorator(_decorator_ , _name =''_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/decorators/#method_decorator)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.decorators.method_decorator "Link to this definition")

Converts a function decorator into a method decorator. It can be used to decorate methods or classes; in the latter case, `name` is the name of the method to be decorated and is required.
`decorator` may also be a list or tuple of functions. They are wrapped in reverse order so that the call order is the order in which the functions appear in the list/tuple.
See [decorating class based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/#id1) for example usage.

decorator_from_middleware(_middleware_class_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/decorators/#decorator_from_middleware)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.decorators.decorator_from_middleware "Link to this definition")

Given a middleware class, returns a view decorator. This lets you use middleware functionality on a per-view basis. The middleware is created with no params passed.
It assumes middleware that’s compatible with the old style of Django 1.9 and earlier (having methods like `process_request()`, `process_exception()`, and `process_response()`).

decorator_from_middleware_with_args(_middleware_class_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/decorators/#decorator_from_middleware_with_args)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.decorators.decorator_from_middleware_with_args "Link to this definition")

Like `decorator_from_middleware`, but returns a function that accepts the arguments to be passed to the middleware_class. For example, the [`cache_page()`](https://docs.djangoproject.com/en/5.0/topics/cache/#django.views.decorators.cache.cache_page "django.views.decorators.cache.cache_page") decorator is created from the `CacheMiddleware` like this:
```
cache_page = decorator_from_middleware_with_args(CacheMiddleware)


@cache_page(3600)
def my_view(request):
    pass

```


sync_only_middleware(_middleware_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/decorators/#sync_only_middleware)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.decorators.sync_only_middleware "Link to this definition")

Marks a middleware as [synchronous-only](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#async-middleware). (The default in Django, but this allows you to future-proof if the default ever changes in a future release.)

async_only_middleware(_middleware_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/decorators/#async_only_middleware)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.decorators.async_only_middleware "Link to this definition")

Marks a middleware as [asynchronous-only](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#async-middleware). Django will wrap it in an asynchronous event loop when it is called from the WSGI request path.

sync_and_async_middleware(_middleware_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/decorators/#sync_and_async_middleware)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.decorators.sync_and_async_middleware "Link to this definition")

Marks a middleware as [sync and async compatible](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#async-middleware), this allows to avoid converting requests. You must implement detection of the current request type to use this decorator. See [asynchronous middleware documentation](https://docs.djangoproject.com/en/5.0/topics/http/middleware/#async-middleware) for details.
