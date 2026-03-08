## Asynchronous support[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#asynchronous-support "Link to this heading")
Django has developing support for asynchronous cache backends, but does not yet support asynchronous caching. It will be coming in a future release.
`django.core.cache.backends.base.BaseCache` has async variants of [all base methods](https://docs.djangoproject.com/en/5.0/topics/cache/#cache-basic-interface). By convention, the asynchronous versions of all methods are prefixed with `a`. By default, the arguments for both variants are the same:
```
>>> await cache.aset("num", 1)
>>> await cache.ahas_key("num")
True

```
