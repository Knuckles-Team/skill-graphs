## Writing custom template filters[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#writing-custom-template-filters "Link to this heading")
Custom filters are Python functions that take one or two arguments:
  * The value of the variable (input) – not necessarily a string.
  * The value of the argument – this can have a default value, or be left out altogether.


For example, in the filter `{{ var|foo:"bar" }}`, the filter `foo` would be passed the variable `var` and the argument `"bar"`.
Since the template language doesn’t provide exception handling, any exception raised from a template filter will be exposed as a server error. Thus, filter functions should avoid raising exceptions if there is a reasonable fallback value to return. In case of input that represents a clear bug in a template, raising an exception may still be better than silent failure which hides the bug.
Here’s an example filter definition:
```
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, "")

```

And here’s an example of how that filter would be used:
```
{{ somevariable|cut:"0" }}

```

Most filters don’t take arguments. In this case, leave the argument out of your function:
```
def lower(value):  # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()

```

### Registering custom filters[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#registering-custom-filters "Link to this heading")

django.template.Library.filter()[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#django.template.Library.filter "Link to this definition")

Once you’ve written your filter definition, you need to register it with your `Library` instance, to make it available to Django’s template language:
```
register.filter("cut", cut)
register.filter("lower", lower)

```

The `Library.filter()` method takes two arguments:
  1. The name of the filter – a string.
  2. The compilation function – a Python function (not the name of the function as a string).


You can use `register.filter()` as a decorator instead:
```
@register.filter(name="cut")
def cut(value, arg):
    return value.replace(arg, "")


@register.filter
def lower(value):
    return value.lower()

```

If you leave off the `name` argument, as in the second example above, Django will use the function’s name as the filter name.
Finally, `register.filter()` also accepts three keyword arguments, `is_safe`, `needs_autoescape`, and `expects_localtime`. These arguments are described in [filters and auto-escaping](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#filters-auto-escaping) and [filters and time zones](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#filters-timezones) below.
### Template filters that expect strings[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#template-filters-that-expect-strings "Link to this heading")

django.template.defaultfilters.stringfilter()[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#django.template.defaultfilters.stringfilter "Link to this definition")

If you’re writing a template filter that only expects a string as the first argument, you should use the decorator `stringfilter`. This will convert an object to its string value before being passed to your function:
```
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def lower(value):
    return value.lower()

```

This way, you’ll be able to pass, say, an integer to this filter, and it won’t cause an `AttributeError` (because integers don’t have `lower()` methods).
### Filters and auto-escaping[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#filters-and-auto-escaping "Link to this heading")
When writing a custom filter, give some thought to how the filter will interact with Django’s auto-escaping behavior. Note that two types of strings can be passed around inside the template code:
  * **Raw strings** are the native Python strings. On output, they’re escaped if auto-escaping is in effect and presented unchanged, otherwise.
  * **Safe strings** are strings that have been marked safe from further escaping at output time. Any necessary escaping has already been done. They’re commonly used for output that contains raw HTML that is intended to be interpreted as-is on the client side.
Internally, these strings are of type [`SafeString`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.safestring.SafeString "django.utils.safestring.SafeString"). You can test for them using code like:
```
from django.utils.safestring import SafeString

if isinstance(value, SafeString):
    # Do something with the "safe" string.
    ...

```



Template filter code falls into one of two situations:
  1. Your filter does not introduce any HTML-unsafe characters (`<`, `>`, `'`, `"` or `&`) into the result that were not already present. In this case, you can let Django take care of all the auto-escaping handling for you. All you need to do is set the `is_safe` flag to `True` when you register your filter function, like so:
```
@register.filter(is_safe=True)
def myfilter(value):
    return value

```

This flag tells Django that if a “safe” string is passed into your filter, the result will still be “safe” and if a non-safe string is passed in, Django will automatically escape it, if necessary.
You can think of this as meaning “this filter is safe – it doesn’t introduce any possibility of unsafe HTML.”
The reason `is_safe` is necessary is because there are plenty of normal string operations that will turn a `SafeData` object back into a normal `str` object and, rather than try to catch them all, which would be very difficult, Django repairs the damage after the filter has completed.
For example, suppose you have a filter that adds the string `xx` to the end of any input. Since this introduces no dangerous HTML characters to the result (aside from any that were already present), you should mark your filter with `is_safe`:
```
@register.filter(is_safe=True)
def add_xx(value):
    return "%sxx" % value

```

When this filter is used in a template where auto-escaping is enabled, Django will escape the output whenever the input is not already marked as “safe”.
By default, `is_safe` is `False`, and you can omit it from any filters where it isn’t required.
Be careful when deciding if your filter really does leave safe strings as safe. If you’re _removing_ characters, you might inadvertently leave unbalanced HTML tags or entities in the result. For example, removing a `>` from the input might turn `<a>` into `<a`, which would need to be escaped on output to avoid causing problems. Similarly, removing a semicolon (`;`) can turn `&amp;` into `&amp`, which is no longer a valid entity and thus needs further escaping. Most cases won’t be nearly this tricky, but keep an eye out for any problems like that when reviewing your code.
Marking a filter `is_safe` will coerce the filter’s return value to a string. If your filter should return a boolean or other non-string value, marking it `is_safe` will probably have unintended consequences (such as converting a boolean False to the string ‘False’).
  2. Alternatively, your filter code can manually take care of any necessary escaping. This is necessary when you’re introducing new HTML markup into the result. You want to mark the output as safe from further escaping so that your HTML markup isn’t escaped further, so you’ll need to handle the input yourself.
To mark the output as a safe string, use [`django.utils.safestring.mark_safe()`](https://docs.djangoproject.com/en/5.0/ref/utils/#django.utils.safestring.mark_safe "django.utils.safestring.mark_safe").
Be careful, though. You need to do more than just mark the output as safe. You need to ensure it really _is_ safe, and what you do depends on whether auto-escaping is in effect. The idea is to write filters that can operate in templates where auto-escaping is either on or off in order to make things easier for your template authors.
In order for your filter to know the current auto-escaping state, set the `needs_autoescape` flag to `True` when you register your filter function. (If you don’t specify this flag, it defaults to `False`). This flag tells Django that your filter function wants to be passed an extra keyword argument, called `autoescape`, that is `True` if auto-escaping is in effect and `False` otherwise. It is recommended to set the default of the `autoescape` parameter to `True`, so that if you call the function from Python code it will have escaping enabled by default.
For example, let’s write a filter that emphasizes the first character of a string:
```
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(needs_autoescape=True)
def initial_letter_filter(text, autoescape=True):
    first, other = text[0], text[1:]
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = "<strong>%s</strong>%s" % (esc(first), esc(other))
    return mark_safe(result)

```

The `needs_autoescape` flag and the `autoescape` keyword argument mean that our function will know whether automatic escaping is in effect when the filter is called. We use `autoescape` to decide whether the input data needs to be passed through `django.utils.html.conditional_escape` or not. (In the latter case, we use the identity function as the “escape” function.) The `conditional_escape()` function is like `escape()` except it only escapes input that is **not** a `SafeData` instance. If a `SafeData` instance is passed to `conditional_escape()`, the data is returned unchanged.
Finally, in the above example, we remember to mark the result as safe so that our HTML is inserted directly into the template without further escaping.
There’s no need to worry about the `is_safe` flag in this case (although including it wouldn’t hurt anything). Whenever you manually handle the auto-escaping issues and return a safe string, the `is_safe` flag won’t change anything either way.


Warning
Avoiding XSS vulnerabilities when reusing built-in filters
Django’s built-in filters have `autoescape=True` by default in order to get the proper autoescaping behavior and avoid a cross-site script vulnerability.
In older versions of Django, be careful when reusing Django’s built-in filters as `autoescape` defaults to `None`. You’ll need to pass `autoescape=True` to get autoescaping.
For example, if you wanted to write a custom filter called `urlize_and_linebreaks` that combined the [`urlize`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-urlize) and [`linebreaksbr`](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#std-templatefilter-linebreaksbr) filters, the filter would look like:
```
from django.template.defaultfilters import linebreaksbr, urlize


@register.filter(needs_autoescape=True)
def urlize_and_linebreaks(text, autoescape=True):
    return linebreaksbr(urlize(text, autoescape=autoescape), autoescape=autoescape)

```

Then:
```
{{ comment|urlize_and_linebreaks }}

```

would be equivalent to:
```
{{ comment|urlize|linebreaksbr }}

```

### Filters and time zones[¶](https://docs.djangoproject.com/en/5.0/howto/custom-template-tags/#filters-and-time-zones "Link to this heading")
If you write a custom filter that operates on `expects_localtime` flag set to `True`:
```
@register.filter(expects_localtime=True)
def businesshours(value):
    try:
        return 9 <= value.hour < 17
    except AttributeError:
        return ""

```

When this flag is set, if the first argument to your filter is a time zone aware datetime, Django will convert it to the current time zone before passing it to your filter when appropriate, according to [rules for time zones conversions in templates](https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/#time-zones-in-templates).
