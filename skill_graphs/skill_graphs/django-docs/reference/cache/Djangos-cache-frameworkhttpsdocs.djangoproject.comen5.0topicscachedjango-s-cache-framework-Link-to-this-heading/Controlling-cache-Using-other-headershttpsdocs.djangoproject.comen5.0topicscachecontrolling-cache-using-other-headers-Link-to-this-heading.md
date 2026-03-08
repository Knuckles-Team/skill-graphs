## Controlling cache: Using other headers[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#controlling-cache-using-other-headers "Link to this heading")
Other problems with caching are the privacy of data and the question of where data should be stored in a cascade of caches.
A user usually faces two kinds of caches: their own browser cache (a private cache) and their provider’s cache (a public cache). A public cache is used by multiple users and controlled by someone else. This poses problems with sensitive data–you don’t want, say, your bank account number stored in a public cache. So web applications need a way to tell caches which data is private and which is public.
The solution is to indicate a page’s cache should be “private.” To do this in Django, use the [`cache_control()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.cache.cache_control "django.views.decorators.cache.cache_control") view decorator. Example:
```
from django.views.decorators.cache import cache_control


@cache_control(private=True)
def my_view(request): ...

```

This decorator takes care of sending out the appropriate HTTP header behind the scenes.
Note that the cache control settings “private” and “public” are mutually exclusive. The decorator ensures that the “public” directive is removed if “private” should be set (and vice versa). An example use of the two directives would be a blog site that offers both private and public entries. Public entries may be cached on any shared cache. The following code uses [`patch_cache_control()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.patch_cache_control "django.utils.cache.patch_cache_control"), the manual way to modify the cache control header (it is internally called by the [`cache_control()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.cache.cache_control "django.views.decorators.cache.cache_control") decorator):
```
from django.views.decorators.cache import patch_cache_control
from django.views.decorators.vary import vary_on_cookie


@vary_on_cookie
def list_blog_entries_view(request):
    if request.user.is_anonymous:
        response = render_only_public_entries()
        patch_cache_control(response, public=True)
    else:
        response = render_private_and_public_entries(request.user)
        patch_cache_control(response, private=True)

    return response

```

You can control downstream caches in other ways as well (see
```
from django.views.decorators.cache import cache_control


@cache_control(max_age=3600)
def my_view(request): ...

```

(If you _do_ use the caching middleware, it already sets the `max-age` with the value of the [`CACHE_MIDDLEWARE_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_SECONDS) setting. In that case, the custom `max_age` from the [`cache_control()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.cache.cache_control "django.views.decorators.cache.cache_control") decorator will take precedence, and the header values will be merged correctly.)
Any valid `Cache-Control` response directive is valid in `cache_control()`. Here are some more examples:
  * `no_transform=True`
  * `must_revalidate=True`
  * `stale_while_revalidate=num_seconds`
  * `no_cache=True`


The full list of known directives can be found in the
If you want to use headers to disable caching altogether, [`never_cache()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.cache.never_cache "django.views.decorators.cache.never_cache") is a view decorator that adds headers to ensure the response won’t be cached by browsers or other caches. Example:
```
from django.views.decorators.cache import never_cache


@never_cache
def myview(request): ...

```
