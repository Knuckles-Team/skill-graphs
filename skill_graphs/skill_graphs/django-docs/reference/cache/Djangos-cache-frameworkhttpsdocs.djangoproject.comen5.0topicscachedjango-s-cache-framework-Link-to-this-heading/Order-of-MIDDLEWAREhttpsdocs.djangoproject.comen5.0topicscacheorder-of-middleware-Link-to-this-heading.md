## Order of `MIDDLEWARE`[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#order-of-middleware "Link to this heading")
If you use caching middleware, it’s important to put each half in the right place within the [`MIDDLEWARE`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MIDDLEWARE) setting. That’s because the cache middleware needs to know which headers by which to vary the cache storage. Middleware always adds something to the `Vary` response header when it can.
`UpdateCacheMiddleware` runs during the response phase, where middleware is run in reverse order, so an item at the top of the list runs _last_ during the response phase. Thus, you need to make sure that `UpdateCacheMiddleware` appears _before_ any other middleware that might add something to the `Vary` header. The following middleware modules do so:
  * `SessionMiddleware` adds `Cookie`
  * `GZipMiddleware` adds `Accept-Encoding`
  * `LocaleMiddleware` adds `Accept-Language`


`FetchFromCacheMiddleware`, on the other hand, runs during the request phase, where middleware is applied first-to-last, so an item at the top of the list runs _first_ during the request phase. The `FetchFromCacheMiddleware` also needs to run after other middleware updates the `Vary` header, so `FetchFromCacheMiddleware` must be _after_ any item that does so.
Previous page and next page
[](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/)
[Conditional View Processing ](https://docs.djangoproject.com/en/5.0/topics/conditional-view-processing/)
[](https://docs.djangoproject.com/en/5.0/topics/cache/#top)
