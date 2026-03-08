##  `QueryDict` objects[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#querydict-objects "Link to this heading")

_class_ QueryDict[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict "Link to this definition")

In an [`HttpRequest`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest "django.http.HttpRequest") object, the [`GET`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.GET "django.http.HttpRequest.GET") and [`POST`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpRequest.POST "django.http.HttpRequest.POST") attributes are instances of `django.http.QueryDict`, a dictionary-like class customized to deal with multiple values for the same key. This is necessary because some HTML form elements, notably `<select multiple>`, pass multiple values for the same key.
The `QueryDict`s at `request.POST` and `request.GET` will be immutable when accessed in a normal request/response cycle. To get a mutable version you need to use [`QueryDict.copy()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.copy "django.http.QueryDict.copy").
### Methods[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#id1 "Link to this heading")
[`QueryDict`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict "django.http.QueryDict") implements all the standard dictionary methods because it’s a subclass of dictionary. Exceptions are outlined here:

QueryDict.__init__(_query_string =None_, _mutable =False_, _encoding =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.__init__)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.__init__ "Link to this definition")

Instantiates a `QueryDict` object based on `query_string`.
```
>>> QueryDict("a=1&a=2&c=3")
<QueryDict: {'a': ['1', '2'], 'c': ['3']}>

```

If `query_string` is not passed in, the resulting `QueryDict` will be empty (it will have no keys or values).
Most `QueryDict`s you encounter, and in particular those at `request.POST` and `request.GET`, will be immutable. If you are instantiating one yourself, you can make it mutable by passing `mutable=True` to its `__init__()`.
Strings for setting both keys and values will be converted from `encoding` to `str`. If `encoding` is not set, it defaults to [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DEFAULT_CHARSET).

_classmethod_ QueryDict.fromkeys(_iterable_ , _value =''_, _mutable =False_, _encoding =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.fromkeys)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.fromkeys "Link to this definition")

Creates a new `QueryDict` with keys from `iterable` and each value equal to `value`. For example:
```
>>> QueryDict.fromkeys(["a", "a", "b"], value="val")
<QueryDict: {'a': ['val', 'val'], 'b': ['val']}>

```


QueryDict.__getitem__(_key_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.__getitem__ "Link to this definition")

Returns the value for the given key. If the key has more than one value, it returns the last value. Raises `django.utils.datastructures.MultiValueDictKeyError` if the key does not exist. (This is a subclass of Python’s standard `KeyError`.)

QueryDict.__setitem__(_key_ , _value_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.__setitem__)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.__setitem__ "Link to this definition")

Sets the given key to `[value]` (a list whose single element is `value`). Note that this, as other dictionary functions that have side effects, can only be called on a mutable `QueryDict` (such as one that was created via [`QueryDict.copy()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.copy "django.http.QueryDict.copy")).

QueryDict.__contains__(_key_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.__contains__ "Link to this definition")

Returns `True` if the given key is set. This lets you do, e.g., `if "foo" in request.GET`.

QueryDict.get(_key_ , _default =None_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.get "Link to this definition")

Uses the same logic as [`__getitem__()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.__getitem__ "django.http.QueryDict.__getitem__"), with a hook for returning a default value if the key doesn’t exist.

QueryDict.setdefault(_key_ , _default =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.setdefault)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.setdefault "Link to this definition")

Like [`__setitem__()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.__setitem__ "django.http.QueryDict.__setitem__") internally.

QueryDict.update(_other_dict_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.update "Link to this definition")

Takes either a `QueryDict` or a dictionary. Like _appends_ to the current dictionary items rather than replacing them. For example:
```
>>> q = QueryDict("a=1", mutable=True)
>>> q.update({"a": "2"})
>>> q.getlist("a")
['1', '2']
>>> q["a"]  # returns the last
'2'

```


QueryDict.items()[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.items "Link to this definition")

Like [`__getitem__()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.__getitem__ "django.http.QueryDict.__getitem__") and returns an iterator object instead of a view object. For example:
```
>>> q = QueryDict("a=1&a=2&a=3")
>>> list(q.items())
[('a', '3')]

```


QueryDict.values()[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.values "Link to this definition")

Like [`__getitem__()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.__getitem__ "django.http.QueryDict.__getitem__") and returns an iterator instead of a view object. For example:
```
>>> q = QueryDict("a=1&a=2&a=3")
>>> list(q.values())
['3']

```

In addition, `QueryDict` has the following methods:

QueryDict.copy()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.copy)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.copy "Link to this definition")

Returns a copy of the object using

QueryDict.getlist(_key_ , _default =None_)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.getlist "Link to this definition")

Returns a list of the data with the requested key. Returns an empty list if the key doesn’t exist and `default` is `None`. It’s guaranteed to return a list unless the default value provided isn’t a list.

QueryDict.setlist(_key_ , _list__)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.setlist)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.setlist "Link to this definition")

Sets the given key to `list_` (unlike [`__setitem__()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.__setitem__ "django.http.QueryDict.__setitem__")).

QueryDict.appendlist(_key_ , _item_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.appendlist)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.appendlist "Link to this definition")

Appends an item to the internal list associated with key.

QueryDict.setlistdefault(_key_ , _default_list =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.setlistdefault)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.setlistdefault "Link to this definition")

Like [`setdefault()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.setdefault "django.http.QueryDict.setdefault"), except it takes a list of values instead of a single value.

QueryDict.lists()[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.lists "Link to this definition")

Like [`items()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.items "django.http.QueryDict.items"), except it includes all values, as a list, for each member of the dictionary. For example:
```
>>> q = QueryDict("a=1&a=2&a=3")
>>> q.lists()
[('a', ['1', '2', '3'])]

```


QueryDict.pop(_key_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.pop)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.pop "Link to this definition")

Returns a list of values for the given key and removes them from the dictionary. Raises `KeyError` if the key does not exist. For example:
```
>>> q = QueryDict("a=1&a=2&a=3", mutable=True)
>>> q.pop("a")
['1', '2', '3']

```


QueryDict.popitem()[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.popitem)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.popitem "Link to this definition")

Removes an arbitrary member of the dictionary (since there’s no concept of ordering), and returns a two value tuple containing the key and a list of all values for the key. Raises `KeyError` when called on an empty dictionary. For example:
```
>>> q = QueryDict("a=1&a=2&a=3", mutable=True)
>>> q.popitem()
('a', ['1', '2', '3'])

```


QueryDict.dict()[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.dict "Link to this definition")

Returns a `dict` representation of `QueryDict`. For every (key, list) pair in `QueryDict`, `dict` will have (key, item), where item is one element of the list, using the same logic as [`QueryDict.__getitem__()`](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.__getitem__ "django.http.QueryDict.__getitem__"):
```
>>> q = QueryDict("a=1&a=3&a=5")
>>> q.dict()
{'a': '5'}

```


QueryDict.urlencode(_safe =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/http/request/#QueryDict.urlencode)[¶](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.QueryDict.urlencode "Link to this definition")

Returns a string of the data in query string format. For example:
```
>>> q = QueryDict("a=2&b=3&b=5")
>>> q.urlencode()
'a=2&b=3&b=5'

```

Use the `safe` parameter to pass characters which don’t require encoding. For example:
```
>>> q = QueryDict(mutable=True)
>>> q["next"] = "/a&b/"
>>> q.urlencode(safe="/")
'next=/a%26b/'

```
