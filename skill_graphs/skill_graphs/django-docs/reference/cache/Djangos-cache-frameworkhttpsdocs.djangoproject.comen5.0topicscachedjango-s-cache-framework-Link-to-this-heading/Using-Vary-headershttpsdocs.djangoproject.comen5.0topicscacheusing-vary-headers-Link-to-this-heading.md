## Using `Vary` headers[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#using-vary-headers "Link to this heading")
The `Vary` header defines which request headers a cache mechanism should take into account when building its cache key. For example, if the contents of a web page depend on a user’s language preference, the page is said to “vary on language.”
By default, Django’s cache system creates its cache keys using the requested fully-qualified URL – e.g., `"https://www.example.com/stories/2005/?order_by=author"`. This means every request to that URL will use the same cached version, regardless of user-agent differences such as cookies or language preferences. However, if this page produces different content based on some difference in request headers – such as a cookie, or a language, or a user-agent – you’ll need to use the `Vary` header to tell caching mechanisms that the page output depends on those things.
To do this in Django, use the convenient [`django.views.decorators.vary.vary_on_headers()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.vary.vary_on_headers "django.views.decorators.vary.vary_on_headers") view decorator, like so:
```
from django.views.decorators.vary import vary_on_headers


@vary_on_headers("User-Agent")
def my_view(request): ...

```

In this case, a caching mechanism (such as Django’s own cache middleware) will cache a separate version of the page for each unique user-agent.
The advantage to using the `vary_on_headers` decorator rather than manually setting the `Vary` header (using something like `response.headers['Vary'] = 'user-agent'`) is that the decorator _adds_ to the `Vary` header (which may already exist), rather than setting it from scratch and potentially overriding anything that was already in there.
You can pass multiple headers to `vary_on_headers()`:
```
@vary_on_headers("User-Agent", "Cookie")
def my_view(request): ...

```

This tells downstream caches to vary on _both_ , which means each combination of user-agent and cookie will get its own cache value. For example, a request with the user-agent `Mozilla` and the cookie value `foo=bar` will be considered different from a request with the user-agent `Mozilla` and the cookie value `foo=ham`.
Because varying on cookie is so common, there’s a [`django.views.decorators.vary.vary_on_cookie()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.vary.vary_on_cookie "django.views.decorators.vary.vary_on_cookie") decorator. These two views are equivalent:
```
@vary_on_cookie
def my_view(request): ...


@vary_on_headers("Cookie")
def my_view(request): ...

```

The headers you pass to `vary_on_headers` are not case sensitive; `"User-Agent"` is the same thing as `"user-agent"`.
You can also use a helper function, [`django.utils.cache.patch_vary_headers()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.patch_vary_headers "django.utils.cache.patch_vary_headers"), directly. This function sets, or adds to, the `Vary header`. For example:
```
from django.shortcuts import render
from django.utils.cache import patch_vary_headers


def my_view(request):
    ...
    response = render(request, "template_name", context)
    patch_vary_headers(response, ["Cookie"])
    return response

```

`patch_vary_headers` takes an [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") instance as its first argument and a list/tuple of case-insensitive header names as its second argument.
For more on Vary headers, see the
