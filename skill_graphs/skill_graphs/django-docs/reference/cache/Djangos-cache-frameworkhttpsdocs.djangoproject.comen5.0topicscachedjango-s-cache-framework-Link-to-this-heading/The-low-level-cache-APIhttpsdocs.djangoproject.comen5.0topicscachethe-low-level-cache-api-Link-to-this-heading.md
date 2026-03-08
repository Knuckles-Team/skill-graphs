## The low-level cache API[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#the-low-level-cache-api "Link to this heading")
Sometimes, caching an entire rendered page doesn’t gain you very much and is, in fact, inconvenient overkill.
Perhaps, for instance, your site includes a view whose results depend on several expensive queries, the results of which change at different intervals. In this case, it would not be ideal to use the full-page caching that the per-site or per-view cache strategies offer, because you wouldn’t want to cache the entire result (since some of the data changes often), but you’d still want to cache the results that rarely change.
For cases like this, Django exposes a low-level cache API. You can use this API to store objects in the cache with any level of granularity you like. You can cache any Python object that can be pickled safely: strings, dictionaries, lists of model objects, and so forth. (Most common Python objects can be pickled; refer to the Python documentation for more information about pickling.)
### Accessing the cache[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#accessing-the-cache "Link to this heading")

django.core.cache.caches[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.caches "Link to this definition")

You can access the caches configured in the [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES) setting through a dict-like object: `django.core.cache.caches`. Repeated requests for the same alias in the same thread will return the same object.
```
>>> from django.core.cache import caches
>>> cache1 = caches["myalias"]
>>> cache2 = caches["myalias"]
>>> cache1 is cache2
True

```

If the named key does not exist, `InvalidCacheBackendError` will be raised.
To provide thread-safety, a different instance of the cache backend will be returned for each thread.

django.core.cache.cache[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache "Link to this definition")

As a shortcut, the default cache is available as `django.core.cache.cache`:
```
>>> from django.core.cache import cache

```

This object is equivalent to `caches['default']`.
### Basic usage[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#basic-usage "Link to this heading")
The basic interface is:

cache.set(_key_ , _value_ , _timeout =DEFAULT_TIMEOUT_, _version =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.set "Link to this definition")

```
>>> cache.set("my_key", "hello, world!", 30)

```


cache.get(_key_ , _default =None_, _version =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.get "Link to this definition")

```
>>> cache.get("my_key")
'hello, world!'

```

`key` should be a `str`, and `value` can be any picklable Python object.
The `timeout` argument is optional and defaults to the `timeout` argument of the appropriate backend in the [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES) setting (explained above). It’s the number of seconds the value should be stored in the cache. Passing in `None` for `timeout` will cache the value forever. A `timeout` of `0` won’t cache the value.
If the object doesn’t exist in the cache, `cache.get()` returns `None`:
```
>>> # Wait 30 seconds for 'my_key' to expire...
>>> cache.get("my_key")
None

```

If you need to determine whether the object exists in the cache and you have stored a literal value `None`, use a sentinel object as the default:
```
>>> sentinel = object()
>>> cache.get("my_key", sentinel) is sentinel
False
>>> # Wait 30 seconds for 'my_key' to expire...
>>> cache.get("my_key", sentinel) is sentinel
True

```

`cache.get()` can take a `default` argument. This specifies which value to return if the object doesn’t exist in the cache:
```
>>> cache.get("my_key", "has expired")
'has expired'

```


cache.add(_key_ , _value_ , _timeout =DEFAULT_TIMEOUT_, _version =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.add "Link to this definition")

To add a key only if it doesn’t already exist, use the `add()` method. It takes the same parameters as `set()`, but it will not attempt to update the cache if the key specified is already present:
```
>>> cache.set("add_key", "Initial value")
>>> cache.add("add_key", "New value")
>>> cache.get("add_key")
'Initial value'

```

If you need to know whether `add()` stored a value in the cache, you can check the return value. It will return `True` if the value was stored, `False` otherwise.

cache.get_or_set(_key_ , _default_ , _timeout =DEFAULT_TIMEOUT_, _version =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.get_or_set "Link to this definition")

