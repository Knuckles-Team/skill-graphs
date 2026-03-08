##  `django.utils.functional`[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#module-django.utils.functional "Link to this heading")

_class_ cached_property(_func_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/functional/#cached_property)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.functional.cached_property "Link to this definition")

The `@cached_property` decorator caches the result of a method with a single `self` argument as a property. The cached result will persist as long as the instance does, so if the instance is passed around and the function subsequently invoked, the cached result will be returned.
Consider a typical case, where a view might need to call a model’s method to perform some computation, before placing the model instance into the context, where the template might invoke the method once more:
```
# the model
class Person(models.Model):
    def friends(self):
        # expensive computation
        ...
        return friends


# in the view:
if person.friends():
    ...

```

And in the template you would have:
```
{% for friend in person.friends %}

```

Here, `friends()` will be called twice. Since the instance `person` in the view and the template are the same, decorating the `friends()` method with `@cached_property` can avoid that:
```
from django.utils.functional import cached_property


class Person(models.Model):
    @cached_property
    def friends(self): ...

```

Note that as the method is now a property, in Python code it will need to be accessed appropriately:
```
# in the view:
if person.friends:
    ...

```

The cached value can be treated like an ordinary attribute of the instance:
```
# clear it, requiring re-computation next time it's called
del person.friends  # or delattr(person, "friends")

# set a value manually, that will persist on the instance until cleared
person.friends = ["Huckleberry Finn", "Tom Sawyer"]

```

Because of the way the `del` (or `delattr`) on a `cached_property` that hasn’t been accessed raises `AttributeError`.
As well as offering potential performance advantages, `@cached_property` can ensure that an attribute’s value does not change unexpectedly over the life of an instance. This could occur with a method whose computation is based on `datetime.now()`, or if a change were saved to the database by some other process in the brief interval between subsequent invocations of a method on the same instance.
You can make cached properties of methods. For example, if you had an expensive `get_friends()` method and wanted to allow calling it without retrieving the cached value, you could write:
```
friends = cached_property(get_friends)

```

While `person.get_friends()` will recompute the friends on each call, the value of the cached property will persist until you delete it as described above:
```
x = person.friends  # calls first time
y = person.get_friends()  # calls again
z = person.friends  # does not call
x is z  # is True

```


_class_ classproperty(_method =None_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/functional/#classproperty)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.functional.classproperty "Link to this definition")

Similar to `@classproperty` decorator converts the result of a method with a single `cls` argument into a property that can be accessed directly from the class.

keep_lazy(_func_ , _* resultclasses_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/functional/#keep_lazy)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.functional.keep_lazy "Link to this definition")

Django offers many utility functions (particularly in `django.utils`) that take a string as their first argument and do something to that string. These functions are used by template filters as well as directly in other code.
If you write your own similar functions and deal with translations, you’ll face the problem of what to do when the first argument is a lazy translation object. You don’t want to convert it to a string immediately, because you might be using this function outside of a view (and hence the current thread’s locale setting will not be correct).
For cases like this, use the `django.utils.functional.keep_lazy()` decorator. It modifies the function so that _if_ it’s called with a lazy translation as one of its arguments, the function evaluation is delayed until it needs to be converted to a string.
For example:
```
from django.utils.functional import keep_lazy, keep_lazy_text


def fancy_utility_function(s, *args, **kwargs):
    # Do some conversion on string 's'
    ...


fancy_utility_function = keep_lazy(str)(fancy_utility_function)


# Or more succinctly:
@keep_lazy(str)
def fancy_utility_function(s, *args, **kwargs): ...

```

The `keep_lazy()` decorator takes a number of extra arguments (`*args`) specifying the type(s) that the original function can return. A common use case is to have functions that return text. For these, you can pass the `str` type to `keep_lazy` (or use the [`keep_lazy_text()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.functional.keep_lazy_text "django.utils.functional.keep_lazy_text") decorator described in the next section).
Using this decorator means you can write your function and assume that the input is a proper string, then add support for lazy translation objects at the end.

keep_lazy_text(_func_)[[source]](https://docs.djangoproject.com/en/5.0/_modules/django/utils/functional/#keep_lazy_text)[¶](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.functional.keep_lazy_text "Link to this definition")

A shortcut for `keep_lazy(str)(func)`.
If you have a function that returns text and you want to be able to take lazy arguments while delaying their evaluation, you can use this decorator:
```
from django.utils.functional import keep_lazy, keep_lazy_text


# Our previous example was:
@keep_lazy(str)
def fancy_utility_function(s, *args, **kwargs): ...


# Which can be rewritten as:
@keep_lazy_text
def fancy_utility_function(s, *args, **kwargs): ...

```
