## Template fragment caching[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#template-fragment-caching "Link to this heading")
If you’re after even more control, you can also cache template fragments using the `cache` template tag. To give your template access to this tag, put `{% load cache %}` near the top of your template.
The `{% cache %}` template tag caches the contents of the block for a given amount of time. It takes at least two arguments: the cache timeout, in seconds, and the name to give the cache fragment. The fragment is cached forever if timeout is `None`. The name will be taken as is, do not use a variable. For example:
```
{% load cache %}
{% cache 500 sidebar %}
    .. sidebar ..
{% endcache %}

```

Sometimes you might want to cache multiple copies of a fragment depending on some dynamic data that appears inside the fragment. For example, you might want a separate cached copy of the sidebar used in the previous example for every user of your site. Do this by passing one or more additional arguments, which may be variables with or without filters, to the `{% cache %}` template tag to uniquely identify the cache fragment:
```
{% load cache %}
{% cache 500 sidebar request.user.username %}
    .. sidebar for logged in user ..
{% endcache %}

```

If [`USE_I18N`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-USE_I18N) is set to `True` the per-site middleware cache will [respect the active language](https://docs.djangoproject.com/en/5.0/topics/cache/#i18n-cache-key). For the `cache` template tag you could use one of the [translation-specific variables](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/#template-translation-vars) available in templates to achieve the same result:
```
{% load i18n %}
{% load cache %}

{% get_current_language as LANGUAGE_CODE %}

{% cache 600 welcome LANGUAGE_CODE %}
    {% translate "Welcome to example.com" %}
{% endcache %}

```

The cache timeout can be a template variable, as long as the template variable resolves to an integer value. For example, if the template variable `my_timeout` is set to the value `600`, then the following two examples are equivalent:
```
{% cache 600 sidebar %} ... {% endcache %}
{% cache my_timeout sidebar %} ... {% endcache %}

```

This feature is useful in avoiding repetition in templates. You can set the timeout in a variable, in one place, and reuse that value.
By default, the cache tag will try to use the cache called “template_fragments”. If no such cache exists, it will fall back to using the default cache. You may select an alternate cache backend to use with the `using` keyword argument, which must be the last argument to the tag.
```
{% cache 300 local-thing ...  using="localcache" %}

```

It is considered an error to specify a cache name that is not configured.

django.core.cache.utils.make_template_fragment_key(_fragment_name_ , _vary_on =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.utils.make_template_fragment_key "Link to this definition")

If you want to obtain the cache key used for a cached fragment, you can use `make_template_fragment_key`. `fragment_name` is the same as second argument to the `cache` template tag; `vary_on` is a list of all additional arguments passed to the tag. This function can be useful for invalidating or overwriting a cached item, for example:
```
>>> from django.core.cache import cache
>>> from django.core.cache.utils import make_template_fragment_key
# cache key for {% cache 500 sidebar username %}
>>> key = make_template_fragment_key("sidebar", [username])
>>> cache.delete(key)  # invalidates cached template fragment
True

```