If you want to get a key’s value or set a value if the key isn’t in the cache, there is the `get_or_set()` method. It takes the same parameters as `get()` but the default is set as the new cache value for that key, rather than returned:
```
>>> cache.get("my_new_key")  # returns None
>>> cache.get_or_set("my_new_key", "my new value", 100)
'my new value'

```

You can also pass any callable as a _default_ value:
```
>>> import datetime
>>> cache.get_or_set("some-timestamp-key", datetime.datetime.now)
datetime.datetime(2014, 12, 11, 0, 15, 49, 457920)

```


cache.get_many(_keys_ , _version =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.get_many "Link to this definition")

There’s also a `get_many()` interface that only hits the cache once. `get_many()` returns a dictionary with all the keys you asked for that actually exist in the cache (and haven’t expired):
```
>>> cache.set("a", 1)
>>> cache.set("b", 2)
>>> cache.set("c", 3)
>>> cache.get_many(["a", "b", "c"])
{'a': 1, 'b': 2, 'c': 3}

```


cache.set_many(_dict_ , _timeout_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.set_many "Link to this definition")

To set multiple values more efficiently, use `set_many()` to pass a dictionary of key-value pairs:
```
>>> cache.set_many({"a": 1, "b": 2, "c": 3})
>>> cache.get_many(["a", "b", "c"])
{'a': 1, 'b': 2, 'c': 3}

```

Like `cache.set()`, `set_many()` takes an optional `timeout` parameter.
On supported backends (memcached), `set_many()` returns a list of keys that failed to be inserted.

cache.delete(_key_ , _version =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.delete "Link to this definition")

You can delete keys explicitly with `delete()` to clear the cache for a particular object:
```
>>> cache.delete("a")
True

```

`delete()` returns `True` if the key was successfully deleted, `False` otherwise.

cache.delete_many(_keys_ , _version =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.delete_many "Link to this definition")

If you want to clear a bunch of keys at once, `delete_many()` can take a list of keys to be cleared:
```
>>> cache.delete_many(["a", "b", "c"])

```


cache.clear()[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.clear "Link to this definition")

Finally, if you want to delete all the keys in the cache, use `cache.clear()`. Be careful with this; `clear()` will remove _everything_ from the cache, not just the keys set by your application. :
```
>>> cache.clear()

```


cache.touch(_key_ , _timeout =DEFAULT_TIMEOUT_, _version =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.touch "Link to this definition")

`cache.touch()` sets a new expiration for a key. For example, to update a key to expire 10 seconds from now:
```
>>> cache.touch("a", 10)
True

```

Like other methods, the `timeout` argument is optional and defaults to the `TIMEOUT` option of the appropriate backend in the [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES) setting.
`touch()` returns `True` if the key was successfully touched, `False` otherwise.

cache.incr(_key_ , _delta =1_, _version =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.incr "Link to this definition")


cache.decr(_key_ , _delta =1_, _version =None_)[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.decr "Link to this definition")

You can also increment or decrement a key that already exists using the `incr()` or `decr()` methods, respectively. By default, the existing cache value will be incremented or decremented by 1. Other increment/decrement values can be specified by providing an argument to the increment/decrement call. A ValueError will be raised if you attempt to increment or decrement a nonexistent cache key:
```
>>> cache.set("num", 1)
>>> cache.incr("num")
2
>>> cache.incr("num", 10)
12
>>> cache.decr("num")
11
>>> cache.decr("num", 5)
6

```

Note
`incr()`/`decr()` methods are not guaranteed to be atomic. On those backends that support atomic increment/decrement (most notably, the memcached backend), increment and decrement operations will be atomic. However, if the backend doesn’t natively provide an increment/decrement operation, it will be implemented using a two-step retrieve/update.

