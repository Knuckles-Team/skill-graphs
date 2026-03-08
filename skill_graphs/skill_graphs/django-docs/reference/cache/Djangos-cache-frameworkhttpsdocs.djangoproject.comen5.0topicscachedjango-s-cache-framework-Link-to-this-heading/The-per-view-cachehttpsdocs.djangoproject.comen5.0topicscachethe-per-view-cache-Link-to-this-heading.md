## The per-view cache[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#the-per-view-cache "Link to this heading")

django.views.decorators.cache.cache_page(_timeout_ , _*_ , _cache =None_, _key_prefix =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.views.decorators.cache.cache_page "Link to this definition")

A more granular way to use the caching framework is by caching the output of individual views. `django.views.decorators.cache` defines a `cache_page` decorator that will automatically cache the view’s response for you:
```
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def my_view(request): ...

```

`cache_page` takes a single argument: the cache timeout, in seconds. In the above example, the result of the `my_view()` view will be cached for 15 minutes. (Note that we’ve written it as `60 * 15` for the purpose of readability. `60 * 15` will be evaluated to `900` – that is, 15 minutes multiplied by 60 seconds per minute.)
The cache timeout set by `cache_page` takes precedence over the `max-age` directive from the `Cache-Control` header.
The per-view cache, like the per-site cache, is keyed off of the URL. If multiple URLs point at the same view, each URL will be cached separately. Continuing the `my_view` example, if your URLconf looks like this:
```
urlpatterns = [
    path("foo/<int:code>/", my_view),
]

```

then requests to `/foo/1/` and `/foo/23/` will be cached separately, as you may expect. But once a particular URL (e.g., `/foo/23/`) has been requested, subsequent requests to that URL will use the cache.
`cache_page` can also take an optional keyword argument, `cache`, which directs the decorator to use a specific cache (from your [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES) setting) when caching view results. By default, the `default` cache will be used, but you can specify any cache you want:
```
@cache_page(60 * 15, cache="special_cache")
def my_view(request): ...

```

You can also override the cache prefix on a per-view basis. `cache_page` takes an optional keyword argument, `key_prefix`, which works in the same way as the [`CACHE_MIDDLEWARE_KEY_PREFIX`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_KEY_PREFIX) setting for the middleware. It can be used like this:
```
@cache_page(60 * 15, key_prefix="site1")
def my_view(request): ...

```

The `key_prefix` and `cache` arguments may be specified together. The `key_prefix` argument and the [`KEY_PREFIX`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES-KEY_PREFIX) specified under [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES) will be concatenated.
Additionally, `cache_page` automatically sets `Cache-Control` and `Expires` headers in the response which affect [downstream caches](https://docs.djangoproject.com/en/5.0/topics/cache/#downstream-caches).
### Specifying per-view cache in the URLconf[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#specifying-per-view-cache-in-the-urlconf "Link to this heading")
The examples in the previous section have hard-coded the fact that the view is cached, because `cache_page` alters the `my_view` function in place. This approach couples your view to the cache system, which is not ideal for several reasons. For instance, you might want to reuse the view functions on another, cache-less site, or you might want to distribute the views to people who might want to use them without being cached. The solution to these problems is to specify the per-view cache in the URLconf rather than next to the view functions themselves.
You can do so by wrapping the view function with `cache_page` when you refer to it in the URLconf. Here’s the old URLconf from earlier:
```
urlpatterns = [
    path("foo/<int:code>/", my_view),
]

```

Here’s the same thing, with `my_view` wrapped in `cache_page`:
```
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("foo/<int:code>/", cache_page(60 * 15)(my_view)),
]

```
