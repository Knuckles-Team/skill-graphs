## The per-site cache[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#the-per-site-cache "Link to this heading")
Once the cache is set up, the simplest way to use caching is to cache your entire site. You’ll need to add `'django.middleware.cache.UpdateCacheMiddleware'` and `'django.middleware.cache.FetchFromCacheMiddleware'` to your [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) setting, as in this example:
```
MIDDLEWARE = [
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

```

Note
No, that’s not a typo: the “update” middleware must be first in the list, and the “fetch” middleware must be last. The details are a bit obscure, but see [Order of MIDDLEWARE](https://docs.djangoproject.com/en/5.0/topics/cache/#order-of-middleware) below if you’d like the full story.
Then, add the following required settings to your Django settings file:
  * [`CACHE_MIDDLEWARE_ALIAS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_ALIAS) – The cache alias to use for storage.
  * [`CACHE_MIDDLEWARE_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_SECONDS) – The integer number of seconds each page should be cached.
  * [`CACHE_MIDDLEWARE_KEY_PREFIX`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_KEY_PREFIX) – If the cache is shared across multiple sites using the same Django installation, set this to the name of the site, or some other string that is unique to this Django instance, to prevent key collisions. Use an empty string if you don’t care.


`FetchFromCacheMiddleware` caches GET and HEAD responses with status 200, where the request and response headers allow. Responses to requests for the same URL with different query parameters are considered to be unique pages and are cached separately. This middleware expects that a HEAD request is answered with the same response headers as the corresponding GET request; in which case it can return a cached GET response for HEAD request.
Additionally, `UpdateCacheMiddleware` automatically sets a few headers in each [`HttpResponse`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse "django.http.HttpResponse") which affect [downstream caches](https://docs.djangoproject.com/en/5.0/topics/cache/#downstream-caches):
  * Sets the `Expires` header to the current date/time plus the defined [`CACHE_MIDDLEWARE_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_SECONDS).
  * Sets the `Cache-Control` header to give a max age for the page – again, from the [`CACHE_MIDDLEWARE_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_SECONDS) setting.


See [Middleware](https://docs.djangoproject.com/en/5.0/topics/http/middleware/) for more on middleware.
If a view sets its own cache expiry time (i.e. it has a `max-age` section in its `Cache-Control` header) then the page will be cached until the expiry time, rather than [`CACHE_MIDDLEWARE_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_SECONDS). Using the decorators in `django.views.decorators.cache` you can easily set a view’s expiry time (using the [`cache_control()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.cache.cache_control "django.views.decorators.cache.cache_control") decorator) or disable caching for a view (using the [`never_cache()`](https://docs.djangoproject.com/en/5.0/topics/http/decorators/#django.views.decorators.cache.never_cache "django.views.decorators.cache.never_cache") decorator). See the [using other headers](https://docs.djangoproject.com/en/5.0/topics/cache/#controlling-cache-using-other-headers) section for more on these decorators.
If [`USE_I18N`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_I18N) is set to `True` then the generated cache key will include the name of the active [language](https://docs.djangoproject.com/en/5.0/topics/i18n/#term-language-code) – see also [How Django discovers language preference](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#how-django-discovers-language-preference)). This allows you to easily cache multilingual sites without having to create the cache key yourself.
Cache keys also include the [current time zone](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#default-current-time-zone) when [`USE_TZ`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_TZ) is set to `True`.