cache.close()[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#django.core.cache.cache.close "Link to this definition")

You can close the connection to your cache with `close()` if implemented by the cache backend.
```
>>> cache.close()

```

Note
For caches that don’t implement `close` methods it is a no-op.
Note
The async variants of base methods are prefixed with `a`, e.g. `cache.aadd()` or `cache.adelete_many()`. See [Asynchronous support](https://docs.djangoproject.com/en/5.0/topics/cache/#id14) for more details.
### Cache key prefixing[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#cache-key-prefixing "Link to this heading")
If you are sharing a cache instance between servers, or between your production and development environments, it’s possible for data cached by one server to be used by another server. If the format of cached data is different between servers, this can lead to some very hard to diagnose problems.
To prevent this, Django provides the ability to prefix all cache keys used by a server. When a particular cache key is saved or retrieved, Django will automatically prefix the cache key with the value of the [`KEY_PREFIX`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES-KEY_PREFIX) cache setting.
By ensuring each Django instance has a different [`KEY_PREFIX`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES-KEY_PREFIX), you can ensure that there will be no collisions in cache values.
### Cache versioning[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#cache-versioning "Link to this heading")
When you change running code that uses cached values, you may need to purge any existing cached values. The easiest way to do this is to flush the entire cache, but this can lead to the loss of cache values that are still valid and useful.
Django provides a better way to target individual cache values. Django’s cache framework has a system-wide version identifier, specified using the [`VERSION`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES-VERSION) cache setting. The value of this setting is automatically combined with the cache prefix and the user-provided cache key to obtain the final cache key.
By default, any key request will automatically include the site default cache key version. However, the primitive cache functions all include a `version` argument, so you can specify a particular cache key version to set or get. For example:
```
>>> # Set version 2 of a cache key
>>> cache.set("my_key", "hello world!", version=2)
>>> # Get the default version (assuming version=1)
>>> cache.get("my_key")
None
>>> # Get version 2 of the same key
>>> cache.get("my_key", version=2)
'hello world!'

```

The version of a specific key can be incremented and decremented using the `incr_version()` and `decr_version()` methods. This enables specific keys to be bumped to a new version, leaving other keys unaffected. Continuing our previous example:
```
>>> # Increment the version of 'my_key'
>>> cache.incr_version("my_key")
>>> # The default version still isn't available
>>> cache.get("my_key")
None
# Version 2 isn't available, either
>>> cache.get("my_key", version=2)
None
>>> # But version 3 *is* available
>>> cache.get("my_key", version=3)
'hello world!'

```

### Cache key transformation[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#cache-key-transformation "Link to this heading")
As described in the previous two sections, the cache key provided by a user is not used verbatim – it is combined with the cache prefix and key version to provide a final cache key. By default, the three parts are joined using colons to produce a final string:
```
def make_key(key, key_prefix, version):
    return "%s:%s:%s" % (key_prefix, version, key)

```

If you want to combine the parts in different ways, or apply other processing to the final key (e.g., taking a hash digest of the key parts), you can provide a custom key function.
The [`KEY_FUNCTION`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES-KEY_FUNCTION) cache setting specifies a dotted-path to a function matching the prototype of `make_key()` above. If provided, this custom key function will be used instead of the default key combining function.
### Cache key warnings[¶](https://docs.djangoproject.com/en/5.0/topics/cache/#cache-key-warnings "Link to this heading")
Memcached, the most commonly-used production cache backend, does not allow cache keys longer than 250 characters or containing whitespace or control characters, and using such keys will cause an exception. To encourage cache-portable code and minimize unpleasant surprises, the other built-in cache backends issue a warning (`django.core.cache.backends.base.CacheKeyWarning`) if a key is used that would cause an error on memcached.
If you are using a production backend that can accept a wider range of keys (a custom backend, or one of the non-memcached built-in backends), and want to use this wider range without warnings, you can silence `CacheKeyWarning` with this code in the `management` module of one of your [`INSTALLED_APPS`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-INSTALLED_APPS):
```
import warnings

from django.core.cache import CacheKeyWarning

warnings.simplefilter("ignore", CacheKeyWarning)

```

If you want to instead provide custom key validation logic for one of the built-in backends, you can subclass it, override just the `validate_key` method, and follow the instructions for [using a custom cache backend](https://docs.djangoproject.com/en/5.0/topics/cache/#using-a-custom-cache-backend). For instance, to do this for the `locmem` backend, put this code in a module:
```
from django.core.cache.backends.locmem import LocMemCache


class CustomLocMemCache(LocMemCache):
    def validate_key(self, key):
        """Custom validation, raising exceptions or warnings as needed."""
        ...

```

…and use the dotted Python path to this class in the [`BACKEND`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES-BACKEND) portion of your [`CACHES`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-CACHES) setting.
