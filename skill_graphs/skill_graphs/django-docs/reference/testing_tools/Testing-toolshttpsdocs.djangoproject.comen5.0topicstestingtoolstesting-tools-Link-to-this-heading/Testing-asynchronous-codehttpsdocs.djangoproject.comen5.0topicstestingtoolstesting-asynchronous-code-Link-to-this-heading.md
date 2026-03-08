## Testing asynchronous code[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#testing-asynchronous-code "Link to this heading")
If you merely want to test the output of your asynchronous views, the standard test client will run them inside their own asynchronous loop without any extra work needed on your part.
However, if you want to write fully-asynchronous tests for a Django project, you will need to take several things into account.
Firstly, your tests must be `async def` methods on the test class (in order to give them an asynchronous context). Django will automatically detect any `async def` tests and wrap them so they run in their own event loop.
If you are testing from an asynchronous function, you must also use the asynchronous test client. This is available as `django.test.AsyncClient`, or as `self.async_client` on any test.

_class_ AsyncClient(_enforce_csrf_checks =False_, _raise_request_exception =True_, _*_ , _headers =None_, _** defaults_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/test/client/#AsyncClient)[¶](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.AsyncClient "Link to this definition")

`AsyncClient` has the same methods and signatures as the synchronous (normal) test client, with the following exceptions:
  * In the initialization, arbitrary keyword arguments in `defaults` are added directly into the ASGI scope.
  * Headers passed as `extra` keyword arguments should not have the `HTTP_` prefix required by the synchronous client (see [`Client.get()`](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.Client.get "django.test.Client.get")). For example, here is how to set an HTTP `Accept` header:
```
>>> c = AsyncClient()
>>> c.get("/customers/details/", {"name": "fred", "age": 7}, ACCEPT="application/json")

```



Changed in Django 4.2:
The `headers` parameter was added.
Changed in Django 5.0:
Support for the `follow` parameter was added to the `AsyncClient`.
Using `AsyncClient` any method that makes a request must be awaited:
```
async def test_my_thing(self):
    response = await self.async_client.get("/some-url/")
    self.assertEqual(response.status_code, 200)

```

The asynchronous client can also call synchronous views; it runs through Django’s [asynchronous request path](https://docs.djangoproject.com/en/5.0/topics/async/), which supports both. Any view called through the `AsyncClient` will get an `ASGIRequest` object for its `request` rather than the `WSGIRequest` that the normal client creates.
Warning
If you are using test decorators, they must be async-compatible to ensure they work correctly. Django’s built-in decorators will behave correctly, but third-party ones may appear to not execute (they will “wrap” the wrong part of the execution flow and not your test).
If you need to use these decorators, then you should decorate your test methods with [`async_to_sync()`](https://docs.djangoproject.com/en/5.0/topics/async/#asgiref.sync.async_to_sync "asgiref.sync.async_to_sync") _inside_ of them instead:
```
from asgiref.sync import async_to_sync
from django.test import TestCase


class MyTests(TestCase):
    @mock.patch(...)
    @async_to_sync
    async def test_my_thing(self): ...

```
