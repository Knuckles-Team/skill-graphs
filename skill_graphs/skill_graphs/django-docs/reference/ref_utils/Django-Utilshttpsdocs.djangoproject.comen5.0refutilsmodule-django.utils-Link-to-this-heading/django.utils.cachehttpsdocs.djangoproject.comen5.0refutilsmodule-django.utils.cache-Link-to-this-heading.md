##  `django.utils.cache`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.cache "Link to this heading")
This module contains helper functions for controlling HTTP caching. It does so by managing the `Vary` header of responses. It includes functions to patch the header of response objects directly and decorators that change functions to do that header-patching themselves.
For information on the `Vary` header, see
Essentially, the `Vary` HTTP header defines which headers a cache should take into account when building its cache key. Requests with the same path but different header content for headers named in `Vary` need to get different cache keys to prevent delivery of wrong content.
For example, [internationalization](https://docs.djangoproject.com/en/5.0/topics/i18n/) middleware would need to distinguish caches by the `Accept-language` header.

patch_cache_control(_response_ , _** kwargs_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/cache/#patch_cache_control)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.patch_cache_control "Link to this definition")

This function patches the `Cache-Control` header by adding all keyword arguments to it. The transformation is as follows:
  * All keyword parameter names are turned to lowercase, and underscores are converted to hyphens.
  * If the value of a parameter is `True` (exactly `True`, not just a true value), only the parameter name is added to the header.
  * All other parameters are added with their value, after applying `str()` to it.



get_max_age(_response_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/cache/#get_max_age)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.get_max_age "Link to this definition")

Returns the max-age from the response Cache-Control header as an integer (or `None` if it wasn’t found or wasn’t an integer).

patch_response_headers(_response_ , _cache_timeout =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/cache/#patch_response_headers)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.patch_response_headers "Link to this definition")

Adds some useful headers to the given `HttpResponse` object:
  * `Expires`
  * `Cache-Control`


Each header is only added if it isn’t already set.
`cache_timeout` is in seconds. The [`CACHE_MIDDLEWARE_SECONDS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHE_MIDDLEWARE_SECONDS) setting is used by default.

add_never_cache_headers(_response_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/cache/#add_never_cache_headers)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.add_never_cache_headers "Link to this definition")

Adds an `Expires` header to the current date/time.
Adds a `Cache-Control: max-age=0, no-cache, no-store, must-revalidate, private` header to a response to indicate that a page should never be cached.
Each header is only added if it isn’t already set.

patch_vary_headers(_response_ , _newheaders_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/cache/#patch_vary_headers)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.patch_vary_headers "Link to this definition")

Adds (or updates) the `Vary` header in the given `HttpResponse` object. `newheaders` is a list of header names that should be in `Vary`. If headers contains an asterisk, then `Vary` header will consist of a single asterisk `'*'`, according to `Vary` aren’t removed.

get_cache_key(_request_ , _key_prefix =None_, _method ='GET'_, _cache =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/cache/#get_cache_key)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.get_cache_key "Link to this definition")

Returns a cache key based on the request path. It can be used in the request phase because it pulls the list of headers to take into account from the global path registry and uses those to build a cache key to check against.
If there is no headerlist stored, the page needs to be rebuilt, so this function returns `None`.

learn_cache_key(_request_ , _response_ , _cache_timeout =None_, _key_prefix =None_, _cache =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/cache/#learn_cache_key)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.cache.learn_cache_key "Link to this definition")

Learns what headers to take into account for some request path from the response object. It stores those headers in a global path registry so that later access to that path will know what headers to take into account without building the response object itself. The headers are named in the `Vary` header of the response, but we want to prevent response generation.
The list of headers to use for cache key generation is stored in the same cache as the pages themselves. If the cache ages some data out of the cache, this means that we have to build the response once to get at the Vary header and so at the list of headers to use for the cache key.
